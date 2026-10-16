---
amendment_id: AMD-FOUNDATIONS-FOCUS-EFFECTS-001
status: DELEGATED_FOR_BUILD
applies_to: FOUNDATIONS-TOKENS-001
base_contract_version: 0.1.0
base_contract_digest_sha256: e7362c364aa2c93a1a5bd50e0024d6b551f8ec6c6947bb62c6779ee25c1b7999
version: 0.1.2
decision_refs: [DEC-SEMANTIC-EXTENSIONS-001]
data_ref: drafts/foundations/ai-design-system.focus-effects.v0.1.0.json
data_digest_sha256: 0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4
base_data_ref: sources/inventories/tokens.inventory.json
base_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-23
user_audit: PENDING
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: QA de las variables de efecto y sus bindings, no igualdad del halo Toggle con la fuente. AUD-003 permanece abierto; conteos iniciales inferiores describen el momento de creación.
>
> Sustento: [QA documental 1](../../qa/contracts/foundations.focus-effects.amendment.v0.1.2.review.md); [QA técnico 1](../../qa/implementations/focus-effects.v0.1.0.figma.review.md), [QA técnico 2](../../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Enmienda candidata de Foundations · colores para efectos de foco

La [autorización de extensiones semánticas](../../registry/decisions.md) permite agregar roles de destino con alias a primitivas existentes, siempre que JSON, Figma y consumidores coincidan. El [JSON de extensión](../../drafts/foundations/ai-design-system.focus-effects.v0.1.0.json) gobierna exclusivamente nombre, tipo, `description`, scopes, código y valores por modo de estos dos roles. Esta enmienda no modifica el inventario histórico ni los 270 tokens de [FOUNDATIONS-TOKENS-001](foundations-tokens.contract.md); coexiste con la extensión de colores de control 0.1.1.

| ID | Requisito | Fuerza | Procedencia | Comprobación |
|---|---|---|---|---|
| REQ-TOK-FX-001 | Crear solo los dos roles de foco del JSON en la colección `semantic` local del destino, sin alterar las variables previas. | MUST | EXPLICIT autorización + OBSERVED error de scope en Toggle | AC-TOK-FX-001 |
| REQ-TOK-FX-002 | Conservar una `description` por rol, tipo `COLOR`, scope exclusivo `EFFECT_COLOR`, `codeSyntax: {}` y cuatro aliases al primitivo indicado. | MUST | DERIVED del JSON canónico y de la taxonomía de uso | AC-TOK-FX-002 |
| REQ-TOK-FX-003 | Registrar IDs reales, consumidor y lectura posterior JSON↔Figma sin atribuir aprobación humana al detalle propuesto. | MUST | EXPLICIT fidelidad entre fuentes y destino | AC-TOK-FX-003 |

El anillo exterior del Toggle Focus usa hoy el azul de `color/focus/ring`, pero ese rol tiene scope `STROKE_COLOR`. Su halo interior usa el blanco de `color/background/default`, cuyo scope es de fill. Como ambos se consumen en `effects[].color`, conservar sus variables actuales viola la regla semántica estricta aunque Figma acepte el binding. Los roles nuevos separan intención y picker de efecto sin crear valor primitivo ni cambiar el color visible. `color/focus/ring` y `color/background/default` conservan sus usos legítimos.

## Acceptance criteria

| ID | Resultado necesario |
|---|---|
| AC-TOK-FX-001 | La colección `semantic` contiene exactamente una variable de cada nombre nuevo; el conteo pasa de 131 a 133 y los roles anteriores conservan ID, scope y alias. |
| AC-TOK-FX-002 | Readback campo por campo de ambas variables iguala el JSON: nombre, tipo, única descripción, scope `EFFECT_COLOR`, código vacío y ocho aliases resolubles en cuatro modos a `color/blue/500` o `color/neutral/100` según corresponda. |
| AC-TOK-FX-003 | Estado, contrato y QA guardan los IDs reales; el Toggle Focus consume estos roles solo en los colores de sus cuatro efectos de anillo. Inventario fuente intacto y auditoría humana `PENDING`. |

Alcance Figma únicamente. No se crea estilo de efecto nuevo ni se modifica la geometría de las sombras; los demás efectos literales conservan su excepción documentada por no existir una categoría de geometría de sombra en el JSON aprobado.
