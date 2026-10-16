# QA-NAVIGATION-SWITCH-TAB-FIGMA-001

- **Resultado:** `PASS` técnico para [NAVIGATION-SWITCH-TAB-001](../../specs/navigation-switch-tab.contract.v0.1.0.md); implementación `VALIDATED`, auditoría humana `PENDING`, Figma `UNPUBLISHED`.
- **AC-NAV-ST-001/002:** componente único `Switch Tab` en la página `Navigation`; cuatro instancias del `Switch Tab Item` local en orden Active, Default, Default, Default. Readback: 488×46 px, hijos 120/116/116/116×38 con x=4/128/248/368 y y=4, gap/padding 4 y radio 8.
- **AC-NAV-ST-003:** fill ligado a `color/background/subtle` (`FRAME_FILL`) con alias a neutral/200 `#F1F5F9` en los cuatro modos, igual al origen. Cinco bindings a `spacing/xs` para gap/padding y cuatro a `radius/md` pasaron lectura real. El primer chequeo asumió erróneamente arrays para aliases geométricos; la lectura del formato de objeto real corrigió nueve falsos positivos y devolvió cero errores.
- **AC-NAV-ST-004/005:** captura fuente y destino inspeccionadas, con un tab activo morado y tres default sobre el gris sutil. Cero reacciones. Los [IDs y límites](../../implementations/figma/navigation-switch-tab.v0.1.0.state.json) quedan registrados. No se declara comportamiento, selección exclusiva ni accesibilidad web.

**Límite:** solo la composición de cuatro items observada. `Tab` y `Pagination` no están cubiertos por este QA.
