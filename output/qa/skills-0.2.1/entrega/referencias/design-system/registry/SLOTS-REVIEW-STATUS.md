# Revisión de Slots · estado de adopción

## Chat · actualización de layout2026-10-09

REQUIRED/IMPLEMENTED como estructura observada:12 Slots propios entre Section y Toolbar;40 incluyendo anidados, sin limitViolations. Messages Active pasa a FILL vertical/overflow VERTICAL. La edición0/1/3/5 histórica no se reejecutó; scrolling con desborde real no validado. [Enmienda](../specs/components/chat.layout.amendment.v0.1.1.md), [QA](../qa/implementations/chat-layout.v0.1.1.review.md). Sin límites de cardinalidad nuevos, sin construir Slots adicionales ni reconstrucción global.

## Characters · 2026-10-08

BENI Standby y NAVI Analysis: NOT_APPLICABLE. Anatomía ilustrativa fija; ojos/sombras no son regiones extensibles. [Contrato](../specs/characters.contract.v0.1.0.md), [QA](../qa/implementations/characters.v0.1.0.review.md).13 variantes, sin slots artificiales.

## Chat Section · 2026-10-08

P-SLOTS0.1.0 REQUIRED/IMPLEMENTED: Messages y Suggestions en cada variante (cuatro Slots propios), además de Slots heredados de Composer. [Contrato](../specs/chat-section.contract.v0.1.0.md), [pruebas](../qa/implementations/chat-section.v0.1.0.slots.json), [readback asentado](../qa/implementations/chat-section.v0.1.0.final.json).0/1/3/5, insertar/quitar/reordenar/sustituir, State preserva overrides. Vacío puede conservar altura residual; no política de negocio inferida. No detach ni modificaciones a maestros reutilizados.

## Conversation · 2026-10-08

REQUIRED e IMPLEMENTED: cinco Slots por Response BENI/NAVI y Draft/Tools en Composer, doce nodos nativos; siete propiedades funcionales compartidas por tipo de anfitrión.0..n sin máximo ficticio, pruebas desde instancia0/1/muestra/más, reordenar/sustituir, texto largo y360px, conservación de Body BENI→NAVI. [Contrato](../specs/conversation.contract.v0.1.0.md), [evidencia](../qa/implementations/conversation.v0.1.0.slots.json). No detach, clones temporales retirados; muestra no limita cardinalidad. Message/Preview/glifos NOT_APPLICABLE: anatomía fija con texto o iconografía, no composición arbitraria.

## App Shell · 2026-10-06

REQUIRED e IMPLEMENTED: Content#737:1, Slot nativo737:447 en main737:304, página737:303. Default vacío,0..n sin máximo ficticio. Inserción/reordenación/eliminación/sustitución/reset desde consumidor comprobados;12casos en dos tamaños desktop y SidebarCollapsed/Expanded. [Contrato](../specs/app-shell.contract.v0.1.0.md), [QA](../qa/implementations/app-shell.v0.1.0.figma.review.md). Slots internos de Header/Sidebar conservan propietarios y contratos, sin reconstrucción. Humana PENDING.

## Chips · refinamiento 2026-10-05

NOT_APPLICABLE conforme a P-SLOTS0.1.0: una etiqueta editable y dos posiciones fijas opcionales con swaps. No lista de cantidad variable. [Enmienda0.2.1](../specs/components/filter-chip.semantic.amendment.v0.2.1.md) precisa la terminología sin introducir Slots ficticios ni modificar la composición.

## Buttons · refinamiento 2026-10-05

NOT_APPLICABLE conforme a P-SLOTS0.1.0: etiqueta editable y dos posiciones fijas de icono con Boolean/INSTANCE_SWAP. La palabra histórica “slot” no implica Slot nativo ni cardinalidad variable. [Enmienda0.2.2](../specs/components/button.local-bindings.amendment.v0.2.2.md). Ningún cambio a Slots de Modal/Empty states; su regresión de estructura/API/overrides pasa en el alcance comprobado.

## Search · refinamiento 2026-10-05

