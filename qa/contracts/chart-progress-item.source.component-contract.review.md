# QA-CHART-PROGRESS-ITEM-SOURCE-001

- **Resultado:** `PASS` de evidencia fuente; no aprueba destino ni comportamiento de datos.
- **Cobertura:** 40/40 nodos con `skipInvisibleInstanceChildren=false`, dos variantes, seis instancias locales `labelCell`, diez textos totales, 17 variables (16 locales/una remota), cero estilos y reacciones. Contrato de dependencia `labelCell` ya registrado.
- **Consistencia:** [MD](../../drafts/contracts/chart-progress-item.source.component-contract.md) y [YAML](../../drafts/contracts/chart-progress-item.source.component-contract.yaml) concuerdan en identidad, variantes, medidas, dependencia, propiedades y límites. YAML parseado; 2/6/10/17 conciliados.
- **Límites:** cuatro paints dentro de Dot ocultos por `spotVisible=false`; fuente usa rol de icono sobre el rectángulo Progress; las proporciones de barra no equivalen al ejemplo `80%`. Sin modificación del origen.
