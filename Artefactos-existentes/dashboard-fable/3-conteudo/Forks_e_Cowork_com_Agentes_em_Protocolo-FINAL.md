---
recipient: Humans-Informative
created: 2026-06-10T01:54:00
type: record
platform: Claude-Desktop
session_father: No Father
autonomy: standalone
set: ecossistema-protocolos
version: 2
status: em aberto
tags:
  - Fork-Return
summary: "Apresentacao (pirâmide de Minto) de duas adicoes que ampliam as capacidades de um projeto reutilizando o governo existente sem o alterar: o Protocolo Fork e a Incorporacao de Cowork. Estrutura: resposta primeiro, funcionamento de cada um, racional/limitacoes, e no fim as Melhorias (refinamentos travados no Fork-Return) e as Tensões a resolver (adiadas, com gatilho)."
---

# Duas adições de capacidade: Protocolo Fork e Incorporação de Cowork

## Enquadramento (SCQA)

- **Situação.** Estávamos em fase de fechar decisões. No entanto tive duas ideias que adicionam capacidade aos projetos, que eu acreditei que podiam acrescentar muito, sem desviar do objetivo do mínimo governo possível.
- **Facto**: O ecossistema tem já protocolos de governo estáveis e debatidos: ficha de sessão, SESSOES/`log-sessoes` (rastreabilidade), LIGACAO de dois braços (blackboard) e o sistema de cristalização.
- **Lacunas operacionais (que não são resolúveis por governo).** (i) Sessões estratégicas longas com nuances importantes a certo ponto merecem explorar hipóteses que precisam do contexto da sessão: difícil delegar por handoff mas difícil continuar, sem context rot. (ii) O setup atual no braço estratégico (deliberação + filesystem) não dá nem agentes especializados nem execução de grau industrial (documentos, dashboards, artefactos).
- **Questão.** Como ampliar as capacidades de um projeto sem mexer nos protocolos de governo já fechados?
- **Resposta.** Duas adições de baixo impacto — **(1) Protocolo Fork** e **(2) Incorporação de Cowork** — que acrescentam capacidade *reutilizando* o governo existente (`log-sessoes`, Blackboard, LIGACAO), sem o alterar.

---

## Parte 1 — Funcionamento (o quê e como)

### Adição 1 — Protocolo Fork

Ferramenta para explorar uma tangente dentro de uma sessão longa sem poluir o fio principal, devolvendo só uma conclusão limpa. Utilizei agora contigo, e noutras sessões. Funciona, mas precisa de ter protocolo, de modo a ser mecanismo formal e com automatismo que me liberta de explicações ao agente. Protocolo a criar:

**Gatilho e sequência (exata):**
1. Sessão está a decorrer normalmente. David sente que quer explorar uma opção. Então dá o gatilho para o fork — passo 2.
2. David: `Fork`
3. Agente: `Fork Ativado — [data/hora, Europe/Lisbon]. Espero resultado.`
4. David: `Ativo`
5. Agente: `O que queres debater?` → decorre o debate.

**Encerramento (close-protocol).** Ao fechar, o agente produz: (a) um texto copiável com a conclusão cristalizada; (b) um MD do substrato quando justificado.

**Retorno** — David edita **uma das suas próprias mensagens**:
- **Sem devolução:** edita a mensagem `Fork` e escreve o que escreveria se não houvesse fork → apaga tudo; o agente nunca soube; sem registo.
- **Com devolução:** edita a mensagem `Ativo` e cola a conclusão → o agente sabe que houve fork e trata o resultado.
- **Variante colapso:** devolve no ponto onde o tema começou (N mensagens antes do fork), colapsando sub-debate + fork numa só conclusão. Aqui salvar o MD do substrato é **obrigatório**.

**Registo.** Havendo devolução, o agente avalia uma de duas hipóteses e sugere ao David qual seguir; o David decide.
- **Hipótese 1 (informativa):** a devolução é útil para a sessão mas não tem importância que justifique registo — o agente usa-a no fio em curso, mas **não deixa rasto**: sem entrada no `log-sessoes`, sem ficha, sem cristalização.
- **Hipótese 2 (crítica):** a devolução contém conteúdo de grande importância (descarta ou valida uma via) — regista-se como **entrada da sessão** no `log-sessoes` (DECISÃO/observação) e na ficha de projeto, não como EXTERNA e sem etiqueta "fork"; se for matéria importante (p.ex. ideias de governo descartadas), produz-se nó cristalizado.

