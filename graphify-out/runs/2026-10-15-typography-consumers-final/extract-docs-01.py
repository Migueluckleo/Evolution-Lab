import json,re,hashlib,difflib,copy
from pathlib import Path
ROOT=Path('/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado');RUN=ROOT/'graphify-out/runs/2026-10-15-typography-consumers-final'
read=lambda p:json.loads(Path(p).read_text());sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();norm=lambda s:re.sub('[^a-z0-9]','_',s.lower())
files=read(RUN/'chunk-01.files.json');plan=read(RUN/'source-plan.json')['source_sha256'];before=read(RUN/'before/graph.json')
for f in files: assert sha(f)==plan[Path(f).relative_to(ROOT).as_posix()],f
seed=read(RUN/'seed-01.json');nodes=copy.deepcopy(seed['nodes']);edges=copy.deepcopy(seed['edges']);hyper=[]
existing={n['id']:n for n in before['nodes']}
for p in sorted(RUN.glob('seed-*.json'))+sorted(RUN.glob('chunk-*.json')):
 if re.fullmatch(r'chunk-\d+\.json',p.name) or p.name.startswith('seed-'):
  for n in read(p).get('nodes',[]): existing[n['id']]=n
known=existing.copy();proof=[]
def relative(source):
 p=Path(source)
 return p.relative_to(ROOT).as_posix() if p.is_absolute() else str(p)
def sourcepath(p): return str(ROOT/p)
def location(p,needle):
 lines=(ROOT/p).read_text().splitlines()
 found=[i+1 for i,s in enumerate(lines) if needle in s]
 assert found,(p,needle)
 return 'L'+str(found[0])
def add(p,label,typ='concept',needle=None,**attrs):
 assert sourcepath(p) in files,p
 ident=norm(str(Path(p).with_suffix('')))+'_'+norm(label)
 # Preserve the established document identity referenced by retained external semantics.
 if p=='registry/skills.md' and label=='Versioned consumer skill release registry':ident='registry_skills_document'
 assert ident not in {n['id'] for n in nodes},ident
 node=dict(id=ident,label=label,file_type=typ,source_file=sourcepath(p),source_location=location(p,needle) if needle else None,source_url=None,captured_at=None,author=None,contributor=None,**attrs)
 nodes.append(node);known[ident]=node;return ident
def edge(a,b,p,rel='references',needle=None,confidence='EXTRACTED',score=1.0,**attrs):
 edges.append(dict(source=a,target=b,relation=rel,confidence=confidence,confidence_score=score,source_file=sourcepath(p),source_location=location(p,needle) if needle else None,weight=1.0,**attrs))
def ref(a,target,p,needle=None):
 candidates=[n for n in known.values() if relative(n.get('source_file',''))==target]
 if not candidates:return False
 candidates.sort(key=lambda n:(n.get('_origin')=='ast',not n.get('id','').endswith('typography_consumption_amendment'),n.get('file_type')!='document',n['id']))
 edge(a,candidates[0]['id'],p,'cites',needle);return True
# Retain semantic history only when its exact snapshot hash equals before/graph provenance.
# Structural AST references are deliberately left to the engine's fresh AST supplement.
for p in ['registry/contracts.md','registry/decisions.md','registry/implementations.md','registry/sources.md','registry/DEC-TYPOGRAPHY-STYLES-001.md']:
 old=ROOT/'output/skills/0.2.0/contpaqi-figma-screens/assets/design-system'/p
 artifact=next(n for n in before['nodes'] if n.get('source_file')==p and n.get('_origin')=='ast')
 assert sha(old)==artifact['sha256'],p
 oldlines=old.read_text().splitlines();newlines=(ROOT/p).read_text().splitlines();ops=difflib.SequenceMatcher(None,oldlines,newlines,autojunk=False).get_opcodes();assert all(op[0] in ['equal','insert'] for op in ops),p
 linemap={i+1:k+1+(i-a) for tag,a,b,k,l in ops if tag=='equal' for i in range(a,b)}
 assert len(linemap)==len(oldlines)
 def remap(loc):
  if loc is None:return None
  m=re.fullmatch(r'L(\d+)(?:-L?(\d+))?',str(loc))
  if not m:return None
  a=int(m[1]);b=int(m[2] or a);mapped=[linemap.get(i) for i in range(a,b+1)]
  if not mapped or None in mapped or mapped!=list(range(mapped[0],mapped[-1]+1)):return None
  return 'L'+str(mapped[0])+(('-L'+str(mapped[-1])) if m[2] else '')
 reused_nodes=0;reused_edges=0;null_locations=0
 for n in before['nodes']:
  if n.get('source_file')!=p or n.get('_origin')!='semantic':continue
  v=copy.deepcopy(n)
  for key in ['_origin','community','community_name','norm_label']:v.pop(key,None)
  loc=v.get('source_location');v['source_file']=sourcepath(p);v['source_location']=remap(loc)
  if loc and not v['source_location']:v['historical_source_location']=loc;null_locations+=1
  v['reuse_basis']='Exact historical snapshot SHA matched before/graph provenance; all prior source lines preserved in current file. Current L locations rebased through verified equal diff blocks; null locations remain unspecified.'
  v['historical_snapshot_sha256']=sha(old)
  nodes.append(v);known[v['id']]=v;reused_nodes+=1
 for e in before['links']:
  if e.get('source_file')!=p or e.get('_origin')=='ast':continue
  records=[x for x in e.get('evidence_records',[]) if relative(x.get('source_file',''))==p] or [e]
  for record in records:
   v={k:record[k] for k in ['source','target','relation','confidence','confidence_score'] if k in record}
   for endpoint in ['source','target']:
    if v.get(endpoint) not in existing:v[endpoint]=e[endpoint]
   for key in ['confidence','confidence_score','relation']:v.setdefault(key,e[key])
   v.update(source_file=sourcepath(p),source_location=remap(record.get('source_location')),weight=record.get('weight',e.get('weight',1.0)))
   if record.get('source_location') and not v['source_location']:v['historical_source_location']=record['source_location']
   edges.append(v);reused_edges+=1
 proof.append({'source':p,'historical_snapshot':str(old.relative_to(ROOT)),'historical_sha256':sha(old),'current_sha256':sha(ROOT/p),'before_graph_sha256':artifact['sha256'],'all_prior_lines_identical':True,'insertions':[{'old_at':a+1,'new_start':k+1,'new_end':l} for tag,a,b,k,l in ops if tag=='insert'],'semantic_nodes_retained':reused_nodes,'semantic_evidence_edges_retained_before_dedup':reused_edges,'unresolvable_old_locations_kept_as_history':null_locations})
