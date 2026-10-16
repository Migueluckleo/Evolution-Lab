---
contract_schema: sdd-project/0.2
contract_id: NAVIGATION-SWITCH-TAB-001
name: Switch Tab
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Navigation
sources: [SRC-FIGMA-NAVIGATION-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-VISUAL-FIDELITY-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/navigation-switch-tab.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001, NAVIGATION-SWITCH-TAB-ITEM-001]
user_audit: PENDING
---

# Navigation · Switch Tab 0.1.0

## 1. Purpose

Composición visual de pestañas para secciones en un mismo contexto. No define navegación funcional ni exclusividad interactiva.

## 2. Contract

Crear en la página semántica `Navigation` un componente público `Switch Tab` independiente del set `Switch Tab Item`. La [evidencia fuente](../drafts/contracts/navigation-switch-tab.source.component-contract.md) y su [YAML](../drafts/contracts/navigation-switch-tab.source.component-contract.yaml) describen el origen; el JSON aprobado gobierna tokens.

## 3. Anatomy

Contenedor con cuatro instancias del set local `Switch Tab Item`, en orden Active, Default, Default, Default. No copiar sus vectores, Dot o textos como capas independientes.

## 4. Properties

La fuente no expone propiedades del padre; el destino tampoco inventa un índice seleccionado. Las propiedades de cada item siguen disponibles en sus instancias anidadas. Si Figma no permite editarlas desde el padre, documentar ese límite sin desprenderlas.

## 5. Variants

Un solo `COMPONENT`, no un set. Los cuatro items representan el ejemplo observado; no generar variantes para cantidades o selecciones no evidenciadas.

## 6. Sizes

488×46 px con los placeholders. Auto layout horizontal hug; 4 px de padding y separación, radio 8. Anchos hijos 120/116/116/116 y alto 38. Contenido editable puede variar el ancho sin cambiar la regla base.

## 7. States

Primera instancia Active; tres siguientes Default. La composición no prueba transición ni impide varias Active en overrides.

## 8. Behavior

Sin reacciones. Cambio de selección, click, teclado y sincronización de contenidos requieren contrato de comportamiento futuro.

## 9. Accessibility

No afirmar `tablist`, `tab`, `aria-selected`, focus management ni conformidad WCAG desde este Figma.

## 10. Design tokens

| Consumidor | Variable local | Justificación |
|---|---|---|
| Fondo del contenedor | `color/background/subtle`, `FRAME_FILL` | alias a `color/neutral/200` en cuatro modos; mismo `#F1F5F9` de origen |
| Separación y padding | `spacing/xs` | 4 px |
| Radio | `radius/md` | 8 px |
| Items anidados | Contrato `NAVIGATION-SWITCH-TAB-ITEM-001` | conserva sus bindings semánticos, incluido fondo Active por modo |

No crear tokens ni primitivas nuevos para esta composición. El rol de fondo existente tiene `FRAME_FILL`; su scope adicional `SHAPE_FILL` no se usa aquí ni se altera globalmente.

## 11. Content rules

`Tab title` y `1` siguen siendo placeholders de demostración. El grupo puede recibir contenido real mediante overrides de las instancias; no se prescribe un número de secciones de producto.

## 12. Composition rules

Usar instancias locales de `Switch Tab Item`, no componentes remotos de la Librería anterior. Mantener los cuatro IDs de hijos reales por separado de los IDs fuente y conservar su orden.

## 13. Responsive behavior

No hay breakpoint, scroll ni overflow observado. No inferir regla responsive desde el ejemplo fijo.

## 14. Edge cases

Varios Active, todos Disabled, badges ocultos o títulos extensos no tienen resolución fuente. Las instancias pueden configurarse visualmente; la exclusividad requiere contrato funcional.

## 15. Forbidden combinations

No presentar cuatro variantes de índice seleccionado o conteo de pestañas como si fueran observadas. No desprender las instancias para facilitar edición.

## 16. Design ↔ Code mapping

El componente Figma es una muestra compositiva; implementación web debe definir arreglo de tabs, valor seleccionado y eventos sin deducirlos de los cuatro placeholders.

## 17. Acceptance criteria

`AC-NAV-ST-001`: componente único en la página `Navigation`, cuatro instancias locales en orden. `AC-NAV-ST-002`: 488×46, auto layout, padding/gap 4, radio 8 y fondo neutral/200 fiel al origen. `AC-NAV-ST-003`: bindings de fondo, gap, padding y radio al JSON aprobado, sin rol text/icon usado como fondo. `AC-NAV-ST-004`: captura fuente/destino concordante, cero reacciones y sin promesas de comportamiento. `AC-NAV-ST-005`: IDs, QA y auditoría humana `PENDING` registrados; Figma `UNPUBLISHED`.

## 18. Examples

Primera pestaña activa y otras tres en default con el mismo título y badge `1`; solo ejemplo visual.

## 19. Source of truth

Este MD gobierna las reglas de composición; el [JSON aprobado](../sources/inventories/tokens.inventory.json) y el [contrato de Switch Tab Item](navigation-switch-tab-item.contract.v0.1.0.md) gobiernan variables y anatomía anidada. La [trazabilidad transversal](MIGRATION-TOKEN-TRACEABILITY.contract.md) define el QA.

## 20. Change management

Un grupo dinámico con cantidad variable o selección exclusiva exige enmienda o contrato de comportamiento. No se añade por analogía durante esta reconstrucción.

## 21. Changelog

- 0.1.0 delegado: composición original de cuatro items; QA documental e implementación técnica completados, auditoría humana pendiente.
