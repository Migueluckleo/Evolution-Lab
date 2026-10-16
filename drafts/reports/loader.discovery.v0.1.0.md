# Descubrimiento inicial · Loader de Librería v1.1.0

**Estado:** `OBSERVED`, no contrato aprobado/delegado ni implementación. **Fecha:** 2026-09-24. **Fuente:** Figma `9zs5RMR8LB5wHjW9Bd59BA`, página `❖ Loader` (`3917:1263`). **Destino previsto:** AI Design System, página semántica `Loaders`; sin cambios de Loader en el destino a este corte.

## Inventario verificado

- Set público `Loader` (`7561:47164`, key `b7b6e1e6560ca57d1a8b9f431551d63fe65116eb`): 16 variantes, `SIze={Sm,Md,Lg,Xl}` × `Color={Primary,Secondary,Default,On color}`. Medidas de lado: 24, 40, 64 y 88 px. `SIze` es el nombre literal fuente, no una recomendación de destino.
- Cuatro sets internos ocultos en la página: `Loader sm` (`4283:240`), `Loader md` (`7556:45810`), `Loader lg` (`7556:46291`) y `Loader xl` (`7556:46652`). Cada uno tiene 24 componentes/fotogramas y un ciclo de 24 transiciones `AFTER_TIMEOUT` a `CHANGE_TO`, `SMART_ANIMATE` lineal de 0.05 s. El timeout observado es 0.001 s. El último fotograma vuelve al primero; los destinos de las transiciones están en el mismo set.
- Cada variante pública anida una instancia del primer fotograma del set de su tamaño; los cuatro colores aparecen como overrides de esa instancia. La pieza visible tiene anillo con relleno angular de tres stops y vector pequeño de remate. Primeros dos stops transparentes; último opaco. El color visible en la fuente es Primary `#3255F7`, Secondary `#64748B`, Default `#0F172A`, On color `#FFFFFF`.
- En la fuente el stop opaco Primary y el remate están ligados a variables de origen; Secondary/Default/On color muestran stop opaco literal y remate ligado. No trasladar esos IDs de origen al destino.

## Preflight de tokens del destino

Los roles locales existentes `color/icon/brand`, `color/icon/secondary`, `color/icon/primary` y `color/icon/on-brand` tienen scope `SHAPE_FILL` y se corresponden semánticamente, respectivamente, con Primary, Secondary, Default y On color. `color/icon/brand` cambia por los cuatro temas; no fijar Primary a blue/400 al construir. Aún falta probar el binding a los stops del gradiente angular y a los remates en las instancias animadas, así como verificar si los overrides se conservan al cambiar de fotograma. No declarar QA antes de ese readback.

## Siguiente operación autorizada de migración

Producir contrato fuente MD/YAML profundo y contrato destino en `specs/`, con QA documental; después crear página `Loaders`, los cuatro sets locales de animación y el set público sin dependencia remota. Probar el ciclo y la respuesta al tema antes de integrarlo como dependencia de Dropdown Item. No hay una decisión material pendiente del usuario con la evidencia actual.
