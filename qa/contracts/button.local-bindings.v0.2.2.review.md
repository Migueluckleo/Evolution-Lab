# QA documental · AMD-BUTTON-LOCAL-BINDINGS-001 · 0.2.2

Fecha: 2026-10-05. Resultado: PASS para el alcance de sustitución de bindings. No equivale a aprobación humana ni a QA de implementación.

Contrato: [enmienda](../../specs/components/button.local-bindings.amendment.v0.2.2.md).
Datos: inventario SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474, sin edición.

- DOC-01–06 PASS: enmienda acotada, identidad/versiones y sustitución exacta de REQ/AC-BTN-004; no nuevo contrato paralelo ni intención de producto inventada.
- DOC-07–10/18 PASS: nueve tokens del JSON localizados por ID/colección; tipo, scope, description, primitiva de alias y valor local comparados. 36 resoluciones por modo. Roles adecuados a gap/padding, esquinas, grosor y tipografía.
- DOC-11–14 PASS: se conservan API, variantes, fuentes y restricciones; aceptación por readback y regresión. No implementa web ni modifica fuentes históricas.
- DOC-15–17 PASS: auditoría PENDING; delegación no APPROVED. Página Buttons única 0:1 confirmada, set26:81.
- SLOT-REV-01/02 y SLOT-QA-01 PASS: NOT_APPLICABLE por anatomía fija; texto/Boolean/swap no requieren lista variable.
- Diferencia explícita: los tokens externos Regular/Manrope y los locales regular/manrope difieren en capitalización. Se exige comprobar misma fuente renderizada y métricas; no se declara igualdad literal.

Fuentes leídas: contratos Button0.1.0/0.2.0, enmiendas de página/semántica0.2.1, contrato transversal, P02–P06 y P-SLOTS; preflight vivo, mapa JSON/local y snapshots de consumidores. La inspección distingue Sidebar/Icon Buttons de consumidores de Buttons.

Habilita DELEGATED_FOR_BUILD bajo la decisión de trazabilidad y solicitud de continuar el pendiente confirmado. Implementación debe validarse separadamente; no nueva aprobación humana.
