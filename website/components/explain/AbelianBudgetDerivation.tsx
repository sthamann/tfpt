import Link from "next/link";
import { Math } from "@/components/Math";
import styles from "./ReadoutMechanisms.module.css";

export function AbelianBudgetDerivation(){return <section id="budget" className={`guide-section ${styles.section}`}>
 <h2>Compute the same budget from the charge content.</h2><p className="guide-lead">The charge builder has just summed X² to 120 on one family. With X = 6Y this is Tr Y² = 120/36 = 10/3. Now apply the actual field weights and normalization that produce the abelian index.</p>
 <Math block>{String.raw`\begin{aligned}\operatorname{Tr}_{16}Y^2&=6\!\left(\frac16\right)^2+3\!\left(\frac23\right)^2\\&\quad+3\!\left(\frac13\right)^2+2\!\left(\frac12\right)^2+1\\&=\frac{10}{3}.\end{aligned}`}</Math>
 <div className={styles.actionPath}><div><span>Three Weyl families, weight 2/3 each</span><Math block>{String.raw`\frac23\cdot3\cdot\frac{10}{3}=\frac{20}{3}`}</Math></div><div><span>One complex Higgs doublet, weight 1/3</span><Math block>{String.raw`\frac13\cdot2\left(\frac12\right)^2=\frac16`}</Math></div><div><span>Total hypercharge coefficient</span><Math block>{String.raw`b_Y=\frac{20}{3}+\frac16=\frac{41}{6}`}</Math></div></div>
 <p>The factors 2/3 and 1/3 are the one loop Weyl fermion and complex scalar weights in the specified field theory. The normalization is fixed by the embedding index: on the five slot carrier Tr Y² = 5/6, while Tr T₃² = 1/2, giving kY = 5/3.</p>
 <Math block>{String.raw`\begin{aligned}k_Y&=\frac{5/6}{1/2}=\frac53,\\b_1&=k_Y^{-1}b_Y=\frac35\frac{41}{6}=\frac{41}{10},\\M&=10b_1=40+1=41.\end{aligned}`}</Math>
 <p>The normalized fermion contribution is 4; the Higgs contributes 1/10. In units of 1/10 they become 40 and 1. The family transport calculation independently exposes ΣL = 40 through its actual matrix entries. This is the shared budget used by the specified EM closure.</p>
 <p><strong>Scope of this calculation:</strong> the indicated spectrum, three families, one Higgs doublet and the stated embedding normalization are carried throughout. The charge and coefficient identities are exact there. Using this coefficient in the local physical EM variation is a further specified source identification.</p>
 <div className={styles.sources}><Link href="/documentation?section=section%3A6a757c5701557192653a">Original charge, heat kernel and embedding index derivation</Link><Link href="/documentation?evidence=python_verification%3Averification%2Fv310_carrier_sm_anomaly.py">Explicit spectrum and anomaly checks</Link><a href="#alpha">Carry 41 into the alpha equation</a></div>
 </section>;}
