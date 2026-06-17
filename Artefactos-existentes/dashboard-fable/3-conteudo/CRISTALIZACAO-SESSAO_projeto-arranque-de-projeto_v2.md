---
created: 2026-06-10 07:13 WEST (UTC+01:00)
chat: Cristalização de sessão — governo, starter kit e camada de ferramentas
recipient: Humans-Informative
type: session-consolidation
class: I
version: 2
supersedes: CRISTALIZACAO-SESSAO_projeto-arranque-de-projeto.md
session_father: "sessão governo AI (auditoria → starter kit), reconstituída de transcript 1.md + devolução Fork 2"
summary: >
  Consolidação v2 da sessão de governo AI: integra a devolução do Fork 2 (Protocolo Fork +
  Incorporação de Cowork) — que não altera o governo, mas adiciona uma camada de ferramentas
  e supersede a decisão de montagem (multibraço sempre). Inclui ledger de decisões, correções
  por aplicar, pendentes com gatilho e hipóteses descartadas.
---

# CRISTALIZAÇÃO DA SESSÃO — O projeto de arranque de projeto *(v2, com Fork & Cowork)*

> **O que isto é:** reconstituição do que a sessão analisou, casou e decidiu — e da estratégia que propôs: um **starter kit** que monta projetos novos coerentes com os protocolos do David corrigidos pela própria sessão. A v2 integra a **devolução do Fork 2** (`Forks_e_Cowork_com_Agentes_em_Protocolo-FINAL.md`, v2), que **não altera o governo** — reutiliza-o — mas introduz uma **camada de ferramentas** (Fork, Cowork, Code como superfícies) e **supersede uma decisão de montagem** (D2 → D19).
> **O que não é:** análise nova. Tudo aqui foi produzido na sessão ou no fork; este documento consolida e separa **decidido / aberto / descartado**.
> **Fontes:** `transcript 1.md` (autoridade até ao marcador Fork 2) + AUDITORIA + REVISAO + outputs do kit + Fork-Return v2 (autoridade sobre Fork/Cowork). Supersede a v1 deste documento.

---

## §0. BLUF

A sessão converteu o projeto **AI Protocols** de "projeto que corre" em **fábrica de projetos**: o seu output é um **starter kit transversal (Classe III)** — `INSTALACAO-PROJETO` + `TEMPLATE-SYSTEM-PROMPT` + `OPERAR-PROJETO` + os protocolos existentes com os fixes do audit. Montar um projeto passa a ser: *"Agente, usa o INSTALACAO-PROJETO e o starter kit."* O coração é o **contrato de coerência (CO1–CO8)**: invariantes que garantem que nenhum projeto arranca com os drifts auditados.

A devolução do Fork 2 acrescenta a **camada de ferramentas** por cima do mesmo governo:
1. **Protocolo Fork** — explorar tangentes dentro de uma sessão longa, com handshake exato, scratch hermético ("secção Fork X" na ficha) e retorno por edição de mensagem (apagar sem rasto / devolver como entrada de sessão). Resolve a lacuna que a Hipótese 1 expôs (o fork não tinha casa na ficha).
2. **Incorporação de Cowork** — o projeto passa a dispor de três superfícies (Projects, Cowork, Code). O braço estratégico vira **entidade única em duas plataformas** (Projects default + Cowork-estratégico para multiagente), com **SP-ficheiro + stubs**, **uma sessão por superfície** e estado partilhado. Braços operacionais (Cowork-op, Code) são projetos próprios ligados **só pelo Blackboard** — onde vive o `log-sessoes` (o relógio comum).
3. **Mudança de montagem (supersede D2):** monta-se **sempre multibraço de início** — Blackboard presente, braços operacionais **declarados mas desativados**, ativação on-demand. Custo quase nulo; mata o retrofit a meio do projeto.

**Atenção:** os 4 ficheiros do kit em disco estão desatualizados face a decisões posteriores da mesma sessão **e** face ao Fork-Return. Divergências concretas em **§5.2** — aplicar antes de usar o kit.

---

## §1. As análises que a sessão fez

