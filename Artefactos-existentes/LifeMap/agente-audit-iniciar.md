# Log de Retomas de Sessão — agente "inicia" (APPEND-ONLY)

> Registo obrigatório exigido pela §0bis de `instrucao-agente-alteracoes.md`. Append-only:
> cada retoma acrescenta uma secção nova datada. Nunca apagar/editar secções anteriores.

---

## [RETOMA] 2026-06-08 — agente novo, sem contexto (ENTRADA DE TESTE)

> Esta entrada é uma **retoma de teste**: o agente NÃO executou a §5 (não perguntou
> continuar/auditoria ao utilizador) e NÃO tocou em código nem em mais nenhum ficheiro.
> Apenas leu, inferiu o estado e registou aqui.

### Ficheiros lidos, por ordem, e o que entendi de cada um
1. **`instrucao-agente-alteracoes.md`** — Processo governado de alterações ao `MapLab.html`
   (single-file, sem build). Define a §0bis (ordem de leitura na retoma + este registo
   obrigatório), as 2 fases (APP/SERVER), o mapa de ficheiros e as regras (só editar
   `MapLab.html`; Arqueologia read-only; snapshot só por marco aceite; não commitar sem pedido).
2. **`handoff.md`** — Estado imediato. Branch ativa = `App-Generica` (não `main`). A→B→C
   (app genérica, ícones Notion, rename MapLab) feitos e **aceites**. Próximo passo de código =
   Ordem 4 (Persistência base). Tensões: app↔server acoplados pelo `.json`; `lifemap_lab*.html`
   redundantes na raiz; nomes das versões de classe por confirmar.
3. **`registo-auditoria.md`** (append-only) — 2 auditorias por subagentes "às cegas":
   AUD-001 (onboarding ✅ suficiente; lacunas 1 e 5 resolvidas; 2,3,4 menores em aberto) e
   AUD-002 (implementabilidade: D/E/F/G/S1–S3 "com pressupostos"; reconciliação colisão,
   S5 e S6 "insuficientes"; 10 lacunas; ação prevista = ronda de perguntas ao utilizador).
4. **`roadmap.md`** — Visão única que une as 2 fases. Fase 1 (app): A/B/C feitos; D Classes &
   Grupos / E atribuição em massa / F versões de classe / G side-by-side por implementar.
   Fase 2 (server): S1+S2+S3 persistência base (Ordem 4, pré-requisito das classes), S4, S5, S6.
5. **`Planodeacao-app.md`** — Executável da app. Grupos A/B/C ✅ ACEITE (2026-06-08); D (Ordem 5),
   E (6), F (7), G (8) por fazer, Branch/Commit "a definir".
6. **`Planodeacao-server.md`** — Executável do server. S1/S2/S3 (Ordem 4) por fazer; S4 (7),
   S5 (9), S6 (10). Servidor Python stdlib OPCIONAL com fallback memória; não exposto à rede.
7. **`log-alteracoes.md`** (append-only) — #001 App genérica, #002 Ícones, #003 Rename+governação,
   #004 Roadmap reaberto + A/B/C aceites + propagação do rename. Implicações registadas
   (campo `node.icon`, serialização futura, reconciliação `nome+nivel+pai`).
8. **§1–§4 de `instrucao-agente-alteracoes.md`** — Arquitetura do `MapLab.html` (modelo
   `workspace`, `tabState[treeId]`, factory de painéis, bloco estanque de ícones), as 2 fases,
   mapa de ficheiros do processo e regras de atuação.
9. **Estado real (git + validação):** `git log -1`, `git status`, validação JS e hash do blob.

### Estado atual inferido
- **Branch:** `App-Generica` (confirmado por `git branch --show-current`).
- **Commit (HEAD):** `65e9797` — "MapLab: app generica + icones + sistema de governacao de alteracoes".
- **`MapLab.html` blob:** `ef140702d86fb3e7f209a6899d746168c2c5c48d` (= `ef14070`, bate certo com
  o registado em AUD-001/AUD-002). Validação JS: **JS OK**.
- **`git status`:** modificados `instrucao-agente-alteracoes.md` e `questionario-validacao.md`;
  untracked `registo-auditoria.md`. (Não commitei nada — fora do âmbito.)
- **Marcos aceites:** A (app genérica, Ordem 1), B (ícones, Ordem 2), C (rename MapLab, Ordem 3)
  — todos ✅ ACEITE em 2026-06-08. Snapshots 00/01/02 congelados na Arqueologia.
- **Próximo item `[ ]` na ordem global:** **Ordem 4 — Persistência base (S1+S2+S3)** no
  `Planodeacao-server.md`. É pré-requisito declarado do Grupo D (Classes, Ordem 5).

