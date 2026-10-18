# Verification, formalization and safeguards — part 9

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## v10 — upstream interfaces closed to the next algebraic layer

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex:95-178](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex#L95) · `section:98fb50cf22a3bc27377c` · subsection

Relative to v9, this version closes the three standing upstream gaps documented in the v9 limitations section. Each gap is replaced by a Mathlib-native structural Lean module:

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1) · explicit_file_citation
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)

## v9 — review-readiness pass and Stage D transparency

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex:179-235](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex#L179) · `section:45afc5b996923469d8f5` · subsection

Relative to v8, this version is a consistency-and-transparency revision rather than a structural one. It addresses internal version drift identified in the v8 review and adds one unconditional transparency theorem at the Stage D interface:

Explicit source references:

- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [verification/v8_horizon.py](../../../../verification/v8_horizon.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L1)

## v8 — Calderón structural + Higgs Stage B

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex:236-299](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex#L236) · `section:b08170f7809abebebd5e` · subsection

Relative to v7, this version upgrades two upstream interfaces from documentary wrappers to structural derivations, narrowing the "out of scope" column of the interface table:

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1) · explicit_file_citation
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean#L1) · explicit_file_citation
- [verification/v8_horizon.py](../../../../verification/v8_horizon.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L1) · explicit_file_citation
- [TFPT.Carrier.HiggsTopForm.DegreeOneTwoVarForm.finrank_eq_two](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L146) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L1)

## Remaining Lean lemma gap.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex:300-314](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex#L300) · `section:e82d0a8c6e8a726c1b29` · paragraph

The Stage D characterisation backward direction — existence of a [formula in source] triple from [formula in source] — requires showing that the wedge map [formula in source] , [formula in source] , is injective in dimension 3. The cleanest formalisation route extends a non-zero vector to a basis and uses exteriorPower.iotaMulti_family_linearIndependent_ofBasis to deduce [formula in source] . Mathlib does not yet hav

## v7 — Signature lock, predicate rename, interface discipline

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex:315-376](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex#L315) · `section:b28cd48f61366eb55359` · subsection

Relative to v6, this version hardens the audit interface, neutralises a semantically-loaded naming choice, and tightens the editorial framing around what the note does and does not claim:

Explicit source references:

- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrientedDeterminantCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrientedDeterminantCarrier.lean#L1) · explicit_file_citation
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## v6 — Yukawa Stage D and Calderón interface

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex:1-62](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex#L1) · `section:e0ce14615c94a8c30361` · subsection

Relative to v5, this version adds two new modules and resolves the standing review-level critique that "Stage C is data, not derivation":

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1) · explicit_file_citation
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)

