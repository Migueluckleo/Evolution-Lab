import json,re
from pathlib import Path
ROOT=Path('/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado')
RUN=ROOT/'graphify-out/runs/2026-10-13-web-components'
old=json.loads((RUN/'before/graph.json').read_text());oldnodes={n['id']:n for n in old['nodes']}; oldids=set(oldnodes)
chunks={i:{'nodes':[],'edges':[],'hyperedges':[],'input_tokens':0,'output_tokens':0,'usage_status':'UNAVAILABLE'} for i in [0,1]}
files={i:json.loads((RUN/f'chunk-{i:02}.files.json').read_text()) for i in chunks}
byfile={}
for n in old['nodes']:
 p=Path(n.get('source_file',''));p=p if p.is_absolute() else ROOT/p
 byfile.setdefault(str(p),[]).append(n)
def stem(f):return re.sub('[^a-z0-9]','_',str(Path(f).relative_to(ROOT).with_suffix('')).lower())
def node(c,f,entity,label,kind='concept',rationale=None,**attrs):
 n={'id':stem(f)+'_'+re.sub('[^a-z0-9]','_',entity.lower()),'label':label,'file_type':kind,'source_file':f,'source_location':None,'source_url':None,'captured_at':None,'author':None,'contributor':None}
 if rationale:n['rationale']=rationale
 n.update(attrs);chunks[c]['nodes'].append(n);return n['id']
def edge(c,f,a,b,rel='references',confidence='EXTRACTED',score=1.0):
 e={'source':a,'target':b,'relation':rel,'confidence':confidence,'confidence_score':score,'source_file':f,'source_location':None,'weight':1.0}
 if e not in chunks[c]['edges']:chunks[c]['edges'].append(e)
def oldtarget(path):
 ns=byfile.get(str(path),[])
 ns=sorted(ns,key=lambda n:(n.get('_origin')!='semantic', n.get('file_type')!='document', not n['id'].endswith('_document'), 'artifact' in n['id']))
 return ns[0]['id'] if ns else None
# The top-level documents retain their still-supported historical semantic entities.
removed={'readme_versi_n_operativa_integrada_0_2_4_verificada_documentalmente'}
for rel in ['AGENTS.md','README.md','CHANGELOG.md']:
 f=str(ROOT/rel);kept=set()
 for n in old['nodes']:
  if n.get('source_file')==rel and n.get('_origin')=='semantic' and n['id'] not in removed:
   k={a:v for a,v in n.items() if a not in ['_origin','community','community_name','norm_label','source_location']};k['source_file']=f;k['source_location']=None
   if n['id']=='agents_document':k['label']='AGENTS · SDD protocols 0.3.0'
   chunks[0]['nodes'].append(k);kept.add(k['id'])
 for e in old['links']:
  if e.get('source_file')==rel and e['source'] in kept and e['target'] not in removed and e['target'] in oldids:
   k={a:e.get(a) for a in ['source','target','relation','confidence','confidence_score','weight']};k.update(source_file=f,source_location=None)
   if k['confidence']=='EXTRACTED':k['confidence_score']=1.0
   chunks[0]['edges'].append(k)
