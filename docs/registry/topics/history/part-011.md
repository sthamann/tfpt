# Archives and dated records — part 11

[Topic entry](../history.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Summary of Claims and Status

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex:286-337](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L286) · `section:e7ce89f8559459d93580` · section

@p3cmp4cmp3cml@ Domain & Quantity & Deviation & Status\\ 4l Structural (parameter-free)\\ CFE & [formula in source] & [formula in source] ppm & green!60!black Closed-form consequence of defect sector reweighting on the orientable double cover\\ UFE & [formula in source] & 0.5–1.7 [formula in source] & green!60!black Solid\\ Cabibbo & [formula in source] & [formula in source] & green!60!black Solid\\ 4l RG-dressed\\ T

## What TFPT Does Not Assume

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex:338-351](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L338) · `section:70aceda6bf8a0d46ccc0` · section

The following are not required: Slow-roll inflation (specific model) String landscape or anthropic selection Extra dimensions as free parameters Dark matter entirely from axions New particles beyond minimal axion sector Any fitted or adjusted parameters

## Conclusions

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex:352-379](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/005-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L352) · `section:528adb89168a764dda21` · section

TFPT demonstrates that the fine-structure constant [formula in source] can be derived from first principles using eight minimal axioms rooted in topology, geometry, and quantum consistency. The key results are:

## Numerical Constants (High Precision)

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:1-33](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L1) · `section:43af2e360abc4637ddde` · section

@ll@ Quantity & Value\\ [formula in source] & 0.0397887357729738339\\ [formula in source] & 0.0530516476972984453\\ [formula in source] & 0.000120304479547082053\\ [formula in source] & 0.0531719521768455273\\ [formula in source] (self-consistent) & 0.053170209119023745\\ [formula in source] & 0.00423128951139541511\\ [formula in source] & [formula in source] \\ [formula in source] (E [formula in source] closure) & [

## Derivation of the CFE from the Effective Potential

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:34-187](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L34) · `section:67dec930ed4a0951926e` · section

In background-field gauge, the one-loop effective potential for the electromagnetic coupling modulus takes the form. Here [formula in source] is the induced potential for [formula in source] after rewriting [formula in source] :

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

## Orbit Data Structure

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:228-237](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L228) · `section:e606725d1ec3f9b3e024` · subsection

Each nilpotent orbit [formula in source] of [formula in source] is characterized by: Bala–Carter label: Standard notation (e.g., [formula in source] , [formula in source] , [formula in source] , ) Dimension: [formula in source] Centralizer dimension: [formula in source] Height: [formula in source] (sum of weighted Dynkin diagram coefficients)

## The Unique Chain (Excerpt)

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:238-262](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L238) · `section:79beb0a8831431946f23` · subsection

The complete chain from [formula in source] to [formula in source] :

## Verification Algorithm

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:263-277](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L263) · `section:cf9ca0eb32a78484f335` · subsection

The uniqueness is verified by: Constructing the complete Hasse diagram of [formula in source] from standard tables. Computing all cover relations with [formula in source] . Running dynamic programming to find all paths from [formula in source] to [formula in source] . Applying the cost function [formula in source] (second-difference smoothness). Verifying that the minimum-cost path is unique (cost gap to second-best 

## Boundary Trace Derivation

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:278-284](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L278) · `section:22830a3e703266cb5577` · section

This appendix derives the block index formula [formula in source] from the APS index theorem.

## Setup

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:285-294](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L285) · `section:054a586e4fa055d672b9` · subsection

Consider a 6D manifold [formula in source] with boundary [formula in source] . For a Weyl fermion coupled to a [formula in source] gauge field [formula in source] , the APS index theorem gives: where [formula in source] is the [formula in source] -invariant of the boundary Dirac operator.

## Flat Connection on Boundary Cycles

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:295-309](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L295) · `section:c29f788a57c716f9f7ea` · subsection

On the orientable double cover [formula in source] , the boundary decomposes as: (two boundary cycles plus the twist seam).

## Spectral Trace Coefficient and [formula in source]

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:310-319](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L310) · `section:1ceed334e6d11d4cf184` · subsection

