---
contract_schema: sdd-project/0.2
contract_id: TOGGLE-001
name: Toggle
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
owner: null
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Toggles
sources: [SRC-FIGMA-TOGGLE-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/toggle.contract.v0.1.0.yaml]
dependencies: [FOUNDATIONS-TOKENS-001]
user_audit: PENDING
---

# Toggle · contrato delegado 0.1.0

Inspección read-only del set [toggled](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1230-23858), key `5dd1c16f84eb1e6803326c404c137e40ae28ca6b`, en la página fuente `1084:7229`. Se leyeron 41/41 nodos, incluidas 16 etiquetas ocultas; 24 variables únicas y ningún componente anidado ni estilo con nombre. El [YAML de evidencia](toggle.contract.v0.1.0.yaml) conserva IDs de origen. El [QA documental](../../qa/contracts/toggle.v0.1.0.review.md) pasó; esta versión queda `DELEGATED_FOR_BUILD` bajo DEC-LEGACY-MIGRATION-DELEGATION-001, no como aprobación humana.

## 1. Component Identity

**Observado de Figma:** el set se llama `toggled`, mide 680×194 como contenedor de documentación y tiene ocho variantes. La descripción de portada explica que el toggle activa o desactiva una opción binaria. **Derivado:** la familia funcional del destino se llama `Toggle` y su página exclusiva `Toggles`, coherente con Buttons, Chips, Tooltips y Badges. La página fuente decorada no gobierna el nombre destino.

## 2. Anatomy

```text
Toggles (PAGE)
└─ Toggle (COMPONENT_SET)
   └─ Toggle={On|Off}, State={Default|Hover|Focus|Disabled}
      ├─ Left label (TEXT; oculto por defecto)
      ├─ Track (FRAME; 40×20)
      │  └─ Thumb (ELLIPSE; 16⅔×16⅔)
      └─ Right label (TEXT; oculto por defecto)
```

Las dos etiquetas son opcionales e independientes. No hay iconos, instancias ni slots.

## 3. Dependencies

El set usa 24 variables locales de origen y cero estilos con nombre; no hay dependencia remota. Para el destino, cada rol debe resolver por nombre y modo al [JSON aprobado](../../sources/inventories/tokens.inventory.json), SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. Los IDs de origen y destino nunca se intercambian.

## 4. Properties

| Propiedad destino | Tipo | Default | Evidencia fuente |
|---|---|---|---|
| Toggle | VARIANT | On | `toggle`: on/off |
| State | VARIANT | Default | `state`: `defualt`, hover, focus, disabled |
| Left label | TEXT | `Field Label` | `text left#7375:36` |
| Right label | TEXT | `Field Label` | ` text right#7375:45` |
| Show left label | BOOLEAN | false | `show left field label#20125:0` |
| Show right label | BOOLEAN | false | `show right field label#102635:0` |

El error fuente `defualt` se normaliza a `Default`; se preserva en el YAML. Se quitan el espacio inicial del nombre de texto derecho y el nombre genérico `Field Label` de las propiedades, no del valor editable.

## 5. Variants

Matriz completa de 2×4: On/Off × Default/Hover/Focus/Disabled. Los ocho pares existen en fuente; no se añade Press ni un eje de tamaño. Cada variante visible sin etiquetas mide 40×20.

## 6. States

Hover y Focus son apariencias existentes, no prueba de interacción real. Disabled es una apariencia existente. El estado On/Off es selección binaria, separado del estado visual. Las reacciones de prototipo del set y de sus tracks están vacías.

## 7. Layout

Cada componente usa auto layout horizontal HUG/HUG y gap 8 ligado a `spacing/sm`. El track es 40×20 fijo, con stroke interior 1 px y radio de píldora. El thumb mide 16.666666×16.666666 px; x=21.666666 si On, x=1.666666 si Off, y=1.666666. Ambas etiquetas fuente son de ancho fijo 68 y ocultas por defecto. Se mantiene la geometría fraccional observada para preservar la imagen.

