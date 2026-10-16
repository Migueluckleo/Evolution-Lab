---
amendment_id: AMD-TOGGLE-MIXED-004
status: DELEGATED_FOR_BUILD
applies_to: TOGGLE-001
base_contract_version: 0.1.0
base_contract_digest_sha256: c3b6d1100241e3bdb5c89cc98e89854cda999c87f775a8552211280979326c38
version: 0.1.4
decision_refs: [DEC-TOGGLE-MIXED-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
behavior_ref: drafts/behavior/toggle-mixed/behavior-contract.yaml
behavior_digest_sha256: 870fee221c30dc80385f72be0339104b7f7cd7ccfc28cbe03138049ff662b8bc
source_data_ref: sources/inventories/tokens.inventory.json
source_data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
last_updated: 2026-09-24
user_audit: PENDING
---

> Publicación documental: 2026-10-06. Ubicación canónica en specs; DELEGATED_FOR_BUILD, auditoría humana PENDING. Movimiento administrativo sin cambiar requisitos ni publicar la biblioteca Figma.
>
> Vigencia: QA de las cuatro variantes Mixed, sin decisión de clic/grupo vacío ni cierre global de Toggle. Las referencias a0.1.2 deben leerse con la sustitución acotada0.1.5. Aplicar [referencia 1](toggle.source-color-amendment.v0.1.5.md).
>
> Sustento: [QA documental 1](../../qa/contracts/toggle.mixed-amendment.v0.1.4.review.md); [QA técnico 1](../../qa/implementations/toggle.mixed.v0.1.4.figma.review.md). [Registro de promoción](../../qa/contracts/specs-promotion.2026-10-06.review.md). Los digests históricos inferiores identifican sus cortes originales.

# Toggle · enmienda Mixed 0.1.4

Esta enmienda agrega a [TOGGLE-001](../../drafts/contracts/toggle.contract.v0.1.0.md) el valor `Mixed` solicitado para una selección agregada con toggles On y Off. El [PNG del usuario](../../references/toggle-mixed-user-2026-09-24.png) muestra una pista azul de 80×40 a escala 2 y un guion horizontal blanco centrado. En AI Design System corresponde a pista 40×20 e indicador 24×4 con extremos redondeados. `Mixed` describe selección parcial, no indisponibilidad. El comportamiento de clic y de grupo vacío queda `REQUIRES_DEFINITION` en el [contrato de comportamiento](../../drafts/behavior/toggle-mixed/behavior-contract.md).

Se mantiene la página existente `Toggles` y el set local `Toggle`. La propiedad de variante `Toggle` pasa de `{On, Off}` a `{On, Off, Mixed}`; `State` conserva `{Default, Hover, Focus, Disabled}`. No hace falta una tercera propiedad: ésta duplicaría el mismo eje. El nuevo producto cartesiano añade **cuatro** componentes, sin cambiar los ocho previos ni las cuatro propiedades de etiquetas. Las nuevas variantes conservan 40×20 y reutilizan los estados de pista/foco de On, sustituyendo únicamente el thumb por el guion. En Mixed/Disabled, la pista y el foco Disabled se conservan y el guion utiliza el rol de icono deshabilitado.

| ID | Requisito | Fuerza | Procedencia | Comprobación |
|---|---|---|---|---|
| REQ-TGL-011 | Añadir `Mixed` al eje `Toggle` y las cuatro combinaciones con `State`; conservar seis definiciones de propiedad y ocho variantes existentes. | MUST | EXPLICIT usuario + DERIVED matriz consistente | AC-TGL-011 |
| REQ-TGL-012 | Representar Mixed con guion centrado 24×4, radio 2 visual, en pista 40×20; Default, Hover y Focus con pista azul semántica correspondiente, Disabled con su pista deshabilitada. | MUST | OBSERVED PNG + DERIVED escala 2 | AC-TGL-012 |
| REQ-TGL-013 | Vincular el guion visible a `color/icon/on-brand` en Default/Hover/Focus y a `color/icon/disabled` en Disabled; ambos son variables locales de scope `SHAPE_FILL` aliasadas a primitivas del JSON aprobado. No crear token ni color literal. | MUST | DERIVED mapa semántico de los tokens aprobados | AC-TGL-013 |
| REQ-TGL-014 | No representar Mixed como Off o Disabled, ni afirmar interacción de Figma/web que no está definida. Actualizar la descripción del set para aclarar su uso agregado. | MUST | EXPLICIT usuario + contrato de comportamiento | AC-TGL-014 |

El mapa fuente→destino para `color/icon/on-brand` es `VariableID:2849:196142`→ID local verificado en preflight; para `color/icon/disabled`, `VariableID:2849:196147`→ID local verificado. La pista, borde, radios, foco y etiquetas de las nuevas variantes clonan los bindings de On del mismo `State`, por identidad de variable local, no por coincidencia visual. El set y su página se leen antes de escribir; este cambio es `UPDATE` aditivo.

## Acceptance criteria

| ID | Resultado necesario |
|---|---|
| AC-TGL-011 | Readback de un solo set `Toggle`, 12 pares únicos, seis definiciones de propiedad, valores `Toggle={On, Off, Mixed}` y ocho IDs preexistentes intactos. |
| AC-TGL-012 | Cuatro variantes Mixed de 40×20; cada pista contiene un guion centrado 24×4 sin thumb, con estados de pista y foco coherentes; captura posterior sin recortes. |
| AC-TGL-013 | Cuatro fills de guion vinculados a variables locales del rol de icono correcto, con scopes y aliases comprobados en los modos; sin fills de texto/superficie en el indicador. |
| AC-TGL-014 | Descripción distingue Mixed de Disabled y documenta que no se define comportamiento de clic; `UNPUBLISHED`, auditoría humana pendiente. |

Esta enmienda no sustituye [0.1.2](toggle.visual-contrast-amendment.v0.1.2.md) ni [0.1.3](toggle.focus-effect-amendment.v0.1.3.md). El PNG se conserva como fuente local en `references/` por el procedimiento de ingesta; su ruta original de portapapeles puede ser temporal.
