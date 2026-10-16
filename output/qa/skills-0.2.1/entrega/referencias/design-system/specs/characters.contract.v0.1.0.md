---
contract_id: CHARACTERS-001
name: Characters
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
review_targets: [figma]
figma_page_name: Characters
slot_applicability: NOT_APPLICABLE
sources: [SRC-ECOSISTEMA-CHARACTERS-001, DEC-EXTERNAL-COMPONENTS-DELEGATION-001, DEC-CHARACTER-IDENTITY-001]
data_refs: [sources/inventories/tokens.inventory.json, specs/tokens/ai-design-system.character-identity.v0.1.0.json, specs/tokens/ai-design-system.character-shadow.v0.1.0.json]
---

# Characters · BENI Standby y NAVI Analysis

## 1. Purpose

Integrar las dos secuencias de personajes indicadas por el usuario desde Ecosistema AI. Se conserva el arte y el bucle Figma observado; no se infiere estado de un servicio ni se modifica Conversation o Chat existentes.

## 2. Contract

REQ-CH-01 MUST crear dos sets locales, BENI Standby (6 fotogramas) y NAVI Analysis (7), en una página Characters. Nombre funcional tomado de la sección fuente characters y normalizado a la taxonomía del destino bajo delegación externa. REQ-CH-02 MUST conservar dimensiones, jerarquía, orden, geometría vectorial y pinturas originales, incluidas capas sin relleno. REQ-CH-03 MUST remapear los 13 CHANGE_TO a IDs locales, con tiempos y easing originales. REQ-CH-04 MUST vincular las 47 pinturas vectoriales a tokens de identidad fija. REQ-CH-05 MUST conservar los tres tokens existentes y añadir únicamente la sombra NAVI según JSON. REQ-CH-06 MUST guardar QA y trazabilidad sin publicación remota. Procedencia OBSERVED para arte/transiciones; EXPLICIT para tokenización y delegación; DERIVED para conteos y nomenclatura destino.

## 3. Anatomy

BENI: cuerpo, ojos agrupados y bigote, cuatro vectores por fotograma. NAVI: cuerpo, ojos agrupados y capas de sombra, incluyendo 17 vectores sin fill necesarios para mantener la estructura observada de la animación. Total: 13 componentes, 13 grupos, 64 vectores. Sin dependencias de instancias ni estilos de fuente.

## 4. Properties

Frame (VARIANT), no nullable; valor inicial 01. Sustituye el nombre genérico Property 1 solamente en el destino. BENI admite 01–06, NAVI 01–07. No añadir estados de producto, tamaños, campos de texto, booleanas ni swaps sin evidencia.

## 5. Variants

Orden de BENI: 209:6942 → 209:6941 → 217:1900 → 217:1894 → 217:1907 → 217:1914. Mapeo fuente Default/close/Variant4/Variant3/Variant5/Variant6 a Frame 01/02/03/04/05/06.

Orden de NAVI: 269:5944 → 509:17580 → 509:17675 → 509:17692 → 509:17699 → 509:17706 → 509:17713. Fuente 1/2/4/5/6/7/8 a Frame 01–07. No inventar el fotograma fuente 3 ausente; la cadena observada es cerrada.

## 6. Sizes

Cada fotograma conserva 168.739990234375 × 163.739990234375 px. Arte vectorial absoluto: no convertir ojos, bigote o sombras a auto layout. Geometría ilustrativa fija exceptuada de spacing/size de interfaz. Muestra de revisión usa auto layout; maestros fuera de ella.

## 7. States

Fotogramas de animación, no Hover/Disabled/Loading funcionales. Los nombres Standby y Analysis describen las secuencias de la fuente, no prueban un proceso de backend.

## 8. Behavior

AFTER_TIMEOUT → CHANGE_TO, bucle al primero de cada set, SMART_ANIMATE. Todos los datos exactos provienen de reactions del [snapshot](../sources/figma-snapshots/characters.ecosistema.2026-10-08.json); no se redondean al escribir. BENI esperas aproximadas 2/.001/.6/.6/.6/.6 s, duraciones .1/.1/.3/.3/.3/.3 s; solo la segunda transición usa EASE_IN_AND_OUT, las demás EASE_OUT. NAVI esperas .8/.4/.8/.8/.4/.8/.2 s; duración .3 s, EASE_OUT. No implementar keyframes de Motion ni inventar controles Play/Pause. QA verifica el grafo de reacciones y los fotogramas; la percepción en reproducción queda para auditoría humana.

## 9. Accessibility

No controles interactivos, texto ni foco. Semántica de producto y reduced motion son UNRESOLVED para frontend fuera de alcance. Medir contraste de rasgos/cuerpo y sombra/cuerpo sin convertir identidad gráfica en certificación WCAG ni cambiar colores.

## 10. Design tokens

Los nombres, valores, modos, scopes, description y codeSyntax se delegan únicamente al [JSON identidad](tokens/ai-design-system.character-identity.v0.1.0.json) y [JSON sombra](tokens/ai-design-system.character-shadow.v0.1.0.json). Scope SHAPE_FILL, colección character-identity, modo Value, valores directos sin alias por DEC-CHARACTER-IDENTITY-001. Cuerpo BENI → color/characters/beni/body; NAVI → color/characters/navi/body; ojos/bigote → color/characters/shared/features; sombra lateral → color/characters/navi/shadow. Conservar pinturas vacías, no convertirlas en negras. Tokens preexistentes leídos en [preflight](../implementations/figma/characters.v0.1.0.preflight.json). No consumir color/brand.

