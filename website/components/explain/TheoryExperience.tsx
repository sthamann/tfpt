"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { ArrowDown, ArrowRight } from "lucide-react";

const outcomes = [
  { title: "Particles & charges", short: "Particles", second: "& charges", text: "The representations and charges of one Standard Model family, with a separate geometric construction for three families.", scope: "Representation and charge results", query: "hypercharge", href: "/explain#matter" },
  { title: "Masses & mixing", short: "Masses", second: "& mixing", text: "Relative charged lepton and quark source masses, a common hierarchy and specified constructions for particle mixing.", scope: "Source relations; physical mass transfer has its own conditions", query: "flavor", href: "/explain#flavor" },
  { title: "Electromagnetic coupling", short: "Electromagnetic", second: "coupling α", text: "A fixed boundary equation with one positive root close to the measured electromagnetic coupling. The equation, its root and its physical origin are distinct results.", scope: "Mathematical closure; physical identification remains a separate task", query: "alpha-global-positive-root", href: "/explain#alpha" },
  { title: "Cosmological readouts", short: "Cosmic", second: "patterns", text: "Conditional readouts for the rotation of polarized light, the ordinary matter fraction, early cosmic expansion and the vacuum energy hierarchy.", scope: "Conditional physical readouts and dated predictions", query: "cosmo", href: "/predictions" },
  { title: "Quantum & information structure", short: "Quantum", second: "structure", text: "Exact connections between the E₈ lattice, coding and finite quantum geometry. Source histories can preserve information that a compressed readout loses.", scope: "Scoped mathematical and source reconstruction results", query: "quartic", href: "/explain#quantum" },
  { title: "Clocks & dynamics", short: "Clocks", second: "& dynamics", text: "Related finite clock actions, exact relaxation in the specified transfer model and constructed state and time bridges.", scope: "Operator relations; physical time and a common source remain separate", query: "clock", href: "/explain#clocks" },
];

const points = [[300,65],[490,170],[490,350],[300,455],[110,350],[110,170]];

function Constellation({ scene = 0 }: { scene?: number }) {
  const active = scene === 1 ? [0,4] : scene === 2 ? [1,2,3] : [0,1,2,3,4,5];
  return <svg className="theory-constellation" viewBox="0 0 600 550" role="img" aria-label={scene === 1 ? "The carrier and lattice construction connect particle representations and quantum geometry." : scene === 2 ? "Shared seeds and budgets connect flavour, alpha and conditional cosmological readouts." : "Overview of six connected TFPT research areas: particles and charges, masses and mixing, alpha, cosmology, quantum structure, clocks and dynamics. This is a map of dependencies, not a picture of physical space."}>
    <g className="constellation-paths">{points.map(([x,y],i)=><path key={`${i}-${active.includes(i)}`} pathLength="1" className={active.includes(i)?"is-lit":""} d={`M300 275 Q${x < 300 ? 205 : x > 300 ? 395 : 350} ${(275+y)/2} ${x} ${y}`} />)}</g>
    <circle className="constellation-core" cx="300" cy="275" r="78" />
    <text className="constellation-center" x="300" y="265" textAnchor="middle"><tspan x="300">{scene === 1 ? "Carrier" : scene === 2 ? "Shared seeds" : "One shared"}</tspan><tspan x="300" dy="31">{scene === 1 ? "& lattices" : scene === 2 ? "& budgets" : "construction"}</tspan></text>
    {points.map(([x,y],i)=><g key={i} className={`constellation-branch ${active.includes(i)?"is-lit":""}`}><circle cx={x} cy={y} r="10" /><text x={x} y={y<275?y-60:y+35} textAnchor="middle"><tspan x={x}>{outcomes[i].short}</tspan><tspan x={x} dy="27">{outcomes[i].second}</tspan></text></g>)}
  </svg>;
}

