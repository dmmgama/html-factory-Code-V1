# TableEditor — Claude Code

## Contexto
Editor de tabelas tipo-Excel que corre no browser, **standalone e auto-contido nesta pasta**. É uma app **multi-tabela** (vários "projectos"). Tem um único script de apoio — `acc_server.py` (Python stdlib, porta 8765) — que é só a **camada de autosave/persistência local** enquanto o HTML está aberto.

> **Só interessa o que está nesta directoria.** A app não tem integração com nenhum sistema externo. Os scripts em `..\..\..\codigo\` (acc_core.py, acc_download.py, etc.) **não pertencem a esta app** — ignorar.
>
> Nota sobre `.claudeignore`: a working directory **é** esta pasta, por isso Bash, Read/Edit/Write funcionam todos normalmente aqui. (A regra "o Bash não acede a `.claudeignore`" vinha do contexto Cowork, que corria noutra pasta e descia para dentro de `.claudeignore` — não se aplica a este setup.)

Ficheiro principal: `MembrosInfo_Editor.html` (~2340 linhas, JS vanilla, sem build, sem dependências).

## Como correr e testar
- **Arrancar servidor:** `Iniciar_Servidor.bat` — corre `acc_server.py` com o Python do sistema (`py`, fallback `python`). **Sem venv, sem pip** (stdlib puro) → folder auto-contido; só precisa de um Python instalado no Windows. O `.bat` força `PYTHONUTF8=1`/`PYTHONIOENCODING=utf-8` — necessário, senão o servidor crasha no banner (`─`) numa consola Windows cp1252. Se correres `py acc_server.py` à mão, define esse env primeiro.
- Servidor em `http://localhost:8765`. `GET /ping` deve devolver `{ok:true,...}`.
- **Abrir a app:** abrir `MembrosInfo_Editor.html` no browser com o servidor a correr.
- **Testar:** não há test suite. Testar a sério = usar a app no browser e observar o comportamento + os ficheiros de autosave gerados. Type-check/lint não existem.
- **Preview via MCP (agente):** o `acc_server.py` (8765) **só serve a API, não o HTML**. Para abrir no browser do preview, servir a pasta à parte (ex.: `py -m http.server 8080 --directory <pasta>`, via `.claude/launch.json`) e navegar para `http://localhost:8080/MembrosInfo_Editor.html`, com o `acc_server.py` também a correr. (O `.claude/` está gitignored.)

## Modelo multi-tabela + classes A/B/C (rearquitectura — fonte única)
A app gere vários projectos/tabelas (botão "Nova tabela" → `createTable`). **Regra-mãe: cada informação tem UM lar (sem duplicação).** Três classes:
- **Classe A — dados + organização da tabela** (viaja com a tabela): `data`, `schema` (colunas+ordem, `fixed`/`hidden` da grelha, `categories`), `groupBy`, `sortHierarchy`, `fieldLinks`, `colSort`, `sortOptsEnabled`. **Lar:** o autosave de dados (envelope) e o ficheiro de dados no "Gravar".
- **Classe B — config de máquina** (local, por destino; não viaja): mirror path/`mirrorWithNum`, `saveFormatMirror` (vestígio), **`channels`** (composição export/mirror), índice global (`activeTable`, `workDir`). **Lar:** config por projecto.
- **Classe C — prefs internas da app** (`x-tableeditor`): `colSort`/`sortOptsEnabled`/`sortHierarchy` verbatim (para I2). Só no autosave; **nunca** no export/mirror.

> **`type` NÃO é propriedade da tabela** — é decisão de **canal de saída** (export/mirror), classe B. O `schema.fields` da tabela só tem `name`/`fixed`/`hidden`/`categories`.

