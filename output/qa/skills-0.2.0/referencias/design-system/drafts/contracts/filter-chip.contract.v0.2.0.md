---
contract_schema: sdd-project/0.2
contract_id: FILTER-CHIP-001
name: Filter Chip
type: component
status: IN_REVIEW
version: 0.2.0
owner: null
last_updated: 2026-09-23
review_targets: [figma]
sources: [SRC-FIGMA-FILTER-CHIP-001, DEC-FILTER-CHIP-DIRECTION-001, DEC-ICONS-001]
data_refs: [drafts/contracts/filter-chip.contract.yaml, drafts/contracts/filter-chip.build.v0.2.0.yaml]
dependencies: [PlusCircle, FOUNDATIONS-TOKENS-001]
---

# Filter Chip · candidato 0.2.0 para Figma

Este candidato adopta la descripción del componente fuente y la decisión explícita del usuario de completar sus estados. La inspección original permanece en [filter-chip.contract.yaml](filter-chip.contract.yaml); el modelo determinista de construcción y los IDs de tokens del destino están en [filter-chip.build.v0.2.0.yaml](filter-chip.build.v0.2.0.yaml). La aprobación de esta versión aún está pendiente.

## 1. Purpose

Control visual tipo pill que indica si un filtro está seleccionado dentro de un conjunto pequeño. Ejemplos de etiqueta en la descripción fuente: «Todos», «Pendientes», «Requieren atención». La lógica de selección única o múltiple permanece fuera del alcance Figma.

## 2. Contract

| ID | Regla candidata para Figma | Fuerza | Procedencia | Criterio |
|---|---|---|---|---|
| REQ-FC-001 | Crear un único component set `Filter Chip` en una página exclusiva `Chips` del archivo `AI-Design-System`, sin alterar Buttons. | MUST | Usuario + P04 | AC-FC-001 |
| REQ-FC-002 | Construir exactamente 30 variantes: `size=small/middle/large × selected=false/true × state=default/hover/press/focus/disabled`. | MUST | Description + decisión del usuario + escala Button del destino | AC-FC-002 |
| REQ-FC-003 | Cada variante tendrá auto layout horizontal y la anatomía `Left icon → Label → Right icon`; iconos ocultos por defecto, etiqueta visible. | MUST | Description + anatomía observada | AC-FC-003 |
| REQ-FC-004 | Exponer TEXT `text`, BOOLEAN `show left icon` y `show right icon`, INSTANCE_SWAP `left icon` y `right icon`, y los tres ejes de variante. Defaults: `Chip`, `false`, `false`, PlusCircle, `large`, `false`, `default`. | MUST | Description + convenciones verificadas | AC-FC-004 |
| REQ-FC-005 | Reutilizar la variante remota `PlusCircle / Outline / Light` de Phosphor Icons, key `46d251bb4099700c5852180f2370d265e5166432`, como dependencia de ambos slots. | MUST | DEC-ICONS-001 + lectura del destino | AC-FC-005 |
| REQ-FC-006 | Vincular propiedades visuales a variables locales de `AI-Design-System` por nombre e ID de destino, conservando aliases y cuatro modos. | MUST | Usuario + foundations aprobado + preflight | AC-FC-006 |
| REQ-FC-007 | Aplicar las recetas visuales de la sección States, incluidos 92% y 85% de opacidad del paint inverso para selected hover/press y disabled idéntico entre selecciones. | MUST | Description + observación + decisión | AC-FC-007 |
| REQ-FC-008 | Mantener la etiqueta editable, propiedades booleanas conectadas a la visibilidad e iconos conectados al swap. | MUST | Description + práctica de componentes | AC-FC-008 |
| REQ-FC-009 | Registrar IDs reales, bindings leídos, página, matriz y QA posterior; no atribuir comportamiento web a los estados visuales. | MUST | P04/P05/P06 | AC-FC-009 |

## 3. Anatomy

```text
Chips (PAGE)
└─ Filter Chip (COMPONENT_SET)
   └─ 30 COMPONENTS: size × selected × state
      ├─ Left icon (INSTANCE → Phosphor PlusCircle; hidden by default)
      ├─ Label (TEXT; visible)
      └─ Right icon (INSTANCE → Phosphor PlusCircle; hidden by default)
```

Los iconos permanecen como instancias vinculadas aunque su visibilidad inicial sea `false`.

