---
created: 2026-06-17 18:30
project: html-artifact-factory
chat: Arquitectura html-factory — planta, blocos, manifesto
session: SArq-3
status: vivo
summary: >
  Cristalizacao da arquitectura do html-factory decidida no grill-me da SArq-3:
  fluxo planta->Code, biblioteca de blocos, manifesto e folha de binding; plano
  de 2 fases com a correccao do executor (Code, nao understand-anything).
---

# Arquitectura do html-factory — cristalizacao SArq-3

> Doc-vivo. Produzido no grill-me da SArq-3 (auditor em modo web). Captura a
> arquitectura que o David fechou e o plano de arranque. NAO e canon (o canon e o
> SYSTEM-PROMPT). E o estado-da-arte da factory ate esta sessao, para alimentar a
> proxima e, se o David quiser, o Operacional (Code) na Fase 1.

---

## 1. O problema que a factory resolve (criterio-mae)

A factory existe para **simplificar a relacao do David com o Claude Code** — menos
tempo a explicar mudancas ao agente, nao mais. Os artefactos do David sao simples; o
atrito real e de **comunicacao**, nao de complexidade. Qualquer proposta que puxe para
"2 semanas a montar" ou exija dominar um protocolo pesado **falhou o proposito**. Este
criterio tem precedencia interpretativa sobre tudo o resto.

---

## 2. A arquitectura fechada — fluxo "planta -> Code -> edificio"

