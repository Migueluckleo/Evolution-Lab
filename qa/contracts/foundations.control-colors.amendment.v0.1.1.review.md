# QA-TOKENS-EXT-001 · revisión documental de colores para controles

```yaml
qa_id: QA-TOKENS-EXT-001
review_type: CONTRACT_AMENDMENT_REVIEW
contract_ref: FOUNDATIONS-TOKENS-001
amendment_ref: AMD-FOUNDATIONS-CONTROL-COLORS-001
candidate_digest_sha256: 41ef13f113e0b9f9c892acbceab84938f2d47dc4ecb468448ac1bfebeef59f76
extension_data_digest_sha256: 4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839
base_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

El usuario autorizó explícitamente agregar las variables necesarias y pidió correspondencia entre JSON, contratos y Figma, vinculándolas a primitivas existentes y anunciando los cambios. El JSON de extensión es válido: contiene dos variables semánticas `COLOR`, cada una con una sola `description`, scopes propios de borde o fondo, cuatro aliases al mismo primitivo local y ningún campo `usage` paralelo. La colección, cuatro IDs de modo y primitivo `color/neutral/500` (`VariableID:8:97`) se leyeron en el destino; no existen duplicados de `color/border/control` ni `color/background/control-hover`. El primitivo conserva el gris #64748b y el inventario fuente mantiene su SHA-256 aprobado. El contrato separa la extensión del snapshot histórico y fija tres requisitos con aceptación verificable. No hay conflicto documental pendiente para esta extensión acotada.

`PASS` autoriza pasar a `DELEGATED_FOR_BUILD` bajo la autorización concreta de ampliación; no certifica todavía las variables Figma ni atribuye aprobación humana del detalle.
