# Síntesis APP-SHELL-0010.1.0

Solicitud explícita: «Incluyelo en el DS con nuestros tokens y json canonico», referente al nodo8284:12565 de la Librería anterior. Fuentes: snapshot de148nodos, contratos vigentes Header/Sidebar, JSON canónico, preflight real de destino y protocolos P02/P03/P04/P05/P06/P-SLOTS.

Decisiones delegadas: nombre funcional App Shell; una página/una composición; Auto Layout vertical sin alterar marco1440×1024; gap de rail normalizado a0por tener un hijo; Slots Content0..n; reutilizar componentes locales en lugar de internals fuente. No se adoptan breakpoints desconocidos ni las propuestas todavía DRAFT de Anticipa.

Cobertura: envoltura y dependencias directas resueltas; iconos, tipografía y controles anidados se consumen de Header/Sidebar y conservan sus contratos/extensiones. La inspección histórica no vuelve a certificar toda la librería. QA documental PASS; construcción autorizada por delegación, auditoría humana posterior por excepciones.

Transformación trazable: fuente blanca sin binding → color/background/default; spacinglg/xl fuente → variables locales con mismas identidades lógicas; esquinas y ceros → radius/none/spacing/none. Cero variables/primitivas nuevas. No se edita inventario histórico ni se publicará remotamente la biblioteca.
