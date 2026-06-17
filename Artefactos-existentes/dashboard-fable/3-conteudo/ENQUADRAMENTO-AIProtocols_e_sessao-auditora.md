---
created: 2026-06-10 07:24 WEST (UTC+01:00)
chat: Enquadramento AI Protocols vs sessão auditora
recipient: Humans-Informative
type: session-consolidation
class: I
session_father: "reconstituição: percurso do audit-prompt + registos SProt-2/SProt-3 + cristalização v2"
relacionados: [CRISTALIZACAO-SESSAO_projeto-arranque-de-projeto_v2.md]
summary: >
  Liga o projeto AI Protocols (o que é, o que planeou, onde parou) ao que a sessão
  auditora estabeleceu (starter kit, decisões, camada de ferramentas). Mostra que a
  sessão executou por outra via grande parte do roadmap do próprio projeto, o que
  isso supersede, o que se mantém, e a sequência de passos a seguir agora.
---

# ENQUADRAMENTO — O projeto AI Protocols e a sessão que começou por o auditar

> **Pergunta a que responde:** como se encaixa o projeto AI Protocols no que a sessão auditora estabeleceu — e que passos seguir agora.
> **Fontes:** percurso completo do audit-prompt (SP v0, Tier 1, SESSOES, INDEX, CATALOGOs, FUNDACAO) + registos `0.David-only` (FICHA-S2, FICHA-S3, LEIA-ME, arranques MONTAR-DIRETORIA e INVENTARIO) + a cristalização v2 da sessão auditora.
> **Companheiro de leitura:** `CRISTALIZACAO-SESSAO_projeto-arranque-de-projeto_v2.md` (o detalhe das decisões D1–D24 e correções). Este documento não as repete — enquadra-as.

---

## §0. BLUF

O projeto AI Protocols e a sessão auditora **não são duas coisas — são o mesmo projeto em dois momentos**. O AI Protocols nasceu (SProt-2) para construir um **repositório de protocolos de governança reutilizáveis** que, no fim, "sai do projeto para um repositório transversal" (INDEX §2) e culmina num **`Protocolos-Base-de-Projeto` — "a receita do projeto-template"** (INVENTARIO §5-bis.3). A sessão auditora, partindo de um mandato de auditoria, acabou por **executar exatamente esse destino por outra via**: o starter kit (INSTALACAO + TEMPLATE-SP + OPERAR + contrato de coerência) **é** o Protocolos-Base-de-Projeto que o roadmap do projeto previa para depois de mais duas sessões de processo. 

A ironia central: o SP v0 tem o §4 ("O que este projecto é") marcado **"A definir"** — e foi a sessão auditora que o definiu: *o AI Protocols é uma fábrica; o seu output é o starter kit* (D1). 

Consequência prática: o roadmap interno do projeto (SProt-3 MONTAR-DIRETORIA → grill-with-docs INVENTARIO → grill-mes isolados de afinação) fica **parcialmente executado, parcialmente superseded, e parcialmente re-scoped**. A §4 mapeia item a item; a §5 dá a sequência de passos.

---

## §1. O que é o projeto AI Protocols *(o que o percurso revelou)*

### 1.1 Génese — SProt-2, a sessão fundadora (2026-06-07→09)
Herdou um grill-me para templatizar o LIGACAO e cresceu até fundar o ecossistema inteiro:
- **Protocolos base (v1.1, tripla auditoria externa):** SESSOES (relógio `S{n}`, 4 logs, poda, ponteiro carimbado) e LIGACAO (dois braços via Blackboard; entrevista emite blocos SP + CLAUDE.md) + manuais.
- **Camada de metadados:** FUNDACAO-FRONTMATTER (keys/enums EN, prosa PT, `recipient` composto, frase-padrão `_INSTRUCAO_AGENTE`, o agente lê só `recipient`), 5 templates por tipo, CATALOGO-TEMPLATES (porteiro).
- **Normas de operação:** PROTOCOLO-PRODUCAO-DOCS, PROTOCOLO-ficha-sessao (pasta+ficha por sessão, preenchimento incremental, prosa auto-suficiente).
- **Governo do próprio projeto:** SP v0 (canon declarativo, Tier 1/2, restrições hard, princípios, continuidade handoff/context embutida §10 "a título provisório", tensão do registo quádruplo marcada §2.7), INDEX, CATALOGO-PROTOCOLOS, `handoff.md`/`context.md`.
- **Três arranques preparados:** MONTAR-DIRETORIA (estrutura), INVENTARIO (grill-with-docs), AUDITORIA-PROJETO (auditor de projetos vivos, in-construction).

