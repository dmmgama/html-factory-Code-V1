# roadmap.md — html-factory

> Rumo e marcos. Deriva do `C-INSTRUCAO-arranque-AGENTE.md` (não inventado). No arranque, o
> agente confere se `handoff.md`/`context.md` estão alinhados com isto.

## Estado do gatilho inicial
Arranque do projeto. Governança instalada (S1). **Próximo marco: Passo 1 (mapeamento).**
Os invariantes (briefing §3) e o critério-mãe (simplicidade > completude > elegância) são
guarda-corpos de todos os marcos.

## Marcos

### M0 — Rede de segurança (git) ✅ CONCLUÍDO
- `git init`, `.gitignore`, commit `pre-grill`, branch `grill1`. Backups absorvidos.

### M0.5 — Governança / continuidade ✅ CONCLUÍDO (S1)
- Camada Claude Code instalada (CLAUDE.md + continuidade + permissões).

### M1 — Mapa dos artefactos ⬜ PRÓXIMO
- Mapear CADA artefacto de `Artefactos-existentes/` em 3 camadas (Dados/Motor/Viewer).
- Síntese transversal: que dados/blocos **reaparecem** (o padrão comum); de onde começar o piloto.
- **Entregável (commit):** `docs/mapa-artefactos.md`.
- Gate: decidir sozinho vs. subagentes de verificação (recomendado) e justificar.

### M2 — Grill (decisões fechadas) ⬜
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
