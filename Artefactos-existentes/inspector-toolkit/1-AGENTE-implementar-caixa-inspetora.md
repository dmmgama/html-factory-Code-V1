# Documento 1 — Script & Instruções para o AGENTE
## Implementar a "Caixa Inspetora" (Inspector) num ficheiro HTML

> **Para quem é este documento:** para um agente LLM (Claude Code, Cursor, etc.) a quem o David pede
> *"implementa a caixa inspetora neste HTML"*. Copia/cola este documento inteiro como instrução,
> ou aponta o agente para ele. Inclui o **código pronto-a-colar** + o **playbook de adaptação**.

---

## 0. O que é a Caixa Inspetora (resumo de 30 segundos)

Um painel lateral retrátil ("Inspector") injetado num ficheiro HTML self-contained, que torna a app
**observável** — permite ver, em tempo real e sem abrir o DevTools do browser:

| Vista | Mostra |
|-------|--------|
| **Data** | O JSON do estado da app (a "fonte da verdade"). |
| **Logic** | Que funções do "engine" foram chamadas na última interação (call tracer ao vivo). |
| **Layout** | Que "viewer"/canvas está a renderizar a vista atual, e quantas vezes renderizou. |
| **🎯 Pick** | Modo "inspecionar" tipo DevTools: ligas, clicas num elemento (a ação normal **não** dispara) e ele diz-te o Data/Logic/Layout **daquele** botão/menu/caixa. |

Objetivo do David: **validar se a arquitetura desenhada está a ser seguida** — comparar o que cada
elemento *diz* que faz (Pick) com o que o tracer *regista* que aconteceu (Logic).

---

## 1. Regras de ouro para o agente (LÊ ISTO PRIMEIRO)

1. **Não-invasivo.** Não reescreves a app. Não alteras nenhuma linha do código original. Tudo o que
   adicionas é: (a) um bloco CSS antes de `</style>`, (b) um bloco HTML a seguir ao `<body>` (ou antes
   de `</body>`), (c) um bloco JS (IIFE) **no fim do último `<script>`, imediatamente antes da última
   instrução de arranque** (ex.: `renderAll()`, `init()`, `main()` — ou no fim do script se não houver).
2. **Ficheiros grandes.** Estes HTML costumam ter dados embutidos (podem ter ~1MB / milhares de linhas).
   **Nunca leias o ficheiro inteiro.** Usa pesquisa (grep) para localizar e lê janelas pequenas.
3. **Descobre o "engine" antes de codificar.** Tens de identificar 4 coisas (ver Secção 3). Se não
   conseguires identificar com confiança, **pergunta ao David** em vez de inventar.
4. **Orçamento.** Faz edições cirúrgicas (idealmente ≤ 4 edições). Verifica no fim que o ficheiro
   continua bem-formado (o `<script>` fecha, a app arranca).
5. **Idioma.** Toda a UI e textos em **pt-PT**.
6. **Faz checkpoint.** Se não houver git, cria uma cópia datada do ficheiro antes de mexer
   (ex.: `_checkpoints/<nome>_<AAAA-MM-DD>.html`).

---

## 2. Passo-a-passo

1. **Checkpoint** do ficheiro original.
2. **Descoberta** (Secção 3): identifica STATE, funções de engine, viewers e elementos interativos.
3. **Cola o CSS** (Secção 4) antes de `</style>`.
4. **Cola o HTML** (Secção 5) a seguir à abertura `<body>`.
5. **Cola o JS** (Secção 6) no fim do último `<script>`, antes da instrução de arranque, e
   **preenche os 4 pontos de configuração** marcados com `// ⚙️ CONFIG`.
6. **Verifica** (Secção 7).
7. **Relata** ao David o que ligaste e quais os limites.

---

## 3. Descoberta — as 4 coisas que tens de mapear

Para o padrão "Curador" (vanilla JS, estado global em JSON, funções de render globais):

### 3.1 — O objeto de estado (`STATE`) → alimenta a vista **Data**
Procura uma variável global que seja a fonte da verdade. Pistas: `let STATE`, `var state`, `const DATA`,
`window.app`, `let store`. Anota o nome e as suas sub-coleções principais (arrays/objetos) — vais listá-las
no dropdown da vista Data.

