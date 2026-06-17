---
_INSTRUCAO_AGENTE: "Este front matter é metadados de registo (ignora). Salta para o corpo e executa-o por ordem. Não o resumas ao David — age."
created: 2026-06-10 17:45
chat: Dashboard governo colapsável — orquestração Claude Code
summary: >
  Instrução de orquestração para Claude Code (Sonnet 4.6, automode): montar a estrutura,
  avaliar understand/ como referência, refactorizar o dashboard para hierarquia colapsável
  com toggle técnico/não-técnico e tour, e produzir os manuais.
---

# Agent.md — Dashboard do Governo AI (versão colapsável)

## §0. Contexto e missão (lê isto primeiro)

**O que existe.** Um dashboard HTML single-file (`2-dashboard/DIAGRAMAS-governo-dashboard.html`) com 4 "folhas" (grafos SVG de dependências) sobre o sistema de governo de projetos AI do David: (1) a cadeia lógica de uma sessão de trabalho, (2) o roadmap de fecho, (3) o pacote de instalação em execução, (4) um projeto montado em operação. Nós clicáveis com inspector lateral, pan/zoom, estética blueprint com cartela técnica.

**A missão.** Evoluir esse ficheiro para um dashboard **hierárquico colapsável** com explicações em dois registos (técnico / não-técnico), tour de vista geral, e dados separados do shell — e produzir dois manuais. A especificação completa, com critérios de aceitação, está em `1-INSTRUCOES-adaptacao.md`. **Lê-a integralmente antes de tocar em código.**

**Modo de trabalho.** Automode autorizado. Podes fazer perguntas de clarificação ao David, mas só as bloqueantes — para tudo o resto, avança com pressupostos numerados (P1, P2…) declarados no relatório final. Não cries repositório git nem instales dependências sem perguntar (o objetivo é manter o output single-file, sem build).

**Regras invioláveis:**
- R1. Nunca alterar ficheiros fora desta pasta (`DashboardGoverno/`). Os originais em `docsTranscript/` e no projeto AI Protocols são **read-only**: copiam-se, não se editam.
- R2. Em conflito entre o que está hard-coded no HTML e o que dizem os documentos de `3-conteudo/`, **prevalece o conteúdo** (a `CRISTALIZACAO-..._v2.md` é a autoridade máxima; a v1 está superseded — ignora-a).
- R3. Não inventar conteúdo: cada descrição de nó deriva dos documentos de `3-conteudo/`. Se não houver fonte, escreve `(a confirmar)` e lista no relatório final.
- R4. O entregável principal mantém-se **um único ficheiro HTML** que abre por duplo-clique, sem servidor nem build. Dependência externa permitida: só as Google Fonts já usadas (com fallback).
- R5. Preserva a estética existente (blueprint, cartela, paleta, fontes) — evolui, não redesenha.

## §1. FASE 0 — Avaliar `understand/` (referência, não base)

A pasta `understand/` contém o output do analisador do plugin Understand-Anything sobre **outro projeto** (o CTE): `knowledge-graph.json`, `fingerprints.json`, `meta.json`. **Não contém o viewer** — não é uma base alternativa; é uma **referência de schema e de padrões**.

1. Lê o `knowledge-graph.json` (estrutura: `project` + `nodes[]` com `id/type/name/filePath/summary/tags/complexity` + edges/domains/flows mais abaixo — explora).
2. Extrai e adota o que servir, no mínimo:
   - **Separação dados↔shell:** os dados do dashboard passam a viver num bloco JS único e claramente delimitado (`/* ===DATA-START=== */ … /* ===DATA-END=== */`) dentro do HTML — é esse bloco que o manual ensinará outros LLMs a editar.
   - **Campos por nó** inspirados no schema dele (ver spec §3 das INSTRUCOES).
   - **Conceito de tour/vista guiada** (o U-A tem "guided tours" e "domain view"): informa o requisito da vista geral.
3. Se concluíres que algo do U-A justifica **mudar a abordagem** para além disto, formula UMA pergunta ao David com a proposta e o trade-off. Caso contrário, regista as adoções no relatório e segue.

## §2. FASE 1 — Montar e verificar a estrutura

Cria (se não existir) e verifica:

