# Breadcrumb item · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, set Breadcrumb item](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2425-35897), página `1098:28190`, set `2425:35897`, key `e96a86bbd1d613d821281d737f2cdc262791cbe6`.
- **Inspección:** `COMPLETE`, solo lectura, 22/22 nodos; captura de la página de origen 1242×1106 verificada. Este documento describe evidencia de Figma, no comportamiento implementado ni especificación aprobada de producto.

## Component Identity

**Observed from Figma:** set reutilizable `Breadcrumb item` de 162×438, sin descripción propia, con seis componentes. Definiciones: `text` TEXT default `Breadcrumb`; `State` VARIANT default `default`, opciones default/shorten/disabled/hover/icon; `active` VARIANT default `off`, opciones off/on. Solo seis combinaciones están materializadas; el producto cartesiano de diez no lo está.

## Anatomy

**Derived structure:** `Breadcrumb item` → ítem textual o iconográfico → opcional CaretRight. La variante Icon usa House y CaretRight. La variante Active no tiene caret. Los vectores internos se omiten del árbol funcional, pero se contaron como cinco nodos.

## Dependencies

**Observed from Figma:** cinco instancias de iconos: cuatro CaretRight de key `e2fc671298e81c590f5a4a5272d9c97709515666` y una House de key `aac149e12fc8ed2da22bd95d2cef764a2b407ad7`; ambas dependencias remotas activas con formato Outline/Light. Las bibliotecas externas y sus versiones no se exponen. 16 variables únicas usadas: 14 locales y dos remotas; cero estilos nombrados usados.

## Properties

**Observed from Figma:** `text` es editable en la definición del set; `State` y `active` son ejes de variante. No se observó propiedad de ocultar el separador ni intercambio de icono expuesto en el set padre.

## Variants

| Combinación observada | ID | Caja | Contenido visible |
|---|---|---:|---|
| default/off | `2425:35898` | 116×24 | Breadcrumb + CaretRight 24 |
| icon/off | `2425:35901` | 44×20 | House 20 + CaretRight 20 |
| shorten/off | `2425:35904` | 42×24 | `...` + CaretRight 24 |
| disabled/off | `2425:35907` | 112×24 | Breadcrumb + CaretRight 20 |
| default/on | `2425:35910` | 88×24 | Breadcrumb, sin caret |
| hover/off | `2425:35912` | 88×24 | Breadcrumb, sin caret |

## States

**Observed from Figma:** Default, Shorten, Disabled, Hover e Icon son valores de `State`; Active es eje separado. `hover/off` no muestra caret en la fuente, aunque `default/off` sí. No se observan reacciones.

## Layout

**Observed from Figma:** las seis variantes usan auto layout horizontal y gap 4 ligado a una variable remota. Sin padding. Las cajas de texto son 88×24 salvo Shorten 14×24. Los iconos tienen 20 o 24 px según la fila. Las posiciones en el set forman una columna de seis muestras.

## Visual Styles

**Observed from Figma:** sin fill ni stroke de cuerpo. Texto default/shorten `color/text/tertiary`; disabled `color/text/disabled`; active `color/text/brand`; hover `color/text/brand/strong`. Caret default/icon/shorten `color/icon/secondary`, disabled `color/icon/tertiary`; House `color/icon/brand`. Los paints blancos de wrapper de icono están ocultos. Son roles de texto para texto y de icono para vectores visibles.

## Typography

**Observed from Figma:** cinco textos Manrope 16 px y line-height 150%, letter-spacing −2%; Default/Disabled/Active/Hover Regular, Shorten SemiBold. El texto fuente carece de binding local explícito para line-height/letter-spacing. `font/size/16` y `size/lg` aparecen como referencias distintas al mismo tamaño resuelto en diferentes variantes; no se consideran equivalentes semánticos.

## Tokens

**Observed from Figma:** las 16 variables y sus IDs/consumidores están en el [YAML sincronizado](breadcrumb-item.source.component-contract.yaml). Tokens locales de color y tipografía, más dos variables remotas de spacing/size. Los IDs fuente no son IDs del destino.

## Content

**Observed from Figma:** `Breadcrumb` y `...` son textos de ejemplo. Solo `text` es una propiedad editable; no hay regla observada para truncamiento real o generación de rutas.

## Interactions

`UNDEFINED`: cero reacciones en los seis componentes. Los estados visuales no prueban navegación ni clic.

## Accessibility

`REQUIRES_DEFINITION`: hay texto visible, iconos y dimensiones, pero Figma no define semántica de navegación, nombres accesibles, foco de teclado ni objetivo táctil. Tampoco se ha hecho una certificación WCAG.

## External Dependencies

House y CaretRight son remotos; el origen de biblioteca, URL externa y versión quedan `NOT_EXPOSED_BY_FIGMA_MCP`.

## Unresolved Information

La intención de diez combinaciones teóricas, rutas dinámicas, acortamiento y navegación requiere definición de producto. No se inventan las cuatro combinaciones ausentes.

## Implementation Notes

La composición `Breadcrumbs` reutiliza este set y se documenta por separado. La reconstrucción debe mapear tokens por identidad semántica, no copiar IDs del archivo fuente ni concluir que Hover puede mantener el caret.

## Evidence / Confidence

**FIGMA_DIRECT:** metadata, screenshot y traversal Plugin API de 22 nodos, cinco instancias y 16 variables. **DERIVED:** agrupación de seis combinaciones y anatomía funcional. **REQUIRES_DEFINITION:** comportamiento, semántica y reglas de truncamiento. Confianza `HIGH` para estructura observada; bibliotecas externas no expuestas.
