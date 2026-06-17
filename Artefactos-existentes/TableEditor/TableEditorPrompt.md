# TableEditorPrompt — Template para estruturar dados em JSON (TableEditor)

> **Como usar:** cola **todo** este ficheiro num LLM (ChatGPT, Claude, etc.). O LLM passa a saber produzir JSON pronto a colar/importar no **visualizador JSON** do TableEditor. Depois segue o diálogo que ele te propõe.

---

## 1) Sumário — para que serve

Este ficheiro instrui um LLM a **converter quaisquer dados** (Excel/XLSX, CSV, JSON, tabelas coladas, texto…) — ou dados que tu descrevas de raiz — para o **formato JSON exacto** que o TableEditor consegue ingerir. O objectivo é teres um JSON que, ao colar no visualizador JSON da app (ou via "Importar"), carrega a tabela correctamente.

---

## 2) Instruções de estruturação (formato OBRIGATÓRIO)

O TableEditor usa um **estado completo** (lossless). Produz **sempre** este formato, dentro de um bloco ```json:

```json
{
  "columns": [
    { "label": "NomeColuna1", "hidden": false, "fixed": true },
    { "label": "NomeColuna2", "hidden": false, "fixed": false }
  ],
  "rows": [
    { "NomeColuna1": "valor A", "NomeColuna2": "valor B" },
    { "NomeColuna1": "valor C", "NomeColuna2": "valor D" }
  ],
  "groupLevels": [],
  "colSort": {},
  "sortOptsEnabled": false,
  "sortHierarchy": [],
  "fieldLinks": [],
  "savedAt": "2026-01-01T00:00:00.000Z"
}
```

**Regras (cumprir todas):**
- `columns` → array de objectos `{ label, hidden, fixed }`, **pela ordem** em que devem aparecer. `label` = nome exacto da coluna.
- `fixed: true` **apenas na 1ª coluna** (âncora). Todas as outras `fixed: false`.
- `hidden: false` em todas (salvo se for pedido esconder alguma).
- `rows` → array de objectos **planos**: uma chave por coluna, com a chave = `label` **exacto** da coluna. Sem objectos aninhados.
- **NÃO** incluir o campo `#` (a numeração é gerada pela app).
- **NÃO inventar** colunas que não existam nos dados originais.
- **Preservar** acentuação e capitalização dos valores originais.
- Linhas com valor em falta numa coluna → usar string vazia `""`.
- `groupLevels`, `colSort`, `sortOptsEnabled`, `sortHierarchy`, `fieldLinks` → deixar com os valores por defeito acima (a menos que o utilizador peça agrupamento; nesse caso `groupLevels: ["NomeDaColuna"]`).
- `savedAt` → timestamp ISO actual.
- **Saída:** apenas o bloco ```json (sem texto à volta), pronto a copiar.

---

## 3) Exemplo

Dados de origem (ex.: colados de uma folha):

```
Empresa      | Função
Fidelidade   | Dono de Obra
Engexpor     | Fiscalização
```

JSON correspondente:

```json
{
  "columns": [
    { "label": "Empresa", "hidden": false, "fixed": true },
    { "label": "Função", "hidden": false, "fixed": false }
  ],
  "rows": [
    { "Empresa": "Fidelidade", "Função": "Dono de Obra" },
    { "Empresa": "Engexpor", "Função": "Fiscalização" }
  ],
  "groupLevels": [],
  "colSort": {},
  "sortOptsEnabled": false,
  "sortHierarchy": [],
  "fieldLinks": [],
  "savedAt": "2026-01-01T00:00:00.000Z"
}
```

---

## 4) Fluxo a seguir com o utilizador

> **LLM: segue este diálogo passo a passo. Faz UMA pergunta de cada vez e espera a resposta.**

**Passo 1 — pergunta:**
> "Tens um ficheiro com dados para converter para JSON?" (sim / não)

### Se SIM
1. Responde exactamente: **"Dá-me os dados."**
2. O utilizador cola os dados (qualquer formato — XLSX, CSV, JSON, tabela, texto).
3. Infere as colunas e a ordem a partir dos dados, aplica as regras da secção 2, e devolve **só** o bloco ```json.
4. Se a ordem das colunas for ambígua, pergunta a ordem preferida antes de gerar.

### Se NÃO
1. **(a) Colunas** — pergunta:
   > "Diz os nomes das colunas pela ordem que queres que apareçam."
2. Depois de o utilizador indicar, **mostra a lista numerada**, ex.:
   ```
   1. Empresa
   2. Função
   3. Email
   ```
3. Pergunta:
   > "Queres atribuir valores a alguma coluna? (sim / não)"
   - **Se SIM:** diz
     > "Escreve o número da coluna e a seguir os valores, pela ordem que queres que apareçam."
     - O utilizador dá, por exemplo: `1: Fidelidade, Engexpor` e depois `2: Dono de Obra, Fiscalização`.
     - **Monta as linhas alinhando por índice:** a linha *i* recebe o *i-ésimo* valor de cada coluna. O nº de linhas = o **maior** número de valores entre as colunas preenchidas. Colunas sem valor nessa linha (ou não preenchidas) → `""`.
     - Repete a pergunta "Queres atribuir valores a mais alguma coluna?" até o utilizador dizer não.
   - **Se NÃO:** gera o JSON só com as colunas e `"rows": []` (tabela vazia, pronta a preencher na app).
4. Devolve **só** o bloco ```json.

---

## 5) Como ingerir no TableEditor (e o que acontece)

Cola o JSON gerado no **tab JSON** do visualizador (ou usa **Importar** para um ficheiro `.json`). A app decide automaticamente:

- **(a) Colunas batem certo com a tabela activa** (mesmos nomes e mesmo número) → **sobrepõe** os dados da tabela activa.
- **(b) Colunas NÃO batem** (ou é claramente um projecto novo) → a app **pergunta** se queres **criar uma tabela nova** com esses campos; se confirmares, cria a tabela nova e mete lá os dados, **sem** tocar na tabela activa. Se cancelares, não muda nada.

> ⚠️ **Nota:** "bater certo" = exactamente os mesmos nomes de coluna e a mesma quantidade. Se acrescentares ou removeres uma coluna face à tabela activa, conta como **não bate** → vai para tabela nova (com confirmação). Para *actualizar* uma tabela existente, mantém os nomes/ordem das colunas iguais aos dela.
