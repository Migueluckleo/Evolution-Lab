---
contract_schema: sdd-project/0.2
contract_id: CHARTS-001
name: Charts
type: component_family
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Charts
sources: [SRC-FIGMA-CHART-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.chart-colors.v0.1.0.json, sources/figma-snapshots/chart-donut.vector-paths.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-CHART-COLORS-001]
user_audit: PENDING
---

# Charts · contrato de reconstrucción 0.1.0

> Vigencia cromática: la [enmienda SIX-FAMILY-COLOR-001](components/six-family-color.amendment.v0.1.0.md) sustituye exclusivamente las recetas/umbrales allí identificados. Publicación documental 2026-10-05; auditoría humana PENDING. Los apartados históricos se leen junto con esa enmienda.

## 1. Purpose

Reconstruir en AI Design System las cinco piezas reutilizables de la página Chart del origen: [labelCell](../drafts/contracts/chart-label-cell.source.component-contract.md), [cell](../drafts/contracts/chart-cell.source.component-contract.md), [Progress chart item](../drafts/contracts/chart-progress-item.source.component-contract.md), [Donut](../drafts/contracts/chart-donut.source.component-contract.md) y [Header](../drafts/contracts/chart-header.source.component-contract.md). Los cuatro gráficos completos superiores de la página son composiciones de demostración, no componentes principales observados; no se convierten en variantes. Los valores son muestras estáticas.

## 2. Contract

Crear una página exclusiva `Charts`, con cuatro sets y un componente suelto: `Chart Legend Label` (4 variantes), `Chart Cell` (13), `Progress Chart Item` (2), `Semi-donut Gauge` (3) y `Chart Header` (1). Total: 23 definiciones reutilizables. Mantenerlos `UNPUBLISHED` y registrar el mapeo de cada ID fuente a ID destino. Construir la dependencia Legend Label antes de Progress y Header; estos dos deben contener instancias locales reales, no copias detach.

## 3. Anatomy

- Chart Legend Label: frame Dot de 16×16 con swatch shape de 16×10 y texto.
- Chart Cell: contorno discontinuo 26×35, opcional BarCell de 14×35 con radios dependientes de segmento.
- Progress Chart Item: encabezado Label/Value, track y relleno; Detail agrega dos filas con tres instancias Legend Label por fila.
- Semi-donut Gauge: dos paths vectoriales —Total y Completed— y porcentaje centrado.
- Chart Header: título, descripción y tres instancias Legend Label para series.

## 4. Properties

| Componente | Propiedades de destino | Default y fundamento |
|---|---|---|
| Chart Legend Label | `Weight` VARIANT Regular/SemiBold; `Text size` VARIANT Small/Medium; `Text` TEXT; `Show swatch` BOOLEAN | Regular/Small, `000`, true; mapea los ejes Regular/Semi-bold × sm/lg y `spotVisible` fuente; Medium significa 16 px, no 20. |
| Chart Cell | `Has content`, `Position`, `Segment` VARIANT | false/−/−; solo las 13 combinaciones observadas. |
| Progress Chart Item | `Type` VARIANT Top/Detail; `Label` TEXT; `Value` TEXT | Top, `Text example`, `$100k`; las dos últimas enlazan ambos encabezados. |
| Semi-donut Gauge | `Progress` VARIANT 75%/50%/25% | 75%; texto y arco permanecen sincronizados por variante, sin propiedad TEXT libre. |
| Chart Header | `Title` TEXT; `Description` TEXT; `Show legend` BOOLEAN; `Show description` BOOLEAN; tres textos de leyenda editables en sus instancias | `Title chart`, `Description`, true/true, Value 1/2/3. `Title` corrige la errata fuente `Ttile`; las instancias conservan su propiedad Text para editar cada valor sin alterar aspecto. |

## 5. Variants

Legend Label tiene cuatro cruces 2×2. Cell tiene exactamente empty false/−/− y true × first/middle/last × solo/upper/middle/lower. Progress tiene Top y Detail. Gauge tiene 75, 50 y 25. Header no es set. No crear 27 cruces faltantes de Cell ni estados interactivos.

