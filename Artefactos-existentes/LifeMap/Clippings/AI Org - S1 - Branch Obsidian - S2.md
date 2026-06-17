---
title: "AI Org - S1 - Branch Obsidian - S2"
source: "https://claude.ai/chat/ede11ac3-95d6-4508-ad1e-1c62ef84d456"
author:
published:
created: 2026-06-14
description: "Claude conversation with 40 messages"
tags:
  - "clippings"
---
**Claude**

Vou retomar a partir do handoff. Antes de propor seja o que for, leio os canónicos como o handoff manda. A começar.

---

**You**

tenta de novo

---

**Claude**

O tool foi descarregado. Recarrego e tento de novo.

---

**You**

o que la ta na raiz ignora. fui eu que pus, mas nao deve servir de base. Agora importante: sobre comunicacao comigo: 1 tema de cada vez. se necessario varios temas, apresentas a lista com mini resumo e depois vais tema a tema. humanos nao leem 2 ou 3 paginas seguidas. e quando tratares os temas trata mece, até nivel 2. 4-5 conceitos max. (mindo piramid). entendido?

---

**Claude**

Entendido. Uma regra, aplico já: **1 tema de cada vez; se forem vários, dou a lista com mini-resumo e depois vamos um a um; Minto (resposta primeiro), MECE até nível 2, máx. 4-5 conceitos.** E ignoro o que está na raiz como base — construo a taxonomia a partir dos canónicos, não do que lá puseste.

Os temas em aberto para fechar a montagem (depois vamos um a um):

1. **Base & limpeza** — confirmar que ignoramos o scaffold existente e construímos limpo; o que sobrevive como *conteúdo* (Claude Skills, timeline-schema) e o que se apaga.
2. **Taxonomia & árvore** — validar os 4 níveis-1 (FERRAMENTAS·PROJETOS·CONHECIMENTO·SISTEMA) + tags + regra de profundidade.
3. **T-A · KB Notion** — catálogo fica no Notion / consolidado vem p/ o vault, vs migrar tudo.
4. **T-C · classificar projetos** — ambíguos (Casinhaaaa, etc.) + decisão "sem pasta VIDA, domínio vai em tag".
5. **T-D · taxonomia `topic`** — diferir para fork próprio (como o Mapa da Vida) ou fazer agora.

Restantes (fronteira vault/operador, front matter) não são decisões — entram na construção do CLAUDE.md.

Começamos pelo **tema 1**?

---

**You**

antes de mais nada: na sessao anterior ela leu mtos docs e inferiu pelos vistos uma estrutura e taxonomia. mas n debatemos. quero debater. PQ é que ta assim? e como é que arrumaria tudo o que viu (folders projetos, ideias, ferramenteas, etc). quero perceber o racionale. E antes de tudo isso: garantir que percebe pq que quero esta pasta do AI organization.

---

**Claude**

Antes de estrutura, o porquê. A minha leitura (confirma ou corrige):

**O vault existe para ser contrapeso ao teu tropismo conceptual** — um mapa humano e mínimo do teu trabalho com IA, para deixares de perder o fio. Quatro peças:

1. **Problema que resolve** — tens meses de projetos que nascem uns dos outros e incham (CTE→CWPP→wikis→WikiBuilder→Life Management). O trabalho está disperso por 3 sítios (disco, Claude Projects, Notion), as conversas são ilhas, e ao fim de semanas não sabes o que tens nem como se liga. O conceptual come o prático.
2. **O que é** — referência/mapa para a *tua* cabeça: Classe I (conhecimento consolidado) + Classe III (governança). Estado vive em ficheiros, não em chats.
3. **O que não é** — não é operador de execução (Classe II, isso é o Code/Life Management), nem mais uma meta-arquitetura. É deliberadamente **mínimo e fechável**.
4. **Para que serve no fim** — acumular arquitetura reutilizável (capital intelectual) rumo à tese de consultoria AI para capital não-tech. Acumula o capital; não substitui a prova (1 caso JSJ medido).

**A tensão honesta:** este vault *nasceu* do mesmo tropismo que diz combater ("organizar o mail" → meta-sistema AI). O risco real é ser ele próprio o próximo buraco conceptual. É exatamente por isso que "mínimo e fechável" não é estética — é a condição de não se trair.

É este o porquê, ou falha-me alguma coisa?

---

**You**

este foi o entendimento da sessao onde falei disto a primeira vez. diz se adiciona algo <contexto> Estou a montar um vault Obsidian de "AI Organization" para centralizar a minha governança de trabalho com IA. O vault já existe e está ligado ao Obsidian, em: C:\\Users\\JSJ\\Desktop\\GoogleDrive\\AI\\AI Organization (sincronizado via Google Drive). Está praticamente vazio — vamos estruturá-lo. Propósito do vault, três áreas: 1. TOOLS — notas sobre ferramentas de IA que uso/avalio (ex.: Understand- Anything, Graphify, karpathy-skills). 2. SISTEMA — conhecimento sobre o meu próprio sistema/workflow de IA (ex.: como funciona a pasta.claude, hierarquia de CLAUDE.md, etc.). 3. PROJETOS — uma pasta "projetos" com um.md por projeto, um index/MOC, e relações entre projetos via wikilinks do Obsidian. Sou engenheiro estrutural sénior; trabalho em PT por defeito. Quero tirar partido do Obsidian a sério: wikilinks \[\[ \]\], graph view, MOCs/index, tags, propriedades YAML, e uma pasta de templates. </contexto> <objetivo> Estruturar o vault e produzir um CLAUDE.md na raiz que sirva de manual operativo para QUALQUER agente de IA (eu, Claude desktop, Claude Code) saber o que o vault é, como o ler, e como nele registar informação. </objetivo> <metodo> 1. PRIMEIRO propõe a estrutura de pastas + lista de ficheiros a criar (templates incluídos) e espera a minha validação. NÃO crizes ficheiros antes de eu aprovar. 2. Depois de aprovada, cria a estrutura e os ficheiros no caminho acima. 3. No fim, dá-me um resumo do que foi criado e como abrir/navegar no Obsidian. </metodo> <requisitos\_obsidian> - index.md na raiz como Map of Content (MOC) principal, com wikilinks para os index de cada área. - Cada área tem o seu próprio index.md (MOC local). - Pasta de templates com, no mínimo: template de nota-de-tool, template de nota-de-projeto, e template de "resumo de sessão de projeto". - Relações entre projetos expressas por wikilinks \[\[ \]\] e tags, para o graph view ser útil. - Propriedades YAML (front matter) em TODAS as notas de conteúdo. </requisitos\_obsidian> <spec\_do\_CLAUDE.md> O CLAUDE.md da raiz é o entregável crítico. Tem de conter, em PT, de forma telegráfica e accionável: - PROPÓSITO: o que o vault é e as três áreas. - MAPA: árvore de pastas e para que serve cada uma. - PROTOCOLO DE LEITURA: por onde um agente começa (index.md → MOCs → seguir wikilinks) para se orientar antes de agir. - PROTOCOLO DE ESCRITA: \* Onde escrever cada tipo de informação (tool → área Tools; conhecimento de sistema → área Sistema; projeto → pasta projetos). \* Convenções de nomenclatura de ficheiros. \* Front matter OBRIGATÓRIO em cada.md novo, com os campos: created: YYYY-MM-DD HH:MM tags: \[\] area: \[tools|sistema|projetos\] relacionados: \[\] # wikilinks summary: > (1-2 linhas, descreve o conteúdo, não o processo) \* Workflow concreto "parei um projeto, regista resumo": qual template usar, em que pasta escrever, como nomear, e como ligar (wikilink) ao index de projetos. Descreve o passo-a-passo exato. \* Regra de não-destruição: nunca apagar/reescrever notas existentes sem pedido; acrescentar de forma cirúrgica e ligar via wikilink. - LÍNGUA: conteúdo em PT por defeito. </spec\_do\_CLAUDE.md> <restricoes> - Simplicidade primeiro: estrutura mínima que sirva os três objetivos. Sem pastas/abstrações especulativas que eu não pedi. Se 4 pastas chegam, não faças 9. - Mudanças cirúrgicas: não toques em nada fora do vault. - Output do trabalho em PT. </restricoes> <criterio\_de\_sucesso> Abro o vault no Obsidian e: (a) o graph view mostra relações reais entre notas; (b) o index.md leva-me a tudo; (c) um agente que leia só o CLAUDE.md consegue, sem mais contexto, registar um resumo de projeto no sítio certo e no formato certo. </criterio\_de\_sucesso>

