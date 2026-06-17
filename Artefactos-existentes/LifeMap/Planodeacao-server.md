# Plano de Ação — SERVER (persistência + pastas)

> Roadmap das alterações de **servidor/persistência** (Fase 2).
> Para melhorias da **app/front-end**, ver [`Planodeacao-app.md`](Planodeacao-app.md).
> Registo de **como** cada alteração foi feita: [`log-alteracoes.md`](log-alteracoes.md) (append-only).

---

## Protocolo de marcação
Igual ao `Planodeacao-app.md`: `[ ]`/`[~]`/`[x]`/`[!]`; preencher `Branch`/`Commit` ao concluir;
`✅ ACEITE` ou `⏳ PENDENTE DE ACEITAÇÃO`; **ordem global partilhada** com o plano da app;
fazer **append** em `log-alteracoes.md` a cada conclusão.

> **🔄 Nota de reordenação (S3, 2026-06-08):** toda a **Fase 2 (servidor)** foi adiada para **depois** da
> Fase 1 (front-end). A antiga regra "persistência (ordem 4) antes das Classes" foi dissolvida — o objetivo
> atual é ver a app a funcionar em memória. Nova ordem: **S1+S2+S3+S7 = ordem 8**, **S4+S8 = 9**,
> **S5 = 10**, **S6 = 11**. O esquema `.json` (S3) mantém-se definido — sem retrabalho.

## Princípio fundador (decidido com o utilizador)
- **Servidor é OPCIONAL.** App faz `ping` ao arrancar:
  - **online** → modo persistente (lê/grava disco);
  - **offline** → **alerta** ("a trabalhar só em memória, perde-se ao fechar") **mas continua a funcionar**
    em memória do browser. Nunca bloqueia.
- Stack do servidor: **Python stdlib puro** (sem pip), à imagem da `TableEditorApp/` (referência de estudo).
  Lançador `.bat`. Não expor à rede (localhost).

## Dependências cruzadas (server ↔ app)
- O server **serializa** o modelo de dados definido pela app (Grupos D–G do `Planodeacao-app.md`):
  classes, grupos, ícones por nó, versões. **Não congelar o formato `.json` sem alinhar com a app.**
- Reconciliação `.md`↔`.json` usa `nome+nivel+pai` que a **app** escreve em cada nó.

---

# GRUPO S1 — Persistência base (servidor + fallback memória)

| Campo | Valor |
|---|---|
| **Ordem** | 8 _(depois de toda a Fase 1 front-end)_ |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] Servidor Python mínimo (localhost): `/ping`, `/load`, `/save`, `/list`.
- [ ] **Contrato espelha `TableEditorApp/acc_server.py`** _(decisão da ronda)_: Python stdlib puro
      (sem pip), porta fixa em localhost (à imagem da TableEditorApp), endpoints REST simples (GET/POST
      com JSON), respostas `{ok:bool, ...}`. Usar `acc_server.py` como referência canónica de estilo/erros.
- [ ] Lançador `.bat`.
- [ ] App: `pingServer()` no arranque + **savebar** de estado (● online / offline).
- [ ] **Fallback gracioso**: offline → alerta + modo memória (estado atual já é em memória).
- [ ] Restauro no arranque: lê índice `MapLab.json` (ver S2).

---

# GRUPO S2 — Índice do workspace (`MapLab.json`)

| Campo | Valor |
|---|---|
| **Ordem** | 8 (com S1) |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] **`MapLab.json`** **SEMPRE na raiz, na pasta do HTML** _(decisão da ronda)_. Formato JSON.
- [ ] **Caminhos HÍBRIDOS (portabilidade)** _(decisão da ronda)_:
  - Árvores guardadas em `Projetos/` (pasta da app; pode ter subpasta por projeto) → referidas por
    **caminho RELATIVO** à pasta do HTML (ex.: `Projetos/<proj>/Arvore X.md`).
  - **`lastKnownPath`**: o índice grava o caminho absoluto da pasta da app **da última execução** — usado
    só para o servidor detetar se a app foi movida (ver S7). NÃO é usado para resolver as árvores.
  - **Mirror**: caminho **ABSOLUTO** (pasta externa à escolha) — ver S8.
- [ ] Conteúdo: lista de **projetos → árvores** com `{id,name,color,tabIcon, file(relativo), mirror?:{path(abs),
      includeJson:bool}}` **+ biblioteca de Classes Sistema e Grupos Sistema** (zona estanque) **+ `lastKnownPath`**.
- [ ] **`.py` do servidor NÃO contém paths** (nem da app nem do mirror) _(decisão da ronda)_: o servidor
      **lê tudo do `MapLab.json`**. O `.py` é genérico/portável; só conhece o seu próprio diretório (para S7).
