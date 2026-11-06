"use client";

import { useEffect, useId, useState } from "react";
import Link from "next/link";
import { ArrowRight, ChevronLeft, ChevronRight } from "lucide-react";
import { Math } from "@/components/Math";
import styles from "./StartingStructures.module.css";

const source = {
  inputs: "/documentation?section=section%3A1234c1fa7fdc0d6d5b35",
  geometry: "/documentation?section=section%3A584e87a9c163ac38f92f",
  glue: "/documentation?section=section%3A2befc1b3b29d5cae0f23",
  seed: "/documentation?section=section%3Ada5a8d451e469c6cb1f5",
  reconstruction: "/documentation?section=section%3A591993c8c68b37136f0d",
  readers: "/documentation?section=section%3A3e7cfda7c9252d871993",
};

const occupancies = [0, 2, 4] as const;
type Occupancy = (typeof occupancies)[number];
const multiplicity: Record<Occupancy, number> = { 0: 1, 2: 10, 4: 5 };
const chosenSlots: Record<Occupancy, number[]> = { 0: [], 2: [1, 3], 4: [0, 1, 2, 3] };
const chapters = ["Build the carrier", "Read the four marks", "Join compatible lattices"];

const slotNames = ["c₁", "c₂", "c₃", "w₁", "w₂"];
const rootClasses = [
  { label: "Class 0", count: 52, vector: [1,-1,0,0,0,0,0,0], explanation: "The two nonzero entries stay in one block. The five coordinate block contributes 40 D₅ roots; the three coordinate block contributes 12 A₃ roots.", countRule: "4 × choose(5, 2) + 4 × choose(3, 2) = 40 + 12 = 52", norm: "1² + (−1)² = 2" },
  { label: "Class 2", count: 60, vector: [1,0,0,0,0,1,0,0], explanation: "One nonzero entry sits in each block. Choose one of five positions, one of three positions and either sign independently at both positions.", countRule: "5 × 3 × 4 = 60 mixed integer roots", norm: "1² + 1² = 2" },
  { label: "Class 1", count: 64, vector: [.5,.5,.5,.5,.5,.5,.5,.5], explanation: "All eight entries are half integers. In this class, each block has an even number of minus signs: 16 sign choices on the five coordinate side and 4 on the three coordinate side.", countRule: "16 × 4 = 64 half integer roots", norm: "5 × (½)² + 3 × (½)² = 5/4 + 3/4 = 2" },
  { label: "Class 3", count: 64, vector: [-.5,.5,.5,.5,.5,-.5,.5,.5], explanation: "The other half integer class has an odd number of minus signs in each block. The combined eight coordinates still have an even number of minus signs.", countRule: "16 × 4 = 64 half integer roots", norm: "5 × (½)² + 3 × (½)² = 5/4 + 3/4 = 2" },
] as const;

