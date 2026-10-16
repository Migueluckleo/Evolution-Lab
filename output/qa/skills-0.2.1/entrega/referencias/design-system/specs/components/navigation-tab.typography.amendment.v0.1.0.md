---
contract_schema: sdd-project/0.2
contract_id: NAVIGATION-TAB-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: NAVIGATION-TAB-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# NavigationTab · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `NAVIGATION-TAB-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../navigation-tab.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Se conservan las 17 combinaciones observadas, incluida Dynamic/On/Selected con etiqueta Regular. El conteo `number-large` es texto de una dependencia importada: se exige el estilo local indicado sobre el consumidor real, sin atribuir al censo un principal de texto local que no contiene.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Navigation](../../sources/figma-snapshots/typography/census.before.275-122.json) | Página `275:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `4aea717e82d2cd4cfb632e1656c93d2c44c03033e19239d6bee18ac6958dfe66`. |
| [Base histórica](../navigation-tab.contract.v0.1.0.md) | SHA-256 `1f28dbd13b0e5c055d2dc551e6a957b2b64f91701425d0b1089ef505c9b0035c`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **33 nodos UI, 33 rangos, 3 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Label` · Propio en Tab | V005, V006, V007, V008, V013, V014, V015, V016, V017 | `ui-navigation-label-auto` | `S:7b2bedcbf319948f84bd56c8a6e537e969be3f86,` | 9 | `N557, N559, N561, N563, N573, N575, N577, N579, N581`; `312:192@[0,9)` |
| `Label` · Propio en Tab | V001, V002, V003, V004, V009, V010, V011, V012 | `ui-navigation-tab-active` | `S:f37ecdfff1fd88d689b8d9b97c3676758a801561,` | 8 | `N549, N551, N553, N555, N565, N567, N569, N571`; `311:250@[0,9)` |
| `number-large` · Instancia/Slot en Tab; principal de texto no identificado en censo local | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016 | `micro-count-large` | `S:04f6e44670660135688151fd5e03b58d2f72ba81,` | 16 | `N550, N552, N554, N556, N558, N560, N562, N564, N566, N568, N570, N572, N574, N576, N578, N580`; `I311:251;1241:39860@[0,1)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `311:247` | Tab → Type=Base, Tab=On, State=Default |
| V002 | `312:169` | Tab → Type=Base, Tab=On, State=Hovered |
| V003 | `312:176` | Tab → Type=Base, Tab=On, State=Focused |
| V004 | `312:183` | Tab → Type=Base, Tab=On, State=Disabled |
| V005 | `312:190` | Tab → Type=Base, Tab=Off, State=Default |
| V006 | `312:197` | Tab → Type=Base, Tab=Off, State=Hovered |
| V007 | `312:204` | Tab → Type=Base, Tab=Off, State=Focused |
| V008 | `312:211` | Tab → Type=Base, Tab=Off, State=Disabled |
| V009 | `312:408` | Tab → Type=Dynamic, Tab=On, State=Default |
| V010 | `314:185` | Tab → Type=Dynamic, Tab=On, State=Hovered |
| V011 | `314:192` | Tab → Type=Dynamic, Tab=On, State=Focused |
| V012 | `314:199` | Tab → Type=Dynamic, Tab=On, State=Disabled |
| V013 | `314:207` | Tab → Type=Dynamic, Tab=Off, State=Default |
| V014 | `314:215` | Tab → Type=Dynamic, Tab=Off, State=Hovered |
| V015 | `314:223` | Tab → Type=Dynamic, Tab=Off, State=Focused |
| V016 | `314:231` | Tab → Type=Dynamic, Tab=Off, State=Disabled |
| V017 | `315:199` | Tab → Type=Dynamic, Tab=On, State=Selected |

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