The regulated determinant of the hypercharge-coupled Dirac operator contains a universal UV logarithmic term whose coefficient is the quadratic charge trace: Thus [formula in source] appears as a spectral index coefficient, independent of IR thresholds, matching its role in the CFE.

## Derivation of [formula in source]

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:320-339](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L320) · `section:6f156757227df61f2de9` · subsection

Step 1: Each boundary cycle contributes a factor proportional to [formula in source] .

## Seam Gluing and the [formula in source] -Invariant Normalization

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:340-345](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L340) · `section:28cbe89c6a53fdd895c3` · section

This appendix provides the [formula in source] -invariant gluing derivation used in Axiom

## Cut Space and Operators

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:346-356](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L346) · `section:f583b38405d13c1096bd` · subsection

Let [formula in source] be the orientable double cover of the M\"obius fiber and cut it along the seam [formula in source] to obtain a manifold-with-boundary [formula in source] with boundary components [formula in source] . Let [formula in source] be the Dirac operator on [formula in source] with APS boundary conditions on [formula in source] and a unitary matching operator [formula in source] identifying [formula i

## Gluing Formula for the [formula in source] -Invariant

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex:357-369](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/006-section-numerical-constants-high-precision.tex#L357) · `section:8f81c4f904ca1876ec00` · subsection

The APS gluing theorem expresses the [formula in source] -invariant of the glued manifold in terms of the cut manifold plus a discrete spectral-flow correction: where [formula in source] is the spectral flow of the matching operator. In TFPT bookkeeping this contributes a quantized seam term to the curvature normalization.

## M\"obius Matching and the Minimal Gluing Class

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:1-7](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L1) · `section:f939d71b3c301107fb9c` · subsection

For the M\"obius [formula in source] identification, the matching satisfies [formula in source] . The minimal nontrivial class is modeled by the unitary phase

## Spectral Flow Computation

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:8-24](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L8) · `section:c65208ce48869314e351` · subsection

Interpolate boundary conditions by a phase [formula in source] , which gives the eigenvalues As [formula in source] runs from [formula in source] to [formula in source] , exactly one eigenvalue crosses zero, so [formula in source] and [formula in source] .

## Normalization of [formula in source]

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:25-33](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L25) · `section:c5c21c85b6ba54188911` · subsection

The two physical boundary cycles contribute [formula in source] , and the seam gluing adds [formula in source] , so the total curvature is [formula in source] . The stationarity normalization [formula in source] therefore yields

## Derivation of the Coefficient 48 in [formula in source]

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:34-44](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L34) · `section:9f511f04bd16a07a60db` · section

This appendix explains the integer coefficient in [formula in source] . The key point is that the canonical quantity is and the appearance of ``48'' is simply the same number expressed in units of [formula in source] .

## The Physical Setup

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:45-57](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L45) · `section:ee42e0b09ec08b705f66` · subsection

The topological correction [formula in source] arises from the leading gauge-invariant correction to the tree-level geometric scale [formula in source] . The requirements are: Gauge invariance: The correction must be built from [formula in source] only (no explicit [formula in source] dependence at this order). Dimensionlessness: Since [formula in source] is dimensionless, the correction must be a pure power [formula

## Power Counting: Why [formula in source] ?

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:58-74](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L58) · `section:6bd51ab22c346df853c7` · subsection

The effective action on the M\"obius fiber includes the Chern–Simons term [formula in source] . The leading topological correction comes from the one-loop determinant of the Dirac operator coupled to this background.

## Spin-Lifted Deficit Factor

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:75-84](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L75) · `section:c25ffcc7bdddeb7a7632` · subsection

The non-orientable identification acts as a [formula in source] operation on the base, but in the spin bundle the same element lifts to order [formula in source] because a [formula in source] rotation acts as [formula in source] on spinors and only a [formula in source] rotation is trivial. This produces a universal deficit factor per minimal sector.

## Sector Count from Cut Geometry

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:85-94](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L85) · `section:6d5fda9a04c25d0d19d9` · subsection

Cutting along [formula in source] yields boundary components [formula in source] . The four local corner patches [formula in source] , [formula in source] , [formula in source] , [formula in source] constitute the fundamental domain. Summing the spin-lifted deficit factor over these sectors yields In TFPT normalization this yields the canonical form [formula in source] .

