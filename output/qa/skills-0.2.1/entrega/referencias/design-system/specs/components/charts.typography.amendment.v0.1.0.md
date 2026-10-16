---
contract_schema: sdd-project/0.2
contract_id: CHARTS-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: CHARTS-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Charts · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `CHARTS-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../charts.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [six-family-color.amendment.v0.1.0.md](six-family-color.amendment.v0.1.0.md); [composition-slots.amendment.v0.1.1.md](../composition-slots.amendment.v0.1.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Charts](../../sources/figma-snapshots/typography/census.before.210-122.json) | Página `210:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `5c21d1c9200268b2152160aa1f95fb4f9235d4af6434113b89be64bab50d0ca2`. |
| [Base histórica](../charts.contract.v0.1.0.md) | SHA-256 `e65d084d9f7a9600df1d00f19922c1039b09e926315b9c3052746a1327d08cea`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **85 nodos UI, 85 rangos, 7 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `000` · Propio en Chart Legend Label | V001 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 1 | `N271`; `210:132@[0,3)` |
| `000` · Propio en Chart Legend Label | V003 | `ui-caption-compact-emphasis` | `S:2abe28a5572333135574e7c097c878babf7fcd84,` | 1 | `N273`; `210:140@[0,3)` |
| `000` · Propio en Chart Legend Label | V004 | `ui-chart-legend-medium-emphasis` | `S:7b31dce69c499509a0af3002b21866abdbfcd262,` | 1 | `N274`; `210:144@[0,3)` |
| `000` · Propio en Chart Legend Label | V002 | `ui-metric-label-compact` | `S:baee55f07c82b151e9cd50adbdd1511c771796ef,` | 1 | `N272`; `210:136@[0,3)` |
| `Percent` · Propio en Semi-donut Gauge | V005, V006, V007 | `ui-chart-gauge-value` | `S:d9b5d1dba7f2299ca9f25120b49032699343f365,` | 3 | `N275–N277`; `211:125@[0,3)` |
| `000` · Instancia/Slot en Progress Chart Item; referencia Chart Legend Label | V008, V009 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 12 | `N280–N285, N288–N293`; `I502:346;210:132@[0,8)` |
| `Label` · Propio en Progress Chart Item | V008, V009 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 2 | `N278, N286`; `213:124@[0,12)` |
| `Value` · Propio en Progress Chart Item | V008, V009 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 2 | `N279, N287`; `213:125@[0,5)` |
| `000` · Instancia/Slot en Chart Header; referencia Chart Legend Label | V010 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 3 | `N296–N298`; `I213:167;210:132@[0,7)` |
| `Description` · Propio en Chart Header | V010 | `ui-chart-description` | `S:996e9c5dc070f4c8cecb0dca5b420a8b212904a9,` | 1 | `N295`; `213:165@[0,11)` |
| `Title` · Propio en Chart Header | V010 | `ui-chart-header-title` | `S:8b81787ac3bffd1aa7be527a254057ae95425c48,` | 1 | `N294`; `213:164@[0,11)` |
| `000` · Instancia/Slot en muestras de revisión; referencia Chart Legend Label | E001, E002, E003, E004, E005 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 46 | `N301–N303, N306–N312, N316–N321, N324–N338, N341–N355`; `I488:240;213:167;210:132@[0,7)` |
| `000` · Instancia/Slot en muestras de revisión; referencia Chart Legend Label | E002 | `ui-caption-compact-emphasis` | `S:2abe28a5572333135574e7c097c878babf7fcd84,` | 1 | `N313`; `I488:261;213:166;488:310;210:140@[0,31)` |
| `Description` · Instancia/Slot en muestras de revisión; referencia Chart Header | E001, E002 | `ui-chart-description` | `S:996e9c5dc070f4c8cecb0dca5b420a8b212904a9,` | 2 | `N300, N305`; `I488:240;213:165@[0,11)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Progress Chart Item | E003, E004, E005 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 3 | `N314, N322, N339`; `I503:305;213:130@[0,12)` |
| `Title` · Instancia/Slot en muestras de revisión; referencia Chart Header | E001, E002 | `ui-chart-header-title` | `S:8b81787ac3bffd1aa7be527a254057ae95425c48,` | 2 | `N299, N304`; `I488:240;213:164@[0,11)` |
| `Value` · Instancia/Slot en muestras de revisión; referencia Progress Chart Item | E003, E004, E005 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 3 | `N315, N323, N340`; `I503:305;213:131@[0,5)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `210:129` | Chart Legend Label → Weight=Regular, Text size=Small |
| V002 | `210:133` | Chart Legend Label → Weight=Regular, Text size=Medium |
| V003 | `210:137` | Chart Legend Label → Weight=SemiBold, Text size=Small |
| V004 | `210:141` | Chart Legend Label → Weight=SemiBold, Text size=Medium |
| V005 | `211:122` | Semi-donut Gauge → Progress=75% |
| V006 | `211:126` | Semi-donut Gauge → Progress=50% |
| V007 | `211:130` | Semi-donut Gauge → Progress=25% |
| V008 | `213:122` | Progress Chart Item → Type=Top |
| V009 | `213:128` | Progress Chart Item → Type=Detail |
| V010 | `213:162` | Chart Header → Chart Header |
| E001 | `488:240` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `488:261` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `503:305` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `503:343` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E005 | `503:601` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

Una referencia compartida de propiedad de componente no unifica roles tipográficos. Una asignación solo es conforme si los rangos de esta tabla y los consumidores relacionados siguen resolviendo su estilo esperado después de la última escritura. No usar un setter posterior que desvincule silenciosamente el TextStyle. El contenido, color, visibilidad y formato semántico conservan su contrato. Cuando el catálogo declara `textDecoration`, ese formato procede del TextStyle y no de un setter posterior; una igualdad visual sin `textStyleId` no prueba cumplimiento.

## Aceptación y estado de implementación

| Criterio | Evidencia requerida |
|---|---|
| TYP-FAM-01 · cobertura | Reconciliar todos los nodos/rangos de esta familia, incluidos ocultos, muestras e instancias; justificar cualquier sustitución de ID con trazabilidad anterior→nuevo. |
| TYP-FAM-02 · estilo | Leer el TextStyle ID de cada rango después de la última mutación y cotejar con la tabla y `styleMap`; comprobar receta canónica, unidades y codificación numérica documentada. |
| TYP-FAM-03 · integridad | Preservar contenido, colores/bindings ajenos, geometría, API de propiedades, variantes, Slots e instancias; documentar cualquier cambio técnico necesario y comprobar sus consumidores. |
| TYP-FAM-04 · aislamiento | Volver a leer componentes que comparten propiedades o dependencias, con pruebas de texto y cambio de variante cuando correspondan; no validar desde el resultado inmediato de un setter. |
| TYP-FAM-05 · destinos | Separar QA documental, asignación Figma, preservación, web y publicación de skills. El PASS anterior de estilos/web no prueba este nuevo consumo Figma. |

Esta enmienda fija requisitos y cobertura documental. **La validación de consumidores requiere el QA final de la tarea de aplicación.** El bloqueo histórico y sus pruebas se conservan en [Figma-blocker.md](../../qa/implementations/typography/Figma-blocker.md); ni esta tabla ni la presencia del catálogo lo convierten en `VALIDATED`. La evidencia nueva debe registrar por separado su resolución o las diferencias restantes.

## Cambio versionado

| Versión | Fecha | Cambio |
|---|---|
| 0.1.0 | 2026-10-15 | Identidades tipográficas explícitas por consumidor y variante, con fuentes conservadas y auditoría humana pendiente. |
