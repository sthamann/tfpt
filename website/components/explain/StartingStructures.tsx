"use client";

import { useId, useState } from "react";
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

/** Shared introductory section for the home page and the detailed guide. */
export function StartingStructures({ embedded = false }: { embedded?: boolean }) {
  const instance = useId();
  const [occupancy, setOccupancy] = useState<Occupancy>(2);
  const [chapter, setChapter] = useState(0);
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
          {chapter === 0 ? <><h4>The even carrier has a D₅ action.</h4><p>The five slot exterior algebra carries an explicit Clifford action. Its even part is the half spinor representation. D₅ names the associated rank five algebra; the branching drawing shows its Dynkin diagram.</p><Link href={source.geometry}>Inspect the carrier map</Link></> : chapter === 1 ? <><h4>Four marks leave three independent cycles.</h4><p>In the specified boundary dictionary, the marks are 1, i, −1 and −i on the projective line. Loops around the four punctures have one relation: their sum vanishes. Three independent cycles remain.</p><p>The family dictionary equips this rank three side with the A₃ lattice. A cycle count alone is not a physical identification of three particle families.</p><Link href={source.geometry}>Inspect the marked boundary dictionary</Link></> : <><h4>The join checks more than 5 + 3.</h4><p>D₅ and A₃ both have ℤ₄ discriminant groups. Their matched classes have squared lengths 5/4 and 3/4, adding to the even value 2. The compatible index four extension is the even, unimodular rank eight E₈ lattice.</p><p>This is a lattice construction under the specified dictionary. It does not make E₈ the physical gauge group by itself.</p><Link href={source.glue}>Inspect the ℤ₄ gluing theorem</Link></>}
        </div>
      </div>
      <div className={styles.chapterFooter}><p>Step {chapter + 1} of {chapters.length}</p><div><button type="button" disabled={chapter === 0} onClick={() => setChapter(value => value - 1)} aria-controls={panelId}><ChevronLeft size={18} aria-hidden/>Previous</button><button type="button" disabled={chapter === chapters.length - 1} onClick={() => setChapter(value => value + 1)} aria-controls={panelId}>Next<ChevronRight size={18} aria-hidden/></button></div></div>
      <details className={styles.details}><summary>Why does the lattice extension have determinant one?</summary><p>The two starting determinants are both 4. Extending by index 4 divides their product by 4²: (4 × 4)/4² = 1. The discriminant form matching supplies evenness. Together with positive definiteness and rank eight, these properties identify E₈.</p><Link href={source.glue}>Read the assumptions and construction</Link></details>
    </div>

    <div className={styles.branches}>
      <h3>The same inputs travel into different outputs.</h3>
      <p>The boundary normalization and carrier enter a shared seed and specified operators. Those connections carry their own assumptions into each readout.</p>
      <div className={styles.readouts}><article><h4>Boundary response → α</h4><p>The electromagnetic branch combines the common normalization, a specified response function and a carrier dependent budget in a closure equation.</p><Link href="/explain#alpha">Follow the alpha equation <ArrowRight size={17} aria-hidden/></Link></article><article><h4>Carrier and family operators → flavour</h4><p>The flavour branch uses the same seed with explicit family operators and transport rules to construct mass and mixing relations.</p><Link href="/explain#flavor">Follow the flavour construction <ArrowRight size={17} aria-hidden/></Link></article></div>
      <p className={styles.scope}>The equation, its numerical outputs and their physical interpretation have distinct scopes. Mass schemes, scale calibration and physical transfer conditions stay attached to the corresponding claim.</p>
    </div>

    <details className={`${styles.details} ${styles.sourceRoute}`}><summary>The common source route: where fields, state and time enter</summary>
      <p>The original construction carries the structured P1/P2 data through one shared source route. It reconstructs the local field net, vacuum representation and positive time evolution together under the theorem’s joint hypotheses.</p>
      <ol className={styles.route}><li><strong>Boundary kernel and carrier</strong><span>Specify the admissible sector P<sub>adm</sub>.</span></li><li><strong>Common action and generating functional</strong><span>S<sub>adm</sub> and Z<sub>rel</sub> supply the full field moments.</span></li><li><strong>OS/CAR reconstruction</strong><span>Reconstruct the Hilbert space, vacuum Ω, local field net and positive time evolution on the admissible sector.</span></li><li><strong>Renormalized effective action</strong><span>Γ<sub>ren</sub> feeds the specified physical readouts.</span></li></ol>
      <p>The OS/CAR theorem requires reflection positivity, temperedness, graded Euclidean covariance, graded symmetry and clustering together. The full route retains its measure, domain and limiting hypotheses.</p>
      <div className={styles.sources}><Link href={source.seed}>Common source construction</Link><Link href={source.reconstruction}>OS/CAR theorem and hypotheses</Link><Link href={source.readers}>Effective action and physical readers</Link></div>
    </details>
  </section>;
}