# MD-only regression and portable deliverable index.
p='qa/skills/release-0.2.1/md-forward-test.md'
md=add(p,'Independent Markdown only forward review','document','Resultado:',result='PASS_MD_ONLY_FORWARD_REVIEW',figma_execution='NOT_RUN',visual_validation='NOT_RUN',package_version='0.2.1',ds_digest='4205fc48bf65ef7f42f3c51f15402d61c7f5e25ae88850f1a50ccd41fb90bc67',rationale='The complete Markdown plus consumer skill snapshot is sufficient to prepare reproduction without demanding external HTML, PNG or handoff JSON.')
mdsrc=add(p,'Verified source and family coverage',needle='Fuentes del traspaso',source_hashes=24,families=43,typography_amendments=43,snapshot_files=2131);edge(md,mdsrc,p,needle='Fuentes del traspaso')
mdscene=add(p,'Recoverable state and instance structure',needle='Cobertura de estado',identities=10,ds_instances=7,ds_families=5,local_nodes=3,states_viewports=14,node_observations=82,text_runs=124,typography_styles=8,viewports=['1440x900','1000x760']);edge(md,mdscene,p,needle='Cobertura de estado')
mdlimit=add(p,'Destination verification still required','rationale','No hay defecto',rationale='figmaTarget is null; actual IDs, bindings and property mappings require authorized destination inspection. Historical DS native proof does not validate a new prototype; this scene has native_inheritance null.');edge(md,mdlimit,p,'references','No hay defecto')
p='qa/skills/release-0.2.1/replicar-en-figma.md'
idx=add(p,'Original complete portable delivery index','document','La [entrega',markdown_sha256='67a733be2561e5d704df4d5d5bdd92e0535c6c5637b8371a01da6d3f25726ce0',archive_sha256='ca8217504e042c212c0cfc5c2382343de544ee79bb57eb673dca62a8e327cc6e',rationale='Links to full original delivery and ZIP preserve relative resources; does not duplicate an isolated Markdown without its folders.');edge(idx,md,p,'conceptually_related_to','La [entrega',confidence='INFERRED',score=0.95)
# Current and historical registry additions; retained lower entries stay historical.
registry_current={}
for p,label,needle,attrs in [
 ('registry/contracts.md','Native typography contract activation 0.1.2','## Tipografía · herencia',{'styles':79,'direct_ranges':3250,'native_ranges':103,'implementation_validation':'VALIDATED_TYPOGRAPHY_SCOPE','audit':'PENDING'}),
 ('registry/decisions.md','Specific native consumption delegation 0.1.2','## DEC-TYPOGRAPHY-STYLES-001 · mecanismo',{'provenance':'EXPLICIT user scope; DERIVED mechanism','contract_status':'DELEGATED_FOR_BUILD','audit':'PENDING','no_remote_publication':True}),
 ('registry/implementations.md','IMP TYPOGRAPHY CONSUMERS 012','## IMP-TYPOGRAPHY-CONSUMERS-012',{'result':'PASS_TYPOGRAPHY_SCOPE','pages':34,'ui_nodes':3351,'ui_ranges':3353,'direct_ranges':3250,'native_ranges':103,'empty_local_style_ids':103,'unresolved_ranges':0,'editorial_preserved':150,'audit':'PENDING','library_publication':'NOT_PUBLISHED','table_nontext_guard':'UNAVAILABLE_TIMEOUT'}),
 ('registry/sources.md','SRC TYPOGRAPHY NATIVE INHERITANCE 012','## SRC-TYPOGRAPHY-NATIVE-INHERITANCE-012',{'catalog_sha256':'074a31a83f09b30a02fa8b8f0a7730bdb33fc0a8a9c59e3c8d2469b5799e934c','inheritance_sha256':'afc4a25f9ca37c48660f6fca159d0d9a66cda5c0a13483a08a4e14d0baaaaa3d','api_routes':242,'pilots':3,'causal_controls':36,'raw_slot_issues_preserved':6,'instance_typographic_overrides':0})]:
 registry_current[p]=add(p,label,'concept',needle,**attrs)