export function CliffordOperation() {
  const [slot, setSlot] = useState(1);
  const [state, setState] = useState<{ occupied: number[]; sign: number; explanation: string }>({ occupied: [0,3], sign: 1, explanation: "Start with c₁ and w₁ occupied: an even degree two basis state." });
  const act = (creation: boolean) => {
    setState(previous => {
      if (previous.sign === 0) return { ...previous, explanation: "Every linear operator sends the zero vector to zero. Reset to try a new operation." };
      const present = previous.occupied.includes(slot);
      if (creation === present) return { ...previous, sign: 0, explanation: creation ? "That slot is already occupied. Inserting it again gives the zero vector." : "That slot is empty. Removing it gives the zero vector." };
      const crossed = previous.occupied.filter(value => value < slot).length;
      const occupied = creation ? [...previous.occupied, slot].sort((a,b) => a-b) : previous.occupied.filter(value => value !== slot);
      return { occupied, sign: previous.sign * (crossed % 2 ? -1 : 1), explanation: `${creation ? "Insert" : "Remove"} ${slotNames[slot]}. Passing ${crossed} earlier occupied ${crossed === 1 ? "slot" : "slots"} contributes ${crossed % 2 ? "a minus sign" : "a plus sign"}. The resulting degree is ${occupied.length}, ${occupied.length % 2 ? "odd" : "even"}.` };
    });
  };
  const vector = state.sign === 0 ? "0" : `${state.sign < 0 ? "−" : ""}${state.occupied.length ? state.occupied.map(index => slotNames[index]).join(" ∧ ") : "1 (empty state)"}`;
  return <div className={styles.operation}>
    <p className={styles.operationIntro}>Try the operation that builds the spinor.</p>
    <div className={styles.operationSlots} aria-label={state.sign === 0 ? "Zero vector" : `Occupied slots: ${state.occupied.map(index => slotNames[index]).join(", ") || "none"}`}>
      {slotNames.map((name, index) => <span key={name} data-occupied={state.sign !== 0 && state.occupied.includes(index)}><span>{name}</span><span aria-hidden="true" className={styles.occupationMark}/></span>)}
    </div>
    <div className={styles.operationControls}><label>Choose a slot<select value={slot} onChange={event => setSlot(Number(event.target.value))}>{slotNames.map((name, index) => <option key={name} value={index}>{name}</option>)}</select></label><button type="button" onClick={() => act(true)}>Insert</button><button type="button" onClick={() => act(false)}>Remove</button><button type="button" onClick={() => setState({ occupied: [0,3], sign: 1, explanation: "Reset to the even state c₁ ∧ w₁." })}>Reset</button></div>
    <div className={styles.operationOutcome} aria-live="polite" aria-atomic="true"><p className={styles.stateVector}>{vector}</p><p>{state.explanation}</p></div>
    <p>Each insertion or removal changes parity. A pair of these operations returns to the original parity. The even 16 dimensional space is preserved by the quadratic spin action, rather than by each individual gamma operator.</p>
  </div>;
}

export function MarkedModes() {
  return <div className={styles.markedModes}>
    <MarksDiagram/>
    <div className={styles.twoReadings}><div><h5>Read loops around the marks.</h5><p>On the punctured sphere, going around all four punctures is homologically trivial. Thus:</p><p className={styles.shortFormula}>ℓ₁ + ℓᵢ + ℓ₋₁ + ℓ₋ᵢ = 0</p><p>One relation among four loops leaves three independent cycles. This fixes rank H₁ = 3.</p></div><div><h5>Read functions with simple poles.</h5><p>Allow a simple pole at each marked point and require regularity elsewhere, including infinity. Every such function has the form:</p><div className={styles.inlineFormula}><Math>{String.raw`f(z)=b_0+\sum_{a\in D}\frac{b_a}{z-a}`}</Math></div><p>One constant and four independent pole coefficients give five modes.</p></div></div>
    <p className={styles.basisLabel}>An explicit basis of H⁰(ℙ¹, O(D)):</p>
    <ul className={styles.modeBasis} aria-label="Five meromorphic basis functions"><li><Math>{"1"}</Math></li>{["1","i","-1","-i"].map(a => <li key={a}><Math>{`\\frac{1}{z${a.startsWith("-") ? "+" + a.slice(1) : "-" + a}}`}</Math></li>)}</ul>
    <details className={styles.details}><summary>Which pairing turns the three directions into A₃?</summary><p>The family dictionary supplies the residue and Cartan pairing. In four formal coordinate directions, the differences e₁ − e₂, e₂ − e₃ and e₃ − e₄ span the sum zero subspace. Their Gram matrix is:</p><div className={styles.inlineFormula}><Math>{String.raw`\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix},\qquad\det=4`}</Math></div><p>This is A₃: its twelve roots are eᵢ − eⱼ for i ≠ j. The eᵢ are formal basis vectors. This specified pairing is distinct from geometric chord distances between the complex marks. Three cycles alone would not determine it.</p><Link href={source.geometry}>Read the family dictionary in its source context</Link></details>
    <p className={styles.scope}>These are two exact invariants of the same divisor D = &#123;1, i, −1, −i&#125;. Identifying this five dimensional function space with the physical, marked 3 + 2 carrier is the conditional carrier reading. Riemann–Roch does not assign colour to particular poles or derive the marked split.</p>
    <Link href="/documentation?evidence=python_verification%3Averification%2Fv189_riemann_roch_carrier.py">Read the exact scope of the carrier reading in v189</Link>
  </div>;
}

