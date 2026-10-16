---
contract_schema: sdd-project/0.2
contract_id: ICON-BUTTON-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: ICON-BUTTON-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# IconButton · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `ICON-BUTTON-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../icon-button.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [six-family-color.amendment.v0.1.0.md](six-family-color.amendment.v0.1.0.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

La ausencia de etiqueta textual de acción no hace esta familia NOT_APPLICABLE: los conteos de Dot, incluidos los ocultos, son consumidores tipográficos. La excepción de legibilidad y el nombre accesible independiente siguen vigentes.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Icon Buttons](../../sources/figma-snapshots/typography/census.before.183-160.json) | Página `183:160`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `85358f69021539ff07414f487968bec250a71f1fa62c68bd156021e07e5f8934`. |
| [Base histórica](../icon-button.contract.v0.1.0.md) | SHA-256 `928d083a785af74510ec0f320a362934f50bf239ffcea856ec83d91898e893cf`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **30 nodos UI, 30 rangos, 3 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Count label` · Instancia/Slot en Icon Button; referencia Dot | V003, V006, V009, V012, V015, V018, V021, V024, V027, V030 | `micro-count-large` | `S:04f6e44670660135688151fd5e03b58d2f72ba81,` | 10 | `N160, N163, N166, N169, N172, N175, N178, N181, N184, N187`; `I183:174;155:133@[0,1)` |
| `Count label` · Instancia/Slot en Icon Button; referencia Dot | V002, V005, V008, V011, V014, V017, V020, V023, V026, V029 | `micro-count-medium` | `S:f0c0dc4cd43b6d27d1c05ad262a09b29dd415bf1,` | 10 | `N159, N162, N165, N168, N171, N174, N177, N180, N183, N186`; `I183:169;155:135@[0,1)` |
| `Count label` · Instancia/Slot en Icon Button; referencia Dot | V001, V004, V007, V010, V013, V016, V019, V022, V025, V028 | `micro-count-small` | `S:2987fb55403e26b9fd23807ce894f58cc084820d,` | 10 | `N158, N161, N164, N167, N170, N173, N176, N179, N182, N185`; `I183:164;155:137@[0,1)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `183:161` | Icon Button → Style=Ghost, Size=Small, State=Default |
| V002 | `183:166` | Icon Button → Style=Ghost, Size=Medium, State=Default |
| V003 | `183:171` | Icon Button → Style=Ghost, Size=Large, State=Default |
| V004 | `183:176` | Icon Button → Style=Ghost, Size=Small, State=Disabled |
| V005 | `183:181` | Icon Button → Style=Ghost, Size=Medium, State=Disabled |
| V006 | `183:186` | Icon Button → Style=Ghost, Size=Large, State=Disabled |
| V007 | `183:191` | Icon Button → Style=Ghost, Size=Small, State=Hover |
| V008 | `183:196` | Icon Button → Style=Ghost, Size=Medium, State=Hover |
| V009 | `183:201` | Icon Button → Style=Ghost, Size=Large, State=Hover |
| V010 | `183:206` | Icon Button → Style=Ghost, Size=Small, State=Focus |
| V011 | `183:211` | Icon Button → Style=Ghost, Size=Medium, State=Focus |
| V012 | `183:216` | Icon Button → Style=Ghost, Size=Large, State=Focus |
| V013 | `183:221` | Icon Button → Style=Ghost, Size=Small, State=Active |
| V014 | `183:226` | Icon Button → Style=Ghost, Size=Medium, State=Active |
| V015 | `183:231` | Icon Button → Style=Ghost, Size=Large, State=Active |
| V016 | `183:236` | Icon Button → Style=Outline, Size=Small, State=Default |
| V017 | `183:241` | Icon Button → Style=Outline, Size=Medium, State=Default |
| V018 | `183:246` | Icon Button → Style=Outline, Size=Large, State=Default |
| V019 | `183:251` | Icon Button → Style=Outline, Size=Small, State=Disabled |
| V020 | `183:256` | Icon Button → Style=Outline, Size=Medium, State=Disabled |
| V021 | `183:261` | Icon Button → Style=Outline, Size=Large, State=Disabled |
| V022 | `183:266` | Icon Button → Style=Outline, Size=Small, State=Hover |
| V023 | `183:271` | Icon Button → Style=Outline, Size=Medium, State=Hover |
| V024 | `183:276` | Icon Button → Style=Outline, Size=Large, State=Hover |
| V025 | `183:281` | Icon Button → Style=Outline, Size=Small, State=Focus |
| V026 | `183:286` | Icon Button → Style=Outline, Size=Medium, State=Focus |
| V027 | `183:291` | Icon Button → Style=Outline, Size=Large, State=Focus |
| V028 | `183:296` | Icon Button → Style=Outline, Size=Small, State=Active |
| V029 | `183:301` | Icon Button → Style=Outline, Size=Medium, State=Active |
| V030 | `183:306` | Icon Button → Style=Outline, Size=Large, State=Active |

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
