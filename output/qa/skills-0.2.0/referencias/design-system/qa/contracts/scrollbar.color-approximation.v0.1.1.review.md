# QA documental · Scrollbar color 0.1.1

**Fecha:** 2026-09-24 · **Resultado:** `PASS` documental para cambio delegado acotado; QA Figma posterior obligatorio.

La instrucción posterior [DEC-MIGRATION-NEAREST-PRIMITIVE-001](../../registry/decisions.md) reemplaza para este caso la primitiva exacta creada antes. Se compararon todas las primitivas COLOR existentes del archivo destino mediante CIELAB ΔE76, excluyendo la primitiva nueva que se retirará: neutral/300 `#E2E8F0` obtuvo 12.24 y neutral/400 `#94A3B8` 14.73. El [JSON 0.1.1](../../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json) preserva el rol de fondo y cuatro aliases al ID real de neutral/300. [Enmienda de componente](../../specs/scrollbar.color-approximation.amendment.v0.1.1.md) y [Foundations 0.1.17](../../specs/foundations.scrollbar-colors.amendment.v0.1.17.md) acotan la sustitución sin cambiar geometría ni el inventario histórico.

La diferencia `#C3C6D4`→`#E2E8F0` es visible y se documenta; `PASS` documental no prueba aún que los 30 thumbs se actualizaran ni implica publicación o auditoría humana.
