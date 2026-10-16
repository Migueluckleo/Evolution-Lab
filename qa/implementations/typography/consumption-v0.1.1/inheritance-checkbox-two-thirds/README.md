# Piloto causal de herencia Checkbox 2/3

Resultado: **CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT**. No valida los 103 rangos ni modifica su aceptación normativa.

La instancia original `446:207` obtiene su principal real `149:179` mediante API. Se clonaron su conjunto propietario y la instancia; el actor es el texto izquierdo `149:180`, con el texto derecho `149:183` como control. Las rutas de hijos reales y el vínculo al principal copiado se verificaron antes de intervenir.

Se aplicó únicamente al actor copiado el estilo A `ui-body-compact`, después B `subheading-1-semibold` y se restauró A. Los tres readbacks independientes registran ID exacto en el principal y **ID vacío en la instancia durante A, B y A restaurado**. Sin setter sobre el texto de instancia, B propagó tamaño 13.333333969116211, peso600/SemiBold, interlineado150% y tracking−2%; A restaurado recuperó tamaño9.333333969116211, interlineado13.333333969116211px y tracking0px.

El control, las propiedades, los overrides y la escala permanecieron iguales. Todos los campos de la observación A restaurada coinciden exactamente con A, incluidos hashes de conjunto/principal/instancia y guards de originales. La limpieza confirmó la eliminación de ambas raíces temporales sin errores.

La evaluación reproducible y los SHA256 están en [evaluation.json](evaluation.json). Se conservaron los seis resultados directos y los seis scripts ejecutados, sin sustituir el fallo inicial ni su diagnóstico guardados en la carpeta superior. Las normalizaciones autorizadas se limitan a refs vacías de la raíz y el override de nombre local exacto; no cubren descendientes, métricas ni otros overrides.

Falta demostrar todas las cadenas reales de los103 textos y el factor4/3 de Count. El hallazgo prueba que un ID vacío puede coexistir con herencia tipográfica causal en este caso; por sí solo no permite aceptar cualquier texto vacío.
