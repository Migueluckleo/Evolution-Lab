# PLAN-ICON-BUTTON-FIGMA-001

- **Operación:** `CREATE` en AI Design System, página exacta `Icon Buttons` ausente en preflight; no se reutiliza Button porque es otra familia con set y matriz distintos. Los Icon Button de Material/Simple externos no usan la matriz ni los tokens locales requeridos.
- **Contrato:** [ICON-BUTTON-001 0.1.0](../contracts/icon-button.contract.v0.1.0.md) `DELEGATED_FOR_BUILD`, QA documental `PASS`, auditoría humana `PENDING`; [YAML de fuente](../contracts/icon-button.source.component-contract.yaml) preserva 30 variantes y 60 instancias.
- **Dependencias verificadas:** dos fondos nuevos en JSON/Figma y QA `PASS`; Dot Count local Large/Medium/Small IDs `155:132`/`155:134`/`155:136`; Bell Phosphor key `ef703d88cfc6792cdd17351c4cc923a019b91855`; picker de Chips con 1512 preferred component sets.
- **P3.a:** crear una página `Icon Buttons`, después leer ID/nombre. No tocar `Buttons` ni `Dots`.
- **P3.b:** construir 30 componentes Style×Size×State, dos instancias por variante, posiciones y dimensiones originales; combinar set y ordenar matriz 3×10.
- **P3.c:** vincular todos los fills/strokes/icones, padding, radio y tamaños. Exponer Icon INSTANCE_SWAP y Show count BOOLEAN. Copiar solo la lista de preferencias del picker Phosphor, no sus variantes.
- **P3.d:** readback de 30 combinaciones, 60 instancias, propiedades, bindings de categorías/scope, cero reacciones, screenshot fuente/destino y estado de publicación. Registrar diferencia: Focus uniforme sin único efecto aislado.
- **Riesgos:** el import por key debe ocurrir dentro de la llamada de construcción; si falla, inspeccionar estado antes de reintentar. Small24 y Count4 son límites de accesibilidad del origen preservados como apariencia, no certificación de producto.
- **Cierre P3/P4:** página `183:160` y set `183:311` construidos; lectura posterior confirmó 30 variantes, 30 Bell, 30 Dot Count, picker con 1512 preferencias, 159/159 paints visibles vinculados, cero incompatibilidades semánticas/scope y capturas 289×960 comparadas. [QA](../../qa/implementations/icon-button.v0.1.0.figma.review.md) `PASS` técnico; auditoría humana pendiente y set sin publicar.
