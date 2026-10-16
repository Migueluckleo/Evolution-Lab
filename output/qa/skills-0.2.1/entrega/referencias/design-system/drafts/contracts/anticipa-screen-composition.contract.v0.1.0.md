---
contract_schema: sdd-project/0.2
contract_id: ANTICIPA-SCREEN-COMPOSITION-001
name: Anticipa · composición y configuración de pantallas con AI Design System
type: screen_composition_and_usage
version: 0.1.0
status: DRAFT
last_updated: 2026-10-06
review_targets: [figma]
figma_page_name: null
readiness_by_target: {figma: BLOCKED, web: BLOCKED}
implementation_status: NOT_STARTED
approval_decision: null
sources: [SRC-FIGMA-ANTICIPA-LAYOUT-OBSERVATION-001, SRC-TOKENS-INV-001, USR-ANTICIPA-COMPOSITION-001]
data_refs: [sources/inventories/tokens.inventory.json]
dependency_lock: drafts/contracts/anticipa-screen-composition.dependencies.v0.1.0.json
slot_applicability: REQUIRED
---

# Anticipa · contrato de composición, uso y propuestas de componentes

**Punto de entrada para un agente:** leer §§2, 10, 12 y 19 antes de configurar cualquier pantalla. Este documento integra layouts observados con AI Design System; **no sustituye contratos de componentes ni aprueba las propuestas nuevas**. No se construyó ni modificó Figma en esta tarea.

## 1. Purpose

Definir una guía contractual de composición para pantallas desktop de Anticipa: shell, dashboards, tablas, lista/detalle, conversación, espacio de trabajo, drawers y modales. El layout se apoya en la observación de Anticipa; apariencia, estados disponibles y tokens de los componentes se consumen de sus contratos vigentes de AI Design System.

La solicitud autoriza redactar especificaciones y proponer componentes. No autoriza por sí sola reconstruir este nuevo conjunto de pantallas, implementar frontend, alterar Foundations ni publicar la biblioteca. La delegación histórica para migrar la Librería raíz no se extiende automáticamente a este archivo. TABLE-001 tiene su autorización propia y sigue siendo reutilizable según su contrato.

**Cobertura de evidencia:** snapshot de 61 páginas inventariadas, 43 no separadoras; 34 estados de Papeles de trabajo y 199 frames/instancias adicionales; 19 capturas representativas previamente inspeccionadas. No fue una auditoría exhaustiva de todos los descendientes, variables o interacciones del archivo. Playground, Graveyard, Pendientes y MVP 2 no aprobado no aportan requisitos de construcción. Los límites están en `/coverage/limits` del snapshot de §19.

## 2. Contract

### 2.1 Autoridad y lectura

- `EXPLICIT`: solicitud humana o regla vigente citada. No significa que este nuevo documento completo esté aprobado.
- `OBSERVED`: dato de la inspección anterior, no intención ni regla universal.
- `DERIVED`: composición o cálculo trazable a la evidencia.
- `INFERRED / PROPUESTO`: recomendación de este candidato; requiere adopción antes de construirla como norma.
- `UNRESOLVED`: falta una definición material. `CONFLICT` se reserva para reglas normativas incompatibles, no para dos ejemplos diferentes.

Precedencia: decisión humana aplicable → contrato propietario + enmiendas de alcance explícito → JSON que ese contrato delega → este contrato de composición cuando sea aprobado. Figma observado y Graphify aportan evidencia, nunca sustituyen esa cadena. Si un requisito de composición no cabe en un componente vigente, se propone una extensión; no se cambia silenciosamente el componente.

### 2.2 Requisitos trazables

Los requisitos nuevos son candidatos; los límites ya establecidos por el usuario/DS conservan su autoridad propia.

| ID | Regla | Procedencia | Aceptación |
|---|---|---|---|
| REQ-ASC-01 | MUST resolver contrato base, enmiendas, datos y restricciones antes de usar cada dependencia; no seleccionar solo el archivo con fecha más reciente. | EXPLICIT: solicitud y P03/P05 | AC-01 |
| REQ-ASC-02 | MUST usar instancias de AI Design System para componentes disponibles, sin detach, duplicar principales ni importar su equivalente visual de Anticipa. | EXPLICIT: consumo del DS; DERIVED: integración | AC-02 |
| REQ-ASC-03 | MUST ligar las regiones nuevas a roles semánticos existentes compatibles por intención, tipo y scope; no copiar variables internas de Anticipa ni conectar primitivas directamente. | EXPLICIT: usuario y Foundations | AC-03 |
| REQ-ASC-04 | MUST heredar el tema y validar Contable, Administrativo, Servicios y Personas; no fijar el azul de la captura. Conservar excepciones de marca/arte del contrato propietario. | EXPLICIT: usuario; contratos DS | AC-04 |
| REQ-ASC-05 | MUST separar geometría observada, receta propuesta y capacidad realmente implementada; las muestras no definen breakpoints ni cardinalidad máxima. | EXPLICIT: P03/P-SLOTS | AC-05 |
| REQ-ASC-06 | MUST aplicar la matriz de Slots de §12; un frame llamado Slot o una lista de booleanas no acredita un Slot nativo. | EXPLICIT: P-SLOTS | AC-06 |
| REQ-ASC-07 | MUST identificar si la región es panel integrado, drawer superpuesto o modal; registrar cierre, scroll y conservación de datos por contexto antes de implementar comportamiento. | DERIVED + propuesta de integración | AC-07 |
| REQ-ASC-08 | MUST mantener separados disponibilidad, contenido y selección. Disabled con contenido no recibe apariencia editable; Off/Mixed no significan Disabled. | EXPLICIT: decisiones y contratos propios | AC-08 |
| REQ-ASC-09 | MUST NOT convertir textos fiscales, porcentajes, formatos de descarga, ejemplos de archivos o pantallas ordenadas en reglas de negocio sin definición. | OBSERVED + límites de contratos | AC-09 |
| REQ-ASC-10 | MUST registrar decisiones abiertas y desviaciones por receta, sin recolorear componentes para ocultar limitaciones de contraste. | EXPLICIT: usuario y enmiendas vigentes | AC-10 |
| REQ-ASC-11 | MUST conservar una sola definición editable: reglas aquí; valores/aliases/description en su JSON; anatomía/estados propios en el contrato de cada componente. | EXPLICIT: AGENTS/P05 | AC-11 |
| REQ-ASC-12 | MUST verificar el resultado real antes de declarar una pantalla construida o validada; no confundir QA documental con implementación o aprobación. | EXPLICIT: P06 | AC-12 |

## 3. Anatomy

Árbol conceptual derivado, no nombres de componentes existentes ni API de código:

