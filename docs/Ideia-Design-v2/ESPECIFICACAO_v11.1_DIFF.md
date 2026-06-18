# ESPECIFICACAO.md v11.1 - DIFF (Alterações vs v11.0)

## MUDANÇAS PRINCIPAIS

### 1.1 Arquitetura (ATUALIZAR)
Adicionar linha após "Auth":
- **Storage**: Firebase Storage (blob assets: imagens, PDFs, DXF)

### 1.2 Componentes Principais (ATUALIZAR)
```
firebase-data.js (~700 linhas)  # Era ~500
├─ Firestore CRUD operations
├─ Map/Array serialization
├─ Nested arrays sanitization
├─ Real-time subscriptions
└─ 🆕 Firebase Storage Layer (generic upload/download/delete)
```

Adicionar novo ficheiro:
```
migrate-v11.0-to-v11.1.html (~300 linhas)
└─ Migration script (Base64 → Storage)
```

### 1.3 Fluxo de Dados (ADICIONAR APÓS DIAGRAMA EXISTENTE)
```
🆕 Asset Storage Flow (v11.1):
User Upload (Input file) → uploadFloorImage()
                              ↓
                    Firebase Storage (blob)
                              ↓
                    getDownloadURL() + TTL 7d
                              ↓
            Firestore (imageURL + cached downloadURL)
                              ↓
          Lazy Load (on-demand) → FloorViewer.loadImage()
                              ↓
                    Cache client-side (URL.createObjectObject)
```

### 1.4 Fluxo Multi-Projeto (ATUALIZAR SCHEMA)
**Firestore Schema** (v11.1):
```
projects (collection)
└─ <projectId> (document)
    ├─ owner: "user@jsj.pt"
    ├─ id_jsj: "2026-001"
    ├─ nome_projeto: "Edifício A"
    ├─ floors: [
    │   {
    │     id, name, cota, area,
    │     🆕 imageURL: "gs://bucket/projects/{id}/floors/{id}/image.png",
    │     🆕 imageDownloadURL: "https://...",  # Cached TTL 7d
    │     🆕 imageURLExpiry: timestamp,
    │     ❌ imageData (REMOVIDO - era Base64),
    │     zones: [...],
    │     actionsData: {...}
    │   }
    │ ]
    ├─ geoHorizons: [...]
    └─ updatedAt: timestamp

🆕 Firebase Storage (paralelo):
gs://ssot-jsj.appspot.com/
└─ projects/{projectId}/
    └─ floors/{floorId}/
        └─ image.png (blob ~500KB)
```

### 2.1 Estrutura Global projectData (ATUALIZAR)
Linha 114 - SUBSTITUIR:
```javascript
// ❌ v11.0 (ANTIGO)
imageData: "",  // Base64 string (PNG/JPG) - planta do piso

// ✅ v11.1 (NOVO)
imageURL: "",              // Storage path: gs://bucket/projects/{id}/floors/{id}/image.png
imageDownloadURL: "",      // Cached download URL (TTL 7 dias)
imageURLExpiry: 0,         // Timestamp expiration
imageLoaded: false,        // 🆕 Client-side cache flag (não persiste)
```

### NOVA SECÇÃO 5.5 (INSERIR APÓS 5.4)

## 5.5 FIREBASE STORAGE LAYER (v11.1+)

### 5.5.1 Arquitetura
**Pattern**: Firestore-Centric (metadata) + Storage (blobs)
- Firestore: Queryable metadata (paths, URLs, expiry)
- Storage: Binary data (images, PDFs, DXF)
- Security: Parallel rules (Firestore + Storage)

**Motivação**:
- Firestore doc limit: 1MB
- v11.0: 10 floors × 500KB Base64 = 5MB → REJECT
- v11.1: 10 floors × 50B URLs = 500B → OK

### 5.5.2 Storage Paths (Genérico)
```
gs://ssot-jsj.appspot.com/
└─ projects/{projectId}/
    ├─ floors/{floorId}/image.png           # v11.1 (implementado)
    ├─ geotecnia/{docId}.pdf                # v11.2+ (futuro)
    ├─ plantas/{dwgId}.dxf                  # v11.2+ (futuro)
    └─ reports/{reportId}.docx              # v13.0+ (futuro)
```

**Design Genérico**: Funções agnósticas de tipo (preparado para qualquer asset).

