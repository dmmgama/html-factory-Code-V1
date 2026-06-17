// build-teste.js — gera MapLab-teste.html = MapLab.html (virgem) + bloco de teste injetado inline.
// A virgem (MapLab.html) NUNCA é tocada e não tem qualquer referência ao bloco.
// Os .md de MapsTeste/ são re-lidos a cada execução (dados frescos).
//
// Uso:  node build-teste.js
//
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const VIRGEM = path.join(ROOT, 'MapLab.html');
const TESTE  = path.join(ROOT, 'MapLab-teste.html');
const SEEDDIR = path.join(ROOT, 'MapsTeste');
const TEMPLATE = path.join(SEEDDIR, 'seed-bloco.template.html');

// 1. Ler os .md do folder e derivar projeto/árvore do nome:  "P1 - A1 -  icloudMap-V3.md"
//    proj = "P1", tree = "A1" (o 2º segmento separado por " - ").
const files = fs.readdirSync(SEEDDIR)
  .filter(f => f.toLowerCase().endsWith('.md'))
  .sort();
if (!files.length) { console.error('Sem .md em MapsTeste/'); process.exit(1); }

const seedData = files.map(fname => {
  const parts = fname.replace(/\.md$/i, '').split(' - ');
  const proj = (parts[0] || '').trim();
  const tree = (parts[1] || '').trim();
  const raw = fs.readFileSync(path.join(SEEDDIR, fname), 'utf8');
  if (!proj || !tree) console.warn('  ⚠ nome inesperado (proj/tree não derivados): ' + fname);
  return { proj, tree, raw, file: fname };
});

console.log('Ficheiros embebidos:');
seedData.forEach(d => console.log(`  ${d.proj} / ${d.tree}  ←  ${d.file}`));

// 2. Construir o bloco a partir do template, injetando o JSON dos dados.
const template = fs.readFileSync(TEMPLATE, 'utf8');
const dataJson = JSON.stringify(seedData.map(d => ({ proj: d.proj, tree: d.tree, raw: d.raw })));
if (!template.includes('__SEED_DATA__')) { console.error('ERRO: __SEED_DATA__ não encontrado no template.'); process.exit(1); }
const bloco = template.replaceAll('__SEED_DATA__', dataJson);

// 3. Injetar o bloco INLINE na virgem, antes de </body>, e escrever a versão teste.
const virgem = fs.readFileSync(VIRGEM, 'utf8');
if (virgem.includes('SEED-TESTE START')) {
  console.error('ERRO: MapLab.html (virgem) contém o bloco de teste! A virgem deve ficar limpa. Aborta.');
  process.exit(1);
}
const idx = virgem.lastIndexOf('</body>');
if (idx === -1) { console.error('ERRO: </body> não encontrado em MapLab.html'); process.exit(1); }
const out = virgem.slice(0, idx) + bloco + '\n' + virgem.slice(idx);
fs.writeFileSync(TESTE, out);

console.log(`\n✔ ${path.basename(TESTE)} gerado (${(out.length/1024).toFixed(0)} KB).`);
console.log('  Virgem intacta:', path.basename(VIRGEM));
