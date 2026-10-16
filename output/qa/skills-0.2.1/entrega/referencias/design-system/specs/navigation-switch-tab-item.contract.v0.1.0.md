---
contract_schema: sdd-project/0.2
contract_id: NAVIGATION-SWITCH-TAB-ITEM-001
name: Switch Tab Item
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Navigation
sources: [SRC-FIGMA-NAVIGATION-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-VISUAL-FIDELITY-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/navigation-switch-tab-item.source.component-contract.yaml, drafts/foundations/ai-design-system.navigation-tab-colors.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-NAVIGATION-TAB-COLORS-001, DOT-001]
user_audit: PENDING
---

# Navigation · Switch Tab Item 0.1.0

## 1. Purpose

Elemento de navegación visual entre secciones de un mismo contexto. La nota fuente describe ese propósito; selección funcional y navegación real quedan fuera del alcance Figma.

## 2. Contract

Construir en la página semántica `Navigation` de AI Design System un set público `Switch Tab Item`. Esta es la primera subfamilia de esa página; `Tab`, `Switch Tab` compuesto y `Pagination` tendrán contratos y QA propios, sin presentar la página como migración completa. La [evidencia de fuente](../drafts/contracts/navigation-switch-tab-item.source.component-contract.md) y su [YAML](../drafts/contracts/navigation-switch-tab-item.source.component-contract.yaml) no gobiernan los IDs de destino.

## 3. Anatomy

Cada variante: icono izquierdo opcional oculto por defecto, texto, Dot numérico visible y icono derecho visible. Reutilizar instancia local Dot `Type=Count, Size=Medium`; AddressBook permanece instancia Phosphor intercambiable, no vector desprendido. No duplicar Dot ni incrustar su contrato completo.

## 4. Properties

| Propiedad destino | Tipo | Default | Procedencia |
|---|---|---|---|
| State | VARIANT | Active | fuente Active/Default/Disabled |
| Label | TEXT | `Tab title` | mejora de edición; fuente tenía texto literal |
| Show left icon | BOOLEAN | false | fuente |
| Show badge | BOOLEAN | true | `Show Badge` fuente |
| Show right icon | BOOLEAN | true | fuente |
| Left icon | INSTANCE_SWAP | AddressBook | fuente, misma key |
| Right icon | INSTANCE_SWAP | AddressBook | fuente, misma key |

Conectar propiedades a todas las variantes. La mejora TEXT no introduce estados ni comportamiento.

## 5. Variants

Tres variantes exactas: `State=Active`, `State=Default`, `State=Disabled`. No añadir Hover/Focus/Press por analogía. Default del set: Active como en fuente.

## 6. Sizes

Altura 38 px; Active ancho observado 120, Default/Disabled 116 con placeholder. Iconos 14, Dot 12, gap 8, padding vertical 8 y horizontal 12, radio 8. La anchura puede abrazar contenido editable; no fijar una regla responsive a partir del ejemplo.

## 7. States

| Estado | Fondo | Texto | Iconos |
|---|---|---|---|
| Active | `color/background/navigation-tab-active` | `color/text/on-brand` | `color/icon/on-brand` |
| Default | transparente | `color/text/primary` | `color/icon/primary` |
| Disabled | transparente | `color/text/disabled` | `color/icon/disabled` |

El Dot anidado conserva sus propios roles rojo/600 y blanco en todos los estados. Disabled es estado visual, no prueba de bloqueo funcional.

## 8. Behavior

No añadir reacciones; la fuente tiene cero. Exclusividad, click, teclado y navegación requieren contrato de comportamiento posterior.

## 9. Accessibility

No declarar rol `tab`, foco programático, nombre accesible ni conformidad WCAG desde el Figma. La instancia real necesitará esa especificación fuera de este contrato.

## 10. Design tokens

