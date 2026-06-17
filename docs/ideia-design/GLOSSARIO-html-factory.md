---
created: 2026-06-17 20:40
project: html-artifact-factory
chat: Glossario canonico do html-factory
session: SArq-3
status: vivo
summary: >
  Glossario canonico (dono do vocabulario) do html-factory: pecas, fluxos e ferramentas,
  cada termo com frase tecnica + traducao civil + onde encaixa. Fonte unica; os outros
  documentos apontam para aqui em vez de repetir definicoes.
---

# Glossário — html-factory

> **Dono do vocabulário.** Esta é a fonte única dos termos do projeto. Qualquer outro
> documento (CLAUDE.md, briefings, context.md) deve **apontar para aqui**, não repetir
> definições. Se um termo mudar, muda-se aqui e só aqui.
>
> Cada entrada tem três linhas: **Técnico** (o que é) · **Civil** (a analogia de
> engenharia/arquitectura) · **Encaixa** (onde vive e a que se liga). Lês ao nível do
> termo; nunca precisas de descer ao código.

---

## A · PEÇAS (os componentes do edifício)

### SSOT — `data.json`
- **Técnico:** a fonte única de verdade — dados + relações + IDs, sem qualquer estilo.
- **Civil:** o registo predial do edifício: o que existe e como se liga, sem decoração.
- **Encaixa:** é lido pelos Blocos através da Alfândega. Nunca contém cor/posição (isso é
  Config). Alimenta o Motor.

### Alfândega — schema / contrato
- **Técnico:** o contrato de formato que todos os Blocos respeitam para ler o SSOT.
- **Civil:** o controlo de fronteira: define o que pode entrar e em que forma; quem não
  cumpre o formato não passa.
- **Encaixa:** entre o SSOT e os Blocos. É a peça-mãe — se for genérica, os Blocos tornam-se
  reutilizáveis; se for específica, ficam presos a um caso. (Tensão T2, a fechar no grill.)

### Motor — engine
- **Técnico:** a lógica que transforma os dados do SSOT no que o ecrã precisa. Tem 3 modos:
  relações, hierarquia, tabela.
- **Civil:** a solução estrutural: as contas e o esquema de cargas que decidem como o
  edifício se aguenta e organiza. (O "grafo" não é um 4.º modo — é relações + hierarquia.)
- **Encaixa:** vive dentro de cada Bloco. Lê via Alfândega; entrega ao Viewer.

### Viewer — fachada cega
- **Técnico:** desenha o que o Motor entrega; não sabe de dados nem os altera.
- **Civil:** a fachada do edifício: mostra-se, mas não decide a estrutura por trás.
- **Encaixa:** recebe do Motor. Forma, com ele, um Bloco. Nunca escreve no SSOT (ver Ciclo
  Reativo).

### Config — `config.json`
- **Técnico:** a estética isolada (cores, tema), fora do SSOT e do código do Motor.
- **Civil:** o caderno de acabamentos: tintas e revestimentos, separados da estrutura.
- **Encaixa:** lido pelo Viewer/build. Nunca dentro de `data.json` (invariante: estética
  fora dos dados).

### Bloco
- **Técnico:** par {Motor + Viewer} normalizado à Alfândega, por tipo (tabela, árvore, grafo,
  cartões, filtros, timeline, mind-map...).
- **Civil:** um tijolo/módulo pré-fabricado: peça acabada que encaixa em qualquer obra que
  respeite a fundação.
- **Encaixa:** vive na biblioteca `blocks/`. É a peça VIVA — lê o SSOT, faz coisas. O Code
  injecta-o nos lugares do Chassis.

### Chassis
- **Técnico:** a estrutura de layout sem conteúdo — barra superior, abas, divisórias, caixas
  vazias, zonas. Não lê dados.
- **Civil:** as paredes e divisões do edifício: definem os espaços, mas estão vazios de
  mobília.
- **Encaixa:** define ONDE os Blocos entram. Cada zona é numerada (ver Slot). É a peça MORTA
  — contrasta com Bloco (vivo). Material do fluxo D-proc (desenhado no Procreate).

### Slot (lugar numerado)
- **Técnico:** identificador único de uma zona do Chassis (`data-slot="3"`), estável de
  ponta a ponta.
- **Civil:** o número da porta de cada divisão: morada fixa para o empreiteiro saber onde pôr
  o quê.
