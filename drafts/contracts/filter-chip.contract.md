---
contract_schema: sdd-project/0.2
contract_id: FILTER-CHIP-001
name: Filter Chip
type: component
status: DRAFT
version: 0.1.0
owner: null
last_updated: 2026-09-23
review_targets: [figma]
sources: [SRC-FIGMA-FILTER-CHIP-001]
data_refs: [drafts/contracts/filter-chip.contract.yaml]
dependencies: [PlusCircle]
---

# Filter Chip

> Contrato candidato generado desde evidencia Figma de solo lectura. No es código de aplicación, no sustituye definiciones de producto o accesibilidad y no autoriza construcción. El estado permanece `DRAFT` por tres conflictos materiales en la fuente.

## Alcance de la revisión

Este candidato cubre el component set `Filter Chip` (`8203:10`) del archivo fuente `Libreria v1.1.0`, sus 24 variantes observadas, 48 instancias activas de `PlusCircle`, 24 etiquetas, 26 variables usadas y cero estilos nombrados. El destino previsto sigue siendo `AI-Design-System` (`tj3WIBEZDGLVs7MJWKCwgf`), pero no fue leído ni modificado en esta fase. Web queda fuera del alcance.

## 1. Purpose

**Observed from Figma.** La descripción del set lo presenta como un control tipo pill para alternar filtros. Esa descripción es evidencia explícita del campo `description`, no una definición aprobada de producto.

**Requires definition.** Deben confirmarse semántica, selección única o múltiple, deselección, navegación, activación, persistencia y relación con el conjunto de filtros.

## 2. Contract

| ID | Requisito candidato | Fuerza | Procedencia | Fuente/localizador | Criterio |
|---|---|---|---|---|---|
| REQ-FC-001 | La familia reproduce únicamente las 24 combinaciones observadas mientras no se resuelva `CONFLICT-FC-003`. | MUST | OBSERVED | `SRC-FIGMA-FILTER-CHIP-001`, hijos directos | AC-FC-001 |
| REQ-FC-002 | Cada variante conserva el orden `Left icon → Label → Right icon` en auto layout horizontal. | MUST | OBSERVED | 24 componentes, tres hijos directos | AC-FC-002 |
| REQ-FC-003 | Las propiedades nativas y sus claves se preservan sin renombrarlas durante reconstrucción. | MUST | OBSERVED | `componentPropertyDefinitions` | AC-FC-003 |
| REQ-FC-004 | Los bindings de variables conservan ID/key/nombre y valor resuelto; el literal no sustituye al token. | MUST | OBSERVED | 26 variables resueltas | AC-FC-004 |
| REQ-FC-005 | Las instancias activas de icono conservan `PlusCircle`, `Format=Outline`, `Weight=Light`, salvo decisión posterior sobre swaps. | MUST | OBSERVED | 48 instancias | AC-FC-005 |
| REQ-FC-006 | No se implementa comportamiento interactivo, teclado o accesibilidad no definido por la fuente. | MUST NOT | UNRESOLVED | `reactions=[]`; sin contrato de producto | AC-FC-006 |

## 3. Anatomy

**Observed from Figma**

```text
Filter Chip (COMPONENT_SET)
└─ Variant (COMPONENT) × 24
   ├─ Left icon (INSTANCE → PlusCircle)
   │  └─ Vector
   ├─ Label (TEXT)
   └─ Right icon (INSTANCE → PlusCircle)
      └─ Vector
```

| Parte | Nodo/rol observado | Presencia observada | Exposición |
|---|---|---|---|
| Icono izquierdo | `Left icon` | Visible en 24/24 | Boolean `Show left icon#8203:31` + swap `Left icon#8203:93` |
| Etiqueta | `Label` | Presente en 24/24 | Text `Text#8203:0` |
| Icono derecho | `Right icon` | Visible en 24/24 | Boolean `Show right icon#8203:62` + swap `Right icon#8203:124` |

Los vectores internos se omiten de la anatomía funcional y se documentan mediante la dependencia `PlusCircle`.

## 4. Properties

