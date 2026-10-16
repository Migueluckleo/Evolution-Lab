# QA-TOGGLE-FIGMA-007 · valor Mixed

---
qa_id: QA-TOGGLE-FIGMA-007
review_type: IMPLEMENTATION_REVIEW
implementation_ref: IMP-TOGGLE-MIXED-FIGMA-001
amendment_ref: AMD-TOGGLE-MIXED-004
result: PASS
reviewed_on: 2026-09-24
user_audit: PENDING
publish_status: UNPUBLISHED
---

| Criterio | Resultado | Evidencia de lectura posterior |
|---|---|---|
| AC-TGL-011 | PASS | `Toggles` conserva el set `Toggle`; 12 nombres únicos, 8 IDs previos intactos y 6 definiciones de propiedad. `Toggle={On,Off,Mixed}`; `State` conserva 4 valores. |
| AC-TGL-012 | PASS | Cuatro componentes Mixed 40×20; guiones 24×4 en (8,8), sin thumb. Foco conserva los dos efectos locales. Captura de set 704×380 y página 704×489 revisadas visualmente; no hay recortes aparentes. |
| AC-TGL-013 | PASS | Guiones Default/Hover/Focus ligados a `color/icon/on-brand` y Disabled a `color/icon/disabled`; ambos `SHAPE_FILL`, con aliases locales en cuatro modos. Radios ligados a `radius/full` con `CORNER_RADIUS`. Pistas, bordes y 48 propiedades tipográficas siguen ligados a tokens locales. |
| AC-TGL-014 | PASS | Descripción y nota de página aclaran Mixed ≠ Disabled; no se definió acción de clic. Ocho etiquetas Mixed están ocultas y sus 16 referencias a propiedades TEXT/BOOLEAN fueron verificadas después de reconectarlas. El set permanece `UNPUBLISHED`. |

**Medición:** contraste del guion Default por modo Contable / Administrativo / Servicios / Personas: 5.56 / 5.93 / 3.24 / 6.32:1; Hover: 11.07 / 9.53 / 7.20 / 10.01:1. Disabled: 2.34:1, marcado `*` para revisión interna; no se cambió color por contraste y el estado inactivo requiere evaluar la aplicabilidad del criterio. Los valores se calcularon con colores resueltos desde variables Figma, no se derivaron solo del PNG.

**Hallazgo corregido:** al clonar las variantes On, Figma dejó vacías las referencias de propiedades en las etiquetas ocultas. Se restauraron explícitamente los enlaces `visible` y `characters` en los ocho nodos nuevos y se comprobó su lectura posterior. No se eliminaron ni renombraron las ocho variantes previas. El QA `PASS` se limita a la enmienda Mixed; la reapertura cromática previa del resto de Toggle sigue separada.
