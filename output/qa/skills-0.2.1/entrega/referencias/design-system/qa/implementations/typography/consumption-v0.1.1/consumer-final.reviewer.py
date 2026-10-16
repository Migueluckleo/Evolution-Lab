"""Review an explicit immutable final-census selection with unchanged QA rules."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT/'implementations/figma'))
import typography_qa as qa


class SelectedReview(qa.Review):
    def __init__(self, root, selection):
        super().__init__(root)
        self.selection_path = selection
        self.selection = self.load(selection)
        self.scopes = {name: {'nodes': 0, 'ranges': 0, 'findings': []}
                       for name in ('applicable', 'unresolvedScaled', 'documentation')}

    def census(self, pattern, phase):
        if phase != 'after':
            return super().census(pattern, phase)
        selection = self.selection
        if (selection.get('schema_version') != 1 or len(selection.get('pages', [])) != 34
                or len({r['pageId'] for r in selection['pages']}) != 34
                or len({r['path'] for r in selection['pages']}) != 34):
            raise ValueError('Require exactly34 unique final selected page identities and files')
        pages, nodes = {}, {}
        for row in selection['pages']:
            if any(character in row['path'] for character in '*?['):
                raise ValueError('Selection must use literal paths')
            raw = self.read_bytes(row['path'])
            if raw is None or hashlib.sha256(raw).hexdigest() != row['sha256']:
                raise ValueError('Selected capture hash mismatch: '+row['path'])
            selected_pages, selected_nodes = super().census(row['path'], phase)
            if set(selected_pages) != {row['pageId']} or set(nodes) & set(selected_nodes):
                raise ValueError('Selected identity differs or repeats text nodes')
            pages.update(selected_pages)
            nodes.update(selected_nodes)
        self.validate_sources([{'path': p, 'sha256': h} for p, h in selection['sources'].items()])
        self.validate_sources([selection['preservedHistorical']])
        self.counts['afterPages'] = len(pages)
        self.counts['afterNodes'] = len(nodes)
        return pages, nodes

    def compare_node(self, before, after, assigned, styles, style_map, bindings, readback):
        start = len(self.findings)
        super().compare_node(before, after, assigned, styles, style_map, bindings, readback)
        bucket = ('documentation' if assigned['scope'] != 'UI' else
                  'unresolvedScaled' if any(s.get('instanceScale', 1) != 1 for s in assigned['segments'])
                  else 'applicable')
        section = self.scopes[bucket]
        section['nodes'] += 1
        section['ranges'] += len(assigned['segments'])
        section['findings'].extend(self.findings[start:])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--selection', default='qa/implementations/typography/consumption-v0.1.1/consumer-final.selection.json')
    parser.add_argument('--strict-output', type=Path, required=True)
    parser.add_argument('--scopes-output', type=Path, required=True)
    args = parser.parse_args()
    review = SelectedReview(ROOT, args.selection)
    settings = qa.argument_parser().parse_args([])
    settings.after_glob = 'EXPLICIT_SELECTION_MANIFEST'
    strict = review.run(settings)
    strict['selectionManifest'] = args.selection
    strict['selectionMethod'] = 'Only census file selection overridden; Review.run and all original comparison rules are unchanged'
    strict['runner'] = {'path': str(Path(__file__)), 'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    expected = {'applicable': (3248, 3250), 'unresolvedScaled': (103, 103), 'documentation': (150, 150)}
    for name, section in review.scopes.items():
        section['findingsByCode'] = dict(Counter(f['code'] for f in section['findings']))
        complete = (section['nodes'], section['ranges']) == expected[name]
        section['coverage'] = 'PASS' if complete else 'FAIL'
        section['result'] = ('BLOCKED' if name == 'unresolvedScaled' else
                             'FAIL' if section['findings'] or not complete else 'PASS')
    globals_ = [f for f in strict['findings'] if 'nodeId' not in f]
    supplemental = {'schema_version': 1, 'version': '0.1.1', 'result': 'BLOCKED',
                    'scope': 'Separate per-node results from unchanged strict full-scope QA;103 unresolved assignments remain blocked',
                    'execution': 'LOCAL_SAVED_EVIDENCE_REVIEW', 'figmaWrites': 'NOT_RUN',
                    'selectionManifest': args.selection, 'strictResult': strict['result'],
                    'scopes': review.scopes, 'globalFindings': globals_, 'counts': strict['counts'],
                    'sources': strict['sources'], 'sourcesDigest': strict['sourcesDigest'], 'runner': strict['runner'],
                    'limits': strict['limits'] + ['Does not replace the lost Table atomic whole-page before/after guard.',
                    'Historical contextual ink FAIL reports remain intact; canonical conformity does not claim ink identity.',
                    'Applicable PASS describes node comparisons; global findings must be reviewed separately.']}
    for path, value in ((args.strict_output, strict), (args.scopes_output, supplemental)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'strictResult': strict['result'], 'failureCount': strict['failureCount'],
                      'blockedCount': strict['blockedCount'], 'scopes': {k: {a: b for a, b in v.items() if a != 'findings'} for k, v in review.scopes.items()},
                      'globalFindings': globals_}, ensure_ascii=False))
    return 0 if strict['result'] == 'PASS' else 2


if __name__ == '__main__':
    sys.exit(main())

