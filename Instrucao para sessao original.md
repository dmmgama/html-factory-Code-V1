**És a sessão Code do html-factory.** Uma sessão-fork correu em paralelo, detectou erros no material da ideia-design (SArq-3) e corrigiu-os, verificando contra o ficheiro real. Retomas o caminho **já corrigido**, em base limpa.

**Git — onde estás:** ramo **`grill-Correto`**, criado do `6fb4da8` (pré-fork, pristino). O trabalho verificado do fork vive em **`grill-with-External`** (o "ensinamento"). **Preserva** esse ramo — não o podes.

**Passo 1 — traz a v2 por git (NUNCA por colagem):**

```
git checkout grill-with-External -- docs/Ideia-Design-v2/ veredicto-v2-grill.md handoff-grill.md docs/ideia-design/ideiasdesign-report-fork.md
```

Bytes verificados, sem transcrição manual (foi uma cópia má que originou todo este episódio).

**Passo 2 — lê o `veredicto-v2-grill.md`** (prova curta de que a v2 está limpa). **NÃO** re-corras o `agente-lerIdeia-v2.md` nem releias tudo — o fork já fez a verificação pesada (e esse ficheiro proíbe delegar).

**Passo 3 — spot-check dirigido** (só onde houve risco), contra o `projetos-curador-v3.html` REAL, a `grep`: (a) `renderAsgMindmap` **não existe** e o mind-map vive em `renderGraph` (`UI.graphMode==="mindmap"`); (b) confere 2–3 linhas reais da tabela de `CORRECAO-blocos-curador.md` (ex.: `renderGraph` ~1081, `renderFilterBar` ~680).

**Passo 4 — valida o `handoff-grill.md`** contra três: a v2 trazida, o `docs/mapa-artefactos.md` (M1) e o `handoff.md`/`context.md`. Se contradisser o M1 (sobretudo "linhas: manda o M1" e "grill é externo"), **manda o M1**.

**Passo 5 — regista o mapa de ramos** numa linha da continuidade: `master`=pre-grill · `grill1` · `grill-with-External`=ensinamento(fork) · `grill-Correto`=linha corrigida (actual).

**Passo 6 — segue para lançar o grill externo** com o `handoff-grill.md`. O grill **não és tu** que o corres — é externo. Diz-me o teu plano antes de avançar, com gate.