---
created: 2026-06-17 20:10
project: html-artifact-factory
chat: Claude Design como candidato a editor de planta
session: SArq-3
status: patch
summary: >
  Patch para context.md: actualiza a tensao "Editor" (sec. 6) para incluir o Claude
  Design como candidato a estudar no grill. Nao fecha a decisao.
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
- **Editor:** tensão em aberto, agora com 3 candidatos a avaliar no grill (recomendar com
  trade-offs; decisão do David, desempate pelo critério-mãe):
  (a) **Claude Design + silhuetas** — montar o layout base no Claude Design (produto
      Anthropic, research preview) com *silhuetas* dos blocos (os blocos reais NUNCA entram
      lá — ele regenera e corrompe-os); no fim o agente substitui silhuetas por blocos
      reais. Encaixa no Caminho 1. RISCOS a validar antes de adoptar: preview/bugs, custo
      Opus, e sobretudo o import/export por provar (testar layout trivial primeiro). Ver
      `ADDON-SArq3-Claude-Design.md`.
  (b) **Manifesto-em-texto** editável à mão (barato, sempre disponível).
  (c) **Gridstack / editor próprio** (provavelmente o mais caro).
```
