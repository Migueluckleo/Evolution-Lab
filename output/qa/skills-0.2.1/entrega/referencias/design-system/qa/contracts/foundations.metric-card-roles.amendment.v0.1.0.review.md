# QA-FOUNDATIONS-METRIC-CARD-ROLES-001

- **Resultado documental:** `PASS` bajo autorización global de extensiones semánticas, auditoría humana posterior `PENDING`. No acredita todavía creación en Figma.
- **Fuentes:** Card/Metric observó ocho CurrencyCircleDollar, ocho ArrowUpRight y seis porcentajes. El inventario base permanece inmutable; la extensión JSON es el único dato editable nuevo.
- **Semántica:** `color/text/metric/trend` es `TEXT_FILL` exclusivo; `color/icon/metric/brand` es `SHAPE_FILL` exclusivo. Ambos usan aliases a primitivas ya existentes; ninguna primitiva nueva. El nombre del porcentaje no codifica ganancia/pérdida.
- **Contraste calculado en destino:** blue/400 5.07:1, green/500 5.41:1, orange/700 6.57:1, purple/500 5.77:1 sobre `color/background/subtle`; sobre blanco, 5.56:1, 5.93:1, 7.20:1 y 6.32:1 respectivamente. Supera 4.5:1 para texto y 3:1 para iconos en ambas superficies.
- **Verificación pendiente de Figma:** crear y leer de vuelta las dos variables, sus descripciones/scopes y cuatro aliases; registrar IDs y después auditar los consumidores.