- **Encaixa:** criado no desenho/Chassis; o Code lê-o para injectar o Bloco certo ("slot 3 →
  grafo"). Liga-se ao Isolamento Acústico. **Instância única**, nunca tipo.

### Silhueta
- **Técnico:** representação leve e descartável de um Bloco (de retângulo etiquetado a
  mini-preview), usada para montar layout sem o Bloco real.
- **Civil:** a maqueta de cartão de um móvel: serve para ver onde fica, não funciona.
- **Encaixa:** usada no fluxo D-sil (dentro do Claude Design, porque os Blocos reais
  corromper-se-iam lá). O Code substitui Silhueta por Bloco real no fim.

### Manifesto / planta — `workspace.json`
- **Técnico:** declara o layout + que Blocos aparecem e onde.
- **Civil:** a planta do arquitecto: o desenho que o empreiteiro segue para erguer o
  edifício.
- **Encaixa:** é a "linguagem de mudança" — mudar o frontend = editar a planta, não explicar
  por prosa. Lida pelo Code no build.

### Folha de binding
- **Técnico:** o mapa de que dados do SSOT cada Bloco mostra; preenchida por escolha em
  menus, não por escrita livre.
- **Civil:** a ordem de serviço que diz a cada máquina a que tubagem se liga.
- **Encaixa:** segundo passo após o layout (a planta diz *onde/que tipo*; a folha diz *que
  dados*). Construção única; promove-se a permanente só se reconfigurares a toda a hora.

### Isolamento Acústico
- **Técnico:** cada Bloco é fechado e nomeado, de modo que "muda aquilo" tem endereço exacto.
- **Civil:** divisórias com insonorização: o que se passa numa sala não vaza para a outra, e
  cada sala tem nome.
- **Encaixa:** propriedade dos Blocos + dos Slots. É o que torna a comunicação com o Code
  precisa.

### Ciclo Reativo — "um só sentido"
- **Técnico:** a informação circula clique → Motor → dados mudam → ecrã actualiza. Nunca o
  Viewer a escrever directamente nos dados.
- **Civil:** sentido único do trânsito: evita choques de frente (o ecrã e os dados a
  contradizerem-se).
- **Encaixa:** regra de fluxo interna a cada artefacto. O David exige-a; o Code implementa-a.

---

## B · FLUXOS (como as peças se movem)

### Fluxo nuclear — "a planta declara, o Code constrói"
- **Técnico:** Manifesto/layout → Code lê → pega nos Blocos da biblioteca + injecta dados →
  HTML single-file.
- **Civil:** o arquitecto entrega a planta; o empreiteiro ergue o edifício com os módulos do
  armazém.
- **Encaixa:** é o esqueleto de operação de todo o factory. Os Blocos reais vivem no Code,
  nunca no editor de planta.

### D-sil — montar com silhuetas dentro do Claude Design
- **Técnico:** montas o layout dentro do Claude Design usando Silhuetas; exportas; o Code
  substitui Silhuetas por Blocos reais.
- **Civil:** montas a maqueta de cartão na própria mesa de design e depois o empreiteiro troca
  o cartão por móveis a sério.
- **Encaixa:** candidato a "Editor" no grill. Risco: o Claude Design regenera o que recebe.

### D-proc — chassis desenhado no Procreate (material paralelo, autocontido)
- **Técnico:** desenhas o Chassis numerado no Procreate → Claude Design traduz desenho→HTML +
  devolve PNGs → Code injecta Blocos nos Slots.
- **Civil:** desenhas a planta à mão com as portas numeradas; o tradutor passa-a a HTML; o
  empreiteiro mobila cada divisão pelo número.
- **Encaixa:** candidato/avaliação paralela à família Claude Design. O Slot é o identificador
  que viaja. Elo a provar: o Claude Design preservar os números legíveis para o Code.

### Ciclo de biblioteca (D-proc, longo prazo)
- **Técnico:** PNGs voltam ao Procreate → refinas → biblioteca de Chassis/elementos cresce →
  eventual artefacto-puzzle.
- **Civil:** vais guardando plantas-tipo e acabamentos; um dia tens catálogo suficiente para
  montar por encaixe.
- **Encaixa:** é como o editor drag-and-drop (Gridstack arquivado) pode emergir por
  acumulação, em vez de ser construído à cabeça.

---

## C · FERRAMENTAS (quem faz o quê)

### Procreate (iPad)
- **Técnico:** app de desenho onde produzes o Chassis numerado e refinas PNGs.
- **Civil:** a prancheta de desenho do arquitecto.
- **Encaixa:** início e refino do fluxo D-proc. Produz desenho + legenda de Slots. Não toca
  em dados nem código.

### Claude Design
- **Técnico:** ferramenta visual da Anthropic (research preview, Opus) que gera HTML/CSS/JS a
  partir de prompt/imagem; exporta HTML e faz handoff para o Code.
- **Civil:** o estúdio que transforma o esboço em desenho técnico apresentável.
- **Encaixa:** candidato a editor de planta (D-sil e D-proc). Serve só o layout base, nunca a
  fundação (SSOT/Alfândega/Motor/Blocos). É preview — validar import/export antes de assentar.

### Claude Code (o "empreiteiro")
- **Técnico:** o agente que constrói: lê planta/chassis, injecta Blocos da biblioteca, liga
  dados, gera o HTML single-file. Mantém a biblioteca e os invariantes.
- **Civil:** o empreiteiro que ergue o edifício a partir da planta e dos módulos.
- **Encaixa:** o motor de execução do factory. Tudo o que é código vive aqui; o David nunca
  desce a este nível — comunica pela planta e pelos termos deste glossário.

### O David (o "arquitecto")
- **Técnico:** define o que se constrói via linguagem e plantas; não escreve código.
- **Civil:** o arquitecto de sistemas: desenha, decide, instrui — não assenta tijolos.
- **Encaixa:** opera sempre ao nível dos termos deste glossário. É a razão de o glossário
  existir: a comunicação com o Code faz-se pela linguagem, e a linguagem tem de ser única.

---

## D · INVARIANTES (atalho — definição plena no briefing/context)
- **Single-file** no produto final (abre offline).
- **Imutabilidade** — HTML compilado descartável; capital nos módulos; exige passo de build.
- **Separação estanque** — Dados / Config / Motor / Viewer.
- **Estética fora dos dados** — cor/posição em Config, nunca no SSOT.
- **Critério-mãe** — simplificar a relação David↔Code. Simplicidade > completude > elegância.
