# Descubrimiento de fuente · Header · 0.1.0

> Cierre2026-10-01: este descubrimiento histórico fue completado por [HEADER-001](../../specs/header.contract.v0.1.0.md) y [QA de implementación](../../qa/implementations/header.v0.1.0.figma.review.md). Header y su Slot existen en destino; los cuatro artworks locales necesarios fueron verificados. Los «próximos gates» inferiores describen el corte histórico, no pendientes activos.

> Nota de conciliación 2026-10-01: el contenido inferior conserva la observación histórica del 24/09. Después se copiaron seis sets locales de Logos; no interpretar «no hay página ni componente Logos» como situación actual. Su equivalencia con la dependencia específica de Header aún requiere verificación. La cola vigente está en [trazabilidad](../../specs/MIGRATION-TRACEABILITY-STATUS.md); no se realizó nueva inspección Figma en esta conciliación.

**Estado:** `SOURCE_INSPECTION_IN_PROGRESS`; **fecha:** 2026-09-24. Evidencia read-only, no contrato listo ni autorización implícita de publicar. Aplica [MIGRATION-TOKEN-TRACEABILITY-001](../../specs/MIGRATION-TOKEN-TRACEABILITY.contract.md).

## Identidad y estructura observadas

- Página fuente `❖ Header ✅` `268:20243`. El componente principal `header` `1349:4907` mide aproximadamente 1143.69×96, no pertenece a un set y expone cuatro propiedades booleanas: show version, show company, show icons y show avatar, todas activadas en la lectura actual. `✅` es parte del nombre observado, no aprobación del proyecto.
- Su recorrido explícito, incluyendo hijos de instancias ocultos, encontró 110 nodos: 1 componente, 25 instancias, 11 frames, 11 textos, 16 grupos, 45 vectores y 1 rectángulo; seis nodos están ocultos. La mayor parte del ruido vectorial pertenece al logotipo y debe mantenerse como dependencia reutilizable, no copiarse como anatomía funcional del Header.
- El helper fuente `icon header` aparece como un set de cinco valores `Amount=1–5` dentro de un frame oculto de la página. El Header observado consume `Amount=5`. Las cinco variantes aún requieren inspección propia antes de contrato/build.
- En la captura del Header se observan: logotipo de categoría, versión y etiqueta Alpha, cinco acciones con iconos (la última con indicador), selector de empresa, avatar y caret. Son datos de la variante visible, no una regla de producto ni inventario completo de estados.

## Dependencias activas

| Dependencia fuente | Evidencia activa | Situación de destino |
|---|---|---|
| Logo Categoria / logo de producto | Instancia `2873:23060`, variante `categoria=contable`; anida logotipo Contabilidad horizontal. El [descubrimiento de las cuatro variantes](logo-categoria.discovery.v0.1.0.md) separa el arte de marca de los tokens de UI. La variable fuente `logo/categoria` gobierna el eje. | La variable local `logo/categoria` existe (`VariableID:13:80`) con los cuatro modos del JSON. No hay página ni componente Logos en AI Design System; la importación local debe preservar vectores, gradientes, imágenes y literales de marca sin fingir equivalencias con primitivas. |
| icon header | Instancia `2780:11932`, `Amount=5`; set fuente con cinco variantes. | Helper aún no construido. Se propone ubicarlo junto al Header en página semántica `Headers`, sujeto a contrato profundo. |
| Button Icon | Cinco instancias middle dentro del helper y una small en selector de empresa; iconos activos ArrowsCounterClockwise, GraduationCap, Headset, AppWindow y Bell. | Icon Button ya existe como familia local; verificar variantes y swaps equivalentes. No enumerar los 1512 candidatos preferidos del selector. |
| Dot | Cuatro anidados ocultos y uno numérico visible en Bell; otros Dot ocultos en icono small y Avatar. | Dot local ya existe; verificar estado/size y contenido antes de reutilizar. |
| Avatar | Instancia Text, extra-large, texto de muestra `JA`, con indicador oculto. | Avatar local ya existe; verificar equivalencia semántica y binding. |
| Iconos Phosphor / caret | Cinco swaps activos del helper, un AppWindow small y dos CaretDown de pesos/formatos distintos. | Resolver por key/variante activa en la biblioteca disponible; no sustituir por un glyph parecido. |

La búsqueda de librerías encontró `logo-categoria` en la Librería antigua, pero **no** una definición local de Logos en AI Design System. Importar esa dependencia como instancia remota no cumple por sí solo el objetivo de biblioteca local trazable.

## Tokens observados

El recorrido de consumidores devolvió 35 IDs de variable distintos, incluidos colores de borde/fondo/texto/icono, tipografía, espaciado, radios, stroke, tamaños de icono y `logo/categoria`. Algunos IDs son de dependencias remotas; su nombre y valor no se infieren como token local. El contrato debe mapear cada consumidor visible al [JSON aprobado](../../sources/inventories/tokens.inventory.json) o a extensión de destino, verificando scope, alias y color por modo. Los tokens locales de borde, fondo, superficie, texto y `logo/categoria` consultados existen; aún falta mapear los 35 consumidores y los cinco valores del helper. No se crean variables en esta fase.

## Próximos gates

1. Completar contratos MD/YAML de `icon header` (cinco variantes ya recorridas) y Logo Categoria (cuatro variantes ya inventariadas), con dependencias por key y verificación de artwork local.
2. Resolver componentes locales ya existentes y mapear los tokens por consumidor, incluyendo los vectores de logotipo y la variable de categoría.
3. Sintetizar contrato de destino `Header` y helper, con nombre de página `Headers` sujeto a QA documental. Separar texto de demostración de propiedades editables.
4. Construir solo cuando dependencias, fidelidad visual y QA documental estén resueltos; después realizar readback, captura y auditoría por excepciones. No se modificó el Figma fuente ni el destino durante este descubrimiento.
