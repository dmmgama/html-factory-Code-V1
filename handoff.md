# handoff.md — estado imediato

> Telegráfico, denso, sem narrativa. Reescrito a cada fecho. Próxima sessão lê isto primeiro.

> [!IMPORTANTE] ARRANQUE (lê isto antes de tudo)
> 1. **A verdade está nos ficheiros, não no transcript.** Lê por ordem: este `handoff.md` →
>    `context.md` → `roadmap.md` → [`docs/mapa-artefactos.md`](docs/mapa-artefactos.md). Depois
>    `CLAUDE.md` para o protocolo de trabalho.
> 2. **Onde estamos:** Passo 0 (git) ✅, governança ✅, **Passo 1 / M1 (mapa dos artefactos) ✅**.
>    **Próximo = Passo 2 / M2 (grill)** para fechar as 4 tensões → `docs/decisoes-grill.md`.
>    **NÃO há código do factory ainda** (correto — não se constrói antes do grill fechar).
> 3. **Branch `grill1`** (trabalho); `master`=`pre-grill` (retorno limpo).
> 4. **O QUE construir** manda nos 3 docs: `A-MANUAL…`, `B-BRIEFING…`, `C-INSTRUCAO…`.
> 5. **Regras que se esquecem:** não construir antes do Passo 2 fechar; **não decidir sozinho as 4
>    tensões (são do David)**; `Artefactos-existentes/` é referência read-only; PT-PT + Linguagem
>    Ubíqua c/ tradução civil, uma ideia por vez com gate; proibido ler `SessionTranscripts/` sem ordem.
> 6. **NÃO arrancar o Passo 2 sem o David mandar.** Confirma primeiro.

**Sessão atual:** S1 — Setup + Mapa (M1). Anterior: nenhuma (arranque do projeto).
**Branch:** `grill1`. **Retorno limpo:** `master` (`pre-grill`, `f50ecef`).

## Feito
- **Passo 0:** `git init`, `.gitignore`, commit `pre-grill`, branch `grill1`. Backups absorvidos
  (4 `.git` internos removidos de FichaProjetosJSJ/LifeMap/TableEditor/projeto-ssot).
- **Governança (M0.5):** CLAUDE.md + continuidade + `.claude/settings.json` (commit `Setup-ClaudeCode`).
- **Passo 1 / M1 (mapa):** [`docs/mapa-artefactos.md`](docs/mapa-artefactos.md) — ~18 famílias em 3
  camadas (Dados/Motor/Viewer). Feito com 5 subagentes `Explore` (read-only) + verificação
  (`code-reviewer` + leitura direta de `sec7-viewer.js`/`V0.json`). Commits `5eb221a` + `8642f63`.

## Achados do mapa (resumo — detalhe no doc)
- **3 modos:** quase tudo cai em **grafo / árvore / tabela** (os 3 modos do Motor).
- **4 peças já existem, dispersas:** contrato de dados → **TableEditor** (envelope Frictionless);
  viewer cego → **`FloorViewer`** (projeto-ssot); ciclo reativo → **curador-v3** (`commit()=save()+renderAll()`);
  formato de grafo → **`knowledge-graph.json`**. A fábrica é juntá-las num sítio só.
- **Piloto = grafo** (confirmado). Contrato pronto a copiar: `nodes[]`/`edges[]`.
- **App de referência principal: curador v3** (não v4 — D9). É a mais complexa; melhor contrato
  (projeto/link 11 tipos/domínio) e melhor ciclo reativo, mas viewer acoplado (cor hardcoded).
- **3 violações de "estética fora dos dados":** dossier (`color` no dado), governance-explorer
  (`cor`), MAPA-EXPLORADOR (`ORIG`/`move`). A Alfândega tem de proibir isto.

## Decisões desta sessão (ver memory.md)
- D8 — mapa com subagentes Explore read-only; síntese fica comigo (alimenta T2).
- D9 — curador **v3** é a app de referência (v4 = experimento).
- D10 — registo: domínio = 3 modos; 4 peças dispersas.

## Próximos passos (por ordem)
1. **Passo 2 / M2 — `grill-with-docs`** alimentado pelo mapa → fechar as 4 tensões (T2 Alfândega
   primeiro) → `docs/decisoes-grill.md`. **Decisões do David — não resolver sozinho.**
2. **Passo 3 / M3 — piloto grafo:** Caixa (Dados/Config/Motor/Viewer) + Alfândega v0 + bloco grafo
   a render dados reais (`knowledge-graph.json` ou links do curador). Ponta-a-ponta → commit.

## Tensões em aberto (para o grill — Passo 2)
T2 Alfândega genérica (um contrato vs. um por modo — peça-mãe, primeiro) · T1 Desacoplamento
(parte-se o STATE global; moldes: curador-v3 + `FloorViewer.loadData`) · Auxiliar/espelho
(precedente: "canais à la carte" do TableEditor) · Editor (Gridstack vs texto; já há os dois mundos) ·
Imutabilidade verificada (nenhum artefacto tem build hoje → passo de compilação é genuinamente novo).

## Notas
- Não construir código do factory antes do Passo 2 fechar.
- CHANGELOG não tocado (não houve código de produto — só docs/governança).
- `ClaudeCodeSetup.md` mostra `SG#` desatualizado; track real é `S#`.
