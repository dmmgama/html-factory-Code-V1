# Log de Alterações — MapLab (APPEND-ONLY)

> **Regras deste ficheiro:**
> - **Append-only.** Nunca editar nem apagar entradas antigas. Se algo mudar, escreve uma entrada NOVA
>   que **supersede** (referencia) a antiga.
> - Uma entrada por alteração concluída. Registar **o que foi feito**, **como**, e **implicações**
>   (ex.: novos ficheiros `.json`, novos campos no modelo, dependências criadas).
> - Datas em formato absoluto. Referenciar a `Ordem` global do plano e o `Branch`/`Commit` quando existir.

---

## [#001] Ordem 1 — App Genérica (projetos + árvores em runtime)
- **Data:** 2026-06-07
- **Plano:** `Planodeacao-app.md` → Grupo A
- **Branch/Commit:** `App-Generica` / `71a132d` ("versao alterada 1"); marco `b3ff567` ("appgeral-nosave-v1")
- **Estado:** feito — ⏳ PENDENTE DE ACEITAÇÃO
- **Como foi feito:** removidos os 4 mapas hardcoded e os dados embebidos; introduzido o modelo
  `workspace{projects→trees}`; os ~11 literais de estado de chave-fixa passaram a `{}` populados por
  `initTree(treeId)`; painéis HTML estáticos convertidos em factory a partir de `<template>`;
  adicionadas barras de Projetos e sub-tabs de Árvores (CRUD); estado vazio inicial; side-by-side
  dinâmico. Todas as funções de edição preservadas (já parametrizadas por `tabId`).
- **Implicações:** o estado deixou de ter mapas fixos → qualquer persistência futura tem de serializar
  esta estrutura dinâmica. `getNodeIcon` deixou de ter lógica por-mapa (iCloud/Notion); nós genéricos
  sem ícone automático. Conceito de "pasta de sistema" (iCloud) removido.
- **Verificação:** JS OK; screenshots (estado vazio, 2 árvores com nós, side-by-side).

## [#002] Ordem 2 — Ícones nos ramos (Notion icons)
- **Data:** 2026-06-08
- **Plano:** `Planodeacao-app.md` → Grupo B
- **Branch/Commit:** `App-Generica` / _(não commitado; trabalho em `MapLab.html`)_
- **Estado:** feito — ⏳ PENDENTE DE ACEITAÇÃO
- **Como foi feito:** os 883 SVG da pasta `IconsNotion/` foram embebidos num bloco isolado
  `<script id="iconPack" type="application/json">` (delimitado por `ICON PACK START/END`), gerado por
  script Node temporário (apagado). Cada valor = path interno do SVG com `fill` removido (recolorir via
  `currentColor`). API de acesso: `iconSvg`/`iconNames`/`iconExists`. Picker pesquisável (`modalIcon`)
  no painel do nó; ícone guardado em `node.icon`; mostrado na árvore e no mind map com a cor do ramo.
- **Implicações:**
  - **Novo campo no nó:** `node.icon` (slug, string). Tem de entrar na futura serialização `.json`.
  - **Reconciliação futura:** quando o `.json` por árvore existir, o ícone liga ao nó por `nome+nivel+pai`.
  - Tamanho do ficheiro subiu para ~347 KB (pacote de ícones). Aceitável (app local).
  - O pacote é uma **zona estanque** — alterar ícones = mexer só entre os marcadores.
- **Verificação:** JS OK; JSON do pacote = 883 chaves válidas; screenshots (ícone com cor do ramo; picker a filtrar).

## [#003] Ordem 3 — Rename para MapLab + montagem do sistema de governação
- **Data:** 2026-06-08
- **Plano:** `Planodeacao-app.md` → Grupo C
- **Branch/Commit:** `App-Generica` / _(não commitado)_
- **Estado:** feito — ⏳ PENDENTE DE ACEITAÇÃO
- **Como foi feito:** criado o ficheiro vivo **`MapLab.html`** (= estado 02, app genérica + ícones), com
  `<title>` e cabeçalho internos mudados para "MapLab". Criada a pasta `Arqueologia Alteracoes/` com
  snapshots congelados: `00-VersaoOriginal` (v12 hardcoded, de `a733819`), `01-AppGenerica-nosave`
  (de `71a132d`), `02-AppGenerica-icones` (ex-`lifemap_lab_v2.html`). Criados os ficheiros de processo:
  `Planodeacao-app.md`, `Planodeacao-server.md`, `instrucao-agente-alteracoes.md`, este log, e
  `questionario-validacao.md`.
- **Implicações:**
  - O ficheiro a editar passa a ser **`MapLab.html`** (os `lifemap_lab*.html` ficam como histórico;
    a Versão Original está congelada na Arqueologia).
  - `CLAUDE.md`/`context.md` ainda referem "Life Map Laboratory" e `lifemap_lab.html` — **a atualizar
    quando o marco for aceite** (ainda não feito, para não tocar em continuidade antes da aceitação).
  - Estabelecido o protocolo: ficheiro vivo único + Arqueologia read-only + ordem global + log append-only.
- **Verificação:** JS OK em `MapLab.html`.

## [#004] Roadmap reaberto + marcos A/B/C ACEITES + propagação do rename
- **Data:** 2026-06-08
- **Plano:** `Planodeacao-app.md` → Grupos A, B, C; `roadmap.md`
- **Branch/Commit:** `App-Generica` / _(a commitar nesta sessão)_
- **Estado:** feito
- **Como foi feito:** o utilizador apontou (corretamente) que o `roadmap.md` estava parado na S1 e não
  refletia as features faladas. Reescrito o `roadmap.md` com a **visão completa**: Fase 1 (app genérica ✓,
  ícones ✓, rename ✓, Classes & Grupos, atribuição em massa, versões de classe, side-by-side 2 modos) e
  Fase 2 (persistência base, índice `MapLab.json`, save `.md`+`.json`, versões em ficheiros, mapear/criar
  pastas), com ordem global e dependências. Auditados os dois `Planodeacao-*.md` contra a conversa —
  cobrem tudo (multi-classe primária/secundária, origem do ícone global+custom, regra de cor, toggle
  flexível, reconciliação `nome+nivel+pai`, fallback memória). O utilizador **CONFIRMOU os marcos A/B/C**
  → marcados ✅ ACEITE; `CLAUDE.md` atualizado (deixa de mandar "editar lifemap_lab.html / app v12";
  passa a distinguir `main`(v12) vs `App-Generica`(MapLab) e a apontar para `instrucao-agente-alteracoes.md`).
