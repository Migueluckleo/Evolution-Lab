---
contract_id: CONVERSATION-COMPOSER-ACTION-001
version: 0.1.2
status: DELEGATED_FOR_BUILD
applies_to: CONVERSATION-001
base_contract: specs/conversation.contract.v0.1.0.md
user_audit: NOT_REQUIRED
human_review_policy: OPTIONAL_NON_BLOCKING
figma_page_name: Conversation
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
slot_applicability: REQUIRED
---

# Conversation Composer · aviso opcional con acción

Fecha: 2026-10-20. Revisión acotada del principal `765:397`, página `765:6`. La solicitud del usuario autoriza documentar su modificación y corregir parámetros incompatibles con el sistema canónico, bajo [DEC-AI-TECHNICAL-CLOSURE-001](../../registry/DEC-AI-TECHNICAL-CLOSURE-001.md).

## Alcance y precedencia

Amplía Anatomy, Properties, Content rules, Composition, Responsive, Design ↔ Code y Acceptance del [contrato base](../conversation.contract.v0.1.0.md) exclusivamente para Composer. Conserva Message, Response, personajes, Draft y Tools. No sustituye las enmiendas de identidad ni tipografía de los consumidores anteriores. No introduce un estado de cuenta, lógica de créditos, compra, navegación ni bloqueo de envío.

La fuente `OBSERVED` es el [snapshot anterior a correcciones](../../sources/figma-snapshots/conversation-composer.765-397.before.2026-10-20.json). Se adopta la composición observada por delegación técnica; no se atribuye aprobación humana del detalle.

## Anatomía, propiedades y contenido

- `input` (`1087:497`) agrupa el aviso y el campo existente en Auto Layout vertical, sin separación.
- `container` (`1087:383`) contiene `message` (`1087:372`), con texto `description` (`1087:365`) y una instancia de Button (`1087:399`, principal `26:102`).
- `Show action#1087:0` es BOOLEAN, default `false`, y controla la visibilidad del aviso completo. El nombre nativo se conserva por compatibilidad. No controla el botón Enviar.
- El Button conserva `type=default`, `size=small`, `state=default`, sin iconos; texto de muestra `Default`, editable mediante su propiedad anidada. No se inventa destino para esa acción.
- El texto observado «Alcanzaste tu límite mensual de créditos. Se renuevan el 1 de noviembre.» es una muestra editable. El mes y la disponibilidad real proceden de la pantalla consumidora; no se calcula una fecha ni se impone esa política al producto.
- Disclaimer, selector de modelo y Slots conservan sus propiedades y defaults anteriores. Mostrar el aviso no deshabilita el Composer.

## Requisitos y normalización

| ID | Requisito MUST | Procedencia y verificación |
|---|---|---|
| CCA-01 | Conservar IDs del principal, aviso y dependencias; booleano `Show action=false` conectado al contenedor. | OBSERVED snapshot; lectura de propiedades e instancia. |
| CCA-02 | Grupo y contenedor siguen el ancho disponible; mensaje crece en altura. Texto con ancho flexible y reflow; botón conserva geometría DS. | DERIVED corrección de ancho fijo616 y texto WIDTH_AND_HEIGHT que impedían adaptación; probar616 y360. |
| CCA-03 | Vincular separaciones, padding, radios y trazos del aviso a los roles existentes indicados abajo. | EXPLICIT reglas canónicas y valores OBSERVED; lectura de bindings. |
| CCA-04 | Sustituir el borde exclusivo de Pagination por `color/border/subtle`. | EXPLICIT scope semántico; token anterior `color/border/pagination/page/default` es exclusivo de Pagination. |
| CCA-05 | Texto nuevo usa estilos base por rango: énfasis inicial Caption/Semibold y resto Caption/Regular; sin overrides posteriores de formato. | EXPLICIT política tipográfica; OBSERVED énfasis inicial Bold sobre estilo Regular, normalizado a estilo base. |
| CCA-06 | Mantener Draft y Tools como Slots nativos editables, sin detach; preservar el envío fuera de Tools. | EXPLICIT contrato base/P-SLOTS; pruebas de instancia. |
| CCA-07 | Web expone visibilidad, mensaje, etiqueta y callback local; documentar y demostrar con datos ficticios. | P07; no servicios de cuenta ni compra. |
| CCA-08 | Readback y QA posteriores, fuentes/hashes, catálogo y ambas skills vigentes. | P05/P06/P08. |

