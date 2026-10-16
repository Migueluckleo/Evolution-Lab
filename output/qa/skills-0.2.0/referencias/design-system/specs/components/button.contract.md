---
contract_schema: sdd-project/0.2
contract_id: BUTTON-001
name: Button
type: component
status: APPROVED
version: 0.1.0
owner: null
last_updated: 2026-09-23
review_targets:
  - figma
sources:
  - SRC-FIGMA-BUTTON-001
  - SRC-FIGMA-PHOSPHOR-001
data_refs:
  - sources/figma-snapshots/button-26-81.snapshot.json
dependencies:
  - PLUS-CIRCLE-OBSERVED-001
  - PHOSPHOR-ICONS-001
  - FOUNDATIONS-TOKENS-001
---

# Contrato aprobado: Button

> Aprobado por el usuario para el alcance Figma de `BUTTON-001` versión `0.1.0`, según `DEC-BUTTON-001`. La evidencia observada documenta el set `26:81`; este contrato no es código de aplicación, no demuestra intención histórica del producto ni valida por sí mismo la implementación existente. La procedencia de iconos también consta en `DEC-ICONS-001`.

## Alcance de la revisión

Se inspeccionó completamente el component set `button` (`26:81`) y sus 364 nodos accesibles en `AI-Design-System`. El alcance cubre anatomía, propiedades nativas, 60 variantes, layout, estilos resueltos, bindings, contenido de ejemplo e interacciones expuestas. Web, semántica de producto, teclado, activación y conformidad de accesibilidad quedan fuera de la evidencia disponible.

La fuente observada ya vive en el archivo configurado como destino. Por ello, P04 deberá clasificar la operación como `VALIDATE_ONLY`, `UPDATE` o `MIGRATE` tras leer el estado actual; la aprobación documental no convierte la implementación existente en conforme por sí misma.

## 1. Purpose

`UNRESOLVED`: Figma identifica una familia llamada `button`, pero no contiene descripción ni enlaces de documentación. La apariencia, el nombre y los estados no demuestran por sí solos su intención de producto, reglas de uso ni equivalencia con un botón HTML.

## 2. Contract

| ID | Requisito aprobado | Fuerza | Procedencia | Fuente/localizador | Criterio |
|---|---|---|---|---|---|
| REQ-BTN-001 | La familia debe conservar los ejes `type`, `size` y `state` y las 60 combinaciones observadas. | MUST | OBSERVED + DERIVED | `SRC-FIGMA-BUTTON-001`, `26:81.variantGroupProperties` y 60 hijos | AC-BTN-001 |
| REQ-BTN-002 | Cada variante debe exponer texto, visibilidad de icono izquierdo/derecho y swaps independientes para ambos iconos, usando las claves nativas registradas. | MUST | OBSERVED | `26:81.componentPropertyDefinitions` | AC-BTN-002 |
| REQ-BTN-003 | La anatomía funcional debe conservar icono izquierdo, `label-text` e icono derecho; `default/focus` conserva el wrapper observado `btn-default` mientras no exista una decisión de normalización. | MUST | OBSERVED | subárbol `26:81` | AC-BTN-003 |
| REQ-BTN-004 | Layout, tipografía, visuales y bindings deben corresponder a tamaño, tipo y estado según este contrato y el inventario técnico YAML; un literal equivalente no sustituye un binding. | MUST | OBSERVED + regla SDD | inspección Plugin API; `button.contract.yaml` | AC-BTN-004 |
| REQ-BTN-005 | El valor inicial del texto debe ser `Default`; los iconos izquierdo y derecho deben estar visibles por defecto y usar `PlusCircle / Outline / Light` como swap activo. | MUST | OBSERVED | definiciones de propiedades y componentes `26:3`/`26:2` | AC-BTN-005 |
| REQ-BTN-006 | No se deben completar, corregir ni generalizar interacciones ausentes sin una decisión explícita. Las 23 reacciones observadas se conservan como evidencia, no como modelo conductual aprobado. | MUST NOT | OBSERVED + gobernanza SDD | `reactions` de variantes | AC-BTN-006 |
| REQ-BTN-007 | La implementación Figma aprobada debe residir en una página canónica exclusiva de la familia; el nombre de página permanece pendiente de decisión. | MUST | EXPLICIT | P04 §3 | AC-BTN-007 |
| REQ-BTN-008 | No se define API, paquete, semántica DOM ni comportamiento web en esta versión. | MUST NOT | UNRESOLVED / límite de alcance | ausencia de fuente web | AC-BTN-008 |
| REQ-BTN-009 | Los iconos de Button, incluidos ambos swaps, deben consumir componentes de la biblioteca Figma `Phosphor Icons` indicada por el usuario. La identidad se comprobará por key, no por semejanza visual ni solo por nombre. | MUST | EXPLICIT + OBSERVED | `DEC-ICONS-001`; `SRC-FIGMA-PHOSPHOR-001`; comparación de keys de `PlusCircle` | AC-BTN-009 |

