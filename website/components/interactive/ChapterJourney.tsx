"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Maximize2, Minimize2, Pause, Play, RotateCcw } from "lucide-react";
import { Math as Formula } from "@/components/Math";
import { calculationJourneys } from "./calculation-journeys";
import { drawCalculationStep } from "./calculation-journey-draw";
import { STRUCTURE_JOURNEYS, drawStructureStep } from "./structure-journeys";
import { clampJourney as clamp, easeJourney as ease, journeyColors as colors } from "./chapter-journey-types";
import type { DrawKit, JourneyComparison, JourneySpec } from "./chapter-journey-types";
import styles from "./ChapterJourney.module.css";

type Point={x:number;y:number};
const lerp=(a:number,b:number,p:number)=>a+(b-a)*p;
const positionAt=(index:number,mobile:boolean):Point=>mobile?{x:175,y:110+index*245}:{x:150+(Math.floor(index/4)%2?3-index%4:index%4)*300,y:135+Math.floor(index/4)*270};
const sources=(spec:JourneySpec,index:number)=>spec.steps[index].from??(index?[index-1]:[]);
function readingFormula(value:string){if(value.includes("\\begin{"))return value;const rows=value.split(/\\(?:qquad|quad)\b/).map(row=>row.trim()).filter(Boolean);return rows.length>1?String.raw`\begin{gathered}`+rows.join(String.raw`\\[.4em]`)+String.raw`\end{gathered}`:value;}
function draw(canvas:HTMLCanvasElement,spec:JourneySpec,chapter:string,progressPosition:number,selected:number,expanded:boolean,comparison:JourneyComparison,freezeDate:string){
  const ctx=canvas.getContext("2d");if(!ctx)return;const {width,height}=canvas.getBoundingClientRect();if(!width||!height)return;
  const mobile=width<900,worldWidth=mobile?350:1200,worldHeight=mobile?spec.steps.length*245:Math.ceil(spec.steps.length/4)*270+20;
  const scale=mobile&&!expanded?Math.min(width/worldWidth,1.1):width/worldWidth,dpr=Math.min(devicePixelRatio||1,2),position=expanded?spec.steps.length-1:progressPosition;
  canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,width,height);
  const viewHeight=height/scale,lower=Math.floor(position),cameraFor=(i:number)=>Math.max(-80,Math.min(worldHeight-viewHeight,positionAt(i,true).y-viewHeight*.68));
  const camera=mobile&&!expanded?lerp(cameraFor(lower),cameraFor(Math.min(spec.steps.length-1,lower+1)),position-lower):0;
  ctx.translate(mobile?(width-worldWidth*scale)/2:0,mobile?-camera*scale:Math.max(0,(height-worldHeight*scale)/2));ctx.scale(scale,scale);
  const text:DrawKit["text"]=(value,x,y,size=15,color="#d4e4f5",weight=400)=>{ctx.font=`${weight} ${size}px system-ui,sans-serif`;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillStyle=color;ctx.fillText(value,x,y);};
  const dot:DrawKit["dot"]=(x,y,r,color,stroke)=>{ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fillStyle=color;ctx.fill();if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=1;ctx.stroke();}};
  const line:DrawKit["line"]=(x1,y1,x2,y2,color="#8caac7",dashed=false)=>{ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.strokeStyle=color;ctx.lineWidth=1.3;ctx.setLineDash(dashed?[3,5]:[]);ctx.stroke();ctx.setLineDash([]);};
  const bar:DrawKit["bar"]=(x,y,w,h,fraction,color=colors[0])=>{ctx.fillStyle="#28435d";ctx.fillRect(x,y,w,h);ctx.fillStyle=color;ctx.fillRect(x,y,w*clamp(fraction),h);};
  spec.steps.forEach((stage,index)=>{if(!index)return;sources(spec,index).forEach((source,j)=>{
    const a=positionAt(source,mobile),b=positionAt(index,mobile),p=clamp(position-index+1),skip=index-source>1;
    let start:Point,end:Point,c1:Point,c2:Point;
    if(mobile&&skip){const lane=j%2?326:24;start={x:a.x+(lane<175?-112:112),y:a.y};end={x:b.x+(lane<175?-112:112),y:b.y};c1={x:lane,y:a.y};c2={x:lane,y:b.y};}
    else if(!mobile&&skip){const sameRow=Math.floor(source/4)===Math.floor(index/4),lane=sameRow?a.y-113:Math.min(a.y,b.y)+135;start={x:a.x,y:a.y+(sameRow?-80:105)};end={x:b.x,y:b.y-80};c1={x:a.x,y:lane};c2={x:b.x,y:lane};}
    else{const dx=b.x-a.x,dy=b.y-a.y,len=Math.hypot(dx,dy),cut=mobile?100:116;start={x:a.x+dx/len*cut,y:a.y+dy/len*cut};end={x:b.x-dx/len*cut,y:b.y-dy/len*cut};c1={x:lerp(start.x,end.x,.4),y:start.y};c2={x:lerp(start.x,end.x,.6),y:end.y};}
    const at=(t:number)=>({x:(1-t)**3*start.x+3*(1-t)**2*t*c1.x+3*(1-t)*t*t*c2.x+t**3*end.x,y:(1-t)**3*start.y+3*(1-t)**2*t*c1.y+3*(1-t)*t*t*c2.y+t**3*end.y});
    ctx.beginPath();ctx.moveTo(start.x,start.y);for(let n=1;n<=36;n++){const q=at((p||1)*n/36);ctx.lineTo(q.x,q.y);}ctx.lineWidth=index===selected?2:1.3;ctx.strokeStyle=p?colors[source%4]:"#304a64";ctx.globalAlpha=p?(index===selected?.95:.47):.6;ctx.setLineDash(p?[]:[3,7]);ctx.stroke();ctx.setLineDash([]);ctx.globalAlpha=1;
    if(p>0){const q=at(p),prior=at(Math.max(0,p-.04)),angle=Math.atan2(q.y-prior.y,q.x-prior.x);ctx.beginPath();ctx.moveTo(q.x,q.y);ctx.lineTo(q.x-7*Math.cos(angle-.45),q.y-7*Math.sin(angle-.45));ctx.moveTo(q.x,q.y);ctx.lineTo(q.x-7*Math.cos(angle+.45),q.y-7*Math.sin(angle+.45));ctx.strokeStyle=colors[source%4];ctx.lineWidth=1.7;ctx.stroke();if(p<1)dot(q.x,q.y,3,colors[source%4]);}
  });});
  spec.steps.forEach((stage,index)=>{
    const node=positionAt(index,mobile),p=index?clamp(position-index+1):1,color=colors[index%4];ctx.save();ctx.translate(node.x,node.y);
    if(!p){text(`${index+1}. ${stage.short}`,0,0,15,"#809bb5");ctx.restore();return;}
    ctx.globalAlpha=.45+.55*p;
    if(index===selected){ctx.beginPath();ctx.roundRect(-111,-80,222,187,10);ctx.strokeStyle=color;ctx.lineWidth=1;ctx.stroke();}
    if(stage.additional)text("+ supplied input",0,-96,12,colors[2]);
    const kit:DrawKit={ctx,progress:p,active:index===selected,color,text,dot,line,bar};
    if(chapter==="standard-model"||chapter==="e8")drawStructureStep(chapter,index,kit);else drawCalculationStep(chapter,index,kit,comparison,freezeDate);
    text(`${index+1}. ${stage.short}`,0,85,15,color,600);ctx.restore();
  });
}

