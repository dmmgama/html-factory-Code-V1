---
created: 2026-06-18
project: html-artifact-factory
session: preparação do grill (M2) — passagem de leitura
status: relatorio
autor: subagente Opus (segunda opinião, independente)
summary: >
  Segunda opinião independente sobre o material da SArq-3 (docs/ideia-design), produzida
  sem ler o RELATORIO-ideia-design.md do outro agente. Leitura na ordem mandada, cruzada
  com o mapa M1 e com o ficheiro real do curador. Estrutura de 6 eixos + resposta às 4
  dúvidas do David. Só leitura + este relatório; não decide tensões, não aplica patches.
---

# Relatório-fork — leitura da "ideia-design" antes do grill

> **Aviso de independência.** Este relatório é uma **segunda opinião**. Não li o
> `RELATORIO-ideia-design.md` do outro agente — formei a visão só a partir do material-fonte
> da pasta, cruzado com o meu mapa M1 (`docs/mapa-artefactos.md`) e com o ficheiro real do
> curador. Onde eu **divergir** ou **acrescentar**, marco com **[DIVERGE]** / **[ACRESCENTA]**.
> Linguagem Ubíqua sempre com tradução civil (o David é arquitecto, não-programador).

---

## Eixo 1 · Entendimento (em linguagem minha)

A arquitectura que a SArq-3 fechou tem uma frase-mãe: **a planta declara, o Code constrói.**
O David deixa de mudar o frontend por *prosa* ("mete o grafo à esquerda e a tabela à direita")
e passa a mudá-lo por uma **planta declarativa** (o **Manifesto**, `workspace.json`). O Code
lê a planta, vai à biblioteca buscar os **Blocos** reais (peças vivas, que lêem dados) e
ergue o **HTML single-file** final, offline.

O que a SArq-3 acrescentou de novo, face à SArq-2, foi sobretudo **nomear e separar duas
naturezas de peça** que antes andavam misturadas — e é aqui que está a verdadeira inteligência
do trabalho:

- **Chassis = peça MORTA.** É a casca: barra superior, abas, divisórias, caixas vazias. Não
  lê dados. *(Civil: as paredes e divisões da casa, ainda sem mobília.)*
- **Bloco = peça VIVA.** É o grafo, a árvore, a tabela — ligado ao SSOT, faz coisas. *(Civil:
  a mobília que se mete dentro de cada divisão.)*

E inventou o **fio que costura as duas:** o **Slot**, um número (`data-slot="3"`) que nasce
no desenho/planta e **viaja** intacto até ao Code. O Code lê "slot 3 → bloco-grafo" e injecta
a peça viva no lugar certo. *(Civil: o número da porta de cada divisão — morada fixa para o
empreiteiro saber onde pôr o quê.)* É uma ideia simples e robusta: o número é o contrato
mínimo entre quem desenha e quem constrói.

Há ainda a **Silhueta** — a maqueta de cartão de um Bloco. Existe por uma razão técnica
específica: o Claude Design é um *gerador* (reinterpreta tudo o que recebe), portanto se lá
metesses um Bloco real ele **regenerava-o e corrompia-o**. Logo monta-se o layout com
silhuetas descartáveis e o Code troca silhueta→bloco real no fim.

**O que mudou face à SArq-2 (li o doc de transição):** nada foi anulado, foi **completado**.
A SArq-2 tinha fechado 6 alicerces (Caixas, Alfândega, Config, Isolamento Acústico, Ciclo
Reativo, Motor de 3 modos) e deixado **um buraco explícito de alta prioridade**: "forma ágil
de mudar o frontend". O Isolamento Acústico já dava o *endereço* ("muda aquilo" tinha morada);
faltava a *linguagem* (como o David formula a mudança). A SArq-3 tapou esse buraco com o
**Manifesto** e desenhou o **fluxo de operação** (planta→Code) que antes estava implícito.

**Prova de que percebi — o ponto mais subtil:** os **3 modos do Motor** (relações /
hierarquia / tabela) **não são 4**. "Grafo" e "árvore" são **vistas** (coisa do Viewer), não
modos: grafo = relações + hierarquia; árvore = relações restritas (arestas só pai→filho).
Isto não é pedantismo de vocabulário — tem consequência directa na Alfândega (quantos
contratos: um, ou um-por-modo). Voltarei a isto no Eixo 3.

