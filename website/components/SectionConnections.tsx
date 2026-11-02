"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { siteSections } from "@/lib/site-sections";
export function SectionConnections(){
 const pathname=usePathname();const page=siteSections.find(s=>s.href===pathname);
 if(!page)return null;
 return <nav className="section-connections" aria-label="Continue through the research"><h2>Where to go from here</h2><div>{page.next.map(href=>{const next=siteSections.find(s=>s.href===href);return next&&<Link key={href} href={href}><strong>{next.title}</strong><span>{next.purpose}</span></Link>})}</div></nav>;
}
