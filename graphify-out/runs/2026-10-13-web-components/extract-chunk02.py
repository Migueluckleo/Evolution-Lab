import pathlib,json,re,hashlib
root=pathlib.Path.cwd();run=root/'graphify-out/runs/2026-10-13-web-components';files=json.loads((run/'chunk-02.files.json').read_text());assigned={str(pathlib.Path(f).relative_to(root)):f for f in files};texts={r:pathlib.Path(f).read_text() for r,f in assigned.items()};old=json.loads((run/'before/graph.json').read_text());oldids={n['id'] for n in old['nodes']};art={n['source_file']:n for n in old['nodes'] if n.get('_origin')=='ast'}
# Verify unchanged historical portions from current bytes, never treating old hashes as new-content evidence.
shifts={}
for rel in ['registry/decisions.md','registry/environment.md','registry/implementations.md','registry/qa.md','registry/sources.md']:
 s=texts[rel];p=s.index('\n## ');q=s.index('\n## ',p+1);prior=s[:p]+s[q:];assert hashlib.sha256(prior.encode()).hexdigest()==art[rel]['sha256'];shifts[rel]=(3,s[p:q].count('\n'))
for rel,start in [('references/PROJECT-TOOLING.md','\n## Extensión web'),('templates/component.contract.template.md','Para el destino web, aplicar '),('protocols/03-CONTRACT-SYNTHESIS.md','Para nuevas incorporaciones al DS, ')]:
 s=texts[rel]
 if rel.startswith('references'):prior=s[:s.index(start)].rstrip()+'\n'
 else:
  line=next(x for x in s.splitlines(True) if x.startswith(start));prior=s.replace(line+'\n','');shifts[rel]=(s[:s.index(start)].count('\n')+1,2)
  if rel.startswith('protocols'):prior=prior.replace('**Versión:** 0.2.4','**Versión:** 0.2.3')
 assert hashlib.sha256(prior.encode()).hexdigest()==art[rel]['sha256'],rel
base=['id','label','file_type','source_file','source_location','source_url','captured_at','author','contributor'];ignore=set(base+['_origin','community','community_name','norm_label','sha256','extraction_scope','rationale'])
def shifted(rel,loc):
 if not isinstance(loc,str):return loc
 if ':L' in loc:loc='L'+loc.rsplit(':L',1)[1]
 if re.fullmatch(r'L?\d+(?:-L?\d+)?',loc):
  cut,off=shifts.get(rel,(0,0));return 'L'+'-L'.join(str(n+off if n>=cut else n) for n in map(int,re.findall(r'\d+',loc)))
 return loc
g={'nodes':[],'edges':[],'hyperedges':[],'input_tokens':0,'output_tokens':0,'usage_status':'UNAVAILABLE'}
for n in old['nodes']:
 rel=n.get('source_file','')
 if rel in assigned and n.get('_origin')!='ast':
  z={k:n.get(k) for k in base};z['source_file']=assigned[rel];z['source_location']=shifted(rel,z['source_location']);rat=n.get('rationale','');extra={k:v for k,v in n.items() if k not in ignore}
  if extra:rat+=((' ' if rat else '')+'Preserved source attributes: '+json.dumps(extra,ensure_ascii=False,sort_keys=True)+'.')
  if rat:z['rationale']=rat
  g['nodes'].append(z)
for e in old['links']:
 rel=e.get('source_file','')
 if rel in assigned and e.get('_origin')!='ast':
  z={k:e.get(k) for k in ['source','target','relation','confidence','confidence_score','source_file','source_location','weight']};z['source_file']=assigned[rel];z['source_location']=shifted(rel,z['source_location']);g['edges'].append(z)
kept=(len(g['nodes']),len(g['edges']))
# Same existing semantic identities now describe the current protocol revision read above.
patch={
'protocols_01_environment_and_tools_frontend_stack':('React + TypeScript + Tailwind CSS + Next.js para el destino web autorizado','P01 §5: DEC-WEB-COMPONENTS-001 and P07 replace the Vite/Storybook projection for this web layer. Storybook is not additional required work. Task authorizes necessary pinned compatible local dependencies, not global changes. Record actual versions, package manager, tokens, units, fonts, tests, accessibility, browsers and commands.','§5'),
'protocols_01_environment_and_tools_document':('P01 Entorno y herramientas v0.3.0','Current protocol version read from source; capability-specific verification and authorization rules remain.','L3'),
'protocols_03_contract_synthesis_p03_contract_synthesis_v0_2_3':('P03 Contract Synthesis v0.2.4','Stable existing semantic identity retained across current protocol revision. P07 adds web implementation/documentation/example requirements without silently approving visual or business rules.','L3'),
'protocols_06_qa_and_validation_document':('P06 QA documental e implementación v0.2.4','Separate CONTRACT_REVIEW and IMPLEMENTATION_REVIEW; neither grants human approval. Web now activated under DEC-WEB-COMPONENTS-001/P07; keyboard/accessibility cannot be validated from Figma screenshots.','L1')}
for n in g['nodes']:
 if n['id'] in patch:n['label'],n['rationale'],n['source_location']=patch[n['id']]