---

## Eixo 2 · Ligação ao meu mapa (M1)

O material da SArq-3 **encaixa bem** no que eu mapeei, e em vários pontos o M1 dá-lhe
fundação dura. Mas há **uma peça que a SArq-3 assume e o M1 confirma ser genuinamente nova**,
e há **uma divergência factual** que tenho de assinalar.

**Onde os artefactos favorecem a SArq-3:**

- **As 4 peças da fábrica já existem na natureza, dispersas** (insight central do M1 §5): o
  melhor *contrato de dados* está no **TableEditor** (envelope Frictionless), o melhor
  *viewer-cego* na classe **`FloorViewer`** (`loadData()` + Canvas), o melhor *Ciclo Reativo*
  no **curador-v3** (`commit()=save()+renderAll()`), e o melhor *formato de grafo* no
  **`knowledge-graph.json`** (nós+arestas limpos). A SArq-3 está certa em dizer "não começar
  do zero" — há mina real.
- **O curador continua a fazer sentido como piloto/mina.** [ACRESCENTA] com um cuidado de
  precisão: a SArq-3 fala do curador como "mina de **blocos**" (andar 1) e *não* como template
  de dashboard (andar 2 — as 4 abas são hardcoded). O M1 §6 confirma o **grafo como piloto** e
  recomenda como ponto de partida o `knowledge-graph.json`, **não** o curador, para o *contrato
  de dados* do grafo. Ou seja: o curador é mina do **Ciclo Reativo e dos viewers**, mas o
  **formato** de grafo mais limpo para copiar é o `knowledge-graph.json`. São minas diferentes
  para fins diferentes — vale a pena não as confundir.

**Onde o M1 dá fundação ao invariante da Imutabilidade (responde à dúvida 1, abaixo):**
o M1 §7 diz, taxativamente, que **nenhum** dos artefactos tem hoje passo de compilação — são
todos single-file editados à mão. Isto confirma que **o passo de compilação módulos→HTML é a
única peça genuinamente nova de toda a arquitectura**, e é o que torna a Imutabilidade
*verificável* em vez de só *decretada*.

**[DIVERGE] A divergência factual — tabela de blocos do curador (secção 5 da SArq-3).**
A SArq-3 lista 7 blocos do curador com função **e número de linha**. Fui conferir no ficheiro
real (`Artefactos-existentes/Projetocurador html/projetos-curador-v3.html`) e **as linhas
estão todas erradas**, por uma margem grande e sistemática (≈140–290 linhas de desvio):

| Função | SArq-3 (cópia web) | Ficheiro REAL | Desvio |
|---|---|---|---|
| `renderFilterBar` | 820 | **680** | −140 |
| `renderHead` | 887 | **747** | −140 |
| `renderBody` | 1088 | **948** | −140 |
| `renderGraph` | 1275 | **1081** | −194 |
| `renderCronologia` | 1485 | **1255** | −230 |
| `renderGenealogy` | 1502 | **1272** | −230 |
| `makeProjCard` | 1691 | **1402** | −289 |
| `renderAsgMindmap` | 1872 | **NÃO EXISTE** | ausente |

Duas conclusões:

1. **A nota de proveniência da SArq-3 estava certíssima** (e o `PatchGlossario` secção D
   também): as linhas vieram de uma cópia web e **não são verdade**. Está agora **provado**,
   não só suspeitado. Antes de qualquer extracção, conferir no ficheiro real — manda o M1.
2. **[DIVERGE] mais grave: `renderAsgMindmap` não existe no ficheiro real.** O mind-map do
   curador **não é um bloco/função separada** — é um *modo* dentro do próprio `renderGraph`
   (`if(UI.graphMode==="mindmap")`, com `computeMindmapLayout()` na linha 1043). Isto é a
   **prova viva** da tese central do Glossário: o mind-map é uma **vista do modo relações**,
   não um bloco autónomo. A SArq-3, ao listá-lo como 7.º bloco com linha própria, **fabricou
   uma peça que não existe na natureza**. Quem extrair blocos do curador a partir da lista da
   SArq-3 vai procurar uma função que não está lá. **Corrigir antes do grill.**

