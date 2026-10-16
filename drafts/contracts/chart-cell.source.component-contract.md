# cell · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, set cell](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2977-2066), página `268:20756`, set `2977:2066`, key `ddc93f484212024c51d2cdddc480ea242a4db18f`.
- **Inspección:** `COMPLETE`, 26/26 nodos, solo lectura; captura de la página Charts y recorrido de las 13 variantes inspeccionados. Es evidencia, no una regla aprobada de visualización de datos.

## Component Identity

**OBSERVED:** set `cell` de 484×392 con 13 componentes de 26×35. Ejes `hasContent` false/true, `position` −/first/middle/last y `segment` −/solo/upper/middle/lower. El default es false/−/−.

## Anatomy

La celda vacía es un componente con borde punteado, sin barra. Cada una de las otras doce contiene un frame `BarCell` de 14×35. No hay textos, vectores ni instancias anidadas.

## Dependencies

Ocho variables únicas: seis locales y dos remotas de spacing. Cero componentes anidados, estilos nombrados y reacciones. Los IDs y scopes están en el YAML. El borde utiliza `color/border/accent`; la barra usa `color/brand/default`, un rol demasiado genérico para un fill de serie en el destino.

## Properties

Tres ejes VARIANT, sin propiedades TEXT, BOOLEAN o INSTANCE_SWAP. `hasContent` controla la presencia real del hijo en los componentes, no una propiedad booleana independiente expuesta. No se observa ajuste de altura de barra como propiedad.

## Variants

Una combinación vacía false/−/− y doce combinaciones true de position first/middle/last × segment solo/upper/middle/lower. Todas 26×35. Las variantes se disponen en una fila vacía y tres filas de cuatro segmentos. No materializar el cartesiano completo de 2×4×5.

## States

`position` describe ubicación horizontal y `segment` el redondeo vertical de la barra, no estados de interacción. `hasContent=false` representa ausencia de barra. Cero reacciones.

## Layout

**OBSERVED:** auto layout horizontal, 26×35, gap 4. Barra 14×35. Padding horizontal first/empty 8 izquierda y 4 derecha; middle 6/6; last 4 izquierda y 8 derecha. Padding vertical cero, ligado a variable remota. Borde interior punteado con patrón 2/2 y color azul pálido. Los 13 componentes incluyen stroke; doce incluyen fill de barra.

## Visual Styles

Barra azul `#3255F7` ligada a `color/brand/default`; borde `#BFCEFE` ligado a `color/border/accent`. Segment=solo redondea cuatro esquinas a 4 px; upper solo las superiores; lower solo las inferiores; middle ninguna. Las esquinas sin radio usan `radius/none`. No hay sombra ni efectos. El esquema es monocromático y no demuestra una escala de valores cuantitativos.

## Typography

No hay texto en las 13 variantes.

## Tokens

Ocho referencias únicas, incluyendo `spacing/xs`, `spacing/sm`, `radius/sm`, `radius/none`, `color/border/accent`, `color/brand/default` y dos remotas de spacing. El [YAML sincronizado](chart-cell.source.component-contract.yaml) conserva IDs y scopes. El rol de barra debe mapearse por función de fondo/serie y no por igualdad RGB.

## Content

No hay cadenas. La celda es una pieza visual de gráfico; no declara datos, eje, unidades ni valor numérico.

## Interactions

`UNDEFINED`: cero reacciones; no se infiere selección, hover, tooltip ni animación.

## Accessibility

`REQUIRES_DEFINITION`: una barra sin etiqueta ni valor no es accesible por sí sola; el consumidor de gráfico debe aportar alternativa textual y significado de series. No se certifica contraste ni semántica de datos desde este set aislado.

## External Dependencies

Dos variables remotas de spacing; biblioteca y versión `NOT_EXPOSED_BY_FIGMA_MCP`. No hay componentes externos activos.

## Unresolved Information

La relación de `segment` con datos apilados o borde por contexto no está definida. El cero remoto puede reemplazarse por token local solo con decisión de destino. No hay token de serie explícito en fuente: `color/brand/default` admite scope amplio, pero su uso en barra no cumple la regla semántica estricta del destino.

## Implementation Notes

Conservar 13 combinaciones, contorno punteado y radios por segmento. No inventar las 27 combinaciones cartesianas ausentes ni replicar un rol de marca genérico como fill de datos. Identificar token semántico `background/chart/...` con alias a primitiva existente antes de construir.

## Evidence / Confidence

**FIGMA_DIRECT:** metadata, screenshot, 26 nodos, 13 strokes, 12 fills de barra, ocho variables y cero reacciones. **DERIVED:** función de celda apilada por `segment`. **REQUIRES_DEFINITION:** significado de datos y accesibilidad. Confianza `HIGH` para estructura observada.
