---
amendment_id: COMPOSITION-SLOTS-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
last_updated: 2026-09-29
review_targets: [figma]
user_audit: PENDING
protocol: P-SLOTS/0.1.0
---

# Slots de composición · enmienda 0.1.0

## Autoridad y alcance

Solicitud explícita del usuario: revisar componentes y aplicar P-SLOTS desde el contrato hasta Figma. Decisión DEC-SLOTS-IMPLEMENTATION-001. Esta enmienda gobierna únicamente las regiones descritas abajo; no altera el inventario JSON, colores, interacciones ni requisitos restantes de los contratos base. No equivale a publicación de biblioteca ni aprobación humana. Su implementación y QA se registran separadamente.

| Contrato propietario | Localizador base | Secciones/requisitos sustituidos parcialmente | Aplicabilidad |
|---|---|---|---|
| SELECT-001 0.1.0 | [Select](select.contract.v0.1.0.md) | REQ-SEL-002/003/004/008/009; Anatomy, Properties, Sizes, Content, Composition, Edge cases, Acceptance | REQUIRED: cantidad y orden de opciones, solicitud explícita |
| NAVIGATION-SWITCH-TAB-001 0.1.0 | [Switch Tab](navigation-switch-tab.contract.v0.1.0.md) | Anatomy, Properties, Composition, Change management; AC-NAV-ST-001/002 | REQUIRED: grupo de pestañas de longitud variable; criterio delegado sobre anatomía observada |
| BREADCRUMBS-001 0.1.0 | [Breadcrumbs](../drafts/contracts/breadcrumbs.contract.v0.1.0.md) | Región Items de composiciones; conteo de ejemplo y aceptación geométrica correspondiente | REQUIRED: profundidad variable de la ruta; criterio delegado sobre anatomía observada |

La base histórica de Breadcrumbs permanece en su ubicación verificada, sin promoverla ni atribuirle una revalidación cromática por este cambio. Esta enmienda vigente se mantiene en specs. Las reglas de tokens posteriores aplicables conservan su autoridad.

## Anatomy y Properties

| Región semántica | Anfitrión destino | Contenido recomendado | Muestra inicial | Operaciones |
|---|---|---|---|---|
| Options | Select 457:470, Closed/Open | Instancias locales Dropdown Item 446:528 | cinco Medium/Default/False/Base | insertar, quitar, reordenar, sustituir y editar propiedades de cada opción |
| Tabs | Switch Tab 283:128 | Instancias locales Switch Tab Item 276:395 | cuatro: Active y tres Default | insertar, quitar, reordenar, sustituir y editar propiedades de cada pestaña |
| Trail | Breadcrumbs 191:229, Level 2–5 | Instancias locales Breadcrumb 190:210 | 2, 3, 4 y 5 respectivamente | insertar, quitar, reordenar, sustituir y editar propiedades de cada elemento |

REQ-SLOTS-001 MUST implementar cada región como nodo nativo SLOT vinculado a una propiedad SLOT. No sustituir por un frame con nombre Slot, booleanas por índice o una colección de variantes por conteo. Las propiedades de texto/boolean/swap de los hijos permanecen en las instancias. Las preferencias de contenido guían la inserción; no atribuirles bloqueo técnico sin evidencia. No desacoplar instancias ni duplicar principales.

REQ-SLOTS-002 MUST conservar los principales y sus IDs. Select convierte Menu 456:440 y añade una región homóloga oculta en Closed, vinculada a la misma propiedad para preservar contenido al cambiar Presentation. El menú cerrado no se vuelve visible. Switch Tab añade un contenedor de contenido y conserva sus cuatro hijos. Breadcrumbs convierte los cuatro frames Items conservando sus hijos. Level conserva sus nombres como presets históricos, no como conteo calculado ni máximo permitido. Cambiarlo no debe borrar overrides del contenido.

## Composition, tamaños y contenido

REQ-SLOTS-003 MUST conservar los valores visuales y bindings existentes. Select: Options vertical, ancho del campo, altura hug de filas, padding/gap cero, radio8 y dos sombras históricas sin modificación; anclaje x0/y80, host464×96 sin clipping. Filas Medium40, FILL horizontal. Cinco filas dan200px; listas mayores crecen y desbordan el host como overlay. No se añade scroll o altura máxima.

