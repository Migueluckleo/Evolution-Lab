# SIDEBAR-001 · Sidebar · v0.1.0

Estado: DELEGATED_FOR_BUILD. QA documental e implementación técnica PASS acotado, 2026-10-05. Auditoría humana PENDING; biblioteca Figma UNPUBLISHED. Promoción bajo DEC-MIGRATION-SPECS-AUDIT-001. Ajustes posteriores se realizan aquí, versionados.

## 1. Propósito y fuentes
Navegación lateral expandida/colapsada y composición horizontal asociada, migradas de la Librería raíz, no de Anticipa. La fuente se conserva en [snapshot](../sources/figma-snapshots/sidebar.v0.1.0.source.json), SHA256 `1ae050ab1e062a221edc4ab473456abeb8005037075b164acc960cd89005e73e`.
Fuente: `9zs5RMR8LB5wHjW9Bd59BA`, página `268:20244`; Menu Item `3365:23953`, Menu `8283:544`, Top-bar `8283:4142`.
Inspección OBSERVED de 286 nodos, 93 instancias, 17 dependencias principales y 48 variables. Observación normalizada PARTIAL: no se inspecciona el resto de las bibliotecas remotas ni se deduce comportamiento de producto.

## 2. Alcance y requisitos
Destino exclusivo `tj3WIBEZDGLVs7MJWKCwgf`, página semántica **Sidebar**, operación CREATE, sin alterar otras familias.
- REQ-SB-01: Menu Item conserva exactamente las 22 combinaciones observadas.
- REQ-SB-02: Sidebar conserva dos presentaciones, Collapsed (72×885) y Expanded (234×885).
- REQ-SB-03: Top bar conserva baseline 1399×48 y composición horizontal variable.
- REQ-SB-04: tokens semánticos locales, aliases por los cuatro modos, tipografía Manrope.
- REQ-SB-05: Slots nativos editables desde instancias, sin detach ni máximos derivados de ejemplos.
- REQ-SB-06: Tooltip e Icon Button reutilizados del destino; iconografía Phosphor mediante keys observadas.
- REQ-SB-07: geometría de curvas/notches preservada; revisión visual, tokens y composición antes de promoción a specs.

## 3. Anatomía
Menu Item: fondo con silueta de selección, icono principal, label, caret opcional; BETA aparece inicialmente solo en Vertical/Expanded/Default/Active y tooltip en los estados colapsados observados.
Sidebar: Toggle control + Menu items + Lower options. Top bar: contenedor + Menu items horizontal.
No reconstruir manualmente vectores de Phosphor. No duplicar mains de Tooltip, Icon Button o Dot.

## 4. Propiedades y variantes
Menu Item preserva ejes orientation, type, status, isActive y 22 combinaciones del snapshot. Label TEXT, show right icon BOOLEAN, fill icon/light icon INSTANCE_SWAP.
No completar producto cartesiano ni agregar Disabled: no existe variante observada.
Sidebar normaliza `Property 1=colapsed/expanded` a `Presentation=Collapsed/Expanded`.
Slots Menu items y Lower options tienen el mismo propósito entre presentaciones; se intentará compartir la propiedad conservando contenidos y se exige prueba de retención. Si la API no permite la normalización sin pérdida, no declarar PASS.
Top bar: Menu items SLOT. Las rutas y acciones no están definidas por la fuente.

## 5. Tamaños y layout
Menu Item expanded234×48, collapsed72×48, submenu234×40, horizontal200×40. Padding e interlineado se conservan salvo normalización explícita indicada.
Sidebar vertical, control superior56px, área principal FILL, zona inferior HUG88px en ejemplo, radio16px.
Top bar padding superior8px, laterales16px, gap de items4px, radio8px.
Las medidas de composición son geometría contractual; no vincular spacing a width/height por coincidencia numérica.
Los Slots no prometen que una cantidad ilimitada quepa en el baseline: el consumidor amplía alto/ancho o define overflow en producto. No inventar breakpoints.

