"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Maximize2, Minimize2, Pause, Play, RotateCcw } from "lucide-react";
import { C3, E8_ROOTS, FIXED_SEED, alphaRoot, inner, seedReadouts } from "./mechanisms";
import styles from "./BeginnerJourney.module.css";

type Comparison = { predicted: number; central: string; uncertaintyMinus: string; date: string; measured: string };
type Point = { x: number; y: number };
type NodeId = "source" | "family" | "carrier" | "matter" | "e8" | "inputs" | "alpha" | "seed" | "test";
const chapters = [
  { short: "Four marks", title: "Start with one shared shape.", body: "Keep your eye on the four coloured marks. This one geometric setup will feed two different parts of the construction.", carry: "One starting geometry", result: "Four marked points", href: "/explain#inputs", link: "Explore the starting structure", detail: "The four point divisor is used in the stated sphere construction. The physical boundary source also contains its kernel, state and time; those inputs remain part of the full theory." },
  { short: "3 and 5", title: "The same four marks open two paths.", body: "Loops around the marks give three independent directions. Functions on the same shape give five internal slots. Watch both branches leave the same starting point.", carry: "The same four marks", result: "3 family directions + 5 internal slots", href: "/three-fermion-generations", link: "Try the shared structure", detail: "The punctured sphere has four loops with one relation, so its cycle space has rank three. The degree four divisor has five basic meromorphic functions, including the constant. These are different spaces with the same geometric source." },
  { short: "Standard Model", title: "Five slots organize a family of matter.", body: "Select zero, two or four of the five slots. There is one empty choice, ten pairs and five four-slot choices. Together they give the sixteen components of one family.", carry: "The five internal slots", result: "1 + 10 + 5 = 16 components", href: "/interactive/standard-model", link: "Build a matter pattern yourself", detail: "The even exterior states form the sixteen dimensional half spinor. The stated colour and weak slot dictionary supplies the Standard Model representations and hypercharges. The physical field interpretation retains its source assumptions." },
  { short: "E₈", title: "Bring the two structural branches together.", body: "The carrier and family lattices join by a matching rule. Four groups of vectors arrive in the same E₈ pattern. The matter structure stays connected to its carrier branch.", carry: "Carrier lattice + family lattice + matching rule", result: "52 + 60 + 64 + 64 = 240 roots", href: "/interactive/e8", link: "Assemble E₈ yourself", detail: "The construction joins D₅ and A₃ with the specified order four glue. The four root groups have sizes 52, 60, 64 and 64. The picture is a flat projection of the actual eight coordinate vectors. E₈ is the lattice closure here; its name alone does not identify a physical gauge group." },
  { short: "Shared inputs", title: "Follow the ingredients that are reused.", body: "The boundary rule supplies a normalization. Matter supplies component counts and a weighted budget. The carrier contributes its norm. These named ingredients meet in the numerical formulas.", carry: "Boundary rule + matter accounting + carrier norm", result: "The shared input set", href: "/explain#budget", link: "Follow the matter budget", detail: "The response uses c₃ = 1/(8π), 48 = 3 × 16 family components, the weighted matter budget 41 and the carrier norm 5/4. The budget requires the stated field weights and normalization. The seed uses c₃ and 48. E₈ alone does not fix every input." },
  { short: "Alpha", title: "The shared inputs meet at a balance point.", body: "Both sides of the alpha equation depend on the same trial number. Watch them balance. The balanced number is one divided by alpha, the strength of electromagnetic interaction.", carry: "The fixed inputs + the response equation", result: "Inverse alpha ≈ 137.036", href: "/interactive/alpha", link: "Find the balance yourself", detail: "The animation evaluates the existing full response equation, including its alpha dependent seam response. It locates its positive root. Identifying that response with physical electromagnetism is the separate physical reading described in the full derivation." },
  { short: "More results", title: "The same starting ingredients feed more answers.", body: "The boundary normalization and the count 48 also fix a small shared number. Four different formulas reuse it, linking particle mixing to the stated cosmic readouts. Alpha stays on its own branch.", carry: "The same normalization and component count", result: "One seed, four linked readouts", href: "/interactive/flavor", link: "Change the shared input yourself", detail: "The fixed seed is 1/(6π) + 48c₃⁴. Its four displayed readouts are quark mixing, neutrino mixing, light rotation in degrees and ordinary matter density. Their physical identifications retain their stated conditions. A shared input makes these values correlated." },
  { short: "Test", title: "Carry the calculated answers to a measurement.", body: "Follow the alpha branch to the dated observation. The measurement has its own uncertainty. The other readouts also need their corresponding tests. A connected calculation becomes useful when it can be checked.", carry: "Recorded calculations + independent observations", result: "Compare the same quantity on one scale", href: "/interactive/predictions", link: "Work through the comparison", detail: "The displayed alpha comparison uses the existing recorded value and CODATA 2022 measurement. These data were already known when this formula was frozen; this comparison is not a blind prediction. Other entries in the register retain their dates, conditions and categories." },
] as const;
const colours = { source: "#a8c7ff", family: "#79dcc5", carrier: "#a8c7ff", matter: "#a8c7ff", e8: "#c4b1ee", inputs: "#eec29c", alpha: "#eec29c", seed: "#79dcc5", test: "#e8f1fc" };
const births: Record<NodeId, number> = { source: 0, family: 1, carrier: 1, matter: 2, e8: 3, inputs: 4, alpha: 5, seed: 6, test: 7 };
const edges: { from: NodeId; to: NodeId; at: number; label?: string }[] = [
  { from: "source", to: "family", at: 1 }, { from: "source", to: "carrier", at: 1 },
  { from: "carrier", to: "matter", at: 2 },
  { from: "family", to: "e8", at: 3 }, { from: "carrier", to: "e8", at: 3 },
  { from: "matter", to: "inputs", at: 4, label: "counts + budget" }, { from: "e8", to: "inputs", at: 4, label: "carrier norm" },
  { from: "inputs", to: "alpha", at: 5 }, { from: "inputs", to: "seed", at: 6 },
  { from: "alpha", to: "test", at: 7 },
];
const clamp = (v: number) => Math.max(0, Math.min(1, v));
const ease = (v: number) => 1 - (1 - clamp(v)) ** 3;
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
const bits = Array.from({ length: 32 }, (_, mask) => mask).filter(mask => Array.from({ length: 5 }, (_, i) => Number(Boolean(mask & 1 << i))).reduce((a, b) => a + b, 0) % 2 === 0);
const rootOrder = [0, 2, 1, 3];
const rootPoints = E8_ROOTS.map(root => ({ group: rootOrder.indexOf(root.coset), x: inner(root.vector, Array.from({ length: 8 }, (_, i) => .5 * Math.cos(i * Math.PI / 4))), y: inner(root.vector, Array.from({ length: 8 }, (_, i) => .5 * Math.sin(i * Math.PI / 4))) }));
const root = 1 / alphaRoot();
const readouts = seedReadouts(FIXED_SEED);

