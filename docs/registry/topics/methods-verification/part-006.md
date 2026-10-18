# Verification, formalization and safeguards — part 6

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## BT1 (closes A.h1).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:227-233](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L227) · `section:6c98d3366398750777cf` · paragraph

TFPT defines the physical vacuum-density determinant as the primitive admissible zeta determinant. Non-primitive admissible repetitions are not physical TFPT vacuum classes. This is a clean physical choice (the same role as the Selberg primitive-orbit decomposition on closed Riemannian manifolds), not a trick.

## Status taxonomy after v4.6.7

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:328-348](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L328) · `section:5a933c86dc641fb7505f` · subsection

@p0.32 Y@ Status & Meaning \\ derived_tfpt_candidate_v46 & v4.6 candidate; Lemmas A–E proposed, none discharged. \\ derived_tfpt_theory_complete_ pending_artifacts \,( NEW v4.6.7) & All 14 hooks resolved theory-internally by 7 bridge theorems. Pending: artefact validation. \\ derived_tfpt & All artefact validations also passed. The pipeline becomes TFPT-derived in the strict sense. \\

## The five validation groups

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:11-49](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L11) · `section:3241a199c704e798fada` · subsection

@p0.06 p0.18 p0.27 Y@ ID & Group & Acceptance criterion & Closes (artefact) \\ G1 & sprint_2a_branch_bundle (12 files) & [formula in source] AND 24/24 hard checks of sprint2a_contract.validate_sprint2a_branch pass. & E1, E2, E3, E4, E5 \\ G2 & sprint_2c_thermal_matter (7 files) & QKE Ward residues [formula in source] , [formula in source] numerically verified to [formula in source] ; BBN [formula in source] to [formu

## The complete status flow

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:119-148](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L119) · `section:5ea787690e28cf9b9e50` · subsection

@p0.36 lY@ Status & Cycle & What flips \\ derived_tfpt_candidate_v46 & v4.6 & Initial candidate; lemmas A–E proposed, none discharged. \\ derived_tfpt_theory_complete_ pending_artifacts & v4.6.7 & can_flip_to_theory_complete(REQUIRED_DISCHARGE_OUTCOMES_V467) returns True. All 14 hooks resolved by 7 bridge theorems. \\ derived_tfpt & v4.6.8 (final) & can_flip_to_derived_tfpt(report) returns True. All 5 measurement-bri

## Kill conditions and audit table

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:149-178](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L149) · `section:3404c2bf78c363ac3a22` · section

@p0.26 Y@ Module & Kill condition \\ ledger & [formula in source] audit mismatch unresolved when used in production. \\ native_closure_v46 & Any of the seven primitives violated; any of Lemmas A–D falsified. \\ branch_phase_selection & [formula in source] not Hermitian; [formula in source] not an involution; any input matching planck_phase, planck_alm, smica_alm_as_phase_seed, nilc_phase, sevem_phase, commander_phase

Explicit source references:

- [verification/v46_grand_mass_volume.py](../../../../verification/v46_grand_mass_volume.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *) checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+", Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16]; checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car", Sort[Abs[plLeft[K]]] == {1, 4, 6} && Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar]; checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car", 4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15]; (* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L168)

## What this pipeline does not claim

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:179-214](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L179) · `section:157a7c50b2b0c5f60c40` · section

No theorem-level lemmas. Lemmas A–E are conjectures with proof skeletons ( at TFPT v4.6. The pipeline runs in candidate mode only. No real Mode-E branch. The Mode-E run uses the candidate v4.6 synthetic bundle, not a real Sprint-2A extraction of [formula in source] , [formula in source] , [formula in source] from the boundary data. Real Mode E is a Sprint 2A–2D deliverable. No claim of pixel-level Planck agreement. M

## Roadmap to a finished v5.0

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:215-247](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L215) · `section:9400f87be0e5ce310646` · section

The five outstanding theorem-level closures are Lemma A (Seam Determinant): rigorous definition of [formula in source] and proof that non-primitive admissible repetitions vanish. Lemma B (Curvature Residue): proof of [formula in source] from the admissible curvature path-integral. Lemma C: subdivide into C1–C4; C4 ( [formula in source] ) is the weakest link — needs SFR/ [formula in source] / [formula in source] to co

