---
contract_schema: sdd-project/0.2
contract_id: SELECT-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: SELECT-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
scaled_link_readiness: BLOCKED
slot_applicability: NOT_APPLICABLE
---

# Select · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `SELECT-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../select.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [composition-slots.amendment.v0.1.0.md](../composition-slots.amendment.v0.1.0.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

La composición hereda Input Field, Dropdown Item y Checkbox. Las etiquetas escaladas se comprueban por rango en el consumidor; aplicar el estilo del Checkbox principal y restablecer su tamaño no satisface esta enmienda. El Slot Options conserva cardinalidad abierta.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Select](../../sources/figma-snapshots/typography/census.before.444-122.json) | Página `444:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `96efb819732bb62b75a4cc5489a9a59a45b9de94f6fbc05decf97e67704af95c`. |
| [Base histórica](../select.contract.v0.1.0.md) | SHA-256 `baa34a17eb5c1674e16d0a5e736b5b09c5be73cfb4d9e48a1257dce8896065fa`; reglas ajenas a esta sustitución preservadas. |
| [Identidad de muestras](../../implementations/figma/composition-slots.v0.1.0.state.json) | Relación de instancias de revisión con su familia; evidencia histórica, no nuevo PASS tipográfico. SHA-256 `53d0df1de3d2745fa4aff861c610dd3d803fd6509ad2a27ae11b1a084ff3f7b5`. |
| [Identidad de muestras](../../implementations/figma/select.v0.1.0.state.json) | Relación de instancias de revisión con su familia; evidencia histórica, no nuevo PASS tipográfico. SHA-256 `c28c12620c06927a9000aa0e21c59d2f11ea363ad29584e44327b5af42d9d0ab`. |

Cobertura de este corte: **168 nodos UI, 168 rangos, 5 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

**Preparación de aplicación 0.1.1:** 64 rangos de esta familia están `UNRESOLVED_SCALED_LINK` en el mapping, con acción `NO_WRITE_PENDING_SCALE_BINDING_RESOLUTION`. La identidad normativa está definida, pero el vínculo explícito de esos rangos sigue bloqueado; conservar métricas no satisface el requisito. Los 104 rangos restantes requieren su propio preflight y lectura final. La [enmienda de formato](../foundations/typography.formatting.amendment.v0.1.1.md) explica el límite observado; esta tabla no autoriza cambiar escala ni geometría para ocultarlo.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Helper` · Instancia/Slot en Select; referencia Input Field | V001, V002 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 2 | `N1099, N1124`; `I456:403;395:221@[0,20)` |
| `Input text` · Instancia/Slot en Select; referencia Input Field | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 2 | `N1097, N1122`; `I456:403;395:215@[0,21)` |
| `Label` · Instancia/Slot en Select; referencia Dropdown Item | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 10 | `N1102, N1106, N1110, N1114, N1118, N1127, N1131, N1135, N1139, N1143`; `I466:602;446:170@[0,11)` |
| `Label` · Instancia/Slot en Select; referencia Input Field | V001, V002 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 2 | `N1095, N1120`; `I456:403;395:211@[0,9)` |
| `Left label` · Instancia/Slot en Select; referencia Checkbox | V001, V002 | `ui-checkbox-label-scaled-five-sixths` | `S:2974d901ccb47912070340154abb5290d567f8ac,` | 10 | `N1100, N1104, N1108, N1112, N1116, N1125, N1129, N1133, N1137, N1141`; `I466:602;446:167;149:180@[0,11)` |
| `Prefix` · Instancia/Slot en Select; referencia Input Field | V001, V002 | `ui-field-prefix-compact` | `S:51ec5e79973ef8b0016006c053f3f26345bc08be,` | 2 | `N1098, N1123`; `I456:403;395:217@[0,3)` |
| `Required` · Instancia/Slot en Select; referencia Input Field | V001, V002 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 2 | `N1096, N1121`; `I456:403;395:212@[0,1)` |
| `Right label` · Instancia/Slot en Select; referencia Checkbox | V001, V002 | `ui-checkbox-label-scaled-five-sixths` | `S:2974d901ccb47912070340154abb5290d567f8ac,` | 10 | `N1101, N1105, N1109, N1113, N1117, N1126, N1130, N1134, N1138, N1142`; `I466:602;446:167;149:183@[0,11)` |
| `Secondary text` · Instancia/Slot en Select; referencia Dropdown Item | V001, V002 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 10 | `N1103, N1107, N1111, N1115, N1119, N1128, N1132, N1136, N1140, N1144`; `I466:602;446:171@[0,10)` |
| `Helper` · Instancia/Slot en muestras de revisión; referencia Input Field | E001, E002, E003, E004, E005, E006 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 6 | `N1149, N1174, N1183, N1200, N1225, N1262`; `I458:470;456:422;395:461@[0,20)` |
| `Input text` · Instancia/Slot en muestras de revisión; referencia Input Field | E001, E002, E003, E004, E005, E006 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 6 | `N1147, N1172, N1181, N1198, N1223, N1260`; `I458:470;456:422;395:455@[0,21)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Dropdown Item | E001, E002, E004, E005, E006 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 22 | `N1152, N1156, N1160, N1164, N1168, N1177, N1186, N1190, N1194, N1203, N1207, N1211, N1215, N1219, N1228, N1232, N1236, N1240, N1244, N1248, N1252, N1256`; `I458:470;456:441;446:170@[0,56)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Input Field | E001, E002, E003, E004, E005, E006 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 6 | `N1145, N1170, N1179, N1196, N1221, N1258`; `I458:470;456:422;395:451@[0,9)` |
| `Left label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E001, E002, E004, E005, E006 | `ui-checkbox-label-scaled-five-sixths` | `S:2974d901ccb47912070340154abb5290d567f8ac,` | 22 | `N1150, N1154, N1158, N1162, N1166, N1175, N1184, N1188, N1192, N1201, N1205, N1209, N1213, N1217, N1226, N1230, N1234, N1238, N1242, N1246, N1250, N1254`; `I458:470;456:441;446:167;149:180@[0,11)` |
| `Prefix` · Instancia/Slot en muestras de revisión; referencia Input Field | E001, E002, E003, E004, E005, E006 | `ui-field-prefix-compact` | `S:51ec5e79973ef8b0016006c053f3f26345bc08be,` | 6 | `N1148, N1173, N1182, N1199, N1224, N1261`; `I458:470;456:422;395:457@[0,3)` |
| `Required` · Instancia/Slot en muestras de revisión; referencia Input Field | E001, E002, E003, E004, E005, E006 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 6 | `N1146, N1171, N1180, N1197, N1222, N1259`; `I458:470;456:422;395:452@[0,1)` |
| `Right label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E001, E002, E004, E005, E006 | `ui-checkbox-label-scaled-five-sixths` | `S:2974d901ccb47912070340154abb5290d567f8ac,` | 22 | `N1151, N1155, N1159, N1163, N1167, N1176, N1185, N1189, N1193, N1202, N1206, N1210, N1214, N1218, N1227, N1231, N1235, N1239, N1243, N1247, N1251, N1255`; `I458:470;456:441;446:167;149:183@[0,11)` |
| `Secondary text` · Instancia/Slot en muestras de revisión; referencia Dropdown Item | E001, E002, E004, E005, E006 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 22 | `N1153, N1157, N1161, N1165, N1169, N1178, N1187, N1191, N1195, N1204, N1208, N1212, N1216, N1220, N1229, N1233, N1237, N1241, N1245, N1249, N1253, N1257`; `I458:470;456:441;446:171@[0,10)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `456:402` | Select → Presentation=Closed |
| V002 | `456:421` | Select → Presentation=Open |
| E001 | `458:470` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `467:1052` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `467:1239` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `467:688` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E005 | `467:811` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E006 | `467:934` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

Una referencia compartida de propiedad de componente no unifica roles tipográficos. Una asignación solo es conforme si los rangos de esta tabla y los consumidores relacionados siguen resolviendo su estilo esperado después de la última escritura. No usar un setter posterior que desvincule silenciosamente el TextStyle. El contenido, color, visibilidad y formato semántico conservan su contrato. Cuando el catálogo declara `textDecoration`, ese formato procede del TextStyle y no de un setter posterior; una igualdad visual sin `textStyleId` no prueba cumplimiento.

Derivados presentes: `ui-checkbox-label-scaled-five-sixths`. Conservar `derivedFrom` del catálogo, `recipeScale=1` y el `instanceScale` observado del mapping; no aplicar dos veces el factor ni promoverlos a tamaños generales.

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
