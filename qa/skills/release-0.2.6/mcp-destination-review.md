# Revisión independiente · conexión MCP y destino Figma

Fecha: 2026-10-16. Revisor: agente independiente `review_governance`. Resultado: **PASS**, catorce escenarios conformes y sin hallazgos bloqueantes. `user_audit: NOT_REQUIRED`; `human_review_policy: OPTIONAL_NON_BLOCKING`.

## Alcance y evidencia

Revisión de comportamiento de las nuevas secciones “Comprobar conexión con Figma” y “Preparar la entrada y el destino”, puntos 4/5, de `skills/contpaqi-figma-screens/SKILL.md`. Se leyó el archivo completo y `references/figma-workflow.md`; se comparó el SKILL.md con la copia inmutable de `output/skills/0.2.3/contpaqi-figma-screens/SKILL.md` para delimitar el cambio. La primera revisión cubrió las instrucciones de conexión y destino. La revisión ampliada incluye los dos párrafos nuevos de “Resolver componentes, variables y estilos” y su coherencia con `references/local-components.md` y `references/design-system.md`.

Hashes revisados:

- `skills/contpaqi-figma-screens/SKILL.md`: `9cb8b71cc74cd418f30acdaba361cb65f5b6633c76aab6166ca1afb843b61a06`.
- `skills/contpaqi-figma-screens/references/figma-workflow.md`: `b1a4e5c59e7ff91e24db122627058acf0a3cee3c3d94fb5ec7139413881d8a91` (corte ampliado final; el anterior fue `e17ba15fe2ced75381087a1da557be302b3b5c477a072ec84b6929b27dc04669`).
- `skills/contpaqi-figma-screens/references/local-components.md`: `7903880803e4ad81ed36e7d36e5fc24945b9684e4d31cf3da324665328ca94ce`.
- `skills/contpaqi-figma-screens/references/design-system.md`: `62fc61e08ead6877c9d4d6cd356f22491d05281ff15ead3c5e0e8919cd4264e1`.

Se consultó primero Graphify mediante `graphify query "contpaqi-figma-screens MCP destino prototipo maestro autorización" --budget 1000`. Se abrió después la fuente local, ya que el grafo derivado no acredita las instrucciones recién modificadas. El resultado del grafo fue truncado; no se usó para declarar cobertura o vigencia.

La comprobación documental externa confirmó que cada conexión usa la cuenta Figma del usuario y que se requiere un cliente compatible: [configuración oficial del servidor remoto](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/). La escritura exige acceso de edición y cliente compatible conectado al servidor remoto: [Write to canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/). Consulta realizada el 2026-10-16; la skill remite a manuales vigentes y no fija una lista estática de clientes.

## Escenarios

Son evaluaciones de las instrucciones efectivas, no llamadas reales ni simulaciones de autorización del servicio.

| ID | Escenario | Comportamiento esperado y resultado de revisión | Resultado |
|---|---|---|---|
| MCP-01 | No existe MCP Figma o la conexión no está activa. | Descubrir herramientas, informar que se necesita conexión y autenticación propia, conservar preparación y detener únicamente construcción Figma. No instalar ni cambiar conexión sin autorización. El mensaje requerido aparece explícitamente. | PASS |
| MCP-02 | Existe conexión de solo lectura. | Explicar necesidad de escritura sobre lienzo con servidor remoto y cliente compatible; comprobar capacidades reales y manuales, sin escritura de prueba. `figma-workflow.md` obliga a conservar mapeo y declarar el límite cuando falte capacidad. | PASS |
| MCP-03 | Cuenta conectada, pero permisos insuficientes sobre el destino. | Señalar el permiso necesario y no escribir sin verificarlo; comprobar identidad y permisos antes de cada lote. Una lectura satisfactoria no sustituye capacidad de edición. La referencia limita mutaciones al prototipo autorizado. | PASS |
| MCP-04 | No se indicó archivo ni se pidió crear uno. | Pedir el enlace o una solicitud de archivo nuevo; conservar preparación y no escribir hasta resolverlo. No elegir archivo activo ni una sesión anterior. | PASS |
| MCP-05 | Se proporciona el enlace del maestro, incluso renombrado y con permisos de edición. | Reconocer el maestro por `tj3WIBEZDGLVs7MJWKCwgf`, mantenerlo de lectura, explicar el límite y solicitar otro archivo o creación nueva. El nombre visible y los permisos no eluden la restricción de esta skill. | PASS |
| MCP-06 | Se proporciona archivo correcto, distinto del maestro, autorizado y con capacidad de escritura. | Conservar ese destino durante la ejecución; verificar identidad y permisos en cada lote, inspeccionar contenido existente y construir dentro del alcance. No exigir confirmación humana rutinaria ni volver a preguntar por un destino ya resuelto. | PASS |
| MCP-07 | El usuario pide explícitamente crear un archivo nuevo. | Cargar `figma-create-new-file`, seguir su procedimiento y registrar el enlace/file key real. Usar ese archivo en los lotes siguientes. Si el procedimiento necesita elegir plan, resolver esa decisión concreta; no inventar identidad ni utilizar el maestro. | PASS |

