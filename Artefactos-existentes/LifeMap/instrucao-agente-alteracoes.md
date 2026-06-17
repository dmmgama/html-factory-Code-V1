# Instrução para Agente — Processo de Alterações ao MapLab

> **És um agente novo, sem contexto prévio.** Lê este ficheiro POR COMPLETO antes de agir.
> O objetivo é fazeres-te ao processo de alterações **em curso** sem repetires a fase de compreensão
> que já foi feita. Idioma de trabalho: **PT-PT**.

---

## 0. O que é isto, em duas frases
Estamos a evoluir um editor de taxonomias hierárquicas (árvores) que vive **num único ficheiro HTML**
(`MapLab.html`), sem build, sem dependências, sem framework. Partimos de uma **Versão Original** com
mapas fixos no código e estamos a torná-la **genérica** (o utilizador cria tudo em runtime) + a dar-lhe
**persistência via servidor local**.

- **Versão Original (intacta, nunca tocar):** [`Arqueologia Alteracoes/00-VersaoOriginal-lifemap_lab.html`](00-VersaoOriginal-lifemap_lab.html)
- **Ficheiro VIVO (onde se trabalha):** [`MapLab.html`](MapLab.html)

---

## 0bis. RETOMA DE SESSÃO — quando o utilizador disser **"inicia"** (ou começar uma sessão nova)
> Isto serve para retomar exatamente onde se ficou, mesmo que a sessão anterior tenha sido longa e o
> contexto se tenha perdido. **Segue esta ordem de leitura** (não saltes):

1. **`handoff.md`** — estado imediato: branch ativa, o que está feito, onde se ficou, próximos passos.
2. **`registo-auditoria.md`** (append-only) — últimas auditorias: **as lacunas conhecidas e o plano de
   correção em curso**. É aqui que descobres o que está por decidir/corrigir.
3. **`roadmap.md`** — a visão e a ordem global das alterações.
4. **`Planodeacao-app.md`** + **`Planodeacao-server.md`** — o executável: que item é o próximo `[ ]`,
   Branch/Commit/Ordem, e os "a confirmar" ainda abertos.
5. **`log-alteracoes.md`** (append-only) — como cada alteração foi feita e as suas implicações.
6. As secções **§1–§4** abaixo (arquitetura, fases, mapa de ficheiros, regras).
7. Confirma o estado real: `git log -1`, `git status`, e corre a **validação de JS** (§ abaixo) para
   garantir que o `MapLab.html` está são.

**REGISTO OBRIGATÓRIO da retoma:** à medida que lês, **escreve um log em `agente-audit-iniciar.md`**
(cria se não existir; é **append-only** — acrescenta uma secção nova datada por cada retoma) com:
- que ficheiros leste, por esta ordem, e **o que entendeste de cada um** (1–2 linhas);
- o **estado atual** que inferiste (branch, commit, marcos aceites, próximo item `[ ]` na ordem global);
- as **lacunas/decisões pendentes** que viste no `registo-auditoria.md`;
- a tua **conclusão**: estás pronto a continuar/auditar? alguma incoerência entre ficheiros?

Só depois deste registo passas à **§5 (ação final obrigatória)** e perguntas ao utilizador o que fazer.

---

## 1. Como o código está estruturado (`MapLab.html`)
Single-file: `<style>` + HTML + `<script>` no fim. Pontos-chave do JS:

- **Modelo central:** `workspace = { projects:[ {id,name,trees:[{id,name,color,icon}], activeTreeId} ], activeProjectId }`.
- **Estado por árvore:** `tabState[treeId]` (`tree`=array de nós `{id,name,isSystem,children, icon?}`,
  `selected`, `notes`, `saves`, `expanded`, …). Um `treeId` é o antigo `tabId` — **todas as funções de
  edição já são parametrizadas por `tabId`** (não assumas estado global por mapa).
- **Stores por árvore** (preenchidos em `initTree(treeId)`): `tabView`, `sideExpanded`, `mmExpanded`,
  `mmPos`, `lastPos`, `mmColor`, `mmSide`, `mmLayout`, `mmView`, `mmInited`, `mmRendered`.
  **Já não são literais de chave-fixa** — são `{}` populados dinamicamente.
- **Factory de UI:** painéis de árvore são clonados de `<template id="treePanelTemplate">` via
  `fillTemplate()`/`buildPanels()`; tabs e barra de projeto em `renderTabsBar()`/`renderProjectBar()`;
  re-render geral em `renderWorkspace()`.
