# Header · contrato observado de fuente · 0.1.0

Evidencia read-only; no contrato normativo de destino. El YAML adjunto y los snapshots preservan la extracción completa.

## 1. Identidad

```yaml
id: "1349:4907"
key: "5a29f5f658d3b85560303a84f025a92bee503f30"
name: "header"
type: "COMPONENT"
description: null
parent:
  id: "1250:13265"
  name: "Content"
  type: "FRAME"
page:
  id: "268:20243"
  name: "❖ Header ✅"
source:
  url: "https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1349-4907"
  file_key: "9zs5RMR8LB5wHjW9Bd59BA"
  node_id: "1349:4907"
```

## 2. Cobertura de inspección

```yaml
status: "COMPLETE"
read_only: true
traversal:
  discovered_nodes: 110
  inspected_nodes: 110
  pending_nodes: 0
  invisible_nodes_inspected: 6
  truncated: false
  limit: null
mcp_limitations:
  - "Respuestas extensas se dividieron en bloques; preferredValues remotos resumidos por cantidad, no resueltos exhaustivamente."
  - "Biblioteca y versión remotas NOT_EXPOSED_BY_FIGMA_MCP."
```

## 3. Clasificación y dimensiones

```yaml
position:
  x: 32
  y: 32
dimensions:
  width: 1143.69091796875
  height: 96
visible: true
clips_content: false
opacity: 1
blend_mode: "PASS_THROUGH"
```

## 4. Anatomía

```yaml
functional_tree:
  - "header → Logo Categoria + content"
  - "content → Version + Actions + Company + User"
  - "Actions → icon header Amount=5 → cinco Button Icon con iconos activos"
graphical_details_omitted:
  - "Vectores se conservan individualmente en header.source.v0.1.0.json; no se convierten en anatomía pública."
```

## 5. Dependencias

```yaml
components:
  total_instances: 25
  total: 16
  local: 10
  remote: 6
  unknown_locality: 0
  resolved: 16
  partially_resolved: 0
  unresolved: 0
variables:
  total: 35
  local: 30
  remote: 5
  unknown_locality: 0
  resolved: 35
  partially_resolved: 0
  unresolved: 0
styles:
  total: 0
  local: 0
  remote: 0
  unknown_locality: 0
  resolved: 0
  partially_resolved: 0
  unresolved: 0
```

## 6. Propiedades

```yaml
definitions:
  -
    name: "show version#1349:1"
    type: "BOOLEAN"
    defaultValue: true
  -
    name: "show company#1349:5"
    type: "BOOLEAN"
    defaultValue: true
  -
    name: "show icons#1452:16"
    type: "BOOLEAN"
    defaultValue: true
  -
    name: "show avatar#1929:0"
    type: "BOOLEAN"
    defaultValue: true
observed: []
available:
  - "show version#1349:1"
  - "show company#1349:5"
  - "show icons#1452:16"
  - "show avatar#1929:0"
unknown:
  - "No propiedades de texto en el contenedor fuente."
```

## 7. Variantes

```yaml
observed_combinations:
  - "Componente único header"
available_values: []
unknown: []
```

## 8. Estados

```yaml
observed: []
available: []
unknown:
  - "Estados de apertura de selectores no definidos en Header."
```

## 9. Layout

```yaml
root:
  id: "1349:4907"
  name: "header"
  type: "COMPONENT"
  parent: null
  x: 32
  y: 32
  width: 1143.69091796875
  height: 96
  visible: true
  opacity: 1
  clipsContent: false
  layoutMode: "HORIZONTAL"
  layoutWrap: "NO_WRAP"
  layoutSizingHorizontal: "FIXED"
  layoutSizingVertical: "HUG"
  primaryAxisSizingMode: "FIXED"
  counterAxisSizingMode: "AUTO"
  primaryAxisAlignItems: "SPACE_BETWEEN"
  counterAxisAlignItems: "CENTER"
  itemSpacing: 40
  paddingLeft: 24
  paddingRight: 24
  paddingTop: 24
  paddingBottom: 24
  layoutGrow: 0
  layoutAlign: "INHERIT"
  constraints:
    horizontal: "MIN"
    vertical: "MIN"
  fills: []
  strokes: []
  strokeWeight: 1
  strokeAlign: "INSIDE"
  cornerRadius: 0
  effects: []
  boundVariables:
    paddingLeft:
      type: "VARIABLE_ALIAS"
      id: "VariableID:562:13"
    paddingTop:
      type: "VARIABLE_ALIAS"
      id: "VariableID:562:13"
    paddingRight:
      type: "VARIABLE_ALIAS"
      id: "VariableID:562:13"
    paddingBottom:
      type: "VARIABLE_ALIAS"
      id: "VariableID:562:13"
  explicitVariableModes: {}
  reactions: []
  componentPropertyReferences: {}
relationships:
  - "Horizontal SPACE_BETWEEN, padding24, no wrap; contenidos HUG, acciones48 con gap8."
  - "RFC observado188px dentro de contenedor160px."
```