Fora isto, **nada no material contradiz os invariantes**. A SArq-3 respeita single-file,
separação estanque e estética-fora-dos-dados; e o M1 §4 reforça onde os artefactos *quebram*
o último (dossier, governance-explorer, MAPA-EXPLORADOR, zonas metem cor no dado) — munição
para a Alfândega proibir isso de raiz.

---

## Eixo 3 · Tensões e riscos (o que me preocupa, e onde nasce torto)

São 4 tensões em aberto (Alfândega genérica, Desacoplamento, Auxiliar/espelho, Editor). Por
ordem de preocupação:

**1. T2 — Alfândega genérica (a que mais me preocupa).** É a **peça-mãe**: se ficar bem,
os Blocos tornam-se reutilizáveis; se ficar mal, ficam presos a um caso ou a Alfândega vira
"tudo e nada". A pergunta dura, que o M1 §7 já formula: **um contrato único** para os 3 modos,
ou **um contrato por modo** com um núcleo partilhado `{id,type,label,meta}`? O risco de nascer
torto está nos dois extremos: um contrato único hiper-abstrato não restringe nada (deixa de
ser alfândega); três contratos sem núcleo comum perdem a reutilização. **A minha leitura**
(não é decisão — é do David): a evidência do M1 puxa para **núcleo comum + perfil por modo** —
a árvore é um grafo restrito, a tabela é mesmo outra coisa (Frictionless). Mas isto fecha-se
**a partir do caso real** (o grafo-piloto), nunca em abstracto. Construir a Alfândega genérica
antes de ter um bloco a funcionar é o caminho clássico para a abstracção-no-vácuo.

**2. T1 — Desacoplamento.** Os Blocos do curador estão colados ao **STATE global** e ao SSOT
específico de projetos-AI. Para virarem biblioteca, cada um tem de ler um contrato *genérico*.
O M1 confirma que os moldes de extracção existem (`commit()=save()+renderAll()`,
`FloorViewer.loadData()`), mas **desacoplar é trabalho real**. Risco de nascer torto: tentar
desacoplar **tudo de uma vez**. A recomendação do auditor (um **bloco-piloto = grafo**, provado
fora do curador, e só dele derivar a Alfândega) é a salvaguarda — e alinha com o M1 §6.

**3. T4/Editor — risco de decidir cedo demais** (ver Eixo 4, e responde à dúvida 2).

**4. Auxiliar/espelho** — ver dúvida 4. É a que **menos** me preocupa; parece subsumida.

**O elo frágil do Claude Design (import/export preservar os Slots) — como o provaria.**
Este é o ponto único de falha dos candidatos D-sil e D-proc, e o material já o assinala (o
banner "⚠ ELO A PROVAR PRIMEIRO" no `fluxo-D-proc.svg`; o ponto 4 do ADDON). O Claude Design
é um *gerador*: nada garante que, ao traduzir desenho→HTML, **preserve os números dos Slots
legíveis** para o Code. **Como eu provaria, antes de assentar qualquer fluxo nele:**

1. **Teste mínimo, não trivial-de-mais.** Um Chassis com **3–4 Slots**, incluindo um caso
   chato de propósito: Slots **não-sequenciais** (1, 2, 5), um Slot **aninhado** (caixa dentro
   de aba) e dois Slots **lado a lado** (para ver se ele os funde).
2. **Round-trip, não ida só.** Exportar → o Code tenta parsear os `data-slot="N"` → re-importar
   o resultado → exportar outra vez. Se os números **sobrevivem a dois ciclos** sem deriva, o
   elo aguenta. Se já à primeira o Claude Design renomeia/funde/perde números, **falhou** e o
   David sabe-o com um teste de 20 minutos, não depois de construir o M9.
3. **Critério de passa/chumba explícito:** o Code consegue mapear **100%** dos Slots desenhados
   para Blocos sem intervenção manual. Menos de 100% = não é "editor", é "editor + remendo à
   mão" — o que mata o critério-mãe (simplificar).

[ACRESCENTA] Este teste deve correr **antes** do M9 e idealmente antes mesmo de o David
investir quota Opus em sessões de design. É barato e elimina o maior risco dos candidatos
mais sedutores.

---

## Eixo 4 · Candidatos a editor (a minha recomendação para o grill — não decido)