El track Off/Focus fuente liga sus radios a `font/size/lg` (=20), un token tipográfico impropio para el radio. El destino empleará `radius/full` en las ocho variantes; ambas formas resultan cápsula en un track de 20 px.

## 8. Visual Styles

| Toggle/State | Track fill | Track stroke | Thumb fill | Label fill |
|---|---|---|---|---|
| On/Default | `color/interactive/primary/default` | `color/border/brand` | `color/background/default` | `color/text/primary` |
| On/Hover | `color/interactive/primary/hover` | `color/border/hover` | `color/background/default` | `color/text/primary` |
| On/Focus | `color/interactive/primary/default` | `color/border/brand` | `color/background/default` | `color/text/primary` |
| On/Disabled | `color/interactive/disabled/bg` | `color/border/disabled` | `color/background/muted` | `color/text/disabled` |
| Off/Default | `color/background/muted` | `color/border/strong` | `color/background/default` | `color/text/primary` |
| Off/Hover | `color/text/tertiary` | `color/border/default` | `color/background/default` | `color/text/primary` |
| Off/Focus | `color/background/muted` | `color/border/strong` | `color/background/default` | `color/text/primary` |
| Off/Disabled | `color/background/disabled` | `color/border/disabled` | `color/icon/on-brand` | `color/text/disabled` |

Off/Focus usa `background/disabled` y `border/disabled` en fuente aunque no está Disabled. Se normalizan a muted/strong, que comparten aliases primitivos en los cuatro modos; la decisión es semántica y no se deduce solo de igualdad RGB. Off/Hover conserva `color/text/tertiary` para fidelidad visual; es una deuda semántica explícita porque el JSON no ofrece un rol de track hover neutral con ese valor.

Seis tracks no Focus llevan tres INNER_SHADOW literales. On/Focus lleva dos DROP_SHADOW de anillo; Off/Focus lleva esos dos más tres INNER_SHADOW. El JSON no contiene una categoría de sombra/elevación: se preserva la geometría fuente sin inventar tokens de sombra. El anillo exterior usa `color/focus/ring`; el halo claro usa `color/background/default` existente, cuya blancura difiere levemente del literal fuente. Si Figma permite ligar el color de efecto, ambos deben tener binding local real; no basta el mismo RGB.

## 9. Typography

Los 16 textos de ejemplo son Manrope Regular 14 px y line-height 15 px con tracking 0%, todos ocultos por defecto. En destino: `font/family/base`, `font/weight/regular`, `font/size/sm`, `font/line-height/xs` (16 px) y `font/letter-spacing/normal`. El interlineado aumenta 1 px para usar la escala tipográfica aprobada; no se inventa un token 15.

## 10. Tokens

Los IDs siguientes son locales de AI-Design-System, todos de `semantic` y con prefijo completo `VariableID:`.

| Uso | Roles e IDs |
|---|---|
| Track On | primary default `13:57`; primary hover `13:58`; disabled bg `13:65` |
| Track Off | background muted `13:37`; background disabled `13:38`; text tertiary `13:29` |
| Bordes | brand `13:16`; hover `13:19`; disabled `13:17`; strong `13:15`; default `13:13` |
| Thumb | background default `13:35`; muted `13:37`; icon on-brand `13:23` |
| Etiquetas | text primary `13:27`; text disabled `13:30` |
| Foco | focus ring `13:71`; background default `13:35` |
| Tipografía | family `10:2`; weight `10:3`; size `10:9`; line-height `12:7`; letter-spacing `12:16` |
| Geometría | spacing/sm `12:30`; stroke/xs `12:41`; radius/full `13:11` |

Los tokens de padding `spacing/3xl` y `spacing/6xl` solo afectan el contenedor documental fuente, no las variantes de consumo; se omiten en el set destino. Ninguna variable se crea o cambia.

## 11. Content

`Field Label` es texto de ejemplo, no una prescripción de contenido. Al activar cualquiera de los booleanos, el texto correspondiente debe ser editable mediante su propiedad. El set fuente no define truncamiento, wrapping, localización ni reglas de texto largo.