# Entries created for the earlier 0.1.1 step remain explicit historical cuts rather than current blockers.
for p,label,needle,attrs in [
 ('registry/contracts.md','Family consumption catalog 0.1.1 historical cut','## Tipografía · catálogo 0.1.1',{'styles':79,'family_amendments':43,'required_families':39,'not_applicable_families':4,'ui_ranges':3353,'historical_application':'IN_PROGRESS;103blocked','scope':'Superseded by scoped native0.1.2 closure above, not erased.'}),
 ('registry/decisions.md','All component consumption delegation 0.1.1','## DEC-TYPOGRAPHY-STYLES-001 · ampliación',{'underline_styles':4,'underline_ranges':27,'technique':'complete style per range without later formatting setters','historical_application':'IN_PROGRESS;103BLOCKED','audit':'PENDING'}),
 ('registry/implementations.md','IMP TYPOGRAPHY CONSUMERS 011 historical interruption','## IMP-TYPOGRAPHY-CONSUMERS-011',{'historical_status':'PARTIAL / BLOCKED_BY_USAGE_LIMIT','direct_ranges_pass':3250,'native_ranges_pending_then':103,'count_copies_pending_then':2,'scope':'Historical cut resolved by IMP-TYPOGRAPHY-CONSUMERS-012; not current state.'}),
 ('registry/sources.md','SRC TYPOGRAPHY CONSUMPTION 011 frozen evidence','## SRC-TYPOGRAPHY-CONSUMPTION-011',{'styles':79,'family_amendments':43,'ui_ranges':3353,'previous_normative_files':68,'historical_native_blocked':103}),
 ('registry/sources.md','SRC TYPOGRAPHY FORMAT PROBES 011','## SRC-TYPOGRAPHY-FORMAT-PROBES-011',{'decoration_setter_result':'FAIL preserved:140discrepancies after11assignments','range_style_probe':'PASS only Button clone and6TEXT-editable instances','scaled_probes':'historical failures preserved','rationale':'A complete underline TextStyle avoids later decoration setters that break or propagate style links; a bounded clone test does not validate all consumers.'})]:
 n=add(p,label,'concept',needle,**attrs);edge(registry_current[p],n,p,'references',needle)
# Standalone decision retains verified original sections, adds the later explicit extensions.
p='registry/DEC-TYPOGRAPHY-STYLES-001.md'
dec11=add(p,'Expanded all family typography consumption delegation','concept','## Ampliación vigente',families=43,ui_nodes=3351,ui_ranges=3353,editorial_nodes=150,authority='DELEGATED_FOR_BUILD',audit='PENDING',rationale='The later explicit request requires applying styles to every Figma component and documenting assignments in each Spec; ordinary per-family reapproval is not required.')
decformat=add(p,'Formatting derived styles and range setter','rationale','El [piloto con estilos de formato]',underline_styles=4,underline_ranges=27,api='setRangeTextStyleIdAsync(start,end,id)',rationale='Complete styles incorporate UNDERLINE and preserve metrics/bindings. Later formatting setters propagated or detached styles; preserve properties and do not recreate or detach text instances.');edge(dec11,decformat,p,'references','El [piloto con estilos de formato]')
dec12=add(p,'Native linkage delegation 0.1.2','concept','## Ampliación de vínculo',styles=79,changed_descriptions=3,metric_recipes_unchanged=True,consumer_result='VALIDATED_TYPOGRAPHY_SCOPE',direct_ranges=3250,native_ranges=103,human_audit='PENDING',table_nontext_guard='UNAVAILABLE_TIMEOUT');edge(dec12,dec11,p,'references','Las43 enmiendas')
# Resolved interruption is explicitly distinguished from preserved recovery instructions.
p='registry/SESSION-HANDOFF-2026-10-15-TYPOGRAPHY-CONSUMERS.md'
session=add(p,'Typography continuation resolved','document','Continuación resuelta',current_status='RESOLVED_BY_0.1.2',native_ranges_pass=103,count_pilot='A/B/A complete and both copies removed',rationale='Top notice supersedes lower historical interruption; skills and Graphify have separate current registries.')
interrupted=add(p,'Historical usage limit interruption','concept','Estado:',historical_status='PARTIAL / BLOCKED_BY_USAGE_LIMIT',failed_read='Count read-a was not executed due usage review limit; not an insecurity rejection',historical_temporary_roots=['1063:1392','1063:1414'],scope='Historical preserved interruption; current top notice resolves it.');edge(session,interrupted,p,'references','Estado:')
recovery=add(p,'Recorded bounded continuation sequence','rationale','## Reanudación concreta',sequence=['inspect exact two owned roots','read-a/set-b/read-b/restore-a/read-restored/cleanup','verify103 chains and all3pilots','activate explicit amendment and native overlay','synchronize descriptions and web','release bothskills','structural and semantic Graphify closure'],rationale='Resume from evidence without replaying all styles or34captures; preserve original identities, metadata guards and all raw failures.');edge(interrupted,recovery,p,'references','## Reanudación concreta')
slotboundary=add(p,'Select local Options Slot boundary','concept','Select tiene6',api_type='SLOT',slot_property='Options#466:0',local_indices=[5,6,7],raw_outer_missing_routes=6,nearest_checkbox_main_verified=True);edge(recovery,slotboundary,p,'references','Select tiene6')
# Release record is read in full; distinguish three historical versions and current consumer snapshot.
p='registry/skills.md';releases=add(p,'Versioned consumer skill release registry','document','# Releases',authority='DERIVED_CONSUMER_SNAPSHOT; no approval inferred',rationale='Integrity, installation and QA per destination are separate. Effective inputs create a new immutable release; managed install preserves user edits.')
for ver,count,digest,status in [('0.1.0',1373,'05f59b74952cf681ac81049a33c368d49e4fa16656e3dee883424f5650367443','HISTORICAL_CREATED_AND_INSTALLED'),('0.2.0',1694,'f3d8dc4b76c8261d02d60cc708b374c0700d7500400057a219f5fdd7c78d4e56','HISTORICAL_CURRENT_AT_RELEASE_WITH_FIGMA_BLOCKER'),('0.2.1',2131,'4205fc48bf65ef7f42f3c51f15402d61c7f5e25ae88850f1a50ccd41fb90bc67','CURRENT_VERIFIED_RELEASE')]:
 n=add(p,'Consumer skills release '+ver,needle='## '+ver,version=ver,source_files=count,families=43,ds_digest=digest,state_at_record=status,skills=['contpaqi-figma-screens','contpaqi-po-prototypes'],figma_prototype='NOT_RUN');edge(releases,n,p,needle='## '+ver)
 if ver=='0.2.1':rel21=n
