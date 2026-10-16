import copy
import json
import re
from pathlib import Path

ROOT = Path('/Users/miguel.leo/Documents/ChatGPT/CONTPAQi-designSystem')
RUN = ROOT / 'graphify-out/runs/2026-10-09-fuentes'
files = json.loads((RUN / 'chunk-01.files.json').read_text())
rel_to_abs = {str(Path(f).relative_to(ROOT)): f for f in files}
old = json.loads((RUN / 'before/graph.json').read_text())
old_by_id = {n['id']: n for n in old['nodes']}

def absolute_source(value):
    if isinstance(value, dict):
        return {k: rel_to_abs.get(v, v) if k == 'source_file' and isinstance(v, str) else absolute_source(v) for k, v in value.items()}
    if isinstance(value, list):
        return [absolute_source(v) for v in value]
    return value

nodes = {n['id']: absolute_source(copy.deepcopy(n)) for n in old['nodes'] if n.get('source_file') in rel_to_abs and n.get('_origin') != 'ast'}
edges = [absolute_source(copy.deepcopy(e)) for e in old['links'] if e.get('source_file') in rel_to_abs and e.get('_origin') != 'ast']
hyperedges = [absolute_source(copy.deepcopy(h)) for h in old.get('hyperedges', []) if h.get('source_file') in rel_to_abs]
retained = {'nodes': len(nodes), 'edges': len(edges), 'hyperedges': len(hyperedges)}
reuse_rationale = ('Section-level incremental extraction: historical semantic contributions retained verbatim in meaning and status from before/graph.json; '
                   'only the additive Fuentes section and adjacent context were read this turn. No claim of rereading the entire historical registry. '
                   'Source paths normalized to FILE_LIST absolute paths; historical null line citations remain null.')

def nid(rel, label):
    return re.sub('[^a-z0-9_]', '_', str(Path(rel).with_suffix('')).lower()) + '_' + re.sub('[^a-z0-9_]', '_', label.lower())

def node(rel, label, line, **attrs):
    key = nid(rel, label)
    nodes[key] = dict(id=key, label=label, file_type='concept', source_file=rel_to_abs[rel], source_location=f'L{line}', source_url=None, captured_at=None, author=None, contributor=None, **attrs)
    return key

def edge(rel, source, target, line, relation='references'):
    edges.append(dict(source=source, target=target, relation=relation, confidence='EXTRACTED', confidence_score=1.0, source_file=rel_to_abs[rel], source_location=f'L{line}', weight=1.0))

def refs(rel, src, line, paths):
    for label, path in paths:
        key = node(rel, 'Fuentes reference ' + path, line, reference_only=True, reference_target=str((ROOT / 'registry' / path).resolve()), reference_label=label)
        nodes[key]['file_type'] = 'document'
        edge(rel, src, key, line, 'cites')

contract = ('Fuentes contract', '../specs/components/fuentes.contract.v0.1.0.md')
qa = ('Fuentes technical visual QA', '../qa/implementations/fuentes.v0.1.0.review.md')
state = ('Fuentes target state and IDs', '../implementations/figma/fuentes.v0.1.0.state.json')

r = 'registry/SLOTS-REVIEW-STATUS.md'
s = node(r, 'Fuentes native Path Slots required and implemented', 80, applicability='REQUIRED', implementation_status='IMPLEMENTED', property='Path#848:9', slot_ids=['848:19', '848:33'], variants=['Default', 'Hover'], rationale=reuse_rationale)
p = node(r, 'Fuentes Path consumer composition and variant retention', 80, operations=['insert', 'remove', 'reorder', 'replace'], cardinalities_tested=[0, 1, 2, 4], state_swap='PRESERVES_OVERRIDES', long_text_width_px=150, long_text='REFLOWS', empty_height_px=16, business_policy='NOT_INFERRED')
i = node(r, 'Fuentes Path Item fixed anatomy excludes Slot requirement', 80, applicability='NOT_APPLICABLE', anatomy=['Label', 'optional separator'], rationale='Fixed segment anatomy is controlled by Label and optional separator rather than variable consumer composition.')
edge(r, s, p, 80, 'implements')
edge(r, s, i, 80, 'conceptually_related_to')
refs(r, s, 80, [contract, qa])

