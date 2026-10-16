# QA-TOGGLE-AMD-002 · revisión documental de fidelidad y contraste

```yaml
qa_id: QA-TOGGLE-AMD-002
review_type: CONTRACT_AMENDMENT_REVIEW
contract_ref: TOGGLE-001
amendment_ref: AMD-TOGGLE-VISUAL-CONTRAST-002
candidate_digest_sha256: 431752526d2defb4a043d569806c10d36d4566eecab5c1e9ba5a5657c8b1309a
base_contract_digest_sha256: c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38
extension_data_digest_sha256: 4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

La enmienda sustituye únicamente REQ-TGL-005/AC-TGL-005 para los tracks Off/Default, Off/Hover y Off/Focus y el thumb Off/Disabled, identificados por IDs reales y preflight de lectura posterior a la versión 0.1.1. El usuario priorizó fidelidad visual y autorizó tokens nuevos sincronizados con JSON y Figma, exigiendo scopes coherentes con fondos y bordes. La extensión de Foundations pasó [QA-TOKENS-EXT-001](foundations.control-colors.amendment.v0.1.1.review.md); su primitivo local y cuatro modos existen y los nombres nuevos no colisionan. `background/disabled` no se confunde con Off disponible. Los demás estados, propiedades y geometría permanecen expresamente fuera de la enmienda. La prueba fija previamente ≥3:1 en contorno o track de estados activos y obliga a captura posterior, sin permitir ajustar el umbral a posteriori.

`PASS` documental permite una implementación secuencial: primero crear y verificar la variable, luego actualizar los dos tracks y releer. No declara construida la corrección ni aprobada por el usuario.