### 3.2 — As funções do "engine" → alimentam a vista **Logic**
Lista as funções globais relevantes (render, save, load, commit, import/export, ações de utilizador).
Procura `function nome(` no topo do scope do script. Reúne-as num array de nomes.

### 3.3 — Os "viewers" / vistas → alimentam a vista **Layout**
A app costuma ter separadores/tabs. Identifica como se sabe qual está ativo (ex.: `.tab.active`,
`data-view`, um `currentView`) e qual a função que renderiza cada um.

### 3.4 — Os elementos interativos → alimentam o **Pick**
Tabs, botões (`#btn...`), filtros (`select`/`input`), caixas, cartões, nós SVG, células editáveis.
Para cada um (ou por grupos via seletor) escreves um mini-relatório {data, logic, layout}.

> **Se for um HTML que NÃO segue o padrão Curador** (React/Vue/sem STATE global, handlers internos):
> ver Secção 8 (Adaptação).

---

## 4. CÓDIGO — CSS (colar antes de `</style>`)

```html
<style>
/* ====== CAIXA INSPETORA — CSS ====== */
:root{
  --insp-w:360px;
  --insp-bg:#0f1117; --insp-panel:#161b24; --insp-border:#252d3d;
  --insp-ink:#c9d1e0; --insp-muted:#5c6a80; --insp-accent:#4f9eff;
  --insp-ok:#3dd68c; --insp-warn:#f5a623; --insp-bad:#ff5f57;
}
body.insp-open { margin-right: var(--insp-w); }
#inspToggleBtn{position:fixed;bottom:20px;right:16px;z-index:400;width:42px;height:42px;border-radius:50%;
  background:var(--insp-accent);border:none;color:#fff;font-size:18px;cursor:pointer;
  box-shadow:0 3px 12px rgba(79,158,255,.45);display:flex;align-items:center;justify-content:center;transition:transform .15s}
#inspToggleBtn:hover{transform:scale(1.08)}
#inspToggleBtn.active{background:#1a56e0}
#inspector{position:fixed;top:0;right:0;bottom:0;width:var(--insp-w);background:var(--insp-bg);
  border-left:1px solid var(--insp-border);display:flex;flex-direction:column;z-index:300;transform:translateX(100%);
  transition:transform .22s cubic-bezier(.4,0,.2,1);font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;color:var(--insp-ink)}
#inspector.open{transform:translateX(0)}
.insp-header{padding:10px 12px 8px;border-bottom:1px solid var(--insp-border);display:flex;align-items:center;gap:8px;flex-shrink:0}
.insp-title{font-weight:700;font-size:13px;color:#fff;flex:1;letter-spacing:.03em}
.insp-badge{background:var(--insp-accent);color:#000;border-radius:4px;font-size:10px;padding:1px 5px;font-weight:800}
#inspPickBtn{background:none;border:1px solid var(--insp-border);color:var(--insp-warn);border-radius:5px;
  font-size:11px;padding:3px 7px;cursor:pointer;font-family:inherit;font-weight:700;white-space:nowrap}
#inspPickBtn:hover{border-color:var(--insp-warn)}
#inspPickBtn.active{background:var(--insp-warn);color:#000;border-color:var(--insp-warn)}
.insp-close{background:none;border:none;color:var(--insp-muted);font-size:18px;cursor:pointer;line-height:1;padding:0 2px}
.insp-close:hover{color:#fff}
.insp-tabs{display:flex;border-bottom:1px solid var(--insp-border);flex-shrink:0}
.insp-tab{flex:1;padding:7px 4px;text-align:center;cursor:pointer;font-size:11px;font-weight:700;color:var(--insp-muted);
  border-bottom:2px solid transparent;margin-bottom:-1px;letter-spacing:.04em;text-transform:uppercase;transition:color .12s,border-color .12s}
.insp-tab:hover{color:var(--insp-ink)}
.insp-tab.active{color:var(--insp-accent);border-bottom-color:var(--insp-accent)}
.insp-pane{display:none;flex:1;overflow:auto;padding:10px;flex-direction:column;gap:8px}
.insp-pane.active{display:flex}
.insp-section{margin-bottom:10px}
.insp-section-title{font-size:10px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--insp-muted);
  margin-bottom:5px;display:flex;align-items:center;gap:5px}
.insp-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.insp-dot.ok{background:var(--insp-ok)}.insp-dot.warn{background:var(--insp-warn)}
.insp-dot.bad{background:var(--insp-bad)}.insp-dot.accent{background:var(--insp-accent)}
.insp-json{background:var(--insp-panel);border:1px solid var(--insp-border);border-radius:6px;padding:8px;
  max-height:340px;overflow:auto;font-size:11px;line-height:1.55;white-space:pre-wrap;word-break:break-all}
.insp-json .jk{color:#9ecbff}.insp-json .js{color:#9aeabc}.insp-json .jn{color:#f8c975}
.insp-json .jb{color:#ff9a6c}.insp-json .jl{color:var(--insp-muted)}
.insp-call-log{display:flex;flex-direction:column;gap:3px}
.insp-call{background:var(--insp-panel);border:1px solid var(--insp-border);border-radius:5px;padding:5px 8px;
  display:flex;align-items:center;gap:7px;animation:insp-fadein .18s ease}
@keyframes insp-fadein{from{opacity:0;transform:translateY(-3px)}to{opacity:1;transform:none}}
.insp-call-name{color:var(--insp-accent);font-weight:700;font-size:11.5px}
.insp-call-time{color:var(--insp-muted);font-size:10px;margin-left:auto;white-space:nowrap}
.insp-call-count{background:var(--insp-accent);color:#000;border-radius:10px;font-size:10px;padding:0 5px;font-weight:800}
.insp-call-idle,.insp-pick-idle{color:var(--insp-muted);font-size:11px;font-style:italic}
.insp-layout-card{background:var(--insp-panel);border:1px solid var(--insp-border);border-radius:6px;padding:8px 10px;margin-bottom:6px}
.insp-layout-card .lc-label{font-size:10px;color:var(--insp-muted);text-transform:uppercase;letter-spacing:.07em;margin-bottom:3px}
.insp-layout-card .lc-value{color:#fff;font-weight:700;font-size:13px}
.insp-layout-card .lc-sub{color:var(--insp-muted);font-size:11px;margin-top:2px}
.insp-layout-card .lc-pill,.lc-pill{display:inline-block;background:rgba(79,158,255,.15);border:1px solid rgba(79,158,255,.3);
  color:var(--insp-accent);border-radius:4px;font-size:10px;padding:1px 6px;font-weight:700;margin-top:4px}
.insp-refresh{background:none;border:1px solid var(--insp-border);color:var(--insp-muted);border-radius:5px;
  font-size:11px;padding:3px 8px;cursor:pointer;font-family:inherit}
.insp-refresh:hover{color:#fff;border-color:var(--insp-accent)}
#inspector ::-webkit-scrollbar{width:5px;height:5px}
#inspector ::-webkit-scrollbar-track{background:var(--insp-bg)}
#inspector ::-webkit-scrollbar-thumb{background:var(--insp-border);border-radius:3px}
/* --- modo PICK --- */
body.insp-picking{cursor:crosshair}
body.insp-picking::after{content:"";position:fixed;inset:0 var(--insp-w) 0 0;border:3px solid var(--insp-warn);
  pointer-events:none;z-index:250;box-sizing:border-box}
.insp-hover-target{outline:2px dashed var(--insp-warn)!important;outline-offset:1px!important}
#inspPickBanner{position:fixed;top:0;left:0;right:var(--insp-w);background:var(--insp-warn);color:#1a1100;
  font-weight:800;font-size:13px;text-align:center;padding:5px;z-index:260;display:none;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.02em}
body.insp-picking #inspPickBanner{display:block}
.insp-pick-head{background:var(--insp-panel);border:1px solid var(--insp-border);border-radius:6px;padding:8px 10px;margin-bottom:8px}
.insp-pick-head .ph-tag{color:var(--insp-warn);font-weight:800;font-size:12px;margin-bottom:4px}
.insp-pick-head .ph-sel{color:var(--insp-muted);font-size:10.5px;word-break:break-all}
.insp-pick-card{background:var(--insp-panel);border:1px solid var(--insp-border);border-left-width:3px;
  border-radius:6px;padding:8px 10px;margin-bottom:6px}
.insp-pick-card.data{border-left-color:var(--insp-ok)}
.insp-pick-card.logic{border-left-color:var(--insp-accent)}
.insp-pick-card.layout{border-left-color:var(--insp-warn)}
.insp-pick-card .pc-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--insp-muted);margin-bottom:4px}
.insp-pick-card .pc-text{font-size:11.5px;line-height:1.5;color:var(--insp-ink)}
.insp-pick-card code{background:#0c0f15;padding:0 4px;border-radius:3px;color:#9ecbff;font-size:10.5px}
</style>
```

