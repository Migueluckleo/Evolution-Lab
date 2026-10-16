# Paso 4 · promoción documental a specs

Fecha: 2026-10-06 · Tipo: verificación administrativa de publicación documental · Resultado: **PASS para las 19 enmiendas enumeradas**, condicionado a la [verificación de archivos](specs-promotion.2026-10-06.verification.json). No es una nueva auditoría Figma ni cierre de familias con asuntos abiertos.

## Autoridad y criterio

Solicitud explícita: «Specs: promover las bases y enmiendas todavía en drafts cuando cierre el QA correspondiente». Se aplican [P03](../../protocols/03-CONTRACT-SYNTHESIS.md), [P05](../../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md), [P06](../../protocols/06-QA-AND-VALIDATION.md), DEC-MIGRATION-SPECS-AUDIT-001 y DEC-MIGRATION-SPECS-CANONICAL-001. Se consultó Graphify con vocabulario contracts/drafts/specs únicamente como índice y se leyeron contratos y QA originales para decidir elegibilidad. Su corte sigue STALE_AFTER_REFINEMENT.

No se promueve usando un PASS invalidado: se aplica el QA posterior al alcance sustituido. Las afirmaciones inferiores de creación, conteos y colores originales conservan su corte histórico; los avisos de vigencia remiten a sustituciones ya existentes, sin nuevos requisitos. DELEGATED_FOR_BUILD y user_audit PENDING se conservan. No aprobación humana simulada, publicación de biblioteca, código frontend, nuevo token ni mutación Figma.

## Enmiendas promovidas

Cada fila identifica la ubicación normativa única y sus QA documentales y técnicos. Los informes de QA existentes permanecen intactos; este reporte acredita el traslado, no atribuye nuevas lecturas al Figma actual.

