# QA Figma · borde de selección fiel a la fuente 0.1.1

**Fecha:** 2026-09-24 · **Resultado:** `PASS` técnico **acotado** al alias y a sus tres consumidores conocidos · **Auditoría humana:** `PENDING` · **Biblioteca:** `UNPUBLISHED`.

## Referencias vigentes

- [Regla transversal de trazabilidad](../../specs/MIGRATION-TOKEN-TRACEABILITY.contract.md); [JSON de override](../../drafts/foundations/ai-design-system.control-colors.v0.1.1.json), SHA-256 `921e7cc9e375dbf5a5317dfd974afc33d7477e09b65a8631a6863305896be683`.
- [Enmienda Foundations 0.1.12](../../drafts/contracts/foundations.control-border-source-color.amendment.v0.1.12.md), SHA-256 `260b16db658d073d9c0bb2fd522d669b0263487fdb47e56cdeadb53a5dd3ba2b`.
- [Checkbox 0.1.1](../../drafts/contracts/checkbox.source-color-amendment.v0.1.1.md), SHA-256 `00b2de0d4fd7aedd3a41c5123cb611ea0a3ed10b466c29495ab63d0861862475`; [Radio Button 0.1.1](../../drafts/contracts/radio-button.source-color-amendment.v0.1.1.md), SHA-256 `b8594caa29d2a8fbee73468e7c34a72e1d412064485018132156a8f4c36e23d1`.
- Fuente observada: Checkbox `1221:28710`, contornos Unselected Default/Focus `#94A3B8`; Radio Button `1230:24283`, anillo Off Default `#94A3B8`. El inventario histórico de tokens permanece intacto.

## Readback posterior a la escritura

| Control | Resultado leído del Figma destino `tj3WIBEZDGLVs7MJWKCwgf` |
|---|---|
| Rol | `color/border/control`, `VariableID:123:122`, tipo `COLOR`, scope exclusivo `STROKE_COLOR`; los modos `6:0`, `6:1`, `6:2`, `6:3` aliasan `color/neutral/400`, `VariableID:8:96`. |
| Primitiva | `color/neutral/400` conserva `#94A3B8` en modo `6:4`; no se creó variable nueva. |
| Checkbox | Página `Checkboxes` `149:122`; set `149:199` mantiene doce variantes. Los strokes `149:182` (Unselected Default) y `149:192` (Unselected Focus) mantienen binding a `VariableID:123:122` y `resolveForConsumer` da `#94A3B8`. |
| Radio Button | Página `Radio Buttons` `142:122`; set público `143:166` mantiene ocho variantes. El anillo `I143:148;142:137` (Selected=False, Default) mantiene el mismo binding y resuelve `#94A3B8`. |
| No regresión local | `color/background/control-hover`, `VariableID:123:123`, conserva scope `FRAME_FILL,SHAPE_FILL` y cuatro aliases a neutral/500. El set Toggle `111:163` conserva doce variantes y tiene **cero** strokes vinculados a `color/border/control`. |
| Vista | Capturas posteriores de ambos sets inspeccionadas: matriz, contornos, focos y otros estados visibles sin colapso ni alteración aparente. |

La comparación previa de todos los paints visibles de las doce variantes Checkbox y las ocho Radio Button encontró únicamente estos tres contornos cromáticamente desviados. Este cambio de alias restaura esos valores; no modifica nodos, propiedades, efectos, geometría ni tipografía. La limitación de contraste del gris original sobre blanco (~2.56:1) se conserva con `*` en [auditoría por excepciones](../../specs/MIGRATION-AUDIT.md), sin declarar conformidad WCAG.

**Límite:** este QA no reevalúa las normalizaciones de anatomía y tipografía de los contratos base ni audita consumidores del rol fuera de estas tres páginas. El resultado es técnico y acotado; publicación Figma y aprobación humana siguen pendientes.
