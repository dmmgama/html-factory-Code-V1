# Build browsable HTML versions of the 3 Markdown manuals.
# Offline, self-contained: embeds the raw .md and renders it with a tiny built-in parser.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlDir = Join-Path $root "html"
if (-not (Test-Path $htmlDir)) { New-Item -ItemType Directory -Path $htmlDir | Out-Null }

$docs = @(
  @{ md = "0-DAVID-instalar-passo-a-passo.md";       html = "0-INSTALAR.html"; title = "0 - David: Instalar (passo-a-passo)";        accent = "#a78bfa" },
  @{ md = "1-AGENTE-implementar-caixa-inspetora.md"; html = "1-AGENTE.html";   title = "1 - Agente: Implementar a Caixa Inspetora"; accent = "#4f9eff" },
  @{ md = "2-DAVID-manual-de-utilizacao.md";        html = "2-DAVID.html";    title = "2 - David: Manual de Utilizacao";            accent = "#3dd68c" },
  @{ md = "3-LLM-manual-da-funcionalidade.md";      html = "3-LLM.html";      title = "3 - LLM: Manual da Funcionalidade";          accent = "#f5a623" }
)

# HTML template parts (the {{...}} tokens are replaced per doc)
$head = @'
<!DOCTYPE html>
<html lang="pt-PT"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>__TITLE__</title>
<style>
:root{--accent:__ACCENT__}
*{box-sizing:border-box}
body{margin:0;background:#0f1117;color:#c9d1e0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;font-size:15px}
.wrap{max-width:880px;margin:0 auto;padding:32px 22px 90px}
.nav{position:sticky;top:0;background:#0f1117ee;backdrop-filter:blur(6px);padding:10px 0;border-bottom:1px solid #252d3d;margin-bottom:22px;display:flex;gap:8px;flex-wrap:wrap;z-index:5}
.nav a{color:#9aa6ba;text-decoration:none;font-size:13px;border:1px solid #252d3d;border-radius:6px;padding:4px 10px}
.nav a:hover{color:#fff;border-color:var(--accent)}
.nav a.cur{color:#000;background:var(--accent);border-color:var(--accent);font-weight:700}
h1,h2,h3,h4{color:#fff;line-height:1.25;margin:1.4em 0 .5em}
h1{font-size:26px;border-bottom:2px solid var(--accent);padding-bottom:.3em}
h2{font-size:20px;border-bottom:1px solid #252d3d;padding-bottom:.25em}
h3{font-size:16.5px}h4{font-size:14px;color:var(--accent)}
a{color:var(--accent)}
p,li{margin:.4em 0}
ul,ol{padding-left:1.4em}
hr{border:0;border-top:1px solid #252d3d;margin:1.8em 0}
blockquote{border-left:3px solid var(--accent);margin:.8em 0;padding:.4em 14px;background:#161b24;border-radius:0 6px 6px 0;color:#aab6c8}
code{background:#1b2230;color:#9ecbff;padding:1px 6px;border-radius:4px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.88em}
pre{background:#0b0e14;border:1px solid #252d3d;border-radius:8px;padding:14px;overflow:auto}
pre code{background:none;color:#c9d1e0;padding:0;font-size:12.5px;line-height:1.5}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:13.5px}
th,td{border:1px solid #252d3d;padding:7px 10px;text-align:left;vertical-align:top}
th{background:#161b24;color:#fff}
tr:nth-child(even) td{background:#13171f}
.tag{display:inline-block;background:var(--accent);color:#000;font-size:11px;font-weight:800;border-radius:5px;padding:2px 8px;letter-spacing:.04em}
</style></head><body><div class="wrap">
<div class="nav">
<a href="index.html">&#127968; &Iacute;ndice</a>
<a href="0-INSTALAR.html" class="__C0__">0 &middot; Instalar</a>
<a href="1-AGENTE.html" class="__C1__">1 &middot; Agente</a>
<a href="2-DAVID.html" class="__C2__">2 &middot; David</a>
<a href="3-LLM.html" class="__C3__">3 &middot; LLM</a>
</div>
<div id="content"></div>
</div>
<script id="md" type="text/markdown">__MD__</script>
<script>
/* mini markdown renderer (suficiente para estes documentos) */
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function inline(s){
  return s
    .replace(/`([^`]+)`/g,(m,c)=>"<code>"+esc(c)+"</code>")
    .replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>")
    .replace(/(^|[^*])\*([^*]+)\*/g,"$1<i>$2</i>")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2">$1</a>');
}
function render(md){
  const lines=md.split(/\r?\n/); let html="", i=0;
  function flushTable(buf){
    if(buf.length<2) return buf.map(r=>"<p>"+inline(esc(r))+"</p>").join("");
    const rows=buf.map(r=>r.replace(/^\||\|$/g,"").split("|").map(c=>c.trim()));
    const head=rows[0]; const body=rows.slice(2);
    let t="<table><thead><tr>"+head.map(h=>"<th>"+inline(esc(h))+"</th>").join("")+"</tr></thead><tbody>";
    body.forEach(r=>{ t+="<tr>"+r.map(c=>"<td>"+inline(esc(c))+"</td>").join("")+"</tr>"; });
    return t+"</tbody></table>";
  }
  while(i<lines.length){
    let ln=lines[i];
    if(/^```/.test(ln)){ let code=""; i++; while(i<lines.length && !/^```/.test(lines[i])){ code+=lines[i]+"\n"; i++; } i++;
      html+="<pre><code>"+esc(code.replace(/\n$/,""))+"</code></pre>"; continue; }
    if(/^\s*\|.*\|\s*$/.test(ln)){ let buf=[]; while(i<lines.length && /^\s*\|.*\|\s*$/.test(lines[i])){ buf.push(lines[i].trim()); i++; }
      html+=flushTable(buf); continue; }
    if(/^#{1,6}\s/.test(ln)){ const lvl=ln.match(/^#+/)[0].length; html+="<h"+lvl+">"+inline(esc(ln.replace(/^#+\s/,"")))+"</h"+lvl+">"; i++; continue; }
    if(/^\s*>/.test(ln)){ let buf=[]; while(i<lines.length && /^\s*>/.test(lines[i])){ buf.push(lines[i].replace(/^\s*>\s?/,"")); i++; }
      html+="<blockquote>"+buf.map(b=>inline(esc(b))).join("<br>")+"</blockquote>"; continue; }
    if(/^\s*[-*]\s/.test(ln)){ let buf=[]; while(i<lines.length && /^\s*[-*]\s/.test(lines[i])){ buf.push(lines[i].replace(/^\s*[-*]\s/,"")); i++; }
      html+="<ul>"+buf.map(b=>"<li>"+inline(esc(b))+"</li>").join("")+"</ul>"; continue; }
    if(/^\s*\d+\.\s/.test(ln)){ let buf=[]; while(i<lines.length && /^\s*\d+\.\s/.test(lines[i])){ buf.push(lines[i].replace(/^\s*\d+\.\s/,"")); i++; }
      html+="<ol>"+buf.map(b=>"<li>"+inline(esc(b))+"</li>").join("")+"</ol>"; continue; }
    if(/^\s*---\s*$/.test(ln)){ html+="<hr>"; i++; continue; }
    if(/^\s*$/.test(ln)){ i++; continue; }
    html+="<p>"+inline(esc(ln))+"</p>"; i++;
  }
  return html;
}
document.getElementById("content").innerHTML = render(document.getElementById("md").textContent);
</script></body></html>
'@

foreach ($d in $docs) {
  $mdPath = Join-Path $root $d.md
  $raw = Get-Content $mdPath -Raw -Encoding UTF8
  # neutralize </script> inside the md so it doesn't close our embedding script
  $rawSafe = $raw -replace "</script>", "<\/script>"
  $c0 = if ($d.html -eq "0-INSTALAR.html") { "cur" } else { "" }
  $c1 = if ($d.html -eq "1-AGENTE.html") { "cur" } else { "" }
  $c2 = if ($d.html -eq "2-DAVID.html")  { "cur" } else { "" }
  $c3 = if ($d.html -eq "3-LLM.html")    { "cur" } else { "" }
  $page = $head
  $page = $page.Replace("__TITLE__", $d.title)
  $page = $page.Replace("__ACCENT__", $d.accent)
  $page = $page.Replace("__C0__", $c0).Replace("__C1__", $c1).Replace("__C2__", $c2).Replace("__C3__", $c3)
  $page = $page.Replace("__MD__", $rawSafe)
  $outPath = Join-Path $htmlDir $d.html
  [System.IO.File]::WriteAllText($outPath, $page, [System.Text.UTF8Encoding]::new($false))
  Write-Output ("OK -> " + $d.html)
}

# index page
$index = @'
<!DOCTYPE html><html lang="pt-PT"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Caixa Inspetora &mdash; Toolkit</title>
<style>
*{box-sizing:border-box}
body{margin:0;background:#0f1117;color:#c9d1e0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.6}
.wrap{max-width:760px;margin:0 auto;padding:48px 22px}
h1{color:#fff;font-size:28px;border-bottom:2px solid #4f9eff;padding-bottom:.3em}
p.sub{color:#8a97ab}
.card{display:block;text-decoration:none;background:#161b24;border:1px solid #252d3d;border-left-width:4px;border-radius:10px;padding:18px 20px;margin:16px 0;transition:transform .12s,border-color .12s}
.card:hover{transform:translateX(4px)}
.card h2{margin:0 0 6px;font-size:18px;color:#fff}
.card p{margin:0;color:#aab6c8;font-size:14px}
.c0{border-left-color:#a78bfa}.c0:hover{border-color:#a78bfa}
.c1{border-left-color:#4f9eff}.c1:hover{border-color:#4f9eff}
.c2{border-left-color:#3dd68c}.c2:hover{border-color:#3dd68c}
.c3{border-left-color:#f5a623}.c3:hover{border-color:#f5a623}
.who{display:inline-block;font-size:11px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;border-radius:5px;padding:2px 8px;margin-bottom:8px;color:#000}
.w0{background:#a78bfa}.w1{background:#4f9eff}.w2{background:#3dd68c}.w3{background:#f5a623}
.start{display:inline-block;font-size:11px;color:#a78bfa;border:1px solid #a78bfa;border-radius:5px;padding:1px 7px;margin-left:8px;vertical-align:middle}
small{color:#5c6a80}
</style></head><body><div class="wrap">
<h1>&#128300; Caixa Inspetora &mdash; Toolkit</h1>
<p class="sub">Implementar e usar a caixa inspetora ("Projeto Observ&aacute;vel") em ficheiros HTML.</p>
<a class="card c0" href="0-INSTALAR.html"><span class="who w0">Para o David</span><span class="start">COME&Ccedil;A AQUI</span><h2>0 &middot; Instalar (passo-a-passo)</h2><p>O que fazer e o que dar a um agente para instalar a caixa num HTML. Inclui checklist e resolu&ccedil;&atilde;o de problemas.</p></a>
<a class="card c2" href="2-DAVID.html"><span class="who w2">Para o David</span><h2>2 &middot; Manual de Utiliza&ccedil;&atilde;o</h2><p>Depois de instalada: como abrir, as 4 abas (Data/Logic/Layout/Pick) e o fluxo para validar a arquitetura. Sem c&oacute;digo.</p></a>
<a class="card c1" href="1-AGENTE.html"><span class="who w1">Para o agente</span><h2>1 &middot; Implementar a Caixa Inspetora</h2><p>Script + instru&ccedil;&otilde;es + c&oacute;digo pronto-a-colar (CSS/HTML/JS) para um agente LLM injetar a caixa num HTML.</p></a>
<a class="card c3" href="3-LLM.html"><span class="who w3">Para um LLM</span><h2>3 &middot; Manual da Funcionalidade</h2><p>Refer&ecirc;ncia sem&acirc;ntica: o que a caixa &eacute;, v&ecirc; e n&atilde;o v&ecirc;; inten&ccedil;&atilde;o vs. facto; como responder a pedidos.</p></a>
<p><small>Vers&atilde;o de refer&ecirc;ncia: projetos-curador-v3O.html &middot; Os .md originais est&atilde;o na pasta-m&atilde;e inspector-toolkit\.</small></p>
</div></body></html>
'@
$idxPath = Join-Path $htmlDir "index.html"
[System.IO.File]::WriteAllText($idxPath, $index, [System.Text.UTF8Encoding]::new($false))
Write-Output "OK -> index.html"
Write-Output "DONE"
