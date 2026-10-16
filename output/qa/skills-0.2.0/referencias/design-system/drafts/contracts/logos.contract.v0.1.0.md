---
contract_id: LOGOS-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
destination_file_key: tj3WIBEZDGLVs7MJWKCwgf
destination_page: Logos
source_file_key: 9zs5RMR8LB5wHjW9Bd59BA
source_page_id: "40:93"
decision_refs: [DEC-LOGOS-AGNOSTIC-ASSETS-001, DEC-LEGACY-MIGRATION-DELEGATION-001]
last_updated: 2026-09-28
---

# Logos · contrato de migración 0.1.0

## 1. Purpose

Copiar los assets de marca originales de la Librería anterior a AI Design System, documentados antes de construir. Son agnósticos: no dependen de variables, tokens del JSON ni temas del sistema. La excepción explícita procede de DEC-LOGOS-AGNOSTIC-ASSETS-001; no se extiende a componentes UI consumidores.

## 2. Contract

| Requisito | Regla | Procedencia | QA |
|---|---|---|---|
| REQ-LOG-001 | MUST conservar los seis conjuntos, sus 72 variantes observadas y los 12 assets sueltos; no completar combinaciones inventadas. | OBSERVED: inventario; adopción delegada | Conteos, nombres y propiedades |
| REQ-LOG-002 | MUST conservar colores, trazados, imágenes, gradientes, efectos, dimensiones, proporciones y jerarquía del artwork. Solo la ubicación en el lienzo y documentación pueden cambiar. | EXPLICIT: copiar originales | Readback geométrico/cromático y capturas |
| REQ-LOG-003 | MUST NOT consumir variables, tokens ni primitivas dentro de Logos. Los ocho bindings heredados de assets sueltos se eliminan solo en destino, conservando azul visible #3255F7 o blanco #FFFFFF. | EXPLICIT + OBSERVED: fills de ocho vectores | Cero bindings en todo el subtree |
| REQ-LOG-004 | MUST mantener dependencias locales: las cuatro instancias de logo-categoria apuntan a copias locales de sus productos. | DERIVED: independencia del destino | Main components por ID local |
| REQ-LOG-005 | MUST conservar fuentes y registrar IDs reales origen→destino. No modificar la Librería anterior. | EXPLICIT: protocolos | Mapa y evidencia |
| REQ-LOG-006 | MUST conservar las propiedades product, type, Mode y categoria tal como están observadas. Mode es una variante manual del asset, no modo de variable ni cambio automático por tema. | OBSERVED + EXPLICIT agnóstico | Definiciones y combinaciones |
| REQ-LOG-007 | MUST ubicar la familia en una sola página Logos, con guía propia; no copiar el header documental de la Librería vieja. | DERIVED: familia del inventario + P04 | Identidad y unicidad de página |
| REQ-LOG-008 | MUST completar QA documental antes de escribir y QA técnico después; publicación documental y de biblioteca son estados separados. | EXPLICIT: P03–P06 | Registros |

## 3. Anatomy

18 raíces de artwork, 2,999 nodos inspeccionados, incluidos descendientes invisibles, sin pendientes de traversal. Los 12 assets sueltos conservan frames originales. No se rasteriza ni redibuja el arte.

| Raíz fuente | ID | Tipo | Variantes | Nodos |
|---|---|---|---:|---:|
| administrativos | `2849:210103` | COMPONENT_SET | 24 | 1276 |
| contables | `2849:211519` | COMPONENT_SET | 21 | 698 |
| personas | `2849:212172` | COMPONENT_SET | 12 | 306 |
| servicios | `2849:212402` | COMPONENT_SET | 6 | 242 |
| CONTPAQi | `5400:1929` | COMPONENT_SET | 5 | 234 |
| logo_SSCi | `4969:325` | FRAME | — | 2 |
| Logo_SaCi | `4969:327` | FRAME | — | 2 |
| Logo_FD | `4969:328` | FRAME | — | 2 |
| Logo_ADD | `4969:326` | FRAME | — | 2 |
| logo_SSCi-bco | `4969:329` | FRAME | — | 2 |
| Logo_SaCi-bco | `4969:331` | FRAME | — | 2 |
| Logo_FD-bco | `4969:333` | FRAME | — | 2 |
| Logo_ADD-bco | `4969:335` | FRAME | — | 2 |
| Capa_1 | `5390:256` | FRAME | — | 6 |
| icono_i | `5656:22` | FRAME | — | 2 |
| Capa_1 | `5390:263` | FRAME | — | 6 |
| logo_mifactura | `5639:1658` | FRAME | — | 2 |
| logo-categoria | `8305:227` | COMPONENT_SET | 4 | 211 |

