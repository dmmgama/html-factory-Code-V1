---
_INSTRUCAO_AGENTE: "Esta é a tua ordem de trabalho, agente Code. Lê-a por completo e executa-a pela ordem dada: lê tu mesmo a ideia-design-v2 (NÃO delegues a subagente), dá o veredicto sobre as correcções, e — se estiver pronto — produz o handoff-grill. NÃO mexas em nenhum outro ficheiro de sistema. Não a resumas."
created: 2026-06-17 23:10
project: html-artifact-factory
chat: Leitura da ideia-design-v2 e producao do handoff-grill
session: SArq-3
status: instrucao
summary: >
  Ordem à sessão Code: ler a ideia-design-v2 (sem delegar), confirmar que as correcções
  desfazem as preocupações do relatório anterior, dar veredicto, e se pronto produzir o
  handoff-grill (com relatório curto). Não toca em mais nenhum ficheiro de sistema.
---

# Instrução — lê a ideia-design-v2 e, se pronta, produz o handoff-grill

## Situação

Tu já produziste um **relatório** sobre a `ideia-design` (v1), onde levantaste preocupações
(furo dos patches, linhas do curador erradas / bloco-fantasma, 3-vs-4 candidatos a editor,
passo de build em falta, fonte única do vocabulário). Em resposta, foi criada
**`docs/ideia-design-v2/`** — versão corrigida e ampliada. As duas pastas coexistem **de
propósito**: precisas de **comparar** para confirmar se as tuas preocupações foram desfeitas.

Esta passagem é de **leitura + veredicto + (se pronta) handoff**. Não constróis código, não
aplicas patches, **não mexes em nenhum ficheiro de sistema** além de produzir os ficheiros de
handoff indicados no fim.

## Regra de método (importante)

**Lê tu mesmo a v2. NÃO delegues a subagente.** O objectivo é avaliar se as correcções batem
certo — e isso exige que sejas TU a ler, não um resumo de segunda mão. (O custo de contexto
não é problema.)

## Passo 1 — Lê a `ideia-design-v2` (ordem)

1. `GLOSSARIO-html-factory.md` — dono do vocabulário (peças, fluxos, ferramentas).
2. `arquitetura-html-factory-SArq-3.md` — a cristalização (D1–D8, T1–T4).
3. `transicao-arquitetura-SArq2-para-SArq3.md` — o que mudou face à SArq-2.
4. `ADDON-SArq3-Claude-Design.md` — Claude Design como candidato; conceito de Silhueta.
5. `fluxo-1-arquitetura.svg`, `fluxo-2-entrega-ao-agente.svg`, `fluxo-D-proc.svg` — os fluxos.
6. `maquina-html-factory.html` — o mapa interactivo.
7. **Correcções (o que responde às tuas preocupações):**
   - `CORRECAO-blocos-curador.md` — linhas da SArq-3 erradas (cópia web); mind-map = modo do
     grafo, não bloco; tabela de linhas reais.
   - `ADENDA-passo-build.md` — o passo de build como peça de primeira classe.
8. **Patches:** `PatchCDesign-context/-roadmap/-CLAUDE` (já a 4 candidatos) e
   `PatchGlossario-integracao` (Chassis/Slot/Silhueta + Glossário como dono; CLAUDE.md aponta,
   não absorve).

## Passo 2 — Veredicto (confirma que as correcções batem certo)

Para CADA preocupação do teu relatório, diz: **resolvida / parcial / por resolver**, com uma
linha de prova (onde na v2 está resolvida):
- Furo dos patches → existe `PatchGlossario-integracao`? CLAUDE.md aponta, não absorve?
- Linhas do curador / bloco-fantasma → existe `CORRECAO-blocos-curador`? Mind-map tratado como
  modo? **A tabela de linhas REAIS já está colada, ou ainda é stub à espera dos teus números?**
- 3-vs-4 candidatos → os PatchCDesign contam **4** (com D-proc), coerentes com os SVGs?
- Passo de build → existe `ADENDA-passo-build`? Build vira peça de primeira classe?
- Fonte única do vocabulário → Glossário é o dono e o CLAUDE.md aponta?

**Conclui:** a v2 está **PRONTA** para avançar para o handoff-grill, ou **NÃO PRONTA** (e o
que falta exactamente). Se não pronta, PARA e reporta ao David — não produzas o handoff.

## Passo 3 — Se PRONTA, produz o handoff-grill

(Segue o que está em `agente-prepara-handoff-grill.md`, Fase 2 — produz aqui o resultado dela.)

Escreve **apenas estes ficheiros** (nada mais de sistema):
- O **handoff** para a sessão grill (em `handoff.md` e/ou bloco colável), com:
  - **Identidade:** sessão Claude Desktop+Filesystem, EXTERNA, não-empreiteiro, só conduz o
    grill.
  - **Regras:** pode ler tudo e debater; escreve só os 2 entregáveis; NÃO toca em canon,
    continuidade, código ou git; NÃO aplica patches (só recomenda).
  - **2 entregáveis do grill:** `decisoes-grill.md` (David audita) + `grill-para-code-A.md`
    (para ti validares coerência e comandares a aplicação).
  - **Tensões a fechar:** T2 Alfândega (contrato único OU um por modo — pergunta-mãe), T1
    Desacoplamento, Auxiliar/espelho, Editor (4 candidatos + teste-gate), reconciliações
    (modos vs. vistas; mind-map = modo; linhas reais do curador; build como peça de primeira
    classe; Glossário dono).
  - **Comunicação:** Linguagem Ubíqua + tradução civil; uma ideia por vez, gate.
- Um **relatório curto** que acompanha o handoff (o veredicto do Passo 2 + a tua recomendação
  para o grill). Curto e factual.

## Limites (não ultrapasses)

- Lê tu mesmo (sem subagente). Veredicto honesto.
- NÃO mexas em nenhum ficheiro de sistema além do handoff + relatório curto.
- Não apliques patches. Não corras o grill. Não construas código.
- Se a v2 não estiver pronta, PARA no veredicto e reporta — não produzas o handoff.