## 12. Interactions

No hay reacciones en componentes ni tracks. No se promete que el prototipo cambie On/Off al pulsar o que Hover/Focus se active automáticamente. El contrato web de control, clic y teclado requiere definición posterior.

## 13. Accessibility

El diseño muestra estado binario y anillo de foco, pero Figma no prueba nombre accesible, rol `switch`, anuncio de checked, navegación de teclado ni área táctil. El 40×20 visual no se interpreta como hit target completo. La fase web deberá definir esos aspectos por separado.

## 14. External Dependencies

Ninguna biblioteca de componente o icono anidado. Foundations/Tokens es dependencia de datos aprobada, no una instancia remota.

## 15. Unresolved Information

La activación real, el comportamiento de labels simultáneas, longitudes extremas y la semántica de Off/Hover no están definidas por la fuente. La ausencia de Press significa fuera del set observado, no prohibición de un futuro producto. Estas lagunas no impiden materializar la representación Figma especificada.

## 16. Implementation Notes

| ID | Regla Figma | Fuerza | Procedencia | QA |
|---|---|---|---|---|
| REQ-TGL-001 | Página exclusiva `Toggles`, set `Toggle`, sin alterar familias existentes. | MUST | Convención semántica delegada | AC-TGL-001 |
| REQ-TGL-002 | Ocho variantes Toggle×State, con default On/Default y ortografía corregida. | MUST | Fuente + normalización explícita | AC-TGL-002 |
| REQ-TGL-003 | Track/Thumb y dos etiquetas opcionales con medidas, posiciones y auto layout especificados. | MUST | Fuente | AC-TGL-003 |
| REQ-TGL-004 | Dos TEXT y dos BOOLEAN enlazadas a los 16 textos. | MUST | Fuente | AC-TGL-004 |
| REQ-TGL-005 | Colores de la matriz, stroke y radio ligados a variables semánticas locales; excepciones Off/Focus declaradas. | MUST | Fuente + JSON + decisión delegada | AC-TGL-005 |
| REQ-TGL-006 | Tipografía, gap y foco tokenizados donde existe variable; sombras sin token específico conservadas. | MUST | Fuente + JSON | AC-TGL-006 |
| REQ-TGL-007 | No añadir reacciones o estados no observados; registrar límite de accesibilidad funcional. | MUST | Fuente | AC-TGL-007 |
| REQ-TGL-008 | Readback, captura, diferencias, estado y auditoría pendiente documentados. | MUST | P05/P06 + delegación | AC-TGL-008 |

| Criterio | Evidencia requerida tras construir |
|---|---|
| AC-TGL-001 | Página y set únicos con IDs reales; otras familias intactas. |
| AC-TGL-002 | 8/8 combinaciones, nombres y defaults exactos. |
| AC-TGL-003 | 8 tracks 40×20, 8 thumbs 16⅔, posiciones y labels opcionales. |
| AC-TGL-004 | 2 TEXT + 2 BOOLEAN, referencias enlazadas en las ocho variantes. |
| AC-TGL-005 | Fills, strokes, radios y pesos ligados por ID; aliases resueltos en cuatro modos. |
| AC-TGL-006 | 16×5 propiedades tipográficas ligadas, gap y efectos focus verificados. |
| AC-TGL-007 | Cero reacciones nuevas, sin afirmación de teclado/web. |
| AC-TGL-008 | Estado, mapa, QA y captura posteriores; `user_audit: PENDING`. |

## 17. Evidence / Confidence

Evidencia directa: set `1230:23858`, propiedades, ocho componentes, 16 etiquetas ocultas, ocho tracks/thumbs, variable bindings y effects, reacciones vacías. Derivación: matriz completa 2×4. Requiere definición: comportamiento de producto y accesibilidad funcional. Confianza alta para representación visual estática, porque el traversal está completo; la captura 680×194 se inspeccionó inline. El cambio de nombres, radio, interlineado y halo claro son decisiones de construcción explícitas y quedarán para auditoría humana.
