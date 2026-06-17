# Manual técnico — LifeMap Laboratory

> Manual para um humano perceber como a app está feita: o que é, como correr, a
> arquitetura, o modelo de dados, e como a estender. Tudo aqui foi verificado contra
> o código de `lifemap_lab.html` (v12). Onde algo não foi confirmado, está marcado
> `[A CONFIRMAR]`.

---

## 1. O que é

**Life Map Laboratory** é um editor interativo de **taxonomias hierárquicas** de várias
áreas da vida/trabalho. Permite ver e editar cada estrutura como **árvore** ou como
**mind map**, anotar nós, exportar/importar em Markdown e guardar versões.

É uma **app single-file**: tudo (HTML + CSS + JavaScript) vive em `lifemap_lab.html`.
Não há build, não há dependências externas, não há framework.

---

## 2. Como correr

1. Abrir `lifemap_lab.html` num browser moderno (duplo-clique chega).
2. Não é preciso servidor, Node, nem instalação.

> **Persistência — ler com atenção.** A app **não grava em disco nem em `localStorage`**.
> Todo o estado vive em memória da página. O botão **"Guardar / Versões"** cria snapshots
> **só em memória** (array `s.saves`). **Fechar/recarregar o separador apaga essas versões**
> e a app volta às estruturas originais embebidas no código.
>
> A **única** forma de persistir trabalho é **exportar para `.md`** (botão *Download .md*
> ou copiar para o clipboard) e mais tarde **Importar MD** / **Editar MD** para recarregar.

---

## 3. Estrutura de ficheiros do projeto

| Ficheiro | Papel |
|---|---|
| `lifemap_lab.html` | A app (v12). **Editar sempre este ficheiro.** |
| `icloud_mail_editor.html` | App **separada e independente** (editor de mail iCloud). Não partilha código. |
| `.Old/lifemap_lab_v*.html` | Arquivo histórico de versões (v2, v4–v11; não existe v3). |
| `docs/` | Documentação (este manual). |
| `CLAUDE.md`, `context.md`, `handoff.md`, `memory.md`, `roadmap.md` | Configuração/continuidade para o Claude Code (ver `CLAUDE.md`). |
| `.gitignore` | Ignora `logs/` e `SessionTranscripts/`. |

---

## 4. Arquitetura da app

### 4.1 Camadas (todas dentro de `lifemap_lab.html`)
1. **`<style>`** — tema escuro azul via CSS variables (`:root`), classes para tabs,
   árvore, mind map, modais.
2. **`<body>`** — barra de tabs + um painel por tab + um painel "Side by Side" + modais.
3. **`<script>`** (começa em ~linha 640) — dados embebidos, estado, parsing MD,
   render de árvore, render de mind map (SVG), import/export, utils, e o boot no fim.

### 4.2 Os 5 separadores (tabs)
| Tab | Cor | Conteúdo |
|---|---|---|
| `lifemap` | verde `#4ade80` | Mapa de vida (fonte canónica) |
| `icloud` | azul `#7eb8f0` | Estrutura de pastas de mail (tem pastas de sistema) |
| `notion` | roxo `#bb86fc` | Mapa do workspace Notion |
| `obsidian` | rosa `#f472b6` | Vault de IA / organização do conhecimento |
| `side` | laranja `#f0a830` | Vista lado-a-lado das 4 tabs acima |

`const TABS = ['lifemap','icloud','notion','obsidian']` é a lista canónica que dirige
quase tudo. O "side" é uma vista derivada, não está em `TABS`.

### 4.3 Dados embebidos (a "fonte original")
Cada mapa nasce de uma **constante string Markdown** no topo do script:
`LIFEMAP_MD`, `ICLOUD_MD`, `NOTION_MD`, `OBSIDIAN_MD`. São convertidas para listas planas:
`LIFEMAP_DATA = parseMdToFlat(LIFEMAP_MD)`, etc. `getRawData(tabId)` devolve a lista certa.

> Nota: `ICLOUD_DATA` é parseada com `parseMdToFlat(ICLOUD_MD, true)` (`keepNum=true`,
> mantém prefixos numéricos). `NOTION_MD` usa um heading diferente (`# NOTION - v2`) que
> **não** casa com `parseMdHeading` (que só reconhece `# Versao …`) — inconsistência menor real.

### 4.4 Pipeline de dados (MD → árvore)
```
string MD  ──parseMdToFlat──▶  flat [{id, name}]  ──buildTreeFromFlat──▶  árvore de nós
```
- **`parseMdToFlat(raw, keepNum)`** ([lifemap_lab.html:1803](../lifemap_lab.html:1803)):
  lê bullets, calcula indentação (espaço=+1, tab→múltiplo de 4), ignora linhas `#`,
  limpa marcadores (`- * • ► ▸ └ ├`) e o sufixo `✨`. Constrói o `id` de cada nó como
  `idDoPai + PATH_SEP + nome`. Empilha por indentação para descobrir o pai.
