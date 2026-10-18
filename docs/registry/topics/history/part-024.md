# Archives and dated records — part 24

[Topic entry](../history.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## 2026-06-18 (4D QFT: the perturbative S-matrix as an Epstein–Glaser / pAQFT skeleton, v269)

[documents/changelog/sections/018-source.tex:120-134](../../../../documents/changelog/sections/018-source.tex#L120) · `section:783bd9d3f50606edb09c` · subsection

v269_spert_paqft_skeleton.py ( QFT4D.SPERT.01) builds the honest middle layer of the three-layer S-matrix (the first concrete 4D-QFT step beyond the spectral-action contract), not a nonperturbative closure. \ three distinct layers: [formula in source] (2d DHR braiding [formula in source] , statistics, v243), [formula in source] (4d Epstein–Glaser/BV S-matrix of the spectral action), [formula in source] (LSZ on the OS

Explicit source references:

- [verification/v243_haag_ruelle_braiding.py](../../../../verification/v243_haag_ruelle_braiding.py#L1) · explicit_script_identifier
- [verification/v265_qft4d_fork_freeze.py](../../../../verification/v265_qft4d_fork_freeze.py#L1) · explicit_script_identifier
- [QFT4D.SPERT.01](../../../../verification/status_ledger.csv#L362) · explicit_claim_identifier · original status at linked ledger row
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_file_citation
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v240_gns_os_reconstruction.py](../../../../verification/v240_gns_os_reconstruction.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)

## 2026-06-18 (PMNS: the reactor-angle exponent closed as the carrier hypercharge trace, v268)

[documents/changelog/sections/018-source.tex:135-147](../../../../documents/changelog/sections/018-source.tex#L135) · `section:45ee2b4ea60ec1f17add` · subsection

v268_theta13_carrier_trace.py ( FLAV.TH13.01) closes the [formula in source] exponent origin. The value [formula in source] was already checked ( v16); now the exponent is exact: \ [formula in source] , the carrier hypercharge-squared trace ( [formula in source] , roots of [formula in source] ; complement [formula in source] the neutrino ratio). \ own channel: the [formula in source] -breaking [formula in source] ind

Explicit source references:

- [FLAV.TH13.01](../../../../verification/status_ledger.csv#L361) · explicit_claim_identifier · original status at linked ledger row
- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_script_identifier
- [verification/v268_theta13_carrier_trace.py](../../../../verification/v268_theta13_carrier_trace.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)

## 2026-06-18 (Infrastructure: a generated causal ``script atlas'' so the suite is navigable at a glance)

[documents/changelog/sections/018-source.tex:148-159](../../../../documents/changelog/sections/018-source.tex#L148) · `section:deafd744d15047be1d98` · subsection

verification/make_script_atlas.py generates verification/script_atlas.md — a single grouped, dependency-aware view fusing the existing single sources ( status_ledger.csv for claim [formula in source] status [formula in source] dependencies [formula in source] supersedes, script_registry.csv/ script_clusters.csv for the theme grouping, docs_map.csv for where each script is cited). It lists every registered script by c

Explicit source references:

- [verification/make_script_atlas.py](../../../../verification/make_script_atlas.py#L1) · explicit_file_citation
- [verification/script_atlas.md](../../../../verification/script_atlas.md#L1) · explicit_file_citation
- [verification/script_clusters.csv](../../../../verification/script_clusters.csv#L1) · explicit_file_citation
- [verification/script_registry.csv](../../../../verification/script_registry.csv#L1) · explicit_file_citation
- [verification/docs_map.csv](../../../../verification/docs_map.csv#L1) · explicit_file_citation
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation

## 2026-06-18 (The bedrock in its minimal-axiom form: a rigidity theorem for QGEO.SYM.01, v267)

[documents/changelog/sections/018-source.tex:160-175](../../../../documents/changelog/sections/018-source.tex#L160) · `section:d22159cf08f411c39c54` · subsection

v267_qgeo_rigidity_minimal_axiom.py ( QGEO.SYM.02) sharpens the one bedrock postulate to its irreducible kernel (it does not close it). \ the single bare statement ``the seam admits the carrier order- [formula in source] clock as a conformal symmetry permuting its four marks'' ( [formula in source] ) forces everything: an order- [formula in source] M\"obius orbit [formula in source] has cross-ratio [formula in source

Explicit source references:

- [verification/v267_qgeo_rigidity_minimal_axiom.py](../../../../verification/v267_qgeo_rigidity_minimal_axiom.py#L1) · explicit_file_citation
- [QGEO.SYM.02](../../../../verification/status_ledger.csv#L360) · explicit_claim_identifier · original status at linked ledger row
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_script_identifier
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v264_raw_seam_marklocal.py](../../../../verification/v264_raw_seam_marklocal.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)

## 2026-06-18 (Branch B decided: the explicit PS threshold model [formula in source] proton-decay window — minimal content killed, [formula in source] survives, Hyper-K decisive, v266)

[documents/changelog/sections/018-source.tex:176-190](../../../../documents/changelog/sections/018-source.tex#L176) · `section:b71b41b72f667ab87708` · subsection

v266_ps_threshold_proton.py ( PS.PROTON.02/ PS.THRESHOLD.02) decides branch B of the v265 fork. The explicit two-step Pati–Salam thresholds give [formula in source] [formula in source] (writes ps_threshold_proton.json): \ the minimal [formula in source] -Higgs content ( [formula in source] ) gives [formula in source] yr [formula in source] Super-K and is killed even at the high hadronic band; \ the [formula in source

Explicit source references:

- [PS.THRESHOLD.02](../../../../verification/status_ledger.csv#L358) · explicit_claim_identifier · original status at linked ledger row
- [verification/v266_ps_threshold_proton.py](../../../../verification/v266_ps_threshold_proton.py#L1) · explicit_file_citation
- [verification/v247_e8_branching_no126.py](../../../../verification/v247_e8_branching_no126.py#L1) · explicit_script_identifier
- [verification/ps_threshold_proton.json](../../../../verification/ps_threshold_proton.json#L1) · explicit_file_citation
- [PS.PROTON.02](../../../../verification/status_ledger.csv#L359) · explicit_claim_identifier · original status at linked ledger row
- [verification/v265_qft4d_fork_freeze.py](../../../../verification/v265_qft4d_fork_freeze.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)

## 2026-06-18 (The 4D-QFT fork frozen as a branch policy: boundary-only canonical, Pati–Salam a falsifiable UV branch, SM-only GUT killed, v265)

[documents/changelog/sections/018-source.tex:191-208](../../../../documents/changelog/sections/018-source.tex#L191) · `section:0e1e7c50a8be56e30768` · subsection

v265_qft4d_fork_freeze.py ( QFT4D.FORK.01) turns the 4D-QFT fork from an open ambiguity into a frozen decision tree ( qft4d_fork_freeze.json), no new physics. A (canonical): boundary-only is the default 4D reading — a 4D-GUT is not claimed by default ( [formula in source] is the audit hull). \ SM-only 4D-GUT unification is killed (1-loop: at the [formula in source] scale [formula in source] off by [formula in source]

Explicit source references:

- [verification/v253_kappa_scalaron_ps.py](../../../../verification/v253_kappa_scalaron_ps.py#L1) · explicit_script_identifier
- [verification/v265_qft4d_fork_freeze.py](../../../../verification/v265_qft4d_fork_freeze.py#L1) · explicit_script_identifier
- [verification/v249_ps_unification.py](../../../../verification/v249_ps_unification.py#L1) · explicit_script_identifier
- [QFT4D.BOUNDARY.DEFAULT.01](../../../../verification/status_ledger.csv#L352) · explicit_claim_identifier · original status at linked ledger row
- [verification/v247_e8_branching_no126.py](../../../../verification/v247_e8_branching_no126.py#L1) · explicit_script_identifier
- [PS.THRESHOLD.01](../../../../verification/status_ledger.csv#L355) · explicit_claim_identifier · original status at linked ledger row
- [PS.UVBRANCH.01](../../../../verification/status_ledger.csv#L354) · explicit_claim_identifier · original status at linked ledger row
- [PS.PROTON.KILL.01](../../../../verification/status_ledger.csv#L356) · explicit_claim_identifier · original status at linked ledger row
- [verification/qft4d_fork_freeze.json](../../../../verification/qft4d_fork_freeze.json#L1) · explicit_file_citation
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [QFT4D.FORK.01](../../../../verification/status_ledger.csv#L351) · explicit_claim_identifier · original status at linked ledger row
- [verification/v248_ps_algebra.py](../../../../verification/v248_ps_algebra.py#L1) · explicit_script_identifier
- [QFT4D.NO_OVERCLAIM.01](../../../../verification/status_ledger.csv#L357) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.SMONLYGUT.01](../../../../verification/status_ledger.csv#L353) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)

## 2026-06-18 (Three open-residual advances: the [formula in source] solver, [formula in source] from [formula in source] , and the raw-seam [formula in source] mark-locality reduction, v262– v264)

[documents/changelog/sections/018-source.tex:209-235](../../../../documents/changelog/sections/018-source.tex#L209) · `section:4a3638ac1b45d771412e` · subsection

v262_fqcd_mp_me.py ( FR.MPME.02) implements the one contract-only [formula in source] pipeline. A real two-loop [formula in source] solver runs [formula in source] with [formula in source] thresholds (carrier [formula in source] , ) to [formula in source] and [formula in source] \,GeV; with the lattice bridge [formula in source] (external [formula in source] ) and the closed [formula in source] it reproduces [formula

Explicit source references:

- [verification/v262_fqcd_mp_me.py](../../../../verification/v262_fqcd_mp_me.py#L1) · explicit_script_identifier
- [FR.MPME.01](../../../../verification/status_ledger.csv#L49) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_script_identifier
- [verification/v264_raw_seam_marklocal.py](../../../../verification/v264_raw_seam_marklocal.py#L1) · explicit_file_citation
- [FR.MPME.02](../../../../verification/status_ledger.csv#L348) · explicit_claim_identifier · original status at linked ledger row
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v231_cp_mu6_phases.py](../../../../verification/v231_cp_mu6_phases.py#L1) · explicit_script_identifier
- [QGEO.ENERGY.03](../../../../verification/status_ledger.csv#L350) · explicit_claim_identifier · original status at linked ledger row
- [verification/v233_cp_triality_phase.py](../../../../verification/v233_cp_triality_phase.py#L1) · explicit_script_identifier
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [verification/v263_mnu_from_df.py](../../../../verification/v263_mnu_from_df.py#L1) · explicit_file_citation
- [FLAV.PMNS.02](../../../../verification/status_ledger.csv#L349) · explicit_claim_identifier · original status at linked ledger row
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* v225 dual normal frame (d,n) and oriented volume *) d = av.Inverse[RRm]; nvec = {5, -9, 6}; KKm = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Lm = KKm + QQm; checkExact["v225 DUAL.FRAME.01: d=a.R^{-1}=(-1/2,-1/2,1)=-1/2(1,1,-2) (Nariai normal; " <> "d.1=0, d.a=1); n=(5,-9,6) with n.R=(det R,0,0)=(8,0,0), n.L=(det L,0,0)=(20,0,0); " <> "oriented volume det(1,d,n)=21=N_fam*scalaron=3*7", d == {-1/2, -1/2, 1} && d == -1/2 {1, 1, -2} && d.one == 0 && d.av == 1 && nvec.RRm == {Det[RRm], 0, 0} == {8, 0, 0} && nvec.Lm == {Det[Lm], 0, 0} == {20, 0, 0} && Det[{{1, 1, 1}, d, nvec}] == 21 == 3*7]; ]; (* ==== v231: both CP phases are mu6 powers of one hexagonal unit, split by the sheet ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1861)

## 2026-06-18 (Paper consistency pass: the closure ledger and the status/QFT sections updated for the Modular Spectral Closure, with an explicit ``what is not closed'' line)

[documents/changelog/sections/018-source.tex:236-254](../../../../documents/changelog/sections/018-source.tex#L236) · `section:817ba5dfc4c0aadf9e21` · subsection

Five paper sections that predated the v238– v261 round are brought up to date (additive, no status marker moved). The introduction closure-ledger table and the ``five questions'' item now carry a boundary QFT (Modular Spectral Closure) row — one relative object [formula in source] closed modulo QGEO.SYM.01 ( v258– v261) — plus an explicit list of what the closure does not reach: the full measured pole masses, the abs

Explicit source references:

- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [verification/v261_modular_spectral_closure.py](../../../../verification/v261_modular_spectral_closure.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v238_modular_lindblad_dynamics.py](../../../../verification/v238_modular_lindblad_dynamics.py#L1) · explicit_script_identifier
- [verification/v258_dirac_covariance_induction.py](../../../../verification/v258_dirac_covariance_induction.py#L1) · explicit_script_identifier
- [verification/v255_spectral_action_expansion.py](../../../../verification/v255_spectral_action_expansion.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)

## 2026-06-18 (Consistency pass: the Modular Spectral Closure surfaced structurally across the website and the intro status card)

[documents/changelog/sections/018-source.tex:255-267](../../../../documents/changelog/sections/018-source.tex#L255) · `section:fe4822aaeee66083bf56` · subsection

The v258– v261 closure is now reflected on every ``what is open'' surface, not just the research-contracts paper. The homepage open-gates section and compiler-pipeline diagram, the hostile-referee FAQ, the glossary [formula in source] entry, the reviewer page and the verification residual-chain caption now state that the entire emergent-QFT layer (Dirac, cutoff, gauging, glue, orientability) collapses onto the same p

Explicit source references:

- [verification/v258_dirac_covariance_induction.py](../../../../verification/v258_dirac_covariance_induction.py#L1) · explicit_script_identifier
- [verification/v261_modular_spectral_closure.py](../../../../verification/v261_modular_spectral_closure.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)

## 2026-06-17 (The Modular Spectral Closure: Dirac as covariance induction, the modular cutoff, the Kummer/K3 unification, and the assembly certificate, v258– v261)

[documents/changelog/sections/018-source.tex:268-310](../../../../documents/changelog/sections/018-source.tex#L268) · `section:ca7f6aced60b17ae6709` · subsection

v258_dirac_covariance_induction.py ( PS.DIRAC.03) closes the ``posited Yukawa vs derived operator'' gap of v250/ v252. The finite Dirac operator [formula in source] is the modular/covariance induction of the boundary seam quasi-free (KMS, [formula in source] ) state: a Gaussian state is fixed by its covariance [formula in source] (a positive contraction) with one-particle modular Hamiltonian [formula in source] (Arak

Explicit source references:

- [verification/v260_k3_kummer_unification.py](../../../../verification/v260_k3_kummer_unification.py#L1) · explicit_file_citation
- [verification/v239_kms_thermal_time.py](../../../../verification/v239_kms_thermal_time.py#L1) · explicit_script_identifier
- [PS.SPECACT.02](../../../../verification/status_ledger.csv#L345) · explicit_claim_identifier · original status at linked ledger row
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [PS.DIRAC.03](../../../../verification/status_ledger.csv#L344) · explicit_claim_identifier · original status at linked ledger row
- [verification/v261_modular_spectral_closure.py](../../../../verification/v261_modular_spectral_closure.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v252_full_finite_triple.py](../../../../verification/v252_full_finite_triple.py#L1) · explicit_script_identifier
- [verification/v232_e8_kleinian_seam.py](../../../../verification/v232_e8_kleinian_seam.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v18_quark_yukawa.py](../../../../verification/v18_quark_yukawa.py#L1) · explicit_script_identifier
- [verification/v197_rr_carrier_clifford_d5.py](../../../../verification/v197_rr_carrier_clifford_d5.py#L1) · explicit_script_identifier
- [verification/v253_kappa_scalaron_ps.py](../../../../verification/v253_kappa_scalaron_ps.py#L1) · explicit_script_identifier
- [verification/v58_seam_horizon_chain.py](../../../../verification/v58_seam_horizon_chain.py#L1) · explicit_script_identifier
- [verification/v238_modular_lindblad_dynamics.py](../../../../verification/v238_modular_lindblad_dynamics.py#L1) · explicit_script_identifier
- [verification/v255_spectral_action_expansion.py](../../../../verification/v255_spectral_action_expansion.py#L1) · explicit_script_identifier
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_file_citation
- [verification/v258_dirac_covariance_induction.py](../../../../verification/v258_dirac_covariance_induction.py#L1) · explicit_script_identifier
- [QFT.MSC.01](../../../../verification/status_ledger.csv#L347) · explicit_claim_identifier · original status at linked ledger row
- [verification/v236_brieskorn_capstone.py](../../../../verification/v236_brieskorn_capstone.py#L1) · explicit_script_identifier
- [verification/v250_dirac_triple_contract.py](../../../../verification/v250_dirac_triple_contract.py#L1) · explicit_script_identifier
- [ARCH.K3.01](../../../../verification/status_ledger.csv#L346) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v232: the seam as the E8 Kleinian singularity (du Val resolution + link) ==== *) Module[{labels, e8edges, A8, C8, degs}, labels = {1, 2, 3, 4, 5, 6, 4, 2, 3}; (* affine E8 Kac marks *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1894)
- [(* ---- (v197) ARCH.RRCAR.02: even Clifford of the 5-dim carrier = the D5 half-spinor ---- *) Module[{h0, lamEven}, h0 = 4 + 1; (* h^0(P^1,O(mu4)) = deg+1 = 5 = g_car *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1630)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v57) horizon cross-links: Jacobson 8pi, Hod ln(3), Hawking |W(D5)| ---- *) checkExact["c3=1/(8pi) Einstein/Jacobson: 1/(16pi)=c3/2; 1/4=1/|mu4|; 1/(2pi)=4c3", Simplify[1/(16 Pi) - (1/(8 Pi))/2] == 0 && 1/4 == 1/4 && Simplify[1/(2 Pi) - 4/(8 Pi)] == 0]; checkExact["Hod QNM omega_R/T_H = ln(3) = ln(N_fam); Hawking power denom 1920=|W(D5)|=2^4*5!", Nfam == 3 && 1920 == 2^4 * 5!]; (* ---- (v58) seam-horizon chain: one-sided Gauss-Bonnet, KMS, S_BH, RT in seam units ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L263)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)

## 2026-06-17 (Infrastructure: the changelog is now a public website page, generated from changelog.tex and audit-gated)

[documents/changelog/sections/018-source.tex:311-328](../../../../documents/changelog/sections/018-source.tex#L311) · `section:872460c09bc51af94bc3` · subsection

The canonical changelog now also drives a public /changelog website page. A new generator verification/make_changelog_web.py parses this file (dated subsection* entries, itemize items, and the inline markup textbf/ emph/ texttt/ vref, the status markers / / / , inline math and accents) into the typed data file website/ lib/ changelog.ts, rendered server-side (math via KaTeX) by website/ app/ changelog/ page.tsx [form

Explicit source references:

- [verification/make_changelog_web.py](../../../../verification/make_changelog_web.py#L1) · explicit_file_citation
- [verification/audit_sync.py](../../../../verification/audit_sync.py#L1) · explicit_file_citation

## 2026-06-17 (Orientability + Poincar\'e duality: the honest, literature-confirmed status — strict fail, weakened hold, v257)

[documents/changelog/sections/018-source.tex:329-344](../../../../documents/changelog/sections/018-source.tex#L329) · `section:ac9cd242068b80a2c433` · subsection

v257_quasiorient_modpd.py ( PS.NCG.ORIENT.02) corrects the slightly too-generous v256 typing. The published result (Cacic–Stephan arXiv:0902.2068; CCM07; SM-vacuum hep-th/0601192) is that the Chamseddine–Connes–Marcolli Standard-Model finite triple (KO-dimension [formula in source] , with three right-handed neutrinos — exactly the TFPT seesaw case) genuinely fails strict orientability and strict Poincar\'e duality, a

Explicit source references:

- [verification/v256_orientability_poincare.py](../../../../verification/v256_orientability_poincare.py#L1) · explicit_script_identifier
- [verification/v257_quasiorient_modpd.py](../../../../verification/v257_quasiorient_modpd.py#L1) · explicit_file_citation
- [verification/v252_full_finite_triple.py](../../../../verification/v252_full_finite_triple.py#L1) · explicit_script_identifier
- [PS.NCG.ORIENT.02](../../../../verification/status_ledger.csv#L343) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-17 (Remaining NCG obligations discharged or honestly typed: inner fluctuations, spectral action, orientability/Poincar\'e, v254– v256)

[documents/changelog/sections/018-source.tex:345-368](../../../../documents/changelog/sections/018-source.tex#L345) · `section:1874fb8cb69b4a8cffd0` · subsection

v254_inner_fluctuations.py ( PS.NCG.FLUCT.01) closes v250 \#5 + the no-junk obligation. The inner fluctuations [formula in source] of the finite Dirac operator are computed explicitly: \ they are purely chirality-odd (scalars), and for the SM algebra sit exactly in the one Higgs doublet [formula in source] — no junk, no triplet, no [formula in source] . \ the [formula in source] ( [formula in source] Majorana) direct

Explicit source references:

- [verification/v255_spectral_action_expansion.py](../../../../verification/v255_spectral_action_expansion.py#L1) · explicit_file_citation
- [PS.NCG.FLUCT.01](../../../../verification/status_ledger.csv#L340) · explicit_claim_identifier · original status at linked ledger row
- [verification/v254_inner_fluctuations.py](../../../../verification/v254_inner_fluctuations.py#L1) · explicit_script_identifier
- [PS.SPECACT.01](../../../../verification/status_ledger.csv#L341) · explicit_claim_identifier · original status at linked ledger row
- [verification/v252_full_finite_triple.py](../../../../verification/v252_full_finite_triple.py#L1) · explicit_script_identifier
- [PS.NCG.ORIENT.01](../../../../verification/status_ledger.csv#L342) · explicit_claim_identifier · original status at linked ledger row
- [verification/v256_orientability_poincare.py](../../../../verification/v256_orientability_poincare.py#L1) · explicit_file_citation
- [verification/v250_dirac_triple_contract.py](../../../../verification/v250_dirac_triple_contract.py#L1) · explicit_script_identifier

## 2026-06-17 (Full [formula in source] -dim finite spectral triple built + NCG axioms verified, and [formula in source] pinned to [formula in source] , v252– v253)

[documents/changelog/sections/019-source.tex:1-20](../../../../documents/changelog/sections/019-source.tex#L1) · `section:84cdd8694056da4b7ff6` · subsection

v252_full_finite_triple.py ( PS.DIRAC.02) advances the Dirac contract v250 from a [formula in source] -obligation contract to a concrete object discharging [formula in source] to . The full [formula in source] -dim finite spectral triple [formula in source] — [formula in source] the particle [formula in source] antiparticle doubling of three [formula in source] [formula in source] -plets — is built explicitly and the

Explicit source references:

- [verification/v250_dirac_triple_contract.py](../../../../verification/v250_dirac_triple_contract.py#L1) · explicit_script_identifier
- [verification/v252_full_finite_triple.py](../../../../verification/v252_full_finite_triple.py#L1) · explicit_file_citation
- [verification/v249_ps_unification.py](../../../../verification/v249_ps_unification.py#L1) · explicit_script_identifier
- [verification/v253_kappa_scalaron_ps.py](../../../../verification/v253_kappa_scalaron_ps.py#L1) · explicit_file_citation
- [PS.KAPPA.01](../../../../verification/status_ledger.csv#L339) · explicit_claim_identifier · original status at linked ledger row
- [PS.DIRAC.02](../../../../verification/status_ledger.csv#L338) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-17 (Spectral triple, first step: the first-order condition is violated exactly by the Majorana/ [formula in source] — the CCvS Pati–Salam mechanism, v251)

[documents/changelog/sections/019-source.tex:21-33](../../../../documents/changelog/sections/019-source.tex#L21) · `section:87dd9044f8c1cc589655` · subsection

v251_first_order_sigma.py ( PS.DIRAC.01) advances the Dirac contract v250 from a contract to an exhibited mechanism. On a faithful lepton-block model ( [formula in source] , [formula in source] ), the real even structure is checked ( [formula in source] , [formula in source] , [formula in source] , KO-dim-6 signs), order-zero holds, the first-order condition HOLDS for the Yukawa block, and is VIOLATED exactly by the 

Explicit source references:

- [verification/v251_first_order_sigma.py](../../../../verification/v251_first_order_sigma.py#L1) · explicit_script_identifier
- [verification/v249_ps_unification.py](../../../../verification/v249_ps_unification.py#L1) · explicit_script_identifier
- [PS.DIRAC.01](../../../../verification/status_ledger.csv#L337) · explicit_claim_identifier · original status at linked ledger row
- [verification/v250_dirac_triple_contract.py](../../../../verification/v250_dirac_triple_contract.py#L1) · explicit_script_identifier

## 2026-06-17 (Carrier-native Pati–Salam program: [formula in source] forbids the 126, PS algebra, unification kill-test, Dirac contract, v247– v250)

[documents/changelog/sections/019-source.tex:34-51](../../../../documents/changelog/sections/019-source.tex#L34) · `section:016e3070914a0c328c63` · subsection

Four scripts turning the gauge-unification finding into typed claims with negative controls. v247_e8_branching_no126.py ( PS.E8BRANCH.01): the [formula in source] hull branches under [formula in source] as [formula in source] , so the [formula in source] content is exactly [formula in source] and the [formula in source] is absent — the renormalisable [formula in source] is algebraically forbidden and [formula in sour

Explicit source references:

- [verification/v249_ps_unification.py](../../../../verification/v249_ps_unification.py#L1) · explicit_file_citation
- [verification/v250_dirac_triple_contract.py](../../../../verification/v250_dirac_triple_contract.py#L1) · explicit_script_identifier
- [verification/v247_e8_branching_no126.py](../../../../verification/v247_e8_branching_no126.py#L1) · explicit_file_citation
- [PS.E8BRANCH.01](../../../../verification/status_ledger.csv#L333) · explicit_claim_identifier · original status at linked ledger row
- [PS.RGTEST.01](../../../../verification/status_ledger.csv#L335) · explicit_claim_identifier · original status at linked ledger row
- [PS.ALGEBRA.01](../../../../verification/status_ledger.csv#L334) · explicit_claim_identifier · original status at linked ledger row
- [verification/v248_ps_algebra.py](../../../../verification/v248_ps_algebra.py#L1) · explicit_file_citation
- [CONTRACT.QFT4D.DIRAC.01](../../../../verification/status_ledger.csv#L336) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-17 (Honest data cross-check + emergent-QFT figures: the unification tension, v246)

[documents/changelog/sections/019-source.tex:52-68](../../../../documents/changelog/sections/019-source.tex#L52) · `section:a47d96c6748aecfb0de9` · subsection

v246_unification_data_crosscheck.py ( QFT4D.RGTEST.01) — the first hard data confrontation of the spectral-action prediction. TFPT's gauge-charged content is the Standard Model ( v159) and the theory adds no new states; the [formula in source] cascade is an arithmetic spine ( v5), not a threshold tower. So the run is the SM run: at one loop the couplings spread [formula in source] – [formula in source] \,GeV (residua

Explicit source references:

- [verification/make_figures.py](../../../../verification/make_figures.py#L1) · explicit_file_citation
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_script_identifier
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [QFT4D.RGTEST.01](../../../../verification/status_ledger.csv#L332) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)

## 2026-06-17 (Spectral-action matter content: the [formula in source] 16 [formula in source] one anomaly-free SM generation, v245)

[documents/changelog/sections/019-source.tex:69-85](../../../../documents/changelog/sections/019-source.tex#L69) · `section:d0aef4f5062824e2d6c2` · subsection

v245_spectral_matter_content.py ( QFT4D.MATTER.01) discharges the computable core of the 4d contract v244. The carrier half-spinor (the [formula in source] 16) is verified, in exact rational arithmetic, to be one Standard-Model generation: [formula in source] , the SM multiplet dimensions sum to [formula in source] ( [formula in source] Weyl fermions [formula in source] ), the electric charges [formula in source] are

Explicit source references:

- [verification/v245_spectral_matter_content.py](../../../../verification/v245_spectral_matter_content.py#L1) · explicit_script_identifier
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [CONTRACT.QFT4D.01](../../../../verification/status_ledger.csv#L330) · explicit_claim_identifier · original status at linked ledger row
- [verification/v244_spectral_action_contract.py](../../../../verification/v244_spectral_action_contract.py#L1) · explicit_script_identifier
- [QFT4D.MATTER.01](../../../../verification/status_ledger.csv#L331) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-17 (The static [formula in source] dynamic flip: modular flow [formula in source] a recovery Lindblad generator, v238)

[documents/changelog/sections/019-source.tex:86-105](../../../../documents/changelog/sections/019-source.tex#L86) · `section:9f084ccace7baa00bf8d` · subsection

New v238_modular_lindblad_dynamics.py ( DYN.SEMIGROUP.01, cluster registry). A companion to the modular round ( v196/ v198) and the recovery code ( v221/ v64) that reads the same seam objects dynamically rather than statically. \ the modular flow [formula in source] is a unitary one-parameter group (Tomita–Takesaki) whose conservation of the [formula in source] clock, [formula in source] , IS the v198 state-invarianc

Explicit source references:

- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [DYN.SEMIGROUP.01](../../../../verification/status_ledger.csv#L324) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v196_seam_energy_functional.py](../../../../verification/v196_seam_energy_functional.py#L1) · explicit_script_identifier
- [verification/v64_causal_boundary_nogo.py](../../../../verification/v64_causal_boundary_nogo.py#L1) · explicit_script_identifier
- [verification/v238_modular_lindblad_dynamics.py](../../../../verification/v238_modular_lindblad_dynamics.py#L1) · explicit_file_citation
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_script_identifier
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation
- [verification/script_registry.csv](../../../../verification/script_registry.csv#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [(* v100_numerology_null_mc.py is Python-only by design: it is a STATISTICAL module (exact integer census of a declared formula grammar + deterministic Monte-Carlo pseudo-theories + RNG-seeded negative controls + 94500 float root-solves), not an exact algebraic identity -- same convention as the Python-only v62/v64/v65. No Wolfram mirror is required; flagged in README.md and ledger GATE.WOLFRAM.02. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L326)
- [(* ---- (v196) QGEO.VARI.01: E_fail = 0 on the mu4 block (exact finite vanishing) ---- *) Module[{rho, Lam, comm, order4, twist}, rho = DiagonalMatrix[{I, -1, -I}]; Lam = DiagonalMatrix[{1, 2, 3}]; (* any real diagonal (mu4-equivariant) DtN *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1619)

## 2026-06-17 (Red-team layer re-synced to the paper; shadow export mirrors figures/)

[documents/changelog/sections/019-source.tex:106-125](../../../../documents/changelog/sections/019-source.tex#L106) · `section:c004d2ee68ddeaaf26ff` · subsection

Red Team Target A re-synced to tfpt_5_redteam ( rt_A_e8net.py, redteam_table.txt, redteam/README.md, infrastructure). The Python red-team surface still emitted the historical three-residual ``A reduced, not closed'' form, lagging the reader-facing note. It now encodes the sharper narrowing already in the paper: the residual collapses to the single statement ``the seam–Calder\'on boundary net is holomorphic with [form

Explicit source references:

- [verification/v152_norm_is_anchor.py](../../../../verification/v152_norm_is_anchor.py#L1) · explicit_script_identifier
- [verification/make_script_index.py](../../../../verification/make_script_index.py#L1) · explicit_file_citation
- [verification/v143_graded_frobenius.py](../../../../verification/v143_graded_frobenius.py#L1) · explicit_script_identifier
- [verification/redteam/redteam_table.txt](../../../../verification/redteam/redteam_table.txt#L1) · explicit_file_citation
- [verification/redteam/README.md](../../../../verification/redteam/README.md#L1) · explicit_file_citation
- [verification/redteam/rt_A_e8net.py](../../../../verification/redteam/rt_A_e8net.py#L1) · explicit_file_citation
- [verification/make_manifest.py](../../../../verification/make_manifest.py#L1) · explicit_file_citation
- [verification/v148_fock_census.py](../../../../verification/v148_fock_census.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v205) GRAV.XI.01: xi = c3/phi_tree = 3/4, the independent gravitational 3/4 ---- *) Module[{c3, phitree}, c3 = 1/(8 Pi); phitree = 1/(6 Pi); checkExact["v205 GRAV.XI.01: the torsion-compression factor xi = c3/phi_tree = (1/8pi)/(1/6pi) = 3/4 EXACTLY; the Einstein-limit reduction 8 pi c3^2 = c3 makes G an output (xi = c3/phi0); and 3/4 = 12 pi (c3/2) = ln(m/mu) = q(A3) (v152) -- the torsion-compression and the gapped EH replica are two independent appearances of the same gravitational 3/4", Simplify[c3/phitree - 3/4] == 0 && Simplify[8 Pi c3^2 - c3] == 0 && Simplify[12 Pi (c3/2) - 3/4] == 0]; ]; (* ---- (v208) HOR.BHTHERMO.01: scalaron Wald factor + modular 2 pi = 1/(4 c3) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1708)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v148) NS/R sector census (corrected) ---- *) Module[{nsClasses, rCounts, glueA, glueB, inA, inB}, nsClasses = Union[Flatten[Table[ {2 Mod[Total[v], 2], 2 Mod[Total[w], 2]}, {v, Tuples[Range[-1, 1], 5]}, {w, Tuples[Range[-1, 1], 3]}], 1]]; rCounts = <||>; Do[Module[{qd = If[EvenQ[Count[s5, -1]], 1, 3]}, Do[Module[{qa = If[EvenQ[Count[s3, -1]], 1, 3]}, rCounts[{qd, qa}] = Lookup[rCounts, Key[{qd, qa}], 0] + 1], {s3, Tuples[{1, -1}, 3]}]], {s5, Tuples[{1, -1}, 5]}]; glueA = {{0, 0}, {1, 1}, {2, 2}, {3, 3}}; glueB = {{0, 0}, {1, 3}, {2, 2}, {3, 1}}; inA = Total[Lookup[rCounts, Key[#], 0] & /@ glueA]; inB = Total[Lookup[rCounts, Key[#], 0] & /@ glueB]; checkExact["v148 NS/R census (corrected): NS supports only even classes {(0,0),(2,0),(0,2),(2,2)} (integer weights); R zero-mode module = four odd pairs of 64; R splits 128+128 into the odd sectors of the two Lagrangian glues; 248 = 120 NS + 128 R", Sort[nsClasses] == Sort[{{0, 0}, {2, 0}, {0, 2}, {2, 2}}] && ! MemberQ[nsClasses, {1, 1}] && ! MemberQ[nsClasses, {3, 3}] && Values[KeySort[rCounts]] == {64, 64, 64, 64} && Total[Values[rCounts]] == 256 && inA == 128 && inB == 128 && 120 + 128 == 248]; ]; (* ---- (v149) cusp normal ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1280)
- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)

## 2026-06-17 (CP phases as [formula in source] powers — a reduction of red-team Target D)

[documents/changelog/sections/019-source.tex:126-196](../../../../documents/changelog/sections/019-source.tex#L126) · `section:05558e866dc724bc0fcb` · subsection

Both CP phases are [formula in source] powers of one hexagonal CM unit, split by the sheet ( v231_cp_mu6_phases, tfpt_5_redteam, / ). Sharper than v220/ v225 (which only located the CP residual). With [formula in source] the primitive [formula in source] th root (the [formula in source] Eisenstein CM unit): [formula in source] leading [formula in source] (quark) and [formula in source] (lepton, the phase lattice), wi

Explicit source references:

- [CP.TRIALITY.01](../../../../verification/status_ledger.csv#L319) · explicit_claim_identifier · original status at linked ledger row
- [verification/v233_cp_triality_phase.py](../../../../verification/v233_cp_triality_phase.py#L1) · explicit_script_identifier
- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier
- [TOPO.BRIESKORN.01](../../../../verification/status_ledger.csv#L322) · explicit_claim_identifier · original status at linked ledger row
- [GATE.HOLO.03](../../../../verification/status_ledger.csv#L323) · explicit_claim_identifier · original status at linked ledger row
- [verification/v232_e8_kleinian_seam.py](../../../../verification/v232_e8_kleinian_seam.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [GATE.HOLO.01](../../../../verification/status_ledger.csv#L320) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v223_coxeter_totative_clock.py](../../../../verification/v223_coxeter_totative_clock.py#L1) · explicit_script_identifier
- [verification/v231_cp_mu6_phases.py](../../../../verification/v231_cp_mu6_phases.py#L1) · explicit_script_identifier
- [CP.MU6.01](../../../../verification/status_ledger.csv#L317) · explicit_claim_identifier · original status at linked ledger row
- [GATE.HOLO.02](../../../../verification/status_ledger.csv#L321) · explicit_claim_identifier · original status at linked ledger row
- [verification/v225_dual_normal_frame.py](../../../../verification/v225_dual_normal_frame.py#L1) · explicit_script_identifier
- [verification/v219_icosahedral_mckay.py](../../../../verification/v219_icosahedral_mckay.py#L1) · explicit_script_identifier
- [TOPO.E8.01](../../../../verification/status_ledger.csv#L318) · explicit_claim_identifier · original status at linked ledger row
- [verification/v220_cp_hexagonal_modulus.py](../../../../verification/v220_cp_hexagonal_modulus.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v223 Coxeter totative clock: (Z/30)^x = E8 exponents, order-4 element 7 *) checkExact["v223 COX.CLOCK.01: (Z/30)^x = {1,7,11,13,17,19,23,29} = E8 exponents, " <> "phi(30)=8=rank E8, 30=2*3*5; mult-by-7 has order 4 (7^2=19, 7^4=1 mod 30): a " <> "mu4 clock <7>={1,7,13,19}; the conjugate pairs split into 4 invariant planes", Select[Range[29], CoprimeQ[#, 30] &] == {1, 7, 11, 13, 17, 19, 23, 29} && EulerPhi[30] == 8 && PowerMod[7, 2, 30] == 19 && PowerMod[7, 4, 30] == 1 && Sort[Mod[7^Range[0, 3], 30]] == {1, 7, 13, 19} && Length[Union[Sort /@ ({#, 30 - #} & /@ {1, 7, 11, 13, 17, 19, 23, 29})]] == 4]; (* v227 degree/exponent channel split: 248 = 120 + 128 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1804)
- [(* v225 dual normal frame (d,n) and oriented volume *) d = av.Inverse[RRm]; nvec = {5, -9, 6}; KKm = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Lm = KKm + QQm; checkExact["v225 DUAL.FRAME.01: d=a.R^{-1}=(-1/2,-1/2,1)=-1/2(1,1,-2) (Nariai normal; " <> "d.1=0, d.a=1); n=(5,-9,6) with n.R=(det R,0,0)=(8,0,0), n.L=(det L,0,0)=(20,0,0); " <> "oriented volume det(1,d,n)=21=N_fam*scalaron=3*7", d == {-1/2, -1/2, 1} && d == -1/2 {1, 1, -2} && d.one == 0 && d.av == 1 && nvec.RRm == {Det[RRm], 0, 0} == {8, 0, 0} && nvec.Lm == {Det[Lm], 0, 0} == {20, 0, 0} && Det[{{1, 1, 1}, d, nvec}] == 21 == 3*7]; ]; (* ==== v231: both CP phases are mu6 powers of one hexagonal unit, split by the sheet ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1861)
- [(* ==== v232: the seam as the E8 Kleinian singularity (du Val resolution + link) ==== *) Module[{labels, e8edges, A8, C8, degs}, labels = {1, 2, 3, 4, 5, 6, 4, 2, 3}; (* affine E8 Kac marks *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1894)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)

## 2026-06-16 (the icosahedral bedrock, CM-norm duality, and a structural-finds round)

[documents/changelog/sections/019-source.tex:197-259](../../../../documents/changelog/sections/019-source.tex#L197) · `section:84a46199f1af35c95044` · subsection

McKay bedrock: why the atoms are [formula in source] ( v219_icosahedral_mckay, origin_theory, ). [formula in source] is the exceptional top of the McKay tower of finite [formula in source] subgroups ( [formula in source] , [formula in source] , [formula in source] ). Built from the group: the [formula in source] unit-quaternion icosians close to the binary icosahedral group [formula in source] (element orders [formul

Explicit source references:

- [MCKAY.E8.01](../../../../verification/status_ledger.csv#L306) · explicit_claim_identifier · original status at linked ledger row
- [E8.CHAN.01](../../../../verification/status_ledger.csv#L309) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.RR.01](../../../../verification/status_ledger.csv#L310) · explicit_claim_identifier · original status at linked ledger row
- [QEC.SEAM.01](../../../../verification/status_ledger.csv#L311) · explicit_claim_identifier · original status at linked ledger row
- [CP.MOD.01](../../../../verification/status_ledger.csv#L312) · explicit_claim_identifier · original status at linked ledger row
- [FTR.PATH.01](../../../../verification/status_ledger.csv#L314) · explicit_claim_identifier · original status at linked ledger row
- [CENTER.NORM.01](../../../../verification/status_ledger.csv#L316) · explicit_claim_identifier · original status at linked ledger row
- [DUAL.FRAME.01](../../../../verification/status_ledger.csv#L313) · explicit_claim_identifier · original status at linked ledger row
- [LEP.FROB.01](../../../../verification/status_ledger.csv#L315) · explicit_claim_identifier · original status at linked ledger row
- [CMNORM.DUAL.01](../../../../verification/status_ledger.csv#L307) · explicit_claim_identifier · original status at linked ledger row
- [COX.CLOCK.01](../../../../verification/status_ledger.csv#L308) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-15 (the diamond axis geometry — two axes + the transfer corner)

[documents/changelog/sections/019-source.tex:260-279](../../../../documents/changelog/sections/019-source.tex#L260) · `section:038ae1c94af71398ea72` · subsection

The Sheet Diamond is a discrete geometry with two axes ( v218_diamond_axis_geometry, tfpt_2_standard_model, ). Sharpens v94/ v95 with three exact \ lemmas (no new numbers). (1) Axis curvature: along the centered cross the determinant is linear on the winding axis [formula in source] (slope [formula in source] ) and quadratic on the sheet axis [formula in source] (2nd difference [formula in source] ); the anchor block

Explicit source references:

- [verification/v95_centered_diamond.py](../../../../verification/v95_centered_diamond.py#L1) · explicit_script_identifier
- [DIAMOND.SPECTRAL.01](../../../../verification/status_ledger.csv#L305) · explicit_claim_identifier · original status at linked ledger row
- [DIAMOND.PLUCKER.01](../../../../verification/status_ledger.csv#L304) · explicit_claim_identifier · original status at linked ledger row
- [DIAMOND.AXIS.01](../../../../verification/status_ledger.csv#L303) · explicit_claim_identifier · original status at linked ledger row
- [verification/v94_sheet_diamond.py](../../../../verification/v94_sheet_diamond.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v95) centered flavor diamond ---- *) Uop = Q.DiagonalMatrix[{1, 0, 0}]; Vop = Q.DiagonalMatrix[{0, 1, 1}]; Cc = R + Uop; Lop = R + 2 Uop; Fop = R + Q; checkExact["v95 centered cross: Q=U+V; R=C-U, L=C+U, K=C-V, F=C+V", (Q == Uop + Vop) && (R == Cc - Uop) && (Lop == Cc + Uop) && (K == Cc - Vop) && (Fop == Cc + Vop)]; checkExact["v95 axes spectra: Spec U = {3,0,0} (winding), Spec V = {0,1,2} = N_fam*cusp", (Sort[Eigenvalues[Uop]] == {0, 0, 3}) && (Sort[Eigenvalues[Vop]] == {0, 1, 2})]; checkExact["v95 center invariants: tr C=12, det C=14, sum C=31=2^g_car-1, det B_C=28", (Tr[Cc] == 12) && (Det[Cc] == 14) && (Total[Cc, 2] == 31) && (31 == 2^gcar - 1) && (Det[bb[Cc]] == 28)]; checkExact["v95 ray alignment: Pi_R(C)=7(2,3,1), Pi_R(L)=10(2,3,1)", (plR[Cc] == 7 {2, 3, 1}) && (plR[Lop] == 10 {2, 3, 1})]; (* ---- (v96) branch-kernel selection (P1) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L204)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [(* ---- (v218) DIAMOND.AXIS/PLUCKER/SPECTRAL.01: the diamond axis geometry ---- *) Module[{R, Q, a, one, Cc, U, V, K, L, F, anc, plL, ram, x, y, dU, dV, bU, bV, sd, bsd, sq, ker}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; one = {1, 1, 1}; a = {1, 1, 2}; Cc = R + Q.DiagonalMatrix[{1, 0, 0}]; (* center C = M(1,0) (v95) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1751)

## 2026-06-15 (QGEO: the four marks emerge from Gauss–Bonnet — K1 executed)

[documents/changelog/sections/019-source.tex:280-299](../../../../documents/changelog/sections/019-source.tex#L280) · `section:640aa248092cb39263eb` · subsection

The four marks emerge from Gauss–Bonnet — count derived, not assumed ( v216_marks_gauss_bonnet, tfpt_research_contracts, ; ledger QGEO.MARKS.03). The K1 lever of the v215 kill-test (``exactly four marks'') is executed: if the marks are [formula in source] branch points (deficit [formula in source] ) on the flat seam sphere ( [formula in source] , the same [formula in source] as the [formula in source] in [formula in 

Explicit source references:

- [QGEO.EMERGE.01](../../../../verification/status_ledger.csv#L277) · explicit_claim_identifier · original status at linked ledger row
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [QGEO.MARKS.03](../../../../verification/status_ledger.csv#L276) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v217_marks_emergence_scan.py](../../../../verification/v217_marks_emergence_scan.py#L1) · explicit_script_identifier
- [verification/v215_seam_deck_killtest.py](../../../../verification/v215_seam_deck_killtest.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)

## 2026-06-15 (QGEO: the bedrock recast as a falsifiable kill-test)

[documents/changelog/sections/019-source.tex:300-319](../../../../documents/changelog/sections/019-source.tex#L300) · `section:12b87d2440c45e44a27e` · subsection

QGEO.SYM.01 as a kill-test, not a proof-promise ( v215_seam_deck_killtest, tfpt_research_contracts, / ; ledger QGEO.KILL.01). A foundational symmetry cannot be derived from nothing (Bisognano–Wichmann would presuppose the covariance it should produce), so the bedrock [formula in source] is recast as four independently-falsifiable predictions about the raw seam DtN. The non-circular reduction ( v198/ v199/ v201) gives

Explicit source references:

- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_script_identifier
- [verification/v199_seam_state_invariance.py](../../../../verification/v199_seam_state_invariance.py#L1) · explicit_script_identifier
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [QGEO.KILL.01](../../../../verification/status_ledger.csv#L275) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/freeze_file.csv](../../../../verification/freeze_file.csv#L1) · explicit_file_citation
- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)
- [(* ---- (v199) QGEO.STATE.01: [rho,H]=0 <=> H is mu4-character-block-diagonal ---- *) Module[{nn, rho, idx, Hbd, Hoff, classOf}, nn = Range[-6, 6]; rho = DiagonalMatrix[I^nn]; (* carrier clock, order 4 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1648)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-15 (QGEO: the pillowcase reduction — two residuals become one canonical metric)

[documents/changelog/sections/019-source.tex:320-342](../../../../documents/changelog/sections/019-source.tex#L320) · `section:e415b5fb585454314b5d` · subsection

Pillowcase reduction of QGEO.SYM.01 ( v214_seam_pillowcase, tfpt_research_contracts, / ; ledger QGEO.PILLOW.01). The two separately-tracked open QGEO residuals — QGEO.ISO.01 ( v180: the carrier clock is an order- [formula in source] isometry of the seam metric) and QGEO.SUBPRIN.01 ( v201: the DtN sub-principal symbol is mark-local, the seam flat away from the [formula in source] marks) — are shown to be one statement

Explicit source references:

- [QGEO.ISO.01](../../../../verification/status_ledger.csv#L260) · explicit_claim_identifier · original status at linked ledger row
- [verification/v180_clock_is_mobius.py](../../../../verification/v180_clock_is_mobius.py#L1) · explicit_script_identifier
- [verification/v168_qgeo_rigidity.py](../../../../verification/v168_qgeo_rigidity.py#L1) · explicit_script_identifier
- [QGEO.SUBPRIN.01](../../../../verification/status_ledger.csv#L273) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [QGEO.PILLOW.01](../../../../verification/status_ledger.csv#L274) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v168) QGEO rigidity: mu4 square cross-ratio, mu4 characters = A3 exponents ---- *) Module[{mu4, cross, zz, eig, qspec}, mu4 = {1, I, -1, -I}; cross = Simplify[(mu4[[1]] - mu4[[3]]) (mu4[[2]] - mu4[[4]]) / ((mu4[[1]] - mu4[[4]]) (mu4[[2]] - mu4[[3]])) ]; (* omega_k = z^{k-1}/(z^4-1); pullback z->i z eigenvalue should be i^k *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1452)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-15 (the F_transfer functor contract CONTRACT.F.01)

[documents/changelog/sections/019-source.tex:343-359](../../../../documents/changelog/sections/019-source.tex#L343) · `section:4376c1a8c4e207cfb1f6` · subsection

[formula in source] formalised as a typed functor with four axioms ( v213_ftransfer_functor, tfpt_research_contracts, ). The four frontier transfers are consolidated into ONE functor [formula in source] , each instance a discrete compiler kernel \ composed with an external continuous solver : (1) [formula in source] -deck equivariance (the Koide multiplier [formula in source] is the deck transfer eigenvalue); (2) Pl\

Explicit source references:

- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_script_identifier
- [CONTRACT.F.01](../../../../verification/status_ledger.csv#L302) · explicit_claim_identifier · original status at linked ledger row
- [verification/v212_leptogenesis_decuple.py](../../../../verification/v212_leptogenesis_decuple.py#L1) · explicit_script_identifier
- [verification/v164_qcd_scale.py](../../../../verification/v164_qcd_scale.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v211_axion_spine_angle.py](../../../../verification/v211_axion_spine_angle.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)

## 2026-06-15 (frontier: two sharper [C] scenario branches — axion angle + leptogenesis)

[documents/changelog/sections/019-source.tex:360-379](../../../../documents/changelog/sections/019-source.tex#L360) · `section:f4b6348640da84580573` · subsection

Axion DM spine-angle branch [formula in source] ( v211_axion_spine_angle, tfpt_4_frontier, ). A more robust misalignment angle than the determinant-line hilltop [formula in source] ( v185, which over-produces [formula in source] ): the central spine quotient gives [formula in source] exactly (no fit), the finite- [formula in source] solver reaches [formula in source] at [formula in source] , and [formula in source] s

Explicit source references:

- [FR.ETAB.04](../../../../verification/status_ledger.csv#L301) · explicit_claim_identifier · original status at linked ledger row
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_script_identifier
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier
- [DM.AXION.SPINE.01](../../../../verification/status_ledger.csv#L299) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-15 (Lean: QGEO.COHOM.01 character grading + MODULE parity machine-proved)

[documents/changelog/sections/020-source.tex:1-17](../../../../documents/changelog/sections/020-source.tex#L1) · `section:c2f9c0d9f1b119435aaf` · subsection

The cohomology character grading is now Lean-formalised ( CohomologyGrading.lean, ledger FORM.QGEO.03, ). A new module machine-proves the Cohom node of the QGEO proof tree ( v177; audit: pass, no sorry/ admit, axioms propext, Classical.choice, Quot.sound only): the three [formula in source] eigenforms [formula in source] ( [formula in source] ) have pullback character [formula in source] under the clock [formula in s

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [FORM.QGEO.03](../../../../verification/status_ledger.csv#L298) · explicit_claim_identifier · original status at linked ledger row
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)

## 2026-06-15 (Lean: QGEO.UNIFORM.01 geometric normal form machine-proved)

[documents/changelog/sections/020-source.tex:18-33](../../../../documents/changelog/sections/020-source.tex#L18) · `section:fbaeb4d566affaf1be8a` · subsection

The M\"obius uniformisation normal form is now Lean-formalised ( Mobius Uniformisation.lean, ledger FORM.QGEO.02, ). A new module machine-proves the constructive Uniform node of the QGEO proof tree ( v177; audit: pass, no sorry/ admit, axioms propext, Classical.choice, Quot.sound only): the clock [formula in source] has [formula in source] and [formula in source] (order exactly [formula in source] ); the reflection [

Explicit source references:

- [FORM.QGEO.02](../../../../verification/status_ledger.csv#L297) · explicit_claim_identifier · original status at linked ledger row
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1) · explicit_file_citation
- [QGEO.MARKS.01](../../../../verification/status_ledger.csv#L256) · explicit_claim_identifier · original status at linked ledger row
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)

## 2026-06-15 (Lean: the QGEO.SYM.01 conditional theorem machine-proved)

[documents/changelog/sections/020-source.tex:34-51](../../../../documents/changelog/sections/020-source.tex#L34) · `section:a892802bd300a4a050f4` · subsection

The mark-local [formula in source] implication is now Lean-formalised ( SeamDeckClosure.lean, ledger FORM.QGEO.01, ). A new module in the carrier-rigidity Lean project machine-proves the algebraic core of v201/ v210 ( audit: pass, no sorry/ admit, no domain axioms — \#print axioms [formula in source] propext, Classical.choice, Quot.sound only): (i) the [formula in source] th-root character orthogonality [formula in s

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [FORM.QGEO.01](../../../../verification/status_ledger.csv#L296) · explicit_claim_identifier · original status at linked ledger row
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [verification/v210_mark_local_dtn.py](../../../../verification/v210_mark_local_dtn.py#L1) · explicit_script_identifier
- [TFPT.Carrier.SeamDeckClosure.markLocal_blockDiagonal](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L127) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)

## 2026-06-15 (QGEO sharpening: mark-local DtN certified on realistic profiles)

[documents/changelog/sections/020-source.tex:52-67](../../../../documents/changelog/sections/020-source.tex#L52) · `section:a5cf57be6b809cb6f0d7` · subsection

Mark-local DtN [formula in source] , certified on realistic Steklov profiles and at the state level ( v210_mark_local_dtn, tfpt_research_contracts, ). A numerical sharpening of QGEO.SUBPRIN.01/ v201: a real von-Mises curvature bump summed over the four [formula in source] marks, [formula in source] , builds the Steklov DtN [formula in source] whose off- [formula in source] Fourier support vanishes to [formula in sour

Explicit source references:

- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [QGEO.SUBPRIN.01](../../../../verification/status_ledger.csv#L273) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.MARKLOCAL.01](../../../../verification/status_ledger.csv#L295) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-15 (archive integration \#5: six dormant results revived from the old papers)

[documents/changelog/sections/020-source.tex:68-98](../../../../documents/changelog/sections/020-source.tex#L68) · `section:c42d97fdd386889e5412` · subsection

Muon [formula in source] as a seam vertex ( v204_muon_seam_g2, tfpt_4_frontier, ). The carrier's second-order topological defect [formula in source] projected through the seam-loop phase gives [formula in source] ( [formula in source] vs the dispersive [formula in source] ; [formula in source] vs lattice/CMD-3). The value is exact ; the vertex identification is the \ bridge. Ledger FR.MUONG2.01; Wolfram-mirrored. An 

Explicit source references:

- [GRAV.ASYMP.01](../../../../verification/status_ledger.csv#L292) · explicit_claim_identifier · original status at linked ledger row
- [FR.MUONG2.01](../../../../verification/status_ledger.csv#L289) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.XI.01](../../../../verification/status_ledger.csv#L290) · explicit_claim_identifier · original status at linked ledger row
- [verification/v152_norm_is_anchor.py](../../../../verification/v152_norm_is_anchor.py#L1) · explicit_script_identifier
- [verification/v28_gravity_fR.py](../../../../verification/v28_gravity_fR.py#L1) · explicit_script_identifier
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_script_identifier
- [HOR.BHCORE.01](../../../../verification/status_ledger.csv#L294) · explicit_claim_identifier · original status at linked ledger row
- [HOR.BHTHERMO.01](../../../../verification/status_ledger.csv#L293) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.H0.01](../../../../verification/status_ledger.csv#L291) · explicit_claim_identifier · original status at linked ledger row
- [verification/v199_seam_state_invariance.py](../../../../verification/v199_seam_state_invariance.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v205) GRAV.XI.01: xi = c3/phi_tree = 3/4, the independent gravitational 3/4 ---- *) Module[{c3, phitree}, c3 = 1/(8 Pi); phitree = 1/(6 Pi); checkExact["v205 GRAV.XI.01: the torsion-compression factor xi = c3/phi_tree = (1/8pi)/(1/6pi) = 3/4 EXACTLY; the Einstein-limit reduction 8 pi c3^2 = c3 makes G an output (xi = c3/phi0); and 3/4 = 12 pi (c3/2) = ln(m/mu) = q(A3) (v152) -- the torsion-compression and the gapped EH replica are two independent appearances of the same gravitational 3/4", Simplify[c3/phitree - 3/4] == 0 && Simplify[8 Pi c3^2 - c3] == 0 && Simplify[12 Pi (c3/2) - 3/4] == 0]; ]; (* ---- (v208) HOR.BHTHERMO.01: scalaron Wald factor + modular 2 pi = 1/(4 c3) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1708)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [(* ---- (v199) QGEO.STATE.01: [rho,H]=0 <=> H is mu4-character-block-diagonal ---- *) Module[{nn, rho, idx, Hbd, Hoff, classOf}, nn = Range[-6, 6]; rho = DiagonalMatrix[I^nn]; (* carrier clock, order 4 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1648)
- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)

## 2026-06-15 (archive integration \#4: M\"obius [formula in source] Lorentz foundation citation)

[documents/changelog/sections/020-source.tex:99-110](../../../../documents/changelog/sections/020-source.tex#L99) · `section:954c40e55830e15dd43b` · subsection

The M\"obius seam is the boundary Lorentz structure ( tfpt_3, ). Added a paragraph to the ``M\"obius origin of [formula in source] '' section: [formula in source] (Penrose \& Rindler, Spinors and Space-time, Vol. 1, 1.2–1.4), the celestial sphere of null directions via stereographic projection. This gives the self-consistency loop a spacetime meaning — the carrier clock [formula in source] is an elliptic [formula in 

Explicit source references:

- [verification/v180_clock_is_mobius.py](../../../../verification/v180_clock_is_mobius.py#L1) · explicit_script_identifier

## 2026-06-15 (archive integration \#3: axion coupling [formula in source] + retired small-angle reading)

[documents/changelog/sections/020-source.tex:111-122](../../../../documents/changelog/sections/020-source.tex#L111) · `section:fc9d294f005b7ca60e26` · subsection

Haloscope coupling tied to [formula in source] ( tfpt_4_frontier, ). Made explicit: in the determinant-line normalization the axion–photon anomaly coefficient is [formula in source] ( [formula in source] ), so the haloscope [formula in source] coupling is set by the same [formula in source] that fixes [formula in source] and [formula in source] — a \ structural relation (the coefficient, not a parameter-free physical

Explicit source references:

- [verification/v188_frontier_wording_guard.py](../../../../verification/v188_frontier_wording_guard.py#L1) · explicit_script_identifier

## 2026-06-15 (archive integration \#2: the EHT achromatic polarization intercept — v203)

[documents/changelog/sections/020-source.tex:123-139](../../../../documents/changelog/sections/020-source.tex#L123) · `section:e60c8c7dc2298081bbd9` · subsection

HOR.EHT.01 ( v203, / / ). The surviving core of the old UFE/black-hole notes ( not the RN-type metric — superseded by the Nariai/seam [formula in source] horizon readouts v101– v104/ v190; only the polarization signature survives): a local achromatic polarization-rotation intercept around a horizon-scale black hole, [formula in source] . The coupling [formula in source] is exact ( , Wolfram-mirrored) — the same top-f

Explicit source references:

- [verification/v104_nariai_clock.py](../../../../verification/v104_nariai_clock.py#L1) · explicit_script_identifier
- [verification/v203_eht_achromatic.py](../../../../verification/v203_eht_achromatic.py#L1) · explicit_script_identifier
- [verification/v190_nariai_entropy_bound.py](../../../../verification/v190_nariai_entropy_bound.py#L1) · explicit_script_identifier
- [verification/v101_horizon_anchor.py](../../../../verification/v101_horizon_anchor.py#L1) · explicit_script_identifier
- [HOR.EHT.01](../../../../verification/status_ledger.csv#L279) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v203) HOR.EHT.01: the EHT polarization coupling 16 c3^4 = 1/(256 pi^4) = delta_top/3 ---- *) Module[{c3, dtop}, c3 = 1/(8 Pi); dtop = 48 c3^4; (* = 3/(256 pi^4) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1685)
- [(* ---- (v190) Nariai entropy bound: S_tot/S_dS >= 2/3 via (x-1)^2 ---- *) Module[{x, ratio, val1, gap, mn}, ratio = (x^2 + 1)/(x^2 + x + 1); (* denom = Phi_3(x), the N_fam cyclotomic *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1574)
- [(* ---- (v126) clock-wall bridge ---- *) Module[{a0, spec, lams}, a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; spec = Sort[Eigenvalues[a0]]; checkExact["v126 the weights are the parabolic weights: spec A0* = {0, 1/3, 2/3} = n/N_fam; bridge (1-alpha)^6 = {1, (2/3)^6, (1/3)^6}", spec == {0, 1/3, 2/3} && Sort[((1 - #)^6 &) /@ spec, Greater] == {1, (2/3)^6, (1/3)^6}]; checkExact["v126 checkpoint 1 + determinant: linear coefficient p2/N = 2 = |Z2| (= v104 entropy rate 2H); det(1 - A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L890)
- [(* ---- (v101) horizon anchor: SdS in seam units ---- *) fSdS = 1 - 2 mm/rr - LL rr^2/3; cubicSdS = Expand[-fSdS 3 rr/LL]; narSol = Solve[{cubicSdS == 0, D[cubicSdS, rr] == 0}, {rr, mm}, Assumptions -> LL > 0]; checkExact["v101 Nariai double root: M_N = 1/(3 Sqrt[L]) = 1/(N_fam Sqrt[L]), r_N = 1/Sqrt[L]", MemberQ[Simplify[{rr, mm} /. narSol], {1/Sqrt[LL], 1/(3 Sqrt[LL])}]]; checkExact["v101 Nariai cubic = t^3 - 3t + 2 = (t-1)^2(t+2): roots (1,1,-2) = traceless anchor", (Expand[(t - 1)^2 (t + 2)] == t^3 - 3 t + 2) && (Simplify[{1, 1, 2} - (4/3) {1, 1, 1} - (-1/3) {1, 1, -2}] == {0, 0, 0})]; checkExact["v101 Koide 2/3 = Nariai entropy bound: S_N/S_dS = 2/3, per horizon 1/3, deficit 1/3", ((2 Pi/LL)/(3 Pi/LL) == 2/3) && ((Pi/LL)/(3 Pi/LL) == 1/3)]; checkExact["v101 interpolation S_tot/S_dS = (x^2+1)/(x^2+x+1) (denominator = Phi_3), min at merge", (Simplify[(xx^2 + 1)/(xx^2 + xx + 1) - (Pi (xx^2 + 1) 3/(LL (xx^2 + xx + 1)))/(3 Pi/LL)] === 0) && (Cyclotomic[3, xx] == xx^2 + xx + 1) && (((xx^2 + 1)/(xx^2 + xx + 1) /. xx -> 0) == 1) && (((xx^2 + 1)/(xx^2 + xx + 1) /. xx -> 1) == 2/3)]; checkExact["v101 three-sheet conservation: Sum r_i^2 = 2(rb^2+rb rc+rc^2) for roots (rb, rc, -(rb+rc))", Expand[rbb^2 + rcc^2 + (rbb + rcc)^2 - 2 (rbb^2 + rbb rcc + rcc^2)] === 0]; checkExact["v101 Q_geom range: pure dS -> 1/2 = delta, Nariai -> 3/8 = p2(a)/e1(a)^2 = SU(4)_1 weights", Module[{Qg = (xx^2 + (xx + 1)^2 + 1)/(4 (xx + 1)^2)}, ((Qg /. xx -> 0) == 1/2) && ((Qg /. xx -> 1) == 3/8) && (6/16 == 3/8)]]; checkExact["v101 mass-line double cover: disc = (108/L^3)(1-9 L M^2) -> (1-3m)(1+3m), branch +-1/N_fam", (Simplify[Discriminant[cubicSdS, rr] - 108/LL^3 (1 - 9 LL mm^2)] === 0) && (Expand[(1 - 3 md) (1 + 3 md) - (1 - 9 md^2)] === 0)]; checkExact["v101 temperature lemma: |kappa_b/kappa_c| = (2x+1)/(x(x+2)), = 1 iff x = 1", Module[{ff, kb, kc}, ff = -LL/(3 rr) (rr - rbb) (rr - rcc) (rr + rbb + rcc); kb = D[ff, rr] /. rr -> rbb; kc = D[ff, rr] /. rr -> rcc; Simplify[(kb/-kc /. rbb -> xx rcc) - (2 xx + 1)/(xx (xx + 2)), Assumptions -> rcc > 0 && xx > 0 && xx < 1] === 0]]; checkExact["v101 seam-unit mechanics: 1/(8Pi) = c3; Smarr 1/(4Pi) = 2c3; Bekenstein 2Pi = 1/(4c3); P_H 15360 Pi = 1920/c3; lifetime 5120 Pi = 128*5/c3; Kerr A_ext = M^2/c3; 4 Log[3] = Log[81]", (1/(8 Pi) == c3) && (Simplify[1/(4 Pi) - 2 c3] === 0) && (Simplify[2 Pi - 1/(4 c3)] === 0) && (Simplify[1/(15360 Pi) - c3/1920] === 0) && (Simplify[5120 Pi - 128*5/c3] === 0) && (Simplify[8 Pi - 1/c3] === 0) && (Simplify[4 Log[3] - Log[81]] === 0)]; (* ---- (v102) seam orientation: anchor = stationary repeller, both sectors ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L333)
- [(* ---- (v103) trisection normal form ---- *) checkExact["v103 trisection: r = 2 cos(theta) => r^3 - 3r = 2 cos(3 theta) exactly", Simplify[(2 Cos[th])^3 - 3 (2 Cos[th]) - 2 Cos[3 th]] === 0]; rcT = 2 Cos[(ps + Pi)/3]; rbT = 2 Cos[(ps - Pi)/3]; r3T = 2 Cos[(ps + 3 Pi)/3]; checkExact["v103 centered angle: m = cos(psi)/3; roots sum 0, e2 = -3; Nariai roots (1,1,-2) at psi = 0", (Simplify[-Cos[ps + Pi]/3 - Cos[ps]/3] === 0) && (Simplify[rcT + rbT + r3T] === 0) && (Simplify[rcT rbT + rcT r3T + rbT r3T + 3] === 0) && (Simplify[{rcT, rbT, r3T} /. ps -> 0] == {1, 1, -2})]; sigT = Simplify[(rbT^2 + rcT^2)/3]; checkExact["v103 NORMAL FORM: sigma(psi) = 4/3 - (2/3) cos(2 psi/3); sigma(0) = 2/3, sigma(pi/2) = 1", (Simplify[sigT - (4/3 - (2/3) Cos[2 ps/3])] === 0) && (Simplify[sigT /. ps -> 0] == 2/3) && (Simplify[sigT /. ps -> Pi/2] == 1)]; checkExact["v103 canonical curvature sigma''(0) = 8/27 = (2/3)^3 (the Koide constant to the family power)", (Simplify[D[sigT, {ps, 2}] /. ps -> 0] == 8/27) && ((2/3)^3 == 8/27)]; checkExact["v103 invariant base slope: dsigma/dm = -(4/3) sin(2 psi/3)/sin(psi), limit -8/9 = -rank(E8)/N_fam^2", (Simplify[D[sigT, ps]/D[Cos[ps]/3, ps] + (4/3) Sin[2 ps/3]/Sin[ps]] === 0) && (Limit[D[sigT, ps]/D[Cos[ps]/3, ps], ps -> 0] == -8/9)]; checkExact["v103 x-coordinate cross-check: m(x) deck-invariant, m''(1) = -1/4, sigma''(1)/m''(1) = -8/9", Module[{mxw = Sqrt[3]/2 xx (1 + xx)/(xx^2 + xx + 1)^(3/2), sxw = (xx^2 + 1)/(xx^2 + xx + 1)}, (Simplify[(mxw /. xx -> 1/xx) - mxw, Assumptions -> xx > 0] === 0) && (Simplify[D[mxw, xx] /. xx -> 1] == 0) && (Simplify[D[mxw, {xx, 2}] /. xx -> 1] == -1/4) && (Simplify[(D[sxw, {xx, 2}] /. xx -> 1)/(D[mxw, {xx, 2}] /. xx -> 1)] == -8/9)]]; checkExact["v103 bridge: (2/3)^6 = ((2/3)^3)^2 -- same base, exponent ratio 2 = |Z2|", (2/3)^6 == ((2/3)^3)^2]; (* ---- (v104) the classical Nariai clock ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L392)

## 2026-06-15 (archive integration \#1: the rare kaon sector [formula in source] — v202)

[documents/changelog/sections/020-source.tex:140-156](../../../../documents/changelog/sections/020-source.tex#L140) · `section:7f2e391c59e00a9e6acb` · subsection

FR.RAREKAON.01 ( v202, ). The closed TFPT CKM point ( [formula in source] , [formula in source] , [formula in source] , [formula in source] rad; v18/ v88, no flavor fit) feeds the cleanest FCNC probe. With standard external short-distance input (Brod–Gorbahn–Stamou [formula in source] ) it gives [formula in source] and [formula in source] — a \ downstream flavor readout, not a compiler power (the SD functions are ext

Explicit source references:

- [verification/v18_quark_yukawa.py](../../../../verification/v18_quark_yukawa.py#L1) · explicit_script_identifier
- [FR.RAREKAON.01](../../../../verification/status_ledger.csv#L278) · explicit_claim_identifier · original status at linked ledger row
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v202_rare_kaon.py](../../../../verification/v202_rare_kaon.py#L1) · explicit_script_identifier
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier

## 2026-06-15 (bedrock: the [formula in source] residual reduced once more — v201)

[documents/changelog/sections/020-source.tex:157-174](../../../../documents/changelog/sections/020-source.tex#L157) · `section:17a730ae6b843f575a43` · subsection

QGEO.SUBPRIN.01 ( v201, / ). The v199 bedrock residual — ``the bounded sub-principal symbol of the raw seam DtN has no off-character (mod 4) matrix elements'' — is reduced one genuine step further: block-diagonality is not an independent postulate. Writing the DtN as [formula in source] with [formula in source] the bounded sub-principal piece [formula in source] multiplication by a curvature [formula in source] (stan

Explicit source references:

- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_script_identifier
- [QGEO.SUBPRIN.01](../../../../verification/status_ledger.csv#L273) · explicit_claim_identifier · original status at linked ledger row
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v195_marks_lefschetz_character.py](../../../../verification/v195_marks_lefschetz_character.py#L1) · explicit_script_identifier
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [verification/v199_seam_state_invariance.py](../../../../verification/v199_seam_state_invariance.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [(* ---- (v199) QGEO.STATE.01: [rho,H]=0 <=> H is mu4-character-block-diagonal ---- *) Module[{nn, rho, idx, Hbd, Hoff, classOf}, nn = Range[-6, 6]; rho = DiagonalMatrix[I^nn]; (* carrier clock, order 4 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1648)
- [(* ---- (v195) QGEO.MARKS.02: Lefschetz/character forcing of the free mu4 orbit ---- *) Module[{chars, trace, noTrivial, orbit, orbitClosed, nPunct}, chars = I^Range[1, 3]; (* {I, -1, -I} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1607)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-15 (F_transfer workshop: the axion relic solver — an honest over-production tension)

[documents/changelog/sections/020-source.tex:175-198](../../../../documents/changelog/sections/020-source.tex#L175) · `section:208cd3e2a794336cad9d` · subsection

Axion relic solver ( experiments/ftransfer/axion_relic/relic_solver.py, ). The first real [formula in source] pipeline computation (work package C / review 6.2): a standard misalignment relic with a numerically-computed anharmonic factor [formula in source] at the hilltop. Honest finding: at the predicted [formula in source] the estimate over-produces dark matter, [formula in source] – [formula in source] (robustly [

Explicit source references:

- [experiments/ftransfer/axion_relic/relic_solver.py](../../../../experiments/ftransfer/axion_relic/relic_solver.py#L1) · explicit_file_citation
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_script_identifier
- [experiments/ftransfer/axion_relic/full_finiteT_solve.py](../../../../experiments/ftransfer/axion_relic/full_finiteT_solve.py#L1) · explicit_file_citation

## 2026-06-14 (work packages A+B: attacking [formula in source] + the variational scan — v199, v200)

[documents/changelog/sections/020-source.tex:199-221](../../../../documents/changelog/sections/020-source.tex#L199) · `section:4d42f8071e36f9952644` · subsection

v199_seam_state_invariance.py / \ (claim QGEO.STATE.01, work package A). Attacking [formula in source] directly on the raw seam. (1) \ the setup is non-circular: [formula in source] is the Coxeter element of [formula in source] ( [formula in source] , v117), an automorphism of the raw CAR algebra (16 Majoranas) — both carrier-side, no seam geometry. (2) \ for a quasi-free RP state [formula in source] , so [formula in

Explicit source references:

- [verification/v200_seam_variational_scan.py](../../../../verification/v200_seam_variational_scan.py#L1) · explicit_file_citation
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_script_identifier
- [QGEO.STATE.01](../../../../verification/status_ledger.csv#L272) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.VARI.02](../../../../verification/status_ledger.csv#L280) · explicit_claim_identifier · original status at linked ledger row
- [verification/v199_seam_state_invariance.py](../../../../verification/v199_seam_state_invariance.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)
- [(* ---- (v199) QGEO.STATE.01: [rho,H]=0 <=> H is mu4-character-block-diagonal ---- *) Module[{nn, rho, idx, Hbd, Hoff, classOf}, nn = Range[-6, 6]; rho = DiagonalMatrix[I^nn]; (* carrier clock, order 4 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1648)

## 2026-06-14 (cracking the bedrock to a state-invariance: principal symbol [formula in source] Tomita–Takesaki — v198)

[documents/changelog/sections/020-source.tex:222-241](../../../../documents/changelog/sections/020-source.tex#L222) · `section:b56f3a2e55f262711774` · subsection

v198_modular_commutator_reduction.py \ (claim QGEO.MODULAR.01). The decisive crack on the last residual. (1) \ the DtN principal symbol [formula in source] and the clock [formula in source] are both diagonal in the Fourier basis, so [formula in source] exactly on all of [formula in source] (verified on 33 modes) — the leading-order commutation is free on the whole boundary, never the open part. (2) \ by Tomita–Takesa

Explicit source references:

- [QGEO.MODULAR.01](../../../../verification/status_ledger.csv#L271) · explicit_claim_identifier · original status at linked ledger row
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_file_citation
- [verification/v194_raw_seam_dtn_rp.py](../../../../verification/v194_raw_seam_dtn_rp.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-14 (three review levers: Marks-via-Lefschetz, E_fail functional, RR [formula in source] D5 — v195–v197)

[documents/changelog/sections/020-source.tex:242-266](../../../../documents/changelog/sections/020-source.tex#L242) · `section:c926c39e5cf2b4b2f828` · subsection

v195_marks_lefschetz_character.py / \ (claim QGEO.MARKS.02). The four seam marks are forced (not posited): [formula in source] fixes only [formula in source] , [formula in source] (the [formula in source] exponents, [formula in source] ) has no trivial component [formula in source] no puncture at a fixed point, and [formula in source] a single free [formula in source] orbit (cross-ratio [formula in source] ). So Mark

Explicit source references:

- [QGEO.MARKS.02](../../../../verification/status_ledger.csv#L269) · explicit_claim_identifier · original status at linked ledger row
- [ARCH.RRCAR.02](../../../../verification/status_ledger.csv#L263) · explicit_claim_identifier · original status at linked ledger row
- [verification/v196_seam_energy_functional.py](../../../../verification/v196_seam_energy_functional.py#L1) · explicit_file_citation
- [QGEO.VARI.01](../../../../verification/status_ledger.csv#L270) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v194_raw_seam_dtn_rp.py](../../../../verification/v194_raw_seam_dtn_rp.py#L1) · explicit_script_identifier
- [verification/v197_rr_carrier_clifford_d5.py](../../../../verification/v197_rr_carrier_clifford_d5.py#L1) · explicit_script_identifier
- [verification/v195_marks_lefschetz_character.py](../../../../verification/v195_marks_lefschetz_character.py#L1) · explicit_file_citation
- [verification/v189_riemann_roch_carrier.py](../../../../verification/v189_riemann_roch_carrier.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v189) Riemann-Roch carrier: (g_car,N_fam)=(5,3) from the mu4 divisor ---- *) Module[{degD, h0, rkH1, rankD5, rankA3}, degD = 4; (* |mu4| = deg D *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1564)
- [(* ---- (v195) QGEO.MARKS.02: Lefschetz/character forcing of the free mu4 orbit ---- *) Module[{chars, trace, noTrivial, orbit, orbitClosed, nPunct}, chars = I^Range[1, 3]; (* {I, -1, -I} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1607)
- [(* ---- (v197) ARCH.RRCAR.02: even Clifford of the 5-dim carrier = the D5 half-spinor ---- *) Module[{h0, lamEven}, h0 = 4 + 1; (* h^0(P^1,O(mu4)) = deg+1 = 5 = g_car *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1630)
- [(* ---- (v196) QGEO.VARI.01: E_fail = 0 on the mu4 block (exact finite vanishing) ---- *) Module[{rho, Lam, comm, order4, twist}, rho = DiagonalMatrix[{I, -1, -I}]; Lam = DiagonalMatrix[{1, 2, 3}]; (* any real diagonal (mu4-equivariant) DtN *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1619)

## 2026-06-14 (subclaim 2 of ENERGY.02 tackled: raw-seam-DtN RP-definability — v194)

[documents/changelog/sections/020-source.tex:267-283](../../../../documents/changelog/sections/020-source.tex#L267) · `section:113a50c68f53872c39d4` · subsection

v194_raw_seam_dtn_rp.py \ (claim QGEO.DTN.01). The next hard lever — ``is the raw RP-seam DtN definable from RP data alone?'' (sub-claim 2 of QGEO.ENERGY.02) — was tackled, and the honest result is a reduction, not a closure. (1) \ the commutator [formula in source] closes on the finite cohomology [formula in source] ( [formula in source] , distinct [formula in source] characters; v177). (2) \ the hinge is met: the D

Explicit source references:

- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_script_identifier
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.DTN.01](../../../../verification/status_ledger.csv#L268) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.ENERGY.02](../../../../verification/status_ledger.csv#L267) · explicit_claim_identifier · original status at linked ledger row
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [verification/v194_raw_seam_dtn_rp.py](../../../../verification/v194_raw_seam_dtn_rp.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)

## 2026-06-14 (QGEO.ENERGY.02 energy-commutator + QFT-wording hardening — v193)

[documents/changelog/sections/020-source.tex:284-303](../../../../documents/changelog/sections/020-source.tex#L284) · `section:6151ea351f3cf66e9630` · subsection

v193_qgeo_energy_commutator.py \ (claim QGEO.ENERGY.02). The non-circular sharpening of QGEO.ENERGY.01: the energy commutator [formula in source] on the rank- [formula in source] Calder\'on polarisation, with three sub-claims — (1) \ [formula in source] is carrier-defined (Coxeter of [formula in source] , v117), not imported from the seam; (2) \ the non-circularity hinge: [formula in source] must be the raw RP-seam D

Explicit source references:

- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.ENERGY.01](../../../../verification/status_ledger.csv#L266) · explicit_claim_identifier · original status at linked ledger row
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_script_identifier
- [verification/v150_replica_eh_model.py](../../../../verification/v150_replica_eh_model.py#L1) · explicit_script_identifier
- [verification/v188_frontier_wording_guard.py](../../../../verification/v188_frontier_wording_guard.py#L1) · explicit_script_identifier
- [QGEO.ENERGY.02](../../../../verification/status_ledger.csv#L267) · explicit_claim_identifier · original status at linked ledger row
- [verification/v193_qgeo_energy_commutator.py](../../../../verification/v193_qgeo_energy_commutator.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v150) replica EH model ---- *) Module[{cdef, imgOK, convOK, mellin, dz0, dC, target}, cdef[g_] := (1/12) (2 Pi/g - g/(2 Pi)); imgOK = And @@ Table[ FullSimplify[Sum[1/Sin[Pi k/n]^2, {k, 1, n - 1}] - (n^2 - 1)/3] === 0, {n, 2, 8}]; convOK = Simplify[(1/(4 nn)) (nn^2 - 1)/3 - cdef[2 Pi/nn]] === 0; mellin = Integrate[tt^(ss - 1) Exp[-mm^2 tt], {tt, 0, Infinity}, Assumptions -> ss > 0 && mm > 0]; dz0 = D[mm^(-2 ss), ss] /. ss -> 0; dC = D[cdef[gg], gg] /. gg -> 2 Pi; target = Simplify[12 Pi (1/2) (1/(8 Pi))]; checkExact["v150 replica EH model: image sum exact (N=2..8); orbifold deficit = C(2pi/N); Mellin Delta-zeta(s) = C m^-2s => Delta log det' = 2C ln m (cutoff-independent); dC/dgamma|_{2pi} = -1/(12pi) => EH form with k = ln m/(12pi); target k = c3/2 <=> ln m = 3/4 = q(A3)", imgOK && convOK && Simplify[mellin - Gamma[ss] mm^(-2 ss)] === 0 && Simplify[dz0 + 2 Log[mm]] === 0 && Simplify[dC + 1/(12 Pi)] === 0 && target == 3/4]; ]; (* ---- (v151) BFK split ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1321)
- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)
- [(* ---- (v193) QGEO.ENERGY.02 EH-rigidity rider: the EH coeff selects q(A3), not q(D5) ---- *) Module[{gcar, Nfam, mu4, c3, qA3, qD5, kFamily, kCarrier, kTarget}, gcar = 5; Nfam = 3; mu4 = 4; c3 = 1/(8 Pi); qA3 = Nfam/mu4; (* 3/4 family glue norm *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1594)

## 2026-06-14 (geometry round: Riemann-Roch carrier, Nariai bound, branch line, energy clock — v189–v192)

[documents/changelog/sections/020-source.tex:304-331](../../../../documents/changelog/sections/020-source.tex#L304) · `section:fe43532db2385fecd956` · subsection

v189_riemann_roch_carrier.py / \ (claim ARCH.RRCAR.01). The pair [formula in source] are the two canonical invariants of one object, the four-point seam divisor [formula in source] on [formula in source] : the cycle side [formula in source] (already QGEO.COHOM.01) and the function side [formula in source] , matched by [formula in source] . The carrier-as-mode-space reading is \ (geometric, does not displace the over-

Explicit source references:

- [verification/v191_universal_branch_line.py](../../../../verification/v191_universal_branch_line.py#L1) · explicit_file_citation
- [verification/v192_qgeo_energy_clock.py](../../../../verification/v192_qgeo_energy_clock.py#L1) · explicit_file_citation
- [HOR.BRANCHLINE.01](../../../../verification/status_ledger.csv#L265) · explicit_claim_identifier · original status at linked ledger row
- [ARCH.RRCAR.01](../../../../verification/status_ledger.csv#L262) · explicit_claim_identifier · original status at linked ledger row
- [verification/v189_riemann_roch_carrier.py](../../../../verification/v189_riemann_roch_carrier.py#L1) · explicit_script_identifier
- [HOR.NARIAI.02](../../../../verification/status_ledger.csv#L264) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v190_nariai_entropy_bound.py](../../../../verification/v190_nariai_entropy_bound.py#L1) · explicit_file_citation
- [QGEO.ENERGY.01](../../../../verification/status_ledger.csv#L266) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v190) Nariai entropy bound: S_tot/S_dS >= 2/3 via (x-1)^2 ---- *) Module[{x, ratio, val1, gap, mn}, ratio = (x^2 + 1)/(x^2 + x + 1); (* denom = Phi_3(x), the N_fam cyclotomic *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1574)
- [(* ---- (v189) Riemann-Roch carrier: (g_car,N_fam)=(5,3) from the mu4 divisor ---- *) Module[{degD, h0, rkH1, rankD5, rankA3}, degD = 4; (* |mu4| = deg D *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1564)
- [(* ---- (v191) Universal branch line: exact affine RELABELING (NOT a theorem) ---- *) Module[{Nfam, q, qm, q0, qp, decoyA, decoyB}, Nfam = 3; q[mm_] := 7/2 + (Nfam^2/2) mm; qm = q[-1/Nfam]; q0 = q[0]; qp = q[1/Nfam]; decoyA = (3 + 4)/2; decoyB = (4 - 3)/(2/Nfam); (* decoy {3,4}: midpoint 7/2, slope 3/2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1584)

## 2026-06-14 (Zenodo release 5.1 (rev 120) — F_transfer firewall, v184–v188)

[documents/changelog/sections/020-source.tex:332-344](../../../../documents/changelog/sections/020-source.tex#L332) · `section:1baa0cb6fdd6a6b16124` · subsection

Published to Zenodo. Version 5.1 (rev 120) of the ten-PDF document set was published as a new version of the TFPT deposit — record 20687564, DOI 10.5281/zenodo.20687564. This version carries the F_transfer-firewall round ( v184– v188): the honest [formula in source] anchored-Boltzmann test (sharper scenario, not a closure), the axion hilltop-relic typing, the ledger v187 and prose v188 guards, and the Route B/Koide/d

Explicit source references:

- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v188_frontier_wording_guard.py](../../../../verification/v188_frontier_wording_guard.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier

## 2026-06-14 (F_transfer round: eta_B honest test v184, axion relic v185, discipline guard v187)

[documents/changelog/sections/020-source.tex:345-385](../../../../documents/changelog/sections/020-source.tex#L345) · `section:b559ae6d59524fc410e4` · subsection

v184_etaB_anchored_boltzmann.py \ (claim FR.ETAB.03). An honest test of the external-review [formula in source] proposal ( [formula in source] , [formula in source] ). Firewall verdict: sharper scenario, not a closure. The washout anchors plausibly ( [formula in source] meV, [formula in source] atom, in the strong-washout window) ; but [formula in source] does not — [formula in source] is the seesaw scale [formula in

Explicit source references:

- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_file_citation
- [QCD.LAMBDA.01](../../../../verification/status_ledger.csv#L250) · explicit_claim_identifier · original status at linked ledger row
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_script_identifier
- [FR.TRANSFER.01](../../../../verification/status_ledger.csv#L181) · explicit_claim_identifier · original status at linked ledger row
- [FR.DM.03](../../../../verification/status_ledger.csv#L180) · explicit_claim_identifier · original status at linked ledger row
- [verification/v188_frontier_wording_guard.py](../../../../verification/v188_frontier_wording_guard.py#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_file_citation
- [AUDIT.WORDING.01](../../../../verification/status_ledger.csv#L182) · explicit_claim_identifier · original status at linked ledger row
- [FR.ETAB.03](../../../../verification/status_ledger.csv#L179) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)

## 2026-06-14 (operator origin of the Koide 53/54 factor: the missing Sheet-Diamond corner, v183)

[documents/changelog/sections/021-source.tex:1-21](../../../../documents/changelog/sections/021-source.tex#L1) · `section:c1ba016bb9366edd1984` · subsection

v183_koide_f_corner_transfer.py / \ (claim FR.KOIDE.07). An external-review proposal, validated exactly: the Koide source [formula in source] pole factor [formula in source] is not a bare arithmetic guess but an operator identity on the carrier, [formula in source] . Here [formula in source] is the [formula in source] cubic family block ( [formula in source] ) and [formula in source] , where [formula in source] is th

Explicit source references:

- [verification/v103_trisection_normal_form.py](../../../../verification/v103_trisection_normal_form.py#L1) · explicit_script_identifier
- [FR.KOIDE.03](../../../../verification/status_ledger.csv#L61) · explicit_claim_identifier · original status at linked ledger row
- [FR.KOIDE.07](../../../../verification/status_ledger.csv#L178) · explicit_claim_identifier · original status at linked ledger row
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_file_citation
- [HOR.TRISECT.01](../../../../verification/status_ledger.csv#L186) · explicit_claim_identifier · original status at linked ledger row
- [verification/v80_operator_pencil_geometry.py](../../../../verification/v80_operator_pencil_geometry.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v80) operator-pencil geometry: anchor singularity + block-det type checker + F4xG2 shadow ---- *) checkExact["anchor singularity: det B(K+xQ)=(3x+2)(3x+5); type checker det B = (9,10,16,40) for (Q,K,R,L)", Module[{one = {1, 1, 1}, av = {1, 1, 2}, bb, dbx}, bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}}; dbx = Det[bb[K + xx*Q]]; (Factor[dbx] == (3 xx + 2) (3 xx + 5)) && (Det[bb[Q]] == 9) && (Det[bb[K]] == 10) && (Det[bb[R]] == 16) && (Det[bb[L]] == 40)]]; checkExact["F4xG2 shadow: det B_{R+Q}=52=dim F4; 248 = 52 + 14 + 26*7 (real E8->F4xG2 branching)", Module[{one = {1, 1, 1}, av = {1, 1, 2}, F = R + Q, bb}, bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}}; (Det[bb[F]] == 52) && (52 + 14 + 26*7 == 248)]]; (* ---- (v81) double cover: det B(K+xQ) quadratic, branch points {-2/3,-5/3}, disc=81=N_fam^4 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L397)
- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)
- [(* ---- (v103) trisection normal form ---- *) checkExact["v103 trisection: r = 2 cos(theta) => r^3 - 3r = 2 cos(3 theta) exactly", Simplify[(2 Cos[th])^3 - 3 (2 Cos[th]) - 2 Cos[3 th]] === 0]; rcT = 2 Cos[(ps + Pi)/3]; rbT = 2 Cos[(ps - Pi)/3]; r3T = 2 Cos[(ps + 3 Pi)/3]; checkExact["v103 centered angle: m = cos(psi)/3; roots sum 0, e2 = -3; Nariai roots (1,1,-2) at psi = 0", (Simplify[-Cos[ps + Pi]/3 - Cos[ps]/3] === 0) && (Simplify[rcT + rbT + r3T] === 0) && (Simplify[rcT rbT + rcT r3T + rbT r3T + 3] === 0) && (Simplify[{rcT, rbT, r3T} /. ps -> 0] == {1, 1, -2})]; sigT = Simplify[(rbT^2 + rcT^2)/3]; checkExact["v103 NORMAL FORM: sigma(psi) = 4/3 - (2/3) cos(2 psi/3); sigma(0) = 2/3, sigma(pi/2) = 1", (Simplify[sigT - (4/3 - (2/3) Cos[2 ps/3])] === 0) && (Simplify[sigT /. ps -> 0] == 2/3) && (Simplify[sigT /. ps -> Pi/2] == 1)]; checkExact["v103 canonical curvature sigma''(0) = 8/27 = (2/3)^3 (the Koide constant to the family power)", (Simplify[D[sigT, {ps, 2}] /. ps -> 0] == 8/27) && ((2/3)^3 == 8/27)]; checkExact["v103 invariant base slope: dsigma/dm = -(4/3) sin(2 psi/3)/sin(psi), limit -8/9 = -rank(E8)/N_fam^2", (Simplify[D[sigT, ps]/D[Cos[ps]/3, ps] + (4/3) Sin[2 ps/3]/Sin[ps]] === 0) && (Limit[D[sigT, ps]/D[Cos[ps]/3, ps], ps -> 0] == -8/9)]; checkExact["v103 x-coordinate cross-check: m(x) deck-invariant, m''(1) = -1/4, sigma''(1)/m''(1) = -8/9", Module[{mxw = Sqrt[3]/2 xx (1 + xx)/(xx^2 + xx + 1)^(3/2), sxw = (xx^2 + 1)/(xx^2 + xx + 1)}, (Simplify[(mxw /. xx -> 1/xx) - mxw, Assumptions -> xx > 0] === 0) && (Simplify[D[mxw, xx] /. xx -> 1] == 0) && (Simplify[D[mxw, {xx, 2}] /. xx -> 1] == -1/4) && (Simplify[(D[sxw, {xx, 2}] /. xx -> 1)/(D[mxw, {xx, 2}] /. xx -> 1)] == -8/9)]]; checkExact["v103 bridge: (2/3)^6 = ((2/3)^3)^2 -- same base, exponent ratio 2 = |Z2|", (2/3)^6 == ((2/3)^3)^2]; (* ---- (v104) the classical Nariai clock ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L392)

## 2026-06-14 (review recommendations 1/3/4 + the four concerns A–D mapped to the named residuals)

[documents/changelog/sections/021-source.tex:22-49](../../../../documents/changelog/sections/021-source.tex#L22) · `section:05aaf35318c9e1bb8204` · subsection

v182_reviewer_residual_map.py / \ (claim REVIEW.MAP.01). A careful external review raised four concerns (A mapping [formula in source] , B UV-gravity abstractness, C grammar-tuning/meta-look-elsewhere, D Koide M\"obius flow). This module shows three of them reduce, by the same discipline as v175– v181, onto the two already-named residuals [formula in source] : A (Pl\"ucker- [formula in source] [formula in source] QBL

Explicit source references:

- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [REVIEW.MAP.01](../../../../verification/status_ledger.csv#L281) · explicit_claim_identifier · original status at linked ledger row
- [verification/v181_clock_is_conformal_symmetry.py](../../../../verification/v181_clock_is_conformal_symmetry.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v174_seam_fock_readings.py](../../../../verification/v174_seam_fock_readings.py#L1) · explicit_script_identifier
- [verification/v182_reviewer_residual_map.py](../../../../verification/v182_reviewer_residual_map.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [(* ---- (v174) seam Fock-space readings: cone compression, Witten index, g-theorem ---- *) Module[{cone, blocks, trunc, disc, cUV, cIR}, cone = 2^15; blocks = {Binomial[16, 4], Binomial[16, 6], Binomial[16, 8]}; trunc = Sum[Binomial[4, k], {k, 0, 2}]; (* 11 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1509)

## 2026-06-14 (external-review response: CSV fix, G_net 3-level, QGEO.SYM.01 page, claim detox)

[documents/changelog/sections/021-source.tex:50-76](../../../../documents/changelog/sections/021-source.tex#L50) · `section:f7f27b7893f1db12bbb4` · subsection

Ledger CSV bug fixed + guarded. Three rows ( AX.P1.01, AX.P2.01, QGEO.ISO.01) had unquoted commas in a status/external field (e.g.\ ``a=(1,1,2)'', ``PSL(2,C)''), so a strict CSV parser read 11–12 columns instead of 10 — a real machine-readability defect in the single source of truth. All offending fields are now quoted (every row parses to exactly 10 columns), and audit_sync.py gained a check_csv_wellformed guard (le

Explicit source references:

- [QGEO.ISO.01](../../../../verification/status_ledger.csv#L260) · explicit_claim_identifier · original status at linked ledger row
- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/audit_sync.py](../../../../verification/audit_sync.py#L1) · explicit_file_citation
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)

## 2026-06-14 (Zenodo release 5.1 (rev 114) — v175–v181 bedrock + figures + P1/P2)

[documents/changelog/sections/021-source.tex:77-88](../../../../documents/changelog/sections/021-source.tex#L77) · `section:56260a726c20b0e2fff7` · subsection

Published to Zenodo. Version 5.1 (rev 114) of the ten-PDF document set was published as a new version of the TFPT deposit — record 20686284, DOI 10.5281/zenodo.20686284. This version carries the AQFT-closure-to-bedrock chain ( v175– v181, the structural residual reduced to the single definitional premise QGEO.SYM.01), the two overview figures ( residual_chain, script_timeline), and the P1/P2 anchor-reduction provenan

Explicit source references:

- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [verification/v181_clock_is_conformal_symmetry.py](../../../../verification/v181_clock_is_conformal_symmetry.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)

## 2026-06-14 (overview figures + P1/P2 reduction reflected on the axiom surfaces)

[documents/changelog/sections/021-source.tex:89-110](../../../../documents/changelog/sections/021-source.tex#L89) · `section:e2c33aad84858bc51b9d` · subsection

Two overview figures ( make_figures.py; PDF [formula in source] website PNG). (i) residual_chain — the structural-residual reduction chain v175– v181 as a descending staircase from ``build a quantum-gravity measure'' to the single definitional bedrock QGEO.SYM.01; embedded in tfpt_research_contracts. (ii) script_timeline — the eight-phase journey of the [formula in source] 181 scripts (foundations [formula in source]

Explicit source references:

- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [FORM.LADDER.01](../../../../verification/status_ledger.csv#L192) · explicit_claim_identifier · original status at linked ledger row
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [verification/v23_anchor_generator.py](../../../../verification/v23_anchor_generator.py#L1) · explicit_script_identifier
- [verification/v181_clock_is_conformal_symmetry.py](../../../../verification/v181_clock_is_conformal_symmetry.py#L1) · explicit_script_identifier
- [ANCHOR.GEN.01](../../../../verification/status_ledger.csv#L24) · explicit_claim_identifier · original status at linked ledger row
- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [verification/make_figures.py](../../../../verification/make_figures.py#L1) · explicit_file_citation
- [ARCH.CORE.01](../../../../verification/status_ledger.csv#L136) · explicit_claim_identifier · original status at linked ledger row
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [verification/v53_compiler_core.py](../../../../verification/v53_compiler_core.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [(* ==== v491 round: P2.PARTITION.01 -- g_car = 5 as the partition corollary of the four marks (the sharpening of v53). Exact content: 4 into exactly 3 positive integer parts is uniquely {1,1,2} => e = (4,5,2) => g_car = e2 = 5, |Z2| = e3 = 2, N_fam = e2 - e3 = 3 as corollaries; every assumption load-bearing (positivity / sum / part count / integrality negative controls); v53 needs all three targets, the partition only e1 = 4; sum rule 4(N-1)/2 = 4 iff N = 3; mirrors v491. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3116)

## 2026-06-14 (the final reduction to bedrock v181 + full non-changelog status sweep)

[documents/changelog/sections/021-source.tex:111-133](../../../../documents/changelog/sections/021-source.tex#L111) · `section:4ff2bf714d7cbf97df82` · subsection

v181_clock_is_conformal_symmetry.py / \ (claim QGEO.SYM.01). The isometry premise QGEO.ISO.01 ( v180) is weakened one more genuine step — to a conformal- symmetry premise — via equivariant uniformisation (Nielsen realisation; for cyclic groups Ker\'ekj\'art\'o [formula in source] uniformisation): a conformal automorphism (strictly weaker than an isometry — every isometry is conformal, conformal allows any positive sc

Explicit source references:

- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [QGEO.ISO.01](../../../../verification/status_ledger.csv#L260) · explicit_claim_identifier · original status at linked ledger row
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v181_clock_is_conformal_symmetry.py](../../../../verification/v181_clock_is_conformal_symmetry.py#L1) · explicit_file_citation
- [verification/v180_clock_is_mobius.py](../../../../verification/v180_clock_is_mobius.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)

## 2026-06-14 (the conformal premise reduces to a milder isometry premise v180)

[documents/changelog/sections/021-source.tex:134-155](../../../../documents/changelog/sections/021-source.tex#L134) · `section:10f005ddcd31b0102625` · subsection

v180_clock_is_mobius.py / \ (claim QGEO.ISO.01). Cracks QGEO.CONF.01 one level further: the conformal-realisation premise is replaced, via three classical theorems, by a strictly milder, non-circular premise. (1) Uniformisation (Poincar\'e–Koebe): a genus- [formula in source] Riemann surface is conformally [formula in source] , so the genus- [formula in source] seam double (P1, v179) with its RP-metric conformal stru

Explicit source references:

- [QGEO.ISO.01](../../../../verification/status_ledger.csv#L260) · explicit_claim_identifier · original status at linked ledger row
- [verification/v180_clock_is_mobius.py](../../../../verification/v180_clock_is_mobius.py#L1) · explicit_script_identifier
- [QGEO.CONF.01](../../../../verification/status_ledger.csv#L259) · explicit_claim_identifier · original status at linked ledger row
- [verification/v179_conformal_realisation.py](../../../../verification/v179_conformal_realisation.py#L1) · explicit_script_identifier

## 2026-06-14 (the two obligations collapse to ONE geometric premise v179)

[documents/changelog/sections/021-source.tex:156-175](../../../../documents/changelog/sections/021-source.tex#L156) · `section:359527c60ffa08a51bf0` · subsection

v179_conformal_realisation.py / \ (claim QGEO.CONF.01). Investigating the two residual premises left by v178 shows they are not independent — they collapse onto a single geometric premise (honest unification; the premise itself stays ). Marks's residual is not three independent assumptions: (1) genus- [formula in source] is P1 — the one-sided Gauss–Bonnet [formula in source] uses [formula in source] and [formula in s

Explicit source references:

- [verification/v158_fixed_point_stable.py](../../../../verification/v158_fixed_point_stable.py#L1) · explicit_script_identifier
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_script_identifier
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [verification/v178_marks_kernel_attempt.py](../../../../verification/v178_marks_kernel_attempt.py#L1) · explicit_script_identifier
- [verification/v58_seam_horizon_chain.py](../../../../verification/v58_seam_horizon_chain.py#L1) · explicit_script_identifier
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [verification/v179_conformal_realisation.py](../../../../verification/v179_conformal_realisation.py#L1) · explicit_file_citation
- [QGEO.CONF.01](../../../../verification/status_ledger.csv#L259) · explicit_claim_identifier · original status at linked ledger row
- [verification/v73_k_c3_half.py](../../../../verification/v73_k_c3_half.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [(* ---- (v158) free chiral c=8 fixed point is stable ---- *) Module[{hpsi, hcur, hquart, bosonic, relevant}, hpsi = 1/2; hcur = 2 hpsi; hquart = 4 hpsi; bosonic = {1, 2, 3}; (* integer-h bosonic chiral ops *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1421)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [(* ---- (v73) k=c3/2 forced: variational factor x Gauss-Bonnet topology; Fursaev-Solodukhin S=A/4 ---- *) checkExact["k=c3/2=1/(16pi)=(1/2)*(1/(|Z2|*2pi*chi(S2))), chi(S2)=2; Fursaev-Solodukhin 4pi k = 1/4", Module[{c3 = 1/(8 Pi), chi = 2, Z2 = 2}, (c3/2 == 1/(16 Pi)) && (c3 == 1/(Z2*2 Pi*chi)) && (4 Pi*(c3/2) == 1/4)]]; (* ---- (v74) compiler micro-lemmas: pencil differences 2->16->48; anchor QF 41-25=16 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L352)
- [(* ---- (v57) horizon cross-links: Jacobson 8pi, Hod ln(3), Hawking |W(D5)| ---- *) checkExact["c3=1/(8pi) Einstein/Jacobson: 1/(16pi)=c3/2; 1/4=1/|mu4|; 1/(2pi)=4c3", Simplify[1/(16 Pi) - (1/(8 Pi))/2] == 0 && 1/4 == 1/4 && Simplify[1/(2 Pi) - 4/(8 Pi)] == 0]; checkExact["Hod QNM omega_R/T_H = ln(3) = ln(N_fam); Hawking power denom 1920=|W(D5)|=2^4*5!", Nfam == 3 && 1920 == 2^4 * 5!]; (* ---- (v58) seam-horizon chain: one-sided Gauss-Bonnet, KMS, S_BH, RT in seam units ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L263)

## 2026-06-14 (an honest attempt at the two obligations v178 — deeper reduction, not closure)

[documents/changelog/sections/021-source.tex:176-197](../../../../documents/changelog/sections/021-source.tex#L176) · `section:c99473f27f0afd476930` · subsection

v178_marks_kernel_attempt.py / \ (claim QGEO.REDUCE.01). An honest attempt at QGEO.MARKS.01 and QGEO.KERNEL.01. These are genuine constructive-geometry/AQFT statements, not finite computations — neither is closed. What the module does is push each as far as computation allows: it closes the finite \ core of each and reduces each to one sharper premise. Marks core : given a genus- [formula in source] double with an or

Explicit source references:

- [QGEO.REDUCE.01](../../../../verification/status_ledger.csv#L258) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.MARKS.01](../../../../verification/status_ledger.csv#L256) · explicit_claim_identifier · original status at linked ledger row
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [QGEO.KERNEL.01](../../../../verification/status_ledger.csv#L257) · explicit_claim_identifier · original status at linked ledger row
- [verification/v178_marks_kernel_attempt.py](../../../../verification/v178_marks_kernel_attempt.py#L1) · explicit_script_identifier
- [verification/v162_seam_transport_identification.py](../../../../verification/v162_seam_transport_identification.py#L1) · explicit_script_identifier
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [verification/v158_fixed_point_stable.py](../../../../verification/v158_fixed_point_stable.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [(* ---- (v158) free chiral c=8 fixed point is stable ---- *) Module[{hpsi, hcur, hquart, bosonic, relevant}, hpsi = 1/2; hcur = 2 hpsi; hquart = 4 hpsi; bosonic = {1, 2, 3}; (* integer-h bosonic chiral ops *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1421)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-14 (QGEO proof tree v177 — the residual sharpened into two named obligations)

[documents/changelog/sections/021-source.tex:198-222](../../../../documents/changelog/sections/021-source.tex#L198) · `section:2f06593b8d87effdfab6` · subsection

v177_seam_marking_kernel.py / \ (claims QGEO.TREE.01, QGEO.MARKS.01, QGEO.KERNEL.01). A second external residual-class audit pointed out that the v176 statement takes the marks/ [formula in source] as a hypothesis — a near-circular trap. This module factors the central theorem honestly as [formula in source] and closes four nodes constructively (all validated symbolically before adoption): Uniform \ — an order- [form

Explicit source references:

- [verification/v168_qgeo_rigidity.py](../../../../verification/v168_qgeo_rigidity.py#L1) · explicit_script_identifier
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [verification/v137_qplus_cohomology.py](../../../../verification/v137_qplus_cohomology.py#L1) · explicit_script_identifier
- [QGEO.TREE.01](../../../../verification/status_ledger.csv#L255) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.MARKS.01](../../../../verification/status_ledger.csv#L256) · explicit_claim_identifier · original status at linked ledger row
- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [verification/v176_seam_collar_realisation.py](../../../../verification/v176_seam_collar_realisation.py#L1) · explicit_script_identifier
- [verification/v162_seam_transport_identification.py](../../../../verification/v162_seam_transport_identification.py#L1) · explicit_script_identifier
- [QGEO.KERNEL.01](../../../../verification/status_ledger.csv#L257) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v168) QGEO rigidity: mu4 square cross-ratio, mu4 characters = A3 exponents ---- *) Module[{mu4, cross, zz, eig, qspec}, mu4 = {1, I, -1, -I}; cross = Simplify[(mu4[[1]] - mu4[[3]]) (mu4[[2]] - mu4[[4]]) / ((mu4[[1]] - mu4[[4]]) (mu4[[2]] - mu4[[3]])) ]; (* omega_k = z^{k-1}/(z^4-1); pullback z->i z eigenvalue should be i^k *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1452)
- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [(* ---- (v137) Q+ cohomology grading ---- *) Module[{omchar, resok, qp, a0c}, omchar = Table[Simplify[((I z)^(k - 1)/((I z)^4 - 1)) I/(z^(k - 1)/(z^4 - 1))], {k, 3}]; resok = And @@ Flatten[Table[ Simplify[Residue[z^(k - 1)/(z^4 - 1), {z, zeta}] - zeta^k/4] === 0, {k, 3}, {zeta, {1, -1, I, -I}}]]; checkExact["v137 characters + residues: omega_k has mu_4 character i^k (k=1,2,3); residue vector = zeta^k/4 exactly", omchar === {I, -1, -I} && resok]; qp = DiagonalMatrix[3 {0, 1/3, 2/3} + 1]; a0c = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; checkExact["v137 grading: Spec(Q+) = {1,2,3}; cusp weights {0,1/3,2/3} = spec(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1086)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-13 (Seam Collar Realisation Theorem v176 — the one central proof obligation)

[documents/changelog/sections/021-source.tex:223-247](../../../../documents/changelog/sections/021-source.tex#L223) · `section:83cee7585db61c131b9a` · subsection

v176_seam_collar_realisation.py / \ (claim QGEO.REALIZE.02). Following an external residual-class audit, the single remaining structural item is formulated as one central theorem and certified as a reduction (not a fabricated proof). Theorem: given an oriented one-sided RP seam collar with a sheet-odd Calder\'on involution, faithful [formula in source] marks, four parabolic marks with [formula in source] decompositio

Explicit source references:

- [verification/v168_qgeo_rigidity.py](../../../../verification/v168_qgeo_rigidity.py#L1) · explicit_script_identifier
- [FR.KOIDE.03](../../../../verification/status_ledger.csv#L61) · explicit_claim_identifier · original status at linked ledger row
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v176_seam_collar_realisation.py](../../../../verification/v176_seam_collar_realisation.py#L1) · explicit_script_identifier
- [QGEO.REALIZE.02](../../../../verification/status_ledger.csv#L254) · explicit_claim_identifier · original status at linked ledger row
- [verification/v137_qplus_cohomology.py](../../../../verification/v137_qplus_cohomology.py#L1) · explicit_script_identifier
- [verification/v162_seam_transport_identification.py](../../../../verification/v162_seam_transport_identification.py#L1) · explicit_script_identifier
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v137) Q+ cohomology grading ---- *) Module[{omchar, resok, qp, a0c}, omchar = Table[Simplify[((I z)^(k - 1)/((I z)^4 - 1)) I/(z^(k - 1)/(z^4 - 1))], {k, 3}]; resok = And @@ Flatten[Table[ Simplify[Residue[z^(k - 1)/(z^4 - 1), {z, zeta}] - zeta^k/4] === 0, {k, 3}, {zeta, {1, -1, I, -I}}]]; checkExact["v137 characters + residues: omega_k has mu_4 character i^k (k=1,2,3); residue vector = zeta^k/4 exactly", omchar === {I, -1, -I} && resok]; qp = DiagonalMatrix[3 {0, 1/3, 2/3} + 1]; a0c = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; checkExact["v137 grading: Spec(Q+) = {1,2,3}; cusp weights {0,1/3,2/3} = spec(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1086)
- [(* ---- (v168) QGEO rigidity: mu4 square cross-ratio, mu4 characters = A3 exponents ---- *) Module[{mu4, cross, zz, eig, qspec}, mu4 = {1, I, -1, -I}; cross = Simplify[(mu4[[1]] - mu4[[3]]) (mu4[[2]] - mu4[[4]]) / ((mu4[[1]] - mu4[[4]]) (mu4[[2]] - mu4[[3]])) ]; (* omega_k = z^{k-1}/(z^4-1); pullback z->i z eigenvalue should be i^k *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1452)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)

## 2026-06-13 (Zenodo release 5.1 (rev 105) — v174 + v175 + doc refresh)

[documents/changelog/sections/021-source.tex:248-259](../../../../documents/changelog/sections/021-source.tex#L248) · `section:63da5b8be1d09edb111a` · subsection

Published to Zenodo. Version 5.1 (rev 105) of the ten-PDF document set (introduction, origin_theory, tfpt_1–5, horizon, research_contracts, changelog) was published as a new version of the TFPT deposit — record 20681451, DOI 10.5281/zenodo.20681451. This version carries the AQFT closure round (v170–v175): the seam Fock-space readings and the heavy-artillery discharge of net existence [formula in source] full-cone ref

Explicit source references:

- [verification/v174_seam_fock_readings.py](../../../../verification/v174_seam_fock_readings.py#L1) · explicit_script_identifier
- [verification/v170_diamond_slice_compression.py](../../../../verification/v170_diamond_slice_compression.py#L1) · explicit_script_identifier
- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v170) E8 slice compression: seven slices from two alphabets ---- *) Module[{p, p0, p1, p2, p3, Delta, e1, e2, dimSp, dQ, dK, dR, dC, dL, dF, slices}, p = Table[2 + 2^n, {n, 0, 3}]; {p0, p1, p2, p3} = p; Delta = p0 + p3; e1 = 4; e2 = 5; dimSp = 16; {dQ, dK, dR, dC, dL, dF} = {3, 4, 8, 14, 20, 32}; slices = { p0 p1 p3 + p1 dF, (p1 p3 + e2) + (p0 p1 + p0) + p2 p3 + 2 e1 dimSp, p2 Delta + dR + 81 + 81, (p0 p1 p3 + Delta) + p0 + dR dC, (p1^2 + p2^2) + dC + Delta dC, 2 p1 p2 + 4 e2 p3, dK dL + 2 p2 dC}; checkExact["v170 E8 slice compression: P=(3,4,6,10), D=(3,4,8,14,20,32) sum 81=N_fam^4; K4 edges {12,18,30,24,40,60}; all seven E8 slices = 248; 78 = p2 Delta = dim E6", p === {3, 4, 6, 10} && Total[{dQ, dK, dR, dC, dL, dF}] == 81 && {p0 p1, p0 p2, p0 p3, p1 p2, p1 p3, p2 p3} === {12, 18, 30, 24, 40, 60} && AllTrue[slices, # == 248 &] && p2 Delta == 78]; ]; (* ---- (v171) atomic OS moment + Sugawara gap safety ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1465)
- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [(* ---- (v174) seam Fock-space readings: cone compression, Witten index, g-theorem ---- *) Module[{cone, blocks, trunc, disc, cUV, cIR}, cone = 2^15; blocks = {Binomial[16, 4], Binomial[16, 6], Binomial[16, 8]}; trunc = Sum[Binomial[4, k], {k, 0, 2}]; (* 11 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1509)

## 2026-06-13 (the heavy artillery v175: net existence + full-cone RP discharged to [E])

[documents/changelog/sections/021-source.tex:260-287](../../../../documents/changelog/sections/021-source.tex#L260) · `section:e16d657ff22e85d37e54` · subsection

v175_net_existence_full_cone.py / \ (claim QFT.NETRP.01). The two structural residuals that the premise-(A) chain had relocated to already-open items — [formula in source] net existence and full-cone reflection positivity — are now discharged to a theorem, leaving the seam realisation as the single irreducible open premise (nothing fabricated). (1) Full-cone RP for all [formula in source] : the CAR second-quantisatio

Explicit source references:

- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [verification/v175_net_existence_full_cone.py](../../../../verification/v175_net_existence_full_cone.py#L1) · explicit_script_identifier
- [QFT.NETRP.01](../../../../verification/status_ledger.csv#L288) · explicit_claim_identifier · original status at linked ledger row
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [verification/v161_one_particle_reduction.py](../../../../verification/v161_one_particle_reduction.py#L1) · explicit_script_identifier
- [verification/v168_qgeo_rigidity.py](../../../../verification/v168_qgeo_rigidity.py#L1) · explicit_script_identifier
- [verification/v83_e8net_holomorphic_uniqueness.py](../../../../verification/v83_e8net_holomorphic_uniqueness.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v168) QGEO rigidity: mu4 square cross-ratio, mu4 characters = A3 exponents ---- *) Module[{mu4, cross, zz, eig, qspec}, mu4 = {1, I, -1, -I}; cross = Simplify[(mu4[[1]] - mu4[[3]]) (mu4[[2]] - mu4[[4]]) / ((mu4[[1]] - mu4[[4]]) (mu4[[2]] - mu4[[3]])) ]; (* omega_k = z^{k-1}/(z^4-1); pullback z->i z eigenvalue should be i^k *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1452)
- [(* ---- (v175) net existence + full-cone RP: E8 Cartan even unimodular, character order 5, Gamma(t) functoriality integers ---- *) Module[{cartan, det, evenDiag, sig3, E4, prodv, chi, c5, fockDim, fixedMult, gap, pairCount}, (* E8 Cartan matrix (Bourbaki): even (diag 2) and det 1 = unique rank-8 even unimodular lattice *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1522)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)

## 2026-06-13 (seam Fock-space readings v174: CAR cone, Witten index, g-theorem)

[documents/changelog/sections/021-source.tex:288-303](../../../../documents/changelog/sections/021-source.tex#L288) · `section:190cc30037d75411e25f` · subsection

v174_seam_fock_readings.py \ (claim QFT.FOCK.01). Three more exact audit bridges from the same source note. (1) CAR cone compression: the even CAR algebra of the 16 seam Majoranas has [formula in source] directions, but a quasi-free Bogoliubov transport reduces the whole cone to a [formula in source] -dim one-particle problem ( [formula in source] ) — the explicit count behind v161. (2) Witten index [formula in sourc

Explicit source references:

- [verification/v158_fixed_point_stable.py](../../../../verification/v158_fixed_point_stable.py#L1) · explicit_script_identifier
- [QFT.FOCK.01](../../../../verification/status_ledger.csv#L287) · explicit_claim_identifier · original status at linked ledger row
- [verification/v157_rigid_fixed_point.py](../../../../verification/v157_rigid_fixed_point.py#L1) · explicit_script_identifier
- [verification/v161_one_particle_reduction.py](../../../../verification/v161_one_particle_reduction.py#L1) · explicit_script_identifier
- [verification/v174_seam_fock_readings.py](../../../../verification/v174_seam_fock_readings.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v158) free chiral c=8 fixed point is stable ---- *) Module[{hpsi, hcur, hquart, bosonic, relevant}, hpsi = 1/2; hcur = 2 hpsi; hquart = 4 hpsi; bosonic = {1, 2, 3}; (* integer-h bosonic chiral ops *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1421)
- [(* ---- (v157) freeness as the rigid boundary fixed point ---- *) Module[{symbolHomog, c3}, symbolHomog = Simplify[Abs[lam kk] - lam Abs[kk], (lam | kk) \[Element] Reals && lam > 0]; c3 = 1/(2*2 Pi*2); (* 1/(|Z2| * 2pi * chi(S^2)) , chi=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1411)
- [(* ---- (v174) seam Fock-space readings: cone compression, Witten index, g-theorem ---- *) Module[{cone, blocks, trunc, disc, cUV, cIR}, cone = 2^15; blocks = {Binomial[16, 4], Binomial[16, 6], Binomial[16, 8]}; trunc = Sum[Binomial[4, k], {k, 0, 2}]; (* 11 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1509)

## 2026-06-13 (CFT/QFT bridges: slice compression v170, OS moment v171, trace-anomaly seed v172, Pfaffian CP v173)

[documents/changelog/sections/021-source.tex:304-333](../../../../documents/changelog/sections/021-source.tex#L304) · `section:e36b11d50051a79291df` · subsection

v170_diamond_slice_compression.py \ (claim E8.SLICE.01). E8 Slice Compression Lemma: the seven [formula in source] audit slices are one projection of two alphabets — anchor power sums [formula in source] ( [formula in source] ) and Sheet-Diamond determinants [formula in source] summing to [formula in source] . All seven [formula in source] -slices, the [formula in source] edge graph, and the row-budget cross [formula

Explicit source references:

- [QFT.OSMOMENT.01](../../../../verification/status_ledger.csv#L284) · explicit_claim_identifier · original status at linked ledger row
- [SEED.ANOMALY.01](../../../../verification/status_ledger.csv#L285) · explicit_claim_identifier · original status at linked ledger row
- [verification/v171_os_moment_cluster.py](../../../../verification/v171_os_moment_cluster.py#L1) · explicit_file_citation
- [verification/v172_trace_anomaly_seed.py](../../../../verification/v172_trace_anomaly_seed.py#L1) · explicit_file_citation
- [verification/v170_diamond_slice_compression.py](../../../../verification/v170_diamond_slice_compression.py#L1) · explicit_file_citation
- [verification/v173_pfaffian_cp_car.py](../../../../verification/v173_pfaffian_cp_car.py#L1) · explicit_file_citation
- [E8.SLICE.01](../../../../verification/status_ledger.csv#L283) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.STRONGCP.02](../../../../verification/status_ledger.csv#L286) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v172) trace-anomaly seed 4/3 + shared integer 7 ---- *) Module[{cc, chi, anomaly, half, b3, scal, vw}, cc = 8; chi = 2; anomaly = cc chi/6; (* 8/3 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1496)
- [(* ---- (v170) E8 slice compression: seven slices from two alphabets ---- *) Module[{p, p0, p1, p2, p3, Delta, e1, e2, dimSp, dQ, dK, dR, dC, dL, dF, slices}, p = Table[2 + 2^n, {n, 0, 3}]; {p0, p1, p2, p3} = p; Delta = p0 + p3; e1 = 4; e2 = 5; dimSp = 16; {dQ, dK, dR, dC, dL, dF} = {3, 4, 8, 14, 20, 32}; slices = { p0 p1 p3 + p1 dF, (p1 p3 + e2) + (p0 p1 + p0) + p2 p3 + 2 e1 dimSp, p2 Delta + dR + 81 + 81, (p0 p1 p3 + Delta) + p0 + dR dC, (p1^2 + p2^2) + dC + Delta dC, 2 p1 p2 + 4 e2 p3, dK dL + 2 p2 dC}; checkExact["v170 E8 slice compression: P=(3,4,6,10), D=(3,4,8,14,20,32) sum 81=N_fam^4; K4 edges {12,18,30,24,40,60}; all seven E8 slices = 248; 78 = p2 Delta = dim E6", p === {3, 4, 6, 10} && Total[{dQ, dK, dR, dC, dL, dF}] == 81 && {p0 p1, p0 p2, p0 p3, p1 p2, p1 p3, p2 p3} === {12, 18, 30, 24, 40, 60} && AllTrue[slices, # == 248 &] && p2 Delta == 78]; ]; (* ---- (v171) atomic OS moment + Sugawara gap safety ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1465)

## 2026-06-13 (Zenodo release 5.1 (rev 97))

[documents/changelog/sections/021-source.tex:334-343](../../../../documents/changelog/sections/021-source.tex#L334) · `section:e7ac5f2397b1b7d72c99` · subsection

Published to Zenodo. Version 5.1 (rev 97) of the ten-PDF document set (introduction, origin_theory, tfpt_1–5, horizon, research_contracts, changelog) was published as a new version of the TFPT deposit — record 20678568, DOI 10.5281/zenodo.20678568. The uploader's DEFAULT_RECORD_ID was advanced to the new record for the next release. Also fixed build.sh zenodo on macOS bash 3.2 (empty-array expansion under set -u).

## 2026-06-13 (QGEO rigidity theorem v168 + [formula in source] leptogenesis interface v169)

[documents/changelog/sections/021-source.tex:344-369](../../../../documents/changelog/sections/021-source.tex#L344) · `section:b3882fb1623949f1d1b5` · subsection

v168_qgeo_rigidity.py / (claims QGEO.RIGID.01, QGEO.REALIZE.01). Hardens the finite half of the one remaining Tier-1 hinge GATE.QGEO (the seam [formula in source] flavour [formula in source] horizon identification). Exact, machine-checked: [formula in source] has cross-ratio [formula in source] and a faithful M\"obius stabiliser of order [formula in source] ; [formula in source] has rank [formula in source] ; and the

Explicit source references:

- [verification/v168_qgeo_rigidity.py](../../../../verification/v168_qgeo_rigidity.py#L1) · explicit_file_citation
- [QGEO.RIGID.01](../../../../verification/status_ledger.csv#L252) · explicit_claim_identifier · original status at linked ledger row
- [verification/v167_inventory_post_closure.py](../../../../verification/v167_inventory_post_closure.py#L1) · explicit_script_identifier
- [FR.ETAB.02](../../../../verification/status_ledger.csv#L282) · explicit_claim_identifier · original status at linked ledger row
- [verification/v169_etaB_boltzmann_interface.py](../../../../verification/v169_etaB_boltzmann_interface.py#L1) · explicit_script_identifier
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [(* ---- (v168) QGEO rigidity: mu4 square cross-ratio, mu4 characters = A3 exponents ---- *) Module[{mu4, cross, zz, eig, qspec}, mu4 = {1, I, -1, -I}; cross = Simplify[(mu4[[1]] - mu4[[3]]) (mu4[[2]] - mu4[[4]]) / ((mu4[[1]] - mu4[[4]]) (mu4[[2]] - mu4[[3]])) ]; (* omega_k = z^{k-1}/(z^4-1); pullback z->i z eigenvalue should be i^k *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1452)

## 2026-06-13 (Higgs quartic from the free seam: SM near-criticality explained, v166)

[documents/changelog/sections/022-source.tex:1-21](../../../../documents/changelog/sections/022-source.tex#L1) · `section:b0bd96461774b2724095` · subsection

v166_higgs_free_seam.py / (claim HIGGS.FREESEAM.01). A new prediction tying the Higgs mass to premise (A). The seam UV is the free chiral [formula in source] fixed point (v158, Gaussian, no relevant/marginal interactions), so the one marginal SM scalar coupling vanishes there: [formula in source] and [formula in source] — the Shaposhnikov–Wetterich double-criticality, here derived from the free seam, not assumed. Int

Explicit source references:

- [verification/pyrate/sm_higgs_betas.txt](../../../../verification/pyrate/sm_higgs_betas.txt#L1) · explicit_file_citation
- [verification/v166_higgs_free_seam.py](../../../../verification/v166_higgs_free_seam.py#L1) · explicit_script_identifier
- [HIGGS.FREESEAM.01](../../../../verification/status_ledger.csv#L251) · explicit_claim_identifier · original status at linked ledger row
- [verification/v158_fixed_point_stable.py](../../../../verification/v158_fixed_point_stable.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v158) free chiral c=8 fixed point is stable ---- *) Module[{hpsi, hcur, hquart, bosonic, relevant}, hpsi = 1/2; hcur = 2 hpsi; hquart = 4 hpsi; bosonic = {1, 2, 3}; (* integer-h bosonic chiral ops *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1421)

## 2026-06-13 (PyR@TE [formula in source] follow-ups: flavor scale-tagging v163, QCD scale v164)

[documents/changelog/sections/022-source.tex:22-46](../../../../documents/changelog/sections/022-source.tex#L22) · `section:593d2f8d7dd5d5b3f6dd` · subsection

v163_rg_stability_flavor.py / (claim FLAV.RGSTAB.01). Scale-tagging of the flavor sector. The lepton-mixing seeds ( [formula in source] , [formula in source] ) are RG-stable: the PMNS running is [formula in source] -suppressed (the only mixing-rotating Yukawa term is [formula in source] , PyR@TE SM RGEs), so [formula in source] and [formula in source] — two to three orders below precision. Seam value [formula in sour

Explicit source references:

- [verification/pyrate/sm_yukawa_betas.txt](../../../../verification/pyrate/sm_yukawa_betas.txt#L1) · explicit_file_citation
- [QCD.LAMBDA.01](../../../../verification/status_ledger.csv#L250) · explicit_claim_identifier · original status at linked ledger row
- [verification/v164_qcd_scale.py](../../../../verification/v164_qcd_scale.py#L1) · explicit_file_citation
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_script_identifier
- [FLAV.RGSTAB.01](../../../../verification/status_ledger.csv#L249) · explicit_claim_identifier · original status at linked ledger row
- [verification/v163_rg_stability_flavor.py](../../../../verification/v163_rg_stability_flavor.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)

## 2026-06-13 (PyR@TE external cross-check of the [formula in source] gauge inputs — v159)

[documents/changelog/sections/022-source.tex:47-71](../../../../documents/changelog/sections/022-source.tex#L47) · `section:d1579fbe47c96d49e4e0` · subsection

New module v159_pyrate_gauge_crosscheck.py / (claim EM.BUDGET.02). The one-loop gauge coefficients used by the transfer functor are confirmed by an independent third-party RGE generator. Feeding the carrier / Standard-Model field content into the textbook one-loop formula (GUT normalisation) gives [formula in source] , and PyR@TE\,3 ( arXiv:2007.12700, github.com/LSartore/pyrate) writes [formula in source] , [formula

Explicit source references:

- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_script_identifier
- [verification/pyrate/sm_gauge_betas.txt](../../../../verification/pyrate/sm_gauge_betas.txt#L1) · explicit_file_citation
- [EM.BUDGET.02](../../../../verification/status_ledger.csv#L248) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)

## 2026-06-13 (terminal residual inventory: (A) no longer a structural class; one hinge + F_transfer + irreducible core, v167)

[documents/changelog/sections/022-source.tex:72-90](../../../../documents/changelog/sections/022-source.tex#L72) · `section:a3835ef2388efb1a54cd` · subsection

New module v167_inventory_post_closure.py / . The terminal residual inventory (line v105 [formula in source] v123 [formula in source] v167), re-pinned after the (A)-chain. With (A) discharged ( GATE.METRIC.16–19) the v123 five structural classes collapse: the seam clock (R1), the index- [formula in source] net (R2) and the [formula in source] -realisation (R5) all merge into one Tier-1 hinge — the seam [formula in so

Explicit source references:

- [verification/v105_residual_inventory.py](../../../../verification/v105_residual_inventory.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [SYNTH.INVENTORY.03](../../../../verification/status_ledger.csv#L208) · explicit_claim_identifier · original status at linked ledger row
- [GATE.METRIC.16](../../../../verification/status_ledger.csv#L244) · explicit_claim_identifier · original status at linked ledger row
- [verification/v152_norm_is_anchor.py](../../../../verification/v152_norm_is_anchor.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v167_inventory_post_closure.py](../../../../verification/v167_inventory_post_closure.py#L1) · explicit_script_identifier
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [verification/v123_inventory_update.py](../../../../verification/v123_inventory_update.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [(* ---- (v205) GRAV.XI.01: xi = c3/phi_tree = 3/4, the independent gravitational 3/4 ---- *) Module[{c3, phitree}, c3 = 1/(8 Pi); phitree = 1/(6 Pi); checkExact["v205 GRAV.XI.01: the torsion-compression factor xi = c3/phi_tree = (1/8pi)/(1/6pi) = 3/4 EXACTLY; the Einstein-limit reduction 8 pi c3^2 = c3 makes G an output (xi = c3/phi0); and 3/4 = 12 pi (c3/2) = ln(m/mu) = q(A3) (v152) -- the torsion-compression and the gapped EH replica are two independent appearances of the same gravitational 3/4", Simplify[c3/phitree - 3/4] == 0 && Simplify[8 Pi c3^2 - c3] == 0 && Simplify[12 Pi (c3/2) - 3/4] == 0]; ]; (* ---- (v208) HOR.BHTHERMO.01: scalaron Wald factor + modular 2 pi = 1/(4 c3) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1708)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)

## 2026-06-13 (premise A maximal honest closure: A2 by assembly, R1 = GATE.QGEO, zero independent open gates, v165)

[documents/changelog/sections/022-source.tex:91-112](../../../../documents/changelog/sections/022-source.tex#L91) · `section:55b733511958e907bad8` · subsection

New module v165_premise_a_closure.py / . Pins the two residual gates of the v160– v162 (A)-chain to their floor. [formula in source] (net existence) closes by assembly of established mathematics : the [formula in source] free Majoranas give a free-fermion conformal net (Buchholz–Mack–Todorov), the holomorphic [formula in source] lattice net is [formula in source] (Frenkel–Kac–Segal / Dong–Xu / Kawahigashi–Longo), the

Explicit source references:

- [verification/v165_premise_a_closure.py](../../../../verification/v165_premise_a_closure.py#L1) · explicit_script_identifier
- [verification/v157_rigid_fixed_point.py](../../../../verification/v157_rigid_fixed_point.py#L1) · explicit_script_identifier
- [GATE.METRIC.19](../../../../verification/status_ledger.csv#L247) · explicit_claim_identifier · original status at linked ledger row
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [verification/v116_resonance_uniqueness.py](../../../../verification/v116_resonance_uniqueness.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v137_qplus_cohomology.py](../../../../verification/v137_qplus_cohomology.py#L1) · explicit_script_identifier
- [verification/v115_anchor_residue.py](../../../../verification/v115_anchor_residue.py#L1) · explicit_script_identifier
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [verification/v162_seam_transport_identification.py](../../../../verification/v162_seam_transport_identification.py#L1) · explicit_script_identifier
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v115) anchor residue ---- The [N] Riemann-Hilbert parts (scipy ODE monodromy of the Fuchsian system, multi-seed uniqueness scan) are Python-only by convention; the exact lemmas are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L668)
- [(* ---- (v137) Q+ cohomology grading ---- *) Module[{omchar, resok, qp, a0c}, omchar = Table[Simplify[((I z)^(k - 1)/((I z)^4 - 1)) I/(z^(k - 1)/(z^4 - 1))], {k, 3}]; resok = And @@ Flatten[Table[ Simplify[Residue[z^(k - 1)/(z^4 - 1), {z, zeta}] - zeta^k/4] === 0, {k, 3}, {zeta, {1, -1, I, -I}}]]; checkExact["v137 characters + residues: omega_k has mu_4 character i^k (k=1,2,3); residue vector = zeta^k/4 exactly", omchar === {I, -1, -I} && resok]; qp = DiagonalMatrix[3 {0, 1/3, 2/3} + 1]; a0c = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; checkExact["v137 grading: Spec(Q+) = {1,2,3}; cusp weights {0,1/3,2/3} = spec(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1086)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [(* ---- (v157) freeness as the rigid boundary fixed point ---- *) Module[{symbolHomog, c3}, symbolHomog = Simplify[Abs[lam kk] - lam Abs[kk], (lam | kk) \[Element] Reals && lam > 0]; c3 = 1/(2*2 Pi*2); (* 1/(|Z2| * 2pi * chi(S^2)) , chi=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1411)
- [(* ---- (v116) resonance theorem ---- The [N] falsification control (scipy ODE) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L687)

## 2026-06-13 (the final identification: premise A factors into the already-open A2 + R1, no new open content, v162)

[documents/changelog/sections/022-source.tex:113-133](../../../../documents/changelog/sections/022-source.tex#L113) · `section:cc5f650209aae2bdc4e6` · subsection

New module v162_seam_transport_identification.py / . Pushes the v161 residual as far as it rigorously goes and shows it carries no new open content. The one-particle symbol splits into a gap value [formula in source] and a fixed space [formula in source] . [formula in source] is forced: a [formula in source] -equivariant generator is diagonal in the cusp basis (the deck average is the diagonal projection, [formula in

Explicit source references:

- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [verification/v137_qplus_cohomology.py](../../../../verification/v137_qplus_cohomology.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [verification/v115_anchor_residue.py](../../../../verification/v115_anchor_residue.py#L1) · explicit_script_identifier
- [verification/v162_seam_transport_identification.py](../../../../verification/v162_seam_transport_identification.py#L1) · explicit_file_citation
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [GATE.METRIC.18](../../../../verification/status_ledger.csv#L246) · explicit_claim_identifier · original status at linked ledger row
- [verification/v161_one_particle_reduction.py](../../../../verification/v161_one_particle_reduction.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v137) Q+ cohomology grading ---- *) Module[{omchar, resok, qp, a0c}, omchar = Table[Simplify[((I z)^(k - 1)/((I z)^4 - 1)) I/(z^(k - 1)/(z^4 - 1))], {k, 3}]; resok = And @@ Flatten[Table[ Simplify[Residue[z^(k - 1)/(z^4 - 1), {z, zeta}] - zeta^k/4] === 0, {k, 3}, {zeta, {1, -1, I, -I}}]]; checkExact["v137 characters + residues: omega_k has mu_4 character i^k (k=1,2,3); residue vector = zeta^k/4 exactly", omchar === {I, -1, -I} && resok]; qp = DiagonalMatrix[3 {0, 1/3, 2/3} + 1]; a0c = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; checkExact["v137 grading: Spec(Q+) = {1,2,3}; cusp weights {0,1/3,2/3} = spec(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1086)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [(* ---- (v115) anchor residue ---- The [N] Riemann-Hilbert parts (scipy ODE monodromy of the Fuchsian system, multi-seed uniqueness scan) are Python-only by convention; the exact lemmas are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L668)

## 2026-06-13 (the cone reduces to one particle: premise A's scope premise discharged to a 16-dim statement, v161)

[documents/changelog/sections/022-source.tex:134-155](../../../../documents/changelog/sections/022-source.tex#L134) · `section:901199b7ffce4a10a268` · subsection

New module v161_one_particle_reduction.py / . Discharges the scope premise of v160 (``the transport is gapped on the full Schwinger cone'') via Bogoliubov second quantisation. A quasi-free transport is [formula in source] , the second quantisation of a one-particle contraction [formula in source] on the [formula in source] -dim Majorana space; [formula in source] acts on the degree- [formula in source] correlator sec

Explicit source references:

- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [GATE.METRIC.17](../../../../verification/status_ledger.csv#L245) · explicit_claim_identifier · original status at linked ledger row
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v158_fixed_point_stable.py](../../../../verification/v158_fixed_point_stable.py#L1) · explicit_script_identifier
- [verification/v161_one_particle_reduction.py](../../../../verification/v161_one_particle_reduction.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v158) free chiral c=8 fixed point is stable ---- *) Module[{hpsi, hcur, hquart, bosonic, relevant}, hpsi = 1/2; hcur = 2 hpsi; hquart = 4 hpsi; bosonic = {1, 2, 3}; (* integer-h bosonic chiral ops *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1421)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)

## 2026-06-13 (premise A as a conditional fixed-point theorem; the load relocates to one scope premise, v160)

[documents/changelog/sections/022-source.tex:156-178](../../../../documents/changelog/sections/022-source.tex#L156) · `section:c39fabd7834a6c050a87` · subsection

New module v160_seam_gaussianity_from_pf.py / . Formalises the proposed closure of premise (A) (``the seam bulk is a reflection-positive free field'') as a fixed-point theorem and types it honestly. The exact parts: (1) a quasi-free state has all higher connected cumulants [formula in source] — verified by the signed set-partition/Pfaffian moment [formula in source] cumulant inversion on a concrete pure Majorana cova

Explicit source references:

- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_file_citation
- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [GATE.METRIC.16](../../../../verification/status_ledger.csv#L244) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)

## 2026-06-13 (changelog date-order audit + reorder pass)

[documents/changelog/sections/022-source.tex:179-188](../../../../documents/changelog/sections/022-source.tex#L179) · `section:841d8f1544a52bd38c3f` · subsection

Changelog sort enforced. audit_sync.py now checks that every dated subsection\*\YYYY-MM-DD...\ block in this file is non-increasing (newest first; range titles such as 2026-06-07 / 2026-06-08 sort by the later date). A manual prepend had left five 2026-06-12 entries above seven 2026-06-13 blocks — reordered; future mis-sorts fail build.sh audit as [B.changelog].

Explicit source references:

- [verification/audit_sync.py](../../../../verification/audit_sync.py#L1) · explicit_file_citation

## 2026-06-13 (premise A: the destination fixed point is provably stable, v158)

[documents/changelog/sections/022-source.tex:189-203](../../../../documents/changelog/sections/022-source.tex#L189) · `section:3683cb3ca5b3f7afe565` · subsection

The free chiral [formula in source] fixed point is provably stable ( v158, exact dimension count). The finite core of (A)'s ``reaches-the-fixed-point'' residual: the chiral Majorana has [formula in source] , the bilinear current [formula in source] , the quartic [formula in source] . The relevant window [formula in source] for bosonic deformations is empty, the [formula in source] currents are chiral ( v157, not [for

Explicit source references:

- [GATE.METRIC.15](../../../../verification/status_ledger.csv#L243) · explicit_claim_identifier · original status at linked ledger row
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v157_rigid_fixed_point.py](../../../../verification/v157_rigid_fixed_point.py#L1) · explicit_script_identifier
- [verification/v158_fixed_point_stable.py](../../../../verification/v158_fixed_point_stable.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v157) freeness as the rigid boundary fixed point ---- *) Module[{symbolHomog, c3}, symbolHomog = Simplify[Abs[lam kk] - lam Abs[kk], (lam | kk) \[Element] Reals && lam > 0]; c3 = 1/(2*2 Pi*2); (* 1/(|Z2| * 2pi * chi(S^2)) , chi=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1411)
- [(* ---- (v158) free chiral c=8 fixed point is stable ---- *) Module[{hpsi, hcur, hquart, bosonic, relevant}, hpsi = 1/2; hcur = 2 hpsi; hquart = 4 hpsi; bosonic = {1, 2, 3}; (* integer-h bosonic chiral ops *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1421)

## 2026-06-13 (premise A reframed: freeness is a rigid boundary fixed point, v157)

[documents/changelog/sections/022-source.tex:204-220](../../../../documents/changelog/sections/022-source.tex#L204) · `section:dd21f4d89cdafe68cd70` · subsection

The free-bulk premise becomes a fixed-point property ( v157, simplicity-first). Instead of postulating Gaussianity, three facts click: (i) the DtN/Calder\'on symbol is universally [formula in source] (Lee–Uhlmann — order- [formula in source] [formula in source] DO, principal symbol [formula in source] ; interactions live in the irrelevant lower-order symbol), so the free dispersion is bulk-detail-independent; (ii) a 

Explicit source references:

- [GATE.METRIC.14](../../../../verification/status_ledger.csv#L242) · explicit_claim_identifier · original status at linked ledger row
- [verification/v157_rigid_fixed_point.py](../../../../verification/v157_rigid_fixed_point.py#L1) · explicit_script_identifier
- [verification/v83_e8net_holomorphic_uniqueness.py](../../../../verification/v83_e8net_holomorphic_uniqueness.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v157) freeness as the rigid boundary fixed point ---- *) Module[{symbolHomog, c3}, symbolHomog = Simplify[Abs[lam kk] - lam Abs[kk], (lam | kk) \[Element] Reals && lam > 0]; c3 = 1/(2*2 Pi*2); (* 1/(|Z2| * 2pi * chi(S^2)) , chi=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1411)

## 2026-06-13 (Route 3: the seam net constructed and [formula in source] verified, v156)

[documents/changelog/sections/022-source.tex:221-238](../../../../documents/changelog/sections/022-source.tex#L221) · `section:fc84e3c0ee4eb2d211d7` · subsection

The constructive route carried to its exact endpoint ( v156). `` [formula in source] '' is no longer an assertion: the chiral seam net is built explicitly and the identification checked. (a) The Dirichlet-to-Neumann (Calder\'on) operator of the [formula in source] d Laplacian is the free chiral dispersion [formula in source] (harmonic extension [formula in source] ); (b) [formula in source] free Majoranas give [formu

Explicit source references:

- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [GATE.METRIC.13](../../../../verification/status_ledger.csv#L241) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)

## 2026-06-13 (the seam-side identification reduced to one shared premise, v155)

[documents/changelog/sections/022-source.tex:239-257](../../../../documents/changelog/sections/022-source.tex#L239) · `section:4b70b6153a1845cabead` · subsection

[formula in source] 's last premise reduces to a single shared physical premise ( v155, Python-only). The seam-side identification of the Simple-Current Extension Theorem ( v154) splits ( v110) into (a) ``the Calder\'on involution is sheet-odd'' (the double-cover deck, structural) and (b) ``the seam [formula in source] -point kernel is quasi-free''. Part (b) is not independent: the boundary marginal of a reflection-p

Explicit source references:

- [verification/v150_replica_eh_model.py](../../../../verification/v150_replica_eh_model.py#L1) · explicit_script_identifier
- [verification/v110_calderon_sheet.py](../../../../verification/v110_calderon_sheet.py#L1) · explicit_script_identifier
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v59_area_law_evidence.py](../../../../verification/v59_area_law_evidence.py#L1) · explicit_script_identifier
- [verification/v151_bfk_split.py](../../../../verification/v151_bfk_split.py#L1) · explicit_script_identifier
- [GATE.METRIC.12](../../../../verification/status_ledger.csv#L240) · explicit_claim_identifier · original status at linked ledger row
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v150) replica EH model ---- *) Module[{cdef, imgOK, convOK, mellin, dz0, dC, target}, cdef[g_] := (1/12) (2 Pi/g - g/(2 Pi)); imgOK = And @@ Table[ FullSimplify[Sum[1/Sin[Pi k/n]^2, {k, 1, n - 1}] - (n^2 - 1)/3] === 0, {n, 2, 8}]; convOK = Simplify[(1/(4 nn)) (nn^2 - 1)/3 - cdef[2 Pi/nn]] === 0; mellin = Integrate[tt^(ss - 1) Exp[-mm^2 tt], {tt, 0, Infinity}, Assumptions -> ss > 0 && mm > 0]; dz0 = D[mm^(-2 ss), ss] /. ss -> 0; dC = D[cdef[gg], gg] /. gg -> 2 Pi; target = Simplify[12 Pi (1/2) (1/(8 Pi))]; checkExact["v150 replica EH model: image sum exact (N=2..8); orbifold deficit = C(2pi/N); Mellin Delta-zeta(s) = C m^-2s => Delta log det' = 2C ln m (cutoff-independent); dC/dgamma|_{2pi} = -1/(12pi) => EH form with k = ln m/(12pi); target k = c3/2 <=> ln m = 3/4 = q(A3)", imgOK && convOK && Simplify[mellin - Gamma[ss] mm^(-2 ss)] === 0 && Simplify[dz0 + 2 Log[mm]] === 0 && Simplify[dC + 1/(12 Pi)] === 0 && target == 3/4]; ]; (* ---- (v151) BFK split ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1321)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v109) sheet pairing ---- *) Module[{splus, sminus, vecw, lamW, addW, crossT, formsEven, diagT, formsOdd, zmult}, splus = Select[Tuples[{1/2, -1/2}, 5], EvenQ[Count[#, -1/2]] &]; sminus = Select[Tuples[{1/2, -1/2}, 5], OddQ[Count[#, -1/2]] &]; vecw = Flatten[Table[s UnitVector[5, i], {i, 5}, {s, {1, -1}}], 1]; lamW[k_] := If[k == 0, {ConstantArray[0, 5]}, Total /@ Subsets[vecw, {k}]]; checkExact["v109 no scalar within a sheet: zero-weight mult of S+xS+ and S-xS- is 0", (Count[Flatten[Outer[Plus, splus, splus, 1], 1], ConstantArray[0, 5]] == 0) && (Count[Flatten[Outer[Plus, sminus, sminus, 1], 1], ConstantArray[0, 5]] == 0)]; crossT = Sort[Flatten[Outer[Plus, splus, sminus, 1], 1]]; checkExact["v109 cross-sheet zero-weight mult = 16 = 1+5+10 (Pascal triple)", Count[crossT, ConstantArray[0, 5]] == 16]; formsEven = Sort[Join[lamW[0], lamW[2], lamW[4]]]; checkExact["v109 EXACT multiset: S+xS- = Lambda^0+Lambda^2+Lambda^4 (256 = 1+45+210)", crossT === formsEven && Length[crossT] == 256]; diagT = Sort[Join[Flatten[Outer[Plus, splus, splus, 1], 1], Flatten[Outer[Plus, sminus, sminus, 1], 1]]]; formsOdd = Sort[Join[lamW[1], lamW[1], lamW[3], lamW[3], lamW[5]]]; checkExact["v109 sheet-diagonal = odd forms: (S+xS+)u(S-xS-) = 2L1+2L3+L5 (512)", diagT === formsOdd && Length[diagT] == 512]; zmult[k_] := Count[lamW[k], ConstantArray[0, 5]]; checkExact["v109 zero-mode grading (L0,L2,L4) -> (1,5,10) = the carrier code; tower tops at 2K = 4", ({zmult[0], zmult[2], zmult[4]} == {1, 5, 10}) && (4 == 2*2)]; ]; (* ---- (v110) Calderon-sheet selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L499)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v59) area-law evidence: exact seam-unit parts (the EE area-law is numerical, Python-only) ---- *) checkExact["8 = |Z2|*|mu4| (sheet x glue); chaos-bound/seam unit 2pi = 1/(4 c3)", 2*4 == 8 && Simplify[2 Pi - 1/(4*(1/(8 Pi)))] == 0]; (* NOTE: the free-field entanglement area-law of v59 is a numerical computation (numpy symplectic spectra), Python-only by design -- not mirrored here. *)](../../../../verification/wolfram/tfpt_readouts.wl#L276)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)

## 2026-06-13 (external review formalised: No-Unit Theorem + Simple-Current Extension Theorem, v153– v154)

[documents/changelog/sections/022-source.tex:258-284](../../../../documents/changelog/sections/022-source.tex#L258) · `section:65e6ea58d3d1fb647f95` · subsection

[formula in source] re-typed: the No-Unit Theorem ( v153). Every load-bearing compiler datum is mass-dimension [formula in source] and invariant under a unit rescaling [formula in source] , whereas a mass / [formula in source] is not — so a dimensionless boundary compiler provably cannot select an absolute scale. [formula in source] is therefore an irreducible metrology primitive, not an open gap, and the three appar

Explicit source references:

- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v143_graded_frobenius.py](../../../../verification/v143_graded_frobenius.py#L1) · explicit_script_identifier
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [GATE.METRIC.11](../../../../verification/status_ledger.csv#L239) · explicit_claim_identifier · original status at linked ledger row
- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v89_carrier_index_lemma.py](../../../../verification/v89_carrier_index_lemma.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v148_fock_census.py](../../../../verification/v148_fock_census.py#L1) · explicit_script_identifier
- [ANCHOR.VGEO.02](../../../../verification/status_ledger.csv#L238) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [(* ---- (v148) NS/R sector census (corrected) ---- *) Module[{nsClasses, rCounts, glueA, glueB, inA, inB}, nsClasses = Union[Flatten[Table[ {2 Mod[Total[v], 2], 2 Mod[Total[w], 2]}, {v, Tuples[Range[-1, 1], 5]}, {w, Tuples[Range[-1, 1], 3]}], 1]]; rCounts = <||>; Do[Module[{qd = If[EvenQ[Count[s5, -1]], 1, 3]}, Do[Module[{qa = If[EvenQ[Count[s3, -1]], 1, 3]}, rCounts[{qd, qa}] = Lookup[rCounts, Key[{qd, qa}], 0] + 1], {s3, Tuples[{1, -1}, 3]}]], {s5, Tuples[{1, -1}, 5]}]; glueA = {{0, 0}, {1, 1}, {2, 2}, {3, 3}}; glueB = {{0, 0}, {1, 3}, {2, 2}, {3, 1}}; inA = Total[Lookup[rCounts, Key[#], 0] & /@ glueA]; inB = Total[Lookup[rCounts, Key[#], 0] & /@ glueB]; checkExact["v148 NS/R census (corrected): NS supports only even classes {(0,0),(2,0),(0,2),(2,2)} (integer weights); R zero-mode module = four odd pairs of 64; R splits 128+128 into the odd sectors of the two Lagrangian glues; 248 = 120 NS + 128 R", Sort[nsClasses] == Sort[{{0, 0}, {2, 0}, {0, 2}, {2, 2}}] && ! MemberQ[nsClasses, {1, 1}] && ! MemberQ[nsClasses, {3, 3}] && Values[KeySort[rCounts]] == {64, 64, 64, 64} && Total[Values[rCounts]] == 256 && inA == 128 && inB == 128 && 120 + 128 == 248]; ]; (* ---- (v149) cusp normal ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1280)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v89) carrier index lemma ---- *) checkExact["v89 KLM: mu(D5xA3)=16, mu(E8)=1 => index 4 = |mu4| = |Z2|^2", (4*4 == 16) && (Sqrt[16/1] == 4) && (4 == mu4) && (4 == 2^2)]; checkExact["v89 branching 248 = 45+15+64+64+60; glue sectors h = 1", (45 + 15 + 16*4 + 16*4 + 10*6 == 248) && (1/2 + 1/2 == 1) && (5/8 + 3/8 == 1)]; checkExact["v89 mu-additivity: 16/4^2 = 1 (holomorphy follows)", 16/4^2 == 1]; (* ---- (v90) conical defect chain ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L117)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## 2026-06-13 (currency sweep: remaining old-series ``Paper N'' cross-references removed)

[documents/changelog/sections/022-source.tex:285-301](../../../../documents/changelog/sections/022-source.tex#L285) · `section:7510d6c9f8fef452a8a6` · subsection

No old-version framing left in the active docs. A consistency sweep found a residual layer of old-series ``Paper N'' attributions and removed them: four literal ``Paper 6'' references ( tfpt_4_frontier leptogenesis/axion, tfpt_2 seam determinant), the old ``Paper 4'' (OS/admissibility) and ``Paper 5'' (APS/Hodge) references in tfpt_2, the old ``Paper 3'' transport-kernel attributions in tfpt_2, and the internal ``Pap

## 2026-06-13 (fifth round: the R3 normalisation is the dimensionful anchor, v152)

[documents/changelog/sections/022-source.tex:302-317](../../../../documents/changelog/sections/022-source.tex#L302) · `section:1a45d75b719beb596c5e` · subsection

R3: the [formula in source] normalisation merges into the one anchor ( v152). The replica EH coefficient is a log-ratio [formula in source] ( [formula in source] alone is scale-ambiguous, only [formula in source] is physical); pinning [formula in source] fixes the dimensionless ratio [formula in source] , and in [formula in source] that ratio is the induced Newton constant [formula in source] ( v68). So [formula in s

Explicit source references:

- [SEAM.EHMODEL.03](../../../../verification/status_ledger.csv#L237) · explicit_claim_identifier · original status at linked ledger row
- [verification/v78_vgeo_floor.py](../../../../verification/v78_vgeo_floor.py#L1) · explicit_script_identifier
- [verification/v68_seeley_dewitt_residual.py](../../../../verification/v68_seeley_dewitt_residual.py#L1) · explicit_script_identifier
- [SEAM.THEOREM.01](../../../../verification/status_ledger.csv#L131) · explicit_claim_identifier · original status at linked ledger row
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v152_norm_is_anchor.py](../../../../verification/v152_norm_is_anchor.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v67) central theorem structural closure: replica area-law coeff => c3=1/(8pi) ---- *) checkExact["Fursaev-Solodukhin: k=c3/2=1/(16pi); S=4pi k A=2pi c3 A; 2pi c3=1/4 => S=A/4 (BH)", With[{c3 = 1/(8 Pi)}, Simplify[c3/2 - 1/(16 Pi)] == 0 && Simplify[2 Pi c3 - 1/4] == 0 && Simplify[4 Pi (c3/2) - 1/4] == 0]]; checkExact["theorem (inverse): S=A/4 & S=4pi k A & k=c3/2 => c3=1/(8pi) UNIQUE", Module[{ksol = 1/(4 (4 Pi))}, Simplify[ksol - 1/(16 Pi)] == 0 && Simplify[2*ksol - 1/(8 Pi)] == 0]]; (* ---- (v68) Seeley-DeWitt a2 for the carrier; 1/G UV-sensitive => k=c3/2 is a normalization ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L315)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v77) G6 via E8 level-1 net: level-1 central charges + conformal embedding c-sum ---- *) checkExact["level-1 c=dim/(1+h^v): c(E8)=248/31=8=rank E8, c(D5)=45/9=5, c(A3)=15/5=3; embedding 5+3=8 => coset c=0", Module[{cE8 = 248/(1 + 30), cD5 = 45/(1 + 8), cA3 = 15/(1 + 4)}, (cE8 == 8) && (cD5 == 5) && (cA3 == 3) && (cD5 + cA3 == cE8)]]; (* ---- (v78) v_geo floor: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (one scale pinned by one measurement) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L376)
- [(* ---- (v205) GRAV.XI.01: xi = c3/phi_tree = 3/4, the independent gravitational 3/4 ---- *) Module[{c3, phitree}, c3 = 1/(8 Pi); phitree = 1/(6 Pi); checkExact["v205 GRAV.XI.01: the torsion-compression factor xi = c3/phi_tree = (1/8pi)/(1/6pi) = 3/4 EXACTLY; the Einstein-limit reduction 8 pi c3^2 = c3 makes G an output (xi = c3/phi0); and 3/4 = 12 pi (c3/2) = ln(m/mu) = q(A3) (v152) -- the torsion-compression and the gapped EH replica are two independent appearances of the same gravitational 3/4", Simplify[c3/phitree - 3/4] == 0 && Simplify[8 Pi c3^2 - c3] == 0 && Simplify[12 Pi (c3/2) - 3/4] == 0]; ]; (* ---- (v208) HOR.BHTHERMO.01: scalaron Wald factor + modular 2 pi = 1/(4 c3) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1708)

## 2026-06-12 (Zenodo version label: semantic + git rev)

[documents/changelog/sections/022-source.tex:318-326](../../../../documents/changelog/sections/022-source.tex#L318) · `section:96bab9fe7e8297dfe11c` · subsection

Release version string. build.sh now writes tex-artefacts/release-version.txt as \TFPTversion\ (rev \git count\) (matches TFPTdatestamp without the date). scripts/zenodo_upload.py and build.sh zenodo/ zenodo-publish use this label on Zenodo; cursor rules extended for when zenodo_description.html must move with deposit-facing changes.

Explicit source references:

- [scripts/zenodo_upload.py](../../../../scripts/zenodo_upload.py#L1) · explicit_file_citation

## 2026-06-12 (Zenodo API upload workflow)

[documents/changelog/sections/022-source.tex:327-335](../../../../documents/changelog/sections/022-source.tex#L327) · `section:2f507dd11e908355b7f4` · subsection

Automated Zenodo versioning. Added scripts/zenodo_upload.py and .github/workflows/ zenodo-release.yml: creates a new draft version of record 20579275 (DOI 10.5281/ zenodo. 20579275), uploads the ten active paper PDFs, refreshes zenodo_description.html, bumps the version from tex-artefacts/version.tex, and optionally publishes via GitHub Actions ( ZENODO_TOKEN secret).

Explicit source references:

- [scripts/zenodo_upload.py](../../../../scripts/zenodo_upload.py#L1) · explicit_file_citation

## 2026-06-12 (Overleaf shadow mirror: tfpt5-shadow)

[documents/changelog/sections/022-source.tex:336-344](../../../../documents/changelog/sections/022-source.tex#L336) · `section:38476028a7422847fd8e` · subsection

One-way GitHub mirror for Overleaf sync. Added scripts/export-shadow.sh and .github/workflows/shadow-sync.yml: on every push to main, a filtered copy is pushed to sthamann/tfpt5-shadow (papers, tex-artefacts/, figures/, verification/, experiments/; excludes _archive/, website/, all *.pdf, .cursor/). [formula in source] 270 files / [formula in source] 3\,MB — within Overleaf GitHub-sync limits.

## 2026-06-12 (origin_theory style alignment + box reduction)

[documents/changelog/sections/022-source.tex:345-357](../../../../documents/changelog/sections/022-source.tex#L345) · `section:91ac555bf8a799498a54` · subsection

Fewer boxes, embedded in text. origin_theory from [formula in source] to [formula in source] boxes: the narrative/interpretation callouts (``Why the interpretation is internally consistent'', ``Dependency chain of the birefringence test'', ``The precise reformulation'', ``The three theses honestly graded'', ``The whole story'', ``One-line summary'') become run-in bold prose; the boxed reformulation becomes a keyeq. T

Explicit source references:

- [verification/v105_residual_inventory.py](../../../../verification/v105_residual_inventory.py#L1) · explicit_script_identifier
- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier
- [verification/v101_horizon_anchor.py](../../../../verification/v101_horizon_anchor.py#L1) · explicit_script_identifier
- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [verification/v53_compiler_core.py](../../../../verification/v53_compiler_core.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)
- [(* ---- (v101) horizon anchor: SdS in seam units ---- *) fSdS = 1 - 2 mm/rr - LL rr^2/3; cubicSdS = Expand[-fSdS 3 rr/LL]; narSol = Solve[{cubicSdS == 0, D[cubicSdS, rr] == 0}, {rr, mm}, Assumptions -> LL > 0]; checkExact["v101 Nariai double root: M_N = 1/(3 Sqrt[L]) = 1/(N_fam Sqrt[L]), r_N = 1/Sqrt[L]", MemberQ[Simplify[{rr, mm} /. narSol], {1/Sqrt[LL], 1/(3 Sqrt[LL])}]]; checkExact["v101 Nariai cubic = t^3 - 3t + 2 = (t-1)^2(t+2): roots (1,1,-2) = traceless anchor", (Expand[(t - 1)^2 (t + 2)] == t^3 - 3 t + 2) && (Simplify[{1, 1, 2} - (4/3) {1, 1, 1} - (-1/3) {1, 1, -2}] == {0, 0, 0})]; checkExact["v101 Koide 2/3 = Nariai entropy bound: S_N/S_dS = 2/3, per horizon 1/3, deficit 1/3", ((2 Pi/LL)/(3 Pi/LL) == 2/3) && ((Pi/LL)/(3 Pi/LL) == 1/3)]; checkExact["v101 interpolation S_tot/S_dS = (x^2+1)/(x^2+x+1) (denominator = Phi_3), min at merge", (Simplify[(xx^2 + 1)/(xx^2 + xx + 1) - (Pi (xx^2 + 1) 3/(LL (xx^2 + xx + 1)))/(3 Pi/LL)] === 0) && (Cyclotomic[3, xx] == xx^2 + xx + 1) && (((xx^2 + 1)/(xx^2 + xx + 1) /. xx -> 0) == 1) && (((xx^2 + 1)/(xx^2 + xx + 1) /. xx -> 1) == 2/3)]; checkExact["v101 three-sheet conservation: Sum r_i^2 = 2(rb^2+rb rc+rc^2) for roots (rb, rc, -(rb+rc))", Expand[rbb^2 + rcc^2 + (rbb + rcc)^2 - 2 (rbb^2 + rbb rcc + rcc^2)] === 0]; checkExact["v101 Q_geom range: pure dS -> 1/2 = delta, Nariai -> 3/8 = p2(a)/e1(a)^2 = SU(4)_1 weights", Module[{Qg = (xx^2 + (xx + 1)^2 + 1)/(4 (xx + 1)^2)}, ((Qg /. xx -> 0) == 1/2) && ((Qg /. xx -> 1) == 3/8) && (6/16 == 3/8)]]; checkExact["v101 mass-line double cover: disc = (108/L^3)(1-9 L M^2) -> (1-3m)(1+3m), branch +-1/N_fam", (Simplify[Discriminant[cubicSdS, rr] - 108/LL^3 (1 - 9 LL mm^2)] === 0) && (Expand[(1 - 3 md) (1 + 3 md) - (1 - 9 md^2)] === 0)]; checkExact["v101 temperature lemma: |kappa_b/kappa_c| = (2x+1)/(x(x+2)), = 1 iff x = 1", Module[{ff, kb, kc}, ff = -LL/(3 rr) (rr - rbb) (rr - rcc) (rr + rbb + rcc); kb = D[ff, rr] /. rr -> rbb; kc = D[ff, rr] /. rr -> rcc; Simplify[(kb/-kc /. rbb -> xx rcc) - (2 xx + 1)/(xx (xx + 2)), Assumptions -> rcc > 0 && xx > 0 && xx < 1] === 0]]; checkExact["v101 seam-unit mechanics: 1/(8Pi) = c3; Smarr 1/(4Pi) = 2c3; Bekenstein 2Pi = 1/(4c3); P_H 15360 Pi = 1920/c3; lifetime 5120 Pi = 128*5/c3; Kerr A_ext = M^2/c3; 4 Log[3] = Log[81]", (1/(8 Pi) == c3) && (Simplify[1/(4 Pi) - 2 c3] === 0) && (Simplify[2 Pi - 1/(4 c3)] === 0) && (Simplify[1/(15360 Pi) - c3/1920] === 0) && (Simplify[5120 Pi - 128*5/c3] === 0) && (Simplify[8 Pi - 1/c3] === 0) && (Simplify[4 Log[3] - Log[81]] === 0)]; (* ---- (v102) seam orientation: anchor = stationary repeller, both sectors ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L333)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [(* ==== v491 round: P2.PARTITION.01 -- g_car = 5 as the partition corollary of the four marks (the sharpening of v53). Exact content: 4 into exactly 3 positive integer parts is uniquely {1,1,2} => e = (4,5,2) => g_car = e2 = 5, |Z2| = e3 = 2, N_fam = e2 - e3 = 3 as corollaries; every assumption load-bearing (positivity / sum / part count / integrality negative controls); v53 needs all three targets, the partition only e1 = 4; sum rule 4(N-1)/2 = 4 iff N = 3; mirrors v491. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3116)

## 2026-06-12 (tfpt_5 / horizon / research-contracts pass + build hardening)

[documents/changelog/sections/022-source.tex:358-377](../../../../documents/changelog/sections/022-source.tex#L358) · `section:b55fee767ef53c6e7ef1` · subsection

Forked document-set box removed (horizon). tfpt_horizon_readouts carried a hand-written, stale copy of the document-set card (``five short documents'', missing tfpt_5) and the canonical input\tex-artefacts/tfpt_docset\; the fork is deleted so the single-source card (all five papers [formula in source] three companions) appears once. Fewer boxes, embedded in text. Narrative/result callouts converted to run-in bold pro

## 2026-06-12 (fourth round: the Calder\'on transfer answered — the BFK split, v151)

[documents/changelog/sections/023-source.tex:1-16](../../../../documents/changelog/sections/023-source.tex#L1) · `section:54d3ef2afad00c946773` · subsection

R3: the Calder\'on/DtN kernel is conically clean ( v151). Reflection doubling derives that the Kac corner constant is boundary-condition independent ( [formula in source] ), so by the Burghelea–Friedlander–Kappeler gluing ledger the conical deficit of the two-sided Calder\'on jump determinant vanishes identically ( [formula in source] ): the seam-reduced effective action inherits the v150 EH form verbatim, with all o

Explicit source references:

- [SEAM.EHMODEL.02](../../../../verification/status_ledger.csv#L236) · explicit_claim_identifier · original status at linked ledger row
- [verification/v151_bfk_split.py](../../../../verification/v151_bfk_split.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [SEAM.THEOREM.01](../../../../verification/status_ledger.csv#L131) · explicit_claim_identifier · original status at linked ledger row
- [verification/v150_replica_eh_model.py](../../../../verification/v150_replica_eh_model.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v150) replica EH model ---- *) Module[{cdef, imgOK, convOK, mellin, dz0, dC, target}, cdef[g_] := (1/12) (2 Pi/g - g/(2 Pi)); imgOK = And @@ Table[ FullSimplify[Sum[1/Sin[Pi k/n]^2, {k, 1, n - 1}] - (n^2 - 1)/3] === 0, {n, 2, 8}]; convOK = Simplify[(1/(4 nn)) (nn^2 - 1)/3 - cdef[2 Pi/nn]] === 0; mellin = Integrate[tt^(ss - 1) Exp[-mm^2 tt], {tt, 0, Infinity}, Assumptions -> ss > 0 && mm > 0]; dz0 = D[mm^(-2 ss), ss] /. ss -> 0; dC = D[cdef[gg], gg] /. gg -> 2 Pi; target = Simplify[12 Pi (1/2) (1/(8 Pi))]; checkExact["v150 replica EH model: image sum exact (N=2..8); orbifold deficit = C(2pi/N); Mellin Delta-zeta(s) = C m^-2s => Delta log det' = 2C ln m (cutoff-independent); dC/dgamma|_{2pi} = -1/(12pi) => EH form with k = ln m/(12pi); target k = c3/2 <=> ln m = 3/4 = q(A3)", imgOK && convOK && Simplify[mellin - Gamma[ss] mm^(-2 ss)] === 0 && Simplify[dz0 + 2 Log[mm]] === 0 && Simplify[dC + 1/(12 Pi)] === 0 && target == 3/4]; ]; (* ---- (v151) BFK split ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1321)

## 2026-06-12 (third round: both normals anchor data; the R3 mechanism exists, v149– v150)

[documents/changelog/sections/023-source.tex:17-38](../../../../documents/changelog/sections/023-source.tex#L17) · `section:1ca85309d96f89f48f6e` · subsection

R4 [formula in source] : both dual normals are anchor data ( v149). In the cusp frame the torsion normal pairs to [formula in source] — one anchor invariant per [formula in source] line (the cusp matrix is unimodular, so this determines [formula in source] uniquely); with [formula in source] the dual normal pair is anchor data through and through. Equivalences to the [formula in source] frame data and the [formula in

Explicit source references:

- [SEAM.EHMODEL.01](../../../../verification/status_ledger.csv#L235) · explicit_claim_identifier · original status at linked ledger row
- [verification/v150_replica_eh_model.py](../../../../verification/v150_replica_eh_model.py#L1) · explicit_script_identifier
- [SEAM.THEOREM.01](../../../../verification/status_ledger.csv#L131) · explicit_claim_identifier · original status at linked ledger row
- [verification/v73_k_c3_half.py](../../../../verification/v73_k_c3_half.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v149_cusp_normal.py](../../../../verification/v149_cusp_normal.py#L1) · explicit_script_identifier
- [GATE.UWALL.14](../../../../verification/status_ledger.csv#L234) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v150) replica EH model ---- *) Module[{cdef, imgOK, convOK, mellin, dz0, dC, target}, cdef[g_] := (1/12) (2 Pi/g - g/(2 Pi)); imgOK = And @@ Table[ FullSimplify[Sum[1/Sin[Pi k/n]^2, {k, 1, n - 1}] - (n^2 - 1)/3] === 0, {n, 2, 8}]; convOK = Simplify[(1/(4 nn)) (nn^2 - 1)/3 - cdef[2 Pi/nn]] === 0; mellin = Integrate[tt^(ss - 1) Exp[-mm^2 tt], {tt, 0, Infinity}, Assumptions -> ss > 0 && mm > 0]; dz0 = D[mm^(-2 ss), ss] /. ss -> 0; dC = D[cdef[gg], gg] /. gg -> 2 Pi; target = Simplify[12 Pi (1/2) (1/(8 Pi))]; checkExact["v150 replica EH model: image sum exact (N=2..8); orbifold deficit = C(2pi/N); Mellin Delta-zeta(s) = C m^-2s => Delta log det' = 2C ln m (cutoff-independent); dC/dgamma|_{2pi} = -1/(12pi) => EH form with k = ln m/(12pi); target k = c3/2 <=> ln m = 3/4 = q(A3)", imgOK && convOK && Simplify[mellin - Gamma[ss] mm^(-2 ss)] === 0 && Simplify[dz0 + 2 Log[mm]] === 0 && Simplify[dC + 1/(12 Pi)] === 0 && target == 3/4]; ]; (* ---- (v151) BFK split ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1321)
- [(* ---- (v73) k=c3/2 forced: variational factor x Gauss-Bonnet topology; Fursaev-Solodukhin S=A/4 ---- *) checkExact["k=c3/2=1/(16pi)=(1/2)*(1/(|Z2|*2pi*chi(S2))), chi(S2)=2; Fursaev-Solodukhin 4pi k = 1/4", Module[{c3 = 1/(8 Pi), chi = 2, Z2 = 2}, (c3/2 == 1/(16 Pi)) && (c3 == 1/(Z2*2 Pi*chi)) && (4 Pi*(c3/2) == 1/4)]]; (* ---- (v74) compiler micro-lemmas: pencil differences 2->16->48; anchor QF 41-25=16 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L352)
- [(* ---- (v148) NS/R sector census (corrected) ---- *) Module[{nsClasses, rCounts, glueA, glueB, inA, inB}, nsClasses = Union[Flatten[Table[ {2 Mod[Total[v], 2], 2 Mod[Total[w], 2]}, {v, Tuples[Range[-1, 1], 5]}, {w, Tuples[Range[-1, 1], 3]}], 1]]; rCounts = <||>; Do[Module[{qd = If[EvenQ[Count[s5, -1]], 1, 3]}, Do[Module[{qa = If[EvenQ[Count[s3, -1]], 1, 3]}, rCounts[{qd, qa}] = Lookup[rCounts, Key[{qd, qa}], 0] + 1], {s3, Tuples[{1, -1}, 3]}]], {s5, Tuples[{1, -1}, 5]}]; glueA = {{0, 0}, {1, 1}, {2, 2}, {3, 3}}; glueB = {{0, 0}, {1, 3}, {2, 2}, {3, 1}}; inA = Total[Lookup[rCounts, Key[#], 0] & /@ glueA]; inB = Total[Lookup[rCounts, Key[#], 0] & /@ glueB]; checkExact["v148 NS/R census (corrected): NS supports only even classes {(0,0),(2,0),(0,2),(2,2)} (integer weights); R zero-mode module = four odd pairs of 64; R splits 128+128 into the odd sectors of the two Lagrangian glues; 248 = 120 NS + 128 R", Sort[nsClasses] == Sort[{{0, 0}, {2, 0}, {0, 2}, {2, 2}}] && ! MemberQ[nsClasses, {1, 1}] && ! MemberQ[nsClasses, {3, 3}] && Values[KeySort[rCounts]] == {64, 64, 64, 64} && Total[Values[rCounts]] == 256 && inA == 128 && inB == 128 && 120 + 128 == 248]; ]; (* ---- (v149) cusp normal ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1280)

## 2026-06-12 (R1–R5 second round: every class at its floor, v145– v148)

[documents/changelog/sections/023-source.tex:39-75](../../../../documents/changelog/sections/023-source.tex#L39) · `section:4d3487ca2d27735cbff3` · subsection

R4 [formula in source] : the pairing values are atom identities ( v145). Reading the v139 lift structurally ( [formula in source] , [formula in source] the [formula in source] exponent duality), all three pairings become atom arithmetic — including the new closure [formula in source] ( [formula in source] , [formula in source] ) and [formula in source] . R4 [formula in source] [formula in source] derive one map (ledg

Explicit source references:

- [FLAV.QGEO.07](../../../../verification/status_ledger.csv#L231) · explicit_claim_identifier · original status at linked ledger row
- [verification/v147_clock_gaussian.py](../../../../verification/v147_clock_gaussian.py#L1) · explicit_script_identifier
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v127_ring_resummation.py](../../../../verification/v127_ring_resummation.py#L1) · explicit_script_identifier
- [verification/v144_detratio_family.py](../../../../verification/v144_detratio_family.py#L1) · explicit_script_identifier
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v145_pairing_atoms.py](../../../../verification/v145_pairing_atoms.py#L1) · explicit_script_identifier
- [GATE.METRIC.10](../../../../verification/status_ledger.csv#L233) · explicit_claim_identifier · original status at linked ledger row
- [verification/v146_moebius_d4.py](../../../../verification/v146_moebius_d4.py#L1) · explicit_script_identifier
- [verification/v148_fock_census.py](../../../../verification/v148_fock_census.py#L1) · explicit_script_identifier
- [HOR.CLOCK.13](../../../../verification/status_ledger.csv#L232) · explicit_claim_identifier · original status at linked ledger row
- [GATE.WOLFRAM.02](../../../../verification/status_ledger.csv#L168) · explicit_claim_identifier · original status at linked ledger row
- [GATE.UWALL.13](../../../../verification/status_ledger.csv#L230) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [(* ---- (v148) NS/R sector census (corrected) ---- *) Module[{nsClasses, rCounts, glueA, glueB, inA, inB}, nsClasses = Union[Flatten[Table[ {2 Mod[Total[v], 2], 2 Mod[Total[w], 2]}, {v, Tuples[Range[-1, 1], 5]}, {w, Tuples[Range[-1, 1], 3]}], 1]]; rCounts = <||>; Do[Module[{qd = If[EvenQ[Count[s5, -1]], 1, 3]}, Do[Module[{qa = If[EvenQ[Count[s3, -1]], 1, 3]}, rCounts[{qd, qa}] = Lookup[rCounts, Key[{qd, qa}], 0] + 1], {s3, Tuples[{1, -1}, 3]}]], {s5, Tuples[{1, -1}, 5]}]; glueA = {{0, 0}, {1, 1}, {2, 2}, {3, 3}}; glueB = {{0, 0}, {1, 3}, {2, 2}, {3, 1}}; inA = Total[Lookup[rCounts, Key[#], 0] & /@ glueA]; inB = Total[Lookup[rCounts, Key[#], 0] & /@ glueB]; checkExact["v148 NS/R census (corrected): NS supports only even classes {(0,0),(2,0),(0,2),(2,2)} (integer weights); R zero-mode module = four odd pairs of 64; R splits 128+128 into the odd sectors of the two Lagrangian glues; 248 = 120 NS + 128 R", Sort[nsClasses] == Sort[{{0, 0}, {2, 0}, {0, 2}, {2, 2}}] && ! MemberQ[nsClasses, {1, 1}] && ! MemberQ[nsClasses, {3, 3}] && Values[KeySort[rCounts]] == {64, 64, 64, 64} && Total[Values[rCounts]] == 256 && inA == 128 && inB == 128 && 120 + 128 == 248]; ]; (* ---- (v149) cusp normal ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1280)
- [(* ---- (v146) Moebius D4 realisation ---- *) Module[{om, deckOK, invOK, ta, sig, p, tac, sigc, delta, iota}, om[k_] := z^(k - 1)/(z^4 - 1); deckOK = And @@ Table[ Simplify[(om[k] /. z -> I w) I - I^k (om[k] /. z -> w)] === 0, {k, 1, 3}]; invOK = Simplify[(om[1] /. z -> 1/w) (-1/w^2) - (om[3] /. z -> w)] === 0 && Simplify[(om[2] /. z -> 1/w) (-1/w^2) - (om[2] /. z -> w)] === 0 && Simplify[(om[3] /. z -> 1/w) (-1/w^2) - (om[1] /. z -> w)] === 0; ta = {{0, 1, 0}, {1, 0, 0}, {2, -2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; p = Transpose[{{0, 0, 1}, {0, 1, 2}, {1, 0, 0}}]; tac = Inverse[p] . ta . p; sigc = Inverse[p] . sig . p; delta = DiagonalMatrix[{I, -1, -I}]; iota = {{0, 0, 1}, {0, 1, 0}, {1, 0, 0}}; checkExact["v146 Moebius D4: delta* omega_k = i^k omega_k; iota* omega_(1,2,3) = omega_(3,2,1) (+1 on chi2, det -1); dihedral relations; T_A (cusp basis, char-2 line first) = the same reflection class as iota (fixes the self-conjugate line with +1, swaps the pair, det -1); Sigma = the delta-iota class", deckOK && invOK && iota . iota == IdentityMatrix[3] && Simplify[iota . delta . Inverse[iota] - Inverse[delta]] == ConstantArray[0, {3, 3}] && tac == {{1, 0, 0}, {0, 0, 1}, {0, 1, 0}} && Det[tac] == -1 && tac[[1, 1]] == 1 == iota[[2, 2]] && sigc == DiagonalMatrix[{-1, -1, 1}] && Simplify[(delta . iota)[[2, 2]]] == -1 && Simplify[Det[delta . iota]] == 1]; ]; (* ---- (v147) clock Gaussian model ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1239)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [(* ---- (v144) det-ratio family cancellation ---- *) Module[{s, p, rb, rc, ro, poly, ratio, ser, cpar, epsSer}, s = 2 Sqrt[1 - \[CapitalDelta]^2/12]; p = 1 - \[CapitalDelta]^2/3; rb = (s + \[CapitalDelta])/2; rc = (s - \[CapitalDelta])/2; ro = -s; poly = Collect[Expand[(t - rb)(t - rc)(t - ro)], t, Simplify]; ratio = (rb rc)^(4/3); ser = Normal[Series[ratio, {\[CapitalDelta], 0, 3}]]; cpar = Simplify[p s/2]; epsSer = Normal[Series[1 - cpar, {\[CapitalDelta], 0, 3}]]; checkExact["v144 det-ratio family cancellation: e2-rigidity r_b r_c = 1 - Delta^2/3 exact (traceless cubic, e2 = -3); ratio = (1 - Delta^2/3)^(4/3) has NO first-order term, quadratic coefficient -4/9; eps = (3/8) Delta^2 => coefficient -32/27 = -|mu4| (2/3)^3", Simplify[rb rc - p] == 0 && Simplify[Coefficient[poly, t, 2]] == 0 && Simplify[Coefficient[poly, t, 1]] == -3 && Coefficient[ser, \[CapitalDelta], 1] == 0 && Coefficient[ser, \[CapitalDelta], 2] == -4/9 && Coefficient[epsSer, \[CapitalDelta], 2] == 3/8 && (-4/9)/(3/8) == -32/27 == -4 (2/3)^3]; ]; (* ---- (v145) pairing atoms ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1207)
- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* v415 (4): the intrinsic order-4 mu4 deck D = -I + J - J^2 *) Pi2 = I3 + J . J; D = J - Pi2; checkExact["v415 DIAMOND.GAUSS.01 (iv): the intrinsic deck D=-I+J-J^2={{-1,1,0},{-2,1,0},{-4,3,-1}} is order 4 (D^4=I), Spec(D)={i,-1,-i} (the seam-deck spectrum, v146); chi2 line = ker[U,V] = NullSpace = {(0,0,1)} = a-1", D == {{-1, 1, 0}, {-2, 1, 0}, {-4, 3, -1}} && MatrixPower[D, 4] == I3 && Sort[Eigenvalues[D]] == Sort[{I, -I, -1}] && NullSpace[J] == {{0, 0, 1}} && a - one == {0, 0, 1}]; (* v416 (1): the Z[i] (square/seam) trichotomy *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2476)
- [(* ---- (v127) ring resummation ---- *) Module[{proj, partial}, proj = {{1, 0, 0}, {0, 0, 0}, {0, 0, 0}}; checkExact["v127 log-det identity: det(1 - a P) = 1 - a (rank-1 P); series -ln(1-a) = a + a^2/2 + a^3/3 + ...", Simplify[Det[IdentityMatrix[3] - a proj] - (1 - a)] === 0 && Normal[Series[-Log[1 - a], {a, 0, 3}]] === a + a^2/2 + a^3/3]; partial[al_, kmax_] := 6 Sum[al^j/j, {j, kmax}]; checkExact["v127 ring ladder: k=1 ring = classical (2, 4 at weights 1, 2); k=2 ring = 1/3 at weight 1; partials below exact and monotone", partial[1/3, 1] == 2 && partial[2/3, 1] == 4 && 6 (1/3)^2/2 == 1/3 && partial[1/3, 8] < -6 Log[1 - 1/3] && partial[1/3, 2] > partial[1/3, 1]]; checkExact["v127 coupling cross-link + wall: kappa_seam = 8/24 = 1/3 = alpha_1 (kappa = alpha_1/pi); ring series diverges at alpha -> 1", 8/24 == 1/3 && Limit[-Log[1 - a], a -> 1, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v128) graded hull ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L903)

## 2026-06-12 (external review integrated: [formula in source] typing, marker migration, website parity)

[documents/changelog/sections/023-source.tex:76-118](../../../../documents/changelog/sections/023-source.tex#L76) · `section:298ca201062fd482dafa` · subsection

[formula in source] normalisation made unambiguous. The external review flagged the adjacent reduced/unreduced displays in origin_theory as a type trap (the formulas were individually correct — [formula in source] vs [formula in source] — but easy to misread). Both normalisations are now shown explicitly side by side with their order counts ( [formula in source] reduced; [formula in source] unreduced) plus a typing n

Explicit source references:

- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_script_identifier
- [verification/v118_hexagon_family_dictionary.py](../../../../verification/v118_hexagon_family_dictionary.py#L1) · explicit_script_identifier
- [verification/v83_e8net_holomorphic_uniqueness.py](../../../../verification/v83_e8net_holomorphic_uniqueness.py#L1) · explicit_script_identifier
- [verification/v141_deck_selection.py](../../../../verification/v141_deck_selection.py#L1) · explicit_script_identifier
- [verification/v143_graded_frobenius.py](../../../../verification/v143_graded_frobenius.py#L1) · explicit_script_identifier
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v75_upoint_to_vgeo.py](../../../../verification/v75_upoint_to_vgeo.py#L1) · explicit_script_identifier
- [verification/v89_carrier_index_lemma.py](../../../../verification/v89_carrier_index_lemma.py#L1) · explicit_script_identifier
- [verification/v87_bulk_uniqueness_reduction.py](../../../../verification/v87_bulk_uniqueness_reduction.py#L1) · explicit_script_identifier
- [verification/v144_detratio_family.py](../../../../verification/v144_detratio_family.py#L1) · explicit_script_identifier
- [verification/v142_frame_integrality.py](../../../../verification/v142_frame_integrality.py#L1) · explicit_script_identifier
- [verification/v122_margin_theorem.py](../../../../verification/v122_margin_theorem.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v140) canonical map ---- *) Module[{charf, cu, cmu, cw}, charf[m_] := Mod[Round[Arg[#]/(Pi/2)], 4] & /@ Diagonal[m]; cu = charf[DiagonalMatrix[{1, I, -I}]]; cmu = charf[-DiagonalMatrix[{1, I, -I}]]; cw = charf[DiagonalMatrix[{I, I^2, I^3}]]; checkExact["v140 canonical map: deck U chars (0,1,3) miss 2; -U = (2,3,1) and i^Q+ = (1,2,3) both have SET {1,2,3} = H^1; i^Q+ assignment = Q+, -U assignment = Q+ o rho (one Z3 rotation apart)", cu == {0, 1, 3} && cmu == {2, 3, 1} && cw == {1, 2, 3} && Sort[cmu] == {1, 2, 3} == Sort[cw] && cmu == (cw[[#]] & /@ {2, 3, 1})]; ]; (* ---- (v141) deck selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1122)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)
- [(* ---- (v144) det-ratio family cancellation ---- *) Module[{s, p, rb, rc, ro, poly, ratio, ser, cpar, epsSer}, s = 2 Sqrt[1 - \[CapitalDelta]^2/12]; p = 1 - \[CapitalDelta]^2/3; rb = (s + \[CapitalDelta])/2; rc = (s - \[CapitalDelta])/2; ro = -s; poly = Collect[Expand[(t - rb)(t - rc)(t - ro)], t, Simplify]; ratio = (rb rc)^(4/3); ser = Normal[Series[ratio, {\[CapitalDelta], 0, 3}]]; cpar = Simplify[p s/2]; epsSer = Normal[Series[1 - cpar, {\[CapitalDelta], 0, 3}]]; checkExact["v144 det-ratio family cancellation: e2-rigidity r_b r_c = 1 - Delta^2/3 exact (traceless cubic, e2 = -3); ratio = (1 - Delta^2/3)^(4/3) has NO first-order term, quadratic coefficient -4/9; eps = (3/8) Delta^2 => coefficient -32/27 = -|mu4| (2/3)^3", Simplify[rb rc - p] == 0 && Simplify[Coefficient[poly, t, 2]] == 0 && Simplify[Coefficient[poly, t, 1]] == -3 && Coefficient[ser, \[CapitalDelta], 1] == 0 && Coefficient[ser, \[CapitalDelta], 2] == -4/9 && Coefficient[epsSer, \[CapitalDelta], 2] == 3/8 && (-4/9)/(3/8) == -32/27 == -4 (2/3)^3]; ]; (* ---- (v145) pairing atoms ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1207)
- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [(* ---- (v89) carrier index lemma ---- *) checkExact["v89 KLM: mu(D5xA3)=16, mu(E8)=1 => index 4 = |mu4| = |Z2|^2", (4*4 == 16) && (Sqrt[16/1] == 4) && (4 == mu4) && (4 == 2^2)]; checkExact["v89 branching 248 = 45+15+64+64+60; glue sectors h = 1", (45 + 15 + 16*4 + 16*4 + 10*6 == 248) && (1/2 + 1/2 == 1) && (5/8 + 3/8 == 1)]; checkExact["v89 mu-additivity: 16/4^2 = 1 (holomorphy follows)", 16/4^2 == 1]; (* ---- (v90) conical defect chain ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L117)
- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)

## 2026-06-12 (R1–R5 attack round: four residual classes sharpened, v141– v144)

[documents/changelog/sections/023-source.tex:119-154](../../../../documents/changelog/sections/023-source.tex#L119) · `section:e09bf94c77ca8cb235a1` · subsection

R5 closed at the discrete level ( v141, deck selection theorem). The v140 [formula in source] choice is derived: the established integer deck [formula in source] ( v97/ v98) pairs the [formula in source] cusp line with the self-conjugate character [formula in source] , so only the sheet-twisted assignment [formula in source] survives; the cusp exponential [formula in source] is excluded (same spectrum, wrong grading 

Explicit source references:

- [SEAM.THEOREM.01](../../../../verification/status_ledger.csv#L131) · explicit_claim_identifier · original status at linked ledger row
- [verification/v141_deck_selection.py](../../../../verification/v141_deck_selection.py#L1) · explicit_script_identifier
- [verification/v144_detratio_family.py](../../../../verification/v144_detratio_family.py#L1) · explicit_script_identifier
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [verification/v132_detratio_anomaly.py](../../../../verification/v132_detratio_anomaly.py#L1) · explicit_script_identifier
- [GATE.METRIC.09](../../../../verification/status_ledger.csv#L228) · explicit_claim_identifier · original status at linked ledger row
- [verification/v142_frame_integrality.py](../../../../verification/v142_frame_integrality.py#L1) · explicit_script_identifier
- [GATE.UWALL.12](../../../../verification/status_ledger.csv#L227) · explicit_claim_identifier · original status at linked ledger row
- [verification/v97_sheet_conjugation_bridge.py](../../../../verification/v97_sheet_conjugation_bridge.py#L1) · explicit_script_identifier
- [FLAV.QGEO.06](../../../../verification/status_ledger.csv#L226) · explicit_claim_identifier · original status at linked ledger row
- [GATE.WOLFRAM.02](../../../../verification/status_ledger.csv#L168) · explicit_claim_identifier · original status at linked ledger row
- [HOR.CLOCK.12](../../../../verification/status_ledger.csv#L229) · explicit_claim_identifier · original status at linked ledger row
- [verification/v131_measure_is_area.py](../../../../verification/v131_measure_is_area.py#L1) · explicit_script_identifier
- [verification/v98_discriminant_dictionary.py](../../../../verification/v98_discriminant_dictionary.py#L1) · explicit_script_identifier
- [verification/v143_graded_frobenius.py](../../../../verification/v143_graded_frobenius.py#L1) · explicit_script_identifier
- [verification/v140_canonical_map.py](../../../../verification/v140_canonical_map.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [(* ---- (v131) measure is area ---- *) Module[{pref, harms, norms}, pref = Sqrt[3/(4 Pi)]; harms = {pref Cos[\[Theta]], pref Sin[\[Theta]] Cos[\[Phi]], pref Sin[\[Theta]] Sin[\[Phi]]}; norms = Table[Integrate[Integrate[y^2 rr^2 Sin[\[Theta]], {\[Theta], 0, Pi}], {\[Phi], 0, 2 Pi}], {y, harms}]; checkExact["v131 zero-mode norm = area: all three l=1 norms^2 = r^2 = A/(4pi); Jacobian bookkeeping (x^3)^2 = x^6; c3 = (1/2)(1/4pi)", AllTrue[norms, Simplify[# - rr^2] === 0 &] && Simplify[(4 Pi rr^2)/(4 Pi) - rr^2] === 0 && Simplify[(x^3)^2 - x^6] === 0 && 1/2 * 1/(4 Pi) == 1/(8 Pi)]; ]; (* ---- (v132) det-ratio anomaly ---- The numerical heat-trace continuation is Python-only (mpmath); the exact arithmetic is mirrored here, plus an independent exact check of the constant term via the full heat-trace expansion. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L968)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v144) det-ratio family cancellation ---- *) Module[{s, p, rb, rc, ro, poly, ratio, ser, cpar, epsSer}, s = 2 Sqrt[1 - \[CapitalDelta]^2/12]; p = 1 - \[CapitalDelta]^2/3; rb = (s + \[CapitalDelta])/2; rc = (s - \[CapitalDelta])/2; ro = -s; poly = Collect[Expand[(t - rb)(t - rc)(t - ro)], t, Simplify]; ratio = (rb rc)^(4/3); ser = Normal[Series[ratio, {\[CapitalDelta], 0, 3}]]; cpar = Simplify[p s/2]; epsSer = Normal[Series[1 - cpar, {\[CapitalDelta], 0, 3}]]; checkExact["v144 det-ratio family cancellation: e2-rigidity r_b r_c = 1 - Delta^2/3 exact (traceless cubic, e2 = -3); ratio = (1 - Delta^2/3)^(4/3) has NO first-order term, quadratic coefficient -4/9; eps = (3/8) Delta^2 => coefficient -32/27 = -|mu4| (2/3)^3", Simplify[rb rc - p] == 0 && Simplify[Coefficient[poly, t, 2]] == 0 && Simplify[Coefficient[poly, t, 1]] == -3 && Coefficient[ser, \[CapitalDelta], 1] == 0 && Coefficient[ser, \[CapitalDelta], 2] == -4/9 && Coefficient[epsSer, \[CapitalDelta], 2] == 3/8 && (-4/9)/(3/8) == -32/27 == -4 (2/3)^3]; ]; (* ---- (v145) pairing atoms ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1207)
- [(* ---- (v97) sheet-conjugation bridge (P1 -> one [P]) ---- *) TA = {{0, 1, 0}, {1, 0, 0}, {2, -2, 1}}; SigM = DiagonalMatrix[{1, -1, -1}]; sig12 = {{0, 1, 0}, {1, 0, 0}, {0, 0, 1}}; e1v = {0, 0, 1}; e2v = {0, 1, 2}; e3v = {1, 0, 0}; QPm = (Q + SigM.Q.SigM)/2; checkExact["v97 Q_+ eigenvectors e1=(0,0,1) [l=1], e2=(0,1,2) [l=2], e3=(1,0,0) [l=3]", (QPm.e1v == 1 e1v) && (QPm.e2v == 2 e2v) && (QPm.e3v == 3 e3v)]; checkExact["v97 T_A integer involution, det -1, fixes 1 and a; T_A swaps e2 <-> e3, fixes e1", (TA.TA == IdentityMatrix[3]) && (Det[TA] == -1) && (TA.one == one) && (TA.av == av) && (TA.e2v == e3v) && (TA.e3v == e2v) && (TA.e1v == e1v)]; checkExact["v97 anchor = conjugation-symmetric vector: a = e2+e3, 1 = a-e1; odd line e2-e3", (av == e2v + e3v) && (one == av - e1v) && (TA.(e2v - e3v) == -(e2v - e3v))]; ddir = {-1, 1, 0}; coeffs = LinearSolve[Transpose[{one, av, ddir}], TA.ddir]; checkExact["v97 one deck action: T_A = -1 on R^3/span{1,a} (like sigma_12); parity det T_A = det sigma_12 = -1, det Sigma = +1", (coeffs[[3]] == -1) && (sig12.ddir == -ddir) && (Det[sig12] == -1) && (Det[SigM] == 1)]; Gm = TA.SigM; RrotM = {{0, 0, -1}, {1, 0, -1}, {0, 1, -1}}; checkExact["v97 D4 closure: G = T_A.Sigma has order 4, char (t+1)(t^2+1) = char(v70 R_rot)", (MatrixPower[Gm, 4] == IdentityMatrix[3]) && (MatrixPower[Gm, 2] != IdentityMatrix[3]) && (Expand[CharacteristicPolynomial[Gm, t] + (t + 1) (t^2 + 1)] === 0) && (Expand[CharacteristicPolynomial[Gm, t] - CharacteristicPolynomial[RrotM, t]] === 0)]; Svars = Array[sv, {3, 3}]; solS = Quiet[Solve[Flatten[Svars.Gm - RrotM.Svars] == 0, Flatten[Svars]], Solve::svars]; Sgen = Svars /. First[solS]; detSgen = Factor[Det[Sgen]]; checkExact["v97 sheet-index lemma: det S always EVEN on the integer intertwiner space, minimum |det| = 2 = |Z2|", Module[{vars = Variables[detSgen], vals}, vals = Select[Abs[detSgen /. Thread[vars -> #]] & /@ Tuples[Range[-2, 2], Length[vars]], # =!= 0 &]; (And @@ (EvenQ /@ vals)) && (Min[vals] == 2)]]; checkExact["v97 Q (det = N_fam) does NOT intertwine G -> R_rot (independent bridge)", Q.Gm != RrotM.Q]; (* ---- (v98) discriminant dictionary derived ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L249)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [(* ---- (v140) canonical map ---- *) Module[{charf, cu, cmu, cw}, charf[m_] := Mod[Round[Arg[#]/(Pi/2)], 4] & /@ Diagonal[m]; cu = charf[DiagonalMatrix[{1, I, -I}]]; cmu = charf[-DiagonalMatrix[{1, I, -I}]]; cw = charf[DiagonalMatrix[{I, I^2, I^3}]]; checkExact["v140 canonical map: deck U chars (0,1,3) miss 2; -U = (2,3,1) and i^Q+ = (1,2,3) both have SET {1,2,3} = H^1; i^Q+ assignment = Q+, -U assignment = Q+ o rho (one Z3 rotation apart)", cu == {0, 1, 3} && cmu == {2, 3, 1} && cw == {1, 2, 3} && Sort[cmu] == {1, 2, 3} == Sort[cw] && cmu == (cw[[#]] & /@ {2, 3, 1})]; ]; (* ---- (v141) deck selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1122)

## 2026-06-12 (sync infrastructure: single-source script index, content maps, one audit)

[documents/changelog/sections/023-source.tex:155-201](../../../../documents/changelog/sections/023-source.tex#L155) · `section:17ff6c6cf5ac233d153f` · subsection

Single-source script index. The master script [formula in source] check table ( tex-artefacts/verification.tex) and the website ScriptIndex.tsx are now generated from one registry ( script_registry.csv [formula in source] script_clusters.csv in verification/) by make_script_index.py; both targets carry a generated-file header and are never edited by hand. Content maps without splitting the papers. verification/make_d

Explicit source references:

- [verification/v91_spine_tetrahedron.py](../../../../verification/v91_spine_tetrahedron.py#L1) · explicit_script_identifier
- [verification/v85_master_cover.py](../../../../verification/v85_master_cover.py#L1) · explicit_script_identifier
- [verification/v17_hexagonal_resolvent.py](../../../../verification/v17_hexagonal_resolvent.py#L1) · explicit_script_identifier
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/docs_map.csv](../../../../verification/docs_map.csv#L1) · explicit_file_citation
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [ARCH.SPINE.01](../../../../verification/status_ledger.csv#L165) · explicit_claim_identifier · original status at linked ledger row
- [verification/script_registry.csv](../../../../verification/script_registry.csv#L1) · explicit_file_citation
- [verification/v19_monodromy_moduli.py](../../../../verification/v19_monodromy_moduli.py#L1) · explicit_script_identifier
- [verification/audit_baseline.json](../../../../verification/audit_baseline.json#L1) · explicit_file_citation
- [verification/make_docs_map.py](../../../../verification/make_docs_map.py#L1) · explicit_file_citation
- [verification/script_clusters.csv](../../../../verification/script_clusters.csv#L1) · explicit_file_citation
- [verification/make_script_index.py](../../../../verification/make_script_index.py#L1) · explicit_file_citation
- [verification/website_map.csv](../../../../verification/website_map.csv#L1) · explicit_file_citation
- [README.md](../../../../README.md#L1) · explicit_file_citation
- [verification/audit_sync.py](../../../../verification/audit_sync.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* ---- (v84) frozen registry decimals recompute from the axioms ---- *) phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); FU1[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 41 Log[1/phiseam[a]]; aStar = a /. FindRoot[FU1[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; check["v84 ALPHA_INV frozen", 1/aStar, 137.0359992168407125035379`30, 10^-20]; lamC = Sqrt[phi0 (1 - phi0)]; check["v84 SIN2_THETA12_SEED frozen", 1/3 - phi0/2, 0.3067473572449105696786871`30, 10^-20]; check["v84 SIN2_THETA13 frozen", phi0 Exp[-5/6], 0.02310843515888110429328466`30, 10^-20]; check["v84 BETA_BIREFRINGENCE_DEG frozen", (phi0/(4 Pi)) (180/Pi), 0.2424350309009295284924315`30, 10^-20]; check["v84 OMEGA_B frozen", (1 - 1/(4 Pi)) phi0, 0.04894066266545011220054565`30, 10^-20]; check["v84 LAMBDA_C frozen", lamC, 0.2243762368847217731120972`30, 10^-20]; check["v84 S23_CKM frozen", phi0/(1 + lamC), 0.04342778843220215630289116`30, 10^-20]; check["v84 S13_CKM frozen", lamC^3/3, 0.003765384454486429837965432`30, 10^-20]; check["v84 DELTA_CKM_RAD frozen", Pi/3 + 3 lamC^2, 1.198231638232244084651243`30, 10^-20]; check["v84 MMU_OVER_MTAU frozen", (8/7) phi0, 0.06076794534496631692490568`30, 10^-20]; check["v84 ME_OVER_MMU frozen", (12/7) phi0^2, 0.004846725425651567674771059`30, 10^-20]; checkExact["v84 MU_OVER_MD = 55/117 exactly", 55/117 == 55/117]; check["v84 MC_OVER_MS frozen", (34/47)/phi0, 13.60499710285539356302651`30, 10^-20]; check["v84 MT_OVER_MB frozen", (3/26)/phi0^2, 40.8115130177002629681607`30, 10^-20]; check["v84 MSCAL_OVER_MBAR frozen", c3^(7/2), 0.00001256494208322844896998079`30, 10^-20]; check["v84 RHOL_OVER_MBAR4 frozen", (3/(4 Pi^2)) Exp[-2/aStar], 7.125329526706216792033797`30 10^-121, 10^-15]; checkExact["v84 theta12 variants distinct (seed < seam < nonlin band)", (1/3 - phi0/2) < (1/3 - 1/(12 Pi))]; (* ---- (v85) master cover: GL(2) covariance on the anchor plane ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L38)
- [(* v431 (1): two-family split forced by 30 = 2*3*5 *) checkExact["v431 E8.DEGREE.LADDER.01 (i): E8 exponents = phi(30)=8 totatives of h=30=2*N_fam*g_car; coprime to 6 => +-1 mod 6, so degrees occupy ONLY {0,2} mod 6", exps == tot30 && EulerPhi[h] == 8 && h == 2*3*5 && expMod6 == {1, 5} && degMod6 == {0, 2}]; (* v431 (2): 6k family = 6 x spine {2,3,4,5} = v91 anchor a=(1,1,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2663)

## 2026-06-12 (tfpt_3 / tfpt_4 style alignment + box reduction)

[documents/changelog/sections/023-source.tex:202-220](../../../../documents/changelog/sections/023-source.tex#L202) · `section:958f74ef121b831419d8` · subsection

Shared header/footer on tfpt_3. tfpt_3_e8_audit_bootstrap dropped its custom footmarkers footer (the post-collapse four- \ artefact) and inherits the shared tfpt_style header/footer with the version stamp; the box-orphan needspace guards are kept. Fewer boxes, embedded in text. Narrative/commentary callouts converted to run-in bold paragraphs (boxed one-line formulas to keyeq): tfpt_3 from [formula in source] to [for

## 2026-06-12 (tfpt_1 / tfpt_2 style alignment + box reduction)

[documents/changelog/sections/023-source.tex:221-241](../../../../documents/changelog/sections/023-source.tex#L221) · `section:5cb9ec06306c576c2af2` · subsection

Shared header/footer everywhere. tfpt_1_architecture_e8 dropped its custom footmarkers footer (which after the marker collapse showed four redundant ) and now inherits the shared tfpt_style header/footer with the version stamp, identical to every other document. Fewer boxes, embedded in text. The narrative/commentary callouts of both documents are converted to run-in bold paragraphs (and the boxed one-line formulas t

Explicit source references:

- [COSMO.NSTAR.01](../../../../verification/status_ledger.csv#L160) · explicit_claim_identifier · original status at linked ledger row
- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)

## 2026-06-12 (marker simplification to 4 classes + status reconciliation)

[documents/changelog/sections/023-source.tex:242-263](../../../../documents/changelog/sections/023-source.tex#L242) · `section:4f6387455280982ea775` · subsection

Four-class display markers. The reader-facing marker system is collapsed from eleven symbols to four: \ exact / machine-proven (identity, Lie/lattice, formalised, numerical FP), \ conditional (physical / bridge / readout under named hypotheses), \ open / axiom, and \ kill test. tex-artefacts/tfpt_style.tex defines mE/ mC/ mO/ mX and keeps the legacy tI tX names as aliases that render their class. All marker call-site

Explicit source references:

- [COSMO.NSTAR.01](../../../../verification/status_ledger.csv#L160) · explicit_claim_identifier · original status at linked ledger row
- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_script_identifier
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)

## 2026-06-12 (version system, predictions/K5, readability pass B3)

[documents/changelog/sections/023-source.tex:264-302](../../../../documents/changelog/sections/023-source.tex#L264) · `section:9b652b6d86057eb55f7d` · subsection

Authors, auto-date and auto-version on every paper. New single source tex-artefacts/version.tex defines TFPTauthors (Stefan Hamann, Alessandro Rizzo), a curated TFPTversion, and a title/footer date stamp ( today [formula in source] version [formula in source] revision). build.sh writes the auto build revision (git commit count) into the gitignored tex-artefacts/version-auto.tex, so every document's title page and pag

Explicit source references:

- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v20_lepton_c_derivation.py](../../../../verification/v20_lepton_c_derivation.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v18_quark_yukawa.py](../../../../verification/v18_quark_yukawa.py#L1) · explicit_script_identifier
- [verification/v23_anchor_generator.py](../../../../verification/v23_anchor_generator.py#L1) · explicit_script_identifier
- [verification/v14_carrier_uniqueness.py](../../../../verification/v14_carrier_uniqueness.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [verification/v108_pascal_ladder.py](../../../../verification/v108_pascal_ladder.py#L1) · explicit_script_identifier
- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [verification/v46_grand_mass_volume.py](../../../../verification/v46_grand_mass_volume.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v107) quantum-clock target ---- *) checkExact["v107 per-l clock: l=0 (la-1)(la+2), l=1 la(la+1); l>=2 complex Re=-1/2", (Factor[la^2 + la + (0 - 2)] == (la - 1) (la + 2)) && (Factor[la^2 + la + (2 - 2)] == la (la + 1)) && (Re[la /. Solve[la^2 + la + 4 == 0, la]] == {-1/2, -1/2})]; checkExact["v107 cusp-ladder cross-link: decay set {0,-1,-2} = -Spec(Q diag(0,1,1)) = -N_fam x cusp", Module[{Vw = Q.DiagonalMatrix[{0, 1, 1}]}, Sort[Eigenvalues[Vw]] == {0, 1, 2}]]; checkExact["v107 exact target: (1/3)^6 = ((2/3)^6)^{log_{3/2}3}; ratio = 1 + log_{3/2}2", (FullSimplify[-6 Log[3] - (Log[3]/Log[3/2]) (6 Log[2] - 6 Log[3])] === 0) && (FullSimplify[Log[3]/Log[3/2] - (1 + Log[2]/Log[3/2])] === 0)]; check["v107 bend log_{9/4}(3) = 1.354756; seam coupling 1/(3Pi) = 0.106103", Log[3]/Log[9/4], 1.3547556457`10, 10^-9]; (* ---- (v108) Pascal ladder ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L471)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *) checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+", Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16]; checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car", Sort[Abs[plLeft[K]]] == {1, 4, 6} && Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar]; checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car", 4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15]; (* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L168)

## 2026-06-12 (tex-artefacts refactor + introduction visual pass B2)

[documents/changelog/sections/023-source.tex:303-330](../../../../documents/changelog/sections/023-source.tex#L303) · `section:826ddf772de04049b71a` · subsection

Shared imports moved to tex-artefacts/. The shared, imported-only TeX fragments ( tfpt_style.tex, tfpt_figures.tex, tfpt_docset.tex, tfpt_status.tex) now live in a dedicated tex-artefacts/ folder; all nine active documents input them via tex-artefacts/<name> (and tfpt_style loads tex-artefacts/tfpt_figures). changelog.tex stays at the repo root because it is also a standalone build.sh notes deliverable. The make_mani

Explicit source references:

- [README.md](../../../../README.md#L1) · explicit_file_citation
- [verification/make_manifest.py](../../../../verification/make_manifest.py#L1) · explicit_file_citation

## 2026-06-12 (visual pass: box reduction B1)

[documents/changelog/sections/023-source.tex:331-340](../../../../documents/changelog/sections/023-source.tex#L331) · `section:37c689285c5fc6a40772` · subsection

Box reduction (B1). The [formula in source] non-load-bearing aside boxes (audit / recorded / interpretation: auditbox/ audbox/ intbox/ resbox/ roadbox) across tfpt_1, tfpt_2, tfpt_3 and origin_theory are converted to inline bold run-in paragraphs — the reviewer's prescription that an audit fingerprint must not carry the same visual volume as a theorem. The loud box families are now only keybox (claim), winbox (result

## 2026-06-12 (visual pass: shared figures, badges, marker typology)

[documents/changelog/sections/023-source.tex:341-355](../../../../documents/changelog/sections/023-source.tex#L341) · `section:58cade7e0ae49570c7f2` · subsection

Shared figure library tfpt_figures.tex ( input by tfpt_style): reusable TikZ macros for the architecture claim stack ( TFPTclaimstack[zone], B3), the anchor cockpit [formula in source] (B4), the [formula in source] glue diagram (B5), the [formula in source] motif map (B6) and the [formula in source] action lattice (B7). The claim stack and a marker badge bar are now shown near the front of every document, each highli

## 2026-06-12 (review pass on list.txt)

[documents/changelog/sections/023-source.tex:356-381](../../../../documents/changelog/sections/023-source.tex#L356) · `section:b7fc94b9c310d988cbec` · subsection

Claim hygiene (review section A). The introduction's one-sentence claim is softened from ``derives all constants'' to ``constructs a discrete compiler; physical readouts run through named, status-typed bridges''; the ledger zombie in FLAV.QRATIO.01 is removed (the statement no longer says ``stays [P]'' — ratios are \ closed on the derived stratum, only the absolute scale stays , with an explicit forbidden-wording not

Explicit source references:

- [FLAV.QRATIO.01](../../../../verification/status_ledger.csv#L25) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-12 (later)

[documents/changelog/sections/024-source.tex:1-11](../../../../documents/changelog/sections/024-source.tex#L1) · `section:e2e448f834c8b18c1b82` · subsection

Shared style and central status artifact. Two new single-source fragments: tfpt_style.tex (the canonical palette, status markers, marker key, veri reference, the four tcolorbox families with back-compat aliases, and one running header/footer) is now input by all eight documents — the per-paper duplicated preambles are gone; and tfpt_status.tex (``TFPT status at a glance'') gives one canonical overall-status card impo
