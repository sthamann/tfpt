"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Play } from "lucide-react";
import { useReproducer } from "@/components/Reproducer";
import styles from "./compiler.module.css";

const SECTIONS = [
  { id: "outputs", label: "What comes out" },
  { id: "construction", label: "How E₈ is constructed" },
  { id: "inputs", label: "What goes in" },
  { id: "physics", label: "The physical connection" },
] as const;
type Section = typeof SECTIONS[number]["id"];

function makeRoots(): { integer: number[][]; half: number[][] } {
  // Same explicit coordinate construction as verification/v1_e8_glue.py.
  const integer: number[][] = [], half: number[][] = [];
  for (let i = 0; i < 8; i++) for (let j = i + 1; j < 8; j++) {
    for (const a of [1, -1]) for (const b of [1, -1]) {
      const root = Array<number>(8).fill(0); root[i] = a; root[j] = b; integer.push(root);
    }
  }
  for (let mask = 0; mask < 256; mask++) {
    const root = Array.from({ length: 8 }, (_, i) => mask & (1 << i) ? -.5 : .5);
    if (root.filter(x => x < 0).length % 2 === 0) half.push(root);
  }
  return { integer, half };
}
const ROOTS = makeRoots();

function RootExplorer() {
  const [family, setFamily] = useState<"integer" | "half">("integer");
  const [index, setIndex] = useState(0);
  const roots = ROOTS[family], root = roots[index];
  const choose = (value: "integer" | "half") => { setFamily(value); setIndex(0); };
  const coordinate = (x: number) => x === .5 ? "+½" : x === -.5 ? "−½" : x > 0 ? "+1" : x < 0 ? "−1" : "0";
  return <figure className={styles.figure}>
    <figcaption><h3>Inspect an actual E₈ root.</h3><p>Each root is a vector with eight coordinates. Choose either family, then move through its vectors. This is the explicit coordinate construction used in the first verification module.</p></figcaption>
    <div className={styles.controls} role="group" aria-label="Root family">
      <button type="button" aria-pressed={family === "integer"} onClick={() => choose("integer")}>112 integer roots</button>
      <button type="button" aria-pressed={family === "half"} onClick={() => choose("half")}>128 half integer roots</button>
    </div>
    <div className={styles.vector} aria-live="polite" aria-atomic="true">
      <dl className={styles.coordinates} aria-label="Root coordinates">{root.map((value, i) => <div key={i}><dt>x<sub>{i + 1}</sub></dt><dd>{coordinate(value)}</dd></div>)}</dl>
      <div className={styles.measure}><strong>Squared length = {root.reduce((sum, x) => sum + x * x, 0)}</strong><span>{family === "integer" ? "Two coordinates contribute 1² + 1²." : "Eight coordinates contribute 8 × (½)²; the number of minus signs is even."}</span></div>
    </div>
    <div className={styles.rootNavigation}>
      <button type="button" onClick={() => setIndex(i => (i - 1 + roots.length) % roots.length)}><ArrowLeft size={16} aria-hidden /> Previous root</button>
      <span>Root {index + 1} of {roots.length}</span>
      <button type="button" onClick={() => setIndex(i => (i + 1) % roots.length)}>Next root <ArrowRight size={16} aria-hidden /></button>
    </div>
    <p className={styles.note}>The two families contain 112 + 128 = 240 roots. Inspecting coordinates explains the construction; the Python module also checks the lattice basis, integrality and determinant.</p>
  </figure>;
}

