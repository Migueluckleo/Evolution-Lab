# UX Behavior Contract

## 1. Context

`BHC-TOGGLE-MIXED-001` · Toggle de selección agregada. Resolución `EXACT` contra el [contrato fuente de Toggle](../../contracts/toggle.contract.v0.1.0.md). Este contrato define el comportamiento del producto sin modificar la evidencia del Figma anterior.

## 2. Resolved UI Elements

El set fuente `toggled` contiene la propiedad de variante `toggle` con On/Off y `state` con Default/Hover/Focus/Disabled. Se corresponde con el set `Toggle` de AI Design System. Evidencia: `component.id`, `properties.definitions` e `interactions.status` del [YAML fuente](../../contracts/toggle.contract.v0.1.0.yaml). No hay interacción definida en la fuente.

## 3. Product Intent

`USER_DEFINED`: indicar visualmente una selección agregada que contiene elementos encendidos y apagados a la vez.

## 4. Controls and Behaviors

`BR-001` · `USER_DEFINED`: cuando un grupo contiene toggles On y Off, el control agregado muestra `Toggle=Mixed`. El indicador visual es una barra horizontal centrada, como en el PNG compartido por el usuario. La propiedad `State` sigue siendo independiente.

## 5. Interaction Rules

No se definió qué ocurre al pulsar el control agregado en Mixed (`UPD-001`). Este contrato no presupone que activar Mixed encienda o apague todo el grupo.

## 6. Data / Filtering Rules

Not defined.

## 7. State Changes

`ST-001` · `Mixed` significa que el agregado contiene al menos un valor On y uno Off. No se definieron transiciones provocadas por clic.

## 8. Dynamic Content

Not defined.

## 9. Feedback

Not defined.

## 10. Edge Cases

No se definió qué representa un grupo vacío (`UPD-002`).

## 11. Unresolved Product Decisions

- `UPD-001` · ¿Qué debe ocurrir al activar el Toggle agregado desde Mixed? Afecta implementación y pruebas.
- `UPD-002` · ¿Qué valor muestra el Toggle agregado cuando el grupo no contiene elementos? Afecta implementación y pruebas.

## 12. Traceability

`EV-001` · declaración verbal del usuario sobre grupos parcialmente activos; `EV-002` · PNG del usuario con guion blanco sobre track azul; `EV-003` · contrato estructural fuente. Los identificadores y la página de origen constan en el [YAML sincronizado](behavior-contract.yaml). `EV-004` y `EV-005` marcan las decisiones pendientes.

## 13. QA-Derivable Rules

`QA-001` · `DERIVED`: dado un grupo con valores On y Off, al evaluar el agregado debe mostrarse `Toggle=Mixed` con el guion centrado. No se derivan casos para interacción ni grupo vacío.
