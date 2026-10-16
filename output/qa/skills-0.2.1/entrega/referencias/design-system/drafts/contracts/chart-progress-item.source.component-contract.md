# Progress chart item · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, set Progress chart item](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3075-871), página `268:20756`, set `3075:871`, key `e0f0518afea25fa255f066c83708099842d1ccc7`.
- **Inspección:** `COMPLETE`, 40/40 nodos, solo lectura, incluyendo descendientes de seis instancias `labelCell`; captura de la página Charts inspeccionada. Evidencia fuente, no especificación de datos.

## Component Identity

**OBSERVED:** set 678×265 con dos variantes: `Top progress item` 639×30 y `Progress item` 639×104. El eje se llama `Property 1` y el default es `Top progress item`.

## Anatomy

Top: Header con Label y Value → Bar 639×8 con rectángulo Progress 580×8. Progress item: Header con Label/Value → Body 639×72 con Bar 639×24, Progress 247×24 y dos filas de Legend. Cada fila de Legend contiene tres instancias `labelCell` (texto de serie, porcentaje, cantidad).

## Dependencies

Seis instancias activas de `labelCell`, variante Regular/sm, main key `28c769fbd86a940b2b097d9267f926e9b2736116`. Cuatro propiedades de las instancias muestran `Progress`, `80%` o `80k`, con spotVisible true solo en la primera instancia de cada fila. Los swatches de estas instancias tienen overrides de fill azul o pálido; cuatro paints están dentro de Dot ocultos por `spotVisible=false` y no son visualmente efectivos. 17 variables únicas (16 locales/una remota), cero estilos nombrados y cero reacciones; detalle en YAML.

## Properties

`Label` TEXT default `Text example` y `Value` TEXT default `$100k` enlazan los dos encabezados. `Property 1` VARIANT elige Top progress item/Progress item. No se expone porcentaje o anchura de Progress como propiedad; el relleno 580/639 y 247/639 es geometría fija de ejemplo.

## Variants

| Variante | ID | Caja | Contenido |
|---|---|---:|---|
| Top progress item | `3075:684` | 639×30 | header + barra de 8 px |
| Progress item | `3075:872` | 639×104 | header + barra de 24 px + dos leyendas |

## States

No hay Hover, Disabled ni estado de ejecución. El eje `Property 1` cambia anatomía, no interacción. Cero reacciones.

## Layout

Top usa auto layout vertical con gap 6; Header horizontal 639×16 y Bar 639×8. Progress item usa gap 16; Body 639×72 con gap 8; Bar 639×24 y dos filas de Legend de 639×16. Las instancias `labelCell` se ensanchan a 213×16 por distribución de tres columnas.

## Visual Styles

Texto `color/text/primary`; track azul grisáceo `#E2E8F0` con `color/background/muted`; relleno azul `#3255F7` ligado en fuente a `color/icon/brand` (rectángulo, categoría incorrecta para destino). El primer swatch de leyenda usa `color/brand/default` y el segundo `color/brand/subtle`, no roles de serie. Radios 4 px o cero según tramo. No hay sombra.

## Typography

Manrope Regular 12 px, line-height 16 px en Label y Value directos; `font/family/base`, `font/size/xs` y `font/line-height/xs` enlazados. Value tiene tracking 0.1% literal, Label 0%. Los seis textos internos de `labelCell` también son 12 px por la variante anidada, con las limitaciones de binding ya documentadas en su contrato.

## Tokens

17 IDs de variables y scopes en el [YAML sincronizado](chart-progress-item.source.component-contract.yaml). El destino necesita roles semánticos de superficie de barra/serie y de swatch; no copiar `color/icon/brand` a un rectángulo de progreso ni `color/brand/default` por mera coincidencia visual.

## Content

`Text example`, `$100k`, `Progress`, `80%` y `80k` son muestras. El ancho de barra equivale aproximadamente a 91% en Top y 39% en Progress item, sin correspondencia documentada con las etiquetas `80%`. No inferir un cálculo ni corregir silenciosamente esa contradicción de muestra.

## Interactions

`UNDEFINED`: cero reacciones. No se observan tooltip, hover, loading ni actualización automática.

## Accessibility

`REQUIRES_DEFINITION`: porcentaje/valor, nombre de métrica, unidades y leyenda necesitan representación accesible. El color no basta para distinguir series. No se certifica semántica o contraste desde Figma fuente.

## External Dependencies

Las seis instancias de `labelCell` pertenecen al mismo archivo fuente; la variable remota de spacing cero no expone biblioteca/versiones. Las claves de componentes fuente no se reutilizan como IDs de destino.

## Unresolved Information

Las barras fijas no concuerdan con los ejemplos `80%`; el comportamiento de datos no está definido. El origen usa rol iconográfico en fill de progreso y roles de marca genéricos en swatches. El destino debe documentar cómo preserva apariencia sin adoptar categorías incorrectas.

## Implementation Notes

Reconstruir `labelCell` antes de este set y usar instancias locales reales; conservar dos variantes, dos filas de leyenda y los ejemplos visibles como muestras, sin afirmar que representen porcentajes calculados.

## Evidence / Confidence

**FIGMA_DIRECT:** 40 nodos, dos variantes, seis instancias, diez textos visibles, 17 variables y cero reacciones. **DERIVED:** proporciones geométricas de las barras. **REQUIRES_DEFINITION:** datos, actualización y accesibilidad. Confianza `HIGH` para estructura; contenido de muestra inconsistente.
