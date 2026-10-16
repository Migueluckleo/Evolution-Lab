# QA-CONTROL-COLORS-FIGMA-001 · variables semánticas de control

```yaml
qa_id: QA-CONTROL-COLORS-FIGMA-001
review_type: IMPLEMENTATION_REVIEW
contract_ref: AMD-FOUNDATIONS-CONTROL-COLORS-001
implementation_ref: IMP-CONTROL-COLORS-FIGMA-001
target: figma
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

Destino leído **después** de crear las variables: `AI-Design-System`, colección local `semantic` (`VariableCollectionId:6:2`). El [JSON canónico de extensión](../../drafts/foundations/ai-design-system.control-colors.v0.1.0.json), SHA-256 `4ef75143af30b0e934cb94aa62d3acb56c32874dc7e229a500a31c8928a7f839`, define dos variables. El [inventario histórico](../../sources/inventories/tokens.inventory.json) conserva SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474` y no fue editado.

| Criterio | Resultado leído |
|---|---|
| AC-TOK-EXT-001 | `semantic` contiene 131 variables frente a 129 antes de la extensión; una `color/border/control` (`VariableID:123:122`) y una `color/background/control-hover` (`VariableID:123:123`), sin colisiones en el preflight. |
| AC-TOK-EXT-002 | Ambas igualan `name`, `resolvedType: COLOR`, la `description` del JSON, `codeSyntax: {}` y scopes respectivos `STROKE_COLOR` / `FRAME_FILL, SHAPE_FILL`. Ocho de ocho valores modo son `VARIABLE_ALIAS` hacia la primitiva local `color/neutral/500` (`VariableID:8:97`), cuyo literal `Value` permanece #64748b. |
| AC-TOK-EXT-003 | [Mapa de IDs](../../implementations/figma/control-colors.v0.1.0.state.json), digest de contrato y JSON registrados. El readback posterior de Toggle comprueba los consumidores por ID. `user_audit: PENDING`; no se publicó la biblioteca. |

La inspección distingue el token de borde del de fondo aun cuando aliasan el mismo primitivo. La respuesta de creación no fue la única evidencia; se leyeron ambos objetos, el conteo y el primitivo de nuevo. La revisión valida esta extensión de dos variables, no reaudita campo por campo las 129 variables previas ni certifica web.
