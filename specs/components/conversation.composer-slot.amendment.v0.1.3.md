---
contract_id: CONVERSATION-COMPOSER-SLOT-001
version: 0.1.3
status: DELEGATED_FOR_BUILD
applies_to: CONVERSATION-001
base_contract: specs/conversation.contract.v0.1.0.md
user_audit: NOT_REQUIRED
human_review_policy: OPTIONAL_NON_BLOCKING
figma_page_name: Conversation
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
slot_applicability: REQUIRED
---

# Conversation Composer · Slot de contenido del aviso

Fecha: 2026-10-20. Solicitud posterior del usuario: «se me pasó decirte que le agregues slot». Alcance de implementación: todo el contenido del aviso nuevo, conservando su composición inicial. Principal `765:397`, página Conversation `765:6`.

## Precedencia y alcance

Esta enmienda sustituye únicamente la clasificación `NOT_APPLICABLE` del aviso y su estructura fija en [CCA 0.1.2](conversation.composer-action.amendment.v0.1.2.md), además de ampliar CCA-06/07 y su aceptación. Las demás reglas de CCA y del [contrato base](../conversation.contract.v0.1.0.md) permanecen aplicables. El QA anterior se conserva como evidencia histórica; no acredita el Slot nuevo.

La petición explícita establece `REQUIRED` bajo [P-SLOTS](../../protocols/SLOTS-REVIEW-AND-IMPLEMENTATION.md). El usuario confirmó explícitamente «Todo el contenido del aviso (texto y acciones)»; el alcance es `EXPLICIT`. No añade comportamiento de créditos, navegación ni bloqueo del envío.

## Anatomía y propiedad

| Campo | Definición |
|---|---|
| Identificador semántico | `Notice content` |
| Propietario | Conversation Composer, `765:397` |
| Ubicación | Dentro del contenedor opcional `1087:383`, antes del campo de escritura |
| Mecanismo | Slot nativo creado por `ComponentNode.createSlot()`, propiedad de tipo `SLOT`; ID `1103:192`, propiedad `Notice content#1103:0`; readback en QA |
| Contenido inicial | El frame `message` existente `1087:372`, con texto `1087:365` y Button `1087:399`; conservar sus IDs, estilos y bindings |
| Contenido permitido | Bloques de aviso compuestos con texto y componentes del DS; conservar el scope semántico y los estilos tipográficos de sus dependencias |
| Operaciones | Insertar, quitar, reordenar y sustituir hijos en una instancia vinculada, sin detach |
| Cardinalidad | Muestra de un bloque; cero permitido estructuralmente; sin máximo impuesto. Máximo de producto `UNRESOLVED`; ninguna prueba implica capacidad ilimitada |
| Preferidos | Sin lista restrictiva ni `allowPreferredValuesOnly`; el tipo de contenido es una regla documental |
| Visibilidad | `Show action#1087:0`, default `false`, sigue gobernando todo el contenedor |

Draft `765:400` y Tools `765:413` conservan sus Slots y reglas. El envío permanece fuera de estos Slots. No se reemplaza ni se duplica el principal.

## Composición y tokens

El Slot se dispone en Auto Layout vertical, ancho FILL y alto HUG, con gap `spacing/sm` y paddings `spacing/none`. Sus hijos se ajustan al ancho; los bloques extensos crecen en altura. No introduce fondo, borde, radios ni clipping propios. El contenedor exterior mantiene su padding horizontal `spacing/lg`. El frame de aviso inicial conserva la decoración y distribución de CCA 0.1.2.

El Slot vacío no genera mensaje de producto ni acción; `Show action=false` oculta la región. La representación vacía visible conserva una caja de edición de 49 px en Figma; web `null` no añade altura propia. Esta diferencia estructural se registra en QA y no define semántica de producto. No se añade scroll ni altura máxima.

Se reutilizan `spacing/none` (`VariableID:12:18`) y `spacing/sm` (`VariableID:12:30`), verificados en el inventario canónico y en Figma. El texto inicial mantiene Caption/Semibold y Caption/Regular por rango. Ningún token ni estilo nuevo es necesario.

## Mapeo web

`ConversationComposer` añade `noticeContent?: ReactNode`. `undefined` muestra el aviso inicial compatible con `actionMessage`, `actionLabel` y `onAction`; `null` permite región vacía. Un nodo o una colección reemplaza el contenido inicial y se distribuye verticalmente con el mismo gap. La pantalla consumidora controla orden y composición mediante React; `showAction` conserva su responsabilidad de visibilidad.

El contenido se mantiene fuera del formulario de envío. Cada acción personalizada define su callback local y usa componentes del DS. No se modifica el borrador al insertar, reordenar, ocultar o sustituir el aviso.

## Aceptación

1. Leer propiedad `SLOT`, ID, settings y referencias reales después de construir.
2. En una instancia vinculada probar vacío, uno y tres bloques; insertar, quitar, reordenar y sustituir. Conservar el vínculo al principal.
3. Probar 616 y 360 px, contenido largo, crecimiento vertical y ausencia de recortes; revisar una captura de composición final.
4. Verificar tokens, estilos del contenido inicial y herencia en Contable, Administrativo, Servicios y Personas.
5. Alternar `Show action` sin perder overrides/contenido. Composer no tiene ejes de variantes: cambio de variante `NOT_APPLICABLE`.
6. Conservar los IDs iniciales, Draft/Tools, instancia de consumo existente y principales ajenos.
7. Web: contenido inicial, `null`, múltiples bloques, reordenación/sustitución, callback independiente y borrador conservado.
8. Sincronizar registro, documentación web, catálogo, ambas skills y grafo; la publicación remota no forma parte del alcance.

## Evidencia

[Preflight](../../implementations/figma/conversation-composer.v0.1.3.preflight.json), [cotejo canónico](../../qa/contracts/conversation-composer.v0.1.3.preflight.json) y [QA documental](../../qa/contracts/conversation-composer.v0.1.3.review.md). Delegación técnica después de QA documental PASS; no equivale a aprobación humana. [QA de implementación](../../qa/implementations/conversation-composer.v0.1.3.review.md) y [estado por destino](../../implementations/figma/conversation-composer.v0.1.3.state.json).

## Changelog

0.1.3 · 2026-10-20: Slot nativo para componer el aviso opcional del Composer, solicitado después del cierre 0.1.2.
