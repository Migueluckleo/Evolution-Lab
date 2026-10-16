---
contract_schema: figma-component-contract/1
contract_id: SRC-FIGMA-NAVIGATION-TAB-001
name: Navigation Tab — observed source
status: SOURCE_INSPECTED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_page_id: "268:20245"
source_set_id: "1183:1146"
source_key: 3fbabad3e0521532b6055ea2e5de2f74de4b2693
read_only: true
last_inspected: 2026-09-24
---

# Navigation · Tab — contrato fuente observado

Esta es evidencia de la [Librería anterior](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1183-1146), no el contrato de construcción de AI Design System. El set tiene 17 variantes y 132 nodos recorridos, 16 nodos ocultos y cuatro reacciones `ON_HOVER → CHANGE_TO`. La captura del set muestra dos filas Base y dos Dynamic; la variante extra `Dynamic / On / Selected` ocupa la misma zona de la muestra que otra variante y no define un eje combinatorio completo.

## Ejes y propiedades observadas

`type={base,dynamic}`, `tab={on,off}` y `state={default,hovered,selected,focused,disabled}`. La matriz no es cartesiana: Base tiene 2×4; Dynamic tiene 2×4 más solo `on/selected`. Hay texto editable `tab text` (`Tab title`), booleanas `show divisor` (true), `show dot` (false), `show right icon` (true) y `show left icon` (true), además de `left icon` y `right icon` como `INSTANCE_SWAP` con 1512 preferencias cada una. En Selected, solo el texto está vinculado a propiedad; su única instancia ImageSquare no tiene referencia de swap ni booleanas. No se deducen 20 variantes de las opciones declaradas.

| Tipo | On | Off | Medidas y anatomía |
|---|---|---|---|
| Base | default, hovered, focused, disabled | default, hovered, focused, disabled | Todas 135×42; dos instancias ImageSquare, texto y Dot oculto. Focus agrega rectángulos de máscara/fondo y subrayado. |
| Dynamic | selected, default, hovered, focused, disabled | default, hovered, focused, disabled | On 135–136×35, Off 133×35; dos ImageSquare, texto, Dot oculto y divisor lineal en las ocho variantes ordinarias. `Selected` tiene un frame `content`, una sola instancia ImageSquare, texto regular y ningún Dot ni divisor. |

## Apariencia observada en el modo mostrado

- Base On: línea inferior, texto e iconos azules `#3255F7`; Hovered usa azul fuerte `#1D21B0`; Focused agrega subrayado de 2 px y efecto exterior azul de 2 px; Disabled usa gris `#94A3B8`.
- Base Off: línea inferior clara `#BFCEFE`, texto/iconos `#0F172A`; Hovered conserva esos RGB; Focused añade fondo blanco, subrayado claro de 1 px y efecto exterior azul de 2 px; Disabled usa gris `#94A3B8`.
- Dynamic On: fondo azul pálido `#EFF3FF` en Default y Selected, `#BFCEFE` en Hovered, blanco bajo máscara Focused con efecto exterior azul de 2 px y gris `#E2E8F0` en Disabled. Texto/iconos azules salvo Selected, que tiene texto/icono primarios, y Disabled, que usa gris.
- Dynamic Off: sin fondo visible por defecto; Hovered muestra contorno claro `#BFCEFE`; Focused usa máscara blanca con efecto exterior azul de 2 px; Disabled atenúa texto e iconos. El divisor claro es visible en las variantes ordinarias.

## Dependencias y bindings

Las variantes ordinarias usan dos instancias ImageSquare de key `f273018f11d7d4e938078bd0b21b0b3a9e7f2634` y una instancia Dot oculta de key `309ba73acbf0853df307a033c09a1a40856357d5`. Selected usa una instancia ImageSquare distinta, key `7e704a5154aa535ff118cc9d6970e0bfce641037`. Los colores de iconos visibles se aplican a los vectores internos; los fills blancos de las instancias ImageSquare están ocultos en la fuente. La tipografía es Manrope 14 px, Regular para Off y Selected, Bold para On ordinario; interlineado Auto y tracking 0 %.

En la fuente se observaron bindings semánticos cruzados: `color/text/disabled` sobre strokes Base Disabled; `color/surface/brand/accent` sobre stroke Base Off Hovered; `color/focus/ring` y `color/border/subtle` como fills de rectángulos de subrayado; y `color/brand/strong` sobre un stroke. Son evidencia visual de origen, no autorizan copiar esas categorías al destino. El contrato destino debe preservar los RGB por modo con roles de borde/fondo adecuados y aliases a primitivas aprobadas.

## Prototipado observado

Solo cuatro variantes Default presentan reacción `ON_HOVER → CHANGE_TO` hacia su Hovered respectiva: Base On, Base Off, Dynamic On y Dynamic Off. No hay evidencia de retorno, clic, cambio de `tab=on/off`, lógica de selección, teclado o ARIA. No se inventan esas reglas.

## Conciliación con el destino

La comparación de modos, los dos roles de borde faltantes y las tres keys de dependencias se resolvieron en el [contrato de construcción](../../specs/navigation-tab.contract.v0.1.0.md) y su [QA técnico](../../qa/implementations/navigation-tab.v0.1.0.figma.review.md). Selected conserva su estructura excepcional y no se fabricaron combinaciones. Este documento sigue siendo evidencia observacional de origen; no sustituye el contrato normativo de destino.