relqa=add(p,'Release 0.2.1 bounded offline and install QA',needle='`sync --bump patch`',offline_states=14,instances=10,source_hashes=24,text_runs=124,release_tests=13,handoff_tests=9,export_tests=6,idempotent_release_files=4300,installed_skills=2,previous_skills_preserved=True,visual_images_reviewed=2,figma_prototype='NOT_RUN');edge(rel21,relqa,p,needle='`sync --bump patch`');edge(relqa,md,p,'cites','revisión independiente MD-only')
# Consumer skills: extract actual workflow semantics rather than just linked file names.
roots={}
p='skills/contpaqi-figma-screens/SKILL.md'
roots[p]=add(p,'contpaqi figma screens','document','name:',purpose='Editable Figma product screens from prompts, images or portable Markdown using bundled CONTPAQi specs',master='tj3WIBEZDGLVs7MJWKCwgf',master_access='READ_IMPORT_ONLY',deliverable='real prototype URL/nodes/captures/component map and evidence',rationale='A prototype request authorizes ordinary local composition, not modification or publication of the shared master.')
for label,needle,attrs in [
 ('Local component composition scope','Si falta cobertura',{'missing_coverage':'compose existing components/tokens in prototype only','official_ds_component':False}),
 ('Portable integrity and necessary contract closure','Lee `assets/release.json`',{'verifier':'python3 scripts/verify_snapshot.py','index_authority':'generated locator only','contract_reading':'base, applicable amendments and needed dependencies'}),
 ('Authorized Figma destination','Usa el archivo de prototipo',{'new_file_skill':'figma-create-new-file','missing_target':'prepare mapping then request only required destination','never_default_to_master':True}),
 ('Official tool manual prerequisites','Carga la skill oficial',{'manuals':['figma-use','figma-generate-design','figma-generate-library forlocalcomponents','figma-create-new-file fornewfiles'],'discover_in_runtime':True}),
 ('Editable linked composition and readback','Conserva instancias vinculadas',{'requirements':['linkedinstances','supportedprops','semanticbindings','aliases','officialassets','AutoLayout','editabletext','Slots accordingtocontract'],'validation':'readback plus affected controls, not successful write alone'})]:
 n=add(p,label,'concept',needle,**attrs);edge(roots[p],n,p,needle=needle)
p='skills/contpaqi-figma-screens/references/design-system.md'
roots[p]=add(p,'Portable snapshot authority resolution','document','# Resolver',rationale='Markdown governs rules and JSON only delegated fields; amended scope, not recency, decides precedence. Snapshot integrity does not confer human approval or live Figma availability.')
for label,needle,attrs in [
 ('Portable package identities','Cada componente del índice',{'fields':['id','slug','name','contract','amendments','exports','version','figma'],'null_figma':'locator unavailable, not component absent'}),
 ('Shared typography 0.1.2 authority','Antes de construir',{'catalog':'specs/tokens/ai-design-system.typography.v0.1.2.json','styles':79,'base_for_new_local_text':18,'family_amendments':43,'description_owner':'canonicalJSON'}),
 ('Native scale evidence gate','El catálogo incluye tres recetas',{'metric_recipe_scale':1,'required':['realmainstyle','chain','nativeScale','properties','no incompatible overrides','causalproof'],'forbidden':['assign materializedstyle tonativeinstance','doublescale','acceptemptyIDalone'],'new_destination_validation':'required'}),
 ('Semantic token identity and exact local replicas','Para cada binding necesario',{'record':['logicalname','origin','consumerproperty','mode','realvariable'],'same_rgb_not_same_semantics':True,'replica_scope':'exact dependency closure with collections/modes/aliases and readback'}),
 ('Character identity and official artwork','Para BENI/NAVI',{'characters':['BENI','NAVI'],'collection':'character-identity','fixed_original_colors':True,'semantic_alias':False,'theme_variation':False,'no_generalized_primitive_exception':True})]:
 n=add(p,label,'concept',needle,**attrs);edge(roots[p],n,p,needle=needle)
