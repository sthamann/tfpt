# Verification, formalization and safeguards — part 5

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Summary of Claims and Status

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/010-section-texorpdfstring-beta-text-rad-centric-identity-su.tex:75-140](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/010-section-texorpdfstring-beta-text-rad-centric-identity-su.tex#L75) · `section:f85f91d5236e161a822a` · section

@p3cmp4cmp3cmp5.2cm@ TFPT status dashboard. ``Exact'': [formula in source] ; ``Solid'': [formula in source] ; ``Minor'': [formula in source] ; ``Moderate'': [formula in source] . Domain & Quantity & Deviation & Status\\ Domain & Quantity & Deviation & Status\\ 4r Continued on next page.\\ 4l Structural (parameter-free)\\ CFE & [formula in source] & [formula in source] & green!60!black Derived (double cover + [formula

## Diagnostic [formula in source] g Variants (Internal Sanity Checks)

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/010-section-texorpdfstring-beta-text-rad-centric-identity-su.tex:244-256](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/010-section-texorpdfstring-beta-text-rad-centric-identity-su.tex#L244) · `section:201bba2851d879c60273` · section

The suite records legacy diagnostic templates in which [formula in source] is varied away from the holonomy value [formula in source] (e.g.\ the ordered-occupancy [formula in source] template). These runs are used only to verify that the defect-sector response is sensitive to discrete holonomy choices and to quantify the direction of the shift in [formula in source] . They are explicitly not used for parameter select

## Verification Suite Summary

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/011-section-coefficient-policy-sketch-for-the-cfe.tex:197-229](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/011-section-coefficient-policy-sketch-for-the-cfe.tex#L197) · `section:5f1b19931dba2fd8357e` · section

The TFPT verification suite turns paper claims into deterministic, assumption-explicit computations. All counts in this section are auto-generated from the suite artifacts (no hardcoded ``39 modules''): [formula in source] Version breakdown: v2.5: 91, v2.7: 44, v2.8: 96, v2.8-t7: 4. Category breakdown: supplementary 107, kernel 64, policy 25, closed_interface 21, crosslink 12, dashboard 2, search_tool 2.

Explicit source references:

- [verification/v28_gravity_fR.py](../../../../verification/v28_gravity_fR.py#L1) · explicit_script_identifier

## Known Gaps and Status (Summary)

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/011-section-coefficient-policy-sketch-for-the-cfe.tex:230-236](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/011-section-coefficient-policy-sketch-for-the-cfe.tex#L230) · `section:56a2ec6b29bbc7621648` · subsection

For the PRL-facing manuscript we omit the auto-generated flagged/open inventory and list open interfaces only as conditional statements in the main text. The full suite manifest (with module-level status and plot inventories) is included in the replication bundle referenced in Appendix

## [formula in source] consolidation policy.

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/012-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex:126-236](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/012-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex#L126) · `section:642926e0ae6650eb954a` · paragraph

The suite computes [formula in source] through 12 internal pathways (spread [formula in source] ). The authoritative value reported in the PRL claim surface is [formula in source] from module h0_diagnostic_closure_v28; all other [formula in source] pathways are classified as diagnostics. The suite contract ( h0_source_contract_audit_v1, PASS) enforces this hierarchy: only one module feeds [formula in source] into the

## E [formula in source] Chain CertificateE8 Chain Certificate

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/012-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex:237-243](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/012-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex#L237) · `section:1fb29c4b21777d0eff0f` · section

This appendix provides the complete verification data for the E [formula in source] chain uniqueness theorem (Theorem

## Verification Algorithm

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/012-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex:279-293](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/012-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex#L279) · `section:7e8b73da2852b8d70b50` · subsection

The uniqueness is verified by: Constructing the complete Hasse diagram of [formula in source] from standard tables. Computing all cover relations with [formula in source] . Running dynamic programming to find all paths from [formula in source] to [formula in source] . Applying the cost function [formula in source] (second-difference smoothness). Verifying that the minimum-cost path is unique (cost gap to second-best 

## Status note

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex:194-198](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex#L194) · `section:4ea097f9b1fd871dc6c9` · subsection

The spin-lift argument fixes the [formula in source] deficit factor robustly, and the sector count is fixed by seam symmetry. The seam normalization is provided by the [formula in source] -gluing derivation in Appendix

## Reproducibility

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex:292-348](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex#L292) · `section:133bbb3fdecc0149db2a` · section

Replication package: All numerical results can be reproduced using the TFPT verification suite (v2.8).

Explicit source references:

- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation

## Reference snapshot pinning.

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex:349-356](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex#L349) · `section:8682b8e9897e94a66fb4` · paragraph

All external reference values (CODATA, PDG, lattice QCD, etc.)\ used by the suite carry mandatory snapshot_date and source_version fields. A dedicated audit ( reference_snapshot_pin_audit) scans all data JSONs and fails if any reference-like entry lacks these fields. Status (v2.8): 42 missing pins out of 167 reference entries identified (audit PASS); resolution is tracked as an informational item.

## Paper–suite number sync.

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex:357-362](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex#L357) · `section:88efaf184d493417ae0f` · paragraph

A separate audit ( paper_table_number_sync_audit_v28) parses all \ table values and compares against suite JSON outputs at rounding tolerance. Extracted 22 TFPT*Num commands; compared 8 quantities at 12-digit tolerance—all match.

## Prediction Ledger and Falsification

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:1-68](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L1) · `section:b50789cf4459ce0a8c38` · section

Purpose: Provide a single, reviewer-friendly list of predictions and candidates that is tied to the same JSON sources used by the verification suite, to prevent number drift between Abstract, theorems, tables, and appendices.

## Identity Catalogue and Status Labels

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:69-112](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L69) · `section:9e86c5ebb859da9a65e0` · section

This appendix labels frequently used equalities by logical status to prevent conflating definitions, algebraic rewrites, and genuine predictions.

## One-Loop Effective Action in Riemann–Cartan and the [formula in source] CoefficientOne-Loop Effective Action in Riemann–Cartan and the R2 Coefficient

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:113-126](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L113) · `section:d37517cafc566fab505c` · section

K1: Field content and torsionful Lagrangian fixed by the minimal UFE sector. K2: Quadratic fluctuation operator is of Laplace type after background-field gauge fixing. K3: Heat-kernel coefficient [formula in source] captures the curvature-squared terms in [formula in source] . K4: Matching to [formula in source] after imposing the GR renormalization condition.

## K.1 Setup

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:127-132](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L127) · `section:c3405563e2d865d60bdd` · subsection

We evaluate the one-loop effective action in a Riemann–Cartan background with torsion decomposed into axial [formula in source] , trace [formula in source] , and tensor [formula in source] . The minimal UFE choice treats torsion at quadratic order, so integrating out torsion is Gaussian and parameter-free once [formula in source] fixes the normalization of the coupling.

## K.2 Operator Form

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:133-141](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L133) · `section:fd4ae19cc07e7b0eab76` · subsection

After background-field gauge fixing, the quadratic operator for torsion fluctuations can be written in Laplace type, with [formula in source] built from curvature and torsion invariants. The contribution to [formula in source] is [formula in source] .

## K.3 Heat-Kernel Coefficients

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:142-149](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L142) · `section:29e161c42ba84fe98d69` · subsection

