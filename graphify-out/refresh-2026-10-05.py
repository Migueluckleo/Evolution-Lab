"""Auditable local Graphify refresh; preserves unchanged semantic evidence.
Run phases explicitly. Outputs stay under graphify-out, outside scan corpus.
"""
from pathlib import Path
import json, hashlib, shutil, sys, re
from collections import Counter
from graphify.detect import detect

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'graphify-out'
RUN = OUT / 'runs' / (sys.argv[2] if len(sys.argv) > 2 else '2026-10-05')
SPEC = ROOT / '.codex/skills/graphify/references/extraction-spec.md'
EXACT_DATA = ['sources/inventories/tokens.inventory.json',
              'sources/figma-snapshots/input-fields.followups.target-tokens.json',
              'qa/implementations/select.v0.1.0.tokens.json']
def read(p): return json.loads(Path(p).read_text())
def dump(p, d):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2))
def digest(p, algorithm='md5'):
    return hashlib.new(algorithm, Path(p).read_bytes()).hexdigest()
def rel(p):
    p = Path(p)
    return p.resolve().relative_to(ROOT).as_posix() if p.is_absolute() else p.as_posix()

def prepare():
    RUN.mkdir(parents=True, exist_ok=True)
    backup = RUN / 'before'
    backup.mkdir(exist_ok=True)
    for name in ['graph.json','graph.html','GRAPH_REPORT.md','manifest.json',
                 '.graphify_health.json','.graphify_labels.json','.graphify_labels.json.sig','cost.json']:
        if (OUT/name).exists() and not (backup/name).exists(): shutil.copy2(OUT/name,backup/name)
    d = detect(ROOT)
    excluded_roots = {'graphify-out','output','tmp','.codex-build','.codex-finalizer'}
    excluded = []
    for kind, paths in d['files'].items():
        excluded.extend(p for p in paths if Path(rel(p)).parts[0] in excluded_roots)
        d['files'][kind] = [p for p in paths if Path(rel(p)).parts[0] not in excluded_roots]
    d['excluded_derived'] = excluded
    # Exact supplement: data structures inspected, no global secret-filter bypass.
    for name in EXACT_DATA:
        obj=read(ROOT/name)
        assert isinstance(obj,dict)
        assert any(k in obj for k in ['collections','vars','issues'])
        def keys(x):
            if isinstance(x,dict):
                for k,v in x.items():
                    if re.search(r'^(password|passwd|secret|api_key|access_token|refresh_token|private_key)$',k,re.I):
                        raise ValueError('Credential-like field: '+name)
                    yield k
                    yield from keys(v)
            elif isinstance(x,list):
                for y in x: yield from keys(y)
        list(keys(obj))
        d['files']['code'].append(str(ROOT/name))
    d['supplemental_design_data']=EXACT_DATA
    d['total_files']=sum(map(len,d['files'].values()))
    from graphify.detect import count_words
    d['total_words']=sum(count_words(Path(p)) for kind in ('code','document','paper') for p in d['files'].get(kind,[]))
    d['warning']='Large existing corpus; unchanged semantic contributions reused by hash, only changed documents/images re-extracted.'
    dump(RUN/'detection.json',d)
    old=read(backup/'graph.json'); manifest=read(backup/'manifest.json')
    graph_sources={rel(n['source_file']) for n in old['nodes'] if n.get('source_file')}
    semantic=d['files']['document']+d['files']['paper']+d['files']['image']
    reuse=[]; todo=[]
    for f in semantic:
        p=rel(f); m=manifest.get(p,{})
        hashes=[m.get('semantic_hash'),m.get('ast_hash')]
        if p in graph_sources and digest(f) in hashes: reuse.append(f)
        else: todo.append(f)
    # Same-source reuse has an explicit content-hash check; do not misattribute
    # these historical extractions to today's prompt cache.
    chunks=[]
    documents=sorted(f for f in todo if f not in d['files']['image'])
    for i in range(0,len(documents),22): chunks.append(documents[i:i+22])
    for f in d['files']['image']:
        if f in todo: chunks.append([f])
    dump(RUN/'semantic-plan.json',{'reused':reuse,'chunks':chunks,
         'reuse_basis':'Existing graph source_file + manifest content MD5; original provenance retained',
         'prompt_sha256':digest(SPEC,'sha256')})
    for i,files in enumerate(chunks): dump(RUN/f'chunk-{i:02d}.files.json',files)
    print(json.dumps({'corpus':d['total_files'],'reused_docs':len(reuse),'semantic_files':len(todo),
                     'chunks':len(chunks),'categories':{k:len(v) for k,v in d['files'].items()}}))

