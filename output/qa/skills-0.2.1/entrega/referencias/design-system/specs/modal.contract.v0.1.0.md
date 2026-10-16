# MODAL-001 · Modal · v0.1.0

Estado: `DELEGATED_FOR_BUILD`. Auditoría humana: `PENDING`. Alcance Figma delegado por DEC-LEGACY-MIGRATION-DELEGATION-001. No significa publicación de biblioteca.
Página semántica de destino: **Modal**, ID `565:122`. Basic `567:360`, Media `569:301`, SideBySide `569:327`. Revisión visual `578:301`. QA técnico PASS; biblioteca UNPUBLISHED.

## 1. Purpose
Diálogo visual con cabecera, contenido sustituible y acciones. Propósito DERIVED de la estructura; lógica de negocio fuera del alcance.

## 2. Contract
REQ-MOD-01: construir en AI-Design-System `tj3WIBEZDGLVs7MJWKCwgf` desde la Librería raíz, no desde Anticipa.
Inventario: Basic (seis variantes), Media y SideBySide; helpers privados Header y Footer (dos variantes cada uno). No agregar estados de producto.
Fuente: página4886:869; Basic7419:38329; Media7419:38363; SideBySide7419:38372; Header7419:38401; Footer7419:38385.
Evidencia: [snapshot](../sources/figma-snapshots/modal.v0.1.0.source.json), 359 nodos,131 instancias,17 dependencias principales,29 variables observadas.
La captura preserva campos mixtos como MIXED; los segmentos leídos muestran texto neutral y sufijo de marca sin hyperlink.

## 3. Anatomy
Basic = Header + Body(SLOT) + Footer. Media = Image + Content + Close + Footer. SideBySide = Content(Header+Body) + Image + Close, seguido de Footer.
Header conserva Title, Subtitle, Icon opcional y Close. Footer contiene Side content y Actions; reutiliza botones locales.
Los placeholders amarillos “Replace me” son indicaciones editoriales de la fuente, no contenido de producto ni color normativo. Body empieza vacío con altura de demostración conservada, sin crear una variable amarilla de relleno.

## 4. Properties
Basic: Size=Small/Medium/Large; Scroll=No/Yes; Body nativo; Header y Footer expuestos.
Header: Title y Subtitle TEXT; Show subtitle, Show icon, Show link y Show close BOOLEAN; Icon INSTANCE_SWAP. Separar el texto de marca de muestra en Link text editable evita rangos rotos al editar Subtitle.
Footer: Side content y Actions SLOT; sin máximo técnico artificial. Botones mantienen sus propiedades de texto, iconos y estado.
Media/SideBySide: Image INSTANCE_SWAP; Close visible; Media tiene Title/Content TEXT y Footer expuesto; SideBySide tiene Body SLOT y Header/Footer expuestos. Media no requiere Slot en el bloque de título/texto de cardinalidad fija. No convertir cantidad de acciones en variantes.

## 5. Variants
REQ-MOD-02: seis combinaciones observadas Size×Scroll de Basic; Media y SideBySide no tienen ejes adicionales.
Header y Footer privados: Scroll=No/Yes. El estado Scroll muestra divisores/sombra; no define eventos de desplazamiento ni cierre.

## 6. Sizes
Anchos Basic480/580/840. Alturas fuente Small266/320, Medium383/383, Large400/400 para No/Yes.
Header fuente112, Footer80. Body74/128/191/208 según muestra, padding lateral32 e inferior32.
Media580×466 con imagen260; SideBySide840×480, cuerpo400, columnas500/340.
REQ-MOD-03: conservar anchos y las alturas mínimas del cuerpo de muestra; componentes crecen cuando contenido variable lo exige en Scroll=No. Scroll=Yes conserva viewport del cuerpo y clipping vertical documentado.
Tipografía normalizada: título24/32 y texto16/24 frente a24/30 y16/22 de la fuente. Header base116; Basic vacío270/324/387/404 con Footer base80; el QA registrará geometría real contra las fórmulas, no contra una falsa identidad exacta. Footer crece cuando las acciones requieren más filas; padding vertical20.
Tracking normal0 sustituye -0.1px del título. Decisión delegada explícitamente documentada para consumir la escala existente, sin modificar primitivas.

