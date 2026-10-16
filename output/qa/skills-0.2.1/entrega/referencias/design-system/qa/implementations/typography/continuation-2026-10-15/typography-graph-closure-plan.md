# Plan local de cierre Graphify · pendiente de freeze y release

**Solo lectura/plan. No se ejecutaron prepare, AST, extracción, freeze ni close.** Las cifras son provisionales mientras continúan Figma, QA y release.

## Comprobado

- P05 GRAPH-SYNC-01–04 y la referencia operativa mantienen `scripts/ds graph` como entrada de cierre completo; Graphify no aprueba diseños ni transforma BLOCKED/FAIL en VALIDATED.
- Runtime local disponible: Python3.12.13, Graphify0.9.65; configuración y prompt coinciden con el último cierre. No hacen falta instalaciones ni red.
- Los8 outputs del cierre `2026-10-15-typography-final` conservan sus hashes:1867 fuentes,11592 nodos y27352 aristas en ese corte histórico. Los cambios actuales hacen que no sea CURRENT para el corpus nuevo.
- Plan provisional:2007 fuentes,140 nuevas,24 modificadas,0 bajas;65 entradas semánticas (62documentos,3PNG) y99 code/datos cambiados. CadaPNG exige inspección visual real.
- 1843 fuentes previas tienen SHA256 idéntico ahora:912 contribuciones semánticas y931 fuentes code/datos. Es reutilización elegible por manifiesto/grafo previo, no un conteo de hits ejecutados de caché.
- El prompt de extracción no cambió. Los chunks anteriores1 y4–60 conservan todos sus archivos por hash. Normalmente no deberán copiarse: sus fuentes no están en el delta semántico nuevo y el motor preserva su procedencia automáticamente.

## Reutilización y JSON grandes

`graphify-out/runs/2026-10-15-typography-final/reuse-verified-extraction.py` es evidencia de una recuperación concreta; no ejecutarlo sin adaptación: fija ambos nombres de run, exige listas de chunks iguales, copia índices4–60, requiere938fuentescode idénticas y una sola alta. Esas condiciones ya no corresponden al lote nuevo. El AST completo anterior no puede copiarse si incluye archivos cambiados.

El helper `graphify-out/runs/2026-10-15-typography/retry-large-data-json.py` limita en memoria la lectura a8MiB y conserva instalado el extractor. Su hash actual sigue siendo3099dff7f78e044380699138a4087729cca423f423c96fea7ea791fa4c25b599. El método es reutilizable, sus constantes/run y número6 no.

Hay8JSON mayores de1MiB en el plan provisional:6históricos conservanSHA; nuevos mappingv0.1.1 de6400169bytes y consumers79 de1212616bytes. Todos caben en8MiB. Recalcular esta lista tras release: pueden añadirse capturas/entregas. Solo reintentar fallos reales del límite1MiB, parsear JSON entero y exigir clasificación explícita `data json`, sin errores/nodos/aristas. Conservar AST fallido y reporte; no editar fuente ni paquete instalado. No basta con vaciar `failed_sources`.

La clasificación de datos no es extracción semántica ni PASS de diseño. El suplemento estructural debe representar cada archivo grande con SHA, claves/identidad real y referencias; registrar cobertura antes de publicar.

## Secuencia posterior a la señal de freeze

1. Terminar resultados Figma con su estado real, QA79,43enmiendas+transversal, documentación, release/instalación y registrosQA/skills. Congelar las fuentes incluidas y también los registros que indexa el grafo.
2. Ejecutar QA documental y vista derivada antes de preparar. Usar `/tmp` para reportes previos, para no crear por accidente el directorio de un run antes de `prepare`.
3. Crear un nombre único de run. Preparar una sola vez; el plan fija fuentes/configuración/prompt y respalda outputs.
4. Extraer semántica de cada chunk y AST en paralelo. DEEP_MODE=false; prompt íntegro; IDs deterministas de ruta completa; fuentes absolutas exactas; EXTRACTED1 y niveles INFERRED fijos; max3hyperedges. Usage UNAVAILABLE, nunca declarar coste0 medido. Validar todos los chunks antes del cierre.
5. Resolver únicamente fallos comprobados de JSON grande con el retry acotado adaptado al run. Comprobar cobertura AST y suplemento; no copiar AST viejo con fuentes modificadas.
6. `close` genera staging, verifica corpus completo, integridad, manifiesto y outputs; revalida todas las fuentes y baseline vivo antes de publicar. Conservar before y no introducir delta-*.json.
7. Ejecutar gate final y smoke queries por rutas exactas nuevas. Comprobar explícitamente79/75histórico,consumo realy103escalados,43enmiendas,restricciones actuales yrelease. CURRENT solo pertenece al grafo/corpus, no acredita Figma.

Comandos de cierre, **todavía no ejecutados**:
```bash
./scripts/ds check --docs-only --report /tmp/typography-final-docs-check.json
./scripts/ds status --write
./scripts/ds graph plan
./scripts/ds graph prepare --run 2026-10-15-typography-consumers-final
# Completar chunks y AST/retry dentro del run, con validación de hashes antes/después.
./scripts/ds graph close --run 2026-10-15-typography-consumers-final
./scripts/ds check
./scripts/ds graph check
```

Confirmar que ese run no exista al ejecutar; es nombre propuesto, no directorio creado. El AST-only oficial no sustituye estos gates. No alterar outputs vivos después de prepare: el gate los compara contra before. El reporte histórico official-update-preservation.json documenta copia/restauración de9outputs, no una licencia para ejecutar update sobre el baseline preparado.

Smoke paths sugeridos: `typography.formatting.amendment.v0.1.1.md`→`ai-design-system.typography.v0.1.1.json`; `TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md`→enmiendas de Button/Table/Select; enmienda porfamilia→mapping/checker→QAfinal. Resolver IDs del grafo real, no suponer nombres.

## Artefactos de esta preparación

- `/tmp/typography-graph-preclose-plan.json`: delta completo leído, sin congelación.
- `/tmp/typography-graph-cache-readiness.json`: runtime, hashes de outputs/extractor y6JSON históricos.
- Este plan: `/tmp/typography-graph-closure-plan.md`.

Ninguna fuente del repositorio ni artefacto Graphify se escribió durante esta preparación.
