# Documento 2 — Manual do David
## Como usar a "Caixa Inspetora" nos teus HTML

> **Para quem é:** para ti, David. Linguagem simples, sem código. Explica o que a caixa faz e
> como a usares no dia-a-dia para **veres se a tua app está a fazer o que devia**.

---

## O que é, em duas frases

A **Caixa Inspetora** é um painel que aparece do lado direito do teu HTML e que te deixa **espreitar
por baixo do capô** da app enquanto a usas — sem precisares de saber programar nem de abrir ferramentas
técnicas do browser. Serve para **confirmares, com os teus próprios olhos, que a arquitetura que
desenhámos está a ser respeitada**: os dados certos, as funções certas, no sítio certo.

---

## Como abrir e fechar

- Carrega no botão redondo **🔬** no **canto inferior direito** do ecrã.
- Ou usa o atalho de teclado **`Ctrl` + `Shift` + `I`**.
- Para fechar: o mesmo botão, o atalho, ou o **×** no topo do painel.

Quando o painel está aberto, o conteúdo da app encolhe um pouco para a esquerda para não ficar tapado.

---

## As 4 abas (no topo do painel)

### 📦 1. DATA — "a minha fonte da verdade"
Mostra-te o **JSON** com os dados reais da app naquele momento. É a "verdade" que a app usa para
desenhar tudo o resto.

- Há um **menu** no topo para escolheres que parte queres ver (ex.: só os projetos, só as ligações,
  ou o estado completo).
- O botão **↻** atualiza (refresh) caso queiras forçar a leitura mais recente.
- Por baixo, um resumo de **estatísticas** (quantos projetos, quantas ligações, etc.).

**Para que serve:** confirmar que aquilo que vês no ecrã corresponde aos dados que estão realmente
guardados. Se editas um projeto e o JSON não muda, há um problema.

---

### ⚙️ 2. LOGIC — "que funções correram"
Mostra, em **tempo real**, a lista das **funções do motor (engine)** que foram chamadas na tua última
interação. A mais recente fica no topo. Se a mesma função for chamada várias vezes seguidas, aparece
um contador (ex.: **×3**).

- Botão **✕ limpar** para começares uma observação limpa antes de testar uma ação específica.

**Para que serve:** validar a lógica. Exemplo: clicas em "Guardar versão" → devias ver as funções de
gravação a aparecer. Se clicas e **não aparece nada**, ou aparece a função **errada**, descobriste um
desvio à arquitetura.

> 💡 **Dica de validação:** limpa o log (✕), faz **uma** ação, e olha exatamente para o que apareceu.
> Assim isolas o que cada botão realmente dispara.

---

### 🖼️ 3. LAYOUT — "quem está a desenhar o ecrã"
Diz-te qual **viewer** (vista/canvas) está ativo neste momento e qual a função que o desenha. Também
lista **todos** os viewers e quantas vezes cada um foi re-desenhado nesta sessão.

**Para que serve:** perceber qual parte da app é responsável pelo que estás a ver, e detetar
**re-renders a mais** (se um número dispara sem razão, algo está a redesenhar de forma ineficiente).

---

### 🎯 4. PICK — "aponta e pergunta" (o mais poderoso)
Este é o modo **inspecionar**, parecido com o "inspecionar elemento" do browser, mas em linguagem da
**tua arquitetura**.

**Como usar:**
1. Carrega no botão **🎯 Inspecionar** (no topo do painel).
2. O ecrã ganha uma **moldura amarela** e aparece uma faixa **"MODO INSPECIONAR ATIVO"** no topo.
   Isto avisa-te que a app está "congelada" para inspeção.
3. **Passa o rato** por cima de qualquer elemento (separador, botão, filtro, caixa, cartão…) — ele
   fica contornado a tracejado para mostrar que é clicável.
4. **Clica** nesse elemento. ⚠️ A ação normal **NÃO acontece** (não guarda, não muda de aba, etc.).
   Em vez disso, abre-se um relatório com 3 cartões:
   - 📦 **Data** — que dados é que aquele elemento lê ou escreve.
   - ⚙️ **Logic** — que função(ões) ele normalmente chama.
   - 🖼️ **Layout** — que parte do ecrã (canvas/vista) ele afeta.
5. Para **sair** do modo: carrega outra vez em **🎯 Inspecionar** ou na tecla **`Esc`**.

**Para que serve:** és tu a apontar. "O que é este botão? E esta caixa? E este filtro?" — e a app
responde-te o papel de cada peça na arquitetura, sem teres de adivinhar.

---

## O teu fluxo de validação recomendado (passo-a-passo)

Queres confirmar que "a arquitetura desenhada está a ser seguida"? Faz isto:

1. **Abre o Inspector** (🔬).
2. **Pergunta o que devia acontecer** — vai a **🎯 Pick**, clica no elemento que vais testar (ex.: o
   separador "Ligações"). Lê o que o cartão **Logic** diz que ele *deveria* chamar (ex.: `renderGraph`).
3. **Sai do Pick** (`Esc`) e vai à aba **Logic**; carrega em **✕ limpar**.
4. **Faz a ação a sério** — clica mesmo no separador "Ligações".
5. **Compara:** o que apareceu na aba Logic é igual ao que o Pick tinha previsto?
   - ✅ **Igual** → a arquitetura está a ser respeitada nesse ponto.
   - ❌ **Diferente / vazio** → encontraste um desvio. Anota e pede ao agente para investigar.
6. **Confirma os dados** na aba **Data** — a ação mexeu no JSON certo?

---

## Perguntas frequentes

**A caixa altera a minha app ou os meus dados?**
Não. É só de leitura/observação. A única exceção controlada é o modo 🎯 Pick, que *de propósito*
bloqueia a ação do elemento enquanto o inspecionas — mas isso é temporário e sai com `Esc`.

**Funciona offline / num ficheiro local?**
Sim. Está tudo dentro do próprio HTML; não precisa de internet nem de servidor.

**Posso usar isto em qualquer HTML meu?**
Sim — é esse o objetivo do *toolkit*. Dás o **Documento 1** a um agente (Claude Code, etc.) e ele
implementa a caixa nesse HTML. Vê o Documento 1 para os detalhes.

**O modo Pick diz que um botão chama a função X — isso é a verdade absoluta?**
Não necessariamente. O Pick mostra a **intenção documentada** (o que *devia* fazer). A aba **Logic**
mostra o que *realmente* correu. **A validação real é comparar os dois** (passo 5 acima). Se divergem,
ou o código mudou e os metadados ficaram desatualizados, ou há mesmo um bug de arquitetura — em ambos
os casos vale a pena olhar.

**Aparece "Sem metadados / inferido" num elemento. É mau?**
Só quer dizer que esse elemento específico ainda não tem uma descrição escrita à mão; a caixa faz o
melhor palpite a partir do tipo/etiqueta. Se for um elemento importante, pede ao agente para lhe
adicionar metadados próprios.

---

## Onde está isto guardado

- A versão de referência é o teu **`projetos-curador-v3O.html`** (o "Projeto Observável").
- Os 3 documentos do *toolkit* (incluindo este) estão em **`OrganizeAI\inspector-toolkit\`**.
- Há também versões `.html` destes manuais (na subpasta `html\`) para abrires no browser.
