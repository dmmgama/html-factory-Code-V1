# handoff.md — estado imediato

> Telegráfico, denso, sem narrativa. Reescrito a cada fecho. Próxima sessão lê isto primeiro.

> [!IMPORTANTE] ARRANQUE PÓS-COMPACT (lê isto antes de tudo)
> 1. **A verdade está nos ficheiros, não no transcript.** Lê por ordem: este `handoff.md` →
>    `context.md` → `roadmap.md`. Depois `CLAUDE.md` para o protocolo de trabalho.
> 2. **Onde estamos:** Passo 0 (git) ✅ e governança ✅ feitos. **Próximo = Passo 1 (mapear
>    `Artefactos-existentes/` → `docs/mapa-artefactos.md`).** NÃO há código do factory ainda.
> 3. **Branch `grill1`** (trabalho); `master`=`pre-grill` (retorno limpo).
> 4. **O QUE construir** manda nos 3 docs: `A-MANUAL…`, `B-BRIEFING…`, `C-INSTRUCAO…`.
> 5. **Regras que se esquecem:** não construir antes do Passo 2 (grill) fechar; não decidir
>    sozinho as 4 tensões (são do David); `Artefactos-existentes/` é referência read-only;
>    PT-PT + Linguagem Ubíqua c/ tradução civil, uma ideia por vez com gate; proibido ler
>    `SessionTranscripts/` sem ordem.
> 6. **Decisão aberta no Passo 1:** se uso subagentes (`html-expert`/`code-reviewer`) p/ o mapa.
> 7. **NÃO arrancar o Passo 1 sem o David mandar.** Confirma primeiro.

**Sessão atual:** S1 — Setup Claude Code (governança). Anterior: nenhuma (arranque do projeto).
**Branch:** `grill1`. **Retorno limpo:** `master` (`pre-grill`, `f50ecef`).

## Feito
- Passo 0 (C-INSTRUCAO): `git init`, `.gitignore`, commit `pre-grill`, branch `grill1`.
- Backups em `Artefactos-existentes/` absorvidos: removidos os `.git` de FichaProjetosJSJ,
  LifeMap, TableEditor, projeto-ssot (eram repos próprios → ficavam só ponteiros). Conteúdo
  agora versionado (~1032 ficheiros). `.gitignore` internos mantidos.
- Camada de governança instalada (commit `Setup-ClaudeCode`): CLAUDE.md, context.md, handoff.md,
  memory.md, roadmap.md, bugs.md, additions.md, CHANGELOG.md, docs/MANUAL.md, .claude/settings.json,
  .gitignore atualizado.

## Decisões desta sessão
- Permissões: git read-only + `node -e` (validar JS single-file).
- Âmbito governança: conjunto completo LifeMap (inclui bugs.md/additions.md).
- Track de sessões único `S#` (abandonado `SG#`).
- Backups: absorver conteúdo (limpar `.git` internos) — são cópias, "o que interessa é o sumo".

## Próximos passos (por ordem)
1. **Passo 1 — Mapear `Artefactos-existentes/`** → `docs/mapa-artefactos.md`. Cada artefacto em
   3 camadas (Dados/Motor/Viewer) + síntese do **padrão comum** + recomendação de piloto.
   Decidir se lanço subagentes de verificação (recomendado: `html-expert`, `code-reviewer`).
2. **Passo 2 — `grill-with-docs`** alimentado pelo mapa → fechar 4 tensões → `docs/decisoes-grill.md`.
3. **Passo 3+ — incrementos** (piloto: grafo).

## Tensões em aberto
T2 Alfândega genérica · T1 Desacoplamento · Auxiliar/espelho · Editor (Gridstack vs texto) ·
Imutabilidade verificada. **Não resolver sozinho — são do grill/David.**

## Notas
- Não construir código do factory antes do Passo 2 fechar.
- `ClaudeCodeSetup.md` (protocolo do David) mostra `SG#` desatualizado; track real é `S#`.
