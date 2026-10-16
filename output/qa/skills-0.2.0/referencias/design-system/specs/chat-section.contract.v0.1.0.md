---
contract_id: CHAT-SECTION-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
figma_page_name: Chat
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
decision: DEC-EXTERNAL-COMPONENTS-DELEGATION-001
slot_applicability: REQUIRED
---

# Chat Section · contrato de construcción

## 1. Purpose

Integrar el organismo sectionChat20355:74859 de Anticipa en AI Design System. Composición visual para bienvenida y conversación activa; no implementación de un servicio de IA.

## 2. Contract

CS01: página semántica Chat, set Chat Section con State=Standby/Active. CS02: reutilizar Conversation Message/Composer y personajes locales, sin cambiar sus principales. CS03: UI con roles semánticos canónicos y personajes con excepción fija autorizada. CS04: Slots reales para mensajes y sugerencias. CS05: contenido editable, auto layout, evidencia técnica, specs y grafo sincronizados. La fuente permanece intacta.

## 3. Anatomy

Standby: BENI de bienvenida, saludo, nombre del usuario, subtítulo, Composer sin disclaimer y Suggestions. Active: Messages, indicador textual de lectura y Composer con disclaimer. Ambos retienen las regiones de composición, ocultando las no pertinentes para preservar overrides al cambiar State. Auxiliar `.Chat / BENI Welcome` conserva la pose de bienvenida exacta, distinta del glifo pequeño de Conversation. Chat Suggestion reutiliza instancias BENI/NAVI y presenta una etiqueta.

## 4. Properties

Chat Section: State VARIANT; Greeting, User name, Subtitle y Status text TEXT; Show status BOOLEAN=true; Messages y Suggestions SLOT. Los textos del saludo se separan para que User name conserve color brand al editar. Composer expuesto como instancia anidada y editado mediante sus propiedades existentes. No propagar referencias del anfitrión a hijos internos de Slots. Chat Suggestion: State Default/Hover, Label TEXT, Character INSTANCE_SWAP con BENI/NAVI preferidos. No eje Selected, no lógica de filtro.

## 5. Variants

Dos variantes de Chat Section y dos de Chat Suggestion, más un auxiliar gráfico independiente. No variantes por cantidad de mensajes, agente, tema, ancho o estado del backend.

## 6. Sizes

Referencia782×775, ancho mínimo574 para esta composición desktop. Columna central max542, FILL dentro de padding lateral16; altura HUG, min775. Margen superior80 compuesto por48+32 semánticos; gap32. En Active, Messages conserva espacio residual de la muestra y crece con contenido. La altura775 no limita cantidad. BENI168.73999×163.73999 conserva geometría fuente. Sugerencias HUG con padding8 vertical/12 horizontal, gap8, radiofull; alto derivado36 con etiqueta14/20. No se inventa token de36 ni se escala un control ajeno.

## 7. States

Standby muestra bienvenida/sugerencias y oculta mensajes/status. Active hace lo inverso y activa disclaimer. Show status permite ocultar el indicador sin quitar mensajes. Default/Hover de sugerencias representa realce visual, no selección persistida; no estados nuevos de producto.

## 8. Behavior

No navegación ni envío automático al pulsar sugerencias. No se copia la animación fuente de113 variantes ni la secuencia del personaje: se conserva pose estática y texto completo editable «Leyendo la información...». La frase es demo de proceso, no prueba de ejecución. No se define cuándo termina, cómo responde el modelo ni recuperación de errores. Hover puede prototiparse entre las dos variantes locales sin destinos remotos.

## 9. Accessibility

Producto deberá definir foco, teclado, nombres y anuncios del progreso. Los personajes no sustituyen etiqueta de la sugerencia. Conservar y medir contraste por tema; documentar limitaciones con asterisco, sin recolorear para ocultarlas. No declarar conformidad WCAG ni funcionalidad web.

## 10. Design tokens

[Inventario base](../sources/inventories/tokens.inventory.json), SHA256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474. [Preflight derivado](../implementations/figma/chat-section.v0.1.0.preflight.json):30 roles/120 aliases cotejados, nombres/tipos/description/scopes/valores coincidentes. Ningún token nuevo.