## v5 — Yukawa Stage C

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex:63-107](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex#L63) · `section:f3a3765337eb4565c864` · subsection

Relative to v4, this version closes the Yukawa interface within Lean by introducing a third stage:

Explicit source references:

- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [TFPT.Carrier.YukawaPrimitive.PrimitiveIndecomposableYukawaCoupling.finrank_E_eq_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L139) · explicit_lean_symbol
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## v4 — Yukawa Stage B

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex:108-139](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex#L108) · `section:eede343e0e630fed2553` · subsection

In v4 the Yukawa rank discharge was promoted from a bare Stage-A rank witness ( [formula in source] , a numerical assumption in linear-equivalence dress) to a Stage-B algebraic hypothesis ( [formula in source] , a structural property of [formula in source] ).

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTopForm.lean#L1) · explicit_file_citation
- [TFPT.Carrier.YukawaTopForm.YukawaTopForm.nonempty_iff_finrank_eq_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTopForm.lean#L188) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## v3 — correcting overclaims

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex:140-218](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex#L140) · `section:96ccc530551994c85dee` · subsection

Scope of the title and the abstract. "SM Hypercharge Spectrum" [formula in source] " [formula in source] Hypercharge Carrier". The note no longer suggests it has formalised all SM chiral- multiplet hypercharges; only the carrier multiplet [formula in source] . Status of the Stage-A certificates. "Not assumptions" [formula in source] "structured Stage-A hypotheses, not bare numerical assumptions". The Higgs and Yukawa

Explicit source references:

- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [TFPT.Carrier.DeterminantCharacter.trace_zero_of_det_one_forall_rat](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/DeterminantCharacter.lean#L94) · explicit_lean_symbol
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [TFPT.Carrier.CarrierData.CarrierPremises.hypercharge_carrier_packet](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierData.lean#L213) · explicit_lean_symbol
- [TFPT.Carrier.DeterminantCharacter.trace_zero_of_det_one_at_two](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/DeterminantCharacter.lean#L118) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## Next Steps

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex:219-283](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex#L219) · `section:be1ea56966a7d77ab977` · section

CI workflow. Wire audit.sh into a GitHub Actions workflow that refuses any merge with AUDIT:\ FAIL.

Explicit source references:

- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)

## Result

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex:284-387](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex#L284) · `section:12c7290ffcb9db5f3bed` · section

Lean-verified outputs (v11). Abstract carrier polynomial: Polarization.sixY_carrier_polynomial. Boundary involution [formula in source] projectors: InvolutionProjectors.CarrierInvolution.toPolarization. Mathlib bridge: MathlibBridge.Polarization.toCompleteOrthogonalIdempotents. General integer rigidity: LatticeRigidityGeneral.primitive_trace_free_pair_general. Structural trace identity: TraceProjection.trace_linear_c

Explicit source references:

- [BoundaryPolarization.ofCarrierInvolution](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L184) · explicit_lean_symbol
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [TFPT.Carrier.YukawaStageDExistence.stage_D_iff_finrank_eq_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L306) · explicit_lean_symbol
- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## Reproducing the Build and Audit

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex:388-418](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/006-subsection-v6-yukawa-stage-d-and-calder-n-interface.tex#L388) · `section:05eb30f183fbe41ac436` · section

# 1. Install elan (Lean toolchain manager) curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \ | sh -s – -y –default-toolchain none export PATH=" [formula in source] PATH"

## Nachgereichte Texte: neue Norm, korrigierte Zustandszuordnung und Feldadapter

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex:21-30](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex#L21) · `section:d9f84c42ae1ceaa24a9b` · section

Die drei während der laufenden Prüfung nachgereichten Texte wurden vollständig gelesen und unverändert eingefroren. Sie sind keine Anweisungen, Ergebnisse ungeprüft zu übernehmen. Zwei Texte vereinfachen ältere Arbeitsstände stark; die dritte längere Forschungsnotiz enthält ausführlichere Beweise einer bereits bekannten grundsätzlichen Diagnose.

## 3. Die kleinste zusätzliche Operation ist schon algebraisch ausreichend

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/004-subsection-1-was-die-tats-chlichen-quellen.tex:158-205](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/004-subsection-1-was-die-tats-chlichen-quellen.tex#L158) · `section:276011355834b8427140` · subsection

Dabei ist der zweite Bosonindex BAR(A). Es gibt dreißig solche ungeordneten Paare. Die vollständige Invarianz von η wird an allen 45+15 ursprünglichen Liegeneratoren geprüft. Die 60 verschiedenen Bosongewichte und der zusammenhängende Lie-Wirkungsgraph beweisen zusätzlich, dass diese Paarung bis auf einen Skalar eindeutig ist.

## Anschluss an das nachgereichte Forschungspaper

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/004-subsection-1-was-die-tats-chlichen-quellen.tex:357-369](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/004-subsection-1-was-die-tats-chlichen-quellen.tex#L357) · `section:8ce13e13dfbb77e9b698` · subsubsection

Abschnitt 9 des nachgereichten Papers benutzt dasselbe Prinzip einer mitgerechneten Ladungsreferenz. Sein dortiger N=9-Vierzustandstransfer erhält mit der neuen Referenz eine einzelne innere Cartanladung. Unsere Konstruktion betrifft stattdessen N und erhält die vollständige innere Gruppe, erzeugt aber keine räumliche Übertragung. Sie ersetzt den dortigen Transferzeugen nicht und beweist dessen native Herkunft nicht.

## 7. Reproduktion und Beweisumfang

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/005-subsection-6-ressourcenbilanz-und-der-jetzt-konkrete-n-c.tex:59-94](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/005-subsection-6-ressourcenbilanz-und-der-jetzt-konkrete-n-c.tex#L59) · `section:27364edd8a48dcf99255` · subsection

Benötigt werden Python, NumPy, SciPy und SymPy. Der Replay liest nur die eingefrorenen Eingaben und braucht weder das ursprüngliche Repository noch Netzwerkzugriff. freeze.py ist nur das Herkunftswerkzeug für die erste Archivierung und gehört nicht zum wissenschaftlichen Replay.

## 2. Exakter Rangbeweis am Tensor

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/005-subsection-6-ressourcenbilanz-und-der-jetzt-konkrete-n-c.tex:177-224](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/005-subsection-6-ressourcenbilanz-und-der-jetzt-konkrete-n-c.tex#L177) · `section:79339c0899b81217a6b1` · subsection

Die Datei enthält zehn symmetrische 16×16-Matrizen β_k. Mit den sechs antisymmetrischen 4×4-Farbmatrizen ε_c gilt eintragsweise

## 5. Prüfung und unveränderte offene Grenze

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/006-subsubsection-unabh-ngige.tex:321-358](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/006-subsubsection-unabh-ngige.tex#L321) · `section:5db7732222bd9f247b33` · subsection

verify_causal.py benutzt explizite Fehlerbedingungen, keine abschaltbaren Assertions. Normaler Python-Lauf und python -OO, jeweils mit Warnungen als Fehler, erzeugen byte-identische JSON-Ergebnisse. Der optimierte Lauf wurde aus einem anderen Arbeitsverzeichnis gestartet; die Quelle wird relativ zum Prüfprogramm aufgelöst. Abhängigkeiten: NumPy, SymPy und SciPy.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_causal.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_causal.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/result_OO.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/result_OO.json#L1) · explicit_file_citation

## Beweisumfang

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/007-subsection-exakte-gemeinsame.tex:169-188](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/007-subsection-exakte-gemeinsame.tex#L169) · `section:6a2fc0f321f18ddaf44c` · subsection

verify_common3.py prüft den eingefrorenen W, die Isometrie, alle Intertwining-Identitäten, den ausdrücklichen n5-Leckterm, die zwei kausalen Endwahrscheinlichkeiten, beide symbolischen Determinanten und die rationale Inversen-Normschranke. common3.json und common3_OO.json sind die normalen und optimierten Replays. Der frühere Bericht und Prüfer wurden nicht geändert.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_common3.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_common3.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3_OO.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3_OO.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3.json#L1) · explicit_file_citation

## Reproduktionsbelege

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/008-subsection-3-der-text-vermischt-drei-verschiedene.tex:171-198](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/008-subsection-3-der-text-vermischt-drei-verschiedene.tex#L171) · `section:a1472e09f611fa71fe50` · subsection

late_a/verify.py prüft elf eingefrorene Eingaben, führt die ν1-ν5- Spurnetzwerke frisch aus und baut beide Ritzpolynome unabhängig neu auf. Es gibt 46 eigene Prüfbedingungen: 36 exakte beziehungsweise faktische Prüfungen und 10 numerische Konsistenzprüfungen, separat dazu 1239 ausgeführte Quellguards der Normkonstruktion. Die Guardzahl zählt keine unabhängigen mathematischen Theoreme.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py#L1) · explicit_file_citation

## Reproduktion

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex:101-123](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex#L101) · `section:14c7352aa21ce1d385e6` · subsection

Benötigt werden nur Python und SymPy. Der separate Lauf verifiziert zwei Quellenpins sowie 36 exakte Bedingungen pro Modus, keine numerischen Bedingungen. Normaler Lauf und -OO ergeben byte-identische JSON-Ausgaben; Warnungen gelten als Fehler und alle Guards bleiben unter Optimierung aktiv. Die vollständigen Matrizen stehen in late_field.normal.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py#L1) · explicit_file_citation

## Übernahmeurteil

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex:130-151](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex#L130) · `section:fac3e071baead3b636c1` · subsection

Der neue Text ist eine ausführlichere Fassung der bereits eingefrorenen fundamentalen Reduktion, ergänzt um die weitgehend gleiche frühere Gesprächszusammenfassung. Er bringt keinen neuen H-Term, keine neue Operationsquelle und keinen neuen Transferbeweis. Seine wesentlichen mathematischen Einschränkungen sind richtig und bleiben in der gemeinsamen Darstellung erhalten. Eine neue Großrechnung ist dafür nicht notwendi

Explicit source references:

- [experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt](../../../../experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation

## 9. Aktueller Stand T1 bis T8

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/011-subsubsection-4-3-zehn-vollst-ndige-energiemomente-der-g.tex:265-319](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/011-subsubsection-4-3-zehn-vollst-ndige-energiemomente-der-g.tex#L265) · `section:40ba66d2b86d563aefe3` · subsection

Die folgende Tabelle ordnet die Beiträge dieser Runde den bisherigen offenen Beweispflichten zu; sie benennt keine neue Definition der ursprünglichen Tore.

## Historischer Anhang: vollständige Fassung v1.6.6

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/013-subsubsection-b5-2-warum-das-noch-kein-holografischer.tex:284-292](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/013-subsubsection-b5-2-warum-das-noch-kein-holografischer.tex#L284) · `section:ec9e31bbdf525854ea3d` · section

Die folgende vollständige Fassung wird unverändert bewahrt. Maßgeblich für den aktuellen Status sind die vorangestellten Kapitel v1.6.7. Ältere Vorhaben, Modellannahmen und Zahlen erhalten dadurch keinen neuen Beweisstatus; die kleinen Energieverschärfungen und die neuen Singulett- und Bilinearergebnisse stehen oben.

## 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex:4-83](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex#L4) · `section:bd201db4b26077af03ab` · subsubsection

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-, Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch reproduziert. Darunter befinden sich neun wörtliche need(True, ...)-Guards mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu; Abschnitt 3 ersetzt sie durch eine explizite Konstru

## 8. T1-T8: gemeinsamer Fortschritt ohne Statusinflation

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex:187-237](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex#L187) · `section:ea0714b4c66468db184f` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Front & In dieser Revision weitergekommen & Noch erforderlicher Nachweis \\ T1 - Ursprung und Auswahl & Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer & Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand \\ T2 - Half-Charge/E8-Feld & Bestehender geladener Pol bleibt abgesichert, innere Dar

## 10. Belege und Reproduzierbarkeit

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex:272-293](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex#L272) · `section:6a66c45dec9591f482eb` · subsection

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit reproduziert die 1127 gelieferten Guards; eigene Programme behandeln Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion, basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählu

## Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex:297-304](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex#L297) · `section:ed249ca472af3c4b9ed2` · section

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1-T8 geschlossen seien.

## 4. Der bereits bewiesene native Grundsatz bleibt gültig

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/017-subsection-4-der-bereits-bewiesene-native-grundsatz-blei.tex:1-27](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/017-subsection-4-der-bereits-bewiesene-native-grundsatz-blei.tex#L1) · `section:87916f5e0b331e568bc5` · subsection

Der ältere, gepinnte Beweis lautet: Für Δ 0 und 0 g /Δ≤1/20 besitzt der unveränderte μ=0-Hamiltonoperator einen eindeutigen globalen Grundzustand in N=64; er ist ein Spin(10)×SU(4)-Singulett. Bei 1/20 bestehen außerdem positive Lücke und die bekannten Energie-, Besetzungs- und Polschranken.

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/017-subsection-4-der-bereits-bewiesene-native-grundsatz-blei.tex:145-172](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/017-subsection-4-der-bereits-bewiesene-native-grundsatz-blei.tex#L145) · `section:40dd3d4c7ac5a548bcda` · subsection

contracted_krylov.cpp ist der unabhängige ganzzahlige Kontraktionskern. verify.py prüft diesen Kern, die korrigierte Pythagoras-Rechnung, kleine Ritz-Matrizen, sämtliche angeführten Graph-, Kern- und Gradierungsidentitäten sowie die Matrixalgebra-Zertifikate. Die Ergebnisse stehen in audit.json und audit_optimized.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json#L1) · explicit_file_citation

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/019-subsubsection-6-4-kleinste-noch-zu-suchende.tex:21-60](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/019-subsubsection-6-4-kleinste-noch-zu-suchende.tex#L21) · `section:396e72082c21a0c0685d` · subsection

verify.py prüft 307 Bedingungen, verwendet keine Python-Assertions und reproduziert normal sowie mit -OO byteidentische JSON-Ergebnisse. Die Prüfung enthält:

## Anhang D: vollständiger Überlappungs-Audit

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/019-subsubsection-6-4-kleinste-noch-zu-suchende.tex:61-63](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/019-subsubsection-6-4-kleinste-noch-zu-suchende.tex#L61) · `section:96ec5566d2ed20acafb5` · section

No opening prose excerpt; see the source.

## Überlappung ist ein Forschungsansatz, kein schon hergeleiteter Link

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/019-subsubsection-6-4-kleinste-noch-zu-suchende.tex:64-83](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/019-subsubsection-6-4-kleinste-noch-zu-suchende.tex#L64) · `section:d84cb8e7d71c3dc11d8b` · section

Teil-Audit vom 15. September 2026 zum vollständig gelesenen neuen Anhang (748 Zeilen). Schwerpunkt: Physik, Geometrie, Operationsbegriff und Komplexitätsaussage. Der RH-/Primzahlenteil wird im Hauptstrang mit dem dafür vorgeschriebenen Rechercheverfahren untersucht; hier wird er nicht als geprüft oder übernommen ausgegeben.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py#L1) · explicit_file_citation

## Zusatzprüfung: Schleifen, Primzahlen und der Universalraum-Vorschlag

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex:48-62](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex#L48) · `section:d36cc029c6bedc022f41` · section

September 2026, v1.6.6. Quellenprüfung des nachgereichten Textes 59dc0059-8914-48ca-953d-85933f66e00b, kein neuer RH-Beweis und kein neuer arithmetischer Quellenoperator. Seine Aussagen über gemeinsame lokale Beschreibungen werden getrennt im Überlappungsaudit behandelt.

## 1. Was die endliche Bank tatsächlich ausschließt

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex:72-100](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex#L72) · `section:1c7886264b00443951b2` · subsection

Der beibehaltene Beweis aus v1.6.5 gilt für den ursprünglichen Hamiltonoperator mit 64 Fermion- und 60 Bosonmoden, Δ 0. Der Hilbertraum ist wegen der Bosonen nicht endlichdimensional. Endlich ist die Zahl der Moden. Mit C=960g²/Δ folgt aus quadratischem Ergänzen

## Historischer vollständiger Herleitungsstand v1.6.5 einschließlich v1.6.4

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex:230-238](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex#L230) · `section:b4c5f2a28f2af8f92d4e` · section

Der folgende Text wird unverändert bewahrt. Neue Gesamtstatusaussagen und Reichweitenkorrekturen stehen in der vorangestellten Revision v1.6.6. Historische Arbeitsaufträge oder Verfügbarkeitsannahmen werden dadurch nicht erneut zu aktuellen Beweisen erklärt.

## 1. Welche Quellen zusammengeführt werden

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex:309-354](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/020-subsection-10-ein-korrigierter-wirklich-entscheidbarer.tex#L309) · `section:4c9884700b1e237edec5` · subsection

Die Benutzeranlage addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt, eingefroren unter sources/user_attachment.txt. Die externe Untersuchung Universalraum_Beweisversuch_2026-09-15.md: Spektralzählung, Primzahl-Dynamik, Phasencocycle und kontrollierte Polnäherung. Die externe Untersuchung Universalraum_Urspruenglicher_Austausch_2026-09-15.md: interne Paarumwandlung, zusätzlicher Rotor-Link und älteres Round37-Beis

Explicit source references:

- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation

## 3.3 Das ältere 99,8718-\%-Beispiel ist ein anderer Träger

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/021-subsection-2-gemeinsame-native.tex:112-122](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/021-subsection-2-gemeinsame-native.tex#L112) · `section:e64367298cb3c0106197` · subsubsection

Die mitgelieferte Round37-Rechnung wurde exakt reproduziert. Ihre sechs Zustände sind der vollständige Gausssektor eines Vierfermion-Modells mit einem Link. Der zertifizierte Wert bei [formula in source] betrifft diesen Parent und diesen vorbereiteten Zustand. Er ist weder eine Zwei-64-Moden-Banken-Simulation noch ein Beweis für deren ursprüngliche Auswahl. Unser folgender Satz ist davon unabhängig und benutzt die ta

## 4. Zustandswahl: keine Rückkehr vor den abgesicherten Grundsatz

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/023-subsection-1-bersicht-bernehmen-korrigieren-oder.tex:127-159](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/023-subsection-1-bersicht-bernehmen-korrigieren-oder.tex#L127) · `section:01fd58449b8b33f3662c` · subsection

Der vorhandene native Satz beweist Eindeutigkeit, N=64, Singulett und positive Lücke bei μ=0 im angegebenen Kopplungsbereich. Eine komplette Clebsch-Gordan-Serie oder Voll-Diagonalisierung ist dafür nicht nötig; Vergleichsungleichungen und Minmax waren gerade der einfache Ausweg. Die physische Auswahl von H beziehungsweise μ=0 bleibt eine andere Frage.

## Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/023-subsection-1-bersicht-bernehmen-korrigieren-oder.tex:301-311](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/023-subsection-1-bersicht-bernehmen-korrigieren-oder.tex#L301) · `section:2a26f6d442de76283ca7` · section

Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. Die externe laufende Symmetrieergänzung wurde separat geprüft und ist nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.

## 3.1 Grundzustand: frische Berechnung statt bloßer Statusübernahme

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/024-subsection-2-ein-unver-nderter.tex:32-88](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/024-subsection-2-ein-unver-nderter.tex#L32) · `section:a2d4ed3c32b1ea013ff0` · subsubsection

Die ursprünglichen Programme wurden mit fixierten Dateihashes in eine eigene Arbeitskopie übernommen. Die Paar-Konfigurationen wurden frisch mit neu kompiliertem Quellcode berechnet:

## 6. Der Polsatz und seine zusätzliche Verschärfung

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/024-subsection-2-ein-unver-nderter.tex:281-330](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/024-subsection-2-ein-unver-nderter.tex#L281) · `section:ee6f0324fb025ab7ea26` · subsection

Der eingegangene Beweis verwendet [formula in source] . Invarianz und Besetzung ergeben

## 3. WP-C: Relativistisches Feldwörterbuch (fertig, 2161 exakte Guards, -OO-stabil)

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/027-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex:53-104](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/027-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex#L53) · `section:35f0d2cac921715c85a2` · subsection

@ > p( - 4 ) * 0.3000 > p( - 4 ) * 0.4000 > p( - 4 ) * 0.3000@ Kanal & Norm² pro Zeile & Status \\ Skalar, gleichhändig ε_\αβ\ψψ & 0 (alle 60 Zeilen, exakt) & verboten \\ Skalar, gepunktet (0,0) & 0 & verboten \\ (1,0) symmetrisch \I, σˣ, σᶻ\ & je 64, Summe 192 & erlaubt - der Vertex ist rein (1,0)+h.c. \\ (0,1) konjugiert & je 64 & erlaubt \\

## 6. Kreuzvalidierung der beiden Spuren

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/027-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex:194-232](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/027-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex#L194) · `section:5841f284e45a57163d4e` · subsection

@ > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500@ Befund & Meine Session & Parallelsession & Status \\ N=3-Zerlegung (7 Blöcke, Mults 2,2,2,1,1,1,1) & ✓ & ✓ & identisch \\ Casimirwerte (je Block) & (45,15), (85,15), & C = (C_S+C_U)/4 = 15, 25, 45, 21, 31, 45, 45 & identisch (zwei Normierungen) \\ Kommutant S1 (volle Symmetrie) & 7 & 7 & identisch \\ Kommutant S0 (X, N_b) & 1 452 961 7

## Nutzerquelle C: Multiplizitaeten und Z4

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/028-section-nutzerquelle-c-multiplizitaeten-und.tex:1-332](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/028-section-nutzerquelle-c-multiplizitaeten-und.tex#L1) · `section:7399d2b0808093b71fa5` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle D: fundamentale Reduktion

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/029-section-nutzerquelle-d-fundamentale.tex:1-180](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/029-section-nutzerquelle-d-fundamentale.tex#L1) · `section:f8feb7dc8c3bc9483966` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle E: gemeinsamer ausfuehrbarer Prozess

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/030-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex:1-363](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/030-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex#L1) · `section:e7a8e550e2e7c2010910` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle F: Operationssatz, Grundzustand und Feldwoerterbuch v1.6.3

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/030-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex:364-370](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/030-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex#L364) · `section:8925055aa81b02fbdfc3` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## 8. Die jetzt entscheidenden Prüfungen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/032-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex:63-89](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/032-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex#L63) · `section:b2985e5f28d80172d59a` · subsection

Untergrenzen verschärfen. Die Casimir-Schranke trennt N=64 bei 1/20 nicht von N=62 und N=66. Eine Jacobi-Vergleichsschranke mit rigorosen Normschranken für TT† je Bosonzahl oder eine Temple-Schranke auf der Ritz-Kette würde den Beweisbereich anheben. Den Zwei-Boson-Singulettraum ausschreiben. w₂ ist der erste Zeuge; die volle Lanczos-Kette von H (nicht nur von T†) ab Tiefe 4 braucht w₂ und seine Nachfolger. Operation

## 9. Verifikation und nicht übernommene Behauptungen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/032-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex:90-116](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/032-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex#L90) · `section:e00312dd04a50beaef17` · subsection

replay.py führt fünf Prüfer normal und unter -OO aus und verlangt byteidentische Ausgaben; Status, Hashes und Guardsummen stehen in replay_manifest.json. Guardzahlen zählen Prüfbedingungen, keine unabhängigen Theoreme. Exakt heißt ganzzahlig/rational; numerisch heißt float64 mit Toleranz-Guard (Ritz-Eigenwerte ab 3×3, Observablen, Erste-Moment-Auswertungen).

## Evidenzkonvention und Abgrenzung

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:4-6](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L4) · `section:5f952ab932298d5fceb2` · section

Wie im Manuskript: gesetzt bezeichnet eine Ausgangsannahme, exakt eine Identität oder einen Beweis unter genannten Voraussetzungen, bedingt eine Folgerung mit zusätzlicher physikalischer Zuordnung, offen eine ungeschlossene Herkunfts- oder Existenzfrage. Alle Zahlen stammen aus den in Anhang A genannten Prüfern; jeder läuft normal und unter python -OO bytegleich. Kein Marker im Ledger wurde bewegt. Alle physikalische

## Kollektiv unsichtbar, relativ sichtbar

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:48-55](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L48) · `section:0a13ef85d898cd076bfb` · subsection

Auf [formula in source] gilt [formula in source] für jede [formula in source] -Matrix [formula in source] ; jede kollektive Operation ändert nur eine globale Phase. Für einen Tick auf genau einem Träger gilt exakt [formula in source] wobei [formula in source] die Paarmarginale nach dem Tick ist. Beweis der Paarformel: [formula in source] . Beide Identitäten sind auf dem expliziten Singulett numerisch bestätigt.

## 9. Aktueller Stand T1 bis T8

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/002-subsection-4-die-richtige-einfache-kette-wiederholung-vo.tex:341-395](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/002-subsection-4-die-richtige-einfache-kette-wiederholung-vo.tex#L341) · `section:fe56ad5839cc30693707` · subsection

Die folgende Tabelle ordnet die Beiträge dieser Runde den bisherigen offenen Beweispflichten zu; sie benennt keine neue Definition der ursprünglichen Tore.

## Historischer Anhang: vollständige Fassung v1.6.6

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/004-subsection-b5-holografie-und-schatten-die-konkrete-nativ.tex:322-330](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/004-subsection-b5-holografie-und-schatten-die-konkrete-nativ.tex#L322) · `section:de75af879906bbb81aef` · section

Die folgende vollständige Fassung wird unverändert bewahrt. Maßgeblich für den aktuellen Status sind die vorangestellten Kapitel v1.6.7. Ältere Vorhaben, Modellannahmen und Zahlen erhalten dadurch keinen neuen Beweisstatus; die kleinen Energieverschärfungen und die neuen Singulett- und Bilinearergebnisse stehen oben.

## 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/005-subsubsection-leseschl-ssel-label-leseschluxfcssel.tex:75-154](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/005-subsubsection-leseschl-ssel-label-leseschluxfcssel.tex#L75) · `section:94e92e7b64b5804606ae` · subsubsection

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-, Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch reproduziert. Darunter befinden sich neun wörtliche need(True, ...)-Guards mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu; Abschnitt 3 ersetzt sie durch eine explizite Konstru

## 8. T1-T8: gemeinsamer Fortschritt ohne Statusinflation

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/006-subsection-5-neuer-kleiner-transportzeuge-mit-tats-chlic.tex:267-317](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/006-subsection-5-neuer-kleiner-transportzeuge-mit-tats-chlic.tex#L267) · `section:9bd14da4f52922be1ca1` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Front & In dieser Revision weitergekommen & Noch erforderlicher Nachweis \\ T1 - Ursprung und Auswahl & Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer & Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand \\ T2 - Half-Charge/E8-Feld & Bestehender geladener Pol bleibt abgesichert, innere Dar

## 10. Belege und Reproduzierbarkeit

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/006-subsection-5-neuer-kleiner-transportzeuge-mit-tats-chlic.tex:352-373](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/006-subsection-5-neuer-kleiner-transportzeuge-mit-tats-chlic.tex#L352) · `section:71c070fdfefb31f444ca` · subsection

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit reproduziert die 1127 gelieferten Guards; eigene Programme behandeln Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion, basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählu

## Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/007-section-anhang-a-quellenpr-fung-symmetrie-und.tex:4-11](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/007-section-anhang-a-quellenpr-fung-symmetrie-und.tex#L4) · `section:894639b2cfe62cfe99b4` · section

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1-T8 geschlossen seien.

## 4. Der bereits bewiesene native Grundsatz bleibt gültig

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/008-subsection-3-die-sechste-dezimalstelle-ist-richtig-aber-.tex:74-100](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/008-subsection-3-die-sechste-dezimalstelle-ist-richtig-aber-.tex#L74) · `section:47e25be8c27c2eda6cf2` · subsection

Der ältere, gepinnte Beweis lautet: Für Δ 0 und 0 g /Δ≤1/20 besitzt der unveränderte μ=0-Hamiltonoperator einen eindeutigen globalen Grundzustand in N=64; er ist ein Spin(10)×SU(4)-Singulett. Bei 1/20 bestehen außerdem positive Lücke und die bekannten Energie-, Besetzungs- und Polschranken.

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/008-subsection-3-die-sechste-dezimalstelle-ist-richtig-aber-.tex:218-245](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/008-subsection-3-die-sechste-dezimalstelle-ist-richtig-aber-.tex#L218) · `section:c0d1e26524a48db839bb` · subsection

contracted_krylov.cpp ist der unabhängige ganzzahlige Kontraktionskern. verify.py prüft diesen Kern, die korrigierte Pythagoras-Rechnung, kleine Ritz-Matrizen, sämtliche angeführten Graph-, Kern- und Gradierungsidentitäten sowie die Matrixalgebra-Zertifikate. Die Ergebnisse stehen in audit.json und audit_optimized.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json#L1) · explicit_file_citation

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/010-subsubsection-6-3-clock-mittelung-ist-m-glich-aber-der-f.tex:87-126](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/010-subsubsection-6-3-clock-mittelung-ist-m-glich-aber-der-f.tex#L87) · `section:fe40d8f2bf05b78dec02` · subsection

verify.py prüft 307 Bedingungen, verwendet keine Python-Assertions und reproduziert normal sowie mit -OO byteidentische JSON-Ergebnisse. Die Prüfung enthält:

## Anhang D: vollständiger Überlappungs-Audit

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/010-subsubsection-6-3-clock-mittelung-ist-m-glich-aber-der-f.tex:127-129](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/010-subsubsection-6-3-clock-mittelung-ist-m-glich-aber-der-f.tex#L127) · `section:6475a58cabc6858aca3e` · section

No opening prose excerpt; see the source.

## Überlappung ist ein Forschungsansatz, kein schon hergeleiteter Link

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/010-subsubsection-6-3-clock-mittelung-ist-m-glich-aber-der-f.tex:130-149](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/010-subsubsection-6-3-clock-mittelung-ist-m-glich-aber-der-f.tex#L130) · `section:a44c7d881e0e7918b5ae` · section

Teil-Audit vom 15. September 2026 zum vollständig gelesenen neuen Anhang (748 Zeilen). Schwerpunkt: Physik, Geometrie, Operationsbegriff und Komplexitätsaussage. Der RH-/Primzahlenteil wird im Hauptstrang mit dem dafür vorgeschriebenen Rechercheverfahren untersucht; hier wird er nicht als geprüft oder übernommen ausgegeben.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py#L1) · explicit_file_citation

## Zusatzprüfung: Schleifen, Primzahlen und der Universalraum-Vorschlag

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/011-subsection-7-operationsgeometrie-ben-tigt-mehr-als.tex:116-130](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/011-subsection-7-operationsgeometrie-ben-tigt-mehr-als.tex#L116) · `section:7dfef19386e6d6283d12` · section

September 2026, v1.6.6. Quellenprüfung des nachgereichten Textes 59dc0059-8914-48ca-953d-85933f66e00b, kein neuer RH-Beweis und kein neuer arithmetischer Quellenoperator. Seine Aussagen über gemeinsame lokale Beschreibungen werden getrennt im Überlappungsaudit behandelt.

## 1. Was die endliche Bank tatsächlich ausschließt

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/011-subsection-7-operationsgeometrie-ben-tigt-mehr-als.tex:140-168](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/011-subsection-7-operationsgeometrie-ben-tigt-mehr-als.tex#L140) · `section:94d32a5ca2d7e1840685` · subsection

Der beibehaltene Beweis aus v1.6.5 gilt für den ursprünglichen Hamiltonoperator mit 64 Fermion- und 60 Bosonmoden, Δ 0. Der Hilbertraum ist wegen der Bosonen nicht endlichdimensional. Endlich ist die Zahl der Moden. Mit C=960g²/Δ folgt aus quadratischem Ergänzen

## Historischer vollständiger Herleitungsstand v1.6.5 einschließlich v1.6.4

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/011-subsection-7-operationsgeometrie-ben-tigt-mehr-als.tex:298-306](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/011-subsection-7-operationsgeometrie-ben-tigt-mehr-als.tex#L298) · `section:0bfc1a1996ea7551fd8a` · section

Der folgende Text wird unverändert bewahrt. Neue Gesamtstatusaussagen und Reichweitenkorrekturen stehen in der vorangestellten Revision v1.6.6. Historische Arbeitsaufträge oder Verfügbarkeitsannahmen werden dadurch nicht erneut zu aktuellen Beweisen erklärt.

## 1. Welche Quellen zusammengeführt werden

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/012-subsection-1-welche-quellen-zusammengef-hrt.tex:1-46](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/012-subsection-1-welche-quellen-zusammengef-hrt.tex#L1) · `section:584bd08c65b5915fd0cf` · subsection

Die Benutzeranlage addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt, eingefroren unter sources/user_attachment.txt. Die externe Untersuchung Universalraum_Beweisversuch_2026-09-15.md: Spektralzählung, Primzahl-Dynamik, Phasencocycle und kontrollierte Polnäherung. Die externe Untersuchung Universalraum_Urspruenglicher_Austausch_2026-09-15.md: interne Paarumwandlung, zusätzlicher Rotor-Link und älteres Round37-Beis

Explicit source references:

- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt#L1) · explicit_file_citation

## 3.3 Das ältere 99,8718-\%-Beispiel ist ein anderer Träger

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/012-subsection-1-welche-quellen-zusammengef-hrt.tex:158-168](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/012-subsection-1-welche-quellen-zusammengef-hrt.tex#L158) · `section:3e1c09783c7bfecb4d0f` · subsubsection

Die mitgelieferte Round37-Rechnung wurde exakt reproduziert. Ihre sechs Zustände sind der vollständige Gausssektor eines Vierfermion-Modells mit einem Link. Der zertifizierte Wert bei [formula in source] betrifft diesen Parent und diesen vorbereiteten Zustand. Er ist weder eine Zwei-64-Moden-Banken-Simulation noch ein Beweis für deren ursprüngliche Auswahl. Unser folgender Satz ist davon unabhängig und benutzt die ta

## 4. Zustandswahl: keine Rückkehr vor den abgesicherten Grundsatz

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/014-subsection-11-reproduktion-und-ehrliche.tex:168-200](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/014-subsection-11-reproduktion-und-ehrliche.tex#L168) · `section:9de453c41d8f3946c1ed` · subsection

Der vorhandene native Satz beweist Eindeutigkeit, N=64, Singulett und positive Lücke bei μ=0 im angegebenen Kopplungsbereich. Eine komplette Clebsch-Gordan-Serie oder Voll-Diagonalisierung ist dafür nicht nötig; Vergleichsungleichungen und Minmax waren gerade der einfache Ausweg. Die physische Auswahl von H beziehungsweise μ=0 bleibt eine andere Frage.

## Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/014-subsection-11-reproduktion-und-ehrliche.tex:342-352](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/014-subsection-11-reproduktion-und-ehrliche.tex#L342) · `section:af18f417563cb829f222` · section

Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. Die externe laufende Symmetrieergänzung wurde separat geprüft und ist nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.

## 3.1 Grundzustand: frische Berechnung statt bloßer Statusübernahme

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/015-subsection-1-ergebnis-in-einem-satz-label-ergebnis-in-ei.tex:87-143](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/015-subsection-1-ergebnis-in-einem-satz-label-ergebnis-in-ei.tex#L87) · `section:a73613a159bcdd4dc679` · subsubsection

Die ursprünglichen Programme wurden mit fixierten Dateihashes in eine eigene Arbeitskopie übernommen. Die Paar-Konfigurationen wurden frisch mit neu kompiliertem Quellcode berechnet:

## 6. Der Polsatz und seine zusätzliche Verschärfung

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/015-subsection-1-ergebnis-in-einem-satz-label-ergebnis-in-ei.tex:336-385](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/015-subsection-1-ergebnis-in-einem-satz-label-ergebnis-in-ei.tex#L336) · `section:afa12163ab34b8af960b` · subsection

Der eingegangene Beweis verwendet [formula in source] . Invarianz und Besetzung ergeben

## 3. WP-C: Relativistisches Feldwörterbuch (fertig, 2161 exakte Guards, -OO-stabil)

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/018-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex:53-104](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/018-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex#L53) · `section:fa058c94fbeda7b27859` · subsection

@ > p( - 4 ) * 0.3000 > p( - 4 ) * 0.4000 > p( - 4 ) * 0.3000@ Kanal & Norm² pro Zeile & Status \\ Skalar, gleichhändig ε_\αβ\ψψ & 0 (alle 60 Zeilen, exakt) & verboten \\ Skalar, gepunktet (0,0) & 0 & verboten \\ (1,0) symmetrisch \I, σˣ, σᶻ\ & je 64, Summe 192 & erlaubt - der Vertex ist rein (1,0)+h.c. \\ (0,1) konjugiert & je 64 & erlaubt \\

## 6. Kreuzvalidierung der beiden Spuren

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/018-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex:194-232](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/018-subsubsection-die-isotypie-zerlegung-von-n-3-beide-spure.tex#L194) · `section:4337292367397f5af33d` · subsection

@ > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500@ Befund & Meine Session & Parallelsession & Status \\ N=3-Zerlegung (7 Blöcke, Mults 2,2,2,1,1,1,1) & ✓ & ✓ & identisch \\ Casimirwerte (je Block) & (45,15), (85,15), & C = (C_S+C_U)/4 = 15, 25, 45, 21, 31, 45, 45 & identisch (zwei Normierungen) \\ Kommutant S1 (volle Symmetrie) & 7 & 7 & identisch \\ Kommutant S0 (X, N_b) & 1 452 961 7

## Nutzerquelle C: Multiplizitaeten und Z4

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/019-section-nutzerquelle-c-multiplizitaeten-und.tex:1-332](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/019-section-nutzerquelle-c-multiplizitaeten-und.tex#L1) · `section:7a4ca181379581c08c32` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle D: fundamentale Reduktion

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/020-section-nutzerquelle-d-fundamentale.tex:1-180](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/020-section-nutzerquelle-d-fundamentale.tex#L1) · `section:01d244e6aa6dba0fc743` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle E: gemeinsamer ausfuehrbarer Prozess

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/021-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex:1-363](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/021-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex#L1) · `section:03dc40de26fb9251a289` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle F: Operationssatz, Grundzustand und Feldwoerterbuch v1.6.3

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/021-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex:364-370](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/021-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex#L364) · `section:cc07e91654931ba01589` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## 8. Die jetzt entscheidenden Prüfungen

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/023-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex:63-89](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/023-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex#L63) · `section:05bd93a177dfeb8a3137` · subsection

Untergrenzen verschärfen. Die Casimir-Schranke trennt N=64 bei 1/20 nicht von N=62 und N=66. Eine Jacobi-Vergleichsschranke mit rigorosen Normschranken für TT† je Bosonzahl oder eine Temple-Schranke auf der Ritz-Kette würde den Beweisbereich anheben. Den Zwei-Boson-Singulettraum ausschreiben. w₂ ist der erste Zeuge; die volle Lanczos-Kette von H (nicht nur von T†) ab Tiefe 4 braucht w₂ und seine Nachfolger. Operation

## 9. Verifikation und nicht übernommene Behauptungen

[documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/023-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex:90-116](../../../../documents/experiments--theory-contracts--universalraum-singlet-observable-20260915--tmp--pdfs--TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7/sections/023-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex#L90) · `section:24fabfcc98fe25546496` · subsection

replay.py führt fünf Prüfer normal und unter -OO aus und verlangt byteidentische Ausgaben; Status, Hashes und Guardsummen stehen in replay_manifest.json. Guardzahlen zählen Prüfbedingungen, keine unabhängigen Theoreme. Exakt heißt ganzzahlig/rational; numerisch heißt float64 mit Toleranz-Guard (Ritz-Eigenwerte ab 3×3, Observablen, Erste-Moment-Auswertungen).

## Vollständiger Beweis: höhere Antwort und positive Kopplungsmatrix

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/002-subsection-7-was-die-vier-rechnungen-gemeinsam-haben-und.tex:206-208](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/002-subsection-7-was-die-vier-rechnungen-gemeinsam-haben-und.tex#L206) · `section:374cd20b88a9ce296e23` · section

No opening prose excerpt; see the source.

## 9. Reproduktion und Grenze

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/003-subsection-5-allgemeine-car-identit-t-auf.tex:169-185](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/003-subsection-5-allgemeine-car-identit-t-auf.tex#L169) · `section:788a1aba5110cb5503e6` · subsection

verify_composition.py führt 67 explizite exakt arbeitende Prüfbedingungen aus, einschließlich Quellenpins und Strukturguards. Es gibt keine numerischen Toleranzprüfungen. Die allgemeine Formel und ihre Inversion sind oben algebraisch hergeleitet; drei vollständige N=3-CAR-Aufbauten kontrollieren Normalisierung, Vorzeichen und komplexe Konvention unabhängig.

## 7. Reproduktion und Prüfgrenze

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/004-subsection-3-exakt-geschlossener-ablauf-und-messbarer.tex:178-207](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/004-subsection-3-exakt-geschlossener-ablauf-und-messbarer.tex#L178) · `section:19b56294f1dd3605ca29` · subsection

python3 verify.py –output results_normal.json und python3 -OO verify.py –output results_optimized.json; REPLAY.json versiegelt Exitcodes, Prüferhash und identische Resultatbytes. replay.py führt beide Varianten lokal aus. Keine Netz-/Live-Repo-Imports, keine große Grundzustandsdiagonalisierung und keine Änderung älterer v1.6.8-Dateien.

## 6. Verifikation und verbleibender Herkunftsschritt

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/005-subsection-3-schaltbarkeit-und-arbeit-werden.tex:150-193](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/005-subsection-3-schaltbarkeit-und-arbeit-werden.tex#L150) · `section:b832eb63610b73ea4b30` · subsection

Für den parallelen Quellvergleich ist zusätzlich ein dimensionsunabhängiger kleiner Blocksatz geprüft: Bei [formula in source] und einem normierten Eingang v auf der Bosonseite ist die erste und dritte Ableitung der Boson-Überlebenswahrscheinlichkeit null, während [formula in source] . Somit gilt [formula in source] . Dieser reine Blocksatz verbindet dieselbe Nb-Auslese mit einem Kopplungs-Gramoperator; er leitet die

## Nachgereichte Texte: neue Norm, korrigierte Zustandszuordnung und Feldadapter

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/008-subsubsection-warum-nur-ein-schatten-auch-nach-beliebig-.tex:290-299](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/008-subsubsection-warum-nur-ein-schatten-auch-nach-beliebig-.tex#L290) · `section:eeb3a1cf7d416dca7171` · section

Die drei während der laufenden Prüfung nachgereichten Texte wurden vollständig gelesen und unverändert eingefroren. Sie sind keine Anweisungen, Ergebnisse ungeprüft zu übernehmen. Zwei Texte vereinfachen ältere Arbeitsstände stark; die dritte längere Forschungsnotiz enthält ausführlichere Beweise einer bereits bekannten grundsätzlichen Diagnose.

## 3. Die kleinste zusätzliche Operation ist schon algebraisch ausreichend

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/010-subsubsection-instrumente-und-die-genaue.tex:20-67](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/010-subsubsection-instrumente-und-die-genaue.tex#L20) · `section:833648cb12b6eb75534f` · subsection

Dabei ist der zweite Bosonindex BAR(A). Es gibt dreißig solche ungeordneten Paare. Die vollständige Invarianz von η wird an allen 45+15 ursprünglichen Liegeneratoren geprüft. Die 60 verschiedenen Bosongewichte und der zusammenhängende Lie-Wirkungsgraph beweisen zusätzlich, dass diese Paarung bis auf einen Skalar eindeutig ist.

## Anschluss an das nachgereichte Forschungspaper

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/010-subsubsection-instrumente-und-die-genaue.tex:219-231](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/010-subsubsection-instrumente-und-die-genaue.tex#L219) · `section:97aa68e4e894d595aab3` · subsubsection

Abschnitt 9 des nachgereichten Papers benutzt dasselbe Prinzip einer mitgerechneten Ladungsreferenz. Sein dortiger N=9-Vierzustandstransfer erhält mit der neuen Referenz eine einzelne innere Cartanladung. Unsere Konstruktion betrifft stattdessen N und erhält die vollständige innere Gruppe, erzeugt aber keine räumliche Übertragung. Sie ersetzt den dortigen Transferzeugen nicht und beweist dessen native Herkunft nicht.

## 7. Reproduktion und Beweisumfang

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/010-subsubsection-instrumente-und-die-genaue.tex:290-325](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/010-subsubsection-instrumente-und-die-genaue.tex#L290) · `section:9d03100e28aedb943e61` · subsection

Benötigt werden Python, NumPy, SciPy und SymPy. Der Replay liest nur die eingefrorenen Eingaben und braucht weder das ursprüngliche Repository noch Netzwerkzugriff. freeze.py ist nur das Herkunftswerkzeug für die erste Archivierung und gehört nicht zum wissenschaftlichen Replay.

## 2. Exakter Rangbeweis am Tensor

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/011-subsection-1-ein-gemeinsamer-tr-ger-mehrere.tex:56-103](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/011-subsection-1-ein-gemeinsamer-tr-ger-mehrere.tex#L56) · `section:a3a3802cb3302c9a3660` · subsection

Die Datei enthält zehn symmetrische 16×16-Matrizen β_k. Mit den sechs antisymmetrischen 4×4-Farbmatrizen ε_c gilt eintragsweise

## 5. Prüfung und unveränderte offene Grenze

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/012-subsection-2-lokale-algebra-und-ehrlicher.tex:169-206](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/012-subsection-2-lokale-algebra-und-ehrlicher.tex#L169) · `section:13c59592bec0830ce708` · subsection

verify_causal.py benutzt explizite Fehlerbedingungen, keine abschaltbaren Assertions. Normaler Python-Lauf und python -OO, jeweils mit Warnungen als Fehler, erzeugen byte-identische JSON-Ergebnisse. Der optimierte Lauf wurde aus einem anderen Arbeitsverzeichnis gestartet; die Quelle wird relativ zum Prüfprogramm aufgelöst. Abhängigkeiten: NumPy, SymPy und SciPy.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/result_OO.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/result_OO.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_causal.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_causal.py#L1) · explicit_file_citation

## Beweisumfang

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:1-20](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L1) · `section:b3cf658dea351b1b3072` · subsection

verify_common3.py prüft den eingefrorenen W, die Isometrie, alle Intertwining-Identitäten, den ausdrücklichen n5-Leckterm, die zwei kausalen Endwahrscheinlichkeiten, beide symbolischen Determinanten und die rationale Inversen-Normschranke. common3.json und common3_OO.json sind die normalen und optimierten Replays. Der frühere Bericht und Prüfer wurden nicht geändert.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_common3.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_common3.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3_OO.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3_OO.json#L1) · explicit_file_citation

## Nachtragsprüfung A: neue fünfte Norm und richtige Antwortzustände

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:21-23](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L21) · `section:348114a2d414af3f02e0` · section

No opening prose excerpt; see the source.

## Nachtrag A: Was am neuen v1.6.3-Erklärtext wirklich neu ist

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:24-26](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L24) · `section:315ae129b3254892e07e` · section

No opening prose excerpt; see the source.

## Urteil

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:27-45](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L27) · `section:1a1728fd2ea0bb1d4b6b` · subsection

