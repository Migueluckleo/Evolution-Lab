# Ajustes aplicados a `tokens.inventory.corrected.json`

## Propósito

Este documento registra los ajustes realizados a partir de la auditoría semántica de `tokens.inventory.enriched.json`.

La corrección se hizo con un criterio conservador: **solo se modificaron anomalías demostrables por la estructura del inventario o por bindings observables en el archivo de Figma**. No se introdujeron nuevos tokens, nuevas escalas, nuevos modos ni sintaxis de código inferida.

El archivo de Figma original **no fue modificado** en esta entrega. Los cambios están reflejados únicamente en `tokens.inventory.corrected.json`.

## Resumen de cambios aplicados

| Tipo | Cantidad |
|---|---:|
| Variables totales | 270 |
| Renombres | 1 |
| Variables con scopes ajustados | 7 |
| Alias corregidos | 1 |
| Descripciones refinadas adicionalmente | 2 |
| IDs modificados | 0 |
| Variables creadas o eliminadas | 0 |
| Modos creados, eliminados o renombrados | 0 |
| `codeSyntax` modificados | 0 |

## Ajustes realizados

### 1. `font/size/1xl` → `font/size/2xs`

**ID preservado:** `VariableID:5401:77`

**Antes**
- Nombre: `font/size/1xl`
- Alias: `font/size/10`

**Después**
- Nombre: `font/size/2xs`
- Alias: sin cambios

**Motivo**

La secuencia semántica existente continúa como `xs → sm → md → lg → xl → 2xl...`. El token de 10 se encuentra inmediatamente antes de `xs` y `1xl` rompe el orden semántico de esa escala. Se corrigió únicamente el nombre y su descripción; el ID y el alias permanecen intactos.

**Impacto a considerar:** este es el único cambio potencialmente disruptivo para integraciones que consuman variables por **nombre** en lugar de ID.

---

### 2. `font/weight/*`: scope `ALL_SCOPES` → `FONT_STYLE`

Variables afectadas:

- `font/weight/regular`
- `font/weight/medium`
- `font/weight/semibold`
- `font/weight/bold`

**Motivo**

La auditoría inicial detectó un scope excesivamente amplio. Una revisión de bindings reales en Figma confirmó que estas variables STRING están enlazadas a la propiedad `fontStyle` de nodos de texto (`boundVariables.fontStyle`). Por ello, `FONT_STYLE` expresa el uso real y reduce ambigüedad para diseñadores y agentes.

Los valores, aliases e IDs no cambiaron.

---

### 3. `color/border/subtle` en modo `Servicios`

**Token:** `VariableID:2849:196129`

**Antes**
- `Contable` → `color/blue/200`
- `Administrativo` → `color/green/200`
- `Servicios` → `color/red/200`
- `Personas` → `color/purple/200`

**Después**
- `Contable` → `color/blue/200`
- `Administrativo` → `color/green/200`
- `Servicios` → `color/orange/200`
- `Personas` → `color/purple/200`

**Nuevo alias en Servicios:** `VariableID:2496:179`

**Motivo**

El patrón de los cuatro modos usa el nivel `200` de la familia cromática asociada a cada producto. `Servicios` es el único modo que rompía ese patrón al usar rojo, mientras el resto de sus tokens de marca utilizan la familia naranja. La corrección conserva nivel, intención y estructura del patrón, cambiando únicamente el alias anómalo.

---

### 4. `color/interactive/disabled/bg`

**ID:** `VariableID:2988:16`

**Antes**
```json
"scopes": ["TEXT_FILL"]
```

**Después**
```json
"scopes": ["FRAME_FILL", "SHAPE_FILL"]
```

**Motivo**

El nombre e intención corresponden a un fondo, y la inspección de Figma confirmó usos reales como `boundVariables.fills` sobre componentes en estado disabled. `TEXT_FILL` no representa el uso observado.

El color y sus aliases permanecen sin cambios.

---

### 5. `color/interactive/primary/hover`

**ID:** `VariableID:2988:9`

**Antes**
```json
"scopes": ["SHAPE_FILL"]
```

**Después**
```json
"scopes": ["FRAME_FILL", "SHAPE_FILL"]
```

### 6. `color/interactive/primary/active`

**ID:** `VariableID:2988:10`

