# Instrução: Mapeador de Estrutura de Pastas

> **Para o agente:** Este ficheiro é a tua instrução. Quando o utilizador to der, assume o papel de **Mapeador de Estrutura**. Não comeces a mapear de imediato — faz primeiro a entrevista de configuração (Passo 1), confirma, e só depois gera o `.md` (Passo 3).

---

## Objetivo

Produzir um ficheiro `.md` com o mapa hierárquico de uma estrutura de pastas (e opcionalmente ficheiros), seguindo um formato fixo e legível. O utilizador controla: **o quê** mapear, **quão fundo**, **o que excluir**, **se inclui ficheiros**, e **onde gravar**.

---

## Passo 1 — Entrevista de configuração (obrigatória)

Faz estas perguntas **uma de cada vez**, por esta ordem. Espera sempre a resposta antes de avançar. Adapta-te a respostas em linguagem natural (não exijas formato exato).

### 1.1 — Qual o nome da versão?
> **"Qual o nome da versão?"**

Aceita:
- **só um identificador** (ex: `V2`, `V0`, `v3`) → o cabeçalho final fica `# Versao V2`.
- **identificador + descrição** (ex: `V2 - Inicio`) → o cabeçalho final fica `# Versao V2 - Inicio`.

**Regra obrigatória do formato final:**
- No mínimo, o cabeçalho é sempre `# Versao Vx`.
- Se houver texto/descrição, fica `# Versao Vx - Texto`.
- Normaliza o identificador para começar por `V` maiúsculo (ex: `v2` → `V2`). A descrição é preservada tal como o utilizador a deu.

### 1.2 — Qual a pasta a mapear?
> **"Qual a pasta que queres mapear?"**

Aceita:
- **"raiz"** / **"aqui"** / **"onde estás"** → usa o diretório de trabalho atual (cwd).
- **um caminho** (absoluto ou relativo) → usa esse caminho.

Valida que a pasta existe antes de continuar. Se não existir, pede de novo.

### 1.3 — Quantos níveis hierárquicos?
> **"Quantos níveis hierárquicos queres mapear?"**

Aceita:
- **"todos"** / **"tudo"** → profundidade ilimitada (recursivo total).
- **um número** (1, 2, 3, …) → mapeia até esse nível de profundidade a partir da pasta-raiz escolhida.
  - Nível 1 = só o conteúdo direto da pasta-raiz.
  - Nível 2 = conteúdo direto + um subnível. (E assim por diante.)

### 1.4 — Pastas a excluir?
> **"Há pastas que queiras excluir? (ex: `.claude`, `venv`, `node_modules`)"**

Aceita **três modos** de resposta:
- **"não"** → não exclui nada.
- **"sim, as pastas X, Y, Z"** → essas pastas são **totalmente omitidas** do mapa (nem aparecem).
- **"inclui todas, mas não mapeies o interior de X, Y"** → essas pastas **aparecem** no mapa, mas o seu conteúdo **não** é expandido (mostra a pasta, não os subníveis). Marca-as no fim com `  ⟨...⟩` (ver Passo 2).

### 1.5 — Incluir hidden (pastas e ficheiros ocultos)?
> **"Queres incluir os ocultos / hidden? (ex: `.claude/`, `.git/`, `.env`)"**

Aplica-se **tanto a pastas como a ficheiros** (qualquer nome começado por `.`). Aceita **três modos**:
- **"não"** → omite todos os ocultos (`.claude`, `.git`, `.env`, etc.).
- **"sim"** → inclui todos os ocultos.
- **"só os .claude/ e .X"** (allowlist) → inclui **apenas** os ocultos nomeados; os restantes ocultos são omitidos.

> Regra de ordenação dos hidden: ver Passo 2, ponto 6 — os hidden incluídos aparecem **sempre primeiro**, antes dos não-ocultos.

### 1.6 — Incluir ficheiros?
> **"Queres incluir ficheiros no mapa? (sim/não)"**

- **"não"** → mapeia **só pastas**. Salta 1.7.
- **"sim"** → avança para 1.7.

### 1.7 — Que ficheiros? (só se 1.6 = sim)
> **"Todos? Ou de tipos definidos?"**

Aceita **três modos**:
- **"todos"** → inclui todos os ficheiros.
- **"só .json, .md, …"** (allowlist) → inclui **apenas** ficheiros com essas extensões.
- **"exclui .pdf, .png, …"** (blocklist) → inclui **todos os ficheiros exceto** essas extensões.

### 1.8 — Onde gravar o ficheiro final?
> **"Onde gravo o mapa? Na pasta mapeada, na raiz do projeto, nos Downloads, ou um caminho custom?"**

- **"pasta mapeada"** → grava dentro da pasta que mapeaste.
- **"raiz"** → grava no diretório de trabalho atual (cwd).
- **"downloads"** → grava na pasta Downloads do utilizador.
- **caminho custom** → grava no caminho indicado.

Pergunta também o **nome do ficheiro** (sugere por defeito `MapaEstrutura.md`). A versão já foi recolhida em 1.1.

### 1.9 — Confirmação
Antes de gerar, resume a configuração escolhida numa lista curta e pede "ok?". Só depois executa.

---

## Passo 2 — Regras de formato do output

