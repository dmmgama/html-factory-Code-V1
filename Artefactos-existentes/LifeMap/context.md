# context.md — SSOT do projeto LifeMap

Conhecimento acumulado do projeto. Cresce ao longo do tempo. Para o "porquê" das decisões
ver `memory.md`; para o estado imediato ver `handoff.md`; para o detalhe técnico ver
`docs/MANUAL.md`.

_Última atualização: 2026-06-10 (S3, branch `App-Generica`: Grupo D Classes & Grupos feito em memória; side-by-side com edição; seed de teste)._

> **⚠️ DUAS LINHAS DE TRABALHO — lê isto primeiro.**
> - **`main`** = app **v12** (`lifemap_lab.html`, 4 mapas hardcoded). As §§1–11 abaixo descrevem ESTE estado.
> - **`App-Generica`** (branch ativa) = a app tornou-se **MapLab**: editor **genérico** (projetos+árvores
>   em runtime, sem hardcode), **+ ícones Notion**, a caminho de **classes/grupos** e **persistência por
>   servidor**. Ficheiro vivo = **`MapLab.html`**. Ver **§14 (estado da branch)** e
>   **`instrucao-agente-alteracoes.md`** (onboarding governado). Versão Original v12 congelada em
>   `Arqueologia Alteracoes/00-…`. **Se estiveres nesta branch, as §§3,4,6,8 estão substituídas pela §14.**

---

## 1. Identidade
- **Nome:** Life Map Laboratory.
- **Objetivo:** editar/visualizar taxonomias hierárquicas de vários domínios (vida, mail
  iCloud, Notion, Obsidian) como árvore e mind map, com import/export Markdown e versões.
- **Forma:** app **single-file** `lifemap_lab.html` (v12).

## 2. Stack
- HTML + CSS + JavaScript **vanilla** (ES6). Sem build, sem dependências, sem framework.
- Mind map em **SVG**. Tema escuro via CSS variables.
- Ambiente de dev: **Windows + PowerShell**. Node usado apenas para validar o JS embebido.

## 3. Arquitetura (resumo; detalhe em docs/MANUAL.md §4)
- **Tabs canónicas:** `TABS = ['lifemap','icloud','notion','obsidian']` + vista derivada "side".
  Cores: lifemap verde `#4ade80`, icloud azul `#7eb8f0`, notion roxo `#bb86fc`, obsidian rosa
  `#f472b6`, side laranja `#f0a830`.
- **Dados originais embebidos** como strings MD: `LIFEMAP_MD`, `ICLOUD_MD`, `NOTION_MD`,
  `OBSIDIAN_MD` → `*_DATA = parseMdToFlat(...)`; `getRawData(tabId)` devolve a lista.
- **Pipeline:** `parseMdToFlat(raw,keepNum)` → flat `[{id,name}]` → `buildTreeFromFlat(flat,
  tabId,preserveOrder,sep)` → árvore de nós `{id,originalId,name,isSystem,children}`.
- **`PATH_SEP = ''`** (string vazia) — separador de path nos ids, escolhido para suportar
  nomes com `/` (ex.: "R/C Esq").
- **Estado em memória:** `tabState[tabId]` (tree, notes, changelog, expanded, selected,
  saves[], …) + objetos por-tab do mind map (`mmExpanded, mmPos, lastPos, mmColor, mmLayout,
  mmSide, mmView, MM_TITLE, sideExpanded`). Adicionar um mapa = registar o `tabId` em todos.
- **Render parametrizado por `tabId`** (renderTab, renderMindmap, buildMmStar,
  buildMmHorizontal, refreshSide, …) — estender não exige lógica nova.
- **Boot:** `TABS.forEach(initTab); TABS.forEach(renderTab);` no fim do `<script>`.

## 4. Persistência (CRÍTICO)
- **Não há persistência.** Sem `localStorage`/`sessionStorage`/`indexedDB`, sem servidor,
  sem `fetch`. O botão "Save / Versões" guarda snapshots **só em memória** (`s.saves`),
  perdidos ao recarregar/fechar.
- Persistência real = **exportar `.md`** (`doDownload`/`doCopy`) e reimportar (`doImport` /
  Editar MD). É o único mecanismo durável.

## 5. Formato MD canónico
`# Versao <V>` + `# Estrutura` + lista única de bullets (2 espaços = 1 nível), emoji opcional,
**sem numeração**, sem outros headings/código. (Manual §5.)

