---
contract_schema: sdd-project/0.2
contract_id: STEPS-001
name: Steps brand theming
type: component-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.1
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Steps
sources: [STEPS-001, DEC-STEPS-BRAND-THEMING-001]
data_refs: [drafts/foundations/ai-design-system.steps-colors.v0.1.1.json]
dependencies: [FOUNDATIONS-STEPS-COLORS-001]
user_audit: PENDING
---

# Steps · enmienda de marca por tema

Sustituye únicamente la tabla de aliases cromáticos fijos y el criterio `AC-ST-003` del [contrato 0.1.0](steps.contract.v0.1.0.md). Las variantes, medidas, estructura, contenido de demostración, dependencias y anomalía `On Primary` permanecen. La observación de origen no se altera: la instrucción posterior del usuario autoriza que los acentos azules cambien con el tema.

Por criterio delegado, el dot seleccionado `On White` sigue marca base; el dot no seleccionado de `.Dot On Primary` y el dot seleccionado de Gallery legada usan el tono 300 del tema. El dot seleccionado blanco `On Primary`, todos los no seleccionados neutros y el texto neutro quedan intactos. Los bindings siguen en roles `color/shape/steps/...` de scope `SHAPE_FILL`. El [JSON 0.1.1](../drafts/foundations/ai-design-system.steps-colors.v0.1.1.json) gobierna exclusivamente los alias por modo; [Foundations 0.1.21](foundations.steps-brand.amendment.v0.1.21.md) fija la regla.

`AC-ST-003` vigente: siete roles semánticos locales, cero variables/primitivas nuevas, scopes y bindings correctos; los tres acentos siguen la familia cromática de cada uno de los cuatro temas. QA documental y readback posterior de Figma, incluidas las 27 combinaciones, son obligatorios antes de volver a declarar `PASS` técnico.
