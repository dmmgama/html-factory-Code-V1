# handoff.md — estado imediato

_Estado para a próxima sessão. Telegráfico. Reescrito a cada fecho._

## Sessões
- **Esta sessão: `S3 - Grupos, side-by-side e seed`** (track único `S #`; anterior = `S2 - App genérica, ícones e governação`).
- Transcript: **o utilizador quis gravar ZIP** em `SessionTranscripts/S3 - Grupos, side-by-side e seed.zip` (exportação manual; o agente não acede à pasta privada).

## Branch / contexto (LER PRIMEIRO)
- **Branch ativa: `App-Generica`** (NÃO `main`). Sincronizada com `origin` (HEAD = `acfe5f6`). `MapLab.html` blob = `012e5ab`.
- Processo GOVERNADO: ler **`instrucao-agente-alteracoes.md`** (§0bis: ao dizer "inicia", retoma na ordem handoff → registo-auditoria → roadmap → planos → log → §1-4, regista em `agente-audit-iniciar.md`).
- **DUAS VERSÕES:** `MapLab.html` é a virgem (NUNCA lhe metas o bloco de teste); `MapLab-teste.html` é gerada (`node build-teste.js`). Após editar a virgem, REGENERA a teste. (§4 da instrução.)

## Feito (S3)
- **Reordenação FRONT-END PRIMEIRO** (D19): Fase 1 toda antes da Fase 2; nova ordem global 4..11. Planos/roadmap atualizados.
- **Grupo D — Classes & Grupos: FEITO em memória** (⏳ pendente de aceitação). Tab Classes em 3 zonas estanques
  (Visualização/Gestor/Atribuir); systemLib+localLib (Sistema/Local); "Sem Grupo" real; multi-classe prim+sec;
  render do nó com ícone(s)+cor (R1/R2/R4); classe resolvida em ambas as libs por id (D20, imune ao scope).
- **Grupo E parcial:** zona Atribuir (Ativar edição, toggle prim/sec, toggle "A filhos"); clique atribui. Falta modo custom/Aplicar em massa.
- **Grupo G parcial (side-by-side com edição):** painel partilhado, árvore ativa por clique no título, só coluna ativa clicável,
  colunas redimensionáveis + "Largura igual", mostra classes. Host de render centralizado por `sideViewActive()` (D21). Paridade com vista normal validada.
- **Infra de teste (D22):** "Carregar projetos" cria projetos+árvores de `MapsTeste/*.md` + grupos/classes de exemplo (Sistema + Local). Só na versão teste.
- Logs #008–#018 em `log-alteracoes.md`. Commits: `52ce0ae`,`4259045`,`f31bd44`,`9ae101d`,`a978f19`,`cecbc0e`,`5240981`,`68e2b31`,`3a0492f`,`acfe5f6`. Tudo pushed.

## Onde ficou
- Ficheiro vivo = **`MapLab.html`** (JS OK; blob `012e5ab`). **Ainda em memória** (sem persistência).
- Working tree: com este fecho ficam modificados `roadmap.md`, `context.md`, `memory.md`, `handoff.md` (+ CHANGELOG já commitado) — **a commitar no fecho**.
- `MapLab-teste.html` é gerada e gitignored — não versionar.

## Próximos passos (escolha do utilizador)
- **RECOMENDADO: `.json` por árvore (entrada na Fase 2 / Ordem 8).** Serializar o estado já estabilizado:
  classes/grupos (`localLib`+`systemLib`), atribuições por nó (`classePrimaria/secundaria/classeTipo/iconCustom`),
  `view`. Esquema completo em `Planodeacao-server.md` → S3. O modelo está maduro → serializar sem retrabalho.
- OU **completar Grupo E** (modo "custom"/checkboxes por nó + botão "Aplicar" em massa).
- OU **Grupo H** (numeração: toggle na vista, export `.md` com/sem, field `numeracao`).
- OU **Grupo G formal** (2 modos de side-by-side — depende de F versões de classe).
- Grupo I (filtros/ficheiros) continua **a debater** (ordem 10, com S5).

## Ficheiros relevantes
- App viva: `MapLab.html`. Versão teste: `MapLab-teste.html` (gerar com `node build-teste.js`). Bloco-fonte: `MapsTeste/seed-bloco.template.html`.
- Onboarding/retoma: `instrucao-agente-alteracoes.md`. Planos: `Planodeacao-app.md` (A-J), `Planodeacao-server.md` (S1-S8). Visão: `roadmap.md`.
- Logs: `log-alteracoes.md` (como), `registo-auditoria.md` (auditorias), `agente-audit-iniciar.md` (retomas). Append-only.
- Snapshots: `Arqueologia Alteracoes/` (read-only; 00 = Versão Original v12). Dados de teste: `MapsTeste/` (5 .md).
- Separado/independente: `icloud_mail_editor.html`.

## Tensões / questões em aberto
- **Limitação `classeTipo` único por nó** mitigada por D20 (render resolve por id em ambas as libs); o campo só serve serialização — rever se o `.json` precisar de origem por-classe.
- **Validação JS** assume 1 só `<script>` simples → na versão teste (2+ scripts) o comando da virgem dá erro; usar a virgem para validar. (AUD-001 lacuna 2, documentada.)
- App↔Server acoplados pelo `.json` (esquema já definido em S3) — não fechar um lado sem o outro.
- Marcos D/E/G ⏳ **pendentes de aceitação** — o utilizador ainda não confirmou formalmente (sem snapshot na Arqueologia até aceitar).