### Storage em disco (`.tableeditor/`, gitignored)
- `.tableeditor/index.json` — global: `workDir`, `activeTable`, `tables[{id,name,file}]`, misc.
- `.tableeditor/<id>.config.json` — config de máquina por projecto (classe B): `mirror`, `mirrorWithNum`, `saveFormatMirror`, `channels`.
- `.tableeditor/<id>.autosave.json` — autosave de dados por projecto (envelope, classe A).
- **Ficheiros de DADOS versionáveis** (ex.: `CompaniesInfo.json`) ficam na **workDir** (limpos).
- O servidor migra 1x o `_editor_config.json` legado → split (→ `_editor_config.json.bak`).

## Persistência — o que o servidor grava
A cada poucos segundos (`persistLS`, debounce 2s) e em acções (gravar/trocar de tabela):
1. **Autosave de dados** → `.tableeditor/<id>.autosave.json` = **envelope canónico (lossless)** (`stateToEnvelope`). Fonte de restauro.
2. **Mirror opcional** → no `serverSave`/"Gravar", grava a composição do **canal `mirror`** (`composeChannel`) num path à escolha. Pré-composto → o servidor grava verbatim (`mirrorIsEnvelope:true`).
3. **Config de máquina** → `.tableeditor/<id>.config.json` (classe B). **Save grava só o ficheiro da tabela ACTIVA** (sem ficheiros órfãos).

Fallback: `localStorage` (`LS_KEY = tableeditor_state_v6`) guarda o envelope. Ordem no `init`: autosave do servidor → localStorage → ficheiro de dados.

> ### Restauro lossless = do PAR (dados + config) — não do envelope sozinho
> O round-trip lossless cobre a **classe A** (dados+organização), a partir do par autosave-de-dados + config. **Não** cobre a classe B (perder o caminho/formato do mirror ou os type/fixed/hidden de saída ao abrir noutra máquina é correcto — são locais).
> ⚠️ **Cuidado ao testar no browser:** o `render()` dispara `persistLS` (autosave 2s). Testar com a app aberta **escreve** no `.tableeditor/<id>.autosave.json`. A fonte de recuperação é o ficheiro de dados (só escrito no "Gravar").

> O `Rules\CompaniesInfo.json` que aparece como mirror é só **um caminho custom que o David escolheu** — não tem nada de especial e não é integração com nada. O mirror pode apontar para qualquer sítio.

## Arquitectura — Servidor (`acc_server.py`)
**Multi-thread** (`ThreadingHTTPServer`) — um `/save` lento (mirror no Google Drive) não bloqueia o `/ping`. Endpoints inalterados na assinatura: `GET /ping /config /load /autosave-load /list /tables` · `POST /config /save /autosave /set-workdir /set-mirror /tables/save /tables/new` · `DELETE /tables/file`.
- **Storage repartido (A3-ii):** `load_config()`/`save_config()` apresentam um dict **unificado** (endpoints e cliente inalterados) mas leem/escrevem o layout `.tableeditor/` (index + `<id>.config.json` + `<id>.autosave.json`). `autosave_path(id)`, `_migrate_if_needed()` (migra o legado 1x), `_write_index_and_configs()`. `TABLE_CFG_KEYS` = classe B (`mirror`,`mirrorWithNum`,`saveFormatMirror`,`channels`).
- `/save` recebe `{filename, data, mirrorData?, mirrorIsEnvelope?}`: grava `data` (envelope) na workDir e `mirrorData` (pré-composto pelo canal) no mirror path. **Gate `mirrorIsEnvelope`:** se `true`, o servidor grava o mirror **verbatim** (salta `add_num`/`strip_num`). `safe_name` impede path traversal.

## Arquitectura — Frontend (`MembrosInfo_Editor.html`)
**Estado em memória** (inalterado — abordagem de fronteira): `columns:[{label,hidden,fixed}]`, `rows:[{<label>:val}]`, `groupLevels:[]`, `colSort:{}`, `sortOptsEnabled:bool`, `sortHierarchy:[{label,dir}]`, `saveFormatMirror`, `fieldLinks:[{parent,children:[]}]`. (`saveFormatAutosave` é vestígio.)

