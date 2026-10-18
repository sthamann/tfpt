# Axioms, origin and bootstrap — part 4

[Topic entry](../foundations.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Reflection Positivity and OS Reconstruction

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:131-136](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L131) · `section:eaf0d1935b534e4f5b24` · section

The reflection-positivity block should state all assumptions on the admissible Schwinger functions, fermionic positivity, quotient form, and domain regularity. The OS theorem is used as a standard interface only after the admissible-sector positivity hypotheses are named.

## Local Net and Scattering

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:137-142](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L137) · `section:e075f49e180aeaf4a160` · section

The local Minkowski net, Haag–Ruelle/LSZ massive scattering, and dressed massless interface are treated as conditional closure outputs. The paper must distinguish stable massive scattering from low-curvature dressed massless behavior.

## Exact Admissible Flow

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:143-154](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L143) · `section:20de188616827cd1449d` · section

The exact admissible RG flow is the analytic continuation of the same sector: [formula in source] with the admissible projection included as part of the flow definition. The observable hierarchy is included only as far as it supports the QFT closure layer.

## Main Technical Development

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:155-190](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L155) · `section:ef55cca101554d90da06` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

Explicit source references:

- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)

## Source Extraction Map

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:191-209](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L191) · `section:dc2548243d0e4165fe45` · section

Use : Sections 7.4 and 7.5 for hadronic admissibility and strong-CP ingredients. Section 8 as the main technical body, with carrier repetition removed. Sections 8.20–8.22 for topological positivity and strong-CP closure. Sections 8.23–8.41 for reflection positivity, OS closure, local net, and scattering. Section 13.2 for exact admissible RG flow, 1PI expansion, and observable hierarchy. Appendices E, F, and H as the 

## Not Used Here

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:210-216](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L210) · `section:228132cd22c2701bbf15` · section

Exact electromagnetic benchmark derivations, CKM/PMNS prediction tables, gravity/metrology readouts, CMB spectra, sky realization, E8 grammar, full empirical ledgers, horizons, and transient channels are not used as proof inputs in this paper.

## Lemma A (Seam Determinant).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:16-38](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L16) · `section:79cfcc11c471d5bbf49d` · paragraph

Proof skeleton. Read the determinant as a primitive admissible zeta determinant. The admissible trace [formula in source] admits a primitive-orbit decomposition; closed-branch selection plus [formula in source] plus [formula in source] leaves only the minimal seam class with multiplicity 2 (double sheet), area [formula in source] (primitive seam norm), and action [formula in source] (two oriented EM runs). The non-pr

## Lemma B (Curvature Residue).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:39-60](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L39) · `section:dfcd021c432501a11821` · paragraph

Proof skeleton. Read [formula in source] as the inverse of the admissible curvature susceptibility [formula in source] in a constant-curvature family. The exponential is then a non-perturbative inverse-susceptibility effect, not a heat-kernel monomial.\\ Critical hook. Prove [formula in source] from the admissible path-integral structure.\\ Consequence. [formula in source] and the Starobinsky potential [formula in so

## Lemma C (Thermal Transport).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:61-89](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L61) · `section:c1704f9d83f0690b188c` · paragraph

Four sub-claims, jointly: Proof skeletons. [formula in source] is a 4D radiation-density seam residue; [formula in source] is the QKE transport trace [formula in source] with three carrier families plus [formula in source] (weak-seam Ward) plus [formula in source] (EM holonomy); [formula in source] is the freeze-out occupancy [formula in source] with [formula in source] ; [formula in source] is the admissible line in

## Lemma D (Matter Occupancy).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:90-111](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L90) · `section:87fc2b82b48a483e0d88` · paragraph

Proof skeleton. [formula in source] is the antisymmetric two-form occupancy on [formula in source] ( [formula in source] since [formula in source] ); [formula in source] is the trace of the stable-neutral admissible projector times [formula in source] (quadratic seed intensity) and the flavour leakage [formula in source] ; [formula in source] is the Takagi trace of an admissible Majorana operator decomposed into orth

## Lemma E (Branch Phase Selection).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:112-137](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L112) · `section:6322f7e4c6b01cc9fa93` · paragraph

where [formula in source] is the admissible primordial-curvature Hessian, [formula in source] is the primitive seam branch state with winding class [formula in source] , [formula in source] is the Calderon sheet involution (which enforces the reality constraint [formula in source] ), [formula in source] is the observer embedding (worldline + tetrad + orientation + last-scattering light cone), and [formula in source] 

## The TFPT primitives ledger and audit table

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:196-234](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L196) · `section:8301f1c88a5e5c8d3bef` · section

@lll@ Symbol & Formula / origin & Numeric value \\ [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & primitive seam winding class & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] rad \\ [formula in source] &

## Mode E. Lemma-E branch phase selection (NEW in v4.6).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:26-35](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L26) · `section:8a13516d3c7282e5381d` · paragraph

The phases [formula in source] are constructed from [formula in source] via the canonical joint diagonalisation of the admissible primordial-curvature Hessian [formula in source] , with the spectral flag breaking degeneracies and the seam convention fixing the residual U(1). No Planck phase enters; no SMICA [formula in source] enters. See construction and acceptance results.

## The Branch Operator Bundle

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:86-101](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L86) · `section:3cb85a1e3fb938d68d5d` · subsection

The minimal native structure of Mode E (Stefan v4.6 brief 11) is i.e.\ the admissible Hilbert space, the primordial-curvature Hessian, the primitive seam state, the Calderon involution, and the observer. Implementation: tfpt_cmb.branch_phase_selection.BranchOperatorBundle plus ObserverEmbedding.

## Contract specification

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:293-336](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L293) · `section:ba4d7ea88722968045bc` · subsection

