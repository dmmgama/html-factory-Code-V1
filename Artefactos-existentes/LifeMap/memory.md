# memory.md — decisões e o seu porquê

Registo persistente do *porquê* das decisões de arquitetura/design. Não é estado corrente
(isso vive em `handoff.md`/`context.md`). Cada entrada: decisão + razão.

---

## D1 — App single-file, sem build/dependências
**Decisão:** tudo (HTML+CSS+JS) num único `lifemap_lab.html`, vanilla.
**Porquê:** portabilidade máxima (abrir num browser, sem instalação), simplicidade, fácil
de partilhar/versionar. Preferência explícita do utilizador por ficheiro único.

## D2 — Formato MD canónico sem numeração
**Decisão:** `# Versao <V>` + `# Estrutura` + lista de bullets (2 espaços/nível), sem `1`,`1.1`.
**Porquê:** consistência entre todas as tabs e legibilidade; facilita copiar estruturas entre
sistemas e gerar/consumir com LLMs. (Estabilizado na v5–v7.)

## D3 — `PATH_SEP = ''` (separador de path vazio)
**Decisão:** ids construídos por concatenação de nomes sem separador visível.
**Porquê:** permitir nomes que contêm `/` (ex.: "R/C Esq") sem partir o parsing de path.

## D4 — Render parametrizado por `tabId`
**Decisão:** toda a renderização (árvore, mind map, side) recebe `tabId`; estado vive em
dicionários por-tab.
**Porquê:** adicionar um novo mapa custa quase nada — basta registar o `tabId` nos literais de
estado + dados + HTML/CSS, sem lógica nova. Validado ao acrescentar o Obsidian na v12.

## D5 — Persistência só em memória (Save) + export MD como save durável
**Decisão:** não usar `localStorage`/servidor; "Save" guarda snapshots em memória; persistência
real é exportar `.md` e reimportar.
**Porquê:** mantém a app 100% estática e portável. **Consequência aceite:** recarregar/fechar
apaga as versões em memória — o utilizador tem de exportar `.md` para não perder trabalho.
(Nota: numa interação inicial houve confusão com um servidor de autosave de **outro** projeto;
confirmado no código que esta app não tem servidor nem autosave.)

## D6 — Versionar por commits git, não por ficheiros `vN`
**Decisão:** editar sempre `lifemap_lab.html`; versões antigas arquivadas em `.Old/`.
**Porquê:** o esquema antigo (`lifemap_lab_vN.html` + scripts `_patch_vN.js`) era pesado e
poluía a pasta. Git dá histórico limpo. Os patch-scripts eram temporários e foram removidos.

## D7 — GitHub Pages abandonado por privacidade
**Decisão:** removido o `index.html` espelho e o pre-commit hook que publicavam a app.
**Porquê:** publicar a app (que contém estruturas pessoais de vida/mail/conhecimento) num site
público é um risco de privacidade. Por isso a ideia de GitHub Pages foi abandonada.
**Não reintroduzir** sem pedido explícito.

## D8 — Validação do JS embebido via `node -e`
**Decisão:** após mexer no `<script>`, validar com
`new Function(html.match(/<script>([\s\S]*)<\/script>/)[1])`.
**Porquê:** apanhar erros de sintaxe sem abrir o browser, dado que tudo é um único ficheiro.

## D10 — CHANGELOG.md por versão (não diário de código)
**Decisão:** manter um `CHANGELOG.md` estilo *Keep a Changelog*, uma linha por mudança
visível da app por versão; **não** um registo linha-a-linha do código.
**Porquê:** dá histórico de produto legível para humanos sem duplicar o git (que já guarda os
diffs exatos) nem o changelog interno da app (que regista mudanças de dados, não de código).
Um diário por-edição ficaria desatualizado e seria redundante.

## D11 — settings.json só com git read-only
**Decisão:** `.claude/settings.json` versionado com `allow` apenas para `git status/diff/log/show`.
**Porquê:** reduz prompts para comandos inofensivos sem conceder execução. `Bash(node -e:*)`
foi deliberadamente **deixado de fora** por ser execução arbitrária de código (o utilizador
aprova a validação JS caso a caso). A proibição de ler `SessionTranscripts/` ficou como
instrução condicional no `CLAUDE.md` (não como `deny` rígido, que bloquearia mesmo a pedido).

## D9 — Pasta de transcripts privada e fora do git
**Decisão:** `SessionTranscripts/` em `.gitignore`; o Claude está proibido de a ler salvo
indicação explícita; transcripts gravados como ZIP `SX - Título`.
**Porquê:** transcripts contêm conteúdo pessoal/sensível; não devem ir para o repo nem ser
lidos por defeito.