### 1.2 O plano que o projeto tinha para si próprio
O `context.md`, o LEIA-ME e os dois arranques fixam a sequência: **(1)** SProt-3 monta a diretoria definitiva (fronteiras CONTEXT.md/INDEX/CATALOGO/SP §2, `docs/adr/`?, gaveta dos arranques, tensão 4(c) da localização do protocolo-ficha); **(2)** o grill-with-docs INVENTARIO classifica todos os artefactos em 4 eixos (camada/função/gaveta/estado epistémico), produz MAPA-ARTEFACTOS + glossário CONTEXT.md, **produz o protocolo de continuidade**, resolve-ou-preserva o registo quádruplo, define **obrigatórios vs opcionais** e começa o **Protocolos-Base-de-Projeto** + a **ficha de projeto**; **(3)** grill-mes isolados afinam protocolo a protocolo, fontes antes de consumidores.

### 1.3 Onde o projeto parou
SProt-3 arrancou (primeira sessão sob o SP v0 — validou o ciclo de arranque), reconciliou o §3 do arranque com o filesystem (ME-2), capturou ME-1 (relógio tri-esquema) e ME-3 (duplicação do protocolo-ficha, então "idêntica verbatim") — e **pausou em 2026-06-09 05:06 WEST no ponto Q2/§3.4(d)**: a localização canónica do protocolo-ficha + dedup, com opções A/B/C postas e nenhuma decidida. O projeto está, formalmente, **a meio da sua primeira sessão de estrutura**.

### 1.4 A natureza dupla (a chave do enquadramento)
O AI Protocols é simultaneamente: **(a)** um projeto que corre sob o seu SP v0 (com sessões SProt-N, fichas, continuidade) e **(b)** o **incubador de um repositório transversal** que o INDEX já declarava destinado a sair do projeto ("move para fora do projeto no fim"). O plano interno servia (a) como caminho para chegar a (b).

---

## §2. O que a sessão auditora estabeleceu *(síntese; detalhe na cristalização v2)*

Entrou como **auditor externo read-only** e saiu como **arquiteto do destino**: auditoria (ME-1/2/3, C1, C3, G1, G2 + confronto SOTA) → revisão pós-clarificações (ficha humana, front matter Obsidian, SESSOES install-time, LOG-PROJECTO não nasce) → casamento com a Cristalização e o AI Path (classes I/II/III, proveniência) → **o starter kit** (INSTALACAO-PROJETO, TEMPLATE-SYSTEM-PROMPT, OPERAR-PROJETO, ficha-ancorada, contrato CO1–CO8) → roadmap F0–F4 → decisões operacionais (fuso, `session_status`, escrita delta/âncoras, template incorporado, esquema de ID, log-sessoes como eixo ORDEM) → camada de ferramentas do Fork-Return (Protocolo Fork; Cowork; **montagem sempre multibraço** D19; Blackboard↔privado; uma sessão por superfície).

---

## §3. O enquadramento — a mesma seta, dois trajetos

A tese: **a sessão auditora não desviou o projeto — comprimiu-o.** O trajeto planeado era processual (montar casa → inventariar → afinar peça a peça → destilar a receita no fim). A sessão auditora foi direta ao destino (definir a receita + o contrato de coerência) e converteu o processo restante numa **lista finita de fixes**. O que era um roadmap de N sessões de grelha passou a: aplicar fixes especificados + fechar pendentes nomeados + testar no Mapa AI.

Três encaixes estruturais:

1. **O starter kit = o `Protocolos-Base-de-Projeto`.** O artefacto-fim que o INVENTARIO §5-bis.3 mandava "começar" foi entregue completo (com orquestrador, molde de SP e guia de operação — três peças que o plano original nem tinha nomeado).
2. **O repositório transversal = o "move para fora no fim".** A ARQUITETURA do kit (`_governo-transversal/`) materializa o destino que o INDEX §2 já declarava. **O "fim" chegou**: assim que os fixes estiverem aplicados, `1.Protocolos/` migra.
3. **A tensão 4(c) de SProt-3 dissolve-se por mudança de modelo.** SProt-3 pausou a escolher entre "raiz (onde o arranque lê)" e "`1.Protocolos/` (onde os protocolos vivem)". O modelo do kit responde: **nem um nem outro — o protocolo-ficha vive no transversal e o SP do projeto referencia-o** (IN7). A pergunta em que o projeto encalhou deixou de existir; sobra só o dedup mecânico.

