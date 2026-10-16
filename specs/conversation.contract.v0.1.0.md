---
contract_id: CONVERSATION-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
figma_page_name: Conversation
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
decision: DEC-EXTERNAL-COMPONENTS-DELEGATION-001
slot_applicability: REQUIRED
---

# Conversation · contrato de construcción

> Vigencia cromática de personajes: la [enmienda0.1.1](components/conversation.character-identity.amendment.v0.1.1.md), por decisión explícita del usuario, sustituye las referencias inferiores a personajes temáticos/brand. BENI y NAVI consumen tokens directos de identidad fija; el resto conserva semánticos. La enmienda y su JSON gobiernan esa excepción.

## 1. Purpose

Componer mensajes enviados, respuestas de agente y un área de redacción reutilizables. Fuente Anticipa20355:72763; integración expresamente delegada2026-10-08. Contrato visual Figma, no chat funcional.

## 2. Contract

REQ-CV-01: página única Conversation. REQ-CV-02: cuatro configuraciones públicas mediante Conversation Message (uno), Conversation Response (Agent=BENI/NAVI) y Conversation Composer (uno). No matriz especulativa de estados.
REQ-CV-03: controles locales Buttons/Badge/Icon Button; Phosphor para iconos y `.Table / Copy` local para copiar. REQ-CV-04: bindings semánticos locales, aliases canónicos y herencia de cuatro temas. REQ-CV-05: Slots nativos editables en instancia. REQ-CV-06: propiedades de texto/visibilidad conectadas, anatomía estable, reflow y captura sin recortes. REQ-CV-07: documentación, diferencias, IDs y QA persistentes.

## 3. Anatomy

Message: contenedor alineado a derecha, burbuja y texto editable. Response: iconografía del agente, columna con nombre/badge, Body, Previews, Secondary content, Additional actions y Feedback actions. Composer: disclaimer opcional, campo con Draft, divisor, selector de modelo opcional, Tools y enviar. Preview interno: icono Table, título editable y badge Tabla. Dos glifos internos reutilizables conservan geometría fuente.

## 4. Properties

Message: Message text TEXT. Response: Agent VARIANT BENI/NAVI; Show previews=false, Show secondary content=false, Show additional actions=false; cinco propiedades SLOT. Nombre del agente es identidad fija de la variante; badge anidado editable/expuesto. Composer: Disclaimer TEXT, Show disclaimer=true, Show model selector=false, Model label TEXT; Draft y Tools SLOT. El placeholder es texto directamente editable dentro de Draft: Figma no permite conectar referencias de propiedades del anfitrión a subcapas de Slot. Los controles dentro de Slots se editan directamente, no mediante isExposedInstance. Preview: Title TEXT, badge anidado editable. No propiedades que finjan ejecución.

## 5. Variants

Solo Response es set de dos variantes. Message/Composer/Preview/glifos son componentes independientes. Total siete principales (cuatro configuraciones públicas y tres auxiliares). No variantes por cantidad de mensajes, previews, acciones o tema.

## 6. Sizes

Ancho de referencia616px para Message/Response/Composer; altura HUG. Burbuja con ancho máximo494 y margen izquierdo122 en muestra, ancho flexible en contenedor estrecho. Respuesta padding horizontal16, avatar32, gap8; columna flexible. Los controles Icon Button Small24 se reutilizan sin escalar principales; composer reserva envoltura32 con padding4 para alineación. Badge25px según DS (fuente24). Geometría de siluetas32×31/31.0518 es fija ilustrativa, no token inventado. Preview ancho de columna, padding16. Pruebas de ancho360 y616, no breakpoints de producto.

## 7. States

Estado base visual. BENI/NAVI identifican agente, no estado. Controles anidados conservan estados disponibles de sus contratos, sin agregar máquinas de estados al padre.

## 8. Behavior

No prototipar envío, grabación, adjuntos, copia real, generación de tabla ni valoración persistida. Tampoco animar personajes con destinos externos no auditados. Se reconstruye la composición visual homologada; prototipo fuente es evidencia, no comportamiento aprobado de aplicación.

## 9. Accessibility

Producto debe definir nombres accesibles, foco, teclado y anuncios. La muestra no certifica accesibilidad web ni tamaño táctil. Mantener legibilidad y registrar contraste observado por temas; no cambiar paleta para ocultar limitaciones.

## 10. Design tokens

Única fuente de datos: sources/inventories/tokens.inventory.json, SHA256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. [Preflight](../implementations/figma/conversation.v0.1.0.preflight.json) conserva mapa derivado ID local/nombre/colección/modos y aliases, no otro catálogo normativo.36 roles comprobados en cuatro modos contra alias primitivo, valor, description y scopes; no variables nuevas.