The local part of [formula in source] is governed by the heat-kernel expansion where [formula in source] contains the curvature-squared terms. The torsion-dependent pieces combine into an effective [formula in source] operator in the low-energy action.

## K.4 Renormalization Condition

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:150-153](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L150) · `section:35445d2b62922b9bd87d` · subsection

The GR limit (A8) fixes the renormalization scheme by requiring that the [formula in source] limit reduces to the Einstein–Hilbert action with coefficient [formula in source] .

## K.5 TFPT Closure

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:154-162](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L154) · `section:64f8d7fff52e888f685c` · subsection

With the TFPT normalization of the torsion sector, the induced [formula in source] coefficient is fixed by [formula in source] , yielding which reproduces

## Bounce Perturbations and the Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:163-172](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L163) · `section:7807e515caaf85260363` · section

This appendix provides a minimal outline; the full numerical transfer-function evaluation is implemented in the bounce_perturbations verification module (see replication bundle).

## L.1 Background Solution

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:173-177](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L173) · `section:b13c114938fb2c09d995` · subsection

The bounce background is modeled by a smooth scale factor [formula in source] where the torsion-induced [formula in source] term regularizes [formula in source] for scalar perturbations. The transition to the [formula in source] inflationary phase is implemented by matching [formula in source] and its derivatives at [formula in source] .

## L.2 Numerical Integration Setup

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:178-182](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L178) · `section:5df7c17b841324b93925` · subsection

Mode functions are initialized in an adiabatic vacuum well before the bounce and integrated through the bounce and into the [formula in source] era. The numerical scheme records the transfer function by comparing late-time solutions to the pure [formula in source] baseline.

## L.3 Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:183-190](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L183) · `section:7a501231de6e8858e342` · subsection

Define the transfer function as with [formula in source] for modes well inside the horizon during the bounce and deviations confined to [formula in source] .