Há um detalhe de **contagem** a assinalar primeiro: **[DIVERGE/ACRESCENTA]** o ADDON e os
3 PatchCDesign falam de **3 candidatos** (Claude Design+silhuetas, manifesto-em-texto,
Gridstack); mas o `fluxo-1-arquitetura.svg` e o Glossário introduzem um **4.º — o D-proc**
(Chassis desenhado no Procreate → Claude Design traduz → Code injecta). O David, na ordem de
trabalho, fala-me em **4**. Ou seja, há uma **inconsistência de número** entre documentos
(3 vs 4) que o grill deve reconciliar. Eu trato os 4:

| Candidato | O que é (civil) | A favor | Contra |
|---|---|---|---|
| **(a) Claude Design + Silhuetas (D-sil)** | Montas a maqueta de cartão na própria mesa de design; o empreiteiro troca cartão por móveis | Visual, rápido de iterar, lê identidade visual | Research preview (bugs), custo Opus, **import/export dos Slots por provar** |
| **(b) Manifesto-em-texto** | Escreves a planta à mão (`workspace.json`) | Barato, sempre disponível, zero dependências, alinha com "manifesto primeiro" (D4) | Sem conforto visual; o David escreve estrutura à mão |
| **(c) D-proc (Procreate→Claude Design)** | Desenhas a planta à mão no iPad com portas numeradas; o tradutor passa-a a HTML | Desenho natural para o David, biblioteca de chassis cresce por acumulação | **Dois** elos a provar (Procreate→Design e Design→Code); mais peças móveis |
| **(d) Gridstack / editor próprio** | A prancheta drag-and-drop construída de raiz | Controlo total, sem dependência da Anthropic | Provavelmente o mais caro; arquivado por design (pode "emergir" por acumulação) |

**A minha recomendação fundamentada para levar ao grill** (sublinho: a decisão é do David,
desempate pelo critério-mãe):

> **Arrancar por (b) manifesto-em-texto**, e tratar (a)/(c) como **upgrade de conforto** a
> validar com o teste de import/export *antes* de adoptar. (d) fica arquivado.

