# Documento 0 — Instalar a Caixa Inspetora (passo-a-passo do David)
## O que fazer e o que dar a um agente

> **Para quem é:** para ti, David. Este é o **primeiro** documento a ler quando queres **pôr a caixa
> num HTML novo**. Diz-te exatamente o que clicar, o que escrever ao agente, e como confirmar que
> ficou bem. Não precisas de saber programar.
>
> Ordem dos documentos: **0 (instalar, este)** → 2 (usar) → 1 e 3 (técnicos, para o agente/LLM).

---

## Antes de começares — o que precisas

- O **ficheiro HTML** onde queres a caixa (ex.: `a-minha-app.html`).
- Um **agente de código** com acesso a esse ficheiro. Qualquer um destes serve:
  - **Claude Code** (terminal, app de desktop, ou extensão no VS Code) — recomendado.
  - **Cursor**, **Windsurf**, ou outro assistente que consiga **ler e editar ficheiros**.
- Os ficheiros deste *toolkit* (já os tens em `OrganizeAI\inspector-toolkit\`).

> ⚠️ **Importante:** tem de ser um agente que **edite o ficheiro diretamente**. Um chat normal
> (ChatGPT/Claude no browser) só te devolve texto e obriga-te a colar à mão — dá para emergências,
> mas é mais frágil com ficheiros grandes. Prefere um agente com acesso a ficheiros.

---

## Receita rápida (a versão de 20 segundos)

1. Abre o agente **na pasta onde está o teu HTML**.
2. Cola-lhe esta frase (troca o nome do ficheiro):

   > *"Lê o documento `inspector-toolkit\1-AGENTE-implementar-caixa-inspetora.md` e segue-o para
   > instalar a Caixa Inspetora no ficheiro `a-minha-app.html`. Faz primeiro um checkpoint, descobre o
   > STATE/funções/viewers, preenche os 4 pontos CONFIG, e no fim diz-me o que ligaste e o que ficou
   > limitado."*

3. Deixa-o trabalhar. No fim, **abre o HTML no browser** e confirma (checklist mais abaixo).

É isto. As secções seguintes explicam cada passo com calma e o que fazer se algo correr mal.

---

## Passo-a-passo detalhado

### Passo 1 — Faz uma cópia de segurança (rede de segurança)
Mesmo que peças ao agente para fazer checkpoint, faz tu também: copia o teu `a-minha-app.html` para
um sítio seguro (ou duplica-o com outro nome, ex.: `a-minha-app_ORIGINAL.html`). Assim, aconteça o que
acontecer, tens sempre o original.

### Passo 2 — Garante que o agente "vê" os ficheiros certos
O agente precisa de aceder a **dois** sítios:
- ao **teu HTML** (`a-minha-app.html`);
- ao **Documento 1** do toolkit (`inspector-toolkit\1-AGENTE-implementar-caixa-inspetora.md`).

A maneira mais simples: abre o agente **na pasta-mãe** que contém os dois (ou copia o `1-AGENTE...md`
para ao pé do teu HTML). Se o agente não conseguir abrir o Documento 1, **cola o conteúdo dele** na
conversa.

### Passo 3 — Dá-lhe a ordem (copia/cola e adapta)
Usa este texto. **Só tens de mudar o nome do ficheiro** a negrito:

```
Quero tornar este HTML num "Projeto Observável" instalando a Caixa Inspetora.

Ficheiro-alvo: a-minha-app.html      ← MUDA para o teu nome

Instruções:
1. Lê o documento "inspector-toolkit/1-AGENTE-implementar-caixa-inspetora.md" e segue-o à risca.
2. Faz primeiro um checkpoint (cópia datada) do ficheiro-alvo.
3. Faz a "descoberta" das 4 coisas (o STATE/fonte de dados, as funções do engine, os viewers/abas,
   e os elementos interativos). Se não conseguires identificar alguma com confiança, PERGUNTA-ME
   em vez de inventar.
4. Cola os blocos CSS + HTML + JS e PREENCHE os 4 pontos marcados com CONFIG.
5. NÃO alteres nenhuma linha do código original da app (modo não-invasivo).
6. No fim, verifica que o ficheiro ainda abre e diz-me um resumo: o que ligaste em cada vista
   (Data/Logic/Layout/Pick) e o que ficou limitado e porquê.
```

### Passo 4 — Responde se ele perguntar
Um bom agente pode perguntar-te coisas como *"qual é a variável de estado?"* ou *"quais são as abas?"*.
Não faz mal não saberes ao certo — diz o que souberes ("acho que os dados estão numa variável chamada
STATE", "as abas no topo são Tabela e Gráfico"). Se não fizeres ideia, diz **"descobre tu, e mostra-me
o que encontraste antes de avançar"**.

### Passo 5 — Testa (sempre tu, no browser)
Quando o agente disser que terminou, **abre o `a-minha-app.html` no browser** (duplo-clique) e corre a
checklist da secção seguinte. **Não confies só no "está feito"** — confirma com os teus olhos.

### Passo 6 — Se estiver bom, guarda a versão
Renomeia ou guarda como a tua versão "Observável" (ex.: `a-minha-app-O.html`, à semelhança do
`projetos-curador-v3O.html`). Mantém o original intacto.

---

## ✅ Checklist de aceitação (faz no browser, ~1 minuto)

- [ ] Aparece o **botão redondo 🔬** no canto inferior direito.
- [ ] Carregar nele (ou `Ctrl`+`Shift`+`I`) **abre/fecha** o painel à direita.
- [ ] A aba **Data** mostra **JSON com dados reais** (não fica em "—").
- [ ] A aba **Logic** começa a **listar funções** quando usas a app.
- [ ] A aba **Layout** mostra **qual a vista ativa** e conta renders.
- [ ] **🎯 Inspecionar** → aparece **moldura amarela** + faixa no topo; clicar num elemento mostra um
      relatório e **não dispara** a ação; **`Esc`** sai.
- [ ] **A app continua a funcionar normalmente** com o Inspector fechado.

Se **tudo** estiver ✔ → instalação concluída. Se algo falhar → secção "Problemas" abaixo.

---

## 🛠️ Problemas comuns (e o que dizer ao agente)

| Sintoma | Provável causa | Diz ao agente |
|---|---|---|
| Não aparece o botão 🔬 | O bloco HTML/CSS não foi colado, ou ficou no sítio errado | *"O botão 🔬 não aparece. Confirma que colaste o CSS antes de `</style>` e o HTML logo a seguir ao `<body>`."* |
| Painel abre mas **Data** diz só "—" | O `getState()` (CONFIG 1) não aponta para os dados certos | *"A vista Data está vazia. Descobre qual é a variável de estado da app e corrige o CONFIG 1 e 2."* |
| **Logic** nunca regista nada | As funções não estão na lista, ou não são globais (CONFIG 3) | *"A vista Logic não regista chamadas. Verifica o CONFIG 3 — as funções estão em window? Se forem internas, explica-me a limitação."* |
| **Layout** mostra a vista errada | O `activeViewKey()` (CONFIG 4) não deteta a aba ativa | *"A vista Layout não acerta na aba ativa. Ajusta o CONFIG 4 ao modo como esta app marca a aba ativa."* |
| Cliquei e **a app não faz nada** | O **modo Pick está ligado** (é de propósito) | Não é erro: carrega `Esc` ou no botão 🎯 para sair do modo inspecionar. |
| A app **deixou de funcionar** | O agente mexeu no código original | *"A app partiu. Repõe a partir do checkpoint e reinstala em modo NÃO-invasivo, sem tocar no código original."* |

> 💡 Truque universal: se algo correr mal, diz simplesmente **"repõe a partir do checkpoint e
> tenta outra vez, com mais cuidado na descoberta"**. Por isso o checkpoint do Passo 1 é importante.

---

## ❓ Perguntas que podes ter

**Tenho de instalar alguma coisa no computador?**
Não. A caixa é só código dentro do próprio HTML. Não precisa de internet, servidor, nem programas.

**Posso pôr isto em vários HTML?**
Sim — repete esta receita para cada um. É esse o objetivo do toolkit.

**E se o meu HTML for muito diferente (feito noutra tecnologia)?**
O Documento 1 tem uma secção de **adaptação** (React/Vue/sem dados globais). O agente trata disso; se
alguma vista não der para ligar com fidelidade, ele instala as outras e avisa-te qual ficou limitada.

**Quanto tempo demora?**
Numa app simples, minutos. Numa grande/complexa, o agente leva mais tempo na "descoberta" — é normal.

**Preciso de saber o que é STATE, engine, viewer?**
Não para instalar. Mas se quiseres perceber, o **Documento 2** explica em linguagem simples, e o
**Documento 3** é a referência técnica.

---

## Resumo numa frase
Abre um agente de código na pasta do teu HTML, manda-o **seguir o Documento 1 para instalar a caixa
no teu ficheiro** (com checkpoint e modo não-invasivo), e no fim **confirma tu no browser** com a
checklist. Se falhar, "repõe do checkpoint e tenta de novo".
