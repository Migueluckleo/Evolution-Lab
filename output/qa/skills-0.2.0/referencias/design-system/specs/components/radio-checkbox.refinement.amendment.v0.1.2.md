---
amendment_id: AMD-RADIO-CHECKBOX-REFINEMENT-001
version: 0.1.2
status: DELEGATED_FOR_BUILD
applies_to: [RADIO-BUTTON-001, CHECKBOX-001]
base_contract_version: 0.1.0
last_updated: 2026-10-06
user_audit: PENDING
---

# Radio Buttons y Checkboxes · refinamiento 0.1.2

## Alcance y autoridad

Solicitud «Pasa al punto 2»: completar el cotejo de anatomía, tipografía y consumidores de ambas familias. Aplican DEC-LEGACY-MIGRATION-DELEGATION-001, DEC-MIGRATION-SPECS-AUDIT-001 y DEC-MIGRATION-NEAREST-PRIMITIVE-001. No añade variantes, comportamientos, primitivas, Slots ni publicación de biblioteca.

Esta enmienda complementa las bases RADIO-BUTTON-001 y CHECKBOX-001 0.1.0 y conserva los cambios cromáticos de sus enmiendas 0.1.1. Sustituye únicamente: coordenada vertical no especificada del icono Checkbox, afirmaciones históricas sobre contraste de bordes y obligación de radio tokenizado para elipses. El resto de reglas de ambas bases permanece.

## Requisitos comprobables

- REF-01: mantener ocho variantes públicas Radio, ocho de su dependencia local y doce Checkbox; IDs, propiedades y defaults existentes intactos. Controles 24×24, formas 18×18, centro Radio 8×8, iconos Checkbox 12×12 y radio Checkbox 4. Elipse circular se define por geometría 18×18/8×8; no exige un binding ficticio `radius/full` en Ellipse. Son geometrías fijas de indicador, no nuevas primitivas.
- REF-02: mantener la normalización tipográfica previamente delegada: Manrope Regular 14, interlineado 20 por `font/line-height/sm` frente a 18 fuente, tracking normal 0. Cuarenta etiquetas con cinco bindings tipográficos locales y color semántico; TEXT y BOOLEAN conectadas. Ancho de contenido, sin truncamiento impuesto; gap8 tokenizado y padding0. El inventario canónico no contiene interlineado18: no se añade una primitiva para simular coincidencia exacta.
- REF-03: preservar las instancias Phosphor Check/Minus y sus vectores. Corregir las ocho coordenadas de icono de Checkbox de y6 a y6.413887023925781, x6 dentro del indicador, según lectura local de la fuente. Esta posición es geometría literal del artwork; no se tokeniza como spacing de layout ni modifica la biblioteca Phosphor. El diferencial obtenido al restar transforms absolutos fuente es 6.41387939453125 por representación numérica; no se afirma identidad bit a bit de transforms globales ni se inventa una tolerancia.
- REF-04: conservar Radio seleccionado como discos concéntricos18/8, equivalentes al stroke5 fuente; helper de ocho estados frente a overrides de origen. Checkbox usa anatomía directa en lugar del helper singular de Unselected/Focus, y elimina grupos redundantes sin desvincular Check/Minus. Son decisiones delegadas previas, no defectos nuevos ni prueba de identidad de jerarquías.
- REF-05: mantener los contornos neutral/400 restaurados por 0.1.1 y las limitaciones con `*`; no exigir ≥3:1 para declarar fidelidad ni oscurecerlos. Mantener el halo interior blanco tokenizado frente a #F8FAFC fuente como aproximación ya documentada. La auditoría del equipo sigue separada del cierre técnico.
- REF-06: probar desde instancias temporales las cuatro combinaciones de etiquetas, edición de texto largo y cambio de variante, sin detach, pérdida de propiedades o superposición. Retirar exclusivamente las instancias temporales identificadas. La prueba no acredita comportamiento web.

## Slots · P-SLOTS 0.1.0

`NOT_APPLICABLE` para ambos controles individuales: anatomía fija de un indicador y dos posiciones de etiqueta cuyo contenido se modifica mediante TEXT/BOOLEAN. No tienen región de lista ni composición abierta. Un grupo de opciones 0..n pertenece al componente anfitrión, no a este control. No se añaden Slots artificiales.

## Fuentes y datos

Origen: Librería `9zs5RMR8LB5wHjW9Bd59BA`, Radio1230:24283 y Checkbox1221:28710; destino `tj3WIBEZDGLVs7MJWKCwgf`, páginas142:122/149:122 y sets142:144/143:166/149:199. Snapshots actuales `qa/implementations/radio-checkbox.refinement.v0.1.0.{radio,checkbox}-{source,destination}.json`; mapa real de variables `radio-checkbox.refinement.v0.1.0.tokens.json` en el mismo directorio.

Las definiciones siguen delegadas al inventario histórico `sources/inventories/tokens.inventory.json` y extensiones vigentes de control, selección y foco; esta enmienda no crea catálogo editable paralelo. Los snapshots son evidencia, no otro JSON normativo. El digest íntegro y calculado del inventario se registra en el manifiesto de QA.

## Cierre

Requiere QA documental, readback posterior a la corrección Checkbox, prueba de instancias y captura. Tras PASS, promover las bases y sus enmiendas cromáticas a specs con referencias corregidas; los borradores serán punteros de compatibilidad, sin segunda norma editable. Aprobación humana PENDING, publicación Figma no ejecutada.
