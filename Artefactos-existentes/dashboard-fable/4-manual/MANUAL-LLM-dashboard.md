---
created: 2026-06-11
chat: Dashboard governo colapsável — orquestração Claude Code
summary: >
  Manual para LLMs: schema do bloco DATA, procedimento de update de conteúdo,
  validação pós-edição, e regra de proveniência. Permite que um modelo barato
  atualize o dashboard sem ler mais nada além deste manual + doc de conteúdo novo + bloco DATA.
---

# MANUAL-LLM — Dashboard do Governo AI

> **Para quê:** permite que um LLM (incluindo um modelo barato como Haiku 4.5) atualize o conteúdo do dashboard sem precisar de ler o código HTML. Lê este manual + o documento de conteúdo novo + o bloco DATA, e edita apenas esse bloco.
> **O que nunca tocar:** tudo fora do bloco DATA (CSS, motor JS, HTML estrutural). O bloco DATA é a única zona editável.

---

## §1. Localizar o bloco DATA

No ficheiro `2-dashboard/DIAGRAMAS-governo-dashboard.html`, procura os delimitadores:

```
/* ===DATA-START=== */
const VIEWS = [ ... ]
/* ===DATA-END=== */
```

**Edita apenas o conteúdo entre estes dois comentários.** Nunca apagues os delimitadores. Nunca escrevas nada fora deste bloco para alterar conteúdo.

---

## §2. Schema — a estrutura do bloco DATA

O bloco DATA contém um array `VIEWS` com 4 entradas (uma por folha). Cada entrada tem este schema:

### 2.1 Schema de uma vista (folha)

```js
{
  id: string,           // ex: 'v1' — não alterar
  num: string,          // ex: 'FOLHA 1' — não alterar
  titulo: string,       // ex: 'A SESSÃO' — não alterar
  nome: string,         // subtítulo descritivo
  vb: [x, y, w, h],    // viewBox SVG — não alterar
  overview_tec: string, // 1 parágrafo — explicação técnica da folha
  overview_simples: string, // 1 parágrafo — explicação sem jargão
  parent_links: [       // ligações entre grupos, como frases
    ["idGrupoA", "idGrupoB", "frase que descreve a ligação"],
    ...
  ],
  tour: [string],       // array de ids de grupos, na ordem da tour
  nodes: [...],         // ver §2.2
  edges: [...]          // ver §2.3 — normalmente não se alteram
}
```

### 2.2 Schema de um nó

```js
{
  id: string,           // identificador único — não alterar
  parent: string|null,  // id do grupo-pai, ou null se é grupo
  level: 0|1,           // 0 = grupo/pai, 1 = filho
  kind: string,         // ver §2.4
  file: string,         // OBRIGATÓRIO se kind='ficheiro'; omitir nos outros
  x, y, w, h: number,  // geometria SVG — não alterar (o motor posiciona)
  tag: string,          // etiqueta curta em maiúsculas — ex: 'INPUT', 'ANÁLISE'
  l: [string],          // linhas do label no SVG (máx 3-4 linhas curtas)
  desc_tec: string,     // explicação técnica completa do nó
  desc_simples: string  // explicação sem jargão (ver §2.5)
}
```

### 2.3 Schema de uma aresta (edge)

```js
[from_id, to_id, label?, crit?, dash?]
// crit: 1 = caminho crítico (cor âmbar, linha grossa)
// dash: 1 = linha tracejada (condicional/referência)
// Exemplo: ['n1','n2','desbloqueia',1] — caminho crítico com label
```

### 2.4 Valores válidos para `kind`

| kind | Quando usar | Estética |
|---|---|---|
| `"grupo"` | Nós de nível 0 (containers) | Rect azul translúcido, borda grid-strong |
| `"doc"` | Documento / ficheiro de input | Rect com fill azul claro |
| `"processo"` | Processo / análise / passo | Rect default (fill escuro, borda line) |
| `"decisao"` | Decisão consolidada | Borda verde |
| `"pendente"` | Pendente por resolver | Borda âmbar tracejada |
| `"marco"` | Marco / resultado | Rect âmbar arredondado (rx:18) |
| `"ficheiro"` | Ficheiro concreto com path | Rect default + campo `file` obrigatório |

> **Nota:** os nós de nível 1 ainda têm o campo `st` (herdado da versão anterior, ex: `st:'doc'`). O motor usa `kind` para o painel mas `st` para a classe CSS. Ao criar nós novos, define ambos com o mesmo valor.

### 2.5 Regras para `desc_simples`

- Para um leitor inteligente que **não vive neste sistema**
- Sem jargão não explicado: traduz "append-only" → "cresce mas nunca é reescrito"; "SSOT" → "fonte única de verdade"; "front matter" → "cabeçalho de metadados do ficheiro"; "Tier 1" → "documentos carregados sempre no arranque"
- 1–3 frases; analogia quando ajudar
- Não é um resumo da `desc_tec` — é outra explicação do mesmo facto
- Se não souberes o que escrever: `"(a confirmar)"` — lista no relatório de update

