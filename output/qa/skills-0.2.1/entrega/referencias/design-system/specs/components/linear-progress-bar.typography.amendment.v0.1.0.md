---
contract_schema: sdd-project/0.2
contract_id: LINEAR-PROGRESS-BAR-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: LINEAR-PROGRESS-BAR-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# LinearProgressBar · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `LINEAR-PROGRESS-BAR-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../linear-progress-bar.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [six-family-color.amendment.v0.1.0.md](six-family-color.amendment.v0.1.0.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Linear Progress Bars](../../sources/figma-snapshots/typography/census.before.220-122.json) | Página `220:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `22f018328717840f7a6bddcfe0f19c0aef2b2bd48034c32504d69915bc0478bc`. |
| [Base histórica](../linear-progress-bar.contract.v0.1.0.md) | SHA-256 `6fa5650cfec2b1c200f58097b29746974defad6198ce76784ff42ab77892b316`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **144 nodos UI, 144 rangos, 2 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Helper text` · Propio en Linear Progress Bar | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018, V019, V020, V021, V022, V023, V024, V025, V026, V027, V028, V029, V030, V031, V032, V033, V034, V035, V036, V037, V038, V039, V040, V041, V042, V043, V044, V045, V046, V047, V048 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 48 | `N359, N362, N365, N368, N371, N374, N377, N380, N383, N386, N389, N392, N395, N398, N401, N404, N407, N410, N413, N416, N419, N422, N425, N428, N431, N434, N437, N440, N443, N446, N449, N452, N455, N458, N461, N464, N467, N470, N473, N476, N479, N482, N485, N488, N491, N494, N497, N500`; `220:130@[0,20)` |
| `Label` · Propio en Linear Progress Bar | V005, V006, V007, V008, V009, V010, V011, V012, V017, V018, V019, V020, V021, V022, V023, V024, V029, V030, V031, V032, V033, V034, V035, V036, V041, V042, V043, V044, V045, V046, V047, V048 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 32 | `N369, N372, N375, N378, N381, N384, N387, N390, N405, N408, N411, N414, N417, N420, N423, N426, N441, N444, N447, N450, N453, N456, N459, N462, N477, N480, N483, N486, N489, N492, N495, N498`; `220:154@[0,5)` |
| `Label` · Propio en Linear Progress Bar | V001, V002, V003, V004, V013, V014, V015, V016, V025, V026, V027, V028, V037, V038, V039, V040 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 16 | `N357, N360, N363, N366, N393, N396, N399, N402, N429, N432, N435, N438, N465, N468, N471, N474`; `220:126@[0,5)` |
| `Percentage` · Propio en Linear Progress Bar | V005, V006, V007, V008, V009, V010, V011, V012, V017, V018, V019, V020, V021, V022, V023, V024, V029, V030, V031, V032, V033, V034, V035, V036, V041, V042, V043, V044, V045, V046, V047, V048 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 32 | `N370, N373, N376, N379, N382, N385, N388, N391, N406, N409, N412, N415, N418, N421, N424, N427, N442, N445, N448, N451, N454, N457, N460, N463, N478, N481, N484, N487, N490, N493, N496, N499`; `220:155@[0,3)` |
| `Percentage` · Propio en Linear Progress Bar | V001, V002, V003, V004, V013, V014, V015, V016, V025, V026, V027, V028, V037, V038, V039, V040 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 16 | `N358, N361, N364, N367, N394, N397, N400, N403, N430, N433, N436, N439, N466, N469, N472, N475`; `220:127@[0,3)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `220:124` | Linear Progress Bar → Type=Primary, Size=Small, Progress=25% |
| V002 | `220:131` | Linear Progress Bar → Type=Warning, Size=Small, Progress=25% |
| V003 | `220:138` | Linear Progress Bar → Type=Positive, Size=Small, Progress=25% |
| V004 | `220:145` | Linear Progress Bar → Type=Danger, Size=Small, Progress=25% |
| V005 | `220:152` | Linear Progress Bar → Type=Primary, Size=Medium, Progress=25% |
| V006 | `220:159` | Linear Progress Bar → Type=Warning, Size=Medium, Progress=25% |
| V007 | `220:166` | Linear Progress Bar → Type=Positive, Size=Medium, Progress=25% |
| V008 | `220:173` | Linear Progress Bar → Type=Danger, Size=Medium, Progress=25% |
| V009 | `220:180` | Linear Progress Bar → Type=Primary, Size=Large, Progress=25% |
| V010 | `220:187` | Linear Progress Bar → Type=Warning, Size=Large, Progress=25% |
| V011 | `220:194` | Linear Progress Bar → Type=Positive, Size=Large, Progress=25% |
| V012 | `220:201` | Linear Progress Bar → Type=Danger, Size=Large, Progress=25% |
| V013 | `220:208` | Linear Progress Bar → Type=Primary, Size=Small, Progress=50% |
| V014 | `220:215` | Linear Progress Bar → Type=Warning, Size=Small, Progress=50% |
| V015 | `220:222` | Linear Progress Bar → Type=Positive, Size=Small, Progress=50% |
| V016 | `220:229` | Linear Progress Bar → Type=Danger, Size=Small, Progress=50% |
| V017 | `220:236` | Linear Progress Bar → Type=Primary, Size=Medium, Progress=50% |
| V018 | `220:243` | Linear Progress Bar → Type=Warning, Size=Medium, Progress=50% |
| V019 | `220:250` | Linear Progress Bar → Type=Positive, Size=Medium, Progress=50% |
| V020 | `220:257` | Linear Progress Bar → Type=Danger, Size=Medium, Progress=50% |
| V021 | `220:264` | Linear Progress Bar → Type=Primary, Size=Large, Progress=50% |
| V022 | `220:271` | Linear Progress Bar → Type=Warning, Size=Large, Progress=50% |
| V023 | `220:278` | Linear Progress Bar → Type=Positive, Size=Large, Progress=50% |
| V024 | `220:285` | Linear Progress Bar → Type=Danger, Size=Large, Progress=50% |
| V025 | `220:292` | Linear Progress Bar → Type=Primary, Size=Small, Progress=75% |
| V026 | `220:299` | Linear Progress Bar → Type=Warning, Size=Small, Progress=75% |
| V027 | `220:306` | Linear Progress Bar → Type=Positive, Size=Small, Progress=75% |
| V028 | `220:313` | Linear Progress Bar → Type=Danger, Size=Small, Progress=75% |
| V029 | `220:320` | Linear Progress Bar → Type=Primary, Size=Medium, Progress=75% |
| V030 | `220:327` | Linear Progress Bar → Type=Warning, Size=Medium, Progress=75% |
| V031 | `220:334` | Linear Progress Bar → Type=Positive, Size=Medium, Progress=75% |
| V032 | `220:341` | Linear Progress Bar → Type=Danger, Size=Medium, Progress=75% |
| V033 | `220:348` | Linear Progress Bar → Type=Primary, Size=Large, Progress=75% |
| V034 | `220:355` | Linear Progress Bar → Type=Warning, Size=Large, Progress=75% |
| V035 | `220:362` | Linear Progress Bar → Type=Positive, Size=Large, Progress=75% |
| V036 | `220:369` | Linear Progress Bar → Type=Danger, Size=Large, Progress=75% |
| V037 | `220:376` | Linear Progress Bar → Type=Primary, Size=Small, Progress=100% |
| V038 | `220:383` | Linear Progress Bar → Type=Warning, Size=Small, Progress=100% |
| V039 | `220:390` | Linear Progress Bar → Type=Positive, Size=Small, Progress=100% |
| V040 | `220:397` | Linear Progress Bar → Type=Danger, Size=Small, Progress=100% |
| V041 | `220:404` | Linear Progress Bar → Type=Primary, Size=Medium, Progress=100% |
| V042 | `220:411` | Linear Progress Bar → Type=Warning, Size=Medium, Progress=100% |
| V043 | `220:418` | Linear Progress Bar → Type=Positive, Size=Medium, Progress=100% |
| V044 | `220:425` | Linear Progress Bar → Type=Danger, Size=Medium, Progress=100% |
| V045 | `220:432` | Linear Progress Bar → Type=Primary, Size=Large, Progress=100% |
| V046 | `220:439` | Linear Progress Bar → Type=Warning, Size=Large, Progress=100% |
| V047 | `220:446` | Linear Progress Bar → Type=Positive, Size=Large, Progress=100% |
| V048 | `220:453` | Linear Progress Bar → Type=Danger, Size=Large, Progress=100% |

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
