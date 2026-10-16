# QA-TOOLTIP-FIGMA-001 · Tooltip en AI Design System

```yaml
qa_id: QA-TOOLTIP-FIGMA-001
review_type: IMPLEMENTATION_REVIEW
contract_ref: TOOLTIP-001
contract_version: 0.1.0
contract_digest_sha256: 522b74426f781231dbf0a3ce7daed35909ab8f1358e347efe97e34f454416402
data_digest_sha256: cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474
implementation_ref: IMP-TOOLTIP-FIGMA-001
target: figma
file_key: tj3WIBEZDGLVs7MJWKCwgf
page_id: '85:122'
component_set_id: '88:122'
reviewer: Codex
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
publish_status: UNPUBLISHED
```

## Controles contra el contrato delegado

| AC | Resultado | Lectura del destino |
|---|---|---|
| AC-TTIP-001 | PASS | Una página `Tooltips` `85:122`, set principal `Tooltip` `88:122`; Buttons `0:1` y Chips `67:122` conservan nombre y un nodo superior cada una. |
| AC-TTIP-002 | PASS | Cuatro variantes únicas: Right `87:122`, Down `87:127`, Up `87:132`, Left `87:137`; `Align` default Right. |
| AC-TTIP-003 | PASS | Cada variante tiene Body, Label, Arrow area y vector; ancho FIXED y alto HUG. Orden cuerpo/flecha y transformaciones corresponden a cada dirección; captura del set de 636×130 inspeccionada inline sin recortes o solapamientos aparentes. |
| AC-TTIP-004 | PASS | TEXT `Content#88:0`, default `Tooltips label`, referenciada en las cuatro etiquetas por `characters`. |
| AC-TTIP-005 | PASS | Cuatro fondos y cuatro flechas enlazados a `color/background/inverse` `VariableID:13:39`; cuatro etiquetas a `color/text/inverse` `VariableID:13:31`. |
| AC-TTIP-006 | PASS | Por variante se verificaron familia, estilo, tamaño, interlineado y tracking en etiquetas; cuatro paddings, gap y cuatro radios del cuerpo; paddings y gap del componente; paddings del área de flecha. 52 pares token-modo conservan aliases en la colección semantic local. |
| AC-TTIP-007 | PASS | Dos DROP_SHADOW por variante, con desplazamientos (0,2) y (0,4), radios 4 y 6, spread −2 y alpha 5% y 10%; son literales observados, no tokens inventados. |
| AC-TTIP-008 | PASS | IDs reales, mapa, decisión, diferencia de medidas, readback y QA quedan en el estado y registros; auditoría humana `PENDING`. |

## Integración y límites

- La normalización `line-height: 24 px` y `letter-spacing: −0.01 px` proviene de variables semánticas existentes; la fuente mostraba 160% y −2%. Para conservar la etiqueta en una línea con el tracking del destino, el ancho final es 121×40 en Right/Left y 111×50 en Up/Down, frente a 116×38 y 107×48 en la fuente. Es una diferencia del contrato delegado, no igualdad pixel a pixel.
- El contraste calculado entre los colores finales del cuerpo y texto es 14.63:1 en Contable, Administrativo, Servicios y Personas. Esto no valida asociación con el disparador, foco, teclado o temporización; esos comportamientos no están definidos en el set fuente.
- Auditoría de 23 nodos del set y documentación: cero nombres vacíos, cero duplicados superiores y cero fills/strokes sólidos visibles sin binding de variable. Las sombras son la excepción literal documentada. No se creó ningún token, estilo, página de Foundations ni Code Connect.
- La captura se inspeccionó como imagen inline y su URL efímera no se guardó como artefacto local. La evidencia reproducible principal es la lectura estructural del destino y el mapa de IDs en el [estado](../../implementations/figma/tooltip.v0.1.0.state.json).
- `getPublishStatusAsync()` devolvió `UNPUBLISHED`; construir en el archivo no significa publicar la biblioteca. La auditoría del usuario puede aceptar o pedir revisión de esta versión.
