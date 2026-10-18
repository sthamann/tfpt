# Quantum fields, dynamics and continuum — part 4

[Topic entry](../quantum-continuum.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Lemma A (Seam Determinant).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:16-38](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L16) · `section:79cfcc11c471d5bbf49d` · paragraph

Proof skeleton. Read the determinant as a primitive admissible zeta determinant. The admissible trace [formula in source] admits a primitive-orbit decomposition; closed-branch selection plus [formula in source] plus [formula in source] leaves only the minimal seam class with multiplicity 2 (double sheet), area [formula in source] (primitive seam norm), and action [formula in source] (two oriented EM runs). The non-pr

## The candidate v4.6 bundle

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:102-124](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L102) · `section:4427ed5d9336270018c6` · subsection

In the absence of a real Sprint-2A boundary extraction, v4.6.3 ships a deterministic candidate bundle synthesised from the seven primitives: [formula in source] : Hermitian, eigenvalues [formula in source] on [formula in source] ; [formula in source] : seam-graded [formula in source] modulated by [formula in source] , normalised; [formula in source] : pairing involution [formula in source] ; spectral flag: c [formula

## The Sprint 2A Branch Extraction Contract

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:281-292](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L281) · `section:251779a935bf6cfe780c` · section

Stefan's v4.6.3 review converges on a single sharp statement: the code is no longer the bottleneck; the data side and the proof side are. The next sensible step is therefore neither another plot nor another module — it is a formal, executable Branch Extraction Contract that any future Sprint-2A run must satisfy. This section defines that contract and reports what the v4.6.3 candidate bundle scores against it.

## Contract specification

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:293-336](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L293) · `section:ba4d7ea88722968045bc` · subsection

Sprint 2A Branch Extraction Contract\\ Input. closed TFPT branch operators.\\ Output. [formula in source] \,( npz), [formula in source] \,( npz), [formula in source] \,( npz), spectral_flag\,( json+ npz), observer_embedding\,( json), [formula in source] -grid\,( npz), direction grid\,( npz), shell-power validation\,( json), branch origin\,( json).\\ Hard checks. (1) [formula in source] Hermitian; (2) [formula in sour

## Engineering.

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:27-35](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L27) · `section:9b59602e5bee6ec454f7` · paragraph

Sprint 2A boundary extraction yielding the seven contract files with [formula in source] and the canonical spectral flag (no Haar rotation). A real observer embedding: tetrad, [formula in source] , parity from a TFPT branch position computation.

## Discharge taxonomy

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:56-100](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L56) · `section:b983c04974ce44edef90` · subsection

Every hook is tagged with one of 12 status classes. The taxonomy distinguishes convention adoption (no theorem needed) from theorem proof (paper-side work) from data extraction (engineering work) from numerical verification. This is the sharpening Stefan demanded:

## BT2 (closes B.h1).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:234-241](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L234) · `section:ec7f7040414e02e11d3b` · paragraph

[formula in source] has a unique primitive curvature instanton with action [formula in source] and zero-mode norm [formula in source] ; saddle-point gives [formula in source] and inverting yields [formula in source] . Structurally analogous to Yang-Mills, BCS-gap, and Coleman-de\,Luccia. Closes the inflation block [formula in source] without COBE.

## What this pipeline does not claim

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:179-214](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L179) · `section:157a7c50b2b0c5f60c40` · section

No theorem-level lemmas. Lemmas A–E are conjectures with proof skeletons ( at TFPT v4.6. The pipeline runs in candidate mode only. No real Mode-E branch. The Mode-E run uses the candidate v4.6 synthetic bundle, not a real Sprint-2A extraction of [formula in source] , [formula in source] , [formula in source] from the boundary data. Real Mode E is a Sprint 2A–2D deliverable. No claim of pixel-level Planck agreement. M

## v4.10–v4.12: Operator-Discharged Closure and the Planck Pass

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:291-303](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L291) · `section:49689ab702d7c648da00` · section

The v4.6 cycle delivered the candidate closure with five lemmas A–E and a 14-hook proof discharge. The next two sprints (v4.7, v4.8) narrowed the geometry to the Lens space [formula in source] on the spectral-action corridor, and v4.9's Fisher residual decomposition pinpointed the remaining [formula in source] gap to two parameters: [formula in source] and [formula in source] . Sprints v4.10–v4.12 closed this gap ope

Explicit source references:

- [verification/v412_sheet_source_corner_J.py](../../../../verification/v412_sheet_source_corner_J.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v411: u/d ratio as a pure V-power readout *) num = one . MatrixPower[V, 4] . one; den = (a . V . one)(one . MatrixPower[V, 2] . one); checkExact["v411 FLAV.UD.VPOWER.01: c_u/c_d = (1.V^4.1)/((a.V.1)(1.V^2.1)) = 55/(9*13) = 55/117, identical to g_car*||Pl(K)||_1/(N_fam^2 Delta_Q) = 5*11/(9*13); RE-ENCODING, value stays [C]", num == 55 && a . V . one == 9 && one . MatrixPower[V, 2] . one == 13 && num/den == 55/117 && (5*11)/(9*13) == 55/117]; (* v412: the sheet source corner J = M(1,-2) on the Z2 wall *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2417)

## Open items beyond v4.12.

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/006-subsection-the-bt2-operator-discharge-v4-11.tex:228-242](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/006-subsection-the-bt2-operator-discharge-v4-11.tex#L228) · `section:077d180c67f187c9d069` · paragraph

Stefan v4.12 brief Section 7 explicitly marks these as optional, NOT CMB-block blockers: Higher-order Spectral-Action coefficients [formula in source] could shift [formula in source] at [formula in source] — below any conceivable Planck sensitivity. Formal QFT proof of the [formula in source] residual in the visibility Ward identity (currently verified numerically: residual [formula in source] ). Multi-channel BSE (o

## Lemma B.h1 (hard).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:47-62](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L47) · `section:a95e9e8c90c77d844a96` · paragraph

Hook. Prove [formula in source] from the admissible curvature path integral.\\ Proposed solution. The exponential is the signature of a non-perturbative instanton-class contribution. The admissible curvature path integral admits a tunneling configuration with Euclidean action [formula in source] . Saddle-point evaluation gives [formula in source] with [formula in source] the zero-mode normalisation. Structurally anal

## Lemma C3.h1 (hard).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:89-102](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L89) · `section:0e32b7565f5445fd8cc3` · paragraph

Hook. Prove the BBN-network collapse onto [formula in source] .\\ Proposed solution. BBN is dominated by the freeze-out [formula in source] ratio. The TFPT EM holonomy [formula in source] shifts the weak rate uniformly: [formula in source] . Detailed-balance freeze-out then gives [formula in source] (the [formula in source] is the SM value at [formula in source] ). Other BBN reactions burn essentially all neutrons in

## Lemma E1.h1 (medium).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:156-166](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L156) · `section:9b453a5d07c5cca10999` · paragraph

Hook. Sprint 2A boundary extraction.\\ Proposed solution. Sprint 2A must supply (i) the boundary Dirac [formula in source] (Paper 1 export), (ii) the admissible projector [formula in source] (Paper 4 selectors), (iii) the second functional derivative of [formula in source] at the cosmological vacuum, (iv) the projection. Acceptance: the Sprint-2A contract validator passes K_zeta_adm_hermitian on a real bundle with [f

## Lemma E2.h1 (hardest).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:167-184](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L167) · `section:489cf8b41b3197563b9a` · paragraph

Hook. Prove that the six flag operators [formula in source] pairwise commute on [formula in source] .\\ Proposed solution. Commutativity is a structural consequence of admissibility: (a) [formula in source] because the action is sheet-symmetric; (b) [formula in source] because both live on the boundary modes; (c) [formula in source] because [formula in source] is the closure of the carrier kinetic energy on which [fo

## Lemma E4.h1 (medium).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:196-210](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L196) · `section:7fc56d36ace0447c688d` · paragraph

Hook. Prove [formula in source] for the real [formula in source] .\\ Proposed solution. [formula in source] is the second functional derivative of a real action and is therefore real-symmetric. When expressed in a real (sheet) basis, [formula in source] ; on a complex eigenbasis, [formula in source] implements complex conjugation modulo sheet swap, giving [formula in source] . The candidate v4.6 bundle fails because 

## C3.h1 \,—\, Helium Fraction \,( closed_pending_bbn_verification)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:319-334](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L319) · `section:4df1aaaa251d85018a31` · subsection

Proof. The leading alpha channel binds four nucleons. In the symmetric freeze-out sector [formula in source] , [formula in source] . TFPT EM holonomy shifts the weak rate uniformly: [formula in source] . Linear sensitivity: [formula in source] . Hence [formula in source] and [formula in source] up to [formula in source] . [formula in source] under TFPT weak-rate deformation.

## E1.h1 \,—\, Existence of branch operator \,( closed_pending_sprint2a_extraction)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex:29-42](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex#L29) · `section:0b78e24d6f5b9b42c90d` · subsection

Claim. [formula in source] self-adjoint on [formula in source] .

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

## Relative objects

[documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/003-subsection-relative-objects.tex:1-25](../../../../documents/archive--tfpt-45--source_extracts--01_boundary_kernel_source/sections/003-subsection-relative-objects.tex#L1) · `section:d99e299ca0fe44467cae` · subsection

The adjective relative is used in one fixed sense throughout the paper: every operator or action is compared to a declared reference object.

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

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/003-source.tex:1-370](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/003-source.tex#L1) · `section:5c1910f055c3e2f71823` · frontmatter

Let [formula in source] be the graded algebra of carrier-invariant Yukawa trilinears. A homogeneous nonzero invariant is called primitive if it is indecomposable, equivalently if it does not lie in the ideal generated by positive-degree invariants of strictly lower carrier degree.

## Front matter / support

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/004-source.tex:1-381](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/004-source.tex#L1) · `section:5248af93a50c00dd9d94` · frontmatter

thm:sheet-cp-protection gives [formula in source] By lem:topological-sector-positivity, the admissible partition function admits a sector decomposition [formula in source] The antiunitary sheet symmetry of thm:sheet-cp-protection gives [formula in source] so the sector weights satisfy [formula in source] . Hence [formula in source] By lem:nontrivial-topological-support, one has [formula in source] . Therefore for eve

## Front matter / support

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex:1-122](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex#L1) · `section:7a7755c65bfd436c721b` · frontmatter

eta=0] Fix finite volume [formula in source] and let [formula in source] be the primitive blocked admissible transfer operator with Perron vector [formula in source] . Let [formula in source] be the blocked admissible parent Hamiltonian of lem:parent-gap-from-transfer-block, with [formula in source] Let the physical admissible Hamiltonian be written as [formula in source] where each added term is positive semidefinit

## Admissible Schwinger functions, Minkowski locality, and scattering closure

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex:123-403](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/005-subsection-admissible-schwinger-functions-minkowski-loca.tex#L123) · `section:58b3a771f93680088d7d` · subsection

Let [formula in source] denote a low-curvature branch region on which [formula in source] and [formula in source] All scattering statements below are formulated on [formula in source] .

## Internal reduction theorem and renormalized observable hierarchy

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/006-section-internal-reduction-theorem-and-renormalized-obse.tex:1-10](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/006-section-internal-reduction-theorem-and-renormalized-obse.tex#L1) · `section:9643ca8ced2e76618571` · section

Above the closed theorem stack ending at [formula in source] , the present version records one theorem-level input reduction and a stratified output-side observable chain. On the input side, the reduction is internal to a deliberately weakened ambient class. On the output side, the passage from [formula in source] to the renormalized low-energy package [formula in source] and then to the physical observable layer [fo

## Weakened ambient class

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/006-section-internal-reduction-theorem-and-renormalized-obse.tex:11-399](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/006-section-internal-reduction-theorem-and-renormalized-obse.tex#L11) · `section:4cc52509e02e7fb2728e` · subsection

Let [formula in source] denote the category whose objects are tuples [formula in source] satisfying the following ambient admissibility axioms: Real even boundary datum: [formula in source] is an admissible real even one-sided boundary datum with reflection-regular collar. Quasilocal positive dynamics: [formula in source] is a quasilocal dynamics with reflection positivity and an admissible vacuum sector. Morphisms a

## Renormalized, physical, and scheme readout layers

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/007-subsection-renormalized-physical-and-scheme-readout-laye.tex:1-372](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/007-subsection-renormalized-physical-and-scheme-readout-laye.tex#L1) · `section:3e7cfda7c9252d871993` · subsection

Let [formula in source] be an admissible infrared regulator commuting with the structural sector selection. Define [formula in source] and set [formula in source] The renormalized admissible effective action is [formula in source]

## Front matter / support

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:1-139](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L1) · `section:84c76a3dafcdc2baa222` · frontmatter

0.96 ! (hadm) at (-5.0,0.9) [formula in source] \ sector; (wk) at (-1.6,0.9) [formula in source] \ generator; (gk) at (1.8,0.9) [formula in source] \ admissible flow; (gren) at (5.2,0.9) [formula in source] \ 1PI action;

## Relative reflection positivity with fermions

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:140-142](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L140) · `section:9ac06ba4695ad4e6544a` · section

No opening prose excerpt; see the source.

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

## Canonical spectral Einstein functional and geometric Hodge closure

[documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/002-subsection-closed-texorpdfstring-41-41-chain-after-famil.tex:39-391](../../../../documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/002-subsection-closed-texorpdfstring-41-41-chain-after-famil.tex#L39) · `section:c8d5c06b887f4073520d` · subsection

The local target action is written as the low-curvature expansion of a canonical spectral Einstein functional: The relative bosonic endomorphism used below is and the resulting low-curvature residue decomposition is summarized in tab:heat-kernel-map.

## Absolute dimensionless metrology from the boundary branch

[documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/005-section-absolute-dimensionless-metrology-from-the-bounda.tex:268-296](../../../../documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/005-section-absolute-dimensionless-metrology-from-the-bounda.tex#L268) · `section:09632977166e5c21e3d5` · section

The closed branch should not be read as a source of isolated SI numbers. Its hard content is an internal dimensionless metrology: the boundary datum carries its own spectral unit, the stationary geometric branch fixes the gravitational normalization relative to that unit, the renormalized 1PI action fixes physical electroweak and pole readouts, and only afterwards does one choose an external comparison scheme. In the

## FRW reduction, seam transfer, and the scalaron branch

[documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/001-section-frw-reduction-seam-transfer-and-the-scalaron-bra.tex:5-389](../../../../documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/001-section-frw-reduction-seam-transfer-and-the-scalaron-bra.tex#L5) · `section:045fa5ee1e2a674718cb` · section

The trace-class seam transfer belongs to the main reconstruction surface. The cosmological constant and the reduced scalaron / determinant-line dynamics are therefore fixed directly on the closed branch. Axion, reheating, and leptogenesis quantities are read through explicit interface formulas built from the same theorem-level objects [formula in source] , [formula in source] , and the positive scalaron sector [formu

## [P] Admissible code subspace, entanglement, and pointer dynamics

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex:113-126](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex#L113) · `section:f3c733a0d9f99c529344` · subsection

The physical sector is the global admissible code subspace [formula in source] and supports stable record algebras and pointer reductions of the form [formula in source]

## Relative objects

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:99-123](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L99) · `section:29cf0c90b46e29d07cfe` · subsection

The adjective relative is used in one fixed sense throughout the paper: every operator or action is compared to a declared reference object.

## Relative reflection positivity with fermions

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:96-98](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L96) · `section:849a5ab4e7e29988291c` · section

No opening prose excerpt; see the source.

## Normalized quotient form

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:99-108](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L99) · `section:6f97adf469554f5ab3a4` · subsection

The relative Euclidean theory used in the main closure section is not interpreted as a difference of measures. Instead it is organized as the normalized quotient [formula in source] Because the denominator is source independent on the admissible sector, the reference theory acts only as a fixed normalizer and does not interfere with reflection positivity.

## OS and CAR reconstruction on [formula in source] Padm

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:171-211](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L171) · `section:1e113de17835fcbe0cf8` · subsection

Padm] Let [formula in source] be the admissible Schwinger family on the Euclidean continuation of [formula in source] . If reflection positivity, temperedness, graded Euclidean covariance, graded symmetry, and clustering hold on [formula in source] , then there exist: a Hilbert space [formula in source] with vacuum vector [formula in source] , a strongly continuous positive-energy semigroup [formula in source] with s

## Record algebra and pointer dynamics

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:236-243](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L236) · `section:1fdbae2cdf2857113fed` · section

This appendix elaborates the main-text record constructions and the stable pointer-algebra package used in the downstream closure discussion. Horizon thermality and prediction / transient semantics are separated into the following appendix sections so that record theory, black-hole continuation, and phenomenological event channels do not blur into one mixed extrapolation block.

## Record growth principle

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:254-267](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L254) · `section:809be784f961d8ece0b0` · subsection

