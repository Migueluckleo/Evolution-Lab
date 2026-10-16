# QA-TOGGLE-AMD-004 · revisión documental de Mixed

---
qa_id: QA-TOGGLE-AMD-004
review_type: CONTRACT_REVIEW
contract_ref: TOGGLE-001
amendment_ref: AMD-TOGGLE-MIXED-004
amendment_digest_sha256: f81bd14ba58ce0401904e09e79fb30c7ed498b4f67dd05335b037daa20e54af9
result: PASS
reviewed_on: 2026-09-24
user_audit: PENDING
---

| Control | Resultado | Evidencia |
|---|---|---|
| Fuente y alcance | PASS | PNG del usuario preservado 80×40 y regla verbal de agregado parcial; set anterior y destino identificados. |
| Matriz y propiedades | PASS | La enmienda añade `Mixed` al eje existente `Toggle`, deja `State` y las cuatro propiedades de etiquetas intactas; cuatro variantes nuevas, no combinaciones inventadas fuera de la matriz vigente. |
| Tokens | PASS | `color/icon/on-brand` y `color/icon/disabled` existen en el JSON aprobado, scope `SHAPE_FILL`, aliasados a `color/neutral/100` y `color/neutral/400`; IDs locales, scopes y aliases leídos en Figma antes de construir. |
| Semántica | PASS | Mixed representa selección parcial, no Disabled ni Off; clic y grupo vacío siguen `REQUIRES_DEFINITION` en el contrato de comportamiento. |
| Fidelidad | PASS | Pista 40×20 y guion 24×4 derivan del PNG 80×40 a escala 2; la pista azul usa los mismos bindings locales de On por estado. |
| Gate | PASS | Enmienda aditiva `DELEGATED_FOR_BUILD` para el destino ya construido, sin conflicto bloqueante para la representación visual. Auditoría humana pendiente. |

Este QA es documental; no afirma que las cuatro variantes existan aún en Figma. La validación de implementación se registra por separado.
