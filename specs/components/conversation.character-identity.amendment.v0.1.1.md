---
contract_id: CONVERSATION-CHARACTER-IDENTITY-001
version: 0.1.1
status: DELEGATED_FOR_BUILD
user_audit: PENDING
decision: DEC-CHARACTER-IDENTITY-001
slot_applicability: NOT_APPLICABLE
---

# Conversation · identidad cromática de BENI y NAVI

## Autoridad y sustitución

La instrucción EXPLICIT del usuario del 2026-10-08 exige preservar los colores originales de los personajes, agregarlos a tokens sin capa semántica y mantener ésta como única excepción nueva. Sustituye en [Conversation0.1.0](../conversation.contract.v0.1.0.md) exclusivamente REQ-CV-04, tabla de personajes de §10, prohibición de nuevos valores/consumo directo de §15 y afirmaciones sobre personajes temáticos de §§17,21,22. Sustituye la misma elección en DEC-EXTERNAL-COMPONENTS-DELEGATION-001. El resto de la interfaz conserva semántica, scopes, aliases y temas. Los QA anteriores de personajes son históricos, no válidos para esta instrucción hasta nueva verificación.

## Datos canónicos

[JSON de extensión](../tokens/ai-design-system.character-identity.v0.1.0.json) es la única definición editable de nombres, tipos, valores exactos, modos, description, scopes y codeSyntax de estos tres tokens. Complementa el inventario base, no altera sus bytes ni finge que los colores ya existían. Fuente [readback de Anticipa](../../sources/figma-snapshots/conversation.characters.original.2026-10-08.json): siete fills observados en los dos personajes. Ningún RGB aproximado ni valor derivado del tema.

Colección local `character-identity`, un modo `Value`, tres variables COLOR literales, no aliases. Son tokens de identidad gráfica, no roles semánticos de UI. Binding directo a rellenos vectoriales, scope SHAPE_FILL exclusivamente. La sintaxis WEB se deriva explícitamente del nombre para handoff; no declara un frontend implementado.

## Requisitos

- CHAR-01: BENI y NAVI usan exactamente sus colores originales de cuerpo y rasgos en todos los temas.
- CHAR-02: las siete pinturas principales se vinculan a los tres tokens locales de identidad; no icon/brand, icon/on-brand ni literales pegados sin variable.
- CHAR-03: Response y el selector de Composer heredan la corrección mediante sus instancias; comprobar posibles overrides de color.
- CHAR-04: burbujas, acciones, badges, texto y fondos restantes mantienen su tokenización semántica; no extender excepción a otros componentes, agentes futuros o iconos funcionales.
- CHAR-05: conservar geometría, vectorPaths, IDs, nombres, jerarquía y doce Slots. Actualizar descripciones que prometían personajes temáticos.
- CHAR-06: verificar los tres datos frente a Figma, exactitud de los siete colores y estabilidad en Contable/Administrativo/Servicios/Personas; captura final, sin publicación de biblioteca.

P-SLOTS: NOT_APPLICABLE al ajuste cromático de personajes de anatomía fija. Conversation mantiene REQUIRED/IMPLEMENTED y sus doce Slots con QA previo; se comprueba su conservación, no se repite su construcción.

## QA y cierre

QA documental previo: requisitos comprobables, colores observados, excepción autorizada, fuentes/JSON separados, IDs conocidos. Preparación READY para UPDATE acotado tras comprobar ausencia de colisiones en la colección. QA técnico se registra por separado; la delegación no implica auditoría humana del resultado.

Contraste de rasgos sobre cuerpo se registra sin recolorear. La identidad gráfica no certifica controles accesibles ni comportamiento web. Ninguna otra variable o componente compartido se modifica.
