---
contract_schema: figma-component-contract/0.1.0
status: OBSERVED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node_id: "1221:28710"
read_only: true
---

# Checkbox · contrato técnico de la fuente

Este documento y su [YAML sincronizado](checkbox.source.component-contract.yaml) describen evidencia de la Librería anterior. No autorizan diseño nuevo, comportamiento web ni equivalencia automática de tokens con AI Design System.

## Identidad y propósito observado

- [Set `checkbox`](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1221-28710), ID `1221:28710`, key `7cd9c016ecf140eef806b29fb23de1d00a718471`, página `1144:34368` (`❖ Checkbox  ✅`). Es un `COMPONENT_SET` 680×290 con 12 componentes 24×24. No tiene Description ni Documentation Link.
- **FIGMA_DIRECT:** la nota de página indica que un checkbox permite seleccionar una o más opciones dentro de un grupo, muestra selected, unselected e indeterminate y debe acompañarse de una etiqueta clara. La nota no define interacciones ni semántica técnica de aplicación.
- **DERIVED:** traversal read-only 86 nodos, incluidas 24 etiquetas invisibles y nueve instancias; 12 variantes, 19 variables usadas al incluir iconos anidados y padding del set, un estilo nombrado, cero reacciones. Captura del set 680×290 inspeccionada.

## Propiedades y variantes

| Propiedad fuente | Tipo | Default | Valores / evidencia |
|---|---|---|---|
| `type` | VARIANT | `selected` | `selected`, `indeterminate`, `unselected` |
| `state` | VARIANT | `enabled` | `enabled`, `hover`, `focus`, `disabled` |
| `show left field label#20125:0` | BOOLEAN | false | visibilidad de 12 textos izquierdos |
| `show right field label#102635:0` | BOOLEAN | false | visibilidad de 12 textos derechos |

La matriz 3×4 está completa. No hay propiedad TEXT para cambiar `Field Label`, ni estados Press/Error/Loading observados. `selected` no debe confundirse con `enabled`; `disabled` no equivale a `unselected`.

| Type | Enabled | Hover | Focus | Disabled |
|---|---|---|---|---|
| selected | `1225:28848` | `1221:28721` | `1225:28921` | `1225:28937` |
| indeterminate | `1225:28856` | `1225:28881` | `1225:28897` | `1225:28913` |
| unselected | `1221:28820` | `1225:28950` | `1221:28809` | `1221:28825` |

## Anatomía y layout

Cada variante es auto layout horizontal, HUG 24×24 cuando sus dos etiquetas están ocultas, gap 8 y padding 0. Orden directo: etiqueta izquierda `TEXT` invisible 68×18, `Content` 24×24, etiqueta derecha `TEXT` invisible 68×18. Excepción estructural: Unselected/Focus usa una instancia local `checkbox` `1144:34470` en vez de `Content` directo. El set coloca variantes en cuadrícula 3 filas × 4 columnas.

En Selected e Indeterminate, el indicador es un rectángulo 18×18 en (3,3), esquinas 4, fill cromático y un icono Phosphor `Check` o `Minus` de 12×12 con vector blanco. El Check visible mide 9.17×6.56 dentro del icono; Minus mide 9×0.75. Unselected usa un rectángulo 18×18 de esquinas 4, sin fill visible y stroke de 2 px. Focus añade estilo `focus/outset` al rectángulo: dos `DROP_SHADOW` sin blur ni offset, spreads 4 y 2, colores #1d21b0 y #f8fafc; Unselected/Focus tiene stroke `OUTSIDE`, los demás strokes `INSIDE`.

Las etiquetas son Manrope Regular 14, interlineado 18, texto de ejemplo `Field Label`; están ocultas por defecto. Su font family y font size tienen bindings; weight e interlineado no. Los estados Disabled ligan el texto a `color/text/disabled`.

## Colores y dependencias observados

| Type/State | Indicador principal | Icono/contorno |
|---|---|---|
| selected o indeterminate / enabled, focus | `color/interactive/primary/default` #3255f7 | `color/icon/on-brand` blanco |
| selected o indeterminate / hover | `color/interactive/primary/hover` #1d21b0 | icono blanco |
| selected o indeterminate / disabled | `color/background/disabled` #e2e8f0 | icono blanco |
| unselected / enabled, focus | sin fill | `color/border/default` #94a3b8 |
| unselected / hover | sin fill | `color/border/hover` #1d21b0 |
| unselected / disabled | sin fill | `color/border/disabled` #e2e8f0 |

Hay 14 variables locales usadas (colores, familia/tamaño y padding del set) y cinco remotas de geometría (`radius/md`, `radius/sm`, `stroke/stroke-focus`, `icons/xxxsm-icon-size`, `spacing/md`). Se conservan referencias e IDs en YAML. El set usa `spacing/6xl` y `spacing/2xl` para padding de presentación; esos bindings tienen scope `GAP` en origen y no son una instrucción para replicar ese scope en el destino.

Dependencias de componente activas: ocho instancias de iconos —cuatro `Check` Outline/Light key `b0e1ef9e3dcc90870bbf7ef05b8ee937890eb31d`, cuatro `Minus` Outline/Regular key `10ad6c579ecb00c883f839281ca2ad812962a324`— más una instancia local `checkbox` State=focus key `0d420b76c03affe6d10c7c83ce37a57f615bb29d` en Unselected/Focus. El estilo nombrado `focus/outset`, key `db4f7e95726995e57ca781fbe41ec23bcab72a1e`, aparece en los tres focos. Las definiciones principales se resolvieron en el archivo; no se hizo inventario completo de todas sus variantes alternativas.

## Interacciones, accesibilidad y límites

No hay reacciones observadas en el set ni en sus 12 variantes. La nota de uso y el texto visible son evidencia de intención, no prueba de agrupación funcional, teclado, rol `checkbox`, nombre accesible, hit target ni WCAG. La captura no prueba estados dinámicos ni responsive. Las etiquetas ocultas significan que la instancia visual sin configuración no presenta texto visible. Un contrato de comportamiento posterior debe definir selección, indeterminate, grupo, foco real y accesibilidad de producto.

## Evidencia y trazabilidad

- `E001` `node:1221:28710`: identidad, set, propiedades, dimensiones y cuadrícula.
- `E002` `component:12 variants`: IDs, ejes, tres hijos directos, auto layout, labels ocultas y cero reacciones.
- `E003` `descendants`: rectángulos, iconos, vectores, fills, strokes, efectos y geometría.
- `E004` `main components`: Check, Minus y helper checkbox local, keys y conteos.
- `E005` `variables/styles`: 19 variables usadas y estilo focus/outset resueltos por ID.
- `E006` `page:2433:227`: nota de uso; captura 680×290 del set.

**REQUIRES_DEFINITION:** comportamiento funcional, contenido real de etiquetas, reglas de agrupación y accesibilidad. No se normaliza ni rediseña la fuente en este contrato.
