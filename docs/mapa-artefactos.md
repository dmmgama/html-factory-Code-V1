# Mapa dos Artefactos — html-factory (Passo 1 / M1)

> **O que é este documento.** O retrato dos artefactos existentes (`Artefactos-existentes/`)
> lido nas **3 camadas** da arquitetura-alvo — **Dados (SSOT) / Motor / Viewer** — para se ver
> *o que se repete em todos*. Esse padrão comum é a matéria-prima da **Alfândega** (o contrato
> único) que se decide no grill (Passo 2). **Não é** decisão de arquitetura — é o levantamento
> que a alimenta.
>
> Tradução civil: antes de construir a fábrica, fomos ver as peças que o David já fez à mão,
> para perceber que molde serve para todas.

## 0. Como foi feito (método e confiança)

- **5 leitores em paralelo** (`Explore`, *read-only* — não tocam nos backups), repartidos por
  clusters coerentes: Mapas/Grafos · Curador · Dossier/Fable · SSOT/TableEditor · Editores/Fichas/Lab.
- **Verificação:** um `code-reviewer` auditou as 5 afirmações mais fortes contra o código real,
  e eu li diretamente os 2 ficheiros mais centrais (`sec7-viewer.js`, `V0.json`).
- **Ruído ignorado** (não são artefactos da fábrica): `.obsidian/plugins/`, `.Old/`,
  `_checkpoints/`, `node_modules/`, `.understand-anything/`, `SessionTranscripts/`.
- **Nível de confiança:** ALTO nos ficheiros lidos/verificados; MÉDIO nos lidos por amostragem
  (ficheiros >300 KB foram lidos pelo esqueleto, não linha a linha). Correções da verificação
  estão incorporadas (ver §8).

## 1. Inventário (o "sumo")

| # | Artefacto | Cluster | Modo dominante | 1 linha |
|---|---|---|---|---|
| 1 | `MAPA-D-G-AI.html` | Mapas | **grafo** (D→G→AI) | 3 colunas de decisões/governança/ações com ligações SVG |
| 2 | `MAPA-EXPLORADOR-AI.html` | Mapas | tabela + **grafo** | "Atlas" multi-vista de 44 projetos + mindmap |
| 3 | `MAPA-INTERATIVO-AI.html` | Mapas | **grafo** 2D | distritos/tiles com pan-zoom e ligações |
| 4 | `governance-map-v2.html` | Mapas | **grafo** (Cytoscape) | grafo interativo de ficheiros/D/G/AI/falhas |
| 5 | `governance-explorer.html` | Mapas | cartões/abas | explorador de governança em 5 abas |
| 6 | `DIAGRAMA-Consolidacao-Metade-A.html` | Mapas | passos/narrativa | diagrama 5-passos com progresso |
| 7 | `projetos-curador-v3.html` ⭐ | Curador | **grafo + hierarquia** | **app principal de referência** — curadoria de 44 projetos (4 vistas, edição inline, drag-drop, genealogia, export multi-formato) |
| 8 | `understand-dashboard-v3-v2.html` | Curador | tour/cartões | explicador da arquitetura tripartida |
| 9 | `dashboard-v3.html` | Curador | documento | **mapa/orientação do curador** — declara as 3 camadas (Dados/Motor/Viewer) |
| 10 | `V0.json` | Curador | **dados puros** | SSOT exportado: 44 projetos + 30 links + 6 domínios |
| 11 | `dossier-credito-dashboard-v5.html` | Dossier | **tabela** + série | comparador de propostas de crédito (Chart.js) |
| 12 | `DIAGRAMAS-governo-dashboard.html` | Fable | **grafo** DAG (SVG) | diagrama de governo com 4 folhas, pan/zoom/tour |
| 13 | `knowledge-graph.json` | Fable | **dados puros** | grafo de conhecimento (nós+arestas tipadas) |
| 14 | `projeto-ssot/index_v11.1.html` + `js/sec7-viewer.js` | SSOT | **hierarquia** + canvas | editor estrutural Supabase + viewer Canvas separado |
| 15 | `TableEditor/MembrosInfo_Editor.html` + 3×JSON | SSOT | **tabela** | editor multi-tabela tipo Excel (envelope Frictionless) |
| 16 | `cte-index-editor-v7.html` | Editores | **árvore** | editor de índices com renumeração/drag/changelog |
| 17 | `FichaProjetosJSJ/Index_v9.1.html` + `zonas.html` | Editores | formulário + canvas | fichas de projeto (form-driven) + mapper 2D |
| 18 | `LifeMap/MapLab.html` + `icloud_mail_editor.html` | Editores | **árvore** + mindmap | editor de taxonomias multi-projeto / pastas email |
| 19 | `materia-conceptual…`, `diagnostico-…`, `inspector-toolkit/*` | Editores | documento | documentos estáticos / Markdown-em-`<script>` |

