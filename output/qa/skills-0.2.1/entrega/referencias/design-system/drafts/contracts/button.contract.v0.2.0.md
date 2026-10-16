---
contract_schema: sdd-project/0.2
contract_id: BUTTON-001
name: Button
type: component
status: IN_REVIEW
version: 0.2.0
base_version: 0.1.0
owner: null
last_updated: 2026-09-23
review_targets:
  - figma
sources:
  - SRC-FIGMA-BUTTON-001
  - SRC-FIGMA-PHOSPHOR-001
  - SRC-BTN-CONFIG-001
  - SRC-GUIDE-MATERIAL-001
  - SRC-GUIDE-CARBON-001
  - SRC-GUIDE-APPLE-001
  - SRC-GUIDE-TAILWIND-001
data_refs:
  - sources/figma-snapshots/button-26-81.snapshot.json
  - drafts/contracts/button.contract.yaml
dependencies:
  - BUTTON-001@0.1.0
  - AMD-BUTTON-PAGE-001
  - PHOSPHOR-ICONS-001
  - FOUNDATIONS-TOKENS-001
---

# Button · revisión candidata 0.2.0

Esta versión propone reglas de uso y documentación. El [contrato 0.1.0](../../specs/components/button.contract.md) y la [enmienda Buttons](../../specs/components/button-page-name.amendment.md) siguen siendo la especificación aprobada. Sus REQ-BTN-001–009, AC-BTN-001–009 y [datos técnicos YAML](button.contract.yaml) se incorporan por referencia sin cambiar valores, variantes, propiedades, interacciones, iconos ni bindings. Las reglas REQ-BTN-010–019 de este documento son candidatas hasta aprobación humana; ninguna regla externa se adopta automáticamente.

## 1. Purpose

Button presenta una acción disponible en el contexto actual. La elección del tipo comunica jerarquía, el tamaño responde al espacio y a controles vecinos, y el estado representa una condición visual. La variante visual link requiere especial cuidado: el nodo Figma no demuestra semántica de enlace ni comportamiento web. Este propósito de producto es una propuesta INFERRED, no una intención histórica probada por Figma.

## 2. Contract

| ID | Requisito candidato | Fuerza | Procedencia | Fuente | Verificación |
|---|---|---|---|---|---|
| REQ-BTN-010 | Elegir type por la matriz de §5; no colocar dos primary competidores en un mismo grupo de decisión. | SHOULD | INFERRED | Material, Carbon, Apple | AC-BTN-010 |
| REQ-BTN-011 | Elegir size por la matriz de §6 y mantener el mismo tamaño en un grupo de acciones. | SHOULD | INFERRED | Carbon; tamaños observados en Figma | AC-BTN-011 |
| REQ-BTN-012 | Documentar los cinco states como condiciones visuales sin convertirlos en garantía de eventos reales. | MUST | OBSERVED + INFERRED | Figma; Tailwind | AC-BTN-012 |
| REQ-BTN-013 | Usar en cada instancia una etiqueta visible, breve y específica; el texto Default es solo valor inicial del maestro. | SHOULD | INFERRED + OBSERVED | Carbon, Material, Apple; Figma | AC-BTN-013 |
| REQ-BTN-014 | En instancias de producto, usar cero o normalmente un icono, y ocultar los dos si no aportan claridad; conservar los dos PlusCircle como defaults técnicos del maestro 0.1.0. | SHOULD | INFERRED + OBSERVED | Carbon; Figma | AC-BTN-014 |
| REQ-BTN-015 | Reservar el slot izquierdo para identificar acción u objeto y el derecho para indicar avance, apertura o dirección. Usar ambos solo si comunican significados distintos y pasan revisión UX. | SHOULD | INFERRED, adaptación local | Material, Carbon, Apple | AC-BTN-015 |
| REQ-BTN-016 | No usar la apariencia link para una mutación de datos; antes de web, resolver semántica de navegación y destino. | MUST NOT | INFERRED | Carbon; Figma no demuestra semántica | AC-BTN-016 |
| REQ-BTN-017 | No declarar validados teclado, WCAG, objetivo táctil, bloqueo de disabled ni web a partir de este documento o del Figma. | MUST NOT | límite de evidencia | Figma; Apple | AC-BTN-017 |
| REQ-BTN-018 | Tras aprobación, incorporar un resumen fiel de estas reglas en Description del component set Buttons; enlazar documentación solo mediante URL pública verificable. | MUST | EXPLICIT + OBSERVED | solicitud del usuario; captura y readback Figma | AC-BTN-018 |
| REQ-BTN-019 | Todo icono usado en cualquiera de los dos slots debe permanecer vinculado por identidad de componente a Phosphor Icons. | MUST | EXPLICIT | DEC-ICONS-001 | AC-BTN-019 |