- [ ] **Autosave** do índice (debounce, a cada alteração estrutural).
- [ ] Arranque: se `MapLab.json` **não existir** → **app vazia** → cria novo ao primeiro Save.
- [ ] Nota: o índice guarda **só a lista** + caminhos + classes sistema + `lastKnownPath`. A **estrutura
      real** de cada árvore vive no `.md`/`.json` da árvore (ver S3).

---

# GRUPO S3 — Save por árvore: `.md` limpo + `.json` completo

| Campo | Valor |
|---|---|
| **Ordem** | 8 (com S1/S2) |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] Definir, por árvore, um **ficheiro de destino** (ex.: `Arvore X.md`).
- [ ] **Save** gera DOIS ficheiros:
  - **`Arvore X.md`** — limpo, **só hierarquia** (formato canónico atual; com/sem numeração conforme o
    toggle do Grupo H — ver formato em `referencias/instrucoesMapa.md`).
  - **`Arvore X.json`** — completo (ver ESQUEMA abaixo).

### Esquema COMPLETO do `.json` por árvore _(definido já agora — decisão da ronda)_
> A persistência base (Ordem 8) grava ESTE formato. Como o front-end (Grupos D/E/F/H) é feito **primeiro**
> em memória, quando a persistência chegar o modelo de dados já está estabilizado — basta serializá-lo para
> este esquema. Não há retrabalho.
```jsonc
{
  "tree": "Arvore X",
  "savedAt": "<iso>",
  "view": { "iconsVisible": true, "colorsVisible": true, "classMode": "primaria|primaria+secundaria",
            "iconSource": "class|group", "numeracaoVisible": false },   // preferências POR ÁRVORE (Grupo D/H)
  "localLib": { "groups": [ {"id","name","icon","color"} ],
                "classes": [ {"id","name","groupId","icon","color"} ] }, // Classes/Grupos LOCAIS
  "nodes": [
    {
      "nome": "Saúde",
      "nivel": 2,
      "pai": "FAMÍLIA",            // nome do pai (a identidade é única por design — ver reconciliação)
      "numeracao": "2.2.2.2",      // SEMPRE gravado; identifica o nó sem ambiguidade (Grupo H)
      "icon": "apple",             // slug custom OU vazio
      "iconCustom": true,          // se o ícone é override custom (não vem da classe/grupo)
      "classePrimaria": "<classId|null>",
      "classeSecundaria": "<classId|null>",
      "classeTipo": "sistema|local" // de onde vêm as classes referenciadas
    }
  ]
}
```
- [ ] **Reconciliação SEM ambiguidade** _(decisão da ronda)_: é PROIBIDO dois nós-irmãos com o mesmo nome
      sob o mesmo pai/nível (regra de integridade na app). Logo a chave **`nome + nivel + pai`** (reforçada
      por `numeracao`) é única. Se o `.md` for editado por fora, ao abrir a app lê o `.json` e **reatribui
      ícone/classe por essa chave**. Nó cuja chave já não existe no `.md` → metadado descartado
      silenciosamente. (Colisão deixou de ser possível por design — ver Grupo H.)
- [ ] Após import de `.md` alterado + Save → **`.json` é atualizado** com a nova estrutura (recalcula `numeracao`).

---

# GRUPO S4 — Versões em ficheiros (estrutura + classe)

| Campo | Valor |
|---|---|
| **Ordem** | 9 (dá durabilidade ao Grupo F, que já funciona em memória) |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] Versões de **estrutura**: `Arvore X-v1.md` + `Arvore X-v1.json`, `Arvore X-v2.md` + `.json`…
      `Arvore X.md`/`.json` = estado atual. _(esquema confirmado na ronda)_
- [ ] Versões de **classe** (sub-versões): partilham o `.md` da versão de estrutura e variam só o JSON:
      `Arvore X-v1a.json`, `Arvore X-v1b.json` (sub-versões de v1). _(esquema confirmado na ronda)_

---

# GRUPO S5 — Mapear Pasta (disco → árvore)

| Campo | Valor |
|---|---|
| **Ordem** | 10 |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] Botão **"Mapear Pasta"**: servidor faz `walk` de uma pasta → devolve árvore → app cria os nós.
- [ ] **Referência canónica: `referencias/instrucoesMapa.md`** (especificação madura, já pensada para este
      projeto). Implementar o que lá está e ainda não temos. _(decisão da ronda)_
- [ ] **Inclui ficheiros** (além de pastas) — ficheiros distinguem-se com prefixo `_ ` no `.md` (pastas `- `),
      agrupados por tipo, hidden primeiro, "não expandido" `⟨...⟩`, exclusões de pastas. (Ver instrucoesMapa.md.)
