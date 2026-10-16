---
contract_schema: sdd-project/0.2
contract_id: FUENTES-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: FUENTES-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Fuentes · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `FUENTES-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](fuentes.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Los textos de ruta y separador mantienen su excepción micro; las etiquetas Type/Location y Source conservan roles distintos. El Dot anidado conserva su estilo. Ninguna coincidencia numérica convierte la ruta en caption general.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Fuentes](../../sources/figma-snapshots/typography/census.before.847-7.json) | Página `847:7`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `ff7bd7ac672567189736820d22bb67569194c2ba4a0fd9223840a07bbea73935`. |
| [Base histórica](fuentes.contract.v0.1.0.md) | SHA-256 `284f22ca2bcb36291bcfcfeb00d48cb0b3f7fef46d9a71c579a4f58456a17799`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **108 nodos UI, 108 rangos, 4 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Count label` · Instancia/Slot en Fuentes; referencia Dot | V001, V002 | `micro-count-medium` | `S:f0c0dc4cd43b6d27d1c05ad262a09b29dd415bf1,` | 2 | `N3379, N3387`; `I848:14;155:135@[0,1)` |
| `Label` · Instancia/Slot en Fuentes; referencia Fuentes Path Item | V001, V002 | `micro-source-path` | `S:249112e571c2a957d3d7b3fd4bf48c12b5796052,` | 4 | `N3384, N3386, N3392, N3394`; `I848:20;848:10@[0,18)` |
| `Location` · Propio en Fuentes | V001, V002 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 2 | `N3382, N3390`; `848:18@[0,9)` |
| `Separator` · Instancia/Slot en Fuentes; referencia Fuentes Path Item | V001, V002 | `micro-source-path` | `S:249112e571c2a957d3d7b3fd4bf48c12b5796052,` | 4 | `N3383, N3385, N3391, N3393`; `I848:20;848:9@[0,3)` |
| `Source` · Propio en Fuentes | V001, V002 | `ui-source-title` | `S:72120f027b39543782c2c7f48edfea7157405e4d,` | 2 | `N3381, N3389`; `848:17@[0,9)` |
| `Type` · Propio en Fuentes | V001, V002 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 2 | `N3380, N3388`; `848:16@[0,20)` |
| `Label` · Propio en Fuentes Path Item | V003 | `micro-source-path` | `S:249112e571c2a957d3d7b3fd4bf48c12b5796052,` | 1 | `N3378`; `848:10@[0,18)` |
| `Separator` · Propio en Fuentes Path Item | V003 | `micro-source-path` | `S:249112e571c2a957d3d7b3fd4bf48c12b5796052,` | 1 | `N3377`; `848:9@[0,3)` |
| `Count label` · Instancia/Slot en muestras de revisión; referencia Dot | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011 | `micro-count-medium` | `S:f0c0dc4cd43b6d27d1c05ad262a09b29dd415bf1,` | 11 | `N3396, N3404, N3413, N3417, N3423, N3431, N3443, N3455, N3463, N3471, N3479`; `I848:45;848:14;155:135@[0,1)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Fuentes Path Item | E001, E002, E003, E004, E005, E006, E007, E008, E010, E011 | `micro-source-path` | `S:249112e571c2a957d3d7b3fd4bf48c12b5796052,` | 23 | `N3401, N3403, N3409, N3411, N3422, N3428, N3430, N3436, N3438, N3440, N3442, N3448, N3450, N3452, N3454, N3460, N3462, N3468, N3470, N3476, N3478, N3484, N3486`; `I848:45;848:20;848:10@[0,18)` |
| `Location` · Instancia/Slot en muestras de revisión; referencia Fuentes | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 11 | `N3399, N3407, N3416, N3420, N3426, N3434, N3446, N3458, N3466, N3474, N3482`; `I848:45;848:18@[0,9)` |
| `Separator` · Instancia/Slot en muestras de revisión; referencia Fuentes Path Item | E001, E002, E003, E004, E005, E006, E007, E008, E010, E011 | `micro-source-path` | `S:249112e571c2a957d3d7b3fd4bf48c12b5796052,` | 23 | `N3400, N3402, N3408, N3410, N3421, N3427, N3429, N3435, N3437, N3439, N3441, N3447, N3449, N3451, N3453, N3459, N3461, N3467, N3469, N3475, N3477, N3483, N3485`; `I848:45;848:20;848:9@[0,3)` |
| `Source` · Instancia/Slot en muestras de revisión; referencia Fuentes | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011 | `ui-source-title` | `S:72120f027b39543782c2c7f48edfea7157405e4d,` | 11 | `N3398, N3406, N3415, N3419, N3425, N3433, N3445, N3457, N3465, N3473, N3481`; `I848:45;848:17@[0,9)` |
| `Type` · Instancia/Slot en muestras de revisión; referencia Fuentes | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 11 | `N3397, N3405, N3414, N3418, N3424, N3432, N3444, N3456, N3464, N3472, N3480`; `I848:45;848:16@[0,20)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `848:11` | Fuentes → State=Default |
| V002 | `848:26` | Fuentes → State=Hover |
| V003 | `848:8` | Fuentes Path Item → Fuentes Path Item |
| E001 | `848:45` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `848:60` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `849:108` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `849:141` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E005 | `849:198` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E006 | `849:213` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E007 | `849:228` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E008 | `849:243` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E009 | `849:45` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E010 | `849:62` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E011 | `849:83` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
