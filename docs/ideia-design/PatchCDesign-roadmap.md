---
created: 2026-06-17 20:10
project: html-artifact-factory
chat: Claude Design como candidato a editor de planta
session: SArq-3
status: patch
summary: >
  Patch para roadmap.md: actualiza M2 (tensao Editor com 3 candidatos) e M9 (passo do
  editor depende do candidato escolhido). Nao fecha a decisao.
---

# PatchCDesign — roadmap.md

> Dois pontos a actualizar em `roadmap.md`. A decisao do editor continua para o grill (M2).

## A) Em M2 — Grill: na lista das 4 tensoes, SUBSTITUIR "Editor" por:
```
Editor (3 candidatos a avaliar: (a) Claude Design + silhuetas — ver ADDON-SArq3-Claude-Design.md;
(b) manifesto-em-texto; (c) Gridstack/próprio). Recomendar com trade-offs; decisão do David.
```

## B) Em M9 — SUBSTITUIR a linha do marco por:
```
### M9 — Editor de planta ⬜ (conforme decidido no grill)
- Implementar o candidato escolhido em M2.
- Se for **Claude Design**: PRIMEIRO teste de import/export (layout trivial → exportar →
  confirmar que o output é legível/parseável para mapear silhuetas→blocos); só depois o
  fluxo de silhuetas (gerar silhuetas por bloco, fidelidade recomendada conforme o bloco,
  David monta layout, agente substitui pelos blocos reais). → provar → commit.
- Se for **manifesto-em-texto** ou **Gridstack**: conforme trade-offs fechados no grill.
```
