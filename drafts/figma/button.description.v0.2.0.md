# Description propuesta para Buttons

Estado: IN_REVIEW. Destino previsto: Description del component set 26:81 en la página Buttons del archivo AI-Design-System. No se ha escrito en Figma.

## Texto para pegar después de aprobar BUTTON-001 0.2.0

Buttons inicia acciones. Elige el tipo por jerarquía: primary para la acción principal del grupo; default para alternativa neutral; text para apoyo de baja prominencia; link solo para acceso contextual a otro contenido (su semántica web requiere definición aparte). Evita dos primary compitiendo.

Elige tamaño según contexto: large (48 px) para CTA destacado y espacio amplio; middle (40 px) para formularios y diálogos; small (32 px) para tablas o barras densas. Mantén un mismo tamaño en cada grupo. La altura small no acredita un objetivo táctil adecuado.

Los estados default, hover, press, focus y disabled representan condiciones visuales; no prueban teclado, eventos ni bloqueo real. Si una acción está deshabilitada, explica el motivo cuando corresponda.

Usa etiquetas breves y específicas, como “Guardar cambios”. “Default” es solo el texto inicial del maestro. Normalmente basta texto; agrega un icono solo si aclara la acción. Izquierdo: identifica acción u objeto. Derecho: anticipa avance, apertura o dirección. Dos iconos son una excepción con significados distintos y revisión UX. Todos los iconos deben seguir vinculados a Phosphor Icons. No usar icon-only ni acciones destructivas sin patrón propio.

Referencia normativa después de la aprobación: contrato BUTTON-001 0.2.0.

## Documentation link

Vacío hasta disponer de una URL pública, estable y verificable para la versión aprobada. No usar una ruta local ni un enlace a este borrador.
