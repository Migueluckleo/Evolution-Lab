# Prueba independiente de traspaso Markdown · skills 0.2.1

Resultado: **PASS_MD_ONLY_FORWARD_REVIEW**. El Markdown pegado íntegramente y el snapshot propio de la skill Figma contienen datos suficientes para preparar esta reproducción. No se ejecutó Figma ni se certifica fidelidad visual o aceptación humana.

Fecha: 2026-10-15. Entrada leída: [replicar-en-figma.md](../../../output/qa/skills-0.2.1/entrega/replicar-en-figma.md). Skill consumidora: contpaqi-figma-screens 0.2.1 (artefacto histórico local; no incluido en esta publicación), junto con sus referencias de autoridad, handoff y flujo Figma. La copia archivada conserva los mismos bytes que la entrada temporal revisada.

- Markdown SHA-256: `67a733be2561e5d704df4d5d5bdd92e0535c6c5637b8371a01da6d3f25726ce0`.
- Paquete: `0.2.1`; DS digest: `4205fc48bf65ef7f42f3c51f15402d61c7f5e25ae88850f1a50ccd41fb90bc67`.
- HTML SHA-256 declarado y ligado a la captura embebida: `09d2e59e405f6b925cbe9c47159f498762a2046d49c1208be684a26a22783d9e`. Se comprobó concordancia interna; esta prueba no abrió ni volvió a ejecutar el HTML.

## Comprobaciones

| Control | Resultado comprobado |
|---|---|
| Entrada autónoma | Un bloque JSON válido, schema 1, productor y consumidor correctos, release/digest coincidentes. La lectura usó solo MD y skill empaquetada; no abrió PNG, HTML ni handoff.json externo. |
| Integridad del paquete | `python3 scripts/verify_snapshot.py`, ejecutado desde la skill consumidora: PASS, 2131 fuentes, cero errores. |
| Fuentes del traspaso | 24 rutas/SHA-256 embebidos contrastados contra manifest y bytes del snapshot propio; 24/24 coinciden. Referencias anidadas están incluidas en esa lista. |
| Familias disponibles | Índice de 43 familias con 43 enmiendas tipográficas presentes. La escena usa cinco familias DS; no se confunde disponibilidad de 43 con construcción de 43 en esta prueba. |
| Identidades y composición | Diez identidades únicas: siete instancias DS de esas cinco familias y tres nodos locales documentados. Contratos, versiones y enmiendas de las instancias coinciden con el índice. |
| Cobertura de estado | Siete estados por dos viewports, 14 combinaciones únicas. Los 82 registros de nodo cubren exactamente las listas requeridas, con parent_id y orden válidos, bounds finitos, texto visible y props por estado. Todas las diez identidades aparecen en evidencia PASS por instancia. |
| Evidencia del productor | Los 14 registros embebidos declaran PASS; acciones y aserciones corresponden a cada estado; cero errores, solicitudes HTTP(S), imágenes rotas o texto sin mapear. La fuente Manrope tiene al menos una face cargada. Esto revisa evidencia guardada, no es una nueva ejecución de navegador. |
| Tipografía | Catálogo activo 0.1.2: 79 estilos, 18 base, tres derivados de escala y cuatro derivados con formato. Ocho IDs tipográficos observados en 124 fragmentos visibles resuelven en el catálogo. Peso, tamaño, line-height, tracking y decoración calculados son consistentes con las recetas declaradas; `normal` equivale a tracking cero cuando corresponde. No se inventó precisión de layout desde el marker. |
| Límite de escala nativa | La escena no consume recetas derivadas; `native_inheritance: null` es coherente. La skill preserva la enmienda 0.1.2, el overlay acotado y la obligación de verificar el destino; el PASS de 103 consumidores del DS no se atribuye a este prototipo. |
| Separación de resultados | Revisión visual del productor: NOT_RUN. Construcción, IDs efectivos, bindings y QA Figma: NOT_RUN. No hay aprobación humana ni equivalencia visual afirmada. |

Se ejecutó además el chequeo independiente `/tmp/md-forward-0.2.1-check.py`; su resultado temporal `/tmp/md-forward-0.2.1-result.json` registra estos conteos sin modificar fuentes. No se comparó el objeto completo con handoff.json: el MD omite intencionalmente el mapa repetido de todas las variables CSS.

## Reconstrucción recuperable desde el MD

El tema Contable y los viewports 1440×900 y 1000×760 están explícitos. La columna local conserva padding 32 px, gap 24 px y jerarquía de heading, InputField, Button y feedback. Los títulos y mensajes locales tienen nodo, texto, bounds y estilo propios. El valor inicial vacío cambia a `PO` mediante stateProps y acciones declaradas.

Modal Media conserva título/contenido textual, sin presentar un BodySlot inexistente. SideBySide declara contenido variable Avatar, Logos y Button; sus nodos están bajo el modal con orden y medidas. El atajo M está marcado como decisión local. Abrir, cerrar, Enter y Escape tienen acciones y estados recuperables; su traducción a conexiones Figma debe registrar los límites de esa plataforma.

No hay defecto bloqueante del formato MD-only. Antes de cualquier escritura quedan las tareas de destino expresamente señaladas: resolver archivo autorizado (`figmaTarget: null`), leer claves/IDs reales y mapear propiedades Figma desde el componente disponible. Un `figma: null` no se transforma en un ID inventado. La comparación visual externa continúa NOT_RUN mientras no se aporten/abran las referencias opcionales; no impide preparar la pantalla a partir de estos datos.
