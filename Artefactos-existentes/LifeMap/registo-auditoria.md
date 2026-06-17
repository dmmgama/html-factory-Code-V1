# Registo de Auditoria — MapLab (APPEND-ONLY)

> **Propósito.** Histórico das auditorias/validações feitas por agentes (subagentes ou sessões de
> auditoria) ao estado do projeto: **o que auditaram, em que versão, o feedback, e o plano de ação**
> para corrigir. Complementa o `log-alteracoes.md` (que regista *o que se fez*); este regista *o que se
> verificou e o que daí resultou*.
>
> **Regras:** append-only. Nunca editar/apagar entradas antigas; uma decisão que mude → nova entrada que
> supersede a anterior. Cada entrada identifica **a versão auditada** (commit + hash do ficheiro) para ser
> reproduzível. Datas absolutas.

---

## [AUD-001] Validação do onboarding (agente sem contexto)
- **Data:** 2026-06-08
- **Versão auditada:** branch `App-Generica`, commit `65e9797`, `MapLab.html` blob `ef14070`.
  (Nota: à data desta corrida o commit ainda não existia; o subagente leu o working tree equivalente.)
- **Tipo:** validação do processo de onboarding (`instrucao-agente-alteracoes.md` + `questionario-validacao.md` Secções 1–6).
- **Quem:** subagente "às cegas" (general-purpose), sem contexto prévio.
- **Veredicto:** ✅ **Onboarding suficiente.** O agente localizou ficheiro vivo, Versão Original, planos,
  log e questionário, e **verificou no código** (encontrou `workspace`, 883 ícones, título "MapLab",
  correu `JS OK`). Documentação/planos/log/código mutuamente consistentes.
- **Lacunas apontadas:**
  1. **Contradição `CLAUDE.md` ↔ processo novo** — o `CLAUDE.md` mandava "editar `lifemap_lab.html` / app v12".
  2. Comando de validação JS assume um único `<script>` simples (frágil).
  3. "Teste visual" sem receita concreta no repo; caminho do Chrome fixo.
  4. Ordem global com saltos (3→5) não explicados localmente.
  5. Grupos B/C "feitos" mas não commitados (só no working tree).
- **Plano de ação / resolução:**
  - [x] Lacuna 1 **RESOLVIDA** em #004 do `log-alteracoes.md` (CLAUDE.md atualizado: `main` v12 vs
    `App-Generica`/MapLab; aponta para `instrucao-agente-alteracoes.md`).
  - [x] Lacuna 5 **RESOLVIDA** — tudo commitado em `65e9797`.
  - [ ] Lacunas 2,3,4 — menores; registadas, a tratar quando se mexer nas respetivas zonas.

## [AUD-002] Validação de IMPLEMENTABILIDADE do roadmap (por alteração)
- **Data:** 2026-06-08
- **Versão auditada:** branch `App-Generica`, commit `65e9797`, `MapLab.html` blob `ef14070`;
  `questionario-validacao.md` com a **Secção 7** (perguntas 24–31) acrescentada.
- **Tipo:** validar se um agente novo consegue **IMPLEMENTAR** cada alteração do roadmap só com
  `roadmap.md` + `Planodeacao-*.md`, ou se a spec é insuficiente.
- **Quem:** subagente "às cegas" (general-purpose).
- **Veredicto por item:**
  | Item | Veredicto |
  |---|---|
  | D — Classes & Grupos | Implementável **com pressupostos** |
  | E — Atribuição em massa | Implementável **com pressupostos** |
  | F — Versões de classe | Implementável **com pressupostos** |
  | G — Side-by-side 2 modos | Implementável **com pressupostos** |
  | S1–S3 — Persistência base | Implementável **com pressupostos** (+ tensão de ordem) |
  | Reconciliação `.md`↔`.json` | Com pressupostos, **EXCETO colisão = insuficiente** |
  | S5 — Mapear Pasta | **Insuficiente** |
  | S6 — Criar pastas | **Insuficiente** |