f=str(ROOT/'AGENTS.md')
p07=node(0,f,'p07','P07 · código, tipos, documentación y ejemplo obligatorio por componente','rationale','La solicitud DEC-WEB-COMPONENTS-001 activa la biblioteca React/TypeScript/Tailwind/Next.js y sustituye la previsión Vite. El alcance es local y no autoriza backend, publicación remota ni aprobación visual ficticia.')
edge(0,f,'agents_document',p07);edge(0,f,p07,'agents_separate_states','conceptually_related_to');edge(0,f,p07,'agents_p_slots','references');edge(0,f,p07,'agents_continuous_sync','references')
f=str(ROOT/'README.md')
n=node(0,f,'paquete_0_3_0','Paquete operativo 0.3.0: destino web local','rationale','El repositorio integra documentación, implementaciones Figma y biblioteca web de 43 familias. P07 exige mantener código/documento/ejemplo en altas y modificaciones; pnpm --dir implementations/web dev sirve el catálogo local.')
edge(0,f,'readme_document',n);edge(0,f,n,p07)
f=str(ROOT/'CHANGELOG.md')
n=node(0,f,'web_componentes_0_3_0','Entrega 0.3.0: 43 familias, 64/72 Logos y sin backend','rationale','La autorización explícita y versiones estables compatibles fijadas activan Next.js y sustituyen Vite. No cambian datos canónicos, aprobaciones visuales o Figma. Ocho Logos siguen pendientes por límite de consultas y la retención anterior de derivados se conserva.')
edge(0,f,'changelog_document_md',n);edge(0,f,n,p07)
# Cross-cutting implementation guide, with separate, evidence-bound decisions.
f=str(ROOT/'implementations/web/README.md')
readmedoc=node(0,f,'document','Biblioteca web local · guía de 43 familias','document', 'Código copiable, API/defaults/composición/fuentes/límites y pantalla Documentos que busca, filtra y agrega datos en memoria. Recargar restaura las muestras; no hay persistencia de producto.')
meta=[
('runtime_fijado','Stack fijado y runtimes verificados','Next 16.4.0, React/React DOM 19.3.0, Tailwind 4.3.3, TypeScript 7.0.2. Verificado con Node 24.19.0, pnpm 11.25.0 y Chrome; dependencias locales, no instalación global.'),
('ejecucion_local','Desarrollo Next y exportación estática por HTTP','pnpm --dir implementations/web install --frozen-lockfile y dev; build produce out, servido mediante python3 -m http.server. file:// no resuelve rutas de Next. No se publica paquete npm ni despliegue.'),
('consumo_local','Consumo mediante src/index y styles.css','@/index es alias del barrel del catálogo. Copiar componentes/lib/generated/index/styles y public/assets permite consumir en otro Next; adaptar alias, rutas /assets y @source de Tailwind si quedan fuera del árbol de escaneo.'),
('frontera_cliente','Datos serializables y callbacks en Client Components','Server Components pueden suministrar datos serializables; estado y callbacks pertenecen a Client Components. Los módulos interactivos incluyen use client. No hay reglas fiscales, permisos, subida remota o respuestas IA simuladas.'),
('cobertura_obligatoria','P07: registro, export, ejemplo, regeneración y verificación','Alta/modificación exige contrato vigente/enmiendas, código/export, ejemplo identificado, registro/fuentes/Slots y ds:generate. El generador consulta scripts/ds y falla por familia sin mapeo/export/ejemplo, hashes desactualizados o documentos sin regenerar. verify y test:browser registran alcance; P05 cierra grafo.'),
('limites_assets_qa','43 APIs iniciales y assets Logos parciales','64/72 Logos disponibles por límite de Figma; src acepta archivo explícito y no sustituye faltantes silenciosamente. La compilación no certifica todas las variantes, equivalencia pixel a pixel ni WCAG integral; excepciones originales siguen vigentes.')]
metaids={}
for ent,label,rat in meta:
 k=node(0,f,ent,label,'rationale',rat);metaids[ent]=k;edge(0,f,readmedoc,k)
