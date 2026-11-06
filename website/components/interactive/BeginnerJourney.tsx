"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Pause, Play, RotateCcw } from "lucide-react";
import { BeginnerExperiments } from "./BeginnerExperiments";
import styles from "./BeginnerJourney.module.css";

type Comparison={predicted:number;central:string;uncertaintyMinus:string;date:string;measured:string};
const connections=[
  ["Four chosen marks", "One shared geometry", "The starting geometry is supplied by the construction."],
  ["The same four marks", "3 routes and 5 functions", "Two different mathematical spaces come from this same setup."],
  ["The five internal slots", "16 even choices", "The rule keeps patterns with zero, two or four occupied slots."],
  ["The carrier and family patterns", "240 vectors in E₈", "A specified matching rule joins the two lattices."],
  ["Boundary normalization and the count 48", "One small shared input", "These supplied ingredients fix the starting number. E₈ alone does not fix it."],
  ["Shared boundary ingredients", "The alpha balance", "The equation also uses the stated matter count 41 and response rule."],
  ["The three family directions", "A changing distribution", "A specified transfer rule moves the weights while keeping their total."],
  ["The calculated alpha number", "A comparison with measurement", "The observation is separate data, with its own date and uncertainty."],
] as const;
const steps=[
  {id:"marks",name:"A shared starting point",title:"Start with four marked spots.",body:"Imagine a sphere with four marked points. TFPT uses this geometric setup to organize two parts of its construction. The marks are mathematical ingredients, rather than four objects floating in space.",next:"See what the same four marks give"},
  {id:"counts",name:"Two building blocks",title:"One setup gives two different building blocks.",body:"The four marks give three independent routes around the missing points. The same setup also supplies five basic functions. These become the three family directions and five internal slots in the stated reading.",next:"Try the five slots"},
  {id:"standard-model",name:"Patterns of matter",title:"Five switches can organize sixteen components.",body:"A slot is a place in an internal pattern. Choose an even number of the five slots and their contributions add. You can now see where the different matter components fit.",next:"Join the two patterns"},
  {id:"e8",name:"The bigger pattern",title:"Join the pieces into one pattern.",body:"The carrier and family give two smaller point patterns. Four matching groups complete the larger pattern called E₈. Watch the groups come together, then inspect the result.",next:"Follow one shared number"},
  {id:"flavor",name:"Linked answers",title:"One shared input connects several answers.",body:"A small number is reused in several formulas. Change that one input and several outputs move together. The marked reference is the fixed value used by TFPT.",next:"Find a balance"},
  {id:"alpha",name:"A balance point",title:"One of the answers has to balance itself.",body:"The alpha equation compares two sides that both depend on the same trial value. At the balance point the sides agree. The balanced trial number is inverse alpha, near 137.",next:"Watch a change unfold"},
  {id:"dynamics",name:"Change over steps",title:"Some differences fade while a total stays fixed.",body:"The specified rule moves weight between three components. Repeat the rule and the distribution settles. The animation makes each mathematical step visible.",next:"Put an answer to the test"},
  {id:"predictions",name:"Check against data",title:"A calculated answer still needs a test.",body:"Follow a formula to its registered number, then compare the same quantity with a dated measurement. The calculation, the measurement and the physical interpretation each have their own role.",next:"Start again"},
] as const;

