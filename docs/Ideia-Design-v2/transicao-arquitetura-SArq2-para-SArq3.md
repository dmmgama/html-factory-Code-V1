---
created: 2026-06-17 18:45
project: html-artifact-factory
chat: Transicao da arquitectura SArq-2 -> SArq-3
session: SArq-3
status: vivo
summary: >
  Documento de transicao: o que estava decidido na SArq-2 (6 alicerces) e para o
  que a SArq-3 o transpos, peca a peca, com a razao de cada transposicao. Ponte
  de continuidade entre as duas sessoes.
---

# Transicao da arquitectura — do que estava decidido (SArq-2) para o que ficou (SArq-3)

> Doc-vivo de continuidade. Lê-se ANTES da cristalizacao da SArq-3
> (`arquitetura-html-factory-SArq-3.md`). Existe porque a SArq-3 NAO partiu do zero:
> partiu do esqueleto que a SArq-2 fechou. Aqui regista-se o que era o decidido, para o
> que se transpos, e porque — para que a proxima sessao veja a linha de continuidade e
> nao leia a SArq-3 como se anulasse a SArq-2. NAO e canon (o canon e o SYSTEM-PROMPT).

---

## 1. O ponto de partida (o que a SArq-2 tinha fechado)

A SArq-2 fechou a factory como **esqueleto de 6 ALICERCES, zero regrinhas**, registado
no `objetivo do david.md`. Regua do David: **alicerce** = define-se 1x e poupa atencao
sempre; **tralha** = exige ritual a cada passo. Os 6 alicerces:

1. **Caixas** (Dados/Config/Motor/Viewer) — separacao em dominios estanques.
2. **Alfandega** (schema) — o molde fixo dos dados; peca de primeira classe.
3. **Config** — estetica isolada, fora dos dados e do codigo.
4. **Isolamento Acustico** — cada bloco visual fechado e nomeado.
5. **Ciclo Reativo** — regra "um so sentido"; o Viewer nunca altera dados.
6. **Motor de 3 modos** — relacoes / hierarquia / tabela (grafo = relacoes+hierarquia,
   NAO 4.o modo).

Tralha descartada: Funil de 4 etapas, Airgap, MCP, aparato de imposicao (Ajv/Zustand
como obrigacao).

**O que a SArq-2 deixou EXPLICITAMENTE EM ABERTO** (e o gancho de toda a SArq-3):
> "[ABERTO · alta prioridade] Forma agil de mudar o frontend. A arquitectura das caixas
> resolve a separacao e a imutabilidade, mas NAO resolve uma forma agil de alterar o
> frontend (a View)."

O Isolamento Acustico (alicerce 4) ja dava o **endereco** ("muda aquilo" tem morada);
faltava a **linguagem** (como o David formula a mudanca para o Code acertar a 1a). Era a
unica peca aberta da arquitectura.

---

## 2. O que a SArq-3 fez — em uma frase

A SArq-3 **nao substituiu** os 6 alicerces: **completou-os**. Fechou a peca aberta (a
forma agil de mudar o frontend) e, ao faze-lo, deu nome e lugar a uma peca que faltava —
o **manifesto/planta** — e desenhou o **fluxo de operacao** (planta -> Code -> edificio)
que ate ai estava implicito. Os alicerces da SArq-2 continuam todos validos; ganharam o
mecanismo que faltava para serem usados.

---

## 3. Transposicao peca a peca

