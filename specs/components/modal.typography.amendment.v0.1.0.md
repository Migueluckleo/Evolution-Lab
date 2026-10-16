---
contract_schema: sdd-project/0.2
contract_id: MODAL-TYPOGRAPHY-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
amends: MODAL-001
amends_version: 0.1.0
typography_applicability: REQUIRED
implementation_validation: REQUIRES_FINAL_READBACK
slot_applicability: NOT_APPLICABLE
---

# Modal · consumo tipográfico · enmienda 0.1.0

## Alcance y autoridad

La solicitud explícita del usuario del 2026-10-15 exige aplicar estilos compartidos a todos los componentes y documentar las tipografías de cada Spec. Esta enmienda adopta, por delegación específica de esa tarea, las identidades de la tabla para `MODAL-001`. Auditoría humana `PENDING`; no equivale a aprobación humana ni a consumo Figma validado. Rigen las [reglas transversales](../TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) y la [enmienda de formato 0.1.1](../foundations/typography.formatting.amendment.v0.1.1.md).

Complementa el [contrato base 0.1.0](../modal.contract.v0.1.0.md) y sustituye exclusivamente la identificación del estilo tipográfico por consumidor: los valores aislados o nombres provisionales quedan referidos al estilo lógico canónico. Conserva contenido, color, geometría, semántica, variantes, formato de enlace y excepciones documentadas. Los archivos históricos no se reescriben.

P-SLOTS `NOT_APPLICABLE` a este ajuste de identidad tipográfica; la aplicabilidad de composición de la familia continúa según su contrato y enmiendas. No se añaden regiones, máximos, variantes ni anatomía por asignar un TextStyle.

Los rangos de Subtitle text y Link text comparten receta métrica, pero preservan contenido, formato de enlace y colores separados. Los botones anidados usan la identidad contextual de la tabla; no propagarla al principal Button. Los Slots siguen siendo los del contrato vigente.

## Fuentes y cobertura

| Fuente | Identidad y localizador |
|---|---|
| [Catálogo canónico](../tokens/ai-design-system.typography.v0.1.1.json) | `styles[id]`: receta, unidades, tokens y única `description`. SHA-256 `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`. |
| [Mapa de identidades Figma](../../implementations/figma/typography.v0.1.1.catalog.state.json) | `styleMap[styleLogicalId]`, destino `tj3WIBEZDGLVs7MJWKCwgf`; IDs observados, no deducidos por nombre. SHA-256 `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0`. |
| [Mapping de consumidores](../../implementations/figma/typography.v0.1.1.mapping.json) | `nodes` y `segments`; SHA-256 `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d`. Intención de aplicación, no readback de consumo. |
| [Censo de Modal](../../sources/figma-snapshots/typography/census.before.565-122.json) | Página `565:122`; `components`, `nodes`, `recipes` y `columns` del esquema 2. SHA-256 `64e0b8ba1b81b69908fcc399fb6b883f1cd254c67667d5ae6315249ef592d869`. |
| [Base histórica](../modal.contract.v0.1.0.md) | SHA-256 `589a78693d2bad3f3d9233a8ea6ecd5e9254f1aae429aac6da941b030cc78f57`; reglas ajenas a esta sustitución preservadas. |

Cobertura de este corte: **96 nodos UI, 98 rangos, 4 estilos lógicos**. Incluye textos ocultos y dependencias anidadas en el contexto de esta familia. El inventario de 43 familias y la conciliación global están en la enmienda transversal.

## Texto y variante → estilo requerido

Cada fila selecciona exactamente los registros `N` indicados del array `nodes` del mapping congelado (índice base cero), y dentro de ellos los segmentos cuyo `styleLogicalId` coincide con la fila. Los intervalos `N…–N…` son inclusivos. La referencia `nodeId@[start,end)` es un ejemplo verificable; la selección `N` incluye todos los rangos, no solo el ejemplo. Los códigos `V` identifican principales/variantes reales y `E` instancias de revisión sin `ownerComponentId`. No representan combinaciones cartesianas inferidas.

