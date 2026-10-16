---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-NAVIGATION-TAB-COLORS-001
name: Navigation tab background color
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.13
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.navigation-tab-colors.v0.1.0.json]
decision_refs: [DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001, DEC-MIGRATION-VISUAL-FIDELITY-001]
---

# Foundations · fondo activo de Navigation 0.1.13

La [extensión JSON](../drafts/foundations/ai-design-system.navigation-tab-colors.v0.1.0.json) define un solo rol nuevo `color/background/navigation-tab-active`, `COLOR`, colección `semantic`, scope exclusivo `FRAME_FILL`, aliasado a primitivas aprobadas `color/purple/400` (Contable/Servicios) y `color/blue/400` (Administrativo/Personas). Estos valores replican el grafo observado de `color/interactive/accent/default` de la fuente para el fill de `Tab item` Active; no alteran la variable interactiva existente ni inventan una primitiva. La única `description` del token vive en el JSON.

Antes de construir, verificar colección/modos y ausencia de nombre duplicado. Tras crear, registrar ID real, comparar nombre, tipo, descripción, scope, `codeSyntax`, cuatro aliases y resolución cromática. No usar esta variable en texto, iconos, strokes o efectos. `targetId` se completa en el JSON solamente después del readback. Auditoría humana `PENDING`; biblioteca `UNPUBLISHED`.
