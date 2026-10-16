# HEADER-001 · Header · v0.1.0

Estado: `DELEGATED_FOR_BUILD`. Auditoría humana: `PENDING`. Delegación: DEC-LEGACY-MIGRATION-DELEGATION-001 y orden «Dale» para la siguiente familia Header (2026-10-01). No representa aprobación humana ni publicación de biblioteca.

## 1. Propósito
Cabecera de escritorio con identidad de categoría, versión, acciones, empresa y perfil. Propósito de destino DERIVED de la composición observada; los destinos de navegación no están definidos por la fuente.

## 2. Contrato
Una composición pública **Header**, página semántica exclusiva **Headers** en AI-Design-System `tj3WIBEZDGLVs7MJWKCwgf`. No crear estados ni variantes de cantidad inexistentes. La fuente permanece inmutable.
P-SLOTS: **REQUIRED** para Actions (0..n); **NOT_APPLICABLE** para textos, logo, empresa y perfil, cuya anatomía es fija y se controla con propiedades.

## 3. Anatomía
Header → Logo Categoria + Content. Content → Version + Actions + Company + User.
Version incluye número, etiqueta preliminar y divisor. Actions contiene Slot nativo con Icon Button locales. Company incluye divisor, icono AppWindow, empresa, RFC y caret. User incluye divisor, Avatar y caret.
Reutilizar logo-categoria435:2653, Icon Button183:311, Avatar165:231 y sus Dots locales; no modificar sus mains.
Comparación acotada de los cuatro artworks de categoría: mismos conteos, trazados y pinturas; delta geométrico máximo0 en los mains comparados. Esta verificación no cierra el QA global de Logos.

## 4. Propiedades
- BOOLEAN: Show version, Show actions, Show company, Show user; true por defecto. Ocultan el grupo completo con sus separadores asociados.
- TEXT del Header: Version (`2.0.0`), Release label (`ALPHA .1`), Company (`Empresa SA de CV`), Tax ID (`CAC840428RH1`). Initials (`JA`) permanece editable en Avatar expuesto; no se duplica una propiedad sin enlace real.
- SLOT: Actions. Cinco elementos iniciales, min0, max sin límite; insertar, borrar, reordenar o sustituir instancias sin detach.
- La categoría del logo sigue la variable local `logo/categoria`; solo selecciona artwork agnóstico, nunca recolorea vectores.
- Los Icon Button dentro del Slot conservan Icon/Show count/Style/Size/State y los swaps propios. No replicarlos como variantes del Header.

## 5. Variantes
Un componente sin ejes de variantes de cabecera. El helper fuente icon header tiene Amount1–5 (48,104,160,216,272px); son muestras históricas, no cardinalidad máxima. Se sustituye funcionalmente por el Slot, no se publica otro helper con cantidad fija.

## 6. Tamaños
Baseline observado1143.6909×96px; padding24; hijos principales48px; gapacciones8; iconosmedianos24.
Logo de referencia175.6909×48; grupo versión170, acciones296 con paddingderecho24, empresa304 y perfil136.
Destino: el contenedor del logo local conserva175.7922px de ancho natural (≈0.1013px respecto a la instancia fuente); artwork principal comparado sin diferencias. Las otras cuatro regiones conservan170/296/304/136px.
Las dimensiones de assets, objetivos y layout son geometría contractual literal cuando no existe token de dimensión compatible; no reutilizar spacing como WIDTH_HEIGHT.
El texto RFC pasa de188 a160px disponibles para evitar el desbordamiento fuente, conservando el tamaño y color tipográfico.

## 7. Estados
No agregar estados globales Default/Hover/Disabled al Header. Los controles anidados conservan sus estados. No presentar menús abiertos inexistentes.
La etiqueta ALPHA es contenido de demostración, no cálculo de ciclo de versión.

## 8. Comportamiento
Figma documenta composición y edición; no navegación funcional, permisos, actualización de datos, menú de empresa o perfil. Acciones de producto: UNRESOLVED fuera del alcance visual.
Show actions=false conserva el contenido insertado al volver a true. Slot vacío no genera acciones ficticias. Si se quiere retirar también el espacio del grupo, usar Show actions=false.

## 9. Accesibilidad
Medición de destino sobre blanco: texto empresa Servicios3.236:1*; extremo violeta de etiqueta con texto blanco4.389:1*. Avatar Servicios conserva3.236:1* según su rol vigente. Asterisco documental, no añadido al componente. No garantiza contraste de texto en toda la superficie del gradiente.

Frontend deberá proporcionar nombres accesibles a acciones y selectores, foco/teclado y semántica de cabecera. No se declara WCAG PASS por construir Figma.
Conservar colores existentes incluso si el contraste es limitado; medir los pares relevantes y marcar con asterisco en la auditoría. No corregir paleta silenciosamente.
Los targets principales de acción son48px. El icono32px de empresa es interno a un selector de48px.