| Texto / ubicación | Variante o contexto observado | ID lógico requerido | Figma TextStyle ID observado | Rangos | Localizador exacto y ejemplo |
|---|---|---|---|---:|---|
| `Link text` · Propio en __Modal/Header | V001, V002 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 2 | `N2881, N2884`; `566:245@[0,9)` |
| `Subtitle text` · Propio en __Modal/Header | V001, V002 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 2 | `N2880, N2883`; `566:244@[0,34)` |
| `Title` · Propio en __Modal/Header | V001, V002 | `ui-modal-title` | `S:cb4052453d42d5ce9ce98f08640582004d80f602,` | 2 | `N2879, N2882`; `566:240@[0,11)` |
| `label-text` · Instancia/Slot en __Modal/Footer; referencia button | V003, V004 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 4 | `N2885–N2888`; `I566:263;26:100@[0,9)` |
| `Content` · Propio en __Modal/Content example | V005 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 1 | `N2889`; `566:282@[0,19)` |
| `Link text` · Instancia/Slot en Modal / Basic; referencia __Modal/Header | V006, V007, V008, V009, V010, V011 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 6 | `N2892, N2897, N2902, N2907, N2912, N2917`; `I567:140;566:245@[0,9)` |
| `Subtitle text` · Instancia/Slot en Modal / Basic; referencia __Modal/Header | V006, V007, V008, V009, V010, V011 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 6 | `N2891, N2896, N2901, N2906, N2911, N2916`; `I567:140;566:244@[0,34)` |
| `Title` · Instancia/Slot en Modal / Basic; referencia __Modal/Header | V006, V007, V008, V009, V010, V011 | `ui-modal-title` | `S:cb4052453d42d5ce9ce98f08640582004d80f602,` | 6 | `N2890, N2895, N2900, N2905, N2910, N2915`; `I567:140;566:240@[0,11)` |
| `label-text` · Instancia/Slot en Modal / Basic; referencia button | V006, V007, V008, V009, V010, V011 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 12 | `N2893–N2894, N2898–N2899, N2903–N2904, N2908–N2909, N2913–N2914, N2918–N2919`; `I567:152;566:263;26:100@[0,9)` |
| `Content` · Propio en Modal / Media | V012 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 2 | `N2921`; `569:305@[0,102)` |
| `Left label` · Instancia/Slot en Modal / Media; referencia Checkbox | V012 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N2922`; `I569:306;566:259;569:323;149:180@[0,11)` |
| `Right label` · Instancia/Slot en Modal / Media; referencia Checkbox | V012 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N2923`; `I569:306;566:259;569:323;149:183@[0,16)` |
| `Title` · Propio en Modal / Media | V012 | `ui-modal-title` | `S:cb4052453d42d5ce9ce98f08640582004d80f602,` | 1 | `N2920`; `569:304@[0,11)` |
| `label-text` · Instancia/Slot en Modal / Media; referencia button | V012 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 2 | `N2924–N2925`; `I569:306;566:263;26:100@[0,9)` |
| `Content` · Instancia/Slot en Modal / SideBySide; referencia __Modal/Side note | V013 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N2929`; `I569:343;566:276;569:366;569:360@[0,17)` |
| `Link text` · Instancia/Slot en Modal / SideBySide; referencia __Modal/Header | V013 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 1 | `N2928`; `I569:330;566:245@[0,9)` |
| `Subtitle text` · Instancia/Slot en Modal / SideBySide; referencia __Modal/Header | V013 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 1 | `N2927`; `I569:330;566:244@[0,34)` |
| `Title` · Instancia/Slot en Modal / SideBySide; referencia __Modal/Header | V013 | `ui-modal-title` | `S:cb4052453d42d5ce9ce98f08640582004d80f602,` | 1 | `N2926`; `I569:330;566:240@[0,11)` |
| `label-text` · Instancia/Slot en Modal / SideBySide; referencia button | V013 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 2 | `N2930–N2931`; `I569:343;566:278;26:100@[0,9)` |
| `Content` · Propio en __Modal/Side note | V014 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N2932`; `569:360@[0,17)` |
| `Content` · Instancia/Slot en muestras de revisión; referencia __Modal/Side note | E008 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N2980`; `I578:498;569:343;569:366;569:360@[0,17)` |
| `Content` · Instancia/Slot en muestras de revisión; referencia Modal / Media | E007 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 2 | `N2971`; `I578:472;569:305@[0,102)` |
| `Left label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E007 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N2972`; `I578:472;569:306;569:323;149:180@[0,11)` |
| `Link text` · Instancia/Slot en muestras de revisión; referencia __Modal/Header | E001, E002, E003, E004, E005, E006, E008 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 7 | `N2936, N2942, N2948, N2954, N2960, N2966, N2979`; `I578:305;567:140;566:245@[0,9)` |
| `Right label` · Instancia/Slot en muestras de revisión; referencia Checkbox | E007 | `ui-body-compact` | `S:1e79e86d57bf4121e3824ddf6dc9cf0a2466d947,` | 1 | `N2973`; `I578:472;569:306;569:323;149:183@[0,16)` |
| `Subtitle text` · Instancia/Slot en muestras de revisión; referencia __Modal/Header | E001, E002, E003, E004, E005, E006, E008 | `ui-content-large` | `S:8d38f6a5868e5d5e0366907a63e27299dbac2c50,` | 7 | `N2935, N2941, N2947, N2953, N2959, N2965, N2978`; `I578:305;567:140;566:244@[0,34)` |
| `Title` · Instancia/Slot en muestras de revisión; referencia __Modal/Header | E001, E002, E003, E004, E005, E006, E008 | `ui-modal-title` | `S:cb4052453d42d5ce9ce98f08640582004d80f602,` | 7 | `N2934, N2940, N2946, N2952, N2958, N2964, N2977`; `I578:305;567:140;566:240@[0,11)` |
| `Title` · Instancia/Slot en muestras de revisión; referencia Modal / Media | E007 | `ui-modal-title` | `S:cb4052453d42d5ce9ce98f08640582004d80f602,` | 1 | `N2970`; `I578:472;569:304@[0,11)` |
| `label-text` · Instancia/Slot en muestras de revisión; referencia button | E001, E002, E003, E004, E005, E006, E007, E008 | `ui-action-label-normal` | `S:cd0499b3ec8aac327af4d4f8cb4d500018288525,` | 16 | `N2937–N2938, N2943–N2944, N2949–N2950, N2955–N2956, N2961–N2962, N2967–N2968, N2974–N2975, N2981–N2982`; `I578:305;567:152;566:263;26:100@[0,9)` |

Los nombres de nodo son localizadores observados, no textos obligatorios de producto. El contenido editable puede cambiar sin cambiar el rol. Las recetas y el uso general se consultan en `styles[id].description`; esta tabla no mantiene valores tipográficos editables paralelos.

## Principales, variantes y referencias de muestra

| Clave | ID observado | Contexto real |
|---|---|---|
| V001 | `566:238` | __Modal/Header → Scroll=No |
| V002 | `566:249` | __Modal/Header → Scroll=Yes |
| V003 | `566:258` | __Modal/Footer → Scroll=No |
| V004 | `566:275` | __Modal/Footer → Scroll=Yes |
| V005 | `566:281` | __Modal/Content example → __Modal/Content example |
| V006 | `567:139` | Modal / Basic → Size=Small, Scroll=No |
| V007 | `567:163` | Modal / Basic → Size=Small, Scroll=Yes |
| V008 | `567:220` | Modal / Basic → Size=Medium, Scroll=No |
| V009 | `567:244` | Modal / Basic → Size=Medium, Scroll=Yes |
| V010 | `567:290` | Modal / Basic → Size=Large, Scroll=No |
| V011 | `567:314` | Modal / Basic → Size=Large, Scroll=Yes |
| V012 | `569:301` | Modal / Media → Modal / Media |
| V013 | `569:327` | Modal / SideBySide → Modal / SideBySide |
| V014 | `569:357` | __Modal/Side note → __Modal/Side note |
| E001 | `578:305` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E002 | `578:331` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E003 | `578:357` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E004 | `578:384` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E005 | `578:413` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E006 | `578:442` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E007 | `578:472` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |
| E008 | `578:498` | Instancia de revisión de esta familia, sin owner en el censo. Conservar la ruta `nodeId` de cada registro; no atribuirle una variante por el nombre de la página. |

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
