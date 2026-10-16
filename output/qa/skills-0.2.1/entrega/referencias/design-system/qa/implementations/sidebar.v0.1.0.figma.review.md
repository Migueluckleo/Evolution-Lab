# Sidebar v0.1.0 · QA de implementación

2026-10-05 · **PASS técnico acotado**. Contrato [SIDEBAR-001](../../specs/sidebar.contract.v0.1.0.md), DELEGATED_FOR_BUILD. Auditoría humana PENDING; biblioteca UNPUBLISHED. No certifica accesibilidad ni producto funcional.

## Construcción y lectura
Página614:125, Menu Item615:355 (22 variantes), Sidebar619:480 (dos presentaciones) y Top bar619:607. Se preservan geometrías234×48,72×48,234×40,200×40; menú72/234×885 y barra1399×48. BETA Manrope en lugar deInter es normalización previamente documentada. Las siluetas se copiaron desde mains fuente sin detach.
Fuente:286nodos/93instancias; observación PARTIAL en proyección normalizada/dependencias externas. Esta limitación no se oculta como inspección completa. El inventario JSON aprobado conserva su digest.

## Evidencia
- [Bindings finales](sidebar.v0.1.0.bindings-final.json):141 paints efectivos,35 textos,42variables semánticas. Cero pinturas sin binding, scopes incorrectos o referencias externas;90instancias de dependencias y cero mains locales ajenos al mapa. No incluye paints editoriales del marco de revisión.
- [Temas](sidebar.v0.1.0.themes.json):576 comparaciones RGB consumidor→alias en Contable/Administrativo/Servicios/Personas, cero diferencias. Incluye pinturas interiores de booleanos además de las141efectivas.
- [Slots](sidebar.v0.1.0.slots.json):16checks PASS. Vacío,12items principales (>10del ejemplo),3opciones inferiores,6tabs (>4del ejemplo), reordenamiento, sustitución, Expanded→Collapsed→Expanded conservando orden y etiquetas. Sin detach.
- [Texto largo](sidebar.v0.1.0.long-labels.json):16variantes con Label real reciben una cadena larga, conservan altura y elipsis. Las dos variantes de submenú con caja fija serializan TRUNCATE/maxLines=null; el criterio inicial esperaba maxLines=1 indebidamente y se corrigió al comportamiento documentado de caja fija. No se declara prueba de texto largo para el Tooltip anidado; se restauraron sus propiedades originales desde el main local.
- Tres roles nuevos, doce aliases a primitivas existentes: [JSON canónico de extensión](../../drafts/foundations/ai-design-system.sidebar.v0.1.0.json), [readback](../../implementations/figma/sidebar.v0.1.0.foundations.json). No primitivas nuevas ni colores nuevos.
- [Mapa origen→destino](../../implementations/figma/sidebar.v0.1.0.local-token-map.json) y180comparaciones de aliases del preflight; el conjunto final consume42variables/168aliases.

## Revisión visual
Marco625:264 de1447×1272, inspeccionado a escala1 tras composición y tras corrección de captions/truncado. Mains fuera del marco; contenido de revisión formado por instancias. Todas las variantes presentes, sin solapamientos o recortes accidentales. Huecos de Focus/Submenu intencionales. Curvas, iconos, BETA, flechas, divisores, tooltip y composición del menú coherentes con la fuente. No se vuelve a tomar una captura idéntica después del PASS.
Capturas mostradas por MCP en la conversación; no se inventa ruta PNG persistente.

## Correcciones del lote
Se sustituyeron dos fills text/on-brand heredados en el control de colapso por background/default (mismo blanco) y14 referencias tipográficas remotas por rango. Se normalizaron cuatro propiedades Slot redundantes a dos compartidas. Un intento de eliminar una propiedad usando su nombre anterior falló; lectura posterior confirmó rollback de esa llamada. Se recuperó por IDs y nombres reales, sin duplicar componentes.
Cinco estilos tipográficos locales Sidebar/Label, Label Active, Submenu, Submenu Active y Release aplicados; los consumidores conservan bindings explícitos. No se modifican mains de Tooltip/Icon Button/Phosphor.
Las instancias temporales se retiraron; IDs de prueba/retirada en sus evidencias. Solo permanecen componentes y marco de revisión.

## Limitaciones conservadas
Mediciones de [contraste](sidebar.v0.1.0.contrast.json) por pares opacos, no evaluación global del gradiente: submenú2.451–4.223:1*, hover horizontal1.582–2.225:1*, BETA inicio2.262/3.368:1*, Servicios blanco/marca3.236:1*, marca/superficie3.046:1*, divisor1.243–1.619:1*. El extremo final violeta deBETA4.389:1*. No cambiar colores por esas mediciones.
Los Slots conservan contenido; la presentación de hijos personalizados no cambia automáticamente con el contenedor. No se promete que cualquier cantidad quepa en885px o1399px: ampliar dimensión o resolver overflow en producto. No breakpoints, rutas, permisos ni comportamiento runtime inventados.

## Cierre
Promover contrato a specs y actualizar registros. Graphify permanece STALE; sin regeneración. Siguiente familia: Empty states desde la Librería raíz, sin repetirTable/Modal/Sidebar ni reactivarlogos omitidos.
