const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const root = process.cwd();
const run = 'graphify-out/runs/2026-10-08-characters/';
const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const hash = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const verification = read(run + 'verification.json');
const manifest = read(run + 'manifest-check.json');
const graph = read('graphify-out/graph.json');
const before = read(run + 'before/graph.json');
const qa = read('qa/implementations/characters.v0.1.0.audit.json');
const edges = graph.links || graph.edges;
const adjacency = new Map(graph.nodes.map(n => [n.id, new Set()]));
for (const e of edges) { adjacency.get(e.source).add(e.target); adjacency.get(e.target).add(e.source); }
const sourceNode = p => graph.nodes.find(n => n.source_file === p && n.sha256)?.id;
function pathBetween(a, b) {
  const start = sourceNode(a), end = sourceNode(b);
  if (!start || !end) return [];
  const queue = [[start]], seen = new Set([start]);
  for (const p of queue) {
    const n = p[p.length - 1];
    if (n === end) return p;
    for (const next of adjacency.get(n)) if (!seen.has(next)) { seen.add(next); queue.push([...p, next]); }
  }
  return [];
}
const contract = 'specs/characters.contract.v0.1.0.md';
const targets = ['sources/inventories/tokens.inventory.json', 'specs/tokens/ai-design-system.character-identity.v0.1.0.json', 'specs/tokens/ai-design-system.character-shadow.v0.1.0.json', 'registry/DEC-CHARACTER-IDENTITY-001.md', 'qa/implementations/characters.v0.1.0.audit.json', 'implementations/figma/characters.v0.1.0.final.json', 'drafts/contracts/beni-standby.source.component-contract.md', 'drafts/contracts/navi-analysis.source.component-contract.md'];
const paths = targets.map(to => ({from: contract, to, path: pathBetween(contract, to)}));
const shadow = graph.nodes.filter(n => n.source_file === targets[2] && n.label === 'color/characters/navi/shadow' && n.valuesByMode);
const errors = [];
if (verification.status !== 'PASS' || manifest.status !== 'PASS' || qa.status !== 'PASS') errors.push('Prior gate not PASS');
if (paths.some(p => !p.path.length)) errors.push('Characters graph lineage missing');
if (shadow.length !== 1 || shadow[0].valuesByMode.Value.type === 'VARIABLE_ALIAS') errors.push('Shadow identity token missing or incorrectly aliased');
for (const [p, expected] of Object.entries(verification.output_sha256)) if (hash('graphify-out/' + p) !== expected) errors.push('Export drift: ' + p);
const canon = hash('sources/inventories/tokens.inventory.json');
if (canon !== 'cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474') errors.push('Canonical inventory changed');
const files = [contract, ...targets, 'qa/implementations/characters.v0.1.0.review.md', 'registry/SESSION-HANDOFF-2026-10-08-CHARACTERS.md'];
const closure = {date: new Date().toISOString(), status: errors.length ? 'FAILED' : 'CURRENT', errors, graph: {nodes: graph.nodes.length, edges: edges.length, nodeDelta: graph.nodes.length - before.nodes.length, edgeDelta: edges.length - (before.links || before.edges).length, corpusFiles: verification.corpus_files}, scopedPaths: paths, shadowTokenNodes: shadow.length, preservedCanonicalInventorySha256: canon, outputSha256: verification.output_sha256, sourceSha256: Object.fromEntries(files.map(p => [p, hash(p)])), sourceLinkLimitations: verification.source_link_limitations.length, scope: 'Derived graph integrity and current Characters evidence; not human approval, remote publication or perceptual playback certification'};
fs.writeFileSync(run + 'closure.json', JSON.stringify(closure, null, 2));
console.log(JSON.stringify({status: closure.status, errors, graph: closure.graph, paths: paths.length, sourceLinkLimitations: closure.sourceLinkLimitations}));
if (errors.length) process.exitCode = 1;
