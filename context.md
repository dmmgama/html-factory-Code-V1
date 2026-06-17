# context.md — html-factory (SSOT acumulado)

> Single source of truth do projeto: arquitetura, decisões, convenções, estado. Cresce a cada
> fecho de sessão. Detalhe imediato em `handoff.md`; o porquê das decisões em `memory.md`.

## 1. O que é
**html-factory** — fábrica de artefactos HTML single-file. Objetivo: substituir o atrito de
comunicação (David explica por prosa o que mudar) por **peças reutilizáveis + planta
declarativa**. O David é arquiteto não-programador; gere o agente como arquiteto.

**Critério-mãe:** simplificar a relação David↔agente. Simplicidade > completude > elegância.
Se algo puxar para "semanas de infraestrutura" antes de algo funcionar → PARA e reporta.

## 2. Arquitetura (alvo — afina no grill)
Fluxo: **planta declara → agente constrói → HTML single-file**. Peças (Linguagem Ubíqua em
`CLAUDE.md`): SSOT (`data.json`), Alfândega (contrato), Motor (3 modos: relações/hierarquia/
tabela), Viewer (fachada cega), Config (`config.json`), Bloco {Motor+Viewer}, Manifesto
(`workspace.json`), Folha de binding, Ciclo Reativo (um só sentido).

Estrutura de diretórios proposta (briefing §4, a confirmar no grill):
```
factory/
  blocks/{grafo,arvore,tabela,...}/{engine.js,viewer.js,README.md}
  schema/{alfandega.md, alfandega.schema.json}
  manifest/workspace.example.json
  config/config.example.json
  build/assemble.*
  dist/workspace.html      ← edifício final single-file
docs/{mapa-artefactos.md, decisoes-grill.md}
```

## 3. Invariantes (não-negociáveis)
- Single-file no produto final (abre offline).
- Imutabilidade: HTML compilado é descartável; capital nos módulos. Exige passo de compilação.
- Separação estanque: Dados / Config / Motor / Viewer.
- Estética fora dos dados (cor/posição → `config.json`, nunca `data.json`).

## 4. Estado atual
- **Fase:** **Passo 1 (M1) concluído** — mapa dos artefactos escrito e verificado. **Próximo:
  Passo 2 (M2) — grill** para fechar as 4 tensões.
- **Git:** repo iniciado. `master` = `pre-grill` (ponto de retorno limpo). Trabalho na branch
  **`grill1`**. Backups em `Artefactos-existentes/` absorvidos (4 `.git` internos removidos).
  Commits do M1: `5eb221a` (mapa) + `8642f63` (correção curador v3).
- **Artefactos de referência:** ~18 famílias em `Artefactos-existentes/`, **mapeadas** em 3 camadas
  → [`docs/mapa-artefactos.md`](docs/mapa-artefactos.md).
- **Achados do mapa (resumo):** o domínio cai em **3 modos** (grafo/árvore/tabela); as 4 peças da
  fábrica já existem dispersas (contrato → TableEditor; viewer cego → `FloorViewer`; ciclo reativo →
  curador-v3; grafo → `knowledge-graph.json`); **piloto = grafo** confirmado. App de referência
  principal: **curador v3** (ver D9). 3 sítios violam "estética fora dos dados" (avisos p/ Alfândega).
- **Código do factory:** **não existe ainda** (correto — não se constrói antes do Passo 2).
- **Continuidade validada:** teste de arranque simulado (subagente Opus, read-only →
  `RELATORIO-arranque-simulado.md`) confirmou que os ficheiros se bastam a si próprios para o
  arranque. **1 lacuna a corrigir no início do grill:** definir **"Auxiliar/espelho"** em linguagem
  civil (hoje só está no `B-BRIEFING`).
- **Síntese arquitetura-com-artefactos (visual S1):** ~80% da arquitetura-alvo é **montagem de
  moldes já provados** nos artefactos (contrato→TableEditor, viewer cego→FloorViewer, ciclo+motor→
  curador-v3, grafo→knowledge-graph.json). Só **uma** peça é genuinamente nova — o **passo de
  compilação**; e só **uma** decisão fica em aberto — a forma da **Alfândega** (T2).

## 5. Convenções
- Idioma de trabalho e UI: **PT-PT**.
- Um commit por incremento funcional, na branch de trabalho.
- `Artefactos-existentes/` é **referência read-only** (backups); ler/mapear, não corromper.
- Validar JS embebido de single-file com `node -e` após mexer no `<script>`.
- Numeração de sessões: track único **`S#`**.

## 6. Tensões em aberto (para o grill — Passo 2, não resolver sozinho)
- **T2 — Alfândega genérica:** o contrato único. Derivar do **padrão comum** dos artefactos,
  não só do curador. Peça-mãe; fechar primeiro.
- **T1 — Desacoplamento:** extrair blocos sem o STATE global; método (piloto vs. tudo).
- **Auxiliar/espelho:** confirmar se ainda é peça própria ou subsumido por manifesto+binding.
- **Editor:** Gridstack (arrastar) vs. manifesto-em-texto. Recomendar com trade-offs; decisão do David.
- **Imutabilidade verificada:** hoje decretada, não verificada (build stamp/hash) — quando chegar à build.

## 7. Histórico de sessões
- **S1** (2026-06-17) — Setup/governança (Passo 0 git + camada de continuidade) **e Passo 1 (M1):
  mapa dos artefactos** (5 subagentes Explore + verificação; síntese própria; foco curador v3).
  Fecho: teste de arranque simulado (Opus) passou; transcript gravado.
