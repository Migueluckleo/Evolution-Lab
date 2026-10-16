---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-WARNING-ICON-SOURCE-COLOR-002
name: Warning icon source color
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.10
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.1.json]
decision_refs: [DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-CONTRAST-LIMITATIONS-001, DEC-MIGRATION-TRACEABILITY-001]
---

# Foundations · restauración del icono Warning 0.1.10

Esta enmienda sustituye **solo** los cuatro aliases de `color/feedback/warning/icon` `VariableID:13:48` establecidos por [FOUNDATIONS-WARNING-ICON-CONTRAST-001](../../drafts/contracts/foundations.warning-icon-contrast.amendment.v0.1.8.md). La fuente y el [JSON aprobado](../../sources/inventories/tokens.inventory.json) aliasan ese rol a la primitiva `color/amber/600` (`#C97B00`); el destino se oscureció a amber/700 exclusivamente por contraste. La decisión posterior del usuario exige fidelidad cromática y marcar la limitación `*`, no mantener el oscurecimiento. El [JSON de override 0.1.1](../../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.1.json) gobierna los aliases nuevos; 0.1.0 queda histórico y no es una segunda definición vigente.

No se crea ni elimina variable. Nombre, tipo `COLOR`, descripción canónica, `codeSyntax` y scope estricto `SHAPE_FILL` quedan intactos. La primitiva local amber/600 ya existe como `VariableID:8:108` y coincide campo por campo con la primitiva de origen. La primera consumidora existente es el vector Warning de Inline Notifications; al cambiar la variable compartida su color se restaura automáticamente. Badge Warning la consumirá después de reconectar sus iconos. No se alteran roles de texto, fondo o borde.

| ID | Requisito | Comprobación |
|---|---|---|
| REQ-TOK-WARN-001 | Los cuatro modos de `color/feedback/warning/icon` aliasan `color/amber/600` local, con scope `SHAPE_FILL` y descripción sin cambio. | AC-TOK-WARN-001 |
| REQ-TOK-WARN-002 | Verificar el consumidor Warning de Inline Notifications tras el cambio y documentar el contraste original ~2.96:1 sobre amber/100 como limitación `*`. | AC-TOK-WARN-002 |

`AC-TOK-WARN-001` requiere readback de nombre, tipo, scope, descripción, `codeSyntax` y cuatro aliases reales, comparados con el JSON 0.1.1. `AC-TOK-WARN-002` requiere readback del vector existente con el color original, sin pérdida de binding ni cambio de geometría; registrar ratio y `*` en la auditoría. No se afirma conformidad WCAG ni publicación de biblioteca. [QA documental](../../qa/contracts/foundations.warning-icon-source-color.v0.1.10.review.md) `PASS` antes de Figma.
