---
contract_id: SIX-FAMILY-COLOR-001
version: 0.1.0
status: DELEGATED_FOR_BUILD
user_audit: PENDING
last_updated: 2026-10-05
decision_refs: [DEC-MIGRATION-VISUAL-FIDELITY-001, DEC-MIGRATION-NEAREST-PRIMITIVE-001, DEC-SEMANTIC-EXTENSIONS-001]
---

# Enmienda cromática · seis familias

## Autoridad y alcance

El usuario solicita ejecutar el punto 1, revisión de colores, tokens y bindings de Buttons, Icon Buttons, Breadcrumbs, Metric Cards, Charts y Linear Progress Bars. Esta enmienda aplica la fidelidad cromática delegada y el uso de primitivas existentes; no cambia aprobaciones humanas, anatomía, tipografía, variantes, comportamientos ni publicación remota.

Sustituye exclusivamente las recetas de color afectadas de BUTTON-001@0.2.0 (baseline técnico0.1.0; conserva las enmiendas0.2.1/0.2.2), ICON-BUTTON-001@0.1.0, BREADCRUMBS-001@0.1.0, METRIC-CARD-001@0.1.0, CHARTS-001@0.1.0 y LINEAR-PROGRESS-BAR-001@0.1.0. En Breadcrumbs §§10/15/17/20, Metric §§10/15/17/20, Charts §§10/20 y Progress §§10/17/20 queda sustituida la exigencia de oscurecer colores para alcanzar un umbral. Se mide y marca la limitación; no se afirma cumplimiento WCAG.

El [JSON de extensión](../tokens/ai-design-system.six-family-color.v0.1.0.json) es la única definición vigente de los doce roles enumerados (ocho existentes, cuatro nuevos): nombres, valores por modo, aliases, scopes, codeSyntax y description. Sustituye esos campos de las extensiones históricas de Breadcrumb Current, Metric roles, Chart colors y Linear Progress colors0.1.0. No modifica el inventario histórico ni los demás tokens.

## Fuentes y evidencia

Fuente Figma: `9zs5RMR8LB5wHjW9Bd59BA`. Destino: `tj3WIBEZDGLVs7MJWKCwgf`. Lecturas completas de pinturas sólidas activas por nodo, incluidos descendientes ocultos, en `qa/implementations/{buttons,icon-button,breadcrumbs,metric-card,charts,linear-progress-bar}.color.v0.1.0.{source,before}.json`. El script `six-families.color.v0.1.0.snapshot.js` conserva consumidores exactos y fingerprints de geometría/API. Las colecciones se resuelven por nombre de modo, no reutilizando IDs fuente como destino.

| Familia | Raíces fuente → destino | Cambio requerido |
|---|---|---|
| Buttons |355:86695→26:81| Default/Hover y Text/Hover usan hover-bg; Default/Press reutiliza color/interactive/secondary/active; Text/Focus conserva fondo transparente; los doce bordes Focus usan color/focus/ring existente. Tres bordes Default/Default usan control/subtle. |
| Icon Buttons |1430:18850→183:311| Seis bordes Outline Default/Active usan control/subtle. Las demás recetas conservan colores y roles locales. |
| Breadcrumbs |2425:35897/2425:35937→190:210/191:229| Current en Servicios vuelve a orange/500. Cinco consumidores, incluidas las composiciones con Slot. |
| Metric Cards |587:2751→202:327| Trend y los dos iconos vuelven a orange/500 en Servicios; dos bordes V2 usan control/subtle. |
| Charts |3086:992/2977:2066/3075:871/3086:1090/3075:764→210:145/210:171/213:161/211:134/213:162| Avance vuelve a marca base; pista Gauge usa la escala300; serie2 vuelve al acento200; swatch neutro aliasa neutral/300. Separar leyenda restante de pista Gauge y usar legend-accent en las celdas secundarias ocultas. Las copias de leyenda en Top mantienen el mismo mapeo que Detail. |
| Linear Progress Bars |7596:48397→220:460| Primary en Servicios vuelve a orange/500. Pista y otras tres intenciones conservadas. |

## Semántica y decisiones concretas

El borde fuente de las tres familias citadas resuelve `#FFBBB0` en Servicios. Existe exactamente como `color/red/200` en el JSON y en Figma: se encapsula en **color/border/control/subtle**, sin modificar el rol global color/border/subtle (orange/200), ni señalar error funcional. Los otros tres modos conservan los tonos200 de marca. No es una aproximación ni una primitiva nueva.

El gris fuente `#D9D9D9` no existe en las primitivas. Entre los81 colores primitivos, neutral/300 `#E2E8F0` obtiene la menor distancia euclídea sRGB8 (28.8964), y conserva uso neutral. Se aplica mediante **color/shape/chart/legend-neutral**, nunca por primitiva directa. Diferencia y contraste quedan documentados para auditoría; no se oscurece a neutral/500.

El nuevo fondo Button de Hover evita reutilizar un token Active por igualdad RGB; Default/Press sí reutiliza el Active existente por intención y color. La leyenda remaining usa escala100; Gauge track usa escala300: compartir nombre conceptual de restante no autoriza igualar sus colores. No se cambian el80% de demo ni las reacciones de Buttons.

## P-SLOTS

Buttons, Icon Buttons, Metric Cards y Linear Progress Bars: NOT_APPLICABLE para esta anatomía fija. Breadcrumbs y Charts: REQUIRED/IMPLEMENTED por las enmiendas composition-slots0.1.0/0.1.1. Se preservan Slots nativos, propiedades y contenido, sin sustituirlos por frames ni duplicar variantes. El cambio de pinturas no cambia cardinalidad.

## Aceptación

1. Doce roles de extensión coinciden con Figma en description, scope y aliases de cuatro modos; cero primitivas creadas y cero cambios en JSON histórico.
2. Todas las pinturas leídas de las seis familias resuelven a variables locales de scope/categoría correcta. Mapa consumidor→rol persistente, incluyendo contenido oculto de leyendas.
3. Colores contrastados con la fuente, distinguiendo el gris aproximado y las extensiones Slots sin equivalente fuente directo.
4. Fingerprints de geometría, propiedades y reacciones anteriores/posteriores coinciden; IDs originales conservados. Lectura independiente posterior y capturas revisadas.
5. Contraste real registrado con asterisco cuando corresponde, sin borrar las limitaciones anteriores ni afirmar una auditoría integral de accesibilidad.
6. QA y estado por familia actualizados; auditoría humana PENDING y biblioteca no publicada por esta operación.
