# QA documental · Steps marca por tema 0.1.1

Estado: `PASS` para actualización delegada; auditoría humana `PENDING`. Fecha: 2026-09-24.

La solicitud posterior del usuario pide que Steps responda al color de marca del tema. La elección específica de marca base para el seleccionado `On White` y escala cromática 300 para los dos acentos `On Primary` se documenta como criterio delegado. La [enmienda de componente](../../specs/steps.brand-theme.amendment.v0.1.1.md) sustituye solo la tabla de color y `AC-ST-003`; conserva la estructura, contenido y anomalías del contrato base. [Foundations 0.1.21](../../specs/foundations.steps-brand.amendment.v0.1.21.md) delega al [JSON vigente](../../drafts/foundations/ai-design-system.steps-colors.v0.1.1.json) los siete roles con cuatro aliases cada uno, IDs reales y scope específico.

Las primitivas necesarias existen en el destino: base de marca blue/400, green/500, orange/500 y purple/500; tono contextual blue/300, green/300, orange/300 y purple/300. Los otros cuatro roles se conservan neutros/blancos. No se crea variable nueva, no se cambia una variable compartida y no se fuerza la unificación de los casos contradictorios de `On Primary`. El readback deberá verificar 28 aliases y todas las pinturas consumidoras. No hay conflicto documental bloqueante; `PASS` no es aprobación humana ni publicación.
