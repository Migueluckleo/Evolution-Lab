# Header (Charts) · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, componente Header](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3075-764), página `268:20756`, componente suelto `3075:764`, key `e322384d309997e64a5446a93ad07fd3560f7cf4`.
- **Inspección:** `COMPLETE`, 17/17 nodos, solo lectura, incluidos descendientes de tres instancias `labelCell`; captura de página Charts inspeccionada. Es evidencia fuente.

## Component Identity

**OBSERVED:** `Header` es un COMPONENT único de 638×47, no un set ni una variante. Está dentro de la página Chart; su nombre genérico no justifica agruparlo con headers de navegación de otras páginas.

## Anatomy

Auto layout horizontal: frame `Legend` 412×47 (Title y Description apilados) + frame `Indicators` 202×16 con tres instancias locales `labelCell` que muestran Value 1/2/3.

## Dependencies

Tres instancias `labelCell`, variante Regular/sm y main key `28c769fbd86a940b2b097d9267f926e9b2736116`. Las tres mantienen `spotVisible=true` y sobrescriben texto y fill de swatch. Doce variables únicas (11 locales/una remota), cero estilos nombrados y reacciones. El contrato de `labelCell` documenta la dependencia base.

## Properties

`Ttile` TEXT default `Title chart` (error tipográfico en la propiedad fuente), `Description` TEXT default `Description`, `valuesVisible` BOOLEAN true para Indicators y `descriptionVisible` BOOLEAN true para Description. Los tres textos Value 1/2/3 son overrides de instancias internas, no propiedades de texto expuestas por Header.

## Variants

No hay eje de variante: un único componente 638×47.

## States

Los dos BOOLEAN controlan visibilidad, no interacción. No hay Hover/Disabled ni reacciones.

## Layout

**OBSERVED:** Header horizontal con gap 24; Legend vertical con gap 8; Indicators horizontal, tres instancias de anchura 66/68/68 px. Title 247×20, Description 412×19; Indicators se alinea al borde inferior del Header. El componente no recorta contenido.

## Visual Styles

Title, Description y tres etiquetas usan `color/text/primary` (`TEXT_FILL`). Swatches de las tres instancias: Value 1 `#1D21B0` con `color/brand/strong`; Value 2 `#BFCEFE` con `color/brand/accent`; Value 3 `#3255F7` con `color/interactive/primary/default`. Son shapes de leyenda, no fondos interactivos; sus roles genéricos/interactive no deben copiarse al destino por RGB.

## Typography

Title Manrope Regular 20 px, line-height 20, tracking 0.1% literal; `font/family/base` y `font/size/lg` enlazados. Description Manrope Regular 12 px, line-height 20, tracking 0.1%; solo tamaño `font/size/xs` enlazado. Los tres textos de instancias son Manrope Regular 12 px, line-height 16, tracking 0%, con tamaño xs enlazado. No hay binding de peso, tracking ni line-height visible en los textos del Header fuente.

## Tokens

Doce IDs, nombres, scopes y consumidores en el [YAML sincronizado](chart-header.source.component-contract.yaml). Una variable de spacing cero es remota; las demás son locales. El destino debe distinguir serie 1/2/3 con roles chart/swatch de `SHAPE_FILL`, no usar interactive/background para esas formas.

## Content

`Title chart`, `Description` y Value 1/2/3 son muestras. Solo Title/Description se editan a nivel Header; los valores se pueden cambiar dentro de las instancias `labelCell` pero no se exponen como propiedades del padre fuente.

## Interactions

`UNDEFINED`: cero reacciones. Visibilidad no implica comportamiento.

## Accessibility

`REQUIRES_DEFINITION`: los swatches requieren asociación semántica con etiquetas y una alternativa que no dependa del color. No se definen niveles de encabezado, lectura de gráfico ni teclado.

## External Dependencies

`labelCell` es local al archivo fuente; la variable de spacing cero remota carece de biblioteca/versiones expuestas.

## Unresolved Information

No se conoce significado ni orden de series ni si pueden ser menos/más de tres. El nombre de propiedad `Ttile` es errata fuente. El destino puede corregirlo a `Title` y añadir propiedades de texto padre para Value 1/2/3, pero debe documentar la mejora.

## Implementation Notes

Reconstruir `labelCell` primero y usar tres instancias locales. Nombrar destino `Chart Header` para distinguirlo de navegación, preservando el mapeo a `Header` fuente. Resolver swatches con tokens chart semánticos de scope correcto y registrar la corrección de `Ttile`.

## Evidence / Confidence

**FIGMA_DIRECT:** componente 638×47, 17 nodos, tres instancias, cinco textos, doce variables, cero reacciones. **DERIVED:** rol de encabezado de gráfico. **REQUIRES_DEFINITION:** series y accesibilidad. Confianza `HIGH` para estructura observada.