- **Implicações:**
  - Resolvida a contradição #1 do validador (CLAUDE.md ↔ processo novo).
  - `roadmap.md` passa a ser a fonte da **visão**; os planos são o **executável**.
  - Marcos A/B/C aceites → os snapshots `01`/`02` na Arqueologia ficam oficialmente como marcos.
  - `context.md`/`handoff.md` a atualizar no fecho da sessão (continuidade).
- **Verificação:** revisão dos .md; sem alteração de código (`MapLab.html` intacto).

## [#005] Auditorias de implementabilidade + ronda de perguntas → planos completados
- **Data:** 2026-06-08
- **Plano:** `registo-auditoria.md` (AUD-002/003 + RESOLUÇÃO); `Planodeacao-app.md`/`-server.md`; `roadmap.md`
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito
- **Como foi feito:** criado `registo-auditoria.md` (append-only) com o feedback de 2 subagentes
  (AUD-001 onboarding; AUD-002 implementabilidade por alteração) + AUD-003 (retoma de sessão). Adicionada
  a **§0bis (Retoma de sessão)** à `instrucao-agente-alteracoes.md` e criado o protocolo de log de retoma
  em `agente-audit-iniciar.md` (validado por subagente). O utilizador respondeu à **ronda de perguntas**
  que fechou as lacunas: planos e roadmap atualizados.
- **Implicações (decisões novas):**
  - **Esquema `.json` completo definido já** (S3) com campos de classe + `numeracao` → persistência base
    grava o formato final (resolve a tensão de ordem D↔4).
  - **Nova funcionalidade Grupo H — Numeração** (toggle; export `.md` com/sem; `.json` field `numeracao`)
    + **regra de integridade**: proibido irmãos homónimos no mesmo pai/nível → reconciliação inequívoca.
  - **Nova secção Grupo I — Filtros/ficheiros na vista** (ligado a S5; a debater) com base em
    `referencias/instrucoesMapa.md` (copiado para o repo).
  - Atribuição em massa: toggle primária/secundária. Cores: paleta + color-picker. Vista: por árvore +
    toggle por painel no side-by-side. Endpoints: espelham `acc_server.py`. Nomes de versão confirmados.
    S6: preview+confirmação, saltar existentes, sanitizar nomes.
- **Verificação:** revisão dos .md; sem alteração de código (`MapLab.html` intacto, blob `ef14070`).

## [#006] Portabilidade + Mirror — decisões e novos grupos (S7, S8, J)
- **Data:** 2026-06-08
- **Plano:** `Planodeacao-server.md` (S2, S7, S8); `Planodeacao-app.md` (Grupo J); `roadmap.md`
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (planeamento; sem código)
- **Como foi feito:** ronda de perguntas sobre portabilidade resolveu a tensão "portável vs paths absolutas".
- **Implicações (decisões):**
  - **Índice híbrido:** `MapLab.json` sempre na raiz; caminhos das árvores **relativos** (`Projetos/...`);
    `lastKnownPath` gravado só para deteção de movimento; mirror em path **absoluto**.
  - **`.py` do servidor NÃO contém paths** — lê tudo do `MapLab.json` (genérico/portável).
  - **S7 Portabilidade/re-base:** mover a pasta inteira funciona; servidor compara o seu dir com
    `lastKnownPath` e pede confirmação; botão "Mudar path de árvores" (com opção de mover ficheiros).
  - **S8 Mirror por versão:** dupla gravação (Projetos/ + mirror externo); mirror **por versão** com
    nomenclatura fixa `MapaXxx-Vx.md`; botões "Atualizar do mirror" (da versão aberta, pergunta sobrepor)
    e "Nova versão de mirror" (cria a V seguinte). Mirror pode ser só `.md` ou `.md`+`.json`.
  - **Grupo J (app):** UI destes (mudar path, configurar/atualizar/nova-versão mirror, diálogo de re-base).
- **Verificação:** revisão dos .md; `MapLab.html` intacto (blob `ef14070`).

## [#007] Reordenação do roadmap — FRONT-END PRIMEIRO (Fase 1 antes da Fase 2)
- **Data:** 2026-06-08 (S3)
- **Plano:** `roadmap.md`; `Planodeacao-app.md`; `Planodeacao-server.md`; `handoff.md`
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (planeamento; sem código)
- **Como foi feito:** o utilizador clarificou que o objetivo imediato é **ver a app a funcionar** com as
  features novas, **em memória** — as classes/versões NÃO precisam de ficar gravadas para já. Isto
  **dissolve** a antiga regra "persistência base (ordem 4) antes das Classes (ordem 5)", que só existia
  para haver onde gravar. Reordenado o roadmap e ambos os planos: toda a **Fase 1 (front-end)** passa a vir
  **antes** da **Fase 2 (servidor)**.
- **Nova ordem global:** 4 = D Classes & Grupos + H Numeração _(foco atual)_ · 5 = E Atribuição em massa ·
  6 = F Versões de classe (em `s.saves`, em memória) · 7 = G Side-by-side · 8 = S1+S2+S3 Persistência base
  + S7 Portabilidade · 9 = S4 Versões em ficheiros + S8 Mirror · 10 = S5 Mapear Pasta + I Filtros · 11 = S6 Criar pastas.
- **Âmbito da fase "ver funcionar" (confirmado pelo utilizador):** **D + E + H** (Classes & Grupos,
  atribuição em massa, numeração). F e G ficam para depois dentro da mesma Fase 1.
- **Implicações:**
  - Grupos D/E/F/H/G implementam-se **em memória** (sem servidor). O field `numeracao` no `.json` e a
    persistência de classes (Sistema no `MapLab.json`, Locais no `.json` da árvore) materializam-se na
    ordem 8, não agora.
  - As versões de classe (F) usam `s.saves` (como a v12) — perdem-se ao recarregar; durabilidade = S4 (ordem 9).
  - **Sem retrabalho de serialização:** o esquema `.json` continua definido em `Planodeacao-server.md` → S3;
    fazer o front-end primeiro só estabiliza o modelo de dados antes de o gravar.
  - Próximo passo de **código** = Grupo D (+H), em `MapLab.html`, em memória.
- **Verificação:** revisão dos .md; `MapLab.html` intacto (blob `ef14070`).

