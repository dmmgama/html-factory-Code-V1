# Arqueologia de Alterações — snapshots congelados

Esta pasta guarda **cópias físicas e CONGELADAS** do `.html` da app, uma por **marco aceite**.
Existe para permitir **abrir duas versões ao mesmo tempo no browser e comparar a funcionar**, sem
ter de fazer `git checkout`.

## Regra de ouro (NÃO violar)
- **Os ficheiros aqui dentro são READ-ONLY.** Nunca se editam. São snapshots mortos.
- **O único ficheiro VIVO é `../MapLab.html`** (na raiz do projeto). É lá que se faz todo o trabalho.
- Um snapshot novo é congelado **só quando o utilizador ACEITA um marco** (não a cada micro-mudança).
  Entre marcos, o histórico fica no git.

## Convenção de nomes
`NN-Titulo.html` — `NN` = ordem global (ver `../Planodeacao-app.md` / `../Planodeacao-server.md`).

## Snapshots existentes
| Ficheiro | O que é | Origem |
|---|---|---|
| `00-VersaoOriginal-lifemap_lab.html` | **Versão Original intacta.** App v12 com 4 mapas HARDCODED (lifemap, icloud, notion, obsidian). Antes de qualquer "app genérica". | commit `a733819` (S1) |
| `01-AppGenerica-nosave.html` | App genérica (projetos+árvores em runtime), **sem ícones**, sem persistência. | commit `71a132d` "versao alterada 1" |
| `02-AppGenerica-icones.html` | App genérica **+ ícones Notion** (883 embebidos, picker, cor por ramo). | trabalho não commitado (ex-`lifemap_lab_v2.html`) |

> Nota: `00` é a **fonte da verdade do "antes"**. Qualquer auditoria sobre "o que mudou desde o
> início" compara contra `00`.