new={};owners={}
def norm(x):return re.sub('[^a-z0-9]','_',x.lower())
def loc(rel,needle):assert needle in texts[rel],(rel,needle);return 'L'+str(texts[rel][:texts[rel].index(needle)].count('\n')+1)
def add(key,rel,label,why,needle,typ='concept'):
 id=norm(str(pathlib.Path(rel).with_suffix('')))+'_'+norm(label);assert id not in oldids and id not in new.values(),id
 g['nodes'].append({'id':id,'label':label,'file_type':typ,'source_file':assigned[rel],'source_location':loc(rel,needle),'source_url':None,'captured_at':None,'author':None,'contributor':None,'rationale':why});new[key]=id;return id
def edge(a,b,rel,relation='references',needle=None,confidence='EXTRACTED',score=1.):
 g['edges'].append({'source':new.get(a,a),'target':new.get(b,b),'relation':relation,'confidence':confidence,'confidence_score':score,'source_file':assigned[rel],'source_location':loc(rel,needle) if needle else None,'weight':1.})
D='registry/decisions.md';E='registry/environment.md';I='registry/implementations.md';Q='registry/qa.md';S='registry/sources.md';T='references/PROJECT-TOOLING.md';P='protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md';V='qa/implementations/web.v0.1.0.review.md';CSS='implementations/web/src/styles.css';CAT='implementations/web/src/app/catalog.css';LOCK='implementations/web/pnpm-lock.yaml';WORK='implementations/web/pnpm-workspace.yaml';TPL='templates/component.contract.template.md'
add('decision',D,'DEC-WEB-COMPONENTS-001','Explicit user authorizes code and technical documentation for each DS component, reusable screen design without Figma/backend, React/TypeScript/Tailwind/NextJS, compatible stable versions and permanent documentation obligation for new components. Local library/examples/catalog/dependencies only; replaces Vite projection for web, not visual authority. No backend/global install/publication/Figma changes. Eight unexported Logos variants remain recorded.','## DEC-WEB-COMPONENTS')
edge('registry_decisions_registro_de_decisiones','decision',D,needle='## DEC-WEB-COMPONENTS')
add('p07',P,'P07 Componentes web y documentación técnica v0.1.0','New authorized web destination independent of backend and Figma consumption. New components and modifications require reusable code plus technical documentation; images/snippets/empty sheets insufficient. Obligation does not authorize design/backend/publication/global installation.','# P07','document')
for key,label,why,needle in [
('web_sources','Fuentes canónicas y autoridad por destino','Identify base/amendments/canonical data/dependencies by identity and hashes. Visual contracts and referenced token JSON govern; preserve character/logo exceptions. Prior Figma-only scope remains historical; web is newly authorized, not retroactive validation. Keep contract approval, human audit, Figma QA and web QA separate.','## 2.'),
('web_technical','Adaptaciones técnicas explícitas con ambigüedad limitada','Record exports/props/CSS units/HTML/events as technical decisions; material design/business ambiguity blocks only affected portion without inventing intent/assets/visual states/services.','Resolver como decisiones'),
('web_minimum','Entregable web mínimo por familia','Reusable typed React export, contract-supported variants/sizes, canonical-derived CSS variables preserving aliases/logical names, Tailwind composition, technical import/props/defaults/content/events/dependencies/tokens/limits/source documentation, runnable copyable fictitious-data example without credentials/auth/API, and scoped verification. Build alone does not certify visual fidelity/all variants/accessibility.','## 3.'),
('web_coverage','Cobertura vinculada de export ficha ejemplo y catálogo','initial code/catalog in implementations/web; README documents actual execution/consumption commands. Coverage fails without family export/catalog/document; consumable internal components also documented.','La implementación inicial'),
('web_slots','Composición React como equivalente web de Slots','P-SLOTS per family; children/ReactNode/stable-ID typed collections are explicit web equivalents, not native Figma Slots. Test insertion/removal/reorder as applicable; demo quantity not product maximum.','## 4.'),
('web_local','Presentación y estado de demostración separados de negocio','Prefer controlled props/callbacks; local file/selection/navigation/form/message actions never fake remote success. No unsolicited backend/persistence/business logic. Appropriate browser HTML semantics, names/focus/keyboard/disabled/messages. Preserve recorded color limits rather than recolor to pass tests.','Separar presentación'),
('web_stack','Next Client Components y versiones locales fijadas','Next/React/TypeScript/Tailwind versions pinned compatibly in package/lockfile, dependencies local. Client boundaries for browser state/events, catalog can static-export/local-serve without product backend. Fonts/icons/assets retain provenance/geometry/colors; missing asset remains real limit.','## 5.'),
('web_gate','Gate por familia con build interacción navegador y trazabilidad','Check exports/types/docs/examples against base/amendments; regenerate token/metadata hashes and coverage without modifying canonical sources; typecheck/build/affected interaction/consumers; inspect variants/long content/slots/theme/documented widths in browser. Record actual scope/limits and Graphify closure, excluding dependencies/build/cache/redundant generated outputs. No ready web status if applicable deliverables/checks missing; does not invalidate historical Figma automatically.','## 6.')]:
 add(key,P,label,why,needle,'rationale');edge('p07',key,P,needle=needle)