### 1.1 Auditoria externa ao governo do AI Protocols *(doc: AUDITORIA-Governo-AIProtocols.md)*
Percurso de arranque observado sem executar + Tier 1 + registos reais (fichas S2/S3) + confronto com o estado da arte. Veredito: desenho acima da média e alinhado com SOTA 2025–2026; o fosso é entre o que o sistema **declara** e o que **força** (enforcement, substrato, espinha única). Achados que escalam:
- **ME-3** — duplicação do `PROTOCOLO-ficha-sessao` **já divergida** (as duas cópias prescrevem arranques diferentes).
- **C1** — deadlock no primeiro fecho: §8.5 escreve em `LOG-PROJECTO.md` que não existe; §5.5/§6 impedem criar/inferir.
- **G2** — colisão `context.md` ↔ `CONTEXT.md` em Windows/Drive (case-insensitive).
- **ME-1** — relógio de sessão tri-esquema (`S{n}` · `{set} - S{n} - {descritor}` · prática `SProt-N`).
- **C3** — incoerência documental do SESSOES (ver 1.2).
- **G1** — `context.md` cresce sem política de compactação. Mais: front matter sem validação na escrita; handoff atual é redireccionamento manual.

### 1.2 Revisão pós-clarificações *(doc: REVISAO-Auditoria-AIProtocols.md)*
As 4 clarificações do David recalibraram o audit:
- **Ficha = arquivo humano** (consumidor: David, fora de sessão). Concedido; retirada a proposta de a promover a fonte de verdade. Fica só o cross-check leve: o fecho autora ficha e handoff/context **na mesma passagem**.
- **Front matter = consumo humano diferido (Obsidian)**, não agente. Concedido; o reenquadramento **agrava** o caso do validador não-agente (lint determinístico).
- **Handoff-redirect = andaime de v0**, não defeito — com remoção a tornar-se critério de saída rastreado.
- **SESSOES = protocolo de instalação**, não ledger do projeto. Intenção aceite; mas o achado relocaliza-se: a intenção está **contradita por 3 documentos** (CATALOGO `ciclo: permanente`; corpo §1–§8 como ledger vivo; LIGACAO §1.5 como autoridade de relógio viva) contra 2 (arranques grill-me). Reconciliar a redação: **protocolo install-time ≠ artefacto runtime-permanente** que ele instala.
- **Consequência maior:** com ficha e front matter fora do balde "máquina", o registo múltiplo reduz-se a `handoff`+`context` — par são working/long-term. **Event-sourcing retirado** como recomendação principal; **LOG-PROJECTO não deve nascer** (git + context cobrem; resolve C1 de caminho).

### 1.3 Calibração 1–10 e pushback CTE
Perfil do David face ao tecto do possível: desenho 7–8 (arquitetura de conhecimento, memória, governança canónica, SOTA) vs. realizado 3–4 (execução, enforcement, shipping). O fosso **é o tropismo §7 quantificado**; valor maioritariamente potencial; convergência com SOTA ≠ novidade de campo; vantagem distintiva real = contexto pessoal + composição cross-projeto afinada ao perfil cognitivo. Pushback do David (CTE 500 páginas não tem turnkey) parcialmente concedido: o problema aplicado é genuinamente difícil e ele *shippa* na frente aplicada — o defeito é específico da camada meta que incha. Mantido: "era inevitável" é forte demais; o ponto de inflexão é **transformar a infraestrutura de um entregável em projeto autónomo aberto**. Régua: **medir pela coluna "realizado"**; o kit só não é WikiBuilder #3 se for time-boxed e **consumido** (Mapa AI) em 1–2 semanas.

### 1.4 Análises operacionais (economia de escrita, fuso, ficha S3, protocolo v2)
- **Economia de escrita da ficha:** o custo não é a call ao filesystem, é re-emitir/re-ler o documento todo. "Md no chat + gravar no fim" é igual ou pior e perde crash-safety. Solução: `edit_file` por **delta contra âncoras-sentinela** semeadas no template; nunca reescrita total, nunca re-leitura; context-editing da Anthropic auto-limpa tool-results antigos. Requer `edit_file` string-match.
- **Ficha S3:** bem-formada; o preenchimento incremental funcionou (ME-1/2/3 capturadas; entrada [PAUSA] com retoma). Defeitos menores: fuso contraditório, `status: decided` em pausa, `relacionados` vazio, `entry` errado, e a própria ficha planeava criar `CONTEXT.md` (G2 prestes a disparar).
- **Protocolo-ficha v2 (rascunho):** marcadores `-> VER` por resolver, FS0 agramatical, FS2 com formato morto, regra data/hora não encodada, versão não bumpada. Feedback dado a cada VER (D12–D14).

