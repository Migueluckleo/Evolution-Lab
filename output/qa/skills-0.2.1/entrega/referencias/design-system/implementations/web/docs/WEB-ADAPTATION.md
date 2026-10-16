# Adaptación técnica web · 0.1.5

**Estado:** IMPLEMENTED_FOR_LOCAL_PROTOTYPING · decisiones técnicas DERIVED de la solicitud [DEC-WEB-COMPONENTS-001](../../../registry/decisions.md). No cambia el estado de aprobación o auditoría de los contratos visuales. Cada fuente y enmienda aplicable se enlaza con hash desde la [ficha de familia](components/README.md).

## Autoridad y API

La solicitud activa el destino React + TypeScript + Tailwind + Next.js que contratos históricos dejaban fuera de alcance. Los nombres de export, props, HTML, callbacks y estado de demostración son decisiones de esta implementación; no se atribuyen retrospectivamente a Figma. La API TypeScript del código es su único propietario editable; el generador extrae tipos y defaults para las fichas y verifica cobertura con los contratos activos.

`components.registry.json` registra fuentes y notas de implementación, no valores canónicos de diseño. Cada familia explicita REQUIRED o NOT_APPLICABLE para Slots. children, ReactNode y listas con IDs permiten modificar contenido; no prueban Slots Figma. La tabla y navegación aceptan más elementos que el ejemplo. Las cantidades visuales documentadas se conservan cuando constituyen una variante explícita, como los porcentajes del gauge.

## Tokens y unidades

[scripts/tokens.py](../scripts/tokens.py) lee el inventario canónico y las extensiones/enmiendas que enumera. [tokens.manifest.json](../src/generated/tokens.manifest.json) conserva fuentes, hashes, nombres, tipos, modos, valores, aliases y description. No se edita ese manifiesto como otra fuente.

La traducción `/` → `-` genera variables CSS `--ds-…`. Los aliases permanecen como `var(…)`; las primitivas internas usan `--ds-primitive-…` y los componentes consumen roles semánticos. Los cuatro temas preservan sus valores originales. Los tokens directos de character-identity/character-shadow permanecen fijos según las excepciones existentes. Logos conserva su archivo original. No se cambió el JSON histórico.

Decisión técnica de unidades: los FLOAT de geometría y tipografía se convierten numéricamente a px, incluidos line-height y letter-spacing; no se supone conversión a rem ni porcentajes de Figma. El tracking tight -0.01 se conserva como -0.01px en CSS: su equivalencia perceptual con otros motores no está certificada. Los pesos STRING Regular/Medium/Semibold/Bold se traducen a 400/500/600/700 y Manrope se sirve localmente desde @fontsource-variable/manrope. Cuando el contrato declara una medida sin token, el CSS conserva la medida literal; esto no crea una variable canónica.

Button, FilterChip y campos centran el contenido dentro de sus alturas 32/40/48: el padding vertical de auto-layout no se suma al alto en CSS. Texto que envuelva puede requerir crecimiento; no se fija una regla editorial de truncamiento desconocida. La adaptación conserva los gaps del campo, incluido helper de InputField a 4px.

## Interacción local

- Button usa button de tipo button salvo que el consumidor pida submit o href; href crea un enlace. Pseudoestados CSS responden al navegador.
- Checkbox/Radio/Toggle usan controles nativos. Mixed de Toggle usa semántica checkbox mixta y un callback separado; no decide cómo resolver una selección agregada.
- InputField/Textarea muestran error o éxito cuando lo indica el consumidor; no validan negocio. Select añade navegación de teclado y cierre local. required de Select se anuncia con ARIA, no aplica validación nativa de formularios al botón.
- Modal usa dialog.showModal, cancel y close del navegador; Escape informa onOpenChange y la pantalla decide el estado. No cierra por backdrop sin regla contractual.
- Tooltip usa hover/focus y Escape en modo no controlado. asChild conecta aria-describedby al control existente sin duplicar su foco; el wrapper enfocable se reserva a contenido no interactivo. No hay detección automática de colisiones con el viewport.
- FileUpload entrega objetos File locales. accept es una ayuda del selector; el consumidor valida archivos arrastrados, tamaño, formato y permisos si después conecta un backend. success/error son props explícitas, no resultados fabricados.
- NavigationPagination calcula una secuencia compacta a partir de page/pages y expone callbacks; es adaptación técnica web, no algoritmo observado en Figma. Tabs aporta selección y navegación por teclado. La pantalla conserva IDs, páginas válidas y paneles.
- Conversation/ChatSection solo presentan contenido. El ejemplo agrega mensajes locales y no genera respuestas automáticas. Characters permite elegir fotogramas explícitos, sin inferir carga o estado remoto.

