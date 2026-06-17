# Prompt: gerar MD no formato do LifeMap

Prompt robusta para dar a qualquer LLM (Claude, GPT, Gemini, Llama, …) para que
produza um Markdown que a app **importa sem fricção**. Cobre o formato canónico
(ver `MANUAL.md` §5) e bloqueia os erros que os LLMs costumam cometer.

**Como usar:** cola o bloco abaixo no LLM; na última secção `TAREFA` descreve
o que queres mapear (tema, áreas-raiz, profundidade, restrições). O LLM devolve
o MD pronto para colar em **Import MD** ou **Editar MD** de qualquer tab.

---

## Prompt (copy/paste)

````text
Vais gerar um mapa hierárquico em Markdown no formato EXATO definido abaixo, para
ser importado por uma aplicação. A resposta deve ser APENAS o ficheiro MD —
nada antes, nada depois, sem ``` à volta, sem explicações.

═══ FORMATO OBRIGATÓRIO ═══

A resposta tem exatamente esta forma:

  # Versao <VERSÃO>
  # Estrutura

  - <nó raiz 1>
    - <filho>
      - <neto>
  - <nó raiz 2>
    ...

Regras (todas obrigatórias):

1. As duas primeiras linhas são headings literais:
     • Linha 1: "# Versao <VERSÃO>"   (substitui <VERSÃO> por uma etiqueta curta:
       ex. "v1", "rascunho-2025-01", "proposta")
     • Linha 2: "# Estrutura"
2. Linha 3 em branco. A partir da linha 4 é tudo lista de bullets.
3. Cada nó é UMA linha que começa por "- " (hífen + espaço).
4. Indentação: EXATAMENTE 2 espaços por nível.
     • Filho = pai + 2 espaços.
     • Irmãos = mesmíssima indentação.
     • NUNCA usar tabs. NUNCA misturar 2 e 4 espaços para o mesmo nível.
5. NÃO usar numeração de secção como prefixo dos nomes ("1.", "1.1", "2.3",
   "2025.08") — a app remove-a. Se quiseres números, escreve-os sem ponto:
   "1 Fte", "4 Taste", "2025 Plano" são permitidos.
6. Emojis dentro dos nomes são permitidos e recomendados nos nós de nível 1
   para destacar categorias (ex.: "💚 SAÚDE", "🏠 PATRIMÓNIO", "💼 WORK").
7. Outros caracteres válidos dentro dos nomes: acentos, espaços, "/", ":",
   "&", parêntesis, hífen, ponto, dígitos. Ex.: "R/C Esq", "4 Taste",
   "Gamma.AI", "Festas & Eventos", "MGB GT".
8. A ordem dos irmãos é preservada — escreve-os pela ordem que queres ver.
9. PROIBIDO: outros headings (##, ###), listas numeradas (1. , 2. ),
   listas com "*" ou "•", blocos de código, citações ">", linhas em branco
   no meio da lista, comentários, texto narrativo, ou nomes duplicados
   entre irmãos do mesmo pai.

═══ EXEMPLO VÁLIDO ═══

# Versao v1
# Estrutura

- 💚 SAÚDE
  - Saúde Clínica
  - Saúde Mental
  - Bem-Estar
    - Relaxamento
    - Cuidado Pessoal
- 🏠 PATRIMÓNIO
  - Imóveis
    - Tv. dos Moinhos
      - 1 Fte
        - Cadastro
        - Manutenção
      - 1 Dto
        - Cadastro
        - Manutenção
    - Calçada da Boa Hora
      - R/C Esq
        - Casa
        - Jardim
  - Automóvel
    - Fiat
      - Manutenção
      - Seguro

═══ ERROS COMUNS A EVITAR ═══

✗ Não fazer:    # Mapa de áreas         ← heading que não seja "# Versao …" / "# Estrutura"
✗ Não fazer:    ```markdown … ```       ← envolver em bloco de código
✗ Não fazer:    1. SAÚDE                ← lista numerada, ou prefixo "1." num nome
✗ Não fazer:    \t- Imóveis             ← tabs em vez de espaços
✗ Não fazer:    "Aqui está o mapa:"     ← texto narrativo antes ou depois
✗ Não fazer:    irmãos com indentação diferente (uns 2 espaços, outros 4)

═══ AUTO-VERIFICAÇÃO (antes de responder) ═══

Antes de finalizares, confirma:
□ As duas primeiras linhas são "# Versao …" e "# Estrutura".
□ Há exatamente uma linha em branco depois dos headings; nenhuma no meio da lista.
□ Cada filho tem exatamente +2 espaços face ao pai.
□ Nenhuma linha tem tabs.
□ Nenhum nome começa por "N." ou "N.N " (numeração de secção).
□ Não há nada além do MD na resposta.

═══ TAREFA ═══

<aqui descreves o que queres mapear: tema, áreas-raiz, profundidade
desejada, restrições, contexto. Quanto mais específico, melhor.>
````

---

## Notas

- **Modelos pequenos** podem precisar de reforço final: "**não escrevas
  absolutamente nada além do MD, sem comentários, sem fences**".
- Se o LLM envolver a resposta em ` ``` `, retira os fences antes de colar — a
  app ignora os headings `#` mas **não** ignora fences de código.
- **Reaproveita:** muda só `<VERSÃO>` e `TAREFA` para novos mapas.
- **Casos validados na prática:** estrutura do Life Map (v4 ~140 nós), iCloud
  Mail (~280 nós com viagens detalhadas), Vault Obsidian (54 nós, 4 raízes).

## Histórico
- v1 (S1, 2026-06-02) — primeira versão arquivada (entregue como rascunho na
  sessão de trabalho anterior; formalizada num ficheiro estável).
