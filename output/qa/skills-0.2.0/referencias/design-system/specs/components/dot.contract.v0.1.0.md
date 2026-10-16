---
contract_schema: sdd-project/0.2
contract_id: DOT-001
name: Dot
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Dots
sources: [SRC-FIGMA-DOT-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/dot.source.component-contract.yaml, drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-DOT-BACKGROUND-COLORS-001]
user_audit: PENDING
---

# Dot · contrato de reconstrucción 0.1.0

## 1. Purpose

Indicador compacto de presencia o conteo visual. La [fuente MD](../../drafts/contracts/dot.source.component-contract.md) y [YAML](../../drafts/contracts/dot.source.component-contract.yaml) documentan el set antiguo; su Description contiene contradicciones y no define comportamiento automático.

## 2. Contract

Crear una página funcional `Dots` y un set `Dot` en `AI-Design-System` `tj3WIBEZDGLVs7MJWKCwgf`. Mantener las 15 combinaciones y la apariencia de origen, corrigiendo únicamente la categoría semántica de los fills mediante la [extensión de fondos](../../drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json). No publicar biblioteca ni implementar web.

## 3. Anatomy

Cada variante es un componente raíz circular o pill con fill, stroke exterior blanco 1 px y radio full. Los tipos Count y Overflow incluyen un TEXT centrado; los demás no tienen hijos. No hay iconos ni dependencias de componente.

## 4. Properties

| Propiedad | Tipo | Default | Mapeo |
|---|---|---|---|
| Type | VARIANT | Active | active→Active, busy→Busy, inactive→Inactive, number→Count, number expand→Overflow |
| Size | VARIANT | Large | small→Small, middle→Medium, large→Large |
| Count | TEXT | `1` | tres variantes Count |
| Overflow label | TEXT | `99+` | tres variantes Overflow |

Las dos propiedades TEXT son nuevas y separadas para que cada familia numérica conserve su ejemplo propio. No definen cálculo del contador.

## 5. Variants

Matriz 5×3 completa: Active, Busy, Inactive, Count, Overflow × Small, Medium, Large. No se crean estados Hover/Focus/Disabled, ya que no se observan. Type=Active y Size=Large son defaults como en la fuente.

## 6. Sizes

Active/Busy/Inactive/Count: Small 8×8, Medium 12×12, Large 16×16. Overflow: Small 12×8, Medium 23×12, Large 23×16. Se ligan las dimensiones que coinciden con la escala semántica `size/sm`, `size/md`, `size/lg`; anchuras 23 y combinaciones pill sin token exacto quedan como geometría literal documentada, no se inventa una primitiva de 23. Stroke 1 px usa `stroke/xs`; radio `radius/full`.

## 7. States

Los tipos son significados de estado o conteo, no interacciones. Active = verde #098300, Busy = rojo #d40000, Inactive = neutral pálido #e2e8f0, Count/Overflow = rojo #d40000. Se conserva el borde exterior blanco. Inactive expresa disponibilidad, no un control deshabilitado.

## 8. Behavior

Puramente estático. La fuente no tiene reacciones ni prueba de cambio automático entre Count y Overflow; un consumidor debe elegir la variante. No se define umbral numérico funcional ni notificación en tiempo real.

## 9. Accessibility

La tipografía fuente de 4 px en Small y 8 px en Medium/Large es un riesgo de legibilidad. Se conserva visualmente para auditoría, pero las variantes numéricas no quedan avaladas para comunicar un conteo indispensable sin alternativa textual accesible. El Dot no debe ser la única señal de estado: el producto debe proveer etiqueta/estado equivalente y validar contraste en el contexto donde se superpone. No se declara WCAG ni accesibilidad web.

## 10. Design tokens