## Diferencias deliberadas y límites visuales

Table conserva la anomalía geométrica TABLE-AUD-001: Hover agrega8px de ancho y resta24px a la primera celda explícita. No se corrige silenciosamente una excepción normativa. Scrollbar representa ocho presets visuales fijos; ScrollArea ofrece desplazamiento nativo por separado. Loader utiliza el anillo/remate extraídos, con 24 avances antihorarios de15°, cada uno con pausa1ms e interpolación50ms (ciclo1.224s), y prefers-reduced-motion. Las16 recetas públicas comparten esa secuencia; no se dibujan384 componentes DOM.

Los gráficos conservan geometría de muestra. ProgressChartItem mantiene fills de 580/247px recortados por el contenedor; value es texto y no determina un porcentaje. SemiDonutGauge usa los paths originales 25/50/75. Para datos continuos se necesitaría una decisión de contrato; no se presenta esta pieza como motor analítico.

Sidebar usa las22 recetas de MenuItem, curvas SVG originales, colores por rol, iconos Fill/Light y BETA solo donde está documentado. Mide72/234×885 por defecto; en AppShell llena904px. Submenús y selección se conservan al contraer. TopBar1399×48. La lista y lowerOptions son composición0..n; no se añade Disabled ni Focus de submenú.

ChatToolbar conserva altura mínima791 y ancho79/264, las visibilidades documentadas y la ausencia de overflow central de la fuente. ChatSection aplica los límites de la enmienda de layout. AppShell parte de1440×1024; width/height pertenecen al anfitrión, sin mínimo1024 ni breakpoint de producto inventado. Los componentes anchos se desplazan dentro del catálogo, cuya navegación compacta se prueba a390px.

Conversation usa sus glifos originales de32px; Characters conserva las poses hero completas. El marco del catálogo y backdrop nativo de dialog son composición de la herramienta. La galería permite inspeccionar variantes y activar hover/focus con el navegador; no presenta todos los estados dinámicos simultáneamente.

Avatar, Toggle, Tooltip y Logos conservan las excepciones de sus fuentes. No se recolorea para superar contraste ni se convierte auditoría pendiente en PASS. No se verificaron visualmente todas las combinaciones de estados, todos los navegadores ni lectores de pantalla.

## Assets

[Manifiesto Logos](../../../sources/assets/web/logos.manifest.json): 72 exportaciones originales con IDs/hashes, PNG o SVG según el exportador. Los ocho assets ausentes en0.1.0 se recuperaron de sus IDs originales. PNG no se anuncia como vector. src permite un asset local explícito y un assetId no disponible produce error. La biblioteca se ejecuta sin consultar Figma.

Characters conserva 13 árboles vectoriales del snapshot original de Ecosistema con hash. Desde la corrección web 0.1.1, cada transformación local SVG se obtiene como inversa de la matriz absoluta del padre multiplicada por la absoluta del hijo: los relativeTransform de los ojos en ese snapshot usan coordenadas del componente y no se pueden anidar directamente bajo el grupo. Se conservan paths, jerarquía, pinturas y relación de aspecto. EmptyStates reutiliza seis SVG locales y asigna sus colores a roles del inventario correspondiente; no crea ilustraciones nuevas. Avatar usa la foto del snapshot base64 original. Los generadores copian assets derivados a public y mantienen las fuentes fuera de esa carpeta.

## Verificación

[QA de implementación](../../../qa/implementations/web.contract-audit.v0.1.3.review.md) separa cobertura, compilación, interacción, vista inspeccionada y límites. La prueba de accesibilidad automática cubre el catálogo con InputField y excluye color-contrast por las excepciones conocidas; no certifica las 43 familias ni WCAG. Toda alta o modificación sigue [P07](../../../protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md).

