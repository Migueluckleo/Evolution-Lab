---
contract_schema: sdd-project/0.2
contract_id: TYPOGRAPHY-CONSUMPTION-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-15
review_targets: [figma, web]
slot_applicability: NOT_APPLICABLE
implementation_validation: REQUIRES_FINAL_READBACK
---

# Consumo tipográfico · 43 familias · enmienda 0.1.0

## Decisión específica y sustitución

La solicitud explícita del usuario del 2026-10-15 exige aplicar los estilos a **todos los componentes Figma** y documentar en cada Spec qué tipografías requiere. Esa solicitud delega esta aplicación y su documentación; no es aprobación humana de cada detalle. La auditoría humana permanece `PENDING`. Esta enmienda y las 43 enmiendas de familia que enlaza son el paquete normativo de esa solicitud, con versiones históricas intactas.

Complementa [FOUNDATIONS-TYPOGRAPHY-001](foundations/typography.contract.v0.1.0.md) y su [decisión de catálogo](../registry/DEC-TYPOGRAPHY-STYLES-001.md), con la [enmienda de formato 0.1.1](foundations/typography.formatting.amendment.v0.1.1.md). Sustituye exclusivamente la ausencia de identidad de TextStyle, los nombres provisionales y las asignaciones tipográficas expresamente identificadas en cada enmienda. No crea otra escala, otra `description`, variables, recetas, variantes ni reglas de composición. Las normas base y sus enmiendas anteriores conservan todo lo que no se sustituye aquí.

El alcance adopta las recetas canónicas ya documentadas para conservar el diseño existente. Las tablas son decisiones de asignación por consumidor; el censo y el mapping aportan evidencia `OBSERVED`/`DERIVED`, no aprobación por sí mismos. Los IDs reales Figma son bindings de implementación verificados por lectura. Las tablas los transcriben para hacer comprobable el destino, sin convertirlos en una segunda receta editable.

## Propiedad de datos y fuentes congeladas

| Fuente | Campos propios / función | SHA-256 del corte |
|---|---|---|
| [ai-design-system.typography.v0.1.1.json](tokens/ai-design-system.typography.v0.1.1.json) | Única receta, unidades, tokenRefs y description por estilo; 79 estilos. | `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd` |
| [typography.v0.1.1.mapping.json](../implementations/figma/typography.v0.1.1.mapping.json) | Selección exacta de nodos/rangos y estilo lógico esperado; intención de aplicación, no prueba de persistencia. | `4a44eeab4e9839eed71ec90e50a4a106a312545edfad912b43c284a7612ae73d` |
| [typography.v0.1.1.catalog.state.json](../implementations/figma/typography.v0.1.1.catalog.state.json) | styleMap lógico→TextStyle ID real del destino; no acredita consumo de los componentes. | `de4aca0f6b0a7e74cf038c53e4c538cd90a167c900639208fc3eddb5865e85d0` |
| [components.registry.json](../implementations/web/components.registry.json) | Universo de 43 familias, base y enmiendas previas consultadas; el registro no sustituye el contrato. | `e8c19e4145e0bac2cab2bb857a920bdde5063835fe6e1741ff6ab7437333c499` |

Los censos `sources/figma-snapshots/typography/census.before.<page-id>.json` quedan enlazados con hash en cada enmienda. El esquema 2 se interpreta mediante `columns`; las identidades de componentes/variantes proceden de `components`. El mapping incluye los hashes de sus fuentes. Las tablas usan índices `N` base cero de ese mapping exacto, con intervalos inclusivos y filtro de `styleLogicalId`; si cambia el mapping, sus localizadores se revalidan y se versionan, no se reutilizan por posición.

## Requisitos transversales

| ID | Requisito |
|---|---|
| TYC-01 | Todo rango TEXT/TEXTPATH de UI en principales, variantes e instancias censadas debe resolver el estilo lógico y el TextStyle ID de su enmienda, aunque esté oculto. Un ID vacío/ajeno o una receta incompatible impide validar ese consumidor. |
| TYC-02 | Mantener la receta canónica y los bindings aplicables, con las unidades originales y la codificación float32 declarada en foundations. No aceptar tolerancias improvisadas, igualdad visual o un ID rodeado de overrides incompatibles como cumplimiento. |
| TYC-02b | El subrayado de los 27 rangos declarados pertenece a cuatro TextStyles específicos. Aplicar el estilo completo por rango y preservar formato; no restaurar decoración con un setter posterior que rompa el vínculo o propague estilos entre textos. |
| TYC-03 | Conservar la función de cada texto: etiqueta, título, metadato, conteo, iniciales, enlace o contenido. Compartir receta o componentPropertyReferences no permite sustituir el estilo de otros rangos ni cambiar su semántica. |
| TYC-04 | Separar el texto propio del principal de las dependencias anidadas. Una excepción contextual se aplica al consumidor indicado; no se propaga al main de la dependencia. Las referencias heredadas se comprueban otra vez tras el último cambio global. |
| TYC-05 | Preservar contenido, formato semántico (por ejemplo UNDERLINE), color, propiedades, Slots, variantes, instancias y geometría. Una reparación estructural necesaria exige mapa de IDs anteriores/nuevos, preservación de la API y QA de sus consumidores; esta tabla no acredita esa reparación. |
| TYC-06 | Los tres derivados materializados conservan derivedFrom e instanceScale; recipeScale=1. No escalar de nuevo sus métricas ni usarlos como tamaños generales. |
| TYC-07 | En un Slot, los componentes insertados conservan su contrato tipográfico. Para texto local nuevo se selecciona un estilo base entre los 18 según description y función; no se fuerza ese catálogo base sobre recetas compactas existentes ni se impone una receta única al Slot. |
| TYC-08 | Artwork vectorial y familias sin texto reciben NOT_APPLICABLE justificado. Los textos editoriales fuera de componentes se mantienen separados. Excluirlos no permite omitir un texto oculto, una muestra instanciada o una dependencia remota consumida por UI. |
| TYC-09 | La aceptación usa lectura exhaustiva posterior a la última escritura y pruebas de propiedades/variantes compartidas. Separar estilos, consumo, preservación, documentación, web y distribución; conservar los FAIL/BLOCKED históricos y registrar la evidencia nueva. |

P-SLOTS es `NOT_APPLICABLE` a la definición de esta asignación; cada familia mantiene la aplicabilidad y anatomía de sus Slots vigentes. P07 exige coherencia documental/web de cualquier cambio efectivo de receta o API. P08 y Graphify se cierran por el lote del cambio; no los acredita este documento.

## Cobertura explícita por familia

El censo de entrada contiene **34 páginas, 3501 nodos y 3503 rangos**: 3351 nodos/3353 rangos UI y 150 textos editoriales. Las 43 familias ocupan 33 páginas; la página separadora `----` no contiene texto. La asignación por familia usa el principal/ComponentSet real en las páginas compartidas Navigation, Input Fields, Select y Chat. Las muestras sin owner se resuelven mediante sus ledgers/QA de identidad o la ruta a un texto principal real, no por analogía de nombres.

El conteo siguiente asigna cada registro UI una sola vez a su contexto anfitrión del censo. Una dependencia puede aparecer además en su propia familia con otros nodeIds; es consumo en distintos contextos, no doble conteo del mismo registro.

| Familia / Spec de consumo | Base vigente consultada | Página | Aplicabilidad | Nodos UI | Rangos | Estilos |
|---|---|---|---|---:|---:|---:|
| [BUTTON-001 · Button](components/button.typography.amendment.v0.1.0.md) | [button.contract.v0.2.0.md](components/button.contract.v0.2.0.md) | `0:1` | REQUIRED | 60 | 60 | 6 |
| [ICON-BUTTON-001 · IconButton](components/icon-button.typography.amendment.v0.1.0.md) | [icon-button.contract.v0.1.0.md](icon-button.contract.v0.1.0.md) | `183:160` | REQUIRED | 30 | 30 | 3 |
| [FILTER-CHIP-001 · FilterChip](components/filter-chip.typography.amendment.v0.1.0.md) | [filter-chip.contract.v0.2.0.md](components/filter-chip.contract.v0.2.0.md) | `67:122` | REQUIRED | 30 | 30 | 3 |
| [BADGE-001 · Badge](components/badge.typography.amendment.v0.1.0.md) | [badge.contract.v0.1.0.md](components/badge.contract.v0.1.0.md) | `94:122` | REQUIRED | 6 | 6 | 1 |
| [DOT-001 · Dot](components/dot.typography.amendment.v0.1.0.md) | [dot.contract.v0.1.0.md](components/dot.contract.v0.1.0.md) | `155:122` | REQUIRED | 6 | 6 | 3 |
| [INLINE-NOTIFICATION-001 · InlineNotification](components/inline-notification.typography.amendment.v0.1.0.md) | [inline-notification.contract.v0.1.0.md](components/inline-notification.contract.v0.1.0.md) | `175:391` | REQUIRED | 10 | 10 | 2 |
| [LINEAR-PROGRESS-BAR-001 · LinearProgressBar](components/linear-progress-bar.typography.amendment.v0.1.0.md) | [linear-progress-bar.contract.v0.1.0.md](linear-progress-bar.contract.v0.1.0.md) | `220:122` | REQUIRED | 144 | 144 | 2 |
| [LOADER-001 · Loader](components/loader.typography.amendment.v0.1.0.md) | [loader.contract.v0.1.0.md](loader.contract.v0.1.0.md) | `377:122` | NOT_APPLICABLE | 0 | 0 | 0 |
| [TOOLTIP-001 · Tooltip](components/tooltip.typography.amendment.v0.1.0.md) | [tooltip.contract.v0.1.0.md](../drafts/contracts/tooltip.contract.v0.1.0.md) | `85:122` | REQUIRED | 4 | 4 | 1 |
| [INPUT-FIELD-001 · InputField](components/input-field.typography.amendment.v0.1.0.md) | [input-field.contract.v0.1.0.md](input-field.contract.v0.1.0.md) | `394:122` | REQUIRED | 150 | 150 | 4 |
| [TEXTAREA-001 · Textarea](components/textarea.typography.amendment.v0.1.0.md) | [textarea.contract.v0.1.0.md](textarea.contract.v0.1.0.md) | `394:122` | REQUIRED | 16 | 16 | 4 |
| [CHECKBOX-001 · Checkbox](components/checkbox.typography.amendment.v0.1.0.md) | [checkbox.contract.v0.1.0.md](checkbox.contract.v0.1.0.md) | `149:122` | REQUIRED | 24 | 24 | 1 |
| [RADIO-BUTTON-001 · RadioButton](components/radio-button.typography.amendment.v0.1.0.md) | [radio-button.contract.v0.1.0.md](radio-button.contract.v0.1.0.md) | `142:122` | REQUIRED | 16 | 16 | 1 |
| [TOGGLE-001 · Toggle](components/toggle.typography.amendment.v0.1.0.md) | [toggle.contract.v0.1.0.md](../drafts/contracts/toggle.contract.v0.1.0.md) | `111:122` | REQUIRED | 24 | 24 | 1 |
| [SEARCH-001 · Search](components/search.typography.amendment.v0.1.0.md) | [search.contract.v0.1.1.md](search.contract.v0.1.1.md) | `394:122` | REQUIRED | 24 | 24 | 2 |
| [SELECT-001 · Select](components/select.typography.amendment.v0.1.0.md) | [select.contract.v0.1.0.md](select.contract.v0.1.0.md) | `444:122` | REQUIRED | 168 | 168 | 5 |
| [DROPDOWN-ITEM-001 · DropdownItem](components/dropdown-item.typography.amendment.v0.1.0.md) | [dropdown-item.contract.v0.1.0.md](dropdown-item.contract.v0.1.0.md) | `444:122` | REQUIRED | 124 | 124 | 4 |
| [FILEUPLOAD-001 · FileUpload](components/file-upload.typography.amendment.v0.1.0.md) | [file-upload.contract.v0.1.0.md](file-upload.contract.v0.1.0.md) | `394:122` | REQUIRED | 32 | 32 | 6 |
| [BREADCRUMBS-001 · Breadcrumbs](components/breadcrumbs.typography.amendment.v0.1.0.md) | [breadcrumbs.contract.v0.1.0.md](breadcrumbs.contract.v0.1.0.md) | `190:188` | REQUIRED | 36 | 36 | 2 |
| [NAVIGATION-PAGINATION-001 · NavigationPagination](components/navigation-pagination.typography.amendment.v0.1.0.md) | [navigation-pagination.contract.v0.1.0.md](navigation-pagination.contract.v0.1.0.md) | `275:122` | REQUIRED | 68 | 68 | 2 |
| [NAVIGATION-SWITCH-TAB-001 · NavigationSwitchTab](components/navigation-switch-tab.typography.amendment.v0.1.0.md) | [navigation-switch-tab.contract.v0.1.0.md](navigation-switch-tab.contract.v0.1.0.md) | `275:122` | REQUIRED | 36 | 36 | 3 |
| [NAVIGATION-SWITCH-TAB-ITEM-001 · NavigationSwitchTabItem](components/navigation-switch-tab-item.typography.amendment.v0.1.0.md) | [navigation-switch-tab-item.contract.v0.1.0.md](navigation-switch-tab-item.contract.v0.1.0.md) | `275:122` | REQUIRED | 6 | 6 | 3 |
| [NAVIGATION-TAB-001 · NavigationTab](components/navigation-tab.typography.amendment.v0.1.0.md) | [navigation-tab.contract.v0.1.0.md](navigation-tab.contract.v0.1.0.md) | `275:122` | REQUIRED | 33 | 33 | 3 |
| [STEPS-001 · Steps](components/steps.typography.amendment.v0.1.0.md) | [steps.contract.v0.1.0.md](steps.contract.v0.1.0.md) | `341:122` | REQUIRED | 18 | 18 | 2 |
| [STEPPER-001 · Stepper](components/stepper.typography.amendment.v0.1.0.md) | [stepper.contract.v0.1.0.md](stepper.contract.v0.1.0.md) | `347:122` | REQUIRED | 54 | 54 | 2 |
| [AVATAR-001 · Avatar](components/avatar.typography.amendment.v0.1.0.md) | [avatar.contract.v0.1.0.md](../drafts/contracts/avatar.contract.v0.1.0.md) | `165:198` | REQUIRED | 4 | 4 | 4 |
| [CHARACTERS-001 · Characters](components/characters.typography.amendment.v0.1.0.md) | [characters.contract.v0.1.0.md](characters.contract.v0.1.0.md) | `820:7` | NOT_APPLICABLE | 0 | 0 | 0 |
| [LOGOS-001 · Logos](components/logos.typography.amendment.v0.1.0.md) | [logos.contract.v0.1.0.md](../drafts/contracts/logos.contract.v0.1.0.md) | `427:122` | NOT_APPLICABLE | 0 | 0 | 0 |
| [EMPTY-STATES-001 · EmptyStates](components/empty-states.typography.amendment.v0.1.0.md) | [empty-states.contract.v0.1.0.md](empty-states.contract.v0.1.0.md) | `639:128` | REQUIRED | 32 | 32 | 5 |
| [METRIC-CARD-001 · MetricCard](components/metric-card.typography.amendment.v0.1.0.md) | [metric-card.contract.v0.1.0.md](metric-card.contract.v0.1.0.md) | `202:208` | REQUIRED | 36 | 36 | 11 |
| [TABLE-001 · Table](components/table.typography.amendment.v0.1.0.md) | [table.contract.v0.1.0.md](table.contract.v0.1.0.md) | `546:122` | REQUIRED | 1446 | 1446 | 5 |
| [MODAL-001 · Modal](components/modal.typography.amendment.v0.1.0.md) | [modal.contract.v0.1.0.md](modal.contract.v0.1.0.md) | `565:122` | REQUIRED | 96 | 98 | 4 |
| [SCROLLBAR-001 · Scrollbar](components/scrollbar.typography.amendment.v0.1.0.md) | [scrollbar.contract.v0.1.0.md](scrollbar.contract.v0.1.0.md) | `328:122` | NOT_APPLICABLE | 0 | 0 | 0 |
| [FUENTES-001 · Fuentes](components/fuentes.typography.amendment.v0.1.0.md) | [fuentes.contract.v0.1.0.md](components/fuentes.contract.v0.1.0.md) | `847:7` | REQUIRED | 108 | 108 | 4 |
| [CHARTS-001 · Charts](components/charts.typography.amendment.v0.1.0.md) | [charts.contract.v0.1.0.md](charts.contract.v0.1.0.md) | `210:122` | REQUIRED | 85 | 85 | 7 |
| [HEADER-001 · Header](components/header.typography.amendment.v0.1.0.md) | [header.contract.v0.1.0.md](header.contract.v0.1.0.md) | `518:122` | REQUIRED | 123 | 123 | 6 |
| [SIDEBAR-001 · Sidebar](components/sidebar.typography.amendment.v0.1.0.md) | [sidebar.contract.v0.1.0.md](sidebar.contract.v0.1.0.md) | `614:125` | REQUIRED | 74 | 74 | 6 |
| [APP-SHELL-001 · AppShell](components/app-shell.typography.amendment.v0.1.0.md) | [app-shell.contract.v0.1.0.md](app-shell.contract.v0.1.0.md) | `737:303` | REQUIRED | 12 | 12 | 7 |
| [CHAT-HISTORY-ITEM-001 · ChatHistoryItem](components/chat-history-item.typography.amendment.v0.1.0.md) | [chat-history-item.contract.v0.1.0.md](chat-history-item.contract.v0.1.0.md) | `783:6` | REQUIRED | 16 | 16 | 2 |
| [CHAT-TOOL-ITEM-001 · ChatToolItem](components/chat-tool-item.typography.amendment.v0.1.0.md) | [chat-tool-item.contract.v0.1.0.md](chat-tool-item.contract.v0.1.0.md) | `783:6` | REQUIRED | 6 | 6 | 1 |
| [CHAT-TOOLBAR-001 · ChatToolbar](components/chat-toolbar.typography.amendment.v0.1.0.md) | [chat-toolbar.contract.v0.1.0.md](chat-toolbar.contract.v0.1.0.md) | `783:6` | REQUIRED | 76 | 76 | 4 |
| [CONVERSATION-001 · Conversation](components/conversation.typography.amendment.v0.1.0.md) | [conversation.contract.v0.1.0.md](conversation.contract.v0.1.0.md) | `765:6` | REQUIRED | 60 | 60 | 5 |
| [CHAT-SECTION-001 · ChatSection](components/chat-section.typography.amendment.v0.1.0.md) | [chat-section.contract.v0.1.0.md](chat-section.contract.v0.1.0.md) | `783:6` | REQUIRED | 58 | 58 | 6 |