Sprint 2A Branch Extraction Contract\\ Input. closed TFPT branch operators.\\ Output. [formula in source] \,( npz), [formula in source] \,( npz), [formula in source] \,( npz), spectral_flag\,( json+ npz), observer_embedding\,( json), [formula in source] -grid\,( npz), direction grid\,( npz), shell-power validation\,( json), branch origin\,( json).\\ Hard checks. (1) [formula in source] Hermitian; (2) [formula in sour

## BT1 (closes A.h1).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:227-233](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L227) · `section:6c98d3366398750777cf` · paragraph

TFPT defines the physical vacuum-density determinant as the primitive admissible zeta determinant. Non-primitive admissible repetitions are not physical TFPT vacuum classes. This is a clean physical choice (the same role as the Selberg primitive-orbit decomposition on closed Riemannian manifolds), not a trick.

## BT5 (closes C4.h1, with sub-theorems C4a, C4b, C4c).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:256-277](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L256) · `section:0397745bedb9c017bcf7` · paragraph

This is Stefan's main astrophysical achievement. Three sub-theorems combined collapse the line integral to two retained-state expectation values: C4a (Press-Schechter Source): [formula in source] with [formula in source] from [formula in source] (Lemma D2). C4b (Carrier IMF Photon Yield): [formula in source] . C4c (Admissible UV Escape): [formula in source] . The non-trivial content is not the integral arithmetic — t

## The 12 G1 files

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:50-73](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L50) · `section:046a88b0c9e3eb83133c` · subsection

ll File & Purpose \\ branch_metadata.json & metadata, must declare [formula in source] \\ B_sigma_adm.npz & boundary Dirac/seam operator \\ P_adm.npz & admissible projector [formula in source] \\ P_C.npz & Calderon polarisation projector \\ iota_C_adm.npz & Calderon sheet involution \\ Delta_prim_adm.npz & primitive Laplacian \\ Q_top_adm.npz & topological phase generator \\ K_zeta_adm.npz & primordial-curvature Hess

## Roadmap to a finished v5.0

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:215-247](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L215) · `section:9400f87be0e5ce310646` · section

The five outstanding theorem-level closures are Lemma A (Seam Determinant): rigorous definition of [formula in source] and proof that non-primitive admissible repetitions vanish. Lemma B (Curvature Residue): proof of [formula in source] from the admissible curvature path-integral. Lemma C: subdivide into C1–C4; C4 ( [formula in source] ) is the weakest link — needs SFR/ [formula in source] / [formula in source] to co

## Lemma A.h1 (medium).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:33-46](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L33) · `section:3e04e51ccb89918e62d8` · paragraph

Hook. TFPT must canonically identify [formula in source] , or prove that non-primitive admissible repetitions vanish.\\ Proposed solution. Adopt the primitive zeta determinant convention. The non-primitive contributions are bounded by [formula in source] in Planck units, 240 orders below any physical observable. The convention is mathematically consistent with Selberg-type primitive-orbit decompositions: the regulari

## Lemma B.h1 (hard).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:47-62](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L47) · `section:a95e9e8c90c77d844a96` · paragraph

Hook. Prove [formula in source] from the admissible curvature path integral.\\ Proposed solution. The exponential is the signature of a non-perturbative instanton-class contribution. The admissible curvature path integral admits a tunneling configuration with Euclidean action [formula in source] . Saddle-point evaluation gives [formula in source] with [formula in source] the zero-mode normalisation. Structurally anal

## Lemma C1.h1 (easy).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:63-72](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L63) · `section:562c665f3c970df11108` · paragraph

Hook. Show that the dimensionless TFPT trace [formula in source] maps onto [formula in source] .\\ Proposed solution. The Stefan-Boltzmann inversion closes the loop in Planck units: [formula in source] with [formula in source] . Setting [formula in source] fixes [formula in source] . The acceptance criterion is a Paper-5 metrology theorem identifying [formula in source] with the Stefan-Boltzmann limit of the admissib

## Lemma C2.h1 (hard).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:73-88](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L73) · `section:660464d1fe573fcf997a` · paragraph

Hook. Prove [formula in source] and [formula in source] from the explicit neutrino QKE.\\ Proposed solution. Both identities follow from the standard QKE [formula in source] with [formula in source] on the admissible neutrino subsector. The weak Hamiltonian couples through the primitive seam, so [formula in source] with the dimensionless seam Ward residue identified with [formula in source] . The EM identity is struc

## Lemma C4.h1 (hardest).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:103-116](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L103) · `section:041da2a709c47b380708` · paragraph

Hook. Prove that the line integral of the admissible reionization transport collapses to [formula in source] without astrophysical fitting.\\ Proposed solution. C4 is the weakest sub-claim. The plausible path: derive [formula in source] from Press-Schechter with [formula in source] from D2; [formula in source] from the carrier-derived stellar IMF; [formula in source] from the admissible UV residue; substitute and ver

## Lemma D2.h1 (medium).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:129-140](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L129) · `section:30f56d3e8cec86968141` · paragraph

Hook. Prove that the stable neutral admissible sector is complete.\\ Proposed solution. Spectral completeness of [formula in source] follows from Paper 2's carrier classification combined with Paper 4's admissibility constraints. Strategy: enumerate every stable neutral spin-0/1/2 mode, verify [formula in source] , verify the [formula in source] leakage from [formula in source] . Acceptance: a Paper-2 corollary stati

## Lemma E1.h1 (medium).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:156-166](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L156) · `section:9b453a5d07c5cca10999` · paragraph

