import pathlib,json,re,hashlib,collections
root=pathlib.Path.cwd();run=root/'graphify-out/runs/2026-10-13-high-priorities'
files=json.loads((run/'chunk-00.files.json').read_text());assigned={str(pathlib.Path(f).relative_to(root)):f for f in files}
texts={rel:pathlib.Path(f).read_text() for rel,f in assigned.items()}
old=json.loads((run/'before/graph.json').read_text());old_byid={n['id']:n for n in old['nodes']}
old_artifact={n['source_file']:n for n in old['nodes'] if n.get('_origin')=='ast'}
checks={}
for rel,heading in [('registry/decisions.md','## DEC-CHARACTERS-ECOSISTEMA'),('registry/environment.md','## Graphify · verificación'),('registry/qa.md','## QA-CHAT-LAYOUT'),('CHANGELOG.md','## Modal')]:
 s=texts[rel];prior=s[:s.index('\n## ')+1]+s[s.index(heading):];digest=hashlib.sha256(prior.encode()).hexdigest()
 assert digest==old_artifact[rel]['sha256'];checks[rel]={'historical_content_sha256':digest,'historical_bytes_unchanged':True}
g={'nodes':[],'edges':[],'hyperedges':[],'input_tokens':0,'output_tokens':0}
basekeys=['id','label','file_type','source_file','source_location','source_url','captured_at','author','contributor']
ignored=set(basekeys+['_origin','community','community_name','norm_label','sha256','extraction_scope','rationale'])
shift={'registry/decisions.md':6,'registry/environment.md':8,'registry/qa.md':4,'CHANGELOG.md':6,'README.md':4,'references/GRAPH-OPERATIONS.md':2}
def locshift(rel,loc):
 if not isinstance(loc,str):return loc
 if ':L' in loc:loc='L'+loc.rsplit(':L',1)[1]
 if re.fullmatch(r'L?\d+(?:-\d+)?',loc):
  nums=list(map(int,re.findall(r'\d+',loc)));off=shift.get(rel,0)
  if nums[0]>=3:nums=[n+off for n in nums]
  elif len(nums)>1:nums[-1]+=off
  return 'L'+'-L'.join(map(str,nums))
 return loc
for n in old['nodes']:
 rel=n.get('source_file','')
 if rel in assigned and n.get('_origin')!='ast':
  z={k:n.get(k) for k in basekeys};z['source_file']=assigned[rel];z['source_location']=locshift(rel,z['source_location'])
  rat=n.get('rationale','');extra={k:v for k,v in n.items() if k not in ignored}
  if extra:rat+=((' ' if rat else '')+'Preserved source attributes: '+json.dumps(extra,ensure_ascii=False,sort_keys=True)+'.')
  if rat:z['rationale']=rat
  g['nodes'].append(z)
for e in old['links']:
 rel=e.get('source_file','')
 if rel in assigned and e.get('_origin')!='ast':
  z={k:e.get(k) for k in ['source','target','relation','confidence','confidence_score','source_file','source_location','weight']};z['source_file']=assigned[rel];z['source_location']=locshift(rel,z['source_location']);g['edges'].append(z)
preserved_nodes=len(g['nodes']);preserved_edges=len(g['edges'])
def norm(s):return re.sub('[^a-z0-9]','_',s.lower())
def stem(rel):return norm(str(pathlib.Path(rel).with_suffix('')))
def location(rel,needle):
 assert needle in texts[rel],(rel,needle)
 return 'L'+str(texts[rel][:texts[rel].index(needle)].count('\n')+1)
new={}
def node(key,rel,label,typ,needle,why):
 ident=stem(rel)+'_'+norm(label)
 assert ident not in old_byid and not any(n['id']==ident for n in g['nodes']),ident
 n={'id':ident,'label':label,'file_type':typ,'source_file':assigned[rel],'source_location':location(rel,needle),'source_url':None,'captured_at':None,'author':None,'contributor':None,'rationale':why}
 g['nodes'].append(n);new[key]=ident;return ident
