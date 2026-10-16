---
contract_schema: sdd-project/0.2
contract_id: NAVIGATION-PAGINATION-001
name: Pagination
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Navigation
sources: [SRC-FIGMA-NAVIGATION-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-VISUAL-FIDELITY-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/navigation-pagination.source.component-contract.yaml, drafts/foundations/ai-design-system.navigation-pagination-border.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-NAVIGATION-PAGINATION-BORDER-001]
user_audit: PENDING
---

# Navigation · Pagination 0.1.0

## 1. Purpose

Control visual de paginación con página actual, navegación anterior/siguiente y cantidad por página; la lógica de datos queda fuera del Figma.

## 2. Contract

Construir en la página `Navigation` un set público `Pagination` de cinco variantes, fiel a la [fuente](../drafts/contracts/navigation-pagination.source.component-contract.md) y su [YAML](../drafts/contracts/navigation-pagination.source.component-contract.yaml). El JSON aprobado gobierna nombres, valores, modos, aliases, scopes y descripciones de variables.

## 3. Anatomy

Cada variante: frame Content con control anterior, cuatro celdas `1 · … · 2 · 3`, control siguiente y selector `20 por pag` con CaretDown. Conservar los controles primero/último ocultos por defecto como instancias Caret dobles, no como vectores desprendidos.

## 4. Properties

| Propiedad destino | Tipo | Default | Procedencia |
|---|---|---|---|
| State | VARIANT | Default | cinco estados fuente |
| Page 1 | TEXT | `1` | mejora de editabilidad |
| Page 2 | TEXT | `2` | mejora de editabilidad |
| Page 3 | TEXT | `3` | mejora de editabilidad |
| Items per page | TEXT | `20 por pag` | mejora de editabilidad; placeholder fuente |
| Show first control | BOOLEAN | false | frame oculto fuente |
| Show last control | BOOLEAN | false | frame oculto fuente |

El texto `...` representa elipsis visual y no se convierte en regla de cómputo ni propiedad de producto.

## 5. Variants

Cinco variantes exactas: `State=Default`, `State=Active`, `State=Hover`, `State=Focus`, `State=Disabled`. No inventar ejes Size o Page Count.

## 6. Sizes

Variante 354×66 px con placeholders, Content 306×26; padding 16 top, 24 laterales y bottom. Gap de Content 12; gaps internos 4; botones y celdas de 26×26; selector 102×26; radio 4. Cuando los TEXT editables cambien, permitir hug de contenido sin pretender una regla responsive no observada.

## 7. States

| State | Página 1 | Resto relevante |
|---|---|---|
| Default | fondo default, borde subtle, texto primary | anterior visualmente atenuado, siguiente normal |
| Active | fondo `surface/brand`, borde brand, texto brand | resto como Default |
| Hover | fondo subtle | resto como Default |
| Focus | fondo default, borde focus ring 2 px | resto como Default |
| Disabled | fondo subtle, borde default, texto disabled | páginas 2/3, elipsis y siguiente atenuados; selector conserva apariencia fuente |

Disabled es una variante visual, no implementación de bloqueo funcional.

## 8. Behavior

Cero reacciones. El rango de páginas, anterior/siguiente, primer/último, cambio de cantidad y datos requieren contrato de comportamiento posterior.

## 9. Accessibility

No declarar nombres programáticos, página actual, tab order, foco real ni conformidad WCAG desde la biblioteca Figma.

## 10. Design tokens

| Consumidor | Roles y scope correctos |
|---|---|
| Fills de frames | `color/background/default`, `color/background/subtle`, `color/surface/brand` · `FRAME_FILL` |
| Bordes | `color/border/default`, `color/border/pagination/subtle`, `color/border/brand`, `color/focus/ring` · `STROKE_COLOR` |
| Textos | `color/text/primary`, `color/text/brand`, `color/text/disabled` · `TEXT_FILL` |
| Vectores Caret | `color/icon/primary`, `color/icon/disabled`, `color/icon/brand` · `SHAPE_FILL` |
| Geometría | `spacing/none|xs|sm|md|lg|xl`, `radius/sm`, `stroke/xs|md` (Focus = 2 px) |
| Tipografía | `font/family/base`, `font/weight/regular|semibold`, `font/size/sm`; line-height 160 % y tracking −2 % son literales fuente sin token idéntico |

El borde sutil de Pagination requiere un solo rol nuevo: en Servicios, el `color/border/subtle` compartido del destino resuelve `#FFD8C8` y la fuente `#FFBBB0`; el nuevo rol usa la primitiva aprobada `color/red/200`. Los otros tres modos conservan los aliases existentes. Verificar JSON, Figma y consumidores sin modificar el token compartido.

## 11. Content rules

Los números, elipsis y `20 por pag` son placeholders. No afirmar que los textos cambian automáticamente con datos ni que la elipsis calcula un rango.

## 12. Composition rules

Reutilizar las variantes Phosphor Outline/Light de CaretLeft y CaretRight por sus keys fuente. Las keys de CaretDoubleLeft/Right/Down son locales al archivo anterior y no importables; usar las variantes publicadas Phosphor del mismo nombre/peso, con geometría comparable verificada, registrando las keys distintas en el estado de implementación. Mantener las cinco instancias por variante.

## 13. Responsive behavior

No hay breakpoint ni overflow documentado. La anchura 354 es muestra con texto por defecto; no prescribir adaptación web.

## 14. Edge cases

Los controles dobles ocultos pueden mostrarse mediante booleanas de destino sin alterar la configuración por defecto. Cambio de conteo, disabled de selector o título largo necesita definición posterior.

## 15. Forbidden combinations

No crear porcentajes/rangos de páginas ni estados combinatorios fuera de las cinco variantes. No sustituir iconos por líneas genéricas o romper el binding semántico.

## 16. Design ↔ Code mapping

Las propiedades de texto Figma son etiquetas visuales, no estado de datos. El frontend deberá definir `currentPage`, `totalPages`, `pageSize`, callbacks y accesibilidad en contrato separado.

## 17. Acceptance criteria

`AC-NAV-PG-001`: set único `Pagination`, cinco variantes y siete propiedades. `AC-NAV-PG-002`: anatomía, tamaño, controles dobles ocultos y 25 instancias Caret sin detach. `AC-NAV-PG-003`: todos los paints visibles y ocultos usan categoría/scope correctos; el rol de borde nuevo coincide con JSON y RGB fuente en cuatro modos, geometría y tipografía ligadas donde hay token. `AC-NAV-PG-004`: capturas fuente/destino concordantes, cambios por estado exactos, cero reacciones. `AC-NAV-PG-005`: documentar keys sustituidas, IDs, QA, Figma `UNPUBLISHED` y auditoría humana `PENDING`.

## 18. Examples

Primera página `1`, otras `2` y `3`, elipsis y `20 por pag` son demo; no datos de producto.

## 19. Source of truth

Este MD gobierna composición y estados; el [JSON aprobado](../sources/inventories/tokens.inventory.json) y la [extensión de borde](../drafts/foundations/ai-design-system.navigation-pagination-border.v0.1.0.json) gobiernan variables. El [contrato transversal](MIGRATION-TOKEN-TRACEABILITY.contract.md) gobierna el QA de tokens.

## 20. Change management

Solo las propiedades TEXT y booleanas descritas son mejoras de edición. Cambios de color, rango, interacción o variantes requieren enmienda con evidencia.

## 21. Changelog

- 0.1.0 delegado: cinco estados, token de borde específico, QA documental y construcción Figma técnicamente validados; auditoría humana pendiente.
