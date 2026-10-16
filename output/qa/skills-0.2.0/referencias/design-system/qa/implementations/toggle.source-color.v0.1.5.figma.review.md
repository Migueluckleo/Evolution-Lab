# QA Figma · Toggle · restauración acotada de color 0.1.5

**Resultado:** `PASS` para `AC-TGL-015–016` (dos strokes Off); **estado de la familia completa:** `IN_PROGRESS`, no `PASS` cromático global. **Fecha:** 2026-09-24. `user_audit: PENDING`; set `UNPUBLISHED`.

## Readback posterior

- AI Design System conserva página `Toggles` `111:122`, un set `Toggle` `111:163` y doce variantes. Se preservaron los ocho IDs heredados y las cuatro variantes Mixed.
- Solo cambiaron los tracks `111:145` (Off/Default) y `111:155` (Off/Focus). Ambos strokes son `#E2E8F0`, vinculados a `color/border/strong` `VariableID:13:15`. La variable tiene scope `STROKE_COLOR` y cuatro aliases a `color/neutral/300` `VariableID:8:95`. Ambos fills permanecen `#E2E8F0` y ligados a `color/background/muted` `VariableID:13:37`.
- Se creó cero variables y no se modificó el JSON aprobado. La captura posterior del set mostró ambos Off con pista y borde pálidos; los estados On, Hover, Disabled y Mixed siguen visibles.
- El contorno/fondo neutral/300 contra blanco tiene aproximadamente 1.23:1. Se conserva por fidelidad y se marca `*` en la auditoría interna; no se afirma conformidad WCAG.

## Barrido cromático de las ocho variantes heredadas

Lectura read-only de los sets fuente `1230:23858` y destino `111:163`, comparando fills, strokes y efectos visibles por estado. Tras esta corrección, **todos los fills y strokes sólidos de las ocho variantes heredadas coinciden en RGB con la fuente**. En On/Focus y Off/Focus, el efecto exterior conserva `#1D21B0`, pero el halo interior fuente es el literal `#F8FAFC` y el destino muestra `#FFFFFF` mediante `color/focus/effect-inner` `VariableID:136:123`. La diferencia ya estaba anotada en 0.1.3 y ahora queda como excepción de fidelidad: no existe primitiva `#F8FAFC` exacta en el inventario aprobado. No se cambia la variable compartida ni se inventa una primitiva. Véase [auditoría](../../specs/MIGRATION-AUDIT.md).

Las sombras internas negras se observaron en fuente y destino; esta revisión no vuelve a certificar su geometría ni todos los bindings tipográficos. Las cuatro variantes Mixed provienen del PNG del usuario y conservan el [QA técnico propio](toggle.mixed.v0.1.4.figma.review.md); no se atribuyen a la fuente antigua.

## Alcance del veredicto

`AC-TGL-015` PASS: dos bindings correctos, alias por modo, fills e IDs conservados. `AC-TGL-016` PASS: color fuente mantenido y limitación señalada. El umbral ≥3:1 de 0.1.2 queda `SUPERSEDED` **solo** para esos dos bordes. El QA 0.1.2/0.1.3 sigue histórico en sus demás alcances, pero su afirmación de fidelidad cromática total no queda vigente tras el hallazgo del halo. La promoción del contrato Toggle completo a `specs/` espera cerrar o exceptuar formalmente ese punto y completar la revisión transversal.
