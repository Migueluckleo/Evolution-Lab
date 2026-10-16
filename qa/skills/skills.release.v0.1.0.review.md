# Skills de consumo · release 0.1.0 · 2026-10-14

Alcance autorizado: [DEC-DS-SKILLS-001](../../registry/DEC-DS-SKILLS-001.md), [P08](../../protocols/08-SKILLS-AND-RELEASES.md). Se crearon dos nombres nuevos, con fuentes mantenidas en `skills/`, snapshots derivados, ZIP reproducibles e instalación gestionada local. No hubo escritura Figma ni cambio de contratos, tokens o componentes web del DS.

## Resultado por alcance

| Control | Resultado | Evidencia |
|---|---|---|
| Tooling de proyecto y releases | PASS, 35 pruebas | [Log](tooling.2026-10-14.log) |
| Sintaxis y metadata de ambas skills | PASS | [Validación original quick_validate](skill-validation.2026-10-14.log), adaptador YAML Ruby sin instalación |
| Snapshot final | PASS, 1,373 fuentes y 43 familias | [Verificador](snapshot-validation.2026-10-14.log) y [manifiesto resumido](release.manifest.2026-10-14.json) |
| Release e instalación | CURRENT 0.1.0, dos skills | [Paquetes](release-check.2026-10-14.json), [instalación](install.2026-10-14.json), [cotejo instalado](installed-check.2026-10-14.json) |
| Exportación repetida | UNCHANGED, bytes y mtimes de 2,784 archivos preservados | [Export](export.2026-10-14.json) y manifiesto resumido |
| Exportador de assets inline | PASS, seis casos positivos/negativos | [Log](contpaqi-inline-export-tests-20261014.log) |
| Build Next/React/TypeScript/Tailwind y HTML offline | PASS | [Log real](contpaqi-offline-final-v2-20261014.log), [resultados](offline.results.2026-10-14.json) |
| Consumo de prompt por skill Figma | PASS documental, sin ejecución | [Evaluación independiente](figma.forward-test.2026-10-14.md) |
| Consumo de MD solo por skill Figma final | PASS documental y compatibilidad del alcance | [Evaluación independiente](md.forward-test.2026-10-14.md) |
| Pantalla construida en Figma y comparación contra ella | NOT_RUN | No era parte de crear las skills; la validación de instrucciones no acredita QA Figma |
| Skills anteriores y datos canónicos | UNCHANGED | [Hashes de preservación](preservation.2026-10-14.json) |

## Prueba funcional offline

Fixture reproducible mediante `skills/contpaqi-po-prototypes/scripts/verify-offline.mjs`. Se compiló con las versiones fijadas del proyecto y se abrió una copia del HTML renombrada en una carpeta aislada por `file://`, con red HTTP(S) bloqueada y sin servidor. Se verificaron siete estados en 1440×900 y 1000×760: inicial, Media abierto, entrada con texto, SideBySide, cierre, Escape y apertura por teclado.

Las 14 capturas pasaron: 10 instancias con evidencia, cero solicitudes externas/vecinas, cero errores, cero imágenes rotas, cero textos visibles sin identidad y Manrope cargada realmente en cada caso. Los 75 assets del paquete incluyen los utilizados tras abrir un Modal; no dependen de estar presentes en el primer HTML renderizado. Media conserva Title/Content; SideBySide usa Body Slot. Avatar, logo y botón aparecen en ese contenido variable. El atajo M pertenece solo a este fixture local.

Se inspeccionaron visualmente [Media 1440×900](demo--open--1440x900.png) y [SideBySide 1000×760](demo--side--1000x760.png): imágenes y textos presentes, fuente visible, distribución y foco de teclado sin defectos observados en esas capturas. No equivale a cotejar todos los estados de las 43 familias ni a prometer equivalencia universal de rasterizado con Figma.

HTML final: 3,333,483 bytes; SHA-256 `4ea5d2c24c4a96d17c35f04bd0ec34bab2a88cddd1c92192c806c7621aea2fcc`. Markdown: `8bc47bcbb220c768d5aef85c8a1212c2d05148ec34b9f2f8f66186cfe5ab386b`. Entrega completa y fixture conservados en `output/skills-validation/0.1.0/`; el informe compacto enlaza el reporte completo y conserva su hash.

## Cotejo del traspaso

El MD incluye JSON autosuficiente con jerarquía, orden, medidas, texto visible, identidad, props, Slots, fuentes y transiciones. Se corrigieron los hallazgos independientes: evidencia por instancia en vez de PASS global, títulos/textos locales medidos, exclusión de texto oculto, y separación contractual entre Media y SideBySide. Los assets inline embebidos se aceptan; las URLs pendientes o externas se rechazan.

El fixture se generó con el snapshot candidato `6a116f362fa0e135a019dde498261be977287b585a68401ef6b79455c1e73fb1`; el release final usa `05f59b74952cf681ac81049a33c368d49e4fa16656e3dee883424f5650367443`. Las instrucciones y documentación de mantenimiento se finalizaron posteriormente. Se cotejaron los bytes de todos los scripts/starter de ejecución contra el release, y el evaluador comprobó 14/14 fuentes del MD y 32/32 dependencias del manifiesto de tokens contra el snapshot final. Se acredita compatibilidad de lo utilizado, no igualdad de los dos snapshots.

## Cierre y límites

Leídos: AGENTS, P05/P06/P07/P08, skill-creator, Graphify, skills anteriores como referencia, contratos y dependencias consumidas por los fixtures. Cambiados: dos skills nuevas, generador/versionado/instalador, gates y protocolos de mantenimiento; registro y QA. Las dos habilidades anteriores conservan exactamente sus árboles; las 673 eliminaciones previamente preparadas en Git no se alteraron. El inventario canónico mantiene su hash protegido.

El índice derivado se cierra tras este registro en el lote `2026-10-14-ds-skills`; el resultado verificable reside en `graphify-out/ds-closure.json` y en `scripts/ds check`, no en una aprobación implícita de este informe. Los ZIP y las instalaciones no conceden aprobación humana a contratos ni publican una biblioteca. No queda una decisión de usuario necesaria para entregar las skills; las futuras pantallas conservan su propio destino y QA.