## 6. Layout de ficheiros
- `lifemap_lab.html` — a app (editar sempre este).
- `icloud_mail_editor.html` — app **separada/independente** (editor de mail). Não confundir.
- `.Old/lifemap_lab_v{2,4,5,6,7,8,9,10,11}.html` — histórico (não há v3).
- `docs/MANUAL.md` — manual técnico (inclui §8: arquitetura de configuração & continuidade).
- `docs/prompt-md-generator.md` — prompt robusta para LLMs gerarem MD no formato da app.
- `CLAUDE.md`, `context.md`, `handoff.md`, `memory.md`, `roadmap.md` — config/continuidade.
- `CHANGELOG.md` — alterações visíveis da app, por versão.
- `.claude/settings.json` — config partilhada (permissões: git read-only). `settings.local.json` fora do git.
- `.gitignore` ignora `logs/` e `SessionTranscripts/`.

> Camada de config Claude Code criada e **commitada+pushed** (`Setup-ClaudeCode`, `5e21636`)
> e formalmente fechada na S1 (`Fecho SG 1`, `1c3b6db`).

## 7. Git
- Remote: `https://github.com/dmmgama/LifeMapEditor.git`. Branch `main`. Utilizador git: `dmm.gama`.
- **Repo privado** (mudado de público após decisão D7).
- Histórico: init → rename `lifemap_lab_v12.html`→`lifemap_lab.html` → add `index.html` mirror
  → **remove `index.html` mirror + pre-commit hook** → `Setup-ClaudeCode` (config Claude Code) →
  `Fecho SG 1` (atualiza continuidade) → `S1 — Setup e gestão` (este fecho).
- **GitHub Pages abandonado por privacidade** (estado final: sem `index.html`, sem hooks).

## 8. Convenções de trabalho
- Editar só `lifemap_lab.html`; versionar por commits (não por ficheiros `vN`).
- Validar JS embebido com `node -e "new Function(...match(/<script>([\s\S]*)<\/script>/)[1])"`.
- Historicamente: alterações grandes via scripts `_patch_vN.js` temporários (apagados; fora do repo).
- UI e documentação em PT-PT.

## 9. Dependências
- Nenhuma (runtime). Node só para validação local.

## 10. Cronologia condensada (v4 → v12)
- v4: base (5 tabs, mind map com bugs).
- v5: mind map a gerar; formato MD `# Versao`/`# Estrutura`; modal "Editar MD"; 2 layouts; zoom.
- v6: drag de nós/linhas; estado do mind map preservado; paleta de cor por nível-1; pan.
- v7: remove numeração; formato MD universal entre tabs.
- v8: lifemap atualizado; reposicionar nível-1 esq/dir; linhas até à fronteira das caixas.
- v9: iCloud com Original + v1.
- v10/v11: lifemap e iCloud atualizados; "Transportes" volta para dentro de Património.
- v12: **Obsidian** adicionado como 4º mapa (estrutura do vault AI). Depois: git + (Pages, abandonado).
- S1 (Setup e gestão): scaffolding da config Claude Code formalizado; prompt MD arquivada
  em `docs/prompt-md-generator.md`; numeração de sessões unificada (track único `S #`).

## 11. Dívida técnica conhecida
- `addPermanentSave` definida mas sem call-site (código morto).
- `NOTION_MD` usa heading `# NOTION - v2` (não reconhecido por `parseMdHeading`).
- Sem persistência durável (ver §4).

## 12. Pendentes herdados do histórico
- ~~Prompt robusta para um LLM gerar MD no formato da app~~ → **entregue na S1** e arquivada
  em `docs/prompt-md-generator.md`.
- ~~**Roadmap da app** — adiado na S1~~ → **REABERTO (2026-06-08)** na branch `App-Generica`.
  Ver `roadmap.md` (visão completa) e os dois `Planodeacao-*.md` (executável).

## 13. Convenção de numeração de sessões
- **Track único `S #`** (a partir da S1, 2026-06-02).
- O esquema antigo (`SG #` para setup vs `S #` para trabalho da app) foi abandonado por
  ser desnecessariamente complexo. Sessões anteriores ao novo esquema (incluindo o
  ZIP `SG 1 - Setup Claude Code.zip` e os ficheiros `S1-Transcript.jsonl`/`S1-metadata.json`
  em `SessionTranscripts/`) ficam como **pré-numeração unificada** — não são renomeadas, mas
  no novo esquema esta é a sessão **S1**.