## 3. Anatomy

```text
button (COMPONENT_SET 26:81)
└─ variant (COMPONENT; 60 combinaciones)
   ├─ PlusCircle (INSTANCE; icono izquierdo)
   ├─ label-text (TEXT)
   └─ PlusCircle (INSTANCE; icono derecho)
```

Excepción observada: las tres variantes `type=default, state=focus` contienen un frame `btn-default` que envuelve los mismos tres roles funcionales.

| Parte | Nodo observado | Condición | Fuente |
|---|---|---|---|
| Contenedor de familia | `COMPONENT_SET 26:81` | Siempre | Plugin API |
| Variante | `COMPONENT` | Una de 60 | hijos directos |
| Icono izquierdo | instancia de `PlusCircle` | Visible por defecto; Boolean + INSTANCE_SWAP | referencias de propiedades |
| Etiqueta | `TEXT label-text` | Texto editable; default `Default` | `text#1205:13` |
| Icono derecho | instancia de `PlusCircle` | Visible por defecto; Boolean + INSTANCE_SWAP | referencias de propiedades |

## 4. Properties

| Clave nativa Figma | Tipo | Default | Valores disponibles/alcance |
|---|---|---|---|
| `show right icon#1017:0` | BOOLEAN | `true` | `true`, `false` |
| `show left icon#1017:13` | BOOLEAN | `true` | `true`, `false` |
| `text#1205:13` | TEXT | `Default` | Cadena; límites no definidos |
| `left icon#2828:101` | INSTANCE_SWAP | `26:3` | 1512 candidatos preferidos expuestos; no resueltos en profundidad |
| `right icon#2828:162` | INSTANCE_SWAP | `26:3` | 1512 candidatos preferidos expuestos; no resueltos en profundidad |
| `type` | VARIANT | `primary` | `primary`, `default`, `text`, `link` |
| `size` | VARIANT | `large` | `large`, `middle`, `small` |
| `state` | VARIANT | `default` | `default`, `hover`, `press`, `disabled`, `focus` |

## 5. Variants

El set contiene exactamente el producto cartesiano observado `4 × 3 × 5 = 60`. Esto acredita disponibilidad en Figma, no intención de uso del producto.

| Eje | Valores observados |
|---|---|
| `type` | `primary`, `default`, `text`, `link` |
| `size` | `large`, `middle`, `small` |
| `state` | `default`, `hover`, `press`, `disabled`, `focus` |

## 6. Sizes

| Tamaño | Alto | Anchos observados | Icono | Fuente tipográfica | Line-height |
|---|---:|---|---:|---:|---:|
| `large` | 48 px | 135 o 154 px | 24 px | 16 px | 20 px |
| `middle` | 40 px | 127 o 146 px | 20 px | 16 px | 20 px |
| `small` | 32 px | 120 o 139 px | 20 px | 14 px | 20 px |

Los anchos son resultado observado con el texto `Default` y ambos iconos visibles; no son una regla de ancho fijo para contenido arbitrario. Las variantes usan auto-layout horizontal y `HUG` horizontal.

## 7. States

| Estado | Evidencia visual | Interacción demostrada |
|---|---|---|
| `default` | Tokens base por tipo | Las 12 variantes cambian a `hover` con `ON_HOVER` |
| `hover` | Tokens hover por tipo | Solo las tres variantes `link` cambian a `press` con `ON_PRESS` |
| `press` | Tokens active/brand por tipo | Sin reacción saliente observada |
| `focus` | Stroke de 2 px con `color/border/hover` | Ocho reacciones `ON_HOVER`; cobertura parcial |
| `disabled` | Tokens disabled | Sin lógica de bloqueo de eventos demostrada |

## 8. Behavior

Figma define 23 reacciones `CHANGE_TO` sin transición animada:

- 12 `default → hover` mediante `ON_HOVER`.
- 3 `link/hover → link/press` mediante `ON_PRESS`.
- 8 `focus → hover` mediante `ON_HOVER`.

Hallazgos que requieren decisión antes de adoptar comportamiento:

- `default/middle/focus` y `default/small/focus` apuntan a `default/large/hover`.
- `primary/small/focus` no tiene la reacción que sí aparece en large/middle.
- `text/focus` no tiene reacciones salientes.
- No existe cobertura general de click/tap, teclado, entrada/salida de focus, release, navegación o supresión de eventos en disabled.