## Conversion to the [formula in source] normalization

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:95-104](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L95) · `section:5f3f235665bc53ce064f` · subsection

Using [formula in source] : so [formula in source] and [formula in source] are exactly equivalent.

## Status note

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:105-110](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L105) · `section:efa00888414c5cf3c810` · subsection

The spin-lift argument fixes the [formula in source] deficit factor robustly, and the sector count is fixed by seam symmetry. The seam normalization is provided by the [formula in source] -gluing derivation in Appendix

## Flavor Monodromy and Cross-Ratio

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:111-116](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L111) · `section:90ce82a5acc368eaa23f` · section

This appendix derives the M\"obius structure of flavor relations from boundary monodromy.

## Projective Invariance on Boundaries

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:117-134](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L117) · `section:f0d58b24c37619710e53` · subsection

On a conformally flat boundary, the metric is locally: Holomorphic automorphisms (Wilson lines of flat connections) act as M\"obius transformations:

## Cross-Ratio as Unique Invariant

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:135-145](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L135) · `section:51847e107bdbed2b614f` · subsection

Given four marked points [formula in source] on the boundary, the unique projective invariant is the cross-ratio:

## Cusp Selection

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:146-156](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L146) · `section:5b77dff132224f718261` · subsection

The cusps [formula in source] arise from: Rationality: Quantized holonomies [formula in source] rational cusps. GUT compatibility: SU(5) hypercharge assignments give [formula in source] (quarks), [formula in source] (leptons), etc. Uniqueness: These are the only rational values that simultaneously separate the three SM sectors (up, down, lepton) and maintain GUT normalization.

## Derivation of [formula in source]

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:157-175](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L157) · `section:45a90177e3d089ffc953` · subsection

Leading term: [formula in source] from the abelian trace (same as [formula in source] numerator divided by 41/10's denominator structure).

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

## One-Loop Effective Action in Riemann–Cartan and the [formula in source] Coefficient

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:243-256](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L243) · `section:fc36fc9abb91f849de4f` · section

K1: Field content and torsionful Lagrangian fixed by the minimal UFE sector. K2: Quadratic fluctuation operator is of Laplace type after background-field gauge fixing. K3: Heat-kernel coefficient [formula in source] captures the curvature-squared terms in [formula in source] . K4: Matching to [formula in source] after imposing the GR renormalization condition.

## K.1 Setup

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:257-262](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L257) · `section:1396be75dc128a9bbdf5` · subsection

We evaluate the one-loop effective action in a Riemann–Cartan background with torsion decomposed into axial [formula in source] , trace [formula in source] , and tensor [formula in source] . The minimal UFE choice treats torsion at quadratic order, so integrating out torsion is Gaussian and parameter-free once [formula in source] fixes the normalization of the coupling.

## K.2 Operator Form

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:263-271](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L263) · `section:f3a795c31b83c464ed83` · subsection

After background-field gauge fixing, the quadratic operator for torsion fluctuations can be written in Laplace type, with [formula in source] built from curvature and torsion invariants. The contribution to [formula in source] is [formula in source] .

## K.3 Heat-Kernel Coefficients

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:272-279](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L272) · `section:4c145ca6f7fa292d37bc` · subsection

The local part of [formula in source] is governed by the heat-kernel expansion where [formula in source] contains the curvature-squared terms. The torsion-dependent pieces combine into an effective [formula in source] operator in the low-energy action.

## K.4 Renormalization Condition

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:280-283](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L280) · `section:86bbbaa4c71290269707` · subsection

The GR limit (A8) fixes the renormalization scheme by requiring that the [formula in source] limit reduces to the Einstein–Hilbert action with coefficient [formula in source] .

## K.5 TFPT Closure

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:284-292](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L284) · `section:ee725d7e5bdc9cead9c6` · subsection

With the TFPT normalization of the torsion sector, the induced [formula in source] coefficient is fixed by [formula in source] , yielding which reproduces

## Bounce Perturbations and the Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:293-302](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L293) · `section:a290fd0ec6bd85dcedc4` · section

This appendix provides a minimal outline; the full numerical transfer-function evaluation is implemented in the bounce_perturbations verification module (see tfpt-suite/).

