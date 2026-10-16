import type { CSSProperties } from 'react';
export type Size = 'small' | 'middle' | 'large';
export type Theme = 'contable' | 'administrativo' | 'servicios' | 'personas';
export const cx = (...values: (string | false | null | undefined)[]) => values.filter(Boolean).join(' ');
export const token = (name: string) => `var(--ds-${name.replaceAll('/', '-')})`;
export const vars = (values: Record<string, string | number>) => values as CSSProperties;