---

**Claude**

Sim — e o mais importante que adiciona é uma **recalibração**: este prompt fundador é bem mais modesto e concreto do que o "porquê" que te devolvi. Eu importei camada conceptual de sessões posteriores.

O que ele adiciona/corrige:

1. **O porquê fundador é prático, não tese.** Querias 3 áreas (Tools / Sistema / Projetos), "tirar partido do Obsidian a sério" e um CLAUDE.md que funcione como manual. Zero menção a contrapeso-do-tropismo, Classes I/II/III, consultoria AI ou capital intelectual. Tudo isso é **acreção** de sessões seguintes — não estava na origem.
2. **Critério de sucesso concreto (novo para mim).** O teste real é *agent-actionability*: um agente que lê só o CLAUDE.md consegue registar um resumo de projeto no sítio e formato certos, sem mais contexto. Mais o graph útil e o index que leva a tudo. Isto é mais operacional do que o meu "mapa/referência".
3. **Uma restrição que muda o debate.** "Simplicidade primeiro; se 4 pastas chegam não faças 9; sem abstrações especulativas que não pedi." Isto **colide de frente** com a taxonomia que as sessões posteriores geraram (4 áreas + 3 vocabulários de tags `dominio` / `camada` / `topic` + Classes + schema de timeline).

A tensão honesta: **a distância entre o porquê fundador e o acreção é o teu tropismo a operar dentro do próprio projeto que devia combatê-lo.** Foi exatamente isto que pediste para vigiar.

Logo a pergunta de fundo para o debate de estrutura passa a ser clara: **qual porquê governa — o fundador (mínimo, 3 pastas) ou o acreção (4 + tags + classes + timeline)?**

Confirmas que o porquê fundador é este, e é por aqui que medimos "simples vs especulativo"?

---

**You**

NOTA: nao é tropismo a funcionar. tou a organizar o minimo. ja tenho o life map, ja pus os mails arrumados, e agora falta isto: é peça fundamental. eu uso AI todos os dias. e vou saltando de projetos em projetos (ou por necessidade pratica - para trabalho, ou pq descobri ferramenta q pode ajudar, ou pq preciso de arquitetura para conseguir que o projeto funcione. AI é um processo de aprendizagem e ssa aprendizagem passa por projetos, por estudo, etc). a necessidade imperial disto é exatamente saber o que tenho. ter a vista high level. senao perco-me em tocas. e se tiver 4 folders e chutar tudo para la fico na mesma: abro a pasta e vejo mil mds. essa logica de tags pressupoe que eu vou meter-me na toca do obsidian: grafos, etc. as pastas evitam exatamente isso! as sub pastas). agora - governa a versao final as 3 areas era uma forma de explicar. no entanto, repara so ta adicionado aí "conhecimento" nao ha mais nenhuma area nova. essas sao as nivel 1. e mesmo essas temos de pensar se fazem sentido. a pergunta certa para definir isso é: agrupas os folders, os projetos, as ferramentas como achas que fazem sentido dentro desses grupos - mas faz sub grupos nivel 2 ou 3 consoante o tema. para isso ve: "1. DAVID CONTEXTO - INTRODUCAO"; AI Life Map — Inventário de Ferramentas.md; e todos os ficheiro de C:\\Users\\JSJ\\Desktop\\GoogleDrive\\AI\\AI Organization\\MontagemVault-TEMP.

---

**Claude**

Aceito as duas correções — e a segunda muda o desenho: **a navegação é por pastas e subpastas, não por tags+graph.** Tags presumem que mergulho na toca do Obsidian; o que precisas é abrir uma pasta e *ver o que tens*, agrupado por tema. O meu modelo anterior era tag-cêntrico — errado para o teu uso.

Deixa-me ler o que mandaste antes de propor o agrupamento.

---

**You**