Los MUST de una versión IN_REVIEW son propuestas, no obligaciones vigentes. Material, Carbon y Apple respaldan principios generales, pero la asignación a los cuatro tipos locales y el significado por lado son decisiones propuestas para este sistema. Tailwind solo informa estilos de estado.

## 3. Anatomy

Sin cambios respecto de 0.1.0: componente de 60 variantes con icono izquierdo, label-text e icono derecho; el wrapper btn-default de default/focus permanece. Los slots de icono pueden ocultarse de forma independiente en instancias; no se elimina ningún nodo del maestro.

## 4. Properties

Sin cambios respecto de 0.1.0: type = primary/default/text/link; size = large/middle/small; state = default/hover/press/disabled/focus; texto editable; visibilidad y swap independientes por lado. Los defaults técnicos siguen siendo primary, large, default, texto Default y dos PlusCircle visibles. Un default de propiedad no prescribe uso en todos los productos.

## 5. Variants

| type | Cuándo y dónde usarlo | Evitar |
|---|---|---|
| primary | Acción principal del grupo de decisión, como guardar o completar; pie de formulario, diálogo o paso con salida dominante. | Dos primary que compitan en el mismo grupo; una acción destructiva sin patrón danger aprobado. |
| default | Alternativa neutral o secundaria, como Volver o Cancelar; puede ser acción independiente de importancia media si el contexto no tiene principal. | Tratarlo como equivalente exacto al secondary de Carbon o hacerlo competir visualmente con primary. |
| text | Acción terciaria de apoyo en encabezados, tarjetas, estados vacíos o herramientas. | Cierre crítico de flujo o acción que necesite énfasis alto. |
| link | Acceso contextual a ayuda, detalle o destino relacionado en prototipos, junto al contenido que lo explica. | Mutar datos; asumir que el estilo visual ya ofrece semántica de enlace. |

Los cuatro tipos tienen tres tamaños y cinco estados: 4 × 3 × 5 = 60 combinaciones Figma observadas. Para decidir cualquiera se aplica una fila de esta sección, una de §6 y una de §7. No hay 60 intenciones de producto distintas. Los tipos de otros sistemas no se mapean 1:1 a estos nombres.

## 6. Sizes

| size | Alto técnico | Icono / texto | Uso propuesto | Precaución |
|---|---:|---|---|---|
| large | 48 px | 24 / 16 px | CTA destacado en área espaciosa o panel expresivo. | No agrandar para compensar una etiqueta ambigua. |
| middle | 40 px | 20 / 16 px | Formulario, diálogo y acciones habituales junto a controles de 40 px. | No mezclar tamaños en el mismo grupo. |
| small | 32 px | 20 / 14 px | Tabla, barra de herramientas o contenedor denso. | 32 px de altura visual no demuestra objetivo táctil suficiente. |

Los anchos observados con Default y dos iconos no son anchos fijos: la disposición horizontal es HUG. El default técnico size=large no obliga a usar large. La recomendación contextual se adapta de Carbon; los píxeles proceden de Figma.

## 7. States

| state | Cuándo mostrarlo | Lo que no demuestra |
|---|---|---|
| default | Acción disponible en reposo. | Activación real. |
| hover | Puntero sobre acción disponible. | Soporte de hover en todos los dispositivos. |
| press | Presión o activación en curso. | Click, release o transición completa. |
| focus | Enfoque visible en una explicación de navegación por teclado. | Orden de tabulación, activación o WCAG. |
| disabled | Acción temporalmente no disponible; explicar por qué y cómo habilitarla cuando corresponda. | Supresión real de eventos. |

Tailwind distingue hover, active, focus-visible y disabled como selectores de estilo; no gobierna el comportamiento. Las 23 reacciones observadas en Figma son parciales.

## 8. Behavior

Esta revisión no modifica interacciones. Se conservan las 23 reacciones de 0.1.0, incluidos dos destinos default/focus middle|small que cambian a default/large/hover. Elegir una variante state en un mockup no implementa mouse, tacto ni teclado. Resolver el ciclo real de estados requiere otra decisión y QA. Para web, comprobar focus-visible, active y disabled en la ejecución real, no inferirlos del diseño.

## 9. Accessibility

La etiqueta visible debe expresar la acción y el icono solo reforzarla. Icon-only no queda autorizado por este contrato. El stroke focus de 2 px observado no prueba contraste ni criterio WCAG. Los altos 48/40/32 px no equivalen automáticamente a áreas táctiles adecuadas; Apple recomienda espacio de activación suficiente, pero aquí no se reclama cumplimiento de ningún umbral. La semántica web de link y el tratamiento RTL de posiciones e iconos direccionales quedan UNRESOLVED.

