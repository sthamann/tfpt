"use client";
import { useId, useState } from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { chargeSectors } from "@/lib/carrier";
import { ChargeExplorer, AlphaExplorer, ClockExplorer } from "./InteractiveReadouts";
import { AlphaComparison, LeptonLadder } from "./DerivationFigures";
import { Math as Formula } from "@/components/Math";

export function OutputPlate(){
 return <figure className="output-plate" aria-label="Three examples of outputs of the specified TFPT construction">
  <div className="output-lane"><div><h3>A family of particle charges</h3><p>Quark and lepton sectors from the same internal carrier.</p></div><div className="output-family" aria-label="Six sectors, with one, three, six, one, two and three components">{chargeSectors.map(s=><div key={s.label}><strong>{s.label}</strong><div>{Array.from({length:s.multiplicity},(_,i)=><i key={i}/>)}</div></div>)}</div></div>
  <div className="output-lane"><div><h3>A hierarchy of masses</h3><p>Fixed relative lepton source masses.</p></div><div className="output-masses" aria-label="Electron, muon and tau source mass hierarchy on a logarithmic scale"><div><span>e</span><i style={{width:"12%"}}/></div><div><span>μ</span><i style={{width:"70%"}}/></div><div><span>τ</span><i style={{width:"100%"}}/></div><small>Logarithmic positions · source ratios</small></div></div>
  <div className="output-lane"><div><h3>A precise electromagnetic root</h3><p>Calculated from the specified boundary equation.</p></div><div className="output-alpha"><strong>α⁻¹ = 137.035 999 2168…</strong><div aria-label="Separate measured uncertainty band and calculated point"><span className="output-measured"/><i/></div><p className="output-alpha-legend"><span><b className="legend-measured"/>CODATA 2022 ±1σ</span><span><b className="legend-calculated"/>Calculated root</span></p><small>1.90 measured uncertainties above the central value</small></div></div>
  <figcaption>These are mathematical outputs of the construction. Their physical interpretation and measurement comparisons retain their stated conditions.</figcaption>
 </figure>;
}

export function LatticeMatch(){
 const [selected,setSelected]=useState(1);const uid=useId();
 const qd=["0","5/4","1","5/4"],qa=["0","3/4","1","3/4"];
 return <div className="lattice-lesson"><p className="lesson-lead">Two lattices can join because their boundary classes match. Select a class and inspect the norm condition.</p>
 <svg viewBox="0 0 640 310" role="img" aria-label={`Allowed matching of discriminant class ${selected}. D5 and A3 each have four classes. The two discriminant norms add to an even integer.`}>
  <defs><marker id={`${uid}-arrow`} markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="#315783"/></marker></defs>
  <text x="130" y="35" textAnchor="middle" fontSize="30" fill="#183b65">D₅ carrier lattice</text><text x="510" y="35" textAnchor="middle" fontSize="30" fill="#183b65">A₃ family lattice</text>
  {[0,1,2,3].map(i=><g key={i} className={selected===i?"lattice-class is-current":"lattice-class"}><line x1="155" y1={80+i*52} x2="485" y2={80+i*52} stroke={selected===i?"#285d91":"#bbc9d7"} strokeWidth={selected===i?3:1} markerEnd={selected===i?`url(#${uid}-arrow)`:undefined}/><circle cx="130" cy={80+i*52} r="18" fill={selected===i?"#285d91":"#f3f6f9"} stroke="#8099b3"/><circle cx="510" cy={80+i*52} r="18" fill={selected===i?"#285d91":"#f3f6f9"} stroke="#8099b3"/><text x="130" y={87+i*52} textAnchor="middle" fontSize="28" fill={selected===i?"#fff":"#344e6a"}>{i}</text><text x="510" y={87+i*52} textAnchor="middle" fontSize="28" fill={selected===i?"#fff":"#344e6a"}>{i}</text></g>)}
  <text x="320" y="300" textAnchor="middle" fontSize="23" fill="#344e6a">An allowed matching of the four discriminant classes</text>
 </svg>
 <div className="lesson-controls" role="group" aria-label="Discriminant class">{[0,1,2,3].map(i=><button type="button" key={i} aria-pressed={selected===i} onClick={()=>setSelected(i)}>Class {i}</button>)}</div>
 <p className="norm-readout" aria-live="polite">qD₅ = {qd[selected]} <span>+</span> qA₃ = {qa[selected]} <span>→</span> {selected===0?"0":"2"} ≡ 0 (mod 2)</p>
 <div className="lattice-conclusion"><div><h4>The matching permits an index four extension.</h4><Formula block plain="The glued lattice has determinant one.">{String.raw`\det L=\frac{4\cdot4}{4^2}=1`}</Formula></div><ArrowRight aria-hidden/><div><h4>Even, positive, unimodular and rank eight.</h4><p>These properties identify the resulting lattice as E₈.</p></div></div>
 <p className="lesson-scope">This is the lattice construction under the given carrier, family lattice and glue data. Selecting physical fields and gauge interactions requires its own dictionary.</p><Link className="guide-link" href="/results?topic=topic%3Ae8">Explore the E₈ research and its conditions</Link>
 </div>;
}

