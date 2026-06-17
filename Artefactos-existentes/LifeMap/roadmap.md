# roadmap.md — rumo do projeto MapLab

Define os marcos e o rumo. No arranque de cada sessão, o Claude confere se `handoff.md` e
`context.md` estão **alinhados** com este roadmap e **assinala discrepâncias** ao utilizador
(ver `CLAUDE.md` → Arranque).

> **Estado do roadmap (atualizado na branch `App-Generica`):** o **roadmap da app foi REABERTO**.
> A app deixou de estar "estável em v12 sem features no horizonte" — está em transformação profunda:
> de editor de mapas fixos → **MapLab**, editor genérico de taxonomias com classes e persistência.
> O detalhe executável (passos, branch/commit, ordem) vive em **`Planodeacao-app.md`** e
> **`Planodeacao-server.md`**; o **como** de cada alteração em **`log-alteracoes.md`** (append-only);
> os snapshots em **`Arqueologia Alteracoes/`**. Este roadmap é a **visão** que une tudo.

> **🔄 REORDENAÇÃO (2026-06-08, S3) — FRONT-END PRIMEIRO.** Decisão do utilizador: o objetivo imediato é
> **ver a app a funcionar** com as features novas, **em memória** (as classes/versões NÃO precisam de ficar
> gravadas para já). Isto **dissolve** a antiga regra "persistência (4) antes das Classes (5)" — essa
> dependência só existia para gravar. **Nova ordem global:** toda a **Fase 1 (front-end)** vem **antes** da
> **Fase 2 (servidor)**. As versões (Grupo F) e o side-by-side de versões (Grupo G) funcionam em memória
> via `s.saves` (como a v12 já fazia). O esquema `.json` continua definido (S3) — sem retrabalho quando a
> persistência chegar.

> **📍 ESTADO no fecho da S3 (2026-06-10):** **D feito** (em memória), **E e G parciais** (ver checkboxes).
> Tudo ⏳ pendente de aceitação. **Próximo recomendado:** os **`.json` por árvore** (serialização: classes,
> grupos, atribuições por nó) — é a entrada na **Fase 2** (S1+S2+S3, Ordem 8). O modelo de dados já está
> estabilizado (campos `classePrimaria/secundaria/classeTipo/iconCustom` + `localLib`/`systemLib` + `view`),
> por isso serializar não exige retrabalho. Alternativas: completar **E** (modo custom/Aplicar em massa) ou **H**.

---

## Visão (onde queremos chegar)
**MapLab** — editor single-file de taxonomias hierárquicas, **genérico** (o utilizador cria projetos e
árvores em runtime, sem nada hardcoded), com **classificação por classes/grupos**, **versões de estrutura
e de classes**, **comparação lado a lado**, **persistência real** via servidor local opcional (com
fallback para memória), e **pontes ao sistema de ficheiros** (mapear pastas → árvore; árvore → criar
pastas). Mantém o princípio single-file, sem build/dependências, e privacidade (uso local).

---

## FASE 1 — App genérica + classificação (front-end) · `Planodeacao-app.md`

### Bloco já feito (⏳ pendente de aceitação → a confirmar)
- [x] **A — App genérica.** Sem mapas hardcoded. Modelo `workspace{projects→trees}`; criar/trocar/
  renomear/apagar Projetos e Árvores em runtime; estado vazio inicial; side-by-side dinâmico;
  edição igual à anterior. _(Ordem 1)_
- [x] **B — Ícones nos ramos.** 883 ícones Notion embebidos (bloco estanque), picker pesquisável,
  ícone por nó (`node.icon`), recolorido pela cor do ramo, na árvore e no mind map. _(Ordem 2)_
- [x] **C — Rename para MapLab.** Título/cabeçalho internos + ficheiro vivo `MapLab.html`. _(Ordem 3)_