Ja, ein belastbarer neuer Rechenschritt ist enthalten: Die zuvor fehlende Norm ν5 liegt jetzt mit passendem Quellstand vor. Wir haben ν1 bis ν5 frisch durch die ursprüngliche exakte Spurnetzwerkrechnung reproduziert und daraus unabhängig strengere rationale Ritzgrenzen gewonnen. Die übrigen großen Aussagen des Textes sind teils bereits bekannt, teils durch v1.6.7 korrigiert. Besonders problematisch ist die Vermischun

## 1. ν5 ist jetzt ein Ergebnis, nicht mehr nur eine Programmeinstellung

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:46-99](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L46) · `section:e2bfcce95c5b774160cd` · subsection

Der v1.6.7-Snapshot hatte zu Recht festgehalten, dass damals norms_by_traces.json und ein abgeschlossener zugehöriger Replay fehlten. Dieser konkrete Quellenstand hat sich geändert. Der neue Checkerhash be72c728e128ae0ef605980a5bae88ea31049e29e2fd17c43167fbd6ad1d0c89 passt jetzt zum Ergebnis; auch der Common-Hash stimmt. Die vorhandenen normalen und optimierten Normausgaben sind byteidentisch. Der gespeicherte JSON-I

## 2. −1,138 ist eine echte bessere Variationsgrenze

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:100-170](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L100) · `section:865c0a43e38007bd1d69` · subsection

