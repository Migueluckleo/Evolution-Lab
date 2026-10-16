# QA-APP-SHELL-FIGMA-001 · 2026-10-06

IMPLEMENTATION_REVIEW: **PASS técnico acotado** para APP-SHELL-0010.1.0. Destino AI Design System, página App Shell737:303, main737:304. Auditoría humana PENDING; publicación de biblioteca no ejecutada. No certifica accesibilidad web ni toda la biblioteca.

## Requisitos y evidencia

| Requisito | Resultado | Evidencia ejecutada |
|---|---|---|
| REQ-AS-01 identidad/página | PASS | Una página App Shell y un COMPONENT; lectura final solo737:304 como hijo de página. |
| REQ-AS-02 dependencias | PASS | Header737:305 deriva de518:123; Sidebar737:412 de619:481. No detach. Mains existentes conservan dimensiones y Slots previos al build. |
| REQ-AS-03 propiedades | PASS | Content#737:1 de tipo SLOT; Header y Sidebar expuestos. Edición de Company probada; Presentation cambia sin resize manual en la segunda prueba. |
| REQ-AS-04 geometría | PASS |1440×1024; Header1440×96; Body1440×928; rail104×928; Sidebar72×904; Content1336×928. |
| REQ-AS-05 layout | PASS | Auto Layout vertical/horizontal, rail HUG/FILL, Slot FILL/FILL; gap0 y padding del rail tokenizados. |
| REQ-AS-06 tokens | PASS |48variables consumidas y45dependencias canónicas:93/93definiciones coinciden en nombre/colección/tipo/scopes/description/codeSyntax/valores/aliases por modo.60pinturas/stops UI vinculados, cero sin binding;34pinturas de artwork agnóstico excluidas según excepción vigente. |
| REQ-AS-07 Slots | PASS | Insertar0→1→2→3, reordenar, borrar, sustituir por Header local, reset→0 desde consumidor. Principal vacío y vínculos conservados. |
| REQ-AS-08 desktop | PASS |12casos:1280×800 y1440×1024 ×Collapsed/Expanded ×0/1/3contenidos. Anchura y posición de hijos ajustadas, sin solapamientos de fixtures. |
| REQ-AS-09 readback/render | PASS | Lectura independiente150nodos incluidos ocultos. Captura737:304 a0.75 revisada: Header horizontal legible, rail56/904coherente, contenido vacío intencional, sin superposiciones. |
| REQ-AS-10 reutilización fiel | PASS | Diferencias heredadas del Header/Sidebar registradas antes del build, sin modificar contratos/mains hijos. No igualdad pixel a pixel de internals históricos. |

## P-SLOTS

SLOT-QA-01–09 PASS en el alcance aplicable Content: REQUIRED, propiedad nativa, cardinalidad0..n sin máximo ficticio, edición desde consumidores737:448 y741:2043, orden/eliminación/sustitución/reset,12escenarios de layout, preservación de enlaces/variables y cuatro temas. SLOT-QA-04: una cantidad menor que la muestra0es NOT_APPLICABLE; se prueban0/1/3/8sin convertir8en máximo. SLOT-QA-06: texto largo truncado correctamente en160×20; lista de8Headers alcanza768px frente al Slot704px. No hay scroll automático (overflow NONE), Slot no recorta y shell sí; límite explícito compatible con§11/13del contrato, no PASS de contenido ilimitado sin overflow. SLOT-QA-07: binding color/text/brand y resolución de cuatro temas conservados tras reordenar el contenido. SLOT-QA-08: contenido/override preservados al cambiar SidebarCollapsed↔Expanded; el anfitrión no tiene variantes propias. Actions/Menu items/Lower options mantienen sus contratos y propietarios; no se certifican aquí nuevamente todas sus interacciones internas.

## Color y tipografía

60/60consumos cromáticos efectivos incluyendo descendientes ocultos conservan rol y scope técnicos correctos. Notch vector blanco de Sidebar es superficie de selección (background/default), no icono; strokes de caret usan rol icon/header-caret-stroke, no text. Todos los IDs leídos son locales/semantic; no fill directo a primitiva.12textos anidados conservan sus bindings (family/style, colores y demás propiedades según contrato hijo); la envoltura no agrega tipografía.

Los cuatro modos del Sidebar resuelven azul/verde/naranja/morado; fondo blanco canónico en los cuatro, sin explicitVariableModes en main. Las limitaciones históricas de contraste de Header/Sidebar no se corrigen ni se vuelven PASS accesibilidad. Logos mantienen sus literales permitidos; no se cierra su QA global.

## Archivos de evidencia

- `app-shell.v0.1.0.readback.json`:150nodos,60pinturas,48IDs consumidos,37bindings propios de envoltura y textos anidados.
- `app-shell.v0.1.0.token-parity.json`:93definiciones comparadas con inventario y extensiones Header/Sidebar/Dot/Avatar +overrideAvatarServicios0.1.1.
- `app-shell.v0.1.0.scope-check.json`:scope técnico por pintura; revisión semántica por función complementada arriba.
- `app-shell.v0.1.0.slot-probe.json`:operaciones, propiedades, tamaños y cuatro temas.
- `app-shell.v0.1.0.final-checks.json`:12casos y limpieza de instancia temporal.
- `app-shell.v0.1.0.extended-slot-results.json`:texto largo,8elementos,overflow explícito,preservación de override y bindings tras reordenación/configuración, cuatro temas del contenido insertado. Captura del fixture1280×800revisada; Header anidado es solo instrumento de QA, no ejemplo de uso recomendado ni contenido default.
- `app-shell.v0.1.0.cleanup.json`:eliminación de fixture adicional741:2043; main vacío e intacto.

## Recuperación y limpieza

Primera escritura rechazó un renombrado redundante de propiedad. La lectura posterior confirmó página ausente; se repitió sin esa operación. No hubo duplicados. Una salida de QA demasiado extensa se repitió con serialización compacta; no se usó salida truncada como PASS. La primera prueba extendida falló buscando texto por contenido; lectura confirmó ausencia de fixture y se repitió en dos llamadas mediante ID estable de subcapa. Se retiraron exclusivamente las instancias temporales737:448 y741:2043 y sus fixtures, creados en esta tarea. Main737:304 permanece. La captura final del main precede a esa limpieza, que no modifica el main.

## Cierre

VALIDATED para la composición y controles definidos. Cero variables/primitivas/estilos nuevos; JSON canónico intacto. Promoción documental a specs habilitada; auditoría humana por excepciones pendiente. Sin nuevas decisiones de producto exigidas para este alcance. Los comportamientos de aplicación/móvil siguen fuera de alcance. Grafo STALE, no regenerado en esta operación.
