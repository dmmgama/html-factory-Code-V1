---
created: 2026-06-13
tipo: indice-pasta
summary: README do 60-DASHBOARD — a vista visual do governo.
---

# 60-DASHBOARD — a vista (DashboardGoverno)

## Para o David: o roadmap deste folder
O **DashboardGoverno** completo: os diagramas em HTML (`2-dashboard\`), o conteúdo que alimenta os diagramas (`3-conteudo\`), os manuais (de uso e para LLM, em `4-manual\`), e a orquestração (`Agent.md`). É a forma **visual** de ver o governo — uma vista, não a fonte.

## Para o LLM: regras de uso
- **Vive aqui:** Agent.md (orquestração Claude Code), 1-INSTRUCOES (spec), `2-dashboard\` (HTMLs + backup), `3-conteudo\` (cópias-input do dashboard), `4-manual\` (MANUAL-USO + MANUAL-LLM), `understand\` (knowledge-graph gerado).
- **NÃO vive aqui:** autoridade de conteúdo. O `3-conteudo\` são **cópias deliberadas** que o dashboard consome — **não são residência canónica** (o canónico vive em 20/30). Se a fonte mudar, re-copiar para cá (não editar aqui como se fosse original).
- **Vista ≠ armazém:** o dashboard é compilação — **nunca é autoridade**. Em conflito, vale a fonte (20/30).
- **Passo da ORDEM:** paralelo, não bloqueia. Refresh de diagramas é **em lote, pós-grill/fixes** (Sonnet/Haiku com o MANUAL-LLM) — nunca antes de as fontes estabilizarem.
- **Editável vs congelado:** os HTML/manuais editam-se quando se faz o refresh; `3-conteudo\` re-copia-se das fontes.
