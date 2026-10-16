# Chat Toolbar · QA de implementación v0.1.0

2026-10-08 · PASS técnico acotado al contrato visual. Auditoría humana PENDING por excepciones; no publicación remota.

## Alcance y evidencia

[Contrato](../../specs/chat-toolbar.contract.v0.1.0.md), [Tool Item](../../specs/chat-tool-item.contract.v0.1.0.md), [History Item](../../specs/chat-history-item.contract.v0.1.0.md). [Readback final](./chat-toolbar.v0.1.0.final.json), [Slots](./chat-toolbar.v0.1.0.slots.json), [wrap/crecimiento](./chat-toolbar.v0.1.0.wrap.json), [contraste](./chat-toolbar.v0.1.0.contrast.json).

## Matriz de aceptación

- CT01–02 PASS: Toolbar798:284, dos variantes79/264×791; Tool Item796:494 tres186×40; History Item796:495 cuatro258×40. Nueve variantes públicas.
- CT03 PASS: páginaChat783:6 reutilizada; principales fuera de muestra798:290 de713×839. Fuente y principales DS reutilizados sin cambios.
- CT04 PASS:36 roles/144 aliases del preflight contra inventario base y extensiones vigentes.136 pinturas UI incluidas ocultas,48 visibles;21 textos visibles con cinco bindings tipográficos; sin errores.46 paints del logo agnóstico exentos. Variables154:125,13:18 y13:33 pertenecen a Count oculto heredado de Icon Button; no se modificó ni se recertifica Count visible.
- Slots PASS: Header/Tools and actions/Indicators/Chats, Extra actions y Title/Actions; inserción0/1/3/5, quitar, reordenar, sustituir y preservación tras cambios de variantes. El primer fixture de Extra actions intentaba insertar su propio componente recursivamente; se corrigió a iconos no recursivos y pasó. No era límite de cardinalidad.
- Layout PASS: Header WRAP, Extra actions max64 y Actions max96/WRAP; cinco iconos sin desborde horizontal. Fixtures264/310 con seis Tool Items y textos largos crecen1620/1360px; plan siempre posterior al contenido. Colapsado Content region fijo695 evita altura residual de región oculta.
- Temas PASS: plan e indicador resuelven marca Contable/Administrativo/Servicios/Personas. Native aliases, sin variables nuevas. Logo conserva colores propios.
- Prototipo: ON_CLICK expansión local y ON_HOVER dependencias; sin rutas remotas, backend, pin o menú inventados.
- Visual PASS: captura final corregida normal1×. Se corrigieron HUG transversal, visibilidad del plan en colapsado, borde neutral300 y radio16. Sin recortes en muestra; nombres largos envuelven intencionalmente.

## Limitaciones documentadas, no pendientes inventados

*Servicios: Pro Plan16px Bold sobre blanco3.236:1 y barra/pista2.954:1. Disabled2.564:1 conserva paleta; control no operable. No se declara WCAG PASS ni se recolorea. Metadatos4.759:1; texto Hover/Selected >10:1 en cuatro temas.

Uso demo42/150=28%, tramo56/200. No cálculo automático; reemplazar datos exige sincronizar texto/longitud. MagicWand Outline Regular reutiliza equivalente de contorno; no se aplica token de fill a stroke. Fuente PARTIAL por aliases históricos; fuente y destino claramente separados.

Se retiraron únicamente fixtures temporales creados en esta ejecución; su evidencia queda guardada. No se borraron componentes del usuario. Los scripts build conservan fases históricas; readback final y contratos specs gobiernan el resultado, no IDs de una receta inicial.
