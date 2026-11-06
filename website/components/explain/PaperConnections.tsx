import Link from "next/link";
import { Math } from "@/components/Math";
import styles from "./TheoryCoverage.module.css";

export function BootstrapSelection() {
  return <div className={styles.coverage}>
    <h3>Why this E₈ completion rather than another lattice?</h3>
    <p>The original bootstrap compares rank filling D<sub>g</sub> + A<sub>m</sub> pairs with g + m = 8. An integral glue index requires 4(m + 1) to be a square. In this comparison class, D₈ + A₀ is the alternative with no family factor; D₅ + A₃ is the familyful completion. Its matching glue has index four and norm 5/4 + 3/4 = 2.</p>
    <p>The stronger primitive extension theorem removes fixed rank eight, evenness, unimodularity and minimality as starting assumptions. For the standard positive D<sub>n+1</sub> + A<sub>n−1</sub> pairing, an integral extension of full rank containing a primitive projection to the A discriminant forces n to divide four. For n ≥ 3 this selects n = 4 and the E₈ completion.</p>
    <p>The positive normalization and the actual primitive insertion on one side remain hypotheses. Locality of the doubled object alone does not supply that insertion. The separate metric rigidity theorem assumes unimodularity; the two results cannot establish each other’s premises.</p>
    <nav className={styles.actions} aria-label="E8 selection sources"><Link href="/documentation?section=section%3A7232024bf56aec8e3f3b">Read the stronger selection theorem and its inputs</Link><Link href="/documentation?section=section%3A3238ca6f112057ff7e42">Inspect the original bootstrap comparison</Link><Link href="/interactive/e8">Watch the actual lattice glue</Link></nav>
  </div>;
}

export function HorizonAndFrontier() {
  return <section id="physical-readouts" className={`guide-section ${styles.coverage}`} aria-labelledby="physical-readouts-title">
    <h2 id="physical-readouts-title">From the source to horizons and other observables</h2>
    <p className="guide-lead">The companion papers also work through gravitational identities and physical transfer calculations. Following the extra input at each step makes their connection to the rest of the theory easier to see.</p>
    <h3>Two horizons, one entropy bound</h3>
    <p>A Schwarzschild–de Sitter black hole has a black hole horizon and a cosmological horizon. At their Nariai merger, the dimensionless horizon cubic factors into (t − 1)²(t + 2). Each horizon carries one third of the empty de Sitter entropy. Together they carry two thirds.</p>
    <Math block>{String.raw`\begin{aligned}\frac{S_{\mathrm{total}}}{S_{\mathrm{dS}}}&=\frac{x^2+1}{x^2+x+1},\\x&=\frac{r_b}{r_c},\\3(x^2+1)&-2(x^2+x+1)\\&=(x-1)^2\ge0,\\S_{\mathrm{total}}&\ge\frac23 S_{\mathrm{dS}}.\end{aligned}`}</Math>
    <p>These are classical general relativity identities in the stated Schwarzschild–de Sitter family. Their alignment with the TFPT anchor is a structural comparison; identifying the horizons with a physical seam is conditional. This is a geometry connection rather than an additional measurement test.</p>
    <p><Link href="/documentation?section=section%3Afda00a19dcba44348ac3">Read the horizon derivation and physical scope</Link></p>
    <h3>Four concrete transfer calculations</h3>
    <ol className={styles.route}>
      <li><h3>Lepton relation to pole masses</h3><div><p>Apply a physical mass transfer to the source relation. In the paper’s stated test, standard QED running alone shifts the Koide quotient in the wrong direction. That negative result concerns this transfer attempt.</p></div></li>
      <li><h3>Matter asymmetry</h3><div><p>The Boltzmann evolution uses the specified heavy neutrino mass and decay inputs to calculate the baryon asymmetry. Separately, converting Ωb into a baryon to photon ratio adds the Hubble input h. A downstream conversion is not an independent prediction.</p></div></li>
      <li><h3>Axion relic abundance</h3><div><p>The finite temperature evolution uses an initial angle in the inflationary branch. A scenario after inflation instead uses a horizon average and its domain wall assumption. These are distinct physical branches.</p></div></li>
      <li><h3>Proton to electron mass ratio</h3><div><p>The QCD transfer uses the declared external strong coupling and proton coefficient. The reported propagated band is ±7.5%. It is a conditional comparison, rather than an extra parameter free compiler number.</p></div></li>
    </ol>
    <nav className={styles.actions} aria-label="Physical transfer sources"><Link href="/documentation?section=section%3Aa5afdfe2d50d9975d56b">Inspect the four original transfer calculations</Link><Link href="/documentation?section=section%3A84d26a09031108cede24">Follow Ωb into the baryon to photon ratio</Link><Link href="/predictions">See which values belong to the frozen register</Link></nav>
  </section>;
}