## [#008] Expandir/Colapsar respeita o nó selecionado (árvore principal)
- **Data:** 2026-06-08 (S3)
- **Plano:** _(fix pedido pelo utilizador; fora dos grupos do roadmap — melhoria de UX da edição existente)_
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito
- **Como foi feito:** alteradas 3 funções em `MapLab.html` — `expandToLevel`, `collapseAll`,
  `collapseBelow` (menu "⊞ Nível ▾" da árvore principal). Adicionado helper `descendantBranchIds(node)`.
  Cada função ganhou um ramo "se `s.selected`": opera **só na subárvore do nó selecionado**, preservando
  o resto de `s.expanded`; o `walk` parte de `[root]` a `d=0`, por isso os níveis do menu contam **a
  partir do nó** ("Nível 1" = só o nó aberto; "Tudo" = subárvore inteira). Sem seleção → comportamento
  original (aplica à árvore toda). `mmExpanded` mantém-se sincronizado como antes.
- **Implicações:**
  - A vista **side-by-side** (`sideExpand*`) **não** foi alterada: não tem conceito de nó selecionado
    (os seus nós só fazem toggle), logo a regra não se aplica lá.
  - Comportamento sem seleção é idêntico ao anterior → não quebra fluxos existentes.
- **Verificação:** JS OK. Teste lógico headless (vm + stubs DOM) com 7 casos — todos passam: expandir/
  colapsar tudo sem seleção; com seleção em A mantém o ramo B intacto; níveis relativos (`expandToLevel(1)`
  e `collapseBelow(1)` deixam só o nó aberto); seleção em folha = no-op sensato. Ficheiro de teste removido.

## [#009] Grupo D, sub-passo D-1 — Classes & Grupos: estado + libs + CRUD + 2 tabs (em memória)
- **Data:** 2026-06-08 (S3)
- **Plano:** `Planodeacao-app.md` → Grupo D (Ordem 4); decisões da ronda registadas abaixo
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (D-1 de 4 sub-passos; ⏳ pendente de aceitação do utilizador)
- **Decisões fechadas com o utilizador (antes de codificar):**
  - **Cor (R1):** precedência **Custom > Classe > Ramo** (cor manual da paleta manda sempre).
  - **Secundárias (R2):** modo "primárias+secundárias" mostra **DOIS ícones** lado a lado (1º=primária, 2º=secundária),
    cada um pintado com a cor da sua classe/grupo; custom usa cor custom. Modo "só primárias" = só o 1º.
  - **Apagar (R3):** avisar/confirmar se em uso — conta nós que usam a classe; grupo com classes → confirmação dupla
    e apaga as classes em cascata, limpando referências nos nós.
  - **Ícones legado (R4):** só custom se marcado; **migração 1x** (nós com `node.icon` e sem classe ganham
    `iconCustom=true`) — a aplicar no D-3 (render), onde tem efeito. Nó sem classe e sem ícone custom = sem ícone.
- **Como foi feito (D-1, só `MapLab.html`):**
  - Estado: `systemLib` global (`{groups,classes}`); `DEFAULT_VIEW`; em `initTree` cada árvore ganha `localLib`,
    `view` (iconsVisible/colorsVisible/classMode/iconSource/numeracaoVisible) e `classTab` (active/scope).
    Mapeia 1:1 ao esquema `.json` S3 (sem retrabalho de serialização).
  - UI: barra de **2 tabs** no painel direito (`rtabs`/`rtab-btn`) + container `rclasses-__TID__`; CSS novo
    (`.rtabs`, `.cls-*`, `.color-pick-free`, `.panel.hidden`). `setRightTab` alterna Edição/Classes.
  - `renderClassPanel`: prefs de visualização (por árvore), toggle Locais/Sistema, CRUD de grupos/classes.
  - Modal `modalClassEdit` (serve grupo e classe): nome, grupo (classe), ícone, **widget de cor reutilizável**
    `colorPickerHtml` (paleta `MM_COLOR_PALETTE` + `<input type=color>`).
  - Picker de ícone **generalizado** (`iconPickTarget`: 'node'|'clsEdit'; `openIconModalFor`); `setNodeIcon`/
    `clearNodeIcon` passam a marcar/limpar `node.iconCustom`.
  - CRUD: `openGroupCreate/Edit`, `openClassCreate/Edit`, `saveClassEdit`, `deleteGroup`, `deleteClass`,
    `removeClassRefs`, `countNodesUsingClass`; toggles `setIconSource`/`setClassMode`/`toggleViewFlag`/`setClassScope`.
  - `renderTab` re-renderiza a tab Classes quando ativa.
- **Implicações:**
  - Campos novos no nó (a usar nos próximos sub-passos): `classePrimaria`, `classeSecundaria`, `classeTipo`, `iconCustom`.
  - **D-1 NÃO toca no render do nó** (árvore/mind map): as classes ainda não afetam ícone/cor — isso é o D-3.
  - Próximos sub-passos: D-2 (atribuir primária/secundária ao nó no painel) · D-3 (resolução ícone/cor no render +
    migração R4) · D-4 (efeito dos toggles de visualização).
- **Verificação:** JS OK. Teste lógico headless (vm+stubs) com 12 casos — todos passam (criar grupo/classe Local e
  Sistema; Local é por-árvore e Sistema é global; ligar classe a grupo; contar uso=2; apagar limpa refs primária e
  secundária; toggles de vista isolados por árvore). Teste visual (Chrome headless): tab Classes renderiza grupo
  "Conhecimento" + classes com ícone+cor, toggles e botões. Ficheiros de teste e screenshot removidos.

## [#010] Mecanismo de DUAS VERSÕES (virgem + teste com seed "Carregar projetos")
- **Data:** 2026-06-08 (S3)
- **Plano:** _(infra de teste pedida pelo utilizador; não é um grupo do roadmap)_
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito
- **Conceito (decisão do utilizador):** a cada alteração da app passam a existir DUAS versões:
  - **`MapLab.html`** = **virgem** — a app real. **NUNCA contém qualquer referência ao bloco de teste**
    (nem botão, nem dados, nem `src`). É a única que se edita à mão.
  - **`MapLab-teste.html`** = **gerada** = virgem + bloco de teste injetado **inline** (auto-contida; abre por
    duplo-clique, sem servidor). É descartável e **não versionada** (`.gitignore`); regenera-se a cada build.
