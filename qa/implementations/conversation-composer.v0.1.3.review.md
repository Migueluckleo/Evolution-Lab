# QA · Conversation Composer Slot 0.1.3

2026-10-20. Contrato: [CONVERSATION-COMPOSER-SLOT-001](../../specs/components/conversation.composer-slot.amendment.v0.1.3.md).

IMPLEMENTATION_REVIEW: PASS. Figma y web local VALIDATED para el Slot nuevo. user_audit: NOT_REQUIRED; human_review_policy: OPTIONAL_NON_BLOCKING.

- Slot nativo1103:192, propiedad Notice content#1103:0, principal765:397. [Escritura](conversation-composer.v0.1.3.write.json).
- En instancias vinculadas se comprobaron0/1/3 bloques, inserción, eliminación, reordenación, sustitución, reset y alternancia de Show action sin pérdida de contenido. [Pruebas](conversation-composer.v0.1.3.slots.json).
- Cuatro temas y616/360px, texto largo, crecimiento vertical y estilos por rango. No se impone máximo de producto.
- Vacío visible conserva caja de edición de49px en Figma; no se atribuye colapso automático. showAction=false oculta la región. Web null produce contenido vacío, sin caja artificial.
- [Captura revisada](../../output/qa/conversation-composer-slot-2026-10-20/figma.png): muestra inicial616 y tres bloques360, sin recortes ni invasión del botón.
- [Readback final](conversation-composer.v0.1.3.final.json): principal y muestra originales conservados; Draft/Tools intactos, instancia766:246 vinculada y Slot nuevo propagado; QA temporal1104:416 eliminado.
- Primer intento de QA excedió el límite de respuesta48000 bytes, sin cambios comprometidos según herramienta; se redujo el payload y la ejecución siguiente pasó.
- No se revalida toda Conversation ni se publica biblioteca o GitHub.

## Web y cierre técnico

- `pnpm verify`: generación vigente (43 familias), TypeScript,9/9 pruebas y compilación Next estática PASS.
- `pnpm exec playwright test tests/browser/conversation-composer-slot.spec.ts`:1/1 PASS. undefined/null/tres bloques, reordenación, sustitución, ocultar/mostrar, callback, borrador y envío; cuatro temas por616/360. [Resultado](../../output/qa/conversation-composer-slot-2026-10-20/web-results.json).
- El primer intento encontró un selector ambiguo de la prueba porque InlineNotification también usa role=status. Se precisó el selector al párrafo de resultado; no requirió modificar el componente.
- [Captura web360](../../output/qa/conversation-composer-slot-2026-10-20/web-360.png) revisada: tres InlineNotification de ejemplo con acciones y borrador, sin recortes. Es otra composición del Slot; no se declara igualdad píxel a píxel con la muestra Figma.
- Catálogo, skills y grafo tienen comprobantes separados al cierre P08/P05. No se publicó GitHub ni la biblioteca Figma.
