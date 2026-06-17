# SPEC — Formato de Dados do TableEditor

> ## 0.1 — Adenda de rearquitectura (spec-version 2 — PREVALECE sobre o texto abaixo)
> A app foi rearquitectada para **fonte única por informação** (sem duplicação) e **canais de saída à la carte**. Onde o texto antigo conflituar, vale isto:
> - **Três classes:** **A** dados+organização (`data`, `schema` colunas/ordem/`fixed`/`hidden`/`categories`, `groupBy`, `sortHierarchy`, `fieldLinks`, `colSort`, `sortOptsEnabled`) → vive no **autosave de dados** (envelope) + ficheiro de dados. **B** config de máquina (mirror, formatos, `channels`, índice global) → vive na **config por projecto**. **C** prefs internas (`x-tableeditor`: `colSort`/`sortOptsEnabled`/`sortHierarchy` verbatim) → só no autosave; nunca em export/mirror.
> - **`type` NÃO é propriedade da tabela** — é decisão de **canal de saída**. O `schema.fields` da tabela só tem `name`/`fixed`/`hidden`/`categories` (sem `type`). `saveFormat*` **não** vivem no envelope (são classe B).
> - **I2 reformulado:** round-trip lossless é do **PAR** (autosave de dados **+** config), cobre a **classe A**. A classe B (caminhos/formatos do mirror, type/fixed/hidden de saída) é local e **não** viaja — perdê-la ao abrir noutra máquina é correcto.
> - **Export e mirror = composição à la carte por canal** (não o envelope canónico): cada canal escolhe `schema`/`types`/`view` (sim/não), `x-<destino>` opcional (`x-excel` implementado; extensível por passthrough), ou só dados crus. `data` sempre plano (I3). **Nunca** sai `x-tableeditor`. (Detalhe em §9.)
> - **Storage:** estado local em `.tableeditor/` (`index.json` + `<id>.config.json` + `<id>.autosave.json`); ficheiros de dados versionáveis na workDir.
> - **Import:** porta única (bate→sobrepõe / difere→nova tabela); pergunta antes de esmagar definições; tipos de origem guardados como `x-import` (não herdados). JSON e CSV.

## 0. Estatuto e âmbito

Este documento é a **fonte canónica** do formato de dados da app TableEditor. Governa **todas** as operações de serialização: export, import, autosave, mirror e o visualizador JSON. Qualquer código que leia ou escreva o estado da tabela DEVE estar conforme a esta spec. Em caso de conflito entre código e spec, a spec prevalece e o código corrige-se.

A spec é versionada (§8). Funcionalidades novas não alteram os invariantes (§3); estendem-se pelo protocolo da §5.

## 1. Vocabulário normativo

- **DEVE / NÃO DEVE** — requisito absoluto (MUST / MUST NOT).
- **DEVERIA** — recomendação forte; desviar exige justificação (SHOULD).
- **PODE** — opcional (MAY).

## 2. O envelope canónico

O estado completo da app É um único objecto JSON com esta forma:

```json
{
  "profile": "tabular-data-resource",
  "name": "string",
  "savedAt": "ISO-8601",
  "schema": {
    "fields": [
      { "name": "string", "type": "string", "fixed": false, "hidden": false }
    ],
    "primaryKey": ["string"],
    "fieldLinks": [
      { "parent": "string", "children": ["string"], "semantics": "string" }
    ]
  },
  "view": {
    "groupBy": ["string"],
    "sortHierarchy": [ { "field": "string", "by": "categories|asc|desc" } ]
  },
  "x-tableeditor": {},
  "data": [ { "<field>": "value" } ]
}
```

Regras dos blocos:

- **`data`** — array de objectos **planos e completos**. Uma chave por campo (nome exacto do field), valor por célula. Valor em falta DEVE ser `""`; a chave NÃO DEVE ser omitida. NÃO DEVE haver aninhamento. Repetir o valor de agrupamento em cada linha é correcto (denormalização) e obrigatório — `data` é sempre lossless e auto-suficiente.
- **`schema.fields`** — ordem do array = ordem das colunas. `name` = chave em `data`. `fixed: true` só na 1ª coluna. `type` ∈ {`string`,`number`,`integer`,`boolean`,`date`,`datetime`,`array`,`object`}. `categories` (array, opcional) define a ordem canónica dos valores do campo (ordered categorical).
- **`schema.primaryKey`** — campo(s) identificador(es). Ver §7 sobre unicidade.
- **`schema.fieldLinks`** — ligação **intra-record** (colunas que formam uma unidade lógica, ex.: `ID`/`WebDomain` identificam `Company`). NÃO confundir com relação inter-tabela (`foreignKeys`).
- **`view`** — instruções de apresentação, não estrutura. `groupBy` (campos por nível). `sortHierarchy` (ordenação composta; `by: "categories"` usa `schema.fields[].categories`).
- **`x-tableeditor`** — estado próprio da app sem equivalente Frictionless (toggles, sort UI, etc.). Outros destinos vivem em `x-notion`, `x-excel`, `x-<custom>`.
- **`savedAt`** — timestamp ISO da última gravação.

## 3. Invariantes (inviolável)

- **I1 — Independência do plano de dados (degradação graciosa).** A correcção de `data` NÃO DEVE depender de `schema`/`view`/`x-`. Um consumidor genérico DEVE poder ler só `data` e obter uma tabela correcta. Metadado enriquece; nunca é necessário.
- **I2 — Round-trip lossless.** Export→import (Protocolar) DEVE devolver estado idêntico. Conversão para vista humana e regresso NÃO DEVE perder `schema`/`view`/`x-`: a vista humana expõe só dados; o envelope é preservado e re-anexado.
- **I3 — Sem dados em chaves.** Valores de dados NÃO DEVEM ser codificados como chaves de objecto (sem agrupamento estrutural em `data`). O agrupamento é declarado em `view.groupBy`.

## 4. Mapeamento do formato legado → Frictionless

Ao importar o formato actual da app, migrar assim:

| Legado | Frictionless |
|---|---|
| `columns[].label` | `schema.fields[].name` |
| `columns[].fixed` / `.hidden` | `schema.fields[].fixed` / `.hidden` |
| `rows[]` | `data[]` |
| `groupLevels[]` | `view.groupBy[]` |
| `sortHierarchy[]` | `view.sortHierarchy[]` |
| `colSort` | `x-tableeditor.colSort` |
| `sortOptsEnabled` | `x-tableeditor.sortOptsEnabled` |
| `fieldLinks[]` | `schema.fieldLinks[]` |
| `savedAt` | `savedAt` |

Princípio: o que tem equivalente standard vai para `schema`/`view`; o que é estado-de-app-only vai para `x-tableeditor`. A migração NÃO DEVE perder informação.

## 5. Protocolo de extensão (escalabilidade)

Qualquer funcionalidade nova segue uma destas vias — **sempre aditivas**, nunca alterando `data` nem os invariantes:

1. **Nova propriedade de coluna** (ex.: largura, descrição, validação) → novo campo em `schema.fields[]`. Se for específica de um destino, ver via 3.
2. **Novo destino de export/import** (Excel, Notion, ...) → novo bloco `x-<destino>` com a config desse destino (ex.: `x-notion.properties[col].type`, `x-excel.columns[col].format`). O destino NÃO DEVE escrever em `data` nem em `schema` standard.
3. **Propriedades de coluna por destino** (ex.: "esta coluna é um `select` no Notion") → `x-<destino>.properties[<field>]`. Mapeamento sugerido a partir de sinais do schema: `categories`→Notion `select` / Excel data-validation; 1ª coluna (`fixed`)→Notion `title` / Excel coluna congelada; `type: date`→`date`; `fieldLinks` platform-identifier→`url`/`relation`; `primaryKey`→Notion `unique_id` / Excel formato texto.
4. **Nova opção de vista/agrupamento/ordenação** → `view.*`.
5. **Novo estado de UI da app** → `x-tableeditor.*`.

Regra-mãe: **standard → `schema`/`view`; específico → `x-<namespace>`; dados → só `data`, plano e completo.** Se uma feature te empurra para codificar dados em chaves ou para tornar `data` dependente de metadados, está mal desenhada — reformula segundo I1/I3.

## 6. Visualizador — duas vistas (normativo)

