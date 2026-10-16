// Fixture SSR aislado: usa el mismo renderer React que el catálogo.
import { renderToStaticMarkup } from 'react-dom/server';
import { Characters } from '../src/components/content';
process.stdout.write(renderToStaticMarkup(<div style={{display:'grid',gap:16}}>{(['beni','navi'] as const).map(character=><div key={character} style={{display:'flex',gap:16}}>{Array.from({length:character==='beni'?6:7},(_,i)=><Characters key={i} character={character} frame={(i+1) as 1|2|3|4|5|6|7}/>)}</div>)}</div>));
