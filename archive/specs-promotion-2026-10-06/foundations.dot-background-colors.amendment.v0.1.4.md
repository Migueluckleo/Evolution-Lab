---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-DOT-BACKGROUND-COLORS-001
name: Dot background semantic roles
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.4
last_updated: 2026-09-23
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json]
---

# Foundations · enmienda de fondos Dot 0.1.4

Esta enmienda añade exclusivamente cuatro roles semánticos de `COLOR` a la colección local `semantic` de AI Design System. El [JSON de extensión](../foundations/ai-design-system.dot-background-colors.v0.1.0.json) gobierna nombres, una descripción por rol, scopes, modos y aliases. El inventario fuente aprobado permanece inmutable.

| Rol nuevo | Uso | Scope | Primitiva en los cuatro modos |
|---|---|---|---|
| `color/background/status-active` | relleno de presencia activa | `FRAME_FILL` | `color/emerald/600` #098300 |
| `color/background/status-busy` | relleno de presencia ocupada | `FRAME_FILL` | `color/red/600` #d40000 |
| `color/background/status-inactive` | relleno de presencia inactiva, no disabled del anfitrión | `FRAME_FILL` | `color/neutral/300` #e2e8f0 |
| `color/background/notification-count` | relleno de conteo | `FRAME_FILL` | `color/red/600` #d40000 |

El origen usa roles de icono para tres fondos y `background/disabled` para una presencia inactiva. Igualdad RGB no es igualdad semántica. Separar Busy y Notification evita que el significado de estado de usuario se transfiera al conteo, aunque ambos aliasen la misma primitiva. No se altera ninguna variable existente ni se crea primitiva.

## Criterios

- Los cuatro nombres no existían antes de crear; se crean solo en `VariableCollectionId:6:2`.
- Cada variable es `COLOR`, tiene scope exclusivo `FRAME_FILL`, una descripción canónica y `codeSyntax={}`.
- Dieciséis aliases por modo apuntan exclusivamente a las primitivas identificadas; nombres y valores se re-leen contra JSON antes de consumir.
- Dot consume estos roles solo en fills de sus componentes raíz; no se aplican a texto, icono ni stroke.
- IDs de Figma, QA, consumidores y auditoría humana quedan registrados; biblioteca no publicada.