Hook. Sprint 2A boundary extraction.\\ Proposed solution. Sprint 2A must supply (i) the boundary Dirac [formula in source] (Paper 1 export), (ii) the admissible projector [formula in source] (Paper 4 selectors), (iii) the second functional derivative of [formula in source] at the cosmological vacuum, (iv) the projection. Acceptance: the Sprint-2A contract validator passes K_zeta_adm_hermitian on a real bundle with [f

## Lemma E2.h1 (hardest).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:167-184](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L167) · `section:489cf8b41b3197563b9a` · paragraph

Hook. Prove that the six flag operators [formula in source] pairwise commute on [formula in source] .\\ Proposed solution. Commutativity is a structural consequence of admissibility: (a) [formula in source] because the action is sheet-symmetric; (b) [formula in source] because both live on the boundary modes; (c) [formula in source] because [formula in source] is the closure of the carrier kinetic energy on which [fo

## A.h1 \,—\, Seam Determinant \,( closed_pending_convention_adoption)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:250-270](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L250) · `section:052f57fe3f4412c82339` · subsection

Proof. Define the primitive admissible zeta determinant by [formula in source] . The primitive orbit formula on the closed seam geometry is [formula in source] . Closed-branch selection plus [formula in source] plus [formula in source] leaves only the minimal primitive seam class with [formula in source] (double sheet), [formula in source] (primitive seam norm), [formula in source] (two oriented EM runs). Hence [form

## B.h1 \,—\, Curvature Residue \,( closed_pending_curvature_instanton_theorem)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:271-290](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L271) · `section:18a71b746fc4e4073a05` · subsection

Proof. [formula in source] . TFPT defines the non-perturbative admissible curvature susceptibility as the saddle-point quantity [formula in source] with [formula in source] (retained-seed barrier) and [formula in source] (zero-mode norm). Inverting: [formula in source] . Then [formula in source] and the Starobinsky potential closes the inflation cascade. Curvature Instanton Theorem: [formula in source] has a unique r

## C4.h1 \,—\, Reionization Optical Depth \,( open_hardest_no_full_discharge)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:335-356](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L335) · `section:65e2cf1dd148933e18b2` · subsection

Proof skeleton. [formula in source] . Full discharge requires three sub-theorems: C4a Press-Schechter Source Theorem [formula in source] ; C4b Carrier IMF Photon Yield [formula in source] ; C4c Admissible UV Escape [formula in source] . Honest verdict (Stefan v4.6.6): not in reach without substantial additional TFPT structure; expect a separate dedicated TFPT companion paper.

## Big picture: what TFPT actually claims

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex:1-237](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex#L1) · `section:ecc6fa18b84127d2053b` · section

TFPT is presented here as a boundary-polarized closed theory of admissible vacua on the oriented double cover. The formal theorem stack now starts from a thinner operational seed which functorially induces the one-sided boundary datum, and the manuscript also shows that within the induced boundary class no extra primitive discrete datum is needed. On the one-sided branch, the self-adjoint boundary operator [formula i

## Canonical rigid object

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex:240-321](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex#L240) · `section:73e0b792da8201a1d9ae` · subsection

Collecting the operational-seed generation theorem, the minimal-packaging theorem for the induced boundary class, the boundary datum, the boundary primitive kernel, the joint discrete admissibility theorem, the derived selector, and the continuous closure theorems of sec:closure-theorems, the main-text reconstruction now takes the rigid two-stage form Here [formula in source] is the canonical rigid object of thm:no-a

## Canonical rigid-object corollary

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex:322-348](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex#L322) · `section:26972d57f1c0a2333f48` · subsection

By thm:intrinsic-closed-branch,thm:canonical-rigid-reconstruction-essential-injective,thm:spectral-completeness-rigid-tfpt, there exists a canonical rigid object [formula in source] in [formula in source] such that [formula in source] and every rigid closed admissible realization is uniquely unitarily equivalent to [formula in source] .

## Primitive relative spectral dynamics

[documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/001-section-primitive-core-and-carrier-interface-handoff.tex:58-377](../../../../documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/001-section-primitive-core-and-carrier-interface-handoff.tex#L58) · `section:5453d74e18aa1a63bd2d` · subsection

The carrier theorem is not intended to float above an unspecified microscopic dynamics. The starting point is therefore the one-sided boundary datum from which the primitive layer, the derived closed datum, and the canonical admissibility projector are reconstructed before the later closure theorems are invoked.

## Intrinsic closed branch and canonical rigid object

[documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex:87-99](../../../../documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex#L87) · `section:0984253c39775ef719af` · section

The closed branch is not selected by a comparison functional. At the top of the main-text theorem stack now stands a thinner operational seed layer: quasilocal Euclidean dynamics, reflection positivity, finite relative action, a nontrivial seam class, and one elliptic collar generator. That seed induces the one-sided admissible boundary datum. Once the induced datum is fixed, the remaining closure problem splits into

## Operational seed and boundary generation

[documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex:100-249](../../../../documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex#L100) · `section:da5a8d451e469c6cb1f5` · subsection

Let [formula in source] denote the category whose objects are tuples [formula in source] satisfying: [formula in source] is a quasilocal Euclidean observable net with positive-time reflection [formula in source] ; [formula in source] is reflection positive and clustering on the admissible local algebra, with finite relative action with respect to the declared reference sector; [formula in source] is a nontrivial seam

## Initial admissible bordisms and induced boundary data

[documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex:250-334](../../../../documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex#L250) · `section:7f54fc651a1d27f17cf0` · subsection

Let [formula in source] denote the category whose objects are tuples such that: [formula in source] is an elliptic Dirac-type operator on a one-sided collar with reflection-regular boundary behavior; the retained Euclidean sector is reflection positive; the relative action with respect to the declared reference sector is finite; the seam class is nontrivial, equivalently [formula in source] . Morphisms are unitary in

## Primitive completion from the boundary kernel

[documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex:335-358](../../../../documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/002-section-intrinsic-closed-branch-and-canonical-rigid-obje.tex#L335) · `section:db88205106dc439012fb` · subsection

Let [formula in source] be the boundary primitive kernel attached to an admissible one-sided boundary datum. Here [formula in source] are fixed by the primitive seam generator theorem. No carrier split, no hypercharge operator, no family geometry, no determinant class, no transport pole, no effective strong angle, and no vacuum datum are part of this definition.

## Layered datum and admissibility

[documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/003-subsection-relative-objects.tex:26-97](../../../../documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/003-subsection-relative-objects.tex#L26) · `section:49cc0c56c1033eba5582` · subsection

The technical bookkeeping behind the manuscript uses five levels: [formula in source] [formula in source] [formula in source] [formula in source] [formula in source] Here [formula in source] is the primitive boundary kernel, while [formula in source] is the derived theorem-level post-carrier kernel reconstructed from the joint discrete datum and the full selector.

## Occupancy and boundary-to-bulk bridge

[documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/006-subsection-family-monodromy-and-occupancy.tex:239-260](../../../../documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/006-subsection-family-monodromy-and-occupancy.tex#L239) · `section:e18972a3bc46d3501db8` · subsection

With the family bridge installed, the matter space becomes [formula in source] and the occupancy [formula in source] is already fixed by the harmonic family-mode theorem and its bridge corollary. Here occupancy means the admissible chiral-state count after family lifting; it is not used as a primitive datum. The bridge point is not that family lifting creates a new numerical surcharge. Rather, the inherited hard kern

## From bridge to geometric completion

[documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/006-subsection-family-monodromy-and-occupancy.tex:261-285](../../../../documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/006-subsection-family-monodromy-and-occupancy.tex#L261) · `section:664c3e0c0e3f89f47742` · subsection

Once the carrier packet and family closure architecture are fixed, the focused main-text closure problem splits into a geometric program [formula in source] and a transport program [formula in source] . Record algebra and prediction semantics are now tied directly to the admissible gap in the main theorem stack, while E [formula in source] scale grammar and horizon extrapolations are deferred to appendix-level contin

## Front matter / support

[documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/008-source.tex:1-399](../../../../documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/008-source.tex#L1) · `section:1df7697213ae2bf024ea` · frontmatter

By definition, [formula in source] The denominator is a fixed positive normalizing constant, so the sign is determined entirely by the admissible numerator.

## Front matter / support

[documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/009-source.tex:1-377](../../../../documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/009-source.tex#L1) · `section:c31408dd658bc23e8254` · frontmatter

Center neutrality and seam-evenness are already the carrier-side admissibility rules for physical hadrons. Passing to the norm closure of the singlet admissible algebra acting on the vacuum gives the completed hadronic space, and no state with [formula in source] survives the selector.

## Front matter / support

[documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/010-partial-alpha-gamma-u-1-alpha-0.tex:1-232](../../../../documents/archive--tfpt-45--source_extracts--02_carrier_source/sections/010-partial-alpha-gamma-u-1-alpha-0.tex#L1) · `section:3f13c487d11f26bd5860` · frontmatter

On the retained admissible branch, the projected modular free energy factorizes as [formula in source] Its admissible critical points are therefore exactly the solutions of [formula in source] Equivalently, the continuous closure laws are [formula in source] In particular the continuous closure equations are derived from one primitive variational object rather than imposed as independent sector primitives. Equivalent

## Kernel output package

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/001-section-kernel-numerics-and-electromagnetic-closure.tex:339-387](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/001-section-kernel-numerics-and-electromagnetic-closure.tex#L339) · `section:c4e8bc1ef2f1d0603199` · subsection

The benchmark row for [formula in source] is defined by the positive self-consistent root of eq:carrier-cfe, not by freezing the opening at its retained seed value. On the canonical branch that positive root remains [formula in source] For the remaining one-seed relations we keep the retained branch opening The two symbols belong to the same admissible branch but play different jobs. The electromagnetic [formula in s

## Closure architecture B: Yukawas, masses, flavor, hadronic admissibility, and the strong-CP sector

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/002-subsection-uv-seed-shadow-identities-and-the-cabibbo-inv.tex:329-336](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/002-subsection-uv-seed-shadow-identities-and-the-cabibbo-inv.tex#L329) · `section:6762cc666122ac246c2e` · section

The second closure-architecture block is the transport closure. Its role is to turn the carrier packet and the family/occupancy closure into actual masses, mixings, hadronic admissibility, and control of the strong-CP sector. The logic is again staged: first the discrete phase operator and the transport kernel, then residue and winding data, then matrix-factorized Yukawas, hadronic selection, determinant-line phase e

## Discrete phase operator and transport grammar

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/003-subsection-discrete-phase-operator-and-transport-grammar.tex:1-87](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/003-subsection-discrete-phase-operator-and-transport-grammar.tex#L1) · `section:184f2763f7510774968c` · subsection

Let [formula in source] This makes the phase grammar concrete rather than rhetorical. The six admissible phases are shown as a finite hexagonal transport geometry in fig:z6-circle: the cusp values live on the same real axis as the positive-real phase, the admissible gap is visible directly, and the holonomy phase can be read as a triangle on the same discrete transport base.

## Regularized Yukawa kernels and path-length masses

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/003-subsection-discrete-phase-operator-and-transport-grammar.tex:88-352](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/003-subsection-discrete-phase-operator-and-transport-grammar.tex#L88) · `section:4f28881002e138056680` · subsection

For each fermion sector define the structural positive transport kernel by [formula in source] whenever the inverse exists on [formula in source] . The final admissible kernel is the restriction of this operator to the gap-stable branch selected below. The transport pole [formula in source] is fixed by the structural stationarity of the exact determinant functional [formula in source] with [formula in source] On the 

## Front matter / support

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/005-source.tex:1-373](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/005-source.tex#L1) · `section:cf4f9a06e2fb09990c7e` · frontmatter

Because [formula in source] has eigenphases [formula in source] , the regularized transport spectrum is for the eigenvalues [formula in source] of [formula in source] . In particular, On the admissible cusp set [formula in source] the smallest singular value of the unregulated hexagon denominator is attained at [formula in source] and [formula in source] . Equivalently, [formula in source] Hence the finite admissible

## CKM and PMNS closure

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/007-subsection-ckm-and-pmns-closure.tex:1-105](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/007-subsection-ckm-and-pmns-closure.tex#L1) · `section:adeb4d9c05c9bbb7d89b` · subsection

On the canonical admissible branch the quark mixing matrix [formula in source] is a branch invariant fixed by the hard holonomy form of thm:exact-transport-closure. Its leading transport magnitudes are Its exact CP phase is [formula in source] on the canonical branch.

## Front matter / support

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/001-subsection-hadronic-admissibility-as-singlet-selection.tex:1-4](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/001-subsection-hadronic-admissibility-as-singlet-selection.tex#L1) · `section:306851babdac39e18091` · frontmatter

No opening prose excerpt; see the source.

## Hadronic admissibility as singlet selection

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/001-subsection-hadronic-admissibility-as-singlet-selection.tex:5-48](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/001-subsection-hadronic-admissibility-as-singlet-selection.tex#L5) · `section:3fcf3866d66b7ac20561` · subsection

For each carrier word [formula in source] , let [formula in source] be its color-center charge and let [formula in source] be its seam parity. Physical hadronic words satisfy [formula in source]

## Transport-side ingredients for the strong-CP sector

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/001-subsection-hadronic-admissibility-as-singlet-selection.tex:49-207](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/001-subsection-hadronic-admissibility-as-singlet-selection.tex#L49) · `section:2d503279c58503122138` · subsection

Define Define the admissible sheet-CP operator by [formula in source]

## Closure theorems from the admissibility complex

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/002-section-closure-theorems-from-the-admissibility-complex.tex:1-397](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/002-section-closure-theorems-from-the-admissibility-complex.tex#L1) · `section:dfd6ad94d3380e6b33e4` · section

The preceding two sections introduced the carrier-compatible geometric and transport architecture. The primitive admissibility projector [formula in source] was already placed in the primitive section so that the proof direction runs from the boundary datum through the derived closed datum to [formula in source] , and only then to the later sector theorems. What remains in this section is therefore (i) the upgrade of

## Front matter / support

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/004-source.tex:1-381](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/004-source.tex#L1) · `section:5248af93a50c00dd9d94` · frontmatter

thm:sheet-cp-protection gives [formula in source] By lem:topological-sector-positivity, the admissible partition function admits a sector decomposition [formula in source] The antiunitary sheet symmetry of thm:sheet-cp-protection gives [formula in source] so the sector weights satisfy [formula in source] . Hence [formula in source] By lem:nontrivial-topological-support, one has [formula in source] . Therefore for eve

## Front matter / support

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex:1-122](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex#L1) · `section:7a7755c65bfd436c721b` · frontmatter

eta=0] Fix finite volume [formula in source] and let [formula in source] be the primitive blocked admissible transfer operator with Perron vector [formula in source] . Let [formula in source] be the blocked admissible parent Hamiltonian of lem:parent-gap-from-transfer-block, with [formula in source] Let the physical admissible Hamiltonian be written as [formula in source] where each added term is positive semidefinit

## Admissible Schwinger functions, Minkowski locality, and scattering closure

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex:123-403](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex#L123) · `section:58b3a771f93680088d7d` · subsection

Let [formula in source] denote a low-curvature branch region on which [formula in source] and [formula in source] All scattering statements below are formulated on [formula in source] .

## Weakened ambient class

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/006-section-internal-reduction-theorem-and-renormalized-obse.tex:11-399](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/006-section-internal-reduction-theorem-and-renormalized-obse.tex#L11) · `section:4cc52509e02e7fb2728e` · subsection

Let [formula in source] denote the category whose objects are tuples [formula in source] satisfying the following ambient admissibility axioms: Real even boundary datum: [formula in source] is an admissible real even one-sided boundary datum with reflection-regular collar. Quasilocal positive dynamics: [formula in source] is a quasilocal dynamics with reflection positivity and an admissible vacuum sector. Morphisms a

## Renormalized, physical, and scheme readout layers

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/007-subsection-renormalized-physical-and-scheme-readout-laye.tex:1-372](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/007-subsection-renormalized-physical-and-scheme-readout-laye.tex#L1) · `section:3e7cfda7c9252d871993` · subsection

Let [formula in source] be an admissible infrared regulator commuting with the structural sector selection. Define [formula in source] and set [formula in source] The renormalized admissible effective action is [formula in source]

## Front matter / support

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:1-139](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L1) · `section:84c76a3dafcdc2baa222` · frontmatter

0.96 ! (hadm) at (-5.0,0.9) [formula in source] \ sector; (wk) at (-1.6,0.9) [formula in source] \ generator; (gk) at (1.8,0.9) [formula in source] \ admissible flow; (gren) at (5.2,0.9) [formula in source] \ 1PI action;

## Normalized quotient form

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:143-152](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L143) · `section:9ba4825482f7ea3785d0` · subsection

The relative Euclidean theory used in the main closure section is not interpreted as a difference of measures. Instead it is organized as the normalized quotient [formula in source] Because the denominator is source independent on the admissible sector, the reference theory acts only as a fixed normalizer and does not interfere with reflection positivity.

## Bosonic and fermionic positivity on [formula in source] Padm

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:153-170](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L153) · `section:adc712862a1f13cf0214` · subsection

The commutation relations [formula in source] ensure that reflection preserves the admissible subspace. The bosonic part then follows the standard Markov / reflection-stable Osterwalder–Schrader argument on admissible observables. For fermions, the admissible CAR kernel may be written as a reflected quadratic form; equivalently one may express the same condition as positivity of the associated Pfaffian structure on t

## Admissible OS reconstruction and asymptotic scattering

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:171-178](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L171) · `section:19059df087b765a037b9` · section

This appendix upgrades the admissible Schwinger, reconstruction, and scattering block from a named standard interface to a manuscript-level proof package. The point is not to replace standard machinery by ad hoc notation, but to verify explicitly that the admissible branch satisfies the relevant hypotheses on [formula in source] .

## Tempered admissible Schwinger families

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:179-214](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L179) · `section:b504056fec0c4bab8ecc` · subsection

On the Euclidean continuation of [formula in source] , each truncated admissible Schwinger distribution [formula in source] defines a tempered distribution. Moreover, for every compact [formula in source] and every source monomial of total degree [formula in source] , its moments obey polynomial bounds determined by the same uniform heat-kernel estimates and finite local moments of the admissible constructive measure

## OS and CAR reconstruction on [formula in source] Padm

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:215-255](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L215) · `section:591993c8c68b37136f0d` · subsection

Padm] Let [formula in source] be the admissible Schwinger family on the Euclidean continuation of [formula in source] . If reflection positivity, temperedness, graded Euclidean covariance, graded symmetry, and clustering hold on [formula in source] , then there exist: a Hilbert space [formula in source] with vacuum vector [formula in source] , a strongly continuous positive-energy semigroup [formula in source] with s

## Stable massive Haag–Ruelle and LSZ closure

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:256-300](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L256) · `section:cfa56a2cdb98159c5599` · subsection

Let [formula in source] have an isolated simple pole with positive residue at [formula in source] . Then the corresponding one-particle contribution defines a positive spectral projector on the admissible Hilbert space.

## Dressed massless interface in the low-curvature region

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:301-317](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L301) · `section:3125dafc2086f760e4b4` · subsection

The massless sector is not treated by bare Fock asymptotics in the present manuscript. The relevant object is the infrared-dressed interface package [formula in source] constructed from the soft charges of the admissible local net on the low-curvature region [formula in source] . This is exactly the interface package used in the main-text theorem thm:dressed-massless-interface.

## Yukawa kernels and positivity lemmas

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:318-355](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L318) · `section:3af6d0fa08cdf2b14930` · section

This appendix is the proof motor for the transport positivity, determinant-phase suppression, and bounded-residual statements used in the main text. The transport program is based on the regularized kernel [formula in source] Three remarks are important. The regulator [formula in source] is not optional: without it the kernel becomes ill-defined exactly where the admissibility question is most delicate. Positivity of

## Optional strong-coupling sharpening

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:356-371](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L356) · `section:1073412fc5b9eaeb4588` · subsection

As an appendix-level dynamical sharpening of the hadronic admissibility theorem, one may further require the admissible center-neutral Wilson functional to obey strong-coupling dominance. On that optional route the relative Wilson loop satisfies [formula in source] and the physical Hilbert space contains no color-nonsinglet asymptotic states. This statement is kept in the appendix so that the main theorem surface doe

## From bridge to geometric completion

[documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/001-subsection-from-bridge-to-geometric-completion.tex:5-29](../../../../documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/001-subsection-from-bridge-to-geometric-completion.tex#L5) · `section:a880f6c4757fad6fc643` · subsection

Once the carrier packet and family closure architecture are fixed, the focused main-text closure problem splits into a geometric program [formula in source] and a transport program [formula in source] . Record algebra and prediction semantics are now tied directly to the admissible gap in the main theorem stack, while E [formula in source] scale grammar and horizon extrapolations are deferred to appendix-level contin

## Native charged-current hard matching and the charged seam projector

[documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/003-subsection-native-charged-current-hard-matching-and-the-.tex:72-400](../../../../documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/003-subsection-native-charged-current-hard-matching-and-the-.tex#L72) · `section:9493c97c6a95a3400b9b` · subsection

Let [formula in source] be the primitive seam normalization constant and let [formula in source] be the admissible transport pole of thm:algebraic-transport-pole. The charged two-loop electroweak seam projector is Equivalently, using the canonical occupancy bridge [formula in source] , [formula in source]

## Stationary spectral Planck root

[documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/005-section-absolute-dimensionless-metrology-from-the-bounda.tex:309-381](../../../../documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/005-section-absolute-dimensionless-metrology-from-the-bounda.tex#L309) · `section:64dcd40c0d2e38840998` · subsection

By thm:absolute-spectral-planck-closure, the admissible geometric branch carries the unique positive stationary root [formula in source] [formula in source] This root is the boundary-normalized Planck datum of the stationary branch.

## Infrared seam and sector bifurcation

[documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/006-subsection-infrared-seam-and-sector-bifurcation.tex:1-56](../../../../documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/006-subsection-infrared-seam-and-sector-bifurcation.tex#L1) · `section:f439b413f52df6383104` · subsection

The primitive response [formula in source] bifurcates on the closed branch into distinct dressed spectral channels: [formula in source] Here [formula in source] is the stationary Einstein/Higgs background scale, while [formula in source] is the transport-dressed hadronic scale. They share one boundary origin but are not identified on the closed theorem surface.

## [P] Pole masses, Higgs readout, and full flavor output

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex:31-112](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex#L31) · `section:71582daab73a540e5b13` · subsection

Let [formula in source] and let [formula in source] denote the renormalized admissible flow. For every mass-independent renormalization scheme [formula in source] and every renormalization scale [formula in source] , the closed-branch quark mass readout is the scheme-and-scale-fixed map [formula in source]

## [P] Admissible code subspace, entanglement, and pointer dynamics

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex:113-126](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex#L113) · `section:f3c733a0d9f99c529344` · subsection

The physical sector is the global admissible code subspace [formula in source] and supports stable record algebras and pointer reductions of the form [formula in source]

## Layered datum and admissibility

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:124-195](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L124) · `section:56aeac129663ec15f98f` · subsection

The technical bookkeeping behind the manuscript uses five levels: [formula in source] [formula in source] [formula in source] [formula in source] [formula in source] Here [formula in source] is the primitive boundary kernel, while [formula in source] is the derived theorem-level post-carrier kernel reconstructed from the joint discrete datum and the full selector.

## Normalized quotient form

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:99-108](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L99) · `section:6f97adf469554f5ab3a4` · subsection

The relative Euclidean theory used in the main closure section is not interpreted as a difference of measures. Instead it is organized as the normalized quotient [formula in source] Because the denominator is source independent on the admissible sector, the reference theory acts only as a fixed normalizer and does not interfere with reflection positivity.

## Bosonic and fermionic positivity on [formula in source] Padm

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:109-126](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L109) · `section:3e62027d730eadf67cd3` · subsection

The commutation relations [formula in source] ensure that reflection preserves the admissible subspace. The bosonic part then follows the standard Markov / reflection-stable Osterwalder–Schrader argument on admissible observables. For fermions, the admissible CAR kernel may be written as a reflected quadratic form; equivalently one may express the same condition as positivity of the associated Pfaffian structure on t

## Admissible OS reconstruction and asymptotic scattering

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:127-134](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L127) · `section:46aaa0c485552cb0fd29` · section

This appendix upgrades the admissible Schwinger, reconstruction, and scattering block from a named standard interface to a manuscript-level proof package. The point is not to replace standard machinery by ad hoc notation, but to verify explicitly that the admissible branch satisfies the relevant hypotheses on [formula in source] .

## Tempered admissible Schwinger families

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:135-170](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L135) · `section:db98896cc2bd07a555c8` · subsection

On the Euclidean continuation of [formula in source] , each truncated admissible Schwinger distribution [formula in source] defines a tempered distribution. Moreover, for every compact [formula in source] and every source monomial of total degree [formula in source] , its moments obey polynomial bounds determined by the same uniform heat-kernel estimates and finite local moments of the admissible constructive measure

## OS and CAR reconstruction on [formula in source] Padm

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:171-211](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L171) · `section:1e113de17835fcbe0cf8` · subsection

Padm] Let [formula in source] be the admissible Schwinger family on the Euclidean continuation of [formula in source] . If reflection positivity, temperedness, graded Euclidean covariance, graded symmetry, and clustering hold on [formula in source] , then there exist: a Hilbert space [formula in source] with vacuum vector [formula in source] , a strongly continuous positive-energy semigroup [formula in source] with s

## Stable massive Haag–Ruelle and LSZ closure

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:212-256](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L212) · `section:a793a2e5f9c55b10d109` · subsection

