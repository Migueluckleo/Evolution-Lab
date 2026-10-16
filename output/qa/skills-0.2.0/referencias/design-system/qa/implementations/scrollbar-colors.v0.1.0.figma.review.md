# QA técnico · Foundations / Scrollbar colors 0.1.0

**Fecha:** 2026-09-24 · **Resultado histórico:** `PASS` técnico antes del cambio de color; `STALE` para estado actual desde [0.1.1](scrollbar-colors.v0.1.1.figma.review.md) · **Auditoría humana:** `PENDING` · **Publicación Figma:** `UNPUBLISHED`.

| Criterio | Evidencia leída de vuelta |
|---|---|
| Primitiva | `color/neutral/350`, `VariableID:327:122`, colección `primitive`, modo Value, RGB `195,198,212` (`#C3C6D4`), sin scope de interfaz. No existía primitiva local de ese RGB antes de la extensión. |
| Rol | `color/background/scrollbar/thumb`, `VariableID:327:123`, colección `semantic`, único scope `SHAPE_FILL`; cuatro modos aliasan la primitiva exacta. |
| JSON | [Extensión versionada](../../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json) registra nombres, descripciones únicas, IDs reales, tipos, modos, scopes y aliases coincidentes con la lectura Figma. El inventario histórico no se modificó. |
| Consumidores | Los 30 thumbs de cinco sets usan el rol semántico como fill. No se aplicó un token de texto, icono o borde a un shape. |

El gris fuente no se sustituyó por un valor similar de la escala previa. El contrato de componente conserva la inconsistencia nominal de `75%` para auditoría, independiente de la paridad cromática.