**Antes**
```json
"scopes": ["SHAPE_FILL"]
```

**Después**
```json
"scopes": ["FRAME_FILL", "SHAPE_FILL"]
```

**Motivo de ambos ajustes**

Los estados `hover` y `active` pertenecen a la misma familia que `color/interactive/primary/default`, que ya admite ambos scopes. Además, la inspección de los componentes Button confirmó que `hover` y `active` están ligados a `fills` de nodos `COMPONENT`. Se añadió `FRAME_FILL` para reflejar ese uso real y mantener consistencia entre estados.

No se modificaron valores ni aliases.

---

### 7. `color/background/overlay`: descripción precisada

**ID:** `VariableID:2849:196115`

No se cambió su scope ni su alias.

La auditoría original señalaba que el JSON por sí solo no demostraba cómo se componía la opacidad. Se inspeccionaron consumidores reales en la página Modal y el token aparece ligado a fills de `FRAME` con `opacity: 1` tanto en el nodo como en el paint.

La descripción canónica ahora evita sugerir transparencia implícita y documenta que los consumidores auditados lo usan como fill opaco.

---

## Observaciones auditadas que NO se modificaron

### `color/feedback/*/icon`

La auditoría detectó una diferencia de scopes:

- positive / warning / danger: `FRAME_FILL`, `SHAPE_FILL`
- information: `SHAPE_FILL`

Se revisaron bindings reales. Los cuatro tokens se usan en fills de vectores en Inline Notifications, mientras `danger/icon` además aparece aplicado a fills de instancias en Buttons icon. La asimetría actual tiene evidencia de uso y **no se normalizó por apariencia**.

### `color/brand/complementary`

Se conserva `ALL_SCOPES`.

La auditoría lo marcó como scope demasiado amplio, pero no se encontró evidencia suficiente en los consumidores revisados para determinar un conjunto de scopes más preciso sin inferir intención.

### `logo/categoria`

Se conserva:

- `Contable` → `contable`
- `Administrativo` → `comercial`
- `Servicios` → `servicios`
- `Personas` → `personas`

La diferencia entre el nombre del modo `Administrativo` y el valor `comercial` puede representar un contrato de producto deliberado. Sin una fuente externa que lo contradiga, modificarlo sería especulativo.

### `color/background/overlay`

No se creó un token de opacidad ni se alteró su color. La auditoría de consumidores demuestra fill opaco, pero no justifica inventar una nueva arquitectura de composición.

### `codeSyntax`

Permanece vacío en las 270 variables.

No existe en el inventario una fuente autoritativa que permita definir nombres de CSS, JavaScript, React, Android o iOS sin inventarlos. Este campo debe completarse cuando exista un contrato de implementación explícito.

---

## Validación de integridad

Se validó el archivo corregido completo después de aplicar los ajustes:

- Colecciones: **2**
- `primitive`: **141 variables**
- `semantic`: **129 variables**
- Total: **270 variables**
- Aliases `VARIABLE_ALIAS`: **512**
- Aliases rotos: **0**
- IDs modificados: **0**
- Variables añadidas: **0**
- Variables eliminadas: **0**
- Estructura de colecciones: sin cambios
- Modos e IDs de modo: sin cambios
- Valores primitive: sin cambios
- `codeSyntax`: sin cambios
- `fileKey`: sin cambios

### Cambios estructurales intencionales

1. Un nombre semántico: `font/size/1xl` → `font/size/2xs`.
2. Siete conjuntos de scopes.
3. Un alias semántico en un único modo: `color/border/subtle`, modo `Servicios`.
4. Dos descripciones canónicas refinadas.

### SHA-256 de serialización canónica

- Antes de correcciones: `337b42bb676b2e771272bc3858e1655109e1b867fa6f5760cb7e2af0573912f9`
- Después de correcciones: `d64892320747c12a82a92df684aa42464646914f8a93392c61abde630b96fb7e`

Los hashes difieren porque esta entrega contiene cambios estructurales explícitamente autorizados y documentados.

## Resultado

`tokens.inventory.corrected.json` representa la versión corregida del inventario enriquecido. Los cambios aplicados responden a anomalías verificables de naming, alias o scope. Las observaciones que todavía requieren una decisión de producto o una fuente externa permanecen intactas para evitar que una corrección se convierta en una suposición.