### Bloco por implementar
- [x] **D — Classes & Grupos.** _(Ordem 4 — front-end, em memória)_ **FEITO em memória (S3, ⏳ pendente de aceitação).**
  Tab "Classes" em **3 zonas estanques**: Visualização ("Mostrar por" Grupo/Classe; Ícones Primário/Secundário;
  Cor Primária/Secundária/Desligada), Gestor (Locais/Sistema, dropdowns Grupo→Classe, Editar Grupos/Classes com
  drag&drop, "Sem Grupo" real com cor/ícone), Atribuir. Multi-classe primária+secundária; render do nó com
  ícone(s)+cor (R1/R2/R4); classe resolvida em ambas as libs por id (imune ao scope). Falta só: persistir (`.json`, Fase 2).
  - Painel lateral com **2 tabs**: "Edição Árvore" (atual) e "Classes".
  - Tab "Classes" com toggle **Locais / Sistema**.
  - **Classes Sistema** = globais, gravadas no índice `MapLab.json` (zona estanque), disponíveis sempre
    (mesmo sem projeto). **Classes Locais** = por árvore, no `.json` dessa árvore.
  - **Grupos** agrupam classes (ex.: "Conhecimento", "Finanças"). Grupo e Classe têm **ícone e cor**.
  - **Multi-classe** por nó: **primária + secundária**.
  - **Origem do ícone do nó**: controlo **global da árvore** ("por Classe" / "por Grupo") + override
    **Custom** por nó (custom muda só o ícone, não a classe).
  - **Regra de cor**: cor do ícone = cor da classe ativa (primária; secundária sobrepõe no modo
    respetivo); se nó sem classe e Custom → cor do custom/ramo.
  - **Visualização configurável**: ícones e/ou cores (ambos, só um, ou nenhum) e modo "só primárias"
    vs "primárias + secundárias".
- [~] **E — Atribuição de classes em massa.** _(Ordem 5 — front-end, em memória)_ **PARCIAL (S3).**
  Feito: zona "Atribuir Classes" — Ativar edição da árvore, toggle Primária/Secundária, toggle **"A filhos" Sim/Não**;
  clicar num nó atribui a classe selecionada no Gestor (com "A filhos" aplica à subárvore). **Falta:** modo
  "custom"/checkboxes por nó só nos níveis abertos + botão "Aplicar" em massa (o atual é clique-a-clique).
  - Botão "Atribuir Classe" + toggle **"aos filhos" / "custom"** (alternável a meio do processo).
  - Checkbox em cada nó **só nos níveis abertos**; "aos filhos" seleciona nó+subárvore (clicar num
    filho remove-o e sub-filhos); "custom" = seleção manual fina; botão "Aplicar".
- [ ] **F — Versões de classe (sub-versões).** _(Ordem 6 — front-end, em memória via `s.saves`)_
  - "Gravar versão classe": V1.a, V1.b… aninhadas na versão de estrutura (V1, V2…). Dropdown de versão
    de árvore + dropdown ao lado com versões de classe.
  - **Em memória:** as versões vivem em `s.saves` (perdem-se ao recarregar, como a v12). A gravação em
    ficheiros é o Grupo **S4** da Fase 2 (com o mesmo esquema de nomes).
- [~] **G — Side-by-side avançado (2 modos).** _(Ordem 7 — front-end)_ **PARCIAL (S3).**
  Feito: side-by-side ganhou **painel de edição partilhado** (árvore ativa por clique no título; tabs Edição+Classes
  agindo sobre a ativa; só a coluna ativa responde a cliques; mostra ícones/cores de classe) + **colunas
  redimensionáveis** + paridade de funções com a vista normal (expand/colapsar respeita seleção; Classes funciona).
  **Falta:** os 2 MODOS formais (Modo 1 mesma árvore versões lado a lado; Modo 2 árvores diferentes com versão por painel)
  — dependem do Grupo F (versões de classe).
  - **Modo 1**: mesma árvore, versões lado a lado (cada painel escolhe versão de estrutura **e** de classe).
  - **Modo 2**: árvores diferentes do projeto (cada uma com a sua versão).
  - **Toggle por vista/painel** para alternar primária/secundária e ícones/cores.
- [ ] **H — Numeração de nós (toggle).** _(Ordem 4, com D)_ Toggle ativar/desativar numeração na vista;
  export `.md` com/sem numeração; `.json` grava sempre o field `numeracao`. **Regra de integridade:** sem
  irmãos homónimos no mesmo pai/nível → reconciliação sem ambiguidade.
- [ ] **I — Filtros e ficheiros na vista.** _(Ordem 10, com S5; ⚠ a debater em detalhe)_ Toggle mostrar/esconder
  ficheiros; filtro por extensão/nome/pasta; 2 modos (expandir-o-necessário vs esconder-irrelevantes).
  Base: `referencias/instrucoesMapa.md`.

---

## FASE 2 — Persistência + ficheiros (servidor) · `Planodeacao-server.md`

- [ ] **S1+S2+S3 — Persistência base.** _(Ordem 8 — depois de toda a Fase 1 front-end)_
  - Servidor Python local **opcional** (stdlib, `.bat`, contrato espelha `TableEditorApp/acc_server.py`);
    `ping` no arranque.
  - **Fallback gracioso**: offline → alerta + modo memória (não bloqueia).
  - **Índice `MapLab.json`** (pasta do HTML): projetos→árvores (ref. ficheiro) + Classes/Grupos Sistema
    (zona estanque). Autosave. Sem ficheiro → app vazia.
  - **Save por árvore = 2 ficheiros**: `Arvore X.md` (só hierarquia, limpo) + `Arvore X.json`.
    **O esquema completo do `.json` está DEFINIDO** em `Planodeacao-server.md` → S3 (inclui campos de
    classe e `numeracao` desde já — resolve a tensão de ordem; a persistência grava o formato final).
  - **Reconciliação `.md`↔`.json` por `nome+nivel+pai`** — SEM ambiguidade por design (ver Grupo H).