A decisão de registo é do David; o agente sugere a *tier*, não classifica a utilidade do fork — só reage a ter havido devolução.

### Adição 2 — Incorporação de Cowork

**O stack.** Um projeto passa a dispor de três ferramentas, escolhidas pela natureza do trabalho: **Claude Projects**, **Claude Code** e **Cowork**.

A estrutura é em braços: um projeto tem sempre um **braço estratégico** (hoje, Claude Projects) e, quando necessário, um ou mais **braços operacionais**. A necessidade operacional resolve-se com **Code** (operações de código), **Cowork** (distinto do Code: produz artefactos, documentação, etc.) ou **ambos**.

A pesquisa conduzida no fork mostrou algo novo: o Cowork não serve só o braço operacional — pode integrar-se também no **braço estratégico**, como complemento ao Projects, ampliando a sua capacidade. (O formalismo que distingue o modo de atuação do Cowork — estratégico vs. operacional — é revelado adiante.)

#### 1. Braço estratégico: uma entidade formal única, em duas plataformas

O trabalho estratégico divide-se entre duas plataformas que, para efeitos de governo, são **uma só entidade**:

- **Claude Projects** — a plataforma base de deliberação e debate estratégico. É o *default*.
- **Cowork em modo estratégico** — o complemento. Entra quando, no decorrer de uma sessão Projects, se torna útil **delegar a multiagentes especialistas**. É isto que amplia enormemente a capacidade estratégica: o Cowork permite agentes *custom* especializados que o Projects não tem.

**A lógica do "entidade única":** ambas as plataformas fazem trabalho estratégico para o mesmo projeto, logo partilham **um só governo** — mesma nomenclatura de sessões, mesmos logs, mesmo relógio, **mesma pasta e mesmo system prompt**. Não há distinção de registo entre usar uma ou outra; o que muda é apenas a capacidade disponível (os subagentes só existem na superfície Cowork). É esta unidade que impede a sessão de se fragmentar entre superfícies.

**Enforcement do modo estratégico no Cowork:** Opus + extended thinking (seletivo) + instrução "debate, não executes" — para contrariar o enviesamento do Cowork para a execução.

#### 2. Braços operacionais: projetos próprios, ligados só pelo Blackboard

Cada braço operacional é um **projeto próprio**: pasta própria, SP próprio. Com o braço estratégico partilha **apenas o Blackboard** — essa é a única membrana entre deliberação e execução.

- **Cowork-op** — funções operacionais únicas e distintas do Code: geração de documentos, documentação, dashboards, artefactos, trabalho "live".
- **Code** — código.
- O SP operacional **não se redige à mão**: é gerado pelo bloco §4.B do LIGACAO.

**Decomposição Blackboard ↔ privado** (o que tem de ser comum vs. o que fica local):

- **No Blackboard** (partilhado, alcançável por todas as superfícies): o `log-sessoes` (o relógio único — é por viver aqui que o governo é único) e o canal estratégia↔operacional (worklog / hot / ops-snapshot / code).
- **Privado de cada braço:** o seu SP, o `context`, a ficha e o handoff de deliberação.

**A lógica da decomposição:** o relógio tem de ser comum (senão não há governo único), mas o estado de deliberação de cada braço é local (senão os braços poluem-se mutuamente).

#### Montagem no template

Monta-se **sempre multibraço de início**, mesmo num projeto que só venha a ser estratégico: a pasta `Blackboard` está presente e os braços operacionais ficam **declarados, mas desativados** no SP. A ativação é *on-demand*: cria-se `OP-Cowork` ou `OP-Code` com o seu SP (gerado pelo LIGACAO), aponta-se ao Blackboard, e segue-se o protocolo de dois braços, **inalterado**. O custo de ter isto sempre montado é quase nulo (uma pasta e umas linhas no SP); o ganho é não precisar de retrofit a meio do projeto.

---

## Parte 2 — Racional (porquês, limitações, o que cada um acrescenta)