```text
Pantalla web
├─ Header → HEADER-001
└─ Cuerpo
   ├─ Navegación → SIDEBAR-001
   └─ Área principal → receta seleccionada
      ├─ Encabezado de página / herramientas / filtros
      ├─ Contenido variable
      │  ├─ Métricas / gráficos
      │  ├─ Tabla / paginación
      │  ├─ Lista + detalle documental
      │  └─ Conversación [+ espacio de trabajo integrado]
      └─ Feedback contextual, solo cuando corresponda
Capa superpuesta independiente
├─ Drawer contextual → propuesta PROP-01
└─ Modal centrado → MODAL-001
```

Header y Sidebar no se reconstruyen dentro de cada pantalla. La región integrada ocupa espacio del área principal; una superposición no reduce automáticamente ese espacio. La existencia de ambos patrones no autoriza anidarlos arbitrariamente.

El historial de conversaciones y carpetas pertenece al área de conversación; no se añade al Sidebar global como si fuera navegación del sistema. Document preview no es una imagen decorativa ni una tabla. Las acciones de un documento pertenecen a ese documento, no al footer global.

## 4. Properties

Configuración **conceptual propuesta**, que el agente debe resolver antes de construir cada receta. No son propiedades Figma ya creadas ni props React:

| Campo | Tipo conceptual / valores | Regla y default |
|---|---|---|
| `recipe` | Identificador R01–R08 | Obligatorio, sin selección automática por nombre de frame. |
| `sourceEvidence` | file key + uno o más node IDs + snapshot | Obligatorio; no confundir IDs fuente y destino. |
| `theme` | Herencia del contexto de AI Design System | Default propuesto: heredar; un modo explícito solo en fixtures de QA. |
| `navigationPresentation` | Collapsed / Expanded, de SIDEBAR-001 | Elección explícita; no inferir breakpoint ni persistencia. |
| `title`, `description` | Texto de producto | Sin contenido fiscal ni marca por defecto; admitir descripción ausente. |
| `contentRegions` | Regiones de §12 con contenido tipado por contrato | No crear `item1…itemN` ni variantes por cantidad. |
| `overlayPresentation` | none / drawer / modal | Solo en contextos que lo requieran; no confundir con panel integrado. |
| `dismissPolicy` | Decisión por contexto | Sin default global; ver §8. No inferir cierre fuera/Escape a partir de X. |
| `scrollOwner` | Región identificada por nombre | Debe quedar explícita por receta antes del QA funcional; no usar `auto` como decisión implícita. |
| `dataState` | Estado definido por producto | No genera nuevas variantes de los hijos. Empty, error y permisos no son equivalentes. |
| `actions` | Etiqueta + intención + contrato visual + resultado definido o pendiente | No asignar un destino por el icono; no publicar etiquetas de demo. |
| `responsivePolicy` | Baseline desktop o política aprobada | Mobile/tablet y breakpoints: UNRESOLVED. |

Las propiedades nativas de cada hijo se conservan con su capitalización exacta: Button usa `type/size/state` en minúsculas; Input Field usa `Size/State/Value`; Modal usa `Size/Scroll`; Sidebar usa `Presentation`. El agente no las homogeneiza mediante cambios a los principales.

## 5. Variants

Estas son **recetas de composición**, no ocho variantes de un megacomponente ni estados cartesianos. Las referencias de nodos son del archivo Anticipa de §19.

| Receta | Uso observado / evidencia | Ensamblaje propuesto y dependencias | Límite |
|---|---|---|---|
| R01 · Shell desktop | Inicio `19871:20289`, OBS-01 | Header + Sidebar + región principal. Base compartida de R02–R06. | No incluir automáticamente shell en un drawer, email o Connect. |
| R02 · Dashboard | `20239:192284`, `18840:28207`, `18818:14273` | Encabezado, colección variable de Metric Cards, bloques Charts y herramientas locales. | Metric Card no es un contenedor genérico. No reconstruir gráficas no cubiertas por CHARTS-001 como si existieran. |
| R03 · Espacio de datos | CFDI `17335:2023`, SAT `17840:22727` | Encabezado, filtros/herramientas, Table y Pagination; métricas opcionales solo con evidencia del contexto. | Filtros, sort, selección, recuentos y paginación no están implementados por sus variantes Figma. |
| R04 · Lista y detalle | Buzón `20082:64748`, documentos `18033:7753` | Lista de registros + región documental persistente; PROP-04 para preview; acciones del registro separado de filtros. | La selección no se infiere de hover; PDF real y privacidad requieren definición de producto. |
| R05 · Conversación | `19871:20289`, `19871:21358` y secuencia principal | Historial/carpetas, transcript y composer; propuestas PROP-02/03, con Input/Buttons existentes cuando encajen. | Orden espacial de pantallas no es un flujo conectado. |
| R06 · Conversación + trabajo | `20453:45364`, `20521:58242`, `19784:25807` | Conversación y región lateral integrada; formularios/tablas como contenido del workspace. | No sustituye automáticamente al formulario embebido `19873:52481`; decisión D01. |
| R07 · Drawer contextual | Base `17010:7683`; detalle `18340:6242`; notificaciones `18589:12795` | PROP-01 con toolbar, header opcional, body y actions; contenido compuesto con dependencias DS. | Cierre, anchura expandida y scroll por contexto; no es Modal/SideBySide. |
| R08 · Modal centrado | Carpetas `20453:11904`; columnas `18121:9022` | MODAL-001 Basic, Body y Actions nativos; Input/Select/Table según necesidad. | El ancho observado 700 no es un tamaño Modal del DS; ver §6/D06. |

**Superficies excluidas de estas recetas:** Connect (`19987:9077` y relacionados) es una ventana separada, no otra pantalla con Header/Sidebar web; los emails `20304:10516` tienen composición propia. Sus observaciones no autorizan contratos desktop/email ni mezclar sus medidas con las recetas web.

## 6. Sizes