## 6. Tokens y trazabilidad
Autoridad: [inventario](../sources/inventories/tokens.inventory.json), SHA256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`, más [extensión Sidebar](../drafts/foundations/ai-design-system.sidebar.v0.1.0.json).
Mapa previo [tokens-preflight](../implementations/figma/sidebar.v0.1.0.tokens-preflight.json); [mapa final origen→destino](../implementations/figma/sidebar.v0.1.0.local-token-map.json). Tres nuevos roles: VariableID:614:122, VariableID:614:123 y VariableID:614:124. codeSyntax vacío conforme al proyecto documental: no se inventan nombres CSS sin implementación frontend.
Reglas explícitas:
- Contenedor colapsado: nuevo color/background/sidebar/brand, alias a primitivas del color de marca por modo.
- Fondo de selección de Menu Item: color/interactive/primary/default; hover intenso: color/interactive/primary/hover.
- Submenú activo: color/surface/brand/accent; superficie expandida: color/surface/brand.
- BETA: nuevos background/sidebar-release-start y end, aliases por modo iguales a la fuente de acento; no usar roles de interacción para la etiqueta pasiva.
- Textos: roles text/inverse, text/brand, text/brand/strong o text/on-brand según la fuente; iconos solo roles icon; bordes solo border/focus.
- fuente font/size/1xs corresponde al nombre local font/size/2xs (10px); aliases verificados, no ID inferido.
- variables remotas spacing0/12/24, radius8/full, stroke1, icon16 se sustituyen por los roles locales none/md/xl, md/full, xs y size/lg respectivamente tras comprobar valores.
- Literales geométricos, sombras observadas y line-height AUTO permanecen explícitos cuando no existe categoría equivalente. No crear primitivas.

## 7. Tipografía y estilos
Manrope Regular/SemiBold 14/24 para labels regulares; conservar AUTO donde la fuente lo usa y no normalizar por adivinación. Tracking0 se vincula a normal.
BETA fuente Inter Bold10/AUTO se normaliza a Manrope Bold10/AUTO, usando variables locales; registrar diferencia geométrica resultante.
Crear/reutilizar estilos compartidos Sidebar/Label y Sidebar/Label Active (14/24), Sidebar/Submenu y Sidebar/Submenu Active (14/AUTO), Sidebar/Release (10/AUTO), y aplicarlos a los textos pertinentes; bindings de consumidor permanecen explícitos.
Tooltip local tiene baseline distinto de fuente (121×40 contra116×38 main fuente, con overrides observados). Reutilizar su contrato y documentar tamaño final, no modificar el main.
Dot interno de Icon Button se hereda de su contrato; Show count=false para toggles sin indicador. Sus fondos blancos heredados usan background/default, nunca text/on-brand. Los bindings tipográficos por rango se reemplazan además de los bindings escalares.

## 8. P-SLOTS
REQUIRED Sidebar.Menu items (0..n), Sidebar.Lower options (0..n), Top bar.Menu items (0..n).
NOT_APPLICABLE Menu Item: anatomía fija, label/booleanas/swaps cubren la variación; no cantidad de hijos de composición.
minChildren0, maxChildren sin límite, preferredValues Menu Item local como sugerencia, no restricción absoluta.
Contenido inicial de fuente es demostrativo. No variants Amount. Permitir insertar, borrar, sustituir y reordenar desde instancia sin detach.
Validar retención de texto/composición al cambiar Expanded→Collapsed→Expanded. Los elementos mantienen su contenido; no prometer transformación automática de variantes de cada hijo si la API no la implementa.
Lower options puede alojar composición adicional; mantener el divisor inicial como ejemplo, no requisito de cardinalidad.

## 9. Comportamiento y contenido
Label y BETA son ejemplos. BETA no calcula versión ni estado. Tooltip muestra texto editable del contrato local.
Mejora delegada de contenido: Label usa una sola línea con elipsis al final; mantiene el texto completo en la propiedad editable, sin modificar altura del control. Frontend debe ofrecer acceso al nombre completo. No extender este truncado al contenido de Tooltip.
La flecha superior es control visual; no se afirma navegación, permisos, rutas, persistencia ni collapse automático en runtime.
Reacciones de prototipo solo se conservarán si el destino es válido y remapeado; enlaces a nodos ajenos o null no se presentan como funcionales.

## 10. Accesibilidad
No declarar WCAG PASS por QA técnico Figma. Conservar colores; medir contraste por modo y marcar limitaciones con asterisco en auditoría, sin recolorear.
Frontend pendiente: navegación por teclado, nombres accesibles para iconos, aria-current y anuncio de estado expandido. Tooltip no sustituye el nombre accesible.
El componente no cubre mobile ni estados disabled inexistentes.

## 11. Dependencias
Tooltip local set88:122, Left87:137; Icon Button local Ghost/Small/Default183:161, set183:311. No editar sus mains.
Phosphor: HouseLineFill `7de3e2b6dd8bfe526ed1ec72cc2df4052c42c2de`; HouseLineLight `090ff24ab3485ba51fe71427dd00328da0afe68f`; CaretDownLight `bc84188a38d95b6865a7c6a57820ee2330e43f34`; CaretRightLight `e2fc671298e81c590f5a4a5272d9c97709515666`; QuestionLight `8ebba51c41e3b39511663395803390b9d2e3d3f7`; CaretLeftLight `4472d4a157a44ccd6e7e4911b4c9dcad1dc04b34`.
Importar/copiar la estructura de componentes fuente como nuevos mains locales, nunca detach de instancias. Remapear las dependencias fuente y todos los bindings.

## 12. QA y aceptación
Comprobar25 definiciones, ejes, propiedades, referencias locales, geometría, todos los paints efectivos y cuatro modos. Probar Slots0/1/3 y más que el ejemplo, reorder, replacement, retención y contenido largo. Revisar instancias en un marco compacto separado de mains.
No construir Empty states hasta resolver el resultado de este lote. No reauditar globalmente familias terminadas.
Promoción documental a specs solo con QA documental e implementación PASS; aprobación humana PENDING, biblioteca UNPUBLISHED.

## 13. Excepciones abiertas
Comportamiento runtime fuera de alcance. BETA pasa a Manrope10/AUTO; su texto mide14px de alto, sin cambiar los48px del Menu Item. Tooltip reutilizado conserva su geometría local y overrides de consumidor; no se modifica su main.
Contraste por pares semánticos: submenú activo2.451–4.223:1*; texto fuerte sobre barra de marca1.582–2.225:1*; inicio de gradiente BETA2.262/3.368:1*; Servicios texto/blanco de marca3.236:1* y marca/superficie3.046:1*. Divisor1.243–1.619:1*. Son limitaciones conservadas para revisión interna, no WCAG PASS. [Mediciones](../qa/implementations/sidebar.v0.1.0.contrast.json).
No hay autorización para regenerar Graphify: quedará STALE tras cambios.

## 14. Implementación y evidencia vigente
Página Sidebar614:125; Menu Item615:355 (22 variantes), Sidebar619:480 (Collapsed619:481, Expanded619:496), Top bar619:607. [Vista de revisión](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=625-264).
42 variables semánticas consumidas,141 pinturas efectivas,35 textos, cero referencias externas de variables o bindings fuera de scope.16 pruebas de Slots y16 de contenido largo;576 comparaciones de color por tema. Los huecos de Focus/Submenu son intencionales: no existe esa combinación fuente.
Slots Menu items#8283:0 y Lower options#8283:3 compartidos entre presentaciones; Top bar Menu items#8283:12. Figma serializa minChildren0 como null (sin mínimo); el vacío fue probado. El truncado de texto con altura fija puede serializar maxLines=null y textAutoResize=TRUNCATE: elipsis dentro de una caja de una línea, sin aumento de altura. No se fuerza ese comportamiento al Tooltip.
Las instancias temporales de QA se retiraron; permanecen mains y vista de revisión. [QA](../qa/implementations/sidebar.v0.1.0.figma.review.md), [estado](../implementations/figma/sidebar.v0.1.0.state.json).