One useful coarse-grained record algebra is [formula in source] As [formula in source] decreases, more stable channels open. The intended arrow-of-time claim is therefore [formula in source] but only as a record-growth principle, not as a replacement for detailed nonequilibrium dynamics.

## Transient event status

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:361-366](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L361) · `section:6dc4af30cbb0c1ea9ae6` · subsection

The topological burst channel of conj:topological_phase_slip_burst_channel is kept at programmatic-target status. What is fixed in the present version is only the admissible phase-slip channel and its scaling form, not yet a complete defect dynamics or radiative-transfer derivation.

## A compressed covariance is not a polarization.

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex:90-99](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex#L90) · `section:5881aed8196c0715700a` · paragraph

If [formula in source] is a proper window projection and [formula in source] is a global Fermi projection, then [formula in source] is generally a positive contraction, not a projection: [formula in source] Consequently, Shale–Stinespring cannot be applied to [formula in source] as though it were a Fock polarization. We repair this by the canonical Araki–Wyss purification in Section

## Two covariances do not specify a sector automorphism.

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex:100-107](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex#L100) · `section:464734c52bee24090d15` · paragraph

Even in finite dimension, two mixed covariances [formula in source] and [formula in source] need not be unitarily conjugate: unitary conjugacy preserves the spectrum. Thus [formula in source] or [formula in source] does not by itself produce a Bogoliubov map on the original window CAR algebra. It does produce a canonical equivalence of the purified standard forms, which is the exact local result proved below.

## The direct rotation

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/002-subsection-the-direct-rotation.tex:1-286](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/002-subsection-the-direct-rotation.tex#L1) · `section:40997fa8df4a235e1a32` · subsection

Let [formula in source] be finite-rank orthogonal projections of equal rank and suppose [formula in source] . Set [formula in source] Then [formula in source] is unitary, [formula in source] , and [formula in source] depends continuously in operator norm on [formula in source] throughout the open set [formula in source] . In addition, [formula in source]

## The exact [formula in source] Z4 tower

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/003-section-the-exact-texorpdfstring-mathbb-z-4-z4-tower.tex:1-213](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/003-section-the-exact-texorpdfstring-mathbb-z-4-z4-tower.tex#L1) · `section:ac3bc77b2d4a37b12824` · section

Let [formula in source] be a unital inductive system of finite matrix algebras. Suppose [formula in source] is unitary, [formula in source] and let [formula in source] . Write [formula in source] for the canonical crossed-product unitary: [formula in source]

## Front matter / support

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex:1-40](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex#L1) · `section:40019e04da209a36b2f2` · frontmatter

Let [formula in source] be an irreducible finite-index inclusion of conformal nets on [formula in source] , let [formula in source] for a proper gauge action commuting with rotations, and suppose that [formula in source] is holomorphic, with [formula in source] and central charge [formula in source] . We prove the strongest correct form of the proposed KMS extension statement. At angular inverse temperature [formula 

## The rotational KMS state

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex:79-117](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex#L79) · `section:6ba6705516b9eeff9f25` · subsection

Let [formula in source] be the conformal Hamiltonian and let [formula in source] be the rotation dynamics on the locally normal universal algebra [formula in source] . For [formula in source] put [formula in source] For a completely rational conformal net the character is finite, and the rotational KMS classification quoted below in fact recovers the trace-class property from any extremal KMS state. In the concrete [

## Araki's CAR KMS theorem

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex:120-155](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex#L120) · `section:822cfcea14e75bfdc29e` · subsection

Let [formula in source] be a complex Hilbert space, let [formula in source] be a possibly unbounded one-particle Hamiltonian, and let [formula in source] be the strongly continuous Bogoliubov dynamics on [formula in source] determined on generators by [formula in source] For every [formula in source] there is a gauge-invariant quasi-free state [formula in source] whose two-point function is [formula in source] and wh

## The holomorphic KMS extension theorem

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex:68-228](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex#L68) · `section:a40d55f336d04a48cbfe` · section

Let [formula in source] satisfy the hypotheses of Section 1: for every interval [formula in source] , [formula in source] is an irreducible index-four inclusion, [formula in source] for a proper internal gauge action commuting with rotations, and [formula in source] is a holomorphic conformal net with [formula in source] and [formula in source] . Let [formula in source] and let [formula in source] be the restriction 

Explicit source references:

- [verification/v993_minimal_defect_selector.py](../../../../verification/v993_minimal_defect_selector.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v993) AX.P2.01 census: SNF disc groups, unique (D5,A3), [lambda]^2=[v], CE dims ---- Python-only: random CE axiom sampling on M_d^{Z4} / crossed product. *)](../../../../verification/wolfram/tfpt_readouts.wl#L557)

## What this closes and does not close

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/003-section-what-this-closes-and-does-not-close.tex:1-31](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/003-section-what-this-closes-and-does-not-close.tex#L1) · `section:fa0328aaea7476296880` · section

For an abstract holomorphic conformal net satisfying the hypotheses, the rotational KMS extension theorem is complete: there is one extension, its expectation is canonical, and both local relative-commutant mixing and thermal-sector mixing are excluded. The finite v995 computation is exactly consistent with this result. Applying it to the TFPT collar remains conditional on the continuum-net identification in the box 

Explicit source references:

- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v995_kms_subnet_rigidity.py](../../../../verification/v995_kms_subnet_rigidity.py#L1) · explicit_script_identifier
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row

## Remaining gap

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/003-section-what-this-closes-and-does-not-close.tex:32-72](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/003-section-what-this-closes-and-does-not-close.tex#L32) · `section:df7c31419ad580f2ce16` · section

red!65!blackred!3 0.91 Remaining gap (exact statement). For the TFPT [formula in source] QWZ collar with its four quarter-twisted deck labels, prove that the scaling-limit local von Neumann algebras are the hyperfinite type- [formula in source] factors of a conformal net and identify, as conformal nets with vacuum, common stress tensor, rotation dynamics, and [formula in source] action, the resulting concrete inclusi

## Volume-independent perturbative stability

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex:1-47](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex#L1) · `section:d2e8b5390f14d8a13881` · section

Let [formula in source] range over finite subsets or tori of a fixed [formula in source] -dimensional bounded-degree lattice. Let [formula in source] be the DET16 Hamiltonian finite-range interaction satisfying Definition uniformly in volume. Then there exists [formula in source] , depending only on [formula in source] , the interaction range, and the local interaction-norm bound, but not on [formula in source] , suc

## The norm count

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/003-subsection-the-norm-count.tex:1-64](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/003-subsection-the-norm-count.tex#L1) · `section:b969269cec59b8c62a7b` · subsection

For unit-amplitude nearest-neighbour hopping across one bond, [formula in source] with [formula in source] unitary, the one-particle bond matrix has sixteen eigenvalues [formula in source] and sixteen eigenvalues [formula in source] . Its fermionic second quantization therefore has [formula in source] If the lattice coordination is [formula in source] , at most [formula in source] such bonds touch one cluster. The ad

## Conclusion

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/003-subsection-the-norm-count.tex:264-319](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/003-subsection-the-norm-count.tex#L264) · `section:f00ab91bc062ae881454` · section

BHM2010 S. Bravyi, M. B. Hastings, and S. Michalakis, Topological quantum order: stability under local perturbations, J.\ Math.\ Phys.\ 51 (2010), 093512, https://doi.org/10.1063/1.3490195 doi:10.1063/1.3490195.

## The continuum estimate is complete

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/002-section-l1-uniform-energy-bounds.tex:4-42](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/002-section-l1-uniform-energy-bounds.tex#L4) · `section:c8c5be1ac1a1fb0892bf` · subsection

In the level-one lattice VOA of the glued rank-eight lattice, the norm-two vector [formula in source] is a weight-one affine current. For every [formula in source] there is a constant [formula in source] such that [formula in source]

## The edge-projected lattice Green form

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/002-section-l1-uniform-energy-bounds.tex:43-294](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/002-section-l1-uniform-energy-bounds.tex#L43) · `section:0b98bdbf75c1bdb48084` · subsection

We now define and estimate the concrete [formula in source] used by the collar bosonization. It is important that this is a definition from the frozen QWZ edge band, not a continuum ansatz.

## Outerness of the limiting four-grade action

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/004-subsection-relative-locality-of-the-charged-and-neutral-.tex:43-82](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/004-subsection-relative-locality-of-the-charged-and-neutral-.tex#L43) · `section:b97bc8122d0311e44b14` · subsection

On every limiting local factor generated by the neutral algebra and the four charged grades, every nonidentity element of the [formula in source] gauge action is outer.

## The [formula in source] -inductive theoremThe C-star inductive theorem

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/004-subsection-relative-locality-of-the-charged-and-neutral-.tex:216-307](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/004-subsection-relative-locality-of-the-charged-and-neutral-.tex#L216) · `section:2a389e0ac3144ae52c80` · subsection

Let [formula in source] be finite and let [formula in source] be an inductive system of unital [formula in source] -algebras with injective maps. Suppose [formula in source] are actions and [formula in source] Let [formula in source] and [formula in source] . Then the canonical map is a [formula in source] -isomorphism [formula in source] For the coefficient expectations [formula in source] and fixed-point expectatio

## Thermodynamic Dynamics for the TFPT Finite-Range\\ Master-Hamiltonian Class

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/preamble.tex:1-43](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/preamble.tex#L1) · `section:b0fa4b0dcd35f08f5957` · frontmatter

colorlinks=true, linkcolor=blue!55!black, citecolor=blue!55!black, urlcolor=blue!55!black

Explicit source references:

- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row

## Front matter / support

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:1-28](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L1) · `section:665d1fce3f7c4d6f2241` · frontmatter

We isolate the uniformly finite-dimensional, finite-range Hamiltonian class actually assembled by the TFPT [formula in source] - and [formula in source] -dimensional probes: electric and plaquette gauge terms, gauge-dressed fermion hopping, the DET16 mirror projector, and the seam clock and charge terms. At the frozen [formula in source] -dimensional coefficients the interaction has range [formula in source] , larges

## The concrete uniformly local class

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:29-30](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L29) · `section:ca221ce847445e4b4967` · section