Inventario base sources/inventories/tokens.inventory.json, SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474, se conserva. Fondo de muestra usa color/background/default y separación spacing/lg de semantic. Componentes transparentes, sin tipografía que tokenizar.

## 11. Content rules

Arte fijo; no strings ni contenido de demo dentro de los personajes. Nombres internos conservados para correspondencia de Smart Animate. No reducir la secuencia a una imagen rasterizada.

## 12. Composition rules

P-SLOTS NOT_APPLICABLE: anatomía ilustrativa fija, no listas ni regiones de contenido extensibles. Un grupo de ojos no es Slot. Se pueden insertar instancias de los sets en futuros consumidores bajo sus contratos; no se reemplazan los auxiliares actuales de Conversation/Chat en este alcance.

## 13. Responsive behavior

Conservar restricciones fuente y relación de aspecto; sin breakpoints inventados. QA incluye una instancia escalada proporcionalmente para comprobar que mantiene vínculos y geometría.

## 14. Edge cases

NAVI tiene capas de sombra sin relleno en varios frames: conservarlas. El frame 3 no existe en el set fuente y no rompe el bucle. Frame inicial es 01 para ambos; no prometer sincronización entre personajes.

## 15. Forbidden combinations

MUST NOT tematizar personajes, usar primitivas UI directas, añadir semánticos intermedios de identidad, recolorear por contraste, apuntar reacciones a IDs fuente, inventar fotogramas ni sustituir componentes previos ajenos.

## 16. Design ↔ Code mapping

Destino AI Design System tj3WIBEZDGLVs7MJWKCwgf, página Characters. Frame es propiedad de prototipo Figma, no API web comprometida. No frontend ni paquetes nuevos. IDs reales se registran tras construcción.

## 17. Acceptance criteria

AC-01/REQ-01: página única y 6+7 variantes con Frame. AC-02/REQ-02: readback de los 64 vectorPaths, dimensiones, posición relativa, grupos, fills vacíos y comparación visual; permitir solo precisión de serialización flotante hasta 0.001 px, criterio delegado declarado antes de construir. AC-03/REQ-03: 13 transiciones fieles, destinos locales, dos ciclos completos, tiempos exactos. AC-04/REQ-04–05: 47 bindings, cuatro tokens identidad con campos idénticos a JSON; tres existentes intactos; todos los modos de semantic mantienen los colores. AC-05/REQ-06: evidencia persistida, muestra de 13 instancias sin clipping, specs tras PASS, sin publicar biblioteca. SLOT-QA-01 PASS documental justificado; SLOT-QA-02–09 NOT_APPLICABLE a contenido fijo. Medición de contraste informativa, no certificación funcional.

## 18. Examples

Nota de validación API (2026-10-08): Figma normaliza `vectorPaths` al escribirlos, dividiendo/reordenando subpaths y serializando coordenadas flotantes. QA conserva el path fuente y compara el destino con su round-trip mediante un vector temporal eliminado tras la prueba, además de posición/dimensiones y revisión visual; no exige igualdad textual del SVG bruto. `AFTER_TIMEOUT=0.8` se devuelve como `0.800000011920929`; se acepta hasta 0.000001 s de serialización, sin cambiar la temporización de diseño. Esto aclara el método de evidencia, no autoriza simplificar el arte.

Instanciar BENI Standby / Frame 01 y NAVI Analysis / Frame 01 para iniciar sus bucles en prototipo. Elegir otro Frame solo cambia el punto inicial, no expresa un error de servicio.

## 19. Source of truth

Este contrato delegado gobierna integración, junto con sus JSON; el [contrato BENI fuente](../drafts/contracts/beni-standby.source.component-contract.md) y [contrato NAVI fuente](../drafts/contracts/navi-analysis.source.component-contract.md) son evidencia de solo lectura. Fuente externa IlNQJgDKvCSqyXAkONcjxl, sección 885:16275; [snapshot](../sources/figma-snapshots/characters.ecosistema.2026-10-08.json), [envolturas](../sources/figma-snapshots/characters.wrappers.2026-10-08.json). Aplican [delegación externa](../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md) e [identidad fija](../registry/DEC-CHARACTER-IDENTITY-001.md). Auditoría humana PENDING.

## 20. Change management

Una vez promovido, todo cambio normativo se versiona en specs. El JSON sombra es extensión aditiva: no sustituye los tres datos existentes ni el contrato Conversation; cada dato tiene un único propietario. QA invalida únicamente el alcance afectado.

## 21. Changelog

0.1.0 · 2026-10-08: primera integración delegada de BENI Standby y NAVI Analysis, 13 frames y una extensión de identidad NAVI. Construcción y QA técnico PASS: página 820:7, sets 822:6 y 822:7; revisión 822:21. Promovido a specs bajo delegación; auditoría humana PENDING, biblioteca UNPUBLISHED.

## Evidencia de implementación

[Estado e IDs](../implementations/figma/characters.v0.1.0.final.json), [QA técnico](../qa/implementations/characters.v0.1.0.review.md), [readback](../qa/implementations/characters.v0.1.0.audit.json), [captura](../implementations/figma/characters.v0.1.0.png). La muestra es organizativa; no altera los componentes. Inventario base y JSON de identidad previo permanecen intactos.