## L.5 Falsification Targets

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/015-subsection-texorpdfstring-l-4-the-k-to-ell-gate-cmb-obse.tex:278-283](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/015-subsection-texorpdfstring-l-4-the-k-to-ell-gate-cmb-obse.tex#L278) · `section:99186b58fa651338355f` · subsection

Large-scale suppression or oscillatory features in [formula in source] are predicted at [formula in source] . Current CMB large-scale bounds constrain the allowable feature amplitude, providing a direct observational test of the bounce completion.

## Reference Ledger (Auto-Generated)

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/015-subsection-texorpdfstring-l-4-the-k-to-ell-gate-cmb-obse.tex:324-393](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/015-subsection-texorpdfstring-l-4-the-k-to-ell-gate-cmb-obse.tex#L324) · `section:53d7ed66963432bf34f7` · section

=0mu plus 1mu @> p0.22 > p0.14 > p0.08 > p0.10 > p0.12 > p0.24 @ Reference ledger used by the TFPT suite (auto-generated). Key & Value & [formula in source] & Units & Version & Source (stable key)\\ Key & Value & [formula in source] & Units & Version & Source (stable key)\\ 6r Continued on next page.\\ A_s_planck2018 & 2.09890e-9 & 0.02938e-9 & dimensionless & Planck 2018 & planck2018 Planck 2018 results VI (2020), b

## Referee Exit Snapshot — Version 2.8

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/016-section-referee-exit-snapshot-version-2-8.tex:1-37](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/016-section-referee-exit-snapshot-version-2-8.tex#L1) · `section:6f1dc76a77b248010354` · section

This appendix summarizes the closed gates and solver outcomes from the v2.8 referee exit snapshot (run date: 2026-02-08, git commit b9d26d4). All 235 modules achieved PASS status; 0 WARN, 0 FAIL.

Explicit source references:

- [verification/v28_gravity_fR.py](../../../../verification/v28_gravity_fR.py#L1) · explicit_script_identifier

## Reference snapshot policy.

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/016-section-referee-exit-snapshot-version-2-8.tex:38-180](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/016-section-referee-exit-snapshot-version-2-8.tex#L38) · `section:7972e0e8abaebba6048f` · paragraph

All experimental reference values used by the verification suite are pinned to a specific publication date or data release. Where a DOI or arXiv identifier exists, it is recorded in the bibliography below and in the suite's sm_inputs_mz.json policy file. Online-only resources (NuFIT, PDG online tables) carry a snapshot date. This ensures that results are reproducible even if upstream databases update: the suite alway

## Reading guide and claim map

[documents/archive--paper-latex--tfpt-v30/sections/001-section-reading-guide-and-claim-map.tex:24-105](../../../../documents/archive--paper-latex--tfpt-v30/sections/001-section-reading-guide-and-claim-map.tex#L24) · `section:5d2060d452f578617756` · section

The paper is organized in three reading layers: Big picture: one section explains what TFPT claims in plain language before the detailed datum and conventions begin. Detail: the main body then runs from primitive core and hard carrier kernel through kernel numerics, the two completion programs, the particle/mass compiler, and the benchmark interface. Proof sketches: the main text gives only the central proof sketches

## Particle and mass compiler

[documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex:63-72](../../../../documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex#L63) · `section:8dfc6ca79b32627dc35f` · section

This section is the phenomenological heart of the manuscript. It is not meant to flatten all rows into one uniform notion of prediction. Instead it makes the compiler interface explicit: a declared RG map, a kernel-output map, and a mass ledger that separates genuinely derived quantities from solver-level candidates and anchor-dependent comparison rows. Accordingly this section is best read through three ledgers: a p

## Mass-closure ledgers

[documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex:123-175](../../../../documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex#L123) · `section:bfbfa83f9c9d2c119922` · subsection

For the mass surface itself the main text now uses only three row-level status words: derived, candidate, and anchor-dependent. The explicit candidate formulas, neutrino rows, and transport-ratio source data are moved to the appendix so that the main text shows a compact comparison-ready ledger rather than a mixed formula dump.

## Primary benchmark map and prediction ledger

[documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex:289-346](../../../../documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex#L289) · `section:c32b199117df78dc771e` · section

The comparison values used in this section follow representative CODATA, PDG, NuFIT, Planck, and birefringence references codata2022,pdg2025,nufit2025,planck2018,minamiKomatsu2020,eskilt2023,sullivan2025. The main-text table is intentionally restricted to six rows whose comparison language is already reasonably convention-complete. The compact mass surface is given separately in tab:sm-mass-ledger-ew,tab:sm-mass-ledg

## Compact prediction ledger

[documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex:347-371](../../../../documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex#L347) · `section:e95b82b61b2b498c588f` · subsection

The main benchmark table shows only a narrow comparison surface. To keep the compiler structure visible, tab:prediction-ledger summarizes which output packages belong to which layer of the paper.

## Falsification matrix

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:47-67](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L47) · `section:230265151fe86b2efd87` · subsection

@> p0.24 YY> p0.13 @ Statement & What would falsify it & Sector affected & Local or global failure \\ Minimal carrier [formula in source] & failure to recover the one-family packet or the global quotient from the carrier theorem & Hard & global \\ Family bridge and [formula in source] & no geometric monodromy interpretation of the three-cycle family space & Bridge & local-to-structural \\ Bosonic relative index selec

## Conditional master theorem and finite proof obligations

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:68-69](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L68) · `section:428218e29da53dacf38b` · section

No opening prose excerpt; see the source.

## Compiler chain

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:70-90](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L70) · `section:4b2358c66466d0ebf0a9` · subsection

Collecting the present hard, bridge, and completion layers, the intended compiler line is This line is not meant as a slogan. Each arrow is attached either to a hard theorem, a bridge construction, or one of the explicit completion interfaces listed in the proof-obligation table below.

## Conditional master theorem

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:91-100](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L91) · `section:f749a2d6a8938dd337e7` · subsection

Assume the hard carrier and kernel layers summarized in tab:status-matrix, together with the completion statements of the geometric and transport programs and the declared comparison map [formula in source] . Then every observable in the present main-text scope is the output of one carrier-first relative spectral compiler from primitive seam data to scheme-specified observables.

## Finite proof obligations

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:101-120](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L101) · `section:3a3a9df38f284e056b4e` · subsection

@> p0.20 > p0.18 > p0.20 YY@ Target statement & Input data & Missing lemma & Minimal deliverable & Empirical consequence \\ Family space theorem & [formula in source] , [formula in source] , [formula in source] & monodromy-to-family theorem & derive [formula in source] from the seam cycle algebra & stabilizes the meaning of [formula in source] \\ Bosonic index closure & [formula in source] , [formula in source] & rel

## Extended comparison rows and supplementary checks

[documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex:352-372](../../../../documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex#L352) · `section:5f85cf9292b7ea5b05e1` · subsection

@> p0.18 > p0.17 > p0.17 > p0.22 > p0.14 @ Observable & TFPT value & Reference value & Role & Status \\ [formula in source] & 1.198 rad & 1.196 rad & unresolved transport comparison & appendix comparison row \\ [formula in source] & 134.979 MeV & 134.977 MeV & hadronic out-of-sample check & appendix comparison row \\ [formula in source] & 0.0015 eV & [formula in source] eV & neutrinoless double-beta interface & appen

## Supplementary mass-source rows

[documents/archive--paper-latex--tfpt-v30/sections/007-subsection-supplementary-mass-source-rows.tex:1-89](../../../../documents/archive--paper-latex--tfpt-v30/sections/007-subsection-supplementary-mass-source-rows.tex#L1) · `section:4026b8980d3f8fe48a93` · subsection

The compact main-text mass ledgers intentionally suppress explicit formula detail. The source rows collected here retain that information without forcing the main text to read like a mixed formula notebook.

## What TFPT Claims

[documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex:81-107](../../../../documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex#L81) · `section:df72377a33dede842c24` · section

TFPT is organized as a boundary-polarized spectral theory whose primitive input is a one-sided boundary datum [formula in source] The main theorem chain in the source draft is not a collection of unrelated numerological readouts. It is a staged reconstruction: [formula in source] The split series follows this burden of proof rather than the order in which a reader might find the numerics exciting.

## What TFPT Does Not Claim at This Level

[documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex:108-114](../../../../documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex#L108) · `section:30e89d37033771ef4ad1` · section

The orientation note does not certify every downstream comparison row as a theorem. In particular, the CMB interface, sky-map realization, horizon continuations, transient channels, and E8 scale grammar remain outside the primitive theorem chain. They are comparison and programmatic layers unless explicitly promoted by a later proof obligation.

## Status Matrix

[documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex:129-232](../../../../documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex#L129) · `section:9070e49b58a12ef7b1e8` · section

@p0.24 p0.08 p0.22 Y@ Layer & Tier & Lean-side target / reference & Notes / location \\ Boundary primitive kernel: algebraic shadow & L & BoundaryPolarization, BoundaryPolarization.ofCarrierInvolution & Algebraic equivalence between the polarisation picture and the involution picture is Lean-proved. Paper 1 + Lean note. \\ Boundary primitive kernel: analytic Paper-1 content & I & target type BoundaryPolarization & An

Explicit source references:

- [BoundaryPolarization.ofCarrierInvolution](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L184) · explicit_lean_symbol

## Source Boundary

[documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex:265-276](../../../../documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex#L265) · `section:7380db88a0ce2f695437` · section

The orientation note draws especially from the abstract, the closed-architecture box, Sections 1 and 2, the canonical rigid-object discussion, the structural falsification map, and the conclusion. It intentionally does not import the extended empirical ledgers, E8 stage atlas, CMB figures, or mass tables.

## Main Technical Development

[documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex:277-288](../../../../documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex#L277) · `section:269f4f814a11de4a62f4` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

## Claim Map

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:90-110](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L90) · `section:f388f7f941baf59b7f2f` · section

The paper proves the first load-bearing arrow of the TFPT series: [formula in source] All later discrete, physical, and numerical structures are treated as unavailable here. The purpose is to make the boundary primitive kernel auditable on its own.

## One-Sided Boundary Datum

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:111-120](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L111) · `section:bc4b9e813b85171a99d2` · section

The starting object is [formula in source] The paper should keep only the source manuscript material needed to explain one-sided admissible data, induced boundary spectral data, and the passage to a doubled closed datum. The proof burden is that the primitive boundary structure is not chosen by hand.

## Boundary Primitive Kernel

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:152-201](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L152) · `section:6c04e27ea5f61161b8ac` · section

Under the one-sided boundary hypotheses and the primitive admissibility assumptions stated above, the minimal boundary datum canonically determines [formula in source] In particular, the Calderon polarization induces a direct-sum decomposition [formula in source] which (passed to the finite essential carrier [formula in source] ) inhabits the Lean-side target type BoundaryPolarization.

Explicit source references:

- [TFPT.Carrier.BoundaryPolarization.BoundaryPolarization](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L83) · explicit_lean_symbol

## Audit Protocol

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:202-218](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L202) · `section:6adae73f1df7ba8e0997` · section

@p0.24 Y@ Audit item & Question \\ One-sided datum & Is every primitive object reconstructed from [formula in source] or from standard boundary spectral data? \\ Calderon interface & Are regularity and projection hypotheses explicit? \\ Primitive selector & Does [formula in source] precede the later singlet and determinant projections? \\ Winding class & Is [formula in source] fixed before any family or flavor interp

## Main Technical Development

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:219-224](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L219) · `section:5aaaf13de56926aa7b0c` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

## tfptblue The [formula in source] Hypercharge Carrier Rigidity Theorem\\[0.35em] with Lean-Verified Algebraic Core and Standard-Model Packet Outlook

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/preamble.tex:1-8](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/preamble.tex#L1) · `section:609a9f667334de63d8c3` · frontmatter

tfptblue The [formula in source] Hypercharge Carrier Rigidity Theorem\\[0.35em] with Lean-Verified Algebraic Core and Standard-Model Packet Outlook Stefan Hamann Alessandro Rizzo tfptgray Paper 2 of the TFPT 4.5 series –

## Front matter / support

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/001-section-formal-status-of-the-carrier-theorem.tex:1-157](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/001-section-formal-status-of-the-carrier-theorem.tex#L1) · `section:e7c01a6c3406a761655d` · frontmatter

This paper proves the algebraic core of TFPT's carrier theorem and, separately, sketches its Standard-Model packet outlook. The carrier core takes four explicit interfaces — a carrier involution [formula in source] , a Higgs rank- [formula in source] interface [formula in source] , a Yukawa Stage-D trilinear interface [formula in source] with operational contraction predicates, and a primitive oriented determinant-pr

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation

## Formal Status of the Carrier Theorem

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/001-section-formal-status-of-the-carrier-theorem.tex:158-195](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/001-section-formal-status-of-the-carrier-theorem.tex#L158) · `section:0f984a39c60f6affc3f9` · section

This paper separates the carrier rigidity theorem (Status A, Lean verified) from the Standard-Model packet outlook (Status C, downstream).

## Carrier Polynomial as a Corollary

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/001-section-formal-status-of-the-carrier-theorem.tex:196-362](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/001-section-formal-status-of-the-carrier-theorem.tex#L196) · `section:6bc4166c0d9d406c8109` · section

The paper does not begin by assuming [formula in source] It begins with the carrier involution induced by the boundary polarization: [formula in source] At this stage there is only a two-point algebra [formula in source] No [formula in source] split, hypercharge vector, Standard-Model packet, or electromagnetic number has been used.

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation

## Seam Winding as Source of the Integer Conditions

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:1-37](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L1) · `section:88b221f684aadec7b605` · section

The integer triple [formula in source] entering input (iii) of thm:carrier-rigidity is not assumed: it is the algebraic shadow of TFPT's seam class [formula in source] . The TFPT-side statement is the three-way obligation [formula in source] None of the three conjuncts is presented as a Lean theorem here; each is a Status-B obligation of TFPT's seam-class theory. Their joint Lean target is [formula in source] which i

Explicit source references:

- [TFPT.Carrier.SeamWindingInterface.SeamWindingData](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L55) · explicit_lean_symbol

## Hypercharge and Gauge Quotient (Status C outlook)

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:38-71](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L38) · `section:ce1f81ead18a4df70689` · section

The remainder of this paper presents the Standard-Model packet outlook conditional on thm:carrier-rigidity. These sections are Status C (mathematical proposal): they are not part of the Lean-verified core and are not signature-locked in AuditContract.lean. The text below indicates this consistently.

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation

## One-Family Packet (Status C outlook)

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:72-87](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L72) · `section:2bce487ef88d07973605` · section

The spinor packet is conjectured to be [formula in source] This section sketches the one-family decomposition including the right-handed neutrino state. Character identities, trace identities, and the abelian index belong here. The expected Lean target is a DerivedSMRepresentations module bundling LinearMap.dualHypercharge, ExteriorPower.hypercharge, and TensorProduct.hypercharge; not yet present in the Lean note.

## Discharging the Rank and Exterior Premises

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:88-102](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L88) · `section:b8e98635e3856fc5cb88` · section

