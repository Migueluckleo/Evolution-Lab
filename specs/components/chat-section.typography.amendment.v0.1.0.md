---
contract_schema: sdd-project/0.2
contract_id: CHAT-SECTION-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: CHAT-SECTION-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# ChatSection · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `CHAT-SECTION-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../chat-section.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [chat.layout.amendment.v0.1.1.md](chat.layout.amendment.v0.1.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Greeting/User name, Subtitle y Status no comparten estilo por tener una referencia de propiedad común. Standby y Active conservan los textos ocultos y sus Slots. Las sugerencias y Conversation anidado mantienen sus contratos y estilos propios.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Chat](../../sources/figma-snapshots/typography/census.before.783-6.json) | Página `783:6`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `0fc1384c45ef91d97ccef9b67040e1ce4124291fea9f4f898a649ac07939fbf0`. |
| [Base histórica](../chat-section.contract.v0.1.0.md) | SHA-256 `59c5331596821920d475c6efa1c80ce3deaf05a9f3ffa41ba97d3a28f7c0093f`; reglas ajenas a esta sustitución preservadas. |
| [Identidad de muestras](../../implementations/figma/chat-section.v0.1.0.state.json) | Relación de instancias de revisión con su familia; evidencia histórica, no nuevo PASS tipográfico. SHA-256 `fcebe26b910602c0d52198f11b499ee237b8d1431a8d9836408d2c4f837551d4`. |

Cobertura de este corte: **58 nodos UI, 58 rangos, 6 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Label` · Propio en Chat Suggestion | V002, V003 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3219–N3220`; `783:20@[0,30)` |
| `Count label` · Instancia/Slot en Chat Section; referencia Dot | V001, V004 | `micro-count-small` | `S:2987fb55403e26b9fd23807ce894f58cc084820d,` | 6 | `N3229–N3231, N3243–N3245`; `I783:47;765:415;183:164;155:137@[0,1)` |
| `Disclaimer` · Instancia/Slot en Chat Section; referencia Conversation Composer | V001, V004 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 2 | `N3226, N3240`; `I783:47;765:398@[0,83)` |
| `Greeting` · Propio en Chat Section | V001, V004 | `ui-chat-title` | `S:711fbb388c69ce8d554ef531ebd946cae14a0080,` | 2 | `N3221, N3235`; `783:34@[0,5)` |
| `Label` · Instancia/Slot en Chat Section; referencia Chat Suggestion | V001, V004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 6 | `N3232–N3234, N3246–N3248`; `I783:84;783:20@[0,30)` |
| `Message text` · Instancia/Slot en Chat Section; referencia Conversation Message | V001, V004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3224, N3238`; `I783:43;765:273@[0,73)` |
| `Model label` · Instancia/Slot en Chat Section; referencia Conversation Composer | V001, V004 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 2 | `N3228, N3242`; `I783:47;765:409@[0,14)` |
| `Placeholder` · Instancia/Slot en Chat Section; referencia Conversation Composer | V001, V004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3227, N3241`; `I783:47;765:401@[0,41)` |
| `Status text` · Propio en Chat Section | V001, V004 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3225, N3239`; `783:46@[0,25)` |
| `Subtitle` · Propio en Chat Section | V001, V004 | `ui-chat-subtitle` | `S:4f627d060dffc9ff20afafa2c8a3adc468a669f6,` | 2 | `N3223, N3237`; `783:40@[0,31)` |
| `User name` · Propio en Chat Section | V001, V004 | `ui-chat-title` | `S:711fbb388c69ce8d554ef531ebd946cae14a0080,` | 2 | `N3222, N3236`; `783:35@[0,11)` |
| `Count label` · Instancia/Slot en muestras de revisión; referencia Dot | E001, E002 | `micro-count-small` | `S:2987fb55403e26b9fd23807ce894f58cc084820d,` | 6 | `N3259–N3261, N3273–N3275`; `I784:103;783:47;765:415;183:164;155:137@[0,1)` |
| `Disclaimer` · Instancia/Slot en muestras de revisión; referencia Conversation Composer | E001, E002 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 2 | `N3256, N3270`; `I784:103;783:47;765:398@[0,83)` |
| `Greeting` · Instancia/Slot en muestras de revisión; referencia Chat Section | E001, E002 | `ui-chat-title` | `S:711fbb388c69ce8d554ef531ebd946cae14a0080,` | 2 | `N3251, N3265`; `I784:103;783:34@[0,5)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Chat Suggestion | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 6 | `N3262–N3264, N3276–N3278`; `I784:103;783:84;783:20@[0,30)` |
| `Message text` · Instancia/Slot en muestras de revisión; referencia Conversation Message | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3254, N3268`; `I784:103;783:43;765:273@[0,73)` |
| `Model label` · Instancia/Slot en muestras de revisión; referencia Conversation Composer | E001, E002 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 2 | `N3258, N3272`; `I784:103;783:47;765:409@[0,14)` |
| `Placeholder` · Instancia/Slot en muestras de revisión; referencia Conversation Composer | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3257, N3271`; `I784:103;783:47;765:401@[0,41)` |
| `Status text` · Instancia/Slot en muestras de revisión; referencia Chat Section | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3255, N3269`; `I784:103;783:46@[0,25)` |
| `Subtitle` · Instancia/Slot en muestras de revisión; referencia Chat Section | E001, E002 | `ui-chat-subtitle` | `S:4f627d060dffc9ff20afafa2c8a3adc468a669f6,` | 2 | `N3253, N3267`; `I784:103;783:40@[0,31)` |
| `User name` · Instancia/Slot en muestras de revisión; referencia Chat Section | E001, E002 | `ui-chat-title` | `S:711fbb388c69ce8d554ef531ebd946cae14a0080,` | 2 | `N3252, N3266`; `I784:103;783:35@[0,11)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `783:116` | Chat Section → State=Active |
| V002 | `783:14` | Chat Suggestion → State=Default |
| V003 | `783:21` | Chat Suggestion → State=Hover |
| V004 | `783:24` | Chat Section → State=Standby |
| E001 | `784:103` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `784:163` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