nota 1: tenho de ter um sitio para repositorio de contexto meu para dar a AI (podes ver como imaginei ja - na pasta Context-forAI e contexto é vario: é info pessoal tipo idade, onde vivo, trabalho etc, é info sobre trabalho pode ser de preferencias, o meu contexto no mundo AI - mto importante para uma sessao ou projeto saber o meu nivel, e tb de padroes de personalidade - mto relevante. portanto essa pasta encaixa onde? nota 2 - Projetos: podem ser por dominio sim. mas pergunta: nivel 2 é projetos feitos e projetos acabados? e depois os dominios la dentro? ou ao contrario? as duas fazem sentido. mas seria mto util saber que ferramentas ja fiz logo á mao. Conhecimento - é a mais facil e pode dividir-se em nivel 2 por: adquirido e por adquirir. mas a questao é: isto tem ligacao forte com as ferramentas. uma ferramenta (agentes por exemplo) fica onde? qto a sistema, concordo. mas aqui fica dividido em "consolidadeo" e nao consolidado"? e fica o q? as arquiteturas so, certo? ou seja, na governanca por exemplo fica o q? a arquitetura e o conhecimento que gerou a mesma ta em classe 1? e tao linkados?

---

**Claude**

As tuas 4 notas são, no fundo, **o mesmo problema: relações que cruzam pastas** ("agents fica onde?", "a tool que fiz é projeto ou ferramenta?", "a arquitetura e o conhecimento que a gerou estão linkados?").

**O princípio que resolve isto (é o teu — "um item, um sítio"):**

> Cada coisa vive **numa pasta só: a casa primária, definida pelo que a coisa *é*.** As relações cruzadas fazem-se por **1 wikilink no fim da nota** — não por duplicar em duas pastas, nem por grafo. Um link é barato e legível. É o *oposto* da toca.

Aplicado: "agents" fica numa casa (conceito que estudas → CONHECIMENTO; um agente concreto que usas → FERRAMENTAS) e **linka** para a outra. Nunca nas duas.

Aplico já à **Nota 1 — o teu contexto:**

Não encaixa nas 4 — é outra natureza: não é AI-artefacto, **és tu como input para o AI**. Recomendo **5ª área de topo: `CONTEXTO`** (já a separaste instintivamente em `Context-ForAI`; não é especulação, é necessidade real declarada — passa a tua própria regra). Subgrupos nível-2, espelhando o que descreveste:

- **pessoal** — idade, onde vivo, família
- **trabalho** — JSJ, papel, preferências
- **ai** — o teu nível/maturidade (o que uma sessão precisa de saber)
- **padrões** — personalidade/calibração (§7)

*Fronteira a vigiar (regra de ferro):* os factos pessoais talvez já sejam SSOT no **Cadastro** (Notion) → `CONTEXTO` **não duplica**; foca-se no *contexto-para-AI* (nível, padrões, preferências de trabalho com AI) e **linka** ao Cadastro. *Alt. rejeitada:* meter em SISTEMA — sujava SISTEMA, que é arquiteturas/governança, não input. Certeza: alta.

**Fila (um a um, mesmo princípio da casa-primária + wikilink):**

- **Nota 2 · Projetos** — nível-2 por *estado* (feitos/em-curso) ou por *domínio*? + ver "ferramentas que já fiz" à mão. → 2 opções com trade-off.
- **Nota 3 · Conhecimento** — *adquirido / por-adquirir* + a ligação às ferramentas.
- **Nota 4 · Sistema** — *consolidado / não-consolidado*, e o que lá vive (só arquiteturas? o conhecimento que as gerou está em Classe I e linkado?).

Seguimos pela **Nota 2**?

---

**You**

pode ficar no sistema. nao esta mal e sistema pode chamar-se arquitetura AI. e aí o contexto encaixa bem

---

**Claude**

Fechado: **SISTEMA → `ARQUITETURA AI`**, e `contexto` entra como subgrupo. Voltamos a 4 áreas de topo (FERRAMENTAS · PROJETOS · CONHECIMENTO · ARQUITETURA AI). O rename é até mais preciso: a área passa a ser *como a tua operação AI está arquitetada* — e os inputs (o teu contexto) são parte da arquitetura, tal como a governança.

Uma ressalva (não para travar — para decidires com olhos abertos): quem abre "Arquitetura AI" não espera "a minha idade" lá dentro; o subgrupo `contexto` sinaliza e resolve. E fica de pé a fronteira com o **Cadastro** (Notion): contexto aqui = *o que o AI precisa de saber* (nível, padrões, preferências de trabalho), sem duplicar os factos pessoais que já sejam SSOT no Cadastro — esses linkam-se.

ARQUITETURA AI fica com 2 famílias nível-2:

- **contexto** — pessoal · trabalho · ai · padrões
- **governança/arquitetura** — (o que lá vive exatamente trata-se na Nota 4)

Seguimos para a **Nota 2 (Projetos)**?

---

**You**

cadastro é outra coisa. é informacao "dura": informacoes de imoveis, que carros tenho, etc. isso n é contexto. é informacao especifica. nota 2 segue

---

**Claude**

Certo — Cadastro = informação dura (imóveis, carros…), não contexto. Cai a minha ressalva: `CONTEXTO` e Cadastro não se tocam.

**Nota 2 — Projetos**

**BLUF: estado *não* deve ser pasta de nível-2; nível-2 = domínio; o estado vive no front-matter; e "as ferramentas que fiz à mão" resolve-se em FERRAMENTAS, não aqui.**

1. **Domínio, não estado, no nível-2 — porquê.** O estado muda (em-curso → feito); pasta-por-estado = mover ficheiros sempre que muda (churn). E procurar "o que tenho em JSJ" obrigava a varrer 3 pastas de estado. **Domínio é estável** e é a forma natural de *ver o que tens por área*. O estado captura-se num campo `status:` — e dá-te "só os feitos" numa vista trivial quando precisares, sem mover nada.
2. **PROJETOS nível-2 = domínio:** `jsj-engenharia` · `meta-ai-governanca` · `vida`. Nível-3 só se um domínio pedir (ex.: `jsj-engenharia/ssot`) — assimetria OK.
3. **"Ferramentas que já fiz, à mão" → vive em FERRAMENTAS, não em PROJETOS.** Uma tool que construíste e usas *é uma ferramenta*. FERRAMENTAS ganha um grupo **`construídas`** (distinto das externas que avalias); abres e vês tudo o que fizeste, à mão, em pastas puras. (O interior de FERRAMENTAS detalha-se quando lá chegarmos.)
4. **Casa primária de uma tool que fizeste — decisão tua.** Tem 2 faces: *como a construí* (história/decisões/sessões) e *o que faz / quando uso*.
	- **(a)** casa em PROJETOS, cartão fino em FERRAMENTAS/ `construídas` a linkar. ← **recomendo**: o registo de projeto é mais rico e é onde os resumos de sessão caem.
		- (b) casa em FERRAMENTAS, nota de história em PROJETOS a linkar.
	Em qualquer caso: 1 item, 1 casa, 1 wikilink.

Confirmas **domínio no nível-2 + `construídas` em FERRAMENTAS + casa (a)**? Seguimos para a **Nota 3**?

---

**You**

nos projetos é faci os dominios: é ver o mapa da vida. por isso tem de ser: JSJ, AI (e dentro de AI ha varios), Vida faz quase sentido mas para ja ta bem. a casa da tool: Ferramentas (e aí distinguir por classes) e nas ferramentas linkagem para os projetos

---

**Claude**

Fechado.

**Domínios = Mapa da Vida, colapsado para o que este vault tem:** `JSJ` · `AI` · `VIDA`. (VIDA fica como está — "para já tá bem"; refina-se se um dia pedir.)

**Dentro de AI (nível-3), provisório** — afino quando metermos os projetos reais (montar ≠ melhorar):

- `governanca` — CWPP, wiki-ai-evolution
- `tooling-pipelines` — DOC-ENGINE, Docling, Notion-auto, chunkers
- *(o resto emerge ao popular)*

**Casa da tool = FERRAMENTAS** (a tua opção, aceite), distinguida por classes, com link para o projeto. Forma resultante de uma tool que construíste:

- **FERRAMENTAS/** `<classe>` **/MQT-AI** → o que faz, quando uso *(casa da identidade-ferramenta)* —linka→
- **PROJETOS/AI/MQT-AI** → história, decisões, **resumos de sessão** *(casa do percurso; é aqui que vivem os nós da timeline)*

2 faces, 2 notas, 1 wikilink — não é duplicação (o que faz ≠ como a construí). Regra geral: tool sem história rica = só nota em FERRAMENTAS; projeto conceptual sem produto = só em PROJETOS; **ambas** só quando existem as duas faces.

**1 ponto por definir (fica para o tema FERRAMENTAS):** "distinguir por classes" — que classes? As do teu Inventário (A–J)? Papel-na-stack? Origem (externas/construídas)? Decido contigo quando lá chegarmos.

Seguimos para a **Nota 3 (Conhecimento)**?

---

**You**

sim

---

**Claude**

**Nota 3 — Conhecimento**

**BLUF: nível-2 deve ser por *tema*, não por adquirido/por-adquirir — pelo mesmo motivo que decidimos há um minuto nos Projetos (estado ≠ pasta). E "agents fica onde" resolve-se com a regra da casa-primária.**

1. **adquirido/por-adquirir é estado, não pasta — consistência com a Nota 2.** "Por-adquirir" vira "adquirido" quando aprendes → churn; e abrir "adquirido" dá uma gaveta sem tema. Pior: *por-adquirir não é conhecimento* — é um **roadmap de lacunas** (é o teu Inventário A–J). Conhecimento adquirido acede-se por **tema**; lacunas acedem-se por **lista**. São coisas diferentes.
2. **CONHECIMENTO nível-2 = tema** (os teus domínios clássicos do §4, criados à medida que entram): `arquitetura-conhecimento` · `classes-conhecimento` · `documentos-canonicos` · `comportamento-modelos` (janela cognitiva, incongruência) · `agentes`. O estado vai em `status: adquirido|por-adquirir` → dá-te a vista "o que me falta" sem mover nada. O Inventário A–J vive como **1 nota-roadmap**, não como pasta.
3. **"Agents fica onde?" → casa-primária:** o *conceito* (o que são agentes, orquestração) → `CONHECIMENTO/agentes`; a *tool concreta* (subagentes do Code, um framework) → FERRAMENTAS. Linkam-se. Nunca nas duas.
4. **A "ligação forte" com ferramentas, afinada:** conhecimento *geral/durável* → CONHECIMENTO; o *how-to específico de uma tool* (como configuro o litellm) → **dentro da nota da tool**, porque é sobre aquele instrumento. Fronteira limpa: **conceito = CONHECIMENTO; operar-uma-tool = na tool**.

*Recomendo tema no nível-2 + estado em front-matter.* Se preferires mesmo adquirido/por-adquirir como pasta, o custo é o churn + temas espalhados — tua decisão.

Nota: a ligação CONHECIMENTO ↔ ARQUITETURA AI (o saber geral vs a tua arquitetura) é exatamente a **Nota 4**. Seguimos?

---

**You**

SIM (NOTA, ISTO NAO É AINDA O FINAL. DEPOIS QUERO UM MAPA DE COMO FICAVAM OS FOLDERS, PROJETOS, ETC

---

**Claude**

SIM. (Anotado: **isto ainda não é o final** — quando fecharmos as notas, faço-te o **mapa completo** — folders + projetos + ferramentas + exemplos — para validares antes de qualquer criação.)

**Nota 4 — Arquitetura AI**

**BLUF: consolidado/não = estado, não pasta (3ª vez o mesmo padrão); nível-2 = `contexto` · `governanca` · `stack`; e a arquitetura é Classe III — não I. O saber geral que a gerou é que é Classe I, noutra casa, linkado.**

1. **consolidado/não-consolidado = estado, não pasta.** Terceira vez o mesmo padrão (Projetos, Conhecimento, agora aqui): estado muda e espalha. Vai em `status: consolidado|candidato` no front-matter (espelha o teu ledger D-NNN/G-NNN). Nível-2 é temático.
2. **ARQUITETURA AI nível-2 = 3 subgrupos:**
	- `contexto` — (já decidido: pessoal · trabalho · ai · padrões)
		- `governanca` — as **regras**: CWPP, ledgers, separação de atores, não-duplicação, disciplina de docs canónicos
		- `stack` — a **arquitetura do setup**: modelo dos 3 ficheiros, divisão de papéis (Opus/Code/Notion/Obsidian), `.claude`, MCP
3. **O que fica aqui = a arquitetura e as regras (Classe III), não o conceito geral.** "As 3 classes" como *conceito* → CONHECIMENTO; a tua *aplicação* delas (atribuir atores no teu sistema) → aqui. Regra de facetas, outra vez.
4. **Q4, a parte que importa — arquitetura e o saber que a gerou NÃO são a mesma classe:**
	- A **decisão/arquitetura** (ex.: "I+III→humano, II→LLM") = **Classe III** → `governanca`. Inclui o *seu próprio porquê* (a razão específica do teu sistema).
		- O **saber geral durável** por baixo (ex.: "organizar para máquina ≠ para humano; a fronteira é real") = **Classe I** → CONHECIMENTO.
		- **Linkados:** a decisão aponta para o conceito que a fundamenta; o conceito aponta para as decisões que gerou.
	Logo: nem tudo o que "gerou" a arquitetura é Classe I — só a parte *geral*. O resto é a fundamentação da decisão, que vive na própria nota. É o teu modelo de classes a traçar a fronteira.

Confirmas a Nota 4? Confirmado, monto-te o **mapa completo** para validares.

---

**You**

fui aos projetos em que mais trateir de governanca e perguntei como fariam. aqui tens as respostas: 1) Desktop confirmado. \*\*Fora de scope deste projecto\*\* — não toco em Tarefa A/B/C nem nos ficheiros do wiki-ai-evolution. Trato isto como design standalone, informado pela governança que aqui se acumulou. Não corro o resto do arranque (irrelevante para a pergunta). --- \*\*BLUF:\*\* a escolha real não são os nomes — é o \*\*eixo de partição\*\* de nível 1. MECE vive ou morre aí. Dou-te dois eixos viáveis + o que parece óbvio mas quebra MECE. ## Candidato 1 — eixo ASPECTO/FUNÇÃO (o que a governança regula) `  governanca/ ├── decisao/ │   ├── registo/          # formato D-NNN, write-ahead, decision records │   ├── mutacao/          # como o canon muda, revisão explícita │   └── vocabulario/      # fixação de vocabulário, zero-expansão ├── regras/ │   ├── ledger/           # G-NNN, classificação, estados provisional/active │   ├── invariantes/      # fundamento, pilares imutáveis │   └── jurisdicao/       # fronteiras de scope, o-que-vive-onde, tiers ├── estado/ │   ├── handoff/          # handoff/context, continuidade inter-sessão (Reter) │   ├── arranque/         # boot protocols │   └── fecho/            # close protocols, critérios de fecho literais ├── verificacao/ │   ├── auditoria/        # protocolos de audit, lint │   ├── gate/             # gate Lakatosiano, critérios de promoção │   └── content-aware/    # verificação por turno, anti verification-theater └── falhas/     ├── tensoes/          # casos T-NN     └── anti-padroes/     # scope drift, premature conclusion, verification-theater  ` Pergunta de sorting: \*"que aspecto de governança é que isto regula?"\* — a mais instintiva. \*\*Costura única:\*\* "critérios de fecho literais" cabe em `estado/fecho` \*\*e\*\* `verificacao/auditoria`. Resolve com casa primária + cross-link no front-matter (`related:`). É a única ambiguidade material. ## Candidato 3 — eixo CAMADA DE ABSTRAÇÃO (que tipo de coisa é) `  governanca/ ├── principios/    # verdades durável, agnósticas (write-ahead, dualidade de clientes, Reter=3ª função) ├── protocolos/    # protocolos nomeados: CWPP, boot, close, mutação ├── mecanismos/    # instrumentos: ledger G-NNN, handoff, gate, verificação content-aware └── casos/         # incidentes: T-NN, lições, post-mortems  ` Pergunta de sorting: \*"isto é uma verdade, um protocolo, uma ferramenta, ou um caso?"\* Tipos disjuntos → \*\*MECE quase perfeito, costura ≈ zero\*\*. Margem fuzzy só em `mecanismo vs protocolo`. Escala melhor: poucos baldes de topo, absorve N projectos sem inchar. ## O trap — eixo CICLO DE VIDA `setup / operacao / preservacao / fecho / meta`. Intuitivo, mas \*\*quebra MECE\*\*: verificação recorre em operação \*e\* fecho → duplicas ou arbitras. Não uses como nível 1. ## Recomendação | Se… | Usa | |------|-----| | Sortes por \*"o que isto regula"\* e o repo fica governança-de-projectos-AI | \*\*Cand. 1\*\* — mapeia ao teu "cada aspeto", sorting instintivo, custo = 1 costura | | Esperas largura/longevidade e queres mínima manutenção de fronteiras | \*\*Cand. 3\*\* — 1 juízo por ficheiro, mas costura ≈ zero | Inclino-me para \*\*Cand. 1\*\* pela tua formulação ("cada \*aspeto\*"), com a costura `fecho↔auditoria` resolvida por convenção fixa logo no README (decisão antes de aplicação — D-016). Queres que gere o scaffold? Como é Desktop, posso dar-te prompt para agente IDE com script de criação de pastas + `README.md` de raiz com a regra de sorting e o front-matter-padrão. Confirma o candidato e crio.;;;; 2)

---

**Claude**

Estas duas respostas são sobre o **mesmo ramo**: o *conhecimento-de-governança* (Classe I) — ou seja, o subgrupo `governanca` dentro de **CONHECIMENTO**. Não reabrem nada; detalham um ramo que é mais fundo que os outros. Dois sinais fortes saltam à vista.

1. **Onde isto vive (confirma a Nota 4, não a reabre).** Ambas estruturam *conhecimento sobre governança* = Classe I → `CONHECIMENTO/governanca/`. A descompressão di-lo à letra: "Classe 1… **NÃO organizar a base como a maquinaria que descreve**." Isto **confirma** a fronteira que fechámos: conhecimento-de-governança ≠ a tua governança *implementada* (CWPP, ledger D/G vivo), que fica em `ARQUITETURA AI/governanca`. Mesma matéria, classes diferentes, linkadas.
2. **Sinal 1 — convergência.** Dois projetos independentes caem no mesmo eixo (*por pergunta / camada de abstração*):
	- Descompressão Eixo C: `fundamentos` · `mecanismos` · `casos`
		- Resposta 1 Cand. 3: `principios` · `protocolos` · `mecanismos` · `casos`
	Quase idênticos — a própria Resposta 1 diz que o Cand. 3 é "MECE quase perfeito, costura ≈ zero, escala melhor". Quando dois sítios diferentes convergem no mesmo eixo, é o eixo.
3. **Sinal 2 — a opção "recomendada" da Resposta 1 viola a tua regra raso.** O Cand. 1 (por aspeto: decisao/regras/estado/verificacao/falhas) vai a **3 níveis de pasta** (`governanca/decisao/registo/`). Colide de frente com o princípio que a *outra* resposta e tu fixaram: "híbrido raso — pasta só ao topo, ficheiro atómico como folha; o 3º nível são secções dentro do.md." **Rejeito a profundidade do Cand. 1.** Governança é exatamente onde o teu tropismo entra; a árvore de 3 níveis é ele a tentar entrar pela porta das traseiras.
4. **Recomendação — `CONHECIMENTO/governanca/`** (o ramo mais fundo, por necessidade real; assimetria OK):  
	`fundamentos` · `mecanismos` · `casos` — o núcleo convergente. Ficheiro atómico como folha (drift/supersession →.md em `fundamentos`; ledger/tiers/handoff →.md em `mecanismos`). Arranque mínimo: abre só `fundamentos` + `mecanismos`; `casos` só ao 2º caso real.
	- Sorting: *"o que é X"* → fundamentos · *"como faço X"* → mecanismos · *"o que aconteceu aqui"* → casos.
		- `casos/` = a **lição durável**; a história completa do projeto fica em `PROJETOS/AI/governanca`, linkada.
		- "protocolos" (do Cand. 3) **não** entra aqui — o CWPP como protocolo *teu implementado* é ARQUITETURA AI, não Classe I.

Nota: o teu **"2)" ficou vazio** — se há segunda resposta, manda que integro antes do mapa.

Confirmas `fundamentos/mecanismos/casos` para o ramo governança do CONHECIMENTO? Confirmado, **monto o mapa completo** (folders + projetos + ferramentas + exemplos) para validares.

---

**You**

ta aqui

---

**Claude**

Esse "2)" é a **mesma** descompressão doc que já tinha em mão — nada novo, já integrada. Aliás reforça: ela recomenda o **Eixo C** = exatamente o `fundamentos/mecanismos/casos` que propus. Com isto, os dois inputs estão dentro e convergem. Tomo `fundamentos/mecanismos/casos` como fechado e dou-te o que pediste.

**Rascunho do mapa — para reagires. Não crio nada até validares.**

```
AI Organization/
├─ CLAUDE.md                         manual do vault (entregável crítico)
├─ index.md                          MOC raiz → liga aos 4 index de área
├─ _templates/                       nota-tool · nota-projeto · resumo-sessao
│
├─ FERRAMENTAS/
│   ├─ index.md
│   └─ «classes — POR DEFINIR»       ÚNICO ponto em aberto (ver nota abaixo)
│       p.ex. construidas/  externas/  …
│       construidas/MQT-AI.md  ──link──▶ PROJETOS/AI/tooling-pipelines/MQT-AI
│
├─ PROJETOS/                         (1 nota/pasta por projeto; estado = front-matter)
│   ├─ index.md
│   ├─ JSJ/
│   │   ├─ CTE/                       (índice + resumos-sessão = nós da timeline)
│   │   └─ SSOT.md
│   ├─ AI/
│   │   ├─ governanca/               CWPP, wiki-ai-evolution
│   │   └─ tooling-pipelines/        DOC-ENGINE, Docling, Notion-auto
│   └─ VIDA/                         Siena-frances, David-2.0  (provisório)
│
├─ CONHECIMENTO/                     Classe I durável (geral, não-tu)
│   ├─ index.md
│   ├─ _roadmap-aprendizagem.md      Inventário A–J (o "por-adquirir")
│   ├─ governanca/                   ▸ ramo mais fundo (nível-3, por necessidade)
│   │   ├─ fundamentos/              classes-conhecimento, primitivos, modos-falha
│   │   ├─ mecanismos/               ledger, tiers, handoff
│   │   └─ casos/                    (só ao 2º caso real) → link a PROJETOS
│   ├─ comportamento-modelos/        janela cognitiva, incongruência
│   ├─ documentos-canonicos/
│   ├─ arquitetura-conhecimento/
│   └─ agentes/
│
└─ Arquitetura AI/                   Classe III + o teu input (ex-"Sistema")
    ├─ index.md
    ├─ contexto/                     pessoal · trabalho · ai (nível) · padroes (§7)
    ├─ governanca/                   IMPLEMENTADO: CWPP teu, ledger D/G vivo, regras
    └─ stack/                        3 ficheiros, divisão de papéis, .claude, MCP
```

**Convenções transversais (a entrar no CLAUDE.md):**

- **Estado = front-matter**, nunca pasta: `status:` cobre em-curso/feito · adquirido/por-adquirir · consolidado/candidato.
- **Cruzamentos = 1 wikilink** (casa-primária + link). Nunca duplicar.
- **Profundidade:** máx. 2 níveis — exceção única `CONHECIMENTO/governanca` (3 níveis, por pressão real). Assimetria OK.
- **Arranque mínimo:** só se criam pastas com conteúdo; ex. governança abre só `fundamentos/` + `mecanismos/`.

**O único ponto que falta decidir:** FERRAMENTAS "por classes" — que eixo?

1. **Origem** — construidas / externas (simples, bate no teu "ver o que fiz à mão")
2. **Papel-na-stack** — estratégia/operação/apresentação/organização/infra
3. **Classes A–J** do teu Inventário (risco: é toolbox, não taxonomia — podes cair em tropismo)

Reage ao mapa: o que mudas? E qual eixo para FERRAMENTAS?

---

**You**

arquitetura sugiro o seguinte: nivel 1: o que resolve? comunicacao entre agentes, protocolos de memoria, regras de arquitetura de informacao (ex: regras para doc canonicos, etc) protocolos de projetos de codigo, de projetos de estrategia, etc

---

**Claude**

Adoto o teu eixo **"o que resolve?"** para a Arquitetura AI — é melhor que o meu `governanca/stack` abstrato: concreto e navega-se por instinto. Mas tem **uma falha MECE** a corrigir, e o `contexto` a reposicionar.

1. **Concedido — funções por "o que resolve":** `comunicacao-agentes` · `memoria` · `arquitetura-informacao` (regras de docs canónicos, precedência, não-duplicação) · …
2. **A falha MECE (a única).** A tua lista mistura **dois cortes**: por **função** (comunicação, memória, arq-informação) e por **tipo de projeto** (código, estratégia). Um *protocolo de memória para um projeto de código* pertence aos dois → costura. Como está, não é MECE.
3. **Resolução — a regra de sempre (casa-primária + link).** As **funções são as casas** (cada nota vive na função que *mais* resolve). Os **protocolos-de-projeto** (código, estratégia = o teu CWPP) são **composições**: notas finas que *linkam* às funções que montam. Sorting: *"isto é uma função-primitiva ou uma receita-de-projeto?"* — casa onde mais é, o resto por wikilink.
4. **`contexto` fica fora deste eixo.** Não "resolve" nada — é input. Mantém-se como bucket próprio ao lado das funções, senão fica órfão.

Mapa resultante:

```
Arquitetura AI/
├─ contexto/                  pessoal · trabalho · ai · padroes
├─ comunicacao-agentes/       handoff inter-agente, passagem de contexto
├─ memoria/                   continuidade, 3 ficheiros, ledger
├─ arquitetura-informacao/    docs canónicos, precedência, não-duplicação
├─ protocolos-projeto/        composições → linkam às funções acima
│   ├─ codigo.md
│   └─ estrategia.md          (CWPP)
└─ … (mais funções emergem por pressão real, não antecipação)
```

O teu antigo "stack" dissolve-se nas funções, nada se perde: 3-ficheiros → `memoria`; divisão de ambientes (Opus/Code/Notion/Obsidian) → função `orquestracao` (emerge); `.claude` /MCP → função `infra` (emerge).

Confirma: **eixo "o que resolve?" + funções-como-casa + protocolos-projeto-como-composição + contexto à parte?**

---

**You**

ainda n adoro, mas repara o q é que eu quero por aí? regras. templates, frameworks, etc. Por exemplo ramo governanca - ramos: arquiteturas, Regras, templates, instrucoes de projeto, etc; memoria: Por wikis, por vetores, etc; MEmoria - intra projeto; inter projetos, continuidade (ficheiros tipo, instrucoes, etc), Codigo - Pyton, htlm,etc - ferramentas, frameworks, regras de construcao, etc

---

**Claude**

"Ainda não adoras" — e percebo o que falhei: andei em **funções abstratas**, quando o que pões aí são **assets reutilizáveis** (regras, templates, instruções, arquiteturas). Isso muda o desenho: é uma grelha de 2 eixos — **função (o que resolve) × tipo de asset**. Adoto, com dois travões.

1. **A grelha.** L2 = **função**: governança · memória · comunicação-agentes · código · estratégia. L3 = **tipo de asset** — vocabulário fixo e pequeno, igual em *todas* as funções → sabes sempre onde pôr. L4 = o ficheiro (o asset).
2. **Tipos de asset (L3), apertados para MECE:** `arquiteturas` (como/porquê está desenhado) · `regras` (constrangimentos, precedência) · `templates` (scaffolds a preencher) · `instrucoes` (procedimentos a correr). **Cortei "frameworks"** — um framework é uma arquitetura *ou* uma instrução; manter as duas é a costura por onde drifta.
3. **A tua memória ia espalhar-se — travo (anti-tropismo).** "por wikis / por vetores", "intra/inter/continuidade" **não são pastas** — são **ficheiros** dentro do tipo de asset certo: `memoria/instrucoes/memoria-por-vetores.md`, `…/continuidade-3-ficheiros.md`. O sub-tópico vive no *nome do ficheiro*, não em mais um nível de pasta. Senão a árvore não pára.
4. **A profundidade extra (3-4 níveis) justifica-se aqui** — ao contrário do CONHECIMENTO. É uma **biblioteca de assets** que cresce (muitos templates/regras), não uma base destilada. Bibliotecas ganham com pastas; bases destiladas não. Bicho diferente, regra diferente — concedo a exceção.

```
Arquitetura AI/
├─ contexto/                    (à parte — input, não asset)
├─ governanca/
│   ├─ arquiteturas/   separacao-atores.md
│   ├─ regras/         docs-canonicos.md · nao-duplicacao.md
│   ├─ templates/      ledger-DG.md
│   └─ instrucoes/     arranque-projeto.md · CWPP.md
├─ memoria/
│   ├─ arquiteturas/   intra-vs-inter-projeto.md
│   ├─ instrucoes/     memoria-por-vetores.md · por-wikis.md · continuidade-3-ficheiros.md
│   └─ templates/      3-ficheiros.md
└─ codigo/
    ├─ regras/         construcao-limpa.md
    ├─ templates/      …
    └─ instrucoes/     …
```

**Fronteira (consistência):** "ferramentas/frameworks de código" que *usas* (pyRevit, libs) → **FERRAMENTAS**, não aqui. `codigo/` aqui = só os **assets que tu autoraste** para governar projetos de código (regras de construção, templates, instruções). Linkam-se.

Confirma a grelha **função × tipo-de-asset (4 tipos)**, sub-tópicos no nome do ficheiro, código-tools em FERRAMENTAS?

---

**You**

parece bem para comecar. depois quando comecarmos a por la, logo se ve.

---

**Claude**

Arquitetura AI fica **provisória** — afinamos ao popular, como dizes. Falta **uma única área**: FERRAMENTAS (o "por classes" que ficou em aberto). Fecho-a e temos o desenho completo.

**Recomendação: L2 = origem · L3 = papel-na-stack.**

1. **L2 = origem:** `construidas/` · `externas/`. Serve diretamente o teu "ver o que já fiz, à mão" — pasta pura, sem index nem filtro.
2. **L3 (dentro de `externas/`) = papel-na-stack** — o teu próprio modelo do §3: `estrategia` (Opus/Projects) · `operacao` (Code) · `apresentacao` (Notion) · `organizacao` (Obsidian) · `infra` (MCP, git, litellm, docling).
3. **"Em avaliação" = `status:`, não pasta** (é estado — padrão de sempre). **A–J descartado**: o próprio Inventário diz que é *toolbox, não taxonomia* → usá-lo como pastas seria o tropismo a entrar.

```
FERRAMENTAS/
├─ index.md
├─ construidas/        MQT-AI.md · SSOT.md   (link → PROJETOS; papel em front-matter; só vira L3 se crescer)
└─ externas/
    ├─ estrategia/
    ├─ operacao/
    ├─ apresentacao/
    ├─ organizacao/
    └─ infra/
```

**Porquê origem no topo e não papel:** a tua prioridade declarada é *ver o que construíste*. Papel ao topo misturava com origem (uma tool que fizeste tem ambos → não-MECE); escolhemos uma casa (origem), a outra dimensão vive em front-matter. Assimetria `construidas` (poucas) vs `externas` (muitas) é OK.

Com isto, **as 4 áreas estão desenhadas**. Queres o **mapa consolidado final** — 4 áreas + convenções + spec do CLAUDE.md — para o último olhar antes de eu criar fosse o que for?

---

**You**

Vais gerar um mapa hierárquico em Markdown no formato EXATO definido abaixo, para ser importado por uma aplicação. Quero que geres o mapa de acordo com todas as hierarquias e taxonomia que definimos até aqui. A resposta deve ser APENAS o ficheiro MD — nada antes, nada depois, sem `  à volta, sem explicações. ═══ FORMATO OBRIGATÓRIO ═══ A resposta tem exatamente esta forma:   # Versao <VERSÃO>   # Estrutura   - <nó raiz 1>     - <filho>       - <neto>   - <nó raiz 2>     ... Regras (todas obrigatórias): 1. As duas primeiras linhas são headings literais:      • Linha 1: "# Versao <VERSÃO>"   (substitui <VERSÃO> por uma etiqueta curta:        ex. "v1", "rascunho-2025-01", "proposta")      • Linha 2: "# Estrutura" 2. Linha 3 em branco. A partir da linha 4 é tudo lista de bullets. 3. Cada nó é UMA linha que começa por "- " (hífen + espaço). 4. Indentação: EXATAMENTE 2 espaços por nível.      • Filho = pai + 2 espaços.      • Irmãos = mesmíssima indentação.      • NUNCA usar tabs. NUNCA misturar 2 e 4 espaços para o mesmo nível. 5. NÃO usar numeração de secção como prefixo dos nomes ("1.", "1.1", "2.3",    "2025.08") — a app remove-a. Se quiseres números, escreve-os sem ponto:    "1 Fte", "4 Taste", "2025 Plano" são permitidos. 6. Emojis dentro dos nomes são permitidos e recomendados nos nós de nível 1    para destacar categorias (ex.: "💚 SAÚDE", "🏠 PATRIMÓNIO", "💼 WORK"). 7. Outros caracteres válidos dentro dos nomes: acentos, espaços, "/", ":",    "&", parêntesis, hífen, ponto, dígitos. Ex.: "R/C Esq", "4 Taste",    "Gamma.AI", "Festas & Eventos", "MGB GT". 8. A ordem dos irmãos é preservada — escreve-os pela ordem que queres ver. 9. PROIBIDO: outros headings (##, ###), listas numeradas (1. , 2. ),    listas com "*" ou "•", blocos de código, citações ">", linhas em branco    no meio da lista, comentários, texto narrativo, ou nomes duplicados    entre irmãos do mesmo pai. ═══ EXEMPLO VÁLIDO ═══ # Versao v1 # Estrutura - 💚 SAÚDE   - Saúde Clínica   - Saúde Mental   - Bem-Estar     - Relaxamento     - Cuidado Pessoal - 🏠 PATRIMÓNIO   - Imóveis     - Tv. dos Moinhos       - 1 Fte         - Cadastro         - Manutenção       - 1 Dto         - Cadastro         - Manutenção     - Calçada da Boa Hora       - R/C Esq         - Casa         - Jardim   - Automóvel     - Fiat       - Manutenção       - Seguro ═══ ERROS COMUNS A EVITAR ═══ ✗ Não fazer:    # Mapa de áreas         ← heading que não seja "# Versao …" / "# Estrutura" ✗ Não fazer:     `markdown … \`\`\` ← envolver em bloco de código ✗ Não fazer: 1. SAÚDE ← lista numerada, ou prefixo "1." num nome ✗ Não fazer: \\t- Imóveis ← tabs em vez de espaços ✗ Não fazer: "Aqui está o mapa:" ← texto narrativo antes ou depois ✗ Não fazer: irmãos com indentação diferente (uns 2 espaços, outros 4) ═══ AUTO-VERIFICAÇÃO (antes de responder) ═══ Antes de finalizares, confirma: □ As duas primeiras linhas são "# Versao …" e "# Estrutura". □ Há exatamente uma linha em branco depois dos headings; nenhuma no meio da lista. □ Cada filho tem exatamente +2 espaços face ao pai. □ Nenhuma linha tem tabs. □ Nenhum nome começa por "N." ou "N.N " (numeração de secção). □ Não há nada além do MD na resposta.

---

**Claude**

## Versao v1

## Estrutura

- 🧰 FERRAMENTAS
	- construidas
		- externas
		- estrategia
				- operacao
				- apresentacao
				- organizacao
				- infra
- 📁 PROJETOS
	- JSJ
		- AI
		- governanca
				- tooling-pipelines
		- VIDA
- 📚 CONHECIMENTO
	- governanca
		- fundamentos
				- mecanismos
				- casos
		- comportamento-modelos
		- documentos-canonicos
		- arquitetura-conhecimento
		- agentes
- 🏛 ARQUITETURA AI
	- contexto
		- pessoal
				- trabalho
				- ai
				- padroes
		- governanca
		- arquiteturas
				- regras
				- templates
				- instrucoes
		- memoria
		- arquiteturas
				- regras
				- templates
				- instrucoes
		- comunicacao-agentes
		- arquiteturas
				- regras
				- templates
				- instrucoes
		- codigo
		- arquiteturas
				- regras
				- templates
				- instrucoes
		- estrategia
		- arquiteturas
				- regras
				- templates
				- instrucoes

---

**You**

da-me u.md para download exatamente como te indiquei antes. os bullets devem ser hiffens

---

**Claude**

Sem front matter de propósito — quebraria o formato de import que definiste.

---

**You**

agora faz o seguinte: popula esse mapa dentro das categorias que tem todoso os elementos (folders, etc) para ver como fica e da md para download

---

**Claude**

4 coisas a reteres (o ficheiro é limpo; estas notas ficam só aqui):

1. **As tools que construíste aparecem 2x — de propósito.** Face-ferramenta em `FERRAMENTAS/construidas`, face-projeto em `PROJETOS` (MQT-AI, SSOT, DOC-ENGINE, GestaoDesenhos, Memorias). É o desenho "2 faces, 1 link" que validámos. Vê na app se a repetição te incomoda visualmente — se sim, colapsamos para uma só.
2. **Deixei de fora 3 que não sei o que são:** `Casinhaaaa`, `Emergencia Lisboa`, `GESTAO PORTFOLIO`. Diz-me o que são + se têm artefacto AI durável, e coloco. `AI - Misc Stuff` ficou fora de propósito (gaveta — falha "estabilidade").
3. **Engenharia JSJ pura está fora** (Entrecampos, Marquês de Pombal, etc.) — este vault é da tua operação *AI*, não o repositório de projetos de estruturas. Em `PROJETOS/JSJ` só entram os projetos AI-tool / AI-doc. Confirma que é o que queres.
4. **Folhas de CONHECIMENTO e ARQUITETURA AI são representativas, não exaustivas** — os conceitos/assets que já apareceram no percurso. Crescem por pressão real ao popular.

`Secil 2026` meti em `PROJETOS/JSJ` (palpite: candidatura/prémio) — corrige se for carreira-OE.

---

**Claude**

AI Map