El contenedor documental fuente 2415:1930, su header y divisor no forman parte del artwork migrado. Los nombres Capa_1 de 5390:256 y 5390:263 se conservan como evidencia; su ID distingue ambos assets sin inventar nombre comercial.

## 4. Properties

Los cuatro conjuntos de productos exponen product/type. CONTPAQi expone product/Mode; logo-categoria expone categoria. Definiciones, defaults y opciones completas: [inventario](../../sources/figma-snapshots/logos.inventory.v0.1.0.json). Sin propiedades de texto, icon swap o disponibilidad añadidas.

## 5. Variants

| Conjunto | Variante observada | ID fuente | Dimensiones px |
|---|---|---|---|
| administrativos | product=comercial_premium, type=vertical | `2849:210092` | 126 × 136 |
| administrativos | product=comercial_premium, type=horizontal | `2849:210099` | 244 × 77 |
| administrativos | product=comercial_premium, type=isotipo | `2849:210100` | 126 × 115 |
| administrativos | product=comercial_pro, type=vertical | `2849:210097` | 126 × 136 |
| administrativos | product=comercial_pro, type=horizontal | `2849:210080` | 243 × 77 |
| administrativos | product=comercial_pro, type=isotipo | `2849:210095` | 126 × 115 |
| administrativos | product=comercial_start, type=vertical | `2849:210093` | 126 × 136 |
| administrativos | product=comercial_start, type=horizontal | `2849:210091` | 243 × 77 |
| administrativos | product=comercial_start, type=isotipo | `2849:210090` | 126 × 115 |
| administrativos | product=mi_factura, type=vertical | `2849:210096` | 168 × 136 |
| administrativos | product=mi_factura, type=horizontal | `2849:210102` | 282 × 77 |
| administrativos | product=mi_factura, type=isotipo | `2849:210088` | 130 × 115 |
| administrativos | product=cfdi_facturacion, type=vertical | `2849:210087` | 210 × 136 |
| administrativos | product=cfdi_facturacion, type=horizontal | `2849:210101` | 357 × 77 |
| administrativos | product=cfdi_facturacion, type=isotipo | `2849:210098` | 125 × 115 |
| administrativos | product=vende, type=vertical | `2849:210082` | 100 × 136 |
| administrativos | product=vende, type=horizontal | `2849:210086` | 206 × 77 |
| administrativos | product=vende, type=isotipo | `2849:210085` | 127 × 115 |
| administrativos | product=timbra, type=vertical | `2849:210084` | 101 × 136 |
| administrativos | product=timbra, type=horizontal | `2849:210094` | 188 × 77 |
| administrativos | product=timbra, type=isotipo | `2849:210083` | 101 × 115 |
| administrativos | product=factura_electronica, type=vertical | `2849:210081` | 143 × 136 |
| administrativos | product=factura_electronica, type=horizontal | `2849:210089` | 264 × 77 |
| administrativos | product=factura_electronica, type=isotipo | `2849:210079` | 116 × 115 |
| contables | product=conecta_tu_banco, type=vertical | `2849:211518` | 120 × 136 |
| contables | product=conecta_tu_banco, type=horizontal | `2849:211516` | 240 × 77 |
| contables | product=conecta_tu_banco, type=isotipo | `2849:211506` | 124 × 115 |
| contables | product=xml_en_linea, type=vertical | `2849:211510` | 221 × 136 |
| contables | product=xml_en_linea, type=horizontal | `2849:211509` | 376 × 77 |
| contables | product=xml_en_linea, type=isotipo | `2849:211517` | 156 × 115 |
| contables | product=contabilidad, type=vertical | `2849:211515` | 193 × 136 |
| contables | product=contabilidad, type=horizontal | `2849:211513` | 282 × 77 |
| contables | product=contabilidad, type=isotipo | `2849:211512` | 112 × 115 |
| contables | product=tesoreria, type=vertical | `2849:211511` | 143 × 136 |
| contables | product=tesoreria, type=horizontal | `2849:211507` | 225 × 77 |
| contables | product=tesoreria, type=isotipo | `2849:211504` | 101 × 115 |
| contables | product=optimiza, type=vertical | `2849:211503` | 131 × 136 |
| contables | product=optimiza, type=horizontal | `2849:211501` | 239 × 77 |
| contables | product=optimiza, type=isotipo | `2849:211514` | 119 × 115 |
| contables | product=bancos, type=vertical | `2849:211505` | 123 × 136 |
| contables | product=bancos, type=horizontal | `2849:211500` | 233 × 77 |
| contables | product=bancos, type=isotipo | `2849:211502` | 125 × 115 |
| contables | product=anticipa, type=vertical | `2849:211499` | 129 × 136 |
| contables | product=anticipa, type=horizontal | `2849:211498` | 239 × 77 |
| contables | product=anticipa, type=isotipo | `2849:211508` | 123 × 115 |
| personas | product=nominas, type=vertical | `2849:212171` | 140 × 136 |
| personas | product=nominas, type=horizontal | `2849:212167` | 247 × 77 |
| personas | product=nominas, type=isotipo | `2849:212166` | 116 × 115 |
| personas | product=colabora, type=vertical | `2849:212163` | 137 × 136 |
| personas | product=colabora, type=horizontal | `2849:212161` | 242 × 77 |
| personas | product=colabora, type=isotipo | `2849:212165` | 120 × 115 |
| personas | product=evalua, type=vertical | `2849:212164` | 103 × 136 |
| personas | product=evalua, type=horizontal | `2849:212170` | 215 × 77 |
| personas | product=evalua, type=isotipo | `2849:212169` | 125 × 115 |
| personas | product=kursa, type=vertical | `2849:212168` | 93 × 136 |
| personas | product=kursa, type=horizontal | `2849:212162` | 215 × 77 |
| personas | product=kursa, type=isotipo | `2849:212160` | 138 × 115 |
| servicios | product=respaldos, type=vertical | `2849:212401` | 153 × 136 |
| servicios | product=respaldos, type=horizontal | `2849:212400` | 256 × 77 |
| servicios | product=respaldos, type=isotipo | `2849:212399` | 125 × 115 |
| servicios | product=VDI, type=isotipo | `5454:2177` | 96 × 94.85856628417969 |
| servicios | product=VDI, type=horizontal | `5454:2176` | 339.0320739746094 × 72.1941909790039 |
| servicios | product=VDI, type=vertical | `5454:2175` | 225.01663208007812 × 159.50588989257812 |
| CONTPAQi | product=CONTPAQi, Mode=dark | `5400:1928` | 348.667724609375 × 77 |
| CONTPAQi | product=CONTPAQi, Mode=light | `5400:1927` | 345.388427734375 × 76.99999237060547 |
| CONTPAQi | product=CONTPAQi, Mode=light2 | `5400:1925` | 343.49951171875 × 77 |
| CONTPAQi | product=Mi CONTPAQi, Mode=light | `5400:1926` | 522.6395263671875 × 77 |
| CONTPAQi | product=Mi CONTPAQi, Mode=dark | `5400:1924` | 484.36444091796875 × 77 |
| logo-categoria | categoria=contable | `8305:68` | 175.79220581054688 × 48 |
| logo-categoria | categoria=comercial | `8305:142` | 152.10389709472656 × 48 |
| logo-categoria | categoria=servicios | `8305:188` | 159.58441162109375 × 48 |
| logo-categoria | categoria=personas | `8305:226` | 150.85714721679688 × 48 |