| Peca | Estado na SArq-2 (antes) | Para o que se transpos na SArq-3 (depois) | Porque |
|---|---|---|---|
| **Caixas** (Dados/Config/Motor/Viewer) | Alicerce fechado: separacao estanque | **Inalterado.** Confirmado pela pesquisa Perplexity (data layer / engine / renderer) — e a separation-of-concerns classica. | A pesquisa externa validou, nao contrariou. So reforcou. |
| **Alfandega** (schema) | Alicerce fechado, mas em abstracto | **Concretizada:** o SSOT do curador, ja documentado campo-a-campo (no `curador-dashboard.html`), passa a ser o ponto de partida do contrato. Promovida a tensao por fechar (T2): definir a Alfandega *generica*. | Deixou de ser ideia; ganhou material real de onde nascer. |
| **Motor (3 modos)** | Alicerce fechado | **Inalterado** na definicao. Reposicionado: vive *dentro de cada bloco*. | Coerencia com a biblioteca de blocos; sem mudanca de conteudo. |
| **Isolamento Acustico** | Alicerce: da o "endereco" ao frontend | **Cumprido e estendido:** o endereco (Isolamento) junta-se agora a uma *linguagem* (o manifesto). Resolve em conjunto o [ABERTO·alta]. | Era meia-solucao; a SArq-3 deu a outra metade. |
| **Ciclo Reativo** | Alicerce: "um so sentido" | **Inalterado.** | Sem mudanca. |
| **Config** | Alicerce: estetica isolada | **Inalterado.** | Sem mudanca. |
| **Biblioteca de BLOCOS** | Objectivo: pares {Motor+Viewer} normalizados ao contrato | **Operacionalizada:** os blocos passam a ter fonte concreta (extraccao do curador, 7 blocos ja identificados com funcao+linha) e um plano (Fase 2). | Era intencao; ganhou caminho de execucao. |
| **"Forma agil de mudar o frontend"** | PROBLEMA ABERTO [alta] | **FECHADO:** = o manifesto (`workspace.json`). A linguagem de mudanca deixa de ser prosa e passa a ser uma planta. | Era o buraco nuclear; a SArq-3 existe sobretudo para o tapar. |
| **Auxiliar / artefacto-espelho** | Peca da SArq-2 (3.o item): 2.o artefacto que le o mesmo SSOT para comunicar com o agente | **Subsumido/transformado:** o papel de "instrumento de comunicacao com o agente" e agora desempenhado pela dupla *manifesto + folha de binding*. O espelho deixa de ser peca separada explicita. | A funcao manteve-se; a forma mudou para algo mais barato e directo. (Ver tensao em sec. 5.) |

---

## 4. As pecas NOVAS que a SArq-3 acrescentou (nao existiam na SArq-2)

1. **Manifesto / planta (`workspace.json`).** A peca que faltava. Declara layout + que
   blocos. E a "linguagem de mudanca" que fecha o [ABERTO·alta].
2. **Fluxo de operacao "planta -> Code -> edificio" (Caminho 1).** A SArq-2 tinha as
   pecas mas nao o *modo de as operar*. A SArq-3 fixou: o editor cospe a planta, o Code
   constroi, os blocos vivem no Code (nao no editor).
3. **Folha de binding (construcao unica, depois promover).** Como o David diz "que dados
   mostra cada bloco" sem escrever JSON — folha meio-preenchida com menus.
4. **Editor drag-and-drop (Gridstack) como luxo adiado.** A SArq-2 nem chegava aqui; a
   SArq-3 avaliou, viu que o arrastar e barato (Gridstack), mas decidiu adia-lo —
   manifesto-em-texto primeiro.
5. **Plano de 2 fases + correccao do executor.** Fase 2 (semear bibliotecas dos
   artefactos existentes) com a conclusao de que o executor e o **Code**, NAO o
   `understand-anything` (pedagogico, e cego em single-file).

---

## 5. O que NAO se transpos (continua aberto ou foi rebaixado)

- **Auxiliar/espelho como peca autonoma.** A sua funcao foi absorvida pelo manifesto +
  folha de binding. Fica a *tensao*: confirmar com o David se o espelho desaparece como
  peca ou se ainda quer um 2.o artefacto dedicado a mostrar relacoes durante o dev.
- **Imutabilidade decretada vs verificada** (tensao herdada da SArq-2): continua por
  resolver. Nada deteta edicao directa do `dist/`. Mitigacao proposta (build stamp/hash)
  nao decidida.
- **§4.2–4.4 do SP** (o que a factory e / nao e / role): continua por fechar; este
  trabalho alimenta-o mas nao o substitui.
- **Versao SOFISTICADA da arquitectura** (item aberto da SArq-2): nao foi o caminho — a
  SArq-3 nao foi por "instrumentos avancados", foi por simplificar via manifesto. A
  sofisticacao foi, na pratica, *recusada* em favor do criterio-mae.

---

## 6. Linha de continuidade (uma frase para a proxima sessao)

A SArq-2 deu o **esqueleto** (6 alicerces) e nomeou o **buraco** (frontend agil). A
SArq-3 **tapou o buraco** (manifesto) e deu o **modo de operar** (planta->Code) + o
**plano de arranque** (extrair blocos do curador, Fase 1/2). Nada foi anulado; tudo foi
completado. Ler a seguir: `arquitetura-html-factory-SArq-3.md` (o estado-da-arte
consolidado).
