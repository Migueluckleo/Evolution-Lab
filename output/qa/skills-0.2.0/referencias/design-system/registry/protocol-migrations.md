# Migraciones de protocolos

## Integración 0.2.3 · revisión de Slots · 2026-09-29

Fuente: DEC-SLOTS-REVIEW-001, solicitud explícita del usuario. Nuevo protocolo P-SLOTS0.1.0 enlazado en AGENTS, P03/P04/P05/P06, README y plantilla de componente; versiones operativas/changelog actualizados. Registros de adopción e implementación distinguen Select estático0.1.0 de su revisión Slots pendiente. No se cambian el contrato histórico, sus digests, Figma ni variables.

Consulta Graphify `composition contract`:23nodos/21relaciones, no aporta reglas específicas de Slots; la definición se apoya en la decisión del usuario y protocolos leídos. Se conserva Graphify STALE sin regeneración. Alcance: documentación operativa, no aprobación de implementación. Verificación local: enlaces de la integración, nueve controles únicos, 21secciones de plantilla y parseo del estado JSON; resultados en qa/contracts/slots-protocol.v0.1.0.review.md.

## Integración 0.2.0 — 2026-09-22

**Alcance:** documentación operativa. **Fuente:** `archive/packages/sdd-codex-protocols-v0.2.0.zip` (SHA-256 `96bbb63d31fe055824220f1a5a6ded6db7cee537b1415d05a18475be60022eb1`). El manifiesto original se conserva en `archive/packages/SHA256SUMS-v0.2.0.txt`; sus 17 entradas pasaron `shasum -a 256 -c` antes de fusionar archivos. El manifiesto certifica el paquete recibido, no los archivos activos modificados.

### Respaldo anterior

Ruta: `archive/protocols-pre-0.2.0/2026-09-22-local/`. Los archivos tienen sufijo `.snapshot` para distinguirlos de los protocolos activos.

| Archivo original | SHA-256 de la copia archivada |
|---|---|
| `AGENTS.md` | `322ba0e9259fba8d64fa83b1e5f96c2b33ed9b763125714d16a681703570bee9` |
| `README.md` | `fbe8cb70beab7a2d20de98d113bb0de599babe66e56c6812f376534e8408b670` |
| `protocols/01-ENVIRONMENT-AND-TOOLS.md` | `0ca2679d77212c093537779bffa4cc38308bd0ce871d4cc6c3c03ca84c4c0818` |
| `protocols/02-DOCUMENT-INGESTION-AND-STORAGE.md` | `7922533a8d8611d0b1559bebb950899280aa0245529611b8ea099d5460bb118c` |
| `protocols/03-FIGMA-CONSTRUCTION.md` | `357113a73d4d8ac392f287ffb4218be4e948ae759beed93d3ea6bac4ccd1a1cc` |
| `protocols/04-SELF-DOCUMENTATION-AND-TRACEABILITY.md` | `c82f9013b19e8a470b73639800589c74e1145c90337e0e3d03b4cd6ab025d145` |
| `protocols/05-QA-AND-VALIDATION.md` | `87606af22b97077ae48bcfc61204e268cc1b799ebeae4c645e732e2cd28e653f` |
| `protocols/06-GRAPH-SELF-DOCUMENTATION.md` | `9a891cd6cdbfb9c0f02411d46c935b3ba968ae3eb040f76c71dccf58200acbf8` |

### Estructura activa y cambios

| Origen | Destino activo | Resultado |
|---|---|---|
| P01 anterior | `protocols/01-ENVIRONMENT-AND-TOOLS.md` | Sustituido por 0.2.0; se conserva la instalación local en `registry/environment.md`. |
| P02 anterior | `protocols/02-DOCUMENT-INGESTION-AND-STORAGE.md` | Sustituido por 0.2.0. |
| Nuevo | `protocols/03-CONTRACT-SYNTHESIS.md` | Añadida síntesis y aprobación antes de construir. |
| P03 Figma anterior | `protocols/04-FIGMA-CONSTRUCTION.md` | Renumerado; se conserva el file key `tj3WIBEZDGLVs7MJWKCwgf` y una página por familia. |
| P04 trazabilidad anterior | `protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md` | Renumerado; enlaza las reglas locales del grafo. |
| P05 QA anterior | `protocols/06-QA-AND-VALIDATION.md` | Renumerado; separa QA documental y de implementación. |
| P06 grafo local anterior | `references/GRAPH-OPERATIONS.md` | Reubicado como referencia complementaria, no como séptimo protocolo. |

