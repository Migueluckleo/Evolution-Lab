# QA-BADGE-FIGMA-001 · hallazgo de contraste antes de la corrección

```yaml
qa_id: QA-BADGE-FIGMA-001
review_type: IMPLEMENTATION_REVIEW
contract_ref: BADGE-001
contract_version: 0.1.0
implementation_ref: IMP-BADGE-FIGMA-001
target: figma
result: FAIL
executed_at: 2026-09-23
```

La construcción inicial contiene seis variantes, doce instancias Presentation con key correcta, 1512 opciones preferidas por swap, propiedad TEXT y dos booleanas conectadas, 26 tokens semánticos y 104 aliases token×modo verificados. La captura de 582×105 muestra las seis apariencias sin recortes aparentes. La variante Light mide 64×25 en destino frente a 62×25 en fuente porque el trazo interior suma 1 px por lado al ancho HUG; se conserva padding y stroke tokenizados.

El cálculo de contraste sobre colores resueltos en los cuatro modos detectó 3.61:1 en texto/icono Informational y 2.96:1 en texto/icono Warning. Para el texto de 12 px, esto no alcanza la referencia 4.5:1 de [WCAG 2.2 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); el icono Warning tampoco llega a 3:1 de [1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Los demás textos quedaron entre 4.59:1 y 17.85:1. Por tanto, la fase final de mejores prácticas no pasa y el estado permanece `VALIDATING` hasta corregir y releer.

El primer barrido de paints marcó 12 fills de contenedor de instancia; la lectura directa mostró `visible:false` en esos fills. Los doce vectores internos visibles están vinculados a variables locales; no se necesita mutación para esos contenedores. El primer auditor también trató referencias tipográficas tipo array y stroke por lado como objetos simples; la lectura corregida confirmó 30/30 bindings tipográficos, 4/4 lados de stroke y 12/12 vectores.
