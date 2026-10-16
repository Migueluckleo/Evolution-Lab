'use client';
import type { AnchorHTMLAttributes, ButtonHTMLAttributes, ReactNode } from 'react';
import { Bell, PlusCircle } from '@phosphor-icons/react';
import { cx, type Size } from '../lib/utils';
import { Dot } from './feedback';

/** Acción nativa. Para navegación usa href; no se envían formularios por defecto. */
export type ButtonProps = {
  children?: ReactNode;
  variant?: 'primary' | 'default' | 'text' | 'link';
  size?: Size;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  showLeftIcon?: boolean;
  showRightIcon?: boolean;
  className?: string;
} & ({ href?: never } & ButtonHTMLAttributes<HTMLButtonElement> | { href: string; disabled?: never } & AnchorHTMLAttributes<HTMLAnchorElement>);
export function Button({ children='Default', variant='primary', size='large', leftIcon=<PlusCircle weight="light"/>, rightIcon=<PlusCircle weight="light"/>, showLeftIcon=true, showRightIcon=true, className, ...props }: ButtonProps) {
  const classes=cx('ds-button',`ds-button-${variant}`,`ds-size-${size}`,className);
  const content=<>{showLeftIcon && leftIcon && <span className="ds-icon">{leftIcon}</span>}<span className="ds-button-label">{children}</span>{showRightIcon && rightIcon && <span className="ds-icon">{rightIcon}</span>}</>;
  if ('href' in props && props.href !== undefined) return <a {...props as AnchorHTMLAttributes<HTMLAnchorElement>} href={props.href} className={classes}>{content}</a>;
  return <button type="button" {...props as ButtonHTMLAttributes<HTMLButtonElement>} className={classes}>{content}</button>;
}
export interface IconButtonProps extends Omit<ButtonHTMLAttributes<HTMLButtonElement>,'children'> {
  /** Nombre obligatorio, incluso cuando el icono parece reconocible. */
  label: string;
  icon?: ReactNode;
  variant?: 'ghost' | 'outline';
  size?: 'small' | 'medium' | 'large';
  /** Texto aportado por la pantalla; sin regla automática de 99+. */
  count?: string;
  showCount?: boolean;
}
export function IconButton({label,icon=<Bell weight="light"/>,variant='ghost',size='small',count='1',showCount=true,className,...props}:IconButtonProps){
  return <button type="button" {...props} aria-label={label} className={cx('ds-icon-button',`ds-icon-button-${variant}`,`ds-icon-button-${size}`,className)}><span className="ds-icon">{icon}</span>{showCount&&<span className="ds-icon-count"><Dot type="count" size={size} count={count}/></span>}</button>;
}
export interface FilterChipProps extends Omit<ButtonHTMLAttributes<HTMLButtonElement>,'onChange'> {
  selected?: boolean;
  size?: Size;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  showLeftIcon?: boolean;
  showRightIcon?: boolean;
  onSelectedChange?: (selected: boolean) => void;
}
export function FilterChip({selected=false,size='large',leftIcon=<PlusCircle weight="light"/>,rightIcon=<PlusCircle weight="light"/>,showLeftIcon=false,showRightIcon=false,onSelectedChange,onClick,children='Chip',className,...props}:FilterChipProps){
  return <button type="button" {...props} aria-pressed={selected} onClick={e=>{onClick?.(e);if(!e.defaultPrevented)onSelectedChange?.(!selected);}} className={cx('ds-chip',`ds-size-${size}`,className)}>{showLeftIcon&&leftIcon&&<span className="ds-icon">{leftIcon}</span>}{children}{showRightIcon&&rightIcon&&<span className="ds-icon">{rightIcon}</span>}</button>;
}
