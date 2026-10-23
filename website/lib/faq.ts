/**
 * Hostile-referee FAQ data. Kept in a plain (non-"use client") module so both
 * the client UI component and the server page (for FAQPage JSON-LD) can import
 * the actual array rather than a client reference.
 */
export interface FaqItem {
  q: string;
  /** Plain-text answer (also used to build FAQPage JSON-LD). */
  a: string;
}

export const FAQ_ITEMS: FaqItem[] = [
  {
    q: "What is Topological Fixed-Point Theory (TFPT)?",
    a: "TFPT is a research programme by Stefan Hamann and Alessandro Rizzo connecting two starting assumptions to a discrete mathematical compiler, E₈ lattice structure and Standard Model readouts. Its papers distinguish exact consequences under assumptions, numerical results, conditional physical interpretations and open derivations. The published code and status ledger let readers inspect those distinctions.",
  },
  {
    q: "What does TFPT say about the fine-structure constant?",
    a: "TFPT defines an electromagnetic fixed-point equation whose positive target root is approximately α⁻¹ = 137.03599921684. The root is calculated within the specified equation and compared with experiment. Deriving the equation's physical inputs and identifying its root with the measured Thomson-limit coupling are separate physical questions. The architecture paper and verification suite provide the formulas, assumptions and checks.",
  },
  {
    q: "Is TFPT a completed physical theory of everything?",
    a: "TFPT does not establish a completed physical theory of everything. Its discrete mathematical construction and numerical readouts have explicit assumptions and verification paths. A common local interacting 3+1-dimensional theory, the chiral measure, physical source and state selection, and other interfaces remain separate obligations. The frontier paper and claim ledger record their scope and status.",
  },
  {
    q: "Is this just E₈ unification again?",
    a: "No. In TFPT, E₈ is the unimodular audit / compiler hull that classifies the admissible discrete charge and residue structures — not an unbroken physical gauge group. The Standard Model is a readout after projection, not an E₈ gauge theory. This is exactly why the no-go results against literal E₈ world-formulas (Distler–Garibaldi; Coleman–Mandula) do not apply: they constrain E₈ as a spacetime gauge symmetry, which TFPT does not claim.",
  },
  {
    q: "Where does experimental input enter?",
    a: "Into the comparison rows, not the construction. CODATA-2022, NuFIT 6.0, ACT DR6, Planck and the running/upcoming experiments are how the closed-branch readouts are checked — they are never used as inputs. The closed branch is built only from the two axioms c₃ = 1/(8π) and g_car = 5.",
  },
  {
    q: "What is actually fitted?",
    a: "In the closed branch: nothing. There are zero fitted constants on the dimensionless axis, and parameter-freeness is a theorem under the named gapped-transport hypotheses (Δ = 6 log(3/2) > 0 gives, by Perron–Frobenius, a unique attractor; the physical identification of the transport operator stays [C]). The only continuous primitive left is π. The conditional layer has declared inputs — the e-fold count N★ for inflation (kept as the frozen band [50,60]; the scalaron-reheating chain computes a conditional point N★ = 51.4 [C], recorded with its A_s tension) and one dimensionful induced-gravity scale — which are typed [C]/[O], never smuggled in.",
  },
  {
    q: "Couldn't all the integer coincidences be numerology?",
    a: "The discipline rule is: every load-bearing number must appear in at least one E₈ branching projection, which turns the number stock into a falsifiable raster. Beyond that, every [E] identity, [E] lattice theorem and [E] numerical fixed point is re-derived from the two axioms by an independent Python suite, mirrored on an independent Wolfram path, and recorded in a versioned status ledger. Since v100 the charge is also quantified by an explicit null model: exhaustively enumerating a declared formula grammar (which provably contains every scored TFPT formula) against conservative data windows gives a joint look-elsewhere-corrected probability ≤ 10⁻³⁰·⁷ that a random theory of equal formula complexity reproduces the scorecard — including the α⁻¹ equation, where exactly one of 94 500 complexity-matched variants hits CODATA. Honestly stated: that is a null-model rejection conditional on the declared grammar, not a certificate — and the test has demonstrated power (perturbing φ₀ by 1% collapses the scorecard). Stripped of that grammar an assumption-minimal floor still remains: the same 94 500-variant α⁻¹ census is pure counting, so p ≤ 1/94 500 ≈ 4.40σ with no subjective probability at all (v436), and a monotone concession ladder (30.7 → 25.8 → 4.98 dex) keeps the 'not chance' verdict even at the most adversarial rung — the only honest gap to 5σ is one further independent confirmation.",
  },
  {
    q: "What would kill the theory fastest?",
    a: "Any one of: the α fixed-point equation F_U(1)(α) = 0 failing or admitting a second admissible root; a robust neutron-EDM signal (θ_eff = 0 is structural); the discovery of a second light seam-even Higgs doublet (N_Φ = 1); a robust tensor ratio r ≳ 0.01 (the R² branch carries M_Pl and A_s); a robust w ≠ −1 (the single-engine dark-energy readout); a JUNO solar angle clearly away from 0.307; or any verification script failing to reproduce its claim.",
  },
  {
    q: "What is still open?",
    a: "The live residual is the pair Rest = v_geo ⊕ G_net ⊕ F_transfer (compiler) and Rest_TOE (strict-physical-TOE accounting of the 2026-08-27/28 contract wave: SeamContinuum ⊕ 4DAction ⊕ ChiralMeasure ⊕ MirrorGap ⊕ UnitaryDynamics ⊕ IR/continuum ⊕ BulkSeam ⊕ QuantumGravity ⊕ GeneratingFunctional ⊕ InitialState — every summand a named [O] or standing-rule contract, nothing claimed closed). The 2026-09-05 non-RH Round 4 (v1026–v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8: ||R_N||HS < 2.995906 < 3 for every even N≥16, with the former CF/DG estimates discharged for this bound by native v1026 using v1022/v1025. It also adds narrow T3/T4/T6–T8 identities and counterbounds. FE-GEN/ALG-EXH, every T1–T8 gate and the shared 3+1D parent remain open; v1029 requires global zero-mode removal and is not a TFPT embedding; no TOE marker moved. (1) v_geo: the single dimensionful scale anchor — the quark ratios are closed, only the absolute amplitude remains, and the No-Unit theorem makes it a CLOSED METROLOGY STRUCTURE (R₊ unit torsor; one dimensionful calibration necessary by dimensional analysis — v153/v725; the same unit as gravity's 1/G), over-determined to 0.11% by gravity vs dark energy. It stays the one genuine [O] unit (no physical [E]); its interface is structurally closed as an R₊ scale torsor in calibration form (v725) — one external reference selects the point in the torsor, everything else is prediction; no scale derivation. (2) G_net: the metric-sector inclusion. Its target (E₈)₁ net is closed — net existence and full-cone reflection positivity are discharged to [E] — and the keystone Seam Equivalence Theorem SEAM.EQUIV.01 ('the raw reflection-positive seam state is the holomorphic (E₈)₁ net at τ=i') is now, on its MMST route SEAM.EQUIV.MMST.01, [C] closed modulo cited theorems, not solved (the twistor route SEAM.EQUIV.TWISTOR.01 and the unconditional parent stay [O]): an explicit gapped lattice model (v367/v368) and the S3 closure stack pin the target at every computable level — central charge c = 8 from the lattice (v376), the (E₈)₁ character 248/1 (v377), genus-1 torus GSD = 1 (v378) and reflection positivity (v379), plus the ground-state witnesses: the modular commutator gives c₋ = 8 from entanglement alone (v489) and the spin-structure parity census gives μ_pre = 4 with θ_v = 1 (v490) — and the chain is Lean-pinned (FORM.SEAM.MMST.01, SeamScalingLimit.lean) to the published MMST/Adamo scaling-limit theorems. The only residual is [O] = the abstract continuum scaling-limit existence (v336), a cited published theorem outside the computational suite; its 128-spinor extension leg is certified at net level by the peer-reviewed crossed-product package (v469, Longo–Rehren/Böckenhauer/KLM; AGT/AMT an independent second witness), with the realisation input reduced to invariant level — stays [O]. Its conformal-deck face QGEO.SYM.01 is a corollary (v335). (3) F_transfer: the source→pole/relic/cosmology transport, now a typed RUNNABLE solver suite — Koide source→pole (v371), η_B via the Boltzmann washout (v372), the axion relic (v373) and m_p/m_e via QCD/EW matching (v374), each with a kill test and folded into a status-typed prediction-observatory CI (v375); they stay typed [C] bridges, never compiler powers; both thermal-time routes for internalizing the clocks are machine-killed (v723 STT-KILLED, v724 T3B-DEAD), so the external clock contract is confirmed and sharpened to {one unit (v_geo-class), one angle θᵢ, one lattice O(1) C_p}. Separately, the nonperturbative ambient measure QG.AMB.01 (full quantum gravity) is NOT a second TFPT structural item: the ambient-redundancy theorem (v369) plus the S3 reflection-positivity closure (v379) discharge it as a redundancy — a certification object, not missing dynamics, conditional on SEAM.EQUIV.01 + Bisognano–Wichmann; every readout factors through the gapped admissible spectrum (Δ_eff = 1.648 > 0), so TFPT provably does not need it. Its R²/Weyl² Stelle ghost is a Seeley–DeWitt truncation artefact — perturbative spin-2 graviton unitarity is established [C] (v304/v370/v380), so it is not a non-unitarity hole either. The full sprint-by-sprint reduction that pinned SEAM.EQUIV.01 lives on the /changelog page, not here. The historical labels U_wall / G_metric / F_frontier are kept only for ledger continuity.",
  },
  {
    q: "Why call α⁻¹ a prediction at 1.9σ from CODATA?",
    a: "α⁻¹ = 137.0359992168 is the unique positive root of a parameter-free cubic with proven existence and uniqueness — it is a fixed point, not a fit. The deviation from the CODATA-2022 recommended value is 3.98×10⁻⁸ in α⁻¹, about 1.9σ of that adjustment's uncertainty. It is presented as a numerical fixed point [E], with its kill criterion stated.",
  },
];
