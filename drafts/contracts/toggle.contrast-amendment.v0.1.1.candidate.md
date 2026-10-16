---
amendment_id: AMD-TOGGLE-CONTRAST-001
status: DRAFT
applies_to: TOGGLE-001
base_contract_version: 0.1.0
base_contract_digest_sha256: c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38
version: 0.1.1
affected_requirements: [REQ-TGL-005, AC-TGL-005]
decision_ref: DEC-TOGGLE-CONTRAST-001
data_ref: sources/inventories/tokens.inventory.json
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-23
user_audit: PENDING
---

# Enmienda candidata 0.1.1 · contraste del Toggle apagado

La matriz del contrato base reproduce los fondos apagados claros de la fuente. La medición posterior a la construcción [QA-TOGGLE-FIGMA-001](../../qa/implementations/toggle.v0.1.0.contrast-finding.md) observó solo 1.23:1 en Off/Default y Off/Focus contra la superficie blanca. [WCAG 2.2 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) usa 3:1 como referencia para la información visual necesaria de controles. Esta medición del color estático no certifica un producto.

## Sustitución acotada de REQ-TGL-005

El fill de los tracks `Toggle=Off, State=Default` (`111:145`) y `Toggle=Off, State=Focus` (`111:155`) usará la variable local semántica existente `color/background/inverse` (`VariableID:13:39`) en lugar de `color/background/muted` (`VariableID:13:37`). Strokes, thumbs, labels, propiedades, otros seis tracks y geometría no cambian. El rol inverse es una superficie neutral oscura y permite distinguir la apariencia Off del On de marca sin inventar una variable. Es una desviación visual clara frente a la fuente y queda para auditoría del usuario.

La comparación read-only predice 14.63:1 para track oscuro contra superficie blanca en los cuatro modos; Off/Hover conserva 4.76:1 y el ring focus 11.07:1. Los modos, aliases y valores proceden del JSON aprobado. La revisión posterior a la escritura debe medirlos de nuevo; no se reajusta la tolerancia después.

## Sustitución acotada de AC-TGL-005

`AC-TGL-005` pasa solo si los dos nodos citados contienen el binding `VariableID:13:39`, todos los demás bindings del contrato base siguen intactos y cada apariencia activa comunica el control con contraste estático ≥3:1 en los cuatro modos. Disabled no se usa para justificar un fallo activo. Un valor inferior es `FAIL`.

Los demás REQ/AC de TOGGLE-001 0.1.0 permanecen intactos. La enmienda no atribuye aprobación humana ni publicación de biblioteca.
