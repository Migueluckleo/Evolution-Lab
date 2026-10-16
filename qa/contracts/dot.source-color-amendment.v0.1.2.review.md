# QA documental · Dot Inactive, fidelidad cromática

**Resultado:** `PASS` documental para construcción delegada · 2026-09-24. Auditoría humana `PENDING`.

- La fuente y el destino fueron leídos en Figma: quince variantes por set, 36 paints visibles por set; solo los tres strokes Inactive difieren en RGB (`#FFFFFF` fuente, `#64748B` destino). Los otros 33 coinciden.
- `color/border/status-inactive` existe en destino y conserva identidad `VariableID:157:122`, tipo `COLOR`, scope `STROKE_COLOR` y los tres bindings. La primitiva local `color/neutral/100` `VariableID:8:93` da el blanco de origen; no se inventa primitiva ni token.
- El [JSON de override 0.1.1](../../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.1.json) es válido y versiona únicamente los cuatro aliases. La enmienda Foundations 0.1.6 precede a la enmienda Dot 0.1.2; ambas sustituyen solo el criterio cromático y su afirmación de contraste de 0.1.1.
- La limitación de contraste se mantiene para la auditoría por excepciones; no se promete accesibilidad ni publicación de Figma.
