---
created: 2026-06-17 21:30
project: html-artifact-factory
chat: Integracao do glossario e vocabulario novo SArq-3
session: SArq-3
status: patch
summary: >
  Patch de integracao: leva o vocabulario novo da SArq-3 (Chassis, Slot, Silhueta,
  Manifesto, fluxos D-sil/D-proc) aos ficheiros de continuidade, e estabelece o
  GLOSSARIO como dono unico do vocabulario (CLAUDE.md passa a apontar para ele).
---

# PatchGlossario — integração do vocabulário SArq-3

> Tapa o furo que o agente sinalizou: os patches PatchCDesign só tratam do candidato
> Claude Design; faltava integrar **Chassis / Slot / Silhueta** e reconciliar o
> **Glossário** como dono do vocabulário. Aplicar ao arrancar o grill, junto com os
> PatchCDesign. Mantém tudo como **referência/vocabulário**, não decide tensões.

---

## A) CLAUDE.md — Glossário passa a dono do vocabulário (CLAUDE.md só APONTA)

> Princípio: o CLAUDE.md é canon — evita acumular vocabulário mutável. Não absorve
> definições; **aponta** para o Glossário, que é o dono. *Quanto* da tabela actual migra
> para o Glossário é **decisão do agente no grill** (não imposta aqui).

### A1. No bloco de topo (os documentos que mandam), ACRESCENTAR uma linha:
```
> - [`GLOSSARIO-html-factory.md`](docs/ideia-design/GLOSSARIO-html-factory.md) — **dono do
>   vocabulário**. Qualquer termo do projeto define-se aqui; os outros documentos apontam
>   para cá, não repetem definições.
```

### A2. Sobre a tabela "Linguagem Ubíqua" — ACRESCENTAR um ponteiro por cima dela:
```
> **Fonte única do vocabulário: `GLOSSARIO-html-factory.md`** (dono). Esta tabela é, no
> máximo, um atalho de trabalho; em caso de divergência manda o Glossário. Termos novos
> (Chassis, Slot, Silhueta...) vivem só no Glossário.
```

### A3. Migração da tabela — DECISÃO DO AGENTE NO GRILL (não fazer já)
O canon não deve duplicar o Glossário. No grill, o agente decide quanto da tabela actual
**migra** para o Glossário e quanto, se algum, fica como atalho mínimo no CLAUDE.md. NÃO
acrescentar termos novos à tabela do CLAUDE.md — esses já vivem no Glossário.

---

## B) context.md — vocabulário e fluxos novos

### B1. Em "§2 Arquitetura", na lista de peças, ACRESCENTAR ao fim um ponteiro (não duplicar):
```
Vocabulário completo e definições: `docs/ideia-design/GLOSSARIO-html-factory.md` (dono do
vocabulário). A SArq-3 acrescentou Chassis, Slot e Silhueta — ver Glossário; não repetir
aqui as definições.
```

### B2. Em "§2", a seguir ao fluxo, ACRESCENTAR a nota dos fluxos de frontend:
```
Fluxos de produção da Planta (candidatos, ver tensão Editor §6):
- **planta→Code** (nuclear): a planta declara, o Code constrói.
- **D-sil:** montar com Silhuetas dentro do Claude Design.
- **D-proc** (paralelo, autocontido): Chassis desenhado no Procreate, numerado → Claude
  Design traduz → Code injecta nos Slots. Elo a provar: Claude Design preservar os Slots.
```

### B3. Em "§6 Tensões", AFINAR a linha do Motor/modos (precisão de vocabulário):
```
- **Vocabulário modos vs. vistas (a fixar no grill):** os 3 MODOS do Motor são
  relações / hierarquia / tabela. "grafo" e "árvore" são VISTAS (Viewer), não modos —
  grafo = relações+hierarquia. O mapa M1 escreveu "grafo/árvore/tabela"; reconciliar.
```

---

## C) roadmap.md — nota de reconciliação no M2

### Em "M2 — Grill", ACRESCENTAR ao fim da descrição:
```
Reconciliações a fazer no grill (além das 4 tensões):
- Vocabulário modos (relações/hierarquia/tabela) vs. vistas (grafo/árvore/tabela) — alinhar
  com o M1.
- Confirmar o GLOSSÁRIO como dono do vocabulário (CLAUDE.md já aponta para ele).
- **Linhas exactas do curador** (ex.: renderGraph) — a SArq-3 citou números de uma CÓPIA
  (modo web); conferir no `projetos-curador-v3.html` REAL antes de extrair. As linhas do M1
  (lidas no ficheiro real) têm precedência.
```

---

## D) Nota de proveniência (importante)

As referências de linha ao curador feitas na SArq-3 (renderGraph ~1275, etc.) saíram de uma
**cópia na Google Drive** (sessão em modo web), que pode diferir do ficheiro real. **Não são
verdade.** Onde o M1 (lido no filesystem real) divergir, **manda o M1**. Conferir sempre as
linhas no ficheiro real antes de qualquer extracção.
