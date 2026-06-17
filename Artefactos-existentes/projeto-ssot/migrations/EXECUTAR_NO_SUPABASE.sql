-- =====================================================
-- VALIDAÇÃO SCHEMA: floors (Supabase SQL Editor)
-- Data: 2026-02-16
-- Descrição: Queries para validar schema completo
-- =====================================================

-- =====================================================
-- QUERY 1: Listar TODAS as colunas de floors
-- =====================================================
SELECT 
  column_name, 
  data_type, 
  is_nullable,
  column_default
FROM information_schema.columns 
WHERE table_name = 'floors'
ORDER BY ordinal_position;

-- ESPERADO:
-- id                UUID         NOT NULL
-- block_id          UUID         NOT NULL
-- project_id        UUID         NOT NULL
-- name              TEXT         NOT NULL
-- cota              NUMERIC      
-- tipologia         TEXT         
-- cotas_tosco       JSONB        DEFAULT '[]'
-- image_path        TEXT         
-- actions_data      JSONB        DEFAULT '{}'  ← CRÍTICO
-- created_at        TIMESTAMPTZ  
-- updated_at        TIMESTAMPTZ  


-- =====================================================
-- QUERY 2: Verificar Foreign Keys
-- =====================================================
SELECT
  tc.constraint_name,
  kcu.column_name,
  ccu.table_name AS references_table,
  ccu.column_name AS references_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu 
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu 
  ON tc.constraint_name = ccu.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY' 
  AND tc.table_name = 'floors';

-- ESPERADO:
-- floors.block_id   → blocks.id
-- floors.project_id → projects.id


-- =====================================================
-- QUERY 3: Validar Dados Sample (3 pisos)
-- =====================================================
SELECT 
  f.id,
  f.name,
  f.cota,
  f.tipologia,
  f.cotas_tosco,
  f.image_path,
  f.actions_data,  -- ← CRÍTICO: deve existir
  b.name AS block_name,
  p.nome_projeto
FROM floors f
JOIN blocks b ON b.id = f.block_id
JOIN projects p ON p.id = f.project_id
LIMIT 3;

-- VERIFICAR:
-- - actions_data existe? (deve ser {} ou null, NÃO "column does not exist")
-- - cotas_tosco populado? (deve ter array: [0.0] ou [0.0, 0.15])
-- - image_path tem valores ou null?


-- =====================================================
-- QUERY 4: Contar pisos por tipologia
-- =====================================================
SELECT 
  tipologia,
  COUNT(*) as total,
  COUNT(actions_data) as com_actions_data,
  COUNT(image_path) as com_imagem
FROM floors
GROUP BY tipologia;


-- =====================================================
-- QUERY 5: Verificar tabela project_files (obsoleta?)
-- =====================================================
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'project_files'
ORDER BY ordinal_position;

-- SE EXISTIR E NÃO É USADA → pode ser removida:
-- DROP TABLE IF EXISTS project_files CASCADE;


-- =====================================================
-- QUERY 6: Validar actions_data estrutura
-- =====================================================
SELECT 
  f.id,
  f.name,
  jsonb_typeof(f.actions_data) as tipo,
  f.actions_data->'layers' as layers,
  jsonb_object_keys(f.actions_data) as chaves
FROM floors f
WHERE f.actions_data IS NOT NULL 
  AND f.actions_data != '{}'::jsonb
LIMIT 5;

-- ESPERADO (se houver dados):
-- tipo: 'object'
-- layers: {...}


-- =====================================================
-- CHECKLIST VALIDAÇÃO:
-- =====================================================
-- [ ] Query 1: actions_data e cotas_tosco existem (JSONB)
-- [ ] Query 2: Foreign keys corretas
-- [ ] Query 3: Dados sample sem erros
-- [ ] Query 4: Estatísticas fazem sentido
-- [ ] Query 5: project_files não usada → remover
-- [ ] Query 6: actions_data tem estrutura correta

-- =====================================================
-- SE HOUVER PROBLEMAS:
-- =====================================================

-- FALTA actions_data:
-- ALTER TABLE floors ADD COLUMN actions_data JSONB DEFAULT '{}'::jsonb;

-- FALTA cotas_tosco:
-- ALTER TABLE floors ADD COLUMN cotas_tosco JSONB DEFAULT '[]'::jsonb;
-- UPDATE floors SET cotas_tosco = jsonb_build_array(cota) WHERE cotas_tosco = '[]'::jsonb;

-- REMOVER project_files (se não usada):
-- DROP TABLE IF EXISTS project_files CASCADE;
