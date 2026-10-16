# QA acotado · identidad tipográfica en handoff · 2026-10-15

Estado: `PASS` para captura efectiva y transporte de identidad. Procedencia:
`OBSERVED` en navegador local y `DERIVED` en el Markdown. No acredita conformidad
tipográfica completa, QA Figma, publicación o instalación de las skills.

## Cambio y fuentes

- [capture.mjs](../../skills/contpaqi-po-prototypes/assets/starter/scripts/capture.mjs)
  lee `--ds-type-style-id` mediante `getComputedStyle` en la raíz y en cada
  fragmento de texto visible; conserva sus métricas. Incluye valores y
  placeholders de controles, que no aparecen como nodos de texto del DOM.
- [handoff.mjs](../../skills/contpaqi-po-prototypes/assets/starter/scripts/handoff.mjs)
  conserva los campos aditivos en schema1, coteja IDs con el catálogo canónico y
  añade catálogo/contrato a las fuentes por hash. Elimina el marker de la lista
  genérica de variables CSS para no confundirlo con un token semántico.
- [verify-offline.mjs](../../skills/contpaqi-po-prototypes/scripts/verify-offline.mjs)
  incorpora aserciones de identidad, métricas y fuentes en el Markdown. Su prueba
  completa de14 estados/viewports queda para el siguiente paquete congelado; no
  se declara ejecutada en esta revisión.
- [Referencia de handoff](../../skills/contpaqi-po-prototypes/references/handoff.md)
  documenta IDENTIFIED/PARTIAL/NOT_RUN y la diferencia entre marker observado y
  conformidad de métricas. Se consultó el catálogo de72 estilos y el contrato
  `FOUNDATIONS-TYPOGRAPHY-001`; no se modificaron.

## Comprobación ejecutada

Fixture temporal autónomo, viewport900×600, Chrome headless mediante Playwright,
HTML renombrado/aislado sin red, Manrope real embebido y scripts actuales. El
archivo se capturó y el Markdown se volvió a leer como JSON autosuficiente.

| Caso | Resultado |
|---|---|
| Raíz Heading5Bold y fragmentos CaptionRegular/BodyRegular | IDs efectivos y métricas conservados |
| Valor de input sin nodo de texto DOM | Capturado como `control-value`, con BodyRegular |
| Fragmento hereda BodyRegular pero sobrescribe tamaño a15px | Conserva ID y tamaño15px observado; no afirma conformidad |
| Texto intencionalmente sin marker | ID null y `typography.status: PARTIAL` |
| ID desconocido introducido en evidencia | Handoff rechazado; no sustituido por estilo semejante |
| Informe schema1 previo sin campos nuevos | Compatible; cobertura tipográfica NOT_RUN, no PASS ficticio |
| Markdown pegable sin archivos adicionales | Conserva IDs, métricas por fragmento, estado y hashes del catálogo/contrato |
| Sintaxis de capture/handoff | `node --check` PASS |

La captura de navegación reporta PASS; la cobertura tipográfica del fixture es
PARTIAL deliberadamente por el texto sin marker. `metric_validation` permanece
NOT_PERFORMED: el estilo puede heredarse mientras un descendiente sobrescribe
una métrica. Esta revisión valida la observación y su transporte fiel.

## Evidencia y límites

Ejecución temporal:
`/var/folders/_9/57g2z7357r7ft9bf8dv7nrq994mxwb/T/contpaqi-typography-handoff-f6uehi70`.
El fixture no es un release ni una exportación de skill. Script de comprobación:
`/tmp/verify-typography-handoff.py`. Son rutas temporales; sus hashes identifican
la ejecución y no prometen conservación permanente de esos archivos.

| Artefacto temporal | SHA-256 |
|---|---|
| capture/report.json | ff5900c59de4ae0b043cd40d2719cbff6c9a25175847efc153a905608c72665a |
| entrega/replicar-en-figma.md | 70fec19daf6e1903b987c602bcc99e427ab884d9b1953dc877c4b21650c99da9 |
| entrega/referencias/handoff.json | 84fee1a30ebaf1a934949fc3e0bca4717e58d6f75b9bc7cbd1b1ea2bee2ac04b |

Pendiente del cierre del lote: congelar fuentes, ejecutar la regresión completa
del paquete y actualizar Graphify con el resto del trabajo. No se ejecutó Figma,
no se cambió el JSON canónico y no se exportaron, versionaron ni instalaron skills.