## Cotejo de contratos 0.1.3

Los43 contratos y sus enmiendas se cotejan con CSS/API y mediciones del navegador. La matriz de QA enlaza los valores comprobados, sus fuentes y las capturas por familia; no convierte un resultado medido en igualdad universal por píxel. Los pseudoestados se fuerzan en Chrome y el foco de campos es real. La prueba de Slots por SSR comprueba orden, vacío y visibilidad; no acredita por sí sola conservación de estado React.

Se exponen las piezas StepsDot/StepsCombination, StepperConnector, ScrollbarThumb, EmptyStateIllustration y ChatWelcome para composición independiente. ScrollbarThumb conserva las22 posiciones internas documentadas sobre el track272 normalizado en la implementación Figma; los presets públicos continúan14×280 y280×16. TableGlyph comparte los trazados locales Sort/Copy; Show brand usa el logo original434:3657. Los Slots aceptan vacío explícito. Las acciones de feedback predeterminadas de Conversation son visuales; el consumidor suministra callbacks mediante feedbackActions y no se simula copia o envío.

ChatSection usa la pose de bienvenida original, distinta de los fotogramas de Characters. ChatToolbar contiene el logo original y control32, crece con sus regiones HUG y mantiene cuerpo mínimo519; colapsado conserva región695. Modal sitúa Close32 en x=ancho−56/y=24 sobre la imagen, con icono20. Las dos imágenes raster originales de Media/SideBySide se recuperaron tras autorización explícita del usuario. Sus SHA-1 coinciden con Figma y el manifiesto local añade SHA-256, tamaño y encuadre FILL (object-fit:cover). Se usan por defecto sin recoloración; media permite reemplazarlas o vaciar con null.

Las lecturas live de la antigua Librería muestran cambios posteriores en NavigationTab, Toggle y Avatar. Se conservan como OBSERVED; no reemplazan los contratos vigentes. La tipografía porcentual documentada de Stepper/Dot/Pagination conserva su conversión relativa explícita; no se aplica la regla general de FLOAT en px a un porcentaje histórico.


## Centralización tipográfica 0.1.4

El [contrato de tipografía](../../../specs/foundations/typography.contract.v0.1.0.md) y su [JSON único](../../../specs/tokens/ai-design-system.typography.v0.1.0.json) gobiernan actualmente los 18 estilos base y los 57 complementarios: 54 de compatibilidad y tres derivados de escala. [TYPOGRAPHY.md](TYPOGRAPHY.md) es la tabla de uso derivada; [typography.manifest.json](../src/generated/typography.manifest.json) conserva fuente, hash, versión, métricas, referencias y descripciones. El censo [anterior a la centralización](../../../sources/figma-snapshots/typography/) aporta observaciones por página, receta y rango; las evidencias de cada complemento citan sus contratos y usos concretos. Un nombre de estilo o una coincidencia numérica no sustituyen esa procedencia.

`scripts/typography.py` integra la generación CSS/TypeScript/documentación en `pnpm ds:generate` y verifica determinismo con `pnpm ds:check`. PERCENT de interlineado se divide entre 100 y se emite sin unidad; PERCENT de tracking se divide entre 100 y se emite en em; PIXELS permanece px; AUTO se traduce a normal. Las referencias existentes de familia, peso, tamaño, interlineado y tracking se conservan como `var(...)` cuando son compatibles con la unidad y el valor. Los tamaños micro 4/8 sin rol del inventario conservan su literal únicamente en el catálogo canónico y sus derivados. La conversión FLOAT histórica de `tokens.py` permanece intacta: esta regla explícita de recetas no reinterpreta el inventario.

`styles.css` asigna recetas completas por rol y variante. Los helpers genéricos de tamaño conservan solo geometría; no seleccionan una tipografía por coincidencia de tamaño. ChartLegendLabel y MenuItem seleccionan `typographyClass(id)` tipada según sus props y recetas. `typography`, `typographyIds`, `typographyClass` y `TypographyId` se exportan desde `src/index.ts`. Las clases y consumidores declaran `--ds-type-style-id`; QA y handoff pueden leerlo con `getComputedStyle`, junto con las métricas efectivas. Una propiedad heredada no acredita por sí sola coincidencia: deben comprobarse los valores renderizados. `line-height:0` de los wrappers de indicadores continúa siendo una decisión geométrica.