function FoundationPicture({part}:{part:"marks"|"counts"}){
  const ref=useRef<HTMLCanvasElement>(null);
  const [progress,setProgress]=useState(0),[playing,setPlaying]=useState(false),[reduced,setReduced]=useState(true);
  const stamp=useRef(0);
  useEffect(()=>{const media=matchMedia("(prefers-reduced-motion: reduce)");const sync=()=>{setReduced(media.matches);if(media.matches)setPlaying(false);};sync();media.addEventListener("change",sync);return()=>media.removeEventListener("change",sync);},[]);
  useEffect(()=>{if(!playing||reduced)return;let frame=0;stamp.current=0;const tick=(time:number)=>{if(!stamp.current)stamp.current=time;const t=Math.min(1,(time-stamp.current)/2200);setProgress(t);if(t<1)frame=requestAnimationFrame(tick);else setPlaying(false);};frame=requestAnimationFrame(tick);return()=>cancelAnimationFrame(frame);},[playing,reduced]);
  useEffect(()=>{
    const canvas=ref.current;if(!canvas)return;const ctx=canvas.getContext("2d");if(!ctx)return;
    const draw=()=>{
      const {width:w,height:h}=canvas.getBoundingClientRect();const dpr=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,w,h);
      const mobile=w<600;const cx=part==="marks"?w/2:mobile?w/2:w*.22,cy=part==="marks"?h*.46:mobile?h*.24:h*.5;const radius=part==="marks"?Math.min(w*.28,h*.32):Math.min(w*.17,mobile?57:95);
      ctx.strokeStyle="#7f9fbd";ctx.lineWidth=1.2;ctx.beginPath();ctx.arc(cx,cy,radius,0,Math.PI*2);ctx.stroke();ctx.beginPath();ctx.ellipse(cx,cy,radius,radius*.31,0,0,Math.PI*2);ctx.strokeStyle="#3f5a73";ctx.stroke();ctx.beginPath();ctx.ellipse(cx,cy,radius*.34,radius,0,0,Math.PI*2);ctx.stroke();
      const colours=["#9dbfff","#7cdac5","#e5b18c","#c4b4f0"];
      const markPoints=colours.map((colour,i)=>{const angle=-Math.PI/2+i*Math.PI/2;const x=cx+Math.cos(angle)*radius*.79,y=cy+Math.sin(angle)*radius*.79;const highlight=part==="marks"?progress>i/4:progress>.05;ctx.beginPath();ctx.fillStyle=highlight?colour:"#63819c";ctx.arc(x,y,highlight?8:5,0,Math.PI*2);ctx.fill();if(highlight){ctx.beginPath();ctx.strokeStyle=colour;ctx.arc(x,y,13,0,Math.PI*2);ctx.stroke();}ctx.font="13px system-ui,sans-serif";ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillStyle=highlight?colour:"#a2bad2";ctx.fillText(String.fromCharCode(65+i),x+Math.cos(angle)*23,y+Math.sin(angle)*23);ctx.textBaseline="alphabetic";return{x,y};});
      ctx.textAlign="center";ctx.fillStyle="#e5eef9";ctx.font="15px system-ui,sans-serif";
      if(part==="marks"){
        ctx.fillText("One sphere. Four marked points.",cx,cy+radius+35);
        if(progress>=1){ctx.fillStyle="#a9c2db";ctx.font="13px system-ui,sans-serif";ctx.fillText("Keep the same four marks in the next picture.",cx,cy+radius+61);}
      }else{
        const groupX=mobile?w/2:w*.72;const upperY=mobile?h*.57:h*.28,lowerY=mobile?h*.86:h*.75;
        const eased=1-(1-progress)**3;
        const routes=Array.from({length:4},(_,i)=>({x:groupX+(i-1.5)*(mobile?43:48),y:upperY}));
        routes.forEach((point,i)=>{
          const start=markPoints[i];const x=start.x+(point.x-start.x)*eased,y=start.y+(point.y-start.y)*eased;
          ctx.globalAlpha=.35+.65*eased;ctx.strokeStyle=colours[i];ctx.lineWidth=i===3?1.2:2;
          if(i===3&&progress>.65)ctx.setLineDash([3,4]);
          ctx.beginPath();ctx.arc(x,y,10,-.4,Math.PI*1.75);ctx.stroke();ctx.setLineDash([]);
        });
        const funcs=Array.from({length:5},(_,i)=>({x:groupX+(i-2)*(mobile?39:48),y:lowerY}));
        funcs.forEach((point,i)=>{
          const start=i===0?point:markPoints[i-1];const x=start.x+(point.x-start.x)*eased,y=start.y+(point.y-start.y)*eased;
          ctx.globalAlpha=.3+.7*eased;ctx.beginPath();ctx.fillStyle=i===0?"#e5eef9":colours[i-1];ctx.arc(x,y,9,0,Math.PI*2);ctx.fill();
          if(progress>.55){ctx.fillStyle="#102439";ctx.font="600 12px system-ui,sans-serif";ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(i===0?"1":String.fromCharCode(64+i),x,y);ctx.textBaseline="alphabetic";}
        });ctx.globalAlpha=1;
        if(progress>.1){
          ctx.fillStyle="#e5eef9";ctx.font="600 16px system-ui,sans-serif";ctx.textAlign="center";
          ctx.fillText("4 loops, linked by 1 rule",groupX,upperY-33);
          ctx.fillText("5 basic functions",groupX,lowerY-33);
          ctx.font="13px system-ui,sans-serif";ctx.fillStyle="#a9c2db";
          ctx.fillText(progress>.65?"The fourth follows from the other three.":"A loop goes around each missing point.",groupX,upperY+31);
          ctx.fillText("One constant + one for each of the 4 marks",groupX,lowerY+31);
          if(progress>.65){ctx.font="600 14px system-ui,sans-serif";ctx.fillStyle="#7cdac5";ctx.fillText("3 independent routes",groupX,upperY+53);}
        }
        ctx.font="13px system-ui,sans-serif";ctx.fillStyle="#a9c2db";ctx.textAlign="center";ctx.fillText("The same four marks",cx,cy+radius+23);
      }
    };
    const observer=new ResizeObserver(draw);observer.observe(canvas);draw();return()=>observer.disconnect();
  },[part,progress]);
  const show=()=>{if(reduced){setProgress(1);return;}setProgress(0);setPlaying(true);};
  return <div className={styles.foundation}>
    <canvas ref={ref} className={part==="counts"?styles.countCanvas:styles.markCanvas} role="img" aria-label={part==="marks"?"A schematic sphere with four marked points. Highlighting does not change the chosen geometry.":"The same four point setup supplies a rank three cycle space and a five dimensional space of basic functions under the stated assumptions."}>Four marked points on a sphere give three independent puncture loops and five basic meromorphic functions in the stated construction.</canvas>
    <div className={styles.foundationControls}><button type="button" onClick={show} disabled={playing}>{part==="marks"?"Highlight the four spots":"Show the two results"}<Play size={16}/></button>{playing&&<button type="button" onClick={()=>setPlaying(false)}><Pause size={16}/>Pause</button>}<button type="button" onClick={()=>{setPlaying(false);setProgress(0);}}><RotateCcw size={16}/>Reset picture</button></div>
    <p className={styles.foundationNote}>{part==="marks"?"The sphere is a schematic drawing. The marks stay the same throughout this construction.":"The moving dots explain how the same input is reused. The two outputs are different mathematical spaces."}</p>
  </div>;
}

