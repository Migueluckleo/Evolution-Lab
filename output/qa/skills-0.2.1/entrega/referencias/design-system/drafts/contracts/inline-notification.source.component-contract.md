---
contract_schema: figma-component-contract/0.1.0
status: OBSERVED
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_node_id: "2778:10287"
read_only: true
---

# Inline Notification · contrato técnico de la fuente

El [YAML sincronizado](inline-notification.source.component-contract.yaml) conserva IDs y dependencias. Este documento describe la Librería anterior, no el destino.

## Identidad y cobertura

- [Set `Inline Notifications`](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2778-10287), ID `2778:10287`, key `55b0bfd8fb39f8b1d16eee72f95a1b44481062ec`, página `1241:55464` (`❖ Inline Notifications ✅`). Tamaño 650×990; cinco variantes de 602×104. Description y links vacíos.
- Traversal read-only 46/46 nodos: cinco componentes, diez instancias de iconos, diez textos y vectores internos; 23 variables únicas, cero estilos nombrados y cero reacciones. Captura 650×990 inspeccionada.

## Ejes, propiedades y estructura

Un eje `type` con default `light` y valores `light`, `success`, `danger`, `warning`, `info`. IDs respectivos `2778:10286`, `2778:10285`, `2778:10283`, `2778:10284`, `2778:10282`. Cada variante es horizontal 602×104, padding 16 px vertical/24 px horizontal, gap 16 px, radio 8 px, con Content horizontal (icono 24 + columna de título/descripción) y un Close 16 al extremo. El título y la descripción se muestran por defecto; ambos son TEXT editables y BOOLEAN visibles. `show icon` y `show dismiss` son BOOLEAN true para las dos instancias.

Los defaults de ejemplo son `Tittle` —error ortográfico en el origen— y `Lorem Ipsum is simply dummy text of the printing and typesetting industry.\nLorem Ipsum is simply dummy text.`. El título Manrope Regular mide 16 px, line-height 150%; la descripción 14 px, line-height 160% y contiene salto de línea explícito. Su tramo final de 18 caracteres es azul y subrayado, pero `hyperlink=null`: visualmente parece enlace sin destino funcional. No es regla de contenido ni de navegación.

## Color e iconos

Los backgrounds observados son blanco Light, verde pálido Success, rojo pálido Danger, amarillo pálido Warning y azul pálido Info, ligados respectivamente a `color/background/default` y `color/feedback/{positive,danger,warning,information}/bg`. El título usa `color/text/primary`; descripción base `color/text/secondary`; tramo final azul `color/text/brand`.

| Variante | Icono 24, key activa | Color del vector |
|---|---|---|
| Light | Confetti `27962798645349b2b27ba120b6bb1db551e4c8a3` | `color/text/primary` (categoría incorrecta para vector) |
| Success | CheckCircle `c05dcb9e418a4827e9999640903ed093e850fdc0` | `color/feedback/positive/icon` |
| Danger | XCircle `a553df531f5cbc790fbf9481e2d13c0a39c6d540` | `color/feedback/danger/icon` |
| Warning | Warning `75ba7898c02f2522c78786982ea96e00a557bec0` | `color/feedback/warning/icon` |
| Info | Info `4b8a12b3aa942823e8f1ecea2a3b8af2759cd7cc` | `color/feedback/information/icon` |

Las cinco variantes usan Close 16 key `ad6c943c212c2ceb4f59e3b435e6781f43657387`, cuyo vector también toma `color/text/primary` en lugar de rol `icon`. Son instancias Phosphor remotas activas; no hay INSTANCE_SWAP expuesto en el set. La visibilidad sí está conectada por Boolean.

## Tokens y anomalías

Las 23 variables utilizadas incluyen cinco backgrounds, cinco colores de icono/feedback más texto primary/secondary/brand, tamaño tipográfico, familia, spacing, radio, tamaño de iconos y un stroke lateral de la fuente. El YAML conserva IDs, scopes y consumidores. Figma muestra el padding de 16/24 ligado a variables `spacing/lg`/`spacing/xl`, y los iconos 24/16 a dependencias remotas. El token remoto `stroke/stroke-focus ring` está ligado a strokeLeftWeight de un componente sin stroke visible; no define un estado Focus funcional.

Hay dos anomalías que el destino no debe copiar silenciosamente: iconos Light/Close con rol de texto y un tramo de descripción que simula link sin URL. `Tittle` es contenido de ejemplo, no nombre de propiedad prescriptivo.

## Interacciones, accesibilidad y límites

No hay reacción de cierre ni evidencia de anuncio live-region, persistencia, prioridad, duración, foco, teclado o interacción del tramo subrayado. `show dismiss=true` solo muestra un icono; no implementa dismiss. El contraste de cada modo/contexto no se certifica por la captura. Una futura implementación debe decidir si se trata de status, alert o mensaje meramente informativo y cómo se comunica a tecnología asistiva. Las cinco variantes visuales no implican niveles de severidad de producto sin definición.

Evidencias: E001 set, propiedades y IDs; E002 matriz/layout y cinco backgrounds; E003 diez instancias y keys; E004 23 variables usadas; E005 diez textos y segmentos de estilo sin hyperlink; E006 screenshot 650×990. Sin truncamiento de traversal.
