# Chat · ajustes del usuario documentados · 2026-10-09

Solicitud explícita: revisar/documentar límites de width, scrolling y otros ajustes hechos por el usuario en Chat. No reparar Figma. [Enmienda vigente0.1.1](../specs/components/chat.layout.amendment.v0.1.1.md), [QA acotado](../qa/implementations/chat-layout.v0.1.1.review.md), [estado](../implementations/figma/chat-layout.v0.1.1.state.json).

Cambios confirmados: maxWidth816 en columna de ambas variantes; Active fijo733/columna683, Messages FILL y VERTICAL; Toolbar expandido FIXED y región central FILL sin mínimo519. Principales Section conservan minWidth574; muestras usan358. Standby conserva HUG/min775. Tokens de spacing existentes, sin crear variables ni modificar JSON. Slots conservados; no reconstrucción ni prueba mutante.

Leer enmienda junto a bases, no ejecutar recetas históricas para sobrescribir ajustes del usuario. Description Figma542 desactualizada,358 solo en muestras y scroll con clipsContent=false quedan documentados; no corregidos ni declarados aprobados. QA previo sigue histórico: no certifica el nuevo scroll ni las listas largas del Toolbar.

Grafo derivado sincronizado por lote según P05. Estado CURRENT únicamente si verification.json, manifest-check.json y closure.json de `graphify-out/runs/2026-10-09-chat-layout/` pasan y sus hashes coinciden; STALE/BLOCKED en caso contrario. No instalación, servicios externos, publicación de biblioteca ni cambios frontend.