def ast():
    from graphify.extract import extract
    d=read(RUN/'detection.json')
    result=extract([Path(p) for p in d['files']['code']],cache_root=ROOT)
    dump(RUN/'ast.json',result)
    sources={rel(n['source_file']) for n in result['nodes'] if n.get('source_file')}
    print(json.dumps({'ast_nodes':len(result['nodes']),'ast_edges':len(result['edges']),
       'files_without_nodes':[rel(p) for p in d['files']['code'] if rel(p) not in sources]}))

def artifact_id(p):
    path=Path(rel(p))
    return re.sub('[^a-z0-9_]', '_', str(path.with_suffix('')).lower())+'_artifact_'+path.suffix.lstrip('.').lower()

def normalize_fragment(chunk):
    # Citation stubs cannot overwrite a definition extracted from its own file.
    # Provenance remains the citing file; actual file definitions take priority.
    for n in chunk['nodes']:
        if n.get('source_file'):
            stem=re.sub('[^a-z0-9_]','_',str(Path(rel(n['source_file'])).with_suffix('')).lower())
            if n.get('label','').lower().startswith('referenced ') or not n['id'].startswith(stem+'_'):
                n['reference_only']=True
    return chunk

def current_semantic_fragments(plan):
    fragments=[normalize_fragment(read(RUN/f'chunk-{i:02d}.json'))
               for i in range(len(plan['chunks']))]
    for path in sorted(RUN.glob('delta-*.json')):
        delta=normalize_fragment(read(path))
        replaced={rel(n['source_file']) for n in delta['nodes']
                  if n.get('source_file') and not n.get('reference_only')}
        for fragment in fragments:
            fragment['nodes']=[n for n in fragment['nodes']
                if rel(n.get('source_file','')) not in replaced or n.get('reference_only')]
            fragment['edges']=[e for e in fragment.get('edges',[])
                if rel(e.get('source_file','')) not in replaced]
            fragment['hyperedges']=[h for h in fragment.get('hyperedges',[])
                if rel(h.get('source_file','')) not in replaced]
        fragments.append(delta)
    return fragments