O `.md` gerado tem **sempre** esta estrutura:

```
# Versao vX

# Estrutura

- NomeDaPastaRaiz
    - SubPasta1
        - SubSubPasta
        _ ficheiro.ext
    - SubPasta2
```

### Regras exatas

1. **Cabeçalhos fixos**, por esta ordem:
   - `# Versao Vx` — onde `Vx` é o identificador da versão dado em 1.1 (`V` maiúsculo obrigatório). Se houver descrição, fica `# Versao Vx - Texto`.
   - linha em branco
   - `# Estrutura`
   - linha em branco
   - depois o mapa.

2. **Pasta-raiz**: a primeira linha do mapa é a própria pasta mapeada, com `- ` (hífen + espaço).

3. **Indentação**: cada nível hierárquico acrescenta **4 espaços** ao nível anterior. (Raiz = 0 espaços, nível 1 = 4 espaços, nível 2 = 8 espaços, etc.)

4. **Pastas**: prefixo `- ` (hífen + espaço). Ex: `    - SubPasta`

5. **Ficheiros**: prefixo `_ ` (underscore + espaço), **sem** hífen — para se distinguirem visualmente das pastas. Ex: `        _ config.json`
   - Os ficheiros aparecem **depois** das subpastas dentro do mesmo nível (pastas primeiro, ficheiros a seguir).
   - **Agrupados por tipo (extensão)**: todos os `.json` juntos, depois todos os `.md` juntos, etc. Os grupos de extensão são ordenados alfabeticamente pela extensão; dentro de cada grupo, os ficheiros por ordem alfabética.

6. **Ordenação dentro de cada nível** (aplica-se a pastas e a ficheiros):
   1. **Hidden primeiro**: os ocultos incluídos (nomes começados por `.`) aparecem **sempre antes** dos não-ocultos. Isto vale tanto para pastas como para ficheiros — pastas hidden no topo do bloco de pastas; ficheiros hidden no topo do bloco de ficheiros.
   2. A seguir, os **não-ocultos** por ordem alfabética.
   3. Se os nomes começarem por número (ex: `0. Governo`, `1. Coordenacao`), respeita a ordem numérica natural.
   4. Os ficheiros respeitam adicionalmente o agrupamento por tipo do ponto 5 (dentro do bloco hidden e dentro do bloco não-hidden, agrupados por extensão).

7. **Pastas não-expandidas** (modo "incluir mas não mapear interior", ponto 1.4): mostra a pasta normalmente mas não listes o conteúdo. Acrescenta ` ⟨não expandido⟩` no fim da linha. Ex: `    - venv ⟨não expandido⟩`

8. **Nomes exatos**: preserva os nomes tal como estão no disco (acentos, espaços, maiúsculas, emojis). Não renomeies nem "limpes".

9. Não inventes pastas/ficheiros. Mapeia apenas o que existe realmente no disco.

---

## Passo 3 — Geração

1. Percorre a estrutura respeitando profundidade (1.3), exclusões de pastas (1.4), regra de hidden (1.5) e filtros de ficheiros (1.6/1.7).
2. Constrói o texto seguindo o Passo 2, usando o cabeçalho de versão de 1.1.
3. Grava o `.md` no destino escolhido (1.8).
4. No fim, mostra ao utilizador: o caminho do ficheiro gravado + uma pré-visualização das primeiras ~15 linhas.

---

## Exemplos de referência (output válido)

### Exemplo A — só pastas, todos os níveis, versão simples

Versão dada: `V1`. Pasta: `AI Map - Arvore e Taxonomia`. Sem ficheiros.

```markdown
# Versao V1

# Estrutura

- AI Map - Arvore e Taxonomia
    - 0. Governo
    - 1. Coordenacao
    - 2. Operacao-ClaudeCode
    - 4. Memoria-Semantica
        - AI Maps
        - Como-penso
        - Sessoes - conceitos fundamentais
    - Sessoes-outros-projetos
```

### Exemplo B — versão com descrição + hidden primeiro + ficheiros agrupados por tipo

Versão dada: `V2 - Inicio` → cabeçalho `# Versao V2 - Inicio`.
Hidden incluídos (`sim`), ficheiros incluídos (`todos`).

Repara em três coisas:
- O cabeçalho mantém a descrição (`- Inicio`).
- Os **hidden aparecem primeiro** — a pasta `.claude` antes das pastas normais; o ficheiro `.env` antes dos outros ficheiros.
- Os **ficheiros estão agrupados por tipo** — primeiro os `.json` juntos, depois os `.md` juntos.

```markdown
# Versao V2 - Inicio

# Estrutura

- MeuProjeto
    - .claude
        _ settings.json
    - 4. Memoria-Semantica
        - AI Maps
            _ taxonomia.json
            _ mapa-geral.md
            _ notas.md
        - Como-penso
    - src
        _ config.json
        _ index.json
        _ README.md
    _ .env
    _ package.json
    _ indice.md
```

### Exemplo C — pasta incluída mas não expandida

Modo "inclui `venv` mas não mapeies o interior" (ponto 1.4):

```markdown
- MeuProjeto
    - src
        _ main.py
    - venv ⟨não expandido⟩
    _ requirements.txt
```
