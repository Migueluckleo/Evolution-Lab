---
contract_schema: sdd-project/0.2
contract_id: BUTTON-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: BUTTON-001
amends_version: 0.2.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Button · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `BUTTON-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.2.0](button.contract.v0.2.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

Se mantienen las enmiendas previas: [button-page-name.amendment.md](button-page-name.amendment.md); [button.local-bindings.amendment.v0.2.2.md](button.local-bindings.amendment.v0.2.2.md); [button.semantic-scope-amendment.v0.2.1.md](button.semantic-scope-amendment.v0.2.1.md); [six-family-color.amendment.v0.1.0.md](six-family-color.amendment.v0.1.0.md).

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Los tipos primary/default/link y text conservan sus pesos diferenciados; el tipo link consume su estilo canónico con `textDecoration: UNDERLINE`, sin setter posterior de decoración. El tracking normal de botones dentro de Modal o Empty states es una excepción de esas composiciones, no una actualización del principal Button.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Buttons](../../sources/figma-snapshots/typography/census.before.0-1.json) | Página `0:1`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `01da10d9ffd1bea7e069b86b0a24da257e9630fba91564a205431f9f42446fb8`. |
| [Base histórica](button.contract.v0.2.0.md) | SHA-256 `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **60 nodos UI, 60 rangos, 6 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `label-text` · Propio en button | V008, V009, V011, V012, V020, V021, V023, V024, V032, V033, V035, V036, V044, V045, V047, V048, V056, V057, V059, V060 | `ui-action-label-medium` | `S:a52860fbc1e28ce8df19b58510e4bf0ffcb8fe75,` | 20 | `N0–N1, N3–N4, N12–N13, N15–N16, N24–N25, N27–N28, N36–N37, N39–N40, N48–N49, N51–N52`; `26:84@[0,7)` |
| `label-text` · Propio en button | V002, V003, V014, V015, V026, V027, V038, V039, V050, V051 | `ui-action-label-medium-underline` | `S:2624a7e4d78200617e44ac4360c72ed90514f244,` | 10 | `N6–N7, N18–N19, N30–N31, N42–N43, N54–N55`; `26:108@[0,7)` |
| `label-text` · Propio en button | V001, V010, V013, V022, V025, V034, V037, V046, V049, V058 | `ui-action-label-small` | `S:51bcebf78427882c8cf6b736692782f5b376d937,` | 10 | `N2, N5, N14, N17, N26, N29, N38, N41, N50, N53`; `26:92@[0,7)` |
| `label-text` · Propio en button | V004, V016, V028, V040, V055 | `ui-action-label-small-underline` | `S:c581c0973863bad4da806638b252d447e0a58ef5,` | 5 | `N8, N20, N32, N44, N59`; `26:116@[0,7)` |
| `label-text` · Propio en button | V005, V006, V017, V018, V029, V030, V041, V042, V052, V053 | `ui-action-text-medium` | `S:899870ed06666398e377ddd7c64e5cfa2d044c46,` | 10 | `N9–N10, N21–N22, N33–N34, N45–N46, N56–N57`; `26:120@[0,7)` |
| `label-text` · Propio en button | V007, V019, V031, V043, V054 | `ui-action-text-small` | `S:209d8601d6cf28513f7df8d0f3a53665dde66d3d,` | 5 | `N11, N23, N35, N47, N58`; `26:128@[0,7)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `26:102` | button → type=default, size=small, state=default |
| V002 | `26:106` | button → type=link, size=large, state=default |
| V003 | `26:110` | button → type=link, size=middle, state=default |
| V004 | `26:114` | button → type=link, size=small, state=default |
| V005 | `26:118` | button → type=text, size=large, state=default |
| V006 | `26:122` | button → type=text, size=middle, state=default |
| V007 | `26:126` | button → type=text, size=small, state=default |
| V008 | `26:130` | button → type=primary, size=large, state=hover |
| V009 | `26:134` | button → type=primary, size=middle, state=hover |
| V010 | `26:138` | button → type=primary, size=small, state=hover |
| V011 | `26:142` | button → type=default, size=large, state=hover |
| V012 | `26:146` | button → type=default, size=middle, state=hover |
| V013 | `26:150` | button → type=default, size=small, state=hover |
| V014 | `26:154` | button → type=link, size=large, state=hover |
| V015 | `26:158` | button → type=link, size=middle, state=hover |
| V016 | `26:162` | button → type=link, size=small, state=hover |
| V017 | `26:166` | button → type=text, size=large, state=hover |
| V018 | `26:170` | button → type=text, size=middle, state=hover |
| V019 | `26:174` | button → type=text, size=small, state=hover |
| V020 | `26:178` | button → type=primary, size=large, state=press |
| V021 | `26:182` | button → type=primary, size=middle, state=press |
| V022 | `26:186` | button → type=primary, size=small, state=press |
| V023 | `26:190` | button → type=default, size=large, state=press |
| V024 | `26:194` | button → type=default, size=middle, state=press |
| V025 | `26:198` | button → type=default, size=small, state=press |
| V026 | `26:202` | button → type=link, size=large, state=press |
| V027 | `26:206` | button → type=link, size=middle, state=press |
| V028 | `26:210` | button → type=link, size=small, state=press |
| V029 | `26:214` | button → type=text, size=large, state=press |
| V030 | `26:218` | button → type=text, size=middle, state=press |
| V031 | `26:222` | button → type=text, size=small, state=press |
| V032 | `26:226` | button → type=primary, size=large, state=focus |
| V033 | `26:230` | button → type=primary, size=middle, state=focus |
| V034 | `26:234` | button → type=primary, size=small, state=focus |
| V035 | `26:238` | button → type=default, size=large, state=focus |
| V036 | `26:243` | button → type=default, size=middle, state=focus |
| V037 | `26:248` | button → type=default, size=small, state=focus |
| V038 | `26:253` | button → type=link, size=large, state=focus |
| V039 | `26:257` | button → type=link, size=middle, state=focus |
| V040 | `26:261` | button → type=link, size=small, state=focus |
| V041 | `26:265` | button → type=text, size=large, state=focus |
| V042 | `26:269` | button → type=text, size=middle, state=focus |
| V043 | `26:273` | button → type=text, size=small, state=focus |
| V044 | `26:277` | button → type=primary, size=large, state=disabled |
| V045 | `26:281` | button → type=primary, size=middle, state=disabled |
| V046 | `26:285` | button → type=primary, size=small, state=disabled |
| V047 | `26:289` | button → type=default, size=large, state=disabled |
| V048 | `26:293` | button → type=default, size=middle, state=disabled |
| V049 | `26:297` | button → type=default, size=small, state=disabled |
| V050 | `26:301` | button → type=link, size=large, state=disabled |
| V051 | `26:305` | button → type=link, size=middle, state=disabled |
| V052 | `26:309` | button → type=text, size=large, state=disabled |
| V053 | `26:313` | button → type=text, size=middle, state=disabled |
| V054 | `26:317` | button → type=text, size=small, state=disabled |
| V055 | `26:321` | button → type=link, size=small, state=disabled |
| V056 | `26:82` | button → type=primary, size=large, state=default |
| V057 | `26:86` | button → type=primary, size=middle, state=default |
| V058 | `26:90` | button → type=primary, size=small, state=default |
| V059 | `26:94` | button → type=default, size=large, state=default |
| V060 | `26:98` | button → type=default, size=middle, state=default |

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