## 10. Design tokens

Sin cambios: 35 variables observadas (26 locales, nueve remotas) y sus bindings están en el [YAML técnico](button.contract.yaml). No se introducen valores de Material, Carbon, Tailwind o Apple ni descripciones paralelas para tokens.

## 11. Content rules

En instancias de producto, nombrar el resultado esperado con verbo y, si ayuda, objeto: Guardar cambios, Añadir cliente, Ver detalles. Usar estilo de frase y terminología consistente. Default permanece como placeholder técnico, no como etiqueta publicable. Evitar etiquetas vagas cuando el siguiente paso no sea obvio. Si se abre otra pestaña o destino, hacerlo claro mediante texto o icono significativo. Longitud máxima, wrapping, truncamiento y localización siguen UNRESOLVED.

## 12. Composition rules

| Composición | Cuándo usar | Ejemplo semántico |
|---|---|---|
| Solo texto | Primera opción si la etiqueta explica la acción. | Guardar cambios |
| Icono izquierdo + texto | Pictograma reconocible que identifica acción u objeto antes de leer. | Añadir cliente con PlusCircle |
| Texto + icono derecho | Pictograma que anticipa continuación, apertura o dirección. | Abrir reporte con icono de salida |
| Ambos + texto | Excepción: dos significados distintos y revisión UX. | Sin ejemplo normativo |
| Solo icono | Fuera de alcance; requiere contrato y nombre accesible propios. | UNRESOLVED |

Los dos PlusCircle visibles son defaults del maestro, no recomendación para cada instancia. Carbon prescribe icono final en su propio sistema; Material Web permite inicio o final. Esta distribución semántica por lado es una adaptación local INFERRED para Buttons, pendiente de aprobación. Si se usan iconos en un grupo, mantener criterio coherente sin agregar ruido.

Cualquier swap debe conservar vínculo por key con [Phosphor Icons](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=7484-1322&t=5f3sI6AFFHMgcXfl-1). La lista de 1512 candidatos no los vuelve apropiados semánticamente. La inversión de símbolos para RTL necesita regla propia; no invertir logos ni signos universales automáticamente.

## 13. Responsive behavior

Sin cambios: ancho HUG, alto por size y auto-layout horizontal. No se observan breakpoints, ancho completo, wrapping ni adaptación móvil. La elección contextual de size no constituye una regla responsive automática.

## 14. Edge cases

| Caso | Tratamiento |
|---|---|
| Texto vacío / icon-only | No usar en esta familia sin contrato separado. |
| Ambos iconos ocultos | Composición normal recomendada si la etiqueta basta. |
| Ambos iconos visibles | Solo con dos significados distintos y revisión UX; se conserva el default del maestro. |
| Texto largo o multilínea | UNRESOLVED; probar contenido real antes de aprobar tratamiento. |
| Icono no disponible en Phosphor | No sustituir por otra fuente sin nueva decisión. |
| Acción destructiva | UNRESOLVED: no existe type danger. |
| Objetivo táctil small | UNRESOLVED por plataforma. |
| disabled y eventos | UNRESOLVED en ejecución real. |
| Modos de variables | QA visual por modo no ejecutado. |

## 15. Forbidden combinations

No se elimina ninguna de las 60 combinaciones técnicas. Restricciones de uso propuestas: no link para mutación; no icon-only; no publicar Default como etiqueta; no tratar disabled visual como bloqueo; no usar iconos ajenos a Phosphor; no duplicar iconos redundantes; no usar primary neutro para destrucción sin patrón danger. En un grupo pueden mezclarse types por jerarquía, pero se recomienda un size consistente.

## 16. Design ↔ Code mapping

| Concepto | Figma | Intención propuesta | Web |
|---|---|---|---|
| type | Cuatro variantes | Jerarquía de §5 | Prop y semántica UNRESOLVED |
| size | Tres variantes | Densidad de §6 | Área táctil y responsive UNRESOLVED |
| state | Cinco variantes | Condición de §7 | Eventos y focus-visible UNRESOLVED |
| texto | Propiedad TEXT | Acción específica | Nombre accesible UNRESOLVED |
| iconos | Boolean + swap por lado | Significado de §12 | API y RTL UNRESOLVED |
| página | Buttons, aprobado | Familia exclusiva | N/A |
| Description | Vacía en readback | Publicar resumen tras aprobación | N/A |
| Documentation link | Lista vacía | URL pública de versión aprobada, si existe | N/A |

Tailwind es referencia futura para estilos de estado, no una API de este contrato.

## 17. Acceptance criteria