- **`PATH_SEP = ''`** ([lifemap_lab.html:645](../lifemap_lab.html:645)): o separador de path é
  **string vazia** — escolhido para permitir nomes com `/` (ex.: "R/C Esq"). O `id` é, na
  prática, a concatenação dos nomes dos ancestrais.
- **`buildTreeFromFlat(flat, tabId, preserveOrder, sep)`** ([lifemap_lab.html:1186](../lifemap_lab.html:1186)):
  cria nós `{id:'n_<tab>_<n>', originalId, name, isSystem, children:[]}` e liga cada nó ao
  pai. `preserveOrder=true` mantém a ordem do MD; para `icloud`, marca pastas de sistema
  via `SYSTEM_FOLDERS_ICLOUD`.

### 4.5 Modelo de estado (tudo em memória)
- **`tabState[tabId]`** ([lifemap_lab.html:1209](../lifemap_lab.html:1209)): por tab guarda
  `tree`, `notes`, `changelog`, `expanded` (Set), `selected`, `saves[]`, `saveCounter`,
  `currentSaveId`, `idCounter`, etc.
- **Objetos por-tab ao nível do módulo** (mind map): `mmExpanded`, `mmPos`, `lastPos`,
  `mmColor`, `mmLayout`, `mmSide`, `mmView`, `MM_TITLE`, `sideExpanded`.
  **Regra de ouro:** para um `tabId` existir, tem de estar registado em **todos** estes.

### 4.6 Vistas
- **Árvore** (`renderTab`/`renderTree`, [lifemap_lab.html:1254](../lifemap_lab.html:1254)):
  hierarquia colapsável, pesquisa, ícone de nota, painel direito com path/ações/nota,
  changelog. Expandir/colapsar por nível (`expandToLevel`, `collapseBelow`).
- **Mind map** (`renderMindmap`, [lifemap_lab.html:1486](../lifemap_lab.html:1486)) em **SVG**:
  - dois layouts: **estrela** (`buildMmStar`) e **horizontal** (`buildMmHorizontal`);
  - **arrastar** nós move a subárvore; arrastar a **linha** move os filhos;
  - **zoom** com scroll, **pan** com botão direito (`mmView` guarda z/vx/vy);
  - **flip** de lado de um ramo (`flipMmSide`, badge ⇄);
  - **cor por nó** que herda nos descendentes (`mmColor`, paletas `MM_PALETTE`/`MM_COLOR_PALETTE`).
- **Side by Side** (`refreshSide`, [lifemap_lab.html:1707](../lifemap_lab.html:1707)):
  itera `TABS` e desenha as 4 árvores em colunas; usa `sideExpanded` (estado independente).

### 4.7 Import / Export / Editar MD
- **Exportar** (`generateExportFrom`, [lifemap_lab.html:1829](../lifemap_lab.html:1829)) produz
  **exatamente**: `# Versao <V>` + `# Estrutura` + uma lista de bullets (2 espaços/nível),
  nomes **sem numeração**. Nada mais.
- **Importar** (`doImport`, [lifemap_lab.html:1827](../lifemap_lab.html:1827)) e **Editar MD**
  (`openEditMdModal`/`doEditMdSave`) substituem a árvore atual a partir de texto MD.
- **Saída para disco**: `doDownload` (data-URI `.md`) e `doCopy` (clipboard).

### 4.8 Boot
No fim do script: `TABS.forEach(initTab); TABS.forEach(renderTab);`
([lifemap_lab.html:1845](../lifemap_lab.html:1845)). Sem leitura de storage — recomeça sempre dos originais.

---

## 5. Formato Markdown canónico (input/output da app)

```
# Versao v1
# Estrutura

- 🏠 CATEGORIA
  - Subcategoria
    - Item        (2 espaços de indentação = 1 nível)
```
Regras: heading `# Versao <V>` + heading `# Estrutura` + **uma única lista de bullets**;
2 espaços por nível; emoji opcional como prefixo; **sem numeração** (`1`, `1.1`, …);
nada de outros headings ou código.

---

## 6. Como adicionar um novo mapa (tab)

Receita (já validada quando se acrescentou o Obsidian na v12 — ver
`~/.claude/plans/ve-o-artefacto-v4-lucky-frost.md`). **Não é preciso lógica nova**, porque
todo o render é parametrizado por `tabId`:

1. **Dados**: adicionar `const XPTO_MD = \`# Versao v1 …\`` e `const XPTO_DATA = parseMdToFlat(XPTO_MD)`.
2. **`getRawData`**: adicionar `if (tabId==='xpto') return XPTO_DATA;`.
3. **Estado**: registar a chave `xpto` em **todos** os literais por-tab: `TABS`, `tabView`,
   `sideExpanded`, `mmExpanded`, `mmPos`, `lastPos`, `mmColor`, `mmLayout`, `mmSide`,
   `mmView`, `MM_TITLE`.
