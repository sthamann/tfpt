"use client";
import { useEffect,useRef,type ReactNode } from "react";
export function HomeComparisonDetails({children}:{children:ReactNode}){
 const ref=useRef<HTMLDetailsElement>(null);
 useEffect(()=>{
  const matches=(hash:string)=>hash==="#prediction-accuracy"||hash.startsWith("#comparison-");
  const reveal=()=>{if(matches(window.location.hash)&&ref.current){ref.current.open=true;requestAnimationFrame(()=>document.getElementById(window.location.hash.slice(1))?.scrollIntoView({block:"start"}));}};
  const click=(event:MouseEvent)=>{const a=event.target instanceof Element?event.target.closest("a[href]"):null;if(a){const url=new URL(a.getAttribute("href")!,window.location.href);if(url.origin===window.location.origin&&url.pathname==="/"&&matches(url.hash)&&ref.current)ref.current.open=true;}};
  reveal();window.addEventListener("hashchange",reveal);document.addEventListener("click",click,true);return()=>{window.removeEventListener("hashchange",reveal);document.removeEventListener("click",click,true);};
 },[]);
 return <details ref={ref} className="experience-shell guide-details my-10 scroll-mt-24" id="prediction-accuracy"><summary>Inspect all ten dated comparisons, inflation bands and the full prediction register</summary>{children}</details>;
}