---

## §3. Procedimento de update de conteúdo

### 3.1 Update simples — alterar descrição de um nó existente

1. Localiza o nó pelo `id` dentro do bloco DATA
2. Edita `desc_tec` e/ou `desc_simples`
3. Se o nó for `kind:'ficheiro'`, verifica que o campo `file` está correto
4. Não alteres `x, y, w, h, id, parent, level`
5. Corre o checklist §4

### 3.2 Adicionar um nó filho a um grupo existente

1. Escolhe o grupo pai — verifica o seu `id` (ex: `g1_inputs`)
2. Cria um novo nó com:
   - `id` único (convenção: prefixo do grupo + descritor, ex: `i8`)
   - `parent`: id do grupo pai
   - `level: 1`
   - `kind`: o valor correto (§2.4)
   - `x, y, w, h`: posiciona **dentro** do rect do grupo pai (usa as coordenadas dos filhos existentes como referência de espaçamento)
   - `tag`, `l`, `desc_tec`, `desc_simples`
3. Adiciona as arestas necessárias no array `edges` da vista
4. **Atenção:** se o nó novo ficar fora do bounding box do grupo pai, aumenta `w` e/ou `h` do grupo para o conter (padding mínimo 14px)
5. Corre o checklist §4

### 3.3 Adicionar um grupo novo

1. Calcula a bounding box dos filhos planeados (x_min, y_min, x_max, y_max)
2. Grupo: `x = x_min - 14`, `y = y_min - 24` (espaço para o label), `w = (x_max - x_min) + 28`, `h = (y_max - y_min) + 38`
3. `level: 0`, `parent: null`, `kind: 'grupo'`
4. Adiciona o id do grupo ao array `tour` da vista (posição lógica)
5. Adiciona entradas relevantes a `parent_links`
6. Cria os nós filhos com `parent` = id do grupo novo
7. Corre o checklist §4

### 3.4 Alterar a overview ou tour de uma folha

- `overview_tec` e `overview_simples`: edita diretamente — 1 parágrafo cada
- `parent_links`: array de triplos `[idA, idB, frase]` — uma linha por ligação grupo-a-grupo
- `tour`: array de ids de grupos na ordem lógica — deve conter todos os grupos da folha

### 3.5 O que NUNCA alterar

- `id`, `parent`, `level` de nós existentes — o motor depende deles
- `vb` (viewBox) de qualquer vista
- `x, y, w, h` de nós existentes (a menos que estejas a mover deliberadamente com ajuste do grupo)
- Os delimitadores `/* ===DATA-START=== */` e `/* ===DATA-END=== */`
- Qualquer coisa fora do bloco DATA

---

## §4. Validação pós-edição (checklist)

Antes de entregar, verifica cada ponto:

- [ ] **JSON válido:** o bloco DATA é JavaScript válido (sem vírgulas em falta, strings fechadas, colchetes balanceados)
- [ ] **Nenhum nó sem `desc_tec` E `desc_simples`** — exceto os marcados `(a confirmar)` (lista-os no relatório)
- [ ] **Todo o `kind:'ficheiro'` tem campo `file`** preenchido
- [ ] **Nós novos têm `parent` válido** (o id existe no array `nodes` da mesma vista)
- [ ] **Nós novos estão dentro do bounding box do seu grupo** (ou o grupo foi aumentado)
- [ ] **`tour` de cada vista inclui todos os grupos** (nós com `level:0`) da vista
- [ ] **`parent_links` referencia apenas ids de grupos** que existem na vista
- [ ] **Nenhuma aresta referencia um id inexistente** — verifica `from_id` e `to_id` em `edges`
- [ ] **Conteúdo derivado de `3-conteudo/`** — nada inventado; pendentes aparecem como `kind:'pendente'`; D2 superseded marcado como tal

---

## §5. Regra de proveniência

**Todo o conteúdo das descrições deriva dos documentos em `3-conteudo/`.** Nunca inventar factos. Nunca usar memória do modelo sobre o sistema do David.

A autoridade máxima é `CRISTALIZACAO-SESSAO_projeto-arranque-de-projeto_v2.md`. Em conflito com outros documentos, esta versão prevalece (a v1 está superseded — ignorar).

Se um facto não tiver fonte em `3-conteudo/`, escreve `(a confirmar)` e lista no relatório de update.

---

## §6. Referência rápida — ids dos grupos por folha

| Folha | Grupos (level 0) |
|---|---|
| v1 — A Sessão | `g1_inputs`, `g1_analises`, `g1_decisoes`, `g1_outputs` |
| v2 — O Fecho | `g2_prep`, `g2_pend`, `g2_exec`, `g2_marcos` |
| v3 — O Pacote em Execução | `g3_kit`, `g3_orch`, `g3_criados`, `g3_marco` |
| v4 — O Projeto em Operação | `g4_arranque`, `g4_runtime`, `g4_fecho`, `g4_bb` |

---

*Fim do MANUAL-LLM · Dashboard Governo AI · 2026-06-11*
