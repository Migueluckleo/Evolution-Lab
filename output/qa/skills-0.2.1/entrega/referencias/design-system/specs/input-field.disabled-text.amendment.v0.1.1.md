---
contract_id: INPUT-FIELD-001
amendment_id: INPUT-FIELD-DISABLED-TEXT-001
version: 0.1.1
status: APPROVED
approval_scope: Disabled value text color only
last_updated: 2026-09-28
base_contract: specs/input-field.contract.v0.1.0.md
decision_ref: DEC-INPUT-FIELD-DISABLED-TEXT-001
review_targets: [figma]
figma_page_name: Input Fields
---

# Input Field · texto Disabled 0.1.1

## Autoridad y alcance

El usuario aprobó expresamente la propuesta de usar `color/text/disabled` tanto para el placeholder como para el valor precargado: «De acuerdo aplica el cambio en su documentación y en figma». Esta aprobación es acotada; no aprueba el resto del contrato base ni cierra su auditoría humana.

Esta enmienda sustituye exclusivamente las reglas de color del texto principal de Disabled en REQ-IF-005, la tabla de tokens de la sección 10 y el ejemplo Small/Disabled/Filled de la sección 18 del [contrato base 0.1.0](input-field.contract.v0.1.0.md), SHA-256 `e01e90d9dbc4dfdfc4230aac875f8d8a7374673b0a02bbda44eabf9962403c2d`. El resto del contrato permanece vigente. La fuente histórica y sus observaciones no se alteran.

## Regla vigente

REQ-IF-DISABLED-001: cuando `State=Disabled`, el texto principal MUST usar el rol semántico `color/text/disabled` para los tres tamaños y ambos valores Empty/Filled. Filled no habilita otro estilo de Disabled ni utiliza `color/text/primary`.

`Value=Empty` representa placeholder; `Value=Filled` representa contenido real o precargado. Comparten el tratamiento visual Disabled, pero no el significado del contenido. La propiedad de texto sigue siendo editable por el diseñador; eso no implica que el usuario final pueda editar el campo.

El cambio de binding se limita a las variantes Filled/Disabled Large `395:638`, Medium `395:654` y Small `395:670`, textos `395:647`, `395:663` y `395:679`. Empty/Disabled ya consume el rol correcto. Se conservan las 30 variantes, IDs, propiedades, cadenas de demostración, geometría, iconos, fondos, bordes y tipografía. No se añaden reacciones ni comportamiento web.

## Tokens y trazabilidad

- JSON canónico: `sources/inventories/tokens.inventory.json`, SHA-256 `cfb17800870306782499f7697e79ca1a13ddfedfe6b225d563ef0d5707fd3474`.
- Rol existente: `color/text/disabled`, variable local `VariableID:13:30`, colección semantic `VariableCollectionId:6:2`, tipo COLOR, scope TEXT_FILL.
- Alias existente a `color/neutral/400`, variable local `VariableID:8:96`, en los cuatro modos. Los valores y la descripción siguen gobernados por el JSON; no se añade catálogo paralelo ni nuevas variables.
- Destino: AI Design System `tj3WIBEZDGLVs7MJWKCwgf`, página Input Fields `394:122`, set `397:152`.
- La desviación respecto al texto oscuro fuente es intencional y aprobada para evitar una señal visual de editabilidad.

## Criterios y revisión documental

AC-DISABLED-001: seis variantes Disabled con el mismo binding de texto principal; únicamente tres fills cambian.
AC-DISABLED-002: las otras 24 variantes conservan su binding; IDs, propiedades, dimensiones y contenido permanecen iguales al preflight.
AC-DISABLED-003: token local, scope y cuatro aliases coinciden con el inventario; cero variables creadas/modificadas.
AC-DISABLED-004: captura posterior confirma Filled/Disabled visualmente atenuado; descripción del set explica la independencia entre estado y contenido.

QA documental PASS antes de escritura: cambio respaldado por aprobación explícita, sustitución acotada y verificable, variable existente resuelta en preflight; no hay contradicción con campos del JSON. La implementación requiere lectura posterior y QA separado.

## Límites

El contraste Disabled sobre la superficie sutil sigue en 2.34:1, registrado como limitación contextual; no se declara conformidad de accesibilidad ni se recolorea por contraste. La aprobación de esta decisión no equivale a publicación de biblioteca Figma ni a aprobación global de Input Field.