function layout(mobile: boolean): Record<NodeId, Point> {
  return mobile ? { source: { x: 175, y: 80 }, family: { x: 85, y: 240 }, carrier: { x: 265, y: 240 }, matter: { x: 265, y: 425 }, e8: { x: 85, y: 425 }, inputs: { x: 175, y: 620 }, alpha: { x: 85, y: 810 }, seed: { x: 265, y: 810 }, test: { x: 175, y: 1005 } } : { source: { x: 85, y: 265 }, family: { x: 270, y: 115 }, carrier: { x: 270, y: 410 }, matter: { x: 475, y: 410 }, e8: { x: 475, y: 115 }, inputs: { x: 690, y: 265 }, alpha: { x: 900, y: 115 }, seed: { x: 900, y: 410 }, test: { x: 1110, y: 265 } };
}

function drawJourney(canvas: HTMLCanvasElement, progressPosition: number, step: number, expanded: boolean, comparisonDistance: number) {
  const position = expanded ? 7 : progressPosition;
  const ctx = canvas.getContext("2d"); if (!ctx) return;
  const { width, height } = canvas.getBoundingClientRect(); if (!width || !height) return;
  const mobile = width < 900, w = mobile ? 350 : 1200, scale = mobile && !expanded ? Math.min(width / w, 1.35) : width / w, dpr = Math.min(devicePixelRatio || 1, 2);
  canvas.width = Math.round(width * dpr); canvas.height = Math.round(height * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, width, height);
  const viewHeight = height / scale;
  const focusY = [140, 230, 380, 380, 580, 770, 770, 920];
  const camera = focusY.map(y => Math.max(-110, Math.min(1090 - viewHeight, y - viewHeight * .48)));
  const lower = Math.floor(position), cameraY = mobile && !expanded ? lerp(camera[lower], camera[Math.min(7, lower + 1)], position - lower) : 0;
  const offsetY = mobile ? -cameraY * scale : Math.max(0, (height - 550 * scale) / 2);
  ctx.translate(mobile ? (width - 350 * scale) / 2 : 0, offsetY); ctx.scale(scale, scale);
  const points = layout(mobile);
  const text = (value: string, x: number, y: number, size = 15, colour = "#d2e2f4", weight = 400) => { ctx.fillStyle = colour; ctx.font = `${weight} ${size}px system-ui,sans-serif`; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(value, x, y); };
  const circle = (x: number, y: number, r: number, fill: string, stroke?: string) => { ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fillStyle = fill; ctx.fill(); if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 1.5; ctx.stroke(); } };
  const line = (a: Point, b: Point, colour: string, alpha = 1) => { ctx.globalAlpha = alpha; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.strokeStyle = colour; ctx.lineWidth = 1.3; ctx.stroke(); ctx.globalAlpha = 1; };
  edges.forEach(edge => {
    const progress = clamp(position - edge.at + 1); if (!progress) {
      const a=points[edge.from],b=points[edge.to],dx=b.x-a.x,dy=b.y-a.y,length=Math.hypot(dx,dy);ctx.save();ctx.setLineDash([3,7]);ctx.strokeStyle="#2f4863";ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(a.x+dx/length*70,a.y+dy/length*70);ctx.lineTo(b.x-dx/length*70,b.y-dy/length*70);ctx.stroke();ctx.restore();return;
    }
    const a = points[edge.from], b = points[edge.to], dx = b.x - a.x, dy = b.y - a.y, dist = Math.hypot(dx, dy), cut = mobile ? 60 : 75;
    const start = { x: a.x + dx / dist * cut, y: a.y + dy / dist * cut }, end = { x: b.x - dx / dist * cut, y: b.y - dy / dist * cut };
    const bypass = edge.from === "source" && edge.to === "inputs";
    const c1 = bypass && mobile ? { x: 12, y: start.y + 70 } : { x: lerp(start.x, end.x, .35), y: start.y };
    const c2 = bypass && mobile ? { x: 12, y: end.y - 70 } : { x: lerp(start.x, end.x, .65), y: end.y };
    const at = (t: number) => ({ x: (1-t)**3*start.x+3*(1-t)**2*t*c1.x+3*(1-t)*t*t*c2.x+t**3*end.x, y: (1-t)**3*start.y+3*(1-t)**2*t*c1.y+3*(1-t)*t*t*c2.y+t**3*end.y });
    ctx.beginPath(); ctx.moveTo(start.x, start.y); for (let i = 1; i <= 40; i++) { const point = at(progress * i / 40); ctx.lineTo(point.x, point.y); }
    ctx.strokeStyle = colours[edge.from]; ctx.globalAlpha = edge.at === step ? .95 : .4; ctx.lineWidth = edge.at === step ? 2 : 1.3; ctx.stroke(); ctx.globalAlpha = 1;
    if (progress < 1) { const point = at(progress); circle(point.x, point.y, 4, colours[edge.from]); }
    if (edge.label && progress > .9 && !mobile) { const mid = at(.5); text(edge.label, mid.x, mid.y - 12, 12, "#adc5df"); }
  });
  (Object.keys(points) as NodeId[]).forEach(id => {
    const born = births[id], p = born === 0 ? 1 : clamp(position - born + 1); if (!p) {
      const labels: Record<NodeId,string>={source:"Four marks",family:"Family directions",carrier:"Internal slots",matter:"Standard Model",e8:"E₈",inputs:"Shared inputs",alpha:"Alpha",seed:"More readouts",test:"Alpha comparison"};const point=points[id];text(labels[id],point.x,point.y,14,"#809bb7");return;
    }
    const { x, y } = points[id], active = born === step, color = colours[id];
    ctx.save(); ctx.translate(x, y); ctx.globalAlpha = .65 + .35 * p;
    // The fixed positions preserve object identity; new branches arrive along their dependency paths.
    if (active) { ctx.beginPath(); ctx.roundRect(-81, -69, 162, 149, 10); ctx.strokeStyle = color; ctx.lineWidth = 1; ctx.stroke(); }
    if (id === "source") {
      ctx.strokeStyle = "#7294b5"; ctx.lineWidth = 1; ctx.beginPath(); ctx.arc(0, -8, 36, 0, Math.PI * 2); ctx.stroke(); ctx.beginPath(); ctx.ellipse(0, -8, 36, 12, 0, 0, Math.PI * 2); ctx.stroke();
      ["#a8c7ff", "#79dcc5", "#eec29c", "#c4b1ee"].forEach((c, i) => { const a = i * Math.PI / 2 - Math.PI / 2; circle(Math.cos(a)*29, -8 + Math.sin(a)*29, 5, c); });
      text("Four marks", 0, 49, 16, color, 600); text("shared geometry", 0, 69, 12, "#adc5df");
    } else if (id === "family" || id === "carrier") {
      const n = id === "family" ? 3 : 5;
      for (let i=0;i<n;i++) { const target = (i-(n-1)/2)*(n===5?22:30); circle(target, -5, n===5?7:10, color); }
      text(id === "family" ? "3 family directions" : "5 internal slots", 0, 38, 14, color, 600);
      text(id === "family" ? "family lattice" : "carrier lattice", 0, 59, 12, "#adc5df");
    } else if (id === "matter") {
      bits.slice(0, Math.max(1, Math.ceil(p * 16))).forEach((mask, i) => { const col=i%4,row=Math.floor(i/4); for(let k=0;k<5;k++) circle(-58+col*35+k*5,-40+row*20,1.7, mask&1<<k?color:"#36516e"); });
      text("Standard Model", 0, 48, 15, color, 600); text("16 components / family", 0, 69, 12, "#adc5df");
    } else if (id === "e8") {
      const groupProgress = p * 4;
      rootPoints.forEach(point => { const t=clamp(groupProgress-point.group); if(!t)return; const sx=0,sy=-5; circle(lerp(sx, point.x*39, ease(t)), lerp(sy, point.y*39-5, ease(t)), 1.5, ["#a8c7ff","#79dcc5","#eec29c","#c4b1ee"][point.group]); });
      text("E₈ lattice", 0, 48, 16, color, 600); text(`${[52,60,64,64].slice(0,Math.floor(groupProgress+1e-6)).reduce((a,b)=>a+b,0)} / 240 roots`, 0, 69, 12, "#adc5df");
    } else if (id === "inputs") {
      [["c₃", "1 / (8π)"], ["components", "48"], ["carrier norm", "5/4"], ["matter budget", "41"]].forEach(([label,value],i)=>{const cx=i%2?43:-43,cy=i<2?-35:18; text(label,cx,cy,11,"#adc5df");text(value,cx,cy+21,17,color,600);});
      text("Shared inputs", 0, 66, 15, color, 600);
      text("+ boundary normalization",0,mobile?-96:-121,12,color);line({x:0,y:mobile?-81:-106},{x:0,y:-58},color,p);
    } else if (id === "alpha") {
      const inverse = lerp(130, root, ease(p)), a = 1/inverse, q=48*C3**4*Math.exp(-2*a), response=1/(6*Math.PI)+q*(1-q)**(-5/4);
      const lhs=a**3-2*C3**3*a**2, rhs=4/5*41*C3**6*Math.log(1/response), max=(1/130)**3-2*C3**3*(1/130)**2;
      [lhs,rhs].forEach((v,i)=>{ctx.fillStyle="#2c435e";ctx.fillRect(-58,-34+i*24,116,9);ctx.fillStyle=i?"#79dcc5":color;ctx.fillRect(-58,-34+i*24,116*v/max,9);});
      text("Alpha balance",0,30,15,color,600);text(inverse.toFixed(6),0,54,18,color,600);text("one divided by alpha",0,73,11,"#adc5df");
    } else if (id === "seed") {
      const outer = [{x:-45,y:-32},{x:45,y:-32},{x:-45,y:22},{x:45,y:22}];
      outer.forEach((point,i)=>{line({x:0,y:-5},point,color,p);circle(point.x,point.y,6,["#a8c7ff","#79dcc5","#eec29c","#c4b1ee"][i]);});circle(0,-5,12,"#183c4a",color);
      text("Shared seed",0,52,15,color,600);text(FIXED_SEED.toFixed(7),0,73,15,color,600);
    } else {
      const measured=0, calculated=Math.max(-3,Math.min(3,comparisonDistance));
      ctx.fillStyle="#29594f";ctx.fillRect(-19,-28,38,25);line({x:-60,y:-3},{x:60,y:-3},"#adc5df");line({x:measured,y:-38},{x:measured,y:4},"#79dcc5");circle(calculated*19,-16,4,"#eec29c");
      text("measured",-29,-49,11,"#79dcc5");text("calculated",32,-49,11,"#eec29c");
      text("Alpha comparison",0,39,14,color,600);text("calculation + observation",0,62,11,"#adc5df");
    }
    ctx.restore();
  });
}

