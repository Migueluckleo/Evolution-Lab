# QA de implementación · Buttons · bindings locales 0.2.2

Fecha: 2026-10-05. Resultado: **PASS acotado**. Implementación VALIDATED para AMD-BUTTON-LOCAL-BINDINGS-001. Auditoría humana PENDING; no publicación de biblioteca ni frontend.

## Evidencia

- [Enmienda en specs](../../specs/components/button.local-bindings.amendment.v0.2.2.md) y [QA documental](../contracts/button.local-bindings.v0.2.2.review.md).
- [Mapa derivado](../../implementations/figma/buttons.local-bindings.v0.2.2.token-map.json): JSON canónico → variable local → aliases por los cuatro modos.
- [Antes](buttons.local-bindings.v0.2.2.before.json), [escritura](buttons.local-bindings.v0.2.2.write.json), [lectura independiente posterior](buttons.local-bindings.v0.2.2.after.json), [722 bindings leídos](buttons.local-bindings.v0.2.2.exact-readback.json) y [verificación consolidada](buttons.local-bindings.v0.2.2.verification.json).
- Capturas [antes](buttons.local-bindings.v0.2.2.before.png) y [después](buttons.local-bindings.v0.2.2.after.png), ambas 516×1883.

## Controles

| Requisito | Resultado | Evidencia |
|---|---|---|
| REQ-BTN-LOCAL-01 | PASS | 722/722 referencias sustituidas en 123 nodos. Cero IDs remotos o no resolubles entre los bindings nodales de los 364 nodos. 34 variables consumidas distintas; 36 aliases de los nueve roles comparados por modo. |
| REQ-BTN-LOCAL-02 | PASS | 60 IDs/variantes, 364 nodos, 120 instancias de icono y geometría idénticos. Huellas de identidad, geometría, pinturas, textos, API y reacciones no cambian; solo cambia la categoría bindings. |
| REQ-BTN-LOCAL-02 · render | PASS | Manrope Bold/Regular y sus métricas se conservan pese a la diferencia de capitalización de los strings de origen. Capturas idénticas: cero píxeles cambiados y SHA-256 de ambos PNG 8b4a7c85f3ec9138a0588f8b922b676696d81f8ffb503d2cef3bb04ba7a4bd04. |
| REQ-BTN-LOCAL-03 | PASS | Cero cambios en las ocho raíces consumidoras/control leídas antes/después, incluidos bindings y overrides. Modal: cuatro botones en Footer y 16 en Basic/Media/SideBySide; Empty states: ocho. Sidebar: cero consumidores de Buttons en las tres raíces, utiliza Icon Buttons. |
| REQ-BTN-LOCAL-04 | PASS | Enmienda, evidencia, estado y registros enlazados; no afirmación de aprobación humana ni publicación Figma. |
| SLOT-REV-01/02 | PASS | NOT_APPLICABLE: anatomía fija de label y dos iconos. No se modifican Slots de anfitriones. |

No se crean nodos, variables ni primitivas; no se cambian pinturas, tokens canónicos, scopes, aliases, reacciones o textos. Las nueve variables locales ya existentes conservan sus definiciones. No se modificaron principales Phosphor ni componentes fuente.

## Método y límites

Los snapshots incluyen contenido oculto de instancias dentro de las raíces declaradas; no recorren todo el archivo. Huellas FNV-1a UTF-16:length detectan regresiones por categoría y se complementan con matriz exacta de bindings, dimensiones por variante y comparación PNG píxel a píxel. No son hashes criptográficos de archivos.

La comprobación de los cuatro modos corresponde a valores/aliases de los nueve tokens sustituidos; no es una nueva auditoría visual de todos los colores/temas, contraste, comportamiento web ni 1512 alternativas de iconos. La renderización observada corresponde al contexto actual del set. Persisten las limitaciones históricas, sin generar incidencias nuevas por campos UNRESOLVED fuera del alcance.

Durante preflight, una lectura de fontStyle como propiedad directa y otra de componentPropertyDefinitions en variantes fallaron sin escrituras. Se corrigió la consulta; las salidas extensas truncadas se sustituyeron por lecturas compactas completas. La única escritura Figma aplicada terminó con 722 operaciones y cero errores; el QA se basa en llamadas posteriores independientes.
