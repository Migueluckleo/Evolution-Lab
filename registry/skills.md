# Releases de skills del DS

Registro de paquetes derivados según [P08](../protocols/08-SKILLS-AND-RELEASES.md). Integridad, vigencia, instalación y QA por destino se registran por separado.

## 0.1.0 · 2026-10-14

Decisión [DEC-DS-SKILLS-001](DEC-DS-SKILLS-001.md). Nuevas skills `contpaqi-figma-screens` y `contpaqi-po-prototypes`; las dos anteriores se conservaron con hashes idénticos. Fuentes versionables bajo `skills/`; instalación local gestionada en `/Users/miguel.leo/.codex/skills` comprobada CURRENT para ambas.

- Snapshot común: 1,373 fuentes, 43 familias; DS SHA-256 `05f59b74952cf681ac81049a33c368d49e4fa16656e3dee883424f5650367443`.
- Input digest: `72895bf3e0ba82c6fbb29e3d54d61ba497a1cc194d2f14deb490a36ca6099fee`.
- ZIP Figma 0.1.0 (artefacto histórico local; no incluido en esta publicación): 5,119,059 bytes; SHA-256 `6e976e1a6bf705de3c007c33b8adadec2e2b08795ad417763e977a60dce9dbd5`.
- ZIP PO 0.1.0 (artefacto histórico local; no incluido en esta publicación): 5,136,711 bytes; SHA-256 `5a24c01ed8927802ab197a13b76909ccdf1f4f9b0ea725e1479b168c8f5f4b18`.
- [Informe de QA](../qa/skills/skills.release.v0.1.0.review.md) y [manifiesto resumido](../qa/skills/release.manifest.2026-10-14.json).

Ejecutados: `scripts/ds test` (35 PASS); validación de ambas skills; `skills sync`, `check`, `export` (UNCHANGED), `install` y `check-installed` (CURRENT). HTML real sin servidor: build y 14 capturas de estados/viewports PASS, diez instancias verificadas, cero red/errores/textos sin mapear; seis pruebas del exportador PASS. Revisiones independientes del prompt y del MD autosuficiente PASS documentales. Figma real NOT_RUN: no se creó una pantalla en este lote.

Cierre de índice por P05 en `graphify-out/runs/2026-10-14-ds-skills`; comprobar resultado actual mediante `scripts/ds check`. Este registro no cambia aprobación de contratos ni estado de publicación Figma.

## 0.2.0 · 2026-10-15

Ambas skills exportadas e instaladas con estado **CURRENT**. El corte incorpora tipografía centralizada de 75 estilos, evidencia web y referencias explícitas al bloqueo de aplicación de TextStyles en componentes Figma existentes. No afirma que ese consumo global esté validado; una pantalla Figma mediante estas skills no se ejecutó en este cierre.

- Snapshot común: 1,694 fuentes, 43 familias; DS SHA-256 `f3d8dc4b76c8261d02d60cc708b374c0700d7500400057a219f5fdd7c78d4e56`.
- Input digest: `bace1600266365ef7b7f566b10586606b4d9af87710a539ce1ffe5acebce90fd`.
- ZIP Figma 0.2.0 (artefacto histórico local; no incluido en esta publicación): 8,846,449 bytes; SHA-256 `aad4cad6cf1e07b822c37a46c43571300e4aae22e550b57b3c27ddca98101711`.
- ZIP PO 0.2.0 (artefacto histórico local; no incluido en esta publicación): 8,865,778 bytes; SHA-256 `5e1df4fea2997551ada0aa91a4ee6a2885bfa4591614b9b05cba6e2a9e95e038`.
- [QA y comandos](../qa/skills/release-0.2.0/README.md), [resumen de manifiesto](../qa/skills/release-0.2.0/manifest-summary.json) e [instalación comprobada](../qa/skills/release-0.2.0/installed-check.json).

`sync --bump minor` creó 0.2.0; `check` CURRENT y `export` UNCHANGED. Snapshot y sintaxis de ambas skills PASS; seis pruebas del exportador PASS; build y 14 estados/viewports reales por `file://` aislado y sin red PASS. Diez instancias y 124 fragmentos tipográficos viajan en el MD autosuficiente; revisión visual acotada a dos PNG. El handoff conserva el bloqueo Figma como control separado. Las dos skills anteriores, el inventario protegido y las 673 eliminaciones preparadas en Git se conservaron según la evidencia de preservación. Release 0.1.0 permanece intacto.

## 0.2.1 · 2026-10-15

Ambas skills exportadas e instaladas con estado **CURRENT**. El corte incorpora las43enmiendas de familia, catálogo tipográfico79 activo0.1.2 y la enmienda de herencia nativa para103 rangos. Conserva la validación Figma tipográfica de3353rangos resueltos y sus límites, incluido el guard no textual de Table perdido. El QA del DS no valida automáticamente una nueva pantalla creada con las skills; Figma real para el prototipo de esta prueba: `NOT_RUN`.

