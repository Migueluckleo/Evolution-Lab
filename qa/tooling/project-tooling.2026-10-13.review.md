# QA-PROJECT-TOOLING-001 · 2026-10-13

Alcance autorizado: prioridades altas 1–3 de la auditoría de optimización. [Decisión](../../registry/decisions.md), [guía](../../references/PROJECT-TOOLING.md), [configuración](../../config/ds-project.json), [pruebas](../../tests/test_project_tooling.py).

## Resultado y reproducción

Regresión local: **21 pruebas PASS**. Incluye rechazo de JSON/YAML inválido o duplicado, carga YAML segura, enlaces históricos ligados a bytes exactos, datos canónicos protegidos, lectura sin mutaciones, metadatos de prosa sin aprobación inferida, sustitución explícita de bases, composición base_version, DRAFT/enmiendas sin reemplazo integral, semántica obligatoria para documentos nuevos, fuentes cambiadas tras prepare, cambios concurrentes del grafo y recuperación tras fallo parcial de publicación.

QA documental inicial: **PASS**, 460 JSON, 218 YAML/frontmatter; se añadieron cuatro contratos con metadatos explícitos en prosa al generador. Conteos finales y hallazgos efectivos se obtienen con scripts/ds check. La vista comprende 47 identidades, incluidas Foundations, contrato transversal y candidato Anticipa; no equivale a 47 familias Figma aprobadas. Base Search0.1.1 y Button0.2.0 se resuelven por sustitución/composición explícita. Chat Layout PARTIAL, Logos y las bases sin promoción conservan sus excepciones citadas desde los propietarios.

Quedan cuatro WARNING de dependencias declaradas sin identidad local resoluble: PLUS-CIRCLE-OBSERVED-001 y PHOSPHOR-ICONS-001 en Button0.1.0; PHOSPHOR-ICONS-001 en Button0.2.0; PlusCircle en Filter Chip0.2.0. No se inventa un contrato de icono. Los 21 enlaces históricos están permitidos solo por ruta, línea, destino y SHA-256 exactos; un enlace nuevo roto falla.

## Gate final del lote

El reporte no certifica por anticipado la sincronización. Cierre en graphify-out/runs/2026-10-13-high-priorities/: documentation-check.json, verification.json y manifest-check.json deben indicar PASS; closure.json debe indicar CURRENT y coincidir con los outputs actuales. El comando scripts/ds check verifica corpus, vista derivada y hashes del cierre. Sin esas condiciones el estado es STALE/BLOCKED.

Comandos de reproducción:

~~~sh
./scripts/ds test
./scripts/ds status --write
./scripts/ds check
./scripts/ds graph plan
~~~

El plan sin delta y prepare sobre un corte verificado deben responder CURRENT_NO_CHANGES sin regeneración. La evidencia final calculada y su prueba de idempotencia se guardan en el run, excluido del corpus para no provocar un ciclo de regeneración.

## Alcance y límites

Se revisaron P01/P05/P06, skill Graphify, runner anterior, metadatos contractuales, registros, auditoría y matriz transversal. Se implementaron launcher, módulos de verificación/estado/cierre, configuración y pruebas; se actualizaron README/changelog y referencias operativas. Se reutiliza la extracción estructural y de aliases del runner verificado; los verificadores .cjs por componente permanecen independientes y no se ejecutaron sin Node.

No hay nuevo QA visual/Figma, cambios a contratos o JSON de diseño, aprobación humana inventada ni publicación de biblioteca. No valida semánticamente todos los requisitos, anclas Markdown, enlaces remotos ni comportamiento frontend. No afirma recuperación atómica ante pérdida de alimentación; los hashes del marcador final permiten detectar publicación incompleta. Datos canónicos protegidos conservan su SHA-256 aprobado.

No se requieren nuevas decisiones para usar estas herramientas. Las cuatro dependencias señaladas y las excepciones de diseño continúan bajo sus registros existentes; el comando no las convierte en autorización de implementación.
