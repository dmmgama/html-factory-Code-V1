# additions.md — Adições ao Roadmap (APPEND-ONLY)

> Registo de adições/updates que o utilizador quer introduzir no roadmap. Append-only: nunca
> apagar entradas; quando um item for incorporado no roadmap e nos planos, marcar `[x]` e
> indicar onde foi integrado. Secções por área funcional.

---

## 1. Dashboard

- [ ] **[ADD-D1] Mostrar código de cores das árvores** — exibir em algum sítio visível (ex.: barra
  de projetos ou painel) as cores associadas a cada árvore, para o utilizador saber rapidamente
  a que cor corresponde cada árvore.

---

## 2. Árvores

- [ ] **[ADD-A1] Toggle "afetar filhos" em todas as funções** — todas as operações que atuam num
  nó devem ter um toggle para propagar ou não aos filhos (subárvore). Aplicável globalmente a
  qualquer função que hoje só age no nó selecionado.

- [ ] **[ADD-A2] Botão Undo** — desfazer a última operação realizada na árvore.

- [ ] **[ADD-A3] Numeração — modos e tipos**
  - **Modos:** Geral (toda a árvore), Por Pai-Filhos (reinicia a contagem por cada ramo), Criar
    Secções (com separador configurável, ex.: `1.1 / 1.2`).
  - **Tipos:** Árabe (1,2,3…), Romano (I,II,III…), Alfabeto (a,b,c…).
  - **Export:** opção de incluir ou não a numeração no export `.md` e no mirror (independente do
    toggle de visualização).

- [ ] **[ADD-A4] Aba específica para Ficheiros (não pastas)**
  - Detetar tipos por extensão; selector para mostrar tudo ou só alguns tipos.
  - Ordenar por tipo ou por nome (globalmente ou dentro de cada subárvore).
  - Numeração de ficheiros **independente** da numeração da árvore: pode numerar dentro de cada
    nível ou sequencialmente por todos os filhos.

- [ ] **[ADD-A5] Dropdowns Colapsar/Expandir inteligentes** — o menu só mostra os níveis que
  existem abaixo do nó selecionado. Se não houver nó selecionado, atua sobre toda a árvore
  (comportamento atual). Aplica-se tanto à vista normal como ao side-by-side.

---

## 3. Side-by-side

- [ ] **[ADD-S1] Dois modos formais de side-by-side**
  1. **Árvores diferentes** — escolher quais as árvores do projeto a mostrar (ativar/desativar
     por coluna).
  2. **Mesma árvore** — versões lado a lado (cada painel escolhe a versão de estrutura e/ou de
     classe) OU uma única versão com classes lado a lado (primária vs secundária por painel).

- [ ] **[ADD-S2] Drag & drop entre árvores diferentes** — no modo side-by-side com árvores
  diferentes, poder arrastar um nó de uma coluna para outra (mover nó para outra árvore).

---

## 4. Abas — Edição

- [x] **[ADD-P1] Painel lateral único para árvore e side-by-side** — ✅ JÁ IMPLEMENTADO.
  Auditoria (S4, 2026-06-11) confirmou: `renderPanel` e `renderClassPanel` são funções únicas
  partilhadas entre as duas vistas. O redirecionamento para o painel correto é feito via
  `if(sideViewActive())hostId='side-rpanel'` no início de cada função. Sem duplicação.

---

## 5. Aba — Classes

_(sem entradas)_

---

## 6. Outros

_(sem entradas)_
