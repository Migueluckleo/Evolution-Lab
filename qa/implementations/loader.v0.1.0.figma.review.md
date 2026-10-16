# QA de implementación · Loader 0.1.0

Estado: PASS técnico y VALIDATED para el contrato LOADER-001 0.1.0. Auditoría humana PENDING; biblioteca UNPUBLISHED. Inspección: 2026-09-25.

## Alcance y estructura

Archivo destino AI Design System, página Loaders (377:122), set público Loader (378:1869), 16 variantes de Size por Color. Los cuatro diámetros públicos son 24, 40, 64 y 88 px. Hay 16 sets internos ocultos, uno por combinación, con 24 fotogramas cada uno. Sus instancias públicas son locales; no consumen el componente remoto de la Librería anterior. La página contiene solo el set público y los 16 sets internos ocultos.

## Readback técnico

La inspección exhaustiva del destino obtuvo 16/16 variantes públicas, 16/16 sets internos, 384/384 fotogramas con tamaño y rotación esperados, 384/384 enlaces AFTER_TIMEOUT → CHANGE_TO → SMART_ANIMATE lineal de 0.05 s cerrados en ciclos, 384/384 stops opacos y 384/384 remates ligados al rol semántico correcto. Cero errores de binding, secuencia, tamaño o asociación entre variante pública y primer fotograma. Los roles existentes color/icon/brand, color/icon/secondary, color/icon/primary y color/icon/on-brand tienen scope SHAPE_FILL, aliases a primitivas del JSON aprobado y cobertura de los cuatro modos. No se crearon variables, primitivas ni colecciones.

La captura del set público mide 331×512 px y conserva exactamente las posiciones de las 16 variantes del set fuente. La silueta circular, el degradado angular y el remate se compararon visualmente con la captura de origen. El origen usa una operación booleana y un remate vectorial; el destino usa un arco elíptico editable y un remate elíptico de apariencia comparable en la captura. No se realizó una comparación píxel a píxel del remate, por lo que no se declara identidad geométrica exacta. La captura de On color requiere contexto externo para apreciar el blanco; el componente no añade fondo.

## Corrección frente a la fuente

La fuente tiene cuatro ciclos Primary y cambia el color solo en el primer fotograma de Secondary, Default y On color. El destino crea los 16 ciclos completos para que el color permanezca estable durante la animación. La diferencia estructural está documentada en el contrato y en DEC-LOADER-COLOR-CYCLE-001; no se presenta como fidelidad literal del prototipo histórico. Primary liga su stop y remate a color/icon/brand, por lo que toma la primitiva de marca del modo activo.

## Límites

No se ha probado ejecución interactiva continua del prototipo en la UI, solo la estructura y destino de las 384 reacciones. No se certifican accesibilidad web, etiqueta para lector de pantalla ni reduced motion: la fuente no los define. Este PASS técnico no equivale a aprobación humana ni a publicación de la biblioteca Figma.
