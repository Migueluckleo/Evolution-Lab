"""Unidades y trazabilidad de recetas; no necesita navegador ni servidor."""
import copy
import json
import unittest

import typography


class TypographyTests(unittest.TestCase):
    def setUp(self):
        self.context = {
            'font/family/base': {'css': '--ds-font-family-base', 'value': '"Manrope Variable", "Manrope", sans-serif', 'source': 'inventory.json'},
            'font/weight/bold': {'css': '--ds-font-weight-bold', 'value': '700', 'source': 'inventory.json'},
            'font/size/5xl': {'css': '--ds-font-size-5xl', 'value': '56px', 'source': 'inventory.json'},
        }
        self.document = {
            'schema_version': 1, 'id': 'FOUNDATIONS-TYPOGRAPHY-001', 'version': '0.1.0', 'font_family': 'Manrope',
            'styles': [{
                'id': 'heading-1-bold', 'name': 'Heading 1/Bold', 'category': 'base',
                'fontFamily': 'Manrope', 'fontStyle': 'Bold', 'fontSize': 56, 'fontWeight': 700,
                'lineHeight': {'unit': 'PERCENT', 'value': 125},
                'letterSpacing': {'unit': 'PERCENT', 'value': -2},
                'description': 'Jerarquía principal.', 'evidence': [],
                'tokenRefs': {'fontFamily': 'font/family/base', 'fontStyle': 'font/weight/bold', 'fontSize': 'font/size/5xl'},
            }],
        }

    def render(self):
        return typography.render(self.document, self.context, 'a' * 64)

    def test_percentages_remain_relative_and_exact(self):
        for value, expected in [(125, '1.25'), (133, '1.33'), (150, '1.5'), (160, '1.6')]:
            self.assertEqual(typography.css_measure({'unit': 'PERCENT', 'value': value}, 'lineHeight'), expected)
        self.assertEqual(typography.css_measure({'unit': 'PERCENT', 'value': -2}, 'letterSpacing'), '-0.02em')
        self.assertEqual(typography.css_measure({'unit': 'PIXELS', 'value': -0.28}, 'letterSpacing'), '-0.28px')
        self.assertEqual(typography.css_measure({'unit': 'PIXELS', 'value': 31.92}, 'lineHeight'), '31.92px')
        self.assertEqual(typography.css_measure({'unit': 'AUTO'}, 'lineHeight'), 'normal')

    def test_units_are_not_guessed(self):
        for measure, kind in [({'value': 160}, 'lineHeight'), ({'unit': 'AUTO'}, 'letterSpacing'), ({'unit': 'PERCENT', 'value': 0}, 'lineHeight'), ({'unit': 'PIXELS', 'value': float('nan')}, 'letterSpacing')]:
            with self.subTest(measure=measure, kind=kind), self.assertRaises(ValueError):
                typography.css_measure(measure, kind)

    def test_generated_outputs_preserve_refs_identity_and_source_hash(self):
        result = self.render()
        css = result['src/generated/typography.css']
        self.assertIn('--ds-type-heading-1-bold-size: var(--ds-font-size-5xl);', css)
        self.assertIn('--ds-type-heading-1-bold-family: var(--ds-font-family-base);', css)
        self.assertIn('--ds-type-heading-1-bold-line-height: 1.25;', css)
        self.assertIn('--ds-type-heading-1-bold-tracking: -0.02em;', css)
        self.assertIn('--ds-type-style-id:heading-1-bold;', css)
        self.assertIn('--ds-type-heading-1-bold-font: var(--ds-type-heading-1-bold-weight) var(--ds-type-heading-1-bold-size)/var(--ds-type-heading-1-bold-line-height) var(--ds-type-heading-1-bold-family);', css)
        manifest = json.loads(result['src/generated/typography.manifest.json'])
        self.assertEqual(manifest['sources'], {typography.SOURCE: 'a' * 64})
        self.assertEqual(manifest['styles']['heading-1-bold']['tokenRefs'], self.document['styles'][0]['tokenRefs'])
        self.assertIn('export type TypographyId = keyof typeof typography;', result['src/generated/typography.ts'])
        self.assertIn('DERIVED_NOT_AUTHORITY', result['docs/TYPOGRAPHY.md'])
        self.assertIn('SHA-256 `' + 'a' * 64 + '`', result['docs/TYPOGRAPHY.md'])
        self.assertIn('Jerarquía principal.', result['docs/TYPOGRAPHY.md'])
        self.assertIn('125 PERCENT', result['docs/TYPOGRAPHY.md'])
        self.assertEqual(result, self.render())

    def test_missing_misclassified_and_mismatched_token_refs_fail(self):
        for field, value in [('fontFamily', 'font/family/primary'), ('fontSize', 'font/weight/bold'), ('fontStyle', 'font/weight/missing')]:
            doc = copy.deepcopy(self.document)
            doc['styles'][0]['tokenRefs'][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                typography.render(doc, self.context, 'a' * 64)
        self.context['font/size/5xl']['value'] = '48px'
        with self.assertRaisesRegex(ValueError, 'no 56px'):
            self.render()

    def test_complement_can_preserve_a_literal_without_fabricated_token(self):
        style = self.document['styles'][0]
        style.update(id='dot-count-small', name='Dot/Count Small', category='complementary', fontSize=4, evidence=['specs/components/dot.contract.v0.1.0.md'])
        del style['tokenRefs']['fontSize']
        style['lineHeight'] = {'unit': 'PERCENT', 'value': 160}
        result = self.render()
        self.assertIn('--ds-type-dot-count-small-size: 4px;', result['src/generated/typography.css'])
        manifest = json.loads(result['src/generated/typography.manifest.json'])
        self.assertNotIn('fontSize', manifest['styles']['dot-count-small']['tokenRefs'])
        self.assertIn('Estilos complementarios · 1', result['docs/TYPOGRAPHY.md'])
        style['evidence'] = []
        with self.assertRaisesRegex(ValueError, 'evidencia'):
            self.render()

    def test_pixel_metrics_use_verified_existing_tokens_only(self):
        self.context.update({
            'font/line-height/xs': {'css': '--ds-font-line-height-xs', 'value': '16px'},
            'font/letter-spacing/tight': {'css': '--ds-font-letter-spacing-tight', 'value': '-0.01px'},
        })
        style = self.document['styles'][0]
        style.update(lineHeight={'unit': 'PIXELS', 'value': 16}, letterSpacing={'unit': 'PIXELS', 'value': -0.01})
        style['tokenRefs'].update(lineHeight='font/line-height/xs', letterSpacing='font/letter-spacing/tight')
        css = self.render()['src/generated/typography.css']
        self.assertIn('--ds-type-heading-1-bold-line-height: var(--ds-font-line-height-xs);', css)
        self.assertIn('--ds-type-heading-1-bold-tracking: var(--ds-font-letter-spacing-tight);', css)
        style['lineHeight'] = {'unit': 'PERCENT', 'value': 160}
        with self.assertRaisesRegex(ValueError, 'solo admite tokenRef para PIXELS'):
            self.render()
        style['lineHeight'] = {'unit': 'PIXELS', 'value': 20}
        with self.assertRaisesRegex(ValueError, 'no 20px'):
            self.render()

    def test_duplicate_ids_and_mismatched_weight_fail(self):
        self.document['styles'].append(copy.deepcopy(self.document['styles'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicado'):
            self.render()
        self.document['styles'].pop()
        self.document['styles'][0]['fontWeight'] = 400
        with self.assertRaisesRegex(ValueError, 'fontStyle'):
            self.render()

    def test_materialized_float32_scales_preserve_exact_css_without_double_scaling(self):
        base = self.document['styles'][0]
        base.update(fontSize=14, lineHeight={'unit': 'PIXELS', 'value': 20}, letterSpacing={'unit': 'PIXELS', 'value': 0})
        del base['tokenRefs']['fontSize']
        dot = copy.deepcopy(base)
        dot.update(id='dot-base', fontSize=4, lineHeight={'unit': 'PERCENT', 'value': 160}, letterSpacing={'unit': 'PERCENT', 'value': -2})
        self.document['styles'].append(dot)
        for sid, parent, ratio, factor, size, height in [
            ('scaled-two-thirds', base, (2, 3), 0.6666666865348816, 9.333333969116211, {'unit': 'PIXELS', 'value': 13.333333969116211}),
            ('scaled-five-sixths', base, (5, 6), 0.8333333134651184, 11.666666030883789, {'unit': 'PIXELS', 'value': 16.66666603088379}),
            ('scaled-four-thirds', dot, (4, 3), 1.3333333730697632, 5.333333492279053, {'unit': 'PERCENT', 'value': 160}),
        ]:
            derived = copy.deepcopy(parent)
            derived.update(id=sid, category='complementary', fontSize=size, lineHeight=height, evidence=['fixture:observed-scaled-use'], derivedFrom={'baseStyleId': parent['id'], 'scaleFactor': factor, 'scaleRatio': {'numerator': ratio[0], 'denominator': ratio[1]}, 'numericEncoding': 'FLOAT32_BASE_TIMES_FLOAT32_SCALE', 'reason': 'Conservar la receta ya escalada.'})
            self.document['styles'].append(derived)
        css = self.render()['src/generated/typography.css']
        for literal in ['9.333333969116211px', '13.333333969116211px', '11.666666030883789px', '16.66666603088379px', '5.333333492279053px']:
            self.assertIn(literal, css)
        self.assertIn('--ds-type-scaled-four-thirds-line-height: 1.6;', css)
        self.assertIn('--ds-type-scaled-four-thirds-tracking: -0.02em;', css)
        self.assertIn('no volver a multiplicarlas', self.render()['docs/TYPOGRAPHY.md'])
        changed = copy.deepcopy(self.document)
        changed['styles'][-1]['fontSize'] *= changed['styles'][-1]['derivedFrom']['scaleFactor']
        with self.assertRaisesRegex(ValueError, 'fontSize.*escala materializada'):
            typography.render(changed, self.context, 'a' * 64)
        changed = copy.deepcopy(self.document)
        changed['styles'][-1]['derivedFrom']['baseStyleId'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'baseStyleId'):
            typography.render(changed, self.context, 'a' * 64)
        changed = copy.deepcopy(self.document)
        changed['styles'][-1]['derivedFrom']['scaleFactor'] = 0
        with self.assertRaisesRegex(ValueError, 'scaleFactor'):
            typography.render(changed, self.context, 'a' * 64)

    def test_alias_resolution_preserves_existing_token_generation(self):
        outputs = {
            'src/generated/tokens.manifest.json': json.dumps({'tokens': [{'collection': 'semantic', 'name': 'font/size/sm', 'css': '--ds-font-size-sm', 'source': 'inventory.json'}]}),
            'src/generated/tokens.css': ':root { --ds-primitive-font-size-14: 14px; --ds-font-size-sm: var(--ds-primitive-font-size-14); } [data-ds-theme="personas"] { --ds-font-size-sm: var(--ds-primitive-font-size-14); }',
        }
        self.assertEqual(typography.token_context(outputs)['font/size/sm']['value'], '14px')
        outputs['src/generated/tokens.css'] += '[data-ds-theme="servicios"] { --ds-font-size-sm: 16px; }'
        with self.assertRaisesRegex(ValueError, 'tema'):
            typography.token_context(outputs)

    def test_formatting_derivation_preserves_metrics_and_emits_underline(self):
        base = self.document['styles'][0]
        style = copy.deepcopy(base)
        style.update(id='heading-1-bold-underline', category='complementary', textDecoration='UNDERLINE',
                     evidence=['fixture:existing-underlined-range'],
                     derivedFormattingFrom={'baseStyleId': base['id'], 'overrides': {'textDecoration': 'UNDERLINE'}, 'reason': 'Preservar subrayado existente.'})
        self.document['styles'].append(style)
        result = self.render()
        self.assertIn('--ds-type-heading-1-bold-underline-decoration: underline;', result['src/generated/typography.css'])
        self.assertIn('text-decoration-line:var(--ds-type-heading-1-bold-underline-decoration)', result['src/generated/typography.css'])
        manifest = json.loads(result['src/generated/typography.manifest.json'])
        self.assertEqual(manifest['styles'][base['id']]['textDecoration'], 'NONE')
        self.assertEqual(manifest['styles'][style['id']]['textDecoration'], 'UNDERLINE')
        for field, value in [('fontSize', 55), ('tokenRefs', {'fontFamily': 'font/family/base'})]:
            changed = copy.deepcopy(self.document)
            changed['styles'][-1][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'formato altera'):
                typography.render(changed, self.context, 'a' * 64)

    def test_unknown_or_mismatched_formatting_derivations_fail(self):
        self.document['styles'][0]['textDecoration'] = 'STRIKETHROUGH'
        with self.assertRaisesRegex(ValueError, 'textDecoration'):
            self.render()
        self.document['styles'][0].update(textDecoration='UNDERLINE', derivedFormattingFrom={'baseStyleId': 'missing', 'overrides': {'textDecoration': 'UNDERLINE'}, 'reason': 'fixture'})
        with self.assertRaisesRegex(ValueError, 'baseStyleId'):
            self.render()


if __name__ == '__main__':
    unittest.main()
