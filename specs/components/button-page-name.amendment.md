---
amendment_id: AMD-BUTTON-PAGE-001
status: APPROVED
applies_to: BUTTON-001
contract_version: 0.1.0
affected_requirements:
  - REQ-BTN-007
  - AC-BTN-007
decision_ref: DEC-BUTTON-PAGE-001
last_updated: 2026-09-23
---

# Enmienda aprobada: página de Buttons

El usuario decidió que la página exclusiva de la familia Button se llame exactamente `Buttons`. Esta enmienda resuelve únicamente el nombre pendiente en `REQ-BTN-007` y su comprobación `AC-BTN-007` del [contrato aprobado](button.contract.md). Todos los demás requisitos, dependencias y límites de `BUTTON-001` versión `0.1.0` permanecen intactos.

El preflight observó una sola página `Page 1` (`0:1`) con un único nodo superior: el component set `button` (`26:81`). La operación autorizada para cumplir la regla de página exclusiva es renombrar esa página a `Buttons`, conservando el mismo page ID y el mismo component set ID. No se creará una segunda página ni se moverán o duplicarán nodos.

## Aceptación

`AC-BTN-007` pasa si el readback confirma una página llamada exactamente `Buttons`, con page ID `0:1`, que contiene como único nodo superior el set `26:81` y no mezcla otra familia. El renombrado no acredita los demás criterios: el QA de implementación debe leer el resultado después de la escritura.