| Propiedad Figma | Tipo | Default API | Valores disponibles / referencia | Estado |
|---|---|---:|---|---|
| `Text#8203:0` | TEXT | `Chip` | Texto libre; límites no definidos | AVAILABLE |
| `Show left icon#8203:31` | BOOLEAN | `true` | `true`, `false` | CONFLICT con description |
| `Show right icon#8203:62` | BOOLEAN | `true` | `true`, `false` | CONFLICT con description |
| `Left icon#8203:93` | INSTANCE_SWAP | `3717:1976` | 1512 candidatos preferidos; resolución profunda fuera de alcance | AVAILABLE |
| `Right icon#8203:124` | INSTANCE_SWAP | `3717:1976` | 1512 candidatos preferidos; resolución profunda fuera de alcance | AVAILABLE |
| `Size` | VARIANT | `large` | `x-small`, `small`, `middle`, `large` | AVAILABLE |
| `Selected` | VARIANT | `false` | `false`, `true` | AVAILABLE |
| `State` | VARIANT | `Default` | `Default`, `Hover`, `Press`, `Focus`, `Disabled` | AVAILABLE |

## 5. Variants

**Observed from Figma.** Existen 24 combinaciones, no las 40 del producto cartesiano:

- `Selected=false`: cuatro tamaños × cinco estados = 20 variantes.
- `Selected=true`: cuatro tamaños × `State=Default` = 4 variantes.
- No se observaron `Selected=true` con `Hover`, `Press`, `Focus` o `Disabled`.

La ausencia no prueba por sí sola que las 16 combinaciones sean inválidas; el campo description afirma lo contrario. La decisión queda bloqueada por `CONFLICT-FC-003`.

## 6. Sizes

| Size | Alto | Ancho observado con “Chip” e iconos | Iconos | Tipografía | Gap | Padding T/R/B/L |
|---|---:|---:|---:|---|---:|---|
| `x-small` | 24 px | 75 px | 12 px | Manrope Medium 12 / AUTO | 4 | 4/8/4/8 |
| `small` | 32 px | 91 px | 16 px | Manrope Medium 12/16 | 4 | 8/12/8/12 |
| `middle` | 40 px | 103 px | 20 px | Manrope Medium 14/20 | 4 | Default no seleccionado: 4/12/4/12; demás observadas: 8/12/8/12 |
| `large` | 48 px | 131 px | 24 px | Manrope Medium 16/24 | 8 | 12/16/12/16 |

Los anchos son resultado observado de contenido y auto layout `HUG`, no anchos universales fijos.

## 7. States

| Estado | Tratamiento observado para `Selected=false` | Interacción demostrada |
|---|---|---|
| Default | Fondo `color/interactive/secondary/active`; texto secundario | Ninguna reacción |
| Hover | Fondo `color/interactive/secondary/hover`; texto secundario | Ninguna reacción |
| Press | Fondo `color/interactive/secondary/default`; texto secundario | Ninguna reacción |
| Focus | Fondo active, anillo exterior 2 px `color/focus/ring`, texto/icono primary | Ninguna reacción |
| Disabled | Fondo disabled, texto/icono disabled | Ninguna reacción |
| Selected + Default | Fondo inverse; texto/icono on-brand | Ninguna reacción |

## 8. Behavior

`interactions.status: UNDEFINED`. Las 24 variantes y el set exponen cero `reactions`. Los nombres `Hover`, `Press`, `Focus` y `Disabled` acreditan tratamientos visuales, no lógica de eventos, navegación, teclado ni supresión de eventos.

## 9. Accessibility

**Observed from Figma.** Hay etiqueta visible editable y variantes Focus con anillo exterior de 2 px.

**Requires definition.** Rol, nombre accesible cuando se oculten etiquetas, semántica de selección, teclado, foco, estados anunciados, área mínima, contraste y conformidad WCAG.

## 10. Design tokens

Las 26 variables usadas pertenecen a la colección local `semantic`, con cuatro modos (`Contable`, `Administrativo`, `Servicios`, `Personas`). Los valores aquí descritos fueron resueltos en `Contable`; la referencia semántica es primaria.

| Categoría | Variables usadas |
|---|---|
| Color | `color/background/inverse`, `color/focus/ring`, `color/icon/{disabled,on-brand,primary,secondary}`, `color/interactive/disabled/{bg,text}`, `color/interactive/secondary/{active,default,hover}`, `color/text/{on-brand,primary,secondary}` |
| Tipografía | `font/size/{xs,sm,md}`, `font/line-height/{xs,sm,md}` |
| Dimensión | `radius/full`, `spacing/{xs,sm,md,lg}`, `stroke/md` |

La lista completa con IDs, keys, valores resueltos y `used_by` vive en [filter-chip.contract.yaml](filter-chip.contract.yaml).

## 11. Content rules

