---
title: Setup de Claude Code em Projetos
type: protocolo
status: em-construção
tags: [claude-code, setup, protocolo, governanca-ai, continuidade]
created: 2026-06-02
updated: 2026-06-02
---

# 🛠️ Setup de Claude Code em Projetos

> [!abstract] O que é este documento
> O meu **protocolo pessoal** para fazer setup de Claude Code num projeto — quer comece do
> zero, quer já exista código. Estou a migrar dos *Claude Projects* para aqui, por isso este
> ficheiro vai **crescendo** à medida que consolido o que funciona.
>
> É ao mesmo tempo:
> - **Pedagógico** — explica o *porquê* de cada peça.
> - **Funcional** — é um *framework* de passos que eu sigo.
> - **Operacional** — tem **caixas para copiar** e colar ao agente.

> [!tip] Como ler este documento
> - **Texto normal** = explicação (para eu perceber).
> - **Callouts** (`[!info]`, `[!warning]`, `[!example]`) = notas e avisos.
> - **Blocos de código com `📋 COLAR AO AGENTE`** = copio tal e qual para o chat do Claude Code.

---

## 🧠 Conceitos base — a camada de continuidade

O Claude Code **não tem memória entre sessões** por defeito. Para resolver isso, cada projeto
ganha uma **camada de ficheiros de continuidade** que o agente lê no arranque e escreve no fecho.

| Ficheiro | Papel | Quando muda |
|---|---|---|
| `CLAUDE.md` | Regras do projeto + protocolos (arranque/fecho) + guidelines. Lido **sempre** no início. | Raramente. |
| `context.md` | **SSOT** acumulado (arquitetura, decisões, convenções, estado). Cresce no tempo. | Em cada fecho. |
| `handoff.md` | Estado **imediato** para a próxima sessão (telegráfico). | Reescrito a cada fecho. |
| `memory.md` | O **porquê** das decisões (D1, D2, …). Não é estado corrente. | Quando há decisão nova. |
| `roadmap.md` | Rumo / marcos do projeto. | Quando o rumo evolui. |
| `.claude/settings.json` | Permissões partilhadas (versionado). | Por minha decisão. |
| `.claude/settings.local.json` | Permissões locais da máquina (**fora do git**). | Automático. |
| `logs/`, `SessionTranscripts/` | Ruído local e transcripts (**fora do git, privados**). | Automático. |
| `CHANGELOG.md` | Alterações **visíveis do produto**, por versão (não diário de código). | Quando se mexe na app. |
| `docs/MANUAL.md` | Manual técnico para humanos. | Quando o projeto muda. |

> _Os ficheiros acima da linha são governança de sessão. `CHANGELOG.md` e `docs/MANUAL.md`
> são artefactos de produto — seguem ciclo diferente._

> [!info] O ciclo de continuidade
> ```
> ARRANQUE → ler handoff.md → ler context.md + roadmap.md →
>            verificar alinhamento (assinalar discrepâncias) → NÃO ler SessionTranscripts/
>      ↓
>   [ trabalho ]
>      ↓
> FECHO → atualizar context/memory/roadmap (+CHANGELOG se mexeu na app) →
>         reescrever handoff.md → numerar a sessão → (opcional) gravar transcript em ZIP
> ```

> [!warning] Regras de privacidade (não negociáveis)
> - `SessionTranscripts/` e `logs/` **fora do git** (`.gitignore`).
> - O agente está **proibido de ler `SessionTranscripts/`** salvo se eu indicar explicitamente.
> - Nada de publicação pública (ex.: GitHub Pages) sem eu pedir.

> [!note] Numeração de sessões
> - `S#` → sessões de **trabalho** no projeto (ex.: `S1 - …`).
> - `SG #` → sessões de **setup/gestão** da config (ex.: `SG 1 - Setup Claude Code`).
> - No fecho, o agente sugere o nome `SX - Título` (X = anterior + 1) e regista no `handoff.md`
>   que a anterior foi `S(X-1)` e esta é `SX`.

---

## 🌱 PARTE 1 — Setup num projeto **de raiz** (novo)

> [!example] Resultado final esperado
> ```
> projeto/
> ├── CLAUDE.md
> ├── context.md
> ├── handoff.md
> ├── memory.md
> ├── roadmap.md
> ├── CHANGELOG.md
> ├── .gitignore
> ├── .claude/
> │   ├── settings.json
> │   └── settings.local.json   (gitignored)
> ├── docs/
> │   └── MANUAL.md
> ├── logs/                     (gitignored)
> └── SessionTranscripts/       (gitignored)
> ```

### Passo 0 — Pré-requisitos (eu)
- [ ] Pasta do projeto criada e aberta no Claude Code.
- [ ] Decidir se quero **git** (recomendado) e se há **remote** (GitHub privado, por privacidade).

### Passo 1 — Briefing inicial ao agente
A regra de ouro: **mandar o agente fazer-me perguntas antes de escrever**. Não quero que assuma.

