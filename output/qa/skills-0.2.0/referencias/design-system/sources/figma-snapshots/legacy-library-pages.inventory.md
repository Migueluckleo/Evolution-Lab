# Inventario inicial de páginas de componentes · Libreria v1.1.0

- **Fuente:** [archivo Figma anterior](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=7339-129&t=sZOrF8YSnEjHSpdU-1), file key `9zs5RMR8LB5wHjW9Bd59BA`.
- **Nodo del enlace:** página `7339:129`, `WIP Chips`; el enlace no selecciona la raíz `Document` ni limita la solicitud a Chips. Se listaron las páginas del archivo mediante Plugin API read-only.
- **Lectura:** 2026-09-23. Se consultaron metadatos de las 28 páginas situadas bajo la sección visual `--- Components ---`; el conteo de `symbol` procede del XML de metadatos de cada página y es **preliminar**, no un traversal profundo ni un conteo definitivo de component sets. Los nombres de página con `✅`/`WIP` son etiquetas observadas, no estados de aprobación del proyecto.
- **Cobertura:** 28 páginas, 748 nodos `symbol` en metadatos. Buttons (60) y Chips (24) ya tienen contratos e implementación de destino; quedan 26 páginas para clasificación y extracción. Algunas páginas contienen varias familias internas; el número de contratos puede ser mayor que 26. La página Logos podría corresponder a assets, no a una familia UI; requiere clasificación antes de construir.

| Página observada | Page ID fuente | `symbol` en metadatos | Candidatos internos o nota |
|---|---|---:|---|
| Avatar | `1132:8891` | 12 | Avatar |
| Badge | `1234:53606` | 6 | Badge |
| Buttons | `0:1` | 60 | Ya documentado y validado en destino |
| WIP Chips | `7339:129` | 24 | Fuente de Filter Chip ya documentada; destino tiene 30 variantes aprobadas |
| Buttons icon | `1430:18021` | 30 | Icon button; posible familia propia |
| Breadcrumb | `1098:28190` | 10 | Breadcrumb |
| Cards | `258:130806` | 8 | Metric card |
| Chart | `268:20756` | 23 | Varias familias internas por clasificar |
| Checkbox | `1144:34368` | 12 | Checkbox |
| Dot | `1133:20620` | 15 | Dot |
| Header | `268:20243` | 6 | Header e icon header |
| Inline Notifications | `1241:55464` | 5 | Inline notification |
| Navigation | `268:20245` | 26 | Item/tab, item/switch tab y pagination |
| Input Field | `20:3` | 52 | Input, search, text area y file upload |
| Select | `268:20247` | 18 | Dropdown e item |
| Radio button | `1144:34653` | 8 | Radio button |
| Table | `1669:25885` | 43 | Table/cell item y subpartes |
| Logos | `40:93` | 72 | Assets de marca; clasificación pendiente |
| Linear Progress Bar | `7568:47417` | 48 | Linear progress bar |
| Modal | `4886:869` | 13 | Modal y subpartes |
| Multi Step Indicator | `2166:596` | 26 | Steppers y progress line |
| Loader | `3917:1263` | 112 | Varios tamaños y subfamilias por clasificar |
| Toggle | `1084:7229` | 8 | Toggle |
| Sidebar | `268:20244` | 25 | Menu item y menu |
| Scrollbar | `3910:928` | 30 | Scrollbar y subpartes |
| Steps | `7861:714` | 37 | Steps |
| Tooltip | `2599:10321` | 4 | Tooltip |
| Empty states | `3027:406` | 15 | Empty states y placeholders |

## Límite de este inventario

Los metadatos solo exponen jerarquía resumida. No acreditan propiedades, bindings, variables, visibilidad interna, interacciones, taxonomía final ni completitud del conjunto de variantes. Cada contrato requiere inspección read-only del component set real, su contexto visual y dependencias. Los nombres semánticos de páginas del destino se fijarán por contrato y se compararán con las páginas ya existentes; no se copian sin más los prefijos, emojis, marcas WIP o nombres internos del archivo antiguo.
