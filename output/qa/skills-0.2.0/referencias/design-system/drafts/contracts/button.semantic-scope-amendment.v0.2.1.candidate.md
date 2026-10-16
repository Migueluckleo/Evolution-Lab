---
amendment_id: AMD-BUTTON-SEMANTIC-SCOPE-001
status: DRAFT
applies_to: BUTTON-001
base_contract_version: 0.2.0
base_contract_digest_sha256: 53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1
version: 0.2.1
affected_requirements: [REQ-BTN-004, AC-BTN-004]
decision_ref: DEC-SEMANTIC-EXTENSIONS-001
data_ref: sources/inventories/tokens.inventory.json
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-23
user_audit: PENDING
---

# Enmienda candidata de Button · texto Disabled con rol de texto

La auditoría retrospectiva exigida por el usuario detectó nueve `label-text` Disabled de Button que usan `color/icon/disabled` (`VariableID:13:24`), token con scope `SHAPE_FILL`. Para texto debe usarse `color/text/disabled` (`VariableID:13:30`), scope `TEXT_FILL`. Los dos roles aliasan la misma primitiva aprobada `color/neutral/400` (`VariableID:8:96`) en los cuatro modos: el cambio corrige semántica y picker sin alterar RGB, geometría, contenido o variantes. No se crea una variable nueva.

## Sustitución acotada de REQ-BTN-004

Solo en los nodos `26:279`, `26:283`, `26:287`, `26:291`, `26:295`, `26:299`, `26:303`, `26:307` y `26:323`, el fill de `label-text` debe vincularse por ID a `color/text/disabled`. Los iconos Disabled mantienen `color/icon/disabled`. Todos los demás requisitos, tokens, layouts, 60 variantes, propiedades y 23 reacciones de BUTTON-001 0.2.0 permanecen sin cambio.

## Sustitución acotada de AC-BTN-004

La lectura posterior debe confirmar el binding `VariableID:13:30` en los nueve textos citados, valores visuales idénticos al anterior en los cuatro modos, y cero pinturas de nodos TEXT vinculadas a roles `color/icon/*` o a un token cuyo scope excluya `TEXT_FILL` en las 60 variantes. Una captura debe confirmar que no se introdujo cambio visible inesperado. No se infiere bloqueo de eventos ni accesibilidad web desde la variante Disabled.

El contrato se ejecuta bajo la autorización de mejora semántica con auditoría humana posterior; no modifica el contrato publicado 0.2.0 ni atribuye aprobación humana del detalle.