function SeamGeometry() {
  return <svg viewBox="0 0 360 230" role="img" aria-label="An oriented circular seam with an arrow making one complete winding. Paired points indicate the boundary response kernel. A schematic of the declared boundary data, not a physical shape prediction." className={styles.seam}>
    <ellipse cx="180" cy="118" rx="115" ry="75" className={styles.seamInterior}/>
    <ellipse cx="180" cy="118" rx="115" ry="75" className={styles.seamLine}/>
    <path d="M75 80 C101 41 173 23 230 48" className={styles.winding}/>
    <path d="m222 37 12 13-17 1" className={styles.winding}/>
    <path d="M85 154 Q180 208 275 154" className={styles.kernel}/>
    <circle cx="85" cy="154" r="6" className={styles.endpoint}/>
    <circle cx="275" cy="154" r="6" className={styles.endpoint}/>
    <text x="180" y="109" textAnchor="middle" className={styles.svgMain}>one winding</text>
    <text x="180" y="136" textAnchor="middle" className={styles.svgSmall}>oriented seam Σ</text>
    <text x="180" y="216" textAnchor="middle" className={styles.svgSmall}>paired boundary response</text>
  </svg>;
}

function SlotsGeometry({ occupancy }: { occupancy: Occupancy }) {
  const xs = [38, 102, 166, 258, 322];
  return <svg viewBox="0 0 360 230" role="img" aria-label={`Five internal slots: three colour slots with hypercharge minus one third and two weak slots with hypercharge plus one half. One example selecting ${occupancy} slots is highlighted.`} className={styles.slots}>
    <path d="M38 105H322" className={styles.slotAxis}/>
    {xs.map((x, index) => <g key={x}>
      <circle cx={x} cy="105" r="25" className={index < 3 ? styles.colourSlot : styles.weakSlot}/>
      {chosenSlots[occupancy].includes(index) && <circle cx={x} cy="105" r="11" className={styles.selectedSlot}/>}
      <text x={x} y="153" textAnchor="middle" className={styles.svgSmall}>{index < 3 ? `c${index + 1}` : `w${index - 2}`}</text>
    </g>)}
    <path d="M15 172v10h174v-10M235 172v10h110v-10" className={styles.slotBrace}/>
    <text x="102" y="211" textAnchor="middle" className={styles.svgSmall}>colour · −⅓ each</text>
    <text x="290" y="211" textAnchor="middle" className={styles.svgSmall}>weak · +½ each</text>
    <text x="180" y="38" textAnchor="middle" className={styles.svgSmall}>internal labels, not spatial directions</text>
  </svg>;
}

function CarrierDiagram() {
  return <svg viewBox="0 0 300 190" role="img" aria-label="The D5 Dynkin diagram: a chain of three nodes whose last node branches to two further nodes." className={styles.connectionSvg}>
    <path d="M35 95H165L250 38M165 95l85 57" className={styles.dynkinLine}/>
    {[[35,95],[100,95],[165,95],[250,38],[250,152]].map(([x,y]) => <circle key={`${x}-${y}`} cx={x} cy={y} r="10" className={styles.dynkinNode}/>)}
  </svg>;
}