## 4. Properties

| Nombre destino | Tipo | Default | Conexión |
|---|---|---|---|
| `text` | TEXT | `Chip` | `Label.characters` |
| `show left icon` | BOOLEAN | `false` | `Left icon.visible` |
| `show right icon` | BOOLEAN | `false` | `Right icon.visible` |
| `left icon` | INSTANCE_SWAP | PlusCircle / Outline / Light | `Left icon` |
| `right icon` | INSTANCE_SWAP | PlusCircle / Outline / Light | `Right icon` |
| `size` | VARIANT | `large` | `small`, `middle`, `large` |
| `selected` | VARIANT | `false` | `false`, `true` |
| `state` | VARIANT | `default` | `default`, `hover`, `press`, `focus`, `disabled` |

Los nombres de propiedad siguen la convención minúscula del set Button del destino. Las claves con sufijo `#id` se generan en Figma y deberán registrarse tras la construcción; las claves de origen no se copian.

## 5. Variants

La matriz aprobable es de 30 combinaciones únicas. Cada par `size × selected` contiene los cinco estados. Las 12 variantes `selected=true` no Default de los tres tamaños de destino se crean desde las reglas de la descripción; no se presentan como variantes observadas en el archivo fuente. Las seis variantes fuente `x-small` se conservan como evidencia pero no forman parte de este alcance.

## 6. Sizes

| Destino | Nombre en description | Alto | Icono | Tipografía | Gap | Padding T/R/B/L |
|---|---|---:|---:|---|---:|---|
| `small` | Sm | 32 | 16 | Manrope Medium 12/16 | 4 | 8/12/8/12 |
| `middle` | Md | 40 | 20 | Manrope Medium 14/20 | 4 | 8/12/8/12 |
| `large` | Xl | 48 | 24 | Manrope Medium 16/24 | 8 | 12/16/12/16 |

La correspondencia con Sm/Md/Xl se apoya en alturas y en las opciones `small/middle/large` del Button aprobado en el destino. Se normaliza a 8 px el padding vertical de `middle`: la variante fuente no seleccionada/default usa 4 px, mientras sus otros estados y selected/default usan 8 px. La altura se mantiene en 40 px y el ancho queda en HUG, por lo que los anchos observados con iconos visibles no se fijan como regla.

## 7. States

| selected | state | Fondo | Texto | Icono visible | Anillo |
|---|---|---|---|---|---|
| false | default | `color/interactive/secondary/active` | `color/text/secondary` | `color/icon/secondary` | ninguno |
| false | hover | `color/interactive/secondary/hover` | secundario | secundario | ninguno |
| false | press | `color/interactive/secondary/default` | secundario | secundario | ninguno |
| false | focus | `color/interactive/secondary/active` | `color/text/primary` | `color/icon/primary` | 2 px `color/focus/ring` exterior |
| false | disabled | `color/interactive/disabled/bg` | `color/interactive/disabled/text` | `color/icon/disabled` | ninguno |
| true | default | `color/background/inverse` al 100% | `color/text/on-brand` | `color/icon/on-brand` | ninguno |
| true | hover | `color/background/inverse` al 92% | on-brand | on-brand | ninguno |
| true | press | `color/background/inverse` al 85% | on-brand | on-brand | ninguno |
| true | focus | `color/background/inverse` al 100% | on-brand | on-brand | 2 px `color/focus/ring` exterior |
| true | disabled | idéntico a false/disabled | disabled | disabled | ninguno |

La opacidad modifica el paint enlazado; no reemplaza la variable por un color literal. `selected=true/focus` combina el aspecto selected/default y el anillo focus observado en la otra rama: es una regla derivada para revisión humana.

## 8. Behavior

Estos estados son representaciones visuales. No se define ni se certifica una transición de prototipo, navegación, exclusividad de filtros, eventos o deselección.

## 9. Accessibility

El texto visible constituye la etiqueta visual y focus usa anillo exterior. Rol accesible, nombre, teclado, contraste, área táctil y comportamiento Disabled requieren especificación de producto/web; no se declaran validados por el archivo Figma.

## 10. Design tokens

Se reutilizan variables `semantic` locales existentes del destino, con modos Contable, Administrativo, Servicios y Personas. El mapa de 26 tokens observados y dos tokens semánticos adicionales para familia/peso tipográfico figura en [el modelo de construcción](filter-chip.build.v0.2.0.yaml). Todos los aliases permanecen en las variables existentes del destino; los componentes vinculan sus IDs de destino. No se crean colecciones ni variables nuevas.

