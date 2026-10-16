# QA-CHECKBOX-SOURCE-001 · fuente Checkbox

- **Resultado:** `PASS` documental para evidencia read-only, no aprobación del diseño destino.
- **Identidad:** archivo fuente `9zs5RMR8LB5wHjW9Bd59BA`, set `1221:28710`, key conservada, página `1144:34368`.
- **Cobertura:** traversal completo 86/86 nodos, 12/12 variantes, 24 textos ocultos, nueve instancias, 19 variables usadas y un estilo; cero reacciones. Captura 680×290 inspeccionada.
- **Dependencias:** tres componentes principales (Check, Minus, helper checkbox) localizados y resueltos; 14 variables locales y cinco remotas; un estilo local resuelto. Las alternativas no activas de iconos no se inventariaron. Los IDs de origen no se reutilizan como IDs destino.
- **Sincronización:** [MD](../../drafts/contracts/checkbox.source.component-contract.md) y [YAML](../../drafts/contracts/checkbox.source.component-contract.yaml) coinciden en matriz, conteos, anatomía, tokens y límites. YAML parseado y conteos 12/19/3/1 comprobados.
- **Separaciones:** nota de página como propósito observado; `Field Label` como ejemplo, no regla de contenido; foco visual observado, sin afirmar semántica o accesibilidad web. El uso de `spacing/6xl`/`spacing/2xl` en padding de presentación con scope GAP se deja como anomalía de origen, no se traslada a componente.
- **Pendiente:** contrato de reconstrucción, preflight de dependencias Phosphor y tokens destino, construcción y QA Figma. Auditoría humana posterior conforme a la delegación de migración.
