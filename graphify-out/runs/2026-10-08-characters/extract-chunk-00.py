"""Derived semantic extraction: authored concepts plus hash-verified history."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path('/Users/miguel.leo/Documents/ChatGPT/CONTPAQi-designSystem')
RUN = ROOT / 'graphify-out/runs/2026-10-08-characters'
FILES = json.loads((RUN / 'chunk-00.files.json').read_text())
REL = {str(Path(f).relative_to(ROOT)): f for f in FILES}
MANIFEST = json.loads((RUN / 'before/manifest.json').read_text())
OLD = json.loads((RUN / 'before/graph.json').read_text())
verified = {}
offsets = {}
for rel, absolute in REL.items():
    if rel not in MANIFEST:
        continue
    s = Path(absolute).read_text()
    start = s.index('\n## ')
    end = s.index('\n## ', start + 1)
    previous = s[:start] + s[end:]
    digest = hashlib.md5(previous.encode()).hexdigest()
    assert digest == MANIFEST[rel]['semantic_hash'], rel
    verified[rel] = digest
    offsets[rel] = s[start:end].count('\n')

def current_location(value, rel):
    if value is None:
        return None
    if isinstance(value, int):
        return value + offsets[rel] if value > 1 else value
    m = re.fullmatch(r'L(\d+)', str(value))
    if m:
        n = int(m[1])
        return 'L' + str(n + offsets[rel] if n > 1 else n)
    return None

nodes, edges = [], []
for original in OLD['nodes']:
    rel = original.get('source_file')
    if rel not in verified:
        continue
    node = {k: v for k, v in original.items() if k not in ['_origin', 'community', 'community_name', 'norm_label']}
    node['source_file'] = REL[rel]
    node['source_location'] = current_location(node.get('source_location'), rel)
    for key in ['source_url', 'captured_at', 'author', 'contributor']:
        node.setdefault(key, None)
    nodes.append(node)
for original in OLD['links']:
    rel = original.get('source_file')
    if rel not in verified:
        continue
    edge = {k: original.get(k) for k in ['source', 'target', 'relation', 'confidence', 'confidence_score']}
    edge.update(source_file=REL[rel], source_location=current_location(original.get('source_location'), rel), weight=original.get('weight', 1.0))
    # Preserve the original multi-citation evidence, without promoting it to authority.
    if original.get('evidence_records'):
        evidence = []
        for record in original['evidence_records']:
            r = dict(record)
            sf = r.get('source_file')
            if sf in verified:
                r['source_file'] = REL[sf]
                r['source_location'] = current_location(r.get('source_location'), sf)
            evidence.append(r)
        edge['evidence_records'] = evidence
    edges.append(edge)
historical_nodes, historical_edges = len(nodes), len(edges)

def stem(rel):
    return re.sub('[^a-z0-9_]', '_', str(Path(rel).with_suffix('')).lower())

def node(rel, entity, label, kind='concept', rationale=None, **extra):
    identifier = stem(rel) + '_' + entity
    item = dict(id=identifier, label=label, file_type=kind, source_file=REL[rel], source_location=None,
                source_url=None, captured_at=None, author=None, contributor=None)
    if rationale:
        item['rationale'] = rationale
    item.update(extra)
    nodes.append(item)
    return identifier

def edge(source, target, rel, relation='references', confidence='EXTRACTED', score=1.0):
    edges.append(dict(source=source, target=target, relation=relation, confidence=confidence,
                      confidence_score=score, source_file=REL[rel], source_location=None, weight=1.0))

contract = 'specs/characters.contract.v0.1.0.md'
main = node(contract, 'characters_001', 'CHARACTERS-001 v0.1.0: BENI Standby and NAVI Analysis', 'document',
    'Normative integration contract in specs, DELEGATED_FOR_BUILD after documentary and technical QA PASS; user audit PENDING and library UNPUBLISHED. Covers the nominated external source, not frontend or replacement of Conversation/Chat.',
    status='DELEGATED_FOR_BUILD', user_audit='PENDING', figma_page='Characters', figma_page_id='820:7')
beni = node(contract, 'beni_standby', 'BENI Standby: six Frame variants', rationale='Preserves source order Default, close, Variant4, Variant3, Variant5, Variant6 as Frame 01–06; set 822:6. Fixed illustration, not a product state API.')
navi = node(contract, 'navi_analysis', 'NAVI Analysis: seven Frame variants', rationale='Maps observed source 1,2,4,5,6,7,8 to Frame 01–07; set 822:7. The absent source frame 3 is not invented.')
identity = node(contract, 'fixed_character_identity', 'Fixed character identity exception', 'rationale', 'Four SHAPE_FILL colors in character-identity/Value are direct, invariant across themes, and have no semantic intermediary. Preserves the three existing identity tokens and adds only NAVI shadow; applies exclusively to character artwork.')
shadow = node(contract, 'navi_shadow_extension', 'NAVI shadow additive canonical extension', 'concept', 'color/characters/navi/shadow is governed exclusively by specs/tokens/ai-design-system.character-shadow.v0.1.0.json. The existing identity JSON and historical inventory remain intact.')
preservation = node(contract, 'vector_art_preservation', 'Vector anatomy and empty fills preserved', 'rationale', 'All thirteen frames keep 168.739990234375 × 163.739990234375 dimensions, hierarchy, layer order, constraints, 64 vector paths and 13 groups. Seventeen empty NAVI fills remain empty so Smart Animate correspondence is preserved.')
cycles = node(contract, 'two_local_smart_animate_cycles', 'Thirteen local Smart Animate transitions form two cycles', 'concept', 'AFTER_TIMEOUT → CHANGE_TO targets local frame IDs, retaining source timeout, duration and easing. Frame 01 starts each loop; the contract does not promise synchronization or perceptual playback certification.')
normalization = node(contract, 'figma_serialization_normalization', 'Figma vector and timing normalization evidence', 'rationale', 'Figma splits/reorders SVG subpaths and serializes floating point coordinates. Compare source round-tripped through temporary vectors to destination, with ≤0.001 px geometry and ≤0.000001 s timing tolerance; do not require raw SVG string equality or simplify artwork.')
slots = node(contract, 'slots_not_applicable', 'Characters Slots NOT_APPLICABLE', 'rationale', 'Eyes, moustache and shadow layers are fixed illustrative anatomy, not extensible consumer content. Do not create artificial Slots.')
limits = node(contract, 'frontend_semantics_unresolved', 'Frontend semantics and reduced motion UNRESOLVED', 'rationale', 'Standby/Analysis label observed sequences, not backend states. Accessible meaning, reduced motion and product behavior require a future consumer/frontend contract and remain outside this scope.')
for target in [beni, navi, identity, shadow, preservation, cycles, normalization, slots, limits]:
    edge(main, target, contract)
edge(identity, 'registry_dec_character_identity_001_fixed_identity', contract, 'implements')
edge(main, 'registry_dec_external_components_delegation_001_external_delegation', contract, 'implements')
edge(shadow, 'specs_tokens_ai_design_system_character_shadow_v0_1_0_artifact_json', contract)
edge(shadow, 'specs_tokens_ai_design_system_character_shadow_v0_1_0_artifact_json_color_characters_navi_shadow', contract)
edge(identity, 'specs_tokens_ai_design_system_character_identity_v0_1_0_artifact_json', contract)
edge(identity, shadow, contract)
edge(cycles, preservation, contract, 'conceptually_related_to')
edge(normalization, preservation, contract, 'rationale_for')

source_nodes = []
for name, title, root_id, count, variants, vectors, sequence, dims in [
    ('beni-standby', 'beniStandBy', '209:6943', 37, 6, 24, ['209:6942','209:6941','217:1900','217:1894','217:1907','217:1914'], [168.739990234375,163.739990234375]),
    ('navi-analysis', 'messageAnalisisNavi', '269:5947', 55, 7, 40, ['269:5944','509:17580','509:17675','509:17692','509:17699','509:17706','509:17713'], [168.739990234375,163.739990234375])]:
    md = f'drafts/contracts/{name}.source.component-contract.md'
    yaml = f'drafts/contracts/{name}.source.component-contract.yaml'
    obs = node(md, 'source_observation', title + ' read-only source contract', 'document',
        f'COMPLETE observed source inspection: {count} nodes, {variants} variants, {vectors} vectors and {variants} eye groups; no component, variable or style dependencies. Animation frames are not functional product states.',
        source_url=f'https://www.figma.com/design/IlNQJgDKvCSqyXAkONcjxl/Ecosistema-AI?node-id={root_id.replace(":", "-")}',
        source_node_id=root_id, inspection_status='COMPLETE')
    model = node(yaml, 'source_evidence_model', title + ' complete graphical evidence model', 'document',
        'Synchronized YAML model retains all-node evidence, exact vectorPaths, paints, constraints and reactions. Evidence HIGH for structural coverage; accessible meaning and product usage require definition.',
        inspected_nodes=count, vectors=vectors, component_count=variants, pending_nodes=0, source_node_id=root_id,
        sequence=sequence, frame_dimensions=dims, generated_at='2026-10-08T20:50:08Z')
    topology = node(yaml, 'observed_animation_cycle', title + ' observed closed timeout cycle', 'concept',
        'All reactions are AFTER_TIMEOUT/CHANGE_TO/SMART_ANIMATE and stay within the set. This is source evidence, not an inferred behavior contract.', sequence=sequence)
    edge(obs, model, md, 'shares_data_with')
    edge(model, topology, yaml)
    edge(main, obs, contract, 'cites')
    edge(cycles, topology, contract, 'implements')
    source_nodes.append(obs)
    if name == 'navi-analysis':
        empty = node(yaml, 'empty_shadow_layers', 'NAVI seventeen unfilled shadow vectors', 'rationale',
            'The full traversal includes seventeen empty fills; only source shadows 509:18311 and 509:18667 carry the original shadow RGB. Empty shadows must not be turned black or discarded.',
            shadow_color_rgb8=[214,116,61], unfilled_vector_count=17)
        edge(model, empty, yaml)
        edge(shadow, empty, contract, 'conceptually_related_to')
edge(source_nodes[0], source_nodes[1], 'drafts/contracts/beni-standby.source.component-contract.md', 'semantically_similar_to', 'INFERRED', 0.85)

pointer_file = 'drafts/contracts/characters.contract.v0.1.0.md'
pointer = node(pointer_file, 'promoted_contract_pointer', 'Characters draft is only a promoted-contract pointer', 'document',
    'Technical QA PASS on 2026-10-08 moved the normative contract to specs; the draft is not a second editable definition. Human audit remains PENDING and no remote publication occurred.')
edge(pointer, main, pointer_file)

docqa_file = 'qa/contracts/characters.v0.1.0.review.md'
docqa = node(docqa_file, 'documentary_qa_pass', 'Characters documentary QA PASS and closing revalidation', 'document',
    'The 21-section contract documents Frame mapping, 13 observed combinations, non-applicable Slots, canonical identity ownership, preflight and frontend exclusion. Closing revalidation accepts the documented API round-trip method without changing artwork; does not simulate human approval.')
edge(docqa, main, docqa_file)
edge(docqa, normalization, docqa_file)
edge(docqa, shadow, docqa_file)
tech_file = 'qa/implementations/characters.v0.1.0.review.md'
tech = node(tech_file, 'technical_qa_pass', 'Characters technical QA PASS / implementation VALIDATED', 'document',
    'Checks cover 90 frame nodes, 64 paths, 13 groups, 47 bindings, 13 reactions, four semantic themes and two 50% scale instances. All QA temporaries removed; no blocking conflict. Human audit PENDING; library UNPUBLISHED.')
roundtrip = node(tech_file, 'round_trip_resolves_textual_path_failures', '64 normalized paths match after initial 46 textual mismatches', 'rationale',
    'Initial raw-text comparison failed for 46/64 paths because of Figma serialization. All 64 source paths round-tripped through temporary Figma vectors match destination exactly. Largest geometry delta 0.00006103515625 px; one timeout delta 1.1921e-8 s is within 1e-6 tolerance. Original failures remain evidence.')
bindingqa = node(tech_file, 'identity_binding_and_theme_qa', '47 identity bindings and four invariant theme checks', 'concept',
    'All paints resolve to four direct SHAPE_FILL identity variables with canonical names, descriptions, codeSyntax and Value mode. Existing three variables unchanged; only new shadow VariableID:820:6. Two half-scale instances preserve bindings and geometry.')
perceptual = node(tech_file, 'perceptual_audit_pending', 'Perceptual playback audit PENDING', 'rationale',
    'Structural verification of the thirteen transitions and two closed cycles does not certify perceived playback or accessibility. Reduced motion and backend remain outside scope.')
contrast = node(tech_file, 'artwork_contrast_observed', 'Artwork contrast observed, not WCAG certification', 'concept',
    'Original identity retained: features/BENI 5.381:1; features/NAVI 2.028:1; shadow/NAVI body 1.278:1. These illustrations are neither text nor controls, so no general WCAG PASS/FAIL is asserted.',
    ratios={'features_beni':5.381,'features_navi':2.028,'shadow_navi':1.278})
for target in [main, roundtrip, bindingqa, perceptual, contrast]:
    edge(tech, target, tech_file)
edge(roundtrip, normalization, tech_file, 'implements')
edge(bindingqa, identity, tech_file, 'implements')
edge(perceptual, limits, tech_file, 'conceptually_related_to')
edge(docqa, tech, docqa_file)

handoff_file = 'registry/SESSION-HANDOFF-2026-10-08-CHARACTERS.md'
handoff = node(handoff_file, 'characters_closure', 'Characters closure and bounded continuation', 'document',
    'Source inspected read-only; new Characters page 820:7, sets 822:6/822:7 and review 822:21 constructed and technically validated. Three identity tokens reused and NAVI shadow added. Conversation, Chat, historical inventory and original identity JSON preserved; no next family authorized.')
graphgate = node(handoff_file, 'graph_current_gate', 'Characters graph CURRENT conditional on verification and hashes', 'rationale',
    'Run 2026-10-08-characters remains STALE during extraction. CURRENT requires verification.json and manifest-check.json PASS plus matching corpus hashes recorded in closure.json; the derived graph cannot grant design approval.')
edge(handoff, main, handoff_file)
edge(handoff, tech, handoff_file)
edge(handoff, graphgate, handoff_file)

registry_new = [
    ('registry/SLOTS-REVIEW-STATUS.md','characters_fixed_anatomy','Characters: fixed illustration, Slots NOT_APPLICABLE', 'Eyes/shadows are fixed anatomical layers, not extensible regions; thirteen variants need no artificial Slots.', slots),
    ('registry/contracts.md','characters_001','CHARACTERS-001 registered in specs', 'DELEGATED_FOR_BUILD; documentary and technical QA PASS; human audit PENDING. Two sets and thirteen frames; shadow JSON governed by contract §10 and fixed identity exception.', main),
    ('registry/decisions.md','dec_characters_ecosistema_integration_001','DEC-CHARACTERS-ECOSISTEMA-INTEGRATION-001', 'Explicit user direction nominates Ecosistema AI885:16275. Page Characters, BENI Standby/NAVI Analysis naming and numbered Frame are delegated derivations. Reuse three fixed identity tokens and add only original NAVI shadow; no product semantics or human approval invented.', main),
    ('registry/environment.md','characters_capabilities','Characters Figma and Graphify capabilities', 'Figma MCP READY with read-only source and verified destination. Code limit 50000 characters and output limit 20480 bytes required 4/4/5 build batches. Graph sync authorized locally; CURRENT gated on run evidence. Agent measured cost UNAVAILABLE, not zero.', graphgate),
    ('registry/implementations.md','imp_characters_figma_001','IMP-CHARACTERS-FIGMA-001', 'Technical VALIDATED: Characters820:7, BENI822:6 six variants, NAVI822:7 seven. Forty-seven bindings, thirteen transitions, three variables reused and one shadow added. Library UNPUBLISHED, human audit PENDING; Conversation/Chat intact.', tech),
    ('registry/qa.md','qa_characters_001','QA-CHARACTERS-001', 'Documentary and technical QA PASS; 64 round-trip paths, thirteen frames, 47 bindings, four themes and two scale checks. Initial text/float failures are retained and explained; not perceptual or WCAG certification.', tech),
    ('registry/sources.md','src_ecosistema_characters_001','SRC-ECOSISTEMA-CHARACTERS-001', 'Read-only Ecosistema AI885:16275 source covers 93 nodes, beniStandBy209:6943 and messageAnalisisNavi269:5947, snapshots/wrappers and synchronized MD/YAML. Source contains zero tokens.', source_nodes[0]),
    ('specs/MIGRATION-AUDIT.md','characters_perceptual_audit','Characters artistic and perceptual audit exception', 'Identity preserved with artistic ratios 5.381:1, 2.028:1* and 1.278:1*. Thirteen reactions pass structurally; perceptual audit PENDING, no blocking decision. Reduced motion/backend remain out of scope, not new tasks.', perceptual),
    ('specs/MIGRATION-TRACEABILITY-STATUS.md','characters_traceability','Characters integration traceability PASS technical', 'Contract in specs, page820:7, two sets with 6+7 frames, thirteen transitions and 47 bindings. One new identity variable; inventory intact. Human audit PENDING and library UNPUBLISHED.', main),
]
registry_ids = {}
for rel, entity, label, rationale, target in registry_new:
    new_id = node(rel, entity, label, 'concept', rationale)
    registry_ids[rel] = new_id
    edge(new_id, target, rel)
    root_id = stem(rel) + '_artifact_md'
    if any(n['id']==root_id for n in nodes):
        edge(root_id, new_id, rel)
edge(registry_ids['registry/sources.md'], source_nodes[1], 'registry/sources.md')
edge(registry_ids['registry/decisions.md'], 'registry_dec_character_identity_001_character_decision', 'registry/decisions.md')
edge(registry_ids['registry/decisions.md'], 'registry_dec_external_components_delegation_001_external_decision', 'registry/decisions.md')
edge(registry_ids['registry/contracts.md'], shadow, 'registry/contracts.md')
edge(registry_ids['registry/qa.md'], docqa, 'registry/qa.md')
edge(registry_ids['specs/MIGRATION-AUDIT.md'], contrast, 'specs/MIGRATION-AUDIT.md')

hyperedges = [dict(id='specs_characters_contract_v0_1_0_art_identity_and_prototype_preservation',
    label='Characters preserves vector art, fixed identity and local prototype cycles',
    nodes=[main,preservation,identity,cycles], relation='form', confidence='EXTRACTED', confidence_score=1.0, source_file=REL[contract])]

assert len({n['id'] for n in nodes}) == len(nodes), 'Duplicate node identifiers'
assert all(re.fullmatch('[a-z0-9_]+', n['id']) for n in nodes)
assert all(n['file_type'] in {'code','document','paper','image','rationale','concept'} for n in nodes)
assert all(n['source_file'] in FILES for n in nodes)
assert all(e['source_file'] in FILES and e['confidence_score'] in {1.0,.95,.85,.75,.65,.55} for e in edges)
assert set(FILES) == {n['source_file'] for n in nodes}, 'Incomplete source coverage'
payload = dict(nodes=nodes, edges=edges, hyperedges=hyperedges, input_tokens=0, output_tokens=0)
content = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
output = RUN / 'chunk-00.json'
assert not output.exists(), 'Do not replace a prior fragment silently'
patch = '*** Begin Patch\n*** Add File: ' + str(output) + '\n' + ''.join('+'+line+'\n' for line in content.splitlines()) + '*** End Patch\n'
subprocess.run(['apply_patch'], input=patch, text=True, check=True, capture_output=True)
assert json.loads(output.read_text()) == payload
print(json.dumps(dict(path=str(output), nodes=len(nodes), edges=len(edges), hyperedges=len(hyperedges),
    historical_nodes=historical_nodes, historical_edges=historical_edges,
    new_nodes=len(nodes)-historical_nodes,new_edges=len(edges)-historical_edges,
    historical_body_hashes_verified=verified, source_files=len(FILES), source_coverage='18/18',
    json_valid=True, source_files_modified=False, sha256=hashlib.sha256(output.read_bytes()).hexdigest()), ensure_ascii=False))
