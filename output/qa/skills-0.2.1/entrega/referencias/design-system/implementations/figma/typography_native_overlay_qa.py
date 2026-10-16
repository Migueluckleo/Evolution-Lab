#!/usr/bin/env python3
"""Join the final34-page census and exact103 native proofs under amendment0.1.2.

Historical checker, mapping and FAIL reports are read unchanged. The only
superseded findings are the two direct-ID requirements on a proven native key.
No Figma calls, inferred IDs, epsilon comparisons or blanket exception lists.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import unittest

import typography_qa as qa
import typography_inheritance_qa as inheritance

ROOT = Path(__file__).resolve().parents[2]
BASE = 'qa/implementations/typography/consumption-v0.1.1/'
SCRIPT = 'implementations/figma/typography_native_overlay_qa.py'
CATALOG = 'specs/tokens/ai-design-system.typography.v0.1.2.json'
AMENDMENT = 'specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md'
SELECTION = BASE + 'consumer-final.selection.json'
PROOF = BASE + 'inheritance103.evaluation.json'
STYLE_QA = 'implementations/figma/typography.v0.1.2.styles.qa.json'
STYLE_READBACK = 'implementations/figma/typography.v0.1.2.styles.readback.json'
OVERLAY = BASE + 'consumer-final.native-inheritance.v0.1.2.json'
GLOBAL = BASE + 'consumer-final.global.v0.1.2.json'
HISTORICAL = [BASE + 'consumer-final.v0.1.1.strict.json', BASE + 'consumer-final.v0.1.1.scopes.json']


def need(value, message):
    if not value:
        raise ValueError(message)


def key(row):
    return (row['pageId'], row['nodeId'], row['start'], row['end'])


def unique_rows(rows):
    result = {key(r): r for r in rows}
    need(len(result) == len(rows), 'Duplicate range identity')
    return result


def accepted_historical_finding(finding, proven, style_map):
    """Only the two explicitly superseded requirements, on an exact proven key."""
    if not all(k in finding for k in ('pageId', 'nodeId', 'start', 'end')):
        return False
    row = proven.get(key(finding))
    if row is None or row.get('status') != 'API_CHAIN_AND_RECIPE_PASS':
        return False
    if finding['code'] == 'ASSIGNMENT_APPLICATION_UNRESOLVED':
        return (finding.get('status') == 'BLOCKED'
                and finding.get('applicationStatus') == 'UNRESOLVED_SCALED_LINK')
    if finding['code'] == 'CONSUMER_STYLE_ID':
        return (finding.get('actual') == '' and row['localTextStyleId'] == ''
                and finding.get('styleLogicalId') == row['materializedStyleLogicalId']
                and finding.get('expected') == style_map[row['materializedStyleLogicalId']])
    return False


def verify_report_sources(review, report):
    review.validate_sources([{'path': p, 'sha256': h} for p, h in report['sources'].items()])


def run(root=ROOT, styles_readback=STYLE_READBACK):
    review = qa.Review(root)
    review.version = '0.1.2'
    direct, native_rows, editorial, superseded = [], [], [], []
    proof = {}
    style_map = {}
    page_summaries = []
    try:
        review.read_bytes(SCRIPT)
        review.read_bytes(qa.SCRIPT)
        amendment = review.read_bytes(AMENDMENT).decode()
        need('status: DELEGATED_FOR_BUILD\n' in amendment and 'version: 0.1.2\n' in amendment
             and all('NAT-0'+str(i) in amendment for i in range(1, 7)), 'Native amendment is not the explicit active rule')
        review.editorial_binding_rule = review.read_bytes(qa.CONTRACT) is not None
        catalog = review.load(CATALOG)
        styles = {s['id']: s for s in catalog['styles']}
        need(catalog['version'] == '0.1.2' and catalog['authority']['status'] == 'DELEGATED_FOR_BUILD'
             and catalog['authority']['amendment'] == AMENDMENT and len(styles) == len(catalog['styles']) == 79,
             'Canonical authority or79-style identity differs')
        mapping = review.load(qa.CURRENT_MAPPING)
        review.validate_sources(mapping['sources'])
        state = review.load(qa.CURRENT_STYLES_STATE)
        style_map = state['styleMap']
        need(not state.get('errors') and set(style_map) == set(styles)
             and len(set(style_map.values())) == 79 and all(style_map.values()), 'Real style identity coverage differs')
        style_qa = review.load(STYLE_QA)
        verify_report_sources(review, style_qa)
        need(style_qa['result'] == 'PASS' and style_qa['version'] == '0.1.2'
             and style_qa['counts']['styles'] == 79 and style_qa['counts']['bindings'] == 322
             and style_qa['counts']['modeResolutions'] == 1288 and not style_qa['findings']
             and CATALOG in style_qa['sources'] and styles_readback in style_qa['sources'],
             'Final79-style definitions/descriptions/bindings QA is not complete')
        records = review.load(styles_readback)
        records = records if isinstance(records, list) else records['styles']
        readback = {r['id']: r for r in records}
        bindings = {sid: readback[style_map[sid]]['boundVariables'] for sid in styles}
        for path in HISTORICAL:
            historical = review.load(path)
            need(historical['version'] == '0.1.1', 'Historical report was relabeled')
        need(review.load(HISTORICAL[0])['result'] == 'FAIL', 'Historical strict FAIL must remain intact')

        proof = review.load(PROOF)
        verify_report_sources(review, proof)
        need(proof == inheritance.run(root), 'Saved103 proof differs from fresh independent reconstruction')
        need(proof['status'] == 'PASS' and not proof['findings'] and proof['counts']['ranges'] == 103,
             'Native API chains and all three causal pilots are not complete')
        proven = unique_rows(proof['ranges'])
        expected_native = unique_rows([{**s, 'pageId': n['pageId'], 'nodeId': n['nodeId']}
                                      for n in mapping['nodes'] if n['scope'] == 'UI'
                                      for s in n['segments'] if s.get('instanceScale', 1) != 1])
        need(set(proven) == set(expected_native) and len(proven) == 103, 'Native proof differs from exact mapped103 keys')

        selection = review.load(SELECTION)
        need(selection['schema_version'] == 1 and len(selection['pages']) == 34
             and len({p['path'] for p in selection['pages']}) == 34
             and len({p['pageId'] for p in selection['pages']}) == 34, 'Final selection is not34 distinct pages')
        verify_report_sources(review, selection)
        review.validate_sources([selection['preservedHistorical']])
        before_pages, before = review.census(qa.BEFORE_GLOB, 'before')
        after_pages, after = {}, {}
        for selected in selection['pages']:
            need(not any(c in selected['path'] for c in '*?['), 'Selection path is not literal')
            review.validate_sources([selected])
            pages, nodes = review.census(selected['path'], 'after')
            need(set(pages) == {selected['pageId']} and not set(nodes) & set(after), 'Selected page identity is duplicated or mismatched')
            after_pages.update(pages)
            after.update(nodes)
        review.counts['afterPages'], review.counts['afterNodes'] = len(after_pages), len(after)
        discovery = review.load(qa.DISCOVERY)
        need(set(before_pages) == set(after_pages) == {p['id'] for p in discovery['pages']}
             and len(after_pages) == 34, 'Before/after/discovery page sets differ')
        for pid in sorted(before_pages):
            old, new = before_pages[pid], after_pages[pid]
            need(old['page'] == new['page'], 'Page identity/name changed: '+pid)
            need(sorted(old['components'], key=lambda x: x['id']) == sorted(new['components'], key=lambda x: x['id']),
                 'Component identity/type/name/parent changed: '+pid)
        assignments = {n['nodeId']: n for n in mapping['nodes']}
        need(len(assignments) == len(mapping['nodes']) == 3501 and set(assignments) == set(before) == set(after),
             'Baseline/mapping/current node identities differ')
        for nid in sorted(assignments):
            assigned, old, new = assignments[nid], before[nid], after[nid]
            start_findings = len(review.findings)
            qa.Review.compare_node(review, old, new, assigned, styles, style_map, bindings, readback)
            new_findings = review.findings[start_findings:]
            review.findings[start_findings:] = []
            for finding in new_findings:
                if accepted_historical_finding(finding, proven, style_map):
                    superseded.append(finding)
                else:
                    review.findings.append(finding)
            if assigned['scope'] != 'UI':
                editorial.append({'nodeId': nid, 'pageId': assigned['pageId'], 'ranges': len(assigned['segments']),
                                  'result': 'PRESERVED' if not new_findings else 'FAIL'})
                continue
            for segment in assigned['segments']:
                identity = {'pageId': assigned['pageId'], 'nodeId': nid, 'start': segment['start'], 'end': segment['end']}
                row_key = key(identity)
                current = [r for a, b, r in new['ranges'] if (a, b) == (segment['start'], segment['end'])]
                need(len(current) == 1, 'Current range identity missing: '+str(row_key))
                recipe = current[0]
                if row_key not in proven:
                    direct.append({**identity, 'styleLogicalId': segment['styleLogicalId'],
                                   'textStyleId': recipe['textStyleId'], 'mechanism': 'DIRECT_STYLE_ID'})
                    continue
                native = proven[row_key]
                sid = segment['styleLogicalId']
                derived = styles[sid]['derivedFrom']
                need(native['materializedStyleLogicalId'] == sid and native['nativeScale'] == segment['instanceScale']
                     == derived['scaleFactor'] and native['recipeScale'] == segment['recipeScale'] == 1
                     and native['baseStyleLogicalId'] == derived['baseStyleId']
                     and native['principalTextStyleId'] == style_map[derived['baseStyleId']], 'Native identity/scale/catalog join differs')
                need(recipe['textStyleId'] == native['localTextStyleId'] == ''
                     and recipe['boundVariables'] == native['instanceBoundVariables']
                     and recipe['textStyleOverrides'] == [] and not qa.recipe_errors(recipe, styles[sid]),
                     'Current native consumer differs from proven recipe/bindings/no overrides')
                principal = after[native['principalTextNodeId']]
                need(all(r['textStyleId'] == native['principalTextStyleId']
                         and not qa.recipe_errors(r, styles[native['baseStyleLogicalId']])
                         and {**readback[r['textStyleId']]['boundVariables'], **r['boundVariables']} == native['principalBoundVariables']
                         for a, b, r in principal['ranges']), 'Current principal differs from observed API principal')
                native_rows.append({**native, 'mechanism': 'INHERITED_NATIVE_SCALE',
                                    'instanceScale': segment['instanceScale'], 'status': 'PASS',
                                    'beforePreservationHash': old['preservationHash'], 'afterPreservationHash': new['preservationHash'],
                                    'currentCensusSource': new['source'], 'apiEvidence': PROOF,
                                    'policy': 'NAT-01..NAT-06', 'localTextStyleId': ''})
        expected = {'uiNodes': 3351, 'uiSegments': 3353, 'documentationNodes': 150,
                    'documentationSegments': 150, 'scaledSegments': 103, 'preservationHashesEqual': 3501}
        need(all(review.counts[k] == v for k, v in expected.items()), 'Complete final census counts differ')
        need(len(direct) == 3250 and len(native_rows) == 103 and len(editorial) == 150,
             'Direct/native/editorial coverage differs')
        need(Counter(f['code'] for f in superseded) == Counter({'CONSUMER_STYLE_ID': 103, 'ASSIGNMENT_APPLICATION_UNRESOLVED': 103}),
             'Unexpected count of superseded historical findings')
        need(Counter(key(f) for f in superseded) == Counter({k: 2 for k in proven}), 'Historical exception is not one-to-one with103 keys')
        for pid in sorted(after_pages):
            page_summaries.append({'pageId': pid, 'name': after_pages[pid]['page']['name'],
                                   'directRanges': sum(r['pageId'] == pid for r in direct),
                                   'nativeRanges': sum(r['pageId'] == pid for r in native_rows),
                                   'editorialNodes': sum(r['pageId'] == pid for r in editorial),
                                   'textNodes': sum(n['pageId'] == pid for n in after.values())})
    except (KeyError, ValueError, TypeError, IndexError, OSError) as error:
        review.issue('FINAL_NATIVE_JOIN', str(error))
    report = review.report()
    report['id'] = 'QA-TYPOGRAPHY-CONSUMERS-V012-001'
    report['scope'] = 'Final34-page typography consumer conformity under amendment0.1.2; not whole-design-system validation'
    report['counts'].pop('uiIntervalsWithForeignStyle', None)  # old checker counts empty as foreign; expose honest disjoint categories below
    report['counts'].update(directStyleRanges=len(direct), inheritedNativeScaleRanges=len(native_rows),
                            resolvedRanges=len(direct)+len(native_rows) if report['result'] == 'PASS' else None,
                            unresolvedRanges=0 if report['result'] == 'PASS' else None,
                            nativeLocalEmptyRanges=len(native_rows),
                            nonemptyForeignStyleRanges=sum(bool(r['textStyleId']) and r['textStyleId'] not in style_map.values() for r in direct))
    report['policy'] = {'amendment': AMENDMENT, 'catalog': CATALOG, 'historicalMappingUnchanged': qa.CURRENT_MAPPING,
                        'historicalReportsUnchanged': HISTORICAL, 'nativeProof': PROOF, 'selection': SELECTION,
                        'styleReadbackQa': STYLE_QA, 'stylesReadback': styles_readback, 'noGlobalEmptyIdException': True}
    report['pages'] = page_summaries
    report['ranges'] = direct + [{'pageId': r['pageId'], 'nodeId': r['nodeId'], 'start': r['start'], 'end': r['end'],
                                'styleLogicalId': r['materializedStyleLogicalId'], 'localTextStyleId': '',
                                'principalTextStyleId': r['principalTextStyleId'], 'mechanism': r['mechanism']} for r in native_rows]
    report['editorial'] = editorial
    report['limits'] += ['Table atomic whole-page before/after response was lost to timeout; final text census and intermediate35-page external comparison do not replace it.',
                         'Historical contextual ink-bounds FAIL reports stay unchanged; canonical typography conformity is separate from literal ink identity.',
                         'This34-page selection follows the last consumer write. Later Typography documentation/style-description updates are outside these34 pages and reviewed separately.',
                         '103 native ranges retain empty local TextStyle IDs; only their exact API-chain and causal evidence resolves consumption under NAT-01..06.']
    overlay = {'schema_version': 1, 'version': '0.1.2', 'id': 'QA-TYPOGRAPHY-NATIVE-OVERLAY-V012-001',
               'result': report['result'], 'approval': 'NOT_CONFERRED', 'userAudit': 'PENDING',
               'scope': 'Exact103 existing native-scaled ranges; no extrapolation to new prototypes',
               'counts': {'ranges': len(native_rows), 'localEmptyStyleIds': len(native_rows), 'inheritedNativeScale': len(native_rows),
                          'nativeApiRoutes': proof.get('counts', {}).get('actualMainRoutes', 0)},
               'policy': report['policy'], 'ranges': native_rows, 'supersededHistoricalFindings': superseded,
               'slotBoundaries': proof.get('slotBoundaries', []), 'rawIssues': proof.get('rawIssues', []),
               'pilots': proof.get('pilots', []), 'findings': report['findings'],
               'sources': report['sources'], 'sourcesDigest': report['sourcesDigest'], 'limits': report['limits']}
    return overlay, report


class Tests(unittest.TestCase):
    def setUp(self):
        self.row = {'pageId': 'page', 'nodeId': 'node', 'start': 0, 'end': 3, 'status': 'API_CHAIN_AND_RECIPE_PASS',
                    'materializedStyleLogicalId': 'derived', 'localTextStyleId': ''}
        self.proven = {key(self.row): self.row}
        self.style_map = {'derived': 'real'}
        self.finding = {**{k: self.row[k] for k in ('pageId', 'nodeId', 'start', 'end')}, 'code': 'CONSUMER_STYLE_ID',
                        'styleLogicalId': 'derived', 'actual': '', 'expected': 'real'}

    def test_exact_native_requirement(self):
        self.assertTrue(accepted_historical_finding(self.finding, self.proven, self.style_map))

    def test_outside_range_not_allowed(self):
        self.assertFalse(accepted_historical_finding({**self.finding, 'end': 4}, self.proven, self.style_map))

    def test_nonempty_foreign_id_not_allowed(self):
        self.assertFalse(accepted_historical_finding({**self.finding, 'actual': 'foreign'}, self.proven, self.style_map))

    def test_unrelated_failure_not_allowed(self):
        self.assertFalse(accepted_historical_finding({**self.finding, 'code': 'LOST_SEMANTIC_BINDING'}, self.proven, self.style_map))

    def test_unproven_native_not_allowed(self):
        self.row['status'] = 'PENDING'
        self.assertFalse(accepted_historical_finding(self.finding, self.proven, self.style_map))

    def test_duplicate_key_rejected(self):
        with self.assertRaises(ValueError):
            unique_rows([self.row, self.row])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--styles-readback', default=STYLE_READBACK)
    parser.add_argument('--overlay-output', type=Path, default=ROOT/OVERLAY)
    parser.add_argument('--global-output', type=Path, default=ROOT/GLOBAL)
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
        return 0 if result.wasSuccessful() else 1
    overlay, report = run(styles_readback=args.styles_readback)
    for path, result in ((args.overlay_output, overlay), (args.global_output, report)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'result': report['result'], 'counts': report['counts'], 'findings': report['findings']}, ensure_ascii=False))
    return 0 if report['result'] == 'PASS' else 2


if __name__ == '__main__':
    sys.exit(main())
