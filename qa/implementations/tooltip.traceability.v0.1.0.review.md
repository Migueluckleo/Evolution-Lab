# QA transversal · Tooltip 0.1.0 · color, tokens y tipografía

**Fecha:** 2026-09-24. **Resultado cromático y de bindings:** `PASS`; **resultado transversal total:** `IN_PROGRESS` por diferencia tipográfica explícita, sin mutación Figma. `user_audit: PENDING`; set `UNPUBLISHED`.

## Fuentes y cobertura

- Contrato delegado [TOOLTIP-001](../../drafts/contracts/tooltip.contract.v0.1.0.md), JSON aprobado [FOUNDATIONS-TOKENS-001](../../sources/inventories/tokens.inventory.json), SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- Readback en la Librería antigua del set `2599:10469`, cuatro variantes Right/Down/Up/Left, y en AI Design System del set `88:122`, mismas cuatro alineaciones. Se inspeccionaron los tres paints visibles de cada variante y las cuatro etiquetas de texto en ambos archivos.

## Cadena cromática comprobada

| Consumidor | Fuente | Destino | Veredicto |
|---|---|---|---|
| Cuerpo y flecha, ocho fills | `#1E293B`, rol fuente `color/background/inverse` | `#1E293B`, rol local `color/background/inverse` `VariableID:13:39`, scopes `FRAME_FILL`/`SHAPE_FILL`, alias a `color/neutral/800` `VariableID:8:100` en cuatro modos | PASS |
| Etiqueta, cuatro fills | `#FFFFFF`, rol fuente `color/text/on-brand` | `#FFFFFF`, rol local `color/text/inverse` `VariableID:13:31`, scope `TEXT_FILL`, alias a `color/neutral/100` `VariableID:8:93` en cuatro modos | PASS: semántica corregida sin alterar color |

Las primitivas locales leídas de vuelta coinciden numéricamente con el JSON aprobado. No hay strokes visibles. Los doce paints de destino están vinculados al rol documentado; no se añadió variable ni se cambió el archivo Figma.

## Tipografía y punto abierto

Las cuatro etiquetas mantienen Manrope Regular, 14 px y los bindings de familia, peso, tamaño, interlineado y tracking que declara el contrato. La fuente usa interlineado 160% de 14 px (aproximadamente 22.4 px) y tracking −2% (aproximadamente −0.28 px); el destino usa el token de 24 px y el token de tracking que Figma resuelve aproximadamente a −0.01 px. La normalización está **documentada y aplicada consistentemente**, pero no es visualmente idéntica. Por la regla de fidelidad reciente se registra como AUD-004 antes de afirmar `PASS` transversal total. No se infiere un token equivalente ni se altera la tipografía sin una decisión de criterio.

Este QA acredita la cadena de color y la coherencia del contrato con los bindings observados, no interacciones de producto, conformidad WCAG ni publicación de biblioteca. El QA técnico original de Tooltip conserva su alcance histórico.
