# Auditoría por excepciones · migración de la Librería anterior

## Chat · observaciones de layout2026-10-09

[Detalle y alcance](components/chat.layout.amendment.v0.1.1.md): mínimos358 en muestras frente a574 en principales; description de set aún542 pese a maxWidth816; scroll VERTICAL de Messages con clipsContent=false no probado en Present; Toolbar Expanded FIXED sin scroll en listas. No se cambia Figma ni se asume una solución. Son observaciones concretas de la revisión pedida, no nuevas familias o tareas especulativas. [QA acotado](../qa/implementations/chat-layout.v0.1.1.review.md); aprobación humana PENDING.

## Characters · alcance artístico2026-10-08

[QA](../qa/implementations/characters.v0.1.0.review.md): rasgos/BENI5.381:1, rasgos/NAVI2.028:1*, sombra/cuerpo NAVI1.278:1*. Identidad conservada; no controles/texto ni certificación de accesibilidad. Auditoría perceptual PENDING; estructura de13 reacciones PASS. Sin decisión bloqueante. Reduced motion/backend fuera del alcance, no tareas nuevas.

## Chat Section · ampliación externa · 2026-10-08

*Contraste de sugerencias: Default Servicios3.046:1; Hover Contable3.567/Administrativo3.476/Servicios2.451/Personas4.223:1, texto14px. Se conserva paleta y se marca para revisión interna conforme a la decisión existente, sin recolorear ni detener la integración. [Mediciones](../qa/implementations/chat-section.v0.1.0.tokens-verification.json), [contrato](chat-section.contract.v0.1.0.md). Seis Count Small ocultos heredan excepción de Conversation; no activarlos para información esencial. No hay nueva decisión bloqueante ni solicitud de aprobación por componente. Comportamiento de backend/animación está fuera del alcance de esta entrega visual.

## Conversation · corrección de identidad · 2026-10-08

Resuelta por decisión explícita: BENI/NAVI ya no se homologan a brand/on-brand, conservan colores originales con tokens directos fijos. [Enmienda](components/conversation.character-identity.amendment.v0.1.1.md), [QA](../qa/implementations/conversation.characters.v0.1.1.review.md). Sustituye esa diferencia del cierre inferior. Rasgos de NAVI mantienen contraste original bajo*, sin recolorear identidad. No nueva tarea global ni pendiente de autorización.

## Incorporación externa · Conversation · 2026-10-08

Construcción cerrada técnicamente bajo delegación externa, no requiere aprobación por cada pieza. [Contrato y diferencias](conversation.contract.v0.1.0.md) preservan siluetas, pero homologan agentes a brand/on-brand y badges a neutrales, controles/medidas a DS. Para revisión interna quedan limitaciones ya heredadas: texto Servicios3.236:1*, bordes/divisor1.233–1.706:1* y Count Small4px oculto de Icon Button (no usado por Conversation). No se recolorea ni crean tokens para ocultarlas. [QA y mediciones](../qa/implementations/conversation.v0.1.0.review.md). Backend, envío, copia real y animación están fuera del contrato visual, no son tareas nuevas abiertas.

## Logos · decisión acotada pendiente · 2026-10-06

El [paso3](../qa/implementations/logos.refinement.v0.1.1.review.md) revalidó seis sets/72 variantes/2967 nodos. Arte y dependencias conservados, Personas exacto. Persisten57 diferencias geométricas de hasta0.00030517578125px; las pruebas seguras en clones no resolvieron la igualdad y los principales quedaron intactos. Única propuesta pendiente: aceptar esos deltas específicos sin tolerancia general, redibujo ni escalado. No se declara VALIDATED_WITH_EXCEPTIONS hasta aceptación explícita. Los doce assets siguen omitidos; las exportaciones nuevas observadas en fuente no son tarea de migración añadida.

## Radio Buttons / Checkboxes · cierre técnico · 2026-10-06

[Cotejo restante cerrado](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md), sin aprobación individual adicional requerida. Se conservan para revisión interna las diferencias ya delegadas: etiquetas18→20px de interlineado, halo interior#F8FAFC→blanco y anatomía normalizada (Radio con discos18/8; Checkbox sin grupos/helper singular). Los contornos2.56:1* siguen originales. Ocho iconos Checkbox recuperaron su posición vertical fuente; esa discrepancia técnica queda resuelta, no como pendiente del equipo. No se añaden tareas ni se afirma identidad píxel por píxel.

## Actualización cromática de seis familias · 2026-10-05

