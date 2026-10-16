# QA-BUTTON-FIGMA-001 · preflight de implementación

```yaml
qa_id: QA-BUTTON-FIGMA-001
review_type: IMPLEMENTATION_REVIEW
contract_ref: BUTTON-001
contract_version: 0.1.0
contract_digest: 4b94f80787c1fc9d9990f806c99900e17db060e65b624471b0c8d93f534f2abb
implementation_ref: IMP-BUTTON-FIGMA-001
target: figma
scope: lectura parcial previa a toda modificación del set existente y su página
blocked_items:
  - nombre canónico y operación de página pendientes de decisión
  - readback visual, jerarquía detallada y destinos de reacciones aún no completados
  - QA final debe repetirse después de la última modificación
accepted_deviations: []
reviewer: Codex
executed_at: 2026-09-23T00:51:28Z
result: BLOCKED
```

La aprobación documental consta en `DEC-BUTTON-001`. Este informe no declara implementación `VALIDATED` ni acredita una escritura en Figma.

| Criterio | Resultado | Lectura real y límite |
|---|---|---|
| AC-BTN-001 | PASS | Set `26:81` conserva 60 variantes, ejes `type` (4), `size` (3) y `state` (5). |
| AC-BTN-002 | PASS | Ocho definiciones nativas: dos Boolean, texto, dos INSTANCE_SWAP y tres ejes VARIANT; defaults coinciden con el contrato. |
| AC-BTN-003 | BLOCKED | Conteos de 60 textos y 120 instancias coinciden; falta comparar toda la jerarquía y el wrapper focus/default. |
| AC-BTN-004 | BLOCKED | Los tamaños, gaps y los 35 IDs de variables vinculadas coinciden exactamente con el YAML aprobado como evidencia; falta comparar todos los bindings por propiedad, visuales y tipografía por variante. |
| AC-BTN-005 | PASS | Ambos swaps tienen default `26:3` y las 120 instancias actuales resuelven a la misma key principal de PlusCircle. |
| AC-BTN-006 | BLOCKED | Se cuentan 23 reacciones, como en la fuente; faltan readback de triggers y destinos individuales para QA final. No se corrigieron ni completaron. |
| AC-BTN-007 | BLOCKED | El set es el único nodo superior de la única página actual `Page 1` (`0:1`), pero el contrato exige nombre canónico de familia aún no decidido. No se renombró ni movió. |
| AC-BTN-008 | NOT_APPLICABLE | Web queda fuera del alcance Figma; la exclusión está documentada en el contrato aprobado. |
| AC-BTN-009 | PASS | 120/120 instancias resuelven a key `46d251bb4099700c5852180f2370d265e5166432`, la misma de la variante en `SRC-FIGMA-PHOSPHOR-001`. |

## Medidas verificadas

| Size | Variantes | Alto | Anchos observados | Texto | Icono | Gap |
|---|---:|---:|---|---:|---:|---:|
| large | 20 | 48 px | 154, 135 px | 16 px | 24 px | 8 px |
| middle | 20 | 40 px | 146, 127 px | 16 px | 20 px | 8 px |
| small | 20 | 32 px | 139, 120 px | 14 px | 20 px | 8 px |

Los anchos corresponden al contenido de ejemplo; no se infirió un ancho fijo. El cotejo de 35 IDs se hizo sobre todos los nodos del set (364 incluido el contenedor) y el inventario `variable_dependencies` del [YAML](../../drafts/contracts/button.contract.yaml): sin IDs faltantes ni extra. No se alteraron nodos Figma.
