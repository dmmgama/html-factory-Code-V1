# CLAUDE.md — LifeMap Laboratory

Instruções para o Claude Code neste projeto. Lê isto por completo antes de agir.
Idioma de trabalho: **PT-PT**.

---

## Arranque de cada sessão (obrigatório, por esta ordem)
1. Ler **`handoff.md`** (estado imediato da sessão anterior).
2. Ler **`context.md`** (SSOT acumulado) e **`roadmap.md`** (rumo do projeto).
3. **Verificar alinhamento:** confirmar se `handoff.md` e `context.md` estão coerentes com
   `roadmap.md`. **Se houver discrepâncias, assinalá-las ao utilizador** antes de continuar.
4. **NÃO ler `SessionTranscripts/`** — está proibido salvo indicação explícita do utilizador
   (ver "Privacidade" abaixo).
5. **Perguntar ao utilizador:** *"Queres **continuar tarefas** (seguir o roadmap/handoff) ou
   fazer **adições ao roadmap** (novos requisitos/correções)?"*
   - Se **continuar tarefas** → prosseguir normalmente (próximo item do handoff/roadmap).
   - Se **adições ao roadmap** → ler primeiro **`bugs.md`** (falhas por corrigir) e
     **`additions.md`** (updates pretendidos), apresentar o que está registado, e só então
     discutir e incorporar as novas adições nos planos (`Planodeacao-app.md` /
     `Planodeacao-server.md` / `roadmap.md`).

> A pergunta-gatilho do roadmap da app foi respondida na S1: **adiada** (manter só roadmap
> de processo). **Não voltar a perguntar** em cada arranque; ver `roadmap.md` → "Estado do
> gatilho inicial". Só reabrir se o utilizador trouxer features ao tema.

---

## O que é o projeto
**Life Map Laboratory** — editor single-file de taxonomias hierárquicas (vida, mail iCloud,
Notion, Obsidian), com vistas em árvore e mind map, import/export Markdown e versões.
Tudo numa única página: `lifemap_lab.html`. **Manual completo: [`docs/MANUAL.md`](MANUAL.md).**

- **Stack:** HTML + CSS + JavaScript vanilla (ES6). **Sem build, sem dependências, sem framework.** SVG para o mind map.
- **Ambiente:** Windows + PowerShell.
- **Persistência:** em transformação. **Em `main` (app v12):** NENHUMA (só memória; persistir =
  exportar `.md`). **Na branch `App-Generica` (MapLab):** a caminho de persistência real via
  **servidor local opcional** (Fase 2), com fallback para memória quando o servidor está offline.
- **Git:** repo `LifeMapEditor` (remote GitHub). Versões antigas em `.Old/` (v2, v4–v11).

## Estado atual (resumo — detalhe em `context.md`/`handoff.md`/`roadmap.md`)
- **`main`:** app **v12** (`lifemap_lab.html`, 4 mapas hardcoded + side-by-side). GitHub Pages
  abandonado por privacidade.
- **Branch `App-Generica` (trabalho ativo):** a app tornou-se **MapLab** — editor **genérico**
  (projetos + árvores criados em runtime, sem mapas hardcoded), **+ ícones Notion**, a caminho de
  **classes/grupos** e **persistência por servidor**. Ficheiro vivo = **`MapLab.html`**.
  **Versão Original v12 congelada** em `Arqueologia Alteracoes/00-…`.

> **Se estiveres na branch `App-Generica`:** o processo de alterações é GOVERNADO. Lê PRIMEIRO
> **`instrucao-agente-alteracoes.md`** (onboarding completo). As regras abaixo marcadas «(v12/main)»
> só valem na `main`.

## Convenções
- **Editar sempre o ficheiro vivo:** «(v12/main)» `lifemap_lab.html` · «(App-Generica)» `MapLab.html`.
  Não criar `_vN.html`; snapshots aceites vão para `Arqueologia Alteracoes/` (read-only); versionar por commits.
- Formato MD canónico: `# Versao <V>` + `# Estrutura` + lista de bullets (2 espaços/nível),
  **sem numeração**. (Detalhe no manual, §5.)
- «(v12/main)» Render parametrizado por `tabId`: adicionar um mapa = registar o `tabId` nos ~11
  literais de estado + `getRawData` + CSS + HTML. (Receita no manual, §6.)
  «(App-Generica)» Já não há mapas hardcoded; árvores criadas em runtime (ver `instrucao-agente-alteracoes.md`).
- Validar o JS embebido após mexer no `<script>` (ajustar o nome do ficheiro à branch):
  `node -e "new Function(require('fs').readFileSync('MapLab.html','utf8').match(/<script>([\s\S]*)<\/script>/)[1]);console.log('JS OK')"`
- «(App-Generica)» **Duas versões:** `MapLab.html` é a **virgem** (nunca lhe metas o bloco de teste);
  `MapLab-teste.html` é **gerada** (virgem + botão "Carregar projetos"). Após editar a virgem, regenera com
  `node build-teste.js`. Ver `instrucao-agente-alteracoes.md` §1/§4.
