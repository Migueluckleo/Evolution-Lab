# QA-ARTIFACT-RETENTION-001

Fecha: 2026-10-13. Alcance: [DEC-ARTIFACT-RETENTION-001](../../registry/decisions.md), [política](../../references/ARTIFACT-RETENTION.md) y seguimiento local en Git. No cambia diseños, tokens, contratos ni auditoría humana.

## Lectura y clasificación

Se consultaron AGENTS, P02/P05, la skill Graphify, el grafo existente mediante consulta de retención/recuperación, la auditoría de optimización, la guía local, los registros y el índice real de Git. La fuente para la decisión es el contenido y los hashes de los archivos, no el grafo.

Se mantienen output (PDF/PPTX/Markdown/manifiestos), .codex-build (fuentes y evidencia), .codex-finalizer (validaciones), tmp y todos los originales de diseño. Las exclusiones afectan únicamente clases generadas expresamente enumeradas en .gitignore. Se conservan extracción semántica, memoria, QA y outputs activos de Graphify.

## Resultado del retiro del índice: PASS

[Manifiesto por archivo](retention.2026-10-13.manifest.json), [resultado calculado](retention.2026-10-13.results.json) y [verificador](retention.2026-10-13.verify.py).

| Medida | Antes | Después |
|---|---:|---:|
| Archivos en el índice, antes de incorporar archivos nuevos de otros lotes | 1,893 | 1,220 |
| Suma de tamaños de blobs del índice, sin comprimir | 187,228,558 bytes | 35,484,979 bytes |
| Archivos locales eliminados | 0 | 0 |

673 derivados retirados: 622 cachés, 16 intermedios de lotes, 32 copias previas de outputs y 3 archivos de snapshots fechados/vocabulario. Diferencia: 151,743,579 bytes (144.71 MiB, 81.05% del índice inicial). Los cambios locales existentes explican que el respaldo capture 151,779,581 bytes originales, una cifra ligeramente distinta del índice.

Comprobaciones ejecutadas:

- Archivo tar.gz de 7,840,848 bytes; hash SHA-256 registrado en el manifiesto.
- Cobertura 673/673, tipos regulares, nombres únicos, tamaños y hashes concordantes.
- Restauración real en directorio temporal y lectura posterior 673/673; ningún archivo del proyecto sobrescrito.
- Archivos locales idénticos al snapshot inmediatamente después de git rm --cached.
- Las únicas operaciones staged son las 673 bajas previstas; sin commit ni publicación.
- 1,187 archivos de fuentes, contratos, evidencia y entregables con hashes intactos.
- Cero enlaces Markdown directos a archivos retirados; once ejemplos protegidos no coinciden con las exclusiones.

La verificación del snapshot se puede repetir con --restore-test. --working comprueba igualdad con el momento de la limpieza; una futura regeneración legítima de cachés puede cambiar esos bytes. --index-removed comprueba las bajas en el índice actual. El respaldo no forma parte de un clon: requiere conservación local; la recuperación histórica usa los blobs registrados y el historial intacto.

## Cierre documental y Graphify

El control documental previo pasó: 462 JSON, 218 YAML/frontmatter y cuatro metadatos en prosa; ningún ERROR. El refresco literal graphify update . exigido después de añadir el verificador salió 0 (7,603 nodos, 13,753 relaciones AST). Se guardó su corte y se restauraron por hash los nueve outputs/marcador anteriores antes de preparar el cierre completo; [evidencia AST](../../graphify-out/runs/2026-10-13-retention-ast-check/verification.json). Ese refresco aislado no acredita documentación actualizada.

El resultado de índice es un corte anterior a la sincronización. El cierre estructural y semántico usa el lote graphify-out/runs/2026-10-13-retention, con respaldo before y gates de P05. CURRENT requiere closure.json, verification.json, manifest-check.json y scripts/ds check concordantes; la existencia de este reporte no lo acredita por sí sola. El resultado final se conserva en final-check.json del lote, sin cambiar retrospectivamente el checkpoint del índice.

No se purga espacio local ni se reescribe la historia: la mejora limita los archivos que seguirán en próximos commits y el crecimiento futuro. No hay decisiones pendientes para este lote. Simplificación de protocolos y revalidación por impacto permanecen fuera del alcance.