The editorial risk is that [formula in source] look like disguised Standard-Model inputs. In v10/v11 of the Lean note this risk is mitigated: [formula in source] follows from [formula in source] via the Lean theorem exteriorPower.finrank_eq; and [formula in source] is the duality content of Yukawa Stage C ( PrimitiveIndecomposableYukawaCoupling), itself derived from Stage D under [formula in source] . The value-level

Explicit source references:

- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)

## Counting Outputs (Status C outlook)

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:103-120](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L103) · `section:6da906e02004f451f5ec` · section

This paper outlines, conditional on the Status-A carrier core and on as-yet-open Status-B content (representation theory of the carrier datum), the discrete counting outputs: [formula in source] These are not Lean theorems and not precision-observable readouts. Their TFPT-side derivation from carrier, seam winding, occupancy, and compact Higgs index closure is the mathematical proposal of TFPT Paper 2's downstream la

## Main Result — Carrier Rigidity (Status A)

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:121-138](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L121) · `section:aeff849bdc90f1763b6b` · section

thm:carrier-rigidity is the main result of this paper. We restate it as a single declarative summary:

## Audit Protocol

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:139-193](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L139) · `section:19f60a3ad3a6dcccf462` · section

Status A audit (Lean).\ The Lean-verified core is audited by the seven-check audit.sh gate of the companion Lean note. The audit gate covers: lake build, no sorry/ admit, no axiom/ constant declarations, no unsafe/ opaque/ partial, every headline depends only on [formula in source] , every headline elaborates via \#check ( AuditCheck.lean), and every headline is signature-locked via [formula in source] ( AuditContrac

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation

## Main Technical Development

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:194-265](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L194) · `section:78e2047342d611dee0bd` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

Explicit source references:

- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## Not Used Here

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:311-317](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L311) · `section:d5e642aea3b342ff60d3` · section

Exact [formula in source] numerics, CKM/PMNS closure, pole-mass ledgers, OS/CAR reconstruction, local Minkowski nets, scattering, gravity/metrology, cosmology, CMB targets, and E8 grammar are not used as proof inputs in this paper.

## Electromagnetic Closure

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:88-97](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L88) · `section:a4e228cda3e7be6c28d2` · section

The electromagnetic calculation is presented only after the carrier branch is fixed. The fixed point is read as a closed-branch output: [formula in source] The paper should include the carrier form of the electromagnetic closure and the compact audit of which structural quantities enter the fixed point.

## Flavor Transport

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:178-186](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L178) · `section:d2f0333f7f6f30e137b8` · section

The CKM and PMNS closure block belongs here, together with the transport grammar and regularized Yukawa kernels needed for the flavor statements. Representative hard readouts include [formula in source] Large mass tables belong in the companion or a later empirical ledger, not in this paper.

## No-Knobs Audit

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:187-202](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L187) · `section:b4f215eea1ac180c1adf` · section

@p0.18 p0.2 p0.18 p0.13 Y@ Constant & First appearance & Prior dependency & Before [formula in source] ? & Variation consequence \\ [formula in source] & Paper 2 carrier theorem & Paper 1 primitive kernel & Yes & Breaks [formula in source] , gauge quotient, and all downstream readouts. \\ [formula in source] & Paper 1 seam generator & Boundary primitive kernel & Yes & Breaks family counting and transport branch norma