| Propiedad | Token y scope |
|---|---|
| Fill Active | `color/background/status-active` `FRAME_FILL` |
| Fill Busy | `color/background/status-busy` `FRAME_FILL` |
| Fill Inactive | `color/background/status-inactive` `FRAME_FILL` |
| Fill Count/Overflow | `color/background/notification-count` `FRAME_FILL` |
| Stroke blanco | `color/border/on-brand` `VariableID:13:18`, `STROKE_COLOR` |
| Texto blanco | `color/text/on-brand` `VariableID:13:33`, `TEXT_FILL` |
| Fuente y peso | `font/family/base` `VariableID:10:2`, `font/weight/bold` `VariableID:10:6` |
| Geometría | `radius/full` `VariableID:13:11`, `stroke/xs` `VariableID:12:41`, `size/sm/md/lg` locales cuando corresponda |

Los cuatro fills nuevos aliasan primitivas existentes en los cuatro modos; no se reutilizan roles de icono para fondos. Los fontSize literales 4/8 no tienen equivalente local aprobado y quedan excepción rastreada; no se inventa una variable ni se usa un token de width como FONT_SIZE.

## 11. Content rules

`1` y `99+` son ejemplos editables, no reglas de truncamiento. `Overflow label` no implica que el componente transforme 100 en `99+`. El consumidor define representación y accesibilidad del conteo real.

## 12. Composition rules

El Dot puede acompañar otros elementos, pero este set no incluye ni posiciona avatar, botón o icono anfitrión. El borde blanco preserva separación visual de la fuente. No se inventan offsets de superposición.

## 13. Responsive behavior

No hay evidencia de breakpoints. La familia ofrece tres tamaños explícitos; no cambia tamaño automáticamente.

## 14. Edge cases

Con texto largo fuera de los ejemplos, Count puede desbordarse; el consumidor debe elegir Overflow o una solución de producto. Small numérico presenta legibilidad limitada y requiere alternativa accesible. Inactive sobre superficie clara puede tener contraste insuficiente; se valida en contexto antes de uso.

## 15. Forbidden combinations

Solo los 15 pares Type×Size. No hay estado Disabled, Hover, Focus, selección ni carga. No se prohíbe ninguna de las combinaciones observadas, pero el uso de Small numérico queda condicionado por la nota de accesibilidad.

## 16. Design ↔ Code mapping

Figma Type y Size son elección visual. Futura API deberá definir estado, count, cap, contenido accesible y placement. No se genera código.

## 17. Acceptance criteria

| ID | Requisito verificable |
|---|---|
| AC-DOT-001 | Página `Dots` única, set `Dot` de 15 variantes, familias anteriores intactas. |
| AC-DOT-002 | Ejes/defaults exactos; tamaños observados y forma circular/pill sin clipping. |
| AC-DOT-003 | Cuatro fills nuevos creados desde JSON, con 16 aliases a primitivas, scope `FRAME_FILL` y readback antes de consumir. |
| AC-DOT-004 | Todos los fills, strokes y textos visibles con categorías/scopes semánticos correctos; radio y stroke ligados. |
| AC-DOT-005 | Seis textos con propiedades TEXT conectadas, Manrope Bold, `1`/`99+` por variante. |
| AC-DOT-006 | Fuente y destino comparados visualmente, excepciones de fontSize 4/8 y legibilidad documentadas, cero reacciones. |
| AC-DOT-007 | `UNPUBLISHED`, auditoría humana pendiente; no afirmación de comportamiento ni accesibilidad web. |

## 18. Examples

`1` y `99+` son ejemplos visuales de la fuente. No se deduce un máximo de conteo.

## 19. Source of truth

Markdown gobierna reglas; JSON aprobado y extensión gobiernan tokens. Fuente `1133:31549`, key `bc7fd5437899a1868aeba789925329c30d5b6996`; IDs destino se registran tras Figma. La Description antigua contradictoria permanece evidencia, no norma.

## 20. Change management

Se normaliza nomenclatura de ejes y se añaden propiedades TEXT; nuevos roles de fondo preservan RGB y aliases a primitivas. No se corrige silenciosamente tipografía diminuta ni contraste contextual; se deja para auditoría y contrato de comportamiento. Cualquier cambio de tamaño o legibilidad requiere enmienda versionada.

## 21. Changelog

- 0.1.0 delegado: matriz 15, tokens de fondo estrictamente semánticos y excepción visible de tipografía numérica.