Las revisiones pendientes de Buttons, Icon Buttons, Breadcrumbs, Metric Cards, Charts y Linear Progress Bars están cerradas técnicamente; no requieren otra aprobación individual. [QA y mediciones](../qa/implementations/six-families.color.v0.1.0.review.md). Se restauraron colores de origen, conservando limitaciones* para revisión interna: Servicios, Primary Press, bordes suaves, Gauge y series claras. El swatch Charts#D9D9D9 se aproxima con neutral/300#E2E8F0 mediante rol semántico; no hay color primitivo nuevo. Los Slots siguen intactos y el80% continúa como demo. La auditoría humana sigue PENDING, sin recolorear para forzar contraste.

## Vigencia de pendientes · conciliación 2026-10-05

La [lista operativa](MIGRATION-TRACEABILITY-STATUS.md) separa refinamiento técnico, decisiones de equipo y cierres ya ejecutados. No añade asuntos a esta auditoría. La integración de cuatro logos locales en Header está cerrada por su [QA](../qa/implementations/header.v0.1.0.figma.review.md); la mención de integración pendiente en AUD-005 inferior es histórica y queda sustituida solo en ese alcance. El QA geométrico de los seis sets de Logos sigue parcial; los doce assets omitidos no son un bloqueo vigente. No hay nueva lectura Figma, aprobación humana ni cambio de paleta en esta conciliación.

## Cierre técnico · Chips · 2026-10-05

[Enmienda0.2.1](components/filter-chip.semantic.amendment.v0.2.1.md) y [QA](../qa/implementations/filter-chip.semantic.v0.2.1.figma.review.md): roles inversos corregidos sin cambiar apariencia. No requiere nueva decisión para construir. Auditoría humana del ajuste delegado PENDING.

*Limitación de la paleta original, conservada según DEC-MIGRATION-CONTRAST-LIMITATIONS-001:* Hover no seleccionado en Administrativo tiene texto4.442:1 e icono opcional2.790:1 contra su fondo sólido. Iconos ocultos por defecto; el criterio no textual depende de su uso significativo. [Mediciones de los cuatro modos](../qa/implementations/filter-chip.semantic.v0.2.1.contrast.json). Se añade evidencia al asunto existente de contraste, no una orden de recolorear ni una tarea de rediseño. Los colores y opacidades fuente permanecen iguales.

## Cierre técnico acotado · Buttons · 2026-10-05

Las nueve variables remotas/722referencias se sustituyeron por roles locales mediante [enmienda0.2.2](components/button.local-bindings.amendment.v0.2.2.md) y [QA PASS](../qa/implementations/button.local-bindings.v0.2.2.figma.review.md). Ningún cambio visual, nueva variable ni aprobación por variante requerida. AuditoríaPENDING del detalle delegado. Las menciones históricas inferiores a principales Buttons “sin modificar” describen las construcciones originales; ahora existe este ajuste separado y sus consumidores leídos no tienen regresiones. No cierra ni altera otras excepciones de contraste/tipografía/Logos.

## Empty states · 2026-10-05

[Contrato](empty-states.contract.v0.1.0.md) yQA técnico/visualPASS acotado, auditoríaPENDING por excepciones.

- *Servicios: texto blanco sobre marca ylinkmarca sobreblanco3.236:1; se conserva el color, revisión interna pendiente, no WCAGPASS. [Mediciones](../qa/implementations/empty-states.v0.1.0.themes.json).
- EMPTY-AUD-001: cinco colores decorativos sin RGB exacto usan primitivas existentes próximas mediante seisroles semánticos; [diferencias](../sources/figma-snapshots/empty-states.v0.1.0.color-approximation.json). No nuevas primitivas.
- EMPTY-AUD-002: Main Poppins18/Figtree14 se normaliza aManrope20/14; tracking normal. Medidas públicas conservadas; no identidadpixel-perfect. IlustracionesSVG editables conservan formas, no internals idénticos.
- EMPTY-AUD-003: Main necesita548px mínimo; callbacks/ARIA/teclado son decisiones de implementación deproducto, no una aprobación de componente bloqueante. Props de ilustración yvisibilidadInline específicas porpreset; accionescompartidas. Nuevos botones insertados desde otra biblioteca requieren revisar sus bindings; ocho defaults integrados sí están normalizados, mainsButtons sin modificar.

## Sidebar · 2026-10-05