def supplement():
    from urllib.parse import unquote
    d=read(RUN/'detection.json')
    paths={rel(p):Path(p) for group in d['files'].values() for p in group}
    nodes=[]; edges=[]; broken=[]
    def edge(a,b,f,loc,relation='references'):
        if a != b: edges.append({'source':a,'target':b,'relation':relation,
             'confidence':'EXTRACTED','confidence_score':1.0,'weight':1.0,
             'source_file':f,'source_location':loc,'_origin':'ast'})
    for p,f in paths.items():
        ft='image' if f.suffix.lower() in ('.png','.jpg','.jpeg') else 'document'
        node={'id':artifact_id(p),'label':f.name,'file_type':ft,'source_file':p,
             'source_location':'L1' if ft=='document' else None,'_origin':'ast',
             'extraction_scope':'file identity, explicit references; semantic entities indexed separately',
             'sha256':digest(f,'sha256')}
        nodes.append(node)
        if f.suffix=='.md':
            for number,line in enumerate(f.read_text().splitlines(),1):
                for match in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',line):
                    target=match.group(1).split(' "')[0].strip('<>').split('#')[0]
                    if not target or re.match(r'\w+:',target) or '{' in target: continue
                    q=(f.parent/unquote(target)).resolve()
                    if not q.is_relative_to(ROOT):continue
                    rp=rel(q)
                    if rp in paths: edge(node['id'],artifact_id(rp),p,'L'+str(number))
                    elif not q.exists(): broken.append({'source':p,'line':number,'target':target})
        elif f.suffix=='.json':
            obj=read(f)
            if isinstance(obj,dict):
                node['data_keys']=list(obj)
                # Status is quoted data, not normalized to a broader validation.
                node['recorded_status']={k:v for k,v in obj.items() if isinstance(v,(str,bool,int))
                     and any(s in k.lower() for s in ['status','contract','version','date','filekey'])}
            def strings(x,pointer=''):
                if isinstance(x,dict):
                    for k,v in x.items():yield from strings(v,pointer+'/'+k)
                elif isinstance(x,list):
                    for i,v in enumerate(x):yield from strings(v,pointer+'/'+str(i))
                elif isinstance(x,str):yield x,pointer
            for value,pointer in strings(obj):
                if value in paths: edge(node['id'],artifact_id(value),p,'JSON:'+pointer)
            if p=='sources/inventories/tokens.inventory.json':
                byid={}; variables=[]
                for ci,col in enumerate(obj.get('collections',[])):
                    for vi,var in enumerate(col.get('variables',[])):
                        nid=artifact_id(p)+'_'+re.sub('[^a-z0-9_]','_',var['id'].lower())
                        byid[var['id']]=nid
                        pointer=f'/collections/{ci}/variables/{vi}'
                        nodes.append({'id':nid,'label':var['name'],'file_type':'concept',
                            'source_file':p,'source_location':'JSON:'+pointer,'_origin':'ast',
                            'collection':col['name'],'resolvedType':var.get('resolvedType'),
                            'description':var.get('description'),'scopes':var.get('scopes'),
                            'rationale':'Design token observed in canonical inventory; not a Figma live binding audit.'})
                        variables.append((nid,var,pointer))
                        edge(node['id'],nid,p,'JSON:'+pointer)
                for nid,var,pointer in variables:
                    for mode,val in var.get('valuesByMode',{}).items():
                        if isinstance(val,dict) and val.get('type')=='VARIABLE_ALIAS' and val.get('id') in byid:
                            edge(nid,byid[val['id']],p,'JSON:'+pointer+'/valuesByMode/'+mode)
    dump(RUN/'structural-supplement.json',{'nodes':nodes,'edges':edges,'hyperedges':[],
          'input_tokens':0,'output_tokens':0,'broken_links':broken})
    print(json.dumps({'artifacts':len(paths),'nodes':len(nodes),'references':len(edges),'broken_links':broken}))

