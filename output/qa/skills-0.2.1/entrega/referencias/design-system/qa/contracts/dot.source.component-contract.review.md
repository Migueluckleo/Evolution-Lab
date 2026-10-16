# QA-DOT-SOURCE-001 · fuente Dot

- **Resultado:** `PASS` documental de evidencia read-only, no aprobación de reconstrucción.
- **Identidad:** archivo fuente `9zs5RMR8LB5wHjW9Bd59BA`, set `1133:31549`, key conservada, página `1133:20620`.
- **Cobertura:** 22/22 nodos, 15/15 variantes 5×3, seis textos, cero instancias, 12 variables usadas (nueve locales, tres remotas), cero estilos nombrados y cero reacciones. Captura 201×290 inspeccionada.
- **Sincronización:** [MD](../../drafts/contracts/dot.source.component-contract.md) y [YAML](../../drafts/contracts/dot.source.component-contract.yaml) concuerdan en IDs, matriz, tamaños, colores, tipografía y dependencias; YAML parseado y conteos 15/15/12 verificados.
- **Conflicto de fuente:** la Description incrustada afirma que faltan variantes large de Busy/Inactive, pero los IDs `1241:39854` y `1241:39856` existen; tampoco hay evidencia de cambio automático a pill. Se prioriza estructura observada y se descartan esas afirmaciones como reglas.
- **Riesgos explícitos:** fondos de presencia y conteo están ligados a roles de icono; fuente usa texto de 4/8 px y no tiene propiedad TEXT. No se trasladan estos problemas silenciosamente al destino.
- **Pendiente:** extensión de roles de background, contrato de reconstrucción, QA documental, construcción y QA Figma. Auditoría humana posterior.