[Contrato en specs](sidebar.contract.v0.1.0.md), QA visual/tokens/Slots PASS acotado. No requiere aprobación repetida por componente; auditoría humanaPENDING.
- *Contraste original: submenú activo2.451–4.223:1; hover horizontal con texto fuerte sobre fondo marca1.582–2.225:1; BETA inicio2.262/3.368:1 y extremo violeta final4.389:1; Servicios blanco/marca3.236:1 y marca/superficie3.046:1; divisor1.243–1.619:1. [Mediciones por modo](../qa/implementations/sidebar.v0.1.0.contrast.json). No se recoloreó para mejorar ratios.
- BETA se normaliza deInter aManrope10; no cambia el alto48 del control. Tooltip local y sus métricas reutilizados sin modificar el main.
- Slots editables y con retención: el cambio del contenedor no transforma automáticamente la presentación de elementos personalizados; configurarla al componer. Cantidad variable no equivale a espacio ilimitado en el baseline.
- Tres roles nuevos de fondo con aliases a primitivas existentes y scopes correctos; no RGB ni primitivas nuevas. Comportamiento de producto fuera de alcance. No bloqueaEmpty states.

## Modal · raíz · 2026-10-01

[Contrato](modal.contract.v0.1.0.md) en specs. QA visual/tokens/Slots PASS acotado; auditoría humanaPENDING.

- MODAL-AUD-001: escala tipográfica existente30→32/22→24 ytracking-0.1→0; alturasBasic/SideBySide+4px,Media+6px. No se afirma identidadpixel-perfect.
- MODAL-AUD-002: texto/botonesServicios3.236:1*,divisores1.233:1*,bordeCheckbox2.564:1*. Se mantienen por la decisión de conservar paleta; revisar internamente, sin recolorear automáticamente.
- MODAL-AUD-003: cierre,Escape,backdrop,foco y persistencia deacciones no definidos. No se transfirió navegación destino=null; “a link.” es demo sinURL. Bodyvacío no define un estado vacío deproducto.
- Sombras observadas y padding Footer20 permanecen literales documentados; no se añadió Foundation. Fuente normalizada PARTIAL. Las cinco referencias externas heredadas de Buttons se corrigieron en consumidores de Modal, sin alterar valores ni principales. No se afirma revisión global de Buttons.

## Table · Anticipa · 2026-10-01

[Contrato](table.contract.v0.1.0.md) en specs y componente548:895 construido; QA acotadoPASS, auditoría por excepcionesPENDING.

- **TABLE-AUD-001:** Hover fuente mide1288pxfrentea1280deDefault y desplaza columnas. Se preservó; revisar con equipo si se desea normalizar su geometría. No se afirma alineación estable.
- Negro puro no disponible: text/iconprimary→neutral900#0F172A; diferenciaRGB(15,23,42) documentada, sin nueva primitiva.
- *DivisorE2E8F0sobreblanco1.233:1 si fuese límite esencial. Icono marcaServiciossobreblanco3.236:1. Se conservan tokens/colores; no WCAGglobal.
- Cardinalidad0..n requierecoordinarcolumnas;320pxconlacomposicióncompleta no soportado. Sort/copy/selección/navegación deproducto no definidos. No se piden aprobaciones repetidas por celda.

## Header · revisión interna no bloqueante · 2026-10-01

[Contrato](header.contract.v0.1.0.md) y [QA](../qa/implementations/header.v0.1.0.figma.review.md) publicados documentalmente; no requieren aprobar cada propiedad.

- *Empresa en Servicios y blanco/AvatarServicios:3.236:1. Colores canónicos conservados, sin recolorear por contraste.
- *Etiqueta de versión: fuente#844AEC→#2868FD, destino semántico#A146FB→#3255F7 por primitivas más cercanas. Blanco frente al extremo violeta4.389:1 y frenteazul5.558:1; no declarar conformidad global del gradiente.
- *Versión conserva line-heightAUTO y empresa tracking0.1% literal; ancho natural de contenedorLogo difiere≈0.1013px sin modificar artwork. Revisar solo si el equipo requiere normalización posterior.
- *320px con todos los grupos no soportado; layoutDesktop y cardinalidad variable requieren espacio o menor composición. Navegación,menús y accesibilidad de producto siguen por definir.
- Integración de los cuatro logos de categoría verificada para Header; no cierra QA general de Logos ni reactiva los doce assets omitidos.

## Hallazgo documental · 2026-10-01 · DOC-SEARCH-001

