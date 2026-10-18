# Verification, formalization and safeguards — part 3

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Reproducibility

[documents/archive--paper-latex--tffpt-theory-fullv2/sections/006-section-verification-suite-summary.tex:297-323](../../../../documents/archive--paper-latex--tffpt-theory-fullv2/sections/006-section-verification-suite-summary.tex#L297) · `section:a63f4e3fa05e41a205c9` · section

Replication package: All numerical results can be reproduced using the TFPT verification suite (v5).

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)

## Identity Catalogue and Status Labels

[documents/archive--paper-latex--tffpt-theory-fullv2/sections/006-section-verification-suite-summary.tex:324-360](../../../../documents/archive--paper-latex--tffpt-theory-fullv2/sections/006-section-verification-suite-summary.tex#L324) · `section:5bfeab8ea48c043fde16` · section

This appendix labels frequently used equalities by logical status to prevent conflating definitions, algebraic rewrites, and genuine predictions.

## References

[documents/archive--paper-latex--tffpt-theory-fullv2/sections/006-section-verification-suite-summary.tex:361-394](../../../../documents/archive--paper-latex--tffpt-theory-fullv2/sections/006-section-verification-suite-summary.tex#L361) · `section:410a2075bf4ba040574d` · section

] F. W. Hehl, P. von der Heyde, G. D. Kerlick, J. M. Nester, ``General Relativity with Spin and Torsion: Foundations and Prospects,'' Rev.\ Mod.\ Phys.\ 48, 393 (1976).

## Reading guide and claim map

[documents/archive--paper-latex--tfpt-31/sections/001-section-reading-guide-and-claim-map.tex:60-165](../../../../documents/archive--paper-latex--tfpt-31/sections/001-section-reading-guide-and-claim-map.tex#L60) · `section:5ad6c8ac0fb46f8da1fd` · section

The paper is organized in three reading layers: Big picture: one section explains what TFPT claims in plain language before the detailed datum and conventions begin. Detail: the main body then runs from primitive core and hard carrier kernel through kernel numerics, the two closure-architecture sections, the closure theorem stack, the particle/mass compiler, and the benchmark interface. Proof sketches: the main text 

## Front matter / support

[documents/archive--paper-latex--tfpt-31/sections/009-partial-t-gamma-k.tex:1-84](../../../../documents/archive--paper-latex--tfpt-31/sections/009-partial-t-gamma-k.tex#L1) · `section:8adc551aa0304f4c3593` · frontmatter

Assume the projected RG flow preserves the admissible Bernstein cone and admits a nontrivial UV fixed point satisfying the pole and positivity audit below. The effective average action is sought in the form [formula in source] where the sector form factors are constrained by complete Bernstein functions [formula in source] The admissible RG flow is required to preserve both the retained sector and this cone: [formula

## Particle and mass compiler

[documents/archive--paper-latex--tfpt-31/sections/012-section-particle-and-mass-compiler.tex:137-392](../../../../documents/archive--paper-latex--tfpt-31/sections/012-section-particle-and-mass-compiler.tex#L137) · `section:3559395957442aff0f78` · section

This section is the phenomenological heart of the manuscript. It is not meant to flatten all rows into one uniform notion of prediction. Instead it makes the relation between derived theorem outputs and intrinsic observation rows explicit: a declared numerical preconditioner, a kernel-output map, and a mass ledger that separates internal theorem outputs from their observation-surface images. Accordingly this section 

## Mass-closure ledgers

[documents/archive--paper-latex--tfpt-31/sections/013-subsection-rg-map-for-compiler-outputs.tex:301-359](../../../../documents/archive--paper-latex--tfpt-31/sections/013-subsection-rg-map-for-compiler-outputs.tex#L301) · `section:8407b09fe7671164c341` · subsection

For the mass surface itself the main text now uses four row-level status classes: exact algebraic, conditional geometric or closure, matched intrinsic observation, and optional extrapolation. The present ledgers use the middle two classes: conditional closure rows for theorem-facing masses and matched intrinsic observation rows for selected branch comparisons.

## Primary benchmark map and prediction ledger

[documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex:87-163](../../../../documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex#L87) · `section:5fc4a6c3bc6151ad32ab` · section

The comparison values used in this section follow representative CODATA, PDG, NuFIT, Planck, and birefringence references codata2022,pdg2025,nufit2025,planck2018,minamiKomatsu2020,eskilt2023,sullivan2025. The snapshot policy is frozen at CODATA 2022 / NIST for [formula in source] , PDG 2025 for particle-mass and weak-mixing rows, NuFIT 2025 for neutrino-angle rows, and Planck 2018 for the baryon-fraction reconstructi

## Operational prediction set

[documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex:164-214](../../../../documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex#L164) · `section:1c2ea22a47f4f1325e00` · subsection

The six-row observation table is not the whole experimental surface of the manuscript. tab:operational-prediction-set collects the rows that are operationally testable on near- to medium-term timescales, while keeping their status, next test, kill criterion, and dependency structure explicit. The point is not to flatten them into one truth class. Rather, the Status column now uses only the manuscript's final output v

## Compact prediction ledger

[documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex:215-244](../../../../documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex#L215) · `section:60033edd5e16c177830a` · subsection

The main observation table shows only a narrow comparison surface. To keep the compiler structure visible, tab:prediction-ledger summarizes which output packages belong to which layer of the paper.

## Realism audit of the present compiler surface

[documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex:245-256](../../../../documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex#L245) · `section:262528400f2be9524405` · subsection

The present main-text surface is no longer intentionally mixed. Its rows now use the manuscript's four final classes: exact algebraic, conditional geometric or closure, matched intrinsic observation, and optional extrapolation. Carrier algebra and the exact [formula in source] row remain the sharpest numerically load-bearing entries, while the seed-driven observation rows remain useful because they are transparent an

## Falsification matrix

[documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex:307-333](../../../../documents/archive--paper-latex--tfpt-31/sections/014-section-downstream-cosmology-module-on-the-observation-c.tex#L307) · `section:59fd5df0b41c3690aa61` · subsection

The present draft does not ask the reader to accept one undifferentiated compiler claim. Each main-text closure statement has a corresponding local or global failure mode, and those failure modes should be readable without first decoding the appendix tables.

## Compiler theorem from the admissibility complex

[documents/archive--paper-latex--tfpt-31/sections/015-subsection-compiler-theorem-from-the-admissibility-compl.tex:1-28](../../../../documents/archive--paper-latex--tfpt-31/sections/015-subsection-compiler-theorem-from-the-admissibility-compl.tex#L1) · `section:5ba7c7bb2bf5294a1869` · subsection

Assume the admissible reduced datum summarized in tab:status-matrix, together with the closure theorems of sec:closure-theorems and the conditional closure selection theorem thm:observation-closure. Then every main-text observable in scope is classified by exactly one of the following status classes: exact algebraic, conditional geometric or closure, matched intrinsic observation, optional extrapolation.

## Optional extrapolations

[documents/archive--paper-latex--tfpt-31/sections/015-subsection-compiler-theorem-from-the-admissibility-compl.tex:109-116](../../../../documents/archive--paper-latex--tfpt-31/sections/015-subsection-compiler-theorem-from-the-admissibility-compl.tex#L109) · `section:7472bd8e84f98fd5f207` · subsection

Optional arithmetic continuations, appendix-level E [formula in source] scale grammar, and horizon semantics are kept as extrapolations and are not part of the theorem surface itself. They are retained only where they illuminate downstream interpretations without carrying any main-text proof burden.

## Symbol guide

[documents/archive--paper-latex--tfpt-31/sections/015-subsection-compiler-theorem-from-the-admissibility-compl.tex:209-271](../../../../documents/archive--paper-latex--tfpt-31/sections/015-subsection-compiler-theorem-from-the-admissibility-compl.tex#L209) · `section:00e22b5635c7e33903b6` · subsection

The main text uses a small number of recurrent symbols across different layers. The table below records their first-duty meaning and status class, now including the seam-matching notation introduced in Definition 9.1, so that the manuscript can be read without repeatedly reverse-engineering the bookkeeping.

## Yukawa kernels and positivity lemmas

[documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:1-34](../../../../documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L1) · `section:628e31c73eb3ec1b51e0` · section

This appendix is the proof motor for the transport positivity, strong-CP protection, and bounded-residual statements used in the main text. The transport program is based on the regularized kernel [formula in source] Three remarks are important. The regulator [formula in source] is not optional: without it the kernel becomes ill-defined exactly where the admissibility question is most delicate. Positivity of the kern

## Information-theoretic and cut-and-project readings

[documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:51-55](../../../../documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L51) · `section:51c3bcf6773dc582b5b1` · section

This appendix collects interpretive notes that help organize the algebraic structure of the carrier-first compiler. When an exact algebraic statement appears below, it refers back to a main-text proposition; the appendix itself does not upgrade any status label beyond the declared hard / closure / benchmark / conditional discipline.

## Global particle ledger and status surface

[documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:244-277](../../../../documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L244) · `section:731c46b99941af694896` · section

This appendix collects the full Standard Model output of the carrier-first compiler into two master tables. The purpose is not to flatten the truth-mode hierarchy but to give the reader a single-page capability audit: which particles, which quantities, which derivation, which status, which reference value, which residual. The status language is the same throughout the paper:

## Table A: Standard Model content and origin map

[documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:278-319](../../../../documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L278) · `section:fc02600046ead802d5e4` · subsection

@> p0.09 > p0.11 > p0.10 > p0.04 > p0.18 > p0.20 > p0.08 @ Particle & Repr. & Ext.\ source & [formula in source] & TFPT origin & Internal source & Status \\ 7@l Fermion sector (one family [formula in source] ): \\ [formula in source] & [formula in source] & [formula in source] & [formula in source] & carrier scaffold & hard carrier, [formula in source] & EA \\ [formula in source] & [formula in source] & [formula in s

## Table B: full mass and benchmark surface

[documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:320-378](../../../../documents/archive--paper-latex--tfpt-31/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L320) · `section:162b2943036b7a704049` · subsection

round-mode=none, group-minimum-digits=20 ! @llllrlrrl@ Quantity & Sector & TFPT formula or source & Obs.\ map & TFPT\ & Unit & Reference\ & Residual & Status \\ 9@l Exact algebraic surface: \\ [formula in source] & EM & exact [formula in source] closure & on-shell Thomson & 137.0359992 & — & 137.03599918 & [formula in source] & EA \\ [formula in source] & EM & unbroken [formula in source] & — & [formula in source] & 

## Extended benchmarks

[documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex:50-54](../../../../documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex#L50) · `section:e5207e7749a3a9f853c7` · section

This appendix turns the broader prediction surface into explicit experimental bookkeeping. The point is not to promote every row to main-text benchmark status, but to keep next test, kill criterion, and dependency structure visible wherever the theory already commits to a concrete target.

## Target and kill-test rows

[documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex:89-113](../../../../documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex#L89) · `section:66f008470993a457ffaa` · subsection

round-mode=none, group-minimum-digits=20 ! @> p0.22 > p0.24 > p0.12 > p0.38 @ Test row & TFPT target or prohibition & Status reading & Failure mode \\ Second light Higgs doublet & no additional seam-even\ doublet & kill\ & robust discovery would\ the bosonic-index route \\ Calibrated birefringence null & [formula in source] \ the minimal branch & kill\ & externally calibrated null\ with zero at the\ tolerance would r

## Supplementary mass-source rows

[documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex:139-182](../../../../documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex#L139) · `section:4170ca510337d8f11b99` · subsection

The compact main-text mass ledgers intentionally suppress explicit formula detail. The source rows collected here retain that information without forcing the main text to read like a mixed formula notebook.

## Extended compiler ledger

[documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex:183-234](../../../../documents/archive--paper-latex--tfpt-31/sections/018-subsection-strict-benchmark-surface.tex#L183) · `section:c5c52d149c66e7fb784e` · subsection

round-mode=none, group-minimum-digits=20 @> p0.15 > p0.33 > p0.15 Y@ Row & TFPT source or target & TFPT value & Status note \\ [formula in source] & exact unbroken [formula in source] direction & [formula in source] & exact structural row \\ [formula in source] & exact color gauge direction before confinement & [formula in source] & exact structural row \\ [formula in source] & intrinsic threshold output at [formula 

## Reading guide and claim map

[documents/archive--paper-latex--tfpt-32/sections/001-section-reading-guide-and-claim-map.tex:25-127](../../../../documents/archive--paper-latex--tfpt-32/sections/001-section-reading-guide-and-claim-map.tex#L25) · `section:44d833b825fd27c41145` · section

The paper is organized in three reading layers: Big picture: one section explains what TFPT claims in plain language before the detailed datum and conventions begin. Detail: the main body then runs from primitive core and hard carrier kernel through kernel numerics, the two closure-architecture sections, the closure theorem stack, the particle/mass compiler, and the benchmark interface. Proof sketches: the main text 

## Particle and mass compiler

[documents/archive--paper-latex--tfpt-32/sections/012-section-particle-and-mass-compiler.tex:75-359](../../../../documents/archive--paper-latex--tfpt-32/sections/012-section-particle-and-mass-compiler.tex#L75) · `section:d7d8ee8a23b4765be497` · section

This section is the phenomenological heart of the manuscript. It is not meant to flatten all rows into one uniform notion of prediction. Instead it makes the compiler interface explicit: a declared RG map, a kernel-output map, and a mass ledger that separates genuinely derived quantities from solver-level candidates and anchor-dependent comparison rows. Accordingly this section is best read through three ledgers: a p

## Mass-closure ledgers

[documents/archive--paper-latex--tfpt-32/sections/013-subsection-rg-map-for-compiler-outputs.tex:238-290](../../../../documents/archive--paper-latex--tfpt-32/sections/013-subsection-rg-map-for-compiler-outputs.tex#L238) · `section:5851dc3f4ef8418c302c` · subsection

For the mass surface itself the main text now uses only three row-level status words: derived, candidate, and anchor-dependent. The explicit candidate formulas, neutrino rows, and transport-ratio source data are moved to the appendix so that the main text shows a compact comparison-ready ledger rather than a mixed formula dump.

## Primary benchmark map and prediction ledger

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:1-58](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L1) · `section:27ed65835598bc44e479` · section

The comparison values used in this section follow representative CODATA, PDG, NuFIT, Planck, and birefringence references codata2022,pdg2025,nufit2025,planck2018,minamiKomatsu2020,eskilt2023,sullivan2025. The snapshot policy is frozen at CODATA 2022 / NIST for [formula in source] , PDG 2025 for particle-mass and weak-mixing rows, NuFIT 2025 for neutrino-angle rows, and Planck 2018 for the baryon-fraction reconstructi

## Operational prediction set

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:59-92](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L59) · `section:29c3d8eae3fa494798a0` · subsection

The six-row benchmark table is not the whole experimental surface of the manuscript. tab:operational-prediction-set collects the rows that are operationally testable on near- to medium-term timescales, while keeping their status, next test, kill criterion, and dependency structure explicit. The point is not to flatten them into one truth class. Rather, the Status column keeps the manuscript's global truth-mode vocabu

## Compact prediction ledger

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:93-119](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L93) · `section:aeefc7afb4631af9d16d` · subsection

The main benchmark table shows only a narrow comparison surface. To keep the compiler structure visible, tab:prediction-ledger summarizes which output packages belong to which layer of the paper.

## Realism audit of the present compiler surface

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:120-123](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L120) · `section:88d5f46d5372a2a592cb` · subsection

The present comparison surface is deliberately uneven, and that unevenness is informative rather than embarrassing. Carrier algebra and the self-consistent [formula in source] row are the sharpest parts of the manuscript. The seed-driven bridge rows are useful because they are transparent and mutually constrained, not because they are independent. In the mass sector, the manuscript should be read as a mixed surface: 

## Residual map and principal comparison refinements

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:124-169](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L124) · `section:8715967a753fdda95ef1` · subsection

The residuals for the restricted six-row table are shown in fig:residual-plot. The carrier-linked electromagnetic, birefringence, and baryon-density channels all remain within the displayed few-sigma window. The CKM phase is not plotted here because it is better treated, at present, in the operational prediction set and Appendix

## Falsification matrix

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:170-196](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L170) · `section:58cfad0a94b05014928f` · subsection

The present draft does not ask the reader to accept one undifferentiated compiler claim. Each main-text closure statement has a corresponding local or global failure mode, and those failure modes should be readable without first decoding the appendix tables.

## Compiler theorem and benchmark bridge

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:197-198](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L197) · `section:22ae61db89883f4a3ad5` · section

No opening prose excerpt; see the source.

## Compiler chain

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:199-219](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L199) · `section:e574c445789ea812b1e6` · subsection

Collecting the present primitive layer, the hard carrier kernel, the closure theorems from the admissibility complex, and the benchmark bridge, the compiler line is This line is not meant as a slogan. Each arrow is attached either to a hard theorem, to one of the closure theorems of sec:closure-theorems, or to the declared benchmark bridge.

## Compiler theorem from the admissibility complex

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:220-235](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L220) · `section:444e5f325f1c8d8ee37a` · subsection

Assume the primitive and hard layers summarized in tab:status-matrix, together with the closure theorems of sec:closure-theorems and the declared benchmark bridge [formula in source] . Then every main-text observable in scope is classified by exactly one of the following modes: a derived carrier or closure output, a retained branch value, an anchor-governed comparison image under [formula in source] , or a conditiona

## Closure stack and benchmark bridge

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:236-264](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L236) · `section:ce55b3b6aade404b2c50` · subsection

The compiler theorem above is only meaningful if the closure arrows are visibly attached to concrete input packages, output packages, and status labels. Otherwise the theorem reads like a slogan instead of a compressed map of the argument.

## Conclusion

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:265-272](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L265) · `section:36d3556b7069783f9f2c` · section

The present paper argues that a small carrier-first core already fixes nontrivial physics: the minimal [formula in source] carrier, the global Standard Model quotient, one chiral family packet, the carrier norm [formula in source] , the abelian index, the seam constant [formula in source] , the retained canonical seed [formula in source] , and the electromagnetic closure channel. The compression identities and exclus

## Scope and limitations

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:273-283](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L273) · `section:f5b7c77d5740c6e700e1` · subsection

The theorem stack proved here is narrower than a full theory-of-everything claim, and the manuscript should say so explicitly. The local spectral-scale / Einstein branch is a semiclassical induced-gravity construction; it is not a UV completion of quantum gravity. The axion block fixes a mass window and search interface, but not yet a full relic-density theorem including misalignment, string-wall production, and scal

## Release architecture

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:284-299](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L284) · `section:4e7e2bfd0553090e9b58` · subsection

The upgrade path is now organized as proof compression and axiom reduction rather than as first introduction of structures already present in v3.1: v3.2 tightens closure inputs: the admissibility selector is recast cohomologically, the residual APS/positivity/holonomy/coercivity block is compressed toward one master closure theorem, and the transport packets are upgraded from a retained admissible rule toward a vacuu

## Six theorem paths to generative closure

[documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex:300-332](../../../../documents/archive--paper-latex--tfpt-32/sections/014-section-primary-benchmark-map-and-prediction-ledger.tex#L300) · `section:1601d0f18313bfa38afc` · subsection

The cleanest route from the present carrier-first compiler to a genuinely generative architecture is not to blur status labels, but to isolate six explicit theorem paths: Master closure theorem: derive APS, Bernstein positivity, reflection positivity, [formula in source] holonomy, and Hamiltonian coercivity from canonical doubling, positive spectral measure, and total Hodge admissibility instead of keeping them as a 

## Internal closure candidates beyond the theorem stack

[documents/archive--paper-latex--tfpt-32/sections/015-subsection-internal-closure-candidates-beyond-the-theore.tex:1-114](../../../../documents/archive--paper-latex--tfpt-32/sections/015-subsection-internal-closure-candidates-beyond-the-theore.tex#L1) · `section:c656252313db4549894a` · subsection

The present manuscript now isolates the cleanest internal upgrade routes instead of leaving them as diffuse future work. They are status-disciplined candidate branches, not proved outputs of the current theorem stack.

## Symbol guide

[documents/archive--paper-latex--tfpt-32/sections/015-subsection-internal-closure-candidates-beyond-the-theore.tex:206-268](../../../../documents/archive--paper-latex--tfpt-32/sections/015-subsection-internal-closure-candidates-beyond-the-theore.tex#L206) · `section:55f91c2975311a7e1c96` · subsection

The main text uses a small number of recurrent symbols across different layers. The table below records their first-duty meaning and status class, now including the seam-matching notation introduced in Definition 9.1, so that the manuscript can be read without repeatedly reverse-engineering the bookkeeping.

## Yukawa kernels and positivity lemmas

[documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:1-34](../../../../documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L1) · `section:8e415d3107ebae026b73` · section

This appendix is the proof motor for the transport positivity, strong-CP protection, and bounded-residual statements used in the main text. The transport program is based on the regularized kernel [formula in source] Three remarks are important. The regulator [formula in source] is not optional: without it the kernel becomes ill-defined exactly where the admissibility question is most delicate. Positivity of the kern

## Information-theoretic and cut-and-project readings

[documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:35-39](../../../../documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L35) · `section:d6206fa4e8bae41f8d6a` · section

This appendix collects interpretive notes that help organize the algebraic structure of the carrier-first compiler. When an exact algebraic statement appears below, it refers back to a main-text proposition; the appendix itself does not upgrade any status label beyond the declared hard / closure / benchmark / conditional discipline.

## Extended benchmarks

[documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:228-232](../../../../documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L228) · `section:6d389648ce9df07257d1` · section

This appendix turns the broader prediction surface into explicit experimental bookkeeping. The point is not to promote every row to main-text benchmark status, but to keep next test, kill criterion, and dependency structure visible wherever the theory already commits to a concrete target.

## Target and kill-test rows

[documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:265-289](../../../../documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L265) · `section:a2206248773a028a8ad3` · subsection

round-mode=none, group-minimum-digits=20 ! @> p0.22 > p0.24 > p0.12 > p0.38 @ Test row & TFPT target or prohibition & Status reading & Failure mode \\ Second light Higgs doublet & no additional seam-even\ doublet & kill\ & robust discovery would\ the bosonic-index route \\ Calibrated birefringence null & [formula in source] \ the minimal branch & kill\ & externally calibrated null\ with zero at the\ tolerance would r

## Supplementary mass-source rows

[documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex:314-361](../../../../documents/archive--paper-latex--tfpt-32/sections/017-section-yukawa-kernels-and-positivity-lemmas.tex#L314) · `section:e0edaeab733523dfb2aa` · subsection

The compact main-text mass ledgers intentionally suppress explicit formula detail. The source rows collected here retain that information without forcing the main text to read like a mixed formula notebook.

## Extended compiler ledger

[documents/archive--paper-latex--tfpt-32/sections/018-subsection-extended-compiler-ledger.tex:1-50](../../../../documents/archive--paper-latex--tfpt-32/sections/018-subsection-extended-compiler-ledger.tex#L1) · `section:e0d221356499ee43bb88` · subsection

round-mode=none, group-minimum-digits=20 @> p0.15 > p0.33 > p0.15 Y@ Row & TFPT source or target & TFPT value & Status note \\ [formula in source] & exact unbroken [formula in source] direction & [formula in source] & exact structural row \\ [formula in source] & exact color gauge direction before confinement & [formula in source] & exact structural row \\ [formula in source] & boundary electroweak anchor at [formula

## Novelty boundary and literature positioning

[documents/archive--paper-latex--tfpt-32/sections/018-subsection-extended-compiler-ledger.tex:51-104](../../../../documents/archive--paper-latex--tfpt-32/sections/018-subsection-extended-compiler-ledger.tex#L51) · `section:9afa3d31cc1e046fb670` · subsection

The paper uses standard tools from relative spectral geometry, APS index theory, transport/resolvent language, and conventional RG comparison. The claim of novelty is not that these background ingredients are new in isolation, but that the minimal [formula in source] carrier packet, the compression identities, and the carrier-first compiler architecture are organized into one tightly overdetermined program. Conversel

## Version 4.5 completion surface

[documents/archive--paper-latex--tfpt-42/sections/001-section-reading-guide-and-claim-map.tex:234-382](../../../../documents/archive--paper-latex--tfpt-42/sections/001-section-reading-guide-and-claim-map.tex#L234) · `section:5edaa1f56c70e3528dfd` · subsection

The manuscript now contains a fully rigid algebraic core together with analytic closure blocks whose exact status is recorded theorem by theorem in the proof-obligation ledger. The remaining explicit standard-theorem interface is [formula in source] while the other former [formula in source] interfaces have now been pulled into the manuscript proof surface. The eight items below are therefore not a promise of later c

## Closure theorems from the admissibility complex

[documents/archive--paper-latex--tfpt-42/sections/022-section-closure-theorems-from-the-admissibility-complex.tex:1-397](../../../../documents/archive--paper-latex--tfpt-42/sections/022-section-closure-theorems-from-the-admissibility-complex.tex#L1) · `section:84843d6bca191a75f2d7` · section

The preceding two sections introduced the carrier-compatible geometric and transport architecture. The primitive admissibility projector [formula in source] was already placed in the primitive section so that the proof direction runs from the boundary datum through the derived closed datum to [formula in source] , and only then to the later sector theorems. What remains in this section is therefore (i) the upgrade of

## Falsification matrix

[documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex:1-61](../../../../documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex#L1) · `section:6e322457dcbc73dce9bf` · subsection

The present draft does not ask the reader to accept one undifferentiated output claim. Each main-text closure statement has a corresponding local or global failure mode, and those failure modes should be readable without first decoding the appendix tables.

## Proof-obligation ledger

[documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex:62-128](../../../../documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex#L62) · `section:aece9c239123e301af67` · subsection

To keep proof status, interface assumptions, and comparison-only layers visibly separated, we record the present audit path explicitly. We use five status classes: ] full proof in manuscript; ] full proof modulo an explicit standard theorem; ] proof sketch in main text with full proof deferred; ] readout or comparison only; ] programmatic closure target with a fixed mathematical statement but without a claimed proof 

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)

## Downstream closure modules from the closed branch

[documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex:129-149](../../../../documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex#L129) · `section:4e6820f6519ea6e01376` · section

The present section records the downstream closure modules that start from the already fixed branch object [formula in source] Nothing in this section changes the upstream theorem chain. The exact proof status of these downstream closures is recorded in the proof-obligation ledger, and each statement below is phrased only as far as it factors through already fixed branch data. The stationary geometric scale, boundary

## [P] Stationary horizons, modular thermality, and compact objects

[documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex:150-212](../../../../documents/archive--paper-latex--tfpt-42/sections/030-subsection-falsification-matrix.tex#L150) · `section:5752b502d049d3f4df75` · subsection

Assume the split property and stationarity of the exterior wedge algebra on the vacuum branch. Then for the outside algebra one has [formula in source] where [formula in source] is the horizon modular generator. Hence the reduced outside state is KMS and the horizon temperature is [formula in source]

## Canonical rigid object and falsification interface

[documents/archive--paper-latex--tfpt-42/sections/033-subsection-p-pole-masses-higgs-readout-and-full-flavor-o.tex:119-120](../../../../documents/archive--paper-latex--tfpt-42/sections/033-subsection-p-pole-masses-higgs-readout-and-full-flavor-o.tex#L119) · `section:0ec57280249ff4d51792` · section

No opening prose excerpt; see the source.

## Structural falsification map

[documents/archive--paper-latex--tfpt-42/sections/033-subsection-p-pole-masses-higgs-readout-and-full-flavor-o.tex:230-271](../../../../documents/archive--paper-latex--tfpt-42/sections/033-subsection-p-pole-masses-higgs-readout-and-full-flavor-o.tex#L230) · `section:e9771601a33e45b03c38` · subsection

The main text closes the theorem chain at [formula in source] and then attaches one structural side card, the falsification map [formula in source] This map reports which local or global structural failure mode would break each arrow of the reconstruction. It is hard-separated from the appendix-level empirical comparison map [formula in source] , which acts only after [formula in source] has been fixed and is collect

## Two side maps from [formula in source] T-star

[documents/archive--paper-latex--tfpt-42/sections/037-subsection-physical-readout-and-metrology-functor.tex:314-330](../../../../documents/archive--paper-latex--tfpt-42/sections/037-subsection-physical-readout-and-metrology-functor.tex#L314) · `section:4ceb90b0ad274be15e72` · subsection

From [formula in source] exactly two side maps are attached, both hard-separated from the theorem chain: Structural falsification map (main text). The map [formula in source] of sec:structural-falsification-map reports the structural failure mode that would break each arrow of the reconstruction. It uses no scheme conventions, no thresholds, and no comparison data. Empirical comparison map (appendix only). The map [f

## Conditional closure layer and status of the four downstream readouts

[documents/archive--paper-latex--tfpt-42/sections/037-subsection-physical-readout-and-metrology-functor.tex:331-397](../../../../documents/archive--paper-latex--tfpt-42/sections/037-subsection-physical-readout-and-metrology-functor.tex#L331) · `section:9096ea138c6033d1fe30` · subsection

The closed-branch theorem stack is supplemented by a single, explicitly labeled conditional closure layer, organized so that every numerical readout can be promoted to a theorem as soon as a single named lift hypothesis is discharged. The four downstream readouts and their current status are [formula in source] The compressed integrated story is [formula in source] and in the matter sector [formula in source] The fou

## Operational prediction set

[documents/archive--paper-latex--tfpt-42/sections/038-subsection-main-claim.tex:211-280](../../../../documents/archive--paper-latex--tfpt-42/sections/038-subsection-main-claim.tex#L211) · `section:6df85258fbb8746d44be` · subsection

The narrow empirical readout table is not the whole experimental surface of the manuscript. tab:operational-prediction-set collects the rows that are operationally testable on near- to medium-term timescales, while keeping their status, next test, kill criterion, and dependency structure explicit. The point is not to flatten them into one truth class. Rather, the Status column now uses only the manuscript's final out

## Compact prediction ledger

[documents/archive--paper-latex--tfpt-42/sections/038-subsection-main-claim.tex:309-340](../../../../documents/archive--paper-latex--tfpt-42/sections/038-subsection-main-claim.tex#L309) · `section:b9901fa20638c8059738` · subsection

The main empirical readout table shows only a narrow readout surface. To keep the output structure visible, tab:prediction-ledger summarizes which output packages belong to which layer of the paper.

## Admissible OS reconstruction and asymptotic scattering

[documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex:45-52](../../../../documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex#L45) · `section:bb2abd3fac8cbb0764ac` · section

This appendix upgrades the admissible Schwinger, reconstruction, and scattering block from a named standard interface to a manuscript-level proof package. The point is not to replace standard machinery by ad hoc notation, but to verify explicitly that the admissible branch satisfies the relevant hypotheses on [formula in source] .

## FRW reduction and cosmology interface proofs

[documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex:190-270](../../../../documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex#L190) · `section:1d252781b8a8cfc51971` · section

This appendix section upgrades the cosmology interface block from a proof sketch to a manuscript proof. The point is to keep the theorem-level content at the level of closed-branch interface data, while leaving late-time numerical continuation in the comparison layer.

## Yukawa kernels and positivity lemmas

[documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex:271-308](../../../../documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex#L271) · `section:dca1b7585c6b0caa6278` · section

This appendix is the proof motor for the transport positivity, determinant-phase suppression, and bounded-residual statements used in the main text. The transport program is based on the regularized kernel [formula in source] Three remarks are important. The regulator [formula in source] is not optional: without it the kernel becomes ill-defined exactly where the admissibility question is most delicate. Positivity of

## Information-theoretic and cut-and-project readings

[documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex:325-332](../../../../documents/archive--paper-latex--tfpt-42/sections/041-section-relative-aps-and-superconnection-setup.tex#L325) · `section:318adfb05d8570fc4b51` · section

This appendix collects interpretive notes that help organize the algebraic structure of the boundary-polarized closed form. When a theorem-level statement appears below, it refers back to a main-text proposition; the appendix itself does not upgrade any status label beyond the declared theorem / derived-consequence / comparison / appendix discipline.

## Prediction semantics and transient event channels

[documents/archive--paper-latex--tfpt-42/sections/042-subsection-seed-variance-and-surprisal-readings.tex:252-258](../../../../documents/archive--paper-latex--tfpt-42/sections/042-subsection-seed-variance-and-surprisal-readings.tex#L252) · `section:ada9ffd5266f47b5875e` · section

This appendix section collects the optional semantic decorations of the prediction map and the status note for transient event channels. These items organize downstream interpretation, but they do not add new upstream theorem arrows to the rigid core.

## Transient event status

[documents/archive--paper-latex--tfpt-42/sections/042-subsection-seed-variance-and-surprisal-readings.tex:273-278](../../../../documents/archive--paper-latex--tfpt-42/sections/042-subsection-seed-variance-and-surprisal-readings.tex#L273) · `section:d5f0606de0ade3b6d3de` · subsection

The topological burst channel of conj:topological_phase_slip_burst_channel is kept at programmatic-target status. What is fixed in the present version is only the admissible phase-slip channel and its scaling form, not yet a complete defect dynamics or radiative-transfer derivation.

## Table 1: Closed theoretical outputs

[documents/archive--paper-latex--tfpt-42/sections/042-subsection-seed-variance-and-surprisal-readings.tex:311-349](../../../../documents/archive--paper-latex--tfpt-42/sections/042-subsection-seed-variance-and-surprisal-readings.tex#L311) · `section:209e2228224b86417e5f` · subsection

@> p0.09 > p0.11 > p0.10 > p0.04 > p0.18 > p0.20 > p0.08 @ Particle & Repr. & Ext.\ source & [formula in source] & TFPT origin & Internal source & Status \\ 7@l Fermion sector (one family [formula in source] ): \\ [formula in source] & [formula in source] & [formula in source] & [formula in source] & carrier scaffold & hard carrier, [formula in source] & Theorem \\ [formula in source] & [formula in source] & [formula

## Table 2: Empirical comparison rows

[documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex:1-58](../../../../documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex#L1) · `section:c4896b30855616e301ff` · subsection

round-mode=none, group-minimum-digits=20 ! @lllllrlrrl@ Quantity & Sector & TFPT formula or source & Metrology\ & Comparison\ & TFPT\ & Unit & Reference\ & Residual & Status \\ 10@l Closed theoretical outputs: \\ [formula in source] & EM & exact [formula in source] closure & [formula in source] \ readout & on-shell Thomson & 137.0359992 & — & 137.03599918 & [formula in source] & Physical observable \\ [formula in sou

## Extended benchmarks

[documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex:108-112](../../../../documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex#L108) · `section:735e76d51ff15c2bcf88` · section

This appendix turns the broader prediction surface into explicit experimental bookkeeping. The point is not to promote every row to main-text benchmark status, but to keep next test, kill criterion, and dependency structure visible wherever the theory already commits to a concrete target.

## Target and kill-test rows

[documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex:147-171](../../../../documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex#L147) · `section:d832cd95a8269cc8eadf` · subsection

round-mode=none, group-minimum-digits=20 ! @> p0.22 > p0.24 > p0.12 > p0.38 @ Test row & TFPT target or prohibition & Status reading & Failure mode \\ Second light Higgs doublet & no additional seam-even\ doublet & kill\ & robust discovery would\ the bosonic-index route \\ Calibrated birefringence null & [formula in source] \ the minimal branch & kill\ & externally calibrated null\ with zero at the\ tolerance would r

## Supplementary UV asymptotic mass-source rows

[documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex:199-279](../../../../documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex#L199) · `section:fcc8754b4160c1961727` · subsection

The compact main-text mass ledgers intentionally suppress explicit formula detail. The source rows collected here retain that information without forcing the main text to read like a mixed formula notebook. In the present version they are explicitly UV asymptotic source rows: the physical masses belong to the pole-level functor [formula in source] on [formula in source] , whereas the formulas below record the closed-

## Extended comparison ledger

[documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex:280-332](../../../../documents/archive--paper-latex--tfpt-42/sections/043-subsection-table-2-empirical-comparison-rows.tex#L280) · `section:877c9d619d76859f1144` · subsection

round-mode=none, group-minimum-digits=20 @> p0.14 > p0.28 > p0.18 > p0.15 Y@ Row & TFPT source or target & Metrology\ & Scheme\ & Status note \\ [formula in source] & exact unbroken [formula in source] direction & [formula in source] \\m_ / _ =0 [formula in source] 0 [formula in source] m_g [formula in source] d_O=1 [formula in source] & [formula in source] & exact structural row \\ [formula in source] & threshold ou

## Summary of Claims and Status

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex:287-326](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L287) · `section:b26ca7abe6aad5e79152` · section

@p3cmp4cmp3cml@ Domain & Quantity & Deviation & Status\\ 4l Structural (parameter-free)\\ CFE & [formula in source] & [formula in source] ppm & green!60!black Closed-form consequence of defect sector reweighting on the orientable double cover\\ UFE & [formula in source] & 0.5–1.7 [formula in source] & green!60!black Solid\\ Cabibbo & [formula in source] & [formula in source] & green!60!black Solid\\ 4l RG-dressed\\ T

## Verification Suite Summary

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/006-section-numerical-constants-high-precision.tex:188-220](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/006-section-numerical-constants-high-precision.tex#L188) · `section:efccd6aa3ef98dcb26f3` · section

The TFPT verification suite (v5) runs 10 independent modules, with two additional modules planned for the [formula in source] effective action and bounce perturbations that complete the inflation/bounce closure:

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## E [formula in source] Chain Certificate

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/006-section-numerical-constants-high-precision.tex:221-227](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/006-section-numerical-constants-high-precision.tex#L221) · `section:ad71b3c13296b82d1d5e` · section

This appendix provides the complete verification data for the E [formula in source] chain uniqueness theorem (Theorem

## Verification Algorithm

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/006-section-numerical-constants-high-precision.tex:263-277](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/006-section-numerical-constants-high-precision.tex#L263) · `section:6158cbfedc1dac1b49e9` · subsection

The uniqueness is verified by: Constructing the complete Hasse diagram of [formula in source] from standard tables. Computing all cover relations with [formula in source] . Running dynamic programming to find all paths from [formula in source] to [formula in source] . Applying the cost function [formula in source] (second-difference smoothness). Verifying that the minimum-cost path is unique (cost gap to second-best 

## Status note

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:105-110](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L105) · `section:0dde3d2251dd28b73ba7` · subsection

The spin-lift argument fixes the [formula in source] deficit factor robustly, and the sector count is fixed by seam symmetry. The seam normalization is provided by the [formula in source] -gluing derivation in Appendix

## Reproducibility

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:176-204](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L176) · `section:397bfd1e9f74b6603a74` · section

Replication package: All numerical results can be reproduced using the TFPT verification suite (v5).

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## Identity Catalogue and Status Labels

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:205-241](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L205) · `section:f93e7dffcdac0bc7be6f` · section

This appendix labels frequently used equalities by logical status to prevent conflating definitions, algebraic rewrites, and genuine predictions.

## Bounce Perturbations and the Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:292-301](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L292) · `section:b20bca9c8966ce00aa28` · section

This appendix provides a minimal outline; the full numerical transfer-function evaluation is scheduled for the bounce_perturbations verification module.

## L.4 Falsification Targets

[documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:320-325](../../../../documents/archive--paper-latex--tfpt-theory-fullv21/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L320) · `section:5bf5d23f735cfedf0952` · subsection

Large-scale suppression or oscillatory features in [formula in source] are predicted at [formula in source] . Current CMB large-scale bounds constrain the allowable feature amplitude, providing a direct observational test of the bounce completion.

## Summary of Claims and Status

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex:286-337](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L286) · `section:e7ce89f8559459d93580` · section

@p3cmp4cmp3cml@ Domain & Quantity & Deviation & Status\\ 4l Structural (parameter-free)\\ CFE & [formula in source] & [formula in source] ppm & green!60!black Closed-form consequence of defect sector reweighting on the orientable double cover\\ UFE & [formula in source] & 0.5–1.7 [formula in source] & green!60!black Solid\\ Cabibbo & [formula in source] & [formula in source] & green!60!black Solid\\ 4l RG-dressed\\ T

## Verification Suite Summary

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:188-220](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L188) · `section:46bc02793ebae03e1be1` · section

The TFPT verification suite (v5) runs 10 independent modules, with two additional modules planned for the [formula in source] effective action and bounce perturbations that complete the inflation/bounce closure:

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## E [formula in source] Chain Certificate

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:221-227](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L221) · `section:12f7b1eca79b36522f76` · section

This appendix provides the complete verification data for the E [formula in source] chain uniqueness theorem (Theorem

## Verification Algorithm

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:263-277](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L263) · `section:cf9ca0eb32a78484f335` · subsection

The uniqueness is verified by: Constructing the complete Hasse diagram of [formula in source] from standard tables. Computing all cover relations with [formula in source] . Running dynamic programming to find all paths from [formula in source] to [formula in source] . Applying the cost function [formula in source] (second-difference smoothness). Verifying that the minimum-cost path is unique (cost gap to second-best 

## Status note

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:105-110](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L105) · `section:efa00888414c5cf3c810` · subsection

The spin-lift argument fixes the [formula in source] deficit factor robustly, and the sector count is fixed by seam symmetry. The seam normalization is provided by the [formula in source] -gluing derivation in Appendix

## Reproducibility

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:176-204](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L176) · `section:d4b96114fb81cbb3762c` · section

Replication package: All numerical results can be reproduced using the TFPT verification suite (v5).

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## Identity Catalogue and Status Labels

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:205-242](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L205) · `section:e26027f0eb812634d524` · section

This appendix labels frequently used equalities by logical status to prevent conflating definitions, algebraic rewrites, and genuine predictions.

## Bounce Perturbations and the Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:293-302](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L293) · `section:a290fd0ec6bd85dcedc4` · section

This appendix provides a minimal outline; the full numerical transfer-function evaluation is implemented in the bounce_perturbations verification module (see tfpt-suite/).

## L.4 Falsification Targets

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:321-326](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L321) · `section:1eda4bf85c73ba7564c7` · subsection

Large-scale suppression or oscillatory features in [formula in source] are predicted at [formula in source] . Current CMB large-scale bounds constrain the allowable feature amplitude, providing a direct observational test of the bounce completion.

## Summary of Claims and Status

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:338-400](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L338) · `section:e5db14aa16ca4e7f0e2b` · section

@p3cmp4cmp3cmp5.2cm@ TFPT status dashboard. ``Exact'': [formula in source] ; ``Solid'': [formula in source] ; ``Minor'': [formula in source] ; ``Moderate'': [formula in source] . Domain & Quantity & Deviation & Status\\ Domain & Quantity & Deviation & Status\\ 4r Continued on next page.\\ 4l Structural (parameter-free)\\ CFE & [formula in source] & [formula in source] & green!60!black Derived (double cover + [formula

## Verification Suite Summary

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:236-252](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L236) · `section:13891e8b420cf3f84576` · section

The TFPT verification suite ( tfpt-suite/) turns paper claims into deterministic, assumption-explicit computations. All counts in this section are auto-generated from the suite artifacts (no hardcoded ``39 modules''): [formula in source] It ships: a conventional suite (registry-driven; core invariants, [formula in source] closure + policy bridge, RG/matching, flavor pipelines, cosmology/bounce wiring, torsion/birefri

## Known Gaps and Status (Auto-Generated)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:253-282](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L253) · `section:b63b138d6fb15db8d399` · subsection

@llrrrrrr@ Module & Mode & Checks & PASS & WARN & FAIL & Plots(exp) & Plots(ok)\\ alpha_on_shell_bridge & engineering & 7 & 6 & 1 & 0 & 0 & 0\\ matching_finite_pieces & engineering & 5 & 4 & 1 & 0 & 0 & 0\\ torsion_condensate & engineering & 8 & 5 & 3 & 0 & 0 & 0\\ alpha_on_shell_bridge & physics & 7 & 6 & 1 & 0 & 0 & 0\\ matching_finite_pieces & physics & 5 & 4 & 1 & 0 & 0 & 0\\ torsion_condensate & physics & 8 & 5 

## E [formula in source] Chain CertificateE8 Chain Certificate

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex:152-158](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex#L152) · `section:22b3cbf63c265acaa292` · section

This appendix provides the complete verification data for the E [formula in source] chain uniqueness theorem (Theorem

## Verification Algorithm

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex:194-208](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex#L194) · `section:b8098ef60509670f5e29` · subsection

The uniqueness is verified by: Constructing the complete Hasse diagram of [formula in source] from standard tables. Computing all cover relations with [formula in source] . Running dynamic programming to find all paths from [formula in source] to [formula in source] . Applying the cost function [formula in source] (second-difference smoothness). Verifying that the minimum-cost path is unique (cost gap to second-best 

## Status note

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/009-subsection-spin-lifted-deficit-factor.tex:31-36](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/009-subsection-spin-lifted-deficit-factor.tex#L31) · `section:c59112b1841b2fb91435` · subsection

The spin-lift argument fixes the [formula in source] deficit factor robustly, and the sector count is fixed by seam symmetry. The seam normalization is provided by the [formula in source] -gluing derivation in Appendix

## Reproducibility

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/009-subsection-spin-lifted-deficit-factor.tex:102-130](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/009-subsection-spin-lifted-deficit-factor.tex#L102) · `section:e6cd0f748cfa56b27a56` · section

Replication package: All numerical results can be reproduced using the TFPT verification suite (v5).

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)

## Prediction Ledger and Falsification

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/009-subsection-spin-lifted-deficit-factor.tex:131-190](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/009-subsection-spin-lifted-deficit-factor.tex#L131) · `section:ae63c20b9d29f703f3fb` · section

Purpose: Provide a single, reviewer-friendly list of predictions and candidates that is tied to the same JSON sources used by the verification suite, to prevent number drift between Abstract, theorems, tables, and appendices.
