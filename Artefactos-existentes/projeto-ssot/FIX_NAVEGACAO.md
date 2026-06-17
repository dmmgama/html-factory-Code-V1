# FIX: Navegação de Secções Bloqueadas

## PROBLEMA IDENTIFICADO

**Sintoma**: Todas as secções (2-8) bloqueadas dentro do projeto - menus não clicáveis

**Causa Raiz**: Event listeners de navegação executando **sem validação** de elementos DOM e **sem logs de debug**

---

## ALTERAÇÕES IMPLEMENTADAS

### 1. **index_v11.1.html** - Refactored Navigation Code

**Antes** (linha ~2074):
```javascript
// ==================== NAVEGAÇÃO ====================
document.querySelectorAll('.nav button').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.nav button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.getElementById(btn.dataset.target).classList.add('active');
  });
});
```

**Depois**:
```javascript
// ==================== NAVEGAÇÃO ====================
function initNavigation() {
  const navButtons = document.querySelectorAll('.nav button[data-target]');
  console.log(`[Nav] Inicializando ${navButtons.length} botões de navegação`);
  
  navButtons.forEach(btn => {
    const targetId = btn.dataset.target;
    if (!targetId) return;
    
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      console.log(`[Nav] Click em botão: ${targetId}`);
      
      // Remove active de todos os botões
      document.querySelectorAll('.nav button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      // Remove active de todas as secções
      document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
      
      // Mostra secção target
      const targetSection = document.getElementById(targetId);
      if (targetSection) {
        targetSection.classList.add('active');
        console.log(`[Nav] ✅ Secção ${targetId} activada`);
      } else {
        console.error(`[Nav] ❌ Secção ${targetId} não encontrada`);
      }
    });
  });
}

// Executa inicialização de navegação imediatamente (DOM já carregado)
initNavigation();
```

**Melhorias**:
- ✅ Encapsulado em função `initNavigation()` para reusabilidade
- ✅ Seletor mais específico: `.nav button[data-target]` (evita botões sem target)
- ✅ Validação: verifica se `targetId` existe antes de processar
- ✅ Validação: verifica se `targetSection` existe antes de addClass
- ✅ `e.preventDefault()` explícito para evitar comportamento default
- ✅ **Console logs** para debug:
  - Quantos botões foram encontrados
  - Qual botão foi clicado
  - Se secção foi ativada ou não encontrada

---

## VALIDAÇÃO

### Teste Isolado: `test-navigation.html`

Criado ficheiro de teste minimalista para validar lógica de navegação:
- ✅ 8 botões de menu
- ✅ 8 secções correspondentes
- ✅ Mesma estrutura HTML do index_v11.1.html
- ✅ Console logs para debug

**Como testar**:
```bash
# Servir ficheiro (ex: com Live Server VS Code)
# Ou abrir direto no browser:
# file:///C:/Users/JSJ/JSJ%20AI/projeto-ssot/test-navigation.html

# Abrir DevTools (F12) → Console
# Clicar em menus
# Verificar logs:
# [Test] Click em botão: sec2
# [Test] ✅ Secção sec2 activada
```

---

## CHECKLIST DE DEBUG (Executar no DevTools Console)

### 1. Verificar elementos DOM existem
```javascript
console.log('Botões nav:', document.querySelectorAll('.nav button[data-target]').length);
console.log('Secções:', document.querySelectorAll('.section').length);
console.log('Secção active:', document.querySelectorAll('.section.active').length);
```

**Esperado**:
```
Botões nav: 9  (8 secções + 1 relatórios)
Secções: 9
Secção active: 1  (apenas uma por vez)
```

---

### 2. Verificar event listeners anexados
```javascript
const btn = document.querySelector('.nav button[data-target="sec2"]');
console.log('Botão sec2 existe:', !!btn);
console.log('Dataset target:', btn?.dataset.target);
```

**Esperado**:
```
Botão sec2 existe: true
Dataset target: sec2
```

---

### 3. Testar manualmente navegação
```javascript
// Simular click programático
const btn = document.querySelector('.nav button[data-target="sec2"]');
btn.click();

// Verificar se secção mudou
const activeSec = document.querySelector('.section.active');
console.log('Secção ativa:', activeSec?.id);
```

**Esperado**:
```
[Nav] Click em botão: sec2
[Nav] ✅ Secção sec2 activada
Secção ativa: sec2
```

---

### 4. Verificar se há erros JS bloqueando
```javascript
// Console deve mostrar APENAS:
// [Nav] Inicializando 9 botões de navegação
// (sem SyntaxError, ReferenceError, TypeError)
```

---

## RED FLAGS (Se Ainda Não Funcionar)

### ❌ Se console mostrar 0 botões:
```
[Nav] Inicializando 0 botões de navegação
```
**Causa**: Script executou antes do DOM carregar  
**Fix**: Mover `initNavigation()` para dentro de `initEditor()` APÓS linha 4289

---

### ❌ Se clicar e nada acontecer (sem logs):
**Causa**: Event listener não anexado ou removido por outro código  
**Fix**: Verificar se há código que chama `.removeEventListener()` ou substitui `.innerHTML` do nav

---

### ❌ Se aparecer erro "Cannot read property 'classList' of null":
**Causa**: Secção com `id` não existe no HTML  
**Fix**: Verificar se todos os botões têm `data-target` correspondente a um `<section id="...">`

---

## PRÓXIMOS PASSOS

1. **Testar em browser** (abrir DevTools)
2. **Verificar console logs** aparecem
3. **Clicar em menus** e observar feedback
4. **Se ainda bloquear**: Executar checklist de debug acima
5. **Reportar**:
   - Screenshot console
   - Output dos 4 testes de debug
   - Mensagens de erro (se houver)

---

## COMMIT

```bash
git add index_v11.1.html test-navigation.html
git commit -m "fix: Restaurar navegação menus secções (encapsulado + logs debug)

- Refactor: initNavigation() com validações robustas
- Add: Console logs para debug [Nav]
- Add: test-navigation.html (teste isolado)
- Fix: Seletor específico .nav button[data-target]
- Fix: Validação targetSection antes de classList.add

Resolve: Secções 2-8 bloqueadas dentro de projeto"
```

---

## ROLLBACK (Se Fix Não Funcionar)

```bash
# Ver histórico
git log --oneline -10

# Identificar commit antes do bug
git checkout <commit-hash> -- index_v11.1.html

# Ou reset completo (CUIDADO: perde alterações não commitadas)
git reset --hard <commit-hash>
```