[Search0.1.1](../specs/search.contract.v0.1.1.md): NOT_APPLICABLE. Anatomía fija de control, texto y swaps individuales; no lista variable de resultados. Confirmado con fuente y destino; no se añadió un Slot nominal ni se modificó Figma. Sustituye cualquier ambigüedad causada por cláusulas ajenas del contrato0.1.0.

## Empty states · 2026-10-05

REQUIRED e IMPLEMENTED: Main actions ySupporting actions, dos propiedades compartidas/ochoSlots nativos.64operaciones y16transiciones PASS conservando contenido, orden ytexto. Cardinalidad0..n, fixtures0/1/2/5 no son límites. Ilustración única/textos/artwork NOT_APPLICABLE: swaps/booleanas/TEXT. [Contrato](../specs/empty-states.contract.v0.1.0.md), [QA](../qa/implementations/empty-states.v0.1.0.figma.review.md). Esta entrada sustituye Empty statesUNRESOLVED histórico; Sidebar ya cerrado arriba delhistorial. [Continuación vigente](SESSION-HANDOFF-2026-10-05-EMPTY-STATES.md).

## Sidebar · 2026-10-05

REQUIRED e IMPLEMENTED: Sidebar/Menu items, Sidebar/Lower options yTop bar/Menu items. Cinco nodos Slot en tres propiedades públicas;16checks PASS de vacío, inserción superior al ejemplo, reordenamiento, sustitución y retenciónExpanded↔Collapsed. Menu Item NOT_APPLICABLE (anatomía fija con texto/swaps/booleana). [Contrato](../specs/sidebar.contract.v0.1.0.md), [QA](../qa/implementations/sidebar.v0.1.0.slots.json). El contenedor no transforma automáticamente la presentación de hijos personalizados. Esta entrada sustituye SidebarUNRESOLVED histórico, noEmpty states.

2026-10-01 · Protocolo [P-SLOTS 0.1.0](../protocols/SLOTS-REVIEW-AND-IMPLEMENTATION.md). Esta cola registra adopción y trabajo pendiente; no reemplaza contratos ni QA. Header, Table y Modal se suman al cierre anterior de seis composiciones.