## L.1 Background Solution

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:303-307](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L303) · `section:0cb50095bbaaec5fdc61` · subsection

The bounce background is modeled by a smooth scale factor [formula in source] where the torsion-induced [formula in source] term regularizes [formula in source] for scalar perturbations. The transition to the [formula in source] inflationary phase is implemented by matching [formula in source] and its derivatives at [formula in source] .

## L.2 Numerical Integration Setup

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:308-312](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L308) · `section:e3133a6ec8297f5d0b32` · subsection

Mode functions are initialized in an adiabatic vacuum well before the bounce and integrated through the bounce and into the [formula in source] era. The numerical scheme records the transfer function by comparing late-time solutions to the pure [formula in source] baseline.

## L.3 Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:313-320](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L313) · `section:5b7f468e2e2c191679d0` · subsection

Define the transfer function as with [formula in source] for modes well inside the horizon during the bounce and deviations confined to [formula in source] .

## L.4 Falsification Targets

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:321-326](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L321) · `section:1eda4bf85c73ba7564c7` · subsection

Large-scale suppression or oscillatory features in [formula in source] are predicted at [formula in source] . Current CMB large-scale bounds constrain the allowable feature amplitude, providing a direct observational test of the bounce completion.

## References

[documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex:327-367](../../../../documents/archive--paper-latex--tfpt-theory-fullv24/sections/007-subsection-m-obius-matching-and-the-minimal-gluing-class.tex#L327) · `section:d109e3b022fb22886c7f` · section

] F. W. Hehl, P. von der Heyde, G. D. Kerlick, J. M. Nester, ``General Relativity with Spin and Torsion: Foundations and Prospects,'' Rev.\ Mod.\ Phys.\ 48, 393 (1976).

## Topological Fixed Point Theory (TFPT)\\[0.5em] A Parameter-Free Derivation of the Fine-Structure Constant\\ from Topology, Geometry, and Quantum Consistency