## Out-of-sample tests.

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex:248-290](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/005-section-the-v4-6-8-measurement-bridge-contract.tex#L248) · `section:044bb626b205fc4a44dc` · paragraph

Even before the proofs land, the following are testable predictions of v4.6 and would either falsify the conjecture or sharpen the agreement: BAO scale (DESI Y3, eBOSS) at 0.5\% precision; CMB lensing power spectrum (Planck PR4, ACT DR6, SPT-3G); [formula in source] tension (KiDS, DES, Euclid); Deuterium primordial abundance (high-resolution QSO absorption); Effective neutrino number from BBN (independent of CMB); Di

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

## Hook Solution Sketches (v4.6.5)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:1-32](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L1) · `section:4e5e7d0df9eb586da6b1` · section

This appendix is the v4.6.5 deliverable Stefan asked for in the v4.6.4 review: a full 1:1 transcription of every proof structure from full-plank/beschreibung.txt, plus a best-effort proposed solution for each of the [formula in source] open hooks. The authoritative machine-readable form is in tfpt_cmb.lemma_proof_outlines; this appendix gives the human-readable summary.

## Lemma D2.h1 (medium).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:129-140](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L129) · `section:30f56d3e8cec86968141` · paragraph

Hook. Prove that the stable neutral admissible sector is complete.\\ Proposed solution. Spectral completeness of [formula in source] follows from Paper 2's carrier classification combined with Paper 4's admissibility constraints. Strategy: enumerate every stable neutral spin-0/1/2 mode, verify [formula in source] , verify the [formula in source] leakage from [formula in source] . Acceptance: a Paper-2 corollary stati

## v4.6.6 Proof Discharges (verbatim)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:239-249](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L239) · `section:5c4cc439c613f5bcc948` · section

This appendix reproduces the full proof body of every v4.6.6 hook discharge. Each entry has (a) the formal claim, (b) the proof body verbatim from Stefan v4.6.6 brief, (c) the boxed final form that exhibits what closes the hook. The discharge status is given for each entry; the closure conditions are summarised in the master table of

## A.h1 \,—\, Seam Determinant \,( closed_pending_convention_adoption)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:250-270](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L250) · `section:052f57fe3f4412c82339` · subsection

Proof. Define the primitive admissible zeta determinant by [formula in source] . The primitive orbit formula on the closed seam geometry is [formula in source] . Closed-branch selection plus [formula in source] plus [formula in source] leaves only the minimal primitive seam class with [formula in source] (double sheet), [formula in source] (primitive seam norm), [formula in source] (two oriented EM runs). Hence [form

## B.h1 \,—\, Curvature Residue \,( closed_pending_curvature_instanton_theorem)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:271-290](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L271) · `section:18a71b746fc4e4073a05` · subsection

Proof. [formula in source] . TFPT defines the non-perturbative admissible curvature susceptibility as the saddle-point quantity [formula in source] with [formula in source] (retained-seed barrier) and [formula in source] (zero-mode norm). Inverting: [formula in source] . Then [formula in source] and the Starobinsky potential closes the inflation cascade. Curvature Instanton Theorem: [formula in source] has a unique r

## C1.h1 \,—\, Photon Density \,( closed_pending_paper5_metrology)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:291-303](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L291) · `section:d79a2ccdced0ebe1036b` · subsection

Proof. The lowest native four-dimensional radiation functional is [formula in source] ; the bosonic thermal phase-space norm gives the universal factor [formula in source] ; hence [formula in source] . Stefan-Boltzmann inversion gives [formula in source] in reduced Planck units. [formula in source] (Stefan-Boltzmann inversion)

## C2.h1 \,—\, Effective Neutrino Number \,( closed_pending_qke_collision_kernels)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:304-318](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L304) · `section:effb17ac700626e45b3f` · subsection

Proof. [formula in source] with [formula in source] . Carrier rigidity: [formula in source] . Weak-seam Ward identity: [formula in source] . EM-holonomy Ward identity: [formula in source] . [formula in source]

## C3.h1 \,—\, Helium Fraction \,( closed_pending_bbn_verification)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:319-334](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L319) · `section:4df1aaaa251d85018a31` · subsection

Proof. The leading alpha channel binds four nucleons. In the symmetric freeze-out sector [formula in source] , [formula in source] . TFPT EM holonomy shifts the weak rate uniformly: [formula in source] . Linear sensitivity: [formula in source] . Hence [formula in source] and [formula in source] up to [formula in source] . [formula in source] under TFPT weak-rate deformation.

## C4.h1 \,—\, Reionization Optical Depth \,( open_hardest_no_full_discharge)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:335-356](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L335) · `section:65e2cf1dd148933e18b2` · subsection

Proof skeleton. [formula in source] . Full discharge requires three sub-theorems: C4a Press-Schechter Source Theorem [formula in source] ; C4b Carrier IMF Photon Yield [formula in source] ; C4c Admissible UV Escape [formula in source] . Honest verdict (Stefan v4.6.6): not in reach without substantial additional TFPT structure; expect a separate dedicated TFPT companion paper.

## D1.h1 \,—\, Baryon Density \,( closed_pending_paper5_metrology)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex:357-370](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/007-section-hook-solution-sketches-v4-6-5.tex#L357) · `section:fea6c6b67d1a5c4308f3` · subsection

Proof. Carrier rigidity [formula in source] . The baryonic occupancy is [formula in source] . Sheet Overlap eigenvalue gives [formula in source] . Hence [formula in source] . Stefan-Boltzmann normalised TFPT carrier metrology.

## D2.h1 \,—\, Cold Dark Matter Density \,( closed_pending_neutral_enumeration)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex:1-14](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex#L1) · `section:21189f754a84e03b0f8b` · subsection

Proof. [formula in source] (spectral completeness), [formula in source] (quadratic stable seed intensity), [formula in source] (Sheet-Overlap leakage). [formula in source] : spectral completeness theorem.

## D3.h1 \,—\, Sum of Neutrino Masses \,( closed_pending_paper5_metrology)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex:15-28](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex#L15) · `section:b65903fd9d86ddcdd67d` · subsection

Proof. [formula in source] , Takagi-orthogonal. Then [formula in source] . The mass-metrology bridge [formula in source] sets the TFPT eV unit. Numerical: [formula in source] eV. [formula in source] as internal TFPT low-energy projection.

## E2.h1 \,—\, Canonical Spectral Flag \,( closed_pending_six_commutators)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex:43-56](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex#L43) · `section:a49e100ba1f7febf0da2` · subsection

Proof. [formula in source] (sheet symmetry); [formula in source] (boundary modes); [formula in source] (carrier kinetic); [formula in source] ( [formula in source] invariance); [formula in source] (Calderon polarisation). Joint spectral theorem: canonical lexicographic flag from joint eigenvalues; residual U(1) fixed by E3. [formula in source] abelian.

## E3.h1 \,—\, Seam state uniqueness \,( closed_pending_paper1_seam_orientation)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex:57-66](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/008-subsection-d2-h1-cold-dark-matter-density.tex#L57) · `section:d60a7965c938fa10d156` · subsection

Proof. Closed Riemannian seam carries canonical [formula in source] from TFPT metric; primitive seam is winding-class-1 closed loop; [formula in source] fixes the global phase. [formula in source] gauge-invariant.

## Version 4.5 completion surface

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/001-section-reading-guide-and-claim-map.tex:235-383](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/001-section-reading-guide-and-claim-map.tex#L235) · `section:12bf5097766a9972f183` · subsection

The manuscript now contains a fully rigid algebraic core together with analytic closure blocks whose exact status is recorded theorem by theorem in the proof-obligation ledger. The remaining explicit standard-theorem interface is [formula in source] while the other former [formula in source] interfaces have now been pulled into the manuscript proof surface. The eight items below are therefore not a promise of later c

## Canonical rigid object and falsification interface

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex:238-239](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/002-section-big-picture-what-tfpt-actually-claims.tex#L238) · `section:a95c8b6a1d951523521b` · section

No opening prose excerpt; see the source.

## Structural falsification map

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex:1-44](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex#L1) · `section:2364dc5301838c28a046` · subsection

The main text closes the theorem chain at [formula in source] and then attaches one structural side card, the falsification map [formula in source] This map reports which local or global structural failure mode would break each arrow of the reconstruction. It is hard-separated from the appendix-level empirical comparison map [formula in source] , which acts only after [formula in source] has been fixed and is collect

## Conclusion

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex:45-46](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex#L45) · `section:98ee9b117357241dce10` · section

No opening prose excerpt; see the source.

## Closed theorem stack and interface layers

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex:47-137](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex#L47) · `section:f55361310e5d255f06b6` · subsection

TFPT is organized around the one-sided boundary datum [formula in source] induced by the minimal operational seed, and reconstructs in a two-stage closure order [formula in source] This reconstruction first fixes the joint discrete datum and only afterwards the continuous Euler–Lagrange branch, thereby identifying the canonical rigid object of the boundary-polarized branch: [formula in source] The selector-to-dynamic

## Two side maps from [formula in source] T-star

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex:138-154](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex#L138) · `section:578930658f93d971b5e0` · subsection

From [formula in source] exactly two side maps are attached, both hard-separated from the theorem chain: Structural falsification map (main text). The map [formula in source] of sec:structural-falsification-map reports the structural failure mode that would break each arrow of the reconstruction. It uses no scheme conventions, no thresholds, and no comparison data. Empirical comparison map (appendix only). The map [f

## Conditional closure layer and status of the four downstream readouts

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex:155-221](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex#L155) · `section:39efd99c17f6a8960bc8` · subsection

The closed-branch theorem stack is supplemented by a single, explicitly labeled conditional closure layer, organized so that every numerical readout can be promoted to a theorem as soon as a single named lift hypothesis is discharged. The four downstream readouts and their current status are [formula in source] The compressed integrated story is [formula in source] and in the matter sector [formula in source] The fou

## Main claim

[documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex:222-312](../../../../documents/archive--tfpt-45--source_extracts--00_orientation_source/sections/003-subsection-structural-falsification-map.tex#L222) · `section:124e3d44910d64d30853` · subsection

A compressed decoder reading of the closed branch is [formula in source] [formula in source] In this condensed form, [formula in source] generates the carrier structure, the primitive winding class [formula in source] fixes the counting, and the retained seed [formula in source] decodes the bridge observables.

## Operational prediction set

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/007-subsection-ckm-and-pmns-closure.tex:223-292](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/007-subsection-ckm-and-pmns-closure.tex#L223) · `section:37f55f89510c77a79a9d` · subsection

The narrow empirical readout table is not the whole experimental surface of the manuscript. tab:operational-prediction-set collects the rows that are operationally testable on near- to medium-term timescales, while keeping their status, next test, kill criterion, and dependency structure explicit. The point is not to flatten them into one truth class. Rather, the Status column now uses only the manuscript's final out

## Compact prediction ledger

[documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/007-subsection-ckm-and-pmns-closure.tex:321-352](../../../../documents/archive--tfpt-45--source_extracts--03_em_flavor_source/sections/007-subsection-ckm-and-pmns-closure.tex#L321) · `section:99e730f6ca596d7ed5b8` · subsection

The main empirical readout table shows only a narrow readout surface. To keep the output structure visible, tab:prediction-ledger summarizes which output packages belong to which layer of the paper.

## Closure theorems from the admissibility complex

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/002-section-closure-theorems-from-the-admissibility-complex.tex:1-397](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/002-section-closure-theorems-from-the-admissibility-complex.tex#L1) · `section:dfd6ad94d3380e6b33e4` · section

The preceding two sections introduced the carrier-compatible geometric and transport architecture. The primitive admissibility projector [formula in source] was already placed in the primitive section so that the proof direction runs from the boundary datum through the derived closed datum to [formula in source] , and only then to the later sector theorems. What remains in this section is therefore (i) the upgrade of

## Admissible OS reconstruction and asymptotic scattering

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:171-178](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L171) · `section:19059df087b765a037b9` · section

This appendix upgrades the admissible Schwinger, reconstruction, and scattering block from a named standard interface to a manuscript-level proof package. The point is not to replace standard machinery by ad hoc notation, but to verify explicitly that the admissible branch satisfies the relevant hypotheses on [formula in source] .

## Yukawa kernels and positivity lemmas

[documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex:318-355](../../../../documents/archive--tfpt-45--source_extracts--04_qft_source/sections/008-section-relative-reflection-positivity-with-fermions.tex#L318) · `section:3af6d0fa08cdf2b14930` · section

This appendix is the proof motor for the transport positivity, determinant-phase suppression, and bounded-residual statements used in the main text. The transport program is based on the regularized kernel [formula in source] Three remarks are important. The regulator [formula in source] is not optional: without it the kernel becomes ill-defined exactly where the admissibility question is most delicate. Positivity of

## Front matter / support

[documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/004-subsection-absolute-spectral-planck-closure.tex:1-170](../../../../documents/archive--tfpt-45--source_extracts--05_metrology_source/sections/004-subsection-absolute-spectral-planck-closure.tex#L1) · `section:d0943a01ef14269bd91b` · frontmatter

(seed) at (0,0) primitive channel\\ [formula in source] ; (geoz) at (-3.2,-3.6) [formula in source] \ / Higgs background; (qcd) at (3.2,-1.9) hadronic dressing\\ _ [formula in source] [formula in source] [formula in source] [formula in source] _ . This is the clean separation that prevents the Planck/Higgs/QCD scale clash.

## Falsification matrix

[documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex:1-61](../../../../documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex#L1) · `section:2d820500af07a5247cdd` · subsection

The present draft does not ask the reader to accept one undifferentiated output claim. Each main-text closure statement has a corresponding local or global failure mode, and those failure modes should be readable without first decoding the appendix tables.

## Proof-obligation ledger

[documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex:62-130](../../../../documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex#L62) · `section:6ac286160fd9206948ae` · subsection

To keep proof status, interface assumptions, and comparison-only layers visibly separated, we record the present audit path explicitly. We use five status classes: ] full proof in manuscript; ] full proof modulo an explicit standard theorem; ] proof sketch in main text with full proof deferred; ] readout or comparison only; ] programmatic closure target with a fixed mathematical statement but without a claimed proof 

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)

## Infrared continuations of the seam transfer

[documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex:131-214](../../../../documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex#L131) · `section:27193bdda852d0217b0c` · subsection

Theorem thm:cosmology-closure and cor:ir-seam-transfer-bounds determine the theorem-level seam-transfer expression for [formula in source] and its determinant bounds. The numerical scales recorded below require one further infrared assumption and therefore are organized as a labeled conditional closure layer, separated from the theorem core. Each member of the layer is stated as a conjecture or as a corollary conditi

## FRW reduction and cosmology interface proofs

[documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex:215-297](../../../../documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex#L215) · `section:a9f7b87f0bddb729c73f` · section

This appendix section upgrades the cosmology interface block from a proof sketch to a manuscript proof. The point is to keep the theorem-level content at the level of closed-branch interface data, while leaving late-time numerical continuation in the comparison layer.

## Axion interface

[documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex:298-324](../../../../documents/archive--tfpt-45--source_extracts--06_cosmology_source/sections/002-subsection-falsification-matrix.tex#L298) · `section:2b723594e455a5b956f0` · subsection

The axion rows are cosmology readouts generated from the same determinant-line / seam-transfer / scalaron interface data that also fix reheating and the heavy-neutrino scale. On the closed cosmology branch, [formula in source] In standard haloscope units this gives [formula in source] so the practical scan prescription is a conservative window [formula in source] at the quoted coupled sensitivity. The present appendi

## Downstream closure modules from the closed branch

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/001-section-downstream-closure-modules-from-the-closed-branc.tex:5-25](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/001-section-downstream-closure-modules-from-the-closed-branc.tex#L5) · `section:1372a38f44e33d847460` · section

The present section records the downstream closure modules that start from the already fixed branch object [formula in source] Nothing in this section changes the upstream theorem chain. The exact proof status of these downstream closures is recorded in the proof-obligation ledger, and each statement below is phrased only as far as it factors through already fixed branch data. The stationary geometric scale, boundary

## Operational prediction set

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex:268-337](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/003-subsection-p-late-time-dark-sector-and-structure-growth.tex#L268) · `section:49a4732ecb6aaa77cb4f` · subsection

The narrow empirical readout table is not the whole experimental surface of the manuscript. tab:operational-prediction-set collects the rows that are operationally testable on near- to medium-term timescales, while keeping their status, next test, kill criterion, and dependency structure explicit. The point is not to flatten them into one truth class. Rather, the Status column now uses only the manuscript's final out

## Compact prediction ledger

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:1-32](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L1) · `section:dd4569858aa685fc786f` · subsection

The main empirical readout table shows only a narrow readout surface. To keep the output structure visible, tab:prediction-ledger summarizes which output packages belong to which layer of the paper.

## Empirical readout and kill-test logic

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:33-43](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L33) · `section:4074cd83824ceb930858` · subsection

The present main-text readout surface is no longer intentionally mixed. Its rows now use the manuscript's closed classes: theorem, physical observable, scheme projection, and appendix continuation. Carrier algebra and the exact [formula in source] row remain the sharpest numerically load-bearing entries, while the former seed-driven rows are now reorganized by sector rather than counted as one compressed shadow packa

## Residual readout and interface refinements

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:44-93](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L44) · `section:2940f62e801e3f9c5344` · subsection

The residuals for the restricted six-row readout table are shown in fig:residual-plot. The carrier-linked electromagnetic, birefringence, and baryon-density channels all remain within the displayed few-sigma window. The CKM phase is not plotted here because it is better treated in the operational prediction set and Appendix app:benchmarks rather than inside the restricted six-row residual plot.

## Technical conventions and data layers

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:94-98](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L94) · `section:3eba10f77107383cdc50` · section

This appendix collects the technical bookkeeping that supports the boundary-to-carrier presentation but would slow the early main-text flow if placed before the carrier theorem.

## Relative objects

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:99-123](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L99) · `section:29cf0c90b46e29d07cfe` · subsection