## D12 — Numeração de sessões: track único `S #` (S1, 2026-06-02)
**Decisão:** abandonado o esquema duplo (`SG #` setup + `S #` trabalho). Doravante todas
as sessões são `S #` num único contador, com título descritivo (ex.: `S1 - Setup e gestão`,
`S2 - <…>`). Ficheiros anteriores em `SessionTranscripts/` (`SG 1 - Setup Claude Code.zip`,
`S1-Transcript.jsonl`) ficam como **pré-numeração-unificada**; não renomear.
**Porquê:** distinção SG/S não acrescentava valor prático e gerava ambiguidade na hora de
nomear sessões mistas (esta tinha tanto de setup como de entrega da prompt). Track único é
mais simples e o título já chega para classificar.

## D13 — Prompt MD arquivada em `docs/` (S1, 2026-06-02)
**Decisão:** a prompt robusta para LLMs gerarem MD no formato da app passou a viver em
`docs/prompt-md-generator.md` (em vez de só existir em contexto de chat ad-hoc).
**Porquê:** é um artefacto **reutilizável** e referenciável; arquivar num ficheiro estável:
(a) garante continuidade entre sessões mesmo que o contexto se perca; (b) deixa a prompt
sob controlo de versão (diffs visíveis); (c) liberta o roadmap/handoff de "pendente herdado".

---
# Decisões da S2 (2026-06-08, branch `App-Generica` — MapLab)

## D14 — App genérica: estado dinâmico em vez de mapas hardcoded
**Decisão:** remover os 4 mapas fixos (lifemap/icloud/notion/obsidian) e o modelo de literais de
chave-fixa; introduzir `workspace{projects→trees}` com `initTree(treeId)` a popular stores dinâmicos.
**Porquê:** o objetivo do utilizador é criar projetos/árvores em runtime (a app é o editor, não o
código). O estado já era indexado por `tabId`, por isso o salto foi viável sem reescrever a edição.
**Consequência:** removeu-se o conceito de "pasta de sistema" (iCloud) e os ícones automáticos por-mapa.

## D15 — Ícones Notion num "pacote estanque" embebido
**Decisão:** os 883 SVG vivem num bloco isolado `<script id="iconPack">` (marcadores ICON PACK
START/END), acedido só por `iconSvg`/`iconNames`/`iconExists`; ícone por nó em `node.icon`, recolorido
por `branchColor`.
**Porquê:** app single-file tem de ser autónoma (sem fetch a pasta externa, que `file://` bloqueia).
Isolar o pacote permite a um agente futuro trocá-lo sem tocar no resto. SVG recolorido via `currentColor`
evita ter versões por cor.

## D16 — Sistema de governação de alterações (Arqueologia + planos + instrução + logs + auditoria)
**Decisão:** ficheiro vivo único `MapLab.html`; snapshots **congelados read-only** por marco aceite em
`Arqueologia Alteracoes/` (00 = Versão Original); 2 planos (app/server) com ordem **global partilhada**;
`instrucao-agente-alteracoes.md` (onboarding + §0bis retoma); `log-alteracoes.md` e `registo-auditoria.md`
**append-only**; `questionario-validacao.md`; retoma registada em `agente-audit-iniciar.md`.
**Porquê:** o projeto cresceu para multi-fase e multi-sessão; era preciso um agente novo (sem contexto)
retomar sem repetir a compreensão. Padrão alinhado com AGENTS.md + ADR append-only (pesquisa web).
**Validado** por subagentes: onboarding ✓, implementabilidade do roadmap ✓, retoma por "inicia" ✓.
**Compromisso sobre a Arqueologia:** congelados read-only por marco (não a cada alteração) para evitar
a "cópia que apodrece" — entre marcos confia-se no git; a Arqueologia serve só para abrir 2 versões lado
a lado no browser.

## D17 — Reconciliação `.md`↔`.json` sem ambiguidade + numeração
**Decisão:** persistência grava `.md` limpo (estrutura) + `.json` completo (ícones/classes/numeração).
Religação por `nome+nivel+pai`. **Regra de integridade:** proibido irmãos homónimos sob o mesmo pai/nível.
**Nova funcionalidade (Grupo H):** toggle ativar/desativar numeração; `.json` grava sempre field `numeracao`.
**Porquê:** o `.md` editável por fora pode reordenar nós; ligar por posição partiria. A regra de integridade
+ numeração tornam a identidade do nó inequívoca, eliminando o caso de colisão (em vez de o "gerir").

## D18 — Persistência: servidor local opcional, índice híbrido portável, mirror por versão
**Decisão:** Fase 2 com servidor Python opcional (espelha `TableEditorApp/acc_server.py`) + **fallback
para memória** com alerta quando offline. **Portabilidade:** `MapLab.json` na raiz; caminhos das árvores
**relativos** (`Projetos/`); `.py` **sem paths** (lê do índice); `lastKnownPath` p/ servidor detetar
movimento e re-base. **Mirror por versão:** dupla gravação (Projetos/ + pasta externa absoluta), ficheiros
`MapaXxx-Vx.md`, com "Atualizar do mirror" e "Nova versão de mirror".
**Porquê:** resolve a contradição "portável vs paths absolutas" — relativo por defeito (move-se a pasta e
funciona), absoluto só onde faz sentido (mirror externo, que deve ficar estável). O `.py` sem paths fica
genérico. Mirror por-versão evita conflitos de escrita no mesmo ficheiro. **Revê D5:** a app genérica
**vai ter** persistência via servidor (mas mantém o modo memória como fallback — D5 continua válido
para o caso sem servidor).