r = 'registry/contracts.md'
c = node(r, 'FUENTES-001 and FOUNDATIONS-FUENTES-HOVER-001 delegated specs publication', 528, version='0.1.0', contract_status='DELEGATED_FOR_BUILD', human_audit='PENDING', documentary_qa='PASS', technical_qa='PASS', publication_location='specs', rationale='Publication in specs follows documentary and technical QA PASS under external delegation; it does not imply human approval. ' + reuse_rationale)
d = node(r, 'Fuentes source Navi 64 4164 and unchanged local Dot', 528, source_node='64:4164', source_name='Navi', variant_count=2, native_path_slot=True, reused_dependency='local Dot', dependency_main_modified=False)
edge(r, c, d, 528, 'references')
refs(r, c, 528, [contract, ('Fuentes Hover semantic role contract', '../specs/foundations/fuentes-hover.contract.v0.1.0.md'), ('Fuentes documentary QA', '../qa/contracts/fuentes.v0.1.0.review.md'), qa, state])

r = 'registry/environment.md'
e = node(r, 'Fuentes corporate Figma destination access and source read only', 355, destination='AI DS', source='Navi', source_access='READ_ONLY', destination_access='READ_WRITE', capabilities_verified=['Slots', 'reflow', 'variables'], new_installations=False, external_services=False, new_credentials=False, remote_publication=False, rationale=reuse_rationale)
g = node(r, 'Fuentes graph closure requires verified structural and semantic delta', 355, closure_path='graphify-out/runs/2026-10-09-fuentes/closure.json', graph_status='NOT_INFERRED_CURRENT', verification_required=True, rationale='The actual closure result must be read from closure.json after verification; the registry does not establish CURRENT in advance.')
edge(r, e, g, 355, 'references')
refs(r, e, 355, [state, qa])
refs(r, g, 355, [('Fuentes Graphify closure gate', '../graphify-out/runs/2026-10-09-fuentes/closure.json')])

r = 'registry/implementations.md'
m = node(r, 'IMP-FUENTES-FIGMA-001 visual contract technically validated', 520, implementation_status='VALIDATED', validation_scope='visual contract with documented accessibility limitations', human_audit='PENDING', library_publication='NOT_PERFORMED', rationale=reuse_rationale)
t = node(r, 'Fuentes target component IDs and visual review', 520, destination='AI DS', page_name='Fuentes', page_id='847:7', set_id='848:41', default_id='848:11', hover_id='848:26', path_item_id='848:8', review_id='848:42')
v = node(r, 'Fuentes validation coverage and semantic variable extension', 520, paints=22, themes=4, slot_cardinalities=[0, 1, 2, 4], long_text_width_px=150, new_semantic_variables=1, new_primitives=0)
edge(r, m, t, 520, 'references')
edge(r, m, v, 520, 'references')
refs(r, m, 520, [contract, state, qa])

new_node_count = len(nodes) - retained['nodes']
new_edge_count = len(edges) - retained['edges']
stub_count = 0
for obj in edges + hyperedges:
    endpoint_ids = obj.get('nodes', [obj.get('source'), obj.get('target')])
    for key in endpoint_ids:
        if key in nodes:
            continue
        original = old_by_id.get(key)
        assert original is not None, f'Historical missing endpoint: {key}'
        nodes[key] = dict(id=key, label=original['label'], file_type=original.get('file_type', 'concept'), source_file=obj['source_file'], source_location=None, source_url=None, captured_at=None, author=None, contributor=None, reference_only=True, referenced_source_file=original.get('source_file'), rationale='Endpoint retained as a reference-only stub to preserve an existing semantic edge; not newly extracted or reread.')
        stub_count += 1

edge_map = {}
for e in edges:
    edge_map[(e['source'], e['target'], e['relation'], e['source_file'], e.get('source_location'))] = e
edges = list(edge_map.values())
for n in nodes.values():
    assert n['source_file'] in files
    assert re.fullmatch('[a-z0-9_]+', n['id'])
    assert n['file_type'] in {'code','document','paper','image','rationale','concept'}
for e in edges:
    assert e['source'] in nodes and e['target'] in nodes
    assert e['source_file'] in files
    assert e['confidence_score'] == 1.0 if e['confidence'] == 'EXTRACTED' else e['confidence_score'] != 0.5
fragment = dict(nodes=list(nodes.values()), edges=edges, hyperedges=hyperedges, input_tokens=0, output_tokens=0)
(RUN / 'chunk-01.json').write_text(json.dumps(fragment, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(file=str(RUN / 'chunk-01.json'), nodes=len(nodes), edges=len(edges), hyperedges=len(hyperedges), retained=retained, new_nodes=new_node_count, new_edges=new_edge_count, reference_endpoint_stubs=stub_count, coverage=files, errors=[], rationale=reuse_rationale, measured_usage='UNAVAILABLE_NOT_ZERO'), ensure_ascii=False))
