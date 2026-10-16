#!/usr/bin/env python3
"""Review final v0.1.2 style descriptions and all79 unchanged recipes/bindings.

Uses the existing readback comparison and variable-resolution functions. It
does not edit historical QA, reinterpret consumer style IDs or write to Figma.
"""
import argparse
import json
from pathlib import Path
import sys

import typography_qa as qa
import typography_consumer_foundation_qa as foundation

ROOT = Path(__file__).resolve().parents[2]
CATALOG = 'specs/tokens/ai-design-system.typography.v0.1.2.json'
OLD_CATALOG = 'specs/tokens/ai-design-system.typography.v0.1.1.json'
SCRIPT = 'implementations/figma/typography_style_readback_v012_qa.py'


def run(args):
    review = qa.Review(ROOT)
    review.version = '0.1.2'
    for source in (SCRIPT, qa.SCRIPT, foundation.SCRIPT):
        review.read_bytes(source)
    values = [review.load(p) for p in (CATALOG, OLD_CATALOG, qa.CURRENT_STYLES_STATE,
              args.readback, foundation.VARIABLES, foundation.INVENTORY, foundation.AVATAR)]
    proofs = []
    if all(value is not None for value in values):
        catalog, old, state, readback, variables, inventory, avatar = values
        styles = {s['id']: s for s in catalog['styles']}
        old_styles = {s['id']: s for s in old['styles']}
        style_map = state['styleMap']
        records = readback if isinstance(readback, list) else readback['styles']
        actual = {s['id']: s for s in records}
        if (catalog.get('version') != '0.1.2' or len(styles) != len(catalog['styles'])
                or len(styles) != 79 or set(styles) != set(old_styles)
                or set(styles) != set(style_map) or len(set(style_map.values())) != 79 or not all(style_map.values())
                or len(actual) != len(records) or set(actual) != set(style_map.values())):
            review.issue('STYLE_MAP_COVERAGE', 'Require79 unique canonical and real IDs with exact historical identity')
        if state.get('errors'):
            review.issue('STYLE_STATE_ERRORS', 'Historical identity state contains errors', errors=state['errors'])
        review.validate_derivatives(styles)
        review.validate_formatting_derivatives(styles)
        observed = foundation.VariableUniverse(variables['collections'], variables['variables'])
        canonical = foundation.canonical_universe(inventory, avatar)
        fixed = ('id', 'name', 'category', 'fontFamily', 'fontStyle', 'fontWeight', 'fontSize',
                 'lineHeight', 'letterSpacing', 'textDecoration', 'tokenRefs', 'derivedFormattingFrom')
        for sid, spec in styles.items():
            for field in fixed:
                if spec.get(field) != old_styles.get(sid, {}).get(field):
                    review.issue('UNAUTHORIZED_RECIPE_CHANGE', 'v0.1.2 is documentary; recipe and identity must stay unchanged', styleLogicalId=sid, field=field)
            old_scale = {k: v for k, v in old_styles.get(sid, {}).get('derivedFrom', {}).items() if k != 'reason'}
            new_scale = {k: v for k, v in spec.get('derivedFrom', {}).items() if k != 'reason'}
            if old_scale != new_scale:
                review.issue('UNAUTHORIZED_SCALE_CHANGE', 'Scale values/encoding must remain identical', styleLogicalId=sid)
            record = actual.get(style_map.get(sid))
            if record is None:
                review.issue('STYLE_NOT_READ', 'Mapped real TextStyle absent from current readback', styleLogicalId=sid)
                continue
            review.counts['styles'] += 1
            differences = qa.recipe_errors(record, spec)
            differences += [field for field in ('name', 'description') if record.get(field) != spec[field]]
            if differences:
                review.issue('STYLE_DEFINITION', 'Readback differs from v0.1.2 canonical fields', styleLogicalId=sid, fields=differences)
            if set(record.get('boundVariables', {})) != set(spec['tokenRefs']):
                review.issue('STYLE_BINDING_FIELDS', 'Readback binding fields differ from canonical refs', styleLogicalId=sid)
            proof = {'styleLogicalId': sid, 'styleId': record['id'], 'bindings': {}}
            for field, token in spec['tokenRefs'].items():
                review.counts['bindings'] += 1
                result = foundation.verify_binding(review, sid, spec, record, field, token, observed, canonical)
                if result is not None:
                    proof['bindings'][field] = result
            proofs.append(proof)
        for field, expected in {'styles': 79, 'bindings': 322, 'modeResolutions': 1288}.items():
            if review.counts[field] != expected:
                review.issue('STYLE_QA_COVERAGE', 'Readback coverage differs from complete catalogue', field=field, expected=expected, actual=review.counts[field])
    report = review.report()
    for unmeasured in ('uiIntervalsWithoutStyle', 'uiIntervalsWithForeignStyle', 'nodesWithChangedSegmentation'):
        report['counts'].pop(unmeasured, None)
    report.update(id='QA-TYPOGRAPHY-STYLES-V012-001', scope='79 real TextStyle definitions/descriptions,322bindings and1288four-mode resolutions',
                  componentMigration='NOT_VALIDATED_BY_THIS_REPORT', validatedStyles=proofs)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--readback', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'result': result['result'], 'counts': result['counts'], 'failureCount': result['failureCount'], 'blockedCount': result['blockedCount']}))
    return 0 if result['result'] == 'PASS' else 2


if __name__ == '__main__':
    sys.exit(main())
