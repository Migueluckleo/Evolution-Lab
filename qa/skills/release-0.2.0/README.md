# QA de skills 0.2.0 · 2026-10-15

**Paquetes e instalación: CURRENT. QA offline: PASS.** Las dos skills consumen el mismo corte: 1,694 fuentes y 43 familias. DS SHA-256 `f3d8dc4b76c8261d02d60cc708b374c0700d7500400057a219f5fdd7c78d4e56`; input digest `bace1600266365ef7b7f566b10586606b4d9af87710a539ce1ffe5acebce90fd`. El [resumen de manifiesto](manifest-summary.json) conserva tamaños y hashes de ambos ZIP y del catálogo único de 75 estilos.

Este release incorpora el catálogo, consumidores web y evidencia de tipografía; las referencias de ambas skills exigen consultar el [bloqueo Figma vigente](../../implementations/typography/Figma-blocker.md) y la entrada foundation del registro. Sus tres recetas `derivedFrom` se aplican con métricas ya materializadas, sin doble escala. La creación de estilos no acredita consumo global en componentes Figma.

## Comprobaciones ejecutadas

| Control | Resultado | Evidencia |
|---|---|---|
| Generación e integridad | CREATED 0.2.0; CURRENT; exportación repetida UNCHANGED | [sync](sync.json), [check](check-before.json), [export](export.json) |
| Snapshot Figma | PASS, 1,694 archivos verificados | [log](snapshot-validation.log) |
| Sintaxis de las dos skills | PASS con `quick_validate.py` original; parser YAML Ruby Psych, sin instalar dependencias | [log](skill-validation.log) |
| Exportador HTML | 6 PASS: data URI, comillas y fragmento permitidos; remotos, locales sin resolver y mezclas rechazados | [log](inline-export.log) |
| Build y recorrido real offline | PASS, 14 estados/viewports, diez instancias, cero solicitudes HTTP(S), errores, imágenes rotas o textos sin mapear | [log inicial](offline.log), [resumen final](offline-summary.json), [captura final](capture-final.json) |
| Tipografía capturada | Manrope cargada en todos los estados; 124 fragmentos identificados, ocho IDs canónicos y hashes en MD | [handoff completo](handoff.json), [índice del MD autosuficiente original](replicar-en-figma.md) |
| Revisión visual | PASS acotado a Media 1440×900 y SideBySide 1000×760; las otras doce capturas no se revisaron manualmente | [Media](demo--open--1440x900.png), [SideBySide](demo--side--1000x760.png) |
| Instalación gestionada | CURRENT, ambas skills 0.2.0; sin copias obsoletas | [install](install.json), [check-installed](installed-check.json) |
| Preservación | Skills anteriores idénticas a baseline; inventario intacto; 673 eliminaciones preparadas y mismo índice antes/después | [control](preservation.json), [antes de instalación](preservation-before-install.json) |

El HTML de 3,657,587 bytes tiene SHA-256 `c58231acbe67cc05897aab049ebd1b34b92688087f8dedbe50ffcc32b7da0adc`. Se abrió movido y renombrado mediante `file://`, aislado de assets vecinos y con HTTP(S) bloqueado, en Chrome 149.0.7827.201. Se recorrieron inicial, Media, SideBySide, cierre, Enter, Escape y entrada controlada a 1440×900 y 1000×760. El artwork de Modal, Avatar y Logos apareció después de interacción.

El fixture inicial del script conserva [brief](brief.original.json) y [reporte](capture.original.json). Después se completó únicamente el [brief temporal](brief.final.json) con el bloqueo Figma y la revisión visual real; se repitieron captura/handoff para ligar ese brief a la evidencia ([capture](capture-final.log), [handoff](handoff-final.log)). HTML y hashes de las dos capturas revisadas permanecieron idénticos. La fuente del fixture está en [fixture.page.tsx](fixture.page.tsx). El [archivo de artefactos](offline-artifacts.zip) conserva HTML, MD, JSON, 14 PNG y fixture; omite solo la copia duplicada `referencias/design-system`, recuperable del snapshot 0.2.0 con el mismo digest.

## Comandos

Desde la raíz del repositorio, con el runtime Node local en PATH:

```bash
export PATH=/Users/miguel.leo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin:$PATH
scripts/ds skills sync --bump minor --json
scripts/ds skills check --json
scripts/ds skills export --json
python3 output/skills/0.2.0/contpaqi-figma-screens/scripts/verify_snapshot.py
node output/skills/0.2.0/contpaqi-po-prototypes/scripts/test-inline-export.mjs
PLAYWRIGHT_CHANNEL=chrome node output/skills/0.2.0/contpaqi-po-prototypes/scripts/verify-offline.mjs "$PWD/output/skills/0.2.0/contpaqi-po-prototypes" "$PWD/implementations/web/node_modules" /tmp/contpaqi-skills-0.2.0-offline
scripts/ds skills check --json
scripts/ds skills install --skills-dir /Users/miguel.leo/.codex/skills --json
scripts/ds skills check-installed --skills-dir /Users/miguel.leo/.codex/skills --json
```

El directorio temporal de `verify-offline.mjs` debe ser nuevo para una repetición. Tras completar allí el brief se ejecutaron `PLAYWRIGHT_CHANNEL=chrome node scripts/capture.mjs` y `node scripts/handoff.mjs`. Chrome y la instalación en home usaron la escalación autorizada. No se instalaron paquetes, iniciaron servidores ni ejecutaron escrituras Figma.

## Alcance y preservación

`typography.status: IDENTIFIED` acredita IDs presentes y fuentes; no certifica todas las métricas frente a la receta. El QA de 75 recetas web permanece en su [revisión específica](../../implementations/typography/web/revision-75/README.md). Construcción de esta pantalla Figma: **NOT_RUN**. Aplicación estable de estilos a componentes Figma existentes: **BLOCKED**, según su reporte; este cierre no la presenta como validada.

El método de hash de las skills anteriores se reprodujo exactamente: SHA-256 de UTF-8 `json.dumps({ruta_relativa_posix: sha256(bytes)}, sort_keys=True, separators=(',', ':'))`, con `ensure_ascii=True` predeterminado y todos los archivos regulares recursivos. Coinciden los 1,900 archivos de `contpaqi-poc-builder` y 462 de `contpaqi-html-prototype` con el [baseline](../legacy-skills.before.2026-10-14.json). El inventario conserva SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. El conteo histórico de eliminaciones es 673; no existía hash histórico de sus rutas. El hash íntegro de `git diff --cached --name-status -z` sí permaneció idéntico entre inicio y cierre de esta instalación.

Leídos P08, configuración/CLI, referencias de ambas skills, catálogo y bloqueo Figma. Tras el freeze solo se generaron paquetes/instalaciones autorizados y evidencia en `qa/skills/` y `registry/skills.md`, excluidos del snapshot. El [check posterior al QA](check-after-offline.json) acredita fuentes CURRENT. Graphify se cierra por separado con estos archivos finales; este reporte no anticipa su resultado.