### 5.5.3 API Storage (firebase-data.js)

#### Generic Functions
```javascript
/**
 * Upload asset to Firebase Storage
 * @param {string} projectId - Project UUID
 * @param {string} path - Relative path (e.g., "floors/123/image.png")
 * @param {File} file - Blob to upload
 * @param {Object} metadata - Optional metadata (contentType, etc.)
 * @returns {Object} { storageURL, downloadURL, expiry }
 */
async function uploadAsset(projectId, path, file, metadata = {}) {
  const fullPath = `projects/${projectId}/${path}`;
  const ref = storage.ref(fullPath);
  
  await ref.put(file, metadata);
  
  const downloadURL = await ref.getDownloadURL();
  const expiry = Date.now() + (7 * 24 * 60 * 60 * 1000); // 7 dias
  
  return {
    storageURL: `gs://${bucket}/${fullPath}`,
    downloadURL,
    expiry
  };
}

/**
 * Get asset download URL (lazy load com cache TTL)
 * @param {string} storageURL - gs:// path
 * @param {string} cachedURL - Cached download URL
 * @param {number} expiry - Cached URL expiry timestamp
 * @returns {string} Valid download URL
 */
async function getAssetURL(storageURL, cachedURL, expiry) {
  const now = Date.now();
  
  // Se cached URL válido → return
  if (cachedURL && expiry > now) {
    return cachedURL;
  }
  
  // Regenerar URL
  const ref = storage.refFromURL(storageURL);
  return await ref.getDownloadURL();
}

/**
 * Delete asset from Storage
 * @param {string} storageURL - gs:// path
 */
async function deleteAsset(storageURL) {
  const ref = storage.refFromURL(storageURL);
  await ref.delete();
}
```

#### Floor-Specific Wrappers (v11.1)
```javascript
/**
 * Upload floor image
 * @param {string} projectId
 * @param {number} floorId - Timestamp ID
 * @param {File} file - PNG/JPG file
 * @returns {Object} { imageURL, imageDownloadURL, imageURLExpiry }
 */
async function uploadFloorImage(projectId, floorId, file) {
  const path = `floors/${floorId}/image.png`;
  const result = await uploadAsset(projectId, path, file, {
    contentType: file.type,
    customMetadata: { floorId: floorId.toString() }
  });
  
  return {
    imageURL: result.storageURL,
    imageDownloadURL: result.downloadURL,
    imageURLExpiry: result.expiry
  };
}

/**
 * Get floor image URL (com cache TTL)
 * @param {Object} floor - Floor object
 * @returns {string} Valid download URL
 */
async function getFloorImageURL(floor) {
  if (!floor.imageURL) return null;
  
  const url = await getAssetURL(
    floor.imageURL,
    floor.imageDownloadURL,
    floor.imageURLExpiry
  );
  
  // Update Firestore cache se regenerado
  if (url !== floor.imageDownloadURL) {
    const projectId = new URLSearchParams(location.search).get('project');
    const floorIndex = projectData.floors.findIndex(f => f.id === floor.id);
    
    await db.collection('projects').doc(projectId).update({
      [`floors.${floorIndex}.imageDownloadURL`]: url,
      [`floors.${floorIndex}.imageURLExpiry`]: Date.now() + (7 * 24 * 60 * 60 * 1000)
    });
    
    floor.imageDownloadURL = url;
    floor.imageURLExpiry = Date.now() + (7 * 24 * 60 * 60 * 1000);
  }
  
  return url;
}

/**
 * Delete floor image
 * @param {string} imageURL - gs:// path
 */
async function deleteFloorImage(imageURL) {
  if (!imageURL) return;
  await deleteAsset(imageURL);
}
```

### 5.5.4 Lazy Loading (FloorViewer)

**CRÍTICO**: NO eager load. Load on-demand apenas.

```javascript
// FloorViewer class (Index_v11.1.html)
class FloorViewer {
  /**
   * Lazy load floor image
   * @param {Object} floor
   * @returns {string} Object URL para canvas
   */
  async loadImage(floor) {
    // Se já carregado → return cached
    if (floor.imageLoaded && floor.imageData) {
      return floor.imageData;
    }
    
    // Fetch download URL (com TTL cache)
    const downloadURL = await getFloorImageURL(floor);
    if (!downloadURL) return null;
    
    // Download blob
    const response = await fetch(downloadURL);
    const blob = await response.blob();
    
    // Cache client-side
    floor.imageData = URL.createObjectURL(blob);
    floor.imageLoaded = true;
    
    return floor.imageData;
  }
}

