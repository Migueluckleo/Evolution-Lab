---
contract_schema: figma-component-contract/1
contract_id: SRC-FIGMA-SCROLLBAR-001
name: Scrollbar — observed source
status: SOURCE_INSPECTED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_page_id: "3910:928"
source_set_id: "7664:49488"
source_key: d3d06e195e2bdb6fc5d2bc9e10f33a8edb2f357c
read_only: true
last_inspected: 2026-09-24
---

# Scrollbar · contrato fuente observado

Esta es evidencia de la [Librería anterior](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7664-49488), no una especificación aprobada del destino. La página contiene cinco component sets: el público `Scroll Bar` de ocho variantes y cuatro sets internos por tamaño de thumb, con 22 variantes de posición/orientación adicionales. Se recorrieron 125 nodos de esos sets y se revisó una captura del set público. No hay reacciones de prototipo ni propiedades de contenido.

## Ejes, composición y geometría

El set público declara `Orientation={vertical,horizontal}` y `Thumb Size={25%,33%,50%,75%}`. Cada variante contiene una instancia del set interno correspondiente, por defecto en primera posición. Las variantes verticales son 14×280 px y las horizontales 280×16 px. En vertical la instancia ocupa 6×272 px con padding exterior de 4 px; en horizontal la instancia original está rotada 90°, pero la captura confirma que se ve como una barra horizontal. El thumb mide 6 px de grosor con radio 3 px. El track es transparente: los `Track Spacer` sirven para posicionamiento, no tienen fill visible.

| Tamaño rotulado | Set interno | Posiciones observadas por orientación | Longitud del thumb en el set público de 272 px | Longitud en el set interno de 280 px |
|---|---|---:|---:|---:|
| 25% | `7706:49949` | 4 | 70 px | 70 px |
| 33% | `7706:50034` | 3 | 90.6667 px | 93.3333 px |
| 50% | `7706:50119` | 2 | 136 px | 140 px |
| 75% | `7706:50204` | 2 | 240 px | 248 px |

El cuarto tamaño es una inconsistencia: 240/272 ≈ 88.24% en el set público y 248/280 ≈ 88.57% en el interno, no 75%. Su segunda posición también usa radio 4 px en vez de 3 px. Se registra el dato sin reinterpretarlo como regla de scroll. En el set interno, las posiciones de 25%, 33% y 50% son segmentos consecutivos; la de 75% solo tiene inicio y fin, con 32 px restantes.

## Color, tokens y contenido

Los 30 thumbs inspeccionados usan fill sólido sin binding de variable, RGB `195,198,212` (`#C3C6D4`); la fuente no aporta un token para ese fill. La captura muestra el mismo gris en barras verticales y horizontales. No hay texto dentro de los componentes, ni roles tipográficos que migrar. Los textos de documentación `Percentage`, `Position` y `Orientation` incluyen descripciones copiadas de Button; no se toman como reglas de Scrollbar.

## Comportamiento y límites

No se observan drag, hover, focus, disabled, scroll real, cálculo de tamaño, teclado, ARIA ni hit target interactivo. Las posiciones son muestras discretas, no evidencia de un valor continuo. El porcentaje rotulado y la longitud real deben quedar diferenciados en el contrato destino; crear una corrección visual sería una decisión de diseño adicional.

## Conciliación prevista

El destino debe usar una página funcional `Scrollbars`, variable semántica de fondo con scope de shape y alias a una primitiva exacta del gris fuente. El inventario aprobado carece de esa primitiva: su extensión requiere JSON de destino, variable local y QA de paridad. El set público y los cuatro sets internos deben preservar identidad, variantes y composición; cualquier normalización de la orientación horizontal o del porcentaje 75% debe anotarse como transformación, no atribuirse al origen.