**CLOSED · 2026-10-05, alcance documental.** [Search0.1.1](search.contract.v0.1.1.md) sustituye0.1.0, retira las cláusulas ajenas y pasa [QA de correspondencia](../qa/implementations/search.v0.1.1.figma.review.md) contra fuente/destino actuales. No cambios Figma ni nueva auditoría cromática global. La descripción siguiente conserva el hallazgo histórico, ya resuelto; no es un bloqueo vigente.

**Revisión documental requerida, sin nueva decisión de producto solicitada.** Durante la actualización del índice se comprobó que [Search 0.1.0](search.contract.v0.1.0.md), §§4, 7, 10, 11, 14–16, mezcla instrucciones de File Upload/Textarea con su anatomía y matriz propias. La matriz Search define únicamente Default/Selected/Focus/Disabled, mientras §7 menciona Success/Error; otras secciones mencionan formatos, progreso, Counter y Button ajenos a la anatomía declarada. Es una contradicción de alcance documental (`CONFLICT` acotado), no prueba de un fallo nuevo en Figma.

El [QA documental](../qa/contracts/search.v0.1.0.review.md) y el [QA de implementación](../qa/implementations/search.v0.1.0.figma.review.md) también contienen prosa cruzada. Su PASS histórico y los conteos observados se conservan como evidencia; no resuelven esta contradicción. Antes de reutilizar esas cláusulas para otra implementación, preparar una corrección versionada/enmienda en specs desde la fuente Search y su readback, y revalidar la documentación afectada. No sustituir requisitos por conjetura, no reconstruir Search ni bloquear Header por este hallazgo. Auditoría humana sigue PENDING; no se tocó Figma en esta revisión.

## Slots · ampliación 2026-09-30

[QA Slots0.1.1](../qa/implementations/composition-slots.v0.1.1.figma.review.md) cierra la capacidad de composición de Steps, Pagination y leyendas Charts. No requiere aprobación repetitiva por componente.

- *AUD-008 sigue vigente: Gallery On Primary conserva su composición legacy separada de On White. Cambiar de contexto muestra su propia lista; volver recupera la anterior. Una futura unificación de roles/contextos necesita decisión de equipo, no se aplicó silenciosamente.
- *Los Slots vacíos conservan placeholders del editor; las políticas de producto para listas vacías y sus límites no están definidas. No se añadió scroll ni algoritmo de selección/paginación.
- Pagination ya propaga Disabled a las celdas personalizadas que conservan sus tokens contextuales, sin perder cantidad/textos. Los nueve aliases añadidos no cambian colores; no queda un bloqueo por este punto.
- Charts conserva el 80% de demo y sus limitaciones cromáticas históricas; QA de Slots no certifica ni restaura esa paleta global.

Estas notas consolidan las excepciones existentes y capacidades comprobadas; no convierten la auditoría humana en APPROVED.

## Select · excepciones registradas 2026-09-29

- *Dos sombras literales del menú: valores fuente conservados porque no hay categoría/opacidades de sombra en JSON; no están tokenizadas. No se ha creado ningún color primitivo. Revisión futura de Foundations, sin usar focus/text como elevación.
- *El menú cubre el helper y conserva Eye como en el ejemplo original. No implica comportamiento de selección definido.
- *Diez etiquetas ocultas del Checkbox escalado, heredadas de Dropdown Item, conservan color/familia/peso vinculados pero métricas numéricas literales escaladas. No afecta al texto de las opciones visibles. No se modificaron principales.
- Borde neutral400/blanco2.564:1 y filas40px mantienen limitaciones contextuales; sin recolorear. No se requiere aprobación rutinaria de cada variante.

Detalle: [Select0.1.0](select.contract.v0.1.0.md), [QA](../qa/implementations/select.v0.1.0.figma.review.md). Estado técnico acotado PASS; auditoría humana PENDING.

**Estado:** abierto · **Actualizado:** 2026-09-24 · **Fuente:** Libreria v1.1.0 → AI Design System.

Este documento reúne solo decisiones materiales ambiguas o no resueltas y limitaciones aceptadas que el equipo debe revisar. No es una lista de aprobaciones por componente. Los contratos con QA documental y de implementación vigente pueden promoverse a `specs/` bajo `DELEGATED_FOR_BUILD`; esa ubicación no significa que el usuario haya aprobado cada requisito. La publicación de componentes en la biblioteca Figma es un paso distinto de la publicación documental. El marcador `*` significa **revisión interna pendiente**, no una modificación visual del componente ni un fallo que deba corregirse alterando el color.

## Decisiones que sí requieren criterio del usuario

