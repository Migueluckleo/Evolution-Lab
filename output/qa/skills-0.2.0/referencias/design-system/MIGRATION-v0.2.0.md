# Migración documental a 0.2.0

**Alcance:** actualizar la gobernanza y añadir síntesis de contratos antes de construcción. No instalar herramientas, generar contratos reales ni tocar Figma.

## 1. Qué se autoriza

Al ejecutar el prompt de integración, el usuario autoriza incorporar esta versión del paquete, organizar los protocolos, crear respaldos de los archivos afectados y documentar la migración. No autoriza aprobar contratos futuros, reconfigurar Graphify o modificar fuentes del sistema de diseño.

## 2. Mapa exacto de archivos

| Archivo anterior | Archivo activo 0.2.0 | Operación |
|---|---|---|
| `AGENTS.md` | `AGENTS.md` | Actualizar gobernanza y enlaces conservando bloques locales compatibles. |
| `01-ENVIRONMENT-AND-TOOLS.md` | `protocols/01-ENVIRONMENT-AND-TOOLS.md` | Integrar cambios de lectura/escritura y preservar instalación existente. |
| `02-DOCUMENT-INGESTION-AND-STORAGE.md` | `protocols/02-DOCUMENT-INGESTION-AND-STORAGE.md` | Enviar fuentes a síntesis en vez de construir directamente. |
| No existe equivalente | `protocols/03-CONTRACT-SYNTHESIS.md` | Añadir. |
| `03-FIGMA-CONSTRUCTION.md` | `protocols/04-FIGMA-CONSTRUCTION.md` | Renumerar y añadir gate de contrato aprobado. |
| `04-SELF-DOCUMENTATION-AND-TRACEABILITY.md` | `protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md` | Renumerar y ampliar trazabilidad documental. |
| `05-QA-AND-VALIDATION.md` | `protocols/06-QA-AND-VALIDATION.md` | Renumerar y distinguir QA documental/de implementación. |

Los protocolos anteriores pueden estar en la raíz o en `protocols/`. Busca únicamente estos nombres y verifica su contenido; no uses un reemplazo global de todos los prefijos `03`, `04` o `05` del repositorio.

## 3. Preflight

Identifica raíz activa y carpeta del paquete recibido. Si no encuentras un único paquete 0.2.0, pide su ruta; no fabriques archivos faltantes a partir de recuerdos.

Lee AGENTS activo, protocolos afectados y README, además de este documento y los archivos nuevos. Inventaría modificaciones locales y configuración existente. Confirma el destino Figma ya acordado y la regla de páginas por familia.

Si existe Git, inspecciona cambios sin descartarlos. No hagas commit, push, reset, checkout ni limpieza de archivos ajenos. Sin Git, utiliza respaldos verificables.

## 4. Integración no destructiva

1. Conserva los archivos afectados antes de editarlos. Puedes usar `archive/protocols-pre-0.2.0/<run-id>/`, guardando el path original y el digest en un registro. Los respaldos pueden tener sufijo `.snapshot` para no convertirse en instrucciones activas.
2. Verifica el manifiesto del paquete calculando SHA-256 de bytes. No confíes únicamente en las cadenas escritas en el manifiesto.
3. Integra `AGENTS.md` sin borrar bloques creados por Graphify ni instrucciones específicas compatibles del usuario. Si aparece una contradicción, identifica ambas reglas y pide resolución del bloque afectado.
4. Coloca los seis protocolos activos dentro de `protocols/`. Integra mejoras locales compatibles; no sobrescribas a ciegas versiones que el usuario haya refinado.
5. Añade las tres plantillas, los prompts, las referencias, `PACKAGE-VERIFICATION.md` y este documento de migración. La verificación incluida acredita el paquete recibido, no una ejecución de QA en el proyecto del usuario. En README/CHANGELOG existentes, incorpora la sección pertinente conservando contenido no relacionado.
6. Retira de rutas activas los tres nombres de protocolos sustituidos, solo después de respaldarlos y confirmar equivalencia. Conserva historial; no elimines carpetas enteras.
7. Si 01/02 estaban en raíz, conserva respaldo y usa exclusivamente su ubicación activa bajo `protocols/`. No dejes dos copias vigentes que digan cosas distintas.
8. Actualiza los enlaces activos en AGENTS, README y protocolos por identidad de documento. Las referencias históricas en este documento son intencionales y no deben transformarse.
9. Registra cambios y discrepancias en `registry/protocol-migrations.md`, o en un registro equivalente ya existente, sin inventar aprobación de contratos.

El manifiesto SHA256SUMS acredita los bytes del paquete recibido antes de fusionar mejoras locales. Consérvalo junto a esa copia inactiva, no como certificación de los archivos fusionados; registra sus digests finales por separado.

El paquete de instalación y los respaldos son material inactivo. No los indexees como contratos aprobados. Su exclusión del corpus de Graphify se configurará/verificará cuando se autorice actualizar el grafo; no ejecutes esa actualización durante esta tarea.

## 5. Comprobaciones obligatorias

- AGENTS conserva una función de orientación, con seis rutas activas resolubles.
- P03 es síntesis de contratos; P04 es construcción Figma; P05 es trazabilidad; P06 es QA.
- El flujo incluye revisión documental y aprobación humana antes de P04.
- Los contratos siguen siendo `.md`; los JSON referenciados no se duplican como catálogos editables.
- La entrada JSON no activa Figma ni crea contratos de componentes inexistentes.
- La entrada nodo Figma no se considera contrato automáticamente aprobado.
- Las plantillas están claramente marcadas como no normativas y no existen contratos reales creados con sus datos de ejemplo.
- El destino sigue siendo `tj3WIBEZDGLVs7MJWKCwgf` y se exige página por familia.
- No hay protocolos antiguos simultáneamente activos; los respaldos son identificables.
- Se conservaron configuración/bloques de Graphify, fuentes JSON, contratos existentes y trabajo no relacionado.
- Las rutas, tablas, fences y frontmatter del paquete son legibles; no se asumió que archivos operativos previstos ya existen.

## 6. Reporte de salida

Informa archivos añadidos, actualizados, movidos y respaldados; hashes verificados; mejoras locales conservadas; conflictos; ruta del registro de migración y tareas no ejecutadas.

Explica sin ejecutar dos recorridos: JSON de tokens → borrador foundations, y nodo de componente → borrador componente. Identifica cuándo pedirías aprobación. No generes entidades ficticias para demostrar comprensión.

Finaliza con el sistema documental preparado. La aprobación e implementación de contratos reales serán tareas posteriores.

## 7. Recuperación

Si falla una escritura local, lee el estado real antes de repetirla. Usa los respaldos únicamente para archivos afectados; no restaures todo el repositorio ni borres trabajo posterior. Registra qué parte de la migración quedó aplicada.