p='skills/contpaqi-figma-screens/references/figma-workflow.md'
roots[p]=add(p,'Verified editable Figma construction flow','document','# Construcción',rationale='Read actual target identities and scope before sequential recoverable writes; package history is not a real component key or remote variable availability check.')
for label,needle,attrs in [
 ('Import only verified component keys','Importa componentes/sets',{'lookup':'individual function intent scoped to verified CONTPAQi library','distinguish':['nodeID','componentkey','filekey','set','main','instance']}),
 ('Full style range assignment','Para asignaciones directas',{'api':'setRangeTextStyleIdAsync(start,end,id)','immutable_interval_snapshot':True,'load_current_and_target_fonts':True,'no_global_textStyleId_setter':True,'no_later_formatting_setters':True,'preserve':['bindings','propertydefinitions','propertyreferences','characters','geometry','unrelatedoverrides']}),
 ('Native consumer chain validation','Lee antes de construir',{'mapping_history':'0.1.1 blocked entries superseded only by verified overlay','native_instance':'preserve scale and main style, do not force materializedlocalID'}),
 ('Structural Auto Layout and prototype transitions','Usa Auto Layout',{'layout':['width','height','padding','gap','alignment','wrap','clipping'],'connections':'source/event/condition/target/overlay/result readback','browser_parity':'do not promise full keyboard/ARIA/backend equivalence'}),
 ('Recoverable writes and global stability read','Usa lotes recuperables',{'uncertain_write':'read affected area before recreation','validation':'after last affected write, compare interval coverage ifsegmentsmerge; edits of sharedTEXT must not changeotherstyles','temporaries':'remove only identified owned resources'})]:
 n=add(p,label,'concept',needle,**attrs);edge(roots[p],n,p,needle=needle)
p='skills/contpaqi-figma-screens/references/handoff-and-qa.md'
roots[p]=add(p,'Self contained Markdown handoff consumption','document','# Handoff',input='complete pasted or attached entrega/replicar-en-figma.md',schema_version=1,external_html_png_json='optional supplementary evidence',rationale='The embedded JSON and consumer snapshot can supply sources, identity, content and layout without needing access to producer machine.')
for label,needle,attrs in [
 ('Structured instance and local content evidence','`kind: local-content`',{'instance_fields':['instanceId','componentId','exportName','props','tokens','slots','identity','kind'],'local_content':'explicitreason,canonicaltokens,owntext/box/order/style;notofficialDSfamily','measured_structure':['parent_id','order','bounding_box','computed_style','visible','declared_props']}),
 ('Exact source compatibility across releases','Si ambos coinciden',{'same_package_digest':'verify used sources in own snapshot','different_version':'verify bytes of all consumed sources and dependencies','material_difference':'CONFLICT limited to affected decision'}),
 ('Typography marker and native proof limits','La identidad tipográfica viaja',{'marker':'typography_style_id','fragment_measurements':'text_runs','identified_not_conformance':True,'native_destination':'NOT_RUN untilactualchainreadback','underline':'completeformatstyle no later setter'}),
 ('Evidence based per screen acceptance','Por pantalla/estado requerido',{'controls':['identity/editability','components/states','layout/type','bindings','assets','interactions','Slots','visualcomparison'],'optional_external_visual':'NOT_RUN when reference absent','screenshot_not_bindings':True,'write_not_conformance':True}),
 ('Portable final prototype report','Guarda un reporte',{'fields':['package/digest','exactcontracts','realURL/IDs','DS/localcomponents','props/states','captures/readback','measuredQA','differences/limits'],'no_human_approval_inferred':True})]:
 n=add(p,label,'concept',needle,**attrs);edge(roots[p],n,p,needle=needle)
p='skills/contpaqi-po-prototypes/SKILL.md'
roots[p]=add(p,'contpaqi po prototypes','document','name:',stack=['React','TypeScript','Tailwind','Next.js'],deliverables=['entrega/render.html','entrega/replicar-en-figma.md','references','captures'],runtime='client state/hash; serverless finalHTML',default_assumptions={'theme':'Contable','viewport':'1440x900'},rationale='Product prototype consumes versioned DS snapshot without editing master, canonical snapshot or installedskills; Markdown invokes a future Figma session, not current execution.')
for label,needle,attrs in [
 ('Prototype source and derived build separation','Edita `prototype/page.tsx`',{'editable':['prototype/page.tsx','localstyles','brief.json'],'generated':['app/','ui/'],'init':'node scripts/init.mjs new-output','no_backend':True}),
 ('Real interaction and identity instrumentation','Implementa respuestas visibles',{'state':'actualvisibleclientresponses','markers':['DSNode','data-ds-node','contractidentity','props'],'localtexts':'mark localtitles/text/containers too'}),
 ('Offline file capture gate','Compila con `npm run build`',{'commands':['build','capture','handoff'],'test':'renamed isolated file:// withHTTP(S)blocked','scope':['keyboard','returns','longcontent','viewports'],'capture_not_visual_review':True}),
 ('Honest missing browser and Figma limits','Si falta capacidad de navegador',{'missing_browser':'NOT_RUN','failed_execution':'FAIL thenrepair','no_localhost_substitute':True,'figma':'NOT_RUN bythisflow'})]:
 n=add(p,label,'concept',needle,**attrs);edge(roots[p],n,p,needle=needle)
