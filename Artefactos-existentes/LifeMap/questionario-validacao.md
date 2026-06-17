# Questionário de Validação — Agente de Alterações ao MapLab

> **Para quem responde:** lê primeiro [`instrucao-agente-alteracoes.md`](instrucao-agente-alteracoes.md)
> e os ficheiros para que ela aponta. Depois responde a TODAS as perguntas abaixo, **na tua resposta**
> (não edites este ficheiro). Responde de forma concreta — citações de ficheiros/funções valem mais que
> generalidades. Estas respostas servem para o utilizador confirmar que percebeste o processo e sabes agir.

## Secção 1 — Estrutura e fonte da verdade
1. Qual é o **único ficheiro que se edita** e qual é o ficheiro que **nunca** se toca? Onde está cada um?
2. O que está na pasta `Arqueologia Alteracoes/` e qual a **regra de ouro** sobre esses ficheiros?
3. Quando se cria um **snapshot novo** na Arqueologia? (não é a cada alteração — quando?)

## Secção 2 — Arquitetura do código
4. Descreve o **modelo de dados central** da app (`workspace`) e onde vive o estado de cada árvore.
5. Os ~11 stores por árvore (ex.: `mmPos`, `tabView`, `mmExpanded`) — como são inicializados hoje, e
   porque é que **já não** são literais de chave-fixa?
6. Como se adicionam painéis de árvore à UI (qual o mecanismo/factory e o template)?
7. Como se acede aos **ícones**? Qual a API e onde está o pacote? Se eu te pedir para **remover** 100
   ícones, **que parte do ficheiro** tocas — e qual NÃO tocas?
8. Qual o **comando exato** para validar o JS depois de editar `MapLab.html`?
8b. **Duas versões:** qual é a **virgem** e qual a **gerada**? O que NUNCA pode estar na virgem? Que comando
    regeneras depois de editar a app, e onde vive o bloco-fonte do botão "Carregar projetos"? O que cria esse
    botão (que projetos/árvores) e de onde lê os dados?

## Secção 3 — As duas fases e o modelo-alvo
9. Quais são as **duas fases** e que ficheiro de plano descreve cada uma?
10. Quando o Save (Fase Server) existir, **que dois ficheiros** gera por árvore e o que vai em cada um?
11. Como se liga um **ícone/classe** a um nó depois de o `.md` ser editado por fora? (qual a chave de
    reconciliação, e porquê não por posição?)
12. Diferença entre **Classe Sistema** e **Classe Local** — onde fica gravada cada uma?
13. Um nó pode ter várias classes. Como se decide o **ícone e a cor** que aparecem? (primária/secundária,
    origem do ícone, regra de cor, e o caso "custom sem classe").

## Secção 4 — Protocolo e governação
14. O que significam os estados `[ ]`, `[~]`, `[x]`, `[!]` e o que preenches num grupo quando concluis um item?
14b. **Checklist "após cada alteração concluída":** enumera TODOS os passos obrigatórios (há um passo novo
    além de validar JS / append no log / atualizar o plano — qual é, e porquê?).
15. O que é a **"ordem global partilhada"** entre os dois planos e porque existe?
16. Regras do `log-alteracoes.md`: é editável? o que se faz quando uma decisão antiga deixa de valer?
17. Há alguma alteração marcada **"pendente de aceitação"**? Quais, e o que isso implica para o teu trabalho?

## Secção 5 — Ação
18. Qual é a **primeira coisa** que tens de perguntar ao utilizador antes de começar a trabalhar?
19. Se a resposta for **"continuar"**, descreve os passos exatos que segues (do plano ao log).
20. Se a resposta for **"auditoria"**, o que verificas e o que **NÃO** podes fazer?
21. Em que circunstância podes **commitar/fazer push**?

## Secção 6 — Armadilhas (mostra que percebeste os riscos)
22. Vais implementar as **Classes** (Grupo D da app). Que pré-requisito de OUTRO plano tens de confirmar
    primeiro, e porquê?
23. Porque é que fechar o formato do `.json` só no plano da app (ou só no do server) é um erro?

---