## 9. Accessibility

| Aspecto | Evidencia | Estado |
|---|---|---|
| Etiqueta visible | Texto editable `Default` | OBSERVED |
| Indicador de focus | Stroke visible de 2 px en variantes focus | OBSERVED; no prueba criterio WCAG |
| Nombre accesible | No expuesto | UNRESOLVED |
| Rol/semántica | No expuesto | UNRESOLVED |
| Teclado y activación | No expuesto | UNRESOLVED |
| Contraste | No evaluado | UNRESOLVED |

## 10. Design tokens

Se observaron 35 variables: 26 locales y 9 remotas, todas resueltas por la Plugin API; no se observaron estilos nombrados. La lista completa de IDs, keys, colecciones, valores resueltos y `used_by` vive en [button.contract.yaml](../../drafts/contracts/button.contract.yaml). No se duplica aquí la `description` canónica de ninguna variable.

Categorías usadas: `color/background`, `color/border`, `color/icon`, `color/interactive`, `color/text`, `font`, `radius`, `size`, `spacing` y `stroke`. La mezcla de variables locales y remotas con nombres equivalentes —por ejemplo `font/family/base`— se conserva; no se normaliza por nombre o valor.

## 11. Content rules

`Default` es contenido de ejemplo y default de la propiedad TEXT, no una regla editorial. No hay evidencia sobre longitud máxima, cadenas vacías, localización, truncamiento o wrapping. El texto usa `Manrope`, line-height 20 px y tamaños 16/14 según tamaño.

## 12. Composition rules

Los iconos son instancias activas de la variante remota `PlusCircle / Format=Outline, Weight=Light` (`26:3`, set `26:2`). Ambos slots son independientes y exponen visibilidad y swap. La lista de 1512 candidatos preferidos por swap se conserva como conteo; no se infiere que cada candidato sea semánticamente válido para Button.

Por [DEC-ICONS-001](../../registry/decisions.md), la única fuente autorizada para iconos del sistema es el archivo Figma [Phosphor Icons](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=7484-1322&t=5f3sI6AFFHMgcXfl-1). El set `PlusCircle` de esa fuente tiene key `322a346f2ce54ea1534d8b0a682a8139d9f20e87` y su variante `Format=Outline, Weight=Light` tiene key `46d251bb4099700c5852180f2370d265e5166432`: ambas coinciden con las keys remotas observadas en Button. Esta coincidencia verifica la procedencia del componente activo; no valida por sí sola los 1512 candidatos de swap ni todos los iconos de otras familias.

## 13. Responsive behavior

El componente observado usa auto-layout horizontal, gap de 8 px, alto fijo por size y ancho `HUG`. No se observaron breakpoints, `fullWidth`, wrapping ni reglas de adaptación al viewport. Los anchos de la captura no se convierten en restricciones universales.

## 14. Edge cases

| Caso | Estado |
|---|---|
| Texto vacío | UNRESOLVED |
| Ambos iconos ocultos | Disponible por propiedades; apariencia/uso no evaluados |
| Texto largo o multilínea | UNRESOLVED |
| Icono swap con dimensiones distintas | UNRESOLVED |
| `disabled` con eventos | UNRESOLVED; la etiqueta visual no demuestra bloqueo |
| Cambio de modo de variables | Variables multi-modo presentes; QA visual por modo no ejecutado |

## 15. Forbidden combinations

No se observaron combinaciones prohibidas entre `type`, `size` y `state`; existen las 60 combinaciones. No se definen prohibiciones de propiedades o contenido en esta versión.

## 16. Design ↔ Code mapping

| Concepto | Figma observado | Web | Límite |
|---|---|---|---|
| Tipo visual | VARIANT `type` | UNRESOLVED | No se propone prop web |
| Tamaño | VARIANT `size` | UNRESOLVED | No se convierten unidades |
| Estado | VARIANT `state` | UNRESOLVED | Estado visual no equivale a lógica |
| Texto | TEXT property | UNRESOLVED | Semántica y restricciones pendientes |
| Iconos | Boolean + INSTANCE_SWAP por lado | UNRESOLVED | API conceptual pendiente |
| Página Figma | Actualmente `Page 1` (`0:1`) | N/A | P04 exige página exclusiva; nombre pendiente |

## 17. Acceptance criteria

