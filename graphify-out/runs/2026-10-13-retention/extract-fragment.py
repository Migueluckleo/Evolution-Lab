import pathlib,json,re,hashlib,collections
root=pathlib.Path.cwd();run=root/'graphify-out/runs/2026-10-13-retention'
files=json.loads((run/'chunk-00.files.json').read_text());assigned={str(pathlib.Path(f).relative_to(root)):f for f in files};texts={r:pathlib.Path(f).read_text() for r,f in assigned.items()}
old=json.loads((run/'before/graph.json').read_text());old_nodes={n['id']:n for n in old['nodes']};artifacts={n['source_file']:n for n in old['nodes'] if n.get('_origin')=='ast'}
for rel in ['registry/decisions.md','registry/environment.md','registry/qa.md','registry/sources.md','README.md','CHANGELOG.md','references/PROJECT-TOOLING.md']:
 s=texts[rel]
 if rel.startswith('registry/'):
  p=s.index('\n## ');q=s.index('\n## ',p+1);prior=s[:p]+s[q:]
 elif rel=='README.md':prior=s.replace(next(x for x in s.splitlines(True) if x.startswith('La [política de retención]'))+'\n','')
 elif rel=='CHANGELOG.md':prior=s.replace(next(x for x in s.splitlines(True) if x.startswith('En un lote posterior'))+'\n','')
 else:prior=s[:s.index('\nEn un lote posterior')].rstrip()+'\n'
 assert hashlib.sha256(prior.encode()).hexdigest()==artifacts[rel]['sha256'],rel
basekeys=['id','label','file_type','source_file','source_location','source_url','captured_at','author','contributor']
ignore=set(basekeys+['_origin','community','community_name','norm_label','sha256','extraction_scope','rationale'])
shifts={'registry/decisions.md':(3,6),'registry/environment.md':(3,6),'registry/qa.md':(3,4),'registry/sources.md':(3,4),'README.md':(13,2),'CHANGELOG.md':(9,2)}
def shifted(rel,loc):
 if not isinstance(loc,str):return loc
 if ':L' in loc:loc='L'+loc.rsplit(':L',1)[1]
 if re.fullmatch(r'L?\d+(?:-L?\d+)?',loc):
  values=list(map(int,re.findall(r'\d+',loc)));cut,off=shifts.get(rel,(0,0));values=[n+off if n>=cut else n for n in values]
  return 'L'+'-L'.join(map(str,values))
 return loc
g={'nodes':[],'edges':[],'hyperedges':[],'input_tokens':0,'output_tokens':0}
for n in old['nodes']:
 rel=n.get('source_file','')
 if rel in assigned and n.get('_origin')!='ast':
  z={k:n.get(k) for k in basekeys};z['source_file']=assigned[rel];z['source_location']=shifted(rel,z['source_location'])
  extra={k:v for k,v in n.items() if k not in ignore};rat=n.get('rationale','')
  if extra:rat+=((' ' if rat else '')+'Preserved source attributes: '+json.dumps(extra,ensure_ascii=False,sort_keys=True)+'.')
  if rat:z['rationale']=rat
  g['nodes'].append(z)
for e in old['links']:
 rel=e.get('source_file','')
 if rel in assigned and e.get('_origin')!='ast':
  z={k:e.get(k) for k in ['source','target','relation','confidence','confidence_score','source_file','source_location','weight']};z['source_file']=assigned[rel];z['source_location']=shifted(rel,z['source_location']);g['edges'].append(z)
kept=(len(g['nodes']),len(g['edges']));new={}
def norm(s):return re.sub('[^a-z0-9]','_',s.lower())
def where(rel,needle):
 assert needle in texts[rel],(rel,needle)
 return 'L'+str(texts[rel][:texts[rel].index(needle)].count('\n')+1)
def node(key,rel,label,typ,needle,why):
 id=norm(str(pathlib.Path(rel).with_suffix('')))+'_'+norm(label)
 assert id not in old_nodes and id not in new.values(),id
 z={'id':id,'label':label,'file_type':typ,'source_file':assigned[rel],'source_location':where(rel,needle),'source_url':None,'captured_at':None,'author':None,'contributor':None,'rationale':why};g['nodes'].append(z);new[key]=id
 return id
