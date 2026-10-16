# QA-RADIO-SOURCE-001 · extracción técnica de origen

```yaml
qa_id: QA-RADIO-SOURCE-001
review_type: SOURCE_CONTRACT_REVIEW
source_ref: SRC-FIGMA-RADIO-BUTTON-001
markdown_digest_sha256: 739b6b023c26b50bfca00c51320403175e9be017ccb18371d5bd7f4051db912b
yaml_digest_sha256: b6e66f541e7740cbea7d20512c5fca19a9d16b97175fa89a61deef02761cb3f4
executed_at: 2026-09-23
result: PASS
```

La lectura read-only identificó el set `1230:24283` por metadata, captura y Plugin API, recorrió 53/53 nodos incluidos 16 textos ocultos, y resolvió ocho variantes, ocho instancias de dos mains locales, 12 variables usadas (nueve locales, tres remotas) y un estilo local. El YAML se parseó y las cuentas de variantes, instancias, dependencias, ocho layout children, ocho visual descendants y 16 text runs reconciliaron con el Markdown. La descripción de la página se separó del campo Description vacío del set. No se añadieron interacciones ni reglas de accesibilidad web. Biblioteca y versión de variables remotas permanecen `NOT_EXPOSED_BY_FIGMA_MCP`.

Este `PASS` acredita el contrato de **evidencia fuente**, no aprueba la reconstrucción propuesta ni valida el Figma destino.
