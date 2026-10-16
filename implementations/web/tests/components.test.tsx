import { test } from 'node:test';
import assert from 'node:assert/strict';
import { renderToStaticMarkup } from 'react-dom/server';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import * as DS from '../src/index';
import { examples } from '../src/generated/example-map';
import { referenceCases } from '../src/variants';
import registry from '../components.registry.json';
import tokens from '../src/generated/tokens.manifest.json';

test('cada familia tiene export y ejemplo renderizable',()=>{
 assert.ok(registry.length>0);
 for(const row of registry){for(const name of row.exports)assert.equal(typeof DS[name as keyof typeof DS],'function',name);const Example=examples[row.slug];assert.ok(renderToStaticMarkup(<Example/>).length>0,row.slug);}
});
test('el inventario canónico y todas las extensiones conservan su hash',()=>{
 for(const [path,sha] of Object.entries(tokens.sources))assert.equal(createHash('sha256').update(readFileSync('../../'+path)).digest('hex'),sha,path);
});
test('no hay referencias CSS a variables DS ausentes',()=>{
 const css=readFileSync('src/styles.css','utf8')+readFileSync('src/app/catalog.css','utf8')+readFileSync('src/generated/tokens.css','utf8')+readFileSync('src/generated/typography.css','utf8');
 const defined=new Set([...css.matchAll(/(--ds-[\w-]+)\s*:/g)].map(m=>m[1]));
 const markup=Object.values(examples).map(Example=>renderToStaticMarkup(<Example/>)).join('')+registry.flatMap(r=>referenceCases(r.slug).map(c=>renderToStaticMarkup(c.content))).join('');
 const used=[...(css+markup).matchAll(/var\((--ds-[\w-]+)/g)].map(m=>m[1]);for(const name of used)assert.ok(defined.has(name),name);
});
test('la identidad de personajes permanece fija y no acepta fotogramas inexistentes',()=>{
 const html=renderToStaticMarkup(<DS.Characters character="beni" label="BENI"/>);assert.match(html,/--ds-color-characters-beni-body/);assert.doesNotMatch(html,/--ds-color-icon-brand/);assert.throws(()=>renderToStaticMarkup(<DS.Characters character="beni" frame={7}/>));
});
test('composición acepta listas vacías y más elementos que la muestra Figma',()=>{
 assert.ok(renderToStaticMarkup(<DS.Table caption="Vacía" rows={[]} columns={[]} rowKey={()=>''}/>).includes('<tbody></tbody>'));
 const items=Array.from({length:9},(_,i)=>({id:String(i),label:String(i)}));
 assert.equal((renderToStaticMarkup(<DS.Breadcrumbs items={items}/>).match(/<li/g)??[]).length,9);
 assert.equal((renderToStaticMarkup(<DS.Steps current={9} total={12} type="gallery-only"/>).match(/<circle/g)??[]).length,12);
});
test('semántica de acciones, progreso y selección agregada',()=>{
 assert.match(renderToStaticMarkup(<DS.Button>Acción</DS.Button>),/type="button"/);
 assert.match(renderToStaticMarkup(<DS.Button href="\/destino" variant="link">Ir</DS.Button>),/^<a /);
 const mixed=renderToStaticMarkup(<DS.Toggle mixed label="Selección parcial"/>);assert.match(mixed,/aria-checked="mixed"/);assert.doesNotMatch(mixed,/role="switch"/);
 assert.match(renderToStaticMarkup(<DS.LinearProgressBar label="Avance" progress={75}/>),/aria-valuenow="75"/);
});
test('assets locales: hashes, existencia y selección explícita',()=>{
 const manifest=JSON.parse(readFileSync('../../sources/assets/web/logos.manifest.json','utf8'));
 assert.equal(DS.logoAssets.length,manifest.assets.length);for(const asset of manifest.assets)assert.equal(createHash('sha256').update(readFileSync('../../'+asset.file)).digest('hex'),asset.sha256);
 assert.throws(()=>renderToStaticMarkup(<DS.Logos assetId="missing" alt="Faltante"/>));
});

test('Table conserva los trazados locales de Sort y Copy',()=>{
 const source=JSON.parse(readFileSync('../../sources/figma-snapshots/table-icons.web-contract-audit.2026-10-13.json','utf8'));
 const paths=(n:{paths?:{data:string}[];children?:unknown[]}):string[]=>[...(n.paths??[]).map(p=>p.data),...(n.children??[]).flatMap(c=>paths(c as Parameters<typeof paths>[0]))];
 for(const [i,type]of (['sort','copy'] as const).entries()){
  const markup=renderToStaticMarkup(<DS.TableGlyph type={type}/>);assert.deepEqual([...markup.matchAll(/ d="([^"]+)"/g)].map(m=>m[1]),paths(source.icons[i]));
 }
});