## Coherencia y límites conservados

Las instrucciones nuevas refuerzan los límites ya presentes: el maestro se consume en lectura, el prototipo se construye en el destino autorizado, faltas de capacidad se comunican sin afirmar creación, y un archivo nuevo pasa por la skill oficial. La referencia mantiene inspección previa, IDs reales, lotes recuperables y protección del contenido ajeno. No se encontró contradicción efectiva.

La indicación de comprobar conexión mediante lectura no autoriza elegir un archivo para escritura. Si esa lectura requiere un enlace aún ausente, el punto 4 determina la información que falta; no habilita sondeos ni mutaciones de prueba. La skill distingue falta de conexión, falta de permisos y fallo de red; no obliga a interpretar cualquier fallo como ausencia de credenciales.

Pedir destino, permisos o selección de plan indispensables es una solicitud de datos/capacidad real, compatible con el cierre técnico sin aprobación humana rutinaria. La cuenta individual no se incluye en la skill ni se comparte mediante el paquete.

## Escenarios ampliados: biblioteca y reutilización

La consulta Graphify de esta ampliación fue `graphify query "contpaqi figma screens componentes existentes inaccesibles composición local" --budget 700`, seguida de lectura directa de los archivos anteriores. El SKILL.md conserva el hash de la revisión MCP/destino; los siete escenarios originales siguen pasando con los dos párrafos añadidos a la referencia.

| ID | Escenario | Comportamiento esperado y resultado de revisión | Resultado |
|---|---|---|---|
| LIB-01 | Biblioteca del DS publicada, accesible a la cuenta y disponible en el destino; la familia cubre la necesidad. | Importar o reutilizar el componente real por identidad/claves verificadas, con propiedades y vínculos admitidos. No reconstruirlo ni crear una familia equivalente por conveniencia. | PASS |
| LIB-02 | El componente real ya está disponible en el archivo destino con identidad comprobada. | Reutilizarlo; no exigir pegar URL del maestro ni permiso de edición del maestro. La nueva instrucción reconoce expresamente este caso. | PASS |
| LIB-03 | El destino carece de los componentes utilizables y la biblioteca no está disponible. | Avisar que se debe habilitar la biblioteca y comprobar acceso de la cuenta. No cambiar su configuración automáticamente ni tratar los specs públicos como instalación de biblioteca. | PASS |
| LIB-04 | La familia adecuada existe, pero la cuenta no puede acceder/importarla. | Conservar UNAVAILABLE_EXISTING_COMPONENT, comunicar la limitación y continuar lo independiente. La falta de acceso no autoriza reconstrucción ni convierte la familia en faltante. | PASS |
| LIB-05 | El índice tiene figma:null o una búsqueda no resuelve la familia. | No inferir inexistencia. Leer contratos/localizadores y descubrir biblioteca/componentes con las capacidades reales; conservar el límite si no puede resolverse. `design-system.md` distingue expresamente figma:null de inexistencia. | PASS |
| LIB-06 | Se demuestra que ninguna familia o composición disponible del DS cubre la necesidad. | Crear un componente local justificado con patrones/tokens existentes y la ficha mínima de local-components; no promoverlo al DS, inventar tokens ni modificar el maestro. Una composición válida de instancias tiene prioridad sobre inventar una familia. | PASS |
| LIB-07 | Algunas familias necesarias están disponibles y otra existente es inaccesible. | Reutilizar las accesibles y conservar el bloqueo específico de la inaccesible; no reconstruir la familia pendiente ni bloquear trabajo independiente. El registro UNAVAILABLE_EXISTING_COMPONENT opera por familia. | PASS |

Las referencias existentes son coherentes con esta prioridad. `local-components.md` distingue componente existente, composición existente, necesidad no cubierta e inaccesibilidad. Su excepción para una reconstrucción local autorizada expresamente no es autorización implícita de esta tarea: la solicitud vigente exige no reconstruir familias inaccesibles, y una petición ordinaria de pantalla o una conexión insuficiente no activa esa excepción. Un cambio futuro explícito de alcance debería documentarse como tal, sin fingir que la réplica mantiene vínculo con biblioteca.

No se detectó una vía que confunda acceso al snapshot público con permisos sobre Figma. Los datos del catálogo son localizadores, la identidad real se verifica mediante lectura y el maestro sigue protegido por file key.

## Cierre

Sin hallazgos que requieran corrección. No se modificaron fuentes ni snapshots. No se ejecutó ninguna herramienta Figma, escritura de prueba, autenticación, instalación, creación de archivo ni publicación. Esta revisión acredita coherencia de instrucciones; no certifica la conexión o permisos reales de una cuenta, ni la integridad de un release posterior que incorpore el cambio. El autor debe incluir los hashes ampliados en su release final 0.2.6 y verificación de P08. Según el alcance de esta ampliación, no se revalidó un release intermedio ni se afirma integridad del paquete 0.2.6 desde esta revisión de instrucciones.
