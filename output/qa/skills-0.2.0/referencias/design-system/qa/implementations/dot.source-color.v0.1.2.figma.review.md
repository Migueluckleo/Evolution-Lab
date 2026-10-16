# QA Figma · Dot, borde Inactive de origen

**Resultado:** `PASS` técnico para `AC-TOK-DOT-001–003` y `AC-DOT-007–009` · 2026-09-24. `user_audit: PENDING`; set sin publicar.

- Fuente `1133:31549` y destino `155:144`: 15 variantes cada uno. Los 36 paints visibles del destino resuelven los RGB observados en la fuente; cero discrepancias tras la corrección. Se preservaron los IDs y bindings de las tres variantes Inactive y no se alteraron las otras doce.
- El rol local `color/border/status-inactive` `VariableID:157:122` conserva nombre, tipo `COLOR`, descripción y scope exclusivo `STROKE_COLOR`. Sus cuatro aliases ahora apuntan a `color/neutral/100` `VariableID:8:93` (`#FFFFFF`), como el [JSON 0.1.1](../../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.1.json). No se crearon variables ni primitivas.
- Los tres strokes Inactive `155:129`, `155:130` y `155:131` conservan ese binding y resuelven blanco. En los sets Avatar `165:247` e Icon Button `183:311` no se encontraron paints vinculados a ese rol; esa comprobación no equivale a auditoría cromática integral de esas familias.
- La limitación original queda `*`: borde blanco contra blanco 1.00:1; relleno neutral/300 contra blanco ~1.23:1. La enmienda histórica 0.1.1 neutral/500 queda sustituida solo para este color, no borrada. No se certifica accesibilidad ni se publica la biblioteca.
