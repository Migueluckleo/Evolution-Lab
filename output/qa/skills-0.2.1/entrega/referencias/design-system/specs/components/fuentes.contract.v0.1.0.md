---
contract_schema: sdd-project/0.2
contract_id: FUENTES-001
name: Fuentes
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
figma_page_name: Fuentes
review_targets: [figma]
slot_applicability: REQUIRED
sources: [SRC-FIGMA-FUENTES-001, SRC-TOKENS-INV-001]
dependencies: [FOUNDATIONS-TOKENS-001, FOUNDATIONS-FUENTES-HOVER-001, DOT-001]
last_updated: 2026-10-09
---

# Fuentes · contrato de integración 0.1.0

## 1. Purpose

Tarjeta compacta que presenta una referencia de contenido: número, tipo, fuente, ubicación y ruta. Fuente observada [Navi / Fuentes64:4164](https://www.figma.com/design/8qsdk3nalNNyCzBfUTrOcP?node-id=64-4164). No define búsqueda ni navegación funcional.

## 2. Contract

REQ-FUE-01 MUST crear un set Fuentes con Default/Hover en página única Fuentes del AI DS `tj3WIBEZDGLVs7MJWKCwgf`. Nombre funcional adoptado del componente fuente bajo [delegación externa](../../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md). No escribir en origen, modificar Dots, importar variables remotas, publicar biblioteca ni implementar frontend.

## 3. Anatomy

Tarjeta vertical → Info (fila Reference + Type, Source, Location) → Path SLOT. Dot Count/Medium local155:134 conserva vínculo, con overrides de referencia neutral observados. Subcomponente Fuentes Path Item incluye Label editable y Separator opcional; pertenece a esta misma familia y página, no reemplaza Breadcrumbs de navegación.

## 4. Properties

REQ-FUE-02 MUST: State VARIANT Default|Hover, defaultDefault; Type TEXT `Manual de referencia`, Source TEXT `CONTPAQi®`, Location TEXT `Mi cuenta`; Reference expone Count de Dot, default2; Path SLOT con segmentos editables. Path Item: Label TEXT, Show separator BOOLEAN false. El consumidor activa separador en elementos posteriores al primero; no cálculo automático de índices.

## 5. Variants

Solo dos variantes observadas: Default64:4163 y Hover64:4162. Sin nuevas variantes por cantidad, tema, selección o Disabled.

## 6. Sizes

REQ-FUE-03 MUST preservar ancho de muestra167.6666717529297, min150,max168, altoHUG, padding8, gap8, radio8,trazo1INSIDE incluido en layout. Límites de ancho son geometría observada, no tokens inventados. Info y Path FILL horizontal/HUG vertical para permitir contenido largo. El alto puede crecer;90px es referencia de muestra, no máximo.

## 7. States

Default fondo base; Hover fondo de marca suave y referencia blanca, ambos conservan borde accent. No fijar modo en los principales; heredan Contable/Administrativo/Servicios/Personas.

## 8. Behavior

REQ-FUE-04 MUST conservar ausencia de reacciones; State representa una vista editable, no un prototipo funcional. Apertura de fuente, URL, hover automático y tratamiento de grupo vacío son UNRESOLVED para producto, fuera del alcance visual.

## 9. Accessibility

La muestra usa texto diminuto8px en ruta y contador*. Se conserva como excepción observada de tamaño sin token equivalente (precedente DOT-001); no certifica accesibilidad. Contraste por modo se documenta sin recolorear. Roles, foco, teclado y nombre accesible quedan para implementación de producto.

## 10. Design tokens

REQ-FUE-05 MUST consumir variables semánticas locales de scope correcto, verificadas contra [inventario canónico](../../sources/inventories/tokens.inventory.json), SHA256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`. El JSON gobierna nombres/tipos/modos/valores/aliases/description; no se duplica catálogo. [Mapa derivado](../../implementations/figma/fuentes.v0.1.0.token-map.json) y [preflight](../../implementations/figma/fuentes.v0.1.0.preflight.json).

| Parte | Rol |
|---|---|
| Fondo Default / contador Hover | color/background/default |
| Fondo Hover | color/background/source-card/hover, extensión específica |
| Contador Default | color/background/subtle |
| Borde tarjeta | color/border/accent |
| Tipo / número | color/text/secondary |
| Fuente | color/text/primary |
| Ubicación | color/text/brand |
| Ruta/separador | color/text/tertiary |
| Fuente/pesos | font/family/base; font/weight/regular,bold |
| Texto principal12 | font/size/xs |
| Interlineado/tracking propio | font/line-height/xs; font/letter-spacing/normal |
| Padding/gaps/radio/trazo | spacing/sm,xs,none; radius/md; stroke/xs |

REQ-FUE-06 MUST crear solo un rol Hover desde [extensión canónica](../../sources/inventories/ai-design-system.fuentes-hover.v0.1.0.json), alias directo a primitivas existentes blue/green/orange/purple100 por modo; cero primitivas nuevas. Corrige semántica sourceghost/active sin cambiar RGBContable. Familia tipográfica observada Manrope, strings canónicos lower-case preservados en variables, fuente renderizada disponible Regular/Bold. La ruta8px y Dot8px son literales observados documentados, no tokens nuevos. Estilos propios reutilizan variables; no modificar estilos compartidos. Normalización adoptada: interlineado16 y tracking0 en texto propio, en lugar de AUTO/160% y−2%; Dot mantiene su tipografía original.

## 11. Content rules

Ejemplos editables, no reglas de negocio. Ruta es metadato de origen, no breadcrumb navegable por apariencia. Separador visible `·` adoptado de captura; getter fuente devuelve cadena vacía, diferencia explícita. El autor mantiene orden y separadores tras reordenar.

## 12. Composition rules

REQ-FUE-07 MUST implementar Path nativo por P-SLOTS0.1.0. Dos segmentos iniciales no limitan cardinalidad. Insertar/quitar/reordenar/sustituir Fuentes Path Item desde instancias vinculadas; anchoFILL, altoHUG, horizontalWRAP, gap0; cada segmento anchoHUG con límite que permite caber en ancho mínimo de tarjeta y texto largo multilineal. No fija máximo de elementos de producto. Vacío se admite estructuralmente para QA, sin mensaje/estado de producto inventado. Bindings se heredan. Preferencias de contenido son recomendaciones, no seguridad. Reusar Dot mediante instancia, con fill/strokes/text override locales solo dentro de Fuentes.

## 13. Responsive behavior

Reflow dentro de150–168px; Info crece y Path pasa a nuevas líneas sin scroll interno. No breakpoints ni distribución de colección definidos. Fuentes no incluye lista anfitriona de tarjetas.

## 14. Edge cases

Probar textos largos a150px; Path0,1,2,4 segmentos, reordenado/sustituido; preservar contenido al cambiar State. Count de muchos dígitos excede geometría de Dot: no se define autoellipsis ni conversión99+.

## 15. Forbidden combinations

No primitivas directas, RGB pegados, rolestext en fondos, states agregados, URLs ficticias ni cambios en principales Dots. No prometer que Hover sea seleccionado. No usar cantidad inicial como máximo.

## 16. Design ↔ Code mapping

Contrato visual Figma únicamente. API web, navegación, ARIA y lógica de referencia no definidos. No se autoriza React ni Code Connect.

## 17. Acceptance criteria

| Control | Comprobación |
|---|---|
| AC-FUE-01 | PáginaFuentes única; set2variantes; principales/ejemplos separados. |
| AC-FUE-02 | Props TEXT y Slot conectados; instanciaDot155:134 intacta, fuente no modificada. |
| AC-FUE-03 | Ancho/límites/padding/radio/trazo y reflow segúnREQ03. Captura comparada. |
| AC-FUE-04 | Colores locales de scope correcto, aliases de19roles auditados+extensión Hover en4modos; sin primitivas consumidoras. |
| AC-FUE-05 | Tipografía12canónica, ruta8excepción, estilos y bindings reales; ninguna fuente ausente. |
| AC-FUE-06 | PathSLOT probado en instancias0/1/2/4, reorder/replacement,longtext,width150,StateSwap; no detach. |
| AC-FUE-07 | Reacciones0; contraste/legibilidad y límites explícitos, sin certificación web. |
| AC-FUE-08 | Contrato/JSON/estado/QA/registros/grafo sincronizados; promociónspecs trasPASS; auditoríaPENDING. |

## 18. Examples

Dos estados con mismo ejemplo de origen; pruebas de tamaño/composición documentadas separadamente, no nuevas variantes.

## 19. Source of truth

Este MD gobierna integración; JSON base y extensión gobiernan tokens. [Evidencia de origen](../../drafts/contracts/fuentes.source.component-contract.md), [YAML](../../drafts/contracts/fuentes.source.component-contract.yaml), [snapshot](../../sources/figma-snapshots/fuentes.source.v0.1.0.json). El grafo es derivado.

## 20. Change management

DEC-EXTERNAL-COMPONENTS-DELEGATION-001 permite homologación con QA y auditoría por excepciones. Diferencias anunciadas: token Hovercorrecto; textos editables; PathSLOT; Info responsive; interlineado/tracking homologados. No aprobación humana simulada. Ajustes posteriores directos en specs con versión.

## 21. Changelog

0.1.0: integración de fuente externa acotada, dos estados, dependencia Dot reutilizada y tokens locales.

Cierre 2026-10-09: [QA técnico](../../qa/implementations/fuentes.v0.1.0.review.md), [estado e IDs](../../implementations/figma/fuentes.v0.1.0.state.json) y [Foundations](../foundations/fuentes-hover.contract.v0.1.0.md). Promoción documental por QA, no aprobación humana ni publicación remota. Ruta: Label HUG con maxWidth116 y alto automático; Path Item maxWidth132, separador12. El Slot vacío conserva16px en el readback de Figma; no se promete colapso. Las limitaciones de contraste medidas quedan en el QA y la auditoría por excepciones, sin recolorear.
