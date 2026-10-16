'use client';
import { cloneElement, isValidElement, useId, useState, type HTMLAttributes, type ReactElement, type ReactNode } from 'react';
import { CheckCircle, Info, Warning, X, XCircle, Presentation } from '@phosphor-icons/react';
import arrow from '../generated/tooltip-arrow.json';
import loader from '../generated/loader.json';
import { cx, token, vars } from '../lib/utils';

export interface DotProps { type?: 'active'|'busy'|'inactive'|'count'|'overflow'; size?: 'small'|'medium'|'large'; count?: string; label?: string }
export function Dot({type='active',size='large',count=type==='overflow'?'99+':'1',label}:DotProps){
  const role={active:'status-active',busy:'status-busy',inactive:'status-inactive',count:'notification-count',overflow:'notification-count'}[type];
  return <span className={cx('ds-dot',`ds-dot-${size}`,type==='overflow'&&'ds-dot-overflow')} style={vars({'--dot-fill':token(`color/background/${role}`),'--dot-border':token(type==='inactive'?'color/border/status-inactive':'color/border/on-brand')})} role={label?'img':undefined} aria-label={label} aria-hidden={label?undefined:true}>{['count','overflow'].includes(type)?count:null}</span>;
}
export interface BadgeProps extends HTMLAttributes<HTMLSpanElement> { tone?: 'base'|'light'|'informational'|'warning'|'error'|'success'; leftIcon?: ReactNode; rightIcon?: ReactNode; showLeftIcon?: boolean; showRightIcon?: boolean }
export function Badge({tone='base',leftIcon=<Presentation weight="fill"/>,rightIcon=<Presentation weight="fill"/>,showLeftIcon=true,showRightIcon=false,children='Light',className,...props}:BadgeProps){
  return <span {...props} className={cx('ds-badge',`ds-tone-${tone}`,className)}>{showLeftIcon&&leftIcon&&<span className="ds-icon">{leftIcon}</span>}{children}{showRightIcon&&rightIcon&&<span className="ds-icon">{rightIcon}</span>}</span>;
}
export interface InlineNotificationProps { tone?: 'light'|'success'|'danger'|'warning'|'info'; title?: ReactNode; children?: ReactNode; showIcon?: boolean; showTitle?: boolean; showDescription?: boolean; showDismiss?: boolean; icon?: ReactNode; onDismiss?: ()=>void; dismissLabel?: string; className?: string }
export function InlineNotification({tone='light',title,children,showIcon=true,showTitle=true,showDescription=true,showDismiss=true,icon,onDismiss,dismissLabel='Cerrar aviso',className}:InlineNotificationProps){
  const Icon={light:Info,info:Info,success:CheckCircle,danger:XCircle,warning:Warning}[tone];
  const severity={light:'light',info:'informational',success:'success',danger:'error',warning:'warning'}[tone];
  return <div className={cx('ds-notification',`ds-tone-${severity}`,className)} role="status"><span hidden={!showIcon} className="ds-feedback-icon">{icon??<Icon size={24} weight="light"/>}</span><div hidden={(!showTitle||title===undefined)&&(!showDescription||children===undefined)} className="ds-notification-copy min-w-0 flex-1"><p hidden={!showTitle||title===undefined} className="ds-notification-title">{title}</p><div hidden={!showDescription||children===undefined} className="ds-notification-description">{children}</div></div>{showDismiss&&<button type="button" className="ds-plain-button" aria-label={dismissLabel} onClick={onDismiss}><X size={16} weight="light"/></button>}</div>;
}
export interface LinearProgressBarProps { progress?: 25|50|75|100; tone?: 'primary'|'warning'|'positive'|'danger'; size?: 'small'|'medium'|'large'; label: string; helper?: string; showLabel?: boolean; showPercentage?: boolean; showHelper?: boolean }
export function LinearProgressBar({progress=25,tone='primary',size='small',label,helper='Optional helper text',showLabel=true,showPercentage=true,showHelper=true}:LinearProgressBarProps){
  return <div className={cx('ds-progress',`ds-progress-${size}`)}><div hidden={!showLabel} className="flex justify-between gap-2"><span hidden={!showLabel}>{label}</span><span hidden={!showPercentage}>{progress}%</span></div><div className="ds-progress-track" role="progressbar" aria-label={label} aria-valuemin={0} aria-valuemax={100} aria-valuenow={progress}><div className="ds-progress-fill" style={{width:`${progress}%`,background:token(`color/background/progress/${tone}`)}}/></div><p hidden={!showHelper||helper===undefined} className="ds-helper">{helper}</p></div>;
}
export interface LoaderProps { size?: 'sm'|'md'|'lg'|'xl'; color?: 'primary'|'secondary'|'default'|'on-color'; label?: string }
export function Loader({size='sm',color='primary',label='Cargando'}:LoaderProps){
  const role={primary:'brand',secondary:'secondary',default:'primary','on-color':'on-brand'}[color];
  return <span role="status" className="inline-flex"><span className={cx('ds-loader',`ds-loader-${size}`)} aria-hidden="true" style={vars({'--loader-color':token(`color/icon/${role}`),'--loader-inner':`${loader.ring.arc.innerRadius*100}%`})}><span className="ds-loader-ring"/><span className="ds-loader-cap" style={{left:`${loader.cap.x/24*100}%`,top:`${loader.cap.y/24*100}%`,width:`${loader.cap.w/24*100}%`,height:`${loader.cap.h/24*100}%`}}/></span><span className="sr-only">{label}</span></span>;
}
/** Align conserva el lado de la flecha; no promete detección del borde de pantalla. */
export interface TooltipProps { content: string; children: ReactNode; align?: 'up'|'right'|'left'|'down'; open?: boolean; asChild?: boolean }
export function Tooltip({content,children,align='right',open,asChild=false}:TooltipProps){
  const id=useId();const [shown,setShown]=useState(false);const [dismissed,setDismissed]=useState(false);
  const visible=open??(shown&&!dismissed);
  return <span className="ds-tooltip-anchor" onMouseEnter={()=>{setShown(true);setDismissed(false);}} onMouseLeave={()=>setShown(false)} onFocus={()=>{setShown(true);setDismissed(false);}} onBlur={e=>{if(!e.currentTarget.contains(e.relatedTarget))setShown(false);}} onKeyDown={e=>{if(e.key==='Escape')setDismissed(true);}}>{asChild&&isValidElement(children)?cloneElement(children as ReactElement<HTMLAttributes<HTMLElement>>,{'aria-describedby':[(children as ReactElement<HTMLAttributes<HTMLElement>>).props['aria-describedby'],visible?id:undefined].filter(Boolean).join(' ')||undefined}):<span tabIndex={0} aria-describedby={visible?id:undefined}>{children}</span>}{visible&&<span id={id} role="tooltip" className={cx('ds-tooltip',`ds-tooltip-${align}`)}>{content}<svg width="16" height="10" viewBox="0 0 16 10" className="ds-tooltip-arrow" aria-hidden="true"><path d={arrow.path} fill={token('color/background/inverse')}/></svg></span>}</span>;
}
