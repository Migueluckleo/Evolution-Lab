# Specs Driven Design · Protocolos para Codex

**Versión operativa integrada:** 0.5.0 · **Política operativa actualizada:** 2026-10-16

Documentación operativa y contratos del sistema de diseño, con implementaciones en Figma y una biblioteca web local para crear pantallas con React, TypeScript, Tailwind y Next.js.

## Componentes web

[Catálogo y guía de ejecución](implementations/web/README.md): 43 familias con código, documentación técnica y ejemplos sin backend. Ejecutar `pnpm --dir implementations/web dev` y abrir http://127.0.0.1:3000. El [P07](protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md) exige mantener código, documento y ejemplo para cada alta o modificación. [QA y límites](qa/implementations/web.v0.1.0.review.md).

## Skills para construir pantallas

- [contpaqi-figma-screens](skills/contpaqi-figma-screens/SKILL.md): pantallas editables en Figma desde un prompt, imágenes de referencia o el traspaso del prototipo. Reutiliza el DS; documenta las composiciones locales cuando falta una pieza.
- [contpaqi-po-prototypes](skills/contpaqi-po-prototypes/SKILL.md): prototipos React/TypeScript/Tailwind/Next.js entregados como HTML interactivo autónomo y Markdown para la primera skill. Abrir el resultado no requiere servidor.

[P08](protocols/08-SKILLS-AND-RELEASES.md) exige actualizar ambas al cerrar cada alta o modificación del DS. Sus paquetes comparten versión y digest de fuentes; `scripts/ds skills check` detecta desactualización. [Releases y QA](registry/skills.md). Las dos skills históricas se conservan.

## Estado de la migración

La [vista derivada por familia](registry/generated/project-status.md) reúne base, enmiendas y evidencia por alcance desde sus documentos propietarios. Se regenera con `./scripts/ds status --write`; no se edita a mano ni concede aprobación.

Verificación local: `./scripts/ds check`. Consulta de una familia: `./scripts/ds status SEARCH-001`. Plan de actualización del grafo sin cambios: `./scripts/ds graph plan`. El [procedimiento operativo](references/PROJECT-TOOLING.md) describe preparación, extracción semántica y cierre verificado, sin instalaciones ni servicios externos.

La [política de retención](references/ARTIFACT-RETENTION.md) separa evidencia y entregables de cachés/intermedios locales; conserva el grafo activo y define la recuperación antes de retirar derivados del seguimiento en Git.

Consulta el [estado consolidado de construcción y trazabilidad](specs/MIGRATION-TRACEABILITY-STATUS.md), la [adopción de Slots](registry/SLOTS-REVIEW-STATUS.md) y la [auditoría por excepciones](specs/MIGRATION-AUDIT.md). Los registros históricos no son la cola actual. En la migración delegada, un contrato puede construirse y pasar a specs bajo `DELEGATED_FOR_BUILD` y QA técnico, sin simular aprobación humana; véase AGENTS. La publicación en specs y la publicación de biblioteca Figma son operaciones distintas.

## Qué cambia

Se incorpora **P03: Contract Synthesis** antes de construcción. El agente ya no salta desde un JSON organizado a Figma: redacta un contrato candidato, lo contrasta con las fuentes y registra delegación técnica tras QA documental para continuar la construcción solicitada, según [DEC-AI-TECHNICAL-CLOSURE-001](registry/DEC-AI-TECHNICAL-CLOSURE-001.md). La revisión humana es opcional y no bloquea el cierre; el agente mantiene documentación y evidencia.

```text
JSON / nodo Figma / documentación
                ↓
       P02 · Ingesta y almacenamiento
                ↓
       P03 · Contrato MD candidato
                ↓
       P06 · QA documental
                ↓
       Delegación técnica de versión y alcance
                ↓
       P04 · Construcción en Figma
                ↓
       Readback + P06 · QA de implementación

P01 comprueba capacidades cuando hacen falta.
P05 registra evidencia y estado durante todo el recorrido.
```

## Archivos principales

| Archivo | Función |
|---|---|
| [AGENTS.md](AGENTS.md) | Orientación y acceso a los ocho protocolos y la revisión transversal P-SLOTS. |
| [P01](protocols/01-ENVIRONMENT-AND-TOOLS.md) | Instalación y verificación técnica, bajo autorización. |
| [P02](protocols/02-DOCUMENT-INGESTION-AND-STORAGE.md) | Clasificación, originales, ubicación y procedencia. |
| [P03](protocols/03-CONTRACT-SYNTHESIS.md) | Síntesis desde JSON, nodo Figma o fuentes combinadas. |
| [P04](protocols/04-FIGMA-CONSTRUCTION.md) | Construcción desde contrato aprobado o delegado técnicamente; página por familia. |
| [P05](protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md) | Registros, decisiones, versiones e identidad de destinos. |
| [P06](protocols/06-QA-AND-VALIDATION.md) | Revisión documental y validación posterior separadas. |
| [P07](protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md) | Código React/TypeScript, tokens/Tailwind, catálogo Next.js y documentación obligatoria por componente. |
| [P08](protocols/08-SKILLS-AND-RELEASES.md) | Skills de consumo como entregables versionados del DS, sincronización, paquetes e instalación local gestionada. |
| [P-SLOTS](protocols/SLOTS-REVIEW-AND-IMPLEMENTATION.md) | Revisión transversal de contenido variable, implementación real de Slots y QA desde instancias consumidoras. |
| [Plantilla de componente](templates/component.contract.template.md) | Las 21 secciones del ejemplo, sin heredar sus datos. |
| [Plantilla de foundations](templates/foundations.contract.template.md) | Contrato que referencia el inventario canónico. |
| [Reporte de síntesis](templates/contract-synthesis-report.template.md) | Evidencia, cobertura, propuestas y preguntas. |
| [Migración](MIGRATION-v0.2.0.md) | Incorporación controlada al proyecto existente. |
| [Prompt de integración](prompts/01-INTEGRATE-PROTOCOLS.md) | Instrucción histórica utilizada para integrar el paquete. |
| [Prompt de síntesis](prompts/02-SYNTHESIZE-CONTRACT.md) | Instrucción para cuando se entreguen fuentes reales. |
| [Changelog](CHANGELOG.md) | Cambios operativos de esta versión. |
| [Fuentes documentales](references/DOCUMENTATION-SOURCES.md) | Alcance de los referentes utilizados. |
| [Operación de Graphify](references/GRAPH-OPERATIONS.md) | Reglas locales complementarias de autodocumentación del grafo. |
| [Verificación del paquete](PACKAGE-VERIFICATION.md) | Comprobaciones locales realizadas antes de entregar. |
| [Registro de migración](registry/protocol-migrations.md) | Respaldos, cambios y verificaciones de esta integración. |

## Integración en este proyecto

La versión 0.2.0 se integró en `AGENTS.md`, `protocols/`, `templates/`, `prompts/` y `references/`. El paquete recibido y la versión operativa anterior se conservaron como material inactivo en `archive/`; el registro de migración identifica sus rutas y digests.

Para nuevas fuentes, usa el [prompt de síntesis](prompts/02-SYNTHESIZE-CONTRACT.md) con el archivo real o la URL y node ID fuente. No se incluyeron inventarios JSON ni contratos reales en esta migración.

Para que el inicio de la siguiente sesión use la nueva cadena de instrucciones, abre una nueva sesión de Codex en la raíz. Referencia: `https://developers.openai.com/codex/guides/agents-md/`.

## Reglas que se mantienen

La especificación vigente aprobada o delegada conforme P03 gobierna Figma y web. El MD expresa reglas y referencia datos canónicos; la `description` de cada token mantiene un único propietario. Graphify es navegación y no aprobación. Crear algo no demuestra que cumpla.

El destino acordado sigue siendo `AI-Design-System`, file key `tj3WIBEZDGLVs7MJWKCwgf`. Cada familia de componentes principales tiene una página. Variantes, tamaños y estados de Button no generan páginas independientes.

## Lo que este paquete no resuelve por sí solo

No identifica automáticamente el proveedor de Figma MCP instalado, no acredita sus permisos y no instala Graphify. Una URL de diseño no es una URL de instalación. La fase de entorno debe comprobar capacidades reales cuando se autorice.

Las nuevas plantillas son herramientas de redacción, no valores por defecto del sistema. El esquema de metadatos, los IDs de requisitos y los estados documentales son convenciones de este proyecto, no una afirmación de que exista un estándar universal de contratos SDD.

El manifiesto recibido está archivado en `archive/packages/SHA256SUMS-v0.2.0.txt`. Acredita los bytes del paquete original, no los archivos fusionados con reglas locales; estos tienen digests finales en el registro de migración. No constituye una firma digital ni aprobación del diseño.
