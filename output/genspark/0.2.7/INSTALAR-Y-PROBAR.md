# Instalar y probar en Genspark

Corte público 0.2.7. Ambos paquetes usan el mismo snapshot del DS, con el correo corporativo anonimizado. Integridad de ZIP y equivalencia del contenido comprobadas; ejecución dentro de Genspark NOT_RUN.

## Instalar

1. Abre Skills en Genspark.
2. Selecciona + New Skill → Upload/Subir.
3. Sube cada ZIP por separado y guarda la skill. Cada archivo incluye skill.md en la raíz, con nombre y descripción; pesan menos de 200 MB.
4. Selecciona la skill instalada antes de enviar el encargo.

La ayuda oficial documenta la carga de ZIP con skill.md y el límite de 200 MB: https://www.genspark.ai/es/helpcenter/skills . No se necesita conector GitHub para abrir el repositorio público.

## Prototipos PO

Instala contpaqi-po-prototypes. No requiere Figma MCP ni biblioteca Figma. La ejecución necesita un entorno que pueda ejecutar los scripts y compilar React/TypeScript con Node y el gestor de paquetes requerido por el starter. Pide una pantalla sencilla con componentes documentados; comprueba que entrega HTML autónomo y Markdown de traspaso, que el HTML abre sin servidor y que sus interacciones funcionan. La importación del ZIP no garantiza por sí sola esas capacidades del entorno.

## Pantallas Figma

Instala contpaqi-figma-screens. Conecta el MCP remoto de Figma con tu propia cuenta y verifica capacidad de escritura. El cliente debe disponer de las herramientas y manuales oficiales requeridos por la skill, incluyendo figma-use y los auxiliares según la operación. Guía oficial: https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/ . La capacidad de escritura de Figma desde Genspark no fue comprobada en esta entrega; si no se ofrece, la skill debe informar el límite.

Habilita la biblioteca DS accesible en un archivo de destino distinto del maestro. Proporciona su URL o solicita un archivo nuevo. La skill prioriza componentes reales del DS; no recrea una familia inaccesible. Solo crea componentes nuevos locales cuando no hay cobertura. No escribe en AI-Design-System.

Prueba primero sin MCP: debe avisar de la conexión necesaria. Luego con MCP y sin URL: debe pedir destino o creación. Finalmente, con destino y biblioteca, solicita una pantalla simple y revisa instancias editables, tokens, Auto Layout, interacciones y reporte QA. La falta de acceso a una pieza bloquea esa pieza, sin inventar resultados.

## Estado de actualización

Estos ZIP contienen una copia versionada. El cargador que consultará futuras versiones del catálogo GitHub todavía no está implementado: instalar estos paquetes no activa actualización automática. El repositorio es la fuente publicada y mantiene el plan en EVOLUTION-LAB.md. Una próxima actualización del motor conectará ese consumo; no se debe confundir con una función ya probada.