No existe Mi CONTPAQi/Mode=light2 en la matriz observada: no generarlo.

## 6. Sizes

Conservar exactamente las dimensiones del inventario, sin normalizar anchos entre marcas. Las medidas son evidencia de cada asset, no tamaños mínimos ni reglas universales de marca.

## 7. States

NOT_APPLICABLE para Hover, Focus, Disabled, Loading y selección: no son controles interactivos. Light/dark/light2 son versiones gráficas seleccionables manualmente.

## 8. Behavior

No se observaron reacciones de prototipo en los 18 subtrees. No añadir animación, navegación ni cambio automático por tema. El comportamiento de Header u otro consumidor se documenta en su propio contrato.

## 9. Accessibility

No se afirma conformidad WCAG del conjunto. Alternativas textuales, enlaces y semántica accesible dependen del contexto web futuro, fuera de alcance. Las versiones blancas necesitan superficie de presentación contrastante; eso no autoriza recolorear el logo.

## 10. Design tokens

NOT_APPLICABLE en destino por DEC-LOGOS-AGNOSTIC-ASSETS-001. No se crea ni modifica el JSON de variables, ni se vinculan primitivas directamente.

Evidencia histórica: cuatro vectores fuente consumen color/interactive/primary/default y cuatro color/icon/on-brand. Se documentan como bindings observados de origen, no como dependencias permitidas del destino. Al transferir se congelan los fills visibles #3255F7 y #FFFFFF respectivamente. No se crean versiones verde/naranja/morada por los modos heredados. Los restantes subtrees no tienen variables ni estilos nombrados usados.

