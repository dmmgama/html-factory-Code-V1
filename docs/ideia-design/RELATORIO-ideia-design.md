---
created: 2026-06-17
project: html-artifact-factory
chat: Leitura da ideia-design antes do grill (resposta à ordem agente-lerIdeia.md)
session: S1 (Code) ← absorve SArq-3 (arquitectura)
status: relatorio
summary: >
  Relatório de leitura do material da SArq-3 (docs/ideia-design), pela ordem mandada,
  ligado ao mapa M1 já feito. Só leitura + entendimento + recomendações; não aplica
  patches, não corre o grill, não constrói código.
---

# Relatório — leitura da "ideia-design" antes do grill

> Resposta à ordem `agente-lerIdeia.md`. Li, por ordem: Glossário → fluxo-1 → transição
> SArq-2→SArq-3 → cristalização SArq-3 → ADDON Claude Design → fluxo-D-proc → fluxo-2 →
> os 3 patches. Liguei tudo ao **mapa M1** que esta sessão (Code) já produziu. Não apliquei
> patches, não corri o grill, não escrevi fora desta pasta. Linguagem Ubíqua + tradução civil.

---

## 1. Entendimento — o que a SArq-3 fechou

**Em uma frase:** a SArq-3 **não substituiu** nada; tapou o único buraco que a SArq-2 tinha
deixado aberto — *"uma forma ágil de mudar o frontend"* — e, ao fazê-lo, deu nome e lugar à
peça que faltava (o **Manifesto/planta**) e ao **fluxo de operação** que estava implícito.

**O fluxo nuclear (a planta declara, o Code constrói):**
```
o David declara          →   eu (Claude Code) construo        →   resultado
PLANTA: Chassis + Slots      leio a planta, pego nos BLOCOS        HTML single-file
+ Manifesto (workspace.json) reais da biblioteca, injecto-os       offline, a funcionar
+ Folha de binding           nos Slots, ligo ao SSOT, aplico Config
```

**A peça-charneira é a distinção VIVO vs MORTO** (a regra que mantém o puzzle limpo):
- **MORTO = Chassis** — paredes, abas, divisórias, caixas vazias *numeradas*. Não lê dados.
  Vive na **planta** (é o que o editor produz). Em civil: as divisões do edifício, vazias.
- **VIVO = Bloco** (`{Motor + Viewer}`) — o tijolo que lê o SSOT e faz coisas. Vive **no Code**,
  nunca no editor. Em civil: o móvel a sério, montado pelo empreiteiro.
- **O fio que liga os dois é o Slot** (`data-slot="3"`): a *morada* numerada de cada lugar,
  que nasce na planta e **viaja** até mim ("slot 3 → bloco-grafo"). Instância única, nunca tipo.

**Decisões fechadas (D1–D8 da cristalização):** critério-mãe a desempatar tudo (D1); fluxo
planta→Code, blocos no Code e não no editor (D2 — rejeitado o "caminho-monstro" de meter blocos
vivos no editor); Manifesto = a linguagem de mudança (D3); editor drag-and-drop **adiado**,
manifesto-em-texto primeiro (D4); binding por **folha meio-preenchida com menus** — o David
*escolhe*, não *escreve* — descartável, promove-se só se reconfigurar a toda a hora (D5); plano
de 2 fases e o **executor da extração é o Code + subagentes** (`html-expert`, `ui-designer`),
**não** o `understand-anything` (D6); curador = **mina de blocos** (andar 1), não template (D7);
a biblioteca começa pelos **Blocos**, os Arranjos-tipo (andar 2) ficam adiados (D8).

**O que mudou face à SArq-2:** os 6 alicerces (Caixas, Alfândega, Config, Isolamento Acústico,
Ciclo Reativo, Motor-3-modos) ficaram **intactos**; ganharam o mecanismo que faltava (Manifesto)
e três peças novas de operação: Manifesto, Folha de binding, e o fluxo planta→Code. O
"Auxiliar/espelho" foi **subsumido** pela dupla manifesto+binding (deixa de ser peça própria — só
fica a *tensão* de confirmar contigo se desaparece mesmo).

**Vocabulário NOVO que a SArq-3 traz** (não estava no meu M1): **Chassis**, **Slot**, **Silhueta**,
e a clarificação importante de que **"grafo" NÃO é um 4.º modo do Motor** — é `relações + hierarquia`.
Os 3 modos canónicos são **relações / hierarquia / tabela**.

---