|Uso|Rol canónico|
|---|---|
|Superficie Chat|color/background/default|
|Saludo / nombre / subtítulo / progreso|color/text/primary / brand / secondary / tertiary|
|Sugerencia Default / Hover|color/surface/brand / color/interactive/secondary/hover|
|Texto de sugerencia|color/text/brand|
|Título32/40 Bold|font/family/base, font/weight/bold, font/size/2xl, font/line-height/2xl|
|Subtítulo20/28 Regular|font/weight/regular, font/size/lg, font/line-height/lg|
|Sugerencia y progreso14/20|font/weight/regular, font/size/sm, font/line-height/sm|
|Tracking|font/letter-spacing/normal|
|Separación|spacing/none,sm,md,lg,2xl,4xl|
|Píldora / glifo16|radius/full / size/lg|

Personajes: [JSON canónico de identidad](../specs/tokens/ai-design-system.character-identity.v0.1.0.json) y [enmienda vigente](../specs/components/conversation.character-identity.amendment.v0.1.1.md). Binding directo a color/characters/beni/body, navi/body y shared/features, coleccióncharacter-identity, sin semánticos ni cambio por tema. Esta excepción no se extiende al nombre del usuario ni a sugerencias. Composer/Message consumen su propio contrato y tokens; no duplicar aquí sus valores.

## 11. Content rules

Textos de la fuente son demos editables. Greeting=Hola,; User name=Bruce Wayne; subtítulo original. Tres sugerencias iniciales, dos BENI y una NAVI; no límite de producto. No confundir placeholder con valor enviado.

## 12. Composition rules / Slots

P-SLOTS0.1.0 REQUIRED. Messages vertical, FILL/HUG, gap8, alineación inferior en la muestra; recibe instancias Message/Response o composición DS equivalente. Suggestions horizontal WRAP, FILL/HUG, gaps16, centrado; recibe instancias Chat Suggestion. Ambos existen en ambas variantes y conservan nombres/propiedades. min/maxChildren null; no límite de negocio conocido. Insertar, quitar, reordenar, sustituir en instancia sin detach. Contenido de Slot se edita directamente.

Messages demo:un Message; status va fuera del Slot y se controla por propiedad. Suggestions demo:tres. Vacío estructural permitido, sin mensaje vacío inventado. Contenido extenso crece en altura; el contenedor de pantalla decide scroll, no este organismo. Mantener el ancho mínimo documentado; no se promete breakpoint móvil. Respuestas reutilizadas mantienen sus Slots propios, sin reconstruirlos.

## 13. Responsive behavior

Columna centrada max542 y ancho de anfitrión574–1024 en QA, referencia782. Saludo WRAP, textos con altura automática; eliminar desbordamiento790px fuente. No breakpoint ni layout móvil definidos. Sugerencias pueden envolver en nuevas filas; Chat Section crece con contenido, no lo recorta.

## 14. Edge cases

QA: Slots0/1/3/5 hijos, sustituir y reordenar, conservar overrides Standby↔Active, texto largo, variante Hover, ancho574/1024. Los números de QA no son capacidades máximas. Probar cuatro temas, personaje fijo, semánticos cambiantes y controles reutilizados intactos.

## 15. Forbidden combinations

No primitivas directas para UI ni variables remotas; no text token en shape; no brand aplicado a BENI/NAVI. No Selected en sugerencias ni estados ficticios por fotograma. No aplanar/detach para simular Slots; no modificar maestros Conversation. No copiar nombres/colores de la fuente como si fueran canónicos.

## 16. Design ↔ Code mapping

Figma solamente. Slots representan contenido configurable; no implican React, ARIA ni backend implementados. MD gobierna reglas, JSON referenciado gobierna datos. Grafo derivado registra vínculos, no modifica autoridad.

## 17. Acceptance criteria

