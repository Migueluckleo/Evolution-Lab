# Input Field · QA Figma 0.1.0

Fecha: 2026-09-28. Resultado **PASS técnico** para [INPUT-FIELD-001](../../specs/input-field.contract.v0.1.0.md). Estado técnico VALIDATED; auditoría humana PENDING por excepciones; biblioteca UNPUBLISHED.

## Alcance y evidencia

Fuente: página 20:3, set 186:14461 de 9zs5RMR8LB5wHjW9Bd59BA. Destino: página Input Fields 394:122, set Input Field 397:152 de tj3WIBEZDGLVs7MJWKCwgf. Search (12), Textarea (4) y File Upload (6) solo están inventariados; esta validación no los cubre.

- [Lectura completa y pruebas](input-field.v0.1.0.audit.json): 487 nodos, incluidas capas ocultas; cero errores.
- [Paridad](input-field.v0.1.0.alias-parity.json): 33 roles, 132 aliases por identidad lógica contra JSON base y extensión existente de foco. Sin nuevos tokens, primitivas ni cambios compartidos.
- [Contrastes](input-field.v0.1.0.contrast.json): cálculo desde RGB observados; no certifica accesibilidad.
- [Fuente observada](../../drafts/contracts/input-field.source.component-contract.md) y [QA documental](../contracts/input-field.v0.1.0.review.md).

## P3 · construcción completada

P3.a página semántica propia; P3.b 30 variantes con auto layout e iconos publicados; P3.c tres ejes y doce propiedades; P3.d documentación y rejilla; P3.e lectura real; P3.f comparación renderizada.

La fuente Question histórica se resolvió a la variante publicada Outline/Light key 8ebba51c41e3b39511663395803390b9d2e3d3f7; Eye conserva key e59dc310706bfe83ca2f09b69441d517c7372db1. Son instancias, no vectores recreados. Las pinturas de los iconos se vincularon a roles locales.

## P4 · resultados

| Comprobación | Resultado |
|---|---|
| Matriz Size × State × Value | 30 combinaciones; 3 × 5 × 2 |
| Geometría inicial | 464 × 96/88/80; Surface 48/40/32 |
| Pinturas, incluso contenido oculto | 306/306 con variables locales y scope/categoría correctos |
| Efectos | 14/14 con roles EFFECT_COLOR existentes |
| Tipografía | 150 textos; 750/750 bindings |
| Propiedades | 360 referencias conectadas; cuatro textos, siete booleanas, un swap |
| Iconos | 60 instancias, incluidas 30 Question ocultas por defecto |
| Modos | Sin modo fijado a los componentes; 132/132 aliases coinciden con JSON |
| Edición y composición | Tres instancias de prueba: textos editables, prefijo/ayuda visibles y controles ocultables |
| Ancho | 320 px probado en Large Default y Medium/Small Focus; Surface y soporte se ajustan |
| Ocultar etiqueta/helper | Altura final 48/40/32; sin huecos residuales |
| Reacciones | Cero, como fuente |
| Publicación Figma | UNPUBLISHED, leído con getPublishStatusAsync |

Los bindings tipográficos se leen como arrays/rangos, no como un único alias escalar. Los roles color/feedback/*/text son texto válido, además de color/text/*. Se corrigió el lector de QA para estas dos formas, sin cambiar tokens ni tipografía.

## Corrección visual del foco

La primera captura mostró ausencia de foco pese a efectos correctamente leídos en Surface. Una prueba temporal comparó efectos literales, ligados y showShadowBehindNode sobre rectángulos: los tres se renderizaron. Se restauró el soporte rectangular que existía en la fuente, con fondo semántico background/default y efecto focus/effect-outer.

Soportes 401:152–401:157, uno por Focus. Captura posterior de Medium Focus Empty 395:366 comparada con fuente 186:14510: anillo visible, misma apariencia, sin alterar dimensiones. Captura final del set 397:152: seis focos visibles, distribución estable, 30 controles sin recortes de contenido predeterminado. No se afirmó equivalencia solo por igualdad de propiedades.

El marco de diagnóstico 400:152 y sus tres rectángulos se retiraron. Las instancias de prueba también se retiraron tras medirlas; sus IDs están en el readback. No se eliminó contenido previo del usuario.

## Límites y auditoría por excepciones

- Borde neutral/400 sobre blanco: **2.56:1 ***. Disabled sobre fondo sutil: **2.34:1 ***. Se conserva fuente; el equipo revisará aplicabilidad contextual.
- Tertiary/blanco 4.76:1; Primary/blanco 17.85:1; Success/blanco 4.93:1; Error/blanco 5.53:1; foco/blanco 11.07:1. Estos pares no prueban por sí solos cumplimiento completo.
- Halo interior #F8FAFC→#FFFFFF por primitiva existente; normalizaciones de tracking 0.1%→0 e interlineado AUTO≈19→20; prefijo Small 12→16. Declaradas antes de construir, sin cambiar alturas públicas.
- Filled Disabled conserva texto primary, como fuente. Eye y Question no implican acciones web inventadas.
- Sin lógica de formulario, teclado, captura real, validación de datos o accesibilidad frontend; no forman parte de esta entrega.

## Cierre

Contrato promovido a specs; posteriores ajustes allí mediante revisión versionada. Graphify STALE para nuevos documentos, sin regeneración. Sigue Search dentro de Input Fields; después Textarea y File Upload, con sus propios contratos y QA. No hay conflicto bloqueante para esta entrega.
