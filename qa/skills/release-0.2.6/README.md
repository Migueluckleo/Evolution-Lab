# Release 0.2.6 · Conexión, destino y biblioteca Figma

Fecha: 2026-10-16. Solicitud explícita del usuario: cada diseñador conecta su propio Figma MCP; debe indicar URL de destino o pedir un archivo nuevo; nunca escribir en el maestro; reutilizar primero componentes reales del DS y crear nuevos solo cuando no exista cobertura. Estos requisitos aplican a la skill Figma; la de PO conserva independencia de Figma.

## Resultado

- Revisión independiente documental: 14 escenarios PASS. [Informe](mcp-destination-review.md). Sin escritura Figma ni afirmación de prueba end-to-end.
- Validación de SKILL.md PASS mediante quick_validate.py oficial con adaptación temporal del parser YAML a Ruby seguro, porque PyYAML no estaba instalado; no se modificó el validador ni se instalaron dependencias.
- Mismo corte de fuentes para ambas skills; archivos, ZIP e instalación verificados por el generador. Skills check CURRENT y export UNCHANGED; [instalación comprobada](installed-check.json).
- Scripts, starter y componentes sin cambios; build/web/Figma NOT_RUN en este lote documental.
- Versiones 0.2.4 y 0.2.5 fueron cortes intermedios de conexión y destino. Se conservaron inmutables; 0.2.6 incorpora la aclaración final de biblioteca.

## Límites

La compatibilidad efectiva con Genspark requiere una prueba en esa cuenta/cliente. El consumo automático del catálogo remoto aún no está implementado. El cierre Graphify se verifica mediante scripts/ds check y su marcador final; no se infiere CURRENT de este reporte. El intento previo encontró un límite del extractor JSON para diez archivos grandes; existe recuperación acotada con hashes y clasificación upstream, sin alterar fuentes.
