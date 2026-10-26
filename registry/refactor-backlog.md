# Refactor pendiente

## REFACTOR-CONTRACTS-001 · Consolidar contratos MD y separar el histórico

- **Estado:** PENDING · no iniciado.
- **Fecha de registro:** 2026-10-23 (America/Merida).
- **Solicitud:** «Anotalo como tarea de Refactor pendiente».
- **Objetivo:** reducir la fragmentación y el esfuerzo de consulta del DS sin perder requisitos, autoridad documental ni trazabilidad.
- **Alcance de esta solicitud:** registrar el pendiente; la ejecución del refactor queda para un encargo posterior.

Trabajo pendiente:

1. Inventariar contratos, enmiendas, candidatos, extracciones de origen, versiones sustituidas y enlaces históricos; determinar su autoridad y consumidores reales.
2. Revisar referencias desde registros, QA, código, generadores, catálogo y skills antes de proponer retiros o movimientos. Un nombre coincidente no prueba duplicación.
3. Proponer una revisión consolidada por familia que integre únicamente los requisitos vigentes de su base y enmiendas, conservando fuentes, excepciones y alcance de sustitución.
4. Separar claramente documentación vigente e histórico. Archivar o retirar únicamente lo que la auditoría justifique, preservando evidencia única y resolviendo enlaces afectados.
5. Al ejecutar, revalidar el alcance afectado y sincronizar registros, catálogo/skills y Graphify según P03/P05/P06/P08.

**Criterio de cierre futuro:** entrada inequívoca a la norma vigente por familia; ninguna pérdida de requisitos o evidencia necesaria; referencias y consumidores verificados; historial recuperable y QA documentado. Medir el cambio antes de afirmar un ahorro de archivos o tokens.

**Evidencia inicial, no auditoría de eliminación:** Button 0.2.0 conserva [candidato](../drafts/contracts/button.contract.v0.2.0.md) y [contrato aprobado](../specs/components/button.contract.v0.2.0.md); el [archivo histórico de Table](../drafts/contracts/table.contract.v0.1.0.md) es un enlace a su ubicación canónica. No se ha identificado una lista de archivos eliminables.

**Registro de esta anotación:** se consultaron el índice Graphify, los registros disponibles y las reglas de [P05](../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md). Se añadió este pendiente; no se ejecutó la consolidación ni se cambiaron contratos, estados de aprobación o implementaciones. No hay una decisión requerida para conservar el pendiente; hace falta un encargo posterior para ejecutarlo.

**Verificación del registro:** PASS en lectura del ID/estado y existencia de todos los enlaces locales. Sincronización del índice **BLOCKED / STALE**: el lote `2026-10-23-refactor-contracts-pending` se preparó con un único archivo nuevo y extracción semántica; `scripts/ds graph close` se detuvo por vista derivada desactualizada. El intento de regenerarla con `scripts/ds status --write` terminó en timeout de 30 segundos del lector Ruby `scripts/ds_yaml.rb`. Se conserva el grafo previo, sin afirmar CURRENT. Al reintentar, preparar un lote nuevo que incluya esta nota final y sus hashes; no reutilizar el plan anterior como evidencia vigente.
