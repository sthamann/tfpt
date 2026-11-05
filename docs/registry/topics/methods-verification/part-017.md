# Verification, formalization and safeguards — part 17

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## The honest open-items list

[universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13559-13627](../../../../universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13559) · `section:91c49cb4658c6aa96d2e` · section

This is the complete current ledger of what is not fully closed, graded by how hard the gap is.

Explicit source references:

- [verification/v69_d4_q_geometry.py](../../../../verification/v69_d4_q_geometry.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_file_citation
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *) checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}", Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]]; checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}", Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} && Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]]; (* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L329)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)

## The [formula in source] -slice scan: results (honest hit / miss)

[universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13628-13677](../../../../universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13628) · `section:249af0249acc6b597589` · section

All seven maximal slices of [formula in source] were scanned for the unassigned quantities. The rule was a meaningful (low-complexity) compiler/slice expression matching to [formula in source] ; matches that need a free fitted factor are reported as misses.

## Following the [formula in source] lead: cross-slice consistency

[universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13678-13715](../../../../universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13678) · `section:b547edb029042b679371` · section

The one scan lead worth following is [formula in source] . Splitting [formula in source] the [formula in source] branching [formula in source] decomposes exactly as:

## Appendix: computational verification

[universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13716-13731](../../../../universal_room/new-3/TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13716) · `section:a0a7cfd8f61d9f4bd72e` · section

The audit/bridge identities of this document (marked , ) are re-derived from [formula in source] and machine-checked by the suite in the repository folder verification/; the inline tags [verification/ [formula in source] ] point to the exact script. Relevant here: v1_e8_glue.py — the [formula in source] glue [formula in source] (load-bearing). v4_flavor_matrix.py — the spectral selector [formula in source] , minors [

Explicit source references:

- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation
- [verification/README.md](../../../../verification/README.md#L1) · explicit_file_citation
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_file_citation
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_file_citation
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## TFPT Verification Catalog

[verification_catalog.tex:1-18](../../../../verification_catalog.tex#L1) · `section:cd2149032c4f50f3c3b2` · frontmatter

TFPT Verification Catalog Source registry edition This reference volume lists the registered verification modules and their stated checks. It is generated from the script registry. A row or a passing finite check is not a proof of the complete physical theory. Claim status and scope remain governed by verification/status_ledger.csv and original sources. The reading guide, research contracts and dated publication hist

Explicit source references:

- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation

