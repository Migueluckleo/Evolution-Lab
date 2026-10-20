# Registro de contratos

## CONVERSATION-COMPOSER-ACTION-001 · 0.1.2 · 2026-10-20

[Enmienda de Composer](../specs/components/conversation.composer-action.amendment.v0.1.2.md), aplica parcialmente a CONVERSATION-0010.1.0. `DELEGATED_FOR_BUILD`; [QA documental PASS](../qa/contracts/conversation-composer.v0.1.2.review.md), destino Figma READY. Revisión humana OPTIONAL_NON_BLOCKING/NOT_REQUIRED. Documenta Show action=false, aviso con texto y Button, mapeo de tokens y estilos base; conserva Draft/Tools. DEC-CONVERSATION-COMPOSER-ACTION-001 autoriza correcciones y sincronización. No sustituye Message/Response ni enmiendas de personajes.

## Tipografía · herencia nativa 0.1.2 · 2026-10-15

La [enmienda nativa 0.1.2](../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) selecciona el [catálogo 0.1.2](../specs/tokens/ai-design-system.typography.v0.1.2.json), SHA-256 `074a31a83f09b30a02fa8b8f0a7730bdb33fc0a8a9c59e3c8d2469b5799e934c`. Conserva 79 estilos y todas sus recetas/IDs/bindings; aclara tres `description` y motivos de compatibilidad, codificación explicativa y procedencia. Sustituye expresamente REQ-TYP-004/AC-TYP-004, §escalados, TYC-01/06 y13 filas de cuatro familias, solo para 103 rangos con evidencia nativa verificable. Los3250 rangos directos y los 27 UNDERLINE conservan sus reglas.

Las43 enmiendas históricas y el mapping 0.1.1 permanecen intactos. [components.registry.json](../implementations/web/components.registry.json) incorpora la nueva enmienda en Select, Dropdown Item, Header y App Shell; conserva el resto del cierre contractual. El ID lógico materializado define la receta métrica; el estilo principal y la escala nativa definen el vínculo Figma demostrado. Un ID local vacío no equivale por sí solo a cumplimiento.

Estado documental `DELEGATED_FOR_BUILD`, auditoría humana `PENDING`; consumo tipográfico `VALIDATED` en el [QA final0.1.2](../qa/implementations/typography.v0.1.2.review.md):3353 rangos resueltos,3250 directos y103 nativos,34 páginas. Estilos/descripciones y documentación tienen readback independiente. Se conserva el límite del guard no textual de Table perdido; este cierre no valida prototipos nuevos ni todo el diseño. El [registro de implementación](implementations.md) mantiene resultados por destino; P08 se registra en [skills.md](skills.md). Los cortes inferiores conservan su estado histórico.

## Tipografía · catálogo 0.1.1 y consumo por familia · 2026-10-15

Corte vigente: [FOUNDATIONS-TYPOGRAPHY-001-FORMATTING-001](../specs/foundations/typography.formatting.amendment.v0.1.1.md) selecciona el [catálogo 0.1.1](../specs/tokens/ai-design-system.typography.v0.1.1.json), con 79 estilos y decoración canónica. Sustituye solo la selección de catálogo y el tratamiento de UNDERLINE que identifica; el contrato base y el catálogo 0.1.0 permanecen como historia. SHA-256 del catálogo activo: `26b05557aeeb40f78398a673f768a82035474dc84796aa6f5350f1ce911664cd`.

[TYPOGRAPHY-CONSUMPTION-001](../specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) enlaza **43 enmiendas nuevas, una por familia**, y sus bases reales. Cada una identifica texto/rol/variante, dependencia propia o anidada, estilo lógico, TextStyle ID real y rangos exactos del mapping congelado. Cobertura: 3351 nodos/3353 rangos UI; 39 familias REQUIRED y cuatro NOT_APPLICABLE justificadas (Loader, Scrollbar, Characters y Logos). No duplica recetas ni altera las 68 fuentes normativas previas consultadas. Las enmiendas se incorporaron a [components.registry.json](../implementations/web/components.registry.json).

QA documental de los 44 MD de consumo: `PASS` acotado, con controles y hashes en la enmienda transversal. Estado documental `DELEGATED_FOR_BUILD` bajo [delegación específica ampliada](DEC-TYPOGRAPHY-STYLES-001.md); auditoría humana `PENDING`. La ejecución Figma está `IN_PROGRESS`: 103 rangos escalados conservan `UNRESOLVED_SCALED_LINK` y no se escriben; los 3250 restantes requieren aplicación y readback final. El `BLOCKED` global de preparación del mapping no significa que todos los componentes estén impedidos. El [piloto de formato](../qa/implementations/typography/consumption-v0.1.1/probe.format-styles.persisted-and-instance-edit.json) solo acredita su copia y seis instancias; no acredita consumidores globales. El resultado por destino se registra en [implementations.md](implementations.md), y el cierre de distribución en [skills.md](skills.md).

## FOUNDATIONS-TYPOGRAPHY-001 · 2026-10-15

[Contrato tipográfico 0.1.0](../specs/foundations/typography.contract.v0.1.0.md), `DELEGATED_FOR_BUILD` por [decisión específica](DEC-TYPOGRAPHY-STYLES-001.md), auditoría humana `PENDING`. Delega valores y descripciones al [catálogo JSON](../specs/tokens/ai-design-system.typography.v0.1.0.json). [QA documental](../qa/contracts/typography.v0.1.0.md) distingue base, complementarios y consumidores; los contratos históricos conservan su alcance salvo sustitución identificada.

## CHAT-LAYOUT-001 · enmienda0.1.1 · 2026-10-09

[Enmienda en specs](../specs/components/chat.layout.amendment.v0.1.1.md) a Chat Section/Toolbar0.1.0: documenta ajustes del usuario de width, altura y scrolling. DELEGATED_FOR_BUILD/user_audit PENDING; QA documental/readback acotado, no VALIDATED global ni permiso nuevo de escritura. [Estado](../implementations/figma/chat-layout.v0.1.1.state.json), [QA y límites](../qa/implementations/chat-layout.v0.1.1.review.md). Sustituye solo las reglas identificadas, no tokens ni propiedades de dependencias; bases y QA anterior preservados como historia.

## CHARACTERS-001 · 2026-10-08

[Contrato0.1.0](../specs/characters.contract.v0.1.0.md), DELEGATED_FOR_BUILD, QA documental/técnico PASS, auditoría PENDING. Dos sets/13 frames; [JSON sombra](../specs/tokens/ai-design-system.character-shadow.v0.1.0.json) gobernado por §10 y DEC-CHARACTER-IDENTITY-001. [Continuidad](SESSION-HANDOFF-2026-10-08-CHARACTERS.md).

## CHAT-SECTION-001 · v0.1.0 · 2026-10-08

[Contrato en specs](../specs/chat-section.contract.v0.1.0.md), SHA25659c5331596821920d475c6efa1c80ce3deaf05a9f3ffa41ba97d3a28f7c0093f. DELEGATED_FOR_BUILD por DEC-EXTERNAL-COMPONENTS-DELEGATION-001; user_audit PENDING, Figma READY/VALIDATED técnicamente; frontend fuera de alcance. [QA documental](../qa/contracts/chat-section.v0.1.0.review.md), [QA técnico](../qa/implementations/chat-section.v0.1.0.review.md), [handoff](SESSION-HANDOFF-2026-10-08-CHAT.md). Slots REQUIRED/IMPLEMENTED. Datos del inventario base y extensión character-identity existente; sin variables nuevas. Candidato preservado en QA, drafts solo localizador.

## CONVERSATION-CHARACTER-IDENTITY-001 · 2026-10-08

[Enmienda0.1.1](../specs/components/conversation.character-identity.amendment.v0.1.1.md), DELEGATED_FOR_BUILD; tres tokens directos de identidad fija en [JSON](../specs/tokens/ai-design-system.character-identity.v0.1.0.json). QA documental y técnico PASS acotados; [estado con digests](../implementations/figma/conversation.characters.v0.1.1.state.json). Sustituye cromática de personajes del contrato0.1.0, no controles ni Slots. Auditoría PENDING; no biblioteca publicada.

## CONVERSATION-001 · 2026-10-08 · cierre vigente

[Contrato0.1.0 en specs](../specs/conversation.contract.v0.1.0.md), SHA256 `06818b9fdd3373ce1a93c217e2d2ce227a203b94bd92ae94927687efbb2e9796`, DELEGATED_FOR_BUILD bajo [delegación externa](DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md). QA documental/técnico PASS acotado; Figma VALIDATED; auditoría PENDING, biblioteca UNPUBLISHED. [Estado](../implementations/figma/conversation.v0.1.0.state.json). Sustituye exclusivamente NOT_STARTED/BLOCKED del registro de ingesta inferior; el extracto fuente sigue DRAFT/PARTIAL, no se reescribe como norma.

## CONVERSATION-SOURCE-OBSERVATION-001 · 2026-10-08

[Control de integridad y digests](../qa/contracts/conversation.source-intake.2026-10-08.review.md): PASS estructural de evidencia; no QA normativo ni de implementación.

[MD de evidencia](../drafts/contracts/conversation.source.component-contract.md) / [YAML](../drafts/contracts/conversation.source.component-contract.yaml), schema0.1.0, DRAFT observacional/PARTIAL; fuente SRC-FIGMA-CONVERSATION-EXTERNAL-001. No sustituye ni aprueba PROP-03 de Anticipa Screen Composition. Contrato normativo destino NOT_STARTED; Figma readiness BLOCKED para P04 hasta resolver alcance de delegación externa, contrato, mapa canónico y dependencias pertinentes. [Reporte](../drafts/reports/conversation.external-intake.2026-10-08.md) separa propuesta, limitaciones y autorización; no se afirma implementación ni publicación.

## APP-SHELL-001 · 2026-10-06

[App Shell0.1.0](../specs/app-shell.contract.v0.1.0.md), DELEGATED_FOR_BUILD, SHA256f4735e43344b54477df4ab8058f55fa5c45b6c03fdbdf651c6d35feb5d75ad9e. [Síntesis](../drafts/reports/app-shell.synthesis.v0.1.0.md), [QA documental](../qa/contracts/app-shell.v0.1.0.review.md) y [QA técnico](../qa/implementations/app-shell.v0.1.0.figma.review.md) PASS. Promovido a specs con auditoría humana PENDING. Fuente SRC-FIGMA-APP-SHELL-001; [decisión delegada](DEC-APP-SHELL-INTEGRATION-001.md). Un shell desktop con Header/Sidebar locales y Content Slot0..n; cinco tokens existentes en envoltura, sin nuevas variables. Figma VALIDATED, web fuera de alcance, biblioteca no publicada por esta operación. No aprueba el contrato Anticipa DRAFT.

## ANTICIPA-SCREEN-COMPOSITION-001 · 2026-10-06

[Contrato MD0.1.0](../drafts/contracts/anticipa-screen-composition.contract.v0.1.0.md), **DRAFT**; ocho recetas de composición y cuatro propuestas de componentes, no implementación delegada. [Síntesis](../drafts/reports/anticipa-screen-composition.synthesis.v0.1.0.md), [lock derivado](../drafts/contracts/anticipa-screen-composition.dependencies.v0.1.0.json) de30 dependencias directas y37 selectores semánticos; valores/descripciones exclusivamente en sus JSON propietarios. Fuente SRC-FIGMA-ANTICIPA-LAYOUT-OBSERVATION-001 y solicitud USR-ANTICIPA-COMPOSITION-001. [QA documental](../qa/contracts/anticipa-screen-composition.v0.1.0.review.md) y [digests/verificación](../qa/contracts/anticipa-screen-composition.v0.1.0.verification.json). Figma/web BLOCKED como contrato integral listo; implementación NOT_STARTED, aprobación pendiente por alcance. No modifica contratos DS, inventario ni Figma; no promoción a specs ni publicación de biblioteca. Grafo STALE para estos nuevos artefactos.

## Promoción documental de enmiendas · paso 4 · 2026-10-06

Diecinueve enmiendas trasladadas a su ubicación normativa en specs:13 de Foundations, una de Buttons, una de Avatar y cuatro de Toggle. [Índice canónico y QA por documento](../qa/contracts/specs-promotion.2026-10-06.review.md), [manifiesto de bytes](../qa/contracts/specs-promotion.2026-10-06.manifest.json). Identidad/versiones conservadas; DELEGATED_FOR_BUILD, user_audit PENDING. Rutas drafts convertidas en punteros y originales archivados; no normas paralelas. Las sustituciones ya adoptadas gobiernan los campos históricos señalados. Bases Tooltip/Toggle/Avatar/Logos no promovidas por sus asuntos existentes; no nuevos pendientes ni aceptación implícita de Logos. Entradas/digests inferiores conservan su fecha histórica.

## LOGOS-001 · alcance0.1.1 y refinamiento · 2026-10-06

[Enmienda de alcance](../specs/components/logos.scope.amendment.v0.1.1.md) formaliza omisión de doce assets y Slots NOT_APPLICABLE. No modifica fidelidad ni tolerancia. Base0.1.0 conserva ubicación previa por [QA geométrico pendiente de decisión](../qa/implementations/logos.refinement.v0.1.1.review.md). DELEGATED_FOR_BUILD, auditoría PENDING; no promocionada ni publicada como aprobada.

## RADIO-BUTTON-001 / CHECKBOX-001 · cierre punto2 · 2026-10-06

[Radio](../specs/radio-button.contract.v0.1.0.md) y [Checkbox](../specs/checkbox.contract.v0.1.0.md) son las ubicaciones canónicas, junto a sus enmiendas cromáticas0.1.1 y [refinamiento0.1.2](../specs/components/radio-checkbox.refinement.amendment.v0.1.2.md). DELEGATED_FOR_BUILD, user_audit PENDING, Figma READY/VALIDATED en este alcance. [QA](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). Rutas drafts ahora punteros; registros y digests inferiores son históricos. No otra aprobación por componente ni catálogo duplicado.

## SIX-FAMILY-COLOR-001 · cierre cromático · 2026-10-05

[Enmienda en specs](../specs/components/six-family-color.amendment.v0.1.0.md), [datos canónicos](../specs/tokens/ai-design-system.six-family-color.v0.1.0.json), [QA](../qa/implementations/six-families.color.v0.1.0.review.md). DELEGATED_FOR_BUILD, auditoría PENDING.12 roles: ocho corregidos/cuatro nuevos; cero primitivas. Sustituye las recetas y umbrales señalados, no la anatomía ni la aprobación humana.

Promovidos a ubicación canónica: [Icon Button](../specs/icon-button.contract.v0.1.0.md), [Breadcrumbs](../specs/breadcrumbs.contract.v0.1.0.md), [Metric Card](../specs/metric-card.contract.v0.1.0.md), [Charts](../specs/charts.contract.v0.1.0.md), [Linear Progress Bar](../specs/linear-progress-bar.contract.v0.1.0.md). Las rutas anteriores son localizadores, no segundas definiciones editables. Los hashes/cierres0.1.0 inferiores son históricos; los bytes actuales se registran en el manifiesto del cierre. Buttons conserva su base0.2.0 y enmiendas0.2.1/0.2.2, complementadas por ésta.

## Conciliación de referencias operativas · 2026-10-05

La [lista vigente](../specs/MIGRATION-TRACEABILITY-STATUS.md) distingue revisiones restantes de construcciones cerradas. Las menciones inferiores de Select Closed/Open u otras subfamilias Navigation pendientes describen su corte inicial: SELECT-001 y las cuatro subfamilias Navigation ya tienen contratos/QA propios registrados. Search vigente es0.1.1; la entrada0.1.0 es histórica. No se promueve por esta conciliación ningún contrato pendiente de QA, no se cambian digests normativos ni se atribuye aprobación humana.

## FILTER-CHIP-001 · enmienda semántica 0.2.1 · 2026-10-05

[Chips 0.2.1](../specs/components/filter-chip.semantic.amendment.v0.2.1.md) y [Foundations inverse icon](../specs/foundations.inverse-icon.amendment.v0.1.0.md): DELEGATED_FOR_BUILD, auditoría PENDING. QA documental e implementación PASS para 36 bindings inversos, sin cambios cromáticos ni variantes. Base aprobada 0.2.0 preservada; nuevo rol canónico en specs/tokens, cero primitivas nuevas.

## BUTTON-001 · enmienda vigente de bindings 0.2.2 · 2026-10-05

[AMD-BUTTON-LOCAL-BINDINGS-001](../specs/components/button.local-bindings.amendment.v0.2.2.md), SHA-256 433e968a44859e47d39c1c3de372d2a806a48e322c81f49e54e19d4795597bd4, sustituye únicamente la preservación de nueve variables remotas de REQ/AC-BTN-004. Base de uso 0.2.0, página Buttons y corrección Disabled0.2.1 permanecen vigentes. DELEGATED_FOR_BUILD; [QA documental](../qa/contracts/button.local-bindings.v0.2.2.review.md) y [QA Figma](../qa/implementations/button.local-bindings.v0.2.2.figma.review.md) PASS acotados; auditoría PENDING. [Estado](../implementations/figma/buttons.local-bindings.v0.2.2.state.json).

## SEARCH-001 · revisión vigente 0.1.1 · 2026-10-05

[Search0.1.1](../specs/search.contract.v0.1.1.md) sustituye íntegramente a0.1.0 como contrato normativo. Corrección editorial de alcance DOC-SEARCH-001, sin cambio de diseño. QA documental y correspondencia con Figma PASS acotados; DELEGATED_FOR_BUILD, auditoría PENDING.0.1.0 y sus QA se conservan históricos; sus cláusulas cruzadas quedan sin vigencia. [Estado](../implementations/figma/search.v0.1.1.state.json). Esta entrada cierra el CONFLICT documental registrado abajo el01/10, no certifica una nueva auditoría cromática global.

## EMPTY-STATES-001 · 2026-10-05

[Contrato0.1.0](../specs/empty-states.contract.v0.1.0.md) y [Foundations](../specs/foundations.empty-states-roles.amendment.v0.1.0.md) promovidos a specs por QA documental/técnicoPASS. DELEGATED_FOR_BUILD, auditoríaPENDING. Cuatro presets, dosSlots por variante yseisroles nuevos sin primitivas. Ajustes posteriores directos en specs; no copia normativa en drafts. [QA](../qa/implementations/empty-states.v0.1.0.figma.review.md).

## SIDEBAR-001 · 2026-10-05

[Sidebar0.1.0](../specs/sidebar.contract.v0.1.0.md) y [extensión Foundations](../specs/foundations.sidebar-roles.amendment.v0.1.0.md) en specs. DELEGATED_FOR_BUILD; QA documental/técnico PASS acotado.22+2+1definiciones, Slots compartidos y tresroles nuevos sin primitivas. AuditoríaPENDING, bibliotecaUNPUBLISHED. [QA](../qa/implementations/sidebar.v0.1.0.figma.review.md).

## MODAL-001 · 2026-10-01

[Modal0.1.0](../specs/modal.contract.v0.1.0.md) promovido a specs con QA documental/técnico PASS. DELEGATED_FOR_BUILD; auditoría humanaPENDING. FuenteLibrería raíz, ocho configuraciones públicas y SlotsBody/Side content/Actions.32tokens/128aliases, sin variablesnuevas. [QA](../qa/implementations/modal.v0.1.0.figma.review.md). No publicaciónFigma.

## TABLE-001 · 2026-10-01

[Table0.1.0](../specs/table.contract.v0.1.0.md) promovido a specs tras QA documental/técnico acotado. DELEGATED_FOR_BUILD, auditoría humanaPENDING. FuenteAnticipa por decisión explícita, SlotsRows/Cells/Actions0..n, siete mains públicos en seis unidades. Cero tokens nuevos; excepcionesHover y aproximación de negro registradas. [QA](../qa/implementations/table.v0.1.0.figma.review.md). No publicación Figma.

## HEADER-001 · 2026-10-01

[Header0.1.0](../specs/header.contract.v0.1.0.md) promovido a specs tras QA documental e implementación técnica PASS. Estado DELEGATED_FOR_BUILD; auditoría humana PENDING. Composición Desktop única, Slot Actions0..n, cuatro textos y Avatar expuesto. [Enmienda Foundations](../specs/foundations.header-roles.amendment.v0.1.0.md): tres roles semánticos, cero primitivas. [Fuente observada](../drafts/contracts/header.source.component-contract.md). No publicación Figma.

## Revisión documental acotada · DOC-SEARCH-001 · 2026-10-01

[Search0.1.0](../specs/search.contract.v0.1.0.md) conserva su identidad y estado DELEGATED_FOR_BUILD, sin aprobación nueva. Se detectó un CONFLICT interno de alcance entre anatomía/matriz Search y cláusulas File Upload/Textarea en §§4,7,10,11,14–16; sus QA también contienen prosa cruzada. [Hallazgo y alcance](../specs/MIGRATION-AUDIT.md). La preparación para reutilizar esas cláusulas queda CONFLICT hasta corrección versionada en specs y QA documental afectado; no se invalida por conjetura toda la implementación ni se reconstruye. No bloquea Header ni modifica los contratos de las otras familias.

## COMPOSITION-SLOTS-002 y FOUNDATIONS-PAGINATION-SLOT-STATE-001

2026-09-30 · [Slots0.1.1](../specs/composition-slots.amendment.v0.1.1.md) y [Foundations Pagination0.1.0](../specs/foundations.pagination-slot-state.amendment.v0.1.0.md), DELEGATED_FOR_BUILD en specs. QA documental y técnico PASS acotados. Steps/Gallery, Pagination/Pages y leyendas Charts; no reemplazan las bases históricas ni la enmienda Slots0.1.0 de otras familias. [Estado](../implementations/figma/composition-slots.v0.1.1.state.json), [QA documental](../qa/contracts/composition-slots.v0.1.1.review.md). Auditoría humana PENDING.

## COMPOSITION-SLOTS-001

2026-09-29 · [Enmienda0.1.0 en specs](../specs/composition-slots.amendment.v0.1.0.md), SHA2563573e964d3f523470e9c3d733993911ccec94dd2484ea6211d739a1588c81cb5, DELEGATED_FOR_BUILD. Sustituye exclusivamente las reglas de composición identificadas de SELECT-001, NAVIGATION-SWITCH-TAB-001 y BREADCRUMBS-001. Incluye ajuste de ancho de cuatro ítems Breadcrumb por evidencia. QA documental y técnico de Slots PASS acotado; no revalida automáticamente las decisiones cromáticas históricas. [Estado vigente](../implementations/figma/composition-slots.v0.1.0.state.json), [matriz](SLOTS-REVIEW-STATUS.md). Auditoría humana PENDING, biblioteca sin publicar.

## SELECT-001

2026-09-29 · [Select0.1.0](../specs/select.contract.v0.1.0.md), DELEGATED_FOR_BUILD, Figma READY, auditoría PENDING. Dos presentaciones visuales Closed/Open, no comportamiento funcional. QA documental y técnico acotado PASS. Datos: inventario canónico y extensiones heredadas; excepción explícita de sombras. [Estado/digest](../implementations/figma/select.v0.1.0.state.json). No copia normativa en drafts.

## DROPDOWN-ITEM-001

- **Vigente en specs:** [Dropdown Item0.1.0](../specs/dropdown-item.contract.v0.1.0.md), SHA-256 `414040f481f994316406dfd61ca09a4c5a52b4b9ec97e30dcb2a1dc90ef27d42`.
- **Estado:** DELEGATED_FOR_BUILD, auditoría humana PENDING. Preparación Figma READY; [QA documental](../qa/contracts/dropdown-item.v0.1.0.review.md) y [técnico](../qa/implementations/dropdown-item.v0.1.0.figma.review.md) PASS.
- **Alcance:** 18 variantes de opción,10 propiedades editables y dependencias locales; página Select444:122, set446:528. Composiciones abiertas/cerradas de Select fuera de este contrato, aún pendientes.
- **Datos:** JSON canónico sin cambio; 24 roles/96comprobaciones. [Síntesis](../drafts/reports/dropdown-item.synthesis.v0.1.0.md), [estado](../implementations/figma/dropdown-item.v0.1.0.state.json). Cualquier ajuste posterior normativo se hará en specs. Biblioteca UNPUBLISHED.

## LOGOS-001

- **Contrato:** [v0.1.0](../drafts/contracts/logos.contract.v0.1.0.md), SHA-256 `088b7e86d695541b4587b891a658a2d50e1843e9bb0e98a1ef0cdfc340bf4f56`.
- **Estado:** DELEGATED_FOR_BUILD, auditoría humana PENDING. [QA documental](../qa/contracts/logos.v0.1.0.review.md) PASS; no aprobación humana simulada.
- **Alcance:** copia fiel de72 variantes y12assets, sin variables/tokens por DEC-LOGOS-AGNOSTIC-ASSETS-001. Fuente SRC-FIGMA-LOGOS-001.
- **Destino:** Logos427:122. Seis sets construidos; doce assets restantes omitidos por el usuario mediante DEC-LOGOS-REMAINDER-OMITTED-001. No pedir acceso al editor para continuar otras familias. La implementación sigue parcial, sin QA global PASS.
- **Gate:** [QA parcial](../qa/implementations/logos.v0.1.0.figma.review.md) PENDING, diferencias geométricas documentadas. No promovido a specs ni publicado en biblioteca.


## MIGRATION-TOKEN-TRACEABILITY-001

- **Ruta vigente:** [contrato transversal](../specs/MIGRATION-TOKEN-TRACEABILITY.contract.md) 0.1.0, SHA-256 `135732d2d2d63261319627bc22eb1b887d2ba00a62dce51bbc2bde80bea1d7ce`, regla de trazabilidad solicitada por el usuario en [DEC-MIGRATION-TRACEABILITY-001](decisions.md).
- **Alcance:** método común de documentación y comprobación fuente→JSON→variable local→binding→readback; no crea una segunda definición editable de tokens ni aprueba contratos de familia retroactivamente.
- **Cobertura:** [matriz vigente](../specs/MIGRATION-TRACEABILITY-STATUS.md), con pendientes explícitos. Las ambigüedades materiales se concentran en [auditoría por excepciones](../specs/MIGRATION-AUDIT.md).
- **QA documental:** [revisión 0.1.0](../qa/contracts/migration-token-traceability.v0.1.0.review.md); no sustituye QA por familia.

## FOUNDATIONS-TOKENS-001

- **Ruta vigente:** [contrato aprobado](../specs/foundations/foundations-tokens.contract.md); [candidato conservado](../drafts/contracts/foundations-tokens.contract.md).
- **Versión:** `0.1.0`.
- **Estado documental:** `APPROVED` para reconstrucción Figma, según [DEC-TOKENS-001](decisions.md).
- **SHA-256 bytes del candidato revisado:** `e89ddaf95e1ee07998fa851c50ef9787b4ec3f9072e0c1ea44e07eb3e298e1da`.
- **SHA-256 bytes del contrato publicado:** `e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999`.
- **Fuentes:** `SRC-TOKENS-INV-001`, `SRC-TOKENS-AUD-001` en [registro de fuentes](sources.md).
- **Dato canónico delegado para este alcance:** [inventario](../sources/inventories/tokens.inventory.json), SHA-256 bytes `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- **Reporte de síntesis:** [SYN-TOKENS-001](../drafts/reports/foundations-tokens.synthesis.md).
- **QA documental:** [QA-TOKENS-001](../qa/contracts/foundations-tokens.review.md).
- **Preparación Figma:** `READY` para el alcance aprobado de variables; destino, lectura y escritura comprobados durante IMP-TOKENS-FIGMA-001.
- **Implementación Figma:** `VALIDATED` para las variables de este contrato; véase [QA-TOKENS-FIGMA-001](../qa/implementations/foundations-tokens.figma.review.md).
- **Extensión de destino 0.1.1:** [AMD-FOUNDATIONS-CONTROL-COLORS-001](../drafts/contracts/foundations.control-colors.amendment.v0.1.1.md), SHA-256 `e53c97caaa47a606f07eab5159cacdfc48fae8a797783c20d2e8ecc7865708e4`, `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.control-colors.amendment.v0.1.1.review.md) `PASS`. Dos roles semánticos con [JSON propio](../drafts/foundations/ai-design-system.control-colors.v0.1.0.json), SHA-256 `4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839`; no modifica el inventario fuente ni la aprobación 0.1.0. [Implementación](implementations.md) y [QA Figma](../qa/implementations/control-colors.v0.1.0.figma.review.md) `PASS`; `user_audit: PENDING`.
- **Web:** fuera del alcance de esta versión.

## BUTTON-001

- **Ruta vigente:** [contrato aprobado 0.2.0](../specs/components/button.contract.v0.2.0.md); [candidato revisado conservado](../drafts/contracts/button.contract.v0.2.0.md); [modelo técnico YAML vinculado](../drafts/contracts/button.contract.yaml).
- **Versión:** `0.2.0`, aprobada según [DEC-BUTTON-USAGE-002](decisions.md). El [contrato 0.1.0](../specs/components/button.contract.md) queda como baseline técnico histórico `SUPERSEDED` para la documentación de uso, pero sus REQ/AC-001–009 se incorporan por referencia sin cambio; la enmienda `Buttons` sigue aplicando.
- **Estado documental:** `APPROVED` para guía de uso y Description Figma. SHA-256 bytes del candidato 0.2.0 `c97cd24a1505236cfdac32d85a676d8eb2b4394ec074412305d7cfd3abf37ae5`; publicado `53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1`.
- **Historial 0.1.0:** aprobación [DEC-BUTTON-001](decisions.md), candidato conservado [aquí](../drafts/contracts/button.contract.md); QA estructural/visual previo conserva validez para ese alcance.
- **SHA-256 Markdown candidato 0.1.0 revisado:** `a2124c2d1236108c5ff129e6d552510568b625a1012ab3653d18528f89c0d6a0`.
- **SHA-256 Markdown publicado 0.1.0:** `4b94f80787c1fc9d9990f806c99900e17db060e65b624471b0c8d93f534f2abb`.
- **SHA-256 YAML:** `734b85826ad4cb4c2caa08932e4364516a6e2f31f4be8e8ce6b0decda6ec4e1b`.
- **Historia del candidato:** antes de `DEC-ICONS-001`, los digests en revisión eran Markdown `9adaaf948e8c02bf9ca6cb89a5d81c277af38e097e12154c9a686912fe53e036` y YAML `a3e90ba85e8397d286c40eea440db7eaebc41ce0a49699e24958c8a2adc40e37`; no hubo versión aprobada ni implementación asociada.
- **Fuentes:** `SRC-FIGMA-BUTTON-001` y `SRC-FIGMA-PHOSPHOR-001` en [registro de fuentes](sources.md); política explícita [DEC-ICONS-001](decisions.md). [AMD-BUTTON-PAGE-001](../specs/components/button-page-name.amendment.md) fija `Buttons` exclusivamente para REQ/AC-BTN-007.
- **Reporte de síntesis:** [SYN-BUTTON-001](../drafts/reports/button.synthesis.md), SHA-256 `a4801721fe9425d7b339115b15ef6bc139459d5b3977180959a4d0b8aae36f19`.
- **QA documental:** [QA-BUTTON-001](../qa/contracts/button.review.md), `PASS` para presentar a decisión humana.
- **Preparación Figma histórica 0.1.0:** `READY` para el alcance aprobado y la enmienda de página; capacidad de renombrar y leer de vuelta verificada. La preservación histórica de nueve variables remotas queda sustituida solo para esos bindings por la enmienda0.2.2 enlazada al inicio; Phosphor conserva sus vínculos.
- **Implementación Figma:** `VALIDATED` para la representación especificada; se renombró la página existente a `Buttons` sin recrear el set. Véanse [IMP-BUTTON-FIGMA-001](implementations.md) y [QA-BUTTON-FIGMA-002](../qa/implementations/button.figma.review.md). No acredita semántica de producto, WCAG ni web.
- **Web:** fuera del alcance de esta versión y sin contrato.

## FILTER-CHIP-001

- **Ruta vigente:** [contrato aprobado 0.2.0](../specs/components/filter-chip.contract.v0.2.0.md); [candidato revisado conservado](../drafts/contracts/filter-chip.contract.v0.2.0.md); [modelo de construcción](../drafts/contracts/filter-chip.build.v0.2.0.yaml). El [candidato observacional 0.1.0](../drafts/contracts/filter-chip.contract.md) y su [YAML de fuente](../drafts/contracts/filter-chip.contract.yaml) se conservan.
- **Versión:** `0.2.0` aprobada según [DEC-FILTER-CHIP-APPROVAL-002](decisions.md); `0.1.0` histórica no aprobada.
- **Estado documental:** `APPROVED` para Figma. SHA-256 bytes candidato `bd82e46bcbde849890af30e9c8f6d5fad3b1d0cb2b3b5b2f5ac1cacd1127ab96`; publicado `325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8`; modelo de construcción `40e9e3464b86560255c185bf893518dea2a445170678fa797c8ff6925218e48c`; YAML de fuente `af6918afb5ce050047c06153d9def42d9365efb3f2fbbee949f2845a2932632e`.
- **Fuente:** `SRC-FIGMA-FILTER-CHIP-001`; snapshot y captura registrados en [sources.md](sources.md).
- **Decisiones:** [DEC-FILTER-CHIP-DIRECTION-001](decisions.md) adopta la descripción; [DEC-FILTER-CHIP-APPROVAL-002](decisions.md) aprueba esta versión y 30 variantes.
- **Plan de construcción:** [PLAN-FILTER-CHIP-FIGMA-001](../drafts/reports/filter-chip.v0.2.0.plan.md).
- **Description propuesta:** [texto exacto](../drafts/figma/filter-chip.description.v0.2.0.md), SHA-256 bytes `a76fec95af4ab8fbfdbb865fef71842bba16f2bd990d98596c0b43b9d4ca86f2`.
- **QA documental vigente:** [QA-FILTER-CHIP-002](../qa/contracts/filter-chip.v0.2.0.review.md), `PASS` para decisión humana. El [QA 0.1.0](../qa/contracts/filter-chip.review.md) conserva el conflicto histórico.
- **Preparación Figma:** `READY`; página `Chips`, 26 variables requeridas, dos tokens de fuente/peso y dependencia Phosphor identificados por preflight de solo lectura. Se revalidarán IDs antes de escribir.
- **Implementación Figma:** `VALIDATED` para el alcance estructural y visual aprobado: página exclusiva `Chips` (`67:122`), set `Filter Chip` (`72:298`) y 30 variantes. Véanse [IMP-FILTER-CHIP-FIGMA-001](implementations.md) y [QA-FILTER-CHIP-FIGMA-001](../qa/implementations/filter-chip.v0.2.0.figma.review.md). El set permanece `UNPUBLISHED` como biblioteca de equipo.
- **Web:** `BLOCKED` y fuera del alcance; no hay API, semántica, teclado ni accesibilidad aprobados.

## TOOLTIP-001

- **Ruta delegada:** [Tooltip 0.1.0](../drafts/contracts/tooltip.contract.v0.1.0.md); [candidato revisado preservado](../drafts/contracts/tooltip.contract.v0.1.0.candidate.md); [YAML de evidencia](../drafts/contracts/tooltip.contract.v0.1.0.yaml).
- **Estado documental:** `DELEGATED_FOR_BUILD`, no `APPROVED`; auditoría humana `PENDING`. Candidato SHA-256 bytes `be1b92f6026cc2825a5bdbc105718c2b9dffbc097a5da39a8cc84745f00d4359`; versión delegada `522b74426f781231dbf0a3ce7daed35909ab8f1358e347efe97e34f454416402`; YAML `0e091b8057c012d012668d01bdc152cf920faa85ae27265fb5a82df374918d2d`.
- **Fuentes:** `SRC-FIGMA-TOOLTIP-001`, JSON aprobado `SRC-TOKENS-INV-001`; [síntesis](../drafts/reports/tooltip.v0.1.0.synthesis.md).
- **QA documental:** [QA-TOOLTIP-001](../qa/contracts/tooltip.v0.1.0.review.md), `PASS`; decisión de trabajo delegado [DEC-LEGACY-MIGRATION-DELEGATION-001](decisions.md).
- **Preparación Figma:** `READY` para crear página `Tooltips` y set con cuatro variantes; las 13 variables destino están presentes, no hay página homónima ni dependencia de componente anidado. [Plan](../drafts/reports/tooltip.v0.1.0.plan.md).
- **Implementación Figma:** `VALIDATED` técnicamente contra el contrato delegado: página `Tooltips` `85:122`, set `Tooltip` `88:122`, cuatro variantes y bindings locales. Véanse [IMP-TOOLTIP-FIGMA-001](implementations.md) y [QA-TOOLTIP-FIGMA-001](../qa/implementations/tooltip.v0.1.0.figma.review.md). `user_audit: PENDING`; set `UNPUBLISHED`. Web fuera del alcance.

## BADGE-001

- **Ruta delegada publicada en `specs/`:** [Badge 0.1.0](../specs/components/badge.contract.v0.1.0.md); [candidato preservado](../drafts/contracts/badge.contract.v0.1.0.candidate.md); [YAML de evidencia](../drafts/contracts/badge.contract.v0.1.0.yaml). Publicación documental técnica, no aprobación humana ni publicación de biblioteca.
- **Estado documental:** `DELEGATED_FOR_BUILD`, no `APPROVED`; auditoría humana `PENDING`. Candidato SHA-256 bytes `388812c1028c1dfaedda1a885b7043fec25e36a7ef7bf23411b513bd64b84830`; versión delegada `abc4e0e768be75831c343fe8e32322322e650ad437b7eae4860e498cbdc6f216`; YAML `b087af4f17a478f136e3bb50e3c4a5eaa3b9c789deb1325310c6a669f879087b`.
- **Fuentes:** `SRC-FIGMA-BADGE-001`, `SRC-FIGMA-PHOSPHOR-001`, JSON aprobado `SRC-TOKENS-INV-001`; [síntesis](../drafts/reports/badge.v0.1.0.synthesis.md).
- **QA documental:** [QA-BADGE-001](../qa/contracts/badge.v0.1.0.review.md), `PASS`; decisión [DEC-LEGACY-MIGRATION-DELEGATION-001](decisions.md).
- **Preparación Figma:** `READY` para crear página `Badges` y set de seis variantes; 26 roles visuales locales presentes, dependencia Presentation confirmada en Phosphor y 1512 preferidos recuperables del set Chips. [Plan](../drafts/reports/badge.v0.1.0.plan.md).
- **Enmienda de contraste histórica:** [AMD-BADGE-CONTRAST-001 0.1.1](../drafts/contracts/badge.contrast-amendment.v0.1.1.md), SHA-256 bytes `8d63aec283dcd5e32d7bd3669e1460d2e493b819b7ca0ef71fe5d27b65cc5e89`; [candidato preservado](../drafts/contracts/badge.contrast-amendment.v0.1.1.candidate.md) y [QA documental](../qa/contracts/badge.contrast-amendment.v0.1.1.review.md) `PASS` histórico. Sus colores Informational/Warning y umbrales fueron sustituidos por 0.1.2; otros requisitos no se borran.
- **Enmienda cromática vigente:** [AMD-BADGE-SOURCE-COLOR-002 0.1.2](../specs/components/badge.source-color-amendment.v0.1.2.md), SHA-256 `5120317285938bb9fc06fd67ed0ce8b11b71c1d23051cd13464137c36280dabb`, [QA documental](../qa/contracts/badge.source-color-amendment.v0.1.2.review.md), [QA Figma](../qa/implementations/badge.source-color.v0.1.2.figma.review.md) y [QA de publicación en specs](../qa/contracts/badge.specs-publication.v0.1.2.review.md) `PASS` técnico. Depende del override Foundations warning/icon 0.1.1; `user_audit: PENDING`.
- **Implementación Figma:** `VALIDATED` técnicamente contra base 0.1.0 más la enmienda 0.1.2 vigente: página `Badges` `94:122`, set `Badge` `98:128`, seis variantes y 19 paints visibles cromáticamente fieles a la fuente. [IMP-BADGE-SOURCE-COLOR-FIGMA-001](implementations.md), [estado](../implementations/figma/badge.source-color.v0.1.2.state.json). Set `UNPUBLISHED`; web fuera del alcance.

### Publicación de uso · 0.2.0

- **Ruta candidata preservada:** [button.contract.v0.2.0.md](../drafts/contracts/button.contract.v0.2.0.md), SHA-256 bytes `c97cd24a1505236cfdac32d85a676d8eb2b4394ec074412305d7cfd3abf37ae5`; aprobación y publicación en [DEC-BUTTON-USAGE-002](decisions.md).
- **Estado documental:** `APPROVED`; versión 0.2.0 vigente. La versión 0.1.0 permanece como evidencia y baseline técnico referenciado.
- **Alcance añadido:** guías de type, size, state, etiqueta e iconos; Description aprobada en [texto fuente](../drafts/figma/button.description.v0.2.0.md), SHA-256 bytes `22ca686667bc9c815d461c6d1e246817b8861e04fb9e448440b96e478d98c56c`. El encabezado IN_REVIEW de ese borrador se conserva como estado histórico del candidato; la aprobación de sus bytes consta en DEC-BUTTON-USAGE-002.
- **Fuentes:** `SRC-BTN-CONFIG-001`, guías Material/Carbon/Apple/Tailwind y baseline Figma/Phosphor; véase [registro](sources.md).
- **Datos técnicos vinculados:** YAML 0.1.0 sin cambios, SHA-256 `734b85826ad4cb4c2caa08932e4364516a6e2f31f4be8e8ce6b0decda6ec4e1b`.
- **Reporte:** [SYN-BUTTON-USAGE-002](../drafts/reports/button-usage.v0.2.0.synthesis.md). **QA documental previo a aprobación:** [QA-BUTTON-USAGE-002](../qa/contracts/button-usage.v0.2.0.review.md), PASS para decisión humana; su bloqueo histórico de publicación quedó resuelto por DEC-BUTTON-USAGE-002.
- **Preparación Figma de 0.2.0:** `READY` para Description; preflight confirmó página única Buttons, set local de 60 variantes y Description/Link vacíos. Documentation link permanece `BLOCKED` por ausencia de URL pública verificable.
- **Implementación 0.2.0:** `VALIDATED` para Description del set dentro del archivo Figma, según [IMP-BUTTON-FIGMA-DOC-002](implementations.md) y [QA-BUTTON-FIGMA-USAGE-003](../qa/implementations/button-description.v0.2.0.figma.review.md). El set reporta estado de biblioteca `UNPUBLISHED`; no se afirma distribución a consumidores.
- **Enmienda semántica 0.2.1:** [AMD-BUTTON-SEMANTIC-SCOPE-001](../drafts/contracts/button.semantic-scope-amendment.v0.2.1.md), SHA-256 `6bc6d7f19e0597938bd57bca9faec273505b225bb262b0bfb575c19116144065`, `DELEGATED_FOR_BUILD` bajo DEC-SEMANTIC-EXTENSIONS-001; [QA documental](../qa/contracts/button.semantic-scope-amendment.v0.2.1.review.md) `PASS`. Corrige nueve textos Disabled con rol `color/text/disabled` sin cambio visual ni token nuevo. [QA Figma](../qa/implementations/button.semantic-scope.v0.2.1.figma.review.md) `PASS`; auditoría humana pendiente para este detalle, sin alterar la aprobación de 0.2.0.

## TOGGLE-001

- **Ruta delegada:** [Toggle 0.1.0](../drafts/contracts/toggle.contract.v0.1.0.md), SHA-256 `c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38`; [candidato preservado](../drafts/contracts/toggle.contract.v0.1.0.candidate.md), SHA-256 `95bc256260c71c32158b7d2d62f29e1cbafdd90176859a7903afe9dcc321f123`; [YAML fuente](../drafts/contracts/toggle.contract.v0.1.0.yaml), SHA-256 `4010c12aaae2784df134268f776a25f7cad1c26d4a6a09f35a1a9cb28fb320f0`.
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001; [QA-TOGGLE-001](../qa/contracts/toggle.v0.1.0.review.md) `PASS`, `user_audit: PENDING`.
- **Enmiendas:** [AMD-TOGGLE-CONTRAST-001 0.1.1](../drafts/contracts/toggle.contrast-amendment.v0.1.1.md), SHA-256 `35c1b1b55ed7fecc1d165896aa6c0b5be42953b2144e14cccf754197aac046ad`, histórica; [AMD-TOGGLE-VISUAL-CONTRAST-002 0.1.2](../drafts/contracts/toggle.visual-contrast-amendment.v0.1.2.md), SHA-256 `13674dd7d6f61efd015ae760b6a89bc71c80c323ff45e665fc4d48f8e89b9187`, vigente excepto para los dos strokes y su umbral sustituidos por 0.1.5. [QA documental 0.1.2](../qa/contracts/toggle.visual-contrast-amendment.v0.1.2.review.md) `PASS` histórico; dos roles adicionales se definen en el JSON de extensión de Foundations, sin alterar los datos históricos de origen.
- **Fuentes:** `SRC-FIGMA-TOGGLE-001`, JSON aprobado `SRC-TOKENS-INV-001`; [plan](../drafts/reports/toggle.v0.1.0.plan.md) y decisiones [DEC-TOGGLE-NORMALIZATION-001](decisions.md)/[DEC-TOGGLE-CONTRAST-001](decisions.md).
- **Enmienda de efectos vigente:** [AMD-TOGGLE-FOCUS-EFFECT-003 0.1.3](../drafts/contracts/toggle.focus-effect-amendment.v0.1.3.md), SHA-256 `07ae4f7700bd4670156e5be211f9476d97eb97e15275addd69198f5152cd6266`, `DELEGATED_FOR_BUILD` tras [QA-TOGGLE-AMD-003](../qa/contracts/toggle.focus-effect-amendment.v0.1.3.review.md) `PASS`. Solo sustituye los cuatro bindings de color de efecto; 0.1.2 sigue rigiendo los paints Off.
- **Ampliación y restauración:** [Mixed 0.1.4](../drafts/contracts/toggle.mixed-amendment.v0.1.4.md) añade cuatro variantes con [QA propio](../qa/implementations/toggle.mixed.v0.1.4.figma.review.md) `PASS`. [AMD-TOGGLE-SOURCE-COLOR-005 0.1.5](../drafts/contracts/toggle.source-color-amendment.v0.1.5.md), SHA-256 `4cdb03bf33078e3461c3fa8524b666700c14fdbd75fd88212cf7994e1a91f9dd`, restaura dos strokes Off sin tokens nuevos; [QA documental](../qa/contracts/toggle.source-color-amendment.v0.1.5.review.md) y [QA Figma](../qa/implementations/toggle.source-color.v0.1.5.figma.review.md) `PASS` **acotado**. El set tiene ahora doce variantes y permanece `UNPUBLISHED`. El barrido cromático global sigue `IN_PROGRESS` por el halo Focus sin primitiva exacta (AUD-003); no se promueve aún el contrato completo a `specs/` ni se afirma fidelidad total.
- **Historial de implementación:** [IMP-TOGGLE-FIGMA-001](implementations.md), [QA-TOGGLE-FIGMA-004](../qa/implementations/toggle.v0.1.2.figma.review.md) y [QA-TOGGLE-FIGMA-006](../qa/implementations/toggle.v0.1.3.figma.review.md) acreditaron ocho variantes, bindings de foco y scopes bajo la regla anterior. Su umbral cromático de Off está `SUPERSEDED` solo en el alcance 0.1.5; otras comprobaciones históricas no se borran. Web fuera de alcance; auditoría humana pendiente.

## FOUNDATIONS-FOCUS-EFFECTS-001

- **Ruta delegada:** [AMD-FOUNDATIONS-FOCUS-EFFECTS-001 0.1.2](../drafts/contracts/foundations.focus-effects.amendment.v0.1.2.md), SHA-256 `4ca4f11c6d858fe2237256019a8b9b4ea046e10b30021887a97a35128df1572d`; [candidato preservado](../drafts/contracts/foundations.focus-effects.amendment.v0.1.2.candidate.md), SHA-256 `da5437fb7406e9761636240f703baae663012a8d91d806acb0b2a990056e2fdf`.
- **JSON canónico de extensión:** [focus-effects 0.1.0](../drafts/foundations/ai-design-system.focus-effects.v0.1.0.json), SHA-256 `0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4`; datos históricos aprobados sin cambios.
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-SEMANTIC-EXTENSIONS-001; [QA-TOKENS-FOCUS-001](../qa/contracts/foundations.focus-effects.amendment.v0.1.2.review.md) `PASS`; auditoría humana `PENDING`.
- **Implementación Figma:** `VALIDATED` técnicamente: dos roles `EFFECT_COLOR`, ocho aliases a primitivas existentes, colección semántica 133 variables. [IMP-FOCUS-EFFECTS-FIGMA-001](implementations.md) y [QA-FOCUS-EFFECTS-FIGMA-001](../qa/implementations/focus-effects.v0.1.0.figma.review.md). Web fuera de alcance.

## FOUNDATIONS-RADIO-INDICATOR-COLORS-001

- **Ruta delegada:** [AMD-FOUNDATIONS-RADIO-INDICATOR-COLORS-001 0.1.3](../drafts/contracts/foundations.radio-indicator-colors.amendment.v0.1.3.md), SHA-256 `b0a3a629b3f20dc011ab1e2122e22f23b6353670c585534630f81d668bb42915`; [candidato preservado](../drafts/contracts/foundations.radio-indicator-colors.amendment.v0.1.3.candidate.md), SHA-256 `012d9b0ff4b967f3ae83892ed0e471de2729ec872e9936288eee4b0a72349867`.
- **JSON canónico:** [radio-indicator-colors 0.1.0](../drafts/foundations/ai-design-system.radio-indicator-colors.v0.1.0.json), SHA-256 `46f53dc329a93374f486ad26452cdd991c6cb0651a6c068865e34352d8e6161a`; inventario histórico fuente sin cambios.
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-SEMANTIC-EXTENSIONS-001; [QA documental](../qa/contracts/foundations.radio-indicator-colors.amendment.v0.1.3.review.md) `PASS`; auditoría humana `PENDING`.
- **Implementación Figma:** `VALIDATED` técnicamente: dos roles exclusivos `SHAPE_FILL`, ocho aliases a primitivas locales existentes y colección semántica 135. [Estado](../implementations/figma/radio-indicator-colors.v0.1.0.state.json) y [QA](../qa/implementations/radio-indicator-colors.v0.1.0.figma.review.md). Web fuera de alcance.

## RADIO-BUTTON-001

- **Ruta delegada:** [Radio Button 0.1.0](../drafts/contracts/radio-button.contract.v0.1.0.md), SHA-256 `f97d72ea3a8abe0c489aaa1a5f7289a4dc900f8c367601f7ccfc1b39651a29f2`; [candidato preservado](../drafts/contracts/radio-button.contract.v0.1.0.candidate.md), SHA-256 `6303f13b1e39e718d0d908a4deffef96a8f684f9b98d086ff4d20dc32f22d1d1`; [evidencia fuente MD/YAML](../drafts/contracts/radio-button.source.component-contract.md).
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA del origen](../qa/contracts/radio-button.source.component-contract.review.md) y [QA del destino](../qa/contracts/radio-button.v0.1.0.review.md) `PASS`; auditoría humana `PENDING`.
- **Fuente:** `SRC-FIGMA-RADIO-BUTTON-001`, JSON aprobado `SRC-TOKENS-INV-001`; dependencias `FOUNDATIONS-RADIO-INDICATOR-COLORS-001` y `FOUNDATIONS-FOCUS-EFFECTS-001`.
- **Implementación Figma:** `VALIDATED` técnicamente: página `Radio Buttons` `142:122`, helper `Radio Indicator` `142:144` y set público `Radio Button` `143:166`, ocho variantes cada uno, todos los bindings semánticos revisados. [Estado](../implementations/figma/radio-button.v0.1.0.state.json) y [QA](../qa/implementations/radio-button.v0.1.0.figma.review.md). `UNPUBLISHED`; web fuera de alcance.

## CHECKBOX-001

- **Ruta delegada:** [Checkbox 0.1.0](../drafts/contracts/checkbox.contract.v0.1.0.md), SHA-256 `bc189560b843aad787b5f17f38f51a60e4a2635955d111a176b9a5d81d2966bd`; [evidencia fuente MD](../drafts/contracts/checkbox.source.component-contract.md) y [YAML](../drafts/contracts/checkbox.source.component-contract.yaml).
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA fuente](../qa/contracts/checkbox.source.component-contract.review.md) y [QA destino](../qa/contracts/checkbox.v0.1.0.review.md) `PASS`; auditoría humana `PENDING`.
- **Fuente:** `SRC-FIGMA-CHECKBOX-001`, JSON aprobado `SRC-TOKENS-INV-001`, iconos de `SRC-FIGMA-PHOSPHOR-001` y extensiones semánticas existentes para selección y foco.
- **Implementación Figma:** `VALIDATED` técnicamente: página `Checkboxes` `149:122`, set `Checkbox` `149:199`, 12 variantes y bindings locales. [Estado](../implementations/figma/checkbox.v0.1.0.state.json) y [QA](../qa/implementations/checkbox.v0.1.0.figma.review.md). `UNPUBLISHED`; web fuera de alcance.

## FOUNDATIONS-DOT-BACKGROUND-COLORS-001

- **Ruta delegada:** [enmienda Foundations 0.1.4](../drafts/contracts/foundations.dot-background-colors.amendment.v0.1.4.md), SHA-256 `f93f3c648fe8d603265beab69a21a2860fee10b7b5211ea4a291d0f18d0998d5`; [JSON canónico](../drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json), SHA-256 `6b78e90c03bf1406807564569ccacdaae15c9ffa4e795b02c7dfdf7151a16667`.
- **Estado:** `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.dot-background-colors.amendment.v0.1.4.review.md) `PASS`, [QA Figma](../qa/implementations/dot-background-colors.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.
- **Implementación:** cuatro roles `FRAME_FILL`, 16 aliases a primitivas existentes y colección semántica 139. [Estado](../implementations/figma/dot-background-colors.v0.1.0.state.json).

## FOUNDATIONS-DOT-INACTIVE-BORDER-001

- **Ruta delegada:** [enmienda Foundations 0.1.5](../drafts/contracts/foundations.dot-inactive-border.amendment.v0.1.5.md), SHA-256 `c70003ac1b237b56bad5ef8b186e7c8dd42990e35c3288c5913258648ee99e2f`; [JSON canónico](../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.0.json), SHA-256 `edd8a4afe5f70502a395a5a1190aa11db3600b6a84472298f9b3a5e325f8c98a`.
- **Estado:** `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.dot-inactive-border.amendment.v0.1.5.review.md) `PASS`, [QA Figma](../qa/implementations/dot-inactive-border.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.
- **Implementación:** un rol `STROKE_COLOR` con cuatro aliases a neutral/500, colección semántica 140, tres consumidores Dot Inactive. [Estado](../implementations/figma/dot-inactive-border.v0.1.0.state.json).
- **Sustitución cromática vigente:** [Foundations 0.1.6](../specs/foundations/foundations.dot-inactive-border-source-color.amendment.v0.1.6.md), SHA-256 `184d8ee5be27cadc459cadf6227aba33326d386ad8f63b58cb51c5467de45b7e`; [JSON de override 0.1.1](../drafts/foundations/ai-design-system.dot-inactive-border.v0.1.1.json), SHA-256 `fa9d3408c87936c88f867de9ea037ecab7ad6b08886f2dc30c3b49aedd87aceb`. Sustituye solo cuatro aliases por neutral/100; identidad, scope y descripción intactos. [QA documental](../qa/contracts/dot.source-color-amendment.v0.1.2.review.md) y [QA Figma](../qa/implementations/dot.source-color.v0.1.2.figma.review.md) `PASS` técnico, auditoría humana pendiente.

## DOT-001

- **Ruta delegada publicada en `specs/`:** [Dot 0.1.0](../specs/components/dot.contract.v0.1.0.md), SHA-256 `31bc2874b34be08187163584701fc8a1be0d66b0479fadd304d81fa67ca2bc77`; [enmienda histórica de borde Inactive 0.1.1](../drafts/contracts/dot.inactive-border-amendment.v0.1.1.md), SHA-256 `5eb352bff505edc9b4298afb1ad6c42a3b11d63f4abdba52e294aaa0b3de4f0c`.
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA fuente](../qa/contracts/dot.source.component-contract.review.md), [QA destino](../qa/contracts/dot.v0.1.0.review.md) y [QA enmienda](../qa/contracts/dot.inactive-border-amendment.v0.1.1.review.md) `PASS`; auditoría humana `PENDING`.
- **Implementación Figma:** `VALIDATED` técnicamente: página `Dots` `155:122`, set `Dot` `155:144`, 15 variantes, 36 paints y cinco roles nuevos de categorías estrictas. [Estado](../implementations/figma/dot.v0.1.0.state.json) y [QA](../qa/implementations/dot.v0.1.1.figma.review.md). `UNPUBLISHED`; web fuera de alcance.
- **Color de origen vigente:** [enmienda Dot 0.1.2](../specs/components/dot.source-color-amendment.v0.1.2.md), SHA-256 `c336802895843eb6cfbc64b74dbfebcabfc767a766d821195723e13bfc8b3df7`, [estado](../implementations/figma/dot.source-color.v0.1.2.state.json), [QA](../qa/implementations/dot.source-color.v0.1.2.figma.review.md) y [QA de publicación](../qa/contracts/dot.specs-publication.v0.1.2.review.md) `PASS` técnico: cero desajustes cromáticos en 36 paints; contorno Inactive blanco restaurado. Limitación `*`; auditoría humana `PENDING`, set sin publicar.

## FOUNDATIONS-AVATAR-ROLES-001

- **Ruta delegada:** [enmienda Foundations 0.1.6](../drafts/contracts/foundations.avatar-roles.amendment.v0.1.6.md), SHA-256 `4604a1002076ff0613890411994ce89f39c05e46358abdfe268cd1277efc60fb`; [JSON canónico](../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json), SHA-256 `66a680bbb494895c76b43b9ca0d1b081c51afbb9c4dd079b6cf841c6488dc1f6`.
- **Estado:** `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.avatar-roles.amendment.v0.1.6.review.md) `PASS`, [QA Figma](../qa/implementations/avatar-roles.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.
- **Implementación:** dos roles `FRAME_FILL`/`FONT_SIZE`, ocho aliases a primitivas existentes, colección semántica 142. [Estado](../implementations/figma/avatar-roles.v0.1.0.state.json).
- **Override cromático vigente:** [Foundations 0.1.11](../drafts/contracts/foundations.avatar-fallback-source-color.amendment.v0.1.11.md), SHA-256 `a685925b9b9b680c56dddf58716119d9119a11aefb32612ad6b0ae98df9ac6de`; [JSON 0.1.1](../drafts/foundations/ai-design-system.avatar-roles.v0.1.1.json), SHA-256 `513d22e690587bf3be16ae71f16ac869d6cb00c6e1d2231ecc140169b486fa53`, sustituye solo el alias Servicios a orange/500. [QA documental](../qa/contracts/avatar.source-color-amendment.v0.1.1.review.md) y [QA Figma](../qa/implementations/avatar.source-color.v0.1.1.figma.review.md) `PASS` técnico; auditoría humana pendiente.

## AVATAR-001

- **Ruta delegada:** [Avatar 0.1.0](../drafts/contracts/avatar.contract.v0.1.0.md), SHA-256 `465296694978a14e8019b2f52af61f42b88f78fecfa480d0081d4f877e122396`; [evidencia fuente MD](../drafts/contracts/avatar.source.component-contract.md) y [YAML](../drafts/contracts/avatar.source.component-contract.yaml).
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA fuente](../qa/contracts/avatar.source.component-contract.review.md), [QA extensión](../qa/contracts/foundations.avatar-roles.amendment.v0.1.6.review.md) y [QA destino](../qa/contracts/avatar.v0.1.0.review.md) `PASS`; auditoría humana `PENDING`.
- **Implementación Figma:** `VALIDATED` técnicamente: página `Avatars` `165:198`, set `Avatar` `165:247`, 12 variantes, Dot/User reutilizados, muestra de imagen fuente y 48 paints semánticos. [Estado](../implementations/figma/avatar.v0.1.0.state.json) y [QA](../qa/implementations/avatar.v0.1.0.figma.review.md). `UNPUBLISHED`; web fuera de alcance.
- **Color de origen vigente:** [enmienda Avatar 0.1.1](../drafts/contracts/avatar.source-color-amendment.v0.1.1.md), SHA-256 `9e0c82ecd19a339c015e1ef539da08528740cc84e3e8721307115b5e609866ce`, [estado](../implementations/figma/avatar.source-color.v0.1.1.state.json) y [QA](../qa/implementations/avatar.source-color.v0.1.1.figma.review.md) `PASS` cromático técnico. Servicios orange/500 restaurado sin nuevo token; iniciales 6/9→10/12 px sujetas a AUD-006. Auditoría humana `PENDING`, set sin publicar.

## FOUNDATIONS-FEEDBACK-ICON-SCOPES-001

- **Ruta delegada:** [enmienda Foundations 0.1.7](../drafts/contracts/foundations.feedback-icon-scopes.amendment.v0.1.7.md), SHA-256 `416e624c0df854c162fe83434712f840c90b85411558c947cdeaa053ce26bd1c`; [JSON de override](../drafts/foundations/ai-design-system.feedback-icon-scopes.v0.1.0.json), SHA-256 `455adef5111796d6e14f97fdf310e768f5ac6bdb9190491714335a0c520dab2e`.
- **Estado:** `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.feedback-icon-scopes.amendment.v0.1.7.review.md) `PASS`, [QA Figma](../qa/implementations/feedback-icon-scopes.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.
- **Implementación:** tres roles feedback/icon existentes restringidos a `SHAPE_FILL`, sin cambio de descripción, aliases ni apariencia. [Estado](../implementations/figma/feedback-icon-scopes.v0.1.0.state.json).

## FOUNDATIONS-WARNING-ICON-CONTRAST-001

- **Ruta delegada:** [enmienda Foundations 0.1.8](../drafts/contracts/foundations.warning-icon-contrast.amendment.v0.1.8.md), SHA-256 `b6643cdc0617793392dbac0344372fadd77e2741e5f332ab0f4a740ea22fe4f6`; [JSON de aliases](../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.0.json), SHA-256 `059a9af5ef58c8d4e800da8fe657c13bdd9c92cf96bc7461d4daca03909a4ac4`.
- **Estado:** `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.warning-icon-contrast.amendment.v0.1.8.review.md) `PASS`, [QA Figma](../qa/implementations/warning-icon-contrast.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.
- **Implementación histórica:** el rol warning/icon aliasó amber/700 en cuatro modos para contraste 4.38:1. [Estado](../implementations/figma/warning-icon-contrast.v0.1.0.state.json). Sus cuatro aliases fueron sustituidos posteriormente por el override 0.1.1; 0.1.0 no es el dato vigente.

## FOUNDATIONS-WARNING-ICON-SOURCE-COLOR-002

- **Ruta delegada publicada en `specs/`:** [enmienda Foundations 0.1.10](../specs/foundations/foundations.warning-icon-source-color.amendment.v0.1.10.md), SHA-256 `2af932c330a1cf70a732e47bb4bd51abd78a34baeb8e0a9f8f3637dae471ea86`; [JSON de override vigente 0.1.1](../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.1.json), SHA-256 `565fddec17b67743a320d91beb3850e2166bbfc892ba81443cc0a4905e6b7887`, que sustituye únicamente aliases de 0.1.0. Auditoría humana pendiente; variable local no publicada.
- **Estado:** `DELEGATED_FOR_BUILD`, [QA documental](../qa/contracts/foundations.warning-icon-source-color.v0.1.10.review.md) y [QA Figma](../qa/implementations/warning-icon-source-color.v0.1.1.figma.review.md) `PASS`; auditoría humana `PENDING`.
- **Implementación:** rol existente warning/icon aliasa amber/600 en cuatro modos con scope `SHAPE_FILL`; ningún token nuevo. El vector Warning de Inline Notifications recuperó `#C97B00` y Badge Warning consume el mismo rol. Contraste original 2.96:1 marcado `*`.

## INLINE-NOTIFICATION-001

- **Ruta delegada publicada en `specs/`:** [Inline Notification 0.1.0](../specs/components/inline-notification.contract.v0.1.0.md), SHA-256 `2d732e7621da22e8aaf9055602ac194582bf84deeba9e9d23eea10649ecdb17e`; [evidencia fuente MD](../drafts/contracts/inline-notification.source.component-contract.md) y [YAML](../drafts/contracts/inline-notification.source.component-contract.yaml).
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA fuente](../qa/contracts/inline-notification.source.component-contract.review.md) y [QA destino](../qa/contracts/inline-notification.v0.1.0.review.md) `PASS`; auditoría humana `PENDING`.
- **Preparación Figma al preflight:** `READY` para `CREATE`; página `Inline Notifications` entonces ausente, 27 variables locales requeridas comprobadas, seis iconos Phosphor identificados, Manrope Regular/SemiBold disponible y Warning Icon Contrast ya validado. [Plan](../drafts/reports/inline-notification.v0.1.0.plan.md).
- **Implementación Figma:** `VALIDATED` técnicamente: página `Inline Notifications` `175:391`, set `Inline Notification` `175:432`, cinco variantes, 25 pinturas visibles con scope/categoría correctos. [Estado](../implementations/figma/inline-notification.v0.1.0.state.json) y [QA](../qa/implementations/inline-notification.v0.1.0.figma.review.md). `UNPUBLISHED`; auditoría humana pendiente; web fuera de alcance.
- **Enmienda Warning vigente:** [0.1.1](../specs/components/inline-notification.warning-source-color-amendment.v0.1.1.md), SHA-256 `064ee3d0de682fc8b00363aa91f26f24e75e3cc56bf436b2198eff7912378a33`, sustituye solo el alias/umbral amber/700 del contrato base por amber/600 fuente. [QA documental](../qa/contracts/inline-notification.warning-source-color.v0.1.1.review.md), [QA Figma](../qa/implementations/inline-notification.warning-source-color.v0.1.1.figma.review.md) y [QA de publicación](../qa/contracts/inline-notification.specs-publication.v0.1.1.review.md) `PASS` técnico. Pseudoenlace de fuente sin URL omitido conforme al contrato; Warning 2.96:1 `*`; auditoría humana pendiente.

## FOUNDATIONS-ICON-BUTTON-BACKGROUNDS-001

- **Ruta delegada:** [enmienda Foundations 0.1.9](../drafts/contracts/foundations.icon-button-backgrounds.amendment.v0.1.9.md), SHA-256 `185227fa124e6d593ce46b0afa80a6c62b0d737dc16a10b8686203e4594f2517`; [JSON canónico](../drafts/foundations/ai-design-system.icon-button-backgrounds.v0.1.0.json), SHA-256 `036d143ca6169355bb2ba345e80a9c6941ce545ef2fbabaae679f1a925201b0e`.
- **Estado:** `DELEGATED_FOR_BUILD` bajo DEC-SEMANTIC-EXTENSIONS-001, [QA documental](../qa/contracts/foundations.icon-button-backgrounds.amendment.v0.1.9.review.md) `PASS`; auditoría humana `PENDING`.
- **Implementación Figma:** `VALIDATED` técnicamente: dos roles de fondo Hover/Active exclusivos `FRAME_FILL` con ocho aliases locales, JSON/Figma concordantes. [Estado](../implementations/figma/icon-button-backgrounds.v0.1.0.state.json) y [QA](../qa/implementations/icon-button-backgrounds.v0.1.0.figma.review.md). Auditoría humana pendiente.

## ICON-BUTTON-001

- **Ruta delegada:** [Icon Button 0.1.0](../drafts/contracts/icon-button.contract.v0.1.0.md), SHA-256 `258c52e92035ed006e45d38476aa76b013283227f4444a3a9fd235e6f749fdc7`; [evidencia fuente MD](../drafts/contracts/icon-button.source.component-contract.md) y [YAML](../drafts/contracts/icon-button.source.component-contract.yaml).
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA fuente](../qa/contracts/icon-button.source.component-contract.review.md), [QA extensión](../qa/contracts/foundations.icon-button-backgrounds.amendment.v0.1.9.review.md) y [QA destino](../qa/contracts/icon-button.v0.1.0.review.md) `PASS`; auditoría humana `PENDING`.
- **Preparación Figma:** `READY` tras readback de dos roles nuevos; Dot Count destino y Bell Phosphor identificados. Página semántica `Icon Buttons`.
- **Implementación Figma:** `VALIDATED` técnicamente: 30 variantes, 30 Bell y 30 Dot Count anidados, 159 pinturas visibles con bindings semánticos correctos. [Estado](../implementations/figma/icon-button.v0.1.0.state.json) y [QA](../qa/implementations/icon-button.v0.1.0.figma.review.md). Auditoría humana pendiente; no publicado.

## BREADCRUMBS-001

- **Ruta delegada:** [Breadcrumbs 0.1.0](../drafts/contracts/breadcrumbs.contract.v0.1.0.md), SHA-256 `bc3e6527189481cb5ec909fc7c3ea7c3ae35fb629c3366bb79a748e4b5599806`; [ítem fuente MD/YAML](../drafts/contracts/breadcrumb-item.source.component-contract.md) y [composición fuente MD/YAML](../drafts/contracts/breadcrumbs.source.component-contract.md).
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA fuente ítem](../qa/contracts/breadcrumb-item.source.component-contract.review.md), [QA fuente composición](../qa/contracts/breadcrumbs.source.component-contract.review.md), [QA extensión](../qa/contracts/foundations.breadcrumb-current-text.amendment.v0.1.0.review.md) y [QA destino](../qa/contracts/breadcrumbs.v0.1.0.review.md) `PASS`. Auditoría humana `PENDING`.
- **Preparación Figma:** `READY`: página `Breadcrumbs` ausente en preflight, variables base leídas y rol Current JSON/Figma verificado antes de consumo.
- **Implementación Figma:** `VALIDATED` técnicamente: página `Breadcrumbs` `190:188`, sets `Breadcrumb item` `190:210` y `Breadcrumbs` `191:229`, diez variantes, 38 paints visibles con bindings/scope/categoría correctos, 14 instancias locales y contraste Current ≥5.56:1 en cuatro modos. [Estado](../implementations/figma/breadcrumbs.v0.1.0.state.json) y [QA](../qa/implementations/breadcrumbs.v0.1.0.figma.review.md). Ambos `UNPUBLISHED`; web fuera de alcance.

## FOUNDATIONS-BREADCRUMB-CURRENT-TEXT-001

- **Ruta delegada:** [enmienda de texto Current 0.1.0](../drafts/contracts/foundations.breadcrumb-current-text.amendment.v0.1.0.md), SHA-256 `f10deb6a36483ce22c260451c3a15b9e12112be2703c07d3ffeb01c1c7785746`; [JSON canónico](../drafts/foundations/ai-design-system.breadcrumb-current-text.v0.1.0.json), SHA-256 `b4ea10cbc0165d737a0dff9c75e8ce8de920b2084df31e722e5f9823e85c5603`.
- **Estado:** `DELEGATED_FOR_BUILD` bajo DEC-SEMANTIC-EXTENSIONS-001, [QA documental](../qa/contracts/foundations.breadcrumb-current-text.amendment.v0.1.0.review.md) y [QA Figma](../qa/implementations/breadcrumb-current-text.v0.1.0.figma.review.md) `PASS`; auditoría humana `PENDING`.
- **Implementación:** rol `TEXT_FILL` `color/text/breadcrumb/current` con cuatro aliases a primitivas existentes y cinco consumidores; corrige Servicios 3.24→7.20:1. [Estado](../implementations/figma/breadcrumb-current-text.v0.1.0.state.json).

## METRIC-CARD-001

