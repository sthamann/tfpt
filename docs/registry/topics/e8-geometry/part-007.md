# E8, lattices and glue — part 7

[Topic entry](../e8-geometry.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Inflation interface

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4622-4664](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4622) · `section:5fbc43aa96ffd3bc0ea8` · section

Machine checks for this section: v7_ gravity_ cosmo.py v86_ nstar_ reheating.py v494_ cosmo_ running_ mu_ record.py

Explicit source references:

- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_file_citation
- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_file_citation
- [verification/v494_cosmo_running_mu_record.py](../../../../verification/v494_cosmo_running_mu_record.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)

## Further simple bridges

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4665-4682](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4665) · `section:e7c5dbcd2cfde70056f9` · section

Machine checks for this section: v74_ compiler_ micro_ lemmas.py

Explicit source references:

- [verification/v74_compiler_micro_lemmas.py](../../../../verification/v74_compiler_micro_lemmas.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v73) k=c3/2 forced: variational factor x Gauss-Bonnet topology; Fursaev-Solodukhin S=A/4 ---- *) checkExact["k=c3/2=1/(16pi)=(1/2)*(1/(|Z2|*2pi*chi(S2))), chi(S2)=2; Fursaev-Solodukhin 4pi k = 1/4", Module[{c3 = 1/(8 Pi), chi = 2, Z2 = 2}, (c3/2 == 1/(16 Pi)) && (c3 == 1/(Z2*2 Pi*chi)) && (4 Pi*(c3/2) == 1/4)]]; (* ---- (v74) compiler micro-lemmas: pencil differences 2->16->48; anchor QF 41-25=16 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L352)

## Closures that the architecture rests on

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4683-4727](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4683) · `section:ba8c8a5a798bc2587f06` · section

Machine checks for this section: v36_ spectral_ action_ g2.py v4_ flavor_ matrix.py

Explicit source references:

- [verification/v36_spectral_action_g2.py](../../../../verification/v36_spectral_action_g2.py#L1) · explicit_file_citation
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [(* v477 (i): Frullani + the moment dictionary at flat weight *) frul = Integrate[(Exp[-aa tt] - Exp[-tt])/tt, {tt, 0, Infinity}, Assumptions -> aa > 0]; eig = Join[{1}, Table[1/4, 4], Table[1/6, 6]]; tr = Total[Exp[-tt (1 - bb # RR)] & /@ eig] - 11 Exp[-tt]; serR = Normal[Series[tr, {RR, 0, 2}]]; mu1f = Integrate[Coefficient[serR, RR, 1]/tt, {tt, 0, Infinity}]; mu2f = Integrate[Coefficient[serR, RR, 2]/tt, {tt, 0, Infinity}]; checkExact["v477 GRAV.ENTROPIC.SCALEFLOW.01 (i): the Frullani/scale-flow identity -Log[a] = Integrate[(e^{-a t}-e^{-t})/t] (symbolic) and the moment dictionary -- at the FLAT weight the maximally-symmetric relative trace integrates to exactly the v475 raw coefficients 3 b R + (17/24) b^2 R^2 (unit moments mu1 = mu2 = 1): the raw entropic action is the unit-moment point of a scale-measure family", frul == -Log[aa] && Simplify[mu1f - 3 bb] == 0 && Simplify[mu2f - (17/24) bb^2] == 0]; (* v477 (ii): the one moment condition + closure + v36 consistency *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3071)
- [(* ---- (v24) quark ratio closure ---- *) checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117]; checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47]; checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26]; check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3]; check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2]; (* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L105)
- [(* v475 (iii): the Lorentzian timelike positivity witness *) gL = DiagonalMatrix[{-1, 1, 1, 1}]; mM = Outer[Times, {vv, 0, 0, 0}, {vv, 0, 0, 0}]; evT = Sort[Eigenvalues[(gL + aal mM) . Inverse[gL]]]; evS = Sort[Eigenvalues[(gL + aal Outer[Times, {0, vv, 0, 0}, {0, vv, 0, 0}]) . Inverse[gL]]]; checkExact["v475 GRAV.ENTROPIC.SCALARON.01 (iii): the Lorentzian-positivity witness -- on Minkowski a TIMELIKE gradient gives G g^-1 eigenvalues {1 - alpha v^2, 1, 1, 1} (nonpositive for v^2 >= 1/alpha, ln undefined) while a SPACELIKE gradient gives {1 + alpha v^2, 1, 1, 1} (positive for all v) -- the v473 caveat exhibited, the OS route sturdier", Sort[evT] == Sort[{1 - aal vv^2, 1, 1, 1}] && Sort[evS] == Sort[{1 + aal vv^2, 1, 1, 1}]]; ]; (* ==== v477 round: the scale-flow representation of the entropic action -- the exact content: the Frullani identity Integrate[(e^{-a t}-e^{-t})/t] = -Log[a], the moment dictionary (flat weight = unit moments = the v475 raw coefficients 3 b R + (17/24) b^2 R^2), the ONE moment condition mu2/mu1^2 = (72/17)(8 pi)^9 with the exact closure (4608 pi^2/17)/((72/17)(8 pi)^9) = c3^7, and the v36 consistency f0 = 6 (4 pi)^2/c3^7 <=> M^2 = c3^7 Mbar^2; mirrors v477 (the chi-form quadrature is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3052)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)

## Status summary and open audit points

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4728-4819](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4728) · `section:7a667667edab66880567` · section

Machine checks for this section: v22_ open_ gates_ audit.py

Explicit source references:

- [verification/v22_open_gates_audit.py](../../../../verification/v22_open_gates_audit.py#L1) · explicit_file_citation
- [verification/v118_hexagon_family_dictionary.py](../../../../verification/v118_hexagon_family_dictionary.py#L1) · explicit_script_identifier
- [verification/v142_frame_integrality.py](../../../../verification/v142_frame_integrality.py#L1) · explicit_script_identifier
- [verification/v531_coxeter_tensor_stage_a.py](../../../../verification/v531_coxeter_tensor_stage_a.py#L1) · explicit_script_identifier
- [verification/v141_deck_selection.py](../../../../verification/v141_deck_selection.py#L1) · explicit_script_identifier
- [verification/v122_margin_theorem.py](../../../../verification/v122_margin_theorem.py#L1) · explicit_script_identifier
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)
- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)
- [(* ---- (v140) canonical map ---- *) Module[{charf, cu, cmu, cw}, charf[m_] := Mod[Round[Arg[#]/(Pi/2)], 4] & /@ Diagonal[m]; cu = charf[DiagonalMatrix[{1, I, -I}]]; cmu = charf[-DiagonalMatrix[{1, I, -I}]]; cw = charf[DiagonalMatrix[{I, I^2, I^3}]]; checkExact["v140 canonical map: deck U chars (0,1,3) miss 2; -U = (2,3,1) and i^Q+ = (1,2,3) both have SET {1,2,3} = H^1; i^Q+ assignment = Q+, -U assignment = Q+ o rho (one Z3 rotation apart)", cu == {0, 1, 3} && cmu == {2, 3, 1} && cw == {1, 2, 3} && Sort[cmu] == {1, 2, 3} == Sort[cw] && cmu == (cw[[#]] & /@ {2, 3, 1})]; ]; (* ---- (v141) deck selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1122)
- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ==== v531 round: COX.STAGEA.TENSOR.01 -- the Stage A tensor clock. Exact mirrors: order 30, chi = Phi30, Ramanujan trace tomography, honest Phi15 scope, coprimality controls. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8300)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)

## Consolidated picture

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4820-4875](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4820) · `section:9e65ba01694e50f9c888` · section

A small grammar generates many sectors: the Standard-Model packet, flavor, the electroweak hierarchy, the cosmological constant, the metrology, and the inflation/CMB interface. The strongest new statements are exact: the decuple bridge ties [formula in source] to the tenth power of the stripped electroweak scale with [formula in source] ; the Hubble scale is the square root of [formula in source] ; and the Einstein n

Explicit source references:

- [verification/v531_coxeter_tensor_stage_a.py](../../../../verification/v531_coxeter_tensor_stage_a.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v531 round: COX.STAGEA.TENSOR.01 -- the Stage A tensor clock. Exact mirrors: order 30, chi = Phi30, Ramanujan trace tomography, honest Phi15 scope, coprimality controls. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8300)

## The Coxeter–cyclotomic compiler and the explicit [formula in source] construction

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4876-4913](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4876) · `section:ea7f8794d6601ffdeccd` · part

This short companion compresses the TFPT bridge layer to a single discrete object. The claim is that the Standard-Model family, the cosmological action ladder, the [formula in source] counting data, the flavor budget, inflation and the cosmological constant are not independent coincidences but projections of one structure: the even-weight code [formula in source] on [formula in source] slots, together with its [formu

## Theorem 1 — the even carrier code

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4914-4947](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4914) · `section:51465d9cabb4969da3d5` · section

tocsectionTheorem 1 Let [formula in source] be the rank- [formula in source] carrier, split [formula in source] (color [formula in source] , weak [formula in source] ). The one-generation spinor packet is the even exterior algebra, equivalently the even-weight binary code The two carrier roots [formula in source] , [formula in source] generate all hypercharges ( [formula in source] , [formula in source] , [formula in

Explicit source references:

- [TFPT.Carrier.Rigidity.unique_carrier_pair](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Rigidity.lean#L20) · explicit_lean_symbol
- [verification/v79_review_identities.py](../../../../verification/v79_review_identities.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v79) hypercharge Lucas-Binet D_n + the quark-ratio reading ---- *) checkExact["Lucas-Binet D_n=(3^n-(-2)^n)/5 = {1,1,7,13,55,133}; c_u/c_d = D_5/(N_fam^2 D_4) = 55/117", Module[{D}, D = Table[(3^n - (-2)^n)/5, {n, 1, 6}]; D == {1, 1, 7, 13, 55, 133} && D[[5]]/(Nfam^2 D[[4]]) == 55/117]]; (* ---- (v79) Inverse Anchor Theorem: 1^T M^-1 1 = 1/atom; a^T M^-1 a = 1 for R,K,L ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L385)

## Theorem 2 — Exterior–Action Duality

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4948-5006](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4948) · `section:8a4b44500953ff638855` · section

tocsectionTheorem 2 On [formula in source] the flip [formula in source] is even, so [formula in source] . The three relations [formula in source] form a symmetric association scheme (the even Hamming scheme on five bits) with The eigenvalues (computed directly) are [formula in source] and [formula in source] , with [formula in source] . The two graphs are named objects: The Standard-Model family is the valency side [

Explicit source references:

- [verification/v79_review_identities.py](../../../../verification/v79_review_identities.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v79) hypercharge Lucas-Binet D_n + the quark-ratio reading ---- *) checkExact["Lucas-Binet D_n=(3^n-(-2)^n)/5 = {1,1,7,13,55,133}; c_u/c_d = D_5/(N_fam^2 D_4) = 55/117", Module[{D}, D = Table[(3^n - (-2)^n)/5, {n, 1, 6}]; D == {1, 1, 7, 13, 55, 133} && D[[5]]/(Nfam^2 D[[4]]) == 55/117]]; (* ---- (v79) Inverse Anchor Theorem: 1^T M^-1 1 = 1/atom; a^T M^-1 a = 1 for R,K,L ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L385)

## Theorem 3 — the Coxeter closure equation selects [formula in source]

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5007-5019](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5007) · `section:f571553ff2e9f9a3c71c` · section

tocsectionTheorem 3 Requiring the even family to equal the action truncation through pair degree, [formula in source] , i.e. the unique positive-integer solution. At [formula in source] the two sides equal [formula in source] , so carrier exhaustion [formula in source] and the Coxeter period [formula in source] coincide only at five slots: [formula in source] and [formula in source] .

## Theorem 4 — the [formula in source] cyclotomic Coxeter compiler

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5020-5038](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5020) · `section:e9e51ef45afec3ba4ffb` · section

tocsectionTheorem 4 From the three atoms [formula in source] , with [formula in source] and [formula in source] : The [formula in source] exponents are the primitive residues modulo [formula in source] , and [formula in source] . The local SM algebra and the root atlas are the two arithmetic projections of [formula in source] :

## Theorem 5 — the root transition atlas and the positive-edge moment

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5039-5064](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5039) · `section:ec1ffa8eecd05cd52454` · section

tocsectionTheorem 5 The directed even-flips of [formula in source] are the complete graph [formula in source] : ( [formula in source] .) So the positive [formula in source] roots are the unordered transitions of one family; the second hypercharge moment, the positive-root count and the sum of the [formula in source] exponents coincide at [formula in source] . The CP pairing [formula in source] of the exponents gives 

## Theorem 6 — downstream readouts from [formula in source]

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5065-5140](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5065) · `section:3bdc8876b2b4284f0227` · section

tocsectionTheorem 6 All discrete budgets and the seam seed are functions of [formula in source] : Two-graph product table. With the carrier-pair graph [formula in source] ( [formula in source] ) and the family-corner graph [formula in source] on [formula in source] ( [formula in source] , [formula in source] ), every large budget is a product of the two graphs: i.e.\ ( [formula in source] , [formula in source] , [for

Explicit source references:

- [verification/v36_spectral_action_g2.py](../../../../verification/v36_spectral_action_g2.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v475 (iii): the Lorentzian timelike positivity witness *) gL = DiagonalMatrix[{-1, 1, 1, 1}]; mM = Outer[Times, {vv, 0, 0, 0}, {vv, 0, 0, 0}]; evT = Sort[Eigenvalues[(gL + aal mM) . Inverse[gL]]]; evS = Sort[Eigenvalues[(gL + aal Outer[Times, {0, vv, 0, 0}, {0, vv, 0, 0}]) . Inverse[gL]]]; checkExact["v475 GRAV.ENTROPIC.SCALARON.01 (iii): the Lorentzian-positivity witness -- on Minkowski a TIMELIKE gradient gives G g^-1 eigenvalues {1 - alpha v^2, 1, 1, 1} (nonpositive for v^2 >= 1/alpha, ln undefined) while a SPACELIKE gradient gives {1 + alpha v^2, 1, 1, 1} (positive for all v) -- the v473 caveat exhibited, the OS route sturdier", Sort[evT] == Sort[{1 - aal vv^2, 1, 1, 1}] && Sort[evS] == Sort[{1 + aal vv^2, 1, 1, 1}]]; ]; (* ==== v477 round: the scale-flow representation of the entropic action -- the exact content: the Frullani identity Integrate[(e^{-a t}-e^{-t})/t] = -Log[a], the moment dictionary (flat weight = unit moments = the v475 raw coefficients 3 b R + (17/24) b^2 R^2), the ONE moment condition mu2/mu1^2 = (72/17)(8 pi)^9 with the exact closure (4608 pi^2/17)/((72/17)(8 pi)^9) = c3^7, and the v36 consistency f0 = 6 (4 pi)^2/c3^7 <=> M^2 = c3^7 Mbar^2; mirrors v477 (the chi-form quadrature is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3052)
- [(* v477 (i): Frullani + the moment dictionary at flat weight *) frul = Integrate[(Exp[-aa tt] - Exp[-tt])/tt, {tt, 0, Infinity}, Assumptions -> aa > 0]; eig = Join[{1}, Table[1/4, 4], Table[1/6, 6]]; tr = Total[Exp[-tt (1 - bb # RR)] & /@ eig] - 11 Exp[-tt]; serR = Normal[Series[tr, {RR, 0, 2}]]; mu1f = Integrate[Coefficient[serR, RR, 1]/tt, {tt, 0, Infinity}]; mu2f = Integrate[Coefficient[serR, RR, 2]/tt, {tt, 0, Infinity}]; checkExact["v477 GRAV.ENTROPIC.SCALEFLOW.01 (i): the Frullani/scale-flow identity -Log[a] = Integrate[(e^{-a t}-e^{-t})/t] (symbolic) and the moment dictionary -- at the FLAT weight the maximally-symmetric relative trace integrates to exactly the v475 raw coefficients 3 b R + (17/24) b^2 R^2 (unit moments mu1 = mu2 = 1): the raw entropic action is the unit-moment point of a scale-measure family", frul == -Log[aa] && Simplify[mu1f - 3 bb] == 0 && Simplify[mu2f - (17/24) bb^2] == 0]; (* v477 (ii): the one moment condition + closure + v36 consistency *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3071)
- [(* ---- (v24) quark ratio closure ---- *) checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117]; checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47]; checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26]; check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3]; check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2]; (* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L105)

## Theorem 7 — the [formula in source] lift of the [formula in source] atlas

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5141-5388](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5141) · `section:f9b30725993b14c4ee95` · section

tocsectionTheorem 7 Since [formula in source] , one has the standard chain [formula in source] , with the exact branching (verified dimensions and root/weight counts): The adjoint [formula in source] of [formula in source] is [formula in source] and its spinor [formula in source] is [formula in source] . The TFPT dictionary makes each summand a known object: @llY@ piece & value & TFPT reading \\ [formula in source] &

Explicit source references:

- [P2.TYPING.01](../../../../verification/status_ledger.csv#L554) · explicit_claim_identifier · original status at linked ledger row
- [verification/v506_seam_clock_rigidity.py](../../../../verification/v506_seam_clock_rigidity.py#L1) · explicit_file_citation
- [verification/v53_compiler_core.py](../../../../verification/v53_compiler_core.py#L1) · explicit_file_citation
- [SEAM.TAU.FLAG.01](../../../../verification/status_ledger.csv#L576) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BIT.ORIGIN.01](../../../../verification/status_ledger.csv#L571) · explicit_claim_identifier · original status at linked ledger row
- [verification/v41_leg_assignment.py](../../../../verification/v41_leg_assignment.py#L1) · explicit_file_citation
- [verification/v499_p2_weights_deligne_bg.py](../../../../verification/v499_p2_weights_deligne_bg.py#L1) · explicit_file_citation
- [verification/v51_boundary_half_step.py](../../../../verification/v51_boundary_half_step.py#L1) · explicit_file_citation
- [verification/v528_seam_bit_twist_class_definition.py](../../../../verification/v528_seam_bit_twist_class_definition.py#L1) · explicit_script_identifier
- [SEAM.CLOCK.RIGIDITY.01](../../../../verification/status_ledger.csv#L570) · explicit_claim_identifier · original status at linked ledger row
- [verification/v503_qgeo_emergence_light.py](../../../../verification/v503_qgeo_emergence_light.py#L1) · explicit_script_identifier
- [SEAM.BIT.FREEDOM.01](../../../../verification/status_ledger.csv#L572) · explicit_claim_identifier · original status at linked ledger row
- [verification/v47_selection_theorem.py](../../../../verification/v47_selection_theorem.py#L1) · explicit_file_citation
- [verification/v491_p2_partition_corollary.py](../../../../verification/v491_p2_partition_corollary.py#L1) · explicit_file_citation
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_script_identifier
- [verification/v512_seam_tau_flag.py](../../../../verification/v512_seam_tau_flag.py#L1) · explicit_file_citation
- [verification/v521_seam_bit_rp_blind.py](../../../../verification/v521_seam_bit_rp_blind.py#L1) · explicit_script_identifier
- [QGEO.EMERGE.LIGHT.01](../../../../verification/status_ledger.csv#L567) · explicit_claim_identifier · original status at linked ledger row
- [verification/v507_seam_bit_origin.py](../../../../verification/v507_seam_bit_origin.py#L1) · explicit_file_citation
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_script_identifier
- [verification/v525_seam_bit_twist_blind.py](../../../../verification/v525_seam_bit_twist_blind.py#L1) · explicit_script_identifier
- [verification/v510_seam_bit_freedom.py](../../../../verification/v510_seam_bit_freedom.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v528 round: SEAM.BIT.TWISTCLASS.01 -- bit = twist-class choice. Exact mirrors: (i) cardinality lemma; (ii) 224-axis flip census; (iii) O-values. Pfaffian spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8213)
- [(* ==== v510 round: SEAM.BIT.FREEDOM.01 -- the freedom attack on the v506/v507 alignment bit: the POSITION half of the bit is topology. Exact content mirrored: (i) the DIHEDRAL CENSUS -- on the refined 2N-point seam circle D_16 has 17 involutions with EXACTLY ONE free (the antipodal shift by 8) and all 16 reflections have exactly 2 circle fixed points (8 site-axis + 8 edge-axis; robustness N = 8, 12; odd control N = 9: zero free), plus the quotient topology chi(C/antipode) = 0 (circle) vs chi(C/reflection) = 1 (interval, 2 boundary corners); (ii) the AUT COMPLETENESS -- Aut(C_8) = D_8 by brute force over all 8! = 40320 permutations and Aut(C_16) = D_16 by degree-2 propagation (all 32 candidates), so the census covers ALL circle symmetries; (iii) the Cl(16) DICHOTOMY CENSUS -- on explicit 256x256 Jordan-Wigner gammas the free deck's NS implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the implementers of ALL 16 reflections exist (one of the two spin lifts +-R) and square to SCALARS {2^7 (site-axis), 2^8 (edge-axis)} (split): NONSPLIT <=> FREE over the complete census; root dichotomy 2 (the +-quarter shifts) vs 0 total over all 16 reflections; (iv) the REAL-STRUCTURE TABLE -- the deck-commuting antiholomorphic involutions solve symbolically to exactly two families (M diagonal: mu conj z, fix line through the poles; M antidiagonal: mu/conj z, fix circle |z| = sqrt mu), and the unique mark-fixing real structure per configuration is equatorial/FREE for mu4 and generic-unit, real-axis/NOT-free for silver and generic-real, and NONEXISTENT for the hexagonal frame; (v) HARMONIC + FREE => mu4 -- the deck-pair cross-ratio (1-b)^2/(1+b)^2 = -1 solves exactly to b = +-i, with the lambda table (2, 1/2, 3/4, 5/4) real and the hexagonal lambda complex; (vi) the HONEST COUNTERWITNESSES -- the discrete witness {0,1,8,9} (shift-invariant, crossing, but not quarter-shift-invariant) and the continuous witness {+-1, +-(3+4i)/5} (pair cross-ratio -1/4, j = 148176/25 != 1728, clock does not preserve): the Fock dichotomy measures the CLASS, not the modulus. The Moebius/Klein covering models and the pillowcase branch control stay Python-side (v510). Mirrors v510. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5155)
- [(* ==== v507 round: SEAM.BIT.ORIGIN.01 -- the tautology attack on the v506 alignment bit, executed and refuted (Part A torus origin + Part B fermion dichotomy). Exact content mirrored: (i) the HALF-PERIOD DESCENT -- the fixed points of w -> -w on C/(Z + tau Z) are the 4 half-periods (2w in Lambda <=> coefficients in {0, 1/2}; the 1/3-control fails), a translation t_c descends iff 2c in Lambda (exactly the 3 nonzero half-periods), and the descended map sigma_i(x) = e_i + (e_i-e_j)(e_i-e_k)/(x-e_i) satisfies the exact curve-lift identity prod(sigma_i - e_l) = psi_i^2 prod(x - e_l) with RATIONAL psi_i, closing to Klein V4 symbolically; (ii) the CORE SOLVE -- the pair cross-ratio condition CR = -1 solves to lambda = -1 (sigma_1), 2 (sigma_2), 1/2 (sigma_3) exactly, union = the harmonic orbit with j = 1728, against j(3) = 21952/9 and j(hex) = 0; (iii) the STABILISER COUNTS -- the complete 24-triple enumeration gives (|Stab|, #involutions, #free) = (4,3,3) generic / (8,5,3) harmonic / (12,3,3) hexagonal, and in ALL three types the free involutions are EXACTLY the three sigma_c (the deck CLASS is forced); (iv) the CM FIXED POINT -- mult-by-i mod 2 fixes exactly the half-period (1,1) = c* = (1+tau)/2 while mult-by-rho 3-cycles all three, the lemniscatic clock ghat: x -> (x-1)/(x+1) needs the curve-lift factor psi = 2i/(x+1)^2 (the CM unit; t^2+1 irreducible over Q) and squares to the central -1/x; (v) the Cl(16) DICHOTOMY -- on explicit 256x256 Jordan-Wigner gammas the central implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the EDGE implementer Utilde_e = P_3 (g1+g5)(g2+g4)(g6-g16)(g7-g15)(g8-g14) (g9-g13)(g10-g12) implements the NS edge reflection and squares to the SCALAR +2^7 (split), and in the 32-element NS dihedral lift group the central deck has EXACTLY 2 square roots (the +-quarter shifts) vs 0 for the edge deck; (vi) the SILVER BIJECTION CENSUS -- all 8 mark bijections {+-1, +-(3+2 sqrt 2)} -> {0, 1, -1, inf} carry the deck z -> -z to the EDGE sigma_2/sigma_3 (never the central sigma_1), while all 8 mu4 bijections carry it to the CENTRAL sigma_1. The v493 circularity-audit direction and the 28/21 arrangement census stay Python-side (v507). Mirrors v507. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4545)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [(* ---- (v51) delta=1/2 glue-norm origin + (g_car,N_fam)/|mu4| unification ---- *) checkExact["glue norms = (g_car,N_fam)/|mu4|: q(D5)=5/4=gcar/4, q(A3)=3/4=Nfam/4", 5/4 == gcar/4 && 3/4 == Nfam/4]; checkExact["four ops forced: sum=2(root), diff=1/2(delta=|Z2|/4), prod=15/16(su4/S+), ratio=5/3(gcar/Nfam)", {5/4 + 3/4, 5/4 - 3/4, 5/4*3/4, (5/4)/(3/4)} == {(gcar + Nfam)/4, (gcar - Nfam)/4, gcar*Nfam/16, gcar/Nfam} == {2, 1/2, 15/16, 5/3}]; checkExact["delta=1/2 reproduces leptons: 4*1/(5/4-cos(2 Pi/3))=16/7, 1/(5/4-cos(Pi/3))=4/3", 4*1/(5/4 - Cos[2 Pi/3]) == 16/7 && 1/(5/4 - Cos[Pi/3]) == 4/3]; (* ---- (v52) K+xQ pencil endpoints ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L205)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v506 round: SEAM.CLOCK.RIGIDITY.01 -- clock rigidity, Route B of the v503 classification (Part A Moebius + Part B Fock). Exact content mirrored: (i) the COMPLETE SQUARE-ROOT SOLVE -- g^2 = deck in PGL2(C) has exactly two solutions z -> +-iz (tr != 0 forces diagonal with (a/d)^2 = -1; tr = 0 forces det = 0), both automatically of projective order 4; (ii) the D4 CENTER + ORDER-4 COUNT + the COUNTEREXAMPLE -- the mu4 stabiliser D4 = {i^k z, i^k/z} has exactly 2 order-4 elements (the clocks), both squaring to the deck, center = {id, deck}; the silver harmonic set {+-1, +-(3+2 sqrt 2)} has j = 1728 and full D4 but its 4-cycle squares to the CROSSING involution v/z, not the deck (deck non-central: 0 roots -- harmonicity alone insufficient); (iii) the Cl(16) IDENTITY -- on explicit 256x256 Jordan-Wigner gamma matrices, Utilde = prod_j (1 - g_j g_{j+8}) satisfies Utilde^2 = 256 g_1...g_16 EXACTLY (U^2 = (-1)^F, the forced nonsplit Z4), the R implementer squares to +256 (split control), and the volume element anticommutes with every gamma; (iv) the N-ARITHMETIC -- S4 element orders {1,2,3,4} (faithfulness kills n >= 5: max cyclic image order < n for n = 5..8), free orbits force n | 4, the cusp side kills n = 6 (deg(lam^5-1) = 5 != 3 = deg(lam^3-1)), transfer spectrum {1, 64/729, 1/729} with gap (2/3)^6, and the generic 4-set stabiliser V4 = {+-z, +-2/z} has exponent 2 (not even the deck has a root). The full 24-triple stabiliser enumeration and the A4/hexagonal profile stay Python-side (v506 Part A). Mirrors v506. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4394)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)
- [(* ==== v491 round: P2.PARTITION.01 -- g_car = 5 as the partition corollary of the four marks (the sharpening of v53). Exact content: 4 into exactly 3 positive integer parts is uniquely {1,1,2} => e = (4,5,2) => g_car = e2 = 5, |Z2| = e3 = 2, N_fam = e2 - e3 = 3 as corollaries; every assumption load-bearing (positivity / sum / part count / integrality negative controls); v53 needs all three targets, the partition only e1 = 4; sum rule 4(N-1)/2 = 4 iff N = 3; mirrors v491. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3116)
- [(* ==== v499 round: P2.TYPING.01 -- the P2 weight-typing postulate hardened: the anchor a = (1,1,2) as the Birkhoff-Grothendieck splitting exponents of the Deligne canonical extension E of the flavor connection (types the v491 check-9 residual). Exact content mirrored: (i) partition enumeration under the full typing (BG dictionary h^0 = 0 <=> a_i >= 1, exhaustive window) + the naive- typing negative control (h^1(E') = 3 forces deg -6, three splittings, e2 never 5) + the h^1 discrepancy (h^1(anchor bundle) = 1 != 3); (ii) the Deligne residue-trace degree (cusp exponents {0,1/3,2/3} = the unique lift of spec(lam^3 - 1) to [0,1), trace 1 per mark, deg E = -4, par-deg 0, witness A0* charpoly); (iii) the Schur-Horn permutohedron integer points {(2,2,0),(2,1,1)} with h^0 = 0 killing {2,2,0}; (iv) the Biswas Z3-cover degree arithmetic (genus 2, eigensheaves O(-2)^2, chi cross-check, regular-rep weights, the decomposable model {0,2,2} with h^0 = 1 = the unstable companion; deck double genus 1, j = 1728); (v) the n-mark formula e2 = (n-2)(n+1)/2 = 5 only at n = 4. The sympy symbolic parts (H^1 residue basis, monodromy group closure |<U,M0>| = 24, the 324-case stability skeleton) stay Python-side (v499). Mirrors v499. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3620)
- [(* ==== v525 round: SEAM.BIT.TWISTBLIND.01 -- "the twist-state kill": the NINTH side-blind test on the v512 scoreboard (8 -> 9); the free-plus-twist class is exhausted. Three exact mirrors: (i) the integer incidence frame + the sigma o r = +-sigma congruence mechanism (swap axes: sigma o r = sigma => the twisted Gram is the diagonal unitary congruence D M D = spectrally invisible; fixing axes at pi/2: sigma o r = -sigma = the eta flip); (ii) the pi/2-existence solveset of the mark-fixing axes + the exact counterwitness census ((3+4i)/5 unimodular but NEVER a root of unity up to order 64 -- no lattice mark-compatible reflection at any dyadic refinement); (iii) the delta <-> pi - delta mirror equivariance (the lattice reflection maps the m-mark set EXACTLY to the (8-m)-mark set -- the exact mechanism behind the Casimir mirror symmetry ln|omega(D)|(m) = ln|omega(D)|(8-m) and behind pi/2 as the symmetric point of every invariant readout). The Pfaffian insertion spectra, the Bogoliubov 2-of-16 pattern census, the defect energy and the 40-digit inertia certificates are numerical (mpmath), Python-only, flagged here. Mirrors v525. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8058)
- [(* ---- (v47) Boundary Carrier Selection Theorem (Theorem A) ---- *) checkExact["q(D5)+q(A3)=5/4+3/4=2 (E8 root norm); glue index sqrt(4*4/1)=4=|mu4|", 5/4 + 3/4 == 2 && Sqrt[4*4/1] == 4]; checkExact["only n=5 gives 16-dim D_n half-spinor (2^{n-1}=16) => D5", Select[Range[2, 8], 2^(# - 1) == 16 &] == {5}]; (* ---- (v48) EM boundary Ward decomposition (Theorem C) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L184)
- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ==== v521 round: SEAM.BIT.RPBLIND.01 -- "free OS positivity does not see delta": the anti-linear census solvesets on M(delta), the counterwitness census, the V4 -> D4 closure (face #13), the cut/mark incidence, the continuum axis elimination + Cauchy-Stieltjes factorisation, the clock-tower clause and the hex/silver precondition controls. The 40-digit lattice Gram inertia spectra (N = 16 / N = 32) are Python-only by the suite convention. Mirrors v521. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7479)
- [(* ==== v512 round: SEAM.TAU.FLAG.01 -- "the flag-transitivity equivalence web": the tau = i attack on the free RP seam circle. Test family M(delta) = {+-1, +-e^(i delta)}; bare mark-transitivity is delta-blind (pair-exchanging V4), FLAG transitivity <=> delta = pi/2 <=> tau = i. Six exact mirrors: (i) the V4/D4 census over five exact members incl. flag/arc orbit counts, (ii) the solveset equivalences + family identities, (iii) the odd-split closed form + arc Laplacian + K3 indicator, (iv) the twist mode identity + AB delta-blindness + j-rationality control, (v) the H4 centraliser rigidity (Schur), and (vi) the negative controls (hexagonal/silver/Z16 census/n = 3). Mirrors v512. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5675)

## Theorem 8 — the [formula in source] anchor microcode and the [formula in source] -ladder

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5389-5445](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5389) · `section:ef3ac63aa9e6dcddf33d` · section

tocsectionTheorem 8 — anchor microcode The parabolic flavor bundle [formula in source] on [formula in source] has splitting type [formula in source] , whose power sums [formula in source] generate the whole compiler budget:

Explicit source references:

- [verification/v407_dn_pairings_omega.py](../../../../verification/v407_dn_pairings_omega.py#L1) · explicit_file_citation
- [verification/v405_seam_equiv_omega.py](../../../../verification/v405_seam_equiv_omega.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.02](../../../../verification/status_ledger.csv#L475) · explicit_claim_identifier · original status at linked ledger row
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v832_anchor_flavor_checksum.py](../../../../verification/v832_anchor_flavor_checksum.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)

## Master statement and status

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5446-5495](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5446) · `section:8ab1f0d3c74dd8b84247` · section

tocsectionMaster statement Five carrier slots give [formula in source] ,\ four family corners give [formula in source] ,\ and [formula in source] gives the [formula in source] atlas. Equivalently: [formula in source] , [formula in source] , [formula in source] ; [formula in source] , [formula in source] , the [formula in source] Coxeter structure and the action ladder read the same five-slot pair-decuple. The Standar

## Appendix: machine-checkable [formula in source] construction

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5496-5542](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5496) · `section:9dbcdb3b5820985270ed` · section

The lift is reproducible by a short script (all entries below verified exactly).

## Appendix: ablation of the EM fixed point

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5543-5614](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5543) · `section:e398e2b82404aee49434` · part

The single sharpest reviewer test is: was the closure [formula in source] engineered so that [formula in source] comes out? The honest answer is an ablation — vary each input and see which actually move the root. Three one-parameter scans (all others held at their compiler values) separate the load-bearing integers from the fine last-digit selector.

Explicit source references:

- [verification/make_figures.py](../../../../verification/make_figures.py#L1) · explicit_file_citation

## Appendix: computational verification

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5615-5634](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5615) · `section:1b936c4aa48ef2007937` · section

The load-bearing identities of this document (marked , , ) are re-derived from [formula in source] alone and machine-checked by the suite in the repository folder verification/; the inline tags [verification/ [formula in source] ] point to the exact script. Relevant here: v1_e8_glue.py — the [formula in source] glue ( [formula in source] , [formula in source] , [formula in source] ). v2_carrier_pascal.py — [formula i

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_file_citation
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_file_citation
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_file_citation
- [verification/README.md](../../../../verification/README.md#L1) · explicit_file_citation
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## The Riemann–Hilbert side (what the monodromy fixes)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2641-2668](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2641) · `section:04d13a0d2894f95a8c21` · section

Constructing the rigid [formula in source] -symmetric local system explicitly (four monodromies [formula in source] , [formula in source] , [formula in source] ), the closure [formula in source] is solvable to machine precision, and the unique rotation [formula in source] has eigenvalues [formula in source] : the [formula in source] Coxeter element. \ This independently reproduces the corner-rotation [formula in sour

## The Parabolic Anchor Compiler

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2933-2945](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2933) · `section:2c70d6b249ff31626bca` · section

The anchor vector [formula in source] — the absolute value of the splitting type [formula in source] — is the smallest parabolic object that encodes the three operative structures at once: The [formula in source] norm is the glue/anti-degree, the [formula in source] norm [formula in source] is the [formula in source] positive-root hexagon, and the product is the sheet parity.

## Budget master table: everything is [formula in source] times a Coxeter datum

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2946-2959](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2946) · `section:4fd5a4b18f4ba9a372b6` · subsection

With [formula in source] fixed by parabolic degree zero, the entire integer landscape collapses: So [formula in source] and the spinor block [formula in source] are all functions of [formula in source] with the single new ingredient [formula in source] derived from parabolic degree zero (not posited).

## Flavor budget split, row sums, scalaron deficit

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2960-2982](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2960) · `section:da9fd7c73cc9015647dc` · subsection

The flavor budget splits into anchor [formula in source] two equal Coxeter copies: The residue row sums and full row sums read named objects, and the generation (column) sums are [formula in source] . \ Finally the scalaron exponent is the parabolic anti-degree plus the family rank, linking the stable family bundle [formula in source] directly to the inflation scale. The [formula in source] residue sum is the project

Explicit source references:

- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_file_citation

## Research Contract — QFT4D.OS.RECON.01 (the genuine 4D Euclidean lattice package)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:12869-12959](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L12869) · `section:44a203d3c701b05d1360` · section

Typing. A research contract \ (ledger row QFT4D.OS.RECON.01: Open, research contract), not a claim. This is step (3) of the DIMENSION.UPLIFT.FIREWALL.01 route ordering: the nonperturbative 4D existence statement that no perturbative or seam-level result can substitute for.

Explicit source references:

- [verification/v1008_master_assembly_scaffold.py](../../../../verification/v1008_master_assembly_scaffold.py#L1) · explicit_file_citation
- [verification/v989_lattice_gate_battery.py](../../../../verification/v989_lattice_gate_battery.py#L1) · explicit_file_citation
- [QFT4D.EG.ALLORDER.01](../../../../verification/status_ledger.csv#L444) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_script_identifier
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_file_citation
- [verification/v1013_thermodynamic_dynamics.py](../../../../verification/v1013_thermodynamic_dynamics.py#L1) · explicit_file_citation
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — CHIRAL4D.NOMIRROR.01 (the chiral 4D lattice matter theorem)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:12960-13028](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L12960) · `section:f0556283246eaeda72b3` · section

Typing. A research contract \ (ledger row CHIRAL4D.NOMIRROR.01: Open, research contract), not a claim. Step (4) of the firewall route ordering: chirality and mirror decoupling must be proven in the same 4D model that QFT4D.OS.RECON.01 constructs — the seam's [formula in source] and Chern/inflow structure are a boundary- anomaly signal, not yet 4D matter.

Explicit source references:

- [verification/v989_lattice_gate_battery.py](../../../../verification/v989_lattice_gate_battery.py#L1) · explicit_file_citation
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [docs/OPEN_PROBLEMS.md](../../../../docs/OPEN_PROBLEMS.md#L1) · explicit_file_citation
- [verification/v997_spin2_smg_witnesses.py](../../../../verification/v997_spin2_smg_witnesses.py#L1) · explicit_file_citation
- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_file_citation
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v997) GRAV.SPIN2.EMERGENCE.01: Barnes-Rivers ranks (5,3,1,1) ---- Python-only: Weyl^2 ghost residues, random-p numeric, SMG N=8 Fidkowski-Kitaev toy (spectrum / Spin(7) / Schmidt / edge). *)](../../../../verification/wolfram/tfpt_readouts.wl#L699)

## Research Contract — TFPT4D.LATTICE.ACTION.01 (the explicit finite 4D lattice action and its seven finite gates)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13530-13615](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13530) · `section:17f2d15b7cbfb816c548` · section

Typing. A research contract \ (ledger row TFPT4D.LATTICE.ACTION.01); route step (2) of the DIMENSION.UPLIFT.FIREWALL.01 ordering made concrete — the single object on which nearly all open 4D questions become simultaneously testable. Demand. Exhibit one fully explicit finite family of 4D Euclidean lattice theories [formula in source] where [formula in source] are the fundamental holonomies (TFPT fixes representation c

Explicit source references:

- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v989_lattice_gate_battery.py](../../../../verification/v989_lattice_gate_battery.py#L1) · explicit_file_citation
- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_file_citation
- [verification/v1013_thermodynamic_dynamics.py](../../../../verification/v1013_thermodynamic_dynamics.py#L1) · explicit_file_citation
- [verification/v1008_master_assembly_scaffold.py](../../../../verification/v1008_master_assembly_scaffold.py#L1) · explicit_file_citation

## TFPT als Grammatik und als Übersetzung

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/01_idee.tex:47-60](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/01_idee.tex#L47) · `section:7f51ad41a315a914969f` · section

TFPT liefert eine reichhaltige Grammatik: Träger, Darstellungen, Gitter, markierte Symmetrien, Projektoren und kurze wiederverwendete Zahlenformeln. Die Metapher vom Compiler meint eine Übersetzung zwischen diesen Beschreibungen. Sie sagt nicht, dass bereits ein kosmisches Computerprogramm identifiziert ist.

## Vom Wiedererkennen zur gemeinsamen Ursache

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/01_idee.tex:62-66](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/01_idee.tex#L62) · `section:6f71ab1e8c92bda060eb` · section

Die Anhänge zeigen keine einzige plötzliche Entdeckung, sondern eine Folge von Verschiebungen der Frage. Zuerst fällt auf, dass kleine geometrische und algebraische Daten in verschiedenen Rechnungen wiederkehren. Der Fünferträger führt zu einem 16-dimensionalen Spinor; die passenden Gitterfaktoren führen zu [formula in source] ; ein komplexer Viererträger zeigt 60 besondere Strahlen. Clocks, Ladungszuordnungen und Fl

## Warum die Verklebung wirklich zu E [formula in source] 8 führt

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/02_algebra.tex:27-57](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/02_algebra.tex#L27) · `section:dc570a18f524ed8c9083` · section

Die beiden positiven Wurzelgitter [formula in source] und [formula in source] besitzen Determinante vier und Diskriminantengruppe [formula in source] . Eine Diskriminantengruppe beschreibt hier die möglichen Restklassen, mit denen man das Gitter ohne Verlust der Ganzzahligkeit ergänzen kann. Für passende Generatoren gilt modulo eins Diagonal gekoppelt ist die Summe [formula in source] ganzzahlig. Die vier gemeinsamen

## Zwei Vierteldrehungen und der Index

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/07_seam.tex:98-103](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/07_seam.tex#L98) · `section:c4ffd1636c079cfb84f5` · section

Die innere Glue- [formula in source] wirkt auf den 248 Strömen mit Phasen [formula in source] auf Sektoren der Größen [formula in source] . Ihre Spur ist null. Die geometrische Vierteldrehung [formula in source] hat auf Stufe eins dagegen Spur [formula in source] . Die Operatoren sind somit nicht identisch. Eine Clock kann eine geometrische Drehung mit innerem Twist kombinieren; die beiden Faktoren bleiben getrennt. 

## T1 bis T8: der vollständige Vertrag

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/10_ausblick.tex:53-66](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/10_ausblick.tex#L53) · `section:d961ab70d61ba5ac29a4` · section

L9mmL62mmL79mm Tor& Was gemeinsam nachzuweisen ist& Was bisher dazu vorliegt\\ T1&Herkunft von P1/P2, Dimensionen, Markierungen und Auswahlregeln.&Exakte Konsequenzen festgelegter Daten; Gegenmodelle gegen Symmetrie-Eindeutigkeit. Herkunft offen.\\ T2&Native half-charge-markierte [formula in source] -Naht samt Skalierungslimes, Domänen, Energieabschätzungen und beiden Adjungierten.&Gitterhülle und Zielerweiterung kon

## Der genaue Ertrag der [formula in source] -Schalen

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex:82-96](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex#L82) · `section:cbeb85103b892f3b7d1b` · subsection

Die ersten sechs Werte sind [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] und [formula in source] . Daraus folgt für [formula in source] Hier ist der Primzahlbezug wirklich vorhanden. Die Selbstdualität des Gitters schließt die Poisson-Transformation auf dasselbe Gitter. Poisson-Summation gilt auch für nichtselbstduale Gitter und verbindet dann Gitter und 

## Was die negativen Routen konkret lehren

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex:109-115](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex#L109) · `section:8a28c8e255701869b4f0` · subsection

Der Jensen/Coxeter-Test r618 findet eine starre [formula in source] -Struktur auf der [formula in source] -Seite, während die verglichenen Jensen-Polynome mit ihrem Index variieren. Die gewählte Identifikation scheitert. Der Selberg-Kontakttest r638 besitzt im untersuchten Fall weiterhin einen negativen kleinsten Eigenwert von ungefähr [formula in source] ; eine Quadratvervollständigung hat die falsche signierte Form

## Eine neue Gegenprobe am Clebsch-Vorschlag

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/14_schatten_dimension.tex:24-47](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/14_schatten_dimension.tex#L24) · `section:049384dfe146a60b52d8` · section

Für einen Graph-Laplaceoperator [formula in source] definieren wir die mittlere Rückkehrfunktion und eine skalenabhängige Dimension durch Auf einem großen regelmäßigen dreidimensionalen Gitter entsteht zwischen der Gitter- und der endlichen Systemskala ein Bereich mit [formula in source] , also [formula in source] . Bei einem endlichen zusammenhängenden Graphen geht [formula in source] sowohl für sehr kleine als auch

## TFPT als Grammatik und als Übersetzung

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/01_idee.tex:47-60](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/01_idee.tex#L47) · `section:47b31f7d1c0cb37d2f3c` · section

TFPT liefert eine reichhaltige Grammatik: Träger, Darstellungen, Gitter, markierte Symmetrien, Projektoren und kurze wiederverwendete Zahlenformeln. Die Metapher vom Compiler meint eine Übersetzung zwischen diesen Beschreibungen. Sie sagt nicht, dass bereits ein kosmisches Computerprogramm identifiziert ist.

## Vom Wiedererkennen zur gemeinsamen Ursache

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/01_idee.tex:62-66](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/01_idee.tex#L62) · `section:3fd2f1193cda98918e0c` · section

Die Anhänge zeigen keine einzige plötzliche Entdeckung, sondern eine Folge von Verschiebungen der Frage. Zuerst fällt auf, dass kleine geometrische und algebraische Daten in verschiedenen Rechnungen wiederkehren. Der Fünferträger führt zu einem 16-dimensionalen Spinor; die passenden Gitterfaktoren führen zu [formula in source] ; ein komplexer Viererträger zeigt 60 besondere Strahlen. Clocks, Ladungszuordnungen und Fl

## Warum die Verklebung wirklich zu E [formula in source] 8 führt

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/02_algebra.tex:27-57](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/02_algebra.tex#L27) · `section:f35bf55f811b5f489d7c` · section

Die beiden positiven Wurzelgitter [formula in source] und [formula in source] besitzen Determinante vier und Diskriminantengruppe [formula in source] . Eine Diskriminantengruppe beschreibt hier die möglichen Restklassen, mit denen man das Gitter ohne Verlust der Ganzzahligkeit ergänzen kann. Für passende Generatoren gilt modulo eins Diagonal gekoppelt ist die Summe [formula in source] ganzzahlig. Die vier gemeinsamen

## Zwei Vierteldrehungen und der Index

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/07_seam.tex:98-103](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/07_seam.tex#L98) · `section:3181c3942c8b50d2b8d9` · section

Die innere Glue- [formula in source] wirkt auf den 248 Strömen mit Phasen [formula in source] auf Sektoren der Größen [formula in source] . Ihre Spur ist null. Die geometrische Vierteldrehung [formula in source] hat auf Stufe eins dagegen Spur [formula in source] . Die Operatoren sind somit nicht identisch. Eine Clock kann eine geometrische Drehung mit innerem Twist kombinieren; die beiden Faktoren bleiben getrennt. 

## T1 bis T8: der vollständige Vertrag

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/10_ausblick.tex:56-69](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/10_ausblick.tex#L56) · `section:26965ed2200cee435949` · section

L9mmL62mmL79mm Tor& Was gemeinsam nachzuweisen ist& Was bisher dazu vorliegt\\ T1&Herkunft von P1/P2, Dimensionen, Markierungen und Auswahlregeln.&Exakte Konsequenzen festgelegter Daten; Gegenmodelle gegen Symmetrie-Eindeutigkeit. Herkunft offen.\\ T2&Native half-charge-markierte [formula in source] -Naht samt Skalierungslimes, Domänen, Energieabschätzungen und beiden Adjungierten.&Gitterhülle und Zielerweiterung kon

## Der genaue Ertrag der [formula in source] -Schalen

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/12_schatten_arithmetik.tex:82-96](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/12_schatten_arithmetik.tex#L82) · `section:a425abe30d729823057f` · subsection

Die ersten sechs Werte sind [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] und [formula in source] . Daraus folgt für [formula in source] Hier ist der Primzahlbezug wirklich vorhanden. Die Selbstdualität des Gitters schließt die Poisson-Transformation auf dasselbe Gitter. Poisson-Summation gilt auch für nichtselbstduale Gitter und verbindet dann Gitter und 

## Was die negativen Routen konkret lehren

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/12_schatten_arithmetik.tex:109-115](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/12_schatten_arithmetik.tex#L109) · `section:beecd8fbf1df986ac09d` · subsection

Der Jensen/Coxeter-Test r618 findet eine starre [formula in source] -Struktur auf der [formula in source] -Seite, während die verglichenen Jensen-Polynome mit ihrem Index variieren. Die gewählte Identifikation scheitert. Der Selberg-Kontakttest r638 besitzt im untersuchten Fall weiterhin einen negativen kleinsten Eigenwert von ungefähr [formula in source] ; eine Quadratvervollständigung hat die falsche signierte Form

## Eine neue Gegenprobe am Clebsch-Vorschlag

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/14_schatten_dimension.tex:24-47](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/14_schatten_dimension.tex#L24) · `section:1b966b6b2bfa4af0d57f` · section

Für einen Graph-Laplaceoperator [formula in source] definieren wir die mittlere Rückkehrfunktion und eine skalenabhängige Dimension durch Auf einem großen regelmäßigen dreidimensionalen Gitter entsteht zwischen der Gitter- und der endlichen Systemskala ein Bereich mit [formula in source] , also [formula in source] . Bei einem endlichen zusammenhängenden Graphen geht [formula in source] sowohl für sehr kleine als auch

## Vorzeichen aus E8 und die noch fehlende Quellbasis

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/23_micro_v14.tex:3-7](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/23_micro_v14.tex#L3) · `section:9b89be7227e7c03590e5` · section

Der geordnete Standard-Gittercocycle [formula in source] wurde unabhängig aus einer einfachen E8-Basis aufgebaut. [formula in source] liefert den Kommutatorfaktor, Bilinearität die Cocycle-Identität. Alle 240 Wurzelkoordinaten sind ganzzahlig. Auf den 40 Clebsch-Kanten bestätigt die exakte F2-Elimination Rang 45 für die Antisymmetriegauge der Ortsfarben und Rang 285 für die zusätzliche kantenlokale Vermittlergauge. F

## T4: Chirale Nullmoden werden gebaut, aber nicht als Familien ausgegeben

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/24_fronts_v14.tex:40-51](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/24_fronts_v14.tex#L40) · `section:3a33b0ffc309758bd248` · section

Das einfachste Gitter-Weylsymbol [formula in source] besitzt acht Knoten, je einen an jeder Kombination [formula in source] . Ihre Chiralitäten wechseln; die Summe ist null. Eine anschauliche zweikomponentige Gleichung allein entfernt die zusätzlichen Arten daher nicht. Diskrete Weyl-Walks sind eine mögliche https://arxiv.org/abs/1708.00826Referenzkonstruktion, keine automatische Lösung dieses TFPT-Problems.

## T7: Warum ein Tensorbild noch keine Gravitation ist

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/24_fronts_v14.tex:68-76](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/chapters/24_fronts_v14.tex#L68) · `section:21088c2aa520860a7446` · section

Für freie massive bosonische Moden mit Lücke [formula in source] hat eine normalgeordnete bilineare Tensorobservable im Vakuum Spektralgewicht erst oberhalb der Zweiteilchenschwelle [formula in source] . Die Gitterproben [formula in source] , [formula in source] , bestätigen die Schwelle eins. Ein transversaler, spurloser Projektor besitzt zwar Rang zwei, verschiebt aber keine Energie zu null. Er erzeugt daher aus di

## S02

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:7-11](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L7) · `section:b19e3a81a50fad07254c` · subsection

TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md Explizite Präparation, Aufzeichnung, Rohwahrscheinlichkeiten, Ressourcen und Mehrzeittest. SHA-256: 065fa53688b8518f81e8d9ea9e9e5a55 7e44a597456bf2b29a49b9db2d6bc724 32mm

Explicit source references:

- [universal_room/TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md](../../../../universal_room/TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md#L1) · explicit_file_citation

## S03

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:12-16](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L12) · `section:cee356cc5b321f5dff9b` · subsection

TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md Gemeinsamer Ursprung: Zweizellenenergie, Verschränkung, Uhrsignal, Propagatorbrücke und TOE-Vertrag. SHA-256: 864bd44fa12d8deb88cb359742ee908b 8b5cc8a12cd2d39bc22c6fdced757b2e 32mm

Explicit source references:

- [universal_room/TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md](../../../../universal_room/TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md#L1) · explicit_file_citation

## S04

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:17-21](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L17) · `section:86eaa75068b5e7ef8abb` · subsection

TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md Frühe Gesamtsynthese mit Fixpunkthypothese, Zahlenübersicht und Einordnung zu RH und Komplexität; mehrere Aussagen später korrigiert. SHA-256: f62f91af70b43ce349a9e4c17f9e4887 7099ae9b6c992f0c1482f4eb77ee6694 32mm

Explicit source references:

- [universal_room/TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md](../../../../universal_room/TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md#L1) · explicit_file_citation

## S05

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:22-26](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L22) · `section:65131d23987d7a70ec1f` · subsection

Analyse_und_Rekonstruktion.md Gegenproben, harte und weiche Hülle, Vermittler, Viereruhr, GNS und physikalische Grenzen. SHA-256: 5726d25cb03443c93cb18d28a8b1589d b0eee06415a84995251875bb00883d60 32mm

Explicit source references:

- [universal_room/Analyse_und_Rekonstruktion.md](../../../../universal_room/Analyse_und_Rekonstruktion.md#L1) · explicit_file_citation

## S06

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:27-31](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L27) · `section:f05ef37b773f4ca01f58` · subsection

TFPT_Universalraum_Rekonstruktion_2026-09-14.md Quotienten 45/30, Register- und Quellenprüfung, Stabilizerhindernis, E8-Rückrekonstruktion. SHA-256: 4515aadc06b13c0216994bb3036bb201 380d00128ab4ce5e6f19f1e7e230fc1e 32mm

Explicit source references:

- [universal_room/TFPT_Universalraum_Rekonstruktion_2026-09-14.md](../../../../universal_room/TFPT_Universalraum_Rekonstruktion_2026-09-14.md#L1) · explicit_file_citation

## S07

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:32-36](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L32) · `section:580bdfb99cfd1c368115` · subsection

TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md Inversionshypothese, Matchingausführung, Registerrekurrenz, Clockblockade und endliche Faktorprüfung. SHA-256: b86f846bf2b20a78d2d8997bd303fe5f 4da82497c23f969e8e616e4d9361e95b 32mm

## S08

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:37-41](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L37) · `section:540200863860c86be656` · subsection

tfpt_anschluss_zellen_seam_2026-09-14.pdf Zellhülle, Tick-Lifts, Kettennumerik, Rotor/CAR-Zustandsgate, Pati-Salam-Läufe und Indexpräzisierungen. SHA-256: 6029544e7bb9ee2e3fa7f94717fa1d18 61b5d0b598e7543cd8abcde1ddf0e8c8 32mm

## S09

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:42-46](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L42) · `section:ae1ed8ee599891ac5f4e` · subsection

tfpt_compiler_universalraum_2026-09-13.pdf Grundmanuskript Version 1.0: Architektur, Standardmodell, Zahlen, Prozess, Register und T1 bis T8. SHA-256: 48ea9ae625ce418607eb718478525d80 2c52844183745f27849e17dd63bad43a 32mm

## S10

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:47-51](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L47) · `section:9b68ac5db35802e524da` · subsection

Eingefügter Text: Erklärung des Universalraums Gesprächstext: einfache Universalraum-Erklärung, hypothetische Anwendungen, Zuse und Wolfram. SHA-256: 5c314fd3f27634dfd0cc8e2ed56e5e64 2a457e08df9db9558ee6c962a7f8fd59 32mm

## S11

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex:52-55](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/main-v1.4/sources_manifest.tex#L52) · `section:5a6344f82e63e2269b4c` · subsection

Eingefügter Text: Die fünf gesetzten Fugen Fünf Fugen: Clebsch-Graph, Austausch, Sektortrennung, Orbitargument und Z4-Erweiterung. SHA-256: 79258cd3d27f5a8219ef3b7d597978ea eb6c2c1f0fd18cb636f0a70bbd548ca8

## TFPT als Grammatik und als Übersetzung

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/01_idee.tex:47-60](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/01_idee.tex#L47) · `section:60efa98fc9116eef9da1` · section

TFPT liefert eine reichhaltige Grammatik: Träger, Darstellungen, Gitter, markierte Symmetrien, Projektoren und kurze wiederverwendete Zahlenformeln. Die Metapher vom Compiler meint eine Übersetzung zwischen diesen Beschreibungen. Sie sagt nicht, dass bereits ein kosmisches Computerprogramm identifiziert ist.

## Vom Wiedererkennen zur gemeinsamen Ursache

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/01_idee.tex:62-66](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/01_idee.tex#L62) · `section:636b6089a783f1c5ff58` · section

Die Anhänge zeigen keine einzige plötzliche Entdeckung, sondern eine Folge von Verschiebungen der Frage. Zuerst fällt auf, dass kleine geometrische und algebraische Daten in verschiedenen Rechnungen wiederkehren. Der Fünferträger führt zu einem 16-dimensionalen Spinor; die passenden Gitterfaktoren führen zu [formula in source] ; ein komplexer Viererträger zeigt 60 besondere Strahlen. Clocks, Ladungszuordnungen und Fl

## Warum die Verklebung wirklich zu E [formula in source] 8 führt

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/02_algebra.tex:27-57](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/02_algebra.tex#L27) · `section:82eaf24607660bcbff6f` · section

Die beiden positiven Wurzelgitter [formula in source] und [formula in source] besitzen Determinante vier und Diskriminantengruppe [formula in source] . Eine Diskriminantengruppe beschreibt hier die möglichen Restklassen, mit denen man das Gitter ohne Verlust der Ganzzahligkeit ergänzen kann. Für passende Generatoren gilt modulo eins Diagonal gekoppelt ist die Summe [formula in source] ganzzahlig. Die vier gemeinsamen

## Zwei Vierteldrehungen und der Index

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/07_seam.tex:98-103](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/07_seam.tex#L98) · `section:0d359d1ab7db2c14501d` · section

Die innere Glue- [formula in source] wirkt auf den 248 Strömen mit Phasen [formula in source] auf Sektoren der Größen [formula in source] . Ihre Spur ist null. Die geometrische Vierteldrehung [formula in source] hat auf Stufe eins dagegen Spur [formula in source] . Die Operatoren sind somit nicht identisch. Eine Clock kann eine geometrische Drehung mit innerem Twist kombinieren; die beiden Faktoren bleiben getrennt. 

## T1 bis T8: der vollständige Vertrag

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/10_ausblick.tex:56-69](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/10_ausblick.tex#L56) · `section:8e06d695d28d64157e5d` · section

L9mmL62mmL79mm Tor& Was gemeinsam nachzuweisen ist& Was bisher dazu vorliegt\\ T1&Herkunft von P1/P2, Dimensionen, Markierungen und Auswahlregeln.&Exakte Konsequenzen festgelegter Daten; Gegenmodelle gegen Symmetrie-Eindeutigkeit. Herkunft offen.\\ T2&Native half-charge-markierte [formula in source] -Naht samt Skalierungslimes, Domänen, Energieabschätzungen und beiden Adjungierten.&Gitterhülle und Zielerweiterung kon

## Der genaue Ertrag der [formula in source] -Schalen

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/12_schatten_arithmetik.tex:82-96](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/12_schatten_arithmetik.tex#L82) · `section:171e1728c5ae88592388` · subsection

Die ersten sechs Werte sind [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] und [formula in source] . Daraus folgt für [formula in source] Hier ist der Primzahlbezug wirklich vorhanden. Die Selbstdualität des Gitters schließt die Poisson-Transformation auf dasselbe Gitter. Poisson-Summation gilt auch für nichtselbstduale Gitter und verbindet dann Gitter und 

## Was die negativen Routen konkret lehren

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/12_schatten_arithmetik.tex:109-115](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/12_schatten_arithmetik.tex#L109) · `section:8cb1d5b7919591505357` · subsection

Der Jensen/Coxeter-Test r618 findet eine starre [formula in source] -Struktur auf der [formula in source] -Seite, während die verglichenen Jensen-Polynome mit ihrem Index variieren. Die gewählte Identifikation scheitert. Der Selberg-Kontakttest r638 besitzt im untersuchten Fall weiterhin einen negativen kleinsten Eigenwert von ungefähr [formula in source] ; eine Quadratvervollständigung hat die falsche signierte Form

## Eine neue Gegenprobe am Clebsch-Vorschlag

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/14_schatten_dimension.tex:24-47](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/14_schatten_dimension.tex#L24) · `section:57f7b37aa0bf6c8f74f2` · section

Für einen Graph-Laplaceoperator [formula in source] definieren wir die mittlere Rückkehrfunktion und eine skalenabhängige Dimension durch Auf einem großen regelmäßigen dreidimensionalen Gitter entsteht zwischen der Gitter- und der endlichen Systemskala ein Bereich mit [formula in source] , also [formula in source] . Bei einem endlichen zusammenhängenden Graphen geht [formula in source] sowohl für sehr kleine als auch

## Vorzeichen aus E8 und die noch fehlende Quellbasis

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/23_micro_v14.tex:6-10](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/23_micro_v14.tex#L6) · `section:c1ff6a1ef440790cd257` · section

Der geordnete Standard-Gittercocycle [formula in source] wurde unabhängig aus einer einfachen E8-Basis aufgebaut. [formula in source] liefert den Kommutatorfaktor, Bilinearität die Cocycle-Identität. Alle 240 Wurzelkoordinaten sind ganzzahlig. Auf den 40 Clebsch-Kanten bestätigt die exakte F2-Elimination Rang 45 für die Antisymmetriegauge der Ortsfarben und Rang 285 für die zusätzliche kantenlokale Vermittlergauge. F

## T4: Chirale Nullmoden werden gebaut, aber nicht als Familien ausgegeben

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/24_fronts_v14.tex:43-54](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/24_fronts_v14.tex#L43) · `section:d963030ec878ae470c30` · section

Das einfachste Gitter-Weylsymbol [formula in source] besitzt acht Knoten, je einen an jeder Kombination [formula in source] . Ihre Chiralitäten wechseln; die Summe ist null. Eine anschauliche zweikomponentige Gleichung allein entfernt die zusätzlichen Arten daher nicht. Diskrete Weyl-Walks sind eine mögliche https://arxiv.org/abs/1708.00826Referenzkonstruktion, keine automatische Lösung dieses TFPT-Problems.

## T7: Warum ein Tensorbild noch keine Gravitation ist

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/24_fronts_v14.tex:71-79](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/24_fronts_v14.tex#L71) · `section:5b01dff035ea648f1b6d` · section

Für freie massive bosonische Moden mit Lücke [formula in source] hat eine normalgeordnete bilineare Tensorobservable im Vakuum Spektralgewicht erst oberhalb der Zweiteilchenschwelle [formula in source] . Die Gitterproben [formula in source] , [formula in source] , bestätigen die Schwelle eins. Ein transversaler, spurloser Projektor besitzt zwar Rang zwei, verschiebt aber keine Energie zu null. Er erzeugt daher aus di

## Rationale Intervalle statt nur Dezimalzahlen

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/25_revision_v15.tex:92-107](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/25_revision_v15.tex#L92) · `section:2a989bcbb69f2e5bdd38` · section

Der ganzzahlige Gruppenalgebraoperator erhält ein Specht-Schnittgitter in seinem rationalen invarianten Teilraum. Daher ist sein charakteristisches Polynom monisch ganzzahlig. Aus [formula in source] folgt die vorab bekannte Koeffizientenabschätzung [formula in source] Siebzehn Primmoduli liefern einen 452-Bit-CRT-Modulus oberhalb der nötigen 428-Bit-Schranke. Eine achtzehnte Primzahl prüft die Rekonstruktion unabhän

## Alle acht Tore mit genauem Rest

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/25_revision_v15.tex:318-335](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/chapters/25_revision_v15.tex#L318) · `section:1157d01ec25653c8097b` · section

L13mmL57mmL67mm Tor&Neuer Beitrag&Vollständig fehlender Nachweis\\ T1&Fester-Delta-Record, endliche Q-Zeiten, kohärente Logik&Native Wedge-, Q-, Schalt- und Controllerherkunft aus einer primitiven Quelle\\ T2&Norm- und energiekontrollierter relativer Half-Charge-Adapter&Renormiertes lokales Feld der tatsächlichen Quelle, E8-/Clock-Zuordnung\\ T3&Skalierende Referenzfamilien, exakte Gaps, linearer gefüllter Kettensekt

## S02

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:7-11](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L7) · `section:cd8dc34f9e550e51961e` · subsection

TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md Explizite Präparation, Aufzeichnung, Rohwahrscheinlichkeiten, Ressourcen und Mehrzeittest. SHA-256: 065fa53688b8518f81e8d9ea9e9e5a55 7e44a597456bf2b29a49b9db2d6bc724 32mm

Explicit source references:

- [universal_room/TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md](../../../../universal_room/TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md#L1) · explicit_file_citation

## S03

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:12-16](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L12) · `section:3b9468b6c21f262e79c7` · subsection

TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md Gemeinsamer Ursprung: Zweizellenenergie, Verschränkung, Uhrsignal, Propagatorbrücke und TOE-Vertrag. SHA-256: 864bd44fa12d8deb88cb359742ee908b 8b5cc8a12cd2d39bc22c6fdced757b2e 32mm

Explicit source references:

- [universal_room/TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md](../../../../universal_room/TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md#L1) · explicit_file_citation

## S04

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:17-21](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L17) · `section:cbbd0312485a4044b734` · subsection

TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md Frühe Gesamtsynthese mit Fixpunkthypothese, Zahlenübersicht und Einordnung zu RH und Komplexität; mehrere Aussagen später korrigiert. SHA-256: f62f91af70b43ce349a9e4c17f9e4887 7099ae9b6c992f0c1482f4eb77ee6694 32mm

Explicit source references:

- [universal_room/TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md](../../../../universal_room/TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md#L1) · explicit_file_citation

## S05

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:22-26](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L22) · `section:7591e0005868df00212b` · subsection

Analyse_und_Rekonstruktion.md Gegenproben, harte und weiche Hülle, Vermittler, Viereruhr, GNS und physikalische Grenzen. SHA-256: 5726d25cb03443c93cb18d28a8b1589d b0eee06415a84995251875bb00883d60 32mm

Explicit source references:

- [universal_room/Analyse_und_Rekonstruktion.md](../../../../universal_room/Analyse_und_Rekonstruktion.md#L1) · explicit_file_citation

## S06

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:27-31](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L27) · `section:179bf3f5d51f8e55501d` · subsection

TFPT_Universalraum_Rekonstruktion_2026-09-14.md Quotienten 45/30, Register- und Quellenprüfung, Stabilizerhindernis, E8-Rückrekonstruktion. SHA-256: 4515aadc06b13c0216994bb3036bb201 380d00128ab4ce5e6f19f1e7e230fc1e 32mm

Explicit source references:

- [universal_room/TFPT_Universalraum_Rekonstruktion_2026-09-14.md](../../../../universal_room/TFPT_Universalraum_Rekonstruktion_2026-09-14.md#L1) · explicit_file_citation

## S07

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:32-36](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L32) · `section:222eabbc67e38467c91f` · subsection

TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md Inversionshypothese, Matchingausführung, Registerrekurrenz, Clockblockade und endliche Faktorprüfung. SHA-256: b86f846bf2b20a78d2d8997bd303fe5f 4da82497c23f969e8e616e4d9361e95b 32mm

## S08

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:37-41](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L37) · `section:3237eed0ff6d26151927` · subsection

tfpt_anschluss_zellen_seam_2026-09-14.pdf Zellhülle, Tick-Lifts, Kettennumerik, Rotor/CAR-Zustandsgate, Pati-Salam-Läufe und Indexpräzisierungen. SHA-256: 6029544e7bb9ee2e3fa7f94717fa1d18 61b5d0b598e7543cd8abcde1ddf0e8c8 32mm

## S09

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:42-46](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L42) · `section:b4b4645fc67d7749c5ce` · subsection

tfpt_compiler_universalraum_2026-09-13.pdf Grundmanuskript Version 1.0: Architektur, Standardmodell, Zahlen, Prozess, Register und T1 bis T8. SHA-256: 48ea9ae625ce418607eb718478525d80 2c52844183745f27849e17dd63bad43a 32mm

## S10

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:47-51](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L47) · `section:52950f60bb386d3907b0` · subsection

Eingefügter Text: Erklärung des Universalraums Gesprächstext: einfache Universalraum-Erklärung, hypothetische Anwendungen, Zuse und Wolfram. SHA-256: 5c314fd3f27634dfd0cc8e2ed56e5e64 2a457e08df9db9558ee6c962a7f8fd59 32mm

## S11

[experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex:52-55](../../../../experiments/theory-contracts/universalraum-native-closure-20260914/main-v1.5/sources_manifest.tex#L52) · `section:51ceafefd57e409cf961` · subsection

Eingefügter Text: Die fünf gesetzten Fugen Fünf Fugen: Clebsch-Graph, Austausch, Sektortrennung, Orbitargument und Z4-Erweiterung. SHA-256: 79258cd3d27f5a8219ef3b7d597978ea eb6c2c1f0fd18cb636f0a70bbd548ca8

## -1.2cm TFPT — Architecture and the [formula in source] Compiler\\[2mm] The two axioms [formula in source] , the derivation map, and the Coxeter–cyclotomic [formula in source] construction

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1-117](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1) · `section:024229b64f9d20277306` · frontmatter

arrows.meta,positioning,calc,fit,backgrounds,shapes.geometric,shapes.misc,decorations.pathmorphing,decorations.pathreplacing,patterns,angles,quotes,matrix =3.5em

## Architecture and the derivation map

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:118-146](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L118) · `section:cf8ad1fb378e48fe5236` · part

This document develops the architecture layer of TFPT: the two axioms, the derivation map, and the explicit [formula in source] construction. The thesis is that the bridge layer of TFPT is governed by three nested grammars: a carrier grammar (from [formula in source] come charges, families, hypercharge, [formula in source] , [formula in source] ), a seed grammar (one seed [formula in source] generates the Cabibbo ang

## How to read this document

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:147-1673](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L147) · `section:0739148b5a5974d0d662` · section

Notation convention. We write [formula in source] for the root-lattice direct sum (used in the glue/lattice statements: discriminant forms, [formula in source] glue, [formula in source] as an even unimodular lattice), and [formula in source] for the group/representation branching (used for subalgebra embeddings and [formula in source] -rep decompositions). The objects are the same atoms; the symbol marks whether the 

Explicit source references:

- [verification/v774_arf_spinor_compiler.py](../../../../verification/v774_arf_spinor_compiler.py#L1) · explicit_file_citation
- [SEAM.TAU.FLAG.01](../../../../verification/status_ledger.csv#L576) · explicit_claim_identifier · original status at linked ledger row
- [verification/v796_duad_syntheme_bridge.py](../../../../verification/v796_duad_syntheme_bridge.py#L1) · explicit_file_citation
- [verification/v852_arf_vacuum_ovoid.py](../../../../verification/v852_arf_vacuum_ovoid.py#L1) · explicit_file_citation
- [verification/v813_p1_index_kms.py](../../../../verification/v813_p1_index_kms.py#L1) · explicit_file_citation
- [verification/v737_seam48_intertwiner.py](../../../../verification/v737_seam48_intertwiner.py#L1) · explicit_file_citation
- [verification/v112_selfcounting_channel.py](../../../../verification/v112_selfcounting_channel.py#L1) · explicit_file_citation
- [verification/v834_pg32_flag_completion.py](../../../../verification/v834_pg32_flag_completion.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean#L1) · explicit_file_citation
- [verification/v506_seam_clock_rigidity.py](../../../../verification/v506_seam_clock_rigidity.py#L1) · explicit_file_citation
- [verification/v574_stageb_winding.py](../../../../verification/v574_stageb_winding.py#L1) · explicit_file_citation
- [verification/v781_one_object_clock_census.py](../../../../verification/v781_one_object_clock_census.py#L1) · explicit_file_citation
- [verification/v512_seam_tau_flag.py](../../../../verification/v512_seam_tau_flag.py#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v832_anchor_flavor_checksum.py](../../../../verification/v832_anchor_flavor_checksum.py#L1) · explicit_file_citation
- [verification/v783_two_qubit_clifford.py](../../../../verification/v783_two_qubit_clifford.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/Rigidity.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Rigidity.lean#L1) · explicit_file_citation
- [verification/v803_e8_jetcode_affine_nsr.py](../../../../verification/v803_e8_jetcode_affine_nsr.py#L1) · explicit_script_identifier
- [SEAM.CFIN.WICKFUNCTOR.01](../../../../verification/status_ledger.csv#L726) · explicit_claim_identifier · original status at linked ledger row
- [verification/v875_shell_global_lean.py](../../../../verification/v875_shell_global_lean.py#L1) · explicit_file_citation
- [verification/v776_boundary_hamming_uniqueness.py](../../../../verification/v776_boundary_hamming_uniqueness.py#L1) · explicit_file_citation
- [verification/v566_parabolic_anchor_selfcode.py](../../../../verification/v566_parabolic_anchor_selfcode.py#L1) · explicit_script_identifier
- [verification/v525_seam_bit_twist_blind.py](../../../../verification/v525_seam_bit_twist_blind.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_file_citation
- [verification/v800_e8_torsor_fourier.py](../../../../verification/v800_e8_torsor_fourier.py#L1) · explicit_file_citation
- [verification/v782_e8_transition_bus.py](../../../../verification/v782_e8_transition_bus.py#L1) · explicit_file_citation
- [verification/v638_code_semantics.py](../../../../verification/v638_code_semantics.py#L1) · explicit_script_identifier
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_file_citation
- [verification/v898_kms_schur_mixing.py](../../../../verification/v898_kms_schur_mixing.py#L1) · explicit_file_citation
- [SEAM.CODE.TYPEII.01](../../../../verification/status_ledger.csv#L691) · explicit_claim_identifier · original status at linked ledger row
- [verification/v808_petersen_sixthroot.py](../../../../verification/v808_petersen_sixthroot.py#L1) · explicit_file_citation
- [verification/v798_seam_clifford_modular_s.py](../../../../verification/v798_seam_clifford_modular_s.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/GaussianShells.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GaussianShells.lean#L1) · explicit_file_citation
- [verification/v690_quartic_half.py](../../../../verification/v690_quartic_half.py#L1) · explicit_file_citation
- [verification/v491_p2_partition_corollary.py](../../../../verification/v491_p2_partition_corollary.py#L1) · explicit_file_citation
- [verification/v590_involution_existence.py](../../../../verification/v590_involution_existence.py#L1) · explicit_script_identifier
- [verification/v584_ext_source_response.py](../../../../verification/v584_ext_source_response.py#L1) · explicit_file_citation
- [verification/v736_orbit_packet.py](../../../../verification/v736_orbit_packet.py#L1) · explicit_file_citation
- [verification/v817_positive_descent_master.py](../../../../verification/v817_positive_descent_master.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/Hypercharge.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Hypercharge.lean#L1) · explicit_file_citation
- [verification/v807_lorentz_nullselector.py](../../../../verification/v807_lorentz_nullselector.py#L1) · explicit_file_citation
- [verification/v601_equivariant_dual.py](../../../../verification/v601_equivariant_dual.py#L1) · explicit_file_citation
- [verification/v853_bent_css_mangoldt.py](../../../../verification/v853_bent_css_mangoldt.py#L1) · explicit_file_citation
- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_file_citation
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_script_identifier
- [verification/v111_quadratic_transport.py](../../../../verification/v111_quadratic_transport.py#L1) · explicit_file_citation
- [E8.GAUSSCODE.01](../../../../verification/status_ledger.csv#L660) · explicit_claim_identifier · original status at linked ledger row
- [verification/v603_seam_marks.py](../../../../verification/v603_seam_marks.py#L1) · explicit_script_identifier
- [verification/v689_gaussian_code_bridge.py](../../../../verification/v689_gaussian_code_bridge.py#L1) · explicit_file_citation
- [verification/v845_cfin_normal_form.py](../../../../verification/v845_cfin_normal_form.py#L1) · explicit_script_identifier
- [verification/v600_joint_embedding.py](../../../../verification/v600_joint_embedding.py#L1) · explicit_script_identifier
- [verification/v510_seam_bit_freedom.py](../../../../verification/v510_seam_bit_freedom.py#L1) · explicit_file_citation
- [verification/v857_simplex_fourier_winding.py](../../../../verification/v857_simplex_fourier_winding.py#L1) · explicit_file_citation
- [verification/v598_cover_dictionary.py](../../../../verification/v598_cover_dictionary.py#L1) · explicit_file_citation
- [verification/v605_translator.py](../../../../verification/v605_translator.py#L1) · explicit_script_identifier
- [verification/v888_finite_pfaffian_signature.py](../../../../verification/v888_finite_pfaffian_signature.py#L1) · explicit_file_citation
- [verification/v599_real_structure.py](../../../../verification/v599_real_structure.py#L1) · explicit_file_citation
- [SEAM.STRADDLE.CONE.01](../../../../verification/status_ledger.csv#L597) · explicit_claim_identifier · original status at linked ledger row
- [verification/v604_equivariant_order.py](../../../../verification/v604_equivariant_order.py#L1) · explicit_script_identifier
- [verification/v602_duality_forms.py](../../../../verification/v602_duality_forms.py#L1) · explicit_script_identifier
- [verification/v108_pascal_ladder.py](../../../../verification/v108_pascal_ladder.py#L1) · explicit_script_identifier
- [verification/v507_seam_bit_origin.py](../../../../verification/v507_seam_bit_origin.py#L1) · explicit_file_citation
- [verification/v572_rp_bit_form.py](../../../../verification/v572_rp_bit_form.py#L1) · explicit_file_citation
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v784_curve_code_2torsion.py](../../../../verification/v784_curve_code_2torsion.py#L1) · explicit_file_citation
- [verification/v858_g31_clock_alphabet.py](../../../../verification/v858_g31_clock_alphabet.py#L1) · explicit_file_citation
- [verification/v844_message_doily_rank.py](../../../../verification/v844_message_doily_rank.py#L1) · explicit_script_identifier
- [verification/v528_seam_bit_twist_class_definition.py](../../../../verification/v528_seam_bit_twist_class_definition.py#L1) · explicit_script_identifier
- [P1.INDEX.KMS.01](../../../../verification/status_ledger.csv#L700) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.STATE.WIRING.SELECTOR.01](../../../../verification/status_ledger.csv#L736) · explicit_claim_identifier · original status at linked ledger row
- [verification/v568_bit_selector_ladder.py](../../../../verification/v568_bit_selector_ladder.py#L1) · explicit_file_citation
- [verification/v106_review_validation.py](../../../../verification/v106_review_validation.py#L1) · explicit_file_citation
- [verification/v310_carrier_sm_anomaly.py](../../../../verification/v310_carrier_sm_anomaly.py#L1) · explicit_script_identifier
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v775_gaussian_class_d5_purity.py](../../../../verification/v775_gaussian_class_d5_purity.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1) · explicit_file_citation
- [verification/v874_feedback_decoder_lean.py](../../../../verification/v874_feedback_decoder_lean.py#L1) · explicit_file_citation
- [verification/v810_cutcode_moment.py](../../../../verification/v810_cutcode_moment.py#L1) · explicit_file_citation
- [verification/v440_seam_lto_rp_beta.py](../../../../verification/v440_seam_lto_rp_beta.py#L1) · explicit_script_identifier
- [verification/v752_projective_hamming_incidence.py](../../../../verification/v752_projective_hamming_incidence.py#L1) · explicit_file_citation
- [verification/v109_sheet_pairing.py](../../../../verification/v109_sheet_pairing.py#L1) · explicit_script_identifier
- [SEAM.CFIN.KMSMIX.01](../../../../verification/status_ledger.csv#L727) · explicit_claim_identifier · original status at linked ledger row
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1) · explicit_file_citation
- [verification/v880_finite_anchor_theorems.py](../../../../verification/v880_finite_anchor_theorems.py#L1) · explicit_file_citation
- [verification/v799_seam_code_typeii.py](../../../../verification/v799_seam_code_typeii.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/LatticeRigidityGeneral.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/LatticeRigidityGeneral.lean#L1) · explicit_file_citation
- [verification/v499_p2_weights_deligne_bg.py](../../../../verification/v499_p2_weights_deligne_bg.py#L1) · explicit_script_identifier
- [verification/v23_anchor_generator.py](../../../../verification/v23_anchor_generator.py#L1) · explicit_file_citation
- [verification/v911_wiring_freedom.py](../../../../verification/v911_wiring_freedom.py#L1) · explicit_file_citation
- [E8.QUARTICHALF.01](../../../../verification/status_ledger.csv#L661) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BIT.TWISTCLASS.01](../../../../verification/status_ledger.csv#L595) · explicit_claim_identifier · original status at linked ledger row
- [verification/v903_seam_rp_exclusion.py](../../../../verification/v903_seam_rp_exclusion.py#L1) · explicit_file_citation
- [verification/v14_carrier_uniqueness.py](../../../../verification/v14_carrier_uniqueness.py#L1) · explicit_script_identifier
- [verification/v833_gaussian_ramification_ladder.py](../../../../verification/v833_gaussian_ramification_ladder.py#L1) · explicit_script_identifier
- [verification/v908_seam_equilibrium_wiring.py](../../../../verification/v908_seam_equilibrium_wiring.py#L1) · explicit_file_citation
- [verification/v809_curve_code_doily.py](../../../../verification/v809_curve_code_doily.py#L1) · explicit_file_citation
- [GATE.QGEO.01](../../../../verification/status_ledger.csv#L52) · explicit_claim_identifier · original status at linked ledger row
- [verification/v170_diamond_slice_compression.py](../../../../verification/v170_diamond_slice_compression.py#L1) · explicit_script_identifier
- [verification/v486_transfer_full_rule.py](../../../../verification/v486_transfer_full_rule.py#L1) · explicit_script_identifier
- [verification/v124_resummed_clock.py](../../../../verification/v124_resummed_clock.py#L1) · explicit_script_identifier
- [verification/v896_wick_block_functor.py](../../../../verification/v896_wick_block_functor.py#L1) · explicit_file_citation
- [verification/v110_calderon_sheet.py](../../../../verification/v110_calderon_sheet.py#L1) · explicit_file_citation
- [verification/v814_k5_sixstep_transport.py](../../../../verification/v814_k5_sixstep_transport.py#L1) · explicit_file_citation
- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [verification/v156_seam_net_construction.py](../../../../verification/v156_seam_net_construction.py#L1) · explicit_script_identifier
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [verification/v597_mu4_cover_model.py](../../../../verification/v597_mu4_cover_model.py#L1) · explicit_script_identifier
- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier
- [verification/v567_carrier_free_q_reconstruction.py](../../../../verification/v567_carrier_free_q_reconstruction.py#L1) · explicit_file_citation
- [verification/v426_seam_lto_rp_kms.py](../../../../verification/v426_seam_lto_rp_kms.py#L1) · explicit_script_identifier
- [verification/v521_seam_bit_rp_blind.py](../../../../verification/v521_seam_bit_rp_blind.py#L1) · explicit_script_identifier
- [verification/v218_diamond_axis_geometry.py](../../../../verification/v218_diamond_axis_geometry.py#L1) · explicit_script_identifier
- [verification/v849_cfin_unique_cofinal_lean.py](../../../../verification/v849_cfin_unique_cofinal_lean.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ==== v525 round: SEAM.BIT.TWISTBLIND.01 -- "the twist-state kill": the NINTH side-blind test on the v512 scoreboard (8 -> 9); the free-plus-twist class is exhausted. Three exact mirrors: (i) the integer incidence frame + the sigma o r = +-sigma congruence mechanism (swap axes: sigma o r = sigma => the twisted Gram is the diagonal unitary congruence D M D = spectrally invisible; fixing axes at pi/2: sigma o r = -sigma = the eta flip); (ii) the pi/2-existence solveset of the mark-fixing axes + the exact counterwitness census ((3+4i)/5 unimodular but NEVER a root of unity up to order 64 -- no lattice mark-compatible reflection at any dyadic refinement); (iii) the delta <-> pi - delta mirror equivariance (the lattice reflection maps the m-mark set EXACTLY to the (8-m)-mark set -- the exact mechanism behind the Casimir mirror symmetry ln|omega(D)|(m) = ln|omega(D)|(8-m) and behind pi/2 as the symmetric point of every invariant readout). The Pfaffian insertion spectra, the Bogoliubov 2-of-16 pattern census, the defect energy and the 40-digit inertia certificates are numerical (mpmath), Python-only, flagged here. Mirrors v525. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8058)
- [(* ==== v512 round: SEAM.TAU.FLAG.01 -- "the flag-transitivity equivalence web": the tau = i attack on the free RP seam circle. Test family M(delta) = {+-1, +-e^(i delta)}; bare mark-transitivity is delta-blind (pair-exchanging V4), FLAG transitivity <=> delta = pi/2 <=> tau = i. Six exact mirrors: (i) the V4/D4 census over five exact members incl. flag/arc orbit counts, (ii) the solveset equivalences + family identities, (iii) the odd-split closed form + arc Laplacian + K3 indicator, (iv) the twist mode identity + AB delta-blindness + j-rationality control, (v) the H4 centraliser rigidity (Schur), and (vi) the negative controls (hexagonal/silver/Z16 census/n = 3). Mirrors v512. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5675)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ==== v507 round: SEAM.BIT.ORIGIN.01 -- the tautology attack on the v506 alignment bit, executed and refuted (Part A torus origin + Part B fermion dichotomy). Exact content mirrored: (i) the HALF-PERIOD DESCENT -- the fixed points of w -> -w on C/(Z + tau Z) are the 4 half-periods (2w in Lambda <=> coefficients in {0, 1/2}; the 1/3-control fails), a translation t_c descends iff 2c in Lambda (exactly the 3 nonzero half-periods), and the descended map sigma_i(x) = e_i + (e_i-e_j)(e_i-e_k)/(x-e_i) satisfies the exact curve-lift identity prod(sigma_i - e_l) = psi_i^2 prod(x - e_l) with RATIONAL psi_i, closing to Klein V4 symbolically; (ii) the CORE SOLVE -- the pair cross-ratio condition CR = -1 solves to lambda = -1 (sigma_1), 2 (sigma_2), 1/2 (sigma_3) exactly, union = the harmonic orbit with j = 1728, against j(3) = 21952/9 and j(hex) = 0; (iii) the STABILISER COUNTS -- the complete 24-triple enumeration gives (|Stab|, #involutions, #free) = (4,3,3) generic / (8,5,3) harmonic / (12,3,3) hexagonal, and in ALL three types the free involutions are EXACTLY the three sigma_c (the deck CLASS is forced); (iv) the CM FIXED POINT -- mult-by-i mod 2 fixes exactly the half-period (1,1) = c* = (1+tau)/2 while mult-by-rho 3-cycles all three, the lemniscatic clock ghat: x -> (x-1)/(x+1) needs the curve-lift factor psi = 2i/(x+1)^2 (the CM unit; t^2+1 irreducible over Q) and squares to the central -1/x; (v) the Cl(16) DICHOTOMY -- on explicit 256x256 Jordan-Wigner gammas the central implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the EDGE implementer Utilde_e = P_3 (g1+g5)(g2+g4)(g6-g16)(g7-g15)(g8-g14) (g9-g13)(g10-g12) implements the NS edge reflection and squares to the SCALAR +2^7 (split), and in the 32-element NS dihedral lift group the central deck has EXACTLY 2 square roots (the +-quarter shifts) vs 0 for the edge deck; (vi) the SILVER BIJECTION CENSUS -- all 8 mark bijections {+-1, +-(3+2 sqrt 2)} -> {0, 1, -1, inf} carry the deck z -> -z to the EDGE sigma_2/sigma_3 (never the central sigma_1), while all 8 mu4 bijections carry it to the CENTRAL sigma_1. The v493 circularity-audit direction and the 28/21 arrangement census stay Python-side (v507). Mirrors v507. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4545)
- [experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v170) E8 slice compression: seven slices from two alphabets ---- *) Module[{p, p0, p1, p2, p3, Delta, e1, e2, dimSp, dQ, dK, dR, dC, dL, dF, slices}, p = Table[2 + 2^n, {n, 0, 3}]; {p0, p1, p2, p3} = p; Delta = p0 + p3; e1 = 4; e2 = 5; dimSp = 16; {dQ, dK, dR, dC, dL, dF} = {3, 4, 8, 14, 20, 32}; slices = { p0 p1 p3 + p1 dF, (p1 p3 + e2) + (p0 p1 + p0) + p2 p3 + 2 e1 dimSp, p2 Delta + dR + 81 + 81, (p0 p1 p3 + Delta) + p0 + dR dC, (p1^2 + p2^2) + dC + Delta dC, 2 p1 p2 + 4 e2 p3, dK dL + 2 p2 dC}; checkExact["v170 E8 slice compression: P=(3,4,6,10), D=(3,4,8,14,20,32) sum 81=N_fam^4; K4 edges {12,18,30,24,40,60}; all seven E8 slices = 248; 78 = p2 Delta = dim E6", p === {3, 4, 6, 10} && Total[{dQ, dK, dR, dC, dL, dF}] == 81 && {p0 p1, p0 p2, p0 p3, p1 p2, p1 p3, p2 p3} === {12, 18, 30, 24, 40, 60} && AllTrue[slices, # == 248 &] && p2 Delta == 78]; ]; (* ---- (v171) atomic OS moment + Sugawara gap safety ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1465)
- [(* ---- (v111) quadratic transport ---- *) Module[{jwOps, evensOf, buildQuads, runWorld}, jwOps[g_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, g - i]], {i, g}]]; evensOf[g_] := Select[Range[2^g], EvenQ[DigitCount[# - 1, 2, 1]] &]; buildQuads[g_] := Module[{a = jwOps[g], ad}, ad = Transpose /@ a; Join[ Flatten[Table[{ad[[i]] . ad[[j]], a[[i]] . a[[j]]}, {i, g}, {j, i + 1, g}], 2], Flatten[Table[ad[[i]] . a[[j]], {i, g}, {j, g}], 1]]]; runWorld[g_] := Module[{a = jwOps[g], ad, ev = evensOf[g], od, quads, vac, d1, d2, orbit, qr, words}, ad = Transpose /@ a; od = Complement[Range[2^g], ev]; quads = buildQuads[g]; vac = UnitVector[2^g, 1]; d1 = (# . vac) & /@ quads; d2 = Flatten[Outer[Dot, quads, d1, 1], 1]; orbit = (#[[ev]]) & /@ Join[{vac}, d1, d2]; qr = (#[[ev, ev]]) & /@ quads; words = Join[{IdentityMatrix[Length[ev]]}, qr, Flatten[Outer[Dot, qr, qr, 1], 1]]; {Length[quads], And @@ ((Max[Abs[#[[ev, ev]]]] == 0 && Max[Abs[#[[od, od]]]] == 0) & /@ Join[a, ad]), And @@ ((Max[Abs[#[[ev, od]]]] == 0 && Max[Abs[#[[od, ev]]]] == 0) & /@ quads), MatrixRank[orbit], MatrixRank[Flatten /@ words], Length[ev]}]; Module[{r5 = runWorld[5], r3 = runWorld[3]}, checkExact["v111 model: 45 quadratics = dim so(10); 10 linears sheet-ODD, 45 quadratics sheet-EVEN (exact block-zero)", r5[[1]] == 45 && r5[[2]] && r5[[3]]]; checkExact["v111 GENERATION: quadratic words of length <= 2 span all 16 code states from the vacuum", r5[[4]] == 16]; checkExact["v111 COMPLETENESS: products of length <= 2 of the 45 quadratics span End(S+) = 256 (transport degree exactly 2)", r5[[5]] == 256]; checkExact["v111 ladder genericity: g=3 world identical (15 quadratics -> End(S+) = 16) - degree selected, not rank", r3[[1]] == 15 && r3[[5]] == 16]; checkExact["v111 channel reading: certified tower 256 = 1 + 45 + 210 = norm + transport generators + pair sector", 1 + 45 + 210 == 256]; ]; ]; (* ---- (v112) self-counting channel ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L542)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean#L1)
- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)
- [(* ==== v491 round: P2.PARTITION.01 -- g_car = 5 as the partition corollary of the four marks (the sharpening of v53). Exact content: 4 into exactly 3 positive integer parts is uniquely {1,1,2} => e = (4,5,2) => g_car = e2 = 5, |Z2| = e3 = 2, N_fam = e2 - e3 = 3 as corollaries; every assumption load-bearing (positivity / sum / part count / integrality negative controls); v53 needs all three targets, the partition only e1 = 4; sum rule 4(N-1)/2 = 4 iff N = 3; mirrors v491. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3116)
- [experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean#L1)
- [(* ---- (v107) quantum-clock target ---- *) checkExact["v107 per-l clock: l=0 (la-1)(la+2), l=1 la(la+1); l>=2 complex Re=-1/2", (Factor[la^2 + la + (0 - 2)] == (la - 1) (la + 2)) && (Factor[la^2 + la + (2 - 2)] == la (la + 1)) && (Re[la /. Solve[la^2 + la + 4 == 0, la]] == {-1/2, -1/2})]; checkExact["v107 cusp-ladder cross-link: decay set {0,-1,-2} = -Spec(Q diag(0,1,1)) = -N_fam x cusp", Module[{Vw = Q.DiagonalMatrix[{0, 1, 1}]}, Sort[Eigenvalues[Vw]] == {0, 1, 2}]]; checkExact["v107 exact target: (1/3)^6 = ((2/3)^6)^{log_{3/2}3}; ratio = 1 + log_{3/2}2", (FullSimplify[-6 Log[3] - (Log[3]/Log[3/2]) (6 Log[2] - 6 Log[3])] === 0) && (FullSimplify[Log[3]/Log[3/2] - (1 + Log[2]/Log[3/2])] === 0)]; check["v107 bend log_{9/4}(3) = 1.354756; seam coupling 1/(3Pi) = 0.106103", Log[3]/Log[9/4], 1.3547556457`10, 10^-9]; (* ---- (v108) Pascal ladder ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L471)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [(* ---- (v218) DIAMOND.AXIS/PLUCKER/SPECTRAL.01: the diamond axis geometry ---- *) Module[{R, Q, a, one, Cc, U, V, K, L, F, anc, plL, ram, x, y, dU, dV, bU, bV, sd, bsd, sq, ker}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; one = {1, 1, 1}; a = {1, 1, 2}; Cc = R + Q.DiagonalMatrix[{1, 0, 0}]; (* center C = M(1,0) (v95) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1751)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ParityWeightLaws.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ParityWeightLaws.lean#L1)
- [(* ---- (v109) sheet pairing ---- *) Module[{splus, sminus, vecw, lamW, addW, crossT, formsEven, diagT, formsOdd, zmult}, splus = Select[Tuples[{1/2, -1/2}, 5], EvenQ[Count[#, -1/2]] &]; sminus = Select[Tuples[{1/2, -1/2}, 5], OddQ[Count[#, -1/2]] &]; vecw = Flatten[Table[s UnitVector[5, i], {i, 5}, {s, {1, -1}}], 1]; lamW[k_] := If[k == 0, {ConstantArray[0, 5]}, Total /@ Subsets[vecw, {k}]]; checkExact["v109 no scalar within a sheet: zero-weight mult of S+xS+ and S-xS- is 0", (Count[Flatten[Outer[Plus, splus, splus, 1], 1], ConstantArray[0, 5]] == 0) && (Count[Flatten[Outer[Plus, sminus, sminus, 1], 1], ConstantArray[0, 5]] == 0)]; crossT = Sort[Flatten[Outer[Plus, splus, sminus, 1], 1]]; checkExact["v109 cross-sheet zero-weight mult = 16 = 1+5+10 (Pascal triple)", Count[crossT, ConstantArray[0, 5]] == 16]; formsEven = Sort[Join[lamW[0], lamW[2], lamW[4]]]; checkExact["v109 EXACT multiset: S+xS- = Lambda^0+Lambda^2+Lambda^4 (256 = 1+45+210)", crossT === formsEven && Length[crossT] == 256]; diagT = Sort[Join[Flatten[Outer[Plus, splus, splus, 1], 1], Flatten[Outer[Plus, sminus, sminus, 1], 1]]]; formsOdd = Sort[Join[lamW[1], lamW[1], lamW[3], lamW[3], lamW[5]]]; checkExact["v109 sheet-diagonal = odd forms: (S+xS+)u(S-xS-) = 2L1+2L3+L5 (512)", diagT === formsOdd && Length[diagT] == 512]; zmult[k_] := Count[lamW[k], ConstantArray[0, 5]]; checkExact["v109 zero-mode grading (L0,L2,L4) -> (1,5,10) = the carrier code; tower tops at 2K = 4", ({zmult[0], zmult[2], zmult[4]} == {1, 5, 10}) && (4 == 2*2)]; ]; (* ---- (v110) Calderon-sheet selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L499)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ==== v528 round: SEAM.BIT.TWISTCLASS.01 -- bit = twist-class choice. Exact mirrors: (i) cardinality lemma; (ii) 224-axis flip census; (iii) O-values. Pfaffian spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8213)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [(* ==== v521 round: SEAM.BIT.RPBLIND.01 -- "free OS positivity does not see delta": the anti-linear census solvesets on M(delta), the counterwitness census, the V4 -> D4 closure (face #13), the cut/mark incidence, the continuum axis elimination + Cauchy-Stieltjes factorisation, the clock-tower clause and the hex/silver precondition controls. The 40-digit lattice Gram inertia spectra (N = 16 / N = 32) are Python-only by the suite convention. Mirrors v521. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7479)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean#L1)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v506 round: SEAM.CLOCK.RIGIDITY.01 -- clock rigidity, Route B of the v503 classification (Part A Moebius + Part B Fock). Exact content mirrored: (i) the COMPLETE SQUARE-ROOT SOLVE -- g^2 = deck in PGL2(C) has exactly two solutions z -> +-iz (tr != 0 forces diagonal with (a/d)^2 = -1; tr = 0 forces det = 0), both automatically of projective order 4; (ii) the D4 CENTER + ORDER-4 COUNT + the COUNTEREXAMPLE -- the mu4 stabiliser D4 = {i^k z, i^k/z} has exactly 2 order-4 elements (the clocks), both squaring to the deck, center = {id, deck}; the silver harmonic set {+-1, +-(3+2 sqrt 2)} has j = 1728 and full D4 but its 4-cycle squares to the CROSSING involution v/z, not the deck (deck non-central: 0 roots -- harmonicity alone insufficient); (iii) the Cl(16) IDENTITY -- on explicit 256x256 Jordan-Wigner gamma matrices, Utilde = prod_j (1 - g_j g_{j+8}) satisfies Utilde^2 = 256 g_1...g_16 EXACTLY (U^2 = (-1)^F, the forced nonsplit Z4), the R implementer squares to +256 (split control), and the volume element anticommutes with every gamma; (iv) the N-ARITHMETIC -- S4 element orders {1,2,3,4} (faithfulness kills n >= 5: max cyclic image order < n for n = 5..8), free orbits force n | 4, the cusp side kills n = 6 (deg(lam^5-1) = 5 != 3 = deg(lam^3-1)), transfer spectrum {1, 64/729, 1/729} with gap (2/3)^6, and the generic 4-set stabiliser V4 = {+-z, +-2/z} has exponent 2 (not even the deck has a root). The full 24-triple stabiliser enumeration and the A4/hexagonal profile stay Python-side (v506 Part A). Mirrors v506. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4394)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ==== v499 round: P2.TYPING.01 -- the P2 weight-typing postulate hardened: the anchor a = (1,1,2) as the Birkhoff-Grothendieck splitting exponents of the Deligne canonical extension E of the flavor connection (types the v491 check-9 residual). Exact content mirrored: (i) partition enumeration under the full typing (BG dictionary h^0 = 0 <=> a_i >= 1, exhaustive window) + the naive- typing negative control (h^1(E') = 3 forces deg -6, three splittings, e2 never 5) + the h^1 discrepancy (h^1(anchor bundle) = 1 != 3); (ii) the Deligne residue-trace degree (cusp exponents {0,1/3,2/3} = the unique lift of spec(lam^3 - 1) to [0,1), trace 1 per mark, deg E = -4, par-deg 0, witness A0* charpoly); (iii) the Schur-Horn permutohedron integer points {(2,2,0),(2,1,1)} with h^0 = 0 killing {2,2,0}; (iv) the Biswas Z3-cover degree arithmetic (genus 2, eigensheaves O(-2)^2, chi cross-check, regular-rep weights, the decomposable model {0,2,2} with h^0 = 1 = the unstable companion; deck double genus 1, j = 1728); (v) the n-mark formula e2 = (n-2)(n+1)/2 = 5 only at n = 4. The sympy symbolic parts (H^1 residue basis, monodromy group closure |<U,M0>| = 24, the 324-case stability skeleton) stay Python-side (v499). Mirrors v499. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3620)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean#L1)
- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [(* ==== v510 round: SEAM.BIT.FREEDOM.01 -- the freedom attack on the v506/v507 alignment bit: the POSITION half of the bit is topology. Exact content mirrored: (i) the DIHEDRAL CENSUS -- on the refined 2N-point seam circle D_16 has 17 involutions with EXACTLY ONE free (the antipodal shift by 8) and all 16 reflections have exactly 2 circle fixed points (8 site-axis + 8 edge-axis; robustness N = 8, 12; odd control N = 9: zero free), plus the quotient topology chi(C/antipode) = 0 (circle) vs chi(C/reflection) = 1 (interval, 2 boundary corners); (ii) the AUT COMPLETENESS -- Aut(C_8) = D_8 by brute force over all 8! = 40320 permutations and Aut(C_16) = D_16 by degree-2 propagation (all 32 candidates), so the census covers ALL circle symmetries; (iii) the Cl(16) DICHOTOMY CENSUS -- on explicit 256x256 Jordan-Wigner gammas the free deck's NS implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the implementers of ALL 16 reflections exist (one of the two spin lifts +-R) and square to SCALARS {2^7 (site-axis), 2^8 (edge-axis)} (split): NONSPLIT <=> FREE over the complete census; root dichotomy 2 (the +-quarter shifts) vs 0 total over all 16 reflections; (iv) the REAL-STRUCTURE TABLE -- the deck-commuting antiholomorphic involutions solve symbolically to exactly two families (M diagonal: mu conj z, fix line through the poles; M antidiagonal: mu/conj z, fix circle |z| = sqrt mu), and the unique mark-fixing real structure per configuration is equatorial/FREE for mu4 and generic-unit, real-axis/NOT-free for silver and generic-real, and NONEXISTENT for the hexagonal frame; (v) HARMONIC + FREE => mu4 -- the deck-pair cross-ratio (1-b)^2/(1+b)^2 = -1 solves exactly to b = +-i, with the lambda table (2, 1/2, 3/4, 5/4) real and the hexagonal lambda complex; (vi) the HONEST COUNTERWITNESSES -- the discrete witness {0,1,8,9} (shift-invariant, crossing, but not quarter-shift-invariant) and the continuous witness {+-1, +-(3+4i)/5} (pair cross-ratio -1/4, j = 148176/25 != 1728, clock does not preserve): the Fock dichotomy measures the CLASS, not the modulus. The Moebius/Klein covering models and the pillowcase branch control stay Python-side (v510). Mirrors v510. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5155)

## Headline: the Pascal compiler on five carrier slots

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1674-1731](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1674) · `section:d427346791d863fc02e1` · section

The strongest new statement is that three of the theory's separate structures are the same truncated row of Pascal's triangle on the five-slot carrier.

Explicit source references:

- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## [formula in source] as the Pascal closure

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1732-1780](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1732) · `section:baf89b99d7afc0a0ef50` · subsection

A family is exactly the complete Pascal truncation to degree two: the unique positive-integer solution of [formula in source] . Proof of uniqueness. Direct evaluation gives [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] ; so [formula in source] is the only root in [formula in source] . For [formula in source] the forward difference is 

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_file_citation
- [verification/v45_family_exterior.py](../../../../verification/v45_family_exterior.py#L1) · explicit_file_citation
- [verification/v46_grand_mass_volume.py](../../../../verification/v46_grand_mass_volume.py#L1) · explicit_file_citation
- [verification/v14_carrier_uniqueness.py](../../../../verification/v14_carrier_uniqueness.py#L1) · explicit_file_citation
- [verification/v44_carrier_exterior.py](../../../../verification/v44_carrier_exterior.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ---- (v44) exterior leg = carrier exterior-algebra grading ---- *) checkExact["16 = Lambda^even(5) = C(5,0)+C(5,2)+C(5,4) = 1+10+5", {Binomial[5, 0], Binomial[5, 2], Binomial[5, 4]} == {1, 10, 5}]; (* u^c in 10=Lambda^2(5) deg 2 ; d^c in 5bar=Lambda^4(5) deg 4 *)](../../../../verification/wolfram/tfpt_readouts.wl#L161)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *) checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+", Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16]; checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car", Sort[Abs[plLeft[K]]] == {1, 4, 6} && Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar]; checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car", 4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15]; (* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L168)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)

## One master moment generates [formula in source] , [formula in source] , [formula in source] , [formula in source]

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1781-1796](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1781) · `section:93683d7c3fd300bd9861` · subsection

With [formula in source] , the quadratic hypercharge trace on one family is [formula in source] , and it generates the whole integer chain: The flavor budget, the [formula in source] budget, the [formula in source] count and the second seam defect all hang on the second hypercharge moment [formula in source] . \ Round-22 sharpening: the moment itself is one symbolic identity, [formula in source] — the Coxeter number 

Explicit source references:

- [verification/v810_cutcode_moment.py](../../../../verification/v810_cutcode_moment.py#L1) · explicit_file_citation

## Compact [formula in source] compression and the role of [formula in source]

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1797-1808](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1797) · `section:33b4fab842cf1417435c` · subsection

with [formula in source] and [formula in source] . . The right-handed neutrino [formula in source] is the Pascal singleton [formula in source] that closes [formula in source] ; removing it breaks the truncation and shifts [formula in source] by [formula in source] .

## The [formula in source] compiler: [formula in source] as a closure, not an input

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1809-1910](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1809) · `section:d3f2b7d7ec6acb95794a` · section

This section upgrades the [formula in source] atlas (Section lattice construction. The whole content is consolidated and verified in the standalone companion note ``The Even Carrier Code and the [formula in source] Coxeter Compiler.'' The thesis: the carrier code is the [formula in source] half-spinor, the family geometry is an [formula in source] , and [formula in source] is the standard unimodular glue closure of [

Explicit source references:

- [verification/v277_seam_calderon_e8_match.py](../../../../verification/v277_seam_calderon_e8_match.py#L1) · explicit_script_identifier
- [verification/v489_seam_modular_commutator.py](../../../../verification/v489_seam_modular_commutator.py#L1) · explicit_file_citation
- [SEAM.EQUIV.TWISTOR.01](../../../../verification/status_ledger.csv#L584) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [GNET.RAMIFIED.01](../../../../verification/status_ledger.csv#L667) · explicit_claim_identifier · original status at linked ledger row
- [verification/v260_k3_kummer_unification.py](../../../../verification/v260_k3_kummer_unification.py#L1) · explicit_script_identifier
- [verification/v726_phys_car_pp_index.py](../../../../verification/v726_phys_car_pp_index.py#L1) · explicit_file_citation
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier
- [GATE.METRIC.08](../../../../verification/status_ledger.csv#L210) · explicit_claim_identifier · original status at linked ledger row
- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [verification/v722_phys_ramified_ns_r.py](../../../../verification/v722_phys_ramified_ns_r.py#L1) · explicit_file_citation
- [verification/v234_seam_holomorphy_selection.py](../../../../verification/v234_seam_holomorphy_selection.py#L1) · explicit_script_identifier
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v802_gnet_martingale.py](../../../../verification/v802_gnet_martingale.py#L1) · explicit_file_citation
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_script_identifier
- [verification/v469_seam_crossedproduct_route.py](../../../../verification/v469_seam_crossedproduct_route.py#L1) · explicit_file_citation
- [verification/v779_gnet_gns_arf.py](../../../../verification/v779_gnet_gns_arf.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* v469 (i): the LR locality integers of both extension routes *) hs = 16/16; (* so(N)_1 spinor weight N/16, N = 16 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2930)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* v463 (ii): the (E8)_1 tower = E4/eta^8 coefficients {1,248,4124,34752,213126} *) inv8 = Series[Product[(1 - q^n)^-8, {n, 1, 6}], {q, 0, 5}]; chiSer = Series[(1 + 240 Sum[DivisorSigma[3, n] q^n, {n, 1, 6}]) inv8, {q, 0, 5}]; tower = CoefficientList[Normal[chiSer], q][[1 ;; 5]]; checkExact["v463 SEAM.EQUIV.UNIQ.01 (ii): the holomorphic c=8 partition function is the unique j^{1/3}=E4/eta^8, whose q-coefficients are the (E8)_1 tower {1,248,4124,34752,213126} -- the q^1=248 is the forced weight-1 dimension (Dong-Mason/Schellekens: the holomorphic c=8 VOA is unique = V_{E8})", tower == {1, 248, 4124, 34752, 213126}]; ]; (* ==== v469 round: the net-level crossed-product certification -- the LR locality integers (h_s(SO(16)_1) = 16/16 = 1 in Z; the mu4 glue h(J^k) = {1,1,1} all integer), the KLM mu-index arithmetic (4/2^2 = 1 and 16/4^2 = 1, both holomorphic) and the Kitaev 16-fold-way pin (nu = 16 x |C| = 16 = 0 mod 16, c_- = nu/2 = 8 = g_car+N_fam); mirrors v469 (the FHS Chern itself is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2916)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## Carrier [formula in source] (proved)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1911-1927](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1911) · `section:aed67380a36c30ec03d3` · subsection

The [formula in source] even-occupation states [formula in source] are exactly the weights of the [formula in source] half-spinor [formula in source] (even number of minus signs). The flip-weight- [formula in source] relation is the Clebsch graph [formula in source] and the flip-weight- [formula in source] relation is its complement [formula in source] ; the affine automorphism group of the scheme (translations [form

Explicit source references:

- [verification/v810_cutcode_moment.py](../../../../verification/v810_cutcode_moment.py#L1) · explicit_file_citation

## Family [formula in source] from [formula in source] (proved, with the metric settled)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1928-1961](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1928) · `section:d748a08ff21c7b67a82f` · subsection

The carrier geometry fixes [formula in source] , [formula in source] , rigid [formula in source] generated by [formula in source] . The twelve puncture-difference cycles [formula in source] carry the residue pairing [formula in source] and form the [formula in source] root system: The corner rotation [formula in source] acts on [formula in source] as the [formula in source] Coxeter element (order [formula in source] 

Explicit source references:

- [verification/v223_coxeter_totative_clock.py](../../../../verification/v223_coxeter_totative_clock.py#L1) · explicit_file_citation
- [verification/v219_icosahedral_mckay.py](../../../../verification/v219_icosahedral_mckay.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)
- [(* v223 Coxeter totative clock: (Z/30)^x = E8 exponents, order-4 element 7 *) checkExact["v223 COX.CLOCK.01: (Z/30)^x = {1,7,11,13,17,19,23,29} = E8 exponents, " <> "phi(30)=8=rank E8, 30=2*3*5; mult-by-7 has order 4 (7^2=19, 7^4=1 mod 30): a " <> "mu4 clock <7>={1,7,13,19}; the conjugate pairs split into 4 invariant planes", Select[Range[29], CoprimeQ[#, 30] &] == {1, 7, 11, 13, 17, 19, 23, 29} && EulerPhi[30] == 8 && PowerMod[7, 2, 30] == 19 && PowerMod[7, 4, 30] == 1 && Sort[Mod[7^Range[0, 3], 30]] == {1, 7, 13, 19} && Length[Union[Sort /@ ({#, 30 - #} & /@ {1, 7, 11, 13, 17, 19, 23, 29})]] == 4]; (* v227 degree/exponent channel split: 248 = 120 + 128 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1804)

## The [formula in source] glue and the [formula in source] discriminant theorem (proved)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:1962-3405](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L1962) · `section:39eddc22c7cf018bcce9` · subsection

The two factors have equal discriminant groups and [formula in source] is unimodular, so the glue index is exactly [formula in source] : The discriminant-form norms sum to the [formula in source] root norm, and — strikingly — they are pre-existing TFPT constants: This is literally the [formula in source] spinor-root split [formula in source] , [formula in source] .

Explicit source references:

- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)

## Glue-norm arithmetic, and three readings of [formula in source] , [formula in source] , [formula in source]

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3406-3560](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3406) · `section:5ae06930f472e00a9545` · subsection

The two glue norms generate the carrier integers through sum, difference and product. With [formula in source] : so the glue already contains the full carrier exhaustion [formula in source] , the [formula in source] rank, and the non-trivial transition count [formula in source] ; and [formula in source] is the inverse displacement of the two norms from the unit norm.

Explicit source references:

- [verification/v137_qplus_cohomology.py](../../../../verification/v137_qplus_cohomology.py#L1) · explicit_file_citation
- [verification/v74_compiler_micro_lemmas.py](../../../../verification/v74_compiler_micro_lemmas.py#L1) · explicit_file_citation
- [verification/v91_spine_tetrahedron.py](../../../../verification/v91_spine_tetrahedron.py#L1) · explicit_file_citation
- [verification/v115_anchor_residue.py](../../../../verification/v115_anchor_residue.py#L1) · explicit_file_citation
- [verification/v142_frame_integrality.py](../../../../verification/v142_frame_integrality.py#L1) · explicit_file_citation
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_file_citation
- [verification/v146_moebius_d4.py](../../../../verification/v146_moebius_d4.py#L1) · explicit_file_citation
- [verification/v222_cm_norm_duality.py](../../../../verification/v222_cm_norm_duality.py#L1) · explicit_file_citation
- [verification/v141_deck_selection.py](../../../../verification/v141_deck_selection.py#L1) · explicit_file_citation
- [verification/v116_resonance_uniqueness.py](../../../../verification/v116_resonance_uniqueness.py#L1) · explicit_file_citation
- [verification/v145_pairing_atoms.py](../../../../verification/v145_pairing_atoms.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v137) Q+ cohomology grading ---- *) Module[{omchar, resok, qp, a0c}, omchar = Table[Simplify[((I z)^(k - 1)/((I z)^4 - 1)) I/(z^(k - 1)/(z^4 - 1))], {k, 3}]; resok = And @@ Flatten[Table[ Simplify[Residue[z^(k - 1)/(z^4 - 1), {z, zeta}] - zeta^k/4] === 0, {k, 3}, {zeta, {1, -1, I, -I}}]]; checkExact["v137 characters + residues: omega_k has mu_4 character i^k (k=1,2,3); residue vector = zeta^k/4 exactly", omchar === {I, -1, -I} && resok]; qp = DiagonalMatrix[3 {0, 1/3, 2/3} + 1]; a0c = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; checkExact["v137 grading: Spec(Q+) = {1,2,3}; cusp weights {0,1/3,2/3} = spec(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1086)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)
- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)
- [(* ---- (v140) canonical map ---- *) Module[{charf, cu, cmu, cw}, charf[m_] := Mod[Round[Arg[#]/(Pi/2)], 4] & /@ Diagonal[m]; cu = charf[DiagonalMatrix[{1, I, -I}]]; cmu = charf[-DiagonalMatrix[{1, I, -I}]]; cw = charf[DiagonalMatrix[{I, I^2, I^3}]]; checkExact["v140 canonical map: deck U chars (0,1,3) miss 2; -U = (2,3,1) and i^Q+ = (1,2,3) both have SET {1,2,3} = H^1; i^Q+ assignment = Q+, -U assignment = Q+ o rho (one Z3 rotation apart)", cu == {0, 1, 3} && cmu == {2, 3, 1} && cw == {1, 2, 3} && Sort[cmu] == {1, 2, 3} == Sort[cw] && cmu == (cw[[#]] & /@ {2, 3, 1})]; ]; (* ---- (v141) deck selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1122)
- [(* v415 (4): the intrinsic order-4 mu4 deck D = -I + J - J^2 *) Pi2 = I3 + J . J; D = J - Pi2; checkExact["v415 DIAMOND.GAUSS.01 (iv): the intrinsic deck D=-I+J-J^2={{-1,1,0},{-2,1,0},{-4,3,-1}} is order 4 (D^4=I), Spec(D)={i,-1,-i} (the seam-deck spectrum, v146); chi2 line = ker[U,V] = NullSpace = {(0,0,1)} = a-1", D == {{-1, 1, 0}, {-2, 1, 0}, {-4, 3, -1}} && MatrixPower[D, 4] == I3 && Sort[Eigenvalues[D]] == Sort[{I, -I, -1}] && NullSpace[J] == {{0, 0, 1}} && a - one == {0, 0, 1}]; (* v416 (1): the Z[i] (square/seam) trichotomy *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2476)
- [(* v431 (1): two-family split forced by 30 = 2*3*5 *) checkExact["v431 E8.DEGREE.LADDER.01 (i): E8 exponents = phi(30)=8 totatives of h=30=2*N_fam*g_car; coprime to 6 => +-1 mod 6, so degrees occupy ONLY {0,2} mod 6", exps == tot30 && EulerPhi[h] == 8 && h == 2*3*5 && expMod6 == {1, 5} && degMod6 == {0, 2}]; (* v431 (2): 6k family = 6 x spine {2,3,4,5} = v91 anchor a=(1,1,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2663)
- [(* ---- (v73) k=c3/2 forced: variational factor x Gauss-Bonnet topology; Fursaev-Solodukhin S=A/4 ---- *) checkExact["k=c3/2=1/(16pi)=(1/2)*(1/(|Z2|*2pi*chi(S2))), chi(S2)=2; Fursaev-Solodukhin 4pi k = 1/4", Module[{c3 = 1/(8 Pi), chi = 2, Z2 = 2}, (c3/2 == 1/(16 Pi)) && (c3 == 1/(Z2*2 Pi*chi)) && (4 Pi*(c3/2) == 1/4)]]; (* ---- (v74) compiler micro-lemmas: pencil differences 2->16->48; anchor QF 41-25=16 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L352)
- [(* v222 CM-norm duality: 41 (square), 7 (hex), 13 (square) *) Ni[a_, b_] := a^2 + b^2; (* Gaussian Z[i] norm *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1793)
- [(* ---- (v115) anchor residue ---- The [N] Riemann-Hilbert parts (scipy ODE monodromy of the Fuchsian system, multi-seed uniqueness scan) are Python-only by convention; the exact lemmas are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L668)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* ---- (v144) det-ratio family cancellation ---- *) Module[{s, p, rb, rc, ro, poly, ratio, ser, cpar, epsSer}, s = 2 Sqrt[1 - \[CapitalDelta]^2/12]; p = 1 - \[CapitalDelta]^2/3; rb = (s + \[CapitalDelta])/2; rc = (s - \[CapitalDelta])/2; ro = -s; poly = Collect[Expand[(t - rb)(t - rc)(t - ro)], t, Simplify]; ratio = (rb rc)^(4/3); ser = Normal[Series[ratio, {\[CapitalDelta], 0, 3}]]; cpar = Simplify[p s/2]; epsSer = Normal[Series[1 - cpar, {\[CapitalDelta], 0, 3}]]; checkExact["v144 det-ratio family cancellation: e2-rigidity r_b r_c = 1 - Delta^2/3 exact (traceless cubic, e2 = -3); ratio = (1 - Delta^2/3)^(4/3) has NO first-order term, quadratic coefficient -4/9; eps = (3/8) Delta^2 => coefficient -32/27 = -|mu4| (2/3)^3", Simplify[rb rc - p] == 0 && Simplify[Coefficient[poly, t, 2]] == 0 && Simplify[Coefficient[poly, t, 1]] == -3 && Coefficient[ser, \[CapitalDelta], 1] == 0 && Coefficient[ser, \[CapitalDelta], 2] == -4/9 && Coefficient[epsSer, \[CapitalDelta], 2] == 3/8 && (-4/9)/(3/8) == -32/27 == -4 (2/3)^3]; ]; (* ---- (v145) pairing atoms ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1207)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [(* ---- (v146) Moebius D4 realisation ---- *) Module[{om, deckOK, invOK, ta, sig, p, tac, sigc, delta, iota}, om[k_] := z^(k - 1)/(z^4 - 1); deckOK = And @@ Table[ Simplify[(om[k] /. z -> I w) I - I^k (om[k] /. z -> w)] === 0, {k, 1, 3}]; invOK = Simplify[(om[1] /. z -> 1/w) (-1/w^2) - (om[3] /. z -> w)] === 0 && Simplify[(om[2] /. z -> 1/w) (-1/w^2) - (om[2] /. z -> w)] === 0 && Simplify[(om[3] /. z -> 1/w) (-1/w^2) - (om[1] /. z -> w)] === 0; ta = {{0, 1, 0}, {1, 0, 0}, {2, -2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; p = Transpose[{{0, 0, 1}, {0, 1, 2}, {1, 0, 0}}]; tac = Inverse[p] . ta . p; sigc = Inverse[p] . sig . p; delta = DiagonalMatrix[{I, -1, -I}]; iota = {{0, 0, 1}, {0, 1, 0}, {1, 0, 0}}; checkExact["v146 Moebius D4: delta* omega_k = i^k omega_k; iota* omega_(1,2,3) = omega_(3,2,1) (+1 on chi2, det -1); dihedral relations; T_A (cusp basis, char-2 line first) = the same reflection class as iota (fixes the self-conjugate line with +1, swaps the pair, det -1); Sigma = the delta-iota class", deckOK && invOK && iota . iota == IdentityMatrix[3] && Simplify[iota . delta . Inverse[iota] - Inverse[delta]] == ConstantArray[0, {3, 3}] && tac == {{1, 0, 0}, {0, 0, 1}, {0, 1, 0}} && Det[tac] == -1 && tac[[1, 1]] == 1 == iota[[2, 2]] && sigc == DiagonalMatrix[{-1, -1, 1}] && Simplify[(delta . iota)[[2, 2]]] == -1 && Simplify[Det[delta . iota]] == 1]; ]; (* ---- (v147) clock Gaussian model ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1239)
- [(* ---- (v116) resonance theorem ---- The [N] falsification control (scipy ODE) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L687)
- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)

## What the compiler outputs for the Standard Model and our reality

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3561-3605](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3561) · `section:9e586335a0db2028446d` · subsection

Every entry below is an output of [formula in source] through the [formula in source] compiler; none is an independent input. ``Reads'' names the lattice object the observable comes from.

## Grammar I — the carrier grammar ( [formula in source] )

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3606-3621](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3606) · `section:0a504430271a73e5e393` · section

Machine checks for this section: v2_ carrier_ pascal.py

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)

## Dual-root dictionary (everything from two charges)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3622-3666](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3622) · `section:1a24e636925cbf73fa9f` · subsection

Two carrier roots generate the family and the transport cusps . With [formula in source] and [formula in source] (the determinant-normalised carrier eigenvalues), the full one-family hypercharge spectrum and the flavor-transport cusps are sums of the two roots: [formula in source] [formula in source] [formula in source] All residuals are exactly zero. The Standard-Model charge table is not assumed; it is built by add

## Carrier arithmetic (proved identities)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3667-3691](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3667) · `section:7d57528668a5c0220a43` · subsection

The discrete coefficients are not isolated numbers; they are exact carrier traces: So: [formula in source] is a Pythagorean carrier identity ( [formula in source] ); equivalently the anchor-product form [formula in source] reads ``all four glue corners times all ten carrier pairs, plus the one leftover Higgs slot''; the electroweak exponent [formula in source] is the hypercharge variance times the [formula in source]

## Grammar II — the seed grammar (one decoder [formula in source] )

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3692-3727](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3692) · `section:78dc60846ed800922f5e` · section

Machine checks for this section: v106_ review_ validation.py

Explicit source references:

- [verification/v106_review_validation.py](../../../../verification/v106_review_validation.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)

## Grammar III — the action grammar (exponentials of [formula in source] )

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3728-3788](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3728) · `section:b1537a2c9cb5c3747a57` · section

The relation in plain words. The fine-structure constant is not just ``a number near [formula in source] '': it is the one exponential engine behind three wildly separated scales. Take the same [formula in source] and divide the carrier into it: [formula in source] of it sets the electroweak scale, [formula in source] it sets the Hubble scale, [formula in source] it sets the cosmological constant. The three action ch

Explicit source references:

- [verification/make_figures.py](../../../../verification/make_figures.py#L1) · explicit_file_citation

## The EM closure: [formula in source] as an explicit fixed point (made explicit here)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:3789-4044](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L3789) · `section:3d3092d4174b4ba2e0ec` · subsection

The engine [formula in source] is not an input — it is the unique root of an explicit closure equation (the exact electromagnetic closure theorem). With [formula in source] , [formula in source] , [formula in source] and the seam response [formula in source] , where the coefficient is [formula in source] , so the fine-structure constant reads the flavor transport budget [formula in source] and the [formula in source]

Explicit source references:

- [verification/v483_pillowcase_exact_traces.py](../../../../verification/v483_pillowcase_exact_traces.py#L1) · explicit_script_identifier
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_script_identifier
- [HYP.PHI0.PUNCTURE.01](../../../../verification/status_ledger.csv#L464) · explicit_claim_identifier · original status at linked ledger row
- [verification/v342_em_ward_heatkernel.py](../../../../verification/v342_em_ward_heatkernel.py#L1) · explicit_script_identifier
- [verification/v151_bfk_split.py](../../../../verification/v151_bfk_split.py#L1) · explicit_script_identifier
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_file_citation
- [verification/v461_seam_strict_locality.py](../../../../verification/v461_seam_strict_locality.py#L1) · explicit_script_identifier
- [verification/v382_alpha_quillen_exact.py](../../../../verification/v382_alpha_quillen_exact.py#L1) · explicit_file_citation
- [verification/v391_alpha_quillen_progress.py](../../../../verification/v391_alpha_quillen_progress.py#L1) · explicit_script_identifier
- [verification/v484_seam_contact_unit.py](../../../../verification/v484_seam_contact_unit.py#L1) · explicit_file_citation
- [verification/v48_em_ward.py](../../../../verification/v48_em_ward.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v341_alpha_quillen.py](../../../../verification/v341_alpha_quillen.py#L1) · explicit_file_citation
- [verification/v472_quillen_detline_moduli.py](../../../../verification/v472_quillen_detline_moduli.py#L1) · explicit_file_citation
- [verification/v239_kms_thermal_time.py](../../../../verification/v239_kms_thermal_time.py#L1) · explicit_script_identifier
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [verification/v470_alpha_inflow_level.py](../../../../verification/v470_alpha_inflow_level.py#L1) · explicit_script_identifier
- [verification/v435_alpha_quillen_chernlevel.py](../../../../verification/v435_alpha_quillen_chernlevel.py#L1) · explicit_file_citation
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v384_residual_certification.py](../../../../verification/v384_residual_certification.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_file_citation
- [EM.WARD.01](../../../../verification/status_ledger.csv#L70) · explicit_claim_identifier · original status at linked ledger row
- [verification/v60_lambda_metrology_branch.py](../../../../verification/v60_lambda_metrology_branch.py#L1) · explicit_script_identifier
- [verification/v456_seam_chirality_from_c3.py](../../../../verification/v456_seam_chirality_from_c3.py#L1) · explicit_script_identifier
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v433_alpha_quillen_heatkernel.py](../../../../verification/v433_alpha_quillen_heatkernel.py#L1) · explicit_file_citation
- [verification/v485_contact_diagonal_closed.py](../../../../verification/v485_contact_diagonal_closed.py#L1) · explicit_script_identifier
- [verification/v985_quillen_channel_swap.py](../../../../verification/v985_quillen_channel_swap.py#L1) · explicit_file_citation
- [verification/v434_alpha_quillen_betafunction.py](../../../../verification/v434_alpha_quillen_betafunction.py#L1) · explicit_file_citation
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [ALPHA.QUILLEN.FACES.01](../../../../verification/status_ledger.csv#L754) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* v461: tied obstruction integers + the reflection forcing (strict-local => C=-C => C=0) *) cMinus = 2^(gcar - 1)*1/2; (* 16*|C|/2 = 8, |C|=1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2881)
- [(* ==== v461/v462 round: the Kapustin-Fidkowski strict-locality obstruction (integer logic; the Wilson-loop winding/Chern themselves are numerical, Python-only) and the 128-spinor extension at character level -- the Jacobi/E8 theta identity theta2^8+theta3^8+theta4^8=2E4 (so the (E8)_1 character is the SO(16)_1 vacuum+spinor sum) and the 120+128=248 sector + finite 16-Majorana Fock counts; mirrors v461/v462. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2874)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v341 ALPHA.QUILLEN.01: the seam-form discriminant identities ==== *) Module[{c3v, phib}, c3v = 1/(8 Pi); phib = 1/(6 Pi); (* phi_base = (4/3) c3 carries q(A3): c3/phi_base = 3/4; with -5/4 = -q(D5) the F_U(1) seam response carries BOTH glue forms, q(D5)+q(A3)=2 = E8 root norm; counterterm coefficient (4/5)M = 8 b1 = 8*(41/10) with b1 the U(1)_Y one-loop beta (rank E8 = 8) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2248)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ==== v454/v456/v457/v459 round (G-block): the edge current-algebra/Sugawara c=8, the S3-from-P1 one-sided arithmetic, the (E8)_1 character/sector kill-test, and the lattice-VOA second route; mirrors v454/v456/v457/v459. The Casimir + Kac-Moody fits (v454), the Chern flip (v456) and the Tomita-Takesaki tower (v455) are numerical, Python-only; the exact algebra is mirrored here. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2827)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)
- [(* ---- (v983) SEAM.SIMPLECURRENT.GENERATOR.01: glue vector lambda = (omega_s, omega_f) ---- *) Module[{omegaS, omegaF, lam, inD5, inA3, inL0, gensD5, gensA3, dots, cosetRoots, census, lamV, omega2, nV, n2, cartanD8}, omegaS = ConstantArray[1/2, 5]; omegaF = {3/4, -1/4, -1/4, -1/4}; lam = Join[omegaS, omegaF]; inD5[x_] := (And @@ (IntegerQ /@ x)) && EvenQ[Total[x]]; inA3[y_] := (And @@ (IntegerQ /@ y)) && Total[y] === 0; inL0[z_] := inD5[Take[z, 5]] && inA3[Take[z, {6, 9}]]; checkExact["v983 NORMS+WEIGHT [E]: |omega_s|^2=5/4, |omega_f|^2=3/4, |lambda|^2=2, h_lambda=1", Total[omegaS^2] === 5/4 && Total[omegaF^2] === 3/4 && Total[lam^2] === 2 && Total[lam^2]/2 === 1]; checkExact["v983 ORDER FOUR [E]: 4*lambda in D5(+)A3, lambda and 2*lambda not -- [lambda] generates the diagonal Z4", inL0[4 lam] && ! inL0[2 lam] && ! inL0[lam]]; gensD5 = {{1, 1, 0, 0, 0}, {1, -1, 0, 0, 0}, {0, 1, 1, 0, 0}, {0, 0, 1, 1, 0}, {0, 0, 0, 1, 1}}; gensA3 = {{1, -1, 0, 0}, {0, 1, -1, 0}, {0, 0, 1, -1}}; dots = Join[omegaS . # & /@ gensD5, omegaF . # & /@ gensA3]; checkExact["v983 ISOTROPY+UNIMODULAR [E]: lambda.L0 subset Z on a generator set; det(D5)*det(A3)=16, index-4 glue => det L=1", (And @@ (IntegerQ /@ dots)) && 16/4^2 === 1]; cosetRoots[k_] := Module[{t = k lam, d5, a3}, d5 = Counts @ Select[ Total[(# + Take[t, 5])^2] & /@ Select[Tuples[Range[-5, 3], 5], EvenQ[Total[#]] &], # <= 2 &]; a3 = Counts @ Select[ Total[(Join[#, {-Total[#]}] + Take[t, {6, 9}])^2] & /@ Tuples[Range[-6, 6], 3], # <= 2 &]; Total[KeyValueMap[#2 Lookup[a3, 2 - #1, 0] &, d5]]]; census = Table[cosetRoots[k], {k, 0, 3}]; checkExact["v983 COSET ROOT CENSUS [E]: norm-2 vectors per fusion power k=0..3 = {52,64,60,64}, total 240; odd powers 64+64=128", census === {52, 64, 60, 64} && Total[census] === 240 && census[[2]] + census[[4]] === 128]; lamV = Join[{1, 0, 0, 0, 0}, omegaF]; omega2 = {1/2, 1/2, -1/2, -1/2}; nV = Total[lamV^2]; n2 = Total[omegaS^2] + Total[omega2^2]; cartanD8 = {{2, -1, 0, 0, 0, 0, 0, 0}, {-1, 2, -1, 0, 0, 0, 0, 0}, {0, -1, 2, -1, 0, 0, 0, 0}, {0, 0, -1, 2, -1, 0, 0, 0}, {0, 0, 0, -1, 2, -1, 0, 0}, {0, 0, 0, 0, -1, 2, -1, -1}, {0, 0, 0, 0, 0, -1, 2, 0}, {0, 0, 0, 0, 0, -1, 0, 2}}; checkExact["v983 KILLS+HOLOMORPHY SHADOW [E]: vector glue (v,omega_f) norm 7/4 and mismatched (omega_s, omega_2) norm 9/4 not in 2Z; det Cartan D8=4 vs glued det=1", nV === 7/4 && n2 === 9/4 && Det[cartanD8] === 4 && 16/4^2 === 1]; ]; (* ---- (v985) ALPHA.QUILLEN.EXACT.01: mu4 circulant spectra + graded channel swap ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L444)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [(* v454: level-1 Sugawara c = dim G/(1+h^v) = 8 for both SO(16)_1 and (E8)_1 *) cSO16 = 120/(1 + 14); cE8 = 248/(1 + 30); checkExact["v454 SEAM.EQUIV.EDGE.VIRASORO.01: level-1 Sugawara c=dim G/(1+h^v)=8 for BOTH SO(16)_1 (120/15) and (E8)_1 (248/31); 16 Majoranas => c_-=8=g_car+N_fam (the Casimir c and Kac-Moody central term <J_n J_-n>=n are numerical, Python-only)", cSO16 == 8 && cE8 == 8 && cSO16 == cE8 && 8 == gcar + Nfam]; (* v456: c3's '8' is the one-sided count; reflection C->-C so two-sided forces C=0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2835)
- [(* ---- (v47) Boundary Carrier Selection Theorem (Theorem A) ---- *) checkExact["q(D5)+q(A3)=5/4+3/4=2 (E8 root norm); glue index sqrt(4*4/1)=4=|mu4|", 5/4 + 3/4 == 2 && Sqrt[4*4/1] == 4]; checkExact["only n=5 gives 16-dim D_n half-spinor (2^{n-1}=16) => D5", Select[Range[2, 8], 2^(# - 1) == 16 &] == {5}]; (* ---- (v48) EM boundary Ward decomposition (Theorem C) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L184)
- [(* ---- (v150) replica EH model ---- *) Module[{cdef, imgOK, convOK, mellin, dz0, dC, target}, cdef[g_] := (1/12) (2 Pi/g - g/(2 Pi)); imgOK = And @@ Table[ FullSimplify[Sum[1/Sin[Pi k/n]^2, {k, 1, n - 1}] - (n^2 - 1)/3] === 0, {n, 2, 8}]; convOK = Simplify[(1/(4 nn)) (nn^2 - 1)/3 - cdef[2 Pi/nn]] === 0; mellin = Integrate[tt^(ss - 1) Exp[-mm^2 tt], {tt, 0, Infinity}, Assumptions -> ss > 0 && mm > 0]; dz0 = D[mm^(-2 ss), ss] /. ss -> 0; dC = D[cdef[gg], gg] /. gg -> 2 Pi; target = Simplify[12 Pi (1/2) (1/(8 Pi))]; checkExact["v150 replica EH model: image sum exact (N=2..8); orbifold deficit = C(2pi/N); Mellin Delta-zeta(s) = C m^-2s => Delta log det' = 2C ln m (cutoff-independent); dC/dgamma|_{2pi} = -1/(12pi) => EH form with k = ln m/(12pi); target k = c3/2 <=> ln m = 3/4 = q(A3)", imgOK && convOK && Simplify[mellin - Gamma[ss] mm^(-2 ss)] === 0 && Simplify[dz0 + 2 Log[mm]] === 0 && Simplify[dC + 1/(12 Pi)] === 0 && target == 3/4]; ]; (* ---- (v151) BFK split ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1321)
- [(* ---- (v60) Lambda branch selection: prefactor 3/(4pi^2), branch mis-scale 64pi^3/3 ---- *) checkExact["delta_top=48 c3^4=3/(256 pi^4); (8pi)^2 delta_top=3/(4 pi^2); 2c3/delta_top=64 pi^3/3 (G_N pinned)", With[{c3 = 1/(8 Pi), dt = 48 (1/(8 Pi))^4}, Simplify[dt - 3/(256 Pi^4)] == 0 && Simplify[(8 Pi)^2 dt - 3/(4 Pi^2)] == 0 && Simplify[2 c3/dt - 64 Pi^3/3] == 0]]; checkExact["action exponents (1,5,10) = K5 counts (5 vertices, C(5,2)=10 edges); Pascal 16=1+5+10", {1, 5, Binomial[5, 2]} == {1, 5, 10} && 1 + 5 + 10 == 16]; (* ---- (v61) boundary-CFT bridge: WZW central charges = atoms, conformal embedding ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L282)
- [(* ==== v342 EM.WARD.02: the heat-kernel origin of the F_U(1) terms ==== *) Module[{c3v, ointK, c3gb, gilkey, q2}, c3v = 1/(8 Pi); (* c3 = boundary Gauss-Bonnet coefficient: oint_{S^2} K = 2 pi chi = 4 pi (chi=2), c3 = 1/(|Z2| oint K) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2259)

## The decuple bridge (new, exact headline)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:4045-4069](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L4045) · `section:1c35145be296ff736043` · subsection

Eliminating [formula in source] between the electroweak and the cosmological-constant lines gives a direct relation between the two scales:

## The full power tower: [formula in source] on the carrier graph [formula in source]

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:4070-4089](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L4070) · `section:9335ed116a174d582d77` · subsection

The decuple bridge is one rung of a tower. Writing [formula in source] for the stripped electroweak unit, all three cosmological scales are powers of the same [formula in source] with binomial exponents (verified exactly): with residues [formula in source] and [formula in source] . . The exponents are the complete-graph counts of the five-slot carrier [formula in source] : [formula in source] So the cosmological cons

## Hubble is the square root of [formula in source] (corollary, exact)

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:4090-4102](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L4090) · `section:366174835e49d62ca259` · subsection

On the comparison layer [formula in source] ; equating to the TFPT line gives So the Hubble rung is not an independent third hit: it is the square root of the vacuum energy plus a geometric cosmology factor. The genuine TFPT content is the single [formula in source] . (The numerical coincidence [formula in source] is just [formula in source] and is [formula in source] -dependent; not a claim. )

## The [formula in source] orders of the cosmological constant

[experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex:4103-4127](../../../../experiments/theory-contracts/universalraum-native-exterior-reset-20260915/sources/tfpt_1_architecture_e8.tex#L4103) · `section:8d43e1355ebf65854c47` · subsection

The `` [formula in source] '' is the action [formula in source] ; the `` [formula in source] '' is the seam defect [formula in source] .

Explicit source references:

- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_file_citation
