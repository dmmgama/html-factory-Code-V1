---
created: 2026-06-09 06:22
chat: Roadmap governo minimo ate Agentic OS
summary: >
  Roadmap em camadas do pacote mínimo de governo (Classe III) até ao Agentic OS, passando por Mapa AI
  (banco de ensaio) e Life Management (prémio), com guardrails anti-tropismo e definições de DONE.
---

# ROADMAP — do pacote mínimo de governo ao Agentic OS

> Documento vivo, "correto na conceção, preenchido ao operar". Se cresce além do mínimo sem dor real a justificá-lo, **violou o seu próprio princípio** — relê a §G.
> Eixo-mestre herdado do AI Path: **três classes de conhecimento por consumidor + ritmo** (I durável/David/lento · II operacional/LLM/rápido · III governança/ambos/quase-nulo). Tudo aqui se classifica por aí.

---

## §A. Onde estás

```
[pacote mínimo] ──▶ Mapa AI ──▶ Life Management ──▶ 2nd brain ──▶ Agentic OS
   F0 (agora)       F1 ensaio      F2 prémio          F3 emerge     F4 destino
```

Tens dois sistemas sofisticados (AI Protocols, Cristalização) + preferências, em paralelo, cada um disciplinado por dentro mas **a proliferar**. O movimento certo não é construir mais — é **destilar o mínimo reutilizável** e aplicá-lo. F0 é isso.

**A regra que governa tudo abaixo:** cada peça vive num sítio só; o formato serve o dono da sua classe; a estrutura cresce por necessidade real, não por antecipação.

---

## §B. A pilha-alvo (o destino, para orientar — não para construir já)

| Camada | O quê | Ferramenta | Classe |
|---|---|---|---|
| Estratégia | deliberar, governar | Opus / Projects | — |
| Execução | operar com determinismo | Claude Code + git | — |
| Apresentação | ver o estado (humano) | Notion (hubs) | — |
| Trabalho/edição | MDs, research, regras | Obsidian (filesystem) | I, III |
| Conhecimento por-projeto | memória de trabalho do agente | wiki Classe II por projeto | II |
| Consolidação | promover nós duráveis cross-projeto | Cristalização (grafo) | I, III |
| **2nd brain (obj 1)** | conhecimento composto e recuperável | Obsidian + Cristalização + retrieval | — |
| **Agentic OS (obj 2)** | agentes que carregam contexto certo sozinhos, executam, e arquivam o novo | tudo acima, orquestrado | — |

**Fronteira de ouro (não-duplicação):** Notion *aponta* para Obsidian ou vice-versa, nunca duplica. Apresentação no Notion; trabalho no Obsidian; o mesmo conteúdo nunca nos dois.

---

## §C. F0 — Pacote mínimo de governo *(agora · time-box: 1–2 sessões · NÃO um projeto)*

O destilado reutilizável da AI Protocols + Cristalização, cortado ao osso. É Classe III: faz-se uma vez, serve todos os projetos. **Não é o sítio para resolver tudo o que auditámos — é o subconjunto que um projeto novo precisa para arrancar sem ser à balda.**

### DONE = esta checklist fechada (e nada mais até F1 operar)
1. **Uma fundação de front matter** (EN, da FUNDACAO) com os 3 campos-eixo: `class` (I/II/III), `recipient` (composto), `status`. Campos de ciclo de vida (`t_valid`, `supersedes`, `confidence`) **disponíveis, não obrigatórios**.
2. **Regra das 3 classes** (uma página): o que é cada uma, dono, ritmo, onde vive (I→Obsidian curado; II→wiki por projeto; III→este pacote).
3. **Fronteira Notion↔Obsidian** (a regra de ouro acima, meia página).
4. **Arranque + ficha mínimos:** ficha = arquivo humano (a tua, com `session_father` = proveniência); relógio único `S{n}`; **sem LOG-PROJECTO**; sem perguntar onde gravar (a regra diz). Aplica os fixes do audit que são baratos (dedup, renomear `context.md`/`CONTEXT.md`).
5. **Gatilho de cristalização (RC1)** + **membrana:** `context.md` (local, por sessão) → **nó** quando bate RC1 (custo alto + decidido + ≥2 usos) **e** é cross-projeto. Só isto da Cristalização entra no pacote agora.
6. **Tier 1/2** (carregar sempre vs. on-demand) — só para higiene de contexto, não como permissões.
7. **Ledger `Aprendizagem.md`** (append-only) — o pacote só cresce por entradas aqui.

### Explicitamente DIFERIDO (não entra em F0)
LIGACAO (dois braços) · ciclo de vida bitemporal a escala · hooks/infra Claude Code · "tiers como controlo de acesso" · event-sourcing · validador automático de front matter *(entra em F3, quando o volume o justificar)*.

> **Guardrail:** se sentires vontade de adicionar à checklist, **pára** — isso é o tropismo. Escreve na Aprendizagem e deixa o uso decidir.

---

## §D. F1 — Mapa AI *(banco de ensaio · greenfield · baixo risco)*

Constrói o **Mapa AI usando o pacote F0**. O Mapa AI **é a porta de entrada do 2nd brain** (índice humano de Classe I/III no Obsidian), não um projeto à parte.