export function CompilerExplorer() {
  const [active, setActive] = useState<Section>("outputs");
  const { open } = useReproducer();
  return <section className={styles.explorer} aria-label="Explore the compiler">
    <div className={styles.controls} role="group" aria-label="Choose a part of the compiler">
      {SECTIONS.map(section => <button type="button" key={section.id} aria-pressed={active === section.id} aria-controls="compiler-explanation" onClick={() => setActive(section.id)}>{section.label}</button>)}
    </div>
    <div id="compiler-explanation" className={styles.explanation}>
      {active === "outputs" && <>
        <h2>One construction, several kinds of output.</h2>
        <p>The lattice, a numerical fixed point and a physical prediction belong to different layers. Follow any one into its detailed source and status.</p>
        <dl className={styles.outputList}>
          <div><dt>E₈ lattice</dt><dd><strong>240 roots in eight dimensions</strong><p>An explicit mathematical construction with a basis certificate.</p><button type="button" onClick={() => setActive("construction")} className={styles.link}>Inspect the construction <ArrowRight size={16} aria-hidden /></button></dd></div>
          <div><dt>Electromagnetic readout</dt><dd><strong>α⁻¹ ≈ 137.0359992</strong><p>The numerical fixed point of the stated electromagnetic closure equation. Its numerical evaluation and physical identification are separate questions.</p><Link href="/results?search=alpha" className={styles.link}>Read the result and its scope <ArrowRight size={16} aria-hidden /></Link></dd></div>
          <div><dt>Matter and flavor</dt><dd><strong>Representations, families and mixing structure</strong><p>Readouts from the carrier and the flavor construction, with physical transfer assumptions stated in their sources.</p><Link href="/papers/standard-model" className={styles.link}>Follow the Standard Model readout <ArrowRight size={16} aria-hidden /></Link></dd></div>
        </dl>
      </>}
      {active === "construction" && <>
        <h2>The glue has a checkable construction.</h2>
        <p>D₅ and A₃ share ℤ₄ discriminant data. Their glue norms add to the required root norm: 5/4 + 3/4 = 2. The resulting rank eight lattice can be built explicitly.</p>
        <RootExplorer />
        <div className={styles.actions}><button type="button" className={styles.primary} onClick={() => open("v1_e8_glue.py")}><Play size={16} aria-hidden /> Run the complete lattice check</button><a href="/verification/v1_e8_glue.py" className={styles.link}>Read its Python source</a></div>
      </>}
      {active === "inputs" && <>
        <h2>The starting assumptions stay visible.</h2>
        <p>The compiler starts from the seam normalization and a five slot carrier. Their stated status as inputs is distinct from the exact mathematical consequences that follow under those premises.</p>
        <dl className={styles.outputList}><div><dt>Seam normalization</dt><dd><strong>c₃ = 1/(8π)</strong><p>The declared normalization entering the electromagnetic closure and other boundary readouts.</p></dd></div><div><dt>Carrier rank</dt><dd><strong>g<sub>car</sub> = 5</strong><p>The carrier used in the D₅ construction. Its even exterior algebra has dimension 1 + 10 + 5 = 16.</p></dd></div></dl>
        <p>The architecture discusses consistency relations and reductions among these inputs. An internal consistency relation does not independently establish their physical origin.</p>
        <Link href="/orientation" className={styles.link}>Read the assumptions in context <ArrowRight size={16} aria-hidden /></Link>
      </>}
      {active === "physics" && <>
        <h2>Where mathematics meets the physical claim.</h2>
        <p>Constructing E₈ establishes a lattice result. The Standard Model readout, the charged seam, continuum dynamics and experimental predictions need their own maps, assumptions and tests.</p>
        <dl className={styles.outputList}><div><dt>Mathematical consequence</dt><dd>The lattice certificate checks the construction in its stated setting.</dd></div><div><dt>Physical identification</dt><dd>A claim about an actual physical system must identify its states, symmetries, operators and interactions.</dd></div><div><dt>Experimental test</dt><dd>A prediction is read with its frozen value, conditions and a declared criterion for failure.</dd></div></dl>
        <div className={styles.actions}><Link href="/results" className={styles.primary}>Read achieved results and open questions <ArrowRight size={16} aria-hidden /></Link><Link href="/falsification" className={styles.link}>Inspect the failure tests</Link></div>
      </>}
    </div>
  </section>;
}
