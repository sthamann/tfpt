# Boundary, seam and clocks — part 9

[Topic entry](../boundary-clocks.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

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

## 2026-06-12

[documents/changelog/sections/024-source.tex:12-75](../../../../documents/changelog/sections/024-source.tex#L12) · `section:a7ddfbed7669a08bf2ee` · subsection

Margin theorem (v122). The established frozen selectors ( [formula in source] annihilator [formula in source] , [formula in source] , [formula in source] ) pin [formula in source] uniquely among hexagon matrices ( [formula in source] ); the atom margins become theorems — H2 introduces no new residual class. Inventory update (v123). Residual table re-pinned post v110–v122: exactly five structural classes (R1 clock, R2

Explicit source references:

- [verification/v138_vw_firewall.py](../../../../verification/v138_vw_firewall.py#L1) · explicit_script_identifier
- [verification/v140_canonical_map.py](../../../../verification/v140_canonical_map.py#L1) · explicit_script_identifier
- [verification/v126_clock_wall_bridge.py](../../../../verification/v126_clock_wall_bridge.py#L1) · explicit_script_identifier
- [verification/v134_dual_anchor.py](../../../../verification/v134_dual_anchor.py#L1) · explicit_script_identifier
- [verification/v128_graded_hull.py](../../../../verification/v128_graded_hull.py#L1) · explicit_script_identifier
- [verification/v129_entropy_power_law.py](../../../../verification/v129_entropy_power_law.py#L1) · explicit_script_identifier
- [verification/v133_zeta_budget.py](../../../../verification/v133_zeta_budget.py#L1) · explicit_script_identifier
- [verification/v127_ring_resummation.py](../../../../verification/v127_ring_resummation.py#L1) · explicit_script_identifier
- [verification/v122_margin_theorem.py](../../../../verification/v122_margin_theorem.py#L1) · explicit_script_identifier
- [verification/v131_measure_is_area.py](../../../../verification/v131_measure_is_area.py#L1) · explicit_script_identifier
- [verification/v132_detratio_anomaly.py](../../../../verification/v132_detratio_anomaly.py#L1) · explicit_script_identifier
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v124_resummed_clock.py](../../../../verification/v124_resummed_clock.py#L1) · explicit_script_identifier
- [verification/v136_dual_normal_selector.py](../../../../verification/v136_dual_normal_selector.py#L1) · explicit_script_identifier
- [verification/v110_calderon_sheet.py](../../../../verification/v110_calderon_sheet.py#L1) · explicit_script_identifier
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [verification/v123_inventory_update.py](../../../../verification/v123_inventory_update.py#L1) · explicit_script_identifier
- [verification/v135_det_surface.py](../../../../verification/v135_det_surface.py#L1) · explicit_script_identifier
- [verification/v130_born_square.py](../../../../verification/v130_born_square.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v133) zeta budget ---- Numerical continuations are Python-only (mpmath); the exact arithmetic of both routes is mirrored, plus a numeric spot-check in WL. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L994)
- [(* ---- (v109) sheet pairing ---- *) Module[{splus, sminus, vecw, lamW, addW, crossT, formsEven, diagT, formsOdd, zmult}, splus = Select[Tuples[{1/2, -1/2}, 5], EvenQ[Count[#, -1/2]] &]; sminus = Select[Tuples[{1/2, -1/2}, 5], OddQ[Count[#, -1/2]] &]; vecw = Flatten[Table[s UnitVector[5, i], {i, 5}, {s, {1, -1}}], 1]; lamW[k_] := If[k == 0, {ConstantArray[0, 5]}, Total /@ Subsets[vecw, {k}]]; checkExact["v109 no scalar within a sheet: zero-weight mult of S+xS+ and S-xS- is 0", (Count[Flatten[Outer[Plus, splus, splus, 1], 1], ConstantArray[0, 5]] == 0) && (Count[Flatten[Outer[Plus, sminus, sminus, 1], 1], ConstantArray[0, 5]] == 0)]; crossT = Sort[Flatten[Outer[Plus, splus, sminus, 1], 1]]; checkExact["v109 cross-sheet zero-weight mult = 16 = 1+5+10 (Pascal triple)", Count[crossT, ConstantArray[0, 5]] == 16]; formsEven = Sort[Join[lamW[0], lamW[2], lamW[4]]]; checkExact["v109 EXACT multiset: S+xS- = Lambda^0+Lambda^2+Lambda^4 (256 = 1+45+210)", crossT === formsEven && Length[crossT] == 256]; diagT = Sort[Join[Flatten[Outer[Plus, splus, splus, 1], 1], Flatten[Outer[Plus, sminus, sminus, 1], 1]]]; formsOdd = Sort[Join[lamW[1], lamW[1], lamW[3], lamW[3], lamW[5]]]; checkExact["v109 sheet-diagonal = odd forms: (S+xS+)u(S-xS-) = 2L1+2L3+L5 (512)", diagT === formsOdd && Length[diagT] == 512]; zmult[k_] := Count[lamW[k], ConstantArray[0, 5]]; checkExact["v109 zero-mode grading (L0,L2,L4) -> (1,5,10) = the carrier code; tower tops at 2K = 4", ({zmult[0], zmult[2], zmult[4]} == {1, 5, 10}) && (4 == 2*2)]; ]; (* ---- (v110) Calderon-sheet selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L499)
- [(* ---- (v126) clock-wall bridge ---- *) Module[{a0, spec, lams}, a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; spec = Sort[Eigenvalues[a0]]; checkExact["v126 the weights are the parabolic weights: spec A0* = {0, 1/3, 2/3} = n/N_fam; bridge (1-alpha)^6 = {1, (2/3)^6, (1/3)^6}", spec == {0, 1/3, 2/3} && Sort[((1 - #)^6 &) /@ spec, Greater] == {1, (2/3)^6, (1/3)^6}]; checkExact["v126 checkpoint 1 + determinant: linear coefficient p2/N = 2 = |Z2| (= v104 entropy rate 2H); det(1 - A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L890)
- [(* ---- (v129) entropy power law ---- *) Module[{levels, lams, rates}, levels = Table[(3 - n)/3, {n, 0, 2}]; lams = levels^6; rates = 6 Log[1/levels]; checkExact["v129 entropy power law: S/S_dS = {1, 2/3, 1/3} = 1 - n/N; lambda = (S/S_dS)^6 = frozen spectrum; rates = {0, Delta, 6 ln 3}; alpha = deficit fraction; p2 = 6 = 2 N_fam", levels == {1, 2/3, 1/3} && lams == {1, (2/3)^6, (1/3)^6} && Simplify[rates[[2]] - 6 Log[3/2]] === 0 && Simplify[rates[[3]] - 6 Log[3]] === 0 && Table[n/3, {n, 0, 2}] == 1 - levels && 6 == 2*3 && rates[[1]] === 0 && levels[[1]] > levels[[2]] > levels[[3]]]; ]; (* ---- (v130) Born square ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L948)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v134) dual anchor ---- *) Module[{rmat, lmat, qmat, av, onev, e1v, nv, d, rinv1}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; lmat = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; av = {1, 1, 2}; onev = {1, 1, 1}; e1v = {1, 0, 0}; nv = {5, -9, 6}; d = av . Inverse[rmat]; rinv1 = Inverse[rmat] . onev; checkExact["v134 dual anchor: a.R^-1 = a.L^-1 = (-1/2,-1/2,1); d.1 = 0, d.a = 1; (1,1,-2) = -2d; d = (3/2)(a - (4/3)1)", d == av . Inverse[lmat] && d == {-1/2, -1/2, 1} && d . onev == 0 && d . av == 1 && {1, 1, -2} == -2 d && d == 3/2 (av - 4/3 onev)]; checkExact["v134 Sherman-Morrison: L = R + 6*1 e1^T; R^-1 1 = (1,1,-1)/4; a on the invariance plane, 1/e1/n not (1/4, 1/4, -5/2); n.1 = 2", lmat == rmat + 6 Outer[Times, onev, e1v] && rinv1 == {1/4, 1/4, -1/4} && av . rinv1 == 0 && onev . rinv1 == 1/4 && e1v . rinv1 == 1/4 && nv . rinv1 == -5/2 && nv . onev == 2]; ]; (* ---- (v135) determinant surface ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1010)
- [(* ---- (v140) canonical map ---- *) Module[{charf, cu, cmu, cw}, charf[m_] := Mod[Round[Arg[#]/(Pi/2)], 4] & /@ Diagonal[m]; cu = charf[DiagonalMatrix[{1, I, -I}]]; cmu = charf[-DiagonalMatrix[{1, I, -I}]]; cw = charf[DiagonalMatrix[{I, I^2, I^3}]]; checkExact["v140 canonical map: deck U chars (0,1,3) miss 2; -U = (2,3,1) and i^Q+ = (1,2,3) both have SET {1,2,3} = H^1; i^Q+ assignment = Q+, -U assignment = Q+ o rho (one Z3 rotation apart)", cu == {0, 1, 3} && cmu == {2, 3, 1} && cw == {1, 2, 3} && Sort[cmu] == {1, 2, 3} == Sort[cw] && cmu == (cw[[#]] & /@ {2, 3, 1})]; ]; (* ---- (v141) deck selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1122)
- [(* ---- (v136) dual-normal selector ---- *) Module[{dv, nv, av, rmat, qmat, kmat, sols, a0, v0, sigma, adjA0, grp, gens, reals}, dv = {-1/2, -1/2, 1}; nv = {5, -9, 6}; av = {1, 1, 2}; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; kmat = rmat + qmat . DiagonalMatrix[{1, -1, -1}]; sols = Table[Select[Tuples[Range[0, 5], 3], dv . # == av[[j]] && nv . # == 8 Boole[j == 1] &], {j, 3}]; checkExact["v136 column normal form: d.c_j = a_j, n.c_j = 8 delta_1j; kernel (6,8,7); each column UNIQUE in {0..5}^3 (1 of 216)", (dv . #) & /@ Transpose[rmat] == av && (nv . #) & /@ Transpose[rmat] == {8, 0, 0} && 7 First[NullSpace[{dv, nv}]] == {6, 8, 7} && Length /@ sols == {1, 1, 1} && (First /@ sols) == Transpose[rmat]]; checkExact["v136 honesty: K not pinned by (d,n) (d.K = (1,1/2,1), n.K = (14,1,-6)); det K = 4 via the diamond", dv . kmat == {1, 1/2, 1} && nv . kmat == {14, 1, -6} && Det[kmat] == 4]; a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; v0 = First[NullSpace[a0]]; v0 = v0/v0[[2]] 3; sigma = {2, -9, 5}; adjA0 = Transpose[Table[(-1)^(i + j) Det[Drop[a0, {i}, {j}]], {i, 3}, {j, 3}]]; checkExact["v136 spectral normal: A0* zero mode signed squares = -(2,-9,5); ||v||^2 = 16/9; adj(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1050)
- [(* v431 (3): 6k+2 family = {2} U det-ladder {8,14,20} on winding line 6s+8 *) fam2 = Sort[Select[degs, Mod[#, 6] == 2 &]]; R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; C = R + Q . DiagonalMatrix[{1, 0, 0}]; L = R + Q . DiagonalMatrix[{2, 0, 0}]; ladder = {Det[R], Det[C], Det[L]}; surf = Table[6 s + 8, {s, 0, 2}]; checkExact["v431 E8.DEGREE.LADDER.01 (iii): degrees==2 mod 6 = {2,8,14,20}; {8,14,20}=(det R,det C,det L)=winding line det M(s,0)=6s+8 (v135); 2=matched metric, 8=rank E8", fam2 == {2, 8, 14, 20} && ladder == {8, 14, 20} && ladder == surf && ladder[[1]] == 8]; (* v431 (4): 18 = 6*N_fam spine member, not det-ladder holdout *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2678)
- [(* ---- (v127) ring resummation ---- *) Module[{proj, partial}, proj = {{1, 0, 0}, {0, 0, 0}, {0, 0, 0}}; checkExact["v127 log-det identity: det(1 - a P) = 1 - a (rank-1 P); series -ln(1-a) = a + a^2/2 + a^3/3 + ...", Simplify[Det[IdentityMatrix[3] - a proj] - (1 - a)] === 0 && Normal[Series[-Log[1 - a], {a, 0, 3}]] === a + a^2/2 + a^3/3]; partial[al_, kmax_] := 6 Sum[al^j/j, {j, kmax}]; checkExact["v127 ring ladder: k=1 ring = classical (2, 4 at weights 1, 2); k=2 ring = 1/3 at weight 1; partials below exact and monotone", partial[1/3, 1] == 2 && partial[2/3, 1] == 4 && 6 (1/3)^2/2 == 1/3 && partial[1/3, 8] < -6 Log[1 - 1/3] && partial[1/3, 2] > partial[1/3, 1]]; checkExact["v127 coupling cross-link + wall: kappa_seam = 8/24 = 1/3 = alpha_1 (kappa = alpha_1/pi); ring series diverges at alpha -> 1", 8/24 == 1/3 && Limit[-Log[1 - a], a -> 1, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v128) graded hull ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L903)
- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* ---- (v131) measure is area ---- *) Module[{pref, harms, norms}, pref = Sqrt[3/(4 Pi)]; harms = {pref Cos[\[Theta]], pref Sin[\[Theta]] Cos[\[Phi]], pref Sin[\[Theta]] Sin[\[Phi]]}; norms = Table[Integrate[Integrate[y^2 rr^2 Sin[\[Theta]], {\[Theta], 0, Pi}], {\[Phi], 0, 2 Pi}], {y, harms}]; checkExact["v131 zero-mode norm = area: all three l=1 norms^2 = r^2 = A/(4pi); Jacobian bookkeeping (x^3)^2 = x^6; c3 = (1/2)(1/4pi)", AllTrue[norms, Simplify[# - rr^2] === 0 &] && Simplify[(4 Pi rr^2)/(4 Pi) - rr^2] === 0 && Simplify[(x^3)^2 - x^6] === 0 && 1/2 * 1/(4 Pi) == 1/(8 Pi)]; ]; (* ---- (v132) det-ratio anomaly ---- The numerical heat-trace continuation is Python-only (mpmath); the exact arithmetic is mirrored here, plus an independent exact check of the constant term via the full heat-trace expansion. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L968)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)

## 2026-06-11

[documents/changelog/sections/024-source.tex:76-108](../../../../documents/changelog/sections/024-source.tex#L76) · `section:9575cef792be9f73f7ff` · subsection

External-review integration (v83) and release hygiene. Manifest –check mode and the release rule; holomorphy pins [formula in source] (the unique even unimodular rank-8 lattice theory). Sheet diamond and centered form (v94/v95). All four flavor operators are points of one two-parameter surface [formula in source] ; centered cross [formula in source] , [formula in source] with the cofactor seam normal [formula in sour

Explicit source references:

- [verification/v118_hexagon_family_dictionary.py](../../../../verification/v118_hexagon_family_dictionary.py#L1) · explicit_script_identifier
- [verification/v94_sheet_diamond.py](../../../../verification/v94_sheet_diamond.py#L1) · explicit_script_identifier
- [verification/v95_centered_diamond.py](../../../../verification/v95_centered_diamond.py#L1) · explicit_script_identifier
- [verification/v109_sheet_pairing.py](../../../../verification/v109_sheet_pairing.py#L1) · explicit_script_identifier
- [verification/v101_horizon_anchor.py](../../../../verification/v101_horizon_anchor.py#L1) · explicit_script_identifier
- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [verification/v83_e8net_holomorphic_uniqueness.py](../../../../verification/v83_e8net_holomorphic_uniqueness.py#L1) · explicit_script_identifier
- [verification/v104_nariai_clock.py](../../../../verification/v104_nariai_clock.py#L1) · explicit_script_identifier
- [verification/v108_pascal_ladder.py](../../../../verification/v108_pascal_ladder.py#L1) · explicit_script_identifier
- [verification/v103_trisection_normal_form.py](../../../../verification/v103_trisection_normal_form.py#L1) · explicit_script_identifier
- [verification/v121_address_pinning.py](../../../../verification/v121_address_pinning.py#L1) · explicit_script_identifier
- [verification/v114_torsion_delta.py](../../../../verification/v114_torsion_delta.py#L1) · explicit_script_identifier
- [verification/v119_review_validation_2.py](../../../../verification/v119_review_validation_2.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v107) quantum-clock target ---- *) checkExact["v107 per-l clock: l=0 (la-1)(la+2), l=1 la(la+1); l>=2 complex Re=-1/2", (Factor[la^2 + la + (0 - 2)] == (la - 1) (la + 2)) && (Factor[la^2 + la + (2 - 2)] == la (la + 1)) && (Re[la /. Solve[la^2 + la + 4 == 0, la]] == {-1/2, -1/2})]; checkExact["v107 cusp-ladder cross-link: decay set {0,-1,-2} = -Spec(Q diag(0,1,1)) = -N_fam x cusp", Module[{Vw = Q.DiagonalMatrix[{0, 1, 1}]}, Sort[Eigenvalues[Vw]] == {0, 1, 2}]]; checkExact["v107 exact target: (1/3)^6 = ((2/3)^6)^{log_{3/2}3}; ratio = 1 + log_{3/2}2", (FullSimplify[-6 Log[3] - (Log[3]/Log[3/2]) (6 Log[2] - 6 Log[3])] === 0) && (FullSimplify[Log[3]/Log[3/2] - (1 + Log[2]/Log[3/2])] === 0)]; check["v107 bend log_{9/4}(3) = 1.354756; seam coupling 1/(3Pi) = 0.106103", Log[3]/Log[9/4], 1.3547556457`10, 10^-9]; (* ---- (v108) Pascal ladder ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L471)
- [(* ---- (v109) sheet pairing ---- *) Module[{splus, sminus, vecw, lamW, addW, crossT, formsEven, diagT, formsOdd, zmult}, splus = Select[Tuples[{1/2, -1/2}, 5], EvenQ[Count[#, -1/2]] &]; sminus = Select[Tuples[{1/2, -1/2}, 5], OddQ[Count[#, -1/2]] &]; vecw = Flatten[Table[s UnitVector[5, i], {i, 5}, {s, {1, -1}}], 1]; lamW[k_] := If[k == 0, {ConstantArray[0, 5]}, Total /@ Subsets[vecw, {k}]]; checkExact["v109 no scalar within a sheet: zero-weight mult of S+xS+ and S-xS- is 0", (Count[Flatten[Outer[Plus, splus, splus, 1], 1], ConstantArray[0, 5]] == 0) && (Count[Flatten[Outer[Plus, sminus, sminus, 1], 1], ConstantArray[0, 5]] == 0)]; crossT = Sort[Flatten[Outer[Plus, splus, sminus, 1], 1]]; checkExact["v109 cross-sheet zero-weight mult = 16 = 1+5+10 (Pascal triple)", Count[crossT, ConstantArray[0, 5]] == 16]; formsEven = Sort[Join[lamW[0], lamW[2], lamW[4]]]; checkExact["v109 EXACT multiset: S+xS- = Lambda^0+Lambda^2+Lambda^4 (256 = 1+45+210)", crossT === formsEven && Length[crossT] == 256]; diagT = Sort[Join[Flatten[Outer[Plus, splus, splus, 1], 1], Flatten[Outer[Plus, sminus, sminus, 1], 1]]]; formsOdd = Sort[Join[lamW[1], lamW[1], lamW[3], lamW[3], lamW[5]]]; checkExact["v109 sheet-diagonal = odd forms: (S+xS+)u(S-xS-) = 2L1+2L3+L5 (512)", diagT === formsOdd && Length[diagT] == 512]; zmult[k_] := Count[lamW[k], ConstantArray[0, 5]]; checkExact["v109 zero-mode grading (L0,L2,L4) -> (1,5,10) = the carrier code; tower tops at 2K = 4", ({zmult[0], zmult[2], zmult[4]} == {1, 5, 10}) && (4 == 2*2)]; ]; (* ---- (v110) Calderon-sheet selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L499)
- [(* ---- (v120) address table ---- *) Module[{pp, llep, lqrk, addr, up, down}, pp[n_] := 2 + 2^n; llep = {8, 5, 3}; lqrk = {7, 7, 5, 3, 2, 0}; checkExact["v120 lepton words = compiler atoms: (8,5,3) = (rank E8, g_car, N_fam) = (p0+e2, e2, p0); sum = 16 = dim S+", llep == {3 + 5, 5, 3} && Total[llep] == 16]; addr = {Mod[#, 6], Quotient[#, 6]} & /@ llep; checkExact["v120 addresses = division by hexagon p2 = 6: (r,w) = {(2,1),(5,0),(3,0)}; sum r = 10 = p3", addr == {{2, 1}, {5, 0}, {3, 0}} && Total[addr[[All, 1]]] == pp[3] && pp[2] == 6]; up = 7 + 3 + 0; down = 7 + 5 + 2; checkExact["v120 quark sum rules: up = 10 = p3, down = 14 = p1+p3, quarks = 24 = |W(A3)|, all nine = 40 = p1 p3; top at vacuum site (0,0)", up == pp[3] && down == pp[1] + pp[3] && up + down == 24 && Total[llep] + up + down == pp[1] pp[3] && Mod[0, 6] == 0 && Quotient[0, 6] == 0]; ]; (* ---- (v121) address pinning ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L799)
- [(* ---- (v218) DIAMOND.AXIS/PLUCKER/SPECTRAL.01: the diamond axis geometry ---- *) Module[{R, Q, a, one, Cc, U, V, K, L, F, anc, plL, ram, x, y, dU, dV, bU, bV, sd, bsd, sq, ker}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; one = {1, 1, 1}; a = {1, 1, 2}; Cc = R + Q.DiagonalMatrix[{1, 0, 0}]; (* center C = M(1,0) (v95) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1751)
- [(* ---- (v126) clock-wall bridge ---- *) Module[{a0, spec, lams}, a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; spec = Sort[Eigenvalues[a0]]; checkExact["v126 the weights are the parabolic weights: spec A0* = {0, 1/3, 2/3} = n/N_fam; bridge (1-alpha)^6 = {1, (2/3)^6, (1/3)^6}", spec == {0, 1/3, 2/3} && Sort[((1 - #)^6 &) /@ spec, Greater] == {1, (2/3)^6, (1/3)^6}]; checkExact["v126 checkpoint 1 + determinant: linear coefficient p2/N = 2 = |Z2| (= v104 entropy rate 2H); det(1 - A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L890)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [(* ---- (v101) horizon anchor: SdS in seam units ---- *) fSdS = 1 - 2 mm/rr - LL rr^2/3; cubicSdS = Expand[-fSdS 3 rr/LL]; narSol = Solve[{cubicSdS == 0, D[cubicSdS, rr] == 0}, {rr, mm}, Assumptions -> LL > 0]; checkExact["v101 Nariai double root: M_N = 1/(3 Sqrt[L]) = 1/(N_fam Sqrt[L]), r_N = 1/Sqrt[L]", MemberQ[Simplify[{rr, mm} /. narSol], {1/Sqrt[LL], 1/(3 Sqrt[LL])}]]; checkExact["v101 Nariai cubic = t^3 - 3t + 2 = (t-1)^2(t+2): roots (1,1,-2) = traceless anchor", (Expand[(t - 1)^2 (t + 2)] == t^3 - 3 t + 2) && (Simplify[{1, 1, 2} - (4/3) {1, 1, 1} - (-1/3) {1, 1, -2}] == {0, 0, 0})]; checkExact["v101 Koide 2/3 = Nariai entropy bound: S_N/S_dS = 2/3, per horizon 1/3, deficit 1/3", ((2 Pi/LL)/(3 Pi/LL) == 2/3) && ((Pi/LL)/(3 Pi/LL) == 1/3)]; checkExact["v101 interpolation S_tot/S_dS = (x^2+1)/(x^2+x+1) (denominator = Phi_3), min at merge", (Simplify[(xx^2 + 1)/(xx^2 + xx + 1) - (Pi (xx^2 + 1) 3/(LL (xx^2 + xx + 1)))/(3 Pi/LL)] === 0) && (Cyclotomic[3, xx] == xx^2 + xx + 1) && (((xx^2 + 1)/(xx^2 + xx + 1) /. xx -> 0) == 1) && (((xx^2 + 1)/(xx^2 + xx + 1) /. xx -> 1) == 2/3)]; checkExact["v101 three-sheet conservation: Sum r_i^2 = 2(rb^2+rb rc+rc^2) for roots (rb, rc, -(rb+rc))", Expand[rbb^2 + rcc^2 + (rbb + rcc)^2 - 2 (rbb^2 + rbb rcc + rcc^2)] === 0]; checkExact["v101 Q_geom range: pure dS -> 1/2 = delta, Nariai -> 3/8 = p2(a)/e1(a)^2 = SU(4)_1 weights", Module[{Qg = (xx^2 + (xx + 1)^2 + 1)/(4 (xx + 1)^2)}, ((Qg /. xx -> 0) == 1/2) && ((Qg /. xx -> 1) == 3/8) && (6/16 == 3/8)]]; checkExact["v101 mass-line double cover: disc = (108/L^3)(1-9 L M^2) -> (1-3m)(1+3m), branch +-1/N_fam", (Simplify[Discriminant[cubicSdS, rr] - 108/LL^3 (1 - 9 LL mm^2)] === 0) && (Expand[(1 - 3 md) (1 + 3 md) - (1 - 9 md^2)] === 0)]; checkExact["v101 temperature lemma: |kappa_b/kappa_c| = (2x+1)/(x(x+2)), = 1 iff x = 1", Module[{ff, kb, kc}, ff = -LL/(3 rr) (rr - rbb) (rr - rcc) (rr + rbb + rcc); kb = D[ff, rr] /. rr -> rbb; kc = D[ff, rr] /. rr -> rcc; Simplify[(kb/-kc /. rbb -> xx rcc) - (2 xx + 1)/(xx (xx + 2)), Assumptions -> rcc > 0 && xx > 0 && xx < 1] === 0]]; checkExact["v101 seam-unit mechanics: 1/(8Pi) = c3; Smarr 1/(4Pi) = 2c3; Bekenstein 2Pi = 1/(4c3); P_H 15360 Pi = 1920/c3; lifetime 5120 Pi = 128*5/c3; Kerr A_ext = M^2/c3; 4 Log[3] = Log[81]", (1/(8 Pi) == c3) && (Simplify[1/(4 Pi) - 2 c3] === 0) && (Simplify[2 Pi - 1/(4 c3)] === 0) && (Simplify[1/(15360 Pi) - c3/1920] === 0) && (Simplify[5120 Pi - 128*5/c3] === 0) && (Simplify[8 Pi - 1/c3] === 0) && (Simplify[4 Log[3] - Log[81]] === 0)]; (* ---- (v102) seam orientation: anchor = stationary repeller, both sectors ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L333)
- [experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean#L1)
- [(* ---- (v95) centered flavor diamond ---- *) Uop = Q.DiagonalMatrix[{1, 0, 0}]; Vop = Q.DiagonalMatrix[{0, 1, 1}]; Cc = R + Uop; Lop = R + 2 Uop; Fop = R + Q; checkExact["v95 centered cross: Q=U+V; R=C-U, L=C+U, K=C-V, F=C+V", (Q == Uop + Vop) && (R == Cc - Uop) && (Lop == Cc + Uop) && (K == Cc - Vop) && (Fop == Cc + Vop)]; checkExact["v95 axes spectra: Spec U = {3,0,0} (winding), Spec V = {0,1,2} = N_fam*cusp", (Sort[Eigenvalues[Uop]] == {0, 0, 3}) && (Sort[Eigenvalues[Vop]] == {0, 1, 2})]; checkExact["v95 center invariants: tr C=12, det C=14, sum C=31=2^g_car-1, det B_C=28", (Tr[Cc] == 12) && (Det[Cc] == 14) && (Total[Cc, 2] == 31) && (31 == 2^gcar - 1) && (Det[bb[Cc]] == 28)]; checkExact["v95 ray alignment: Pi_R(C)=7(2,3,1), Pi_R(L)=10(2,3,1)", (plR[Cc] == 7 {2, 3, 1}) && (plR[Lop] == 10 {2, 3, 1})]; (* ---- (v96) branch-kernel selection (P1) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L204)
- [(* ---- (v103) trisection normal form ---- *) checkExact["v103 trisection: r = 2 cos(theta) => r^3 - 3r = 2 cos(3 theta) exactly", Simplify[(2 Cos[th])^3 - 3 (2 Cos[th]) - 2 Cos[3 th]] === 0]; rcT = 2 Cos[(ps + Pi)/3]; rbT = 2 Cos[(ps - Pi)/3]; r3T = 2 Cos[(ps + 3 Pi)/3]; checkExact["v103 centered angle: m = cos(psi)/3; roots sum 0, e2 = -3; Nariai roots (1,1,-2) at psi = 0", (Simplify[-Cos[ps + Pi]/3 - Cos[ps]/3] === 0) && (Simplify[rcT + rbT + r3T] === 0) && (Simplify[rcT rbT + rcT r3T + rbT r3T + 3] === 0) && (Simplify[{rcT, rbT, r3T} /. ps -> 0] == {1, 1, -2})]; sigT = Simplify[(rbT^2 + rcT^2)/3]; checkExact["v103 NORMAL FORM: sigma(psi) = 4/3 - (2/3) cos(2 psi/3); sigma(0) = 2/3, sigma(pi/2) = 1", (Simplify[sigT - (4/3 - (2/3) Cos[2 ps/3])] === 0) && (Simplify[sigT /. ps -> 0] == 2/3) && (Simplify[sigT /. ps -> Pi/2] == 1)]; checkExact["v103 canonical curvature sigma''(0) = 8/27 = (2/3)^3 (the Koide constant to the family power)", (Simplify[D[sigT, {ps, 2}] /. ps -> 0] == 8/27) && ((2/3)^3 == 8/27)]; checkExact["v103 invariant base slope: dsigma/dm = -(4/3) sin(2 psi/3)/sin(psi), limit -8/9 = -rank(E8)/N_fam^2", (Simplify[D[sigT, ps]/D[Cos[ps]/3, ps] + (4/3) Sin[2 ps/3]/Sin[ps]] === 0) && (Limit[D[sigT, ps]/D[Cos[ps]/3, ps], ps -> 0] == -8/9)]; checkExact["v103 x-coordinate cross-check: m(x) deck-invariant, m''(1) = -1/4, sigma''(1)/m''(1) = -8/9", Module[{mxw = Sqrt[3]/2 xx (1 + xx)/(xx^2 + xx + 1)^(3/2), sxw = (xx^2 + 1)/(xx^2 + xx + 1)}, (Simplify[(mxw /. xx -> 1/xx) - mxw, Assumptions -> xx > 0] === 0) && (Simplify[D[mxw, xx] /. xx -> 1] == 0) && (Simplify[D[mxw, {xx, 2}] /. xx -> 1] == -1/4) && (Simplify[(D[sxw, {xx, 2}] /. xx -> 1)/(D[mxw, {xx, 2}] /. xx -> 1)] == -8/9)]]; checkExact["v103 bridge: (2/3)^6 = ((2/3)^3)^2 -- same base, exponent ratio 2 = |Z2|", (2/3)^6 == ((2/3)^3)^2]; (* ---- (v104) the classical Nariai clock ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L392)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)

## tfptblue Formal Verification of TFPT Carrier Rigidity in Lean 4\\[0.4em] An Audited Dependency Graph from the Boundary Involution\\ to the Standard-Model [formula in source] \ Hypercharge Carrier

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/preamble.tex:1-60](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/preamble.tex#L1) · `section:01e6b4359c05da0e8680` · frontmatter

tfptgray TFPT Lean Note: Carrier Rigidity Audit Harness tfptgray

Explicit source references:

- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)

## Front matter / support

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/001-section-what-this-note-is-about.tex:1-267](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/001-section-what-this-note-is-about.tex#L1) · `section:25a09b35c9322690a2b6` · frontmatter

This note documents a Lean 4 formalisation of the algebraic carrier rigidity theorem of TFPT Paper 2 ( Carrier Rigidity, Hypercharge, and the Standard-Model Packet from Boundary Polarization), up to and including the determinant-normalised [formula in source] hypercharge carrier [formula in source] . The bundled top-level theorem consumes four explicit interfaces: a carrier involution, Higgs and Yukawa rank witnesses

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [BoundaryPolarization.ofCarrierInvolution](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L184) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)

## What remains is upstream TFPT theory work.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:167-190](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L167) · `section:458a3ef36e2c278139fa` · paragraph

The Lean chain takes the Stage D quadruple [formula in source] as input. The remaining open question is whether TFPT itself produces such a quadruple from the boundary kernel. Concretely:

## Remaining limitations of the Lean chain itself.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:191-238](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L191) · `section:35345827b51908140e58` · paragraph

Calder\'on: two structural layers formalised, analytic input of the polarisation open.\ CalderonProjector proves [formula in source] , and BoundaryPolarization (v10) shows that any direct-sum decomposition [formula in source] of a [formula in source] -module produces such an idempotent via Mathlib's IsCompl.projection. What remains is the analytic Paper 1 theorem producing the boundary spectral decomposition itself —

Explicit source references:

- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)

## Other items deliberately out of scope.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:239-251](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L239) · `section:02393735276ef9585ebf` · paragraph

Full [formula in source] -quotient theorem for [formula in source] . Derived Standard-Model representations (dual, exterior powers, tensor products); the diagonal formalised here is the carrier hypercharge, not the full SM hypercharge spectrum. Analytic content of Paper 1 (Calder\'on polarisation, boundary elliptic theory).

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

## 11. Reproduktionsumfang

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex:1-20](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex#L1) · `section:49f368bb92a717229580` · subsection

Der gemeinsame Replay führt alle eigenen mathematischen Prüfer normal und optimiert mit Warnungen als Fehler aus. Die Teilberichte unterscheiden exakte Identitäten von numerischen Kontrollen. Die 57 Prüfbedingungen des gelieferten Papers und dessen 20 übernommene Kettenprüfungen werden separat ausgewiesen, nicht als neue eigene Entdeckungen addiert. Sie decken nicht automatisch jeden Satz des Papers ab; die Korrektur

## D. Weitere Übernahmegrenzen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex:179-209](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex#L179) · `section:cab35a8ac53284475c8f` · subsection

Die Clock ist nach der späteren konkreten Konstruktion ein Element der inneren Spin(10)-Darstellung. Die ältere Formulierung „äußerer Handgriff`` wird nicht als neue Herkunftstatsache übernommen. Die große Kommutantdimension zählt nicht direkt physische Freiheitsgrade. Ein skalarer Kommutant bedeutet nicht automatisch beliebige dynamische Kontrolle. Als exakter Gegenzeuge haben Spin-1-Kontrollen einen skalaren Kommut

## Automatisch aus dem abgeschlossenen Replay

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex:275-306](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/003-subsection-11-reproduktionsumfang-label-reproduktionsumf.tex#L275) · `section:e8c648e4f48eab73c01f` · subsubsection

@lrr@ Eigener Strang & Exakte Bedingungen & Numerische Bedingungen \\ causal & 662 & 10 \\ common3 & 43 & 0 \\ late_field & 36 & 0 \\ late_moments & 2 & 2 \\ late_norm & 36 & 10 \\ mechanism & 261 & 0 \\ phase_bridge & 32 & 0 \\ resource_boundary & 24 & 0 \\ shadows & 5417 & 17 \\

## 2. Geschlossener Erhaltungssatz für das dokumentierte Alphabet

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/004-subsection-1-was-die-tats-chlichen-quellen.tex:78-138](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/004-subsection-1-was-die-tats-chlichen-quellen.tex#L78) · `section:b766321aff43d5c9ecd8` · subsection

hat jedes der 480 signierten Wechselwirkungsmonome Ladung +2−1−1=0. Nb, alle Modenbesetzungen und alle passiven Bilineare f†Af beziehungsweise b†Cb sind ebenfalls neutral. Die dokumentierten inneren Liegeneratoren werden genau auf diese Weise zweitquantisiert. Die Clock schickt f† nach GF f† und b† nach GB b†, mischt also keine Erzeuger mit Vernichtern.

## 6. Ressourcenbilanz und der jetzt konkrete nächste Nachweis

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/005-subsection-6-ressourcenbilanz-und-der-jetzt-konkrete-n-c.tex:1-58](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/005-subsection-6-ressourcenbilanz-und-der-jetzt-konkrete-n-c.tex#L1) · `section:730fbc4f55abaa00acc6` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Ressource & Herkunft im geprüften Vertrag & Was noch zu liefern wäre \\ W, η, innere Darstellung, endliche Clock & Tatsächliche Quellkonstruktion und erneuter exakter Replay & Physische Identifikation des Trägers \\ Hnat mit Δ,g & Bestehender ausdrücklich festgelegter Modellvertrag & Physische Auswahl und Kalibrierung \\ Zweizustandsblock β↔ρ & Neue volls

## 4. Was bereits überholt ist

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/008-subsection-3-der-text-vermischt-drei-verschiedene.tex:107-153](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/008-subsection-3-der-text-vermischt-drei-verschiedene.tex#L107) · `section:34327224462429251911` · subsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage der Anlage & Prüfung \\ Clock sei ein äußerer Handgriff, weil er Gewichte verschiebt & Bereits in v1.6.6/7 durch das explizite Spin(10)-Wort widerlegt. Nichtskalare Wirkung innerhalb eines Irreps bedeutet keine äußere Symmetrie. Die aktuelle Mechanismusprüfung reproduziert zudem den ursprünglichen Clock und seinen passiven Focklift. \\ Mit allen gewährten inneren Kon

## Nachtrag C: überwiegend bereits abgedeckte fundamentale Reduktion

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex:127-129](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex#L127) · `section:c72e6bc56a056fdf065f` · section

No opening prose excerpt; see the source.

## Was bestätigt und bereits abgedeckt ist

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex:152-206](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex#L152) · `section:7727bcd80eda98b5a7f9` · subsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage & Urteil und Grenze \\ Volle Schur-Antwort T†F(H−E0)T=γF I64 & Richtig bei gruppeninvariantem H und Grundzustand sowie irreduziblem ursprünglichem Entnahmemultiplett. Gilt für die volle beschränkte Spektralfunktion, nicht nur einen dominanten Pol. Schon in v1.6.7 BIG_PICTURE B2 und der eingefrorenen Kurzfassung enthalten. \\ Aus C_rs(t)=δ_rs c(t) folgt kein Ortsindex

## Zwei Präzisierungen bei der Übernahme

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex:253-279](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/009-subsection-3-die-neue-pr-zise.tex#L253) · `section:5836bda6b354d5019788` · subsection

In §7 sollte „ein positiver Unterschied`` durch „eine nichtverschwindende Differenz`` ersetzt werden. Ein negativer signierter Unterschied ist ebenso ein kausaler Interventionsnachweis; genau dies zeigt der neue N=2-Phasenversuch. Die globale Sektorwahl und die Beobachtbarkeit innerhalb eines festen Gesamtsektors getrennt halten. Ein System-Referenz-Vergleich kann relative Ladungsenergien aufdecken; ein Zusatz μN_tot

## 6.2 Warum bloßes Lesen noch keine fehlende Bewegung erzeugt

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/011-subsubsection-4-3-zehn-vollst-ndige-energiemomente-der-g.tex:161-178](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/011-subsubsection-4-3-zehn-vollst-ndige-energiemomente-der-g.tex#L161) · `section:30bda1816c3dc0b64295` · subsubsection

Ohne die zusätzlich gewährten Gruppenkontrollen erhalten X, Nb, der Clock und alle Modenbesetzungen weiterhin mindestens eine nichtskalare Farb-Cartanladung. Jede Komposition dieser Operatoren behält diese Erhaltung. Die alleinige Erlaubnis, mehr Moden zu unterscheiden, hebt das Hindernis also nicht auf.

## 8.1 Ein überprüfbarer Unterbestimmtheitssatz

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/011-subsubsection-4-3-zehn-vollst-ndige-energiemomente-der-g.tex:213-241](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/011-subsubsection-4-3-zehn-vollst-ndige-energiemomente-der-g.tex#L213) · `section:b791ebe659805af6a046` · subsubsection

Betrachte bei festem W dieselbe Familie [formula in source] . Alle diese Hamiltonoperatoren besitzen die gleiche innere Quellsymmetrie, dieselbe Ladungserhaltung und denselben kommutierenden endlichen Clock. Dennoch unterscheiden sie sich dynamisch. Schon für dieselbe gefüllte Referenz F ist die dimensionslose Momentenkombination

## TFPT / Universalraum: Clock, gemeinsame Quelle und tatsächlicher Transport

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/013-subsubsection-b5-2-warum-das-noch-kein-holografischer.tex:293-296](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/013-subsubsection-b5-2-warum-das-noch-kein-holografischer.tex#L293) · `section:cc26d361ce575668b6da` · section

No opening prose excerpt; see the source.

## Konsolidierung und eigene Forschungsfortsetzung v1.6.6 - 15. September 2026

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/013-subsubsection-b5-2-warum-das-noch-kein-holografischer.tex:297-322](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/013-subsubsection-b5-2-warum-das-noch-kein-holografischer.tex#L297) · `section:dc0a6d7395c92312f241` · subsection

Ergebnis: Der dokumentierte endliche Clock ist jetzt ausdrücklich als Element der vorhandenen inneren Spin(10)-Symmetrie konstruiert. Dadurch lässt sich die bislang offene gemeinsame Clock-/Casimir-Auslesung exakt bestimmen. Daneben wurde ein kleiner, echter Vierzustandskanal der ursprünglichen Paarwechselwirkung gefunden, der nach Zulassung eines Bosonmischers eine Fermionenmarke überträgt. Die Herkunft dieses Misch

## 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex:4-83](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex#L4) · `section:bd201db4b26077af03ab` · subsubsection

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-, Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch reproduziert. Darunter befinden sich neun wörtliche need(True, ...)-Guards mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu; Abschnitt 3 ersetzt sie durch eine explizite Konstru

## 3. Neuer exakter Anschluss: Der Clock liegt bereits in Spin(10)

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex:139-141](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex#L139) · `section:e0a0c9335b62790fbffd` · subsection

No opening prose excerpt; see the source.

## 3.1 Ausgangspunkt ist der tatsächliche Quell-Clock

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex:142-158](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex#L142) · `section:8bd609e76a1a81b80976` · subsubsection

Der gepinnte endliche Compilerpräfix liefert auf fünf Hilfsachsen

## 4. Clock und getrennte Casimire lassen sich gemeinsam auslesen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex:216-294](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/014-subsection-2-quellenpr-fung-der-beiden-neuen.tex#L216) · `section:8913fe068a17b55fa91c` · subsection

Weil G aus Spin(10) stammt und auf SU(4) trivial wirkt, kommutiert es mit beiden getrennten Casimiren, auch auf ihren Fockhebungen. Die Frage aus dem neuen Text ist damit auf algebraischer Ebene beantwortet.

## 8. T1-T8: gemeinsamer Fortschritt ohne Statusinflation

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex:187-237](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex#L187) · `section:ea0714b4c66468db184f` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Front & In dieser Revision weitergekommen & Noch erforderlicher Nachweis \\ T1 - Ursprung und Auswahl & Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer & Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand \\ T2 - Half-Charge/E8-Feld & Bestehender geladener Pol bleibt abgesichert, innere Dar

## 10. Belege und Reproduzierbarkeit

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex:272-293](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/015-subsection-6-das-feldw-rterbuch-eine-basis-nderung-allei.tex#L272) · `section:6a66c45dec9591f482eb` · subsection

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit reproduziert die 1127 gelieferten Guards; eigene Programme behandeln Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion, basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählu

## 5. Der Clock-Satz ist im gelieferten Checker nicht geprüft

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/016-subsection-2-best-tigte-mathematik-label-bestuxe4tigte-m.tex:130-148](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/016-subsection-2-best-tigte-mathematik-label-bestuxe4tigte-m.tex#L130) · `section:d4a842653c33d0323e73` · subsection

operation_symmetry.py:478 schreibt den Normalisator- und Nichts-hinzufügen-Satz als need(True, ...). Insgesamt enthält diese Datei neun solche als Prüfbedingungen gezählten theoretischen Folgerungen. Einige sind durch die vorausgehende Mathematik gut begründet; der bloße grüne Guard zertifiziert sie jedoch nicht unabhängig.

## 1. Warum eine Clockphase die bisherige Paritätsschranke nicht aufhebt

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/017-subsection-4-der-bereits-bewiesene-native-grundsatz-blei.tex:216-254](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/017-subsection-4-der-bereits-bewiesene-native-grundsatz-blei.tex#L216) · `section:35fb31b0f0e1ec2c7ac5` · subsection

Seien zwei operational unabhängig definierte Banken mit lokalen Paritäten

## 6.2 Tatsächlicher endlicher Clock statt unterstellter voller Gruppe

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/018-subsection-3-exakter-vierzustandskanal-mit-dem-vollst-nd.tex:271-328](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/018-subsection-3-exakter-vierzustandskanal-mit-dem-vollst-nd.tex#L271) · `section:095e48d2c10ff1baf309` · subsubsection

Die Prüfung lädt den gepinnten ursprünglichen Clock-Konstruktor über

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/sources/repo/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/sources/repo/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py#L1) · explicit_file_citation

## 6.3 Clock-Mittelung ist möglich, aber der Farb-Cartan sperrt sie weiterhin

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/018-subsection-3-exakter-vierzustandskanal-mit-dem-vollst-nd.tex:329-394](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/018-subsection-3-exakter-vierzustandskanal-mit-dem-vollst-nd.tex#L329) · `section:eb8b79f92ec9d6b7e899` · subsubsection

Der Clock-Ausschluss allein wäre zu schwach. Die Orbitsumme

## 8. Während der Arbeit entdeckte Änderung: „Kommutant 7`` richtig einordnen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/022-subsection-5-warum-die-herkunftsl-cke-nicht-durch-l-nger.tex:170-228](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/022-subsection-5-warum-die-herkunftsl-cke-nicht-durch-l-nger.tex#L170) · `section:dcca08f91b7edee05576` · subsection

Die strikte Originalquellenprüfung stoppte korrekt, als eine andere Arbeit den früheren nativen Bericht ergänzte. Der alte Stand mit Hash 1062e13fe0fb79cce015657a7b4d40a61e9639922ff95fa60c689c0068c38ffc blieb eingefroren. Der gesonderte geänderte Entwurf hat Hash ab745e74b1232b1ddf35dd0e0d0da4ace0176c797d769e5db8bedd0010bcba6a. Die in dieser Revision verwendeten Energie- und Polzertifikate änderten sich bei dieser Pr

## Die Kommutanten-Leiter (N=3-Sektor, 45 504-dim)

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/026-section-nutzerquelle-a-vollst-ndige-runde.tex:335-363](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/026-section-nutzerquelle-a-vollst-ndige-runde.tex#L335) · `section:c01237afb611d27afb7e` · subsubsection

@lrr@ Operationssatz & erzeugte Algebra & Kommutante \\ S0: \X, N_b\ & 14 & 1 444 233 216 \\ S1: + Spin(10)×SU(4)-Rahmen & 743 583 744 & 7 \\ S2: + Clock-Lift & unverändert & 7 \\ S3: + Modenbesetzungen \n_r, m_A\ & M₄₅₅₀₄ (2 070 614 016) & 1 \\ S4: + geladene f-Instrumente & M₄₇₅₈₀ (N=2∪N=3) & 1 \\

Explicit source references:

- [experiments/theory-contracts/universalraum-relational-hole-20260915/minimal_interfaces.py](../../../../experiments/theory-contracts/universalraum-relational-hole-20260915/minimal_interfaces.py#L1) · explicit_file_citation

## 2. Unveränderte Quelle und Konventionen

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/031-section-tfpt-universalraum-operationssatz-nativer-grundz.tex:38-56](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/031-section-tfpt-universalraum-operationssatz-nativer-grundz.tex#L38) · `section:0a0955454adeb5051086` · subsection

Der Tensor wird repo-lokal gelesen (SHA-256 3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763), der Clock-Konstruktor ist gepinnt ( 9bf99de7…). common.py prüft: 60 Kanäle × 8 disjunkte Paare, jede Mode in 15 Kanälen; Gewichtserhaltung auf allen 480 Paaren; die Casimir-Identität 8WᵀW + 𝒞_S + 𝒞_C − 120 I = 0 auf allen 2016 Zweiteilchenzuständen (𝒞 = −ΣL², d. h. viermal der Standard-Casimir); induzierte B

## 3.2 Kommutanten-Leiter

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/031-section-tfpt-universalraum-operationssatz-nativer-grundz.tex:109-154](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/031-section-tfpt-universalraum-operationssatz-nativer-grundz.tex#L109) · `section:c5721e1100fdcf3ab99f` · subsubsection

@ > p( - 4 ) * 0.2727 > p( - 4 ) * 0.3636 > p( - 4 ) * 0.3636@ Verfügbare Operationen & N=2 & N=3 \\ A: \X, N_b\ (die zwei bisher geprüften Kontrollen) & 3 829 536 & 1 444 233 216 \\ B: A + Clock (Ordnung 6) & 641 760 & 240 742 144 \\ Cc: A + 15 su(4)-Generatoren & 30 376 & 2 247 168 \\ Cs: A + 45 so(10)-Generatoren & 172 & 1 648 \\ C: A + alle 60 Generatoren & 3 & 7 \\ D: B + C & 3 & 7 \\ B(H_N) & 1 & 1 \\

## 7. T1-T8

[documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/032-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex:22-62](../../../../documents/experiments--theory-contracts--universalraum-common-process-20260915--tmp--pdfs--TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8/sections/032-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex#L22) · `section:db3cd3f398aea37bc140` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Tor & Beitrag dieser Runde & Weiter offen \\ T1 & Exakte Kommutanten-Leiter A→B→Cc→Cs→C; Clock als äußeres Symmetrieelement & Welche Symmetrieoperationen der Compiler tatsächlich bereitstellt \\ T2 & Lochbild bewiesen; Z_h + Z_add = 1; ε_h, ε_add & Konvergierter Zustand, Renormierung, Grenzraum \\ T3 & - (ausgeklammert) & Räumlicher Träger \\ T4 & Kern-Sy

## TFPT-Anschluss: Zustandsgate, Trägerzellen und der [formula in source] -Faktor des Seams\\ Ergebnisse der Fable-Runden 3 (11.–14.\ September 2026) als Fortsetzung des Manuskripts Vom geometrischen Compiler zum Prozess mit Aufzeichnung (Version 1.1)

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/preamble.tex:1-25](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/preamble.tex#L1) · `section:2c91d319f950b6b851fb` · frontmatter

satzSatz lemma[satz]Lemma TFPT-Anschluss: Zustandsgate, Trägerzellen und der [formula in source] -Faktor des Seams\\ Ergebnisse der Fable-Runden 3 (11.–14.\ September 2026) als Fortsetzung des Manuskripts Vom geometrischen Compiler zum Prozess mit Aufzeichnung (Version 1.1) Claude Fable 5.1 im Cursor-Fenster tfpt-theoryv4\\ für Stefan Hamann\\ Prüfer und Zahlen: experiments/theory-contracts/\\ universalraum-fable-ker

## Front matter / support

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:1-3](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L1) · `section:356cc134d2b0054e3ef5` · frontmatter

No opening prose excerpt; see the source.

## Evidenzkonvention und Abgrenzung

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:4-6](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L4) · `section:5f952ab932298d5fceb2` · section

Wie im Manuskript: gesetzt bezeichnet eine Ausgangsannahme, exakt eine Identität oder einen Beweis unter genannten Voraussetzungen, bedingt eine Folgerung mit zusätzlicher physikalischer Zuordnung, offen eine ungeschlossene Herkunfts- oder Existenzfrage. Alle Zahlen stammen aus den in Anhang A genannten Prüfern; jeder läuft normal und unter python -OO bytegleich. Kein Marker im Ledger wurde bewegt. Alle physikalische

## Zusammenfassung

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:7-19](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L7) · `section:5b6b5fa61e78c1af1dcc` · section

Das Manuskript vom 14.\ September endet mit drei Fragen: Folgt die Wechselwirkung aus dem Compiler? Wie entsteht Veränderung und eine auslesbare Uhr? Was passiert bei vielen gekoppelten Zellen? Alle drei werden hier gerechnet, nicht vorgeschlagen.

Explicit source references:

- [verification/v993_minimal_defect_selector.py](../../../../verification/v993_minimal_defect_selector.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v993) AX.P2.01 census: SNF disc groups, unique (D5,A3), [lambda]^2=[v], CE dims ---- Python-only: random CE axiom sampling on M_d^{Z4} / crossed product. *)](../../../../verification/wolfram/tfpt_readouts.wl#L557)

## Ausgangslage

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:20-26](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L20) · `section:5926380330792d2bbe2b` · section

Das Manuskript (Version 1.1) konstruiert auf den 60 Quellstrahlen des Compilers eine endliche Kette mit klassischem und quantenmechanischem Schatten, eine Vor-Messung mit Registern und ein ausdrücklich zusätzlich gesetztes Vierträger-Austauschmodell [formula in source] mit eindeutigem antisymmetrischem Grundzustand [formula in source] , Gap [formula in source] , dem Spektrum [formula in source] , [formula in source] 

## Der Compiler wählt die Zelle

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:27-27](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L27) · `section:4d49ddd0990f5786695b` · section

No opening prose excerpt; see the source.

## Zweiträgersektoren in [formula in source]

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:28-43](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L28) · `section:e6e4893a70280b706b85` · subsection

Mit der [formula in source] -Realisierung der 240 Wurzeln, [formula in source] auf den Koordinaten [formula in source] und [formula in source] auf [formula in source] , liest man die [formula in source] -Gewichte der 248 ab: [formula in source] also [formula in source] . Von den beiden Zweiträgersektoren [formula in source] kommt nur [formula in source] vor. Der Paarterm [formula in source] des Tetramers ist der Proj

Explicit source references:

- [PS.E8BRANCH.01](../../../../verification/status_ledger.csv#L333) · explicit_claim_identifier · original status at linked ledger row

## Die Klammer antisymmetrisiert Trägerindizes

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:44-46](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L44) · `section:8a47a2f0d4bfbf803d88` · subsection

Für alle geordneten Paare [formula in source] mit [formula in source] liegt [formula in source] in [formula in source] ; es gibt 960 solche Paare und kein Ziel in [formula in source] oder [formula in source] . Repräsentationstheoretisch: [formula in source] . Eine über den Spinorsektor vermittelte Träger–Träger-Kopplung erzeugt daher nur antisymmetrische Paare. Die Ableitung eines effektiven [formula in source] aus d

## Die relative Uhr

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:47-47](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L47) · `section:26435e5bead5b769d643` · section

No opening prose excerpt; see the source.

## Kollektiv unsichtbar, relativ sichtbar

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:48-55](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L48) · `section:0a13ef85d898cd076bfb` · subsection

Auf [formula in source] gilt [formula in source] für jede [formula in source] -Matrix [formula in source] ; jede kollektive Operation ändert nur eine globale Phase. Für einen Tick auf genau einem Träger gilt exakt [formula in source] wobei [formula in source] die Paarmarginale nach dem Tick ist. Beweis der Paarformel: [formula in source] . Beide Identitäten sind auf dem expliziten Singulett numerisch bestätigt.

## Der Lift ist chart-unabhängig fixiert

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:56-74](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L56) · `section:eb5830602d5801bd979a` · subsection

Die Uhr des Compilers ist [formula in source] , der Familien-3-Zykel auf [formula in source] mit festem Anker [formula in source] ( v774), mit Lift [formula in source] , [formula in source] , [formula in source] . In [formula in source] fixiert [formula in source] genau drei der 15 Klassen [formula in source] ; nach der Punkt/Geraden-Dualität von [formula in source] ( v783: Klassen [formula in source] Kontexte) sind 

Explicit source references:

- [verification/v774_arf_spinor_compiler.py](../../../../verification/v774_arf_spinor_compiler.py#L1) · explicit_script_identifier
- [verification/v783_two_qubit_clifford.py](../../../../verification/v783_two_qubit_clifford.py#L1) · explicit_script_identifier

## Von der Zelle zur Kette

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:75-75](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L75) · `section:6590c50e3470c9a861d7` · section

No opening prose excerpt; see the source.

## Methode

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:76-78](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L76) · `section:9fcbe6fd9447cc219992` · subsection

[formula in source] liegt in der Algebra der symmetrischen Gruppe [formula in source] auf [formula in source] . Nach Schur–Weyl zerfällt der Raum in [formula in source] ; [formula in source] wirkt als [formula in source] . [formula in source] wird in Youngs Orthogonalform aus den benachbarten Transpositionen aufgebaut (dünnbesetzt, zwei Einträge pro Zeile), die SU(4)-Vielfachheit folgt aus der Hook-Content-Formel. Fü

## Zwei vollständige Zellen mit einer Brücke

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:79-92](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L79) · `section:98212216b94bf8a6c792` · subsection

@rccccc@ [formula in source] & [formula in source] & Vielfachheit & Gap & Manuskript-Schranke [formula in source] & Grund-Irrep\\ 0 & 0 & 1 & 2,000 & 2,000 & [formula in source] \\ 0,5 & 0,2974 & 1 & 1,922 & 1,6875 & [formula in source] \\ 1 & 0,5635 & 1 & 1,818 & 1,375 & [formula in source] \\ 2 & 1,0000 & 1 & 1,586 & 0,750 & [formula in source] \\ 3,2 & 1,3729 & 1 & 1,340 & 0 & [formula in source] \\ 6 & 1,8377 & 1

## Ketten von Zellen: gapped für [formula in source] , kritisch bei [formula in source]

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:93-104](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L93) · `section:d47832ca5a693daf34f7` · subsection

Offene Ketten aus [formula in source] Viererketten-Segmenten (nächste-Nachbar-Bindungen, Zwischenkopplung [formula in source] ), erste Anregung stets in der Adjungierten-Familie [formula in source] : @lccc@ Gap & [formula in source] ( [formula in source] ) & [formula in source] ( [formula in source] ) & [formula in source] ( [formula in source] )\\ [formula in source] & 0,2664 & 0,2552 & 0,2497\\ [formula in source] 

## Der uniforme Ring ist [formula in source]

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:105-113](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L105) · `section:d6f4b2322476e4c7a6db` · subsection

Uniforme periodische Ringe [formula in source] ergeben [formula in source] mit der Sutherland-Geschwindigkeit [formula in source] (für [formula in source] ) und dem konformen Gewicht [formula in source] der [formula in source] in SU(4) [formula in source] . Die Grundenergie pro Träger extrapoliert zu [formula in source] gegen [formula in source] mit Sutherlands [formula in source] ; der [formula in source] -Koeffizie

## Das Zustandsgate am Ringparent

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:114-128](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L114) · `section:f943ac460349d7240fef` · section

Auf dem vollen neutralen Gauß-Sektor des Rotor/CAR-Rings (70 Materiemasken [formula in source] Schleifenfluss, 1190 Zustände) wurde geprüft, ob der Grundzustand den Generator in der lokalen Klasse [formula in source] über den Kovarianzkern [formula in source] bestimmt (modulo [formula in source] und der Sektoridentität [formula in source] ).

## Kopplungsvereinigung mit dem quelleigenen Pati–Salam-Inhalt

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:129-143](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L129) · `section:ba9522cc4af6db9d84e8` · section

QFT4D.RGTEST.01 trägt [X] für den reinen SM-Lauf. Mit dem Inhalt aus PS.ALGEBRA.01 – Eichgruppe [formula in source] , Skalare nur aus [formula in source] , kein 126 – ist die Zweistufe [formula in source] bei 1-Loop ein lineares System und reproduziert v249 ziffergenau. Bei 2-Loop (gauge-only, Machacek–Vaughn; validiert an [formula in source] , [formula in source] , [formula in source] ): @lcccccc@ Inhalt oberhalb [f

Explicit source references:

- [verification/v249_ps_unification.py](../../../../verification/v249_ps_unification.py#L1) · explicit_script_identifier
- [PS.ALGEBRA.01](../../../../verification/status_ledger.csv#L334) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.RGTEST.01](../../../../verification/status_ledger.csv#L332) · explicit_claim_identifier · original status at linked ledger row

## Zwei Präzisierungen

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:144-144](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L144) · `section:c31154d9ce63fcaa1448` · section

No opening prose excerpt; see the source.

## Zwei [formula in source] .

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:145-145](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L145) · `section:bdb9d2ad81791492cab1` · paragraph

Auf den 248 Strömen der Stufe 1 des [formula in source] -Vakuummoduls hat die innere Glue- [formula in source] (Phasen [formula in source] auf [formula in source] ) die Spur [formula in source] , die geometrische Vierteldrehung [formula in source] die Spur [formula in source] ; die Quadrate sind [formula in source] bzw.\ [formula in source] . Die transitive Identifikation Glue = konforme Monodromie ( QGEO.SYM.01) = e

Explicit source references:

- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v522_woit_beta1_gso_gauge.py](../../../../verification/v522_woit_beta1_gso_gauge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v522 round: WOIT.BETA1.GSO.01 -- "the clock is time-like, GSO is the gauge datum": the Z8/NS tower + Ramond control, the invariant- dimension chain, the time-like reflection census, the exact Hermiticity witness of the clock insertion, the GSO 2-torsion census and the family-A tower-normalisation failure. The 40-digit GSO-fixed RP inertia certificates ((29,0,0)/(8,0,0)/(7,9,6)/(17,12,0)) are Python-only by the suite convention. Mirrors v522. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7609)

## Hecke-Index = Jones-Index.

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:146-147](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L146) · `section:5da3c2dfd59709ee909c` · paragraph

Mit [formula in source] (Kawahigashi–Longo–Müger), die das Repo für den Glue-Index 4 benutzt, gilt für jedes injektive [formula in source] : [formula in source] = Hecke-Überlagerungsindex von [formula in source] auf [formula in source] (Zählfunktion [formula in source] , Pol bei [formula in source] ). Pimsner–Popa macht [formula in source] zur bedingten Entropie; das Vakuum ist unter den Dualgruppen-Automorphismen fe

## Grenzen und offene Punkte

[documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex:148-156](../../../../documents/experiments--theory-contracts--universalraum-fable-kernfragen-20260910--fable-runde3--paper--tfpt_anschluss_zellen_seam_2026-09-14/sections/001-section-evidenzkonvention-und-abgrenzung.tex#L148) · `section:eb1aa8a2e4d55b3cc2c4` · section

Der Hüllensatz fixiert Zellstruktur und Vorzeichen, nicht [formula in source] , nicht den Graphen, nicht die Cross-Register-Kopplung der Vor-Messung. Die Superaustausch-Ableitung von [formula in source] aus den [formula in source] -Strukturkonstanten ist formuliert, nicht ausgeführt. Die Uhr ist ein Protokoll auf einem gesetzten Modell; eine Zeit in Sekunden folgt nicht. Die Phasenreferenz für die Periode 12 ist eine
