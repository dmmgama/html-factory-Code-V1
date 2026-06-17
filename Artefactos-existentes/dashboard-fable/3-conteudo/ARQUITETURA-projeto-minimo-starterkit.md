---
created: 2026-06-09 06:35
chat: Arquitetura projeto minimo e starter kit de protocolos
summary: >
  Define o output do projeto AI Protocols: a estrutura de um projeto mínimo, o seu ciclo de vida,
  e o conjunto de protocolos-template (instalação + SP template + runtime) que o montam de forma coerente.
---

# Arquitectura do Projeto Mínimo + Starter Kit

> **O que isto responde:** o que tem de *sair* do projeto AI Protocols para montar projetos novos sem os drifts/contradições do audit. Em concreto: a estrutura de um projeto mínimo, como funciona, e que protocolos-template são precisos para o criar.
> **Tese:** o projeto AI Protocols não corre — produz um **starter kit** (Classe III). Montar um projeto = dar ao agente o starter kit + uma instrução, e ele constrói uma base coerente.

---

## §1. O output do projeto = o Starter Kit

Vive no **repositório transversal de governo** (Classe III, feito uma vez, reutilizável — *não* copiado para dentro de cada projeto):

```
_governo-transversal/                         (Classe III · transversal)
├── INSTALACAO-PROJETO.md          ◄ FALTA   (o orquestrador de montagem)
├── TEMPLATE-SYSTEM-PROMPT.md      ◄ FALTA   (o SP genérico a preencher)
├── PROTOCOLO-SESSOES.md           ✔ corrigir (relógio S{n}; install-time)
├── PROTOCOLO-LIGACAO.md           ✔ ok      (dois braços; install-time, com toggle)
├── PROTOCOLO-ficha-sessao.md      ✔ dedup   (runtime; arquivo humano + proveniência)
├── PROTOCOLO-PRODUCAO-DOCS.md     ✔ ok      (runtime; produção de docs)
├── FUNDACAO-FRONTMATTER.md
├── CATALOGO-TEMPLATES.md + templates/        (fundação de metadados)
└── PROTOCOLO-cristalizacao_*                 (camada de conhecimento — casa aqui, F0 do roadmap)
```

**Estado:** dos protocolos que precisas, **só faltam dois** — e são os que apontaste: a **instrução de montagem** e o **template de SP**. Tudo o resto existe; precisa só dos fixes de coerência do audit.

---

## §2. O que é um projeto mínimo (a estrutura que a montagem cria)

```
<Projeto>/
├── SYSTEM-PROMPT.md      (Classe III · canon do projeto; GERADO do TEMPLATE-SP)
├── INDEX.md             (Tier 2 · navegação; gerado)
├── handoff.md           (Classe II · estado vivo; continuidade, reescrito)
├── context.md           (Classe II · raciocínio acumulado; append)
├── 0.Registos/
│   └── Sessions/        (fichas humanas por sessão · proveniência S{n})
└── Coordenação/         (SÓ se dois braços) worklog · hot · ops-snapshot · code · log-sessoes
   (wiki/ Classe II — criada DEPOIS de saber o objetivo; não nasce no arranque)
```

**Dois braços é o default-com-toggle, não exceção.** Projetos como o Mapa AI (varrer folders/tools = braço operacional) e o Life Management (agente de mail) precisam dele. A montagem **pergunta** "um braço ou dois?"; se dois, cria `Coordenação/` e corre a entrevista do LIGACAO. Se um, omite ambos.

### Ciclo de vida (como funciona)
- **Arranque:** lê SP (canon) → ficha-sessao (cria ficha + proveniência) → handoff → context → [se dois braços: runbook "iniciar" do LIGACAO] → pronto. Relógio `S{n}` proposto no arranque (SESSOES §2).
- **Runtime:** produz docs sob PRODUCAO-DOCS + FUNDACAO; cristaliza ao bater RC1; [se dois braços: emite instruções `S{n}-{i}` ao operacional].
- **Fecho:** reescreve handoff → atualiza context (append) → finaliza ficha → read-after-write. **Sem LOG-PROJECTO** (git/Cristalização cobrem auditoria).

---

## §3. Os protocolos-template, por papel

| Protocolo | Papel | Quando | Vive | Estado |
|---|---|---|---|---|
| **INSTALACAO-PROJETO** | orquestra a montagem | uma vez, ao montar | transversal | **FALTA** |
| **TEMPLATE-SYSTEM-PROMPT** | molde do canon do projeto | gerado na montagem | → vira o SP do projeto | **FALTA** |
| **SESSOES** | relógio único `S{n}` + log | install-time (entrevista) | transversal (não copia) | corrigir incoerência ciclo |
| **LIGACAO** | dois braços (Blackboard) | install-time, se dois braços | transversal (emite blocos) | ok |
| **ficha-sessao** | ficha humana + proveniência | runtime, cada sessão | referenciado pelo SP | dedup (2 cópias divergiram) |
| **PRODUCAO-DOCS** | regras de produção de docs | runtime | referenciado pelo SP | ok |
| **Continuidade** (handoff/context) | estado vivo + raciocínio | runtime | **secção do TEMPLATE-SP** | extrair p/ standalone só com ≥2 projetos |
| **FUNDACAO + templates** | esquema de front matter | runtime | transversal | uma fundação (EN) |

> **Nota sobre a continuidade:** hoje está embutida no SP "a título provisório". Para o mínimo, fica como **secção fixa do TEMPLATE-SP** (herda `S{n}`). Só se extrai para protocolo próprio quando ≥2 projetos a usarem — anti-tropismo.