p='skills/contpaqi-po-prototypes/references/design-system.md'
roots[p]=add(p,'Canonical DS consumption for portable prototypes','document','# Consumo',rationale='Consume actual exported components, generatedCSS, assets and contractclosure; Tailwind composes locally without overriding .ds-* or altering recipes.')
for label,needle,attrs in [
 ('Canonical typography classes','Para texto local nuevo',{'class_pattern':'.ds-type-<id>','base_styles':18,'catalog_version':'0.1.2','family_amendments':43,'underline':'consume exact formatting-derived ID'}),
 ('Materialized web versus native Figma scale','Los tres IDs con `derivedFrom`',{'web':'materializedrecipe once,recipeScale=1','figma':'actualmainstyle andnativeScale withproof','handoff':'include amendment andoverlay foraffectedfamilies','not_general_scale':True}),
 ('Themes and character exception','El tema se aplica',{'themes':['contable','administrativo','servicios','personas'],'character_identity':'BENI/NAVI fixed direct character-identity tokens only'}),
 ('Slot applicability and local composition','Revisa Slots por región',{'states':['REQUIRED','NOT_APPLICABLE','UNRESOLVED'],'unbounded_by_example':True,'react_children_not_figma_slots':True,'local_composition':'reason,bases,behavior,limitations withoutlibrarychange'})]:
 n=add(p,label,'concept',needle,**attrs);edge(roots[p],n,p,needle=needle)
p='skills/contpaqi-po-prototypes/references/handoff.md'
roots[p]=add(p,'Reproducible prototype evidence schema','document','# Evidencia',schema=1,rationale='brief describes implemented screen and controls, while captured DOM and calculated results supply evidence; never copy demonstration as result or infer API from pixels.')
for label,needle,attrs in [
 ('Declarative states and supported actions','Cada estado:',{'state_fields':['id','name','hash','actions','expect','nodes'],'actions':['click','fill','press','check','uncheck','select'],'required':'keyboard andreturn/cancel states','arbitrary_code':'notpermitted'}),
 ('DS instance local composition and local content kinds','`components`:',{'kinds':['ds','local-composition','local-content'],'local_content':'ownnode/text/bounds/order/type, reasonandtokens','figma_target':'providedURL ornull,neverimplicitmaster'}),
 ('DOM marker measurement and visible text coverage','`DSNode` usa display:contents',{'display_contents':'measurefirstrealchild, explicitcommoncontainer for siblings','fields':['parent_id','order','bounds','declaredprops'],'state_props':'screen/state mapping','unmapped_visible_text':'captureFAIL'}),
 ('Computed typography identity and fragment evidence','La captura añade',{'identity_source':'computed --ds-type-style-id','fragment_roles':'includinginputvalues/placeholders','statuses':['IDENTIFIED','PARTIAL','NOT_RUN'],'marker_does_not_prove_metrics':True}),
 ('Native evidence dependency even without capture','El generador exige esta fuente',{'requires':'nativeamendment onfamily or capturedderivedFrom','report_state':'preserve PASS/VALIDATION_PENDING/BLOCKED','new_destination':'NOT_RUN','forbidden':['omitmissingdependency','assignmaterializedtonative','doublescale','inferchainfromemptyID']})]:
 n=add(p,label,'concept',needle,**attrs);edge(roots[p],n,p,needle=needle)
# Explicit reference links between the skills and their same-chunk guides.
for src,targets in {
 'skills/contpaqi-figma-screens/SKILL.md':['skills/contpaqi-figma-screens/references/design-system.md','skills/contpaqi-figma-screens/references/figma-workflow.md','skills/contpaqi-figma-screens/references/handoff-and-qa.md'],
 'skills/contpaqi-po-prototypes/SKILL.md':['skills/contpaqi-po-prototypes/references/design-system.md','skills/contpaqi-po-prototypes/references/handoff.md'],
 'skills/contpaqi-figma-screens/references/figma-workflow.md':['skills/contpaqi-figma-screens/references/design-system.md','skills/contpaqi-figma-screens/references/handoff-and-qa.md']}.items():
 for target in targets:edge(roots[src],roots[target],src,'references')
edge(roots['skills/contpaqi-po-prototypes/references/handoff.md'],roots['skills/contpaqi-figma-screens/references/handoff-and-qa.md'],'skills/contpaqi-po-prototypes/references/handoff.md','references','habilidad de Figma')
# Transversal: retain the historical requirement state and reference actual family entities.
p='specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md'
consumption=add(p,'TYPOGRAPHY CONSUMPTION 001','document','contract_id:',version='0.1.0',status='DELEGATED_FOR_BUILD',audit='PENDING',implementation_validation='REQUIRES_FINAL_READBACK_HISTORICAL_CUT',rationale='Explicit user request requires versioned text/role/variant assignments for all43families; assignments do not duplicate canonical recipes or confer implementation PASS.')
coverage=add(p,'Exact family and range coverage','concept','El censo de entrada contiene',families=43,component_pages=33,census_pages=34,all_text_nodes=3501,all_ranges=3503,ui_nodes=3351,ui_ranges=3353,editorial_nodes=150,required_families=39,not_applicable=['Loader','Scrollbar','Characters','Logos'],rationale='Each UI range is counted once by host context; nested dependencies in different instances are separate consumers. Hidden text is not excluded.');edge(consumption,coverage,p,needle='El censo de entrada contiene')
for line in (ROOT/p).read_text().splitlines():
 if line.startswith('| TYC-'):
  c=[v.strip() for v in line.split('|')];label=c[1];req=add(p,label,'rationale',line,requirement=c[2],rationale=c[2]);edge(consumption,req,p,'references',line)
