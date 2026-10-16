# QA web · barrido de fidelidad · 0.1.2

> Continuidad0.1.3: las primeras ejecuciones del barrido reutilizaron las rutas de captura/medición de `web-fidelity-2026-10-13`; esos archivos compartidos contienen recapturas posteriores del mismo día y ya no representan todos los bytes del corte0.1.2. El results.json histórico conserva sus hashes originales como referencia, no como manifiesto vigente. Desde el cierre0.1.3 las pruebas escriben exclusivamente en [web-contract-audit-2026-10-13](web-contract-audit-2026-10-13/family-matrix.md), con hashes y reporte propios. Este reporte mantiene los resultados declarados en su ejecución original; no se usa para certificar los archivos recapturados.

**Fecha:** 2026-10-13. **Resultado:** PASS para el alcance comprobado abajo; no certificación global por píxel. **Destino:** biblioteca local React/TypeScript/Tailwind/Next.js. Contratos y aprobaciones Figma sin cambios.

## Solicitud y fuentes

Solicitud EXPLICIT del usuario: «La sidebar no se parece ni tiene los parametros correctos de acuerdo a los specs ni componente, necesito que hagas un barrido y todo quede permeado exactamente a lo que se documentó». Se corrigió implementación, no se reescribieron requisitos visuales para adaptarlos al código. Leídos AGENTS, P07, P05, P06 y P-SLOTS; Graphify utilizado primero como índice y contrastado contra fuentes.

El barrido cubre las 43 familias de [components.registry.json](../../implementations/web/components.registry.json), sus contratos y enmiendas. La [matriz por familia](web-fidelity-2026-10-13/family-matrix.md) identifica corrección, casos y tipo de comprobación; su [JSON](web-fidelity-2026-10-13/family-matrix.json) guarda fuentes y hashes, exports, módulos y aplicabilidad de Slots. Las fichas se regeneran desde tipos/defaults reales del código, sin otro inventario editable de props.

Se contrastaron además las geometrías con snapshots existentes y lecturas Figma de solo lectura: [Sidebar](../../sources/figma-snapshots/sidebar.web-fidelity.2026-10-13.json), [Metric Card](../../sources/figma-snapshots/metric-card.web-fidelity.2026-10-13.json), [Header/Modal](../../sources/figma-snapshots/header-modal.web-fidelity.2026-10-13.json), [Loader/Header](../../sources/figma-snapshots/loader-header.web-fidelity.2026-10-13.json) y [caret perfil](../../sources/figma-snapshots/header.profile-caret.web-fidelity.2026-10-13.svg). No se modificó el archivo Figma.

## Cambios principales

- Sidebar: MenuItem tipado con las 22 combinaciones existentes, contornos Union desde vectores, roles por estado, iconos Light/Fill, BETA solo en la receta documentada, submenús, toggle24, cajas72/234×885 y TopBar1399×48. Selección y contenido sobreviven al cambio de presentación. No se agregó Disabled ni Focus al submenú.
- Controles: booleanas de visibilidad y swaps, defaults del maestro, estados CSS, medidas, tipografía y roles corregidos. Button conserva sus dos PlusCircle de maestro; las pantallas de ejemplo los ocultan explícitamente cuando no aportan significado. FileUpload usa trazos5/5 y alturas148/140/162; Search conserva foco dentro de su grupo y lo retira al salir.
- Composición: ocho Metric Card, ocho Modal, piezas de Table y ocho presets de Scrollbar; contenedor nativo ScrollArea separado. Table conserva expresamente TABLE-AUD-001 en Hover. Header/AppShell/ChatToolbar usan sus cajas y visibilidades documentadas.
- Gráficos: Cell mantiene los desplazamientos8/6/4, trazo2/2, Header638×48 y Progress Top639×30/Detail639×104 con dos leyendas. Las barras conservan valores de muestra, sin cálculo inventado.
- Personajes: se preservó el arreglo de matrices de BENI/NAVI; Conversation usa su dibujo propio de32px. Se completaron los ocho archivos faltantes de Logos:72/72 originales locales, con IDs/hashes en [manifiesto](../../sources/assets/web/logos.manifest.json).
- Catálogo: pestaña Variantes por familia y442 casos de referencia. Se aisló el estilo de los títulos del catálogo que contaminaba los títulos internos de Metric Card. Fichas, ejemplos, API, notas de adaptación y P07 actualizados.

## Comprobaciones ejecutadas

[Resultados](web-fidelity-2026-10-13/results.json) conserva nombres de pruebas, resultados, estadísticas y hashes relevantes.

