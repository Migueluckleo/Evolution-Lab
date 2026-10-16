---
amendment_id: AMD-FOUNDATIONS-RADIO-INDICATOR-COLORS-001
status: DELEGATED_FOR_BUILD
applies_to: FOUNDATIONS-TOKENS-001
base_contract_version: 0.1.0
base_contract_digest_sha256: e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999
version: 0.1.3
decision_refs: [DEC-SEMANTIC-EXTENSIONS-001]
data_ref: drafts/foundations/ai-design-system.radio-indicator-colors.v0.1.0.json
data_digest_sha256: 46f53dc329a93374f486ad26452cdd991c6cb0651a6c068865e34352d8e6161a
base_data_ref: sources/inventories/tokens.inventory.json
base_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-23
user_audit: PENDING
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: Los roles y aliases fueron revalidados en el cierre de Radio/Checkbox. Conteos de colección inferiores son históricos, no un límite actual.
>
> Sustento: [QA documental 1](../../qa/contracts/foundations.radio-indicator-colors.amendment.v0.1.3.review.md); [QA técnico 1](../../qa/implementations/radio-indicator-colors.v0.1.0.figma.review.md), [QA técnico 2](../../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Enmienda candidata de Foundations · rellenos para indicador de selección

La [extensión JSON del destino](../../drafts/foundations/ai-design-system.radio-indicator-colors.v0.1.0.json) es la única fuente editable de nombre, tipo, descripción, scope y aliases de dos colores para geometría de indicador seleccionado. No altera el inventario histórico de la Librería ni las extensiones previas de control y foco. Esta enmienda gobierna su uso en Figma bajo la autorización de extensiones semánticas del usuario.

| ID | Requisito | Fuerza | Procedencia | QA |
|---|---|---|---|---|
| REQ-TOK-RAD-001 | Añadir los dos roles del JSON a `semantic`, sin duplicados ni cambios en variables anteriores. | MUST | EXPLICIT autorización; DERIVED de la composición del indicador On | AC-TOK-RAD-001 |
| REQ-TOK-RAD-002 | Cada rol tiene una sola `description`, `COLOR`, scope exclusivo `SHAPE_FILL`, código vacío y cuatro aliases a primitivas existentes conforme al JSON. | MUST | EXPLICIT semántica/scope y JSON ↔ Figma fieles | AC-TOK-RAD-002 |
| REQ-TOK-RAD-003 | Usar estos roles solo en fills del indicador de selección normal y hover; no como texto, icono, stroke ni efecto. | MUST | DERIVED de uso exacto requerido | AC-TOK-RAD-003 |

El contorno seleccionado de 5 px de la fuente no tiene primitiva de grosor equivalente en Foundations. Para mantener su apariencia sin crear grosor primitivo, el destino propone un disco exterior de 18 px y un centro blanco de 8 px, ambos fills semánticos. Los tokens existentes `color/interactive/primary/*` comparten varias primitivas pero describen superficies de acción, no selección; `color/background/brand` es deliberadamente tenue. Los dos roles nuevos aliasan los mismos primitivos de `color/border/brand` y `color/border/hover` en cada modo, con scope de **fill de forma**; no amplían aquellos roles de stroke. En estado Disabled se reutiliza `color/background/disabled` y no se crea token adicional.

## Acceptance criteria

| ID | Resultado necesario |
|---|---|
| AC-TOK-RAD-001 | Colección `semantic` pasa de 133 a 135 variables; cada nombre nuevo aparece exactamente una vez y los roles previos mantienen ID/alias/scope. |
| AC-TOK-RAD-002 | Readback iguala JSON en nombre, tipo, descripción, scope, código y ocho aliases por cuatro modos, resolviendo cada ID al primitivo nombrado. |
| AC-TOK-RAD-003 | Inspección del consumidor Radio Button verifica que solo los discos On normal/hover consumen los nuevos tokens como `SHAPE_FILL`; ningún stroke, texto o efecto los consume. |

Figma es el único destino autorizado; publicación y frontend no quedan implicados. Auditoría humana del detalle pendiente.
