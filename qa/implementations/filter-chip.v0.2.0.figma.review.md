# QA-FILTER-CHIP-FIGMA-001 · Filter Chip 0.2.0 en Figma

```yaml
qa_id: QA-FILTER-CHIP-FIGMA-001
review_type: IMPLEMENTATION_REVIEW
contract_ref: FILTER-CHIP-001
contract_version: 0.2.0
contract_digest: 325a408cfa6a5880c2136aee89a448e9ab3a6d928199543d946d6ae3a52a6cb8
build_model_digest: 40e9e3464b86560255c185bf893518dea2a445170678fa797c8ff6925218e48c
implementation_ref: IMP-FILTER-CHIP-FIGMA-001
target: figma
scope: Filter Chip estructural y visual en AI-Design-System; excluye web, lógica de producto y publicación de biblioteca
blocked_items: []
accepted_deviations: []
reviewer: Codex
executed_at: 2026-09-23
result: PASS
```

## Resultado

La implementación se leyó de vuelta después de la última corrección visual y de configurar los swaps. El archivo `AI-Design-System` (`tj3WIBEZDGLVs7MJWKCwgf`) contiene dos páginas: `Buttons` (`0:1`) con el set `26:81` y 60 variantes, y `Chips` (`67:122`) con el único set `Filter Chip` (`72:298`). El set está `UNPUBLISHED`: este resultado acredita el archivo Figma, no su distribución como biblioteca de equipo.

| Criterio | Resultado | Evidencia de lectura posterior |
|---|---|---|
| AC-FC-001 | PASS | Página exclusiva `Chips` `67:122`, un único nodo superior `72:298`; Buttons retuvo página `0:1`, set `26:81` y 60 variantes. |
| AC-FC-002 | PASS | 30 variantes únicas; producto completo `small/middle/large × false/true × default/hover/press/focus/disabled`, sin faltantes o extras. `x-small` fuera del alcance aprobado. |
| AC-FC-003 | PASS | Las 30 variantes tienen tres hijos directos en orden `Left icon` INSTANCE, `Label` TEXT, `Right icon` INSTANCE, auto layout horizontal, iconos ocultos por defecto, 30 etiquetas visibles y anchos HUG. |
| AC-FC-004 | PASS | Ocho definiciones: TEXT `text=Chip`, BOOLEAN `show left icon=false` y `show right icon=false`, dos INSTANCE_SWAP con default `26:3`, y ejes size/selected/state con defaults `large/false/default`. `defaultVariant` es `size=large, selected=false, state=default` (`70:122`). |
| AC-FC-005 | PASS | 60 instancias conservan main component key `46d251bb4099700c5852180f2370d265e5166432` de Phosphor PlusCircle / Outline / Light. Ambos swaps tienen el mismo catálogo de 1512 component sets Phosphor preferidos, con sus 60 referencias conectadas. |
| AC-FC-006 | PASS | Readback exhaustivo de fills, texto, vectores de icono, radio, gap y cuatro paddings en las 30 variantes: bindings por ID local según modelo aprobado. Los 28 tokens usados se resolvieron en los cuatro modos (`112/112` pares token×modo); los 126 paints inspeccionados tienen binding y RGB de respaldo coherente con Contable. |
| AC-FC-007 | PASS | Diez recetas de estado aplicadas en tres tamaños. Seis selected+hover/press usan `color/background/inverse` enlazado al 92%/85%; seis focus tienen anillo exterior 2 px con `color/focus/ring` y los cuatro lados vinculados a `stroke/md`. Disabled seleccionado y no seleccionado comparten tokens. [Captura final](../../implementations/figma/filter-chip.v0.2.0.png) de 780×508, SHA-256 bytes `0a37beae3477782d77020eea80d1c0da0fa23a760c8713bcd52bc75247baada8`, revisada sin texto recortado o solapamientos aparentes. |
| AC-FC-008 | PASS | Las 30 etiquetas enlazan `characters` con TEXT; las 60 instancias enlazan `visible` y `mainComponent` con BOOLEAN e INSTANCE_SWAP respectivos. La etiqueta inicial es `Chip` en 30/30. |
| AC-FC-009 | PASS | [Mapa y diario](../../implementations/figma/filter-chip.v0.2.0.state.json) con IDs reales; Description rica coincide exactamente con el [texto aprobado](../../drafts/figma/filter-chip.description.v0.2.0.md) entre marcadores. Figma deriva automáticamente `description` de texto plano y quita la sintaxis Markdown. No se atribuye comportamiento web. |

## Validación visual y corrección

La primera captura detectó 15 paints cuyo RGB de respaldo seguía en negro pese a tener el binding correcto: seis fondos `color/interactive/secondary/active` y nueve etiquetas `color/text/secondary`. Se corrigieron con los valores resueltos de las variables locales, conservando sus IDs vinculados. Un readback posterior confirmó cero discrepancias de color en los 126 paints inspeccionados y la captura final muestra fondos y etiquetas legibles. La primera asignación de opacidad de los seis estados selected hover/press fue normalizada a 100% por Figma; se reestableció sobre el paint ya enlazado y se leyó de vuelta 92%/85% con el token intacto.

El primer grid colocaba `small` arriba a la izquierda y Figma lo elegía como default. Se reordenaron las filas para colocar `large/false/default` en esa posición; el readback confirmó tanto `defaultVariant` como el default `size=large`.

## Límites

La revisión cubre la representación y los bindings del archivo Figma. No acredita selección funcional, teclado, área táctil, contraste WCAG o frontend. `get_metadata` mostró temporalmente una lista de páginas anterior después de crear Chips; las lecturas directas posteriores mediante Plugin API confirmaron ambas páginas, IDs y contenido. No se ejecutó publicación de biblioteca de equipo.