edge(0,f,metaids['cobertura_obligatoria'],p07)
f=str(ROOT/'implementations/web/docs/WEB-ADAPTATION.md')
adoc=node(0,f,'document','Adaptación técnica web 0.1.0 · IMPLEMENTED_FOR_LOCAL_PROTOTYPING','document','Decisiones técnicas DERIVED de DEC-WEB-COMPONENTS-001; no cambia aprobación/auditoría visual. La API TypeScript es el único propietario editable de props y defaults; fichas derivadas enlazan fuentes mediante hashes.')
adapt=[
('autoridad_api','API en código y fuentes en registro, sin duplicar valores canónicos','components.registry.json registra fuentes/notas y aplicabilidad de Slots. ReactNode, children y listas con IDs permiten variar contenido pero no prueban Slots Figma. Cantidades de muestra no son máximos; porcentajes explícitos del gauge sí se conservan.'),
('tokens_aliases','Variables CSS conservan aliases, modos e identidad','tokens.py lee inventario y extensiones enumeradas. tokens.manifest conserva hashes/nombres/tipos/modos/valores/aliases/description. / se convierte a - en --ds; primitivas internas --ds-primitive; componentes consumen roles semánticos. Cuatro temas y character-identity/character-shadow fijos, Logos original; JSON histórico intacto.'),
('unidades_tipograficas','FLOAT a px y pesos Manrope locales','Geometría, line-height y letter-spacing se traducen numéricamente a px; tight -0.01 queda -0.01px sin certificar equivalencia perceptual. Pesos STRING se traducen a 400/500/600/700. Medidas literales contractuales no crean tokens canónicos.'),
('altura_controles','Altura 32/40/48 sin duplicar padding de auto-layout','Button, FilterChip y campos centran contenido en altura; padding vertical no se suma en CSS. Texto envuelto puede crecer sin inventar truncamiento. InputField conserva helper a 4px.'),
('eventos_locales','Controles locales sin semántica de backend','Button usa type=button; Checkbox/Radio/Toggle usan semántica nativa. Toggle Mixed emite callback independiente sin resolver selección agregada. Campos reciben status externo. FileUpload entrega Files; accept es ayuda del selector y no validación.'),
('accesibilidad_html','Dialog, combobox y tooltip tienen límites explícitos','Modal usa showModal/cancel/close y onOpenChange sin cierre de backdrop. Select agrega teclado/cierre local; required solo ARIA. Tooltip hover/focus/Escape no controlado, wrapper tabIndex para disparador no interactivo, sin colisiones automáticas.'),
('adaptacion_datos','Tabla alineada, barra nativa y loader reducido','Table evita desplazamiento hover histórico TABLE-AUD001. Scrollbar deja thumb proporcional al navegador/sistema. Loader rotación CSS respeta prefers-reduced-motion sin inferir tiempo de carga.'),
('graficos_estaticos','Geometría estática no representa motor analítico','ProgressChartItem mantiene fills 580/247px recortados; value es texto, no cálculo. Gauge usa paths originales 25/50/75. Datos continuos requerirían decisión contractual.'),
('layout_web','Overflow local y mínimos desktop explícitos','ChatToolbar agrega overflow central; ChatSection aplica enmienda de layout. AppShell mínimo 1024px es decisión de muestra, no breakpoint de producto. Catálogo admite navegación compacta a 390px y scroll para componentes anchos.'),
('glifo_conversation','Conversation escala fotograma local en vez de glifo reducido original','Conserva identidad mediante primer fotograma Characters reducido, con diferencia explícita respecto de dibujo Conversation. Marca/marco del catálogo y backdrop son composición de herramienta, no variantes del DS.'),
('assets_procedencia','Assets originales y cobertura 64/72 Logos','Manifiesto registra IDs/hashes/formatos originales; ocho ausentes por cuota Figma. Characters reutiliza 13 árboles vectoriales y transformaciones, EmptyStates seis SVG locales con roles semánticos, Avatar foto original base64. No se promete vector para PNG.'),
('alcance_verificacion','QA por alcance sin WCAG integral ni aprobación visual','Prueba automática de accesibilidad cubre catálogo con InputField y excluye contraste por excepciones conocidas; no certifica 43 familias. Avatar/Toggle/Tooltip/Logos conservan excepciones y no se altera color para superar contraste.')]
adids={}
for ent,label,rat in adapt:
 k=node(0,f,ent,label,'rationale',rat);adids[ent]=k;edge(0,f,adoc,k)
