---
contract_id: SELECT-001
name: Select
type: composition
version: 0.1.0
status: DELEGATED_FOR_BUILD
last_updated: 2026-09-29
figma_page_name: Select
review_targets: [figma]
user_audit: PENDING
dependencies: [INPUT-FIELD-001, DROPDOWN-ITEM-001, FOUNDATIONS-TOKENS-001]
---

# Select · contrato de composición 0.1.0

## 1. Purpose
Presentaciones visuales cerrada y abierta de un selector. Alcance: reconstrucción en Figma; no implementación funcional web.

## 2. Contract
REQ-SEL-001 MUST crear un set local `Select`, página existente `Select` 444:122, destino `tj3WIBEZDGLVs7MJWKCwgf`. Fuente de lectura `9zs5RMR8LB5wHjW9Bd59BA`, ejemplos 2488:13364 y 2488:13365. La fuente contiene composiciones, no un set público de Select: convertirlas en dos variantes reutilizables es una normalización de construcción delegada, no un hecho histórico.

## 3. Anatomy
REQ-SEL-002 MUST reutilizar Input Field local como instancia, sin modificar su principal. Open añade Menu absoluto con cinco instancias de Dropdown Item local. Mantener los iconos Eye observados; no inferir su acción ni sustituirlos por chevrons sin decisión. No duplicar masters ni desacoplar instancias.

## 4. Properties
REQ-SEL-003 MUST exponer `Presentation=Closed|Open`, default Closed. Las instancias anidadas Field y Option 1–5 se exponen para edición de sus propiedades existentes, evitando propiedades duplicadas desconectadas. Label=`Drop down`; Text=`Selecciona una opción`; Helper=`Optional helper text`; opciones=`Option text`. Show label, Required, Show helper y Show trailing icon conservan defaults de Input Field. No se amplía el producto cartesiano de estados/tamaños.

## 5. Variants
Closed: Input Field Large/Default/Empty principal 395:206. Open: Input Field Large/Default/Filled principal 395:446 y cinco Dropdown Item Medium/Default/False/Base principal 446:165. Son exactamente dos presentaciones observadas; Open no implica lógicamente Filled en una futura implementación. Se conserva esa combinación de ejemplo sin elevarla a regla de producto.

## 6. Sizes
REQ-SEL-004 MUST conservar envoltura inicial 464×96, campo 464×96 y menú 464×200 situado x=0,y=80. Filas de40px. Menu: auto layout vertical, gap/padding0, radio8, clip=true. Envoltura: auto layout vertical, transparente, clip=false. La huella visual abierta llega a y=280. Dimensiones y anclaje son geometría observada, no tokens GAP usados como tamaño.

## 7. States
No se agregan estados funcionales. Default corresponde al ejemplo. Las propiedades del Field anidado conservan la enmienda Input Field Disabled0.1.1: Filled y Empty Disabled usan color/text/disabled. Otros tamaños/estados anidados no se anuncian como composiciones Select validadas.

## 8. Behavior
REQ-SEL-005 MUST NOT añadir reacciones, selección, apertura por clic, navegación por teclado, cierre exterior ni lógica de carga: no están definidas por la fuente. Presentation es una elección del diseñador. Reacciones propias deben quedar vacías. Animación de Loader oculto es dependencia heredada, no interacción propia de Select.

## 9. Accessibility
No se certifican ARIA ni teclado. Hereda limitaciones de contraste del Field y de Dropdown Item; no recolorear para ocultarlas. Filas40px requieren evaluación contextual táctil. El menú cubre el helper en Open como en la fuente; registrar esta limitación de presentación, no afirmar que el mensaje sigue visible.