## 11. Content rules

`Chip` es el texto inicial editable. No se establecen máximo, truncamiento, localización ni icon-only. El uso de un chip sin etiqueta queda fuera de este contrato.

## 12. Composition rules

Auto layout horizontal con alineación centrada, ancho HUG, altura según tamaño, radius/full y bindings de spacing. Cada icono conserva 16/20/24 px según tamaño y su key Phosphor. No se crean variantes por icono.

## 13. Responsive behavior

La anchura acompaña el texto en HUG; no se especifican breakpoints, ancho completo ni wrapping. Se comprueba que un texto distinto de `Chip` no recorte el contenido.

## 14. Edge cases

Ambos iconos ocultos es la referencia inicial; cualquiera puede activarse independientemente. `selected=true/disabled` es visualmente idéntico a `selected=false/disabled`. Etiquetas largas o sin texto requieren una decisión posterior de producto.

## 15. Forbidden combinations

Ninguna de las 30 combinaciones de ejes está prohibida. `x-small` queda fuera del alcance de esta versión y no se convierte en una prohibición general.

## 16. Design ↔ Code mapping

Los nombres Figma definidos aquí no establecen props React. Los estados son ejes visuales. La implementación web, teclado y accesibilidad funcional requieren otro contrato.

## 17. Acceptance criteria

| ID | REQ | Comprobación de lectura posterior |
|---|---|---|
| AC-FC-001 | 001 | Archivo, página `Chips` única y set principal con IDs reales; Buttons intacta. |
| AC-FC-002 | 002 | 30 nombres únicos, producto cartesiano completo 3×2×5. |
| AC-FC-003 | 003 | Tres hijos por variante, orden y tipos exactos, auto layout horizontal e iconos ocultos por defecto. |
| AC-FC-004 | 004 | Definiciones y defaults de ocho propiedades del set. |
| AC-FC-005 | 005 | 60 instancias con key Phosphor exacta; sin detach. |
| AC-FC-006 | 006 | Readback de cada binding obligatorio por ID de destino y colección/modo; sin colores literales sustitutos. |
| AC-FC-007 | 007 | Por estado: variable de fondo/texto/icono, opacidad y anillo; lectura de 30 variantes y captura visual. |
| AC-FC-008 | 008 | Referencias de propiedad TEXT/BOOLEAN/INSTANCE_SWAP conectadas a los tres hijos. |
| AC-FC-009 | 009 | Diario, mapa de IDs y QA de implementación; sin afirmación de comportamiento web. |

## 18. Examples

- `size=small, selected=false, state=default`: referencia sin iconos.
- `size=middle, selected=true, state=hover`: fondo inverso enlazado al 92%.
- `size=large, selected=true, state=disabled`: mismo tratamiento visual que `selected=false/disabled`.

## 19. Source of truth

La descripción exacta del set fuente `8203:10` y el snapshot de la inspección sustentan la familia y su baseline observado. [DEC-FILTER-CHIP-DIRECTION-001](../../registry/decisions.md) adopta la descripción y pide completar variantes. [DEC-ICONS-001](../../registry/decisions.md) fija Phosphor Icons. El contrato aprobado de foundations gobierna los tokens existentes del destino. Este documento aún necesita aprobación explícita de su versión `0.2.0` y digest antes de P04.

## 20. Change management

El candidato 0.1.0 se conserva como registro de la contradicción fuente. Esta revisión propone decisiones de construcción sin modificar el archivo fuente ni el inventario observado. Cualquier cambio normativo posterior requiere nueva versión y QA documental.

## 21. Changelog

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-09-23 | Baseline observacional, 24 variantes; conflictos registrados. |
| 0.2.0 | 2026-09-23 | Candidato para destino: 30 variantes, tres tamaños, iconos ocultos, estados selected completos y tokens propios. |

Revisión documental: [filter-chip.v0.2.0.review.md](../../qa/contracts/filter-chip.v0.2.0.review.md). Plan de construcción: [filter-chip.v0.2.0.plan.md](../reports/filter-chip.v0.2.0.plan.md). Texto exacto de Description: [filter-chip.description.v0.2.0.md](../figma/filter-chip.description.v0.2.0.md).
