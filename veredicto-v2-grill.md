---
created: 2026-06-18
project: html-factory
autor: sessão-fork (Claude Code)
status: relatorio-curto
summary: >
  Relatório curto que acompanha o handoff-grill. Veredicto da sessão-fork sobre a
  docs/Ideia-Design-v2/ (lida pela própria sessão, não delegada) + recomendação para o grill.
  Conclusão: v2 PRONTA; os 2 resíduos foram fechados e verificados.
---

# Veredicto da v2 + recomendação para o grill

> Curto e factual. Acompanha o `handoff-grill.md`. A sessão-fork **leu ela própria** a
> `docs/Ideia-Design-v2/` (sem delegar) e verificou as correcções contra o ficheiro real.

## 1. Veredicto — as preocupações do fork batem certo na v2?

| Preocupação | Estado | Prova |
|---|---|---|
| Furo dos patches (integrar Chassis/Slot/Silhueta + dono do vocabulário) | ✅ Resolvida | `PatchGlossario-integracao.md`: Glossário = dono; `CLAUDE.md` aponta, não absorve |
| Fonte única do vocabulário | ✅ Resolvida | Glossário "dono do vocabulário"; ponteiro no `CLAUDE.md` |
| Passo de build em falta | ✅ Resolvida (input p/ grill) | `ADENDA-passo-build.md`; fluxo-1 tem a caixa "CONSTRUÇÃO (Code)" |
| 3-vs-4 candidatos a editor | ✅ Resolvida | context/roadmap/SVG ✅ 4; **corrigido**: "3→4" no `PatchCDesign-CLAUDE.md` + (d) D-proc no `ADDON` |
| Linhas do curador / bloco-fantasma | ✅ Resolvida | `CORRECAO-blocos-curador.md`: mind-map = modo de `renderGraph`; **tabela de linhas reais colada** (680/747/948/1081/1255/1272/1402; `renderAsgMindmap` não existe, ~1043) + proveniência |

**Conclusão: v2 PRONTA.** Os 2 resíduos que estavam por fechar (número "3→4"; enumeração do
ADDON; tabela de linhas reais) **foram fechados e verificados** pela sessão-fork.

## 2. Recomendação para o grill
- **T2 Alfândega primeiro** — a peça-mãe; fechar a partir do **grafo-piloto**, nunca em abstracto.
  Evidência do M1 puxa para **núcleo comum + perfil por modo** (a árvore é grafo restrito; a
  tabela é Frictionless). Não decidir — é do David.
- **Editor:** fechar só até **direção + teste-gate** (manifesto-em-texto primeiro; Claude Design /
  D-proc presos a passar o teste de **preservar os Slots**, round-trip, 100% mapeável). Não cravar
  a ferramenta final — o piloto (grafo) nem precisa de editor.
- **Build:** dar-lhe **lugar explícito** (caixa no fluxo + marco no roadmap); fechar a Imutabilidade
  ao menos até "build stamp/hash sim/não".
- **Mind-map:** tratar como **modo do bloco-grafo**, não bloco separado, em qualquer extracção.

## 3. Fonte das linhas do curador (não repetir o erro)
As linhas reais estão em `docs/Ideia-Design-v2/CORRECAO-blocos-curador.md` (lidas no
`projetos-curador-v3.html` real pela sessão-fork; detalhe em
`docs/ideia-design/ideiasdesign-report-fork.md`). **Nunca** usar as da SArq-3 (cópia web, erradas).
