# Instalar y probar el consumo GitHub en Genspark

Estos ZIP contienen el motor de las skills, sin specs fijos. Cada nuevo encargo consulta el canal público de Evolution Lab y descarga datos verificados. No requieren cuenta ni token de GitHub. Los paquetes anteriores 0.2.x no cumplen este flujo; usa los nuevos.

## Instalación

En Genspark abre Skills → + New Skill → Upload/Subir. Carga cada ZIP por separado y guarda. Cada uno contiene skill.md en raíz. La instalación de ZIP está documentada en https://www.genspark.ai/es/helpcenter/skills .

El entorno que ejecute la skill necesita Python 3.10 o posterior, ejecución de scripts, HTTPS hacia raw.githubusercontent.com y almacenamiento de trabajo. La skill ejecuta scripts/resolve_ds.py para crear una carpeta con el corte remoto verificado. Si Genspark no ofrece estas capacidades, debe informar el bloqueo; importar un ZIP no prueba compatibilidad completa. La ejecución dentro de Genspark sigue NOT_RUN hasta tu prueba.

## Prueba inicial

Pide una pantalla pequeña y solicita que el reporte incluya versión del motor, identidad del catálogo, digest del DS y contratos usados. Antes de construir debe consultar GitHub y producir un resultado PASS del cargador. Si falla red, catálogo o integridad, no debe sustituirlos por specs antiguos.

Cuando publiques un cambio compatible en las fuentes de GitHub, espera a que el workflow Publicar catálogo de consumo termine correctamente. Abre un nuevo encargo con la misma skill instalada: deberá consultar la nueva publicación sin reinstalar el ZIP. Una tarea ya iniciada conserva su corte para evitar mezclar versiones. Los cambios de protocolo del motor sí pueden requerir actualizarlo.

## Prototipos PO

No exige Figma. Necesita Node, gestor de paquetes, compilación React/TypeScript/Next y navegador para las pruebas indicadas. Comprueba HTML autónomo, interacciones y Markdown de traspaso. El HTML entregado funciona offline; obtener specs y preparar el proyecto sí requiere red.

## Pantallas Figma

Conecta tu propia cuenta mediante MCP Figma con escritura disponible, proporciona URL de un archivo destino distinto de AI-Design-System y habilita la biblioteca DS accesible en ese archivo. La skill prioriza instancias reales; no recrea familias existentes por falta de acceso. Sin MCP, permiso, biblioteca o destino correcto debe explicar el requisito y detener solo lo afectado. Genspark debe exponer las herramientas y manuales oficiales necesarios; su capacidad real de escritura Figma no se ha probado aquí.

Los ZIP se entregan localmente. En GitHub se publican fuentes, protocolo, catálogo y datos de consumo, no estos instaladores.
