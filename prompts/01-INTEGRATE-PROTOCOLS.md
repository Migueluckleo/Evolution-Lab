# Prompt 01. Integrar el paquete documental

Pegar en Codex desde la raíz real del proyecto, después de colocar dentro la carpeta completa `sdd-codex-protocols-v0.2.0/`. No ejecutar desde la carpeta del paquete.

```text
Integra el paquete documental sdd-codex-protocols-v0.2.0 que he colocado en este proyecto.

Autorizo esta actualización de protocolos y las modificaciones locales necesarias para incorporarla. No estoy aprobando ningún contrato de componente ni autorizando instalaciones o construcción en Figma.

Primero lee el AGENTS.md activo, los protocolos existentes y MIGRATION-v0.2.0.md del paquete. Después lee los archivos nuevos y ejecuta la migración indicada, preservando cualquier mejora local compatible. Si no localizas el paquete, pídeme la ruta exacta; no reconstruyas su contenido por suposición.

La estructura activa debe quedar con estos seis protocolos dentro de protocols/:
01-ENVIRONMENT-AND-TOOLS.md
02-DOCUMENT-INGESTION-AND-STORAGE.md
03-CONTRACT-SYNTHESIS.md
04-FIGMA-CONSTRUCTION.md
05-SELF-DOCUMENTATION-AND-TRACEABILITY.md
06-QA-AND-VALIDATION.md

Integra AGENTS.md como guía breve y actualiza todas las referencias afectadas. Incorpora las plantillas, los prompts y la documentación de migración. Respalda las versiones anteriores y retira sus copias de las rutas activas únicamente después de comprobar la sustitución.

No sobrescribas bloques ni configuración de Graphify. Conserva instrucciones locales compatibles y consulta cualquier conflicto real antes de resolverlo. No reinstales herramientas, no regeneres el grafo, no accedas a Figma, no generes frontend, no modifiques JSON ni contratos existentes y no crees un contrato real usando datos del ejemplo o de las plantillas.

No necesito entregarte los JSON todavía. Esta tarea es exclusivamente integrar y comprobar el nuevo flujo:
fuentes → ingesta → síntesis de contrato MD → QA documental → aprobación humana → construcción → readback → QA de implementación.

Verifica que cada enlace activo apunte a un archivo existente, que no queden dos versiones operativas del mismo protocolo y que permanezca la regla de una página de Figma por familia en el archivo tj3WIBEZDGLVs7MJWKCwgf.

Al terminar, registra y muéstrame qué archivos agregaste, actualizaste, moviste y respaldaste, qué comprobaste y qué no ejecutaste. Explica también, sin generar contratos ficticios, cómo procesarías un JSON de tokens y cómo procesarías un nodo Figma, señalando en qué punto esperarías mi aprobación.
```