---

## §4. INSTALACAO-PROJETO — o orquestrador que falta

A peça que substitui o "agente: adapta daqui". É a instrução que se dá a um agente para montar o projeto. Fluxo:

```
1. Entrevista de montagem (uma pergunta de cada vez):
   · Nome + objetivo do projeto?
   · Um braço ou dois?            → liga/desliga LIGACAO + Coordenação/
   · Classe dominante do output?  → I / II / III
   · Tipos de sessão a semear?    → alimenta a entrevista do SESSOES
2. Corre a entrevista do SESSOES → fixa o relógio S{n} + tipos de sessão.
3. SE dois braços → corre a entrevista do LIGACAO → emite bloco-SP + bloco-CLAUDE.md(operacional).
4. Gera SYSTEM-PROMPT.md a partir do TEMPLATE-SP, preenchido com:
     respostas da entrevista + blocos emitidos (3) + secção de continuidade.
5. Cria a estrutura de pastas (§2) — só Coordenação/ se dois braços.
6. Cria handoff.md / context.md vazios + INDEX.md.
7. Read-after-write: confirma que tudo foi escrito. Confirma montagem.
```

Saída: um projeto pronto a arrancar, sem o agente ter de "adaptar daqui".

---

## §5. TEMPLATE-SYSTEM-PROMPT — o molde que falta

O SP genérico que a montagem preenche. Secções (parametrizadas por `<...>`):

- **§0 Identidade** — `<nome>`, `<objetivo>`, `<classe dominante>`, `<um/dois braços>`.
- **§1 Género** — canon declarativo; sem front matter; anti-changelog (da AI Protocols, já maduro).
- **§2 Vocabulário** — termos do projeto + os herdados (classe I/II/III, recipient, nó/cristalização).
- **§3 Tiers** — Tier 1 (arranque) / Tier 2 (on-demand). Lista de Tier 1 = `<ficheiros>`.
- **§4 Restrições hard + §5 Princípios contínuos** — herdados (não-inferir-em-silêncio, grau de certeza, honestidade, não-duplicação…).
- **§6 Arranque** — sequência §2-do-ciclo; relógio `S{n}`; [bloco LIGACAO "iniciar" se dois braços].
- **§7 Continuidade** — schema de handoff + context (herda `S{n}`). ◄ a secção que substitui o "embutido provisório".
- **§8 Fecho** — handoff → context → ficha → read-after-write. **Sem LOG-PROJECTO.**
- **§9 Ferramentas** — web/filesystem/MCP; criar ficheiros conforme PRODUCAO-DOCS.
- **§10 [se dois braços] Bloco do Estratégico** — emitido pelo LIGACAO §4.A.

O protótipo é o SP actual da AI Protocols — **abstraído e com os fixes do audit aplicados**, senão propaga os drifts.

---

## §6. Contrato de coerência — os invariantes que matam os drifts

Isto é o objetivo do projeto: que um projeto novo **não arranque com as contradições que apontei**. Cada invariante mata um achado concreto:

| Invariante (no starter kit) | Mata o drift |
|---|---|
| **Um relógio `S{n}`** — SP, ficha e pastas usam o mesmo (do SESSOES) | numeração tri-esquema (ME-1) |
| **Uma fundação de front matter (EN)** + tipo-nó da Cristalização | fork EN/PT + campos não-declarados |
| **Uma continuidade** (handoff+context, herda `S{n}`); **sem LOG-PROJECTO** | registo quádruplo + deadlock do fecho (C1) |
| **Cada ficheiro tem um caminho canónico** (INDEX gerado, não duplicado) | duplicação ficha-sessao já divergida (ME-3) |
| **Arranque/fecho só tocam ficheiros que a montagem criou** | apontar para ficheiro inexistente |
| **SESSOES é install-time e vive no transversal** (não corre dentro do projeto) | incoerência "permanente vs desaparece" (C3) |
| **Nomes sem colisão** (`context.md` ≠ qualquer `CONTEXT.md`) | colisão Windows (G2) |
| **Classe (I/II/III) em todo o doc** | "o que vive onde" |

> Regra-mãe transversal: **uma matéria, um sítio.** É o que o LIGACAO (barramento único), o SESSOES (relógio único) e a FUNDACAO (fundação única) já dizem, cada um no seu eixo. O starter kit só tem de os manter alinhados.

---

## §7. O que produzir, e por que ordem

1. **Aplicar os fixes de coerência** aos protocolos existentes (dedup ficha-sessao; relógio único; resolver ciclo do SESSOES; renomear colisão). Sem isto, os templates herdam os drifts.
2. **TEMPLATE-SYSTEM-PROMPT.md** — abstrair do SP actual + fixes + secção de continuidade.
3. **INSTALACAO-PROJETO.md** — o orquestrador (§4), que invoca SESSOES/LIGACAO e gera o SP.
4. **Teste real:** montar o **Mapa AI** com o starter kit (dois braços — precisa do varrimento). É o banco de ensaio do roadmap; cada fricção → Aprendizagem.

Depois disto, montar um projeto = "Agente, usa o `INSTALACAO-PROJETO` e o starter kit." Acabou o "adapta daqui".

---

> **Coerência primeiro, conteúdo depois.** Este esquema é a conceção; os dois ficheiros que faltam são o trabalho. Não cresças o starter kit além disto até o Mapa AI o testar.
