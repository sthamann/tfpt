import Link from "next/link";
import { frozenRegistry, predictionGroups, predictionById, predictionLabel, shortFrozenValue } from "@/lib/frozen-predictions";
import styles from "./TheoryCoverage.module.css";

export function GuidePredictions() {
  return <section id="predictions" className={`guide-section ${styles.coverage}`} aria-labelledby="guide-predictions-title">
    <h2 id="guide-predictions-title">What comes out, and how can we test it?</h2>
    <p className="guide-lead">The construction reaches beyond alpha and mass ratios. The same inputs feed particle mixing, cosmic rotation, ordinary matter and cosmological scales. Each output has a formula, conditions and a way to fail.</p>
    <nav className={styles.actions} aria-label="Prediction reading paths"><Link href="/predictions">Open every registered prediction</Link><Link href="/empirical-audit">Compare with dated measurements</Link><Link href="/interactive/predictions">Follow the animated testing journey</Link></nav>
    <p>The register preserves the values frozen on 9 June 2026: {frozenRegistry.predictions.length} main values, {frozenRegistry.assigned_texture_values.length} assigned textures and {frozenRegistry.conditional_bands.length} conditional inflation bands. Measurements already known at the freeze remain comparisons. The conditions below travel with each physical interpretation.</p>
    <div className={styles.predictionGroups}>{predictionGroups.map(group => <div key={group.id}>
      <h3>{group.title}</h3>
      <p>{group.id === "masses" ? "Source mass ratios need their physical reader, renormalization scale and mass scheme." : group.id === "mixing" ? "Quark and neutrino mixing share the seed and their specified flavour construction." : group.id === "cosmology" ? "These readouts retain the branch, scale and cosmological identification stated in the original source." : "The boundary equation fixes a root; cosmic rotation uses its separate physical readout."}</p>
      <ul>{group.ids.map(id => <li key={id}><Link href={`/predictions#${id}`}><span>{predictionLabel(id)}</span><strong>{shortFrozenValue(predictionById(id))}{id === "BETA_BIREFRINGENCE_DEG" ? "°" : ""}</strong></Link></li>)}</ul>
    </div>)}</div>
    <h3>What is assigned, and what uses an external input?</h3>
    <p>The neutrino CP phase 240° and atmospheric mixing sin² θ₂₃ = 0.5 are assigned textures in this register. The inflation bands use the external reheating range N★ = 50 to 60. Their equations link the two tests: nₛ = 1 − 2/N★ and r = 12/N★², hence r = 3(1 − nₛ)².</p>
    <p>The dated comparison page also shows tensions. The frozen inflation tilt band lies below the cited ACT central value; the cited gravitational wave upper limit still allows the tensor band. Source mass ratios need their transfer before a precision agreement can be stated.</p>
    <nav className={styles.actions} aria-label="Conditions and tests"><Link href="/predictions#assigned">Assigned textures</Link><Link href="/predictions#bands">Inflation bands</Link><Link href="/falsification">Failure criteria for each branch</Link><Link href="/papers">Read the original publication set</Link></nav>
  </section>;
}