No opening prose excerpt; see the source.

## Ambient tensor-product algebra

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:31-111](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L31) · `section:db01ea1aa320dae5cd00` · subsection

Let [formula in source] with graph distance [formula in source] and coordination [formula in source] . For a finite [formula in source] , put [formula in source] One cell contains the four representative physical edge modes, a mirror Fock factor, the two positively oriented outgoing finite-group gauge links, and a four-state seam clock. Thus [formula in source] The DET4 numerical analogue has dimension [formula in so

Explicit source references:

- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_file_citation

## Uniform constants

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:112-139](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L112) · `section:4eb86e473c472c9b53e6` · subsection

Define the finite-range interaction moment [formula in source] There are two assigned electric links, four plaquettes, and four bonds incident on a square-lattice cell. Consequently [formula in source] These bounds are independent of [formula in source] . More generally, bounded degree, finite [formula in source] , finite local dimension and finite [formula in source] are the class hypotheses; the displayed numbers a

## The Lieb–Robinson theorem and explicit TFPT velocity

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:140-224](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L140) · `section:5890da8efe52b8feadb2` · section

Let [formula in source] be a graph, let every local Hilbert space be finite dimensional with a uniform dimension bound, and let a self-adjoint interaction satisfy [formula in source] For every finite [formula in source] , define [formula in source] . If [formula in source] , [formula in source] , and [formula in source] , then, uniformly in [formula in source] , [formula in source] Thus an admissible Lieb–Robinson ve

## Norm thermodynamic limit

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:225-300](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L225) · `section:a83819dcff945ddb5996` · section

For every [formula in source] , the net [formula in source] exists in norm, uniformly for [formula in source] in compact real intervals and independently of the exhausting sequence. It extends uniquely to a strongly continuous one-parameter group of [formula in source] -automorphisms of [formula in source] .

