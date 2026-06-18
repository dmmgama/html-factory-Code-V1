# handoff.md — estado imediato

> Telegráfico, denso, sem narrativa. Reescrito a cada fecho. Próxima sessão lê isto primeiro.

> [!IMPORTANTE] ARRANQUE (lê isto antes de tudo)
> 1. **A verdade está nos ficheiros, não no transcript.** Lê por ordem: este `handoff.md` →
>    `context.md` → `roadmap.md` → [`docs/mapa-artefactos.md`](docs/mapa-artefactos.md). Depois
>    `CLAUDE.md` para o protocolo de trabalho.
> 2. **Onde estamos:** Passo 0 (git) ✅, governança ✅, **Passo 1 / M1 (mapa dos artefactos) ✅**.
>    **Próximo = Passo 2 / M2 (grill)** para fechar as 4 tensões → `docs/decisoes-grill.md`.
>    **NÃO há código do factory ainda** (correto — não se constrói antes do grill fechar).
> 3. **Branch atual: `grill-Correto`** (linha corrigida pós-fork). O grill (Passo 2) corre
>    **externamente** com o `handoff-grill.md`; `grill-with-External` guarda o trabalho verificado
>    do fork (**preservar, não tocar**); `master`=`pre-grill` (retorno limpo).
> 4. **O QUE construir** manda nos 3 docs: `A-MANUAL…`, `B-BRIEFING…`, `C-INSTRUCAO…`.
> 5. **Regras que se esquecem:** não construir antes do Passo 2 fechar; **não decidir sozinho as 4
>    tensões (são do David)**; `Artefactos-existentes/` é referência read-only; PT-PT + Linguagem
>    Ubíqua c/ tradução civil, uma ideia por vez com gate; proibido ler `SessionTranscripts/` sem ordem.
> 6. **O grill (Passo 2) NÃO é executado por este agente (Code).** Corre **externamente** (branch
>    `grill-with-External`). Este Code prepara/integra; **não arranca o grill por iniciativa própria**.

**Sessão atual:** S1 — Setup + Mapa (M1) + absorção SArq-3 + arrumação + **linha corrigida pós-fork**. **Transcript gravado.**
**Branch atual:** `grill-Correto` (linha corrigida).
**Mapa de ramos:** `master`=`pre-grill` (retorno limpo, `f50ecef`) · `grill1`=baseline pré-grill ·
`grill-with-External`=*ensinamento* do fork (v2 verificada — **preservar, não tocar**) ·
`grill-Correto`=linha corrigida **(atual)**.
**Material corrigido (trazido por git):** `docs/Ideia-Design-v2/` (16 fich.) + `veredicto-v2-grill.md`
+ `handoff-grill.md` (handoff p/ o grill **externo**). Linhas do curador verificadas no ficheiro real
(`CORRECAO-blocos-curador.md`): `renderGraph`=1081, `renderFilterBar`=680; `renderAsgMindmap` **não existe**
(mind-map = modo de `renderGraph`). **Onde o M1 estimou linhas, manda o ficheiro real / a v2.**

## Feito
- **Passo 0:** `git init`, `.gitignore`, commit `pre-grill`, branch `grill1`. Backups absorvidos
  (4 `.git` internos removidos de FichaProjetosJSJ/LifeMap/TableEditor/projeto-ssot).
- **Governança (M0.5):** CLAUDE.md + continuidade + `.claude/settings.json` (commit `Setup-ClaudeCode`).
- **Passo 1 / M1 (mapa):** [`docs/mapa-artefactos.md`](docs/mapa-artefactos.md) — ~18 famílias em 3
  camadas (Dados/Motor/Viewer). Feito com 5 subagentes `Explore` (read-only) + verificação
  (`code-reviewer` + leitura direta de `sec7-viewer.js`/`V0.json`). Commits `5eb221a` + `8642f63`.
