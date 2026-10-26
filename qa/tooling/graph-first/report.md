# Índice de consumo y adaptador compartido · 2026-10-23

Alcance autorizado: implementación local completa en la rama `codex/graph-first-consumption`, preservando cambios existentes. No se publicó en GitHub ni se modificó Figma. La fuente del encargo y el preflight están en [auditoría](audit.md) y [solicitud preservada](request.txt). El [contrato delegado](../../../drafts/contracts/graph-first-consumption.contract.v0.1.0.md) conserva la autoridad de las fuentes; el grafo es derivado.

## Implementación

- `scripts/ds_consumption.py`: proyección determinista desde el grafo local CURRENT, lista explícita de campos públicos, referencias verificadas en las fuentes, tokens mediante punteros JSON, comprobante de hashes del corte y de las herramientas. No exporta atributos libres, IDs internos, rationale ni rutas privadas del grafo.
- `scripts/consumer_graph.py`: única implementación mantenida, distribuida idéntica en ambas Skills. Consultas por componente, dependencias, evidencia, tokens, variantes y estados; límites explícitos, hash de cada documento, identidad de snapshot y métricas.
- Los cargadores existentes verifican el índice opcional dentro de la misma publicación inmutable del catálogo. Fallback explícito a contrato y enmiendas del snapshot íntegro; cobertura más limitada y revisión dirigida obligatoria. Conflictos, referencias obsoletas y estados YAML ambiguos bloquean sin contexto parcial. Un snapshot inválido nunca habilita fallback.
- P05/P08 y documentación de ambas Skills sincronizados. Se reutilizan selección, manifiestos, caché, empaquetador y transacciones existentes. Los datos remotos y el motor instalado conservan versiones independientes.
- GitHub Actions ejecuta pruebas, valida la preparación local y ensambla/publica el catálogo. No ejecuta Graphify ni reconstruye el índice. Una política explícita HOLD impide publicación aunque los hashes sean correctos. La retención concurrente de Button se preserva.

## Evidencia y reproducción

Los resultados del cierre están en [evidencia ejecutable](../../../output/verification/graph-first/results.json), las [métricas Button](../../../output/verification/graph-first/metrics.json) y el [log de pruebas](../../../output/verification/graph-first/remote-tests.log). Los estados de esos archivos reflejan las comprobaciones realmente ejecutadas; este informe no sustituye los gates. Los artefactos de verificación están fuera del corpus para no generar un ciclo de hashes.

La suite cubre: consulta Button y enmiendas, variantes/estados/tokens, integridad, cobertura, aislamiento, paths y symlinks, formatos incompatibles, índices ausentes/STALE/alterados, conflictos con YAML quoted y comentarios, límites sin éxito parcial, preservación de puntero, retención de publicación y ejecución ZIP → loader → consulta en procesos sin importar el checkout. La regresión previa del tooling dio 44 pruebas PASS con 9 omisiones declaradas. La revisión independiente detectó y permitió corregir tipos de colecciones, punteros, referencias YAML, localizadores históricos enteros, backticks largos y estados de fallback.

La verificación real usa las dos Skills extraídas en directorios limpios y un transporte local del catálogo preparado: no demuestra publicación remota ni conectividad de GitHub. Verifica el mismo loader que usa GitHub. No acredita QA visual de una pantalla ni modifica componentes web. El validador oficial quick_validate no pudo ejecutarse por PyYAML ausente; las comprobaciones equivalentes de metadatos de Skill se ejecutaron con Ruby/Psych existente, sin instalar dependencias.

Secuencia local (intérprete indicado en `graphify-out/.graphify_python`):

1. `./scripts/ds status --write`; `./scripts/ds graph prepare --run <lote>`; extracción semántica según Graphify; `./scripts/ds graph close --run <lote>` y `./scripts/ds graph check`.
2. `python scripts/ds_consumption.py --prepare`; `python scripts/ds_consumption.py`; `python scripts/ds_remote.py`; `python scripts/ds_remote.py --check`.
3. `./scripts/ds skills sync --bump minor --json`; `./scripts/ds skills check --json`; verificar ambos paquetes en directorios limpios.
4. `python scripts/consumer_graph.py --runtime <runtime> --component BUTTON-001 --intent tokens`. El archivo ejecutado en producción es la copia del runtime instalado.
5. `python scripts/benchmark_consumption.py --runtime <runtime> --output <métricas.json>`.

## Alcance de las métricas y límites

Baseline observado antes del cambio: grafo completo de 49.170.594 bytes. El índice diagnóstico era de unos 299 KB; la cifra certificada se obtiene de results.json. Ninguna Skill descarga el grafo completo. El bundle histórico de documentos sigue descargándose/verificándose: reducir el índice y la lectura de contexto no significa reducir ese bundle.

Las métricas comparan la consulta con la lectura completa de exactamente los mismos documentos; no atribuyen un coste de descubrimiento inventado al control. Se mide también fallback con el índice deshabilitado solo en memoria, cuya cobertura es contrato/enmiendas. Se registran archivos, bytes, nodos, contexto y duración, sin estimar tokens ni atribuir significación estadística a tiempos de una ejecución local.

Se resuelve un salto de referencias explícitas desde contrato/enmiendas, sin recorrer todo el grafo. No se afirma clausura transitiva de dependencias ni detección general de contradicciones de lenguaje natural. El consumidor debe respetar la cobertura declarada y confirmar reglas en fuentes. No se promueven drafts ni delegaciones a aprobaciones humanas. Las fuentes concurrentes se verifican por hash antes y después de cada cierre; un plan invalidado se conserva y se prepara otro.

`user_audit: NOT_REQUIRED`; `human_review_policy: OPTIONAL_NON_BLOCKING` para este tooling. La política HOLD específica de Button conserva su alcance independiente. No se requiere una decisión adicional para los cambios locales; publicar ese contenido queda sujeto a su autorización explícita.
