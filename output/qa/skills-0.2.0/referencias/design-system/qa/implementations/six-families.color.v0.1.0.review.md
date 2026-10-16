# QA cromático · seis familias · 2026-10-05

Resultado: **PASS técnico acotado a pinturas sólidas, roles, aliases y bindings**, bajo [enmienda SIX-FAMILY-COLOR-001](../../specs/components/six-family-color.amendment.v0.1.0.md). No constituye aprobación humana ni auditoría global de accesibilidad. No se publicó la biblioteca.

## Cobertura comprobada

| Familia | Definiciones | Pinturas incluidas | Geometría/API |
|---|---:|---:|---|
| buttons | 60 | 243 | Sin cambios |
| icon-button | 30 | 159 | Sin cambios |
| breadcrumbs | 10 | 38 | Sin cambios |
| metric-card | 8 | 70 | Sin cambios |
| charts | 23 | 82 | Sin cambios |
| linear-progress-bar | 48 | 240 | Sin cambios |

832 pinturas, incluidas16 ocultas de Charts. Cero pinturas sin variable, remotas, fuera de scope o categoría.84 definiciones consumidas y su cadena de primitivas comparadas con los JSON canónicos (description, scopes, codeSyntax, aliases por modo y RGB primitivo); cero discrepancias. Las doce definiciones de extensión usan48 aliases. El inventario histórico permanece idéntico.

## Cambios

- 42 bindings: Buttons24, Icon Buttons6, Metric Cards2, Charts10. Breadcrumbs y Linear Progress heredan por variables; no fue necesario reescribir sus nodos.
- Ocho roles existentes corregidos y cuatro nuevos: border/control/subtle, interactive/button/hover-bg, shape/chart/remaining y shape/chart/legend-accent. Cero primitivas añadidas.
- Durante preflight se creó un rol focus-bg innecesario por una correspondencia errónea entre estados fuente. Se retiró por su ID712:124 antes de vincularlo a nodos; Text Focus permanece transparente. Evidencia de alta y retirada conservada, no se considera una variable pendiente ni parte del contrato vigente.
- Se conservan179 definiciones, incluyendo el componente suelto de Header Charts; sus IDs, propiedades, geometría y reacciones mantienen fingerprints anteriores. Los Slots existentes y contenido adicional de Top no se reconstruyen.

## Fidelidad y límites del cotejo

La comparación agrupa pinturas por tipo de nodo, propiedad y RGB resuelto en los cuatro temas. En Buttons, Icon Buttons, Breadcrumbs, Metric Cards y Linear Progress Bars los multiconjuntos fuente/destino coinciden sin diferencias. Los42 cambios se aplicaron con IDs y precondiciones de binding individuales; en Buttons se cotejaron nombres de estado antes de aplicar. Esta prueba no afirma identidad de paths, tipografía ni de estructura entre archivos.

Charts: fuente70 pinturas y destino82. Las12 adicionales corresponden a la leyenda preservada/oculta en Top por Slots (seis textos, un avance, un restante y cuatro acentos). Las cuatro muestras grises fuente#D9D9D9 se aproximan mediante neutral/300#E2E8F0, distancia sRGB8=28.8964, la menor entre81 primitivas. El resto de la paleta coincide con las recetas observadas. Cero primitivas directas en consumidores.

Capturas revisadas de Buttons26:81, Icon Buttons183:311, Breadcrumb item190:210, Metric Cards202:327, Charts211:134/213:161/213:162 y Linear Progress220:460. Sin clipping ni regresión visual de layout observados. Capturas del tema resuelto Contable; la comprobación de cuatro temas es por aliases/RGB, no una galería de cuatro capturas. La transparencia se conserva. Los textos informativos de las seis páginas se leyeron y no contienen afirmaciones obsoletas de contraste.

## Contraste conservado

[Mediciones reproducibles](six-families.color.v0.1.0.verification.json), ratios derivados de sRGB. El asterisco indica limitación para revisión interna, no autorización de recolorear:

- Servicios: texto Current3.236:1*, Trend/iconos sobre sutil2.954:1*, segmento Primary/pista2.954:1*.
- Gauge avance/pista:1.650/2.267/1.938/2.796:1* por Contable/Administrativo/Servicios/Personas.
- Series2/blanco:1.558/1.706/1.320/1.498:1*. Neutro aproximado/blanco1.233:1*.
- Button Primary Press, texto blanco:3.368/2.615/1.670/2.262:1*. Default Servicios3.236:1*. Bordes suaves1.498–1.706:1*.

No se afirma cumplimiento de umbrales funcionales desde Figma. La aplicabilidad concreta de un criterio de accesibilidad depende del uso; se preserva la decisión de fidelidad del usuario.

## Evidencia y cierre

Antes/fuente/después por familia: archivos `*.color.v0.1.0.{before,source,after}.json` de este directorio. [Resultado consolidado](six-families.color.v0.1.0.verification.json), [comparación canónica](six-families.color.v0.1.0.canonical-after.json) y [estado persistente](../../implementations/figma/six-family-color.v0.1.0.state.json). Scripts de escritura y respuestas en implementations/figma. Hashes y verificación local en el manifiesto generado.

Los cinco contratos base antes en drafts fueron promovidos a specs con localizadores de compatibilidad, no copias normativas dobles. Buttons ya estaba en specs. Human audit:PENDING. Biblioteca:no publicada por esta operación. Quedan fuera de alcance los pendientes de Radio/Checkbox, Logos y decisiones del equipo.

