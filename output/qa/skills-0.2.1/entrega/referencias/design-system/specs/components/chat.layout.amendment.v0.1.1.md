---
contract_id: CHAT-LAYOUT-001
version: 0.1.1
status: DELEGATED_FOR_BUILD
user_audit: PENDING
change_origin: USER_EDITED_FIGMA
implementation_review: PARTIAL
figma_page_name: Chat
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
slot_applicability: REQUIRED
---

# Chat · límites de ancho, altura y scrolling

## 1. Autoridad y alcance

El 2026-10-09 el usuario indicó que ajustó límites de width, scrolling y otros atributos de Chat y pidió revisarlos y documentarlos. Esta enmienda registra esos ajustes observados en los principales de AI Design System. No declara aprobación humana de todos los valores ni autoriza reparaciones automáticas. Se mantiene la [delegación externa](../../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md).

Complementa [Chat Section0.1.0](../chat-section.contract.v0.1.0.md) y [Chat Toolbar0.1.0](../chat-toolbar.contract.v0.1.0.md). Sustituye únicamente sus reglas de dimensiones, sizing y propietario del scroll señaladas abajo (§6, §12–14 y alcance del QA de §17/22). Los demás requisitos, tokens, propiedades, dependencias, identidad de personajes y Slots siguen vigentes. No modifica Conversation Composer, Message, Tool Item ni History Item como componentes principales.

Los números de referencia no son breakpoints ni tamaños obligatorios para todas las pantallas. Las discrepancias de instancia no se promueven a reglas del componente. Evidencia `OBSERVED` = lectura Plugin API; fórmulas `DERIVED` = cálculo sobre esa lectura; autoría individual de cada propiedad no está expuesta por Figma.

## 2. Chat Section: ancho

|Elemento|Regla anterior|Principal observado vigente|Evidencia|
|---|---|---|---|
|Chat content, ambas variantes|maxWidth542|maxWidth816; horizontal FILL; columna centrada|783:25,783:117|
|Standby y Active|minWidth574|minWidth574, maxWidth=null; ancho de referencia782|783:24,783:116|
|Instancias de muestra|No regla independiente documentada|minWidth358 **solo override de instancia**|784:103,784:163|
|Padding lateral|16|16, ligado a spacing/lg|Ambos principales|

En los principales, la anchura de contenido se deriva como `min(ancho anfitrión − 32, 816)` mientras se respete minWidth574. A782px el contenido mide750; alcanza el tope816 con un anfitrión de848px. Esto no declara soporte móvil358px: ese mínimo solo se observó en las dos muestras y no se ensayó allí contenido estrecho/largo. No cambiar los principales a358 sin una decisión explícita de alcance.

Composer, subtítulo, región de conversación y Slots visibles llenan la columna; Suggestions conserva WRAP/FILL/HUG. Las dimensiones542 de regiones ocultas son geometría residual, no el máximo de la columna visible. Los límites internos de los hijos mantienen sus contratos propios.

## 3. Chat Section: altura y propietario del scroll

|Elemento|Configuración leída|
|---|---|
|Standby783:24|782×775 de referencia; vertical HUG; minHeight775; sin maxHeight; overflow NONE|
|Standby content783:25|750×573.74; vertical HUG; paddingTop32|
|Active783:116|782×733 de referencia; vertical FIXED; minHeight/maxHeight=null; overflow NONE|
|Active content783:117|750×683 de referencia; vertical FIXED; paddingTop32|
|Conversation region783:125|750×481; FILL horizontal y vertical; gap8|
|Messages783:126|750×453; FILL horizontal y vertical; minHeight=null; overflowDirection VERTICAL; clipsContent=false; alineación vertical MAX|
|Status783:128|750×20; fuera del Slot Messages|
|Composer783:129|750×138; FILL horizontal/HUG vertical; fuera del Slot Messages|

El scroll configurado ahora pertenece a **Messages de Active**, no al organismo completo. Status y Composer no son hijos del Slot desplazable; esa estructura no prueba posicionamiento sticky/fixed de navegador. No se infiere autoscroll al último mensaje, retención de posición, carga paginada ni comportamiento de teclado.

Se sustituye la regla anterior «todo contenido extenso crece en altura y la pantalla decide scroll» **solo para Active**. Standby conserva crecimiento HUG. Active y su columna tienen altura fija independiente: redimensionar solo la raíz no demuestra que la columna se adapte automáticamente.683/733 son medidas observadas, no una relación FILL vertical inventada.