edge('p07','decision',P,'cites',needle='[DEC-WEB');edge('decision','p07',D,'cites',needle='[P07]')
add('qa',V,'QA-WEB-COMPONENTS-001 biblioteca local 0.1.0','PASS_WITH_DOCUMENTED_LIMITS for initial code/docs/compilation/local journeys; IMPLEMENTED_FOR_LOCAL_PROTOTYPING, not globally visual VALIDATED or Figma-contract approval.','# QA-WEB','document')
for key,label,why,needle in [
('qa_sources','43 familias y 32 fuentes de tokens preservadas','Read contracts/amendments via registry/owners, 43 typed families with semantic styles/local composition/Next catalog/document screen. Figma read-only logos export. Approved token inventory SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474 unchanged; fichas preserve source hashes.','## Fuentes'),
('qa_checks','QA web ejecutado con pruebas y build de alcance local','Source reports ds:generate/check coverage coherent 43; pnpm verify strict TS/7 unit tests/static Next build PASS; browser 6 Chrome tests PASS; stale ficha mutation rejected exit1/restored by hash; documentary tooling21/21 PASS. ds check docs-only remains separate pre-graph-publication gate, not inferred from web build.','## Comprobaciones'),
('qa_browser','Recorridos locales de 43 ejemplos temas y composición','Source reports no pageerrors/broken images for43 examples, checkbox/toggle/keyboard select/tabs/dialog Escape+focus return, local file selection, memory message, four themes fixed character fill, screen create/search/reload reset,390px catalog without horizontal overflow, Button32/40/48.','Pruebas de navegador'),
('qa_access','Axe limitado a catálogo e InputField sin color contrast','Zero violations in catalog+InputField with color-contrast disabled for source exceptions; not extrapolated to other families/contrast/integral WCAG. Catalog tabs support arrows/Home/End.','Axe:'),
('qa_corrections','Correcciones deterministas y blanco geométrico de EmptyStates','Source reports corrected Button/FilterChip height, helper gap, ProgressChartItem fixed fill and missing EmptyStates color ref. White masks/clipPaths retained as geometry under REQ-ES-05 with fill/stroke distinctions, no new tokens; final rerun PASS.','Durante verificación'),
('qa_visual','Inspección visual acotada a catálogo y pantalla contable','Desktop/catalog composite screenshots inspected for legibility/no overlap, theme contable1440px. Mobile test only catalog navigation; AppShell/Chat keep desktop/internal overflow limits. No pixel comparison of all variants to Figma.','## Inspección'),
('qa_assets','Logos PARTIAL_ASSETS 64 de 72','Eight assets pending MCP query limit with IDs in manifest; no substitute to fake coverage. Family code/API available, eight asset variants PARTIAL; available assets need no new decision. Historical Avatar/Toggle/Tooltip/Logos exceptions persist.','Logos: 64/72'),
('qa_gate','Graphify CURRENT independiente de build web y condicionado','Graph STALE during lot. Isolated AST update saved and previous nine complete-closure outputs restored by hash; maintained status/prepare/close run 2026-10-13-web-components-v2 must cover docs/CSS/lock/images. CURRENT only closure.json/final check; measured semantics UNAVAILABLE. Prior673 index removals preserved, no commit/push.','## Cierre')]:
 add(key,V,label,why,needle,'rationale' if key not in ['qa_checks','qa_assets','qa_sources'] else 'concept');edge('qa',key,V,needle=needle)
