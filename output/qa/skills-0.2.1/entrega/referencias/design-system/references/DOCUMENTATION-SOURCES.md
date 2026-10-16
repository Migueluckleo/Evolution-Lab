# Fuentes y alcance de esta documentación

## 1. Decisiones del proyecto aportadas por el usuario

SDD significa Specs Driven Design. Los contratos se entregan como Markdown y pueden apoyarse en JSON. La documentación aprobada del repositorio es la fuente de especificación, con Figma y frontend como destinos.

El usuario pidió separar entorno, ingesta, construcción, autodocumentación y QA; después añadió síntesis de contratos a partir de JSON o nodos antes de construcción. También definió el archivo destino y una página por familia de componentes.

Destino aportado: `https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=0-1`. Esta entrega documenta la decisión; no vuelve a inspeccionar ni modificar ese archivo.

## 2. Documentación local revisada

Se revisó el paquete previo `sdd-codex-protocols/`: AGENTS, README y sus cinco protocolos. La actualización conserva sus responsabilidades y reglas fundamentales; los cambios de autoridad/estados necesarios para incorporar aprobación explícita se enumeran en CHANGELOG y requieren la integración autorizada del usuario.

No se afirma haber inspeccionado la carpeta local del usuario desde este entorno. Codex debe comparar las versiones realmente existentes allí durante la migración.

## 3. Ejemplo educativo de Button

Archivo proporcionado en la conversación: `Markdown(9).md pegado`. Se utiliza como referencia de organización y profundidad: metadatos y 21 secciones, desde Purpose hasta Changelog, incluyendo anatomía, propiedades, estados, comportamiento, tokens, mapping y aceptación.

No se adopta como contrato aprobado del Button del proyecto. Sus tokens ilustrativos, números, props, variantes, paquete de código y `status: stable` no se transfieren a los candidatos. Las plantillas corrigen su forma sintáctica para ser utilizables sin afirmar que sus decisiones de diseño hayan sido verificadas.

No se incluye una copia del ejemplo dentro de `specs/` ni se crean contratos reales a partir de él. Los placeholders de las plantillas deben reemplazarse con evidencia de las fuentes que se entreguen después.

## 4. Fuentes técnicas externas consultadas

Consulta: 2026-09-22. Se usan únicamente para las instrucciones técnicas de herramientas; no definen tokens, anatomía ni intención de nuestro sistema.

### OpenAI: instrucciones de Codex

`https://developers.openai.com/codex/guides/agents-md/`

La documentación consultada explica el descubrimiento de AGENTS y la construcción de su cadena de instrucciones al inicio de una ejecución/sesión. El diseño de P02/P03 y del esquema local de contratos es una decisión de este proyecto, no una funcionalidad automática prometida por Codex.

### Graphify: instalación

`https://github.com/Graphify-Labs/graphify`

El README consultado distingue instalación del paquete y registro de la skill. P01 conserva los comandos pertinentes y pide verificarlos contra la versión realmente instalada antes de usarlos. No se instaló ni ejecutó Graphify para preparar esta entrega.

## 5. Límites de verificación

Se verificaron localmente estructura, archivos, referencias relativas, YAML de las plantillas e integridad del paquete. No se ejecutó la integración dentro de Codex ni se verificó comportamiento de Figma/frontend. Ningún reporte de este paquete sustituye esos pasos.