---

## 5. CÓDIGO — HTML (colar logo a seguir a `<body>`)

```html
<!-- ======= CAIXA INSPETORA ======= -->
<button id="inspToggleBtn" title="Abrir/fechar Inspector">🔬</button>
<aside id="inspector">
  <div class="insp-header">
    <span class="insp-title">Inspector</span>
    <span class="insp-badge">OBS</span>
    <button id="inspPickBtn" title="Modo inspecionar: clica num elemento (não dispara a ação)">🎯 Inspecionar</button>
    <button class="insp-close" id="inspClose" title="Fechar">×</button>
  </div>
  <div class="insp-tabs">
    <div class="insp-tab active" data-insp="data">Data</div>
    <div class="insp-tab" data-insp="logic">Logic</div>
    <div class="insp-tab" data-insp="layout">Layout</div>
    <div class="insp-tab" data-insp="pick">🎯 Pick</div>
  </div>
  <div class="insp-pane active" id="insp-data">
    <div class="insp-section">
      <div class="insp-section-title"><span class="insp-dot ok"></span>JSON State (fonte da verdade)</div>
      <div style="display:flex;gap:6px;margin-bottom:6px;align-items:center">
        <select id="inspDataSel" style="flex:1;background:#0f1117;border:1px solid #252d3d;color:#c9d1e0;border-radius:5px;padding:3px 6px;font-size:11px;font-family:inherit"></select>
        <button class="insp-refresh" id="inspDataRefresh">↻</button>
      </div>
      <div class="insp-json" id="inspDataJson">—</div>
    </div>
    <div class="insp-section">
      <div class="insp-section-title"><span class="insp-dot accent"></span>Estatísticas</div>
      <div class="insp-json" id="inspDataStats" style="max-height:120px">—</div>
    </div>
  </div>
  <div class="insp-pane" id="insp-logic">
    <div class="insp-section">
      <div class="insp-section-title"><span class="insp-dot warn"></span>Últimas chamadas ao engine</div>
      <button class="insp-refresh" id="inspLogicClear" style="margin-bottom:6px">✕ limpar</button>
      <div class="insp-call-log" id="inspCallLog">
        <div class="insp-call-idle">Nenhuma interação registada ainda.</div>
      </div>
    </div>
  </div>
  <div class="insp-pane" id="insp-layout">
    <div class="insp-section">
      <div class="insp-section-title"><span class="insp-dot accent"></span>Viewer ativo</div>
      <div class="insp-layout-card">
        <div class="lc-label">Canvas atual</div>
        <div class="lc-value" id="inspLayoutName">—</div>
        <div class="lc-sub" id="inspLayoutDesc">—</div>
        <div class="lc-pill" id="inspLayoutPill">—</div>
      </div>
    </div>
    <div class="insp-section">
      <div class="insp-section-title"><span class="insp-dot ok"></span>Todos os viewers</div>
      <div id="inspLayoutAll"></div>
    </div>
    <div class="insp-section">
      <div class="insp-section-title"><span class="insp-dot warn"></span>Render count (sessão)</div>
      <div class="insp-json" id="inspRenderCount" style="max-height:140px">—</div>
    </div>
  </div>
  <div class="insp-pane" id="insp-pick">
    <div id="inspPickReport">
      <div class="insp-pick-idle">Carrega em 🎯 Inspecionar e clica num elemento da app para ver o seu Data / Logic / Layout.</div>
    </div>
  </div>
</aside>
<div id="inspPickBanner">🎯 MODO INSPECIONAR ATIVO — clica num elemento para o analisar (Esc para sair)</div>
```