- Nomes/labels da UI em PT-PT.

## NÃO fazer
- Não editar `icloud_mail_editor.html` ao mexer na app (é um artefacto separado).
- Não reintroduzir `index.html`/GitHub Pages sem o utilizador pedir (foi abandonado por privacidade).
- Não usar numeração nem headings/código extra no MD.
- Não alterar a ordem de nós de nível ≥3 sem confirmar.
- «(v12/main)» Não inventar persistência/servidor: a app v12 não tem. «(App-Generica)» a persistência
  por servidor é planeada — segue `Planodeacao-server.md`, não improvises fora do plano.
- Não tocar em `Arqueologia Alteracoes/` (snapshots congelados / Versão Original).
- Não "melhorar" código adjacente ao que foi pedido (ver guidelines abaixo).

---

## Guidelines de comportamento (reduzir erros comuns de LLM)
> Tradeoff: estas regras privilegiam cautela sobre velocidade. Para tarefas triviais, usar bom senso.

**1. Pensar antes de codificar.** Não assumir. Não esconder confusão. Expor tradeoffs.
Antes de implementar: declarar as suposições; se houver várias interpretações, apresentá-las
(não escolher em silêncio); se existir abordagem mais simples, dizê-lo; se algo for ambíguo,
parar e perguntar.

**2. Simplicidade primeiro.** Código mínimo que resolve o problema. Nada especulativo:
sem features além do pedido, sem abstrações para uso único, sem "flexibilidade" não pedida,
sem tratar cenários impossíveis. Se escreveste 200 linhas e davam 50, reescreve.

**3. Mudanças cirúrgicas.** Tocar só no necessário. Ao editar código existente: não "melhorar"
código/comentários/formatação à volta, não refatorar o que não está partido, seguir o estilo
existente. Remover só os órfãos que as **tuas** mudanças criaram; código morto pré-existente
**menciona-se, não se apaga** sem pedido. Teste: cada linha alterada deve rastrear ao pedido.

**4. Execução orientada a objetivos.** Definir critérios de sucesso e iterar até verificar.
"Corrigir o bug" → "escrever um teste que o reproduz, depois fazê-lo passar". Para tarefas
multi-passo, enunciar um plano curto com verificação por passo.

---

## Continuidade entre sessões

### Fecho de cada sessão (protocolo)
1. **Atualizar `context.md`** — incorporar o estado acumulado (arquitetura, decisões,
   convenções, dependências, estado atual). É o SSOT que cresce ao longo do tempo.
2. **Atualizar `memory.md`** — registar o *porquê* de novas decisões arquiteturais/design.
3. **Atualizar `roadmap.md`** — refletir progresso e próximos marcos.
4. **Atualizar `CHANGELOG.md`** — **se mexeste no código da app**, acrescentar uma linha por
   mudança visível (feature/fix/remoção/bump de versão) na secção `[Não lançado]` ou na versão.
   É registo de produto, não diário de código (os diffs estão no git).
5. **Reescrever `handoff.md`** — estado imediato para a próxima sessão (feito / decisões /
   próximos passos / ficheiros tocados / tensões em aberto). **Formato telegráfico, denso, sem narrativa.**
6. **Numerar a sessão:** perguntar ao utilizador *"Que nome dar à sessão?"* e **sugerir** um
   nome baseado no trabalho feito, no formato **`SX - Título`** (X = número da sessão anterior + 1).
   Registar no `handoff.md` que a sessão anterior foi `S(X-1)` e que esta é `SX`.
   > **Track único `S #`** (decisão D12 em `memory.md`). O esquema antigo `SG #` foi abandonado.
7. **Transcript:** perguntar ao utilizador se quer **gravar o transcript** da sessão. Se sim,
   gravar para `SessionTranscripts/` um **ZIP** com o nome **`SX - Título.zip`**.

### Privacidade — pasta de sessões
- **`SessionTranscripts/` é privada e está fora do git** (em `.gitignore`).
- **Proibido ler `SessionTranscripts/`** salvo quando o utilizador o pedir explicitamente.

### Ficheiros de continuidade
| Ficheiro | Papel |
|---|---|
| `handoff.md` | Estado imediato p/ próxima sessão (telegráfico). Reescrito a cada fecho. |
| `context.md` | SSOT acumulado do projeto. Cresce no tempo. |
| `memory.md` | "Porquê" das decisões (não é estado corrente). |
| `roadmap.md` | Rumo/marcos do projeto. |
| `bugs.md` | Registo de falhas conhecidas (append-only, por área funcional). |
| `additions.md` | Adições/updates ao roadmap pretendidos pelo utilizador (append-only). |
| `CHANGELOG.md` | Alterações visíveis da app, por versão (registo de produto). |
| `docs/MANUAL.md` | Manual técnico para humanos. |
| `docs/prompt-md-generator.md` | Prompt para LLMs gerarem MD no formato da app. |
