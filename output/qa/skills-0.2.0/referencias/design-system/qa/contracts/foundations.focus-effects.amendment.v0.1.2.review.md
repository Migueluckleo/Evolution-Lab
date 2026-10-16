# QA-TOKENS-FOCUS-001 · revisión documental

```yaml
qa_id: QA-TOKENS-FOCUS-001
review_type: CONTRACT_AMENDMENT_REVIEW
amendment_ref: AMD-FOUNDATIONS-FOCUS-EFFECTS-001
candidate_digest_sha256: da5437fb7406e9761636240f703baae663012a8d91d806acb0b2a990056e2fdf
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
| DOC-02/03/04 | PASS | Frontmatter legible, identidad/versiones/digests, tres requisitos y criterios enlazados. |
| DOC-05/07/08 | PASS | Se distingue autorización explícita del usuario de la solución derivada; JSON válido con una sola `description` por token, sin `usage`; ocho aliases completos. |
| DOC-09/10/14 | PASS | Scope exclusivo `EFFECT_COLOR`; `color/blue/500` y `color/neutral/100` existen en el destino con IDs indicados; inventario fuente conserva digest. |
| DOC-15/16/18 | PASS | `DELEGATED_FOR_BUILD` solo después de esta revisión; auditoría humana pendiente; alcance Figma y binding por ID verificables. |

La lectura previa confirmó colección `semantic`, cuatro modos e IDs primitivos. No existe en el destino un rol `color/focus/*` con scope `EFFECT_COLOR`. La enmienda añade roles de efecto sin abrir scopes de borde o fondo ni crear valores cromáticos. `PASS` habilita la ejecución delegada, no acredita todavía variables creadas ni aprobación humana de los nombres.