```text
📋 COLAR AO AGENTE — briefing inicial (projeto novo)
Este projeto não tem CLAUDE.md nem estrutura .claude/.
Quero montar a base de configuração e continuidade de Claude Code.

ANTES de escrever seja o que for:
- Analisa o que já existe na pasta.
- Faz-me TODAS as perguntas necessárias (objetivos do projeto, stack, convenções,
  o que NÃO fazer, se quero git/remote). Não assumas nada; o que for ambíguo marca [A CONFIRMAR].

DEPOIS cria:
1) CLAUDE.md  2) context.md  3) handoff.md  4) memory.md  5) roadmap.md
6) CHANGELOG.md  7) docs/MANUAL.md  8) .claude/settings.json  9) atualiza .gitignore
Mostra-me um plano antes de executar.
```

### Passo 2 — O que cada ficheiro deve conter (instrução ao agente)

```text
📋 COLAR AO AGENTE — conteúdo dos ficheiros
- CLAUDE.md: o que é o projeto, stack, estado atual, próximos passos, convenções,
  "NÃO fazer", + protocolo de continuidade (arranque/fecho) + guidelines de disciplina
  (pensar antes de codificar, simplicidade, mudanças cirúrgicas, execução orientada a objetivos)
  + proibição de ler SessionTranscripts/ salvo indicação explícita.
- context.md: SSOT acumulado (arquitetura, decisões, convenções, dependências, estado). Cresce.
- handoff.md: estado imediato p/ próxima sessão (telegráfico): feito / decisões / próximos
  passos / ficheiros tocados / tensões em aberto.
- memory.md: o "porquê" de cada decisão (D1, D2, …).
- roadmap.md: marcos do projeto; no arranque o agente confere se handoff/context estão
  alinhados com o roadmap e assinala discrepâncias.
- CHANGELOG.md: alterações visíveis do produto, por versão (não diário de código).
- docs/MANUAL.md: manual técnico para humanos (arquitetura, como correr, como estender).
```

### Passo 3 — Git

```text
📋 COLAR AO AGENTE — git
Inicializa git (se ainda não houver), faz um primeiro commit da config com a mensagem
"Setup-ClaudeCode", e (se eu autorizar) liga ao remote e faz push.
NÃO publiques nada publicamente (sem GitHub Pages). Confirma comigo antes de push.
```

> [!tip] `.gitignore` mínimo recomendado
> ```gitignore
> .claude/settings.local.json
> logs/
> SessionTranscripts/
> .DS_Store
> Thumbs.db
> ```

### Passo 4 — Protocolos de continuidade (o coração)
Estes textos devem ficar **dentro do `CLAUDE.md`**. Dou-os ao agente para os embeber.

```text
📋 COLAR AO AGENTE — protocolo de ARRANQUE (meter no CLAUDE.md)
No início de cada sessão, por esta ordem:
1. Ler handoff.md.
2. Ler context.md e roadmap.md.
3. Verificar se handoff/context estão coerentes com o roadmap; se houver discrepâncias,
   assinalar-mas ANTES de continuar — assinalar apenas discrepâncias que sejam relevantes
   para o objetivo da sessão atual.
4. NÃO ler SessionTranscripts/ (proibido salvo indicação explícita minha).
```

```text
📋 COLAR AO AGENTE — protocolo de FECHO (meter no CLAUDE.md)
No fim de cada sessão:
1. Atualizar context.md (estado acumulado).
2. Atualizar memory.md (porquê de novas decisões).
3. Atualizar roadmap.md (progresso/próximos marcos).
4. Atualizar CHANGELOG.md SE mexeste no código (uma linha por mudança visível).
5. Reescrever handoff.md (telegráfico: feito/decisões/próximos passos/ficheiros/tensões).
6. Perguntar-me "Que nome dar à sessão?" e sugerir "SX - Título" (X = anterior + 1);
   registar no handoff que a anterior foi S(X-1) e esta é SX.
7. Perguntar se quero gravar o transcript. Se sim, gravar para SessionTranscripts/
   um ZIP "SX - Título.zip".
```

> [!info] Logs e transcripts
> - `logs/` é ruído local (logs de MCP/sessão) — só serve para debug, vai para o `.gitignore`.
> - `SessionTranscripts/` guarda o histórico das sessões em ZIP (`SX - Título.zip`). É privado
>   e o agente não o lê sozinho. O transcript da sessão atual costuma estar em
>   `~/.claude/projects/<slug-do-projeto>/<id>.jsonl` (o agente localiza e comprime no fecho).

### Passo 5 — Permissões (`.claude/settings.json`)

> [!warning] Eu é que autorizo as permissões
> O agente **não pode** conceder-se permissões sozinho (é bloqueado). Eu escolho o nível.
> - **Seguro (recomendado):** só git read-only.
> - **Conveniente:** + `node -e` (mas é execução arbitrária — mais permissivo).