## 10. Design tokens
REQ-SEL-006 MUST conservar bindings semánticos locales de las dependencias. JSON canónico `sources/inventories/tokens.inventory.json`, SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`; gobierna nombres, tipos, valores, aliases, modos, scopes y description. No hay nuevas variables ni primitivas ni cambios al inventario.

Menu y envoltura: spacing/none (origen lógico VariableID:1098:28491 → destino VariableID:12:18 → spacing/0 VariableID:8:33), para padding/gap0. Radio Menu: radius/md (origen lógico VariableID:562:4 → destino VariableID:13:6 → radius/8 VariableID:8:38). Cuatro modos6:0–6:3, mismos aliases. Radio de envoltura: radius/none VariableID:12:39.
Las superficies y textos provienen de los contratos de Input Field y Dropdown Item y sus mapas locales, sin fijar un modo. Sus pinturas no se sustituyen por primitivas ni por roles de scope ajeno. Los aliases semánticos y bindings tipográficos de las instancias deben conservarse.

Limitación heredada documentada: las dos etiquetas ocultas del Checkbox escalado dentro de cada Dropdown Item Medium mantienen sus bindings de familia, peso y color, pero sus métricas numéricas están escaladas (11.666666px/16.666666px) y carecen de binding numérico. Select no altera esa dependencia ni declara que esas etiquetas estén totalmente tokenizadas. No son el texto de las opciones. El rol heredado color/border/control se rige por drafts/foundations/ai-design-system.control-colors.v0.1.0.json y su enmienda v0.1.1.json, alias neutral/400 en cuatro modos.

REQ-SEL-007 MUST conservar las dos sombras del menú como excepción literal acotada de P03 §11/P04 §6: el inventario no define categoría de sombras ni sus opacidades, y los únicos efectos locales son de foco, semánticamente incompatibles. No reutilizar focus ni text para simular elevación. Efecto1: DROP_SHADOW #223548 alpha0.30000001192092896, offset(0,2), radius8, spread0. Efecto2: DROP_SHADOW mismoRGB alpha0.47999998927116394, offset(0,0), radius0, spread1. Ambos visibles, NORMAL, showShadowBehindNode=true. Los floats exactos de RGB y las referencias remotas originales se conservan en el snapshot. No importar esas variables remotas. Esta excepción NO constituye tokenización integral ni autoriza otros literales. Se registra con asterisco para auditoría de Foundations; no se crea una primitiva nueva ni un alias ficticio.

## 11. Content rules
Cadenas de ejemplo editables en las instancias expuestas. Cinco filas describen la muestra observada, no un límite de opciones para frontend. Contenido largo hereda truncamiento de Dropdown Item. No inferir valores seleccionados a partir de la cadena placeholder.

## 12. Composition rules
REQ-SEL-008 MUST usar un único set en la página Select existente, separado de Dropdown Item y sus ejemplos, sin mover objetos ajenos. Una guía en español explica alcance, edición anidada y excepción de sombras. El menú se dibuja por encima del helper. No recortar el overflow de la envoltura.

## 13. Responsive behavior
Ancho inicial464. Field y Menu se adaptan al ancho de la instancia; menú con constraints horizontales STRETCH, filas FILL. Validar también ancho320. Anclaje vertical80 corresponde a la configuración Large con etiqueta visible; cambiar tamaño/etiqueta requiere ajustar composición y no está certificado por este bloque. No se prometen breakpoints.

## 14. Edge cases
Helper largo puede quedar oculto detrás de Menu como el helper inicial. Múltiples estados, grupos vacíos, búsqueda, multiselección y número dinámico de opciones UNRESOLVED para producto; fuera de este artefacto visual acotado.

## 15. Forbidden combinations
No construir combinaciones adicionales por inferencia. No bindings de text en superficies/efectos ni primitivas directas. No confundir Open con enabled, ni Filled con editable. No declarar QA global de accesibilidad o publicación de biblioteca.

## 16. Design ↔ Code mapping
Composición cerrada2488:13364 → Presentation Closed; abierta2488:13365 → Presentation Open. Los IDs de destino se registran después de construir. API de código, eventos y semántica web REQUIRES_PRODUCT_DEFINITION.

## 17. Acceptance criteria
REQ-SEL-009 MUST verificar dos nombres únicos, siete instancias directas de dependencias y exposición de todas, geometría464 y320, menu5×40 en y80, radio/spacing vinculados, pinturas reales y semántica/scopes locales, cuatro modos y captura visual. Efectos deben coincidir exactamente con snapshot exceptuando eliminación de referencias remotas. QA documental y técnico separados antes de promoción a specs; auditoría humana PENDING, biblioteca UNPUBLISHED.

## 18. Examples
Closed y Open reproducen los ejemplos fuente. El ejemplo de320px es prueba de integración de ancho, no variante pública adicional.

## 19. Source of truth
Este MD gobierna el alcance delegado; JSON aprobado gobierna variables. Evidencia: `sources/figma-snapshots/select-composition.source.v0.1.0.json`, `sources/figma-snapshots/select.source.v0.1.0.json`; dependencias: `specs/input-field.contract.v0.1.0.md`, `specs/input-field.disabled-text.amendment.v0.1.1.md`, `specs/dropdown-item.contract.v0.1.0.md`. Mapas: `sources/figma-snapshots/select.target-tokens.v0.1.0.json` y mapas de Input Field referenciados por su contrato. La fuente histórica permanece inmutable.

## 20. Change management
Decisión delegada DEC-LEGACY-MIGRATION-DELEGATION-001. Después de QA documental puede pasar a DELEGATED_FOR_BUILD; después de QA técnico se promueve a specs sin aprobación humana simulada. Ajustes posteriores directamente allí, versionados. Graphify STALE, no regenerado.

## 21. Changelog
0.1.0 · 2026-09-29: composición referencial Closed/Open, sin alterar los componentes base; excepción explícita para dos sombras observadas sin categoría canónica equivalente. Promoción documental a specs tras QA documental y técnico acotado PASS; auditoría humana PENDING.
