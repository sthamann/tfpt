# Archives and dated records — part 23

[Topic entry](../history.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## 2026-06-25 (The Gaussian operator [formula in source] the atom trichotomy: v415, v416)

[documents/changelog/sections/013-source.tex:91-121](../../../../documents/changelog/sections/013-source.tex#L91) · `section:bb2a02a767e560376342` · subsection

New module v415 ( DIAMOND.GAUSS.01). The square CM-norm dictionary of v222/ v230 is operator-realised, and the [formula in source] deck becomes an intrinsic diamond object. \ the integer commutator [formula in source] has [formula in source] , [formula in source] on the rank- [formula in source] image and [formula in source] — a [formula in source] quarter-turn born from the binary [formula in source] and ternary [fo

Explicit source references:

- [ARITH.TRICHOTOMY.01](../../../../verification/status_ledger.csv#L484) · explicit_claim_identifier · original status at linked ledger row
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation
- [verification/v410_sheet_generator_binary.py](../../../../verification/v410_sheet_generator_binary.py#L1) · explicit_script_identifier
- [verification/script_registry.csv](../../../../verification/script_registry.csv#L1) · explicit_file_citation
- [verification/v222_cm_norm_duality.py](../../../../verification/v222_cm_norm_duality.py#L1) · explicit_script_identifier
- [verification/v403_facet_compositum.py](../../../../verification/v403_facet_compositum.py#L1) · explicit_script_identifier
- [verification/v95_centered_diamond.py](../../../../verification/v95_centered_diamond.py#L1) · explicit_script_identifier
- [verification/wolfram/tfpt_readouts_extension.wl](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1) · explicit_file_citation
- [verification/v140_canonical_map.py](../../../../verification/v140_canonical_map.py#L1) · explicit_script_identifier
- [verification/v412_sheet_source_corner_J.py](../../../../verification/v412_sheet_source_corner_J.py#L1) · explicit_script_identifier
- [DIAMOND.GAUSS.01](../../../../verification/status_ledger.csv#L483) · explicit_claim_identifier · original status at linked ledger row
- [verification/v416_atom_trichotomy.py](../../../../verification/v416_atom_trichotomy.py#L1) · explicit_script_identifier
- [GATE.WOLFRAM.02](../../../../verification/status_ledger.csv#L168) · explicit_claim_identifier · original status at linked ledger row
- [verification/v415_gaussian_operator.py](../../../../verification/v415_gaussian_operator.py#L1) · explicit_script_identifier
- [verification/v230_center_budget_norms.py](../../../../verification/v230_center_budget_norms.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v222 CM-norm duality: 41 (square), 7 (hex), 13 (square) *) Ni[a_, b_] := a^2 + b^2; (* Gaussian Z[i] norm *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1793)
- [(* v411: u/d ratio as a pure V-power readout *) num = one . MatrixPower[V, 4] . one; den = (a . V . one)(one . MatrixPower[V, 2] . one); checkExact["v411 FLAV.UD.VPOWER.01: c_u/c_d = (1.V^4.1)/((a.V.1)(1.V^2.1)) = 55/(9*13) = 55/117, identical to g_car*||Pl(K)||_1/(N_fam^2 Delta_Q) = 5*11/(9*13); RE-ENCODING, value stays [C]", num == 55 && a . V . one == 9 && one . MatrixPower[V, 2] . one == 13 && num/den == 55/117 && (5*11)/(9*13) == 55/117]; (* v412: the sheet source corner J = M(1,-2) on the Z2 wall *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2417)
- [(* ==== v410-v414 round: the sheet generator V as a binary internal compiler ==== *) Module[{R, Q, V, C, J, one, a, I3, t, lam, Mt, e1, e2, e3, d1, d2, en, num, den}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; V = Q . DiagonalMatrix[{0, 1, 1}]; C = R + Q . DiagonalMatrix[{1, 0, 0}]; J = C - 2 V; one = {1, 1, 1}; a = {1, 1, 2}; I3 = IdentityMatrix[3]; (* v410: closed form V^n, binary spine, bilinear families, theta cross-link *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2393)
- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)
- [(* ==== v415-v416 round: Gaussian operator + atom trichotomy ==== *) Module[{R, Q, U, V, J, I3, one, a, Pi2, D, x, neis}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; U = Q . DiagonalMatrix[{1, 0, 0}]; V = Q . DiagonalMatrix[{0, 1, 1}]; J = (U . V - V . U)/3; I3 = IdentityMatrix[3]; one = {1, 1, 1}; a = {1, 1, 2}; (* v415 (1): J = [U,V]/3 is an integer mu4 quarter-turn complex structure *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2447)
- [(* v415 (4): the intrinsic order-4 mu4 deck D = -I + J - J^2 *) Pi2 = I3 + J . J; D = J - Pi2; checkExact["v415 DIAMOND.GAUSS.01 (iv): the intrinsic deck D=-I+J-J^2={{-1,1,0},{-2,1,0},{-4,3,-1}} is order 4 (D^4=I), Spec(D)={i,-1,-i} (the seam-deck spectrum, v146); chi2 line = ker[U,V] = NullSpace = {(0,0,1)} = a-1", D == {{-1, 1, 0}, {-2, 1, 0}, {-4, 3, -1}} && MatrixPower[D, 4] == I3 && Sort[Eigenvalues[D]] == Sort[{I, -I, -1}] && NullSpace[J] == {{0, 0, 1}} && a - one == {0, 0, 1}]; (* v416 (1): the Z[i] (square/seam) trichotomy *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2476)
- [(* v230 center budget (7,11,13) = three local norms *) RRm = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; QQm = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Cc2 = RRm + QQm.DiagonalMatrix[{1, 0, 0}]; checkExact["v230 CENTER.NORM.01: C=R+Q diag(1,0,0) row sums (7,11,13) = " <> "(N_Z[omega](3+2w)=7 hex, C(4,0)+C(4,1)+C(4,2)=11 QBL Fock, N_Z[i](3+2i)=13 square) " <> "= (hex norm, boundary Fock count, square norm)", Total /@ Cc2 == {7, 11, 13} && {Nw[3, 2], Binomial[4, 0] + Binomial[4, 1] + Binomial[4, 2], Ni[3, 2]} == {7, 11, 13}]; (* v224 diamond F_transfer path: sheet axis curved, winding axis flat, Plucker steps *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1838)
- [(* ---- (v95) centered flavor diamond ---- *) Uop = Q.DiagonalMatrix[{1, 0, 0}]; Vop = Q.DiagonalMatrix[{0, 1, 1}]; Cc = R + Uop; Lop = R + 2 Uop; Fop = R + Q; checkExact["v95 centered cross: Q=U+V; R=C-U, L=C+U, K=C-V, F=C+V", (Q == Uop + Vop) && (R == Cc - Uop) && (Lop == Cc + Uop) && (K == Cc - Vop) && (Fop == Cc + Vop)]; checkExact["v95 axes spectra: Spec U = {3,0,0} (winding), Spec V = {0,1,2} = N_fam*cusp", (Sort[Eigenvalues[Uop]] == {0, 0, 3}) && (Sort[Eigenvalues[Vop]] == {0, 1, 2})]; checkExact["v95 center invariants: tr C=12, det C=14, sum C=31=2^g_car-1, det B_C=28", (Tr[Cc] == 12) && (Det[Cc] == 14) && (Total[Cc, 2] == 31) && (31 == 2^gcar - 1) && (Det[bb[Cc]] == 28)]; checkExact["v95 ray alignment: Pi_R(C)=7(2,3,1), Pi_R(L)=10(2,3,1)", (plR[Cc] == 7 {2, 3, 1}) && (plR[Lop] == 10 {2, 3, 1})]; (* ---- (v96) branch-kernel selection (P1) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L204)
- [(* ---- (v140) canonical map ---- *) Module[{charf, cu, cmu, cw}, charf[m_] := Mod[Round[Arg[#]/(Pi/2)], 4] & /@ Diagonal[m]; cu = charf[DiagonalMatrix[{1, I, -I}]]; cmu = charf[-DiagonalMatrix[{1, I, -I}]]; cw = charf[DiagonalMatrix[{I, I^2, I^3}]]; checkExact["v140 canonical map: deck U chars (0,1,3) miss 2; -U = (2,3,1) and i^Q+ = (1,2,3) both have SET {1,2,3} = H^1; i^Q+ assignment = Q+, -U assignment = Q+ o rho (one Z3 rotation apart)", cu == {0, 1, 3} && cmu == {2, 3, 1} && cw == {1, 2, 3} && Sort[cmu] == {1, 2, 3} == Sort[cw] && cmu == (cw[[#]] & /@ {2, 3, 1})]; ]; (* ---- (v141) deck selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1122)
- [(* v415 (2): the Gaussian integers 3+2i, 5+4i are eigenvalues *) checkExact["v415 DIAMOND.GAUSS.01 (ii): 3I+2J has spectrum {3+2i,3-2i,3} and 5I+4J has {5+4i,5-4i,5}; |3+2i|^2=13=Delta_Q, |5+4i|^2=41=10 b1 -- the Gaussian integers are literal operator eigenvalues", Sort[Eigenvalues[3 I3 + 2 J]] == Sort[{3 + 2 I, 3 - 2 I, 3}] && Sort[Eigenvalues[5 I3 + 4 J]] == Sort[{5 + 4 I, 5 - 4 I, 5}] && 3^2 + 2^2 == 13 && 5^2 + 4^2 == 41]; (* v415 (3): the square-norm dictionary as operator identities *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2463)
- [(* ---- (v218) DIAMOND.AXIS/PLUCKER/SPECTRAL.01: the diamond axis geometry ---- *) Module[{R, Q, a, one, Cc, U, V, K, L, F, anc, plL, ram, x, y, dU, dV, bU, bV, sd, bsd, sq, ker}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; one = {1, 1, 1}; a = {1, 1, 2}; Cc = R + Q.DiagonalMatrix[{1, 0, 0}]; (* center C = M(1,0) (v95) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1751)
- [(* v416 (2): the Z[omega] (hex/flavor) trichotomy + ramified prime = own atom *) neis[aa_, bb_] := aa^2 - aa bb + bb^2; checkExact["v416 ARITH.TRICHOTOMY.01 (Z[omega], hex/flavor): 3 RAMIFIES (N(1-omega)=3), 2 INERT (2 mod 3=2, norm 4), 5 INERT (5 mod 3=2, norm 25=g_car^2); the ramified prime of each ring is its atom (Z[i]<->2, Z[omega]<->3)", neis[1, -1] == 3 && Mod[2, 3] == 2 && neis[2, 0] == 4 && Mod[5, 3] == 2 && neis[5, 0] == 25]; (* v416 (3): the three facets ramify over one atom each (v403) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2489)
- [(* v417 (1): the family rotation = Eisenstein deck + the hex norm 7 *) checkExact["v417 DIAMOND.EISEN.01 (i): P=(1 2 3) Eisenstein deck (P^3=I, P^2+P+I=ONES); (3I+2P)(3I+2P^2)=7I+6 ONES with Spec {7,7,25} (7=N_omega(3+2omega)=scalaron, 25=g_car^2) -- the dual of v415's {13,13,9}; NEG (5I+4P)(5I+4P^2)->{21,21,81}, N_omega(5,4)=21!=41", MatrixPower[P, 3] == I3 && MatrixPower[P, 2] + P + I3 == ones3 && (3 I3 + 2 P) . (3 I3 + 2 MatrixPower[P, 2]) == 7 I3 + 6 ones3 && Sort[Eigenvalues[(3 I3 + 2 P) . (3 I3 + 2 MatrixPower[P, 2])]] == Sort[{7, 7, 25}] && (3^2 - 3*2 + 2^2) == 7 && Sort[Eigenvalues[(5 I3 + 4 P) . (5 I3 + 4 MatrixPower[P, 2])]] == Sort[{21, 21, 81}] && (5^2 - 5*4 + 4^2) == 21]; (* v417 (2): the CP clock W = -P^2 and both CP phases *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2508)

## 2026-06-24 (The sheet generator [formula in source] as a binary internal compiler: v410– v414)

[documents/changelog/sections/013-source.tex:122-158](../../../../documents/changelog/sections/013-source.tex#L122) · `section:2ff762f6d6932ac2b2c5` · subsection

New module v410 ( SHEET.GEN.BINARY.01). The rank- [formula in source] sheet axis [formula in source] of the centered cross ( v95/ v218) is a binary internal compiler: its powers print the carrier spine. \ the closed form [formula in source] (proved by the inductive step [formula in source] ), so [formula in source] ; \ the four bilinear families [formula in source] , [formula in source] , [formula in source] , [formu

Explicit source references:

- [verification/v410_sheet_generator_binary.py](../../../../verification/v410_sheet_generator_binary.py#L1) · explicit_script_identifier
- [verification/v224_diamond_ftransfer_path.py](../../../../verification/v224_diamond_ftransfer_path.py#L1) · explicit_script_identifier
- [DIAMOND.SHEET.CALCULUS.01](../../../../verification/status_ledger.csv#L481) · explicit_claim_identifier · original status at linked ledger row
- [verification/script_registry.csv](../../../../verification/script_registry.csv#L1) · explicit_file_citation
- [verification/v412_sheet_source_corner_J.py](../../../../verification/v412_sheet_source_corner_J.py#L1) · explicit_script_identifier
- [verification/v218_diamond_axis_geometry.py](../../../../verification/v218_diamond_axis_geometry.py#L1) · explicit_script_identifier
- [verification/v413_sheet_characteristic_calculus.py](../../../../verification/v413_sheet_characteristic_calculus.py#L1) · explicit_script_identifier
- [FLAV.UD.VPOWER.01](../../../../verification/status_ledger.csv#L479) · explicit_claim_identifier · original status at linked ledger row
- [verification/v94_sheet_diamond.py](../../../../verification/v94_sheet_diamond.py#L1) · explicit_script_identifier
- [DIAMOND.CENTER.RESOLVENT.01](../../../../verification/status_ledger.csv#L482) · explicit_claim_identifier · original status at linked ledger row
- [verification/v414_center_resolvent_portal.py](../../../../verification/v414_center_resolvent_portal.py#L1) · explicit_script_identifier
- [DIAMOND.SHEET.SOURCE.J.01](../../../../verification/status_ledger.csv#L480) · explicit_claim_identifier · original status at linked ledger row
- [verification/v95_centered_diamond.py](../../../../verification/v95_centered_diamond.py#L1) · explicit_script_identifier
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v135_det_surface.py](../../../../verification/v135_det_surface.py#L1) · explicit_script_identifier
- [verification/v411_ud_ratio_vpower.py](../../../../verification/v411_ud_ratio_vpower.py#L1) · explicit_script_identifier
- [SHEET.GEN.BINARY.01](../../../../verification/status_ledger.csv#L478) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v230 center budget (7,11,13) = three local norms *) RRm = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; QQm = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Cc2 = RRm + QQm.DiagonalMatrix[{1, 0, 0}]; checkExact["v230 CENTER.NORM.01: C=R+Q diag(1,0,0) row sums (7,11,13) = " <> "(N_Z[omega](3+2w)=7 hex, C(4,0)+C(4,1)+C(4,2)=11 QBL Fock, N_Z[i](3+2i)=13 square) " <> "= (hex norm, boundary Fock count, square norm)", Total /@ Cc2 == {7, 11, 13} && {Nw[3, 2], Binomial[4, 0] + Binomial[4, 1] + Binomial[4, 2], Ni[3, 2]} == {7, 11, 13}]; (* v224 diamond F_transfer path: sheet axis curved, winding axis flat, Plucker steps *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1838)
- [(* ---- (v134) dual anchor ---- *) Module[{rmat, lmat, qmat, av, onev, e1v, nv, d, rinv1}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; lmat = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; av = {1, 1, 2}; onev = {1, 1, 1}; e1v = {1, 0, 0}; nv = {5, -9, 6}; d = av . Inverse[rmat]; rinv1 = Inverse[rmat] . onev; checkExact["v134 dual anchor: a.R^-1 = a.L^-1 = (-1/2,-1/2,1); d.1 = 0, d.a = 1; (1,1,-2) = -2d; d = (3/2)(a - (4/3)1)", d == av . Inverse[lmat] && d == {-1/2, -1/2, 1} && d . onev == 0 && d . av == 1 && {1, 1, -2} == -2 d && d == 3/2 (av - 4/3 onev)]; checkExact["v134 Sherman-Morrison: L = R + 6*1 e1^T; R^-1 1 = (1,1,-1)/4; a on the invariance plane, 1/e1/n not (1/4, 1/4, -5/2); n.1 = 2", lmat == rmat + 6 Outer[Times, onev, e1v] && rinv1 == {1/4, 1/4, -1/4} && av . rinv1 == 0 && onev . rinv1 == 1/4 && e1v . rinv1 == 1/4 && nv . rinv1 == -5/2 && nv . onev == 2]; ]; (* ---- (v135) determinant surface ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1010)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [(* v431 (3): 6k+2 family = {2} U det-ladder {8,14,20} on winding line 6s+8 *) fam2 = Sort[Select[degs, Mod[#, 6] == 2 &]]; R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; C = R + Q . DiagonalMatrix[{1, 0, 0}]; L = R + Q . DiagonalMatrix[{2, 0, 0}]; ladder = {Det[R], Det[C], Det[L]}; surf = Table[6 s + 8, {s, 0, 2}]; checkExact["v431 E8.DEGREE.LADDER.01 (iii): degrees==2 mod 6 = {2,8,14,20}; {8,14,20}=(det R,det C,det L)=winding line det M(s,0)=6s+8 (v135); 2=matched metric, 8=rank E8", fam2 == {2, 8, 14, 20} && ladder == {8, 14, 20} && ladder == surf && ladder[[1]] == 8]; (* v431 (4): 18 = 6*N_fam spine member, not det-ladder holdout *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2678)
- [(* ---- (v95) centered flavor diamond ---- *) Uop = Q.DiagonalMatrix[{1, 0, 0}]; Vop = Q.DiagonalMatrix[{0, 1, 1}]; Cc = R + Uop; Lop = R + 2 Uop; Fop = R + Q; checkExact["v95 centered cross: Q=U+V; R=C-U, L=C+U, K=C-V, F=C+V", (Q == Uop + Vop) && (R == Cc - Uop) && (Lop == Cc + Uop) && (K == Cc - Vop) && (Fop == Cc + Vop)]; checkExact["v95 axes spectra: Spec U = {3,0,0} (winding), Spec V = {0,1,2} = N_fam*cusp", (Sort[Eigenvalues[Uop]] == {0, 0, 3}) && (Sort[Eigenvalues[Vop]] == {0, 1, 2})]; checkExact["v95 center invariants: tr C=12, det C=14, sum C=31=2^g_car-1, det B_C=28", (Tr[Cc] == 12) && (Det[Cc] == 14) && (Total[Cc, 2] == 31) && (31 == 2^gcar - 1) && (Det[bb[Cc]] == 28)]; checkExact["v95 ray alignment: Pi_R(C)=7(2,3,1), Pi_R(L)=10(2,3,1)", (plR[Cc] == 7 {2, 3, 1}) && (plR[Lop] == 10 {2, 3, 1})]; (* ---- (v96) branch-kernel selection (P1) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L204)
- [(* v413: the sheet axis is a characteristic-difference calculator *) Mt = C + t V; e1 = Tr[Mt]; e3 = Det[Mt]; e2 = (Tr[Mt]^2 - Tr[Mt . Mt])/2; d1[f_] := (f /. t -> t + 1) - f; d2[f_] := d1[d1[f]]; en = a . Mt . a; checkExact["v413 DIAMOND.SHEET.CALCULUS.01: on M_t=C+tV, e1=3t+12, e2=2t^2+15t+25, e3=4t^2+14t+14 => Delta e1=3=N_fam, Delta^2 e2=4=|mu4|, Delta^2 e3=8=rank E8; anchor energy a.M_t.a = 52+11t (30->41->52->63)", Simplify[e1 - (3 t + 12)] == 0 && Simplify[e2 - (2 t^2 + 15 t + 25)] == 0 && Simplify[e3 - (4 t^2 + 14 t + 14)] == 0 && Simplify[d1[e1] - 3] == 0 && Simplify[d2[e2] - 4] == 0 && Simplify[d2[e3] - 8] == 0 && Simplify[en - (52 + 11 t)] == 0]; (* v414: the center C is a resolvent portal G2 -> F4 -> E8 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2430)
- [(* ---- (v218) DIAMOND.AXIS/PLUCKER/SPECTRAL.01: the diamond axis geometry ---- *) Module[{R, Q, a, one, Cc, U, V, K, L, F, anc, plL, ram, x, y, dU, dV, bU, bV, sd, bsd, sq, ker}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; one = {1, 1, 1}; a = {1, 1, 2}; Cc = R + Q.DiagonalMatrix[{1, 0, 0}]; (* center C = M(1,0) (v95) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1751)
- [(* v411: u/d ratio as a pure V-power readout *) num = one . MatrixPower[V, 4] . one; den = (a . V . one)(one . MatrixPower[V, 2] . one); checkExact["v411 FLAV.UD.VPOWER.01: c_u/c_d = (1.V^4.1)/((a.V.1)(1.V^2.1)) = 55/(9*13) = 55/117, identical to g_car*||Pl(K)||_1/(N_fam^2 Delta_Q) = 5*11/(9*13); RE-ENCODING, value stays [C]", num == 55 && a . V . one == 9 && one . MatrixPower[V, 2] . one == 13 && num/den == 55/117 && (5*11)/(9*13) == 55/117]; (* v412: the sheet source corner J = M(1,-2) on the Z2 wall *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2417)
- [(* ==== v410-v414 round: the sheet generator V as a binary internal compiler ==== *) Module[{R, Q, V, C, J, one, a, I3, t, lam, Mt, e1, e2, e3, d1, d2, en, num, den}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; V = Q . DiagonalMatrix[{0, 1, 1}]; C = R + Q . DiagonalMatrix[{1, 0, 0}]; J = C - 2 V; one = {1, 1, 1}; a = {1, 1, 2}; I3 = IdentityMatrix[3]; (* v410: closed form V^n, binary spine, bilinear families, theta cross-link *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2393)

## 2026-06-24 (Two new tracked targets + axion-branch consistency: v408, v409)

[documents/changelog/sections/013-source.tex:159-192](../../../../documents/changelog/sections/013-source.tex#L159) · `section:cb81efd922f7b6f4776f` · subsection

New module v408 ( HYP.PHI0.PUNCTURE.01). Names the [formula in source] puncture term [formula in source] as the order- [formula in source] local boundary heat-kernel (Seeley–DeWitt) contact term of the [formula in source] puncture divisor, summed over [formula in source] admissible states — the analytic complement of the icosahedral tree term ( v396). \ the exact split [formula in source] , the puncture count, the cl

Explicit source references:

- [verification/v408_phi0_puncture_heatkernel.py](../../../../verification/v408_phi0_puncture_heatkernel.py#L1) · explicit_script_identifier
- [verification/v409_coxeter_prime2_lemma.py](../../../../verification/v409_coxeter_prime2_lemma.py#L1) · explicit_script_identifier
- [ARCH.QUAD.01](../../../../verification/status_ledger.csv#L189) · explicit_claim_identifier · original status at linked ledger row
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_script_identifier
- [HYP.PHI0.PUNCTURE.01](../../../../verification/status_ledger.csv#L464) · explicit_claim_identifier · original status at linked ledger row
- [verification/v396_phi0_icosahedral.py](../../../../verification/v396_phi0_icosahedral.py#L1) · explicit_script_identifier
- [FORM.COXETER.PRIME2.01](../../../../verification/status_ledger.csv#L466) · explicit_claim_identifier · original status at linked ledger row
- [RES.COXETER.SYMMETRY.01](../../../../verification/status_ledger.csv#L465) · explicit_claim_identifier · original status at linked ledger row
- [experiments/lean4-carrier-rigidity/TfptCarrier/CoxeterPrime2.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CoxeterPrime2.lean#L1) · explicit_file_citation
- [verification/v394_coxeter_atoms.py](../../../../verification/v394_coxeter_atoms.py#L1) · explicit_script_identifier
- [verification/v407_dn_pairings_omega.py](../../../../verification/v407_dn_pairings_omega.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CoxeterPrime2.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CoxeterPrime2.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)

## 2026-06-24 (Cross-surface consistency sweep: papers, website, gates, figures realigned)

[documents/changelog/sections/013-source.tex:193-201](../../../../documents/changelog/sections/013-source.tex#L193) · `section:3c0ef7a887cebe028f40` · subsection

Ledger hygiene. Resolved a duplicate active claim_id: GATE.UWALL.06–09 was carried by two distinct chains. It is an ID collision (not a supersede): the monodromy/residue chain v114– v117 keeps .06–.09 (as asserted by v123_inventory_update.py and run_all.py); the older exterior-leg chain v42– v45 is renumbered to GATE.UWALL.15–.18 (internal depends_on carried along). No claim content changed. Website. papers.ts docume

Explicit source references:

- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier
- [verification/v42_exterior_leg.py](../../../../verification/v42_exterior_leg.py#L1) · explicit_script_identifier
- [verification/v407_dn_pairings_omega.py](../../../../verification/v407_dn_pairings_omega.py#L1) · explicit_script_identifier
- [verification/v45_family_exterior.py](../../../../verification/v45_family_exterior.py#L1) · explicit_script_identifier
- [GATE.UWALL.06](../../../../verification/status_ledger.csv#L198) · explicit_claim_identifier · original status at linked ledger row
- [verification/v123_inventory_update.py](../../../../verification/v123_inventory_update.py#L1) · explicit_file_citation
- [verification/v114_torsion_delta.py](../../../../verification/v114_torsion_delta.py#L1) · explicit_script_identifier
- [GATE.UWALL.15](../../../../verification/status_ledger.csv#L66) · explicit_claim_identifier · original status at linked ledger row
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [(* ---- (v42) Exterior Leg Lemma: u/d leg is a Lambda^2 F area, not a scalar ---- *) (* u,d share (r,w)=(1,1): the C6 resolvent reads only (r,w) => scalar ratio = 1. *)](../../../../verification/wolfram/tfpt_readouts.wl#L148)
- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *) checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+", Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16]; checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car", Sort[Abs[plLeft[K]]] == {1, 4, 6} && Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar]; checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car", 4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15]; (* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L168)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)

## 2026-06-24 (The [formula in source] dual keystone + the flavor residuals it homes: v405– v407)

[documents/changelog/sections/013-source.tex:202-208](../../../../documents/changelog/sections/013-source.tex#L202) · `section:20ef03b5c6c62b042300` · subsection

/ / \ v405_seam_equiv_omega.py ( SEAM.EQUIV.02): the dual keystone at [formula in source] – the family/flavor sector as the order- [formula in source] Eisenstein [formula in source] face of [formula in source] , dual to the seam [formula in source] at [formula in source] ( v404). A named contract (genre of v286/ v398), NOT a closure. \ [formula in source] (the family CM point degenerates [formula in source] ) vs [for

Explicit source references:

- [FLAV.SELECTOR.CLOSE.01](../../../../verification/status_ledger.csv#L477) · explicit_claim_identifier · original status at linked ledger row
- [verification/v407_dn_pairings_omega.py](../../../../verification/v407_dn_pairings_omega.py#L1) · explicit_file_citation
- [FLAV.PMNS.CLOSE.01](../../../../verification/status_ledger.csv#L476) · explicit_claim_identifier · original status at linked ledger row
- [verification/v286_seam_equivalence_contract.py](../../../../verification/v286_seam_equivalence_contract.py#L1) · explicit_script_identifier
- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_script_identifier
- [verification/v272_nu_mass_scale.py](../../../../verification/v272_nu_mass_scale.py#L1) · explicit_script_identifier
- [verification/v140_canonical_map.py](../../../../verification/v140_canonical_map.py#L1) · explicit_script_identifier
- [verification/v136_dual_normal_selector.py](../../../../verification/v136_dual_normal_selector.py#L1) · explicit_script_identifier
- [verification/v404_e8_char_cm_duality.py](../../../../verification/v404_e8_char_cm_duality.py#L1) · explicit_script_identifier
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.02](../../../../verification/status_ledger.csv#L475) · explicit_claim_identifier · original status at linked ledger row
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v406_pmns_phase_origin.py](../../../../verification/v406_pmns_phase_origin.py#L1) · explicit_file_citation
- [verification/v405_seam_equiv_omega.py](../../../../verification/v405_seam_equiv_omega.py#L1) · explicit_script_identifier
- [verification/v398_seam_state_rigidity.py](../../../../verification/v398_seam_state_rigidity.py#L1) · explicit_script_identifier
- [verification/v268_theta13_carrier_trace.py](../../../../verification/v268_theta13_carrier_trace.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* ---- (v140) canonical map ---- *) Module[{charf, cu, cmu, cw}, charf[m_] := Mod[Round[Arg[#]/(Pi/2)], 4] & /@ Diagonal[m]; cu = charf[DiagonalMatrix[{1, I, -I}]]; cmu = charf[-DiagonalMatrix[{1, I, -I}]]; cw = charf[DiagonalMatrix[{I, I^2, I^3}]]; checkExact["v140 canonical map: deck U chars (0,1,3) miss 2; -U = (2,3,1) and i^Q+ = (1,2,3) both have SET {1,2,3} = H^1; i^Q+ assignment = Q+, -U assignment = Q+ o rho (one Z3 rotation apart)", cu == {0, 1, 3} && cmu == {2, 3, 1} && cw == {1, 2, 3} && Sort[cmu] == {1, 2, 3} == Sort[cw] && cmu == (cw[[#]] & /@ {2, 3, 1})]; ]; (* ---- (v141) deck selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1122)
- [(* ---- (v136) dual-normal selector ---- *) Module[{dv, nv, av, rmat, qmat, kmat, sols, a0, v0, sigma, adjA0, grp, gens, reals}, dv = {-1/2, -1/2, 1}; nv = {5, -9, 6}; av = {1, 1, 2}; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; kmat = rmat + qmat . DiagonalMatrix[{1, -1, -1}]; sols = Table[Select[Tuples[Range[0, 5], 3], dv . # == av[[j]] && nv . # == 8 Boole[j == 1] &], {j, 3}]; checkExact["v136 column normal form: d.c_j = a_j, n.c_j = 8 delta_1j; kernel (6,8,7); each column UNIQUE in {0..5}^3 (1 of 216)", (dv . #) & /@ Transpose[rmat] == av && (nv . #) & /@ Transpose[rmat] == {8, 0, 0} && 7 First[NullSpace[{dv, nv}]] == {6, 8, 7} && Length /@ sols == {1, 1, 1} && (First /@ sols) == Transpose[rmat]]; checkExact["v136 honesty: K not pinned by (d,n) (d.K = (1,1/2,1), n.K = (14,1,-6)); det K = 4 via the diamond", dv . kmat == {1, 1/2, 1} && nv . kmat == {14, 1, -6} && Det[kmat] == 4]; a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; v0 = First[NullSpace[a0]]; v0 = v0/v0[[2]] 3; sigma = {2, -9, 5}; adjA0 = Transpose[Table[(-1)^(i + j) Det[Drop[a0, {i}, {j}]], {i, 3}, {j, 3}]]; checkExact["v136 spectral normal: A0* zero mode signed squares = -(2,-9,5); ||v||^2 = 16/9; adj(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1050)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)

## 2026-06-24 (The arithmetic hull + the [formula in source] -character CM duality: v403, v404)

[documents/changelog/sections/013-source.tex:209-214](../../../../documents/changelog/sections/013-source.tex#L209) · `section:8e3e6d08d3c102a09298` · subsection

/ \ v403_facet_compositum.py ( ARITH.HULL.01): the three single-prime number-field facets of the order- [formula in source] clock ( v390/ v394, used so far only one at a time) compose to one field [formula in source] . \ the squarefree parts [formula in source] are independent in [formula in source] , so [formula in source] with Galois group [formula in source] (order [formula in source] ); \ exactly [formula in sour

Explicit source references:

- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v404_e8_char_cm_duality.py](../../../../verification/v404_e8_char_cm_duality.py#L1) · explicit_script_identifier
- [ARITH.HULL.01](../../../../verification/status_ledger.csv#L473) · explicit_claim_identifier · original status at linked ledger row
- [verification/v267_qgeo_rigidity_minimal_axiom.py](../../../../verification/v267_qgeo_rigidity_minimal_axiom.py#L1) · explicit_script_identifier
- [verification/v390_prime2_facet.py](../../../../verification/v390_prime2_facet.py#L1) · explicit_script_identifier
- [verification/v403_facet_compositum.py](../../../../verification/v403_facet_compositum.py#L1) · explicit_script_identifier
- [verification/v220_cp_hexagonal_modulus.py](../../../../verification/v220_cp_hexagonal_modulus.py#L1) · explicit_script_identifier
- [E8.CMDUAL.01](../../../../verification/status_ledger.csv#L474) · explicit_claim_identifier · original status at linked ledger row
- [verification/v282_e8_tau_i_unification.py](../../../../verification/v282_e8_tau_i_unification.py#L1) · explicit_script_identifier
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [verification/v394_coxeter_atoms.py](../../../../verification/v394_coxeter_atoms.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v416 (2): the Z[omega] (hex/flavor) trichotomy + ramified prime = own atom *) neis[aa_, bb_] := aa^2 - aa bb + bb^2; checkExact["v416 ARITH.TRICHOTOMY.01 (Z[omega], hex/flavor): 3 RAMIFIES (N(1-omega)=3), 2 INERT (2 mod 3=2, norm 4), 5 INERT (5 mod 3=2, norm 25=g_car^2); the ramified prime of each ring is its atom (Z[i]<->2, Z[omega]<->3)", neis[1, -1] == 3 && Mod[2, 3] == 2 && neis[2, 0] == 4 && Mod[5, 3] == 2 && neis[5, 0] == 25]; (* v416 (3): the three facets ramify over one atom each (v403) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2489)
- [(* ==== v282: E8-at-tau=i unification, chi_E8(i)=12 (QGAMB.UNIFY.01) ==== *) Module[{jf, jorder4, chiI}, jf[x_] := 256 (x^2 - x + 1)^3/(x^2 (x - 1)^2); jorder4 = jf[2]; (* cross-ratio 2 => j = 1728 = the tau=i CM point *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2170)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)

## 2026-06-24 (The five TOE/QFT closure contracts v398– v402 + a ledger rescope)

[documents/changelog/sections/013-source.tex:215-224](../../../../documents/changelog/sections/013-source.tex#L215) · `section:75d473d613aba16a08b8` · subsection

/ \ v398_seam_state_rigidity.py ( SEAM.RIGIDITY.01, Paper A): the Seam State Rigidity Theorem as ONE named target, consolidating the scattered state-invariance reductions ( v177/ v199/ v308/ v309/ v335) and hardening the finite-block evidence to a multi-mode sweep. \ RP-definability hinge (OS canonical transfer [formula in source] from RP [formula in source] reflection alone, v54, quasi-free v155, no [formula in sour

Explicit source references:

- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v386_grav_amplitude.py](../../../../verification/v386_grav_amplitude.py#L1) · explicit_script_identifier
- [verification/v274_scale_overdetermination.py](../../../../verification/v274_scale_overdetermination.py#L1) · explicit_script_identifier
- [METROLOGY.CLOSURE.01](../../../../verification/status_ledger.csv#L471) · explicit_claim_identifier · original status at linked ledger row
- [verification/v309_modular_bedrock.py](../../../../verification/v309_modular_bedrock.py#L1) · explicit_script_identifier
- [verification/v36_spectral_action_g2.py](../../../../verification/v36_spectral_action_g2.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v384_residual_certification.py](../../../../verification/v384_residual_certification.py#L1) · explicit_script_identifier
- [verification/v399_gravity_complete.py](../../../../verification/v399_gravity_complete.py#L1) · explicit_file_citation
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [GRAV.NONLINEAR.01](../../../../verification/status_ledger.csv#L75) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.RIGIDITY.01](../../../../verification/status_ledger.csv#L468) · explicit_claim_identifier · original status at linked ledger row
- [verification/v398_seam_state_rigidity.py](../../../../verification/v398_seam_state_rigidity.py#L1) · explicit_script_identifier
- [verification/v402_ftransfer_suite.py](../../../../verification/v402_ftransfer_suite.py#L1) · explicit_file_citation
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v199_seam_state_invariance.py](../../../../verification/v199_seam_state_invariance.py#L1) · explicit_script_identifier
- [GRAV.NONLOCAL.01](../../../../verification/status_ledger.csv#L470) · explicit_claim_identifier · original status at linked ledger row
- [verification/v335_seam_equiv_unify.py](../../../../verification/v335_seam_equiv_unify.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_script_identifier
- [verification/v364_vgeo_sharpen.py](../../../../verification/v364_vgeo_sharpen.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v253_kappa_scalaron_ps.py](../../../../verification/v253_kappa_scalaron_ps.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [GATE.METRIC.01](../../../../verification/status_ledger.csv#L55) · explicit_claim_identifier · original status at linked ledger row
- [verification/v177_seam_marking_kernel.py](../../../../verification/v177_seam_marking_kernel.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [FTRANSFER.SUITE.01](../../../../verification/status_ledger.csv#L472) · explicit_claim_identifier · original status at linked ledger row
- [verification/v401_metrology_closure.py](../../../../verification/v401_metrology_closure.py#L1) · explicit_file_citation
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [GRAVITY.COMPLETE.01](../../../../verification/status_ledger.csv#L469) · explicit_claim_identifier · original status at linked ledger row
- [verification/v308_seam_equiv_chain.py](../../../../verification/v308_seam_equiv_chain.py#L1) · explicit_script_identifier
- [verification/v400_grav_nonlocal_action.py](../../../../verification/v400_grav_nonlocal_action.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [(* ---- (v24) quark ratio closure ---- *) checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117]; checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47]; checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26]; check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3]; check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2]; (* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L105)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [(* v475 (iii): the Lorentzian timelike positivity witness *) gL = DiagonalMatrix[{-1, 1, 1, 1}]; mM = Outer[Times, {vv, 0, 0, 0}, {vv, 0, 0, 0}]; evT = Sort[Eigenvalues[(gL + aal mM) . Inverse[gL]]]; evS = Sort[Eigenvalues[(gL + aal Outer[Times, {0, vv, 0, 0}, {0, vv, 0, 0}]) . Inverse[gL]]]; checkExact["v475 GRAV.ENTROPIC.SCALARON.01 (iii): the Lorentzian-positivity witness -- on Minkowski a TIMELIKE gradient gives G g^-1 eigenvalues {1 - alpha v^2, 1, 1, 1} (nonpositive for v^2 >= 1/alpha, ln undefined) while a SPACELIKE gradient gives {1 + alpha v^2, 1, 1, 1} (positive for all v) -- the v473 caveat exhibited, the OS route sturdier", Sort[evT] == Sort[{1 - aal vv^2, 1, 1, 1}] && Sort[evS] == Sort[{1 + aal vv^2, 1, 1, 1}]]; ]; (* ==== v477 round: the scale-flow representation of the entropic action -- the exact content: the Frullani identity Integrate[(e^{-a t}-e^{-t})/t] = -Log[a], the moment dictionary (flat weight = unit moments = the v475 raw coefficients 3 b R + (17/24) b^2 R^2), the ONE moment condition mu2/mu1^2 = (72/17)(8 pi)^9 with the exact closure (4608 pi^2/17)/((72/17)(8 pi)^9) = c3^7, and the v36 consistency f0 = 6 (4 pi)^2/c3^7 <=> M^2 = c3^7 Mbar^2; mirrors v477 (the chi-form quadrature is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3052)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* v477 (i): Frullani + the moment dictionary at flat weight *) frul = Integrate[(Exp[-aa tt] - Exp[-tt])/tt, {tt, 0, Infinity}, Assumptions -> aa > 0]; eig = Join[{1}, Table[1/4, 4], Table[1/6, 6]]; tr = Total[Exp[-tt (1 - bb # RR)] & /@ eig] - 11 Exp[-tt]; serR = Normal[Series[tr, {RR, 0, 2}]]; mu1f = Integrate[Coefficient[serR, RR, 1]/tt, {tt, 0, Infinity}]; mu2f = Integrate[Coefficient[serR, RR, 2]/tt, {tt, 0, Infinity}]; checkExact["v477 GRAV.ENTROPIC.SCALEFLOW.01 (i): the Frullani/scale-flow identity -Log[a] = Integrate[(e^{-a t}-e^{-t})/t] (symbolic) and the moment dictionary -- at the FLAT weight the maximally-symmetric relative trace integrates to exactly the v475 raw coefficients 3 b R + (17/24) b^2 R^2 (unit moments mu1 = mu2 = 1): the raw entropic action is the unit-moment point of a scale-measure family", frul == -Log[aa] && Simplify[mu1f - 3 bb] == 0 && Simplify[mu2f - (17/24) bb^2] == 0]; (* v477 (ii): the one moment condition + closure + v36 consistency *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3071)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ---- (v199) QGEO.STATE.01: [rho,H]=0 <=> H is mu4-character-block-diagonal ---- *) Module[{nn, rho, idx, Hbd, Hoff, classOf}, nn = Range[-6, 6]; rho = DiagonalMatrix[I^nn]; (* carrier clock, order 4 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1648)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean#L1)

## 2026-06-24 ( [formula in source] leading term from icosahedral combinatorics: v396)

[documents/changelog/sections/013-source.tex:225-229](../../../../documents/changelog/sections/013-source.tex#L225) · `section:7ef5c3edcea8d045b5b2` · subsection

/ \ v396_phi0_icosahedral.py ( HYP.PHI0.01): the tree-level seed [formula in source] is exactly [formula in source] on the icosahedral hypergraph ( [formula in source] triangular hyperedges, [formula in source] , [formula in source] ); [formula in source] (the same survival ratio as v327). \ Gauss–Bonnet consistent with [formula in source] ( v216/ v342). \ honest negative: the puncture [formula in source] is still an

Explicit source references:

- [verification/v396_phi0_icosahedral.py](../../../../verification/v396_phi0_icosahedral.py#L1) · explicit_script_identifier
- [verification/v342_em_ward_heatkernel.py](../../../../verification/v342_em_ward_heatkernel.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [HYP.PHI0.01](../../../../verification/status_ledger.csv#L463) · explicit_claim_identifier · original status at linked ledger row
- [verification/v327_hypergraph_rewrite.py](../../../../verification/v327_hypergraph_rewrite.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v342 EM.WARD.02: the heat-kernel origin of the F_U(1) terms ==== *) Module[{c3v, ointK, c3gb, gilkey, q2}, c3v = 1/(8 Pi); (* c3 = boundary Gauss-Bonnet coefficient: oint_{S^2} K = 2 pi chi = 4 pi (chi=2), c3 = 1/(|Z2| oint K) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2259)
- [(* ==== v325/v327: the keystone pillowcase orbifold + the cusp-weight rewrite (exact) ==== *) Module[{chiOrb, M, evs, edges, cAff, x, p23}, (* v325 QGEO.KEYSTONE.01: the flat pillowcase orbifold S^2(2,2,2,2) has chi_orb = 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2220)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)

## 2026-06-24 (Coupled hypergraph rewrite: v395 unifies carrier [formula in source] family in one local rule)

[documents/changelog/sections/013-source.tex:230-234](../../../../documents/changelog/sections/013-source.tex#L230) · `section:ccaa58843679b0b5ee13` · subsection

\ v395_hypergraph_coupled.py ( HYP.COUPLED.01): one coupled local rewrite on a [formula in source] labelled grid (affine- [formula in source] nodes [formula in source] family channels) unifies v299 (carrier growth), v327 (branching rule [formula in source] ) and v324 (fiber product). Micro-step [formula in source] network lazy diffusion on each cusp column [formula in source] [formula in source] on each node's family

Explicit source references:

- [verification/v395_hypergraph_coupled.py](../../../../verification/v395_hypergraph_coupled.py#L1) · explicit_script_identifier
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [verification/v324_hypergraph_fiber.py](../../../../verification/v324_hypergraph_fiber.py#L1) · explicit_script_identifier
- [verification/v327_hypergraph_rewrite.py](../../../../verification/v327_hypergraph_rewrite.py#L1) · explicit_script_identifier
- [verification/v299_hypergraph_0d_autonomous.py](../../../../verification/v299_hypergraph_0d_autonomous.py#L1) · explicit_script_identifier
- [HYP.COUPLED.01](../../../../verification/status_ledger.csv#L462) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [(* ==== v325/v327: the keystone pillowcase orbifold + the cusp-weight rewrite (exact) ==== *) Module[{chiOrb, M, evs, edges, cAff, x, p23}, (* v325 QGEO.KEYSTONE.01: the flat pillowcase orbifold S^2(2,2,2,2) has chi_orb = 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2220)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)

## 2026-06-24 (A falsifiable clock probe of the frontier: v397 how external is the ``external physics''?)

[documents/changelog/sections/013-source.tex:235-248](../../../../documents/changelog/sections/013-source.tex#L235) · `section:cb09371605fac20095ba` · subsection

v397 ( FR.CLOCK.PROBE.01) — do the ``external'' frontier scheme-numbers land on the [formula in source] clock? A falsifiable, anti-numerology probe (strict No-Free-Pattern, v100: ``on the clock'' means an exact match, not a wide-band fit). \ the [formula in source] decuple [formula in source] is ON the clock ( v212); \ the Koide rate [formula in source] is ON the clock ( v303); \ the axion spine angle [formula in sou

Explicit source references:

- [verification/v373_ftransfer_relic.py](../../../../verification/v373_ftransfer_relic.py#L1) · explicit_script_identifier
- [verification/v374_ftransfer_qcd.py](../../../../verification/v374_ftransfer_qcd.py#L1) · explicit_script_identifier
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier
- [verification/v397_external_clock_probe.py](../../../../verification/v397_external_clock_probe.py#L1) · explicit_script_identifier
- [verification/v211_axion_spine_angle.py](../../../../verification/v211_axion_spine_angle.py#L1) · explicit_script_identifier
- [FR.CLOCK.PROBE.01](../../../../verification/status_ledger.csv#L467) · explicit_claim_identifier · original status at linked ledger row
- [verification/v100_numerology_null_mc.py](../../../../verification/v100_numerology_null_mc.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v212_leptogenesis_decuple.py](../../../../verification/v212_leptogenesis_decuple.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)

## 2026-06-24 (Correction error-bars: v393 the typed budget as actual first-correction magnitudes)

[documents/changelog/sections/013-source.tex:249-264](../../../../documents/changelog/sections/013-source.tex#L249) · `section:9a49b0a6b8928419303b` · subsection

v393 ( CORRECTIONS.NUMERIC.01) — the typed correction budget ( v388) as actual numbers. The short-term, testable harvest of v388: instead of merely typing each prediction's correction, this gives the magnitude, so a parameter-free central value can be quoted as ``value [formula in source] computed first correction''. \ FIXED-POINT band (the [formula in source] -derived [formula in source] ) [formula in source] the ex

Explicit source references:

- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v388_corrections_budget.py](../../../../verification/v388_corrections_budget.py#L1) · explicit_script_identifier
- [verification/v337_decoupling_theorem.py](../../../../verification/v337_decoupling_theorem.py#L1) · explicit_script_identifier
- [CORRECTIONS.NUMERIC.01](../../../../verification/status_ledger.csv#L460) · explicit_claim_identifier · original status at linked ledger row
- [verification/v393_corrections_numeric.py](../../../../verification/v393_corrections_numeric.py#L1) · explicit_script_identifier
- [verification/v374_ftransfer_qcd.py](../../../../verification/v374_ftransfer_qcd.py#L1) · explicit_script_identifier
- [verification/v212_leptogenesis_decuple.py](../../../../verification/v212_leptogenesis_decuple.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v337 DECOUPLING.THEOREM.01: the ambient back-reaction scale identity ==== *) Module[{ambient}, (* the largest ambient back-reaction scale 2*dim(E8)*c3^2 = 31/(4 pi^2) exactly (c3=1/(8pi)) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2240)

## 2026-06-24 (Attacking the last open lemma: v392 the scaling-limit central charge converges)

[documents/changelog/sections/013-source.tex:265-278](../../../../documents/changelog/sections/013-source.tex#L265) · `section:a553d00a39600c2d24cd` · subsection

v392 ( SEAM.S3.SCALINGLIMIT.01) — an honest attack on SEAM.EQUIV.01's one open lemma (continuum existence, v336). It does not close v336 (the abstract existence is the cited MMST theorem); it strengthens the case with the existence-relevant observable v376 did not test: that the finite-size data converge. \ the Calabrese–Cardy entanglement slope [formula in source] at [formula in source] is a monotone Cauchy-like seq

Explicit source references:

- [verification/v377_seam_s3_e8character.py](../../../../verification/v377_seam_s3_e8character.py#L1) · explicit_script_identifier
- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_script_identifier
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier
- [SEAM.S3.SCALINGLIMIT.01](../../../../verification/status_ledger.csv#L459) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v392_seam_s3_scalinglimit.py](../../../../verification/v392_seam_s3_scalinglimit.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)

## 2026-06-24 (Lean 4: FORM.SPECTRALGAP.01 extended to the finite-dimensional Perron–Frobenius case)

[documents/changelog/sections/013-source.tex:279-294](../../../../documents/changelog/sections/013-source.tex#L279) · `section:48dc2c7b5335aebad935` · subsection

FORM.SPECTRALGAP.01 — the multi-dimensional case, reduced to the scalar core. The Lean module TfptCarrier/SpectralGapAttractor.lean now also proves the finite-dimensional gapped-operator statement ( lake build OK, no sorry): \ component_tendsto (a non-dominant eigencomponent [formula in source] decays, [formula in source] ); \ deviation_tendsto (with the dominant eigenvalue normalised to [formula in source] , the dev

Explicit source references:

- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier
- [TFPT.Carrier.SpectralGapAttractor.flavor_deviation_tendsto](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L164) · explicit_lean_symbol
- [TFPT.Carrier.SpectralGapAttractor.deviation_unique](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L140) · explicit_lean_symbol
- [FORM.SPECTRALGAP.01](../../../../verification/status_ledger.csv#L454) · explicit_claim_identifier · original status at linked ledger row
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1) · explicit_file_citation
- [TFPT.Carrier.SpectralGapAttractor.deviation_tendsto](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L130) · explicit_lean_symbol
- [TFPT.Carrier.SpectralGapAttractor.component_tendsto](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L110) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)
- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)

## 2026-06-24 (Website: an animated ``Universal Gap Lab'' visualising v383– v391)

[documents/changelog/sections/013-source.tex:295-307](../../../../documents/changelog/sections/013-source.tex#L295) · `section:6b87e1b142e887eedca7` · subsection

Website — the UniversalGapLab animation on /verification. A new client component (Framer Motion, no new dependency) with three linked, module-grounded views: (A) every sector as the gap contraction [formula in source] racing to its attractor at [formula in source] (seam-gapped, v303/ v387/ v388) or the golden [formula in source] ( v312), with a gapless [formula in source] track that never forgets its start (the Lean 

Explicit source references:

- [verification/v386_grav_amplitude.py](../../../../verification/v386_grav_amplitude.py#L1) · explicit_script_identifier
- [verification/v387_corrections_gap.py](../../../../verification/v387_corrections_gap.py#L1) · explicit_script_identifier
- [verification/v391_alpha_quillen_progress.py](../../../../verification/v391_alpha_quillen_progress.py#L1) · explicit_script_identifier
- [FORM.SPECTRALGAP.01](../../../../verification/status_ledger.csv#L454) · explicit_claim_identifier · original status at linked ledger row
- [verification/v384_residual_certification.py](../../../../verification/v384_residual_certification.py#L1) · explicit_script_identifier
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier
- [verification/v388_corrections_budget.py](../../../../verification/v388_corrections_budget.py#L1) · explicit_script_identifier
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [verification/v389_grav_loop_finiteness.py](../../../../verification/v389_grav_loop_finiteness.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)

## 2026-06-24 (Honest attempt at an external target: v391 reduces it, not a closure)

[documents/changelog/sections/013-source.tex:308-323](../../../../documents/changelog/sections/013-source.tex#L308) · `section:7486a840eb74d5da4e47` · subsection

v391 ( ALPHA.QUILLEN.PROGRESS.01) — an honest attempt at the external target ALPHA.QUILLEN.EXACT.01 ( v382, door 5). It REDUCES the open step to a sharper named sub-target via a solvable model but does not close it: ALPHA.QUILLEN.EXACT.01 stays \ (external math, type A, v384). \ a solvable model [formula in source] on a circle of circumference [formula in source] equals [formula in source] , whose [formula in source]

Explicit source references:

- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v384_residual_certification.py](../../../../verification/v384_residual_certification.py#L1) · explicit_script_identifier
- [verification/v382_alpha_quillen_exact.py](../../../../verification/v382_alpha_quillen_exact.py#L1) · explicit_script_identifier
- [verification/v391_alpha_quillen_progress.py](../../../../verification/v391_alpha_quillen_progress.py#L1) · explicit_script_identifier
- [ALPHA.QUILLEN.PROGRESS.01](../../../../verification/status_ledger.csv#L455) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## 2026-06-24 (Lean 4: FORM.SPECTRALGAP.01 formalises the scalar core of the universal spectral-gap principle)

[documents/changelog/sections/013-source.tex:324-339](../../../../documents/changelog/sections/013-source.tex#L324) · `section:fddca2e76a3d11b710e6` · subsection

FORM.SPECTRALGAP.01 — a Lean 4 proof of the gap [formula in source] unique-attractor [formula in source] parameter-free core (door 4). New module TfptCarrier/SpectralGapAttractor.lean ( lake build OK, no sorry, only the three standard kernel axioms), formalising the meta-theorem of v303/ v383/ v387 at the one-dimensional reduction — the affine gap contraction [formula in source] with multiplier [formula in source] . 

Explicit source references:

- [TFPT.Carrier.SpectralGapAttractor.no_gap_no_forget](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L85) · explicit_lean_symbol
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [TFPT.Carrier.SpectralGapAttractor.iter_sub](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L47) · explicit_lean_symbol
- [TFPT.Carrier.SpectralGapAttractor.starts_agree](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L74) · explicit_lean_symbol
- [FORM.SPECTRALGAP.01](../../../../verification/status_ledger.csv#L454) · explicit_claim_identifier · original status at linked ledger row
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1) · explicit_file_citation
- [verification/v387_corrections_gap.py](../../../../verification/v387_corrections_gap.py#L1) · explicit_script_identifier
- [TFPT.Carrier.SpectralGapAttractor.iter_tendsto](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L59) · explicit_lean_symbol
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)

## 2026-06-24 (Completing the Coxeter clock: v390 the prime-2 (Gaussian / [formula in source] -seam) facet of [formula in source] )

[documents/changelog/sections/013-source.tex:340-355](../../../../documents/changelog/sections/013-source.tex#L340) · `section:f1054498b80cd7df6676` · subsection

v390 ( COXETER.PRIME2.01) — the prime-2 facet of the order-30 Coxeter clock. v383/ v387 named two number-field facets of the clock [formula in source] — the golden [formula in source] (prime-5, carrier) and [formula in source] (prime-3, family). This names the prime-2 facet and identifies it with structure already in the theory: the Gaussian field [formula in source] , i.e.\ the CM point [formula in source] and the o

Explicit source references:

- [verification/v387_corrections_gap.py](../../../../verification/v387_corrections_gap.py#L1) · explicit_script_identifier
- [verification/v390_prime2_facet.py](../../../../verification/v390_prime2_facet.py#L1) · explicit_script_identifier
- [verification/v288_full_l2_subprincipal_z4.py](../../../../verification/v288_full_l2_subprincipal_z4.py#L1) · explicit_script_identifier
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [verification/v333_cm_selection.py](../../../../verification/v333_cm_selection.py#L1) · explicit_script_identifier
- [verification/v282_e8_tau_i_unification.py](../../../../verification/v282_e8_tau_i_unification.py#L1) · explicit_script_identifier
- [COXETER.PRIME2.01](../../../../verification/status_ledger.csv#L453) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ==== v282: E8-at-tau=i unification, chi_E8(i)=12 (QGAMB.UNIFY.01) ==== *) Module[{jf, jorder4, chiI}, jf[x_] := 256 (x^2 - x + 1)^3/(x^2 (x - 1)^2); jorder4 = jf[2]; (* cross-ratio 2 => j = 1728 = the tau=i CM point *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2170)

## 2026-06-24 (Graviton loop finiteness: v389 the entire form factor is UV-finite at the loop level by power counting)

[documents/changelog/sections/013-source.tex:356-370](../../../../documents/changelog/sections/013-source.tex#L356) · `section:a64d54bbcb8a16651802` · subsection

v389 ( GRAV.LOOP.FINITE.01) — the entire-form-factor graviton is UV-finite at the loop level. The honest next step past v386 (which established the tree amplitude), extending v304/ v370/ v380/ v386 from the propagator to the superficial degree of divergence of loop graphs. This is the standard infinite-derivative / nonlocal-gravity finiteness statement (Tomboulis; Biswas–Mazumdar–Siegel; Modesto), not a full proof of

Explicit source references:

- [verification/v253_kappa_scalaron_ps.py](../../../../verification/v253_kappa_scalaron_ps.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v389_grav_loop_finiteness.py](../../../../verification/v389_grav_loop_finiteness.py#L1) · explicit_script_identifier
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [verification/v386_grav_amplitude.py](../../../../verification/v386_grav_amplitude.py#L1) · explicit_script_identifier
- [GRAV.LOOP.FINITE.01](../../../../verification/status_ledger.csv#L452) · explicit_claim_identifier · original status at linked ledger row
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)

## 2026-06-24 (Typed correction budget: v388 the gap correction is keyed to the mechanism class, not a uniform band)

[documents/changelog/sections/014-source.tex:1-19](../../../../documents/changelog/sections/014-source.tex#L1) · `section:5b0172590490b241cb77` · subsection

v388 ( CORRECTIONS.BUDGET.01) — the gap-driven correction ( v387) is a typed budget. A machine-checked answer to ``does the [formula in source] correction apply to all predictions?'' — the answer is no, and for one whole class a band would be wrong. Because the size is the distance from a gapped operator's leading eigenvector, it is defined only where a subleading [formula in source] exists, so the prediction surface

Explicit source references:

- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier
- [verification/v337_decoupling_theorem.py](../../../../verification/v337_decoupling_theorem.py#L1) · explicit_script_identifier
- [verification/v388_corrections_budget.py](../../../../verification/v388_corrections_budget.py#L1) · explicit_script_identifier
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [verification/v384_residual_certification.py](../../../../verification/v384_residual_certification.py#L1) · explicit_script_identifier
- [CORRECTIONS.BUDGET.01](../../../../verification/status_ledger.csv#L451) · explicit_claim_identifier · original status at linked ledger row
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v387_corrections_gap.py](../../../../verification/v387_corrections_gap.py#L1) · explicit_script_identifier
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v337 DECOUPLING.THEOREM.01: the ambient back-reaction scale identity ==== *) Module[{ambient}, (* the largest ambient back-reaction scale 2*dim(E8)*c3^2 = 31/(4 pi^2) exactly (c3=1/(8pi)) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2240)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)

## 2026-06-24 (Harvesting the QFT/gravity machinery: v385 the UV-branch kill-test surface, v386 the graviton-exchange amplitude, v387 the gap-driven correction calculus)

[documents/changelog/sections/014-source.tex:20-48](../../../../documents/changelog/sections/014-source.tex#L20) · `section:633620b74c9f05d23e78` · subsection

v385 ( UVBRANCH.KILLTEST.01) — the carrier-Pati–Salam UV branch on the all-order footing. A consolidation that ties the all-order EG/BRST closure ( v381) to the optional UV branch and computes the one genuinely new thing: the proton-decay safety hierarchy. \ the carrier content is the SM with no new states, so the SM-non-unification ( v246) is now all-order-robust; \ the plain-SM 4D-GUT stays killed ( [formula in sou

Explicit source references:

- [verification/v253_kappa_scalaron_ps.py](../../../../verification/v253_kappa_scalaron_ps.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [CORRECTIONS.GAP.01](../../../../verification/status_ledger.csv#L450) · explicit_claim_identifier · original status at linked ledger row
- [verification/v386_grav_amplitude.py](../../../../verification/v386_grav_amplitude.py#L1) · explicit_script_identifier
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v265_qft4d_fork_freeze.py](../../../../verification/v265_qft4d_fork_freeze.py#L1) · explicit_script_identifier
- [verification/v385_uvbranch_killtest.py](../../../../verification/v385_uvbranch_killtest.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v387_corrections_gap.py](../../../../verification/v387_corrections_gap.py#L1) · explicit_script_identifier
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [UVBRANCH.KILLTEST.01](../../../../verification/status_ledger.csv#L448) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.AMPLITUDE.01](../../../../verification/status_ledger.csv#L449) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)

## 2026-06-23 (Bird's-eye synthesis: two new structural patterns — v383 the universal spectral-gap principle and v384 the residual is certification, not construction)

[documents/changelog/sections/014-source.tex:49-77](../../../../documents/changelog/sections/014-source.tex#L49) · `section:8b1a1c6a205860e21edc` · subsection

v383 ( DYNAMICS.UNIVERSAL.01) — the universal spectral-gap / Perron–Frobenius principle. A fresh bird's-eye pass found that every TFPT sector is the same structural object: a gapped operator with a unique leading attractor (the physics) and a spectral gap (the reason there is no free parameter). v303 named this only for [formula in source] ; this module extends it to the sectors made parameter-free after it. \ three 

Explicit source references:

- [verification/v333_cm_selection.py](../../../../verification/v333_cm_selection.py#L1) · explicit_script_identifier
- [verification/v374_ftransfer_qcd.py](../../../../verification/v374_ftransfer_qcd.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v364_vgeo_sharpen.py](../../../../verification/v364_vgeo_sharpen.py#L1) · explicit_script_identifier
- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [RESIDUAL.CERTIFICATION.01](../../../../verification/status_ledger.csv#L447) · explicit_claim_identifier · original status at linked ledger row
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/v384_residual_certification.py](../../../../verification/v384_residual_certification.py#L1) · explicit_script_identifier
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v365_qg_oneloop_saddle.py](../../../../verification/v365_qg_oneloop_saddle.py#L1) · explicit_script_identifier
- [verification/v382_alpha_quillen_exact.py](../../../../verification/v382_alpha_quillen_exact.py#L1) · explicit_script_identifier
- [verification/v157_rigid_fixed_point.py](../../../../verification/v157_rigid_fixed_point.py#L1) · explicit_script_identifier
- [DYNAMICS.UNIVERSAL.01](../../../../verification/status_ledger.csv#L446) · explicit_claim_identifier · original status at linked ledger row
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier
- [verification/v337_decoupling_theorem.py](../../../../verification/v337_decoupling_theorem.py#L1) · explicit_script_identifier
- [verification/v158_fixed_point_stable.py](../../../../verification/v158_fixed_point_stable.py#L1) · explicit_script_identifier
- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v313_golden_atoms_spectral.py](../../../../verification/v313_golden_atoms_spectral.py#L1) · explicit_script_identifier
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier
- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_script_identifier
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ==== v337 DECOUPLING.THEOREM.01: the ambient back-reaction scale identity ==== *) Module[{ambient}, (* the largest ambient back-reaction scale 2*dim(E8)*c3^2 = 31/(4 pi^2) exactly (c3=1/(8pi)) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2240)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)
- [(* ---- (v157) freeness as the rigid boundary fixed point ---- *) Module[{symbolHomog, c3}, symbolHomog = Simplify[Abs[lam kk] - lam Abs[kk], (lam | kk) \[Element] Reals && lam > 0]; c3 = 1/(2*2 Pi*2); (* 1/(|Z2| * 2pi * chi(S^2)) , chi=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1411)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [(* ---- (v158) free chiral c=8 fixed point is stable ---- *) Module[{hpsi, hcur, hquart, bosonic, relevant}, hpsi = 1/2; hcur = 2 hpsi; hquart = 4 hpsi; bosonic = {1, 2, 3}; (* integer-h bosonic chiral ops *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1421)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)

## 2026-06-23 (External-review closure: the two genuine residual targets named — v381 the all-order Epstein–Glaser/BRST contract for [formula in source] , and v382 the Quillen determinant-line variation as a tracked target)

[documents/changelog/sections/014-source.tex:78-106](../../../../documents/changelog/sections/014-source.tex#L78) · `section:2a73aae2d89b3c427077` · subsection

v381 ( QFT4D.EG.ALLORDER.01) — the all-order 4D perturbative-QFT closing statement. A mathematical-physics review of the QFT/TOE layers identified exactly one genuinely new, buildable item: the all-order Epstein–Glaser/BRST contract for the perturbative 4D S-matrix [formula in source] (the previous documents had the [formula in source] skeleton and one-loop, v269/ v271/ v273/ v278, but no named all-order claim). This

Explicit source references:

- [verification/v273_eg_gauge_running.py](../../../../verification/v273_eg_gauge_running.py#L1) · explicit_script_identifier
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_script_identifier
- [verification/v278_lsz_bridge_unitarity.py](../../../../verification/v278_lsz_bridge_unitarity.py#L1) · explicit_script_identifier
- [verification/v271_eg_oneloop_quartic.py](../../../../verification/v271_eg_oneloop_quartic.py#L1) · explicit_script_identifier
- [verification/v382_alpha_quillen_exact.py](../../../../verification/v382_alpha_quillen_exact.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [EM.WARD.01](../../../../verification/status_ledger.csv#L70) · explicit_claim_identifier · original status at linked ledger row
- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [verification/v341_alpha_quillen.py](../../../../verification/v341_alpha_quillen.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v342_em_ward_heatkernel.py](../../../../verification/v342_em_ward_heatkernel.py#L1) · explicit_script_identifier
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [QFT4D.EG.ALLORDER.01](../../../../verification/status_ledger.csv#L444) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ==== v278: S_pert -> S_phys LSZ bridge, one-loop optical theorem (QFT4D.SPERT.04) ==== *) Module[{xs, measureSq, phaseSq}, xs = x /. Solve[s x (1 - x) == m^2, x]; (* x_+ , x_- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2141)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v341 ALPHA.QUILLEN.01: the seam-form discriminant identities ==== *) Module[{c3v, phib}, c3v = 1/(8 Pi); phib = 1/(6 Pi); (* phi_base = (4/3) c3 carries q(A3): c3/phi_base = 3/4; with -5/4 = -q(D5) the F_U(1) seam response carries BOTH glue forms, q(D5)+q(A3)=2 = E8 root norm; counterterm coefficient (4/5)M = 8 b1 = 8*(41/10) with b1 the U(1)_Y one-loop beta (rank E8 = 8) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2248)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [(* ==== v342 EM.WARD.02: the heat-kernel origin of the F_U(1) terms ==== *) Module[{c3v, ointK, c3gb, gilkey, q2}, c3v = 1/(8 Pi); (* c3 = boundary Gauss-Bonnet coefficient: oint_{S^2} K = 2 pi chi = 4 pi (chi=2), c3 = 1/(|Z2| oint K) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2259)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## 2026-06-23 (Track 2 of the forward plan v2 — the AMBIENT REDUNDANCY statement ( v369): the holographic route to Gravity-complete that sidesteps building the general Euclidean QG measure)

[documents/changelog/sections/014-source.tex:107-125](../../../../documents/changelog/sections/014-source.tex#L107) · `section:acb731fecb30c7953915` · subsection

v369 ( QGAMB.REDUNDANCY.01) — Track 2 (forward plan v2). Instead of constructing the non-perturbative ambient measure (the conformal-factor swamp, v332/ v334), assemble the established discriminators that prove the ambient sector carries no physical degrees of freedom relative to the holomorphic boundary algebra, so the QG measure (gate C7/ QG.AMB.01) is a non-fundamental certification object (like a coordinate choic

Explicit source references:

- [verification/v329_os_gap_reduction.py](../../../../verification/v329_os_gap_reduction.py#L1) · explicit_script_identifier
- [verification/v334_conformal_resolution.py](../../../../verification/v334_conformal_resolution.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v337_decoupling_theorem.py](../../../../verification/v337_decoupling_theorem.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v258_dirac_covariance_induction.py](../../../../verification/v258_dirac_covariance_induction.py#L1) · explicit_script_identifier
- [verification/v332_qgamb_metric_sector.py](../../../../verification/v332_qgamb_metric_sector.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [verification/v366_mmst_seam_collar.py](../../../../verification/v366_mmst_seam_collar.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [QGAMB.REDUNDANCY.01](../../../../verification/status_ledger.csv#L94) · explicit_claim_identifier · original status at linked ledger row
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/v309_modular_bedrock.py](../../../../verification/v309_modular_bedrock.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ==== v337 DECOUPLING.THEOREM.01: the ambient back-reaction scale identity ==== *) Module[{ambient}, (* the largest ambient back-reaction scale 2*dim(E8)*c3^2 = 31/(4 pi^2) exactly (c3=1/(8pi)) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2240)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)

## 2026-06-23 (Status propagation: the v365– v380 [formula in source] FORM.SEAM.MMST.01 status carried into the remaining papers, the README and the Zenodo description)

[documents/changelog/sections/014-source.tex:126-139](../../../../documents/changelog/sections/014-source.tex#L126) · `section:43e53494baf54171d70d` · subsection

Deep-sync of the post-S3 status. The canonical surfaces ( tfpt_status, introduction) were already current; this pass propagated the same honest wording into origin_theory, tfpt_1– tfpt_5, tfpt_research_contracts, the root README.md, the Zenodo description and website/lib/papers.ts: SEAM.EQUIV.01 is closed modulo a cited theorem (lattice v367/ v368 [formula in source] the [formula in source] stack v376– v379 [formula 

Explicit source references:

- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_script_identifier
- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier
- [verification/v365_qg_oneloop_saddle.py](../../../../verification/v365_qg_oneloop_saddle.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [README.md](../../../../README.md#L1) · explicit_file_citation
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [verification/v374_ftransfer_qcd.py](../../../../verification/v374_ftransfer_qcd.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)

## 2026-06-23 ( v380 — the KMS Entire Hessian: the Stelle ghost is EXACTLY the Seeley–DeWitt truncation, and resummation pushes it to infinity)

[documents/changelog/sections/014-source.tex:140-153](../../../../documents/changelog/sections/014-source.tex#L140) · `section:6db706756a796987fc17` · subsection

v380 ( GRAV.KMS.HESSIAN.01). Upgrades v304/ v370 from the assumption ``the resummed graviton form factor is entire'' to a derived statement. \ the seam KMS cutoff [formula in source] ( v259) gives the dressed spin-2 propagator [formula in source] with [formula in source] entire and nowhere zero (only the [formula in source] pole). \ each finite Seeley–DeWitt truncation is a Taylor partial sum of [formula in source] a

Explicit source references:

- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [GRAV.KMS.HESSIAN.01](../../../../verification/status_ledger.csv#L93) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)

## 2026-06-23 (Lean: the S3 continuum leg formalised as ``closed modulo a cited theorem'' — FORM.SEAM.MMST.01)

[documents/changelog/sections/014-source.tex:154-167](../../../../documents/changelog/sections/014-source.tex#L154) · `section:ded29520f6b18df4c062` · subsection

FORM.SEAM.MMST.01 — Lean 4 formalisation. The S3 continuum leg is now machine-formalised in a new module ( SeamScalingLimit.lean), lake build OK and \#print axioms clean, in the audit-contract style of SeamEquivChain.lean. The MMST applicability hypotheses for the seam collar are provable by kernel decide (no axioms): [formula in source] , [formula in source] , the range [formula in source] , [formula in source] , an

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1) · explicit_file_citation
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## 2026-06-23 (S3 closure stack — the target of the seam scaling limit pinned at EVERY computable level: central charge [formula in source] from the lattice ( v376), the [formula in source] character ( v377), the genus-1 torus count [formula in source] ( v378), and reflection positivity ( v379); only the abstract continuum existence (cited MMST) stays external)

[documents/changelog/sections/014-source.tex:168-192](../../../../documents/changelog/sections/014-source.tex#L168) · `section:b450ecffaba882770fc8` · subsection

v376 ( SEAM.S3.CENTRALCHARGE.01). The Calabrese–Cardy finite-size entanglement-entropy scaling of the critical free-fermion content gives [formula in source] per complex mode (Peschel correlation-matrix EE; the [formula in source] sizes avoid the half-filling zero-mode), so the 16-Majorana ( [formula in source] complex) collar has [formula in source] , chiral ( [formula in source] , v367/ v368). Numerical [formula in

Explicit source references:

- [SEAM.S3.E8CHARACTER.01](../../../../verification/status_ledger.csv#L89) · explicit_claim_identifier · original status at linked ledger row
- [verification/v377_seam_s3_e8character.py](../../../../verification/v377_seam_s3_e8character.py#L1) · explicit_script_identifier
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_script_identifier
- [SEAM.S3.MODULAR.01](../../../../verification/status_ledger.csv#L90) · explicit_claim_identifier · original status at linked ledger row
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [SEAM.S3.CENTRALCHARGE.01](../../../../verification/status_ledger.csv#L88) · explicit_claim_identifier · original status at linked ledger row
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_script_identifier
- [SEAM.S3.RP.01](../../../../verification/status_ledger.csv#L91) · explicit_claim_identifier · original status at linked ledger row
- [verification/v344_detk_synthesis.py](../../../../verification/v344_detk_synthesis.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v344 SEAM.DETK.01: the ADE |det Cartan| = |H_1(link)| sequence, only E8 -> 1 ==== *) Module[{cartanA, cartanD, E8, detADE}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}]; cartanD[n_] := Module[{M = Normal[cartanA[n]]}, M[[n, n - 1]] = M[[n - 1, n]] = 0; M[[n, n - 2]] = M[[n - 2, n]] = -1; M]; E8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; (* |det Cartan| = |H_1(link)| = #(1-dim irreps): A_n->n+1, D_n->4, E6->3, E7->2, E8->1; only E8 -> 1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2271)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)

## 2026-06-23 (Track 4 — the prediction OBSERVATORY: a status-typed CI over the frozen prediction registry that makes the falsifiability surface machine-checkable, with a live data scorecard ( v375))

[documents/changelog/sections/014-source.tex:193-204](../../../../documents/changelog/sections/014-source.tex#L193) · `section:2ad2ac4126620b31f007` · subsection

v375 ( OBSERVATORY.REGISTRY.01). A CI over freeze_file.csv: \ every prediction carries a kill criterion (falsifiability complete, no orphan claims); \ the headline values re-derive from [formula in source] ( [formula in source] , [formula in source] , [formula in source] ); \ a live scorecard records [formula in source] vs the JUNO first run ( [formula in source] , compatible), [formula in source] vs NuFIT 6.0 NO ( [

Explicit source references:

- [verification/freeze_file.csv](../../../../verification/freeze_file.csv#L1) · explicit_file_citation
- [OBSERVATORY.REGISTRY.01](../../../../verification/status_ledger.csv#L87) · explicit_claim_identifier · original status at linked ledger row
- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier

## 2026-06-23 (Track 3 — the [formula in source] functor promoted from contracts to TYPED runnable solvers with kill tests: Koide source [formula in source] pole ( v371), [formula in source] Boltzmann ( v372), axion finite- [formula in source] relic ( v373), [formula in source] uncertainty budget ( v374))

[documents/changelog/sections/014-source.tex:205-223](../../../../documents/changelog/sections/014-source.tex#L205) · `section:2692631f31aef19d9368` · subsection

v371 ( FR.POLE.SOLVE.01). A clean negative: standard QED/EW running cannot be the Koide source [formula in source] pole transfer (it pushes [formula in source] above [formula in source] ; the required [formula in source] is negative while QED's is positive), so the transfer is the non-QED [formula in source] operator / [formula in source] Moebius generator ( v183/ v82). , plain running excluded as the kill. Python (n

Explicit source references:

- [verification/v262_fqcd_mp_me.py](../../../../verification/v262_fqcd_mp_me.py#L1) · explicit_script_identifier
- [verification/v372_ftransfer_boltzmann.py](../../../../verification/v372_ftransfer_boltzmann.py#L1) · explicit_script_identifier
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_script_identifier
- [verification/v373_ftransfer_relic.py](../../../../verification/v373_ftransfer_relic.py#L1) · explicit_script_identifier
- [verification/v374_ftransfer_qcd.py](../../../../verification/v374_ftransfer_qcd.py#L1) · explicit_script_identifier
- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier
- [FR.QCD.BUDGET.01](../../../../verification/status_ledger.csv#L86) · explicit_claim_identifier · original status at linked ledger row
- [FR.BOLTZMANN.SOLVE.01](../../../../verification/status_ledger.csv#L84) · explicit_claim_identifier · original status at linked ledger row
- [FR.RELIC.SOLVE.01](../../../../verification/status_ledger.csv#L85) · explicit_claim_identifier · original status at linked ledger row
- [FR.POLE.SOLVE.01](../../../../verification/status_ledger.csv#L83) · explicit_claim_identifier · original status at linked ledger row
- [verification/v212_leptogenesis_decuple.py](../../../../verification/v212_leptogenesis_decuple.py#L1) · explicit_script_identifier
- [verification/v326_ftransfer_suite.py](../../../../verification/v326_ftransfer_suite.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)
- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)

## 2026-06-23 (Track 1 — the S3 input made CONCRETE: an explicit gapped chiral-Majorana ( [formula in source] ) lattice model with numerical Chern [formula in source] realises the [formula in source] edge ( v367), and a strip shows the chiral edge exists by anomaly inflow ( v368))

[documents/changelog/sections/014-source.tex:224-242](../../../../documents/changelog/sections/014-source.tex#L224) · `section:1a6d16256ec9d6226d97` · subsection

v367 ( SEAM.S3.LATTICE.01) — Track 1. The abstract S3 residual of v356/ v366 (``the collar realised as a genuine lattice chiral free-fermion invertible phase'') is turned into a RUNNABLE model. \ the [formula in source] Bloch model is gapped at [formula in source] with a numerically computed Fukui–Hatsugai–Suzuki Chern number [formula in source] ( [formula in source] trivially at [formula in source] ); \ [formula in 

Explicit source references:

- [SEAM.S3.LATTICE.01](../../../../verification/status_ledger.csv#L81) · explicit_claim_identifier · original status at linked ledger row
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v356_continuum_mmst_applicability.py](../../../../verification/v356_continuum_mmst_applicability.py#L1) · explicit_script_identifier
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v366_mmst_seam_collar.py](../../../../verification/v366_mmst_seam_collar.py#L1) · explicit_script_identifier
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_script_identifier
- [verification/v351_continuum_realisation_sharpened.py](../../../../verification/v351_continuum_realisation_sharpened.py#L1) · explicit_script_identifier
- [SEAM.S3.INFLOW.01](../../../../verification/status_ledger.csv#L82) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ==== v351 SEAM.EQUIV.CONTINUUM.02: the order-4 clock + Coxeter-match pin E8 over SO(16) ==== *) Module[{cE8, cD8}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; checkExact["v351 SEAM.EQUIV.CONTINUUM.02: the c=8 which-net ambiguity (E8 det 1 vs SO(16)=D8 det 4) is RESOLVED by the seam's ORDER-4 mu4 clock -- index-4 extension of D5(+)A3 = E8 (full mu4 condensation 16->4->1), index-2 = SO(16) (partial Z2 16->4); the order (4 not 2) selects E8. The bootstrap agrees: h(E8)=30 max prime 5=g_car, h(D8)=14 max prime 7, so SO(16) fails the Coxeter-match. The residual of SEAM.EQUIV.01 is then PURELY the chiral-edge existence, not which-net", Det[cE8] == 1 && Det[cD8] == 4 && Max[FactorInteger[30][[All,1]]] == 5 && Max[FactorInteger[14][[All,1]]] == 7]; ]; (* ==== v352 TFPT.IRREDUCIBLE.01: both axioms bootstrap-forced; irreducibles = framework + pi ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2334)

## 2026-06-23 (Track 2 — perturbative graviton unitarity sector-by-sector: the Barnes–Rivers spin decomposition localises the Stelle ghost in the spin-2 sector, cured by the entire KMS form factor; the spin-0 mode by the GHP contour ( v370))

[documents/changelog/sections/014-source.tex:243-257](../../../../documents/changelog/sections/014-source.tex#L243) · `section:b08e66805b3affcf9678` · subsection

v370 ( GRAV.SPIN2.UNITARITY.01) — Track 2. Extends v304 (the scalar [formula in source] pole algebra) to the actual tensor spin structure. \ the Barnes–Rivers projectors are complete ( [formula in source] , [formula in source] , [formula in source] sum to [formula in source] ; [formula in source] split [formula in source] ), the EH propagator is [formula in source] , and the Stelle ghost is a spin-2 state. \ the enti

Explicit source references:

- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [GRAV.SPIN2.UNITARITY.01](../../../../verification/status_ledger.csv#L80) · explicit_claim_identifier · original status at linked ledger row
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v332_qgamb_metric_sector.py](../../../../verification/v332_qgamb_metric_sector.py#L1) · explicit_script_identifier
- [verification/v354_e8_reverse_audit.py](../../../../verification/v354_e8_reverse_audit.py#L1) · explicit_script_identifier
- [verification/v355_e8_unmapped_bandwidth.py](../../../../verification/v355_e8_unmapped_bandwidth.py#L1) · explicit_script_identifier
- [verification/v334_conformal_resolution.py](../../../../verification/v334_conformal_resolution.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v354 E8.REVERSE.AUDIT.01: 3 of 8 E8 Casimir degrees are load-bearing, 5 unmapped ==== *) Module[{exps, degs, mapped, unmapped}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; (* E8 exponents *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2352)
- [(* ==== v355 E8.UNMAPPED.BANDWIDTH.01: the unmapped region's forced content is COLLECTIVE ==== *) Module[{exps, degs, totatives}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; degs = exps + 1; (* {2,8,12,14,18,20,24,30} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2362)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [(* v431 (5): clean {0,2} split special to E8 among exceptionals *) cleanSplit[name_] := Module[{ex, hh, dm}, ex = Switch[name, "A4", {1, 2, 3, 4}, "D5", {1, 3, 5, 7, 4}, "E6", {1, 4, 5, 7, 8, 11}, "E7", {1, 5, 7, 9, 11, 13, 17}, "E8", exps, "F4", {1, 5, 7, 11}, "G2", {1, 5}]; hh = Switch[name, "A4", 5, "D5", 8, "E6", 12, "E7", 18, "E8", 30, "F4", 12, "G2", 6]; dm = DeleteDuplicates[Mod[ex + 1, 6]]; Sort[ex] == Select[Range[1, hh - 1], CoprimeQ[#, hh] &] && SubsetQ[{0, 2}, dm] && Mod[hh, 6] == 0]; e8Clean = cleanSplit["E8"]; e67Fail = ! (cleanSplit["E6"] && cleanSplit["E7"] && cleanSplit["D5"]); checkExact["v431 E8.DEGREE.LADDER.01 (v): clean {0,2}-mod-6 split (6|h AND exponents=totatives) holds for E8 but FAILS for E6,E7,D5; F4/G2 share split but not spine+flavor-det content", e8Clean && e67Fail && cleanSplit["F4"] && cleanSplit["G2"]]; (* v431 (6): all five 'unmapped' degrees homed; v355 functorial line upheld [P] *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2693)

## 2026-06-23 (Directions 3 \& 7 — the two hard functional-analysis residuals ADVANCED: the QG measure as one-loop fluctuations around the parameter-free saddle ( v365), and the seam collar verified IN MMST's free-fermion class so the scaling limit is [formula in source] ( v366))

[documents/changelog/sections/014-source.tex:258-280](../../../../documents/changelog/sections/014-source.tex#L258) · `section:4a157afd200102fcaaee` · subsection

v365 ( QGAMB.SADDLE.01) — Direction 3. With the parameter-free saddle ( v358/ v359) the QG measure (gate C7/ QG.AMB.01) organises as a one-loop Gaussian fluctuation determinant. \ the fluctuation stiffness is [formula in source] (no free dial, so the one-loop problem is now well-posed); \ the fluctuation operator is gapped [formula in source] ( v76/ v337) [formula in source] mode-by-mode convergence, finite model log

Explicit source references:

- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v351_continuum_realisation_sharpened.py](../../../../verification/v351_continuum_realisation_sharpened.py#L1) · explicit_script_identifier
- [verification/v334_conformal_resolution.py](../../../../verification/v334_conformal_resolution.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [verification/v356_continuum_mmst_applicability.py](../../../../verification/v356_continuum_mmst_applicability.py#L1) · explicit_script_identifier
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [verification/v297_route_a_literature_stack.py](../../../../verification/v297_route_a_literature_stack.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v337_decoupling_theorem.py](../../../../verification/v337_decoupling_theorem.py#L1) · explicit_script_identifier
- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [verification/v330_qgamb_admissible_measure.py](../../../../verification/v330_qgamb_admissible_measure.py#L1) · explicit_script_identifier
- [QGAMB.SADDLE.01](../../../../verification/status_ledger.csv#L78) · explicit_claim_identifier · original status at linked ledger row
- [verification/v364_vgeo_sharpen.py](../../../../verification/v364_vgeo_sharpen.py#L1) · explicit_script_identifier
- [SEAM.MMST.INCLASS.01](../../../../verification/status_ledger.csv#L79) · explicit_claim_identifier · original status at linked ledger row
- [verification/v366_mmst_seam_collar.py](../../../../verification/v366_mmst_seam_collar.py#L1) · explicit_script_identifier
- [verification/v365_qg_oneloop_saddle.py](../../../../verification/v365_qg_oneloop_saddle.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v351 SEAM.EQUIV.CONTINUUM.02: the order-4 clock + Coxeter-match pin E8 over SO(16) ==== *) Module[{cE8, cD8}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; checkExact["v351 SEAM.EQUIV.CONTINUUM.02: the c=8 which-net ambiguity (E8 det 1 vs SO(16)=D8 det 4) is RESOLVED by the seam's ORDER-4 mu4 clock -- index-4 extension of D5(+)A3 = E8 (full mu4 condensation 16->4->1), index-2 = SO(16) (partial Z2 16->4); the order (4 not 2) selects E8. The bootstrap agrees: h(E8)=30 max prime 5=g_car, h(D8)=14 max prime 7, so SO(16) fails the Coxeter-match. The residual of SEAM.EQUIV.01 is then PURELY the chiral-edge existence, not which-net", Det[cE8] == 1 && Det[cD8] == 4 && Max[FactorInteger[30][[All,1]]] == 5 && Max[FactorInteger[14][[All,1]]] == 7]; ]; (* ==== v352 TFPT.IRREDUCIBLE.01: both axioms bootstrap-forced; irreducibles = framework + pi ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2334)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [(* ==== v337 DECOUPLING.THEOREM.01: the ambient back-reaction scale identity ==== *) Module[{ambient}, (* the largest ambient back-reaction scale 2*dim(E8)*c3^2 = 31/(4 pi^2) exactly (c3=1/(8pi)) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2240)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## 2026-06-23 (Consistency pass: the parameter-free full covariant Einstein equation ( v358/ v359) propagated across ALL stale paper and website surfaces; new v359 keybox; homepage gravity animation)

[documents/changelog/sections/014-source.tex:281-302](../../../../documents/changelog/sections/014-source.tex#L281) · `section:e7b2d5a6deafa57401db` · subsection

Deep-sync of the parameter-free gravity status. A cross-surface audit found several documents and website components still framing gravity as ``exact only in the [formula in source] regime'' or the metric-sector field equation as ``open''. These were reconciled with the canonical post- v358/ v359 status: the local covariant field equation [formula in source] is PARAMETER-FREE (both coefficients fixed); what remains o

Explicit source references:

- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/script_registry.csv](../../../../verification/script_registry.csv#L1) · explicit_file_citation
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)

## 2026-06-23 (Direction 6, [formula in source] sharpened: after the parameter-free gravity, the gravity sector adds NO new dimensionful input either, so [formula in source] is the SINGLE dimensionful input of the complete theory — final tally [formula in source] , ZERO dimensionless dials: v364)

[documents/changelog/sections/014-source.tex:303-316](../../../../documents/changelog/sections/014-source.tex#L303) · `section:761d5a6c7853cbe93148` · subsection

v364 ( VGEO.SHARPEN.01) — Direction 6. The No-Unit Theorem ( v153) already made [formula in source] a forced metrology primitive. \ The SHARPENING after the parameter-free gravity ( v358/ v359/ v361): the Einstein coefficient [formula in source] and the [formula in source] prefactor [formula in source] are dimensionless, so [formula in source] and [formula in source] reduce to [formula in source] times atoms — the gr

Explicit source references:

- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v364_vgeo_sharpen.py](../../../../verification/v364_vgeo_sharpen.py#L1) · explicit_script_identifier
- [verification/v68_seeley_dewitt_residual.py](../../../../verification/v68_seeley_dewitt_residual.py#L1) · explicit_script_identifier
- [VGEO.SHARPEN.01](../../../../verification/status_ledger.csv#L72) · explicit_claim_identifier · original status at linked ledger row
- [verification/v361_grav_backreaction.py](../../../../verification/v361_grav_backreaction.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v67) central theorem structural closure: replica area-law coeff => c3=1/(8pi) ---- *) checkExact["Fursaev-Solodukhin: k=c3/2=1/(16pi); S=4pi k A=2pi c3 A; 2pi c3=1/4 => S=A/4 (BH)", With[{c3 = 1/(8 Pi)}, Simplify[c3/2 - 1/(16 Pi)] == 0 && Simplify[2 Pi c3 - 1/4] == 0 && Simplify[4 Pi (c3/2) - 1/4] == 0]]; checkExact["theorem (inverse): S=A/4 & S=4pi k A & k=c3/2 => c3=1/(8pi) UNIQUE", Module[{ksol = 1/(4 (4 Pi))}, Simplify[ksol - 1/(16 Pi)] == 0 && Simplify[2*ksol - 1/(8 Pi)] == 0]]; (* ---- (v68) Seeley-DeWitt a2 for the carrier; 1/G UV-sensitive => k=c3/2 is a normalization ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L315)

## 2026-06-23 (Direction 5, the matter–gravity backreaction: the carrier's gravitational anomaly is forced [formula in source] , and the matter vacuum-energy backreaction is finite ( [formula in source] the forced [formula in source] from [formula in source] , not [formula in source] ) — the loop closes; no new SM-quantum-number read-out (declined): v361)

[documents/changelog/sections/014-source.tex:317-330](../../../../documents/changelog/sections/014-source.tex#L317) · `section:b0eabbf91a1894618a3d` · subsection

v361 ( GRAV.BACKREACT.01) — Direction 5. With the parameter-free equation ( v359) and the explicit J3 flux ( v358), the backreaction of TFPT's carrier matter is computed. \ the carrier's gravitational anomaly is forced: [formula in source] (the chiral central charge of the [formula in source] -Majorana content). \ the backreaction is FINITE [formula in source] from [formula in source] : the matter vacuum energy throu

Explicit source references:

- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_script_identifier
- [verification/v361_grav_backreaction.py](../../../../verification/v361_grav_backreaction.py#L1) · explicit_script_identifier
- [GRAV.BACKREACT.01](../../../../verification/status_ledger.csv#L73) · explicit_claim_identifier · original status at linked ledger row
- [verification/v355_e8_unmapped_bandwidth.py](../../../../verification/v355_e8_unmapped_bandwidth.py#L1) · explicit_script_identifier
- [verification/v337_decoupling_theorem.py](../../../../verification/v337_decoupling_theorem.py#L1) · explicit_script_identifier
- [verification/v60_lambda_metrology_branch.py](../../../../verification/v60_lambda_metrology_branch.py#L1) · explicit_script_identifier
- [verification/v354_e8_reverse_audit.py](../../../../verification/v354_e8_reverse_audit.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v355 E8.UNMAPPED.BANDWIDTH.01: the unmapped region's forced content is COLLECTIVE ==== *) Module[{exps, degs, totatives}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; degs = exps + 1; (* {2,8,12,14,18,20,24,30} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2362)
- [(* ---- (v60) Lambda branch selection: prefactor 3/(4pi^2), branch mis-scale 64pi^3/3 ---- *) checkExact["delta_top=48 c3^4=3/(256 pi^4); (8pi)^2 delta_top=3/(4 pi^2); 2c3/delta_top=64 pi^3/3 (G_N pinned)", With[{c3 = 1/(8 Pi), dt = 48 (1/(8 Pi))^4}, Simplify[dt - 3/(256 Pi^4)] == 0 && Simplify[(8 Pi)^2 dt - 3/(4 Pi^2)] == 0 && Simplify[2 c3/dt - 64 Pi^3/3] == 0]]; checkExact["action exponents (1,5,10) = K5 counts (5 vertices, C(5,2)=10 edges); Pascal 16=1+5+10", {1, 5, Binomial[5, 2]} == {1, 5, 10} && 1 + 5 + 10 == 16]; (* ---- (v61) boundary-CFT bridge: WZW central charges = atoms, conformal embedding ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L282)
- [(* v431 (5): clean {0,2} split special to E8 among exceptionals *) cleanSplit[name_] := Module[{ex, hh, dm}, ex = Switch[name, "A4", {1, 2, 3, 4}, "D5", {1, 3, 5, 7, 4}, "E6", {1, 4, 5, 7, 8, 11}, "E7", {1, 5, 7, 9, 11, 13, 17}, "E8", exps, "F4", {1, 5, 7, 11}, "G2", {1, 5}]; hh = Switch[name, "A4", 5, "D5", 8, "E6", 12, "E7", 18, "E8", 30, "F4", 12, "G2", 6]; dm = DeleteDuplicates[Mod[ex + 1, 6]]; Sort[ex] == Select[Range[1, hh - 1], CoprimeQ[#, hh] &] && SubsetQ[{0, 2}, dm] && Mod[hh, 6] == 0]; e8Clean = cleanSplit["E8"]; e67Fail = ! (cleanSplit["E6"] && cleanSplit["E7"] && cleanSplit["D5"]); checkExact["v431 E8.DEGREE.LADDER.01 (v): clean {0,2}-mod-6 split (6|h AND exponents=totatives) holds for E8 but FAILS for E6,E7,D5; F4/G2 share split but not spine+flavor-det content", e8Clean && e67Fail && cleanSplit["F4"] && cleanSplit["G2"]]; (* v431 (6): all five 'unmapped' degrees homed; v355 functorial line upheld [P] *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2693)
- [(* ==== v354 E8.REVERSE.AUDIT.01: 3 of 8 E8 Casimir degrees are load-bearing, 5 unmapped ==== *) Module[{exps, degs, mapped, unmapped}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; (* E8 exponents *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2352)
- [(* ==== v337 DECOUPLING.THEOREM.01: the ambient back-reaction scale identity ==== *) Module[{ambient}, (* the largest ambient back-reaction scale 2*dim(E8)*c3^2 = 31/(4 pi^2) exactly (c3=1/(8pi)) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2240)
- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)

## 2026-06-23 (Direction 2, the disciplined result: the gap-induced GR correction is the known [formula in source] scalaron — already falsifiable via [formula in source] ; a new forced near-term deviation does NOT survive the discriminator and is declined: v360)

[documents/changelog/sections/014-source.tex:331-347](../../../../documents/changelog/sections/014-source.tex#L331) · `section:b9e3cb43b2bc303303e6` · subsection

v360 ( GRAV.GAPCORR.01) — Direction 2, run honestly. Does the seam transfer gap [formula in source] yield a NEW, calculable, FORCED deviation from GR (a near-term kill test) beyond the known [formula in source] scalaron? With the v354/ v355 discriminator the answer is no, and this is recorded rather than manufacturing a coefficient. \ the leading higher-curvature term IS the [formula in source] scalaron (spectral-act

Explicit source references:

- [verification/v354_e8_reverse_audit.py](../../../../verification/v354_e8_reverse_audit.py#L1) · explicit_script_identifier
- [verification/v355_e8_unmapped_bandwidth.py](../../../../verification/v355_e8_unmapped_bandwidth.py#L1) · explicit_script_identifier
- [verification/v36_spectral_action_g2.py](../../../../verification/v36_spectral_action_g2.py#L1) · explicit_script_identifier
- [verification/v360_grav_gap_corrections.py](../../../../verification/v360_grav_gap_corrections.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [GRAV.GAPCORR.01](../../../../verification/status_ledger.csv#L74) · explicit_claim_identifier · original status at linked ledger row
- [verification/v28_gravity_fR.py](../../../../verification/v28_gravity_fR.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v431 (5): clean {0,2} split special to E8 among exceptionals *) cleanSplit[name_] := Module[{ex, hh, dm}, ex = Switch[name, "A4", {1, 2, 3, 4}, "D5", {1, 3, 5, 7, 4}, "E6", {1, 4, 5, 7, 8, 11}, "E7", {1, 5, 7, 9, 11, 13, 17}, "E8", exps, "F4", {1, 5, 7, 11}, "G2", {1, 5}]; hh = Switch[name, "A4", 5, "D5", 8, "E6", 12, "E7", 18, "E8", 30, "F4", 12, "G2", 6]; dm = DeleteDuplicates[Mod[ex + 1, 6]]; Sort[ex] == Select[Range[1, hh - 1], CoprimeQ[#, hh] &] && SubsetQ[{0, 2}, dm] && Mod[hh, 6] == 0]; e8Clean = cleanSplit["E8"]; e67Fail = ! (cleanSplit["E6"] && cleanSplit["E7"] && cleanSplit["D5"]); checkExact["v431 E8.DEGREE.LADDER.01 (v): clean {0,2}-mod-6 split (6|h AND exponents=totatives) holds for E8 but FAILS for E6,E7,D5; F4/G2 share split but not spine+flavor-det content", e8Clean && e67Fail && cleanSplit["F4"] && cleanSplit["G2"]]; (* v431 (6): all five 'unmapped' degrees homed; v355 functorial line upheld [P] *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2693)
- [(* ==== v354 E8.REVERSE.AUDIT.01: 3 of 8 E8 Casimir degrees are load-bearing, 5 unmapped ==== *) Module[{exps, degs, mapped, unmapped}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; (* E8 exponents *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2352)
- [(* v475 (iii): the Lorentzian timelike positivity witness *) gL = DiagonalMatrix[{-1, 1, 1, 1}]; mM = Outer[Times, {vv, 0, 0, 0}, {vv, 0, 0, 0}]; evT = Sort[Eigenvalues[(gL + aal mM) . Inverse[gL]]]; evS = Sort[Eigenvalues[(gL + aal Outer[Times, {0, vv, 0, 0}, {0, vv, 0, 0}]) . Inverse[gL]]]; checkExact["v475 GRAV.ENTROPIC.SCALARON.01 (iii): the Lorentzian-positivity witness -- on Minkowski a TIMELIKE gradient gives G g^-1 eigenvalues {1 - alpha v^2, 1, 1, 1} (nonpositive for v^2 >= 1/alpha, ln undefined) while a SPACELIKE gradient gives {1 + alpha v^2, 1, 1, 1} (positive for all v) -- the v473 caveat exhibited, the OS route sturdier", Sort[evT] == Sort[{1 - aal vv^2, 1, 1, 1}] && Sort[evS] == Sort[{1 + aal vv^2, 1, 1, 1}]]; ]; (* ==== v477 round: the scale-flow representation of the entropic action -- the exact content: the Frullani identity Integrate[(e^{-a t}-e^{-t})/t] = -Log[a], the moment dictionary (flat weight = unit moments = the v475 raw coefficients 3 b R + (17/24) b^2 R^2), the ONE moment condition mu2/mu1^2 = (72/17)(8 pi)^9 with the exact closure (4608 pi^2/17)/((72/17)(8 pi)^9) = c3^7, and the v36 consistency f0 = 6 (4 pi)^2/c3^7 <=> M^2 = c3^7 Mbar^2; mirrors v477 (the chi-form quadrature is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3052)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* v477 (i): Frullani + the moment dictionary at flat weight *) frul = Integrate[(Exp[-aa tt] - Exp[-tt])/tt, {tt, 0, Infinity}, Assumptions -> aa > 0]; eig = Join[{1}, Table[1/4, 4], Table[1/6, 6]]; tr = Total[Exp[-tt (1 - bb # RR)] & /@ eig] - 11 Exp[-tt]; serR = Normal[Series[tr, {RR, 0, 2}]]; mu1f = Integrate[Coefficient[serR, RR, 1]/tt, {tt, 0, Infinity}]; mu2f = Integrate[Coefficient[serR, RR, 2]/tt, {tt, 0, Infinity}]; checkExact["v477 GRAV.ENTROPIC.SCALEFLOW.01 (i): the Frullani/scale-flow identity -Log[a] = Integrate[(e^{-a t}-e^{-t})/t] (symbolic) and the moment dictionary -- at the FLAT weight the maximally-symmetric relative trace integrates to exactly the v475 raw coefficients 3 b R + (17/24) b^2 R^2 (unit moments mu1 = mu2 = 1): the raw entropic action is the unit-moment point of a scale-measure family", frul == -Log[aa] && Simplify[mu1f - 3 bb] == 0 && Simplify[mu2f - (17/24) bb^2] == 0]; (* v477 (ii): the one moment condition + closure + v36 consistency *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3071)
- [(* ==== v355 E8.UNMAPPED.BANDWIDTH.01: the unmapped region's forced content is COLLECTIVE ==== *) Module[{exps, degs, totatives}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; degs = exps + 1; (* {2,8,12,14,18,20,24,30} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2362)
- [(* ---- (v24) quark ratio closure ---- *) checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117]; checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47]; checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26]; check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3]; check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2]; (* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L105)

## 2026-06-23 (the FULL covariant Einstein equation, parameter-free: the fixed-volume entanglement equilibrium gives [formula in source] with BOTH coefficients TFPT-fixed ( [formula in source] from v358, [formula in source] from [formula in source] via v60); B6 closed at the local level: v359)

[documents/changelog/sections/014-source.tex:348-365](../../../../documents/changelog/sections/014-source.tex#L348) · `section:49790f0118ee369b917a` · subsection

v359 ( GRAV.NONLINEAR.01) — Direction 1, the full covariant equation. Extends v358 from the linearised (fixed-radius, Ricci-level) result to the FULL covariant equation. \ Jacobson 2015: demanding stationarity of the small-ball entanglement entropy at fixed volume brings in the EINSTEIN TENSOR [formula in source] (not just [formula in source] ) — trace [formula in source] in [formula in source] , the structure that c

Explicit source references:

- [GRAV.NONLINEAR.01](../../../../verification/status_ledger.csv#L75) · explicit_claim_identifier · original status at linked ledger row
- [verification/v60_lambda_metrology_branch.py](../../../../verification/v60_lambda_metrology_branch.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ---- (v60) Lambda branch selection: prefactor 3/(4pi^2), branch mis-scale 64pi^3/3 ---- *) checkExact["delta_top=48 c3^4=3/(256 pi^4); (8pi)^2 delta_top=3/(4 pi^2); 2c3/delta_top=64 pi^3/3 (G_N pinned)", With[{c3 = 1/(8 Pi), dt = 48 (1/(8 Pi))^4}, Simplify[dt - 3/(256 Pi^4)] == 0 && Simplify[(8 Pi)^2 dt - 3/(4 Pi^2)] == 0 && Simplify[2 c3/dt - 64 Pi^3/3] == 0]]; checkExact["action exponents (1,5,10) = K5 counts (5 vertices, C(5,2)=10 edges); Pascal 16=1+5+10", {1, 5, Binomial[5, 2]} == {1, 5, 10} && 1 + 5 + 10 == 16]; (* ---- (v61) boundary-CFT bridge: WZW central charges = atoms, conformal embedding ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L282)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)

## 2026-06-23 (the classical gravity field equation, parameter-free: the entanglement first law [formula in source] with TFPT's atoms gives the LINEARISED Einstein equation with [formula in source] from [formula in source] ; the thermodynamic and geometric origins of [formula in source] coincide via [formula in source] ; the two formerly-open pieces (matter flux J3, entropy-density coefficient) closed/atom-fixed: v358)

[documents/changelog/sections/015-source.tex:1-16](../../../../documents/changelog/sections/015-source.tex#L1) · `section:708f3d321d2dd13c9cb9` · subsection

v358 ( GRAV.ENTROPY.EQUILIBRIUM.01) — the bridge to the dynamic world, instantiated on the gravity side. Carrying out the Jacobson-2015 / Faulkner-et-al.\ ``first law of entanglement [formula in source] Einstein equation'' with TFPT's atoms. \ PARAMETER-FREE COEFFICIENT: [formula in source] gives [formula in source] with [formula in source] fixed; all four [formula in source] -roles consistent (Unruh [formula in sour

Explicit source references:

- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v57_horizon_crosslinks.py](../../../../verification/v57_horizon_crosslinks.py#L1) · explicit_script_identifier
- [GRAV.ENTROPY.EQUILIBRIUM.01](../../../../verification/status_ledger.csv#L76) · explicit_claim_identifier · original status at linked ledger row
- [verification/v59_area_law_evidence.py](../../../../verification/v59_area_law_evidence.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* ---- (v57) horizon cross-links: Jacobson 8pi, Hod ln(3), Hawking |W(D5)| ---- *) checkExact["c3=1/(8pi) Einstein/Jacobson: 1/(16pi)=c3/2; 1/4=1/|mu4|; 1/(2pi)=4c3", Simplify[1/(16 Pi) - (1/(8 Pi))/2] == 0 && 1/4 == 1/4 && Simplify[1/(2 Pi) - 4/(8 Pi)] == 0]; checkExact["Hod QNM omega_R/T_H = ln(3) = ln(N_fam); Hawking power denom 1920=|W(D5)|=2^4*5!", Nfam == 3 && 1920 == 2^4 * 5!]; (* ---- (v58) seam-horizon chain: one-sided Gauss-Bonnet, KMS, S_BH, RT in seam units ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L263)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ---- (v59) area-law evidence: exact seam-unit parts (the EE area-law is numerical, Python-only) ---- *) checkExact["8 = |Z2|*|mu4| (sheet x glue); chaos-bound/seam unit 2pi = 1/(4 c3)", 2*4 == 8 && Simplify[2 Pi - 1/(4*(1/(8 Pi)))] == 0]; (* NOTE: the free-field entanglement area-law of v59 is a numerical computation (numpy symplectic spectra), Python-only by design -- not mirrored here. *)](../../../../verification/wolfram/tfpt_readouts.wl#L276)

## 2026-06-23 (the two frontier walls attacked directly: Direction A assembles the continuum chain of SEAM.EQUIV.01 theorem-by-theorem and ties its residual to the seam one-sidedness; Direction B was found ALREADY closed by v40 (harmonic metric [formula in source] finite linear algebra, not a PDE): v356)

[documents/changelog/sections/015-source.tex:17-40](../../../../documents/changelog/sections/015-source.tex#L17) · `section:5f8b87dd447560390c4e` · subsection

v356 ( SEAM.EQUIV.CONTINUUM.03) — Direction A, the continuum chain assembled. After the reverse-audit/bandwidth work showed no hidden discrete lever remains, the only fundamental progress is to assemble the continuum chain. Link-by-link: S1 the gapped ( [formula in source] , v302) quasi-free [formula in source] -Majorana collar ( v155/ v160) [formula in source] S2 invertible (gapped free fermions have no intrinsic to

Explicit source references:

- [verification/v31_R_dictionary.py](../../../../verification/v31_R_dictionary.py#L1) · explicit_script_identifier
- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.CONTINUUM.03](../../../../verification/status_ledger.csv#L77) · explicit_claim_identifier · original status at linked ledger row
- [verification/v356_continuum_mmst_applicability.py](../../../../verification/v356_continuum_mmst_applicability.py#L1) · explicit_script_identifier
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [verification/v297_route_a_literature_stack.py](../../../../verification/v297_route_a_literature_stack.py#L1) · explicit_script_identifier
- [verification/v351_continuum_realisation_sharpened.py](../../../../verification/v351_continuum_realisation_sharpened.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v301_route_a_invertible.py](../../../../verification/v301_route_a_invertible.py#L1) · explicit_script_identifier
- [verification/v58_seam_horizon_chain.py](../../../../verification/v58_seam_horizon_chain.py#L1) · explicit_script_identifier
- [verification/v40_harmonic_metric.py](../../../../verification/v40_harmonic_metric.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v351 SEAM.EQUIV.CONTINUUM.02: the order-4 clock + Coxeter-match pin E8 over SO(16) ==== *) Module[{cE8, cD8}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; checkExact["v351 SEAM.EQUIV.CONTINUUM.02: the c=8 which-net ambiguity (E8 det 1 vs SO(16)=D8 det 4) is RESOLVED by the seam's ORDER-4 mu4 clock -- index-4 extension of D5(+)A3 = E8 (full mu4 condensation 16->4->1), index-2 = SO(16) (partial Z2 16->4); the order (4 not 2) selects E8. The bootstrap agrees: h(E8)=30 max prime 5=g_car, h(D8)=14 max prime 7, so SO(16) fails the Coxeter-match. The residual of SEAM.EQUIV.01 is then PURELY the chiral-edge existence, not which-net", Det[cE8] == 1 && Det[cD8] == 4 && Max[FactorInteger[30][[All,1]]] == 5 && Max[FactorInteger[14][[All,1]]] == 7]; ]; (* ==== v352 TFPT.IRREDUCIBLE.01: both axioms bootstrap-forced; irreducibles = framework + pi ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2334)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ---- (v57) horizon cross-links: Jacobson 8pi, Hod ln(3), Hawking |W(D5)| ---- *) checkExact["c3=1/(8pi) Einstein/Jacobson: 1/(16pi)=c3/2; 1/4=1/|mu4|; 1/(2pi)=4c3", Simplify[1/(16 Pi) - (1/(8 Pi))/2] == 0 && 1/4 == 1/4 && Simplify[1/(2 Pi) - 4/(8 Pi)] == 0]; checkExact["Hod QNM omega_R/T_H = ln(3) = ln(N_fam); Hawking power denom 1920=|W(D5)|=2^4*5!", Nfam == 3 && 1920 == 2^4 * 5!]; (* ---- (v58) seam-horizon chain: one-sided Gauss-Bonnet, KMS, S_BH, RT in seam units ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L263)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)

## 2026-06-22 (bandwidth search of the unmapped [formula in source] region, with a strict forced-identity discriminator: the genuine overlooked structure is COLLECTIVE ( [formula in source] , [formula in source] , exponents [formula in source] totatives of [formula in source] ); the per-degree atom matches are unforced and DECLINED; no new physical hit – reconciling v66 and v354: v355)

[documents/changelog/sections/015-source.tex:41-62](../../../../documents/changelog/sections/015-source.tex#L41) · `section:99fa7c49f30373d04fa1` · subsection

v355 ( E8.UNMAPPED.BANDWIDTH.01) — the next step after v354, run honestly. The obvious follow-up (``search those five degrees for hits we overlooked'') is itself the numerology temptation v354 warns about: a rich object like [formula in source] returns a numerical match for almost anything. So the scan uses a STRICT discriminator – a candidate counts only if it is a FORCED identity (a theorem about [formula in source

Explicit source references:

- [verification/v223_coxeter_totative_clock.py](../../../../verification/v223_coxeter_totative_clock.py#L1) · explicit_script_identifier
- [E8.UNMAPPED.BANDWIDTH.01](../../../../verification/status_ledger.csv#L95) · explicit_claim_identifier · original status at linked ledger row
- [verification/v219_icosahedral_mckay.py](../../../../verification/v219_icosahedral_mckay.py#L1) · explicit_script_identifier
- [verification/v355_e8_unmapped_bandwidth.py](../../../../verification/v355_e8_unmapped_bandwidth.py#L1) · explicit_script_identifier
- [verification/v354_e8_reverse_audit.py](../../../../verification/v354_e8_reverse_audit.py#L1) · explicit_script_identifier
- [verification/v66_e8_casimir_degrees.py](../../../../verification/v66_e8_casimir_degrees.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v355 E8.UNMAPPED.BANDWIDTH.01: the unmapped region's forced content is COLLECTIVE ==== *) Module[{exps, degs, totatives}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; degs = exps + 1; (* {2,8,12,14,18,20,24,30} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2362)
- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)
- [(* ---- (v63) Seam-Engineering Index: exact closed form ---- *) checkExact["||V||=248 c3^2=31/(8pi^2); 2||V||=31/(4pi^2); 248=dim E8, 31=1+h^v(E8)", With[{c3 = 1/(8 Pi)}, Simplify[248 c3^2 - 31/(8 Pi^2)] == 0 && 248/8 == 31 == 1 + 30]]; checkExact["Xi = 2||V||/Delta = 31/(24 pi^2 log(3/2)); Delta_eff = Delta - 2||V|| > 0", Simplify[(31/(4 Pi^2))/(6 Log[3/2]) - 31/(24 Pi^2 Log[3/2])] == 0 && N[6 Log[3/2] - 31/(4 Pi^2)] > 1]; (* ---- (v66) compiler atoms = E8 Casimir invariant degrees ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L300)
- [(* v223 Coxeter totative clock: (Z/30)^x = E8 exponents, order-4 element 7 *) checkExact["v223 COX.CLOCK.01: (Z/30)^x = {1,7,11,13,17,19,23,29} = E8 exponents, " <> "phi(30)=8=rank E8, 30=2*3*5; mult-by-7 has order 4 (7^2=19, 7^4=1 mod 30): a " <> "mu4 clock <7>={1,7,13,19}; the conjugate pairs split into 4 invariant planes", Select[Range[29], CoprimeQ[#, 30] &] == {1, 7, 11, 13, 17, 19, 23, 29} && EulerPhi[30] == 8 && PowerMod[7, 2, 30] == 19 && PowerMod[7, 4, 30] == 1 && Sort[Mod[7^Range[0, 3], 30]] == {1, 7, 13, 19} && Length[Union[Sort /@ ({#, 30 - #} & /@ {1, 7, 11, 13, 17, 19, 23, 29})]] == 4]; (* v227 degree/exponent channel split: 248 = 120 + 128 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1804)
- [(* ==== v354 E8.REVERSE.AUDIT.01: 3 of 8 E8 Casimir degrees are load-bearing, 5 unmapped ==== *) Module[{exps, degs, mapped, unmapped}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; (* E8 exponents *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2352)
- [(* v431 (5): clean {0,2} split special to E8 among exceptionals *) cleanSplit[name_] := Module[{ex, hh, dm}, ex = Switch[name, "A4", {1, 2, 3, 4}, "D5", {1, 3, 5, 7, 4}, "E6", {1, 4, 5, 7, 8, 11}, "E7", {1, 5, 7, 9, 11, 13, 17}, "E8", exps, "F4", {1, 5, 7, 11}, "G2", {1, 5}]; hh = Switch[name, "A4", 5, "D5", 8, "E6", 12, "E7", 18, "E8", 30, "F4", 12, "G2", 6]; dm = DeleteDuplicates[Mod[ex + 1, 6]]; Sort[ex] == Select[Range[1, hh - 1], CoprimeQ[#, hh] &] && SubsetQ[{0, 2}, dm] && Mod[hh, 6] == 0]; e8Clean = cleanSplit["E8"]; e67Fail = ! (cleanSplit["E6"] && cleanSplit["E7"] && cleanSplit["D5"]); checkExact["v431 E8.DEGREE.LADDER.01 (v): clean {0,2}-mod-6 split (6|h AND exponents=totatives) holds for E8 but FAILS for E6,E7,D5; F4/G2 share split but not spine+flavor-det content", e8Clean && e67Fail && cleanSplit["F4"] && cleanSplit["G2"]]; (* v431 (6): all five 'unmapped' degrees homed; v355 functorial line upheld [P] *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2693)

## 2026-06-22 (the REVERSE numerology audit, and what the golden ratio means: of [formula in source] 's 8 Casimir invariants only [formula in source] feed a primary readout and [formula in source] are hull overhead; the golden ratio is UNMAPPED structure, so it cannot be numerology: v354)

[documents/changelog/sections/015-source.tex:63-84](../../../../documents/changelog/sections/015-source.tex#L63) · `section:90d9ccdfa2e81d8ea0bd` · subsection

v354 ( E8.REVERSE.AUDIT.01) — the reverse complement of v305. TFPT's forward discipline ( v305) is one-directional: every physical READOUT must map onto an [formula in source] structure (anti-fitting). The sharp adversarial question runs the OTHER way — how much [formula in source] structure maps onto NOTHING, and is the recurring golden ratio numerology? \ THE REVERSE AUDIT: of [formula in source] 's eight Casimir i

Explicit source references:

- [verification/v355_e8_unmapped_bandwidth.py](../../../../verification/v355_e8_unmapped_bandwidth.py#L1) · explicit_script_identifier
- [verification/v305_witness_independence.py](../../../../verification/v305_witness_independence.py#L1) · explicit_script_identifier
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [verification/v354_e8_reverse_audit.py](../../../../verification/v354_e8_reverse_audit.py#L1) · explicit_script_identifier
- [E8.REVERSE.AUDIT.01](../../../../verification/status_ledger.csv#L96) · explicit_claim_identifier · original status at linked ledger row
- [verification/v66_e8_casimir_degrees.py](../../../../verification/v66_e8_casimir_degrees.py#L1) · explicit_script_identifier
- [verification/v348_seam_rigidity_route.py](../../../../verification/v348_seam_rigidity_route.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v354 E8.REVERSE.AUDIT.01: 3 of 8 E8 Casimir degrees are load-bearing, 5 unmapped ==== *) Module[{exps, degs, mapped, unmapped}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; (* E8 exponents *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2352)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [(* ==== v355 E8.UNMAPPED.BANDWIDTH.01: the unmapped region's forced content is COLLECTIVE ==== *) Module[{exps, degs, totatives}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; degs = exps + 1; (* {2,8,12,14,18,20,24,30} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2362)
- [(* ---- (v63) Seam-Engineering Index: exact closed form ---- *) checkExact["||V||=248 c3^2=31/(8pi^2); 2||V||=31/(4pi^2); 248=dim E8, 31=1+h^v(E8)", With[{c3 = 1/(8 Pi)}, Simplify[248 c3^2 - 31/(8 Pi^2)] == 0 && 248/8 == 31 == 1 + 30]]; checkExact["Xi = 2||V||/Delta = 31/(24 pi^2 log(3/2)); Delta_eff = Delta - 2||V|| > 0", Simplify[(31/(4 Pi^2))/(6 Log[3/2]) - 31/(24 Pi^2 Log[3/2])] == 0 && N[6 Log[3/2] - 31/(4 Pi^2)] > 1]; (* ---- (v66) compiler atoms = E8 Casimir invariant degrees ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L300)
- [(* v431 (5): clean {0,2} split special to E8 among exceptionals *) cleanSplit[name_] := Module[{ex, hh, dm}, ex = Switch[name, "A4", {1, 2, 3, 4}, "D5", {1, 3, 5, 7, 4}, "E6", {1, 4, 5, 7, 8, 11}, "E7", {1, 5, 7, 9, 11, 13, 17}, "E8", exps, "F4", {1, 5, 7, 11}, "G2", {1, 5}]; hh = Switch[name, "A4", 5, "D5", 8, "E6", 12, "E7", 18, "E8", 30, "F4", 12, "G2", 6]; dm = DeleteDuplicates[Mod[ex + 1, 6]]; Sort[ex] == Select[Range[1, hh - 1], CoprimeQ[#, hh] &] && SubsetQ[{0, 2}, dm] && Mod[hh, 6] == 0]; e8Clean = cleanSplit["E8"]; e67Fail = ! (cleanSplit["E6"] && cleanSplit["E7"] && cleanSplit["D5"]); checkExact["v431 E8.DEGREE.LADDER.01 (v): clean {0,2}-mod-6 split (6|h AND exponents=totatives) holds for E8 but FAILS for E6,E7,D5; F4/G2 share split but not spine+flavor-det content", e8Clean && e67Fail && cleanSplit["F4"] && cleanSplit["G2"]]; (* v431 (6): all five 'unmapped' degrees homed; v355 functorial line upheld [P] *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2693)
- [(* ==== v348 SEAM.EQUIV.RIGID.01: phi bridges crystallographic mu4 to non-crystallographic 2I ==== *) Module[{cryst, phi}, cryst = {1, 2, 3, 4, 6}; (* crystallographic restriction: lattice-compatible rotation orders *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2306)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)

## 2026-06-22 (the bird's-eye rethink: TFPT is a unique self-consistent LOOP with ZERO free dials, not a linear axiom system; [formula in source] is a fixed geometric constant, not a dial; the one residual is the continuum closure: v353)

[documents/changelog/sections/015-source.tex:85-99](../../../../documents/changelog/sections/015-source.tex#L85) · `section:dcc46f2343a1ce26d935` · subsection

v353 ( TFPT.SELFLOOP.01) — refining v352. Stepping all the way back: TFPT is not a LINEAR theory (axioms [formula in source] theorems) but a CLOSED SELF-CONSISTENT LOOP whose outputs fix its own inputs. \ it is a loop: [formula in source] max prime of the output [formula in source] , and the [formula in source] in [formula in source] – the outputs fix the inputs ( v6), with a unique fixed point ( v56); ``which is the

Explicit source references:

- [verification/v353_selfloop_capstone.py](../../../../verification/v353_selfloop_capstone.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier
- [TFPT.SELFLOOP.01](../../../../verification/status_ledger.csv#L102) · explicit_claim_identifier · original status at linked ledger row
- [verification/v352_framework_irreducible.py](../../../../verification/v352_framework_irreducible.py#L1) · explicit_script_identifier
- [verification/v351_continuum_realisation_sharpened.py](../../../../verification/v351_continuum_realisation_sharpened.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v351 SEAM.EQUIV.CONTINUUM.02: the order-4 clock + Coxeter-match pin E8 over SO(16) ==== *) Module[{cE8, cD8}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; checkExact["v351 SEAM.EQUIV.CONTINUUM.02: the c=8 which-net ambiguity (E8 det 1 vs SO(16)=D8 det 4) is RESOLVED by the seam's ORDER-4 mu4 clock -- index-4 extension of D5(+)A3 = E8 (full mu4 condensation 16->4->1), index-2 = SO(16) (partial Z2 16->4); the order (4 not 2) selects E8. The bootstrap agrees: h(E8)=30 max prime 5=g_car, h(D8)=14 max prime 7, so SO(16) fails the Coxeter-match. The residual of SEAM.EQUIV.01 is then PURELY the chiral-edge existence, not which-net", Det[cE8] == 1 && Det[cD8] == 4 && Max[FactorInteger[30][[All,1]]] == 5 && Max[FactorInteger[14][[All,1]]] == 7]; ]; (* ==== v352 TFPT.IRREDUCIBLE.01: both axioms bootstrap-forced; irreducibles = framework + pi ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2334)
- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-22 (two consequences: the [formula in source] which-net ambiguity resolved by the order-4 clock, and BOTH axioms shown bootstrap-forced so the only irreducibles are the framework [formula in source] [formula in source] : v351, v352)

[documents/changelog/sections/015-source.tex:100-119](../../../../documents/changelog/sections/015-source.tex#L100) · `section:a5034e3be2279bec9f75` · subsection

v351 ( SEAM.EQUIV.CONTINUUM.02) — the which-net ambiguity falls. The long-standing `` [formula in source] ambiguity'' ( [formula in source] det 1 vs [formula in source] det 4, both [formula in source] , flagged open in v277/ v344) is RESOLVED, non-circularly, by the seam's ORDER-4 [formula in source] clock: the index-4 simple-current extension of [formula in source] is [formula in source] ( v154), the index-2 would b

Explicit source references:

- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [verification/v344_detk_synthesis.py](../../../../verification/v344_detk_synthesis.py#L1) · explicit_script_identifier
- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_script_identifier
- [verification/v277_seam_calderon_e8_match.py](../../../../verification/v277_seam_calderon_e8_match.py#L1) · explicit_script_identifier
- [verification/v352_framework_irreducible.py](../../../../verification/v352_framework_irreducible.py#L1) · explicit_script_identifier
- [verification/v351_continuum_realisation_sharpened.py](../../../../verification/v351_continuum_realisation_sharpened.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.CONTINUUM.02](../../../../verification/status_ledger.csv#L71) · explicit_claim_identifier · original status at linked ledger row
- [verification/v83_e8net_holomorphic_uniqueness.py](../../../../verification/v83_e8net_holomorphic_uniqueness.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [TFPT.IRREDUCIBLE.01](../../../../verification/status_ledger.csv#L103) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ==== v344 SEAM.DETK.01: the ADE |det Cartan| = |H_1(link)| sequence, only E8 -> 1 ==== *) Module[{cartanA, cartanD, E8, detADE}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}]; cartanD[n_] := Module[{M = Normal[cartanA[n]]}, M[[n, n - 1]] = M[[n - 1, n]] = 0; M[[n, n - 2]] = M[[n - 2, n]] = -1; M]; E8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; (* |det Cartan| = |H_1(link)| = #(1-dim irreps): A_n->n+1, D_n->4, E6->3, E7->2, E8->1; only E8 -> 1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2271)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v351 SEAM.EQUIV.CONTINUUM.02: the order-4 clock + Coxeter-match pin E8 over SO(16) ==== *) Module[{cE8, cD8}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; checkExact["v351 SEAM.EQUIV.CONTINUUM.02: the c=8 which-net ambiguity (E8 det 1 vs SO(16)=D8 det 4) is RESOLVED by the seam's ORDER-4 mu4 clock -- index-4 extension of D5(+)A3 = E8 (full mu4 condensation 16->4->1), index-2 = SO(16) (partial Z2 16->4); the order (4 not 2) selects E8. The bootstrap agrees: h(E8)=30 max prime 5=g_car, h(D8)=14 max prime 7, so SO(16) fails the Coxeter-match. The residual of SEAM.EQUIV.01 is then PURELY the chiral-edge existence, not which-net", Det[cE8] == 1 && Det[cD8] == 4 && Max[FactorInteger[30][[All,1]]] == 5 && Max[FactorInteger[14][[All,1]]] == 7]; ]; (* ==== v352 TFPT.IRREDUCIBLE.01: both axioms bootstrap-forced; irreducibles = framework + pi ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2334)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## 2026-06-22 (correction: the inputs are bootstrap-forced fixed points, not free axioms – [formula in source] IS the icosahedral [formula in source] of [formula in source] , and the golden ratio is emergent from the [formula in source] -glue, not external: v350)

[documents/changelog/sections/015-source.tex:120-134](../../../../documents/changelog/sections/015-source.tex#L120) · `section:2ef143ddeb6e7890a438` · subsection

v350 ( SEAM.EQUIV.BOOTSTRAP.01) — correcting v349. An honest correction prompted by the right objection that the inputs are not axioms but are back-determined by the theory. \ the inputs ARE bootstrap-forced ( v6): [formula in source] is over-determined three ways – rank-fill ( [formula in source] ), Coxeter-match ( [formula in source] max prime of [formula in source] ), Pascal ( [formula in source] ). \ so [formula 

Explicit source references:

- [verification/v349_raw_seam_golden_test.py](../../../../verification/v349_raw_seam_golden_test.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v350_bootstrap_inputs_correction.py](../../../../verification/v350_bootstrap_inputs_correction.py#L1) · explicit_script_identifier
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.BOOTSTRAP.01](../../../../verification/status_ledger.csv#L104) · explicit_claim_identifier · original status at linked ledger row
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* ==== v349 SEAM.EQUIV.GOLDEN.01: the raw carrier is NOT golden (D5 h=8 -> sqrt2); 5|h only on the output side ==== *) Module[{eigD5, eigA3, goldenHs}, (* Coxeter eigenvalue 2cos(2pi/h): D5 (h=8) -> sqrt2, A3 (h=4) -> 0; golden needs 5|h *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2314)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* ==== v350 SEAM.EQUIV.BOOTSTRAP.01: g_car=5 IS the icosahedral 5 of h(E8)=30 (the v349 correction) ==== *) Module[{primes30, maxPrime, piecesGolden, glueGolden}, primes30 = Sort[FactorInteger[30][[All, 1]]]; (* {2,3,5} = the icosahedral axes *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2323)

## 2026-06-22 (the honest test – does the raw seam carry [formula in source] ? – answer NO: the bare carrier gives [formula in source] , golden is the icosahedral input; the keystone reduces to ``is [formula in source] a pentagon or a count?'': v349)

[documents/changelog/sections/015-source.tex:135-151](../../../../documents/changelog/sections/015-source.tex#L135) · `section:fac429be371842092df9` · subsection

v349 ( SEAM.EQUIV.GOLDEN.01). The honest, computed test of the v348 question, and a clarifying NEGATIVE: the raw seam does not carry the golden ratio. \ the golden ratio [formula in source] is the signature of a [formula in source] -fold rotation ( [formula in source] ); the carrier [formula in source] has [formula in source] (eigenvalue [formula in source] ) and [formula in source] has [formula in source] – no 5-fol

Explicit source references:

- [verification/v349_raw_seam_golden_test.py](../../../../verification/v349_raw_seam_golden_test.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.GOLDEN.01](../../../../verification/status_ledger.csv#L105) · explicit_claim_identifier · original status at linked ledger row
- [verification/v348_seam_rigidity_route.py](../../../../verification/v348_seam_rigidity_route.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* ==== v349 SEAM.EQUIV.GOLDEN.01: the raw carrier is NOT golden (D5 h=8 -> sqrt2); 5|h only on the output side ==== *) Module[{eigD5, eigA3, goldenHs}, (* Coxeter eigenvalue 2cos(2pi/h): D5 (h=8) -> sqrt2, A3 (h=4) -> 0; golden needs 5|h *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2314)
- [(* ==== v348 SEAM.EQUIV.RIGID.01: phi bridges crystallographic mu4 to non-crystallographic 2I ==== *) Module[{cryst, phi}, cryst = {1, 2, 3, 4, 6}; (* crystallographic restriction: lattice-compatible rotation orders *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2306)
- [(* ==== v350 SEAM.EQUIV.BOOTSTRAP.01: g_car=5 IS the icosahedral 5 of h(E8)=30 (the v349 correction) ==== *) Module[{primes30, maxPrime, piecesGolden, glueGolden}, primes30 = Sort[FactorInteger[30][[All, 1]]]; (* {2,3,5} = the icosahedral axes *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2323)

## 2026-06-22 (Route B carried out: rigidity [formula in source] the icosian-ring identity reduce the whole keystone to ONE question – does the raw seam carry the golden ratio? – the simplest form of L2: v348)

[documents/changelog/sections/015-source.tex:152-167](../../../../documents/changelog/sections/015-source.tex#L152) · `section:414a84d23afa6566ca5e` · subsection

v348 ( SEAM.EQUIV.RIGID.01). Executes the rigidity route (mode B of v347) and lands on a strikingly simple statement. \ rigidity closes the crystallographic part: the order-4 clock has the unique normal form [formula in source] (Nielsen/Kerckhoff, v180), Troyanov gives the unique flat pillowcase metric ( v284). \ the downstream is a LATTICE identity, not just a graph: by Conway–Sloane the ring of icosians ( [formula 

Explicit source references:

- [verification/v284_route_i_rp_uniqueness.py](../../../../verification/v284_route_i_rp_uniqueness.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.RIGID.01](../../../../verification/status_ledger.csv#L106) · explicit_claim_identifier · original status at linked ledger row
- [verification/v347_seam_closure_modes.py](../../../../verification/v347_seam_closure_modes.py#L1) · explicit_script_identifier
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [verification/v348_seam_rigidity_route.py](../../../../verification/v348_seam_rigidity_route.py#L1) · explicit_script_identifier
- [verification/v180_clock_is_mobius.py](../../../../verification/v180_clock_is_mobius.py#L1) · explicit_script_identifier
- [verification/v313_golden_atoms_spectral.py](../../../../verification/v313_golden_atoms_spectral.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* ==== v347 SEAM.EQUIV.CLOSURE.01: the flat seam base vs the spherical icosahedral base ==== *) Module[{chiSeam, chi2I}, (* seam pillowcase S^2(2,2,2,2): chi_orb = 0 (Euclidean/flat); 2I Seifert base S^2(2,3,5): chi_orb = 1/30 (spherical) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2297)
- [(* ==== v348 SEAM.EQUIV.RIGID.01: phi bridges crystallographic mu4 to non-crystallographic 2I ==== *) Module[{cryst, phi}, cryst = {1, 2, 3, 4, 6}; (* crystallographic restriction: lattice-compatible rotation orders *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2306)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)

## 2026-06-22 (can the one open arrow be fully solved? the closure-mode classification: the flat [formula in source] spherical base locus, four modes, no free theorem – only rigidity or axiom [formula in source] : v347)

[documents/changelog/sections/015-source.tex:168-182](../../../../documents/changelog/sections/015-source.tex#L168) · `section:9800e2e20cb3dc2e280a` · subsection

v347 ( SEAM.EQUIV.CLOSURE.01). A direct, honest answer to ``is there any other way to fully solve the one open arrow L2?''. \ the precise locus: the seam gives the flat pillowcase base [formula in source] ( [formula in source] , v216) while the [formula in source] structure is the Seifert base over the spherical [formula in source] ( [formula in source] ), so L2 bridges two geometric types – why it needs the carrier 

Explicit source references:

- [verification/v347_seam_closure_modes.py](../../../../verification/v347_seam_closure_modes.py#L1) · explicit_script_identifier
- [verification/v331_necessity_of_H.py](../../../../verification/v331_necessity_of_H.py#L1) · explicit_script_identifier
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [verification/v300_flataway_rigid.py](../../../../verification/v300_flataway_rigid.py#L1) · explicit_script_identifier
- [verification/v284_route_i_rp_uniqueness.py](../../../../verification/v284_route_i_rp_uniqueness.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.CLOSURE.01](../../../../verification/status_ledger.csv#L107) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ==== v347 SEAM.EQUIV.CLOSURE.01: the flat seam base vs the spherical icosahedral base ==== *) Module[{chiSeam, chi2I}, (* seam pillowcase S^2(2,2,2,2): chi_orb = 0 (Euclidean/flat); 2I Seifert base S^2(2,3,5): chi_orb = 1/30 (spherical) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2297)

## 2026-06-22 (the geometric bridge made explicit: the keystone is ONE arrow – raw-seam [formula in source] is a six-link chain, five theorems [formula in source] one open orbifold realisation, the group forced by the [formula in source] atoms: v346)

[documents/changelog/sections/015-source.tex:183-197](../../../../documents/changelog/sections/015-source.tex#L183) · `section:00c96659d1c56ecb746e` · subsection

v346 ( SEAM.EQUIV.GEOM.01). The honest capstone of the SEAM.EQUIV.01 investigation: it lays out the full path raw-seam [formula in source] as six links and shows exactly one is open. / \ L1 raw seam [formula in source] [formula in source] four marks (Gauss–Bonnet, v216); \ L2 [formula in source] [formula in source] the [formula in source] atoms [formula in source] the [formula in source] orbifold [formula in source] 

Explicit source references:

- [verification/v219_icosahedral_mckay.py](../../../../verification/v219_icosahedral_mckay.py#L1) · explicit_script_identifier
- [verification/v346_seam_geometric_bridge.py](../../../../verification/v346_seam_geometric_bridge.py#L1) · explicit_script_identifier
- [verification/v345_hypergraph_homotopy.py](../../../../verification/v345_hypergraph_homotopy.py#L1) · explicit_script_identifier
- [verification/v232_e8_kleinian_seam.py](../../../../verification/v232_e8_kleinian_seam.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.GEOM.01](../../../../verification/status_ledger.csv#L108) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v232: the seam as the E8 Kleinian singularity (du Val resolution + link) ==== *) Module[{labels, e8edges, A8, C8, degs}, labels = {1, 2, 3, 4, 5, 6, 4, 2, 3}; (* affine E8 Kac marks *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1894)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [(* ==== v345 SEAM.DETK.02: the plumbing-link H_1 = coker(Cartan) via Smith normal form ==== *) Module[{cartanD, E8, sfE8, sfD5, cokerE8, cokerD5}, cartanD[n_] := Module[{M = Normal[SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}]]}, M[[n, n - 1]] = M[[n - 1, n]] = 0; M[[n, n - 2]] = M[[n - 2, n]] = -1; M]; E8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; (* coker = product of invariant factors > 1 = |H_1(plumbing link)|; E8 -> 1 (homology sphere), D5 -> 4 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2284)
- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)

## 2026-06-22 (executing route R3: the [formula in source] -rewrite attractor link computed to be the Poincar\'e homology sphere ( [formula in source] ), the combinatorial core complete, only the geometric bridge open: v345)

[documents/changelog/sections/015-source.tex:198-213](../../../../documents/changelog/sections/015-source.tex#L198) · `section:f45ff82a01e81b33f3c1` · subsection

v345 ( SEAM.DETK.02). Carries out the combinatorial core of the hypergraph-homotopy route (R3, the most promising fresh angle from v344) as far as it computably goes. By plumbing topology (Brieskorn/Hirzebruch) the link of a tree plumbing with the ADE Cartan intersection form has [formula in source] . \ the Smith normal form of the [formula in source] Cartan matrix is the identity, so [formula in source] – the [formu

Explicit source references:

- [SEAM.DETK.02](../../../../verification/status_ledger.csv#L109) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v344_detk_synthesis.py](../../../../verification/v344_detk_synthesis.py#L1) · explicit_script_identifier
- [verification/v345_hypergraph_homotopy.py](../../../../verification/v345_hypergraph_homotopy.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v345 SEAM.DETK.02: the plumbing-link H_1 = coker(Cartan) via Smith normal form ==== *) Module[{cartanD, E8, sfE8, sfD5, cokerE8, cokerD5}, cartanD[n_] := Module[{M = Normal[SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}]]}, M[[n, n - 1]] = M[[n - 1, n]] = 0; M[[n, n - 2]] = M[[n - 2, n]] = -1; M]; E8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; (* coker = product of invariant factors > 1 = |H_1(plumbing link)|; E8 -> 1 (homology sphere), D5 -> 4 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2284)
- [(* ==== v344 SEAM.DETK.01: the ADE |det Cartan| = |H_1(link)| sequence, only E8 -> 1 ==== *) Module[{cartanA, cartanD, E8, detADE}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}]; cartanD[n_] := Module[{M = Normal[cartanA[n]]}, M[[n, n - 1]] = M[[n - 1, n]] = 0; M[[n, n - 2]] = M[[n - 2, n]] = -1; M]; E8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; (* |det Cartan| = |H_1(link)| = #(1-dim irreps): A_n->n+1, D_n->4, E6->3, E7->2, E8->1; only E8 -> 1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2271)

## 2026-06-22 (the one keystone bit [formula in source] mapped: six equivalent faces, the genus-1 obstruction, three access routes, the hypergraph-homotopy route the most promising fresh angle: v344)

[documents/changelog/sections/015-source.tex:214-229](../../../../documents/changelog/sections/015-source.tex#L214) · `section:ee9a2e2d9ccdc3799662` · subsection

v344 ( SEAM.DETK.01). A bird's-eye, full-spectrum map of SEAM.EQUIV.01's only open residual, the holomorphy bit [formula in source] . \ it is ONE statement with six equivalent faces (holomorphy / homology-sphere link [formula in source] / one [formula in source] -dim irrep / [formula in source] Cartan [formula in source] / full [formula in source] condensation / [formula in source] CM), unified by [formula in source]

Explicit source references:

- [verification/v87_bulk_uniqueness_reduction.py](../../../../verification/v87_bulk_uniqueness_reduction.py#L1) · explicit_script_identifier
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [SEAM.DETK.01](../../../../verification/status_ledger.csv#L110) · explicit_claim_identifier · original status at linked ledger row
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v232_e8_kleinian_seam.py](../../../../verification/v232_e8_kleinian_seam.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v344_detk_synthesis.py](../../../../verification/v344_detk_synthesis.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [(* ==== v344 SEAM.DETK.01: the ADE |det Cartan| = |H_1(link)| sequence, only E8 -> 1 ==== *) Module[{cartanA, cartanD, E8, detADE}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}]; cartanD[n_] := Module[{M = Normal[cartanA[n]]}, M[[n, n - 1]] = M[[n - 1, n]] = 0; M[[n, n - 2]] = M[[n - 2, n]] = -1; M]; E8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; (* |det Cartan| = |H_1(link)| = #(1-dim irreps): A_n->n+1, D_n->4, E6->3, E7->2, E8->1; only E8 -> 1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2271)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)
- [(* ==== v232: the seam as the E8 Kleinian singularity (du Val resolution + link) ==== *) Module[{labels, e8edges, A8, C8, degs}, labels = {1, 2, 3, 4, 5, 6, 4, 2, 3}; (* affine E8 Kac marks *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1894)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)

## 2026-06-22 (the four black-hole-birth completion routes investigated: none closes all or is 100\% provable alone; all four converge on SEAM.EQUIV.01 [formula in source] the decoupled QG contour: v343)

[documents/changelog/sections/015-source.tex:230-245](../../../../documents/changelog/sections/015-source.tex#L230) · `section:4dcf513f2ae74de8645b` · subsection

v343 ( FOUR.ROUTES.01). A direct, honest answer to ``which black-hole-birth route closes ALL problems and is 100\% provable'': none individually — but the four converge on the same two residuals as v335. \ (A) the finite causal diamond reframes QG.AMB to a finite thermal trace (de Sitter [formula in source] finite, [formula in source] ) but inherits the GHP contour ( v334, ); does not touch the seam. \ (B) Carlip–Car

Explicit source references:

- [FOUR.ROUTES.01](../../../../verification/status_ledger.csv#L111) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v334_conformal_resolution.py](../../../../verification/v334_conformal_resolution.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v239_kms_thermal_time.py](../../../../verification/v239_kms_thermal_time.py#L1) · explicit_script_identifier
- [verification/v335_seam_equiv_unify.py](../../../../verification/v335_seam_equiv_unify.py#L1) · explicit_script_identifier
- [verification/v343_four_routes_analysis.py](../../../../verification/v343_four_routes_analysis.py#L1) · explicit_script_identifier
- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)

## 2026-06-22 (the heat-kernel origin of the [formula in source] terms: the Calder\'on quadratic is the Gilkey gauge-curvature coefficient; the cubic Maxwell moment stays the EM.WARD.01 residual: v342)

[documents/changelog/sections/015-source.tex:246-259](../../../../documents/changelog/sections/015-source.tex#L246) · `section:ed458665aa45a0bcd44b` · subsection

v342 ( EM.WARD.02) — the heat-kernel sharpening of EM.WARD.01. Derives the ORIGIN and STRUCTURE of the [formula in source] determinant-line terms from textbook Seeley–DeWitt / Gilkey coefficients, advancing the EM-Ward origin from \ (conjectured) to \ for the term structure; no new gate. \ [formula in source] is the boundary Gauss–Bonnet coefficient ( [formula in source] , [formula in source] , v216). \ the [formula 

Explicit source references:

- [EM.WARD.01](../../../../verification/status_ledger.csv#L70) · explicit_claim_identifier · original status at linked ledger row
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v342_em_ward_heatkernel.py](../../../../verification/v342_em_ward_heatkernel.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [EM.WARD.02](../../../../verification/status_ledger.csv#L112) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v342 EM.WARD.02: the heat-kernel origin of the F_U(1) terms ==== *) Module[{c3v, ointK, c3gb, gilkey, q2}, c3v = 1/(8 Pi); (* c3 = boundary Gauss-Bonnet coefficient: oint_{S^2} K = 2 pi chi = 4 pi (chi=2), c3 = 1/(|Z2| oint K) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2259)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## 2026-06-22 ( [formula in source] as the stationarity of a [formula in source] determinant line: every ingredient an index / heat-kernel coefficient / discriminant form, the open EM-Ward obligation named: v341)

[documents/changelog/sections/015-source.tex:260-278](../../../../documents/changelog/sections/015-source.tex#L260) · `section:656d00cdb6c9c469cdbe` · subsection

v341 ( ALPHA.QUILLEN.01). Answers the external review's sharpest valid point — ``derive the form of [formula in source] , not more decimals''. The EM closure [formula in source] is rewritten as a stationarity of the boundary [formula in source] determinant line: [formula in source] . \ every ingredient is a NAMED object, not a knob: [formula in source] is a [formula in source] index ( [formula in source] , [formula i

Explicit source references:

- [verification/v341_alpha_quillen.py](../../../../verification/v341_alpha_quillen.py#L1) · explicit_script_identifier
- [verification/v48_em_ward.py](../../../../verification/v48_em_ward.py#L1) · explicit_script_identifier
- [EM.WARD.01](../../../../verification/status_ledger.csv#L70) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.01](../../../../verification/status_ledger.csv#L443) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v341 ALPHA.QUILLEN.01: the seam-form discriminant identities ==== *) Module[{c3v, phib}, c3v = 1/(8 Pi); phib = 1/(6 Pi); (* phi_base = (4/3) c3 carries q(A3): c3/phi_base = 3/4; with -5/4 = -q(D5) the F_U(1) seam response carries BOTH glue forms, q(D5)+q(A3)=2 = E8 root norm; counterterm coefficient (4/5)M = 8 b1 = 8*(41/10) with b1 the U(1)_Y one-loop beta (rank E8 = 8) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2248)
- [(* ---- (v47) Boundary Carrier Selection Theorem (Theorem A) ---- *) checkExact["q(D5)+q(A3)=5/4+3/4=2 (E8 root norm); glue index sqrt(4*4/1)=4=|mu4|", 5/4 + 3/4 == 2 && Sqrt[4*4/1] == 4]; checkExact["only n=5 gives 16-dim D_n half-spinor (2^{n-1}=16) => D5", Select[Range[2, 8], 2^(# - 1) == 16 &] == {5}]; (* ---- (v48) EM boundary Ward decomposition (Theorem C) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L184)

## 2026-06-22 ( [formula in source] reconciled with the archived derivation: predicted \& dimensionless (so it does not define a mass), the tension is the reheating channel: v340)

[documents/changelog/sections/015-source.tex:279-294](../../../../documents/changelog/sections/015-source.tex#L279) · `section:3bd0d82163305ccd4d89` · subsection

v340 ( AS.RECONCILE.01). Answers ``why don't we have [formula in source] / the old versions derived it'' and ``can a ratio define mass itself''. \ [formula in source] is predicted and dimensionless: [formula in source] with [formula in source] a pure ratio, so [formula in source] pins the e-fold count [formula in source] , NOT [formula in source] — it cannot define an absolute mass (No-Unit, v153, stands). \ the [for

Explicit source references:

- [verification/v84_frozen_registry.py](../../../../verification/v84_frozen_registry.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v340_As_reconcile.py](../../../../verification/v340_As_reconcile.py#L1) · explicit_script_identifier
- [AS.RECONCILE.01](../../../../verification/status_ledger.csv#L442) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v84) frozen registry decimals recompute from the axioms ---- *) phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); FU1[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 41 Log[1/phiseam[a]]; aStar = a /. FindRoot[FU1[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; check["v84 ALPHA_INV frozen", 1/aStar, 137.0359992168407125035379`30, 10^-20]; lamC = Sqrt[phi0 (1 - phi0)]; check["v84 SIN2_THETA12_SEED frozen", 1/3 - phi0/2, 0.3067473572449105696786871`30, 10^-20]; check["v84 SIN2_THETA13 frozen", phi0 Exp[-5/6], 0.02310843515888110429328466`30, 10^-20]; check["v84 BETA_BIREFRINGENCE_DEG frozen", (phi0/(4 Pi)) (180/Pi), 0.2424350309009295284924315`30, 10^-20]; check["v84 OMEGA_B frozen", (1 - 1/(4 Pi)) phi0, 0.04894066266545011220054565`30, 10^-20]; check["v84 LAMBDA_C frozen", lamC, 0.2243762368847217731120972`30, 10^-20]; check["v84 S23_CKM frozen", phi0/(1 + lamC), 0.04342778843220215630289116`30, 10^-20]; check["v84 S13_CKM frozen", lamC^3/3, 0.003765384454486429837965432`30, 10^-20]; check["v84 DELTA_CKM_RAD frozen", Pi/3 + 3 lamC^2, 1.198231638232244084651243`30, 10^-20]; check["v84 MMU_OVER_MTAU frozen", (8/7) phi0, 0.06076794534496631692490568`30, 10^-20]; check["v84 ME_OVER_MMU frozen", (12/7) phi0^2, 0.004846725425651567674771059`30, 10^-20]; checkExact["v84 MU_OVER_MD = 55/117 exactly", 55/117 == 55/117]; check["v84 MC_OVER_MS frozen", (34/47)/phi0, 13.60499710285539356302651`30, 10^-20]; check["v84 MT_OVER_MB frozen", (3/26)/phi0^2, 40.8115130177002629681607`30, 10^-20]; check["v84 MSCAL_OVER_MBAR frozen", c3^(7/2), 0.00001256494208322844896998079`30, 10^-20]; check["v84 RHOL_OVER_MBAR4 frozen", (3/(4 Pi^2)) Exp[-2/aStar], 7.125329526706216792033797`30 10^-121, 10^-15]; checkExact["v84 theta12 variants distinct (seed < seam < nonlin band)", (1/3 - phi0/2) < (1/3 - 1/(12 Pi))]; (* ---- (v85) master cover: GL(2) covariance on the anchor plane ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L38)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)

## 2026-06-22 (the first-principles boundary, mapped: can [formula in source] be computed? can [formula in source] be first-principles? both NO, with the exact reason: v339)

[documents/changelog/sections/015-source.tex:295-310](../../../../documents/changelog/sections/015-source.tex#L295) · `section:a850fdd649c27ed35b89` · subsection

v339 ( FIRSTPRINCIPLES.BOUNDARY.01). An honest boundary audit answering two head-on questions and fabricating nothing. \ The Planck mass cannot be computed — [formula in source] is forbidden by theorem (No-Unit, v153): a mass is mass-dimension [formula in source] while every TFPT datum is dimension [formula in source] , so no dimensionless map outputs an absolute scale. It is not a gap but over-determined (gravity [f

Explicit source references:

- [FIRSTPRINCIPLES.BOUNDARY.01](../../../../verification/status_ledger.csv#L441) · explicit_claim_identifier · original status at linked ledger row
- [verification/v35_quark_qcd_boundary.py](../../../../verification/v35_quark_qcd_boundary.py#L1) · explicit_script_identifier
- [verification/v339_firstprinciples_boundary.py](../../../../verification/v339_firstprinciples_boundary.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [verification/v262_fqcd_mp_me.py](../../../../verification/v262_fqcd_mp_me.py#L1) · explicit_script_identifier
- [verification/v274_scale_overdetermination.py](../../../../verification/v274_scale_overdetermination.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)

## 2026-06-22 (next-steps round: the one open lemma literature-anchored, the Decoupling Theorem, the holomorphy discriminator hardened in Lean, and the [formula in source] budget: v336, v337, v338, FORM.CARTAN.DET.01)

[documents/changelog/sections/015-source.tex:311-341](../../../../documents/changelog/sections/015-source.tex#L311) · `section:cfd99b18e189abbc1f87` · subsection

v336 ( SEAM.EQUIV.CONTINUUM.01) — the one open lemma, literature-anchored. SEAM.EQUIV.01's only open input (the continuum OS reconstruction of the gapped quasi-free collar) is split into a CITABLE part and a narrow open part. \ continuum leg: Osborne–Stottmeister ( CFT from Lattice Fermions, doi:10.1007/s00220-022-04521-8, CMP 398 (2023) 219) give, building on the MMST (Morinelli–Morsella–Stottmeister–Tanimoto) opera

Explicit source references:

- [verification/v328_theta13_pressure.py](../../../../verification/v328_theta13_pressure.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.CONTINUUM.01](../../../../verification/status_ledger.csv#L438) · explicit_claim_identifier · original status at linked ledger row
- [DECOUPLING.THEOREM.01](../../../../verification/status_ledger.csv#L439) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1) · explicit_file_citation
- [verification/v335_seam_equiv_unify.py](../../../../verification/v335_seam_equiv_unify.py#L1) · explicit_script_identifier
- [FORM.CARTAN.DET.01](../../../../verification/status_ledger.csv#L431) · explicit_claim_identifier · original status at linked ledger row
- [verification/v338_theta13_budget.py](../../../../verification/v338_theta13_budget.py#L1) · explicit_script_identifier
- [verification/v311_gap_decoupled_measure.py](../../../../verification/v311_gap_decoupled_measure.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v330_qgamb_admissible_measure.py](../../../../verification/v330_qgamb_admissible_measure.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v337_decoupling_theorem.py](../../../../verification/v337_decoupling_theorem.py#L1) · explicit_script_identifier
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [THETA13.BUDGET.01](../../../../verification/status_ledger.csv#L440) · explicit_claim_identifier · original status at linked ledger row
- [verification/v332_qgamb_metric_sector.py](../../../../verification/v332_qgamb_metric_sector.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v337 DECOUPLING.THEOREM.01: the ambient back-reaction scale identity ==== *) Module[{ambient}, (* the largest ambient back-reaction scale 2*dim(E8)*c3^2 = 31/(4 pi^2) exactly (c3=1/(8pi)) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2240)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)

## 2026-06-22 (keystone unification + status reframe: ONE open theorem, ONE decoupled foreign problem: v335, FORM.QGEO.BW.01 qgeoSymIsCorollary)

[documents/changelog/sections/015-source.tex:342-373](../../../../documents/changelog/sections/015-source.tex#L342) · `section:2cf3ee9ae0a89a313d79` · subsection

v335 ( SEAM.EQUIV.UNIFY.01) — the keystone unification. A bird's-eye consolidation of the v308/v323/v325/v329/v333 arc that collapses the ``two open structural items'' narrative. \ QGEO.SYM.01 is a COROLLARY of SEAM.EQUIV.01 (no extra premise): a chiral conformal net has, by axiom, a M\"obius-covariant vacuum (the unique invariant positive-energy vector); rotations [formula in source] are the compact subgroup of the 

Explicit source references:

- [FORM.QGEO.BW.01](../../../../verification/status_ledger.csv#L428) · explicit_claim_identifier · original status at linked ledger row
- [verification/v332_qgamb_metric_sector.py](../../../../verification/v332_qgamb_metric_sector.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [verification/v325_pillowcase_keystone.py](../../../../verification/v325_pillowcase_keystone.py#L1) · explicit_script_identifier
- [verification/v330_qgamb_admissible_measure.py](../../../../verification/v330_qgamb_admissible_measure.py#L1) · explicit_script_identifier
- [verification/v333_cm_selection.py](../../../../verification/v333_cm_selection.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.UNIFY.01](../../../../verification/status_ledger.csv#L437) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [experiments/next.txt](../../../../experiments/next.txt#L1) · explicit_file_citation
- [verification/v335_seam_equiv_unify.py](../../../../verification/v335_seam_equiv_unify.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [verification/v329_os_gap_reduction.py](../../../../verification/v329_os_gap_reduction.py#L1) · explicit_script_identifier
- [verification/v308_seam_equiv_chain.py](../../../../verification/v308_seam_equiv_chain.py#L1) · explicit_script_identifier
- [verification/v311_gap_decoupled_measure.py](../../../../verification/v311_gap_decoupled_measure.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1) · explicit_file_citation
- [TfptCarrier.BWKeystone.conformal_net_vacuum_rotation_invariant](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L87) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ==== v325/v327: the keystone pillowcase orbifold + the cusp-weight rewrite (exact) ==== *) Module[{chiOrb, M, evs, edges, cAff, x, p23}, (* v325 QGEO.KEYSTONE.01: the flat pillowcase orbifold S^2(2,2,2,2) has chi_orb = 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2220)

## 2026-06-22 (closing round: the CM-selection mechanism (the last keystone residual), the conformal-mode resolution, and the Conway–Sloane even-unimodular side in Lean: v333, v334, FORM.CARTAN.DET.01)

[documents/changelog/sections/016-source.tex:1-22](../../../../documents/changelog/sections/016-source.tex#L1) · `section:ee232865bdd19669d0cd` · subsection

v333_cm_selection.py ( QGEO.CMSELECT.01, / ). The CM-selection mechanism for the last keystone residual: [formula in source] (the square) is the unique order-4 modulus — [formula in source] has [formula in source] and fixes [formula in source] , and an order-4 deck selects [formula in source] (vs the order-3 hexagon [formula in source] ) — AND the square is the Fekete attractor of symmetric mark-equilibration (four p

Explicit source references:

- [verification/v334_conformal_resolution.py](../../../../verification/v334_conformal_resolution.py#L1) · explicit_file_citation
- [QGEO.CMSELECT.01](../../../../verification/status_ledger.csv#L435) · explicit_claim_identifier · original status at linked ledger row
- [FORM.CARTAN.DET.01](../../../../verification/status_ledger.csv#L431) · explicit_claim_identifier · original status at linked ledger row
- [QGAMB.CONFORMAL.01](../../../../verification/status_ledger.csv#L436) · explicit_claim_identifier · original status at linked ledger row
- [verification/v333_cm_selection.py](../../../../verification/v333_cm_selection.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-22 (endgame round: the necessity of [formula in source] reduced to the order-4 CM selection, the QG metric sector characterized as the conformal-mode problem, [formula in source] and the [formula in source] commutation grounded in Lean: v331, v332, FORM.MU4COMM.01)

[documents/changelog/sections/016-source.tex:23-48](../../../../documents/changelog/sections/016-source.tex#L23) · `section:8611c18776ca96eaa8ee` · subsection

v331_necessity_of_H.py ( QGEO.NECESS.01, / ). The necessity companion to v329: a concrete Steklov (DtN) computation shows the seam [formula in source] commutes with the [formula in source] clock iff the four marks sit at the square ( [formula in source] ) — moving a mark off the square breaks [formula in source] and [formula in source] . The square has cross-ratio [formula in source] ( [formula in source] ), the uniq

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1) · explicit_file_citation
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v331_necessity_of_H.py](../../../../verification/v331_necessity_of_H.py#L1) · explicit_script_identifier
- [QGEO.NECESS.01](../../../../verification/status_ledger.csv#L432) · explicit_claim_identifier · original status at linked ledger row
- [verification/v332_qgamb_metric_sector.py](../../../../verification/v332_qgamb_metric_sector.py#L1) · explicit_file_citation
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [QGAMB.METRIC.01](../../../../verification/status_ledger.csv#L433) · explicit_claim_identifier · original status at linked ledger row
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [verification/v330_qgamb_admissible_measure.py](../../../../verification/v330_qgamb_admissible_measure.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1) · explicit_file_citation
- [verification/v267_qgeo_rigidity_minimal_axiom.py](../../../../verification/v267_qgeo_rigidity_minimal_axiom.py#L1) · explicit_script_identifier
- [verification/v329_os_gap_reduction.py](../../../../verification/v329_os_gap_reduction.py#L1) · explicit_script_identifier
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [FORM.MU4COMM.01](../../../../verification/status_ledger.csv#L434) · explicit_claim_identifier · original status at linked ledger row
- [FORM.CARTAN.DET.01](../../../../verification/status_ledger.csv#L431) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-22 (frontier round: the OS step discharged at the many-body level, the ambient measure built on the gap-decoupled sector, and the carrier Cartan determinants grounded in Lean: v329, v330, FORM.CARTAN.DET.01)

[documents/changelog/sections/016-source.tex:49-73](../../../../documents/changelog/sections/016-source.tex#L49) · `section:7d4bb4b4aaeb1717e77f` · subsection

v329_os_gap_reduction.py ( QGEO.OSGAP.01, / ). The one analytic input the v308 keystone chain still cited — ``the OS-reconstructed bulk gap [formula in source] the transfer gap'' — is discharged at the many-body level: the OS/Euclidean Hamiltonian is the second quantization [formula in source] , whose spectrum is the set of sums of single-mode energies, so the bulk gap [formula in source] the smallest positive single

Explicit source references:

- [QGEO.OSGAP.01](../../../../verification/status_ledger.csv#L429) · explicit_claim_identifier · original status at linked ledger row
- [verification/v308_seam_equiv_chain.py](../../../../verification/v308_seam_equiv_chain.py#L1) · explicit_script_identifier
- [FORM.CARTAN.DET.01](../../../../verification/status_ledger.csv#L431) · explicit_claim_identifier · original status at linked ledger row
- [verification/v275_qgamb_roadmap.py](../../../../verification/v275_qgamb_roadmap.py#L1) · explicit_script_identifier
- [verification/v330_qgamb_admissible_measure.py](../../../../verification/v330_qgamb_admissible_measure.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1) · explicit_file_citation
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [verification/v329_os_gap_reduction.py](../../../../verification/v329_os_gap_reduction.py#L1) · explicit_file_citation
- [QGAMB.MEASURE.01](../../../../verification/status_ledger.csv#L430) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)

## 2026-06-22 (next-steps round: the keystone collapsed to one shared premise (Lean [formula in source] one citable theorem), the [formula in source] solver suite, the cusp weight derived from a minimal rewrite, and the [formula in source] pressure point: FORM.QGEO.BW.01, v325, v326, v327, v328)

[documents/changelog/sections/016-source.tex:74-108](../../../../documents/changelog/sections/016-source.tex#L74) · `section:f3b90b032a2851e13827` · subsection

BWKeystone.lean ( FORM.QGEO.BW.01, Lean 4, / ). The v323 Bisognano–Wichmann linkage formalised: the nodes [formula in source] (= QGEO.SYM.01) composed over the v308 chain. The theorem bedrockReducesToRotationInvariance shows the WHOLE bedrock QGEO.SYM.01 reduces to the SINGLE shared open premise RotationInvariantVacuum — the two open bedrock items collapse to one — with \#print axioms confirming the residual [formula

Explicit source references:

- [verification/v307_data_watchdog.py](../../../../verification/v307_data_watchdog.py#L1) · explicit_script_identifier
- [verification/wolfram/tfpt_readouts_extension.wl](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1) · explicit_file_citation
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [GATE.WOLFRAM.02](../../../../verification/status_ledger.csv#L168) · explicit_claim_identifier · original status at linked ledger row
- [verification/v324_hypergraph_fiber.py](../../../../verification/v324_hypergraph_fiber.py#L1) · explicit_script_identifier
- [verification/v268_theta13_carrier_trace.py](../../../../verification/v268_theta13_carrier_trace.py#L1) · explicit_script_identifier
- [QGEO.KEYSTONE.01](../../../../verification/status_ledger.csv#L424) · explicit_claim_identifier · original status at linked ledger row
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [FR.SUITE.01](../../../../verification/status_ledger.csv#L425) · explicit_claim_identifier · original status at linked ledger row
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [HYP.REWRITE.01](../../../../verification/status_ledger.csv#L426) · explicit_claim_identifier · original status at linked ledger row
- [FORM.QGEO.BW.01](../../../../verification/status_ledger.csv#L428) · explicit_claim_identifier · original status at linked ledger row
- [verification/v309_modular_bedrock.py](../../../../verification/v309_modular_bedrock.py#L1) · explicit_script_identifier
- [verification/v326_ftransfer_suite.py](../../../../verification/v326_ftransfer_suite.py#L1) · explicit_script_identifier
- [verification/v328_theta13_pressure.py](../../../../verification/v328_theta13_pressure.py#L1) · explicit_file_citation
- [verification/v327_hypergraph_rewrite.py](../../../../verification/v327_hypergraph_rewrite.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1) · explicit_file_citation
- [verification/v325_pillowcase_keystone.py](../../../../verification/v325_pillowcase_keystone.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.TH13.PRESSURE.01](../../../../verification/status_ledger.csv#L427) · explicit_claim_identifier · original status at linked ledger row
- [verification/v308_seam_equiv_chain.py](../../../../verification/v308_seam_equiv_chain.py#L1) · explicit_script_identifier
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [(* ==== v325/v327: the keystone pillowcase orbifold + the cusp-weight rewrite (exact) ==== *) Module[{chiOrb, M, evs, edges, cAff, x, p23}, (* v325 QGEO.KEYSTONE.01: the flat pillowcase orbifold S^2(2,2,2,2) has chi_orb = 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2220)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)

## 2026-06-22 (consistency + de-accretion editorial pass: current-state alignment across papers, website and ledger; no new modules)

[documents/changelog/sections/016-source.tex:109-138](../../../../documents/changelog/sections/016-source.tex#L109) · `section:ac6f5be914309816a43d` · subsection

Keystone naming reconciled to SEAM.EQUIV.01. Following v323/ QGEO.BW.01 (the deck premise is downstream of the seam being a chiral net), the single named open keystone is now SEAM.EQUIV.01 everywhere, with QGEO.SYM.01 stated as its downstream conformal-deck face. The ledger row QGEO.SYM.01 was updated (it no longer calls itself ``the single structural residual of the whole theory''; it now depends on SEAM.EQUIV.01/ Q

Explicit source references:

- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [verification/v213_ftransfer_functor.py](../../../../verification/v213_ftransfer_functor.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [FORM.SEAMEQUIV.01](../../../../verification/status_ledger.csv#L423) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v324_hypergraph_fiber.py](../../../../verification/v324_hypergraph_fiber.py#L1) · explicit_script_identifier
- [QGEO.BW.01](../../../../verification/status_ledger.csv#L421) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)

## 2026-06-22 (external-review pass: a registry bug fix, the NA62 2026 rare-kaon update, CP-phase prose hygiene, and three firewall/visualisation enhancements: v202, v203, v305, v307, v321)

[documents/changelog/sections/016-source.tex:139-173](../../../../documents/changelog/sections/016-source.tex#L139) · `section:ddeb7ff0b27d4750ff23` · subsection

Bug fix — [formula in source] display value. The predictions table ( tex-artefacts/predictions.tex) showed [formula in source] , but that formula evaluates to [formula in source] (the canonical frozen DELTA_CKM_RAD [formula in source] rad, used by v88/ v202/ FLAV.CP.01 everywhere else). Corrected to [formula in source] . An external review correctly flagged the inconsistency; it was an isolated display typo (the webs

Explicit source references:

- [verification/v315_coxeter_coupling.py](../../../../verification/v315_coxeter_coupling.py#L1) · explicit_script_identifier
- [verification/v203_eht_achromatic.py](../../../../verification/v203_eht_achromatic.py#L1) · explicit_file_citation
- [verification/v202_rare_kaon.py](../../../../verification/v202_rare_kaon.py#L1) · explicit_script_identifier
- [FLAV.CP.01](../../../../verification/status_ledger.csv#L162) · explicit_claim_identifier · original status at linked ledger row
- [verification/v305_witness_independence.py](../../../../verification/v305_witness_independence.py#L1) · explicit_script_identifier
- [verification/v307_data_watchdog.py](../../../../verification/v307_data_watchdog.py#L1) · explicit_script_identifier
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [FR.RAREKAON.01](../../../../verification/status_ledger.csv#L278) · explicit_claim_identifier · original status at linked ledger row
- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [verification/v306_seed_crossval.py](../../../../verification/v306_seed_crossval.py#L1) · explicit_script_identifier
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier
- [verification/v321_killtest_board.py](../../../../verification/v321_killtest_board.py#L1) · explicit_script_identifier
- [verification/make_figures.py](../../../../verification/make_figures.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v203) HOR.EHT.01: the EHT polarization coupling 16 c3^4 = 1/(256 pi^4) = delta_top/3 ---- *) Module[{c3, dtop}, c3 = 1/(8 Pi); dtop = 48 c3^4; (* = 3/(256 pi^4) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1685)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)

## 2026-06-22 (Wolfram mirror of the arithmetic arc [formula in source] three sharpening steps: the CP-lock made quantitative, the Bisognano–Wichmann keystone, the minimal hypergraph fibre: v322, v323, v324)

[documents/changelog/sections/016-source.tex:174-216](../../../../documents/changelog/sections/016-source.tex#L174) · `section:029b7dd988521b5ffc7e` · subsection

Wolfram mirror of the cyclotomic/Galois arithmetic arc (the independent second path). The exact algebraic results of the arc are now mirrored in verification/wolfram/tfpt_readouts_extension.wl (ten new checkExact blocks, [formula in source] , all passing): v313 (the affine- [formula in source] characteristic polynomial with the golden factor [formula in source] ; the [formula in source] atoms as [formula in source] ;

Explicit source references:

- [verification/v315_coxeter_coupling.py](../../../../verification/v315_coxeter_coupling.py#L1) · explicit_script_identifier
- [verification/v320_galois_cp_relation.py](../../../../verification/v320_galois_cp_relation.py#L1) · explicit_script_identifier
- [verification/v313_golden_atoms_spectral.py](../../../../verification/v313_golden_atoms_spectral.py#L1) · explicit_script_identifier
- [verification/v309_modular_bedrock.py](../../../../verification/v309_modular_bedrock.py#L1) · explicit_script_identifier
- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_file_citation
- [verification/wolfram/tfpt_readouts_extension.wl](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1) · explicit_file_citation
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [GATE.WOLFRAM.02](../../../../verification/status_ledger.csv#L168) · explicit_claim_identifier · original status at linked ledger row
- [verification/v317_galois_family.py](../../../../verification/v317_galois_family.py#L1) · explicit_script_identifier
- [verification/v318_arithmetic_capstone.py](../../../../verification/v318_arithmetic_capstone.py#L1) · explicit_script_identifier
- [verification/v322_cp_lock_sharpened.py](../../../../verification/v322_cp_lock_sharpened.py#L1) · explicit_file_citation
- [verification/v316_galois_readout.py](../../../../verification/v316_galois_readout.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.BW.01](../../../../verification/status_ledger.csv#L421) · explicit_claim_identifier · original status at linked ledger row
- [verification/v324_hypergraph_fiber.py](../../../../verification/v324_hypergraph_fiber.py#L1) · explicit_script_identifier
- [verification/v308_seam_equiv_chain.py](../../../../verification/v308_seam_equiv_chain.py#L1) · explicit_script_identifier
- [GALOIS.CP.SHARPEN.01](../../../../verification/status_ledger.csv#L420) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [HYP.FIBER.01](../../../../verification/status_ledger.csv#L422) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* v316 GALOIS.READOUT.01 -- CP phases are the family-factor cyclotomic data *) z6 = Exp[I Pi/3]; z30 = Exp[2 Pi I/30]; checkExact["v316 GALOIS.READOUT.01: the CP unit rho=zeta6=zeta30^5 (the order-6 family factor c^5); rho^4=-rho (sheet flip); Gal(Q(zeta6)/Q)=Z2 with zeta6->zeta6^5=conj(zeta6) = CP conjugation", Simplify[z6 - z30^5] == 0 && Simplify[z6^4 + z6] == 0 && Simplify[Conjugate[z6] - z6^5] == 0]; (* v317 GALOIS.FAMILY.01 -- the three generations are the mu3 orbit, Galois-refined 1+2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2206)
- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)

## 2026-06-22 (the forward kill-test board: the decisive upcoming measurements ranked, each locked to a freeze row — incl. the new Galois-CP relation: v321)

[documents/changelog/sections/016-source.tex:217-228](../../../../documents/changelog/sections/016-source.tex#L217) · `section:77994b345651d1c08987` · subsection

v321_killtest_board.py ( KILL.BOARD.01, ). The forward companion to v307 (the current-data board): the decisive upcoming measurements, ranked and each locked to a freeze_file.csv kill row – \#1 JUNO [formula in source] (fastest), \#2 CMB-S4/LiteBIRD [formula in source] (kill [formula in source] ), \#3 DESI/Euclid [formula in source] (kill [formula in source] ), \#4 DUNE/Hyper-K [formula in source] (the new v320 Galoi

Explicit source references:

- [verification/v320_galois_cp_relation.py](../../../../verification/v320_galois_cp_relation.py#L1) · explicit_script_identifier
- [KILL.BOARD.01](../../../../verification/status_ledger.csv#L419) · explicit_claim_identifier · original status at linked ledger row
- [verification/v307_data_watchdog.py](../../../../verification/v307_data_watchdog.py#L1) · explicit_script_identifier
- [verification/freeze_file.csv](../../../../verification/freeze_file.csv#L1) · explicit_file_citation
- [verification/v321_killtest_board.py](../../../../verification/v321_killtest_board.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)

## 2026-06-22 (Lean: the SEAM.EQUIV.01 composition chain formalised — the keystone residual machine-pinned to the named cited steps: FORM.SEAMEQUIV.01)

[documents/changelog/sections/016-source.tex:229-244](../../../../documents/changelog/sections/016-source.tex#L229) · `section:d2dce761d475a2f11d08` · subsection

SeamEquivChain.lean ( FORM.SEAMEQUIV.01, Lean 4, / ). A Lean 4 mirror of the v308 closing chain: the four nodes [formula in source] assembled as a well-typed composition theorem seamEquivChain, with the three cited literature steps (Kitaev free-fermion invertibility; M\"uger / Kawahigashi–Longo–M\"uger holomorphy; Conway–Sloane [formula in source] uniqueness) as named axioms and the carrier recovery gap (the OS step)

Explicit source references:

- [TfptCarrier.SeamEquivChain.recovery_gap](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L64) · explicit_lean_symbol
- [FORM.SEAMEQUIV.01](../../../../verification/status_ledger.csv#L423) · explicit_claim_identifier · original status at linked ledger row
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1) · explicit_file_citation
- [verification/v308_seam_equiv_chain.py](../../../../verification/v308_seam_equiv_chain.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)

## 2026-06-22 (a NEW falsifiable prediction from the Galois structure: the two CP phases are locked, [formula in source] : v320)

[documents/changelog/sections/016-source.tex:245-259](../../../../documents/changelog/sections/016-source.tex#L245) · `section:d200c6e6e5dab4f9f985` · subsection

v320_galois_cp_relation.py ( GALOIS.CP.PREDICT.01, / / ). The v316 follow-up turned into a testable cross-prediction. \ both leading CP phases are powers of the one hexagonal unit [formula in source] of the family Galois factor: [formula in source] ( [formula in source] ), [formula in source] ( [formula in source] ), and [formula in source] locks them as [formula in source] (the [formula in source] sheet flip); \ thi

Explicit source references:

- [verification/v320_galois_cp_relation.py](../../../../verification/v320_galois_cp_relation.py#L1) · explicit_script_identifier
- [verification/freeze_file.csv](../../../../verification/freeze_file.csv#L1) · explicit_file_citation
- [GALOIS.CP.PREDICT.01](../../../../verification/status_ledger.csv#L418) · explicit_claim_identifier · original status at linked ledger row
- [verification/v319_translation_clock.py](../../../../verification/v319_translation_clock.py#L1) · explicit_script_identifier
- [verification/v313_golden_atoms_spectral.py](../../../../verification/v313_golden_atoms_spectral.py#L1) · explicit_script_identifier
- [verification/v316_galois_readout.py](../../../../verification/v316_galois_readout.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v316 GALOIS.READOUT.01 -- CP phases are the family-factor cyclotomic data *) z6 = Exp[I Pi/3]; z30 = Exp[2 Pi I/30]; checkExact["v316 GALOIS.READOUT.01: the CP unit rho=zeta6=zeta30^5 (the order-6 family factor c^5); rho^4=-rho (sheet flip); Gal(Q(zeta6)/Q)=Z2 with zeta6->zeta6^5=conj(zeta6) = CP conjugation", Simplify[z6 - z30^5] == 0 && Simplify[z6^4 + z6] == 0 && Simplify[Conjugate[z6] - z6^5] == 0]; (* v317 GALOIS.FAMILY.01 -- the three generations are the mu3 orbit, Galois-refined 1+2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2206)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)
- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)

## 2026-06-22 (the translation clock: the discrete [formula in source] dynamic bridge is the order- [formula in source] Coxeter element, a clock with two coprime hands [formula in source] , read law-inclusive ( [formula in source] ) or live-only ( [formula in source] ): v319)

[documents/changelog/sections/016-source.tex:260-283](../../../../documents/changelog/sections/016-source.tex#L260) · `section:cc398ba7e3e94c7addf2` · subsection

v319_translation_clock.py ( TRANSLATE.CLOCK.01, / ). A synthesis of the v313– v318 arc with v124/ v55, answering the question ``is the static [formula in source] dynamic translation a clock running [formula in source] or [formula in source] ?''. \ the only object holding both the static carrier ( [formula in source] ) and the dynamic family (rational) data is the order- [formula in source] Coxeter element ( v314); [f

Explicit source references:

- [verification/v318_arithmetic_capstone.py](../../../../verification/v318_arithmetic_capstone.py#L1) · explicit_script_identifier
- [verification/v319_translation_clock.py](../../../../verification/v319_translation_clock.py#L1) · explicit_script_identifier
- [verification/v315_coxeter_coupling.py](../../../../verification/v315_coxeter_coupling.py#L1) · explicit_script_identifier
- [verification/v316_galois_readout.py](../../../../verification/v316_galois_readout.py#L1) · explicit_script_identifier
- [TRANSLATE.CLOCK.01](../../../../verification/status_ledger.csv#L417) · explicit_claim_identifier · original status at linked ledger row
- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [verification/v56_unique_attractor.py](../../../../verification/v56_unique_attractor.py#L1) · explicit_script_identifier
- [verification/v313_golden_atoms_spectral.py](../../../../verification/v313_golden_atoms_spectral.py#L1) · explicit_script_identifier
- [verification/v124_resummed_clock.py](../../../../verification/v124_resummed_clock.py#L1) · explicit_script_identifier
- [verification/v55_coxeter_cycle.py](../../../../verification/v55_coxeter_cycle.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v316 GALOIS.READOUT.01 -- CP phases are the family-factor cyclotomic data *) z6 = Exp[I Pi/3]; z30 = Exp[2 Pi I/30]; checkExact["v316 GALOIS.READOUT.01: the CP unit rho=zeta6=zeta30^5 (the order-6 family factor c^5); rho^4=-rho (sheet flip); Gal(Q(zeta6)/Q)=Z2 with zeta6->zeta6^5=conj(zeta6) = CP conjugation", Simplify[z6 - z30^5] == 0 && Simplify[z6^4 + z6] == 0 && Simplify[Conjugate[z6] - z6^5] == 0]; (* v317 GALOIS.FAMILY.01 -- the three generations are the mu3 orbit, Galois-refined 1+2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2206)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)
- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)

## 2026-06-21 (capstone: the SM structural sector is [formula in source] Galois [formula in source] , and the complete input is [formula in source] — zero dimensionless free parameters: v318)

[documents/changelog/sections/016-source.tex:284-299](../../../../documents/changelog/sections/016-source.tex#L284) · `section:31a155495fcd43cf1264` · subsection

v318_arithmetic_capstone.py ( ARITH.CAPSTONE.01, / ). The synthesis of the v313– v317 arc. \ the SM structural sector (the [formula in source] generations, the [formula in source] CP phases, their orbit/hierarchy) is the cyclotomic field [formula in source] with Galois group [formula in source] (degree [formula in source] rank [formula in source] , [formula in source] ), forced by the anchor atoms [formula in source]

Explicit source references:

- [ARITH.CAPSTONE.01](../../../../verification/status_ledger.csv#L415) · explicit_claim_identifier · original status at linked ledger row
- [ARCH.CORE.01](../../../../verification/status_ledger.csv#L136) · explicit_claim_identifier · original status at linked ledger row
- [verification/v317_galois_family.py](../../../../verification/v317_galois_family.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v318_arithmetic_capstone.py](../../../../verification/v318_arithmetic_capstone.py#L1) · explicit_file_citation
- [verification/v313_golden_atoms_spectral.py](../../../../verification/v313_golden_atoms_spectral.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* v316 GALOIS.READOUT.01 -- CP phases are the family-factor cyclotomic data *) z6 = Exp[I Pi/3]; z30 = Exp[2 Pi I/30]; checkExact["v316 GALOIS.READOUT.01: the CP unit rho=zeta6=zeta30^5 (the order-6 family factor c^5); rho^4=-rho (sheet flip); Gal(Q(zeta6)/Q)=Z2 with zeta6->zeta6^5=conj(zeta6) = CP conjugation", Simplify[z6 - z30^5] == 0 && Simplify[z6^4 + z6] == 0 && Simplify[Conjugate[z6] - z6^5] == 0]; (* v317 GALOIS.FAMILY.01 -- the three generations are the mu3 orbit, Galois-refined 1+2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2206)

## 2026-06-21 (are the 3 generations a [formula in source] /Galois orbit? Yes ( [formula in source] ), Galois-refined [formula in source] with the fixed generation [formula in source] the recovery attractor: v317)

[documents/changelog/sections/016-source.tex:300-314](../../../../documents/changelog/sections/016-source.tex#L300) · `section:fa6e96662b31faa3de47` · subsection

v317_galois_family.py ( GALOIS.FAMILY.01, / ). The v316 follow-up to the generation structure. \ the three cusp weights [formula in source] (with [formula in source] , the [formula in source] exponents) are the cube roots of unity [formula in source] under [formula in source] , and the cyclic family symmetry [formula in source] is a transitive [formula in source] orbit (the family IS the cube-root orbit); \ the trans

Explicit source references:

- [verification/v317_galois_family.py](../../../../verification/v317_galois_family.py#L1) · explicit_file_citation
- [verification/v316_galois_readout.py](../../../../verification/v316_galois_readout.py#L1) · explicit_script_identifier
- [GALOIS.FAMILY.01](../../../../verification/status_ledger.csv#L414) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v316 GALOIS.READOUT.01 -- CP phases are the family-factor cyclotomic data *) z6 = Exp[I Pi/3]; z30 = Exp[2 Pi I/30]; checkExact["v316 GALOIS.READOUT.01: the CP unit rho=zeta6=zeta30^5 (the order-6 family factor c^5); rho^4=-rho (sheet flip); Gal(Q(zeta6)/Q)=Z2 with zeta6->zeta6^5=conj(zeta6) = CP conjugation", Simplify[z6 - z30^5] == 0 && Simplify[z6^4 + z6] == 0 && Simplify[Conjugate[z6] - z6^5] == 0]; (* v317 GALOIS.FAMILY.01 -- the three generations are the mu3 orbit, Galois-refined 1+2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2206)

## 2026-06-21 (does the Galois [formula in source] organize the readouts? Yes — the CP phases are the family-factor cyclotomic data, Galois [formula in source] CP conjugation: v316)

[documents/changelog/sections/016-source.tex:315-330](../../../../documents/changelog/sections/016-source.tex#L315) · `section:49c4830cbc40c1211137` · subsection

v316_galois_readout.py ( GALOIS.READOUT.01, / ). The v315 follow-up to phenomenology: does the Galois coupling [formula in source] reach the physics? \ it does, through the family factor — the hexagonal CP unit [formula in source] is exactly the order- [formula in source] factor [formula in source] of v315 (the carrier being [formula in source] ); \ the leading CP phases are its cyclotomic arguments [formula in sourc

Explicit source references:

- [verification/v233_cp_triality_phase.py](../../../../verification/v233_cp_triality_phase.py#L1) · explicit_script_identifier
- [GALOIS.READOUT.01](../../../../verification/status_ledger.csv#L413) · explicit_claim_identifier · original status at linked ledger row
- [verification/v315_coxeter_coupling.py](../../../../verification/v315_coxeter_coupling.py#L1) · explicit_script_identifier
- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [verification/v231_cp_mu6_phases.py](../../../../verification/v231_cp_mu6_phases.py#L1) · explicit_script_identifier
- [verification/v316_galois_readout.py](../../../../verification/v316_galois_readout.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [(* v316 GALOIS.READOUT.01 -- CP phases are the family-factor cyclotomic data *) z6 = Exp[I Pi/3]; z30 = Exp[2 Pi I/30]; checkExact["v316 GALOIS.READOUT.01: the CP unit rho=zeta6=zeta30^5 (the order-6 family factor c^5); rho^4=-rho (sheet flip); Gal(Q(zeta6)/Q)=Z2 with zeta6->zeta6^5=conj(zeta6) = CP conjugation", Simplify[z6 - z30^5] == 0 && Simplify[z6^4 + z6] == 0 && Simplify[Conjugate[z6] - z6^5] == 0]; (* v317 GALOIS.FAMILY.01 -- the three generations are the mu3 orbit, Galois-refined 1+2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2206)
- [(* v225 dual normal frame (d,n) and oriented volume *) d = av.Inverse[RRm]; nvec = {5, -9, 6}; KKm = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Lm = KKm + QQm; checkExact["v225 DUAL.FRAME.01: d=a.R^{-1}=(-1/2,-1/2,1)=-1/2(1,1,-2) (Nariai normal; " <> "d.1=0, d.a=1); n=(5,-9,6) with n.R=(det R,0,0)=(8,0,0), n.L=(det L,0,0)=(20,0,0); " <> "oriented volume det(1,d,n)=21=N_fam*scalaron=3*7", d == {-1/2, -1/2, 1} && d == -1/2 {1, 1, -2} && d.one == 0 && d.av == 1 && nvec.RRm == {Det[RRm], 0, 0} == {8, 0, 0} && nvec.Lm == {Det[Lm], 0, 0} == {20, 0, 0} && Det[{{1, 1, 1}, d, nvec}] == 21 == 3*7]; ]; (* ==== v231: both CP phases are mu6 powers of one hexagonal unit, split by the sheet ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1861)

## 2026-06-21 (couple or factorize? the order-30 Coxeter element couples the carrier and family sectors as a cyclotomic compositum, Galois [formula in source] : v315)

[documents/changelog/sections/016-source.tex:331-347](../../../../documents/changelog/sections/016-source.tex#L331) · `section:03d2cc780ce0cfabf94c` · subsection

v315_coxeter_coupling.py ( COX.COUPLE.01, / ). Answers the v314 question — does [formula in source] couple the carrier ( [formula in source] -fold, golden, [formula in source] ) and family ( [formula in source] , rational) sectors, or just factorize? \ the cyclic group factorizes: [formula in source] (direct product, group-decoupled, in line with the v314 field obstruction); \ the [formula in source] exponents [formu

Explicit source references:

- [verification/v223_coxeter_totative_clock.py](../../../../verification/v223_coxeter_totative_clock.py#L1) · explicit_script_identifier
- [COX.COUPLE.01](../../../../verification/status_ledger.csv#L412) · explicit_claim_identifier · original status at linked ledger row
- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [verification/v315_coxeter_coupling.py](../../../../verification/v315_coxeter_coupling.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)
- [(* v223 Coxeter totative clock: (Z/30)^x = E8 exponents, order-4 element 7 *) checkExact["v223 COX.CLOCK.01: (Z/30)^x = {1,7,11,13,17,19,23,29} = E8 exponents, " <> "phi(30)=8=rank E8, 30=2*3*5; mult-by-7 has order 4 (7^2=19, 7^4=1 mod 30): a " <> "mu4 clock <7>={1,7,13,19}; the conjugate pairs split into 4 invariant planes", Select[Range[29], CoprimeQ[#, 30] &] == {1, 7, 11, 13, 17, 19, 23, 29} && EulerPhi[30] == 8 && PowerMod[7, 2, 30] == 19 && PowerMod[7, 4, 30] == 1 && Sort[Mod[7^Range[0, 3], 30]] == {1, 7, 13, 19} && Length[Union[Sort /@ ({#, 30 - #} & /@ {1, 7, 11, 13, 17, 19, 23, 29})]] == 4]; (* v227 degree/exponent channel split: 248 = 120 + 128 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1804)

## 2026-06-21 (do the discrete-kernel and dynamic rates translate? An exact number-field split [formula in source] vs [formula in source] : v314)

[documents/changelog/sections/016-source.tex:348-364](../../../../documents/changelog/sections/016-source.tex#L348) · `section:a444fd35a837e55b2dcd` · subsection

v314_rate_translation.py ( RATE.TRANSLATE.01, / ). Answers, exactly, whether the discrete kernel (the affine- [formula in source] network, carrying the golden ratio) and the dynamic part (the seam transfer, carrying the recovery rate [formula in source] ) translate. \ FIELD SPLIT: the adjacency spectrum is the rational part [formula in source] plus the golden part [formula in source] , while the transfer spectrum [fo

Explicit source references:

- [verification/v314_rate_translation.py](../../../../verification/v314_rate_translation.py#L1) · explicit_script_identifier
- [RATE.TRANSLATE.01](../../../../verification/status_ledger.csv#L416) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v314 RATE.TRANSLATE.01 -- the number-field split between discrete kernel and dynamic rates *) checkExact["v314 RATE.TRANSLATE.01: the discrete kernel rates {1/2,1/3,2/3,(2/3)^6} are rational (Q); the dynamic golden rate uses phi=2cos(pi/5), MinimalPolynomial x^2-x-1, living in Q(sqrt5) = the real subfield of Q(zeta5) ([Q(zeta5):Q]=4); since Q(sqrt5) cap Q = Q, exact translation acts only on the rational (2,3)-fold sector", Element[1/2, Rationals] && Element[(2/3)^6, Rationals] && MinimalPolynomial[2 Cos[Pi/5], x] == x^2 - x - 1 && EulerPhi[5] == 4 && Simplify[2 Cos[2 Pi/5] - (Sqrt[5] - 1)/2] == 0]; (* v315 COX.COUPLE.01 -- the order-30 Coxeter sectors couple as a cyclotomic field *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2195)

## 2026-06-21 (the golden ratio made precise: the [formula in source] atoms are the affine- [formula in source] network spectral angles, [formula in source] the [formula in source] signature: v313)

[documents/changelog/sections/017-source.tex:1-18](../../../../documents/changelog/sections/017-source.tex#L1) · `section:f31ad742de6c0cadfda1` · subsection

v313_golden_atoms_spectral.py ( GOLD.ATOMS.01, / ). A follow-up to v312's observation, made exact. \ the affine- [formula in source] adjacency characteristic polynomial factors as [formula in source] , so the golden minimal polynomial [formula in source] divides it and [formula in source] is an exact eigenvalue; \ the non-trivial eigenvalues are [formula in source] for exactly [formula in source] ( [formula in source

Explicit source references:

- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [verification/v313_golden_atoms_spectral.py](../../../../verification/v313_golden_atoms_spectral.py#L1) · explicit_file_citation
- [verification/v63_seam_engineering_index.py](../../../../verification/v63_seam_engineering_index.py#L1) · explicit_script_identifier
- [verification/v305_witness_independence.py](../../../../verification/v305_witness_independence.py#L1) · explicit_script_identifier
- [GOLD.ATOMS.01](../../../../verification/status_ledger.csv#L411) · explicit_claim_identifier · original status at linked ledger row
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v63) Seam-Engineering Index: exact closed form ---- *) checkExact["||V||=248 c3^2=31/(8pi^2); 2||V||=31/(4pi^2); 248=dim E8, 31=1+h^v(E8)", With[{c3 = 1/(8 Pi)}, Simplify[248 c3^2 - 31/(8 Pi^2)] == 0 && 248/8 == 31 == 1 + 30]]; checkExact["Xi = 2||V||/Delta = 31/(24 pi^2 log(3/2)); Delta_eff = Delta - 2||V|| > 0", Simplify[(31/(4 Pi^2))/(6 Log[3/2]) - 31/(24 Pi^2 Log[3/2])] == 0 && N[6 Log[3/2] - 31/(4 Pi^2)] > 1]; (* ---- (v66) compiler atoms = E8 Casimir invariant degrees ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L300)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)

## 2026-06-21 (TOE-roadmap solver round: the SEAM.EQUIV.01 keystone certificate, the modular bedrock, the carrier [formula in source] SM closure, the gap-decoupled measure, and the sharpened hypergraph substrate: v308– v312)

[documents/changelog/sections/017-source.tex:19-55](../../../../documents/changelog/sections/017-source.tex#L19) · `section:796200681c870006983a` · subsection

v308_seam_equiv_chain.py ( SEAM.EQUIV.CHAIN.01, / ). TOE attack point 1: the keystone ``the raw seam-Calder\'on net is the holomorphic [formula in source] [formula in source] net'' assembled into ONE well-typed logical chain [formula in source] , with the exact discriminators [formula in source] vs [formula in source] , the carrier tower [formula in source] and [formula in source] all machine-checked; the input gap i

Explicit source references:

- [QGEO.MODHAM.01](../../../../verification/status_ledger.csv#L407) · explicit_claim_identifier · original status at linked ledger row
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [HYP.INJECT.01](../../../../verification/status_ledger.csv#L410) · explicit_claim_identifier · original status at linked ledger row
- [verification/v308_seam_equiv_chain.py](../../../../verification/v308_seam_equiv_chain.py#L1) · explicit_script_identifier
- [verification/v312_hypergraph_substrate.py](../../../../verification/v312_hypergraph_substrate.py#L1) · explicit_script_identifier
- [QGAMB.CLUSTER.01](../../../../verification/status_ledger.csv#L409) · explicit_claim_identifier · original status at linked ledger row
- [verification/v309_modular_bedrock.py](../../../../verification/v309_modular_bedrock.py#L1) · explicit_file_citation
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v311_gap_decoupled_measure.py](../../../../verification/v311_gap_decoupled_measure.py#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.CHAIN.01](../../../../verification/status_ledger.csv#L406) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [CAR.SM.ANOM.01](../../../../verification/status_ledger.csv#L408) · explicit_claim_identifier · original status at linked ledger row
- [verification/v310_carrier_sm_anomaly.py](../../../../verification/v310_carrier_sm_anomaly.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)

## 2026-06-21 (adversarial-review follow-ups: a structural anti-numerology firewall, an out-of-sample seed cross-validation, an operational data watchdog, and the Target-A holomorphy kill test: v305– v307)

[documents/changelog/sections/017-source.tex:56-91](../../../../documents/changelog/sections/017-source.tex#L56) · `section:d21a62fafd64ff24f0b6` · subsection

v305_witness_independence.py ( WITNESS.ECON.01, ). The structural anti-numerology firewall complementing the v100 phenomenological null test, against the sharpest self-deception worry (``the same integer counted many times as if independent''). Every headline integer ( [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source

Explicit source references:

- [verification/v305_witness_independence.py](../../../../verification/v305_witness_independence.py#L1) · explicit_script_identifier
- [WITNESS.ECON.01](../../../../verification/status_ledger.csv#L401) · explicit_claim_identifier · original status at linked ledger row
- [verification/v237_seam_sre_closure.py](../../../../verification/v237_seam_sre_closure.py#L1) · explicit_script_identifier
- [DATA.WATCHDOG.01](../../../../verification/status_ledger.csv#L405) · explicit_claim_identifier · original status at linked ledger row
- [verification/v307_data_watchdog.py](../../../../verification/v307_data_watchdog.py#L1) · explicit_file_citation
- [SEED.CROSSVAL.01](../../../../verification/status_ledger.csv#L402) · explicit_claim_identifier · original status at linked ledger row
- [verification/v143_graded_frobenius.py](../../../../verification/v143_graded_frobenius.py#L1) · explicit_script_identifier
- [verification/v84_frozen_registry.py](../../../../verification/v84_frozen_registry.py#L1) · explicit_script_identifier
- [verification/v306_seed_crossval.py](../../../../verification/v306_seed_crossval.py#L1) · explicit_file_citation
- [verification/freeze_file.csv](../../../../verification/freeze_file.csv#L1) · explicit_file_citation
- [verification/v83_e8net_holomorphic_uniqueness.py](../../../../verification/v83_e8net_holomorphic_uniqueness.py#L1) · explicit_script_identifier
- [verification/v301_route_a_invertible.py](../../../../verification/v301_route_a_invertible.py#L1) · explicit_script_identifier
- [verification/v100_numerology_null_mc.py](../../../../verification/v100_numerology_null_mc.py#L1) · explicit_script_identifier
- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v84) frozen registry decimals recompute from the axioms ---- *) phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); FU1[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 41 Log[1/phiseam[a]]; aStar = a /. FindRoot[FU1[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; check["v84 ALPHA_INV frozen", 1/aStar, 137.0359992168407125035379`30, 10^-20]; lamC = Sqrt[phi0 (1 - phi0)]; check["v84 SIN2_THETA12_SEED frozen", 1/3 - phi0/2, 0.3067473572449105696786871`30, 10^-20]; check["v84 SIN2_THETA13 frozen", phi0 Exp[-5/6], 0.02310843515888110429328466`30, 10^-20]; check["v84 BETA_BIREFRINGENCE_DEG frozen", (phi0/(4 Pi)) (180/Pi), 0.2424350309009295284924315`30, 10^-20]; check["v84 OMEGA_B frozen", (1 - 1/(4 Pi)) phi0, 0.04894066266545011220054565`30, 10^-20]; check["v84 LAMBDA_C frozen", lamC, 0.2243762368847217731120972`30, 10^-20]; check["v84 S23_CKM frozen", phi0/(1 + lamC), 0.04342778843220215630289116`30, 10^-20]; check["v84 S13_CKM frozen", lamC^3/3, 0.003765384454486429837965432`30, 10^-20]; check["v84 DELTA_CKM_RAD frozen", Pi/3 + 3 lamC^2, 1.198231638232244084651243`30, 10^-20]; check["v84 MMU_OVER_MTAU frozen", (8/7) phi0, 0.06076794534496631692490568`30, 10^-20]; check["v84 ME_OVER_MMU frozen", (12/7) phi0^2, 0.004846725425651567674771059`30, 10^-20]; checkExact["v84 MU_OVER_MD = 55/117 exactly", 55/117 == 55/117]; check["v84 MC_OVER_MS frozen", (34/47)/phi0, 13.60499710285539356302651`30, 10^-20]; check["v84 MT_OVER_MB frozen", (3/26)/phi0^2, 40.8115130177002629681607`30, 10^-20]; check["v84 MSCAL_OVER_MBAR frozen", c3^(7/2), 0.00001256494208322844896998079`30, 10^-20]; check["v84 RHOL_OVER_MBAR4 frozen", (3/(4 Pi^2)) Exp[-2/aStar], 7.125329526706216792033797`30 10^-121, 10^-15]; checkExact["v84 theta12 variants distinct (seed < seam < nonlin band)", (1/3 - phi0/2) < (1/3 - 1/(12 Pi))]; (* ---- (v85) master cover: GL(2) covariance on the anchor plane ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L38)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)

## 2026-06-19 (an infinite-derivative narrowing of the Stelle-ghost attack, the double-pushout figure, and the ``constancy of [formula in source] '' framing of SEAM.EQUIV.01: v304)

[documents/changelog/sections/017-source.tex:92-115](../../../../documents/changelog/sections/017-source.tex#L92) · `section:355a87dfaea9de9cb7cc` · subsection

v304_idg_nonlocal_ghost.py ( QGAMB.IDG.01, / ). A conditional, parameter-free narrowing of the red-team rt_F/ v278 Stelle-ghost attack on the perturbative gravity sector. \ the local [formula in source] Weyl [formula in source] four-derivative propagator [formula in source] carries a negative-residue massive spin-2 mode (the Stelle ghost) only as a truncation artefact; \ for an entire graviton form factor [formula in

Explicit source references:

- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v278_lsz_bridge_unitarity.py](../../../../verification/v278_lsz_bridge_unitarity.py#L1) · explicit_script_identifier
- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [verification/v277_seam_calderon_e8_match.py](../../../../verification/v277_seam_calderon_e8_match.py#L1) · explicit_script_identifier
- [verification/v234_seam_holomorphy_selection.py](../../../../verification/v234_seam_holomorphy_selection.py#L1) · explicit_script_identifier
- [verification/v267_qgeo_rigidity_minimal_axiom.py](../../../../verification/v267_qgeo_rigidity_minimal_axiom.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [QGAMB.IDG.01](../../../../verification/status_ledger.csv#L400) · explicit_claim_identifier · original status at linked ledger row
- [verification/v260_k3_kummer_unification.py](../../../../verification/v260_k3_kummer_unification.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [(* ==== v278: S_pert -> S_phys LSZ bridge, one-loop optical theorem (QFT4D.SPERT.04) ==== *) Module[{xs, measureSq, phaseSq}, xs = x /. Solve[s x (1 - x) == m^2, x]; (* x_+ , x_- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2141)
- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-19 (the discrete [formula in source] dynamic lens on F_transfer: one shape, one seam-rate, v303)

[documents/changelog/sections/017-source.tex:116-132](../../../../documents/changelog/sections/017-source.tex#L116) · `section:0968f1b6845750a87eeb` · subsection

v303_ftransfer_dynamics.py asks whether the main-branch mechanism — a gapped, positivity-preserving relaxation to a unique attractor (the local-averaging update [formula in source] the [formula in source] marks, gap [formula in source] ) — is also the shape of the four F_transfer instances, or an unrelated bolt-on. It is the same shape: \ F_pole (Koide) is the seam dynamics (M\"obius multiplier [formula in source] , 

Explicit source references:

- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier
- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)

## 2026-06-19 (the last lever: the seam mass gap is the derived Recovery gap [formula in source] , v302)

[documents/changelog/sections/017-source.tex:133-151](../../../../documents/changelog/sections/017-source.tex#L133) · `section:5b9fc9c550f79525abcd` · subsection

v302_seam_gap.py closes the chain on the single statement v301 had left: ``the quasi-free seam bulk is gapped''. That gap is not a free input — it is the established Recovery gap of the seam transfer operator, derived from the carrier. \ the frozen transfer spectrum is [formula in source] ( v160/ v162), a simple Perron eigenvalue [formula in source] separated from the rest; \ the gap is [formula in source] (multiplic

Explicit source references:

- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_file_citation
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [verification/v162_seam_transport_identification.py](../../../../verification/v162_seam_transport_identification.py#L1) · explicit_script_identifier
- [verification/v301_route_a_invertible.py](../../../../verification/v301_route_a_invertible.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [verification/v300_flataway_rigid.py](../../../../verification/v300_flataway_rigid.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v297_route_a_literature_stack.py](../../../../verification/v297_route_a_literature_stack.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)

## 2026-06-19 (Route A's last hypothesis discharged: the gapped quasi-free bulk is invertible by the free-fermion classification, v301)

[documents/changelog/sections/017-source.tex:152-170](../../../../documents/changelog/sections/017-source.tex#L152) · `section:41a8556f07331f818583` · subsection

v301_route_a_invertible.py attacks the single remaining unconditional gap of SEAM.EQUIV.01. Since v300 collapsed Route B into Route A's rationality, that gap is Route A's open hypothesis ( v297 LIT-A): ``the raw quasi-free seam bulk is invertible (SRE)''. A gapped free-fermion (Gaussian) [formula in source] D bulk cannot carry intrinsic topological order — free fermions give the integer (IQHE/Chern) phases, all inver

Explicit source references:

- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v301_route_a_invertible.py](../../../../verification/v301_route_a_invertible.py#L1) · explicit_file_citation
- [verification/v297_route_a_literature_stack.py](../../../../verification/v297_route_a_literature_stack.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v148_fock_census.py](../../../../verification/v148_fock_census.py#L1) · explicit_script_identifier
- [verification/v300_flataway_rigid.py](../../../../verification/v300_flataway_rigid.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [(* ---- (v148) NS/R sector census (corrected) ---- *) Module[{nsClasses, rCounts, glueA, glueB, inA, inB}, nsClasses = Union[Flatten[Table[ {2 Mod[Total[v], 2], 2 Mod[Total[w], 2]}, {v, Tuples[Range[-1, 1], 5]}, {w, Tuples[Range[-1, 1], 3]}], 1]]; rCounts = <||>; Do[Module[{qd = If[EvenQ[Count[s5, -1]], 1, 3]}, Do[Module[{qa = If[EvenQ[Count[s3, -1]], 1, 3]}, rCounts[{qd, qa}] = Lookup[rCounts, Key[{qd, qa}], 0] + 1], {s3, Tuples[{1, -1}, 3]}]], {s5, Tuples[{1, -1}, 5]}]; glueA = {{0, 0}, {1, 1}, {2, 2}, {3, 3}}; glueB = {{0, 0}, {1, 3}, {2, 2}, {3, 1}}; inA = Total[Lookup[rCounts, Key[#], 0] & /@ glueA]; inB = Total[Lookup[rCounts, Key[#], 0] & /@ glueB]; checkExact["v148 NS/R census (corrected): NS supports only even classes {(0,0),(2,0),(0,2),(2,2)} (integer weights); R zero-mode module = four odd pairs of 64; R splits 128+128 into the odd sectors of the two Lagrangian glues; 248 = 120 NS + 128 R", Sort[nsClasses] == Sort[{{0, 0}, {2, 0}, {0, 2}, {2, 2}}] && ! MemberQ[nsClasses, {1, 1}] && ! MemberQ[nsClasses, {3, 3}] && Values[KeySort[rCounts]] == {64, 64, 64, 64} && Total[Values[rCounts]] == 256 && inA == 128 && inB == 128 && 120 + 128 == 248]; ]; (* ---- (v149) cusp normal ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1280)

## 2026-06-19 (the Flat-Away attack: a hard discrete obstruction [formula in source] the pin derived from [formula in source] , v300)

[documents/changelog/sections/017-source.tex:171-189](../../../../documents/changelog/sections/017-source.tex#L171) · `section:2f80e058daba5055768b` · subsection

v300_flataway_rigid.py attacks the single external fact the three Flat-Away routes ( v291/ v293/ v295) left open, on two fronts. Harden: the flat seam was only a soft minimum (``the spectral mismatch grows with [formula in source] ''); here the obstruction becomes a discrete on/off invariant. \ the flat fingerprint — [formula in source] is the integer ladder with every level [formula in source] of multiplicity exactl

Explicit source references:

- [verification/v300_flataway_rigid.py](../../../../verification/v300_flataway_rigid.py#L1) · explicit_file_citation
- [verification/v295_flataway_a2_exact.py](../../../../verification/v295_flataway_a2_exact.py#L1) · explicit_script_identifier
- [verification/v293_flataway_spectral_hessian.py](../../../../verification/v293_flataway_spectral_hessian.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v291_flataway_contract.py](../../../../verification/v291_flataway_contract.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## 2026-06-19 (the hypergraph/Wolfram bridge hardened: the [formula in source] seed reaches [formula in source] as the last finite point, v299)

[documents/changelog/sections/017-source.tex:190-206](../../../../documents/changelog/sections/017-source.tex#L190) · `section:6c5940fdfa107000ca6f` · subsection

v299_hypergraph_0d_autonomous.py hardens the Wolfram/hypergraph reading into a precisely typed bridge (builds on v219/ v298): \ the icosahedron is a 3-uniform hypergraph ( [formula in source] ; the McKay group is the [formula in source] binary lift [formula in source] , a different order-120 group whose McKay graph is affine [formula in source] ; [formula in source] edges [formula in source] ); \ the [formula in sour

Explicit source references:

- [verification/v299_hypergraph_0d_autonomous.py](../../../../verification/v299_hypergraph_0d_autonomous.py#L1) · explicit_script_identifier
- [verification/v219_icosahedral_mckay.py](../../../../verification/v219_icosahedral_mckay.py#L1) · explicit_script_identifier
- [verification/v298_e8_network_attractor.py](../../../../verification/v298_e8_network_attractor.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)

## 2026-06-18 (E8 as a network attractor — the Wolfram-program reading, v298)

[documents/changelog/sections/017-source.tex:207-219](../../../../documents/changelog/sections/017-source.tex#L207) · `section:678b949672ccc6aa27ab` · subsection

v298_e8_network_attractor.py is an honest audit of the ``TFPT as a hypergraph/rewrite system'' idea, on the v219 McKay bedrock. \ the affine- [formula in source] Kac marks [formula in source] are the unique dynamical attractor of a minimal local-averaging update [formula in source] on the [formula in source] McKay graph (converges from any positive start; [formula in source] , top eigenvalue [formula in source] ); th

Explicit source references:

- [verification/v298_e8_network_attractor.py](../../../../verification/v298_e8_network_attractor.py#L1) · explicit_file_citation
- [verification/v219_icosahedral_mckay.py](../../../../verification/v219_icosahedral_mckay.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)

## 2026-06-18 (a [formula in source] closed form + Route A literature stack, v296– v297)

[documents/changelog/sections/017-source.tex:220-233](../../../../documents/changelog/sections/017-source.tex#L220) · `section:aaf9450d3002873f5a8a` · subsection

v296_flataway_a2_closed.py ( FLATAWAY.A2.CLOSED.01) evaluates the exact [formula in source] coefficient in closed form: the operator tails telescope geometrically ( [formula in source] ) to [formula in source] , leaving a finite [formula in source] -term middle; e.g.\ [formula in source] . Manifestly positive, small- [formula in source] law [formula in source] (the [formula in source] term cancels). Reproduces v295 t

Explicit source references:

- [FLATAWAY.A2.CLOSED.01](../../../../verification/status_ledger.csv#L392) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.A.LIT.01](../../../../verification/status_ledger.csv#L397) · explicit_claim_identifier · original status at linked ledger row
- [verification/v286_seam_equivalence_contract.py](../../../../verification/v286_seam_equivalence_contract.py#L1) · explicit_script_identifier
- [verification/v296_flataway_a2_closed.py](../../../../verification/v296_flataway_a2_closed.py#L1) · explicit_file_citation
- [verification/v297_route_a_literature_stack.py](../../../../verification/v297_route_a_literature_stack.py#L1) · explicit_file_citation
- [verification/v295_flataway_a2_exact.py](../../../../verification/v295_flataway_a2_exact.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-18 (Flat-Away heat route made exact + Lean-formalised, v295 / FORM.FLATAWAY.01)

[documents/changelog/sections/017-source.tex:234-249](../../../../documents/changelog/sections/017-source.tex#L234) · `section:310122d1b406c61c400f` · subsection

v295_flataway_a2_exact.py ( FLATAWAY.A2.01) upgrades the v292 positive-definiteness from a numerical scan to a proof: the first variation of [formula in source] vanishes (zero-mean off-mark curvature, Gauss-Bonnet), and since [formula in source] is convex (Klein/Peierls), [formula in source] is the global minimum — so [formula in source] for all deformations, [formula in source] iff [formula in source] . The exact se

Explicit source references:

- [verification/v295_flataway_a2_exact.py](../../../../verification/v295_flataway_a2_exact.py#L1) · explicit_file_citation
- [TFPT.Carrier.SeamDeckClosure.heatDeviation_eq_zero_iff](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L229) · explicit_lean_symbol
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1) · explicit_file_citation
- [verification/v292_flataway_heat_reduction.py](../../../../verification/v292_flataway_heat_reduction.py#L1) · explicit_script_identifier
- [FLATAWAY.A2.01](../../../../verification/status_ledger.csv#L390) · explicit_claim_identifier · original status at linked ledger row
- [FORM.FLATAWAY.01](../../../../verification/status_ledger.csv#L391) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-18 (Flat-Away attacked on all three routes, v292– v294)

[documents/changelog/sections/017-source.tex:250-269](../../../../documents/changelog/sections/017-source.tex#L250) · `section:db81095caf4bfe7ff937` · subsection

v292_flataway_heat_reduction.py ( FLATAWAY.HEAT.01): the heat route, made precise. The heat-trace deviation [formula in source] is a positive-definite quadratic form in the off-mark curvature ( [formula in source] for every [formula in source] mode, positive on all combinations), leading invariant [formula in source] — so Flat-Away reduces to the single fact ``the seam fixes the [formula in source] heat coefficient''

Explicit source references:

- [verification/v293_flataway_spectral_hessian.py](../../../../verification/v293_flataway_spectral_hessian.py#L1) · explicit_file_citation
- [FLATAWAY.HEAT.01](../../../../verification/status_ledger.csv#L387) · explicit_claim_identifier · original status at linked ledger row
- [FLATAWAY.ENERGY.01](../../../../verification/status_ledger.csv#L389) · explicit_claim_identifier · original status at linked ledger row
- [verification/v292_flataway_heat_reduction.py](../../../../verification/v292_flataway_heat_reduction.py#L1) · explicit_file_citation
- [FLATAWAY.SPEC.01](../../../../verification/status_ledger.csv#L388) · explicit_claim_identifier · original status at linked ledger row
- [verification/v294_flataway_rp_energy.py](../../../../verification/v294_flataway_rp_energy.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-18 (Route-B red-team: the smooth [formula in source] adversary + Flat-Away as a mini-theorem, v290– v291)

[documents/changelog/sections/017-source.tex:270-285](../../../../documents/changelog/sections/017-source.tex#L270) · `section:1dd51adeb586c882e7c4` · subsection

v290_z4_smooth_curvature_adversary.py ( SEAM.ADVERSARY.01) is the honest red-team that [formula in source] block-diagonality is not mark-locality: a smooth [formula in source] off-mark curvature [formula in source] \ passes the v288 commutator ( [formula in source] , same as mark-local) yet \ shifts the DtN spectrum ( [formula in source] ) and the heat trace ( [formula in source] ). So the commutator is necessary, no

Explicit source references:

- [verification/v291_flataway_contract.py](../../../../verification/v291_flataway_contract.py#L1) · explicit_script_identifier
- [verification/v290_z4_smooth_curvature_adversary.py](../../../../verification/v290_z4_smooth_curvature_adversary.py#L1) · explicit_script_identifier
- [verification/v288_full_l2_subprincipal_z4.py](../../../../verification/v288_full_l2_subprincipal_z4.py#L1) · explicit_script_identifier
- [FLATAWAY.RP.01](../../../../verification/status_ledger.csv#L386) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.ADVERSARY.01](../../../../verification/status_ledger.csv#L385) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-18 (Route B sharpened: raw mark-locality decomposed + reviewer firewalls, v289 / v287– v288)

[documents/changelog/sections/017-source.tex:286-303](../../../../documents/changelog/sections/017-source.tex#L286) · `section:f3f0a4f56db397726de9` · subsection

v289_marklocal_raw.py ( MARKLOCAL.RAW.01) decomposes the one remaining Route-B residual (`why is the raw seam sub-principal term mark-local?') into a 5-lemma chain and isolates the single open analytic lemma: \ L1 conic parametrix (b-calculus/Melrose, imported); \ L2 Flat-Away — RP [formula in source] gap [formula in source] 4 marks [formula in source] curvature vanishes away from the marks; \ L3 orbit-source ( v195/

Explicit source references:

- [verification/v288_full_l2_subprincipal_z4.py](../../../../verification/v288_full_l2_subprincipal_z4.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v289_marklocal_raw.py](../../../../verification/v289_marklocal_raw.py#L1) · explicit_file_citation
- [verification/v287_free_rp_bulk_to_holomorphic_boundary.py](../../../../verification/v287_free_rp_bulk_to_holomorphic_boundary.py#L1) · explicit_script_identifier
- [MARKLOCAL.RAW.01](../../../../verification/status_ledger.csv#L384) · explicit_claim_identifier · original status at linked ledger row
- [verification/v195_marks_lefschetz_character.py](../../../../verification/v195_marks_lefschetz_character.py#L1) · explicit_script_identifier
- [verification/v264_raw_seam_marklocal.py](../../../../verification/v264_raw_seam_marklocal.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v195) QGEO.MARKS.02: Lefschetz/character forcing of the free mu4 orbit ---- *) Module[{chars, trace, noTrivial, orbit, orbitClosed, nPunct}, chars = I^Range[1, 3]; (* {I, -1, -I} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1607)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)

## 2026-06-18 (closing sprint: the Seam Equivalence Theorem named + both routes attacked, v286– v288)

[documents/changelog/sections/017-source.tex:304-324](../../../../documents/changelog/sections/017-source.tex#L304) · `section:98e28332378f4d77a163` · subsection

v286_seam_equivalence_contract.py ( SEAM.EQUIV.01) names the one open theorem — the raw RP seam state is the holomorphic [formula in source] net at [formula in source] — and concentrates the whole open structure on it: four objects, six arrows (2 closed, 1 conditional v282, 1 open Gral), an import firewall proving the two routes ( v276/ v280/ v284 vs v277/ v281/ v285) never import each other (no ` [formula in source]

Explicit source references:

- [verification/v277_seam_calderon_e8_match.py](../../../../verification/v277_seam_calderon_e8_match.py#L1) · explicit_script_identifier
- [verification/v276_qgeo_flat_closes_commutator.py](../../../../verification/v276_qgeo_flat_closes_commutator.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v287_free_rp_bulk_to_holomorphic_boundary.py](../../../../verification/v287_free_rp_bulk_to_holomorphic_boundary.py#L1) · explicit_file_citation
- [verification/v288_full_l2_subprincipal_z4.py](../../../../verification/v288_full_l2_subprincipal_z4.py#L1) · explicit_file_citation
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [verification/v285_route_ii_seam_condensation.py](../../../../verification/v285_route_ii_seam_condensation.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.B01](../../../../verification/status_ledger.csv#L383) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.A01](../../../../verification/status_ledger.csv#L382) · explicit_claim_identifier · original status at linked ledger row
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [verification/seam_equivalence.json](../../../../verification/seam_equivalence.json#L1) · explicit_file_citation
- [verification/v284_route_i_rp_uniqueness.py](../../../../verification/v284_route_i_rp_uniqueness.py#L1) · explicit_script_identifier
- [verification/v286_seam_equivalence_contract.py](../../../../verification/v286_seam_equivalence_contract.py#L1) · explicit_script_identifier
- [verification/v280_pillowcase_steklov.py](../../../../verification/v280_pillowcase_steklov.py#L1) · explicit_script_identifier
- [verification/v282_e8_tau_i_unification.py](../../../../verification/v282_e8_tau_i_unification.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [(* ==== v282: E8-at-tau=i unification, chi_E8(i)=12 (QGAMB.UNIFY.01) ==== *) Module[{jf, jorder4, chiI}, jf[x_] := 256 (x^2 - x + 1)^3/(x^2 (x - 1)^2); jorder4 = jf[2]; (* cross-ratio 2 => j = 1728 = the tau=i CM point *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2170)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)

## 2026-06-18 (the two proof routes decomposed: Route (i) and Route (ii) into lemma chains, v284/ v285)

[documents/changelog/sections/017-source.tex:325-340](../../../../documents/changelog/sections/017-source.tex#L325) · `section:2c657950cbbf3e8129b9` · subsection

v284_route_i_rp_uniqueness.py ( QGEO.ROUTEI.01) turns Route (i) (RP-state uniqueness) into a 6-lemma chain: \ 5/6 lemmas are already discharged — L1 RP [formula in source] DtN ( v194), L2 marks [formula in source] pillowcase ( v195/ v216/ v214), L3 flat Steklov [formula in source] (verified here), L4 covariance from DtN ( v258), L5 [formula in source] -invariance ( v276/Lean/ v280); \ Troyanov ( [formula in source] u

Explicit source references:

- [verification/v284_route_i_rp_uniqueness.py](../../../../verification/v284_route_i_rp_uniqueness.py#L1) · explicit_script_identifier
- [verification/v280_pillowcase_steklov.py](../../../../verification/v280_pillowcase_steklov.py#L1) · explicit_script_identifier
- [verification/v276_qgeo_flat_closes_commutator.py](../../../../verification/v276_qgeo_flat_closes_commutator.py#L1) · explicit_script_identifier
- [verification/v258_dirac_covariance_induction.py](../../../../verification/v258_dirac_covariance_induction.py#L1) · explicit_script_identifier
- [verification/v195_marks_lefschetz_character.py](../../../../verification/v195_marks_lefschetz_character.py#L1) · explicit_script_identifier
- [verification/v285_route_ii_seam_condensation.py](../../../../verification/v285_route_ii_seam_condensation.py#L1) · explicit_script_identifier
- [verification/v194_raw_seam_dtn_rp.py](../../../../verification/v194_raw_seam_dtn_rp.py#L1) · explicit_script_identifier
- [verification/v282_e8_tau_i_unification.py](../../../../verification/v282_e8_tau_i_unification.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [QGAMB.ROUTEII.01](../../../../verification/status_ledger.csv#L380) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.ROUTEI.01](../../../../verification/status_ledger.csv#L379) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v282: E8-at-tau=i unification, chi_E8(i)=12 (QGAMB.UNIFY.01) ==== *) Module[{jf, jorder4, chiI}, jf[x_] := 256 (x^2 - x + 1)^3/(x^2 (x - 1)^2); jorder4 = jf[2]; (* cross-ratio 2 => j = 1728 = the tau=i CM point *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2170)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [(* ---- (v195) QGEO.MARKS.02: Lefschetz/character forcing of the free mu4 orbit ---- *) Module[{chars, trace, noTrivial, orbit, orbitClosed, nPunct}, chars = I^Range[1, 3]; (* {I, -1, -I} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1607)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)

## 2026-06-18 (self-investigation round: pillowcase DtN, modular data, the E8-at- [formula in source] unification, live scorecard, v280– v283)

[documents/changelog/sections/017-source.tex:341-359](../../../../documents/changelog/sections/017-source.tex#L341) · `section:5573768c07b5b0367bc7` · subsection

v280_pillowcase_steklov.py ( QGEO.STEKLOV.01) runs the QGEO chain on the actual flat [formula in source] pillowcase orbifold: the order-4 deck permutes the 4 cone points (2 fixed [formula in source] 1 swap) and the geometric chain [formula in source] is numerically exact — route-(i) evidence for QGEO.OBLIG.01; the premise stays . v281_holomorphy_modular_data.py ( QGAMB.MODULAR.01): \#anyons [formula in source] (E8 [f

Explicit source references:

- [verification/v280_pillowcase_steklov.py](../../../../verification/v280_pillowcase_steklov.py#L1) · explicit_script_identifier
- [verification/v283_live_killtest_scorecard.py](../../../../verification/v283_live_killtest_scorecard.py#L1) · explicit_file_citation
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_file_citation
- [QGEO.OBLIG.01](../../../../verification/status_ledger.csv#L373) · explicit_claim_identifier · original status at linked ledger row
- [QGAMB.MODULAR.01](../../../../verification/status_ledger.csv#L376) · explicit_claim_identifier · original status at linked ledger row
- [PRED.LIVE.01](../../../../verification/status_ledger.csv#L378) · explicit_claim_identifier · original status at linked ledger row
- [QGAMB.UNIFY.01](../../../../verification/status_ledger.csv#L377) · explicit_claim_identifier · original status at linked ledger row
- [verification/v282_e8_tau_i_unification.py](../../../../verification/v282_e8_tau_i_unification.py#L1) · explicit_script_identifier
- [QGEO.STEKLOV.01](../../../../verification/status_ledger.csv#L375) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v282: E8-at-tau=i unification, chi_E8(i)=12 (QGAMB.UNIFY.01) ==== *) Module[{jf, jorder4, chiI}, jf[x_] := 256 (x^2 - x + 1)^3/(x^2 (x - 1)^2); jorder4 = jf[2]; (* cross-ratio 2 => j = 1728 = the tau=i CM point *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2170)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)

## 2026-06-18 (the Gr\"al: QGEO.SYM.01 as one precise lemma [formula in source] the all-orders step Lean-formalised, v279/ FORM.QGEO.04)

[documents/changelog/sections/017-source.tex:360-377](../../../../documents/changelog/sections/017-source.tex#L360) · `section:47adde543bdad0ea081f` · subsection

v279_qgeo_obligation_lemma.py ( QGEO.OBLIG.01) writes the bedrock as ONE precise constructive-QFT lemma. Given the premise the raw seam carries the flat [formula in source] pillowcase metric (Troyanov-unique, [formula in source] ), then [formula in source] mark-locality [formula in source] . \ the reduction DAG from `free RP seam' has exactly one open leaf — `the raw seam state is the flat state'; \ the geometric sid

Explicit source references:

- [TFPT.Carrier.SeamDeckClosure.flat_all_orders_clock](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L202) · explicit_lean_symbol
- [verification/v276_qgeo_flat_closes_commutator.py](../../../../verification/v276_qgeo_flat_closes_commutator.py#L1) · explicit_script_identifier
- [FORM.QGEO.04](../../../../verification/status_ledger.csv#L374) · explicit_claim_identifier · original status at linked ledger row
- [verification/v279_qgeo_obligation_lemma.py](../../../../verification/v279_qgeo_obligation_lemma.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1) · explicit_file_citation
- [QGEO.OBLIG.01](../../../../verification/status_ledger.csv#L373) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [TFPT.Carrier.SeamDeckClosure.diagonal_commutesClock](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L182) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-18 (4D QFT: the [formula in source] LSZ bridge [formula in source] one-loop unitarity, v278)

[documents/changelog/sections/018-source.tex:1-14](../../../../documents/changelog/sections/018-source.tex#L1) · `section:4972356a38c52e50cf39` · subsection

v278_lsz_bridge_unitarity.py ( QFT4D.SPERT.04) connects the perturbative S-matrix to the physical asymptotic one and verifies one-loop unitarity. \ LSZ bridge: the EG [formula in source] -products of [formula in source] ( v269) are the OS Wick-rotated correlators ( v240), so amputate [formula in source] on-shell-residue gives [formula in source] ; \ the gap [formula in source] gives Haag–Ruelle asymptotic states. \ o

Explicit source references:

- [verification/v240_gns_os_reconstruction.py](../../../../verification/v240_gns_os_reconstruction.py#L1) · explicit_script_identifier
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_script_identifier
- [QFT4D.SPERT.04](../../../../verification/status_ledger.csv#L372) · explicit_claim_identifier · original status at linked ledger row
- [verification/v278_lsz_bridge_unitarity.py](../../../../verification/v278_lsz_bridge_unitarity.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v278: S_pert -> S_phys LSZ bridge, one-loop optical theorem (QFT4D.SPERT.04) ==== *) Module[{xs, measureSq, phaseSq}, xs = x /. Solve[s x (1 - x) == m^2, x]; (* x_+ , x_- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2141)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)

## 2026-06-18 (QG.AMB.01 Tier-B made concrete: the seam-Calder\'on [formula in source] match, v277)

[documents/changelog/sections/018-source.tex:15-26](../../../../documents/changelog/sections/018-source.tex#L15) · `section:f1a0b6f25c4c201d4774` · subsection

v277_seam_calderon_e8_match.py ( QGAMB.TIERB.01) reduces Tier-B to ONE bit. \ the full [formula in source] matching target is computed and matches: [formula in source] , [formula in source] , the holomorphic character [formula in source] with a single primary and exactly [formula in source] weight-1 currents ( [formula in source] roots). \ the discriminator is holomorphy — the [formula in source] counterexample [form

Explicit source references:

- [verification/v277_seam_calderon_e8_match.py](../../../../verification/v277_seam_calderon_e8_match.py#L1) · explicit_script_identifier
- [QGAMB.TIERB.01](../../../../verification/status_ledger.csv#L371) · explicit_claim_identifier · original status at linked ledger row
- [verification/v276_qgeo_flat_closes_commutator.py](../../../../verification/v276_qgeo_flat_closes_commutator.py#L1) · explicit_script_identifier
- [verification/v260_k3_kummer_unification.py](../../../../verification/v260_k3_kummer_unification.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)

## 2026-06-18 (QGEO.SYM.01 narrowed: the flat pillowcase closes the commutator to all orders, v276)

[documents/changelog/sections/018-source.tex:27-40](../../../../documents/changelog/sections/018-source.tex#L27) · `section:25e03edabfb4b9161f7f` · subsection

v276_qgeo_flat_closes_commutator.py ( QGEO.SYM.03) collapses the bedrock to ONE geometric postulate. The state-level residual the whole bedrock rests on is the operator equation [formula in source] . \ if [formula in source] and the order-4 deck [formula in source] ( [formula in source] ) is a flat- [formula in source] isometry, then [formula in source] exactly, to all orders (verified on the discretised square torus

Explicit source references:

- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v201_seam_subprincipal_marks.py](../../../../verification/v201_seam_subprincipal_marks.py#L1) · explicit_script_identifier
- [verification/v276_qgeo_flat_closes_commutator.py](../../../../verification/v276_qgeo_flat_closes_commutator.py#L1) · explicit_file_citation
- [verification/v198_modular_commutator_reduction.py](../../../../verification/v198_modular_commutator_reduction.py#L1) · explicit_script_identifier
- [QGEO.SYM.03](../../../../verification/status_ledger.csv#L370) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [(* ---- (v198) QGEO.MODULAR.01: principal symbol |k| commutes with the clock rho EXACTLY ---- *) Module[{nn, rho1, absK, comm}, nn = Range[-8, 8]; rho1 = DiagonalMatrix[I^nn]; (* z->iz: e^{in t} -> i^n e^{in t} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1638)
- [(* ---- (v201) QGEO.SUBPRIN.01: a mu4-mark sum is Z4-invariant => sub-principal block-diagonal ---- *) Module[{markSum, nn, rho, fmodes, Mf, Moff, gprof}, (* exact: the mu4-mark Fourier weight sum_{j=0}^3 e^{-i m 2pi j/4} = 4 [m=0 mod 4], else 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1665)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)

## 2026-06-18 (Red Team Target F — adversarial audit of the v269–v275 round, rt_F)

[documents/changelog/sections/018-source.tex:41-54](../../../../documents/changelog/sections/018-source.tex#L41) · `section:b83adf4eee20d614ac74` · subsection

redteam/rt_F_qft4d.py ( REDTEAM.F.01) stress-tests the just-published round (the perturbative [formula in source] layer, the PMNS Jarlskog, the [formula in source] -scale, the over-determination, the QG.AMB.01 roadmap). Survives (narrowed): two attacks land and are folded in. (1) the gravity [formula in source] Weyl [formula in source] sub-sector is power-counting renormalizable but non-unitary (the Stelle ghost: the

Explicit source references:

- [verification/v274_scale_overdetermination.py](../../../../verification/v274_scale_overdetermination.py#L1) · explicit_script_identifier
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_script_identifier
- [REDTEAM.F.01](../../../../verification/status_ledger.csv#L369) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/redteam/run_redteam.py](../../../../verification/redteam/run_redteam.py#L1) · explicit_file_citation
- [LAMBDA.BRANCH.01](../../../../verification/status_ledger.csv#L129) · explicit_claim_identifier · original status at linked ledger row
- [verification/redteam/rt_F_qft4d.py](../../../../verification/redteam/rt_F_qft4d.py#L1) · explicit_file_citation
- [verification/v275_qgamb_roadmap.py](../../../../verification/v275_qgamb_roadmap.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)

## 2026-06-18 (Zenodo release 5.2 (rev 191) — the perturbative 4D-QFT layer + scale closure, v269–v275)

[documents/changelog/sections/018-source.tex:55-67](../../../../documents/changelog/sections/018-source.tex#L55) · `section:63427eabab107d1a2a94` · subsection

Published to Zenodo. Version 5.2 (rev 191) of the ten-PDF document set was published as a new version of the TFPT deposit — record 20743347, DOI 10.5281/zenodo.20743347. This release carries the perturbative 4D-QFT layer (the Epstein–Glaser [formula in source] skeleton v269, the concrete one-loop quartic v271 and gauge [formula in source] -coefficients v273), the complete complex PMNS matrix and leptonic CP strength 

Explicit source references:

- [verification/v272_nu_mass_scale.py](../../../../verification/v272_nu_mass_scale.py#L1) · explicit_script_identifier
- [verification/v273_eg_gauge_running.py](../../../../verification/v273_eg_gauge_running.py#L1) · explicit_script_identifier
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v274_scale_overdetermination.py](../../../../verification/v274_scale_overdetermination.py#L1) · explicit_script_identifier
- [verification/v271_eg_oneloop_quartic.py](../../../../verification/v271_eg_oneloop_quartic.py#L1) · explicit_script_identifier
- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_script_identifier
- [verification/v275_qgamb_roadmap.py](../../../../verification/v275_qgamb_roadmap.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)

## 2026-06-18 (scale + frontier round: [formula in source] -mass scale, EG gauge running, over-determination, QG roadmap, v272– v275)

[documents/changelog/sections/018-source.tex:68-92](../../../../documents/changelog/sections/018-source.tex#L68) · `section:366ba63a37a50edd34ea` · subsection

v272_nu_mass_scale.py ( FLAV.NUSCALE.01) types the absolute neutrino-mass scale honestly (no fabricated [formula in source] — would contradict the v184 firewall). \ the absolute scale reduces to one seesaw ratio [formula in source] (one UV input, like [formula in source] , v153); \ the observed [formula in source] eV with the TFPT PS [formula in source] GUT window [formula in source] GeV ( v249) needs [formula in sou

Explicit source references:

- [verification/v272_nu_mass_scale.py](../../../../verification/v272_nu_mass_scale.py#L1) · explicit_file_citation
- [verification/v274_scale_overdetermination.py](../../../../verification/v274_scale_overdetermination.py#L1) · explicit_file_citation
- [verification/v275_qgamb_roadmap.py](../../../../verification/v275_qgamb_roadmap.py#L1) · explicit_script_identifier
- [verification/v36_spectral_action_g2.py](../../../../verification/v36_spectral_action_g2.py#L1) · explicit_script_identifier
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier
- [QFT4D.SPERT.03](../../../../verification/status_ledger.csv#L366) · explicit_claim_identifier · original status at linked ledger row
- [verification/v271_eg_oneloop_quartic.py](../../../../verification/v271_eg_oneloop_quartic.py#L1) · explicit_script_identifier
- [SCALE.OVERDET.01](../../../../verification/status_ledger.csv#L367) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NUSCALE.01](../../../../verification/status_ledger.csv#L365) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_script_identifier
- [verification/v76_gmetric_reduction.py](../../../../verification/v76_gmetric_reduction.py#L1) · explicit_script_identifier
- [QGAMB.ROADMAP.01](../../../../verification/status_ledger.csv#L368) · explicit_claim_identifier · original status at linked ledger row
- [verification/v273_eg_gauge_running.py](../../../../verification/v273_eg_gauge_running.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v249_ps_unification.py](../../../../verification/v249_ps_unification.py#L1) · explicit_script_identifier
- [verification/v78_vgeo_floor.py](../../../../verification/v78_vgeo_floor.py#L1) · explicit_script_identifier
- [verification/v77_e8_conformal_net.py](../../../../verification/v77_e8_conformal_net.py#L1) · explicit_script_identifier
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)
- [(* ---- (v24) quark ratio closure ---- *) checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117]; checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47]; checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26]; check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3]; check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2]; (* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L105)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* v475 (iii): the Lorentzian timelike positivity witness *) gL = DiagonalMatrix[{-1, 1, 1, 1}]; mM = Outer[Times, {vv, 0, 0, 0}, {vv, 0, 0, 0}]; evT = Sort[Eigenvalues[(gL + aal mM) . Inverse[gL]]]; evS = Sort[Eigenvalues[(gL + aal Outer[Times, {0, vv, 0, 0}, {0, vv, 0, 0}]) . Inverse[gL]]]; checkExact["v475 GRAV.ENTROPIC.SCALARON.01 (iii): the Lorentzian-positivity witness -- on Minkowski a TIMELIKE gradient gives G g^-1 eigenvalues {1 - alpha v^2, 1, 1, 1} (nonpositive for v^2 >= 1/alpha, ln undefined) while a SPACELIKE gradient gives {1 + alpha v^2, 1, 1, 1} (positive for all v) -- the v473 caveat exhibited, the OS route sturdier", Sort[evT] == Sort[{1 - aal vv^2, 1, 1, 1}] && Sort[evS] == Sort[{1 + aal vv^2, 1, 1, 1}]]; ]; (* ==== v477 round: the scale-flow representation of the entropic action -- the exact content: the Frullani identity Integrate[(e^{-a t}-e^{-t})/t] = -Log[a], the moment dictionary (flat weight = unit moments = the v475 raw coefficients 3 b R + (17/24) b^2 R^2), the ONE moment condition mu2/mu1^2 = (72/17)(8 pi)^9 with the exact closure (4608 pi^2/17)/((72/17)(8 pi)^9) = c3^7, and the v36 consistency f0 = 6 (4 pi)^2/c3^7 <=> M^2 = c3^7 Mbar^2; mirrors v477 (the chi-form quadrature is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3052)
- [(* v477 (i): Frullani + the moment dictionary at flat weight *) frul = Integrate[(Exp[-aa tt] - Exp[-tt])/tt, {tt, 0, Infinity}, Assumptions -> aa > 0]; eig = Join[{1}, Table[1/4, 4], Table[1/6, 6]]; tr = Total[Exp[-tt (1 - bb # RR)] & /@ eig] - 11 Exp[-tt]; serR = Normal[Series[tr, {RR, 0, 2}]]; mu1f = Integrate[Coefficient[serR, RR, 1]/tt, {tt, 0, Infinity}]; mu2f = Integrate[Coefficient[serR, RR, 2]/tt, {tt, 0, Infinity}]; checkExact["v477 GRAV.ENTROPIC.SCALEFLOW.01 (i): the Frullani/scale-flow identity -Log[a] = Integrate[(e^{-a t}-e^{-t})/t] (symbolic) and the moment dictionary -- at the FLAT weight the maximally-symmetric relative trace integrates to exactly the v475 raw coefficients 3 b R + (17/24) b^2 R^2 (unit moments mu1 = mu2 = 1): the raw entropic action is the unit-moment point of a scale-measure family", frul == -Log[aa] && Simplify[mu1f - 3 bb] == 0 && Simplify[mu2f - (17/24) bb^2] == 0]; (* v477 (ii): the one moment condition + closure + v36 consistency *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3071)
- [(* ---- (v77) G6 via E8 level-1 net: level-1 central charges + conformal embedding c-sum ---- *) checkExact["level-1 c=dim/(1+h^v): c(E8)=248/31=8=rank E8, c(D5)=45/9=5, c(A3)=15/5=3; embedding 5+3=8 => coset c=0", Module[{cE8 = 248/(1 + 30), cD5 = 45/(1 + 8), cA3 = 15/(1 + 4)}, (cE8 == 8) && (cD5 == 5) && (cA3 == 3) && (cD5 + cA3 == cE8)]]; (* ---- (v78) v_geo floor: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (one scale pinned by one measurement) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L376)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)

## 2026-06-18 (4D QFT: a concrete Epstein–Glaser one-loop quartic renormalization, v271)

[documents/changelog/sections/018-source.tex:93-106](../../../../documents/changelog/sections/018-source.tex#L93) · `section:b45acf2298f96eb443c6` · subsection

v271_eg_oneloop_quartic.py ( QFT4D.SPERT.02) takes the v269 [formula in source] skeleton from ``exists'' to an actual EG number (no path integral). \ the first renormalization is the order-2 product [formula in source] ; the massless propagator has scaling degree [formula in source] in [formula in source] , the one-loop bubble has [formula in source] , so [formula in source] [formula in source] exactly one logarithmi

Explicit source references:

- [verification/v271_eg_oneloop_quartic.py](../../../../verification/v271_eg_oneloop_quartic.py#L1) · explicit_script_identifier
- [QFT4D.SPERT.02](../../../../verification/status_ledger.csv#L364) · explicit_claim_identifier · original status at linked ledger row
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)

## 2026-06-18 (PMNS: the complete complex matrix + the leptonic Jarlskog CP strength, v270)

[documents/changelog/sections/018-source.tex:107-119](../../../../documents/changelog/sections/018-source.tex#L107) · `section:3116e55fdb4f7529082e` · subsection

v270_pmns_jarlskog_assembly.py ( FLAV.PMNS.03) assembles the four TFPT channels ( [formula in source] , [formula in source] , [formula in source] , [formula in source] ) into one exactly-unitary complex PMNS matrix and derives the leptonic CP strength. \ [formula in source] is unitary; \ the Jarlskog [formula in source] ( [formula in source] ) is a derived number, the leptonic analogue of the CKM [formula in source] 

Explicit source references:

- [FLAV.PMNS.03](../../../../verification/status_ledger.csv#L363) · explicit_claim_identifier · original status at linked ledger row
- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_script_identifier
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
