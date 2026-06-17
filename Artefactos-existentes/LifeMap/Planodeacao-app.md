# Plano de Ação — APP (melhorias do `MapLab.html`)

> Roadmap das alterações ao **front-end / app** (single-file HTML+CSS+JS vanilla).
> Para alterações de **servidor/persistência**, ver [`Planodeacao-server.md`](Planodeacao-server.md).
> Registo de **como** cada alteração foi feita: [`log-alteracoes.md`](log-alteracoes.md) (append-only).
> Snapshots congelados: [`Arqueologia Alteracoes/`](Arqueologia%20Alteracoes/).

---

## Protocolo de marcação (como usar este ficheiro)
- Estado de cada alteração no checkbox: `[ ]` por fazer · `[~]` em curso · `[x]` feito · `[!]` bloqueado.
- Quando um item fica **`[x]`**, preencher na **tabela do grupo** os campos `Branch` e `Commit`.
- Item **aceite pelo utilizador** → acrescentar `✅ ACEITE` ao lado do título do grupo e congelar
  snapshot em `Arqueologia Alteracoes/` (ver README dessa pasta).
- Item feito mas **ainda não aprovado** → `⏳ PENDENTE DE ACEITAÇÃO`.
- **Ordem** = numeração **global partilhada** com o `Planodeacao-server.md` (1,2,3… únicos entre os dois).
- Cada vez que se completa um item, **append** uma entrada em `log-alteracoes.md`.

---

## Dependências cruzadas (app ↔ server)
- **Classes/Grupos, ícones por nó e versões** (este ficheiro) definem o **modelo de dados** que o
  **server** (outro ficheiro) terá de **serializar** para `.json`. Não fechar o formato do `.json`
  num lado sem refletir no outro.
- A **reconciliação `.md`↔`.json`** (server) depende dos fields `nivel`/`pai`/`nome` que a **app** escreve.

---

# GRUPO A — App Genérica (projetos + árvores em runtime) — ✅ ACEITE (2026-06-08)

| Campo | Valor |
|---|---|
| **Ordem** | 1 |
| **Branch** | `App-Generica` |
| **Commit** | `71a132d` ("versao alterada 1"), marco `b3ff567` ("appgeral-nosave-v1") |
| **Snapshot** | `Arqueologia Alteracoes/01-AppGenerica-nosave.html` |
| **Estado** | ✅ **ACEITE pelo utilizador (2026-06-08)** |

- [x] Remover os 4 mapas hardcoded (lifemap/icloud/notion/obsidian) e dados embebidos.
- [x] Modelo `workspace = { projects:[{id,name,trees:[{id,name,color,icon}],activeTreeId}], activeProjectId }`.
- [x] `initTree(treeId)` substitui os ~11 literais de estado de chave-fixa (agora `{}` dinâmicos).
- [x] Factory de painéis a partir de `<template id="treePanelTemplate">` (HTML deixou de ser estático).
- [x] Barra de Projetos (criar/trocar/renomear/apagar) + sub-tabs de Árvores (criar/renomear/apagar).
- [x] Estado vazio inicial ("App vazia" → Criar Projeto).
- [x] Side-by-side gera colunas dinamicamente por árvore do projeto ativo.
- [x] Todas as funções de edição mantidas (já parametrizadas por `tabId` = `treeId`).
- [ ] **Mostrar código de cores das árvores** _(ADD-D1)_ — exibir visivelmente (ex.: barra de projetos
      ou cabeçalho da coluna no side-by-side) a cor associada a cada árvore.

---

# GRUPO B — Ícones nos ramos (Notion icons) — ✅ ACEITE (2026-06-08)

| Campo | Valor |
|---|---|
| **Ordem** | 2 |
| **Branch** | `App-Generica` |
| **Commit** | `65e9797` ("MapLab: app generica + icones + sistema de governacao de alteracoes") |
| **Snapshot** | `Arqueologia Alteracoes/02-AppGenerica-icones.html` |
| **Estado** | ✅ **ACEITE pelo utilizador (2026-06-08)** |