def edge(source,target,rel,kind='references',needle=None,conf='EXTRACTED',score=1.):
 source=new.get(source,source);target=new.get(target,target)
 g['edges'].append({'source':source,'target':target,'relation':kind,'confidence':conf,'confidence_score':score,'source_file':assigned[rel],'source_location':location(rel,needle) if needle else None,'weight':1.})
D='registry/decisions.md';E='registry/environment.md';Q='registry/qa.md';T='references/PROJECT-TOOLING.md';V='qa/tooling/project-tooling.2026-10-13.review.md';P='protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md';G='references/GRAPH-OPERATIONS.md';R='README.md';C='CHANGELOG.md'
node('decision',D,'DEC-PROJECT-HIGH-PRIORITIES-001','concept','## DEC-PROJECT-HIGH-PRIORITIES','EXPLICIT user authorization on 2026-10-13: “Dale empieza con las Altas”, after the optimization audit, authorizes proposals 1–3 only: common local verification/closure entry, derived per-family state, deterministic documentary QA. This adopts this bounded tooling scope; prior audit proposals retain their original historical status.')
node('limits',D,'Alcance limitado de prioridades altas','rationale','DERIVED implementación','Derived implementation includes declarative corpus, hash guards, session semantic extraction, existing safe Ruby/Psych YAML parser and regenerable views; reconcile declared package 0.2.4. No authority, approval, contract, canonical data or design changes. Git retention, transversal simplification, external services and frontend remain outside this scope.')
edge('registry_decisions_registro_de_decisiones','decision',D,needle='## DEC-PROJECT-HIGH-PRIORITIES');edge('decision','limits',D,needle='DERIVED implementación')
node('guide',T,'Operación local del proyecto con scripts/ds','document','# Operación local','Operational guide implementing authorized high priorities, complementing P01/P05/P06 without changing authority, design requirements or approvals.')
node('readonly',T,'check status y graph plan de solo lectura','rationale','Los tres comandos leen','From repo root check, status FAMILY-ID and graph plan read current state without writes/installations/Figma/external services. check exit codes: 0 passed controls, 1 failure, 2 blocked. PASS is documentary/deterministic, never human approval or visual QA.')
node('runtime',T,'Runtime comprobado y parser YAML seguro Ruby/Psych','concept','Runtime comprobado','Graphify 0.9.65 and Python 3.12 resolve through .graphify_python or DS_PYTHON. Existing system Ruby/Psych safely loads YAML and detects duplicate keys. Missing capabilities report BLOCKED, with environment preparation governed by P01; no implicit installation.')
node('view',T,'Vista derivada por familia sin autoridad paralela','rationale','## Vista por familia','status --write generates registry/generated/project-status.md and .json. Reads contracts/amendments with declared identity and metadata; source extractions are evidence rather than normative bases. Eligible bases APPROVED or DELEGATED_FOR_BUILD remain separate; DRAFT cannot displace current base.')
node('prose',T,'Metadatos explícitos de contratos antiguos en prosa','rationale','También reconoce','Recognizes explicit ID · name · version heading and Estado label of Header, Modal, Sidebar and App Shell without frontmatter. Does not infer contract state from QA paragraphs. Amendments lacking automatic base relation remain in a separate visible index without invented consumer.')
node('base',T,'Resolución conservadora de supersedes y base_version','rationale','Entre bases usa','Only explicit supersedes or declared base_version composition selects among bases; multiple remaining eligible candidates are AMBIGUOUS and fail, never latest-date/highest-version wins. Baseline inherited requirements stay linked; partial amendments never replace whole base.')
node('selectors',T,'Selectores de evidencia por hash y fragmento','rationale','Las enmiendas con','Amendments grouped through applies_to, base_contract or same identity preserve scoped requirements. Prose-only relations have config/ds-project.json evidence selectors bound to hash and fragment; changed selectors fail until reviewed. Configuration owns locators, not design values or editable status.')
node('dimensions',T,'Implementación QA publicación y auditoría separadas','rationale','La implementación se asocia','Exact contractual references or explicit contract/amendment links associate implementations. Show declared values by file and scope, never a synthesized global VALIDATED from multiple PASS results. Missing fields UNKNOWN; QA, publication and human audit remain distinct.')
node('exceptions',T,'Excepciones citadas desde auditoría y matriz propietarias','rationale','Los cierres y excepciones','Chat, Logos, Search, six families, Radio/Checkbox and unpromoted-base closures/exceptions quote explicit owner sections. Configuration stores titles, hashes and addressees; text is read from owner. No parallel editable queue or latest-date authority.')
node('viewhash',T,'Vigencia de vista comparada en memoria y excluida del corpus','rationale','Los outputs son derivados','Generated outputs are excluded from Graphify corpus to avoid feedback. check regenerates in memory and compares content and source hashes; changing a view or source makes view STALE.')
node('checks',T,'Controles documentales deterministas','concept','## Controles documentales','Validate JSON/YAML/frontmatter and duplicate keys; local inline/reference Markdown destinations outside code blocks; declared states/versions, data references and resolvable dependencies; protected canonical hashes and source_data_ref/source_data_digest_sha256 pairs; base/prose relations; package version across config/AGENTS/README/changelog; view/graph freshness, integrity and output hashes. Excludes anchors, remote URLs and rendering.')
node('histlinks',T,'Excepción histórica ligada a ruta línea enlace y SHA-256','rationale','Un enlace histórico','A link is HISTORICAL only if exact path, line, target and SHA-256 match. Never edit backups or grant blanket archive exemption. A modification or new broken link fails.')
node('deps',T,'Dependencias externas sin identidad resoluble producen WARNING','rationale','Las dependencias externas','Do not invent contracts to make checks pass; an observed icon ID/name does not establish a ready local dependency.')
node('docs_only',T,'check docs-only no acredita CURRENT','rationale','Durante preparación','--docs-only explicitly skips view/graph gates. Persisting evidence requires --report with local path. Controls are operational conventions, not an externally approved design schema.')
node('prepare',T,'graph prepare con respaldo y plan fijado por hashes','rationale','plan no escribe','plan is read-only. prepare creates a unique new run, preserves existing outputs, locks hashes of all sources/configuration/prompt and produces semantic plan/chunk file lists. Never reuse run names/overwrite backup. No delta and verified outputs means no regeneration.')
node('semantic',T,'Semántica de la sesión obligatoria por delta documental','rationale','El agente sigue','Agent follows Graphify skill to read new/changed files, retain historical provenance and distinguish proposals from norms; software cannot replace reading with headings. Missing fragment/coverage/evidence stops with previous graph preserved. No API key required or external service authorized.')
node('close',T,'graph close construye y verifica outputs en staging','rationale','El cierre valida','Validate docs/view, extract AST, add references/design data, merge semantics and stage JSON/report/HTML. Read outputs; verify coverage, integrity, identity queries and manifest. Recheck all sources against prepared plan before publish. A post-prepare source change requires new run; no old semantics certified for new content.')
node('recovery',T,'Publicación recuperable con marcador final de hashes','rationale','Los destinos se reemplazan','Replace destinations only after verification; ordinary errors recover from backup. Publish ds-closure.json last with output hashes so interruption between replacements is detectable as STALE. No claim of multi-file atomicity under power failure; retain before for recovery.')
node('concurrent',T,'Cambios concurrentes del grafo impiden publicar','rationale','Si los outputs vigentes','close fails before publication if active outputs changed since prepare; preserve that cut. engine.log stores detailed log. Semantic deltas outside prepared plan rejected.')
node('corpus',T,'Corpus explícito y consumo semántico no medido','rationale','El HTML usa','HTML aggregates communities above 5000 nodes. Semantic measured usage UNAVAILABLE without session counters, never attributed zero. Explicit filters retain four design JSON and supplementary Mermaid without globally disabling secret protection.')
node('astonly',T,'graphify update AST no acredita cierre documental','rationale','graphify update .','Maintained P05 entry is scripts/ds graph; dated scripts under graphify-out remain historical evidence. graphify update alone is AST and does not establish documentary closure.')
node('config',T,'Configuración de corpus guardas consultas y excepciones','concept','config/ds-project.json declara','Configuration declares verified version, derived exclusions, supplements, protected data, queries, exact historical exceptions and relation selectors. Config changes invalidate closure. Enlarging sources/filters/exemptions requires recorded evidence, never hiding FAIL.')
node('componentqa',T,'Verificadores cjs históricos independientes','rationale','Los verificadores .cjs','Common command does not execute Figma creation scripts or convert historical component QA to current readback. Specific validator execution requires Node availability and verified scope.')
node('toolscope',T,'Retención Git simplificación transversal y frontend fuera de lote','rationale','Retención Git','No hooks, libraries, palettes or contracts changed to obtain PASS; local regression available through scripts/ds test.')
for key in ['readonly','runtime','view','checks','prepare','semantic','close','recovery','concurrent','corpus','astonly','config','componentqa','toolscope']:edge('guide',key,T,needle=g['nodes'][-1]['label'] if False else None)
for key in ['prose','base','selectors','dimensions','exceptions','viewhash']:edge('view',key,T)
for key in ['histlinks','deps','docs_only']:edge('checks',key,T)
edge('decision','guide',D,'cites',needle='[Guía operativa]');edge('prepare','semantic',T);edge('semantic','close',T);edge('close','recovery',T);edge('close','concurrent',T)
node('qa',V,'QA-PROJECT-TOOLING-001 revisión local','document','# QA-PROJECT','Authorized high priorities 1–3. Records executed local tests/documentary initial QA plus distinct prospective graph closure gates. It does not certify new Figma QA, design approval or library publication.')
node('testpass',V,'21 pruebas de regresión local PASS declaradas','concept','Regresión local','Source records 21 executed PASS tests: invalid/duplicate JSON/YAML, safe YAML, exact-byte historical links, protected canonical data, read-only commands, explicit prose metadata, supersedes/base_version, partial/DRAFT amendments, semantic requirement for new docs, post-prepare source changes, concurrent graph changes and recovery from partial publish failure. This semantic extraction records the report, not independent test rerun.')
node('docpass',V,'QA documental inicial PASS y vista de 47 identidades','concept','QA documental inicial','Source records initial PASS: 460 JSON and 218 YAML/frontmatter; four prose-metadata contracts added to generator. Final effective counts/findings must come from scripts/ds check. View has 47 identities including Foundations, transversal contract and Anticipa candidate, not 47 approved Figma families. Explicit Search 0.1.1 and Button 0.2.0 resolution; Chat Layout PARTIAL, Logos and unpromoted exceptions preserved.')
node('warnings',V,'Cuatro WARNING de dependencias y 21 enlaces históricos','concept','Quedan cuatro WARNING','Unresolved local identity: PLUS-CIRCLE-OBSERVED-001 and PHOSPHOR-ICONS-001 in Button 0.1.0; PHOSPHOR-ICONS-001 in Button 0.2.0; PlusCircle in Filter Chip 0.2.0. No invented icon contract. 21 historical broken links exempt only exact path/line/target/SHA-256; new broken link fails.')
node('qagate',V,'Gate final high-priorities pendiente de evidencia efectiva','rationale','## Gate final','Report does not prospectively certify sync. documentation-check.json, verification.json and manifest-check.json must PASS; closure.json must CURRENT and match current outputs in 2026-10-13-high-priorities run. scripts/ds check confirms corpus/view/output hashes. Without conditions STALE/BLOCKED.')
node('idem',V,'Idempotencia CURRENT_NO_CHANGES por comprobar al cierre','rationale','El plan sin delta','Plan without delta and prepare on a verified cut must return CURRENT_NO_CHANGES without regeneration; final calculated evidence and idempotence test live in run excluded from corpus to avoid regeneration cycle. This is a stated acceptance gate, not an asserted completed test.')
node('qalimit',V,'Límites de QA tooling y datos canónicos protegidos','rationale','No hay nuevo QA','No new visual/Figma QA, changes to design contracts/JSON, invented human approval or library publishing. Does not semantically validate all requirements, Markdown anchors, remote links or frontend. No power-loss atomicity assertion; final-marker hashes detect incomplete publication. Protected canonical data retain approved SHA-256. Four dependency warnings/design exceptions remain under existing owners, not implementation authorization.')
for key in ['testpass','docpass','warnings','qagate','idem','qalimit']:edge('qa',key,V)
edge('qa','guide',V,'cites',needle='[guía]');edge('qa','decision',V,'cites',needle='[Decisión]');edge('decision','qa',D,'cites',needle='[QA del lote]')
node('env',E,'Herramientas de prioridades altas 2026-10-13','concept','## Herramientas','DEC-PROJECT-HIGH-PRIORITIES-001 implemented by scripts/ds and configuration. Existing Graphify 0.9.65/Python 3.12.13 and Ruby/Psych 3.1.0; no installs. CLI exposes check/status/graph plan-prepare-close-check/test. Node unavailable in checked PATH; historical .cjs not run and no new Figma QA attributed.')
node('astcheck',E,'Prueba AST con corte previo restaurado por hash','concept','La ejecución requerida','graphify update . exited 0 producing 7546 nodes/13581 relations and reporting four sources omitted by ordinary detector. Log/results preserved, eight prior outputs restored by hashes before full closure; isolated AST does not prove documentation current. Evidence in 2026-10-13-tooling-ast-check run.')
node('envgate',E,'Estado del lote STALE hasta cierre y check efectivos','rationale','[QA y límites]','During lot graph STALE; CURRENT only when scripts/ds check confirms corpus/view/outputs and high-priorities run closure says CURRENT. Community HTML above 5000 nodes; measured semantic usage UNAVAILABLE; no new external capabilities/hooks/global configuration.')
edge('registry_environment_environment_registry','env',E,needle='## Herramientas');edge('env','astcheck',E,needle='La ejecución requerida');edge('env','envgate',E,needle='[QA y límites]');edge('env','decision',E,'cites',needle='[DEC-PROJECT');edge('envgate','qa',E,'cites',needle='[QA y límites]')
node('qareg',Q,'QA-PROJECT-TOOLING-001 registro acotado','concept','## QA-PROJECT-TOOLING','Deterministic docs, conservative base/amendment resolution, source protection and recoverable publication; regression tests executed. Graph/view also need final report gates. Not new visual QA, contract approval or library publication.')
edge('registry_qa_registro_de_qa','qareg',Q,needle='## QA-PROJECT');edge('qareg','qa',Q,'cites',needle='[QA local')
node('p05entry',P,'scripts/ds implementa controles P05 sin sustituir GRAPH-SYNC','rationale','Herramienta local','Maintained common entry implements verification, derived view and closure, while P05 authority and GRAPH-SYNC criteria remain intact.')
edge('protocols_05_self_documentation_and_traceability_p05','p05entry',P,needle='Herramienta local');edge('p05entry','guide',P,'cites',needle='[guía scripts/ds]');edge('p05entry','protocols_05_self_documentation_and_traceability_graph_sync_01_04',P,'implements',needle='Herramienta local')
node('graphentry',G,'Entrada mantenida scripts/ds desde 2026-10-13','rationale','Entrada operativa mantenida','scripts/ds check verifies; scripts/ds graph prepares/closes with backup, semantic delta and readback. Dated graphify-out scripts retained as historical evidence; existing gates remain applicable.')
edge('references_graph_operations_graph_operations','graphentry',G,needle='Entrada operativa');edge('graphentry','guide',G,'cites',needle='[scripts/ds y guía de cierre]')
node('readme_version',R,'Versión operativa integrada 0.2.4 verificada documentalmente','concept','**Versión operativa','README declares operational package 0.2.4 and documentary verification date 2026-10-13. Does not itself certify any Graphify closure or design approval.')
node('readme_view',R,'Acceso a vista derivada y verificación local','concept','La [vista derivada','Per-family view joins base/amendments/scoped evidence from owner documents; regenerate with scripts/ds status --write, never manual edit or approval. scripts/ds check, status SEARCH-001 and graph plan provide local navigation; guide describes prepare/semantics/verified closure without installs/external services.')
edge('readme_document','readme_version',R,needle='**Versión operativa');edge('readme_document','readme_view',R,needle='La [vista derivada');edge('readme_view','guide',R,'cites',needle='[procedimiento operativo]')
node('changelog',C,'Paquete 0.2.4 sincronización continua y herramientas locales','concept','## 0.2.4','2026-10-13 entry and README reconcile version already declared by AGENTS and P05/DEC-GRAPH-CONTINUOUS-SYNC-001 from 2026-10-08. User request implements high priorities with scripts/ds, config, derived view and deterministic QA; closure stages and verifies semantics with backup. No design-contract approvals, canonical/Figma/global hook changes or retention work.')
edge('changelog_document_md','changelog',C,needle='## 0.2.4');edge('changelog','guide',C,'cites',needle='[Operación y límites]');edge('changelog','decision',C,'references',needle='Por solicitud')
# Source-supported cross-file mechanisms, without claiming executed prospective gates.
edge('qagate','close',V,'conceptually_related_to',needle='El reporte no certifica');edge('testpass','recovery',V,'references',needle='Regresión local');edge('docpass','view',V,'references',needle='QA documental inicial');edge('envgate','qagate',E,'references',needle='[QA y límites]')
edge('base','protocols_05_self_documentation_and_traceability_lineage_revalidation',T,'conceptually_related_to',needle='Entre bases usa',conf='INFERRED',score=.95)
edge('histlinks','registry_environment_21_referencias_hist_ricas_relativas_rotas' if 'registry_environment_21_referencias_hist_ricas_relativas_rotas' in old_byid else 'registry_environment_auditor_a_2026_10_13_corte_inicial_verificado',T,'conceptually_related_to',needle='Un enlace histórico',conf='INFERRED',score=.85)
# Persist exact source citations to existing external artifact identities only.
for rel in [V,T,R,P,G,C,D,E,Q]:
 scope=texts[rel]
 if rel in [D,E,Q]:scope=scope[:scope.find('\n## ',scope.find('\n## ')+1)]
 owner={'registry/decisions.md':'decision','registry/environment.md':'env','registry/qa.md':'qareg',V:'qa',T:'guide',R:'readme_document',P:'p05entry',G:'graphentry',C:'changelog'}[rel]
 for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)',scope):
  target=m.group(1)
  if '://' in target or target.startswith('#'):continue
  dest=(root/pathlib.Path(rel).parent/target.split('#')[0]).resolve()
  try:destrel=str(dest.relative_to(root))
  except ValueError:continue
  if destrel in old_artifact:
   edge(owner,old_artifact[destrel]['id'],rel,'cites',needle=m.group(0))