| Región | OBSERVED o contrato propietario | Propuesta de integración / límite |
|---|---|---|
| Pantalla de referencia | Anticipa usa frecuentemente 1440×1024. | Fixture desktop de comparación, no tamaño obligatorio de todas las pantallas. |
| Shell inicial | Header 1440×96; body 1440×909; navegación234×885; principal1126×885. | No forzar que sumen 1024: la fuente mezcla cajas y sizing. Propuesta: body ocupa el espacio restante del fixture; adaptación derivada, no clon píxel exacto. |
| Header / Sidebar | HEADER-001: alto96; SIDEBAR-001: ancho72/234 y muestra de alto885. | Consumir esas definiciones; ajuste de altura al viewport se propone a nivel de composición y se prueba, no se modifica el principal. |
| Márgenes de área nueva | Fuente repite24; Drawer base padding24/24/128/24. | Propuesta de margen/gap principal: `spacing/xl`; separación entre secciones `spacing/2xl`; herramientas `spacing/sm`. No convertir128 de compensación en regla universal. |
| Drawer base | 650×1024; Slots de602 de ancho; toolbar32, header92 y content684. | Propuesta650 como ancho de referencia literal; body FILL y header/actions HUG. Alturas de contenido no se fijan por la muestra. |
| Drawer expandido | 1280×1266, padding lateral80; otros estados alcanzan1844 de alto. | Variante candidata, no responsive automático. Requiere decidir ancho frente a viewport y scroll, D05. |
| Modal columnas | Fuente700×600 con padding32. | DS Basic solo Small480/Medium580/Large840. Proponer Large y adaptar el contenido; no inventar Medium700 ni redimensionar su principal. Si el ancho700 es requisito, enmienda específica antes de construir. |
| Tabla | TABLE-001 baseline1280×412; columnas concretas y filas36. | Contenedor de datos no redefine anchos/altos del Table. Ver limitación Hover de §14 antes de prometer alineación. |
| Split view | Dos regiones observadas, distintas pantallas. | Proporciones, mínimos y resizer no definidos. No inventar50/50, arrastre ni un ancho fijo de conversación. |

Dimensiones literales de referencia no son nuevos tokens. Los tokens `spacing/*` se usan en padding/gap, no en width/height por igualdad numérica. Cuando una capacidad no está contemplada por el contrato hijo, la receta la deja como propuesta y prueba de integración pendiente.

## 7. States

1. **Hijos:** usar solo estados y combinaciones enumerados en sus contratos. Table Row ofrece Default/Hover, no Selected/Disabled/Error. Tab tiene17 combinaciones, no todo su producto cartesiano. Textarea tiene Default/Error/Disabled/Focus, no Success.
2. **Input Field:** `Value=Filled` no significa editable. Su enmienda0.1.1 obliga a `color/text/disabled` tanto en Empty como en Filled cuando `State=Disabled`; no aplicar texto primary a datos precargados deshabilitados. Search conserva la misma regla en0.1.1.
3. **Producto:** loading/empty/failure/permission denied son condiciones por definir; no crear un eje State global que se propague a todo el árbol. Empty states solo representa ausencia de datos según su propio alcance.
4. **Feedback:** usar Type de Inline Notification si corresponde; Show dismiss es visibilidad, no persistencia ni evento de cierre.
5. **Temas:** son modos de variables, no variantes de página ni copias coloreadas. Un cambio de tema no cambia el significado de Enabled/Disabled ni de una severidad.

## 8. Behavior

### 8.1 Lo que la fuente sí demuestra

| Contexto | Evidencia | Tratamiento contractual |
|---|---|---|
| Papeles de trabajo | OBS-09: CHANGE_TO, CONDITIONAL y SET_VARIABLE; no NAVIGATE/OVERLAY entre pantallas del proceso, disparadores vacíos y dos destinos NODE nulos. | Secuencia ilustrada, no flujo ejecutable. No copiar IDs de destino ni presentar una PoC navegable como comportamiento ya validado. |
| Detalle CFDI / notificaciones | `18340:6242` y `18589:12795`: cierre exterior configurado. | Registrar ese comportamiento observado por contexto; no convertirlo en política global del DS. |
| Nuevo grupo | `17010:7690`: outside NONE. | No aplicar el cierre exterior del drawer de consulta al formulario de edición. Guardado/descarte no definido. |
| Configurar columnas | OBS-11: OVERLAY → SWAP por press/drag/timeout → NAVIGATE. | Evidencia de una cadena concreta, no contrato de arrastre libre, orden persistido ni cobertura de todo el sistema. |
| Notificaciones SAT | `18690:4113`: controles de frecuencia y toggles; sin Save visible. | No deducir autosave. Persistencia, confirmación y error UNRESOLVED. |

### 8.2 Propuesta de política por contexto, pendiente de adopción

- **Panel integrado:** conservar el contexto principal visible; acciones y navegación de detalle no bloquean toda la pantalla por defecto. Propuesta, no comportamiento probado.
- **Drawer de lectura:** proponer un cierre explícito y conservar el registro/posición de origen; cierre exterior solo si se adopta para ese contexto. No hay política aprobada para Escape o retorno de foco.
- **Drawer de edición:** proponer footer de acciones separado del contenido desplazable y protección ante pérdida de datos. Qué cuenta como cambio y qué hace Cancelar debe decidirse, no se inventa un diálogo adicional.
- **Modal de decisión:** reutilizar Basic y su jerarquía de acciones. Describir resultado de confirmar/cancelar, destino de foco y scroll de fondo antes de implementación funcional. El contrato Modal no resuelve estos comportamientos.
- **Conversación:** proponer independencia entre historial, transcript y workspace; no inferir streaming, cancelación, reintento, autoscroll o envío con Enter. No añadir estados del asistente por analogía con otro chat.

El bloqueo de una regla funcional no impide documentar o revisar visualmente una receta independiente; sí impide declararla funcional o completar la parte afectada por suposiciones.

## 9. Accessibility

No se declara cumplimiento WCAG ni evaluación de teclado/lector de pantalla. Los controles DS conservan sus limitaciones conocidas; su QA visual no certifica una pantalla compuesta.

**Propuestas para el contrato funcional posterior:** regiones y títulos con jerarquía coherente; nombre de cada acción iconográfica; foco inicial/retorno y contención si el overlay es modal; orden de lectura entre conversación y workspace; lectura de estado/errores sin depender solo de color; alternativa textual de gráficos y documentos. Son criterios candidatos, no capacidades actuales ni recomendaciones externas adoptadas automáticamente.

En QA visual de la futura composición: comprobar contenido largo, recortes, contraste por modo y visibilidad de acciones. Registrar limitaciones con `*` en documentación interna, no insertar asteriscos indiscriminados en la interfaz ni recolorear variables compartidas. No reducir tipografía de un hijo para ocultar overflow.

## 10. Design tokens

### 10.1 Fuente única y resolución

