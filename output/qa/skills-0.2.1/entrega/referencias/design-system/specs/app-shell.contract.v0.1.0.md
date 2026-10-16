# APP-SHELL-001 · App Shell · v0.1.0

Estado: `DELEGATED_FOR_BUILD`. Auditoría humana: `PENDING`. Destino: Figma; web fuera de alcance. Decisión DEC-APP-SHELL-INTEGRATION-001, bajo DEC-LEGACY-MIGRATION-DELEGATION-001. No significa aprobación humana ni publicación de biblioteca.

## 1. Propósito

Contenedor reutilizable de pantalla desktop con Header, Sidebar y contenido sustituible. DERIVED de la composición fuente Breakpoints; el nombre histórico no demuestra reglas responsive.

## 2. Contrato

REQ-AS-01: una página semántica **App Shell** y un componente público **App Shell** en AI Design System, file key `tj3WIBEZDGLVs7MJWKCwgf`. Nombre funcional adoptado por decisión delegada, sin modificar el nombre fuente. No crear variantes Mobile/Tablet ni duplicar Header/Sidebar.

## 3. Anatomía

REQ-AS-02: App Shell → Header + Body; Body → Navigation rail + Content. Navigation rail contiene una instancia Sidebar Collapsed. Content es Slot nativo vacío. Header y Sidebar permanecen instancias vinculadas a sus mains locales.

## 4. Propiedades

REQ-AS-03: propiedad SLOT **Content**, 0..n hijos, vacía por defecto. Exponer las instancias Header y Sidebar para conservar sus propiedades existentes sin duplicarlas. Sidebar mantiene Presentation=Collapsed por defecto; Expanded es configuración heredada del DS, no variante observada en Breakpoints. No inventar estados ni propiedades de navegación de producto.

## 5. Variantes

Una composición pública, sin ComponentSet ni ejes propios. La fuente solo contiene una composición desktop 1440×1024 (OBSERVED). Cambiar el contenido no crea otra variante del shell.

## 6. Tamaños

REQ-AS-04: baseline1440×1024; Header1440×96; Body1440×928; rail104×928 con padding superior0, laterales16 e inferior24; Sidebar72×904; Content1336×928. Geometría contractual literal, no reutilizar spacing como WIDTH_HEIGHT. Sidebar expandido conserva234px de ancho del DS y rail266; contenido restante1174 a1440px.

## 7. Estados

Sin estados globales Default/Disabled/Hover. Estados de controles según sus contratos. No confundir Collapsed/Expanded con breakpoints ni con estados deshabilitados.

## 8. Comportamiento

REQ-AS-05: sustituir root NONE por Auto Layout vertical, Header arriba y Body debajo. Body horizontal sin wrap. Header FILL horizontal y96px de alto; Body FILL ambos ejes; rail HUG horizontal/FILL vertical; Sidebar FIXED ancho/FILL alto; Content FILL ambos ejes. El gap28 del rail fuente tiene un solo hijo: normalizarlo a spacing/none sin efecto visual en esta anatomía. No añadir scroll, rutas, permisos ni transición automática no definidos.

## 9. Accesibilidad

Se heredan las limitaciones de contraste documentadas en Header y Sidebar; no se recolorea para corregirlas. La envoltura no añade texto funcional, iconos ni nuevos pares cromáticos. Semántica web header/nav/main, orden de foco y navegación deben definirse en implementación web futura; no se declara WCAG PASS desde Figma.

## 10. Design tokens

REQ-AS-06: fuente canónica `sources/inventories/tokens.inventory.json`, SHA256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. Aplican MIGRATION-TOKEN-TRACEABILITY y enmienda0.1.2. No crear variables, primitivas, estilos o copias del JSON. Descripciones de tokens únicamente en su JSON.

| Uso nuevo | Token semántico | ID lógico canónico | ID local verificado |
|---|---|---|---|
| Superficie blanca del shell | color/background/default | VariableID:2849:196104 | VariableID:13:35 |
| Separación/padding cero | spacing/none | VariableID:1098:28491 | VariableID:12:18 |
| Padding lateral del rail16 | spacing/lg | VariableID:562:12 | VariableID:12:32 |
| Padding inferior del rail24 | spacing/xl | VariableID:562:13 | VariableID:12:33 |
| Esquinas rectas de wrappers | radius/none | VariableID:559:40 | VariableID:12:39 |

Colección local semantic `VariableCollectionId:6:2`; modos Contable6:0, Administrativo6:1, Servicios6:2, Personas6:3. Roles nuevos de envoltura idénticos en los cuatro modos; heredar modo, no fijarlo al componente. Alias y scopes se verifican contra el JSON, no por igualdad visual. Header/Sidebar conservan todos sus bindings y extensiones documentadas; sus colores de marca responden al modo. Los logos conservan la excepción agnóstica vigente, sin recolorear artwork.