export function BudgetLesson(){
 const [step,setStep]=useState(0);
 const labels=["Sum the family charges","Connect the compiler budget","Include the Higgs term"];
 return <div className="budget-lesson"><p className="lesson-lead">The charge pattern participates in another part of the construction. Follow the identity, while retaining the flavour operators and their transport rules.</p>
 <div className="lesson-controls" role="group" aria-label="Charge budget explanation">{labels.map((label,i)=><button type="button" key={label} aria-pressed={step===i} onClick={()=>setStep(i)}>{label}</button>)}</div>
 <div className="budget-teaching-grid"><div><h4>The whole family</h4><p className="lesson-small">Each contribution is multiplicity × X², with X = 6Y.</p><div className="charge-bars">{chargeSectors.map(s=><div key={s.label}><span>{s.label}</span><div><i style={{width:`${s.contribution/48*100}%`}}/></div><strong>{s.contribution}</strong></div>)}</div><p className="budget-total">Tr X² = <strong>120</strong></p></div>
 <div className={`budget-teaching-stage ${step>=1?"is-current":""}`}><span className="budget-identity-arrow" aria-hidden>→</span><h4>A stated compiler identity</h4><Formula block>{String.raw`\Sigma L=\frac{\operatorname{Tr}X^2}{3}=40`}</Formula><p>This connects the existing flavour budget and charge trace. It does not construct individual flavour operators from the total.</p><p className="lesson-small">The division is not an average over three families.</p></div>
 <div className={`budget-teaching-stage ${step>=2?"is-current":""}`}><span className="budget-identity-arrow" aria-hidden>→</span><h4>The specified Higgs content</h4><p className="higgs-budget"><span>40</span><span>+ H</span><strong>41</strong></p><p>One Higgs contribution supplies the final unit of the stated electromagnetic budget.</p><Link className="guide-link" href="/explain#alpha">See where 41 enters the equation</Link></div></div>
 <p className="lesson-caption" aria-live="polite">{step===0?"All sixteen components contribute to one family charge trace.":step===1?"The identity is exact within the compiler contract, with its operator and transport assumptions.":"The budget is one ingredient of the fixed boundary equation. Its physical electromagnetic origin remains a further question."}</p>
 </div>;
}

const lessons=[
 {id:"charges",title:"Particle charges",heading:"How do the particle charges appear?",intro:"The given carrier has colour and weak slots with fixed hypercharges. Selecting them shows a component, its charge and its place in the whole family."},
 {id:"glue",title:"E₈ closure",heading:"Why can the two lattice sides join?",intro:"Matching discriminant forms supplies the actual connection. Adding their ranks alone would not identify E₈."},
 {id:"budget",title:"Shared alpha budget",heading:"How do the charges enter the alpha budget?",intro:"The charge trace, flavour budget and Higgs contribution meet through a specified compiler identity."},
 {id:"alpha",title:"Alpha and measurement",heading:"What does solving the alpha equation mean?",intro:"The curve shows the residual of a fixed equation. Its root is a mathematical result. A separate graphic compares that root with measured data."},
 {id:"masses",title:"Mass hierarchy",heading:"Why do the source masses form a ladder?",intro:"Different fixed powers of one small seed create separated levels. The common source scale cancels in ratios."},
 {id:"clocks",title:"Clock actions",heading:"How does one clock act on another?",intro:"Follow the actual relabeling of the five cycle. Four applications restore the original labels; this operation does not set seconds."},
];
export function MechanismWalkthrough(){
 const [active,setActive]=useState("charges");const lesson=lessons.find(l=>l.id===active)!;
 return <section className="mechanism-walkthrough" id="connections"><div className="experience-shell"><header className="experience-heading"><h2>See how the pieces actually connect.</h2><p>Choose a connection. Each figure shows the operation, the result and the assumptions it needs.</p></header>
 <div className="mechanism-tabs" role="group" aria-label="Explanatory figures">{lessons.map(l=><button key={l.id} type="button" aria-pressed={active===l.id} onClick={()=>setActive(l.id)}>{l.title}</button>)}</div>
 <div className="mechanism-reading"><h3>{lesson.heading}</h3><p>{lesson.intro}</p></div>
 <div className="mechanism-panel" aria-label={lesson.title}>{active==="charges"?<ChargeExplorer/>:active==="glue"?<LatticeMatch/>:active==="budget"?<BudgetLesson/>:active==="alpha"?<><div className="alpha-reading-path"><span>Given response</span><ArrowRight aria-hidden/><span>Solve the fixed equation</span><ArrowRight aria-hidden/><span>Compare with data</span></div><AlphaExplorer/><AlphaComparison/></>:active==="masses"?<LeptonLadder/>:<ClockExplorer/>}</div>
 <div className="mechanism-next"><Link href="/compiler">Follow the complete compiler path <ArrowRight size={18}/></Link><Link href="/results">Explore the questions and attempts behind the results <ArrowRight size={18}/></Link></div>
 </div></section>;
}
