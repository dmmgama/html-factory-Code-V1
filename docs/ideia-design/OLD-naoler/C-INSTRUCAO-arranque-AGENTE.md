---
created: 2026-06-17 19:10
project: html-artifact-factory
chat: Bootstrap do factory em Claude Code
session: SArq-3
status: vivo
summary: >
  Instrucao de arranque para o agente Claude Code: passo-zero git, reconhecimento
  opcional por subagentes, grill-with-docs para fechar tensoes, e construcao do
  factory por incrementos verticais funcionais.
---

# INSTRUCAO DE ARRANQUE — html-factory (para o agente Claude Code)

> Esta e a tua ordem de trabalho. Le antes o `B-BRIEFING-arquitetura-AGENTE.md` (a
> logica) e tem a mao o `A-MANUAL-implementacao-DAVID.md` (a visao do David). Executa os
> passos por ordem. NAO saltes o Passo 0. NAO comeces a construir antes do Passo 2 fechar.

## Passo 0 — Rede de seguranca (git) [OBRIGATORIO, ANTES DE TUDO]

1. Se o projecto ainda nao for repositorio git: `git init` e cria um `.gitignore` minimo
   (ignora apenas scratch/temporarios; **inclui** a pasta `Artefactos-existentes/` no
   versionamento — o David quer rasto de que os usaste como referencia sem os corromper).
2. Faz um **commit pre-grill** com TODO o estado actual (incluindo `Artefactos-existentes/`
   e estes ficheiros de bootstrap). Mensagem: `pre-grill: estado inicial antes do
   html-factory`. Esta e a fotografia do antes — o ponto de retorno limpo.
3. Cria e muda para uma branch de trabalho: `git checkout -b grill1`.
4. A partir daqui, TODO o trabalho acontece na branch `grill1`, com um commit a cada
   incremento funcional. O estado base fica intacto.

## Passo 1 — Mapeamento dos artefactos existentes [OBRIGATORIO antes do grill]

A pasta `Artefactos-existentes/` contem VARIOS artefactos HTML do David, postos la de
proposito: antes de qualquer decisao profunda, e preciso ver exactamente o que ele faz.
Convencao de arrumacao ja aplicada pelo David: artefactos que **usam server** ou que
**pre-carregam dados de ficheiros** estao em **subpastas proprias**; os **HTML soltos e
auto-suficientes** estao na **raiz** dessa pasta.

**Tarefa:** mapear CADA artefacto, decompondo-o em tres camadas (ver briefing sec. 5-BIS):
- **Dados** — estruturas, campos, relacoes, hierarquias; como carrega; SSOT de facto.
- **Motor** — logica de transformacao; que modos (relacoes / hierarquia / tabela).
- **UI / Viewer** — que blocos visuais contem; o que se repete entre artefactos.

- **Tu decides** se lancas subagentes de verificacao (ex.: verificadores de HTML/codigo)
  para inspeccionar cada artefacto — recomenda-se, para ficares com o mapa fiavel. Aplica
  o gate de arquitectura de execucao: avalia se vais sozinho ou com subagentes, e porque.
- **Entregavel (commit obrigatorio):** `docs/mapa-artefactos.md` — por artefacto, as tres
  camadas, mais uma sintese transversal: que tipos de dados/blocos REAPARECEM (o padrao
  comum), e de onde recomendas comecar o piloto (nota: o curador e o mais rico mas o mais
  complexo e atipico; pode haver blocos mais simples noutros para o piloto).

Este mapa e o **input factual do Passo 2**. NAO entres no grill sem ele.

## Passo 2 — grill-with-docs [OBRIGATORIO antes de construir]

Corre o skill **`grill-with-docs`**, **alimentado pelo `docs/mapa-artefactos.md` do Passo
1**. Objectivo: garantir que percebes a fundo o que vais implementar E fechar com o David
as decisoes ainda em aberto — agora com base no padrao real dos artefactos dele, nao num
palpite. NAO comeces a construir enquanto estas nao estiverem fixadas e escritas.

Tensoes a fechar no grill (do briefing, sec. 6):
1. **Alfandega generica (T2)** — qual o contrato unico de dados. Deriva-a do **padrao
   comum** que o mapa revelou (tipos de dados/blocos que reaparecem entre artefactos), nao
   so do curador. Esta e a peca-mae: se nascer torta, a biblioteca toda fica acoplada ao
   formato errado. Fecha-a primeiro.
2. **Desacoplamento (T1)** — como extrair os blocos sem o STATE global; metodo (piloto vs.
   tudo).
3. **Auxiliar/espelho** — confirma se ainda e peca propria ou se foi subsumido pelo
   manifesto + folha de binding.
4. **Silhuetas / Claude Design** — o editor de planta esta decidido: o David monta o
   **layout base no Claude Design**, com **silhuetas** dos blocos (os blocos reais NUNCA
   entram la — ele regenera e corrompe-os). Recomenda-lhe a **fidelidade das silhuetas**
   por tipo de bloco (retangulo etiquetado vs. mini-preview) e valida na pratica o
   import/export do Claude Design (e research preview) antes de assentar o fluxo nele.

Escreve as decisoes fechadas em `docs/decisoes-grill.md` e faz commit.

## Passo 3 em diante — Construcao por INCREMENTO VERTICAL FUNCIONAL

Regra absoluta do David: **cada passo funcional antes do seguinte.** Nada de montar o
esqueleto todo em abstracto. Cada incremento entrega algo a funcionar de ponta a ponta,
provado, e so depois passas ao proximo. Cada incremento = um commit em `grill1`.

Sequencia (afina conforme o grill):
1. Caixa (Dados/Config/Motor/Viewer) + Alfandega + **um** bloco (piloto recomendado: o
   grafo) a renderizar dados reais. **Prova que funciona** -> commit.
2. Generaliza a Alfandega a partir desse caso real -> commit.
3. Segundo bloco no mesmo contrato -> prova -> commit.
4. Restantes blocos, um a um.
5. Silhuetas dos blocos + o David monta o **layout base no Claude Design** -> exporta ->
   tu les o layout e **substituis as silhuetas pelos blocos reais** -> prova -> commit.
6. Folha de binding -> prova -> commit.
7. Build final single-file (junta layout + blocos + dados) -> prova -> commit.

A cada incremento, reporta ao David em linguagem de arquitecto nao-tecnico (Linguagem
Ubiqua + traducao civil; uma ideia por vez, com gate de confirmacao — ver briefing sec. 7).

## Limites (nao ultrapasses)

- Nao decidas sozinho as tensoes do Passo 2 — sao do David.
- Nao avances de incremento sem o anterior estar funcional e commitado.
- Nao quebres os invariantes (single-file final, imutabilidade, um-so-sentido, estetica
  fora dos dados — briefing sec. 3).
- Se algo te empurrar para "semanas de infraestrutura" antes de algo funcionar, PARA e
  reporta: viola o criterio-mae.
