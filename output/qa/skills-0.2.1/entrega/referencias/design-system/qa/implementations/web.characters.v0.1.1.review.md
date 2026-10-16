# QA-WEB-CHARACTERS-011 · corrección web 0.1.1

**Fecha:** 2026-10-13 · **Clasificación:** IMPLEMENTATION_DEFECT · **Resultado:** PASS para geometría y apariencia estática de Characters y BENI del Chat. [Resultados/hashes](web.characters.v0.1.1.results.json).

Usuario: «El logo de Beni se ve mal», con [captura del defecto](web.beni.v0.1.1.before.png). Se corrige la implementación existente bajo P06/P07, sin rediseñar el personaje. Se leyeron AGENTS, P07, P05/P06/P-SLOTS, [contrato Characters](../../specs/characters.contract.v0.1.0.md), snapshot, captura y QA Figma originales. P-SLOTS NOT_APPLICABLE para Characters: arte fijo. Los Slots de Conversation/Chat conservan su composición; el cambio se limita al dibujo reutilizado.

## Causa y corrección

El generador anterior anidaba directamente relativeTransform. En el snapshot de Ecosistema, los ojos bajo GROUP tienen la traslación referida al componente: para el primer ojo de BENI, grupo y vector comparten x≈69.94, y≈17.29. SVG sumaba ambas traslaciones y llevaba los ojos a la derecha y abajo. NAVI comparte el mismo patrón y estaba afectado.

[assets.py](../../implementations/web/scripts/assets.py) ahora lee directamente [el snapshot original](../../sources/figma-snapshots/characters.ecosistema.2026-10-08.json) y deriva matrices locales mediante inversa de absoluteTransform del padre × absoluteTransform del hijo. La raíz se conserva como origen del viewBox. No se cambia el path, color, tamaño, jerarquía ni proporción para compensar el error. La corrección aplica a los 6 frames BENI y 7 NAVI y sus consumidores web. API pública sin cambios.

## Verificación

- `pnpm verify`: generación/cobertura, TypeScript, 8/8 pruebas y export estático Next PASS.
- Prueba nueva: reconstrucción de coordenadas absolutas en los 64 vectores/13 frames, contra el snapshot independiente. Tolerancia 0.001px establecida previamente por CHARACTERS-001 AC-02.
- `pnpm test:browser --grep 'BENI|cuatro temas'`: 2/2 pruebas Chrome PASS. Matrices CTM reales de 47 paths pintados en 13 SVG y BENI en Chat coinciden con el snapshot; cuatro temas conservan identidad.
- [BENI corregido](web.beni.v0.1.1.png), [Chat en contexto](web.beni.v0.1.1.chat.png) y [13 frames web](web.characters.v0.1.1.png) inspeccionados contra la [captura Figma existente](../../implementations/figma/characters.v0.1.0.png): ojos alineados y formas/colores conservados.

El primer arranque de la prueba de navegador encontró una incompatibilidad del runner CommonJS con el paquete ESM Phosphor. La prueba renderiza su fixture mediante el runtime tsx existente, igual que las pruebas React, sin cambiar dependencias ni producción; la reejecución pasó. No se presenta aquel arranque fallido como PASS.

Se actualizaron la ficha Characters, notas de adaptación y vínculos QA de Characters/Conversation/Chat. Los resultados 0.1.0 permanecen históricos: sus comprobaciones no detectaban la transformación interna y no certifican este dibujo. La comparación es estática; no añade animación, certificación de accesibilidad ni auditoría visual de familias ajenas. No consulta/escribe Figma ni modifica tokens. El límite de assets Logos no pertenece a esta corrección.

## Cierre

Solicitud, modificación y evidencia quedan registradas aquí y en implementaciones/QA. Graphify STALE durante las ediciones; cierre completo `2026-10-13-web-characters-fix`. CURRENT únicamente si closure.json y scripts/ds check verifican el corpus final. Se preserva/restaura el corte anterior antes de cerrar semántica y AST; sin nuevas instalaciones. Uso semántico medido UNAVAILABLE.