## 2. Fichas por camada (condensado)

> Legenda da coluna *Estética fora dos dados?*: **✓** = cor/tema isolados em CSS; **✗** = cor
> misturada nos dados (viola o invariante); **n/a** = documento estático.

### Cluster Mapas/Grafos
| Artefacto | Dados (SSOT) | Motor | Viewer | Estética fora? | Acoplamento |
|---|---|---|---|---|---|
| MAPA-D-G-AI | arrays `D_ITEMS/G_ITEMS/AI_ITEMS` + `CONNECTIONS[{from,to}]` | adjacência O(1), `openCardId` | DOM + **SVG** caseiro (linhas) | ✓ | baixo |
| MAPA-EXPLORADOR | `PROJ[][]` (44×11), `LINKS[from,to,tipo,ev]`, `RECON` | 8 vistas lazy, tabela sortável genérica | DOM + SVG mindmap | ✗ (`ORIG`→cor, `move/relev`) | médio |
| MAPA-INTERATIVO | `P[][]` compacto, `RELC` | layout 2D pré-calc, pan/zoom/filtros | DOM tiles + SVG linhas | ✓ | baixo |
| governance-map-v2 | `FILES/DNNN/GNNN/AINNN/MODOS_FALHA` (objetos limpos) | constrói `elements`, filtros via `cy.style()` | **Cytoscape.js** | ✓ | **muito baixo** |
| governance-explorer | arrays `GLOSSARY/PATTERNS/LAYERS/LEDGER_SCHEMA` | modo simples/técnico, abas, busca | DOM puro (cards/callouts) | ✗ (campo `cor:'emerald'`) | médio |
| DIAGRAMA-Consolidacao | `STEPS[{n,titulo,why,what,nodes[]}]` | navegação por `data-step` | DOM + CSS transições | ✓ | baixo (simples) |

### Cluster Curador
| Artefacto | Dados (SSOT) | Motor | Viewer | Estética fora? | Acoplamento |
|---|---|---|---|---|---|
| **projetos-curador-v3** ⭐ | `STATE{projetos[],links[],domainTree,domains,version}` + `localStorage["curador-projetos-ai-v3"]` | funções puras (`passesFilter/filtered/sortRows/projDomPai1/domWouldCycle/computeGroups`), ciclo **`commit()=save()+renderAll()`** | DOM (tabela) + **SVG** (grafo força/mindmap); reconstrói tudo a cada render | ⚠️ parcial (cor do nó por `estado` *hardcoded* em `renderGraph`) | **motor puro / viewer acoplado** |
| projetos-curador-v4 *(experimento)* | igual ao v3 | igual + atribuições bilaterais | + mindmap SVG nas atribuições, chips cross-link | — | **não entrou em produção** |
| understand-dashboard-v3-v2 | `TOUR_STEPS/DIAG_DATA/CAMPOS_GRID/VISTAS` | tour linear, diagrama clicável | DOM + SVG | ✓ | **muito baixo** |
| dashboard-v3 *(mapa do curador)* | hard-coded (texto) | nenhum | HTML/CSS | n/a | n/a (documento) |
| V0.json | **dados puros** (ver §3) | — | — | ✓ | — |

### Curador v3 — tratamento detalhado (app principal de referência)

> A app mais complexa e a mais relevante agora. `dashboard-v3.html` é o seu próprio mapa: declara
> **Dados** (`STATE.projetos/links/domainTree`, persiste em `localStorage`), **Motor** (funções
> puras que lêem o STATE e nunca tocam no DOM) e **Viewer** (`renderAll()` reconstrói o DOM do zero).

- **Dados (contrato real):** `projeto` = 10 campos factuais (só-leitura: `id, nome, caminho, origem,
  stack, plataformas[], git, remoto, relevancia, notasFonte`) + 10 de curadoria (editáveis:
  `interesse, dominios[], prioridade, estado, cronologia, nasceuDe, notas, tags[], domPai1Manual,
  domPaiImediatoManual`). `link` = `{id, a, b, t}` com **11 tipos** de relação. `domínio` = árvore
  (`nome → pai|null`). **Esta é a forma mais rica para o contrato de grafo da Alfândega.**
