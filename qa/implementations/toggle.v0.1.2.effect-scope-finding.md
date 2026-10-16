# QA-TOGGLE-FIGMA-005 · hallazgo de scope en efectos de foco

```yaml
qa_id: QA-TOGGLE-FIGMA-005
review_type: IMPLEMENTATION_REVIEW
implementation_ref: IMP-TOGGLE-FIGMA-001
contract_version_observed: 0.1.2
target: figma
scope: effects_color
executed_at: 2026-09-23
result: FAIL
resolution: AMD-TOGGLE-FOCUS-EFFECT-003
```

Una auditoría posterior al QA de **paints** leyó también `effects[].boundVariables.color` en el set Toggle. Los tracks On/Focus `111:135` y Off/Focus `111:155` conservan colores y anillos visibles, pero cada uno contiene:

| Efecto | Binding leído | Scope de la variable | Scope requerido |
|---|---|---|---|
| DROP_SHADOW exterior | `color/focus/ring` `VariableID:13:71` | `STROKE_COLOR` | `EFFECT_COLOR` |
| DROP_SHADOW interior | `color/background/default` `VariableID:13:35` | `FRAME_FILL`, `SHAPE_FILL` | `EFFECT_COLOR` |

Son cuatro bindings técnicamente aceptados por Figma pero incompatibles con la exigencia semántica estricta del usuario. El [QA retrospectivo de 430 paints](semantic-scope-retrospective.v0.1.0.review.md) no cubría efectos y permanece correcto dentro de ese alcance. El `PASS` técnico 0.1.2 se conserva como historia, pero el estado actual de Toggle pasa a `VALIDATING` para el control ampliado hasta la corrección y lectura posterior. No se modifica el Figma fuente.