The adjective relative is used in one fixed sense throughout the paper: every operator or action is compared to a declared reference object.

## Layered datum and admissibility

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:124-195](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L124) · `section:56aeac129663ec15f98f` · subsection

The technical bookkeeping behind the manuscript uses five levels: [formula in source] [formula in source] [formula in source] [formula in source] [formula in source] Here [formula in source] is the primitive boundary kernel, while [formula in source] is the derived theorem-level post-carrier kernel reconstructed from the joint discrete datum and the full selector.

## Symbol guide

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:196-293](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L196) · `section:5c8c49a3dba7767a1392` · subsection

The symbol guide is split into two tables to keep theorem-level objects lexically separate from appendix-only comparison and readout objects. tab:symbol-guide-theorem contains only symbols that participate in the main-text theorem chain; tab:symbol-guide-appendix contains only symbols that live in the appendix-level comparison and readout layer.

## Constants atlas and downstream scale grammar

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:294-298](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L294) · `section:f9b8b8f5a95d9b4c2b47` · section

This appendix collects material that is useful for internal compression but should not dominate the main-text scope of explicit claims.

## Global rotation angle and constants atlas

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex:299-382](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/004-subsection-compact-prediction-ledger.tex#L299) · `section:b827287876766de15bf0` · subsection

On the canonical branch the seam loop carries one unit of spectral flow, [formula in source] Because the spin lift closes only after [formula in source] , the normalized rotation modulus is [formula in source] The cascade in fig:constant-cascade is kept here as technical bookkeeping rather than as an early main-text dependency graphic.

## Admissible OS reconstruction and asymptotic scattering

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:127-134](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L127) · `section:46aaa0c485552cb0fd29` · section

