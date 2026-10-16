# Revisión independiente · consumo remoto del DS

Fecha: 2026-10-16. Revisor: agente independiente `review_governance`, distinto del autor. Alcance: motor remoto, canal de datos, paquetes instaladores e integración PO. Resultado final: **PASS local** para el alcance del cambio de consumo remoto. Sin defectos abiertos en los controles ejecutados. Build PO adicional: **INTERRUPTED** por petición del coordinador; no se cuenta como PASS ni FAIL. No acredita publicación remota ni ejecución Figma. `user_audit: NOT_REQUIRED`; `human_review_policy: OPTIONAL_NON_BLOCKING`.

## Archivos revisados y método

Se leyeron `scripts/ds_remote.py`, `scripts/ds_skills.py`, `config/ds-skills.json`, ambos `scripts/resolve_ds.py`, ambos SKILL.md, sus referencias de consumo remoto, el inicializador PO y `.github/workflows/publish-catalog.yml`. Los hashes exactos del corte de fuentes están en `reviewed-hashes.json`.

Se consultó primero Graphify (`graphify query "ds_remote resolve_ds skills snapshot remoto GitHub" --budget 700`) y se confirmaron los hallazgos en los archivos: el índice previo no contenía aún la implementación nueva. No se atribuye actualidad al grafo.

Las pruebas de red se ejecutaron con transporte inyectado en carpetas temporales: permite reproducir fallos y A→B sin publicar. La integración de corpus real utilizó los objetos de `catalog/` mediante transporte local de lectura, respetando el mismo contrato del cargador. No se modificaron fuentes ni snapshots por esta revisión. Los tests pueden generar cachés Python locales; no son cambios de implementación.

## Resultados

| Control | Evidencia ejecutada | Resultado |
|---|---|---|
| Mismo motor, nuevas fuentes A→B | Suite remota: el segundo trabajo obtiene el contenido nuevo y archivo adicional; el primero conserva A; la instalación conserva su contenido y no incorpora snapshot. | PASS |
| Consulta de actualidad y caché | Suite remota y corpus real: cada trabajo solicita current.json; la segunda ejecución con igual identidad evita volver a descargar manifiesto y tar. | PASS |
| Caída de red con caché válida | Suite remota: falla la consulta del puntero, no se crea la salida y no se usa fallback antiguo. | PASS |
| Integridad de descarga/caché | Suite remota: descarga alterada se rechaza; caché corrupta se vuelve a solicitar y verificar. | PASS |
| Protocolo/rutas del catálogo | Suite remota rechaza protocolo incompatible y URL externa. Prueba aislada adicional del publicador rechaza esquema/protocolo/digest/longitud inconsistentes como STALE. | PASS |
| Rutas del tar y manifest | Suite remota rechaza traversal y symlink; pruebas independientes rechazan ruta absoluta, Windows, backslash y ruta no normalizada. No se escribe fuera del destino. | PASS |
| Integridad de miembros | Pruebas independientes rechazan archivo faltante, duplicado, hardlink, hash por archivo incorrecto y límite de expansión excedido. No queda una salida de ejecución parcial. | PASS |
| Salida existente | Suite remota conserva salida previa y rechaza reutilizarla. | PASS |
| JSON remoto de tipo inesperado | Se encontró un defecto inicial; tras corregirse, la suite y relectura verifican rechazo controlado de null/lista/texto mediante ValueError. Detalle abajo. | PASS corregido |
| Equivalencia de cargadores | Ambos scripts son idénticos; prueba incluida en suite remota. | PASS |
| Paquetes sin corpus | ZIP 0.3.1 Figma: 10 entradas, 25443 bytes; PO: 25 entradas, 43674 bytes. Sin assets/design-system, snapshot-manifest ni components.json. Ambos loaders y todos los archivos fuente de sus skills coinciden con el ZIP. | PASS |
| Corpus real → Figma runtime | Motor 0.3.0 inicial: extracción verificada de 2132 archivos y verify_snapshot.py exit 0, PASS. No se llamó a Figma. El loader final corregido está empaquetado en 0.3.1. | PASS |
| Corpus real → PO runtime/proyecto | Extracción verificada y init.mjs exit 0. El proyecto conserva el ds_digest y la versión del corte remoto; no depende de un snapshot instalado. | PASS |
| Regresiones del consumidor | 22 tests de skills, incluyendo 9 de handoff tipográfico, pasan con Node disponible; no hay skips en la ejecución final. | PASS |

