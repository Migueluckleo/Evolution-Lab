# Loader · análisis de brechas de Phase 0

**Fecha:** 2026-09-25. **Fuente:** Figma Libreria v1.1.0, página `❖ Loader` (`3917:1263`), set público `7561:47164` y sets internos `4283:240`, `7556:45810`, `7556:46291`, `7556:46652`. **Destino:** AI Design System, archivo `tj3WIBEZDGLVs7MJWKCwgf`. Lectura de fuente de solo lectura; ninguna escritura Figma en esta fase.

## Inventario cerrado

- `P0.a`: 16 variantes públicas observadas: `SIze={Sm,Md,Lg,Xl}` × `Color={Primary,Secondary,Default,On color}`. Lados 24, 40, 64, 88 px. La grafía `SIze` es literal del origen y no obliga a conservarla como nombre de propiedad del destino.
- Cuatro sets internos de 24 fotogramas cada uno. En los 96 fotogramas se comprobaron cero errores de enlace secuencial, ángulo, estructura y temporización: 15° por paso, `AFTER_TIMEOUT` de 0.001 s, `CHANGE_TO` con `SMART_ANIMATE` lineal de 0.05 s; el último vuelve al primero.
- La forma visible es un anillo con gradiente angular y un remate vectorial. El color opaco del gradiente y el remate son `#3255F7`, `#64748B`, `#0F172A` o `#FFFFFF` según variante. En origen solo Primary liga el stop opaco a variable; los otros tres stops son literales, aunque los cuatro remates usan variables. Los stops transparentes y el operando de sustracción no aportan color visible de producto.

## Destino y reutilización

- `P0.b`: no existe página `Loaders` ni componente Loader local. El archivo tiene colecciones `primitive` y `semantic`; esta última tiene los cuatro modos Contable, Administrativo, Servicios y Personas.
- Los roles locales existentes `color/icon/brand`, `color/icon/secondary`, `color/icon/primary` y `color/icon/on-brand` tienen scope `SHAPE_FILL` y cubren las cuatro variantes de color. `brand` cambia de primitiva en cada tema. El inventario base aprobado tiene SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- `P0.c`: la búsqueda de biblioteca encuentra el Loader de la Librería antigua y spinners genéricos. Ninguno es un componente Loader local del destino con el contrato de 16 variantes y 96 fotogramas; se reconstruirá localmente sin dependencia remota.

## Alcance y brechas

- `P0.d`: página semántica propuesta `Loaders`; un set público de 16 variantes y cuatro sets internos de 24 fotogramas. No se agregan estados, colores, tamaños ni comportamiento web inferidos. La animación Figma forma parte del alcance.
- `P0.e`: el origen tiene tres gradientes con color literal por tamaño; el destino exige binding semántico también en los stops opacos y remates. La API expone `ColorStop.boundVariables`, pero falta demostrar en una construcción real que el binding persiste al escribir el gradiente y cambiar de fotograma. Esta es una verificación técnica de P04, no una licencia para hardcodear.
- `P0.e`: en los colores Secondary, Default y On color, los overrides cromáticos solo están en el primer fotograma público; los restantes de los sets internos permanecen Primary. El destino debe crear ciclos completos por combinación Size×Color para que el color no cambie al animar. Eso amplía la dependencia interna a 16 secuencias de 24 fotogramas, manteniendo 16 variantes públicas.
- `P0.f`: no se necesitan tokens, colecciones ni primitivas nuevas. La divergencia intencional será Primary temático, color persistente durante la animación y el cierre de los tres bindings faltantes de gradiente. Contrato y QA se prepararán antes de crear la página.

**Gate:** evidencia suficiente para sintetizar contrato. Figma destino sigue `NOT_STARTED`; no declarar implementación ni publicación.
