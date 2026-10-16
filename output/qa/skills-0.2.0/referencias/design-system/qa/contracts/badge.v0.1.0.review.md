# QA-BADGE-001 · revisión documental 0.1.0

```yaml
qa_id: QA-BADGE-001
review_type: CONTRACT_REVIEW
contract_ref: BADGE-001
contract_version: 0.1.0
candidate_digest_sha256: 388812c1028c1dfaedda1a885b7043fec25e36a7ef7bf23411b513bd64b84830
evidence_model_digest_sha256: b087af4f17a478f136e3bb50e3c4a5eaa3b9c789deb1325310c6a669f879087b
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

| Control | Resultado | Evidencia o límite |
|---|---|---|
| DOC-01 | PASS | Set reutilizable `badge` con seis variantes Type; contrato de componente. |
| DOC-02 | PASS | YAML parseado con Ruby, invariantes 37 nodos/seis variantes; MD con 21 secciones. |
| DOC-03 | PASS | ID/key, página, archivo fuente, versión, destino y owner desconocido explícitos. |
| DOC-04 | PASS | Ocho REQ con fuerza, procedencia y AC trazables. |
| DOC-05 | PASS | Se separan hechos de fuente, decisiones de mapeo y conducta no observada. |
| DOC-06 | PASS | No se importan variantes o valores de la plantilla Button. |
| DOC-07 | PASS | Los 26 roles visualmente aplicables existen en el JSON y en la colección semantic local; un binding de font/size/lg en padding del set se conserva como anomalía no visual. |
| DOC-08 | PASS | El JSON conserva las descripciones canónicas; el contrato solo referencia nombres/roles. |
| DOC-09 | PASS | Seis apariencias, dos booleans, dos swaps y una TEXT consistentes con el set fuente; no se inventan estados. |
| DOC-10 | PASS | Padding/gap/radio/stroke apuntan a tokens locales existentes y medidas fuente explícitas. |
| DOC-11 | PASS | Defaults base/Light/left true/right false/Icon Presentation reflejan la lectura; no se confunde oculto con ausente. |
| DOC-12 | PASS | Figma visual separado de API web, teclado y semántica de producto. |
| DOC-13 | PASS | AC-BDG-001–008 enlazan uno a uno a REQ-BDG-001–008. |
| DOC-14 | PASS | Fuente y JSON sin modificación. |
| DOC-15 | PASS | Candidato DRAFT preservado; decisión delegada no se atribuye como aprobación humana. |
| DOC-16 | PASS | Interacción y accesibilidad funcional quedan fuera del set; preferidos de iconos e importación se verificarán en destino. |
| DOC-17 | PASS | `Badges` es nombre funcional de página, sin colisión en el destino preflight. |
| DOC-18 | PASS | Roles por Type referencian el JSON y los IDs locales; border/disabled→strong y text→icon para iconos derechos se declaran decisiones, no equivalencias silenciosas. |

La captura fuente de 104×429 se inspeccionó inline y mostró seis badges con icono izquierdo. La key de Presentation coincidió con la búsqueda de `Phosphor Icons`; no se inspeccionó todo el catálogo de 1512 iconos. La revisión habilita `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001, con `user_audit: PENDING`. No acredita implementación.
