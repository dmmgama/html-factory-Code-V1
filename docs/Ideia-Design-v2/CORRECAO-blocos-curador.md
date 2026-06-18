---
created: 2026-06-17 22:40
project: html-artifact-factory
chat: Correccao dos blocos do curador (linhas reais + bloco-fantasma)
session: SArq-3
status: correcao
summary: >
  Correccao critica: as linhas dos blocos do curador citadas pela SArq-3 vieram de COPIA web
  e estao todas erradas (desvio 140-290 linhas); renderAsgMindmap NAO existe (mind-map e um
  modo de renderGraph, nao um bloco). Usar a tabela de linhas reais do fork antes de extrair.
---

# Correcção — blocos do curador (NÃO usar as linhas da SArq-3)

> Documento de correcção, para o grill e para a extracção (Fase 2). Tem precedência sobre
> as linhas citadas em `arquitetura-html-factory-SArq-3.md` e nos diagramas. Confirmado pelo
> fork (subagente que leu o `projetos-curador-v3.html` REAL no filesystem).

## 1. As linhas da SArq-3 estão TODAS erradas (cópia ≠ real)

A SArq-3 leu o curador a partir de uma **cópia na Google Drive** (sessão modo web). As 7
linhas citadas têm **desvio sistemático de 140–290 linhas** face ao ficheiro real. **Não as
uses.** Fonte de verdade = o `projetos-curador-v3.html` no repositório, lido pelo fork.

| Bloco | Linha citada (SArq-3, cópia) | Estado real |
|---|---|---|
| renderGraph | 1275 | **conferir no real** (tabela do fork) |
| renderGenealogy | 1502 | conferir no real |
| renderCronologia | 1485 | conferir no real |
| renderHead / renderBody | 887 / 1088 | conferir no real |
| renderFilterBar | 820 | conferir no real |
| makeProjCard | 1691 | conferir no real |
| renderAsgMindmap | 1872 | **NÃO EXISTE — ver §2** |

> **Acção:** colar aqui (ou em ficheiro próprio na ideia-design) a **tabela de linhas reais**
> produzida pelo fork, e usá-la como referência única na extracção. Este ficheiro é o stub
> que essa tabela preenche.

## 2. Bloco-fantasma: o mind-map NÃO é um bloco

`renderAsgMindmap` **não existe** no curador real. O mind-map não é uma peça autónoma — é um
**modo dentro de `renderGraph`** (activado por `UI.graphMode === "mindmap"`).

**Consequências (importantes):**
- Quem for extrair blocos pela lista da SArq-3 vai **procurar uma peça que não está lá**.
- Confirma a tese de vocabulário: **mind-map é uma VISTA/modo, não um modo do Motor nem um
  bloco**. Reforça a reconciliação "modos (relações/hierarquia/tabela) vs. vistas".
- Na biblioteca de blocos, o mind-map nasce como **variante do bloco-grafo**, não como bloco
  separado.

## 3. O que isto muda na contagem de blocos

A SArq-3 dizia "7 blocos". Reais: os 6 verdadeiros (grafo, genealogia/árvore, cronologia/
timeline, tabela [head+body], filtros, card) + o mind-map **dentro** do grafo. Contar 6
blocos + 1 modo, não 7 blocos.

## 4. Para o grill

- Usar a tabela de linhas reais (do fork), nunca as da SArq-3.
- Tratar o mind-map como modo do grafo na extracção.
- Este achado é prova viva de "mind-map = vista, não modo do Motor" — levar para a
  reconciliação de vocabulário.
