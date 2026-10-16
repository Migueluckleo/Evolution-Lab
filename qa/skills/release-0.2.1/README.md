# QA de skills0.2.1 · 2026-10-15

**Paquetes e instalación: CURRENT. QA offline: PASS.** Ambas skills comparten2131 fuentes y43 familias. DS SHA-256 `4205fc48bf65ef7f42f3c51f15402d61c7f5e25ae88850f1a50ccd41fb90bc67`; input digest `14696426ec4dc9591a40d0b9fd7a925ad54b570c7f925bcd51a5a1424783ff39`. El [manifiesto resumido](manifest-summary.json) registra hashes y tamaños de ambos ZIP.

El corte incorpora las43 enmiendas de familia, catálogo79 activo0.1.2 y enmienda nativa para103 consumidores. Conserva los3250 rangos directos, los103 IDs locales vacíos observados y su evidencia de principal/cadena/escala. El [QA Figma del DS](../../implementations/typography.v0.1.2.review.md) es `PASS` tipográfico acotado, con el guard no textual perdido de Table explícito; no es validación integral del diseño. Esta prueba de skills no construyó una pantalla Figma ni publica la biblioteca.

| Control | Resultado y evidencia |
|---|---|
| Release | [sync](sync.json) CREATED0.2.1; [check](skills-check.json) CURRENT |
| Integridad y reproducibilidad | [Export](export.json) UNCHANGED; [4300 archivos con bytes ymtime idénticos](export-reproducibility.json), ambos ZIP CRC PASS |
| Snapshot Figma | [2131 fuentes verificadas](figma-snapshot-check.json), cero errores |
| Empaquetador e instalación |13 pruebas unitarias PASS: altas/cambios/bajas, integridad, paths, idempotencia, colisión de versión, preservación de ediciones y rollback; comando `PYTHONPATH=tests python3 -m unittest test_ds_skills.ReleaseTests -v` |
| Handoff | [Nueve regresiones PASS](../../contracts/typography.native-inheritance.v0.1.2.handoff-tests.log); conserva `status` y `result` del reporte nativo con destino nuevo `NOT_RUN` |
| Sintaxis | [Scripts y frontmatter](../../contracts/typography.native-inheritance.v0.1.2.verification.json) PASS |
| Exportador HTML | [Seis pruebas PASS](inline-export-tests.log): data URI/comillas/fragmentos y rechazo de recursos externos/locales sin resolver |
| Build y navegador | [Log](offline.log), [resumen](offline-summary.json) y [captura](capture-final.json): Next/TypeScript y14 estados/viewports reales PASS, cero red/errores/imágenes rotas/textos sin identificar |
| Markdown | [Entrega original completa](replicar-en-figma.md):24 fuentes y hashes cotejados con la skill Figma,10 instancias,124 fragmentos tipográficos identificados |
| Revisión visual | PASS solo para [Media1440×900](demo--open--1440x900.png) y [SideBySide1000×760](demo--side--1000x760.png); sin recortes ni solapamientos observados dentro del diálogo. Las otras12capturas no tuvieron revisión visual manual |
| Revisión independiente MD-only | [PASS](md-forward-test.md):24fuentes,43enmiendas,10identidades,82observaciones y124fragmentos/8estilos; sin leer HTML, PNG ni JSON externo, Figma NOT_RUN |
| Instalación gestionada | [INSTALLED](install.json), [check-installed CURRENT](installed-check.json), ambas0.2.1 y ninguna obsoleta |
| Preservación | [Skills anteriores y ZIP históricos](preservation.json) intactos;1900 y462archivos conservados por digest exacto |

El HTML contiene3741671bytes, SHA-256 `09d2e59e405f6b925cbe9c47159f498762a2046d49c1208be684a26a22783d9e`. Chrome149.0.7827.201 lo abrió movido y renombrado por `file://`, aislado de recursos vecinos y con HTTP(S) bloqueado. Se probaron inicio, Modal Media, SideBySide, cierre, Enter, Escape y entrada controlada en1440×900 y1000×760. La prueba usa Button, InputField, Modal, Avatar y Logos; las43enmiendas están en ambos paquetes. La excepción nativa no se ejercita en esas cinco familias: sus reglas de traspaso y rechazo se probaron en las nueve regresiones sintéticas indicadas.

La [entrega original](../../../output/qa/skills-0.2.1/entrega/replicar-en-figma.md) y el [ZIP completo](../../../output/qa/skills-0.2.1/offline-artifacts.zip) conservan HTML, MD,14capturas y snapshot completo, con enlaces relativos resolubles. El [JSON auxiliar](handoff.json) y el bloque del MD coinciden excepto por la omisión intencional del mapa completo y repetido de CSS variables de cada nodo; jerarquía, props, estados, mediciones, fuentes y tipografía coinciden. No se copió un MD aislado sin sus carpetas.

`typography.status: IDENTIFIED` registra identidad y métricas observadas, no conformidad universal frente a cada receta. El fixture conserva su revisión visual `NOT_RUN` original dentro del handoff; la inspección posterior de dos imágenes se documenta aquí sin reescribir aquella evidencia. Construcción de pantalla Figma con estas skills: **NOT_RUN**. Auditoría humana del DS: **PENDING**.

## Comandos ejecutados

```bash
scripts/ds skills sync --bump patch --json
scripts/ds skills check --json
scripts/ds skills export --json
python3 output/skills/0.2.1/contpaqi-figma-screens/scripts/verify_snapshot.py --skill-root output/skills/0.2.1/contpaqi-figma-screens
node output/skills/0.2.1/contpaqi-po-prototypes/scripts/test-inline-export.mjs
PLAYWRIGHT_CHANNEL=chrome node output/skills/0.2.1/contpaqi-po-prototypes/scripts/verify-offline.mjs "$PWD/output/skills/0.2.1/contpaqi-po-prototypes" "$PWD/implementations/web/node_modules" /tmp/contpaqi-skills-0.2.1-final-offline
scripts/ds skills install --skills-dir /Users/miguel.leo/.codex/skills --json
scripts/ds skills check-installed --skills-dir /Users/miguel.leo/.codex/skills --json
```

Se usó el runtime Node existente y dependencias locales; no se instalaron paquetes ni iniciaron servidores. Chrome y la instalación gestionada en home usaron la escalación autorizada. El destino temporal debe ser nuevo al repetir la prueba. Después del freeze solo se escribieron paquetes, instalación y QA/registros de release excluidos del snapshot. Graphify se cierra por separado; este informe no anticipa su estado.

El [control documental final](docs-check-final.json) pasó1091 JSON/272frontmatter, con21 hallazgos históricos y cuatro advertencias preexistentes. Se conserva un [intento de salida autorreferente](docs-check-self-output-attempt.json): redirigir el JSON del checker a su propia ruta de entrada lo dejó vacío durante esa lectura; el único error fue ese archivo de reporte. Se repitió con salida temporal y copia posterior, sin modificar fuentes ni ocultar fallos de contenido. El [check posterior al QA](check-after-offline.json) confirma paquetes CURRENT.
