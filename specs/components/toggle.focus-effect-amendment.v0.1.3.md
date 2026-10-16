---
amendment_id: AMD-TOGGLE-FOCUS-EFFECT-003
status: DELEGATED_FOR_BUILD
applies_to: TOGGLE-001
base_contract_version: 0.1.0
base_contract_digest_sha256: c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38
version: 0.1.3
decision_refs: [DEC-SEMANTIC-EXTENSIONS-001]
extension_data_ref: drafts/foundations/ai-design-system.focus-effects.v0.1.0.json
extension_data_digest_sha256: 0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4
source_data_ref: sources/inventories/tokens.inventory.json
source_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-23
user_audit: PENDING
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: QA acotado a bindings semánticos y conservación del efecto. No certifica fidelidad total del halo: AUD-003 permanece abierto. La mención inferior a ocho variantes es previa a Mixed0.1.4; fills/strokes se leen con0.1.5. Aplicar [referencia 1](toggle.mixed-amendment.v0.1.4.md), [referencia 2](toggle.source-color-amendment.v0.1.5.md).
>
> Sustento: [QA documental 1](../../qa/contracts/toggle.focus-effect-amendment.v0.1.3.review.md); [QA técnico 1](../../qa/implementations/toggle.v0.1.3.figma.review.md), [QA técnico 2](../../qa/implementations/toggle.source-color.v0.1.5.figma.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Enmienda candidata de Toggle · binding semántico del foco

Esta enmienda sustituye **solo** la receta de color de los dos DROP_SHADOW de anillo en las variantes On/Focus y Off/Focus de [TOGGLE-001](../../drafts/contracts/toggle.contract.v0.1.0.md). [La enmienda visual y de contraste 0.1.2](toggle.visual-contrast-amendment.v0.1.2.md) continúa vigente para fills y strokes Off. No se modifica el comportamiento de los ocho estados, su layout, propiedades, sombras internas ni dimensiones de los efectos.

| ID | Requisito | Fuerza | Procedencia | Comprobación |
|---|---|---|---|---|
| REQ-TGL-009 | Vincular el color de cada anillo exterior de foco a `color/focus/effect-outer` y el halo interior a `color/focus/effect-inner`, con scope `EFFECT_COLOR` y alias local aprobado en los cuatro modos. | MUST | OBSERVED cuatro bindings con scope equivocado + EXPLICIT semántica estricta | AC-TGL-009 |
| REQ-TGL-010 | Mantener tipos, offsets, radios, spreads, orden y colores resueltos de los efectos, y los seis estados no Focus intactos. | MUST | OBSERVED implementación 0.1.2 + EXPLICIT fidelidad visual | AC-TGL-010 |

Los nodos afectados son `111:135` y `111:155`, ambos `Toggle track`. Antes de esta corrección, cada efecto exterior está ligado a `color/focus/ring` (`STROKE_COLOR`) y cada halo interior a `color/background/default` (`FRAME_FILL`/`SHAPE_FILL`), aunque sus colores resuelven a #1d21b0 y #ffffff. Los nuevos roles tienen exactamente los mismos primitivos y se definen solo en el [JSON de extensión de destino](../../drafts/foundations/ai-design-system.focus-effects.v0.1.0.json); no alteran esas variables previas. La diferencia entre el halo blanco del destino y el literal #f8fafc de la fuente ya estaba documentada en el contrato base y sigue pendiente de auditoría humana.

## Acceptance criteria

| ID | Resultado necesario |
|---|---|
| AC-TGL-009 | Readback de cuatro `effects[].boundVariables.color`: dos IDs de `effect-outer` y dos de `effect-inner`; ambos scopes incluyen exclusivamente `EFFECT_COLOR`, los aliases por modo resuelven y ningún efecto de foco consume `color/focus/ring` ni `color/background/default`. |
| AC-TGL-010 | On/Focus conserva dos efectos; Off/Focus, cinco. Su geometría, orden y colores resueltos coinciden con la lectura previa. El set sigue con ocho variantes; la captura posterior no muestra pérdida del anillo ni cambio visual aparente. |

Alcance Figma únicamente; no hay afirmación de focus funcional en web. `user_audit: PENDING`.