function MarksDiagram() {
  return <svg viewBox="0 0 300 190" role="img" aria-label="Four marked points 1, i, minus 1 and minus i on the projective line. Loops around all four points satisfy one relation, leaving three independent cycles." className={styles.connectionSvg}>
    <circle cx="150" cy="95" r="61" className={styles.markCircle}/>
    {[[211,95,"1"],[150,34,"i"],[89,95,"−1"],[150,156,"−i"]].map(([x,y,label]) => <g key={label}><circle cx={x} cy={y} r="7" className={styles.endpoint}/><text x={Number(x)+(x===211?22:x===89?-25:0)} y={Number(y)+(y===34?-17:y===156?26:6)} textAnchor="middle" className={styles.svgSmall}>{label}</text></g>)}
  </svg>;
}

function GlueDiagram() {
  return <div className={styles.glueGraphic}>
    <div className={styles.glueLabels}><span>D₅ · 5/4</span><span>A₃ · 3/4</span></div>
    <div className={styles.normCells} role="img" aria-label="Eight equal quarters of squared length: five quarters from D5 and three quarters from A3, totaling two.">{Array.from({ length: 8 }, (_, i) => <span key={i} className={i < 5 ? styles.normCarrier : styles.normFamily}/>)}</div>
    <p className={styles.normCaption}>Matching ℤ₄ classes · total squared length 2</p>
    <svg viewBox="0 0 340 100" role="img" aria-label="The E8 Dynkin diagram, a chain of seven nodes with one extra node attached to the third." className={styles.e8Diagram}>
      <path d="M35 70H305M125 70V20" className={styles.dynkinLine}/>
      {[35,80,125,170,215,260,305].map(x => <circle key={x} cx={x} cy="70" r="7" className={styles.dynkinNode}/>)}
      <circle cx="125" cy="20" r="7" className={styles.dynkinNode}/>
    </svg>
  </div>;
}

export function RootClasses() {
  const [selected, setSelected] = useState(0);
  const root = rootClasses[selected];
  const coordinate = (value: number) => value === .5 ? "½" : value === -.5 ? "−½" : value === -1 ? "−1" : String(value);
  return <div className={styles.rootConstruction}>
    <h5>Build the roots in four cosets.</h5>
    <p>Split eight Euclidean coordinates into five and three. In this coordinate model, A₃ is realized as the isometric D₃ root lattice. The extension joins four paired discriminant classes. Each contributes the following norm two vectors.</p>
    <div className={styles.cosetControls} role="group" aria-label="Inspect one of the four gluing classes">{rootClasses.map((item, index) => <button key={item.label} type="button" aria-pressed={selected === index} onClick={() => setSelected(index)}><span>{item.label}</span><strong>{item.count} roots</strong></button>)}</div>
    <div className={styles.rootExample} aria-live="polite" aria-atomic="true">
      <p><strong>{root.label}:</strong> {root.explanation}</p>
      <p className={styles.countRule}>{root.countRule}</p>
      <p className={styles.basisLabel}>One actual root, shown coordinate by coordinate:</p>
      <div className={styles.coordinateLabels}><span>D₅ coordinates</span><span>A₃ ≅ D₃ coordinates</span></div>
      <div className={styles.coordinates} role="img" aria-label={`Root coordinates: ${root.vector.slice(0,5).join(", ")}, followed by ${root.vector.slice(5).join(", ")}. Squared norm two.`}>{root.vector.map((value,index) => <span key={index} data-block={index < 5 ? "carrier" : "family"}>{coordinate(value)}</span>)}</div>
      <p className={styles.rootNorm}>Squared length: {root.norm}</p>
      {selected === 0 && <p>The A₃ roots occupy the other block, for example (0, 0, 0, 0, 0 | 1, −1, 0).</p>}
    </div>
    <p className={styles.rootTotal}>52 + 60 + 64 + 64 = <strong>240 roots</strong></p>
    <p>Integer roots have two entries ±1 and six zeroes. Half integer roots have eight entries ±½ with an even number of minus signs. These explicit vectors, together with the lattice basis and its Gram matrix, provide the E₈ construction. The identity 5/4 + 3/4 = 2 is its compatibility check, not the whole construction.</p>
    <p className={styles.scope}>The labels 1 and 3 depend on the choice of discriminant generator and can be interchanged. The four cosets are lattice classes, not four particle species.</p>
    <Link href="/documentation?evidence=python_verification%3Averification%2Fv1_e8_glue.py">Inspect the explicit root and lattice certificate in v1</Link>
  </div>;
}