add('qa_slots_correction',V,'Corrección de Slots Select y composición Scrollbar con plan v2','Ficha review corrected Select to REQUIRED for options collection and made Scrollbar viewport children composition explicit. These are web classifications, not Figma mutations. First graph plan retained; v2 prepared with new hashes and only reread or unchanged semantic fragments reused. No closure CURRENT inferred from plan creation.','La revisión de fichas','rationale');edge('qa','qa_slots_correction',V,needle='La revisión de fichas')
edge('qa','p07',V,'cites',needle='[P07]');edge('qa','decision',V,'cites',needle='[DEC-WEB');edge('decision','qa',D,'cites',needle='[QA]')
add('env',E,'Runtime web local y capacidad de exportación parcial','Existing Node24.19.0 at codex-primary-runtime dependencies; pnpm11.25.0, React19.3.0/Next16.4.0/Tailwind4.3.3/TS7.0.2 local in implementations/web. Manrope/Phosphor local, no global updates. Corporate Figma read-only exported64 logos,8 pending query limit. Existing Chrome used; auto-review authorized local Chrome/server after sandbox initially blocked localhost.','## Web')
add('envgate',E,'Corpus web con suplementos exactos y cierre condicionado','Full run 2026-10-13-web-components-v2 keeps prior cut; CURRENT only closure/check confirm hashes/coverage. node_modules/build/public assets/duplicate metadata excluded. Two author CSS and pnpm-lock exact supplements indexed semantically and hash guarded. Semantic usage UNAVAILABLE.','Grafo STALE')
edge('registry_environment_environment_registry','env',E,needle='## Web');edge('env','envgate',E,needle='Grafo STALE');edge('env','decision',E,'cites',needle='[DEC-WEB');edge('env','qa',E,'cites',needle='[Evidencia')
add('impl',I,'IMP-WEB-COMPONENTS-001 API 0.1.0 para prototipos locales','43 families with React export/TS props/styles/tokens/ficha/runnable example and composite local-data screen; IMPLEMENTED_FOR_LOCAL_PROTOTYPING separate from Figma/contract status, not global visual validation. Logos PARTIAL_ASSETS64/72 with8 unmodified/missing IDs, no substitutes; source exceptions remain, publication NOT_REQUESTED, no backend. P07 applies to future additions/modifications.','## IMP-WEB')
edge('registry_implementations_registro_de_implementaciones','impl',I,needle='## IMP-WEB');edge('impl','qa',I,'cites',needle='[QA por alcance]')
add('qareg',Q,'QA-WEB-COMPONENTS-001 registro de resultados por alcance','Source records43 code/API/ficha/examples, TypeScript/7tests/staticbuildPASS,6browserjourneysPASS including backend-free screen/themes, temporary stale-document gate+restore, scoped visual inspection, Logos64/72 partial query limit. No global visual QA/human approval.','## QA-WEB');edge('registry_qa_registro_de_qa','qareg',Q,needle='## QA-WEB');edge('qareg','qa',Q,'cites',needle='[Reporte]')
add('src',S,'SRC-WEB-LOGOS-EXPORT-001 OBSERVED_EXPORT','Read-only export of AI DS file tj3WIBEZDGLVs7MJWKCwgf Logos427:122,64 original PNG/SVG files with IDs/names/format/observed dimensions/hashes;8 explicit pending MCP-limit variants. Temporary download URLs not normative sources; no new approval/geometric Logos QA.','## SRC-WEB')
add('src_assets',S,'Assets web derivados de snapshots originales','Web also reuses original Avatar/EmptyStates/Charts snapshots and local Characters paths; assets.py identifies paths. Contracts and approved JSON retain authority.','La capa web reutiliza','rationale');edge('registry_sources_registro_de_fuentes','src',S,needle='## SRC-WEB');edge('src','src_assets',S,needle='La capa web reutiliza')
add('supplement',T,'supplemental_web_sources limitado a CSS y YAML del destino','Three exact omitted sources: two authored CSS and pnpm-lock. Only CSS/YAML text within implementations/web is accepted; semantic extraction/hash guards required. Generated CSS/tokens/copiedassets/deps/build excluded; no expansion of detector rules for remaining corpus.','## Extensión web','rationale')
# New protocol/template requirements supplement retained historical concepts.
for key,rel,label,needle,why,owner in [
('p03web','protocols/03-CONTRACT-SYNTHESIS.md','P03 mapeo web exige implementación documentación y ejemplo','Para nuevas incorporaciones','P07 requires React/TS/Tailwind/Next implementation/docs/backend-free example for new DS components; DEC-WEB activates existing families. Technical API/local behavior documented by scope cannot silently change visual norms/approve business rules.','protocols_03_contract_synthesis_document'),
('p06web','protocols/06-QA-AND-VALIDATION.md','P06 QA web activado y separado de Figma','La fase web está activada','Apply P07 to per-family code/types/docs/backend-free examples, interactions/accessibility/token consumption/test environment. Figma/React visual equality is additional, not replacement for each destination conformity. No keyboard/accessibility validation from Figma screenshots.','protocols_06_qa_and_validation_document'),
('templateweb',TPL,'Plantilla exige entregables web trazables bajo P07','Para el destino web, aplicar','Editorial template only: capture React export/module, TSprops/defaults/events, variants/tokens/Slots translation/example/catalog docs, typecheck/build/interaction evidence; update registry and regenerate docs. Unknown values not copied from template and no ready web status without deliverables.','templates_component_contract_template_document')]:
 add(key,rel,label,why,needle,'rationale');edge(owner,key,rel,needle=needle);edge(key,'p07',rel,'cites',needle='[P07]')