| Familia | Aplicabilidad | Estado de adopción | Evidencia y siguiente acción |
|---|---|---|---|
| Table (Anticipa) | REQUIRED: Rows, Header/Cells, Row/Cells, Actions | IMPLEMENTED; QA acotado PASS | Página546:122, Table548:895.0/1/5/10/12filas,0/1/3/7/9celdas y0/1/2/3acciones. RetenciónDefault↔Hover y reordenamiento/restauración probados. [Contrato](../specs/table.contract.v0.1.0.md), [QA](../qa/implementations/table.v0.1.0.figma.review.md). |
| Select / Dropdown | REQUIRED | IMPLEMENTED; QA Slots PASS | Slot Options#466:0, set457:470;1/3/5/8/0 opciones probadas. [Enmienda](../specs/composition-slots.amendment.v0.1.0.md), [QA](../qa/implementations/composition-slots.v0.1.0.figma.review.md). |
| Switch Tab | REQUIRED | IMPLEMENTED; QA Slots PASS | Slot Tabs#468:0, componente283:128;1/2/4/7/0 pestañas. La selección sigue manual. Contrato base specs/navigation-switch-tab.contract.v0.1.0.md más la enmienda. |
| Breadcrumbs · composición | REQUIRED | IMPLEMENTED; QA Slots PASS | Slot Trail#470:0, set191:229;1/3/5/8/0 elementos; persisten al cambiar Level. Ajuste HUG en cuatro ítems documentado. Base drafts/contracts/breadcrumbs.contract.v0.1.0.md más enmienda en specs. No revalida su paleta histórica. |
| Steps · Gallery/Gallery only | REQUIRED | IMPLEMENTED; QA Slots PASS | Indicators#487:0 en 27 presets Combination y Legacy indicators#487:28; 0/1/2/3/9 indicadores. Se conservan seis públicos y roles de marca; contextos legacy separados. Numbers no muestra indicadores. [Enmienda0.1.1](../specs/composition-slots.amendment.v0.1.1.md), [QA](../qa/implementations/composition-slots.v0.1.1.figma.review.md). |
| Pagination · Pages | REQUIRED | IMPLEMENTED; QA Slots PASS | Pages#496:0 en cinco variantes; 0/1/2/4/8 celdas. Nueve tokens contextuales permiten heredar Disabled sin perder contenido; cero colores nuevos y 200 comparaciones sin diferencias. Defaults354×66. No algoritmo de elipsis/selección. [Estado](../implementations/figma/composition-slots.v0.1.1.state.json). |
| Charts · leyendas | REQUIRED | IMPLEMENTED; QA Slots PASS | Header Legend#486:0 y Progress Legend rows#502:0; Top oculta las filas preservando contenido. Header0/1/2/3/8 elementos; Progress0/1/2/5 filas completas; cuatro temas, texto largo y320px. [QA](../qa/implementations/composition-slots.v0.1.1.figma.review.md). No revalida paleta histórica de Charts ni promueve automáticamente su base. |
| Button, Filter Chip, Badge | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | specs/components/{button.contract.v0.2.0,filter-chip.contract.v0.2.0,badge.contract.v0.1.0}.md: etiqueta, iconos únicos opcionales e intercambiables. TEXT/BOOLEAN/INSTANCE_SWAP cubren esas regiones; no hay lista de contenido variable. La palabra histórica «slots de icono» no acredita Slots nativos. |
| Icon Button | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | drafts/contracts/icon-button.contract.v0.1.0.md §3: un icono intercambiable y Dot opcional, no lista. |
| Dot, Avatar | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | specs/components/dot.contract.v0.1.0.md y drafts/contracts/avatar.contract.v0.1.0.md §3: valor/foto/iniciales o icono único y estado; sin región de hijos variables. |
| Radio Button, Checkbox | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | drafts/contracts/{radio-button,checkbox}.contract.v0.1.0.md §3: indicador y etiquetas izquierda/derecha fijas opcionales. Un grupo de controles sería otra composición, no Slot dentro del indicador. |
| Tooltip, Inline Notification | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | drafts/contracts/tooltip.contract.v0.1.0.md y specs/components/inline-notification.contract.v0.1.0.md §3: textos e iconos fijos; no se ha definido contenido enriquecido ni lista de acciones variable. |
| Input Field, Textarea, Search | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | specs/{input-field,textarea,search}.contract.v0.1.0.md §3: contenido textual, helper, prefijo/contador e iconos fijos. No convertir el control de texto en contenedor arbitrario. |
| File Upload | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | specs/file-upload.contract.v0.1.0.md §3: dropzone, textos, progreso y botón opcional. No existe lista de archivos construida en este componente que convertir. |
| Dropdown Item, Switch Tab Item, Tab, Breadcrumb item | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | Contratos de cada ítem y lectura Navigation/Breadcrumbs: unidades con etiqueta, estado y partes fijas; el Slot pertenece al grupo, no al ítem. Breadcrumb item solo recibe la corrección de ancho descrita en la enmienda. |
| Stepper Item / Connector | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | specs/stepper.contract.v0.1.0.md: unidad de etapa y conectores; la composición de etapas es ejemplo, no un anfitrión público definido. Evaluar Slot al crear ese anfitrión, no dentro de la etapa. |
| Metric Card | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | drafts/contracts/metric-card.contract.v0.1.0.md §3–4: tipos de una/dos métricas y campos editables concretos. No se ha definido una colección extensible de métricas ni contenido arbitrario. |
| Loader, Scrollbar, Linear Progress Bar | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | Contratos specs/{loader,scrollbar}.contract.v0.1.0.md y drafts/contracts/linear-progress-bar.contract.v0.1.0.md: fotogramas, thumb/pista y textos de progreso son anatomía controlada, no contenido insertable por consumidor. |
| Toggle | NOT_APPLICABLE al alcance actual | REVIEWED documentalmente | drafts/contracts/toggle.contract.v0.1.0.md §2/4: track, thumb y dos etiquetas opcionales. TEXT/BOOLEAN cubren el contenido; Mixed es otro valor visual del control, no una región extensible. No se modificó ni se revalidó su paleta en esta tarea. |
| Logos | NOT_APPLICABLE al artwork | OMITTED_BY_USER para remanente | Assets agnósticos copiados fielmente, no composición extensible. Se mantiene la excepción y omisión expresas del usuario. |
| Header / Actions | REQUIRED | IMPLEMENTED; QA Slots PASS | Slot518:124, propiedadActions#518:0, componente518:123;0/1/3/5/7acciones,agregar/borrar/reordenar yshow/hide conservancontenido sin detach. [Contrato](../specs/header.contract.v0.1.0.md), [QA](../qa/implementations/header.v0.1.0.figma.review.md). |
| Modal | REQUIRED: Body, Side content, Actions | IMPLEMENTED; QA Slots PASS | Página565:122, Basic567:360,Media569:301,SideBySide569:327;25pruebas incluyen0/1/3/8contenidos,0/1/2/4acciones,retenciónSize/Scroll,reordenamiento y sustitución. [Contrato](../specs/modal.contract.v0.1.0.md), [QA](../qa/implementations/modal.v0.1.0.figma.review.md). MediaTitle/Text eimagenúnicaNOT_APPLICABLEaSlot. |
| Sidebar | REQUIRED | IMPLEMENTED; QA acotado PASS | Cierre2026-10-05 superior: cinco Slots nativos y16checks de composición/retención. [QA](../qa/implementations/sidebar.v0.1.0.slots.json). Sustituye UNRESOLVED histórico. |
| Empty states | REQUIRED | IMPLEMENTED; QA acotado PASS | Cierre2026-10-05 superior: dos propiedades/ocho Slots;64operaciones y16transiciones. [QA](../qa/implementations/empty-states.v0.1.0.figma.review.md). Sustituye UNRESOLVED histórico. |