- [ ] **S4 — Versões em ficheiros.** _(Ordem 9, com Grupo F)_ `Arvore X-vN.md/.json`; sub-versões de classe
  `Arvore X-vNa.json` partilham o `.md` da versão. _(esquema confirmado)_ Dá durabilidade ao que o Grupo F
  já faz em memória.
- [ ] **S5 — Mapear Pasta (disco → árvore).** _(Ordem 10)_ `walk` de uma pasta → cria a árvore, **incluindo
  ficheiros**. Base: `referencias/instrucoesMapa.md`. Liga ao Grupo I (filtros/ficheiros na vista).
- [ ] **S6 — Criar pastas a partir de path (árvore → disco).** _(Ordem 11)_ preview+confirmação sempre;
  saltar existentes; sanitizar nomes inválidos.
- [ ] **S7 — Portabilidade / re-base.** _(Ordem 8, com a persistência base)_ Mover a pasta da app inteira e tudo
  funciona: caminhos das árvores **relativos**; `MapLab.json` na raiz; `.py` sem paths (lê do índice);
  servidor deteta mudança (compara o seu dir com `lastKnownPath`) e pede confirmação. Botão **"Mudar path
  de árvores"** (com opção de mover ficheiros).
- [ ] **S8 — Mirror por versão.** _(Ordem 9, com S4)_ Cada árvore grava em `Projetos/` (app) **e** num
  **mirror** externo (path absoluto; só `.md` ou `.md`+`.json`). Mirror **por versão** com nomenclatura
  fixa `MapaXxx-Vx.md`. Botões **"Atualizar do mirror"** (da versão aberta, pergunta sobrepor) e
  **"Nova versão de mirror"** (cria a V seguinte no path).
  - **UI destes na app → Grupo J do `Planodeacao-app.md`.**

---

## Dependências e ordem (visão) — REORDENADA (S3, front-end primeiro)
- Ordem **global partilhada** entre os dois planos (1,2,3… únicos).
- **FRONT-END PRIMEIRO:** toda a Fase 1 (D,H,E,F,G em memória) **antes** da Fase 2 (servidor). A antiga
  regra "persistência (4) antes das Classes (5)" foi **dissolvida** — só existia para gravar; o objetivo
  atual é ver funcionar.
- **Nova ordem global:**
  - **4** = D Classes & Grupos + H Numeração _(foco atual)_
  - **5** = E Atribuição em massa
  - **6** = F Versões de classe (em memória, `s.saves`)
  - **7** = G Side-by-side avançado
  - **8** = S1+S2+S3 Persistência base + S7 Portabilidade
  - **9** = S4 Versões em ficheiros + S8 Mirror
  - **10** = S5 Mapear Pasta + I Filtros/ficheiros _(⚠ I a debater)_
  - **11** = S6 Criar pastas
- **App ↔ Server acoplados** pelo formato dos dados (`.json`): esquema já definido (S3), por isso fazer o
  front-end primeiro **não cria retrabalho** de serialização quando a persistência chegar.

---

## Marcos de processo (continuidade) — histórico
- [x] **M0 — Scaffolding da config Claude Code.** _(2026-06-02)_
- [x] **M2 — Commit da config.** (`Setup-ClaudeCode`, `5e21636`). _(2026-06-02)_
- [x] **M1 — Primeiro ciclo de continuidade real.** Fecho `S1 - Setup e gestão`. _(2026-06-02)_
- [x] **M3 — Prompt MD arquivada.** `docs/prompt-md-generator.md`. _(2026-06-02)_
- [x] **M4 — Numeração unificada.** Track único `S #`. _(2026-06-02)_
- [x] **M5 — Sistema de governação de alterações.** Arqueologia + 2 planos + instrução de agente +
  log append-only + questionário (validado por subagente). _(2026-06-08, branch `App-Generica`)_

---

## Princípios (do utilizador)
- App **single-file**, portável, sem build/dependências.
- **Privacidade primeiro** (sem publicação pública; transcripts fora do git). Servidor é **local**, não exposto.
- Mudanças **cirúrgicas** e **simples** (ver guidelines em `CLAUDE.md`).
- **Versão Original intacta** em `Arqueologia Alteracoes/00-…`; ficheiro vivo = `MapLab.html`.