### 1.5 Fork 2 — a análise que produziu a camada de ferramentas *(doc: Forks_e_Cowork…FINAL.md, v2)*
Lacunas operacionais identificadas, **não resolúveis por governo**: (i) sessões estratégicas longas precisam de explorar hipóteses **com o contexto inteiro da sessão** — não delegável por handoff (perde nuance) nem continuável no fio (context rot); (ii) o braço estratégico atual (deliberação + filesystem) não tem **agentes especializados** nem **execução de grau industrial**. Resposta: duas adições de baixo impacto que **reutilizam** `log-sessoes`, Blackboard e LIGACAO sem os alterar. Argumento-chave: **fork ≠ subagente** — o subagente é delegação de contexto isolado; o fork é ramo que **herda o contexto inteiro**; complementam-se, não se substituem. Dentro do Fork 2 correu um sub-fork que produziu a versão final; a devolução foi classificada (pelo próprio protocolo em debate) como **Hipótese 2 / crítica**.

---

## §2. Como a sessão casou os elementos fornecidos

| Elemento dado pelo David | Como entrou no sistema |
|---|---|
| **Sistema Cristalização** (CANONICO + OPERACIONAL + ROADMAP) | Camada de conhecimento que faltava. Casamento bidirecional: a **FUNDACAO EN ganha a sintaxe**; a **Cristalização ganha o tipo** (nó cabeça+ponteiro, 3 eixos, ciclo de vida) como extensão de tipo. Entra no projeto mínimo via SP §9 (RC1 + hand-raise) e CO8. Métrica north-star: **taxa de re-derivação**. |
| **David - AI Path** | Dá a **tese-arco** (loop de tropismo, 4×) — primeiro nó a cristalizar — e o **eixo-mestre das 3 classes** (I durável/David · II operacional/LLM · III governança/ambos). Mapa AI = porta do 2nd brain. |
| **PROTOCOLO-SESSOES** | Corrige o audit: o `log-sessoes` é a espinha de **rastreabilidade** (event-sourcing) — capta o interleaving temporal de fios concorrentes. **4 eixos não-redundantes**: ORDEM (log-sessoes) / PORQUÊ (context) / ESTADO (handoff) / NARRATIVA (ficha); um eixo por artefacto, sem sangria. Entra no pacote mínimo **mesmo num braço**. |
| **Ficha S3 + template + protocolo v2** | Convergem num `PROTOCOLO-ficha-sessao` consolidado: template **incorporado**, âncoras-sentinela para escrita delta, fuso fixado, `session_status`. |
| **Clarificações (ficha/FM/handoff/SESSOES)** | Recalibraram o audit (§1.2); separação humano/máquina **sã e endossada**, stress-testada a pedido. |
| **Hub conceptual (links/proveniência)** | `session_father` em todos os docs + ficha = **aresta de proveniência** de um grafo de conhecimento. Mas: links Obsidian = navegação **humana**; retrieval **de agente** é o problema difícil — tratado por threshold na Cristalização. |
| **Fork-Return v2 (Fork & Cowork)** | **Camada de ferramentas sobre o governo existente, sem o alterar.** O Fork reutiliza ficha (secção Fork X) + `log-sessoes` (registo Hipótese 2) + cristalização (nós). O Cowork reutiliza LIGACAO + Blackboard + relógio único; o que muda é a montagem (multibraço sempre — D19) e a existência de superfícies dentro do braço estratégico. Detalhe em §3.7. |

---

## §3. A estratégia — o projeto de arranque de projeto

### 3.1 Tese
O projeto AI Protocols **não corre** — o seu output é um **starter kit** (Classe III) no repositório transversal que monta projetos novos. Montagem = entrevista curta + instalação dos protocolos certos + geração do SP a partir do template + criação da estrutura. Resultado: projeto que **arranca inteiro**, sem os drifts auditados, e já com a camada de ferramentas declarada.

### 3.2 O starter kit (peças e estado)

