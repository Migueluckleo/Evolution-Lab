---
amendment_id: AMD-CHECKBOX-SOURCE-COLOR-002
status: DELEGATED_FOR_BUILD
applies_to: CHECKBOX-001
base_contract_version: 0.1.0
base_contract_digest_sha256: bc189560b843aad787b5f17f38f51a60e4a2635955d111a176b9a5d81d2966bd
version: 0.1.1
supersedes_scope: Unselected Default and Focus stroke color and related contrast claim only
foundation_dependency: specs/foundations/foundations.control-border-source-color.amendment.v0.1.12.md
last_updated: 2026-09-24
user_audit: PENDING
---

> Ubicación canónica desde 2026-10-06. Aplicar la [enmienda de refinamiento 0.1.2](components/radio-checkbox.refinement.amendment.v0.1.2.md) y el [QA vigente](../qa/implementations/radio-checkbox.refinement.v0.1.2.review.md). Las cláusulas históricas sustituidas no son requisitos actuales. DELEGATED_FOR_BUILD; auditoría humana PENDING.


# Checkbox · contorno Unselected de origen 0.1.1

En `Selection=Unselected`, `State=Default` y `State=Focus`, los strokes `149:182` y `149:192` conservan binding a `color/border/control` `VariableID:123:122`, `STROKE_COLOR`, pero resuelven `#94A3B8` por el [override Foundations 0.1.12](foundations/foundations.control-border-source-color.amendment.v0.1.12.md), como la fuente. No se cambia el fill de las ocho variantes Selected/Indeterminate ni los bordes Hover/Disabled. La limitación de contorno neutral/400 sobre blanco (~2.56:1) queda `*`; ninguna mejora de contraste justifica recolorear silenciosamente.

`AC-CHK-008`: comparar doce variantes y sus paints visibles con el color fuente tras el override. `AC-CHK-009`: confirmar dos consumidores de borde y aliases en cuatro modos sin cambiar propiedades, iconos, textos, geometría o efectos de foco. Auditoría humana pendiente; set sin publicar.