def edge(a,b,rel,kind='references',needle=None,conf='EXTRACTED',score=1.):
 g['edges'].append({'source':new.get(a,a),'target':new.get(b,b),'relation':kind,'confidence':conf,'confidence_score':score,'source_file':assigned[rel],'source_location':where(rel,needle) if needle else None,'weight':1.})
P='references/ARTIFACT-RETENTION.md';V='qa/tooling/retention.2026-10-13.review.md';D='registry/decisions.md';E='registry/environment.md';Q='registry/qa.md';S='registry/sources.md';T='references/PROJECT-TOOLING.md';C='CHANGELOG.md';R='README.md'
node('decision',D,'DEC-ARTIFACT-RETENTION-001','concept','## DEC-ARTIFACT-RETENTION-001','EXPLICIT user “Dale” authorizes the subsequent local retention and Git-weight reduction lot, preserving sources, evidence and recovery. Scope excludes protocol simplification, frontend, design changes and remote publication.')
node('decision_scope',D,'Retención acotada sin eliminación local ni purga automática','rationale','DERIVED implementación','Derived implementation: explicit retention policy and bounded .gitignore exclusions, index removal of 673 backed-up derivatives with verified restoration. All local originals, active graph, per-run semantics, QA, deliverables and Git history remain. Policy defines backup retention and possible future compaction conditions; it does not install/run automatic purge.')
edge('registry_decisions_registro_de_decisiones','decision',D,needle='## DEC-ARTIFACT');edge('decision','decision_scope',D,needle='DERIVED implementación')
node('policy',P,'Política operativa de retención 1.0 del 2026-10-13','document','# Retención','Content-based tracking and local recovery policy; folder names alone cannot discard files. Does not change documentary authority or approve contracts; anchored to DEC-ARTIFACT-RETENTION-001.')
node('unique',P,'Fuentes evidencia y entregables conservados indefinidamente','rationale','| Fuentes, inventarios','Keep sources, inventories, contracts, amendments, decisions, QA, screenshots and implementation evidence in Git and locally indefinitely without automatic deletion. Also keep output deliverables, .codex-build sources, .codex-finalizer evidence, PDF/PPTX versions, manifests, scripts and validations.')
node('active',P,'Grafo activo verificable conservado en Git','concept','| Grafo activo','Track active graph JSON, HTML, report, manifest, health, labels, signature, cost and ds-closure.json. Keep one verifiable operational cut; graph remains a derived index, not authority.')
node('semantics',P,'Semántica por lote y memoria no presuntamente reproducibles','rationale','| Semántica por lote','Track and retain indefinitely chunk/delta extraction, plans/scripts, verification/manifest-check/closure, queries and QA logs. Semantic extraction is not presumed byte-reproducible; keep memory, reflections and .graphify_learning.json because AST cannot reconstruct all evidence.')
node('cache',P,'Exclusión precisa de cachés vocabulario e intermedios','rationale','| cache, vocabulario','Only specifically enumerated .gitignore cache/vocabulary/.graphify_* intermediates are excluded. Work cache is dispensable only with verified active graph, retained sources and per-run semantic contributions. Exclude run AST/combined/combined-raw/structural-supplement intermediates but retain locally until closure and recovery verified.')
node('copies',P,'Copias before staged after con conservación de recuperación','rationale','| runs/*/before','Exclude Graphify output copies before/staged/after from Git; preserve locally backups of the last two verified closures and every open/failed run. Never put unique evidence there. Dated graphify-out/AAAA-MM-DD/graph.json snapshots excluded while small manifests/reports/receipts remain tracked.')
node('conservative',P,'Sin exclusión global por carpeta o por tamaño','rationale','Las exclusiones exactas','Do not globally exclude graphify-out, output, tmp, .codex-build or .codex-finalizer. Existing previews remain for low weight and possible evidence use. Every new exclusion class needs review, not size-only expansion.')
node('workflow',P,'Retiro del índice precedido por respaldo y restore verificables','rationale','## Retención y cambios seguros','Inventory exact tracked candidates with path, bytes, SHA-256 and index blob; inspect concrete documentary links. Archive current bytes including local changes, save manifest/archive hash, verify members and restore temporarily for byte comparison. git rm --cached only for verified list, preserve local files, never git clean or history rewrite. Check exact removals/local presence/protected-source hashes, then close graph under P05 and local guide.')
node('future',P,'Compactación física futura condicionada sin automatismo por edad','rationale','Este lote no borra','No local deletion or purge task in this lot. Recovery archives kept indefinitely until another verified copy exists. Future physical compaction may remove closed-run intermediates older than 30 days while keeping last two verified closures; open/failed runs and unique evidence excluded. Requires its own inventory/verification and does not execute just because age reached.')
node('recover',P,'Recuperación local exacta separada de recuperación histórica Git','rationale','El respaldo local vive','Local archive under graphify-out/retention is excluded from Git, is not remote and does not accompany clones; exact cleanup-time local bytes require that archive. Manifest identifies original Git blobs for temporary historical recovery via git cat-file and hash verification. Preserve history; no filters/destructive garbage collection.')
node('clone',P,'Clon conserva solamente artefactos incluidos en su commit','rationale','Un clon conserva','A clone retains active graph and per-run semantic contributions included in its commit. Caches/intermediates may be generated again from sources and maintained closure. Re-track excluded file only after temporary restore/hash verification and explicit path addition with policy exception reviewed.')
node('metric',P,'Reducción del índice sin ahorro retroactivo de disco o historia','rationale','La reducción medida','Measured reduction is future-commit index tracking footprint. It does not reduce prior Git history or local disk because originals and backup remain. No commit/remote publication in this lot.')
for key in ['unique','active','semantics','cache','copies','conservative','workflow','future','recover','clone','metric']:edge('policy',key,P)
edge('policy','decision',P,'cites',needle='[DEC-ARTIFACT');edge('decision_scope','policy',D,'cites',needle='[política de retención]')
node('qa',V,'QA-ARTIFACT-RETENTION-001 revisión del índice y recuperación','document','# QA-ARTIFACT','2026-10-13 review under bounded retention decision/policy; no design, token, contract or human-audit changes. Source records executed index/removal/recovery checks separately from pending Graphify closure.')
node('classification',V,'Clasificación conservadora de contenido y originales','rationale','## Lectura y clasificación','Consulted AGENTS, P02/P05, Graphify skill/query, audit, guide, registries and real Git index. File content/hashes govern classification, not graph. Preserve output, .codex-build/.codex-finalizer evidence, tmp, design originals, per-run semantics, memory, QA and active graph. Only expressly enumerated generated classes excluded.')
node('result',V,'673 bajas del índice con reducción de 144.71 MiB y 81.05 por ciento','concept','673 derivados retirados','Executed checkpoint: index files 1893 to 1220 before adding new files from other lots; uncompressed index blob sum 187228558 to 35484979 bytes. 673 removed: 622 cache, 16 run intermediates, 32 prior output copies, 3 dated-snapshot/vocabulary files. Difference 151743579 bytes (144.71 MiB, 81.05%); zero local deletions. Existing local changes explain 151779581 current-byte backup size distinct from index.')
node('restorepass',V,'Respaldo y restauración 673 de 673 PASS declarados','concept','Comprobaciones ejecutadas','Source reports tar.gz size 7840848 bytes with manifest SHA-256, 673/673 regular unique members with matching size/hash, real temporary restore/readback 673/673 without project overwrite, local files identical immediately after git rm --cached, only expected 673 staged removals and no commit/publication. This extraction records source evidence, not independent rerun of verifier.')
node('protected',V,'1187 fuentes y entregables protegidos sin cambios','concept','- 1,187 archivos','Source reports 1187 source/contract/evidence/deliverable hashes intact, zero direct Markdown links to removed files, eleven protected examples not matched by exclusions.')
node('checkpoint',V,'Verificación del snapshot separada de cachés regeneradas','rationale','La verificación del snapshot','--restore-test repeats archive restoration; --working compares cleanup-time bytes and legitimate later regeneration can differ; --index-removed checks current index removals. Backup is local and not part of clone; historical recovery uses recorded blobs and intact history.')
node('docqa',V,'Control documental previo y AST aislado verificados','concept','El control documental previo','Prior documentary control passed with 462 JSON, 218 YAML/frontmatter and four explicit prose metadata documents, no ERROR. Required graphify update exited 0 producing AST 7603 nodes/13753 relations; saved cut and restored previous nine outputs/marker by hash before full closure. AST alone does not certify current documentation.')
node('closure',V,'CURRENT del lote retención condicionado al cierre completo','rationale','El resultado de índice','Index result is a checkpoint before graph sync. Complete structural/semantic retention run with before backup and P05 gates. CURRENT requires closure.json, verification.json, manifest-check.json and scripts/ds check to agree; report itself does not prove it. final-check.json stores final result without retrospectively changing index checkpoint.')
node('scope',V,'Retención limita crecimiento futuro sin purgar historia o disco','rationale','No se purga','No local purge/history rewrite. Improvement limits files tracked in subsequent commits/future growth. No pending decision for this lot; protocol simplification and impact-based revalidation outside scope.')
for key in ['classification','result','restorepass','protected','checkpoint','docqa','closure','scope']:edge('qa',key,V)
edge('qa','decision',V,'cites',needle='[DEC-ARTIFACT');edge('qa','policy',V,'cites',needle='[política]');edge('decision_scope','qa',D,'cites',needle='[QA del lote]');edge('restorepass','workflow',V,'conceptually_related_to',needle='Comprobaciones ejecutadas')
node('source',S,'SRC-ARTIFACT-RETENTION-2026-10-13 INDEXED','concept','## SRC-ARTIFACT','OBSERVED operational evidence, not design norm. Manifest inventories 673 Git-tracked derivatives with path/current-byte SHA-256/size/mode/original index blob and starting commit 41ab4c0bf4197ef0a5b1dda73c7a6be81c818933. Sources remain in place; no new design sources.')
node('archive',S,'Respaldo tracked-derivatives.tar.gz con digest registrado','concept','OBSERVED operativo','Local graphify-out/retention/2026-10-13-git-retention/tracked-derivatives.tar.gz: 7840848 bytes, SHA-256 d748bd900b97d91bbf00020d2ec4248fab5b54d44f0e9e4437ca5fb2288f1280. Source records 673/673 restored and checked; backup location is evidence, not a remote or committed copy.')
edge('registry_sources_registro_de_fuentes','source',S,needle='## SRC-ARTIFACT');edge('source','archive',S,needle='OBSERVED operativo');edge('source','qa',S,'cites',needle='[QA y límites]')
node('env',E,'Retención Git 2026-10-13 capacidades locales y recuperación','concept','## Retención Git','Existing Git and Python stdlib used; 673 staged index removals with files retained and 7840848-byte tar.gz digest/restore verified. 1187 protected files retain hashes. No installs, commit, remote publishing or history rewrite.')
node('envgate',E,'Grafo STALE durante retención hasta closure y check final','rationale','El cierre de este lote','Full corpus uses scripts/ds graph prepare/close run 2026-10-13-retention. Graph STALE during edits; CURRENT only if run closure.json and final check verify it. Cache/before/staged/after copies local per policy, evidence/semantics retained. Measured semantic usage UNAVAILABLE.')
edge('registry_environment_environment_registry','env',E,needle='## Retención Git');edge('env','policy',E,'cites',needle='[Política]');edge('env','qa',E,'cites',needle='[verificación de recuperación]');edge('env','envgate',E,needle='El cierre de este lote')
node('qareg',Q,'QA-ARTIFACT-RETENTION-001 registro de PASS acotado','concept','## QA-ARTIFACT','Reports PASS restoration of 673 derivatives, local comparison/exact index removals and preservation of 1187 protected files. Index reduction 151743579 logical bytes is not history/disk reduction; Graphify closure independent under P05, no new Figma QA.')
edge('registry_qa_registro_de_qa','qareg',Q,needle='## QA-ARTIFACT');edge('qareg','qa',Q,'cites',needle='[Reporte]')
node('guide_retention',T,'Retención posterior de copias locales con before obligatorio','rationale','En un lote posterior','Separately authorized subsequent same-day lot applies retention: before/staged/after excluded from Git but remain local; active graph, per-run semantics and closure receipts stay tracked. before retention remains mandatory for recovery. Original high-priority lot scope is unchanged historically.')
edge('guide_retention','policy',T,'cites',needle='[política de retención de derivados]')
node('readme_retention',R,'Acceso a política de retención y recuperación previa','concept','La [política de retención]','Separates evidence/deliverables from local caches/intermediates; keeps active graph and defines recovery before untracking derivatives from Git.')
edge('readme_document','readme_retention',R,needle='La [política de retención]');edge('readme_retention','policy',R,'cites',needle='[política de retención]')
node('changelog_retention',C,'Lote posterior autorizado de retención de 673 derivados','concept','En un lote posterior','User “Dale” on 2026-10-13 authorized Git-weight reduction after high priorities. Cache/intermediate/full local copies excluded; 673 derivatives removed from index with backup/restore verified. Sources, evidence, deliverables, active graph and history preserved; no change to historical high-priorities scope.')
edge('changelog_document_md','changelog_retention',C,needle='En un lote posterior');edge('changelog_retention','policy',C,'cites',needle='[retención de artefactos]')
# Explicit external citations resolve to existing graph identities; no fabricated target stubs.
for rel,owner in [(P,'policy'),(V,'qa')]:
 for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)',texts[rel]):
  dest=m.group(1).split('#')[0]
  if '://' in dest:continue
  p=(root/pathlib.Path(rel).parent/dest).resolve()
  try:drel=str(p.relative_to(root))
  except ValueError:continue
  if drel in artifacts:edge(owner,artifacts[drel]['id'],rel,'cites',needle=m.group(0))