- **Motor (o melhor exemplar do Ciclo Reativo):** evento → muta `STATE` → `commit()` (=`save()` +
  `renderAll()`). Funções puras notáveis: `domWouldCycle()` (anti-ciclo na hierarquia de domínios),
  `computeGroups()` (componentes conexos do grafo), `sortRows()` (ordenação multi-nível).
- **Viewer (4 vistas):** Tabela (19 colunas, drag-reorder, edição inline) · Ligações (grafo SVG,
  modos *força* e *mind-map*, criar/apagar arestas ao clique) · Cronologia & Genealogia · Atribuições
  (drag de projetos para caixas de domínio, drill-down de subdomínios). Tudo SVG/DOM nativo — **sem
  bibliotecas**.
- **Porque é a mais complexa:** 4 vistas com estado partilhado · drag-drop em 3 contextos · grafo
  interativo com 11 tipos de aresta · hierarquia de domínios com anti-ciclo em tempo real · genealogia
  · export JSON/XLSX/CSV/MD · snapshots de versão.
- **Separação (≈60% feita):** ✅ Dados e Motor genuinamente isolados e testáveis. ❌ Viewer acoplado —
  cor do nó *hardcoded* em `renderGraph`, handlers inline recriados a cada render, render total (sem
  diffing). **O que a fábrica acrescenta:** externalizar tema, isolar o viewer atrás de uma interface,
  e (talvez) render incremental.

### Cluster Dossier/Fable
| Artefacto | Dados (SSOT) | Motor | Viewer | Estética fora? | Acoplamento |
|---|---|---|---|---|---|
| dossier-credito-v5 | `DATA` inline ~865 KB (`bancos`, `dataset`, `custos_totais`) | custo 30 anos, modos A/B/C, slider Euribor | DOM + **Chart.js** | **✗** (`color` hex nos dados) | **alto** |
| DIAGRAMAS-governo (fable) | `VIEWS[{nodes[{id,parent,level,kind,x,y,w,h,desc_tec,desc_simples}],edges}]` | render SVG, collapse, tour, técnico/simples | **SVG** gerado | ✓ | médio |
| knowledge-graph.json | **dados puros**: `nodes[{id,type,name,tags,complexity}]` + `edges[{source,target,type,weight}]` | — | — | ✓ | — |

### Cluster SSOT/TableEditor
| Artefacto | Dados (SSOT) | Motor | Viewer | Estética fora? | Acoplamento |
|---|---|---|---|---|---|
| projeto-ssot index_v11.1 | Supabase (`blocks/floors`), `actions_data` JSON = `{layers:{…[{uso,manualLoad,shapes:[[{x,y}]]}]}, blueprint}` | seletores cascata, sync Supabase | delega ao `FloorViewer` | ✓ | médio |
| `sec7-viewer.js` → **classe `FloorViewer`** | recebe via `loadData(data)`; estado local (`scale/offset/mode`) | cálculos geométricos (área, centroide, cargas) | **Canvas 2D** puro, "fachada cega" | ✓ | **baixo (na classe)** |
| TableEditor | **envelope Frictionless** `tabular-data-resource` (`schema.fields/fieldLinks`, `view.groupBy`, `x-tableeditor`) | fronteira `stateToEnvelope`/`envelopeToState`; sort físico/virtual; canais à la carte | DOM (tabela editável + tabs) | ✓ | **alto (ficheiro monolítico)** |

### Cluster Editores/Fichas/Lab
| Artefacto | Dados (SSOT) | Motor | Viewer | Estética fora? | Acoplamento |
|---|---|---|---|---|---|
| cte-index-editor-v7 | `tree[{id,title,num,type,children}]`, `notes` | renumeração (modos), drag | DOM recursivo | ✓ | baixo |
| Index_v9.1 (ficha) | **no DOM** (inputs/selects) | form-driven, Chart.js | HTML cards | ✗ (sem schema) | **alto** |
| zonas (Ficha) | `zones[{x,y,w,h,nome,cor,linkedTo}]` (inferido) | layout 2D, draw/pan/move | Canvas + sidebar | parcial (`cor` no dado) | médio |
| MapLab | `workspace{projects[{trees[{tree,notes,saves,changelog}]}]}`, `tabState[id]` | hierarquia + mindmap, classes/grupos, versões | DOM (árvore) + **SVG** (mindmap) | ✓ | médio |
| icloud_mail_editor | `tree[{id,name,children}]`, `saves[]` | hierarquia, versões, MD | DOM | ✓ | baixo |
| materia / diagnostico / inspector | estático / Markdown em `<script id="md">` | nenhum / render MD | HTML/CSS / DOM | n/a | — |