- **Render da árvore:** `renderTree(tabId,nodes,term,depth)`. Painel do nó: `renderPanel(tabId)`.
  Mind map: `buildMmStar`/`buildMmHorizontal` via `svgRect(...)`.
- **Ícones (já implementados):** pacote dos 883 SVG Notion num bloco ISOLADO
  `<!-- ICON PACK START --> <script id="iconPack" type="application/json">{...}</script> <!-- ICON PACK END -->`.
  **Só lhe acedes por:** `iconSvg(name,color,size)`, `iconNames(filter)`, `iconExists(name)`. Para
  trocar/remover ícones edita **APENAS** entre os marcadores. Ícone do nó = `node.icon` (slug);
  cor via `branchColor()`.
- **Validação OBRIGATÓRIA do JS após editar:**
  ```
  node -e "new Function(require('fs').readFileSync('MapLab.html','utf8').match(/<script>([\s\S]*)<\/script>/)[1]);console.log('JS OK')"
  ```
  > ⚠ **Limitação conhecida (AUD-001 lacuna 2):** a regex apanha tudo entre o primeiro `<script>` e o
  > último `</script>`, incluindo o bloco `<script id="iconPack" type="application/json">`. O resultado
  > `JS OK` continua válido (o JSON do iconPack é sintaxe JS legal), mas a zona auditada é maior do que
  > o pretendido. Se forem adicionados mais blocos `<script>` independentes, rever este comando.
- **Teste visual:** Chrome headless existe em `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`.
  Padrão: copiar para `__t.html`, injetar driver, `--screenshot`, ler o PNG, apagar temporários.
- **Sem persistência real ainda:** "Save" guarda só em memória. Persistir = exportar `.md` (a Fase 2 muda isto).
- **DUAS VERSÕES (obrigatório a cada alteração da app):**
  - **`MapLab.html`** = **virgem** (a app real). **NUNCA** lhe metas o bloco de teste / botão de seed / dados.
  - **`MapLab-teste.html`** = **gerada** (virgem + bloco de teste inline, com botão **"Carregar projetos"** que
    cria P1[A1,A2] e P2[A1,A2,A2b] a partir de `MapsTeste/*.md`). Não é versionada (`.gitignore`).
  - **Sempre que editares `MapLab.html`, regenera a versão teste:** `node build-teste.js`. O bloco-fonte vive em
    `MapsTeste/seed-bloco.template.html` (os `.md` são re-lidos a cada build). Ver `log-alteracoes.md` #010.

---

## 2. As DUAS fases do projeto
1. **Fase APP** (front-end): app genérica ✅, ícones ✅, rename MapLab ✅ (tudo **pendente de aceitação**),
   e por implementar: **Classes & Grupos**, atribuição em massa, versões de classe, side-by-side avançado.
   → Roadmap completo: [`Planodeacao-app.md`](Planodeacao-app.md).
2. **Fase SERVER** (persistência): servidor Python opcional + fallback memória, índice `MapLab.json`,
   Save→`.md`+`.json` por árvore, versões em ficheiros, "Mapear Pasta" e "Criar pastas a partir de path".
   → Roadmap completo: [`Planodeacao-server.md`](Planodeacao-server.md).

**Modelo de dados-alvo (resumo que NÃO precisas de redescobrir):**
- `MapLab.html` = ficheiro vivo da app.
- `MapLab.json` (pasta do HTML) = índice: projetos→árvores (ref. ficheiro) + **Classes/Grupos Sistema**
  (zona estanque). Lido no arranque; se não existir → app vazia.
- Por árvore: **`Arvore X.md`** (só hierarquia, limpo) + **`Arvore X.json`** (completo: por nó
  `nome,nivel,pai,icon,classes,grupo,classeTipo,primaria/secundaria` + classes/grupos locais).
- **Reconciliação `.md`↔`.json` por `nome+nivel+pai`** (não por posição).
- **Classes**: Sistema (globais, no índice) vs Locais (por árvore). Grupos agrupam classes; grupo e
  classe têm ícone+cor. Nó pode ter primária+secundária. Origem do ícone do nó = global da árvore
  (por Classe/por Grupo) + override Custom por nó. Cor do ícone = cor da classe ativa (custom se sem classe).

---