**Límite de validación:** Messages tiene clipsContent=false, al igual que sus ancestros leídos. La configuración VERTICAL está confirmada; el desplazamiento efectivo, recorte y acceso a mensajes desbordados no se comprobaron en Present con contenido largo. No se declara PASS de scroll operativo ni se corrige clipping por iniciativa del agente.

## 4. Chat Toolbar: diferencia observada respecto de0.1.0

Expanded797:316 conserva ancho264, minWidth264/maxWidth310 y minHeight791, pero su altura es **FIXED**, no HUG. Content region797:381 conserva232×519 de referencia, ahora vertical FILL y minHeight=null en lugar de519. Header y Expanded plan permanecen fuera de esa región; el plan sigue en flujo normal, no absoluto. El plan de referencia comienza en y631 y mide144 de alto.

Collapsed797:458 mantiene79×791, minWidth79/maxWidth93, minHeight791, vertical HUG; su región central oculta conserva altura fija695. No se atribuye ese comportamiento histórico a este nuevo cambio.

No se observó overflow VERTICAL en Toolbar: todos sus contenedores leídos tienen overflowDirection NONE. Expanded content799:461 sigue HUG con clipsContent=true; eso no significa scroll. La regla anterior que garantizaba crecimiento del Toolbar ante listas largas ya no queda demostrada con la raíz FIXED. Listas mayores que el espacio disponible requieren validación; no se inventa una política nueva ni se toca Figma.

El ancho264–310, el colapsado79–93, padding16/gap32 y la reacción ON_CLICK/CHANGE_TO local entre variantes (Smart Animate, EASE_OUT, ~300ms) siguen observados. No se deduce lógica de backend del prototipo.

## 5. Tokens, identidad y Slots

La geometría de composición816/574/358/733/683 no crea tokens nuevos ni altera el [JSON canónico](../../sources/inventories/tokens.inventory.json). Los bindings de layout relevantes continúan en spacing/none,sm,lg,2xl,4xl; sus cinco definiciones y veinte aliases se cotejan en el [QA](../../qa/implementations/chat-layout.v0.1.1.review.md). No se cambiaron colores, tipografías, variables ni descripciones canónicas durante esta revisión. No se afirma una revalidación cromática completa a partir de estos chequeos.

P-SLOTS sigue REQUIRED: Messages/Suggestions (dos variantes) y Header/Tools and actions/Indicators/Chats (dos variantes) son Slots reales. Propiedades del set conservan minChildren/maxChildren=null; no se añaden límites de cantidad. El censo incluye Slots anidados de dependencias: limitViolations vacío en los40 observados. La lectura actual no vuelve a ejecutar inserción, reorder, sustitución ni overrides entre variantes.

La [identidad BENI/NAVI](./conversation.character-identity.amendment.v0.1.1.md) y el logo agnóstico no cambian. Tampoco se incorporan nuevos estados o familias.

## 6. Evidencia, QA y continuidad

- [Lectura layout por nodo](../../qa/implementations/chat-layout.v0.1.1.observed.json):84 registros de layout propios/instancias directas, sin vectores ni textos.
- [Censo estructural y propiedades](../../qa/implementations/chat-layout.v0.1.1.structure.json):478 nodos recorridos, incluidos ocultos; cobertura de recorrido completa para cuatro principales, no inspección exhaustiva de todos sus atributos.
- [Muestras y spacing](../../qa/implementations/chat-layout.v0.1.1.instances-and-spacing.json): diferencia358/574, herencia del máximo816, scroll y referencias de primitivas.
- [QA de esta revisión](../../qa/implementations/chat-layout.v0.1.1.review.md) y [estado vigente por alcance](../../implementations/figma/chat-layout.v0.1.1.state.json).

El QA anterior permanece como evidencia histórica y no certifica los nuevos límites ni el scroll. La documentación del readback puede pasar QA sin que pase una prueba interactiva no ejecutada. No usar VALIDATED global para este cambio.

**Desfase documental en Figma:** la description del set784:98 todavía dice «Columna542» y «altura adaptable». No es la regla vigente de esta enmienda y no fue modificada, porque la solicitud actual es de revisión/documentación. Mínimo358 en muestras frente a574 en principales y scroll con clipsContent=false se conservan como observaciones concretas para el equipo; no se convierten en aprobaciones, correcciones automáticas ni una nueva lista genérica de pendientes.