AC-BTN-001–009 permanecen por referencia a 0.1.0. Los siguientes criterios solo aplican tras aprobación de esta versión.

| ID | REQ | Comprobación |
|---|---|---|
| AC-BTN-010 | REQ-BTN-010 | Tabla de los cuatro types con contextos y anti-usos; no se atribuye mapeo 1:1 a otras bibliotecas. |
| AC-BTN-011 | REQ-BTN-011 | Tres sizes con valores observados, contexto, consistencia de grupo y advertencia táctil. |
| AC-BTN-012 | REQ-BTN-012 | Cinco states documentados; se separa apariencia de eventos. |
| AC-BTN-013 | REQ-BTN-013 | Pauta de etiqueta y Default identificado como placeholder. |
| AC-BTN-014 | REQ-BTN-014 | Se distingue el default del maestro de la composición de producto. |
| AC-BTN-015 | REQ-BTN-015 | Ambos lados, ninguno y caso doble documentados como adaptación INFERRED. |
| AC-BTN-016 | REQ-BTN-016 | link diferencia navegación de mutación y deja semántica web pendiente. |
| AC-BTN-017 | REQ-BTN-017 | No se declara QA de teclado, WCAG, touch target ni web. |
| AC-BTN-018 | REQ-BTN-018 | Tras aprobación, readback de Description del set 26:81 coincide con resumen aprobado; link solo si URL pública verificada. |
| AC-BTN-019 | REQ-BTN-019 | Todo swap usado resuelve como instancia de Phosphor por key. |

Cobertura: cada una de las 60 variantes hereda exactamente una fila de §5, una de §6 y una de §7. No se inventan 60 excepciones.

## 18. Examples

| Configuración | Uso propuesto | Iconos |
|---|---|---|
| primary / large / default | Completar flujo en panel amplio. | Ninguno, salvo aporte claro. |
| primary / middle / focus | Guardar cambios con enfoque visible en formulario. | Ninguno. |
| default / middle / default | Cancelar junto a acción principal de diálogo. | Ninguno. |
| text / small / hover | Acción auxiliar de tabla bajo puntero. | Uno solo si ayuda. |
| link / small / default | Ver ayuda relacionada en prototipo. | Derecho de apertura si aclara; web pendiente. |
| cualquier type / size / disabled | Acción indisponible junto a explicación. | Sin asumir bloqueo real. |

Son escenarios de elección candidatos, no nuevas variantes ni evidencia de comportamiento. El ejemplo técnico Default con dos PlusCircle permanece en la biblioteca.

## 19. Source of truth

| Fuente | Rol |
|---|---|
| [BUTTON-001 0.1.0](../../specs/components/button.contract.md) y [enmienda Buttons](../../specs/components/button-page-name.amendment.md) | Baseline aprobado y validado en Figma para ese alcance. |
| SRC-FIGMA-BUTTON-001 y SRC-FIGMA-PHOSPHOR-001 | Estructura, valores técnicos y procedencia de iconos observados. |
| SRC-BTN-CONFIG-001 | Captura del campo Description vacío y Link vacío; complementada con readback Figma. |
| SRC-GUIDE-MATERIAL-001 | Material Web: jerarquía, etiqueta y posición opcional de icono. |
| SRC-GUIDE-CARBON-001 | Carbon: jerarquía, tamaños por contexto, navegación mediante links e iconos moderados. Su regla icono-derecha no se adopta literalmente. |
| SRC-GUIDE-APPLE-001 | HIG: propósito claro, símbolos comprensibles y espacio de activación. |
| SRC-GUIDE-TAILWIND-001 | Selectores de estilo; no semántica de producto. |

Las URLs, cobertura y digests están en [registro de fuentes](../../registry/sources.md). Este MD es la única definición candidata editable de reglas de uso; el YAML existente solo conserva el baseline técnico.

## 20. Change management

Mientras 0.2.0 esté IN_REVIEW, 0.1.0 y la enmienda Buttons permanecen vigentes. Aprobar esta revisión incorporaría reglas de uso y permitiría actualizar Description en Figma después de P04 y readback. No autoriza cambiar estructura, variantes, tokens, interacciones, defaults ni bindings. Documentation link requiere URL pública verificable; una ruta local no sirve. Web, danger, icon-only, RTL y área táctil necesitan especificación posterior.

## 21. Changelog

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 0.1.0 | 2026-09-23 | Baseline técnico y visual; página Buttons por enmienda. | APPROVED; Figma VALIDATED para ese alcance |
| 0.2.0 candidata | 2026-09-23 | Guía de elección de type/size/state, contenido, iconos y Description. | IN_REVIEW; no publicada en Figma |