export function BigPictureHero() {
  return <section className="big-picture-hero" aria-labelledby="big-picture-title"><div className="experience-shell big-picture-layout">
    <div className="big-picture-copy"><h1 id="big-picture-title">Connecting the particles and constants of nature.</h1>
      <p className="big-picture-lead">TFPT investigates how much of the Standard Model of particle physics and its constants can follow from one mathematical construction, without fitting each result separately.</p>
      <p>Particle charges. Mass relations. Electromagnetic coupling. Connections reaching into quantum structure, time and cosmology. Start with the results, then follow what connects them.</p>
      <div className="experience-actions"><a href="#outcomes" className="experience-primary">See what the theory determines <ArrowDown size={18} aria-hidden /></a><a href="#connections" className="experience-secondary">Follow the connections <ArrowRight size={18} aria-hidden /></a></div>
      <p className="experience-byline">Topological Fixed-Point Theory · Stefan Hamann & Alessandro Rizzo</p>
    </div>
    <figure className="big-picture-figure"><Constellation /><figcaption>A map of connected research areas. The status of each result appears below.</figcaption></figure>
  </div></section>;
}

export function OutcomeAtlas() {
  return <section className="experience-shell outcome-atlas" id="outcomes" aria-labelledby="outcome-title">
    <div className="experience-heading"><h2 id="outcome-title">What does the theory determine?</h2><p>Several parts of physics become outputs of the same specified construction. Some are exact mathematical results; others are conditional physical readouts. A complete physical realization remains an open research goal.</p></div>
    <div className="outcome-list">{outcomes.map(item=><article key={item.title}><h3><Link href={item.href}>{item.title} <ArrowRight size={20} aria-hidden /></Link></h3><div><p>{item.text}</p><p className="outcome-scope">{item.scope}. <Link href={`/results?search=${encodeURIComponent(item.query)}`}>Inspect the evidence</Link>.</p></div></article>)}</div>
    <p className="parameter-intro" id="parameter-definition"><strong>“Parameter free” within a specified branch:</strong> no separate fitted number for each output. The starting inputs and any physical calibration conditions remain part of the claim.</p>
    <details className="parameter-meaning"><summary>What does “parameter free” mean here?</summary><p>Within a specified branch, the inputs fix the stated output. A separate fitted number is not supplied for every observable. The boundary normalization, carrier, marking, transport rules and branch choices still belong to the starting construction. Some physical readouts also require scale calibration, mass scheme transfer or cosmological assumptions. Those conditions remain attached to the result.</p><Link className="guide-link" href="/explain#inputs">Inspect the starting inputs</Link><Link className="guide-link" href="/predictions">Distinguish predictions, assigned values and conditional bands</Link></details>
  </section>;
}

const scenes = [
  { title: "One construction feeds several parts of physics.", text: "The results are connected. Particle representations, the lattice structure, flavour operators and boundary response reuse the same starting data. The point is to understand those shared dependencies.", link: "/explain#inputs", label: "See the starting structure" },
  { title: "Geometry organizes the particle content.", text: "The marked carrier supplies representations and charges. Compatible lattice data on the carrier and family sides join into E₈. The lattice closure and the interpretation as physical fields are distinct steps.", link: "/explain#e8", label: "Follow the lattice construction" },
  { title: "Shared seeds connect the numerical readouts.", text: "Flavour relations, the electromagnetic boundary equation and conditional cosmological readouts share seeds or budgets. Their agreement has to be assessed with those dependencies in view; the outputs are correlated.", link: "/explain#alpha", label: "Follow a connection into alpha" },
];

