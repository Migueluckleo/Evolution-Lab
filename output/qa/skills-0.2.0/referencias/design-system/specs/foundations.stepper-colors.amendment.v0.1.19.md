---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-STEPPER-COLORS-001
name: Stepper semantic colors
type: foundations-amendment
status: SUPERSEDED
version: 0.1.19
last_updated: 2026-09-24
review_targets: [figma]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.stepper-colors.v0.1.0.json]
user_audit: PENDING
---

# Enmienda cromática de Stepper

**Histórica:** [Foundations 0.1.20](foundations.stepper-brand.amendment.v0.1.20.md) y el JSON 0.1.1 sustituyen íntegramente estos aliases fijos por el mapeo vigente por tema.

Esta extensión añade ocho roles semánticos y cero primitivas a AI Design System. El [JSON canónico](../drafts/foundations/ai-design-system.stepper-colors.v0.1.0.json) gobierna nombre, descripción, ID local, scope y alias de cada rol en cuatro modos. Los RGB de emerald/600, blue/400, neutral/300, neutral/500 y neutral/400 ya existen y coinciden exactamente con la fuente. El icono consume `color/icon/on-brand` o `color/icon/secondary`, existentes y con scope de forma.

Los fondos de indicador usan `FRAME_FILL`, los rectángulos conectores `SHAPE_FILL` y los tres niveles de texto `TEXT_FILL`. Ningún consumidor debe vincularse directamente a la primitiva. La coincidencia visual no autoriza intercambiar roles semánticos ni modificar el inventario de primitivas aprobado. La implementación y la auditoría humana se registran por separado; esta enmienda no publica la biblioteca.
