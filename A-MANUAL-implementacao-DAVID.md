---
created: 2026-06-17 19:10
project: html-artifact-factory
chat: Bootstrap do factory em Claude Code
session: SArq-3
status: vivo
summary: >
  Manual humano (para o David) de como instalar e operar o html-factory num projecto
  Claude Code: o que e, que ficheiros entregar ao agente, a ordem dos passos, e como
  saber que cada incremento esta pronto.
---

# Manual de implementacao do html-factory — para o David

> Para ti, nao para o agente. Explica como por isto a andar num projecto Claude Code, o
> que esperar de cada passo, e como saber que esta a correr bem. Linguagem de arquitecto
> nao-tecnico, com as analogias civis de sempre.

---

## 1. O que vais montar, em uma imagem

Pensa numa **fabrica de edificios HTML**. Tu nao pousas tijolos — desenhas plantas e
dizes ao empreiteiro (o Claude Code) o que erguer. A fabrica tem tres coisas:

- **Os tijolos** = *blocos* (arvore, grafo, tabela, cartoes, filtros...). Pecas prontas,
  reutilizaveis.
- **A planta** = um ficheiro (`workspace.json`) onde dizes "aqui uma tabela, ali uma
  arvore, a esquerda filtros". E a tua *linguagem de mudanca* — em vez de explicares por
  palavras, entregas a planta.
- **O empreiteiro** = o Claude Code, que le a planta, pega nos tijolos e ergue o edificio
  (o HTML final, num so ficheiro).

E uma **alfandega** (o contrato de dados) garante que todos os tijolos encaixam na mesma
fundacao — defines o molde uma vez e nunca mais explicas o formato.

## 2. O que entregas ao agente (3 ficheiros)

Esta pasta tem tres ficheiros. Entrega-os ao Claude Code por esta ordem:

1. **`B-BRIEFING-arquitetura-AGENTE.md`** — o que ele vai montar e porque (a logica toda,
   pastas, ficheiros, invariantes). E o manual *dele*.
2. **`C-INSTRUCAO-arranque-AGENTE.md`** — a primeira ordem: fazer git, correr um
   grill-with-docs para perceber tudo e fechar as decisoes em aberto contigo, e so depois
   construir, passo a passo.
3. (Este manual fica contigo — nao precisas de o dar ao agente.)

## 3. O que preparas ANTES de arrancar

- Cria uma pasta **`Artefactos-existentes/`** no projecto e poe la os teus artefactos
  HTML actuais (o curador e outros). Servem de mina de tijolos.
  - **Regra de arrumacao:** os artefactos que **pre-carregam dados de ficheiros** ou que
    **usam um server** ficam em **subpastas proprias** (cada um na sua). Os que sao um
    **HTML solto e auto-suficiente** ficam **soltos** na raiz dessa pasta.
- Mais nada. O agente trata do resto.

## 4. Como isto corre — os passos (e como sabes que cada um esta pronto)

O agente trabalha por **incrementos verticais**: cada passo entrega *algo a funcionar de
ponta a ponta* antes de avancar. Nunca monta tudo em abstracto para so no fim testar. E o
teu criterio-mae aplicado a obra: nada de "duas semanas a montar antes de ver algo
funcionar".

**Passo 0 — Rede de seguranca (git).** Antes de tocar em nada, o agente faz uma
"fotografia do antes" (commit) e abre uma linha de trabalho separada (branch `grill1`).
*Pronto quando:* existe o commit pre-grill e ele esta a trabalhar na branch `grill1`.

**Passo 1 — Mapeamento.** Antes de qualquer decisão, o agente abre os teus artefactos e
mapeia exactamente o que cada um contém, separado em três camadas — **Dados**, **Motor**,
**UI**. Pode lançar ajudantes para verificar o código de cada um. *Pronto quando:* tens um
mapa (por artefacto + o que se repete entre eles) que mostra o tipo de coisa que fazes — e
é esse padrão, não um só artefacto, que vai alimentar as decisões seguintes.

**Passo 2 — Grill (ele interroga-te), com o mapa na mão.** Com o mapa do Passo 1 como
base, o agente faz-te perguntas para fechar as decisões em aberto — desde logo o contrato
de dados (a Alfândega), que nasce do padrão comum aos teus artefactos, não de um palpite.
*Pronto quando:* as decisões ficaram fixadas contigo, escritas.

**Passo 3 em diante — Construcao incremental.** Caixa + Alfandega + **um** bloco a
funcionar -> provas -> proximo bloco -> ... -> manifesto -> binding -> (editor, se
decidido). Cada incremento e um commit. *Pronto quando:* cada peca funciona sozinha antes
de a seguinte comecar.

## 5. O que exiges, sempre (as tuas regras de ouro)

- **Cada passo funcional antes do seguinte.** Se ele quiser saltar a frente, trava.
- **Single-file no fim.** O edificio final e um HTML so, que abre offline.
- **Um so sentido.** A informacao circula clique -> motor -> dados -> ecra; o ecra nunca
  altera dados directamente. Exiges esta frase; nao a implementas.
- **A planta e a linguagem.** Mudancas ao frontend comunicam-se pela planta/folha, nao
  por prosa solta.
- **Se puxar para "2 semanas a montar" — falhou.** A fabrica serve a simplicidade.

## 6. Se algo correr mal

Esta tudo na branch `grill1` com a fotografia do antes guardada. Se o grill1 descarrilar,
deita-se fora a branch e nao perdeste nada — voltas ao ponto limpo.