## 3. O padrão comum (a assinatura do domínio)

Apesar da variedade, **quase tudo se reduz a um de três modos** — que são exatamente os 3 modos
do Motor previstos no briefing (relações / hierarquia / tabela):

1. **GRAFO — nó + aresta tipada.** O mais frequente (8+ artefactos). Forma recorrente:
   - **Nó:** `{ id, type, label, metadata{…}, payload{…}, relations/edges }`
   - **Aresta:** `{ source/from, target/to, type, weight?, evidence? }` — sempre **tipada**
     (`depends_on/alimenta/variante-de/confirmed/plausible/broken…`).
   - Aparece em: D/G/AI maps, governance-map (Cytoscape), DIAGRAMAS-governo (DAG), curador (links),
     `knowledge-graph.json`. **O `knowledge-graph.json` é o protótipo mais limpo deste contrato.**

2. **ÁRVORE/HIERARQUIA — nó + filhos.** Forma: `{ id, name/title, children[], notes?, icon?, color? }`
   + versionamento `saves[{id,label,ts,tree,changelog}]`. Aparece em: cte-index, MapLab,
   icloud_mail, e (em dados) na cascata projeto→bloco→piso do `projeto-ssot`.

3. **TABELA — linhas + colunas + schema.** Forma canónica mais madura: **envelope Frictionless**
   do TableEditor (`schema.fields[]`, `fieldLinks` pai→filhos, `view.groupBy`, `primaryKey`).
   O dossier é uma tabela "achatada" (N bancos × modos × cenários) — mas suja (estética nos dados).

**Três coisas que aparecem em TODOS os artefactos vivos (não-documento)** — e que são, na prática,
peças da fábrica já inventadas à mão:
- **Um STATE global** (objeto único em memória, às vezes + `localStorage`).
- **Um ciclo `evento → muta STATE → commit()/render() → DOM`** — é literalmente o **Ciclo Reativo
  "um só sentido"** da Linguagem Ubíqua. O `curador-v3` (`commit()=save()+renderAll()`) é o exemplar.
- **Tema centralizado em CSS `:root`** — o invariante "estética fora dos dados" já é *quase* a
  norma, com 3 exceções (§4).

> Conclusão para o grill: **não é só um padrão repetido — é a assinatura de um domínio.** Há
> material real para uma Alfândega. A pergunta aberta é se é **um** contrato ou **um por modo** (§7).

## 4. Onde o invariante "estética fora dos dados" é quebrado (avisos para a Alfândega)

| Artefacto | Violação | Forma |
|---|---|---|
| `dossier-credito-v5` | cor hex no dado | `DATA.bancos[b].color = "#475569"` (verificado) |
| `governance-explorer` | cor no dado | `pattern.cor = 'emerald'` |
| `MAPA-EXPLORADOR` | atributos visuais no dado | `ORIG`→`--o-*`, `move/relev` usados no render |
| `zonas` (Ficha) | cor no dado | `zone.cor` editável guardado no objeto |

A Alfândega tem de **proibir** isto de raiz: cor/posição/tema vão para o `config.json`; o dado
guarda no máximo um `type`/`tag` semântico, e o tema **deriva** do type.

## 5. Mais limpo vs mais acoplado

- **Referências "limpas" a imitar:**
  - `governance-map-v2` — dados limpos + Cytoscape faz layout/render (separação modelo↔render quase perfeita).
  - `curador-v3` (app principal) — **motor de funções puras** + `commit()=save()+renderAll()` (o Ciclo
    Reativo bem feito). Ressalva: o *viewer* é acoplado (cor *hardcoded*, render total).
  - `FloorViewer` (classe) — **viewer cego** que só recebe `loadData()` e desenha (a "fachada" ideal).
  - `TableEditor` — o **contrato de dados** mais maduro (envelope Frictionless, round-trip lossless),
    apesar de o *código* ser monolítico.
  - `knowledge-graph.json` — o **formato de grafo** mais limpo (dados puros, schema regular).
- **Mais acoplados (o que NÃO imitar):** `dossier` (estética nos dados + Chart.js entrelaçado),
  `Index_v9.1` (estado vive no DOM — não serializa), `MAPA-EXPLORADOR`/`governance-explorer`
  (render inline, cor no dado).

> Insight central: **as 4 peças da fábrica já existem na natureza, mas dispersas** — o melhor
> contrato de dados está no TableEditor, o melhor viewer-cego no `FloorViewer`, o melhor ciclo
> reativo no `curador-v3`, o melhor formato de grafo no `knowledge-graph.json`. A fábrica é
> **juntar num sítio só** o que o David já acertou separadamente.

