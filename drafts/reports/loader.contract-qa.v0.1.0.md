# Loader · QA documental 0.1.0

Estado: PASS para construcción delegada en Figma; auditoría humana PENDING. Fecha: 2026-09-25. Alcance: contrato Loader 0.1.0, fuente observada, inventario de tokens y brechas de Phase 0.

## Cobertura y trazabilidad

- Fuente leída: set público de 16 variantes, cuatro sets internos de 24 fotogramas, 96 reacciones, gradientes, remates, tamaños e IDs. Contrato fuente MD/YAML independiente de la implementación.
- JSON canónico: sources/inventories/tokens.inventory.json, SHA-256 cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474. Cuatro roles color/icon existentes con scope SHAPE_FILL y variables locales identificadas en los cuatro modos. Sin creación de token ni alteración del JSON.
- Destino: AI Design System, página semántica propuesta Loaders; no existía al cierre de Phase 0. El contrato diferencia fuente, destino, reglas, ejemplos y límites web.
- Requisitos comprobables: 16 variantes públicas, 16 ciclos internos de 24, 384 reacciones, 384 bindings de stop opaco y 384 de remate, cuatro modos, medidas discretas e IDs separados.

## Resolución de anomalía

La fuente solo personaliza el primer fotograma de Secondary, Default y On color; los siguientes conservan Primary. El contrato exige un ciclo interno completo para cada combinación Size×Color. La mejora preserva los RGB originales y evita el salto cromático durante la animación. Se registra como decisión delegada de migración para auditoría por excepciones, no como comportamiento histórico de la fuente.

## Límites que no bloquean Figma

Reduced motion, etiqueta accesible y API web son UNRESOLVED en el producto de código; el contrato no afirma que Figma los implemente. La persistencia de variables en stops de gradiente es riesgo de implementación y debe validarse antes de declarar PASS técnico. Si falla, se bloquea la construcción cromática afectada; no se reemplaza silenciosamente por un literal.

## Gate

No se hallaron conflictos bloqueantes para iniciar P04. La delegación vigente permite construir sin aprobación previa por componente. La promoción a specs/ queda condicionada a QA de implementación PASS, sin convertir la auditoría humana en aprobada.