| Consumidor | Token local y scope | Primitiva/observación |
|---|---|---|
| Frame Active fill | `color/background/navigation-tab-active`, `FRAME_FILL` | morado/400 o azul/400 por modo, JSON de extensión |
| Texto | `color/text/on-brand`, `color/text/primary`, `color/text/disabled`, `TEXT_FILL` | blanco, neutral/900, neutral/400 |
| Vectores AddressBook | `color/icon/on-brand`, `color/icon/primary`, `color/icon/disabled`, `SHAPE_FILL` | blanco, neutral/900, neutral/400 |
| Tipografía | `font/family/base`, `font/weight/regular|bold`, `font/size/sm` | Manrope 14; interlineado 22.4 y tracking −0.28 se conservan como valores fuente sin alias inventado |
| Gap/radio | `spacing/sm`, `radius/md` | 8 px; padding 8/12 usa `spacing/sm|md` si su binding de padding es admitido por Figma, de lo contrario se registra literal |
| Dot | set local `Dot`, `Type=Count, Size=Medium` | bindings internos de Dot, sin overrides cromáticos |

El JSON aprobado y la extensión gobiernan aliases, valores, tipos, modos y descriptions. Se comparan IDs reales de Figma tras la creación; no se equiparan a IDs de fuente por valor.

## 11. Content rules

`Tab title` y `1` son ejemplos. La instancia de producto debe reemplazar la etiqueta y definir el conteo. La visibilidad del badge se controla sin eliminar su instancia.

## 12. Composition rules

Orden izquierda–label–Dot–derecha en auto layout horizontal. Mantener instancias reutilizables y propiedades de visibilidad. La composición `Switch Tab` de cuatro items se construirá después, contra su contrato propio.

## 13. Responsive behavior

No hay breakpoints observados. Mantener altura 38 y permitir ancho variable por texto; no inferir scroll ni overflow.

## 14. Edge cases

Ocultar ambos iconos o el badge conserva espaciado automático. El ejemplo de icono izquierdo oculto es el estado por defecto, no ausencia de la propiedad. Texto largo no tiene regla fuente de truncamiento: no imponerla sin contrato.

## 15. Forbidden combinations

Solo tres estados publicados. No simular Active+Disabled ni añadir Hover/Focus sin evidencia o enmienda.

## 16. Design ↔ Code mapping

State y propiedades Figma son API visual; futura implementación web debe definir valores, activación, disabled, teclado, aria y sincronización del grupo. No se genera código aquí.

## 17. Acceptance criteria

`AC-NAV-SW-001`: página `Navigation` única y set `Switch Tab Item` de tres variantes, nombres exactos. `AC-NAV-SW-002`: anatomía, dimensiones y propiedades conectadas. `AC-NAV-SW-003`: Dot local y AddressBook como instancias, sin detach. `AC-NAV-SW-004`: paints/typography con categorías y scopes correctos; variable nueva coincide campo a campo con JSON y aliases en cuatro modos. `AC-NAV-SW-005`: comparación de captura fuente/destino, cero reacciones, sin afirmar accesibilidad web. `AC-NAV-SW-006`: registro de IDs, QA y auditoría humana `PENDING`; biblioteca `UNPUBLISHED`.

## 18. Examples

La fuente muestra Active morado, Default blanco/transparente y Disabled claro, todos con badge `1`; son ejemplos de apariencia, no datos de producto.

## 19. Source of truth

Este MD gobierna reglas del componente; inventario JSON aprobado más [extensión Navigation](../drafts/foundations/ai-design-system.navigation-tab-colors.v0.1.0.json) gobiernan variables. El [contrato transversal](MIGRATION-TOKEN-TRACEABILITY.contract.md) gobierna la cadena de QA.

## 20. Change management

Una propiedad TEXT nueva mejora edición sin cambiar apariencia. El rol nuevo de fondo corrige el scope frente al rol interactivo genérico fuente, conservando aliases cromáticos. Cualquier variante o color adicional exige enmienda y readback.

## 21. Changelog

- 0.1.0 delegado: primera subfamilia de Navigation, con QA documental e implementación técnica superados; auditoría humana pendiente.