> ### ⭐ Formato canónico = envelope Frictionless (SPEC) — não reverter sem pedido
> O JSON que a app **grava/autosave/importa** é o **envelope Frictionless** definido em `docs/SPEC-TableEditor-Formato-Dados.md` (ler antes de mexer em serialização). Forma: `{ profile:"tabular-data-resource", name, savedAt, schema:{fields:[{name,fixed,hidden,categories?}],primaryKey,fieldLinks:[{parent,children,semantics}]}, view:{groupBy,sortHierarchy:[{field,by}]}, "x-tableeditor":{colSort,sortOptsEnabled,sortHierarchy}, data:[{<field>:val}] }`. **Sem `type` no schema da tabela** (type é decisão de canal de saída). Export/mirror usam `composeChannel` (à la carte), não o envelope canónico.
> **Abordagem de fronteira:** os globais em memória ficam como estão; traduz-se só nas pontas via `stateToEnvelope()`/`envelopeToState()` (a ÚNICA fronteira). `data` é **sempre plano/completo/lossless, sem `#` nem `_selected`**. Invariantes (SPEC §3): **I1** data não depende de schema/view/x-*; **I2** round-trip lossless (garantido por `x-tableeditor` guardar `colSort`+`sortOptsEnabled`+`sortHierarchy` verbatim); **I3** dados nunca em chaves de objecto. `semantics` default dos fieldLinks = `'platform-identifier'` (SPEC §5.3). Blocos `x-<destino>` (ex.: `x-notion`) são preservados verbatim no round-trip via o global `xExtensions`.

Variáveis de estado globais: `columns`, `rows`, `groupLevels`, `colSort`, `sortOptsEnabled`, `sortHierarchy`, `saveFormatMirror`, `jsonPreviewMode`, `jsonViewMode` (`protocolar`|`humano`), `xExtensions`, `fieldLinks`, `activeTableId`, `tablesConfig`, `serverOnline`. (`saveFormatAutosave` vestígio.)

### Dois modos de ordenação
- **MODE OFF** (`sortOptsEnabled=false`): `getSortedRows()` devolve `rows` tal-qual (ordem de inserção/drag). Aplicar um sort popup (`applySortPopup`) **reordena fisicamente** o array `rows`.
- **MODE ON** (`sortOptsEnabled=true`, `sortHierarchy=[...]`): `getSortedRows()` computa um sort multi-nível **sem mutar** `rows`; desligar restaura a ordem física.

### Duas vistas (Protocolar/Humano) + dois formatos Humano
- **Protocolar** = o envelope canónico (`stateToEnvelope`). É a vista importável/lossless; única que aceita import (paste/Aplicar). `jsonViewMode='protocolar'`.
- **Humano** (`stateToHumano` → `getFormattedData`) = projecção derivada, **só leitura** (textarea `readOnly`, import bloqueado). Sub-formatos:
  - **A — "Tabela"** (`getTableFormatData`): MODE ON agrupa por `sortHierarchy`; OFF flat.
  - **B — "Export JSON"** (`getExportFormatData`): agrupa por `groupLevels` (tab Opções), independente do sort. Formato dos botões Export/Copy.
- **Fronteira I3:** o agrupamento Humano (vista no ecrã) põe o valor de grupo como CHAVE; o `data` do envelope/canais é SEMPRE plano e **nunca** passa por `buildGrouped`/`applyFieldLinksToRow`.

