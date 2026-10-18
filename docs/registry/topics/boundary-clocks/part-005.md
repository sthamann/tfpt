# Boundary, seam and clocks — part 5

[Topic entry](../boundary-clocks.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Cross-Ratio as Unique Invariant

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex:251-261](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex#L251) · `section:6cce62effca78e3a7bd0` · subsection

Given four marked points [formula in source] on the boundary, the unique projective invariant is the cross-ratio:

## Cusp Selection

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex:262-272](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex#L262) · `section:6b338033097b5768f02b` · subsection

The cusps [formula in source] arise from: Rationality: Quantized holonomies [formula in source] rational cusps. GUT compatibility: SU(5) hypercharge assignments give [formula in source] (quarks), [formula in source] (leptons), etc. Uniqueness: These are the only rational values that simultaneously separate the three SM sectors (up, down, lepton) and maintain GUT normalization.

## Derivation of [formula in source] Derivation of delta_star

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex:273-291](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/013-section-texorpdfstring-seam-gluing-and-the-eta-invariant.tex#L273) · `section:477f17713cf3dadb90ec` · subsection

Leading term: [formula in source] from the abelian trace (same as [formula in source] numerator divided by 41/10's denominator structure).

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

## L.3 Transfer Function

[documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex:183-190](../../../../documents/archive--paper-latex--tfpt-theory-fullv28/sections/014-section-prediction-ledger-and-falsification.tex#L183) · `section:7a501231de6e8858e342` · subsection

Define the transfer function as with [formula in source] for modes well inside the horizon during the bounce and deviations confined to [formula in source] .

## Front matter / support

[documents/archive--paper-latex--tfpt-v29/sections/001-section-overview-and-claim-map.tex:1-51](../../../../documents/archive--paper-latex--tfpt-v29/sections/001-section-overview-and-claim-map.tex#L1) · `section:c1b312c4d39cc26db2e1` · frontmatter

This document rewrites TFPT v2.8 into a carrier-first primary form. The rigid core is the Minimal Carrier Theorem: admissibility on the orientable double cover together with the seam involution forces the minimal carrier [formula in source] . From this rigid package follow the global Standard Model group [formula in source] , one chiral family [formula in source] , the carrier norm [formula in source] , and the linea

## Admissibility and Seam Data

[documents/archive--paper-latex--tfpt-v29/sections/001-section-overview-and-claim-map.tex:93-100](../../../../documents/archive--paper-latex--tfpt-v29/sections/001-section-overview-and-claim-map.tex#L93) · `section:047654eb4505008d0a4a` · section

The ambient v2.9 datum may be packaged as [formula in source] but the hard carrier core uses only [formula in source] . The field [formula in source] belongs to the absolute-scale and gravity channels discussed later in Section 8.

## Seam data recalled from v2.8

[documents/archive--paper-latex--tfpt-v29/sections/001-section-overview-and-claim-map.tex:101-121](../../../../documents/archive--paper-latex--tfpt-v29/sections/001-section-overview-and-claim-map.tex#L101) · `section:2e1e43eb36c1351d7bda` · subsection

The seam information needed by the carrier rewrite is already present in v2.8. In the minimal gluing class one has [formula in source] On the orientable double cover the distinguished cycles are [formula in source] where [formula in source] is the seam cycle in the glued description and corresponds to [formula in source] in the cut description. These data should appear near the front of the paper because Sections 3–6

## Boundary Multiplicity and Admissible Occupancy

[documents/archive--paper-latex--tfpt-v29/sections/002-subsection-general-abelian-index.tex:36-37](../../../../documents/archive--paper-latex--tfpt-v29/sections/002-subsection-general-abelian-index.tex#L36) · `section:93be441f9b64c1ccd1a3` · section

No opening prose excerpt; see the source.

## Seam descent normalization of [formula in source] c3

[documents/archive--paper-latex--tfpt-v29/sections/002-subsection-general-abelian-index.tex:91-119](../../../../documents/archive--paper-latex--tfpt-v29/sections/002-subsection-general-abelian-index.tex#L91) · `section:15709279023bc2823359` · subsection

The normalization of [formula in source] is best presented in two stages.

## Higgs as a conditional seam-even mode in [formula in source] E2

[documents/archive--paper-latex--tfpt-v29/sections/002-subsection-general-abelian-index.tex:346-355](../../../../documents/archive--paper-latex--tfpt-v29/sections/002-subsection-general-abelian-index.tex#L346) · `section:c61435255ddd3d0d5d0e` · subsection

If a light seam-even bosonic zero mode exists in [formula in source] , then the minimal carrier provides a natural Higgs candidate [formula in source] This is the correct representation-theoretic slot for a Standard Model Higgs doublet. The existence of the light mode itself remains part of the dynamical completion and should not be overstated as a theorem of the hard carrier core.

## Family-Index Bridge

[documents/archive--paper-latex--tfpt-v29/sections/003-subsection-flavor-and-the-phase-grammar.tex:71-86](../../../../documents/archive--paper-latex--tfpt-v29/sections/003-subsection-flavor-and-the-phase-grammar.tex#L71) · `section:d1515011efa17ff45bd0` · section

The v2.8 block relation [formula in source] already shows that family multiplicity is tied to the three distinguished cycles of the orientable double cover. Writing [formula in source] makes the same factorization explicit and immediately yields [formula in source] The equal-one assignment is the minimal symmetric branch and is the natural source of [formula in source] .

## Seam Descent Normalization

[documents/archive--paper-latex--tfpt-v29/sections/003-subsection-flavor-and-the-phase-grammar.tex:102-110](../../../../documents/archive--paper-latex--tfpt-v29/sections/003-subsection-flavor-and-the-phase-grammar.tex#L102) · `section:7e569e1df9ad6a0aa85c` · section

The seam descent logic is intentionally separated into two pieces: the spin-lifted seam loop closes only after [formula in source] , so [formula in source] and [formula in source] ; if the admissible carrier modulus is identified with the axionic angle variable, then [formula in source] and therefore [formula in source] . The first step is geometric. The second is the explicit carrier-to-axion identification.

## Numerical Branch Table

[documents/archive--paper-latex--tfpt-v29/sections/003-subsection-flavor-and-the-phase-grammar.tex:123-142](../../../../documents/archive--paper-latex--tfpt-v29/sections/003-subsection-flavor-and-the-phase-grammar.tex#L123) · `section:c857c002ffa7ed94e137` · section

@> Xcccc@ Branch & [formula in source] & [formula in source] & [formula in source] & [formula in source] \\ canonical carrier branch & [formula in source] & [formula in source] & [formula in source] & 137.03599921615843 \\ boundary multiplicity deformation & [formula in source] & [formula in source] & [formula in source] & 156.094045457 \\ boundary multiplicity deformation & [formula in source] & [formula in source] 

## TFPT: Carrier Algebra, Compression Identities, and Finite Completion\\[0.5em] An overdetermined rank-5 spectral theory on the oriented double cover

[documents/archive--paper-latex--tfpt-v30/preamble.tex:1-116](../../../../documents/archive--paper-latex--tfpt-v30/preamble.tex#L1) · `section:1b65be961c617457d120` · frontmatter

skins,breakable arrows.meta,positioning,calc,fit,backgrounds,matrix,decorations.pathmorphing compat=1.18

## Front matter / support

[documents/archive--paper-latex--tfpt-v30/sections/001-section-reading-guide-and-claim-map.tex:1-23](../../../../documents/archive--paper-latex--tfpt-v30/sections/001-section-reading-guide-and-claim-map.tex#L1) · `section:10ed59c4d51ebc81ad55` · frontmatter

A minimal carrier [formula in source] on the oriented double cover is shown to be the unique rank-5 split satisfying [formula in source] and [formula in source] . This carrier already forces the global Standard Model group [formula in source] , one chiral family with [formula in source] from the positive half-spinor, the hypercharge–seam inversion [formula in source] , and a self-consistent electromagnetic closure eq

## Big picture: what TFPT actually claims

[documents/archive--paper-latex--tfpt-v30/sections/001-section-reading-guide-and-claim-map.tex:106-129](../../../../documents/archive--paper-latex--tfpt-v30/sections/001-section-reading-guide-and-claim-map.tex#L106) · `section:d186bb25882f48f69fbe` · section

TFPT is presented here as a carrier-first theory of admissible vacua on the oriented double cover. The seam involution enforces the minimal carrier [formula in source] . That carrier fixes the global Standard Model group, hypercharge, and one chiral family. The family count [formula in source] is then supported by two independent routes: a local patch-deficit count and a global monodromy argument. The monodromy space

## Family monodromy and occupancy

[documents/archive--paper-latex--tfpt-v30/sections/002-subsection-character-trace-identities-and-the-abelian-in.tex:309-364](../../../../documents/archive--paper-latex--tfpt-v30/sections/002-subsection-character-trace-identities-and-the-abelian-in.tex#L309) · `section:4dfd6d1d0ae54e107e2b` · subsection

The simplest carrier-to-family bridge is to promote the three distinguished cycles into a monodromy space, [formula in source] so that [formula in source] . In this interpretation [formula in source] is neither an arbitrary flavor vector space nor a loose bookkeeping trick; it is a cycle space attached to the seam data. The geometric picture is shown in fig:family-triangle.

## Occupancy and boundary-to-bulk transgression

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:1-13](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L1) · `section:c62dd101b3fb5f44234f` · subsection

With the family bridge installed, the matter space becomes [formula in source] and the occupancy [formula in source] is already fixed by the preceding proposition. Here occupancy means the admissible chiral-state count after family lifting; it is not used as a primitive datum. The bridge point is not that family lifting creates a new numerical surcharge. Rather, the inherited hard kernel value [formula in source] adm

## From bridge to geometric completion

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:14-31](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L14) · `section:0b2eff2c53632282a578` · subsection

Once the carrier packet and family bridge are fixed, the focused main-text completion problem splits into a geometric program [formula in source] and a transport program [formula in source] . Record algebra is retained only as a conditional appendix layer in app:record.

## Relative APS and superconnection setup

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:32-43](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L32) · `section:abddd8b0a1c1d0ac1ab5` · subsection

The geometric completion is formulated on a graded bundle [formula in source] with a declared reference pair [formula in source] and APS-type boundary conditions on the seam [formula in source] ; see Appendix [formula in source] This is a construction, not yet a theorem. Its value is to keep grading, reference subtraction, seam data, and the [formula in source] channel in one object from the start rather than mixing 

## Bosonic relative index and Higgs selection

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:44-73](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L44) · `section:15b90d2c25e761fe7f36` · subsection

The bosonic relative index satisfies [formula in source] Consequently the unique light seam-even bosonic zero mode lies in [formula in source]

## Heat-kernel coefficient map and [formula in source] chi bifurcation

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:74-176](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L74) · `section:69c5091605b0ca192009` · subsection

The local target action is written as The coefficient bookkeeping expected from the relative spectral expansion is summarized in tab:heat-kernel-map.

## Completion program B: Yukawas, masses, flavor, confinement, and strong CP

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:177-180](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L177) · `section:40c61c33e8b926eb640b` · section

The second completion block is the transport compiler. Its role is to turn the carrier packet and the family/occupancy bridge into actual masses, mixings, hadronic admissibility, and strong-CP control. The logic is again staged: first the discrete phase operator and the transport kernel, then path-length masses and mixing data, then confinement and strong CP as transport-side admissibility statements.

## Discrete phase operator and transport grammar

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:181-209](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L181) · `section:0a553cb8b9ad18370c39` · subsection

Let [formula in source] This makes the phase grammar concrete rather than rhetorical. The six admissible phases are shown in fig:z6-circle, and CP acts by inversion [formula in source] on this circle.

## Regularized Yukawa kernels and path-length masses

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:210-305](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L210) · `section:17f5ff6729010d251df2` · subsection

Here is treated as a transport bridge parameter inherited from the cross-ratio and boundary-monodromy program, rather than as a proved hard-kernel identity. The full derivation is therefore deferred to the supplementary layer, while the regularized transport operator used here is and the singular limit [formula in source] is taken only in admissible sectors.

## CKM and PMNS sharpening

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:306-340](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L306) · `section:94948562d34b95ae29ea` · subsection

The leading CKM magnitudes on the transport branch are The CKM phase receives a tri-familial dressing beyond the raw topological [formula in source] : so [formula in source] remains the base monodromy phase and [formula in source] is the leading family-transport correction.

## Confinement as admissible word selection

[documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex:341-379](../../../../documents/archive--paper-latex--tfpt-v30/sections/003-subsection-occupancy-and-boundary-to-bulk-transgression.tex#L341) · `section:05bfa7920c557ec99f90` · subsection

For each carrier word [formula in source] , let [formula in source] be its color-center charge and let [formula in source] be its seam parity. Physical hadronic words satisfy [formula in source]

## E [formula in source] E8 as downstream scale grammar

[documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex:176-182](../../../../documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex#L176) · `section:543460db4565fb1e4fba` · section

E [formula in source] is not part of the primitive carrier ontology and should not compete with the seam data, the carrier theorem, or the completion program for explanatory priority. In the present main-text form it plays one restricted role only: a downstream scale grammar attached to the already fixed carrier norm. [formula in source]

## Permissiveness barrier and real-domain boundary

[documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex:261-288](../../../../documents/archive--paper-latex--tfpt-v30/sections/004-subsection-strong-cp-closure-as-conditional-steps.tex#L261) · `section:fa38cdf61469ef638bf8` · subsection

] Under the restricted trace grammar, stages [formula in source] and [formula in source] have no unambiguous physical target. If [formula in source] is allowed to scan over all simple rationals, these stages can mimic almost any scale between [formula in source] and [formula in source] GeV. They mark the exact boundary where E [formula in source] without a derived block-trace theorem becomes too permissive. The open 

## Falsification matrix

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:47-67](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L47) · `section:230265151fe86b2efd87` · subsection

@> p0.24 YY> p0.13 @ Statement & What would falsify it & Sector affected & Local or global failure \\ Minimal carrier [formula in source] & failure to recover the one-family packet or the global quotient from the carrier theorem & Hard & global \\ Family bridge and [formula in source] & no geometric monodromy interpretation of the three-cycle family space & Bridge & local-to-structural \\ Bosonic relative index selec

## Conditional master theorem

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:91-100](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L91) · `section:f749a2d6a8938dd337e7` · subsection

Assume the hard carrier and kernel layers summarized in tab:status-matrix, together with the completion statements of the geometric and transport programs and the declared comparison map [formula in source] . Then every observable in the present main-text scope is the output of one carrier-first relative spectral compiler from primitive seam data to scheme-specified observables.

## Finite proof obligations

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:101-120](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L101) · `section:3a3a9df38f284e056b4e` · subsection

@> p0.20 > p0.18 > p0.20 YY@ Target statement & Input data & Missing lemma & Minimal deliverable & Empirical consequence \\ Family space theorem & [formula in source] , [formula in source] , [formula in source] & monodromy-to-family theorem & derive [formula in source] from the seam cycle algebra & stabilizes the meaning of [formula in source] \\ Bosonic index closure & [formula in source] , [formula in source] & rel

## Conclusion

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:121-128](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L121) · `section:70b254bd9df14d93caf8` · section

The present paper argues that a small carrier-first core already fixes nontrivial physics: the minimal [formula in source] carrier, the global Standard Model quotient, one chiral family, the carrier norm [formula in source] , the abelian index, the seam constant [formula in source] , the corrected opening [formula in source] , and the electromagnetic closure channel. The compression identities and exclusion theorems 

## Global rotation angle and constants atlas

[documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex:226-309](../../../../documents/archive--paper-latex--tfpt-v30/sections/005-subsection-residual-map-and-principal-unresolved-compari.tex#L226) · `section:85d00b0b6c3f339df248` · subsection

The seam loop is assumed to carry one unit of spectral flow, [formula in source] Because the spin lift closes only after [formula in source] , the normalized rotation modulus is [formula in source] The cascade in fig:constant-cascade is kept here as technical bookkeeping rather than as an early main-text dependency graphic.

## Conditional minimal-parameter picture

[documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex:169-234](../../../../documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex#L169) · `section:f6b7f5c66f7a7bf901c9` · subsection

The next package is stronger but also more conditional. It assumes that the carrier rank, family multiplicity, and seam normalization are all read as closed rather than only partially inherited.

## Relative APS and superconnection setup

[documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex:235-247](../../../../documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex#L235) · `section:a0ac73faa933af59552a` · section

The geometric completion uses APS-type relative data aps1975. In practice this means: one works with a declared pair [formula in source] rather than a single unanchored operator, boundary conditions on the seam [formula in source] are part of the definition of the relative index, the [formula in source] -term keeps track of the residual spectral asymmetry, the superconnection package is used in the same spirit as the

## Optional record algebra, horizons, and prediction semantics

[documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex:282-286](../../../../documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex#L282) · `section:b764d8ae0b38cd19afa0` · section

This appendix keeps the record-level constructions available without letting them dominate the scope of explicit claims in the main paper.

## Horizons as conjectural inner seams

[documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex:327-334](../../../../documents/archive--paper-latex--tfpt-v30/sections/006-subsection-compression-identities-on-the-minimal-branch.tex#L327) · `section:f657450740beb3cf8787` · subsection

If a horizon is modeled as an inner seam, the manuscript uses only an approximate factorization language, [formula in source] or, better, an algebraic split on an appropriate code subspace. This appendix intentionally avoids selling the factorization as exact fundamental structure.

## tfptblue TFPT in One Map\\[0.4em] Boundary Polarization, Carrier Rigidity, and Observable Closure

[documents/archive--tfpt-45--00_orientation_note/preamble.tex:1-8](../../../../documents/archive--tfpt-45--00_orientation_note/preamble.tex#L1) · `section:2d3587201870d8c81de9` · frontmatter

tfptblue TFPT in One Map\\[0.4em] Boundary Polarization, Carrier Rigidity, and Observable Closure Stefan Hamann Alessandro Rizzo tfptgray Orientation Note for the TFPT 4.5 paper series –

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

## Series Map

[documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex:233-258](../../../../documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex#L233) · `section:74e461207c6ce033a883` · section

Boundary Polarization and the Primitive Kernel of TFPT. Establishes [formula in source] and keeps all Standard-Model claims out. Carrier Rigidity, Hypercharge, and the Standard Model Packet from Boundary Polarization. Establishes the rigid [formula in source] carrier, hypercharge, [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] , and [formula in source] . El

## Source Boundary

[documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex:265-276](../../../../documents/archive--tfpt-45--00_orientation_note/sections/001-section-what-tfpt-claims.tex#L265) · `section:7380db88a0ce2f695437` · section

The orientation note draws especially from the abstract, the closed-architecture box, Sections 1 and 2, the canonical rigid-object discussion, the structural falsification map, and the conclusion. It intentionally does not import the extended empirical ledgers, E8 stage atlas, CMB figures, or mass tables.

## tfptblue Boundary Polarization and the Primitive Kernel of TFPT

[documents/archive--tfpt-45--01_boundary_kernel/preamble.tex:1-7](../../../../documents/archive--tfpt-45--01_boundary_kernel/preamble.tex#L1) · `section:6a8ce74c5d3ba070bea7` · frontmatter

tfptblue Boundary Polarization and the Primitive Kernel of TFPT Stefan Hamann Alessandro Rizzo tfptgray Paper 1 of the TFPT 4.5 series –

## Front matter / support

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:1-89](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L1) · `section:6707621b12b5f3772c3d` · frontmatter

This paper isolates the primitive boundary kernel. Starting from the minimal operational seed and the one-sided boundary datum, it reconstructs the exact double, the deck involution, the Calderon polarization, the primitive admissibility complex, the primitive seam generator, the winding normalization [formula in source] , and the normalization [formula in source] . No Standard-Model, phenomenological, gravitational,

Explicit source references:

- [TFPT.Carrier.BoundaryPolarization.BoundaryPolarization](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L83) · explicit_lean_symbol

## Claim Map

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:90-110](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L90) · `section:f388f7f941baf59b7f2f` · section

The paper proves the first load-bearing arrow of the TFPT series: [formula in source] All later discrete, physical, and numerical structures are treated as unavailable here. The purpose is to make the boundary primitive kernel auditable on its own.

## One-Sided Boundary Datum

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:111-120](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L111) · `section:bc4b9e813b85171a99d2` · section

The starting object is [formula in source] The paper should keep only the source manuscript material needed to explain one-sided admissible data, induced boundary spectral data, and the passage to a doubled closed datum. The proof burden is that the primitive boundary structure is not chosen by hand.

## Exact Double and Deck Involution

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:121-130](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L121) · `section:7b3b47b77f66630b99e3` · section

The exact double reconstructs [formula in source] with [formula in source] as deck involution and [formula in source] as the involution induced by the Calderon polarization. This section carries the analytic interface to Calderon projectors and the primitive relative spectral dynamics from the source draft.

## Primitive Admissibility Complex

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:131-140](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L131) · `section:c8971769ac838900b92e` · section

The primitive selector is introduced before any color, determinant, family, or QFT sector: [formula in source] The section should include the primitive admissibility differential, the primitive Hodge form, and the selector upgrade logic only as far as it is needed to prove that a later full selector can factor through [formula in source] .

## Primitive Seam Generator

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:141-151](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L141) · `section:0a058b360956f9faa31f` · section

The primitive seam generator records the two normalizations that are allowed to survive this paper: [formula in source] The winding class is a primitive boundary output. It is not yet a family-counting or flavor transport input; those interpretations are postponed to Papers 2 and 3.

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

## Source Extraction Map

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:225-250](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L225) · `section:baa84683f82162539020` · section

Use : Sections 1 and 2 only as a shortened claim map. Sections 3.1 and 3.2 for primitive core, one-sided boundary datum, doubling, deck involution, Calderon projector, and primitive admissibility complex. Section 4.1 only for the primitive seam generator, [formula in source] , and [formula in source] . Sections 8.1–8.4 only for primitive selector and upgrade logic. Sections 9.1–9.3 for operational seed, admissible bo

## Not Used Here

[documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex:251-260](../../../../documents/archive--tfpt-45--01_boundary_kernel/sections/001-section-claim-map.tex#L251) · `section:3e4f001b6b3b62132221` · section

Carrier rigidity, the Standard-Model packet, exact electromagnetic closure, flavor transport, QFT reconstruction, gravity/metrology, cosmology, CMB targets, E8 grammar, horizons, and transient channels are not used as inputs in this paper.

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

## Source Extraction Map

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:266-310](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L266) · `section:1d17cb67633074f90691` · section

Use : Sections 3.3, 3.4, and 3.5 for carrier normal form, internal stabilizer, one-family packet, character identities, trace identities, and abelian index. Sections 5.1–5.3 only for carrier-relevant compression identities. Sections 6.1–6.6 for families, occupancy, and compact Higgs index. Sections 8.11–8.15 for the Yukawa-based discharge of carrier premises. Section 8.19 and Section 9.11 only for the joint discrete 

## Not Used Here

[documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex:311-317](../../../../documents/archive--tfpt-45--02_carrier_rigidity_standard_model_packet/sections/002-section-seam-winding-as-source-of-the-integer-conditions.tex#L311) · `section:d5e642aea3b342ff60d3` · section

Exact [formula in source] numerics, CKM/PMNS closure, pole-mass ledgers, OS/CAR reconstruction, local Minkowski nets, scattering, gravity/metrology, cosmology, CMB targets, and E8 grammar are not used as proof inputs in this paper.

## Compact UFE bridge for the birefringence seed

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:126-177](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L126) · `section:06db7a3e9e3e1c287faf` · subsection

Before the determinant-line response is invoked in its full form, the same retained seed admits a short bridge derivation that connects the boundary-normalised axion–photon coupling to the cosmological birefringence amplitude. Starting from the unified-field-equation reduction of the seam transfer, the dimensionless axion–photon anomaly coefficient is [formula in source] and the modified Maxwell sector responds to a 

## No-Knobs Audit

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:187-202](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L187) · `section:b4f215eea1ac180c1adf` · section

@p0.18 p0.2 p0.18 p0.13 Y@ Constant & First appearance & Prior dependency & Before [formula in source] ? & Variation consequence \\ [formula in source] & Paper 2 carrier theorem & Paper 1 primitive kernel & Yes & Breaks [formula in source] , gauge quotient, and all downstream readouts. \\ [formula in source] & Paper 1 seam generator & Boundary primitive kernel & Yes & Breaks family counting and transport branch norma

## Not Used Here

[documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex:241-250](../../../../documents/archive--tfpt-45--03_electromagnetic_closure_flavor_transport/sections/001-section-electromagnetic-closure.tex#L241) · `section:ac01d6f66ff8854f6dae` · section

Strong-CP admissibility closure, OS/CAR reconstruction, local Minkowski nets, scattering, gravity/metrology proofs, CMB spectra, sky realization, E8 grammar, horizons, and large pole-mass tables are not used as proof inputs in this paper.

## Not Used Here

[documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex:210-216](../../../../documents/archive--tfpt-45--04_admissibility_strong_cp_qft_closure/sections/001-section-selector-versus-dynamics.tex#L210) · `section:228132cd22c2701bbf15` · section

Exact electromagnetic benchmark derivations, CKM/PMNS prediction tables, gravity/metrology readouts, CMB spectra, sky realization, E8 grammar, full empirical ledgers, horizons, and transient channels are not used as proof inputs in this paper.

## tfptblue Geometric Hodge Closure and Dimensionless Metrology\\[0.35em] from the TFPT Boundary Branch

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/preamble.tex:1-8](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/preamble.tex#L1) · `section:501e611ed982c78e5d79` · frontmatter

tfptblue Geometric Hodge Closure and Dimensionless Metrology\\[0.35em] from the TFPT Boundary Branch Stefan Hamann Alessandro Rizzo tfptgray Paper 5 of the TFPT 4.5 series –

## Front matter / support

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:1-90](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L1) · `section:721911e8bd876db4d766` · frontmatter

This paper isolates the geometric and metrological branch of TFPT. The theory is not presented as predicting isolated SI numbers. Instead it constructs an internal dimensionless metrology from the boundary spectral unit [formula in source] , with gravity, Planck normalization, electroweak matching, and pole readouts expressed as boundary-normalized observables.

## Boundary Spectral Unit

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:91-99](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L91) · `section:a7f46b9c5e07103cd4b0` · section

The internal unit is [formula in source] All dimensionful-looking statements in this paper are rewritten as dimensionless quotients by powers of [formula in source] . This is the editorial rule that separates metrology from numerology.

## Geometric Hodge Closure

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:100-105](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L100) · `section:a85b970c0ab5bf9c0f63` · section

The geometric branch reconstructs a spectral Einstein functional and its Hodge closure. The paper should retain the source draft's geometric reconstruction, spectral Einstein functional, and Planck closure, but it should remove cosmological and horizon continuations.

## Planck Normalization

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:106-118](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L106) · `section:6f91b391bfcb41e42c2b` · section

The Planck readout is internal: [formula in source] The question is not which SI value of [formula in source] is inserted, but which dimensionless branch quotient is fixed.

## Einstein-limit normalizer [formula in source] xi = c3/phi0

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:119-162](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L119) · `section:88f7bb7763acd9ba04b2` · subsection

Once the boundary spectral unit [formula in source] , the seam constant [formula in source] , and the retained seed [formula in source] are fixed, a single dimensionless quotient governs the transition between the UFE-normalized boundary functional and the Einstein–Hilbert presentation. Writing [formula in source] for the Einstein–Hilbert prefactor, the boundary-branch reduction yields a relation of the form The prod

## Electroweak Matching

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:163-173](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L163) · `section:b30b9b028993b4c90136` · section

The electroweak matching layer is included only as boundary-normalized metrology: [formula in source] is an internal dimensionless output. Pole matching may be included in compact form when it is expressed as a quotient by [formula in source] .

## Observable Functor

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:174-189](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L174) · `section:da0dcdd20924f9cd4558` · section

The output layer is organized as [formula in source] Only the final projection chooses scheme or comparison conventions. The paper should keep this distinction visible whenever a physical readout is compared to an empirical row.

## Main Technical Development

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:190-210](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L190) · `section:70da2f72e0e0912c91df` · section