- [x] Pacote dos 883 SVG Notion embebido em bloco isolado `<script id="iconPack">` (marcadores ICON PACK START/END).
- [x] API isolada: `iconSvg(name,color,size)`, `iconNames(filter)`, `iconExists(name)`.
- [x] Picker pesquisável (modal `modalIcon`) acionado no painel do nó.
- [x] Ícone guardado em `node.icon` (slug); sobrevive ao `cloneTree`.
- [x] Ícone à esquerda do nome na árvore, recolorido com a cor do ramo (`branchColor`).
- [x] Ícone também no mind map (`svgRect`).

---

# GRUPO C — Rename para MapLab — ✅ ACEITE (2026-06-08)

| Campo | Valor |
|---|---|
| **Ordem** | 3 |
| **Branch** | `App-Generica` |
| **Commit** | `65e9797` ("MapLab: app generica + icones + sistema de governacao de alteracoes") |
| **Estado** | ✅ **ACEITE pelo utilizador (2026-06-08)** |

- [x] `<title>` → "MapLab".
- [x] Cabeçalho interno → "🗺 MapLab" + subtítulo neutro.
- [x] Ficheiro vivo passa a `MapLab.html` (na raiz).
- [x] Atualizar `CLAUDE.md`/`roadmap.md` para refletir o novo nome e processo. _(context.md/handoff.md nesta sessão.)_

---

# GRUPO D — Classes & Grupos (FEITO em memória — ⏳ pendente de aceitação)

| Campo | Valor |
|---|---|
| **Ordem** | 4 _(front-end, em memória — já NÃO depende de persistência; ver nota de reordenação)_ |
| **Branch** | `App-Generica` |
| **Commit** | `f31bd44` (D-1) · `cecbc0e`/`5240981` (3 zonas, redesenho) · `3a0492f`/`acfe5f6` (correções). Logs #009,#011,#012,#013,#014,#017,#018 |
| **Estado** | `[x]` feito em memória · ⏳ **pendente de aceitação** (falta só persistir → Fase 2) |

> **Nota de reordenação (S3, 2026-06-08):** este grupo é agora o **próximo a implementar**, em **memória**
> (sem servidor). As Classes Sistema/Locais funcionam em runtime; a gravação no `MapLab.json`/`.json` da
> árvore fica para a Fase 2 (ordem 8). O esquema `.json` (S3 do server) já prevê todos os campos.

**Conceito.** Field `Type=Classe` atribuível a nós. Duas bibliotecas: **Sistema** (globais, no índice
da app, zona estanque) e **Locais** (por árvore, no `.json` da árvore). Classes organizam-se em **Grupos**.
Cada Grupo e cada Classe têm **ícone** e **cor**. Um nó pode ter **várias** classes (primária + secundária).

- [ ] Painel lateral passa a ter 2 tabs: **"Edição Árvore"** (atual) e **"Classes"**.
- [ ] Tab "Classes" com toggle **Locais / Sistema**.
- [ ] CRUD de **Grupos** (nome, ícone, cor) e **Classes** (nome, grupo, ícone, cor).
- [ ] **Classes Sistema** = globais, disponíveis sempre (mesmo sem projeto); **Classes Locais** = por árvore.
      _(Em memória nesta fase. A persistência — Sistema no `MapLab.json` zona isolada, Locais no `.json` da
      árvore — chega na Fase 2, ordem 8.)_
- [ ] Atribuir a um nó **classe primária** e **secundária**; multi-classe suportada.
- [ ] **Cor de Grupo, de Classe e Custom**: posso atribuir cor a cada Grupo, a cada Classe, e cor
      Custom a um nó. Widget: paleta existente (`MM_COLOR_PALETTE`) + seletor de cor livre (`<input type=color>`).
