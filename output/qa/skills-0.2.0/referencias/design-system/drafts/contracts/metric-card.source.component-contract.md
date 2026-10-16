# Card/Metric · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, set Card/Metric](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=587-2751), página `258:130806`, set `587:2751`, key `9d7e8dc9398238b70936d1eeb37ef4651116a42d`.
- **Inspección:** `COMPLETE`, solo lectura, 119/119 nodos; metadata, captura del set y recorrido estructural verificados. Es evidencia del origen, no una especificación aprobada de producto.

## Component Identity

**OBSERVED:** set reutilizable `Card/Metric` de 806×935 con ocho variantes. Los ejes son `type` (Vertical Metric, Horizontal Metric, One Metric V1, One Metric V2) y `size` (Large, Small). Las ocho combinaciones están materializadas.

## Anatomy

**DERIVED:** las variantes Vertical y Horizontal comparten Header (icono monetario, título, botón de navegación, descripción) y Content (dos pares etiqueta/importe). Las dos One Metric presentan un importe y variación porcentual; V1 coloca el icono junto al contenido y V2 lo sitúa en una baldosa propia con borde de tarjeta. Los 24 vectores internos de iconos se cuentan, pero se omiten del árbol funcional.

## Dependencies

**OBSERVED:** 16 instancias de dos componentes remotos: ocho `CurrencyCircleDollar` (key `441865351ce8a0390c7544fee2348dd8ae895f51`, Format=Stroke/Weight=Fill) y ocho `ArrowUpRight` (key `8f20fac8635901c6627e086c16fdf197d5134b7f`, Format=Outline/Weight=Regular). No hay dependencias locales de componentes ni estilos nombrados aplicados. Se observaron 31 variables únicas, todas locales en el archivo de origen; sus IDs y scopes están en el YAML.

## Properties

**OBSERVED:** `show icon` BOOLEAN true enlaza la visibilidad de CurrencyCircleDollar; `show button` BOOLEAN true enlaza Navigate; `show detail visible` BOOLEAN true enlaza Description o el porcentaje; `title` TEXT default `Title` enlaza el título; `detail text` TEXT default `Description` enlaza solo la descripción de las variantes de dos importes; `icon` INSTANCE_SWAP apunta al icono monetario con preferred values vacío. Las etiquetas, importes y porcentajes no exponen propiedades de texto editables en el set fuente.

## Variants

| Tipo | Tamaño | ID | Caja |
|---|---|---|---:|
| Vertical Metric | Large | `587:2747` | 289×256 |
| Vertical Metric | Small | `2838:2255` | 200×216 |
| Horizontal Metric | Large | `587:2748` | 311×192 |
| Horizontal Metric | Small | `2847:243` | 232×160 |
| One Metric V1 | Large | `587:2749` | 337×151 |
| One Metric V1 | Small | `2847:258` | 257×111 |
| One Metric V2 | Large | `587:2750` | 397×144 |
| One Metric V2 | Small | `2847:266` | 313×112 |

## States

No hay eje State, estados Hover/Disabled ni reacciones observadas. `type` y `size` describen estructura y escala, no interacción.

## Layout

**OBSERVED:** Vertical/Horizontal son tarjetas auto layout vertical con padding 24 Large / 16 Small, gap principal 16 y radius 16. Vertical apila dos métricas; Horizontal las dispone en una fila. V1/V2 usan auto layout horizontal con el mismo padding/radius. La baldosa de icono V2 mide 96×96 Large / 80×80 Small y contiene icono de 64 / 48 px. Navigate mide 32 / 24 px; su icono ArrowUpRight mide 24 / 16 px.

## Visual Styles

**OBSERVED:** Vertical, Horizontal y V1 usan `color/background/subtle` como fondo. V2 usa borde `color/border/subtle` y baldosa `color/background/subtle`. Navigate usa `color/background/default` en Vertical/Horizontal/V1 y `color/background/subtle` en V2. Iconos visibles: `color/icon/brand`; títulos e importes: `color/text/primary`; descripciones: `color/text/secondary`; porcentajes: `color/text/brand`. Los seis fills blancos ocultos en wrappers de iconos no son pinturas visibles. Se contaron 70 pinturas visibles y seis ocultas en las variantes.

## Typography

**OBSERVED:** Manrope Regular. Títulos Large 24 px; Small 16 px salvo One Metric V1 Small de 18 px. Importes Vertical Large/Small 32/24 px, Horizontal Large/Small 24/20 px y One Metric Large/Small 32/24 px. Las etiquetas de dos métricas Large 16 px / Small 14 px. Descripciones Large 14 px / Small 12 px. Porcentajes Large 16 px / Small 14 px. La fuente mezcla tokens semánticos y primitivos de font-size/line-height; hay medidas fuente inconsistentes entre cajas de texto y line-height, que no se reinterpretan como intención de producto.

## Tokens

**OBSERVED:** 31 variables locales: siete de color, 11 tipográficas, cinco de tamaño, cinco de espacio, dos de radio y una de stroke. Los IDs, nombres, scopes y recuentos de uso exactos se registran en el [YAML sincronizado](metric-card.source.component-contract.yaml). Igualdad de color entre roles no implica equivalencia semántica. Los IDs fuente no se reutilizan en AI Design System.

## Content

**OBSERVED:** `Title`, `Description`, `Amount 1`, `Amount 2`, `$123,456.00`, `$123,320.00` y `+5.2%` son ejemplos. No hay formato numérico, localización, cálculo de tendencia ni reglas de truncamiento explícitos.

## Interactions

`UNDEFINED`: Navigate parece un control de acción por su nombre y representación, pero las ocho variantes tienen cero reacciones. No se inventa su destino ni comportamiento.

## Accessibility

`REQUIRES_DEFINITION`: no se expone nombre accesible, semántica del botón, foco, teclado, anuncio de métricas ni actualización en vivo. La verificación de contraste del destino es una tarea separada; este documento no certifica WCAG.

## External Dependencies

CurrencyCircleDollar y ArrowUpRight son remotos. La biblioteca, URL y versión de publicación externas son `NOT_EXPOSED_BY_FIGMA_MCP`.

## Unresolved Information

Faltan reglas de interacción, semántica de las cifras y contenido editable para etiquetas/importes. El título de 18 px de V1 Small no tiene equivalente semántico confirmado en destino. El porcentaje `color/text/brand` necesita revisión modal de contraste antes de construir.

## Implementation Notes

Conservar estructura y apariencia en lo posible, pero no copiar bindings solo por RGB. Cualquier rol semántico nuevo debe tener scope correcto, alias a primitiva existente y trazabilidad simultánea en JSON, Figma y contrato destino. La fuente permanece inalterada.

## Evidence / Confidence

**FIGMA_DIRECT:** metadata, screenshot, properties del set y recorrido completo de 119 nodos, 16 instancias, 36 textos, 31 variables, cero reacciones. **DERIVED:** anatomía por familia y recuentos. **REQUIRES_DEFINITION:** conducta y accesibilidad. Confianza `HIGH` para estructura observada; identidad de biblioteca remota no expuesta.