**Resultado documental:** 43/43 familias identificadas: 39 con consumo `REQUIRED` y cuatro `NOT_APPLICABLE` (Loader, Scrollbar, Characters y Logos). Las cuatro exclusiones se justifican en sus propias enmiendas. App Shell e Icon Button sí tienen consumo por sus descendientes. Todos los 3353 rangos UI tienen una selección de estilo canónico y una identidad real Figma; esto es cobertura de requisitos, no un PASS de asignación persistida.

Tooltip, Toggle, Avatar y Logos conservan sus rutas base históricas reales en `drafts/contracts/`; sus enmiendas nuevas viven en `specs/components/`. No se inventa una promoción previa ni se altera el estado de aprobación de esos archivos.

## Preparación por subconjunto

El catálogo activo contiene 79 estilos (18 base + 61 complementarios). La enmienda de formato cambia únicamente 27 IDs lógicos: 15 rangos de Button, 4 de File Upload y 8 de Empty states. Sus métricas y bindings conservan la receta anterior; el formato UNDERLINE ahora forma parte del TextStyle. Los otros 3326 rangos UI conservan su identidad lógica.

El mapping 0.1.1 distingue `blockedSegments=0` (toda selección lógica está resuelta) de `applicationBlockedSegments=103` (vínculo explícito de escalados sin resolver). La preparación global de aplicación es `BLOCKED`; no se generaliza el piloto satisfactorio de Button a esos rangos. Los rangos afectados se reparten entre Select (64), Dropdown Item (26), Header (12) y App Shell (1), identificados en sus enmiendas. Los 3250 rangos no bloqueados por escala siguen sujetos a preflight, aplicación y QA final; este documento no afirma que ya estén implementados.

