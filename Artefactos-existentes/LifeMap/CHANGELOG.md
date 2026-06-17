# Changelog — LifeMap Laboratory

Registo das alterações **visíveis na app**, por versão. Formato inspirado em
[Keep a Changelog](https://keepachangelog.com/). Para os diffs exatos do código, ver o git;
para mudanças de **dados/estrutura** dentro da app, ver o changelog interno de cada tab.

> **Regra:** uma linha por mudança que o utilizador nota (feature, fix, remoção, bump de
> versão). **Não** é um diário linha-a-linha do código. Atualizado no fecho de cada sessão
> em que se mexa na app (ver `CLAUDE.md` → Fecho).

---

## [Não lançado]
### Adicionado
- **Side-by-side com edição:** a vista "Side by Side" passa a ter um **painel de edição partilhado** à
  direita. Clicar no **título de uma coluna** torna essa árvore a ativa (destacada com contorno);
  só a coluna ativa responde a cliques nos nós (seleção/atribuição) e o painel mostra as ações dessa
  árvore (tabs "Edição Árvore"/"Classes"). As **colunas ficam redimensionáveis** — arrasta a borda
  direita de cada coluna — com botão **"Largura igual"** para repor. O side passa também a mostrar os
  **ícones e cores das classes** de cada nó (igual à vista normal).
- **Classes & Grupos** (Grupo D, início): painel direito passa a ter 2 tabs — "Edição Árvore" e
  "Classes". Na tab Classes: **dropdowns encadeados Grupo → Classe** (escolher grupo filtra as classes
  desse grupo; "Sem Grupo" sempre disponível) para selecionar a classe; botões **"Editar Grupos"** e
  **"Editar Classes"** que abrem modais com criar / renomear / apagar / **reordenar (drag & drop)** —
  nas classes também **mudar de grupo**; apagar um grupo deixa as classes em "Sem Grupo". Bibliotecas
  **Locais** (por árvore) e **Sistema** (globais); widget de cor com paleta + cor livre; preferências
  de visualização por árvore (ícone por Classe/Grupo, só primárias / prim+sec, mostrar ícones/cores).
- **Atribuir classes aos nós** (Grupo D/E): a tab Classes ganha 3 zonas — Visualização, Gestor e
  **Atribuir Classes**. Em Atribuir: botão "Ativar edição da árvore" + toggle Primária/Secundária;
  com o modo ativo, **clicar num nó atribui-lhe a classe** selecionada no Gestor (substitui a do mesmo
  tipo). Os nós passam a **mostrar o ícone e a cor da classe** — no modo "prim+sec" aparecem dois ícones
  (primária + secundária). Durante a atribuição a árvore fica realçada e o arrastar de nós é desativado.
- **Atribuir a filhos:** a zona Atribuir ganha um toggle **Sim/Não "A filhos"** — com "Sim", clicar num
  nó atribui a classe **ao nó e a toda a sua subárvore** (ignora nós de sistema); com "Não", só ao nó.
- **"Sem Grupo" com cor e ícone:** em "Editar Grupos" passa a haver uma linha fixa **"Sem Grupo"** cuja
  cor e ícone se podem editar (nome fixo, sem apagar/renomear). As classes sem grupo passam a poder herdar
  essa aparência quando a visualização está "por Grupo".
### Corrigido
- No **side-by-side**, o toggle **Locais/Sistema** e a seleção de grupo/classe na tab Classes passam
  a funcionar correctamente (antes escreviam no painel escondido da vista normal em vez do painel side).
- No **side-by-side**, **expandir/colapsar** com um nó selecionado respeita agora a subárvore desse
  nó (igual ao comportamento da vista normal): "Nível N" expande só dentro do nó selecionado sem
  tocar nos outros ramos; "Colapsar tudo" colapsa só os descendentes do nó selecionado.
- No **side-by-side**, o realce visual do **modo Atribuir** (contorno na coluna activa) passa a
  aparecer/desaparecer ao ligar/desligar o modo via o botão na tab Classes.
- No **modo Atribuir**, a árvore segue a zona Atribuir (não a Visualização): mostra só o tipo
  escolhido — Primária ou Secundária —, escondendo o outro.
- Nós **sem classe/grupo** do tipo mostrado passam a aparecer em **cinzento neutro**, em vez de
  herdarem a cor do ramo/árvore.
- Painel direito da tab Classes faz **scroll** quando o conteúdo não cabe (deixa de ficar cortado).
- Modais sobrepostos: ao abrir "Nova classe" ou "Escolher ícone" a partir de um modal de gestão, o de
  trás deixa de ficar empilhado — só um modal é visível de cada vez, e o anterior reabre ao fechar.
- **Classes atribuídas deixam de desaparecer ao mudar o toggle Locais/Sistema** no Gestor de Classes:
  a visualização mostra sempre o que está atribuído, procurando cada classe por id em ambas as
  bibliotecas (Sistema e Local). Um nó com primária de Sistema e secundária de Local passa a mostrar
  os dois ícones/cores corretamente, independentemente do scope ativo.
### Alterado
- **Visualização (tab Classes) reformulada:** em vez de "ícone por Classe/Grupo" + "só primárias/prim+sec"
  + checkboxes de ícones/cores, passa a ter — **"Mostrar por"** (Grupo|Classe, aplica-se a ícones **e** cor),
  **"Ícones"** (mostrar Primário e/ou Secundário, independentes) e **"Cor"** (Primária|Secundária|Desligada).
- Menus de **Expandir/Colapsar** (árvore principal) passam a respeitar o nó selecionado: sem
  seleção, aplicam a toda a árvore (como antes); com um nó selecionado, atuam **só a partir desse
  nó** (a sua subárvore), sem afetar o resto. Os níveis ("Nível 1/2/…") contam **a partir do nó**
  selecionado.

## [v12]
### Adicionado
- 4º mapa **Obsidian** (vault AI / organização do conhecimento), com árvore, mind map
  (estrela/horizontal), versões, Import/Editar MD, cor de área e coluna no Side-by-Side.

## [v11]
### Corrigido
- "Transportes" reposto dentro de **Património** (mesmo nível que Imóveis).
### Alterado
- Estruturas de Life Map e iCloud atualizadas a partir dos MD fornecidos.

## [v10]
### Alterado
- Life Map e iCloud atualizados; tratados como "Originais" (sem criar versões).

## [v9]
### Adicionado
- iCloud passa a ter "Original" + "v1" gravada (estrutura ampla de email).

## [v8]
### Corrigido
- Mind map: reposicionar nível-1 à esquerda/direita (setinha clicável no filho).
- Linhas dos ramos passam a ir até à fronteira das caixas (não ao centro).
### Alterado
- Estrutura original do Life Map substituída pelo ficheiro fornecido.

## [v7]
### Removido
- Numeração hierárquica automática (1, 1.1, 2…) nos mapas.
### Alterado
- Formato MD universal entre tabs: `# Versao` + `# Estrutura`.

## [v6]
### Adicionado
- Mind map interativo: arrastar nós move filhos; arrastar a seta move filhos.
- Paleta de cores por nível-1 (cascata para descendentes); zoom (scroll) e pan (botão direito).
### Corrigido
- Estado do mind map preservado ao alternar para a árvore.

## [v5]
### Adicionado
- Mind map a gerar; dois layouts (estrela vs horizontal); zoom por scroll.
- Modal "Editar em MD"; formato de import/export MD especificado.
### Corrigido
- Botão do mind map deixa de falhar.

## [v4]
- Base inicial conhecida: 5 tabs (lifemap, icloud, notion, obsidian, side) e mind map com
  controlos básicos. _(Versões anteriores: v2 em `.Old/`; não existe v3.)_

---

_Notas: datas por versão não estão registadas no histórico; ver `git log` para a cronologia
de commits. GitHub Pages foi abandonado por privacidade (ver `memory.md` D7)._
