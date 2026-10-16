---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-CONTROL-BORDER-SOURCE-COLOR-002
name: Control border source color
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.12
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.control-colors.v0.1.1.json]
decision_refs: [DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-CONTRAST-LIMITATIONS-001, DEC-MIGRATION-TRACEABILITY-001]
---

# Foundations · borde de control, color de origen 0.1.12

Sustituye **solo los cuatro aliases** de `color/border/control` de [Foundations Control Colors 0.1.1](foundations.control-colors.amendment.v0.1.1.md): de neutral/500 a la primitiva aprobada `color/neutral/400` (`#94A3B8`). El [JSON de override 0.1.1](../foundations/ai-design-system.control-colors.v0.1.1.json) gobierna estos aliases; el JSON 0.1.0 sigue como historial para el rol distinto `color/background/control-hover`, que no cambia. No se altera la identidad del token, descripción, tipo `COLOR`, `codeSyntax` ni scope exclusivo `STROKE_COLOR`; no se crea variable ni primitiva.

La fuente de Checkbox Unselected Default/Focus y Radio Button Off Default usa neutral/400. El destino conservó la semántica correcta de borde, pero oscureció esos tres strokes por contraste. El Toggle actual ya no consume `color/border/control`: sus dos bordes Off se reconectaron a `color/border/strong` en 0.1.5. La restauración deja la limitación de contraste del contorno operable (~2.56:1 contra blanco) marcada `*`, sin afirmar conformidad WCAG.

`AC-TOK-CTRL-001`: leer nombre, ID, descripción, scope y cuatro aliases contra JSON 0.1.1. `AC-TOK-CTRL-002`: readback de los tres consumidores Checkbox/Radio y ausencia de consumidores Toggle actuales. `AC-TOK-CTRL-003`: confirmar que `color/background/control-hover` conserva alias, scope y consumidores; no alterar otros colores ni efectos. Auditoría humana pendiente y biblioteca sin publicar.
