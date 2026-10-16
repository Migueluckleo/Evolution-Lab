# FileUpload · React / TypeScript

Documento técnico generado por `pnpm ds:generate`. Editar la API en código, el ejemplo ejecutable o las notas de `components.registry.json`, y regenerar. No es otra aprobación del contrato visual.

Familia `FILEUPLOAD-001` · API local 0.1.0 · categoría Formularios.

## Uso sin backend

Solo entrega File[] al consumidor, sin red, persistencia ni lectura del contenido. accept orienta al selector, no valida seguridad, tamaño ni archivos arrastrados. status es externo: seleccionar archivo no muestra éxito. El ejemplo distingue selección de carga.

```tsx
'use client';
import { useState } from 'react';
import { ArrowRight, Bell, Check, CurrencyCircleDollar, FileText, Gear, House, HouseLine, Question, Info, Plus, Trash } from '@phosphor-icons/react';
import * as DS from '@/index';

export function FileUploadExample(){const [files,setFiles]=useState<string[]>([]);return <div className="grid gap-3"><DS.FileUpload onFilesChange={items=>setFiles(items.map(f=>f.name))} formats="Selecciona archivos de tu equipo. No se enviarán." multiple/><p role="status">{files.length?`Seleccionados localmente: ${files.join(', ')}`:'Ningún archivo seleccionado'}</p></div>;}
```

Ejemplo compilado en [examples.tsx](../../src/examples.tsx). Usa React state en memoria; recargar restaura la muestra. No hay endpoint, credencial ni persistencia implícita.

## API tipada

Importar desde [src/index.ts](../../src/index.ts), con `@/index` dentro del catálogo. Código propietario: [forms.tsx](../../src/components/forms.tsx). Los atributos HTML heredados mantienen los tipos de React; callbacks y datos controlados pertenecen a la pantalla. `Size` es small/middle/large cuando se referencia; los tamaños propios están enumerados en cada API.

```tsx
export interface FileUploadProps { label?: string; actionText?:string; formats?: string; helper?: string; accept?: string; multiple?: boolean; disabled?: boolean; status?: 'default'|'success'|'error'; statusMessage?: string; onFilesChange: (files:File[])=>void; prefixText?:string; suffixText?:string; showHelper?:boolean; showButton?:boolean; buttonLabel?:string; onButtonClick?:()=>void; icon?:ReactNode; successMessage?:string; errorMessage?:string }
```

## Defaults y eventos

Las firmas siguientes se extraen de las funciones, incluidos sus valores por defecto. Una prop sin asignación `=` es obligatoria o permanece undefined según su tipo; no se rellena con reglas de negocio.

```tsx
FileUpload: {label='Seleccionar archivo',actionText='subir tu archivo',formats='Formatos compatibles: .XLS, XLSX o CSV - Tamaño máximo 50 MB',helper='Optional helper text',accept,multiple,disabled,status='default',statusMessage,onFilesChange,prefixText='Haz clic para',suffixText='o arrástralo aquí',showHelper=true,showButton=false,buttonLabel='Volver a cargar',onButtonClick,icon,successMessage='Archivo cargado exitosamente',errorMessage='Error al cargar el archivo'}:FileUploadProps
```

Props `on…` son callbacks locales. No atribuyen autorización, carga, guardado ni resultados de negocio. Los iconos de intercambio usan `@phosphor-icons/react`; una posición de icono no admite texto que simule un icono.

## Composición y Slots

P-SLOTS: **NOT_APPLICABLE**. Anatomía fija; texto, icono o estado tipado. Sin lista de composición abierta. ReactNode/listas tipadas son la traducción web de las regiones, no evidencia de Slots Figma. El anfitrión conserva el orden y los IDs de listas; las cantidades de las demos no son límites de producto.

## Estilos y Next.js

Importar [styles.css](../../src/styles.css) una vez desde el layout de Next. Incluye Tailwind 4, Manrope local y las variables CSS generadas desde el inventario/enmiendas. Las recetas de texto se consumen por rol y variante desde [TYPOGRAPHY.md](../TYPOGRAPHY.md), tabla derivada del JSON tipográfico único; [typography.manifest.json](../../src/generated/typography.manifest.json) conserva métricas, unidades, referencias, identidad y hash. `typographyClass(id)` expone las clases tipadas y `--ds-type-style-id` permite inspeccionar la receta efectiva sin duplicar sus valores. El [manifiesto de tokens](../../src/generated/tokens.manifest.json) conserva nombres, description, aliases, modos, valores y hashes. Las tablas de tokens de los contratos citados abajo y las reglas de styles.css documentan los roles usados por esta familia; los componentes compuestos heredan los roles de sus piezas. Cambiar tema con `data-ds-theme="contable|administrativo|servicios|personas"` en el contenedor. Logos conserva artwork original y Characters conserva identidad fija.

Los ejemplos que usan estado/eventos requieren `'use client'`. Los datos serializables pueden venir de un Server Component; crear callbacks en una frontera cliente. No enviar funciones desde el servidor. No se requiere backend para el catálogo ni para componer con fixtures.

## Fuentes y límites

- [file-upload.contract.v0.1.0.md](../../../../specs/file-upload.contract.v0.1.0.md) · SHA-256 `e069fb28b37cb08c73300ace453d5318858f912f078566e87c731cc874ae4fb5`.

Las enmiendas sustituyen solo su alcance explícito. Los estados de aprobación, auditoría y excepciones visuales permanecen en esas fuentes. La API web inicial no certifica identidad pixel a pixel ni conformidad WCAG completa. Ver [decisiones web](../WEB-ADAPTATION.md) para las adaptaciones de HTML, geometría y comportamiento.

## Verificación

`pnpm verify` comprueba generación/cobertura, TypeScript, pruebas y build estático. `pnpm test:browser` valida los recorridos locales. [Evidencia de QA](../../../../qa/implementations/web.contract-audit.v0.1.3.review.md) identifica alcance, resultados y límites; una demo visible por sí sola no es un PASS visual.
