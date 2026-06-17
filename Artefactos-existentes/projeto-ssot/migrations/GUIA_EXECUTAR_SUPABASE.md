# 🔧 GUIA: Executar Migration no Supabase

## ⚠️ IMPORTANTE
Copie **APENAS** o código SQL abaixo. **NÃO** copie comentários JavaScript (//).

---

## 📋 Passo-a-Passo

### 1️⃣ Abrir Supabase SQL Editor
1. Ir para [supabase.com](https://supabase.com)
2. Login com sua conta
3. Selecionar projeto: **SSOT-JSJ** (vkuqmnoepiddpidmdale)
4. Menu lateral → **SQL Editor**
5. Clicar **"New query"**

---

### 2️⃣ Copiar Código SQL

**COPIAR EXATAMENTE ESTAS 3 LINHAS:**

```sql
ALTER TABLE floors 
ADD COLUMN IF NOT EXISTS actions_data JSONB DEFAULT '{}'::jsonb;

COMMENT ON COLUMN floors.actions_data IS 'Dados zonamento gráfico: layers, zones, rcp, etc (Secção 7)';
```

---

### 3️⃣ Colar no SQL Editor
- Colar no campo de texto grande
- **NÃO** adicionar nada antes ou depois
- **NÃO** incluir comentários com `//`

---

### 4️⃣ Executar
- Clicar botão **"Run"** (ou Ctrl+Enter)
- Aguardar mensagem: **"Success. No rows returned"**

---

### 5️⃣ Validar (Opcional)

Executar esta query para confirmar:

```sql
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'floors' 
  AND column_name = 'actions_data';
```

**Resultado esperado:**
| column_name | data_type |
|------------|-----------|
| actions_data | jsonb |

---

## ✅ Confirmação Final

Se vir a mensagem **"Success"** e a validação retornar 1 linha, está completo!

---

## 🚨 Se Houver Erro

**Erro comum:** "syntax error at or near '//'", "syntax error at or near 'Blocos'"

**Causa:** Copiou texto JavaScript ou comentários inválidos

**Solução:** 
1. Limpar completamente o SQL Editor (Ctrl+A → Delete)
2. Copiar **APENAS** as 3 linhas SQL acima
3. Colar e executar novamente

---

## 📞 Suporte

Se persistir erro, copiar mensagem **COMPLETA** de erro e partilhar.
