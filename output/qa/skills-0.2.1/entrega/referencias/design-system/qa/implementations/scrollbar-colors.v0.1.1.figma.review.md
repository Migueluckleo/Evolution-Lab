# QA técnico · Foundations / Scrollbar colors 0.1.1

**Fecha:** 2026-09-24 · **Resultado:** `PASS` técnico contra [Foundations 0.1.17](../../specs/foundations.scrollbar-colors.amendment.v0.1.17.md) · **Auditoría humana:** `PENDING` · **Biblioteca Figma:** `UNPUBLISHED`.

| Criterio | Evidencia de lectura posterior |
|---|---|
| Búsqueda | Entre primitivas locales previas a la extensión, `color/neutral/300` `#E2E8F0` fue la más cercana a `#C3C6D4` fuente por ΔE76=12.24; neutral/400 dio 14.73. La instrucción posterior del usuario prioriza reutilización. |
| Rol semántico | `color/background/scrollbar/thumb` conserva `VariableID:327:123`, tipo COLOR y único scope `SHAPE_FILL`; su `description` coincide con [JSON 0.1.1](../../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json). Cuatro modos aliasan `color/neutral/300` `VariableID:8:95`. |
| Primitiva obsoleta | `color/neutral/350` tenía cero aliases y cero consumidores directos antes de retirarla. Tras `remove()`, no aparece en `getLocalVariablesAsync`; una búsqueda directa por ID aún devolvió objeto en la sesión de la herramienta, por lo que la comprobación de membresía en la colección local se toma como evidencia de retirada activa. No se reintentó la eliminación. |
| Consumidores | Los 22 thumbs de sets internos y ocho thumbs de instancias públicas, 30/30 en total, conservan binding directo al rol semántico; ninguno consume la primitiva directamente. Scope y categoría son correctos. |
| Visual y contraste | Captura nueva confirma un thumb más claro que en la fuente. Sobre blanco, `#E2E8F0` da 1.23:1 frente a 1.70:1 del gris fuente; marcado `*` para revisión interna, sin certificar accesibilidad ni recolorear por contraste. |

El [QA 0.1.0](scrollbar-colors.v0.1.0.figma.review.md) queda histórico para el estado con primitiva nueva y no describe el Figma actual.
