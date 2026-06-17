---
_INSTRUCAO_AGENTE: "No frontmatter lê APENAS recipient. Define destinatário e natureza da tua ação. Salta para o corpo e age conforme. Não resumas."
recipient: Humans-Informative
created: 2026-06-09
type: manual
platform: Claude-Desktop
session_father: "sessão de arquitetura do starter kit (audit AI Protocols)"
class: III
autonomy: requires-set
set: ecossistema-protocolos
status: provisional
entry: INSTALACAO-PROJETO.md
tags: [operar, projeto, cristalizacao, manutencao, guia, governanca]
summary: "Guia do operador (David) de um projeto já montado: como correr uma sessão, quando cristalizar e fazer hand-raise, como fechar, e a cadência de manutenção."
---

# OPERAR-PROJETO — o que fazer num projeto a correr

> Para ti, David, quando voltas a um projeto já montado e não te entendes. Contraparte da `INSTALACAO-PROJETO` (que monta) — esta diz o que **fazer** depois.
> O projeto já tem SP, continuidade e ficha. Não montas nada aqui; operas.

---

## 1. Começar uma sessão

Abres a sessão e dás-lhe o projeto (ou, num Claude Project, o SP já é as instruções). O agente faz o arranque sozinho: lê o SP, cria a ficha, propõe o número de sessão (`<prefixo>-S{n}`), lê o `handoff` e o `context`, e fica pronto. **Não tens de dar ficheiros.** Se for sessão de uma tarefa específica (ex.: um grill-me), dás-lhe a prompt dessa tarefa; o resto é automático.

Se algo do arranque falhar (handoff/context inacessíveis), o agente avisa e pergunta se prossegue. Se disser "sessão de raiz", é porque o projeto está vazio — normal numa primeira sessão.

## 2. Durante a sessão — trabalhar

Trabalhas normalmente. Três coisas que o sistema faz por baixo, e que deves reconhecer:

### 2.1 Cristalizar (matéria do projeto)
Quando se produz algo custoso e decidido que vais reusar — uma decisão de arquitetura, um conceito, um inventário — o agente cristaliza: uma **cabeça destilada** ("decidiu-se X em vez de Y porque Z") + **ponteiro** ao substrato. Vai para o `context.md` (ou para a wiki do projeto, se existir). Não cristalizas tudo: o gatilho é **custo alto + decidido + ≥2 usos**.

### 2.2 Hand-raise — *o que resolve a ansiedade de perder o essencial*
Isto é o ponto central. **Quando aparece, no meio de uma sessão, matéria importante que não tem a ver com este projeto** — uma verdade sobre governança, uma aprendizagem de arquitetura, algo sobre ti, um padrão — **não tens de decidir onde isso vai.** Dizes "hand-raise" (ou o agente sinaliza), e a matéria é **capturada no momento, no inbox transversal**. Fica lá, segura, até a processares na manutenção (§4). A regra é: **captura imediata, colocação diferida.** Nada importante se perde por não saberes, naquele segundo, onde encaixa.

> É para isto que o inbox existe: para o teu cérebro poder largar a matéria sabendo que ela ficou registada, em vez de a tentar segurar até "arrumar".

### 2.3 Watchdog
Em sessões longas o contexto degrada. Se o agente detetar que está a perder o fio (muito contexto, inconsistências próprias), **oferece** fechar — não impõe. Aceita quando sentires que a sessão já não rende; é melhor fechar limpo e reabrir do que arrastar.

## 3. Fechar uma sessão

Dizes **"handoff"** / **"fecha"**. O agente, por ordem: reescreve o `handoff` (estado vivo), acrescenta entrada ao `context` (raciocínio + relógio `S{n}`), finaliza a ficha, e confirma com read-after-write. Não há mais nada a manter à mão — sem log de mutações, sem quádruplo registo.

Se vais sair a meio sem fechar, não faz mal: a ficha foi preenchida ao longo da sessão (não no fim), por isso o essencial ficou. Mas fecha sempre que puderes — é o handoff que faz a próxima sessão arrancar cheia.

## 4. Manutenção — a cadência *(acionas tu)*

O sistema acumula duas coisas que precisam de ser processadas de vez em quando. Não é por sessão; é por cadência (semanal, ou quando o inbox encher):

1. **Processar o inbox transversal de hand-raise.** Pegas no que foi capturado e **colocas** cada peça no sítio certo — no Mapa AI / 2nd brain, na classe certa (I/II/III). É aqui que a "colocação diferida" se cumpre. O inbox esvazia; o conhecimento fica arrumado e ligado.
2. **Processar a Aprendizagem** (`Aprendizagem.md`). As lições onde uma regra falhou em uso. Se justificarem, regeneras o protocolo afetado (via cannon-rules). É o loop que impede o drift de se acumular.

> Sem esta cadência, o inbox vira pântano e os protocolos derivam. É a única parte que exige disciplina tua — o resto o agente faz.

## 5. Se te perderes

Lê o `context.md` (o que se fez e porquê, com o relógio) e o `handoff` (onde ficaste). Este guia é só a seta "o que fazer". Para entender o conceito de cristalização, o protocolo de cristalização do conjunto. Para montar **outro** projeto, a `INSTALACAO-PROJETO`.

---

> **Regra de ouro do operador:** captura sempre, decide depois. A ansiedade vem de tentar arrumar no momento da descoberta — o sistema existe para separar as duas coisas.
