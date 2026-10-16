---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-SCROLLBAR-COLORS-001
name: Scrollbar thumb color approximation
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.17
supersedes: FOUNDATIONS-SCROLLBAR-COLORS-001/0.1.16
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json]
decision_refs: [DEC-MIGRATION-NEAREST-PRIMITIVE-001]
---

# Foundations · alias de Scrollbar a primitiva existente

Esta revisión sustituye solo la primitiva y los cuatro aliases de [Foundations 0.1.16](foundations.scrollbar-colors.amendment.v0.1.16.md). El rol semántico `color/background/scrollbar/thumb` mantiene ID, tipo `COLOR` y scope exclusivo `SHAPE_FILL`; su [JSON vigente](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json) define la única descripción y cuatro aliases a `color/neutral/300`, primitiva ya aprobada en el inventario y presente en el archivo Figma. La variable `color/neutral/350` creada en la primera versión queda obsoleta y debe retirarse solo tras comprobar cero referencias directas.

El cambio responde a [DEC-MIGRATION-NEAREST-PRIMITIVE-001](../registry/decisions.md). El color de la fuente `#C3C6D4` sigue registrado como evidencia, pero el color de destino `#E2E8F0` es aproximado; no se declara igualdad cromática. La geometría y anatomía de Scrollbar no se alteran. Readback de aliases, 30 consumidores y captura actualizada obligatorios antes del QA técnico.
