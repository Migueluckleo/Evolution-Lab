---
contract_id: APP-SHELL-EMBEDDED-CHAT-001
version: 0.1.1
status: DELEGATED_FOR_BUILD
applies_to: APP-SHELL-001
base_contract: specs/app-shell.contract.v0.1.0.md
user_audit: NOT_REQUIRED
human_review_policy: OPTIONAL_NON_BLOCKING
figma_page_name: Layout
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
target_node_id: "1108:3201"
slot_applicability: REQUIRED
---

# App Shell · arquitectura de chat embebido en un aplicativo

Fecha: 2026-10-20. El usuario solicita documentar la composición **App Shell | Chat embebido** para que cada encargo de un chat embebido en un aplicativo respete esta arquitectura. [Fuente Figma](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=1108-3201), instancia `1108:3201`, página `Layout` `1108:620`, principal App Shell `737:304`.

## Alcance, activación y precedencia

**ECS-01 · MUST · EXPLICIT:** aplicar esta arquitectura cuando se solicite «chat embebido», «chat integrado en un aplicativo» o una conversación de IA dentro de la interfaz de una aplicación. La pantalla conserva el contexto del aplicativo. Una solicitud posterior explícita puede modificar el alcance; registrar esa excepción.

Amplía Composition, Content, Responsive, Design↔Code y Acceptance del [App Shell 0.1.0](../app-shell.contract.v0.1.0.md) exclusivamente para este caso de uso. No cambia el principal vacío, crea una variante del shell ni sustituye la arquitectura de un chat independiente. La página Layout contiene una instancia de composición, no una nueva familia de componentes.

La arquitectura queda delegada por la solicitud y el QA documental; las observaciones visuales no se convierten en aprobación global de tokens, estilos o dependencias remotas. El [contrato de extracción MD](../../drafts/contracts/embedded-chat-shell/component-contract.md) y su [modelo YAML](../../drafts/contracts/embedded-chat-shell/component-contract.yaml) son evidencia, no otra definición normativa.

## Arquitectura obligatoria

**ECS-02 · MUST · OBSERVED + adopción EXPLICIT:** conservar esta jerarquía y orden:

```text
App Shell
├── Header del aplicativo
└── Body
    ├── Navigation rail → Sidebar del aplicativo
    └── Content [Slot nativo]
        └── Contenido de chat embebido [vertical]
            ├── Cabecera de contexto: identidad/título y descripción
            └── Área de trabajo [horizontal]
                ├── Chat Section: bienvenida o conversación + Composer
                └── Chat Toolbar: historial y acciones del chat
```

El historial está **a la derecha** del chat, dentro de Content y debajo de la cabecera de contexto. La navegación global permanece **a la izquierda**, fuera de la región del chat. Son regiones distintas con responsabilidades distintas.

**ECS-03 · MUST · DERIVED:** el Header y la Sidebar siguen perteneciendo al aplicativo. No agregar otro Header o Sidebar global dentro de Content. No reemplazar la navegación del aplicativo por el historial, trasladar el historial a la izquierda, convertir esta composición en modal, overlay o ventana flotante, ni eliminar el contexto global por conveniencia.

## Dependencias y responsabilidad

| Región | Componente/contrato propietario | Identidad observada |
|---|---|---|
| Envoltura | [App Shell](../app-shell.contract.v0.1.0.md) | main `737:304`; Content `737:447` |
| Cabecera global | [Header](../header.contract.v0.1.0.md) | instancia `I1108:3201;737:305` |
| Navegación global | [Sidebar](../sidebar.contract.v0.1.0.md) | instancia `I1108:3201;737:412`, Collapsed |
| Conversación | [Chat Section](../chat-section.contract.v0.1.0.md) | main Standby `783:24`; instancia terminada en `1108:3664` |
| Escritura | [Conversation](../conversation.contract.v0.1.0.md), [aviso 0.1.2](conversation.composer-action.amendment.v0.1.2.md) y [Slot 0.1.3](conversation.composer-slot.amendment.v0.1.3.md) | main Composer `765:397` |
| Historial lateral | [Chat Toolbar](../chat-toolbar.contract.v0.1.0.md) | main Expanded `797:316`; instancia terminada en `1108:3665` |
| Acciones y conversaciones | [Chat Tool Item](../chat-tool-item.contract.v0.1.0.md) y [Chat History Item](../chat-history-item.contract.v0.1.0.md) | la muestra incluye referencias remotas; no son nuevos principales canónicos |

