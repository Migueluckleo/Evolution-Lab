---
contract_schema: sdd-project/0.2
contract_id: NAVIGATION-PAGINATION-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: NAVIGATION-PAGINATION-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# NavigationPagination · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `NAVIGATION-PAGINATION-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../navigation-pagination.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [composition-slots.amendment.v0.1.1.md](../composition-slots.amendment.v0.1.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Navigation](../../sources/figma-snapshots/typography/census.before.275-122.json) | Página `275:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `4aea717e82d2cd4cfb632e1656c93d2c44c03033e19239d6bee18ac6958dfe66`. |
| [Base histórica](../navigation-pagination.contract.v0.1.0.md) | SHA-256 `314ad6b95a6938aa1c6527b22b867f8714d21bbf138a21956333d43c8f40c0ee`; reglas ajenas a esta sustitución preservadas. |
| [Identidad de muestras](../../qa/implementations/composition-slots.v0.1.1.pagination.json) | Relación de instancias de revisión con su familia; evidencia histórica, no nuevo PASS tipográfico. SHA-256 `6657f3a0b5b537aeb97aaae936cf8e95660046ad5e7a4d8f4b9761ca15e26d02`. |

Cobertura de este corte: **68 nodos UI, 68 rangos, 2 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Ellipsis label` · Propio en Pagination | V001, V002, V003, V004, V005 | `body-semibold` | `S:4ee45102c701e2a111b2c448495a18fd46e6a8c8,` | 5 | `N525, N530, N535, N540, N545`; `291:314@[0,3)` |
| `Items per page label` · Propio en Pagination | V001, V002, V003, V004, V005 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 5 | `N528, N533, N538, N543, N548`; `291:327@[0,10)` |
| `Page 1 label` · Propio en Pagination | V001, V002, V003, V004, V005 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 5 | `N524, N529, N534, N539, N544`; `291:312@[0,1)` |
| `Page 2 label` · Propio en Pagination | V001, V002, V003, V004, V005 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 5 | `N526, N531, N536, N541, N546`; `291:316@[0,1)` |
| `Page 3 label` · Propio en Pagination | V001, V002, V003, V004, V005 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 5 | `N527, N532, N537, N542, N547`; `291:318@[0,1)` |
| `Ellipsis label` · Instancia/Slot en muestras de revisión; referencia Pagination | E002, E003, E004, E005, E006 | `body-semibold` | `S:4ee45102c701e2a111b2c448495a18fd46e6a8c8,` | 5 | `N611, N616, N621, N626, N631`; `I499:334;291:314@[0,3)` |
| `Items per page label` · Instancia/Slot en muestras de revisión; referencia Pagination | E001, E002, E003, E004, E005, E006, E007 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 7 | `N614, N619, N624, N629, N634, N643, N652`; `I499:334;291:327@[0,10)` |
| `Page 1 label` · Instancia/Slot en muestras de revisión; referencia Pagination | E002, E003, E004, E005, E006 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 5 | `N610, N615, N620, N625, N630`; `I499:334;291:312@[0,1)` |
| `Page 1 label` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E001, E007 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 6 | `N635–N636, N641, N644–N645, N650`; `I499:624;291:310;499:685@[0,1)` |
| `Page 2 label` · Instancia/Slot en muestras de revisión; referencia Pagination | E002, E003, E004, E005, E006 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 5 | `N612, N617, N622, N627, N632`; `I499:334;291:316@[0,1)` |
| `Page 2 label` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E001, E007 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 8 | `N638–N640, N642, N647–N649, N651`; `I499:624;291:310;499:667@[0,1)` |
| `Page 3 label` · Instancia/Slot en muestras de revisión; referencia Pagination | E002, E003, E004, E005, E006 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 5 | `N613, N618, N623, N628, N633`; `I499:334;291:318@[0,1)` |
| `Page 3 label` · Instancia/Slot en muestras de revisión; principal de texto no identificado en censo local | E001, E007 | `body-regular` | `S:ba9f7a5c3e8665f41e72f8b1317a9cc36e4714aa,` | 2 | `N637, N646`; `I499:624;291:310;499:665@[0,1)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `291:301` | Pagination → State=Default |
| V002 | `297:122` | Pagination → State=Active |
| V003 | `297:147` | Pagination → State=Hover |
| V004 | `297:172` | Pagination → State=Focus |
| V005 | `297:197` | Pagination → State=Disabled |
| E001 | `499:1264` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `499:334` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `499:363` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `499:392` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E005 | `499:421` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E006 | `499:450` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E007 | `499:624` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
