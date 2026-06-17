# bugs.md — Registo de Falhas (APPEND-ONLY)

> Registo de bugs/falhas conhecidos no MapLab. Append-only: nunca apagar entradas; quando um bug
> for corrigido, marcar `[x]` e indicar o commit. Secções por área funcional.

---

## 1. Dashboard

_(sem entradas)_

---

## 2. Árvores

_(sem entradas)_

---

## 3. Side-by-side

- [ ] **[BUG-S1] Drag & drop não funciona no side-by-side** — arrastar nós está quebrado na vista
  side-by-side (funciona na vista normal). A investigar.

---

## 4. Abas — Edição

_(sem entradas)_

---

## 5. Aba — Classes

- [ ] **[BUG-C1] Visualizador mostra primária e secundária ao mesmo tempo** (árvore e side-by-side) —
  a vista devia mostrar só a cor escolhida (primária OU secundária), mas está a mostrar ambas
  simultaneamente. Suspeita: quando uma classe é de Sistema e a outra é Local, `resolveNodeVisual`
  não está a filtrar pelo modo ativo e aplica as duas.

- [ ] **[BUG-C2] Toggle Primária/Secundária em modo edição não atualiza o visualizador** (árvore e
  side-by-side) — mudar o botão prim/sec na zona Atribuir (modo edição ativo) não faz re-render
  da árvore; as cores só mudam depois de outra ação. Falta um `renderTree` / `renderSideTree` no
  handler do toggle.

---

## 6. Outros

_(sem entradas)_
