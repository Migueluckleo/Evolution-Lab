---
report_schema: sdd-project/0.2
report_type: CONTRACT_SYNTHESIS
report_id: SYN-DROPDOWN-ITEM-001
contract_id: DROPDOWN-ITEM-001
contract_version: 0.1.0
created_at: 2026-09-28
review_status: PASS
---

# Síntesis · Dropdown Item

## 1. Encargo y entregables
Continuar con los componentes pendientes, omitiendo los doce Logos restantes. Select fue seleccionado como siguiente familia. El bloque reusable observado es Dropdown Item; las composiciones abiertas/cerradas se mantienen separadas. Contrato, proyección fuente MD/YAML, mapa JSON→Figma, implementación y QA persistidos.

## 2. Fuentes revisadas
- SRC-FIGMA-SELECT-001: página268:20247, set2479:11730 y ejemplos2488:13364–13372. Lectura MCP propia; snapshot SHA-256 0c105f7924d2de0a3566764a063aac646a8a68852d699ba813daac11a0d4525c.
- SRC-TOKENS-INV-001: JSON aprobado SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474.
- Snapshot de variables locales SHA-256 85d1a49b5fe191ca8c0d764a3e287e70cc60b6ae25fa08657e05fd211ca1e251.
- Componentes reales del destino: Checkbox149:199, Loader378:1869, Input Field397:152; Eye395:125 y X175:356 por keys Phosphor verificadas.
- Graphify no contiene etiquetas de Select en el grafo actual; no se regeneró y no se usó como autoridad.

## 3. Matriz de evidencia
| Evidencia | Clasificación | Respaldo | REQ |
|---|---|---|---|
| 18 combinaciones, dimensiones y colores | OBSERVED | snapshot rows | DI-001,003–005 |
| Textos, booleanas y swap izquierdo | OBSERVED | defs fuente | DI-002 |
| Alias, scopes y cuatro modos | OBSERVED / DERIVED | JSON y mapa destino, validador96checks | DI-008 |
| Checkbox siempre unselected en origen | OBSERVED | dependency1221:28820 en sus 18 instancias | DI-005 |
| Normalizar checkbox, interlineado y swap derecho | DERIVED, decisión delegada | contrato y DEC-DROPDOWN-ITEM-NORMALIZATION-001 | DI-002,004,005 |
| Cero reacciones de filas | OBSERVED |18root.reactions.length=0 | DI-006 |

## 4. Transformaciones
Nombres de ejes normalizados al destino. Texto/icono/divisor con rol semántico adecuado sin cambiar RGB. Interlineado tokenizado24/20 y truncado. Proyección fuente conserva los datos observados y sus límites; originales y JSON histórico intactos.

## 5. Requisitos y adopción
REQ-DI-001–009 delimitan CREATE de18variantes,10propiedades,72dependencias directas y pruebas de cuatro modos. Delegación de migración vigente, auditoría humana PENDING; no aprobación individual simulada. Revisión documental PASS antes de la escritura.

## 6. Conflictos
Ningún conflicto bloqueante dentro del bloque visual. Fuente usa tokens de texto en iconos y token de interacción en texto Selected; destinos semánticos equivalentes resuelven la incompatibilidad sin nuevos tokens. La futura composición tiene efectos y comportamiento por documentar, fuera de alcance de este contrato.

## 7. Inferencias no normativas
No inferir selección múltiple, apertura/cierre, reglas de teclado, acciones de Eye/X ni tratamiento de grupos vacíos. Header no implica una acción.

## 8. Preparación por destino
Figma READY y finalmente VALIDATED. Frontend fuera de alcance. No se requiere decisión adicional para estas filas; revisión de contraste y tipografía consolidada por excepciones.

## 9. Revisión documental
[QA](../../qa/contracts/dropdown-item.v0.1.0.review.md) PASS. Validador de tokens ejecutado dos veces:24roles×4modos,0errores. Las definiciones normativas de tokens permanecen solo en el inventario.

## 10. Cierre
[Contrato en specs](../../specs/dropdown-item.contract.v0.1.0.md), SHA-256 414040f481f994316406dfd61ca09a4c5a52b4b9ec97e30dcb2a1dc90ef27d42. QA técnico PASS;18variantes,180referencias y186pinturas. Se corrigió una pintura de respaldo incorrecta detectada visualmente, sin cambiar variables. No biblioteca publicada. Composiciones Select pendientes.

## 11. Historial
Primera versión. Borrador trasladado a specs tras QA; aclaración de conteo72dependencias directas frente a93instancias expandidas no cambia el alcance. Ajustes posteriores normativos se harán directamente en specs.