AC01 dos variantes principales y dos sugerencias, auxiliar identificado; AC02 instancias locales reutilizadas sin cambios a maestros; AC03 cada paint visible propio con rol/scope correcto o excepción de identidad, cinco bindings tipográficos; AC04 JSON/modos/aliases coinciden; AC05 Slot real y operaciones de instancia0/1/más que demo, cambio de variante preservado; AC06 geometría y textos sin recortes en muestra/anchos documentados; AC07 fuente/contrato/IDs/QA/specs/grafo trazables. PASS técnico no equivale a auditoría humana ni publicación remota.

## 18. Examples

Muestra compacta de dos instancias Standby y Active; principales fuera de ella. Muestra de sugerencias en Default/Hover. Los datos no ejecutan acciones reales ni describen al usuario.

## 19. Source of truth

[Evidencia fuente](../drafts/contracts/chat-section.source.component-contract.md), snapshots allí enlazados, [Conversation vigente](../specs/conversation.contract.v0.1.0.md), enmienda de personajes y [delegación externa](../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md). Esta incorporación corresponde exclusivamente al nodo compartido, no a todo Anticipa.

## 20. Change management

Promoción a specs tras QA documental/técnico PASS. Cambios posteriores directamente en specs con versión y evidencia. Auditoría humana PENDING por excepciones, no aprobación repetida. Actualizar grafo según P05§8, sin publicar biblioteca ni crear frontend.

## 21. Deviations and readiness

Homologaciones delegadas anunciadas antes de construir: nombre de usuario brand en lugar del azul fijo de BENI; tipografía32/40,20/28,14/20 y trackingnormal; Composer/Message DS existentes; sugerencias de acción en vez de filtro Selected; geometría desktop fluida en altura y limitada en ancho; texto de lectura/pose estáticos. Fuente PARTIAL por aliases/animación histórica no resueltos; esas dependencias no se importan ni sostienen el binding destino. Nuevos assets se limitan a la pose BENI específica y sugerencia no cubierta por Filter Chip. Preparación y QA documental PASS; construcción y QA técnico completados según el cierre inferior.

## 22. Cierre técnico · 2026-10-08

[Estado e IDs](../implementations/figma/chat-section.v0.1.0.state.json), [QA](../qa/implementations/chat-section.v0.1.0.review.md). Página783:6; Chat Section784:98, Standby783:24/Active783:116; Chat Suggestion784:96, Default783:14/Hover783:21; auxiliar783:9; revisión784:99. La integración no modifica los principales de Conversation ni la fuente. No se crearon variables; dos estilos de texto nuevos y Body reutilizado.

QA técnico PASS acotado al contrato visual:62 pinturas visibles y13 textos visibles sin errores de bindings/scope;39 definiciones/156 aliases y tres identidades coincidentes. Seis Count Small ocultos conservan la excepción tipográfica de Dot/Conversation, sin certificar su uso visible. [Verificación](../qa/implementations/chat-section.v0.1.0.tokens-verification.json).

Slots probados desde instancia:0/1/3/5, reordenar/sustituir, overrides conservados entre variantes. Readback después de render con5 hijos/texto largo:Suggestions480px y anfitrión1093.74px; Messages652px y anfitrión930px; sin desbordes. Un Slot vacío puede conservar espacio residual (88/497px); vacío estructural no implica colapso ni estado vacío de producto. Se corrigió HUG vertical de Suggestions/Greeting line antes de la captura final. Pruebas temporales propias retiradas; muestra y maestros preservados.

Contraste*: sugerencias Default en Servicios3.046:1; Hover Contable3.567, Administrativo3.476, Servicios2.451, Personas4.223:1. Son limitaciones para texto14px conservadas por instrucción del usuario, no WCAG PASS. Nombre de usuario32px en Servicios3.236:1 se registra separado del texto pequeño. Demás limitaciones de controles reutilizados siguen su contrato.

Contrato promovido a specs con estado DELEGATED_FOR_BUILD, user_audit PENDING por excepciones. Publicación remota de estos cambios no realizada. Grafo sincronizado al cierre conforme a [P05](../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md), verificable desde el [handoff](../registry/SESSION-HANDOFF-2026-10-08-CHAT.md); su condición CURRENT requiere outputs y hashes concordantes, no se deduce del texto.
