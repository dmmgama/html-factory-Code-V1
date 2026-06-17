# CLAUDE.md — html-factory

Instruções para o Claude Code neste projeto. Lê isto por completo antes de agir.
Idioma de trabalho: **PT-PT**.

> Este projeto tem três documentos de bootstrap que mandam sobre tudo o resto:
> - [`A-MANUAL-implementacao-DAVID.md`](A-MANUAL-implementacao-DAVID.md) — a visão do David.
> - [`B-BRIEFING-arquitetura-AGENTE.md`](B-BRIEFING-arquitetura-AGENTE.md) — a lógica/arquitetura.
> - [`C-INSTRUCAO-arranque-AGENTE.md`](C-INSTRUCAO-arranque-AGENTE.md) — a ordem de trabalho (Passos 0→3).
>
> Em caso de dúvida sobre **o que construir**, mandam estes. Este `CLAUDE.md` governa **como
> trabalhamos** (processo, continuidade, disciplina).

---

## Arranque de cada sessão (obrigatório, por esta ordem)
1. Ler **`handoff.md`** (estado imediato da sessão anterior).
2. Ler **`context.md`** (SSOT acumulado) e **`roadmap.md`** (rumo do projeto).
3. **Verificar alinhamento:** confirmar se `handoff.md` e `context.md` estão coerentes com
   `roadmap.md`. Se houver discrepâncias **relevantes para o objetivo da sessão atual**,
   assinalá-las ao utilizador antes de continuar.
4. **NÃO ler `SessionTranscripts/`** — proibido salvo indicação explícita do David.
5. **Perguntar ao David:** *"Queres **continuar tarefas** (seguir o roadmap/handoff) ou fazer
   **adições ao roadmap** (novos requisitos/correções)?"*
   - **Continuar tarefas** → próximo item do handoff/roadmap.
   - **Adições ao roadmap** → ler primeiro `bugs.md` e `additions.md`, apresentar o registado,
     e só então discutir e incorporar.

---

## O que é o projeto
**html-factory** — uma *fábrica* de artefactos HTML single-file. O David é engenheiro
estrutural sénior, **não-programador por opção**: quer gerir o agente como **arquitecto**, não
como operário. A fábrica substitui a *prosa* ("muda este bloco assim") por **peças
reutilizáveis + uma planta declarativa** (`workspace.json`).

**Critério-mãe (precedência sobre tudo):** a fábrica existe para **simplificar** a relação do
David com o agente — menos tempo a explicar mudanças, não mais. Se uma decisão puxar para
"semanas de infraestrutura" antes de algo funcionar, ou exigir que o David domine um protocolo
pesado, **falhou o propósito**. **Simplicidade > completude > elegância.**

Fluxo nuclear — **a planta declara, o agente constrói:**
```
EDITOR/PLANTA (workspace.json)  →  TU (Claude Code)  →  HTML single-file final, offline
o David declara layout+blocos      pegas nos blocos       a funcionar
                                   da biblioteca + dados
```

### Stack / ambiente
- HTML + CSS + JavaScript vanilla (single-file no **output**). Pode haver passo de compilação
  módulos → HTML; o single-file é o *output*, não obrigatoriamente o ambiente de dev.
- Windows + PowerShell (shell primário). Bash também disponível.
- Sem dependências de runtime no produto final (abre offline).

## Linguagem Ubíqua (usa estes termos SEMPRE com tradução civil)
| Termo | Tradução civil |
|---|---|
| **SSOT (`data.json`)** | a verdade única: dados + relações + IDs, **zero estilo** |
| **Alfândega** (schema/contrato) | controlo de fronteira do formato — o contrato que todo o bloco respeita |
| **Motor** | a lógica que transforma dados (3 modos: relações / hierarquia / tabela) |
| **Viewer** | a fachada cega — desenha o que o motor entrega, não "sabe" de dados |
| **Config (`config.json`)** | estética isolada (cores, tema), fora do SSOT e do motor |
| **Bloco** | par {Motor + Viewer} normalizado à Alfândega (tabela, árvore, grafo, cartões…) |
| **Manifesto / planta (`workspace.json`)** | declara layout + que blocos — a "linguagem de mudança" do David |
| **Folha de binding** | como o David diz "que dados mostra cada bloco" (menus, ele escolhe, não escreve) |
| **Isolamento Acústico** | cada bloco é fechado e **nomeado** → "muda aquilo" tem endereço exato |
| **Ciclo Reativo ("um só sentido")** | clique → Motor → dados mudam → ecrã atualiza. NUNCA ao contrário |

## Invariantes (regras absolutas — não negociáveis, briefing §3)
- **Single-file no produto final.** O edifício entregue é um HTML só, abre offline.
- **Imutabilidade.** O HTML compilado é descartável ("betão curado"); o capital vive nos
  módulos isolados. Só válido se existir SEMPRE um passo de compilação.
- **Separação estanque.** Dados / Config / Motor / Viewer — mexer numa peça não parte as outras.
- **Estética fora dos dados.** Nunca metas cor/posição no `data.json`. Vai para `config.json`.