- **Como foi feito:**
  - `MapsTeste/seed-bloco.template.html` — ficheiro-fonte do bloco: botão flutuante **"⤓ Carregar projetos"**
    + `seedCarregarProjetos()` + placeholder `__SEED_DATA__` (preenchido no build com os `.md`).
  - `build-teste.js` — gerador: lê `MapLab.html` (recusa-se a correr se a virgem já contiver o bloco), **re-lê
    os `.md` de `MapsTeste/`** (dados frescos a cada geração), deriva `proj`/`tree` do nome do ficheiro
    (`P{n} - A{n} - <nome>-V<x>.md` → proj=1º segmento, tree=2º), injeta o JSON no template e cola o bloco
    inline antes de `</body>`. Uso: `node build-teste.js`.
  - O botão cria: **P1**[A1,A2] e **P2**[A1,A2,A2b] via `parseMdToFlat`+`applyMdTree` (mesmo caminho do Import MD).
  - `.gitignore` ignora `MapLab-teste.html`.
- **Implicações:**
  - **Protocolo novo:** sempre que se edita `MapLab.html`, correr `node build-teste.js` para regenerar a versão
    teste. Documentado em `instrucao-agente-alteracoes.md` (§1).
  - Os 5 `.md` de teste vivem em `MapsTeste/` (versionados); o A2b (MapaEstruturaFiles) é a 3ª árvore do P2
    (pastas+ficheiros, prefixo `_`) — útil p/ testar o Grupo I/S5 mais tarde.
  - **Bug corrigido durante o desenvolvimento:** `String.replace` substitui só a 1ª ocorrência → o placeholder
    no comentário do template era trocado em vez do código. Resolvido com `replaceAll` + remoção do marcador do
    comentário. Verificado: 0 placeholders restantes; seed popula P1[A1,A2]/P2[A1,A2,A2b] (P1-A1 com 231 nós).
- **Verificação:** JS OK (virgem e teste); virgem confirmada limpa (sem `SEED-TESTE`); harness vm corre o seed e
  devolve a estrutura correta; screenshot Chrome headless mostra P1 com A1(231 nós) carregada + botão presente.

