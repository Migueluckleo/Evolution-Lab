---
amendment_id: AMD-TOGGLE-SOURCE-COLOR-005
status: DELEGATED_FOR_BUILD
applies_to: TOGGLE-001
base_contract_version: 0.1.0
base_contract_digest_sha256: c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38
version: 0.1.5
supersedes_scope: AMD-TOGGLE-VISUAL-CONTRAST-002 REQ-TGL-005/AC-TGL-005 only for Off/Default and Off/Focus track strokes and their >=3:1 border threshold
decision_refs: [DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-CONTRAST-LIMITATIONS-001, DEC-MIGRATION-TRACEABILITY-001]
source_data_ref: sources/inventories/tokens.inventory.json
source_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-24
user_audit: PENDING
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: QA exclusivo AC-TGL-015–016. La base Toggle permanece en drafts; AUD-003 y el alcance transversal pendiente no se convierten en PASS.
>
> Sustento: [QA documental 1](../../qa/contracts/toggle.source-color-amendment.v0.1.5.review.md); [QA técnico 1](../../qa/implementations/toggle.source-color.v0.1.5.figma.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Toggle · enmienda de color fuente 0.1.5

La [regla transversal de trazabilidad](../MIGRATION-TOKEN-TRACEABILITY.contract.md) y las decisiones recientes del usuario priorizan el color de la Librería original frente al ajuste de contraste de la [enmienda 0.1.2](toggle.visual-contrast-amendment.v0.1.2.md). Esta enmienda sustituye **solo** el stroke de los tracks Off/Default y Off/Focus y su umbral de contraste. Conserva los fills `color/background/muted` ya correctos, el rol `color/background/control-hover` de Off/Hover, el thumb `color/background/default` de Off/Disabled, los efectos de foco de [0.1.3](toggle.focus-effect-amendment.v0.1.3.md) y las cuatro variantes Mixed de [0.1.4](toggle.mixed-amendment.v0.1.4.md).

## Evidencia y mapa de binding

| Estado / propiedad | Fuente observada | Destino antes de corregir | Destino exigido |
|---|---|---|---|
| Off/Default · stroke de track | Nodo `1230:23896`; `color/border/strong` origen `VariableID:2849:196130` → neutral/300 | Nodo `111:145`; `color/border/brand` local `VariableID:13:16` | `color/border/strong` local `VariableID:13:15` → neutral/300 |
| Off/Focus · stroke de track | Nodo `1230:23886`; `color/border/disabled` origen `VariableID:2849:196137` → neutral/300 | Nodo `111:155`; `color/border/control` local `VariableID:123:122` → neutral/500 | `color/border/strong` local `VariableID:13:15` → neutral/300 |

En la fuente, Off/Focus consume un rol llamado `disabled` pese a que Focus es operable. El destino utiliza `strong` para conservar **exactamente el mismo gris** sin asignar semántica Disabled a un estado activo. El rol local ya existe, tiene scope `STROKE_COLOR` y alias a `color/neutral/300` (`VariableID:8:95`) en los cuatro modos. El fondo de ambos tracks ya consume `color/background/muted` local `VariableID:13:37`, que resuelve al mismo neutral/300; no se modifica. No se agregan variables ni se edita el JSON.

| ID | Requisito | Procedencia | Criterio |
|---|---|---|---|
| REQ-TGL-015 | Vincular los strokes de Off/Default y Off/Focus al rol local `color/border/strong`, sin cambiar fills, geometría, propiedades, efectos, otros estados ni IDs de variante. | OBSERVED fuente/destino + EXPLICIT fidelidad y scope semántico | AC-TGL-015 |
| REQ-TGL-016 | Mantener el gris de origen aunque su contorno sobre blanco tenga contraste limitado; registrar `*` con medición real y no presentar esta limitación como conformidad accesible. | EXPLICIT decisión de contraste + DERIVED medición | AC-TGL-016 |

## Acceptance criteria

| ID | Resultado necesario |
|---|---|
| AC-TGL-015 | Readback de `111:145` y `111:155` confirma `strokes[].boundVariables.color.id = VariableID:13:15`, y el alias de esa variable apunta a neutral/300 en los cuatro modos. Sus fills siguen en `VariableID:13:37`; las ocho variantes originales conservan IDs, Mixed conserva cuatro variantes, y los efectos de Focus no cambian. |
| AC-TGL-016 | El borde y fondo neutral/300 sobre blanco se documentan con ratio aproximado 1.23:1 y asterisco en la auditoría interna; el QA cromático previo que exigía ≥3:1 para estos dos strokes queda `SUPERSEDED` solo en ese alcance. No se afirma WCAG ni publicación Figma. |

Esta corrección no cierra por sí sola el barrido cromático de las doce variantes Toggle ni la auditoría humana; cualquier otra divergencia se documentará por separado. [QA documental](../../qa/contracts/toggle.source-color-amendment.v0.1.5.review.md) `PASS` para construir esta corrección acotada.