# Non-structural cross-file similarity in conservative treatment of unknown reproducibility.
existing=[n['id'] for n in old['nodes'] if n.get('source_file')==T and n['label']=='Semántica de la sesión obligatoria por delta documental']
if existing:edge('semantics',existing[0],P,'semantically_similar_to',needle='| Semántica por lote',conf='INFERRED',score=.85)
ids=[n['id'] for n in g['nodes']];assert len(ids)==len(set(ids));known=set(ids)|set(old_nodes)
for n in g['nodes']:
 assert re.fullmatch('[a-z0-9_]+',n['id']) and n['source_file'] in files
 assert n['file_type'] in ['code','document','paper','image','rationale','concept'] and '_origin' not in n
 assert all(k in n for k in basekeys)
for e in g['edges']:
 assert e['source'] in known and e['target'] in known,(e['source'],e['target'])
 assert e['source']!=e['target'] and e['source_file'] in files
 assert e['relation'] in ['calls','implements','references','cites','conceptually_related_to','shares_data_with','semantically_similar_to','rationale_for']
 assert (e['confidence']=='EXTRACTED' and e['confidence_score']==1) or (e['confidence']=='INFERRED' and e['confidence_score'] in [.95,.85,.75,.65,.55]) or (e['confidence']=='AMBIGUOUS' and .1<=e['confidence_score']<=.3)
for f in files:assert any(n['source_file']==f for n in g['nodes']) and any(e['source_file']==f for e in g['edges'])
assert all(pathlib.Path(assigned[r]).read_text()==s for r,s in texts.items()),'source changed during extraction'
(run/'chunk-00.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(run/'chunk-00.json'),'nodes':len(g['nodes']),'edges':len(g['edges']),'hyperedges':0,'files':len(files),'preserved_semantic_nodes':kept[0],'preserved_semantic_edges':kept[1],'validated':'schema, IDs, endpoint union, source coverage, historical SHA-256, current source stability','measured_usage':'UNAVAILABLE; zero schema placeholders'}))