| Ubicación canónica | QA documental existente | QA técnico existente |
|---|---|---|
| [foundations.breadcrumb-current-text.amendment.v0.1.0.md](../../specs/foundations/foundations.breadcrumb-current-text.amendment.v0.1.0.md) | [D1](foundations.breadcrumb-current-text.amendment.v0.1.0.review.md), [D2](six-family-color.v0.1.0.review.md) | [I1](../implementations/six-families.color.v0.1.0.review.md) |
| [foundations.chart-colors.amendment.v0.1.0.md](../../specs/foundations/foundations.chart-colors.amendment.v0.1.0.md) | [D1](charts.v0.1.0.review.md), [D2](six-family-color.v0.1.0.review.md) | [I1](../implementations/six-families.color.v0.1.0.review.md) |
| [foundations.linear-progress-colors.amendment.v0.1.0.md](../../specs/foundations/foundations.linear-progress-colors.amendment.v0.1.0.md) | [D1](foundations.linear-progress-colors.v0.1.0.review.md), [D2](six-family-color.v0.1.0.review.md) | [I1](../implementations/six-families.color.v0.1.0.review.md) |
| [foundations.metric-card-roles.amendment.v0.1.0.md](../../specs/foundations/foundations.metric-card-roles.amendment.v0.1.0.md) | [D1](foundations.metric-card-roles.amendment.v0.1.0.review.md), [D2](six-family-color.v0.1.0.review.md) | [I1](../implementations/six-families.color.v0.1.0.review.md) |
| [foundations.icon-button-backgrounds.amendment.v0.1.9.md](../../specs/foundations/foundations.icon-button-backgrounds.amendment.v0.1.9.md) | [D1](foundations.icon-button-backgrounds.amendment.v0.1.9.review.md) | [I1](../implementations/six-families.color.v0.1.0.review.md) |
| [foundations.avatar-roles.amendment.v0.1.6.md](../../specs/foundations/foundations.avatar-roles.amendment.v0.1.6.md) | [D1](foundations.avatar-roles.amendment.v0.1.6.review.md), [D2](avatar.source-color-amendment.v0.1.1.review.md) | [I1](../implementations/avatar-roles.v0.1.0.figma.review.md), [I2](../implementations/avatar.source-color.v0.1.1.figma.review.md) |
| [foundations.avatar-fallback-source-color.amendment.v0.1.11.md](../../specs/foundations/foundations.avatar-fallback-source-color.amendment.v0.1.11.md) | [D1](avatar.source-color-amendment.v0.1.1.review.md) | [I1](../implementations/avatar.source-color.v0.1.1.figma.review.md) |
| [foundations.control-colors.amendment.v0.1.1.md](../../specs/foundations/foundations.control-colors.amendment.v0.1.1.md) | [D1](foundations.control-colors.amendment.v0.1.1.review.md), [D2](selection-control-source-color.v0.1.1.review.md) | [I1](../implementations/control-colors.v0.1.0.figma.review.md), [I2](../implementations/selection-control-source-color.v0.1.1.figma.review.md), [I3](../implementations/radio-checkbox.refinement.v0.1.2.review.md) |
| [foundations.control-border-source-color.amendment.v0.1.12.md](../../specs/foundations/foundations.control-border-source-color.amendment.v0.1.12.md) | [D1](selection-control-source-color.v0.1.1.review.md) | [I1](../implementations/selection-control-source-color.v0.1.1.figma.review.md), [I2](../implementations/radio-checkbox.refinement.v0.1.2.review.md) |
| [foundations.dot-background-colors.amendment.v0.1.4.md](../../specs/foundations/foundations.dot-background-colors.amendment.v0.1.4.md) | [D1](foundations.dot-background-colors.amendment.v0.1.4.review.md) | [I1](../implementations/dot-background-colors.v0.1.0.figma.review.md) |
| [foundations.feedback-icon-scopes.amendment.v0.1.7.md](../../specs/foundations/foundations.feedback-icon-scopes.amendment.v0.1.7.md) | [D1](foundations.feedback-icon-scopes.amendment.v0.1.7.review.md) | [I1](../implementations/feedback-icon-scopes.v0.1.0.figma.review.md) |
| [foundations.focus-effects.amendment.v0.1.2.md](../../specs/foundations/foundations.focus-effects.amendment.v0.1.2.md) | [D1](foundations.focus-effects.amendment.v0.1.2.review.md) | [I1](../implementations/focus-effects.v0.1.0.figma.review.md), [I2](../implementations/radio-checkbox.refinement.v0.1.2.review.md) |
| [foundations.radio-indicator-colors.amendment.v0.1.3.md](../../specs/foundations/foundations.radio-indicator-colors.amendment.v0.1.3.md) | [D1](foundations.radio-indicator-colors.amendment.v0.1.3.review.md) | [I1](../implementations/radio-indicator-colors.v0.1.0.figma.review.md), [I2](../implementations/radio-checkbox.refinement.v0.1.2.review.md) |
| [button.semantic-scope-amendment.v0.2.1.md](../../specs/components/button.semantic-scope-amendment.v0.2.1.md) | [D1](button.semantic-scope-amendment.v0.2.1.review.md) | [I1](../implementations/button.semantic-scope.v0.2.1.figma.review.md), [I2](../implementations/six-families.color.v0.1.0.review.md) |
| [avatar.source-color-amendment.v0.1.1.md](../../specs/components/avatar.source-color-amendment.v0.1.1.md) | [D1](avatar.source-color-amendment.v0.1.1.review.md) | [I1](../implementations/avatar.source-color.v0.1.1.figma.review.md) |
| [toggle.visual-contrast-amendment.v0.1.2.md](../../specs/components/toggle.visual-contrast-amendment.v0.1.2.md) | [D1](toggle.visual-contrast-amendment.v0.1.2.review.md), [D2](toggle.source-color-amendment.v0.1.5.review.md) | [I1](../implementations/toggle.v0.1.2.figma.review.md), [I2](../implementations/toggle.source-color.v0.1.5.figma.review.md) |
| [toggle.focus-effect-amendment.v0.1.3.md](../../specs/components/toggle.focus-effect-amendment.v0.1.3.md) | [D1](toggle.focus-effect-amendment.v0.1.3.review.md) | [I1](../implementations/toggle.v0.1.3.figma.review.md), [I2](../implementations/toggle.source-color.v0.1.5.figma.review.md) |
| [toggle.mixed-amendment.v0.1.4.md](../../specs/components/toggle.mixed-amendment.v0.1.4.md) | [D1](toggle.mixed-amendment.v0.1.4.review.md) | [I1](../implementations/toggle.mixed.v0.1.4.figma.review.md) |
| [toggle.source-color-amendment.v0.1.5.md](../../specs/components/toggle.source-color-amendment.v0.1.5.md) | [D1](toggle.source-color-amendment.v0.1.5.review.md) | [I1](../implementations/toggle.source-color.v0.1.5.figma.review.md) |

## Sustituciones y cobertura

- Breadcrumb Current, Chart colors, Metric roles y Linear Progress: los campos afectados se rigen por [SIX-FAMILY-COLOR-001](../../specs/components/six-family-color.amendment.v0.1.0.md) y su JSON. No reaplicar orange/700, orange/600 ni oscurecimientos históricos por contraste.
- Control colors0.1.1: alias del borde sustituido por0.1.12; Toggle strokes por0.1.5. Hover conserva su definición. El QA Radio/Checkbox0.1.2 acredita los roles consumidos; no se reinicia su revisión.
- Avatar roles0.1.6: Servicios se rige por0.1.11. El QA de variables y el cambio cromático pueden publicarse sin declarar resuelta la tipografía de la base.
- Feedback scopes0.1.7: sustituye solo scopes. Warning source-color0.1.10 sigue gobernando sus aliases; no hay conflicto entre ambos alcances.
- Toggle0.1.2: conserva fills y correcciones de Hover/Disabled; sus dos strokes y umbral ya están sustituidos por0.1.5. Toggle0.1.3 acredita bindings de efecto, no identidad visual del halo. Mixed0.1.4 añade cuatro variantes y no decide clic/grupo vacío. Ninguna promoción cierra AUD-003 ni la revisión transversal del contrato base.
- Las definiciones de tokens de foco, indicador Radio y fondos Dot se publican con el QA de variables correspondiente, sin extenderlo a todos sus posibles consumidores.