## 10. Apariencia e iconos

```yaml
node:
  fills: []
  strokes: []
  effects: []
descendants:
  - "Degradado Alpha literal #844AEC→#2868FD"
  - "Selector empresa borde de marca; perfil superficie de marca"
icons:
  - "ArrowsCounterClockwise Outline Light"
  - "GraduationCap Outline Light"
  - "Headset Outline Light"
  - "AppWindow Outline Light"
  - "Bell Outline Light"
  - "CaretDown Outline Regular"
  - "CaretDown Stroke Thin"
```

## 11. Tipografía

```yaml
styles: []
text_runs:
  -
    id: "2412:268"
    characters: "2.0.0"
    fontName:
      family: "Manrope"
      style: "Regular"
      variationSettings:
        wght: 400
    fontSize: 16
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: 0
  -
    id: "2412:270"
    characters: "ALPHA .1"
    fontName:
      family: "Manrope"
      style: "Regular"
      variationSettings:
        wght: 400
    fontSize: 16
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: 0
  -
    id: "I2780:11932;1452:35164;1430:18853;1133:31555"
    characters: "1"
    fontName:
      family: "Manrope"
      style: "Bold"
      variationSettings:
        wght: 700
    fontSize: 8
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: -2
  -
    id: "I2780:11932;1452:35184;1430:18853;1133:31555"
    characters: "1"
    fontName:
      family: "Manrope"
      style: "Bold"
      variationSettings:
        wght: 700
    fontSize: 8
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: -2
  -
    id: "I2780:11932;1452:35165;1430:18853;1133:31555"
    characters: "1"
    fontName:
      family: "Manrope"
      style: "Bold"
      variationSettings:
        wght: 700
    fontSize: 8
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: -2
  -
    id: "I2780:11932;1452:35166;1430:18853;1133:31555"
    characters: "1"
    fontName:
      family: "Manrope"
      style: "Bold"
      variationSettings:
        wght: 700
    fontSize: 8
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: -2
  -
    id: "I2780:11932;1452:35167;1430:18853;1133:31555"
    characters: "1"
    fontName:
      family: "Manrope"
      style: "Bold"
      variationSettings:
        wght: 700
    fontSize: 8
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: -2
  -
    id: "I2412:276;1430:18859;1133:31553"
    characters: "1"
    fontName:
      family: "Manrope"
      style: "Bold"
      variationSettings:
        wght: 700
    fontSize: 5.333333492279053
    lineHeight:
      unit: "PERCENT"
      value: 160.0000023841858
    letterSpacing:
      unit: "PERCENT"
      value: -2
  -
    id: "2412:277"
    characters: "Empresa SA de CV"
    fontName:
      family: "Manrope"
      style: "Regular"
      variationSettings:
        wght: 400
    fontSize: 14
    lineHeight:
      unit: "PIXELS"
      value: 20
    letterSpacing:
      unit: "PERCENT"
      value: 0.10000000149011612
  -
    id: "7905:1927"
    characters: "CAC840428RH1"
    fontName:
      family: "Manrope"
      style: "Regular"
      variationSettings:
        wght: 400
    fontSize: 12
    lineHeight:
      unit: "AUTO"
    letterSpacing:
      unit: "PERCENT"
      value: 0
  -
    id: "I3001:3246;1132:21379"
    characters: "JA"
    fontName:
      family: "Manrope"
      style: "SemiBold"
      variationSettings:
        wght: 600
    fontSize: 20
    lineHeight:
      unit: "PERCENT"
      value: 133.00000429153442
    letterSpacing:
      unit: "PERCENT"
      value: -2
```