export function ConnectionStory() {
  const [scene,setScene]=useState(0);
  const [manual,setManual]=useState(false);
  const [compact,setCompact]=useState(false);
  const root=useRef<HTMLElement>(null);
  useEffect(()=>{
    const media=window.matchMedia("(max-width:900px)");
    const update=()=>setCompact(media.matches);
    update();media.addEventListener("change",update);
    return ()=>media.removeEventListener("change",update);
  },[]);
  useEffect(()=>{
    if(manual || compact) return;
    const observer=new IntersectionObserver(entries=>{
      const visible=entries.filter(entry=>entry.isIntersecting).sort((a,b)=>b.intersectionRatio-a.intersectionRatio);
      if(visible[0]) setScene(Number((visible[0].target as HTMLElement).dataset.scene));
    },{rootMargin:window.matchMedia("(max-width:900px)").matches?"-60% 0px -5% 0px":"-25% 0px -30% 0px",threshold:[0,.25,.5,.75]});
    root.current?.querySelectorAll("[data-scene]").forEach(el=>observer.observe(el));
    return ()=>observer.disconnect();
  },[manual,compact]);
  return <section ref={root} id="connections" className="connection-story" data-compact={compact} aria-labelledby="connections-title">
    <div className="experience-shell"><div className="experience-heading"><h2 id="connections-title">How does it all connect?</h2><p>Explore the shared construction, then follow two threads: the geometric structure and the numerical readouts.</p></div>
      <div className="connection-layout"><div className="connection-stage"><Constellation scene={scene}/><div className="connection-controls" role="group" aria-label="Connection map views">{["Whole picture","Geometry","Shared readouts"].map((label,i)=><button key={label} type="button" aria-pressed={scene===i} onClick={()=>{setManual(true);setScene(i);}}>{label}</button>)}</div><button className="connection-follow" type="button" aria-pressed={!manual} onClick={()=>setManual(v=>!v)}>{manual?"Follow the text":"Following text · switch to manual"}</button><p className="connection-caption">Lines show shared construction and dependencies. This is a reading map, not physical spacetime.</p></div>
      <div className="connection-chapters">{scenes.map((item,i)=><article key={item.title} data-scene={i} className={scene===i?"is-current":""}><h3>{item.title}</h3><p>{item.text}</p><Link className="guide-link" href={item.link}>{item.label} <ArrowRight size={18} aria-hidden /></Link>{i<scenes.length-1&&<button type="button" className="compact-story-next" onClick={()=>{setManual(true);setScene(i+1);root.current?.querySelectorAll<HTMLButtonElement>(".connection-controls button")[i+1]?.focus({preventScroll:true});root.current?.querySelector(".connection-stage")?.scrollIntoView({block:"start",behavior:window.matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"});}}>Next connection <ArrowRight size={18} aria-hidden /></button>}</article>)}</div></div>
    </div>
  </section>;
}

export function MethodAndDiscoveries() {
  return <div className="experience-shell">
    <section className="method-story" id="method-overview"><div className="experience-heading"><h2>How does the construction work?</h2><p>Start with declared inputs, apply explicit maps, then compare the resulting statements with mathematics and measurement.</p></div>
      <ol className="method-path"><li><h3>Specify the starting structure.</h3><p>An oriented boundary and a marked internal carrier. Their normalization and rules are explicit inputs.</p><Link href="/explain#inputs">Starting inputs</Link></li><li><h3>Construct representations and operators.</h3><p>Exterior algebra, lattice matching and transport rules produce the particle sectors and connected readout operators.</p><Link href="/explain#matter">A worked charge example</Link></li><li><h3>Calculate, prove and test.</h3><p>Separate exact identities and numerical outputs from physical assumptions. Compare predictions with data and preserve scoped exclusions.</p><Link href="/verification">Verification and reproduction</Link></li></ol>
      <p className="method-open"><strong>The common physical origin remains the central task.</strong> The constructed pieces do not yet amount to a complete interacting quantum theory in physical spacetime with three spatial dimensions and time. The actual source, state, dynamics and gravity have their own open connections.</p>
    </section>
    <section className="discovery-story" id="discoveries"><div className="experience-heading"><h2>What is remarkable about the connections?</h2><p>The interesting part is where a structure reappears in a different role, through a map that can be checked.</p></div>
      <article><h3>The charge trace also enters the alpha budget.</h3><p>The same family charges participate in the compiler budget used by the electromagnetic equation. The identity retains its flavour transport and Higgs assumptions.</p><Link href="/explain#budget">Trace the connection</Link></article>
      <article><h3>One seed builds several levels of a hierarchy.</h3><p>Fixed powers and rational coefficients connect the charged lepton source masses. The same seed also appears in mixing and other readout branches.</p><Link href="/explain#flavor">See the mass ladder</Link></article>
      <article><h3>The clocks act on one another.</h3><p>The quarter action relabels the five cycle. It is an explicit operator relation, with four actions returning the labels to their starting point.</p><Link href="/explain#clocks">Try the clock action</Link></article>
      <article><h3>A present readout need not contain the whole history.</h3><p>The source construction retains information needed for later responses that a finite compressed readout can lose.</p><Link href="/results?search=memory">Inspect the source and memory results</Link></article>
    </section>
  </div>;
}
