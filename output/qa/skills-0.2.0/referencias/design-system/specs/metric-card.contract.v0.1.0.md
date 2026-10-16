---
contract_schema: sdd-project/0.2
contract_id: METRIC-CARD-001
name: Metric Cards
type: component_family
status: DELEGATED_FOR_BUILD
version: 0.1.0
last_updated: 2026-09-23
review_targets: [figma]
figma_page_name: Metric Cards
sources: [SRC-FIGMA-METRIC-CARD-001, SRC-TOKENS-INV-001, DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-SEMANTIC-EXTENSIONS-001]
data_refs: [sources/inventories/tokens.inventory.json, drafts/foundations/ai-design-system.metric-card-roles.v0.1.0.json, drafts/contracts/metric-card.source.component-contract.yaml]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-METRIC-CARD-ROLES-001, SRC-FIGMA-PHOSPHOR-001]
user_audit: PENDING
---

# Metric Cards · contrato de reconstrucción 0.1.0

> Vigencia cromática: la [enmienda SIX-FAMILY-COLOR-001](components/six-family-color.amendment.v0.1.0.md) sustituye exclusivamente las recetas/umbrales allí identificados. Publicación documental 2026-10-05; auditoría humana PENDING. Los apartados históricos se leen junto con esa enmienda.

## 1. Purpose

Mostrar métricas numéricas destacadas en cuatro disposiciones y dos escalas. El [contrato fuente](../drafts/contracts/metric-card.source.component-contract.md) es evidencia; este contrato gobierna la reconstrucción en AI Design System. El contenido es de muestra y no calcula datos.

## 2. Contract

Crear una página semántica exclusiva `Metric Cards` y un set principal `Metric Card`, con ocho variantes `Type × Size`, conservando el aspecto de la fuente salvo correcciones explícitas. Usar variables locales de AI Design System y la [extensión semántica Metric Card](../drafts/foundations/ai-design-system.metric-card-roles.v0.1.0.json). Mantener el set `UNPUBLISHED` hasta auditoría humana.

## 3. Anatomy

Vertical Metric y Horizontal Metric: fondo sutil, Header con CurrencyCircleDollar, Title, Navigate/ArrowUpRight y Description; Content con dos pares Amount/Value. Vertical apila pares; Horizontal los coloca en filas etiqueta-valor. One Metric V1: icono, Title, Value, Trend, Navigate. One Metric V2: borde de tarjeta, baldosa sutil con icono, Content y Navigate. Ambos iconos son instancias Phosphor reales, no vectores convertidos en componentes nuevos.

## 4. Properties

| Propiedad | Tipo | Default | Aplicación |
|---|---|---|---|
| Type | VARIANT | Vertical Metric | Cuatro estructuras observadas |
| Size | VARIANT | Large | Large/Small |
| Title | TEXT | Title | Ocho variantes |
| Show icon | BOOLEAN | true | Instancia CurrencyCircleDollar, ocho variantes |
| Icon | INSTANCE_SWAP | CurrencyCircleDollar | Ocho variantes; sin preferred values inventados |
| Show action | BOOLEAN | true | Contenedor Navigate, ocho variantes |
| Show detail | BOOLEAN | true | Description en doble métrica; Trend en One Metric |
| Description | TEXT | Description | Cuatro variantes de dos métricas |
| Amount 1/2 label | TEXT | Amount 1/2 | Cuatro variantes de dos métricas |
| Amount 1/2 value | TEXT | `$123,456.00` | Vertical Large/Small |
| Horizontal amount 1/2 value | TEXT | `$123,320.00` | Horizontal Large/Small; separado para conservar el ejemplo fuente |
| Value | TEXT | `$123,320.00` | Cuatro variantes One Metric |
| Trend | TEXT | `+5.2%` | Cuatro variantes One Metric |

Las propiedades de textos numéricos son una mejora de editabilidad del destino; la fuente solo exponía Title y Description. Su presencia no define formato, signo o cálculo.

