---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-FEEDBACK-ICON-SCOPES-001
name: Feedback icon scopes
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.7
last_updated: 2026-09-23
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.feedback-icon-scopes.v0.1.0.json]
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: Vigencia limitada a scopes. La restauración posterior de Warning afecta aliases, no este cambio de scope. Aplicar [referencia 1](foundations.warning-icon-source-color.amendment.v0.1.10.md).
>
> Sustento: [QA documental 1](../../qa/contracts/foundations.feedback-icon-scopes.amendment.v0.1.7.review.md); [QA técnico 1](../../qa/implementations/feedback-icon-scopes.v0.1.0.figma.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Foundations · scope de iconos feedback 0.1.7

La [enmienda JSON](../../drafts/foundations/ai-design-system.feedback-icon-scopes.v0.1.0.json) sustituye únicamente `scopes` en tres variables `semantic`: `color/feedback/positive/icon`, `color/feedback/warning/icon` y `color/feedback/danger/icon`. Cada una pasa de `[FRAME_FILL, SHAPE_FILL]` a `[SHAPE_FILL]`, congruente con su categoría de icono. `color/feedback/information/icon` ya es exclusivo `SHAPE_FILL` y no se modifica.

El inventario histórico conserva descripciones y aliases canónicos. Esta enmienda no repite ni redefine esos campos: nombres, IDs, tipos, modos, valores, primitivas, descripciones y code syntax deben quedar idénticos tras la mutación. El chequeo read-only de nueve páginas de familias existentes encontró dos consumidores, ambos VECTOR visibles en Badges, y cero consumidores FRAME_FILL. No se altera apariencia ni estructura de componentes. Tras la escritura se releen los tres scopes y los dos consumidores; auditoría humana pendiente.