## 14. Branch `App-Generica` — MapLab (estado atual, substitui §§3,4,6,8 nesta branch)
- **Identidade:** **MapLab** — editor **genérico** de taxonomias. Ficheiro vivo: **`MapLab.html`**.
- **Modelo:** `workspace = {projects:[{id,name,trees:[{id,name,color,icon}],activeTreeId}],activeProjectId}`.
  Estado por árvore em `tabState[treeId]` (= antigo `tabId`). Os ~11 stores do mind map são `{}`
  populados por **`initTree(treeId)`** (já não são literais de chave-fixa). `TABS` espelha o projeto
  ativo via `syncTABS()`. UI por factory: `<template id="treePanelTemplate">` + `buildPanels()` +
  `renderTabsBar()`/`renderProjectBar()` + `renderWorkspace()`.
- **Sem mapas hardcoded** (removidos lifemap/icloud/notion/obsidian e dados embebidos). App arranca vazia.
- **Ícones:** 883 SVG Notion num bloco estanque `<script id="iconPack">` (marcadores ICON PACK START/END);
  API `iconSvg`/`iconNames`/`iconExists`; ícone por nó em `node.icon`, recolorido por `branchColor()`.
- **Marcos ACEITES (2026-06-08):** A (app genérica), B (ícones), C (rename MapLab). Snapshots em
  `Arqueologia Alteracoes/01-…` e `02-…`.
- **CLASSES & GRUPOS (Grupo D) — FEITO em memória (S3, ⏳ pendente de aceitação):**
  - Painel direito com **2 tabs** (Edição Árvore | Classes). Tab Classes em **3 zonas estanques** (sub-renders
    isolados, compositor `renderClassPanel`): **Visualização** (`s.view`: "Mostrar por" Grupo/Classe; Ícones
    Primário/Secundário (2 checkboxes); Cor Primária/Secundária/Desligada) · **Gestor** (`s.classTab`: toggle
    Locais/Sistema, dropdowns Grupo→Classe, "Editar Grupos"/"Editar Classes" com **drag&drop**) · **Atribuir**
    (`s.assign`: Ativar edição, toggle Primária/Secundária, toggle "A filhos").
  - **Bibliotecas:** `systemLib` (global) e `tabState[treeId].localLib` — ambas `{groups[],classes[],noGroup{icon,color}}`.
    Grupo `{id,name,icon,color}`; Classe `{id,name,groupId,icon,color}` (`groupId:''`=Sem Grupo, que é **grupo real**
    com cor/ícone editáveis em `lib.noGroup`).
  - **Campos novos no nó:** `classePrimaria`,`classeSecundaria` (classId|null), `classeTipo` ('local'/'sistema'),
    `iconCustom` (bool). A classe do nó resolve-se por id em **ambas** as libs (imune ao scope — `classeTipo` só p/ serialização).
  - **Render do nó** (`resolveNodeVisual`): ícones+cor por R1 (cor Custom>Classe>cinzento neutro), R2 (modo prim+sec =
    2 ícones), R4 (iconCustom). Em modo Atribuir, a vista segue o tipo a atribuir. Integrado em `renderTree` E `renderSideTree`.
  - **Side-by-side ganhou edição** (parte do Grupo G): painel partilhado à direita, **árvore ativa por clique no título**,
    só a coluna ativa responde a cliques, **colunas redimensionáveis** + "Largura igual". `renderPanel`/`renderClassPanel`
    forçam o host do side quando `sideViewActive()`. Paridade com a vista normal validada (expand/colapsar respeita seleção).
- **Persistência:** ainda em memória (Fase 2 por fazer — é o **próximo passo recomendado**). Alvo: servidor local
  opcional + fallback memória; índice `MapLab.json`; save por árvore = `Arvore X.md` (limpo) + `Arvore X.json`
  (completo, esquema em `Planodeacao-server.md` S3); reconciliação `nome+nivel+pai`.
- **DUAS VERSÕES:** `MapLab.html` (virgem) + `MapLab-teste.html` (gerada por `node build-teste.js` = virgem + bloco
  de teste com botão "Carregar projetos"). O seed cria P1[A1,A2]/P2[A1,A2,A2b] + grupos/classes de exemplo (Sistema:
  Classes de conhecimento C1-C3 + Orçamento/Planeamento; Local: DominiosVida Camada0/Manutenção + Night). Bloco-fonte:
  `MapsTeste/seed-bloco.template.html`. A virgem NUNCA contém o bloco; regenera-se a cada edição.
- **Por implementar (visão em `roadmap.md`):** E atribuição em massa (modo custom/Aplicar — **parcial**), F versões de
  classe, G 2 modos formais (**parcial**), H numeração; persistência S1–S6, mapear/criar pastas (S5/S6).
- **Governação:** processo de alterações descrito em `instrucao-agente-alteracoes.md`; roadmap executável
  nos `Planodeacao-*.md`; como-foi-feito em `log-alteracoes.md` (append-only); snapshots em
  `Arqueologia Alteracoes/` (read-only).
