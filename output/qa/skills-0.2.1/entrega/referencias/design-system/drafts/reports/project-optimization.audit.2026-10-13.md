# Revisión de Graphify y optimización del proyecto · 2026-10-13

Estado: **OBSERVED / propuestas no adoptadas**. Alcance: verificar Graphify y analizar documentación y protocolos. No cambia contratos, tokens, diseños, aprobaciones ni reglas del proyecto.

## Dictamen

Graphify está instalado y operativo. La herramienta vive en el entorno de usuario de `uv`; la skill y el grafo están dentro del repositorio. No hace falta reinstalar para las capacidades probadas.

La arquitectura documental separa correctamente procedencia, autoridad, preparación, implementación y auditoría humana. La oportunidad principal es reducir conciliación manual, aislar el estado vigente del historial y convertir los controles mecánicos en una ejecución reproducible.

## Verificación

Evidencia calculada: [baseline-verification.json](../../graphify-out/runs/2026-10-13-project-audit/baseline-verification.json). Conteos anteriores a agregar este reporte y su entrada de entorno.

| Comprobación | Resultado observado |
|---|---|
| Ejecutable | `/Users/miguel.leo/.local/bin/graphify`, resuelve al entorno `uv/tools/graphifyy`. |
| Versión/runtime | Graphify **0.9.65**, Python **3.12.13**; paquete requiere Python >=3.10. Importación correcta. |
| Integración | `.codex/skills/graphify/SKILL.md`, referencias y bloque Graphify en AGENTS presentes. |
| CLI | `--version`, `--help`, `query`, `explain`, `diagnose multigraph`, `hook status`, `check-update` y `reflect --if-stale` ejecutados. |
| AST | Fixture Python temporal fuera del corpus: 3 nodos y 3 relaciones; llamada `root()` → `leaf()`. |
| Grafo inicial | **8,058 nodos / 18,019 relaciones**; cero IDs duplicados y cero endpoints rotos. |
| Vigencia inicial | **1,172 archivos** del manifiesto con hashes concordantes; cero archivos nuevos en el corpus detectado y filtrado. |
| Outputs iniciales | JSON, HTML y reporte coinciden por SHA-256 con el cierre Fuentes del 2026-10-09. |
| Sintaxis JSON | **459 archivos** parseados sin errores. No es validación de esquemas ni QA de tokens. |
| Hooks Git | Post-commit/post-checkout no instalados; merge driver no registrado. No son requisito de las consultas probadas. |
| Hook Codex | `.codex/hooks.json` presente; ejecución por el host no verificada. |
| Enlaces históricos | **21 referencias relativas rotas**: 18 en respaldos de promoción y 3 en candidatos preservados de QA. No son endpoints rotos ni defectos nuevos de Figma. |