El [inventario canónico](../../sources/inventories/tokens.inventory.json) gobierna nombres, tipos, modos, valores, aliases y única `description`. SHA-256: `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.

El [lock derivado](anticipa-screen-composition.dependencies.v0.1.0.json) contiene37 referencias exactas de tokens con JSON Pointer, ID **del inventario** y scope, además de hashes de30 dependencias revisadas. No contiene otro catálogo de valores ni descripciones. Los IDs `VariableID:*` del inventario no son IDs locales reutilizables en AI Design System. Antes de escribir: resolver colección semántica local, nombres, tipos, scopes, modos por nombre y aliases; registrar el mapa local real. Igualdad RGB no prueba identidad semántica.

No se adopta ninguna de las cuatro colecciones internas observadas en Anticipa. Esta tarea no crea tokens ni primitivas. Los hijos mantienen las extensiones que sus contratos vigentes referencian; no se mezcla una extensión histórica con su sustitución en el mismo campo.

### 10.2 Recetas de pintura para regiones nuevas — PROPUESTA

Estas elecciones aplican a envolturas nuevas, **no a los paints internos de componentes reutilizados**. Deben aprobarse con la receta; los tokens citados ya existen.

| Región/parte | Token propuesto | Propiedad / scope | Restricción |
|---|---|---|---|
| Superficie principal, drawer, panel documental y bloque de lectura | `color/background/default` | Fill de frame / FRAME_FILL | No significa estado interactivo ni selección. |
| Separación neutral de una zona de trabajo o agrupación secundaria | `color/background/subtle` | Fill de frame / FRAME_FILL | No aplicar como Disabled por semejanza: cada control conserva su receta. |
| Región suave de marca en composición nueva, por ejemplo agrupación destacada del mensaje de usuario | `color/surface/brand` | Fill de frame / FRAME_FILL | Propuesta de tratamiento, no un estado enviado/seleccionado. Cambia de familia de marca por modo. |
| Borde de panel neutral | `color/border/default` + `stroke/xs` | Stroke / STROKE_COLOR + STROKE_FLOAT | No copiar color text en bordes. Separador de mayor énfasis solo si se justifica: `color/border/strong`. |
| Título y contenido principal | `color/text/primary` | Text fill / TEXT_FILL | Textos de hijos conservan el rol de su contrato, no se sobreescriben globalmente. |
| Explicación y metadatos secundarios | `color/text/secondary` | Text fill / TEXT_FILL | Información legible, no apariencia de placeholder por defecto. |
| Placeholder de una región de texto nueva | `color/text/tertiary` | Text fill / TEXT_FILL | Nunca fill de un panel, icono o pista. En un Input usar su contrato. |
| Texto de control deshabilitado | `color/text/disabled` | Text fill / TEXT_FILL | Solo en un estado realmente Disabled y conforme al contrato hijo. |
| Texto de marca y enlace con destino explícito | `color/text/brand` | Text fill / TEXT_FILL | Una cadena azul sin URL/acción no se convierte en enlace. |
| Icono de herramienta neutral / secundario / marca | `color/icon/primary`, `color/icon/secondary`, `color/icon/brand` | Vector fill / SHAPE_FILL | Usar instancias Phosphor según contrato. Un stroke necesita rol compatible específico; no forzar SHAPE_FILL sobre STROKE_COLOR. |
| Backdrop, si se adopta overlay modal | `color/background/overlay` | Frame fill / FRAME_FILL | **No tiene transparencia implícita**. Opacidad, bloqueo y comportamiento quedan D05; no copiar un rgba ni inventar opacity0.5. |

`color/background/brand` y `color/surface/brand` **no son intercambiables**: sus aliases difieren por modo. TABLE-001 consume el primero en su header y debe conservarlo; las nuevas regiones de baja intensidad aquí propuestas consumen el segundo. No corregir Table a partir de esta tabla.

Los botones reciben su apariencia de BUTTON-001 + enmiendas, no del token genérico de superficie. Inline Notification usa sus roles de feedback, no una envoltura pintada de marca. Charts usa roles shape/chart, no icon ni interactive. Header y Sidebar conservan sus degradados de release acotados por contrato; logos mantienen su excepción agnóstica. No convertir todos los azules decorativos en un token brand mediante búsqueda/reemplazo.

### 10.3 Tipografía y geometría de envolturas nuevas — PROPUESTA

Para texto nuevo: `font/family/base` y `font/letter-spacing/normal`, además de peso/tamaño/interlineado de la fila aplicable. No usar estilos internos de Anticipa como fuente canónica ni inventar nombres CSS.

| Rol nuevo | Peso | Tamaño | Interlineado |
|---|---|---|---|
| Título de página | `font/weight/bold` | `font/size/xl` | `font/line-height/xl` |
| Título de sección / panel | `font/weight/semibold` | `font/size/md` | `font/line-height/md` |
| Mensaje de conversación / lectura | `font/weight/regular` | `font/size/md` | `font/line-height/md` |
| Etiqueta contextual compacta | `font/weight/regular` | `font/size/sm` | `font/line-height/sm` |
| Metadato breve | `font/weight/regular` | `font/size/xs` | `font/line-height/xs` |

Layout propuesto: `spacing/xl` en márgenes principales y drawer; `spacing/lg` en panel interno; `spacing/sm` entre herramientas; `spacing/xs` entre título y metadato; `spacing/2xl` entre secciones; `spacing/none` donde no corresponda separación. Panel nuevo: `radius/lg`; agrupación de mensaje: `radius/md`. Son selecciones de roles existentes, no redefinición de sus valores. No imponer estas filas sobre Modal, Table, Metric Cards o demás hijos con tipografía/espacios propios.

**Sombras y efectos:** no hay una receta universal nueva. Las excepciones de sombras de Select y Modal quedan dentro de esos componentes; no se copian al Drawer ni se simula elevación usando un token de foco. Elevación del Drawer queda abierta en D05. El JSON no se amplía para cubrirla en esta tarea.

## 11. Content rules

- Sustituir ejemplos de compañía, RFC, importes, archivos y marcas por datos de demo no sensibles o copy de producto aprobado. No usar credenciales reales ni completar contenido oculto por intuición.
- Elegir terminología de producto antes de publicar: Anticipa, Contabilidad, NAVI y BENI coexisten en la fuente; no son nombres equivalentes demostrados.
- Reutilizar reglas de Button: etiqueta con acción clara, no `Default`; normalmente un solo primary por grupo; mismo tamaño en el grupo; `link` no muta datos. Ocultar iconos redundantes mediante propiedades existentes.
- El80% de Charts y los importes de Metric Cards son demos, no fórmulas. El contador de Textarea no define límite300. File Upload no convierte XLS/XLSX/CSV ni50MB en política de carga para CSF o FIEL.
- No introducir URL ficticia para los segmentos que parecen enlaces en la fuente. No prometer PDF/ZIP porque figure en el nombre del frame; D03.
- Las longitudes máximas, redondeo, validación fiscal, obligatoriedad, formatos aceptados y tratamiento de datos personales requieren definición de producto. Este contrato no ofrece validación contable/legal.

## 12. Composition rules

### 12.1 Reutilizar antes de proponer otra familia

| Necesidad | Dependencia propietaria y alcance efectivo |
|---|---|
| Shell | [Header0.1.0](../../specs/header.contract.v0.1.0.md) + [roles Header](../../specs/foundations.header-roles.amendment.v0.1.0.md); [Sidebar0.1.0](../../specs/sidebar.contract.v0.1.0.md) + [roles Sidebar](../../specs/foundations.sidebar-roles.amendment.v0.1.0.md). |
| Acción con etiqueta | [Button0.2.0](../../specs/components/button.contract.v0.2.0.md), baseline0.1.0 incorporado por referencia; [página](../../specs/components/button-page-name.amendment.md), [texto Disabled0.2.1](../../specs/components/button.semantic-scope-amendment.v0.2.1.md), [bindings locales0.2.2](../../specs/components/button.local-bindings.amendment.v0.2.2.md) y [color seis familias](../../specs/components/six-family-color.amendment.v0.1.0.md). No omitir la última al leer colores históricos. |
| Acción iconográfica | [Icon Button0.1.0](../../specs/icon-button.contract.v0.1.0.md) + enmienda seis familias. No reemplazarlo por Button sin label. Ocultar Count si no aporta información. |
| Campo | [Input Field0.1.0](../../specs/input-field.contract.v0.1.0.md) + [Disabled0.1.1](../../specs/input-field.disabled-text.amendment.v0.1.1.md). |
| Búsqueda / texto multilínea / carga | [Search0.1.1](../../specs/search.contract.v0.1.1.md), [Textarea0.1.0](../../specs/textarea.contract.v0.1.0.md), [File Upload0.1.0](../../specs/file-upload.contract.v0.1.0.md). No inferir búsqueda, resize o upload reales. |
| Selector variable | [Select0.1.0](../../specs/select.contract.v0.1.0.md) + [Slots0.1.0](../../specs/composition-slots.amendment.v0.1.0.md). Dropdown Item e Input Field se resuelven transitivamente; no reconstruirlos desde apariencia. |
| Tabla y páginas | [Table0.1.0](../../specs/table.contract.v0.1.0.md); [Pagination0.1.0](../../specs/navigation-pagination.contract.v0.1.0.md) + [Slots0.1.1](../../specs/composition-slots.amendment.v0.1.1.md), incluyendo su extensión contextual de estado. |
| Pestañas de espacio de trabajo | [Tab0.1.0](../../specs/navigation-tab.contract.v0.1.0.md). Para una región de varias pestañas, Slot en el anfitrión; un Tab individual no se convierte en lista. |
| Métricas y gráficos | [Metric Card0.1.0](../../specs/metric-card.contract.v0.1.0.md), [Charts0.1.0](../../specs/charts.contract.v0.1.0.md), ambos con enmienda seis familias; Charts además Slots0.1.1. Los roles sustituidos proceden del [JSON cromático vigente](../../specs/tokens/ai-design-system.six-family-color.v0.1.0.json), no de una extensión histórica seleccionada por nombre. |
| Mensaje contextual | [Inline Notification0.1.0](../../specs/components/inline-notification.contract.v0.1.0.md) + [Warning0.1.1](../../specs/components/inline-notification.warning-source-color-amendment.v0.1.1.md) y Foundations citadas por ella. El requisito histórico de oscurecer Warning está sustituido. |
| Ausencia de datos | [Empty states0.1.0](../../specs/empty-states.contract.v0.1.0.md), con Slots y límites de ancho propios. No aplicarlo automáticamente a permiso denegado o error. |
| Diálogo | [Modal0.1.0](../../specs/modal.contract.v0.1.0.md), conservando Body/Actions y dependencias de Button. No usar SideBySide como sustituto de Drawer. |

El lock fija las dependencias directas revisadas, **no certifica todo su cierre transitivo ni el Figma actual**. Antes de implementación se deben abrir sus referencias de datos, resolver sustituciones por campo y cotejar los estados/IDs reales del destino. Phosphor, Avatar, Dot, Checkbox, Radio, Toggle, Loader y otras piezas anidadas se consumen a través de sus contratos propietarios; este candidato no amplía sus capacidades ni vuelve a definir sus tokens.

### 12.2 Matriz P-SLOTS

`REQUIRED` aquí expresa aplicabilidad. Solo los contratos DS citados aportan evidencia previa de implementación; las propuestas nuevas todavía no tienen Slots creados.

| Anfitrión / región | Aplicabilidad y mecanismo | Hijos admisibles / cardinalidad | Layout candidato o regla heredada |
|---|---|---|---|
| Shell: contenido principal | REQUIRED si se convierte en componente reutilizable; Slot nativo | Una composición activa; su interior puede variar. No mezclar varias pantallas completas. | FILL ancho; altura según scrollOwner; regiones estructurales Header/Sidebar separadas. |
| Encabezado de página: herramientas/filtros | REQUIRED si se empaqueta; Slot nativo por región | Instancias Buttons, Icon Buttons, Search, Select; cantidad variable sin máximo de negocio definido. | Herramientas horizontal HUG, gap `spacing/sm`; wrap propuesto solo si no altera hijos ni orden de acciones. |
| Dashboard: bloques | REQUIRED si se empaqueta; Slot nativo | Metric Card/Charts/composiciones aprobadas; muestras no limitan cantidad. | Colección con reflow propuesto; columnas y mínimo de cada tarjeta pendientes de validación, no grilla fija inferida. |
| Table: rows/header cells/row cells/actions | REQUIRED, ya especificado en TABLE-001 | Según contrato Table. Añadir/quitar columnas exige sincronizar encabezado y filas; no automático. | Conservar mecanismos y restricciones de Table, no un Table nuevo con slots simulados. |
| Select: Options | REQUIRED, enmienda0.1.0 | Dropdown Item; cinco es muestra, no máximo. | Slot vertical HUG. No añadir max-height/scroll por inferencia; el anclaje80 corresponde al preset documentado. |
| Drawer: Toolbar/Header/Body/Actions | REQUIRED, PROP-01; fuente tiene tres Slots, Actions fuente es frame | Toolbar/actions: controles DS; Header: contenido contextual; Body: composición identificada. Actions variable, sin máximo de negocio. | Toolbar/header/actions HUG; body FILL si viewport limitado; scroll propuesto solo body. No declarar footer sticky por su nombre fuente. |
| Workspace integrado: Tools/Tabs/Content | REQUIRED, PROP-02 | Herramientas DS, Tab, una composición activa de tabla/formulario/preview. | Columnas independientes; cada región identifica scrollOwner. Sin arrastre de divisor asumido. |
| Conversación: Messages/Attachments/Actions | REQUIRED, PROP-03 | Mensajes tipados por propuesta; artefactos con contrato; controles DS. | Transcript vertical; composer separado. Cantidad variable no crea variantes por índice. |
| Preview documental: Toolbar/Content/Actions | REQUIRED, PROP-04 | Acciones DS + documento o estado definido; no scripts embebidos. | Cuerpo documental limitado al área disponible, sin escalar toda la UI. |
| Modal/Empty states/Sidebar/Header | REQUIRED donde sus contratos ya declaran Slots | Sus regiones exactas; no renombrar propiedades nativas. | Heredar reglas propias; no reemplazarlas por la geometría nueva de esta tabla. |
| Título/etiqueta simple/icono único | NOT_APPLICABLE | TEXT/BOOLEAN/INSTANCE_SWAP cuando el propietario los ofrece. | No implementar Slot para una cadena o un pictograma de anatomía fija. |

Para Slots nuevos, propuesta de fixture:0,1 y3 hijos donde vacío sea válido; además un caso mayor que la muestra fuente. Esas cantidades son pruebas, no mínimos/máximos de producto. Probar insertar, eliminar, reordenar y sustituir desde instancia; retención al cambiar presentación; herencia de tema; overflow y variantes de los hijos. No propagar Disabled o selección a todo el Slot salvo regla explícita del propietario. Un Slot vacío no equivale a pantalla Empty: esa decisión corresponde al consumidor.

### 12.3 Propuestas de construcción, no nuevas tareas aprobadas

| ID / familia candidata | Qué construir solo tras adopción | Reutilización y superficie pública propuesta | Lo que debe resolverse antes |
|---|---|---|---|
| PROP-01 · Drawer | Anfitrión lateral contextual; página propuesta **Drawers** si no existe otra equivalente. | Toolbar, Header, Body y Actions nativos; título/descripcion editables; presentación de referencia650 y expansión candidata1280. Buttons/Icon Buttons dentro de Slots. Superficies/tipografía de §10. | D05: scroll, cierre, footer, backdrop/elevación y adaptación; preflight para no duplicar una familia existente. No asumir estado Disabled del Drawer. |
| PROP-02 · Workspace Panel | Región integrada de trabajo, no overlay; página propuesta **Workspace Panels** solo si el patrón necesita main reutilizable. | Tools/Tabs/Content; reutiliza Tab, Table, Input y Preview. Mostrar/ocultar encabezado por propiedad, sin duplicar cada pantalla como variante. | D01/D05: alternativa de formulario, proporciones, mínimo y desplazamiento. Puede bastar una receta de composición sin crear una familia pública. |
| PROP-03 · Conversation | Composición de transcript/composer e ítems de mensaje; página propuesta **Conversation**. | Messages/Attachments/Actions variables; texto editable y controles locales. Propuesta de distinguir mensaje de usuario, respuesta y artefacto por anatomía; no fabricar matriz de estados. | D01–D04 y D07: resultados del proceso, validación, formatos, nombres; decidir envío y tratamiento de adjuntos. Textarea actual no demuestra composer listo: no heredar cláusulas File Upload ni contador300. |
| PROP-04 · Document Preview | Contenedor de preview con herramientas; página propuesta **Document Preview**. | Body de documento y herramientas/acciones; reutiliza controles DS y presentación de ausencia de datos solo si corresponde. | Formatos, visor real, permisos y estados operativos por producto. El recurso documental conserva su aspecto; UI del visor sí consume DS. |

Estas propuestas no justifican crear nuevos Button, Input, Tab, Card o Modal. Primero comprobar el registro y el archivo destino: ausencia en la evidencia consultada no prueba ausencia absoluta en Figma. `figma_page_name` permanece null para este contrato paraguas porque no representa una sola familia construible; los nombres anteriores son propuestas por familia, sin page IDs inventados. Las pantallas de producto no se depositan indiscriminadamente entre principales de biblioteca.

## 13. Responsive behavior

Únicamente baseline desktop observado. **Propuestas**: contenedores de lectura FILL en ancho disponible, texto nuevo con crecimiento vertical, regiones auxiliares HUG y body desplazable cuando se adopte un viewport fijo. Verificar el comportamiento de cada hijo antes de fijar mínimos del conjunto.

No inferir móvil, tablet, cambio automático de Sidebar, colapso de columnas, Drawer a pantalla completa, anchura máxima de chat ni arrastre del split. D05 bloquea esas promesas, no la documentación del baseline. El mínimo548 de Empty states Main y las restricciones de Table/Modal son límites de hijos que el compositor no puede ignorar. No escalar la pantalla completa para aparentar responsive.

## 14. Edge cases

### 14.1 Decisiones pendientes realmente respaldadas por la fuente

| ID | Evidencia / decisión pendiente | Impacto acotado |
|---|---|---|
| D01 | Formulario mensual embebido `19873:52481` frente a laterales multimes `20453:45364`/`20521:58242`. Elegir coexistencia o sustitución. | R05/R06 y PROP-03. No elegir el más reciente por posición/nombre. |
| D02 | Asteriscos de obligatoriedad frente a omisiones tratadas como cero; caso sin CFDI con mensajes/resultados distintos (OBS-07/08). | Validación y resultados de Papeles de trabajo; no bloquea diseño de un drawer de lectura independiente. |
| D03 | ZIP/ExcelPDF en nombres frente a archivo .xls y pregunta posterior sobre PDF (OBS-06). | Salidas y acciones de descarga, no estilo de los botones. |
| D04 | Crear grupo: diagrama `17158:6625` menciona chat; pantalla `17010:7690` muestra drawer. | Composición/resultado de Nuevo grupo. |
| D05 | Scroll ausente en34 estados y drawers largos; cierre exterior distinto por contexto; footer/backdrop/elevación y responsive sin regla común. | Requiere elegir política para la receta que se implemente, no una aprobación global de todos los overlays. |
| D06 | Modal columnas700 frente a480/580/840 de MODAL-001. | Adoptar adaptación a Large propuesta o especificar extensión. No cambiar maestro por comodidad. |
| D07 | Anticipa/Contabilidad/NAVI/BENI y acciones de chat no consolidadas; sin Save en config SAT. | Copy final y comportamiento de producto; no se interpreta ausencia de botón como autosave. |

No se registran como `CONFLICT` entre contratos aprobados: son ambigüedades de una fuente observacional o decisiones de integración nuevas. Se elevan únicamente cuando el alcance de construcción las necesite; no generan automáticamente un backlog nuevo del DS.

### 14.2 Restricciones heredadas que el agente debe conservar

- TABLE-AUD-001: Hover añade8px/desplaza columnas en el componente existente. No declarar alineación perfecta ni corregirlo desde una envoltura sin enmienda al propietario. El número variable de celdas tampoco sincroniza columnas automáticamente.
- Select Open cubre el helper y su anclaje está definido para Large con etiqueta. Cambiar tamaño/etiqueta requiere validar la composición; el Slot no soluciona eso por sí solo.
- Modal, Select y otros componentes contienen excepciones geométricas/de efectos acotadas. No extrapolarlas a toda la pantalla ni afirmar tokenización absoluta.
- Textarea0.1.0 y File Upload0.1.0 contienen redacción cruzada de otras subfamilias. Este contrato **no la corrige ni la usa para añadir capacidades**: sus ejes/anatomía propios gobiernan las referencias aquí empleadas; Success solo está definido en File Upload, no en Textarea. Si el caso necesita una cláusula ambigua, detener ese uso y resolverla en el contrato propietario.
- Contraste de Warning y tonos de marca de Servicios tiene limitaciones documentadas; leer las enmiendas vigentes, no restaurar reglas históricas de oscurecimiento.
- Un control Disabled dentro de una pantalla normal conserva su estado; no volverlo activo al reemplazar texto o tema.

## 15. Forbidden combinations

No se permite dentro del alcance documentado:

1. Copiar colores/variables internas de Anticipa o aplicar primitivas directamente a UI porque el RGB coincida.
2. Usar un token text en fondo, shape o stroke; icon en texto; feedback como decoración de marca; foco como sombra de elevación.
3. Recolorear componentes hijos con las recetas de envolturas de §10; sobrescribir aliases compartidos para resolver una sola pantalla.
4. Crear una variante por cantidad de opciones, filas, mensajes, tabs o acciones; simular Slots mediante capas numeradas o detach.
5. Llamar Drawer a Modal SideBySide, o llamar overlay a un panel integrado, sin definir la diferencia de composición.
6. Afirmar interacción, permisos, validación fiscal, cálculo, streaming, persistencia o accesibilidad por una apariencia estática.
7. Interpretar Empty como error, Off como Disabled, o Filled como habilitado; inventar variantes ausentes para acomodar una receta.
8. Copiar reacciones con IDs de otro archivo, publicar controles con textos técnicos de demo, o hacer pasar un enlace falso por acción real.
9. Sustituir una norma por el grafo, por el lock derivado o por este DRAFT. Una propuesta nueva no modifica una aprobación existente.

## 16. Design ↔ Code mapping

| Concepto | Figma futuro | Implementación de código |
|---|---|---|
| Dependencia de componente | Instancia de principal local verificado; properties exactas del propietario | Import/paquete/API aún no definidos por este documento. |
| Región de contenido variable | Slot nativo cuando la composición sea componente reutilizable | Composición tipada propuesta; no se dicta API children/render prop ni framework nuevo. |
| Tema | Modo semántico heredado y readback de bindings | Resolver adaptador desde datos canónicos; `codeSyntax` vacío no autoriza inventar CSS como si fuera parte del JSON. |
| Layout | Auto layout y geometría aprobada por receta; separado de comportamiento de overlay | CSS/layout es destino posterior; no deducir sticky/fixed/breakpoints solo del nombre de una capa. |
| Evento/estado de producto | Prototipo solo con destinos definidos | Contrato funcional pendiente para eventos, validación, accesibilidad y persistencia. |

La pila prevista del proyecto es React + TypeScript + Vite; esta documentación no implementa esa pila ni añade imports, endpoints o código de producto. Una skill puede usar el contrato como entrada de planificación, no como aprobación automática de todos sus campos.

## 17. Acceptance criteria

| ID | REQ | Comprobación requerida | Estado de esta entrega |
|---|---|---|---|
| AC-01 | 01 | Dependencias versionadas, enmiendas de alcance y hashes contrastados; cierre transitivo antes de build. | QA documental acotado; cierre transitivo de ejecución pendiente. |
| AC-02 | 02 | Mapas de principales/instancias fuente→destino; sin detach o duplicación. | NOT_RUN: no Figma escrito. |
| AC-03 | 03 |37 referencias del lock existen en colección semántica; tipo/scope y alias válidos; posterior readback de cada consumidor. | JSON comprobado; bindings destino NOT_RUN. |
| AC-04 | 04 | Fixtures de los cuatro modos, sin fijación Contable y sin cambios indebidos a excepciones. | NOT_RUN en Figma. |
| AC-05 | 05 | Baselines y normalizaciones etiquetados; restricciones heredadas preservadas; render sin recortes en anchos aprobados. | Distinción documental revisada; render futuro NOT_RUN. |
| AC-06 | 06 | Matriz P-SLOTS y pruebas SLOT-QA-01–09 por nuevo anfitrión con0/1/3 y más que la muestra, según aplicabilidad. | Matriz documentada; implementación NOT_RUN. |
| AC-07 | 07 | Cada overlay/panel tiene región de scroll, cierre, acciones y pérdida de datos definidos y probados. | UNRESOLVED por contexto; no capacidad declarada. |
| AC-08 | 08 | Readback de Disabled Empty/Filled, cambios de tema/contenido sin activación visual; no estados inventados en hijos. | Regla y enmienda vinculadas; integración NOT_RUN. |
| AC-09 | 09 | Ejemplos identificados; D01–D04/D07 no resueltos por inferencia ni reglas fiscales inventadas. | Revisado documentalmente. |
| AC-10 | 10 | Desviaciones y contraste medidos de la composición, asterisco documental, sin recolor automático. | Limitaciones heredadas citadas; nueva medición NOT_RUN. |
| AC-11 | 11 | Links existentes, lock coherente, JSON/source/specs sin cambios, sin catálogo paralelo ni descripción duplicada. | Verificación local en QA adjunto. |
| AC-12 | 12 | Estados separados, registros persistentes y evidencia posterior real antes de validar. | DRAFT / NOT_STARTED, sin aprobación o QA Figma simulados. |

La revisión documental de este candidato no equivale a `READY`. Un futuro lote puede aprobar una receta y las propuestas pertinentes con exclusiones explícitas, sin obligar a resolver todas las decisiones de otras pantallas.

## 18. Examples

### A. Datos CFDI — configuración conceptual de R03

Shell R01 con Sidebar Expanded elegido explícitamente; Header local; título de producto; herramientas Search y Button; Table y Pagination locales. Button de acción principal: `type=primary`, `size=small`, `state=default` para una barra densa; etiqueta concreta definida por producto, no un `link` que cambie datos. Las opciones y filas se editan desde Slots existentes. La cantidad de filas y de páginas no se calcula a partir de la demo.

Superficie de envoltura nueva: background/default; título text/primary; herramientas conservan sus colores; header de Table conserva background/brand, no se repinta con surface/brand. Antes de certificar layout se verifica TABLE-AUD-001. Esta configuración es propuesta de montaje visual, no selección/sort funcionales.

### B. Campo precargado no editable

Input Field con `Size=Large`, `State=Disabled`, `Value=Filled`, texto de ejemplo no sensible. Conservar `color/text/disabled` por enmienda0.1.1; no pasar a primary por tener información. El aspecto no prueba que los eventos estén bloqueados en un navegador. No inventar estado Readonly como sinónimo.

### C. Configuración de columnas — R08

Propuesta: Modal Basic `Size=Large`, `Scroll=No` solo si el contenido cabe; Body con herramientas y región de selección; Actions con Buttons de igual tamaño y jerarquías distintas. Si no cabe, evaluar `Scroll=Yes` dentro del contrato Modal y probar el contenido; no escalar todo a700px ni dibujar otro footer. La regla de orden, visibilidad y guardado de columnas sigue pendiente de producto, aunque el prototipo origen muestre drag.

### D. Drawer de consulta frente a edición — R07

Consulta: toolbar de documento + contenido; cierre exterior observado para CFDI. Edición de Nuevo grupo: acciones de confirmar/cancelar propuestas y outside NONE observado. No heredar el cierre de consulta a edición. Body largo requiere política de scroll explícita; el nombre fixedActions no sirve como prueba.

### E. Conversación con workspace — R06

Mostrar R06 como alternativa explícita a R05, no reemplazo. Panel lateral con Tab y formulario/tabla local; mensajes usando roles de lectura y tratamiento suave de marca propuesto en §10. No activar todos los meses ni generar resultados fiscales sin D01/D02. Historial/carpetas y acciones variables son Slots candidatos, no una colección fija de ejemplos.

## 19. Source of truth

| Referencia | Autoridad / uso |
|---|---|
| Solicitud USR-ANTICIPA-COMPOSITION-001, registrada en [decisiones](../../registry/decisions.md) | EXPLICIT: documentar contrato MD y propuestas compatibles con JSON/DS. No aprueba la construcción. |
| [FOUNDATIONS-TOKENS-001](../../specs/foundations/foundations-tokens.contract.md) + [JSON canónico](../../sources/inventories/tokens.inventory.json) | Contrato y datos existentes; gobiernan sus campos delegados. |
| Contratos y enmiendas de §12.1 | Normas propietarias; conservan sus propios estados APPROVED/DELEGATED_FOR_BUILD y auditoría pendiente donde corresponda. |
| [Snapshot Anticipa](../../sources/figma-snapshots/anticipa-layouts.observation.2026-10-06.json) | OBSERVED_NON_NORMATIVE, SHA-256 `de9255da9d2ec536d632fe624dd93ea572832c9125400800554a47097a494f5b`; `/findings` OBS-01–14 y estructuras/textos por IDs de nodo. No nueva inspección Figma en esta tarea. |
| [Archivo fuente, página de entrada](https://www.figma.com/design/zuUq3gcF9T3CLid44bjY6W/Anticipa-Junio2026?node-id=19871-20287) | `zuUq3gcF9T3CLid44bjY6W`; origen de layouts, no destino de reconstrucción ni inventario de tokens del DS. |
| AI Design System | Destino de componentes eventual `tj3WIBEZDGLVs7MJWKCwgf`; IDs locales nuevos NOT_CREATED. |
| [Trazabilidad transversal](../../specs/MIGRATION-TOKEN-TRACEABILITY.contract.md) + [enmienda0.1.2](../../specs/MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.2.md) | Referencia del DS para cadena de evidencia y primitiva semejante→rol semántico. Su autorización de migración no se amplía a nuevas pantallas por citarlas. |
| [Lock derivado](anticipa-screen-composition.dependencies.v0.1.0.json) | Referencias y hashes, nunca autoridad sobre valores o aprobación. No duplicar descriptions/aliases en él. |

En esta adaptación a SDD del proyecto se entrega **MD normativo candidato**, como solicitó el usuario. Las guías de inspección y comportamiento se aplican para procedencia, dependencias y ambigüedades; no se emite otro YAML normativo paralelo ni se presenta la observación anterior como extracción profunda completa de un único componente.

## 20. Change management

1. Un agente empieza por este MD, valida hashes del lock y abre las dependencias pertinentes con sus enmiendas. Un cambio de hash indica revisión necesaria, no permiso para adoptar el nuevo archivo ni prueba automática de conflicto.
2. Elige una receta, identifica hijos y resuelve solo sus decisiones materiales. Registra configuración/alcance/approval por lote antes de P04. No vuelve a sintetizar contratos ya existentes.
3. En preflight confirma que los componentes y variables reales están disponibles en el destino, sus IDs y capacidades de Slot; no los deduce de este documento. No crea familias propuestas sin comprobar reutilización primero.
4. Si la receta necesita cambiar un hijo o añadir un rol, propone enmienda en el lugar normativo del propietario y datos delegados; no crea una segunda definición en este MD. No se crean primitivas/variables como efecto lateral del montaje.
5. Construye solo el alcance aprobado y ejecuta QA proporcional: geometría, contenidos, Slots, temas, scopes, bindings y comportamiento realmente definido. Registra diferencias y evidencia; no hereda un PASS de otra composición.
6. Este nuevo candidato permanece en drafts hasta aprobación aplicable. La regla de promoción delegada de la migración no lo convierte en specs automáticamente. Una vez promovido, los ajustes normativos se hacen en specs con versión/enmienda y trazabilidad.

Los documentos existentes de specs, el JSON canónico y Figma no cambian en esta entrega. Graphify es índice derivado `STALE_FOR_THIS_NEW_CONTRACT`; no se regeneró ni se usa para afirmar que el DS está actualizado.

## 21. Changelog

| Versión | Fecha | Cambio / estado |
|---|---|---|
| 0.1.0 | 2026-10-06 | Primer candidato: ocho recetas, cuatro propuestas de componentes, mapa de consumo semántico, Slots, dependencias/enmiendas y siete decisiones contextuales. DRAFT, sin construcción ni aprobación simulada. |

## Anexo de revisión

- [Reporte de síntesis y cobertura](../reports/anticipa-screen-composition.synthesis.v0.1.0.md).
- [QA documental y límites](../../qa/contracts/anticipa-screen-composition.v0.1.0.review.md).
- [Verificación reproducible de referencias](../../qa/contracts/anticipa-screen-composition.v0.1.0.verification.json).

Estos anexos son evidencia de revisión; no contienen otra definición editable de los requisitos ni sustituyen las decisiones pendientes del contrato.
