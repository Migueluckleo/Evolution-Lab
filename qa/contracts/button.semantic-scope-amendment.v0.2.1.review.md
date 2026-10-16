# QA-BUTTON-AMD-001 · revisión documental de scope Disabled

```yaml
qa_id: QA-BUTTON-AMD-001
review_type: CONTRACT_AMENDMENT_REVIEW
contract_ref: BUTTON-001
amendment_ref: AMD-BUTTON-SEMANTIC-SCOPE-001
candidate_digest_sha256: f0aa838ffe29f849b8f794584364e4e09349214fee8883f3e0d8f6008246d275
base_contract_digest_sha256: 53e13fa8e664f70d0ce81116e850bbcb0ab7da9f14ac0f08607fa5fda09894a1
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

Preflight read-only recorrió las 243 pinturas sólidas del set Button y localizó exactamente nueve textos Disabled con `color/icon/disabled`; los otros 51 textos pintados usan roles de texto. Ambos tokens Disabled existen en el JSON base y en Figma, con scopes distintos pero el mismo alias `color/neutral/400` en cuatro modos. La enmienda identifica nueve IDs reales, afecta solo REQ/AC-BTN-004 y no pide crear tokens ni alterar interacciones, iconos o variantes. La comprobación posterior exige cero usos `icon` en nodos TEXT y valores visuales preservados.

`PASS` documental habilita `DELEGATED_FOR_BUILD` bajo [DEC-SEMANTIC-EXTENSIONS-001](../../registry/decisions.md); no acredita aún la corrección Figma ni aprobación humana del detalle.