| Uso | Rol existente |
|---|---|
|Burbuja enviada|color/surface/brand/accent|
|Campo/Preview/muestra|color/background/default|
|Texto principal/secundario/placeholder|color/text/primary, color/text/secondary, color/text/tertiary|
|Borde campo/preview y divisor|color/border/subtle, color/border/strong|
|Glifos de agente y acciones destacadas|color/icon/brand|
|Rasgos del glifo y enviar|color/icon/on-brand|
|Iconos neutrales|color/icon/primary|
|Superficie enviar|color/interactive/primary/default|
|Tipografía|font/family/base; font/weight/regular o bold; font/size/xs,sm,md; font/line-height/xs,sm,md; font/letter-spacing/normal|
|Espaciado/radio/borde|spacing/none,xs,sm,md,lg; radius/sm,md; stroke/xs|
|Iconos/controles|size/lg,xl,2xl|

Los controles anidados consumen sus contratos y enmiendas vigentes, incluida SIX-FAMILY-COLOR-001. No usar active-bg para simular un envío seleccionado ni roles warning para distinguir una identidad de agente. Badge light neutral reemplaza la codificación info/warning de categorías del origen; sus textos identifican el tipo de agente.

## 11. Content rules

Textos fuente como demo: solicitud de facturas, respuesta BENI/NAVI, títulos de preview, Crear indicador/Agregar a dashboard, placeholder y disclaimer. No implican capacidades fiscales reales. Editar texto no convierte Placeholder en dato precargado ni habilita una acción.

## 12. Composition rules / Slots

P-SLOTS0.1.0 REQUIRED. Doce Slots: cinco por respuesta (Body, Previews, Secondary content, Additional actions, Feedback actions) y dos en Composer (Draft, Tools). Body/Draft/Secondary content verticales y ancho FILL, altura HUG; aceptan texto/instancias homologadas. Previews vertical, ancho FILL y gap8; muestra un Preview oculto. Additional actions horizontal WRAP gap8, muestra dos Buttons ocultos. Feedback actions horizontal gap8, tres Icon Buttons. Tools horizontal gap8 con adjuntar/micrófono; envío fuera del Slot para preservar jerarquía.

Mecanismo ComponentNode.createSlot y propiedad SLOT con slotSettings: minChildren null (sin mínimo; se acepta vacío), maxChildren null, allowPreferredValuesOnly false; cantidades son restricciones de composición Figma, no límites de negocio. Insertar/quitar/reordenar/sustituir en instancia sin detach; vacío estructural permitido, sin inventar mensaje vacío. Hijos de contenido ancho flexible; acciones mantienen su geometría DS y pueden envolver. No scroll ni alturas fijas que limiten cardinalidad. El consumidor conserva tokens/temas del contenido insertado. Preferencias del picker orientan, no validan por sí solas.

## 13. Responsive behavior

Auto layout: mensajes/respuestas/composer siguen ancho del anfitrión; bloques textuales crecen verticalmente. Header de respuesta y footer composer envuelven si falta espacio. No hay breakpoint móvil ni envío anclado al viewport definido. Ancho360 es caso QA, no nueva variante.

## 14. Edge cases

QA estructural:0,1,muestra y más que muestra (4previews/5acciones); reordenar y reemplazar; texto largo; ancho360; cambio BENI↔NAVI conservando overrides pertinentes. La aplicación define límites de caracteres, adjuntos y conversaciones vacías.

## 15. Forbidden combinations

No crear primitivas nuevas, bindings remotos en UI ni literales RGB en paints consumidores; no token de texto en shape. No importar variables de prototipo como Foundations. No desacoplar controles DS ni modificar principales ajenos. No convertir gris/ámbar del personaje en semántica disabled/warning. No atribuir QA a comportamiento web.

## 16. Design ↔ Code mapping

Solo Figma. Se normaliza Property2 en piezas funcionales; Slots separan contenido y acciones de identidad. JSON gobierna datos, este MD composición. La futura API frontend necesita contrato propio.

## 17. Acceptance criteria

AC01 página única y siete principales/cuatro configuraciones; AC02 dependencias locales verificadas y Phosphor vinculado; AC03 paints UI/glifos con roles locales correctos y texto propio/acciones con cinco bindings tipográficos más fill; Count Small oculto conserva la excepción de Dot; AC04 aliases y cuatro modos coinciden con JSON; AC05 doce Slots reales y pruebas desde instancia; AC06 textos/booleanas/exposición funcionales y respuesta intercambiable; AC07 captura de muestra con estados opcionales visibles, sin solapamiento/recorte; AC08 IDs/contrato/QA registrados y fuente intacta. Todos mapean REQ-CV-01–07.

