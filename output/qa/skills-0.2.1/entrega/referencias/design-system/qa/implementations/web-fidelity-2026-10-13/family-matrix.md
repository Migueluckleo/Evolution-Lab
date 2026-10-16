# Matriz del barrido web · 0.1.2

Fecha:2026-10-13. Las fuentes exactas y sus hashes están en [family-matrix.json](family-matrix.json); las fichas contienen tipos, defaults y ejemplos generados del código. «Medida» identifica aserciones concretas en fidelity.spec.ts/catalog.spec.ts; «revisión» identifica revisión de fuente/API/CSS y render, sin comparación exhaustiva por píxel.

| Familia | Corrección/revisión contra fuente | Casos de galería | Verificación |
|---|---|---:|---|
| [Button](../../../implementations/web/docs/components/button.md) | Defaults PlusCircle/Default, visibilidad independiente, estados Default/Text, foco y tipografía. | 24 | Medida + render |
| [IconButton](../../../implementations/web/docs/components/icon-button.md) | Small/count=1/showCount=true; estado Outline/Focus y posición de contadores. | 12 | Medida + render |
| [FilterChip](../../../implementations/web/docs/components/filter-chip.md) | PlusCircle ocultos, props de ambos lados, foco seleccionado/no seleccionado. | 12 | Revisión + render |
| [Badge](../../../implementations/web/docs/components/badge.md) | Presentation Fill por defecto, Show left/right independientes y borde Light sin alterar25px. | 6 | Revisión + render |
| [Dot](../../../implementations/web/docs/components/dot.md) | Large por defecto; contorno exterior y cinco apariencias por tamaño. | 15 | Revisión + render |
| [InlineNotification](../../../implementations/web/docs/components/inline-notification.md) | Show icon/title/description/dismiss e icon swap; regiones ocultas conservadas. | 5 | Revisión + render |
| [LinearProgressBar](../../../implementations/web/docs/components/linear-progress-bar.md) | Label/percentage/helper independientes; helper y roles semánticos. | 48 | Revisión + render |
| [Loader](../../../implementations/web/docs/components/loader.md) | 16 combinaciones, anillo/remate fuente, ciclo antihorario1.224s, reducción de movimiento. | 16 | Revisión + render |
| [Tooltip](../../../implementations/web/docs/components/tooltip.md) | Right por defecto, flecha SVG16×10 fuente, tipografía14/24, dos sombras, asChild. | 4 | Revisión + render |
| [InputField](../../../implementations/web/docs/components/input-field.md) | Booleanas label/text/helper/prefix/trailing/help, Eye Light, defaults y alturas32/40/48. | 24 | Medida + render |
| [Textarea](../../../implementations/web/docs/components/textarea.md) | Superficie108, total160 de referencia, contador/Notches y show label/helper/counter. | 3 | Medida + render |
| [Checkbox](../../../implementations/web/docs/components/checkbox.md) | Dos etiquetas independientes y default Selected; foco y check fuente12px. | 6 | Revisión + render |
| [RadioButton](../../../implementations/web/docs/components/radio-button.md) | Etiquetas independientes/default seleccionado, borde Off/Focus y roles Disabled. | 4 | Revisión + render |
| [Toggle](../../../implementations/web/docs/components/toggle.md) | Etiquetas independientes/default On, Mixed y roles/sombras del control. | 6 | Revisión + render |
| [Search](../../../implementations/web/docs/components/search.md) | Lupa/X Light, clear en foco vacío, foco dentro del grupo y salida, tres tamaños. | 12 | Revisión + render |
| [Select](../../../implementations/web/docs/components/select.md) | Large, propiedades de contenido/visibilidad/status, Eye y navegación de teclado. | 2 | Revisión + render |
| [DropdownItem](../../../implementations/web/docs/components/dropdown-item.md) | Base/Header, iconos y texto secundario, altura48/40/32, checkbox/loader opcionales. | 12 | Medida + render |
| [FileUpload](../../../implementations/web/docs/components/file-upload.md) | Default148/Error140/Success162, dash5/5, mensajes separados, Helper/Button e icono. | 3 | Medida + render |
| [Breadcrumbs](../../../implementations/web/docs/components/breadcrumbs.md) | BreadcrumbItem público, Default/Icon/Shortened, Current/Disabled y trail0..n. | 3 | Revisión + render |
| [NavigationPagination](../../../implementations/web/docs/components/navigation-pagination.md) | Visibilidad First/Last, carets dobles, gaps y select102×26; slot páginas. | 2 | Revisión + render |
| [NavigationSwitchTab](../../../implementations/web/docs/components/navigation-switch-tab.md) | Composición0..n, teclado y preservación de selección con IDs. | 2 | Revisión + render |
| [NavigationSwitchTabItem](../../../implementations/web/docs/components/navigation-switch-tab-item.md) | No wrap, Active y count=1 por defecto; AddressBook Light. | 3 | Revisión + render |
| [NavigationTab](../../../implementations/web/docs/components/navigation-tab.md) | ImageSquare, divisor opcional, Dynamic Selected/hover/focus/disabled. | 9 | Revisión + render |
| [Steps](../../../implementations/web/docs/components/steps.md) | Galería de tipos/contextos; cantidad de indicadores variable y colores de enmienda. | 6 | Revisión + render |
| [Stepper](../../../implementations/web/docs/components/stepper.md) | Show step/caption, regiones fijas77px, conectores y radios por posición. | 18 | Revisión + render |
| [Avatar](../../../implementations/web/docs/components/avatar.md) | Show status=true como default óptico; significado accesible solo si se aporta. | 12 | Revisión + render |
| [Characters](../../../implementations/web/docs/components/characters.md) | Regresión13 poses y64 vectores; matrices SVG sin doble traslación; identidad fija. | 13 | Revisión + render |
| [Logos](../../../implementations/web/docs/components/logos.md) | 72 assets locales; ocho originales recuperados por ID; hashes y proporción. | 72 | Revisión + render |
| [EmptyStates](../../../implementations/web/docs/components/empty-states.md) | Show visual/title/main/supporting independientes; defaults Inline y Slots. | 4 | Revisión + render |
| [MetricCard](../../../implementations/web/docs/components/metric-card.md) | Ocho anatomías y cajas; V/H dos métricas, V1/V2 una; icono/action/detail independientes. | 8 | Medida + render |
| [Table](../../../implementations/web/docs/components/table.md) | Exports de piezas, Slots, visibilidades, cajas52/36 y hover1288/primera celda132. | 2 | Medida + render |
| [Modal](../../../implementations/web/docs/components/modal.md) | Ocho cajas y anatomías; Header/Body/Footer, media260 y SideBySide500+340; flags. | 8 | Medida + render |
| [Scrollbar](../../../implementations/web/docs/components/scrollbar.md) | Ocho presets visuales exactos; ScrollArea nativo separado; tamaños literales. | 8 | Medida + render |
| [Fuentes](../../../implementations/web/docs/components/fuentes.md) | Ancho167.6667, gaps externos8/internos4 y ruta8/16; composición de Path. | 1 | Revisión + render |
| [Charts](../../../implementations/web/docs/components/charts.md) | Cell padding8/6/4 y dash2/2; Header638×48, Progress639×30/104 y dos leyendas. | 20 | Medida + render |
| [Header](../../../implementations/web/docs/components/header.md) | Show version/actions/company/user, caret company/profile original y altura96. | 2 | Medida + render |
| [Sidebar](../../../implementations/web/docs/components/sidebar.md) | 22 recetas, unions SVG, relleno/iconos, BETA,72/234×885, toggle24, TopBar1399×48. | 25 | Medida + render |
| [AppShell](../../../implementations/web/docs/components/app-shell.md) | 1440×1024 por defecto, Header96, rail104/266; Sidebar904 sin mínimo inventado. | 1 | Medida + render |
| [ChatHistoryItem](../../../implementations/web/docs/components/chat-history-item.md) | Selected/hover, gap y acciones hermanas del control principal. | 2 | Revisión + render |
| [ChatToolItem](../../../implementations/web/docs/components/chat-tool-item.md) | Show extra actions=false; caret independiente y Disabled sin hover. | 2 | Revisión + render |
| [ChatToolbar](../../../implementations/web/docs/components/chat-toolbar.md) | 79/264×791, Show indicators=false/plan=true; contenido y ausencia de overflow. | 2 | Medida + render |
| [Conversation](../../../implementations/web/docs/components/conversation.md) | Glifos originales32px, flags respuesta/feedback, Draft y Disclaimer; slots. | 2 | Revisión + render |
| [ChatSection](../../../implementations/web/docs/components/chat-section.md) | Show status, separación de regiones, mínimo574/máximo816 y layout de enmienda. | 1 | Revisión + render |

Hover/Focus/Press de controles nativos se activan en el navegador; no cuentan como tarjetas estáticas separadas. Sidebar sí expone las22 recetas para inspección explícita. Charts agrupa sus cuatro Legend Label en una tarjeta:20 tarjetas representan23 definiciones. Los slots aceptan contenido fuera de las muestras; la galería no define máximos de producto.

No se convierten los asuntos de auditoría de los contratos en aprobaciones nuevas. Loader usa interpolación CSS continua; ScrollArea depende del motor nativo; asset PNG no equivale a vector.
