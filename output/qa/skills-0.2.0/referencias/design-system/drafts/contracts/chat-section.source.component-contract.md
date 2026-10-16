# Chat Section · evidencia fuente

Inspección PARTIAL · 2026-10-08 · solo lectura de Figma. Proyección del [YAML normalizado](chat-section.source.component-contract.yaml); no es el contrato normativo del destino.

## 1. Component Identity

Observed from Figma: `Organism | AI Ecosistem | sectionChat`, COMPONENT_SET20355:74859, key bade7cd7895f387b35107ba565fd79ad7a2b0281, [Anticipa](https://www.figma.com/design/zuUq3gcF9T3CLid44bjY6W/Anticipa-Junio2026?node-id=20355-74859). Dos componentes782×775, set1848×807.

## 2. Anatomy

Observed from Figma: standBy contiene BENI, saludo, pregunta, composer y tres sugerencias. active contiene Slot chat (mensaje y texto de lectura) y composer con disclaimer. [Índice completo](../../sources/figma-snapshots/chat-section.index.2026-10-08.json):116 nodos, incluyendo ocultos.

## 3. Dependencies

39 instancias activas agrupadas en18 principales; [índice de bindings](../../sources/figma-snapshots/chat-section.binding-index.2026-10-08.json). Conversation20355:72764/72815 y versión duplicada20355:71068; BENI20355:74823; Chips19784:32787; lectura19871:20904. No se duplican contratos hijos aquí.

## 4. Properties

Observed: state VARIANT, default standBy; chat#588:0 SLOT, mínimos/máximos null. Los textos del padre no están expuestos como propiedades. Definiciones hijas y ocultamiento observado en [dependencias](../../sources/figma-snapshots/chat-section.dependencies.2026-10-08.json).

## 5. Variants

20355:74860 active;20355:74868 standBy. No más variantes del anfitrión.

## 6. States

active/standBy describen composición, no disabled ni garantía de procesamiento. Sugerencias usan State=Selected de otro set y reacción hover a19786:72353.

## 7. Layout

Observed: ambos verticales, padding80 arriba/120 lateral/0 abajo, gap32, columna542. Active Slot FILL, alineado abajo; overflow VERTICAL en anfitrión. StandBy no scroll. Sugerencias WRAP, gaps16; composer y sugerencias separados30. Saludo790px desborda columna542. [Geometría propia](../../sources/figma-snapshots/chat-section.20355-74859.own.2026-10-08.json) conserva valores exactos.

## 8. Visual Styles

Observed: fondo blanco; nombre y BENI #41589B; rasgos #E4E5E6. Sugerencias #EFF3FF, hover #BFCEFE; texto #3255F7. Pinturas fuente y aliases no equivalen a tokens aprobados de destino.

## 9. Typography

Manrope Bold32, interlineado AUTO para saludo; Regular20 AUTO pregunta; mensaje14/20; sugerencias14/16; disclaimer12 AUTO. Saludo mezcla negro y azul; runs preservados. Dos estilos nombrados, recetas parciales.

## 10. Tokens

45 IDs de variables observados con used_by; siete definiciones consultadas y resto sin terminales resueltos. YAML los distingue, no los presenta como inventario canónico. Los tokens de destino se cotejan independientemente.

## 11. Content

Datos de demostración: Bruce Wayne, ingresos/IVA/facturas, pregunta al SAT. No hechos financieros ni capacidades reales. Placeholder de composer; disclaimer oculto en standBy y visible en active.

## 12. Interactions

FIGMA_DEFINED: BENI tiene timeout2s y smart animate0.1s; lectura tiene113 fotogramas, comienza por L, timeout≈0.0616s. [Evidencia](../../sources/figma-snapshots/chat-section.hero.2026-10-08.json) incluye fotograma completo «Leyendo la información...». No se inspeccionó toda la máquina ni se deduce lógica de backend.

## 13. Accessibility

Requires definition: teclado, anuncios, foco, nombres accesibles, contraste funcional de aplicación. No certificación WCAG desde esta fuente.

## 14. External Dependencies

Locales y remotas identificadas en índice; terminales remotos históricos parcialmente sin resolver. No se importan como Foundations.

## 15. Unresolved Information

No límites de mensajes/sugerencias, semántica de vacío, click de sugerencia ni proceso real definidos. Animaciones completas fuera de esta lectura. Identidades116/116 inspeccionadas no significan cobertura total de propiedades.

## 16. Implementation Notes

Derived structure: composition y contenido variable. Evidencia separada del contrato homologado; no prescribe envío ni procesamiento. Conservar IDs fuente; nuevos IDs del destino por separado.

## 17. Evidence / Confidence

Confianza MEDIUM: captura observada, árbol completo, propiedades propias/runs y dependencias activas; cobertura profunda parcial. Fuente no modificada. El YAML y snapshots son evidencia, no aprobación ni norma del destino.