Se actualizaron `AGENTS.md` y `README.md`. Se añadieron `templates/`, `prompts/`, `references/DOCUMENTATION-SOURCES.md`, `MIGRATION-v0.2.0.md`, `CHANGELOG.md` y `PACKAGE-VERIFICATION.md`. Las rutas activas antiguas P03 Figma, P04 trazabilidad, P05 QA y P06 grafo dejaron de existir; sus bytes siguen recuperables en el respaldo.

### Reglas y configuración local conservadas

- El bloque `## graphify` de `AGENTS.md` es idéntico al archivado: SHA-256 `6a4a2e13159f2d89a9ab83351766e72ab94de06929d80767ac50913e4350e3a5` para ambas copias.
- `.codex/hooks.json` conserva SHA-256 `123313824d5e7a64f4ced412f15cf2161abb16d6a54bead18abd8f7f40e53eca`; `.codex/skills/graphify/SKILL.md` conserva `3898b1042721cad27d6f87ca44f638415a7f763203aefd86b90f9358ffea3a43`.
- No se reemplazó el registro técnico de Graphify. Se añadió `graph_state: STALE` a `registry/environment.md` porque la documentación cambió y esta tarea excluyó la actualización del grafo; `status: READY` sigue describiendo la herramienta verificada.
- La regla local de autodocumentación del grafo se conserva en `references/GRAPH-OPERATIONS.md`, enlazada desde P05. Su ejecución está sujeta al alcance autorizado por el usuario.
- La indicación local de actualizar Graphify tras cambios de código se interpreta dentro del alcance de cada tarea. Se añadió una aclaración antes del bloque intacto en `AGENTS.md`: si el usuario excluye Graphify, se registra `STALE` y no se ejecuta.
- La antigua afirmación de que Markdown siempre prevalece sobre JSON delegado y el conteo 270 como baseline general no se trasladaron como reglas activas; 0.2.0 los sustituye expresamente. Permanecen en los snapshots históricos.

### Digests finales de los protocolos activos

| Archivo | SHA-256 |
|---|---|
| `protocols/01-ENVIRONMENT-AND-TOOLS.md` | `cdb4e0ae450a85da131c75add2bdba12a7236be25c5c0e36ed16684cce9f85bd` |
| `protocols/02-DOCUMENT-INGESTION-AND-STORAGE.md` | `01820f7a0d1828b90b4c119ef632fbd23eee89cf703654afe6cb1ebcc0fcf0a4` |
| `protocols/03-CONTRACT-SYNTHESIS.md` | `aabe427ceb7100cb3638f2dde95243ae99d7b333f1a2a9af254186f9e2943779` |
| `protocols/04-FIGMA-CONSTRUCTION.md` | `28c2aa4d402fd125abafe4892a4d1adab6b47c76e1d485971cac72209dd2687e` |
| `protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md` | `5bb06b7d070007475d633d50f29044bd2c2723b3633af98cbf02cdadae9f303d` |
| `protocols/06-QA-AND-VALIDATION.md` | `70f534c7a247e0ebe759c00cb57e4d1b2e7f6bb9ece7de6e22b2f1aae8766660` |

Otros digests finales: `AGENTS.md` `422192c70c1d9454d0762f48b2f65e3e2b4b305abde5aafd7b8d188a6a40041d`; `README.md` `f5b7531d35c20691d7ded9672364b51735ad0d7cbc582bcab95ee7e11b9d350b`; `references/GRAPH-OPERATIONS.md` `84dcdb77d82cb6f2e22884bf8bd3d4f1e8a2f271a489d03dfe9e229fc7b2675c`.

### Verificación y límites

Se verificaron inventario, hashes de respaldo, seis rutas activas, enlaces locales, numeración, flujo P02 → P03 → P06 documental → aprobación humana → P04 → P06 de implementación, file key de Figma y regla de página por familia. El paquete original pasó su propio manifiesto SHA-256.

No se ejecutaron Graphify, Figma, instalaciones, construcción frontend ni síntesis de contratos reales. No se modificaron datos canónicos JSON. El grafo queda `STALE` hasta una actualización autorizada.