*Esta parte existe porque um agente que leia os protocolos vai questioná-los. Aqui está o processo que levou a cada decisão e o que ficou rejeitado, para que não se re-litigue.*

### Fork

**Porque existe, apesar dos subagentes.** Subagente e fork são mecanismos opostos: o subagente é uma **delegação de contexto isolado** (worker fresco, tarefa scoped, recebe só o que se lhe passa); o fork é um **ramo que herda o contexto inteiro** da sessão. Explorar uma abordagem estratégica com toda a nuance já construída não é delegável a um subagente — ele não tem esse contexto, por desenho. Logo o fork não é substituído pela delegação; complementa-a.

**Porque a sequência tem de ser exata.** Só se podem editar as mensagens do próprio David, não as do agente. São precisos **dois anchors dele** a abraçar o fork: `Fork` (editar = apagar tudo, sem rasto) e `Ativo` (editar = devolver, preservando que houve fork). O `Ativo` não é cerimónia — é o segundo anchor editável, sem o qual não se obtêm os dois resultados limpos (apagar vs. devolver).

**Limitações.** O que não é devolvido perde-se do fio principal (daí o MD obrigatório nos colapsos grandes, que destroem contexto real); a disciplina do handshake depende do David; o ganho é de **higiene de contexto**, não de capacidade de raciocínio nova.

**O que acrescenta.** Sustentabilidade das sessões longas: resolver e colapsar sub-threads sem poluir o fio principal, preservando a nuance via cristalização.

### Cowork

**Porque "incorporação" e não "migração".** Considerou-se migrar de Projects para Cowork (pelas capacidades adicionais que Projects não tem) e rejeitou-se: o Cowork é debate-*capaz* mas execução-*enviesado* (o harness puxa para executar — observado também no Claude Code). "Migrar" assume que uma superfície substitui a outra; deliberação ≠ execução. A decisão foi **dividir por fases**, não substituir.

**Porque se dispensou o teste empírico.** O teste só servia para decidir o *colapso* num só ambiente (a hipótese de o Cowork substituir a deliberação). Essa hipótese foi rejeitada (perde-se o ambiente-como-guarda: o Desktop, por não executar, é obrigado a deliberar). Escolhida a via de não-colapso, o teste tornou-se irrelevante: o Cowork só se usa quando se quer multiagente, não como debatedor puro.

**O que os subagentes acrescentam.** Fluxo integrado (substitui o protocolo manual chat-novo→pesquisa→devolve); especialistas persistentes (subagente + memória + "Dreaming", que cura a memória entre sessões); modelo-por-tarefa.

**Limitações e contras (reais, não "quase nenhum").** (i) **Dependência cross-superfície:** o governo único só se aguenta se Desktop, Cowork e Code alcançarem *o mesmo* Blackboard; verifica-se uma vez, mas é pré-condição. (ii) **Viés de execução** do Cowork-estratégico, mitigado por um gatilho de escalada de volta ao Desktop quando uma sessão derivar para debate profundo puro. (iii) **Custo:** o routing tem um footgun conhecido (a indicação de "usar Opus" pode vazar para todos os subagentes); o Fable 5 serve só investigação pesada, é caro (2× Opus) e o seu acesso por subscrição muda a 23 jun 2026.

**O que acrescenta.** O braço operacional ganha execução de grau industrial (ficheiros, dashboards, artefactos) mais especialistas; o braço estratégico ganha multiagente sem sair do governo único.

---

## Parte 3 — Melhorias (refinamentos travados no Fork-Return)

*Estas melhorias resultam do debate de retorno do fork. Afinam as duas adições sem as recolocar em causa: as decisões da Parte 1 mantêm-se. Tornam operacionais pontos que, sem este detalhe, vazariam na prática.*

### Fork