def assemble():
    from graphify.build import build_from_json, mint_external_stubs_in_data
    from graphify.cluster import cluster, score_all, community_member_sigs
    from graphify.analyze import god_nodes, surprising_connections, suggest_questions
    from graphify.report import generate
    from graphify.export import to_json
    from graphify.diagnostics import diagnose_extraction
    d=read(RUN/'detection.json'); plan=read(RUN/'semantic-plan.json')
    sem=[]; covered=set()
    for i,files in enumerate(plan['chunks']):
        chunk=normalize_fragment(read(RUN/f'chunk-{i:02d}.json'))
        represented={rel(n['source_file']) for n in chunk['nodes'] if n.get('source_file') and not n.get('reference_only')}
        absent=set(map(rel,files))-represented
        assert not absent,(i,absent)
        sem.append(chunk); covered.update(map(rel,files))
    for p in sorted(RUN.glob('delta-*.json')):
        chunk=normalize_fragment(read(p)); sem.append(chunk)
        covered.update(rel(n['source_file']) for n in chunk['nodes'] if n.get('source_file') and not n.get('reference_only'))
    sem=current_semantic_fragments(plan)
    ast_data=read(RUN/'ast.json'); structural=read(RUN/'structural-supplement.json')
    replaced=covered | {rel(p) for p in d['files']['code']}
    old=read(RUN/'before/graph.json')
    current_sources={rel(p) for group in d['files'].values() for p in group}
    old_nodes=[n for n in old['nodes'] if rel(n.get('source_file','')) not in replaced and (not n.get('source_file') or rel(n['source_file']) in current_sources)]
    retained={n['id'] for n in old_nodes}
    old_edges=[e for e in old.get('links',old.get('edges',[]))
               if e['source'] in retained and e['target'] in retained
               and rel(e.get('source_file','')) not in replaced]
    # Sources are replaced explicitly before assembly, not silently unioned.
    nodes={n['id']:dict(n) for n in old_nodes}; edges=list(old_edges)
    raw_semantic=[]
    for fragment in [ast_data]+sem+[structural]:
        for n in fragment['nodes']:
            n=dict(n)
            if n.get('source_file'):n['source_file']=rel(n['source_file'])
            if fragment in sem:n['_origin']='semantic'
            # Prefer richer metadata over cross-file reference stubs.
            previous=nodes.get(n['id'])
            if previous is None or (previous.get('reference_only') and not n.get('reference_only')) or (
                not n.get('reference_only') and len(n)>=len(previous)):
                nodes[n['id']]=n
        for e in fragment.get('edges',[]):
            e=dict(e)
            if e.get('confidence')=='EXTRACTED': e.setdefault('confidence_score',1.0)
            if e.get('source_file'):e['source_file']=rel(e['source_file'])
            edges.append(e)
        if fragment in sem:raw_semantic.append(fragment)
    # Connect entity evidence to its containing file, never infer approval.
    for n in list(nodes.values()):
        p=n.get('source_file')
        if p and artifact_id(p) in nodes and n['id']!=artifact_id(p):
            edges.append({'source':artifact_id(p),'target':n['id'],'relation':'references',
                'confidence':'EXTRACTED','confidence_score':1.0,'weight':1.0,
                'source_file':p,'source_location':n.get('source_location')})
    old_hyperedges=old.get('hyperedges',old.get('graph',{}).get('hyperedges',[]))
    kept_hyperedges=[h for h in old_hyperedges if all(n in retained for n in h.get('nodes',[]))]
    raw={'nodes':list(nodes.values()),'edges':edges,'hyperedges':kept_hyperedges+[
        h for fragment in sem for h in fragment.get('hyperedges',[])],
        'input_tokens':0,'output_tokens':0}
    mint_external_stubs_in_data(raw)
    nodes={n['id']:n for n in raw['nodes']}
    dump(RUN/'combined-raw.json',raw)
    missing=[e for e in edges if e['source'] not in nodes or e['target'] not in nodes]
    assert not missing,('missing endpoints',missing[:5])
    # NetworkX simple graph supports one edge/pair. Preserve all explicit
    # evidence in attributes and raw extraction instead of losing relations.
    pairs={}; selfloops=[]
    directed=old.get('directed',False)
    for e in edges:
        if e['source']==e['target']:selfloops.append(e);continue
        key=(e['source'],e['target']) if directed else tuple(sorted([e['source'],e['target']]))
        if key not in pairs:
            pairs[key]=dict(e);pairs[key]['evidence_records']=[]
        records=e.get('evidence_records') or [{k:e.get(k) for k in ['source','target','relation','confidence','confidence_score','source_file','source_location']}]
        for rec in records:
            if rec not in pairs[key]['evidence_records']:pairs[key]['evidence_records'].append(rec)
    for e in pairs.values():
        e['relations']=sorted(set(r['relation'] for r in e['evidence_records'] if r['relation']))
    consolidated={**raw,'edges':list(pairs.values())}
    dump(RUN/'combined.json',consolidated)
    health=diagnose_extraction(consolidated,directed=directed,root=str(ROOT))
    health['refresh_date']='2026-10-05';health['raw_edge_count']=len(edges)
    health['consolidated_pairs']=len(pairs);health['self_references_excluded']=len(selfloops)
    health['provenance_note']='All pair evidence preserved in evidence_records and combined-raw.json; token usage unavailable.'
    G=build_from_json(consolidated,root=str(ROOT),directed=directed)
    # Graphify canonicalizes file-root semantic nodes into file artifacts.
    # This can turn their explicit membership edges into trivial self-links.
    # Remove only references created by that normalization, retaining raw evidence.
    normalization_loops=[(u,v,dict(attrs)) for u,v,attrs in G.edges(data=True) if u==v]
    assert all(e.get('relation')=='references' for _,_,e in normalization_loops), 'Unexpected semantic self-loop'
    dump(RUN/'normalization-cleanup.json',{'removed_self_references':normalization_loops,
       'reason':'File identity normalization; raw extraction preserved; no source document changed'})
    G.remove_edges_from((u,v) for u,v,_ in normalization_loops)
    health['normalization_self_references_removed']=len(normalization_loops)
    health['exported_node_count']=G.number_of_nodes()
    health['exported_edge_count']=G.number_of_edges()
    communities=cluster(G); cohesion=score_all(G,communities)
    labels={}
    for cid,members in communities.items():
        sources=Counter(Path(G.nodes[n].get('source_file','')).stem for n in members)
        common=sources.most_common(1)[0][0] if sources else 'Evidence'
        title=re.sub(r'\.v\d+(?:\.\d+)*','',common)
        title=re.sub(r'\.(?:contract|component|source|review|state|amendment|candidate|figma|json|yaml)','',title)
        title=re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ0-9 ]',' ',title)
        title=' '.join(title.split()[:5])
        labels[cid]=title.title() or 'Evidencia del proyecto'
        hub=max(members,key=lambda n:G.degree(n))
        hub_file=G.nodes[hub].get('source_file','')
        override={'registry/qa.md':'QA y evidencias','registry/contracts.md':'Contratos e implementación',
          'registry/sources.md':'Fuentes y procedencia','registry/decisions.md':'Decisiones de migración',
          'specs/MIGRATION-AUDIT.md':'Auditoría por excepciones',
          'specs/MIGRATION-TRACEABILITY-STATUS.md':'Continuidad y pendientes',
          'sources/inventories/tokens.inventory.json':'Primitivas y aliases'}
        if hub_file in override:labels[cid]=override[hub_file]
    dump(RUN/'community-proposals.json',{str(cid):{'label':labels[cid],
         'nodes':len(members),'cohesion':cohesion[cid],
         'examples':[G.nodes[n].get('label',n) for n in sorted(members,key=lambda n:G.degree(n),reverse=True)[:5]]}
         for cid,members in communities.items()})
    curated=RUN/'curated-labels.json'
    if curated.exists(): labels.update({int(k):v for k,v in read(curated).items()})
    gods=god_nodes(G);surprises=surprising_connections(G,communities)
    questions=suggest_questions(G,communities,labels)
    if not to_json(G,communities,str(OUT/'graph.json'),community_labels=labels):
        raise RuntimeError('Shrink guard refused; backup preserved. Do not force.')
    health['exported_graph_sha256']=digest(OUT/'graph.json','sha256')
    dump(OUT/'.graphify_health.json',health)
    report=generate(G,communities,cohesion,labels,gods,surprises,d,
                    {'input':0,'output':0},str(ROOT),suggested_questions=questions)
    report=report.replace('- Token cost: 0 input · 0 output',
        '- Token cost: UNAVAILABLE (host-agent measured usage not exposed; not zero).')
    confidence_counts=Counter(attrs.get('confidence','UNSPECIFIED') for _,_,attrs in G.edges(data=True))
    confidence_summary=', '.join(f'{k}: {v} ({100*v/G.number_of_edges():.2f}%)' for k,v in sorted(confidence_counts.items()))
    report=re.sub(r'^- Extraction:.*$', '- Edge provenance (primary relation per pair): '+confidence_summary, report, flags=re.M)
    report+='\n\n## Refresh provenance · 2026-10-05\n\n'
    actual_reused=set(map(rel,plan['reused']))-covered
    report+='The extraction reuses '+str(len(actual_reused))+' unchanged source contributions verified by content hashes. '
    report+='Updated documents were read by Codex extraction agents; JSON identity/references and canonical token aliases were extracted deterministically. '
    report+='Token counters shown as zero by the template are placeholders: measured agent token usage is unavailable, not zero cost. '
    report+='Historical specs, QA and snapshots remain historical; graph currency does not certify Figma or approval. '
    report+='Full corpus, exact supplemental token paths, raw edge provenance and backup live under runs/'+RUN.name+'/.\n'
    report+='Effective scope: '+str(d['total_files'])+' files, including 3 explicitly inspected design-data JSON files. Derived exports, temporary renders and graph outputs excluded.\n'
    report+='Suggested questions and community heuristics above are navigation aids, not authorized tasks or confirmed Design System defects.\n'
    (OUT/'GRAPH_REPORT.md').write_text(report)
    dump(OUT/'.graphify_labels.json',{str(k):v for k,v in labels.items()})
    dump(OUT/'.graphify_labels.json.sig',{str(k):v for k,v in community_member_sigs(communities).items()})
    dump(RUN/'analysis.json',{'nodes':G.number_of_nodes(),'edges':G.number_of_edges(),
         'communities':len(communities),'gods':gods,'surprises':surprises,'questions':questions})
    print(json.dumps({'nodes':G.number_of_nodes(),'edges':G.number_of_edges(),
       'communities':len(communities),'health':health},ensure_ascii=False))

