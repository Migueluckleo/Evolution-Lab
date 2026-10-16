---
contract_schema: sdd-project/0.2
contract_id: TOGGLE-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: TOGGLE-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Toggle · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `TOGGLE-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../../drafts/contracts/toggle.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [toggle.focus-effect-amendment.v0.1.3.md](toggle.focus-effect-amendment.v0.1.3.md); [toggle.mixed-amendment.v0.1.4.md](toggle.mixed-amendment.v0.1.4.md); [toggle.source-color-amendment.v0.1.5.md](toggle.source-color-amendment.v0.1.5.md); [toggle.visual-contrast-amendment.v0.1.2.md](toggle.visual-contrast-amendment.v0.1.2.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Toggles](../../sources/figma-snapshots/typography/census.before.111-122.json) | Página `111:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `0316fccc7e5ec144a692343e0d150276eee88cd059bcf7ebe546708fb11df295`. |
| [Base histórica](../../drafts/contracts/toggle.contract.v0.1.0.md) | SHA-256 `c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **24 nodos UI, 24 rangos, 1 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Left label` · Propio en Toggle | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012 | `ui-field-prefix-compact` | `S:51ec5e79973ef8b0016006c053f3f26345bc08be,` | 12 | `N60, N62, N64, N66, N68, N70, N72, N74, N76, N78, N80, N82`; `111:124@[0,11)` |
| `Right label` · Propio en Toggle | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012 | `ui-field-prefix-compact` | `S:51ec5e79973ef8b0016006c053f3f26345bc08be,` | 12 | `N61, N63, N65, N67, N69, N71, N73, N75, N77, N79, N81, N83`; `111:127@[0,11)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `111:123` | Toggle → Toggle=On, State=Default |
| V002 | `111:128` | Toggle → Toggle=On, State=Hover |
| V003 | `111:133` | Toggle → Toggle=On, State=Focus |
| V004 | `111:138` | Toggle → Toggle=On, State=Disabled |
| V005 | `111:143` | Toggle → Toggle=Off, State=Default |
| V006 | `111:148` | Toggle → Toggle=Off, State=Hover |
| V007 | `111:153` | Toggle → Toggle=Off, State=Focus |
| V008 | `111:158` | Toggle → Toggle=Off, State=Disabled |
| V009 | `232:122` | Toggle → Toggle=Mixed, State=Default |
| V010 | `232:128` | Toggle → Toggle=Mixed, State=Hover |
| V011 | `232:134` | Toggle → Toggle=Mixed, State=Focus |
| V012 | `232:140` | Toggle → Toggle=Mixed, State=Disabled |

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