## 5. Variants

Exactamente Vertical Metric/Large, Vertical Metric/Small, Horizontal Metric/Large, Horizontal Metric/Small, One Metric V1/Large, One Metric V1/Small, One Metric V2/Large y One Metric V2/Small. No crear variantes interactivas adicionales.

## 6. Sizes

Cajas de referencia fuente: 289×256, 200×216, 311×192, 232×160, 337×151, 257×111, 397×144 y 313×112 respectivamente. El destino mantiene seis cajas idénticas y amplía solo V1 Large/Small a 337×156 y 257×116: cinco píxeles verticales permiten line-height semántico de 20 px a Trend sin cortar su texto. Padding 24 Large / 16 Small, radius 16, gaps 16 y secundarios 8/4 según anatomía; iconos CurrencyCircleDollar 32/24 en Vertical/Horizontal/V1 y 64/48 en V2; ArrowUpRight 24/16; Navigate 32/24. Los iconos y Navigate de V1/V2 se alinean arriba como en la fuente.

## 7. States

El origen no contiene State, Hover, Focus ni Disabled. Las propiedades Show no crean estados interactivos; solo controlan visibilidad. No simular hover o acción mediante prototipos no observados.

## 8. Behavior

Navigate es una affordance visual sin reacción Figma ni destino definido. Ninguna tarjeta actualiza cifras, porcentajes o iconos automáticamente. El comportamiento web debe especificarse después.

## 9. Accessibility

El consumidor debe decidir si Navigate es botón o enlace y darle nombre, foco y objetivo táctil. La lectura de importe, etiqueta y tendencia debe ser comprensible sin depender solo de color. No se certifica accesibilidad funcional desde Figma; sí se comprueba contraste visual de tokens aplicados.

## 10. Design tokens

El inventario base aprobado tiene SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. Los roles nuevos están en el JSON de extensión y fueron leídos de vuelta en Figma. Mapa estricto por consumidor:

| Consumidor | Variable semántica | Scope |
|---|---|---|
| Fondo de tarjeta Vertical/Horizontal/V1, baldosa V2, Navigate V2 | `color/background/subtle` | `FRAME_FILL` |
| Navigate Vertical/Horizontal/V1 | `color/background/default` | `FRAME_FILL` |
| Borde V2 | `color/border/subtle` | `STROKE_COLOR` |
| Title, etiquetas e importes | `color/text/primary` | `TEXT_FILL` |
| Description | `color/text/secondary` | `TEXT_FILL` |
| Trend | `color/text/metric/trend` | `TEXT_FILL` |
| Vectores CurrencyCircleDollar y ArrowUpRight | `color/icon/metric/brand` | `SHAPE_FILL` |
| Tipografía | `font/family/base`, `font/weight/regular`, tamaños `xs/sm/md/lg/xl/2xl`, line-height `xs/sm/md/lg/xl`, tracking `normal` | Sus scopes tipográficos respectivos |
| Layout | `spacing/xs/sm/lg/xl`, `radius/sm/xl`, `size/lg/xl/2xl/4xl/6xl`, `stroke/xs` | GAP/CORNER_RADIUS/WIDTH_HEIGHT/STROKE_FLOAT según propiedad |

La fuente V1 Small usa 18 px para Title, sin primitiva ni semántica de 18 en el destino; se normaliza a `font/size/lg`=20 px y se ajusta su caja solo si hace falta. En Horizontal Small, el importe es 20 px, no 24. Los aliases nuevos retienen marca de origen en tres modos; Servicios usa orange/700 en texto e icono para pasar de 2.95 a 6.57:1 sobre sutil. No aplicar tokens de texto en shapes, de icono en textos ni de fondo en trazos.

## 11. Content rules

