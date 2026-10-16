---
contract_schema: sdd-project/0.2
contract_id: SCROLLBAR-001
name: Scrollbar
type: component
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-24
review_targets: [figma]
figma_page_name: Scrollbars
sources: [SRC-FIGMA-SCROLLBAR-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-SEMANTIC-EXTENSIONS-001, DEC-MIGRATION-MISSING-PRIMITIVE-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/contracts/scrollbar.source.component-contract.yaml, drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-SCROLLBAR-COLORS-001]
user_audit: PENDING
---

# Scrollbar 0.1.0 · candidato de construcción

**Vigencia parcial:** la [enmienda cromática 0.1.1](scrollbar.color-approximation.amendment.v0.1.1.md) sustituye la exigencia de primitiva exacta de la sección 10 y `AC-SB-003` tras la decisión posterior del usuario. La anatomía, variantes y geometría de este contrato siguen vigentes.

## 1. Purpose

Representar visualmente el recorrido de contenido desbordado mediante un thumb y un track transparente. El desplazamiento real y la relación con el contenido quedan fuera de esta biblioteca Figma.

## 2. Contract

Construir en una página propia `Scrollbars` un set público `Scrollbar` y subcomponentes de posición reutilizables. La [fuente](../drafts/contracts/scrollbar.source.component-contract.md) y su [YAML](../drafts/contracts/scrollbar.source.component-contract.yaml) gobiernan la geometría observada; el JSON de destino gobierna las nuevas variables. El nombre de página sigue la familia funcional y la convención plural de las páginas del destino ya verificadas, no un color o estado.

## 3. Anatomy

Cada variante pública contiene un thumb redondeado dentro de un marco transparente de 280 px de longitud. Los subcomponentes separan posición y orientación. No dibujar un track coloreado: los separadores fuente carecen de fill visible. El thumb debe permanecer una forma editable vinculada a variable local, no una imagen.

## 4. Properties

| Propiedad Figma | Tipo | Valores | Procedencia |
|---|---|---|---|
| Orientation | VARIANT | Vertical, Horizontal | eje fuente |
| Thumb Size | VARIANT | 25%, 33%, 50%, 75% | eje fuente; etiquetas conservadas |
| Position, en subcomponentes | VARIANT | 1/4…4/4, 1/3…3/3 o 1/2…2/2 según tamaño | ejes fuente no cartesianos |

La variante pública usa la primera posición por defecto, como en la fuente. No añadir una propiedad continua o de datos que Figma no define.

## 5. Variants

Set público con 2×4 = ocho variantes. Mantener cuatro conjuntos internos del tamaño correspondiente con 8, 6, 4 y 4 variantes de posición/orientación, respectivamente. No fabricar posiciones adicionales para 33%, 50% o 75%.

## 6. Sizes

Vertical 14×280 px; horizontal 280×16 px. Thumb de 6 px de grosor, radio 3 px salvo la segunda posición interna de 75%, que tiene radio 4 px en la fuente. En el set público las longitudes observadas son 70, 90.6667, 136 y 240 px. Los sets internos fuente miden 280 px y tienen longitudes 70, 93.3333, 140 y 248 px. Preservar los tamaños visuales públicos; documentar cualquier ajuste necesario al anidar las partes.

## 7. States

La fuente solo muestra apariencia base. `Orientation`, `Thumb Size` y `Position` no son estados hover/focus/disabled. No inventar estos últimos.

## 8. Behavior

Cero reacciones. Las posiciones son ejemplos discretos; no implementan drag, scroll, cálculo de thumb ni límites de contenido. El rótulo `75%` se conserva como identificador histórico aunque el thumb público mida 240/272 px ≈ 88.24% del recorrido interior. No afirmar que el valor sea un porcentaje calculado del viewport.

## 9. Accessibility

No se demuestra rol `scrollbar`, `aria-valuenow`, teclado, foco, área táctil ni contraste suficiente del thumb en todos los fondos. El componente visual Figma no equivale a un control accesible implementado.