```json
{
  "permissions": {
    "allow": [
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git show:*)"
    ],
    "deny": []
  }
}
```

### Passo 6 — Fechar a sessão de setup
Correr o **protocolo de fecho** (Passo 4) — incluindo numerar a sessão (ex.: `SG 1 - Setup
Claude Code`) e, se eu quiser, gravar o transcript em ZIP.

---

## 🧩 PARTE 2 — Setup num projeto **já existente**

A diferença é que primeiro é preciso **o agente perceber o que já lá está** antes de escrever config.

### Passo 1 — Mapear o projeto
Usar o skill **`understand-anything`** (ou `mapear-projeto`) para gerar um mapa/knowledge-graph.

> `understand-anything` — TypeScript monorepo com análise tree-sitter e pipeline multi-agente.
> Escreve o mapa em `.understand-anything/` na raiz do projeto. Requer pnpm.

```text
📋 COLAR AO AGENTE — mapear
Usa o skill understand-anything para mapear este projeto (arquitetura, componentes,
relações). Quando terminar, dá-me um resumo do que encontraste.
```

### Passo 2 — Agente lê e compreende o mapa

```text
📋 COLAR AO AGENTE — compreender
Lê o mapa que geraste e explica-me, em linguagem simples: o que é o projeto, a stack,
a arquitetura, o estado atual e os pontos de risco/dúvida. Lista o que NÃO percebeste.
```

### Passo 3 — Perguntas de alinhamento (objetivos)

```text
📋 COLAR AO AGENTE — perguntas
Antes de criares config, faz-me perguntas sobre: objetivos do projeto, prioridades,
convenções a respeitar, o que NÃO mexer, e o que falta no mapa. Não assumas; marca [A CONFIRMAR].
```

### Passo 4 — Transcripts de sessões anteriores

```text
📋 COLAR AO AGENTE — transcripts
Faz sentido importar transcripts de sessões anteriores deste projeto?
Pergunta-me DE QUE sessões. Se eu indicar quais, coloca-os em SessionTranscripts/ e
LÊ-OS (autorizo explicitamente) para extraíres decisões, estado e histórico para o context.md.
Lembra-te: sem a minha indicação explícita, não podes ler essa pasta.
```

> [!note] Porque é que isto respeita a regra de privacidade
> A leitura de `SessionTranscripts/` é proibida **por defeito**. Aqui eu **autorizo
> explicitamente** e digo *quais* — só nesse caso o agente lê.

### Passo 5 — Criar a config e fechar
A partir daqui é igual à **Parte 1** (Passos 2–6): criar `CLAUDE.md` + restantes ficheiros
(já preenchidos com o que o mapa + transcripts revelaram), git, permissões, e fecho.

```text
📋 COLAR AO AGENTE — criar config (projeto existente)
Com base no mapa, nas minhas respostas e nos transcripts que leste, cria a base de config
Claude Code (CLAUDE.md, context.md, handoff.md, memory.md, roadmap.md, CHANGELOG.md,
docs/MANUAL.md, .claude/settings.json, .gitignore) preenchida com o estado REAL do projeto.
Nada inventado; [A CONFIRMAR] no que for ambíguo. Mostra plano antes de executar.
```

---

## ✅ Checklists rápidas

> [!todo] Projeto novo
> - [ ] Briefing inicial (agente faz-me perguntas)
> - [ ] CLAUDE.md + context + handoff + memory + roadmap + CHANGELOG + docs/MANUAL
> - [ ] .claude/settings.json (permissões que eu autorizei) + .gitignore
> - [ ] git init + commit "Setup-ClaudeCode" (+ push se autorizado)
> - [ ] protocolo de fecho (numerar sessão + transcript)

> [!todo] Projeto existente
> - [ ] Mapear (understand-anything)
> - [ ] Agente explica o mapa + lista dúvidas
> - [ ] Perguntas de objetivos/convenções
> - [ ] Decidir transcripts (quais) → agente lê
> - [ ] Criar config preenchida com estado real
> - [ ] git + permissões + fecho

---

## 📌 Notas e evolução
- Este protocolo foi consolidado a partir do setup do projeto **LifeMap** (sessão
  `SG 1 - Setup Claude Code`, 2026-06-02).
- [x] **Template de pasta pronto a copiar** criado em `Template-ProjetoClaudeCode/` — esqueleto de
  todos os ficheiros, com o `CLAUDE.md` já a trazer os protocolos de arranque/fecho, guidelines,
  privacidade e numeração de sessões embebidos. Ver `_LEIA-ME.md` da pasta. _(2026-06-02)_
- A fazer / a decidir:
  - [ ] Se a numeração `S#`/`SG #` se mantém ou se unifica.
  - [ ] Se o protocolo de fecho deve ser reforçado por *hook* (hoje é só instrução no CLAUDE.md).