- **Lacunas concretas apontadas (10):**
  1. **🔴 Tensão de ordem D ↔ Ordem 4** — o `.json` da persistência base precisa de campos de classe
     que só nascem no Grupo D (ordem 5), mas a ordem manda fazer 4 antes de 5.
  2. **🔴 Política de colisão na reconciliação** — dois irmãos homónimos colidem na chave `nome+nivel+pai`;
     comportamento indefinido.
  3. **🟡 E — primária vs secundária** no "Aplicar" não está especificado.
  4. **🟡 D — defaults e widget de cor** — default de `iconSource`, default do modo de cor, e não existe
     color-picker no código.
  5. **🟡 D — escopo das flags de visualização** (por árvore/projeto/global?) e se persistem.
  6. **F/S4 — esquema de nomes** das versões em ficheiros por confirmar.
  7. **S1 — contrato dos endpoints** (porta/host/erros/timeout) por especificar (apontar p/ `TableEditorApp/acc_server.py`).
  8. **S5/S6 — decisões em aberto** (ficheiros vs pastas, profundidade, ocultas; base path, colisões,
     sanitização, preview) tornam-nos não-implementáveis sem confirmar.
  9. Fragilidade do comando de validação JS (regex de `<script>`).
  10. Inconsistência cosmética log (#001-003 "pendente") vs planos ("aceite") — coerente com append-only.
- **Plano de ação / resolução:**
  - [ ] **RONDA DE PERGUNTAS AO UTILIZADOR** (aceite por ele) para fechar lacunas 1–8. Com as respostas,
        completar os `Planodeacao-*.md` e o `roadmap.md` (transformar os "a confirmar" em decisões).
  - [ ] Lacuna 1 (tensão de ordem) é a prioritária — decide se: (a) especificar o esquema `.json` completo
        antes de ambos, ou (b) dividir a Ordem 4 em "estrutura" + "extensão de classes (com D)".
  - [ ] Lacuna 9 — documentar a dependência do comando de validação (menor).
  - [ ] Lacuna 10 — garantir que `handoff.md` deixa claro que o estado vivo é o dos planos (A/B/C aceites). _(já reflectido)_

## [AUD-003] Validação da RETOMA DE SESSÃO ("inicia")
- **Data:** 2026-06-08
- **Versão auditada:** branch `App-Generica`, commit `65e9797`, `MapLab.html` blob `ef14070`.
- **Tipo:** testar se um agente novo, numa sessão nova, com só "inicia", retoma o trabalho sozinho.
- **Quem:** subagente "às cegas", seguindo a nova **§0bis (Retoma de sessão)** de `instrucao-agente-alteracoes.md`.
- **Veredicto:** ✅ **Retoma suficiente.** O agente leu na ordem certa (handoff → registo-auditoria →
  roadmap → planos → log → instrução), confirmou estado real (`git log -1`, `git status`, JS OK, blob
  `ef14070`), inferiu corretamente (branch, commit, A/B/C aceites, próximo = Ordem 4, lacunas pendentes),
  e escreveu o registo obrigatório em `agente-audit-iniciar.md`. Sem incoerências materiais.

## [RESOLUÇÃO] Ronda de perguntas — lacunas da AUD-002 fechadas
- **Data:** 2026-06-08
- **Contexto:** o utilizador aceitou a ronda e respondeu às lacunas 1-8 da AUD-002. Resultado refletido
  em `Planodeacao-app.md`, `Planodeacao-server.md` e `roadmap.md`.
- **Decisões:**
  1. **🔴 Tensão de ordem (D↔4) — RESOLVIDA:** esquema COMPLETO do `.json` por árvore **definido já agora**
     em `Planodeacao-server.md` → S3 (inclui campos de classe + `numeracao`). A persistência base grava o
     formato final; o Grupo D só o preenche. Sem retrabalho.
  2. **🔴 Colisão na reconciliação — ELIMINADA por design:** regra de integridade — **proibido** dois
     irmãos com o mesmo nome sob o mesmo pai/nível. + **NOVA FUNCIONALIDADE (Grupo H)**: toggle
     "ativar/desativar numeração" na vista; export `.md` com/sem numeração; `.json` grava sempre field
     `numeracao`. Identidade do nó fica inequívoca.
  3. **🟡 E — Aplicar:** toggle **primária/secundária** no painel de atribuição em massa.
  4. **🟡 D — cor:** cor por Grupo, por Classe e Custom; widget = paleta existente + `<input type=color>`.
     Defaults: origem do ícone "por Classe", vista "só primárias".
  5. **🟡 D — escopo da vista:** preferências de visualização **por árvore** (persistem no `.json`).
     No side-by-side, **toggle por vista/painel** (Grupo G).
  6. **F/S4 — nomes:** `Arvore X-vN.md/.json` + sub-versões de classe `Arvore X-vNa.json` (md partilhado). Confirmado.
  7. **S1 — endpoints:** espelhar `TableEditorApp/acc_server.py` (Python stdlib, porta fixa, REST simples).
  8. **S5/S6 — pastas:** base = `referencias/instrucoesMapa.md` (copiado para o repo). **Mapear INCLUI
     ficheiros** (prefixo `_`, agrupados por tipo, hidden primeiro, exclusões). **NOVO (Grupo I)**: toggle
     ficheiros + filtros (ext/nome/pasta) com 2 modos (expandir-o-necessário / esconder-irrelevantes) —
     **a debater em detalhe**. S6: preview+confirmação sempre, saltar existentes, sanitizar nomes.
- **Itens novos criados:** Grupo H (numeração) e Grupo I (filtros/ficheiros) em `Planodeacao-app.md`;
  esquema `.json` em S3; `referencias/instrucoesMapa.md`.
- **Pendente de debate (não bloqueante):** Grupo I (filtros/ficheiros na vista) — detalhe a fechar com o utilizador.

<!-- Próximas auditorias: append abaixo desta linha. -->
