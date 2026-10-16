---
contract_id: CHAT-TOOLBAR-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
figma_page_name: Chat
target_file_key: tj3WIBEZDGLVs7MJWKCwgf
slot_applicability: REQUIRED
---

# Chat Toolbar · contrato de construcción

## 1. Purpose

Integrar el sidebar conversacional fuente20355:72872 junto con sus dependencias locales Options and Tools20355:72830 y ChatHistory20355:72852. Delegación externa vigente; no migrar el archivo Anticipa completo.

## 2. Contract

CT01 dos variantes Expanded=false/true. CT02 dependencias reutilizables Chat Tool Item (3) y Chat History Item (4). CT03 página Chat783:6 existente. CT04 roles locales, aliases canónicos y Slots reales. CT05 fuente intacta; QA, specs y grafo trazables. No publicación remota ni frontend.

## 3. Anatomy

Header con logo Anticipa y control de expansión; región central con Tools and actions, Indicators y Chats; plan Pro Plan con uso42/150 y28%. Colapsado conserva regiones ocultas para no perder contenido al expandir; solo muestra control. Sin personaje ni nueva excepción de identidad.

## 4. Properties

Expanded VARIANT false/true; Show indicators BOOLEAN=false; Show plan BOOLEAN=true; Header, Tools and actions, Indicators, Chats SLOT. Textos de encabezados Indicators title y Chats title TEXT, Plan name TEXT. Los textos dentro de Slots se editan en el contenido o en propiedades del componente hijo, no referencias cruzadas del anfitrión.

## 5. Variants

Dos variantes Toolbar, tres Tool Item y cuatro History Item. No variantes por cantidad de chats, tema o consumo. Las dependencias se definen en sus contratos enlazados.

## 6. Sizes

Toolbar79×791 colapsado y264×791 expandido; minHeight791, altura HUG para contenido extenso. Padding16 y gap32; referencia expanded Header232×32, cuerpo232×519 y plan232×144. Ancho expandido264–310, colapsado79–93. Borde únicamente derecho1px. Región central minHeight519 en expanded; overflow no recorta. Plan padding16/gap16, radio16; progreso200×8 en referencia.

## 7. States

Expanded es presentación, no disponibilidad. Indicadores ocultos de inicio. No inferir Disabled global del organismo. Selección de historial es independiente de hover y conserva texto/acciones.

## 8. Behavior

Control de32 contiene Icon Button Ghost Small24 de DS (icono16), sin count. Reacción ON_CLICK entre variantes locales con Smart Animate300ms EASE_OUT. Hover de dependencias respeta pares locales. No navegación, creación de chat, anclado, menú o consumo de IA implementado. Demostración estática42/150=28%; fill56/200 corrige94/200 fuente. La barra usa constraints proporcionales al ancho; no calcula textos desde datos. El consumidor debe actualizar cantidad, porcentaje y geometría conjuntamente; no exponer una propiedad que sugiera cálculo automático.

## 9. Accessibility

No certificación WCAG. Documentar contraste por cuatro temas y limitaciones con asterisco sin cambiar paleta. Implementación futura debe aportar nombres accesibles, foco/teclado y alternativa a acciones solo hover. No inventar variantes Focus no presentes. Esto no impide uso de propiedades visuales.

## 10. Design tokens

[JSON base](../sources/inventories/tokens.inventory.json), SHA256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474. [Preflight](../implementations/figma/chat-toolbar.v0.1.0.preflight.json) y [verificador](../qa/contracts/chat-toolbar.verify-preflight.cjs):36 roles/144 aliases PASS.

|Parte|Rol|
|---|---|
|Superficie / plan|color/background/default|
|Separador derecho|color/border/strong; neutral300 #E2E8F0, aproximación al #E5E7EB fuente, sin semántica Disabled|
|Control expansión|color/surface/brand|
|Texto / metadatos / títulos secundarios|color/text/primary, secondary, tertiary|
|Plan texto/icono|color/text/brand, color/icon/brand|
|Tool Hover / History Hover|color/interactive/secondary/hover|
|History Selected|color/surface/brand|
|Tool Disabled texto/icono|color/interactive/disabled/text, color/icon/disabled|
|Iconografía neutra|color/icon/primary|
|Barra / pista|color/background/progress/primary, track|
|Tipografía|font/family/base; font/weight/regular,medium,bold; font/size/xs,sm,md; font/line-height/sm; font/letter-spacing/normal|
|Espacios/radios|spacing/none,xs,sm,lg,2xl; radius/md,xl,full|

Fuente normativa de pista: [extensión original](../drafts/foundations/ai-design-system.linear-progress-colors.v0.1.0.json); primary: [extensión vigente](../specs/tokens/ai-design-system.six-family-color.v0.1.0.json), que la sustituye solo donde enumera. No tokens nuevos. Medidas estructurales79/264/310/791 no son escalones de tamaño ni primitivas cromáticas; permanecen geometría del contrato. Iconos16/24/32 pueden consumir size/lg,xl,2xl si sus valores cotejados corresponden. No duplicar description canónica.

## 11. Content rules

