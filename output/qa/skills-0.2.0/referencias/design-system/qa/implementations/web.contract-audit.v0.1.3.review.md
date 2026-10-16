# QA web · cotejo contractual 0.1.3 · 2026-10-13

**Estado:** `PASS_MEASURED_SCOPE`. Las43 familias fueron cotejadas contra contrato, enmiendas y datos canónicos, con correcciones en la implementación web. El resultado no declara igualdad universal por píxel. **Las dos imágenes originales de Modal ya están integradas tras autorización explícita del usuario y verificadas por hash.**

[Resultados y hashes](web-contract-audit-2026-10-13/results.json) · [matriz de43 familias](web-contract-audit-2026-10-13/family-matrix.md) · [725 fixtures de propiedades/Slots](web-contract-audit-2026-10-13/properties-and-slots.json).

## Autoridad y alcance

Solicitud explícita del usuario: «cotejalos todos, no puede existir ni una discrepancia». Se aplicaron P06/P07/P-SLOTS y P05. Se leyeron las43 bases y enmiendas del registro web, snapshots y evidencia técnica vinculada. Cada ficha conserva fuentes/hashes. Los contratos siguen en su estado documental original; no se simula aprobación humana ni publicación Figma.

Se cotejó implementación, API/defaults, anatomía, propiedades de visibilidad, Slots y estilos con las fuentes vigentes. Los valores esperados de tests provienen de contratos y geometría documentada; los tests no leen styles.css para inventar expectativas. Las comparaciones exactas de computed style y caja no usan tolerancias nuevas. El test Characters conserva únicamente la tolerancia0.001 ya autorizada por su contrato para matrices SVG.

Las lecturas live de la Librería anterior mostraron rediseños de Avatar, Toggle y NavigationTab posteriores a sus contratos. Los snapshots `*.live-source-drift.2026-10-13.json` son OBSERVED y no sustituyen las normas. No se cambiaron los componentes para adoptar esos rediseños sin contrato.

## Discrepancias corregidas

- **Acciones y feedback:** alturas/padding/bordes interiores de Button, roles Default/Text/Press/Disabled, subrayado solo de label Link; IconButton Focus/Disabled; Badge25px/fondos/borde; Notification sin borde inventado y sin huecos de contenido oculto; Progress visibilidad del encabezado; tipografía Dot; Loader con24 pasos15° y ciclo1.224s.
- **Formularios:** Input/Search/Select dejaban de conservar48/40/32 en estados de error o Disabled por una regla compartida. Se corrigieron estructura horizontal, halos de foco, orden de prefijo/iconos, ayuda20 y defaults. Textarea conserva superficie108 y total160, helper/counter y colores. Radio ya no hereda el estilo indeterminate de Checkbox. Toggle recupera roles Disabled y sombras. Dropdown Header no es botón; áreas selector/contenido e iconos coinciden. FileUpload conserva trazo5/5 y foco1.5; Disabled no toma Hover.
- **Navegación:** Breadcrumb mantiene anchos120/92/52/42, flecha24 y gaps; Pagination conserva padding16/24/24, gaps12/4, selector102×26 y disabled heredado por su Slot. SwitchTabItem38 y defaults de iconos/conteo; NavigationTab Base42/Dynamic35 con divisor externo22 y foco correcto. StepsCombination es HUG también como export independiente; StepsDot,27 combinaciones y8 conectores de Stepper quedan disponibles sin crear variantes canónicas nuevas.
- **Contenido:** Avatar usa borde interior; EmptyStates conserva regiones visibles vacías y sus seis ilustraciones reutilizables. Table coloca Badge antes del texto y reutiliza los trazados exactos Sort/Copy de546:253/546:256, además del logo434:3657. Fuentes usa la jerarquía Info4/Path8 y Dot local. ScrollbarThumb expone22 posiciones internas; los ocho presets públicos y ScrollArea nativo siguen separados.
- **Composición y chat:** Header conserva release/RFC y ancho de versión170. ChatToolbar restaura control32/surface-brand, logo24, cuerpo mínimo519, plan200×8 con fill56 y crecimiento HUG sin solapamiento. Conversation recupera badge, feedback, padding/gaps, disclaimer, selector y Preview; las acciones por defecto son visuales y no simulan resultados. ChatSection utiliza su pose original Welcome y tipografía32/40 y20/28. BENI/NAVI conservan identidad fija y los13 frames existentes.
- **Modal y Charts:** Close32/icono20 de Media/SideBySide vuelve a x=ancho−56/y=24 sobre la imagen; se corrigió composición centrada de Media y Footer20/24 con gap0. Se preserva la sombra original. Header de Charts conserva mínimo de leyendas76; Detail usa celdas FILL y truncado explícito a una línea. No se convierte el gráfico estático en cálculo de datos.
- **Catálogo:** los títulos externos no gobiernan componentes. Se acotó el fondo Primary a Steps para no ocultar Loader Primary; se separaron los tooltips de muestra y se usa fondo inverso al inspeccionar logos Mode=dark. Son soportes de inspección, sin recolorear artwork.

