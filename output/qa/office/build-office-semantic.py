"""Host-agent semantic extraction of the prepared office delta, from read sources."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / 'graphify-out/runs/2026-10-16-office'
part = {'nodes': [], 'edges': [], 'hyperedges': [], 'input_tokens': 0, 'output_tokens': 0}
ids = {}

def node(path, entity, label, description, rationale=None, kind='concept', **extra):
    stem = re.sub('[^a-z0-9_]', '_', str(Path(path).with_suffix('')).lower())
    ident = stem + '_' + entity
    value = dict(id=ident, label=label, file_type=kind, source_file=str(ROOT / path),
                 source_location=None, source_url=None, captured_at=None, author=None,
                 contributor=None, description=description, **extra)
    if rationale:
        value['rationale'] = rationale
    part['nodes'].append(value)
    ids[path, entity] = ident
    return ident

def edge(path, source, target, relation='references'):
    part['edges'].append(dict(source=source, target=target, relation=relation,
        confidence='EXTRACTED', confidence_score=1.0, source_file=str(ROOT/path),
        source_location=None, weight=1.0))

def document(path, label, summary, facts):
    root = node(path, 'document', label, summary, kind='document')
    for entity, title, description, reason in facts:
        child = node(path, entity, title, description, reason,
                     kind='rationale' if reason else 'concept')
        edge(path, root, child)
    return root

document('AGENTS.md', 'SDD project governance with Evolution Lab office',
 'Protocol package 0.5.0 governs scope and source authority; office work uses canonical roles and real execution evidence.', [
 ('scope', 'Task-scoped SDD protocol selection', 'P01–P08 and P-SLOTS apply according to the authorized task; reading phases does not authorize executing them.', 'Prevent automatic expansion of authorized work.'),
 ('technical_closure', 'DEC-AI-TECHNICAL-CLOSURE-001', 'Technical documentation and sufficient QA permit closure without routine human approval; user_audit NOT_REQUIRED and human_review_policy OPTIONAL_NON_BLOCKING. Historical PENDING is neither approval nor executed QA.', 'Preserve evidence while avoiding routine blocking human gates.'),
 ('authority', 'Markdown rules and delegated canonical JSON', 'User decisions set scope; active delegated or approved contracts govern rules and JSON governs only delegated fields. Contradictions between approved sources become CONFLICT. Inventories, observed Figma, code and Graphify remain evidence.', 'Avoid two editable definitions of the same requirement.'),
 ('provenance', 'Provenance is distinct from approval', 'EXPLICIT, DERIVED, OBSERVED, INFERRED, UNRESOLVED and CONFLICT do not imply approval. A synthesized contract starts DRAFT; eligible QA and request allow DELEGATED_FOR_BUILD.' ,None),
 ('slots', 'P-SLOTS applicability', 'Each family needs REQUIRED, justified NOT_APPLICABLE or UNRESOLVED. Fixed examples or frames named Slot do not establish implemented slots.', 'Content variability requires verifiable composition rather than a name.'),
 ('migration', 'Delegated legacy migration and canonical specs', 'The scoped legacy migration permits technical construction and promotion to specs after QA without changing DELEGATED_FOR_BUILD to APPROVED. Subsequent amendments stay versioned in specs; historical pending audit remains evidence.', None),
 ('identity', 'BENI/NAVI identity exception', 'DEC-CHARACTER-IDENTITY-001 and Conversation 0.1.1 require original character colors through fixed character-identity direct tokens. Exception is scoped to those characters.', None),
 ('tokens', 'Canonical tokens and actual destination bindings', 'Approved tokens.inventory.json governs names/types/modes/values/aliases/description; actual destination IDs must be read from AI-Design-System tj3WIBEZDGLVs7MJWKCwgf. A single description and preserved aliases are required.', None),
 ('typography', 'Typography styles and bounded native inheritance', 'Active typography 0.1.2, formatting 0.1.1, native inheritance 0.1.2 and consumption amendment require complete per-text/range styles and verified properties/overrides. Empty local ID is insufficient for native exemption; historical consumers are not automatically revalidated.', None),
 ('nearest_primitive', 'Nearest existing primitive supersedes historical exact-color exception', 'DEC-MIGRATION-NEAREST-PRIMITIVE-001 and traceability amendment 0.1.2 use a similar existing primitive via a semantic alias if exact RGB is absent; record visual difference/contrast. Amendment 0.1.1 is historical.', 'Maintain scope-appropriate semantic aliases without default creation of new primitives.'),
 ('graph', 'Continuous incremental Graphify closure', 'Graphify is derived evidence. Relevant changes require complete structural and semantic P05 closure, outputs, coverage/integrity, manifest and queries before CURRENT; failed closure remains STALE/BLOCKED. Same hashes allow reuse.', 'AST alone cannot establish semantic document freshness.'),
 ('web_skills', 'Web implementation and paired consumption skills', 'P07 uses React/TypeScript/Tailwind/Next.js without backend. P08 requires both current versioned skills from the same DS cut; do not edit historical consumption snapshots or auto-promote screen compositions.', None),
 ('office', 'Evolution Lab office directives', 'EVOLUTION-LAB.md defines office; office/config.json is canonical for roles and directives; office/OPERATING-PROTOCOL.md applies to orchestration and optimization. All profiles pursue maintenance, documented construction and token efficiency.', None),
 ('preflight', 'Light office preflight and measured reuse', 'Before building, record lightweight preflight, reuse current evidence and compare benefits without invented metrics or expanded scope.', 'Coordinate authorized work with minimal necessary context and checks.'),
 ('real_activity', 'Named roles are not permanent agents', 'Names identify separate AI roles assigned on demand. Record real requests and responses with rationale/correlation/evidence; the panel is a ledger cut, not fabricated live activity or a scheduled monitor.', 'Make actual execution distinguishable from role definitions and visual presentation.')
])

document('EVOLUTION-LAB.md', 'Evolution Lab operating model',
 'Named AI office with canonical directives, actual conversations, technical QA and simple ledger chat.', [
 ('roles', 'Eva Atlas Bruno Vera Iris', 'Five canonical roles: Eva coordinates, Atlas documents, Bruno builds, Vera verifies and Iris optimizes. Concrete executions are assigned on demand; these names do not start permanent agents.', None),
 ('objectives', 'Three primary objectives', 'Keep documentation and maintenance queryable, construct the documented design system and improve token efficiency within authorized work.', None),
 ('chat', 'Simple office chat of recorded exchanges', 'Chat shows names and ordered requests/responses; filter by agent or text search, with directives and evidence in folded details.', 'Reduce visual complexity while retaining traceability.'),
 ('refresh', 'HTTP refresh versus offline snapshot', 'HTTP mode checks state every three seconds while visible and shows disconnection; file mode retains embedded snapshot. Neither is token streaming nor presence of active agents.', None),
 ('ledger', 'Hash-chained real event ledger', 'Operators record actual tool exchanges; hash chain detects accidental modification but is not a signature or proof that an agent spoke.', 'Avoid treating structural validation as verification of tool execution.'),
 ('qa', 'Technical closure and bounded Figma access', 'Delegated technical QA does not simulate human acceptance. Figma work needs real access and an explicit non-master destination for consumption; existing components must be genuinely available.', None),
 ('remote', 'Remote DS data independent of skill engine', 'GitHub catalog pointer is consulted per encounter; data revisions are independent of engine releases. Document records GitHub workflow and local download/tests of ZIP 0.3.2; external Genspark use remains separate.', None)
])

document('office/OPERATING-PROTOCOL.md', 'Office operating protocol 0.1.2',
 'Canonical operating process for named roles, real messages, proportional QA and honest optimization.', [
 ('preflight', 'Eva preflight and stop conditions', 'Declare objective, scope, deliverable, destinations and acceptance. Reuse context/hashes and deterministic checks. Define iteration and stop limits; proposed budgets are not measured use; unavailable costs remain UNAVAILABLE.', 'Prevent repeated context extraction and uncontrolled iterations.'),
 ('roles', 'Canonical profiles and on-demand runtime assignment', 'Eva coordinates, Atlas documents, Bruno builds, Vera verifies and Iris optimizes; config owns directives. Profile existence does not imply a process is running. Direct named contacts are authorized with Eva visibility; actual relays are recorded.', None),
 ('exchange', 'Real correlated request and response', 'Requests have stable identity, mission/correlation, sender/recipient/runtime, action/rationale/objective, scope/dependencies, deliverable, time/status and evidence. Responses preserve correlation and report real execution/limits; a new request stays separate.', 'Make delegation reconstructible without inventing activity.'),
 ('recording', 'Record after confirmed tool send', 'CLI records after a real confirmed send; it does not dispatch. Never invent chat, include secrets or expose private reasoning.', None),
 ('optimization', 'Measured improvements inside active scope', 'State hypothesis, baseline, cost and criterion across all three objectives. Include coordination/rework in comparisons; unavailable token/time savings remain UNAVAILABLE. Out-of-scope ideas are proposals; stop at goal, limit or material block.', 'Optimization must preserve scope and mandatory controls.'),
 ('qa', 'Impact-based independent verification', 'Vera independently verifies high-impact flow changes; reuse deterministic evidence by matching hashes/config/environment/scope. P05/P06 apply to affected work; technical failure is not waived by optional human review.', None),
 ('evidence_gate', 'PASS/COMPLETED requires local evidence for every kind', 'Every PASS or COMPLETED result needs an existing local evidence file. Existence is structural validation, not proof of content truth. Notes use RECORDED and unexecuted tests use NOT_RUN.', 'Keep evidence gate distinct from semantic or human approval.'),
 ('ledger', 'Append-only hash-chained event corrections', 'Use CLI for events.jsonl and append corrections instead of rewriting history. Evidence is relative local file paths; tool_ref is declarative and not verification by reading the tool.', None),
 ('derived_view', 'Generated index.html and state.json', 'record/render produce office/dist/index.html and state.json from config and ledger. HTTP polls every three seconds when visible with disconnection status; file HTML shows embedded snapshot. No dispatcher, token stream or permanent agents.', 'The UI must represent the same ledger without suggesting live agent presence.'),
 ('continuity', 'Five-field RECORDED continuity note', 'A note records requests/correlations, last verified result, next action or closure, limits, and evidence/hashes. Reuse cited source versions; a continuity note is not PASS.', 'Recover work with minimal context and without creating another state authority.'),
 ('graph', 'P05 closure per coherent batch', 'Graph updates follow coherent source batches; the ledger links canonical records. Completion checks real exchanges, validation and matching view, without claiming later follow-up or active-agent presence.', None)
])

document('office/README.md', 'Office entry points and chat operation',
 'Practical navigation for the five canonical profiles and a chat backed by real recorded events.', [
 ('routes', 'Four routes by need', 'Entry routes cover resuming continuity, consulting a profile, recording an exchange and proposing an improvement. First session reads the protocol; resumption checks relevant source changes.', 'Avoid rereading the entire office for every task.'),
 ('authority', 'Config directives and protocol authority', 'Five roles share three objectives; table is summary only. office/config.json owns directives and OPERATING-PROTOCOL.md owns procedure; roles and actual execution assignments are distinct.', None),
 ('files', 'Ledger, generator and generated view', 'Config, events.jsonl and evolution_office.py produce office/dist/index.html and state.json. Generated files are not independent normative sources.', None),
 ('cli', 'CLI check record render', 'CLI validates, appends recorded events or renders. Request example is illustrative rather than an actual ledger event; CLI does not send messages to agents.', None),
 ('responses', 'Response correlation and evidence semantics', 'A response refers to a pending request with reversed participants and the same objective. Evidence requirements are structural, and claimed states still require real execution evidence.', None),
 ('refresh', 'Three-second HTTP chat refresh', 'Serve locally to poll while visible; opening HTML directly preserves its embedded cut. No agent presence or token streaming is implied.', None),
 ('continuity', 'Resume through actual ledger continuity', 'Resume from recorded requests, last verified result and next action/limits/evidence rather than assuming that a role name carries memory.', 'Reduce context without fabricating continuity.')
])

document('office/dashboard.html', 'Office simple chat template',
 'Source template renders an escaped inert data block into an accessible filtered chat and periodically reads generated state over HTTP.', [
 ('safe_dom', 'Inert data and text-only DOM rendering', 'Template consumes __OFFICE_DATA__ JSON; script uses textContent for user-visible content and encoded relative evidence URLs. No agent dispatch function is exposed.', None),
 ('filters', 'Agent selection and text search', 'Sidebar lists team profiles; chat filters exchanges by selected sender/recipient and textual search. Replies show cited request context; directives and message evidence are collapsed details.', 'Keep the primary flow a readable conversation.'),
 ('details', 'Traceability details', 'Message details retain reason, scope, deliverable, observed status, objective, tool reference, evidence paths, event ID and timestamp.', None),
 ('refresh', 'Visible-tab polling with revision detection', 'On HTTP(S), state.json is fetched without cache every three seconds; hidden documents defer fetch, requests have a four-second timeout, and changed revisions update chat. Errors show a disconnected label.', None),
 ('position', 'Scroll-preserving updates', 'New revisions retain user scroll unless already at the bottom; a new-messages button lets the reader jump. role=log and aria-live=polite accompany responsive layout.', 'Avoid moving the reader unexpectedly during updates.'),
 ('offline', 'File protocol uses embedded snapshot', 'Local file mode renders embedded data without starting HTTP polling; UI is not token streaming or proof of running agents.', None)
])

document('office/reviews/eva.md', 'Eva directive review and integration decisions',
 'Coordinator review records proposals and actual integration decisions; chat simplicity follows the user request.', [
 ('preflight', 'Explicit outcome and acceptance', 'Proposed directives define objective/scope/deliverable/acceptance and stop conditions before assignment; keep a light preflight proportional to work.', 'Avoid unbounded iterations and irrelevant context.'),
 ('delegation', 'Assign roles only when needed', 'The explicit all-profile review is a current mission; it does not create a default requirement to run all five agents on future tasks.', 'Preserve user authorization without permanent coordination overhead.'),
 ('real_records', 'Record actual dispatch and integrate QA', 'Document real requests/responses and integrate affected independent verification with concrete evidence; do not invent activity.', None),
 ('simple_chat', 'Simplify the requested office UI', 'User feedback called for a simple chat; traceability and directives move into details instead of dominating the main view. UI verification is recorded separately.', 'Keep primary reading focused on the conversation.'),
 ('measurement', 'Efficiency savings unavailable', 'No invented token or duration savings are claimed for the proposed directives; measurement remains UNAVAILABLE.', None)
])

document('office/reviews/atlas.md', 'Atlas documentary directive review',
 'Documentary review distinguishes proposals, implemented navigation/continuity improvements and later 0.1.2 chat alignment.', [
 ('authority', 'Preserve canonical rules and historical evidence', 'Proposed Atlas directive distinguishes sources, current authority and historical evidence; reports do not silently replace canonical rules.', None),
 ('routes', 'Four navigation routes instead of zero', 'README now provides four entry routes. Protocol adds one five-field continuity format instead of none; no new state files were introduced.', 'Reduce context needed to resume while preserving source ownership.'),
 ('continuity', 'Continuity with Vera contrast', 'Documentary result is PASS with Vera contrast; continuity cites real events, source versions and limits. A future real continuity exercise is proposed, not claimed as executed.', None),
 ('chat_alignment', '0.1.2 HTTP/offline clarification', 'Appendix aligns documentation to periodic HTTP refresh and offline snapshot. Atlas does not claim browser execution; actual visual QA is separate.', 'Avoid implying live agent presence or token streaming.'),
 ('proposal', 'Three directives submitted for Eva integration', 'Review proposes source authority, entry-by-need/continuity and avoiding duplicated context. Proposal state records its point in history; canonical config owns later adoption.', None),
 ('measurement', 'Token and time results UNAVAILABLE', 'Counts of documentation changes are observable; token/time savings and future pilot results are not measured.', None)
])

document('office/reviews/bruno.md', 'Bruno builder directive proposals',
 'Report-only proposals for building across Figma reconstruction, Figma consumption and web, with scenarios not executed.', [
 ('destinations', 'B1 destination-specific preflight', 'Distinguish P04 reconstruction destination, authorized non-master Figma consumption and independent web/PO work. Confirm destination and scope before implementation.', 'Prevent a consumer screen request from changing the master design system.'),
 ('components', 'B2 existing versus inaccessible components', 'Use genuinely accessible components; unavailable libraries or nodes remain an explicit limit rather than an invented existing component.', None),
 ('evidence', 'B3 evidence before and after implementation', 'Plan evidence before writes, read back results, verify affected dependencies and apply P08 with separate catalog-data and engine release decisions.', 'Close against actual output instead of assuming successful commands prove conformity.'),
 ('limits', 'Proposed scenarios remain NOT_RUN', 'Bruno changed only the review report, no components or configuration. Proposed scenarios are NOT_RUN, costs UNAVAILABLE; report itself does not authorize adoption.', None)
])

document('office/reviews/iris.md', 'Iris optimizer directive proposals',
 'Three proposed efficiency directives reuse Atlas, Bruno and Vera reports without additional delegation or claimed savings.', [
 ('preflight', 'Minimal context with justified delegation and stop', 'Reuse lightweight preflight and current evidence; delegate when outcome justifies coordination, with explicit acceptance and stopping conditions.', 'Reduce repeated context while retaining required work.'),
 ('conversation', 'Brief real chat with traceability details', 'Keep real requests/responses clear and correlated, with reason, scope and evidence in details.', 'Readable interaction should not remove auditability.'),
 ('comparison', 'Compare complete cost at equal scope', 'Include coordination and rework in measured comparisons; unavailable metrics stay UNAVAILABLE. Catalog data updates do not automatically require an engine release.', 'Avoid apparent savings caused by omitted work or uncounted overhead.'),
 ('limits', 'Proposal counts are not measured savings', 'Report records three directives, three reused reports and zero new delegations; comparison experiment is NOT_RUN, savings unavailable, and adoption belongs to canonical integration.', None)
])

document('office/reviews/vera.md', 'Vera verification directive review and office QA',
 'Three directive proposals remain report-scoped while independent office verification records 24 passing tests without skips.', [
 ('qa', '24 office tests PASS without skips', 'Review links tests/office/test_office.py, output/qa/office/tests.txt and independent-review.md. Revalidated evidence gate for all PASS/COMPLETED kinds, failures before/after append, state/HTML, simulated HTTP chat network and concurrent render serialization.', 'Verify observable persistence and chat behavior rather than only implementation details.'),
 ('selection', 'Select tests by affected requirements and dependencies', 'Proposed directive reuses evidence only with matching version/hashes, configuration, relevant environment and scope; widen tests for new changes, failures or concrete uncertainty.', 'Avoid repeating unrelated builds without weakening mandatory controls.'),
 ('regression', 'Bound defect correction and revalidation', 'Record minimal input, expected/observed result and scope; tell responsible role with Eva copy; repeat repaired case and affected dependencies. Invalid template prevents append; post-commit panel failure returns persisted ID and render recovers without duplication.', None),
 ('closure', 'Evidence-led closure with optional human audit', 'Proposed directive distinguishes technical PASS, documentary state and explicit human approval. FAIL/BLOCKED/NOT_RUN/STALE stay visible; historical PENDING alone does not block. Evidence file existence is not semantic approval.', 'Avoid false approvals and unjustified human waiting gates.'),
 ('historical', 'Proposal state versus verified implementation', 'Review itself did not edit config or DS protocols; directive adoption belongs to Eva integration. Actual office corrections/QA are distinct from proposed future experiments and from later canonical directives.', None),
 ('measurement', 'No quantified efficiency improvement', 'Cost savings, token comparison and coordination savings remain UNAVAILABLE. Existing test durations are observations, not controlled comparisons; proposed pilots are not separately executed.', None),
 ('evidence_hashes', 'Read-cut hashes identify evidence', 'Report records hashes of config, protocol, P06, technical-closure decision, office tests/output and prior remote build. Hashes identify a read cut, not approval or measured savings.', None)
])

# Explicit cross-document references and source-defined connections.
for source_path, entity, target_path, target_entity, relation in [
 ('AGENTS.md','office','EVOLUTION-LAB.md','document','references'),
 ('AGENTS.md','office','office/OPERATING-PROTOCOL.md','document','references'),
 ('EVOLUTION-LAB.md','roles','office/OPERATING-PROTOCOL.md','roles','references'),
 ('office/README.md','authority','office/OPERATING-PROTOCOL.md','document','references'),
 ('office/README.md','continuity','office/OPERATING-PROTOCOL.md','continuity','references'),
 ('office/reviews/atlas.md','routes','office/README.md','routes','references'),
 ('office/reviews/atlas.md','continuity','office/OPERATING-PROTOCOL.md','continuity','references'),
 ('office/reviews/atlas.md','chat_alignment','office/dashboard.html','refresh','references'),
 ('office/reviews/vera.md','qa','office/OPERATING-PROTOCOL.md','evidence_gate','references'),
 ('office/reviews/iris.md','document','office/reviews/atlas.md','document','references'),
 ('office/reviews/iris.md','document','office/reviews/bruno.md','document','references'),
 ('office/reviews/iris.md','document','office/reviews/vera.md','document','references'),
 ('office/reviews/eva.md','simple_chat','office/dashboard.html','filters','references')
]:
    edge(source_path, ids[source_path,entity], ids[target_path,target_entity], relation)

expected = set(json.loads((RUN/'chunk-00.files.json').read_text()))
assert expected == {n['source_file'] for n in part['nodes']}
assert len({n['id'] for n in part['nodes']}) == len(part['nodes'])
known = {n['id'] for n in part['nodes']}
assert all(e['source'] in known and e['target'] in known for e in part['edges'])
(RUN/'chunk-00.json').write_text(json.dumps(part,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'semantic_files':len(expected),'nodes':len(part['nodes']),'edges':len(part['edges']),'usage':'UNAVAILABLE; schema zeros are not measured use'}))
