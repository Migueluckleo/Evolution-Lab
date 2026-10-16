---
contract_schema: sdd-project/0.2
contract_id: STEPPER-001
name: Stepper Item brand theming
type: component-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.1
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Steppers
sources: [STEPPER-001, DEC-STEPPER-BRAND-THEMING-001]
data_refs: [drafts/foundations/ai-design-system.stepper-colors.v0.1.1.json]
dependencies: [FOUNDATIONS-STEPPER-COLORS-001]
user_audit: PENDING
---

# Stepper Item · enmienda de color por tema

Sustituye solo la exigencia de RGB fuente fijo en **Tokens y tipografía**, la frase de color de **Estados, contenido y comportamiento** y `AC-SI-003` del [contrato 0.1.0](stepper.contract.v0.1.0.md). Geometría, variantes, textos, iconos, propiedades y demás criterios permanecen vigentes. La observación original conserva sus colores históricos, pero la decisión posterior del usuario exige que los acentos cambien con el tema.

Por criterio delegado, `Checked` usa marca fuerte tanto en el fondo circular como en los conectores; `Default` usa marca base en el fondo circular; `Inactive` y el conector Default se mantienen neutros. El mapeo determinista de aliases por modo y scope se delega exclusivamente al [JSON 0.1.1](../drafts/foundations/ai-design-system.stepper-colors.v0.1.1.json) y a [Foundations 0.1.20](foundations.stepper-brand.amendment.v0.1.20.md). Los componentes siguen ligados a roles semánticos de Stepper, nunca directamente a primitivas.

`AC-SI-003` vigente: ocho roles semánticos locales, cero variables/primitivas nuevas, scopes correctos y pinturas vinculadas; los tres roles de acento coinciden con `color/brand/strong` o `color/brand/default` según corresponda **en los cuatro modos**, no solo en la vista por defecto. QA documental y readback de Figma posteriores a esta enmienda son obligatorios antes de volver a declarar `PASS` técnico.