### §4. Mapeamento item a item — o plano do projeto vs o que a sessão fez

| Item do plano interno (fonte) | Estado pós-sessão auditora |
|---|---|
| Definir "o que o projeto é" (SP §4 "a definir") | **EXECUTADO por outra via** — D1: fábrica/starter kit. Falta encodar no SP §4. |
| Protocolo de continuidade handoff/context (INVENTARIO §5-bis.1; SP §10 "provisório") | **EXECUTADO** — TEMPLATE-SP §8, secção fixa que herda `S{n}` (D3). Standalone só com ≥2 projetos. |
| Resolver/preservar registo quádruplo (SP §2.7; §5-bis.2) | **RESOLVIDO** — 4 eixos não-redundantes (D7) + LOG-PROJECTO não nasce (D4). A guarda "não apagar até resolver" cumpriu-se; a sede própria acabou por ser a própria sessão. |
| Obrigatórios vs opcionais + Protocolos-Base-de-Projeto (§5-bis.3) | **EXECUTADO** — o starter kit inteiro + a entrevista IN1 (que braços ativar) + diferidos explícitos do F0. |
| Ficha de projeto / "onde gravar" (§5-bis.4; FS0) | **DISSOLVIDO em parte** — o SP gerado fixa os caminhos (CO5; cascata FS0 com ramo do meio dormente, D13). Uma "ficha de projeto" como manifesto continua possível mas deixou de ser bloqueante. |
| SProt-3: estrutura definitiva da diretoria (MONTAR-DIRETORIA §3.4) | **SUPERSEDED em maioria** — a estrutura que importa passou a ser: `_governo-transversal/` (kit) + estrutura do projeto mínimo (cristalização v2 §3.3, com Blackboard sempre, D19/D21). Sobram da grelha original: dedup (mecânico) e a gaveta dos arranques (menor). |
| SProt-3: 4(c) localização do protocolo-ficha + dedup (Q2, ponto da pausa) | **RESPONDIDO** — vive no transversal, referenciado (IN7); dedup = eleger a cópia da raiz como base do consolidado v2 e apagar a outra (fix §5.1-1 da cristalização). |
| CONTEXT.md glossário (MONTAR-DIRETORIA §3.1) | **MANTÉM-SE, re-scoped** — continua tarefa do grill-with-docs, mas **renomeado** (G2: colide com `context.md` em Windows) e agora com a fundação reconciliada (D17) como input. |
| `docs/adr/` e fronteira context↔ADR (§3.2) | **MANTÉM-SE em aberto** — a hipótese de fronteira (context = cronológico; ADR = decisão atemporal) ficou enunciada no audit; decisão é do grill-with-docs. Nota: as entradas DECISÃO do log-sessoes (+ campo `Base:` se aprovado) cobrem parte do papel. |
| INVENTARIO: MAPA-ARTEFACTOS descritivo (4 eixos) | **PARCIALMENTE ABSORVIDO** — o audit mapeou e classificou o essencial (incl. estado epistémico); os eixos "camada/consumidor" foram superseded pelas classes I/II/III do AI Path. O que sobra do inventário funde-se no **Mapa AI (F1)** — não correr como sessão própria. |
| Grill-mes isolados de afinação por protocolo (INVENTARIO §6.2) | **SUBSTITUÍDOS** pela lista finita de fixes (§5.1/§5.2 da cristalização) + cannon-rules audit. Afinação aberta vira fix fechado. |
| PROTOCOLO-AUDITORIA-PROJETO (in-construction) | **MANTÉM-SE** — enriquecido pelo audit: modelar no padrão read-only + formato Sintoma→Fonte→Consequência→Remédio; o contrato CO1–CO8 é a régua natural. |
| SESSOES "permanente" vs "desaparece" (CATALOGO vs arranques) | **RECONCILIADO conceptualmente** (D9: protocolo install-time / artefacto runtime) — falta encodar nos docs (fix §5.1-5). |
| Regra "cada sessão pondera rever o governo no fim" (context.md PLANO-5) | **MANTÉM-SE** — e ganha mecanismo: o Ledger `Aprendizagem.md` + cadência de manutenção do OPERAR-PROJETO. |