| ID | Asunto | Evidencia y estado actual | Decisión pendiente |
|---|---|---|---|
| AUD-003 | Halo de foco de Toggle: fuente `#F8FAFC`, destino `#FFFFFF`. El valor fuente no tiene primitiva exacta en el JSON aprobado; cambiar el token de efecto compartido o crear una primitiva alteraría Foundations. [Readback](../qa/implementations/toggle.source-color.v0.1.5.figma.review.md). | Decidir con el equipo si se acepta la diferencia, se permite literal de efecto como excepción o se amplía expresamente la escala primitiva. Hasta entonces no declarar fidelidad cromática total de Toggle. |
| AUD-004 | Tooltip conserva los colores de origen, pero el contrato normalizó interlineado 22.4→24 px y tracking aproximado −0.28→−0.01 px en cuatro etiquetas. [Readback](../qa/implementations/tooltip.traceability.v0.1.0.review.md). | Decidir si esta normalización tipográfica tokenizada es aceptable o si se debe conservar el valor original mediante una extensión/literal justificado. No cambiarla por conjetura. |
| AUD-006 | [Avatar](../qa/implementations/avatar.source-color.v0.1.1.figma.review.md) conserva los colores originales, pero normalizó las iniciales Small/Medium de 6/9 px en fuente a 10/12 px en destino. | Decidir si la mejora de legibilidad es aceptable pese a la diferencia visual; mantenerla por ahora sin atribuirle aprobación de fidelidad tipográfica total. |
| AUD-007 · baja prioridad | [Scrollbar](../qa/implementations/scrollbar.v0.1.1.figma.review.md) conserva la variante llamada `75%`, pero el thumb fuente y destino mide 240/272 px ≈ 88.24% del recorrido interior. Los subcomponentes internos se normalizaron a 272 px para anidarlos sin rotación. | El usuario indicó que no es importante por ahora: no bloquea otras familias. Revisar con el equipo si `75%` es nombre histórico de muestra o si se corrige nombre/longitud en una versión futura; no atribuirle significado de datos mientras tanto. |
| AUD-008 · baja prioridad | [Steps](../qa/implementations/steps.v0.1.1.figma.review.md) presenta tres paletas para `On Primary`: el Gallery público usa un `Combination` externo cromático/gris, Gallery only usa los dots On White y el `.Dot` interno define blanco/tono claro. El destino conserva esas diferencias con roles semánticos y primitivas existentes aproximadas; los acentos ya siguen la familia de marca por tema según instrucción posterior. | Revisar con el equipo si en una versión futura las dos variantes públicas deben unificarse con la paleta contextual del subcomponente. No bloquear la migración actual ni tratar esa normalización como ya aprobada. |
| AUD-009 · baja prioridad | [Stepper](../qa/implementations/stepper.v0.1.1.figma.review.md) conserva tracking fuente −2 % como literal en 54 textos: el token local `tight` da −0.01 px y hacía que el título se partiera. Los interlineados se vincularon a 16/20 px frente a 15/21 px fuente. | Revisar con el equipo si la próxima escala tipográfica incorpora un valor semántico equivalente o si se acepta esta excepción literal acotada. Los acentos ahora siguen la marca por decisión resuelta, no se recolorean por contraste. |

**AUD-INPUT-FIELD-001 · revisión no bloqueante:** [Input Field](../qa/implementations/input-field.v0.1.0.figma.review.md) normaliza tracking fuente 0.1% a 0 e interlineado AUTO≈19 a 20; el prefijo Small usa 16 en lugar de 12 para evitar recorte. Halo interior #F8FAFC aproximado a blanco mediante rol existente. Se conserva geometría pública y paleta restante. Revisar estas diferencias junto a las excepciones tipográficas ya abiertas, sin pedir aprobación por variante ni atribuir acciones web a los iconos.

## Decisiones resueltas

**Logos restantes omitidos · 2026-09-28:** el usuario pidió saltar los doce assets sueltos. DEC-LOGOS-REMAINDER-OMITTED-001 sustituye su copia como pendiente activo; no solicitar acceso al editor por ellos. Los seis sets existentes y su QA parcial se conservan. Esto no aprueba el QA geométrico restante ni marca toda la familia completa.

**AUD-005 · Logos agnósticos · 2026-09-28:** [DEC-LOGOS-AGNOSTIC-ASSETS-001](../registry/decisions.md) resuelve la política cromática: conservar artwork original sin variables ni tokens. No volver a solicitar autorización para usar literales dentro de estos assets. Los seis sets ya tienen copia local y dependencias de categoría, con [QA parcial](../qa/implementations/logos.v0.1.0.figma.review.md). Esto no cierra Header ni afirma equivalencia entre su nodo histórico 8321:504 y el set de la página Logos 8305:227; esa integración sigue pendiente. El cierre geométrico sigue pendiente técnico; los doce frames quedaron omitidos por la decisión posterior, no son aprobaciones por componente pendientes.