Let [formula in source] have an isolated simple pole with positive residue at [formula in source] . Then the corresponding one-particle contribution defines a positive spectral projector on the admissible Hilbert space.

## Dressed massless interface in the low-curvature region

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:257-271](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L257) · `section:8179568fc4c8c5884599` · subsection

The massless sector is not treated by bare Fock asymptotics in the present manuscript. The relevant object is the infrared-dressed interface package [formula in source] constructed from the soft charges of the admissible local net on the low-curvature region [formula in source] . This is exactly the interface package used in the main-text theorem thm:dressed-massless-interface.

## Yukawa kernels and positivity lemmas

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:1-38](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L1) · `section:2334f2b3d13fcb70cd58` · section

This appendix is the proof motor for the transport positivity, determinant-phase suppression, and bounded-residual statements used in the main text. The transport program is based on the regularized kernel [formula in source] Three remarks are important. The regulator [formula in source] is not optional: without it the kernel becomes ill-defined exactly where the admissibility question is most delicate. Positivity of

## Optional strong-coupling sharpening

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:39-54](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L39) · `section:26bf85fbb0c246d4fa02` · subsection

As an appendix-level dynamical sharpening of the hadronic admissibility theorem, one may further require the admissible center-neutral Wilson functional to obey strong-coupling dominance. On that optional route the relative Wilson loop satisfies [formula in source] and the physical Hilbert space contains no color-nonsinglet asymptotic states. This statement is kept in the appendix so that the main theorem surface doe