This section contains the main technical development assigned to this paper by the TFPT 4.5 clean split. Cross-paper background is referenced through dependency and scope boxes; extended backend material is kept in the Technical Companion.

## Source Extraction Map

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:211-234](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L211) · `section:8fca1a2211f07d612dd1` · section

Use : Sections 6.4, 6.7, 6.8, and 6.9 for geometric reconstruction, spectral Einstein functional, and Planck closure. Sections 6.21–6.26 for electroweak matching and pole matching. Section 13.2 only for observable hierarchy parts not already used in Paper 4. Section 14 in full as the dimensionless metrology core. Appendix C only in shortened form and without making E8 prominent.

## Not Used Here

[documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex:235-240](../../../../documents/archive--tfpt-45--05_geometric_hodge_closure_dimensionless_metrology/sections/001-section-boundary-spectral-unit.tex#L235) · `section:3989d5bf2e359ffa6552` · section

Late-time [formula in source] , CMB spectra, sky realization, black holes, horizons, E8 stage atlas, transient channels, and cosmological comparison rows are not used as proof inputs in this paper.

## tfptblue Cosmology Interfaces of the TFPT Closed Branch\\[0.35em] Seam Transfer, Axion Sector, Reheating, and CMB Targets

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/preamble.tex:1-8](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/preamble.tex#L1) · `section:79180875bf2f0eb43208` · frontmatter

tfptblue Cosmology Interfaces of the TFPT Closed Branch\\[0.35em] Seam Transfer, Axion Sector, Reheating, and CMB Targets Stefan Hamann Alessandro Rizzo tfptgray Paper 6 of the TFPT 4.5 series –

## Front matter / support

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:1-81](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L1) · `section:15a7d35d81ffae4245ac` · frontmatter