Switch Tab: Tabs horizontal hug, gap4, sin padding adicional; el anfitrión conserva padding4, radio8 y fondo. La muestra sigue488×46. Breadcrumbs: Trail horizontal hug con el gap y tamaño de filas existentes, ArrowLeft fuera de la región; el anfitrión crece en ancho. No se añaden wrap, truncamiento de ruta ni scroll automáticos; ancho reducido puede producir overflow y debe documentarse. No cambiar la tipografía o los colores para corregirlo.

REQ-SLOTS-004 MUST separar muestras de límites. No hay min/max de producto definidos; no imponerlos ni prometer cardinalidad ilimitada. Probar estructuralmente cero hijos sin añadir mensaje, selección, redirección o política de estado vacío. La semántica de una lista/ruta/grupo vacío y la exclusividad de selección continúan UNRESOLVED para producto. Las operaciones de autoría Figma sí quedan dentro del alcance. El autor debe mantener orden, selección y último elemento coherentes; el Slot no los calcula automáticamente.

### Ajuste de dependencia descubierto en QA

REQ-SLOTS-003b MUST permitir que los ítems textuales Breadcrumb crezcan con su etiqueta para evitar solapamiento al editar contenido del Slot. La primera captura de ocho elementos mostró texto largo sobrepuesto porque el texto era HUG pero el componente permanecía FIXED. Alcance adicional acotado: principales190:189/190:202/190:206/190:208, eje horizontal HUG con ancho mínimo histórico120/120/92/92 y altura24 conservada. No modifica Icon, Shortened, colores, texto por defecto, propiedades o IDs. Sustituye solo la interpretación de ancho fijo de Sizes/Composition/AC-BRC-002 para estas cuatro variantes. Registrar impacto en consumidores y repetir QA de la ruta; no certificar otras composiciones sin lectura.

## Tokens y capacidad

REQ-SLOTS-005 MUST mantener variables semánticas, scopes, aliases y herencia de cuatro modos. El JSON canónico y extensiones vigentes de cada base gobiernan los valores; no crear tokens por añadir Slots. Preservar las excepciones históricas de sombras y métricas ocultas de Select, sin declarar tokenización integral.

Capacidad documentada: figma-use/references/component-patterns.md, sección Slots: createSlot and SLOT Properties; plugin-api-standalone.d.ts, ComponentNode.createSlot, SlotSettings y SlotNode. Se documenta conversión de frame con componentPropertyReferences.slotContentId, propiedad SLOT y edición de hijos desde instancia. La lectura real de Select confirmó createSlot disponible; la prueba de escritura y consumidor debe confirmar la capacidad completa antes de PASS.

## Acceptance criteria

REQ-SLOTS-006 MUST ejecutar SLOT-QA-01…09 por familia y guardar IDs/readback. Casos: muestra; un hijo; menor y mayor que muestra; cero estructural; agregar/quitar/reordenar/sustituir desde consumidor enlazado; texto largo; ancho reducido; modos6:0…6:3; cambio de variante cuando exista. Cantidades concretas son datos de prueba, no límites de producto. Verificar preservación de contenido personalizado, dependencias, pinturas y propiedades.

Un comportamiento que no pase se registra FAIL/BLOCKED y se corrige o limita explícitamente; no se oculta tras QA anterior. No se certifican teclado, ARIA, navegación o lógica frontend. Para pruebas se crean instancias identificadas, separadas de ejemplos ajenos; no modificar otros consumidores.

## Trazabilidad y cambios

Evidencia de selección: contratos enlazados y lectura actual de páginas Select444:122, Navigation275:122 y Breadcrumbs190:188. [Matriz de adopción](../registry/SLOTS-REVIEW-STATUS.md). QA y estado se guardarán bajo qa/implementations y implementations/figma con prefijo composition-slots.v0.1.0. Graphify consultado como índice derivado, permanece STALE sin regeneración.

0.1.0: revisión delegada de tres composiciones, sin modificación de paleta ni aprobación humana simulada.