- **Teste de continuidade:** subagente Opus read-only simulou o arranque só pelos ficheiros e passou
  (relatório arquivado em `docs/Obsoletos/`). Confirma que os ficheiros se bastam. Síntese arquitetura:
  ~80% montagem de moldes provados; único novo = passo de compilação; única decisão aberta = Alfândega (T2).
- **Absorção SArq-3 + arrumação:** li o material da SArq-3 (ver bloco abaixo) → `docs/ideia-design/RELATORIO-ideia-design.md`.
  Arrumei a raiz: arqueologia (`ClaudeCodeSetup`, `RELATORIO-arranque-simulado`, `agente-lerIdeia`) →
  `docs/Obsoletos/2026-06-17/`. Nova secção "Arqueologia" no `CLAUDE.md`.

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
   - **AO ARRANCAR o grill: absorver a SArq-3 e aplicar os 4 patches candidatos** (ver bloco
     "Material SArq-3" abaixo). Antes disso já estão lidos, não aplicados.
   - "Auxiliar/espelho": a SArq-3 já dá a definição civil (subsumido por manifesto+binding) — falta
     só confirmar com o David se desaparece como peça.
2. **Passo 3 / M3 — piloto grafo:** Caixa (Dados/Config/Motor/Viewer) + Alfândega v0 + bloco grafo
   a render dados reais (`knowledge-graph.json` ou links do curador). Ponta-a-ponta → commit.

## Tensões em aberto (para o grill — Passo 2)
T2 Alfândega genérica (um contrato vs. um por modo — peça-mãe, primeiro) · T1 Desacoplamento
(parte-se o STATE global; moldes: curador-v3 + `FloorViewer.loadData`) · Auxiliar/espelho
(precedente: "canais à la carte" do TableEditor) · Editor (Gridstack vs texto; já há os dois mundos) ·
Imutabilidade verificada (nenhum artefacto tem build hoje → passo de compilação é genuinamente novo).

## Material SArq-3 (entra no grill — lido, NÃO aplicado)
Sessão de arquitetura paralela (chat externo) que **completou** a SArq-2. Material em
[`docs/ideia-design/`](docs/ideia-design/); a minha leitura/síntese em
[`docs/ideia-design/RELATORIO-ideia-design.md`](docs/ideia-design/RELATORIO-ideia-design.md)
(a ordem de leitura original, `agente-lerIdeia.md`, foi para arquivo). **Convergiu com o M1.** Para o grill:
- **Fluxo "planta → Code"** + peça nova **Manifesto** (`workspace.json`); vocabulário novo
  **Chassis / Slot / Silhueta** + regra **VIVO vs MORTO** (definições no `GLOSSARIO-html-factory.md`).
- **4 patches candidatos a aplicar AO ARRANCAR o grill** (não antes): `PatchCDesign-context/roadmap/CLAUDE`
  (Claude Design = candidato a editor) + `PatchGlossario-integracao` (Glossário = dono do vocabulário;
  CLAUDE.md **aponta, não absorve**; quanto da tabela migra = decisão no grill).
- **Editor:** 3–4 candidatos (Claude Design+silhuetas · D-proc/Procreate · manifesto-em-texto · Gridstack).
  Recomendação: manifesto-em-texto 1.º; Claude Design preso a teste de import/export (preservar Slots).
- **Reconciliar:** 3 **modos** = relações/hierarquia/tabela; "grafo/árvore" são **vistas**, não modos
  (alinhar M1). **Linhas do curador da SArq-3 vêm de cópia web → não são verdade; manda o M1**
  (re-verificar no ficheiro real antes de extrair).

## Notas
- Não construir código do factory antes do Passo 2 fechar.
- CHANGELOG não tocado (não houve código de produto — só docs/governança).
- `docs/Obsoletos/` = arqueologia, **nunca ler** (regra no `CLAUDE.md`). Track de sessões real é `S#` (não `SG#`).
- **O grill (M2) corre num agente EXTERNO** (branch `grill-with-External`), não neste Code. Este agente
  preparou o material (mapa M1 + absorção SArq-3 + 4 patches) e depois integra o que o grill decidir.
