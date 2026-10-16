---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-AVATAR-FALLBACK-SOURCE-COLOR-002
name: Avatar fallback source color
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.11
last_updated: 2026-09-24
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.avatar-roles.v0.1.1.json]
decision_refs: [DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-CONTRAST-LIMITATIONS-001, DEC-MIGRATION-TRACEABILITY-001]
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: Promoción del cambio cromático AC-TOK-AVA-001–003, sin promover la base Avatar ni resolver AUD-006.
>
> Sustento: [QA documental 1](../../qa/contracts/avatar.source-color-amendment.v0.1.1.review.md); [QA técnico 1](../../qa/implementations/avatar.source-color.v0.1.1.figma.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Foundations · Avatar fallback Servicios, color de origen 0.1.11

Sustituye **solo el alias Servicios** de `color/background/avatar-fallback` establecido en [Foundations Avatar Roles 0.1.6](foundations.avatar-roles.amendment.v0.1.6.md): de la primitiva `color/orange/600` a `color/orange/500` (`#FF5300`) ya aprobada. El [JSON de override 0.1.1](../../drafts/foundations/ai-design-system.avatar-roles.v0.1.1.json) gobierna este campo; el 0.1.0 permanece histórico para los otros roles y modos. Nombre, tipo `COLOR`, descripción canónica, `codeSyntax` y scope `FRAME_FILL` permanecen intactos. No se crean variables ni primitivas.

La fuente Avatar usa orange/500 en Servicios para sus ocho fondos Icon/Text; los otros modos ya coinciden. El cambio de 0.1.6 a orange/600 fue exclusivamente por contraste. Esta restauración conserva el color original y marca `*` la relación de iniciales blancas sobre orange/500 (~3.24:1), sin declarar conformidad WCAG. La mejora de tamaño de iniciales Small/Medium es independiente y no se revierte por esta enmienda.

`AC-TOK-AVA-001`: readback del alias Servicios, de los otros tres aliases intactos, nombre, tipo, descripción y scope del rol. `AC-TOK-AVA-002`: verificar los ocho consumidores de fondo Icon/Text y los doce Dot anidados sin pérdida de binding, además de ausencia de cambios de color en los otros modos. `AC-TOK-AVA-003`: documentar contraste `*` y ausencia de mutación de `font/size/avatar-small`. Auditoría humana pendiente, biblioteca sin publicar.