## Gauss law and the correct consistent family

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex:301-363](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/001-section-the-concrete-uniformly-local-class.tex#L301) · `section:30db4349cae910dc7034` · section

Let [formula in source] be the group of finitely supported local gauge transformations on the ambient field algebra, and let [formula in source] denote its action. Define [formula in source] The electric and plaquette terms are gauge invariant; the hopping contains its parallel transporter; the determinant projector is a Spin(10) singlet; and the seam charge is neutral as assembled. Thus [formula in source]

## Existence of equilibrium states

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex:1-61](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex#L1) · `section:0e46a5a279dce3de4926` · section

The infinite-volume system [formula in source] , and its invariant subalgebra [formula in source] , have at least one ground state. For every [formula in source] , they have at least one [formula in source] -KMS state.

## Numeric twin

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex:62-106](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex#L62) · `section:f31237f5fb1b89d8d1a6` · section

The companion [formula in source] uses the exact nearest-neighbour physical-edge sector of the assembled model while comparing it against the complete class constant earlier IR-universality witness. It reports: [formula in source] For the one-site projector, [formula in source] , and nested open volumes, the specialization of [formula in source] The zeros are numerical precision statements, not analytic finite-speed 

Explicit source references:

- [experiments/tfpt-discovery/lieb_robinson_witness_probe.py](../../../../experiments/tfpt-discovery/lieb_robinson_witness_probe.py#L1) · explicit_file_citation

## Combined theorem and exact boundary

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex:107-156](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex#L107) · `section:b26762fa76b33b384e1a` · section

For the TFPT master-Hamiltonian class finite-dimensional local factors and coefficients of Table the finite-volume dynamics satisfy the uniform Lieb–Robinson bound [formula in source] ; the thermodynamic-limit dynamics exist in norm on all local observables and define a strongly continuous automorphism group; the group restricts consistently to the Gauss-invariant quasilocal algebra, with projector compatibility in t

## Conclusion

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex:157-212](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex#L157) · `section:f1269209928f923042c2` · section

The amended contract makes the continuum limit optional but the thermodynamic limit mandatory. The latter is now proved at the Hamiltonian-class level for the concrete finite-group, finite-local-space TFPT assembly. The proof is insensitive to finite-volume boundary shape and does not infer thermodynamics from a finite scan. Its explicit velocity is conservative, while the numerical witness checks the expected cone, 

## 2026-09-09 (CLXII): Source fields, full lattice dynamics and Clock/E8 bridge consolidated

[documents/changelog/sections/001-source.tex:122-151](../../../../documents/changelog/sections/001-source.tex#L122) · `section:117cbc6545f0d479f930` · subsection

The post-Round 27 research archive, including Rounds 28–50 and subsequent named branches, is integrated without rewriting source-pinned historical records. The contracts paper gives a consolidated derivation of local charged CAR fields from the original filled QWZ sea: both adjoints, integer charge, finite-energy generator convergence and the top-edge charge minimum [formula in source] . Neutral four-point collision 

## 2026-09-05 (CLIX): non-RH round 7 — free quantum curvature, charged twists and interaction boundaries

[documents/changelog/sections/001-source.tex:209-236](../../../../documents/changelog/sections/001-source.tex#L209) · `section:cfb240e07819e5428824` · subsection

Five modules v1031– v1035 add [formula in source] typed checks (183 exact, 13 source-contract, 37 floating) to the registered suite ( [formula in source] modules), including the round-6 quantum prerequisite. v1031_quantum_tensor_curvature.py ( [formula in source] ) constructs the zero-mean Weyl/Fock target and its distribution limit; v1032_covariant_curvature.py ( [formula in source] ) supplies exact identities for t

Explicit source references:

- [verification/v1034_parent_mirror.py](../../../../verification/v1034_parent_mirror.py#L1) · explicit_file_citation
- [verification/v1033_charged_disorder.py](../../../../verification/v1033_charged_disorder.py#L1) · explicit_script_identifier
- [verification/v1032_covariant_curvature.py](../../../../verification/v1032_covariant_curvature.py#L1) · explicit_file_citation
- [verification/v1035_matter_coupling.py](../../../../verification/v1035_matter_coupling.py#L1) · explicit_file_citation
- [verification/v1031_quantum_tensor_curvature.py](../../../../verification/v1031_quantum_tensor_curvature.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v1035: physical-position Fourier convention D -> i k. Retain I: c0=-s.q and c_i=i (B p)_i. The source Ward equations then propagate both affine constraints exactly. *)](../../../../verification/wolfram/tfpt_round7.wl#L181)
- [(* v1033: exact Z4 deck algebra and the load-bearing weight mismatch. *) z4 = DiagonalMatrix[{1, I, -1, -I}]; x4 = Sum[SparseArray[{{Mod[col, 4] + 1, col} -> 1}, {4, 4}], {col, 1, 4}]; check["v1033 local flux register is an exact Z4 Weyl pair", zeroQ[MatrixPower[z4, 4] - IdentityMatrix[4]] && zeroQ[MatrixPower[x4, 4] - IdentityMatrix[4]] && zeroQ[z4.x4.ConjugateTranspose[z4] - I x4]]; qDeck = ConstantArray[1/4, 8]; check["v1033 common quarter deck charge has norm 1/2 and h=1/4", qDeck.qDeck === 1/2 && qDeck.qDeck/2 === 1/4]; omegaS = ConstantArray[1/2, 5]; omegaF = Join[{3/4}, ConstantArray[-1/4, 3]]; lambdaNorm2 = omegaS.omegaS + omegaF.omegaF; check["v1033 D5+A3 lambda has h=1, distinct from deck h=1/4", omegaS.omegaS === 5/4 && omegaF.omegaF === 3/4 && lambdaNorm2 === 2 && lambdaNorm2/2 === 1 && lambdaNorm2/2 =!= qDeck.qDeck/2]; (* v1034: exact source parent envelope. The source's 3/5 is a dispersion amplitude; a standard symmetric NN bond has half of it. *)](../../../../verification/wolfram/tfpt_round7.wl#L141)
- [(* v1031: exact rational-fibre curvature projector and positivity. *) p = {1, 2, 2}; {r2, b, trace, scalar, kp, kq, c} = tensorData[p]; ptt = Simplify[explicitPTT[p, r2]]; check["v1031 C=r^4 PTT with a symmetric rank-two projector", zeroQ[c - r2^2 ptt] && zeroQ[ptt - Transpose[ptt]] && zeroQ[ptt.ptt - ptt] && MatrixRank[ptt] === 2]; cFactor = r2 ptt; check["v1031 exact PSD factorization has spectrum {0^4,r^4,r^4}", zeroQ[c - cFactor.Transpose[cFactor]] && MatrixRank[c] === 2 && Sort[Simplify[Eigenvalues[c]]] === {0, 0, 0, 0, r2^2, r2^2}]; (* v1032: a separate Lorentz-covariant curvature calculation at one exact nonzero null momentum. Pi is the de Donder trace-reversed numerator; positivity is inferred only after the curvature sandwich. *)](../../../../verification/wolfram/tfpt_round7.wl#L79)

## =150 2026-08-31 (CXLIX) (Monday-morning harvest — axiom-core closure [formula in source] state/gap batteries graduate as v1015– v1016; suite [formula in source] , ledger [formula in source] no new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v1014, engine still DEFERRED_NO_ENGINE). (1) v1015_ axiom_ core_ closure.py ( [formula in source] ): character-blind P-dem response DERIVED — [formula in source] exactly at collar sizes [formula in source] and [formula in source] , democracy residual [formula in source] ; mutants split [formula in source] and [formula in source] . Together with P-anch (v1014) BOTH W-bridge premises are derived at finite level; the axiom-core remainder is ZERO modulo the externalized MMST identification. AX.P2.01 stays an axiom (finite shadows; continuum identification is the same external leg). T1 note on TFPT.TOE.COMPLETE.01: the structure-postulate route is now fully premise-supported at finite level. (2) v1016_ state_ gap_ batteries.py ( [formula in source] ): [formula in source] seam-modular cap is the unique finite-level non-entropic selector ( [formula in source] , SK RMS [formula in source] , [formula in source] saddle preserved; finite-proxy caveat; FTRANSFER.SK.RHO0.01 stays ). TEL-B certified-tail BLOCKED ( [formula in source] [formula in source] , UV-supported remainder); strictly smaller external target [formula in source] with factor- [formula in source] measured headroom; [formula in source] -uniform CAR nuclearity PROVED ( [formula in source] ) as ALG specialist input; ALG-EXH unchanged ( SEAM.MMST.TYPEIII.CHARGED.01 stays ). DFP volume-uniform gap cited-verified for [formula in source] open chains ( [formula in source] , [formula in source] ); dynamical-link leg closed at that level; remaining rotor/wall/ [formula in source] D ( CHIRAL4D.MIRROR.DET16.01 stays ). Surfaces: tfpt_research_contracts executed-update paragraphs (five items [formula in source] L1 nuclearity note); tfpt_4_frontier [formula in source] introduction Monday-morning note; MMST handoff HTML update-2026-08-31 block; website papers.ts / VerificationDag.

[documents/changelog/sections/001-source.tex:282-283](../../../../documents/changelog/sections/001-source.tex#L282) · `section:8c44b477c1ab034d5ccf` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1015_axiom_core_closure.py](../../../../verification/v1015_axiom_core_closure.py#L1) · explicit_script_identifier
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_script_identifier
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_script_identifier
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row

## =150 2026-08-30 (CXLVIII) (late-evening harvest — thermodynamic-dynamics theorem [formula in source] detline/W-bridge refinements graduate as v1013– v1014; suite [formula in source] , ledger [formula in source] no new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v1012, engine still DEFERRED_NO_ENGINE). (1) v1013_ thermodynamic_ dynamics.py ( [formula in source] ): the mandatory-dynamics leg of QFT4D.LATTICE.FUNDAMENTAL.01 is CLOSED at Hamiltonian-class level. Cited articles/ 2026-08-30/ tfpt_ thermodynamic_ dynamics_ en.tex/ .pdf: uniform Lieb–Robinson bound [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] ; norm-convergent [formula in source] ; gauge-invariant quasilocal [formula in source] (Gauss caveat resolved on the invariant subalgebra); existence of ground and [formula in source] -KMS states. Numeric twin: measured [formula in source] proved bound; analytic finite-volume bound dominates nested differences at buffers [formula in source] ; [formula in source] mutant ratio [formula in source] ; Gauss-positive control commutes, violating embedding has commutator norm [formula in source] . Remaining: phase uniqueness, limit gap, IR universality. Decision typing UNCHANGED. (2) v1014_ bridge_ refinements.py ( [formula in source] ): finite detline restriction isomorphism VERIFIED ( [formula in source] constancy [formula in source] , conjugation covariance exact, [formula in source] / mirror [formula in source] ); orientation fixes only the conjugate branch ( [formula in source] ); the residual constant [formula in source] is the [formula in source] reference normalization — recorded on ALPHA.QUILLEN.EXACT.01. W-bridge: P-anch DERIVED ( [formula in source] via the winding lock); P-dem PARTIAL (the [formula in source] average annihilates the nontrivial character space); missing object [formula in source] the character-blind determinant-response map — the same MMST/Quillen externalized leg as TEL-B/ALG-EXH/P1. AX.P2.01 stays an axiom. Convergence: every remaining axiom-core and continuum gap now runs through ONE externalized theorem. Surfaces: tfpt_research_contracts executed-update paragraphs; tfpt_4_frontier [formula in source] introduction late-evening note; website papers.ts / VerificationDag.

[documents/changelog/sections/001-source.tex:284-285](../../../../documents/changelog/sections/001-source.tex#L284) · `section:62b5d88e8412144c1f8b` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_file_citation
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_script_identifier
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1013_thermodynamic_dynamics.py](../../../../verification/v1013_thermodynamic_dynamics.py#L1) · explicit_script_identifier
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row

## =150 2026-08-30 (CXLVII) (evening TOE-gate wave — four executed witnesses graduate as v1012; suite [formula in source] , ledger [formula in source] no new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v1011). v1012_ toe_ gate_ witnesses.py ( [formula in source] ): T5 IR universality on the physical QWZ edge — [formula in source] (limit [formula in source] ), clustering dichotomy [formula in source] vs power-law exponent [formula in source] , Lieb–Robinson cone [formula in source] with leakage [formula in source] , cubic curvature [formula in source] with volume; TYPED SPLIT: gauge holonomy [formula in source] seam clock are not propagating modes, so the common- [formula in source] test needs dynamical gauge excitations. T8 [formula in source] eight-candidate table ALL unique; hard sectors kill the SK response ( [formula in source] ); every response-alive set is exactly [formula in source] even without [formula in source] — entropic-proximity selection is VACUOUS at finite level; verdict NO_SET_WORKS with the double diagnosis; binding requirement [formula in source] a non-entropic principle (Euclidean-cap / orientation-branch). T6 [formula in source] six-fold NULL: six pre-declared D4-odd candidates, all parity-checked, all NULL (five at [formula in source] ; [formula in source] is [formula in source] too large); the [formula in source] cancellation requires the true [formula in source] D functional — third and final scaffold-level nu-mechanism bound this week. T7 interacting TT: conserved interaction-complete lattice stress [formula in source] , TT spectral positivity exact, sum rules [formula in source] , dominant positive- [formula in source] pole persists under [formula in source] (gapped); [formula in source] trend [formula in source] suppressed [formula in source] / [formula in source] enhanced [formula in source] ; free analytic match. Missing: TFPT content, [formula in source] volume scaling, Ward identities. Ledger notes only on TFPT.TOE.COMPLETE.01, FTRANSFER.SK.RHO0.01, FLAV.NU.TEXTURE.MECHANISM.01, GRAV.SPIN2.EMERGENCE.01 (all stay ). Surfaces: tfpt_research_contracts executed-update paragraphs; tfpt_4_frontier [formula in source] introduction evening-wave note; website papers.ts / VerificationDag.

[documents/changelog/sections/001-source.tex:286-287](../../../../documents/changelog/sections/001-source.tex#L286) · `section:a1b31833986dad8762ee` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_script_identifier
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NU.TEXTURE.MECHANISM.01](../../../../verification/status_ledger.csv#L768) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_script_identifier
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier

## =150 2026-08-30 (CXLVI) (afternoon harvest — simplicity campaign [formula in source] [formula in source] D ladder graduate as v1010– v1011; suite [formula in source] , ledger [formula in source] no new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v1009). (1) v1010_ simplicity_ bridge_ census.py ( [formula in source] ): derivation matrix over four frozen seeds, unique remainder min [formula in source] ; anchor [formula in source] is not among the three declared Milnor maps; [formula in source] four novel candidates NULL. Bridge [formula in source] CANONICAL — the bit-selector ladder forces [formula in source] and family [formula in source] forces [formula in source] column sums [formula in source] ; [formula in source] 's carrier-looking [formula in source] is inherited from [formula in source] column [formula in source] , not inserted (the v1005 circularity flag is corrected as forced provenance). Bridge [formula in source] CHOICE-but-conditionally-unique: spectrum [formula in source] alone has [formula in source] solutions; democratic-image [formula in source] carrier-anchor kernel leave exactly the corpus shift (count [formula in source] ); remaining obligation [formula in source] seam-geometric derivation of those two directional premises. Milnor strong all-structure bridge NONEXISTENT at [formula in source] (clock [formula in source] vs [formula in source] , CP rank [formula in source] vs [formula in source] ) and at every upstairs home ( [formula in source] , Gaussian [formula in source] , affine); only the coarse [formula in source] -module [formula in source] pairing bridge exists (witness constructed; [formula in source] , [formula in source] ). Ring-internal identities of v1004 (rank clock, socle CP, self-clock) unaffected. SEAM.MILNOR.LOCALRING.01 stays \ (canonical status SHARPENED); AX.P2.01 stays an axiom (pencil rehabilitated, W premises remain). (2) v1011_ 3p1d_ ladder_ battery.py ( [formula in source] ): B6–B9 compressed — minimal [formula in source] D viable (exact Gauss [formula in source] , confinement [formula in source] vs [formula in source] , exact in-face isotropy, [formula in source] ); exact tree-fixing [formula in source] with tree-independence [formula in source] ; DET survives coupling; back-reaction; periodicity restores holonomy [formula in source] ; charged channels [formula in source] at weak [formula in source] ; charge- [formula in source] control matches B8 to [formula in source] ; [formula in source] collapses above [formula in source] . BINDING: the matching point of the coupling functional must sit in the deconfined/weak regime. QFT4D.LATTICE.FUNDAMENTAL.01 Decision typing UNCHANGED (Kronecker limitation removed); GAUGE.DETLINE.FIXPOINT.01 stays \ with the matching-scale constraint recorded. Surfaces: tfpt_research_contracts executed-update paragraphs (MILNOR sharpening, P2 rehabilitation, QFT4D ladder, DETLINE matching-scale); tfpt_4_frontier [formula in source] introduction afternoon note; website papers.ts / VerificationDag.

[documents/changelog/sections/001-source.tex:288-289](../../../../documents/changelog/sections/001-source.tex#L288) · `section:86d6234f384db2b3c770` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1009_rho0_minimizer.py](../../../../verification/v1009_rho0_minimizer.py#L1) · explicit_script_identifier
- [verification/v1004_milnor_frobenius_gray.py](../../../../verification/v1004_milnor_frobenius_gray.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [verification/v1010_simplicity_bridge_census.py](../../../../verification/v1010_simplicity_bridge_census.py#L1) · explicit_file_citation
- [SEAM.MILNOR.LOCALRING.01](../../../../verification/status_ledger.csv#L769) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_file_citation
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1005_relative_pencil_bridges.py](../../../../verification/v1005_relative_pencil_bridges.py#L1) · explicit_script_identifier

## =150 2026-08-30 (CXLV) (review wave 7 — four exploration strands graduate as v1006– v1009: the MMST lemma battery, the DET16 stability battery, the [formula in source] D master-object assembly scaffold, and the [formula in source] constrained minimizer; suite [formula in source] , ledger [formula in source] no new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v1005). (1) v1006_ mmst_ lemma_ battery.py ( [formula in source] ): five lemmas in-house on SEAM.MMST.TYPEIII.CHARGED.01 \ — L3 crossed-product; UGF [formula in source] (measured plateau [formula in source] , max measured [formula in source] [formula in source] at [formula in source] ); TEL-a [formula in source] with exact isometries ( [formula in source] , measured envelope [formula in source] ); integer D5+A3 pairings; [formula in source] outerness in the limit [formula in source] finite-inner correction. Residual boxed: TEL-B-EXTERNAL (Hankel [formula in source] ; HS remainder sourced from the paper max [formula in source] / fit [formula in source] / v998 bound [formula in source] , not recomputed) [formula in source] ALG-EXH (two Buchholz–Verch estimates). Display stays . Cited articles/2026-08-30/mmst_charged_scaling_limit_en.tex ( [formula in source] pp) [formula in source] externalization_mmst_handoff_v2_en.html. (2) v1007_ det16_ stability_ battery.py ( [formula in source] ): T1/T2 proved (v1002); T3 Michalakis–Zwolak cited-verified (LTQO, [formula in source] , gap [formula in source] ). Counting line [formula in source] ; [formula in source] closing scan through [formula in source] ; dynamical [formula in source] uniquely gapped (full-probe min [formula in source] pinned; compressed suite). SW [formula in source] ; [formula in source] bounded. [formula in source] boxed (ordinary hopping not block-diagonal); BDL boxed (no volume-uniform gap remainder). CHIRAL4D.MIRROR.DET16.01 stays ; CHIRAL4D.NOMIRROR.01 unmoved. Cited articles/2026-08-30/det16_mirror_gap_theorem_en.tex. (3) v1008_ master_ assembly_ scaffold.py ( [formula in source] ): [formula in source] D master-object scaffold-coherent — combinatorial [formula in source] ; frozen-link [formula in source] , [formula in source] ; unique-contractive [formula in source] ; QWZ wall slope [formula in source] , DET gap [formula in source] through [formula in source] ; assembly [formula in source] [formula in source] , clock [formula in source] . [formula in source] spaces [formula in source] / [formula in source] out of suite. Decision QFT4D.LATTICE.FUNDAMENTAL.01 and GAUGE.DETLINE.FIXPOINT.01 \ unmoved. (4) v1009_ rho0_ minimizer.py ( [formula in source] ): finite uniqueness of the KMS compression (Klein); Hessian strictly positive; centre dim [formula in source] ; identity [formula in source] . TYPED: V1000_CONSEQUENCE_MISMATCH (compression kills the SK response vs frozen contrast [formula in source] ) [formula in source] CENTER_FLATNESS_PREMISE_FALSE. Canonical formula needs a weaker admissible set. FTRANSFER.SK.RHO0.01 stays . Surfaces: tfpt_research_contracts executed-update paragraphs; tfpt_4_frontier wave-7 paragraph; introduction status card; website papers.ts / VerificationDag.

[documents/changelog/sections/001-source.tex:290-291](../../../../documents/changelog/sections/001-source.tex#L290) · `section:710760dba8520599a644` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1006_mmst_lemma_battery.py](../../../../verification/v1006_mmst_lemma_battery.py#L1) · explicit_file_citation
- [verification/v998_seam_modular_closure.py](../../../../verification/v998_seam_modular_closure.py#L1) · explicit_script_identifier
- [verification/v1008_master_assembly_scaffold.py](../../../../verification/v1008_master_assembly_scaffold.py#L1) · explicit_file_citation
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1007_det16_stability_battery.py](../../../../verification/v1007_det16_stability_battery.py#L1) · explicit_file_citation
- [verification/v1009_rho0_minimizer.py](../../../../verification/v1009_rho0_minimizer.py#L1) · explicit_script_identifier
- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_script_identifier
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [verification/v1005_relative_pencil_bridges.py](../../../../verification/v1005_relative_pencil_bridges.py#L1) · explicit_script_identifier

## =150 2026-08-30 (CXLIV) (review wave 6 — two exploration probes graduate as v1004– v1005 plus two registrations and display corrections: the Milnor–Frobenius–Gray finite algebra, the circularity-flagged relative pencil, the local-ring identification contract, the Weinberg–Witten spin-2 firewall, and honest rest/SM/gravity wording; suite [formula in source] , ledger [formula in source] : two new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v1003). (1) v1004_ milnor_ frobenius_ gray.py ( [formula in source] ): CLASSICAL (cite, no claim) — Milnor algebra of [formula in source] dimension [formula in source] , spectral numbers [formula in source] [formula in source] exponents [formula in source] . NEW-IN-CORPUS EXACT -finite: rank clock [formula in source] table-sum [formula in source] ; [formula in source] ; self-clock iff [formula in source] ; [formula in source] unique among ordered spherical triples; Galois–Gray [formula in source] (binary Gray order [formula in source] ); CP [formula in source] socle/Frobenius; integral dual-number bridge [formula in source] free rank [formula in source] over [formula in source] , basis-dependent. INTERPRETIVE : [formula in source] . Mutants: [formula in source] [formula in source] ; [formula in source] self-clock survives but exponents fail; wrong socle rank [formula in source] . NEW ledger row SEAM.MILNOR.LOCALRING.01 : required canonical geometric/mechanical identification of the raw seam collar / [formula in source] transition bus with [formula in source] preserving dual-number action, Frobenius pairing, Gray torsor, deck action and CP (rank clock and socle-CP as outputs); kill [formula in source] second inequivalent identification or [formula in source] -equivariance failure; currently \ because Milnor algebra [formula in source] exponents are classical and the corpus map is unproven. (2) v1005_ relative_ pencil_ bridges.py ( [formula in source] ): EXACT -finite Hankel [formula in source] [formula in source] Jacobi spec [formula in source] diag [formula in source] (v106/v119) and winding spec [formula in source] [formula in source] fixed plane (v4). EXACT BUT CIRCULARITY-FLAGGED : unique [formula in source] , [formula in source] , factorisation [formula in source] , CM [formula in source] , dual number mod [formula in source] , index [formula in source] SNF [formula in source] — BUT carrier [formula in source] already sits in the column sums of [formula in source] and [formula in source] : NOT a P2 selector until [formula in source] , [formula in source] , [formula in source] are derived from seam geometry independently; AX.P2.01 typing UNCHANGED. INTERPRETIVE : Klein-four SNF [formula in source] only after [formula in source] (side-blind nulls v521, not a theorem). Mutants: [formula in source] fails; perturbed [formula in source] breaks factorisation; [formula in source] breaks Hankel. (3) registrations (no marker moves). NEW GRAV.WEINBERG.WITTEN.01 : binding firewall BEFORE any spin-2 marker move — the microscopic Hamiltonian family must NOT possess a fundamental Lorentz-covariant local conserved [formula in source] ; Lorentz, diffeomorphism Ward identities and the spin-2 mode must emerge in the SAME IR limit; acceptance [formula in source] positive TT density, two helicities, massless pole, emergent diff Ward, universal soft coupling, named evaded Weinberg–Witten premise; kill [formula in source] microscopic covariant local [formula in source] together with a massless composite spin-2 claim; child of T7, cross-link GRAV.SPIN2.EMERGENCE.01 (not back). (4) display corrections (honest wording, no claim changes). Status-at-a-glance: compiler rest [formula in source] now sits NEXT TO the strict-physical-TOE rest (ten-component [formula in source] / eight TFPT.TOE.COMPLETE.01 gates, one line). SM completeness retyped: the discrete Standard-Model structure (charges, families, flavor operators) is derived under the axioms; [formula in source] D existence, chiral measure, mirror gap, couplings and neutrino dynamics are open. Gravity display: ``parameter-free'' headlines replaced by ``the classical covariant field equation carries no free dimensionless Newton coupling under the named QFT/entanglement premises ''. Surfaces: tfpt_research_contracts (new sections MILNOR.LOCALRING, WEINBERG.WITTEN; SPIN2 firewall note; T7 child; v358/v359 keybox titles); tfpt_4_frontier wave-6 paragraph; introduction status card [formula in source] SM/gravity lines; tfpt_2 gravity heading [formula in source] conclusion; website StatusMatrix / WhatTfptClaims / ClaimStack / GravityEmergence / OpenGates / VerificationDag.

[documents/changelog/sections/001-source.tex:292-293](../../../../documents/changelog/sections/001-source.tex#L292) · `section:89a96ea40df8ee1ce3c8` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v119_review_validation_2.py](../../../../verification/v119_review_validation_2.py#L1) · explicit_script_identifier
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.WEINBERG.WITTEN.01](../../../../verification/status_ledger.csv#L770) · explicit_claim_identifier · original status at linked ledger row
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v1003_nu_structural_nulls.py](../../../../verification/v1003_nu_structural_nulls.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v1005_relative_pencil_bridges.py](../../../../verification/v1005_relative_pencil_bridges.py#L1) · explicit_script_identifier
- [verification/v1004_milnor_frobenius_gray.py](../../../../verification/v1004_milnor_frobenius_gray.py#L1) · explicit_file_citation
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [verification/v106_review_validation.py](../../../../verification/v106_review_validation.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v521_seam_bit_rp_blind.py](../../../../verification/v521_seam_bit_rp_blind.py#L1) · explicit_script_identifier
- [SEAM.MILNOR.LOCALRING.01](../../../../verification/status_ledger.csv#L769) · explicit_claim_identifier · original status at linked ledger row
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v521 round: SEAM.BIT.RPBLIND.01 -- "free OS positivity does not see delta": the anti-linear census solvesets on M(delta), the counterwitness census, the V4 -> D4 closure (face #13), the cut/mark incidence, the continuum axis elimination + Cauchy-Stieltjes factorisation, the clock-tower clause and the hex/silver precondition controls. The 40-digit lattice Gram inertia spectra (N = 16 / N = 32) are Python-only by the suite convention. Mirrors v521. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7479)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)

## =150 2026-08-29 (CXLIII) (review wave 5 — two exploration probes graduate as v1002– v1003 plus three registrations: the DET16 finite-cluster hit, the two neutrino-texture structural nulls, the master scaling-limit theorem SEAM.MMST.TYPEIII.CHARGED.01, the gauge-stiffness step-scaling divergence, and the holomorphic-KMS document; suite [formula in source] , ledger [formula in source] : three new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v1001). (1) v1002_ spin10_ mirror_ projector.py ( [formula in source] ): DET16 rank-one projector on the full [formula in source] cluster — [formula in source] , [formula in source] , defect [formula in source] ; [formula in source] hermitian idempotent [formula in source] , rank [formula in source] ; [formula in source] spectrum [formula in source] , gap exactly [formula in source] ; all [formula in source] [formula in source] Fock commutators [formula in source] ( [formula in source] ); parity commutator [formula in source] ; [formula in source] and [formula in source] singlets. Hopping stability on the [formula in source] -mode analogue: gap [formula in source] ( [formula in source] clusters) / [formula in source] ( [formula in source] clusters) at [formula in source] ; spectators untouched. NEW ledger row CHIRAL4D.MIRROR.DET16.01 Candidate \ (exact finite-cluster gapping; open: dynamical gauge fields, domain-wall geometry, [formula in source] D volume theorem). (2) the Casimir kill, permanent. Number-preserving Casimir projector uniqueness fails at every cluster size: one [formula in source] (none at [formula in source] ); [formula in source] half-filling multiplicity [formula in source] ; [formula in source] (exact Weyl alternation, [formula in source] ). Ledger note on CHIRAL4D.NOMIRROR.01: number-preserving Casimir projector route excluded; display stays . (3) v1003_ nu_ structural_ nulls.py ( [formula in source] ): charged-sector data [formula in source] , [formula in source] ; Schur-texture NULL — all [formula in source] preregistered [formula in source] fail, D4 reflection forces [formula in source] , hierarchy [formula in source] structurally unreachable from D4-even seam data, required [formula in source] matches none of [formula in source] comparators; orientation-doubling structure theorem — [formula in source] odd sector generically lifts the degeneracy (exact rational witness); scale NULL — [formula in source] fail, required cancellation [formula in source] not supplied, [formula in source] -branches isospectral. NEW ledger row FLAV.NU.TEXTURE.MECHANISM.01 : both nulls are binding constraints (mechanism must be D4-odd AND supply a [formula in source] even-odd cancellation; pure seam data excluded -typed). FLAV.NUSCALE.05/ .06 notes only; candidates unmoved. (4) registrations (no marker moves). NEW SEAM.MMST.TYPEIII.CHARGED.01 : ONE scaling-limit theorem [formula in source] strongly on the finite-energy core [formula in source] crossed-product continuity, from which [formula in source] , [formula in source] , type III [formula in source] , unique rotational KMS, unique CE, deck equidistribution and modular invariance follow as corollaries; children SEAM.SIMPLECURRENT.GENERATOR.01, SEAM.STATE.RPMIXING.01 continuum, ALPHA.QUILLEN.EXACT.01 rigidity, AX.P1.01 reading (listed on the parent, not back). Cited document articles/2026-08-29/holomorphic_kms_extension_en.tex ( [formula in source] pp): unconditional rotational-KMS uniqueness via KLM [formula in source] Longo–Tanimoto GIVEN the identification; P1 [formula in source] theorem-conditional on seam identification [formula in source] [formula in source] ; axiom typing UNCHANGED. GAUGE.DETLINE.FIXPOINT.01: mechanism executed at fixed volume (unique fixed point, contraction [formula in source] , exact [formula in source] and [formula in source] Dynkin ratio [formula in source] ) BUT the preregistered thermodynamic step-scaling [formula in source] is DIVERGENT ( [formula in source] oscillates [formula in source] , [formula in source] at [formula in source] ); typed hurdle: the [formula in source] D toy has no plaquette self-interaction, the real contract needs [formula in source] D; display stays . [formula in source] boundary note: unit choice closed; dimensionless hierarchies [formula in source] remain predictive obligations. Surfaces: tfpt_research_contracts (new sections MIRROR.DET16, TYPEIII.CHARGED, NU.TEXTURE.MECHANISM; DETLINE stiffness update; NOMIRROR Casimir kill); tfpt_4_frontier wave-5 paragraph; tfpt_2 (texture-mechanism note); introduction status card [formula in source] hierarchy sentence.

[documents/changelog/sections/001-source.tex:294-295](../../../../documents/changelog/sections/001-source.tex#L294) · `section:5a8078e84394b902d12b` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1001_nu_pentagon_chain.py](../../../../verification/v1001_nu_pentagon_chain.py#L1) · explicit_script_identifier
- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_script_identifier
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [verification/v1003_nu_structural_nulls.py](../../../../verification/v1003_nu_structural_nulls.py#L1) · explicit_file_citation
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NU.TEXTURE.MECHANISM.01](../../../../verification/status_ledger.csv#L768) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row

## =150 2026-08-29 (CXLII) (review wave 4 — four exploration probes graduate as v998– v1001 plus the lattice-fundamental quasilocal-family amendment, the [formula in source] closed-metrology retype, the ALPHA.QUILLEN relative-determinant note, and the master contract TFPT.TOE.COMPLETE.01; suite [formula in source] , ledger [formula in source] : two new rows, existing contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v997). (1) v998_ seam_ modular_ closure.py ( [formula in source] ): two-edge HS remainder bounded by [formula in source] on the frozen plateau [formula in source] ; lattice character [formula in source] EXACT four orders [formula in source] ; [formula in source] as Eisenstein series, [formula in source] -expansion match to [formula in source] orders exact (Jacobi identity; the reviewer's C7 sharpening); [formula in source] numeric transform at [formula in source] digits with [formula in source] -weight bookkeeping. Ledger notes on SEAM.EQUIV.MMST.01 and SEAM.SIMPLECURRENT.GENERATOR.01: C7 arithmetic shadow now exact; net-level C7 stays cited/open. (2) v999_ weak_ collision_ hp.py ( [formula in source] ): the continuous-time dilation leg — generator extraction Richardson [formula in source] ; [formula in source] symbolic; [formula in source] exact; GNS splitting defect [formula in source] ; locality [formula in source] ; strong-collision singularity contrast rank [formula in source] . DYN.UNITARY.DILATION.01: the finite ladder is now COMPLETE (discrete/kernel/field-free/interacting-classical/quantum-coupled/continuous-time); open [formula in source] the thermodynamic field limit only; contract stays . (3) v1000_ spin2_ sk_ witnesses.py ( [formula in source] ): lattice graviton — positivity exact, [formula in source] TT helicities at all [formula in source] momenta ( [formula in source] ), [formula in source] exact; SK — KMS/FDT [formula in source] , [formula in source] -dependence contrast [formula in source] vs static [formula in source] , saddle [formula in source] -fold degenerate with [formula in source] unique in the [formula in source] lift . GRAV.SPIN2.EMERGENCE.01 quadratic Hamiltonian half executed; FTRANSFER.SK.RHO0.01 mechanism executed; both contracts stay . (4) v1001_ nu_ pentagon_ chain.py ( [formula in source] ): [formula in source] inventory theorem; misalignment [formula in source] ; pentagon double hit [formula in source] frozen, all three measured angles [formula in source] (honest max pull [formula in source] ) at [formula in source] , unique LEE survivor [formula in source] ; v3 chain SHA-16 a4c28732fa687620 with [formula in source] eV, [formula in source] meV, [formula in source] meV, [formula in source] ; v270– [formula in source] tension [formula in source] TYPED; census null [formula in source] . NEW ledger row FLAV.NUSCALE.06 Candidate \ (pentagon-class misalignment; mechanism [formula in source] the [formula in source] -to-flavor operator ; kills DESI/DUNE [formula in source] vs [formula in source] /JUNO). NO seesaw closure; FLAV.NUSCALE.05 unmoved. (5) Amendments (typed; no marker moves). QFT4D.LATTICE.FUNDAMENTAL.01: a single finite box is not a world — the fundamental object is the quasilocal consistent family [formula in source] with [formula in source] ; continuum ( [formula in source] ) optional, thermodynamic limit and controlled IR universality mandatory (dated 2026-08-29). ANCHOR.VGEO.01/ .02: display retyped from open-physics/primitive phrasing to CLOSED METROLOGY STRUCTURE ( [formula in source] unit torsor; one dimensionful calibration necessary by dimensional analysis — No-Unit v153/ v725); display stays , no physical . ALPHA.QUILLEN.EXACT.01: the correct object is the relative determinant [formula in source] ; BFK [formula in source] is [formula in source] -independent at fixed cut number so [formula in source] — no physical compensation (consistent with COMPENSATION_INTERNAL). NEW master contract TFPT.TOE.COMPLETE.01 : eight gates T1–T8 with the binding separation [formula in source] vs [formula in source] AND independent holdouts; every existing [formula in source] D/dilation/detline/SK/flavor/gravity contract is a child of one gate. Surfaces: tfpt_research_contracts (executed-update paragraphs at MMST/SIMPLECURRENT, DILATION, GRAV.SPIN2, SK.RHO0; new sections TOE.COMPLETE and NUSCALE.06; lattice-fundamental amendment; ALPHA relative-det note); tfpt_4_frontier [formula in source] introduction status card / [formula in source] row; tfpt_2 (NUSCALE.06 candidate paragraph).

[documents/changelog/sections/001-source.tex:296-298](../../../../documents/changelog/sections/001-source.tex#L296) · `section:970b604e67143eb148a6` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [verification/v999_weak_collision_hp.py](../../../../verification/v999_weak_collision_hp.py#L1) · explicit_file_citation
- [verification/v997_spin2_smg_witnesses.py](../../../../verification/v997_spin2_smg_witnesses.py#L1) · explicit_script_identifier
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1000_spin2_sk_witnesses.py](../../../../verification/v1000_spin2_sk_witnesses.py#L1) · explicit_file_citation
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v998_seam_modular_closure.py](../../../../verification/v998_seam_modular_closure.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.06](../../../../verification/status_ledger.csv#L765) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v725_phys_vgeo_torsor_audit.py](../../../../verification/v725_phys_vgeo_torsor_audit.py#L1) · explicit_script_identifier
- [verification/v1001_nu_pentagon_chain.py](../../../../verification/v1001_nu_pentagon_chain.py#L1) · explicit_file_citation
- [ANCHOR.VGEO.01](../../../../verification/status_ledger.csv#L144) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [(* ---- (v997) GRAV.SPIN2.EMERGENCE.01: Barnes-Rivers ranks (5,3,1,1) ---- Python-only: Weyl^2 ghost residues, random-p numeric, SMG N=8 Fidkowski-Kitaev toy (spectrum / Spin(7) / Schmidt / edge). *)](../../../../verification/wolfram/tfpt_readouts.wl#L699)

## =150 2026-08-28 (CXLI) (the completeness wave — four exploration probes graduate as v994– v997 (suite [formula in source] , ledger [formula in source] : eight contract rows updated, NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v993). (1) v994_ mmst_ criteria_ battery.py ( [formula in source] ): [formula in source] of [formula in source] MMST identification criteria executed -measured — measured [formula in source] (16 Majorana copies), conformal edge spectrum [formula in source] , current normalisation [formula in source] , sector collapse [formula in source] , and the flagship: [formula in source] /GSO-projected lattice character sums reproduce the [formula in source] vacuum character [formula in source] three orders deep; C6 is now written out in articles/2026-08-28/psi_lambda_convergence_theorem_en.tex (analytic log coefficient [formula in source] vs measured [formula in source] , [formula in source] ); C7 modular invariance stays cited/open. Ledger notes on SEAM.EQUIV.MMST.01 (stays ) and SEAM.SIMPLECURRENT.GENERATOR.01 (stays ; open rest [formula in source] C7 [formula in source] net G2/G3/G4). (2) v995_ kms_ subnet_ rigidity.py ( [formula in source] ): all [formula in source] v972 mixing directions killed by KMS alone on finite [formula in source] ; covariance provably redundant; unique [formula in source] -invariant crossed-product extension [formula in source] . SEAM.STATE.RPMIXING.01 finite KMS rigidity ; type-III/continuum stays . (3) v996_ gauge_ grammar_ kill.py ( [formula in source] ): H0 structural kill — negative [formula in source] flip the stationary-root signs ( [formula in source] inverse [formula in source] , [formula in source] [formula in source] ); [formula in source] conventions [formula in source] hits; [formula in source] control [formula in source] survives all mutants; detline curvature [formula in source] exponentially with rate [formula in source] (numerical Bismut–Freed shadow). GAUGE.DETLINE.FIXPOINT.01 naive grammar excluded ; genuinely nonabelian structure required — typed; [formula in source] remains an external input; contract stays . (4) v997_ spin2_ smg_ witnesses.py ( [formula in source] ): Barnes–Rivers quadratic decomposition — [formula in source] clean (one massless TT pole, two helicities, scalaron at [formula in source] exact); the local [formula in source] Weyl [formula in source] truncation necessarily carries an opposite-residue spin-2 ghost — typed; FK SMG toy: [formula in source] unique [formula in source] -singlet ground state, Schmidt rank [formula in source] , volume-independent gap [formula in source] at [formula in source] ; [formula in source] contrast [formula in source] -degenerate; physical chiral edge keeps [formula in source] exactly. GRAV.SPIN2.EMERGENCE.01 quadratic witnesses , content pinned on the untruncated form factor; CHIRAL4D.NOMIRROR.01 SMG toy-proved , [formula in source] D [formula in source] stays ; both contracts stay . Canonical note (not a module) on FLAV.NUSCALE.05: NU_TEXTURE_CENSUS_NULL [formula in source] — frozen [formula in source] inventory provably insufficient; mechanism \ sharpened. Surfaces: tfpt_research_contracts (executed-update paragraphs at MMST/SIMPLECURRENT, RPMIXING, GAUGE.DETLINE.FIXPOINT.01, GRAV.SPIN2.EMERGENCE.01, CHIRAL4D.NOMIRROR.01, ALPHA.QUILLEN rigidity/ln-2 notes); tfpt_2 (census-null note); tfpt_4_frontier [formula in source] introduction card addendum. Exploration record: articles/2026-08-28/big_picture_simplicity_first_en.md.

[documents/changelog/sections/001-source.tex:299-300](../../../../documents/changelog/sections/001-source.tex#L299) · `section:ccd38232c9f484cdbcb7` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v994_mmst_criteria_battery.py](../../../../verification/v994_mmst_criteria_battery.py#L1) · explicit_file_citation
- [verification/v993_minimal_defect_selector.py](../../../../verification/v993_minimal_defect_selector.py#L1) · explicit_script_identifier
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [verification/v996_gauge_grammar_kill.py](../../../../verification/v996_gauge_grammar_kill.py#L1) · explicit_file_citation
- [verification/v995_kms_subnet_rigidity.py](../../../../verification/v995_kms_subnet_rigidity.py#L1) · explicit_file_citation
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [verification/v972_seam_interaction_front.py](../../../../verification/v972_seam_interaction_front.py#L1) · explicit_script_identifier
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row
- [verification/v997_spin2_smg_witnesses.py](../../../../verification/v997_spin2_smg_witnesses.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [articles/2026-08-28/big_picture_simplicity_first_en.md](../../../../articles/2026-08-28/big_picture_simplicity_first_en.md#L1) · explicit_file_citation
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v997) GRAV.SPIN2.EMERGENCE.01: Barnes-Rivers ranks (5,3,1,1) ---- Python-only: Weyl^2 ghost residues, random-p numeric, SMG N=8 Fidkowski-Kitaev toy (spectrum / Spin(7) / Schmidt / edge). *)](../../../../verification/wolfram/tfpt_readouts.wl#L699)
- [(* ---- (v993) AX.P2.01 census: SNF disc groups, unique (D5,A3), [lambda]^2=[v], CE dims ---- Python-only: random CE axiom sampling on M_d^{Z4} / crossed product. *)](../../../../verification/wolfram/tfpt_readouts.wl#L557)
- [(* ---- (v994) SEAM.EQUIV.MMST.01 C3: Theta_E8 / eta^8 = {1,248,4124,34752} ---- Python-only: C1 entropy, C2 QWZ spectrum, C4 two-point numeric, C5 sector recombination beyond det, C6 cited, C7 open, GSO/N=8 must-fail combinatorics. *)](../../../../verification/wolfram/tfpt_readouts.wl#L680)

## =150 2026-08-28 (CXXXVIII) (the master-object wave, part 2 — the second external bird's-eye review (``one 4D lattice [formula in source] one seam simple current [formula in source] one unitary dilation [formula in source] one determinant line [formula in source] one [formula in source] '') adjudicated: its four machine-checkable candidate results verified and integrated as FOUR new modules (suite [formula in source] , ledger [formula in source] : one new row FLAV.NUSCALE.05; three contract rows updated, NO status-marker moves). (1) v983_ simple_ current_ generator.py: the SEAM.SIMPLECURRENT.GENERATOR.01 generator is identified — the glue vector [formula in source] with [formula in source] , [formula in source] , order 4 in the discriminant group [formula in source] of [formula in source] ; isotropic glue [formula in source] even unimodular rank-8 overlattice ( [formula in source] ); coset root census [formula in source] — the odd fusion powers of the ONE class carry the full [formula in source] spinor sector; kill tests (vector-class / mismatched glue) fire; holomorphy shadow [formula in source] vs [formula in source] at the lattice level; the analytic half (G1–G4) stays . (2) v984_ markov_ qca_ dilation.py: the DISCRETE leg of DYN.UNITARY.DILATION.01 realized constructively — the collision step [formula in source] is exactly unitary, the Stinespring identity [formula in source] holds symbolically, [formula in source] and six fresh ancillas give [formula in source] exactly (radius-1 collision band); must-fail fires ( [formula in source] ); typed remark AGAINST the review text: a reused mod-3 adder ancilla still reproduces the populations exactly; the continuous Hamiltonian/OS legs stay . (3) v985_ quillen_ channel_ swap.py: the v974 CHANNEL-SWAP face of ALPHA.QUILLEN.EXACT.01 resolved at the finite level by [formula in source] -character grading — the deck swap [formula in source] maps the jump spectrum [formula in source] onto the mark pattern [formula in source] exactly (odd swap fails), the graded [formula in source] difference is [formula in source] -free [formula in source] , the channelwise unit ratio is uniform [formula in source] ; continuum Bismut–Freed, KMS rigidity and the [formula in source] compensation stay . (4) v986_ nu_ scalaron_ rung.py: the SCALARON-TRACE RUNG [formula in source] GeV — a structured point INSIDE the v481 window, [formula in source] from the 1-loop requirement (the review claimed [formula in source] 1\%; the honest value is 1.8), [formula in source] sharper than the declined integer rung; exact ladder position [formula in source] , [formula in source] from the closed [formula in source] Clebsch door — adjacency TYPED, not consumed (v488 killed the Clebsch mechanism; the generation-blind scalaron trace is a different class, itself ); kill test [formula in source] eV; new row FLAV.NUSCALE.05 [C]/[N], no seesaw closure. The remaining review content is typed, not consumed: the axion line ( [formula in source] , [formula in source] ) and the Riemann–Roch carrier ARE the existing v185/v211/v189; the 4D action, chiral measure, OS package, bulk dictionary, determinant-line unification, [formula in source] , transduction matrix and joint likelihood stay open contracts exactly as registered on 2026-08-27. Paper surfaces: tfpt_research_contracts (three executed-update paragraphs), tfpt_2_standard_model (scalaron-trace rung paragraph).)

[documents/changelog/sections/001-source.tex:304-306](../../../../documents/changelog/sections/001-source.tex#L304) · `section:64a9e573649942dd32e9` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v985_quillen_channel_swap.py](../../../../verification/v985_quillen_channel_swap.py#L1) · explicit_file_citation
- [verification/v189_riemann_roch_carrier.py](../../../../verification/v189_riemann_roch_carrier.py#L1) · explicit_script_identifier
- [verification/v481_seesaw_carrier_ladder.py](../../../../verification/v481_seesaw_carrier_ladder.py#L1) · explicit_script_identifier
- [verification/v986_nu_scalaron_rung.py](../../../../verification/v986_nu_scalaron_rung.py#L1) · explicit_file_citation
- [verification/v211_axion_spine_angle.py](../../../../verification/v211_axion_spine_angle.py#L1) · explicit_script_identifier
- [verification/v984_markov_qca_dilation.py](../../../../verification/v984_markov_qca_dilation.py#L1) · explicit_file_citation
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v983_simple_current_generator.py](../../../../verification/v983_simple_current_generator.py#L1) · explicit_file_citation
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [verification/v488_majorana_clebsch_door.py](../../../../verification/v488_majorana_clebsch_door.py#L1) · explicit_script_identifier
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v189) Riemann-Roch carrier: (g_car,N_fam)=(5,3) from the mu4 divisor ---- *) Module[{degD, h0, rkH1, rankD5, rankA3}, degD = 4; (* |mu4| = deg D *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1564)
- [(* ---- (v983) SEAM.SIMPLECURRENT.GENERATOR.01: glue vector lambda = (omega_s, omega_f) ---- *) Module[{omegaS, omegaF, lam, inD5, inA3, inL0, gensD5, gensA3, dots, cosetRoots, census, lamV, omega2, nV, n2, cartanD8}, omegaS = ConstantArray[1/2, 5]; omegaF = {3/4, -1/4, -1/4, -1/4}; lam = Join[omegaS, omegaF]; inD5[x_] := (And @@ (IntegerQ /@ x)) && EvenQ[Total[x]]; inA3[y_] := (And @@ (IntegerQ /@ y)) && Total[y] === 0; inL0[z_] := inD5[Take[z, 5]] && inA3[Take[z, {6, 9}]]; checkExact["v983 NORMS+WEIGHT [E]: |omega_s|^2=5/4, |omega_f|^2=3/4, |lambda|^2=2, h_lambda=1", Total[omegaS^2] === 5/4 && Total[omegaF^2] === 3/4 && Total[lam^2] === 2 && Total[lam^2]/2 === 1]; checkExact["v983 ORDER FOUR [E]: 4*lambda in D5(+)A3, lambda and 2*lambda not -- [lambda] generates the diagonal Z4", inL0[4 lam] && ! inL0[2 lam] && ! inL0[lam]]; gensD5 = {{1, 1, 0, 0, 0}, {1, -1, 0, 0, 0}, {0, 1, 1, 0, 0}, {0, 0, 1, 1, 0}, {0, 0, 0, 1, 1}}; gensA3 = {{1, -1, 0, 0}, {0, 1, -1, 0}, {0, 0, 1, -1}}; dots = Join[omegaS . # & /@ gensD5, omegaF . # & /@ gensA3]; checkExact["v983 ISOTROPY+UNIMODULAR [E]: lambda.L0 subset Z on a generator set; det(D5)*det(A3)=16, index-4 glue => det L=1", (And @@ (IntegerQ /@ dots)) && 16/4^2 === 1]; cosetRoots[k_] := Module[{t = k lam, d5, a3}, d5 = Counts @ Select[ Total[(# + Take[t, 5])^2] & /@ Select[Tuples[Range[-5, 3], 5], EvenQ[Total[#]] &], # <= 2 &]; a3 = Counts @ Select[ Total[(Join[#, {-Total[#]}] + Take[t, {6, 9}])^2] & /@ Tuples[Range[-6, 6], 3], # <= 2 &]; Total[KeyValueMap[#2 Lookup[a3, 2 - #1, 0] &, d5]]]; census = Table[cosetRoots[k], {k, 0, 3}]; checkExact["v983 COSET ROOT CENSUS [E]: norm-2 vectors per fusion power k=0..3 = {52,64,60,64}, total 240; odd powers 64+64=128", census === {52, 64, 60, 64} && Total[census] === 240 && census[[2]] + census[[4]] === 128]; lamV = Join[{1, 0, 0, 0, 0}, omegaF]; omega2 = {1/2, 1/2, -1/2, -1/2}; nV = Total[lamV^2]; n2 = Total[omegaS^2] + Total[omega2^2]; cartanD8 = {{2, -1, 0, 0, 0, 0, 0, 0}, {-1, 2, -1, 0, 0, 0, 0, 0}, {0, -1, 2, -1, 0, 0, 0, 0}, {0, 0, -1, 2, -1, 0, 0, 0}, {0, 0, 0, -1, 2, -1, 0, 0}, {0, 0, 0, 0, -1, 2, -1, -1}, {0, 0, 0, 0, 0, -1, 2, 0}, {0, 0, 0, 0, 0, -1, 0, 2}}; checkExact["v983 KILLS+HOLOMORPHY SHADOW [E]: vector glue (v,omega_f) norm 7/4 and mismatched (omega_s, omega_2) norm 9/4 not in 2Z; det Cartan D8=4 vs glued det=1", nV === 7/4 && n2 === 9/4 && Det[cartanD8] === 4 && 16/4^2 === 1]; ]; (* ---- (v985) ALPHA.QUILLEN.EXACT.01: mu4 circulant spectra + graded channel swap ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L444)

## =150 2026-08-27 (CXXXVI) (the transport-lift wave — the two external-review rounds on the quantum structure of the seam transport graduate from the experiments tree into the load-bearing suite as v976_seam_lift_birkhoff.py and v977_transfer_unistochastic_wilson.py (suite [formula in source] , ledger [formula in source] : new rows TRANSFER.HIDDEN.CIRCULATION.01 and TRANSFER.COHERENT.WILSON.01, both ``executed half [E] / selection open [O]''; the exploration probes transfer_ birkhoff_ circulation_ probe.py 42/42 and transfer_ coherent_ wilson_ probe.py 28/28 stay in experiments/tfpt-discovery/ as the discovery record). (1) v976 — the Birkhoff fibre and the entanglement-breaking no-go. The Birkhoff (random-permutation) fibre of the seam single step [formula in source] (exact sixth root of the v221 kernel, [formula in source] bit-exact) is exactly a one-parameter line [formula in source] ; the hidden coordinate is the sign-character Fourier coefficient [formula in source] , populations are exactly [formula in source] -free, and no fibre member is chiral ( [formula in source] forced). The one-step coherence spectrum is [formula in source] and the triangle loop current is an exact eigen-observable [formula in source] — one step plus one current readout measures [formula in source] without an ancilla. On the contrast qubit the Choi partial transpose has spectrum [formula in source] : the deployed sixth-root spectrum sits exactly on the entanglement-breaking boundary because [formula in source] (mutated spectra miss by [formula in source] ); at the full three-level the family stays NPT at every tested iteration with [formula in source] , [formula in source] -independent. The no-go that sharpens DYN.UNITARY.DILATION.01: the deployed Kraus dilation [formula in source] is measure-and-prepare, hence entanglement breaking with quantum capacity [formula in source] and [formula in source] exactly — any dilation closing that contract must be a genuinely different object. Shannon KKT certificates: [formula in source] is exactly capacity-achieving for both [formula in source] and [formula in source] ( [formula in source] bit, [formula in source] bit, ratio [formula in source] ) — the surviving classical message is binary on every scale. The defect–Birkhoff value coincidence (weights [formula in source] vs the v652 ladder [formula in source] ) is recorded typed [C] with its honest multiplicity audit; the forcing functor is the named open contract TRANSFER.DEFECT.BIRKHOFF.01. (2) v977 — the unistochastic [formula in source] lift and the 5-12-13 Wilson code. [formula in source] is unistochastic: an exact [formula in source] with [formula in source] entrywise, angles forced by [formula in source] ( [formula in source] , [formula in source] , [formula in source] ), [formula in source] unique, lift set [formula in source] up to rephasing; Jarlskog [formula in source] exactly, and the real part of every Wilson plaquette is fixed by [formula in source] through unitarity — the full rephasing-invariant Wilson data is classical up to the [formula in source] orientation bit [formula in source] . The main plaquette is [formula in source] , normalized [formula in source] with [formula in source] (atoms: [formula in source] , [formula in source] , [formula in source] ); all nine plaquettes close on four Gaussian phase types with norms exclusively [formula in source] . The center bridge: [formula in source] for the v530 atom matrix, [formula in source] , and the v530 sibling quotients fail the identity — the bridge selects the atom quotient. Rationality selection: [formula in source] is rational only at [formula in source] (the deployed step hits [formula in source] exactly, so [formula in source] ); census over 238 valid family points: exactly one full-code point [formula in source] the deployed [formula in source] ( [formula in source] the preregistered [formula in source] kill). No fixed microstep: [formula in source] and a Dirichlet recurrence witness ( [formula in source] ) shows no single closed unitary generates the relaxing sequence — repeated steps require dephasing between steps, the six-step macro-gate [formula in source] (the coherent sharpening of clock-vs-walk). The PMNS near-miss stays a negative control ( [formula in source] vs [formula in source] ; [formula in source] ; no PMNS derivation). Surfaces. Research-contracts document: the DYN.UNITARY.DILATION.01 section gains the executed lift-structure sharpening, the CCC reduced-channel prose and the two former ``exploration-only'' citations of rounds DCXCVI/DCXCVII are upgraded to veri citations; origin_theory gains the honest ``what the classical transport does not determine'' paragraph next to the v221 recoverability code; tfpt_2 gains the [formula in source] bridge corollary in the v530 center-quotient block. No status marker moves; both contracts stay open; no PMNS/CP/flavor claim.)

[documents/changelog/sections/001-source.tex:307-308](../../../../documents/changelog/sections/001-source.tex#L307) · `section:edc607bc9be0dce5ac62` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [experiments/tfpt-discovery/transfer_coherent_wilson_probe.py](../../../../experiments/tfpt-discovery/transfer_coherent_wilson_probe.py#L1) · explicit_file_citation
- [TRANSFER.COHERENT.WILSON.01](../../../../verification/status_ledger.csv#L744) · explicit_claim_identifier · original status at linked ledger row
- [verification/v530_center_quotient_compiler.py](../../../../verification/v530_center_quotient_compiler.py#L1) · explicit_script_identifier
- [verification/v977_transfer_unistochastic_wilson.py](../../../../verification/v977_transfer_unistochastic_wilson.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/transfer_birkhoff_circulation_probe.py](../../../../experiments/tfpt-discovery/transfer_birkhoff_circulation_probe.py#L1) · explicit_file_citation
- [verification/v652_orbifold_arf.py](../../../../verification/v652_orbifold_arf.py#L1) · explicit_script_identifier
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/v976_seam_lift_birkhoff.py](../../../../verification/v976_seam_lift_birkhoff.py#L1) · explicit_script_identifier
- [TRANSFER.HIDDEN.CIRCULATION.01](../../../../verification/status_ledger.csv#L743) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v530 round: DIAMOND.CENTER.QUOTIENT.01 -- the center quotient compiler. Exact mirrors: fixed line, unimodular quotient = atom matrix, invariants, self-coding row sums, CP code, resolvent factorisation, K/Q controls. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8263)

## =150 2026-08-27 (CXXXI) (the external deep-review round — dimension / dynamics / gravity firewalls and the 4D construction ladder: the review diagnosis ``chiral [formula in source] D seam net [formula in source] local, interacting [formula in source] D quantum world'' is implemented as eight new contract IDs in tfpt_research_contracts plus one new load-bearing module. (1) DIMENSION.UPLIFT.FIREWALL.01 (standing rule, in force): no [formula in source] D theorem closes a [formula in source] D claim; every contract closure states the spacetime dimension of hypotheses AND conclusion; audit census recorded (SEAM.EQUIV.01 is [formula in source] D in and out — even fully proved it is a boundary building block, not the 4D theory; the v957 kinematic uplift does not close it; the anomaly-inflow bulk is invertible/topological, never to be silently equated with physical spacetime); the realistic route ordering (seam as boundary module [formula in source] genuine 4D Euclidean lattice [formula in source] OS package [formula in source] chirality/no-mirror [formula in source] only then BW/CHM [formula in source] entanglement gravity [formula in source] bulk–seam equivalence) is registered as the programme skeleton. (2) SEAM.BULK4D.RECON.01 : the previously implicit seam [formula in source] bulk theorem made explicit (4D local algebras/Schwinger functions; locality/microlocality, Poincar\'e covariance [formula in source] spectrum condition, spin-statistics [formula in source] CPT, both helicities, clustering, nontrivial S-matrix, unique operator dictionary). (3) the dynamics split DYN.MARKOV.EMBED.01 / DYN.UNITARY.DILATION.01 (``three meanings of dynamics'': relaxation [formula in source] / dissipative semigroup [formula in source] / unitary [formula in source] ): the finite kernel half of MARKOV.EMBED is executed \ as v971_markov_embedding_generator.py ( [formula in source] , sympy-exact) — [formula in source] of the v221 seam kernel is an EXACT classical Markov generator: [formula in source] by spectral calculus, row sums symbolically zero, off-diagonals exactly [formula in source] (the reviewer's independently verified numbers), uniformization certificate [formula in source] entrywise [formula in source] [formula in source] positivity-preserving doubly stochastic for all [formula in source] , [formula in source] (gap [formula in source] ), negative control: second eigenvalue [formula in source] gives [formula in source] — provably NOT embeddable; the field level and the local size-consistent unitary dilation (Stinespring [formula in source] Lieb–Robinson [formula in source] OS continuation) stay ; binding precision: the shared F_transfer relaxation shape is a universal CONTRACTION CLASS, not one physical clock (v723/v724/v777). (4) QFT4D.OS.RECON.01 \ (the genuine 4D Euclidean lattice OS package) with the binding phrasing rule: the v381 all-orders leg is a local perturbative construction under the stated EG/BRST hypotheses (Duch weak adiabatic limit cited, hypotheses unverified for the concrete model; no confinement / mass gap / asymptotic charged states / nonperturbative Higgs vacuum / full S-matrix follows) — tfpt_2 and tfpt_5 phrasing restricted accordingly. (5) CHIRAL4D.NOMIRROR.01 \ (explicit GW/overlap chiral lattice operator; local gauge-invariant measure, perturbative [formula in source] global anomaly freedom, no Witten [formula in source] anomaly, no mirrors, correct index/charges, stable continuum limit; Mastropietro arXiv:2303.02790 as calibration). (6) GRAV.NONCIRCULAR.01 (standing rule, in force): BW is a theorem WITHIN a local Poincar\'e-covariant QFT (Mund/Morinelli counterexample landscape cited), never a generator of Lorentz spacetime from a modular flow; every BW/CHM use declares assumption-vs-result; audit census: the entanglement-equilibrium Einstein derivation (v323/v358/v359) is typed ASSUMPTION (conditional on the 4D package, never citable as evidence for it), QG.AMB.01 correctly declared, the seam KMS [formula in source] chain dimension-typed, the intrinsic-BW programme the honest result-direction attempt. (7) OBS.TRANSDUCTION.01: the transduction principle (internal eigenvalue [formula in source] nonvanishing projection [formula in source] [formula in source] physical coupling [formula in source] observable signature; without the middle arrow neither non-observation falsifies nor observation confirms; minimal model machine-checked at exploration level in fo01, uniform functional blind to [formula in source] , character channel recovers [formula in source] to [formula in source] ; the ACT [formula in source] Planck birefringence proximity typed coincidence-level pending the shared-action proof). (8) PRED.JOINTLIKELIHOOD.01 : evidence reorganized from hit-counting into overdetermined relation bundles (flavor sum rule; [formula in source] , [formula in source] ; one normalized axion action; character-resolved transfer) with the statistical demand (joint likelihood, atom-induced covariance, effective dof, prespecified null [formula in source] formula grammar, real holdout); the v100 ``13/13, [formula in source] '' statement retyped as a look-elsewhere quantifier under its declared null — the 2026-06-09 freeze protects FUTURE measurements, it does not retroactively make historically known data blind. Docs corrected in the same change: docs/OPEN_PROBLEMS.md (the Einstein-derivation overstatement rewritten to the conditional Jacobson-route typing with the explicit does-NOT-follow list; ``zero open internal mechanisms'' fixed to match the contract scope fence — ledger wins; the all-orders phrasing restricted) and docs/FALSIFICATION.md (the null-model section retitled and rescoped, freeze and kill tests unchanged). Ledger [formula in source] rows; suite [formula in source] modules; bash build.sh audit and the manifest regeneration are the joint exit gate)

[documents/changelog/sections/001-source.tex:309-310](../../../../documents/changelog/sections/001-source.tex#L309) · `section:01c88746fb95cc0958d7` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [docs/OPEN_PROBLEMS.md](../../../../docs/OPEN_PROBLEMS.md#L1) · explicit_file_citation
- [OBS.TRANSDUCTION.01](../../../../verification/status_ledger.csv#L748) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [verification/v723_phys_modular_clock.py](../../../../verification/v723_phys_modular_clock.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [verification/v971_markov_embedding_generator.py](../../../../verification/v971_markov_embedding_generator.py#L1) · explicit_file_citation
- [verification/v724_phys_t3b_modular_flows.py](../../../../verification/v724_phys_t3b_modular_flows.py#L1) · explicit_script_identifier
- [PRED.JOINTLIKELIHOOD.01](../../../../verification/status_ledger.csv#L749) · explicit_claim_identifier · original status at linked ledger row
- [DYN.MARKOV.EMBED.01](../../../../verification/status_ledger.csv#L741) · explicit_claim_identifier · original status at linked ledger row
- [verification/v777_ftransfer_clock_jets.py](../../../../verification/v777_ftransfer_clock_jets.py#L1) · explicit_script_identifier
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_script_identifier
- [verification/v100_numerology_null_mc.py](../../../../verification/v100_numerology_null_mc.py#L1) · explicit_script_identifier
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [docs/FALSIFICATION.md](../../../../docs/FALSIFICATION.md#L1) · explicit_file_citation
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)

## =150 2026-08-24 (CXVIII) (the CCC-crossover promotion — the kinematics dictionary of the conformal-cyclic crossover graduates from the experiments tree into the load-bearing suite as v957_ccc_crossover_kinematics.py (suite [formula in source] ; six discovery probes of rounds DL–DLV re-run GREEN AS TYPED at promotion and embedded BYTE-EXACT with pinned SHA-256 hashes: ccc_crossover_gates_probe.py [formula in source] , ccc_uplift_4d_probe.py [formula in source] , ccc_fork_kms_holonomy_probe.py [formula in source] , ccc_kernel_gamma_kms_probe.py [formula in source] , ccc_transfer_selector_probe.py [formula in source] , ccc_kappa_freeze_probe.py [formula in source] ): (1) Penrose's reciprocal gauge [formula in source] is the element [formula in source] of the PROVEN [formula in source] M\"obius stabiliser [formula in source] — [formula in source] reverses the clock ( [formula in source] the [formula in source] sheet parity), swaps the aeon poles [formula in source] , and the crossover locus [formula in source] is the unit circle carrying ALL FOUR marks; (2) conformal-factor rigidity: on the 2D seam the clock alone leaves exactly ONE constant-curvature modulus (Liouville-exact dilation family) and the reciprocal [formula in source] kills it (unique zero at [formula in source] ); on the 3D crossover the deck ALONE kills all conformal moduli (the [formula in source] deck-commutant is [formula in source] -dimensional [formula in source] , ALL Killing, boost content [formula in source] ; global uniqueness on the explicit Obata boost family, 200-axis scan bounded below by [formula in source] ) — TFPT's candidate answer to CCC's open unique-conformal-factor problem, [formula in source] staying pure unit calibration; (3) the entropy reset of the cyclic \ reading is a REDUCED CHANNEL: the v221 transport is CPTP not unitary ( [formula in source] ), its Stinespring isometry explicit ( [formula in source] exact), [formula in source] EXACTLY, the global overlap invariant and the environment retaining the full distinguishability — ``unitarity [formula in source] rank-1 attractor'' is isometry [formula in source] partial trace; (4) the kinematic [formula in source] uplift from corpus objects only: stereographic(Hopf [formula in source] ) [formula in source] EXACTLY (the seam sphere IS the Hopf base), the v492 deck [formula in source] acts freely so the crossover [formula in source] is the smooth lens boundary of the corpus [formula in source] ALE [formula in source] , clock [formula in source] and the reciprocal lift [formula in source] normalise the deck and descend ( [formula in source] to [formula in source] , inverting the clock), the four marks lift to four Hopf fibre circles paired by the deck into the TWO [formula in source] sheet orbits with Gauss linking number [formula in source] , the 4D bridge is the cone [formula in source] with the inversion [formula in source] a conformal involution (pullback [formula in source] symbolic) fixing the unit lens POINTWISE and swapping the aeon ends, and the Lorentzian shadow [formula in source] is Einstein [formula in source] (symbolic Ricci) with a SPACELIKE round- [formula in source] crossover and [formula in source] vanishing to first order; (5) the KMS/modular closure of discrete [formula in source] dynamics at the free level: detailed balance EXACT, [formula in source] EXACTLY (the seam gap IS a modular energy), [formula in source] (one clock tick [formula in source] one unit of KMS time at [formula in source] ), OS Gram PSD, and the v526 normalisation [formula in source] replicated exactly [formula in source] the Gibbons–Hawking normalisation on the crossover fibre; (6) the holonomy dictionary: the two clock-pole circles descend to the lens core geodesics with the full [formula in source] monodromy [formula in source] while EVERY seam string carries exactly the 2-torsion [formula in source] , and [formula in source] is trivial on the base while flipping the spinor coordinates — the v522 statement ``gaugeable datum [formula in source] the 2-torsion [formula in source] ; full wrap [formula in source] fermion parity'' in geometric form (typed \ correspondence); (7) the selector necessity (the [formula in source] -facing theorem): the admissible OS reflections of the v512 mark family [formula in source] form the pair-exchanging [formula in source] for every [formula in source] and close to [formula in source] EXACTLY at [formula in source] (the order-4 clock factorises into admissible reflections, [formula in source] , iff [formula in source] ), and at Majorana operator level on the [formula in source] seam ring with fermionic reordering signs kept the free parent is [formula in source] -real on ALL 16 axes (v521 side-blindness replicated) while the interacting family is [formula in source] -real on exactly [formula in source] axes and the clock-axis cuts ONLY at [formula in source] , asymmetric couplings breaking reality — the UNIQUENESS half of the v534 straddle selector ( [formula in source] , symmetric couplings) is thereby DERIVED as a [formula in source] -reality necessity (the survival half and the coupling sign stay v534's nonperturbative toy facts, cited; reality is sign-blind, checked); (8) the frozen Gate-6 kernel: exactly two decay modes [formula in source] and [formula in source] (ratio [formula in source] ), the frozen defect-class overlap table [formula in source] / [formula in source] with the sheet-parity sign rule, disc radius [formula in source] , and [formula in source] DERIVED from the v526 KMS normalisation up to a declared convention band — [formula in source] ticks across the whole band, relic contrast [formula in source] : the template degenerates ROBUSTLY to the sharp causal top-hat disc; three freeze hashes pinned and recomputed in-run. NEW LEDGER ROWS: CCC.SEAM.KINEMATICS.01 [E] (the certified dictionary) and CCC.SEAM.CROSSOVER.01 [O] (the dynamical-crossover research contract: D1 interacting algebra on the crossover [formula in source] WOIT [formula in source] in the crossover geometry, D2 field-level Stinespring, D3 the cosmology fork decision — Starobinsky [formula in source] priced decidable by [formula in source] experiments —, D4 the executed disc search; kill criteria frozen incl.\ the forbidden mark/Hawking-point count identification); new contract section in tfpt_research_contracts; the origin-theory Penrose-CCC bullet SHARPENED (asymptotic de Sitter does NOT imply conformal flatness — [formula in source] for Schwarzschild–de Sitter, machine-checked; the CCC smoothness/Weyl conditions are additional crossover data) and pointed at the certified kinematics; PREREGISTERED SEARCH scaffolded at experiments/ccc-crossover-disc/ (frozen hypotheses ccc_disc_v1.yaml with kill criteria K1–K6, null battery and BH- [formula in source] [formula in source] replication decision rule; freeze-check CLI 3/3 hashes intact; 5/5 guard tests; catalog entry 7b.9 of the experiments README) — verdict slot data_limited (preregistered); the Planck PR3 SMICA data pass executed separately at experiments level (first data contact logged in the project README). FENCES CARRIED EVERYWHERE: the cyclic/CCC reading stays \ and is NOT upgraded by the promotion; WOIT.OS.TWISTOR.01 stays \ with all kill tests live (the module certifies kinematics [formula in source] free level [formula in source] the necessity direction ONLY); the deck fork is decided only CONDITIONALLY on the v522 wrap identification; a null disc search damages nothing in the compiler core. Research notes DL–DLV appended to experiments/next.txt; FULL run_all.py ALL CHECKS PASSED at 950 modules; bash build.sh release green; bash build.sh audit [formula in source] AUDIT OK; manifests regenerated LAST. No omega closed beyond the two new rows; NO claim that CCC follows from TFPT)

[documents/changelog/sections/001-source.tex:311-312](../../../../documents/changelog/sections/001-source.tex#L311) · `section:84ec2c9d7a3c77ec2664` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v521_seam_bit_rp_blind.py](../../../../verification/v521_seam_bit_rp_blind.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [CCC.SEAM.CROSSOVER.01](../../../../verification/status_ledger.csv#L738) · explicit_claim_identifier · original status at linked ledger row
- [verification/v512_seam_tau_flag.py](../../../../verification/v512_seam_tau_flag.py#L1) · explicit_script_identifier
- [experiments/tfpt-discovery/ccc_crossover_gates_probe.py](../../../../experiments/tfpt-discovery/ccc_crossover_gates_probe.py#L1) · explicit_file_citation
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [experiments/tfpt-discovery/ccc_fork_kms_holonomy_probe.py](../../../../experiments/tfpt-discovery/ccc_fork_kms_holonomy_probe.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/ccc_kappa_freeze_probe.py](../../../../experiments/tfpt-discovery/ccc_kappa_freeze_probe.py#L1) · explicit_file_citation
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_script_identifier
- [CCC.SEAM.KINEMATICS.01](../../../../verification/status_ledger.csv#L737) · explicit_claim_identifier · original status at linked ledger row
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_file_citation
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_script_identifier
- [verification/v522_woit_beta1_gso_gauge.py](../../../../verification/v522_woit_beta1_gso_gauge.py#L1) · explicit_script_identifier
- [experiments/tfpt-discovery/ccc_kernel_gamma_kms_probe.py](../../../../experiments/tfpt-discovery/ccc_kernel_gamma_kms_probe.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/ccc_transfer_selector_probe.py](../../../../experiments/tfpt-discovery/ccc_transfer_selector_probe.py#L1) · explicit_file_citation
- [verification/v492_celestial_z4_orbifold.py](../../../../verification/v492_celestial_z4_orbifold.py#L1) · explicit_script_identifier
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/ccc_uplift_4d_probe.py](../../../../experiments/tfpt-discovery/ccc_uplift_4d_probe.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v525 round: SEAM.BIT.TWISTBLIND.01 -- "the twist-state kill": the NINTH side-blind test on the v512 scoreboard (8 -> 9); the free-plus-twist class is exhausted. Three exact mirrors: (i) the integer incidence frame + the sigma o r = +-sigma congruence mechanism (swap axes: sigma o r = sigma => the twisted Gram is the diagonal unitary congruence D M D = spectrally invisible; fixing axes at pi/2: sigma o r = -sigma = the eta flip); (ii) the pi/2-existence solveset of the mark-fixing axes + the exact counterwitness census ((3+4i)/5 unimodular but NEVER a root of unity up to order 64 -- no lattice mark-compatible reflection at any dyadic refinement); (iii) the delta <-> pi - delta mirror equivariance (the lattice reflection maps the m-mark set EXACTLY to the (8-m)-mark set -- the exact mechanism behind the Casimir mirror symmetry ln|omega(D)|(m) = ln|omega(D)|(8-m) and behind pi/2 as the symmetric point of every invariant readout). The Pfaffian insertion spectra, the Bogoliubov 2-of-16 pattern census, the defect energy and the 40-digit inertia certificates are numerical (mpmath), Python-only, flagged here. Mirrors v525. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8058)
- [(* ==== v521 round: SEAM.BIT.RPBLIND.01 -- "free OS positivity does not see delta": the anti-linear census solvesets on M(delta), the counterwitness census, the V4 -> D4 closure (face #13), the cut/mark incidence, the continuum axis elimination + Cauchy-Stieltjes factorisation, the clock-tower clause and the hex/silver precondition controls. The 40-digit lattice Gram inertia spectra (N = 16 / N = 32) are Python-only by the suite convention. Mirrors v521. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7479)
- [(* ==== v522 round: WOIT.BETA1.GSO.01 -- "the clock is time-like, GSO is the gauge datum": the Z8/NS tower + Ramond control, the invariant- dimension chain, the time-like reflection census, the exact Hermiticity witness of the clock insertion, the GSO 2-torsion census and the family-A tower-normalisation failure. The 40-digit GSO-fixed RP inertia certificates ((29,0,0)/(8,0,0)/(7,9,6)/(17,12,0)) are Python-only by the suite convention. Mirrors v522. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7609)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [(* ==== v512 round: SEAM.TAU.FLAG.01 -- "the flag-transitivity equivalence web": the tau = i attack on the free RP seam circle. Test family M(delta) = {+-1, +-e^(i delta)}; bare mark-transitivity is delta-blind (pair-exchanging V4), FLAG transitivity <=> delta = pi/2 <=> tau = i. Six exact mirrors: (i) the V4/D4 census over five exact members incl. flag/arc orbit counts, (ii) the solveset equivalences + family identities, (iii) the odd-split closed form + arc Laplacian + K3 indicator, (iv) the twist mode identity + AB delta-blindness + j-rationality control, (v) the H4 centraliser rigidity (Schur), and (vi) the negative controls (hexagonal/silver/Z16 census/n = 3). Mirrors v512. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5675)
