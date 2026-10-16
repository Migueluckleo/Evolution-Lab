---
amendment_id: AMD-RADIO-BUTTON-SOURCE-COLOR-002
status: DELEGATED_FOR_BUILD
applies_to: RADIO-BUTTON-001
base_contract_version: 0.1.0
base_contract_digest_sha256: f97d72ea3a8abe0c489aaa1a5f7289a4dc900f8c367601f7ccfc1b39651a29f2
version: 0.1.1
supersedes_scope: Selected=False State=Default stroke color and related contrast claim only
foundation_dependency: specs/foundations/foundations.control-border-source-color.amendment.v0.1.12.md
last_updated: 2026-09-24
user_audit: PENDING
---

> Ubicación canónica desde 2026-10-06. Aplicar la [enmienda de refinamiento 0.1.2](components/radio-checkbox.refinement.amendment.v0.1.2.md) y el [QA vigente](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). Las cláusulas históricas sustituidas no son requisitos actuales. DELEGATED_FOR_BUILD; auditoría humana PENDING.


# Radio Button · contorno Off de origen 0.1.1

En `Selected=False, State=Default`, el stroke del anillo `I143:148;142:137` mantiene binding a `color/border/control` `VariableID:123:122`, `STROKE_COLOR`, pero resuelve `#94A3B8` mediante el [override Foundations 0.1.12](foundations/foundations.control-border-source-color.amendment.v0.1.12.md), como la fuente Off Enabled. Las otras siete variantes, los rellenos, la estructura concéntrica del indicador, textos y efectos de foco no cambian. El contorno original sobre blanco (~2.56:1) queda `*`; no se declara conformidad WCAG.

`AC-RAD-008`: readback del anillo Off Default, alias en cuatro modos y comparación cromática con fuente. `AC-RAD-009`: preservar ocho variantes públicas y helper, sin alterar otros paints, propiedades o bindings. Auditoría humana pendiente; set sin publicar.
