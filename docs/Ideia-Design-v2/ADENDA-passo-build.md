---
created: 2026-06-17 22:40
project: html-artifact-factory
chat: Passo de build em falta nos fluxos e roadmap
session: SArq-3
status: correcao
summary: >
  Adenda: o passo de COMPILACAO/BUILD (modulos -> HTML single-file) nao aparece como caixa
  nos fluxos nem como marco explicito no roadmap, apesar de ser exigido pela Imutabilidade.
  Risco de cair no esquecimento. Acrescentar.
---

# Adenda — o passo de build está em falta

> Apontado pelo fork. Para o grill e para o roadmap. Não fecha decisão; sinaliza uma omissão.

## O problema

A **Imutabilidade** (invariante) só é válida se existir SEMPRE um **passo de compilação**:
o HTML compilado é descartável; o capital vive nos módulos. Mas esse passo:

- **não aparece como caixa** em nenhum fluxo (`fluxo-1-arquitetura.svg` salta directamente de
  "Manifesto" para "HTML single-file");
- **não é marco explícito** no roadmap (está implícito em M3+, mas sem caixa própria).

É o elemento que mais risco corre de cair no esquecimento — e sem ele a Imutabilidade é só
uma intenção.

## O que acrescentar

1. **Nos fluxos:** entre "Code injecta os Blocos" e "HTML single-file", uma caixa
   **`build/assemble`** (junta Manifesto + Blocos + dados + Config → `dist/workspace.html`).
2. **No roadmap:** tornar o passo de build um item verificável dentro dos marcos (não um
   pressuposto). Candidato: um sub-passo em M3 (o piloto já exige build para provar
   ponta-a-ponta) e formalização em M7 (manifesto a comandar o build).
3. **Tensão ligada (já registada):** Imutabilidade *verificada* (build stamp / hash das
   fontes) — decide-se quando o build existir.

## Para o grill

Confirmar que o build é peça de primeira classe (caixa no fluxo + verificável no roadmap),
não pressuposto. Ligar à decisão da Imutabilidade verificada.