| Peça | Papel | Quando | Estado pós-sessão |
|---|---|---|---|
| `INSTALACAO-PROJETO.md` | orquestrador: entrevista → SESSOES → LIGACAO → gera SP → cria estrutura → read-after-write | install-time | **produzido** (v0.1; rever §5.2 — montagem multibraço) |
| `TEMPLATE-SYSTEM-PROMPT.md` | molde do canon (§1–§12) | gerado na montagem | **produzido** (v0.1; rever §5.2) |
| `OPERAR-PROJETO.md` | guia do operador: arrancar · cristalizar · hand-raise · fechar · manutenção | runtime, humano | **produzido** (acrescentar Fork à operação) |
| `TEMPLATE-ficha-ancorada.md` | ficha humana com âncoras p/ escrita delta | runtime | **produzido** (incorporar no protocolo-ficha; acrescentar secção Fork X) |
| **`PROTOCOLO-FORK`** | tangentes em sessão: handshake, scratch hermético, retorno, registo | runtime | **a criar** (especificação fechada no Fork-Return, Partes 1+3) |
| `PROTOCOLO-SESSOES` | relógio + log-sessoes (rastreabilidade) | install-time (artefacto fica) | existe; **corrigir redação install/runtime** |
| `PROTOCOLO-LIGACAO` | braços operacionais (Blackboard); gera SP operacional (§4.B) | install-time | existe; ok — ganha o Cowork-op como destinatário além do Code |
| `PROTOCOLO-ficha-sessao` | ficha humana + proveniência | runtime | **dedup + consolidar v2** (D10–D16) + secção Fork X (D20) |
| `PRODUCAO-DOCS` + `FUNDACAO` + templates | produção de docs + fundação única EN | runtime | existe; FUNDACAO recebe tipo-nó da Cristalização |
| Cristalização + **inbox transversal** | camada de conhecimento + captura | runtime | existe; inbox transversal **único** a criar |
| **Stubs de superfície** (Projects / Cowork) | apontam ambas as superfícies ao SP-ficheiro | install-time | **a criar** (2 linhas cada — D22) |

### 3.3 O projeto mínimo que a montagem cria *(atualizado pelo Fork-Return)*
```
<Projeto>/
├── SYSTEM-PROMPT.md       (gerado; sem front matter; lido por TODAS as superfícies)
├── INDEX.md               (Tier 2, navegação)
├── handoff.md             (estado vivo do braço estratégico, reescrito)
├── context.md             (raciocínio do braço estratégico, append)
├── 0.Registos/Sessions/   (fichas humanas, proveniência; cada ficha com secção Fork X)
├── Blackboard/            (SEMPRE presente — D19)
│   ├── log-sessoes        (relógio único; comum a todas as superfícies — D21)
│   └── worklog · hot · ops-snapshot · code   (canal estratégia↔operacional)
└── OP-Cowork/ · OP-Code/  (braços operacionais: SÓ quando ativados, on-demand;
                            cada um = projeto próprio com SP gerado pelo LIGACAO §4.B)
    (wiki Classe II nasce DEPOIS, quando o objetivo é conhecido)
```
**Ciclo de vida:** arranque (SP → ficha → handoff → context → relógio do `log-sessoes`) · runtime (PRODUCAO-DOCS + cristalização RC1 + hand-raise + Fork quando preciso) · fecho (handoff → context → ficha na mesma passagem → read-after-write, **sem LOG-PROJECTO**).

### 3.4 O contrato de coerência — cada invariante mata um drift
**CO1** um relógio (mata ME-1) · **CO2** uma fundação de front matter (mata fork EN/PT + campos não-declarados) · **CO3** uma continuidade, sem log de mutações (mata registo quádruplo + C1) · **CO4** um caminho canónico por ficheiro (mata ME-3) · **CO5** sem ficheiros-fantasma · **CO6** nomes sem colisão case-insensitive (mata G2) · **CO7** classe declarada · **CO8** captura não se perde (hand-raise → inbox). Regra-mãe: **uma matéria, um sítio**. *(O Fork-Return acrescenta dois invariantes de facto, a formalizar: **uma sessão por superfície** — D23 — e **decomposição Blackboard↔privado** — D21.)*

### 3.5 Ordem de produção definida pela sessão
1. **Fixes de coerência aos protocolos existentes** (§5.1) — senão os templates herdam os drifts.
2. **Propagar ao kit** as decisões pós-produção + Fork-Return (§5.2).
3. Consolidar o `PROTOCOLO-ficha-sessao` v2 (D10–D16 + secção Fork X).
4. Redigir o **PROTOCOLO-FORK** (espec. fechada — D20) e os **stubs de superfície** (D22).
5. **Teste real: montar o Mapa AI com o kit.** Cada fricção → `Aprendizagem.md`.

### 3.6 Enquadramento no roadmap (F0→F4)
F0 pacote mínimo (time-box 1–2 sessões, DONE fechado) → F1 Mapa AI (banco de ensaio; primeiro nó = tese-arco) → F2 Life Management (o prémio) → F3 2nd brain **emerge** (retrieval por threshold; validador + substrato quando doer) → F4 Agentic OS (auto-contexto S1 · execução · auto-arquivo · loop de entropia). Guardrails: time-box + DONE fixo · pull-não-push · conceção correta/conteúdo incremental · um sítio só · ensaio antes do prémio · pára-e-sinaliza às 2–3 sessões. *(A 1ª ativação real de um braço Cowork-estratégico — gatilho de T1/T2 — acontece naturalmente em F1/F2, não antes.)*