## 6. Recomendação de piloto

**Confirma-se o grafo como piloto** (recomendação do C-INSTRUCAO), por 3 razões objetivas:
1. É o **modo mais repetido** (8+ artefactos) → o que mais rende ao generalizar.
2. Já existe um **contrato de dados pronto a copiar**: o par `nodes[]`/`edges[]` do
   `knowledge-graph.json`, cruzado com a forma nó/aresta do `governance-map` e dos links do curador.
3. Já existem **dois caminhos de Viewer provados**: biblioteca (Cytoscape, `governance-map`) ou
   SVG caseiro (estilo `MAPA-D-G-AI`/`DIAGRAMAS-governo`). Dá para arrancar simples (SVG) sem prender.

**Proposta concreta de arranque do piloto (M3):** Alfândega v0 = `{ nodes:[{id,type,label,meta}],
edges:[{source,target,type}] }` derivada do `knowledge-graph.json`; Motor = adjacência + filtros
por `type`; Viewer = SVG simples (à `MAPA-D-G-AI`) com upgrade opcional para Cytoscape. Dados reais
de teste: o próprio `knowledge-graph.json` ou os `links` do `V0.json`.

## 7. Munição para o grill (Passo 2 — as 4 tensões)

- **T2 — Alfândega genérica (peça-mãe):** o padrão existe, mas **bifurca em 3 modos**
  (grafo/árvore/tabela). **Decisão do David:** um contrato único que os cubra os três (mais
  abstrato, risco de "tudo e nada"), ou **um contrato por modo** com um núcleo partilhado
  (`{id,type,label,meta}`)? Evidência para ambos: a árvore é um grafo restrito (arestas
  pai→filho); a tabela é mesmo outra coisa (Frictionless).
- **T1 — Desacoplamento:** os moldes de extração já existem — `curador-v3` (`commit()=save()+renderAll()`)
  e `FloorViewer.loadData()`. O que se "parte" para extrair é o **STATE global**. Método (piloto-só
  vs tudo) fica para o David.
- **Auxiliar/espelho:** o TableEditor já pratica "**canais à la carte**" (export/mirror compõem
  schema/tipos/view por destino) + `x-tableeditor` para round-trip — precedente real de que o
  espelho pode ser *vista derivada*, não peça própria.
- **Editor (Gridstack vs texto):** já existem **os dois mundos** — edição visual-direta (MapLab
  mindmap com drag, `zonas` em canvas, curador com drag entre domínios) e estado-como-estrutura
  (cte-index, árvores). Há base para recomendar com trade-offs.
- **Imutabilidade verificada:** **nenhum** artefacto tem hoje passo de compilação — são todos
  single-file editados à mão. Confirma que o "passo de compilação módulos→HTML" da fábrica é
  genuinamente **novo** (e é o que torna a Imutabilidade verificável, não só decretada).

## 8. Confiança e correções da verificação

- **Verificado contra código real:** envelope Frictionless do TableEditor; `FloorViewer` recebe
  `loadData()` e não importa Supabase; Cytoscape no `governance-map`; `color` nos dados do dossier.
- **Corrigido (curador):** a app de produção é o **v3** (o v4 foi um experimento de atribuições
  bilaterais que não entrou em produção). O `dashboard-v3.html` é o *mapa* do curador. O `v3` persiste
  em `localStorage["curador-projetos-ai-v3"]`.
- **Corrigido:** `V0.json` **não** é carregado pelo curador — os dados estão *embebidos*
  (`SEED_PROJECTS`, "verbatim da V1"); `V0.json` é um *export* de estado com a mesma forma.
- **Nuance:** o ficheiro `sec7-viewer.js` **mistura** orquestração Supabase (linhas ~1–270) com a
  classe-viewer `FloorViewer` (a partir de ~279). A separação Motor↔Viewer existe **na classe**,
  não no ficheiro — bom aviso para a fábrica: separar por **módulo nomeado**, não só por classe.
- **Amostragem (confiança média):** ficheiros >300 KB (`projetos-curador-v3`, `dossier`, `MapLab`)
  lidos pelo esqueleto. `FichaProjetosJSJ/zonas` e alguns campos foram **inferidos** (assinalado
  nas fichas) — a confirmar se virarem relevantes para um incremento.

---

*Entregável do M1. Próximo: Passo 2 — `grill-with-docs` alimentado por este mapa, para fechar as
4 tensões (`docs/decisoes-grill.md`). Não se constrói código do factory antes disso.*
