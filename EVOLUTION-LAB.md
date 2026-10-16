# Evolution Lab

Laboratorio de optimización del sistema de diseño CONTPAQi y sus skills. El repositorio reúne fuentes, contratos, componentes, protocolos, QA y evidencia. La prioridad es mantenimiento consultable, ejecución documentada y ahorro de tokens antes de construir.

## Estado de esta entrega

Implementado: delegación técnica sin espera humana rutinaria, QA obligatorio, dos skills empaquetadas desde un mismo corte, y controles de conexión MCP, archivo destino y biblioteca para Figma. El usuario revisa cuando lo necesita; sus observaciones abren una corrección acotada. Nunca se simula aprobación humana ni se transforma una prueba fallida en PASS.

Pendiente: cargador automático de specs desde GitHub, catálogo remoto firmado/verificado, automatización de ingesta y ejecución periódica del laboratorio. Los ZIP actuales contienen snapshots; no se actualizan solos. La biblioteca Figma y el cliente Genspark requieren pruebas propias.

## Roles bajo demanda

| Perfil | Responsabilidad | Entrega |
|---|---|---|
| Orquestador | Define alcance, métrica, presupuesto y reutilización antes de delegar | Plan y decisiones visibles |
| Documentalista | Conserva fuentes y genera contratos/documentación trazable | Specs y referencias |
| Constructor | Materializa el trabajo solicitado en su destino autorizado | Código o nodos reales |
| Verificador | Comprueba integridad y criterios de aceptación | QA y evidencia con límites |
| Optimizador | Propone y compara mejoras contra una referencia medida | Resultado y recomendación |

Son responsabilidades, no cinco agentes obligatorios en cada ejecución. Las tareas deterministas usan scripts y las lecturas se acotan por familia y cambios. El coste incluye coordinación y correcciones; si no hay contador disponible se declara UNAVAILABLE.

## Comunicación visible

Cada encargo registra emisor, receptor, solicitud, motivo, alcance, entregable, estado, respuesta resumida y evidencia. Las solicitudes y resultados reales pueden consultarse; no se fabrica conversación entre agentes ni se presenta razonamiento interno como evidencia.

El ciclo es objetivo → referencia medible → hipótesis → experimento aislado → comparación → conservar o revertir → aprendizaje documentado. El cierre exige QA verificable, sin revisión humana rutinaria como puerta.

## Consumo por diseñadores

La skill Figma requiere MCP remoto compatible y autenticado, capacidad de escritura y URL de un archivo destino distinto del maestro, o una solicitud explícita de crearlo. Los componentes del DS tienen prioridad: la biblioteca debe ser accesible, o sus componentes ya estar disponibles con identidad verificable en el destino. Si falta acceso se avisa; no se recrea una familia existente como sustituto. Los componentes locales nuevos cubren necesidades ausentes del catálogo.

La skill de PO genera prototipos HTML y su handoff, sin requerir conexión Figma. GitHub público permite consultar documentación sin autenticación; no concede acceso a bibliotecas Figma.

## Mantenimiento

Las reglas operativas están en AGENTS.md y protocols/. Los registros conservan estados y límites por destino. El objetivo de distribución futura separa versión del motor de skill y versión del contenido del DS; cada ejecución fijará un mismo corte compatible y descargará solo lo necesario. Ese cargador no se presupone implementado por la presencia de este repositorio.

## Actualización: consumo GitHub implementado

Esta sección sustituye el estado anterior de cargador pendiente. Los motores nuevos consultan el canal público catalog/current.json en cada encargo, validan hashes y crean un corte de ejecución. La publicación de datos es independiente de la versión instalada. El workflow de main regenera y publica el canal tras pasar sus comprobaciones; una automatización pendiente o fallida conserva la última publicación. Los ZIP se entregan solo localmente. El uso real de Genspark sigue pendiente de prueba del usuario.