## 6. Sizes

Legend Label 76×16 por variante; set original 193×92. Cell 26×35; barra 14×35. Progress Top 639×30 y Detail 639×104, con tracks 639×8 y 639×24; rellenos de muestra 580×8 y 247×24. Gauge 283×142 y paths del [snapshot geométrico](../sources/figma-snapshots/chart-donut.vector-paths.json). Header de origen 638×47; destino 638×48 para ligar Title y Description a interlineado local de 20 px sin recorte. No hay otros cambios de cajas de definición.

## 7. States

No se observan Hover, Focus, Disabled, Loading ni reacciones. `Progress` de Gauge es valor estático; `Position` y `Segment` de Cell son estructura. Las booleanas de visibilidad no implican comportamiento interactivo.

## 8. Behavior

Figma muestra ejemplos fijos. No convertir el ancho de barra en porcentaje calculado ni corregir el `80%` de leyenda para hacerlo coincidir con 580/639 o 247/639: la fuente no define esa relación. No añadir tooltip, animación o actualización de datos.

## 9. Accessibility

Los textos y porcentajes visibles son pistas, pero un consumidor real debe suministrar nombre, unidad, valor/rango y alternativa no cromática para cada serie. Figma no demuestra semántica de lectores de pantalla ni teclado. Comprobar legibilidad visual, no certificar accesibilidad funcional.

## 10. Design tokens

El inventario base tiene SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; el [JSON de extensión](../drafts/foundations/ai-design-system.chart-colors.v0.1.0.json) gobierna siete roles nuevos y Figma ya confirma sus cuatro aliases. Mapa obligatorio de pintura:

| Consumidor | Token semántico | Scope |
|---|---|---|
| Textos de las cinco piezas | `color/text/primary` | TEXT_FILL |
| Track lineal | `color/background/muted` | FRAME_FILL |
| BarCell | `color/background/chart/bar` | FRAME_FILL |
| Borde discontinuo de Cell | `color/border/accent` | STROKE_COLOR |
| Relleno de progreso lineal y Completed del Gauge | `color/shape/chart/progress` | SHAPE_FILL |
| Total del Gauge | `color/shape/chart/track` | SHAPE_FILL |
| Swatch por defecto sin serie | `color/shape/chart/legend-neutral` | SHAPE_FILL |
| Swatches de Header Value 1/2/3 | `color/shape/chart/series-1/2/3` respectivamente | SHAPE_FILL |

Los swatches de las filas Detail usan progress y track como roles de shape. No usar `color/icon/*`, `color/interactive/*` ni `color/text/*` para formas, ni `color/background/*` para swatches. Tipografía: Manrope por `font/family/base`; peso Regular/SemiBold por roles `font/weight/*`; tamaños `font/size/xs` 12, `font/size/md` 16, `font/size/lg` 20 y `font/size/2xl` 32; line-heights xs/sm/md donde correspondan, más `font/letter-spacing/normal`. El origen no liga todo eso; el destino sí debe ligar familia, estilo, tamaño, interlineado y tracking de todos los textos. Espacios/radios usan variables locales `spacing/*` y `radius/*` donde corresponda; el cero puede permanecer cero explícito, sin alias remoto inventado. La posición Middle de Cell necesita padding lateral 6 px, valor ausente de la escala primitiva 0/4/8/12…; se conserva solo allí como excepción geométrica literal, sin añadir primitiva ni redondear a 4 u 8. El avance del Gauge usa un tono más oscuro que la fuente para distinguirlo de la pista: contraste entre ambos de 3.10:1 o mayor en los cuatro modos, conservando la familia de marca. El swatch de segunda serie y el neutro también se oscurecen para legibilidad sobre blanco.

## 11. Content rules

`000`, `Text example`, `$100k`, `Progress`, `80%`, `80k`, Value 1/2/3 y los porcentajes del Gauge son muestras. El color de una serie nunca sustituye su etiqueta. Los textos editables no imponen formato monetario, locale, precisión ni longitud máxima.

## 12. Composition rules