## 11. Content rules

Los nombres y letras forman parte de vectores; no sustituirlos por texto editable ni por otra fuente. No corregir nombres comerciales por conjetura. Las descripciones de destino son nuestras y explican la copia agnóstica, no simulan manual de marca oficial.

## 12. Composition rules

Construir los cinco conjuntos de productos/corporativos antes de logo-categoria. Esta última reutiliza cuatro variantes horizontales locales: contabilidad, comercial_premium, respaldos y colabora. Conservar escala y overrides de cada instancia.

## 13. Responsive behavior

No se define responsive web. Conservar constraints originales; no estirar por separado los ejes para adaptar el logo a un espacio. No imponer Auto Layout al trazado vectorial que cambie su geometría.

## 14. Edge cases

Conservar gradientes, imágenes, opacidad, sombra corporativa, máscaras y contenido invisible. Assets blancos no se declaran vacíos por verse sobre blanco. Dos raíces llamadas Capa_1 se distinguen por ID de fuente, no se deduplican.

## 15. Forbidden combinations

No inventar variantes faltantes, recolorear con brand, vincular JSON, dejar instancias dependientes del archivo anterior, sustituir por raster ni aplanar el artwork para ocultar una pérdida de estructura.

## 16. Design ↔ Code mapping

Solo Figma. No se genera código frontend, paquete ni Code Connect. Un asset no demuestra reglas de enlaces, alt text o rutas.

## 17. Acceptance criteria

REQ-LOG-001–008 deben pasar antes de VALIDATED. Comprobar 72 variantes + 12 assets, propiedades/defaults, dimensiones, colores, paths y dependencias. Cero bindings en 18 subtrees. Comparar firmas estructurales deterministas del [baseline](../../sources/figma-snapshots/logos.fidelity-baseline.v0.1.0.json), sin IDs y sin traslación de la raíz; cualquier diferencia requiere comparación de campos, no relajar la prueba. Las firmas duales de 32 bits son checksums de ingeniería, no hashes criptográficos ni sustituyen revisión visual. Conservar SHA-256 de archivos de evidencia por separado.

## 18. Examples

Seleccionar product=contabilidad,type=horizontal en contables; seleccionar product=CONTPAQi,Mode=dark para esa versión gráfica. Elegir categoria=contable no cambia colores según el tema.

## 19. Source of truth

Reglas: este contrato y [decisión](../../registry/decisions.md). Datos observados: inventario y baseline referenciados. Fuente: https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=40-93. Destino: AI Design System, página prevista Logos; ID se obtiene después de crear. El discovery histórico de Logo Categoria 8321:504 no sustituye el set real de esta página 8305:227; su consumidor Header se revisará por separado.

## 20. Change management

Promover a specs solo con QA técnico PASS. Después, ajustes directamente en specs con versión y trazabilidad. Auditoría humana PENDING por excepciones; no publicar biblioteca automáticamente.

## 21. Changelog

2026-09-28 · 0.1.0: lectura profunda de 18 raíces; adopción delegada de copia fiel y excepción agnóstica explícita. Documentación previa a construcción.