| Comprobación | Resultado y alcance |
|---|---|
| `pnpm --dir implementations/web verify` | PASS:43 familias, cero derivados desactualizados, TypeScript,8 pruebas, build estático Next. |
| `pnpm --dir implementations/web test:browser` | PASS:15 pruebas Chrome local, sin fallos, omisiones ni reintentos. |
| Ejemplos y galería |43 ejemplos y442 casos sin errores JavaScript ni assets rotos. No equivale a comparación de cada píxel. |
| Sidebar |22 recetas×4 temas:88 comprobaciones de ancho, alto, rol de texto y presencia de Union; dos cajas885, toggle24, TopBar48; selección, submenús y tooltip sin doble foco. [Medidas](web-fidelity-2026-10-13/sidebar.measurements.json). |
| Metric Card / Modal |8 cajas de cada familia, contrastadas con dimensiones finales. [Metric Card](web-fidelity-2026-10-13/metric-card.measurements.json). |
| Campos y piezas |Input/Dropdown48/40/32; Textarea108/160; Scrollbar8 presets; FileUpload3 alturas y dash5/5; Charts3 cajas y posiciones de barra. |
| Composiciones |Table encabezado52/fila36, Default1280/Hover1288 y primera celda156/132; Header96; ChatToolbar79/264×791; AppShell1440×1024 y Sidebar904. |
| Interacciones |Hover/foco de Button, contador IconButton, teclado Select/Tabs, Modal Escape/devolución de foco, selección de archivo local, conversación local y agregar/filtrar/resetear tabla. |
| Identidad y datos |13 frames,64 vectores fuente/47 paths pintados; matrices CTM con tolerancia0.001. Cuatro temas cambian marca y preservan personajes. Inventario canónico SHA256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474 intacto. |
| Accesibilidad acotada |Axe en InputField/catálogo, sin color-contrast; navegación de catálogo a390px. No evaluación integral WCAG. |

Inspección visual de [Sidebar](web-fidelity-2026-10-13/sidebar.web.png), [sus variantes](web-fidelity-2026-10-13/sidebar.variants.png), [Metric Card](web-fidelity-2026-10-13/metric-card.web.png), [Modal](web-fidelity-2026-10-13/modal.web.png) y [BENI](web-fidelity-2026-10-13/beni.web.png). Capturas adicionales: [catálogo](web-fidelity-2026-10-13/catalog.web.png), [composición](web-fidelity-2026-10-13/composition.web.png), [Characters](web-fidelity-2026-10-13/characters.web.png), [Chat](web-fidelity-2026-10-13/chat-section.web.png). Las capturas históricas0.1.0/0.1.1 se conservan.

Las ejecuciones intermedias detectaron y corrigieron: contadores desplazados1px, Textarea168 en vez de160, títulos Metric Card afectados por CSS del catálogo, navegación que conservaba la pestaña anterior y Table Hover ensanchado dos veces por el algoritmo nativo de tabla. El cambio de presentación de la tabla elimina ese cálculo duplicado y mantiene thead/tbody/th/td. El resultado final corresponde a una reejecución completa posterior a las correcciones.

## Límites vigentes

La revisión de las43 familias combina contrato, API/CSS, render y medidas específicas. No se verificó pixel a pixel cada estado de todas las familias en los cuatro temas. Hover/Focus/Press usan eventos nativos; no todas sus combinaciones tienen tarjeta estática separada. No se certifican otros navegadores, lectores de pantalla o una auditoría WCAG global.

[WEB-ADAPTATION](../../implementations/web/docs/WEB-ADAPTATION.md) identifica decisiones de HTML/ARIA y límites: Loader interpola de forma continua, ScrollArea usa el motor nativo, PNG conserva resolución de exportación, fondos de Modal/media dependen del consumidor y los gráficos son muestras. Las excepciones aprobadas o pendientes de las fuentes (color, tipografía, TABLE-AUD-001, Toolbar sin overflow y geometría histórica Logos) no quedan resueltas por este QA web. No se afirma una aprobación humana nueva.

No se inventaron servicios, backend, publicación ni estados de producto. No se modificaron datos canónicos, bibliotecas Figma ni las673 bajas que ya estaban preparadas en Git. No se necesita decisión del usuario para consumir las correcciones locales. Una comparación visual exhaustiva no ejecutada sigue identificada como tal, sin convertirla en un requisito nuevo del proyecto.

## Cierre y continuidad

P07 v0.1.1 exige en altas/modificaciones futuras correspondencia de props/defaults, galería, revisión de estados y medición de geometría afectada; build por sí solo no acredita fidelidad. Registro persistente en decisiones, implementación, QA y fuentes.

Graphify permanece STALE durante las ediciones. Lote de cierre completo `2026-10-13-web-fidelity`: respaldo del corte anterior, AST y semántica incremental, integridad/cobertura/manifiesto y readback de JSON/reporte/HTML. CURRENT únicamente si su closure.json y `scripts/ds check` confirman el corpus final. Uso semántico medido UNAVAILABLE, no cero. Dependencias globales y configuración de servicios sin cambios.