El QA de Select0.1.0 permanece histórico. [COMPOSITION-SLOTS-001](../specs/composition-slots.amendment.v0.1.0.md) acredita Select, Switch Tab y Breadcrumbs; [COMPOSITION-SLOTS-002](../specs/composition-slots.amendment.v0.1.1.md) acredita Steps, Pagination y leyendas Charts. Header, Table, Modal, Sidebar y Empty states tienen sus propios cierres posteriores. Las revisiones NOT_APPLICABLE se apoyan en anatomía contractual, no simulan una auditoría Figma global. No quedan composiciones REQUIRED sin implementar dentro de esta cola registrada. No se publica biblioteca. [Lista operativa vigente](../specs/MIGRATION-TRACEABILITY-STATUS.md). Conciliación documental2026-10-05: no nueva implementación ni repetición del QA de Slots.

## Chat Toolbar y dependencias · 2026-10-08

REQUIRED e IMPLEMENTED: Toolbar Header/Tools and actions/Indicators/Chats, Tool Item Extra actions, History Item Title/Actions. [Contrato](../specs/chat-toolbar.contract.v0.1.0.md), [QA](../qa/implementations/chat-toolbar.v0.1.0.slots.json). Sin máximo de negocio, edición0/1/3/5, reorder/replace, retención de variante; wrap en acciones y Header. Plan y logo no requieren Slots adicionales. No se abre revisión global.

## Fuentes · 2026-10-09

REQUIRED/IMPLEMENTED: Path#848:9, dos Slots848:19/848:33 en Default/Hover. Insertar/quitar/reordenar/sustituir0/1/2/4; StateSwap conserva overrides, texto largo a150px refluye. Vacío conserva16px; no política de negocio inferida. [Contrato](../specs/components/fuentes.contract.v0.1.0.md), [QA](../qa/implementations/fuentes.v0.1.0.review.md). Path Item NOT_APPLICABLE: segmento de anatomía fija con Label y separador opcional.
