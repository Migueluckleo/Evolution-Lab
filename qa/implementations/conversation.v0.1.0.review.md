# QA-CONVERSATION-FIGMA-001 · 2026-10-08

Resultado: **PASS técnico acotado** para [CONVERSATION-001 v0.1.0](../../specs/conversation.contract.v0.1.0.md). No aprobación humana, no certificación de accesibilidad, no backend ni publicación remota.

## Evidencia y cobertura

- [Lectura final](conversation.v0.1.0.final.json): siete principales,179 nodos incluidos ocultos,124 pinturas; cero paints sin token, variables remotas o scopes de color incorrectos.22 textos propios/acciones/dependencias con los cinco bindings tipográficos; nueve textos Count Small ocultos conservan excepción contractual Dot.
- [Tokens](conversation.v0.1.0.tokens-verification.json):40 roles,38 primitivas,160 aliases; description, scopes, alias por nombre y valores contra JSON base y dos extensiones vigentes. SHA256 base intacto cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474. [Script reproducible](conversation.v0.1.0.verify-tokens.cjs), ejecutar desde raíz.
- [Cuatro temas](conversation.v0.1.0.themes.json):216 resoluciones de paints en clones consumidores de la muestra, sin errores de scopes/localidad; burbuja, glifos y acciones siguen la marca. No hay variables nuevas.
- [Slots](conversation.v0.1.0.slots.json): doce Slots nativos. Vacío, uno, cantidad de muestra y más que muestra; reordenar y sustituir sin detach ni violaciones; texto largo y ancho360. BENI→NAVI conserva override de Body. Pruebas sobre instancias temporales retiradas, no sobre originales. Se conserva anatomía mínima al vaciar; no se afirma colapso.
- Vista de referencia616px revisada visualmente (muestra680×775) y vista estrecha360×634 revisada tras completar bindings: textos legibles sin recortes, acciones envuelven y footer se ajusta. Cero desbordes horizontales detectados. Propiedad Message text y booleanas probadas en consumidores; fuentes Manrope cargadas para edición.
- Siete componentes principales y set Response de dos variantes; las cuatro configuraciones públicas se conservan. Textos internos de Slots editables directamente, no falsas propiedades expuestas. Estilos propios Body/Emphasis/Caption/Preview title permanecen aplicados.

## Correcciones y límites

Dos intentos iniciales rechazados por API no dejaron página ni estilos: exposición dentro de Slot y referencia a propiedad de anfitrión en subcapa de Slot. Se corrigió contrato antes del build exitoso. Tras el build se corrigió HUG vertical de contenedores horizontales, se combinó Response y se creó muestra. Se añadió tracking normal a cuatro textos de Buttons en instancias de Conversation, sin modificar maestros DS. El script build inicial no es una reconstrucción completa del resultado final: composición y correcciones quedan registradas separadamente.

El primer audit compacto omitía subcapas de instancias ocultas; el [audit ampliado previo a corrección](conversation.v0.1.0.all-nodes.audit.json) y lectura final incluyen todo. Las nueve excepciones de Count Small derivan de [Dot](../../specs/components/dot.contract.v0.1.0.md), no se ocultan como bindings completos. Show count=false; tamaños4px no homologables a escala existente sin cambiar el asset.

[Contraste calculado](conversation.v0.1.0.contrast.json)*: Servicios3.236:1 para textos de marca/acción primaria; bordes sutiles1.320–1.706:1 y divisor1.233:1. Se conservan los tokens del DS; no se cambia paleta ni se declara WCAG PASS. Iconografía de agentes usa brand/on-brand, badges neutrales y controles de tamaño DS según homologación delegada, no fidelidad cromática exacta a Anticipa.

Todos los nodos temporales de Slots, temas y vista estrecha se retiraron; sus IDs están en evidencia. Fuente Anticipa inalterada. Auditoría humana PENDING por excepciones; biblioteca UNPUBLISHED; Graphify STALE para Conversation (no regenerado, fuera del alcance actual).

AC01–08 PASS dentro de este alcance: anatomía y destino, dependencia local, tokenización con excepción Dot declarada, aliases/temas, Slots, edición, captura/reflow y trazabilidad.
