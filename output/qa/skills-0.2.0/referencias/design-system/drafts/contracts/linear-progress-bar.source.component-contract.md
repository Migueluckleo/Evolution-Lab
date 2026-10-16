# Linear Progress Bar · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, Linear Progress Bar](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7596-48397), set `7596:48397`, página `7568:47417`, key `c65677f139942b3cc11a8a8e8b3754029d044d57`.
- **Inspección:** `COMPLETE`, 336/336 nodos y 48/48 variantes leídos sin escritura. Captura del set inspeccionada. Esta evidencia no aprueba todavía la reconstrucción.

## Component Identity

**OBSERVED:** set de 1034×1402, un solo componente reutilizable con matriz completa Type primary/warning/danger/positive × Size small/middle/large × Percentage 25/50/75/100. Son 48 combinaciones reales, no un producto teórico añadido.

## Anatomy

Cada variante tiene tres hijos directos: fila Label + Percentage, frame `linear-progress-indicator` con un único frame `Progress bar`, y helper text. No hay instancias, vectores, iconos, imágenes ni nodos de otro componente.

## Dependencies

Doce variables únicas, todas locales: dos spacing, dos text colors, tres de familia/peso/tamaño tipográfico más font/size/sm, marca default y tres feedback/icon. No hay estilos nombrados ni reacciones. Los IDs exactos, categorías y scopes se conservan en el [YAML sincronizado](linear-progress-bar.source.component-contract.yaml).

## Properties

BOOLEAN `Show Percentage`, `Show label` y `Show helper text` default true; TEXT `✏️ Percentage` default `25%`, `✏️ Label` default `Label`, `✏️ helper text` default `Optional helper text`. VARIANT `Type` default primary, `Size` default small, `Percentage` default 25%. Los TEXT son ejemplos editables, pero `✏️ Percentage` no está sincronizado con la variante ni con la anchura.

## Variants

48/48 combinaciones presentes. La matriz precisa y los 48 IDs están en el YAML. Cada porcentaje ocupa exactamente 25/50/75/100% de 246 px: 61.5/123/184.5/246 px. En todas las 48 variantes el texto visible es `25%`, incluso donde el eje dice 50/75/100 y la barra tiene esa anchura. Es una contradicción interna de la fuente, no una regla de producto.

## States

No hay estado interactivo. Type distingue tono contextual, Size escala visual y Percentage controla solo geometría. Ninguna variante representa Hover, Focus o Disabled. Cero reacciones.

## Layout

Ancho fijo 246 px. Small 246×44, Middle 246×51 y Large 246×55; pista y relleno de 4/8/12 px de altura respectivamente. La fila superior contiene Label a la izquierda y Percentage a la derecha; helper debajo. Gap vertical observado de 4 px en Small. Track y relleno tienen radio 999 px; el relleno comienza en x=0. No se infiere responsive ni regla de datos desde estas cajas.

## Visual Styles

Track literal `#F1F5F9` sin binding. Barras: primary `#3255F7` con `color/brand/default`; warning `#C97B00` con `color/feedback/warning/icon`; positive `#098300` con `color/feedback/positive/icon`; danger `#D40000` con `color/feedback/danger/icon`. Son frames de fondo, por lo que los tres roles icon y el brand genérico no cumplen la semántica estricta del destino. Textos Label/Percentage `color/text/primary`, helper `color/text/secondary`.

## Typography

Manrope Regular. Small usa 12 px en Label/Percentage; Middle/Large usan 14 px. Helper usa 12 px en las 48 variantes. En fuente, line-height AUTO y tracking 0%; algunos campos ligan familia, peso y tamaño, pero no se observan bindings completos de interlineado/tracking para todos los textos.

## Tokens

El track no tiene token; no elevar el literal a norma. Los valores de colores de barra coinciden con primitivas existentes en AI Design System, pero la coincidencia no autoriza copiar roles icon a frames. La reconstrucción requiere fondo/track y fondos de avance por tono con scope `FRAME_FILL`, aliasados a primitivas aprobadas; el JSON de destino, no este contrato fuente, gobernará los aliases.

## Content

`Label`, `Optional helper text` y `25%` son ejemplos. La contradicción porcentaje visible/anchura debe resolverse explícitamente antes de construir; no se debe copiar `25%` a las 36 variantes cuyo eje es distinto. No hay fórmula, unidades, locale ni actualización dinámica observados.

## Interactions

`UNDEFINED`: cero prototipos y reacciones. La propiedad Percentage es una variante visual, no un controlador de valor accesible o animado.

## Accessibility

`REQUIRES_DEFINITION`: los textos aportan una pista, pero Figma no define etiqueta programática, valor/rango, lectura por lector de pantalla, manejo de colores ni contraste contextual. La inconsistencia visible impide interpretar confiablemente el porcentaje sin corrección.

## External Dependencies

Ninguna dependencia remota activa en el set. No hay assets externos ni instancias anidadas.

## Unresolved Information

No está definido si Type expresa severidad, progreso objetivo o estado de resultado; no se extrapola semántica funcional. No se sabe si los textos deberían derivar del porcentaje real en producto. La decisión de destino puede sincronizar texto y barra por variante, registrando esa mejora como cambio deliberado.

## Implementation Notes

Conservar 48 variantes, tres alturas, cuatro anchos de relleno y los tres textos/visibilidades editables donde no creen contradicción. Para destino, usar una sola fuente de verdad para Percentage: la variante gobierna texto visible y anchura; evitar que un TEXT libre los desacople. Crear y verificar roles `color/background/progress/*` antes de construir, sin primitiva nueva.

## Evidence / Confidence

**FIGMA_DIRECT:** set, 336 nodos, 48 variantes, 144 textos, doce variables, screenshot y cero reacciones. **DERIVED:** 61.5/246=25%, etc. **CONFLICT interno observado:** texto 25% fijo frente a ejes/anchuras 50/75/100. Confianza `HIGH` para estructura; significado de datos no definido.
