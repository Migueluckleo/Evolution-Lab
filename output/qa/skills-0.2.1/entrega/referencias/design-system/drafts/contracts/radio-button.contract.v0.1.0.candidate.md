---
contract_schema: sdd-project/0.2
contract_id: RADIO-BUTTON-001
name: Radio Button
type: component
status: IN_REVIEW
version: 0.1.0
owner: null
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Radio Buttons
sources: [SRC-FIGMA-RADIO-BUTTON-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/radio-button.source.component-contract.yaml, drafts/foundations/ai-design-system.radio-indicator-colors.v0.1.0.json, drafts/foundations/ai-design-system.focus-effects.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-RADIO-INDICATOR-COLORS-001, FOUNDATIONS-FOCUS-EFFECTS-001]
user_audit: PENDING
---

# Radio Button · contrato candidato de reconstrucción 0.1.0

La evidencia de origen está en el [contrato técnico MD](radio-button.source.component-contract.md) y [YAML](radio-button.source.component-contract.yaml), SHA-256 `739b6b023c26b50bfca00c51320403175e9be017ccb18371d5bd7f4051db912b` y `b6e66f541e7740cbea7d20512c5fca19a9d16b97175fa89a61deef02761cb3f4`. El inventario histórico de variables SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474` sigue inmutable. Los colores adicionales se definen solo en [JSON del indicador](../foundations/ai-design-system.radio-indicator-colors.v0.1.0.json), SHA-256 `46f53dc329a93374f486ad26452cdd991c6cb0651a6c068865e34352d8e6161a`, y [JSON de efectos de foco](../foundations/ai-design-system.focus-effects.v0.1.0.json), SHA-256 `0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4`. Las IDs de origen no son IDs de destino.

## 1. Purpose

**EXPLICIT, nota de página fuente:** presentar opciones mutuamente excluyentes con una etiqueta clara. El contrato Figma representa un control individual, no crea automáticamente un grupo funcional o comportamiento de selección exclusiva.

## 2. Contract

Destino único `AI-Design-System` `tj3WIBEZDGLVs7MJWKCwgf`, página funcional exacta `Radio Buttons`. El nombre procede de la familia `radio button` de origen y de su función, no de color, estado o regla automática. El target contiene actualmente Buttons, Chips, Tooltips, Badges y Toggles; no existe página homónima. La construcción queda sometida a QA documental y a auditoría humana posterior, no a una supuesta aprobación previa del detalle.

## 3. Anatomy

```text
Radio Buttons (PAGE)
├─ Radio Indicator (COMPONENT_SET; dependencia local de la familia)
│  └─ Selected={True|False}, State={Default|Hover|Focus|Disabled}
└─ Radio Button (COMPONENT_SET; API de consumo)
   └─ Selected={True|False}, State={Default|Hover|Focus|Disabled}
      ├─ Left label (TEXT; oculto por defecto)
      ├─ Radio Indicator (INSTANCE; 24×24)
      └─ Right label (TEXT; oculto por defecto)
