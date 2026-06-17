# Prompt — Adoptar Frictionless Table Schema no TableEditor

## Objectivo

Migrar o modelo de dados canónico da app **TableEditor** para o envelope **Frictionless Table Schema / Data Package**, de forma **escalável**: a app deve filtrar todas as operações de dados (autosave, mirror, import, export e o visualizador) por um único modelo canónico, e o código deve registar que esse formato é a fonte de verdade, apontando para a spec que o define. Quando, mais tarde, um agente acrescentar funcionalidades (ex.: menu de propriedades de coluna, export para Excel ou Notion), deve saber exactamente onde encaixar sem partir o formato.

Não escrevas a app por mim aqui — esta é a ordem de trabalho. A fonte normativa do formato é o ficheiro **`SPEC-TableEditor-Formato-Dados.md`** (entregue em conjunto): consulta-o e implementa contra ele.

## Pressupostos (confirmar antes de implementar)

- **P1** — O formato canónico **interno** da app passa a ser o envelope Frictionless (`data` / `schema` / `view` / `x-*`). Governa autosave, mirror, import e export — não é apenas um formato de export.
- **P2** — Estado de UI/vista sem equivalente Frictionless (`colSort`, `sortOptsEnabled`, toggles do editor) vive sob `x-tableeditor`, **nunca** em `data`.
- **P3** — O visualizador tem duas vistas: **Protocolar** (envelope canónico, editável/colável) e **Humano** (derivada, read-only, export-only, agrupada sem redundância).
- **P4** — A SPEC é commitada no repo; o código mantém um ponteiro para ela na fronteira de (de)serialização.
- **P5** — Retrocompatibilidade: a app continua a importar o formato legado (`columns`/`rows`/`groupLevels`/...), auto-migrando-o para o envelope na importação.

## O que implementar agora

1. **Modelo canónico único.** Substituir o estado actual (`columns`/`rows`/`groupLevels`/`colSort`/`sortOptsEnabled`/`sortHierarchy`/`fieldLinks`/`savedAt`) pelo envelope Frictionless, segundo o mapeamento da §4 da SPEC. Toda a (de)serialização — autosave, mirror, import, export — passa por uma única camada que lê/escreve o envelope.

2. **Migração e retrocompatibilidade.** Na importação, detectar o formato legado e auto-migrá-lo para o envelope (mapeamento da SPEC). Nunca perder dados nem estado de vista existente: o que não tiver casa Frictionless vai para `x-tableeditor`.

3. **Visualizador JSON com duas vistas** (§6 da SPEC):
   - **Vista Protocolar** — mostra o envelope canónico completo. Permite **copiar** (export) e **colar + "Aplicar"** (import): ao aplicar, valida e substitui o estado da tabela. É a única vista que importa.
   - **Vista Humano** — render **read-only**, **só export**. Sem import, sem edição. Quando agrupada, o valor do grupo aparece **uma vez** (no cabeçalho do grupo) e **não** é repetido em cada entrada. É uma projecção derivada do envelope, gerada on-the-fly.

4. **Escalabilidade (registo no código).** Implementar os pontos de extensão da §5 da SPEC e deixar, na camada de serialização, um comentário/constante que aponte para a SPEC e enuncie as regras invioláveis (I1: `data` nunca depende de metadados; I2: round-trip lossless). Qualquer funcionalidade futura (propriedade de coluna, novo destino de export, nova opção de vista) deve ser **aditiva** segundo o protocolo de extensão — sem tocar em `data`, sem codificar dados em chaves.

## Definition of Done

- Autosave, mirror, import e export produzem/consomem o mesmo envelope canónico.
- Importar um ficheiro legado reconstrói o estado sem perdas.
- Exportar e voltar a importar (Protocolar) devolve estado idêntico (round-trip lossless).
- Vista Humano agrupada não repete valores de grupo nas entradas; não permite import/edição.
- Existe no código um ponteiro explícito para a SPEC na fronteira de serialização.
- Adicionar uma propriedade de coluna ou um bloco `x-<destino>` não requer alterar a lógica de `data`.

## Não fazer

- Não codificar dados em chaves de objecto (sem estruturas aninhadas em `data`).
- Não tornar a leitura dos dados dependente de `schema`/`view`/`x-`.
- Não apagar campos de agrupamento das entradas em `data`.
- Não inventar campos fora do que a SPEC define; extensões só sob `x-`.

## Referência

`SPEC-TableEditor-Formato-Dados.md` — fonte canónica do formato. Consultar sempre que se tocar em serialização, import/export, autosave, mirror ou no visualizador.
