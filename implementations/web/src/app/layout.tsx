import type { Metadata } from 'next';
import '../styles.css';
import './catalog.css';
export const metadata:Metadata={title:'CONTPAQi · Componentes web',description:'Biblioteca React para diseñar pantallas con datos locales.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="es"><body>{children}</body></html>;}