4. **CSS**: `.tab-btn.tab-xpto.active{color:#COR;border-bottom-color:#COR}` e `.side-col-title.xx`.
5. **HTML**: botão na `.tabs-bar`; clonar o painel de outra tab trocando ids; clonar a coluna
   em `#panel-side`.
6. **Título**: atualizar `<title>` e `app-sub`.

---

## 7. Versionamento e workflow de desenvolvimento

- **Editar sempre `lifemap_lab.html`.** Não criar novos `lifemap_lab_vN.html` (o esquema
  antigo). As versões antigas estão em `.Old/`.
- **Versionar por commits git** no repo `LifeMapEditor` (remote em GitHub).
- **GitHub Pages foi abandonado por privacidade** — não há `index.html` nem hook (foram
  adicionados e depois removidos; ver `memory.md`).
- **Validar o JS embebido** depois de mexer no `<script>`:
  ```
  node -e "new Function(require('fs').readFileSync('lifemap_lab.html','utf8').match(/<script>([\s\S]*)<\/script>/)[1]); console.log('JS OK')"
  ```
- Historicamente as alterações grandes faziam-se via scripts `_patch_vN.js` (regex/split-join)
  + validação acima; os patches eram temporários e apagados (não estão no repo).

---

## 8. Arquitetura de configuração & continuidade (Claude Code)

Para além da app, o projeto tem uma **camada de configuração** que dá memória e disciplina ao
agente Claude Code entre sessões. Foi montada na sessão de setup (commit `Setup-ClaudeCode`).

### 8.1 Ficheiros e papéis
| Ficheiro | Papel | Quando muda |
|---|---|---|
| `CLAUDE.md` | Regras do projeto + protocolos de arranque/fecho + guidelines. É lido pelo agente em cada sessão. | Raramente (quando mudam regras). |
| `context.md` | **SSOT** acumulado (arquitetura, decisões, convenções, estado). Cresce no tempo. | Em cada fecho. |
| `handoff.md` | Estado **imediato** para a próxima sessão (telegráfico). | Reescrito em cada fecho. |
| `memory.md` | O **porquê** das decisões (D1, D2, …). Não é estado corrente. | Quando há decisão nova. |
| `roadmap.md` | Rumo/marcos (processo + futura app). | Quando o rumo evolui. |
| `CHANGELOG.md` | Alterações **visíveis da app**, por versão (registo de produto). | Quando se mexe na app. |
| `docs/MANUAL.md` | Este manual (para humanos). | Quando a app/projeto muda. |
| `.claude/settings.json` | Config partilhada (permissões; hoje só git read-only). Versionado. | Por decisão do utilizador. |
| `.claude/settings.local.json` | Permissões locais da máquina. **Fora do git.** | Automático/local. |

### 8.2 O ciclo de continuidade
```
        ┌─────────────── ARRANQUE ───────────────┐
        │ 1. ler handoff.md                       │
        │ 2. ler context.md + roadmap.md          │
        │ 3. verificar alinhamento → assinalar    │
        │    discrepâncias ao utilizador          │
        │ 4. NÃO ler SessionTranscripts/          │
        └──────────────────┬──────────────────────┘
                           ▼
                      [ trabalho ]
                           ▼
        ┌─────────────────── FECHO ───────────────┐
        │ atualizar context / memory / roadmap     │
        │ + CHANGELOG (se mexeu na app)            │
        │ reescrever handoff.md (telegráfico)      │
        │ perguntar nome da sessão → "SX - Título" │
        │ registar SX (anterior = S(X-1))          │
        │ perguntar se grava transcript → ZIP em   │
        │ SessionTranscripts/ "SX - Título.zip"    │
        └──────────────────────────────────────────┘
```
Detalhe normativo: ver `CLAUDE.md` (secções *Arranque* e *Continuidade entre sessões*).

### 8.3 Privacidade
- `SessionTranscripts/` e `logs/` estão **fora do git** (`.gitignore`).
- O agente está **proibido de ler `SessionTranscripts/`** salvo indicação explícita.
- A app **não é publicada** (GitHub Pages foi abandonado por privacidade — `memory.md` D7).

### 8.4 Disciplina do agente
`CLAUDE.md` embebe guidelines (pensar antes de codificar, simplicidade, mudanças cirúrgicas,
execução orientada a objetivos) para reduzir erros comuns de LLM. Ao mexer no `<script>` da
app, validar sempre o JS com o comando `node -e` (manual §7).

## 9. Notas / dívida técnica observada

- `addPermanentSave` ([lifemap_lab.html:1219](../lifemap_lab.html:1219)) está definida mas
  **parece não ter call-site** (código morto). Mencionado para referência — não remover sem pedido.
- `NOTION_MD` usa heading `# NOTION - v2` em vez de `# Versao …`, logo a versão não é
  reconhecida por `parseMdHeading`.
- Sem persistência: qualquer trabalho não exportado para `.md` perde-se ao recarregar.
- `icloud_mail_editor.html` é um artefacto à parte; não confundir com a tab `icloud` da app.
