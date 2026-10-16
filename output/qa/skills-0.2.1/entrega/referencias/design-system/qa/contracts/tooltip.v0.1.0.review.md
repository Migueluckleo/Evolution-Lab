# QA-TOOLTIP-001 · revisión documental 0.1.0

```yaml
qa_id: QA-TOOLTIP-001
review_type: CONTRACT_REVIEW
contract_ref: TOOLTIP-001
contract_version: 0.1.0
candidate_digest_sha256: be1b92f6026cc2825a5bdbc105718c2b9dffbc097a5da39a8cc84745f00d4359
evidence_model_digest_sha256: 0e091b8057c012d012668d01bdc152cf920faa85ae27265fb5a82df374918d2d
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
target: figma
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

## Controles documentales

| Control | Resultado | Evidencia o límite |
|---|---|---|
| DOC-01 | PASS | Set reutilizable `Tooltip` leído como COMPONENT_SET; contrato de componente, no de tokens. |
| DOC-02 | PASS | YAML parseable, 21 secciones numeradas de MD, tablas y bloque de anatomía cerrados. |
| DOC-03 | PASS | ID, versión, Figma fuente, nodo, página, destino previsto y dependencias identificados; owner desconocido se conserva `null`. |
| DOC-04 | PASS | Ocho requisitos verificables con procedencia y criterios AC-TTIP-001–008. |
| DOC-05 | PASS | Se separan lectura directa, decisiones delegadas de mapeo y comportamiento no definido. |
| DOC-06 | PASS | No se importaron variantes ni valores de la plantilla Button. |
| DOC-07 | PASS | JSON aprobado sin cambio de bytes; 12 variables fuente resueltas y nombres destino encontrados por ID local. |
| DOC-08 | PASS | El JSON conserva la única `description` canónica; el contrato referencia roles sin duplicar catálogo editable. |
| DOC-09 | PASS | Cuatro variantes Align observadas, sin eje State/Size inventado; propiedad TEXT conectada a las cuatro etiquetas fuente. |
| DOC-10 | PASS | Padding 4/8/12, gap 0/24 y radio 8 mapeados a tokens locales existentes. Interlineado 160%→24 y tracking −2%→tight se declaran normalizaciones, no equivalencias exactas. |
| DOC-11 | PASS | Defaults Right y `Tooltips label` consistentes con fuente; no hay icon-only ni nullable inventados. |
| DOC-12 | PASS | Figma visual separado de trigger, teclado, acceso y frontend, que permanecen sin contrato. |
| DOC-13 | PASS | Ocho AC enlazan uno a uno con REQ-TTIP-001–008 y piden lectura posterior. |
| DOC-14 | PASS | Fuente Figma y JSON no se modificaron; las dos sombras se conservan como literales observados por ausencia de categoría tokenizada. |
| DOC-15 | PASS | Estado DRAFT del candidato; decisión delegada permite fase posterior sin afirmar aprobación humana. |
| DOC-16 | PASS | Comportamiento y accesibilidad funcional fuera de alcance Figma; equivalencia exacta de tracking/interlineado no se oculta. |
| DOC-17 | PASS | Página `Tooltips` elegida por función y registrada como decisión delegada; no hay página homónima en el destino leído. |
| DOC-18 | PASS | Tabla distingue tokens fuente y destino, IDs locales y semántica del JSON, incluida corrección on-brand→inverse sin basarse solo en RGB. |

## Resultado y decisiones pendientes de auditoría

La inspección del set abarcó 21/21 nodos, cuatro variantes, cero instancias internas, 12 variables usadas y cero estilos nombrados. El conteo se cotejó con el YAML. La captura del set fue inspeccionada inline; la URL efímera no queda como evidencia local. Se detectó en la página una instancia de documentación con una frase de Modal ajena al Tooltip y se excluyó del contrato.

La normalización de texto blanco a `color/text/inverse`, el interlineado semántico de 24, el tracking `tight` y la preservación literal de sombras son decisiones delegadas **para auditar después**. No hay bloqueo de construcción Figma identificado en esta revisión; la preparación del destino y el QA de implementación son verificaciones separadas. Ninguna de estas decisiones constituye aprobación humana del contrato.
