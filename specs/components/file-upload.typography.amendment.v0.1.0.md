---
contract_schema: sdd-project/0.2
contract_id: FILEUPLOAD-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: FILEUPLOAD-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# FileUpload · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `FILEUPLOAD-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../file-upload.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Input Fields](../../sources/figma-snapshots/typography/census.before.394-122.json) | Página `394:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `80d4bb678b15ef6ffca912dfc290d700d1e65bcfe5c471c1b97f8abfcefcc827`. |
| [Base histórica](../file-upload.contract.v0.1.0.md) | SHA-256 `e069fb28b37cb08c73300ace453d5318858f912f078566e87c731cc874ae4fb5`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **32 nodos UI, 32 rangos, 6 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Action text` · Propio en File Upload | V001, V002, V003, V004 | `ui-upload-action-feedback-underline` | `S:84b3287900a860c9096c09ccc9c405e2bfbc7207,` | 4 | `N922, N928, N934, N940`; `420:229@[0,16)` |
| `Error message` · Propio en File Upload | V006 | `ui-upload-action-feedback` | `S:ce2a18b20dd0f99926e713b79ca430cf90f70b25,` | 1 | `N949`; `420:311@[0,26)` |
| `Formats` · Propio en File Upload | V001, V002, V003, V004, V006 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 5 | `N924, N930, N936, N942, N950`; `420:231@[0,60)` |
| `Formats` · Propio en File Upload | V005 | `ui-upload-format-success` | `S:3b0d7f1a14a98fbc39b0b3dbc9d48a0aca58da71,` | 1 | `N946`; `420:296@[0,60)` |
| `Helper` · Propio en File Upload | V001, V002, V003, V004, V005, V006 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 6 | `N926, N932, N938, N944, N948, N952`; `420:238@[0,20)` |
| `Message prefix` · Propio en File Upload | V001, V002, V003, V004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N921, N927, N933, N939`; `420:228@[0,13)` |
| `Message suffix` · Propio en File Upload | V001, V002, V003, V004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N923, N929, N935, N941`; `420:230@[0,17)` |
| `Success message` · Propio en File Upload | V005 | `ui-upload-action-feedback` | `S:ce2a18b20dd0f99926e713b79ca430cf90f70b25,` | 1 | `N945`; `420:295@[0,28)` |
| `label-text` · Instancia/Slot en File Upload; referencia button | V001, V002, V003, V004, V005, V006 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 6 | `N925, N931, N937, N943, N947, N951`; `I420:232;26:104@[0,13)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `420:222` | File Upload → State=Default |
| V002 | `420:239` | File Upload → State=Hover |
| V003 | `420:256` | File Upload → State=Focus |
| V004 | `420:273` | File Upload → State=Disabled |
| V005 | `420:290` | File Upload → State=Success |
| V006 | `420:306` | File Upload → State=Error |

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