**ECS-04 · MUST:** reutilizar las dependencias vigentes sin detach, duplicación de principales ni redefinición de sus variantes. BENI/NAVI conservan las excepciones de identidad existentes. La cabecera de contexto puede adaptar identidad, título y descripción al aplicativo; el logotipo NAVI y la etiqueta Beta observados no obligan a usar Beta ni autorizan redibujar artwork no disponible.

## Layout y tamaños

**ECS-05 · MUST · OBSERVED:** App Shell vertical; Body horizontal; contenido embebido vertical; fila de Chat Section e historial horizontal sin wrap. La cabecera de contexto es HUG en altura y FILL en ancho; el área de trabajo ocupa el espacio restante. Chat Section crece en ancho; el historial conserva su ancho lateral y llena la altura de esa área.

| Referencia desktop observada | Geometría |
|---|---|
| App Shell | 1440×1024 |
| Header / Body | alto96 / alto928 |
| Rail / Sidebar | ancho104 / ancho72 |
| Content | 1336×928 |
| Cabecera de contexto / separación vertical | alto aproximado52 / 32 |
| Área de trabajo | 1336×844 |
| Chat Section / historial | ancho1072 / ancho264 |
| Columna central de Chat Section | máximo816, centrada |

Estas medidas identifican la muestra y no son breakpoints. Los 32 de separación vertical corresponden al rol existente `spacing/2xl`; la muestra no tiene binding en ese wrapper. La fila horizontal declara `SPACE_BETWEEN` e `itemSpacing=32`, pero los bounds leídos muestran **separación efectiva0**: 1072+264=1336. No introducir un gutter32 como supuesta reproducción exacta.

**ECS-06 · MUST · herencia de layout:** la columna de Chat Section conserva máximo816, FILL y centrado conforme a la [enmienda vigente Chat Layout0.1.1](./chat.layout.amendment.v0.1.1.md). Esa enmienda ya sustituyó el máximo542 histórico en ambas variantes; el chat embebido hereda la regla, sin introducir un override adicional. Respetar las restricciones del anfitrión y del contenido. No escalar personajes para llenar el ancho.

## Contenido, estados y Slots

**ECS-07 · MUST:** conservar Content y los Slots heredados: mensajes, sugerencias, Draft, Tools, Notice content, cabecera/acciones/chats/indicadores del historial, títulos y acciones de cada conversación. `slot_applicability: REQUIRED`. Los wrappers locales de dos regiones establecen jerarquía; no representan una lista nueva ni exigen crear otro principal con Slots.

La muestra contiene Standby, tres sugerencias y una conversación visible en el historial; no son límites de cantidad. Header, navegación y cabecera de contexto no se desmontan al pasar de bienvenida a conversación. Aplicar Standby/Active según Chat Section, sin inventar un estado global del shell.

Composer conserva sus props y Slots. En la muestra `Show action=false`, `Show disclaimer=false` y `Show model selector=false`; no son nuevos defaults globales. El aviso y sus acciones siguen dentro de Composer, no dentro del historial. `noticeContent` conserva la composición definida en 0.1.3.

El historial observado está Expanded, muestra «Nuevo chat», Chats y Plan, y oculta Indicators. Sus controles permanecen configurables según Chat Toolbar. Nombre del usuario, empresa, RFC, títulos, fechas, 42/150 y 28% son muestras; no definen cuotas, facturación, políticas ni cálculos.

## Canonicalidad y límites de la fuente