[documents/archive--paper-latex--tfpt-theory-fullv25/preamble.tex:1-591](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/preamble.tex#L1) · `section:5cb8442e876f729ca70b` · frontmatter

compat=1.18 groupplots arrows.meta,positioning,decorations.markings,decorations.pathmorphing,calc,patterns,shapes.geometric

## Front matter / support

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex:1-24](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex#L1) · `section:c539f356c8955bd431ce` · frontmatter

We present the complete axiomatic foundation of Topological Fixed Point Theory (TFPT), which derives the fine-structure constant [formula in source] and other fundamental quantities from eight minimal assumptions rooted in topology, geometry, and quantum field theory. The theory rests on two fundamental invariants: the topological coupling [formula in source] from 11D Chern–Simons quantization and the geometric scale

## Kernel and Discrete Grammar

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex:25-196](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex#L25) · `section:6b876a777857acc978fa` · section

Structural input (fixed, not fitted): the Standard Model abelian trace [formula in source] (determined by SM particle content and GUT normalization; not a TFPT knob).

## Introduction: The Problem of Parameters

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex:197-244](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex#L197) · `section:df2fe7929023aae9cd6e` · section

The Standard Model of particle physics contains approximately 19 free parameters that must be determined experimentally. Among these, the fine-structure constant [formula in source] stands out as a dimensionless number whose value has no explanation within conventional frameworks.

## Axiomatic Foundation

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex:245-252](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex#L245) · `section:23d49a2e7da2a44cea57` · section

TFPT is built on eight axioms, organized into three categories: geometric structure, quantum field theory, and closure conditions. Each axiom is either derived from established physics or explicitly marked as a new postulate.

## Geometric Axioms (A1–A4)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex:253-412](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/001-section-kernel-and-discrete-grammar.tex#L253) · `section:c4679245b235aacce773` · subsection

Riemann–Cartan GeometryRC The fundamental spacetime connection possesses torsion; the Levi-Civita connection is a limiting case when torsion vanishes.

## Quantum Field Theory Axioms (A5–A6)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex:1-80](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex#L1) · `section:8d4861c93ff0b0f1bb33` · subsection

Units and constants: Natural units: [formula in source] ; energies in GeV, lengths in GeV [formula in source] . Reference data: CODATA 2022, PDG 2024. Metric signature: [formula in source] . Levi-Civita tensor: [formula in source] , [formula in source] .

## Closure Axioms (A7–A8)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex:81-152](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex#L81) · `section:2db2f4cdd4072fb315de` · subsection

Standard Model Hypercharge TraceSMT The hypercharge trace invariant, summed over all SM fermions with GUT normalization [formula in source] , is: In TFPT this quantity appears as the spectral quadratic index of the hypercharge-coupled boundary operators in the regulated determinant (Appendix

## Derivation of Fundamental Constants

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex:153-156](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex#L153) · `section:fcde0f67dd1a7906af75` · section

No opening prose excerpt; see the source.

## The Geometric Scale [formula in source] The Geometric Scale phi0

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex:157-204](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex#L157) · `section:0abb91b38dc79e489a0a` · subsection

Existence and Uniqueness of [formula in source] phi0 From Axioms A3 and A4, the geometric scale is uniquely determined:

## The Cubic Fixed-Point Equation (CFE)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex:205-293](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex#L205) · `section:c898c04038f6bc36266d` · subsection

Effective Potential Parametersparams From the 11D Chern–Simons reduction (A5) and modulus-closure structure (A6): Notation: We use [formula in source] (calligraphic) for this CFE parameter to distinguish it from [formula in source] (gravitational coupling).

## Geometric Self-Consistency (Backreaction)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex:294-296](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex#L294) · `section:e84eee49d5cc8fa58d13` · subsection

No opening prose excerpt; see the source.

## Backreaction as Structural Response

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex:297-420](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/002-subsection-quantum-field-theory-axioms-a5-a6.tex#L297) · `section:dfe86a2a3a23348ef58c` · subsubsection

The response [formula in source] is the closed form consequence of defect sector reweighting on the orientable double cover. The linear form is the [formula in source] expansion, not a separate assumption.

## Sensitivity Analysis

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:1-46](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L1) · `section:45f7419ec4ad58b0714a` · subsubsection

The sub-ppm precision of the [formula in source] prediction depends critically on the backreaction coefficient. We analyze the sensitivity to demonstrate this is not fine-tuning but a genuine geometric constraint.

## Comparison and Scheme Policy (No Hidden Knobs)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:47-71](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L47) · `section:bad424bbba9a98e6de60` · subsection

(MS [formula in source] ), fonttitle= ] Why this matters: Precision electroweak fits and PDG summaries use the MS [formula in source] coupling at [formula in source] , [formula in source] , as the comparison observable. CODATA [formula in source] is an on-shell/IR reference and is therefore treated as secondary diagnostic once scheme and threshold bookkeeping is made explicit.

## The Unified Field Equation (UFE)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:72-75](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L72) · `section:6d2ff0f5077567a812a6` · section

No opening prose excerpt; see the source.

## Torsionful Geometric Action

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:76-172](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L76) · `section:e8c3b33dff6dcab8cdb3` · subsection

UFE ActionUFEaction On a manifold [formula in source] with metric [formula in source] and torsionful connection [formula in source] , the action is: Here [formula in source] denotes the Ricci scalar constructed from the full torsionful connection [formula in source] .

## Present-Day Torsion Regimes and Local Tests

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:173-243](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L173) · `section:414e5b9306da2bd98822` · subsection

TFPT distinguishes between cosmological torsion (which may be active in the early universe and drive a bounce) and local vacuum torsion (which is constrained by laboratory and astrophysical bounds on Lorentz violation). To avoid hidden assumptions, we treat ``torsion today'' as an explicit regime choice rather than a vague qualitative statement.

## Gravitational Coupling from Invariants

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:244-278](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L244) · `section:e18090b50a6280647d60` · subsection

Gravitational Coupling Consistencykappa The gravitational coupling [formula in source] (with dimension [formula in source] ) is constrained by consistency with the dimensionless ratio:

## Observable Predictions

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:279-282](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L279) · `section:d7a23827a2ab625aa107` · section

No opening prose excerpt; see the source.

## Axion–Photon Coupling

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:283-294](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L283) · `section:bb00edbbeb9d44dca77d` · subsection

Axion–Photon Couplinggagg The CFE fixes the axion–photon vertex uniquely: This determines cosmic birefringence without free parameters.