# Remove exact duplicate relation rows while keeping distinct provenance/location.
seen=set();unique=[]
for e in g['edges']:
 key=(e['source'],e['target'],e['relation'],e['source_file'],e['source_location'])
 if key not in seen:seen.add(key);unique.append(e)
g['edges']=unique
ids=[n['id'] for n in g['nodes']];assert len(ids)==len(set(ids));known=set(ids)|set(old_byid)
for n in g['nodes']:
 assert re.fullmatch('[a-z0-9_]+',n['id']) and n['source_file'] in files
 assert n['file_type'] in ['code','document','paper','image','rationale','concept']
 assert '_origin' not in n
 assert all(k in n for k in basekeys)
for e in g['edges']:
 assert e['source'] in known and e['target'] in known,(e['source'],e['target'])
 assert e['source']!=e['target'] and e['source_file'] in files
 assert (e['confidence']=='EXTRACTED' and e['confidence_score']==1) or (e['confidence']=='INFERRED' and e['confidence_score'] in [.95,.85,.75,.65,.55]) or (e['confidence']=='AMBIGUOUS' and .1<=e['confidence_score']<=.3)
for f in files:assert any(n['source_file']==f for n in g['nodes']) and any(e['source_file']==f for e in g['edges'])
(run/'chunk-00.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
validation={'status':'PASS','files':len(files),'nodes':len(g['nodes']),'edges':len(g['edges']),'hyperedges':0,'historical_semantic_nodes_preserved':preserved_nodes,'historical_semantic_edges_preserved':preserved_edges,'history_checks':checks,'endpoint_scope':'chunk plus before/graph.json','source_file_paths':'FILE_LIST absolute verbatim','measured_semantic_usage':'UNAVAILABLE; zero schema placeholders','source_sha256':{rel:hashlib.sha256(t.encode()).hexdigest() for rel,t in texts.items()}}
(run/'chunk-00.validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in validation.items() if k not in ['source_sha256','history_checks']},ensure_ascii=False))