- **Conceção (correta), conteúdo (incremental).** Cria a taxonomia/estrutura dos eixos do AI Path §4 (por classe · projeto · ferramenta · domínio · estado). Vazia. Preenche ao operar.
- **Primeiro nó a cristalizar:** a tese-arco do AI Path (o padrão de tropismo). Depois, as decisões da própria reconciliação AI Protocols↔Cristalização. Dogfood: o sistema prova-se em conteúdo real e de alto valor.
- **Objetivo duplo:** (a) ter o eagle-eye — saber onde está e onde pôr cada coisa; (b) **stress-testar o pacote F0** — cada fricção vai para a Aprendizagem.
- **DONE de F1:** Mapa navegável + os primeiros ~5–10 nós reais + a Aprendizagem com as primeiras lições do pacote. Não "Mapa completo" — isso nunca fecha.

---

## §E. F2 — Life Management *(o prémio · já corre · maior valor)*

Aplica o pacote **já provado** ao Life Management. É onde vive a Camada 0 (avó, filha, relações, saúde) — por isso só depois de F1 o pacote ter passado no ensaio.

- Retrofit, não reconstrução: o LM já funciona; o pacote dá-lhe a governança e a ligação ao Mapa AI.
- A inteligência do LM passa a saber gerir-te **também na frente AI** (o doc pede isto explicitamente) — porque o Mapa AI fica ligado ao hub do LM (§4.5), por ponteiro, não cópia.
- **DONE de F2:** LM a operar sob o pacote; Mapa AI referenciado no hub; segunda volta de lições na Aprendizagem.

---

## §F. F3 — Acumulação → o 2nd brain emerge *(puxado, não construído)*

Não se "constrói" o 2nd brain numa fase. Ele **emerge** à medida que mais projetos correm sob o pacote e a Cristalização acumula nós.

- **Retrieval por threshold (D1/§12 da Cristalização):** índice curado/routing aguenta ~centenas de páginas. Só se muda para híbrido BM25+vetorial quando exceder **ou** precision@k < ~0.8. Não antecipar.
- **Validador de front matter entra aqui** (remark-lint-frontmatter-schema + markdownlint) — quando o volume torna o drift manual real.
- **Substrato:** ponderar git e/ou Supabase quando o ciclo de vida bitemporal começar a doer em YAML à mão (não antes).
- **Métrica north-star:** instrumenta a **taxa de re-derivação** (↓ = memória funciona). É o sinal de que o 2nd brain está vivo, não o número de nós.

---

## §G. F4 — Agentic OS *(o destino · obj 2)*

Só faz sentido quando o 2nd brain tem conteúdo real e o retrieval funciona. O Agentic OS é a **camada de operação** por cima:

1. **Auto-contexto no arranque** — a sessão carrega o contexto certo sozinha (o teu S1 north-star). O pacote F0 (Tier + classes + ficha+proveniência) é o que torna isto possível: o agente sabe o que ler porque o sistema o diz, não porque tu o forneces.
2. **Execução** — Claude Code como braço operacional (LIGACAO entra aqui, *se* um projeto o exigir), git como substrato determinístico.
3. **Auto-arquivo** — conhecimento novo importante cristaliza-se e arquiva-se no sítio certo do Mapa, sem tu o arrumares à mão (o problema-raiz do AI Path).
4. **Loop de entropia** (Fowler harness engineering) — um agente periódico que repara drift: relê a Aprendizagem, regenera o protocolo operacional, apanha duplicações/staleness. **Sem isto, o 2nd brain à escala vira pântano.** É o que falta a tudo o que construíste até hoje.

> O Agentic OS não se ataca antes de F3. Atacá-lo agora é repetir o WikiBuilder. Está aqui para orientar, não para começar.

---

## §H. Guardrails anti-tropismo *(a parte que não podes saltar)*

O AI Path documenta o teu loop quatro vezes. Estas regras existem para o quebrar:

1. **Time-box e DONE fixo por fase.** Cada fase tem uma checklist fechada. "Completo" não é um estado de nenhum mapa — só de checklists.
2. **Pull, não push.** Governança nova só nasce de uma entrada na Aprendizagem (dor real), nunca de uma ideia elegante.
3. **Conceção correta, conteúdo incremental.** Constrói a estrutura certa vazia; preenche ao operar. (A tua própria regra do Mapa.)
4. **Um sítio só.** Mapa AI = porta do 2nd brain; vistas Cristalização = ramos; não três coisas.
5. **Banco de ensaio antes do prémio.** Testa em greenfield (Mapa AI); aplica no que importa (Life Management) depois.
6. **Pára-e-sinaliza:** se uma fase passa de 2–3 sessões sem fechar, é sinal de tropismo — não de complexidade. Fecha o mínimo, regista o resto na Aprendizagem, avança.

---

## §I. Próximo passo concreto

1. Fechar a **reconciliação da fundação** (qual schema ganha — EN da FUNDACAO + tipo-nó da Cristalização) — é o item 1 da checklist F0. Posso esboçar-to.
2. Cristalizar a **tese-arco do AI Path** como primeiro nó (e limpar a numeração de secções desse doc, que está baralhada).
3. Verificar as âncoras §11 da Cristalização (fecham o `(a confirmar)`).

Escolhe por onde — e qual destes faço já contigo.

---

> **Mantém-me vivo:** a cada fase fechada, atualiza o "Onde estás" (§A). Se este roadmap crescer, cresceu errado.