## Cosmic Birefringence

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex:295-321](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/003-subsubsection-sensitivity-analysis.tex#L295) · `section:ad1bd2d43ab8364cc0ad` · subsection

Topological Excursion Quantizationtopoexcursion The topological axion excursion is quantized in discrete sector changes: with [formula in source] the minimal nontrivial class. The corresponding birefringence is [formula in source] .

## Dynamical Completion of the Excursion

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex:1-112](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex#L1) · `section:81788e961f9a34bcdc7b` · subsubsection

Goal: Provide one minimal dynamical realization compatible with the topological quantization (Definition

## Two-Loop RG Fingerprints

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex:113-165](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex#L113) · `section:3bba4d004ae20c0e4581` · subsection

RG FingerprintsRGfingerprints The TFPT invariants leave signatures in the RG flow of gauge couplings: These values are obtained by two-loop RG running from PDG boundary conditions at [formula in source] using the declared PyR@TE model (checked by two_loop_rg_fingerprints in tfpt-suite/; not direct measurements at the quoted scales). The crossing scale for [formula in source] is [formula in source] GeV.

## The E [formula in source] Cascade and Block ConstantsThe E8 Cascade and Block Constants

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex:166-170](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex#L166) · `section:b9f571561e9c0abf7434` · section

No opening prose excerpt; see the source.

## Nilpotent Orbit Structure

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex:171-219](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex#L171) · `section:0400b64df246225b9453` · subsection

E [formula in source] Orbit Graphorbitgraph Let [formula in source] denote the set of nilpotent orbits of the exceptional Lie algebra [formula in source] . For each orbit [formula in source] , define: [formula in source] : the dimension of the orbit as a variety [formula in source] : the ``centralizer dimension'' [formula in source] : the height (sum of coefficients in weighted Dynkin diagram) The orbit graph [formul

## Log-Exact Ladder Formula

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex:220-325](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/004-subsubsection-dynamical-completion-of-the-excursion.tex#L220) · `section:722c044a4fabd4da41fb` · subsection

Holonomy degeneracy anchor for [formula in source] holonomydeg TFPT uses the SU(5) hypercharge holonomy data already fixed elsewhere in the construction. On the fundamental splitting, the holonomy spectrum separates into two eigenspaces of dimensions [formula in source] and [formula in source] , hence we define the discrete degeneracy count [formula in source] The minimal damping ratio compatible with a single additi

## Block Constant Formula and Derivation

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex:1-111](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex#L1) · `section:237f2533caab801d4b14` · subsection

For a 6D Weyl fermion zero mode on a boundary cycle [formula in source] with flat [formula in source] connection (holonomy [formula in source] ), the variation of [formula in source] under the connection is proportional to the quadratic charge index: The proportionality constant is fixed by the topological normalization [formula in source] .

## Neutrino Seesaw Predictions

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex:112-144](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex#L112) · `section:7c27ebea695743da0656` · subsection

The neutrino block at [formula in source] provides concrete predictions for the seesaw mechanism.

## Flavor Structure: The Z [formula in source] ArchitectureFlavor Structure: The Z3 Architecture

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex:145-148](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex#L145) · `section:a76f40cc33b28df4cdc3` · section

No opening prose excerpt; see the source.

## Universal Phase [formula in source] Universal Phase delta

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex:149-200](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex#L149) · `section:f3a1ffb884610a2574c6` · subsection

On a conformally flat boundary geometry, the unique projectively invariant quantity from four marked points is the cross-ratio. Any boundary monodromy acts as a PSL [formula in source] transformation. Therefore, relations depending only on boundary monodromies must be rational functions of a M\"obius map.

## M\"obius Mass Relations

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex:201-232](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex#L201) · `section:916878d34aeff2263855` · subsection

Mass Ratios from M\"obius Mapmassratios The M\"obius map [formula in source] evaluated at cusps [formula in source] yields mass ratios:

## Cabibbo Angle

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex:233-319](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex#L233) · `section:1b71820a1c7adc0f4931` · subsection

Cabibbo AngleCabibbo The Cabibbo angle is fixed parameter-free by [formula in source] : PDG reference: [formula in source] . Deviation: [formula in source] .

## Suite benchmark: RG-dressed CKM pipeline (explicit conventions)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex:320-342](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/005-subsection-block-constant-formula-and-derivation.tex#L320) · `section:dab6dce1b7061f48ba0c` · subsubsection

The shipped suite includes a deterministic CKM reconstruction pipeline with declared UV textures, two-loop RG dressing, and a reference-scale comparison at [formula in source] (module ckm_full_pipeline). The baseline benchmark gives a CKM matrix close to PDG at the level quantified by the reported [formula in source] .

## PMNS Neutrino Mixing: TM1 Pattern

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:1-58](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L1) · `section:e5d979c0fbaa38a0bbe4` · subsection

TFPT provides a closed prediction for [formula in source] via a single kernel identity plus the TM1 pattern. The remaining PMNS degrees of freedom [formula in source] are treated as an open interface requiring explicit Z [formula in source] -breaking and (eventually) correlated Yukawa/RG treatment; they must not be read as closed predictions at this stage.

## Inflation: [formula in source] Completion (Starobinsky Limit)Inflation: R2 Completion (Starobinsky Limit)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:59-99](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L59) · `section:0de55ed5a55d69bf3169` · section

The TFPT topological correction scale is set by [formula in source] (cf.\ [formula in source] ). In effective gravity, the leading higher-curvature completion compatible with general covariance is an [formula in source] term.

## [formula in source] Term from the Torsionful Effective ActionR2 Term from the Torsionful Effective Action

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:100-124](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L100) · `section:5e4c2c8a59455cb3b5bc` · subsection

Relevant Torsion DegreesR2torsion Decompose torsion into irreducible parts [formula in source] (axial, trace, tensor). In the minimal UFE setting the dominant coupling is through axial torsion [formula in source] , and the torsion sector is treated at quadratic order so it can be integrated out in the one-loop effective action.

## Coefficient Identification and GR Renormalization

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:125-144](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L125) · `section:33aaa77e94d07bc11538` · subsection