### 3.7 A camada de ferramentas *(do Fork-Return — não altera o governo, amplia a capacidade)*

#### A. Protocolo Fork — tangentes sem poluir o fio
- **Para quê:** explorar uma opção que **precisa do contexto inteiro** da sessão (não delegável a subagente) sem context rot nem poluição do fio principal.
- **Handshake exato:** David `Fork` → Agente `Fork Ativado — [data/hora, Europe/Lisbon]. Espero resultado.` → David `Ativo` → Agente `O que queres debater?` → debate. Os **dois anchors editáveis** (`Fork`, `Ativo`) são a mecânica: só as mensagens do David se editam.
- **Retorno:** *sem devolução* = edita `Fork` e escreve o que escreveria → rasto zero; *com devolução* = edita `Ativo` e cola a conclusão; *colapso* = devolve N mensagens antes (sub-debate + fork numa conclusão) — MD do substrato **obrigatório**.
- **Scratch hermético:** durante o fork, escrita persistente vai **só** para a secção **"Fork X"** da ficha — nunca para `log-sessoes`, cristalização ou outro ponto. Sem devolução → secção apaga-se (rasto zero hermético). Hipótese 2 → conteúdo **promove-se** a entradas reais (`log-sessoes` DECISÃO/observação, ficha, nó) e a secção limpa-se.
- **Registo:** Hipótese 1 (informativa) = usa-se no fio, sem rasto; Hipótese 2 (crítica) = **entrada da sessão**, não EXTERNA, **sem etiqueta "fork"**. O agente sugere a tier; o David decide.
- **Limitações assumidas:** o não-devolvido perde-se (daí o MD nos colapsos); disciplina do handshake é do David; o ganho é higiene de contexto, não raciocínio novo.

#### B. Incorporação de Cowork — três superfícies, um governo
- **Stack:** Projects (deliberação, default) · **Cowork** · Code. A escolha é pela natureza do trabalho.
- **Braço estratégico = entidade única em duas plataformas.** Projects + **Cowork-estratégico** (entra quando é útil delegar a **multiagentes especialistas** — a capacidade que o Projects não tem: subagentes custom, memória persistente, "Dreaming", modelo-por-tarefa). Mesma pasta, mesmo SP, mesmos logs, mesmo relógio; **mesmo `context`, mesma ficha, mesmo handoff**. A superfície distingue-se por **sufixo no ID** (ex.: `S-1-A` Projects / `S-1-B` Cowork — encaixe no esquema de ID por fechar, T3).
- **Enforcement do modo estratégico no Cowork:** Opus + extended thinking seletivo + instrução "debate, não executes" (contraria o viés de execução do harness); gatilho de escalada de volta ao Desktop quando derivar para debate profundo puro.
- **SP-ficheiro + stubs:** o SP é **um ficheiro** no folder, lido por ambas as superfícies; as "instruções de projeto" de cada superfície são *stubs* idênticos exceto uma linha (Cowork: "debate, não executes" primeiro). Não há SP configurado dentro de superfície — divergiria.
- **Uma sessão por superfície:** nunca a mesma sessão em simultâneo em duas superfícies — é o que impede escrita concorrente no `log-sessoes` (append-only resolve sequência, não concorrência).
- **Braços operacionais = projetos próprios** (pasta própria, SP próprio gerado pelo LIGACAO §4.B): **Cowork-op** (documentos, dashboards, artefactos, trabalho "live" — distinto do Code) e **Code** (código). Partilham com o estratégico **apenas o Blackboard** — a única membrana deliberação↔execução.
- **Decomposição Blackboard↔privado:** no Blackboard vive o `log-sessoes` (relógio comum — é por viver aqui que o governo é único) + o canal worklog/hot/ops-snapshot/code; privado de cada braço: SP, `context`, ficha, handoff. Relógio comum, deliberação local — senão os braços poluem-se.
- **Pré-condição (verificar uma vez):** Desktop, Cowork e Code alcançam *o mesmo* Blackboard.
- **Custos reais assumidos:** routing com footgun ("usar Opus" pode vazar para todos os subagentes); Fable 5 só para investigação pesada (caro, ~2× Opus; acesso por subscrição muda a 23 jun 2026).