## 2. Ligação ao meu mapa (M1) — encaixa, e reforça

O material da SArq-3 e o meu [mapa dos artefactos](../mapa-artefactos.md) **convergem fortemente** —
foram feitos em paralelo e chegaram às mesmas conclusões nucleares:

| Conclusão | SArq-3 | Meu M1 | Veredicto |
|---|---|---|---|
| Curador **v3** é a fonte de blocos / referência | sec. 5 ("mina de blocos") | D9 + ficha detalhada | **Igual** |
| Alfândega nasce do SSOT do curador, a generalizar | T2 | §3/§7 | **Igual** |
| Blocos acoplados ao STATE global → desacoplar é trabalho real | T1 | §3/§5/§7 | **Igual** |
| O grafo é o bloco-piloto (mais valioso e difícil) | sec. 9 | §6 | **Igual** |
| Passo de compilação é genuinamente novo (nenhum artefacto o tem) | T3 | §7 + síntese visual | **Igual** |
| `understand-anything` **não** serve para extrair (single-file, deu mapa vazio) | sec. 4 | (implícito: usei Explore/code-reviewer, não o skill) | **Igual — valida o método do M1** |

**O curador continua a fazer sentido como piloto/mina? Sim, e com mais detalhe.** A SArq-3 já
identifica **7 blocos** no curador com função (e linha aproximada): grafo (`renderGraph`), árvore
(`renderGenealogy`), timeline (`renderCronologia`), tabela (`renderHead`/`renderBody`), filtros
(`renderFilterBar`), card (`makeProjCard`), mind-map (`renderAsgMindmap`). O meu M1 tinha dito
"motor puro / viewer acoplado, cor *hardcoded* em `renderGraph`" — bate certo: são exatamente
estes os blocos a desacoplar.

**Há blocos/peças que contrariam o que a SArq-3 assumiu?** Não em substância. Mas há **dois
desalinhamentos de vocabulário/factos a reconciliar no grill** (sinalizo, não resolvo):

1. **"3 modos" — etiquetas diferentes.** O meu M1 escreveu os 3 modos como **grafo / árvore /
   tabela**. O Glossário (dono do vocabulário) diz **relações / hierarquia / tabela**, e que
   *grafo não é modo* (é um tipo de Bloco = relações+hierarquia). Não é contradição de fundo — é
   precisão de linguagem. **Recomendo alinhar o M1 ao Glossário** quando o grill abrir.
2. **Números de linha do curador divergem.** A SArq-3 cita `renderGraph` na **linha 1275** (e
   v3 com ~blocos nessas linhas); o subagente que leu o v3 para o meu M1 citou `renderGraph` na
   **linha ~1131** e v3 com ~1924 linhas. Podem ser cópias/versões ligeiramente diferentes (há
   `v3`, `v3O`, e o mapa `curador-arquitetura-dashboard.html`). **As linhas exatas têm de ser
   re-verificadas contra o `projetos-curador-v3.html` atual antes da extração (M3)** — não confiar
   em nenhum dos dois números às cegas.

> Nota de nomes: a SArq-3 chama ao mapa do curador `curador-dashboard.html`; na pasta o ficheiro
> é `curador-arquitetura-dashboard.html` (e há `dashboard-v3.html`). Pequena deriva de nome a
> confirmar.

---

## 3. Tensões e riscos — o que me preocupa mais

As 4 tensões do grill, por ordem de preocupação minha:

**T2 — Alfândega genérica (a que mais me preocupa; é a peça-mãe).** Aqui é onde o factory pode
"nascer torto". O meu M1 mostrou que o domínio **bifurca**: o grafo/árvore cabem num contrato
nó+aresta, mas a **tabela** é outra coisa (envelope Frictionless do TableEditor). Se a Alfândega
for forçada a *um* contrato único para os três, arrisca ficar "tudo e nada" (abstração no vácuo —
viola o critério-mãe). Se for *um por modo*, há mais peças mas cada uma limpa. **Esta é a decisão
de arquitectura mais cara de desfazer** e devia fechar-se primeiro, com o caso real do curador à
frente — exatamente como SArq-3 (T2) e o meu M1 dizem.

**T1 — Desacoplamento.** Risco médio mas trabalho real. Os blocos do curador estão colados ao
`STATE` global e ao SSOT específico de projetos-AI. O molde de extração existe (o ciclo
`commit()=save()+renderAll()` e o `FloorViewer.loadData()` do `projeto-ssot`), mas o método —
*um bloco-piloto* (grafo) vs. *todos de uma vez* — **não está decidido**. Recomendo **piloto-só**
(é o que de-risca sem comprometer): provar o grafo fora do curador e só então generalizar.

