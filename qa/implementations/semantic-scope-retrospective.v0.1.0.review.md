# QA-SEMANTIC-SCOPE-001 · revisión retrospectiva de familias construidas

```yaml
qa_id: QA-SEMANTIC-SCOPE-001
review_type: CROSS_COMPONENT_BINDING_REVIEW
target: figma
executed_at: 2026-09-23
result: PASS
user_audit: PENDING
```

Se recorrieron en AI Design System los component sets Buttons, Chips, Tooltips, Badges y Toggles después de las correcciones documentadas de Toggle 0.1.2 y Button 0.2.1. La lectura comparó el ID de cada paint sólido renderizado con la variable local, scope técnico y función semántica de texto, superficie, borde, anillo de foco o icono. Un paint `visible:false` en una envoltura de icono Phosphor se distinguió de la geometría vectorial renderizada; no se contó como consumidor visible. Se revisaron variantes y estados, no solo la instancia default.

| Familia | Paints sólidos renderizados comprobados | Hallazgos vigentes |
|---|---:|---:|
| Buttons | 243 | 0 |
| Chips | 126 | 0 |
| Tooltips | 12 | 0 |
| Badges | 25 | 0 |
| Toggles | 24 | 0 |

Los 120, 60 y 6 paints de icono renderizados en Buttons, Chips y Badges, respectivamente, pertenecen a geometría iconográfica; ninguno usa un rol de texto. En Button se repararon nueve labels Disabled antes de esta lectura. En Toggle se repararon el fondo Off/Hover y el thumb Off/Disabled y se añadieron roles con scopes adecuados para borde y fondo. Las envolturas Phosphor contienen un fill blanco no ligado pero `visible:false` —60 en Chips y 12 en Badges— heredado del componente remoto; no aparece en el render y no se confundió con un paint de icono visible. Las variables de feedback con sufijo `/text` y `color/focus/ring` se clasificaron por su propósito completo y scope, no por prefijo simplista.

`PASS` acredita bindings de color renderizados y categoría semántica de estas cinco familias en este snapshot. No sustituye el QA estructural individual, no acredita estados futuros de contenido editado, accesibilidad funcional, web ni publicación de biblioteca.