## Bases que no se promueven en este paso

| Base | Evidencia y condición ya registrada |
|---|---|
| [Tooltip0.1.0](../../drafts/contracts/tooltip.contract.v0.1.0.md) | [QA transversal IN_PROGRESS](../implementations/tooltip.traceability.v0.1.0.review.md), AUD-004: interlineado/tracking. Falta cerrar o exceptuar el alcance afectado. |
| [Toggle0.1.0](../../drafts/contracts/toggle.contract.v0.1.0.md) | [QA acotado0.1.5](../implementations/toggle.source-color.v0.1.5.figma.review.md) no cierra el total; AUD-003 halo Focus y revisión transversal pendiente. Sus enmiendas cerradas sí están promovidas. |
| [Avatar0.1.0](../../drafts/contracts/avatar.contract.v0.1.0.md) | [QA cromático0.1.1](../implementations/avatar.source-color.v0.1.1.figma.review.md) no cierra tipografía; AUD-006 tamaños6/9→10/12. |
| [Logos0.1.0](../../drafts/contracts/logos.contract.v0.1.0.md) | [QA paso3](../implementations/logos.refinement.v0.1.1.review.md):57 deltas geométricos requieren aceptación explícita. Paso4 no la concede; doce assets siguen omitidos. |

No se crean tareas nuevas: son los asuntos existentes de la [auditoría por excepciones](../../specs/MIGRATION-AUDIT.md). Las bases de otras familias ya publicadas no se duplican ni se resintetizan.

## Historia que permanece en drafts

Candidatos (*.candidate.md), contratos fuente (*.source.component-contract.*), YAML de observación y borradores previos de Button/Filter Chip/Foundations se conservan como evidencia. Las bases aprobadas de estos últimos ya tienen ubicación canónica en specs; no se promueve de nuevo su candidato IN_REVIEW/DRAFT.

Enmiendas con recetas sustituidas: Badge contrast0.1.1, Dot inactive-border0.1.1 y Foundations Dot inactive-border0.1.5, Foundations Warning contrast0.1.8, Toggle contrast0.1.1. Permanecen como antecedentes de las sustituciones expresas, no como pendientes de construcción ni normas de color activas. Sus sucesoras ya están en specs. La identidad del rol que introdujeron se conserva a través de esas referencias.

## Integridad y trazabilidad

- Diecinueve originales archivados con sus bytes previos en archive/specs-promotion-2026-10-06/. Cada ruta previa en drafts es ahora un puntero, no un segundo contrato editable.
- Los contratos promovidos mantienen versión/ID/estado. Solo cambian ruta, enlaces administrativos y avisos explícitos de vigencia; el contenido normativo previo se conserva bajo sus sustituciones ya documentadas.
- Cuatro documentos que ya estaban en specs actualizan exclusivamente rutas de dependencias: Checkbox/Radio source-color0.1.1, Button local-bindings0.2.2 e Inline Notification0.1.0. Los digests históricos no se reescriben como si fueran actuales.
- Todos los JSON canónicos conservan bytes y ruta; no se duplican en specs. Los informes QA previos permanecen intactos. Hashes de originales, publicados, punteros, QA y datos protegidos en el [manifiesto](specs-promotion.2026-10-06.manifest.json).
- P-SLOTS: operación exclusivamente documental; no cambia anatomía, composición, cardinalidad ni bindings. Se conserva el alcance de la [matriz de Slots](../../registry/SLOTS-REVIEW-STATUS.md); esta promoción no simula nuevas pruebas de Slots.
- Se verifican enlaces locales, existencia de dependencias, estado delegado y auditoría pendiente; los cuatro contratos base bloqueados permanecen sin modificar.

## Continuación

Cierre de este paso administrativo: 19 enmiendas promovidas, cero bases bloqueadas promovidas y cero cambios Figma. Los únicos impedimentos documentales de las cuatro bases son los ya indicados. No repetir QA cerrado ni iniciar reconstrucciones por mover archivos. Graphify sigue STALE; su actualización es distinta de esta promoción y no se ejecutó aquí.