- [ ] **Origem do ícone do nó**: controlo **global da árvore** ("por Classe" ou "por Grupo") **+** override
      **Custom** por nó (custom NÃO altera a classe, só o ícone). Default: "por Classe".
- [ ] **Regra de cor**: a cor do ícone = cor da classe ativa (primária; secundária sobrepõe no modo
      respetivo). Se o nó não tiver classe e for Custom → cor do custom/ramo.
- [ ] **Visualização configurável (POR ÁRVORE)**: ícones e/ou cores (ambos, só um, ou nenhum); e modo
      **só primárias** vs **primárias+secundárias** (secundária sobrepõe). Default: só primárias.
      Estas preferências são **por árvore** e persistem no `.json` da árvore.
      No **side-by-side**, há um **toggle por vista/painel** para alternar primária/secundária (decisão D-G).
- [ ] Reconciliação por `nome+nivel+pai` (ver server) — a app escreve estes fields. **Sem ambiguidade
      por design**: é PROIBIDO dois nós-irmãos com o mesmo nome sob o mesmo pai/nível (regra de integridade
      ao criar/renomear/importar). Ver Grupo H (numeração) que torna a identidade explícita.
- [ ] **Dropdowns Colapsar/Expandir inteligentes** _(ADD-A5)_ — o menu mostra só os níveis que existem
      abaixo do nó selecionado; sem seleção, atua sobre toda a árvore. Aplica-se a ambas as vistas.

---

# GRUPO E — Atribuição de classes em massa (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | 5 _(front-end, em memória)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] Botão **"Atribuir Classe"** + toggle **"aos filhos" / "custom"** (alternável a meio do processo).
- [ ] Toggle **primária / secundária**: define se o "Aplicar" escreve a classe como primária ou secundária. _(decisão da ronda)_
- [ ] Ao ativar: mostra **caixa de seleção (checkbox) em cada nó** — **só nos níveis abertos** na árvore.
- [ ] Modo **"aos filhos"**: clicar num nó alterna (seleciona/des-seleciona) o nó **+ subárvore**;
      clicar num filho já selecionado remove-o (e sub-filhos).
- [ ] Modo **"custom"**: clicar afeta apenas o nó clicado (seleção manual fina).
- [ ] Botão **"Aplicar"** → atribui a classe escolhida aos nós selecionados.

---

# GRUPO F — Versões de classe (sub-versões) (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | 6 _(front-end, em memória via `s.saves`)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] Na tab "Atribuir Classes": **"Gravar versão classe"**.
- [ ] Versões de classe (V1.a, V1.b…) aninhadas na versão de estrutura (V1, V2…): mesma árvore,
      atribuições de classe diferentes.
- [ ] Dropdown de versão de árvore (V1/V2) + dropdown ao lado com versões de classe (a/b/c).
- [ ] **Em memória** nesta fase: as versões vivem em `s.saves` (perdem-se ao recarregar, como na v12).
      A **persistência em ficheiros** (`Arvore X-vN`/`-vNa`) é o Grupo **S4** (Fase 2, ordem 9), com o mesmo
      esquema de nomes já confirmado.

---

# GRUPO G — Side-by-side avançado (2 modos) (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | 7 _(front-end; fecha a Fase 1)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] **Modo 1 — Árvores diferentes** _(ADD-S1)_: escolher quais as árvores do projeto a mostrar em
      cada coluna (ativar/desativar por coluna); por cada árvore escolher qual a versão.
- [ ] **Modo 2 — Mesma árvore** _(ADD-S1)_: versões lado a lado (cada painel escolhe versão de estrutura
      e/ou de classe) OU uma única versão com classes lado a lado (primária vs secundária por painel).
- [ ] Seletor de modo na vista side-by-side.
- [ ] **Toggle por vista/painel** para alternar a visualização **primária / secundária** (e ícones/cores)
      independentemente em cada painel. _(decisão da ronda)_
