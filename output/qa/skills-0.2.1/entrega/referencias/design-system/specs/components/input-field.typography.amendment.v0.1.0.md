---
contract_schema: sdd-project/0.2
contract_id: INPUT-FIELD-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: INPUT-FIELD-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# InputField · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `INPUT-FIELD-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../input-field.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [input-field.disabled-text.amendment.v0.1.1.md](../input-field.disabled-text.amendment.v0.1.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Input Fields](../../sources/figma-snapshots/typography/census.before.394-122.json) | Página `394:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `80d4bb678b15ef6ffca912dfc290d700d1e65bcfe5c471c1b97f8abfcefcc827`. |
| [Base histórica](../input-field.contract.v0.1.0.md) | SHA-256 `e01e90d9dbc4dfdfc4230aac875f8d8a7374673b0a02bbda44eabf9962403c2d`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **150 nodos UI, 150 rangos, 4 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Helper` · Propio en Input Field | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018, V019, V020, V021, V022, V023, V024, V025, V026, V027, V028, V029, V030 | `ui-caption-compact` | `S:00ebc27da069f50e5d170d9e45cc9f392042a351,` | 30 | `N731, N736, N741, N746, N751, N756, N761, N766, N771, N776, N781, N786, N791, N796, N801, N806, N811, N816, N821, N826, N831, N836, N841, N846, N851, N856, N861, N866, N871, N876`; `395:221@[0,20)` |
| `Input text` · Propio en Input Field | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018, V019, V020, V021, V022, V023, V024, V025, V026, V027, V028, V029, V030 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 30 | `N729, N734, N739, N744, N749, N754, N759, N764, N769, N774, N779, N784, N789, N794, N799, N804, N809, N814, N819, N824, N829, N834, N839, N844, N849, N854, N859, N864, N869, N874`; `395:215@[0,16)` |
| `Label` · Propio en Input Field | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018, V019, V020, V021, V022, V023, V024, V025, V026, V027, V028, V029, V030 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 30 | `N727, N732, N737, N742, N747, N752, N757, N762, N767, N772, N777, N782, N787, N792, N797, N802, N807, N812, N817, N822, N827, N832, N837, N842, N847, N852, N857, N862, N867, N872`; `395:211@[0,5)` |
| `Prefix` · Propio en Input Field | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018, V019, V020, V021, V022, V023, V024, V025, V026, V027, V028, V029, V030 | `ui-field-prefix-compact` | `S:51ec5e79973ef8b0016006c053f3f26345bc08be,` | 30 | `N730, N735, N740, N745, N750, N755, N760, N765, N770, N775, N780, N785, N790, N795, N800, N805, N810, N815, N820, N825, N830, N835, N840, N845, N850, N855, N860, N865, N870, N875`; `395:217@[0,3)` |
| `Required` · Propio en Input Field | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018, V019, V020, V021, V022, V023, V024, V025, V026, V027, V028, V029, V030 | `ui-label-compact-bold` | `S:9c72f9fd7020cef8974458d27505fe7a151fc595,` | 30 | `N728, N733, N738, N743, N748, N753, N758, N763, N768, N773, N778, N783, N788, N793, N798, N803, N808, N813, N818, N823, N828, N833, N838, N843, N848, N853, N858, N863, N868, N873`; `395:212@[0,1)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `395:206` | Input Field → Size=Large, State=Default, Value=Empty |
| V002 | `395:222` | Input Field → Size=Medium, State=Default, Value=Empty |
| V003 | `395:238` | Input Field → Size=Small, State=Default, Value=Empty |
| V004 | `395:254` | Input Field → Size=Large, State=Success, Value=Empty |
| V005 | `395:270` | Input Field → Size=Medium, State=Success, Value=Empty |
| V006 | `395:286` | Input Field → Size=Small, State=Success, Value=Empty |
| V007 | `395:302` | Input Field → Size=Large, State=Error, Value=Empty |
| V008 | `395:318` | Input Field → Size=Medium, State=Error, Value=Empty |
| V009 | `395:334` | Input Field → Size=Small, State=Error, Value=Empty |
| V010 | `395:350` | Input Field → Size=Large, State=Focus, Value=Empty |
| V011 | `395:366` | Input Field → Size=Medium, State=Focus, Value=Empty |
| V012 | `395:382` | Input Field → Size=Small, State=Focus, Value=Empty |
| V013 | `395:398` | Input Field → Size=Large, State=Disabled, Value=Empty |
| V014 | `395:414` | Input Field → Size=Medium, State=Disabled, Value=Empty |
| V015 | `395:430` | Input Field → Size=Small, State=Disabled, Value=Empty |
| V016 | `395:446` | Input Field → Size=Large, State=Default, Value=Filled |
| V017 | `395:462` | Input Field → Size=Medium, State=Default, Value=Filled |
| V018 | `395:478` | Input Field → Size=Small, State=Default, Value=Filled |
| V019 | `395:494` | Input Field → Size=Large, State=Success, Value=Filled |
| V020 | `395:510` | Input Field → Size=Medium, State=Success, Value=Filled |
| V021 | `395:526` | Input Field → Size=Small, State=Success, Value=Filled |
| V022 | `395:542` | Input Field → Size=Large, State=Error, Value=Filled |
| V023 | `395:558` | Input Field → Size=Medium, State=Error, Value=Filled |
| V024 | `395:574` | Input Field → Size=Small, State=Error, Value=Filled |
| V025 | `395:590` | Input Field → Size=Large, State=Focus, Value=Filled |
| V026 | `395:606` | Input Field → Size=Medium, State=Focus, Value=Filled |
| V027 | `395:622` | Input Field → Size=Small, State=Focus, Value=Filled |
| V028 | `395:638` | Input Field → Size=Large, State=Disabled, Value=Filled |
| V029 | `395:654` | Input Field → Size=Medium, State=Disabled, Value=Filled |
| V030 | `395:670` | Input Field → Size=Small, State=Disabled, Value=Filled |

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