`Chip` es contenido de ejemplo y default de la propiedad TEXT. No se definieron longitud máxima, truncamiento, wrapping, localización, singular/plural ni reglas editoriales.

## 12. Composition rules

Cada variante usa auto layout horizontal, alineación centrada y tres hijos en el orden observado. Los iconos son instancias del set remoto `PlusCircle`, variante `Format=Outline, Weight=Light`. No se resolvieron profundamente los 1512 candidatos preferidos de cada swap.

## 13. Responsive behavior

El ancho de variante está en `HUG`; los iconos son `FIXED` y la etiqueta `HUG`. No se observaron breakpoints, wrapping o full width. `x-small` usa alto en `HUG`; los demás tamaños observados usan alto fijo.

## 14. Edge cases

| Caso | Resultado | Estado |
|---|---|---|
| Ambos iconos ocultos | No inspeccionado como variante renderizada; propiedades booleanas disponibles | UNRESOLVED |
| Texto largo/localizado | Sin límites ni wrapping definidos | UNRESOLVED |
| `Selected=true` con estado no Default | Descripción y estructura se contradicen | CONFLICT |
| Disabled seleccionado | La descripción afirma equivalencia visual, pero la variante no existe | CONFLICT |

## 15. Forbidden combinations

No se declara ninguna combinación prohibida. Las 16 combinaciones ausentes no se convierten en prohibiciones sin decisión humana.

## 16. Design ↔ Code mapping

| Contrato | Figma observado | Web | Límite |
|---|---|---|---|
| Texto | TEXT component property | UNRESOLVED | No hay API web aprobada |
| Visibilidad de iconos | Dos BOOLEAN properties | UNRESOLVED | Defaults en conflicto con description |
| Iconos | Dos INSTANCE_SWAP properties | UNRESOLVED | Alternativas no enumeradas profundamente |
| Tamaño/selección/estado | Tres VARIANT properties | UNRESOLVED | Combinaciones incompletas y conflictivas |

## 17. Acceptance criteria

| ID | REQ | Alcance | Comprobación | Evidencia requerida |
|---|---|---|---|---|
| AC-FC-001 | REQ-FC-001 | Figma | Contar exactamente las combinaciones aprobadas después de resolver conflicto | Readback de component set |
| AC-FC-002 | REQ-FC-002 | Figma | Verificar tres hijos, orden, tipos y auto layout en cada variante | Traversal completo |
| AC-FC-003 | REQ-FC-003 | Figma | Comparar claves/tipos/defaults de propiedades | Readback Plugin API |
| AC-FC-004 | REQ-FC-004 | Figma | Reconciliar 26 bindings por identidad y modo | Readback de variables |
| AC-FC-005 | REQ-FC-005 | Figma | Cotejar keys de componente y set de las 48 instancias | Readback de dependencias |
| AC-FC-006 | REQ-FC-006 | Figma/web | Confirmar que no se certifica conducta ausente | QA documental |

## 18. Examples

- Observado: `Size=large, Selected=false, State=Focus`.
- Observado: `Size=x-small, Selected=true, State=Default`.
- No observado y no declarado inválido: `Size=small, Selected=true, State=Hover`.

## 19. Source of truth

| Fuente | Localizador | Snapshot | Rol |
|---|---|---|---|
| `SRC-FIGMA-FILTER-CHIP-001` | Archivo `9zs5RMR8LB5wHjW9Bd59BA`, nodo `8203:10` | 2026-09-23T15:11:23Z | Evidencia observacional; no aprobada |

Aprobación pendiente. La fuente Figma no se modificó. Este contrato no está publicado en `specs/`.

## 20. Change management

Toda resolución de los conflictos cambiará requisitos y exige una nueva revisión del candidato. La futura construcción deberá registrar IDs de destino separados de los IDs de origen.

## 21. Changelog

| Versión | Fecha | Cambio | Fuente |
|---|---|---|---|
| 0.1.0 | 2026-09-23 | Primer candidato desde inspección read-only | `SRC-FIGMA-FILTER-CHIP-001` |

## Anexo de revisión

- Reporte: [filter-chip.synthesis.md](../reports/filter-chip.synthesis.md)
- QA documental: [filter-chip.review.md](../../qa/contracts/filter-chip.review.md)
- Conflictos: `CONFLICT-FC-001` a `CONFLICT-FC-003`
- Graphify: índice consultado; no actualizado. Su estado queda `STALE` respecto de estos nuevos artefactos.