## NÃO fazer
- **Não construir código do factory antes do Passo 2 (grill) fechar.** Mapa (Passo 1) e
  decisões (Passo 2) primeiro.
- **Não decidir sozinho as tensões do Passo 2** (Alfândega genérica, Desacoplamento,
  Auxiliar/espelho, Editor) — são do David.
- Não avançar de incremento sem o anterior **funcional e commitado**.
- Não quebrar os invariantes acima.
- Não tocar nos artefactos de `Artefactos-existentes/` para os "melhorar" — são **referência
  read-only** (backups). Lê, mapeia, não corrompas.
- Não "melhorar" código adjacente ao que foi pedido (ver guidelines).

---

## Ordem de trabalho (resumo do C-INSTRUCAO — detalhe no ficheiro)
- **Passo 0 — git** ✅ feito (repo, commit `pre-grill`, branch `grill1`).
- **Passo 1 — Mapear `Artefactos-existentes/`** → `docs/mapa-artefactos.md` (3 camadas:
  Dados/Motor/Viewer + síntese do padrão comum). Decidir se uso subagentes de verificação.
- **Passo 2 — `grill-with-docs`** alimentado pelo mapa → fechar as 4 tensões →
  `docs/decisoes-grill.md`.
- **Passo 3+ — Incremento vertical funcional.** Cada passo a funcionar ponta-a-ponta antes do
  seguinte; um commit por incremento. Piloto recomendado: o **grafo**.

Todo o trabalho na branch **`grill1`**. `master` (`pre-grill`) é o ponto de retorno limpo.

---

## Guidelines de comportamento (reduzir erros comuns de LLM)
> Tradeoff: privilegiam cautela sobre velocidade. Para tarefas triviais, usar bom senso.

**1. Pensar antes de codificar.** Não assumir. Não esconder confusão. Expor tradeoffs.
Declarar suposições; se houver várias interpretações, apresentá-las (não escolher em silêncio);
se existir abordagem mais simples, dizê-lo; se algo for ambíguo, parar e perguntar.

**2. Simplicidade primeiro.** Código mínimo que resolve o problema. Nada especulativo: sem
features além do pedido, sem abstrações para uso único, sem "flexibilidade" não pedida.

**3. Mudanças cirúrgicas.** Tocar só no necessário. Não refatorar o que não está partido;
seguir o estilo existente. Código morto pré-existente **menciona-se, não se apaga** sem pedido.

**4. Execução orientada a objetivos.** Definir critérios de sucesso e iterar até verificar.
Para tarefas multi-passo, enunciar um plano curto com verificação por passo.

## Como comunicas com o David (briefing §7)
- **Linguagem Ubíqua sempre com tradução civil** (ver tabela). O termo a seco falha; a
  tradução sozinha também.
- **Ritmo com gate:** uma ideia por vez, do macro para o micro, e PARA a pedir confirmação
  antes de avançar. Não despejar análise densa em bloco.

---

## Continuidade entre sessões

### Fecho de cada sessão (protocolo)
1. **Atualizar `context.md`** — estado acumulado (SSOT que cresce).
2. **Atualizar `memory.md`** — o *porquê* de novas decisões (D1, D2, …).
3. **Atualizar `roadmap.md`** — progresso e próximos marcos.
4. **Atualizar `CHANGELOG.md`** — **se mexeste no código do factory**, uma linha por mudança
   visível. Registo de produto, não diário de código.
5. **Reescrever `handoff.md`** — telegráfico: feito / decisões / próximos passos / ficheiros /
   tensões em aberto. Denso, sem narrativa.
6. **Numerar a sessão:** perguntar *"Que nome dar à sessão?"* e **sugerir** `SX - Título`
   (X = sessão anterior + 1). Registar no `handoff.md` que a anterior foi `S(X-1)` e esta é `SX`.
   > **Track único `S#`** (o esquema `SG#` foi abandonado).
7. **Transcript:** perguntar se quer gravar. Se sim, ZIP `SX - Título.zip` em `SessionTranscripts/`.

### Privacidade (não-negociável)
- `SessionTranscripts/` e `logs/` **fora do git** (`.gitignore`).
- **Proibido ler `SessionTranscripts/`** salvo indicação explícita do David.
- Nada de publicação pública (ex.: GitHub Pages) sem o David pedir.

### Ficheiros de continuidade
| Ficheiro | Papel |
|---|---|
| `handoff.md` | Estado imediato p/ próxima sessão (telegráfico). Reescrito a cada fecho. |
| `context.md` | SSOT acumulado do projeto. Cresce no tempo. |
| `memory.md` | "Porquê" das decisões (não é estado corrente). |
| `roadmap.md` | Rumo/marcos do projeto. |
| `bugs.md` | Falhas conhecidas (append-only, por área funcional). |
| `additions.md` | Adições/updates ao roadmap pretendidos pelo David (append-only). |
| `CHANGELOG.md` | Alterações visíveis do produto, por versão. |
| `docs/MANUAL.md` | Manual técnico para humanos. |