Nuevo chat×3, Chats×2 e Indicadores opcionales son muestras, no límites. Textos largos de etiquetas pueden envolver y aumentar altura; historial reserva zona de acciones/metadatos. La fuente tenía textos truncados manualmente; contenido completo editable y ellipsis cuando se limite una línea debe definirse explícitamente, no inferir límite de caracteres. Plan name editable; consumo demo estático.

## 12. Composition rules / Slots

P-SLOTS REQUIRED. Header horizontal con logo/control predeterminados; Tools and actions vertical; Indicators vertical; Chats vertical. Sin min/maxChildren, contenido puede agregarse/quitarse/reordenarse/sustituirse desde instancia sin detach. Encabezados de regiones fuera de Slots para no contar como ítems. Los Slots existen en ambas variantes; se ocultan regiones colapsadas sin eliminarlas. La instancia puede reemplazar el Header; si quita el control, Expanded sigue editable en propiedades. Reglas de Slots de hijos en contratos específicos.

## 13. Responsive behavior

Anchos desktop documentados; no breakpoint móvil. Regiones FILL horizontal/HUG vertical. Toolbar crece si excede minHeight; scroll queda a pantalla anfitriona. Plan usa espacio restante inferior mediante región central mínima; no superponer listas largas sobre el plan.

Header permite WRAP con gap vertical8. Dependencias: Extra actions HUG/maxWidth64 y Actions HUG/maxWidth96 permiten WRAP/gap vertical8 para que más iconos crezcan en altura. Estos anchos son medidas de composición, no límites de cantidad. Colapsado fija Content region a695px mientras Expanded content permanece oculto; evita que la altura residual de hijos invisibles expanda la barra.

## 14. Edge cases

QA 0/1/3/5 hijos, reorder/replace, override entre variantes, texto largo, ancho264/310, cuatro modos. Cinco es prueba, no máximo. Slot vacío permitido sin inventar mensaje de producto.

## 15. Forbidden combinations

No variables fuente/remotas en UI destino, no text token en shape, no colores literales fuera de logo agnóstico. No instancias desconectadas, no editar principales existentes de Sidebar/Icon Button/Logo. No sustituir el28% por variante25% de Linear Progress Bar ni modificar su matriz compartida.

## 16. Design ↔ Code mapping

Figma y MD solamente. Fuente propia para organismo y dependencias; sistema existente gobierna roles y controles reutilizados. Native Slots no prueban implementación React o accesibilidad operativa.

## 17. Acceptance criteria

Nueve variantes públicas totales, propiedades editables, Slots efectivos, efectos/reacciones locales, cadena de tokens verificada, geometría sin recortes, evidencia visual y QA. PASS técnico no equivale a aprobación humana ni publicación Figma.

## 18. Examples

Muestra compacta con instancia expandida/colapsada y dependencia por estado; principales fuera de muestra, a partir de zona libre y sin mover componentes existentes.

## 19. Source of truth

[Fuente Toolbar](../drafts/contracts/chat-toolbar.source.component-contract.md), [Tool Item](./chat-tool-item.contract.v0.1.0.md), [History Item](./chat-history-item.contract.v0.1.0.md), [delegación](../registry/DEC-EXTERNAL-COMPONENTS-DELEGATION-001.md), [Icon Button](../specs/icon-button.contract.v0.1.0.md), [Logos](../specs/components/logos.scope.amendment.v0.1.1.md). Logo434:3979 se reutiliza con altura24 y ancho74.49 proporcional, no se recolorea. Iconos Phosphor por keys observadas; MagicWand Outline Regular sustituye representación Stroke Regular sin cambiar peso/grafía y permite rol icon/brand SHAPE_FILL correcto.

## 20. Change management

Borrador inicial sintetizado desde evidencia; esta versión queda DELEGATED_FOR_BUILD por decisión registrada y QA documental. Promover a specs al cerrar QA; posteriores cambios allí versionados. Grafo completo se sincroniza al cierre del lote según P05§8.

## 21. Deviations and readiness

Homologaciones previas a escritura: semánticos temáticos sustituyen colores fijos; History Selected usa superficie de marca en vez de violeta fijo; metadatos adoptan jerarquía neutral DS; espaciado tipográfico normal. Source PARTIAL por alias históricos/remotos; no son dependencia del mapeo destino. Reutilización Icon Button24 dentro de32 conserva hitbox de ejemplo; iconografía Phosphor por key. Se añade propiedad de texto y Slot de acciones donde faltaban, sin inventar acciones de producto. Discrepancia47→28% documentada. Preparación READY tras preflight y QA documental; implementación aún NOT_STARTED al redactar.

## 22. Cierre técnico · 2026-10-08

QA documental e implementación PASS. [Evidencia y límites](../qa/implementations/chat-toolbar.v0.1.0.review.md), [IDs y lectura final](../qa/implementations/chat-toolbar.v0.1.0.final.json). PáginaChat783:6; Toolbar798:284, Tool Item796:494, History Item796:495; revisión798:290. Nueve variantes;36 roles/144 aliases sin variables nuevas. Esta sección actualiza el NOT_STARTED de la preparación histórica: implementación VALIDATED para el contrato visual, user_audit PENDING por excepciones. Promovido a specs; ajustes posteriores aquí. Biblioteca remota no publicada.

