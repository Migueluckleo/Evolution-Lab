---
contract_schema: sdd-project/0.2
contract_id: FILTER-CHIP-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: FILTER-CHIP-001
amends_version: 0.2.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# FilterChip · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `FILTER-CHIP-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.2.0](filter-chip.contract.v0.2.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [filter-chip.semantic.amendment.v0.2.1.md](filter-chip.semantic.amendment.v0.2.1.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Chips](../../sources/figma-snapshots/typography/census.before.67-122.json) | Página `67:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `bfbae0f2615152190aeef9f9ea75afc00e0ff85de4f2672d129e4de374863d2f`. |
| [Base histórica](filter-chip.contract.v0.2.0.md) | SHA-256 `325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **30 nodos UI, 30 rangos, 3 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Label` · Propio en Filter Chip | V001, V022, V023, V024, V025, V026, V027, V028, V029, V030 | `ui-chip-label-large` | `S:a1b9b3b0c48341d7c06114963c96ab0b2170f7ac,` | 10 | `N3116, N3137–N3145`; `70:125@[0,4)` |
| `Label` · Propio en Filter Chip | V012, V013, V014, V015, V016, V017, V018, V019, V020, V021 | `ui-chip-label-middle` | `S:cbc9125e6f78d23635d88782fad6fefddf462d39,` | 10 | `N3127–N3136`; `72:164@[0,4)` |
| `Label` · Propio en Filter Chip | V002, V003, V004, V005, V006, V007, V008, V009, V010, V011 | `ui-chip-label-small` | `S:916f48478d785ab2b7fbae4c789b036435f670eb,` | 10 | `N3117–N3126`; `72:124@[0,4)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `70:122` | Filter Chip → size=large, selected=false, state=default |
| V002 | `72:122` | Filter Chip → size=small, selected=false, state=default |
| V003 | `72:126` | Filter Chip → size=small, selected=false, state=hover |
| V004 | `72:130` | Filter Chip → size=small, selected=false, state=press |
| V005 | `72:134` | Filter Chip → size=small, selected=false, state=focus |
| V006 | `72:138` | Filter Chip → size=small, selected=false, state=disabled |
| V007 | `72:142` | Filter Chip → size=small, selected=true, state=default |
| V008 | `72:146` | Filter Chip → size=small, selected=true, state=hover |
| V009 | `72:150` | Filter Chip → size=small, selected=true, state=press |
| V010 | `72:154` | Filter Chip → size=small, selected=true, state=focus |
| V011 | `72:158` | Filter Chip → size=small, selected=true, state=disabled |
| V012 | `72:162` | Filter Chip → size=middle, selected=false, state=default |
| V013 | `72:166` | Filter Chip → size=middle, selected=false, state=hover |
| V014 | `72:170` | Filter Chip → size=middle, selected=false, state=press |
| V015 | `72:174` | Filter Chip → size=middle, selected=false, state=focus |
| V016 | `72:178` | Filter Chip → size=middle, selected=false, state=disabled |
| V017 | `72:182` | Filter Chip → size=middle, selected=true, state=default |
| V018 | `72:186` | Filter Chip → size=middle, selected=true, state=hover |
| V019 | `72:190` | Filter Chip → size=middle, selected=true, state=press |
| V020 | `72:194` | Filter Chip → size=middle, selected=true, state=focus |
| V021 | `72:198` | Filter Chip → size=middle, selected=true, state=disabled |
| V022 | `72:202` | Filter Chip → size=large, selected=false, state=hover |
| V023 | `72:206` | Filter Chip → size=large, selected=false, state=press |
| V024 | `72:210` | Filter Chip → size=large, selected=false, state=focus |
| V025 | `72:214` | Filter Chip → size=large, selected=false, state=disabled |
| V026 | `72:218` | Filter Chip → size=large, selected=true, state=default |
| V027 | `72:222` | Filter Chip → size=large, selected=true, state=hover |
| V028 | `72:226` | Filter Chip → size=large, selected=true, state=press |
| V029 | `72:230` | Filter Chip → size=large, selected=true, state=focus |
| V030 | `72:234` | Filter Chip → size=large, selected=true, state=disabled |

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