---

## §4. Ledger — decisões consolidadas

*(D1–D18 da sessão principal; D19–D24 do Fork-Return. Supersessões marcadas.)*

- **D1.** AI Protocols = fábrica; output = starter kit no transversal; não se copia para dentro dos projetos.
- **D2.** ~~Dois braços = default-com-toggle (entrevista pergunta "um ou dois?")~~ — **SUPERSEDED por D19.**
- **D3.** Continuidade (handoff+context) = secção do TEMPLATE-SP, não protocolo standalone; extrai-se só com ≥2 projetos.
- **D4.** **LOG-PROJECTO não nasce.** Git + context + cristalização cobrem auditoria; resolve C1.
- **D5.** Contrato de coerência CO1–CO8 como invariantes de montagem.
- **D6.** Cristalização no projeto mínimo: SP §9 (RC1 + hand-raise), inbox transversal **único**, CO8.
- **D7.** Eixos de registo: **ORDEM** (log-sessoes) / **PORQUÊ** (context) / **ESTADO** (handoff) / **NARRATIVA** (ficha). Um eixo por artefacto, sem sangria.
- **D8.** **log-sessoes no pacote mínimo mesmo num braço**; relógio **lê-se do log-sessoes, não do context.md**. *(Localização fixada por D21: Blackboard.)*
- **D9.** SESSOES: **protocolo install-time / artefacto runtime-permanente** — distinção a encodar (fecha C3).
- **D10.** Fuso: **Europe/Lisbon, ISO 8601 com offset explícito**; convenção nas preferências, valor da tool de tempo; timestampar só eventos significativos. "GMT+0 (Lisboa)" morre.
- **D11.** `status` (doc) mantém-se + campo custom **`session_status`** (open/paused/closed) na ficha.
- **D12.** VER#1 → regra normativa com ID (alcance: front matter **e** cada entrada do Fio Condutor).
- **D13.** VER#2 → FS0 como cascata limpa **SP > ficha-de-projeto > perguntar**; ramo do meio dormente.
- **D14.** VER#3/#4 → **template incorporado no PROTOCOLO-ficha-sessao**; descritor sai do ID para o nome do ficheiro.
- **D15.** Escrita da ficha: **delta via `edit_file` string-match contra âncoras-sentinela**; proibido reescrever o todo ou re-ler.
- **D16.** Esquema de ID: principal `{F}-S{Label}-{n}`; branch `{id_pai}-{tipo}-{m}`; campo `session_id`; descritor no nome do ficheiro. *(4 confirmações pendentes — §6.1; tem de absorver o sufixo de superfície — T3.)*
- **D17.** Fundação reconciliada: **EN dá a sintaxe; Cristalização dá o tipo-nó** + eixos + ciclo de vida. Sede: grill-with-docs.
- **D18.** Sequência: pacote mínimo → Mapa AI (ensaio) → Life Management (prémio). Régua: coluna "realizado"; kit consumido em 1–2 semanas ou inflou.

*Do Fork-Return (decididas; Partes 1–2 fechadas, refinadas pela Parte 3):*

- **D19** *(supersede D2)*. **Montagem sempre multibraço de início:** Blackboard presente; braços operacionais **declarados mas desativados** no SP; ativação on-demand (cria-se `OP-Cowork`/`OP-Code` com SP gerado pelo LIGACAO, aponta-se ao Blackboard, protocolo de dois braços inalterado). Custo quase nulo; elimina retrofit.
- **D20.** **Protocolo Fork** adotado, com: handshake exato de 2 anchors editáveis; close-protocol (texto copiável + MD quando justificado); retorno sem-devolução/com-devolução/colapso (MD obrigatório no colapso); **secção "Fork X" na ficha como único local de escrita persistente do fork** (apagável → sem-rasto hermético; promovível → Hipótese 2); registo Hipótese 2 como **entrada de sessão, não EXTERNA, sem etiqueta** — fecha o crack taxonómico #1 da Hipótese 1.
- **D21.** **Decomposição Blackboard↔privado:** `log-sessoes` + canal operacional no Blackboard (comum); SP, context, ficha, handoff privados de cada braço. *(Fecha o pendente "onde vive o log-sessoes num braço": no Blackboard, que existe sempre por D19.)*
- **D22.** **SP-ficheiro + stubs de superfície:** um só SP no folder; stubs mínimos por superfície, idênticos exceto a linha "debate, não executes" do Cowork.
- **D23.** **Uma sessão por superfície** — nunca a mesma sessão em duas superfícies em simultâneo (integridade do relógio append-only).
- **D24.** **Entidade estratégica única:** Projects + Cowork-estratégico partilham governo e estado (context/ficha/handoff); distinção por sufixo de superfície no ID; enforcement do modo estratégico no Cowork (Opus + "debate, não executes" + gatilho de escalada).

