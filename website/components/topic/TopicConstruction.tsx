import Link from "next/link";
import type { ReactNode } from "react";
import { Math } from "@/components/Math";
import { CliffordOperation, MarkedModes, RootClasses } from "@/components/explain/StartingStructures";
import { ChargeExplorer } from "@/components/explain/InteractiveReadouts";
import styles from "@/components/explain/StartingStructures.module.css";

/** Reuse the original construction readers with the same operations and scope. */
function ConstructionSurface({ children }: { children: ReactNode }) {
  return <div className={`${styles.root} ${styles.embedded} topic-construction`}>
    <div className={styles.workedStep}>{children}</div>
  </div>;
}

export function E8Construction({ part }: { part: "roots" | "spinor" | "charges" }) {
  if (part === "roots") return <ConstructionSurface><RootClasses /></ConstructionSurface>;

  if (part === "spinor") return <ConstructionSurface>
    <h3>Act on a carrier state</h3>
    <p>An exterior state records the occupied slots in their order. Insertion and removal change that state, including its sign. Try an occupied slot twice to see the zero vector, then reset and compare operations in different orders.</p>
    <CliffordOperation />
    <details className={styles.details}>
      <summary>From five operator pairs to the D₅ spin action</summary>
      <p>Write a†ⱼ for insertion and aⱼ for removal. These operations satisfy the canonical anticommutation relations. Their ten gamma combinations give the Clifford action:</p>
      <Math block plain="Insertion and removal obey the exclusion and sign relations of the exterior algebra.">{String.raw`\{a_j,a_k^\dagger\}=\delta_{jk},\qquad\{a_j,a_k\}=\{a_j^\dagger,a_k^\dagger\}=0`}</Math>
      <Math block plain="Five insertion and removal pairs supply ten Clifford gamma operators.">{String.raw`\gamma_{2j-1}=a_j^\dagger+a_j,\qquad\gamma_{2j}=i(a_j^\dagger-a_j),\qquad\{\gamma_a,\gamma_b\}=2\delta_{ab}`}</Math>
      <p>Each gamma flips even and odd degree. The quadratic generators ¼[γₐ, γᵦ] preserve parity and realize the spin action of so(10). The full exterior algebra has dimension 32; its even half S⁺ has dimension 16. This gives the representation action behind the dimension count.</p>
      <p>The operations act in the specified representation. Identifying them with physical fields or a particle preparation retains the original carrier and source assumptions.</p>
      <Link href="/documentation?evidence=python_verification%3Averification%2Fv197_rr_carrier_clifford_d5.py">Read the carrier and Clifford source</Link>
    </details>
  </ConstructionSurface>;

  return <ConstructionSurface>
    <h3>Read the charges of all six sectors</h3>
    <p>Select the occupied colour and weak slots, or choose one of the six sectors. The original reader adds the slot hypercharges and computes the electric charge. Odd selections are identified as the other half spinor.</p>
    <ChargeExplorer />
    <details className={styles.details}>
      <summary>Check the gauge anomalies of the stated Weyl spectrum</summary>
      <p>For the full sixteen component spectrum, the linear and cubic hypercharge traces vanish. The mixed coefficients include the sector multiplicities and the fundamental representation indices:</p>
      <Math block plain="The gravitational hypercharge trace and the cubic hypercharge trace both vanish for this spectrum.">{String.raw`\operatorname{Tr}Y=0,\qquad\operatorname{Tr}Y^3=0`}</Math>
      <Math block plain="The mixed colour and weak hypercharge anomaly coefficients vanish.">{String.raw`\begin{aligned}SU(3)^2U(1):&\quad\frac16-\frac13+\frac16=0,\\SU(2)^2U(1):&\quad\frac14-\frac14=0.\end{aligned}`}</Math>
      <p>These cancellations check the consistency of the specified Weyl charge spectrum. They retain a different scope from constructing the interacting physical fields and their common source.</p>
      <Link href="/documentation?evidence=python_verification%3Averification%2Fv310_carrier_sm_anomaly.py">Inspect the complete anomaly calculation</Link>
    </details>
  </ConstructionSurface>;
}

export function FamilyConstruction() {
  return <ConstructionSurface><MarkedModes /></ConstructionSurface>;
}
