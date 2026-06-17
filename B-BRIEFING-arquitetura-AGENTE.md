---
created: 2026-06-17 19:10
project: html-artifact-factory
chat: Bootstrap do factory em Claude Code
session: SArq-3
status: vivo
summary: >
  Briefing de arquitectura para o agente Claude Code: o que vai montar e porque, com
  estrutura de directorios/ficheiros, invariantes e a regra de incremento funcional.
  Auto-suficiente — o agente percebe sem ter vivido as sessoes anteriores.
---

# BRIEFING — html-factory (para o agente Claude Code)

> Le este documento inteiro antes de agir. E o teu mapa: o que vais construir, porque, e
> com que estrutura. Nao o resumas. A tua PRIMEIRA accao operacional esta no ficheiro
> `C-INSTRUCAO-arranque-AGENTE.md` — mas le este briefing primeiro para perceber a logica.

## 0. Contexto e utilidade (porque isto existe)

O utilizador (David) e engenheiro estrutural senior, **nao-programador por opcao**. Quer
gerir-te como **arquitecto**, nao como operario: sabe o que compoe o "edificio" mas nao
escreve codigo. Produz muitos artefactos HTML single-file (dashboards, mapas, curadores
de dados). O problema que esta factory resolve **nao** e a complexidade dos artefactos —
e o **atrito de comunicacao** contigo: hoje ele gasta tempo a explicar por palavras o que
quer mudar. A factory substitui essa prosa por **pecas reutilizaveis + uma planta
declarativa**.

**Criterio-mae (tem precedencia sobre tudo):** a factory existe para **simplificar** a
relacao do David contigo — menos tempo a explicar mudancas, nao mais. Se alguma decisao
tua puxar para "duas semanas a montar infraestrutura" ou exigir que o David domine um
protocolo pesado, **falhaste o proposito**. Simplicidade > completude > elegancia.

## 1. A arquitectura — fluxo "planta -> tu -> edificio"

```
   EDITOR/PLANTA              TU (Claude Code)            RESULTADO
   ---------------            -----------------           ---------------
   o David declara o      ->  les a planta            ->  HTML single-file
   layout + que blocos        + pegas nos blocos da       final, offline,
   (workspace.json)           biblioteca                  a funcionar
                              + injectas os dados
```

Principio nuclear: **a planta declara, tu constróis.** Os blocos reais vivem na
biblioteca do projecto (em ti), NUNCA dentro do editor. O editor (se existir) so mexe em
"retangulos-etiqueta"; e leve.

## 2. As pecas (vocabulario do projecto — usa estes termos)

- **SSOT (`data.json`)** — a verdade unica: dados + relacoes + IDs, **zero estilo**.
- **Alfandega (schema/contrato)** — o formato fixo que TODOS os blocos respeitam para
  ler o SSOT. Peca de primeira classe. E o que torna os blocos intercambiaveis. (Ainda
  por definir na forma generica — ver tensoes; sera fechada no grill.)
- **Motor** — a logica que transforma dados no que o ecra precisa. Tem 3 modos:
  **relacoes**, **hierarquia**, **tabela**. (O "grafo" NAO e um 4.o modo — e relacoes +
  hierarquia juntas.)
- **Viewer** — a fachada cega: desenha o que o motor entrega; nao "sabe" de dados.
- **Config (`config.json`)** — estetica isolada (cores, tema). Fora do SSOT e fora do
  codigo do motor.
- **Bloco** — par {Motor + Viewer} normalizado a Alfandega, por tipo (tabela, arvore,
  grafo, cartoes, filtros, timeline, mind-map...). Os tijolos da biblioteca.
- **Manifesto / planta (`workspace.json`)** — declara o layout e que blocos. E a
  "linguagem de mudanca" do David: mudar o frontend = editar a planta, nao explicar por
  prosa.
- **Folha de binding** — como o David diz "que dados mostra cada bloco". Folha
  meio-preenchida, com menus dos campos existentes no SSOT (ele escolhe, nao escreve).
  Serve **so na construcao** (descartavel); promove-se a permanente so se ele reconfigurar
  a toda a hora.
- **Isolamento Acustico** — cada bloco visual e fechado e **nomeado**: "muda aquilo" passa
  a ter endereco exacto.
- **Ciclo Reativo ("um so sentido")** — a informacao circula clique -> Motor -> dados
  mudam -> ecra actualiza. NUNCA ao contrario; o Viewer **nunca** altera dados
  directamente. Implementa-o; o David exige-o.

## 3. Invariantes (regras absolutas — nao negociaveis)

- **Single-file no produto final.** O edificio entregue e um HTML so, abre offline. (Pode
  haver passo de compilacao modulos -> HTML; o single-file e o *output*, nao
  obrigatoriamente o ambiente de dev.)
- **Imutabilidade.** O HTML compilado e descartavel ("betao curado"); o capital vive nos
  modulos isolados. So valido se existir SEMPRE um passo de compilacao.
- **Separacao estanque.** Dados / Config / Motor / Viewer — mexer numa peca nao parte as
  outras.
- **Estetica fora dos dados.** Nunca metas cor/posicao no `data.json`. Vai para `config.json`.

## 4. Estrutura de directorios e ficheiros (proposta — afina no grill)

