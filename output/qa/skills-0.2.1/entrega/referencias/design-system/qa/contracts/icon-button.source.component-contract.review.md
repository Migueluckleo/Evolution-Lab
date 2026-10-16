# QA-ICON-BUTTON-SOURCE-001 · fuente Button Icon

- **Resultado:** `PASS` documental de evidencia read-only; no aprueba diseño destino.
- **Identidad:** set `1430:18850`, key `fbc267a15caab7547a5d782a8887da547ee7cf03`, página `1430:18021`; captura 289×960 inspeccionada.
- **Cobertura:** 151/151 nodos, matriz 5×3×2 completa de 30 variantes, 60 instancias activas agrupadas en Bell Phosphor y tres variantes Count de Dot local, 27 variables únicas (21 locales/seis remotas), un estilo de efecto local y cero reacciones. PreferredValues del icono: 1512 candidatos contados superficialmente, no confundidos con dependencias activas.
- **Sincronización:** [MD](../../drafts/contracts/icon-button.source.component-contract.md) y [YAML](../../drafts/contracts/icon-button.source.component-contract.yaml) concuerdan en ejes, tamaños, IDs, 60 instancias y anomalía de Focus.
- **Riesgos observados:** Dot numérico usa rol `feedback/danger/icon` en fill de contenedor; solo Focus/Large/Default lleva `focus/outset`; Small 24 px y texto de conteo 4 px no demuestran accesibilidad. Son observaciones, no reglas de destino.
