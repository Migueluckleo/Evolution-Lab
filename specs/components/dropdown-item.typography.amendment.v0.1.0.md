---
contract_schema: sdd-project/0.2
contract_id: DROPDOWN-ITEM-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: DROPDOWN-ITEM-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
scaled_link_readiness: BLOCKED
slot_applicability: NOT_APPLICABLE
---

# DropdownItem · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `DROPDOWN-ITEM-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../dropdown-item.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Las etiquetas de Checkbox anidado conservan sus estilos derivados en los contextos escalados. `recipeScale=1` evita volver a escalar la receta materializada; `instanceScale` describe la composición existente. Esto no añade tamaños públicos de Checkbox.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Select](../../sources/figma-snapshots/typography/census.before.444-122.json) | Página `444:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `96efb819732bb62b75a4cc5489a9a59a45b9de94f6fbc05decf97e67704af95c`. |
| [Base histórica](../dropdown-item.contract.v0.1.0.md) | SHA-256 `414040f481f994316406dfd61ca09a4c5a52b4b9ec97e30dcb2a1dc90ef27d42`; reglas ajenas a esta sustitución preservadas. |
| [Identidad de muestras](../../qa/implementations/dropdown-item.v0.1.0.integration.json) | Relación de instancias de revisión con su familia; evidencia histórica, no nuevo PASS tipográfico. SHA-256 `e006687cc2ab0d7274f3f4d2e6168645c55bc9c3df340c576f3c2b47acbc86f8`. |

Cobertura de este corte: **124 nodos UI, 124 rangos, 4 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