---
# Decisões da S3 (2026-06-08, branch `App-Generica`)

## D19 — Front-end primeiro: dissolver a regra "persistência antes das Classes"
**Decisão:** reordenar o roadmap para fazer **toda a Fase 1 (front-end: D Classes & Grupos, H Numeração,
E atribuição em massa, F versões de classe, G side-by-side) em memória, ANTES** da Fase 2 (servidor/
persistência). A antiga ordem punha "Persistência base (4) antes das Classes (5)". Nova ordem global:
4=D+H · 5=E · 6=F · 7=G · 8=S1+S2+S3+S7 · 9=S4+S8 · 10=S5+I · 11=S6. Âmbito da fase imediata: **D+E+H**.
**Porquê:** o objetivo do utilizador agora é **ver a app a funcionar** com as features novas, não gravá-las.
A dependência "persistência antes das classes" só existia para haver onde gravar — mas a app já funciona
em memória (e já se perde ao recarregar, como sempre), por isso ver classes/versões a funcionar **não exige
servidor**. Fazer o front-end primeiro tem ainda a vantagem de **estabilizar o modelo de dados** antes de o
serializar. **Sem retrabalho:** o esquema `.json` continua definido (S3) — quando a persistência chegar,
só serializa um modelo já maduro. **Revê parcialmente D18/D17:** a persistência mantém-se planeada e o
esquema intacto; só muda *quando* se implementa (depois, não antes). As versões de classe (F) usam `s.saves`
em memória nesta fase; a gravação em ficheiros é S4 (ordem 9).

## D20 — Classes do nó resolvidas por id em ambas as libs (imune ao scope)
**Decisão:** no render (`resolveNodeVisual`), a classe de um nó é encontrada procurando o seu id em
**`systemLib` E `localLib`** (ids únicos), em vez de usar `node.classeTipo` para escolher uma só lib.
O campo `classeTipo` mantém-se (para serialização futura) mas **deixa de condicionar a visualização**.
**Porquê:** `classeTipo` é **um campo único por nó**, mas a primária pode vir de Sistema e a secundária de
Local — com um só `classeTipo`, uma delas era procurada na lib errada, não encontrada, e o ícone/cor
**desaparecia** (agravado ao mudar o toggle Locais/Sistema). Sistema vs Local é só sobre **disponibilidade
para atribuir**, nunca sobre visualização. Resolver por id torna o render imune ao scope e fecha a dívida
do `classeTipo` único registada em #012.

## D21 — Side-by-side: host de render decidido por contexto, não propagado por função
**Decisão:** o painel partilhado do side reutiliza `renderPanel`/`renderClassPanel`; em vez de passar um
`hostId` a cada uma das ~13 funções de zona, estas duas funções **decidem o host centralmente**: se
`sideViewActive()`, forçam `side-rpanel`/`side-rclasses`. As funções de zona continuam a chamar
`renderClassPanel(tabId)` sem saber o contexto.
**Porquê:** quando o side está ativo, os painéis da vista normal ficam só **escondidos** no DOM (não
removidos), por isso `renderClassPanel(tabId)` sem host escrevia no painel invisível e o do side nunca
atualizava — algumas funções "funcionavam por acidente" porque também chamavam `renderActiveView`→`refreshSide`.
Centralizar a decisão num único ponto (2 funções) corrige todos os casos de uma vez, sem tocar nos call-sites
e sem depender de efeitos colaterais. **Princípio mais geral:** "contexto de render ativo" > propagar host
em cada chamada.

## D22 — Infra de DUAS VERSÕES (virgem + teste gerada)
**Decisão:** a cada alteração da app existem duas versões: `MapLab.html` (**virgem**, a app real, sem qualquer
vestígio de teste) e `MapLab-teste.html` (**gerada** por `node build-teste.js` = virgem + bloco de teste inline).
O bloco-fonte vive em `MapsTeste/seed-bloco.template.html`; o botão "Carregar projetos" cria projetos/árvores
de `MapsTeste/*.md` + grupos/classes de exemplo. A teste é **gitignored**; regenera-se a cada edição.
**Porquê:** o utilizador precisa de carregar um cenário de teste repetível sem o criar à mão a cada vez, mas a
app real (virgem) tem de ficar limpa e portável (sem botão/dados de teste). Inline (não `<script src>`) garante
que a teste é auto-contida e abre por duplo-clique em `file://`. O protocolo "regenerar a teste após editar a
virgem" está na checklist da §4 de `instrucao-agente-alteracoes.md`.