This paper isolates the downstream cosmology interface of TFPT. Cosmology is not used as a primitive selector of the theory. It is read from the closed branch through seam transfer, determinant-line phase, scalaron sector, axion interface, reheating input, leptogenesis input, neutrino sector, CMB spectra, and conjectural sky-map realization targets.

## Seam Transfer and Infrared Determinant

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:94-104](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L94) · `section:6fb36890eae3b31ae8d5` · section

The seam-transfer expression is [formula in source] The text should state which part is theorem-level interface data and which part is an empirical comparison convention.

## Axion Interface

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:105-117](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L105) · `section:d0ca2a1debedf9301f14` · section

The axion sector is recorded as [formula in source] The axion interface belongs here because it depends on seam transfer and determinant-line phase, not on the primitive carrier proof.

## Downstream Obligations Moved to the Companion

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:136-152](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L136) · `section:f0e60a47149e6eefb905` · section

@p0.28 Y@ Module & Status in this paper \\ Stationary horizons and compact objects & Listed only as downstream programmatic obligations; technical material is in the Companion. \\ Code subspace, pointer dynamics, and record algebra & Not part of the cosmology-interface proof surface. \\ Transient event channels & Falsification and prediction semantics belong to the Companion. \\ Pole masses, Higgs readout, and full f