Geometría final comprobada: Small270/324, Medium387/387, Large404/404, Media580×472, SideBySide840×484. Normalización tipográfica +4px en Basic/SideBySide y +6px en Media. Subtitle text tiene máximo352px (480−64padding−60link−4gap); el contenido lateral del pie máximo216px, derivado de la mitad del ancho útil de Small. Son restricciones de layout de escritorio, no límites de cantidad. Padding vertical20 del Footer conserva geometría literal observada: no existe un token spacing20 en el JSON.

## 7. States
Sin estado global disabled/loading/error inventado. Los controles locales conservan sus propios estados. Scroll es configuración visual observada.
Botones precargados son ejemplos de acciones; sus etiquetas no definen reglas de producto.

## 8. Behavior
REQ-MOD-04: no copiar la reacción ON_CLICK→NAVIGATE con destinationId=null como navegación válida.
Cerrar con X, Escape, clic en backdrop, focus trap, devolución de foco y resultados de acciones: UNRESOLVED para frontend. No bloquear composición visual por estas reglas externas.
No afirmar que Scroll=Yes implementa teclado o desplazamiento web.

## 9. Accessibility
No certificación WCAG. Mediciones contra blanco: texto primary17.853:1; texto/botón de marca Servicios3.236:1*; divisor neutral1.233:1*; borde Checkbox2.564:1*. Los asteriscos documentan revisión interna, no cambian los colores ni se imprimen en la UI. Medir texto y separadores con roles canónicos; conservar colores y marcar limitaciones con asterisco.
La X ocupa32×32 como fuente. La semántica dialog/modal, nombre accesible y foco son responsabilidades futuras de frontend.
El texto de marca “and link.” es una muestra sin URL; no presentarlo como enlace funcional.

## 10. Design tokens
REQ-MOD-05: [JSON canónico](../sources/inventories/tokens.inventory.json), SHA256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
Nombres/tipos/modos/aliases/description delegados exclusivamente al JSON. [Mapa final local](../implementations/figma/modal.v0.1.0.local-token-map.json): 34 tokens locales y 136 aliases comparados con cero discrepancias, incluyendo dependencias. Los mapas previos de 21 y 32 tokens quedan como evidencia histórica.
Superficie→color/background/default; texto→color/text/primary; sufijo→color/text/brand; iconos→color/icon/primary; divisor→color/border/strong.
Tipografía→font/family/base, weight/bold o regular, size/xl o md, line-height/xl o md, letter-spacing/normal. Spacing→none/xs/sm/lg/xl/2xl; radius→md/xl; stroke→xs.
Reutilizar Buttons26:81 (middle primary/default), Scrollbar330:194 y Checkbox149:179 cuando aparezcan en contenido inicial. No modificar sus mains.
Sombra de Modal: literal observado negro0.3, offset0/15, blur50. Footer Scroll: negro0.2, offset0/6, blur20. Se conserva excepción de categoría sombra ausente en JSON, como estilos compartidos privados de Modal; no usar tokens de texto en efectos.
Imágenes son contenido raster original, no pinturas semánticas de interfaz. Conservarlas mediante dependencia importada verificada; no recolorearlas por tema.
REQ-MOD-06: los roles de marca de texto y botones heredan los cuatro modos. Ningún modo de marca se fija en componentes públicos. Sin variables ni primitivas nuevas. Las dependencias añaden font/size/sm y line-height/sm para Caption14/20. [Control0.1.0](../drafts/foundations/ai-design-system.control-colors.v0.1.0.json) conserva descripción/scopes y [enmienda0.1.1](../drafts/foundations/ai-design-system.control-colors.v0.1.1.json) gobierna su alias; [Scrollbar0.1.1](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.1.json) gobierna el thumb. Los cambios locales de tracking solo afectan instancias de botones dentro de Modal, no el main Buttons.

## 11. Content rules
Title, Subtitle, Link text y etiquetas de botones editables. No inventar límites de caracteres. Title reserva espacio de cierre para no solaparse; texto largo crece.
“Modal title”, “Secondary”, “Main CTA”, “Don’t show again” y “Side actions text” son ejemplos, no normas de producto.
Body vacío no significa estado vacío de producto; mantiene la región estructural mínima.

