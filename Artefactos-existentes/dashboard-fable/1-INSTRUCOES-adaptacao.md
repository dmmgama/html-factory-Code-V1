---
created: 2026-06-10 17:45
chat: Dashboard governo colapsável — especificação de adaptação
summary: >
  Especificação dos requisitos 1–6 da adaptação do dashboard (hierarquia colapsável,
  vista geral/tour, regras do inspector, toggle técnico/não-técnico, manuais), com
  schema de dados alvo, hierarquia de partida e critérios de aceitação testáveis.
---

# INSTRUÇÕES DE ADAPTAÇÃO — Dashboard do Governo AI

> Spec consumida pelo `Agent.md`. Os requisitos são normativos; as sugestões de implementação são-no apenas onde marcadas **deve**.

---

## §1. Requisito 1 — Hierarquia colapsável

1.1. Cada folha organiza os nós em **grupos pai → filhos** (1 nível de profundidade chega; 2 é o máximo). Hierarquia de partida (refinável pelo subagente de conteúdo, justificando):
- **Folha 1 (A Sessão):** Inputs · Análises · Decisões · Outputs
- **Folha 2 (O Fecho):** Preparação · Pendentes · Execução · Marcos
- **Folha 3 (O Pacote em Execução):** Kit (repositório) · Orquestração (passos) · Criados · Marco
- **Folha 4 (Operação):** Arranque · Runtime · Fecho · Relógio & Braços

1.2. **Estado inicial: tudo colapsado** — só as caixas-pai visíveis, com as setas agregadas entre pais.
1.3. Expandir um pai mostra os filhos **dentro/abaixo dele** e re-liga as setas aos filhos reais; colapsar re-agrega. As setas filho↔nó-externo, com o pai colapsado, ligam ao pai (o grafo é sempre legível, em qualquer combinação de estados).
1.4. Cada caixa com filhos tem um **botão ± no próprio retângulo** (canto superior direito), clicável sem disparar a seleção.
1.5. Controles globais por folha: «Expandir tudo» / «Colapsar tudo».

## §2. Requisito 2+3 — Vista geral e detalhe de pai

2.1. **Sem nada selecionado**, o painel lateral mostra a **vista geral da folha**: 1 parágrafo do que a folha conta + a explicação de **como as caixas-pai se ligam entre si** (uma linha por ligação pai→pai).
2.2. **Tour:** botão «TOUR» que percorre as caixas-pai por ordem lógica — destaca a caixa, mostra o texto dela no painel, botões anterior/seguinte/sair. (Padrão inspirado nas guided tours do Understand-Anything.)
2.3. **Clique numa caixa-pai** → o painel detalha o papel desse grupo no conjunto e lista os filhos (clicáveis).

## §3. Requisito 4 — Inspector por nó + schema de dados

3.1. Clique em qualquer nó → painel com a explicação, segundo a **regra de conteúdo**:
- nó `kind: "processo"` → explica **o que o processo faz e ao que se liga** (as ligações entram na prosa, não só na lista);
- nó `kind: "ficheiro"` → explica **o que esse ficheiro faz**, e o painel mostra obrigatoriamente o campo **Ficheiro:** com o nome/path;
- restantes kinds (decisão, marco, pendente) → como hoje, com estado visível.

3.2. **Schema do bloco DATA** (JS, delimitado por `/* ===DATA-START=== */ … /* ===DATA-END=== */`; é o único sítio que futuros updates tocam):

```js
node = {
  id, parent,            // parent: id do grupo-pai, ou null se é pai
  level,                 // 0 = pai, 1 = filho (2 só se justificado)
  kind,                  // "grupo" | "processo" | "ficheiro" | "decisao" | "marco" | "pendente"
  file,                  // path/nome do ficheiro associado (obrigatório se kind=ficheiro; senão omitir)
  x, y, w, h, tag, l,    // geometria + etiqueta + linhas de label (como hoje)
  desc_tec,              // explicação técnica (registo atual)
  desc_simples           // explicação não-técnica (novo — ver 3.3)
}
view = { id, titulo, overview_tec, overview_simples, parent_links: [[paiA,paiB,frase]], tour: [ids por ordem] }
edge = [from, to, label, crit?, dash?]   // como hoje
```

3.3. `desc_simples`: para um leitor inteligente que **não vive neste sistema** — sem jargão (nada de "append-only", "SSOT", "front matter" sem tradução), frases curtas, analogia quando ajudar. Não é um resumo da técnica; é outra explicação.

## §4. Requisito 5 — Toggle Técnico / Não-técnico

4.1. Toggle persistente no header (default: **Não-técnico**). Troca **todas** as explicações: descrições de nós, vistas gerais, textos da tour. Labels das caixas mantêm-se (são nomes, não explicações).
4.2. O estado do toggle não se perde ao mudar de folha.

## §5. Requisito 6 — Manuais (ver Agent.md §4)

`4-manual/MANUAL-LLM-dashboard.md` (schema + procedimento de update + validação) e `4-manual/MANUAL-USO-dashboard.md` (uso, para o David). O MANUAL-LLM deve permitir que um modelo barato (Haiku 4.5) faça um update de conteúdo sem ler mais nada além dele + o doc de conteúdo novo + o bloco DATA.

## §6. Critérios de aceitação (QA corre todos)

1. Abrir por duplo-clique, sem build/servidor; sem erros na consola.
2. Cada folha abre **colapsada nos pais**; setas pai→pai presentes e legíveis.
3. ± expande/colapsa sem partir setas: em qualquer combinação de estados, nenhuma seta aponta para nó invisível.
4. Sem seleção → vista geral da folha com ligações pai→pai. Tour funciona nas 4 folhas (avançar/recuar/sair).
5. Clique em pai → papel do grupo + filhos clicáveis. Clique em filho → regra processo/ficheiro cumprida; todo o `kind:"ficheiro"` mostra **Ficheiro:**.
6. Toggle troca todos os textos nos dois sentidos, incluindo tour e vistas gerais; sobrevive à mudança de folha.
7. Nenhum nó sem `desc_tec` E `desc_simples` (exceto marcados `(a confirmar)` — listados no relatório).
8. Conteúdo fiel a `3-conteudo/`: D2 aparece como superseded; pendentes (ID, T3, Base:, Blackboard/Coordenação) aparecem como pendentes; nada inventado.
9. Estética preservada (blueprint, cartela, paleta); pan/zoom/AJUSTAR continuam a funcionar; Esc limpa seleção.
10. Backup `_v1-backup.html` existe e abre.

## §7. Regras por pasta

| Pasta | Regra |
|---|---|
| `understand/` | Referência read-only (schema/padrões). Nunca editar. |
| `2-dashboard/` | O único código a modificar. Backup antes do refactor. |
| `3-conteudo/` | Autoridade do conteúdo, read-only. Cristalização v2 > tudo. |
| `4-manual/` | Output dos manuais. |
| Fora de `DashboardGoverno/` | Proibido escrever. |

— Fim —