### Canais de saída (export / mirror) — composição à la carte (classe B)
O que o **export** e o **mirror** produzem é escolhido **por canal** (`composeChannel`), guardado no per-project config (`tablesConfig[].channels{export,mirror}`):
- `parts`: `schema` (colunas+ordem) / `types` (`type`/`fixed`/`hidden` por coluna; "" = não definido) / `view` (groupBy+sortHierarchy declarativo) — sim/não cada.
- `destino`: bloco `x-<destino>` opcional. **`x-excel`** implementado (`buildXDestino`: format/hidden/largura/congelar-1ª/cor). Destinos extensíveis por passthrough genérico (sem lista fechada).
- Sem schema/view/destino = **só dados crus** (array nu). `data` SEMPRE plano. **Nunca** sai `x-tableeditor`.
- UI: tab Config "Canais de saída" (`renderChannels`/`channelFromUI`/`saveChannels`). `serverSave` grava `mirror = composeChannel(canal mirror)`; `exportJSON/MD/CSV` usam o canal `export`. `categories` vem do custom-sort (`colSort.order`).
- **Import:** `parseCSV` (`.csv` aceite); `ingestJSON` pergunta antes de esmagar definições; tipos de origem → `x-import.fieldTypes` (não herdados).

### Grouping + dedup (T1) e Field Links (T2)
- `buildGrouped`/`buildGroupedRaw`: ao agrupar por nível `lvl` fazem `delete copy[lvl]` antes de recursar — o campo de agrupamento só aparece como chave do grupo, não dentro dos filhos.
- `fieldLinks` aninham `parent → children`: `{"Company":"X","ID":"1"}` → `{"Company":{"value":"X","ID":"1"}}`. Aplicado por `applyFieldLinksToRow`. Validações (`validateLink`): pai≠filho, filho não pode ser pai, filho não pode ser campo de group-by, sem ciclos, 1 nível só, sem pai duplicado.

### UI (painel direito — 4 tabs)
`tab-json` (preview/import + toggle **Protocolar/Humano** + sub-toggle A/B só em Humano + prompt-LLM), `tab-opts` (colunas, ordenação hierárquica, agrupamento, field links, export), `tab-tables` (lista de tabelas, nova/remover/apagar), `tab-config` (workDir, mirror, formato do mirror A/B). Savebar: `save-filename`, Gravar (`serverSave`), Carregar (`serverLoad`), Importar (`importFromFile`), estado do servidor, autosave-tag, Undo, Repor.

### Atalhos de teclado
Ctrl/Cmd+C / +V (copy/paste de células via clipboard TSV; fallback interno), Ctrl+A (selecionar tudo), Esc (limpar selecção), Delete (apagar linhas selecionadas), **Ctrl+S → gravar**, **Ctrl+Z → undo** (50 níveis).

### `applyState` aceita 5 formas de input
(0) **envelope Frictionless** (`isEnvelope` → `envelopeToState`) — detectado primeiro; (1) estado completo (`columns` label-keyed + `rows`); (2) legacy `col_xx`/`key` (migra, dropa `Numero`); (3) objecto agrupado export (`flattenGrouped` + `detectGroupField`); (4) array flat. As 4 legadas mantêm-se (retrocompat P5). `copyLLMPrompt` gera um prompt que produz o **envelope** (forma 0).