export function BeginnerJourney({inverseAlpha,comparison}:{inverseAlpha:number;comparison:Comparison}){
  const [step,setStep]=useState(0);const current=steps[step];
  return <section className={styles.journey} aria-label="Build the theory one visual step at a time">
    <div className={styles.progress}><p>Step {step+1} of {steps.length}</p><div className={styles.arrows}><button type="button" disabled={step===0} onClick={()=>setStep(s=>s-1)} aria-label="Previous explanation"><ArrowLeft size={18}/></button><button type="button" onClick={()=>setStep(s=>s===steps.length-1?0:s+1)}>{step===steps.length-1?"Start again":"Next step"}<ArrowRight size={18}/></button></div></div>
    <div className={styles.intro} aria-live="polite"><h2>{current.title}</h2><p>{current.body}</p></div>
    <div className={styles.connection} aria-label="What this step uses and shows"><div><span>{connections[step][0]}</span><ArrowRight size={21} aria-hidden/><strong>{connections[step][1]}</strong></div><p>{connections[step][2]}</p></div>
    <div key={current.id} className={styles.visual}>{current.id==="marks"||current.id==="counts"?<FoundationPicture part={current.id}/>:<BeginnerExperiments embedded chapter={current.id} inverseAlpha={inverseAlpha} comparison={comparison}/>}</div>
    <div className={styles.continue}><span>{step<steps.length-1?current.next:"You have followed the main route. Explore a chapter below for more."}</span><button type="button" onClick={()=>setStep(s=>s===steps.length-1?0:s+1)}>{step===steps.length-1?<><RotateCcw size={16}/>Start again</>:<>Continue<ArrowRight size={18}/></>}</button></div>
    <details className={styles.choose}><summary>Choose a step</summary><ol>{steps.map((s,i)=><li key={s.id}><button type="button" aria-current={i===step?"step":undefined} onClick={()=>setStep(i)}>{i+1}. {s.name}</button></li>)}</ol></details>
    <details className={styles.precise}><summary>Why start with these ingredients?</summary><p>The geometric counts use the stated sphere and four point divisor. Four marks follow in the flat sphere class with order two branch points; the square arrangement adds the order four input. The physical boundary source includes its kernel, state and time. These source and field assumptions remain attached to the interpretation.</p><Link href="/explain#inputs">Read the starting structure and its assumptions<ArrowRight size={15}/></Link></details>
  </section>;
}