## Secção 7 — Compreensão POR ALTERAÇÃO (o teste-chave)
> Objetivo: provar que, **só com o `roadmap.md` + os `Planodeacao-*.md`**, sabes IMPLEMENTAR cada
> alteração. Para **cada** item abaixo responde aos **4 pontos**: **(a) o que farias** (passos concretos
> no código de `MapLab.html` e/ou servidor — funções/estruturas que criarias ou tocarias); **(b) output
> pretendido** (o que o utilizador vê/obtém quando está feito); **(c) implicações no código/dados**
> (campos novos no modelo, no `.json`, dependências, riscos); **(d) entrada no log** — escreve o
> **rascunho real** da entrada que farias em `log-alteracoes.md` ao concluir (no formato das entradas
> existentes: #NNN, Data, Plano, Branch/Commit, Estado, Como foi feito, Implicações, Verificação).
>
> **Importante:** se a especificação de um item for **insuficiente para implementar sem adivinhar**,
> di-lo explicitamente e lista as perguntas que precisarias de fazer ao utilizador. Isso é tão valioso
> como uma boa resposta — é para isto que serve este teste.

### Fase 1 (app) — `Planodeacao-app.md`
24. **Grupo D — Classes & Grupos.** ⚠ **PARCIALMENTE IMPLEMENTADO** (sub-passo D-1 feito; ver `log` #009).
    (a/b/c/d) — inclui: como modelarias Classes Sistema vs Locais em memória e onde cada uma persiste;
    estrutura de um Grupo e de uma Classe; como um nó referencia primária/secundária; como funciona a
    "origem do ícone global da árvore + override custom" e a regra de cor; o que muda no painel lateral (2 tabs).
    **Adicionalmente, VERIFICA o que já está no código** (`MapLab.html`): confirma que existem `systemLib`,
    `localLib`/`view`/`classTab` em `initTree`, a tab "Classes" (`renderClassPanel`), o CRUD e o widget de cor;
    e indica o que **falta** (sub-passos D-2 atribuição ao nó, D-3 render ícone/cor, D-4 toggles). As decisões
    R1-R4 (precedência de cor, dois ícones no modo prim+sec, avisar ao apagar, migração de ícones legado) estão
    fechadas — onde estão registadas?
25. **Grupo E — Atribuição de classes em massa.** (a/b/c/d) — inclui: o comportamento exato do toggle
    "aos filhos"/"custom", como mostras checkboxes só nos níveis abertos, e como o "Aplicar" altera o estado.
26. **Grupo F — Versões de classe (sub-versões).** (a/b/c/d) — inclui: como representas V1.a/V1.b em
    relação a V1, e como isso interage com os saves de estrutura já existentes.
27. **Grupo G — Side-by-side avançado (2 modos).** (a/b/c/d) — inclui: o que muda face ao side-by-side
    atual, e como cada painel escolhe versão de estrutura + versão de classe (Modo 1) vs árvore+versão (Modo 2).

### Fase 2 (server) — `Planodeacao-server.md`
28. **S1+S2+S3 — Persistência base.** (a/b/c/d) — inclui: que endpoints do servidor criarias; como a app
    deteta online/offline e faz o fallback; o conteúdo exato do `MapLab.json`; e os DOIS ficheiros do Save
    por árvore (o que vai no `.md` vs no `.json`).
29. **Reconciliação `.md`↔`.json`.** Descreve o algoritmo que implementarias para, depois de o `.md` ser
    editado por fora, reatribuir ícones/classes por `nome+nivel+pai`. O que acontece a um nó cujo
    `nome+nivel+pai` já não existe? E a dois nós que colidam na mesma chave?
30. **S5 — Mapear Pasta** e **S6 — Criar pastas a partir de path.** (a/b/c/d para cada) — inclui: as
    decisões em aberto que terias de confirmar antes de implementar (ex.: ficheiros vs só pastas,
    profundidade, ocultas; preview/confirmação antes de escrever no disco).

### Meta
31. Depois de responderes a 24–30: o roadmap + planos foram **suficientes para implementar sem adivinhar**?
    Dá um veredicto por item (D,E,F,G,S1-3,S5,S6): **"implementável"** / **"implementável com pressupostos"**
    (lista-os) / **"insuficiente"** (lista as perguntas que farias ao utilizador). Esta é a saída mais importante.
