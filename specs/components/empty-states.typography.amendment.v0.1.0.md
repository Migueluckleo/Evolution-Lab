---
contract_schema: sdd-project/0.2
contract_id: EMPTY-STATES-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: EMPTY-STATES-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# EmptyStates · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `EMPTY-STATES-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../empty-states.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Default/Compact/Inline y Main conservan sus títulos distintos. Los botones anidados tienen un estilo contextual propio; no trasladar esa elección al principal Button.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Empty states](../../sources/figma-snapshots/typography/census.before.639-128.json) | Página `639:128`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `904f0c344ec762bfd3ea8ff2062c489719fbc7fabdccb7e7d3a063e5b72dcaee`. |
| [Base histórica](../empty-states.contract.v0.1.0.md) | SHA-256 `25de9da45c7e835f9b244867b7b70d3ec496a270ab61ec785e49775526fd750f`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **32 nodos UI, 32 rangos, 5 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Description` · Propio en Empty State | V001, V002, V003, V004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N3085, N3089, N3093, N3097`; `645:148@[0,116)` |
| `Title` · Propio en Empty State | V004 | `ui-empty-main-title` | `S:36d346b8b1c5766a8dfd3498701a7bb92f8e8539,` | 1 | `N3096`; `645:225@[0,43)` |
| `Title` · Propio en Empty State | V001, V002, V003 | `ui-empty-title` | `S:e131a51074bfff0c80f1c3f2f164e74a77b77ca0,` | 3 | `N3084, N3088, N3092`; `645:147@[0,43)` |
| `label-text` · Instancia/Slot en Empty State; referencia button | V001, V002, V003, V004 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 4 | `N3086, N3090, N3094, N3098`; `I645:150;26:88@[0,11)` |
| `label-text` · Instancia/Slot en Empty State; referencia button | V001, V002, V003, V004 | `ui-action-label-normal-underline` | `S:872b2d6d8242f9b571eb16c75b9535809600ac73,` | 4 | `N3087, N3091, N3095, N3099`; `I645:157;26:112@[0,9)` |
| `Description` · Instancia/Slot en muestras de revisión; referencia Empty State | E001, E002, E003, E004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N3101, N3105, N3109, N3113`; `I649:292;645:148@[0,116)` |
| `Title` · Instancia/Slot en muestras de revisión; referencia Empty State | E004 | `ui-empty-main-title` | `S:36d346b8b1c5766a8dfd3498701a7bb92f8e8539,` | 1 | `N3112`; `I649:437;645:225@[0,43)` |
| `Title` · Instancia/Slot en muestras de revisión; referencia Empty State | E001, E002, E003 | `ui-empty-title` | `S:e131a51074bfff0c80f1c3f2f164e74a77b77ca0,` | 3 | `N3100, N3104, N3108`; `I649:292;645:147@[0,43)` |
| `label-text` · Instancia/Slot en muestras de revisión; referencia button | E001, E002, E003, E004 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 4 | `N3102, N3106, N3110, N3114`; `I649:292;645:150;26:88@[0,11)` |
| `label-text` · Instancia/Slot en muestras de revisión; referencia button | E001, E002, E003, E004 | `ui-action-label-normal-underline` | `S:872b2d6d8242f9b571eb16c75b9535809600ac73,` | 4 | `N3103, N3107, N3111, N3115`; `I649:292;645:157;26:112@[0,9)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `645:124` | Empty State → Use case=Default |
| V002 | `645:163` | Empty State → Use case=Compact |
| V003 | `645:192` | Empty State → Use case=Inline |
| V004 | `645:221` | Empty State → Use case=Main |
| E001 | `649:292` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `649:335` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `649:376` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `649:437` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
