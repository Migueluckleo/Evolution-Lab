# QA-TOGGLE-AMD-003 · revisión documental del foco

```yaml
qa_id: QA-TOGGLE-AMD-003
review_type: CONTRACT_AMENDMENT_REVIEW
amendment_ref: AMD-TOGGLE-FOCUS-EFFECT-003
candidate_digest_sha256: 61e7c3c4e3628f3be7bcb48b919d52d8d56c05af9b8c9349cdd31274dfcbe5df
extension_data_digest_sha256: 0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4
base_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

| Control | Resultado | Evidencia |
|---|---|---|
| DOC-03/04/05 | PASS | Delimita la sustitución a cuatro colores de efecto y separa observación, autorización y propuesta. |
| DOC-07/09/10 | PASS | Los dos tokens están definidos en JSON de destino con aliases a primitivas existentes; 0.1.2 mantiene autoridad para el contraste Off. |
| DOC-13/14/15 | PASS | AC-TGL-009/010 son medibles en Figma; el JSON histórico no cambia y la auditoría humana permanece pendiente. |

La inspección de `111:135` y `111:155` confirmó dos y cinco efectos respectivamente. Los primeros dos de cada nodo están ligados a roles con scopes `STROKE_COLOR` y fill; los dos roles propuestos preservan sus colores, geometría y orden. No hay conflicto documental bloqueante. `PASS` no implica QA de implementación.