La migración conserva cajas, padding, gaps, colores, assets, estados y API. Corrige diferencias tipográficas cotejadas: Button usa tracking 0.1% (los botones de acción de 16px en Modal/EmptyStates conservan su receta contextual con tracking 0); Avatar, Dot medio, NavigationTab, versión Header y BETA Sidebar usan AUTO donde está documentado; contador Textarea, elipsis Pagination, Breadcrumb acortado, gauge, preview Conversation y contador del plan recuperan sus pesos. Breadcrumb actual y empresa Header son Regular, la empresa usa tracking 0.1%, Modal link usa 16/24 y títulos de sección ChatToolbar usan 14/20. Estas correcciones no reinterpretan Slots arbitrarios ni aplican la jerarquía base a toda la UI por tamaño.

El título local de `AppShellExample` consume Heading 5/Semibold de la nueva base (24px, 133%, tracking −2%); es contenido de la composición de ejemplo y no una propiedad de AppShell. El marco de navegación del catálogo (`app/catalog.css`) es composición de documentación y queda fuera de las recetas de las 43 familias. El texto de Slots aportado por una pantalla puede elegir otro estilo canónico explícito; centralizar los defaults no fija cardinalidad ni contenido de esos Slots. El interlineado AUTO y el ancho de glifos dependen del motor y la fuente realmente cargada; la validación web comprueba Chrome con Manrope local y no certifica igualdad entre motores.

La prueba `tests/browser/typography.spec.ts` compara actualmente las 75 clases con el JSON canónico en los cuatro temas, comprueba Manrope cargada y utilizada mediante CDP, y coteja el texto de las variantes de las 43 familias con su identidad efectiva. Se mantienen además los checks de geometría, estados y Slots existentes. Los resultados de cada corte se registran por separado del QA histórico de 0.1.3; ejecutar las pruebas y revisar sus resultados es requisito para declarar PASS.

Validación local histórica del corte de 72 estilos: generación determinista, TypeScript, 8 pruebas Python del generador, 9 pruebas unitarias de componentes y build estático PASS; suite Chrome 61/61 PASS, con 20,860 comprobaciones contractuales de 43 familias. Las pruebas específicas verificaron 288 recetas (72 × 4 temas) y 2,956 textos de variantes. La inspección visual adicional se limitó a las capturas Header y Conversation; no se atribuye inspección manual a las demás capturas ni se certifica Figma desde este resultado web.


## Recetas escaladas de compatibilidad 0.1.5

El corte posterior amplía el catálogo a **75 estilos: 18 base y 57 complementarios**. Añade `ui-checkbox-label-scaled-two-thirds`, `ui-checkbox-label-scaled-five-sixths` y `micro-count-small-scaled-four-thirds` para preservar 103 rangos existentes del destino Figma (14, 76 y 13 respectivamente), cuya escala materializa métricas y requiere una identidad de estilo explícita. Sus usos y evidencia permanecen en el JSON único; este documento no redefine las recetas.

`derivedFrom` registra receta de origen, razón, ratio y factor FLOAT32. El generador valida exactamente `FLOAT32(base × FLOAT32(ratio))` para tamaño e interlineado PIXELS, conserva medidas porcentuales y emite los valores ya materializados sin redondearlos ni aplicar otra escala. Las tres clases son adicionales: no reasignan recetas a los consumidores web existentes ni añaden transforms. Se conserva intacto el corte QA de 72 estilos; [la revisión de 75](../../../qa/implementations/typography/web/revision-75/README.md) registra el nuevo hash y la comprobación afectada.

Validación afectada del corte de 75: 9 pruebas Python, determinismo, TypeScript y build estático PASS; 2 pruebas Chrome PASS, con 300 recetas (75 × 4) y 2,956 textos de las 43 familias en cuatro temas. Las mediciones de consumidores y los hashes de CSS/componentes/API son idénticos al corte de 72. La suite completa de 61 pruebas conserva su evidencia histórica y no se repitió para esta ampliación de clases adicionales.