# Five generated technical sheets: preserve actual API/slots/behavior, not mere headings.
behavior={
'steps':('STEPS-001','Variable total/custom indicators; current/total controlled by screen, presets2–7 not maximum; preserves historical OnPrimary/Gallery roles; no product meaning of step completion.'),
 'table':('TABLE-001','Semantic HTML table with typed columns/cell renderers, no implicit sorting/selection/copy/virtualization/backend. Keeps columns aligned on hover as documented TABLE-AUD-001 adaptation; horizontal overflow for inadequate width.'),
 'textarea':('TEXTAREA-001','counter is consumer text, no implicit300limit; maxLength only if consumer supplies it; resize disabled in this API.'),
 'toggle':('TOGGLE-001','On/Off native switch; Mixed uses mixed checkbox with24x4dash, does not toggle/calculate aggregates. onMixedAction leaves click/empty-group business rule with consumer. Halo AUD-003 exception persists; no full-fidelity claim.'),
 'tooltip':('TOOLTIP-001','Focus/hover opens, Escape hides; align refers to arrow side, not placement side; no viewport collision detection. Avoid interactive children in initial API.')}
for slug,(family,why) in behavior.items():
 rel='implementations/web/docs/components/'+slug+'.md';s=texts[rel];key='sheet_'+slug
 add(key,rel,family+' ficha React TypeScript 0.1.0',why+' Generated by pnpm ds:generate from API/example/registry notes; not new visual-contract approval.','# ','document');owners[rel]=key
 api='\n'.join(re.findall(r'^export interface .+$',s,re.M));defaults=re.search(r'```tsx\n('+slug.title()+r':.*?)\n```',s,re.S)
 if not defaults:defaults=re.search(r'```tsx\n([A-Z]\w+:.*?)\n```',s,re.S)
 add(key+'_api',rel,slug.title()+' API tipada y defaults',api+'\n'+(defaults.group(1) if defaults else '')+' Consumer controls inherited HTML props/callbacks; no business result implied.','## API tipada');edge(key,key+'_api',rel,needle='## API tipada')
 slotline=next(line for line in s.splitlines() if line.startswith('P-SLOTS:'))
 add(key+'_slots',rel,slug.title()+' composición web y Slots',slotline,'## Composición','rationale');edge(key,key+'_slots',rel,needle='## Composición')
 add(key+'_limits',rel,slug.title()+' consumo Next temas y autoridad de fuentes','State/events require use client, serializable data can originate in server components, callbacks created on client boundary. styles.css once from layout with Tailwind4/localManrope/generated token vars; data-ds-theme selects contable/administrativo/servicios/personas, fixed Characters and original Logos. Source contract+amendment hashes govern scoped changes; no pixel identity/integral WCAG claim. Demo in-memory/reload reset, no endpoint/credentials/persistence.','## Estilos','rationale');edge(key,key+'_limits',rel,needle='## Estilos');edge(key,'qa',rel,'cites',needle='[Evidencia de QA]')
