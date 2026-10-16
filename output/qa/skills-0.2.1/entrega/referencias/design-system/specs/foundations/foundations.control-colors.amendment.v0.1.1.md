---
amendment_id: AMD-FOUNDATIONS-CONTROL-COLORS-001
status: DELEGATED_FOR_BUILD
applies_to: FOUNDATIONS-TOKENS-001
base_contract_version: 0.1.0
base_contract_digest_sha256: e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999
version: 0.1.1
decision_refs: [DEC-TOGGLE-VISUAL-CONTRAST-002, DEC-SEMANTIC-EXTENSIONS-001]
data_ref: drafts/foundations/ai-design-system.control-colors.v0.1.0.json
data_digest_sha256: 4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839
base_data_ref: sources/inventories/tokens.inventory.json
base_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-23
user_audit: PENDING
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: Los cuatro aliases de border/control se rigen por0.1.12; Toggle ya no consume ese borde conforme a0.1.5. La definición de background/control-hover permanece. Los conteos y consumidores iniciales inferiores son el corte histórico de creación. Aplicar [referencia 1](foundations.control-border-source-color.amendment.v0.1.12.md), [referencia 2](../components/toggle.source-color-amendment.v0.1.5.md).
>
> Sustento: [QA documental 1](../../qa/contracts/foundations.control-colors.amendment.v0.1.1.review.md), [QA documental 2](../../qa/contracts/selection-control-source-color.v0.1.1.review.md); [QA técnico 1](../../qa/implementations/control-colors.v0.1.0.figma.review.md), [QA técnico 2](../../qa/implementations/selection-control-source-color.v0.1.1.figma.review.md), [QA técnico 3](../../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Enmienda delegada de Foundations · colores neutrales para controles

La autorización explícita del usuario permite agregar variables cuando sean necesarias, con definición sincronizada en JSON, contratos y Figma. Esta enmienda no cambia ni suplanta las 270 variables de [FOUNDATIONS-TOKENS-001 0.1.0](foundations-tokens.contract.md): extiende exclusivamente el destino AI Design System. El inventario fuente conserva sus bytes y digest. El [JSON de extensión](../../drafts/foundations/ai-design-system.control-colors.v0.1.0.json) es la única definición editable de nombre, tipo, descripción, scopes y valores por modo de los dos tokens nuevos; este MD gobierna reglas y aceptación.

| ID | Requisito | Fuerza | Procedencia | Comprobación |
|---|---|---|---|---|
| REQ-TOK-EXT-001 | Crear exactamente las dos variables del JSON de extensión en la colección local `semantic` de AI Design System, sin modificar variables existentes. | MUST | EXPLICIT autorización de ampliación + DERIVED solución de contraste y scopes | AC-TOK-EXT-001 |
| REQ-TOK-EXT-002 | Conservar por variable nombre, tipo `COLOR`, única `description`, scopes propios, `codeSyntax: {}` y los cuatro aliases a la variable primitiva local indicada por el JSON. | MUST | DERIVED del JSON de extensión | AC-TOK-EXT-002 |
| REQ-TOK-EXT-003 | Registrar los IDs reales de destino, la correspondencia JSON↔Figma y los consumidores Toggle; no alterar el inventario fuente ni adjudicar aprobación humana al detalle de los tokens. | MUST | EXPLICIT fidelidad JSON/Figma + regla SDD | AC-TOK-EXT-003 |

La primera necesidad se observa en Toggle Off/Default y Off/Focus: el fondo claro de la fuente mide 1.23:1 contra blanco; los bordes neutros existentes, `default` y `strong`, miden 2.56:1 y 1.23:1. `disabled` no aplica semánticamente a un Off todavía operable y comparte el gris claro. La segunda necesidad se observa en Off/Hover, cuyo track usa `color/text/tertiary` con scope `TEXT_FILL` como fondo, contraviniendo la separación solicitada por el usuario. El primitivo `color/neutral/500` ya existe tanto en el JSON base como en Figma destino; frente a blanco mide 4.76:1. Dos roles semánticos con scopes distintos (`STROKE_COLOR` y `FRAME_FILL`/`SHAPE_FILL`) aliasan el mismo primitivo sin confundirse por compartir valor.

## Acceptance criteria

| ID | Resultado necesario |
|---|---|
| AC-TOK-EXT-001 | La colección `semantic` contiene exactamente las dos variables locales con los nombres del JSON de extensión; el conteo pasa de 129 a 131. La primitiva y los roles anteriores conservan sus IDs, valores y aliases. |
| AC-TOK-EXT-002 | Una lectura posterior a la escritura iguala para ambas `name`, `resolvedType`, `description`, `scopes`, `codeSyntax` y `valuesByMode` con el JSON de extensión, resolviendo cada alias por ID a `color/neutral/500`. Ningún modo queda sin valor. |
| AC-TOK-EXT-003 | El registro guarda ambos IDs de Figma, digest del JSON de extensión, contrato y QA; Toggle consume el borde mediante stroke y el hover mediante fill. El digest del inventario fuente sigue igual y `user_audit` continúa `PENDING`. |

La implementación es Figma solamente. No autoriza publicación de la biblioteca, CSS ni propagación automática a otras familias. [QA documental](../../qa/contracts/foundations.control-colors.amendment.v0.1.1.review.md) `PASS`; auditoría humana posterior.