**ECS-08 · MUST:** consumir tokens y estilos canónicos de las familias reutilizadas. El [inventario](../../sources/inventories/tokens.inventory.json), [catálogo tipográfico](../tokens/ai-design-system.typography.v0.1.2.json) y sus enmiendas conservan autoridad. No convertir valores observados en tokens nuevos.

El readback encontró wrappers con valores sin binding; descripción y Beta sin estilo compartido; dependencias remotas en elementos del historial; y un override Contable en Toolbar. Estos hechos son `OBSERVED`, **no excepciones adoptadas**. En futuras construcciones se usan roles semánticos y estilos completos por función, las dependencias locales vigentes cuando existan y el tema del aplicativo; una dependencia artística no resuelta se declara, no se inventa. Esta tarea no modifica Figma ni certifica esos detalles como normalizados.

## Responsive, comportamiento y accesibilidad

**ECS-09 · MUST:** la fuente documenta desktop. No deducir una conversión móvil, ocultamiento automático del historial, drawer, scroll fijo, breakpoint ni tamaño mínimo universal. Para anchos insuficientes documentar la adaptación antes de cambiar la arquitectura; no afirmar validación responsive desde esta captura.

La muestra no define búsqueda, persistencia, envío a una IA, cambio de conversación, navegación, foco o teclado. Las reacciones anidadas de Hover y timeout del personaje son evidencia de prototipo, no un backend ni una política de producto. No se adopta una nueva obligación de animación desde esa reacción. Los controles ejecutables y su accesibilidad se verifican en la pantalla consumidora.

## Consumo web y por skills

**ECS-10 · MUST:** al resolver un encargo de chat embebido, las skills deben leer esta enmienda junto con App Shell, Chat Section, Chat Toolbar y Conversation. Queda referenciada desde el índice de esas familias para que sea consumible por los motores remotos existentes.

El mapeo de composición utiliza `AppShell` (`header`, `sidebar`, `children`), una cabecera de contexto dentro de `children`, `ChatSection` a la izquierda y `ChatToolbar` a la derecha. Sus exports, props y ejemplos existentes se documentan en las fichas web correspondientes. No hay un export nuevo `EmbeddedChatShell` ni un nuevo servicio. El máximo816 procede de Chat Layout0.1.1 y se conserva en esta composición. La API de callbacks pertenece a las piezas y a la pantalla.

Esta entrega modifica documentación de composición y metadatos de consumo; no crea ni modifica implementación React de componentes. P07 se satisface en este alcance con mapeo y documentación de los exports existentes; una pantalla futura debe aportar su propio ejemplo ejecutable y QA de layout.

## Aceptación y trazabilidad

**ECS-11 · MUST:** en cada entrega futura verificar:

1. Header y navegación del aplicativo presentes; una sola envoltura global.
2. Cabecera de contexto dentro de Content, encima del área de trabajo.
3. Chat Section a la izquierda e historial a la derecha, sin confundirlo con la navegación global.
4. Estados, cantidades y composición mediante propiedades/Slots existentes, conservando Composer y sus acciones.
5. Columna central y anchos sustentados; sin gutter, breakpoint o scroll inventados.
6. Bindings, tema, tipografía, artwork y dependencias verificados; las inconsistencias de esta muestra no se propagan como reglas.
7. Captura y QA de la pantalla construida, independientes del QA documental de esta enmienda.

[QA documental y cotejo de arquitectura](../../qa/contracts/app-shell.embedded-chat.v0.1.1.review.md). [Evidencia de inspección](../../sources/figma-snapshots/embedded-chat-shell.1108-3201.index.2026-10-20.json). El QA de arquitectura no acredita edición de Slots, todos los temas, todos los estados ni implementación web de esta pantalla.

## Changelog

0.1.1 · 2026-10-20: regla de composición para chats embebidos solicitada por el usuario, basada en la instancia1108:3201; preserva contratos de piezas y registra límites de canonicalidad.