**Input Field Disabled · 2026-09-28:** el usuario aprobó que placeholder y valor precargado usen el mismo texto atenuado. [Enmienda 0.1.1](input-field.disabled-text.amendment.v0.1.1.md) aplicada a los tres Filled/Disabled con QA PASS. Value sigue distinguiendo contenido; no crea un estado editable ni una nueva variable. El contraste 2.34:1 ya registrado incluye ahora también el valor precargado.

| ID | Decisión | Efecto |
|---|---|---|
| AUD-001 · 2026-09-24 | El usuario confirmó que `80%` en Charts es solo contenido de demostración. | Conservarlo como muestra estática, sin atribuirle cálculo ni relación numérica con el ancho de las barras. No bloquea el contrato ni la construcción Figma. Un producto con datos reales necesitará una regla independiente; no se infiere aquí. |
| AUD-002 · 2026-09-24 | El usuario pidió mantener por ahora los colores originales y las limitaciones de contraste, con un asterisco para revisión interna del equipo. | Restaurar cualquier ajuste cromático hecho solo para superar contraste. Conservar roles semánticos del scope correcto y aliases a las primitivas existentes. Identificar con `*` los pares medidos que merecen revisión de legibilidad o de aplicabilidad del criterio; documentar valores y evidencia sin insertar el asterisco en los componentes. No afirmar conformidad de accesibilidad donde no se haya demostrado. |
| Stepper marca · 2026-09-24 | El usuario pidió que los acentos de Stepper sean de marca y cambien con el tema. | [Enmienda 0.1.1](stepper.brand-theme.amendment.v0.1.1.md): Checked = marca fuerte, Default = marca base en cuatro modos; Inactive permanece neutro. La diferencia frente al verde/azul fijo de origen es intencional y pasó [QA técnico](../qa/implementations/stepper.v0.1.1.figma.review.md). |
| Steps marca · 2026-09-24 | El usuario pidió el mismo comportamiento de marca por tema para Steps. | [Enmienda 0.1.1](steps.brand-theme.amendment.v0.1.1.md): seleccionado `On White` = marca base y dos acentos `On Primary` = tono 300 en cuatro modos; blancos y neutros permanecen. Pasó [QA técnico](../qa/implementations/steps.v0.1.1.figma.review.md); la anomalía AUD-008 no se unifica. |

## Limitaciones para revisión interna `*`