## 3. Onde está cada coisa (mapa de ficheiros do processo)
| Ficheiro/pasta | Papel |
|---|---|
| [`MapLab.html`](MapLab.html) | **Ficheiro vivo (virgem).** É aqui que se edita. Nunca lhe metas o bloco de teste. |
| `MapLab-teste.html` | **Gerado** (não versionado): virgem + botão "Carregar projetos" inline. Regenera com `node build-teste.js`. |
| [`build-teste.js`](build-teste.js) | Gerador da versão de teste (re-lê os `.md` de `MapsTeste/` a cada build). |
| [`MapsTeste/`](MapsTeste/) | `.md` de teste (P1[A1,A2], P2[A1,A2,A2b]) + `seed-bloco.template.html` (bloco-fonte do botão). |
| [`Arqueologia Alteracoes/`](Arqueologia%20Alteracoes/) | Snapshots **congelados (read-only)**, um por marco aceite. `00` = Versão Original. Ver o README de lá. |
| [`Planodeacao-app.md`](Planodeacao-app.md) | Roadmap das alterações da **app**. Grupos com Branch/Commit/Ordem e checkboxes. |
| [`Planodeacao-server.md`](Planodeacao-server.md) | Roadmap das alterações de **servidor**. Mesma estrutura. |
| [`roadmap.md`](Artefactos-existentes/LifeMap/roadmap.md) | **Visão** que une as duas fases (o "porquê" e o "para onde"). Os planos são o "como/quando". |
| [`log-alteracoes.md`](log-alteracoes.md) | **Append-only.** Por cada alteração: como foi feita + implicações (ex.: criação de JSONs). NUNCA editar entradas antigas; só acrescentar (ou marcar uma como *superseded* por nova). |
| [`registo-auditoria.md`](registo-auditoria.md) | **Append-only.** Auditorias/validações: o que foi auditado, em que versão, feedback e plano de correção. É aqui que vês as lacunas conhecidas e o que falta corrigir. |
| [`questionario-validacao.md`](questionario-validacao.md) | Perguntas que um agente deve saber responder para provar que percebeu este processo (inclui Secção 7: implementabilidade por alteração). |
| `CLAUDE.md` · `context.md` · `handoff.md` | Regras gerais do repo + SSOT + estado imediato (lê também — `handoff.md` diz onde se ficou). |

**Ordem das alterações = numeração GLOBAL partilhada** entre os dois planos (1,2,3… únicos). Não há
duas "alteração 1".

---

## 4. Regras de atuação (não violar)
1. **Só se edita `MapLab.html`.** A `Arqueologia/` é read-only. Nunca tocar em `00-VersaoOriginal`.
2. **Snapshot só por marco ACEITE** pelo utilizador (congelar cópia em `Arqueologia/`). Entre marcos, git.
3. **Mudanças cirúrgicas**, estilo do código existente, PT-PT nas labels. Não refatorar o que não é pedido.
   Não inventar persistência/servidor fora do que está nos planos.
4. **Após cada alteração concluída:** validar JS (comando acima) + **regenerar a versão de teste**
   (`node build-teste.js`) + **append** em `log-alteracoes.md` + atualizar checkbox e Branch/Commit no plano respetivo.
   > A versão de teste (`MapLab-teste.html`) é a virgem + botão "Carregar projetos" (seed). Mantém-na em sincronia:
   > sempre que mexes em `MapLab.html`, corre o gerador. Ver §1 (duas versões) e `log-alteracoes.md` #010.
5. **App ↔ Server estão acoplados** pelo formato dos dados. Antes de fechar um `.json` num lado, confirma
   o outro plano (secção "Dependências cruzadas").
6. **Não commitar nem fazer push** sem o utilizador pedir.

---

## 5. AÇÃO FINAL OBRIGATÓRIA (faz isto sempre que arrancas com este processo)
Depois de leres tudo acima, **PERGUNTA AO UTILIZADOR**, textualmente:

> **"Queres que CONTINUE as alterações (e a partir de que ponto/ordem do plano), ou preferes que faça uma AUDITORIA do estado atual?"**

E age conforme a resposta:
- **Continuar** → vai ao plano (app/server), encontra o próximo item `[ ]` na ordem global, confirma
  pré-requisitos, implementa, valida, regista no log, atualiza o plano.
- **Auditoria** → compara `MapLab.html` contra `Arqueologia Alteracoes/00-VersaoOriginal-*` e contra o
  estado declarado nos planos; verifica que o que está `[x]` está mesmo feito e funcional (corre a
  validação de JS e um teste visual); lista discrepâncias entre planos, log e código; **não alteres**
  código numa auditoria — só relatas.

> Não assumas a escolha. Pergunta primeiro.
