---
created: 2026-06-17 20:10
project: html-artifact-factory
chat: Claude Design como candidato a editor de planta
session: SArq-3
status: patch
summary: >
  Patch para context.md: actualiza a tensao "Editor" (sec. 6) para 4 candidatos a avaliar
  no grill (manifesto-texto, Claude Design+silhuetas, D-proc, Gridstack). Nao fecha a decisao.
---

# PatchCDesign — context.md

> Aplicar em `context.md`, seccao "6. Tensoes em aberto". SUBSTITUIR a linha do **Editor**
> pelo texto abaixo. Nao mexe em mais nada. A tensao continua ABERTA.

## Localizar (texto actual)
```
- **Editor:** Gridstack (arrastar) vs. manifesto-em-texto. Recomendar com trade-offs; decisão do David.
```

## Substituir por
```
- **Editor:** tensão em aberto, agora com 4 candidatos a avaliar no grill (recomendar com
  trade-offs; decisão do David, desempate pelo critério-mãe):
  (a) **Manifesto-em-texto** editável à mão (barato, sempre disponível; prova o pipeline
      sem risco novo — recomendado como arranque).
  (b) **Claude Design + silhuetas (D-sil)** — montar o layout base no Claude Design (produto
      Anthropic, research preview) com *silhuetas* dos blocos (os blocos reais NUNCA entram
      lá — ele regenera e corrompe-os); no fim o agente substitui silhuetas por blocos
      reais. Encaixa no Caminho 1. RISCOS a validar: preview/bugs, custo Opus, e sobretudo
      o import/export por provar (testar layout trivial primeiro). Ver
      `ADDON-SArq3-Claude-Design.md`.
  (c) **D-proc (Procreate)** — desenhar o Chassis numerado no Procreate → Claude Design
      traduz desenho→HTML + PNGs → Code injecta nos Slots. Material paralelo e autocontido.
      Mais sedutor mas com mais pontos de falha. Ver `fluxo-D-proc.svg`.
  (d) **Gridstack / editor próprio** (provavelmente o mais caro; pode emergir por acumulação).
```