## 12. Variables y tokens

```yaml
summary:
  total: 35
categories:
  color:
    - "color/text/primary"
    - "color/text/on-brand"
    - "color/border/subtle"
    - "color/icon/primary"
    - "color/feedback/danger/icon"
    - "color/border/on-brand"
    - "color/border/brand"
    - "color/interactive/primary/default"
    - "color/text/brand"
    - "color/text/secondary"
    - "color/surface/brand"
    - "color/feedback/positive/icon"
  font:
    - "font/size/md"
    - "font/weight/regular"
    - "font/family/base"
    - "font/weight/bold"
    - "font/size/sm"
    - "font/size/xs"
    - "font/size/lg"
  spacing:
    - "spacing/xl"
    - "spacing/none"
    - "spacing/sm"
    - "spacing/xs"
    - "spacing/lg"
  radius:
    - "radius/sm"
    - "radius/md"
    - "radius/radius-full"
    - "radius/2xl"
    - "radius/full"
  stroke:
    - "stroke/xs"
    - "stroke/stroke-default"
  logo:
    - "logo/categoria"
source: "variable_dependencies"
```

## 13. Contenido

```yaml
example_content:
  observed_strings:
    - "2.0.0"
    - "ALPHA .1"
    - "1"
    - "1"
    - "1"
    - "1"
    - "1"
    - "1"
    - "Empresa SA de CV"
    - "CAC840428RH1"
    - "JA"
component_rules:
  - "Cuatro booleanas controlan la visibilidad de grupos, no el contenido textual."
truncation_and_wrapping:
  -
    id: "2412:268"
    textAutoResize: "WIDTH_AND_HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "2412:270"
    textAutoResize: "WIDTH_AND_HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "I2780:11932;1452:35164;1430:18853;1133:31555"
    textAutoResize: "WIDTH_AND_HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "I2780:11932;1452:35184;1430:18853;1133:31555"
    textAutoResize: "WIDTH_AND_HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "I2780:11932;1452:35165;1430:18853;1133:31555"
    textAutoResize: "WIDTH_AND_HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "I2780:11932;1452:35166;1430:18853;1133:31555"
    textAutoResize: "WIDTH_AND_HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "I2780:11932;1452:35167;1430:18853;1133:31555"
    textAutoResize: "WIDTH_AND_HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "I2412:276;1430:18859;1133:31553"
    textAutoResize: "NONE"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "2412:277"
    textAutoResize: "HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "7905:1927"
    textAutoResize: "HEIGHT"
    textTruncation: "DISABLED"
    maxLines: null
  -
    id: "I3001:3246;1132:21379"
    textAutoResize: "NONE"
    textTruncation: "DISABLED"
    maxLines: null
```

## 14. Interacción

```yaml
status: "UNDEFINED"
reason: "Header no expone reacciones propias; estados internos pertenecen a dependencias."
rules: []
```

## 15. Semántica y accesibilidad

```yaml
status: "REQUIRES_DEFINITION"
observed:
  - "Acciones48px y selector empresa48px; icono interior32px."
  - "Textos y colores observados, no prueba de accesibilidad web."
undefined:
  - "Nombres accesibles de acciones"
  - "Orden de foco de aplicación"
  - "Destinos y apertura de menús"
```

## 16. Pendientes y notas

```yaml
- "Destinos de acciones, menús y permisos dependen del producto; no se inventan."
- "No regla responsive observada."
```

## 17. Evidencia

```yaml
figma_direct:
  -
    id: "E001"
    source: "sources/figma-snapshots/header.source.v0.1.0.json"
    value: "110/110 nodos inspeccionados"
  -
    id: "E002"
    source: "sources/figma-snapshots/header.dependencies.v0.1.0.json"
    value: "25 instancias,16 mains únicos"
  -
    id: "E003"
    source: "sources/figma-snapshots/header.source-variables.v0.1.0.json"
    value: "35 variables usadas"
derived:
  -
    id: "D001"
    source: "traversal"
    value: "Agrupación anatómica funcional"
requires_definition:
  - "Navegación y semántica de producto"
confidence:
  level: "HIGH"
  reason: "Recorrido completo incluyendo nodos ocultos; sin inferir reglas de producto."
```

