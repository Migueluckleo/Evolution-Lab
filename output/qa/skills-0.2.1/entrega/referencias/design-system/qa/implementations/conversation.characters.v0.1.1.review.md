# QA · Conversation: identidad de personajes0.1.1

PASS técnico acotado. [Enmienda](../../specs/components/conversation.character-identity.amendment.v0.1.1.md), [JSON canónico de extensión](../../specs/tokens/ai-design-system.character-identity.v0.1.0.json), [readback](conversation.characters.v0.1.1.final.json), [escritura e instancias](../../implementations/figma/conversation.characters.v0.1.1.write.json).

- CHAR-01/02: tres variables COLOR directas, colección character-identity con modo único Value. Nombre, tipo, description, scopes, codeSyntax y valor coinciden exactamente con JSON; siete rellenos principales restaurados desde fuente y27 apariciones principales/instancias verificadas sin overrides divergentes.
- CHAR-03: las instancias de Response BENI/NAVI y selector Composer heredan sus respectivos colores.40 resoluciones de colores de personajes en cuatro temas coinciden con valores originales;324 pinturas UI muestreadas por colección siguen semánticas (incluye ocultas).
- CHAR-04: variables previas inalteradas; no se cambió ningún binding UI ajeno a personajes. No semánticos nuevos ni alias intermedio para identidad.
- CHAR-05: IDs y geometría de página intactos; vectorPaths y dimensiones de personajes iguales al preflight; doce Slots principales conservados (24 al incluir muestra). No detach ni nuevas variantes.
- CHAR-06: captura posterior revisada visualmente, BENI azul original y NAVI naranja original; rasgos grises. Sin cambios de estructura ni recortes. Clon temporal retirado, IDs en readback. Un primer QA excedió el límite de respuesta y no se confirmó su ejecución; la herramienta indicó rollback. Se repitió con un único clon y pasó.

Contraste de rasgos/cuerpo derivado de valores originales: BENI5.381:1; NAVI2.028:1*. Identidad gráfica fija, no se afirma WCAG ni se recolorea para elevar contraste. Fuente Anticipa intacta; inventario base intacto. La enmienda sustituye solo el alcance cromático de personajes del QA0.1.0; los demás controles anteriores siguen vigentes. Auditoría humana PENDING, biblioteca no publicada, grafo no regenerado.