**O que a sessão acrescentou que o plano não tinha:** a camada de conhecimento (Cristalização, hand-raise, inbox transversal — CO8), a camada de ferramentas (Fork; Cowork/superfícies; multibraço-sempre D19), o eixo-mestre das classes I/II/III, o roadmap F0–F4 com guardrails anti-tropismo, e a régua de calibração (medir pela coluna "realizado").

---

## §5. Passos a seguir agora *(sequência; cada passo desbloqueia o seguinte)*

1. **Fechar SProt-3 formalmente.** A sessão está pausada num ponto que já tem resposta. Retomar (ou fechar por decisão tua, registando): executar o **dedup** do protocolo-ficha (eleger raiz; apagar `1.Protocolos/ficha-sessao/`; alinhar INDEX+CATALOGO), registar que a grelha §3.4 restante foi superseded pelo modelo do kit, preencher `session_closed` e o handoff. Não deixar a primeira sessão sob o SP v0 em zombie — o próprio SESSOES (§3) o pune.
2. **Aplicar os fixes aos protocolos existentes** (cristalização v2 §5.1): desreferenciar LOG-PROJECTO do SP; renomear a colisão `CONTEXT.md`; relógio único; encodar install/runtime no SESSOES; FUNDACAO (`project`, enums, tipo-nó); consolidar o protocolo-ficha v2 (VERs, fuso, `session_status`, delta/âncoras, template incorporado, secção Fork X); LIGACAO admite Cowork-op.
3. **Propagar ao kit** as decisões pós-produção (cristalização v2 §5.2: relógio do log-sessoes; CO3 reescrito; multibraço-sempre na INSTALACAO e no TEMPLATE-SP; ISO 8601; nomenclatura). Encodar no SP do projeto o §4 com a definição D1.
4. **Fechar os pendentes que travam o formato** (cristalização v2 §6.1–§6.4): os 4 pontos do esquema de ID + sufixo de superfície (T3) + `Base:` + nome único Blackboard/Coordenação. Fecham juntos — são todos o mesmo eixo (identidade e morada do registo).
5. **Redigir as duas peças novas:** PROTOCOLO-FORK (espec. fechada no Fork-Return) e os stubs de superfície. Correr o **cannon-rules em modo audit** sobre o kit completo.
6. **Migrar `1.Protocolos/` + normas para `_governo-transversal/`.** É o "move para fora no fim" do INDEX — o fim é agora. O projeto AI Protocols fica como incubadora/registo histórico; o kit vive no transversal.
7. **grill-with-docs, re-scoped e mais curto.** Já não é o INVENTARIO inteiro: sobra a **fundação reconciliada** (D17), o **glossário** (renomeado), a **fronteira ADR↔context**, e o **critério de saída do handoff-redirect**. Uma sessão, não uma fase.
8. **Montar o Mapa AI com o kit (F1).** O teste real. O resto do inventário descritivo vive lá. Cada fricção → `Aprendizagem.md`.

> **Guardrail (o teu §H):** os passos 1–5 são uma a duas sessões de execução, não de desenho — está tudo especificado. Se algum passo começar a gerar desenho novo, é o tropismo: regista na Aprendizagem e segue. O ponto de não-retorno saudável é o passo 8 — o kit a ser **consumido**.

---

## §6. Tensões residuais (honestidade)

- **O projeto correu à frente do seu próprio governo.** A sessão auditora decidiu matéria estrutural fora do ciclo de mutação do SP (§8.4) — legítimo (era sessão externa, não o agente do projeto), mas as decisões só ficam canónicas quando os passos 2–3 as encodarem. Até lá, há **dois estados de verdade**: os ficheiros (velhos) e a cristalização (nova). Não operar o projeto nesse intervalo.
- **SProt-3 zombie.** Enquanto não fechar (passo 1), o log de sessões do projeto contradiz a prática — precisamente o drift declarado-vs-real que o audit apontou como o padrão do sistema.
- **O INVENTARIO não morreu — mudou de casa.** Reduzi-lo (passo 7) é decisão minha proposta com base no mapeamento §4; se preferes correr o grill-with-docs com o âmbito original completo, é defensável — custa mais uma a duas sessões e re-litiga pouco. A recomendação é o re-scope. [confiança: média-alta]

---

*Fim — Enquadramento AI Protocols ↔ sessão auditora · 2026-06-10 · ler com a cristalização v2*