```
projeto/
  Artefactos-existentes/        # mina de blocos (input, leitura)
    <artefacto-solto>.html      # HTML auto-suficiente -> fica solto
    <artefacto-com-server>/     # usa server OU pre-carrega ficheiros -> subpasta propria
      index.html
      dados/...
  factory/
    blocks/                     # a biblioteca de tijolos
      grafo/    { engine.js, viewer.js, README.md }
      arvore/   { ... }
      tabela/   { ... }
      ...
    schema/
      alfandega.md              # o contrato generico (SSOT que todo o bloco respeita)
      alfandega.schema.json
    manifest/
      workspace.example.json    # exemplo de planta
    config/
      config.example.json
    build/
      assemble.*                # junta planta + blocos + dados -> dist/
    dist/
      workspace.html            # o edificio final, single-file
  docs/
    decisoes-grill.md           # output do grill (decisoes fechadas) — criar no Passo 2
```

## 5. A regra de execucao: INCREMENTO VERTICAL FUNCIONAL

O David exige: **cada passo funcional antes do seguinte.** Nao montes o esqueleto todo em
abstracto. Cada incremento entrega algo a funcionar de ponta a ponta:

1. Caixa (Dados/Config/Motor/Viewer) + Alfandega + **UM** bloco (recomenda-se o grafo: o
   mais valioso e o mais dificil) a renderizar dados reais -> **prova** -> commit.
2. Generaliza a Alfandega a partir desse caso real (nao em abstracto).
3. Segundo bloco a encaixar no mesmo contrato -> prova -> commit.
4. Restantes blocos, um a um.
5. Manifesto: a planta passa a comandar que blocos aparecem -> prova.
6. Folha de binding -> prova.
7. Editor (se decidido no grill) -> prova.

Cada incremento = um commit na branch de trabalho.

## 5-BIS. Mapeamento dos artefactos PRECEDE as decisoes (sequencia obrigatoria)

O David pos VARIOS artefactos em `Artefactos-existentes/` de proposito. A Alfandega
generica (T2) e as outras decisoes profundas **NAO devem ser fechadas a partir de um so
artefacto** (o curador e o mais rico, mas o mais atipico). Devem nascer do **padrao comum
a varios**.

Por isso, ANTES do grill (Passo 2), tens de **mapear cada artefacto**, decompondo-o em:
- **Dados** — que estruturas de dados usa (formato, campos, relacoes, hierarquias); como
  carrega (inline, ficheiro, server); qual o SSOT de facto.
- **Motor** — que logica de transformacao tem (que modos: relacoes / hierarquia / tabela);
  como processa.
- **UI / Viewer** — que blocos visuais contem (tabela, arvore, grafo, cartoes, filtros,
  timeline...); como renderiza; o que se repete entre artefactos.

O produto deste mapeamento e o **input factual do grill**: revela o vocabulario real do
David e o que ele de facto faz, para o contrato generico nascer do padrao observado, nao
de um palpite. Sem este mapa, NAO entres no Passo 2.

## 6. Tensoes em aberto (NAO as resolvas sozinho — sao para o grill, Passo 2)

- **T2 — Alfandega generica.** O contrato unico que torna os blocos reutilizaveis.
  Fecha-a a partir do **padrao comum** revelado pelo mapeamento (sec. 5-BIS), nao so do
  curador. O SSOT do curador (`projetos[]`, `links[]{id,a,b,t}`, `crossLinks[]`,
  `domainTree`) e apenas UM dos casos. **Por fechar com o David.**
- **T1 — Desacoplamento.** Os blocos do curador estao soldados a um STATE global e a um
  SSOT especifico de projetos-AI. Para serem biblioteca, cada bloco tem de ler o contrato
  generico (arvore = qualquer pai/filho; grafo = quaisquer nos/arestas; tabela = qualquer
  lista). Metodo (todos de uma vez vs. um piloto) por decidir.
- **Auxiliar/espelho.** Conceito da arquitectura: um 2.o artefacto que le o mesmo SSOT e
  mostra relacoes durante o dev. Pode ter sido subsumido pelo manifesto+folha. **Confirmar
  com o David se ainda existe como peca.**
- **Editor.** Gridstack (arrastar a serio) vs. manifesto-em-texto editavel a mao.
  **Recomenda ao David no grill, com trade-offs.** Nao decidas sozinho.
- **Imutabilidade verificada.** Hoje e decretada, nao verificada (nada deteta edicao
  directa do `dist/`). Mitigacao possivel: build stamp (hash das fontes). Detalhe de
  implementacao; levanta quando chegar a build.

## 7. Como comunicas com o David (obrigatorio)

Ele e arquitecto nao-tecnico. Em qualquer explicacao de arquitectura:
- **Linguagem Ubiqua sempre com traducao:** usa os termos do projecto (SSOT, Motor,
  Alfandega, Viewer...) SEMPRE emparelhados com a analogia civil (alfandega = controlo de
  fronteira do formato; viewer = fachada; ciclo reativo = sentido unico do transito). O
  termo a seco falha; a traducao sozinha tambem.
- **Ritmo com gate:** uma ideia por vez, do macro para o micro, e PARA a pedir confirmacao
  antes de avancar. Nao despejes analise densa em bloco.