## Alternative Discrete Worlds

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:203-209](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L203) · `section:6ca3fc0d9cf8ce339659` · section

The alternative discrete worlds table is a falsification device. It should not be presented as decorative numerics. Each alternative must fail because it breaks a prior branch constraint, the fixed-point equation, or the simultaneous reuse audit.

## Main Technical Development

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:210-215](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L210) · `section:bafb68a85151d35f3102` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

## Source Extraction Map

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:216-240](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L216) · `section:402bdac3fd09ce4bce51` · section

Use : Sections 4.1 and 4.2 for electromagnetic closure. Sections 5.4 and 5.5 for UV seed shadow, Cabibbo inversion, and alternative discrete worlds. Sections 7.1–7.3 for the discrete phase operator, transport grammar, and Yukawa kernels. Sections 7.16–7.27 for CKM and PMNS closure. Appendix A only as a narrow operational prediction surface and compact prediction ledger. Add a dedicated [formula in source] audit appen

## Not Used Here

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:241-250](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L241) · `section:ac01d6f66ff8854f6dae` · section

Strong-CP admissibility closure, OS/CAR reconstruction, local Minkowski nets, scattering, gravity/metrology proofs, CMB spectra, sky realization, E8 grammar, horizons, and large pole-mass tables are not used as proof inputs in this paper.

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

## Not Used Here

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:210-216](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L210) · `section:228132cd22c2701bbf15` · section

Exact electromagnetic benchmark derivations, CKM/PMNS prediction tables, gravity/metrology readouts, CMB spectra, sky realization, E8 grammar, full empirical ledgers, horizons, and transient channels are not used as proof inputs in this paper.

## Main Technical Development

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:190-210](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L190) · `section:70da2f72e0e0912c91df` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

## Not Used Here

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:235-240](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L235) · `section:3989d5bf2e359ffa6552` · section

Late-time [formula in source] , CMB spectra, sky realization, black holes, horizons, E8 stage atlas, transient channels, and cosmological comparison rows are not used as proof inputs in this paper.

## Cosmology as Downstream Interface

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:82-93](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L82) · `section:8ee73443cb760ceae12f` · section

The closed branch is fixed before cosmology enters: [formula in source] This section should make the nonprimitive status of cosmology explicit.

## Axion Interface

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:105-117](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L105) · `section:d0ca2a1debedf9301f14` · section

The axion sector is recorded as [formula in source] The axion interface belongs here because it depends on seam transfer and determinant-line phase, not on the primitive carrier proof.

## Reheating, Leptogenesis, and Neutrino Inputs

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:118-123](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L118) · `section:483b4d4658b6a3959f95` · section

Reheating and leptogenesis are stated as downstream inputs supplied by the closed branch. The paper should keep them status-coded and avoid turning the module into a hidden fit engine for later CMB targets.

