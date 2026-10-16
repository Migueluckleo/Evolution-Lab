# labelCell · contrato de evidencia fuente

- **Origen:** [Libreria v1.1.0, set labelCell](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=3086-992), página `268:20756`, set `3086:992`, key `b5deacd96d67b6a46805de3d5abc20cc2717a4ea`.
- **Inspección:** `COMPLETE`, 17/17 nodos, solo lectura. La página Charts y el set se inspeccionaron visualmente; esta evidencia no aprueba todavía su reconstrucción.

## Component Identity

**OBSERVED:** `labelCell` es un set reutilizable 193×92 con cuatro variantes `Font weight` Regular/Semi-bold × `Font Size` sm/lg. Cada variante mide 76×16; el nombre `lg` corresponde a 16 px en este set, no a 20 px.

## Anatomy

**OBSERVED:** variante → frame `Dot` 16×16 con shape 16×10 → texto `000`. `Dot` se puede ocultar mediante BOOLEAN. No hay iconos ni instancias dentro de la definición.

## Dependencies

Cinco variables únicas: cuatro locales (`spacing/xs`, `radius/sm`, `color/text/primary`, `font/size/xs`) y una remota (`Spacing/Small/spacing-sm-0`); cero componentes anidados, estilos nombrados o reacciones. La dependencia remota solo da padding cero. El shape gris no tiene variable de color.

## Properties

`Text` TEXT default `000` enlaza los cuatro textos; `spotVisible` BOOLEAN true enlaza los cuatro frames Dot. Ejes `Font weight` default Regular y `Font Size` default sm. No hay propiedad de color de swatch ni de tamaño físico del Dot.

## Variants

| Variante | ID | Texto | Peso |
|---|---|---:|---|
| Regular/sm | `3015:2309` | 12 px | Manrope Regular |
| Semi-bold/sm | `3086:993` | 12 px | Manrope SemiBold |
| Semi-bold/lg | `3086:1001` | 16 px | Manrope SemiBold |
| Regular/lg | `3086:1013` | 16 px | Manrope Regular |

## States

No hay estado interactivo; `spotVisible` solo controla visibilidad. Cero reacciones observadas.

## Layout

**OBSERVED:** auto layout horizontal, 76×16, gap 4, padding horizontal 4, sin padding vertical. Dot 16×16 contiene un rectángulo 16×10 centrado verticalmente. Los textos usan cajas entre 22 y 31 px de ancho, altura 16 px. El set coloca dos columnas y dos filas.

## Visual Styles

Los cuatro textos usan `color/text/primary` (TEXT_FILL). Los cuatro shapes usan el literal gris `#D9D9D9` sin binding; los frames Dot carecen de fill. No se debe aceptar ese literal como token aprobado del destino ni usar un rol text/icon en el swatch de gráfico.

## Typography

Manrope Regular/SemiBold, tamaño 12 px en sm y 16 px en lg, line-height 16 px y tracking 0%. Solo los dos textos sm enlazan explícitamente `font/size/xs`; los dos lg tienen 16 px literales. No hay bindings de familia, peso, line-height o tracking observados en esos cuatro textos.

## Tokens

Los cinco IDs, scopes y consumidores se detallan en el [YAML sincronizado](chart-label-cell.source.component-contract.yaml). Igualdad numérica del padding cero remoto con un token local no demuestra identidad semántica.

## Content

`000` es texto de ejemplo editable; en instancias de Header y Progress chart item se sobrescribe por etiquetas/porcentajes/valores. No hay definición de formato o significado.

## Interactions

`UNDEFINED`: no hay prototipos ni reacciones.

## Accessibility

`REQUIRES_DEFINITION`: la relación entre color de swatch y etiqueta no tiene semántica accesible definida; no se certifica lectura de leyenda ni contraste.

## External Dependencies

Una variable de spacing remoto; su biblioteca y versión son `NOT_EXPOSED_BY_FIGMA_MCP`. No hay componente remoto activo en la definición.

## Unresolved Information

El origen no explica cómo elegir el color de una serie o si el swatch se oculta por significado. Los overrides de instancias no crean nuevas variantes fuente. El gris literal y el binding faltante del tamaño lg se deben resolver semánticamente en destino.

## Implementation Notes

Es una dependencia local para `Header` y `Progress chart item`; debe reconstruirse antes que ambos. No copiar el literal gris ni el ID de la variable remota. Preservar propiedades Text/spotVisible y cuatro combinaciones observadas.

## Evidence / Confidence

**FIGMA_DIRECT:** metadata, screenshot de página, traversal completo 17 nodos, propiedades, paints y tipografía. **DERIVED:** función de swatch+etiqueta. **REQUIRES_DEFINITION:** significado y accesibilidad del color. Confianza `HIGH` para estructura; comportamiento no definido.
