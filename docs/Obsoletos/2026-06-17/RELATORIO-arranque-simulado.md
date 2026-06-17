# RELATÓRIO — Arranque simulado (sessão nova, modo read-only)

> Documento de teste. Objetivo: provar que os ficheiros de continuidade do projeto
> **se bastam a si próprios** para um agente sem memória reconstruir o estado e o rumo.
> Escrito a partir de: `handoff.md`, `context.md`, `roadmap.md`, `docs/mapa-artefactos.md`,
> `memory.md` (e `CLAUDE.md` para o protocolo). **Não li `SessionTranscripts/`** (proibido).
> Nada no repositório foi alterado além deste ficheiro.

---

## 1. Objetivo do projeto (o que é o html-factory)

O **html-factory** é uma *fábrica* de artefactos **HTML single-file** (um único ficheiro
que abre offline, sem dependências de runtime). Fonte: `context.md` §1 e `CLAUDE.md`.

**Problema que resolve para o David.** O David é engenheiro estrutural sénior e
**não-programador por opção**: quer gerir o agente como **arquitecto**, não como operário.
Hoje, para mudar um artefacto, tem de **explicar por prosa** ao agente o que mudar ("muda
este bloco assim") — atrito de comunicação que consome tempo. A fábrica substitui essa prosa
por **peças reutilizáveis + uma planta declarativa** (`workspace.json`): o David **declara**
layout e que blocos quer; o agente **constrói** o HTML final. Fonte: `context.md` §1,
`CLAUDE.md` ("Fluxo nuclear").

Fluxo nuclear (a planta declara, o agente constrói):
`workspace.json (David declara) → Claude Code (pega nos blocos + dados) → HTML single-file offline`.

**Critério-mãe (precedência sobre tudo).** "Simplificar a relação David↔agente —
**menos** tempo a explicar mudanças, não mais." Ordem de prioridades: **Simplicidade >
completude > elegância.** Se uma decisão puxar para "semanas de infraestrutura" antes de algo
funcionar, ou exigir que o David domine um protocolo pesado, **falhou o propósito** — o agente
deve PARAR e reportar. Fonte: `context.md` §1, `CLAUDE.md` ("Critério-mãe").

---

## 2. Para que serviu o mapa de artefactos (`docs/mapa-artefactos.md`)

**Porque foi feito.** Antes de construir a fábrica, era preciso ir ver as peças que o David
**já fez à mão** (a pasta `Artefactos-existentes/`, ~18 famílias de artefactos), lendo-as
nas **3 camadas** da arquitetura-alvo — **Dados (SSOT) / Motor / Viewer** — para descobrir
**o que se repete em todas**. Esse padrão comum é a matéria-prima da **Alfândega** (o contrato
único) que se decide no grill (Passo 2). O mapa **não é** decisão de arquitetura — é o
levantamento que a alimenta. Fonte: `mapa-artefactos.md` cabeçalho e §0.

**Como foi feito (método).** 5 subagentes `Explore` em paralelo (read-only, não tocam nos
backups), repartidos por clusters; verificação por um `code-reviewer` + leitura direta dos 2
ficheiros mais centrais (`sec7-viewer.js`, `V0.json`); síntese final feita pelo próprio agente.
Confiança ALTA nos ficheiros lidos/verificados, MÉDIA nos lidos por amostragem (>300 KB lidos só
pelo esqueleto). Decisão registada como **D8** em `memory.md`. Commits `5eb221a` + `8642f63`.

**O que descobriu (achados concretos):**

- **O domínio reduz-se a 3 modos.** Quase tudo cai em **grafo / árvore / tabela** — exatamente
  os 3 modos do Motor previstos no briefing. O grafo é o mais frequente (8+ artefactos).
- **As 4 peças da fábrica já existem na natureza, mas dispersas** (insight central, §5/§1):
  - **contrato de dados** mais maduro → **TableEditor** (envelope Frictionless, round-trip lossless);
  - **viewer cego** ideal → classe **`FloorViewer`** (recebe `loadData()` e só desenha);
  - **ciclo reativo** melhor → **curador-v3** (`commit() = save() + renderAll()`);
  - **formato de grafo** mais limpo → **`knowledge-graph.json`** (`nodes[]` + `edges[]` tipadas).
  A fábrica é **juntar num sítio só** o que o David já acertou em separado.
- **App de referência principal = curador v3** (não v4 — `v4` foi experimento que não entrou em
  produção; correção do David, decisão **D9**). É a mais complexa, com o contrato de grafo mais
  rico (projeto / link de 11 tipos / domínio em árvore) e o melhor Ciclo Reativo; ressalva: o
  *viewer* é acoplado (cor do nó *hardcoded* em `renderGraph`, render total sem diffing).
- **Padrão comum confirmado** (§3): todos os artefactos vivos têm (a) um **STATE global**,
  (b) um **ciclo `evento → muta STATE → render → DOM`** (= o Ciclo Reativo "um só sentido"),
  (c) **tema centralizado em CSS `:root`**.
- **3–4 violações de "estética fora dos dados"** (§4): `dossier-credito-v5` (`color` hex no dado),
  `governance-explorer` (`cor:'emerald'`), `MAPA-EXPLORADOR` (`ORIG`/`move`/`relev`) e `zonas`
  (`cor` no objeto). São avisos: a Alfândega tem de **proibir** isto de raiz.

**Como liga ao próximo passo.** O mapa é literalmente a **munição do grill** (§7): enquadra as
4 tensões com evidência real de ambos os lados. Em particular, a tensão-mãe **T2 (Alfândega)**:
há material para um contrato real, mas o domínio **bifurca em 3 modos** — daí a pergunta aberta
"um contrato único vs. um por modo". O mapa também **confirma o grafo como piloto** (§6) e dá uma
proposta concreta de Alfândega v0 para o M3.

---

## 3. Onde estamos e o que vem a seguir

**Marcos já fechados** (fonte: `roadmap.md`, `handoff.md`, `context.md` §4):

- **M0 — Rede de segurança (git)** ✅ — `git init`, `.gitignore`, commit `pre-grill`, branch
  `grill1`. Backups absorvidos (4 `.git` internos removidos — decisão **D1**).
- **M0.5 — Governança / continuidade** ✅ (S1) — CLAUDE.md + camada de continuidade +
  `.claude/settings.json` (commit `Setup-ClaudeCode`).
- **M1 — Mapa dos artefactos** ✅ (S1) — `docs/mapa-artefactos.md` escrito e verificado.

**Próximo marco: M2 — Grill (`grill-with-docs`)** ⬜. Correr o grill **alimentado pelo mapa**
para **fechar as 4 tensões** (T2 Alfândega primeiro) → entregável `docs/decisoes-grill.md`.

**Depois: M3 — Piloto grafo** ⬜ — Caixa (Dados/Config/Motor/Viewer) + Alfândega v0 + **um**
bloco (grafo) a renderizar **dados reais** (`knowledge-graph.json` ou links do `V0.json`),
ponta-a-ponta → commit. M4–M9 seguem (generalizar Alfândega, 2.º bloco, restantes blocos,
manifesto `workspace.json`, folha de binding, editor).

**Por que NÃO se deve construir código já.** Regra explícita e repetida em vários sítios:
*"Não construir código do factory antes do Passo 2 (grill) fechar"* (`CLAUDE.md` "NÃO fazer";
`roadmap.md` M2; `handoff.md` notas). A razão de fundo: a **Alfândega** (o contrato que todos os
blocos respeitam) é a **peça-mãe**, e a sua forma depende de uma decisão do David que ainda não
foi tomada (um contrato vs. um por modo). Construir antes seria escolher essa arquitetura em
silêncio — e há a regra de que **as 4 tensões são decisão do David, não do agente**. O `handoff.md`
acrescenta um gate de processo: *"NÃO arrancar o Passo 2 sem o David mandar — confirma primeiro."*

---

## 4. Regras absolutas a respeitar nesta sessão

**Invariantes (não-negociáveis — `CLAUDE.md`, `context.md` §3):**
1. **Single-file no produto final** — o edifício entregue é um HTML só, abre offline.
2. **Imutabilidade** — o HTML compilado é descartável ("betão curado"); o capital vive nos
   módulos isolados. Só válido se existir **sempre** um passo de compilação.
3. **Separação estanque** — Dados / Config / Motor / Viewer; mexer numa peça não parte as outras.
4. **Estética fora dos dados** — nunca cor/posição no `data.json`; vão para `config.json`.

**O que NÃO fazer (`CLAUDE.md`):**
- Não construir código do factory **antes do Passo 2 fechar**.
- **Não decidir sozinho as 4 tensões** (Alfândega, Desacoplamento, Auxiliar/espelho, Editor) —
  são do David.
- Não avançar de incremento sem o anterior **funcional e commitado**.
- Não quebrar os invariantes.
- **Não tocar em `Artefactos-existentes/`** — é referência **read-only** (backups); ler/mapear,
  não corromper.
- Não "melhorar" código adjacente ao que foi pedido (mudanças cirúrgicas).
- **Não ler `SessionTranscripts/`** salvo ordem explícita do David.

**Estilo de comunicação (`CLAUDE.md`, briefing §7):**
- **PT-PT** sempre.
- **Linguagem Ubíqua sempre com tradução civil** (o termo a seco falha; a tradução sozinha também).
- **Ritmo com gate:** uma ideia por vez, do macro para o micro, e **PARA** a pedir confirmação
  antes de avançar. Não despejar análise densa em bloco.

**Protocolo de arranque (que segui):** ler `handoff.md` → `context.md` → `roadmap.md`, verificar
alinhamento, **não** ler transcrições, e perguntar ao David se quer **continuar tarefas** (seguir
roadmap/handoff) ou fazer **adições ao roadmap** (e nesse caso ler `bugs.md`/`additions.md` primeiro).

---

## 5. Linguagem Ubíqua (1 linha cada)

- **SSOT (`data.json`)** — a verdade única: dados + relações + IDs, **zero estilo**.
- **Alfândega** — o contrato/schema de fronteira que **todo o bloco respeita** (controla o formato
  dos dados); é a peça-mãe a decidir no grill.
- **Motor** — a lógica que transforma os dados, em 3 modos: relações (grafo) / hierarquia (árvore) / tabela.
- **Viewer** — a "fachada cega": desenha o que o Motor lhe entrega, sem "saber" de dados.
- **Bloco** — um par {Motor + Viewer} normalizado à Alfândega (grafo, árvore, tabela, cartões…).
- **Manifesto / planta (`workspace.json`)** — declara layout + que blocos aparecem; é a "linguagem
  de mudança" do David.
- **Ciclo Reativo ("um só sentido")** — clique → Motor → dados mudam → ecrã atualiza; **nunca** ao
  contrário.

*(Termos adicionais da tabela: **Config (`config.json`)** = estética isolada, fora do SSOT;
**Folha de binding** = como o David escolhe, por menu, que dados cada bloco mostra;
**Isolamento Acústico** = cada bloco é fechado e **nomeado**, logo "muda aquilo" tem endereço exato.)*

---

## 6. Pontos de confusão, lacunas e contradições

Honestamente, os ficheiros estão **muito coerentes entre si** — `handoff.md`, `context.md`,
`roadmap.md`, `memory.md` e `mapa-artefactos.md` contam a mesma história sem se contradizerem, e
o `handoff.md` traz um bloco de arranque explícito que orienta a leitura. Reconstruir o estado foi
direto. Ainda assim, registo o seguinte, por honestidade:

1. **`ClaudeCodeSetup.md` está desatualizado e auto-assumido como tal.** Mostra o esquema de
   sessões `SG#`, abandonado a favor do track único `S#` (decisão **D7**; nota também no
   `handoff.md`). Não é contradição perigosa — está sinalizado — mas é uma fonte que um agente
   ingénuo poderia seguir por engano. Lacuna menor de higiene documental.

2. **A tensão "Auxiliar/espelho" nunca é definida em texto civil.** Aparece nas listas de tensões
   (`context.md` §6, `handoff.md`, `mapa` §7) e há o precedente dos "canais à la carte" do
   TableEditor, mas **o que é** exatamente um "auxiliar/espelho" e por que seria peça própria não
   está explicado num sítio só — depende provavelmente do `B-BRIEFING`, que não li nesta simulação.
   Quem arrancar só com os ficheiros de continuidade percebe que **há** esta tensão, mas não a
   *substância* dela sem ir ao briefing.

3. **A arquitetura de diretórios em `context.md` §2 é "proposta", não decidida.** Está
   honestamente marcada como "a confirmar no grill", mas inclui detalhes (`build/assemble.*`,
   `dist/workspace.html`) que poderiam ser lidos como já fixados. Risco baixo porque está rotulado.

4. **O "passo de compilação" é central mas ainda inexistente.** O mapa (§7) é claro: **nenhum**
   artefacto tem build hoje — todos são single-file editados à mão. Logo, o passo módulos→HTML
   (que torna a Imutabilidade *verificável* e não só decretada) é genuinamente **novo** e ainda
   não tem desenho. Não é contradição; é a maior incógnita técnica à frente, e está bem assinalada.

5. **Dependência implícita dos 3 documentos de bootstrap.** Os ficheiros de continuidade remetem,
   para "o que construir", aos `A-MANUAL` / `B-BRIEFING` / `C-INSTRUCAO`. Confirmei que **existem**
   na raiz, mas **não os li** (o exercício pedia "a partir SÓ" dos ficheiros de continuidade). Ou
   seja: os ficheiros de continuidade bastam para reconstruir **estado, rumo e processo**, mas para
   o **detalhe fino do que construir** (ex.: definição exata da tensão Auxiliar/espelho, §4 do
   briefing dos invariantes) continua a ser preciso o briefing. Isto parece-me **desenho
   intencional**, não falha.

**Conclusão do teste:** os ficheiros de continuidade são **autossuficientes para o arranque
operacional** (onde estamos, o que vem a seguir, regras, próximo gate). A única dependência real
para *executar o próximo passo* é o `B-BRIEFING` para a substância de uma das tensões. Os pontos
1–4 são lacunas menores, já sinalizadas pelos próprios ficheiros.