TFPT [formula in source] ScaleR2coeff Using the GR renormalization condition (A8) to fix the scheme, the coefficient of the [formula in source] term yields Here the square root applies only to [formula in source] , consistent with the numerical value above.

## Bounce + [formula in source] Perturbations and Transfer FunctionBounce + R2 Perturbations and Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:145-177](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L145) · `section:b7dbb22d61dd0c553106` · subsection

Bounce-to-Inflation Backgroundbouncebg Assume a non-singular bounce driven by the torsion-induced [formula in source] term (Lemma above), followed by a transition into the [formula in source] inflationary phase. We take the CMB pivot scales to exit the horizon during the [formula in source] phase.

## Axion Cosmology and Dark Matter

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:178-181](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L178) · `section:9c3dc73acc8c09501e08` · section

No opening prose excerpt; see the source.

## Two-Field Structure: Topological vs.\ QCD Axion

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:182-220](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L182) · `section:c1569d6e8c4ccf9c52ae` · subsection

The TFPT axion sector is split into two distinct fields to avoid an internal contradiction (a single [formula in source] eV axion cannot remain quasi-static over Hubble times):

## Dark Matter Relic Density

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:221-271](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L221) · `section:b3308ecc8e6d63796873` · subsection

Axion Dark Matter ParametersaxionDM For the QCD axion field [formula in source] from the E [formula in source] cascade (PQ block at [formula in source] ):

## Dark Energy as a Defect-Suppressed Torsion Condensate (candidate)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:272-306](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L272) · `section:a2276a7072f25a857362` · subsection

with no continuous knobs, fonttitle= ] We test the discrete defect-suppression candidate [formula in source] The two-defect sector uses [formula in source] and the corresponding [formula in source] (Sec.

## [formula in source] -Centric Identity Summarybeta_rad-Centric Identity Summary

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:307-337](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L307) · `section:dbe204242972dddce491` · section

