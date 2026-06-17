# roadmap.md — html-factory

> Rumo e marcos. Deriva do `C-INSTRUCAO-arranque-AGENTE.md` (não inventado). No arranque, o
> agente confere se `handoff.md`/`context.md` estão alinhados com isto.

## Estado do gatilho inicial
Arranque do projeto. Governança instalada + **mapa dos artefactos feito (M1)** (S1). **Próximo
marco: Passo 2 — grill (M2).** Os invariantes (briefing §3) e o critério-mãe (simplicidade >
completude > elegância) são guarda-corpos de todos os marcos.

## Marcos

### M0 — Rede de segurança (git) ✅ CONCLUÍDO
- `git init`, `.gitignore`, commit `pre-grill`, branch `grill1`. Backups absorvidos.

### M0.5 — Governança / continuidade ✅ CONCLUÍDO (S1)
- Camada Claude Code instalada (CLAUDE.md + continuidade + permissões).

### M1 — Mapa dos artefactos ✅ CONCLUÍDO (S1)
- Mapeados ~18 famílias em 3 camadas (Dados/Motor/Viewer) → [`docs/mapa-artefactos.md`](docs/mapa-artefactos.md).
- Feito com 5 subagentes `Explore` (read-only) + verificação (`code-reviewer` + leitura direta).
- Achados: 3 modos (grafo/árvore/tabela); 4 peças já existem dispersas; **piloto = grafo**; app de
  referência = **curador v3**. Commits `5eb221a` + `8642f63`.

### M2 — Grill (decisões fechadas) ⬜ PRÓXIMO
- Correr `grill-with-docs` alimentado pelo mapa. Fechar as 4 tensões:
  T2 Alfândega genérica (primeiro) · T1 Desacoplamento · Auxiliar/espelho · Editor.
- **Entregável (commit):** `docs/decisoes-grill.md`. Não construir antes disto.

### M3 — Piloto: Caixa + Alfândega + 1 bloco ⬜
- Caixa (Dados/Config/Motor/Viewer) + Alfândega + **um** bloco (recomendado: grafo) a renderizar
  **dados reais**. Provar ponta-a-ponta → commit.

### M4 — Generalizar a Alfândega ⬜
- A partir do caso real (não em abstrato) → commit.

### M5 — Segundo bloco no mesmo contrato ⬜ → provar → commit.
### M6 — Restantes blocos ⬜ (um a um).
### M7 — Manifesto `workspace.json` ⬜ (comanda que blocos aparecem) → provar → commit.
### M8 — Folha de binding ⬜ → provar → commit.
### M9 — Editor ⬜ (se decidido no grill) → provar → commit.

## Regra transversal (incremento vertical funcional)
Cada marco entrega algo a **funcionar ponta-a-ponta**, provado, e só depois se passa ao
seguinte. Cada incremento = um commit em `grill1`. Reporta ao David em Linguagem Ubíqua +
tradução civil, uma ideia por vez, com gate de confirmação.
