# Publicación de Composer para consumo remoto

2026-10-20. El usuario solicita publicar Composer en el catálogo de Evolution-Lab para las skills instaladas en Genspark. Esta autorización es posterior al cierre local y a la publicación documental en otro repositorio.

Se incorporan las enmiendas del aviso 0.1.2 y del Slot 0.1.3, código React, props, estilos, ejemplo, pruebas, documentación y evidencia de QA. `noticeContent` permite componer todo el aviso; `undefined` mantiene la muestra y `null` permite vacío. `showAction=false` conserva el valor inicial. No se introduce lógica de créditos ni servicios.

El canal se genera desde las fuentes públicas de Evolution-Lab, preservando su anonimización y sus releases anteriores. El digest público difiere correctamente del corte privado. Los motores 0.3.3 no cambian; las skills consultan el puntero de nuevo al iniciar cada encargo. Las sesiones existentes mantienen su corte. No se publican instaladores ZIP ni la biblioteca Figma.

[Comprobaciones previas](prepublication.json) y [QA documental](docs-check.json). Los QA históricos que dicen «no publicación» describen su ejecución anterior. Las capturas y pruebas del componente permanecen bajo output/qa/conversation-composer-slot-2026-10-20 y qa/implementations. El único enlace histórico roto detectado se restaura con el comprobante original po-build.txt, cuyo resultado permanece INTERRUPTED.

El workflow y la descarga anónima real por ambos cargadores se comprobarán tras el push; el resultado queda en la evidencia local de esta publicación. No se afirma ejecución dentro de Genspark ni regeneración del grafo público.
