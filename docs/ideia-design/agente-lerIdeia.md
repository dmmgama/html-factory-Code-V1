---
_INSTRUCAO_AGENTE: "Este ficheiro é uma ordem de trabalho. Lê-o por completo e executa-o. Não o resumas. A tua tarefa é LER os documentos indicados, pela ordem dada, e produzir UM relatório. Não construis código, não aplicas patches, não corres o grill nesta passagem."
created: 2026-06-17 21:00
project: html-artifact-factory
chat: Leitura da pasta ideia-design antes do grill
session: SArq-3
status: instrucao
local: "C:\\Users\\JSJ\\David\\AI\\Projects\\html-factory-Code-V1\\docs\\ideia-design"
summary: >
  Ordem para o agente: antes do grill (M2), ler o material de arquitectura desta pasta
  pela ordem dada e devolver um relatório. Só leitura + relatório + recomendação sobre
  patches; não aplica nada nesta passagem.
---

# Instrução — lê a "ideia-design" antes do grill

## Situação (porque estás a ler isto)

Tu (agente do projecto html-factory) já fizeste o **Passo 0** (git) e o **Passo 1** (mapa
dos artefactos), e estás à porta do **Passo 2 (grill / M2)**. Entretanto, decorreu **em
paralelo** uma sessão de arquitectura (SArq-3) — um grill-me com o David, num agente
auditor — que **tu não viveste** e cujo resultado precisas de absorver **antes** de entrar
no grill. Todo esse material está nesta pasta (`docs/ideia-design`).

Esta passagem é de **leitura e relatório**, mais nada. **Não** construis código, **não**
aplicas patches, **não** corres o grill. O objectivo é garantir que percebes a fundo o que
a SArq-3 decidiu e o que deixou em aberto, e que me devolves um relatório que prove esse
entendimento e sinalize o que for importante.

## Onde tudo vive

- **Todo o material a ler vive nesta pasta:** `docs/ideia-design`.
- **A tua única escrita nesta passagem** é o relatório, que pões **na raiz desta mesma
  pasta**: `docs/ideia-design/RELATORIO-ideia-design.md`. (Esta instrução também aqui
  vive.) Não escrevas em mais lado nenhum nesta passagem.

## O que ler — e por que ordem (não saltes a ordem)

A ordem importa: cada documento assume o anterior. Lê assim:

1. **`GLOSSARIO-html-factory.md`** — PRIMEIRO, sempre. É o dono do vocabulário (peças,
   fluxos, ferramentas). Tudo o resto usa estes termos; sem ele, lês o resto com o
   significado errado.
2. **`fluxo-1-arquitetura.svg`** — o desenho de como as peças encaixam (Fundação → Planta →
   Construção). Ancora visualmente o glossário.
3. **`transicao-arquitetura-SArq2-para-SArq3.md`** — o que a SArq-2 tinha decidido e para o
   que a SArq-3 o transpôs, e porquê. Dá-te a linha de continuidade (nada foi anulado, foi
   completado).
4. **`arquitetura-html-factory-SArq-3.md`** — a cristalização: o estado-da-arte da
   arquitectura, com as decisões D1–D8 e as tensões T1–T4. É o documento central.
5. **`ADDON-SArq3-Claude-Design.md`** — o Claude Design como **candidato** a editor de
   planta (não decisão), e o conceito de Silhueta.
6. **`fluxo-D-proc.svg`** — o candidato **paralelo e autocontido**: chassis desenhado no
   Procreate, numerado → Claude Design traduz → Code injecta nos Slots.
7. **`fluxo-2-entrega-ao-agente.svg`** — como o material todo se te entrega (camada de
   leitura + camada de construção). Mostra-te onde esta passagem encaixa.
8. **Patches (lê, não apliques):** `PatchCDesign-context.md`, `PatchCDesign-roadmap.md`,
   `PatchCDesign-CLAUDE.md` — alterações propostas aos teus ficheiros de continuidade, para
   o candidato Claude Design entrar no grill. **`PatchGlossario-integracao.md`** — o patch
   que integra o vocabulário novo (Chassis, Slot, Silhueta) e estabelece o Glossário como
   dono do vocabulário; inclui a nota de proveniência das linhas do curador. **Nesta
   passagem só os avalias.**

> Os três ficheiros de bootstrap (A-MANUAL, B-BRIEFING, C-INSTRUCAO) já os conheces do
> arranque; relê o B-BRIEFING se precisares, mas o foco aqui é o material novo da SArq-3.

## O relatório que tens de devolver

Escreve `RELATORIO-ideia-design.md` na raiz de `docs/ideia-design`. Estrutura-o por estes
eixos (dentro de cada, diz o que achares relevante — tens liberdade):

1. **Entendimento.** Em linguagem tua, o que é a arquitectura fechada na SArq-3 (fluxo
   planta→Code, peças do glossário, o que mudou face à SArq-2). Prova que percebeste, não
   resumas por resumir.
2. **Ligação ao teu mapa (M1).** Como é que isto encaixa no que tu já mapeaste nos
   artefactos? Há blocos/peças que favorecem ou contrariam o que a SArq-3 assumiu? O curador
   continua a fazer sentido como piloto/mina?
3. **Tensões e riscos.** Das tensões em aberto (Alfândega genérica, Desacoplamento,
   Auxiliar/espelho, Editor), quais te preocupam mais e porquê. Onde vês risco de o factory
   "nascer torto". O elo frágil do Claude Design (import/export preservar Slots) — como o
   provarias.
4. **Candidatos a editor.** A tua leitura dos 4 (Claude Design+silhuetas, D-proc,
   manifesto-em-texto, Gridstack) — sem decidir (é do David, no grill), mas com a tua
   recomendação fundamentada para levar ao grill.
5. **Patches — recomendação.** Os 4 patches (3 PatchCDesign + PatchGlossario-integracao)
   reflectem bem o material? Aplicá-los-ias como estão, reescreverias algo, ou farias
   diferente? Em particular: confirma a nota de proveniência (as linhas do curador citadas
   na SArq-3 vêm de uma cópia web e podem divergir do ficheiro real — as do teu M1 mandam).
   **Recomenda; não apliques.**
6. **O que falta / perguntas.** O que ainda está ambíguo e devia ser fechado no grill, e
   quaisquer perguntas que tu próprio levantes.

Comunica no relatório em **Linguagem Ubíqua + tradução civil** (o David é arquitecto
não-programador). Denso mas legível; sem encher.

## Limites desta passagem

- Não construis código. Não corres o grill. Não aplicas patches. Não escreves fora de
  `docs/ideia-design`.
- Não decides as tensões — são do David, no grill.
- Se algo no material te parecer contradizer o teu mapa (M1) ou os invariantes, **assinala-o
  no relatório** em vez de o resolveres por iniciativa própria.