Header y Progress reutilizan el mismo main component local `Chart Legend Label` mediante instancias con textos y swatches personalizados. Seis instancias en Detail y tres en Header; Top no necesita leyenda. Los paths Gauge proceden del snapshot exacto y permanecen vectoriales; Figma puede normalizar la serialización de decimales sin cambiar su geometría. Cada conjunto vive en la misma página `Charts`, separado visualmente con título de sección, sin convertir las demostraciones en components.

## 13. Responsive behavior

No se observan breakpoints; las cajas son muestras de diseño. Los valores Small/Medium de Legend son variantes tipográficas, no tamaños de viewport. La adaptación a ancho menor queda `UNRESOLVED` para web y no bloquea estas definiciones Figma.

## 14. Edge cases

Ocultar swatch o descripción debe colapsar el hueco por auto layout. Cambiar texto largo puede requerir ancho mayor; no recortar silenciosamente. Los dos tramos de Gauge no deben superponerse con un orden que oculte Completed. Las barras fijas no representan una API de porcentaje variable.

## 15. Forbidden combinations

No materializar combinaciones Cell ausentes; no añadir estados, cálculos o prototipos; no rasterizar Gauge; no detach de Legend Label; no usar fills literales visibles ni roles fuera de scope; no renombrar los valores 75/50/25 como intervalos variables.

## 16. Design ↔ Code mapping

En frontend futuro, Legend Label sería una leyenda con texto y swatch, Cell una visualización de segmento, Progress/Gauge componentes controlados por datos tipados y Header un encabezado de gráfico. Esta tarea no implementa frontend ni promete equivalencia de comportamiento con Figma.

## 17. Acceptance criteria

| ID | Verificación |
|---|---|
| AC-CHT-001 | Página única `Charts` con cuatro sets y un componente Header, 23 definiciones en total y nombres semánticos. |
| AC-CHT-002 | Cuatro, trece, dos y tres variantes de los sets, más Header, con propiedades/defaults del contrato y sin cruces Cell inventados. |
| AC-CHT-003 | Nueve instancias locales reales de Legend Label en Progress Detail/Header y cero detach. |
| AC-CHT-004 | Gauge conserva seis paths vectoriales y tres porcentajes vinculados a sus variantes; no hay raster. |
| AC-CHT-005 | Todos los paints visibles usan variables locales de categoría/scope correctos; siete roles nuevos coinciden con JSON en cuatro modos. |
| AC-CHT-006 | Todos los textos tienen bindings locales para familia, estilo, tamaño, interlineado y tracking; geometría y muestra visual se contrastan con fuente. |
| AC-CHT-007 | Cero reacciones; página y componentes `UNPUBLISHED`; QA técnico y cambios frente al origen registrados para auditoría humana. |

## 18. Examples

Legend Label Regular/Small muestra `000`; Cell first/solo muestra una barra redondeada; Progress Detail muestra dos leyendas; Gauge 75% y Header con tres valores muestran composiciones estáticas.

## 19. Source of truth

Este Markdown gobierna las reglas de destino; el inventario y extensión JSON gobiernan variables. Los cinco contratos fuente y el snapshot vectorial preservan observación, no son IDs de destino. Los IDs reales se guardan en `implementations/figma/` tras readback.

## 20. Change management

Cambios deliberados: nombres funcionales en página destino; errata `Ttile`→`Title`; Header +1 px de alto; gris literal de swatch→rol neutral; avance Gauge más oscuro para distinguirlo de pista; swatches de series normalizados por modo; roles genéricos/interactive/icon de origen→roles chart estrictos; tipografía completa ligada a variables locales. Los tres textos de leyenda del Header siguen editables en las instancias, como en fuente. Se conservan conteos, anatomía, geometría fija de ejemplos y paths; el padding Middle de 6 px es la excepción literal acotada. La normalización numérica de path que hace Figma se comprueba por comandos y coordenadas, no por identidad de bytes.

## 21. Changelog

- 0.1.0 delegado: cinco piezas, 23 definiciones, siete roles semánticos de Chart y auditoría humana posterior.
