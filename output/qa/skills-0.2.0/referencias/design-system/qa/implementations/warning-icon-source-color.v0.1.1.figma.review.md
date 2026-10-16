# QA Figma · Warning icon · color de origen

**Resultado:** `PASS` técnico para `AC-TOK-WARN-001–002`; **fecha:** 2026-09-24. `user_audit: PENDING`.

- El [JSON de override vigente](../../drafts/foundations/ai-design-system.warning-icon-contrast.v0.1.1.json) exige alias de `color/feedback/warning/icon` a `color/amber/600` en Contable, Administrativo, Servicios y Personas. Readback de la variable local `VariableID:13:48` confirmó cuatro aliases a `VariableID:8:108`, nombre, `COLOR`, scope exclusivo `SHAPE_FILL`, `codeSyntax: {}` y descripción sin cambios. La primitiva local resuelve `#C97B00`, como el JSON base; no se creó variable.
- El vector Warning existente de Inline Notifications `I175:417;8899:88650` mantuvo el binding a ese rol y ahora resuelve `#C97B00`. El fondo warning `#FDF2C8` no cambió. El par original calcula 2.96:1; queda marcado `*` para revisión interna, no recoloreado ni certificado como conforme.
- La modificación fue solo a la variable compartida. Badge se revalidó como consumidor nuevo por separado. El override 0.1.0 amber/700 y su QA se conservan como historial `SUPERSEDED` en los cuatro aliases.

Esta revisión no vuelve a certificar toda Inline Notifications ni publica la biblioteca.