## Source Extraction Map

[documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex:174-191](../../../../documents/archive--tfpt-45--06_cosmology_interfaces_downstream_closure/sections/001-section-cosmology-as-downstream-interface.tex#L174) · `section:7f8cc17f94ae4b0fb41a` · section

Use : Section 10 for FRW reduction, seam transfer, and scalaron branch. Sections 10.1 and 10.2 for falsification matrix and proof-obligation ledger. Appendix C.7, Appendix G, and the cosmology-interface proof material in Appendix J. Appendix N only for the axion-interface excerpt. Keep CMB Stage 1 and Stage 2 visibly separate.

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

## Lemma C (Thermal Transport).

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex:61-89](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/002-section-the-five-lemmas-native-closure-conjecture-v4-6.tex#L61) · `section:c1704f9d83f0690b188c` · paragraph

Four sub-claims, jointly: Proof skeletons. [formula in source] is a 4D radiation-density seam residue; [formula in source] is the QKE transport trace [formula in source] with three carrier families plus [formula in source] (weak-seam Ward) plus [formula in source] (EM holonomy); [formula in source] is the freeze-out occupancy [formula in source] with [formula in source] ; [formula in source] is the admissible line in

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

## The candidate v4.6 bundle

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:102-124](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L102) · `section:4427ed5d9336270018c6` · subsection

In the absence of a real Sprint-2A boundary extraction, v4.6.3 ships a deterministic candidate bundle synthesised from the seven primitives: [formula in source] : Hermitian, eigenvalues [formula in source] on [formula in source] ; [formula in source] : seam-graded [formula in source] modulated by [formula in source] , normalised; [formula in source] : pairing involution [formula in source] ; spectral flag: c [formula

## The 13\,\% RMS reduction

[documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex:163-177](../../../../documents/archive--tfpt-45--07_cmb_operational_closure_planck_pipeline/sections/003-section-stage-2-sky-realisation-four-modes-a-b-c-e.tex#L163) · `section:5d13a1defc2c75194bab` · subsection

The Mode-E residual RMS is [formula in source] , i.e.\ [formula in source] below the Mode-A RMS [formula in source] at the same [formula in source] . We do not interpret this as evidence for Lemma E. In the candidate construction, the Lemma-E phases happen to inherit a deterministic structure that is not aligned with the Planck realisation by construction — the bundle is not extracted from the boundary data. The 13\,