This appendix upgrades the admissible Schwinger, reconstruction, and scattering block from a named standard interface to a manuscript-level proof package. The point is not to replace standard machinery by ad hoc notation, but to verify explicitly that the admissible branch satisfies the relevant hypotheses on [formula in source] .

## FRW reduction and cosmology interface proofs

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex:272-352](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/006-subsection-infrared-continuations-of-the-seam-transfer.tex#L272) · `section:e1dd48d5555a9b0f5e6d` · section

This appendix section upgrades the cosmology interface block from a proof sketch to a manuscript proof. The point is to keep the theorem-level content at the level of closed-branch interface data, while leaving late-time numerical continuation in the comparison layer.

## Yukawa kernels and positivity lemmas

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:1-38](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L1) · `section:2334f2b3d13fcb70cd58` · section

This appendix is the proof motor for the transport positivity, determinant-phase suppression, and bounded-residual statements used in the main text. The transport program is based on the regularized kernel [formula in source] Three remarks are important. The regulator [formula in source] is not optional: without it the kernel becomes ill-defined exactly where the admissibility question is most delicate. Positivity of

## Information-theoretic and cut-and-project readings

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:55-62](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L55) · `section:8a3d558aff0027052310` · section

This appendix collects interpretive notes that help organize the algebraic structure of the boundary-polarized closed form. When a theorem-level statement appears below, it refers back to a main-text proposition; the appendix itself does not upgrade any status label beyond the declared theorem / derived-consequence / comparison / appendix discipline.

## Prediction semantics and transient event channels

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:340-346](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L340) · `section:c3f6db8e53b1ac74c32a` · section

This appendix section collects the optional semantic decorations of the prediction map and the status note for transient event channels. These items organize downstream interpretation, but they do not add new upstream theorem arrows to the rigid core.

