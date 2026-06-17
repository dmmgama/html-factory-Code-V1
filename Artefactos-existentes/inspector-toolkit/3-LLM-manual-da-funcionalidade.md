# Documento 3 — Manual para LLM
## Funcionalidade da "Caixa Inspetora" (referência semântica)

> **Para quem é:** para um modelo de linguagem (LLM) que vai trabalhar num HTML que **já tem** a Caixa
> Inspetora, ou que precisa de **raciocinar sobre ela**, responder a perguntas do David, depurá-la ou
> estendê-la. Este documento descreve **o que a caixa É, o que VÊ, o que NÃO vê, e como interpretá-la**.
> Não é um tutorial de implementação (esse é o Documento 1).

---

## 1. Definição e propósito

A Caixa Inspetora ("Inspector") é uma camada de **observabilidade não-invasiva** injetada num HTML
self-contained. Transforma a app num **"Projeto Observável"**: expõe, em runtime, três dimensões da
arquitetura — **Data, Logic, Layout** — mais um modo interativo de *element-picking* (**Pick**).

**Intenção do utilizador (David):** validar que a arquitetura desenhada está a ser seguida — i.e.,
verificar a correspondência entre *design pretendido* e *comportamento real*. Quando ajudares, ancora
sempre as respostas neste objetivo.

**Princípio fundador:** a caixa **não altera** a app. É adicionada por cima (um bloco CSS, um bloco
HTML, um IIFE de JS) sem editar o código original. Mantém este princípio em qualquer alteração.

---

## 2. Arquitetura interna (modelo mental)

Tudo vive num **IIFE** no fim do último `<script>`, partilhando o scope com as funções da app. Peças:

| Peça | Papel |
|------|------|
| `getState()` | Devolve o objeto de estado da app (fonte da verdade). Base da vista **Data**. |
| `dataSources()` | Mapa `{rótulo → função}` das coleções mostráveis no dropdown da Data. |
| `ENGINE_FNS` + `patch()` + `recordCall()` | **Call tracer**: cada função listada é envolvida (`window[fn] = patch(window[fn], fn)`) para registar invocações. Base da vista **Logic**. |
| `VIEWER_META` + `activeViewKey()` + `renderCount` | Metadados das vistas e contagem de renders. Base da vista **Layout**. |
| `PICK_META` + `findInspectable()` + `lookup()` + `infer()` | Registo semântico por elemento + resolução. Base do **Pick**. |
| Listeners de `mouseover`/`click`(captura)/`keydown` | Implementam o modo Pick e os atalhos. |

---

## 3. As quatro vistas — semântica precisa

### 3.1 DATA
- **Mostra:** `JSON.stringify` (com syntax-highlight) de um pedaço do estado, escolhido no dropdown
  (`dataSources()`), mais estatísticas derivadas (contagens por chave).
- **Significado:** a "fonte da verdade". É **um snapshot** no momento do render da vista — não é
  reativo a cada mutação; atualiza quando o Inspector re-renderiza (refresh manual, troca de aba,
  ou um render principal da app via o hook).
- **Arrays longos** são truncados (ex.: 5 itens + "… (+N mais)") para performance.

### 3.2 LOGIC
- **Mostra:** as últimas N (≈50) chamadas às funções de `ENGINE_FNS`, mais recente no topo, com
  deduplicação consecutiva (contador `×n`) e tempo relativo ("agora", "3s atrás").
- **Significado:** evidência **factual** do que correu. É a **verdade do runtime**.
- **Limite crítico:** só "ouve" funções que (a) estão em `ENGINE_FNS` e (b) são chamáveis via
  `window[nome]` no momento do patch. Funções internas a closures, métodos de objeto não-globais,
  ou handlers de frameworks **não são capturados**. Ausência de registo ≠ ausência de execução.

### 3.3 LAYOUT
- **Mostra:** o viewer ativo (via `activeViewKey()`), a sua descrição/renderer (de `VIEWER_META`),
  a lista de todos os viewers, e o `renderCount` por vista nesta sessão.
- **Significado:** que subsistema de apresentação é responsável pelo canvas atual.
- **Limite:** `VIEWER_META` é **curado** (texto escrito à mão). O `renderCount` é factual (incrementa
  no hook do render principal).

### 3.4 PICK (modo inspecionar)
- **Comportamento:** ao ativar, `document.body` ganha `insp-picking` (moldura âmbar + banner). Um
  listener de **clique em fase de captura** chama `preventDefault()` + `stopPropagation()` +
  `stopImmediatePropagation()` — **a ação real do elemento NÃO dispara**. Em vez disso resolve o
  elemento (`findInspectable` via `closest(PICK_SELECTORS)`) e mostra o relatório `{data, logic, layout}`.
- **Resolução de metadados (`lookup`):** itera `PICK_META` e devolve o **primeiro** seletor que faz
  `el.matches(seletor)` → daí a ordem importar (mais específico primeiro). Sem match, cai em `infer()`.
