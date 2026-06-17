---
created: 2026-06-11
chat: Dashboard governo colapsável — orquestração Claude Code
summary: >
  Manual de uso do dashboard para o David: como abrir, navegar pelas folhas,
  colapsar/expandir grupos, usar o toggle técnico/não-técnico, a tour,
  o inspector, pan/zoom, e como pedir um update de conteúdo a um LLM.
---

# MANUAL DE USO — Dashboard do Governo AI

> **O que é:** um dashboard visual em quatro folhas que mostra como o sistema de governo de projetos AI funciona — desde como uma sessão de trabalho acontece até como um projeto arranca e opera. Cada folha é um grafo de dependências com explicações clicáveis.

---

## 1. Abrir o dashboard

Duplo-clique em `2-dashboard/DIAGRAMAS-governo-dashboard.html`. Abre no browser sem precisar de servidor, build, ou instalação. Se aparecer uma página em branco, usa Chrome ou Edge (Firefox e Safari também funcionam).

---

## 2. As quatro folhas

A coluna da esquerda tem os botões de navegação entre folhas:

| Folha | O que mostra |
|---|---|
| **A SESSÃO** | Como nasceu o projeto: os inputs, as análises, as decisões, e o que foi produzido |
| **O FECHO** | O roteiro de tarefas até o kit estar pronto a usar |
| **O PACOTE EM EXECUÇÃO** | O que o kit contém e como monta um projeto novo |
| **O PROJETO EM OPERAÇÃO** | Como funciona um projeto no dia-a-dia: arranque, trabalho, fecho |

Clica num botão para mudar de folha. A folha ativa fica marcada com uma barra âmbar à esquerda.

---

## 3. Grupos e colapso

Cada folha organiza os nós em **grupos** (secções com fundo azul translúcido). Por defeito, os grupos estão colapsados — só os títulos das secções são visíveis, ligados por setas entre si.

### Expandir / colapsar um grupo
- Clica no botão **±** no canto superior direito do grupo
- `+` = expandir (ver os nós dentro do grupo)
- `−` = colapsar (esconder os nós, setas agregam-se ao nível do grupo)

### Controles globais (toolbar, canto superior direito do mapa)
- **EXPANDIR TUDO** — abre todos os grupos da folha atual
- **COLAPSAR TUDO** — fecha todos os grupos
- **+** / **−** — zoom in / zoom out
- **AJUSTAR** — repõe a vista ao tamanho da folha

As setas são sempre legíveis em qualquer combinação de grupos abertos/fechados — nunca apontam para nós escondidos.

---

## 4. Toggle Técnico / Não-técnico

No header (topo da página), botão **TÉCNICO** / **NÃO-TÉCNICO**.

- **NÃO-TÉCNICO** (default) — explicações sem jargão, com analogias
- **TÉCNICO** — explicações com o vocabulário do sistema (decisões D1–D24, siglas, referências cruzadas)

O toggle troca todas as descrições ao mesmo tempo: o que está no painel, os textos da tour, e as vistas gerais. Sobrevive quando mudas de folha.

---

## 5. O painel lateral (Inspector)

O painel à direita muda consoante o que clicas:

### Sem nada selecionado
Mostra a **vista geral da folha**: um parágrafo explicativo + as ligações principais entre grupos (como as secções se encadeiam). No fundo, botão **TOUR**.

### Clique num grupo
Mostra o papel do grupo no conjunto da folha + lista dos nós dentro do grupo como links clicáveis. Clica num nó da lista para o selecionar e expandir automaticamente o grupo.

### Clique num nó (filho)
Mostra a explicação do nó (técnica ou não-técnica, conforme o toggle) + as suas ligações (setas de entrada e saída) como links clicáveis.

Se o nó for um **ficheiro**, o painel mostra também a linha **Ficheiro:** com o nome/path do ficheiro.

### Limpar a seleção
- Clica numa zona vazia do mapa
- Ou prime **Esc**

---

## 6. Tour guiada

Clica **TOUR** no painel (aparece quando não há nada selecionado).

A tour percorre os grupos da folha por ordem lógica:
- O grupo atual fica destacado (borda âmbar brilhante)
- O painel mostra a descrição do grupo
- Botões **ANTERIOR** / **SEGUINTE** para navegar
- Botão **SAIR** para terminar

Usa o toggle Técnico/Não-técnico para escolher o registo dos textos da tour antes de a começar.

---

## 7. Pan e Zoom

| Ação | Como |
|---|---|
| Deslocar o mapa | Arrasta com o rato em qualquer zona vazia |
| Zoom | Roda do rato (scroll) sobre o mapa |
| Zoom in/out preciso | Botões **+** / **−** na toolbar |
| Repor a vista | Botão **AJUSTAR** na toolbar |

---

## 8. O que significam as cores e formas

| Elemento | Significado |
|---|---|
| Rect com fundo azul translúcido | **Grupo** — container de uma secção |
| Rect com fundo escuro, borda azul clara | **Processo** ou **análise** |
| Rect com fundo azul muito claro | **Documento** / input |
| Rect com borda verde | **Decisão** consolidada |
| Rect com borda âmbar tracejada | **Pendente** — por resolver |
| Rect arredondado, âmbar | **Marco** — resultado ou checkpoint |
| **Seta âmbar** (linha grossa) | Caminho crítico — sem este passo, o seguinte não avança |
| **Seta tracejada** | Condicional ou referência — ligação mais fraca |

---

## 9. Pedir um update de conteúdo a um LLM

Quando o sistema de governo evoluir e o dashboard precisar de ser atualizado:

1. Dá ao LLM (pode ser Haiku 4.5 — não precisas de Opus para isto):
   - O ficheiro `4-manual/MANUAL-LLM-dashboard.md`
   - O documento de conteúdo novo (de `3-conteudo/` ou um novo)
   - O bloco DATA do HTML (o conteúdo entre `/* ===DATA-START=== */` e `/* ===DATA-END=== */`)

2. Pede-lhe para atualizar apenas o bloco DATA seguindo as instruções do manual.

3. Copia o bloco DATA devolvido para o HTML, substituindo o bloco antigo (mantendo os delimitadores).

4. Abre o HTML e verifica que funciona (duplo-clique).

**O LLM não precisa de ler o código HTML.** O manual diz-lhe exatamente o que pode e não pode tocar.

---

## 10. Se algo não funcionar

| Sintoma | Causa provável | Solução |
|---|---|---|
| Página em branco | Browser antigo | Usa Chrome ou Edge |
| Setas a desaparecer | Janela muito pequena | Usa **AJUSTAR** ou aumenta a janela |
| Nós sobrepostos após update | Geometria mal calculada | Revê `x, y, w, h` dos nós novos no bloco DATA |
| Painel não atualiza | Erro JS no bloco DATA | Abre a consola do browser (F12) e lê o erro |
| Tour não avança | `tour` com id inválido | Verifica os ids no array `tour` da vista |

Para erros de conteúdo, o ficheiro de backup `2-dashboard/DIAGRAMAS-governo-dashboard_v1-backup.html` tem a versão original.

---

*Fim do Manual de Uso · Dashboard Governo AI · 2026-06-11*
