---
contract_schema: sdd-project/0.2
contract_id: CHAT-TOOLBAR-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: CHAT-TOOLBAR-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# ChatToolbar · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `CHAT-TOOLBAR-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../chat-toolbar.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [chat.layout.amendment.v0.1.1.md](chat.layout.amendment.v0.1.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Las recetas de títulos, metadatos, plan y dependencias anidadas se verifican separadamente en Expanded=true/false, incluso cuando se ocultan regiones. No propagar una asignación entre propiedades o textos que tengan funciones diferentes.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Chat](../../sources/figma-snapshots/typography/census.before.783-6.json) | Página `783:6`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `0fc1384c45ef91d97ccef9b67040e1ce4124291fea9f4f898a649ac07939fbf0`. |
| [Base histórica](../chat-toolbar.contract.v0.1.0.md) | SHA-256 `2b96dccbb48044dae0157cf09c068b368cac7d8dbdecd4a13e7ef7caf6d8fb43`; reglas ajenas a esta sustitución preservadas. |
| [Identidad de muestras](../../qa/implementations/chat-toolbar.v0.1.0.final.json) | Relación de instancias de revisión con su familia; evidencia histórica, no nuevo PASS tipográfico. SHA-256 `1275ee978ba935d67af17c05eb62677a98508714e4f2b48bb2afe4757456b817`. |

Cobertura de este corte: **76 nodos UI, 76 rangos, 4 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Chats title` · Propio en Chat Toolbar | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3300, N3319`; `797:430@[0,5)` |
| `Count label` · Instancia/Slot en Chat Toolbar; referencia Dot | V001, V002 | `micro-count-small` | `S:2987fb55403e26b9fd23807ce894f58cc084820d,` | 2 | `N3290, N3309`; `I797:375;183:164;155:137@[0,1)` |
| `Indicators title` · Propio en Chat Toolbar | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3294, N3313`; `797:405@[0,11)` |
| `Label` · Instancia/Slot en Chat Toolbar; referencia Chat Tool Item | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 8 | `N3291–N3293, N3295, N3310–N3312, N3314`; `I797:383;796:434@[0,10)` |
| `Plan name` · Propio en Chat Toolbar | V001, V002 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 2 | `N3305, N3324`; `797:450@[0,8)` |
| `Title text` · Instancia/Slot en Chat Toolbar; referencia Chat History Item | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N3296, N3298, N3315, N3317`; `I797:419;796:476@[0,10)` |
| `Title text` · Instancia/Slot en Chat Toolbar; principal de texto no identificado en censo local | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N3301, N3303, N3320, N3322`; `I797:432;796:475;797:438@[0,33)` |
| `Updated` · Instancia/Slot en Chat Toolbar; referencia Chat History Item | V001, V002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 8 | `N3297, N3299, N3302, N3304, N3316, N3318, N3321, N3323`; `I797:419;796:477@[0,5)` |
| `Usage label` · Propio en Chat Toolbar | V001, V002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 2 | `N3306, N3325`; `797:453@[0,9)` |
| `Usage percentage` · Propio en Chat Toolbar | V001, V002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 2 | `N3308, N3327`; `797:457@[0,13)` |
| `Usage quantity` · Propio en Chat Toolbar | V001, V002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 2 | `N3307, N3326`; `797:454@[0,7)` |
| `Chats title` · Instancia/Slot en muestras de revisión; referencia Chat Toolbar | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3338, N3357`; `I798:291;797:475@[0,5)` |
| `Count label` · Instancia/Slot en muestras de revisión; referencia Dot | E001, E002 | `micro-count-small` | `S:2987fb55403e26b9fd23807ce894f58cc084820d,` | 2 | `N3328, N3347`; `I798:291;797:462;183:164;155:137@[0,1)` |
| `Indicators title` · Instancia/Slot en muestras de revisión; referencia Chat Toolbar | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N3332, N3351`; `I798:291;797:469@[0,11)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Chat Tool Item | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 8 | `N3329–N3331, N3333, N3348–N3350, N3352`; `I798:291;797:465;796:434@[0,10)` |
| `Plan name` · Instancia/Slot en muestras de revisión; referencia Chat Toolbar | E001, E002 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 2 | `N3343, N3362`; `I798:291;797:482@[0,8)` |
| `Title text` · Instancia/Slot en muestras de revisión; referencia Chat History Item | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N3334, N3336, N3353, N3355`; `I798:291;797:472;796:476@[0,10)` |
| `Title text` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E001, E002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 4 | `N3339, N3341, N3358, N3360`; `I798:291;797:477;797:491@[0,33)` |
| `Updated` · Instancia/Slot en muestras de revisión; referencia Chat History Item | E001, E002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 8 | `N3335, N3337, N3340, N3342, N3354, N3356, N3359, N3361`; `I798:291;797:472;796:477@[0,5)` |
| `Usage label` · Instancia/Slot en muestras de revisión; referencia Chat Toolbar | E001, E002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 2 | `N3344, N3363`; `I798:291;797:485@[0,9)` |
| `Usage percentage` · Instancia/Slot en muestras de revisión; referencia Chat Toolbar | E001, E002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 2 | `N3346, N3365`; `I798:291;797:489@[0,13)` |
| `Usage quantity` · Instancia/Slot en muestras de revisión; referencia Chat Toolbar | E001, E002 | `ui-chat-metadata` | `S:5a3f44d14ee74e638de3493a255ca0c55e337289,` | 2 | `N3345, N3364`; `I798:291;797:486@[0,7)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `797:316` | Chat Toolbar → Expanded=true |
| V002 | `797:458` | Chat Toolbar → Expanded=false |
| E001 | `798:291` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `798:316` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
