---
contract_id: EMPTY-STATES-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
target: figma
page_name: Empty states
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node_id: "7772:2272"
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
slot_applicability: REQUIRED
---
# Empty states

## 1. Purpose
Mostrar ausencia de datos y acciones opcionales. OBSERVED: descripción del set fuente7772:2272. No se infieren reglas de negocio, errores, carga ni permisos.

## 2. Contract
REQ-ES-01 MUST construir cuatro presentaciones Default, Compact, Inline, Main en una sola página funcional **Empty states**. Delegación DEC-LEGACY-MIGRATION-DELEGATION-001, auditoría posterior. No modificar la fuente ni dependencias principales locales.
REQ-ES-02 MUST conservar estructura visual de la muestra y seis ilustraciones vectoriales reutilizables. Las envolturas privadas .Base Empty State y .Visual se normalizan dentro del set público; no son nuevas familias ni variantes públicas.

## 3. Anatomy
Ilustración única intercambiable; bloque de título/descripción; regiones Main actions y Supporting actions. Dos Slots nativos REQUIRED por composición variable; textos TEXT y visibilidad BOOLEAN, ilustración INSTANCE_SWAP: estos últimos no requieren Slot. Seis artworks reutilizables privados, anatomía fija NOT_APPLICABLE.

## 4. Properties
Presentación: Use case (VARIANT). Title y Description (TEXT). Show title, Show visual, Show main actions, Show supporting actions (BOOLEAN). Illustration (INSTANCE_SWAP). Main actions y Supporting actions (SLOT).
Los Slots se comparten entre variantes para retener contenido. Etiquetas/estados de botones editables en instancias anidadas, sin detach. Defaults visibles salvo Inline: título, visual y acción principal ocultos. Supporting visible en todas.
Los valores iniciales distintos de Illustration y de visibilidad Inline requieren claves de propiedad independientes por presentación; se documentan los IDs reales sin forzar un único default que altere los presets. Los Slots y textos siguen compartidos.

## 5. Variants
| Use case | Fuente | Ancho muestra | Alto observado | Ilustración |
|---|---|---|---|---|
| Default | 7772:2273 | 696 | 532 | 280×280 |
| Compact | 7772:2275 | 696 | 366 | 150×150 |
| Inline | 7772:2277 | 696 | 120 | Oculta |
| Main | 7772:2279 | 696 | 572 | 500×320 |

No producto cartesiano adicional. Altura HUG, no fijar por el ejemplo.

## 6. Sizes
Padding24 Default/Main;16 Compact/Inline. Separación visual/texto32 o16 respectivamente; título/descripción4. Ancho del texto máximo500; ancho del anfitrión editable. Geometría de ilustraciones150/280/500×320 conservada como dimensiones observadas, no escala de tokens inventada.

## 7. States
Presets de contenido, no estados de interacción. Inline es una composición sin título/visual/acción principal. No añadir Loading, Disabled o Error a la familia. Estados de botones pertenecen a Buttons.

## 8. Behavior
REQ-ES-03 MUST usar Buttons locales primary/link, middle, default; mantener vínculo y propiedades. No copiar IDs de reacciones de la fuente a otro archivo. Interacciones de botones serán las locales ya existentes. Destinos de acción de producto UNRESOLVED y fuera del alcance Figma.

## 9. Accessibility
No certificar WCAG ni teclado/ARIA desde Figma. Texto principal sobre superficie blanca; acciones brand dependientes del modo. Contrastes medidos se registran en QA con asterisco donde aplique. Ilustraciones decorativas sin significado funcional.

## 10. Design tokens
REQ-ES-04 MUST consumir variables semánticas locales. [Inventario canónico](../sources/inventories/tokens.inventory.json), SHA256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474; nombres, tipos, aliases, modos, scopes y description se delegan al JSON, no a este MD. [Mapa preflight](../implementations/figma/empty-states.v0.1.0.tokens-preflight.json), colección semantic6:2; no elegir primitives homónimas.
| Consumidor | Rol |
|---|---|
| Texto título/descripción | color/text/primary |
| Botón principal | color/interactive/primary/default; color/text/inverse; color/icon/on-brand |
| Acción secundaria | color/text/brand; color/icon/brand |
| Tipografía base | font/family/base; weight/bold o regular; size/xl o sm |
| Título Main | font/family/base; weight/medium; size/lg; line-height/md |
| Interlineado | font/line-height/md para títulos; sm para descripción |
| Tracking | font/letter-spacing/normal |
| Layout | spacing/none,xs,sm,md,lg,xl,2xl |
| Geometría de Buttons anidados | spacing/sm para gap/padding vertical; spacing/lg horizontal; radius/md para esquinas; overrides locales que conservan8/16/8px |
| Ilustraciones | seis roles de FOUNDATIONS-EMPTY-STATES-001 |