- [ ] Configuração ao mapear: profundidade (níveis ou "todos"); excluir pastas; incluir/excluir ocultos;
      incluir ficheiros (todos / allowlist `.ext` / blocklist `.ext`).
- [ ] **Vista/filtros na app → Grupo I do `Planodeacao-app.md`** (toggle ficheiros; filtro por ext/nome/pasta;
      2 modos: expandir-o-necessário vs esconder-ramos-irrelevantes). **A debater em detalhe antes de implementar.**

---

# GRUPO S6 — Criar pastas a partir de path (árvore → disco)

| Campo | Valor |
|---|---|
| **Ordem** | 11 |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

- [ ] Botão **"Criar Árvore a partir de path"**: dás um path → servidor cria toda a hierarquia de pastas.
- [ ] **Preview + confirmação SEMPRE** antes de escrever ("vou criar estas N pastas em X — confirmas?"). _(decisão da ronda)_
- [ ] **Colisões: saltar** as pastas que já existem (não sobrescrever). _(decisão da ronda)_
- [ ] **Sanitizar** nomes de nó inválidos para o sistema de ficheiros (`\ / : * ? " < > |`). _(decisão da ronda)_
- [ ] Tratamento de erros de permissão.

---

# GRUPO S7 — Portabilidade / re-base da app (mover a pasta)

| Campo | Valor |
|---|---|
| **Ordem** | 8 (com a persistência base — fundacional na Fase 2) |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

**Conceito (decisão da ronda).** Posso mover a **pasta da app inteira** (HTML + `Projetos/` + `MapLab.json`)
para qualquer sítio e tudo continua a funcionar.
- [ ] **Deteção via servidor**: ao arrancar, o servidor sabe o seu próprio diretório; compara-o com
      `lastKnownPath` do `MapLab.json`. Se diferir → a app **pede confirmação da nova localização** e
      **atualiza `lastKnownPath`** + quaisquer paths que precisem (os das árvores são relativos, logo não
      mudam; só o `lastKnownPath` e, se aplicável, referências absolutas).
- [ ] Como os caminhos das árvores são **relativos** (S2), mover a pasta normalmente **não exige re-escrever
      nada** além do `lastKnownPath` — a deteção serve de confirmação/segurança.
- [ ] **Botão "Mudar path de árvores"** na app: aponta deliberadamente a base das árvores para outra pasta
      (ex.: subpasta diferente). Opção de **mover os ficheiros** existentes para a nova base (via servidor).
- [ ] Sem servidor: a app não consegue detetar o caminho real (file://) → cai para modo memória e avisa.

---

# GRUPO S8 — Mirror por versão (dupla gravação + sync)

| Campo | Valor |
|---|---|
| **Ordem** | 9 (com S4 versões) |
| **Branch** | _(a definir)_ |
| **Commit** | _(a definir)_ |
| **Estado** | `[ ]` por fazer |

**Conceito (decisão da ronda).** Cada árvore grava em **DOIS sítios**: `Projetos/` (na app) **e** um
**mirror** numa pasta externa à escolha (caminho **absoluto**, não se auto-corrige ao mover a app).
- [ ] Por árvore, configurar mirror: **path absoluto** + se inclui **só `.md`** ou **`.md`+`.json`**.
- [ ] **Save afeta os dois** (Projetos/ + mirror).
- [ ] **Mirror é POR VERSÃO**, com **nomenclatura fixa**: `MapaXxx-V1.md`, `MapaXxx-V2.md`, … (e `.json` se incluído).
- [ ] **Botão "Atualizar do mirror"**: lê o ficheiro de mirror **da versão atualmente aberta**, **pergunta
      "sobrepor?"**, e ao confirmar atualiza a árvore na app **e** o save em `Projetos/`.
- [ ] **Botão "Nova versão de mirror"**: procura no path do mirror a **V seguinte** na sequência e cria-a lá.
- [ ] A nomenclatura `-Vx` consistente é o que permite à app saber que versões existem no mirror.

---

## Faseamento sugerido — REORDENADO (S3: Fase 2 depois da Fase 1 front-end)
Toda a **Fase 1 (front-end, em memória)** primeiro (D,H,E,F,G). Só depois a Fase 2:
8 (S1+S2+S3 persistência base **+ S7 portabilidade** — fundacional da Fase 2) → 9 (S4 versões **+ S8 mirror**,
dá durabilidade ao Grupo F) → 10 (S5 mapear) → 11 (S6 criar).
A antiga dependência "persistência antes das Classes" foi **dissolvida**: as classes funcionam em memória;
a persistência grava-as quando chegar (esquema `.json` já definido em S3 — sem retrabalho).