La instalación por `uv` y el registro de skill son operaciones separadas, coherentes con [P01](../../protocols/01-ENVIRONMENT-AND-TOOLS.md) y la [fuente oficial consultada](https://github.com/Graphify-Labs/graphify). No se certifica que 0.9.65 sea la versión más reciente ni que deba actualizarse.

El detector ordinario omite cuatro JSON de diseño por su nombre y ocho fuentes Mermaid no entran como documentos. El cierre local los agrega mediante rutas explícitas; sí están dentro de los 1,172 archivos. Las cinco entradas de `skipped_sensitive` son:

- `sources/inventories/tokens.inventory.json`.
- `sources/figma-snapshots/input-fields.followups.target-tokens.json`.
- `qa/implementations/select.v0.1.0.tokens.json`.
- `qa/implementations/radio-checkbox.refinement.v0.1.0.tokens.json`.
- `implementations/figjam/sdd-flow-2026-10-07/03-tokens.mmd`.

No se desactivaron filtros de secretos. PyYAML no está en el runtime Graphify: no se validó YAML con ese parser ni se instaló. Esto no afecta las capacidades Graphify probadas. La búsqueda CLI de un camino dirigido DEC-GRAPH→P05 no devolvió ruta; no equivale a ausencia de relación documental. Los enlaces reales y las consultas deben comprobarse por identidad/dirección.

## Mejoras propuestas, por prioridad

### 1. Un punto de entrada para verificar y cerrar el proyecto

**Evidencia:** [P05 §8](../../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md) exige delta estructural/semántico, cobertura, manifiesto final y outputs concordantes. La ayuda instalada describe `graphify update` como extracción de código. El cierre completo depende de [refresh-2026-10-08.py](../../graphify-out/refresh-2026-10-08.py), con rutas suplementarias, digest del inventario y casos de familias incorporados en el script. Ese archivo estaba sin seguimiento Git. No se encontró `scripts/` ni workflows locales en `.github/workflows/`.

**Propuesta:** mantener ese procedimiento fuera de `graphify-out/`, con configuración declarativa del corpus y suplementos, versión de runtime/herramienta fijada y operaciones separadas de verificar sin cambios, planificar delta, extraer y cerrar. Preservar respaldo antes de escribir. La semántica debe usar las capacidades autorizadas de la sesión; no presuponer APIs externas ni ejecución automática en CI.

**Aceptación:** sin delta no reescribe; un Markdown nuevo exige semántica; incluye JSON canónicos; conserva el corte anterior ante interrupción; CURRENT requiere readback/hashes. No sustituirlo por un hook AST-only.

### 2. Una vista derivada del estado vigente por familia

**Evidencia:** los seis registros principales suman 2,898 líneas. La [matriz](../../specs/MIGRATION-TRACEABILITY-STATUS.md) y [auditoría](../../specs/MIGRATION-AUDIT.md) necesitan aclaraciones para no reabrir tareas cerradas. El cierre cromático del 2026-10-05 resuelve Charts; un párrafo histórico inferior aún dice que su swatch sigue en análisis. Hay menciones STALE históricas seguidas por sincronizaciones exitosas.

**Propuesta:** generar por ID contrato base, enmiendas aplicables, alcance sustituido, autorización, preparación por destino, QA vigente, auditoría humana y acción pendiente, con enlaces al historial. Derivar desde metadatos propietarios existentes; cualquier cambio de propiedad de datos requiere definición explícita. No crear otro catálogo editable que compita con los contratos.

**Aceptación:** consultar una familia revela versión efectiva y evidencia sin recorrer la cronología. PASS técnico, auditoría PENDING y biblioteca UNPUBLISHED siguen separados. No resolver vigencia solo por fecha.

### 3. Automatizar el QA documental determinista

**Evidencia:** [P06](../../protocols/06-QA-AND-VALIDATION.md) enumera 18 controles documentales. Hay 9 scripts `.cjs` y 6 `.js` en QA, pero no un punto de entrada común observado. [README](../../README.md) anuncia paquete 0.2.3; AGENTS y P05 usan 0.2.4; falta entrada 0.2.4 en el changelog. Las versiones individuales de protocolos pueden diferir legítimamente: el desfase es de la versión declarada del paquete.

**Propuesta:** reutilizar verificadores y sumar sintaxis YAML/JSON, enlaces, IDs, campos requeridos, digests, dependencias y sustituciones por alcance. Separar errores actuales de enlaces históricos. Un mapa de ubicación original puede resolver respaldos sin alterar sus bytes. Los esquemas nuevos son propuestas a revisar, no supuestos estándares externos.

**Aceptación:** cada fallo señala archivo/localizador/control; referencias históricas se conservan con procedencia; un error nuevo vigente falla. Aprobar una prueba no aprueba el diseño. El juicio semántico permanece separado del PASS mecánico.

### 4. Reducir el peso de derivados en Git

**Evidencia:** al inicio había **26 archivos seguidos modificados y 571 sin seguimiento**. Entre archivos seguidos que existen en el working tree, `graphify-out/` ocupa **172.2 MiB de 188.0 MiB**, aproximadamente **91.6 %**, en 812 archivos. No es el tamaño de `.git` ni de todo el historial. `.gitignore` no excluye cachés Graphify, runs, `tmp/`, `output/` o `.codex-build/`; algunas rutas ya tienen archivos seguidos.

**Propuesta:** separar fuentes/evidencia irreemplazable de cachés, exportaciones y respaldos regenerables. Conservar corte activo y manifiestos necesarios; definir retención para cortes completos. Evaluar almacenamiento de artefactos según el equipo. Agregar ignore no retira archivos ya seguidos.

**Aceptación:** revisiones más ligeras y recuperación demostrable. Clasificar y respaldar antes del cambio autorizado. No se eliminaron, desindexaron ni confirmaron archivos en esta revisión.

### 5. Acortar la ruta de lectura sin debilitar la gobernanza

**Evidencia:** P03/P04/P06 repiten reglas de delegación, bindings y aprobación. P03 presenta delegación exclusiva de la Librería anterior; [DEC-EXTERNAL-COMPONENTS-DELEGATION-001](../../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md) la amplía para incorporaciones externas señaladas por el usuario. La decisión gobierna, pero la ruta de lectura puede detenerse en la regla anterior.

**Propuesta:** una guía breve por intención —consultar, verificar, sintetizar, construir, revalidar— enlaza secciones y excepciones aplicables. Cada regla tiene un protocolo propietario; los demás lo referencian. Preservar alcance de decisiones, identidad BENI/NAVI y aproximación a primitivas existentes. Reconciliar README/changelog en una revisión documental autorizada.

**Aceptación:** ruta clara a gates y autoridad; leer no dispara fases; historia no se borra ni se convierte en autorización nueva.

### 6. Revalidar por impacto y preparar la frontera con frontend

**Evidencia:** P05 exige localizar consumidores afectados. Chat layout 0.1.1 conserva QA interactivo parcial; existen decisiones pendientes de Logos, Tooltip, Toggle y Avatar. Los contratos visuales dejan fuera teclado, foco, ARIA y backend.

**Propuesta:** derivar requisito → datos/dependencias → consumidor → prueba. Graphify localiza candidatos; las fuentes confirman las dependencias. Un digest/enmienda nuevo señala el QA preciso a repetir. Al iniciar frontend, definir comportamiento y criterios accesibles para los componentes elegidos y después habilitar la pila prevista en P01.

**Aceptación:** no repetir cierres válidos sin cambios; una captura no certifica web; las excepciones tienen entidad, alcance, evidencia y decisión requerida. No reabrir familias omitidas ni recolorear automáticamente.

## Secuencia sugerida y límites

1. Reconciliar versión del paquete y diseñar índice de vigencia/configuración del corpus.
2. Implementar verificador local común reutilizando controles existentes.
3. Encapsular cierre Graphify e impacto por hashes.
4. Definir retención de derivados; adoptar CI determinista si el equipo decide compartir el flujo.
5. Tratar excepciones de diseño y frontend como decisiones separadas.

Medir antes/después tiempo para encontrar contrato vigente, duración del cierre incremental, enlaces activos rotos, cobertura de hashes y bytes regenerables. No se prometen ahorros numéricos sin baseline.

Se leyeron AGENTS, skill Graphify y referencia de consultas, P01–P06, P-SLOTS, operación del grafo, decisión de sincronización, README y changelog. Se inspeccionaron manifiesto/cierre Fuentes, script local, registros y matrices relevantes, muestras de contratos/QA/enmiendas. No se afirma lectura semántica completa de los 1,172 archivos.

Se agregaron este reporte, evidencia local y una entrada en `registry/environment.md`. Recomendaciones sin adoptar. El nuevo cierre se registra en `graphify-out/runs/2026-10-13-project-audit/verification.json` y `manifest-check.json`; solo su PASS efectivo acredita el corte, no esta declaración prospectiva.

Sin bloqueo para terminar la revisión. Queda decidir qué mejoras implementar. No hubo instalación/actualización, cambios de hooks/globales, servicios externos, cambios Figma ni publicación remota.
