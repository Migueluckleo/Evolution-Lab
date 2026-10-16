---
contract_schema: figma-component-contract/0.1.0
status: OBSERVED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node_id: "1132:21344"
read_only: true
---

# Avatar · contrato técnico de la fuente

El [YAML sincronizado](avatar.source.component-contract.yaml) conserva los IDs y dependencias. Este documento describe el set anterior; no prescribe aún el destino ni reglas de identidad de producto.

## Identidad y cobertura

- [Set `avatar`](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1132-21344), ID `1132:21344`, key `2df4b15820fade1cc23c83fde049c755286bfdc4`, página `1132:8891` (`❖ Avatar`). Es un COMPONENT_SET de 324×312 en el frame `1132:21310`, sin Description ni links.
- Traversal read-only completo de 49/49 nodos: 12 variantes, 12 frames internos de cara, 16 instancias (12 Dot y cuatro User), cuatro vectores expandidos y cuatro textos. Cero estilos nombrados y cero reacciones. Captura 324×312 inspeccionada.

## Variantes y propiedades observadas

La matriz es `type=Image/Icon/Text × size=small/middle/large/extra-large` (12/12). Defaults observados: Image y extra-large. Tamaños de cara: small 20×20, middle 24×24, large 32×32, extra-large 48×48. Cada variante contiene una cara circular y una instancia Dot activa situada en la esquina inferior derecha. La propiedad BOOLEAN `show badge Indicator` es `true` por defecto y controla visibilidad de las doce instancias.

| Type | Small | Middle | Large | Extra-large |
|---|---|---|---|---|
| Image | `1132:21354` | `1132:21351` | `1132:21345` | `1132:21348` |
| Icon | `1132:21369` | `1132:21365` | `1132:21357` | `1132:21361` |
| Text | `1132:21385` | `1132:21381` | `1132:21373` | `1132:21377` |

`Content` es TEXT con default `JA`, ligado a los cuatro nodos Text. `icon` es INSTANCE_SWAP con User activo y 1512 preferred component sets; estos valores disponibles no son variantes Avatar ni dependencias activas. El swap está ligado a las cuatro instancias User. No se inventaría el catálogo completo.

## Anatomía y apariencia

- Image: cuatro frames circulares con el mismo fill IMAGE, hash `33f6b019db4382817513e4485e94d3a7dd5a6ca2`. La muestra visual es una fotografía; no contiene propiedad de imagen intercambiable expuesta por el set. El source image original es un asset, no un token de color. Los crops se revisaron por captura; la exportación read-only del frame 48×48 produjo PNG de 5103 bytes, apto como muestra visual del destino.
- Icon/Text: la cara usa `color/interactive/primary/default` (#3255f7 en el modo observado), aunque el Avatar no es una acción. Borde blanco `color/border/on-brand`. Icon usa cuatro instancias User Phosphor de 16, 20, 24 y 32 px, con vector blanco `color/icon/on-brand`. Text muestra `JA` en Manrope SemiBold blanco `color/text/on-brand`; font sizes observados small 6, middle 9, large 14 y extra-large 20 px. Solo 14 y 20 tienen equivalentes semánticos directos en el JSON destino; 6/9 son riesgo de legibilidad.
- Dot: los tamaños de instancia son 5, 8, 12 y 16 px para Avatar small/middle/large/extra-large respectivamente. Small redimensiona un Dot Small de 8 a 5 px. Las otras tres corresponden a Dot Small/Medium/Large de la fuente. La instancia conserva el verde de estado activo y borde exterior blanco en la fuente.

## Dependencias y tokens

Las 12 instancias Dot se resuelven al set local [Dot](dot.source.component-contract.md) `1133:31549`; keys activas Small `75cd122976036d9912d025e275f5f1bbc56a43f3`, Medium `59b662c0e72f3d61f4dd9040dec80a5e7d14b225` y Large `a2ef7876aa1f84fc9b13914a89a4b30c664d180d`. Las cuatro User resuelven al componente Phosphor `2828:33431`, key `77a821b72c03fcfbd0ca9b2910c3fb5c98ed210f`; el set de alternativas preferidas es superficial y no se importa como dependencia completa.

Se observaron 18 variables únicas: color para Dot/Avatar/borde/icono/texto, radius/full, stroke/xs/default/active, familia y tamaño/peso de texto, y espacios locales/remotos. El [YAML](avatar.source.component-contract.yaml) preserva cada ID y su consumidor. La categoría `interactive` del fill de Avatar y el rol `feedback/*/icon` heredado dentro de Dot no deben trasladarse a un fill no interactivo del destino. La igualdad RGB no equivale a semántica.

## Interacciones, accesibilidad y límites

No hay reacciones ni evidencia de carga de foto, iniciales calculadas, fallback automático Image→Text/Icon, presencia en tiempo real, acción de click, tooltip, semántica web ni hit target. La propiedad de texto es solo ejemplo editable. El punto activo no debe interpretarse como estado funcional sin contrato de comportamiento. Los tamaños 6/9 px son demasiado pequeños para avalar legibilidad; el destino deberá decidir una normalización explícita.

Evidencias: E001 set y propiedades; E002 12 variantes y 49 nodos; E003 16 instancias con mains y keys; E004 18 variables usadas; E005 screenshot 324×312, image hash y export 48×48; E006 cuatro textos. Sin truncamiento de traversal; preferredValues se contó, no enumeró.
