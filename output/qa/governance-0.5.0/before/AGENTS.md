# AGENTS.md

**Paquete de protocolos:** 0.4.0 · **Método:** Specs Driven Design (SDD)

## Propósito y alcance

Este repositorio documenta un sistema de diseño para reconstruirlo en Figma y, posteriormente, en frontend. SDD es el método; los contratos son archivos `.md` y pueden referenciar datos canónicos `.json`.

Este archivo orienta y dirige. Los procedimientos viven en los protocolos. No ejecutes todas las fases por haberlas leído: la solicitud actual determina qué acciones están autorizadas.

## Lectura y selección de protocolo

Lee este archivo, el protocolo de la tarea y sus dependencias indicadas. Consulta los registros existentes antes de asumir el estado del proyecto. No interpretes una ruta mencionada como prueba de que el archivo existe.

| ID | Protocolo | Cuándo utilizarlo |
|---|---|---|
| P01 | [Entorno y herramientas](protocols/01-ENVIRONMENT-AND-TOOLS.md) | Verificar o preparar herramientas, únicamente con autorización. |
| P02 | [Ingesta y almacenamiento](protocols/02-DOCUMENT-INGESTION-AND-STORAGE.md) | Recibir, clasificar, conservar y organizar fuentes. |
| P03 | [Construcción de contratos MD](protocols/03-CONTRACT-SYNTHESIS.md) | Transformar JSON, nodos de Figma y documentación en un contrato para revisión. |
| P04 | [Construcción en Figma](protocols/04-FIGMA-CONSTRUCTION.md) | Materializar un contrato aprobado o delegado de forma expresa y listo para ese destino. |
| P05 | [Autodocumentación y trazabilidad](protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md) | Registrar fuentes, decisiones, contratos, ejecución y evidencia. |
| P06 | [QA y validación](protocols/06-QA-AND-VALIDATION.md) | Revisar el contrato antes de aprobarlo y validar la implementación después. |
| P07 | [Componentes web y documentación técnica](protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md) | Implementar y documentar componentes React/TypeScript/Tailwind/Next.js para diseñar pantallas sin backend. Obligatorio al agregar o modificar componentes del DS. |
| P08 | [Skills de consumo y releases](protocols/08-SKILLS-AND-RELEASES.md) | Entregar y actualizar las dos skills versionadas al cerrar altas o cambios en componentes, specs, tokens, assets o documentación de consumo del DS. |
| P-SLOTS | [Revisión e implementación de Slots](protocols/SLOTS-REVIEW-AND-IMPLEMENTATION.md) | Revisión transversal obligatoria de aplicabilidad; implementar y validar Slots cuando el contenido deba variar en cantidad o composición. |

Flujo normal: **P02 → P03 → QA documental → aprobación humana → P04 → lectura del resultado → QA de implementación.** La migración acotada desde la Librería anterior admite decisión delegada y auditoría humana posterior según P03. P01 se aplica según capacidades necesarias; P05 acompaña todas las fases.

Un contrato ya aprobado no necesita sintetizarse de nuevo: verifica su versión, aprobación, fuentes y dependencias antes de P04.

Antes de construir o modificar cada familia, aplica P-SLOTS y registra `REQUIRED`, `NOT_APPLICABLE` justificado o `UNRESOLVED`. Un ejemplo de cantidad fija no limita la cardinalidad. Un frame nombrado Slot o unas instancias expuestas no prueban Slots implementados. La revisión se incorpora a P03/P04/P06, no añade una fase automática de reconstrucción global.

## Autoridad documental

Las instrucciones superiores de la herramienta, los permisos y la seguridad siguen vigentes. Dentro del proyecto:

- Las decisiones explícitas del usuario gobiernan el alcance. Un cambio de diseño debe registrarse antes de propagarse a implementaciones.
- La especificación vigente es el contrato aprobado junto con sus datos canónicos referenciados. El Markdown gobierna las reglas; el JSON gobierna los campos que el contrato le delega. No mantengas dos definiciones editables del mismo dato.
- Una enmienda aprobada solo sustituye los requisitos y versiones que identifica. No gana por ser más reciente o llamarse `corrected`.
- Ante contradicción entre fuentes aprobadas, registra `CONFLICT` y detén la operación afectada. No elijas silenciosamente por formato o apariencia.
- Inventarios sin aprobar, auditorías, ejemplos, Figma observado, código y Graphify son evidencia. No se convierten en norma por existir.

## Reglas globales

**Excepción de identidad de personajes:** [DEC-CHARACTER-IDENTITY-001](registry/DEC-CHARACTER-IDENTITY-001.md) y la [enmienda Conversation0.1.1](specs/components/conversation.character-identity.amendment.v0.1.1.md) exigen que BENI/NAVI conserven colores originales mediante tokens directos de la colección fija `character-identity`, sin alias semántico ni variación por tema. Su JSON de extensión es canónico para esos valores. Excepción limitada a esos personajes; no permite primitivas directas o colores fijos en el resto de la UI.

No inventes intención, tokens, estados, variantes, valores ni aprobaciones. Distingue `EXPLICIT`, `DERIVED`, `OBSERVED`, `INFERRED`, `UNRESOLVED` y `CONFLICT`; su procedencia no equivale a su aprobación. Un contrato sintetizado empieza en `DRAFT` y normalmente requiere aprobación humana explícita antes de construir. Aprobar un protocolo o una plantilla no aprueba contratos futuros.

**Excepción acotada de migración:** [DEC-LEGACY-MIGRATION-DELEGATION-001](registry/decisions.md) registra la solicitud posterior del usuario de reconstruir la biblioteca anterior `9zs5RMR8LB5wHjW9Bd59BA` en `AI-Design-System` sin aprobación previa por componente y con auditoría humana posterior. P03/P04/P05/P06 definen `DELEGATED_FOR_BUILD` para ese alcance: no significa `APPROVED` por el usuario. Exige fuentes, contrato versionado, QA documental, mapa al JSON aprobado, ausencia de conflictos bloqueantes y QA posterior; no autoriza inventar variables, resolver incertidumbres materiales ni sobrescribir destructivamente componentes ajenos.

**Publicación delegada y auditoría por excepciones:** [DEC-MIGRATION-SPECS-AUDIT-001](registry/decisions.md) autoriza que los contratos de esta migración con QA documental e implementación técnica `PASS` se ubiquen en `specs/` sin cambiar su estado `DELEGATED_FOR_BUILD` ni simular aprobación humana. Su auditoría sigue `PENDING` y se consolida en un único documento de ambigüedades y asuntos no resueltos, no en aprobaciones repetitivas por componente. Si una instrucción nueva invalida el QA previo, se revalida la parte afectada antes de promoverla.

**Ajustes posteriores a la publicación documental:** [DEC-MIGRATION-SPECS-CANONICAL-001](registry/decisions.md) confirma que `specs/` es la ubicación de los contratos normativos de esta migración una vez promovidos. Los ajustes posteriores se redactan allí mismo como revisión versionada o enmienda con alcance explícito, QA afectado y registro de cambio; no se abre otro contrato normativo en `drafts/` ni se altera silenciosamente una versión histórica. Los borradores de observación y los reportes de evidencia permanecen en sus ubicaciones propias. La ubicación en `specs/` sigue sin equivaler a aprobación humana ni a publicación de la biblioteca Figma.

Usa una sola `description` canónica por token. No crees `usage` ni descripciones paralelas. Conserva aliases y bindings; igualdad visual no implica igualdad semántica. Preserva fuentes originales e IDs de origen; registra los IDs reales de destino por separado.

Las plantillas de `templates/` no son contratos aprobados. No copies sus instrucciones editoriales a requisitos finales ni completes campos desconocidos con datos del ejemplo de Button.

**Destino de reconstrucción:** `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`. P04 define la URL, el nombramiento semántico de una página por familia y el uso verificable de variables locales del destino. P03 exige documentar el nombre de página y el mapeo de tokens antes de declarar preparación Figma. El nodo fuente de extracción no sustituye este destino.

Para contratos de componentes que consumen tokens, el inventario JSON aprobado en `sources/inventories/tokens.inventory.json`, vinculado por `FOUNDATIONS-TOKENS-001`, es la fuente canónica de nombres, tipos, modos, valores, aliases y `description`. Los IDs de variables del archivo destino se obtienen del Figma real y se mapean a ese inventario; no se deducen por igualdad visual.

**Estilos tipográficos compartidos:** [DEC-TYPOGRAPHY-STYLES-001](registry/DEC-TYPOGRAPHY-STYLES-001.md), el [contrato tipográfico](specs/foundations/typography.contract.v0.1.0.md) y su [enmienda de formato 0.1.1](specs/foundations/typography.formatting.amendment.v0.1.1.md) y la [enmienda nativa 0.1.2](specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) exigen consumo de estilos verificable por texto/rango: asignación directa o la excepción nativa acotada con evidencia. El [catálogo activo 0.1.2](specs/tokens/ai-design-system.typography.v0.1.2.json) gobierna propiedades, unidades, decoración y la única `description` de uso; no edites el inventario histórico ni mantengas recetas aisladas duplicadas. La [enmienda transversal y sus 43 Specs de consumo](specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) identifican texto/rol/variante → estilo lógico → TextStyle ID, incluidas dependencias y exclusiones justificadas. Para texto local nuevo elige entre los 18 estilos base según función; conserva los complementarios restringidos de los componentes existentes. Registra el mapeo, verifica propiedades resueltas y overrides por destino y aplica estilos completos por rango donde corresponda, sin setters posteriores de formato. En la excepción nativa, comprueba principal/cadena/escala y no asignes el derivado materializado a la instancia; un ID local vacío no basta. Un rango con aplicación bloqueada se conserva identificado y no impide comprobar los independientes. Sincroniza documentación y ambas skills según P05/P06/P07/P08 antes de cerrar el alcance afectado. Una regla nueva o el catálogo creado no convierten automáticamente los consumidores históricos en revalidados.

En esta migración, [DEC-MIGRATION-VISUAL-FIDELITY-001](registry/decisions.md) prioriza conservar los colores observados en la Librería anterior. Una mejora no cambia colores por criterio de contraste; si falta el rol semántico correcto, se crea un token de destino con alias a una primitiva existente del mismo color, con JSON/contrato/Figma sincronizados. Las incompatibilidades entre fidelidad, contraste y primitivas disponibles se registran para la auditoría por excepciones; no se ocultan bajo un `PASS` anterior.

La instrucción más reciente [DEC-MIGRATION-NEAREST-PRIMITIVE-001](registry/decisions.md) y la [enmienda transversal 0.1.2](specs/MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.2.md) sustituyen esa excepción histórica: si falta RGB primitivo exacto, prioriza una primitiva existente semejante y crea o reutiliza un rol semántico del scope correcto que la aliase. Documenta la diferencia visual y el contraste; no uses la primitiva directamente como fill del componente, no crees otra por defecto ni alteres el inventario histórico. La [enmienda 0.1.1](specs/MIGRATION-TOKEN-TRACEABILITY.amendment.v0.1.1.md) queda como registro histórico, no regla vigente.

El [contrato transversal de fidelidad y trazabilidad](specs/MIGRATION-TOKEN-TRACEABILITY.contract.md), solicitado en [DEC-MIGRATION-TRACEABILITY-001](registry/decisions.md), fija la cadena de evidencia obligatoria para revisar las familias existentes y construir las siguientes. Su [matriz de cobertura](specs/MIGRATION-TRACEABILITY-STATUS.md) informa qué está revalidado y qué sigue pendiente; no reemplaza el JSON canónico ni los contratos de cada familia.

Graphify es un índice derivado, no una autoridad. Confirma los hallazgos contra la fuente. [DEC-GRAPH-CONTINUOUS-SYNC-001](registry/DEC-GRAPH-CONTINUOUS-SYNC-001.md) autoriza y exige mantener actualizado el grafo local completo del corpus DS tras cambios relevantes: contratos, datos canónicos, decisiones, protocolos, QA, registros o implementación. Ejecuta el cierre incremental estructural y semántico de P05 por lote coherente, verifica JSON/reporte/HTML, cobertura, integridad, manifiesto y consultas antes de declarar CURRENT. No basta un refresco AST para documentos. Sin nuevas fuentes, confirma vigencia por hashes y no regeneres innecesariamente. Si falla, conserva respaldo, registra STALE/BLOCKED y comunica el límite; nunca simules CURRENT. No autoriza instalaciones, servicios externos, hooks globales ni cambios Figma. Una prohibición explícita posterior de actualizar el grafo prevalece. La solicitud DEC-WEB-COMPONENTS-001 activa la biblioteca web con React + TypeScript + Tailwind CSS + Next.js, sustituyendo la previsión Vite. P07 exige código reutilizable, documentación técnica y ejemplo sin backend para cada componente nuevo o modificado. La solicitud actual autoriza esta capa local; no implica backend, publicación remota ni aprobación visual ficticia.

## Estados y cierre

**Skills como entregable obligatorio:** [DEC-DS-SKILLS-001](registry/DEC-DS-SKILLS-001.md) y P08 exigen que `contpaqi-figma-screens` y `contpaqi-po-prototypes` se generen desde el mismo corte del DS. Al terminar un alta o modificación, sincroniza ambas, comprueba su vigencia y entrega los paquetes versionados; actualiza las copias locales gestionadas cuando ese destino esté autorizado. No cierres la tarea solo con specs o código si las skills quedaron desactualizadas. No edites snapshots de consumo ni las dos skills históricas. Las composiciones locales de una pantalla no se promueven automáticamente al DS. Esta obligación forma parte del cierre del lote; no exige monitores, servidores ni hooks globales.

No confundas aprobación del contrato, preparación del destino y validación de la implementación. P03 define el ciclo documental; P05 registra el estado por destino; P06 define los criterios de cierre.

Sin fuentes suficientes puedes documentar un borrador parcial, pero no declararlo listo. Sin capacidad de escritura puedes sintetizar desde datos accesibles, pero no construir. Sin evidencia de QA no declares una implementación `VALIDATED`.

Antes de cerrar, registra qué leíste, qué cambiaste, qué comprobaste, qué sigue bloqueado y qué decisión se necesita. No uses la conversación como único registro persistente.

Las instrucciones locales de Graphify que siguen operan dentro del alcance autorizado para cada tarea. Si una solicitud excluye actualizar el grafo, registra su estado `STALE` y conserva los artefactos existentes.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
