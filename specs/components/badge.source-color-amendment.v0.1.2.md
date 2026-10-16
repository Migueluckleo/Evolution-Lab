---
amendment_id: AMD-BADGE-SOURCE-COLOR-002
status: DELEGATED_FOR_BUILD
applies_to: BADGE-001
base_contract_version: 0.1.0
base_contract_digest_sha256: 886fd8376f440063532a526825287e030918bf9092d827108ca58a49596e4b0b
version: 0.1.2
supersedes_scope: AMD-BADGE-CONTRAST-001 REQ-BDG-006/AC-BDG-006 only for Informational text and Warning text/icon colors and their contrast thresholds
decision_refs: [DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-CONTRAST-LIMITATIONS-001, DEC-MIGRATION-TRACEABILITY-001]
source_data_ref: sources/inventories/tokens.inventory.json
source_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
foundation_dependency: specs/foundations/foundations.warning-icon-source-color.amendment.v0.1.10.md
last_updated: 2026-09-24
user_audit: PENDING
---

# Badge · restauración de colores fuente 0.1.2

La [enmienda de contraste 0.1.1](../../drafts/contracts/badge.contrast-amendment.v0.1.1.md) sustituyó por negro el texto Informational y el texto/icono Warning. La lectura actual de las seis variantes fuente y destino confirma que esos son los únicos RGB visibles desviados; los fondos y Base/Light/Error/Success ya coinciden. La decisión posterior del usuario restaura los colores fuente y conserva las limitaciones de contraste para revisión interna.

| Consumidor | Fuente observada | Binding destino requerido |
|---|---|---|
| Informational · texto `97:185` | `#007FC8` | `color/feedback/information/text` `VariableID:13:54`, `TEXT_FILL` |
| Warning · texto `97:191` | `#C97B00` | `color/feedback/warning/text` `VariableID:13:46`, `TEXT_FILL` |
| Warning · vectores de icono izquierdo `I97:189;8899:60223` y derecho opcional `I97:192;8899:60223` | `#C97B00` | `color/feedback/warning/icon` `VariableID:13:48`, `SHAPE_FILL`, tras [restaurar su alias compartido](../foundations/foundations.warning-icon-source-color.amendment.v0.1.10.md) |

El vector derecho está dentro de una instancia oculta por defecto, pero se reconecta para que al activar la propiedad no reaparezca el color incorrecto. Los roles de texto/información y texto/warning ya aliasan las primitivas originales en los cuatro modos. El rol de icono Warning es compartido con Inline Notifications, por lo que su cambio de alias se versiona en Foundations y se verifica **antes** de reconectar Badge. No se crean tokens ni se alteran geometría, propiedades, demás variantes o contenido.

| ID | Requisito | Comprobación |
|---|---|---|
| REQ-BDG-007 | Reconectar los cuatro paints indicados a sus roles semánticos correctos, conservando el RGB de origen en los cuatro modos. | AC-BDG-007 |
| REQ-BDG-008 | Conservar y señalar con `*` el contraste original de texto Informational (~3.61:1) y texto/icono Warning (~2.96:1) sobre sus fondos; no exigir recoloración para declarar fidelidad. | AC-BDG-008 |

`AC-BDG-007` exige readback de los cuatro IDs de nodo, roles, scopes y aliases por modo, sin alterar los demás bindings y con seis variantes/IDs preservados. `AC-BDG-008` exige medición y marca documental, no asterisco dibujado sobre Figma. La enmienda no certifica accesibilidad, no publica biblioteca y deja `user_audit: PENDING`. [QA documental](../../qa/contracts/badge.source-color-amendment.v0.1.2.review.md) `PASS` para construir tras la dependencia de Foundations.
