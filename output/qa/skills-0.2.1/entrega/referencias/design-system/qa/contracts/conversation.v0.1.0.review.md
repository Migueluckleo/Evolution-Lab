# QA-CONVERSATION-DOC-001 · 2026-10-08

## Cierre documental vigente

[Contrato publicado en specs](../../specs/conversation.contract.v0.1.0.md), SHA256 `06818b9fdd3373ce1a93c217e2d2ce227a203b94bd92ae94927687efbb2e9796`. PASS documental y [técnico](../implementations/conversation.v0.1.0.review.md) acotados. Se precisaron Copy local, minChildren=null normalizado por Figma, dependencias normativas y excepción de nueve textos Count Small ocultos; no se amplían tokens ni comportamiento. Registro final40 roles/160 aliases frente a selección inicial36. DELEGATED_FOR_BUILD, auditoría PENDING, biblioteca UNPUBLISHED. El [candidato anterior a promoción](conversation.v0.1.0.pre-promotion.md) preserva bytes; drafts ahora es localizador. Los párrafos inferiores son el corte histórico previo a la construcción.

## QA previo a implementación · histórico

Corrección previa a la primera implementación: [candidato preservado](conversation.v0.1.0.prebuild-candidate.md), digest inicial d9c57540a6013081a9f8c62c25a04db001c1cc910e22e7c6248e9df658a38813. Dos operaciones fallidas no dejaron página ni estilos. La API rechaza isExposedInstance dentro de Slots y referencias de propiedades en subcapas de Slot. Se corrigió la especificación de propiedades: contenido Draft se edita directamente; controles internos también. Conserva los doce Slots y siete principales. DOC11/12 revalidados PASS para esa corrección; no se finge una propiedad Placeholder conectada. No era un contrato publicado ni implementación aceptada.

CONTRACT_REVIEW: PASS para el alcance visual homologado de CONVERSATION-001 v0.1.0. Autorización DEC-EXTERNAL-COMPONENTS-DELEGATION-001; no aprobación humana del diseño. Figma READY para construcción acotada; auditoría PENDING.

DOC01–06:21 secciones; familia externa y cuatro configuraciones explícitas; separación fuente observada/normalización delegada/comportamiento no implementado. DOC07–10/18:preflight vivo de36 roles, cuatro modos; script compara nombres/colección/aliases/valores/description/scopes contra JSON canónico sin discrepancias. No nuevas variables. DOC11–13: propiedades, doce Slots y criterios AC01–08 comprobables, límites de producto separados. DOC14–17: fuente intacta, sin aprobación simulada, página Conversation ausente en inventario vivo y autorización CREATE registrada. Se reutilizan principales98:128/183:311/26:81.

P-SLOTS documental PASS: regiones, contenido, operaciones, cardinalidad estructural0..n, muestras, layout y pruebas de instancia explícitos. Capacidad createSlot/slotSettings/slotContentId respaldada por typings y scripts previos del repositorio; la validación de esta implementación aún no se ha ejecutado.

La inspección fuente PARTIAL no se reclasifica: el contrato no depende de copiar sus componentProperties fallidas, sus destinos de animación ni backend. Diferencias cromáticas de agentes, badges, medidas y elevación se documentaron y anunciaron antes de escribir. QA técnico Figma todavía PENDING.
