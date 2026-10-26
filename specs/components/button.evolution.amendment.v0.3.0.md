---
amendment_id: AMD-BUTTON-EVOLUTION-001
applies_to: BUTTON-001
base_contract_version: 0.2.0
version: 0.3.0
status: DELEGATED_FOR_BUILD
user_audit: NOT_REQUIRED
human_review_policy: OPTIONAL_NON_BLOCKING
last_updated: 2026-10-26
operation: UPDATE
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
target_page: Buttons
target_page_id: "0:1"
target_set_id: "26:81"
slot_applicability: NOT_APPLICABLE
data_ref: specs/tokens/ai-design-system.button-danger.v0.1.0.json
publication_policy: AUTHORIZED_BY_USER
publication_decision: registry/DEC-GIT-PUBLICATION-001.md
---

# Button · ampliación 0.3.0: destructivo, carga y foco separado

## Autoridad, alcance y versionado

EXPLICIT: el usuario solicita incorporar el tipo destructivo, el elemento de carga y la nueva configuración de focus ring para todos los tamaños y estados correspondientes, conservando los botones existentes. Pide documentar la ampliación antes de agregar las variantes en AI Design System y no publicar en Git hasta su revisión. La fuente de recopilación permanece de solo lectura.

Esta enmienda amplía [BUTTON-001 0.2.0](button.contract.v0.2.0.md), sus requisitos técnicos heredados de [0.1.0](button.contract.md) y sus enmiendas de [bindings locales](button.local-bindings.amendment.v0.2.2.md), [scope semántico](button.semantic-scope-amendment.v0.2.1.md), [color](six-family-color.amendment.v0.1.0.md) y [tipografía](button.typography.amendment.v0.1.0.md). Sustituye únicamente la matriz cerrada de cuatro tipos/cinco estados, la ausencia de patrón destructivo/carga y la receta de foco pegado al borde. Conserva las demás reglas, identidades, defaults, tamaños, variantes previas y estilos tipográficos. Minor 0.3.0 expresa ampliación compatible de la API; no reescribe documentos históricos ni simula aprobación humana.

Destino UPDATE: página Buttons 0:1, set button 26:81. No crear otra biblioteca, otra página de Buttons ni copiar principales desde la fuente. La revisión humana solicitada es condición para publicar en Git; no impide la implementación y QA locales/Figma pedidos ahora. No hacer commit, push ni publicación de biblioteca en este lote.

## Fuentes, diferencias y decisiones de adaptación