- **`infer()`:** best-effort a partir de tag, id, texto, `closest('[data-view]')`, `onclick` inline, e
  (para form controls) label/placeholder/opção selecionada.
- **Significado:** a **intenção documentada** de cada elemento — o que *deveria* fazer.
- **Saída:** botão 🎯 ou tecla `Esc`. Cliques **dentro** do próprio Inspector continuam funcionais.

---

## 4. A distinção que mais importa: INTENÇÃO vs. FACTO

Esta é a chave para usares a caixa corretamente e para explicares ao David.

| | Fonte | Natureza |
|---|---|---|
| **Pick → Logic/Layout** | `PICK_META` / `infer()` | **Intenção curada** — o que o design diz. Pode ficar **desatualizado** se o código mudar. |
| **Aba Logic** | call tracer em runtime | **Facto** — o que realmente correu. |
| **Aba Layout → renderCount** | hook em runtime | **Facto**. |
| **Aba Data** | `getState()` | **Facto** (snapshot). |

**Método de validação de arquitetura** (o uso-alvo): comparar a *previsão do Pick* para um elemento
com o *registo da aba Logic* depois de acionar esse elemento a sério. Convergência ⇒ arquitetura
respeitada. Divergência ⇒ ou metadados desatualizados, ou desvio/bug real. Ao reportar, **distingue
sempre estas duas causas** em vez de afirmar um bug com certeza.

---

## 5. O que a caixa NÃO consegue ver (não alucines o contrário)

- Funções não registadas em `ENGINE_FNS` ou não-globais.
- Lógica dentro de bibliotecas/frameworks (React/Vue/etc.) — sem expor `window`, o tracer fica cego.
- Mutações de estado fora de `getState()` (ex.: dados só no DOM, ou noutra estrutura não mapeada).
- A *correção* da lógica — só observa **que** algo correu, não **se** o resultado está certo.
- Ordem de execução fina dentro de uma única função (vê a função como uma só chamada).

Se o David perguntar algo que caia nestes pontos, diz claramente que está **fora do alcance** da caixa
e propõe alternativa (ex.: adicionar a função a `ENGINE_FNS`, ou expor estado em `window`).

---

## 6. Como responder a pedidos típicos do David

| Pedido | Abordagem correta |
|--------|-------------------|
| "O botão X faz o que devia?" | Lê o `PICK_META['#X']` (intenção). Pede/descreve o teste: limpar Logic → clicar X → comparar. Reporta convergência/divergência. |
| "Adiciona inspeção a este elemento" | Acrescenta entrada em `PICK_META` (seletor específico, ordem certa) e, se preciso, um token em `PICK_SELECTORS`. Não toques no resto. |
| "A vista Data está vazia/—" | Verifica `getState()` e `dataSources()` (CONFIG 1 e 2). O estado existe e é global? |
| "A Logic não regista nada" | A função-alvo está em `ENGINE_FNS` e é `window[nome]`? Se for closure/framework, explica o limite e propõe expor em `window`. |
| "Estende a caixa para outro HTML" | Encaminha para o **Documento 1** (script do agente). Faz a descoberta das 4 coisas (STATE, engine fns, viewers, elementos). |
| "Porque é que clicar não faz nada?" | Provavelmente o **modo Pick está ligado** (de propósito bloqueia ações). `Esc` para sair. |

---

## 7. Invariantes a preservar em qualquer edição

1. **Não-invasivo:** zero alterações ao código original da app.
2. **Um só** bloco CSS, **um só** bloco HTML, **um só** IIFE do Inspector.
3. O IIFE corre **depois** das funções da app existirem e **antes/junto** do arranque, para conseguir
   envolvê-las.
4. `PICK_META` ordenado do mais específico para o menos específico.
5. Cliques dentro de `#inspector` nunca são bloqueados pelo modo Pick.
6. Tudo em **pt-PT**, formatação com `<code>`/`<b>` consistente.
7. Após editar, confirmar que o `<script>` fecha e a app arranca.

---

## 8. Glossário rápido

- **Engine / motor:** as funções que executam a lógica e o render da app.
- **Viewer / canvas:** a área principal que mostra uma vista (tabela, grafo, etc.).
- **STATE / fonte da verdade:** o objeto/JSON de onde a app deriva tudo o que mostra.
- **Tracer:** mecanismo que regista chamadas a funções por *wrapping*.
- **Pick / modo inspecionar:** apontar a um elemento e obter o seu papel arquitetural, sem disparar a ação.
- **Curado vs. factual:** escrito à mão (intenção) vs. observado em runtime (facto).

---

### Resumo de uma linha
A Caixa Inspetora expõe **Data (estado real), Logic (funções que correram), Layout (quem renderiza)** e
um modo **Pick (intenção por elemento)**; usa-a para **comparar intenção com facto** e validar a
arquitetura — sabendo que ela observa *que* acontece, não garante que está *correto*.