Die Unterräume aus den normierten bosonweise geordneten Vektoren [formula in source] sind nicht invariant, aber sie sind gültige Variationsräume. Da unterschiedliche k orthogonal sind und H die Bosonzahl höchstens um eins ändert, besitzt die Kompression auf v0, ,v5 exakt

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)

## 3. Der Text vermischt drei verschiedene Näherungszustände

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:171-236](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L171) · `section:8a924ef8eba766c36438` · subsection

Die neuen kleinen Matrizen wurden unabhängig diagonalisiert. Sie bestätigen die gespeicherten numerischen Ritz-Erwartungswerte, aber nicht deren Umdeutung zu exakten Eigenschaften von Ω.

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## Die mittleren Antwortenergien lassen sich ohne riesige Zustandsdateien korrigieren

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:237-276](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L237) · `section:ec3804e1a8260dcf8442` · subsubsection

Aus den CAR folgen für jeden normierten G-Singulettzustand mit N=64:

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py#L1) · explicit_file_citation

## 4. Was bereits überholt ist

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:277-323](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L277) · `section:38c5fefe918ee0afdd3b` · subsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage der Anlage & Prüfung \\ Clock sei ein äußerer Handgriff, weil er Gewichte verschiebt & Bereits in v1.6.6/7 durch das explizite Spin(10)-Wort widerlegt. Nichtskalare Wirkung innerhalb eines Irreps bedeutet keine äußere Symmetrie. Die aktuelle Mechanismusprüfung reproduziert zudem den ursprünglichen Clock und seinen passiven Focklift. \\ Mit allen gewährten inneren Kon

## 5. Was daran spannend ist und was als nächstes trägt

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:324-340](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L324) · `section:c8886a87174ed386526d` · subsection

Der gute neue Schritt ist die tatsächlich abgeschlossene fünfte Spurnetzwerk-Norm mit der daraus folgenden stärkeren strengen Energie- und Entnahmeschranke. Hinzu kommt unsere kleine CAR-Auswertung, die die geladenen ersten Momente auf den richtigen größeren Ritz-Zustand hebt. Das verbessert nachprüfbar die Rechnung im bestehenden nativen Modell.
