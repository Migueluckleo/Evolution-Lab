# Auditoría y preflight · 2026-10-23

Leídos: AGENTS, P02/P03/P05/P06/P07/P08, GRAPH-OPERATIONS, PROJECT-TOOLING, DEC-GRAPH-CONTINUOUS-SYNC-001, skill Graphify y skill-creator; scripts/ds, ds_graph, ds_skills, ds_remote, cargadores y pruebas remotas, workflow publish-catalog.

Existen selección compartida, releases inmutables, hashes de bundle y archivos, caché, detección de enlaces omitidos, manifiestos, empaquetado determinista y cierre estructural/semántico con respaldo. Faltan índice reducido, adaptador y preparación verificable para CI. No se necesita servicio, dependencia nueva ni segundo motor de conocimiento.

Baseline: grafo 49,170,594 bytes, 15,097 nodos, 35,197 relaciones; gate STALE por registry/refactor-backlog.md nuevo. PUBLICATION-STATE.json ausente. Rama codex/graph-first-consumption creada; cambios anteriores preservados. No se interpreta el cierre histórico CURRENT como vigencia actual.

QA documental del contrato candidato: PASS para alcance, autoridad, compatibilidad, estados, límites, aislamiento y trazabilidad de requisitos con la solicitud. Delegación técnica de implementación autorizada por la solicitud y DEC-AI-TECHNICAL-CLOSURE-001; no aprobación humana ficticia. user_audit: NOT_REQUIRED; human_review_policy: OPTIONAL_NON_BLOCKING. QA de implementación aún pendiente.

Implementación incremental: validación común en ambos loaders, un solo adaptador empaquetado, proyección conservadora por campos y evidencia pública; metadatos YAML explícitos incorporados al suplemento estructural existente de Graphify. El parser Ruby mostró timeouts de arranque de 30 s, también registrados en el backlog previo; se amplió su límite a 120 s sin alterar resultados ni desactivar validaciones. Suite remota de 29 pruebas PASS tras el ajuste; corrige los tres hallazgos de la evaluación independiente (tipos, punteros JSON y referencias YAML). La validación final de integración real y cierre del grafo se registrará por separado.

Fuente preservada: `qa/tooling/graph-first/request.txt`, SHA-256 `3555aab62e327b98c743c2ea0e064440f66152afa73cbf829c1fa97008ff4268`. Evidencia interna excluida del catálogo por la regla existente `qa/tooling/**`. No se alteró el adjunto original.
