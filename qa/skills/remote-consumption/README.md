# QA de consumo remoto

Alcance: motor de las dos skills y canal GitHub independiente. Los ZIP nuevos no incluyen specs fijos.

Pruebas automatizadas: `python3 -m unittest discover -s tests/remote -v`. Casos: actualización A→B con el mismo motor, corte anterior preservado, caché con consulta nueva, fallo de red sin fallback, corrupción de descargas y caché, traversal/symlink, protocolo incompatible, origen no permitido, salida preexistente y JSON con tipo inválido.

La revisión independiente verificó catálogo local real → ambos runtimes, 2132 archivos, verificador Figma PASS, inicialización PO PASS y suite existente de skills (22 casos) PASS. Encontró un error de diagnóstico con JSON no objeto; corregido con validación explícita y regresión.

La prueba local usa un transporte de archivos equivalente al canal remoto; no acredita disponibilidad HTTPS en GitHub ni capacidades de Genspark. Las comprobaciones de publicación y los límites finales se conservan bajo output/evolution-lab/2026-10-16/.
