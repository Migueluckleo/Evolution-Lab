# QA-CHAT-SECTION-IMPL-001 · 2026-10-08

PASS técnico acotado de [CHAT-SECTION-0010.1.0](../../specs/chat-section.contract.v0.1.0.md), sin certificar accesibilidad web ni comportamiento backend. Dos variantes Chat Section, dos Chat Suggestion y un auxiliar gráfico. Fuente sin modificar; sin cambios a maestros Conversation ni tokens nuevos. Dos estilos nuevos Chat/Title y Chat/Subtitle; Conversation/Body reutilizado.

AC01/02: página Chat783:6, sets784:98/784:96, auxiliar783:9, revisión784:99. Instancias de Conversation765:271/397 y glifos765:249/254, no detach ni clones de sus maestros. El principal Message/Composer conserva sus propios Slots/contratos.

AC03/04: [auditoría de pinturas/textos](chat-section.v0.1.0.final.json),62 paints visibles y13 textos visibles, cero errores de scope/rol, cinco bindings tipográficos. [Cotejo canónico](chat-section.v0.1.0.tokens-verification.json):39 roles,156 aliases, tres variables de identidad, descripción/scopes/tipos/valores coincidentes. Inventario base SHA256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474 preservado. Seis Count Small ocultos conservan tipografía literal heredada y documentada; no se certifican visibles.

AC05/P-SLOTS01–09: cuatro Slots propios, dos por variante. [Prueba desde instancias](chat-section.v0.1.0.slots.json) verifica0/1/3/5, insertar/quitar/reordenar/sustituir y conservación entre variantes. Las medidas dentro de esa transacción son provisionales: gobierna el readback asentado en final.json. Cinco sugerencias con texto largo: Slot480px/host1093.74px; cinco mensajes: Slot652px/host930px, sin overflow. Vacíos mantienen88/497px residuales, no política de estado vacío. Anchos574/782/1024 y nombre largo comprobados. HUG vertical corregido antes de cierre.

AC06: captura final del review784:99 contrastada con la fuente:pose/jerarquía y distribución conservadas; nombre temático, lectura completa estática y controles homologados son cambios documentados. No superposición ni recorte en muestra; no promesa móvil bajo574px. BENI conserva#41589B en cuatro modos; NAVI/features coinciden exactamente con JSON de identidad, sin aliases temáticos.

AC07: fuenteMD/YAML, snapshots, contrato, scripts/readbacks y registros persistidos. Publicación documental en specs; DELEGATED_FOR_BUILD/user_auditPENDING. No publicación remota Figma ni implementación frontend. Grafo se verifica por el run2026-10-08-chat-section, sin asumir vigencia antes del gate.

Contraste*: Default Servicios3.046:1; Hover3.567/3.476/2.451/4.223:1 en Contable/Administrativo/Servicios/Personas. Mantener paleta como indicó el usuario y revisión interna por excepción. No WCAG PASS. Controles anidados conservan excepciones de Conversation.

Incidencias de herramientas: lecturas sobredimensionadas se reemplazaron por lotes; prueba con método inexistente no comprometió cambios y se repitió con API documentada. La prueba final no contiene errores. [Cleanup](chat-section.v0.1.0.cleanup.json) confirma retirada de seis instancias temporales propias; quedan solo auxiliar, dos sets y review.