# Lockfile and workspace facts from full safe YAML parse, with no claim that locked versions are newest.
add('lock',LOCK,'pnpm lockfile 9.0 con resoluciones fijadas','Single importer ., autoInstallPeers true, excludeLinksFromLockfile false;157 package records and157 snapshots parsed. Integrity/engine/peer/platform/optional records pin actual dependency resolution; no latest-version claim.','lockfileVersion','document')
add('lock_runtime',LOCK,'Dependencias React Next Manrope y Phosphor fijadas','@fontsource-variable/manrope5.3.0, @phosphor-icons/react2.1.10, next16.4.0,react/react-dom19.3.0. Next resolved with React19.3.0/Playwright1.64.0/@types/node26.6.5; next engine>=20.9.0.','    dependencies:');edge('lock','lock_runtime',LOCK,needle='    dependencies:')
add('lock_dev',LOCK,'Herramientas de tipos estilos pruebas y accesibilidad fijadas','Dev locks @axe-core/playwright4.13.0, @playwright/test1.64.0, @tailwindcss/postcss4.3.3, @types/node26.6.5, @types/react19.3.0,@types/react-dom19.3.0,postcss8.5.30,tailwindcss4.3.3,tsx4.23.15,typescript7.0.2. Playwright engine>=20; TS>=16.20.0; esbuild0.28.2>=18.','    devDependencies:');edge('lock','lock_dev',LOCK,needle='    devDependencies:')
add('workspace',WORK,'pnpm workspace permite build de esbuild y excepción postcss','allowBuilds.esbuild true and minimumReleaseAgeExclude includes postcss@8.5.30. These are observed project configuration values, not a separate approval or a claim of package safety.','allowBuilds:','concept');edge('workspace','lock_dev',WORK,needle='minimumReleaseAgeExclude:')
# CSS semantic mechanisms beyond AST imports.
add('styles',CSS,'Estilos DS semánticos con variables canónicas','Tailwind inline theme maps font-sans,surface,subtle,text,muted,brand,border,radius to --ds logical CSS vars. Base body typography/surfaces and components consume semantic tokens. Styles contain fixed geometry and source-compatible shadows; do not infer every literal is tokenized or all variants verified.','@theme inline','document')
for key,label,needle,why in [
('css_controls','Estados de controles y tamaños 32 40 48',' .ds-size-large','Control heights small32/middle40/large48; buttons/chips/iconbuttons use semantic default/hover/active/disabled/pressed roles; chips selected uses inverse role and color-mix hover/active.'),
('css_access','Foco visible y reducción de movimiento',' :focus-visible','2px semantic focus ring with2px offset; hidden important display:none. Native focus/checked/indeterminate/disabled selectors style forms. Loader rotates1.2s but prefers-reduced-motion disables animation.'),
('css_forms','Formularios textarea mixed y roles de feedback',' .ds-field {','Fields max464px; textarea max305px and resize:none; input focus inner/outer effects, status error/success/disabled roles and counter styles. Toggle40x20, mixed dash24x4; semantic native state appearance is stylesheet evidence, not event logic certification.'),
('css_tooltip','Tooltip posición según lado de flecha sin colisión',' .ds-tooltip-anchor','Absolute tooltip max260px and four arrow-position classes using inverse background/text; CSS positioning not collision detection. Align down places bubble above anchor, up below, left right of anchor and right left of anchor.'),
('css_table','Tabla mantiene columnas y permite overflow',' .ds-table-container','Container width100% overflow:auto, table collapse and nowrap, headers/rows semantic background/border. Hover changes row cell background without column geometry changes.'),
('css_layout','Límites desktop de AppShell y Chat explícitos',' .ds-app-shell','AppShell min-width/min-height1024px; chat-section min-width574px, contentmax816px, active733px/content683px with scrollable messages; sidebar and toolbar collapsed/expanded widths. Do not infer universal mobile support from catalog responsiveness.'),
('css_content','Composiciones navegación contenido y modal con variables',' .ds-breadcrumbs','Breadcrumb/current semantics, pagination/current+disabled, switch/navigation tabs selected styles, steps/stepper geometry, avatar fallback/image, character/logo display, empty-state/metric/chart/source-card styles, dialog backdrop/scroll and scrollbar roles. Component classes preserve variable-based presentation; code provides interactions.')]:
 add(key,CSS,label,why,needle,'rationale');edge('styles',key,CSS,needle=needle)
