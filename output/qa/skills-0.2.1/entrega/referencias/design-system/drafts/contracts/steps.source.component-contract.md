# Steps · contrato de observación de la Librería anterior

Estado: `OBSERVED`; este documento describe la fuente, no aprueba su reconstrucción. Fuente: archivo Figma `9zs5RMR8LB5wHjW9Bd59BA`, página `❖ Steps` (`7861:714`), sección `Steps` (`8029:8263`). Inspección: 2026-09-24. Los IDs de destino se registrarán por separado.

## Inventario comprobado

| Set fuente | ID | Variantes | Ejes |
|---|---|---:|---|
| `Steps` público | `8029:8267` | 6 | `On color={On White, On Primary}` × `Type={Gallery, Numbers, Gallery only}` |
| `.Dot` interno | `8029:8294` | 4 | `Primary={true,false}` × `Selected={true,false}` |
| `.Combination` interno | `8029:8320` | 27 | `Number=02…07`; `Step=1…Number` |

Total observado: 37 variantes. Los sets internos de 7 pasos usan a su vez `.Color` (`8029:8304`), que conserva las siete instancias `.Dot`; no son una variante vacía.

## Geometría y contenido

`Gallery` mide 191×32 px, `Numbers` 196×32 px y `Gallery only` 40×8 px. En `Gallery`, los botones de texto izquierdo y derecho miden 76×32 y 75×32 px, rodean una combinación de tres dots de 40×8 px y muestran `Back` y `Next`. `Numbers` sustituye los dots por el ejemplo estático `5 / 6` en 45×20 px, conservando los botones. `Gallery only` contiene solo los tres dots visibles; la variante On Primary retiene dos botones ocultos en la estructura. Los dots tienen caja 8×8 px, centro seleccionado de 8 px y no seleccionado de 6 px; la separación de centros es 16 px. Las combinaciones de 2 a 7 dots miden 24, 40, 56, 72, 88 y 104 px de ancho, respectivamente.

La fuente no muestra un fondo propio en las variantes públicas: `On Primary` describe el contexto de colocación. La muestra de documentación coloca estas variantes sobre un fondo azul externo. Los botones son instancias de la biblioteca anterior (`1443:281`) con iconos de flecha y texto Manrope Regular de 14 px. No asumir que esas instancias deben seguir remotas en el destino.

## Color observado y procedencia

| Uso | Fuente observada | Evidencia |
|---|---|---|
| Dot seleccionado On White | `#3255F7` | variable de la fuente `2849:196141` |
| Dot no seleccionado On White | `#E2E8F0` | variable de la fuente `2849:196106` |
| Dot seleccionado `.Dot Primary=false` | `#FFFFFF` | variable de la fuente `2849:196104` |
| Dot no seleccionado `.Dot Primary=false` | `#7D9AFF` | fill literal en la fuente |
| Texto e icono de botones On White | `#0F172A` | variables fuente de roles text/icon |
| Texto e icono de botones On Primary | `#FFFFFF` | variables fuente de roles text/icon |
| Texto del contador On White | aprox. `#323338` | alias de variable remota; el RGB de la capa es evidencia |
| Texto del contador On Primary | `#FFFFFF` | visible en variante fuente |

## Contradicciones y límites de evidencia

La variante pública `On Primary / Gallery` no consume el set `.Combination` local de esta página. Usa otro `Combination` (`8029:8134`) cuyo dot seleccionado es `#0073EA` y no seleccionado `#DCDFEC`. En cambio, `On Primary / Gallery only` usa la misma `.Combination` azul/gris de `On White`, a pesar de estar rotulada On Primary. La variante `.Dot Primary=false` presenta una tercera interpretación —blanco y azul claro— que es la única paleta contextual coherente sobre el fondo de muestra. Los tres hechos deben quedar separados en el contrato de destino; no afirmar que la fuente es internamente consistente.

Una variante `.Dot` no seleccionada (`8029:8297`) tiene reacción `ON_HOVER → CHANGE_TO` sin `destinationId`; no demuestra un estado de destino ejecutable. No se observaron reacciones en el set público ni en `.Combination`. No se deducen reglas para habilitación de botones, incrementos, límites, teclado ni accesibilidad web.

## Regla verificable para reconstrucción

El contrato de destino debe mapear cada dot y cada texto/icono a variables semánticas locales del scope correcto, con alias a primitivas existentes del JSON. Si se normalizan las contradicciones de On Primary, registrar la desviación de RGB y pedir auditoría por excepción, sin añadir primitivas ajenas a la paleta ni presentar los ejemplos `5 / 6` como datos calculados.