export function BeginnerJourney({ inverseAlpha, comparison }: { inverseAlpha: number; comparison: Comparison }) {
  const [step, setStep] = useState(0), [position, setPosition] = useState(0), [playing, setPlaying] = useState(false), [paused, setPaused] = useState(false), [reduced, setReduced] = useState(true), [expanded, setExpanded] = useState(false), [size, setSize] = useState(0);
  const canvas = useRef<HTMLCanvasElement>(null), section = useRef<HTMLElement>(null), currentPosition = useRef(0);
  const moving = Math.abs(position-step) > .0001, current = chapters[step];
  const go = (next: number) => { setPlaying(false); setPaused(false); setExpanded(false); setStep(next); };
  useEffect(() => { const media=matchMedia("(prefers-reduced-motion: reduce)");const sync=()=>{setReduced(media.matches);if(media.matches){setPlaying(false);setPaused(false);}};sync();media.addEventListener("change",sync);return()=>media.removeEventListener("change",sync); }, []);
  useEffect(() => {
    if(paused)return; if(reduced){currentPosition.current=step;setPosition(step);return;}
    const from=currentPosition.current;if(Math.abs(from-step)<.0001)return;let frame=0;const start=performance.now();
    const tick=(time:number)=>{const t=clamp((time-start)/1600),value=lerp(from,step,ease(t));currentPosition.current=value;setPosition(value);if(t<1)frame=requestAnimationFrame(tick);};frame=requestAnimationFrame(tick);return()=>cancelAnimationFrame(frame);
  },[step,paused,reduced]);
  useEffect(()=>{if(!playing||moving||paused||reduced)return;if(step===7){setPlaying(false);return;}const timer=setTimeout(()=>setStep(s=>s+1),3500);return()=>clearTimeout(timer);},[playing,moving,paused,reduced,step]);
  useEffect(()=>{const stop=()=>{setPlaying(false);setPaused(true);};const visibility=()=>{if(document.hidden)stop();};document.addEventListener("visibilitychange",visibility);const observer=new IntersectionObserver(([entry])=>{if(!entry.isIntersecting)stop();},{threshold:0});if(section.current)observer.observe(section.current);return()=>{document.removeEventListener("visibilitychange",visibility);observer.disconnect();};},[]);
  useEffect(()=>{const c=canvas.current;if(!c)return;const observer=new ResizeObserver(()=>setSize(c.getBoundingClientRect().width));observer.observe(c);return()=>observer.disconnect();},[]);
  useEffect(()=>{if(canvas.current)drawJourney(canvas.current,position,step,expanded,(comparison.predicted-Number(comparison.central))/Number(comparison.uncertaintyMinus));},[position,step,size,expanded,comparison.predicted,comparison.central,comparison.uncertaintyMinus]);
  const start=()=>{setExpanded(false);setPaused(false);if(step===7&&!moving){currentPosition.current=0;setPosition(0);setStep(0);}setPlaying(true);};
  const uncertainty=Number(comparison.uncertaintyMinus), distance=(comparison.predicted-Number(comparison.central))/uncertainty;
  return <section ref={section} className={styles.journey} aria-label="A connected animated journey through TFPT">
    <div className={styles.transport}>
      <div className={styles.playback}>{playing||(!paused&&moving)?<button type="button" onClick={()=>{setPlaying(false);setPaused(true);}}><Pause size={17}/>Pause journey</button>:<button type="button" onClick={start} disabled={reduced}>{step===7&&!moving?<RotateCcw size={17}/>:<Play size={17}/>} {step===7&&!moving?"Replay journey":paused?"Resume journey":"Play journey"}</button>}<span>Step {step+1} of {chapters.length}</span></div>
      <div className={styles.arrows}><button type="button" aria-label="Previous step" disabled={step===0} onClick={()=>go(step-1)}><ArrowLeft size={18}/></button><button type="button" disabled={step===7} onClick={()=>go(step+1)}>Next step<ArrowRight size={18}/></button></div>
    </div>
    <div className={styles.story} aria-live={playing?"off":"polite"}><h2>{current.title}</h2><p>{current.body}</p></div>
    <figure className={styles.figure}>
      <canvas ref={canvas} className={`${styles.canvas}${expanded?` ${styles.expanded}`:""}`} role="img" aria-label={expanded?"Complete connection map: four marks, family and carrier spaces, Standard Model components, E8, shared inputs, alpha, seed readouts and the separate alpha measurement comparison.":`Step ${step+1}. ${current.carry} leads to ${current.result}. The diagram retains the preceding branches.`}>Four marked points supply three family directions and five internal slots. Five slots organize sixteen matter components. Carrier and family lattices join into E8. Boundary normalization, matter accounting and carrier norm enter the alpha response. The normalization and component count also supply a shared seed. The alpha branch is compared with its dated measurement; the other readouts need their own tests.</canvas>
      <button className={styles.mapSize} type="button" aria-pressed={expanded} onClick={()=>{setExpanded(v=>!v);setPlaying(false);setPaused(true);}}>{expanded?<Minimize2 size={15}/>:<Maximize2 size={15}/>} {expanded?"Follow the journey":"See the whole map"}</button>
      <figcaption>Lines carry shared ingredients into the next calculation. Earlier branches stay in place. {reduced?"Reduced motion is on. Use Next step or choose any stage below.":"Play the journey, pause anywhere, or choose your own step."}</figcaption>
    </figure>
    <ol className={styles.route} aria-label="Choose a stage of the connected journey">{chapters.map((chapter,index)=><li key={chapter.short} data-reached={position>=index}><button type="button" aria-current={step===index?"step":undefined} onClick={()=>go(index)}><span>{index+1}</span>{chapter.short}</button></li>)}</ol>
    <div className={styles.takeaway}><div><span>{current.carry}</span><ArrowRight size={20} aria-hidden/><strong>{current.result}</strong></div>
      {step===5&&<p>The fixed equation gives inverse alpha {inverseAlpha.toFixed(10)}. Alpha itself is approximately {(1/inverseAlpha).toFixed(8)}.</p>}
      {step===6&&<dl className={styles.readouts}>{["Quark mixing","Neutrino mixing","Light rotation","Ordinary matter"].map((label,i)=><div key={label}><dt>{label}</dt><dd>{readouts[i].toFixed(7)}{i===2?"°":""}</dd></div>)}</dl>}
      {step===7&&<p>Alpha example: calculated {comparison.predicted.toFixed(10)}, measured {comparison.measured} ({comparison.date}). The difference is {distance.toFixed(2)} quoted experimental uncertainties.</p>}
      <Link href={current.href}>{current.link}<ArrowRight size={16}/></Link>
    </div>
    <details className={styles.precise}><summary>See the rule behind this connection</summary><p>{current.detail}</p></details>
    <p className={styles.branches}>Keep exploring the other branches: <Link href="/interactive/dynamics">Dynamical change</Link>, <Link href="/interactive/quantum">quantum states and clocks</Link>, and <Link href="/interactive/cosmology">cosmic scales</Link>.</p>
  </section>;
}