- **Regra do "sem rasto", agora hermética.** Durante um fork, a escrita persistente vai **só** para uma secção dedicada **"Fork X"** na ficha de projeto — **nunca** para o `log-sessoes`, **nunca** para cristalização, **nunca** para outro ponto da ficha. Essa secção é o scratch do fork (serve também para o proteger de *context rot* a meio: questões de relevo vão sendo lá escritas). No retorno, o close-protocol **força** a decisão:
  - *Sem devolução* (edita `Fork`) → apaga-se a secção "Fork X" → rasto zero.
  - *Hipótese 2 / crítica* → promove-se o conteúdo da secção a entradas reais (`log-sessoes` DECISÃO/observação, ficha, cristalização) e limpa-se a secção "Fork X".
  Sem esta confinação a um único local apagável, o caminho de "apagar" não era hermético: bastaria uma escrita a meio do fork para deixar rasto que o anchor editado não desfaz.

### Cowork

- **Carregamento do SP único (resolve a pré-condição).** O SP é um **ficheiro** no folder, lido por ambas as superfícies no arranque. As "instruções de projeto" de cada superfície são *stubs* mínimos, idênticos **exceto** numa linha:
  - Projects → "lê o SP, é o teu cânone."
  - Cowork → "1. nesta sessão debate, não executes; 2. lê o SP, é o teu cânone."
  A partir daí a atuação é idêntica. Não há SP configurado *dentro* de cada superfície (que divergiria); há um SP-ficheiro e dois stubs que lhe apontam.

- **Uma sessão por superfície.** Cada sessão é dona de **uma** superfície; nunca a mesma sessão corre em simultâneo em Projects e Cowork. É isto que impede escrita concorrente no `log-sessoes` e mantém o relógio único íntegro (o append-only resolve sequência, não concorrência).

- **A entidade estratégica partilha um só estado.** Projects e Cowork-estratégico partilham o **mesmo** `context`, a **mesma** ficha e o **mesmo** handoff. A superfície distingue-se por um **sufixo de sigla** no ID da sessão (ex.: `S-1-A` = Projects, `S-1-B` = Cowork), não por artefactos separados. A distinção é de *bootstrap* (montagem do projeto); o projeto a correr pode não precisar de a conhecer, ou pode formalizá-la — a decidir (ver T3).

---

## Parte 4 — Tensões a resolver (adiadas, com gatilho)

*Cada tensão leva um gatilho de resolução — não "um dia". Sem gatilho, uma tensão ou cai no esquecimento ou vira o próximo meta-projeto que incha antes de ser preciso. As três são reais e foram conscientemente adiadas; nenhuma bloqueia o uso das adições no seu caso simples.*

- **T1 — Cowork: "debate, não executes" vs. a sua função de delegar a agentes.** A instrução de modo estratégico colide aparentemente com a capacidade que justifica o Cowork (orquestrar multiagentes *é* uma forma de executar). Reconciliação provável: **não** executar *entregáveis operacionais* (documentos, código, dashboards), mas **poder** delegar *subtarefas analíticas* a consultores (research, crítica, análise) que alimentam a deliberação. A fronteira exata fica por cravar.
  **Gatilho:** *deep-search* ao funcionamento do Cowork — conduzido depois de definir por inteiro o que se quer e não se quer dele no braço estratégico — e cravado na **1ª ativação real** de um braço Cowork-estratégico.

- **T2 — Mecânica de duas superfícies numa só sessão estratégica.** Se cada sessão é dona de uma superfície (Parte 3), como é que uma sessão estratégica usa *tanto* o Projects (deliberar) *como* o Cowork (multiagente)? Posse sequencial (fecha numa, abre noutra), ramo, ou handoff de superfície a meio? A escolha condiciona como o `log-sessoes` regista a passagem.
  **Gatilho:** **1ª ativação real** de um braço Cowork-estratégico (mesmo momento de T1).

- **T3 — Formato do ID de superfície e encaixe no esquema de ID.** O sufixo de superfície (`-A`/`-B`) é **mais um eixo** sobre o esquema de ID já em desenho (`{F}-S{Label}-{n}` para fios principais + `{id_pai}-{tipo}-{m}` para branches). Tem de **encaixar** nesse esquema sem criar um quarto formato — senão regressa o ME-1 (relógio de sessão fragmentado), o defeito que o esquema único existe para matar.
  **Gatilho:** **fecho do esquema de ID de sessão** (já em debate noutra sessão).

---

*Fork-Return — v2. As decisões (Partes 1–2) estão decididas; as tensões (Parte 4) estão abertas, com gatilho. `status: em aberto` reflete as tensões, não as decisões.*
