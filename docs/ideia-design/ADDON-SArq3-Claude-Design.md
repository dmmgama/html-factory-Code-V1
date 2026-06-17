---
created: 2026-06-17 20:10
project: html-artifact-factory
chat: Claude Design como candidato a editor de planta
session: SArq-3
status: vivo
summary: >
  Add-on explicativo: introduz o Claude Design como CANDIDATO a editor de planta (a
  estudar no grill/M2), nao como decisao fechada. Traz a mecanica de silhuetas e os
  riscos ja mapeados, para o agente avaliar contra as outras opcoes.
---

# ADD-ON — Claude Design como candidato a editor de planta (NAO e decisao)

> Para o agente Claude Code. Le isto ANTES de correr o grill (M2). NAO altera o que ja
> esta feito (M1/mapa). Acrescenta UM candidato novo a tensao "Editor", com a mecanica ja
> pensada. **Trata-o como hipotese a avaliar, nao como verdade assente.** A decisao e do
> David, no grill, com o criterio-mae a desempatar.

## 0. Porque este add-on existe

O mapa (M1) e a governanca foram feitos numa sessao anterior, que **nao conhecia o Claude
Design**. Entretanto, numa sessao de arquitectura (SArq-3), o David explorou o Claude
Design como possivel **editor de planta** e desenhou a mecanica que o tornaria compativel
com a arquitectura (silhuetas). Este add-on traz isso para o projecto **como candidato**,
para a tensao "Editor" do grill deixar de ter so duas opcoes e passar a ter tres — uma
delas com a mecanica ja estudada.

## 1. O que e o Claude Design (factual)

Produto da Anthropic Labs (research preview, lancado Abr/2026, corre em Opus). Tela
visual: descreves/montas em linguagem natural + arrasto + comentarios inline + botoes de
ajuste; gera HTML/CSS/JS a correr (nao mockups). Exporta HTML standalone, PDF, PPTX,
Canva, e tem um **handoff bundle para o Claude Code**. Le identidade visual de um
repo/ficheiro/deck (extrai cores, tipografia, componentes) uma vez por projecto.

## 2. Como ENCAIXARIA na arquitectura (a hipotese a testar)

O Claude Design serviria **so o layout base** (a planta), nunca a fundacao (SSOT,
Alfandega, Motor, blocos — esses ficam em ti, no Code). Fluxo proposto:

```
   LAYOUT BASE (Claude Design)      TU (Claude Code)              RESULTADO
   o David monta zonas com      ->  les o layout exportado    ->  HTML single-file
   SILHUETAS dos blocos             + substituis cada silhueta     final, offline
   -> exporta layout/handoff        pelo BLOCO REAL da biblioteca
                                     + injectas os dados
```

Isto e o **Caminho 1** ja escolhido (a planta declara, o Code constroi) — o Claude Design
seria apenas a ferramenta que produz a planta.

## 3. Conceito-chave: SILHUETA (porque os blocos reais NAO entram no Claude Design)

O Claude Design e um **gerador** — reinterpreta o que recebe. Se la meteres um bloco real
(ligado ao SSOT), ele regenera-o e **corrompe-o**. Logo, o David monta o layout com
**silhuetas**: representacoes leves e descartaveis de cada bloco (do retangulo etiquetado
"BLOCO: grafo" ate um mini-preview do aspecto). Servem so para desenhar a disposicao;
morrem depois. No fim, TU les o layout e **substituis cada silhueta pelo bloco real** da
biblioteca.

**Se este candidato vencer no grill:** recomendas ao David a **fidelidade das silhuetas
por tipo de bloco** (retangulo simples vs. mini-preview — conforme o bloco; um bloco cujo
tamanho/proporcao afecta o layout pode pedir mini-preview).

## 4. Riscos / o que VALIDAR antes de adoptar (nao assumir que funciona)

- **Research preview.** Bugs conhecidos (comentarios inline que desaparecem, erros de save
  em vista compacta, lag com repos grandes).
- **Custo.** Corre em Opus; sessoes iterativas gastam depressa a quota de design.
- **Import/export por provar.** O passo critico — o layout exportado ser **legivel e
  estavel** o suficiente para tu o leres e mapeares silhuetas -> blocos — NAO esta testado.
  Antes de assentar o fluxo no Claude Design, **faz um teste pequeno**: um layout trivial,
  exporta, confirma que consegues parsear/usar o output.
- **Deriva estetica.** O output pode afastar-se do design-system com a iteracao.

## 5. O que o agente deve fazer com isto (instrucao operacional)

1. **NAO** tratar o Claude Design como decidido. Continua a ser a tensao "Editor", agora
   com 3 candidatos: (a) **Claude Design + silhuetas** (este add-on); (b)
   **manifesto-em-texto** editavel a mao; (c) **Gridstack / editor proprio**.
2. No grill (M2), apresentar os 3 ao David com trade-offs, e **recomendar** um — desempate
   pelo criterio-mae (qual reduz mais o atrito sem puxar para "semanas a montar").
3. Se o David escolher o Claude Design, **so entao** marcar a tensao como fechada e fazer
   o teste de import/export (ponto 4) antes de construir o passo do editor (M9).
4. Registar a decisao (qualquer que seja) em `docs/decisoes-grill.md`.

## 6. Patches propostos (opcionais, separados)

Acompanham este add-on tres ficheiros `PatchCDesign-*` com o texto exato para
`context.md`, `roadmap.md` e `CLAUDE.md` — todos redigidos como **"candidato a estudar"**,
nao como decisao. Aplica-os so se concordares; sao para manter os ficheiros de
continuidade cientes do candidato, sem o transformar em verdade.