| ID | REQ | Destino | Comprobación | Evidencia |
|---|---|---|---|---|
| AC-BTN-001 | REQ-BTN-001 | Figma | Leer e igualar 60 combinaciones y valores de ejes | readback completo |
| AC-BTN-002 | REQ-BTN-002 | Figma | Comparar definiciones y referencias de propiedad | Plugin API |
| AC-BTN-003 | REQ-BTN-003 | Figma | Comparar árbol funcional y excepción focus/default | jerarquía + captura |
| AC-BTN-004 | REQ-BTN-004 | Figma | Comparar layout, visuales, tipografía y bindings por identidad de variable | readback exhaustivo |
| AC-BTN-005 | REQ-BTN-005 | Figma | Leer defaults y componente activo de ambos swaps | definiciones + main component |
| AC-BTN-006 | REQ-BTN-006 | Figma | Verificar que toda interacción implementada esté aprobada; faltantes no pasan por inferencia | matriz de reacciones |
| AC-BTN-007 | REQ-BTN-007 | Figma | Confirmar página exclusiva y page ID real | inventario de páginas |
| AC-BTN-008 | REQ-BTN-008 | Web | Confirmar que no se declara implementación web | revisión documental |
| AC-BTN-009 | REQ-BTN-009 | Figma | Resolver el componente principal de cada icono usado y comparar su key con el componente correspondiente del archivo Phosphor Icons; rechazar copias desvinculadas o de otra biblioteca | readback de instancias y fuente |

## 18. Examples

- Válido observado: `type=primary, size=large, state=default`, texto `Default`, dos `PlusCircle` visibles.
- Válido observado: `type=text, size=small, state=disabled`.
- No normativo: ocultar ambos iconos es posible por propiedades, pero su uso no está definido.
- No aprobado: corregir automáticamente destinos de interacción o completar eventos ausentes.

## 19. Source of truth

| Fuente | Localizador | Snapshot/digest | Rol |
|---|---|---|---|
| SRC-FIGMA-BUTTON-001 | URL Figma, file `tj3WIBEZDGLVs7MJWKCwgf`, node `26:81` | JSON snapshot; digest registrado en `registry/sources.md` | Evidencia observacional de solo lectura |
| SRC-FIGMA-BUTTON-001-IMG | [captura](../../sources/figma-snapshots/button-26-81.png) | SHA-256 `8b4a7c85f3ec9138a0588f8b922b676696d81f8ffb503d2cef3bb04ba7a4bd04` | Corroboración visual |
| SRC-FIGMA-PHOSPHOR-001 | [snapshot PlusCircle](../../sources/figma-snapshots/phosphor-plus-circle.snapshot.json) | SHA-256 `c3529c0ecc28a2cb1cdb2af852b3b72bd7f5751639bf89c73e712037e9813e60` | Fuente de iconos seleccionada por el usuario; identidad de componente observada |
| DEC-ICONS-001 | [decisión de iconos](../../registry/decisions.md) | 2026-09-23 | Regla explícita global de procedencia; la aprobación integral consta por separado en DEC-BUTTON-001 |
| FOUNDATIONS-TOKENS-001 | [contrato aprobado](../../specs/foundations/foundations-tokens.contract.md) | versión `0.1.0` | Autoridad vigente de variables locales aprobadas, no del componente |

Este MD gobierna las reglas aprobadas para Figma y el YAML técnico conserva la evidencia normalizada. El nodo Figma observado sigue siendo evidencia; la conformidad de la implementación requiere preflight, readback y QA por separado. La aprobación se registra en `DEC-BUTTON-001`.

## 20. Change management

Todo cambio normativo exige una nueva revisión y aprobación. La corrección de interacciones, la normalización de variables remotas/locales, el movimiento a una página dedicada y cualquier mapeo web son cambios separados que no se ejecutarán silenciosamente.

## 21. Changelog

| Versión | Fecha | Cambio | Fuente/decisión |
|---|---|---|---|
| 0.1.0 | 2026-09-23 | Primer candidato basado en inspección completa read-only de `26:81` | SRC-FIGMA-BUTTON-001; aprobación pendiente |
| 0.1.0 · revisión de candidato | 2026-09-23 | Se incorpora la fuente obligatoria Phosphor Icons y se verifica PlusCircle por key; sin aprobación de Button | DEC-ICONS-001; SRC-FIGMA-PHOSPHOR-001 |
| 0.1.0 · publicación | 2026-09-23 | Publicación administrativa del candidato aprobado para Figma; requisitos, criterios, conteos y alcance sin cambios | DEC-BUTTON-001 |

## Anexo de revisión

Véanse [reporte de síntesis](../../drafts/reports/button.synthesis.md), [revisión documental](../../qa/contracts/button.review.md) y [modelo técnico YAML](../../drafts/contracts/button.contract.yaml). Preparación Figma: pendiente de preflight y de resolver la página canónica y las variables remotas. La procedencia de los iconos ya fue decidida; no se infiere validación de implementación.
