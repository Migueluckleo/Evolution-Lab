# QA-WEB-COMPONENTS-001 · web 0.1.0

**Fecha:** 2026-10-13. **Resultado:** PASS_WITH_DOCUMENTED_LIMITS para biblioteca inicial, documentación, compilación y recorridos locales. Destino IMPLEMENTED_FOR_LOCAL_PROTOTYPING; no VALIDATED visual global ni aprobación de contratos Figma. [Resultados y hashes](web.v0.1.0.results.json).

## Fuentes y cambios

Se revisaron AGENTS, P01/P03/P05/P06/P-SLOTS, la skill Graphify y contratos/enmiendas de 43 familias mediante la vista registral y fuentes originales. Para exportar Logos se aplicó figma-use en lectura. Las fichas conservan los enlaces/hashes exactos y los scripts identifican 32 fuentes de tokens. No se modificó el JSON aprobado: SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474.

[DEC-WEB-COMPONENTS-001](../../registry/decisions.md) autoriza código, documentación técnica, ejemplos sin backend y protocolo para altas posteriores. Se implementaron 43 familias con API tipada, estilos semánticos, composición local, catálogo Next y una pantalla de documentos con formulario/búsqueda/filtro. [Guía](../../implementations/web/README.md), [índice](../../implementations/web/docs/components/README.md), [P07](../../protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md).

## Comprobaciones ejecutadas

| Comando / alcance | Resultado |
|---|---|
| pnpm ds:generate y ds:check, en implementations/web | 43 familias, exports/ejemplos/fichas coherentes, derivados actualizados |
| pnpm verify | TypeScript estricto, 7/7 pruebas y build estático Next PASS |
| pnpm test:browser | 6/6 pruebas en Chrome PASS |
| Alteración temporal de una ficha + ds:check | Rechazada con exit 1 por documento desactualizado; bytes originales restaurados y hash registrado |
| scripts/ds test | 21/21 pruebas del tooling documental PASS |
| scripts/ds check --docs-only | Gate documental separado en el cierre; debe estar PASS antes de publicar el grafo |

Pruebas unitarias: render de todas las familias/exports; hashes de fuentes de tokens; referencias CSS y SVG de ejemplos resueltas; personajes de identidad fija y frames inexistentes rechazados; listas vacías y cardinalidad superior a la muestra; semántica button/link/progreso/mixed; existencia y hashes de assets Logos.

Pruebas de navegador: recorrido de los 43 ejemplos sin pageerror ni imágenes rotas; checkbox, toggle, select por teclado, tabs, diálogo Escape y retorno de foco; selección de un archivo local; envío de mensaje a memoria; cambio de cuatro temas y conservación del fill de Characters; alta, búsqueda y reinicio por recarga de la pantalla; catálogo a 390px sin overflow horizontal; Button en 32/40/48px.

Axe: cero infracciones en catálogo + InputField, con color-contrast deshabilitado por las excepciones de fuentes. No se extrapola a otras familias, contraste o WCAG integral. La navegación de tabs del catálogo admite flechas/Home/End.

Durante verificación se corrigieron el alto de Button/FilterChip, el gap del helper, el fill fijo de ProgressChartItem y una referencia de color ausente en EmptyStates. La última deriva se resolvió preservando blanco de máscaras/clipPaths como geometría según REQ-ES-05 y distinguiendo roles de fill/stroke; no creando tokens nuevos. Reejecución final PASS. La revisión de fichas corrigió Select a Slots REQUIRED por su lista options y explicitó la composición children del viewport Scrollbar; son clasificaciones web, sin mutar Figma. El primer plan de grafo se conserva y se prepara v2 con hashes nuevos, reutilizando solo fragmentos releídos o sin cambios.

## Inspección visual acotada

[Catálogo desktop](web.v0.1.0.catalog.png) y [pantalla compuesta](web.v0.1.0.screen.png) inspeccionados: navegación, títulos, controles y tabla legibles, sin solapamientos en las vistas capturadas. La captura muestra tema contable a 1440px. La prueba móvil se limita a navegación del catálogo; AppShell/Chat conservan límites desktop y overflow interno. No se compararon pixel a pixel todas las variantes contra Figma.

## Límites y decisiones pendientes

Logos: 64/72 assets. Ocho pendientes por límite de consultas MCP, con IDs en [manifiesto](../../sources/assets/web/logos.manifest.json). No se usó un logo alternativo para simular cobertura. Código y API de la familia disponibles; assets de esas ocho variantes PARTIAL. No se requiere decisión adicional para usar las disponibles.

Las [adaptaciones técnicas](../../implementations/web/docs/WEB-ADAPTATION.md) registran unidades, control nativo, scrollbar, gráfico estático, glifo reducido de Conversation y comportamiento de demostración. Siguen las excepciones/auditorías históricas de Avatar/Toggle/Tooltip/Logos. No se validaron todas las combinaciones visuales, todos los navegadores o lectores de pantalla. No hay backend, publicación, modificación Figma ni nuevas aprobaciones de diseño.

## Cierre de trazabilidad

Grafo STALE durante el lote. Se ejecutó graphify update . y se conservó el resultado AST separado, restaurando por hash los nueve outputs del cierre completo anterior. El cierre mantenido usa scripts/ds status --write y graph prepare/close con run 2026-10-13-web-components-v2, incluyendo semántica de documentos, CSS, lockfile e imágenes nuevas. CURRENT depende de closure.json y del check final; no se deduce del build web. Uso semántico medido UNAVAILABLE. Los 673 retiros previos del índice se preservan; este lote no hace commit ni push.
