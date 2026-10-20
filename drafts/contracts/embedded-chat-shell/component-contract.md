# App Shell | Chat embebido · evidencia de Figma

Fuente: https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=1108-3201

Inspección COMPLETE · 2026-10-20T19:17:32.884655+00:00 · **Read-only Figma evidence**. No es un contrato normativo de producto.

## 1. Component Identity

**Observed from Figma:** `App Shell | Chat embebido` · INSTANCE `1108:3201`, página Layout `1108:620`, main App Shell `737:304`. 1440×1024.

## 2. Anatomy

**Derived structure:** App Shell → Header + Body → Navigation rail + Content → Title + fila de Chat Section (izquierda) y Chat Toolbar (derecha). Inventario completo: 340 nodos, incluidos ocultos.

## 3. Dependencies

**Observed from Figma:** 96 instancias, 55 principales (26 locales, 29 remotos), todos resueltos para sus definiciones activas. Las versiones/bibliotecas remotas no están expuestas. Detalle por ID/key en YAML.

## 4. Properties

**Observed from Figma:** Content#737:1 es SLOT. Las props del chat, Composer e historial pertenecen a sus componentes anidados, sin una nueva API del shell.

## 5. Variants

**Observed from Figma:** Chat Section Standby, Toolbar Expanded=true y Sidebar Collapsed. No se demuestra una variante nueva de App Shell.

## 6. States

**Observed from Figma:** bienvenida visible; conversación y aviso Composer ocultos. Active existe en el contrato hijo; no se probó aquí.

## 7. Layout

**Observed from Figma:** Header96; rail104; Content1336×928; cabecera ~52 y separación vertical32; fila1336×844 con Chat Section1072 y Toolbar264. Columna de chat max816. La fila usa SPACE_BETWEEN, itemSpacing32, pero su distancia efectiva es0; no interpretar32 como gutter efectivo.

## 8. Visual Styles

**Observed from Figma:** apariencia conservada; ver captura. Wrappers nuevos con valores sin binding y Toolbar con override Contable. No se certifica normalización canónica.

## 9. Typography

**Observed from Figma:** 47 nodos de texto; 20 estilos usados resueltos. Description y Beta no tienen estilo compartido; Count label requiere verificar herencia nativa. No se corrigen por esta extracción.

## 10. Tokens

**Observed from Figma:** 98 variables usadas (68 locales/30 remotas); valores resueltos en un consumidor real por variable. No constituye prueba de todos los temas.

## 11. Content

**Observed from Figma:** nombre, empresa, RFC, créditos, fechas, conversaciones y sugerencias son muestras. La cantidad visible no limita Slots.

## 12. Interactions

**Observed from Figma:** diez nodos contienen reacciones de prototipo anidadas, incluidos Hover y timeout del personaje. **Requires definition:** envío, búsqueda, nuevo chat, navegación y persistencia.

## 13. Accessibility

**Requires definition:** semántica HTML, foco, teclado y evaluación WCAG. La captura no los acredita.

## 14. External Dependencies

**Observed from Figma:** label BETA, icon-button, Chat Tool Item, Chat History Item y varios iconos referencian principales remotos. Source/library/version: NOT_EXPOSED_BY_FIGMA_MCP.

## 15. Unresolved Information

**Requires definition:** normalización de wrappers/typography, disponibilidad de artwork, comportamiento estrecho, scroll y acciones de producto. YAML ECS-LIMIT-01…04 conserva impacto.

## 16. Implementation Notes

Extracción de solo lectura; no se generó código de producto ni se modificó Figma. La enmienda normativa separada adopta la arquitectura solicitada sin aprobar inconsistencias de la muestra.

## 17. Evidence / Confidence

Confianza MEDIUM: cobertura completa, límites explícitos. [Modelo YAML](component-contract.yaml), [índice fuente](../../../sources/figma-snapshots/embedded-chat-shell.1108-3201.index.2026-10-20.json), [captura](../../../output/qa/embedded-chat-shell-2026-10-20/figma.png).