REQ-ES-05 MUST aplicar [extensión](foundations.empty-states-roles.amendment.v0.1.0.md) antes de ilustraciones. Aproximaciones de decoración explícitas, no nuevas primitivas. Los colores de máscaras geométricas se conservan únicamente como geometría no visible. Main normaliza Poppins18 Medium/Figtree14 a Manrope20 Medium/14 Regular; tracking fuente-0.5% pasa a normal porque tight no equivale a esa unidad. Estas diferencias se registran como normalización delegada a auditoría, no como igualdad original.
Los textos de Buttons anidados normalizan el peso Bold al token local font/weight/bold y tracking a font/letter-spacing/normal (heredaban un alias externo y0.1% literal). Se mantienen mains y colores; el ajuste es un override de consumidor documentado. Las ilustraciones se transfieren como SVG editable de la fuente; las máscaras geométricas no visibles quedan excluidas del alcance de tokenización de paints visibles.

## 11. Content rules
Title/Description editables con salto de línea y altura automática, centrados. Texto inglés fuente solo demo. No inventar mensajes de producto. Acciones conservan etiquetas Main action/Read more iniciales y pueden reemplazarse por consumidor.

## 12. Composition rules
REQ-ES-06 MUST implementar Slots nativos **Main actions** y **Supporting actions** en las cuatro variantes. Cada región inicia con un botón (aunque Main actions está oculto en Inline), cardinalidad editable0..n sin máximo de negocio declarado. Operaciones insertar/quitar/reordenar/sustituir desde instancia. Contenido recomendado: Buttons locales, no coerción global de estados.
Contenedor vertical centrado, ancho disponible FILL, alto HUG, gap8. Padding superior16(Default/Main) o12(Compact/Inline) en Main actions;8 en Supporting actions. Vacío conserva padding de región si está visible; ocultar región elimina su espacio. Pruebas0/1/2/5 son fixtures, no límites.
Show/hide y cambio de Use case deben conservar contenido y overrides; una ilustración personalizada puede conservar tamaño propio y no autoajustarse al cambiar preset. No modificar mains de Buttons.

## 13. Responsive behavior
REQ-ES-07 MUST comprobar reflow de textos a360px, sin clipping. Ilustración Display de500px requiere ancho mínimo548px con padding24; no prometer mobile para esa geometría. Default/Compact/Inline se prueban a360. No se inventa breakpoint de producto.

## 14. Edge cases
Slots vacíos, cantidades superiores a muestra, etiquetas largas, texto largo y cambio de variantes probados. Acciones muy largas dependen de ajuste de ancho del botón; no inventar truncamiento silencioso. Ilustración mayor que contenedor requiere espacio suficiente o swap apropiado.

## 15. Forbidden combinations
MUST NOT usar primitivas como fills de UI, roles text en shapes, refs a variables externas, reacciones a nodos fuente, componentes aplanados o Slots simulados por frames. No llamar error/success a las ilustraciones decorativas.

## 16. Design ↔ Code mapping
Solo Figma. Web, teclado, ARIA, callbacks, navegación y lógica de ausencia de datos UNRESOLVED; no implementación React autorizada. Propiedades nativas no prueban comportamiento de navegador.

## 17. Acceptance criteria
AC-ES-01: cuatro variantes/página única/artworks fieles en geometría (REQ01–02).
AC-ES-02: textos y booleanas editables; Buttons locales y fuentes intactas (REQ03).
AC-ES-03: readback completo de colores/tipografía, scopes/aliases por cuatro temas; extensión JSON idéntica (REQ04–05).
AC-ES-04: SLOT-QA01–09; instancia vinculada,0/1/2/5 hijos, insertar/quitar/reordenar/sustituir, retención y temas (REQ06).
AC-ES-05: revisar composición renderizada, medidas y texto largo, respetar mínimoMain (REQ07).
Auditoría humana PENDING y biblioteca UNPUBLISHED separados del QA técnico.

## 18. Examples
Revisión compacta con instancias de las cuatro presentaciones y seis ilustraciones, principales fuera del frame. No copiar las páginas de documentación externas.

## 19. Source of truth
Este MD rige decisiones de construcción. [Resumen fuente](../sources/figma-snapshots/empty-states.v0.1.0.summary.json), [layout](../sources/figma-snapshots/empty-states.v0.1.0.frames.json), [detalles](../sources/figma-snapshots/empty-states.v0.1.0.details.json), [variables fuente](../sources/figma-snapshots/empty-states.v0.1.0.variables.json) son evidencia OBSERVED, no norma independiente. Raíz3027:406, sección7772:2225, set7772:2272. Lectura433nodos,27ocultos; dependencia de botón e icono resuelta para su uso observado, sin auditar1512alternativas.

## 20. Change management
P03/P04/P05/P06 y P-SLOTS0.1.0. Promover a specs solo tras QA documental y técnico PASS; cambios siguientes directamente en specs con revisión. No publicar biblioteca por implicación.

## Estado de implementación
QA técnico/visual PASS acotado, auditoría humana PENDING, biblioteca UNPUBLISHED. Página639:128, set645:275, revisión649:291. [QA](../qa/implementations/empty-states.v0.1.0.figma.review.md), [ledger](../implementations/figma/empty-states.v0.1.0.state.json) y [bindings finales](../qa/implementations/empty-states.v0.1.0.bindings.json).31 roles/124 aliases cotejados; el mapa final incluye radius/md y overrides de consumidores que amplían el preflight inicial.

## 21. Changelog
0.1.0 · 2026-10-05 · Reconstrucción delegada desde librería raíz, dos Slots, integración tipográfica local y seis roles semánticos para decoración.
