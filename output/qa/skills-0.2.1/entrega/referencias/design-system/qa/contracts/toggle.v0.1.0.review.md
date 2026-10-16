# QA-TOGGLE-001 · revisión documental 0.1.0

```yaml
qa_id: QA-TOGGLE-001
review_type: CONTRACT_REVIEW
contract_ref: TOGGLE-001
contract_version: 0.1.0
candidate_digest_sha256: 95bc256260c71c32158b7d2d62f29e1cbafdd90176859a7903afe9dcc321f123
evidence_model_digest_sha256: 4010c12aaae2784df134268f776a25f7cad1c26d4a6a09f35a1a9cb28fb320f0
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

| Control | Resultado | Evidencia o límite |
|---|---|---|
| DOC-01 | PASS | Set reutilizable Toggle, no plantilla Button. |
| DOC-02 | PASS | YAML parseado; 41/41 nodos, 24/24 variables, 8 combinaciones. MD de 17 secciones de evidencia y ocho REQ/AC. |
| DOC-03 | PASS | ID/key/página fuente, destino, versión y owner desconocido explícitos. |
| DOC-04 | PASS | Reglas de destino separadas de observaciones y normalizaciones delegadas. |
| DOC-05 | PASS | `defualt`, radio tipográfico, Off/Focus y sombra sin token declarados como anomalías/decisiones. |
| DOC-06 | PASS | No se importan valores o variantes de otra familia. |
| DOC-07 | PASS | Roles usados propuestos, focus ring y cinco tokens tipográficos/geométricos existen en JSON y destino; no se crean variables. |
| DOC-08 | PASS | JSON conserva descripciones canónicas; MD solo referencia roles. |
| DOC-09 | PASS | Matriz 2×4, cuatro propiedades no-variant y defaults consistentes. |
| DOC-10 | PASS | 40×20, thumb fraccional, gap8, stroke1, radio full; interlineado 16 frente a 15 fuente se declara. |
| DOC-11 | PASS | Etiquetas ocultas por defecto, textos independientes; no hay caso icon-only. |
| DOC-12 | PASS | Figma visual separado de semántica web y teclado. |
| DOC-13 | PASS | AC-TGL-001–008 enlazan REQ-TGL-001–008 uno a uno. |
| DOC-14 | PASS | Fuente y JSON sin modificación. |
| DOC-15 | PASS | Candidato DRAFT preservado; no se atribuye aprobación humana. |
| DOC-16 | PASS | Interacciones, hit target y accesibilidad funcional pendientes de producto; no bloquean representación estática especificada. |
| DOC-17 | PASS | Nombre de página `Toggles` funcional y exclusivo; no había página homónima en preflight. |
| DOC-18 | PASS | Mapa fuente/destino por rol e IDs; cuatro modos en JSON; corrección Off/Focus justificada por semántica además de alias. |

La captura fuente de 680×194 mostró ocho apariencias sin etiquetas visibles y foco con doble anillo. Las sombras internas/focus se describen como geometría observada; no se inventa categoría de token. La revisión habilita `DELEGATED_FOR_BUILD` por DEC-LEGACY-MIGRATION-DELEGATION-001, con `user_audit: PENDING`. No acredita construcción.
