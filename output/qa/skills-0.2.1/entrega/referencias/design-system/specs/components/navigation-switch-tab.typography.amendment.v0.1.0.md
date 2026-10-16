---
contract_schema: sdd-project/0.2
contract_id: NAVIGATION-SWITCH-TAB-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: NAVIGATION-SWITCH-TAB-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# NavigationSwitchTab · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `NAVIGATION-SWITCH-TAB-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../navigation-switch-tab.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [composition-slots.amendment.v0.1.0.md](../composition-slots.amendment.v0.1.0.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Navigation](../../sources/figma-snapshots/typography/census.before.275-122.json) | Página `275:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `4aea717e82d2cd4cfb632e1656c93d2c44c03033e19239d6bee18ac6958dfe66`. |
| [Base histórica](../navigation-switch-tab.contract.v0.1.0.md) | SHA-256 `c9007112a7155c155a5fc32ee8e809fa28576005069c8964f3205e9f77fb4cf1`; reglas ajenas a esta sustitución preservadas. |
| [Identidad de muestras](../../qa/implementations/composition-slots.v0.1.0.switch-tab.json) | Relación de instancias de revisión con su familia; evidencia histórica, no nuevo PASS tipográfico. SHA-256 `bf0f951241e15b4bdf3d18d9f47055e2ff59b6f37fc24b98104abb845dfd3e82`. |

Cobertura de este corte: **36 nodos UI, 36 rangos, 3 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Count label` · Instancia/Slot en Switch Tab; referencia Dot | V001 | `micro-count-medium` | `S:f0c0dc4cd43b6d27d1c05ad262a09b29dd415bf1,` | 4 | `N513, N515, N517, N519`; `I283:129;276:184;155:135@[0,1)` |
| `Label` · Instancia/Slot en Switch Tab; referencia Switch Tab Item | V001 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 3 | `N514, N516, N518`; `I283:136;276:191@[0,9)` |
| `Label` · Instancia/Slot en Switch Tab; referencia Switch Tab Item | V001 | `ui-navigation-switch-active` | `S:394b4cb7f577fc48ce5ab91e4bbd16f6f381ccc8,` | 1 | `N512`; `I283:129;276:183@[0,9)` |
| `Count label` · Instancia/Slot en muestras de revisión; referencia Dot | E001, E002, E003, E004 | `micro-count-medium` | `S:f0c0dc4cd43b6d27d1c05ad262a09b29dd415bf1,` | 14 | `N583, N585, N587, N589, N591, N593, N595, N597, N599, N601, N603, N605, N607, N609`; `I469:206;468:206;469:241;276:184;155:135@[0,1)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Switch Tab Item | E002, E003, E004 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 10 | `N586, N590, N592, N594, N596, N600, N602, N604, N606, N608`; `I469:244;468:206;469:280;276:191@[0,9)` |
| `Label` · Instancia/Slot en muestras de revisión; referencia Switch Tab Item | E001, E002, E003, E004 | `ui-navigation-switch-active` | `S:394b4cb7f577fc48ce5ab91e4bbd16f6f381ccc8,` | 4 | `N582, N584, N588, N598`; `I469:206;468:206;469:241;276:183@[0,9)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `283:128` | Switch Tab → Switch Tab |
| E001 | `469:206` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `469:244` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `469:282` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `469:316` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