family_targets=[]
for line in (ROOT/p).read_text().splitlines():
 if not re.match(r'\| \[[A-Z][A-Z0-9-]+ · ',line):continue
 c=[v.strip() for v in line.split('|')];m=re.search(r'\[([^]]+)\]\(([^)]+)\)',c[1]);target=Path('specs')/m[2]
 targetstr=target.as_posix(); candidates=[n for n in known.values() if relative(n.get('source_file',''))==targetstr and n.get('file_type')=='document' and n.get('_origin')!='ast']
 assert len(candidates)==1,(targetstr,len(candidates));tn=candidates[0]['id'];family_targets.append(tn)
 edge(coverage,tn,p,'references',line,family=m[1],applicability=c[4],ui_nodes=int(c[5]),ui_ranges=int(c[6]),logical_styles=int(c[7]))
assert len(family_targets)==43
histprep=add(p,'Historical per subset preparation','concept','El mapping 0.1.1 distingue',logical_blocked_segments=0,application_blocked_segments=103,direct_segments=3250,historical_global_preparation='BLOCKED',families={'Select':64,'DropdownItem':26,'Header':12,'AppShell':1},rationale='Logical assignment completeness is distinct from stable style application; the bounded Button probe does not validate103scaled consumers. Native0.1.2 explicitly supersedes this condition only for proven ranges.');edge(consumption,histprep,p,needle='El mapping 0.1.1 distingue')
fmt=add(p,'Preserved underline assignments','concept','La enmienda de formato cambia',styles=4,ranges=27,family_counts={'Button':15,'FileUpload':4,'EmptyStates':8},unchanged_other_ranges=3326,metric_recipe_change=False);edge(consumption,fmt,p,needle='La enmienda de formato cambia')
controls=add(p,'Documentary controls for 44 Markdown files','concept','Control documental del',result='PASS_DOCUMENTARY_ONLY',family_ids=43,prior_normative_files=68,local_links=528,hash_references=226,assignment_rows=360,range_coverage=3353,figma_execution='NOT_RUN',rationale='Canonical hashes, Ruby/Psych frontmatter, links and exact mapping selectors validate documentation only; no persistent Figma consumption inferred.');edge(consumption,controls,p,needle='Control documental del')
# Native amendment: exact scoped replacement, three native recipe links and bounded current evidence.
p='specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md'
native=add(p,'TYPOGRAPHY NATIVE INHERITANCE 001','document','contract_id:',version='0.1.2',status='DELEGATED_FOR_BUILD',audit='PENDING',implementation_validation='VALIDATED_TYPOGRAPHY_SCOPE',catalog_styles=79,base_styles=18,complementary_styles=61,metric_recipe_change=False,rationale='103scaled consumers can resolve shared typography through verified main style and native instance scale despite an observed empty localID; scope-specific proof replaces only the identified historical direct-materialized-ID requirement.')
supersession=add(p,'Explicit native supersession scope','concept','Las fuentes históricas permanecen',requirements=['REQ-TYP-004','AC-TYP-004','derivedinstances section','TYC-01','TYC-06','format0.1.1 scaledlink preparation'],family_assignment_rows=13,family_ranges={'Select':64,'DropdownItem':26,'Header':12,'AppShell':1},preserved_direct_ranges=3250,preserved_underline_ranges=27,history_preserved=True);edge(native,supersession,p,needle='Las fuentes históricas permanecen');edge(supersession,consumption,p,'references','[Consumo transversal 0.1.0]')
nativerules={}
for line in (ROOT/p).read_text().splitlines():
 m=re.match(r'\*\*(NAT-\d+) · ([^*]+)\*\* (.*)',line)
 if m:
  n=add(p,m[1]+' '+m[2].rstrip('.'),'rationale',line,requirement=m[3],rationale=m[3]);nativerules[m[1]]=n;edge(native,n,p,needle=line)
assert len(nativerules)==6
for logical,count,main,styleid,scale in [('ui-checkbox-label-scaled-two-thirds',14,'ui-body-compact','S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,','2/3'),('ui-checkbox-label-scaled-five-sixths',76,'ui-body-compact','S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,','5/6'),('micro-count-small-scaled-four-thirds',13,'micro-count-small','S:2987fb55403e26b9fd23807ce894f58cc084820d,','4/3')]:
 n=add(p,logical,'concept','| `'+logical+'`',metric_identity=logical,ranges=count,main_style=main,main_figma_style_id=styleid,native_relation_scale=scale,recipe_scale=1,local_style_assignment='Do not apply materializedderived style to nativeinstance');edge(nativerules['NAT-02'],n,p,needle='| `'+logical+'`')
