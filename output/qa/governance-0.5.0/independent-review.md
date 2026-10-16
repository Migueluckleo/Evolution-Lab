# Revisión independiente del flujo de cierre técnico · gobernanza 0.5.0

Fecha: 2026-10-16. Revisor: agente independiente `review_governance`, distinto del autor del cambio. Alcance: semántica de autorización, QA y cierre; comparación documental con los backups del lote; instrucciones de ambas skills y sus paquetes. No se modificaron fuentes, contratos ni snapshots durante esta revisión.

Resultado final: **PASS** para los escenarios de gobernanza y la integridad del corte 0.2.3. Revisión humana: `NOT_REQUIRED`; política: `OPTIONAL_NON_BLOCKING`. La observación editorial detectada fue corregida y revalidada.

## Fuentes y procedimiento

- Se consultó primero Graphify con `graphify query "DEC-AI-TECHNICAL-CLOSURE-001 aprobación humana QA delegado PENDING" --budget 1800`. El resultado recuperó antecedentes históricos de delegación/auditoría; fue truncado y no se usó como autoridad de la decisión nueva ni como prueba de vigencia del grafo.
- Se leyó `registry/DEC-AI-TECHNICAL-CLOSURE-001.md`, los 17 cambios enumerados en `changes.json` contrastados mediante diff contra `before/`, y las secciones vigentes relevantes de P03/P06/P07/P08, AGENTS, plantillas y prompt de síntesis.
- Se inspeccionaron los SKILL.md de `skills/contpaqi-figma-screens` y `skills/contpaqi-po-prototypes`, sus referencias de consumo, construcción, conflictos y QA, y sus equivalentes en el release 0.2.2.
- Se comprobaron SHA-256 de cada par before/after, igualdad de las fuentes de skill frente a las carpetas empaquetadas, presencia e igualdad de la decisión y protocolos en ambos snapshots, y bytes de cada archivo de las carpetas frente al ZIP correspondiente.
- Se ejecutó el verificador propio de la skill Figma y una comprobación independiente de todos los hashes, digest común e índices de componentes de ambas skills.

## Escenarios de comportamiento

Estos resultados son pruebas de razonamiento sobre las instrucciones efectivas; no simulan ejecución de Figma ni de una implementación web.

| ID | Entrada o condición | Comportamiento exigido y observado en las instrucciones | Evidencia | Resultado |
|---|---|---|---|---|
| GOV-01 | El usuario pide solo análisis o síntesis; el candidato pasa QA documental. | Entregar análisis/contrato y reporte; no construir ni escribir en Figma o web por la mera delegación. | Decisión, flujo 1 y 3; P03 §12; `prompts/02-SYNTHESIZE-CONTRACT.md`. | PASS |
| GOV-02 | Construcción solicitada, fuentes suficientes, dependencias resueltas, QA documental PASS y destino READY. | Registrar solicitud/alcance y DELEGATED_FOR_BUILD; continuar construcción sin aprobación humana rutinaria. Cerrar solo tras los controles y entregables aplicables. | Decisión, flujo 2–5; P03 §11–12; P04 §1; P06 §3 y §6. | PASS |
| GOV-03 | QA documental o de implementación FAIL, BLOCKED, NOT_RUN o STALE en un requisito obligatorio. | No habilitar ni validar la parte afectada; corregir o registrar límite. La política no convierte el resultado en PASS. | Decisión, estados y límites; P06 §2, §5 y §6; referencias QA de ambas skills. | PASS |
| GOV-04 | Un registro histórico mantiene user_audit: PENDING y el alcance técnico aplicable sí está comprobado. | Conservar la historia; no bloquear solo por la auditoría humana pendiente. No inferir que fue revisado ni sustituir QA faltante. | Decisión, estados; P05 §2; P06 §1; referencias design-system de ambas skills. | PASS |
| GOV-05 | El agente concluye implementación y QA técnico sin decisión humana de aprobación. | Mantener DELEGATED_FOR_BUILD y usar VALIDATED únicamente para la implementación comprobada; no afirmar APPROVED ni aceptación/publicación por silencio. | Decisión, estados; P03 §11; P06 DOC-15 y gate final; ambas SKILL.md. | PASS |
| GOV-06 | Dos fuentes vigentes discrepan o falta una decisión material indispensable. | Registrar CONFLICT/UNRESOLVED y detener solo la parte afectada; continuar lo independiente. No resolver la intención por conveniencia ni ocultarla bajo QA PASS. | Decisión, límites; P03 §10–11; P06 §5; Figma `design-system.md` y `handoff-and-qa.md`; PO `SKILL.md`. | PASS |
| GOV-07 | El usuario comunica un defecto después del cierre. | Registrar versión y alcance, corregir y repetir QA pertinente; conservar el cierre histórico sin presentarlo como garantía absoluta. | Decisión, flujo 6; P05 apertura; P06 §6. | PASS |
| GOV-08 | Se pretende publicar remotamente o modificar otra superficie solo por esta delegación. | La política no amplía por sí sola permisos, alcance ni autorización de publicación. Una solicitud posterior explícita tiene que evaluarse separadamente. | Decisión, límites; P08 §1; límites de ambas SKILL.md. | PASS |