## 11. Reglas de contenido

Content vacío es un estado válido, no un error ni obligación de insertar una tabla. El consumidor puede insertar frames e instancias compatibles, eliminar, reordenar y sustituirlos. El layout interno y el scroll pertenecen al contenido insertado. Cantidad de muestra no limita cardinalidad; no asegurar que cualquier contenido cabe sin desbordar.

## 12. Composición

REQ-AS-07 / P-SLOTS: **REQUIRED** para Content. Mecanismo nativo SLOT con propiedad vinculada, no un frame solo llamado Slot. Header Actions y Sidebar Menu items/Lower options conservan sus Slots existentes y propietarios. No anidar mains ni hacer detach. Referencias: `specs/header.contract.v0.1.0.md`, main518:123; `specs/sidebar.contract.v0.1.0.md`, set619:480, Collapsed619:481/Expanded619:496. No mutar esos principales.

## 13. Responsive

Solo composición desktop flexible. REQ-AS-08: comprobar1280×800 y1440×1024, con contenido0/1/3 y configuración heredada Collapsed/Expanded. Son escenarios de QA, no nuevos breakpoints ni garantía para móvil. Header NO_WRAP requiere espacio suficiente para su contenido según su propio contrato. No inventar mínimo universal.

## 14. Edge cases

Probar inserción/eliminación/reordenación/sustitución/reset de Content desde instancia consumidora; no desde main. Probar propiedades de Header y Sidebar, vínculos y herencia en cuatro temas. Confirmar que el principal sigue vacío y que las ediciones no afectan a otras instancias ni a Header/Sidebar mains.

## 15. Combinaciones prohibidas

Primitivas como fills directos de UI; tokens de texto como fondos; colores nuevos; detach para editar contenido; copiar controles fuente sobre los existentes; fijar modo Contable en el main; pretender comportamiento de aplicación funcional; llamar publicada a una biblioteca que no se publicó.

## 16. Design↔Code

Mapa orientativo AppShell(header, sidebar, children); no define API React ni autoriza frontend. El agente consumidor debe leer este contrato, los contratos Header/Sidebar, el de cada contenido y sus datos canónicos. No tomar el snapshot histórico ni el grafo como norma.

## 17. Criterios de aceptación

REQ-AS-09: lectura independiente y captura final; comprobar geometría exacta de envoltura baseline, Slots editables en consumidor, props heredadas y variables locales por modo. Las diferencias de decimales de assets se rigen por Header, no se escala artwork. QA documental antes de escribir; QA técnico después. Promoción a specs solo tras PASS técnico aplicable; humana PENDING.

## 18. Ejemplos

Baseline vacío con navegación colapsada. Instancia con1/3 bloques de contenido y Header/Sidebar configurados por sus propiedades. Los ejemplos no crean variantes públicas adicionales ni contenido predeterminado obligatorio.

## 19. Source of truth

Implementación técnica VALIDATED al2026-10-06: página737:303, main737:304, Slot737:447, propiedad Content#737:1. QA documental y técnico PASS; este contrato se promueve a specs bajo DEC-MIGRATION-SPECS-AUDIT-001. Auditoría humana PENDING; biblioteca no publicada por esta tarea. Evidencias en `qa/implementations/app-shell.v0.1.0.*` y ledger `implementations/figma/app-shell.v0.1.0.state.json`.

Reglas: este contrato. Tokens: inventario y extensiones ya citadas por Header/Sidebar. Evidencia: `sources/figma-snapshots/app-shell.source.v0.1.0.json` (fuente completa recorrida148nodos, propiedades propias y dos dependencias directas); `implementations/figma/app-shell.v0.1.0.preflight.json` (destino y mapa local). Fuente `9zs5RMR8LB5wHjW9Bd59BA`, `8284:12565`, key `bb5d4674e276ae713e7638f00103c4d8e1cdb59c`; página2798:22643. El contrato Anticipa de pantallas sigue DRAFT; no se aprueba por esta incorporación.

## 20. Gestión de cambios

REQ-AS-10: reutilizar el DS vigente prevalece sobre copiar internals históricos: Header mantiene su release y corrección RFC documentados, Sidebar su control superior56px frente a64px histórico. El marco externo permanece fiel. Estas diferencias de dependencia se declaran, no se ocultan como igualdad pixel a pixel de toda la fuente. No cambia ningún contrato hijo. Ajustes futuros directamente en specs con versión/enmienda y QA afectado; publicación documental ≠ publicación de biblioteca.

## 21. Changelog

2026-10-06 ·0.1.0· Incorporación solicitada del shell histórico con variables canónicas, dependencias DS reutilizadas, Slot nativo vacío y Auto Layout. Sin nuevas variables ni variantes responsive.