## CMB Stage 1: Spectra

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:124-129](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L124) · `section:d460ccf69df0e08ddf6a` · section

Stage 1 is the spectral target: transfer functions, angular spectra, and comparison rows. This stage may define falsification targets and benchmark rows, but it does not claim a unique sky-map realization.

## Downstream Obligations Moved to the Companion

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:136-152](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L136) · `section:f0e60a47149e6eefb905` · section

@p0.28 Y@ Module & Status in this paper \\ Stationary horizons and compact objects & Listed only as downstream programmatic obligations; technical material is in the Companion. \\ Code subspace, pointer dynamics, and record algebra & Not part of the cosmology-interface proof surface. \\ Transient event channels & Falsification and prediction semantics belong to the Companion. \\ Pole masses, Higgs readout, and full f

## Main Technical Development

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:153-173](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L153) · `section:78dc731bfe3c36e77b3f` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

## Source Extraction Map

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:174-191](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L174) · `section:7f8cc17f94ae4b0fb41a` · section

Use : Section 10 for FRW reduction, seam transfer, and scalaron branch. Sections 10.1 and 10.2 for falsification matrix and proof-obligation ledger. Appendix C.7, Appendix G, and the cosmology-interface proof material in Appendix J. Appendix N only for the axion-interface excerpt. Keep CMB Stage 1 and Stage 2 visibly separate.

## Not Used Here

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:192-201](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L192) · `section:2ae423d020a51a6197c7` · section

Carrier proofs, the full [formula in source] derivation, QFT closure proofs, Standard-Model packet proofs, and metrology proofs are not reproved or used as adjustable inputs in this paper. They enter only as fixed outputs of the earlier closed branch.

## tfptblue CMB Operational Closure and the\\ Planck Comparison Pipeline\\[0.35em] From the TFPT 4.6 Native Closure to a HEALPix Sky Realization,\\ the Lemma A–E Conjectures, Seven TFPT Bridge Theorems,\\ and the v4.6.8 Measurement Bridge Contract\\ (Five Artefact Validation Groups closing the Final Status Flip)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/preamble.tex:1-44](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/preamble.tex#L1) · `section:a361b6ca86f19f4dd4d2` · frontmatter

basicstyle= , backgroundcolor= tfptcodebg, frame=single, framerule=0.4pt, rulecolor= tfptblue!40, breaklines=true, showstringspaces=false, columns=fullflexible, xleftmargin=4pt, xrightmargin=4pt, aboveskip=6pt, belowskip=6pt,

## Front matter / support

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/001-section-what-this-paper-does-and-does-not-do.tex:1-226](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/001-section-what-this-paper-does-and-does-not-do.tex#L1) · `section:6696018adf21f42f20da` · frontmatter

This paper documents the v4.6 incarnation of the CMB operational closure between the TFPT 4.6 closed branch and the Planck PR3 component maps, including the v4.6.4 audit upgrade. We move beyond the v4.5 ``calibrated'' pipeline into a fully-strict, audit-disciplined comparison where every entry of the cosmological parameter vector [formula in source] is labelled derived_tfpt_candidate_v46 and traced back to one of fiv

Explicit source references:

- [verification/v412_sheet_source_corner_J.py](../../../../verification/v412_sheet_source_corner_J.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v411: u/d ratio as a pure V-power readout *) num = one . MatrixPower[V, 4] . one; den = (a . V . one)(one . MatrixPower[V, 2] . one); checkExact["v411 FLAV.UD.VPOWER.01: c_u/c_d = (1.V^4.1)/((a.V.1)(1.V^2.1)) = 55/(9*13) = 55/117, identical to g_car*||Pl(K)||_1/(N_fam^2 Delta_Q) = 5*11/(9*13); RE-ENCODING, value stays [C]", num == 55 && a . V . one == 9 && one . MatrixPower[V, 2] . one == 13 && num/den == 55/117 && (5*11)/(9*13) == 55/117]; (* v412: the sheet source corner J = M(1,-2) on the Z2 wall *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2417)

## What this paper does and does not do

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/001-section-what-this-paper-does-and-does-not-do.tex:227-277](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/001-section-what-this-paper-does-and-does-not-do.tex#L227) · `section:8a58c509d92464215d11` · section

The downstream cosmology interface introduced in Paper 6 left two clean gaps for any honest CMB comparison: the seam-transfer determinant, the scalaron coefficient [formula in source] , and the leptogenesis Boltzmann were interfaces stated, not yet closed; Stage 2 — producing this sky — requires a boundary realisation operator [formula in source] whose existence was a programmatic target, not a theorem.

Explicit source references:

- [verification/v46_grand_mass_volume.py](../../../../verification/v46_grand_mass_volume.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *) checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+", Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16]; checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car", Sort[Abs[plLeft[K]]] == {1, 4, 6} && Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar]; checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car", 4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15]; (* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L168)

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

## Lemma E decomposition (E1–E5).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:138-195](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L138) · `section:0bf624212f6bc5ce352c` · paragraph

