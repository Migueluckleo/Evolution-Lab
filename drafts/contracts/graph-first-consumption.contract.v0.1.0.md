---
contract_id: TOOLING-GRAPH-CONSUMPTION-001
version: 0.1.0
type: tooling
status: DELEGATED_FOR_BUILD
user_audit: NOT_REQUIRED
human_review_policy: OPTIONAL_NON_BLOCKING
---

# Índice de consumo Graph-First

Fuente EXPLICIT: solicitud del usuario de 2026-10-23 y adjunto «Evolution-Lab | Graph-First Knowledge Consumption». Alcance: herramientas locales, catálogo y motores de las dos skills. No cambia diseño, tokens ni Figma. P-SLOTS: NOT_APPLICABLE; no modifica familias visuales. P07: documentación técnica del consumidor; componentes web sin cambios.

1. El grafo es un índice derivado. Las fuentes originales gobiernan. Exportar solo desde un cierre local CURRENT comprobado por P05; nunca desde STALE. GitHub Actions valida una preparación local y publica, sin extracción AST/semántica ni reconstrucción del índice.
2. Reutilizar selección, identidad de snapshot, hashes, caché y transacción de catálogo existentes. El índice tiene schema_version 1, ds_digest, source_commit (base Git; hashes describen cambios de trabajo), source_graph_sha256, documentos, relaciones y cobertura. No copiar atributos libres del grafo, rutas privadas ni nodos ajenos al catálogo. Identidad pública: ruta permitida y localizador verificado; el ID interno queda en evidencia local, fuera del índice.
3. Relaciones públicas verificables: referencias explícitas entre documentos, secciones de variantes/estados/tokens, punteros JSON a tokens. Las enmiendas aplicables provienen del índice de componentes existente y conservan estado y versión. No deducir vigencia del nombre o fecha. No inferir ausencia de contradicción por validación de hashes.
4. Adaptador compartido de biblioteca estándar, una fuente mantenida y copias generadas idénticas dentro de los paquetes. Entrada v1: intención component/dependencies/evidence/tokens/variants/states, identidad canónica, límite de documentos y bytes. Respuesta v1: status, mode, reason, snapshot, nodes, relations, documents y metrics. Errores tipados: INVALID_QUERY, UNKNOWN_COMPONENT, CONFLICT, COVERAGE_GAP, LIMIT_EXCEEDED, INTEGRITY, INCOMPATIBLE, STALE, MISSING, OBSOLETE_REFERENCE, STATUS_UNRESOLVED. Ausencia o fallo del índice activa lectura selectiva de contrato y enmiendas del snapshot validado, sin presentarla como éxito del grafo. Conflicto explícito bloquea; límites no truncan silenciosamente.
5. Cada nodo conserva fuente, localizador, versión, estado documental y evidencia. Lectura de documentos y hash antes de devolver contexto. Medir archivos, bytes, nodos, duración y bytes de contexto; distinguir descarga del bundle de lectura selectiva del contexto. No prometer reducción del bundle histórico.
6. Preparación local vinculada por hashes al catálogo, a las fuentes operativas del exportador y a la clausura del grafo. Validación CI sin grafo completo: comprobar corte, integridad, esquema, relaciones, cobertura y procedencia con fuentes públicas. Fallos conservan el puntero anterior. No publicación remota en este encargo.
7. QA: consulta Button, enmiendas, conflictos explícitos, cobertura, STALE, alteración, aislamiento, compatibilidad sin índice, límites y empaquetado limpio de ambas skills. Comparar lecturas equivalentes con fallback. Una contradicción semántica no codificada requiere revisión documental; el adaptador no es un árbitro de diseño.

Compatibilidad: motor protocol 1; campo opcional consumption_graph en manifiesto. Motores anteriores ignoran el campo; motores nuevos aceptan releases anteriores con fallback registrado. Schema incompatible del índice no invalida fuentes íntegras; manifiesto/snapshot inválido bloquea sin fallback.
