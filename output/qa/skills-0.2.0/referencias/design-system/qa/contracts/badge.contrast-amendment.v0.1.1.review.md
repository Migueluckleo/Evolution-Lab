# QA-BADGE-AMD-001 · revisión documental de contraste 0.1.1

```yaml
qa_id: QA-BADGE-AMD-001
review_type: CONTRACT_AMENDMENT_REVIEW
contract_ref: BADGE-001
amendment_ref: AMD-BADGE-CONTRAST-001
candidate_digest_sha256: c85abd212d654762afb491588d093211fde9531600558918e55e720c82d516b6
base_contract_digest_sha256: abc4e0e768be75831c343fe8e32322322e650ad437b7eae4860e498cbdc6f216
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

La enmienda identifica exactamente REQ-BDG-006/AC-BDG-006 del contrato delegado 0.1.0; no altera variantes, estructura, propiedades ni otras familias. El hallazgo [QA-BADGE-FIGMA-001](../implementations/badge.v0.1.0.contrast-finding.md) aporta la medición fallida antes del cambio. Los tres roles de reemplazo son variables semánticas locales existentes en el JSON aprobado y se verificó su alias en los cuatro modos. La predicción de contraste se calculó sin modificar Figma y el criterio posterior queda fijado antes de construir: texto normal ≥4.5:1 e iconos necesarios ≥3:1. La desviación visible frente a la fuente está declarada y no se presenta como aprobación humana.

Resultado documental `PASS` para ejecución delegada y readback posterior. Esta revisión no acredita el resultado visual ni el contraste final de Figma.
