"use client";

import { useEffect, useId, useRef, useState } from "react";
import { RotateCcw } from "lucide-react";
import { Math as Formula } from "@/components/Math";
import styles from "./CosmologyExperience.module.css";

/** The published leading R² relations; N remains the external reheating input. */
export function CosmologyExperience({ inverseAlpha }: { inverseAlpha: number }) {
  const [n, setN] = useState(55);
  const [view, setView] = useState<"inflation"|"scales">("inflation");
  const canvas = useRef<HTMLCanvasElement>(null);
  const control = useId();
  const ns = 1-2/n, r = 12/n**2;
  const c3 = 1/(8*Math.PI);
  const scalaron = c3**3.5;
  const logVacuum = Math.log10(3/(4*Math.PI**2))-2*inverseAlpha/Math.LN10;
  const logVacuumEnergy = logVacuum/4;

  useEffect(()=>{
    const surface=canvas.current;if(!surface)return;
    const ctx=surface.getContext("2d");if(!ctx)return;
    const draw=()=>{
      const bounds=surface.getBoundingClientRect();const w=bounds.width,h=bounds.height,dpr=Math.min(devicePixelRatio||1,2);
      surface.width=Math.round(w*dpr);surface.height=Math.round(h*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,w,h);
      const left=w<500?48:70,right=w-28,top=44,bottom=h-63;
      ctx.font="12px system-ui,sans-serif";ctx.lineWidth=1;ctx.textBaseline="middle";
      if(view==="inflation"){
        const x=(value:number)=>left+(value-.958)/.011*(right-left);
        const y=(value:number)=>bottom-(value-.0025)/.003*(bottom-top);
        ctx.strokeStyle="#425970";ctx.beginPath();ctx.moveTo(left,top);ctx.lineTo(left,bottom);ctx.lineTo(right,bottom);ctx.stroke();
        ctx.fillStyle="#b8cde3";ctx.textAlign="right";
        for(const v of [.003,.004,.005]){ctx.fillText(v.toFixed(3),left-9,y(v));ctx.strokeStyle="#294157";ctx.beginPath();ctx.moveTo(left,y(v));ctx.lineTo(right,y(v));ctx.stroke();}
        ctx.textAlign="center";for(const v of [.96,.963,.966])ctx.fillText(v.toFixed(3),x(v),bottom+22);
        ctx.fillText("Spectral tilt nₛ",(left+right)/2,h-14);ctx.textAlign="left";ctx.fillText("Tensor ratio r",left,19);
        ctx.lineWidth=3;ctx.strokeStyle="#82d6c3";ctx.beginPath();
        for(let i=0;i<=150;i++){const q=50+10*i/150;const xx=x(1-2/q),yy=y(12/q**2);if(i===0)ctx.moveTo(xx,yy);else ctx.lineTo(xx,yy);}ctx.stroke();
        const xx=x(ns),yy=y(r);ctx.lineWidth=1;ctx.setLineDash([3,5]);ctx.strokeStyle="#91abd0";ctx.beginPath();ctx.moveTo(left,yy);ctx.lineTo(xx,yy);ctx.lineTo(xx,bottom);ctx.stroke();ctx.setLineDash([]);
        ctx.fillStyle="#eff5ff";ctx.beginPath();ctx.arc(xx,yy,7,0,2*Math.PI);ctx.fill();ctx.strokeStyle="#a6bff8";ctx.beginPath();ctx.arc(xx,yy,13,0,2*Math.PI);ctx.stroke();
        ctx.textAlign=xx>w*.65?"right":"left";ctx.fillText(`N★ = ${n}`,xx+(xx>w*.65?-18:18),yy-17);
      }else{
        const x=(log:number)=>left+(-log/34)*(right-left);
        ctx.fillStyle="#b8cde3";ctx.textAlign="center";
        for(const v of [0,-10,-20,-30]){const xx=x(v);ctx.fillText(v===0?"1":`10${v===-10?"⁻¹⁰":v===-20?"⁻²⁰":"⁻³⁰"}`,xx,bottom+22);ctx.strokeStyle="#294157";ctx.beginPath();ctx.moveTo(xx,top+10);ctx.lineTo(xx,bottom);ctx.stroke();}
        const rows=[{name:"Reference M̄",log:0,color:"#b8cde3"},{name:"Scalaron mass",log:Math.log10(scalaron),color:"#82d6c3"},{name:"Vacuum energy scale",log:logVacuumEnergy,color:"#e7b58a"}];
        rows.forEach((row,i)=>{const yy=top+30+i*(bottom-top-55)/2;ctx.textAlign="left";ctx.fillStyle=row.color;ctx.fillText(row.name,left,yy-19);ctx.strokeStyle=row.color;ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(left,yy);ctx.lineTo(x(row.log),yy);ctx.stroke();ctx.beginPath();ctx.arc(x(row.log),yy,6,0,2*Math.PI);ctx.fill();});
        ctx.fillStyle="#b8cde3";ctx.textAlign="center";ctx.fillText("Energy divided by the reference scale M̄",(left+right)/2,h-14);
      }
    };
    const observer=new ResizeObserver(draw);observer.observe(surface);draw();return()=>observer.disconnect();
  },[n,ns,r,view,scalaron,logVacuumEnergy]);

  return <section className={styles.experience} aria-label="Cosmological relations experiment">
    <div className={styles.switch} role="group" aria-label="Choose a cosmological mechanism"><button type="button" aria-pressed={view==="inflation"} onClick={()=>setView("inflation")}>One inflation curve</button><button type="button" aria-pressed={view==="scales"} onClick={()=>setView("scales")}>Huge scale separations</button></div>
    <div className={styles.stage}>
      <div className={styles.stageTitle}><h2>{view==="inflation"?"One input moves two observables.":"Small inputs, exponentially separated scales."}</h2><p>{view==="inflation"?"Move along the leading R² branch. Each point has one tilt and one tensor ratio.":"The two branches reuse c₃ and alpha. The horizontal axis is logarithmic: equal distances mean equal powers of ten."}</p></div>
      <canvas ref={canvas} aria-label={view==="inflation"?`Calculated inflation curve at N star ${n}: tilt ${ns.toFixed(6)}, tensor ratio ${r.toFixed(6)}.`:"Dimensionless energy scale hierarchy: reference scale, scalaron mass and the fourth root of the vacuum energy density."}>The leading relations are nₛ = 1 − 2/N★ and r = 12/N★². The source branches also specify a scalaron mass and a vacuum energy density relative to the same reference scale.</canvas>
      {view==="inflation"?<div className={styles.controls}><label htmlFor={control}>External reheating input N★ <output htmlFor={control}>{n}</output></label><input id={control} type="range" min="50" max="60" step="1" value={n} onChange={e=>setN(Number(e.target.value))}/><div className={styles.outputs} aria-live="polite"><div><span>Spectral tilt nₛ</span><strong>{ns.toFixed(6)}</strong></div><div><span>Tensor ratio r</span><strong>{r.toFixed(6)}</strong></div><button type="button" onClick={()=>setN(55)}><RotateCcw size={16}/>Reset to 55</button></div><p>The frozen band uses N★ from 50 to 60. Reheating selects its physical location; the slider explores that external choice.</p></div>:<div className={styles.scales}><p>Each plotted quantity is an energy divided by M̄. The vacuum point uses the fourth root of its density, so the comparison has matching dimensions.</p><dl><div><dt>Scalaron mass / M̄</dt><dd>{scalaron.toExponential(6)}</dd></div><div><dt>log₁₀ of vacuum density / M̄⁴</dt><dd>{logVacuum.toFixed(6)}</dd></div></dl></div>}
    </div>
    <div className={styles.equations}>{view==="inflation"?<><Formula block plain="Spectral tilt is one minus two over N star; the tensor ratio is twelve over N star squared.">{String.raw`n_s=1-\frac{2}{N_\star},\qquad r=\frac{12}{N_\star^2}`}</Formula><Formula block plain="Eliminating N star puts both observables on the same curve: r equals three times one minus n s squared.">{String.raw`r=3(1-n_s)^2`}</Formula></>:<><Formula block plain="The stated scalaron branch gives mass over reference scale equal to the seventh half power of the boundary normalization.">{String.raw`\frac{M_{\rm scal}}{\bar M}=c_3^{7/2},\qquad c_3=\frac1{8\pi}`}</Formula><Formula block plain="The stated vacuum density branch is three over four pi squared times exp of minus two over alpha, relative to the fourth power of the reference scale.">{String.raw`\frac{\rho_\Lambda}{\bar M^4}=\frac3{4\pi^2}\exp\!\left(-\frac2\alpha\right)`}</Formula></>}</div>
  </section>;
}