Stefan v4.6.3 review 6: Lemma E factors into five strictly weaker theorems, each carrying its own proof status. These are now formalised in tfpt_cmb.native_closure_v46.LEMMA_E_DECOMPOSITION and exposed by the Sprint-2A contract validator ( @p0.16 p0.36 Y@ ID & Statement & Status / hook \\ E1 Existence & [formula in source] is self-adjoint on [formula in source] with discrete bounded-below spectrum [formula in source]

## The TFPT primitives ledger and audit table

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:196-234](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L196) · `section:8301f1c88a5e5c8d3bef` · section

@lll@ Symbol & Formula / origin & Numeric value \\ [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & primitive seam winding class & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] rad \\ [formula in source] &

## Audit flag.

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:235-241](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L235) · `section:6977d5718ecda58e5e57` · paragraph

The two [formula in source] values disagree at the [formula in source] relative level. The pipeline records this as an unresolved audit_mismatch and refuses to advertise any [formula in source] -dependent prediction without resolving which side — the formula or the text — is correct.

## Operational closures, v4.6

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:294-326](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L294) · `section:62b0b4d5c1d2440898ea` · section

The twelve closures [formula in source] survive verbatim; their status upgrades from operational_closure_v1 (v4.5) to derived_tfpt_candidate_v46 (v4.6) wherever the lemma chain backs them.

## Comparison metrics and audit ledger

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:200-223](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L200) · `section:63de841c254efaf3181e` · section

@p0.27 p0.16 p0.16 Y@ Quantity & TFPT v4.6.3 & Planck & Comment \\ [formula in source] & 6\,546 & 6\,202 & 5.6\,\% high; tracks [formula in source] excess. \\ [formula in source] & 0.722 & 0.758 & SMICA anafast \\ [formula in source] proxy (RMS T) & 44.85 & 42.21 & 6\,\% high \\ Cold-spot min. ( [formula in source] )& [formula in source] & [formula in source] & 5\,\% \\ Cold-spot max. ( [formula in source] )& [formul

## The Sprint 2A Branch Extraction Contract

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:281-292](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L281) · `section:251779a935bf6cfe780c` · section

Stefan's v4.6.3 review converges on a single sharp statement: the code is no longer the bottleneck; the data side and the proof side are. The next sensible step is therefore neither another plot nor another module — it is a formal, executable Branch Extraction Contract that any future Sprint-2A run must satisfy. This section defines that contract and reports what the v4.6.3 candidate bundle scores against it.

## The candidate v4.6 bundle vs the contract

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:337-375](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L337) · `section:60bce3ca3086efbef633` · subsection

We dump the candidate v4.6 synthetic bundle and run it through the validator: The result is exactly the audit Stefan asked for: [formula in source] hard checks pass; the six that fail are the v4.6.3 audit gap and they are the gap by design:

Explicit source references:

- [verification/v46_grand_mass_volume.py](../../../../verification/v46_grand_mass_volume.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *) checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+", Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16]; checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car", Sort[Abs[plLeft[K]]] == {1, 4, 6} && Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar]; checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car", 4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15]; (* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L168)

## The v4.6.6 Proof Discharge Package

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:40-55](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L40) · `section:84e9714e24dfe155ac39` · section

Stefan's v4.6.5 review delivered an uncomfortable but accurate verdict: the proposed_solution fields of v4.6.5 were sketches, not discharges. v4.6.6 closes that gap. This section formalises the discharge of all 14 hooks: the full proof body, the boxed final form, the discharge taxonomy, the closure condition, and the new theorem (or data artifact) required to flip each hook to discharged.

## Discharge taxonomy

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:56-100](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L56) · `section:b983c04974ce44edef90` · subsection

Every hook is tagged with one of 12 status classes. The taxonomy distinguishes convention adoption (no theorem needed) from theorem proof (paper-side work) from data extraction (engineering work) from numerical verification. This is the sharpening Stefan demanded:

## Critical-path roadmap (7 steps)

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:101-133](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L101) · `section:6b4819f05f57f2198a67` · subsection

The seven steps are sequenced in tfpt_cmb.proof_discharge_v466.ROADMAP_V466. When all seven complete, every status flag in the pipeline flips from derived_tfpt_candidate_v46 to derived_tfpt without further code changes.

## The single acceptance gate

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:134-176](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L134) · `section:1d0c4c12c2eceefe20c8` · subsection

The pipeline's flip predicate is tfpt_cmb.proof_discharge_v466.can_flip_to_derived_tfpt. It accepts the status flip iff the dictionary of discharge outcomes matches the 14 entries of REQUIRED_DISCHARGE_OUTCOMES, which are:

## The v4.6.7 Final Closure Proposal: Seven Bridge Theorems

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex:177-187](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/004-subsection-what-a-passing-sprint-2a-run-looks-like.tex#L177) · `section:e5339d506f942a04e145` · section

Stefan's v4.6.6 review delivered the final acceptance test: theory-intern kann ich die verbleibenden Probleme schliessen, indem wir die fehlenden Brueckensaetze explizit als TFPT Theoreme formulieren und beweisen. v4.6.7 does this. Seven TFPT bridge theorems close all 14 hooks theory-internally; what remains is artefact validation, not theory.