def verify():
    d=read(RUN/'detection.json'); g=read(OUT/'graph.json'); health=read(OUT/'.graphify_health.json')
    files={rel(p) for group in d['files'].values() for p in group}
    nodes=g['nodes'];edges=g.get('links',g.get('edges',[]));ids={n['id'] for n in nodes}
    sources={rel(n['source_file']) for n in nodes if n.get('source_file')}
    missing=files-sources
    errors=[]
    if missing:errors.append({'unrepresented_files':sorted(missing)})
    if len(ids)!=len(nodes):errors.append('Duplicate node IDs')
    if any(e['source'] not in ids or e['target'] not in ids for e in edges):errors.append('Missing edge endpoint')
    if any(e['source']==e['target'] for e in edges):errors.append('Self-loop')
    for p in files:
        if not (ROOT/p).exists():errors.append({'missing_source':p})
    report=(OUT/'GRAPH_REPORT.md').read_text()
    html=(OUT/'graph.html').read_text()
    # HTML emitter may aggregate graph >5000 nodes; expected labels tested separately.
    if len(html)<1000:errors.append('Empty HTML')
    if len(nodes)<=5000:
        match=re.search(r'const RAW_NODES\s*=\s*',html)
        if not match:errors.append('HTML lacks raw node payload')
        else:
            html_nodes,_=json.JSONDecoder().raw_decode(html[match.end():])
            if {n['id'] for n in html_nodes}!=ids:errors.append('HTML nodes differ from JSON export')
    if 'Refresh provenance' not in report:errors.append('Report lacks run provenance')
    if health.get('exported_graph_sha256')!=digest(OUT/'graph.json','sha256'):
        errors.append('Health sidecar does not match graph hash')
    if health.get('exported_node_count')!=len(nodes) or health.get('exported_edge_count')!=len(edges):
        errors.append('Health sidecar counts differ from graph')
    stale_artifacts=[n['source_file'] for n in nodes if n.get('sha256')
        and n.get('source_file') in files and n['sha256']!=digest(ROOT/n['source_file'],'sha256')]
    if stale_artifacts:errors.append({'stale_artifact_hashes':stale_artifacts})
    canonical=digest(ROOT/'sources/inventories/tokens.inventory.json','sha256')
    if canonical!='cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474':
        errors.append('Canonical inventory changed unexpectedly')
    result={'date':'2026-10-05','status':'PASS' if not errors else 'FAILED','errors':errors,
      'corpus_files':len(files),'represented_files':len(files&sources),'graph_nodes':len(nodes),
      'graph_edges':len(edges),'canonical_inventory_sha256':canonical,
      'reference_only_missing_paths':sorted(p for p in sources-files if not (ROOT/p).exists()),
      'output_sha256':{p:digest(OUT/p,'sha256') for p in ['graph.json','graph.html','GRAPH_REPORT.md']},
      'scope':'Graph freshness, file coverage and integrity only; no live Figma revalidation'}
    dump(RUN/'verification.json',result)
    print(json.dumps(result,ensure_ascii=False))
    assert not errors,errors

