---
contract_schema: sdd-project/0.2
contract_id: SIDEBAR-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: SIDEBAR-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Sidebar · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `SIDEBAR-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../sidebar.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Los labels regulares/activos, submenús AUTO y BETA conservan las identidades distintas de la tabla. Esta selección sustituye los nombres provisionales Sidebar/Label, Sidebar/Label Active, Sidebar/Submenu, Sidebar/Submenu Active y Sidebar/Release de §7 del contrato base por los IDs lógicos canónicos; no sustituye sus reglas de función o composición.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Sidebar](../../sources/figma-snapshots/typography/census.before.614-125.json) | Página `614:125`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `eb4641205014683f79eb2e9d146a077cc951d2995969cdc21205e00fed13be35`. |
| [Base histórica](../sidebar.contract.v0.1.0.md) | SHA-256 `6ddb3bb5e4166d5c53396d1b5f0bdac56e2bf431cce926050d818c726447cc8f`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **74 nodos UI, 74 rangos, 6 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `BETA` · Propio en Menu Item | V001 | `ui-sidebar-release` | `S:2aaadfa872db2d91b827f3dca6ce5c3588e9e86e,` | 1 | `N2984`; `615:360@[0,4)` |
| `Label` · Instancia/Slot en Menu Item; referencia Tooltip | V002, V003 | `ui-body-spacious` | `S:2e68e082c5bcf7f7f03fb21fe9f55b140c2bc134,` | 2 | `N2985–N2986`; `I615:376;87:139@[0,4)` |
| `Label` · Propio en Menu Item | V004, V011, V012, V014, V016, V018 | `ui-body-spacious` | `S:2e68e082c5bcf7f7f03fb21fe9f55b140c2bc134,` | 6 | `N2987, N2994–N2995, N2997, N2999, N3001`; `615:382@[0,4)` |
| `Label` · Propio en Menu Item | V006, V007 | `ui-navigation-emphasis-auto` | `S:cb57ef141d48f08f57ac520929ff687dfce22cef,` | 2 | `N2989–N2990`; `615:396@[0,4)` |
| `Label` · Propio en Menu Item | V005, V008 | `ui-navigation-label-auto` | `S:7b2bedcbf319948f84bd56c8a6e537e969be3f86,` | 2 | `N2988, N2991`; `615:389@[0,4)` |
| `Label` · Propio en Menu Item | V001, V009, V010, V013, V015, V017 | `ui-sidebar-label-active` | `S:c49296dee25b58bf5cb46e2ab7730a351093551b,` | 6 | `N2983, N2992–N2993, N2996, N2998, N3000`; `615:358@[0,4)` |
| `BETA` · Instancia/Slot en Sidebar; principal de texto no identificado en censo local | V020 | `ui-sidebar-release` | `S:2aaadfa872db2d91b827f3dca6ce5c3588e9e86e,` | 1 | `N3005`; `I619:500;7268:1070@[0,4)` |
| `Count label` · Instancia/Slot en Sidebar; referencia Dot | V019, V020 | `micro-count-small` | `S:2987fb55403e26b9fd23807ce894f58cc084820d,` | 2 | `N3002–N3003`; `I619:483;183:164;155:137@[0,1)` |
| `Label` · Instancia/Slot en Sidebar; principal de texto no identificado en censo local | V020 | `ui-body-spacious` | `S:2e68e082c5bcf7f7f03fb21fe9f55b140c2bc134,` | 7 | `N3009–N3015`; `I619:504;3290:2511@[0,4)` |
| `Label` · Instancia/Slot en Sidebar; principal de texto no identificado en censo local | V020 | `ui-navigation-emphasis-auto` | `S:cb57ef141d48f08f57ac520929ff687dfce22cef,` | 1 | `N3008`; `I619:503;3374:24402@[0,4)` |
| `Label` · Instancia/Slot en Sidebar; principal de texto no identificado en censo local | V020 | `ui-navigation-label-auto` | `S:7b2bedcbf319948f84bd56c8a6e537e969be3f86,` | 2 | `N3006–N3007`; `I619:501;3374:24367@[0,4)` |
| `Label` · Instancia/Slot en Sidebar; principal de texto no identificado en censo local | V020 | `ui-sidebar-label-active` | `S:c49296dee25b58bf5cb46e2ab7730a351093551b,` | 1 | `N3004`; `I619:500;3284:2422@[0,4)` |
| `Label` · Instancia/Slot en Top bar; principal de texto no identificado en censo local | V021 | `ui-body-spacious` | `S:2e68e082c5bcf7f7f03fb21fe9f55b140c2bc134,` | 3 | `N3017–N3019`; `I619:610;3365:23898@[0,4)` |
| `Label` · Instancia/Slot en Top bar; principal de texto no identificado en censo local | V021 | `ui-sidebar-label-active` | `S:c49296dee25b58bf5cb46e2ab7730a351093551b,` | 1 | `N3016`; `I619:609;3365:23866@[0,4)` |
| `BETA` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E001, E020 | `ui-sidebar-release` | `S:2aaadfa872db2d91b827f3dca6ce5c3588e9e86e,` | 2 | `N3024, N3067`; `I625:273;7268:1070@[0,4)` |
| `Count label` · Instancia/Slot en muestras de revisión; referencia Dot | E019, E020 | `micro-count-small` | `S:2987fb55403e26b9fd23807ce894f58cc084820d,` | 2 | `N3064–N3065`; `I625:488;3425:3674;183:164;155:137@[0,1)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Tooltip | E004, E005 | `ui-body-spacious` | `S:2e68e082c5bcf7f7f03fb21fe9f55b140c2bc134,` | 2 | `N3031, N3035`; `I625:316;5113:740;87:139@[0,4)` |
| `Label` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E006, E007, E008, E016, E017, E018, E020, E021 | `ui-body-spacious` | `S:2e68e082c5bcf7f7f03fb21fe9f55b140c2bc134,` | 16 | `N3038, N3040, N3042, N3058, N3060, N3062, N3071–N3077, N3080–N3082`; `I625:360;3290:2511@[0,4)` |
| `Label` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E011, E012, E020 | `ui-navigation-emphasis-auto` | `S:cb57ef141d48f08f57ac520929ff687dfce22cef,` | 3 | `N3048, N3050, N3070`; `I625:408;3374:24402@[0,4)` |
| `Label` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E009, E010, E020 | `ui-navigation-label-auto` | `S:7b2bedcbf319948f84bd56c8a6e537e969be3f86,` | 4 | `N3044, N3046, N3068–N3069`; `I625:388;3374:24367@[0,4)` |
| `Label` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E001, E002, E003, E013, E014, E015, E020, E021 | `ui-sidebar-label-active` | `S:c49296dee25b58bf5cb46e2ab7730a351093551b,` | 8 | `N3023, N3026, N3028, N3052, N3054, N3056, N3066, N3079`; `I625:273;3284:2422@[0,4)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `615:356` | Menu Item → orientation=vertical, type=expanded, status=default, isActive=true |
| V002 | `615:373` | Menu Item → orientation=vertical, type=collapsed, status=hover, isActive=true |
| V003 | `615:377` | Menu Item → orientation=vertical, type=collapsed, status=hover, isActive=false |
| V004 | `615:380` | Menu Item → orientation=vertical, type=expanded, status=default, isActive=false |
| V005 | `615:384` | Menu Item → orientation=vertical, type=sub-menu, status=default, isActive=false |
| V006 | `615:390` | Menu Item → orientation=vertical, type=sub-menu, status=default, isActive=true |
| V007 | `615:397` | Menu Item → orientation=vertical, type=sub-menu, status=hover, isActive=true |
| V008 | `615:404` | Menu Item → orientation=vertical, type=sub-menu, status=hover, isActive=false |
| V009 | `615:410` | Menu Item → orientation=vertical, type=expanded, status=hover, isActive=true |
| V010 | `615:415` | Menu Item → orientation=vertical, type=expanded, status=focus, isActive=true |
| V011 | `615:423` | Menu Item → orientation=vertical, type=expanded, status=hover, isActive=false |
| V012 | `615:427` | Menu Item → orientation=vertical, type=expanded, status=focus, isActive=false |
| V013 | `615:431` | Menu Item → orientation=horizontal, type=collapsed, status=default, isActive=true |
| V014 | `615:436` | Menu Item → orientation=horizontal, type=collapsed, status=default, isActive=false |
| V015 | `615:440` | Menu Item → orientation=horizontal, type=collapsed, status=hover, isActive=true |
| V016 | `615:445` | Menu Item → orientation=horizontal, type=collapsed, status=hover, isActive=false |
| V017 | `615:449` | Menu Item → orientation=horizontal, type=collapsed, status=focus, isActive=true |
| V018 | `615:454` | Menu Item → orientation=horizontal, type=collapsed, status=focus, isActive=false |
| V019 | `619:481` | Sidebar → Presentation=Collapsed |
| V020 | `619:496` | Sidebar → Presentation=Expanded |
| V021 | `619:607` | Top bar → Top bar |
| E001 | `625:273` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `625:285` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `625:295` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `625:316` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E005 | `625:342` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E006 | `625:360` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E007 | `625:369` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E008 | `625:378` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E009 | `625:388` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E010 | `625:397` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E011 | `625:408` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E012 | `625:418` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E013 | `625:430` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E014 | `625:440` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E015 | `625:450` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E016 | `625:461` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E017 | `625:470` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E018 | `625:479` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E019 | `625:488` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E020 | `625:523` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E021 | `625:603` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
