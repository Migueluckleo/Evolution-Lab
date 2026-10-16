#!/usr/bin/env python3
"""Verify a documentary catalogue update without asserting a new browser run."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT/'implementations/web/scripts'))
import typography
import tokens

OLD = 'specs/tokens/ai-design-system.typography.v0.1.1.json'
NEW = 'specs/tokens/ai-design-system.typography.v0.1.2.json'
OUTPUT = Path(__file__).with_name('metadata-review.json')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def recipe(style):
    result = copy.deepcopy(style)
    result.pop('description', None)
    if 'derivedFrom' in result:
        result['derivedFrom'].pop('reason', None)
    return result


def main():
    sources, checks, changes = {}, {}, []
    def read(path):
        raw = (ROOT/path).read_bytes()
        sources[path] = sha(raw)
        return raw
    old, new = (json.loads(read(p)) for p in (OLD, NEW))
    old_styles, new_styles = ({s['id']: s for s in d['styles']} for d in (old, new))
    checks['activeSelector'] = typography.SOURCE == NEW
    checks['exact79IdentitiesAndRecipes'] = (len(old_styles) == len(new_styles) == 79
        and {k: recipe(v) for k, v in old_styles.items()} == {k: recipe(v) for k, v in new_styles.items()})
    for sid, style in new_styles.items():
        previous = old_styles.get(sid, {})
        for field in ('description', 'derivedFrom'):
            if previous.get(field) != style.get(field):
                changes.append({'styleLogicalId': sid, 'field': 'derivedFrom.reason' if field == 'derivedFrom' else field})
    checks['onlyThreeDescriptionsAndReasons'] = (len(changes) == 6
        and {c['styleLogicalId'] for c in changes} == {
            'ui-checkbox-label-scaled-two-thirds', 'ui-checkbox-label-scaled-five-sixths',
            'micro-count-small-scaled-four-thirds'})
    token_outputs = tokens.build()
    context = typography.token_context(token_outputs)
    old_outputs = typography.render(old, context, sources[OLD])
    new_outputs = typography.render(new, context, sources[NEW])
    css_path = 'src/generated/typography.css'
    old_css, new_css = (outputs[css_path].split('\n', 1)[1] for outputs in (old_outputs, new_outputs))
    checks['presentationCssByteIdentical'] = old_css == new_css
    for path, text in new_outputs.items():
        checks['generated:'+path] = read('implementations/web/'+path) == text.encode()
    for path in tokens.SOURCES + ['implementations/web/scripts/typography.py',
                                'implementations/web/scripts/tokens.py',
                                'implementations/web/scripts/test_typography.py',
                                Path(__file__).relative_to(ROOT).as_posix()]:
        read(path)
    test_command = [sys.executable, '-m', 'unittest', 'discover', '-s', 'implementations/web/scripts', '-p', 'test_typography.py']
    tests = subprocess.run(test_command, cwd=ROOT, text=True, capture_output=True)
    checks['existing11UnitTests'] = tests.returncode == 0 and 'Ran 11 tests' in tests.stderr
    report = {'schema_version': 1, 'version': '0.1.2', 'result': 'PASS' if all(checks.values()) else 'FAIL',
              'scope': 'Documentary typography update; exact79 recipes and identical CSS declarations/selectors',
              'counts': {'styles': 79, 'base': 18, 'complementary': 61, 'descriptionChanges': 3, 'reasonChanges': 3},
              'checks': checks, 'styleChanges': changes, 'presentationCssSha256': sha(new_css.encode()),
              'tests': {'command': test_command, 'exitCode': tests.returncode, 'output': tests.stdout+tests.stderr},
              'browser': 'NOT_RERUN_FOR_DOCUMENTARY_CHANGE',
              'limits': ['No new browser, Figma consumer or visual-approval claim.',
                         'CSS comparison excludes only the generated first-line provenance comment; all declarations and selectors compare byte-for-byte.'],
              'sources': dict(sorted(sources.items()))}
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'result': report['result'], 'checks': checks, 'presentationCssSha256': report['presentationCssSha256']}))
    return 0 if report['result'] == 'PASS' else 2


if __name__ == '__main__':
    sys.exit(main())