**Método:** contraste de luminancia WCAG calculado a dos decimales desde el [JSON de primitivas](../sources/inventories/tokens.inventory.json) y los pares observados en contratos de fuente o QA. Algunas filas ya enlazan un readback nuevo de Figma destino (Badge, Checkbox/Radio Button, Dot, Inline Notifications y Toggle); las demás representan la **paleta original propuesta para restauración**, no una validación actual del destino. Para texto normal, la referencia es [4.5:1](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); para la información visual indispensable de controles o gráficos, [3:1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Un ratio bajo en un gráfico con información textual redundante, o en un control inactivo, no prueba por sí solo incumplimiento WCAG; `*` pide revisar el contexto con el equipo.

| Familia / par original | Ratio | Motivo de revisión interna |
|---|---:|---|
| [Avatar](../qa/implementations/avatar.source-color.v0.1.1.figma.review.md) · iniciales blancas sobre orange/500, Servicios `*` | 3.24:1 | Readback actual confirmó alias y ocho fondos restaurados. Texto pequeño, referencia 4.5:1. Los otros tres modos resuelven 5.56–6.32:1. |
| [Badge](../qa/implementations/badge.source-color.v0.1.2.figma.review.md) · texto Informational / cyan/100 `*`; texto e icono Warning / amber/100 `*` | 3.61:1; 2.96:1 | Readback posterior confirmó los colores originales y bindings semánticos; ambos textos están por debajo de 4.5:1, y el icono Warning de 3:1 si comunica estado indispensable. |
| [Breadcrumbs](../drafts/contracts/breadcrumb-item.source.component-contract.md) · Current orange/500 sobre blanco, Servicios `*` | 3.24:1 | Texto, referencia 4.5:1. |
| [Charts](../drafts/contracts/chart-donut.source.component-contract.md) · avance del Gauge frente a pista `*`; [segunda serie de Header](../drafts/contracts/chart-header.source.component-contract.md) frente a blanco `*` | Gauge: 1.65 / 2.27 / 1.94 / 2.80:1; serie 2: 1.56 / 1.71 / 1.32 / 1.50:1 | Orden de modos: Contable / Administrativo / Servicios / Personas. Revisar si las formas son información indispensable o redundante con porcentaje y etiquetas. |
| [Checkbox](../drafts/contracts/checkbox.source.component-contract.md) y [Radio Button](../drafts/contracts/radio-button.source.component-contract.md) · contorno Off/Unselected neutral/400 sobre blanco `*` | 2.56:1 en cuatro modos | [Readback del destino](../qa/implementations/selection-control-source-color.v0.1.1.figma.review.md) confirmó los tres contornos; por debajo de la referencia de 3:1 si identifican controles operables. |
| [Dot](../qa/implementations/dot.source-color.v0.1.2.figma.review.md) · contorno Inactive blanco sobre blanco `*` | 1.00:1 en cuatro modos; relleno 1.23:1 | Readback actual confirma fidelidad a la fuente en 36 paints. Límite de visibilidad; el estado inactivo puede estar exento del criterio WCAG. |
| [Inline Notifications](../qa/implementations/inline-notification.warning-source-color.v0.1.1.figma.review.md) · icono Warning amber/600 sobre amber/100 `*` | 2.96:1 en cuatro modos | Readback completo de cinco variantes confirmó el rol compartido y color fuente; por debajo de 3:1 si el icono comunica estado indispensable. El pseudoenlace fuente sin URL se omite según contrato. |
| [Linear Progress Bars](../drafts/contracts/linear-progress-bar.source.component-contract.md) · segmento Primary orange/500 sobre pista fuente `#F1F5F9`, Servicios `*` | 2.95:1 | Por debajo de 3:1 si el segmento aporta información no reemplazada por el porcentaje visible. |
| [Metric Cards](../drafts/contracts/metric-card.source.component-contract.md) · tendencia orange/500 sobre fondo sutil, Servicios `*` | 2.95:1 | Texto, referencia 4.5:1. |
| [Toggle](../qa/implementations/toggle.source-color.v0.1.5.figma.review.md) · track y borde Off Default/Focus neutral/300 sobre blanco `*` | 1.23:1 en cuatro modos | Readback posterior confirma el mismo gris para fill y stroke, como la fuente. Revisar la visibilidad del control operable; no se recolorea solo por contraste. |
| [Scrollbar](../qa/implementations/scrollbar.v0.1.1.figma.review.md) · thumb destino neutral/300 `#E2E8F0` sobre blanco `*` | 1.23:1 en cuatro modos; fuente `#C3C6D4` 1.70:1 | Readback confirma la aproximación con primitiva existente y binding semántico autorizados después. Revisar si el thumb es información indispensable del control bajo la referencia de 3:1; no declarar fidelidad cromática exacta ni accesibilidad. |
| [Stepper](../qa/implementations/stepper.v0.1.1.figma.review.md) · Caption neutral/400 `#94A3B8` sobre blanco `*` | 2.56:1 en cuatro modos | Texto de 10 px; por debajo de la referencia de 4.5:1. Se conserva el color fuente exacto, tokenizado con rol de texto específico; requiere revisión interna, no recoloración automática. |

**Input Field `*`:** [readback vigente](../qa/implementations/input-field.v0.1.0.figma.review.md) confirma borde neutral/400 sobre blanco **2.56:1**, y contenido Disabled neutral/400 sobre fondo sutil **2.34:1**, en cuatro modos. Conservar colores; revisar visibilidad del contorno operable y contexto del contenido inactivo. No equivale a afirmar incumplimiento automático del estado Disabled.

**Pendiente técnico:** restaurar los colores fuente donde el destino los oscureció solo por contraste, mantener bindings del scope semántico correcto, comprobar paridad JSON/Figma y repetir medición sobre el readback real. El swatch gris literal `#D9D9D9` de [Chart Legend Label](../drafts/contracts/chart-label-cell.source.component-contract.md) no tiene correspondencia exacta demostrada con una primitiva del JSON; su tokenización fiel sigue en análisis y no se presenta aquí como ya resuelta.

**Toggle Mixed/Disabled `*`:** la [medición actual en Figma](../qa/implementations/toggle.mixed.v0.1.4.figma.review.md) del guion neutral/400 sobre la pista neutral/200 es 2.34:1 en los cuatro modos. Se conserva la semántica Disabled y el color de los tokens existentes; el equipo revisará si este indicador inactivo necesita un ajuste, sin tratar el asterisco como una modificación del componente.

**Search / Textarea / File Upload \***: el [readback de las 22 variantes](../qa/implementations/input-fields.followups.v0.1.0.audit.json) confirma contorno neutral/400 sobre blanco 2.56:1 y contenido Disabled sobre sutil 2.34:1. File Upload conserva Helper neutral/400 2.56:1; la acción de Servicios orange/500 tiene 3.24:1 sobre blanco y 2.90:1 en Hover sobre background/brand. No recolorear automáticamente. Los estados inactivos se evalúan en contexto; el enlace operable de Servicios requiere revisión interna. Se conservan formatos Success de10px; normalizaciones tipográficas y omisión de Tooltip oculto no expuesto constan en su contrato. Ninguno de estos puntos bloquea la entrega visual delegada ni exige aprobación individual ahora.

## Correcciones delegadas, sin decisión individual solicitada

**Dropdown Item / Select \* · 2026-09-28:** [readback y QA actuales](../qa/implementations/dropdown-item.v0.1.0.figma.review.md) confirman texto Selected de Servicios sobre surface/brand **3.05:1** y texto Disabled sobre blanco **2.56:1**. Conservar colores; evaluar Disabled como estado inactivo, no incumplimiento automático. Alturas Medium40 y Small32 requieren revisar contexto táctil. Normalización tipográfica AUTO22/19→24/20 y checkbox seleccionado/deshabilitado coherente documentadas bajo delegación; revisar junto con las excepciones existentes, sin pedir aprobación por variante. El componente no define lógica de teclado ni apertura/cierre.

1. Revisar las diferencias cromáticas ya documentadas en [estados de implementación](../registry/implementations.md). Donde la primitiva del color fuente exista, usar un rol semántico del scope correcto aliasado a esa primitiva; sincronizar JSON, contrato y Figma y repetir QA. Si no existe RGB primitivo exacto, la instrucción vigente [DEC-MIGRATION-NEAREST-PRIMITIVE-001](../registry/decisions.md) exige una primitiva existente semejante, tokenizada mediante rol semántico y diferencia visual documentada; no modificar tokens compartidos silenciosamente. Actualizar cada `*` con el par real leído de Figma y aclarar si el criterio de contraste aplica o si es solo una limitación visual contextual.
2. Conservar la estructura y el estilo de origen al mejorar nombres, editabilidad y bindings. Si una corrección de buenas prácticas alteró un rasgo visual sin necesidad demostrada, documentar y corregir antes de promover el contrato afectado.
3. Mantener fuera de la auditoría de Figma las reglas no definidas de frontend —teclado, datos vivos, responsive, navegación—. Requerirán contratos o decisiones de producto cuando empiece esa fase, no ahora.

## Criterio de cierre de esta lista

Solo se agregan nuevos renglones cuando una inspección profunda encuentre un conflicto que no pueda resolverse con el contrato, el JSON y las decisiones ya registradas. Cada renglón debe enlazar evidencia y explicar qué decisión cambia el resultado. Las decisiones resueltas se conservan con fecha y efecto; no desaparecen del historial.

## Excepciones Chat Toolbar · 2026-10-08

[Contrato](./chat-toolbar.contract.v0.1.0.md), [mediciones](../qa/implementations/chat-toolbar.v0.1.0.contrast.json). *Servicios: Pro Plan16px Bold3.236:1; barra/pista2.954:1. Disabled2.564:1 es control no operable, sin afirmar conformidad general. Se conservan colores DS; no cambio de paleta por contraste. Uso demo42/150=28% corrige dibujo fuente47%, sin cálculo automático. No nueva decisión bloqueante ni backend en alcance; auditoría por excepciones PENDING.

## Fuentes · excepción visual 2026-10-09*

[Contrato](components/fuentes.contract.v0.1.0.md), [QA y mediciones](../qa/implementations/fuentes.v0.1.0.review.md). Se conservan ruta/contador8px; brandServicios3.24/3.05:1 Default/Hover y tertiaryHoverContable4.29,Servicios4.48,Personas4.26:1. Bordesaccent1.24–1.71:1. No se cambian colores por contraste. Auditoría de legibilidad/accesibilidad en producto, no bloqueo de integración visual ni solicitud de aprobación de toda la familia. Navegación/URL/teclado sin definición fuente: fuera de alcance, no tareas nuevas de migración.