// Uso (initFloorViewer)
async function initFloorViewer() {
  const floorId = parseInt(selector.value);
  const floor = projectData.floors.find(f => f.id === floorId);
  if (!floor) return;
  
  window.currentFloorViewer = new FloorViewer('zonamentoCanvas', floor);
  
  // 🆕 Lazy load image
  if (floor.imageURL) {
    const imageURL = await window.currentFloorViewer.loadImage(floor);
    if (imageURL) {
      window.currentFloorViewer.render();  // Re-render com imagem
    }
  }
}
```

### 5.5.5 Security Rules

**Firestore Rules** (já existem, sem mudanças):
```javascript
match /projects/{projectId} {
  allow read, write: if isOwner(projectId) && isJSJEmail();
}
```

**Storage Rules** (🆕 ADICIONAR):
```javascript
service firebase.storage {
  match /b/{bucket}/o {
    
    function isAuthenticated() {
      return request.auth != null;
    }
    
    function isJSJEmail() {
      return request.auth.token.email.matches('.*@jsj[.]pt$');
    }
    
    function isOwner(projectId) {
      return firestore.get(/databases/(default)/documents/projects/$(projectId)).data.owner == request.auth.uid;
    }
    
    match /projects/{projectId}/{allPaths=**} {
      // Read: owner only (valida via Firestore doc)
      allow read: if isAuthenticated() && isJSJEmail() && isOwner(projectId);
      
      // Write: owner only
      allow write: if isAuthenticated() && isJSJEmail() && isOwner(projectId);
    }
  }
}
```

**CRÍTICO**: Storage Rules podem aceder Firestore (`firestore.get()`).

### 5.5.6 Migration v11.0 → v11.1

**Script**: `migrate-v11.0-to-v11.1.html` (standalone page)

**Workflow**:
1. User: Backup Firestore (export manual)
2. Script: Itera todos os projects do user
3. Para cada floor com `imageData` (Base64):
   - Upload blob → Storage
   - Update Firestore doc: remove `imageData`, add `imageURL/imageDownloadURL/imageURLExpiry`
4. Validação: Todos floors têm `imageURL`

**IMPORTANTE**:
- ❌ NUNCA executar 2x (duplica blobs)
- ✅ SEMPRE backup antes
- ✅ VALIDAR Firestore doc size <100KB após

**Código Exemplo**:
```javascript
async function migrateProject(projectId) {
  const docRef = db.collection('projects').doc(projectId);
  const doc = await docRef.get();
  const data = doc.data();
  
  for (let i = 0; i < data.floors.length; i++) {
    const floor = data.floors[i];
    
    // Se já migrado → skip
    if (floor.imageURL) continue;
    
    // Se não tem Base64 → skip
    if (!floor.imageData) continue;
    
    // Convert Base64 → Blob
    const base64 = floor.imageData.split(',')[1];
    const blob = base64ToBlob(base64, 'image/png');
    
    // Upload → Storage
    const result = await uploadFloorImage(projectId, floor.id, blob);
    
    // Update Firestore (este floor apenas)
    await docRef.update({
      [`floors.${i}.imageURL`]: result.imageURL,
      [`floors.${i}.imageDownloadURL`]: result.imageDownloadURL,
      [`floors.${i}.imageURLExpiry`]: result.imageURLExpiry,
      [`floors.${i}.imageData`]: firebase.firestore.FieldValue.delete()
    });
    
    console.log(`✅ Migrated floor ${floor.id}`);
  }
}
```

### 5.5.7 Breaking Changes v11.1

| Mudança | v11.0 | v11.1 | Migração |
|---------|-------|-------|----------|
| Floor image field | `imageData` (Base64) | `imageURL` (Storage path) | Script obrigatório |
| Firestore doc size | ~5MB (10 floors) | ~50KB | Auto após migration |
| Image loading | Sync (inline Base64) | Async (lazy fetch) | Update code |
| FloorViewer API | `new FloorViewer()` sync | `await loadImage()` async | Add await calls |

**Compatibilidade**: JSONs v11.0 **incompatíveis** com v11.1.

---

