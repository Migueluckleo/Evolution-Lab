# Loader · observación de la Librería anterior

Estado: OBSERVED. Este documento describe la fuente; no autoriza por sí solo una construcción. Fuente: Figma Libreria v1.1.0, página Loader (3917:1263), set público Loader (7561:47164). Inspección: 2026-09-25. El registro estructurado complementario está en loader.source.component-contract.yaml.

## Identidad e inventario

El set público tiene 16 variantes: propiedad literal SIze={Sm,Md,Lg,Xl} por Color={Primary,Secondary,Default,On color}, con defaults Sm y Primary. Los cuatro tamaños son cuadrados de 24, 40, 64 y 88 px. La capitalización SIze se conserva como evidencia de origen, no como requisito del destino.

Cada variante pública contiene una instancia del primer fotograma de su set local de animación. Existen cuatro sets internos: Loader sm (4283:240), Loader md (7556:45810), Loader lg (7556:46291) y Loader xl (7556:46652), con 24 fotogramas cada uno. Los cuatro sets están ocultos en la página fuente; no son 96 opciones públicas de tamaño o estado.

Las variantes públicas Secondary, Default y On color sobrescriben los paints de la instancia del primer fotograma, pero las variantes siguientes de los cuatro sets internos conservan el color Primary. Por ello, el prototipo fuente no demuestra que esos tres colores persistan durante todo el ciclo. Es una anomalía de la fuente que el contrato de destino debe resolver explícitamente.

## Anatomía y apariencia

Cada fotograma tiene un anillo obtenido por operación booleana Subtract —una elipse exterior menos una interior— con un gradiente angular, más un remate vectorial Ellipse 8 (Stroke). Los stops del gradiente están en 0, 0.0001 y 1; los dos primeros son transparentes y el tercero es opaco. El operando interno de sustracción no aporta un color visible al anillo final.

Los resultados observados son Primary #3255F7, Secondary #64748B, Default #0F172A y On color #FFFFFF. El remate está vinculado respectivamente a las variables de origen color/icon/brand, color/icon/secondary, color/icon/primary y color/icon/on-brand, todas con scope SHAPE_FILL. Solo el stop opaco Primary está vinculado a variable en la fuente; los stops opacos de los otros tres colores son literales. No confundir un RGB igual con un binding existente.

## Movimiento observado

Los 96 fotogramas forman cuatro ciclos íntegros de 24. Cada paso rota -15 grados. Cada fotograma cambia al siguiente mediante AFTER_TIMEOUT de 0.001 segundos, CHANGE_TO y SMART_ANIMATE lineal de 0.05 segundos; el último vuelve al primero. No se observaron reacciones en el set público. La inspección profunda de 581 nodos no halló enlaces rotos, saltos angulares ni fotogramas con estructura distinta.

## Dependencias y límites

La fuente no define una etiqueta accesible, texto visible, porcentaje, duración de carga, comportamiento web ni reduced motion. Ninguno de esos elementos se deriva de su apariencia. Tampoco demuestra que los cuatro colores tengan semántica universal fuera de esta familia.

Para reconstruirla en AI Design System se propone una página Loaders y un set público de 16 variantes, con secuencias internas completas por combinación de tamaño y color para evitar el salto a Primary observado. La propuesta de destino y sus criterios de aceptación viven en un contrato distinto. Los IDs del destino nunca sustituyen los IDs de esta observación.

## Cobertura de evidencia

La lectura cubrió el set público, las 16 variantes, los cuatro sets internos, 96 fotogramas, sus 96 reacciones, gradientes y bindings visibles. La captura de la cuadrícula pública confirma la forma; no demuestra por sí sola propiedades o bindings. Para localizadores y brechas, consultar el reporte loader.phase0-gap.v0.1.0.md.
