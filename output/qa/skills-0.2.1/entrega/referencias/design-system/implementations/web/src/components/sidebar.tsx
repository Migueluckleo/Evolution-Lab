'use client';
import { useId, useState, type CSSProperties, type ReactNode } from 'react';
import { CaretDown, CaretLeft, CaretRight, HouseLine } from '@phosphor-icons/react';
import { cx, token, vars } from '../lib/utils';
import { IconButton } from './actions';
import { Tooltip } from './feedback';
import reference from '../generated/sidebar.json';
import { typographyClass, type TypographyId } from '../generated/typography';

export type MenuItemVariant =
  | { orientation?: 'vertical'; type?: 'expanded'|'collapsed'; status?: 'default'|'hover'|'focus' }
  | { orientation?: 'vertical'; type: 'sub-menu'; status?: 'default'|'hover' }
  | { orientation: 'horizontal'; type?: 'collapsed'; status?: 'default'|'hover'|'focus' };
export type MenuItemProps = MenuItemVariant & {
  label?: string; isActive?: boolean; showRightIcon?: boolean;
  fillIcon?: ReactNode; lightIcon?: ReactNode; href?: string; onClick?: () => void;
  className?: string;
};
export function MenuItem({orientation='vertical',type='collapsed',status,isActive=true,label='Home',showRightIcon=true,fillIcon=<HouseLine weight="fill"/>,lightIcon=<HouseLine weight="light"/>,href,onClick,className}:MenuItemProps) {
  const [hover,setHover]=useState(false), [focus,setFocus]=useState(false);
  const gradientId=useId();
  const state=status??(focus&&type!=='sub-menu'?'focus':hover?'hover':'default');
  const name=`orientation=${orientation}, type=${type}, status=${state}, isActive=${isActive}`;
  const recipe=reference.variants.find(v=>v.name===name);
  if(!recipe) throw new Error(`MenuItem: combinación no documentada: ${name}`);
  const collapsed=orientation==='vertical'&&type==='collapsed';
  const beta=orientation==='vertical'&&type==='expanded'&&state==='default'&&isActive;
  const emphasized=recipe.label?.weight==='SemiBold';
  const textStyle:TypographyId=type==='sub-menu'?(emphasized?'ui-navigation-emphasis-auto':'ui-navigation-label-auto'):(emphasized?'ui-sidebar-label-active':'ui-body-spacious');
  const styles:CSSProperties={width:recipe.width,height:recipe.height,gap:recipe.gap,padding:recipe.padding.map(n=>`${n}px`).join(' '),color:token(recipe.label?.color??recipe.icon!.color),...vars({'--icon':token(recipe.icon?.color??'color/icon/brand'),'--menu-line':recipe.line?token(recipe.line):'transparent','--menu-bg':recipe.background?token(recipe.background):'transparent'})};
  const props={className:cx('ds-menu-item',typographyClass(textStyle),`ds-menu-${orientation}`,`ds-menu-${type}`,state==='focus'&&'is-focus',className),style:styles,'data-state':state,'data-active':isActive,'data-variant':name,'aria-label':label,'aria-current':isActive?'page' as const:undefined,onMouseEnter:()=>setHover(true),onMouseLeave:()=>setHover(false),onFocus:(e:React.FocusEvent<HTMLElement>)=>setFocus(e.currentTarget.matches(':focus-visible')),onBlur:()=>setFocus(false),onClick};
  const content=<>
    {recipe.union&&<svg className="ds-menu-union" aria-hidden="true" width={recipe.union.width} height={recipe.union.height} viewBox={recipe.union.viewBox} style={{left:recipe.union.x,top:recipe.union.y}}>{recipe.union.paths.map((d,i)=><path key={i} d={d} fill={token(recipe.union!.color)}/>)}</svg>}
    {type==='sub-menu'?<span className="ds-menu-submenu-background"/>:<span className="ds-icon">{recipe.icon?.name.endsWith('Fill')?fillIcon:lightIcon}</span>}
    <span hidden={collapsed} className="ds-menu-label">{label}</span>
    {beta&&<span className="ds-menu-release"><svg aria-hidden="true" viewBox="0 0 1 1" preserveAspectRatio="none"><defs><linearGradient id={gradientId} x1="0" y1="0.5" x2="1" y2="0.5" gradientTransform={reference.releaseGradient}><stop stopColor={token('color/background/sidebar-release-end')}/><stop offset="1" stopColor={token('color/background/sidebar-release-start')}/></linearGradient></defs><rect width="1" height="1" fill={`url(#${gradientId})`}/></svg><span>BETA</span></span>}
    {!collapsed&&type!=='sub-menu'&&<span hidden={!showRightIcon} className="ds-menu-caret"><CaretDown weight="light" size="100%" aria-hidden="true"/></span>}
  </>;
  const control=href?<a {...props} href={href}>{content}</a>:<button {...props} type="button">{content}</button>;
  return collapsed?<Tooltip content={label} align="left" asChild open={state==='hover'?true:undefined}>{control}</Tooltip>:control;
}

export interface SidebarItem { id:string; label:string; icon?:ReactNode; fillIcon?:ReactNode; lightIcon?:ReactNode; href?:string; active?:boolean; onClick?:()=>void; submenu?:boolean; showRightIcon?:boolean }
export interface SidebarProps { expanded?:boolean; onExpandedChange?:(expanded:boolean)=>void; items?:readonly SidebarItem[]; children?:ReactNode; lowerOptions?:ReactNode; label?:string; height?:CSSProperties['height']; className?:string }
export function Sidebar({expanded=false,onExpandedChange,items=[],children,lowerOptions,label='Navegación principal',height=885,className}:SidebarProps) {
  return <nav aria-label={label} style={{height}} className={cx('ds-sidebar',expanded&&'ds-sidebar-expanded',className)}>
    <div className="ds-sidebar-toggle"><IconButton showCount={false} label={expanded?'Contraer navegación':'Expandir navegación'} icon={expanded?<CaretLeft weight="light"/>:<CaretRight weight="light"/>} size="small" onClick={()=>onExpandedChange?.(!expanded)} aria-expanded={expanded}/></div>
    <div className="ds-sidebar-items">{items.map(item=><div key={item.id} hidden={item.submenu&&!expanded}><MenuItem {...(expanded&&item.submenu?{type:'sub-menu' as const}:{type:expanded?'expanded' as const:'collapsed' as const})} label={item.label} isActive={item.active??false} lightIcon={item.lightIcon??item.icon} fillIcon={item.fillIcon??item.icon} href={item.href} onClick={item.onClick} showRightIcon={item.showRightIcon}/></div>)}{children}</div>
    <div className="ds-sidebar-lower">{lowerOptions}</div>
  </nav>;
}
export interface TopBarProps { items?:readonly Omit<SidebarItem,'submenu'>[]; children?:ReactNode; label?:string; width?:CSSProperties['width']; className?:string }
export function TopBar({items=[],children,label='Navegación superior',width=1399,className}:TopBarProps) {
  return <nav aria-label={label} className={cx('ds-top-bar',className)} style={{width}}>{items.map(item=><MenuItem key={item.id} orientation="horizontal" label={item.label} isActive={item.active??false} lightIcon={item.lightIcon??item.icon} fillIcon={item.fillIcon??item.icon} href={item.href} onClick={item.onClick} showRightIcon={item.showRightIcon}/>)}{children}</nav>;
}
