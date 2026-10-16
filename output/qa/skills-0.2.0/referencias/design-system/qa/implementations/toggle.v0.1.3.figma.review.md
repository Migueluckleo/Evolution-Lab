# QA-TOGGLE-FIGMA-006 · corrección de efectos de foco

```yaml
qa_id: QA-TOGGLE-FIGMA-006
review_type: IMPLEMENTATION_REVIEW
implementation_ref: IMP-TOGGLE-FIGMA-001
amendment_ref: AMD-TOGGLE-FOCUS-EFFECT-003
contract_digest_sha256: 07ae4f7700bd4670156e5be211f9476d97eb97e15275addd69198f5152cd6266
extension_data_digest_sha256: 0baef3e14a121d3284c04d28bd8bf2cc66a940270f3486994a23e3456d7fc3d4
target: figma
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

| Criterio | Resultado | Lectura posterior |
|---|---|---|
| AC-TGL-009 | PASS | On/Focus `111:135` y Off/Focus `111:155`: cada efecto exterior liga `VariableID:136:122`, cada interior `VariableID:136:123`; cuatro de cuatro bindings con scope `EFFECT_COLOR` y nombre semántico de efecto. Cero uso de los antiguos roles de stroke/fill en efectos. Ocho aliases por modo comprobados en Foundations. |
| AC-TGL-010 | PASS | Set `111:163` con ocho variantes; On/Focus mantiene dos efectos, Off/Focus cinco y el set 25 en total. La escritura devolvió tipos, offsets, radios, spreads, orden, visibilidad y colores RGBA iguales antes/después. La captura posterior 704×280 conserva anillos visibles y fondos pálidos Off, sin cambio aparente. |

Los otros 21 efectos son sombras internas literales previamente documentadas por ausencia de categoría de geometría de sombra en el JSON; no se les asigna un token de color inventado. Los 40 paints y el contraste 0.1.2 no se modificaron. Set `UNPUBLISHED`; web y accesibilidad funcional fuera de alcance. [Hallazgo previo](toggle.v0.1.2.effect-scope-finding.md) conservado como `FAIL` histórico, resuelto para los cuatro bindings mediante esta enmienda. Auditoría humana pendiente.
