---
contract_schema: sdd-project/0.2
contract_id: STEPPER-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: STEPPER-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Stepper · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `STEPPER-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../stepper.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [stepper.brand-theme.amendment.v0.1.1.md](../stepper.brand-theme.amendment.v0.1.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Steppers](../../sources/figma-snapshots/typography/census.before.347-122.json) | Página `347:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `0ac10669f775bb66d4743e6ff09f2cfef08a72c560fb455917173e7ccc4db7e2`. |
| [Base histórica](../stepper.contract.v0.1.0.md) | SHA-256 `5c3f8d75fe20736fd08411654db5757ea9517af6dd6b078234a17627bac19466`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **54 nodos UI, 54 rangos, 2 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Caption` · Propio en Stepper Item | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018 | `ui-stepper-caption` | `S:df912e1588c72a69e31e731f1c57f0398d103761,` | 18 | `N673, N676, N679, N682, N685, N688, N691, N694, N697, N700, N703, N706, N709, N712, N715, N718, N721, N724`; `350:164@[0,7)` |
| `Step` · Propio en Stepper Item | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018 | `ui-stepper-caption` | `S:df912e1588c72a69e31e731f1c57f0398d103761,` | 18 | `N671, N674, N677, N680, N683, N686, N689, N692, N695, N698, N701, N704, N707, N710, N713, N716, N719, N722`; `350:162@[0,6)` |
| `Title` · Propio en Stepper Item | V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011, V012, V013, V014, V015, V016, V017, V018 | `ui-stepper-title` | `S:ce17b35d63371c1ee82cc804b301c5644efe4b6e,` | 18 | `N672, N675, N678, N681, N684, N687, N690, N693, N696, N699, N702, N705, N708, N711, N714, N717, N720, N723`; `350:163@[0,12)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `350:155` | Stepper Item → Orientation=Horizontal, State=Checked, Position=Start |
| V002 | `350:165` | Stepper Item → Orientation=Horizontal, State=Checked, Position=Middle |
| V003 | `350:177` | Stepper Item → Orientation=Horizontal, State=Checked, Position=End |
| V004 | `350:187` | Stepper Item → Orientation=Horizontal, State=Default, Position=Start |
| V005 | `350:197` | Stepper Item → Orientation=Horizontal, State=Default, Position=Middle |
| V006 | `350:209` | Stepper Item → Orientation=Horizontal, State=Default, Position=End |
| V007 | `350:219` | Stepper Item → Orientation=Horizontal, State=Inactive, Position=Start |
| V008 | `350:229` | Stepper Item → Orientation=Horizontal, State=Inactive, Position=Middle |
| V009 | `350:241` | Stepper Item → Orientation=Horizontal, State=Inactive, Position=End |
| V010 | `350:251` | Stepper Item → Orientation=Vertical, State=Checked, Position=Start |
| V011 | `350:261` | Stepper Item → Orientation=Vertical, State=Checked, Position=Middle |
| V012 | `350:273` | Stepper Item → Orientation=Vertical, State=Checked, Position=End |
| V013 | `350:283` | Stepper Item → Orientation=Vertical, State=Default, Position=Start |
| V014 | `350:293` | Stepper Item → Orientation=Vertical, State=Default, Position=Middle |
| V015 | `350:305` | Stepper Item → Orientation=Vertical, State=Default, Position=End |
| V016 | `350:315` | Stepper Item → Orientation=Vertical, State=Inactive, Position=Start |
| V017 | `350:325` | Stepper Item → Orientation=Vertical, State=Inactive, Position=Middle |
| V018 | `350:337` | Stepper Item → Orientation=Vertical, State=Inactive, Position=End |

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
