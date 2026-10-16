# QA de implementación · Typography 0.1.0

**Fecha:** 2026-10-15 · **Resultado global:** `PARTIAL / BLOCKED` · **Auditoría humana:** `PENDING`.

La solicitud permite documentar los 18 estilos de la referencia y los complementarios necesarios para conservar los componentes existentes. El [contrato](../../specs/foundations/typography.contract.v0.1.0.md) gobierna las reglas; el [JSON canónico](../../specs/tokens/ai-design-system.typography.v0.1.0.json) centraliza las recetas, su única `description`, las referencias semánticas y la evidencia. El JSON es necesario para generar y comprobar Figma, CSS, TypeScript y los paquetes de las dos skills desde los mismos datos. No añade una fuente editable paralela de valores.

## Resultados por destino

| Destino / control | Resultado | Alcance y evidencia |
|---|---|---|
| Catálogo y documentación | `PASS` documental | 75 recetas: 18 base, 54 de compatibilidad con los contratos existentes y tres derivadas de escalas observadas. [QA documental](../contracts/typography.v0.1.0.md). |
| TextStyles en AI-Design-System | `PASS` técnico | 75 IDs reales, 304 bindings semánticos y 1,216 resoluciones en cuatro modos, verificados mediante readback independiente. [QA de estilos](../../implementations/figma/typography.v0.1.0.styles.qa.json). |
| Página Typography | `PASS` acotado | 75 tarjetas, 316 textos y 79 frames; estilos, medidas, variables y geometría comprobados. [Readback](typography/specimens.readback.json) y [revisión visual](typography/specimens.review.md). [Abrir Figma](https://www.figma.com/design/tj3WIBEZDGLVs7MJWKCwgf/AI-Design-System?node-id=1006-292). |
| Consumo en componentes Figma existentes | `BLOCKED` | La asignación de estilos reproduce propagación entre variantes de Button. El mapping completo no acredita una migración ejecutada. [Diagnóstico y condiciones de cierre](typography/Figma-blocker.md). |
| Preservación de los componentes existentes | `PASS` con adiciones identificadas | Readback de 34 páginas, 3,501 textos y 3,503 rangos: métricas, cajas, contenido, formato e IDs originales conservados. Solo se permiten 244 rangos con bindings canónicos añadidos a 17 TextStyles preexistentes. [QA independiente](../../implementations/figma/typography.v0.1.0.preservation.qa.json). |
| Restauración literalmente idéntica de bindings | `FAIL` conservado | El control estricto detecta las 244 diferencias aditivas. Se conserva sin sobrescribirlo ni convertirlo en una validación del consumo. [Reporte estricto](../../implementations/figma/typography.v0.1.0.restoration.qa.json). |
| Biblioteca web | `PASS` en alcance medido | 75 estilos × cuatro temas y 2,956 textos de 43 familias × cuatro temas. El generador, TypeScript y build pasan; los consumidores y 717 reglas no tipográficas se preservan. [Corte de 75 estilos](typography/web/revision-75/README.md) y [suite previa de 61 pruebas](typography/web/README.md). |

Los complementarios conservan necesidades ya presentes: no amplían la escala base para nuevos diseños sin justificación. Las tres recetas fraccionarias materializan escalas existentes y no deben escalarse de nuevo. Los 150 textos editoriales históricos del censo están identificados fuera del consumo UI. Logos y otros elementos sin texto no necesitan un estilo tipográfico.

## Límite pendiente

El catálogo compartido está disponible, pero no todos los componentes Figma consumen todavía su estilo. Los intentos fallidos y las restauraciones permanecen como evidencia; todas las copias temporales de diagnóstico se eliminaron. La reconstrucción de textos en una copia de Button tampoco superó el QA, por lo que no existe una propuesta de sustitución validada para aplicar a los maestros.

La revisión automática de aprobación rechazó repetir escrituras sobre componentes vivos después de observar propagación entre variantes y rechazó inicialmente un reset de overrides sin protección suficiente. Se continuó con respaldos, una prueba acotada de overrides y copias aisladas. El rechazo no se usa como excusa para omitir la documentación, el QA web o el catálogo; sí impide afirmar un cierre completo sin una solución segura y comprobada del fallo de Figma.

No se publicó la biblioteca remota ni se simula aprobación humana. La actualización de las skills se registra por separado en [registry/skills.md](../../registry/skills.md); la vigencia del grafo se acredita por su cierre de P05, no por este informe.

## Reproducción

El [validador de foundation](../../implementations/figma/typography_foundation_qa.py) coteja el catálogo, los estilos reales, las variables y el censo final. La prueba negativa de identidad de alias falla incluso cuando otro token resuelve al mismo número. El [validador general](../../implementations/figma/typography_qa.py) conserva la comprobación estricta de restauración y la de migración; estos controles no se sustituyen por el validador de preservación acotada.

Antes de reintentar la migración se necesita resolver el fallo reproducible de vinculación. Después se debe leer todo el conjunto afectado tras la última escritura, incluyendo instancias, propiedades, overrides, contenido, bindings y geometría. Una lectura favorable dentro de un bucle de asignación no es evidencia suficiente.