A peca que faltava (pendente [ALTA] do handoff SArq-2: "frontend agil / linguagem de
mudanca") ficou **resolvida**. A linguagem com que o David comunica a montagem ao Code
deixa de ser prosa e passa a ser uma **planta** (manifesto). Desenho geral:

```
   EDITOR (Gridstack)         FACTORY / CODE              RESULTADO
   "prancheta"                "empreiteiro + biblioteca"  "edificio"
   ----------------           -----------------------     ----------------
   arrastas zonas/blocos  ->  Code le a planta        ->  HTML single-file
   (retangulos-etiqueta)      + pega nos blocos reais     final, a funcionar
        |                     da biblioteca
        v                            |
   cospe workspace.json         blocks/ (arvore, grafo,
   = a PLANTA / manifesto       cards, filtros, barras,
        |                       timeline, mind-map...)
        |                       cada um le o SSOT via Alfandega
        +---------> a planta e a ponte <-----------+
```

### 2.1 As pecas e como o que ja existia encaixa

| Peca (nome do projeto) | Traducao civil | Papel |
|---|---|---|
| **Caixa de Dados / SSOT** | a verdade unica | dados puros, zero estilo |
| **Alfandega** (schema/contrato) | a alfandega | formato fixo que todo o bloco respeita para ler o SSOT |
| **Motor (3 modos)** | a solucao estrutural | vive dentro de cada bloco (relacoes / hierarquia / tabela; grafo = relacoes+hierarquia, NAO 4.o modo) |
| **Viewer** | a fachada cega | desenha o que o motor entrega |
| **Biblioteca de BLOCOS** | tijolos | `blocks/` — pecas reutilizaveis por tipo |
| **Manifesto / planta** (peca nova) | a planta do arquitecto | `workspace.json` que o editor cospe; diz layout + que blocos |
| **Editor (Gridstack)** | a prancheta | comprado, leve; so mexe em retangulos-etiqueta |
| **Ciclo Reativo ("um so sentido")** | sentido unico do transito | o David so tem de o EXIGIR; o Code implementa |

### 2.2 Decisao-charneira: Caminho 1 (planta), nao Caminho 2 (blocos no editor)

O editor **gera uma planta**; o Code constroi o edificio a partir dela. Os blocos reais
vivem na **factory/Code**, NAO dentro do editor. O editor e leve (so formas). Rejeitado
o Caminho 2 (meter os blocos a funcionar dentro do editor) — e o caminho-monstro das "2
semanas".

### 2.3 O arrastar (Gridstack) e luxo, nao requisito — adiado

O valor ("montar a carta sem re-explicar") consegue-se com o **manifesto em texto**. O
arrastar-com-rato (Gridstack resolve-o barato, nao e bicho de 7 cabecas) e **conforto
adicional**, adiado ate a base funcionar com manifesto-em-texto. Inverter a ordem e o
caminho para o pantano.

### 2.4 O binding (que dados mostra cada bloco) — fluxo do David, validado

A planta diz *onde* e *que tipo* de bloco. Falta *que dados* mostra (o **binding**).
Fluxo escolhido pelo David:

1. Monta o layout no editor -> sai a planta.
2. O Code pega na planta e mete os blocos.
3. O Code devolve uma **tabela/lista** a identificar cada bloco colocado.
4. O Code da uma **folha (Excel ou similar)** onde o David diz "este bloco mostra este
   campo".

Refinamentos (certeza alta): a folha vai **meio-preenchida**, com **menus de escolha**
dos campos que existem no SSOT (o David **escolhe**, nao **escreve**); a folha e a
**ponte de volta** (David preenche -> Code injeta os bindings). Duas plantas: uma de
**forma** (editor), uma de **conteudo** (folha).

### 2.5 Binding: construcao unica, depois promover

A folha de binding serve **so na construcao** (descartavel, anda com o Code). Se mais
tarde o David der por si a reconfigurar a toda a hora, **promove-se** a peca permanente
(mapa de bindings ao lado do SSOT). Nao agora.

---

## 3. Plano de 2 fases

### Fase 1 — montar a arquitectura do html-factory
Estabelecer o esqueleto: Caixa de Dados/SSOT + Alfandega (contrato) + biblioteca de
blocos + manifesto + folha de binding. Editor Gridstack adiado (2.3).

### Fase 2 — semear as bibliotecas a partir dos artefactos existentes (CORRIGIDA)
Ideia-mae do David (boa): **nao comecar do zero** — varrer os artefactos que ja tem e
extrair deles os blocos e padroes de UI que gosta, ficando logo com biblioteca semeada.

**Correccao do executor (certeza alta):** o executor **NAO e o `understand-anything`**.
Ver seccao 4. A Fase 2 e uma **encomenda de varrimento-e-extraccao ao Operacional
(Code)**, usando os seus subagentes (`html-expert`, `ui-designer`). O
`understand-anything` pode entrar como *auxiliar* (explicar o que cada artefacto faz),
nao como motor da extraccao.

---

## 4. O que o understand-anything faz, e porque NAO e o motor da Fase 2

**E:** plugin do Claude Code; pipeline multi-agente que produz um **grafo de
conhecimento** (.json) + dashboard interativo **pedagogico** ("ensina-te o codigo").
Motor: **Tree-sitter** (factos estruturais: imports/exports/definicoes/quem-chama-quem,
**entre ficheiros**) + **LLM** (resumos, camadas API/Servico/Dados/UI/Util, dominios,
tours). Incremental.

**Porque falha aqui (2 razoes):**
1. **Finalidade errada.** Da *mapas pedagogicos*, nao *componentes reutilizaveis*. Diz
   "aqui esta renderGraph, camada UI, faz X" — nao entrega renderGraph empacotado como
   bloco pronto a encaixar.
2. **Topologia errada.** Assenta em Tree-sitter a **seguir imports ENTRE ficheiros**.
   Os artefactos do David sao **single-file HTML** — sem imports entre ficheiros para
   seguir. Evidencia dura: ja correu no curador e deu **mapa vazio** (0 imports, 0
   edges) — registado no context.md. A causa esta agora explicada.

**Evidencia do que funciona:** o `curador-dashboard.html` (gerado por analise direta,
nao pelo skill nativo) **inventaria os blocos e o SSOT campo-a-campo** — muito melhor
para extraccao do que o output nativo do skill.

---

## 5. O curador como mina de blocos (engenharia reversa)

O `projetos-curador-v3.html` e o seu mapa (`curador-dashboard.html`) servem como
**fonte de blocos** (andar 1), NAO como template de dashboard (andar 2 — as 4 abas sao
fixas, hardcoded, sem manifesto). Blocos ja identificados, com funcao e linha:

| Bloco | Funcao no curador | Linha |
|---|---|---|
| Grafo (relacoes) | `renderGraph` | 1275 |
| Arvore / genealogia | `renderGenealogy` | 1502 |
| Timeline | `renderCronologia` | 1485 |
| Tabela | `renderHead` + `renderBody` | 887 / 1088 |
| Filtros (13 partilhados) | `renderFilterBar` | 820 |
| Card | `makeProjCard` | 1691 |
| Mind-map | `renderAsgMindmap` | 1872 |

**Alfandega ja documentada:** a aba STATE do `curador-dashboard.html` lista o SSOT
campo-a-campo (`projetos[]`, `links[]{id,a,b,t}`, `crossLinks[]`, `domainTree`). Isto e
o contrato de dados ja redigido — ponto de partida da Alfandega generica.

**Tensao herdada (do handoff SArq-2):** os blocos do curador estao **acoplados** ao
STATE global e ao SSOT especifico de projetos-AI. Para serem biblioteca a serio, cada
bloco tem de ler um contrato **generico** (arvore = qualquer pai/filho; grafo =
qualquer nos/arestas; tabela = qualquer lista de registos). Desacoplar = trabalho real.

---

## 6. Distincao que estrutura tudo: 2 andares de "biblioteca"

- **Andar 1 — BLOCOS** (tipos de visualizacao): pecas genericas reutilizaveis em
  `blocks/`. **Ponto de partida.** Sai bem do curador.
- **Andar 2 — ARRANJOS** (menus, abas, disposicoes): manifestos-modelo (`workspace.json`
  pre-feitos). **Adiado** — so vale a pena quando ja houver 3-4 artefactos e o padrao se
  vir repetir. Extrair antes disso = abstraccao no vacuo. NAO sai do curador.

---

## 7. Decisoes fechadas (resumo)

- D1. Criterio-mae: simplificar a relacao com o Code; alarme "2 semanas".
- D2. Fluxo planta->Code (Caminho 1). Blocos vivem no Code, nao no editor.
- D3. Manifesto (`workspace.json`) = a "linguagem de mudanca" para layout. Resolve [ALTA].
- D4. Editor drag-and-drop (Gridstack) = luxo adiado; manifesto-em-texto primeiro.
- D5. Binding por folha meio-preenchida com menus; construcao unica, depois promover.
- D6. Plano 2 fases; Fase 2 = extraccao pelo Code, NAO pelo understand-anything.
- D7. Curador = mina de blocos (andar 1), nao template (andar 2).
- D8. Biblioteca comeca pelos BLOCOS (andar 1); arranjos (andar 2) adiados.

## 8. Tensoes / pendentes

- T1. Desacoplamento dos blocos do curador (STATE global + SSOT especifico) -> contrato
  generico. Trabalho real; metodo (todos de uma vez vs. um bloco-piloto) NAO decidido.
- T2. Definir a **Alfandega generica** — o contrato unico que torna os blocos
  reutilizaveis. Ponto de partida: o SSOT do curador, ja documentado (sec. 5). Por fechar.
- T3. Imutabilidade decretada, nao verificada (herdada de SArq-2): nada deteta edicao
  directa do `dist/`. Mitigacao proposta: build stamp (hash das fontes). NAO decidida.
- T4. Arranjos-tipo (andar 2) — quando e como extrair. Adiado por design.

## 9. Proxima accao

Arrancar a **Fase 1** (montar o esqueleto) ou preparar a encomenda de extraccao ao Code
(um bloco-piloto: o grafo, o mais valioso e dificil, provado fora do curador, e a partir
dele definir a Alfandega generica — recomendacao de metodo do auditor, por validar pelo
David).
