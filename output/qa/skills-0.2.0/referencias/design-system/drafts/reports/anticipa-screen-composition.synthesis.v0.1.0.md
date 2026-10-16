---
report_schema: sdd-project/0.2
report_type: CONTRACT_SYNTHESIS
report_id: SYN-ANTICIPA-SCREEN-COMPOSITION-001
contract_id: ANTICIPA-SCREEN-COMPOSITION-001
contract_version: 0.1.0
created_at: 2026-10-06
review_status: REVIEWED_WITH_LIMITATIONS
---

# Síntesis · composición de pantallas Anticipa con AI Design System

## 1. Encargo y entregables

USR-ANTICIPA-COMPOSITION-001 solicita un contrato MD que documente layouts y configuración de pantallas/drawers, proponga componentes y consuma los contratos y JSON del DS sin discrepancias. Se entrega el [contrato candidato](../contracts/anticipa-screen-composition.contract.v0.1.0.md) y un [lock derivado](../contracts/anticipa-screen-composition.dependencies.v0.1.0.json), no una implementación.

No se escribió Figma, no se creó frontend, no se modificaron skills, contratos existentes ni tokens. La construcción de estas nuevas composiciones no está autorizada por la delegación histórica de migración. Esta entrega no se promueve automáticamente a specs.

## 2. Fuentes revisadas

| Fuente | Cobertura y autoridad |
|---|---|
| Solicitud actual | EXPLICIT: documentación MD y propuestas; compatibilidad con DS. No aprobación implícita de resultados. |
| SRC-FIGMA-ANTICIPA-LAYOUT-OBSERVATION-001 | Snapshot persistente de la inspección anterior; OBSERVED_NON_NORMATIVE.61 páginas inventariadas,34 estados principales,199 raíces adicionales,19 capturas previas. No se repitió inspección Figma ni se afirmó cobertura total de variables/descendientes. |
| FOUNDATIONS-TOKENS-001 y JSON base | Contrato existente y datos normativos para sus campos. Se verifican270 variables y512 aliases; identidad/tipo/modos/ciclos del inventario, no bindings Figma actuales. |
|30 documentos del lock | Dependencias directas y enmiendas revisadas. Los hashes de bytes son calculados, no copiados de encabezados históricos. Sus estados se conservan; un contrato delegado no recibe aprobación por citarlo. |
| P02/P03/P04/P05/P06 y P-SLOTS | Procedimiento local para ubicación, síntesis, futura construcción, trazabilidad, QA y regiones variables. Solo se ejecuta el alcance documental. |
| Graphify | Consulta de navegación `foundations tokens modal header sidebar table slots layout contracts`; índice derivado ya STALE. Hallazgos confirmados en archivos propietarios. No regeneración. |

Los digests exactos del snapshot, JSON y dependencias están en el lock; los del candidato y entregables en la [verificación](../../qa/contracts/anticipa-screen-composition.v0.1.0.verification.json). No se mantiene aquí un catálogo de valores editable.

## 3. Matriz de evidencia

| Evidencia | Fuente/localizador | Clasificación | Integración / REQ |
|---|---|---|---|
| E01 · shell y patrones | Snapshot `/findings` OBS-01/02; `/layout_structures_and_local_collections/nodes`,19871:20289 | OBSERVED → DERIVED | R01–R06, REQ05. Las medidas no se convierten en breakpoints. |
| E02 · overlays distintos | OBS-03/04/10;17010:7683,17010:7690,18340:6242,18589:12795,19286:42269 | OBSERVED / UNRESOLVED | R07, PROP01, REQ07; cierre/scroll separados por contexto. |
| E03 · alternativas de captura | OBS-05/07/08 | UNRESOLVED | D01/D02, R05/R06, REQ09. No se elige una versión por ubicación. |
| E04 · descargas / flujo | OBS-06/09/11/13 | OBSERVED / UNRESOLVED | D03/D04 y límites de prototipo; REQ09. |
| E05 · colores de destino | JSON `/collections/1/variables`,37 selectores del lock | EXPLICIT existente; elección de consumidor PROPUESTA | REQ03/04/11; tokens por función y scope. No variables Anticipa. |
| E06 · Disabled | INPUT-FIELD-001 + enmienda0.1.1; SEARCH-0010.1.1 | EXPLICIT, alcance propietario | REQ08; Empty/Filled Disabled no cambian a texto activo. |
| E07 · vigencia cromática | SIX-FAMILY-COLOR-001; Warning0.1.1; Button0.2.1/0.2.2 | Regla vigente delegada o aprobada según propietario | REQ01/10; no repetir reglas históricas de oscurecimiento ni bindings externos. |
| E08 · Slots | P-SLOTS; composition-slots0.1.0/0.1.1; Table/Header/Sidebar/Modal/Empty states | Existente en hijos; propuesto en nuevos anfitriones | REQ06; distinguir aplicación, existencia y QA. |
| E09 · tamaños del modal | MODAL-001 §6; fuente18121:9022 | Diferencia de integración, no conflicto entre normas aprobadas | D06; no inventar700 como tamaño DS. |
| E10 · no identidad de marca genérica | JSON surface/brand y background/brand; TABLE-001 §10 | DERIVED desde aliases distintos | Conservar Table; proponer surface/brand solo para nuevas regiones suaves. |