Suite remota final: **11 tests, OK**, exit 0, en `remote-tests.txt`. Regresión de skills: **22 tests, OK**, exit 0, en `skills-tests.txt`. La primera ejecución sin Node omitió 9 casos; se repitió con el Node empaquetado y quedaron todos ejecutados. No se contabiliza el primer intento como cobertura completa.

Corpus real probado: manifest `8e807e104d1b2222bb214ddaefb63c50968e40c89e08168958d8c8c6ce591b83`, ds_digest `c3d9ced225a2811dc64ae5640124e97fbc51c8b3a6a2f30a644b52f255f037f8`, 2132 archivos. El segundo consumidor solo solicitó `catalog/current.json`, reutilizando objetos por hash. Runtimes y proyecto aislados en `/private/tmp/remote-independent-rsa7fzn8/`.

## Defecto encontrado y resuelto

**REMOTE-REV-001, P2, resuelto:** un current.json que fuese JSON válido pero no objeto (`[]`, `null` o `"bad"`) producía AttributeError en `.get()`. Esa excepción escapaba al manejador CLI y rompía el diagnóstico JSON `BLOCKED`/`offline_fallback:false`, aunque no creaba salida ni aceptaba datos. Se informó al autor. La corrección valida que unique_json devuelva un dict y emite ValueError antes de acceder a campos; cubre también manifest y configuración del motor. Se añadió `test_non_object_catalog_is_structured_error`. Ambos scripts corregidos son idénticos y están incluidos en 0.3.1; 0.3.0 se conserva histórico.

No quedan defectos concretos abiertos en los controles ejecutados. La revisión no pretende demostrar ausencia universal de fallos.

## Flujo, permisos y límites

El instalador contiene instrucciones, scripts y starter. El contenido DS se publica por separado bajo identidades de manifiesto y hashes de archivos. Cambios compatibles del DS permiten que el mismo motor resuelva nuevos datos sin reinstalarse; cambios de protocolo o del propio motor sí pueden requerir actualizar la skill, como indica la documentación.

El transporte usa el origen GitHub público fijo, sin header de autenticación ni token. El cargador rechaza redirecciones, paths ajenos y formatos incompatibles. Los hashes prueban consistencia e integridad del corte, no autentican una decisión de diseño ni protegen contra un mantenedor autorizado comprometido. Los datos remotos se extraen dentro del snapshot de ejecución; no reemplazan instrucciones ni scripts del motor instalado.

Las instrucciones fijan el corte durante cada trabajo, exigen consulta nueva para otro encargo y bloquean construcción dependiente cuando faltan Python, scripts, HTTPS, catálogo o integridad. Mantienen los límites MCP/biblioteca/destino Figma y la distinción entre fuentes públicas y acceso a componentes reales.

El workflow publica solo catalog/ después de ejecutar la suite remota, construir y comprobar el canal. Se revisó estáticamente su configuración; no se lanzó GitHub Actions ni git push. El funcionamiento público, reglas de main, capacidades de un cliente concreto y autenticación/permisos Figma quedan fuera de esta prueba local. No se promete compatibilidad universal ni actualización instantánea por cada commit: la fuente es la última publicación válida.

## Cierre del alcance

No hubo publicación, instalaciones globales, autenticación ni ejecución Figma. El QA de motor no acredita una pantalla visual. La integración PO se inicializó con el corpus real; la preparación de assets terminó con exit 0 (75 assets), pero el build adicional se interrumpió durante compilación por petición del coordinador, con exit 130/KeyboardInterrupt de la sesión propia. Se registra **INTERRUPTED**, sin éxito ni fallo atribuidos, en `po-build.txt`. Los scripts del starter/PO no cambiaron en este alcance; init y las regresiones ejecutadas cubren la nueva entrada remota. No se ejecutó inline-export ni inspección visual de HTML en esta prueba adicional. El autor conserva responsabilidad de sincronizar los registros/grafo, validar publicación efectiva si se autoriza y distribuir el release corregido.
