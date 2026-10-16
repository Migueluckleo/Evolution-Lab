# Stepper · observación de la Librería anterior

Estado `OBSERVED`; inspección 2026-09-24. Fuente: archivo `9zs5RMR8LB5wHjW9Bd59BA`, página `❖ Multi Step Indicator (Wizard)  ✅` (`2166:596`), set público `container` (`2166:1499`, key `13119fb2380627682c0f22d3a3d59563cc4a832c`) y set interno `Progress line` (`2473:1781`, key `d90476f09539927ad4878ffb38ee7bef12fcbcbb`). La documentación de la página lo llama “Steppers”. Es una familia distinta del componente de puntos `Steps`.

## Matriz y propiedades

`container` tiene 18 variantes cartesianas: `type={vertical,horizontal}` × `state={checked,default,inactive}` × `position={start,middle,end}`. Expone texto `step` (`STEP 1`), `title` (`Step details`), `caption` (`Caption`), booleanas `show step` y `show caption`, y swap de icono. `Progress line` tiene ocho variantes: orientación vertical/horizontal × apariencia checked/default × posición start/end. No hay reacción de prototipo en ninguno de los sets.

## Medidas y anatomía

El indicador redondo `Number` mide 32×32 px y contiene un `CheckFat` de 16×16 px. La línea horizontal visible es 80×4 px dentro de una caja 80×32 px; la vertical es 4×32 px dentro de 12×32 px, salvo la salida de `vertical/start`, redimensionada a 21 px. Los extremos cercanos al indicador tienen radio 8 px y los extremos exteriores radio 0, según start/end. Los textos están en un bloque nominal de 77×57 px: `STEP 1` Manrope Regular 10/15, título Manrope SemiBold 14/21 y caption Manrope Regular 10/15.

| Orientación | start | middle | end |
|---|---:|---:|---:|
| horizontal | 116×97 | 200×97 | 161×97 |
| vertical | 117×57 | 117×104 | 117×68 |

En horizontal, start sitúa círculo en x=0 y línea saliente en x=36; middle sitúa líneas en x=0 y x=120 con círculo en x=84; end usa línea entrante x=0 y círculo x=84. Los detalles empiezan y=40; en middle/end se alinean con x=84. En vertical, start usa círculo y=0 y línea saliente y=36, middle usa círculo y=36 entre líneas y=0/72, y end usa línea entrante y=0 y círculo y=36. Los detalles empiezan en x=40 y se alinean a y=0/23.5/11 según posición.

## Colores observados

| Rol visual | checked | default | inactive |
|---|---|---|---|
| Fondo del círculo | `#098300` | `#3255F7` | `#E2E8F0` |
| Icono check | `#FFFFFF` | `#FFFFFF` | `#64748B` |
| Línea de progreso | `#098300` | `#E2E8F0` | `#E2E8F0` |

El rótulo y título usan `#64748B` en los tres estados; caption usa `#94A3B8`. Todos estos RGB tienen correspondencia exacta con primitivas existentes del JSON destino: emerald/600, blue/400, neutral/300, neutral/100, neutral/500 y neutral/400. Los fills fuente están vinculados a variables de la Librería anterior, no son autorización para reutilizar sus IDs en destino.

El modelo visible es una muestra de composición, no navegación funcional. No se observó cálculo de paso actual, cambios de estado, teclado, foco ni sincronización con datos. El extra `Content` de `horizontal/end` tiene un bar blanco oculto: no es una línea visible que deba copiarse.