---

## 6. CÓDIGO — JS (colar no fim do último `<script>`, antes do arranque da app)

> **Importante:** preenche os **4 pontos `// ⚙️ CONFIG`**. Sem isso, o Inspector abre mas mostra "—".

```js
/* ====== CAIXA INSPETORA — ENGINE ====== */
(function(){
  /* ⚙️ CONFIG 1 — como obter o objeto de estado (a fonte da verdade) */
  function getState(){
    return (typeof STATE !== "undefined") ? STATE : (window.STATE || window.state || {});
  }
  /* ⚙️ CONFIG 2 — coleções a mostrar no dropdown da vista Data.
     {chave no dropdown : função que devolve o pedaço de estado} */
  function dataSources(){
    const S = getState();
    return {
      "estado completo": ()=>S,
      // exemplos (adapta aos arrays/objetos reais da app):
      // "projetos (array)": ()=>S.projetos,
      // "links (array)":    ()=>S.links,
    };
  }
  /* ⚙️ CONFIG 3 — funções do engine a "ouvir" (call tracer da vista Logic).
     Têm de ser funções globais (no mesmo scope ou em window). */
  const ENGINE_FNS = [
    // "renderAll","save","load","commit","render", ...
  ];
  /* ⚙️ CONFIG 4 — viewers (vista Layout) + como saber qual está ativo. */
  const VIEWER_META = {
    // "tabela": {label:"Tabela", icon:"📋", renderer:"renderHead+renderBody", desc:"Grelha editável."},
  };
  function activeViewKey(){
    // adapta: ex. document.querySelector(".tab.active")?.dataset.view
    const t = document.querySelector(".tab.active,[data-view].active,.view.active");
    return t ? (t.dataset.view || t.id || "—") : "—";
  }
  /* ⚙️ CONFIG (Pick) — metadados por elemento. Seletores do MAIS específico ao MENOS específico. */
  const PICK_META = {
    // '#btnGuardar': { data:'Escreve em STATE…', logic:'save()', layout:'Não muda o canvas.' },
    // '.tab[data-view="tabela"]': { data:'Lê STATE.x', logic:'renderAll()', layout:'Canvas Tabela.' },
  };

  /* ---------- daqui para baixo: motor genérico, não precisa de tocar ---------- */
  const MAX_LOG=50, callLog=[], callCount={}, renderCount={};
  let inspOpen=false, inspectMode=false, lastHover=null;
  const $=id=>document.getElementById(id);

  function recordCall(name){
    callCount[name]=(callCount[name]||0)+1;
    const p=callLog[0];
    if(p&&p.name===name){p.count++;p.ts=Date.now();}
    else{callLog.unshift({name,ts:Date.now(),count:1}); if(callLog.length>MAX_LOG)callLog.pop();}
    if(inspOpen && $("insp-logic").classList.contains("active")) renderLogic();
  }
  function patch(fn,name){ return function(){ recordCall(name); return fn.apply(this,arguments); }; }
  ENGINE_FNS.forEach(n=>{ if(typeof window[n]==="function") window[n]=patch(window[n],n); });

  // hook extra no renderizador principal p/ atualizar render count + refresh
  const mainRender = ENGINE_FNS.find(n=>/render(All|Main)?$/i.test(n)) || ENGINE_FNS[0];
  if(mainRender && typeof window[mainRender]==="function"){
    const orig=window[mainRender];
    window[mainRender]=function(){ const r=orig.apply(this,arguments);
      const v=activeViewKey(); renderCount[v]=(renderCount[v]||0)+1; if(inspOpen) refreshAll(); return r; };
  }

  function hl(json){ return String(json)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")
    .replace(/"([^"\\]*(\\.[^"\\]*)*)"\s*:/g,'<span class="jk">"$1"</span>:')
    .replace(/:\s*"([^"\\]*(\\.[^"\\]*)*)"/g,': <span class="js">"$1"</span>')
    .replace(/:\s*(-?\d+(\.\d+)?)/g,': <span class="jn">$1</span>')
    .replace(/:\s*(true|false)/g,': <span class="jb">$1</span>')
    .replace(/:\s*(null)/g,': <span class="jl">null</span>'); }
  function pretty(obj,max){ let d=obj;
    if(Array.isArray(obj)&&max&&obj.length>max) d=obj.slice(0,max);
    let raw=JSON.stringify(d,null,2);
    if(Array.isArray(obj)&&max&&obj.length>max) raw=raw.slice(0,-1)+',\n  … (+'+(obj.length-max)+' mais)\n]';
    return hl(raw); }

  // ---- Data ----
  function fillDataSel(){ const sel=$("inspDataSel"); if(sel.options.length) return;
    Object.keys(dataSources()).forEach(k=>{ const o=document.createElement("option"); o.value=k; o.textContent=k; sel.appendChild(o); }); }
  function renderData(){ fillDataSel(); const k=$("inspDataSel").value||Object.keys(dataSources())[0];
    let v; try{ v=dataSources()[k](); }catch(e){ v=null; }
    $("inspDataJson").innerHTML=pretty(v, Array.isArray(v)?5:null);
    const S=getState(), stats={};
    Object.keys(S||{}).forEach(key=>{ const val=S[key]; stats[key]=Array.isArray(val)?val.length+" itens":(typeof val); });
    $("inspDataStats").innerHTML=hl(JSON.stringify(stats,null,2)); }

  // ---- Logic ----
  function renderLogic(){ const box=$("inspCallLog");
    if(!callLog.length){ box.innerHTML='<div class="insp-call-idle">Nenhuma interação registada ainda.</div>'; return; }
    box.innerHTML=callLog.map(e=>{ const a=Math.round((Date.now()-e.ts)/100)/10;
      const t=a<1?"agora":a+"s atrás"; const c=e.count>1?'<span class="insp-call-count">×'+e.count+'</span>':'';
      return '<div class="insp-call"><span class="insp-call-name">'+e.name+'()</span>'+c+'<span class="insp-call-time">'+t+'</span></div>'; }).join(""); }

  // ---- Layout ----
  function renderLayout(){ const v=activeViewKey(); const m=VIEWER_META[v]||{label:v,icon:"?",renderer:"?",desc:"Vista."};
    $("inspLayoutName").textContent=(m.icon||"")+" "+m.label;
    $("inspLayoutDesc").textContent=m.desc||""; $("inspLayoutPill").textContent="renderer: "+(m.renderer||"?");
    $("inspLayoutAll").innerHTML=Object.entries(VIEWER_META).map(([k,mm])=>{ const on=k===v; const c=renderCount[k]||0;
      return '<div class="insp-layout-card" style="'+(on?'border-color:var(--insp-accent)':'')+'">'+
        '<div class="lc-label">'+(mm.icon||"")+' '+mm.label+(on?' <span class="lc-pill">ATIVO</span>':'')+'</div>'+
        '<div class="lc-sub">'+(mm.renderer||"")+'</div><div class="lc-sub">renders: <b>'+c+'</b></div></div>'; }).join("");
    $("inspRenderCount").innerHTML=hl(JSON.stringify(renderCount,null,2)); }

  function refreshAll(){ if(!inspOpen) return; const tab=document.querySelector(".insp-tab.active");
    const p=tab?tab.dataset.insp:"data"; if(p==="data")renderData(); if(p==="logic")renderLogic(); if(p==="layout")renderLayout(); }

  // ---- abrir/fechar ----
  const insp=$("inspector"), tgl=$("inspToggleBtn");
  function open(){ inspOpen=true; insp.classList.add("open"); tgl.classList.add("active"); document.body.classList.add("insp-open"); refreshAll(); }
  function close(){ inspOpen=false; insp.classList.remove("open"); tgl.classList.remove("active"); document.body.classList.remove("insp-open"); }
  tgl.onclick=()=> inspOpen?close():open();
  $("inspClose").onclick=close;
  document.querySelectorAll(".insp-tab").forEach(t=>t.onclick=()=>{
    document.querySelectorAll(".insp-tab").forEach(x=>x.classList.remove("active"));
    document.querySelectorAll(".insp-pane").forEach(x=>x.classList.remove("active"));
    t.classList.add("active"); $("insp-"+t.dataset.insp).classList.add("active"); refreshAll(); });
  $("inspDataRefresh").onclick=renderData; $("inspDataSel").onchange=renderData;
  $("inspLogicClear").onclick=()=>{ callLog.length=0; renderLogic(); };

  // ---- modo PICK ----
  const PICK_SELECTORS='.tab,[data-view],button,.btn,[id^="btn"],[onclick],.menu-item,.subtab,select,input,textarea,td';
  function findInspectable(t){ if(!t||!t.closest) return null;
    if(t.closest("#inspector")||t.closest("#inspToggleBtn")) return null; return t.closest(PICK_SELECTORS); }
  function lookup(el){ for(const s in PICK_META){ if(el.matches&&el.matches(s)) return Object.assign({matched:s},PICK_META[s]); }
    if(el.id&&PICK_META["#"+el.id]) return Object.assign({matched:"#"+el.id},PICK_META["#"+el.id]); return infer(el); }
  function infer(el){ const tag=el.tagName.toLowerCase(), id=el.id?"#"+el.id:"";
    const txt=(el.textContent||"").trim().replace(/\s+/g," ").slice(0,50);
    const view=el.closest("[data-view]"); const onclk=el.getAttribute&&el.getAttribute("onclick");
    if(tag==="select"||tag==="input"||tag==="textarea"){ const lbl=el.closest("label"); let name=lbl?lbl.textContent.trim():"";
      name=name||el.placeholder||el.id||tag;
      return {generic:true,_hdr:"Controlo de formulário — &lt;"+tag+"&gt; "+(id?'id="'+el.id+'" ':"")+'· "'+name.slice(0,40)+'"',
        data:'Controlo "<b>'+name.slice(0,40)+'</b>": lê/escreve um valor de estado/UI ao mudar.',
        logic:onclk?("Handler inline: <code>"+onclk.slice(0,70)+"</code>"):"<code>"+(tag==="select"?"onchange":"oninput")+"</code> → guarda o valor e re-renderiza.",
        layout:view?("Afeta a vista <code>"+view.getAttribute("data-view")+"</code>."):"Atualiza a UI dependente."}; }
    return {generic:true,_hdr:"Sem metadados — &lt;"+tag+"&gt; "+(id?'id="'+el.id+'" ':"")+(txt?'· "'+txt+'"':""),
      data:view?("Pertence à vista <code>"+view.getAttribute("data-view")+"</code> (lê STATE via render)."):"Lê/escreve parte do STATE ou de preferências locais.",
      logic:onclk?("Handler inline: <code>"+onclk.slice(0,70)+"</code>"):"Lógica inferida (listener atribuído em JS).",
      layout:view?("Afeta o canvas da vista <code>"+view.getAttribute("data-view")+"</code>."):"Elemento de UI."}; }
  function pickReport(el){ const m=lookup(el), r=$("inspPickReport");
    const head=m._hdr||("&lt;"+el.tagName.toLowerCase()+"&gt; "+(el.id?'id="'+el.id+'"':""));
    const sel=m.matched?("registo: <code>"+m.matched+"</code>"):"sem entrada no registo — inferido";
    r.innerHTML='<div class="insp-pick-head"><div class="ph-tag">🎯 Elemento inspecionado</div>'+
      '<div class="ph-sel">'+head+'</div><div class="ph-sel">'+sel+'</div></div>'+
      '<div class="insp-pick-card data"><div class="pc-label">📦 Data</div><div class="pc-text">'+m.data+'</div></div>'+
      '<div class="insp-pick-card logic"><div class="pc-label">⚙️ Logic</div><div class="pc-text">'+m.logic+'</div></div>'+
      '<div class="insp-pick-card layout"><div class="pc-label">🖼️ Layout</div><div class="pc-text">'+m.layout+'</div></div>'; }
  function switchPick(){ document.querySelectorAll(".insp-tab").forEach(t=>t.classList.remove("active"));
    document.querySelectorAll(".insp-pane").forEach(p=>p.classList.remove("active"));
    document.querySelector('.insp-tab[data-insp="pick"]').classList.add("active"); $("insp-pick").classList.add("active"); }
  function clearHover(){ if(lastHover){ lastHover.classList.remove("insp-hover-target"); lastHover=null; } }
  const pickBtn=$("inspPickBtn");
  function setPick(on){ inspectMode=on; document.body.classList.toggle("insp-picking",on); pickBtn.classList.toggle("active",on);
    if(on){ if(!inspOpen)open(); switchPick(); } else clearHover(); }
  pickBtn.onclick=()=>setPick(!inspectMode);
  document.addEventListener("mouseover",e=>{ if(!inspectMode)return; const el=findInspectable(e.target);
    if(el===lastHover)return; clearHover(); if(el){ el.classList.add("insp-hover-target"); lastHover=el; } });
  document.addEventListener("click",e=>{ if(!inspectMode)return;
    if(e.target.closest&&e.target.closest("#inspector"))return;
    const el=findInspectable(e.target); e.preventDefault(); e.stopPropagation();
    if(e.stopImmediatePropagation)e.stopImmediatePropagation();
    if(el){ switchPick(); pickReport(el); } },true);
  document.addEventListener("keydown",e=>{
    if((e.ctrlKey||e.metaKey)&&e.shiftKey&&(e.key==="I"||e.key==="i")){ e.preventDefault(); inspOpen?close():open(); }
    if(e.key==="Escape"&&inspectMode) setPick(false); });
})();
```