Porquê: o **valor nuclear** ("montar sem re-explicar ao agente") obtém-se **já** com o
manifesto em texto — é o que a própria SArq-3 conclui (D4: "manifesto-em-texto primeiro;
inverter a ordem é o caminho para o pântano"). Os candidatos visuais são **conforto adicional**,
não requisito; e arrastam o único risco que pode fazer a fábrica "nascer torta" (o elo dos
Slots). Começar pelo barato-e-certo, e só depois comprar conforto, é exactamente o critério-mãe
(simplicidade > completude > elegância). **Isto também responde à dúvida 2** (ver abaixo): o
grill deve fechar o Editor só até **"direção + teste-gate"**, não cravar a ferramenta final.

---

## Eixo 5 · Patches — recomendação (recomendo; não aplico)

São 4: 3× **PatchCDesign** (context / roadmap / CLAUDE) + **PatchGlossario-integracao**.

**Avaliação geral: bem feitos e fiéis ao material.** Todos se apresentam, correctamente, como
**"candidato a estudar"**, não como decisão — respeitam o invariante "não decidir as tensões
sozinho". Aplicá-los-ia **quase como estão**, com **três ressalvas**:

1. **[DIVERGE] Os 3 PatchCDesign falam de 3 candidatos; o David e os SVGs falam de 4** (falta
   o D-proc). Antes de aplicar, **acrescentar o D-proc** à lista de candidatos nos três patches
   (context §6, roadmap M2/M9, CLAUDE.md "NÃO fazer"), ou o registo de continuidade fica a
   contradizer os diagramas. Não reescrevia o resto — só fecharia esta lacuna de contagem.

2. **PatchGlossario secção D (proveniência) — confirmo e reforço.** A nota está certa, e agora
   **provei-a** (Eixo 2): as linhas do curador divergem 140–290 linhas e `renderAsgMindmap`
   nem existe. **Reforço sugerido ao texto do patch:** acrescentar a tabela de desvios reais
   e, sobretudo, a correcção do mind-map (é *modo* de `renderGraph`, não bloco). Tal como está,
   o patch diz "as linhas podem divergir"; eu mudaria para "as linhas **divergem** (provado) e
   a lista de 7 blocos tem **um bloco fantasma** (`renderAsgMindmap`) — usar a tabela real".

3. **PatchGlossario B3 / roadmap (reconciliação modos vs. vistas) — manter, é importante.**
   O patch já manda alinhar "3 modos (relações/hierarquia/tabela)" vs. "grafo/árvore/tabela"
   que o meu M1 escreveu. **Concordo e é meu também o erro a corrigir:** o M1 usou "grafo/árvore"
   como rótulos de modo por comodidade; o vocabulário canónico do Glossário é melhor. A prova do
   mind-map-como-modo (Eixo 2) sela isto.

Sobre a **migração da tabela de Linguagem Ubíqua do CLAUDE.md para o Glossário** (PatchGlossario
A3): o patch deixa-a, bem, como **decisão do agente no grill** e não a força. Concordo em não a
fazer agora — é mexer no canon (CLAUDE.md) numa passagem que é só de leitura. [ACRESCENTA] mas
sinalizo um risco de **deriva de fonte-única**: enquanto a tabela viver no CLAUDE.md *e* no
Glossário, há **duas fontes** do vocabulário e podem divergir. O grill devia decidir
explicitamente: ou o CLAUDE.md só aponta (e a tabela esvazia-se), ou fica um atalho mínimo
declarado como não-canónico. Não decidir isto deixa um foco de incoerência futura.

**Não apliquei nenhum patch** (limite desta passagem).

---

## Eixo 6 · O que falta / perguntas para o grill

**Ambiguidades a fechar no grill:**

1. **3 ou 4 candidatos a editor?** Inconsistência real entre os PatchCDesign (3) e os SVGs +
   ordem do David (4, com D-proc). Reconciliar a contagem.
2. **A Alfândega: um contrato ou um-por-modo?** (T2) — a decisão-mãe, a fechar a partir do
   grafo-piloto, não em abstracto.
3. **Imutabilidade (T3): decretada ou verificada?** O passo de compilação aparece nos
   invariantes e como tensão, **mas não como peça desenhada** com lugar no fluxo. Ver dúvida 1.
4. **Auxiliar/espelho: morre como peça ou sobrevive?** (dúvida 4) — a transição diz "subsumido",
   mas deixa-o como tensão a confirmar com o David.
5. **Fonte-única do vocabulário:** CLAUDE.md aponta-só ou guarda atalho? (risco de deriva).
6. **Método do desacoplamento (T1):** bloco-piloto vs. tudo-de-uma-vez — não decidido.

**Perguntas minhas (que eu próprio levanto):**

- **[ACRESCENTA] O passo de compilação tem dono e lugar?** Está nos invariantes e em T3, mas
  nunca aparece como **caixa no fluxo** (o `fluxo-1` salta de "Manifesto" para "HTML
  single-file" sem desenhar o *build* como peça). Vejo aqui o maior risco de **cair no
  esquecimento** — ver dúvida 1.
- **A "folha de binding" e o Slot encontram-se onde?** O Slot diz *onde* vai o bloco; a folha
  diz *que dados* mostra. São dois mapas (forma e conteúdo). O material trata-os em separado,
  mas não diz como se cruzam no Code (o Slot 3 é grafo *e* a folha diz "grafo mostra estes
  campos"). Provavelmente trivial, mas vale uma frase no grill.
- **O `knowledge-graph.json` vs. curador como fonte do contrato de grafo:** o M1 recomenda o
  primeiro para o *formato*; a SArq-3 enfatiza o curador. Confirmar qual é o ponto de partida
  do contrato do grafo-piloto (eu diria: formato do `knowledge-graph.json`, ciclo reativo do
  curador).

---

## Anexo · Resposta directa às 4 dúvidas do David

**Dúvida 1 — Passo de compilação (Imutabilidade): tratado, assumido, ou no ar? Risco de cair
no esquecimento?**

**O material assume-o, mas não o desenha — e sim, vejo risco real de esquecimento.** Concordo
com a tua síntese: é a **única peça genuinamente nova** de toda a arquitectura, e o M1 §7
confirma-o de forma dura (nenhum artefacto tem compilação hoje). A SArq-3 trata-o **só como
invariante e como tensão T3** ("Imutabilidade decretada, não verificada; mitigação build
stamp/hash NÃO decidida"), herdada da SArq-2. **Mas em lado nenhum o passo de compilação
aparece como peça com lugar no fluxo:** o `fluxo-1-arquitetura.svg` vai de "Manifesto" direto
para "HTML single-file", e a caixa "CONSTRUÇÃO (Code)" descreve injecção de blocos, não um
*build* identificado. O Glossário menciona-o só no atalho dos invariantes (linha "exige passo
de build"). **Risco concreto:** como vive só como invariante abstracto e não como caixa
desenhada nem como marco no roadmap M3–M9, é fácil o incremento vertical chegar ao fim "a
funcionar" sem nunca ter materializado a fronteira módulos→single-file — e aí a Imutabilidade
fica decretada mas inexistente. **Recomendação para o grill:** dar ao passo de compilação um
**lugar explícito** (uma caixa no fluxo + um marco no roadmap), nem que seja mínimo, e fechar
T3 ao menos até "build stamp/hash sim ou não". É a peça que, por ser a única nova, mais merece
não ficar implícita.

**Dúvida 2 — Editor: o grill deve fechá-lo só até "direção + teste-gate", sem cravar a
ferramenta final?**

**Concordo plenamente.** O grill deve fechar o Editor a **"manifesto-em-texto primeiro
(direção) + teste de import/export como gate"** e **não** cravar agora a ferramenta final. Três
razões: (1) o **piloto = grafo não precisa de editor** — precisa de Caixa+Alfândega+1 bloco a
render dados reais (M3 do `fluxo-2`); o editor é o M9, marco distante. (2) O valor nuclear
("montar sem re-explicar") já se obtém com o manifesto-em-texto — a própria SArq-3 conclui isso
(D4). (3) Cravar Claude Design ou Gridstack agora seria comprar o risco do elo dos Slots antes
de saber se o piloto sequer existe. **A formulação que recomendo:** manifesto-em-texto como
base; Claude Design / D-proc presos a **passar o teste de preservação dos Slots** (round-trip,
100% mapeável) antes de serem adoptados; Gridstack arquivado, podendo emergir por acumulação.
Decidir mais do que isto no grill é decidir cedo demais.

**Dúvida 3 — Proveniência das linhas do curador.**

**Confirmado e provado: as linhas da SArq-3 divergem e não devem ser usadas.** Fui ao ficheiro
real e as 7 linhas citadas estão **todas erradas** (desvio sistemático de 140–290 linhas — ver
tabela no Eixo 2), e **`renderAsgMindmap` nem existe** (o mind-map é um *modo* de `renderGraph`,
linha 1043, não uma função separada). O `PatchGlossario` secção D já avisava disto; agora está
**provado**, não suspeitado. Onde o material depender destas linhas (sobretudo a secção 5 da
SArq-3 e qualquer encomenda de extracção de blocos), **re-verificar no ficheiro real — manda o
M1.** Reforço: usar a **tabela de linhas reais** que deixo no Eixo 2, e corrigir o **bloco
fantasma** do mind-map antes de qualquer extracção.

**Dúvida 4 — "Auxiliar/espelho": peça própria ou subsumido por manifesto+binding?**

**A minha leitura: está subsumido, e bem — mas mantém-no como pergunta de confirmação ao
David, não como peça.** A transição (secção 5) diz que o papel de "instrumento de comunicação
com o agente" passou para a dupla **manifesto + folha de binding**, e o M1 §7 dá-lhe fundação
independente: o **TableEditor já pratica "canais à la carte"** (compõe schema/tipos/view por
destino, com `x-tableeditor` para round-trip) — ou seja, há **precedente real** de que o espelho
pode ser uma **vista derivada do mesmo SSOT**, não uma peça separada. **Convergência clara entre
SArq-3 e M1.** A única coisa que falta é o David **confirmar** que não quer um 2.º artefacto
dedicado a mostrar relações durante o desenvolvimento. Enquanto não confirmar, fica como tensão;
mas a arquitectura não precisa dela como peça autónoma. **Não a ressuscitaria** sem o David pedir.

---

*Fim do relatório-fork. Só leitura + este ficheiro. Não apliquei patches, não decidi tensões,
não construí código. As decisões são do David, no grill.*