## 12. Composition rules
P-SLOTS0.1.0: REQUIRED. Body permite componentes de contenido del DS,0..n; Actions permite controles locales,0..n; Side content permite texto/checkbox u otras composiciones locales,0..n.
REQ-MOD-07: insertar, quitar, reordenar y sustituir desde instancias consumidoras, conservando vínculos, overrides y tokens. No detach.
Body es vertical, FILL ancho, padding32 lateral/inferior. Scroll=No HUG con mínimo de muestra; Scroll=Yes viewport fijo con clipping; contenido puede excederlo.
Actions es horizontal WRAP, gap8 y alineación derecha; el pie crece si necesita más filas. Side content es FILL, vacío permitido. Los ejemplos2acciones no son máximo.
Header y Footer expuestos permiten editar sus slots sin cambiar principales. Imagen única usa swap, NOT_APPLICABLE Slot por cardinalidad fija.
Los Slots no retokenizan automáticamente el contenido insertado: cada componente consumidor debe cumplir su propio contrato. Los botones precargados de Modal usan bindings locales verificados sin modificar el principal de Buttons.

## 13. Responsive behavior
Los anchos observados son presets de escritorio, no breakpoints web. Probar480 y contenido largo. No prometer diseño móvil320px; SideBySide conserva columnas fuente.
El consumidor puede redimensionar, pero el contrato no asegura legibilidad fuera de los anchos comprobados.

## 14. Edge cases
REQ-MOD-08: probar Body0/1/3, Actions0/1/2/4, reordenamiento, cambio de Scroll/Size y conservación de texto. Verificar clipping intencional en Scroll.
Texto extenso no debe superponerse a X. Side content vacío no crea mensajes ni controles ficticios.

## 15. Forbidden combinations
No títulos usados como iconos; no roles text en fills de superficies; no primitivas directas; no colores de marca literales; no duplicación de Buttons ni publicación automática.
No certificar Media/SideBySide si la imagen original no se recupera. Se verificaron hashes c501b83c7359259626cc55a14fd37122b56ad90f y73f7fc927575ad4cf7008efc6fe4f8a9cb5b27fe; no se sustituyeron por placeholders.

## 16. Design ↔ Code mapping
Figma controla composición, Slots y variables. Implementación React/TypeScript/Vite no autorizada en esta ejecución. Sin API de eventos inventada.

## 17. Acceptance criteria
REQ-MOD-01–08 verificables en fuente, snapshot, mapa y destino. Ocho configuraciones públicas; cuatro helpers de cabecera/pie; una páginaModal.
[QA de implementación](../qa/implementations/modal.v0.1.0.figma.review.md): captura posterior, readback de todos los paints efectivos y bindings, scopes/aliases, 25 pruebas de Slots/composición desde instancias y cuatro temas. El readback final confirma cero referencias externas en el alcance auditado. Se corrigieron cinco referencias heredadas de spacing, radius, stroke y fontStyle en instancias visibles de Buttons dentro de Modal, con valores resueltos idénticos; no eran geometría oculta de iconos. No se modificó ni se declara auditoría global del principal de Buttons.
Si falla un requisito, no promover su alcance a specs ni declararloVALIDATED.

## 18. Examples
Revisión compacta con instancias BasicSmall/Medium/Large y ambas configuraciones Scroll, Media y SideBySide. Principales fuera del marco de ejemplos. Pruebas temporales eliminadas tras guardar evidencia.

## 19. Source of truth
Este contrato gobierna reconstrucción; JSON gobierna tokens; snapshot solo evidencia histórica. Aplican P03/P04/P05/P06/P-SLOTS y MIGRATION-TOKEN-TRACEABILITY con enmienda0.1.2.
Una vez promovido, revisiones normativas directamente en specs.

## 20. Change management
No tocar Table ni otros principales; no regenerar Graphify en esta tarea. Guardar IDs reales y QA en implementaciones/registros. Diferencias de tipografía y ausencia de lógica funcional quedan en auditoría por excepciones.

## 21. Changelog
2026-10-01: v0.1.0; extracción desde raíz, mapeo21tokens, Slots de contenido/acciones y normalización tipográfica documentada. Construcción y QA técnico cerrados:25pruebas de composición,123paints,53textos y392comparaciones de tema. Publicación documental delegada, no aprobación humana.
2026-10-01, cierre de evidencia: mapa final ampliado a 34 tokens y 136 aliases por localización de bindings heredados en consumidores de Buttons. Sin cambio de valores visuales, variables nuevas ni modificación de principales ajenos. Se corrige la clasificación preliminar errónea de esas referencias como geometría oculta.