## Comprobación documental y límites

Se verificaron 43 IDs de familia únicos, 43 bases existentes y sus 25 rutas adicionales de enmiendas únicas (68 archivos normativos previos en total), 3351 nodeIds UI distintos, 3353 rangos sin omitir ni duplicar registros, las 79 claves únicas del catálogo y de styleMap, y resolución de cada estilo seleccionado. Los localizadores se derivan del mapping congelado y los nombres de variante del censo real. Las recetas no se transcriben como datos editables; description sigue teniendo un solo propietario.

Control documental del 2026-10-15: `PASS` acotado a los 44 MD de este paquete. El parser Ruby/Psych del repositorio aceptó sus frontmatters sin errores; se comprobaron 528 enlaces locales, 226 referencias de hash, 360 filas de asignación y las 43 referencias nuevas del registro web. Las selecciones de filas cubren exactamente los 3353 pares nodo/rango del mapping, con ID de estilo y decoración concordantes; 3250 no están bloqueados por escala y 103 conservan su bloqueo declarado. Este control no leyó ni modificó Figma y no valida su consumo persistido.

Los valores de Header expresados históricamente para empresa y RFC difieren del censo y catálogo vigentes. Su enmienda identifica esa sustitución de forma explícita; no se atribuye igualdad retroactiva. Sidebar sustituye nombres provisionales de estilos por identidades lógicas actuales, conservando sus roles. Las demás excepciones compactas y contextuales permanecen delimitadas por las tablas y por description del catálogo.

El [bloqueo de aplicación anterior](../qa/implementations/typography/Figma-blocker.md) sigue siendo evidencia histórica: compartir referencias de propiedades produjo propagación de estilos entre textos. Crear este paquete normativo no demuestra su resolución. El responsable del QA de aplicación debe reconciliar cada rango tras el último cambio, verificar aislamiento y preservar o explicar las diferencias. Ningún resultado PASS de estilos, documentación o web autoriza por sí solo a marcar consumidores Figma `VALIDATED`.

La delegación permite continuar el trabajo autorizado sin pedir aprobaciones repetidas por familia. Una incertidumbre material nueva se acota al consumidor afectado; no se completa con una variante, receta o aprobación inventada. La auditoría humana sigue pendiente.

## Cambio versionado

| Versión | Fecha | Alcance |
|---|---|---|
| 0.1.0 | 2026-10-15 | Asignación explícita de estilos a 43 familias mediante enmiendas nuevas; consumo real sujeto a QA final. |