---

## 7. Verificação (o agente faz no fim)

- O ficheiro continua a abrir e a app arranca sem erros na consola.
- O botão 🔬 aparece (canto inferior direito); abre/fecha o painel; `Ctrl+Shift+I` também.
- **Data** mostra JSON real do estado (não "—").
- **Logic** regista chamadas ao usares a app.
- **Layout** mostra o viewer ativo e conta renders.
- **🎯 Inspecionar** → moldura âmbar + banner; clicar num elemento mostra o relatório e **não** dispara a ação; `Esc` sai.
- Estrutura intacta: o `<script>` fecha, há um só bloco CSS/HTML/JS do Inspector.

---

## 8. Adaptação a HTML que NÃO segue o padrão "Curador"

| Situação no HTML-alvo | O que o agente faz |
|---|---|
| **Sem STATE global** (dados espalhados/no DOM) | Em `getState()`, monta um objeto-resumo a partir do que existir (ex.: ler `localStorage`, ou montar `{itens: [...]}` a partir do DOM). A vista Data passa a ser um *snapshot*. |
| **React/Vue/Svelte** | Não dá para envolver funções globais. Alternativas: (a) expor `window.__state` no app e ler daí; (b) na vista Logic, em vez de envolver funções, registar eventos do utilizador (cliques) com um listener delegado; (c) Layout: ler a rota atual / componente montado. Avisa o David que o tracer fica "por evento", não "por função". |
| **Handlers só inline (`onclick=...`)** | O Pick já lê o atributo `onclick` e mostra-o como Logic. O tracer da vista Logic pode não capturar nada — documenta isso. |
| **Sem tabs/viewers** | `VIEWER_META` pode ter uma só entrada ("app"); a vista Layout fica simples mas funcional. |
| **Vários `<script>` / módulos ES** | Cola o IIFE no script onde as funções-alvo são visíveis. Para módulos, pode ser preciso o app expor as funções em `window`. |

**Regra:** se uma das 4 vistas não puder ser ligada com fidelidade, **implementa as outras e diz claramente
ao David qual ficou limitada e porquê** — não finjas dados.

---

## 9. Checklist final de entrega (o agente relata isto)

- [ ] Checkpoint criado em `_checkpoints/…`
- [ ] CSS + HTML + JS colados; 4 `// ⚙️ CONFIG` preenchidos
- [ ] STATE ligado à vista Data ✓ / ✗ (se ✗: porquê)
- [ ] N funções ligadas ao tracer (Logic) — listar
- [ ] M viewers no Layout — listar
- [ ] Pick: que elementos têm metadados próprios vs inferidos
- [ ] Limitações conhecidas
- [ ] App testada e a arrancar
