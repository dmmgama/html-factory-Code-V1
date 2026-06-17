# MANUAL — html-factory (técnico, para humanos)

> Manual técnico do projeto. **[A CONFIRMAR]** em quase tudo — o factory ainda não existe;
> este ficheiro cresce à medida que cada peça é construída e provada (Passo 3+).

## O que é
Fábrica de artefactos HTML single-file: uma planta declarativa (`workspace.json`) + uma
biblioteca de blocos reutilizáveis → um HTML final que abre offline. Ver `context.md` para a
arquitetura-alvo e `CLAUDE.md` para a Linguagem Ubíqua.

## Como correr
**[A CONFIRMAR]** — ainda não há build nem `dist/`. Definir quando existir o passo de compilação
(briefing §4: `factory/build/assemble.*` → `factory/dist/workspace.html`).

## Como estender
**[A CONFIRMAR]** — o processo de adicionar um bloco novo (par Motor+Viewer normalizado à
Alfândega) será documentado depois de fechada a Alfândega no grill (Passo 2) e provado o piloto.

## Estrutura
**[A CONFIRMAR]** — proposta em `context.md` §2 / briefing §4; afina-se no grill.

## Validação
- JS embebido de single-file valida-se com `node -e` (ler o `<script>` e instanciá-lo).
  Receita concreta a fixar quando existir o primeiro artefacto.