- **Ruta delegada:** [Metric Cards 0.1.0](../drafts/contracts/metric-card.contract.v0.1.0.md), SHA-256 `f59add2d0f424d671d71a76890c980a9a8c15443c0d29903f71c4db046b7a3d9`.
- **Evidencia fuente:** [MD](../drafts/contracts/metric-card.source.component-contract.md), SHA-256 `431b99b91122c781b39f0bdedc1c63e24ef3cb3c15f62684607203f5dcbc1cbb`; [YAML](../drafts/contracts/metric-card.source.component-contract.yaml), SHA-256 `b57528bf6bc80298d484e931c82f2675fb8d0fb0c255eeeb980749d5a288eb88`.
- **Estado documental:** `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001 y DEC-SEMANTIC-EXTENSIONS-001; [QA fuente](../qa/contracts/metric-card.source.component-contract.review.md) y [QA destino](../qa/contracts/metric-card.v0.1.0.review.md) `PASS`; auditoría humana `PENDING`.
- **Preparación Figma:** `READY` para `CREATE`: página `Metric Cards` ausente en preflight, roles nuevos JSON/Figma leídos de vuelta, tokens base y Manrope Regular disponibles. [Plan](../drafts/reports/metric-card.v0.1.0.plan.md).
- **Implementación Figma:** `VALIDATED` técnicamente: página `Metric Cards` `202:208`, set `Metric Card` `202:327`, ocho variantes y 70/70 pinturas visibles vinculadas con scopes/categorías correctos. 36 textos, 16 iconos Phosphor, cuatro tendencias y 16 vectores ligados a roles nuevos; captura fuente/destino comparada. [Estado](../implementations/figma/metric-card.v0.1.0.state.json) y [QA](../qa/implementations/metric-card.v0.1.0.figma.review.md). `UNPUBLISHED`; auditoría humana pendiente.

## FOUNDATIONS-METRIC-CARD-ROLES-001

- **Ruta delegada:** [enmienda Foundations 0.1.0](../drafts/contracts/foundations.metric-card-roles.amendment.v0.1.0.md), SHA-256 `c3c038c6da9795fc8e41a4dfd0afe7c84c080bfcdcc272b33165110dcdd8af78`; [JSON canónico](../drafts/foundations/ai-design-system.metric-card-roles.v0.1.0.json), SHA-256 `61e3eb83c09cd8eef57da4dc7b30a3f425f7f22983a4231bc72e0540ac7f8df0`.
- **Estado:** `DELEGATED_FOR_BUILD` bajo DEC-SEMANTIC-EXTENSIONS-001; [QA documental](../qa/contracts/foundations.metric-card-roles.amendment.v0.1.0.review.md) y [QA Figma](../qa/implementations/metric-card-roles.v0.1.0.figma.review.md) `PASS` técnico. Auditoría humana `PENDING`.
- **Implementación:** dos roles exclusivos de texto/icono con cuatro aliases cada uno a primitivas existentes; JSON/Figma idénticos por readback. Cuatro textos Trend y 16 vectores iconográficos consumen ya los roles con categoría correcta. [Estado](../implementations/figma/metric-card-roles.v0.1.0.state.json).

## CHART-LABEL-CELL-001

- **Evidencia fuente:** [MD](../drafts/contracts/chart-label-cell.source.component-contract.md), SHA-256 `af7aa39f9885a799e4acc97a321640d21f5d37906a41054591e25848eda76aab`; [YAML](../drafts/contracts/chart-label-cell.source.component-contract.yaml), SHA-256 `2b583c9e1549720a77a99f3548d2e0a6581d2e5fbe843b5d416a6033ea4cd050`.
- **Estado documental:** `SOURCE_INSPECTED`, [QA fuente](../qa/contracts/chart-label-cell.source.component-contract.review.md) `PASS`. Adoptado por [CHARTS-001](../drafts/contracts/charts.contract.v0.1.0.md) y construido como Chart Legend Label; dependencia de Header/Progress con nueve instancias locales. [Estado](../implementations/figma/charts.v0.1.0.state.json).

## CHART-CELL-001

- **Evidencia fuente:** [MD](../drafts/contracts/chart-cell.source.component-contract.md), SHA-256 `1fd4832f581d51b94316ccda46d9b55e8fa7f937a375831c9d20b4ad06eb5843`; [YAML](../drafts/contracts/chart-cell.source.component-contract.yaml), SHA-256 `30cfba0f619e0ade4dffa09d3c62c32f541e414a6c2a739c7ac423d0c56ab583`.
- **Estado documental:** `SOURCE_INSPECTED`, [QA fuente](../qa/contracts/chart-cell.source.component-contract.review.md) `PASS`. Adoptado por [CHARTS-001](../drafts/contracts/charts.contract.v0.1.0.md) y construido como Chart Cell con 13 combinaciones. [Estado](../implementations/figma/charts.v0.1.0.state.json).

## CHART-PROGRESS-ITEM-001

- **Evidencia fuente:** [MD](../drafts/contracts/chart-progress-item.source.component-contract.md), SHA-256 `cf65a19048f2a4bb8cca26b18ef4d9c481ecdf5a8c665af318692f85252d335f`; [YAML](../drafts/contracts/chart-progress-item.source.component-contract.yaml), SHA-256 `4756bc0772bcf305d382cc9a06e55376d301bf6c740a0c2d3df510c0b28eb346`.
- **Estado documental:** `SOURCE_INSPECTED`, [QA fuente](../qa/contracts/chart-progress-item.source.component-contract.review.md) `PASS`. Adoptado por [CHARTS-001](../drafts/contracts/charts.contract.v0.1.0.md) y construido como Progress Chart Item con dos variantes. [Estado](../implementations/figma/charts.v0.1.0.state.json).

## CHART-DONUT-001

- **Evidencia fuente:** [MD](../drafts/contracts/chart-donut.source.component-contract.md), SHA-256 `302f1f6e17f4f8bd0985486066da16a4b224ae16f5617d173289d8d30dc22e4a`; [YAML](../drafts/contracts/chart-donut.source.component-contract.yaml), SHA-256 `4f451c4bef6c2e97b6cacd0adab104d7ee7b8fa94ca50ecb97bb22b839313a97`; [paths vectoriales](../sources/figma-snapshots/chart-donut.vector-paths.json), SHA-256 `60e22a15421f6be666e175bc64905074562f00453abb2032c3203c587c5ad764`.
- **Estado documental:** `SOURCE_INSPECTED`, [QA fuente](../qa/contracts/chart-donut.source.component-contract.review.md) `PASS`. Adoptado por [CHARTS-001](../drafts/contracts/charts.contract.v0.1.0.md) y construido como Semi-donut Gauge con tres valores y seis vectores. [Estado](../implementations/figma/charts.v0.1.0.state.json).

## CHART-HEADER-001

- **Evidencia fuente:** [MD](../drafts/contracts/chart-header.source.component-contract.md), SHA-256 `29ba17d5b763ce6ee011ddd915186f73acb137b507694965f1432ddc7749cff4`; [YAML](../drafts/contracts/chart-header.source.component-contract.yaml), SHA-256 `480ffeccca334481d61518a421709abebba4d33d0cf958a9eac10734e1274d91`.
- **Estado documental:** `SOURCE_INSPECTED`, [QA fuente](../qa/contracts/chart-header.source.component-contract.review.md) `PASS`. Adoptado por [CHARTS-001](../drafts/contracts/charts.contract.v0.1.0.md) y construido como Chart Header; `Ttile` fuente queda mapeado a `Title` destino. [Estado](../implementations/figma/charts.v0.1.0.state.json).

## FOUNDATIONS-CHART-COLORS-001

- **Contrato de extensión:** [enmienda](../drafts/contracts/foundations.chart-colors.amendment.v0.1.0.md) 0.1.0 `DELEGATED_FOR_BUILD`, SHA-256 `9b367f12ef1331397b1730e5a0781595d21dda6d87e6408a66f14b39249a8f25`; [JSON canónico](../drafts/foundations/ai-design-system.chart-colors.v0.1.0.json), SHA-256 `12768f8d7d3f786ece264678263a3acc94417255e4de34d23554ec762113b9e0`.
- **Alcance:** siete roles locales de fondo/shape exclusivos para Charts; dieciséis primitivas existentes, cuatro modos. [QA Figma](../qa/implementations/chart-colors.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.

## CHARTS-001

- **Contrato destino:** [Charts 0.1.0](../drafts/contracts/charts.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, SHA-256 `9e62e9a75b41d93e565a54061b98c03271c22ef863300c13b7b3bd76576ced0c`; [síntesis](../drafts/reports/charts.v0.1.0.synthesis.md), [plan](../drafts/reports/charts.v0.1.0.plan.md), [QA documental](../qa/contracts/charts.v0.1.0.review.md) `PASS`.
- **Alcance:** cinco piezas fuente → cuatro sets y un componente en la página `Charts`, 23 definiciones. [Implementación](../implementations/figma/charts.v0.1.0.state.json) y [QA final](../qa/implementations/charts.v0.1.0.figma.review.md) `VALIDATED` técnico; auditoría humana `PENDING`.

## LINEAR-PROGRESS-BAR-001

- **Evidencia fuente:** [MD](../drafts/contracts/linear-progress-bar.source.component-contract.md), SHA-256 `d14be5a10bf63a89554ef9891711686b629bdc1b4928cff7cbd5eae7e655ed5d`; [YAML](../drafts/contracts/linear-progress-bar.source.component-contract.yaml), SHA-256 `58f61d6ed10c85ba343fb75f8adbba086ca1d7e5f5834d7fab9d161f9ac6e295`.
- **Contrato destino:** [Linear Progress Bar 0.1.0](../drafts/contracts/linear-progress-bar.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, SHA-256 `aa7b726dab3095110884c4e7eb2c57e9cbcba04d76a61e2a66ed555c2d7f2ece`; [síntesis](../drafts/reports/linear-progress-bar.v0.1.0.synthesis.md), [plan](../drafts/reports/linear-progress-bar.v0.1.0.plan.md), [QA fuente](../qa/contracts/linear-progress-bar.source.component-contract.review.md) y [QA destino](../qa/contracts/linear-progress-bar.v0.1.0.review.md) `PASS` documental. Auditoría humana `PENDING`.
- **Implementación:** página `Linear Progress Bars` con 48 variantes y corrección de 36 porcentajes fuente. [Estado](../implementations/figma/linear-progress-bar.v0.1.0.state.json) y [QA final](../qa/implementations/linear-progress-bar.v0.1.0.figma.review.md) `VALIDATED` técnico, `UNPUBLISHED`.

## FOUNDATIONS-LINEAR-PROGRESS-COLORS-001

- **Contrato de extensión:** [enmienda](../drafts/contracts/foundations.linear-progress-colors.amendment.v0.1.0.md) 0.1.0 `DELEGATED_FOR_BUILD`, SHA-256 `0b416066e3f74e64c62b761bd0677e6337fcf6d755ebd72bdebcfbd610cafcd4`; [JSON canónico](../drafts/foundations/ai-design-system.linear-progress-colors.v0.1.0.json), SHA-256 `8dfbd5c2952bc47feabbf202687a69da14e60277f250b6493fe4222d5a66472b`.
- **Alcance:** cinco roles `color/background/progress/*` de scope `FRAME_FILL`, veinte aliases a primitivas existentes en cuatro modos; [QA documental](../qa/contracts/foundations.linear-progress-colors.v0.1.0.review.md) `PASS`, [QA Figma](../qa/implementations/linear-progress-colors.v0.1.0.figma.review.md) `PASS` técnico. Auditoría humana `PENDING`.

## FOUNDATIONS-CONTROL-BORDER-SOURCE-COLOR-002

- **Contrato vigente del ajuste:** [Foundations 0.1.12](../drafts/contracts/foundations.control-border-source-color.amendment.v0.1.12.md), SHA-256 `260b16db658d073d9c0bb2fd522d669b0263487fdb47e56cdeadb53a5dd3ba2b`; [JSON de override 0.1.1](../drafts/foundations/ai-design-system.control-colors.v0.1.1.json), SHA-256 `921e7cc9e375dbf5a5317dfd974afc33d7477e09b65a8631a6863305896be683`.
- **Alcance:** solo los cuatro aliases de `color/border/control` a neutral/400; el fondo hover no cambia. [QA documental](../qa/contracts/selection-control-source-color.v0.1.1.review.md) y [QA Figma acotado](../qa/implementations/selection-control-source-color.v0.1.1.figma.review.md) `PASS`; auditoría humana `PENDING`.

## AMD-CHECKBOX-SOURCE-COLOR-002 y AMD-RADIO-BUTTON-SOURCE-COLOR-002

- **Enmiendas vigentes:** [Checkbox 0.1.1](../drafts/contracts/checkbox.source-color-amendment.v0.1.1.md), SHA-256 `00b2de0d4fd7aedd3a41c5123cb611ea0a3ed10b466c29495ab63d0861862475`; [Radio Button 0.1.1](../drafts/contracts/radio-button.source-color-amendment.v0.1.1.md), SHA-256 `b8594caa29d2a8fbee73468e7c34a72e1d412064485018132156a8f4c36e23d1`.
- **Estado:** `DELEGATED_FOR_BUILD`; restauran tres contornos fuente sin cambiar nodos ni otros paints. [Readback](../qa/implementations/selection-control-source-color.v0.1.1.figma.review.md) `PASS` acotado. Revisión transversal de otras diferencias `IN_PROGRESS`; no promover aún los contratos completos a `specs/` ni afirmar aprobación humana.

## FOUNDATIONS-NAVIGATION-TAB-COLORS-001

- **Contrato de extensión:** [enmienda en specs](../specs/foundations.navigation-tab-colors.amendment.v0.1.13.md) 0.1.13 `DELEGATED_FOR_BUILD`, SHA-256 `5668f0dba66568c1781ccc734c4e7fc6a1b712496f6b56d3003e2d2bda16304a`; [JSON canónico](../drafts/foundations/ai-design-system.navigation-tab-colors.v0.1.0.json), SHA-256 `513f1dd9e009d09b1f42c270ce7354ccc2bcebc72dd51d0642a3415e269825bf`.
- **Alcance:** un rol `color/background/navigation-tab-active` de scope `FRAME_FILL`, cuatro aliases a primitivas existentes. [QA Figma](../qa/implementations/navigation-tab-colors.v0.1.0.figma.review.md) `PASS` técnico, auditoría humana `PENDING`.

## NAVIGATION-SWITCH-TAB-ITEM-001

- **Evidencia fuente:** [MD](../drafts/contracts/navigation-switch-tab-item.source.component-contract.md), SHA-256 `5114d57d5a031ef1b2e4b94b241989869629bde971aed7f95e14d608f6621510`; [YAML](../drafts/contracts/navigation-switch-tab-item.source.component-contract.yaml), SHA-256 `fce176b178a9e7702c8ffdfd62341775ecc6f8d8055e67560614daa224fc938f`.
- **Contrato destino:** [Switch Tab Item en specs](../specs/navigation-switch-tab-item.contract.v0.1.0.md) 0.1.0 `DELEGATED_FOR_BUILD`, SHA-256 `60d2caa198236e8a508711b185be780814187e2e72ff11f2a6eda30d9a4cb44b`; [QA documental](../qa/contracts/navigation-switch-tab-item.v0.1.0.review.md) `PASS`.
- **Implementación:** página `Navigation`, set con tres variantes y seis propiedades configurables. [Estado](../implementations/figma/navigation-switch-tab-item.v0.1.0.state.json) y [QA Figma](../qa/implementations/navigation-switch-tab-item.v0.1.0.figma.review.md) `VALIDATED` técnico; biblioteca `UNPUBLISHED`, auditoría humana `PENDING`. Las otras subfamilias de Navigation siguen pendientes.

## NAVIGATION-SWITCH-TAB-001

- **Evidencia fuente:** [MD](../drafts/contracts/navigation-switch-tab.source.component-contract.md), SHA-256 `9085b11b12b899d76321ed114782ddef946dcaf1f49138800c5a23f09c3666fa`; [YAML](../drafts/contracts/navigation-switch-tab.source.component-contract.yaml), SHA-256 `cce11d972640b709c930ddc3b10efe375972988527cc08e4d2bd7cfe306ab5d9`.
- **Contrato destino:** [Switch Tab en specs](../specs/navigation-switch-tab.contract.v0.1.0.md) 0.1.0 `DELEGATED_FOR_BUILD`, SHA-256 `c9007112a7155c155a5fc32ee8e809fa28576005069c8964f3205e9f77fb4cf1`; [QA documental](../qa/contracts/navigation-switch-tab.v0.1.0.review.md) `PASS`.
- **Implementación:** componente de cuatro instancias locales sobre fondo sutil original. [Estado](../implementations/figma/navigation-switch-tab.v0.1.0.state.json) y [QA Figma](../qa/implementations/navigation-switch-tab.v0.1.0.figma.review.md) `VALIDATED` técnico; biblioteca `UNPUBLISHED`, auditoría humana `PENDING`.

## FOUNDATIONS-NAVIGATION-PAGINATION-BORDER-001

- **Contrato de extensión:** [enmienda en specs](../specs/foundations.navigation-pagination-border.amendment.v0.1.14.md) 0.1.14 `DELEGATED_FOR_BUILD`, SHA-256 `6d8dd1cad02d905fe140a600e4ac416adf744623903c7cd62a4dce1c95754bad`; [JSON canónico](../drafts/foundations/ai-design-system.navigation-pagination-border.v0.1.0.json), SHA-256 `863f1711d70cb2f020680d89686693fcb1b2e65055afc017e9e10947c506f7c7`.
- **Alcance:** un rol `color/border/pagination/subtle` de scope `STROKE_COLOR`, cuatro aliases a primitivas existentes. [QA Figma](../qa/implementations/navigation-pagination-border.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.

## NAVIGATION-PAGINATION-001

- **Evidencia fuente:** [MD](../drafts/contracts/navigation-pagination.source.component-contract.md), SHA-256 `1f64b837e271cc9ffb1c8b5503bfc7e76451d02077bc15acfb6ab6ea029b0e9d`; [YAML](../drafts/contracts/navigation-pagination.source.component-contract.yaml), SHA-256 `ca6a57f32f520b6f040e37d5bab81ac164b0b867bb424e47647ffc8b8608c6c0`.
- **Contrato destino:** [Pagination en specs](../specs/navigation-pagination.contract.v0.1.0.md) 0.1.0 `DELEGATED_FOR_BUILD`, SHA-256 `314ad6b95a6938aa1c6527b22b867f8714d21bbf138a21956333d43c8f40c0ee`; [QA documental](../qa/contracts/navigation-pagination.v0.1.0.review.md) `PASS`.
- **Implementación:** página `Navigation`, set de cinco variantes y siete propiedades. [Estado](../implementations/figma/navigation-pagination.v0.1.0.state.json) y [QA Figma](../qa/implementations/navigation-pagination.v0.1.0.figma.review.md) `VALIDATED` técnico; biblioteca `UNPUBLISHED`, auditoría humana `PENDING`.

## FOUNDATIONS-NAVIGATION-TAB-BORDERS-001

- **Contrato de extensión:** [enmienda en specs](../specs/foundations.navigation-tab-borders.amendment.v0.1.15.md) 0.1.15 `DELEGATED_FOR_BUILD`, SHA-256 `697abca87e0794334d680b22b011280eb2f059fe9074cf6f7d44f7afbd87bcd2`; [JSON canónico](../drafts/foundations/ai-design-system.navigation-tab-borders.v0.1.0.json), SHA-256 `fe78ac2b642db5bb6f355dda93af1d6ecf54bb8c11c29c6249b6addfe949c2eb`.
- **Alcance:** dos roles `STROKE_COLOR` exclusivos de Tab, con aliases a primitivas existentes y paridad JSON/Figma. [QA](../qa/implementations/navigation-tab-borders.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.

## NAVIGATION-TAB-001

- **Evidencia fuente:** [MD](../drafts/contracts/navigation-tab.source.component-contract.md), SHA-256 `46b99bb3201dfb1fd089c4586f7dfe27c8ed7fa7ea1e38b7dc3f4db6ef0724d8`; [YAML](../drafts/contracts/navigation-tab.source.component-contract.yaml), SHA-256 `13e6ac5e13306ab5ab295ff117680dd787e3211e5e3949617427f51b6c960776`.
- **Contrato destino:** [Tab en specs](../specs/navigation-tab.contract.v0.1.0.md) 0.1.0 `DELEGATED_FOR_BUILD`, SHA-256 `1f28dbd13b0e5c055d2dc551e6a957b2b64f91701425d0b1089ef505c9b0035c`; [QA documental](../qa/contracts/navigation-tab.v0.1.0.review.md) `PASS`.
- **Implementación:** página `Navigation`, set de 17 variantes, diez propiedades y cuatro prototipos hover observados. [Estado](../implementations/figma/navigation-tab.v0.1.0.state.json) y [QA Figma](../qa/implementations/navigation-tab.v0.1.0.figma.review.md) `VALIDATED` técnico; biblioteca `UNPUBLISHED`, auditoría humana `PENDING`.

## SRC-FIGMA-SCROLLBAR-001

- **Evidencia fuente:** [MD](../drafts/contracts/scrollbar.source.component-contract.md), SHA-256 `923983a5722eae8e5eb94b0d76e19081d59a56a554f64a8282850456f8415679`; [YAML](../drafts/contracts/scrollbar.source.component-contract.yaml), SHA-256 `4f41c96a75bd2ceed19f46da83c75a7caa990288589e91c38f49a7051d4e1f19`.
- **Estado:** `SOURCE_INSPECTED`, [QA de inventario](../qa/contracts/scrollbar.source.component-contract.review.md) `PASS`. Cinco sets y 30 variantes observadas; el nombre `75%` no equivale a su longitud real.

## FOUNDATIONS-SCROLLBAR-COLORS-001

- **Histórico 0.1.16:** [enmienda exacta](../specs/foundations.scrollbar-colors.amendment.v0.1.16.md) `SUPERSEDED`, SHA-256 `c058c25f24e30fc267e82985d2628728410bd182c58e66437837345563807a68`; [JSON 0.1.0](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json) `SUPERSEDED`, SHA-256 `8b86b86a81d5afbe419567619aa4b150a4ad9d1a8b1cc13717b501925849ad88`.
- **Vigente 0.1.17:** [enmienda de alias](../specs/foundations.scrollbar-colors.amendment.v0.1.17.md) `DELEGATED_FOR_BUILD`, SHA-256 `790c8dac21d8283c1999417fda1bced23448bcf822595d2cc95c83ed3259561f`; [JSON 0.1.1](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json), SHA-256 `22d7e5f428732ce8158267873c0e10d52311d748a7a5a7f4ac64a40010ac78d4`.
- **Alcance:** el rol de fondo `SHAPE_FILL` aliasa neutral/300 existente en cuatro modos; primitiva 350 retirada del inventario local. [QA vigente](../qa/implementations/scrollbar-colors.v0.1.1.figma.review.md) `PASS` técnico; auditoría humana `PENDING`.

## SCROLLBAR-001

- **Contrato base:** [Scrollbar 0.1.0](../specs/scrollbar.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, SHA-256 `64326d0219578049084a46beed5181bfee13eba4b1c801a95098ce1b390cf9f9`; [QA documental](../qa/contracts/scrollbar.v0.1.0.review.md) `PASS`.
- **Enmienda cromática vigente:** [0.1.1](../specs/scrollbar.color-approximation.amendment.v0.1.1.md), SHA-256 `9706debe1203c2b29bd58d646060744be24bddcf5ad16b65ca9ca039f40b173e`; [QA documental](../qa/contracts/scrollbar.color-approximation.v0.1.1.review.md) `PASS`. Sustituye solo la exigencia de primitiva exacta/`AC-SB-003` del contrato base.
- **Implementación:** página `Scrollbars`, ocho variantes públicas, 22 internas, 30/30 thumbs vinculados al rol. [Estado vigente](../implementations/figma/scrollbar.v0.1.1.state.json) y [QA Figma](../qa/implementations/scrollbar.v0.1.1.figma.review.md) `VALIDATED` técnico; diferencia cromática documentada, biblioteca `UNPUBLISHED`, auditoría humana `PENDING`.

## MIGRATION-TOKEN-TRACEABILITY-001 · enmiendas de primitiva ausente

- **Histórico 0.1.1:** [enmienda](../specs/MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.1.md) `SUPERSEDED`, SHA-256 `36c249756d45c8e63083d7a8f66c07ef6b92aa9f9a561e1125ba79cdd9773908`.
- **Vigente 0.1.2:** [enmienda](../specs/MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.2.md) `DELEGATED_FOR_BUILD`, SHA-256 `19874f1a561e64e363e8a4cc24fe81588a5eb8adacfbd57efcfc4ccc95b59362`; [QA documental](../qa/contracts/migration-token-traceability.amendment.v0.1.2.review.md) `PASS`. Para RGB fuente sin primitiva exacta, prioriza la existente más cercana y exige alias semántico, JSON, readback y diferencia visual registrada.

## FOUNDATIONS-STEPS-COLORS-001

- **Histórico:** [Steps colors 0.1.18](../specs/foundations.steps-colors.amendment.v0.1.18.md) `SUPERSEDED`, SHA-256 `11df74a046e354d652d32853bdc604889a12e1948fef12b917398fcd2ddffc26`; [JSON 0.1.0](../drafts/foundations/ai-design-system.steps-colors.v0.1.0.json) `SUPERSEDED`, SHA-256 `51993b9e1c2c25c3686e3ac12b7c190646c707c15391c2fd1d1fa547a9a96212`.
- **Vigente:** [Steps brand 0.1.21](../specs/foundations.steps-brand.amendment.v0.1.21.md) `DELEGATED_FOR_BUILD`, SHA-256 `e10a4813dd23f931b6c718871d61364ac6f8337ae8c3590398d279193e9bc3f0`; [JSON 0.1.1](../drafts/foundations/ai-design-system.steps-colors.v0.1.1.json), SHA-256 `a02f22afaf3966a08d559e6420a7bdcec6f60bc2ef83b5cc80ece78b0cd69e33`.
- **Alcance:** siete roles del scope correcto y 28 aliases a primitivas existentes en cuatro modos; tres acentos temáticos, cuatro roles neutros/blancos preservados y cero variables/primitivas nuevas. Auditoría humana `PENDING`.

## STEPS-001

- **Fuente:** [MD](../drafts/contracts/steps.source.component-contract.md), SHA-256 `7aef8f2392868bfafdd4629f429963d7a5e2d3fce6f8a4e413a02b16b5702d07`; [YAML](../drafts/contracts/steps.source.component-contract.yaml), SHA-256 `a30cbe261720dd35f6806ec4d3c2d9a702b867b7b365cc424f462078839405ff`.
- **Contrato destino:** [Steps base 0.1.0](../specs/steps.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, SHA-256 `dad5b88393048c35391c09a5a13369849adf5b6fb9f1bfdd9fe16847690697e9`; [enmienda de marca 0.1.1](../specs/steps.brand-theme.amendment.v0.1.1.md) `DELEGATED_FOR_BUILD`, SHA-256 `d13f98fb092e845e72844ccf7f0936816d3f3cdba8a432d4e68b22bbe3bbcc8b`; [QA documental vigente](../qa/contracts/steps.brand-theme.v0.1.1.review.md) `PASS`.
- **Implementación:** página `Steps`, 6 variantes públicas, 4 Dot y 27 Combination. [Estado vigente](../implementations/figma/steps.v0.1.1.state.json) y [QA Figma](../qa/implementations/steps.v0.1.1.figma.review.md) `VALIDATED` técnico; estado anterior `STALE` para color, biblioteca `UNPUBLISHED`, auditoría humana `PENDING`.

## FOUNDATIONS-STEPPER-COLORS-001

- **Histórico:** [Stepper colors 0.1.19](../specs/foundations.stepper-colors.amendment.v0.1.19.md) `SUPERSEDED`, SHA-256 `b26933599cb2af865e72208db74707095973c18bf96d02eb11dcc725a022a357`; [JSON 0.1.0](../drafts/foundations/ai-design-system.stepper-colors.v0.1.0.json) `SUPERSEDED`, SHA-256 `c66a786d6c92ff73bbbabe3ee7016899eb0fd3ad2c79aeae8cd387cb0d55fb18`.
- **Vigente:** [Stepper brand 0.1.20](../specs/foundations.stepper-brand.amendment.v0.1.20.md) `DELEGATED_FOR_BUILD`, SHA-256 `93479bc761ce8eaf42fe9ade3ba7bc361036d002edd64dfbf90fa84c7f62527e`; [JSON 0.1.1](../drafts/foundations/ai-design-system.stepper-colors.v0.1.1.json), SHA-256 `ba53e25baec0fa80d9f53e30ca3f5cec5e9e85563cfcc7e1b138cc74018bea14`.
- **Alcance:** ocho roles de fondo, forma y texto; tres acentos alineados con marca base/fuerte en cuatro temas, cinco roles neutros preservados, cero variables/primitivas nuevas. Auditoría humana `PENDING`.

## STEPPER-001

- **Fuente:** [MD](../drafts/contracts/stepper.source.component-contract.md), SHA-256 `54b7b1a91c8a0ed4a423ed2d454e74b3e0b02ac3518f77d43415f0eaa4efd153`; [YAML](../drafts/contracts/stepper.source.component-contract.yaml), SHA-256 `d38f8a02ef9eb19f4948d297b63c1244c48ee1aad79dcac2ffc790c84450de04`.
- **Contrato base:** [Stepper Item 0.1.0](../specs/stepper.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, SHA-256 `5c3f8d75fe20736fd08411654db5757ea9517af6dd6b078234a17627bac19466`; QA documental 0.1.0 histórico para acentos fijos.
- **Enmienda vigente:** [Stepper marca 0.1.1](../specs/stepper.brand-theme.amendment.v0.1.1.md) `DELEGATED_FOR_BUILD`, SHA-256 `de9981eddd06b1c39b1f0830fa2f298a09d8d63511fb6e078f88023f3081c6bf`; [QA documental](../qa/contracts/stepper.brand-theme.v0.1.1.review.md) `PASS`.
- **Implementación:** página `Steppers`, 18 variantes públicas y ocho conectores. [Estado vigente](../implementations/figma/stepper.v0.1.1.state.json) y [QA Figma](../qa/implementations/stepper.v0.1.1.figma.review.md) `VALIDATED` técnico; biblioteca `UNPUBLISHED`, auditoría humana `PENDING`.

## LOADER-001

- **Fuente:** [MD](../drafts/contracts/loader.source.component-contract.md), SHA-256 `c9435904cf805b2b51759c96a6a4f7778a6c5fccb997118c21120052dfeef3be`; [YAML](../drafts/contracts/loader.source.component-contract.yaml), SHA-256 `f9ec5a35627c9f537dacb85f1eb7c3de9bd736e3a7be9ef7b5e8b4516f77a67d`.
- **Contrato destino:** [Loader 0.1.0](../specs/loader.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, SHA-256 `2e20f1d300bef2c53acbbf79b400343efb344fb47a555b45e2afed62099bcf6b`; [QA documental](../drafts/reports/loader.contract-qa.v0.1.0.md) `PASS`.
- **Implementación:** página `Loaders`, 16 variantes públicas y 16 ciclos internos de 24. [Estado](../implementations/figma/loader.v0.1.0.state.json) y [QA Figma](../qa/implementations/loader.v0.1.0.figma.review.md) `VALIDATED` técnico; biblioteca `UNPUBLISHED`, auditoría humana `PENDING`. DEC-LOADER-COLOR-CYCLE-001 documenta la corrección del cambio involuntario de color durante el ciclo fuente.

## SEARCH-001 · histórico 0.1.0, sustituido por 0.1.1

- **Contrato histórico:** [Search 0.1.0](../specs/search.contract.v0.1.0.md), DELEGATED_FOR_BUILD; SHA-256 bfad6fc189a4ae56c422eff7089fec69236978da51b41c1a1f0cf991de8ba60c. QA histórico acotado; sus cláusulas cruzadas no son vigentes. [Search0.1.1](../specs/search.contract.v0.1.1.md) y su entrada superior gobiernan; auditoría humana PENDING.
- **Destino:** Input Fields 394:122, set 418:263, 12 variantes. [Estado](../implementations/figma/search.v0.1.0.state.json) VALIDATED. Sin tokens/primitivas nuevos; biblioteca UNPUBLISHED.
- **Fuente:** [MD](../drafts/contracts/search.source.component-contract.md), SHA-256 76a123f558e1d9d18aaa0d5b98afa7609786ce4a2285a3645a45dbf5abe39a60; [YAML](../drafts/contracts/search.source.component-contract.yaml), SHA-256 c74b5aa9a2b290c4d2e65abc1091fd342c1df050c3ffefcd592c74db06d919fe. Ajustes posteriores directamente en specs.

## TEXTAREA-001

- **Contrato vigente:** [Textarea 0.1.0](../specs/textarea.contract.v0.1.0.md), DELEGATED_FOR_BUILD; SHA-256 5458ad9a5e9352e58b77106c40dd8df272cf07c4bd5534a59337926be943a1fa. QA documental/técnico PASS, auditoría humana PENDING.
- **Destino:** Input Fields 394:122, set 419:247, 4 variantes. [Estado](../implementations/figma/textarea.v0.1.0.state.json) VALIDATED. Sin tokens/primitivas nuevos; biblioteca UNPUBLISHED.
- **Fuente:** [MD](../drafts/contracts/textarea.source.component-contract.md), SHA-256 99c6857dc9e9803a36d7df37949b46bff7ccb83f3967562612b2652fcaa0cb5c; [YAML](../drafts/contracts/textarea.source.component-contract.yaml), SHA-256 61f978f09a77a043ebb379c6c5d8110f179c28904d00b3fe103c167aa82121a1. Ajustes posteriores directamente en specs.

## FILE-UPLOAD-001

- **Contrato vigente:** [File Upload 0.1.0](../specs/file-upload.contract.v0.1.0.md), DELEGATED_FOR_BUILD; SHA-256 e069fb28b37cb08c73300ace453d5318858f912f078566e87c731cc874ae4fb5. QA documental/técnico PASS, auditoría humana PENDING.
- **Destino:** Input Fields 394:122, set 420:320, 6 variantes. [Estado](../implementations/figma/file-upload.v0.1.0.state.json) VALIDATED. Sin tokens/primitivas nuevos; biblioteca UNPUBLISHED.
- **Fuente:** [MD](../drafts/contracts/file-upload.source.component-contract.md), SHA-256 ffb9396be18417267141808bf9fc11d86ef48a5a09b61dce9fbea39eaa5aa2eb; [YAML](../drafts/contracts/file-upload.source.component-contract.yaml), SHA-256 03c254f980dd4afba8e86da223c773f66c13adce81d749952e74494034f3e547. Ajustes posteriores directamente en specs.

## INPUT-FIELD-001

- **Enmienda vigente 0.1.1:** [texto Disabled](../specs/input-field.disabled-text.amendment.v0.1.1.md), APPROVED solo para este cambio; SHA-256 fc73aef18bd2c4ca6fcdd4eaa17d92c9e65aee0f4e54ff993eb9aeefc0f98a45. Sustituye el texto primary de Filled/Disabled en REQ-IF-005, mapa y ejemplo; el contrato base restante sigue vigente y pendiente de auditoría. [QA 0.1.1](../qa/implementations/input-field.v0.1.1.figma.review.md) PASS.

- **Contrato vigente:** [Input Field 0.1.0](../specs/input-field.contract.v0.1.0.md), DELEGATED_FOR_BUILD; SHA-256 e01e90d9dbc4dfdfc4230aac875f8d8a7374673b0a02bbda44eabf9962403c2d. Promoción documental por QA, no aprobación humana.
- **Fuente:** SRC-FIGMA-INPUT-FIELD-001; JSON base y extensión de foco existentes; 33 roles/132 aliases verificados, sin nuevas variables.
- **QA:** [documental](../qa/contracts/input-field.v0.1.0.review.md) y [Figma](../qa/implementations/input-field.v0.1.0.figma.review.md) PASS técnico.
- **Implementación:** página Input Fields, set 397:152, 30 variantes, doce propiedades. [Estado base](../implementations/figma/input-field.v0.1.0.state.json) y enmienda0.1.1 superior; auditoría humana PENDING por excepciones, biblioteca UNPUBLISHED. Los ajustes posteriores se hacen en specs. Search/Textarea/File Upload están cerrados en las entradas propias de este registro.

## CHAT-TOOLBAR-001 · CHAT-TOOL-ITEM-001 · CHAT-HISTORY-ITEM-001 · 2026-10-08

Tres contratos v0.1.0 promovidos a specs: [Toolbar](../specs/chat-toolbar.contract.v0.1.0.md), [Tool Item](../specs/chat-tool-item.contract.v0.1.0.md), [History Item](../specs/chat-history-item.contract.v0.1.0.md). DELEGATED_FOR_BUILD por delegación externa; auditoría humana PENDING. QA documental y técnico PASS, nueve variantes. [Continuidad](./SESSION-HANDOFF-2026-10-08-CHAT-TOOLBAR.md).

## FUENTES-001 · FOUNDATIONS-FUENTES-HOVER-001 · 2026-10-09

[Fuentes0.1.0](../specs/components/fuentes.contract.v0.1.0.md) y [rol Hover0.1.0](../specs/foundations/fuentes-hover.contract.v0.1.0.md) promovidos a specs tras [QA documental](../qa/contracts/fuentes.v0.1.0.review.md) y [QA técnico](../qa/implementations/fuentes.v0.1.0.review.md) PASS. DELEGATED_FOR_BUILD por delegación externa; humana PENDING. Fuente Navi64:4164; dos estados, Path Slot nativo, Dot local sin modificación. [Estado](../implementations/figma/fuentes.v0.1.0.state.json).


## CONVERSATION-COMPOSER-SLOT-001 · 0.1.3 · 2026-10-20

[Enmienda](../specs/components/conversation.composer-slot.amendment.v0.1.3.md), base CONVERSATION-001. DELEGATED_FOR_BUILD tras [QA documental PASS](../qa/contracts/conversation-composer.v0.1.3.review.md). Sustituye solo la estructura fija del aviso CCA0.1.2 por Notice content; usuario confirmó texto y acciones. No reemplaza toda la familia. user_audit: NOT_REQUIRED; human_review_policy: OPTIONAL_NON_BLOCKING.

## APP-SHELL-EMBEDDED-CHAT-001 · 0.1.1 · 2026-10-20

DELEGATED_FOR_BUILD para arquitectura de chats embebidos, por DEC-EMBEDDED-CHAT-ARCHITECTURE-001. Amplía App Shell y documenta herencia de Chat Layout0.1.1 y composición con Toolbar/Conversation; no redefine sus principales. Consumo documental READY; normalización integral y construcción de otra pantalla no ejecutadas. [Enmienda](../specs/components/app-shell.embedded-chat.amendment.v0.1.1.md); [QA documental](../qa/contracts/app-shell.embedded-chat.v0.1.1.review.md). user_audit: NOT_REQUIRED; human_review_policy: OPTIONAL_NON_BLOCKING.
