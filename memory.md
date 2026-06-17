# memory.md — porquê das decisões

> Regista o *porquê* de decisões arquiteturais/processo. Não é estado corrente (isso é
> `context.md`/`handoff.md`). Append; cada decisão numerada (D1, D2, …).

## D1 — Absorver os backups (limpar `.git` internos)
**Decisão:** remover os `.git` de FichaProjetosJSJ, LifeMap, TableEditor, projeto-ssot dentro de
`Artefactos-existentes/`.
**Porquê:** eram repositórios git próprios → o repo do factory registava-os só como *ponteiros*
(gitlinks), sem o conteúdo. O David confirmou que são **cópias/backups** ("o que interessa é o
sumo"), não código vivo com histórico a preservar. Absorver garante que a referência fica
versionada e legível para o mapeamento (Passo 1).

## D2 — Manter os `.gitignore` internos dos backups
**Decisão:** ao absorver, não apagar os `.gitignore` que estavam dentro de cada backup.
**Porquê:** são sensatos (ignoram node_modules/build) e evitam arrastar lixo para o repo. O
"sumo" (source) fica; o lixo de build não.

## D3 — Branch `grill1` como linha de trabalho; `master` = retorno limpo
**Decisão:** todo o trabalho em `grill1`; `master` fica em `pre-grill`.
**Porquê:** instrução do C-INSTRUCAO (Passo 0). Rede de segurança — o estado "antes" fica
intacto e recuperável a qualquer momento.

## D4 — Instalar governança ANTES do Passo 1
**Decisão:** correr o setup do `ClaudeCodeSetup.md` (camada de continuidade) antes de mapear.
**Porquê:** pedido do David — "ter algum tipo de governo antes de avançar". Sem CLAUDE.md +
continuidade, cada sessão recomeça do zero e o protocolo de fecho/arranque não existe. Fundiu-se
com o C-INSTRUCAO (que governa *o que* construir); a governança governa *como* trabalhamos.

## D5 — Permissões: git read-only + `node -e`
**Decisão:** `.claude/settings.json` permite git status/diff/log/show **e** `node -e`.
**Porquê:** o factory produz HTML single-file e validar o JS embebido faz-se com `node -e` a
cada incremento (padrão já usado no LifeMap). Sem isto, cada validação pedia aprovação manual.
Trade-off aceite pelo David (é execução arbitrária, mas necessária ao fluxo).

## D6 — Conjunto completo de governança (inclui bugs.md/additions.md)
**Decisão:** criar os 11 ficheiros, incluindo `bugs.md` e `additions.md` append-only.
**Porquê:** o David escolheu espelhar o LifeMap por inteiro, para o protocolo de arranque
(que lê bugs.md/additions.md no ramo "adições ao roadmap") funcionar desde já.

## D7 — Track de sessões único `S#`
**Decisão:** usar só `S#`; abandonar `SG#` (setup vs trabalho).
**Porquê:** o LifeMap já tinha consolidado isto (a sua D12). O `ClaudeCodeSetup.md` ainda mostra
`SG#`, mas está desatualizado; seguimos a versão mais recente do protocolo.

## D8 — Mapa (M1) feito com subagentes `Explore` read-only; síntese fica comigo
**Decisão:** repartir a leitura de `Artefactos-existentes/` por 5 subagentes `Explore` (read-only),
verificar com `code-reviewer` + leitura direta de 2 ficheiros centrais, e fazer **eu** a síntese.
**Porquê:** são ~18 famílias de artefactos, vários >300 KB — ler tudo no contexto principal era
lento e enchia-o. `Explore` é read-only → garante que os backups não são corrompidos. A síntese do
**padrão comum** alimenta a tensão-mãe T2 (Alfândega) → não se delega; é juízo que fica comigo/David.

## D9 — Curador: a app de referência é o **v3** (não o v4)
**Decisão:** tratar `projetos-curador-v3.html` como app principal de referência; `v4` é experimento.
**Porquê:** correção do David ("o que interessa é o v3"). O `v4` foi um ensaio de atribuições
bilaterais que não entrou em produção. O `dashboard-v3.html` é o **mapa do próprio curador** (declara
as 3 camadas). O v3 tem o contrato de grafo mais rico (projeto/link/domínio) e o melhor Ciclo Reativo
(`commit()=save()+renderAll()`) — é o melhor manancial para a Alfândega e para a tensão T1.

## D10 — Descoberta do mapa: o domínio reduz-se a 3 modos; as 4 peças já existem dispersas
**Decisão (registo, não escolha):** o levantamento mostra que quase tudo cai em **grafo / árvore /
tabela** (os 3 modos do Motor), e que as 4 peças da fábrica já existem na natureza mas separadas:
contrato de dados → TableEditor (Frictionless); viewer cego → `FloorViewer`; ciclo reativo →
curador-v3; formato de grafo → `knowledge-graph.json`.
**Porquê importa:** valida que há matéria para uma Alfândega real e enquadra a grande pergunta do
grill (T2): **um** contrato para os 3 modos ou **um por modo** com núcleo comum. Detalhe em
[`docs/mapa-artefactos.md`](docs/mapa-artefactos.md).