Fuentes nuevas de lectura: Button, navegación/avatar/toggle live drift, Scrollbar parts, Stepper connectors, Table icons, Modal close/footer en `sources/figma-snapshots/*web-contract-audit.2026-10-13.json`. Metadatos leídos sin modificar Figma. Los generadores conservan hashes y procedencia para los assets derivados.

## Evidencia ejecutable

- `pnpm --dir implementations/web verify`: generación y comprobación de43 fichas, TypeScript, tests de código y build estático. Último build posterior a las correcciones;9 tests unitarios finales PASS, incluidos trazados Table y geometría Characters.
- `pnpm --dir implementations/web test:browser --timeout=120000`:59 pruebas Chrome locales.43 pruebas por familia, tests de catálogo/interacción/geometría/personajes y un recorrido de725 fixtures. El resultado final y conteos exactos están en results.json; no se suman intentos fallidos previos como PASS.
- Las43 pruebas de contrato recorren los cuatro temas y las recetas de galería. En controles aplicables fuerzan Hover/Press con CDP y usan foco real para focus-within. Los JSON por familia guardan actual/expected por propiedad y cualquier fallo. Las capturas muestran Contable de referencia, no cada estado dinámico simultáneamente.
- Los725 fixtures cubren36 familias con booleanas, swaps, listas0/1/3/9, reordenamiento y piezas internas. Cada tema ejecuta2302 comprobaciones de visibilidad, orden y geometría; total9208. Hay crecimiento de Toolbar con30 entradas y leyendas largas a320px. SSR no demuestra retención de estado React; esta se comprueba en los recorridos interactivos existentes de Sidebar y pantallas locales, sin extender esa conclusión a todos los Slots posibles.
- Se inspeccionaron las43 capturas de galería; esa lectura permitió detectar y reparar el soporte visual de Loader/Tooltip/Logos. No se usó una captura aprobada inexistente como golden image.
- Los controles locales de teclado, selección, carga de archivo, Modal/Escape/devolución de foco y conversación/tabla en memoria se prueban sin backend. Axe cubre catálogo/InputField sin color-contrast; no es certificación WCAG ni de todos los lectores de pantalla.

Inventario canónico SHA256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474` intacto. No hay nuevas primitivas, cambios Figma, dependencia añadida, publicación remota ni alteración de las673 bajas preexistentes del índice Git.

## Recuperación de imágenes Modal · resuelta

**WEB-MODAL-ORIGINAL-IMAGES-001: RESOLVED.** El contrato Modal §15 prohíbe certificar Media/SideBySide sin imagen original. La revisión automática de permisos rechazó inicialmente la exportación base64 por falta de autorización específica. El usuario respondió «Sí, copiar ambas imágenes al proyecto». Tras esa autorización se extrajeron los bytes originales desde AI-Design-System y se integraron como defaults locales.

[Manifiesto](../../sources/assets/web/modal.manifest.json): Media561×260/9911bytes, SHA-1 `c501b83c7359259626cc55a14fd37122b56ad90f`; SideBySide341×400/7735bytes, SHA-1 `73f7fc927575ad4cf7008efc6fe4f8a9cb5b27fe`. Ambos SHA-1 de archivo coinciden exactamente con el imageHash de Figma; el manifiesto guarda también SHA-256 y encuadre FILL. Se conservan sin recoloración en los cuatro temas. La extracción no modificó Figma.

El generador valida ambos hashes, copia a public/assets y no requiere Figma durante uso. QA comprueba src, dimensiones naturales/renderizadas580×260/340×404, object-fit:cover y capturas. media permite sustitución explícita y null permite vacío. La autorización y la extracción ocurrieron antes del QA final; el rechazo inicial no permanece como bloqueo activo.

## Límites heredados y cierre

Se conservan las normalizaciones y excepciones del contrato: TABLE-AUD-001, colores/contrastes fuente, geometría histórica de Logos, Scrollbar normalizado y poses estáticas explícitas. Su existencia en la norma no autoriza corregir el diseño silenciosamente. No están verificadas todas las combinaciones arbitrarias de contenido ni la equivalencia de rasterizado entre navegadores.

Código reutilizable, exports, API/defaults y43 fichas técnicas se sincronizaron conforme P07. [Adaptación web0.1.3](../../implementations/web/docs/WEB-ADAPTATION.md). Este reporte reemplaza el alcance de cotejo web0.1.2; los reportes anteriores conservan sus cortes históricos.

Graphify: lote `2026-10-13-web-contract-audit`, respaldo y extracción estructural/semántica del delta. La vigencia se determina en `graphify-out/runs/2026-10-13-web-contract-audit/closure.json` y `scripts/ds check`; esta frase no simula CURRENT. El grafo debe reflejar también la autorización Modal y la evidencia del cierre de imágenes.