## 18. Examples

Una muestra compacta contiene mensaje, respuesta BENI, respuesta NAVI con Preview/acciones y composer. Maestros quedan fuera de la muestra. Contenido de prueba temporal se retira al terminar QA.

## 19. Source of truth

[Evidencia fuente](../drafts/contracts/conversation.source.component-contract.md), [snapshot](../sources/figma-snapshots/conversation.20355-72763.observation.2026-10-08.json), JSON canónico, contratos DS vigentes y [decisión](../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md). La inspección PARTIAL no se transforma en completa: propiedades defectuosas de Anticipa se reconstruyen explícitamente; no se copian.

## 20. Change management

Promover a specs tras QA documental/técnico PASS; ajustes posteriores allí. Mantener user_audit PENDING por excepciones. No publicación de biblioteca ni regeneración de grafo automática.

## 21. Deviations and readiness

Homologaciones delegadas: separación de set heterogéneo; badges neutrales25px; Icon Button24 dentro de envoltura32; Preview title16/24 en escala canónica; disclaimer12/16 y separación4 (fuenteAUTO/6); radios8 de DS; glifos estáticos con brand/on-brand en vez de RGB fijo azul/naranja/gris; fuente no usa el mismo tema para todos sus elementos. No copiar sombra literal del composer: superficie/borde DS sin elevación, evitando ampliar Foundations para un efecto fuera de datos canónicos. Siluetas preservadas, cambios cromáticos explícitos por homologación. No estados de producto inventados. Preflight de alias/controles resuelto; capacidad Slots comprobada en las doce regiones mediante instancias, con vacío, inserción, reordenamiento, sustitución y cambio de variante.

## 22. Cierre técnico y dependencias vigentes

Construido y validado el 2026-10-08. [Estado e IDs](../implementations/figma/conversation.v0.1.0.state.json), [QA técnico](../qa/implementations/conversation.v0.1.0.review.md). Página765:6, Message765:271, Response766:119 (BENI765:274 / NAVI765:342), Composer765:397; muestra766:120. Auxiliares765:249/254/258. QA técnico PASS acotado; auditoría humana PENDING y biblioteca UNPUBLISHED. El paso a specs no equivale a aprobación humana.

Consumir [Button0.2.0](components/button.contract.v0.2.0.md), [sus bindings locales0.2.2](components/button.local-bindings.amendment.v0.2.2.md), [Badge](components/badge.contract.v0.1.0.md), [su color fuente0.1.2](components/badge.source-color-amendment.v0.1.2.md), [Icon Button](icon-button.contract.v0.1.0.md), [Dot](components/dot.contract.v0.1.0.md) y [SIX-FAMILY-COLOR](components/six-family-color.amendment.v0.1.0.md). El fondo del conteo oculto usa la [extensión Dot vigente](foundations/foundations.dot-background-colors.amendment.v0.1.4.md). Copy reutiliza el principal local546:256 como iconografía de la acción, sin adoptar comportamiento de Table.

El cotejo completo incluye40 roles consumidos (38 del inventario base y dos de extensiones vigentes),38 primitivas y160 aliases por modo, con description/scopes y valores coincidentes. Los36 roles del preflight eran una selección de construcción, no el inventario final de dependencias. [Readback completo](../implementations/figma/conversation.v0.1.0.tokens-readback.json).

Excepciones heredadas, no nuevos requisitos: los nueve Count Small de Icon Button están ocultos (Show count=false) y mantienen tipografía literal4px, interlineado160% y tracking−2% de Dot; no activarlos para comunicar conteo indispensable. No se amplía Foundations para esa geometría. Los cuatro textos de Buttons reciben aquí binding local de tracking normal, sin modificar sus principales. Las instancias dentro de Slots se editan directamente.

Contraste*: en Servicios, texto brand sobre blanco y texto blanco sobre acción primaria3.236:1; los bordes sutiles sobre blanco1.320–1.706:1 y divisor neutral1.233:1. Limitaciones conservadas conforme al criterio del usuario; no se declara WCAG PASS. [Mediciones](../qa/implementations/conversation.v0.1.0.contrast.json). Texto principal de burbuja10.466–13.524:1, placeholder4.759:1, disclaimer7.578:1. Sin cambios cromáticos para elevar contraste.

La fuente no se modificó; geometría de muestra homologada, no copia píxel a píxel. Draft, Body y Slots vacíos pueden conservar altura mínima estructural; no se promete colapso automático ni estado vacío de producto. Prueba360px sin desbordes, crecimiento de texto verificado; no certifica todos los anchos posibles. El alcance funcional sigue limitado por la sección8.