The parameter [formula in source] provides a compact dictionary for expressing multiple quantities. Most equalities in this section are algebraic rewrites of earlier definitions rather than independent new inputs (see Appendix Inflation observables additionally depend on a dynamical completion (here: the conditional [formula in source] sector in Theorem

## Summary of Claims and Status

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex:338-400](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/006-subsection-pmns-neutrino-mixing-tm1-pattern.tex#L338) · `section:e5db14aa16ca4e7f0e2b` · section

@p3cmp4cmp3cmp5.2cm@ TFPT status dashboard. ``Exact'': [formula in source] ; ``Solid'': [formula in source] ; ``Minor'': [formula in source] ; ``Moderate'': [formula in source] . Domain & Quantity & Deviation & Status\\ Domain & Quantity & Deviation & Status\\ 4r Continued on next page.\\ 4l Structural (parameter-free)\\ CFE & [formula in source] & [formula in source] & green!60!black Derived (double cover + [formula

## What TFPT Does Not Assume

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:1-14](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L1) · `section:c309179e21930c428fb5` · section

The following are not required: Slow-roll inflation (specific model) String landscape or anthropic selection Extra dimensions as free parameters Dark matter entirely from axions New particles beyond minimal axion sector Any fitted or adjusted parameters

## Conclusions

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:15-42](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L15) · `section:de77ecba6ba9c40a0b31` · section

TFPT demonstrates that the fine-structure constant [formula in source] can be derived from first principles using eight minimal axioms rooted in topology, geometry, and quantum consistency. The key results are:

## Numerical Constants (High Precision)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:43-81](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L43) · `section:b8149cc5edc87b2bacad` · section

@ll@ Quantity & Value\\ [formula in source] & \\ [formula in source] & \\ [formula in source] & \\ [formula in source] & \\ [formula in source] (self-consistent) & 0.053170209119023745\\ [formula in source] & \\ [formula in source] & [formula in source] \\ [formula in source] & \\ [formula in source] (E [formula in source] ) & [formula in source] \\ [formula in source] (E [formula in source] exponent) & 0.58723319078

## Derivation of the CFE from the Effective Potential

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:82-235](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L82) · `section:9e986ea812c04ac4216f` · section

In background-field gauge, the one-loop effective potential for the electromagnetic coupling modulus takes the form. Here [formula in source] is the induced potential for [formula in source] after rewriting [formula in source] :

## Verification Suite Summary

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:236-252](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L236) · `section:13891e8b420cf3f84576` · section

The TFPT verification suite ( tfpt-suite/) turns paper claims into deterministic, assumption-explicit computations. All counts in this section are auto-generated from the suite artifacts (no hardcoded ``39 modules''): [formula in source] It ships: a conventional suite (registry-driven; core invariants, [formula in source] closure + policy bridge, RG/matching, flavor pipelines, cosmology/bounce wiring, torsion/birefri

## Known Gaps and Status (Auto-Generated)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex:253-282](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/007-section-what-tfpt-does-emph-not-assume.tex#L253) · `section:b63b138d6fb15db8d399` · subsection

@llrrrrrr@ Module & Mode & Checks & PASS & WARN & FAIL & Plots(exp) & Plots(ok)\\ alpha_on_shell_bridge & engineering & 7 & 6 & 1 & 0 & 0 & 0\\ matching_finite_pieces & engineering & 5 & 4 & 1 & 0 & 0 & 0\\ torsion_condensate & engineering & 8 & 5 & 3 & 0 & 0 & 0\\ alpha_on_shell_bridge & physics & 7 & 6 & 1 & 0 & 0 & 0\\ matching_finite_pieces & physics & 5 & 4 & 1 & 0 & 0 & 0\\ torsion_condensate & physics & 8 & 5 

## theoryv3 Evidence Layer (Compressed, Auto-Generated)

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex:1-151](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex#L1) · `section:8b3aa891da48a1a2c113` · subsection

The theoryv3 analysis branch is a compact ``evidence layer'' for the discrete kernel and crosslink logic. Current inventory (auto-generated from tfpt-suite/2.5/theoryv3/out/): [formula in source]

## E [formula in source] Chain CertificateE8 Chain Certificate

[documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex:152-158](../../../../documents/archive--paper-latex--tfpt-theory-fullv25/sections/008-subsection-theoryv3-evidence-layer-compressed-auto-gener.tex#L152) · `section:22b3cbf63c265acaa292` · section

This appendix provides the complete verification data for the E [formula in source] chain uniqueness theorem (Theorem