## 10. Design tokens

El color original del thumb es `#C3C6D4`, literal sin binding en la fuente. El inventario aprobado no contiene una primitiva de ese RGB: crear en el destino `color/neutral/350` como primitiva exacta y `color/background/scrollbar/thumb` como alias semántico en los cuatro modos, scope exclusivo `SHAPE_FILL`. No usar un token `text`, `icon` o `border` sobre el rectángulo. El [JSON de extensión](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json) contiene las únicas descripciones editables, tipos, valores y aliases; el [inventario aprobado](../sources/inventories/tokens.inventory.json) conserva intacto el catálogo histórico. No hay tipografía consumidora.

## 11. Content rules

Sin texto ni imagen. Los porcentajes y posiciones son nombres de variante, no contenido visible editable.

## 12. Composition rules

El set público usa instancias de los subcomponentes de posición, preferiblemente locales al mismo archivo. Permitir inspeccionar el thumb en cada posición sin desprender instancias. Si se normaliza la geometría interna horizontal para evitar rotación de 90°, conservar el resultado visual público, los IDs de origen en el registro y el cambio como transformación explícita.

## 13. Responsive behavior

280 px es una muestra fija de la fuente; no hay regla observada para tracks más largos, breakpoints ni relación automática con la altura del contenedor.

## 14. Edge cases

El tamaño llamado `75%` no corresponde a 75% de longitud; es una excepción conocida que se preserva visualmente para no alterar la fuente sin una regla de producto. La segunda posición interna de ese tamaño tiene radio 4 px. Esta inconsistencia se señala para auditoría del equipo y no se generaliza a frontend.

## 15. Forbidden combinations

No crear `Position=4/4` para tamaños 33%, 50% o 75%, ni 3/3 para 50% o 75%. No recolorear el thumb, inventar fondo de track, estados de interacción, porcentajes funcionales o efectos.

## 16. Design ↔ Code mapping

Las variantes Figma solo modelan apariencia. En web se necesitarían longitud visible, longitud total, offset, interacción, foco y atributos ARIA definidos en un contrato de comportamiento separado; no convertir las muestras discretas en una API web por inferencia.

## 17. Acceptance criteria

`AC-SB-001`: página `Scrollbars`, set público de ocho variantes y cuatro sets internos con 22 variantes, sin detach. `AC-SB-002`: geometría y posiciones públicas observadas, con la discrepancia 75% documentada. `AC-SB-003`: 30 thumbs con fill local `color/background/scrollbar/thumb` y scope correcto; variable semántica con cuatro aliases a `color/neutral/350`, RGB exacto, JSON y Figma concordantes. `AC-SB-004`: captura fuente/destino comparable, track transparente y cero reacciones. `AC-SB-005`: IDs, transformaciones, QA, auditoría humana `PENDING` y Figma `UNPUBLISHED` registrados.

## 18. Examples

Ocho variantes públicas muestran dos orientaciones y cuatro longitudes rotuladas. Las posiciones internas son muestras de inicio, intermedios y final.

## 19. Source of truth

Este MD gobierna composición y límites de implementación. El [inventario aprobado](../sources/inventories/tokens.inventory.json) y la [extensión JSON](../drafts/foundations/ai-design-system.scrollbar-colors.v0.1.0.json) gobiernan variables. La [trazabilidad transversal](MIGRATION-TOKEN-TRACEABILITY.contract.md) gobierna verificación de bindings. La descripción antigua de la página solo es evidencia.

## 20. Change management

Una corrección futura del porcentaje 75%, comportamiento continuo, color o tamaño requiere enmienda y revalidación. La migración actual conserva apariencia y expone la inconsistencia en la auditoría por excepciones.

## 21. Changelog

- 0.1.0 delegado: cinco sets, extensión cromática exacta y QA técnico histórico; su parte cromática fue sustituida por la enmienda 0.1.1. Auditoría humana pendiente.
