# QA · Conversation Composer0.1.2

Fecha2026-10-20. Contrato: [enmienda CCA0.1.2](../../specs/components/conversation.composer-action.amendment.v0.1.2.md). `IMPLEMENTATION_REVIEW: PASS` para el aviso y sus correcciones; Figma y web local `VALIDATED` en este alcance. `user_audit: NOT_REQUIRED`, `human_review_policy: OPTIONAL_NON_BLOCKING`. No certifica toda la familia ni aprobación/publicación de biblioteca.

| Control | Resultado y evidencia |
|---|---|
| CCA-01 identidad/API | PASS: principal765:397, página Conversation765:6; Show action=false gobierna1087:383. Button1087:399 sigue vinculado a26:102, default/small, texto Default y sin iconos. [Final](conversation-composer.v0.1.2.final.json). |
| CCA-02 reflow | PASS: aviso616/360, texto largo de seis repeticiones en instancia temporal; altura de texto228, mensaje245. [Pruebas](conversation-composer.v0.1.2.slots.json). Muestra normal: texto459/203px, gap efectivo8, alturas del mensaje49/74. |
| CCA-03/04 tokens | PASS: [23 variables cotejadas](../contracts/conversation-composer.v0.1.2.canonical-check.json); [bindings posteriores](conversation-composer.v0.1.2.readback.json), borde13:14. [Cuatro temas × dos anchos](conversation-composer.v0.1.2.themes.json) con aliases resueltos; ningún token creado. |
| CCA-05 tipografía | PASS: rangos `[0,42)` Caption/Semibold y `[42,72)` Caption/Regular, IDs y recetas persistidos en principal e instancia existente766:246. [Readback final](conversation-composer.v0.1.2.final.json); sin bindings incompatibles de tracking/interlineado por rango. |
| CCA-06 Slots | PASS: Draft/Tools siguen SLOT reales765:400/765:413, min/max null. En instancia vinculada: vacío, uno, muestra1/2, crecimiento4/5, reordenación y sustitución. Se retiraron originales solo en la copia QA; principales conservan1/2. [Pruebas](conversation-composer.v0.1.2.slots.json). |
| CCA-07 web | PASS: TypeScript, nueve tests existentes, build Next estático y prueba Chrome dedicada. Visibilidad off/on, borrador preservado al pulsar la acción, envío independiente, texto largo y cuatro temas ×616/360. [Resultado](../../output/qa/conversation-composer-2026-10-20/web-results.json). |
| CCA-08 evidencia | PASS técnico del componente: snapshots originales, enmienda, preflight, operaciones, final y hashes persistentes. Catálogo/skills/grafo se verifican separadamente al cierre P08/P05. |

## Revisión visual y ajustes

Se inspeccionó la [composición Figma final](../../output/qa/conversation-composer-2026-10-20/figma-final.png), con aviso visible a616 y360px, y el [web360](../../output/qa/conversation-composer-2026-10-20/web-360.png). Texto visible, botón separado, bordes y contenido sin recortes. La muestra web cambia disclaimer y etiqueta por datos de demostración; no se declara igualdad píxel a píxel entre esas muestras.

La primera prueba encontró que SPACE_BETWEEN eliminaba el gap efectivo cuando el texto usaba FILL. Se corrigió únicamente `primaryAxisAlignItems=MIN` del mensaje, preservando gap8 tokenizado; la [medición posterior](conversation-composer.v0.1.2.slots.json) confirma8px. La captura final corresponde a ese ajuste.

El agregado `boundVariables` seguía enumerando referencias métricas previas; `getRangeBoundVariable` ya devolvía null en ambos rangos. Se verificó y reaplicó el estilo completo; no se atribuye un defecto de render a ese agregado. [Evidencia](conversation-composer.v0.1.2.range-bindings.json).

El campo y los controles previos conservan sus reglas/limitaciones de contraste. El nuevo aviso utiliza fondo neutral y texto primario; no se altera la paleta para certificar WCAG. El rol de borde genérico sigue el tema del Composer, eliminando la dependencia accidental de Pagination.

## Ejecución, limpieza y límites

- `pnpm ds:generate`, `pnpm typecheck`, `pnpm test`: generación, tipos y9/9 pruebas PASS.
- `pnpm build`: PASS después de corregir un campo width duplicado en el test nuevo. El fallo inicial se conserva como antecedente, no como estado final.
- `pnpm exec playwright test tests/browser/conversation-composer.spec.ts`:1/1 PASS en Chrome. El sandbox bloqueó inicialmente el puerto local; la ejecución autorizada con revisión automática permitió el servidor temporal127.0.0.1. Sin instalación.
- `scripts/ds check --docs-only`: PASS documental; no equivale a cierre de grafo/skills.
- Todas las copias Figma de QA se retiraron; [final](conversation-composer.v0.1.2.final.json) confirma ausencia de1092:195. No se modificaron principales de Button/Pagination, Message/Response ni personajes.

El aviso permanece oculto por defecto. La fecha, texto y acción son contenido de muestra; no hay consulta de saldo, compra, renovación, bloqueo de envío ni backend. Los anchos probados no son breakpoints ni garantía universal. La evidencia no revalida consumidores fuera de este alcance.