def manifest():
    from graphify.detect import save_manifest
    from graphify.cache import save_semantic_cache
    from datetime import datetime, timezone
    d=read(RUN/'detection.json');plan=read(RUN/'semantic-plan.json'); g=read(OUT/'graph.json')
    # Complete evidence has already passed verification. Semantic placeholders
    # and failed/absent chunks never reach this gate.
    assert read(RUN/'verification.json')['status']=='PASS'
    stamped={k:list(v) for k,v in d['files'].items()}
    save_manifest(stamped,manifest_path=str(OUT/'manifest.json'),root=ROOT,
      scan_corpus={p for group in stamped.values() for p in group})
    # Cache only fresh host-agent extractions under today's extraction prompt.
    chunks=current_semantic_fragments(plan)
    nn=[n for c in chunks for n in c['nodes']];ee=[e for c in chunks for e in c['edges']]
    hh=[h for c in chunks for h in c.get('hyperedges',[])]
    allowed={p for group in plan['chunks'] for p in group}
    for p in RUN.glob('delta-*.json'):
        allowed.update(n['source_file'] for n in read(p)['nodes']
                       if n.get('source_file') and not n.get('reference_only'))
    saved=save_semantic_cache(nn,ee,hh,root=ROOT,allowed_source_files=list(allowed),prompt_file=SPEC)
    m=read(OUT/'manifest.json');mismatches=[]
    for paths in stamped.values():
        for f in paths:
            if m.get(rel(f),{}).get('semantic_hash')!=digest(f):mismatches.append(rel(f))
    assert not mismatches,mismatches
    cost=read(RUN/'before/cost.json')
    cost.setdefault('runs',[]).append({'date':datetime.now(timezone.utc).isoformat(),
        'files':d['total_files'],'input_tokens':None,'output_tokens':None,
        'usage_status':'UNAVAILABLE: host agents do not expose measured usage',
        'method':'AST + content-verified semantic reuse + host-agent extraction + explicit references'})
    cost['totals_scope']='Historical measured counters only; latest unmeasured host-agent run excluded.'
    dump(OUT/'cost.json',cost)
    dump(RUN/'manifest-check.json',{'status':'PASS','checked_files':sum(map(len,stamped.values())),
          'hash_mismatches':mismatches,'fresh_semantic_cache_files':saved,
          'supplemental_paths':EXACT_DATA})
    print(json.dumps({'manifest_files':len(m),'hash_mismatches':mismatches,'cached_files':saved}))

if __name__=='__main__':
    {'prepare':prepare,'ast':ast,'supplement':supplement,'assemble':assemble,
     'verify':verify,'manifest':manifest}[sys.argv[1]]()