## Contradicciones e interpretación efectiva

No se encontró una instrucción efectiva que exija esperar aprobación humana rutinaria. Persisten frases históricas sobre auditoría posterior y terminología de “aprobado” en P02/P03/P04 y antecedentes; su alcance está explícitamente subordinado por AGENTS, la decisión y la sección de delegación general de P03. Esto preserva la historia sin mantener un bloqueo actual. Las instrucciones para registrar una aprobación humana real siguen siendo válidas cuando esa aprobación exista; no convierten esa vía en requisito para delegación técnica.

La revisión no reclasifica `VALIDATION_PENDING`, fallos de tipografía ni limitaciones de las herramientas como auditoría humana: las skills conservan esos controles técnicos. Los manifiestos declaran que empaquetar no aprueba diseño ni QA de Figma/web.

Se encontró un residuo editorial en `templates/contract-synthesis-report.template.md:43`: la celda “Sí” bajo la nueva columna “Autoridad o delegación aplicable”. Se comunicó al autor; se verificó su corrección a `TODO: referencia de autoridad o delegación`. No era una aprobación ficticia efectiva: era un placeholder de plantilla, subordinado a las instrucciones de no copiar ejemplos. La revisión final comprobó el nuevo corte 0.2.3; se mantiene 0.2.2 como evidencia histórica.

## Evidencia de integridad inicial: 0.2.2

- Los 17 pares de hashes before/after coincidían al iniciar la revisión. Tras la corrección de la plantilla, se detectó y comunicó que el hash after de esa entrada requería actualizarse.
- Las dos carpetas de skill coincidían byte a byte con todos sus archivos fuente editables.
- Ambas copias de la decisión, AGENTS y P02–P08 coincidían con las fuentes vigentes revisadas.
- Ambos snapshots: 2132 archivos verificados, cero errores de hashes, índices o digest. Digest común: `86fa54819c42f7d6d45c959549022e995e6f7e534b0ccab56e0ffb7254a64b32`.
- ZIP Figma: 2142 entradas verificadas contra carpeta. ZIP PO: 2157 entradas verificadas contra carpeta. Sin discrepancias detectadas.

## Evidencia de integridad final: 0.2.3

- `changes.json`: los 17 pares before/after coinciden, incluida la plantilla corregida. No quedan discrepancias de manifiesto en el alcance revisado.
- Ambas skills: 2132 archivos por snapshot, cero discrepancias de SHA-256, digest e índices; versión 0.2.3 y digest común `51e1f612be422d89aa3c93f5591f822fb711dceaf1a9b0e0e9b088f0b1c966e1`.
- Todos los archivos fuente editables de cada skill coinciden con su carpeta de release. La decisión, AGENTS, P02–P08 y la plantilla corregida coinciden con el corpus en ambos paquetes.
- Ambos ZIP coinciden con sus carpetas: Figma 2142 entradas, PO 2157 entradas; cero diferencias. Se ejecutó de nuevo `python3 output/skills/0.2.3/contpaqi-figma-screens/scripts/verify_snapshot.py`: PASS, 2132 archivos y cero errores.
- Comprobación independiente de los dos manifiestos: lectura de cada archivo, SHA-256, recomputación de digest mediante JSON canónico y correspondencia de `references/components.json` con el índice del manifiesto. PASS en ambas skills.

## Límites y cierre del revisor

No se ejecutaron build de producto, navegador, cambios Figma, validación visual ni publicación remota: no son evidencia necesaria para este cambio exclusivamente documental. No se certifica que todos los componentes históricos estén conformes ni que el grafo ya esté CURRENT. El autor debe incorporar este informe al cierre documental/grafo. No quedan hallazgos bloqueantes en este alcance de revisión independiente; el cierre global del lote y cualquier publicación posterior requieren sus propias evidencias. No se requiere revisión humana rutinaria.
