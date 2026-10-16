---
amendment_id: AMD-DOT-SOURCE-COLOR-002
status: DELEGATED_FOR_BUILD
applies_to: DOT-001
base_contract_version: 0.1.0
base_contract_digest_sha256: 31bc2874b34be08187163584701fc8a1be0d66b0479fadd304d81fa67ca2bc77
version: 0.1.2
supersedes_scope: AMD-DOT-INACTIVE-BORDER-001 0.1.1 only for Inactive stroke color and contrast claim
foundation_dependency: specs/foundations/foundations.dot-inactive-border-source-color.amendment.v0.1.6.md
last_updated: 2026-09-24
user_audit: PENDING
---

# Dot · restauración del borde Inactive 0.1.2

Las tres variantes Inactive de la [fuente Dot](../../drafts/contracts/dot.source.component-contract.md) muestran borde blanco. La [enmienda 0.1.1](../../drafts/contracts/dot.inactive-border-amendment.v0.1.1.md) lo cambió a neutral/500 por contraste; la decisión posterior de fidelidad cromática sustituye solo ese ajuste. `Type=Inactive` en Small, Medium y Large conserva su fill neutral/300 y su binding `color/border/status-inactive` `VariableID:157:122`, `STROKE_COLOR`; la [dependencia Foundations 0.1.6](../foundations/foundations.dot-inactive-border-source-color.amendment.v0.1.6.md) restaura el alias a neutral/100 `#FFFFFF` en los cuatro modos. No se cambia el token compartido `color/border/on-brand`, ni estructura, textos, propiedades o las demás doce variantes.

`AC-DOT-007`: los 36 paints visibles de las quince variantes conservan RGB de la fuente, incluidas las tres variantes Inactive. `AC-DOT-008`: los siete roles usados por Dot mantienen categoría/scope semánticos y aliases registrados en JSON aprobado/extensiones vigentes. `AC-DOT-009`: la limitación Inactive se marca `*` en la auditoría sin alterar el color ni afirmar conformidad accesible. `DELEGATED_FOR_BUILD` no es aprobación humana; el set permanece sin publicar.