---

## §5. Correções a aplicar (decididas; ainda não estão nos ficheiros)

### 5.1 Aos protocolos existentes *(pré-requisito dos templates)*
1. **Dedup `PROTOCOLO-ficha-sessao`** — eleger a cópia da raiz, apagar a de `1.Protocolos/ficha-sessao/`, alinhar INDEX + CATALOGO (ME-3). *(À data, as duas cópias ainda existem.)*
2. **Desreferenciar `LOG-PROJECTO`** do SP atual (§2.6, §8.5-5, §10) — não criar (C1, D4).
3. **Renomear a colisão** `context.md`/`CONTEXT.md` antes do inventário lá chegar (G2).
4. **Relógio único** — matar `{set} - S{n} - {descritor}` do FS2 (ME-1); formato final fecha com §6.1 + T3.
5. **SESSOES** — encodar install-time/runtime (D9): corpo §1–§8, CATALOGO `ciclo:` e LIGACAO §1.5 reconciliados.
6. **FUNDACAO** — declarar `project`; alinhar `functional`/`functional-vN`; receber o tipo-nó (D17).
7. **Consolidar o protocolo-ficha v2:** VER resolvidos (D12–D14), regra data/hora encodada (D10/D12), `session_status` (D11), FS8-delta (D15), template incorporado (D14), **secção "Fork X"** no esqueleto (D20), versão bumpada.
8. **LIGACAO** — admitir **Cowork-op** como braço operacional gerável pelo §4.B (além do Code).

### 5.2 Aos 4 ficheiros do kit produzidos *(divergências decisão-vs-ficheiro)*
1. **TEMPLATE-SP §7.2** lê o relógio do `context.md` — contradiz **D8** (log-sessoes, no Blackboard). Corrigir também §2 e §8.
2. **TEMPLATE-SP §12 condicional "dois braços"** — contradiz **D19**: o bloco deixa de ser condicional-na-geração e passa a **declarado-mas-desativado** em todo o SP gerado; idem o passo 1 e 5 do arranque (§7).
3. **INSTALACAO CO3** proíbe "log de sessões paralelo" — redigido antes de D8. Reescrever: o proibido é o **log de mutações**; o `log-sessoes` é o eixo ORDEM e **entra**, no Blackboard.
4. **INSTALACAO IN1.3** ("um braço ou dois?") e **IN4/IN6** (estrutura condicional) — contradizem **D19**: a entrevista pergunta que braços **ativar já** (nenhum/Cowork-op/Code/ambos); o Blackboard e a declaração-desativada criam-se **sempre**. Acrescentar a criação dos **stubs de superfície** (D22) à montagem.
5. **INSTALACAO CO1/IN1-2** fixam `<prefixo>-S{n}` — atualizar quando §6.1 + T3 fecharem (o esquema D16 + sufixo de superfície).
6. **TEMPLATE-ficha-ancorada** usa `GMT+0` no `session_open` — contradiz **D10** (ISO 8601 c/ offset). Acrescentar âncora **`<!-- /FORKX -->`** (secção Fork X, D20).
7. **ARQUITETURA §2** mostra log-sessoes só em `Coordenação/` (dois braços) e dois-braços-como-toggle — atualizar para D19/D21 (Blackboard sempre; `Coordenação/` renomeada/absorvida pelo Blackboard — confirmar nomenclatura, §6.4).
8. **OPERAR-PROJETO** — acrescentar a operação do Fork (§2.x: quando forkar, handshake, retorno) e a nota das superfícies (em que superfície estás, sufixo de ID).

---

## §6. Em aberto (pendentes — agora todos com dono ou gatilho)