### Ingestão de JSON (paste / Importar / Aplicar) — `ingestJSON`
As 3 vias (paste no `#json-preview`, "Importar" `importFromFile`, "↑ Aplicar" `applyJSONFromEditor`) fazem `parseJSONLoose` (tira cercas ```json/BOM) e passam por **`ingestJSON(data)`**, que decide:
- **colunas batem** com a tabela activa (mesmos nomes+número, via `sameColumnSet`) **ou tabela activa vazia** → `applyState` **sobrepõe** a activa;
- **colunas diferentes** → `confirm` + `prompt(nome)` → **cria tabela nova** com os dados (`createTableWithData`, reutiliza os endpoints de `createTable`), sem tocar na activa; cancelar → não faz nada.
`incomingColumnLabels` extrai os labels das 5 formas (incl. envelope → `schema.fields[].name`). **Importar só em Protocolar** (Humano é só leitura). **`serverLoad`/"Carregar" NÃO passa por aqui** (carrega o ficheiro da própria tabela activa → sobrepõe sempre). Template externo que gera o JSON: `TableEditorPrompt.md` (raiz).

### Mapa de funções (nº de linha aproximado — regenerado por símbolo)
**Fronteira (de)serialização (envelope Frictionless):** `isEnvelope:576`, `stateToEnvelope:587`, `envelopeToState:652`, `rebuildColSortFromCategories:691`, `stateToHumano:2239`. (`stateToJSON` removido — vestígio.)
**Estado/ingestão:** `applyState:702` (shape #0 envelope + 4 legadas), `compareByColSort:808`, `getSortedRows:825`, `parseJSONLoose:1372` (cercas ```json/BOM), `parseCSV:1381`, `incomingColumnLabels:1766`, `sameColumnSet:1792`, `ingestJSON:1801` (pergunta antes de sobrepor; tipos origem→`x-import`), `createTableWithData:1846`.
**Persistência/servidor:** `persistLS:1229`, `sanitizeTables:1291` (config só classe B), `loadServerConfig:1300`, `serverSave:1330` (mirror=composeChannel), `serverLoad:1358`, `switchTable:1599`, `createTable:1717`.
**Canais (export/mirror — classe B):** `defaultChannel:2251`, `getChannels:2254`, `composeChannel:2266`, `buildXDestino:2310`, `updateFormatUI:1472`→`renderChannels:1474`, `channelFromUI:1499`, `saveChannels:1516`, `exportJSON:2643`.
**Output/agrupamento Humano (vista no ecrã):** `getTableFormatData:2177`, `getExportFormatData:2209`, `getFormattedData:2229`, `buildGrouped:2139`, `buildGroupedRaw:2328`, `applyFieldLinksToRow:2116`, `validateLink:2092`.
**Viewer/render/colunas:** `updateJSON:2355`, `toggleJsonView:2386`, `render:1939`, `renameCol:2420`, `deleteColumn:2439`, `init:2784`.

## Regras ao alterar esta app
1. **Trabalhar SÓ nesta pasta.** A working directory é esta pasta; Bash e Read/Edit/Write funcionam normalmente (ver nota sobre `.claudeignore` no topo). Mesmo assim, manter o foco só nesta directoria.
2. **`stateToJSON` grava rows em ordem de inserção** (não ordenada) — intencional, para preservar a ordem manual. Não "corrigir".
3. **Não mexer no mecanismo de group-by** sem pedido explícito.
4. O **mirror é só um output custom** configurável por tabela — sem integração externa.
5. **Detalhe subtil:** drag/copy/paste indexam contra `getSortedRows()` e mapeiam de volta a `rows` via `rows.indexOf(row)`. Qualquer mudança no sort tem de preservar este mapeamento.
6. Ignorar `.Old\` (versões antigas v1–v4) e os scripts em `..\..\..\codigo\`.

### Invariantes a manter (não partir)
- (a) `buildGroupedRaw` espelha o strip T1 de `buildGrouped` — mudar um exige mudar o outro.
- (b) `applyFieldLinksToRow` é chamado em `buildGrouped`/`buildGroupedRaw` **e** nos paths flat de `getTableFormatData`/`getExportFormatData` — manter sincronizado em todos.
- (c) **`colSort` nunca é mutado fora de `applySortPopup`.**
- (d) Formato A vs B nunca híbrido no output (mirror/export usam sempre um ou outro, inteiros).
- (e) `renameCol`/`deleteColumn` mantêm `fieldLinks`/`colSort`/`sortHierarchy`/`groupLevels` coerentes — preservar essa limpeza ao tocar em colunas.

## Histórico
`SessaoCowork.md` (nesta pasta) = reconstituição da sessão que implementou os Formatos A/B, os dois sort modes, T1 (dedup) e T2 (field links). Consultar para **histórico**, não para estado actual — para o estado actual, ler o código.
