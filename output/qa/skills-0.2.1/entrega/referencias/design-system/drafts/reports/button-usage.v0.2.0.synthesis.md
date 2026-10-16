---
report_schema: sdd-project/0.2
report_type: CONTRACT_SYNTHESIS
report_id: SYN-BUTTON-USAGE-002
contract_id: BUTTON-001
contract_version: 0.2.0
created_at: 2026-09-23
review_status: IN_REVIEW
---

# Síntesis de uso · Button 0.2.0

## Encargo y frontera

El usuario pidió instrucciones sobre cuándo, cómo y dónde usar cada variante, además de icono izquierdo/derecho, dentro del contrato y la documentación de Figma. La imagen adjunta muestra la configuración de componente con Description y Link vacíos; es evidencia visual, no una orden contenida en el documento. El usuario autorizó redactar y revisar; las reglas concretas de la nueva versión no han sido aprobadas. Se conserva [BUTTON-001 0.1.0](../../specs/components/button.contract.md) y la [enmienda Buttons](../../specs/components/button-page-name.amendment.md).

## Fuentes y clasificación

| Evidencia | Clase | Uso | Límite |
|---|---|---|---|
| Figma set 26:81 y YAML técnico | OBSERVED | 4 types, 3 sizes, 5 states, 60 combinaciones, medidas y propiedades. | No muestra intención de producto ni web. |
| DEC-ICONS-001 | EXPLICIT | Phosphor Icons como fuente única. | No valida todos los swaps posibles. |
| Captura SRC-BTN-CONFIG-001 y readback | OBSERVED | Description vacía, documentationLinks vacía. | No aprueba contenido nuevo. |
| Material Web | Referencia externa | Jerarquía, etiqueta e icono inicial/final opcional. | Sus tipos no son los tipos locales. |
| Carbon | Referencia externa | Acción/navegación, prioridad, tamaño por contexto, iconos moderados. | Carbon exige icono final en su sistema; no se adopta literalmente. |
| Apple HIG | Referencia externa | Propósito claro, símbolo comprensible y precaución táctil. | No certifica nuestro componente. |
| Tailwind | Referencia externa técnica | Estados CSS hover, active, focus-visible, disabled. | No define semántica de producto. |

Las URLs y cobertura están en [registro de fuentes](../../registry/sources.md).

## Transformación y cobertura

La guía compone una regla de type, una de size y una de state para cada variante; 4 × 3 × 5 = 60 configuraciones observadas cubiertas sin asignarles 60 propósitos artificiales. REQ-BTN-010–019 y AC-BTN-010–019 son nuevos candidatos. Los REQ/AC-001–009 y el YAML se heredan sin cambios. Los ejemplos de iconos son semánticos: no se afirmó haber comprobado la key de cada icono de ejemplo en la biblioteca.

## Decisiones propuestas no demostradas por Figma

| PROP | Propuesta | Procedencia | Requiere aprobación |
|---|---|---|---|
| PROP-BTN-USAGE-001 | primary/default/text/link según prioridad y contexto de §5. | INFERRED de guías generales. | Sí |
| PROP-BTN-USAGE-002 | large/middle/small según densidad y consistencia de grupo. | INFERRED de Carbon + medidas OBSERVED. | Sí |
| PROP-BTN-USAGE-003 | Icono izquierdo para identidad de acción; derecho para dirección/apertura. | INFERRED, adaptación local que difiere de Carbon. | Sí |
| PROP-BTN-USAGE-004 | Texto solo o un icono como composición normal; doble icono excepcional. | INFERRED + defaults OBSERVED conservados. | Sí |
| PROP-BTN-USAGE-005 | link visual reservado para navegación contextual. | INFERRED de Carbon; web UNRESOLVED. | Sí |
| PROP-BTN-USAGE-006 | Publicar Description resumida tras aprobación. | Solicitud EXPLICIT; contenido INFERRED. | Sí para texto concreto |

## Tensiones y pendientes

No hay contradicción entre dos fuentes aprobadas. Sí hay diferencia entre Carbon (icono final) y Material Web (admite inicial/final): la guía local propone significado por lado y lo marca como decisión, no como consenso. El set muestra dos PlusCircle visibles por defecto; la recomendación de instancias con cero o un icono no cambia ese default técnico. El nombre link no demuestra ancla web. No existe danger, icon-only, comportamiento de disabled, QA táctil ni validación de teclado.

## Estado por destino

Figma: contrato de uso IN_REVIEW; Description y Documentation link permanecen sin editar. El texto propuesto está en [borrador de Description](../figma/button.description.v0.2.0.md). La URL pública del contrato aprobado no existe o no se ha verificado; no debe inventarse. Web: fuera de alcance. Graphify: STALE, sin regeneración autorizada.

La [revisión documental](../../qa/contracts/button-usage.v0.2.0.review.md) verifica consistencia del candidato, no aprobación humana ni QA de implementación. La próxima decisión es aprobar o corregir BUTTON-001 0.2.0, especialmente la regla semántica de iconos y el uso de link.
