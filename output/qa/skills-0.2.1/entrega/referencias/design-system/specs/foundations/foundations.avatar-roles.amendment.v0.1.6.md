---
contract_schema: sdd-project/0.2
contract_id: FOUNDATIONS-AVATAR-ROLES-001
name: Avatar semantic roles
type: foundation-amendment
status: DELEGATED_FOR_BUILD
version: 0.1.6
last_updated: 2026-09-23
user_audit: PENDING
data_refs: [drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json]
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: El alias Servicios del fondo está sustituido por Foundations Avatar fallback0.1.11. El QA de las dos variables no cierra la normalización de tamaños de la familia (AUD-006). Aplicar [referencia 1](foundations.avatar-fallback-source-color.amendment.v0.1.11.md).
>
> Sustento: [QA documental 1](../../qa/contracts/foundations.avatar-roles.amendment.v0.1.6.review.md), [QA documental 2](../../qa/contracts/avatar.source-color-amendment.v0.1.1.review.md); [QA técnico 1](../../qa/implementations/avatar-roles.v0.1.0.figma.review.md), [QA técnico 2](../../qa/implementations/avatar.source-color.v0.1.1.figma.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Foundations · roles de Avatar 0.1.6

El [JSON canónico](../../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json) añade dos variables `semantic`, sin editar el inventario histórico ni crear primitivas:

- `color/background/avatar-fallback`, `COLOR`, scope único `FRAME_FILL`, cuatro aliases a primitivas de marca: blue/400, green/500, orange/600 y purple/500. Conserva los colores de `color/interactive/primary/default` observados en Avatar excepto Servicios: orange/500 daría 3.24:1 con iniciales blancas, mientras orange/600 da 4.72:1. El rol describe un fondo no interactivo; no se amplía ni reutiliza el scope de `color/icon` o `color/text`.
- `font/size/avatar-small`, `FLOAT`, scope único `FONT_SIZE`, alias a `font/size/10` en los cuatro modos. Su consumidor es el texto de Avatar Small de 20 px, cuya fuente usa 6 px. Esta mejora no modifica la escala primitiva ni los demás tamaños tipográficos.

Se verifican ausencia previa, modos/aliases, una descripción por variable, ID real y readback de los consumidores antes de cerrar Avatar. Auditoría humana pendiente; no se publica biblioteca ni se implementa web.
