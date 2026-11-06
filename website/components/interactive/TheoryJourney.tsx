"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Pause, Play, RotateCcw } from "lucide-react";
import styles from "./InteractiveWorld.module.css";

const stages = [
  { title: "Start with a boundary and five slots.", short: "The starting point", body: "A boundary tells the construction how a change at its edge is answered. Five internal slots organize the possible matter states: three colour slots and two weak slots. Start with both inputs, then follow what their rules produce.", detail: "Think of a construction kit: both its pieces and the rules for joining them matter. The specified boundary source contains its kernel, state and time, with normalization c₃ = 1/(8π). The carrier slots are internal representation data, rather than five locations in physical space.", active: [0, 1], href: "/explain#inputs", link: "Inspect the starting structure" },
  { title: "One geometry, two ways to read it.", short: "Families and carrier", body: "Four marked points on a sphere leave three independent loops. The same four marks also allow five independent functions. These give the three family directions and five carrier slots in the stated geometric reading.", detail: "Four marks follow in the stated class: a sphere, flat away from its branch points, with each branch point of order two. The square arrangement uses the additional order four input. Three comes from four loops with one relation; five comes from a constant and four simple poles. Colour slots and family directions remain different spaces.", active: [0, 1, 2, 3], href: "/three-fermion-generations", link: "Explore the shared four marks" },
  { title: "The two lattices fit together.", short: "The E₈ closure", body: "A lattice is a regular pattern of points. The carrier and family give two such patterns, called D₅ and A₃. Four matching classes let them join into E₈: one eight dimensional lattice with 240 shortest nonzero vectors, called roots.", detail: "The join is checked by the actual lattice norms and determinant. E₈ is the closure structure here; it is not labelled as the unbroken physical gauge group.", active: [1, 2, 3, 4], href: "/interactive/e8", link: "Build the 240 roots" },
  { title: "Follow the same structure into different readouts.", short: "Charges and readouts", body: "Select carrier slots and their charges add. The boundary and carrier data also supply a small shared number, called the seed. It enters the alpha equation, particle mixing and cosmic readouts, making these outputs connected.", detail: "Different branches use different mathematical maps. A shared input does not make their experimental comparisons independent, or give every branch the same physical status.", active: [0, 1, 4, 5, 6, 7], href: "/interactive/alpha", link: "Find the alpha fixed point" },
  { title: "Let the clocks and modes act.", short: "Dynamics and clocks", body: "A named conversion rule reads lattice vectors as finite quantum states. Fivefold and sixfold cycles return together after 30 steps. The transfer has one stationary mode and two decaying modes. These are distinct operations.", detail: "You can step the actual finite rules in the dynamics chapter. These are dimensionless operations; converting a step into physical time needs the corresponding physical map.", active: [4, 5, 8, 10], href: "/interactive/dynamics", link: "Run the dynamics" },
  { title: "Close the loop by checking what follows.", short: "Test the connections", body: "Compare exact lattice results, calculated values and physical identifications with their own evidence. Consistency can check a proposed starting structure. It does not let a consequence prove its own assumptions.", detail: "The goal is one common physical source for the connected construction. The atlas preserves both the results already obtained and the specific source connections still being worked out.", active: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], href: "/interactive/predictions", link: "Explore the registered readouts" },
] as const;

const nodes = [
  { label: "Boundary", subtitle: "oriented source", x: .12, y: .23, color: "#89b5ff", stage: 0 },
  { label: "Carrier", subtitle: "five marked slots", x: .12, y: .70, color: "#75d5c5", stage: 0 },
  { label: "Four marks", subtitle: "one shared geometry", x: .32, y: .19, color: "#c3b5f4", stage: 1 },
  { label: "Families", subtitle: "three cycle directions", x: .33, y: .70, color: "#75d5c5", stage: 1 },
  { label: "E₈", subtitle: "the lattice closes", x: .52, y: .43, color: "#d7e6ff", stage: 2 },
  { label: "Charges", subtitle: "the marked 3 + 2", x: .72, y: .17, color: "#75d5c5", stage: 3 },
  { label: "Alpha", subtitle: "a response fixed point", x: .73, y: .43, color: "#89b5ff", stage: 3 },
  { label: "Readouts", subtitle: "mixing, masses, cosmos", x: .73, y: .72, color: "#e5b58c", stage: 3 },
  { label: "Dynamics", subtitle: "clocks and transfer", x: .50, y: .85, color: "#c3b5f4", stage: 4 },
  { label: "Checks", subtitle: "consistency and evidence", x: .91, y: .43, color: "#e5b58c", stage: 5 },
  { label: "Quantum", subtitle: "lattice, complex structure, chart", x: .51, y: .10, color: "#c3b5f4", stage: 4 },
] as const;
const edges = [[0,2],[1,3],[2,3],[1,4],[3,4],[1,5],[0,6],[4,5],[4,6],[4,7],[0,7],[4,8],[5,9],[6,9],[7,9],[8,9],[2,1],[4,10],[10,8],[10,9]] as const;