## Transient event status

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex:361-366](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/007-section-yukawa-kernels-and-positivity-lemmas.tex#L361) · `section:6dc4af30cbb0c1ea9ae6` · subsection

The topological burst channel of conj:topological_phase_slip_burst_channel is kept at programmatic-target status. What is fixed in the present version is only the admissible phase-slip channel and its scaling form, not yet a complete defect dynamics or radiative-transfer derivation.

## Table 1: Closed theoretical outputs

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex:33-71](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex#L33) · `section:e5b0bcd49a6753c5f3ff` · subsection

@> p0.09 > p0.11 > p0.10 > p0.04 > p0.18 > p0.20 > p0.08 @ Particle & Repr. & Ext.\ source & [formula in source] & TFPT origin & Internal source & Status \\ 7@l Fermion sector (one family [formula in source] ): \\ [formula in source] & [formula in source] & [formula in source] & [formula in source] & carrier scaffold & hard carrier, [formula in source] & Theorem \\ [formula in source] & [formula in source] & [formula

## Table 2: Empirical comparison rows

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex:72-129](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex#L72) · `section:6f48394f9227dc263658` · subsection

round-mode=none, group-minimum-digits=20 ! @lllllrlrrl@ Quantity & Sector & TFPT formula or source & Metrology\ & Comparison\ & TFPT\ & Unit & Reference\ & Residual & Status \\ 10@l Closed theoretical outputs: \\ [formula in source] & EM & exact [formula in source] closure & [formula in source] \ readout & on-shell Thomson & 137.0359992 & — & 137.03599918 & [formula in source] & Physical observable \\ [formula in sou

## Extended benchmarks

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex:179-183](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex#L179) · `section:3fb1165fb73a951f577a` · section

This appendix turns the broader prediction surface into explicit experimental bookkeeping. The point is not to promote every row to main-text benchmark status, but to keep next test, kill criterion, and dependency structure visible wherever the theory already commits to a concrete target.

## Target and kill-test rows

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex:219-243](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex#L219) · `section:522eab0b31635c22b052` · subsection

round-mode=none, group-minimum-digits=20 ! @> p0.22 > p0.24 > p0.12 > p0.38 @ Test row & TFPT target or prohibition & Status reading & Failure mode \\ Second light Higgs doublet & no additional seam-even\ doublet & kill\ & robust discovery would\ the bosonic-index route \\ Calibrated birefringence null & [formula in source] \ the minimal branch & kill\ & externally calibrated null\ with zero at the\ tolerance would r

## Supplementary UV asymptotic mass-source rows

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex:271-351](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/008-section-closed-theoretical-outputs-and-empirical-compari.tex#L271) · `section:57c2b014c34f4084e9c9` · subsection

The compact main-text mass ledgers intentionally suppress explicit formula detail. The source rows collected here retain that information without forcing the main text to read like a mixed formula notebook. In the present version they are explicitly UV asymptotic source rows: the physical masses belong to the pole-level functor [formula in source] on [formula in source] , whereas the formulas below record the closed-

## Extended comparison ledger

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/009-subsection-extended-comparison-ledger.tex:1-53](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/009-subsection-extended-comparison-ledger.tex#L1) · `section:835be65c1d126b6d0cd5` · subsection

round-mode=none, group-minimum-digits=20 @> p0.14 > p0.28 > p0.18 > p0.15 Y@ Row & TFPT source or target & Metrology\ & Scheme\ & Status note \\ [formula in source] & exact unbroken [formula in source] direction & [formula in source] \\m_ / _ =0 [formula in source] 0 [formula in source] m_g [formula in source] d_O=1 [formula in source] & [formula in source] & exact structural row \\ [formula in source] & threshold ou

## Novelty boundary and literature positioning

[documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/009-subsection-extended-comparison-ledger.tex:54-145](../../../../documents/archive--tfpt-45--source_extracts--technical_companion_source/sections/009-subsection-extended-comparison-ledger.tex#L54) · `section:2153d2675afa0b87c2d3` · subsection

The paper uses standard tools from relative spectral geometry, APS index theory, transport/resolvent language, and conventional RG comparison. The claim of novelty is not that these background ingredients are new in isolation, but that the minimal [formula in source] carrier packet, the compression identities, and the boundary-polarized closed architecture are organized into one tightly overdetermined program. Conver

## Classical theorems used, with full statements

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex:115-186](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/001-section-scope-frozen-input-and-the-necessary-correction.tex#L115) · `section:621b005f0e4aa97fc0f2` · section

Only two external analytic results are used in the proof. They are quoted here in the form needed below.

## Status of the measured QWZ logarithm

[documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/004-subsection-two-edges-and-comparison-with-the-qwz-measure.tex:243-256](../../../../documents/articles--2026-08-28--psi_lambda_convergence_theorem_en/sections/004-subsection-two-edges-and-comparison-with-the-qwz-measure.tex#L243) · `section:cefe6e9e3ebe205d854e` · subsection

The coefficient [formula in source] has a sharp analytic explanation: each chiral boundary contributes [formula in source] and the two boundaries contribute [formula in source] . The measured intercept [formula in source] is nonuniversal and receives bulk, ultraviolet, and finite-width contributions. To turn the coefficient match into a proof for the QWZ collar, one must establish the decomposition in the frozen prob

## Verification of the hypotheses

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex:337-338](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/001-section-setting-and-correction-of-terminology.tex#L337) · `section:f2e7036ac3e83720cfec` · section

No opening prose excerpt; see the source.

## Holomorphy and thermal classification

[documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex:55-67](../../../../documents/articles--2026-08-29--holomorphic_kms_extension_en/sections/002-subsection-the-frozen-car-covariance.tex#L55) · `section:3d2d7b5378d5169e6dd3` · subsection

By [formula in source] The vacuum already contributes one, so there can be no other irreducible DHR sector. Theorem state and no other extreme point. This verifies the analytic hypothesis needed for unconditional rotational KMS uniqueness.

## Front matter / support

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/001-section-concrete-model-and-frozen-finite-input.tex:1-39](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/001-section-concrete-model-and-frozen-finite-input.tex#L1) · `section:b4a9b15bd2f0f6acbebd` · frontmatter

On every finite set of disjoint sixteen-mode clusters we prove exactly that the DET16 Hamiltonian [formula in source] has the unique product ground state [formula in source] , spectrum [formula in source] , and gap one independently of volume. The proof includes the graded-CAR argument: the determinant monomial has even degree sixteen, so local projectors on disjoint clusters commute without an ordering sign. We also

## One DET16 cluster

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/001-section-concrete-model-and-frozen-finite-input.tex:42-78](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/001-section-concrete-model-and-frozen-finite-input.tex#L42) · `section:8bcd1b39df69f2ce6417` · subsection

Let [formula in source] carry the positive-chirality spin representation [formula in source] of [formula in source] and let [formula in source] be its fermionic Fock space. For an ordered orthonormal basis [formula in source] , write [formula in source] and [formula in source] . Put [formula in source] The exact finite computation in verification/v1002_spin10_mirror_projector.py verifies [formula in source] and all f

Explicit source references:

- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_file_citation

## Dynamical finite gauge links: Lie–Schwinger gap theorem

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex:48-276](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex#L48) · `section:42c2beac40084e5dc2c7` · section

Theorem not itself add fluctuating link Hilbert spaces. We therefore audit the finite-group dynamical-link extension first against the local Schrieffer–Wolff construction of Bravyi, DiVincenzo, and Loss BDL2011, and then against the gap theorem proved by Fröhlich and Pizzo FP2020.

## What is and is not explicit in the FP window

[documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex:277-345](../../../../documents/articles--2026-08-30--det16_mirror_gap_theorem_en/sections/002-section-volume-independent-perturbative-stability.tex#L277) · `section:0e3fe3476cf5c8d9f09e` · subsection

The Lie–Schwinger proof contains one explicit series constant: [formula in source] Appendix A of FP2020 uses the explicit convergence restriction [formula in source] Its local-gap estimate also has the explicit sufficient inequality [formula in source] whose positive boundary is [formula in source] . However, the induction closing Theorem 3.4 of FP2020 introduces unevaluated universal constants [formula in source] an

Explicit source references:

- [experiments/tfpt-discovery/det16_dynamical_links_probe.py](../../../../experiments/tfpt-discovery/det16_dynamical_links_probe.py#L1) · explicit_file_citation

## The Charged MMST Scaling-Limit Theorem:\\ A Complete In-House Proof Attempt for SEAM.MMST.TYPEIII.CHARGED.01

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/preamble.tex:1-60](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/preamble.tex#L1) · `section:4183a7d19583b0408c74` · frontmatter

colorlinks=true, linkcolor=blue!55!black, citecolor=blue!55!black, urlcolor=blue!55!black

Explicit source references:

- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row

## Finite audit (numerical support, not proof).

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/002-section-l1-uniform-energy-bounds.tex:295-304](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/002-section-l1-uniform-energy-bounds.tex#L295) · `section:1140c8b5234792a8864a` · paragraph

The companion probe experiments/tfpt-discovery/mmst_ugf_bound_probe.py checks every displayed inequality at [formula in source] . It finds [formula in source] , verifies [formula in source] and the unit edge slope, and rejects both a gapless transverse mutant (whose ratio grows from [formula in source] to [formula in source] ) and the false symbol constant [formula in source] .

Explicit source references:

- [experiments/tfpt-discovery/mmst_ugf_bound_probe.py](../../../../experiments/tfpt-discovery/mmst_ugf_bound_probe.py#L1) · explicit_file_citation

## Finite audit (numerical support, not proof).

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/003-subsection-the-multiplier-rate-extracted-from-ugf.tex:172-189](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/003-subsection-the-multiplier-rate-extracted-from-ugf.tex#L172) · `section:88e790a15d18040fcd87` · paragraph

The companion probe experiments/tfpt-discovery/mmst_tel_probe.py checks [formula in source] . The Gram and compatibility errors are exactly zero, the measured coefficient envelope is [formula in source] , and a smooth-test Wick seminorm fits [formula in source] . A wrong-rate [formula in source] mutant and a non-isometric embedding mutant are both rejected.

Explicit source references:

- [experiments/tfpt-discovery/mmst_tel_probe.py](../../../../experiments/tfpt-discovery/mmst_tel_probe.py#L1) · explicit_file_citation

## Third-angle audit.

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/003-subsection-the-multiplier-rate-extracted-from-ugf.tex:405-411](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/003-subsection-the-multiplier-rate-extracted-from-ugf.tex#L405) · `section:cc93617532a2b2466455` · paragraph

experiments/tfpt-discovery/mmst_telb_tail_probe.py reproduces all six established finite norms, evaluates both embeddings through [formula in source] , verifies the reverse-triangle inequality, and rejects an [formula in source] mutant as an [formula in source] tail. Its verdict is TAIL-TELESCOPING-FAILS; all diagnostic and honesty guards pass.

Explicit source references:

- [experiments/tfpt-discovery/mmst_telb_tail_probe.py](../../../../experiments/tfpt-discovery/mmst_telb_tail_probe.py#L1) · explicit_file_citation

## The neutral net and its index

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/005-subsection-the-neutral-net-and-its-index.tex:1-114](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/005-subsection-the-neutral-net-and-its-index.tex#L1) · `section:a4ec880324ba47c0530f` · subsection

The intended neutral current net is [formula in source] Its central charge is [formula in source] The discriminant groups of [formula in source] and [formula in source] each have order four, so the product lattice net has [formula in source] The isotropic diagonal subgroup generated by [formula in source] has order four. The exact lattice identities verify integer spin, evenness and unimodularity of the extension lat

## Per-lemma status

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/005-subsection-the-neutral-net-and-its-index.tex:176-257](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/005-subsection-the-neutral-net-and-its-index.tex#L176) · `section:2fb6cd875276a150402c` · section

@p0.13 p0.24 p0.16 p0.39 @ Item & Statement & Status & Reason\\ S0 & Frozen generator arithmetic: [formula in source] , [formula in source] , order four, census [formula in source] & & Exact rational lattice calculation; rechecked 10/10.\\ S1 & Neutral bilinear currents and stress tensor have a scaling limit & & Osborne–Stottmeister Theorems 4.11, 4.16 and 5.1; the frozen neutral objects are in the bilinear class.\\ 

Explicit source references:

- [verification/v1025_telb_c1_c2a_certificates.py](../../../../verification/v1025_telb_c1_c2a_certificates.py#L1) · explicit_script_identifier
- [verification/v1026_telb_round4_closure.py](../../../../verification/v1026_telb_round4_closure.py#L1) · explicit_script_identifier
- [verification/v1022_telb_round3_certificates.py](../../../../verification/v1022_telb_round3_certificates.py#L1) · explicit_script_identifier

## The remaining analytic gap

[documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/005-subsection-the-neutral-net-and-its-index.tex:258-330](../../../../documents/articles--2026-08-30--mmst_charged_scaling_limit_en/sections/005-subsection-the-neutral-net-and-its-index.tex#L258) · `section:263c5e01a142571bcd11` · section

red!65!blackred!3 0.92 Remaining microscopic-exhaustion gaps (status 2026-09-05).

Explicit source references:

- [verification/v1026_telb_round4_closure.py](../../../../verification/v1026_telb_round4_closure.py#L1) · explicit_script_identifier

## Conclusion

[documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex:157-212](../../../../documents/articles--2026-08-30--tfpt_thermodynamic_dynamics_en/sections/002-section-existence-of-equilibrium-states.tex#L157) · `section:f1269209928f923042c2` · section

The amended contract makes the continuum limit optional but the thermodynamic limit mandatory. The latter is now proved at the Hamiltonian-class level for the concrete finite-group, finite-local-space TFPT assembly. The proof is insensitive to finite-volume boundary shape and does not infer thermodynamics from a finite scan. Its explicit velocity is conservative, while the numerical witness checks the expected cone, 

## TFPT — Changelog\\[1mm] All changes and new results, by date

[documents/changelog/preamble.tex:1-57](../../../../documents/changelog/preamble.tex#L1) · `section:d85367316428383efbf7` · frontmatter

TFPT — Changelog\\[1mm] All changes and new results, by date Stefan Hamann Alessandro Rizzo This file is the canonical, dated record of every change to the TFPT theory development: new verification modules ( vN), status changes, editorial passes and infrastructure. It is maintained in the same change as the work it records, and it is also imported at the end of the introduction document. Module numbers vN refer to ve

Explicit source references:

- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation

## Appendix: changelog

[documents/changelog/preamble.tex:58-63](../../../../documents/changelog/preamble.tex#L58) · `section:2fca84369c4a253cec63` · section

tocsectionAppendix: changelog The dated record of every change (canonical source: changelog.tex, also compiled standalone). Module numbers vN refer to verification/vN_*.py.

## 2026-10-18: Project separation and retained physics history

[documents/changelog/sections/001-source.tex:1-102](../../../../documents/changelog/sections/001-source.tex#L1) · `section:f091de1c3533bab48372` · subsection

The combined publication history was separated by research ownership. Complete original dated entries remain byte-preserved in the independent archive, including mixed entries that also recorded physical work. The following existing TFPT modules retain their original identifiers and their currently scoped physical, compiler or verification roles. This entry records ownership and preserves history navigation; it does 

Explicit source references:

- [verification/v898_kms_schur_mixing.py](../../../../verification/v898_kms_schur_mixing.py#L1) · explicit_file_citation
- [verification/v880_finite_anchor_theorems.py](../../../../verification/v880_finite_anchor_theorems.py#L1) · explicit_file_citation
- [verification/v639_twist_ope.py](../../../../verification/v639_twist_ope.py#L1) · explicit_file_citation
- [verification/v800_e8_torsor_fourier.py](../../../../verification/v800_e8_torsor_fourier.py#L1) · explicit_file_citation
- [verification/v911_wiring_freedom.py](../../../../verification/v911_wiring_freedom.py#L1) · explicit_file_citation
- [verification/v726_phys_car_pp_index.py](../../../../verification/v726_phys_car_pp_index.py#L1) · explicit_file_citation
- [verification/v715_qgeo_car_continuum.py](../../../../verification/v715_qgeo_car_continuum.py#L1) · explicit_file_citation
- [verification/v646_rm13_reverse.py](../../../../verification/v646_rm13_reverse.py#L1) · explicit_file_citation
- [verification/v799_seam_code_typeii.py](../../../../verification/v799_seam_code_typeii.py#L1) · explicit_file_citation
- [verification/v638_code_semantics.py](../../../../verification/v638_code_semantics.py#L1) · explicit_file_citation
- [verification/v645_klein_rp.py](../../../../verification/v645_klein_rp.py#L1) · explicit_file_citation
- [verification/v650_orbifold_modular.py](../../../../verification/v650_orbifold_modular.py#L1) · explicit_file_citation
- [verification/v834_pg32_flag_completion.py](../../../../verification/v834_pg32_flag_completion.py#L1) · explicit_file_citation
- [verification/v810_cutcode_moment.py](../../../../verification/v810_cutcode_moment.py#L1) · explicit_file_citation
- [verification/v736_orbit_packet.py](../../../../verification/v736_orbit_packet.py#L1) · explicit_file_citation
- [verification/v809_curve_code_doily.py](../../../../verification/v809_curve_code_doily.py#L1) · explicit_file_citation
- [verification/v737_seam48_intertwiner.py](../../../../verification/v737_seam48_intertwiner.py#L1) · explicit_file_citation
- [verification/v664_look_elsewhere.py](../../../../verification/v664_look_elsewhere.py#L1) · explicit_file_citation
- [verification/v628_orbifold_casimir.py](../../../../verification/v628_orbifold_casimir.py#L1) · explicit_file_citation
- [verification/v775_gaussian_class_d5_purity.py](../../../../verification/v775_gaussian_class_d5_purity.py#L1) · explicit_file_citation
- [verification/v757_fano_disc7_bridge.py](../../../../verification/v757_fano_disc7_bridge.py#L1) · explicit_file_citation
- [verification/v814_k5_sixstep_transport.py](../../../../verification/v814_k5_sixstep_transport.py#L1) · explicit_file_citation
- [verification/v987_os_dilation_package.py](../../../../verification/v987_os_dilation_package.py#L1) · explicit_file_citation
- [verification/v857_simplex_fourier_winding.py](../../../../verification/v857_simplex_fourier_winding.py#L1) · explicit_file_citation
- [verification/v752_projective_hamming_incidence.py](../../../../verification/v752_projective_hamming_incidence.py#L1) · explicit_file_citation
- [verification/v782_e8_transition_bus.py](../../../../verification/v782_e8_transition_bus.py#L1) · explicit_file_citation
- [verification/v700_orbit60_census.py](../../../../verification/v700_orbit60_census.py#L1) · explicit_file_citation
- [verification/v779_gnet_gns_arf.py](../../../../verification/v779_gnet_gns_arf.py#L1) · explicit_file_citation
- [verification/v990_wj_transduction_mechanism.py](../../../../verification/v990_wj_transduction_mechanism.py#L1) · explicit_file_citation
- [verification/v621_interacting_semigroup.py](../../../../verification/v621_interacting_semigroup.py#L1) · explicit_file_citation
- [verification/v578_native_jets.py](../../../../verification/v578_native_jets.py#L1) · explicit_file_citation
- [verification/v616_su2_internal_kinematic.py](../../../../verification/v616_su2_internal_kinematic.py#L1) · explicit_file_citation
- [verification/v633_orbit60_quotient.py](../../../../verification/v633_orbit60_quotient.py#L1) · explicit_file_citation
- [verification/v845_cfin_normal_form.py](../../../../verification/v845_cfin_normal_form.py#L1) · explicit_file_citation
- [verification/v1018_e8_directed_readout.py](../../../../verification/v1018_e8_directed_readout.py#L1) · explicit_file_citation
- [verification/v908_seam_equilibrium_wiring.py](../../../../verification/v908_seam_equilibrium_wiring.py#L1) · explicit_file_citation
- [verification/v653_bond_defect.py](../../../../verification/v653_bond_defect.py#L1) · explicit_file_citation
- [verification/v888_finite_pfaffian_signature.py](../../../../verification/v888_finite_pfaffian_signature.py#L1) · explicit_file_citation
- [verification/v874_feedback_decoder_lean.py](../../../../verification/v874_feedback_decoder_lean.py#L1) · explicit_file_citation
- [verification/v632_ftransfer_pgl2.py](../../../../verification/v632_ftransfer_pgl2.py#L1) · explicit_file_citation
- [verification/v858_g31_clock_alphabet.py](../../../../verification/v858_g31_clock_alphabet.py#L1) · explicit_file_citation
- [verification/v778_qgeo_gridsup_logsum.py](../../../../verification/v778_qgeo_gridsup_logsum.py#L1) · explicit_file_citation
- [verification/v832_anchor_flavor_checksum.py](../../../../verification/v832_anchor_flavor_checksum.py#L1) · explicit_file_citation
- [verification/v722_phys_ramified_ns_r.py](../../../../verification/v722_phys_ramified_ns_r.py#L1) · explicit_file_citation
- [verification/v807_lorentz_nullselector.py](../../../../verification/v807_lorentz_nullselector.py#L1) · explicit_file_citation
- [verification/v746_phys_gnet_local_functor.py](../../../../verification/v746_phys_gnet_local_functor.py#L1) · explicit_file_citation
- [verification/v853_bent_css_mangoldt.py](../../../../verification/v853_bent_css_mangoldt.py#L1) · explicit_file_citation
- [verification/v803_e8_jetcode_affine_nsr.py](../../../../verification/v803_e8_jetcode_affine_nsr.py#L1) · explicit_file_citation
- [verification/v805_e8_syndrome_algebra.py](../../../../verification/v805_e8_syndrome_algebra.py#L1) · explicit_file_citation
- [verification/v781_one_object_clock_census.py](../../../../verification/v781_one_object_clock_census.py#L1) · explicit_file_citation
- [verification/v796_duad_syntheme_bridge.py](../../../../verification/v796_duad_syntheme_bridge.py#L1) · explicit_file_citation
- [verification/v878_ledger_integrity.py](../../../../verification/v878_ledger_integrity.py#L1) · explicit_file_citation
- [verification/v690_quartic_half.py](../../../../verification/v690_quartic_half.py#L1) · explicit_file_citation
- [verification/v1019_coxeter_euler_completion.py](../../../../verification/v1019_coxeter_euler_completion.py#L1) · explicit_file_citation
- [verification/v833_gaussian_ramification_ladder.py](../../../../verification/v833_gaussian_ramification_ladder.py#L1) · explicit_file_citation
- [verification/v647_st31_degree24.py](../../../../verification/v647_st31_degree24.py#L1) · explicit_file_citation
- [verification/v903_seam_rp_exclusion.py](../../../../verification/v903_seam_rp_exclusion.py#L1) · explicit_file_citation
- [verification/v802_gnet_martingale.py](../../../../verification/v802_gnet_martingale.py#L1) · explicit_file_citation
- [verification/v783_two_qubit_clifford.py](../../../../verification/v783_two_qubit_clifford.py#L1) · explicit_file_citation
- [verification/v808_petersen_sixthroot.py](../../../../verification/v808_petersen_sixthroot.py#L1) · explicit_file_citation
- [verification/v989_lattice_gate_battery.py](../../../../verification/v989_lattice_gate_battery.py#L1) · explicit_file_citation
- [verification/v626_e8_code.py](../../../../verification/v626_e8_code.py#L1) · explicit_file_citation
- [verification/v991_detline_bulk_edge.py](../../../../verification/v991_detline_bulk_edge.py#L1) · explicit_file_citation
- [verification/v241_dhr_sectors.py](../../../../verification/v241_dhr_sectors.py#L1) · explicit_file_citation
- [verification/v896_wick_block_functor.py](../../../../verification/v896_wick_block_functor.py#L1) · explicit_file_citation
- [verification/v852_arf_vacuum_ovoid.py](../../../../verification/v852_arf_vacuum_ovoid.py#L1) · explicit_file_citation
- [verification/v844_message_doily_rank.py](../../../../verification/v844_message_doily_rank.py#L1) · explicit_file_citation
- [verification/v875_shell_global_lean.py](../../../../verification/v875_shell_global_lean.py#L1) · explicit_file_citation
- [verification/v564_cp_fiber_pin.py](../../../../verification/v564_cp_fiber_pin.py#L1) · explicit_file_citation
- [verification/v774_arf_spinor_compiler.py](../../../../verification/v774_arf_spinor_compiler.py#L1) · explicit_file_citation
- [verification/v988_psi_lambda_reduction.py](../../../../verification/v988_psi_lambda_reduction.py#L1) · explicit_file_citation
- [verification/v798_seam_clifford_modular_s.py](../../../../verification/v798_seam_clifford_modular_s.py#L1) · explicit_file_citation
- [verification/v975_dimension_selector_4d.py](../../../../verification/v975_dimension_selector_4d.py#L1) · explicit_file_citation
- [verification/v679_orbifold_continuum_os.py](../../../../verification/v679_orbifold_continuum_os.py#L1) · explicit_file_citation
- [verification/v812_flavor_graph_filtration.py](../../../../verification/v812_flavor_graph_filtration.py#L1) · explicit_file_citation
- [verification/v849_cfin_unique_cofinal_lean.py](../../../../verification/v849_cfin_unique_cofinal_lean.py#L1) · explicit_file_citation
- [verification/v629_root_incidence.py](../../../../verification/v629_root_incidence.py#L1) · explicit_file_citation
- [verification/v689_gaussian_code_bridge.py](../../../../verification/v689_gaussian_code_bridge.py#L1) · explicit_file_citation
- [verification/v654_st31_degree8.py](../../../../verification/v654_st31_degree8.py#L1) · explicit_file_citation
- [verification/v817_positive_descent_master.py](../../../../verification/v817_positive_descent_master.py#L1) · explicit_file_citation
- [verification/v651_orbifold_assembly.py](../../../../verification/v651_orbifold_assembly.py#L1) · explicit_file_citation
- [verification/v634_st31_structure.py](../../../../verification/v634_st31_structure.py#L1) · explicit_file_citation
- [verification/v561_cp_channel_identities.py](../../../../verification/v561_cp_channel_identities.py#L1) · explicit_file_citation
- [verification/v784_curve_code_2torsion.py](../../../../verification/v784_curve_code_2torsion.py#L1) · explicit_file_citation
- [verification/v973_seam_route_narrowing.py](../../../../verification/v973_seam_route_narrowing.py#L1) · explicit_file_citation
- [verification/v242_spin_statistics_modular.py](../../../../verification/v242_spin_statistics_modular.py#L1) · explicit_file_citation
- [verification/v776_boundary_hamming_uniqueness.py](../../../../verification/v776_boundary_hamming_uniqueness.py#L1) · explicit_file_citation
- [verification/v792_ftransfer_kms_coset.py](../../../../verification/v792_ftransfer_kms_coset.py#L1) · explicit_file_citation
- [verification/v705_chain_deck_sector.py](../../../../verification/v705_chain_deck_sector.py#L1) · explicit_file_citation
- [verification/v745_qgeo_car_l1_sector_lemma.py](../../../../verification/v745_qgeo_car_l1_sector_lemma.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v987) DYN.UNITARY.DILATION.01: B spectral decomp, H=-log B, Wick, congruence ---- Python-only: size-uniform free-band D2/LR (numeric collision), interacting gap plateau, quantum SWAP coupling. *)](../../../../verification/wolfram/tfpt_readouts.wl#L520)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SquareParity.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SquareParity.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/G31WordOrders.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/G31WordOrders.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/G31Orders.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/G31Orders.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/WatataniIndexFour.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/WatataniIndexFour.lean#L1)

## 2026-09-29 (CLXIII): Executable TFPT explorer and consolidated session synthesis

[documents/changelog/sections/001-source.tex:103-121](../../../../documents/changelog/sections/001-source.tex#L103) · `section:c6a235002defa9df2d26` · subsection

The new tfpt_explorer package connects the origin principles, algebraic compiler, geometric and topological structures, physical readouts, and their evidence in an executable process with a guided graphical tour. It includes source browsing, verification and experiment discovery, and a Lean bridge that preserves the distinction between formal statements and executable numerical checks. Six recent source documents and

## 2026-09-07 (CLXI): Non-RH research through Round 27 integrated into repository, papers and website

[documents/changelog/sections/001-source.tex:152-183](../../../../documents/changelog/sections/001-source.tex#L152) · `section:04b5cf8557bf29474e32` · subsection

The previously local theory-contract archive is shipped with its proofs, source-pinned checkers and immutable per-round validation snapshots. The intervening geometry, positive-parent, constraint-domain and charge transport branches retain their distinct hypotheses and additional off-shell inputs; they are not combined into a claimed microscopic TOE. The contracts paper now includes the full-reference argument for th

Explicit source references:

- [verification/v472_quillen_detline_moduli.py](../../../../verification/v472_quillen_detline_moduli.py#L1) · explicit_file_citation

## =150 2026-09-05 (CLVII) (non-RH T1–T8 Round 3 graduates as v1022– v1025; suite [formula in source] , ledger rows [formula in source] through six narrow subcontracts; [formula in source] module checks; NO marker move; TFPT.TOE.COMPLETE.01 and every T1–T8 gate remain ). v1022_ telb_ round3_ certificates.py ( [formula in source] ; native python-flint==0.9.0, 256-bit Arb/Acb) replaces the float/Richardson TEL-B input by 5812 rational cells and the exact cut jump, proving [formula in source] and [formula in source] . Together with the stated analytic digamma/midpoint lemmas, its executable Arb arithmetic gives [formula in source] , [formula in source] and [formula in source] ; full C2b remains open exactly at CF [formula in source] and DG [formula in source] . Its exact one-mode [formula in source] countermodel refutes the former ALG2 Vandermonde-to-generated-algebra implication: FE-GEN or an exact gauge/code-projected microscopic-algebra theorem is still required, and ALG1 remains conditional on the generated projection. v1025_ telb_ c1_ c2a_ certificates.py ( [formula in source] ; native 100-bit Arb/Acb) executes the existing analytic C1/C2a proofs: [formula in source] and [formula in source] for every even [formula in source] . v1023_ derivative_ filtered_ wall.py ( [formula in source] ) proves only the finite quasi-free singular-value block: the high continuation branch is separated, but the bare [formula in source] subspace is not invariant, the low branch has [formula in source] rather than a Weyl cone, and no DET16/DET32, interacting-parent, measure/anomaly/index or [formula in source] D theorem follows. v1024_ parent_ internal_ boundaries.py ( [formula in source] ) supplies finite parent-internal T6–T8 witnesses and no-gos: a positive seam/neutrino-pair intertwiner with projective full-Fock [formula in source] lift but no mass texture; the uniform-gap and direct-TT locality obstructions but no graviton; and a gapped internal [formula in source] cap that is chosen, [formula in source] -breaking and complement-trivial, hence no global [formula in source] . T1 retains only finite axiom-core/W-bridge support while unconditional provenance and the dimension selector remain open; T3 remains at Hamiltonian-class level; T5 retains finite IR witnesses and the v1020 spectator obstruction while prime completion, OS reconstruction, confinement and scattering remain open. The common missing object is still one shared [formula in source] D parent satisfying T3–T8. Native-only handling is explicit in the website reproducer; v1022/v1025 are not represented as Pyodide certificates. NO RH CLAIM. Surfaces: tfpt_research_contracts, tfpt_4_frontier, introduction, tfpt_2_standard_model, the MMST article/PDF, ledger, generated verification maps/index, website paper/DAG/gap/FAQ mirrors and changelog.

[documents/changelog/sections/001-source.tex:280-280](../../../../documents/changelog/sections/001-source.tex#L280) · `section:17757402db902787518b` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v1023_derivative_filtered_wall.py](../../../../verification/v1023_derivative_filtered_wall.py#L1) · explicit_file_citation
- [verification/v1022_telb_round3_certificates.py](../../../../verification/v1022_telb_round3_certificates.py#L1) · explicit_file_citation
- [verification/v1025_telb_c1_c2a_certificates.py](../../../../verification/v1025_telb_c1_c2a_certificates.py#L1) · explicit_file_citation
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1020_spectator_sector_obstruction.py](../../../../verification/v1020_spectator_sector_obstruction.py#L1) · explicit_script_identifier

## =150 2026-09-04 (CLIV) (TEL-B reduction absorbed into the SEAM.MMST.TYPEIII.CHARGED.01 contract text and ledger row; NO marker move, status stays ). The standalone note articles/2026-09-04/telb_bound_b_sketch.tex is superseded and removed: the contract is now the single home. Cover identity [formula in source] sawtooth split [formula in source] ; bound (A) certified numerically for all [formula in source] ( [formula in source] , all-mode BV, one float64 TV constant); bound (B) reduced to [formula in source] (measured [formula in source] ), open items C1/C2a/C2b. Residual restated as TEL-B-EXTERNAL (2026-09-04 reduction); the [formula in source] dyadic-increment route is superseded (measured [formula in source] at r645, no longer the route). Numerically [formula in source] , conditional analytic [formula in source] ; analytically open. Evidence (experiments, not veri-citable): mmst_telb_trace_decomposition_probe.py, mmst_telb_cover_split_probe.py, mmst_telb_bound_a_probe.py ( [formula in source] ), mmst_telb_bound_b_probe.py ( [formula in source] , G18–G20 open by design). Surfaces: tfpt_research_contracts (new TEL-B reduction subsection); ledger row claim text only; website changelog.ts regenerated.

[documents/changelog/sections/001-source.tex:281-281](../../../../documents/changelog/sections/001-source.tex#L281) · `section:aa4a70b2117802d4bb85` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [experiments/tfpt-discovery/mmst_telb_cover_split_probe.py](../../../../experiments/tfpt-discovery/mmst_telb_cover_split_probe.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/mmst_telb_bound_a_probe.py](../../../../experiments/tfpt-discovery/mmst_telb_bound_a_probe.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/mmst_telb_trace_decomposition_probe.py](../../../../experiments/tfpt-discovery/mmst_telb_trace_decomposition_probe.py#L1) · explicit_file_citation
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [experiments/tfpt-discovery/mmst_telb_bound_b_probe.py](../../../../experiments/tfpt-discovery/mmst_telb_bound_b_probe.py#L1) · explicit_file_citation

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

## =150 2026-08-28 (CXL) (review wave 3 — the third external bird's-eye review adjudicated and integrated: ONE new module v993 plus THREE new \ contracts plus a v986 motivation retype plus the dual-rest formula; suite [formula in source] , ledger [formula in source] ; NO status-marker upgrades; Python-only / Wolfram mirror deferred as for v974–v992). (1) v993_ minimal_ defect_ selector.py ( [formula in source] ): the FULL rank-8 ADE census (SNF of Cartan) with cyclic [formula in source] glue on BOTH factors selects [formula in source] uniquely ( [formula in source] aliases collapsed) — the [formula in source] architecture of v624 is an OUTPUT of (rank 8 [formula in source] cyclic [formula in source] ), not an INPUT; kill tests [formula in source] / [formula in source] (product 16, fail cyclicity) and the [formula in source] control [formula in source] ; [formula in source] exact (lattice shadow of [formula in source] ); the [formula in source] average is the UNIQUE trace-preserving finite conditional expectation (uniqueness needs the module property; kernel dim [formula in source] without it). Ledger notes on AX.P1.01/ AX.P2.01: axiom typing UNCHANGED; the equidistribution identification stays the open \ of v813; cited-not-proved remain [formula in source] and holomorphic uniqueness of [formula in source] . SEAM.SIMPLECURRENT.GENERATOR.01 canonical status grows the [formula in source] parity-shadow line. (2) Three new research contracts, all , no scripts: GAUGE.DETLINE.FIXPOINT.01 (all three gauge couplings as unique stationary points of one nonabelian zeta-det/inflow functional; generalizes ALPHA.QUILLEN.EXACT.01; honest: [formula in source] is currently an external input); GRAV.SPIN2.EMERGENCE.01 (massless transversal spin-2 pole from the same spectral determinant; Einstein equation stays downstream/conditional; GRAV.NONCIRCULAR.01 binding); FTRANSFER.SK.RHO0.01 (cosmological transfers need [formula in source] , not [formula in source] alone; typed candidate [formula in source] , [formula in source] orientation picks [formula in source] ; FTRANSFER.GENERATING.01 covers equilibrium only). (3) v986 docstring retype: the [formula in source] motivation is loose ( [formula in source] ); the operator reading is the [formula in source] eigenvalue route [formula in source] ; texture data-constrains-texture; check logic and pass/fail UNCHANGED. (4) Dual rest: introduction status card (and the research-contracts keybox, with a brief frontier mirror) now carries [formula in source] (compiler) beside [formula in source] (strict-physical-TOE accounting of the 2026-08-27/28 contract wave); nothing in the second formula is claimed closed. Exploration not promoted: the wave-3 Quillen zero-mode Gram identity is a reformulation ( [formula in source] ), not a Quillen-metric object.

[documents/changelog/sections/001-source.tex:301-303](../../../../documents/changelog/sections/001-source.tex#L301) · `section:c86ec693b903bfd2aa01` · subsection

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v993_minimal_defect_selector.py](../../../../verification/v993_minimal_defect_selector.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [verification/v624_external_lattice_audit.py](../../../../verification/v624_external_lattice_audit.py#L1) · explicit_script_identifier
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [verification/v813_p1_index_kms.py](../../../../verification/v813_p1_index_kms.py#L1) · explicit_script_identifier
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [verification/v992_joint_likelihood_v1.py](../../../../verification/v992_joint_likelihood_v1.py#L1) · explicit_script_identifier
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [verification/v986_nu_scalaron_rung.py](../../../../verification/v986_nu_scalaron_rung.py#L1) · explicit_script_identifier
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_script_identifier
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean#L1)
- [(* ---- (v993) AX.P2.01 census: SNF disc groups, unique (D5,A3), [lambda]^2=[v], CE dims ---- Python-only: random CE axiom sampling on M_d^{Z4} / crossed product. *)](../../../../verification/wolfram/tfpt_readouts.wl#L557)