export function ChapterJourney({chapter,comparison,freezeDate}:{chapter:string;comparison:JourneyComparison;freezeDate:string}){
  const spec=useMemo(()=>STRUCTURE_JOURNEYS[chapter]??calculationJourneys(comparison,freezeDate)[chapter],[chapter,comparison,freezeDate]);
  const [step,setStep]=useState(0),[position,setPosition]=useState(0),[playing,setPlaying]=useState(false),[paused,setPaused]=useState(false),[reduced,setReduced]=useState(true),[expanded,setExpanded]=useState(false),[width,setWidth]=useState(0);
  const canvas=useRef<HTMLCanvasElement>(null),section=useRef<HTMLElement>(null),positionRef=useRef(0);
  const last=spec.steps.length-1,current=spec.steps[step],moving=Math.abs(position-step)>.0001;
  useEffect(()=>{const media=matchMedia("(prefers-reduced-motion: reduce)");const sync=()=>{setReduced(media.matches);if(media.matches){setPlaying(false);setPaused(false);}};sync();media.addEventListener("change",sync);return()=>media.removeEventListener("change",sync);},[]);
  useEffect(()=>{if(paused)return;if(reduced){positionRef.current=step;setPosition(step);return;}const from=positionRef.current;if(Math.abs(from-step)<.0001)return;let frame=0;const start=performance.now();const tick=(time:number)=>{const p=clamp((time-start)/1550),next=lerp(from,step,ease(p));positionRef.current=next;setPosition(next);if(p<1)frame=requestAnimationFrame(tick);};frame=requestAnimationFrame(tick);return()=>cancelAnimationFrame(frame);},[step,reduced,paused]);
  useEffect(()=>{if(!playing||paused||moving||reduced)return;if(step===last){setPlaying(false);return;}const timer=setTimeout(()=>setStep(s=>s+1),9000);return()=>clearTimeout(timer);},[playing,paused,moving,reduced,step,last]);
  useEffect(()=>{const stop=()=>{setPlaying(false);setPaused(true);};const hidden=()=>{if(document.hidden)stop();};document.addEventListener("visibilitychange",hidden);const observer=new IntersectionObserver(([entry])=>{if(!entry.isIntersecting)stop();},{threshold:0});if(section.current)observer.observe(section.current);return()=>{document.removeEventListener("visibilitychange",hidden);observer.disconnect();};},[]);
  useEffect(()=>{if(!canvas.current)return;const observer=new ResizeObserver(()=>setWidth(canvas.current?.getBoundingClientRect().width??0));observer.observe(canvas.current);return()=>observer.disconnect();},[]);
  useEffect(()=>{if(canvas.current)draw(canvas.current,spec,chapter,position,step,expanded,comparison,freezeDate);},[spec,chapter,position,step,expanded,width,comparison,freezeDate]);
  const go=(next:number)=>{setPlaying(false);setPaused(false);setExpanded(false);setStep(next);};
  const start=()=>{setPaused(false);setExpanded(false);if(step===last&&!moving){positionRef.current=0;setPosition(0);setStep(0);}setPlaying(true);};
  return <section ref={section} className={styles.journey} aria-label={`${spec.name}: connected derivation journey`}>
    <div className={styles.transport}><div className={styles.playback}>{playing||(!paused&&moving)?<button type="button" onClick={()=>{setPlaying(false);setPaused(true);}}><Pause size={17}/>Pause journey</button>:<button type="button" onClick={start} disabled={reduced}>{step===last&&!moving?<RotateCcw size={17}/>:<Play size={17}/>} {step===last&&!moving?"Replay journey":paused?"Resume journey":"Play journey"}</button>}<span>Step {step+1} of {spec.steps.length}</span></div><div className={styles.arrows}><button type="button" aria-label="Previous step" disabled={!step} onClick={()=>go(step-1)}><ArrowLeft size={18}/></button><button type="button" disabled={step===last} onClick={()=>go(step+1)}>Next step<ArrowRight size={18}/></button></div></div>
    <div className={styles.story} aria-live={playing?"off":"polite"}><h2>{current.title}</h2><p>{current.body}</p></div>
    <figure className={styles.figure}><canvas ref={canvas} className={`${styles.canvas}${expanded?` ${styles.expanded}`:""}`} style={expanded?{aspectRatio:width<900?`350 / ${spec.steps.length*245}`:`1200 / ${Math.ceil(spec.steps.length/4)*270+20}`} : undefined} role="img" aria-label={expanded?`${spec.name}: complete derivation path. ${spec.steps.map((s,i)=>`${i+1}. ${s.short}: ${s.output}`).join(". ")}`:`${spec.name}, step ${step+1}. Input: ${current.input}. Operation: ${current.operation}. Result: ${current.output}.`}>{spec.steps.map((stage,index)=>`${index+1}. ${stage.input}. ${stage.operation}. ${stage.output}.`).join(" ")}</canvas><button className={styles.mapSize} type="button" aria-pressed={expanded} onClick={()=>{setExpanded(v=>!v);setPlaying(false);setPaused(true);}}>{expanded?<Minimize2 size={15}/>:<Maximize2 size={15}/>} {expanded?"Follow the journey":"See the full derivation"}</button><figcaption>Arrows carry the named inputs into later calculations. Added inputs stay marked. {reduced?"Reduced motion is on. Use Next step or choose a stage below.":"Pause to inspect any operation, or choose a stage below."}</figcaption></figure>
    <ol className={styles.route} aria-label="Choose a derivation step">{spec.steps.map((stage,index)=><li key={stage.short} data-reached={position>=index}><button type="button" aria-current={index===step?"step":undefined} onClick={()=>go(index)}><span>{index+1}</span>{stage.short}</button></li>)}</ol>
    <div className={styles.working}><dl><div><dt>Carry forward</dt><dd>{current.input}</dd></div>{current.additional&&<div className={styles.added}><dt>Added at this step</dt><dd>{current.additional}</dd></div>}<div><dt>Operation</dt><dd>{current.operation}</dd></div><div className={styles.result}><dt>Result</dt><dd>{current.output}</dd></div></dl><div className={styles.formula}><Formula block plain={current.operation}>{readingFormula(current.formula)}</Formula></div><details><summary>Why this step works and what it assumes</summary><p>{current.detail}</p><Link href={current.href}>Read the original calculation<ArrowRight size={16}/></Link></details></div>
    <Link className={styles.return} href="/interactive"><ArrowLeft size={16}/>See where this fits in the whole theory</Link>
  </section>;
}