## Minimal admissible vacuum

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:244-253](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L244) · `section:11f5a6c75297d76088e5` · subsection

At finite volume or with a declared cutoff, an admissible vacuum candidate is written as [formula in source] with lower boundedness and coercivity understood exactly as in the main-text closure axioms. The stronger generative theorem path described in the conclusion would refine this object to the global admissible vacuum functional [formula in source] whose variations also select the transport branch. In this append

## Split inclusion horizon approximation

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:305-339](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L305) · `section:9f1b339bd5128b255be4` · subsection

Let [formula in source] be the local admissible net reconstructed in thm:admissible-local-minkowski-net, and assume in addition the split property. Then for every nested triple [formula in source] there exists a type-I factor [formula in source] such that [formula in source] Hence on a suitable code subspace one obtains an approximate tensor factorization [formula in source]

## Transient event status

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:361-366](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L361) · `section:6dc4af30cbb0c1ea9ae6` · subsection

The topological burst channel of conj:topological_phase_slip_burst_channel is kept at programmatic-target status. What is fixed in the present version is only the admissible phase-slip channel and its scaling form, not yet a complete defect dynamics or radiative-transfer derivation.

## Table 1: Closed theoretical outputs

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex:33-71](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex#L33) · `section:e5b0bcd49a6753c5f3ff` · subsection

@> p0.09 > p0.11 > p0.10 > p0.04 > p0.18 > p0.20 > p0.08 @ Particle & Repr. & Ext.\ source & [formula in source] & TFPT origin & Internal source & Status \\ 7@l Fermion sector (one family [formula in source] ): \\ [formula in source] & [formula in source] & [formula in source] & [formula in source] & carrier scaffold & hard carrier, [formula in source] & Theorem \\ [formula in source] & [formula in source] & [formula

## Why the originally proposed implication is false

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex:86-89](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex#L86) · `section:22866ebd1bb6a6c4dd9f` · subsection

No opening prose excerpt; see the source.

## Two covariances do not specify a sector automorphism.

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex:100-107](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex#L100) · `section:464734c52bee24090d15` · paragraph

Even in finite dimension, two mixed covariances [formula in source] and [formula in source] need not be unitarily conjugate: unitary conjugacy preserves the spectrum. Thus [formula in source] or [formula in source] does not by itself produce a Bogoliubov map on the original window CAR algebra. It does produce a canonical equivalence of the purified standard forms, which is the exact local result proved below.

## The index-four fixed-point Q-system

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex:339-384](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex#L339) · `section:992f64e38e1943a88315` · subsection

For each interval set [formula in source] and [formula in source] . Conformal-net local algebras are factors; and trivial relative commutant. Theorem applies. The group average is [formula in source] It is normal, unital, positive, faithful, idempotent, and [formula in source] -bimodular. For example, if [formula in source] , then [formula in source] Faithfulness follows because [formula in source] and [formula in so

Explicit source references:

- [verification/v973_seam_route_narrowing.py](../../../../verification/v973_seam_route_narrowing.py#L1) · explicit_script_identifier

## TFPT corollary and the P1 reading

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex:287-288](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex#L287) · `section:584fe4ac4fcf353a0b77` · section

No opening prose excerpt; see the source.

## Equidistribution over four deck channels

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex:324-412](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex#L324) · `section:a90bfaafa3f1446fd499` · subsection

The exact statement needed for the P1 reading is elementary but has one hypothesis that must be visible.

Explicit source references:

- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [P1.INDEX.KMS.01](../../../../verification/status_ledger.csv#L700) · explicit_claim_identifier · original status at linked ledger row

## Dynamical finite gauge links: Lie–Schwinger gap theorem

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex:48-276](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex#L48) · `section:42c2beac40084e5dc2c7` · section

Theorem not itself add fluctuating link Hilbert spaces. We therefore audit the finite-group dynamical-link extension first against the local Schrieffer–Wolff construction of Bravyi, DiVincenzo, and Loss BDL2011, and then against the gap theorem proved by Fröhlich and Pizzo FP2020.

## What is and is not explicit in the FP window

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex:277-345](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex#L277) · `section:0e3fe3476cf5c8d9f09e` · subsection

The Lie–Schwinger proof contains one explicit series constant: [formula in source] Appendix A of FP2020 uses the explicit convergence restriction [formula in source] Its local-gap estimate also has the explicit sufficient inequality [formula in source] whose positive boundary is [formula in source] . However, the induction closing Theorem 3.4 of FP2020 introduces unevaluated universal constants [formula in source] an

Explicit source references:

- [experiments/tfpt-discovery/det16_dynamical_links_probe.py](../../../../experiments/tfpt-discovery/det16_dynamical_links_probe.py#L1) · explicit_file_citation

## Exact spectator statement

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/003-subsection-the-norm-count.tex:181-263](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/003-subsection-the-norm-count.tex#L181) · `section:cc5e83b2baf29bc6787b` · subsection

Let [formula in source] carry a wall Hamiltonian [formula in source] and let [formula in source] carry [formula in source] . If the DET16 terms act as the identity on wall modes, then [formula in source] Hence [formula in source] The [formula in source] copy is exactly the original wall spectrum, with every multiplicity preserved.

Explicit source references:

- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row

## Front matter / support

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/001-section-verdict-and-logical-form.tex:1-44](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/001-section-verdict-and-logical-form.tex#L1) · `section:b1247ef0938a179aa8e0` · frontmatter

We attempt the complete scaling-limit theorem for the concrete order-four charged field [formula in source] The algebraic limit-exchange statement is proved in full for an arbitrary finite group: equivariant injective inductive limits commute isometrically with crossed products, coefficient and fixed-point expectations commute with the limit, and their Pimsner–Popa constants remain uniform. Assuming the charged field

## The [formula in source] -inductive theoremThe C-star inductive theorem

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/004-subsection-relative-locality-of-the-charged-and-neutral-.tex:216-307](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/004-subsection-relative-locality-of-the-charged-and-neutral-.tex#L216) · `section:2a389e0ac3144ae52c80` · subsection

Let [formula in source] be finite and let [formula in source] be an inductive system of unital [formula in source] -algebras with injective maps. Suppose [formula in source] are actions and [formula in source] Let [formula in source] and [formula in source] . Then the canonical map is a [formula in source] -isomorphism [formula in source] For the coefficient expectations [formula in source] and fixed-point expectatio

## The Lieb–Robinson theorem and explicit TFPT velocity

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:140-224](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L140) · `section:5890da8efe52b8feadb2` · section

Let [formula in source] be a graph, let every local Hilbert space be finite dimensional with a uniform dimension bound, and let a self-adjoint interaction satisfy [formula in source] For every finite [formula in source] , define [formula in source] . If [formula in source] , [formula in source] , and [formula in source] , then, uniformly in [formula in source] , [formula in source] Thus an admissible Lieb–Robinson ve