/** Shared introductory section for the home page and the detailed guide. */
export function StartingStructures({ embedded = false }: { embedded?: boolean }) {
  const instance = useId();
  const [occupancy, setOccupancy] = useState<Occupancy>(2);
  const [chapter, setChapter] = useState(0);
  useEffect(() => {
    const selectHash = (hash: string) => {
      if (hash === "#root-classes") {
        setChapter(2);
        requestAnimationFrame(() => document.getElementById("root-classes")?.scrollIntoView({ block: "start" }));
      }
    };
    const reveal = () => selectHash(window.location.hash);
    const click = (event: MouseEvent) => {
      const anchor = event.target instanceof Element ? event.target.closest("a[href]") : null;
      if (!anchor) return;
      const url = new URL(anchor.getAttribute("href")!, window.location.href);
      if (url.origin === window.location.origin && url.pathname === window.location.pathname) selectHash(url.hash);
    };
    reveal();
    window.addEventListener("hashchange", reveal);
    document.addEventListener("click", click, true);
    return () => { window.removeEventListener("hashchange", reveal); document.removeEventListener("click", click, true); };
  }, []);
  const panelId = `${instance}-connection`;
  return <section id="inputs" className={`${styles.root}${embedded ? ` ${styles.embedded}` : ""}`} aria-labelledby={`${instance}-heading`}>
    <header className={styles.heading}>
      <h2 id={`${instance}-heading`}>Two starting structures.<br/>One connected construction.</h2>
      <p>A boundary response supplies a common normalization. A five slot carrier supplies internal structure. TFPT specifies both, then follows the maps that connect them.</p>
    </header>

    <div className={styles.startingPair}>
      <article className={styles.boundary}>
        <h3>P1: an oriented boundary</h3>
        <p>Give the boundary a direction and one full winding. The kernel specifies how a change at one boundary point contributes to the response at another. c₃ sets its normalization.</p>
        <SeamGeometry/>
        <p className={styles.formula}><Math ariaLabel="c three equals one divided by eight pi">{String.raw`c_3=\frac{1}{8\pi}`}</Math></p>
        <details className={styles.details}><summary>What does the first input, P1, specify?</summary>
          <p>P1 assumes a primitive, reflection positive boundary kernel on an oriented seam, with unit winding. The stated self linking normalization fixes c₃. Reflection positivity is the positivity condition used by the later quantum reconstruction.</p>
          <p>This is structured starting data. The picture shows its orientation and pairing; it does not establish a universal physical origin for the kernel.</p>
          <p>Why 8π? In the stated normal slice normalization, the two sheet factor and the sphere Euler characteristic give 2 × 2π × 2 = 8π. The same value is written using the anchor a = (1,1,2): its sum is e₁ = 4, so c₃ = 1/(2e₁π). These are geometric and arithmetic connections within the declared construction. The ledger keeps P1 typed as an axiom.</p>
          <Link href={source.inputs}>Read the P1 definition</Link>
          <Link href="/results?claim=AX.P1.01">Read the normalization and its exact ledger status</Link>
        </details>
      </article>

      <article className={styles.carrier}>
        <h3>P2: five internal slots</h3>
        <p>Think of five internal labels whose allowed combinations build a particle family. Three belong to the colour sector of the strong interaction and two to the weak sector. The algebra assigns the displayed hypercharges.</p>
        <SlotsGeometry occupancy={occupancy}/>
        <div className={styles.selection}>
          <p id={`${instance}-selection`}>Keep selections with an even number of slots.</p>
          <div className={styles.controls} role="group" aria-labelledby={`${instance}-selection`}>{occupancies.map(value => <button key={value} type="button" aria-pressed={occupancy === value} onClick={() => setOccupancy(value)}>{value} slots</button>)}</div>
          <p className={styles.selectionResult} aria-live="polite" aria-atomic="true"><strong>{multiplicity[occupancy]} {multiplicity[occupancy] === 1 ? "choice" : "choices"}</strong> with {occupancy} slots. {occupancy ? "The diagram highlights one example." : "The empty selection also counts."}</p>
        </div>
        <p className={styles.total}>Together: <strong>1 + 10 + 5 = 16</strong> components.</p>
        <details className={styles.details}><summary>What does P2 assume, and what follows?</summary>
          <p>P2 supplies the five slot interface with its 3 + 2 split. Given the stated idempotent and lattice axioms, the algebra fixes the colour and weak hypercharges, −1/3 and +1/2.</p>
          <p>The even exterior algebra keeps all choices of zero, two or four slots. Their counts are the binomial coefficients 1, 10 and 5. With the Clifford action, this is the 16 dimensional half spinor of Spin(10), associated with D₅. The representation is more than a matching dimension.</p>
          <p>Why five? The marked interface is supplied in P2. A separate consistency bootstrap singles out g = 5 in its stated positive integer comparison class, through 2ᵍ = g² + g + 2. That rigidity result and the physical origin of the interface answer different questions.</p>
          <Link href={source.inputs}>P2 interface and algebra</Link><Link href={source.geometry}>Exterior algebra and carrier construction</Link>
        </details>
      </article>
    </div>

    <div className={styles.connection}>
      <header className={styles.subheading}><h3>How do the pieces fit?</h3><p>Follow the carrier, the marked boundary and the compatibility test that joins their lattices.</p></header>
      <div className={styles.chapterControls} role="group" aria-label="Explore the structural connection">{chapters.map((label, index) => <button key={label} type="button" aria-pressed={chapter === index} aria-controls={panelId} onClick={() => setChapter(index)}><span>{index + 1}</span>{label}</button>)}</div>
      <div id={panelId} className={styles.connectionPanel}>
        <div className={styles.connectionImage}>{chapter === 0 ? <CarrierDiagram/> : chapter === 1 ? <MarksDiagram/> : <GlueDiagram/>}</div>
        <div className={styles.connectionCopy} aria-live="polite" aria-atomic="true">
          {chapter === 0 ? <><h4>Insert, remove, then combine the operations.</h4><p>A basis state records which of five slots are occupied. Exterior multiplication inserts a slot; contraction removes one. Their signs remember the order. Combining these five pairs gives ten Clifford gamma operators.</p><p>The quadratic gamma generators act as so(10), whose root system is D₅. They preserve the even part with 1 + 10 + 5 = 16 components. The drawing identifies the algebra; the operation below shows how it acts.</p><Link href={source.geometry}>Inspect the carrier construction</Link></> : chapter === 1 ? <><h4>The same four marks have two different readings.</h4><p>Take D = &#123;1, i, −1, −i&#125; on the projective line. Loops around the punctures give a rank three cycle space. Meromorphic functions with at most a simple pole at each mark give a five dimensional function space.</p><p>The specified family dictionary supplies the A₃ lattice on the rank three side. The function space gives a geometric carrier reading, with the physical identification still conditional.</p><Link href={source.geometry}>Inspect the two readings of the divisor</Link></> : <><h4>Compatible classes supply the missing vectors.</h4><p>D₅ and A₃ both have ℤ₄ discriminant groups. Pairing their four classes extends the direct sum by index four. The norm relation 5/4 + 3/4 = 2 checks that the half integer vectors have the required even length.</p><p>To see the actual construction, inspect the four cosets below. They supply 52, 60, 64 and 64 roots. The completed lattice is E₈; its physical interpretation requires the stated dictionary.</p><Link href={source.glue}>Inspect the ℤ₄ gluing theorem</Link></>}
        </div>
      </div>
      <div id="root-classes" className={styles.workedStep}>{chapter === 0 ? <><CliffordOperation/><details className={styles.details}><summary>How do five operator pairs become ten gammas and so(10)?</summary><p>Write a†ⱼ for insertion and aⱼ for removal in the ordered exterior basis. The canonical anticommutation relations encode exclusion and the signs. For j = 1, …, 5:</p><div className={styles.inlineFormula}><Math>{String.raw`\{a_j,a_k^\dagger\}=\delta_{jk},\quad \{a_j,a_k\}=\{a_j^\dagger,a_k^\dagger\}=0`}</Math></div><div className={styles.inlineFormula}><Math>{String.raw`\gamma_{2j-1}=a_j^\dagger+a_j,\qquad\gamma_{2j}=i(a_j^\dagger-a_j)`}</Math></div><p>These ten gamma operators satisfy &#123;γₐ, γᵦ&#125; = 2δₐᵦ. Each gamma flips even and odd degree. The quadratic generators ¼[γₐ, γᵦ] preserve parity and realize the spin representation of so(10). Its even sector is S⁺ = Λ⁰ ⊕ Λ² ⊕ Λ⁴, of dimension 16; the full exterior algebra has dimension 32.</p><p>This is an operation in a representation space. Calling the operators creation and annihilation does not by itself identify an instrument that physically creates particles. The physical carrier interpretation retains its assumptions.</p><Link href="/documentation?evidence=python_verification%3Averification%2Fv197_rr_carrier_clifford_d5.py">Inspect the Clifford carrier scope in v197</Link></details></> : chapter === 1 ? <MarkedModes/> : <RootClasses/>}</div>
      <div className={styles.chapterFooter}><p>Step {chapter + 1} of {chapters.length}</p><div><button type="button" disabled={chapter === 0} onClick={() => setChapter(value => value - 1)} aria-controls={panelId}><ChevronLeft size={18} aria-hidden/>Previous</button><button type="button" disabled={chapter === chapters.length - 1} onClick={() => setChapter(value => value + 1)} aria-controls={panelId}>Next<ChevronRight size={18} aria-hidden/></button></div></div>
      <details className={styles.details}><summary>Why does the lattice extension have determinant one?</summary><p>The two starting determinants are both 4. Extending by index 4 divides their product by 4²: (4 × 4)/4² = 1. The discriminant form matching supplies evenness. Together with positive definiteness and rank eight, these properties identify E₈.</p><Link href={source.glue}>Read the assumptions and construction</Link></details>
    </div>

    <div className={styles.branches}>
      <h3>The same inputs travel into different outputs.</h3>
      <p>The boundary normalization and carrier enter a shared seed and specified operators. Those connections carry their own assumptions into each readout.</p>
      <div className={styles.readouts}><article><h4>Boundary response → α</h4><p>The electromagnetic branch combines the common normalization, a specified response function and a carrier dependent budget in a closure equation.</p><Link href="/explain#alpha">Follow the alpha equation <ArrowRight size={17} aria-hidden/></Link></article><article><h4>Carrier and family operators → flavour</h4><p>The flavour branch uses the same seed with explicit family operators and transport rules to construct mass and mixing relations.</p><Link href="/explain#flavor">Follow the flavour construction <ArrowRight size={17} aria-hidden/></Link></article></div>
      <p className={styles.scope}>The equation, its numerical outputs and their physical interpretation have distinct scopes. Mass schemes, scale calibration and physical transfer conditions stay attached to the corresponding claim.</p>
    </div>

    <p className={styles.scope}>The source action and full field moments also enter a joint reconstruction of the field net, vacuum and positive time. <Link href="#source">Follow that common source route once, with its full hypotheses.</Link></p>

  </section>;
}