`Title`, `Description`, `Amount 1/2`, importes y `+5.2%` son ejemplos editables en Figma. El porcentaje no implica positividad semántica. No se define moneda, redondeo, signo, localización ni longitud máxima. Para textos más largos, el consumidor debe revisar el layout; esta matriz documenta las muestras visibles.

## 12. Composition rules

Cada variante contiene una instancia CurrencyCircleDollar y una ArrowUpRight. No duplicar iconos con vector manual ni detach. Las dos métricas de Vertical/Horizontal son grupos separados; V2 usa baldosa independiente y borde de tarjeta. Los componentes principales importados siguen en la biblioteca de iconos.

## 13. Responsive behavior

Large y Small son variantes explícitas, no breakpoints automáticos. No se infiere adaptación móvil ni salto de dos métricas a una.

## 14. Edge cases

Si se oculta icono, acción o detalle, auto layout debe colapsar el espacio correspondiente sin pintar elementos invisibles. Una cifra larga puede requerir más ancho; no truncar silenciosamente un importe. La estructura V2 conserva borde visible cuando el icono se oculta, aunque la baldosa pueda vaciarse.

## 15. Forbidden combinations

No crear estados no observados, no aplicar `color/text/brand` a Trend en Servicios, no reutilizar un token de icono para el porcentaje ni viceversa, no añadir primitive orange/700 duplicada, no usar literales de color visibles sin variable y no usar iconos del archivo fuente como assets detached.

## 16. Design ↔ Code mapping

Type y Size representan presentación; en código futuro la cifra y variación deberán ser datos tipados y localizados, y Navigate una acción o enlace declarado por producto. Esta tarea no genera frontend.

## 17. Acceptance criteria

| ID | Requisito verificable |
|---|---|
| AC-MTC-001 | Página exclusiva `Metric Cards`, un set y ocho variantes con Type×Size y defaults correctos. |
| AC-MTC-002 | Anatomía, escala y jerarquía visual comparadas con la captura fuente; desviaciones V1 Title Small 18→20 px y altura +5 px documentadas, sin clipping. |
| AC-MTC-003 | Ocho instancias CurrencyCircleDollar y ocho ArrowUpRight importadas por key, visibles y sin detach. |
| AC-MTC-004 | Propiedades de visibilidad y textos editables enlazadas a consumidores correctos; ejemplos mantienen cadenas fuente. |
| AC-MTC-005 | Todas las pinturas visibles tienen binding semántico local y scope/categoría correctos; JSON/Figma de dos roles nuevos coincide. |
| AC-MTC-006 | Texto Trend ≥4.5:1 e iconos ≥3:1 sobre blanco y sutil en los cuatro modos; tamaños/espacios/radios/typography ligados a variables locales. |
| AC-MTC-007 | Cero reacciones, set `UNPUBLISHED`, QA visual/estructural y auditoría humana posterior registradas. |

## 18. Examples

Vertical Large muestra dos importes apilados; Horizontal Small dos filas compactas; One Metric V1/V2 muestran un importe y variación. Son muestras estáticas.

## 19. Source of truth

Este Markdown gobierna reglas; el inventario base y el JSON de roles Metric Card gobiernan variables. El [YAML fuente](../drafts/contracts/metric-card.source.component-contract.yaml) conserva observación. Los IDs de origen no son IDs de destino; la implementación registra los últimos aparte.

## 20. Change management

Se mantienen ocho disposiciones y apariencia base. Cambios deliberados: dos roles de color separados por scope, Servicios orange/500→orange/700, título V1 Small 18→20 px, altura V1 +5 px para Trend y propiedades de edición para cifras/etiquetas/variación. Figma unificó el default de dos valores al combinar variantes; se separaron las propiedades de importe Horizontal y Vertical para recuperar `$123,320.00` y `$123,456.00` respectivamente. La fuente no se modifica.

## 21. Changelog

- 0.1.0 delegado: ocho variantes, página semántica, roles de texto/icono nuevos y mejoras de editabilidad explícitas.