### Lacunas / decisões pendentes vistas no `registo-auditoria.md`
- **🔴 Tensão de ordem D ↔ Ordem 4** (AUD-002 #1): o `.json` da persistência base precisa de
  campos de classe que só nascem no Grupo D. Decidir: (a) especificar o `.json` completo antes
  de ambos, ou (b) dividir a Ordem 4 em "estrutura" + "extensão de classes (com D)".
- **🔴 Política de colisão na reconciliação** (AUD-002 #2): irmãos homónimos colidem na chave
  `nome+nivel+pai` — comportamento indefinido.
- **🟡 E — primária vs secundária no "Aplicar"** não especificado (#3).
- **🟡 D — defaults e widget de cor** (`iconSource`, modo de cor, falta color-picker) (#4).
- **🟡 D — escopo das flags de visualização** (por árvore/projeto/global? persistem?) (#5).
- **F/S4 — esquema de nomes das versões em ficheiros** por confirmar (#6).
- **S1 — contrato dos endpoints** por especificar (apontar p/ `TableEditorApp/acc_server.py`) (#7).
- **S5/S6 — decisões em aberto** tornam-nos não-implementáveis sem confirmar (#8).
- **Menores:** fragilidade do comando de validação JS / regex de `<script>` (AUD-001 #2, AUD-002 #9);
  teste visual sem receita fixa e caminho do Chrome fixo (AUD-001 #3); saltos na ordem global
  (3→5) (AUD-001 #4); inconsistência cosmética log "pendente" vs planos "aceite" (AUD-002 #10).
- **Ação prevista (ainda `[ ]`):** ronda de perguntas ao utilizador para fechar lacunas 1–8 antes
  de implementar a Ordem 4 / Grupo D.

### Conclusão
- **Pronto a continuar/auditar?** Sim. A §0bis foi suficiente para reconstruir o estado sem
  contexto prévio. Documentação, planos, log e código estão **mutuamente coerentes** e o estado
  real do git/validação bate certo com o declarado.
- **Incoerências entre ficheiros:** nenhuma material. Apenas notas menores já registadas nas
  auditorias: (i) log mostra A/B/C como "⏳ PENDENTE" enquanto planos/roadmap dizem "✅ ACEITE" —
  é esperado (log é append-only; a aceitação está em #004); (ii) `registo-auditoria.md` está
  untracked (ainda por commitar) — fora do meu âmbito nesta retoma.
- **Nota de processo:** a tensão de ordem 🔴 (D ↔ Ordem 4) continua **por decidir** e deve ser
  resolvida com o utilizador ANTES de implementar a Ordem 4, sob pena de refazer o `.json`.
- **Pergunta da §5 (NÃO executada neste teste):** _"Queres que CONTINUE as alterações (e a partir
  de que ponto/ordem do plano), ou preferes que faça uma AUDITORIA do estado atual?"_
- **Próximo item de trabalho recomendado:** resolver a ronda de perguntas (lacunas 1–8 da AUD-002),
  começando pela tensão de ordem 🔴, e só depois implementar **Ordem 4 — Persistência base (S1+S2+S3)**.

<!-- Próximas retomas: append abaixo desta linha. -->

---

## [RETOMA] 2026-06-11 — S4, arranque de sessão nova

### Ficheiros lidos, por ordem, e o que entendi de cada um
1. **`handoff.md`** — Esta sessão = S4 (anterior = S3). Branch `App-Generica`, HEAD `5394c95`, blob `012e5ab`. Feito em S3: Grupo D (Classes&Grupos, em memória), E parcial, G parcial, infra de teste D22. Tudo ⏳ pendente de aceitação. Próximo recomendado = `.json` por árvore (Fase 2, ordem 8) — ou E (Aplicar em massa) ou H (Numeração).
2. **`registo-auditoria.md`** — AUD-001/002/003 + RESOLUÇÃO (todas lacunas 1-8 fechadas). Grupo I ("a debater") único ponto não resolvido. Sem novas auditorias desde S3.
3. **`roadmap.md`** — REORDENAÇÃO S3 "front-end primeiro". Estado: D feito, E/G parciais, ⏳ pendentes. Ordem 8 = `.json` por árvore + S7 Portabilidade (Fase 2). Alternativas: E, H.
4. **`Planodeacao-app.md`** — A/B/C ✅ ACEITE; D `[x]` ⏳; E `[~]` ⏳; G `[~]` ⏳; H/F/I/J `[ ]`.
5. **`log-alteracoes.md`** (#001-#018) — D, E parcial, G parcial e infra de teste tudo registado. Logs #008-#018. Commits pushed (HEAD `5394c95`).
6. **`instrucao-agente-alteracoes.md` §1-§4** — arquitetura, regras DUAS VERSÕES, Arqueologia read-only.
7. **Estado real:** HEAD `5394c95` ("Fecho S3: continuidade"), working tree limpa, JS OK.

### Estado atual inferido
- **Branch:** `App-Generica`, uptodate com origin.
- **HEAD:** `5394c95` — "Fecho S3: continuidade (Grupos, side-by-side, seed)".
- **`MapLab.html`:** JS OK; blob `012e5ab`. Virgem limpa (sem bloco de teste).
- **Marcos aceites:** A/B/C (Ordens 1-3). D/E/G ⏳ pendentes de aceitação.
- **Próximo item `[ ]` recomendado:** `.json` por árvore (Ordem 8, Fase 2) — OU completar E OU H.

### Lacunas / decisões pendentes
- **D/E/G pendentes de aceitação formal** — sem snapshot na Arqueologia até aceitar.
- **Grupo I** continua "a debater em detalhe".
- Menores: fragilidade do regex de validação JS na versão teste; teste visual sem receita fixa.

### Conclusão
Pronto a continuar. Working tree limpa, JS OK, documentação coerente com o código. Sem incoerências materiais entre `handoff.md`, `context.md` e `roadmap.md`.

### Pergunta da §5
**"Queres que CONTINUE as alterações (e a partir de que ponto/ordem do plano), ou preferes que faça uma AUDITORIA do estado atual?"**

---

## [RETOMA] 2026-06-08 — S3, arranque de sessão nova

### Ficheiros lidos, por ordem, e o que entendi de cada um
1. **`handoff.md`** — Branch ativa = `App-Generica` (HEAD = `d2310f5`). Marcos A/B/C aceites. Próximo passo = Ordem 4 (Persistência base) ou debater Grupo I. Tensão D↔4 resolvida (esquema `.json` completo definido no S3). Commits pushed, working tree limpa.
2. **`registo-auditoria.md`** — AUD-001/002/003 + RESOLUÇÃO: todas as lacunas 1-8 fechadas pela ronda de perguntas. Grupo I (filtros/ficheiros) é o único ponto "a debater em detalhe" ainda pendente.
3. **`roadmap.md`** — Visão: Fase 1 (A/B/C feitos; D/E/F/G/H/I por fazer) + Fase 2 (S1-S8). Ordem global: pré-requisito persistência (4) antes de classes (5).
4. **`Planodeacao-app.md`** + **`Planodeacao-server.md`** — A/B/C ✅ ACEITE; próximo `[ ]` = Ordem 4 (S1+S2+S3 persistência base) no server plan; depois D (Ordem 5) na app.
5. **`log-alteracoes.md`** — 6 entradas (#001–#006); código intacto (blob `ef14070`) desde #001–#003; #004–#006 são apenas alterações de planeamento/docs.
6. **`instrucao-agente-alteracoes.md` §1–§4** — arquitetura, fases, mapa e regras (já conhecidas da retoma anterior).
7. **Estado real:** `git log -3` mostra HEAD = `d2310f5` ("Fecho S2: handoff + memory"); `git status` = working tree clean; `JS OK` confirmado.

### Estado atual inferido
- **Branch:** `App-Generica`, uptodate com origin.
- **Commit (HEAD):** `d2310f5` — "Fecho S2: handoff + memory".
- **`MapLab.html`:** JS OK; blob `ef14070` (inalterado desde S2).
- **Marcos aceites:** A (Ordem 1), B (Ordem 2), C (Ordem 3) — todos ✅ ACEITE.
- **Próximo item `[ ]` na ordem global:** **Ordem 4 — Persistência base (S1+S2+S3)** (`Planodeacao-server.md`). Pré-requisito de Classes (Ordem 5).

### Lacunas / decisões pendentes
- **Grupo I (filtros/ficheiros na vista):** "a debater em detalhe" — único ponto não fechado.
- Menores da AUD-001 (2, 3, 4) ainda abertas: fragilidade do regex JS, teste visual sem receita fixa, salto 3→5 não explicado localmente.

### Conclusão
Documentação, planos, log e código coerentes. Working tree limpa, JS OK. Pronto a continuar.

### Pergunta da §5
**"Queres que CONTINUE as alterações (e a partir de que ponto/ordem do plano), ou preferes que faça uma AUDITORIA do estado atual?"**

---

## [RETOMA] 2026-06-10 — agente novo, arranque de sessão (validação de continuidade)

### Ficheiros lidos, por ordem, e o que entendi de cada um
1. **`instrucao-agente-alteracoes.md`** (completo) — Processo governado de alterações ao `MapLab.html` (single-file). §0bis define a ordem de retoma; §1 a arquitetura (modelo `workspace`, `tabState[treeId]`, bloco estanque de ícones, mecanismo das DUAS VERSÕES); §2 as 2 fases; §4 as regras (só editar a virgem; Arqueologia read-only; não commitar sem pedido).
2. **`handoff.md`** — Estado imediato de S3. Branch `App-Generica`, HEAD `acfe5f6`, blob `012e5ab`. Feito: D (Classes&Grupos, em memória), E parcial, G parcial, infra de teste (D22). Tudo ⏳ pendente de aceitação. Próximo recomendado = `.json` por árvore (entrada na Fase 2).
3. **`registo-auditoria.md`** — AUD-001/002/003 + RESOLUÇÃO. Onboarding/implementabilidade/retoma validados por subagentes "às cegas". Lacunas 1-8 da AUD-002 fechadas pela ronda. Único ponto a debater: Grupo I (filtros/ficheiros).
4. **`roadmap.md`** — Visão. REORDENAÇÃO S3 "front-end primeiro": toda a Fase 1 antes da Fase 2. Estado no fecho S3: D feito, E/G parciais, próximo = `.json` por árvore (ordem 8).
5. **`Planodeacao-app.md`** — Grupos A/B/C ✅ ACEITE; D `[ ]` mas FOCO; E `[~]`; F `[ ]`; G `[~]`; H/I/J `[ ]`. Branch/Commit "a definir" em D-J (não atualizados apesar do trabalho — ver incoerência abaixo).
6. **`Planodeacao-server.md`** — Toda a Fase 2 `[ ]`. Esquema `.json` por árvore definido em S3. Ordem 8 = S1+S2+S3+S7.
7. **`log-alteracoes.md`** — #001-#018 (com #017 colocado fora de ordem cronológica, depois de #018 — append-only, aceitável). #009-#018 documentam o Grupo D, E/G parciais e infra de teste, todos em `App-Generica`, todos "a commitar".
8. **`agente-audit-iniciar.md`** — 2 retomas anteriores (ambas 2026-06-08), úteis mas com estado já desatualizado (apontavam Ordem 4 = persistência, pré-reordenação).
9. **Estado real (git+JS):** ver abaixo.

### Estado atual inferido
- **Branch:** `App-Generica` (confirmado).
- **HEAD:** `acfe5f6` ("Side-by-side paridade: classes + expand/colapsar OK") — **bate certo** com o handoff.
- **`MapLab.html` blob:** `012e5ab` — **bate certo** com o handoff (`012e5ab`).
- **Validação JS:** **JS OK** (virgem).
- **`git status`:** modificados `context.md`, `handoff.md`, `memory.md`, `roadmap.md` — exatamente os 4 ficheiros que o handoff diz estarem "a commitar no fecho" da S3. NÃO commitados ainda.
- **Verificação no código (Grep, não leitura):** confirmados `systemLib`, `localLib` (em `initTree` l.533), `resolveNodeVisual` (l.633), as 3 zonas `renderClassZoneView`/`Manager`/`Assign` (ll.823/841/873), `sideActiveTab`/`sideViewActive`/`sideActiveValid` (ll.554-555). Virgem **limpa** do bloco de teste (0 ocorrências de `SEED-TESTE`/`seedCarregarProjetos`/`seedSystemLib`). Seed em `MapsTeste/seed-bloco.template.html` existe.
- **Marcos aceites:** A/B/C (Ordens 1-3). D/E/G ⏳ pendentes de aceitação (sem snapshot na Arqueologia).
- **Próximo item recomendado:** `.json` por árvore (Fase 2, ordem 8) — OU completar E (modo custom/Aplicar) OU Grupo H.

### Lacunas / decisões pendentes
- **D/E/G pendentes de aceitação formal** — o utilizador ainda não confirmou; sem snapshot congelado.
- **Grupo I** continua "a debater em detalhe".
- **Limitação `classeTipo` único** mitigada por D20 (#017) — só relevante na serialização.
- Menores: fragilidade do regex de validação JS na versão teste (usar a virgem); teste visual sem receita fixa.

### Conclusão
Pronto a continuar. Documentação de continuidade **coerente com o código real** — git (HEAD `acfe5f6`, blob `012e5ab`), JS OK e todos os símbolos declarados confirmados no código. Incoerência menor: os campos Branch/Commit dos Grupos D-J nos `Planodeacao-*.md` continuam "a definir" apesar de D/E/G já terem código e commits — o estado vivo está nos checkboxes/handoff/log, não nas tabelas. Não bloqueante. Sem incoerências materiais.

### Pergunta da §5
**"Queres que CONTINUE as alterações (e a partir de que ponto/ordem do plano), ou preferes que faça uma AUDITORIA do estado atual?"**