- Fuente indicada: [Frame 6, 10:4046](https://www.figma.com/design/EGUrRbbjSizruuBL4XFTfT/Untitled?node-id=10-4046), con destructivo 8:2748, cargas 8:2752/9:2802/9:2810/9:2806 y foco 10:4009/10:4031/10:4030.
- [Evidencia del principal relacionado 10:3444](../../sources/figma-snapshots/button-evolution.related-source.2026-10-23.json): 90 combinaciones observadas; amplía evidencia de estados destructivos y tamaños, no reemplaza la muestra indicada.
- [Destino previo](../../sources/figma-snapshots/button-evolution.destination-before.2026-10-23.json) y [60 variantes antes](../../sources/figma-snapshots/button-evolution.all-variants-before.2026-10-23.json).
- [Variables locales y Loader](../../sources/figma-snapshots/button-evolution.tokens-loader.2026-10-23.json). Inventario canónico: [tokens.inventory.json](../../sources/inventories/tokens.inventory.json), SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474.

OBSERVED: la muestra indica Loader a la derecha; el principal relacionado lo ubica a la izquierda. DERIVED bajo la discreción solicitada: prevalece la composición del nodo expresamente compartido, con etiqueta seguida del Loader. No se adopta la tipografía 14 px de medium, el renombrado secondary/medium/pressed, los iconos apagados por defecto ni reglas fiscales y de producto de su Description: el DS conserva default/middle/press, estilos compartidos y defaults anteriores.

OBSERVED: fuente danger default/hover/pressed = #D40000/#9D0000/#680000. Las primitivas locales red/600, red/700 y red/800 coinciden exactamente; diferencia RGB cero. Foco fuente #272FD5 frente a token DS color/focus/ring = #1D21B0: se conserva el token semántico vigente del DS y se cambia solo la configuración geométrica. No se altera globalmente ese token ni se extiende el cambio a otras familias.

## Requisitos verificables y matriz

| ID | MUST / MUST NOT | Comprobación |
|---|---|---|
| REQ-BTN-EVO-01 | Conservar los 60 IDs de variantes, sus nombres, defaults y API existentes. No eliminar botones. | Comparación con snapshot previo; mismo set y página. |
| REQ-BTN-EVO-02 | Agregar type=danger en large/middle/small y default/hover/press/disabled/focus; agregar state=loading para los cinco tipos y tres tamaños. | 90 combinaciones únicas: 60 previas + 15 danger sin carga + 15 loading; sin duplicados. |
| REQ-BTN-EVO-03 | Danger reutiliza anatomía, altura y tipografía de primary del mismo tamaño. Default/focus/loading usan danger/default, hover usa danger/hover, press usa danger/active, disabled usa los roles disabled del DS. | Bindings locales, aliases y valores en los cuatro modos; texto/icono on-brand heredados y disabled correspondiente. |
| REQ-BTN-EVO-04 | Loading presenta la etiqueta editable y un Loader local a la derecha. Oculta los iconos de acción durante carga; los flags de icono no agregan iconos en ese estado. | Instancia consumidora, edición de texto y cambios de variante; Loader sigue vinculado al principal local. |
| REQ-BTN-EVO-05 | Alturas 48/40/32; Loader 24/20/16 respectivamente mediante instancia escalada de Loader Sm (24). On color para primary/danger; Primary para default/text/link, como en la muestra. | Geometría y principal local 378:1804 o 378:1789; escala y subárbol conservados, sin nuevos principales Loader. |
| REQ-BTN-EVO-06 | Focus usa capa absoluta Focus ring sin fill, stroke/md 2 px INSIDE, radius/lg 12 px y color/focus/ring local; x/y -4 y ancho/alto +8, constraints STRETCH. | Separación visible 2 px, lectura real, resize y texto largo; sin recorte. Se quita únicamente el stroke de foco antiguo del root, conservando el borde interno default. |
| REQ-BTN-EVO-07 | Conservar estilos tipográficos completos por rango. Danger hereda label-medium en large/middle y label-small en small; loading hereda el estilo del tipo/tamaño, incluido UNDERLINE de link. | IDs y propiedades resueltas de los 90 textos, sin setters de formato después de asignar estilos. |
| REQ-BTN-EVO-08 | Los botones loading no ejecutan acciones ni navegación en web y comunican aria-busy. Disabled sigue siendo un estado diferente. | Pruebas de activación y teclado; no recolorear loading como disabled. En Figma no inventar eventos remotos ni afirmar bloqueo nativo por apariencia. |
| REQ-BTN-EVO-09 | No modificar variantes ajenas al foco ni principales de iconos/Loader. Las reacciones nuevas de danger deben apuntar al danger del mismo tamaño; loading no hereda navegación de primary. | Snapshot/reacciones y QA de dependientes; no corregir deuda histórica ajena silenciosamente. |
| REQ-BTN-EVO-10 | Registrar evidencias de QA y actualizar consumo web/catálogo/skills localmente. Publicación Git retenida hasta revisión del usuario. | Artefactos, comandos y límites registrados por destino; ningún push ni publicación remota. |

Matriz final: type=primary/default/text/link/danger × size=large/middle/small × state=default/hover/press/disabled/focus/loading. Default técnico del set conserva primary/large/default, texto Default e iconos izquierdo/derecho visibles. Loading es un estado excluyente en Figma; en web conserva el foco mientras está ocupado. Si el consumidor combina disabled y loading, disabled tiene precedencia y no muestra Loader.

## Anatomía, contenido, composición y Slots

P-SLOTS NOT_APPLICABLE: etiqueta única y posiciones fijas de icono o Loader; no se admite cardinalidad variable. Una instancia de Loader y swaps individuales no se presentan como Slots nativos.

Loading mantiene auto layout horizontal y ancho HUG conforme a la muestra; esta ampliación no introduce una regla global de ancho fijo ni truncamiento. Probar etiquetas largas y ancho de instancia. El texto sigue siendo controlado por la pantalla; no imponer automáticamente gerundios, mensajes fiscales, confirmaciones o respuestas remotas. Danger identifica acciones destructivas; la política de confirmación pertenece al producto consumidor.

Los nuevos elementos se agregan al set existente respetando su grid y sus 60 variantes. Una muestra de revisión con instancias puede colocarse a su lado; no será otro set maestro.

## Tokens y tipografía

El [JSON de extensión](../tokens/ai-design-system.button-danger.v0.1.0.json) es la única definición editable de los tres roles nuevos, sus aliases, scopes, codeSyntax y description. No modificar el inventario histórico. Los IDs nuevos se registran en el mapa de implementación después de crearlos.

Roles existentes reutilizados: color/focus/ring (13:71), stroke/md (13:3), radius/lg (13:7); los colores, tipografía, padding, gap e iconos heredados mantienen bindings. El offset geométrico -4 deriva de 2 px de separación + stroke/md; no es un color literal ni un token nuevo.

Estilos lógicos conforme al [catálogo activo](../tokens/ai-design-system.typography.v0.1.2.json): ui-action-label-medium, ui-action-label-small, ui-action-text-medium, ui-action-text-small y sus variantes underline para link. No usar los estilos externos de la muestra ni redefinir recetas.

## QA y estados por destino

QA documental: PASS, 2026-10-23; evidencia en [revisión 0.3.0](../../qa/contracts/button-evolution.v0.3.0.review.md). Delegación técnica por solicitud expresa; no equivale a aprobación visual del usuario.

Antes de construir: verificar fuentes/hash, matriz, aliases, alcance de sustitución, capacidad de escritura, tipografía y revisión P-SLOTS. DRAFT no autoriza construcción; tras QA documental PASS registrar DELEGATED_FOR_BUILD según [DEC-AI-TECHNICAL-CLOSURE-001](../../registry/DEC-AI-TECHNICAL-CLOSURE-001.md).

Después: readback de matriz/IDs/bindings, geometría de 15 focus y 15 loading, prueba de texto y cambio de tipo/tamaño en instancias, revisión visual de todos los tamaños/estados nuevos, contraste documentado por modo, typecheck/build y pruebas funcionales web. Verificar consumidores existentes pertinentes sin confundir compilación con fidelidad o WCAG integral.

## Changelog

| Versión | Fecha | Cambio |
|---|---|---|
| 0.3.0 | 2026-10-23 | Ampliación danger y loading; focus ring separado. Conserva API e identidades anteriores; registra diferencias de la fuente y retiene publicación Git para revisión. |


## Actualización administrativa de publicación · 2026-10-26

La solicitud posterior «Publica en Git», registrada en [DEC-GIT-PUBLICATION-001](../../registry/DEC-GIT-PUBLICATION-001.md), levanta el HOLD de Git descrito en este documento y en REQ-BTN-EVO-10. Se conserva ese texto como antecedente del lote del 2026-10-23. No cambia requisitos de diseño, versión 0.3.0, delegación técnica ni auditoría visual; la publicación de biblioteca Figma sigue fuera del alcance.