- Snapshot común:2131fuentes,43familias; DS SHA-256 `4205fc48bf65ef7f42f3c51f15402d61c7f5e25ae88850f1a50ccd41fb90bc67`.
- Input digest: `14696426ec4dc9591a40d0b9fd7a925ad54b570c7f925bcd51a5a1424783ff39`.
- ZIP Figma0.2.1 (artefacto histórico local; no incluido en esta publicación):10843055bytes; SHA-256 `4828c72fa6a27a1cce5f18a6ddb49cf5f3080a754a53f8ac29a1198ee92f60b0`.
- ZIP PO0.2.1 (artefacto histórico local; no incluido en esta publicación):10862513bytes; SHA-256 `8898a26e181c9b2b1ed23fc6da6ca51f234c15e710669d4a832ccd8599c77af1`.
- [QA y comandos](../qa/skills/release-0.2.1/README.md), [manifiesto](../qa/skills/release-0.2.1/manifest-summary.json) e [instalación comprobada](../qa/skills/release-0.2.1/installed-check.json).

`sync --bump patch` creó0.2.1; `check` CURRENT y `export` UNCHANGED preservó4300archivos, bytes ymtimes. Trece pruebas de release/install, nueve de handoff y seis del exportador PASS. Build/TypeScript y14 estados/viewports por `file://` aislado sin red PASS; diez instancias,24fuentes con hashes y124fragmentos identificados en el MD autosuficiente. Se revisaron visualmente dos capturas. Los paquetes anteriores y ambas skills antiguas conservaron sus hashes. La instalación gestionada solo actualizó las dos skills nuevas autorizadas. La [revisión independiente MD-only](../qa/skills/release-0.2.1/md-forward-test.md) pasó usando únicamente el Markdown y el snapshot de la skill Figma, sin ejecutar Figma.

## 0.2.3 · 2026-10-16

Ambas skills sincronizadas, exportadas e instaladas con estado **CURRENT**. Incorporan la política general [DEC-AI-TECHNICAL-CLOSURE-001](DEC-AI-TECHNICAL-CLOSURE-001.md): documentación y QA a cargo de IA, revisión humana opcional y no bloqueante. No se alteran los requisitos técnicos, no se simula aprobación humana ni se revalidan implementaciones históricas.

- 2132 fuentes, 43 familias; mismo digest del DS en ambas skills.
- [QA, límites y comandos](../qa/skills/release-0.2.3/README.md), [manifiesto y SHA de ZIP](../qa/skills/release-0.2.3/manifest-summary.json), [revisión independiente](../qa/skills/release-0.2.3/independent-review.md) e [instalación comprobada](../qa/skills/release-0.2.3/installed-check.json).
- Ocho escenarios documentales PASS; archivos, snapshots y ZIP íntegros. Sin cambios en scripts/starter; Figma y build web no ejecutados en este lote documental.
- El corte 0.2.2 fue intermedio, conservado sin reescritura; 0.2.3 incorpora la corrección editorial detectada en revisión.
- El consumo remoto desde GitHub aún no está implementado.

## 0.2.6 · 2026-10-16

La skill Figma verifica conexión MCP propia, escritura disponible, URL explícita o solicitud de archivo nuevo, protección del maestro por identidad y acceso a componentes reales de la biblioteca. Si falta acceso avisa; no recrea familias existentes. La skill PO permanece independiente de Figma.

[QA y límites](../qa/skills/release-0.2.6/README.md), [revisión independiente de 14 escenarios](../qa/skills/release-0.2.6/mcp-destination-review.md), [manifiesto](../qa/skills/release-0.2.6/manifest-summary.json) e [instalación](../qa/skills/release-0.2.6/installed-check.json). Ambas skills CURRENT; export UNCHANGED. Validación documental, sin ejecución Figma/Genspark en este lote. Consumo remoto pendiente.

## Mantenimiento

Cada alta o cambio documentado del DS debe cerrar P07/P08 con ambas skills sincronizadas y exportadas desde el mismo corte; el gate impide declarar cierre con paquetes obsoletos. Cambios efectivos generan otra versión y preservan releases anteriores. La instalación gestionada protege ediciones ajenas; compartir un ZIP no actualiza automáticamente otras máquinas. Este registro y su QA no se incluyen dentro del snapshot para evitar autorreferencia.

## Consumo remoto solicitado — motor y datos independientes

El usuario exige consultar GitHub en cada nuevo trabajo y recibir ZIP instaladores únicamente locales. P08 sección 6 gobierna `github-live-v1`: el motor se mantiene instalado; `catalog/current.json` anuncia la última publicación de datos verificada. El cargador valida manifiesto y archivos, mantiene un corte por ejecución y consulta de nuevo al iniciar otra. Sin acceso de red no usa silenciosamente datos antiguos. La biblioteca Figma sigue requiriendo acceso real; los specs públicos no sustituyen sus instancias.

La verificación local y los límites de publicación/Genspark se registran en `qa/skills/remote-consumption/`. No se considera consumo remoto comprobado contra GitHub hasta verificar el canal publicado.

## Chat embebido · arquitectura0.1.1 · 2026-10-20

[QA P08](../qa/skills/embedded-chat-shell-2026-10-20.json): catálogo local CURRENT,43 familias; ambas skills conservan motor0.3.3, sync/check/export/check-installed CURRENT, paquetes sin cambios. La enmienda aparece en App Shell, Chat Section, Chat Toolbar y Conversation. Publicación remota y readback se registran aparte en output/qa/embedded-chat-shell-2026-10-20; este registro no anticipa un push ni una ejecución Genspark.