1. **4 pontos do esquema de ID (D16):** (a) ordem do fio estável = primeira aparição? (b) gatilho de fio-novo por propor-confirma + lista controlada de labels? (c) branch com linhagem completa? (d) enum de tipos (`res/aud/ops/agt`)? — pendente de confirmação do David.
2. **Campo `Base:` na entrada DECISÃO do log-sessoes** (proveniência inputs→decisão) — pendente de sim/não.
3. **T3 — sufixo de superfície no ID** (`-A`/`-B`): tem de encaixar no esquema D16 **sem criar um quarto formato** (senão regressa o ME-1). **Gatilho: fecho do esquema de ID** (= resolver junto com §6.1).
4. **Nomenclatura Blackboard vs. `Coordenação/`** — o Fork-Return usa "Blackboard"; o kit usa `Coordenação/`. Um nome, um conceito — escolher e propagar (CO4/CO6 em espírito).
5. **T1 — fronteira do Cowork-estratégico:** "debate, não executes" vs. delegar subtarefas analíticas a consultores (research/crítica/análise alimentam deliberação; entregáveis operacionais não). Fronteira exata por cravar. **Gatilho: deep-search ao Cowork + 1ª ativação real de um braço Cowork-estratégico.**
6. **T2 — mecânica de duas superfícies numa sessão estratégica:** posse sequencial, ramo, ou handoff de superfície a meio — condiciona o registo no `log-sessoes`. **Gatilho: 1ª ativação real (mesmo momento de T1).**
7. **Inbox transversal único vs. por-projeto** — D6 tomada e exposta para correção; confirmar.
8. **Tiers: (a) economia de contexto vs. (b) permissão/segredo** — a sessão apostou em (a); confirmar.
9. **Audit formal `cannon-rules`** aos docs do kit (agora incluindo o futuro PROTOCOLO-FORK) — proposto, não corrido.
10. **Verificação das âncoras §11 da Cristalização** (`a confirmar` = vetor de memory-poisoning) — oferecido, não feito.
11. **Esboço da fundação EN unificada** para o grill-with-docs — oferecido, não feito.
12. **Critério de saída do handoff-redirect** (andaime de v0) — a rastrear no grill-with-docs.
13. **Pré-condição cross-superfície** — verificar uma vez que Desktop/Cowork/Code alcançam o mesmo Blackboard.

---

## §7. Hipóteses descartadas *(não ressuscitar sem novo argumento)*

1. **Event-sourcing como reorganização principal do registo** — sobre-engenharia dado o modelo humano/máquina; fica opção futura condicional.
2. **Criar o LOG-PROJECTO** — substituído por git + context (D4).
3. **M4 — instalar o SESSOES como espinha permanente** — substituído pela reconciliação documental (D9).
4. **Promover o Fio Condutor da ficha a fonte de verdade de máquina** — ficha é arquivo humano.
5. **Fundir handoff em context** — par working/long-term canónico.
6. **Ficha "em md no chat, gravar no fim"** — pior em tokens e perde crash-safety; substituída por delta/âncoras (D15).
7. **Fundir AI Protocols + Cristalização num mega-sistema** — só a fundação se reconcilia (D17); o resto fica modular.
8. **Continuidade como protocolo standalone já** — adiado por minimalismo (D3).
9. **Migrar de Projects para Cowork** — rejeitado: Cowork é debate-capaz mas execução-enviesado; deliberação ≠ execução; decisão = **dividir por fases**, não substituir. *(Corolário: o teste empírico do colapso num só ambiente foi dispensado — a hipótese que ele testava morreu; o Desktop, por não executar, é o ambiente-como-guarda da deliberação.)*
10. **Subagente como substituto do Fork** — mecanismos opostos (delegação de contexto isolado vs. ramo que herda o contexto inteiro); complementares.
11. **Toggle "um braço ou dois?" na montagem** (D2) — superseded por multibraço-sempre com ativação on-demand (D19).
12. *(Registado por referência:)* **Hipótese 1** — consolidar a sessão via ficha retroativa — testada e **falhada** (5 cracks; #1 taxonomia do fork e #5 multi-fio eram estruturais). O crack #1 fica **resolvido pela frente** por D20 (secção Fork X + registo como entrada de sessão); o método substituto para consolidação retroativa é este documento.

---

## §8. Próximo passo único

Aplicar §5.1 + §5.2 (fixes especificados e baratos), redigir o **PROTOCOLO-FORK** e os **stubs** (D20/D22), fechar §6.1–§6.4 (ID + sufixo + nomenclatura Blackboard — fecham juntos), e **montar o Mapa AI com o kit**. É o teste que decide se isto foi F0 — ou WikiBuilder #3.

---

*Fim — Cristalização da sessão v2 · transcript 1.md + AUDITORIA + REVISAO + outputs do kit + Fork-Return v2 · 2026-06-10 · supersede a v1*