- [ ] **Drag & drop entre árvores diferentes** _(ADD-S2)_ — no Modo 1, poder arrastar um nó de uma
      coluna para outra (mover nó para outra árvore).

---

# GRUPO H — Numeração de nós (toggle ativar/desativar) (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | 4 _(com D; resolve a identidade de nós)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer · **🎯 FOCO ATUAL (S3, com D)** |

**Conceito (decisão da ronda — resolve a ambiguidade da reconciliação).** Regra de integridade: **não
podem existir dois nós-irmãos com o mesmo nome sob o mesmo pai/nível**. Para tornar a identidade
explícita e legível:
- [ ] Toggle **"ativar/desativar numeração"** na vista do mapa: mostra/esconde a numeração hierárquica.
- [ ] **Modos de numeração** _(ADD-A3)_:
  - **Geral** — numeração contínua de toda a árvore (ex.: `1`, `1.1`, `1.1.1`).
  - **Por Pai-Filhos** — reinicia a contagem em cada ramo (ex.: cada grupo de irmãos começa em `1`).
  - **Criar Secções** — com separador configurável (ex.: `1.1 / 1.2`).
- [ ] **Tipos de numeração** _(ADD-A3)_: Árabe (1,2,3…), Romano (I,II,III…), Alfabeto (a,b,c…).
      Podem combinar-se por nível (ex.: nível 1 romano, nível 2 árabe).
- [ ] No **export `.md`**: opção de incluir ou não a numeração (independente do toggle de visualização).
      Também configurável para **mirror** (S8). _(ADD-A3)_
- [ ] No **`.json`** (server, Fase 2): grava-se **sempre** um field `numeracao` por nó (ex.: "2.2.2.2"),
      identificando o nó sem ambiguidade — independentemente do toggle de visualização. _(Nesta fase em
      memória, basta o toggle de vista + o export `.md`; o field `.json` materializa-se na ordem 8.)_
- [ ] A numeração deriva da posição na árvore (nível + ordem entre irmãos); recalculada ao mover/criar/apagar.

---

# GRUPO I — Filtros e ficheiros na vista (liga ao Mapear Pasta, S5) (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | 10 _(com S5 — Mapear Pasta)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer · **⚠ a debater em detalhe com o utilizador** |

**Conceito (decisão/abertura da ronda; base em `referencias/instrucoesMapa.md`).** Quando uma árvore vem
de mapear uma pasta, pode conter **ficheiros** além de pastas:
- [ ] Toggle **mostrar/esconder ficheiros** na vista (ficheiros distinguem-se das pastas — no `.md` levam
      prefixo `_ ` em vez de `- `, conforme `instrucoesMapa.md`).
- [ ] **Filtro** que mostra só os nós que interessam: por **extensão** (`*.ext`), por **nome.ext**, ou por
      **pasta** (ex.: esconder `venv`, `node_modules`).
- [ ] Toggle do filtro com **2 comportamentos**: (a) **expandir** só os ramos necessários para mostrar os
      elementos filtrados (+ os seus pais), mantendo o resto fechado mas visível; ou (b) **esconder** todos
      os ramos que não levam a elementos filtrados.

> **Nota:** este grupo será **debatido em detalhe** antes de implementar (o utilizador pediu-o). A
> referência canónica é `referencias/instrucoesMapa.md` (formato de mapa de pastas, ficheiros com `_`,
> agrupamento por tipo, hidden primeiro, "não expandido", exclusões).

---

# GRUPO J — UI de portabilidade & mirror (front-end dos grupos S7/S8) (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | 8 (portabilidade) / 9 (mirror) — acompanha S7/S8 do server (Fase 2) |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