```

El indicador On visible se compone de disco exterior 18×18 y centro blanco 8×8, ambos círculos concéntricos dentro de 24×24; es equivalente al contorno fuente de 5 px sin fingir que existe un token de stroke 5. Off conserva círculo blanco 18×18 con stroke 2 px. La dependencia local observada `radio` se preserva conceptualmente; el destino expone los ocho estados visuales en el indicador para evitar overrides manuales por instancia.

## 4. Properties

| Propiedad destino | Tipo | Default | Procedencia |
|---|---|---|---|
| Selected | VARIANT | True | fuente `radio=on/off`, mapeada a selección booleana |
| State | VARIANT | Default | fuente `state=enabled/hover/focus/disabled`; enabled→Default |
| Left label | TEXT | `Field Label` | mejora explícita sobre texto fuente no editable como propiedad |
| Right label | TEXT | `Field Label` | misma mejora |
| Show left label | BOOLEAN | false | booleano fuente izquierdo |
| Show right label | BOOLEAN | false | booleano fuente derecho |

Los nombres son propios del destino. Las dos propiedades TEXT se enlazan a las 16 etiquetas; las dos BOOLEAN controlan visibilidad independientemente. `Field Label` es solo texto de muestra. El estado de selección no se modela como un tercer booleano además del eje Selected.

## 5. Variants

Matriz completa 2×4 en ambos sets: True/False × Default/Hover/Focus/Disabled, ocho variantes cada uno. No se inventan Press, Error ni tamaños. Cada variante del componente de consumo mide 24×24 sin etiquetas visibles, como la fuente. Default de consumo: Selected=True, State=Default para preservar la variante default del origen; no implica que un grupo deba arrancar seleccionado en producto.

## 6. Sizes

Indicador 24×24 y círculo exterior 18×18 centrado en 3,3. Centro On 8×8 centrado en 8,8. El tamaño del control visual no demuestra área táctil de 24×24 ni sustituye reglas web. Las etiquetas opcionales usan ancho de contenido flexible bajo auto layout para permitir edición; el ancho fijo 68×18 de la fuente es evidencia histórica, no límite impuesto al texto editable.

## 7. States

| Selected | State | Indicador exterior | Centro/contorno | Label |
|---|---|---|---|---|
| True | Default | `color/background/control-selected` | centro `color/background/default` | primary |
| True | Hover | `color/background/control-selected-hover` | centro blanco | primary |
| True | Focus | `color/background/control-selected` | centro blanco + anillo de efecto | primary |
| True | Disabled | `color/background/disabled` | centro blanco | disabled |
| False | Default | `color/background/default` | 2 px `color/border/control` | primary |
| False | Hover | blanco | 2 px `color/border/hover` | primary |
| False | Focus | blanco | 2 px `color/border/brand` + anillo de efecto | primary |
| False | Disabled | blanco | 2 px `color/border/disabled` | disabled |

Disabled expresa indisponibilidad, no Off. Off Default/Hover/Focus permanecen operables en la representación del componente.
El contorno Off Default fuente usa `color/border/default`, que resuelve a 2.56:1 sobre blanco; el destino usa el rol existente `color/border/control` `VariableID:123:122`, 4.76:1, ya documentado para controles operables. Es un oscurecimiento acotado del anillo sin modificar el fondo, pendiente de auditoría visual del usuario. Los otros contornos y discos activos alcanzan al menos 3:1 en Contable, Administrativo, Servicios y Personas; el caso cromático mínimo entre los seleccionados es el naranja de Servicios, 3.24:1 sobre blanco.

## 8. Behavior

Las variantes son estados visuales estáticos; la fuente no contiene reacciones. No se añade prototipo que cambie Selected automáticamente. Selección exclusiva de grupo, clic, hover real, teclado y validación del formulario quedan fuera del Figma construido.

## 9. Accessibility

Se preserva el anillo Focus y la diferencia On/Off; las etiquetas están ocultas por defecto para fidelidad visual. La documentación de página debe indicar que un uso real requiere etiqueta clara y nombre accesible. El contrato no afirma rol radio web, comportamiento de teclado, agrupación, hit target ni conformidad WCAG. QA puede medir contraste visual en los cuatro modos, no funcionalidad web.

## 10. Design tokens

| Parte | Binding semántico de destino | Scope exigido |
|---|---|---|
| Disco On normal/Focus | `color/background/control-selected` (extensión) | `SHAPE_FILL` |
| Disco On Hover | `color/background/control-selected-hover` (extensión) | `SHAPE_FILL` |
| Disco On Disabled | `color/background/disabled` `VariableID:13:38` | fill de forma |
| Centro On y círculo Off | `color/background/default` `VariableID:13:35` | fill de forma |
| Stroke Off | `color/border/control` `VariableID:123:122` y `color/border/{hover,brand,disabled}` `VariableID:13:{19,16,17}` | `STROKE_COLOR` |
| Anillo Focus exterior/interior | `color/focus/effect-outer` `VariableID:136:122` / `color/focus/effect-inner` `VariableID:136:123` | `EFFECT_COLOR` |
| Etiquetas | `color/text/{primary,disabled}` `VariableID:13:{27,30}` | `TEXT_FILL` |
| Tipografía | `font/family/base` `VariableID:10:2`, `font/weight/regular` `VariableID:10:3`, `font/size/sm` `VariableID:10:9`, `font/line-height/sm` `VariableID:12:8`, `font/letter-spacing/normal` `VariableID:12:16` | scopes tipográficos respectivos |
| Geometría | `spacing/sm` `VariableID:12:30`, `radius/full` `VariableID:13:11`, `stroke/md` `VariableID:13:3` | GAP, CORNER_RADIUS, STROKE_FLOAT |

Los dos IDs de color nuevos del indicador se asignarán tras creación y lectura en Figma; sus aliases por modo están fijados en el JSON de extensión. Todos los demás IDs son locales del destino ya leídos. Los tres tokens de geometría remotos del origen no se importan: el gap exterior y stroke Off se asignan a variables locales por función, y el radio del indicador usa `radius/full`. Igualdad visual no da equivalencia semántica. Ningún color text se aplica a shapes ni efecto, ni un borde como fill.

## 11. Content rules

Cuando se active una etiqueta visual, su texto debe poder cambiarse desde una propiedad TEXT. No se deben publicar instancias reales con `Field Label` como contenido final. Se recomienda una sola etiqueta visible por control para evitar redundancia visual, pero el origen permite ambas y el contrato Figma no prohíbe su combinación; la semántica de nombre accesible requiere definición posterior.

## 12. Composition rules

El indicador anidado se instancia en cada variante del wrapper, sin detachment. Los ocho indicadores internos exponen correspondencia Selected/State 1:1 con el wrapper. Las etiquetas y el indicador son hijos directos de auto layout HORIZONTAL, gap `spacing/sm`, sin padding. La variación entre modos de marca ocurre por aliases del target, no duplicando componentes por modo.

## 13. Responsive behavior

No se deduce responsive de la captura. El wrapper abraza su contenido visible; las etiquetas editables deben crecer sin solaparse. El tamaño visual del indicador es fijo. No se especifican breakpoints.

## 14. Edge cases

Con ambas etiquetas ocultas, el indicador queda sin texto visible como en la fuente; la página de documentación debe advertir la necesidad de un nombre accesible en consumo real. Con ambas visibles, el auto layout conserva orden izquierda–indicador–derecha. Texto largo puede crecer; no se impone truncamiento no observado. Focus Disabled simultáneo no forma parte de la matriz.

## 15. Forbidden combinations

Solo los ocho pares Selected×State enumerados son variantes de esta versión. No se agregan mezclas Press/Error/Loading. Las dos booleanas de etiqueta pueden combinarse libremente porque la fuente no impone prohibición. No se prohíbe False+Disabled: existe en la fuente.

## 16. Design ↔ Code mapping

Figma `Selected` representa selección visual; `State` representa apariencia visual. Una futura implementación web deberá definir `checked`, `disabled`, foco real y agrupación semántica en contrato de comportamiento propio; no se genera código ni se declara equivalencia de API. Las propiedades TEXT/BOOLEAN gobiernan solo composición en Figma.

## 17. Acceptance criteria

| ID | Requisito verificable |
|---|---|
| AC-RAD-001 | Página `Radio Buttons` única, set de consumo `Radio Button` y dependencia local `Radio Indicator` con IDs registrados; familias previas intactas. |
| AC-RAD-002 | Ocho variantes por set, ejes, nombres y defaults exactos; correspondencia de instancia 1:1. |
| AC-RAD-003 | Control 24×24 sin labels visibles, disco 18×18, centro 8×8 On, contorno Off 2 px, auto layout y gap tokenizado. |
| AC-RAD-004 | Dos TEXT y dos BOOLEAN conectadas a cada variante del wrapper; 16 etiquetas con bindings tipográficos y color semántico. |
| AC-RAD-005 | Todos los fills, strokes, effects de foco, radios, gaps y stroke widths aplicables ligados a variables locales de rol y scope correctos; extensiones JSON verificadas antes de consumir. |
| AC-RAD-006 | Dos Focus con anillo 4/2 px, colores de efecto tokenizados, sin cambio visual material contra la captura fuente salvo halo interior blanco documentado. |
| AC-RAD-007 | Cero reacciones añadidas; nota de accesibilidad sin afirmar comportamiento web. Captura y readback finales, `user_audit: PENDING`, set `UNPUBLISHED`. |

## 18. Examples

Ejemplo visual de origen: ocho controles sin etiquetas visibles en una cuadrícula On/Off × Enabled/Hover/Focus/Disabled. `Field Label` se conserva solo como placeholder editable. No se infieren microcopys de producto.

## 19. Source of truth

Fuente estructural: [set antiguo](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1230-24283), key `92e794dad0b717afa2e923d7bf2db0b041e9f230`, lectura 53/53. Datos de tokens históricos: JSON aprobado y sus IDs de origen conservados en YAML. Datos de extensiones: JSON de destino versionados. Contrato MD gobierna reglas; JSON gobierna definición de tokens. La implementación destino y QA son evidencia posterior, no fuente que reescriba el contrato.

## 20. Change management

Toda diferencia de estructura, colores o API se registra antes de escribir: selected ring por dos fills; enabled→Default; texto editable; interlineado 18→20; halo interior #f8fafc→blanco por primitiva existente; contorno Off Default neutral 400→500 para contraste; dependencia del indicador expandida a ocho estados. Estas son decisiones delegadas para auditoría posterior, no observaciones del origen. Un cambio posterior necesita enmienda identificada y nuevo QA.

## 21. Changelog

- 0.1.0 candidato: evidencia completa del origen, matriz de reconstrucción, variables estrictamente semánticas, indicador local reusable y criterios AC-RAD-001–007. Sin ejecución Figma hasta QA documental y preflight de extensiones.