edge(0,f,adoc,p07);edge(0,f,adids['tokens_aliases'],'agents_canonical_tokens');edge(0,f,adids['tokens_aliases'],'agents_character_identity')
# Component docs: API contracts are local code-facing documents, not approved design contracts.
apiids={};docids={};slotids={};behaviorids={};exampleids={}
componentfiles=[(c,f) for c in [0,1] for f in files[c] if '/docs/components/' in f and not f.endswith('/README.md')]
for c,f in componentfiles:
 t=Path(f).read_text();name=t.split('\n')[0].removeprefix('# ').split(' · ')[0];fid=re.search(r'Familia `([^`]+)`',t).group(1);slug=Path(f).stem
 notes=t.split('## Uso sin backend\n\n')[1].split('```tsx')[0].strip()
 api=t.split('## API tipada')[1].split('```tsx\n')[1].split('```')[0].strip()
 defaults=t.split('## Defaults y eventos')[1].split('```tsx\n')[1].split('```')[0].strip()
 composition=t.split('## Composición y Slots')[1].split('## Estilos')[0].strip()
 status=re.search(r'P-SLOTS: \*\*(\w+)\*\*',composition).group(1)
 example=t.split('## Uso sin backend')[1].split('```tsx\n')[1].split('```')[0].strip()
 # Preserve documented interface/defaults as source evidence; code owns the editable definition.
 d=node(c,f,'document',name+' · ficha técnica React/TypeScript 0.1.0','document', 'Familia '+fid+'. Documento derivado de API en código, ejemplo ejecutable y notas del registro; no concede aprobación del contrato visual.',family_id=fid,implementation_status='INITIAL_LOCAL_API')
 a=node(c,f,'api_tipificada',name+' · props, defaults y callbacks locales','concept','Tipos y defaults extraídos del código; atributos React heredados y callbacks pertenecen a la pantalla. No atribuyen autorización, carga, guardado o resultados de negocio.',api_types=api,defaults=defaults)
 b=node(c,f,'comportamiento_y_limites',name+' · comportamiento local y límites','rationale',notes)
 s=node(c,f,'slots_web',name+' · P-SLOTS '+status,'rationale',composition,slots_status=status)
 x=node(c,f,'ejemplo_ejecutable',name+' · ejemplo compilado sin backend','concept','Ejemplo de examples.tsx con estado de React en memoria cuando aplica; recargar restaura muestra. Sin endpoint, credencial ni persistencia implícita.',example_source=example)
 srcs=[]
 for href,digest in re.findall(r'\]\(([^)]+)\) · SHA-256 `([0-9a-f]{64})`',t):
  path=(Path(f).parent/href).resolve();srcs.append({'path':str(path.relative_to(ROOT)),'sha256':digest})
 p=node(c,f,'fuentes_y_alcance',name+' · fuentes con hashes y enmiendas acotadas','rationale','Fuentes contractuales y enmiendas sustituyen solo alcance explícito; aprobación/auditoría/excepciones permanecen en fuentes. API inicial no certifica identidad pixel a pixel ni conformidad WCAG. QA identifica alcance y límites.',cited_sources=srcs)
 for target in [a,b,s,x,p]:edge(c,f,d,target)
 edge(c,f,d,adoc);edge(c,f,s,adids['autoridad_api']);edge(c,f,x,metaids['frontera_cliente'])
 for src in srcs:
  target=oldtarget(ROOT/src['path'])
  if target:edge(c,f,p,target,'cites')
 apiids[slug]=a;docids[slug]=d;slotids[slug]=s;behaviorids[slug]=b;exampleids[slug]=x
