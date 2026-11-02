"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowDown, ArrowRight } from "lucide-react";
import { Math } from "@/components/Math";
import styles from "./SharedStructureBridge.module.css";

export function SharedStructureBridge({ compact = false }: { compact?: boolean }) {
  const [step,setStep] = useState(0);
  return <section id={compact ? "connections" : "e8"} className={`${compact ? "experience-shell" : "guide-section"} ${styles.section}`} aria-labelledby="shared-structure-heading">
    <header><h2 id="shared-structure-heading">Follow the same structure into a different result.</h2><p>The two lattice norms that make the E₈ join possible reappear in the specified electromagnetic response. The matter budget enters the same equation. Follow the quantities across that connection.</p></header>
    <div className={styles.controls} role="group" aria-label="Trace the shared invariants">{["Join the lattices","Read the boundary response","Close the equation"].map((s,i)=><button type="button" key={s} aria-pressed={step===i} aria-controls="shared-structure-panel" onClick={()=>setStep(i)}>{s}</button>)}</div>
    <div className={styles.bridge}>
      <div className={styles.original}><h3>Carrier and family geometry</h3><p>Representative squared norms in the two ℤ₄ discriminant groups</p><div className={styles.norms}><div><span>D₅ carrier</span><strong className={styles.carrier}>5/4</strong></div><div><span>A₃ family side</span><strong className={styles.family}>3/4</strong></div></div><div className={styles.quarters} role="img" aria-label="Five quarters plus three quarters give squared norm two">{Array.from({length:8},(_,i)=><i key={i} data-carrier={i<5}/>)}</div><p><strong>5/4 + 3/4 = 2.</strong> Matching the full discriminant forms permits an even index four extension. The new cosets complete E₈.</p></div>
      <ArrowRight className={styles.direction} aria-hidden/>
      <div id="shared-structure-panel" className={styles.reading} aria-live="polite">
        {step===0 ? <><h3>The join is an operation.</h3><p>The direct D₅ ⊕ A₃ lattice contains 52 roots. Adding the three matched cosets contributes 60, 64 and 64 more. All 240 have squared norm two.</p><Math block>{String.raw`\det L=\frac{4\cdot4}{4^2}=1`}</Math><p>Evenness, positive definiteness and rank eight identify the resulting unimodular lattice as E₈. The norm sum is the compatibility check within this construction.</p><Link href="/explain#root-classes">Build the actual cosets and inspect a root</Link></> : step===1 ? <><h3>The norms keep their identity.</h3><div className={styles.reuse}><div><strong className={styles.carrier}>5/4</strong><p>becomes the power of the marked carrier response</p><Math block>{String.raw`(1-q)^{-5/4}`}</Math></div><div><strong className={styles.family}>3/4</strong><p>sets the base opening relative to c₃</p><Math block>{String.raw`\varphi_{\rm base}=\frac{c_3}{3/4}=\frac1{6\pi}`}</Math></div></div><p>The marked D₅ grade calculation realizes the fractional power in the stated source. These identities explain the coefficients used by the EM branch; the local physical EM functional retains its own identification.</p></> : <><h3>The matter budget joins the response.</h3><p>The specified matter construction supplies M = 40 + 1 = 41. Together with the boundary normalization and response it fixes the displayed equation.</p><Math block>{String.raw`\begin{aligned}F(\alpha)&=\alpha^3-2c_3^3\alpha^2\\&\quad-\frac45\,41c_3^6\log\frac1{\varphi_s(\alpha)}=0.\end{aligned}`}</Math><p>The fixed function has one positive root: <strong>α⁻¹ ≈ 137.035 999 2168.</strong> Mathematical uniqueness, the input provenance and the physical Thomson coupling are distinct statements along this route.</p><Link href="/explain#alpha">Follow every term, the proof and the measurement</Link></>}
      </div>
    </div>
    <p className={styles.scope}>The common invariant data connect the calculations. They do not by themselves derive the full local electromagnetic variation. The guide separates the exact maps, the response contract and the physical readout at the step where each enters.</p>
    {compact ? <Link className={styles.primary} href="/explain">Work through the complete construction <ArrowRight size={18} aria-hidden/></Link> : <div className={styles.sources}><Link href="/documentation?section=section%3A2befc1b3b29d5cae0f23">Original lattice join</Link><Link href="/documentation?section=section%3A6a757c5701557192653a">The same norms in the EM response</Link><a href="#flavor">Continue into the family operators <ArrowDown size={16} aria-hidden/></a></div>}
  </section>;
}