## 4. Transformaciones realizadas

Se agruparon observaciones en ocho recetas conceptuales y cuatro propuestas de reutilización/creación, sin fabricar variantes cartesianas. Se trazaron dependencias a sus MD vigentes y se incorporaron sus enmiendas por campo. Se añadieron configuraciones conceptuales explícitamente distintas de propiedades Figma y API web.

La propuesta visual adapta envolturas a roles existentes, pero no conserva por obligación la paleta interna de Anticipa: la solicitud actual exige consumir AI Design System. No se traslada a este nuevo alcance una obligación de clonación cromática de la migración anterior. Los componentes reutilizados conservan su norma propietaria, incluidas excepciones visuales y limitaciones.

Se generó un lock con paths, hashes SHA-256 y JSON Pointers. No contiene valores, aliases ni description duplicados. Se separaron las decisiones de negocio de las demostraciones y los futuros criterios de implementación de los controles documentales ejecutados.

## 5. Requisitos y adopción

REQ-ASC-01–12 se relacionan uno a uno con AC-01–12 en el MD. Los límites de uso del DS ya tienen autoridad propia; las nuevas composiciones, tipografías de envolturas, propuestas de componentes y políticas funcionales permanecen candidatas. No se registró aprobación de una nueva familia.

## 6. Discrepancias y conflictos

No se identificó en el alcance consultado un conflicto nuevo entre dos normas aprobadas que obligara a modificar el JSON. Sí hay alternativas y omisiones de la fuente, consignadas como D01–D07. Se evita confundirlas con errores corregibles automáticamente.

Se detectó redacción cruzada en Textarea/File Upload0.1.0. No se modificaron esos contratos ni se usaron las cláusulas ajenas para ampliar su API. El nuevo contrato vincula sus matrices/anatomías propias y obliga a detener un uso que dependa de una cláusula ambigua. La ausencia de estado Success en Textarea queda explícita.

## 7. Propuestas no adoptadas

PROP01 Drawer, PROP02 Workspace Panel, PROP03 Conversation y PROP04 Document Preview son propuestas de empaquetado, no comprobación de ausencia global en Figma ni permiso de creación. El preflight futuro debe revisar si hay equivalentes. Shell y Page Header pueden permanecer como recetas, evitando crear componentes sin necesidad.

Tokens propuestos para envolturas, selección de tamaño Modal Large, body desplazable y política de conservación de datos no se presentan como observados o aprobados. Los mecanismos funcionales de chat, documentos y formularios siguen sin definirse.

## 8. Preparación por destino

| Destino | Estado / razón |
|---|---|
| Documento candidato | Entregado y revisado en su alcance; DRAFT. |
| Figma | BLOCKED como contrato integral listo: falta adopción del alcance nuevo y preflight real. D01–D07 se resuelven solo para las recetas afectadas. No se bloquea todo el DS. |
| Web | BLOCKED y fuera de implementación autorizada: eventos, validación, responsive y accesibilidad no están definidos íntegramente. |
| Publicación | No realizada ni autorizada por la solicitud documental. |

## 9. QA documental

[Revisión](../../qa/contracts/anticipa-screen-composition.v0.1.0.review.md) y [verificación local](../../qa/contracts/anticipa-screen-composition.v0.1.0.verification.json). Separan consistencia del DRAFT, enlaces/IDs/tokens y protección de fuentes de cualquier QA Figma o funcional, que no se ejecutó.

## 10. Entrega y continuidad

Entrada única para el agente: el MD candidato; el lock solo facilita reproducibilidad. La próxima decisión consiste en adoptar una receta/propuesta concreta y sus parámetros pendientes antes de P04, no en aprobar nuevamente todos los componentes existentes. Graphify queda STALE para estos artefactos, sin actualización automática.

## 11. Historial

0.1.0 · 2026-10-06: síntesis inicial desde evidencia persistida y normas locales. Se adaptan las guías de contrato Figma/comportamiento al pedido MD y a la autoridad documental SDD del proyecto; no se crea YAML normativo paralelo ni se reescribe la extracción fuente.
