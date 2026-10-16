---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-ICON-BUTTON-BACKGROUNDS-001
name: Icon Button interactive backgrounds
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.9
last_updated: 2026-09-23
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.icon-button-backgrounds.v0.1.0.json]
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: Los dos fondos Hover/Active conservan su definición. El cierre cromático posterior acredita sus aliases y consumidores; no se extiende el veredicto a otros requisitos. Aplicar [referencia 1](../components/six-family-color.amendment.v0.1.0.md).
>
> Sustento: [QA documental 1](../../qa/contracts/foundations.icon-button-backgrounds.amendment.v0.1.9.review.md); [QA técnico 1](../../qa/implementations/six-families.color.v0.1.0.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Foundations · fondos semánticos de Icon Button 0.1.9

El [JSON canónico](../../drafts/foundations/ai-design-system.icon-button-backgrounds.v0.1.0.json) añade dos variables `COLOR` en `semantic`, cada una con scope exclusivo `FRAME_FILL`, descripción única y cuatro aliases a primitivas locales existentes:

- `color/interactive/icon-button/hover-bg` reproduce el hover pálido de la fuente con blue/100, green/100, orange/100 y purple/100. Un rol `active` de igual valor sería semánticamente incorrecto para Hover.
- `color/interactive/icon-button/active-bg` reproduce el estado Active con blue/400, green/500, orange/500 y purple/500. `color/interactive/primary/default` comparte valores, pero su nombre y descripción gobiernan el estado base, no Active.

No se añaden primitivas ni se cambia el inventario histórico. Antes de usar estas variables en el componente, comprobar ausencia previa, tipo, nombre, descripción, scope, modos, aliases y `codeSyntax` por lectura posterior. El cambio fue anunciado al usuario y permanece pendiente de auditoría humana; no autoriza web ni publicación.