```
DashboardGoverno/
├── Agent.md                        (este ficheiro)
├── 1-INSTRUCOES-adaptacao.md       (a spec — já existe)
├── understand/                     (referência — read-only)
├── 2-dashboard/
│   └── DIAGRAMAS-governo-dashboard.html
├── 3-conteudo/                     (copiar de fontes — read-only depois de copiado)
└── 4-manual/                       (output dos manuais)
```

1. **`2-dashboard/`** — verifica que `DIAGRAMAS-governo-dashboard.html` lá está (o David coloca-o; foi-lhe entregue por download). Se faltar: **pára e pede ao David** o ficheiro. Não o reconstruas de memória.
2. **`3-conteudo/`** — copia (cópia, nunca mover) destas fontes:
   - `ROOT\30-KIT-GOVERNO\CRISTALIZACAO-SESSAO_projeto-arranque-de-projeto_v2.md`
   - `ROOT\30-KIT-GOVERNO\ENQUADRAMENTO-AIProtocols_e_sessao-auditora.md`
   - `ROOT\30-KIT-GOVERNO\ROADMAP-governo-minimo-ate-AgenticOS.md`
   - `ROOT\30-KIT-GOVERNO\ARQUITETURA-projeto-minimo-starterkit.md`
   - `ROOT\30-KIT-GOVERNO\OPERAR-PROJETO.md`
   - `ROOT\30-KIT-GOVERNO\Forks_e_Cowork_com_Agentes_em_Protocolo-FINAL.md`
3. Cria `4-manual/` vazia.

## §3. FASE 2 — Refactor do dashboard (o trabalho principal)

Implementa a spec da `1-INSTRUCOES-adaptacao.md` §1–§5. Sugestão de decomposição em **subagentes** (usa a tua Task tool; cada subagente recebe só o contexto de que precisa):

- **Subagente A — "redator-conteudo":** lê `3-conteudo/` + o bloco de dados atual do HTML e produz o novo bloco DATA completo (hierarquia pai→filhos, `desc_tec` + `desc_simples` por nó, `file` onde aplicável, vistas gerais por folha, passos da tour). Output: um ficheiro `_data-draft.json` na raiz para revisão. **Não escreve as duas descrições à pressa: a não-técnica é para um leitor inteligente que não vive nisto — sem jargão, com analogias quando ajudarem.**
- **Subagente B — "refactor-frontend":** implementa no HTML o motor: colapso/expansão com re-ligação de setas ao pai, botões ±, estado inicial colapsado, toggle técnico/não-técnico, painel de vista geral por defeito, tour passo-a-passo, regras do inspector (processo vs ficheiro, mostrar `file`). Consome o `_data-draft.json` e embebe-o no bloco DATA.
- **Subagente C — "qa":** corre os critérios de aceitação da spec (§6 das INSTRUCOES), um a um, abrindo o ficheiro no browser se tiveres como; reporta falhas ao orquestrador até tudo passar.

Itera B↔C até os critérios passarem. Apaga `_data-draft.json` no fim (os dados vivem no HTML).

## §4. FASE 3 — Manuais (em `4-manual/`)

1. **`MANUAL-LLM-dashboard.md`** — para um LLM (e legível pelo David): o que o dashboard é; o schema do bloco DATA campo a campo; o procedimento de update (onde editar, o que nunca tocar, como adicionar nó/grupo/folha, como manter as duas descrições em sincronia); validação pós-edição (checklist); e a regra de proveniência — updates derivam de `3-conteudo/` atualizado, nunca de memória.
2. **`MANUAL-USO-dashboard.md`** — para o David: como abrir, navegar (folhas, colapso, ±, toggle, tour, inspector, pan/zoom, atalhos), o que cada cor/forma significa, e como pedir um update a um LLM barato (apontar para o MANUAL-LLM + o doc de conteúdo novo).

Ambos com o front matter padrão do David no topo (`created`, `chat`, `summary`).

## §5. FASE 4 — Fecho

1. QA final completo (critérios §6 da spec) + abrir o dashboard e percorrer a tour de cada folha.
2. Relatório final ao David, telegráfico: o que foi feito, pressupostos tomados (P1…), `(a confirmar)` pendentes, adoções da Fase 0, e o caminho do ficheiro final.
3. **Não** apagues a versão original do HTML: antes do refactor, copia-a para `2-dashboard/DIAGRAMAS-governo-dashboard_v1-backup.html`.

— Fim do Agent.md —