São os botões/diálogos na app que conduzem a lógica de servidor S7/S8:
- [ ] **"Mudar path de árvores"** — escolher nova pasta base; opção de mover os ficheiros (chama S7).
- [ ] Diálogo de **re-base ao detetar que a app foi movida** (confirmar nova localização) (S7).
- [ ] Por árvore: **configurar mirror** (path absoluto + só `.md` ou `.md`+`.json`) (S8).
- [ ] **"Atualizar do mirror"** (da versão aberta; pergunta "sobrepor?") (S8).
- [ ] **"Nova versão de mirror"** (cria a V seguinte no path do mirror) (S8).

---

# GRUPO K — Toggle "afetar filhos" em todas as funções (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | _(a integrar na Fase 1, com D/E)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

**Conceito _(ADD-A1)_.** Qualquer operação que hoje age só no nó selecionado deve ter um toggle
para propagar (ou não) a toda a subárvore (filhos, netos, etc.).
- [ ] Toggle **"Afetar filhos: Sim / Não"** disponível globalmente em todas as operações de edição
      (renomear, mover, atribuir ícone, atribuir classe, etc.).
- [ ] Comportamento: ao ativar, a operação aplica-se recursivamente a todos os descendentes do nó.

---

# GRUPO L — Botão Undo (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | _(a integrar na Fase 1, com D/E)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

**Conceito _(ADD-A2)_.** Desfazer a última operação realizada numa árvore.
- [ ] Botão **Undo** (ou atalho de teclado) que reverte a última alteração ao estado da árvore.
- [ ] Stack de undo em memória por árvore (em `tabState[treeId]`); profundidade a definir.
- [ ] Aplica-se a: criar/apagar/mover nós, renomear, atribuir ícone/classe, reordenar.

---

# GRUPO M — Aba específica para Ficheiros (NOVO — por implementar)

| Campo | Valor |
|---|---|
| **Ordem** | 10 _(com S5 Mapear Pasta e Grupo I — depende de árvores com ficheiros)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

**Conceito _(ADD-A4)_.** Quando uma árvore contém ficheiros (vindos de S5 Mapear Pasta), uma aba
dedicada trata-os separadamente das pastas.
- [ ] **Detetar tipos por extensão** e apresentar lista de extensões presentes na árvore.
- [ ] **Selector de visibilidade**: mostrar tudo ou só alguns tipos de ficheiro (allowlist de extensões).
- [ ] **Ordenação**: por tipo ou por nome — configurável globalmente ou por subárvore.
- [ ] **Numeração de ficheiros independente** da numeração da árvore (Grupo H não afeta ficheiros):
  - Opção de numerar dentro de cada nível (reinicia por pasta).
  - Opção de numerar sequencialmente por todos os filhos de um ramo.
- [ ] Ficheiros distinguem-se no `.md` por prefixo `_ ` (conforme `referencias/instrucoesMapa.md`).

---

## Faseamento sugerido (para avaliar peça a peça) — REORDENADO (S3: front-end primeiro)
1. **A+B+C** (feitos, aceites).
2. **FASE 1 front-end, em memória** (foco atual):
   - **D** Classes & Grupos (+ **H** Numeração com modos/tipos) → **E** Atribuição em massa →
     **F** Versões de classe (em `s.saves`) → **G** Side-by-side avançado (2 modos + drag entre árvores).
   - **K** Toggle "afetar filhos" + **L** Undo — integrar com D/E (mesma fase).
   - **ADD-D1** Cores das árvores visíveis + **ADD-A5** Colapsar/Expandir inteligente — pequenas melhorias, integrar quando conveniente.
3. **FASE 2 servidor/persistência** (só depois): **S1+S2+S3** persistência base **+ S7** portabilidade →
   **S4** versões em ficheiros **+ S8** mirror (+ **J** UI) → **S5 + I + M** (Mapear pasta + filtros/ficheiros
   + aba Ficheiros) → **S6** (criar pastas).

> O **esquema `.json` completo** continua definido em `Planodeacao-server.md` → S3 (inclui classe +
> numeração). Fazer o front-end primeiro **não gera retrabalho** de serialização quando a Fase 2 chegar.