## [#011] Grupo D, D-1 (revisão) — tab Classes redesenhada: dropdowns encadeados + modais de gestão
- **Data:** 2026-06-08 (S3)
- **Plano:** `Planodeacao-app.md` → Grupo D; correção pedida pelo utilizador à UI do D-1 (#009)
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (⏳ pendente de aceitação)
- **Motivo:** o CRUD em lista do #009 não era o pretendido. O utilizador pediu um fluxo **dropdown-cêntrico**.
- **Decisões fechadas (ronda):**
  - Dropdowns **Grupo → Classe** servem para **selecionar a classe a atribuir ao nó** (o seletor da classe ativa;
    a atribuição fina ao nó é o D-2). "Sem Grupo" é uma entrada **sempre presente** (virtual; `groupId=''`).
  - Filtro em **cascata**: escolher grupo → o dropdown de classes mostra **só as classes desse grupo** (ou as
    sem-grupo). Mudar de grupo limpa a classe selecionada.
  - **"Editar Grupos"** e **"Editar Classes"** abrem **modais dedicados** com criar / renomear / apagar /
    **reordenar por drag & drop**; nas classes, também **mudar de grupo** (dropdown por linha).
  - **Apagar grupo** → as suas classes passam para **"Sem Grupo"** (NÃO se apagam as classes).
- **Como foi feito (só `MapLab.html`):**
  - `renderClassPanel`: substituídos os botões "+ Grupo/+ Classe" e a lista por **2 `<select>` encadeados**
    (Grupo/Classe) + preview da classe selecionada + botões "Editar Grupos"/"Editar Classes" + contador.
    Estado novo em `classTab`: `selGroup`/`selClass`. Funções `selectClsGroup`/`selectClsClass`.
  - Modais novos `modalGroupsManage` / `modalClassesManage` + `renderGroupsManage`/`renderClassesManage`;
    **drag&drop isolado** (`reorderDragStart`/`reorderDrop`, estado `dragReorder`) — NÃO toca no drag de nós
    da árvore (`handleDragStart`). `setClassGroup` muda o grupo de uma classe. CSS `.manage-*`/`.drag-handle`.
  - `deleteGroup` reescrito (classes → `groupId=''`). `saveClassEdit` re-renderiza os modais de gestão se abertos.
  - `classRowHtml` removido (já não usado). `modalClassEdit` mantido (criar/renomear individual com ícone+cor).
- **Implicações:**
  - A **ordem** dos grupos/classes é a posição no array (drag&drop reordena o array). Será serializada no `.json`
    por árvore (próximo passo: criar os `.json`).
  - Render do nó continua **não** afetado (D-2/D-3/D-4 por fazer).
- **Verificação:** JS OK; `node build-teste.js`. Teste lógico headless (12 casos): filtro cascata, selecionar grupo
  limpa classe, mudar grupo de classe, apagar grupo → classes para Sem Grupo (4 classes intactas), reordenar D&D,
  D&D cross-kind ignorado. Teste visual (Chrome headless): tab com 2 dropdowns + preview + botões; modal "Editar
  Classes" com handles ⠿, dropdown de grupo por linha, ✎/🗑, "+ Nova classe". Temporários removidos.

## [#012] Grupo D — tab Classes em 3 zonas estanques + Atribuir (E incremental) + render do nó (D-3) + fix modais
- **Data:** 2026-06-09 (S3)
- **Plano:** `Planodeacao-app.md` → Grupo D (+ início do Grupo E); correções pedidas pelo utilizador
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (⏳ pendente de aceitação)
- **Plano de arquitetura:** validado por subagente (Plan) antes de codificar — 3 tarefas, zonas estanques.
- **Decisões fechadas (ronda):**
  - Modais: **pilha** (só um visível de cada vez); secundário abre com `{stacked:true}` e o de baixo reabre ao fechar.
  - 3 **zonas estanques** na tab Classes: **Visualização** (só `s.view`) · **Gestor** (só `s.classTab`) · **Atribuir** (só `s.assign`).
  - **Atribuir** (E incremental, "zona+atribuir simples"): botão Ativar edição da árvore + toggle primária/secundária;
    a classe é **sempre a viva no Gestor** (`classTab.selClass`); clicar num nó atribui (substitui a do mesmo tipo).
    Modo "aos filhos"/checkboxes/Aplicar em massa fica para depois.
  - Desvio do clique: **guarda em `selectNode`** (Opção A) — `renderTree` intocado. **Drag desligado** no modo atribuir.
  - **Render do nó (puxou o D-3 para já):** já mostra cor/ícone da classe. R1 cor Custom>Classe>Ramo; R2 modo
    prim+sec = 2 ícones (1º prim, 2º sec) cada um com a cor da sua classe/grupo; iconSource class/group; iconCustom.
  - **Campos de classe sempre presentes; vazio = `null`** (esquema `.json` estável) — não se faz `delete`.
- **Como foi feito (só `MapLab.html`):**
  - **Pilha de modais** em `showModal(id,{stacked})`/`hideModal(id)` (var `modalStack`); `openClassEditModal` e
    `openIconModal*` abrem com `{stacked:true}`.
  - `renderClassPanel` agora é **compositor**: `renderClassZoneView` + `classZoneSep()` + `renderClassZoneManager`
    + sep + `renderClassZoneAssign`. Cada sub-render devolve string e toca só no seu ramo de estado.
  - Zona Atribuir: estado `s.assign{active,tipo}` (em `initTree`; **UI volátil, não serializar**); `toggleAssignMode`,
    `setAssignTipo`, `assignClassToNode`, `activeAssignClass`, `applyAssignModeCue` (classe CSS `.assign-mode` no host).
  - `selectNode`: guarda `if(assign.active)→assignClassToNode`. `handleDragStart`: bloqueia se `assign.active`.
  - **`resolveNodeVisual(tabId,node,branchCol)`** (novo): resolve `{icons:[{slug,color}],color}` por R1/R2/R4;
    integrado no `renderTree` (a cascata de cor continua a usar a cor do ramo, não a da classe). CSS `.tree-container.assign-mode`.
- **Implicações:**
  - Campos no nó: `classePrimaria`/`classeSecundaria` (classId|`null`), `classeTipo` ('local'/'sistema'), `iconCustom`.
    Mapeiam ao `.json` S3. **`assign` NÃO entra no `.json`** (volátil).
  - **Migração R4** (node.icon sem classe → iconCustom) só importa ao carregar `.json` (próximo passo) — `setNodeIcon`
    já marca `iconCustom`, por isso não há órfãos agora; sem código morto adicionado.
  - **Limitação conhecida:** `classeTipo` é único por nó — primária local + secundária de sistema não é totalmente
    representável (reflete o último scope escrito). Dívida sinalizada; resolve-se separando em tipos por-classe quando preciso.
- **Verificação:** JS OK; `node build-teste.js`. Teste lógico headless (19 casos): estado assign; atribuir prim/sec;
  substituir; nó sistema ignorado; sem-classe não atribui; drag bloqueado; `resolveNodeVisual` (ícone class/group,
  2 ícones prim+sec, custom, iconsVisible/colorsVisible, cor R1). Teste visual (Chrome headless): 3 zonas visíveis;
  modo atribuir ativo com realce na árvore; INBOX com ★ laranja (primária) e Sent Messages com ♥+✓ (prim+sec). Temporários removidos.

## [#013] Reformulação da Visualização (view novo) + "Sem Grupo" com cor + Atribuir a filhos + scroll + botão na barra
- **Data:** 2026-06-09
- **Plano:** reformulação aprovada (§1–§6: modelo `view`, Zona1, `resolveNodeVisual`, "Sem Grupo" real, Zona3 toggle filhos, CSS scroll, botão no seed)
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (⏳ pendente de aceitação)
- **Decisões fechadas (do utilizador; não reabertas):**
  - **Cor manual manda:** R1 = Custom(`mmColor` por-nó) > Classe(prim/sec conforme `view.color`) > Ramo.
  - **Cor em falta:** `view.color='secundaria'` sem secundária/cor → cor neutra do ramo (NÃO cai para primária).
  - **"Sem Grupo":** sentinela `'__nogroup__'`, NÃO materializado em `lib.groups`; classes sem grupo mantêm `groupId=''`;
    aparência (cor/ícone) editável em `lib.noGroup={icon,color}` por scope (local + sistema). Nome fixo; sem apagar/renomear/arrastar.
  - **Grupo do nó** é DERIVADO da classe ao vivo (`classe.groupId`; vazio→Sem Grupo); não se guarda no nó.
  - **`view.source`** aplica-se a ícones E cor (escolha global). **`assign` não se serializa** (UI volátil).
- **Como foi feito (só `MapLab.html`):**
  - **§1 `DEFAULT_VIEW`** reescrito: `{source:'class',iconPrim:true,iconSec:false,color:'primaria',numeracaoVisible:false}`
    (substitui `iconsVisible/colorsVisible/classMode/iconSource`). `initTree` herda via `{...DEFAULT_VIEW}`.
  - **§2 `renderClassZoneView`** reformulada: "Mostrar por" (Grupo|Classe → `setViewSource`), "Ícones" (checkboxes
    Primário/Secundário → `toggleViewFlag('iconPrim'|'iconSec')`), "Cor" (Primária|Secundária|Desligada → `setViewColor`).
    Removidos `setIconSource`/`setClassMode`; adicionados `setViewSource`/`setViewColor` (ambos chamam `classViewChanged`).
  - **§3 `resolveNodeVisual`** reescrita: helper `visOf(c)` devolve `{slug,color}` por `v.source` (group via novo
    `resolveGroupOf(lib,c)`; class via a classe). Ícones: custom (R4) → 1 ícone cor do ramo; senão push primário (se
    `iconPrim`) e secundário (se `iconSec`), cada ícone com cor da classe/grupo ou fallback ramo. Cor: Custom>alvo(prim/sec)>ramo.
  - **§4 "Sem Grupo" real:** `systemLib`/`initTree.localLib` ganham `noGroup:{icon:'',color:''}`; helper `resolveGroupOf`;
    row fixa "Sem Grupo" em `renderGroupsManage` (swatch+ícone, `draggable=false`, só ✎); novo `kind:'nogroup'` em
    `openNoGroupEdit`/`openClassEditModal` (esconde campo nome + group row)/`saveClassEdit` (grava em `lib.noGroup`).
  - **§5 Zona3:** `assign.toChildren` (em `initTree`); preview "A atribuir (...)" removido; view-toggle Sim|Não
    "A filhos" → `setAssignToChildren`; `assignClassToNode` extrai `applyTo(node)` e, se `toChildren`, walk recursivo
    (ignora `isSystem`).
  - **§6a CSS:** `.right-pane` ganha `min-height:0;overflow:hidden` (permite o `.panel{overflow:auto}` encolher e fazer scroll).
- **Como foi feito (`MapsTeste/seed-bloco.template.html`, SÓ no seed):**
  - **§6b** botão `#seedTesteBtn` deixa de ser `position:fixed`; passa a ser injetado por JS na `.app-header`
    (`margin-left:auto`, estilo compacto). Não usa `#projectBar`/`editor-btns` (reescritos por innerHTML). `build-teste.js` intocado.
- **Implicações:**
  - Modelo `view` mudou de forma — `.json` S3 da view passa a serializar `source/iconPrim/iconSec/color/numeracaoVisible`.
  - `lib.noGroup` é novo campo de lib (local e sistema) a entrar no `.json` quando a persistência chegar.
  - `assign.toChildren` é volátil (não serializa, como o resto de `assign`).
  - Render do nó deixou de depender de `iconsVisible/colorsVisible` (sempre mostra ícones conforme iconPrim/iconSec).
- **Verificação:** virgem JS OK + sem `SEED-TESTE`. Teste lógico headless (28 asserts, todas passaram): novo `view` em
  `initTree`; `resolveNodeVisual` (source class/group, iconPrim/iconSec, cor primaria/secundaria/off, custom R1,
  cor em falta→ramo, `resolveGroupOf` Sem Grupo derivado); `assign.toChildren` (subárvore vs só nó, ignora sistema).
  `node build-teste.js` OK (teste tem `SEED-TESTE`+`seedTesteBtn`). Screenshots (Chrome headless): tab Classes com as 3
  zonas novas (Mostrar por / Ícones prim+sec / Cor prim-sec-off; toggle "A filhos"); botão "Carregar projetos" na barra
  de cima; modal Editar Grupos com row fixa "Sem Grupo" (ícone+cor, só ✎). Temporários removidos.

## [#014] Correções: vista segue o modo Atribuir; nós sem classe a cinzento neutro
- **Data:** 2026-06-09
- **Plano:** correções pedidas pelo utilizador à tab Classes (#013)
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (⏳ pendente de aceitação)
- **Como foi feito (só `MapLab.html`, em `resolveNodeVisual`, linhas 608–635):**
  - **Correção 1 — vista efetiva `vf`:** no início da função, se `s.assign.active` constrói
    `vf={source:s.view.source, iconPrim:(tipo==='primaria'), iconSec:(tipo==='secundaria'), color:tipo}`;
    senão `vf=s.view`. Substituídas todas as referências `v.` por `vf.` no resto da função
    (origem `visOf`, flags de ícones, alvo de cor). `renderTree` intocado (override isolado). No modo
    Atribuir mostra SÓ o tipo escolhido (esconde o outro) e a origem Grupo/Classe herda de `view.source`.
  - **Correção 2 — fallback da cor do texto = cinzento neutro:** `let color` passou de `branchCol` para
    `'var(--text)'` (#c8d6e5, a variável de texto principal do CSS). Ordem final inalterada na intenção:
    Manual(`mmColor`) > Classe/Grupo(conforme `vf`) > `var(--text)`. `branchColor` NÃO foi tocado — continua
    a alimentar a cor dos ícones de classe (fallback), o ícone custom (R4, cor do ramo) e a cascata/mind map.
- **Implicações:**
  - Nós sem classe do tipo mostrado deixam de herdar a cor do ramo/árvore no texto (passam a cinzento).
  - No modo Atribuir, a árvore deixa de refletir `s.view`; reflete o tipo selecionado na Zona Atribuir
    (re-render garantido: `assignClassToNode`/`toggleAssignMode`/`setAssignTipo` já re-renderizam).
- **Verificação:** virgem JS OK + sem `SEED-TESTE`. Teste lógico headless (15 asserts, todas passaram):
  assign off→usa `s.view` (2 ícones, cor primária); assign primária→só ícone/cor primária (sec escondida);
  assign secundária→só secundária; assign sec num nó sem secundária→sem ícone e cor `var(--text)`;
  sem classe→`var(--text)` (não branchCol); só primária→cor da classe; `mmColor` manda sobre classe;
  ícone custom→cor do ramo (R4 intacta); assign ignora `view.iconSec`. `node build-teste.js` OK.
  Screenshot (Chrome headless): modo Atribuir tipo Secundária — nós com 2ª classe mostram ♥ rosa,
  nós com só 1ª classe NÃO mostram ★ (esconde primária), nós sem classe a cinzento neutro. Temporários removidos.

<!-- Próximas entradas: append abaixo desta linha. -->

## [#015] Painel de edição partilhado no side-by-side + colunas redimensionáveis
- **Data:** 2026-06-09
- **Plano:** painel de edição no side-by-side + colunas redimensionáveis (pedido do utilizador)
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito (⏳ pendente de aceitação)
- **Como foi feito (só `MapLab.html`):**
  - **Estado novo (≈l.551):** `let sideActiveTab=null;` + `const sideColWidth={};` + helpers
    `sideActiveValid()` (devolve `sideActiveTab` se existir no projeto ativo, senão 1ª árvore, senão null)
    e `sideViewActive()` (`activeTab==='side'`). `switchProject` faz `sideActiveTab=null`.
    `disposeTree` passou a limpar também `sideColWidth[treeId]`.
  - **Reutilização sem duplicar:** `renderPanel(tabId,hostId)` e `renderClassPanel(tabId,hostId)` ganham
    2º arg opcional (host alternativo; callers normais inalterados). `setRightTab(tabId,which,scope)`
    (≈l.789): com `scope==='side'` escreve nos ids `side-rtab-edicao/classes`, `side-rpanel`,
    `side-rclasses` e passa o hostId certo aos dois renders; senão caminho normal.
  - **HTML/Template/CSS:** `#panel-side` passou a `.side-stage` (flex row) = `#sidePanel` (colunas, flex:1)
    + `#sideEditPanel` (260px, border-left) com rtabs (`setSideRightTab`), `#side-rpanel`, `#side-rclasses`.
    Botão **"↔ Largura igual"** no cabeçalho (`sideEqualWidths()`). `sideColTemplate`: título clicável
    (`setSideActive`, `data-side-title`, cursor:pointer) + `.side-col-resizer` na borda direita
    (`sideResizeStart`) + id `side-col-__TID__`. CSS novo: `.side-stage`, `#sideEditPanel`,
    `.side-col-title.side-active`, `.side-col.side-active-col`, `.side-col-resizer`,
    `.side-tree.assign-mode`/`.side-tree.assign-mode .side-node`, `.side-col{position:relative}`.
  - **`renderSideTree(tabId,nodes,expSet,depth,inheritedColor)` (≈l.1474):** passou a usar
    `branchColor`+`resolveNodeVisual` (ícones de classe via `iconSvg(slug,color,12)`, cor do nome = `vis.color`)
    em vez de `getNodeIcon`. Seleção SÓ na coluna ativa (`tabId===sideActiveTab`): adiciona
    `onclick="selectNode(...)"` + cursor:pointer + realce `.selected`; colunas inativas sem onclick.
    Toggle de expand mantém `event.stopPropagation()` em qualquer coluna.
  - **`refreshSide` (≈l.1444):** normaliza `sideActiveTab=sideActiveValid()`; aplica `sideColWidth[t.id]`
    (`flex:0 0 Wpx`+width) ou `flex:1` por defeito; aplica `.side-active`/`.side-active-col`/`assign-mode`
    à coluna ativa; chama `renderSidePanel()`.
  - **Re-render agnóstico:** `renderTab` e `renderActiveView` ganham guarda no topo
    `if(sideViewActive()){refreshSide();return;}` — mutações existentes re-renderizam o side sem alterar
    cada função. (`renderTab` mantém também o `||tabId==='side'`.)
  - **Funções novas** (bloco `// ── SIDE EDIT (painel partilhado + resize) ──`): `setSideActive`,
    `setSideRightTab`, `renderSidePanel` (placeholder se sem árvore), `sideResizeStart`/`sideEqualWidths`.
- **Implicações:**
  - `sideColWidth` é estado de sessão (UI volátil) — **NÃO serializar** no `.json` (como `assign`).
  - O painel partilhado reutiliza `tabState[tabId].classTab.active` por árvore (a tab edição/classes
    do side segue a mesma preferência da vista normal dessa árvore).
  - Nenhuma função de mutação foi alterada; o side acompanha por causa das guardas em renderTab/renderActiveView.
- **Verificação:** virgem JS OK + sem `SEED-TESTE`. Teste lógico headless (19 asserts, todas passaram):
  `sideActiveValid` (default 1ª árvore; revalida ao apagar; null sem projetos); `setSideActive`;
  `setRightTab scope='side'` escreve nos ids `side-*`; `renderSideTree` de nó com classe contém `<svg`;
  coluna ativa tem `selectNode` e inativa não; `selectNode` muda `s.selected`; `sideColWidth` aplicada e
  `sideEqualWidths` limpa; `sideViewActive` reflete `activeTab`; `disposeTree` limpa `sideColWidth`;
  **regressão:** com `activeTab!='side'`, `renderTab` NÃO chama `refreshSide` (caminho normal), e com
  `activeTab='side'` chama. `node build-teste.js` OK. Screenshots (Chrome headless): (i) side com 2 colunas,
  A1 ativa destacada (título + barra accent) e nó INBOX selecionado, painel à direita 260px; (ii) modo
  Atribuir ativo no side (tab Classes, "Edição da árvore ATIVA", cue na coluna ativa); (iii) coluna A1
  redimensionada (~520px) com painel à direita intacto. Temporários removidos.

## [#016] Seed de teste: grupos/classes pré-feitos no "Carregar projetos" — só na versão teste
- **Data:** 2026-06-09
- **Plano:** seed de teste: grupos/classes pré-feitos no Carregar projetos — só na versão teste
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** feito
- **Como foi feito (só `MapsTeste/seed-bloco.template.html`):**
  - **`safeIcon(name, fallback)`** (l.21): helper que devolve o nome do ícone se `iconExists(name)`,
    caso contrário tenta o fallback ('star'), caso contrário ''. Usado em todas as criações de grupos/classes.
  - **`seedSystemLib()`** (ll.23-34): cria 1 grupo ("Classes de conhecimento", cor `#ef4444`,
    ícone `graduation-cap`) + 5 classes (Orçamento/Planeamento com `groupId:''`; C1/C2/C3 apontam ao grupo).
    Guard de idempotência no topo: `if(systemLib.groups.length||systemLib.classes.length) return;`.
  - **`seedLocalLib(treeId)`** (ll.36-45): cria 1 grupo ("DominiosVida", cor `#bb86fc`, ícone `compass`)
    + 3 classes (Camada0/Manutenção apontam ao grupo; Night com `groupId:''`). Cada chamada gera `newId`
    novos — sem partilha de referências entre árvores.
  - **`seedCarregarProjetos` — pontos de inserção:**
    - l.48: `seedSystemLib()` logo no início (antes do loop de projetos).
    - l.62: `seedLocalLib(t.id)` logo a seguir a `initTree(t.id)`, antes de `parseMdToFlat`/`applyMdTree`.
- **Implicações:** alteração restrita à versão teste. A virgem `MapLab.html` permanece intacta e
  sem qualquer referência a `seedSystemLib`/`seedLocalLib`/`SEED-TESTE`. Os marcadores
  `SEED-TESTE START/END`, a linha `const SEED_FILES = __SEED_DATA__;` e o `renderWorkspace()` final
  não foram tocados.
- **Verificação:** `node build-teste.js` OK (419 KB). Virgem intacta (grep: 0 ocorrências).
  Sintaxe JS: 2 blocos `<script>` validados com `new Function`, sem erros.
  Teste funcional headless (vm, 44 asserts, 0 falhas): `systemLib.groups.length===1`,
  `systemLib.classes.length===5`; Orçamento/Planeamento `groupId===''`; C1/C2/C3 apontam ao grupo;
  5 árvores criadas; cada árvore com `localLib.groups.length===1` e `localLib.classes.length===3`;
  Night `groupId===''`; Camada0/Manutenção apontam ao grupo DominiosVida; IDs de grupo distintos
  entre todas as árvores; idempotência confirmada (2ª chamada: `systemLib.classes.length` continua 5).


## [#018] Correção de paridade side-by-side: host centralizado para o painel + expand/colapsar respeita seleção + cue Atribuir
- **Data:** 2026-06-10
- **Plano:** correção de paridade side-by-side — auditoria identificou 4 bugs onde funções da tab Classes e do expand/colapsar se comportavam diferentemente no side vs. na vista normal.
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** ⏳ pendente de aceitação
- **Como foi feito (só `MapLab.html`):**
  - **Correção B (host centralizado, principal):** `renderClassPanel` (~l.813) e `renderPanel` (~l.701): adicionada linha no início de cada função — `if(sideViewActive())hostId='side-rclasses';` e `if(sideViewActive())hostId='side-rpanel';` — que força o host do painel side quando a vista side está ativa. Isto faz com que QUALQUER chamada sem hostId (das funções de zona: `setClassScope`, `selectClsGroup`, `selectClsClass`, `toggleAssignMode`, `setAssignTipo`, `setAssignToChildren`, `classViewChanged`/`setViewSource`/`setViewColor`/`toggleViewFlag`, `saveClassEdit`, `deleteGroup`, `deleteClass`, `setClassGroup`, `reorderDrop`) escreva automaticamente no painel correto do side.
  - **Correção A (expand/colapsar respeita seleção):** `sideExpandToLevel`, `sideCollapseAll`, `sideCollapseBelow` (~l.1524–1545): replicada a lógica `if(s.selected){...}` das funções normais (`expandToLevel`/`collapseAll`/`collapseBelow`), mas operando sobre `sideExpanded[tabId]` em vez de `s.expanded`. Com seleção: `sideExpandToLevel` semeia o walk a partir do nó selecionado, adicionando ao Set existente (sem limpar o resto); `sideCollapseAll` remove só os ids de `descendantBranchIds(root)`; `sideCollapseBelow` análogo. Sem seleção: comportamento anterior (toda a árvore).
  - **Correção D (cue do modo Atribuir):** `toggleAssignMode` (~l.885): quando `sideViewActive()`, chama `refreshSide()` (que reaplica `.assign-mode` ao `side-tree-<sideActiveTab>` e re-renderiza) em vez de `applyAssignModeCue(tabId)`.
  - **Correção C (cor/ícone no side):** NÃO foi necessária. `setNodeColor`/`clearNodeColor` chamam `renderPanel` — já coberto pela Correção B. `setNodeIcon`/`clearNodeIcon` chamam `renderTab` que em side faz `refreshSide(); return` — e `refreshSide` chama `renderSidePanel` → `setRightTab(...,'side')` → passa `'side-rclasses'`/`'side-rpanel'` explicitamente, logo o painel já atualizava corretamente. Zero linhas adicionadas para C.
- **Implicações:** qualquer função de zona que chame `renderClassPanel(tabId)` ou `renderPanel(tabId)` sem hostId passa a escrever no painel side correto quando em contexto side, sem precisar de alterações nessas funções. A regressão (vista normal) está coberta por teste. `sideExpanded` e `s.expanded` continuam como stores separados — a Correção A só toca `sideExpanded`.
- **Verificação:** JS OK. `node build-teste.js` OK (virgem sem SEED-TESTE). Teste headless (vm, 22 asserts, 0 falhas): A1–A6 (expand/colapsar com e sem seleção), B1–B6 (host correto com regressão), D1–D3 (toggleAssignMode side e normal). Screenshots Chrome headless: side-by-side com tab Classes aberta, Locais (1 grupo · 3 classes) vs. Sistema (1 grupo · 5 classes) — os dois painéis diferem conforme esperado.

## [#017] Correção: scope Sistema/Local não deve afetar a visualização; classe do nó resolvida em ambas as libs por id
- **Data:** 2026-06-10
- **Plano:** correção de bug — `resolveNodeVisual` usava uma única biblioteca escolhida por `node.classeTipo`, fazendo desaparecer o ícone/cor quando a primária e secundária vêm de libs diferentes (Sistema vs Local).
- **Branch/Commit:** `App-Generica` / _(a commitar)_
- **Estado:** ⏳ pendente de aceitação
- **Como foi feito (só `MapLab.html`, função `resolveNodeVisual` ~l.633):**
  - **Removida** a linha `const lib=node.classeTipo==='sistema'?systemLib:lib0;` que escolhia UMA só lib pelo campo único do nó.
  - **Adicionado helper inline `clsWithLib(cid)`**: procura primeiro em `systemLib.classes`, depois em `s.localLib.classes`; devolve `{c, lib}` ou `null`. Assim a resolução é imune ao `classTab.scope` — encontra a classe pelo seu id único em qualquer das duas libs.
  - **`visOf(cid)`** reformulado para receber o `cid` diretamente (em vez do objeto `c`): chama `clsWithLib` internamente e resolve o grupo via `resolveGroupOf(lib, c)` usando a lib de onde a classe veio — garante que o `noGroup` usado é o da lib certa.
  - **Chamadas** a `visOf` e à cor do nó passam agora `node.classePrimaria` / `node.classeSecundaria` (cids) em vez dos objetos já resolvidos.
  - `node.classeTipo` mantido para compatibilidade/serialização mas já **não é usado** na resolução visual.
  - `lib0` e `cls()` removidos (tornaram-se dead code após a refatoração).
- **Implicações:** resolve a dívida registada em #012 (classeTipo único por nó impedia classes mistas Sistema/Local). A partir de agora, um nó pode ter primária de Sistema e secundária de Local (ou vice-versa) e ambas aparecem. O toggle Locais/Sistema no Gestor deixa de afetar a visualização — afeta apenas "o que vou atribuir". `renderTree` e `renderSideTree` não foram tocados (apenas chamam `resolveNodeVisual`). Nenhuma leitura de `classTab.scope`/`selGroup`/`selClass` no caminho de render — confirmado por Grep (estas variáveis só aparecem em `scopeLib`, `renderClassPanel`, `selectClsGroup`, `selectClsClass`, `activeAssignClass`, `assignClassToNode`, `setClassScope` — todas fora do render de árvore).
- **Verificação:** JS OK (validação `new Function`). `node build-teste.js` OK (419 KB, virgem intacta). Teste headless (vm, 14 asserts, 0 falhas): [1-5] 2 ícones (star+heart) com `assign.active=false, iconPrim+iconSec=true`; [6-9] scope muda local↔sistema → resultado idêntico (imune); [10-11] cor primária=#ff0000 / secundária=#0000ff; [12] só primária → 1 ícone; [13] iconCustom → 1 ícone custom (R4 intacta); [14] Atribuir ativo tipo=secundaria → 1 ícone (L1). Screenshot Chrome headless: 2 PASS confirmados (2 ícones presentes; scope=sistema → mesmo resultado).