## Tokens y tipografía

El [inventario aprobado](../../sources/inventories/tokens.inventory.json) conserva nombres, valores, aliases, modos, scopes y única `description`. El [preflight](../../implementations/figma/conversation-composer.v0.1.2.preflight.json) contiene IDs reales leídos; el [cotejo](../../qa/contracts/conversation-composer.v0.1.2.canonical-check.json) verifica23 variables, incluidos los aliases primitivos, sin crear tokens.

| Parte/propiedad | Rol canónico |
|---|---|
| Grupo input: gap y cuatro paddings | `spacing/none` |
| Contenedor del aviso: padding horizontal / vertical / gap | `spacing/lg` / `spacing/none` / `spacing/sm` |
| Mensaje: padding horizontal / vertical / gap | `spacing/lg` / `spacing/sm` / `spacing/sm` |
| Esquinas superiores / inferiores del aviso | `radius/xl` / `radius/none` |
| Trazo superior y laterales / inferior | `stroke/xs` / `stroke/none` |
| Fondo / texto / borde del mensaje | `color/background/subtle` / `color/text/primary` / `color/border/subtle` |

El [catálogo tipográfico0.1.2](../tokens/ai-design-system.typography.v0.1.2.json) gobierna las recetas. No se duplica el catálogo ni se cambia el estilo compacto del disclaimer existente.

| Consumidor | ID lógico | TextStyle ID |
|---|---|---|
| `1087:365`, frase inicial enfatizada; en la muestra rango `[0,42)` | `caption-semibold` | `S:44d1ab87ed7291cac7a1f308466f04aca4cb25b8,` |
| `1087:365`, resto de la muestra `[42,72)` | `caption-regular` | `S:ed58d525ce135d142794e5c47e201096c023a800,` |

Los offsets pertenecen a esta muestra, no son un límite de contenido. En ediciones de texto se conservan los roles y se vuelven a comprobar los rangos. El cambio de receta compacta16px a la base porcentual modifica el interlineado y tracking; queda explícitamente normalizado por CCA-05. El borde adopta los cuatro temas del Composer; no hereda los modos específicos de Pagination.

## Slots y adaptación

P-SLOTS0.1.0: `REQUIRED` en Draft/Tools, sin alterar su contrato ni cardinalidad. El aviso añadido es `NOT_APPLICABLE` como Slot: tiene un texto y una acción de estructura fija; variar el texto o mostrar/ocultar el bloque no demuestra necesidad de lista. No se crea una variante por cantidad.

Ancho de referencia616; QA reducido360. El mensaje mantiene botón a la derecha y texto FILL con altura HUG. Conserva padding horizontal16 del contenedor, padding16/8 del mensaje y gap8 mediante sus tokens; las medidas no fijan una altura universal. Texto largo debe aumentar altura sin invadir el botón. El aviso oculto no reserva espacio. No se promete soporte universal de anchos ni listas ilimitadas.

## Mapeo web y límites

`ConversationComposer` añade `showAction=false`, `actionMessage`, `actionLabel='Default'` y `onAction`. `actionMessage` acepta contenido React para conservar énfasis y texto editable; no convierte la estructura del aviso en una lista de acciones. La acción es Button default/small, `type=button`, con callbacks locales. Si no hay callback, no se simula éxito ni navegación.

El ejemplo usa datos ficticios y cambia únicamente un mensaje local al pulsar. `disabled` continúa gobernando entrada/envío; no es un estado de créditos. La pantalla define la fecha, habilitación y destino reales.

## Aceptación y trazabilidad

Verificar booleano off/on, instancia vinculada, texto largo, ancho616/360, estilos completos por rango, bindings/aliases y cuatro temas, preservación de Draft/Tools y geometría de Button. Comparar implementación web, callback independiente del submit, contenidos ocultos y reflow. Los resultados viven en QA, separados de este contrato.

[QA documental](../../qa/contracts/conversation-composer.v0.1.2.review.md) y [QA de implementación ejecutado](../../qa/implementations/conversation-composer.v0.1.2.review.md). El [estado de implementación](../../implementations/figma/conversation-composer.v0.1.2.state.json) conserva el alcance y los IDs; la delegación no equivale a aprobación humana.

## Changelog

0.1.2 · 2026-10-20: documenta aviso con acción añadido por el usuario; normaliza rol de borde, bindings, texto por rango y adaptación; conserva identidad y API existente.