## 10. Design tokens
Autoridad: [inventario aprobado](../sources/inventories/tokens.inventory.json), SHA256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`, más [extensión Header](../drafts/foundations/ai-design-system.header-release.v0.1.0.json). Aplican [trazabilidad](MIGRATION-TOKEN-TRACEABILITY.contract.md) y enmienda0.1.2.
Dependencias de datos heredadas: [Dot backgrounds0.1.0](../drafts/foundations/ai-design-system.dot-background-colors.v0.1.0.json), [Avatar roles0.1.0](../drafts/foundations/ai-design-system.avatar-roles.v0.1.0.json) con [override0.1.1](../drafts/foundations/ai-design-system.avatar-roles.v0.1.1.json) exclusivamente para Servicios.
La extensión añade tres roles, ninguna primitiva: dos fondos FRAME_FILL para stops de gradiente y un icono STROKE_COLOR para el caret de perfil. Descripciones canónicas solo en JSON.
Degradado observado #844AEC→#2868FD; aproximación por menor distancia RGB a primitivas existentes: purple400 #A146FB y blue400 #3255F7. Ambos stops fijos en los cuatro modos, como el acento de versión observado; no sustituyen los roles de marca de empresa/perfil.
Caret perfil #0F172A coincide exactamente con neutral900. Usar color/icon/header-caret-stroke, nunca token de texto como stroke.
Empresa, superficie de perfil y Avatar siguen roles semánticos de marca por modo. Los artwork de logos conservan sus literales por excepción explícita.
Tipografía: Manrope Regular/Bold disponibles; family/style/size vinculados. AUTO line-height de versión se conserva para no cambiar22pxobservados; no hay variable de tipoAUTO. Empresa20px y RFC16px usan line-height/sm y xs. Tracking0 usa normal; empresa0.1% permanece literal por falta de primitiva equivalente en unidad compatible.
Bindings remotos de iconos se reemplazan en las instancias consumidoras por variables semánticas locales de color; no se cambia la biblioteca Phosphor.

| Token consumido | ID real de destino | Scope |
|---|---|---|
| spacing/xl | VariableID:12:33 | GAP |
| radius/none | VariableID:12:39 | CORNER_RADIUS |
| spacing/none | VariableID:12:18 | GAP |
| spacing/sm | VariableID:12:30 | GAP |
| color/text/primary | VariableID:13:27 | TEXT_FILL |
| font/letter-spacing/normal | VariableID:12:16 | LETTER_SPACING |
| font/size/md | VariableID:10:10 | FONT_SIZE |
| font/weight/regular | VariableID:10:3 | FONT_STYLE |
| font/family/base | VariableID:10:2 | FONT_FAMILY |
| spacing/xs | VariableID:12:29 | GAP |
| radius/sm | VariableID:13:5 | CORNER_RADIUS |
| color/background/header-release-start | VariableID:516:122 | FRAME_FILL |
| color/background/header-release-end | VariableID:516:123 | FRAME_FILL |
| color/text/on-brand | VariableID:13:33 | TEXT_FILL |
| stroke/xs | VariableID:12:41 | STROKE_FLOAT |
| color/border/subtle | VariableID:13:14 | STROKE_COLOR |
| size/4xl | VariableID:12:26 | WIDTH_HEIGHT |
| radius/md | VariableID:13:6 | CORNER_RADIUS |
| size/xl | VariableID:12:23 | WIDTH_HEIGHT |
| color/icon/primary | VariableID:13:20 | SHAPE_FILL |
| size/md | VariableID:12:21 | WIDTH_HEIGHT |
| radius/full | VariableID:13:11 | CORNER_RADIUS |
| color/background/notification-count | VariableID:154:125 | FRAME_FILL |
| color/border/on-brand | VariableID:13:18 | STROKE_COLOR |
| font/weight/bold | VariableID:10:6 | FONT_STYLE |
| spacing/lg | VariableID:12:32 | GAP |
| color/border/brand | VariableID:13:16 | STROKE_COLOR |
| color/interactive/primary/default | VariableID:13:57 | FRAME_FILL, SHAPE_FILL |
| size/lg | VariableID:12:22 | WIDTH_HEIGHT |
| color/icon/on-brand | VariableID:13:23 | SHAPE_FILL |
| color/text/brand | VariableID:13:32 | TEXT_FILL |
| font/size/sm | VariableID:10:9 | FONT_SIZE |
| font/line-height/sm | VariableID:12:8 | LINE_HEIGHT |
| color/text/secondary | VariableID:13:28 | TEXT_FILL |
| font/size/xs | VariableID:10:8 | FONT_SIZE |
| font/line-height/xs | VariableID:12:7 | LINE_HEIGHT |
| color/icon/brand | VariableID:13:25 | SHAPE_FILL |
| radius/2xl | VariableID:13:9 | CORNER_RADIUS |
| color/surface/brand | VariableID:13:69 | FRAME_FILL, SHAPE_FILL |
| color/background/avatar-fallback | VariableID:164:122 | FRAME_FILL |
| font/size/lg | VariableID:10:11 | FONT_SIZE |
| font/weight/semibold | VariableID:10:5 | FONT_STYLE |
| color/icon/header-caret-stroke | VariableID:516:124 | STROKE_COLOR |
| logo/categoria (selección, no pinturas) | VariableID:13:80 | ALL_SCOPES (STRING) |

## 11. Reglas de contenido
Version, release, empresa, RFC e iniciales son editables y sus defaults son ejemplos. Company y Tax ID usan una línea con truncado en160px; conservar acceso al texto completo en producto. No imponer RFC de ejemplo como validación legal.
Cada acción mantiene una instancia y su identidad; no convertir iconos en texto o dibujarlos manualmente.

## 12. Composición
Slot Actions horizontal HUG, gap8, preferencia Icon Button local, sin restricción rígida a cinco. Puede recibir otra composición pertinente al producto; el consumidor debe mantener altura compatible48px.
Logo/Avatar se insertan como instancias locales. Los iconos Phosphor activos se importan por key observada; no sustituirlos por aproximaciones gráficas.

## 13. Responsive
Desktop horizontal, NO_WRAP y SPACE_BETWEEN según fuente. No se inventa menú móvil ni breakpoints.
Para más acciones o textos de versión largos, el consumidor amplía el Header o reduce composición; ancho1143.69 es baseline, no promesa de que cualquier cardinalidad cabe allí. QA con siete acciones usará ancho suficiente y registrará el límite de320px como no soportado; no ocultar solapamientos con un PASS responsive universal.

## 14. Edge cases
Probar0/1/3/5/7 acciones, reordenar, Show actions off/on, texto largo de empresa/RFC, cuatro temas y composición reducida. Verificar herencia y no detach. Quitar todas las acciones no cambia empresa ni perfil.
Al ocultar grupos, sus divisores viajan con ellos como en la anatomía fuente; no inventar lógica condicional de separadores entre grupos.

## 15. Combinaciones prohibidas
Texto utilizado como fondo/icono; primitiva aplicada directamente a UI; recolorear logos; duplicar Header por cantidad de acciones; detach para editar Slot; IDs de origen fingidos como destino; llamar navegación funcional a un ejemplo estático; declarar aprobación humana o publicación Figma.

## 16. Design↔Code
Mapeo orientativo: Header, version/releaseLabel/company/taxId/initials, showVersion/showActions/showCompany/showUser, actions[]. No autoriza implementar React ni una API final; el comportamiento requiere definición de producto.

## 17. Criterios de aceptación
Contrato versionado y evidencia completa; QA documental antes de escritura; extensión JSON y Figma iguales en nombre,tipo,scope,description y cuatro aliases; fuente sin cambios.
Componente único con cinco textos y cuatro booleanas funcionales; Slot nativo editable sin detach; iconos activos correctos; variantes locales reutilizadas; artwork intacto; captura y lectura independiente.
QA debe distinguir geometría, color, composición, accesibilidad pendiente y excepciones. Publicar documentalmente en specs únicamente después de QA técnico afectado PASS.

## 18. Ejemplos
Baseline cinco acciones (actualizar, formación, soporte, aplicaciones y notificaciones); copia con tres; copia con siete a mayor ancho; versiones en Contable, Administrativo, Servicios y Personas. Son muestras, no permisos o navegación definidos.

## 19. Source of truth
QA documental e implementación técnica PASS al cierre del2026-10-01. Componente518:123, página518:122, Slot518:124. [QA detallado](../qa/implementations/header.v0.1.0.figma.review.md). Biblioteca UNPUBLISHED y auditoría humana PENDING.

Fuente visual: [Header observado](../drafts/contracts/header.source.component-contract.md) y YAML asociado; snapshots header.source, header.dependencies y header.source-variables0.1.0.
Contrato normativo: este MD; datos de tokens delegados al inventario y extensión citados. IDs destino y readbacks: [ledger](../implementations/figma/header.v0.1.0.state.json).
No promover el grafo ni una captura a autoridad normativa. Logos generales siguen con QA parcial y resto OMITTED_BY_USER.

## 20. Gestión de cambios
Excepción técnica registrada antes de construir: CaretDown Outline Regular fuente355:77922 es local y su key no es importable; Select no contiene equivalente y la búsqueda no devolvió coincidencia. Reproducir su SVG exacto observado en instancia2412:278 como helper privado de24px, con color/icon/brand. No redibujar ni sustituir por otro icono.
Ajustes futuros en specs tras promoción; versionar o enmendar con alcance explícito. Cambios de slots/props exigen prueba en instancias. Extensiones de tokens sincronizan JSON,Figma y evidencia antes de consumo.
Publicación documental no publica biblioteca Figma. Auditoría humana por excepciones PENDING.

## 21. Changelog
2026-10-01 · 0.1.0 · Síntesis y delegación de Header. Mejora: Slot de acciones, cinco campos editables y corrección de ancho RFC. Tres roles semánticos acotados; dos aproximaciones del gradiente a primitivas existentes. Sin nuevos colores primitivos, sin otros logos ni familias modificadas.