proofnative=add(p,'Exhaustive native chain and causal evidence','concept','La [evaluación de herencia 103]',result='PASS_NATIVE_SCOPE',ranges=103,pages=3,api_routes=242,principal_texts=9,principal_components=5,local_empty_style_ids=103,typographic_instance_overrides=0,raw_outer_slot_issues=6,slot_property='Options#466:0',pilots=3,causal_checks=36,verifier_selftests=8);edge(native,proofnative,p,needle='La [evaluación de herencia 103]');edge(nativerules['NAT-05'],proofnative,p,needle='La [evaluación de herencia 103]')
globalproof=add(p,'Final bounded typography consumer acceptance','concept','El [QA global]',result='PASS_TYPOGRAPHY_SCOPE',pages=34,ui_nodes=3351,ui_ranges=3353,direct_ranges=3250,native_ranges=103,unresolved_ranges=0,preservation_fingerprints_equal=3501,editorial_preserved=150,styles=79,bindings=322,mode_resolutions=1288,human_audit='PENDING');edge(native,globalproof,p,needle='El [QA global]');edge(globalproof,proofnative,p,needle='El [QA global]')
meta=add(p,'Metadata only changes do not invalidate consumer census','rationale','El [registro de implementación]',rationale='Global reads follow the last consumer write. Later3style descriptions/11Typography texts and2prefix/card clarifications are outside34consumerpages, preserve recipes/IDs/bindings, and have their own readback; they do not require repeating consumercensus.',distinct_results=['DIRECT_STYLE_ID','INHERITED_NATIVE_SCALE','UNRESOLVED']);edge(native,meta,p,needle='El [registro de implementación]')
web=add(p,'Materialized web recipe and evidence carrying handoff','concept','Web sigue consumiendo',web_transform='apply effective recipe once',css_recipes_unchanged=79,family_amendments_preserved=43,native_registry_families=4,new_prototype_execution='NOT_RUN untildestinationread',release_closure='P08 separate',slots='NOT_APPLICABLE to linkagechange; existing family anatomy preserved');edge(native,web,p,needle='Web sigue consumiendo')
# Same-chunk explicit normative connections and verified external citation endpoints only.
for registry,n in registry_current.items():edge(n,native,registry,'references','nativa' if registry!='registry/implementations.md' else 'enmienda de herencia')
edge(dec12,native,'registry/DEC-TYPOGRAPHY-STYLES-001.md','references','[enmienda nativa 0.1.2]');edge(dec11,consumption,'registry/DEC-TYPOGRAPHY-STYLES-001.md','references','[enmienda transversal de consumo]')
edge(rel21,native,'registry/skills.md','references','El corte incorpora las43enmiendas')
for p,r in roots.items():
 text=(ROOT/p).read_text()
 if 'TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md' in text:edge(r,native,p,'references','TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md')
 if 'TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md' in text:edge(r,consumption,p,'references','TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md')
for p,r in [(p,native) for p in ['specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md']]+[('specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md',consumption)]:
 for target in ['specs/foundations/typography.contract.v0.1.0.md','implementations/figma/typography.v0.1.1.mapping.json','implementations/figma/typography.v0.1.1.catalog.state.json']:
  ref(r,target,p)
# Non-obvious conceptual bridge: build-time declared identity and Figma readback share a need
# for independently measured properties; neither marker/ID is accepted as proof by itself.
edge(roots['skills/contpaqi-po-prototypes/references/handoff.md'],roots['skills/contpaqi-figma-screens/references/handoff-and-qa.md'],'skills/contpaqi-po-prototypes/references/handoff.md','semantically_similar_to','IDENTIFIED verifica IDs',confidence='INFERRED',score=0.85,rationale='Both workflows distinguish declared identity from independently checked metric/binding conformity across runtimes.')
# Final complete fragment validation and deterministic serialization; no live graph writes.
ids={n['id'] for n in nodes};assert len(ids)==len(nodes)
assert set(files)=={n['source_file'] for n in nodes if not n.get('reference_only')}
allowed=ids|set(existing)
uniq={}
for e in edges:
 assert e['source'] in allowed and e['target'] in allowed,(e['source'],e['target'])
 assert e['source_file'] in files,e['source_file']
 score=e['confidence_score'];conf=e['confidence'];assert (conf=='EXTRACTED' and score==1) or (conf=='INFERRED' and score in [.95,.85,.75,.65,.55]) or (conf=='AMBIGUOUS' and .1<=score<=.3),(conf,score)
 key=(e['source'],e['target'],e['relation'],e['source_file'],e.get('source_location'));uniq[key]=e
edges=sorted(uniq.values(),key=lambda e:(e['source_file'],e['source'],e['target'],e['relation'],str(e.get('source_location'))))
for n in nodes:
 assert re.fullmatch('[a-z0-9_]+',n['id'])
 assert n['file_type'] in {'code','document','paper','image','rationale','concept'}
 for key in ['source_location','source_url','captured_at','author','contributor']:n.setdefault(key,None)
for f in files:assert sha(f)==plan[Path(f).relative_to(ROOT).as_posix()]
part={'nodes':sorted(nodes,key=lambda n:n['id']),'edges':edges,'hyperedges':hyper,'input_tokens':0,'output_tokens':0,'usage_status':'UNAVAILABLE','usage_note':'Provider token counts unavailable. Zero numeric fields are legacy-schema placeholders, not measured usage.','source_sha256':{f:sha(f) for f in files},'extraction_scope':'18 newly reviewed documents/current insertions plus4exact preverified family seeds. Prior append-only registry semantics reused only after exact beforegraph snapshot hash and unchanged-line proof; original statuses retained and locations rebased. No new Figma or current graph publication claimed.'}
(RUN/'chunk-01.json').write_text(json.dumps(part,ensure_ascii=False,indent=2)+'\n')
(RUN/'chunk-01.history-reuse.json').write_text(json.dumps({'status':'PASS','files':proof,'ast_edges_reextracted':False,'before_graph':str((RUN/'before/graph.json').relative_to(ROOT))},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'chunk':'01','files':len(files),'nodes':len(nodes),'edges':len(edges),'hyperedges':len(hyper),'sha256':sha(RUN/'chunk-01.json'),'seed_nodes':len(seed['nodes']),'seed_edges':len(seed['edges']),'history_nodes':sum(x['semantic_nodes_retained'] for x in proof),'source_hashes':'PASS','external_endpoint_ids':'VERIFIED_BEFORE_OR_SEEDS'},indent=2))
