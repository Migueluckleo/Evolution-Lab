---
contract_schema: sdd-project/0.2
contract_id: CHECKBOX-001
name: Checkbox
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Checkboxes
sources: [SRC-FIGMA-CHECKBOX-001, SRC-TOKENS-INV-001, SRC-FIGMA-PHOSPHOR-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/checkbox.source.component-contract.yaml, drafts/foundations/ai-design-system.radio-indicator-colors.v0.1.0.json, drafts/foundations/ai-design-system.focus-effects.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-RADIO-INDICATOR-COLORS-001, FOUNDATIONS-FOCUS-EFFECTS-001]
user_audit: PENDING
---

> Aplicar también la [enmienda cromática 0.1.1](checkbox.source-color-amendment.v0.1.1.md).

> Ubicación canónica desde 2026-10-06. Aplicar la [enmienda de refinamiento 0.1.2](components/radio-checkbox.refinement.amendment.v0.1.2.md) y el [QA vigente](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). Las cláusulas históricas sustituidas no son requisitos actuales. DELEGATED_FOR_BUILD; auditoría humana PENDING.


# Checkbox · contrato de reconstrucción 0.1.0

## 1. Purpose

El control representa la selección visual de una o más opciones de un grupo, con estados Selected, Unselected e Indeterminate. La nota fuente pide etiquetas claras. Este contrato Figma no crea comportamiento funcional ni agrupación web.

## 2. Contract

Construir en `AI-Design-System` (`tj3WIBEZDGLVs7MJWKCwgf`) una página funcional exclusiva `Checkboxes` y un set público `Checkbox`. Se conserva la matriz completa de la fuente. El [contrato de fuente](../drafts/contracts/checkbox.source.component-contract.md) y [YAML](../drafts/contracts/checkbox.source.component-contract.yaml) son evidencia; las variables del destino se gobiernan por el JSON aprobado y sus extensiones versionadas, no por IDs del archivo anterior.

## 3. Anatomy

Cada variante contiene etiqueta izquierda oculta, indicador 24×24 y etiqueta derecha oculta. El indicador Selected/Indeterminate tiene rectángulo 18×18 en (3,3), esquinas 4 y un icono Phosphor de 12×12 con vector blanco. Unselected tiene rectángulo 18×18 con contorno de 2 px, sin icono. El helper local observado solo en Unselected/Focus se normaliza a estructura directa; no se replica una dependencia interna de uso único. Los iconos Check y Minus siguen anidados como instancias de Phosphor, sin detachment.

## 4. Properties

| Destino | Tipo | Default | Fuente |
|---|---|---|---|
| Selection | VARIANT | Selected | `type=selected/indeterminate/unselected` |
| State | VARIANT | Default | `state=enabled/hover/focus/disabled` |
| Left label | TEXT | `Field Label` | texto fuente no editable como propiedad |
| Right label | TEXT | `Field Label` | idem |
| Show left label | BOOLEAN | false | visibilidad fuente izquierda |
| Show right label | BOOLEAN | false | visibilidad fuente derecha |

Las propiedades TEXT y BOOLEAN se conectan a las 24 capas de etiqueta. `Field Label` es solo placeholder.

## 5. Variants

Matriz exacta 3×4: `Selection=Selected/Indeterminate/Unselected` × `State=Default/Hover/Focus/Disabled`, doce variantes. Default del set: Selected/Default como en fuente. `enabled` se normaliza a `Default`; no se añaden Press, Error, tamaños u otras combinaciones.

## 6. Sizes

Wrapper sin etiquetas visibles 24×24; geometría principal 18×18, icono 12×12 (`size/md` local), stroke 2 px (`stroke/md`) y radio 4 (`radius/sm`). `radius/md` remoto de fuente mide 4; el nombre local `radius/md` mide 8, por eso se usa `radius/sm` sin cambiar la apariencia. El tamaño visual no acredita área de activación web.

## 7. States

| Selection | State | Fill o borde principal | Icono |
|---|---|---|---|
| Selected/Indeterminate | Default, Focus | `color/background/control-selected` | `color/icon/on-brand` |
| Selected/Indeterminate | Hover | `color/background/control-selected-hover` | `color/icon/on-brand` |
| Selected/Indeterminate | Disabled | `color/background/disabled` | `color/icon/on-brand` |
| Unselected | Default, Focus | sin fill; `color/border/control` | ninguno |
| Unselected | Hover | sin fill; `color/border/hover` | ninguno |
| Unselected | Disabled | sin fill; `color/border/disabled` | ninguno |

Focus usa dos efectos `DROP_SHADOW` de spread 4/2, tokens `color/focus/effect-outer`/`effect-inner`. En Unselected/Focus, el stroke de 2 px se alinea `OUTSIDE` como fuente; los otros strokes son `INSIDE`. El contorno Unselected Default/Focus pasa de neutral 400 fuente a neutral 500 local para alcanzar 4.76:1 sin colorear el fondo. Disabled no significa Unselected.

## 8. Behavior

Estados visuales estáticos, sin reacciones. No añadir clic, toggle, transición ni sincronización entre checkboxes en Figma. Un contrato de comportamiento posterior debe definir cambios de valor, indeterminate, teclado y agrupación.

## 9. Accessibility