### 6.1 Vista Protocolar
- Mostra o **envelope canónico completo**.
- Permite **copiar** (export) e **colar + Aplicar** (import).
- Ao aplicar: validar (§7) e substituir o estado da tabela. É a **única** vista que importa/edita.
- DEVE garantir round-trip lossless (I2).

### 6.2 Vista Humano
- Projecção **derivada** do envelope, gerada on-the-fly.
- **Read-only** e **só export**. NÃO DEVE permitir import nem edição.
- Quando agrupada, o valor de cada grupo aparece **uma só vez** (no cabeçalho do grupo) e NÃO DEVE ser repetido nas entradas (sem a redundância do agrupamento ingénuo). A reconstrução para o envelope (caso exportada e reimportada noutro fluxo) reata o valor a partir do cabeçalho.
- O formato de render/export humano PODE ser agrupado-legível (outline/tabela), MD, ou Excel; a regra de **não-redundância** é normativa em qualquer um.
- Características de destino (`x-notion`/`x-excel`) DEVERIAM ser visíveis/editáveis no artefacto humano (ex.: front matter YAML em MD, folha de propriedades em Excel) para não se perderem no round-trip.

## 7. Validação

Ao aplicar (import) ou exportar, a app DEVERIA validar:
- **Completude de `data`** — todas as chaves de `schema.fields` presentes em todas as linhas (em falta → `""`).
- **Tipos** — valores compatíveis com `schema.fields[].type`.
- **Categories** — valores fora de `categories` sinalizados (não necessariamente rejeitados).
- **`primaryKey`** — unicidade. **Aviso:** em datasets actuais a unicidade pode falhar (ex.: o mesmo `ID` repete-se por empresa com várias especialidades). Se `primaryKey` único for requisito, usar chave **composta** (ex.: `["ID","ID Especialidade"]`) ou não declarar `primaryKey`. A app DEVE avisar em duplicados, não corromper silenciosamente.

## 8. Versionamento da spec

- Esta spec tem uma versão. **spec-version 2** = adenda §0.1 (classes A/B/C, canais, `type` fora do schema, I2 do par, storage `.tableeditor/`). O envelope regista a versão sob `x-tableeditor.specVersion`.
- Alterações que preservem I1–I3 e sejam aditivas = minor. Alterações aos invariantes ou ao mapeamento = major, e exigem rota de migração documentada.
- O código DEVE referenciar a versão da spec contra a qual foi escrito.

## 9. Canais de saída (export / mirror) — composição à la carte

O **envelope canónico** (§2) governa **autosave + import** (classe A, lossless). O que **sai** para consumidores (export/mirror) é uma **composição por canal**, config de máquina (classe B), guardada em `<id>.config.json` sob `channels.{export,mirror}`:

```json
{ "parts": { "schema": true, "types": false, "view": false },
  "destino": "",
  "cols": { "<coluna>": { "type": "", "fixed": "", "hidden": "", "width": "", "color": "" } } }
```

Regras:
- **`parts.schema`** — inclui `schema.fields` (nomes + ordem). **`parts.types`** — junta `type`/`fixed`/`hidden` por coluna a partir de `cols` ("" = não comprometer; omite a chave). **`parts.view`** — junta `view` (`groupBy` + `sortHierarchy`) declarativo.
- **`destino`** — bloco `x-<destino>` opcional. `x-excel` (`buildXDestino`): `format`/`hidden`/`width`/`color`/`frozen` (congelar 1ª coluna) por coluna. Outros destinos = passthrough genérico (sem lista fechada). Mapeamento sugerido por sinais: §5.3.
- **Sem `schema`/`view`/`destino`** = só **dados crus** (array nu).
- **`data` é SEMPRE plano** (I3) — agrupar declara-se em `view`, nunca na estrutura. **NUNCA** sai `x-tableeditor` (classe C).
- `hidden` de **output** é por canal (`cols[col].hidden==='sim'` exclui a coluna do canal) — separado do `hidden` da **grelha do editor** (classe A).
- `categories` (classe A) vem do custom-sort (`colSort.order`), emitido em `schema.fields[].categories` quando há schema.
- O mirror é **pré-composto** pelo cliente (`composeChannel`) e gravado **verbatim** pelo servidor (`mirrorIsEnvelope:true` salta `add_num`/`strip_num`).