export function TheoryJourney() {
  const [step, setStep] = useState(0);
  const [playing, setPlaying] = useState(true);
  const [reduced, setReduced] = useState(false);
  const canvas = useRef<HTMLCanvasElement>(null);
  const stage = stages[step];

  useEffect(() => {
    const query = window.matchMedia("(prefers-reduced-motion: reduce)");
    const sync = () => { setReduced(query.matches); if (query.matches) setPlaying(false); };
    sync(); query.addEventListener("change", sync);
    return () => query.removeEventListener("change", sync);
  }, []);

  useEffect(() => {
    const surface = canvas.current;
    if (!surface) return;
    const ctx = surface.getContext("2d");
    if (!ctx) return;
    let width = 900, height = 460, frame = 0, visible = true;
    const active: readonly number[] = stages[step].active;
    const positions = () => nodes.map(n => ({x:n.x * width, y:n.y * height}));
    const draw = (time: number) => {
      ctx.clearRect(0,0,width,height);
      const p = positions();
      edges.forEach(([a,b], i) => {
        const lit = active.includes(a) && active.includes(b);
        const start=p[a], end=p[b];
        ctx.beginPath();ctx.moveTo(start.x,start.y);ctx.lineTo(end.x,end.y);
        ctx.strokeStyle=lit?"#607b9c":"#24394e";ctx.lineWidth=lit?1.2:1;ctx.stroke();
        if(lit && playing && !reduced && visible){
          const t=((time*.00015+i*.123)%1);
          ctx.beginPath();ctx.arc(start.x+(end.x-start.x)*t,start.y+(end.y-start.y)*t,2.5,0,Math.PI*2);
          ctx.fillStyle=nodes[b].color;ctx.fill();
        }
      });
      nodes.forEach((n,i)=>{
        const lit=active.includes(i), point=p[i];
        ctx.globalAlpha=lit?1:.32;
        ctx.fillStyle="#102439";ctx.strokeStyle=n.color;ctx.lineWidth=lit?1.5:1;
        ctx.beginPath();ctx.arc(point.x,point.y,i===4?31:22,0,Math.PI*2);ctx.fill();ctx.stroke();
        if(i===0){const phase=playing&&!reduced?time*.0003:0;ctx.beginPath();ctx.arc(point.x,point.y,12,phase-.4,phase+Math.PI*1.55);ctx.stroke();const end=phase+Math.PI*1.55;const ex=point.x+12*Math.cos(end),ey=point.y+12*Math.sin(end);ctx.beginPath();ctx.moveTo(ex+5*Math.cos(end-.8),ey+5*Math.sin(end-.8));ctx.lineTo(ex,ey);ctx.lineTo(ex-5*Math.cos(end+.8),ey-5*Math.sin(end+.8));ctx.stroke();}
        else if(i===1){for(let k=0;k<5;k++){ctx.beginPath();ctx.fillStyle=k<3?"#89b5ff":"#75d5c5";ctx.arc(point.x-12+k*6,point.y,2,0,Math.PI*2);ctx.fill();}}
        else if(i===2){for(let k=0;k<4;k++){ctx.beginPath();ctx.arc(point.x+Math.cos(k*Math.PI/2)*12,point.y+Math.sin(k*Math.PI/2)*12,2.2,0,Math.PI*2);ctx.fillStyle=n.color;ctx.fill();}}
        else if(i===4){for(let k=0;k<8;k++){const t=k*Math.PI/4;ctx.beginPath();ctx.moveTo(point.x+Math.cos(t)*17,point.y+Math.sin(t)*17);ctx.lineTo(point.x+Math.cos(t+Math.PI*.75)*17,point.y+Math.sin(t+Math.PI*.75)*17);ctx.stroke();}}
        else if(i===8){ctx.beginPath();ctx.arc(point.x,point.y,11,-.5,Math.PI*1.3);ctx.stroke();ctx.beginPath();ctx.moveTo(point.x-11,point.y-5);ctx.lineTo(point.x-7,point.y-9);ctx.lineTo(point.x-5,point.y-3);ctx.stroke();}
        else if(i===9){ctx.beginPath();ctx.moveTo(point.x-8,point.y);ctx.lineTo(point.x-2,point.y+6);ctx.lineTo(point.x+9,point.y-7);ctx.stroke();}
        else {ctx.font=`${i===6?"italic ":""}17px Georgia,serif`;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillStyle=n.color;ctx.fillText(i===3?"3":i===5?"3+2":i===6?"α":i===7?"φ":i===10?"ψ":"",point.x,point.y);}
        ctx.globalAlpha=1;
        if(width>640){ctx.textAlign="center";ctx.textBaseline="top";ctx.font="600 13px system-ui,sans-serif";ctx.fillStyle=lit?"#f4f6fb":"#8092a8";ctx.fillText(n.label,point.x,point.y+(i===4?40:31));}
      });
      if(playing&&!reduced&&visible)frame=requestAnimationFrame(draw);
    };
    const resize=()=>{const box=surface.getBoundingClientRect();width=box.width;height=box.height;const dpr=Math.min(window.devicePixelRatio||1,2);surface.width=Math.round(width*dpr);surface.height=Math.round(height*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);cancelAnimationFrame(frame);draw(0);};
    const observer=new ResizeObserver(resize);observer.observe(surface);
    const visibility=()=>{visible=!document.hidden;cancelAnimationFrame(frame);if(visible)draw(0);};
    document.addEventListener("visibilitychange",visibility);resize();
    return()=>{cancelAnimationFrame(frame);observer.disconnect();document.removeEventListener("visibilitychange",visibility);};
  },[step,playing,reduced]);

  return <section className={styles.journey} aria-label="Guided journey through the connected theory">
    <div className={styles.stageBar}>
      <p>A shared structure. Several connected consequences.</p>
      <button type="button" aria-pressed={playing&&!reduced} disabled={reduced} onClick={()=>setPlaying(v=>!v)}>{playing?<Pause size={16}/>:<Play size={16}/>} {reduced?"Motion reduced":playing?"Pause motion":"Play motion"}</button>
    </div>
    <div className={styles.canvasWrap}>
      <canvas ref={canvas} className={styles.canvas} aria-label="Dependency map from boundary and carrier, through family geometry and E8, to charges, alpha, readouts, dynamics and checks">The boundary and carrier connect through family geometry and E₈ to charges, alpha, cosmological readouts and dynamics. Each result has its own assumptions and evidence.</canvas>
      <div className={styles.mapControls} aria-label="Explore a connection">
        {nodes.map((node,i)=><button key={node.label} type="button" style={{left:`${node.x*100}%`,top:`${node.y*100}%`}} aria-label={`Explore ${node.label}: ${node.subtitle}`} aria-pressed={stage.active.some(index=>index===i)} onClick={()=>setStep(node.stage)}><span>{node.label}</span></button>)}
      </div>
    </div>
    <div className={styles.story}>
      <div className={styles.storyText} aria-live="polite"><h2>{stage.title}</h2><p>{stage.body}</p><details><summary>Make the connection precise</summary><p>{stage.detail}</p></details><Link href={stage.href}>{stage.link}<ArrowRight size={16}/></Link>{step===4&&<Link href="/interactive/quantum">Explore quantum states and clocks<ArrowRight size={16}/></Link>}</div>
      <div className={styles.journeyControls}>
        <ol aria-label="Journey steps">{stages.map((s,i)=><li key={s.short}><button type="button" aria-current={i===step?"step":undefined} onClick={()=>setStep(i)}><span aria-hidden>{i+1}</span>{s.short}</button></li>)}</ol>
        <div className={styles.stepButtons}><button type="button" disabled={step===0} onClick={()=>setStep(v=>v-1)}><ArrowLeft size={18}/>Back</button><button type="button" onClick={()=>setStep(v=>v===stages.length-1?0:v+1)}>{step===stages.length-1?<><RotateCcw size={16}/>Start again</>:<>Next connection<ArrowRight size={18}/></>}</button></div>
      </div>
    </div>
    <p className={styles.mapCaption}>Moving points trace selected dependencies in this map. They do not depict particles travelling through physical space.</p>
  </section>;
}