La página debe recordar que cada instancia real necesita etiqueta clara y nombre accesible. El anillo Focus y contraste de estados operables se revisan visualmente; no se declara cumplimiento WCAG, hit target ni semántica web.

## 10. Design tokens

| Uso | Rol de destino y scope |
|---|---|
| Fill seleccionado | `color/background/control-selected` `VariableID:140:122`, `SHAPE_FILL` |
| Fill seleccionado hover | `color/background/control-selected-hover` `VariableID:140:123`, `SHAPE_FILL` |
| Fill disabled | `color/background/disabled` `VariableID:13:38`, `SHAPE_FILL` |
| Borde Unselected | `color/border/control` `VariableID:123:122`, `color/border/hover` `VariableID:13:19`, `color/border/disabled` `VariableID:13:17`; `STROKE_COLOR` |
| Check/Minus blanco | `color/icon/on-brand` `VariableID:13:23`, `SHAPE_FILL` solo en vectores |
| Focus | `color/focus/effect-outer` `VariableID:136:122` y `effect-inner` `VariableID:136:123`; `EFFECT_COLOR` |
| Etiquetas | `color/text/primary` `VariableID:13:27` / `color/text/disabled` `VariableID:13:30`; `TEXT_FILL` |
| Tipografía | `font/family/base`, `font/weight/regular`, `font/size/sm`, `font/line-height/sm`, `font/letter-spacing/normal` |
| Geometría | `spacing/sm` `VariableID:12:30`, `radius/sm` `VariableID:13:5`, `stroke/md` `VariableID:13:3`, `size/md` `VariableID:12:21` |

Los roles cromáticos de selección ya existen en [JSON de extensión](../drafts/foundations/ai-design-system.radio-indicator-colors.v0.1.0.json) y en Figma, con alias a primitivas existentes por modo. No se crean tokens nuevos ni se usan colores de text para shapes.

## 11. Content rules

`Field Label` se cambia antes de usar la instancia en un producto. Ambas etiquetas pueden mostrarse independientemente por fidelidad a la fuente; se recomienda evitar redundancia visual. El componente no define microcopy concreto.

## 12. Composition rules

Las instancias Check/Minus conservan sus keys Phosphor. Una variante Unselected no contiene icono. Auto layout HORIZONTAL, gap `spacing/sm`, sin padding, orden izquierda–indicador–derecha. Las etiquetas crecen con su contenido sin truncamiento impuesto.

## 13. Responsive behavior

No se infieren breakpoints de la fuente. El indicador mantiene 24×24; con etiquetas visibles el wrapper abraza contenido.

## 14. Edge cases

Ambas etiquetas ocultas dejan el control sin texto visual; el uso real requiere nombre accesible. Ambas etiquetas visibles conservan orden y gap. Unselected/Focus usa contorno y efectos simultáneos. Disabled+Focus no existe en la matriz.

## 15. Forbidden combinations

Solo doce pares Selection×State. Indeterminate no se representa como combinación simultánea de booleanos Selected/Unselected. No hay Loading, Error ni Press.

## 16. Design ↔ Code mapping

Selection y State son ejes visuales de Figma; futura API web (`checked`, `indeterminate`, `disabled`) necesita contrato propio. Ninguna propiedad Figma prueba equivalencia semántica de código.

## 17. Acceptance criteria

| ID | Verificación |
|---|---|
| AC-CBX-001 | Página `Checkboxes` única, set `Checkbox` de doce variantes; familias existentes intactas. |
| AC-CBX-002 | Ejes/defaults exactos y geometría 24/18/12, radio 4 y stroke 2 ligados a tokens locales. |
| AC-CBX-003 | Ocho instancias Phosphor activas Check/Minus correctas, sin detachment ni icono en Unselected. |
| AC-CBX-004 | Dos TEXT y dos BOOLEAN conectadas a 24 etiquetas ocultas; bindings de tipografía y color correctos. |
| AC-CBX-005 | Todos los paints visibles y seis colores de efecto Focus usan variable local de categoría y scope correctos. |
| AC-CBX-006 | Contraste activo al menos 3:1 en los cuatro modos; diferencias frente a fuente documentadas y captura comparada. |
| AC-CBX-007 | Cero reacciones añadidas, documentación de límites de accesibilidad, `UNPUBLISHED` y auditoría humana pendiente. |

## 18. Examples

La captura fuente presenta tres filas Selected, Indeterminate y Unselected, cada una con cuatro estados. `Field Label` es ejemplo, no contenido de producto.

## 19. Source of truth

Markdown gobierna reglas; JSON aprobado y extensiones gobiernan variables. El set fuente `1221:28710` con key `7cd9c016ecf140eef806b29fb23de1d00a718471` se conserva como evidencia, no como componente de destino. IDs nuevos de Figma se registran tras construcción.

## 20. Change management

Diferencias deliberadas: enabled→Default; texto editable; radio fuente 4 mapeado a `radius/sm`; contorno neutral más contrastante; fill de selección ligado a rol de control, no acción primaria; foco tokenizado; helper local de uso único eliminado; interlineado 18→20. La biblioteca Phosphor permanece dependencia. Auditoría humana posterior.

## 21. Changelog

- 0.1.0 delegado: contrato destino basado en traversal completo del origen y tokens locales preflight; sujeto a QA documental antes de escritura Figma.
