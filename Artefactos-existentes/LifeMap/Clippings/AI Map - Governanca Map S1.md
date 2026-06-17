---
title: "AI Map - Governanca Map S1"
source: "https://claude.ai/chat/6479f336-64e0-4da7-979f-180d7b8933db"
author:
published:
created: 2026-06-14
description: "Claude conversation with 5 messages"
tags:
  - "clippings"
---
**You**

pergunta: quero fazer um repositorio para guardar docs de governanca. como fazias uma hierarquia de pastas em 3 niveis no maximo, idealmente MECE? da nomes

---

**Claude**

Arranque (1ª mensagem do chat):

**0\. Web ou Desktop?** — necessário para aceder à wiki (handoff, context, fundamento, decisions, index/log). Steps 1-3 já satisfeitos (SYSTEM-PROMPT, ROADMAP, TASK-TYPES estão no contexto); 4-9 dependem desta resposta.

**Scope guard.** A pergunta não cai limpa em Tarefa A/B/C (fase em foco = fecho do wiki-ai-evolution). "Repositório para guardar docs de governança" lê-se como uma de três coisas, e a estrutura correcta depende de qual:

- **(a) Destino da Tarefa A** — o `CWPP-CANDIDATES.md` entregue ao projecto **cwpp-implementation**. Se for isto, é o repo do projecto *downstream*, não deste. Estrutura orientada a ciclo de promoção (candidatas → gate G-016 → canonizadas).
- **(b) Projecto novo** de consolidação de governança transversal (separado deste e do skill). Estrutura orientada a corpus + protocolo-mãe (CWPP) + ledgers por projecto.
- **(c) Parte do fecho deste projecto** (Tarefa C). Improvável — falas em *criar* repositório, não arquivar.

Preciso de saber qual antes de dar nomes de pastas: um repo de candidatos CWPP, um repo de protocolo-mãe consolidado, e um arquivo de fecho têm hierarquias MECE diferentes (eixo de partição distinto — por *estado de promoção* vs. por *projecto-origem* vs. por *tipo de artefacto*).

Confirma **Web/Desktop** + **(a)/(b)/(c)**. Com isso leio o estado relevante e devolvo 2-3 hierarquias candidatas com o trade-off de cada eixo de partição — não uma só.

---

**You**

desktop. o o scope nao cai em nenhuma das opcoes. nao é nenhum dipo de particao que fizeste. é para um repo em que guardo informacao geral que vou coletando de projetos como este. e preciso de taxonomia e hierarquia para saber onde guardo ficheiros md para cristalizar informacao sobre cada aspeto de governanca. pergunto neste projeto pq foi onde isso foi mais visto.

---

**Claude**

Desktop confirmado. **Fora de scope deste projecto** — não toco em Tarefa A/B/C nem nos ficheiros do wiki-ai-evolution. Trato isto como design standalone, informado pela governança que aqui se acumulou. Não corro o resto do arranque (irrelevante para a pergunta).

---

**BLUF:** a escolha real não são os nomes — é o **eixo de partição** de nível 1. MECE vive ou morre aí. Dou-te dois eixos viáveis + o que parece óbvio mas quebra MECE.

### Candidato 1 — eixo ASPECTO/FUNÇÃO (o que a governança regula)

```
governanca/
├── decisao/
│   ├── registo/          # formato D-NNN, write-ahead, decision records
│   ├── mutacao/          # como o canon muda, revisão explícita
│   └── vocabulario/      # fixação de vocabulário, zero-expansão
├── regras/
│   ├── ledger/           # G-NNN, classificação, estados provisional/active
│   ├── invariantes/      # fundamento, pilares imutáveis
│   └── jurisdicao/       # fronteiras de scope, o-que-vive-onde, tiers
├── estado/
│   ├── handoff/          # handoff/context, continuidade inter-sessão (Reter)
│   ├── arranque/         # boot protocols
│   └── fecho/            # close protocols, critérios de fecho literais
├── verificacao/
│   ├── auditoria/        # protocolos de audit, lint
│   ├── gate/             # gate Lakatosiano, critérios de promoção
│   └── content-aware/    # verificação por turno, anti verification-theater
└── falhas/
    ├── tensoes/          # casos T-NN
    └── anti-padroes/     # scope drift, premature conclusion, verification-theater
```

Pergunta de sorting: *"que aspecto de governança é que isto regula?"* — a mais instintiva.  
**Costura única:** "critérios de fecho literais" cabe em `estado/fecho` **e** `verificacao/auditoria`. Resolve com casa primária + cross-link no front-matter (`related:`). É a única ambiguidade material.

### Candidato 3 — eixo CAMADA DE ABSTRAÇÃO (que tipo de coisa é)

```
governanca/
├── principios/    # verdades durável, agnósticas (write-ahead, dualidade de clientes, Reter=3ª função)
├── protocolos/    # protocolos nomeados: CWPP, boot, close, mutação
├── mecanismos/    # instrumentos: ledger G-NNN, handoff, gate, verificação content-aware
└── casos/         # incidentes: T-NN, lições, post-mortems
```

Pergunta de sorting: *"isto é uma verdade, um protocolo, uma ferramenta, ou um caso?"*  
Tipos disjuntos → **MECE quase perfeito, costura ≈ zero**. Margem fuzzy só em `mecanismo vs protocolo`. Escala melhor: poucos baldes de topo, absorve N projectos sem inchar.

### O trap — eixo CICLO DE VIDA

`setup / operacao / preservacao / fecho / meta`. Intuitivo, mas **quebra MECE**: verificação recorre em operação *e* fecho → duplicas ou arbitras. Não uses como nível 1.

### Recomendação

| Se… | Usa |
| --- | --- |
| Sortes por *"o que isto regula"* e o repo fica governança-de-projectos-AI | **Cand. 1** — mapeia ao teu "cada aspeto", sorting instintivo, custo = 1 costura |
| Esperas largura/longevidade e queres mínima manutenção de fronteiras | **Cand. 3** — 1 juízo por ficheiro, mas costura ≈ zero |

Inclino-me para **Cand. 1** pela tua formulação ("cada *aspeto* "), com a costura `fecho↔auditoria` resolvida por convenção fixa logo no README (decisão antes de aplicação — D-016).

Queres que gere o scaffold? Como é Desktop, posso dar-te prompt para agente IDE com script de criação de pastas + `README.md` de raiz com a regra de sorting e o front-matter-padrão. Confirma o candidato e crio.

---

**Claude**

AI Map