**Preparación de aplicación 0.1.1:** 26 rangos de esta familia están `UNRESOLVED_SCALED_LINK` en el mapping, con acción `NO_WRITE_PENDING_SCALE_BINDING_RESOLUTION`. La identidad normativa está definida, pero el vínculo explícito de esos rangos sigue bloqueado; conservar métricas no satisface el requisito. Los 98 rangos restantes requieren su propio preflight y lectura final. La [enmienda de formato](../foundations/typography.formatting.amendment.v0.1.1.md) explica el límite observado; esta tabla no autoriza cambiar escala ni geometría para ocultarlo.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Label` · Propio en Dropdown Item | V003, V004, V005, V006, V008, V009, V011, V012, V014, V015, V017, V018 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 12 | `N973, N977, N981, N985, N993, N997, N1005, N1009, N1017, N1021, N1029, N1033`; `446:170@[0,11)` |
| `Label` · Propio en Dropdown Item | V001, V002, V007, V010, V013, V016 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 6 | `N965, N969, N989, N1001, N1013, N1025`; `446:132@[0,11)` |
| `Left label` · Instancia/Slot en Dropdown Item; referencia Checkbox | V001, V002, V007, V010, V013, V016 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 6 | `N963, N967, N987, N999, N1011, N1023`; `I446:124;149:180@[0,11)` |
| `Left label` · Instancia/Slot en Dropdown Item; referencia Checkbox | V003, V004, V008, V011, V014, V017 | `ui-checkbox-label-scaled-five-sixths` | `S:2974d901ccb47912070340154abb5290d567f8ac,` | 6 | `N971, N975, N991, N1003, N1015, N1027`; `I446:167;149:180@[0,11)` |
| `Left label` · Instancia/Slot en Dropdown Item; referencia Checkbox | V005, V006, V009, V012, V015, V018 | `ui-checkbox-label-scaled-two-thirds` | `S:b26c73d6d7eed2bde7c20d7a413f9673856b0750,` | 6 | `N979, N983, N995, N1007, N1019, N1031`; `I446:207;149:180@[0,11)` |
| `Right label` · Instancia/Slot en Dropdown Item; referencia Checkbox | V001, V002, V007, V010, V013, V016 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 6 | `N964, N968, N988, N1000, N1012, N1024`; `I446:124;149:183@[0,11)` |
| `Right label` · Instancia/Slot en Dropdown Item; referencia Checkbox | V003, V004, V008, V011, V014, V017 | `ui-checkbox-label-scaled-five-sixths` | `S:2974d901ccb47912070340154abb5290d567f8ac,` | 6 | `N972, N976, N992, N1004, N1016, N1028`; `I446:167;149:183@[0,11)` |
| `Right label` · Instancia/Slot en Dropdown Item; referencia Checkbox | V005, V006, V009, V012, V015, V018 | `ui-checkbox-label-scaled-two-thirds` | `S:b26c73d6d7eed2bde7c20d7a413f9673856b0750,` | 6 | `N980, N984, N996, N1008, N1020, N1032`; `I446:207;149:183@[0,11)` |
| `Secondary text` · Propio en Dropdown Item | V003, V004, V005, V006, V008, V009, V011, V012, V014, V015, V017, V018 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 12 | `N974, N978, N982, N986, N994, N998, N1006, N1010, N1018, N1022, N1030, N1034`; `446:171@[0,10)` |
| `Secondary text` · Propio en Dropdown Item | V001, V002, V007, V010, V013, V016 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 6 | `N966, N970, N990, N1002, N1014, N1026`; `446:133@[0,10)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Dropdown Item | E013 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N1089`; `I448:569;446:210@[0,53)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Dropdown Item | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011, E012 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 12 | `N1038, N1042, N1046, N1051, N1055, N1059, N1064, N1068, N1072, N1077, N1081, N1085`; `I448:315;446:132@[0,17)` |
| `Left label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011, E012 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 12 | `N1036, N1040, N1044, N1049, N1053, N1057, N1062, N1066, N1070, N1075, N1079, N1083`; `I448:315;446:124;149:180@[0,11)` |
| `Left label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E013 | `ui-checkbox-label-scaled-two-thirds` | `S:b26c73d6d7eed2bde7c20d7a413f9673856b0750,` | 1 | `N1087`; `I448:569;446:207;149:180@[0,11)` |
| `Right label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011, E012 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 12 | `N1037, N1041, N1045, N1050, N1054, N1058, N1063, N1067, N1071, N1076, N1080, N1084`; `I448:315;446:124;149:183@[0,11)` |
| `Right label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E013 | `ui-checkbox-label-scaled-two-thirds` | `S:b26c73d6d7eed2bde7c20d7a413f9673856b0750,` | 1 | `N1088`; `I448:569;446:207;149:183@[0,11)` |
| `Secondary text` · Instancia/Slot en muestras de revisión; referencia Dropdown Item | E013 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N1090`; `I448:569;446:211@[0,10)` |
| `Secondary text` · Instancia/Slot en muestras de revisión; referencia Dropdown Item | E001, E002, E003, E004, E005, E006, E007, E008, E009, E010, E011, E012 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 12 | `N1039, N1043, N1047, N1052, N1056, N1060, N1065, N1069, N1073, N1078, N1082, N1086`; `I448:315;446:133@[0,7)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `446:122` | Dropdown Item → Size=Large, State=Default, Selected=False, Type=Base |
| V002 | `446:145` | Dropdown Item → Size=Large, State=Default, Selected=False, Type=Header |
| V003 | `446:165` | Dropdown Item → Size=Medium, State=Default, Selected=False, Type=Base |
| V004 | `446:185` | Dropdown Item → Size=Medium, State=Default, Selected=False, Type=Header |
| V005 | `446:205` | Dropdown Item → Size=Small, State=Default, Selected=False, Type=Base |
| V006 | `446:225` | Dropdown Item → Size=Small, State=Default, Selected=False, Type=Header |
| V007 | `446:245` | Dropdown Item → Size=Large, State=Hover, Selected=False, Type=Base |
| V008 | `446:269` | Dropdown Item → Size=Medium, State=Hover, Selected=False, Type=Base |
| V009 | `446:293` | Dropdown Item → Size=Small, State=Hover, Selected=False, Type=Base |
| V010 | `446:317` | Dropdown Item → Size=Large, State=Disabled, Selected=False, Type=Base |
| V011 | `446:341` | Dropdown Item → Size=Medium, State=Disabled, Selected=False, Type=Base |
| V012 | `446:365` | Dropdown Item → Size=Small, State=Disabled, Selected=False, Type=Base |
| V013 | `446:389` | Dropdown Item → Size=Large, State=Default, Selected=True, Type=Base |
| V014 | `446:416` | Dropdown Item → Size=Medium, State=Default, Selected=True, Type=Base |
| V015 | `446:442` | Dropdown Item → Size=Small, State=Default, Selected=True, Type=Base |
| V016 | `446:468` | Dropdown Item → Size=Large, State=Focus, Selected=False, Type=Base |
| V017 | `446:488` | Dropdown Item → Size=Medium, State=Focus, Selected=False, Type=Base |
| V018 | `446:508` | Dropdown Item → Size=Small, State=Focus, Selected=False, Type=Base |
| E001 | `448:315` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `448:335` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `448:355` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `448:379` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E005 | `448:399` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E006 | `448:419` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E007 | `448:443` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E008 | `448:463` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E009 | `448:483` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E010 | `448:507` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E011 | `448:527` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E012 | `448:547` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E013 | `448:569` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

Una referencia compartida de propiedad de componente no unifica roles tipográficos. Una asignación solo es conforme si los rangos de esta tabla y los consumidores relacionados siguen resolviendo su estilo esperado después de la última escritura. No usar un setter posterior que desvincule silenciosamente el TextStyle. El contenido, color, visibilidad y formato semántico conservan su contrato. Cuando el catálogo declara `textDecoration`, ese formato procede del TextStyle y no de un setter posterior; una igualdad visual sin `textStyleId` no prueba cumplimiento.

Derivados presentes: `ui-checkbox-label-scaled-five-sixths`, `ui-checkbox-label-scaled-two-thirds`. Conservar `derivedFrom` del catálogo, `recipeScale=1` y el `instanceScale` observado del mapping; no aplicar dos veces el factor ni promoverlos a tamaños generales.

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