**Editor.** Risco concentrado num ponto: o **elo frágil do Claude Design** (ver §4). Não é risco
de "nascer torto" na fundação — o editor serve só a planta, nunca a fundação — mas é onde se pode
gastar tempo num caminho que não fecha.

**T3 — Imutabilidade verificada.** Risco baixo agora, mas real: hoje a imutabilidade é *decretada*,
não *verificada* — nada deteta uma edição direta ao `dist/`. Mitigação proposta (build stamp/hash
das fontes) não decidida. Fica para quando existir build.

**O elo frágil do Claude Design — como o provaria.** O passo crítico é o **import/export**: o
layout exportado pelo Claude Design ser **legível e estável** o suficiente para eu mapear
*silhuetas → blocos reais* pelos Slots. Como prova mínima (antes de assentar qualquer coisa):
1. Montar um **layout trivial** (2–3 zonas numeradas, silhuetas-retângulo).
2. Exportar (HTML/handoff).
3. Confirmar que consigo **parsear o output e ler os `data-slot` de forma fiável** — i.e. que o
   "slot 3" que o David desenhou chega a mim como "slot 3", não regenerado nem renomeado.
4. Repetir com um re-export depois de uma pequena alteração, para ver se os Slots **persistem**
   (o elo é a *estabilidade*, não só a *legibilidade*). Só se isto passar é que o candidato vive.

---

## 4. Candidatos a editor — leitura e recomendação (não decisão)

São **4** (o fluxo-1 e o ADDON juntos):

| Candidato | O que é | A favor | Contra |
|---|---|---|---|
| **(a) Claude Design + silhuetas (D-sil)** | montar layout no Claude Design com silhuetas; eu troco por blocos reais | visual, gera HTML a sério, handoff para o Code | research preview (bugs), custo Opus, **import/export por provar**, deriva estética |
| **(b) D-proc (Procreate)** | desenhas o Chassis numerado à mão no iPad → Claude Design traduz → eu injeto | encaixa no teu modo de pensar (desenho); biblioteca de chassis cresce | **mais peças móveis** (2 traduções); o mesmo elo import/export + risco de OCR dos números |
| **(c) Manifesto-em-texto** | editar `workspace.json` à mão | **barato, sempre disponível, zero tooling novo**; prova já o pipeline planta→Code | menos confortável que arrastar; exige ver a planta como texto |
| **(d) Gridstack / editor próprio** | editor drag-and-drop construído | conforto de arrastar | o mais caro a construir à cabeça; "pode emergir por acumulação" |

**A minha recomendação fundamentada para levar ao grill** (desempate pelo critério-mãe — *qual
reduz mais o atrito sem puxar para "semanas a montar"*):

> **Arrancar com (c) manifesto-em-texto** como editor v0. É o único que prova o fluxo
> planta→Code **sem introduzir risco novo** (nenhuma ferramenta externa, nenhum elo por provar).
> Tira-se logo o valor nuclear ("mudar o frontend editando a planta, não re-explicando").
>
> **Em paralelo, tratar (a) Claude Design + silhuetas como o upgrade mais promissor** — mas
> *gated* no teste de import/export (§3). Só fecha como decisão depois de o elo passar.
>
> **(b) D-proc é o mais sedutor para ti** (és arquitecto, desenhas) e tem o bónus de acumular
> uma biblioteca de chassis — mas tem **o dobro dos pontos de falha** do (a) (Procreate→tradução
> →Code + leitura de números desenhados). Recomendo avaliá-lo **depois** de (a), e só se o elo
> import/export do Claude Design já estiver provado (ambos dependem do mesmo passo).
>
> **(d) Gridstack fica por último** — deixá-lo *emergir* quando a biblioteca de chassis já o
> tornar trivial, em vez de o construir especulativamente.

Isto é coerente com a própria D4 da SArq-3 (manifesto-em-texto primeiro, arrastar adiado).
**Decisão é tua, no grill** — eu só recomendo.

---

## 5. Patches — recomendação (não apliquei)

Os 3 `PatchCDesign-*` propõem acrescentar o **Claude Design como candidato** (não decisão) aos
ficheiros de continuidade. Verifiquei-os contra os ficheiros reais:

- **`PatchCDesign-context.md`** → substitui a linha "Editor" da §6. **Bate certo** com o texto
  atual do `context.md`. Bem redigido, framing "candidato" correto. **Aplicaria como está.**
- **`PatchCDesign-roadmap.md`** → atualiza o Editor no M2 e reescreve o M9. **Aplicável** (o meu
  `roadmap.md` tem ambos os pontos). Boa adição do *teste import/export como pré-requisito do M9*.
  Pequeno ajuste: a minha lista de tensões do M2 está em texto corrido, não em bullet "Editor"
  isolado — basta adaptar a localização.
- **`PatchCDesign-CLAUDE.md`** → acrescenta a nota dos 3 candidatos na linha do "NÃO fazer".
  **Bate certo** e mantém o framing "candidato, não verdade". **Aplicaria como está.**

**Veredicto:** os 3 patches refletem bem o material e estão honestamente marcados como "candidato".
**Recomendo aplicá-los** (com o micro-ajuste de localização no roadmap) **quando arrancarmos o
grill** — não agora, porque esta passagem é só de leitura.

**Mas os patches são pequenos demais para tudo o que a SArq-3 traz.** Eles só tratam a tensão
*Editor*. Ficam de fora, e merecem decisão no grill:
- **O Glossário** declara-se "dono do vocabulário" e diz que o `CLAUDE.md`/`context.md` devem
  *apontar* para ele, não repetir definições. O meu `CLAUDE.md` tem a sua própria tabela de
  Linguagem Ubíqua. **Há que decidir:** o `CLAUDE.md` passa a apontar para o `GLOSSARIO`, ou
  fundem-se? (Senão ficam duas fontes de vocabulário a divergir.)
- **Vocabulário novo** (Chassis, Slot, Silhueta, VIVO/MORTO, D-proc) não está em nenhum ficheiro
  de continuidade — só nesta pasta. Tem de ser integrado no canon do projeto no grill.

---

## 6. O que falta / perguntas que levanto

1. **Dois "canons" a reconciliar.** A ordem diz que estes docs "não são canon — o canon é o
   SYSTEM-PROMPT". Mas neste repositório o canon é o `CLAUDE.md` + os 3 bootstrap (A/B/C). Há um
   **SYSTEM-PROMPT** da linhagem SArq que eu não tenho. **Pergunta:** o que manda quando a
   SArq-3 e os meus bootstrap divergirem? (Assumo: David > Briefing/Instrução na arquitectura >
   Glossário nas palavras — é o que o fluxo-2 diz — mas confirma.)
2. **Referências da SArq-3 a coisas que não estão neste repo:** `objetivo do david.md`, e um
   `context.md` onde alegadamente está registado o "mapa vazio" do understand-anything. **Esse
   registo não está no meu `context.md`** — é de outra linhagem de chat. Não é problema, mas
   confirma que estes docs vêm de um contexto paralelo a absorver, não de estado deste repo.
3. **Auxiliar/espelho** — a SArq-3 **resolve a lacuna** que o meu teste de arranque tinha
   apanhado (faltava a definição civil): é um *2.º artefacto que lê o mesmo SSOT para comunicar
   com o agente*, agora **subsumido** por manifesto+binding. Fica a pergunta para ti: **o espelho
   desaparece mesmo como peça, ou ainda queres um 2.º artefacto dedicado a mostrar relações
   durante o desenvolvimento?**
4. **Alfândega: um contrato ou um por modo?** É a pergunta-mãe do grill (§3). Tenho munição para
   os dois lados; não a decido.
5. **Linhas/nomes do curador a re-verificar** (§2) antes de qualquer extração.
6. **Onde param os números de linha vs. desenho no D-proc:** o elo "os números 1/2/3 voltam
   legíveis para o Code" é o mesmo risco do (a); vale a pena prová-lo **uma vez** e aproveitar
   para os dois candidatos.

---

### Conclusão (provo que percebi, em 3 linhas)

A SArq-3 fechou o **como** (planta→Code), nomeou o **Chassis/Slot/Silhueta** e pôs o
manifesto-em-texto à frente do arrastar — tudo coerente com o critério-mãe e a convergir com o
meu M1. As decisões caras (Alfândega genérica, desacoplamento) continuam abertas e são tuas. O
Claude Design é **candidato**, não verdade; vive ou morre no teste de import/export. **Estou
pronto para o grill** assim que mandares — começando, como a SArq-3 e o M1 apontam, pela
**Alfândega** com o grafo do curador como caso real.