add('catalog_css',CAT,'Catálogo adaptable con navegación y superficie temática','Sticky80px header; desktop264px navigation grid, sticky viewport-height nav with scroll list, semantic surfaces/text/borders/selection. Component previews overflow:auto; code/API panels wrap/scroll; mock-screen composition and metrics use flexible layouts. Skip link moves into view on focus.','.catalog {','document')
add('catalog_breakpoints',CAT,'Breakpoints del catálogo 1100 y 800 px','At<=1100 mainpadding32/24 and heading36px. At<=800 single-column grid, nav hidden unless is-open then fixed264px, menu visible, detail single-column, title/banner stack, preview horizontal overflow retained, filters wrap, heading32/40. These are catalog rules, not blanket component responsive guarantees.','@media(max-width:1100px)','rationale');edge('catalog_css','catalog_breakpoints',CAT,needle='@media(max-width:1100px)')
edge('supplement','styles',T,needle='P07 incorpora');edge('supplement','catalog_css',T,needle='P07 incorpora');edge('supplement','lock',T,needle='P07 incorpora')
edge('sheet_tooltip','css_tooltip','implementations/web/docs/components/tooltip.md','conceptually_related_to',needle='## Estilos',confidence='INFERRED',score=.95)
edge('sheet_table','css_table','implementations/web/docs/components/table.md','conceptually_related_to',needle='## Estilos',confidence='INFERRED',score=.95)
# Existing references only; new cross-chunk targets intentionally left to their owner extraction/AST.
owners.update({P:'p07',V:'qa',D:'decision',E:'env',I:'impl',Q:'qareg',S:'src',T:'supplement',TPL:'templateweb','protocols/03-CONTRACT-SYNTHESIS.md':'p03web','protocols/06-QA-AND-VALIDATION.md':'p06web','protocols/01-ENVIRONMENT-AND-TOOLS.md':'protocols_01_environment_and_tools_document'})
for rel,owner in owners.items():
 s=texts[rel]
 if rel.startswith('registry/'):
  p=s.index('\n## ');s=s[:s.index('\n## ',p+1)]
 for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)',s):
  target=m.group(1).split('#')[0]
  if not target or '://' in target:continue
  p=(root/pathlib.Path(rel).parent/target).resolve()
  try:rr=str(p.relative_to(root))
  except ValueError:continue
  if rr in art:edge(owner,art[rr]['id'],rel,'cites',needle=m.group(0))
# A no-source schema counter is a placeholder, not a measured zero cost.
ids=[n['id'] for n in g['nodes']];assert len(ids)==len(set(ids));known=set(ids)|oldids
for n in g['nodes']:
 assert n['source_file'] in files and re.fullmatch('[a-z0-9_]+',n['id'])
 assert n['file_type'] in ['code','document','paper','image','rationale','concept'] and '_origin' not in n
 assert all(k in n for k in base)
for e in g['edges']:
 assert e['source'] in known and e['target'] in known,(e['source'],e['target'])
 assert e['source']!=e['target'] and e['source_file'] in files
 assert (e['confidence']=='EXTRACTED' and e['confidence_score']==1.) or (e['confidence']=='INFERRED' and e['confidence_score'] in [.95,.85,.75,.65,.55]) or (e['confidence']=='AMBIGUOUS' and .1<=e['confidence_score']<=.3)
for f in files:assert any(n['source_file']==f for n in g['nodes']) and any(e['source_file']==f for e in g['edges'])
assert all(pathlib.Path(assigned[r]).read_text()==s for r,s in texts.items()),'source changed during extraction'
(run/'chunk-02.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(run/'chunk-02.json'),'files':len(files),'nodes':len(g['nodes']),'edges':len(g['edges']),'hyperedges':0,'preserved_node_identities':kept[0],'preserved_edges':kept[1],'current_semantic_records_updated':len(patch),'validation':'PASS schema, identities, endpoints against fragment+before, source coverage/current stability, historical byte checks','usage_status':'UNAVAILABLE'}))