# Index coverage references only docs actually created here; remaining five links kept as cited paths.
f=str(ROOT/'implementations/web/docs/components/README.md')
idx=node(0,f,'document','Índice técnico web de 43 familias','document','Cada ficha contiene API, ejemplo ejecutable, Slots, fuentes y límites; se genera desde implementación local. No es un listado de contratos aprobados.',cited_paths=[m for m in re.findall(r'\]\(([^)]+)\)',Path(f).read_text())])
for k,d in docids.items():edge(0,f,idx,d)
edge(0,str(ROOT/'implementations/web/README.md'),readmedoc,idx);edge(0,str(ROOT/'implementations/web/README.md'),readmedoc,adoc)
edge(0,str(ROOT/'README.md'),'readme_document',readmedoc);edge(0,str(ROOT/'CHANGELOG.md'),'changelog_web_componentes_0_3_0',readmedoc)
# Explicit compositional example relationships among documented API families.
examples={
'app-shell':['header','logos','sidebar','metric-card'],
'chat-history-item':['icon-button'],
'chat-section':['conversation'],
'chat-toolbar':['chat-tool-item','chat-history-item'],
'conversation':['badge'],
'empty-states':['button'],
'header':['logos','icon-button','avatar'],
'modal':['button','input-field'],
'sidebar':['icon-button'],
'inline-notification':['button'],
'linear-progress-bar':['button'],
'characters':['button']}
for slug,deps in examples.items():
 f=next(f for c,f in componentfiles if Path(f).stem==slug);c=next(c for c,fp in componentfiles if fp==f)
 for dep in deps:edge(c,f,exampleids[slug],apiids[dep],'references')
# Non-obvious semantic links: no claim of code import or behavior equivalence.
similar=[('avatar','loader','La presentación de presencia/carga no acredita estado remoto.'),('dot','icon-button','Counts de contenido literal sin cálculo ni reglas automáticas de notificaciones.'),('file-upload','conversation','Callbacks entregan contenido local sin simular resultado remoto.'),('filter-chip','search','Interacción controlada en componente; datos y filtrado pertenecen a pantalla.'),('metric-card','charts','Contenido visual numérico no implica cálculo/formateo analítico.'),('navigation-tab','navigation-switch-tab-item','Piezas de selección individuales cuyo anfitrión asigna roles y paneles.')]
for a,b,why in similar:
 f=next(f for c,f in componentfiles if Path(f).stem==a);c=next(c for c,fp in componentfiles if fp==f);edge(c,f,behaviorids[a],behaviorids[b],'semantically_similar_to','INFERRED',0.85)
 chunks[c]['edges'][-1]['rationale']=why
# Explicit flexible composition pattern across chat APIs (single hyperedge).
f=next(f for c,f in componentfiles if Path(f).stem=='conversation')
chunks[0]['hyperedges'].append({'id':'implementations_web_docs_components_conversation_regiones_reactnode','label':'Regiones ReactNode variables en composiciones de conversación','nodes':[slotids[x] for x in ['conversation','chat-section','chat-toolbar']],'relation':'implement','confidence':'INFERRED','confidence_score':0.85,'source_file':f})
# Syntax, coverage, confidence and endpoint integrity before emitting derived fragments.
allids=oldids|{n['id'] for v in chunks.values() for n in v['nodes']}
for c,g in chunks.items():
 seen=set()
 for n in g['nodes']:
  assert re.fullmatch('[a-z0-9_]+',n['id']),n['id'];assert n['id'] not in seen,n['id'];seen.add(n['id']);assert n['source_file'] in files[c]
  assert n['file_type'] in ['code','document','paper','image','rationale','concept']
 for e in g['edges']:
  assert e['source'] in allids and e['target'] in allids,e
  assert e['source_file'] in files[c]
  assert (e['confidence']=='EXTRACTED' and e['confidence_score']==1.0) or (e['confidence']=='INFERRED' and e['confidence_score'] in [.95,.85,.75,.65,.55]) or (e['confidence']=='AMBIGUOUS' and .1<=e['confidence_score']<=.3)
 assert set(files[c])=={n['source_file'] for n in g['nodes']},(c,set(files[c])-{n['source_file'] for n in g['nodes']})
 (RUN/f'chunk-{c:02}.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
 print(c,'nodes',len(g['nodes']),'edges',len(g['edges']),'hyperedges',len(g['hyperedges']),'coverage',len(files[c]))
