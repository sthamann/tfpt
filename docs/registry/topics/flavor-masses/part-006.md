# Flavor, masses and neutrinos — part 6

[Topic entry](../flavor-masses.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Front matter / support

[documents/tfpt_1_architecture_e8/sections/004-source.tex:1-243](../../../../documents/tfpt_1_architecture_e8/sections/004-source.tex#L1) · `section:f22c82858ff073c133d4` · frontmatter

equilibrium kernel witnesses carry the full [formula in source] mixing at zero entropy production — no non-equilibrium state is needed, and whether the deployed pure-i wiring is compiler-forced became the registered successor contract ( v908_seam_equilibrium_wiring.py, SEAM.STATE.WIRING.SELECTOR.01); the \ premise stays unmoved. Dated addendum (2026-08-12, rounds 69–71): the successor contract is closed, and the answ

Explicit source references:

- [verification/v845_cfin_normal_form.py](../../../../verification/v845_cfin_normal_form.py#L1) · explicit_file_citation
- [verification/v491_p2_partition_corollary.py](../../../../verification/v491_p2_partition_corollary.py#L1) · explicit_file_citation
- [verification/v776_boundary_hamming_uniqueness.py](../../../../verification/v776_boundary_hamming_uniqueness.py#L1) · explicit_script_identifier
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v109_sheet_pairing.py](../../../../verification/v109_sheet_pairing.py#L1) · explicit_script_identifier
- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_file_citation
- [SEAM.STRADDLE.CONE.01](../../../../verification/status_ledger.csv#L597) · explicit_claim_identifier · original status at linked ledger row
- [verification/v112_selfcounting_channel.py](../../../../verification/v112_selfcounting_channel.py#L1) · explicit_file_citation
- [verification/v499_p2_weights_deligne_bg.py](../../../../verification/v499_p2_weights_deligne_bg.py#L1) · explicit_script_identifier
- [verification/v908_seam_equilibrium_wiring.py](../../../../verification/v908_seam_equilibrium_wiring.py#L1) · explicit_file_citation
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v525_seam_bit_twist_blind.py](../../../../verification/v525_seam_bit_twist_blind.py#L1) · explicit_script_identifier
- [verification/v110_calderon_sheet.py](../../../../verification/v110_calderon_sheet.py#L1) · explicit_file_citation
- [verification/v510_seam_bit_freedom.py](../../../../verification/v510_seam_bit_freedom.py#L1) · explicit_file_citation
- [verification/v799_seam_code_typeii.py](../../../../verification/v799_seam_code_typeii.py#L1) · explicit_script_identifier
- [verification/v506_seam_clock_rigidity.py](../../../../verification/v506_seam_clock_rigidity.py#L1) · explicit_file_citation
- [SEAM.TAU.FLAG.01](../../../../verification/status_ledger.csv#L576) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.STATE.WIRING.SELECTOR.01](../../../../verification/status_ledger.csv#L736) · explicit_claim_identifier · original status at linked ledger row
- [verification/v106_review_validation.py](../../../../verification/v106_review_validation.py#L1) · explicit_file_citation
- [SEAM.BIT.TWISTCLASS.01](../../../../verification/status_ledger.csv#L595) · explicit_claim_identifier · original status at linked ledger row
- [verification/v911_wiring_freedom.py](../../../../verification/v911_wiring_freedom.py#L1) · explicit_file_citation
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_file_citation
- [verification/v108_pascal_ladder.py](../../../../verification/v108_pascal_ladder.py#L1) · explicit_script_identifier
- [verification/v507_seam_bit_origin.py](../../../../verification/v507_seam_bit_origin.py#L1) · explicit_file_citation
- [verification/v111_quadratic_transport.py](../../../../verification/v111_quadratic_transport.py#L1) · explicit_file_citation
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_file_citation
- [verification/v521_seam_bit_rp_blind.py](../../../../verification/v521_seam_bit_rp_blind.py#L1) · explicit_script_identifier
- [verification/v512_seam_tau_flag.py](../../../../verification/v512_seam_tau_flag.py#L1) · explicit_file_citation
- [verification/v528_seam_bit_twist_class_definition.py](../../../../verification/v528_seam_bit_twist_class_definition.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ==== v510 round: SEAM.BIT.FREEDOM.01 -- the freedom attack on the v506/v507 alignment bit: the POSITION half of the bit is topology. Exact content mirrored: (i) the DIHEDRAL CENSUS -- on the refined 2N-point seam circle D_16 has 17 involutions with EXACTLY ONE free (the antipodal shift by 8) and all 16 reflections have exactly 2 circle fixed points (8 site-axis + 8 edge-axis; robustness N = 8, 12; odd control N = 9: zero free), plus the quotient topology chi(C/antipode) = 0 (circle) vs chi(C/reflection) = 1 (interval, 2 boundary corners); (ii) the AUT COMPLETENESS -- Aut(C_8) = D_8 by brute force over all 8! = 40320 permutations and Aut(C_16) = D_16 by degree-2 propagation (all 32 candidates), so the census covers ALL circle symmetries; (iii) the Cl(16) DICHOTOMY CENSUS -- on explicit 256x256 Jordan-Wigner gammas the free deck's NS implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the implementers of ALL 16 reflections exist (one of the two spin lifts +-R) and square to SCALARS {2^7 (site-axis), 2^8 (edge-axis)} (split): NONSPLIT <=> FREE over the complete census; root dichotomy 2 (the +-quarter shifts) vs 0 total over all 16 reflections; (iv) the REAL-STRUCTURE TABLE -- the deck-commuting antiholomorphic involutions solve symbolically to exactly two families (M diagonal: mu conj z, fix line through the poles; M antidiagonal: mu/conj z, fix circle |z| = sqrt mu), and the unique mark-fixing real structure per configuration is equatorial/FREE for mu4 and generic-unit, real-axis/NOT-free for silver and generic-real, and NONEXISTENT for the hexagonal frame; (v) HARMONIC + FREE => mu4 -- the deck-pair cross-ratio (1-b)^2/(1+b)^2 = -1 solves exactly to b = +-i, with the lambda table (2, 1/2, 3/4, 5/4) real and the hexagonal lambda complex; (vi) the HONEST COUNTERWITNESSES -- the discrete witness {0,1,8,9} (shift-invariant, crossing, but not quarter-shift-invariant) and the continuous witness {+-1, +-(3+4i)/5} (pair cross-ratio -1/4, j = 148176/25 != 1728, clock does not preserve): the Fock dichotomy measures the CLASS, not the modulus. The Moebius/Klein covering models and the pillowcase branch control stay Python-side (v510). Mirrors v510. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5155)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ==== v506 round: SEAM.CLOCK.RIGIDITY.01 -- clock rigidity, Route B of the v503 classification (Part A Moebius + Part B Fock). Exact content mirrored: (i) the COMPLETE SQUARE-ROOT SOLVE -- g^2 = deck in PGL2(C) has exactly two solutions z -> +-iz (tr != 0 forces diagonal with (a/d)^2 = -1; tr = 0 forces det = 0), both automatically of projective order 4; (ii) the D4 CENTER + ORDER-4 COUNT + the COUNTEREXAMPLE -- the mu4 stabiliser D4 = {i^k z, i^k/z} has exactly 2 order-4 elements (the clocks), both squaring to the deck, center = {id, deck}; the silver harmonic set {+-1, +-(3+2 sqrt 2)} has j = 1728 and full D4 but its 4-cycle squares to the CROSSING involution v/z, not the deck (deck non-central: 0 roots -- harmonicity alone insufficient); (iii) the Cl(16) IDENTITY -- on explicit 256x256 Jordan-Wigner gamma matrices, Utilde = prod_j (1 - g_j g_{j+8}) satisfies Utilde^2 = 256 g_1...g_16 EXACTLY (U^2 = (-1)^F, the forced nonsplit Z4), the R implementer squares to +256 (split control), and the volume element anticommutes with every gamma; (iv) the N-ARITHMETIC -- S4 element orders {1,2,3,4} (faithfulness kills n >= 5: max cyclic image order < n for n = 5..8), free orbits force n | 4, the cusp side kills n = 6 (deg(lam^5-1) = 5 != 3 = deg(lam^3-1)), transfer spectrum {1, 64/729, 1/729} with gap (2/3)^6, and the generic 4-set stabiliser V4 = {+-z, +-2/z} has exponent 2 (not even the deck has a root). The full 24-triple stabiliser enumeration and the A4/hexagonal profile stay Python-side (v506 Part A). Mirrors v506. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4394)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)
- [(* ==== v525 round: SEAM.BIT.TWISTBLIND.01 -- "the twist-state kill": the NINTH side-blind test on the v512 scoreboard (8 -> 9); the free-plus-twist class is exhausted. Three exact mirrors: (i) the integer incidence frame + the sigma o r = +-sigma congruence mechanism (swap axes: sigma o r = sigma => the twisted Gram is the diagonal unitary congruence D M D = spectrally invisible; fixing axes at pi/2: sigma o r = -sigma = the eta flip); (ii) the pi/2-existence solveset of the mark-fixing axes + the exact counterwitness census ((3+4i)/5 unimodular but NEVER a root of unity up to order 64 -- no lattice mark-compatible reflection at any dyadic refinement); (iii) the delta <-> pi - delta mirror equivariance (the lattice reflection maps the m-mark set EXACTLY to the (8-m)-mark set -- the exact mechanism behind the Casimir mirror symmetry ln|omega(D)|(m) = ln|omega(D)|(8-m) and behind pi/2 as the symmetric point of every invariant readout). The Pfaffian insertion spectra, the Bogoliubov 2-of-16 pattern census, the defect energy and the 40-digit inertia certificates are numerical (mpmath), Python-only, flagged here. Mirrors v525. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8058)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ==== v491 round: P2.PARTITION.01 -- g_car = 5 as the partition corollary of the four marks (the sharpening of v53). Exact content: 4 into exactly 3 positive integer parts is uniquely {1,1,2} => e = (4,5,2) => g_car = e2 = 5, |Z2| = e3 = 2, N_fam = e2 - e3 = 3 as corollaries; every assumption load-bearing (positivity / sum / part count / integrality negative controls); v53 needs all three targets, the partition only e1 = 4; sum rule 4(N-1)/2 = 4 iff N = 3; mirrors v491. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3116)
- [(* ==== v528 round: SEAM.BIT.TWISTCLASS.01 -- bit = twist-class choice. Exact mirrors: (i) cardinality lemma; (ii) 224-axis flip census; (iii) O-values. Pfaffian spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8213)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v521 round: SEAM.BIT.RPBLIND.01 -- "free OS positivity does not see delta": the anti-linear census solvesets on M(delta), the counterwitness census, the V4 -> D4 closure (face #13), the cut/mark incidence, the continuum axis elimination + Cauchy-Stieltjes factorisation, the clock-tower clause and the hex/silver precondition controls. The 40-digit lattice Gram inertia spectra (N = 16 / N = 32) are Python-only by the suite convention. Mirrors v521. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7479)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v107) quantum-clock target ---- *) checkExact["v107 per-l clock: l=0 (la-1)(la+2), l=1 la(la+1); l>=2 complex Re=-1/2", (Factor[la^2 + la + (0 - 2)] == (la - 1) (la + 2)) && (Factor[la^2 + la + (2 - 2)] == la (la + 1)) && (Re[la /. Solve[la^2 + la + 4 == 0, la]] == {-1/2, -1/2})]; checkExact["v107 cusp-ladder cross-link: decay set {0,-1,-2} = -Spec(Q diag(0,1,1)) = -N_fam x cusp", Module[{Vw = Q.DiagonalMatrix[{0, 1, 1}]}, Sort[Eigenvalues[Vw]] == {0, 1, 2}]]; checkExact["v107 exact target: (1/3)^6 = ((2/3)^6)^{log_{3/2}3}; ratio = 1 + log_{3/2}2", (FullSimplify[-6 Log[3] - (Log[3]/Log[3/2]) (6 Log[2] - 6 Log[3])] === 0) && (FullSimplify[Log[3]/Log[3/2] - (1 + Log[2]/Log[3/2])] === 0)]; check["v107 bend log_{9/4}(3) = 1.354756; seam coupling 1/(3Pi) = 0.106103", Log[3]/Log[9/4], 1.3547556457`10, 10^-9]; (* ---- (v108) Pascal ladder ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L471)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [(* ---- (v111) quadratic transport ---- *) Module[{jwOps, evensOf, buildQuads, runWorld}, jwOps[g_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, g - i]], {i, g}]]; evensOf[g_] := Select[Range[2^g], EvenQ[DigitCount[# - 1, 2, 1]] &]; buildQuads[g_] := Module[{a = jwOps[g], ad}, ad = Transpose /@ a; Join[ Flatten[Table[{ad[[i]] . ad[[j]], a[[i]] . a[[j]]}, {i, g}, {j, i + 1, g}], 2], Flatten[Table[ad[[i]] . a[[j]], {i, g}, {j, g}], 1]]]; runWorld[g_] := Module[{a = jwOps[g], ad, ev = evensOf[g], od, quads, vac, d1, d2, orbit, qr, words}, ad = Transpose /@ a; od = Complement[Range[2^g], ev]; quads = buildQuads[g]; vac = UnitVector[2^g, 1]; d1 = (# . vac) & /@ quads; d2 = Flatten[Outer[Dot, quads, d1, 1], 1]; orbit = (#[[ev]]) & /@ Join[{vac}, d1, d2]; qr = (#[[ev, ev]]) & /@ quads; words = Join[{IdentityMatrix[Length[ev]]}, qr, Flatten[Outer[Dot, qr, qr, 1], 1]]; {Length[quads], And @@ ((Max[Abs[#[[ev, ev]]]] == 0 && Max[Abs[#[[od, od]]]] == 0) & /@ Join[a, ad]), And @@ ((Max[Abs[#[[ev, od]]]] == 0 && Max[Abs[#[[od, ev]]]] == 0) & /@ quads), MatrixRank[orbit], MatrixRank[Flatten /@ words], Length[ev]}]; Module[{r5 = runWorld[5], r3 = runWorld[3]}, checkExact["v111 model: 45 quadratics = dim so(10); 10 linears sheet-ODD, 45 quadratics sheet-EVEN (exact block-zero)", r5[[1]] == 45 && r5[[2]] && r5[[3]]]; checkExact["v111 GENERATION: quadratic words of length <= 2 span all 16 code states from the vacuum", r5[[4]] == 16]; checkExact["v111 COMPLETENESS: products of length <= 2 of the 45 quadratics span End(S+) = 256 (transport degree exactly 2)", r5[[5]] == 256]; checkExact["v111 ladder genericity: g=3 world identical (15 quadratics -> End(S+) = 16) - degree selected, not rank", r3[[1]] == 15 && r3[[5]] == 16]; checkExact["v111 channel reading: certified tower 256 = 1 + 45 + 210 = norm + transport generators + pair sector", 1 + 45 + 210 == 256]; ]; ]; (* ---- (v112) self-counting channel ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L542)
- [experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean#L1)
- [(* ==== v499 round: P2.TYPING.01 -- the P2 weight-typing postulate hardened: the anchor a = (1,1,2) as the Birkhoff-Grothendieck splitting exponents of the Deligne canonical extension E of the flavor connection (types the v491 check-9 residual). Exact content mirrored: (i) partition enumeration under the full typing (BG dictionary h^0 = 0 <=> a_i >= 1, exhaustive window) + the naive- typing negative control (h^1(E') = 3 forces deg -6, three splittings, e2 never 5) + the h^1 discrepancy (h^1(anchor bundle) = 1 != 3); (ii) the Deligne residue-trace degree (cusp exponents {0,1/3,2/3} = the unique lift of spec(lam^3 - 1) to [0,1), trace 1 per mark, deg E = -4, par-deg 0, witness A0* charpoly); (iii) the Schur-Horn permutohedron integer points {(2,2,0),(2,1,1)} with h^0 = 0 killing {2,2,0}; (iv) the Biswas Z3-cover degree arithmetic (genus 2, eigensheaves O(-2)^2, chi cross-check, regular-rep weights, the decomposable model {0,2,2} with h^0 = 1 = the unstable companion; deck double genus 1, j = 1728); (v) the n-mark formula e2 = (n-2)(n+1)/2 = 5 only at n = 4. The sympy symbolic parts (H^1 residue basis, monodromy group closure |<U,M0>| = 24, the 324-case stability skeleton) stay Python-side (v499). Mirrors v499. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3620)
- [(* ==== v512 round: SEAM.TAU.FLAG.01 -- "the flag-transitivity equivalence web": the tau = i attack on the free RP seam circle. Test family M(delta) = {+-1, +-e^(i delta)}; bare mark-transitivity is delta-blind (pair-exchanging V4), FLAG transitivity <=> delta = pi/2 <=> tau = i. Six exact mirrors: (i) the V4/D4 census over five exact members incl. flag/arc orbit counts, (ii) the solveset equivalences + family identities, (iii) the odd-split closed form + arc Laplacian + K3 indicator, (iv) the twist mode identity + AB delta-blindness + j-rationality control, (v) the H4 centraliser rigidity (Schur), and (vi) the negative controls (hexagonal/silver/Z16 census/n = 3). Mirrors v512. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5675)
- [(* ---- (v109) sheet pairing ---- *) Module[{splus, sminus, vecw, lamW, addW, crossT, formsEven, diagT, formsOdd, zmult}, splus = Select[Tuples[{1/2, -1/2}, 5], EvenQ[Count[#, -1/2]] &]; sminus = Select[Tuples[{1/2, -1/2}, 5], OddQ[Count[#, -1/2]] &]; vecw = Flatten[Table[s UnitVector[5, i], {i, 5}, {s, {1, -1}}], 1]; lamW[k_] := If[k == 0, {ConstantArray[0, 5]}, Total /@ Subsets[vecw, {k}]]; checkExact["v109 no scalar within a sheet: zero-weight mult of S+xS+ and S-xS- is 0", (Count[Flatten[Outer[Plus, splus, splus, 1], 1], ConstantArray[0, 5]] == 0) && (Count[Flatten[Outer[Plus, sminus, sminus, 1], 1], ConstantArray[0, 5]] == 0)]; crossT = Sort[Flatten[Outer[Plus, splus, sminus, 1], 1]]; checkExact["v109 cross-sheet zero-weight mult = 16 = 1+5+10 (Pascal triple)", Count[crossT, ConstantArray[0, 5]] == 16]; formsEven = Sort[Join[lamW[0], lamW[2], lamW[4]]]; checkExact["v109 EXACT multiset: S+xS- = Lambda^0+Lambda^2+Lambda^4 (256 = 1+45+210)", crossT === formsEven && Length[crossT] == 256]; diagT = Sort[Join[Flatten[Outer[Plus, splus, splus, 1], 1], Flatten[Outer[Plus, sminus, sminus, 1], 1]]]; formsOdd = Sort[Join[lamW[1], lamW[1], lamW[3], lamW[3], lamW[5]]]; checkExact["v109 sheet-diagonal = odd forms: (S+xS+)u(S-xS-) = 2L1+2L3+L5 (512)", diagT === formsOdd && Length[diagT] == 512]; zmult[k_] := Count[lamW[k], ConstantArray[0, 5]]; checkExact["v109 zero-mode grading (L0,L2,L4) -> (1,5,10) = the carrier code; tower tops at 2K = 4", ({zmult[0], zmult[2], zmult[4]} == {1, 5, 10}) && (4 == 2*2)]; ]; (* ---- (v110) Calderon-sheet selection ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L499)
- [(* ==== v507 round: SEAM.BIT.ORIGIN.01 -- the tautology attack on the v506 alignment bit, executed and refuted (Part A torus origin + Part B fermion dichotomy). Exact content mirrored: (i) the HALF-PERIOD DESCENT -- the fixed points of w -> -w on C/(Z + tau Z) are the 4 half-periods (2w in Lambda <=> coefficients in {0, 1/2}; the 1/3-control fails), a translation t_c descends iff 2c in Lambda (exactly the 3 nonzero half-periods), and the descended map sigma_i(x) = e_i + (e_i-e_j)(e_i-e_k)/(x-e_i) satisfies the exact curve-lift identity prod(sigma_i - e_l) = psi_i^2 prod(x - e_l) with RATIONAL psi_i, closing to Klein V4 symbolically; (ii) the CORE SOLVE -- the pair cross-ratio condition CR = -1 solves to lambda = -1 (sigma_1), 2 (sigma_2), 1/2 (sigma_3) exactly, union = the harmonic orbit with j = 1728, against j(3) = 21952/9 and j(hex) = 0; (iii) the STABILISER COUNTS -- the complete 24-triple enumeration gives (|Stab|, #involutions, #free) = (4,3,3) generic / (8,5,3) harmonic / (12,3,3) hexagonal, and in ALL three types the free involutions are EXACTLY the three sigma_c (the deck CLASS is forced); (iv) the CM FIXED POINT -- mult-by-i mod 2 fixes exactly the half-period (1,1) = c* = (1+tau)/2 while mult-by-rho 3-cycles all three, the lemniscatic clock ghat: x -> (x-1)/(x+1) needs the curve-lift factor psi = 2i/(x+1)^2 (the CM unit; t^2+1 irreducible over Q) and squares to the central -1/x; (v) the Cl(16) DICHOTOMY -- on explicit 256x256 Jordan-Wigner gammas the central implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the EDGE implementer Utilde_e = P_3 (g1+g5)(g2+g4)(g6-g16)(g7-g15)(g8-g14) (g9-g13)(g10-g12) implements the NS edge reflection and squares to the SCALAR +2^7 (split), and in the 32-element NS dihedral lift group the central deck has EXACTLY 2 square roots (the +-quarter shifts) vs 0 for the edge deck; (vi) the SILVER BIJECTION CENSUS -- all 8 mark bijections {+-1, +-(3+2 sqrt 2)} -> {0, 1, -1, inf} carry the deck z -> -z to the EDGE sigma_2/sigma_3 (never the central sigma_1), while all 8 mu4 bijections carry it to the CENTRAL sigma_1. The v493 circularity-audit direction and the 28/21 arrangement census stay Python-side (v507). Mirrors v507. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4545)
- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)

## One master moment generates [formula in source] , [formula in source] , [formula in source] , [formula in source]

[documents/tfpt_1_architecture_e8/sections/004-source.tex:351-366](../../../../documents/tfpt_1_architecture_e8/sections/004-source.tex#L351) · `section:e2ac56d63dc5b474ddb4` · subsection

With [formula in source] , the quadratic hypercharge trace on one family is [formula in source] , and it generates the whole integer chain: The flavor budget, the [formula in source] budget, the [formula in source] count and the second seam defect all hang on the second hypercharge moment [formula in source] . \ Round-22 sharpening: the moment itself is one symbolic identity, [formula in source] — the Coxeter number 

Explicit source references:

- [verification/v810_cutcode_moment.py](../../../../verification/v810_cutcode_moment.py#L1) · explicit_file_citation

## Compact [formula in source] compression and the role of [formula in source]

[documents/tfpt_1_architecture_e8/sections/005-source.tex:1-12](../../../../documents/tfpt_1_architecture_e8/sections/005-source.tex#L1) · `section:87aef64679791ec15f2e` · subsection

with [formula in source] and [formula in source] . . The right-handed neutrino [formula in source] is the Pascal singleton [formula in source] that closes [formula in source] ; removing it breaks the truncation and shifts [formula in source] by [formula in source] .

## Dual-root dictionary (everything from two charges)

[documents/tfpt_1_architecture_e8/sections/006-source.tex:62-106](../../../../documents/tfpt_1_architecture_e8/sections/006-source.tex#L62) · `section:5db71905be923888908e` · subsection

Two carrier roots generate the family and the transport cusps . With [formula in source] and [formula in source] (the determinant-normalised carrier eigenvalues), the full one-family hypercharge spectrum and the flavor-transport cusps are sums of the two roots: [formula in source] [formula in source] [formula in source] All residuals are exactly zero. The Standard-Model charge table is not assumed; it is built by add

## The EM closure: [formula in source] as an explicit fixed point (made explicit here)

[documents/tfpt_1_architecture_e8/sections/007-source.tex:1-256](../../../../documents/tfpt_1_architecture_e8/sections/007-source.tex#L1) · `section:6a757c5701557192653a` · subsection

The engine [formula in source] is not an input — it is the unique root of an explicit closure equation (the exact electromagnetic closure theorem). With [formula in source] , [formula in source] , [formula in source] and the seam response [formula in source] , where the coefficient is [formula in source] , so the fine-structure constant reads the flavor transport budget [formula in source] and the [formula in source]

Explicit source references:

- [EM.WARD.01](../../../../verification/status_ledger.csv#L70) · explicit_claim_identifier · original status at linked ledger row
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_file_citation
- [verification/v434_alpha_quillen_betafunction.py](../../../../verification/v434_alpha_quillen_betafunction.py#L1) · explicit_file_citation
- [verification/v470_alpha_inflow_level.py](../../../../verification/v470_alpha_inflow_level.py#L1) · explicit_script_identifier
- [verification/v391_alpha_quillen_progress.py](../../../../verification/v391_alpha_quillen_progress.py#L1) · explicit_file_citation
- [ALPHA.QUILLEN.FACES.01](../../../../verification/status_ledger.csv#L754) · explicit_claim_identifier · original status at linked ledger row
- [verification/v985_quillen_channel_swap.py](../../../../verification/v985_quillen_channel_swap.py#L1) · explicit_file_citation
- [verification/v48_em_ward.py](../../../../verification/v48_em_ward.py#L1) · explicit_file_citation
- [verification/v485_contact_diagonal_closed.py](../../../../verification/v485_contact_diagonal_closed.py#L1) · explicit_file_citation
- [verification/v60_lambda_metrology_branch.py](../../../../verification/v60_lambda_metrology_branch.py#L1) · explicit_script_identifier
- [verification/v151_bfk_split.py](../../../../verification/v151_bfk_split.py#L1) · explicit_script_identifier
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [verification/v484_seam_contact_unit.py](../../../../verification/v484_seam_contact_unit.py#L1) · explicit_script_identifier
- [verification/v456_seam_chirality_from_c3.py](../../../../verification/v456_seam_chirality_from_c3.py#L1) · explicit_script_identifier
- [verification/v382_alpha_quillen_exact.py](../../../../verification/v382_alpha_quillen_exact.py#L1) · explicit_script_identifier
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_script_identifier
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [verification/v342_em_ward_heatkernel.py](../../../../verification/v342_em_ward_heatkernel.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v461_seam_strict_locality.py](../../../../verification/v461_seam_strict_locality.py#L1) · explicit_script_identifier
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_file_citation
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v435_alpha_quillen_chernlevel.py](../../../../verification/v435_alpha_quillen_chernlevel.py#L1) · explicit_file_citation
- [verification/v472_quillen_detline_moduli.py](../../../../verification/v472_quillen_detline_moduli.py#L1) · explicit_file_citation
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v239_kms_thermal_time.py](../../../../verification/v239_kms_thermal_time.py#L1) · explicit_script_identifier
- [verification/v433_alpha_quillen_heatkernel.py](../../../../verification/v433_alpha_quillen_heatkernel.py#L1) · explicit_file_citation
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v384_residual_certification.py](../../../../verification/v384_residual_certification.py#L1) · explicit_script_identifier
- [verification/v341_alpha_quillen.py](../../../../verification/v341_alpha_quillen.py#L1) · explicit_file_citation
- [verification/v483_pillowcase_exact_traces.py](../../../../verification/v483_pillowcase_exact_traces.py#L1) · explicit_script_identifier
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [HYP.PHI0.PUNCTURE.01](../../../../verification/status_ledger.csv#L464) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v454/v456/v457/v459 round (G-block): the edge current-algebra/Sugawara c=8, the S3-from-P1 one-sided arithmetic, the (E8)_1 character/sector kill-test, and the lattice-VOA second route; mirrors v454/v456/v457/v459. The Casimir + Kac-Moody fits (v454), the Chern flip (v456) and the Tomita-Takesaki tower (v455) are numerical, Python-only; the exact algebra is mirrored here. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2827)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v983) SEAM.SIMPLECURRENT.GENERATOR.01: glue vector lambda = (omega_s, omega_f) ---- *) Module[{omegaS, omegaF, lam, inD5, inA3, inL0, gensD5, gensA3, dots, cosetRoots, census, lamV, omega2, nV, n2, cartanD8}, omegaS = ConstantArray[1/2, 5]; omegaF = {3/4, -1/4, -1/4, -1/4}; lam = Join[omegaS, omegaF]; inD5[x_] := (And @@ (IntegerQ /@ x)) && EvenQ[Total[x]]; inA3[y_] := (And @@ (IntegerQ /@ y)) && Total[y] === 0; inL0[z_] := inD5[Take[z, 5]] && inA3[Take[z, {6, 9}]]; checkExact["v983 NORMS+WEIGHT [E]: |omega_s|^2=5/4, |omega_f|^2=3/4, |lambda|^2=2, h_lambda=1", Total[omegaS^2] === 5/4 && Total[omegaF^2] === 3/4 && Total[lam^2] === 2 && Total[lam^2]/2 === 1]; checkExact["v983 ORDER FOUR [E]: 4*lambda in D5(+)A3, lambda and 2*lambda not -- [lambda] generates the diagonal Z4", inL0[4 lam] && ! inL0[2 lam] && ! inL0[lam]]; gensD5 = {{1, 1, 0, 0, 0}, {1, -1, 0, 0, 0}, {0, 1, 1, 0, 0}, {0, 0, 1, 1, 0}, {0, 0, 0, 1, 1}}; gensA3 = {{1, -1, 0, 0}, {0, 1, -1, 0}, {0, 0, 1, -1}}; dots = Join[omegaS . # & /@ gensD5, omegaF . # & /@ gensA3]; checkExact["v983 ISOTROPY+UNIMODULAR [E]: lambda.L0 subset Z on a generator set; det(D5)*det(A3)=16, index-4 glue => det L=1", (And @@ (IntegerQ /@ dots)) && 16/4^2 === 1]; cosetRoots[k_] := Module[{t = k lam, d5, a3}, d5 = Counts @ Select[ Total[(# + Take[t, 5])^2] & /@ Select[Tuples[Range[-5, 3], 5], EvenQ[Total[#]] &], # <= 2 &]; a3 = Counts @ Select[ Total[(Join[#, {-Total[#]}] + Take[t, {6, 9}])^2] & /@ Tuples[Range[-6, 6], 3], # <= 2 &]; Total[KeyValueMap[#2 Lookup[a3, 2 - #1, 0] &, d5]]]; census = Table[cosetRoots[k], {k, 0, 3}]; checkExact["v983 COSET ROOT CENSUS [E]: norm-2 vectors per fusion power k=0..3 = {52,64,60,64}, total 240; odd powers 64+64=128", census === {52, 64, 60, 64} && Total[census] === 240 && census[[2]] + census[[4]] === 128]; lamV = Join[{1, 0, 0, 0, 0}, omegaF]; omega2 = {1/2, 1/2, -1/2, -1/2}; nV = Total[lamV^2]; n2 = Total[omegaS^2] + Total[omega2^2]; cartanD8 = {{2, -1, 0, 0, 0, 0, 0, 0}, {-1, 2, -1, 0, 0, 0, 0, 0}, {0, -1, 2, -1, 0, 0, 0, 0}, {0, 0, -1, 2, -1, 0, 0, 0}, {0, 0, 0, -1, 2, -1, 0, 0}, {0, 0, 0, 0, -1, 2, -1, -1}, {0, 0, 0, 0, 0, -1, 2, 0}, {0, 0, 0, 0, 0, -1, 0, 2}}; checkExact["v983 KILLS+HOLOMORPHY SHADOW [E]: vector glue (v,omega_f) norm 7/4 and mismatched (omega_s, omega_2) norm 9/4 not in 2Z; det Cartan D8=4 vs glued det=1", nV === 7/4 && n2 === 9/4 && Det[cartanD8] === 4 && 16/4^2 === 1]; ]; (* ---- (v985) ALPHA.QUILLEN.EXACT.01: mu4 circulant spectra + graded channel swap ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L444)
- [(* ---- (v60) Lambda branch selection: prefactor 3/(4pi^2), branch mis-scale 64pi^3/3 ---- *) checkExact["delta_top=48 c3^4=3/(256 pi^4); (8pi)^2 delta_top=3/(4 pi^2); 2c3/delta_top=64 pi^3/3 (G_N pinned)", With[{c3 = 1/(8 Pi), dt = 48 (1/(8 Pi))^4}, Simplify[dt - 3/(256 Pi^4)] == 0 && Simplify[(8 Pi)^2 dt - 3/(4 Pi^2)] == 0 && Simplify[2 c3/dt - 64 Pi^3/3] == 0]]; checkExact["action exponents (1,5,10) = K5 counts (5 vertices, C(5,2)=10 edges); Pascal 16=1+5+10", {1, 5, Binomial[5, 2]} == {1, 5, 10} && 1 + 5 + 10 == 16]; (* ---- (v61) boundary-CFT bridge: WZW central charges = atoms, conformal embedding ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L282)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [(* ---- (v47) Boundary Carrier Selection Theorem (Theorem A) ---- *) checkExact["q(D5)+q(A3)=5/4+3/4=2 (E8 root norm); glue index sqrt(4*4/1)=4=|mu4|", 5/4 + 3/4 == 2 && Sqrt[4*4/1] == 4]; checkExact["only n=5 gives 16-dim D_n half-spinor (2^{n-1}=16) => D5", Select[Range[2, 8], 2^(# - 1) == 16 &] == {5}]; (* ---- (v48) EM boundary Ward decomposition (Theorem C) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L184)
- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v461/v462 round: the Kapustin-Fidkowski strict-locality obstruction (integer logic; the Wilson-loop winding/Chern themselves are numerical, Python-only) and the 128-spinor extension at character level -- the Jacobi/E8 theta identity theta2^8+theta3^8+theta4^8=2E4 (so the (E8)_1 character is the SO(16)_1 vacuum+spinor sum) and the 120+128=248 sector + finite 16-Majorana Fock counts; mirrors v461/v462. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2874)
- [(* v454: level-1 Sugawara c = dim G/(1+h^v) = 8 for both SO(16)_1 and (E8)_1 *) cSO16 = 120/(1 + 14); cE8 = 248/(1 + 30); checkExact["v454 SEAM.EQUIV.EDGE.VIRASORO.01: level-1 Sugawara c=dim G/(1+h^v)=8 for BOTH SO(16)_1 (120/15) and (E8)_1 (248/31); 16 Majoranas => c_-=8=g_car+N_fam (the Casimir c and Kac-Moody central term <J_n J_-n>=n are numerical, Python-only)", cSO16 == 8 && cE8 == 8 && cSO16 == cE8 && 8 == gcar + Nfam]; (* v456: c3's '8' is the one-sided count; reflection C->-C so two-sided forces C=0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2835)
- [(* ==== v342 EM.WARD.02: the heat-kernel origin of the F_U(1) terms ==== *) Module[{c3v, ointK, c3gb, gilkey, q2}, c3v = 1/(8 Pi); (* c3 = boundary Gauss-Bonnet coefficient: oint_{S^2} K = 2 pi chi = 4 pi (chi=2), c3 = 1/(|Z2| oint K) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2259)
- [(* v461: tied obstruction integers + the reflection forcing (strict-local => C=-C => C=0) *) cMinus = 2^(gcar - 1)*1/2; (* 16*|C|/2 = 8, |C|=1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2881)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* ==== v341 ALPHA.QUILLEN.01: the seam-form discriminant identities ==== *) Module[{c3v, phib}, c3v = 1/(8 Pi); phib = 1/(6 Pi); (* phi_base = (4/3) c3 carries q(A3): c3/phi_base = 3/4; with -5/4 = -q(D5) the F_U(1) seam response carries BOTH glue forms, q(D5)+q(A3)=2 = E8 root norm; counterterm coefficient (4/5)M = 8 b1 = 8*(41/10) with b1 the U(1)_Y one-loop beta (rank E8 = 8) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2248)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v150) replica EH model ---- *) Module[{cdef, imgOK, convOK, mellin, dz0, dC, target}, cdef[g_] := (1/12) (2 Pi/g - g/(2 Pi)); imgOK = And @@ Table[ FullSimplify[Sum[1/Sin[Pi k/n]^2, {k, 1, n - 1}] - (n^2 - 1)/3] === 0, {n, 2, 8}]; convOK = Simplify[(1/(4 nn)) (nn^2 - 1)/3 - cdef[2 Pi/nn]] === 0; mellin = Integrate[tt^(ss - 1) Exp[-mm^2 tt], {tt, 0, Infinity}, Assumptions -> ss > 0 && mm > 0]; dz0 = D[mm^(-2 ss), ss] /. ss -> 0; dC = D[cdef[gg], gg] /. gg -> 2 Pi; target = Simplify[12 Pi (1/2) (1/(8 Pi))]; checkExact["v150 replica EH model: image sum exact (N=2..8); orbifold deficit = C(2pi/N); Mellin Delta-zeta(s) = C m^-2s => Delta log det' = 2C ln m (cutoff-independent); dC/dgamma|_{2pi} = -1/(12pi) => EH form with k = ln m/(12pi); target k = c3/2 <=> ln m = 3/4 = q(A3)", imgOK && convOK && Simplify[mellin - Gamma[ss] mm^(-2 ss)] === 0 && Simplify[dz0 + 2 Log[mm]] === 0 && Simplify[dC + 1/(12 Pi)] === 0 && target == 3/4]; ]; (* ---- (v151) BFK split ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1321)

## A two-dimensional action lattice

[documents/tfpt_1_architecture_e8/sections/008-source.tex:1-28](../../../../documents/tfpt_1_architecture_e8/sections/008-source.tex#L1) · `section:4bd3b166d51412804107` · subsection

All scales sit on the integer lattice spanned by two generators — the gauge unit [formula in source] and the flavor unit [formula in source] — as [formula in source] : @llll@ scale & [formula in source] & [formula in source] & axis \\ [formula in source] & [formula in source] & [formula in source] & gauge \\ [formula in source] & [formula in source] & [formula in source] & gauge \\ [formula in source] & [formula in s

## Level 2.8 — positive-root moment: [formula in source]

[documents/tfpt_1_architecture_e8/sections/008-source.tex:262-277](../../../../documents/tfpt_1_architecture_e8/sections/008-source.tex#L262) · `section:376087e15c98226fb1b8` · subsection

The number of positive [formula in source] roots equals the master hypercharge moment: so the second hypercharge moment of one family is the positive-root half-system. The whole integer chain then reads off [formula in source] : The [formula in source] slice is then [formula in source] : one [formula in source] phase slice of the [formula in source] root atlas is exactly the full flavor transport budget. \ (arithmeti

## [formula in source] monodromy, flavor and CP readouts

[documents/tfpt_1_architecture_e8/sections/008-source.tex:331-348](../../../../documents/tfpt_1_architecture_e8/sections/008-source.tex#L331) · `section:3c6bc074137cada172b9` · section

Machine checks for this section: v88_ cp_ phase_ audit.py

Explicit source references:

- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_file_citation

## CP as triple seed variance; a closed observable quadrilateral

[documents/tfpt_1_architecture_e8/sections/008-source.tex:349-384](../../../../documents/tfpt_1_architecture_e8/sections/008-source.tex#L349) · `section:2c03897e6b898161b07b` · subsection

The Cabibbo angle is the Bernoulli width of the seed. The exact CKM phase is the family transport holonomy (document 3), [formula in source] ; on the small-area branch this has the compact readout form (with an [formula in source] remainder) The coefficient [formula in source] is the family number [formula in source] : weak CP is the [formula in source] base angle [formula in source] plus [formula in source] times th

## Mass hierarchy as a hexagon with one extra turn

[documents/tfpt_1_architecture_e8/sections/009-source.tex:1-26](../../../../documents/tfpt_1_architecture_e8/sections/009-source.tex#L1) · `section:e8c037c79f7fa4995590` · section

Machine checks for this section: v18_ quark_ yukawa.py v20_ lepton_ c_ derivation.py

Explicit source references:

- [verification/v18_quark_yukawa.py](../../../../verification/v18_quark_yukawa.py#L1) · explicit_file_citation
- [verification/v20_lepton_c_derivation.py](../../../../verification/v20_lepton_c_derivation.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)

## Lepton flavor decuple: the charged-lepton determinant carries [formula in source]

[documents/tfpt_1_architecture_e8/sections/009-source.tex:27-49](../../../../documents/tfpt_1_architecture_e8/sections/009-source.tex#L27) · `section:b82b2bc3ca9a55c897cf` · subsection

The source masses on the [formula in source] branch are [formula in source] . Their product is a pure decuple in the seed: with [formula in source] . So the charged-lepton Yukawa powers [formula in source] are the three carrier numbers [formula in source] , and the lepton determinant carries the same decuple ( [formula in source] ) that the cosmological constant carries in the gauge sector ( [formula in source] ): [f

## Why the top Yukawa is [formula in source] : the [formula in source] anchor (Froggatt–Nielsen ladder)

[documents/tfpt_1_architecture_e8/sections/009-source.tex:50-73](../../../../documents/tfpt_1_architecture_e8/sections/009-source.tex#L50) · `section:bb8c7f52275738bbe02f` · subsection

The transport length [formula in source] is a Froggatt–Nielsen-type charge with expansion parameter [formula in source] : The top sits at [formula in source] (the unwound carrier direction), so [formula in source] ( [formula in source] ); every other charged fermion is suppressed by integer powers of [formula in source] . Numerically (with [formula in source] sector prefactors [formula in source] ): @lcccccccc@ [form

## Closures that the architecture rests on

[documents/tfpt_1_architecture_e8/sections/009-source.tex:135-179](../../../../documents/tfpt_1_architecture_e8/sections/009-source.tex#L135) · `section:ea5c1a7e1cb184a3e1e8` · section

Machine checks for this section: v36_ spectral_ action_ g2.py v4_ flavor_ matrix.py

Explicit source references:

- [verification/v36_spectral_action_g2.py](../../../../verification/v36_spectral_action_g2.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v24) quark ratio closure ---- *) checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117]; checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47]; checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26]; check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3]; check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2]; (* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L105)
- [(* v477 (i): Frullani + the moment dictionary at flat weight *) frul = Integrate[(Exp[-aa tt] - Exp[-tt])/tt, {tt, 0, Infinity}, Assumptions -> aa > 0]; eig = Join[{1}, Table[1/4, 4], Table[1/6, 6]]; tr = Total[Exp[-tt (1 - bb # RR)] & /@ eig] - 11 Exp[-tt]; serR = Normal[Series[tr, {RR, 0, 2}]]; mu1f = Integrate[Coefficient[serR, RR, 1]/tt, {tt, 0, Infinity}]; mu2f = Integrate[Coefficient[serR, RR, 2]/tt, {tt, 0, Infinity}]; checkExact["v477 GRAV.ENTROPIC.SCALEFLOW.01 (i): the Frullani/scale-flow identity -Log[a] = Integrate[(e^{-a t}-e^{-t})/t] (symbolic) and the moment dictionary -- at the FLAT weight the maximally-symmetric relative trace integrates to exactly the v475 raw coefficients 3 b R + (17/24) b^2 R^2 (unit moments mu1 = mu2 = 1): the raw entropic action is the unit-moment point of a scale-measure family", frul == -Log[aa] && Simplify[mu1f - 3 bb] == 0 && Simplify[mu2f - (17/24) bb^2] == 0]; (* v477 (ii): the one moment condition + closure + v36 consistency *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3071)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [(* v475 (iii): the Lorentzian timelike positivity witness *) gL = DiagonalMatrix[{-1, 1, 1, 1}]; mM = Outer[Times, {vv, 0, 0, 0}, {vv, 0, 0, 0}]; evT = Sort[Eigenvalues[(gL + aal mM) . Inverse[gL]]]; evS = Sort[Eigenvalues[(gL + aal Outer[Times, {0, vv, 0, 0}, {0, vv, 0, 0}]) . Inverse[gL]]]; checkExact["v475 GRAV.ENTROPIC.SCALARON.01 (iii): the Lorentzian-positivity witness -- on Minkowski a TIMELIKE gradient gives G g^-1 eigenvalues {1 - alpha v^2, 1, 1, 1} (nonpositive for v^2 >= 1/alpha, ln undefined) while a SPACELIKE gradient gives {1 + alpha v^2, 1, 1, 1} (positive for all v) -- the v473 caveat exhibited, the OS route sturdier", Sort[evT] == Sort[{1 - aal vv^2, 1, 1, 1}] && Sort[evS] == Sort[{1 + aal vv^2, 1, 1, 1}]]; ]; (* ==== v477 round: the scale-flow representation of the entropic action -- the exact content: the Frullani identity Integrate[(e^{-a t}-e^{-t})/t] = -Log[a], the moment dictionary (flat weight = unit moments = the v475 raw coefficients 3 b R + (17/24) b^2 R^2), the ONE moment condition mu2/mu1^2 = (72/17)(8 pi)^9 with the exact closure (4608 pi^2/17)/((72/17)(8 pi)^9) = c3^7, and the v36 consistency f0 = 6 (4 pi)^2/c3^7 <=> M^2 = c3^7 Mbar^2; mirrors v477 (the chi-form quadrature is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3052)

## Consolidated picture

[documents/tfpt_1_architecture_e8/sections/009-source.tex:272-327](../../../../documents/tfpt_1_architecture_e8/sections/009-source.tex#L272) · `section:718f04ace2423814ada5` · section

A small grammar generates many sectors: the Standard-Model packet, flavor, the electroweak hierarchy, the cosmological constant, the metrology, and the inflation/CMB interface. The strongest new statements are exact: the decuple bridge ties [formula in source] to the tenth power of the stripped electroweak scale with [formula in source] ; the Hubble scale is the square root of [formula in source] ; and the Einstein n

Explicit source references:

- [verification/v531_coxeter_tensor_stage_a.py](../../../../verification/v531_coxeter_tensor_stage_a.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v531 round: COX.STAGEA.TENSOR.01 -- the Stage A tensor clock. Exact mirrors: order 30, chi = Phi30, Ramanujan trace tomography, honest Phi15 scope, coprimality controls. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8300)

## The Coxeter–cyclotomic compiler and the explicit [formula in source] construction

[documents/tfpt_1_architecture_e8/sections/009-source.tex:328-365](../../../../documents/tfpt_1_architecture_e8/sections/009-source.tex#L328) · `section:b41c336f017dcb22d331` · part

This short companion compresses the TFPT bridge layer to a single discrete object. The claim is that the Standard-Model family, the cosmological action ladder, the [formula in source] counting data, the flavor budget, inflation and the cosmological constant are not independent coincidences but projections of one structure: the even-weight code [formula in source] on [formula in source] slots, together with its [formu

## Theorem 8 — the [formula in source] anchor microcode and the [formula in source] -ladder

[documents/tfpt_1_architecture_e8/sections/011-source.tex:249-305](../../../../documents/tfpt_1_architecture_e8/sections/011-source.tex#L249) · `section:5d8f619883df80c56b36` · section

tocsectionTheorem 8 — anchor microcode The parabolic flavor bundle [formula in source] on [formula in source] has splitting type [formula in source] , whose power sums [formula in source] generate the whole compiler budget:

Explicit source references:

- [verification/v407_dn_pairings_omega.py](../../../../verification/v407_dn_pairings_omega.py#L1) · explicit_file_citation
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v405_seam_equiv_omega.py](../../../../verification/v405_seam_equiv_omega.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.02](../../../../verification/status_ledger.csv#L475) · explicit_claim_identifier · original status at linked ledger row
- [verification/v832_anchor_flavor_checksum.py](../../../../verification/v832_anchor_flavor_checksum.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)

## -1.2cm TFPT — The Standard Model from the Compiler\\[2mm] The [formula in source] -ladder, the flavor block from parabolic transport, and the worked closures ( [formula in source] , quark [formula in source] , the gap, Starobinsky [formula in source] )

[documents/tfpt_2_standard_model/preamble.tex:1-94](../../../../documents/tfpt_2_standard_model/preamble.tex#L1) · `section:1468343fd774f9e33200` · frontmatter

arrows.meta,positioning,calc,fit,backgrounds,shapes.geometric,shapes.misc,decorations.pathmorphing,decorations.pathreplacing,patterns,angles,quotes,matrix =3.5em

## Front matter / support

[documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex:1-24](../../../../documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex#L1) · `section:3b5318f0d65e3c120bab` · frontmatter

The Standard Model as one [formula in source] -ladder mass formula (all masses, CKM, PMNS, neutrinos), the flavor matrix from parabolic transport on [formula in source] , the five worked closures ( [formula in source] , quark [formula in source] , the explicit mass gap, Starobinsky [formula in source] , the H2 splitting), and gravity/quantum gravity as the seam response (the Seam Response Grammar [formula in source] 

## The Standard Model in one master formula

[documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex:25-36](../../../../documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex#L25) · `section:ba46ba938e8645842055` · part

In one sentence. The fermion spectrum — masses, Yukawa structure, CKM, the PMNS skeleton and the neutrinos — follows from one master formula with three ingredients: the seed [formula in source] , the carrier base [formula in source] and the residue matrix of the compiler. No free Yukawa exponents remain; the charged-lepton amplitudes are closed, the quark mass ratios are closed too (integer Pl\"ucker readouts, v49/ v

Explicit source references:

- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)

## The principle: one master formula instead of many Yukawa numbers

[documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex:37-66](../../../../documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex#L37) · `section:70e249c656b3bbd339e9` · section

In the source-layer construction each fermion mass arises through a Yukawa coupling [formula in source] built as a transport word-length [formula in source] on a hexagon ( [formula in source] ) times a holonomy amplitude. In the compiler picture this is one line:

Explicit source references:

- [verification/v172_trace_anomaly_seed.py](../../../../verification/v172_trace_anomaly_seed.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v172) trace-anomaly seed 4/3 + shared integer 7 ---- *) Module[{cc, chi, anomaly, half, b3, scal, vw}, cc = 8; chi = 2; anomaly = cc chi/6; (* 8/3 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1496)

## The seed [formula in source] as a decoder

[documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex:67-91](../../../../documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex#L67) · `section:2705ce15584daef708e2` · section

A single seed drives four independent low-energy observables. This is the strongest compression of the flavor input:

## The flavor residue matrix is the compiler signature

[documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex:92-216](../../../../documents/tfpt_2_standard_model/sections/001-part-the-standard-model-in-one-master-formula.tex#L92) · `section:7e0600a35f2488ae7d56` · section

The core of the simplification: the word-length matrix [formula in source] splits into the residue matrix [formula in source] (the hexagon packets of the three sectors) and the winding matrix [formula in source] (one [formula in source] per first generation [formula in source] anchor). [formula in source] carries all the discrete flavor information — and its invariants are exclusively compiler numbers:

Explicit source references:

- [verification/v812_flavor_graph_filtration.py](../../../../verification/v812_flavor_graph_filtration.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## Quarks: hierarchy from the same word-lengths

[documents/tfpt_2_standard_model/sections/002-section-quarks-hierarchy-from-the-same-word-lengths.tex:1-164](../../../../documents/tfpt_2_standard_model/sections/002-section-quarks-hierarchy-from-the-same-word-lengths.tex#L1) · `section:115c4091b215e2a670ca` · section

The quark sectors use the same master formula with [formula in source] , [formula in source] . Where two generations share the same word-length the mass ratio is pure transport amplitude; where they differ by [formula in source] a factor [formula in source] appears:

Explicit source references:

- [verification/v42_exterior_leg.py](../../../../verification/v42_exterior_leg.py#L1) · explicit_file_citation
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_file_citation
- [verification/v69_d4_q_geometry.py](../../../../verification/v69_d4_q_geometry.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_file_citation
- [verification/v174_seam_fock_readings.py](../../../../verification/v174_seam_fock_readings.py#L1) · explicit_file_citation
- [verification/v94_sheet_diamond.py](../../../../verification/v94_sheet_diamond.py#L1) · explicit_file_citation
- [verification/make_figures.py](../../../../verification/make_figures.py#L1) · explicit_file_citation
- [verification/v70_q_integer_lift.py](../../../../verification/v70_q_integer_lift.py#L1) · explicit_script_identifier
- [verification/v17_hexagonal_resolvent.py](../../../../verification/v17_hexagonal_resolvent.py#L1) · explicit_file_citation
- [verification/v24_quark_ratio_closure.py](../../../../verification/v24_quark_ratio_closure.py#L1) · explicit_file_citation
- [verification/v26_flavor_frontier_unification.py](../../../../verification/v26_flavor_frontier_unification.py#L1) · explicit_file_citation
- [verification/v37_plucker_anchor.py](../../../../verification/v37_plucker_anchor.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *) checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}", Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]]; checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}", Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} && Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]]; (* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L329)
- [(* ---- (v42) Exterior Leg Lemma: u/d leg is a Lambda^2 F area, not a scalar ---- *) (* u,d share (r,w)=(1,1): the C6 resolvent reads only (r,w) => scalar ratio = 1. *)](../../../../verification/wolfram/tfpt_readouts.wl#L148)
- [(* ---- (v97) sheet-conjugation bridge (P1 -> one [P]) ---- *) TA = {{0, 1, 0}, {1, 0, 0}, {2, -2, 1}}; SigM = DiagonalMatrix[{1, -1, -1}]; sig12 = {{0, 1, 0}, {1, 0, 0}, {0, 0, 1}}; e1v = {0, 0, 1}; e2v = {0, 1, 2}; e3v = {1, 0, 0}; QPm = (Q + SigM.Q.SigM)/2; checkExact["v97 Q_+ eigenvectors e1=(0,0,1) [l=1], e2=(0,1,2) [l=2], e3=(1,0,0) [l=3]", (QPm.e1v == 1 e1v) && (QPm.e2v == 2 e2v) && (QPm.e3v == 3 e3v)]; checkExact["v97 T_A integer involution, det -1, fixes 1 and a; T_A swaps e2 <-> e3, fixes e1", (TA.TA == IdentityMatrix[3]) && (Det[TA] == -1) && (TA.one == one) && (TA.av == av) && (TA.e2v == e3v) && (TA.e3v == e2v) && (TA.e1v == e1v)]; checkExact["v97 anchor = conjugation-symmetric vector: a = e2+e3, 1 = a-e1; odd line e2-e3", (av == e2v + e3v) && (one == av - e1v) && (TA.(e2v - e3v) == -(e2v - e3v))]; ddir = {-1, 1, 0}; coeffs = LinearSolve[Transpose[{one, av, ddir}], TA.ddir]; checkExact["v97 one deck action: T_A = -1 on R^3/span{1,a} (like sigma_12); parity det T_A = det sigma_12 = -1, det Sigma = +1", (coeffs[[3]] == -1) && (sig12.ddir == -ddir) && (Det[sig12] == -1) && (Det[SigM] == 1)]; Gm = TA.SigM; RrotM = {{0, 0, -1}, {1, 0, -1}, {0, 1, -1}}; checkExact["v97 D4 closure: G = T_A.Sigma has order 4, char (t+1)(t^2+1) = char(v70 R_rot)", (MatrixPower[Gm, 4] == IdentityMatrix[3]) && (MatrixPower[Gm, 2] != IdentityMatrix[3]) && (Expand[CharacteristicPolynomial[Gm, t] + (t + 1) (t^2 + 1)] === 0) && (Expand[CharacteristicPolynomial[Gm, t] - CharacteristicPolynomial[RrotM, t]] === 0)]; Svars = Array[sv, {3, 3}]; solS = Quiet[Solve[Flatten[Svars.Gm - RrotM.Svars] == 0, Flatten[Svars]], Solve::svars]; Sgen = Svars /. First[solS]; detSgen = Factor[Det[Sgen]]; checkExact["v97 sheet-index lemma: det S always EVEN on the integer intertwiner space, minimum |det| = 2 = |Z2|", Module[{vars = Variables[detSgen], vals}, vals = Select[Abs[detSgen /. Thread[vars -> #]] & /@ Tuples[Range[-2, 2], Length[vars]], # =!= 0 &]; (And @@ (EvenQ /@ vals)) && (Min[vals] == 2)]]; checkExact["v97 Q (det = N_fam) does NOT intertwine G -> R_rot (independent bridge)", Q.Gm != RrotM.Q]; (* ---- (v98) discriminant dictionary derived ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L249)
- [(* ---- (v24) quark ratio closure ---- *) checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117]; checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47]; checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26]; check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3]; check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2]; (* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L105)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [(* ---- (v174) seam Fock-space readings: cone compression, Witten index, g-theorem ---- *) Module[{cone, blocks, trunc, disc, cUV, cIR}, cone = 2^15; blocks = {Binomial[16, 4], Binomial[16, 6], Binomial[16, 8]}; trunc = Sum[Binomial[4, k], {k, 0, 2}]; (* 11 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1509)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ---- (v37) anchor-plane Plücker apparatus + K+xQ pencil + dualities ---- *) oneV = {1, 1, 1}; aVc = {1, 1, 2}; plLeft[Mat_] := Module[{r1 = oneV.Mat, r2 = aVc.Mat}, {r1[[1]] r2[[2]] - r1[[2]] r2[[1]], r1[[1]] r2[[3]] - r1[[3]] r2[[1]], r1[[2]] r2[[3]] - r1[[3]] r2[[2]]}]; plRight[Mat_] := Module[{c1 = Mat.oneV, c2 = Mat.aVc}, {c1[[1]] c2[[2]] - c1[[2]] c2[[1]], c1[[1]] c2[[3]] - c1[[3]] c2[[1]], c1[[2]] c2[[3]] - c1[[3]] c2[[2]]}]; checkExact["Pl(K) = (-1,6,4) and ||Pl(K)||_1 = 11 (the '11' localised in K)", plLeft[K] == {-1, 6, 4} && Total[Abs[plLeft[K]]] == 11]; checkExact["Pl_R(K)=(12,12,-2), ||Pl_R(K)||_1=26; sum Pl_R(L)=60 (cascade start)", plRight[K] == {12, 12, -2} && Total[Abs[plRight[K]]] == 26 && Total[plRight[L]] == 60]; checkExact["pencil det(K + x Q) = 3x^3 + 7x^2 + 6x + 4 = (N_fam,7,|R+A3|,|mu4|)", Expand[Det[K + x Q]] === 3 x^3 + 7 x^2 + 6 x + 4]; checkExact["lepton-up duality: K_e - K_u = a = (1,1,2)", K[[3]] - K[[1]] == {1, 1, 2}]; checkExact["lepton-up duality: L_e - L_u = Exp(A3) = (1,2,3)", L[[3]] - L[[1]] == {1, 2, 3}]; checkExact["lepton ring: c_e c_tau = |Z2| c_mu (= 8/3)", ce ctau == 2 cmu]; (* ---- (v39) (U_wall) selectors read off the bundle (algebraic) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L122)

## The Sheet Diamond and the Winding Line: masses and transport from one surface

[documents/tfpt_2_standard_model/sections/002-section-quarks-hierarchy-from-the-same-word-lengths.tex:165-183](../../../../documents/tfpt_2_standard_model/sections/002-section-quarks-hierarchy-from-the-same-word-lengths.tex#L165) · `section:9343e60c67510b20c910` · section

The mass-power matrix and the transport word-length matrix are not two independent machines: they are the two sheet-readouts of one parabolic projection [formula in source] acting on the residue matrix [formula in source] . Collect the [formula in source] -orders [formula in source] of the nine charged fermions into the mass-power matrix with [formula in source] the sheet ( [formula in source] ) involution. Then, exa

Explicit source references:

- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)

## Front matter / support

[documents/tfpt_2_standard_model/sections/003-source.tex:1-447](../../../../documents/tfpt_2_standard_model/sections/003-source.tex#L1) · `section:51e91159532ef7479ff8` · frontmatter

The whole flavor algebra lives on a single two-parameter operator surface, [formula in source] with the two global invariants [formula in source] The mass-transport pencil [formula in source] is the cut [formula in source] , on which the anchor-block determinant factorises as [formula in source] — the master cover of the operator-pencil sections below (unique up to M\"obius reparametrisation, v85_master_cover.py). Th

Explicit source references:

- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier
- [verification/v135_det_surface.py](../../../../verification/v135_det_surface.py#L1) · explicit_file_citation
- [verification/v528_seam_bit_twist_class_definition.py](../../../../verification/v528_seam_bit_twist_class_definition.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean#L1) · explicit_file_citation
- [verification/v689_gaussian_code_bridge.py](../../../../verification/v689_gaussian_code_bridge.py#L1) · explicit_file_citation
- [verification/v568_bit_selector_ladder.py](../../../../verification/v568_bit_selector_ladder.py#L1) · explicit_file_citation
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v218_diamond_axis_geometry.py](../../../../verification/v218_diamond_axis_geometry.py#L1) · explicit_file_citation
- [verification/v574_stageb_winding.py](../../../../verification/v574_stageb_winding.py#L1) · explicit_file_citation
- [verification/v776_boundary_hamming_uniqueness.py](../../../../verification/v776_boundary_hamming_uniqueness.py#L1) · explicit_file_citation
- [verification/v874_feedback_decoder_lean.py](../../../../verification/v874_feedback_decoder_lean.py#L1) · explicit_file_citation
- [E8.GAUSSCODE.01](../../../../verification/status_ledger.csv#L660) · explicit_claim_identifier · original status at linked ledger row
- [verification/v567_carrier_free_q_reconstruction.py](../../../../verification/v567_carrier_free_q_reconstruction.py#L1) · explicit_file_citation
- [verification/v72_q_det_from_cusp.py](../../../../verification/v72_q_det_from_cusp.py#L1) · explicit_script_identifier
- [verification/v128_graded_hull.py](../../../../verification/v128_graded_hull.py#L1) · explicit_file_citation
- [verification/v736_orbit_packet.py](../../../../verification/v736_orbit_packet.py#L1) · explicit_file_citation
- [verification/v597_mu4_cover_model.py](../../../../verification/v597_mu4_cover_model.py#L1) · explicit_file_citation
- [verification/v590_involution_existence.py](../../../../verification/v590_involution_existence.py#L1) · explicit_file_citation
- [verification/v566_parabolic_anchor_selfcode.py](../../../../verification/v566_parabolic_anchor_selfcode.py#L1) · explicit_script_identifier
- [verification/v600_joint_embedding.py](../../../../verification/v600_joint_embedding.py#L1) · explicit_file_citation
- [E8.QUARTICHALF.01](../../../../verification/status_ledger.csv#L661) · explicit_claim_identifier · original status at linked ledger row
- [verification/v14_carrier_uniqueness.py](../../../../verification/v14_carrier_uniqueness.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1) · explicit_file_citation
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_script_identifier
- [verification/v598_cover_dictionary.py](../../../../verification/v598_cover_dictionary.py#L1) · explicit_file_citation
- [verification/v752_projective_hamming_incidence.py](../../../../verification/v752_projective_hamming_incidence.py#L1) · explicit_file_citation
- [verification/v601_equivariant_dual.py](../../../../verification/v601_equivariant_dual.py#L1) · explicit_file_citation
- [verification/v230_center_budget_norms.py](../../../../verification/v230_center_budget_norms.py#L1) · explicit_file_citation
- [verification/v737_seam48_intertwiner.py](../../../../verification/v737_seam48_intertwiner.py#L1) · explicit_script_identifier
- [verification/v799_seam_code_typeii.py](../../../../verification/v799_seam_code_typeii.py#L1) · explicit_file_citation
- [verification/v798_seam_clifford_modular_s.py](../../../../verification/v798_seam_clifford_modular_s.py#L1) · explicit_file_citation
- [verification/v690_quartic_half.py](../../../../verification/v690_quartic_half.py#L1) · explicit_file_citation
- [verification/v95_centered_diamond.py](../../../../verification/v95_centered_diamond.py#L1) · explicit_file_citation
- [verification/v599_real_structure.py](../../../../verification/v599_real_structure.py#L1) · explicit_file_citation
- [verification/v572_rp_bit_form.py](../../../../verification/v572_rp_bit_form.py#L1) · explicit_file_citation
- [verification/v775_gaussian_class_d5_purity.py](../../../../verification/v775_gaussian_class_d5_purity.py#L1) · explicit_file_citation
- [verification/v774_arf_spinor_compiler.py](../../../../verification/v774_arf_spinor_compiler.py#L1) · explicit_file_citation
- [verification/v69_d4_q_geometry.py](../../../../verification/v69_d4_q_geometry.py#L1) · explicit_script_identifier
- [verification/v222_cm_norm_duality.py](../../../../verification/v222_cm_norm_duality.py#L1) · explicit_file_citation
- [verification/v857_simplex_fourier_winding.py](../../../../verification/v857_simplex_fourier_winding.py#L1) · explicit_file_citation
- [verification/v134_dual_anchor.py](../../../../verification/v134_dual_anchor.py#L1) · explicit_file_citation
- [verification/v94_sheet_diamond.py](../../../../verification/v94_sheet_diamond.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1) · explicit_file_citation
- [verification/v584_ext_source_response.py](../../../../verification/v584_ext_source_response.py#L1) · explicit_file_citation
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_script_identifier
- [SEAM.CODE.TYPEII.01](../../../../verification/status_ledger.csv#L691) · explicit_claim_identifier · original status at linked ledger row
- [verification/v638_code_semantics.py](../../../../verification/v638_code_semantics.py#L1) · explicit_script_identifier
- [verification/v37_plucker_anchor.py](../../../../verification/v37_plucker_anchor.py#L1) · explicit_script_identifier
- [GATE.QGEO.01](../../../../verification/status_ledger.csv#L52) · explicit_claim_identifier · original status at linked ledger row
- [verification/v85_master_cover.py](../../../../verification/v85_master_cover.py#L1) · explicit_file_citation
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/FlavorFeedback.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/FlavorFeedback.lean#L1) · explicit_file_citation
- [verification/v224_diamond_ftransfer_path.py](../../../../verification/v224_diamond_ftransfer_path.py#L1) · explicit_file_citation
- [verification/v310_carrier_sm_anomaly.py](../../../../verification/v310_carrier_sm_anomaly.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean#L1)
- [(* v230 center budget (7,11,13) = three local norms *) RRm = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; QQm = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Cc2 = RRm + QQm.DiagonalMatrix[{1, 0, 0}]; checkExact["v230 CENTER.NORM.01: C=R+Q diag(1,0,0) row sums (7,11,13) = " <> "(N_Z[omega](3+2w)=7 hex, C(4,0)+C(4,1)+C(4,2)=11 QBL Fock, N_Z[i](3+2i)=13 square) " <> "= (hex norm, boundary Fock count, square norm)", Total /@ Cc2 == {7, 11, 13} && {Nw[3, 2], Binomial[4, 0] + Binomial[4, 1] + Binomial[4, 2], Ni[3, 2]} == {7, 11, 13}]; (* v224 diamond F_transfer path: sheet axis curved, winding axis flat, Plucker steps *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1838)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [(* ---- (v218) DIAMOND.AXIS/PLUCKER/SPECTRAL.01: the diamond axis geometry ---- *) Module[{R, Q, a, one, Cc, U, V, K, L, F, anc, plL, ram, x, y, dU, dV, bU, bV, sd, bsd, sq, ker}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; one = {1, 1, 1}; a = {1, 1, 2}; Cc = R + Q.DiagonalMatrix[{1, 0, 0}]; (* center C = M(1,0) (v95) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1751)
- [(* ==== v219-v230 round: icosahedral McKay, CM-norm duality, structural finds ==== *) Module[{labels, edges, A, Ni, Nw, RRm, QQm, Cc2, Mst, s, t, d, nvec, one, av, KKm, Lm}, (* v219 McKay: affine E8 marks = 2I irrep degrees, sums 30 and 120 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1780)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [(* ---- (v37) anchor-plane Plücker apparatus + K+xQ pencil + dualities ---- *) oneV = {1, 1, 1}; aVc = {1, 1, 2}; plLeft[Mat_] := Module[{r1 = oneV.Mat, r2 = aVc.Mat}, {r1[[1]] r2[[2]] - r1[[2]] r2[[1]], r1[[1]] r2[[3]] - r1[[3]] r2[[1]], r1[[2]] r2[[3]] - r1[[3]] r2[[2]]}]; plRight[Mat_] := Module[{c1 = Mat.oneV, c2 = Mat.aVc}, {c1[[1]] c2[[2]] - c1[[2]] c2[[1]], c1[[1]] c2[[3]] - c1[[3]] c2[[1]], c1[[2]] c2[[3]] - c1[[3]] c2[[2]]}]; checkExact["Pl(K) = (-1,6,4) and ||Pl(K)||_1 = 11 (the '11' localised in K)", plLeft[K] == {-1, 6, 4} && Total[Abs[plLeft[K]]] == 11]; checkExact["Pl_R(K)=(12,12,-2), ||Pl_R(K)||_1=26; sum Pl_R(L)=60 (cascade start)", plRight[K] == {12, 12, -2} && Total[Abs[plRight[K]]] == 26 && Total[plRight[L]] == 60]; checkExact["pencil det(K + x Q) = 3x^3 + 7x^2 + 6x + 4 = (N_fam,7,|R+A3|,|mu4|)", Expand[Det[K + x Q]] === 3 x^3 + 7 x^2 + 6 x + 4]; checkExact["lepton-up duality: K_e - K_u = a = (1,1,2)", K[[3]] - K[[1]] == {1, 1, 2}]; checkExact["lepton-up duality: L_e - L_u = Exp(A3) = (1,2,3)", L[[3]] - L[[1]] == {1, 2, 3}]; checkExact["lepton ring: c_e c_tau = |Z2| c_mu (= 8/3)", ce ctau == 2 cmu]; (* ---- (v39) (U_wall) selectors read off the bundle (algebraic) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L122)
- [(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *) checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}", Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]]; checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}", Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} && Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]]; (* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L329)
- [(* ---- (v95) centered flavor diamond ---- *) Uop = Q.DiagonalMatrix[{1, 0, 0}]; Vop = Q.DiagonalMatrix[{0, 1, 1}]; Cc = R + Uop; Lop = R + 2 Uop; Fop = R + Q; checkExact["v95 centered cross: Q=U+V; R=C-U, L=C+U, K=C-V, F=C+V", (Q == Uop + Vop) && (R == Cc - Uop) && (Lop == Cc + Uop) && (K == Cc - Vop) && (Fop == Cc + Vop)]; checkExact["v95 axes spectra: Spec U = {3,0,0} (winding), Spec V = {0,1,2} = N_fam*cusp", (Sort[Eigenvalues[Uop]] == {0, 0, 3}) && (Sort[Eigenvalues[Vop]] == {0, 1, 2})]; checkExact["v95 center invariants: tr C=12, det C=14, sum C=31=2^g_car-1, det B_C=28", (Tr[Cc] == 12) && (Det[Cc] == 14) && (Total[Cc, 2] == 31) && (31 == 2^gcar - 1) && (Det[bb[Cc]] == 28)]; checkExact["v95 ray alignment: Pi_R(C)=7(2,3,1), Pi_R(L)=10(2,3,1)", (plR[Cc] == 7 {2, 3, 1}) && (plR[Lop] == 10 {2, 3, 1})]; (* ---- (v96) branch-kernel selection (P1) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L204)
- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)
- [(* ---- (v84) frozen registry decimals recompute from the axioms ---- *) phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); FU1[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 41 Log[1/phiseam[a]]; aStar = a /. FindRoot[FU1[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; check["v84 ALPHA_INV frozen", 1/aStar, 137.0359992168407125035379`30, 10^-20]; lamC = Sqrt[phi0 (1 - phi0)]; check["v84 SIN2_THETA12_SEED frozen", 1/3 - phi0/2, 0.3067473572449105696786871`30, 10^-20]; check["v84 SIN2_THETA13 frozen", phi0 Exp[-5/6], 0.02310843515888110429328466`30, 10^-20]; check["v84 BETA_BIREFRINGENCE_DEG frozen", (phi0/(4 Pi)) (180/Pi), 0.2424350309009295284924315`30, 10^-20]; check["v84 OMEGA_B frozen", (1 - 1/(4 Pi)) phi0, 0.04894066266545011220054565`30, 10^-20]; check["v84 LAMBDA_C frozen", lamC, 0.2243762368847217731120972`30, 10^-20]; check["v84 S23_CKM frozen", phi0/(1 + lamC), 0.04342778843220215630289116`30, 10^-20]; check["v84 S13_CKM frozen", lamC^3/3, 0.003765384454486429837965432`30, 10^-20]; check["v84 DELTA_CKM_RAD frozen", Pi/3 + 3 lamC^2, 1.198231638232244084651243`30, 10^-20]; check["v84 MMU_OVER_MTAU frozen", (8/7) phi0, 0.06076794534496631692490568`30, 10^-20]; check["v84 ME_OVER_MMU frozen", (12/7) phi0^2, 0.004846725425651567674771059`30, 10^-20]; checkExact["v84 MU_OVER_MD = 55/117 exactly", 55/117 == 55/117]; check["v84 MC_OVER_MS frozen", (34/47)/phi0, 13.60499710285539356302651`30, 10^-20]; check["v84 MT_OVER_MB frozen", (3/26)/phi0^2, 40.8115130177002629681607`30, 10^-20]; check["v84 MSCAL_OVER_MBAR frozen", c3^(7/2), 0.00001256494208322844896998079`30, 10^-20]; check["v84 RHOL_OVER_MBAR4 frozen", (3/(4 Pi^2)) Exp[-2/aStar], 7.125329526706216792033797`30 10^-121, 10^-15]; checkExact["v84 theta12 variants distinct (seed < seam < nonlin band)", (1/3 - phi0/2) < (1/3 - 1/(12 Pi))]; (* ---- (v85) master cover: GL(2) covariance on the anchor plane ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L38)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ParityWeightLaws.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ParityWeightLaws.lean#L1)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* v222 CM-norm duality: 41 (square), 7 (hex), 13 (square) *) Ni[a_, b_] := a^2 + b^2; (* Gaussian Z[i] norm *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1793)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ==== v528 round: SEAM.BIT.TWISTCLASS.01 -- bit = twist-class choice. Exact mirrors: (i) cardinality lemma; (ii) 224-axis flip census; (iii) O-values. Pfaffian spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8213)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean#L1)
- [(* ---- (v127) ring resummation ---- *) Module[{proj, partial}, proj = {{1, 0, 0}, {0, 0, 0}, {0, 0, 0}}; checkExact["v127 log-det identity: det(1 - a P) = 1 - a (rank-1 P); series -ln(1-a) = a + a^2/2 + a^3/3 + ...", Simplify[Det[IdentityMatrix[3] - a proj] - (1 - a)] === 0 && Normal[Series[-Log[1 - a], {a, 0, 3}]] === a + a^2/2 + a^3/3]; partial[al_, kmax_] := 6 Sum[al^j/j, {j, kmax}]; checkExact["v127 ring ladder: k=1 ring = classical (2, 4 at weights 1, 2); k=2 ring = 1/3 at weight 1; partials below exact and monotone", partial[1/3, 1] == 2 && partial[2/3, 1] == 4 && 6 (1/3)^2/2 == 1/3 && partial[1/3, 8] < -6 Log[1 - 1/3] && partial[1/3, 2] > partial[1/3, 1]]; checkExact["v127 coupling cross-link + wall: kappa_seam = 8/24 = 1/3 = alpha_1 (kappa = alpha_1/pi); ring series diverges at alpha -> 1", 8/24 == 1/3 && Limit[-Log[1 - a], a -> 1, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v128) graded hull ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L903)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ---- (v134) dual anchor ---- *) Module[{rmat, lmat, qmat, av, onev, e1v, nv, d, rinv1}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; lmat = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; av = {1, 1, 2}; onev = {1, 1, 1}; e1v = {1, 0, 0}; nv = {5, -9, 6}; d = av . Inverse[rmat]; rinv1 = Inverse[rmat] . onev; checkExact["v134 dual anchor: a.R^-1 = a.L^-1 = (-1/2,-1/2,1); d.1 = 0, d.a = 1; (1,1,-2) = -2d; d = (3/2)(a - (4/3)1)", d == av . Inverse[lmat] && d == {-1/2, -1/2, 1} && d . onev == 0 && d . av == 1 && {1, 1, -2} == -2 d && d == 3/2 (av - 4/3 onev)]; checkExact["v134 Sherman-Morrison: L = R + 6*1 e1^T; R^-1 1 = (1,1,-1)/4; a on the invariance plane, 1/e1/n not (1/4, 1/4, -5/2); n.1 = 2", lmat == rmat + 6 Outer[Times, onev, e1v] && rinv1 == {1/4, 1/4, -1/4} && av . rinv1 == 0 && onev . rinv1 == 1/4 && e1v . rinv1 == 1/4 && nv . rinv1 == -5/2 && nv . onev == 2]; ]; (* ---- (v135) determinant surface ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1010)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* v431 (3): 6k+2 family = {2} U det-ladder {8,14,20} on winding line 6s+8 *) fam2 = Sort[Select[degs, Mod[#, 6] == 2 &]]; R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; C = R + Q . DiagonalMatrix[{1, 0, 0}]; L = R + Q . DiagonalMatrix[{2, 0, 0}]; ladder = {Det[R], Det[C], Det[L]}; surf = Table[6 s + 8, {s, 0, 2}]; checkExact["v431 E8.DEGREE.LADDER.01 (iii): degrees==2 mod 6 = {2,8,14,20}; {8,14,20}=(det R,det C,det L)=winding line det M(s,0)=6s+8 (v135); 2=matched metric, 8=rank E8", fam2 == {2, 8, 14, 20} && ladder == {8, 14, 20} && ladder == surf && ladder[[1]] == 8]; (* v431 (4): 18 = 6*N_fam spine member, not det-ladder holdout *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2678)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)

## Closing the audit gates: is [formula in source] , [formula in source] , [formula in source] derived or imported?

[documents/tfpt_2_standard_model/sections/005-subsection-closing-the-audit-gates-is-m-41-k-q-derived-o.tex:161-284](../../../../documents/tfpt_2_standard_model/sections/005-subsection-closing-the-audit-gates-is-m-41-k-q-derived-o.tex#L161) · `section:72a14eb552d3c9fdbe67` · subsection

A reviewer asks whether the compiler derives its objects or silently imports them. We answer the three flavor/EM gates explicitly ( v13_open_gates.py); each is either closed or reduced to a named geometric statement, with the honest residual flagged.

Explicit source references:

- [verification/v467_thirdgen_mixing_pattern.py](../../../../verification/v467_thirdgen_mixing_pattern.py#L1) · explicit_script_identifier
- [verification/v21_solar_product_quark.py](../../../../verification/v21_solar_product_quark.py#L1) · explicit_file_citation
- [verification/v74_compiler_micro_lemmas.py](../../../../verification/v74_compiler_micro_lemmas.py#L1) · explicit_file_citation
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_file_citation
- [verification/v79_review_identities.py](../../../../verification/v79_review_identities.py#L1) · explicit_file_citation
- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_file_citation
- [verification/v163_rg_stability_flavor.py](../../../../verification/v163_rg_stability_flavor.py#L1) · explicit_file_citation
- [verification/v13_open_gates.py](../../../../verification/v13_open_gates.py#L1) · explicit_file_citation
- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_file_citation
- [verification/v164_qcd_scale.py](../../../../verification/v164_qcd_scale.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [(* ---- (v73) k=c3/2 forced: variational factor x Gauss-Bonnet topology; Fursaev-Solodukhin S=A/4 ---- *) checkExact["k=c3/2=1/(16pi)=(1/2)*(1/(|Z2|*2pi*chi(S2))), chi(S2)=2; Fursaev-Solodukhin 4pi k = 1/4", Module[{c3 = 1/(8 Pi), chi = 2, Z2 = 2}, (c3/2 == 1/(16 Pi)) && (c3 == 1/(Z2*2 Pi*chi)) && (4 Pi*(c3/2) == 1/4)]]; (* ---- (v74) compiler micro-lemmas: pencil differences 2->16->48; anchor QF 41-25=16 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L352)
- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v79) hypercharge Lucas-Binet D_n + the quark-ratio reading ---- *) checkExact["Lucas-Binet D_n=(3^n-(-2)^n)/5 = {1,1,7,13,55,133}; c_u/c_d = D_5/(N_fam^2 D_4) = 55/117", Module[{D}, D = Table[(3^n - (-2)^n)/5, {n, 1, 6}]; D == {1, 1, 7, 13, 55, 133} && D[[5]]/(Nfam^2 D[[4]]) == 55/117]]; (* ---- (v79) Inverse Anchor Theorem: 1^T M^-1 1 = 1/atom; a^T M^-1 a = 1 for R,K,L ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L385)

## Mixing: CKM and PMNS from holonomy

[documents/tfpt_2_standard_model/sections/005-subsection-closing-the-audit-gates-is-m-41-k-q-derived-o.tex:285-324](../../../../documents/tfpt_2_standard_model/sections/005-subsection-closing-the-audit-gates-is-m-41-k-q-derived-o.tex#L285) · `section:d0b4a8a863a916ac84c8` · section

@p3.0cmp6.0cmcc@ Quantity & Formula & Prediction & PDG \\ [formula in source] & [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & [formula in source] & [formula in source] & [formula in source] \\ [formula in source] & [formula in source] (leading, ) & [formula in source] rad & [formula in s

## Downstream flavor readout: the rare kaons [formula in source]

[documents/tfpt_2_standard_model/sections/005-subsection-closing-the-audit-gates-is-m-41-k-q-derived-o.tex:325-356](../../../../documents/tfpt_2_standard_model/sections/005-subsection-closing-the-audit-gates-is-m-41-k-q-derived-o.tex#L325) · `section:9cb3b04ab25cb016cf69` · subsection

The closed CKM point is not an end state — it feeds the theoretically cleanest flavor-changing neutral-current probe, the rare decays [formula in source] and [formula in source] . These are not a new compiler power: the only TFPT-specific content is the CKM point above; the short-distance loop functions ( [formula in source] , [formula in source] , [formula in source] , [formula in source] , Brod–Gorbahn–Stamou) are 

Explicit source references:

- [verification/v202_rare_kaon.py](../../../../verification/v202_rare_kaon.py#L1) · explicit_file_citation
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier

## Neutrinos

[documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex:1-262](../../../../documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex#L1) · `section:697c671889813baf24f5` · section

The neutrino sector is the Majorana branch of the same construction: [formula in source] . @p3.6cmp5.2cmc@ Quantity & Origin & Value \\ [formula in source] & [formula in source] (UV), closure [formula in source] & [formula in source] \\ [formula in source] & primary (freeze): [formula in source] (seed, [formula in source] ); two derived variants in the named box & [formula in source] (NuFIT 6.0 [formula in source] ) 

Explicit source references:

- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier
- [verification/v338_theta13_budget.py](../../../../verification/v338_theta13_budget.py#L1) · explicit_file_citation
- [verification/v263_mnu_from_df.py](../../../../verification/v263_mnu_from_df.py#L1) · explicit_file_citation
- [verification/v482_seesaw_rung_decision.py](../../../../verification/v482_seesaw_rung_decision.py#L1) · explicit_file_citation
- [verification/v253_kappa_scalaron_ps.py](../../../../verification/v253_kappa_scalaron_ps.py#L1) · explicit_script_identifier
- [verification/v488_majorana_clebsch_door.py](../../../../verification/v488_majorana_clebsch_door.py#L1) · explicit_script_identifier
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v355_e8_unmapped_bandwidth.py](../../../../verification/v355_e8_unmapped_bandwidth.py#L1) · explicit_script_identifier
- [FLAV.DM2RATIO.01](../../../../verification/status_ledger.csv#L529) · explicit_claim_identifier · original status at linked ledger row
- [verification/v252_full_finite_triple.py](../../../../verification/v252_full_finite_triple.py#L1) · explicit_script_identifier
- [verification/v272_nu_mass_scale.py](../../../../verification/v272_nu_mass_scale.py#L1) · explicit_script_identifier
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [verification/v320_galois_cp_relation.py](../../../../verification/v320_galois_cp_relation.py#L1) · explicit_script_identifier
- [verification/v50_q_geometry.py](../../../../verification/v50_q_geometry.py#L1) · explicit_script_identifier
- [verification/v328_theta13_pressure.py](../../../../verification/v328_theta13_pressure.py#L1) · explicit_file_citation
- [REG.FREEZE.01](../../../../verification/status_ledger.csv#L158) · explicit_claim_identifier · original status at linked ledger row
- [verification/v478_entropic_continuum_legs.py](../../../../verification/v478_entropic_continuum_legs.py#L1) · explicit_script_identifier
- [verification/v393_corrections_numeric.py](../../../../verification/v393_corrections_numeric.py#L1) · explicit_script_identifier
- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_script_identifier
- [verification/v481_seesaw_carrier_ladder.py](../../../../verification/v481_seesaw_carrier_ladder.py#L1) · explicit_file_citation
- [verification/v986_nu_scalaron_rung.py](../../../../verification/v986_nu_scalaron_rung.py#L1) · explicit_file_citation
- [verification/v69_d4_q_geometry.py](../../../../verification/v69_d4_q_geometry.py#L1) · explicit_script_identifier
- [FLAV.THIRDGEN.PATTERN.01](../../../../verification/status_ledger.csv#L528) · explicit_claim_identifier · original status at linked ledger row
- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_script_identifier
- [FLAV.NU.TEXTURE.MECHANISM.01](../../../../verification/status_ledger.csv#L768) · explicit_claim_identifier · original status at linked ledger row
- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_file_citation
- [verification/v233_cp_triality_phase.py](../../../../verification/v233_cp_triality_phase.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.06](../../../../verification/status_ledger.csv#L765) · explicit_claim_identifier · original status at linked ledger row
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier
- [verification/v249_ps_unification.py](../../../../verification/v249_ps_unification.py#L1) · explicit_script_identifier
- [verification/v468_dm2_ratio_jarlskog.py](../../../../verification/v468_dm2_ratio_jarlskog.py#L1) · explicit_script_identifier
- [verification/v306_seed_crossval.py](../../../../verification/v306_seed_crossval.py#L1) · explicit_script_identifier
- [verification/v231_cp_mu6_phases.py](../../../../verification/v231_cp_mu6_phases.py#L1) · explicit_script_identifier
- [verification/v1003_nu_structural_nulls.py](../../../../verification/v1003_nu_structural_nulls.py#L1) · explicit_file_citation
- [verification/v470_alpha_inflow_level.py](../../../../verification/v470_alpha_inflow_level.py#L1) · explicit_script_identifier
- [verification/v1001_nu_pentagon_chain.py](../../../../verification/v1001_nu_pentagon_chain.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/nu_texture_census_probe.py](../../../../experiments/tfpt-discovery/nu_texture_census_probe.py#L1) · explicit_file_citation
- [verification/v247_e8_branching_no126.py](../../../../verification/v247_e8_branching_no126.py#L1) · explicit_script_identifier
- [verification/v248_ps_algebra.py](../../../../verification/v248_ps_algebra.py#L1) · explicit_script_identifier
- [verification/v406_pmns_phase_origin.py](../../../../verification/v406_pmns_phase_origin.py#L1) · explicit_file_citation
- [verification/v405_seam_equiv_omega.py](../../../../verification/v405_seam_equiv_omega.py#L1) · explicit_script_identifier
- [verification/v467_thirdgen_mixing_pattern.py](../../../../verification/v467_thirdgen_mixing_pattern.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.02](../../../../verification/status_ledger.csv#L542) · explicit_claim_identifier · original status at linked ledger row
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_script_identifier
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [FLAV.NU.PARENT.INTERTWINER.01](../../../../verification/status_ledger.csv#L777) · explicit_claim_identifier · original status at linked ledger row
- [verification/v268_theta13_carrier_trace.py](../../../../verification/v268_theta13_carrier_trace.py#L1) · explicit_script_identifier
- [verification/v245_spectral_matter_content.py](../../../../verification/v245_spectral_matter_content.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.02](../../../../verification/status_ledger.csv#L475) · explicit_claim_identifier · original status at linked ledger row
- [verification/v354_e8_reverse_audit.py](../../../../verification/v354_e8_reverse_audit.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.04](../../../../verification/status_ledger.csv#L549) · explicit_claim_identifier · original status at linked ledger row
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v725_phys_vgeo_torsor_audit.py](../../../../verification/v725_phys_vgeo_torsor_audit.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.01](../../../../verification/status_ledger.csv#L365) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [(* v431 (5): clean {0,2} split special to E8 among exceptionals *) cleanSplit[name_] := Module[{ex, hh, dm}, ex = Switch[name, "A4", {1, 2, 3, 4}, "D5", {1, 3, 5, 7, 4}, "E6", {1, 4, 5, 7, 8, 11}, "E7", {1, 5, 7, 9, 11, 13, 17}, "E8", exps, "F4", {1, 5, 7, 11}, "G2", {1, 5}]; hh = Switch[name, "A4", 5, "D5", 8, "E6", 12, "E7", 18, "E8", 30, "F4", 12, "G2", 6]; dm = DeleteDuplicates[Mod[ex + 1, 6]]; Sort[ex] == Select[Range[1, hh - 1], CoprimeQ[#, hh] &] && SubsetQ[{0, 2}, dm] && Mod[hh, 6] == 0]; e8Clean = cleanSplit["E8"]; e67Fail = ! (cleanSplit["E6"] && cleanSplit["E7"] && cleanSplit["D5"]); checkExact["v431 E8.DEGREE.LADDER.01 (v): clean {0,2}-mod-6 split (6|h AND exponents=totatives) holds for E8 but FAILS for E6,E7,D5; F4/G2 share split but not spine+flavor-det content", e8Clean && e67Fail && cleanSplit["F4"] && cleanSplit["G2"]]; (* v431 (6): all five 'unmapped' degrees homed; v355 functorial line upheld [P] *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2693)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *) checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}", Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]]; checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}", Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} && Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]]; (* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L329)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)
- [(* v225 dual normal frame (d,n) and oriented volume *) d = av.Inverse[RRm]; nvec = {5, -9, 6}; KKm = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Lm = KKm + QQm; checkExact["v225 DUAL.FRAME.01: d=a.R^{-1}=(-1/2,-1/2,1)=-1/2(1,1,-2) (Nariai normal; " <> "d.1=0, d.a=1); n=(5,-9,6) with n.R=(det R,0,0)=(8,0,0), n.L=(det L,0,0)=(20,0,0); " <> "oriented volume det(1,d,n)=21=N_fam*scalaron=3*7", d == {-1/2, -1/2, 1} && d == -1/2 {1, 1, -2} && d.one == 0 && d.av == 1 && nvec.RRm == {Det[RRm], 0, 0} == {8, 0, 0} && nvec.Lm == {Det[Lm], 0, 0} == {20, 0, 0} && Det[{{1, 1, 1}, d, nvec}] == 21 == 3*7]; ]; (* ==== v231: both CP phases are mu6 powers of one hexagonal unit, split by the sheet ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1861)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ==== v355 E8.UNMAPPED.BANDWIDTH.01: the unmapped region's forced content is COLLECTIVE ==== *) Module[{exps, degs, totatives}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; degs = exps + 1; (* {2,8,12,14,18,20,24,30} *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2362)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ==== v354 E8.REVERSE.AUDIT.01: 3 of 8 E8 Casimir degrees are load-bearing, 5 unmapped ==== *) Module[{exps, degs, mapped, unmapped}, exps = {1, 7, 11, 13, 17, 19, 23, 29}; (* E8 exponents *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2352)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)

## How the legacy layers simplify (bridge map)

[documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex:263-289](../../../../documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex#L263) · `section:40ced8641cc307aac43a` · section

@p0.7cmp3.5cmY@ layer & before & in the compiler picture \\ 1 & boundary [formula in source] & axiom (P1), unchanged; hardenable via Calder\'on/Lean \\ 2 & carrier, [formula in source] , [formula in source] , [formula in source] , [formula in source] & all one Pascal row [formula in source] on [formula in source] ; [formula in source] is the [formula in source] half-spinor \\ 3 & EM fixed point [formula in source] fl

Explicit source references:

- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)

## Is the entire Standard Model thereby derived?

[documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex:290-340](../../../../documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex#L290) · `section:9ab10db608f7371e00a5` · section

Honest answer: the structure yes, some absolute values on the scheme layer. Three layers:

Explicit source references:

- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [EM.FP.01](../../../../verification/status_ledger.csv#L11) · explicit_claim_identifier · original status at linked ledger row
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)

## Closure status of the five former open questions

[documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex:341-347](../../../../documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex#L341) · `section:c62c3f0e611125ba06ab` · section

For each question the entry is typed honestly as closed, reduced or conditional: the proof chain isolating one sharply named remainder — and, where possible, a reduction that makes the problem smaller than previously thought. This is a resolution map, not a claim that all five are fully solved.

## (1) Flavor residual — ratios closed combinatorially; only the absolute scale is the wall-selection [formula in source] /

[documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex:348-377](../../../../documents/tfpt_2_standard_model/sections/006-section-neutrinos.tex#L348) · `section:52b4cce0c7c3cdd6eeca` · subsection

Mehta–Seshadri supplies the equivalence-class framework — stable parabolic bundles [formula in source] irreducible unitary representations — but it does not by itself give ``parabolic-stable [formula in source] transport-minimal'' or the hexagonal word-lengths; that is the TFPT-specific step. The family connection [formula in source] provides the representation, its weights are the cusp exponents, the stable degree i

Explicit source references:

- [verification/v31_R_dictionary.py](../../../../verification/v31_R_dictionary.py#L1) · explicit_file_citation
- [verification/v34_h2_bridge_attempt.py](../../../../verification/v34_h2_bridge_attempt.py#L1) · explicit_file_citation
- [verification/v69_d4_q_geometry.py](../../../../verification/v69_d4_q_geometry.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v33_explicit_flat_bundle.py](../../../../verification/v33_explicit_flat_bundle.py#L1) · explicit_file_citation
- [verification/v30_d4_character_variety.py](../../../../verification/v30_d4_character_variety.py#L1) · explicit_file_citation
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v70_q_integer_lift.py](../../../../verification/v70_q_integer_lift.py#L1) · explicit_script_identifier
- [verification/v27_wall_representative.py](../../../../verification/v27_wall_representative.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *) checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}", Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]]; checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}", Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} && Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]]; (* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L329)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ---- (v97) sheet-conjugation bridge (P1 -> one [P]) ---- *) TA = {{0, 1, 0}, {1, 0, 0}, {2, -2, 1}}; SigM = DiagonalMatrix[{1, -1, -1}]; sig12 = {{0, 1, 0}, {1, 0, 0}, {0, 0, 1}}; e1v = {0, 0, 1}; e2v = {0, 1, 2}; e3v = {1, 0, 0}; QPm = (Q + SigM.Q.SigM)/2; checkExact["v97 Q_+ eigenvectors e1=(0,0,1) [l=1], e2=(0,1,2) [l=2], e3=(1,0,0) [l=3]", (QPm.e1v == 1 e1v) && (QPm.e2v == 2 e2v) && (QPm.e3v == 3 e3v)]; checkExact["v97 T_A integer involution, det -1, fixes 1 and a; T_A swaps e2 <-> e3, fixes e1", (TA.TA == IdentityMatrix[3]) && (Det[TA] == -1) && (TA.one == one) && (TA.av == av) && (TA.e2v == e3v) && (TA.e3v == e2v) && (TA.e1v == e1v)]; checkExact["v97 anchor = conjugation-symmetric vector: a = e2+e3, 1 = a-e1; odd line e2-e3", (av == e2v + e3v) && (one == av - e1v) && (TA.(e2v - e3v) == -(e2v - e3v))]; ddir = {-1, 1, 0}; coeffs = LinearSolve[Transpose[{one, av, ddir}], TA.ddir]; checkExact["v97 one deck action: T_A = -1 on R^3/span{1,a} (like sigma_12); parity det T_A = det sigma_12 = -1, det Sigma = +1", (coeffs[[3]] == -1) && (sig12.ddir == -ddir) && (Det[sig12] == -1) && (Det[SigM] == 1)]; Gm = TA.SigM; RrotM = {{0, 0, -1}, {1, 0, -1}, {0, 1, -1}}; checkExact["v97 D4 closure: G = T_A.Sigma has order 4, char (t+1)(t^2+1) = char(v70 R_rot)", (MatrixPower[Gm, 4] == IdentityMatrix[3]) && (MatrixPower[Gm, 2] != IdentityMatrix[3]) && (Expand[CharacteristicPolynomial[Gm, t] + (t + 1) (t^2 + 1)] === 0) && (Expand[CharacteristicPolynomial[Gm, t] - CharacteristicPolynomial[RrotM, t]] === 0)]; Svars = Array[sv, {3, 3}]; solS = Quiet[Solve[Flatten[Svars.Gm - RrotM.Svars] == 0, Flatten[Svars]], Solve::svars]; Sgen = Svars /. First[solS]; detSgen = Factor[Det[Sgen]]; checkExact["v97 sheet-index lemma: det S always EVEN on the integer intertwiner space, minimum |det| = 2 = |Z2|", Module[{vars = Variables[detSgen], vals}, vals = Select[Abs[detSgen /. Thread[vars -> #]] & /@ Tuples[Range[-2, 2], Length[vars]], # =!= 0 &]; (And @@ (EvenQ /@ vals)) && (Min[vals] == 2)]]; checkExact["v97 Q (det = N_fam) does NOT intertwine G -> R_rot (independent bridge)", Q.Gm != RrotM.Q]; (* ---- (v98) discriminant dictionary derived ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L249)

## (3) Strong CP — decoupled from the mass-gap problem /

[documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex:51-91](../../../../documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex#L51) · `section:e563b224f9d38e2a2c72` · subsection

The key reduction: [formula in source] needs neither the full OS package nor the mass gap. It follows from three purely structural facts plus reflection positivity on the admissible branch:

Explicit source references:

- [verification/v173_pfaffian_cp_car.py](../../../../verification/v173_pfaffian_cp_car.py#L1) · explicit_file_citation

## (4) Constructive QFT closure of the admissible physical sector /

[documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex:92-179](../../../../documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex#L92) · `section:a29d0e884b184665e5ef` · subsection

This is the constructive QFT closure of the admissible physical sector — not the unprojected ambient theory: the unprojected ambient metric measure is not constructed here and remains the [formula in source] frontier item ( ambient QG). On the admissible sector, the input previously listed as ``open'' — the parent-domination / mass-gap lemma from (3) — is not analytically open: it is computed by the explicit discrete

Explicit source references:

- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [QFT4D.EG.ALLORDER.01](../../../../verification/status_ledger.csv#L444) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_file_citation
- [verification/v258_dirac_covariance_induction.py](../../../../verification/v258_dirac_covariance_induction.py#L1) · explicit_file_citation
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v374_ftransfer_qcd.py](../../../../verification/v374_ftransfer_qcd.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v252_full_finite_triple.py](../../../../verification/v252_full_finite_triple.py#L1) · explicit_file_citation
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [verification/v261_modular_spectral_closure.py](../../../../verification/v261_modular_spectral_closure.py#L1) · explicit_file_citation
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v260_k3_kummer_unification.py](../../../../verification/v260_k3_kummer_unification.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)

## Conclusion

[documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex:279-304](../../../../documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex#L279) · `section:be245dd6a6eb1776e773` · section

tocsectionConclusion The simplification is substantial: the discrete Standard-Model structure (charges, families, flavor operators) is derived under the axioms; [formula in source] D existence, chiral measure, mirror gap, couplings and neutrino dynamics are open. The [formula in source] -ladder formula [formula in source] with one seed [formula in source] and one fixed residue matrix whose spectral invariants ( [form

Explicit source references:

- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)

## The flavor block: parabolic weights and the transport theorem

[documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex:305-349](../../../../documents/tfpt_2_standard_model/sections/007-subsection-2-gravity-the-classical-covariant-field-equat.tex#L305) · `section:4842f867b01b3a29625f` · part

This note closes the last structural gap of the [formula in source] compiler by deriving the charged-fermion transport word-lengths [formula in source] , [formula in source] , [formula in source] — equivalently the residue triple [formula in source] and its [formula in source] orbit — from first principles, rather than from the legacy resolvent construction. The correct framework is parabolic Higgs/bundle theory on t

## The setup: parabolic data on the family curve

[documents/tfpt_2_standard_model/sections/008-section-the-setup-parabolic-data-on-the-family-curve.tex:1-49](../../../../documents/tfpt_2_standard_model/sections/008-section-the-setup-parabolic-data-on-the-family-curve.tex#L1) · `section:94523e5f47098f45239e` · section

The family curve is the rigid four-punctured sphere [formula in source] , [formula in source] (the flavor construction above). The flavor bundle is a rank- [formula in source] parabolic bundle [formula in source] on [formula in source] . At each puncture the local monodromy is the order- [formula in source] cusp class with eigenvalues [formula in source] , [formula in source] ; by the Mehta–Seshadri dictionary the co

## The parabolic-weight computation (resolved this round)

[documents/tfpt_2_standard_model/sections/008-section-the-setup-parabolic-data-on-the-family-curve.tex:115-172](../../../../documents/tfpt_2_standard_model/sections/008-section-the-setup-parabolic-data-on-the-family-curve.tex#L115) · `section:95ef9c8e927ef9e25379` · section

Status (no drift). The splitting type is now closed: the unique partition [formula in source] fixes the anchor and [formula in source] fixes the residue branch (verified, below and v4_flavor_matrix.py), and the solar texture is built ( v9_neutrino_texture.py). The roadmap below is kept as the derivation record of how [formula in source] is obtained; it is no longer an open project. The only residual is the parabolic 

Explicit source references:

- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)

## The flavor transport theorem

[documents/tfpt_2_standard_model/sections/008-section-the-setup-parabolic-data-on-the-family-curve.tex:317-378](../../../../documents/tfpt_2_standard_model/sections/008-section-the-setup-parabolic-data-on-the-family-curve.tex#L317) · `section:2084a73fd736c7360a0e` · subsection

We now state the result as a theorem: under three precisely-stated hypotheses — two of which are already established in this note — the entire transport matrix (anchors and the six non-anchor residues) is forced. The combinatorial core is proved by complete enumeration.

## Flavor budget split, row sums, scalaron deficit

[documents/tfpt_2_standard_model/sections/009-section-the-parabolic-anchor-compiler.tex:28-50](../../../../documents/tfpt_2_standard_model/sections/009-section-the-parabolic-anchor-compiler.tex#L28) · `section:c24e9e51ac519b7d5719` · subsection

The flavor budget splits into anchor [formula in source] two equal Coxeter copies: The residue row sums and full row sums read named objects, and the generation (column) sums are [formula in source] . \ Finally the scalaron exponent is the parabolic anti-degree plus the family rank, linking the stable family bundle [formula in source] directly to the inflation scale. The [formula in source] residue sum is the project

Explicit source references:

- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_file_citation

## Closing the flavor block: two theorems

[documents/tfpt_2_standard_model/sections/009-section-the-parabolic-anchor-compiler.tex:198-316](../../../../documents/tfpt_2_standard_model/sections/009-section-the-parabolic-anchor-compiler.tex#L198) · `section:a660765e3a391c14ceef` · section

We promote the two genericity/equivalence steps to proved statements.

Explicit source references:

- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v142_frame_integrality.py](../../../../verification/v142_frame_integrality.py#L1) · explicit_script_identifier
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v75_upoint_to_vgeo.py](../../../../verification/v75_upoint_to_vgeo.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v142) frame integrality ---- *) Module[{onev, av, sigma, nv, axs, sx1, oxa, congOK, mref, rmat, rinv}, onev = {1, 1, 1}; av = {1, 1, 2}; sigma = {2, -9, 5}; nv = {5, -9, 6}; axs = Cross[av, sigma]; sx1 = Cross[sigma, onev]; oxa = Cross[onev, av]; mref = {2, -5, 7}; congOK = And @@ Flatten[Table[ (AllTrue[x axs + y sx1 + z oxa, Mod[#, 11] == 0 &]) == (Mod[x - 3 y + z, 11] == 0), {x, 0, 10}, {y, 0, 10}, {z, 0, 10}]]; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; rinv = Inverse[rmat]; checkExact["v142 frame integrality: 11 m = (m.1)(a x s) + (m.a)(s x 1) + (m.s)(1 x a); integer covectors <=> x - 3y + z = 0 mod 11 (index 11 = ||Pl(K)||_1); with (2,8) the third pairing is forced = 0 mod 11; odd t non-primitive; Cramer: n.a = det R = 8, n.1 = 8 (R^-1 1)_1 = 2", 11 mref == (mref . onev) axs + (mref . av) sx1 + (mref . sigma) oxa && congOK && Mod[2 - 3*8 + 121, 11] == 0 && AllTrue[Range[-21, 21, 2], GCD @@ ({5 + #, -9 - #, 6}) > 1 &] && Det[rmat] == 8 && rinv . onev == {1/4, 1/4, -1/4} && 8 (rinv . onev)[[1]] == 2 == nv . onev && nv . av == 8]; ]; (* ---- (v143) graded Frobenius ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1156)
- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *) checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)", Module[{c = {16/7, 4/3, 7/6}, P, r, c0}, P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3); (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]]; (* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L365)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)

## Closing computations and proofs

[documents/tfpt_2_standard_model/sections/009-section-the-parabolic-anchor-compiler.tex:362-373](../../../../documents/tfpt_2_standard_model/sections/009-section-the-parabolic-anchor-compiler.tex#L362) · `section:c090e3872219b2913e9e` · part

Scope and honesty. This note discharges the items that were flagged ``standard but not written out,'' and now also carries the closures previously collected in the research-sprints note: the seam-fixed Starobinsky mass, the derived solar angle [formula in source] , the H2 splitting type, and the quark [formula in source] amplitude band. It does not force the items that stay typed transfer targets, never compiler powe

Explicit source references:

- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier

## The explicit mass gap closes dynamics and clustering

[documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex:1-160](../../../../documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex#L1) · `section:cbcb5b486b59ced607c8` · section

unique limit state and exponential clustering] The admissible [formula in source] transport transfer operator has the closed spectrum [formula in source] (the cusp cubic). Hence [formula in source] The contraction ratio [formula in source] satisfies the Dobrushin uniqueness condition for a finite-range (range- [formula in source] , cyclic) transfer operator; therefore the thermodynamic limit has a unique Gibbs/vacuum

Explicit source references:

- [verification/v798_seam_clifford_modular_s.py](../../../../verification/v798_seam_clifford_modular_s.py#L1) · explicit_file_citation
- [verification/v783_two_qubit_clifford.py](../../../../verification/v783_two_qubit_clifford.py#L1) · explicit_file_citation
- [verification/v802_gnet_martingale.py](../../../../verification/v802_gnet_martingale.py#L1) · explicit_file_citation
- [GNET.LOCALNET.01](../../../../verification/status_ledger.csv#L675) · explicit_claim_identifier · original status at linked ledger row
- [verification/v746_phys_gnet_local_functor.py](../../../../verification/v746_phys_gnet_local_functor.py#L1) · explicit_file_citation
- [verification/v779_gnet_gns_arf.py](../../../../verification/v779_gnet_gns_arf.py#L1) · explicit_file_citation

## The seam elliptic complex is Fredholm (APS)

[documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex:161-183](../../../../documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex#L161) · `section:0a3610a9e32985012149` · section

Compactify the oriented two-dimensional normal slice [formula in source] to [formula in source] . The geometric BRST/Hodge differential, restricted to the seam-even sector with Atiyah–Patodi–Singer boundary conditions on [formula in source] , is an elliptic operator on a compact manifold; hence it is Fredholm, with finite-dimensional kernel and cokernel and an integer index. The compact bosonic Higgs index selects [f

## The [formula in source] truncation is [formula in source] -bounded

[documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex:184-272](../../../../documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex#L184) · `section:ee5c68ec39d878e448bd` · section

On the [formula in source] attractor the curvature during observable inflation is [formula in source] . Higher curvature terms [formula in source] , [formula in source] , enter with [formula in source] , so their contribution to the observables is [formula in source] . With [formula in source] this is [formula in source] ( [formula in source] ), and the leading predictions are [formula in source] matching Planck. The

Explicit source references:

- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_file_citation
- [verification/v494_cosmo_running_mu_record.py](../../../../verification/v494_cosmo_running_mu_record.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)

## The ambient closure: one spectral-action measure, IR-complete by decoupling

[documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex:273-408](../../../../documents/tfpt_2_standard_model/sections/010-section-the-explicit-mass-gap-closes-dynamics-and-cluste.tex#L273) · `section:9d6c7d63f5df5a4df579` · section

The two formerly-hardest items — the ambient (unprojected) QFT measure beyond the selector [formula in source] , and full quantum gravity beyond the [formula in source] scalaron — are not two separate problems. They are one object: the relative spectral-action measure [formula in source] with [formula in source] the matter/gauge Dirac operator and the gravitational data in the same trace. Three facts reduce both open

Explicit source references:

- [verification/v28_gravity_fR.py](../../../../verification/v28_gravity_fR.py#L1) · explicit_file_citation
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v255_spectral_action_expansion.py](../../../../verification/v255_spectral_action_expansion.py#L1) · explicit_file_citation
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v261_modular_spectral_closure.py](../../../../verification/v261_modular_spectral_closure.py#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v258_dirac_covariance_induction.py](../../../../verification/v258_dirac_covariance_induction.py#L1) · explicit_file_citation
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_file_citation
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)

## The solar angle [formula in source] : derived from the seam

[documents/tfpt_2_standard_model/sections/011-subsection-seam-response-grammar-gravity-is-the-inverse-.tex:69-134](../../../../documents/tfpt_2_standard_model/sections/011-subsection-seam-response-grammar-gravity-is-the-inverse-.tex#L69) · `section:682f3c9b44d35fa728c8` · section

The PMNS matrix is [formula in source] on the Majorana branch. The reactor angle is closed, [formula in source] . The solar angle is realized by a TFPT texture and reduced to the seam-misalignment lemma in three dictionary steps (the residual is the coefficient [formula in source] (leading term [formula in source] ), a [formula in source] conditional input).

Explicit source references:

- [verification/predictions_frozen.json](../../../../verification/predictions_frozen.json#L1) · explicit_file_citation
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_file_citation
- [verification/v84_frozen_registry.py](../../../../verification/v84_frozen_registry.py#L1) · explicit_file_citation
- [REG.FREEZE.01](../../../../verification/status_ledger.csv#L158) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v84) frozen registry decimals recompute from the axioms ---- *) phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); FU1[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 41 Log[1/phiseam[a]]; aStar = a /. FindRoot[FU1[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; check["v84 ALPHA_INV frozen", 1/aStar, 137.0359992168407125035379`30, 10^-20]; lamC = Sqrt[phi0 (1 - phi0)]; check["v84 SIN2_THETA12_SEED frozen", 1/3 - phi0/2, 0.3067473572449105696786871`30, 10^-20]; check["v84 SIN2_THETA13 frozen", phi0 Exp[-5/6], 0.02310843515888110429328466`30, 10^-20]; check["v84 BETA_BIREFRINGENCE_DEG frozen", (phi0/(4 Pi)) (180/Pi), 0.2424350309009295284924315`30, 10^-20]; check["v84 OMEGA_B frozen", (1 - 1/(4 Pi)) phi0, 0.04894066266545011220054565`30, 10^-20]; check["v84 LAMBDA_C frozen", lamC, 0.2243762368847217731120972`30, 10^-20]; check["v84 S23_CKM frozen", phi0/(1 + lamC), 0.04342778843220215630289116`30, 10^-20]; check["v84 S13_CKM frozen", lamC^3/3, 0.003765384454486429837965432`30, 10^-20]; check["v84 DELTA_CKM_RAD frozen", Pi/3 + 3 lamC^2, 1.198231638232244084651243`30, 10^-20]; check["v84 MMU_OVER_MTAU frozen", (8/7) phi0, 0.06076794534496631692490568`30, 10^-20]; check["v84 ME_OVER_MMU frozen", (12/7) phi0^2, 0.004846725425651567674771059`30, 10^-20]; checkExact["v84 MU_OVER_MD = 55/117 exactly", 55/117 == 55/117]; check["v84 MC_OVER_MS frozen", (34/47)/phi0, 13.60499710285539356302651`30, 10^-20]; check["v84 MT_OVER_MB frozen", (3/26)/phi0^2, 40.8115130177002629681607`30, 10^-20]; check["v84 MSCAL_OVER_MBAR frozen", c3^(7/2), 0.00001256494208322844896998079`30, 10^-20]; check["v84 RHOL_OVER_MBAR4 frozen", (3/(4 Pi^2)) Exp[-2/aStar], 7.125329526706216792033797`30 10^-121, 10^-15]; checkExact["v84 theta12 variants distinct (seed < seam < nonlin band)", (1/3 - phi0/2) < (1/3 - 1/(12 Pi))]; (* ---- (v85) master cover: GL(2) covariance on the anchor plane ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L38)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)

## Quark [formula in source] -rationals: best values at current precision

[documents/tfpt_2_standard_model/sections/011-subsection-seam-response-grammar-gravity-is-the-inverse-.tex:135-199](../../../../documents/tfpt_2_standard_model/sections/011-subsection-seam-response-grammar-gravity-is-the-inverse-.tex#L135) · `section:d84c8a8b6b42a871e6ef` · section

Every mass is [formula in source] with the leptons exact from the hexagonal resolvent, [formula in source] . The quark [formula in source] are outputs of the same resolvent, but the published table is only [formula in source] -digit, so their closed rationals can only be bracketed at present: @lccccccccc@ [formula in source] & [formula in source] & [formula in source] & [formula in source] & [formula in source] & [fo

Explicit source references:

- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/v814_k5_sixstep_transport.py](../../../../verification/v814_k5_sixstep_transport.py#L1) · explicit_file_citation
- [verification/v808_petersen_sixthroot.py](../../../../verification/v808_petersen_sixthroot.py#L1) · explicit_file_citation
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)

## Front matter / support

[documents/tfpt_3_e8_audit_bootstrap/sections/006-source.tex:1-374](../../../../documents/tfpt_3_e8_audit_bootstrap/sections/006-source.tex#L1) · `section:dcbb8ba68bde5b18c375` · frontmatter

The [formula in source] torsor closure ( VGEO.TORSOR.01). The calibration/scale-torsor audit of the [formula in source] interface ( [formula in source] checks, [formula in source] \,s; verdict torsor closure pass). The interface is a well-defined [formula in source] scale torsor: complete export table [formula in source] ; dimension matrix rank [formula in source] (conditional [A] on the flavor block, named); all con

Explicit source references:

- [E8.PROJHAMMING.01](../../../../verification/status_ledger.csv#L677) · explicit_claim_identifier · original status at linked ledger row
- [VGEO.TORSOR.01](../../../../verification/status_ledger.csv#L670) · explicit_claim_identifier · original status at linked ledger row
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1) · explicit_file_citation
- [verification/v745_qgeo_car_l1_sector_lemma.py](../../../../verification/v745_qgeo_car_l1_sector_lemma.py#L1) · explicit_file_citation
- [GNET.PPINDEX.01](../../../../verification/status_ledger.csv#L671) · explicit_claim_identifier · original status at linked ledger row
- [verification/v807_lorentz_nullselector.py](../../../../verification/v807_lorentz_nullselector.py#L1) · explicit_file_citation
- [E8.ORBITPACKET.01](../../../../verification/status_ledger.csv#L672) · explicit_claim_identifier · original status at linked ledger row
- [verification/v778_qgeo_gridsup_logsum.py](../../../../verification/v778_qgeo_gridsup_logsum.py#L1) · explicit_script_identifier
- [verification/v752_projective_hamming_incidence.py](../../../../verification/v752_projective_hamming_incidence.py#L1) · explicit_file_citation
- [verification/v775_gaussian_class_d5_purity.py](../../../../verification/v775_gaussian_class_d5_purity.py#L1) · explicit_file_citation
- [verification/v757_fano_disc7_bridge.py](../../../../verification/v757_fano_disc7_bridge.py#L1) · explicit_file_citation
- [verification/v776_boundary_hamming_uniqueness.py](../../../../verification/v776_boundary_hamming_uniqueness.py#L1) · explicit_file_citation
- [verification/v14_carrier_uniqueness.py](../../../../verification/v14_carrier_uniqueness.py#L1) · explicit_script_identifier
- [GNET.LOCALNET.01](../../../../verification/status_ledger.csv#L675) · explicit_claim_identifier · original status at linked ledger row
- [verification/v746_phys_gnet_local_functor.py](../../../../verification/v746_phys_gnet_local_functor.py#L1) · explicit_file_citation
- [verification/v781_one_object_clock_census.py](../../../../verification/v781_one_object_clock_census.py#L1) · explicit_file_citation
- [verification/v799_seam_code_typeii.py](../../../../verification/v799_seam_code_typeii.py#L1) · explicit_file_citation
- [verification/v310_carrier_sm_anomaly.py](../../../../verification/v310_carrier_sm_anomaly.py#L1) · explicit_script_identifier
- [GNET.GNSLIMIT.01](../../../../verification/status_ledger.csv#L683) · explicit_claim_identifier · original status at linked ledger row
- [verification/v23_anchor_generator.py](../../../../verification/v23_anchor_generator.py#L1) · explicit_script_identifier
- [verification/v802_gnet_martingale.py](../../../../verification/v802_gnet_martingale.py#L1) · explicit_file_citation
- [verification/v777_ftransfer_clock_jets.py](../../../../verification/v777_ftransfer_clock_jets.py#L1) · explicit_file_citation
- [verification/v737_seam48_intertwiner.py](../../../../verification/v737_seam48_intertwiner.py#L1) · explicit_file_citation
- [QGEO.GRIDSUP.01](../../../../verification/status_ledger.csv#L682) · explicit_claim_identifier · original status at linked ledger row
- [E8.ONEOBJECT.01](../../../../verification/status_ledger.csv#L684) · explicit_claim_identifier · original status at linked ledger row
- [ARF.ROOTCLASS.01](../../../../verification/status_ledger.csv#L680) · explicit_claim_identifier · original status at linked ledger row
- [verification/v726_phys_car_pp_index.py](../../../../verification/v726_phys_car_pp_index.py#L1) · explicit_file_citation
- [FTRANSFER.CLOCKS.01](../../../../verification/status_ledger.csv#L676) · explicit_claim_identifier · original status at linked ledger row
- [ARF.SPINORCOMPILER.01](../../../../verification/status_ledger.csv#L679) · explicit_claim_identifier · original status at linked ledger row
- [verification/v725_phys_vgeo_torsor_audit.py](../../../../verification/v725_phys_vgeo_torsor_audit.py#L1) · explicit_file_citation
- [verification/v736_orbit_packet.py](../../../../verification/v736_orbit_packet.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/WatataniIndexFour.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/WatataniIndexFour.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean#L1) · explicit_file_citation
- [verification/v792_ftransfer_kms_coset.py](../../../../verification/v792_ftransfer_kms_coset.py#L1) · explicit_file_citation
- [SEAM.CODE.TYPEII.01](../../../../verification/status_ledger.csv#L691) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.CARL1.01](../../../../verification/status_ledger.csv#L674) · explicit_claim_identifier · original status at linked ledger row
- [verification/v779_gnet_gns_arf.py](../../../../verification/v779_gnet_gns_arf.py#L1) · explicit_script_identifier
- [verification/v715_qgeo_car_continuum.py](../../../../verification/v715_qgeo_car_continuum.py#L1) · explicit_script_identifier
- [verification/v623_covered_seam.py](../../../../verification/v623_covered_seam.py#L1) · explicit_script_identifier
- [E8.SEAM48.01](../../../../verification/status_ledger.csv#L673) · explicit_claim_identifier · original status at linked ledger row
- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [ARF.BOUNDARY.CODE.01](../../../../verification/status_ledger.csv#L681) · explicit_claim_identifier · original status at linked ledger row
- [CONTRACT.F.01](../../../../verification/status_ledger.csv#L302) · explicit_claim_identifier · original status at linked ledger row
- [verification/v638_code_semantics.py](../../../../verification/v638_code_semantics.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1) · explicit_file_citation
- [verification/v798_seam_clifford_modular_s.py](../../../../verification/v798_seam_clifford_modular_s.py#L1) · explicit_file_citation
- [QGEO.FANODISC7.01](../../../../verification/status_ledger.csv#L678) · explicit_claim_identifier · original status at linked ledger row
- [verification/v774_arf_spinor_compiler.py](../../../../verification/v774_arf_spinor_compiler.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean#L1)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean#L1)
- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)

## Front matter / support

[documents/tfpt_3_e8_audit_bootstrap/sections/009-section-further-audit-lemmas-machine-verified-this-round.tex:1-189](../../../../documents/tfpt_3_e8_audit_bootstrap/sections/009-section-further-audit-lemmas-machine-verified-this-round.tex#L1) · `section:e7e7f78a69bea2986c9f` · frontmatter

The Wick functor arc ( SEAM.CFIN. WICKFUNCTOR.01 [O]). Three probes ( [formula in source] ; wickfunctor-partial, wickmix-measured (wickmix-obstructed), wickblock-measured (blockfunctor-constructed / seam-diagonal); embedded byte-exact; exact integer/rational/symbolic in every decision typed proved or symbolic). The six compiler roles exist in the deployed seam ( [formula in source] slot pairs [formula in source] the 

Explicit source references:

- [verification/v898_kms_schur_mixing.py](../../../../verification/v898_kms_schur_mixing.py#L1) · explicit_script_identifier
- [SEAM.CFIN.MINIMAL.MEDIATOR.01](../../../../verification/status_ledger.csv#L730) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.CFIN.GAP.PENCIL.01](../../../../verification/status_ledger.csv#L733) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.CFIN.MIXING.NORMALIZATION.01](../../../../verification/status_ledger.csv#L729) · explicit_claim_identifier · original status at linked ledger row
- [verification/v911_wiring_freedom.py](../../../../verification/v911_wiring_freedom.py#L1) · explicit_file_citation
- [SEAM.CFIN.WICKFUNCTOR.01](../../../../verification/status_ledger.csv#L726) · explicit_claim_identifier · original status at linked ledger row
- [verification/v908_seam_equilibrium_wiring.py](../../../../verification/v908_seam_equilibrium_wiring.py#L1) · explicit_script_identifier
- [verification/v896_wick_block_functor.py](../../../../verification/v896_wick_block_functor.py#L1) · explicit_file_citation
- [verification/v903_seam_rp_exclusion.py](../../../../verification/v903_seam_rp_exclusion.py#L1) · explicit_script_identifier
- [SEAM.CFIN.RP.DILATION.01](../../../../verification/status_ledger.csv#L732) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.STATE.WIRING.SELECTOR.01](../../../../verification/status_ledger.csv#L736) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.CFIN.TWISTED.RP.01](../../../../verification/status_ledger.csv#L731) · explicit_claim_identifier · original status at linked ledger row
- [verification/v972_seam_interaction_front.py](../../../../verification/v972_seam_interaction_front.py#L1) · explicit_file_citation
- [SEAM.CFIN.MARGINAL.STABILITY.01](../../../../verification/status_ledger.csv#L734) · explicit_claim_identifier · original status at linked ledger row
- [QGEO.DECKSECTOR.01](../../../../verification/status_ledger.csv#L665) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.CFIN.KMSMIX.01](../../../../verification/status_ledger.csv#L727) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.CFIN.NESS.PARENT.01](../../../../verification/status_ledger.csv#L735) · explicit_claim_identifier · original status at linked ledger row
- [verification/v705_chain_deck_sector.py](../../../../verification/v705_chain_deck_sector.py#L1) · explicit_file_citation

## Further audit lemmas (machine-verified this round)

[documents/tfpt_3_e8_audit_bootstrap/sections/009-section-further-audit-lemmas-machine-verified-this-round.tex:190-227](../../../../documents/tfpt_3_e8_audit_bootstrap/sections/009-section-further-audit-lemmas-machine-verified-this-round.tex#L190) · `section:be6c56c049e0e8a525fd` · section

Five more exact identities tie the flavor matrices and the [formula in source] exponents to the compiler. All checked with exact integer arithmetic.

## Three views of one spine

[documents/tfpt_3_e8_audit_bootstrap/sections/010-section-three-views-of-one-spine.tex:1-48](../../../../documents/tfpt_3_e8_audit_bootstrap/sections/010-section-three-views-of-one-spine.tex#L1) · `section:b19a7595d83b1a10d11a` · section

at (0.35,58) [formula in source] — E-series / atlas branchings (UV); at (0.35,40) [formula in source] ; at (0.35,30) [formula in source] \,(Coxeter rung, [formula in source] ); at (0.35,24) [formula in source] — [formula in source] , [formula in source] , [formula in source] ; at (0.35,15) [formula in source] (IR atoms); at (0.35,8) [formula in source] \,(flavor selector, end); at (0,60.5) [formula in source] start; 

Explicit source references:

- [verification/v91_spine_tetrahedron.py](../../../../verification/v91_spine_tetrahedron.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v431 (1): two-family split forced by 30 = 2*3*5 *) checkExact["v431 E8.DEGREE.LADDER.01 (i): E8 exponents = phi(30)=8 totatives of h=30=2*N_fam*g_car; coprime to 6 => +-1 mod 6, so degrees occupy ONLY {0,2} mod 6", exps == tot30 && EulerPhi[h] == 8 && h == 2*3*5 && expMod6 == {1, 5} && degMod6 == {0, 2}]; (* v431 (2): 6k family = 6 x spine {2,3,4,5} = v91 anchor a=(1,1,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2663)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)

## Sector inventory: have all the old-cascade sectors been computed?

[documents/tfpt_3_e8_audit_bootstrap/sections/010-section-three-views-of-one-spine.tex:74-112](../../../../documents/tfpt_3_e8_audit_bootstrap/sections/010-section-three-views-of-one-spine.tex#L74) · `section:9b133930ab1a7134e578` · section

The old cascade also carried calibrated absolute scales: per block, one unit [formula in source] was fixed on a single reference and every other scale in the block followed fit-free from the ratio law [formula in source] (Paper V1.06, App. C). These block assignments are the place where the proton mass, the EW masses and the CMB temperature lived. The honest question is: has the new compiler re-derived each of these,

Explicit source references:

- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)

## What is new, what is old, what stays open

[documents/tfpt_3_e8_audit_bootstrap/sections/010-section-three-views-of-one-spine.tex:113-145](../../../../documents/tfpt_3_e8_audit_bootstrap/sections/010-section-three-views-of-one-spine.tex#L113) · `section:200db589cdbff42f04e6` · section

The flavor selector [formula in source] is the terminal orbit of the [formula in source] cascade; the compiler is the cascade's IR endpoint. The atlas branching blocks ( [formula in source] ) are the cascade's UV head ( [formula in source] ); the secondary atlas and the orbit cascade are the same spine read top-down vs.\ as subalgebras. The anchor power sums sit on doubled-exponent rungs: [formula in source] ( [formu

## Appendix: computational verification

[documents/tfpt_3_e8_audit_bootstrap/sections/014-section-the-honest-open-items-list.tex:158-173](../../../../documents/tfpt_3_e8_audit_bootstrap/sections/014-section-the-honest-open-items-list.tex#L158) · `section:625a244079dc7ffc20ed` · section

The audit/bridge identities of this document (marked , ) are re-derived from [formula in source] and machine-checked by the suite in the repository folder verification/; the inline tags [verification/ [formula in source] ] point to the exact script. Relevant here: v1_e8_glue.py — the [formula in source] glue [formula in source] (load-bearing). v4_flavor_matrix.py — the spectral selector [formula in source] , minors [

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_file_citation
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation
- [verification/README.md](../../../../verification/README.md#L1) · explicit_file_citation
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## -1.2cm TFPT — Frontier items\\[2mm] [formula in source] , [formula in source] , the Koide relation, dark matter and quantum gravity —\\ the honest status, not forced onto the ladder

[documents/tfpt_4_frontier/preamble.tex:1-37](../../../../documents/tfpt_4_frontier/preamble.tex#L1) · `section:e04339a135a123052daa` · frontmatter

-1.2cm TFPT — Frontier items\\[2mm] [formula in source] , [formula in source] , the Koide relation, dark matter and quantum gravity —\\ the honest status, not forced onto the ladder

## Front matter / support

[documents/tfpt_4_frontier/sections/001-source.tex:1-90](../../../../documents/tfpt_4_frontier/sections/001-source.tex#L1) · `section:fbc55d19f88e095d54eb` · frontmatter

The honest frontier: which physics has a genuine TFPT handle and which does not. For each of [formula in source] , [formula in source] , the Koide relation, dark matter and full quantum gravity, this note states the genuine structural handle, the precision with which it currently lands, and — crucially — what is not a clean compiler power and is deliberately not forced onto the ladder. This document is the status aut

Explicit source references:

- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation
- [CONTRACT.F.01](../../../../verification/status_ledger.csv#L302) · explicit_claim_identifier · original status at linked ledger row
- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier
- [verification/v211_axion_spine_angle.py](../../../../verification/v211_axion_spine_angle.py#L1) · explicit_script_identifier
- [FTRANSFER.SUITE.01](../../../../verification/status_ledger.csv#L472) · explicit_claim_identifier · original status at linked ledger row
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_file_citation
- [verification/v402_ftransfer_suite.py](../../../../verification/v402_ftransfer_suite.py#L1) · explicit_file_citation
- [verification/v35_quark_qcd_boundary.py](../../../../verification/v35_quark_qcd_boundary.py#L1) · explicit_file_citation
- [verification/v792_ftransfer_kms_coset.py](../../../../verification/v792_ftransfer_kms_coset.py#L1) · explicit_file_citation
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_script_identifier
- [verification/v188_frontier_wording_guard.py](../../../../verification/v188_frontier_wording_guard.py#L1) · explicit_file_citation
- [verification/v212_leptogenesis_decuple.py](../../../../verification/v212_leptogenesis_decuple.py#L1) · explicit_script_identifier
- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v213_ftransfer_functor.py](../../../../verification/v213_ftransfer_functor.py#L1) · explicit_file_citation
- [verification/v777_ftransfer_clock_jets.py](../../../../verification/v777_ftransfer_clock_jets.py#L1) · explicit_file_citation
- [verification/v397_external_clock_probe.py](../../../../verification/v397_external_clock_probe.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)

## Route B — leptogenesis interface ( ).

[documents/tfpt_4_frontier/sections/001-source.tex:110-188](../../../../documents/tfpt_4_frontier/sections/001-source.tex#L110) · `section:d0c4725137a9427c8a0b` · paragraph

The TFPT branch fixes the neutrino spectrum, the CP phase structure ( [formula in source] , [formula in source] , both closed) and a plausible washout anchor [formula in source] meV. The heavy-mass input, however, remains scenario-level: [formula in source] is viable but does not close [formula in source] — [formula in source] is the seesaw scale [formula in source] , not a compiler power, so the relation relocates t

Explicit source references:

- [verification/v212_leptogenesis_decuple.py](../../../../verification/v212_leptogenesis_decuple.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.06](../../../../verification/status_ledger.csv#L765) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1001_nu_pentagon_chain.py](../../../../verification/v1001_nu_pentagon_chain.py#L1) · explicit_file_citation
- [experiments/ftransfer/leptogenesis_boltzmann/fboltzmann_solve.py](../../../../experiments/ftransfer/leptogenesis_boltzmann/fboltzmann_solve.py#L1) · explicit_file_citation
- [verification/v986_nu_scalaron_rung.py](../../../../verification/v986_nu_scalaron_rung.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_file_citation
- [verification/v169_etaB_boltzmann_interface.py](../../../../verification/v169_etaB_boltzmann_interface.py#L1) · explicit_file_citation

## Proton/electron ratio [formula in source] — a cross-sector ratio

[documents/tfpt_4_frontier/sections/001-source.tex:189-261](../../../../documents/tfpt_4_frontier/sections/001-source.tex#L189) · `section:2805350687457d7649bf` · section

[formula in source] is closed on the [formula in source] -ladder ( [formula in source] ). The proton mass is not a Yukawa: it is QCD-dominated, [formula in source] a few [formula in source] , and [formula in source] arises by dimensional transmutation from [formula in source] running (scheme level). Hence [formula in source] mixes two different sectors. It is no single [formula in source] power: [formula in source] a

Explicit source references:

- [FR.MPME.02](../../../../verification/status_ledger.csv#L348) · explicit_claim_identifier · original status at linked ledger row
- [verification/v79_review_identities.py](../../../../verification/v79_review_identities.py#L1) · explicit_file_citation
- [verification/v262_fqcd_mp_me.py](../../../../verification/v262_fqcd_mp_me.py#L1) · explicit_script_identifier
- [verification/v723_phys_modular_clock.py](../../../../verification/v723_phys_modular_clock.py#L1) · explicit_file_citation
- [verification/v725_phys_vgeo_torsor_audit.py](../../../../verification/v725_phys_vgeo_torsor_audit.py#L1) · explicit_file_citation
- [verification/v339_firstprinciples_boundary.py](../../../../verification/v339_firstprinciples_boundary.py#L1) · explicit_file_citation
- [verification/v35_quark_qcd_boundary.py](../../../../verification/v35_quark_qcd_boundary.py#L1) · explicit_script_identifier
- [FR.MPME.01](../../../../verification/status_ledger.csv#L49) · explicit_claim_identifier · original status at linked ledger row
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v274_scale_overdetermination.py](../../../../verification/v274_scale_overdetermination.py#L1) · explicit_script_identifier
- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_file_citation
- [verification/v246_unification_data_crosscheck.py](../../../../verification/v246_unification_data_crosscheck.py#L1) · explicit_script_identifier
- [verification/v724_phys_t3b_modular_flows.py](../../../../verification/v724_phys_t3b_modular_flows.py#L1) · explicit_file_citation
- [verification/v164_qcd_scale.py](../../../../verification/v164_qcd_scale.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [(* ---- (v79) hypercharge Lucas-Binet D_n + the quark-ratio reading ---- *) checkExact["Lucas-Binet D_n=(3^n-(-2)^n)/5 = {1,1,7,13,55,133}; c_u/c_d = D_5/(N_fam^2 D_4) = 55/117", Module[{D}, D = Table[(3^n - (-2)^n)/5, {n, 1, 6}]; D == {1, 1, 7, 13, 55, 133} && D[[5]]/(Nfam^2 D[[4]]) == 55/117]]; (* ---- (v79) Inverse Anchor Theorem: 1^T M^-1 1 = 1/atom; a^T M^-1 a = 1 for R,K,L ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L385)

## The Koide relation — near [formula in source] , computed exactly

[documents/tfpt_4_frontier/sections/002-source.tex:1-154](../../../../documents/tfpt_4_frontier/sections/002-source.tex#L1) · `section:eb0ad9c39f3387e3dcf3` · section

With the closed lepton source masses [formula in source] the Koide ratio is a pure number (the common prefactor cancels): [formula in source] The measured pole-mass value is famously [formula in source] . So TFPT predicts a Koide ratio that is near [formula in source] but not exactly [formula in source] at source level.

Explicit source references:

- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_file_citation
- [verification/v420_fpole_qed_running.py](../../../../verification/v420_fpole_qed_running.py#L1) · explicit_file_citation
- [verification/v25_frontier_conjectures.py](../../../../verification/v25_frontier_conjectures.py#L1) · explicit_file_citation
- [verification/v93_koide_relaxation_toy.py](../../../../verification/v93_koide_relaxation_toy.py#L1) · explicit_script_identifier
- [verification/v80_operator_pencil_geometry.py](../../../../verification/v80_operator_pencil_geometry.py#L1) · explicit_script_identifier
- [verification/v99_koide_flow_time.py](../../../../verification/v99_koide_flow_time.py#L1) · explicit_file_citation
- [verification/v37_plucker_anchor.py](../../../../verification/v37_plucker_anchor.py#L1) · explicit_file_citation
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier
- [FR.KOIDE.06](../../../../verification/status_ledger.csv#L177) · explicit_claim_identifier · original status at linked ledger row
- [verification/v327_hypergraph_rewrite.py](../../../../verification/v327_hypergraph_rewrite.py#L1) · explicit_script_identifier
- [FR.KOIDE.05](../../../../verification/status_ledger.csv#L167) · explicit_claim_identifier · original status at linked ledger row
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)
- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)
- [(* v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1} *) M = {{1, 0, 0}, {0, 1/3, 1/3}, {0, 1/3, 1/3}}; evs = Sort[Eigenvalues[M]]; checkExact["v327 HYP.REWRITE.01: the minimal 3-channel/1-absorbing rewrite M has spectrum {0,2/3,1}; the recovery survival 2/3 = (Nfam-1)/Nfam = |Z2|/Nfam emerges from the rule arity, and over the order-6 = 2 Nfam hand (2/3)^(2 Nfam) = 64/729 = the recovery gap", evs == {0, 2/3, 1} && 2/3 == (Nfam - 1)/Nfam && (2/3)^(2 Nfam) == 64/729]; (* v327 NON-GRAPH-SPECTRAL: 2/3 is NOT a root of the affine-E8 charpoly (sharpens v312) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2227)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [(* ---- (v37) anchor-plane Plücker apparatus + K+xQ pencil + dualities ---- *) oneV = {1, 1, 1}; aVc = {1, 1, 2}; plLeft[Mat_] := Module[{r1 = oneV.Mat, r2 = aVc.Mat}, {r1[[1]] r2[[2]] - r1[[2]] r2[[1]], r1[[1]] r2[[3]] - r1[[3]] r2[[1]], r1[[2]] r2[[3]] - r1[[3]] r2[[2]]}]; plRight[Mat_] := Module[{c1 = Mat.oneV, c2 = Mat.aVc}, {c1[[1]] c2[[2]] - c1[[2]] c2[[1]], c1[[1]] c2[[3]] - c1[[3]] c2[[1]], c1[[2]] c2[[3]] - c1[[3]] c2[[2]]}]; checkExact["Pl(K) = (-1,6,4) and ||Pl(K)||_1 = 11 (the '11' localised in K)", plLeft[K] == {-1, 6, 4} && Total[Abs[plLeft[K]]] == 11]; checkExact["Pl_R(K)=(12,12,-2), ||Pl_R(K)||_1=26; sum Pl_R(L)=60 (cascade start)", plRight[K] == {12, 12, -2} && Total[Abs[plRight[K]]] == 26 && Total[plRight[L]] == 60]; checkExact["pencil det(K + x Q) = 3x^3 + 7x^2 + 6x + 4 = (N_fam,7,|R+A3|,|mu4|)", Expand[Det[K + x Q]] === 3 x^3 + 7 x^2 + 6 x + 4]; checkExact["lepton-up duality: K_e - K_u = a = (1,1,2)", K[[3]] - K[[1]] == {1, 1, 2}]; checkExact["lepton-up duality: L_e - L_u = Exp(A3) = (1,2,3)", L[[3]] - L[[1]] == {1, 2, 3}]; checkExact["lepton ring: c_e c_tau = |Z2| c_mu (= 8/3)", ce ctau == 2 cmu]; (* ---- (v39) (U_wall) selectors read off the bundle (algebraic) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L122)
- [(* ---- (v80) operator-pencil geometry: anchor singularity + block-det type checker + F4xG2 shadow ---- *) checkExact["anchor singularity: det B(K+xQ)=(3x+2)(3x+5); type checker det B = (9,10,16,40) for (Q,K,R,L)", Module[{one = {1, 1, 1}, av = {1, 1, 2}, bb, dbx}, bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}}; dbx = Det[bb[K + xx*Q]]; (Factor[dbx] == (3 xx + 2) (3 xx + 5)) && (Det[bb[Q]] == 9) && (Det[bb[K]] == 10) && (Det[bb[R]] == 16) && (Det[bb[L]] == 40)]]; checkExact["F4xG2 shadow: det B_{R+Q}=52=dim F4; 248 = 52 + 14 + 26*7 (real E8->F4xG2 branching)", Module[{one = {1, 1, 1}, av = {1, 1, 2}, F = R + Q, bb}, bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}}; (Det[bb[F]] == 52) && (52 + 14 + 26*7 == 248)]]; (* ---- (v81) double cover: det B(K+xQ) quadratic, branch points {-2/3,-5/3}, disc=81=N_fam^4 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L397)
- [(* ==== v325/v327: the keystone pillowcase orbifold + the cusp-weight rewrite (exact) ==== *) Module[{chiOrb, M, evs, edges, cAff, x, p23}, (* v325 QGEO.KEYSTONE.01: the flat pillowcase orbifold S^2(2,2,2,2) has chi_orb = 0 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2220)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)

## Target F — the perturbative 4D-QFT [formula in source] scale round (v269–v275)

[documents/tfpt_5_redteam/sections/001-section-method.tex:186-266](../../../../documents/tfpt_5_redteam/sections/001-section-method.tex#L186) · `section:c00f76407fefd9782fd7` · section

Minimal claim. The round published in release 5.2 — the Epstein–Glaser [formula in source] layer ( v269/ v271/ v273), the PMNS Jarlskog CP strength ( v270), the absolute [formula in source] -scale typing ( v272), the scale over-determination ( v274) and the QG.AMB.01 roadmap ( v275). redteam/rt_F_qft4d.py

Explicit source references:

- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/redteam/rt_F_qft4d.py](../../../../verification/redteam/rt_F_qft4d.py#L1) · explicit_file_citation
- [GRAV.KMS.HESSIAN.01](../../../../verification/status_ledger.csv#L93) · explicit_claim_identifier · original status at linked ledger row
- [verification/v335_seam_equiv_unify.py](../../../../verification/v335_seam_equiv_unify.py#L1) · explicit_script_identifier
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_script_identifier
- [verification/v481_seesaw_carrier_ladder.py](../../../../verification/v481_seesaw_carrier_ladder.py#L1) · explicit_script_identifier
- [verification/v385_uvbranch_killtest.py](../../../../verification/v385_uvbranch_killtest.py#L1) · explicit_file_citation
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [LAMBDA.BRANCH.01](../../../../verification/status_ledger.csv#L129) · explicit_claim_identifier · original status at linked ledger row
- [verification/v265_qft4d_fork_freeze.py](../../../../verification/v265_qft4d_fork_freeze.py#L1) · explicit_script_identifier
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_script_identifier
- [verification/v482_seesaw_rung_decision.py](../../../../verification/v482_seesaw_rung_decision.py#L1) · explicit_script_identifier
- [verification/v272_nu_mass_scale.py](../../../../verification/v272_nu_mass_scale.py#L1) · explicit_script_identifier
- [verification/v274_scale_overdetermination.py](../../../../verification/v274_scale_overdetermination.py#L1) · explicit_script_identifier
- [QFT4D.EG.ALLORDER.01](../../../../verification/status_ledger.csv#L444) · explicit_claim_identifier · original status at linked ledger row
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v271_eg_oneloop_quartic.py](../../../../verification/v271_eg_oneloop_quartic.py#L1) · explicit_script_identifier
- [verification/v275_qgamb_roadmap.py](../../../../verification/v275_qgamb_roadmap.py#L1) · explicit_script_identifier
- [GRAV.SPIN2.UNITARITY.01](../../../../verification/status_ledger.csv#L80) · explicit_claim_identifier · original status at linked ledger row
- [verification/v269_spert_paqft_skeleton.py](../../../../verification/v269_spert_paqft_skeleton.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [QGAMB.IDG.01](../../../../verification/status_ledger.csv#L400) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v334_conformal_resolution.py](../../../../verification/v334_conformal_resolution.py#L1) · explicit_script_identifier
- [verification/v273_eg_gauge_running.py](../../../../verification/v273_eg_gauge_running.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ==== v273: EG one-loop gauge self-energy -> (b1,b2,b3) (QFT4D.SPERT.03) ==== v272 (nu-scale, numerical) + v274 (over-determination, numerical) + v275 (QG roadmap) are Python-only; v273's exact one-loop beta coefficients from the content are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2102)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)

## Front matter / support

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/001-section-korrektur-der-suchrichtung-am-29-september.tex:1-23](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/001-section-korrektur-der-suchrichtung-am-29-september.tex#L1) · `section:1e9042b9ed5880e04858` · frontmatter

13mm teal TFPT / Universalraum / Prozess und Physik 16mm navy Die gemeinsame Quelle 5mm und der Weg zur Gesamtlösung 13mm Gesamtsynthese der Sitzung vom 28. September 2026\ bis zum 30. September 2026 8mm Das Ganze: ein Ursprung, mehrere gekoppelte Antworten. TFPT besitzt bereits konkrete Herleitungsketten für Quellenmassen, Yukawa-Hierarchien, Mischungen und [formula in source] sowie bedingte Neutrino-, Gravitations-

## Der Mikrounterbau ist weiter geschlossen als zuvor ausgewiesen

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/002-subsection-der-entscheidende-selektor-vollst-ndigkeit-de.tex:174-258](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/002-subsection-der-entscheidende-selektor-vollst-ndigkeit-de.tex#L174) · `section:8ccfe1dd89183bdd87e8` · subsection

Die erneute Quellenprüfung korrigiert eine zu schwache Darstellung des vorhandenen Bestands. Der Vertrag microscopic-neutral-limit beweist für den unveränderten QWZ-Kragen mit Breite acht, Masse eins, Holonomiesektor [formula in source] , tatsächlichem gefülltem negativem Spektrum und Filterbreite [formula in source] bereits [formula in source] Dies ist der analytische Vergleich der vollständigen bewegten Geschichte,

## Was als vollständige Lösung zählen würde

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex:6-10](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex#L6) · `section:d7bed9da952b67b42a66` · subsection

Eine Lösung muss zugleich die vollständige Quelle aus den ursprünglichen Bedingungen auswählen, ihre gemeinsame Wirkungs- und Zustandsregel konstruieren und die vorhandenen physikalischen Auslesungen in einer konsistenten lokalen Raumzeit realisieren. Dabei müssen auch Kopplungen, Neutrinosektor, Gravitation und kosmologische Anfangs-/Transferbedingungen am selben Objekt hängen. Ein metrologischer Maßstab darf ausdrü

Explicit source references:

- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row

## Die verzahnten Clocks, Flavor und [formula in source] im Gesamtgefüge

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex:100-101](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex#L100) · `section:38a70245f636d0b354c2` · section

No opening prose excerpt; see the source.

## Die bereits vorhandene physikalische Herleitungskette

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex:115-132](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex#L115) · `section:f5188df5e6a05ddf62a8` · subsection

Die Aussage ``Massen, Flavor, Yukawa und [formula in source] müssen noch hergeleitet werden'' war zu pauschal. Die Originale enthalten konkrete Formeln, Operatoren und Begründungen. Die präzise Frage lautet: Realisiert ein und derselbe ursprüngliche Quellprozess diese vorhandenen Gesetze mit denselben Markierungen, Normierungen und Zuständen?

## Massen und Yukawa-Kopplungen aus derselben markierten Struktur

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex:133-192](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex#L133) · `section:db553f90608e785ea4a8` · subsection

Mit Zeilen [formula in source] lauten die ursprünglichen Operatoren beziehungsweise markierten Auslesetabellen Es gilt [formula in source] , [formula in source] und [formula in source] . Der Seed und das gemeinsame Yukawa-Gesetz sind Hüte kennzeichnen die Quellenwerte. Die Standard-RG-/Schwellenabbildung zu laufenden oder Polmassen ist ein eigener, benannter Rechenschritt. Sie macht die Quellenherleitung nicht wertlo

Explicit source references:

- [FLAV.RIGID.01](../../../../verification/status_ledger.csv#L67) · explicit_claim_identifier · original status at linked ledger row
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_script_identifier
- [verification/v118_hexagon_family_dictionary.py](../../../../verification/v118_hexagon_family_dictionary.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)

## Warum [formula in source] , [formula in source] und [formula in source] eine gemeinsame Einschränkung sind

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex:193-228](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex#L193) · `section:e7f00fa0a0e13367f31d` · subsection

Die Kopplung zwischen den beiden Herleitungswegen ist genauer als eine Zahlenähnlichkeit. Auf einer ursprünglichen Familie gilt Ungewichtet ergeben die drei Familien den Punkturnachtrag [formula in source] . Mit Fermion-/Skalargewicht und Eichnormierung folgt dagegen Der Higgs trägt den letzten Beitrag bei. Ein ungeladenes rechtshändiges Neutrino trägt nicht zur [formula in source] -Spur bei, gehört aber zum ungewich

Explicit source references:

- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row

## Der Flavor-Determinant und die Eichspur aus gemeinsamen Ladungsdaten

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex:229-317](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/003-subsection-wo-die-ergebnisse-der-sitzung-in-dieses-bild-.tex#L229) · `section:0cf51a01f0489758a3da` · subsection

Der ursprüngliche Flavorpol ist bereits aus einer gemeinsamen Wirkung hergeleitet. Die heutige Verbindung erklärt ihre genaue Einsetzung mit denselben [formula in source] -Ladungsdaten und dem vorhandenen gedoppelten Familienweg. Entscheidend sind die Art der Projektion und die Art der Spur.

Explicit source references:

- [tfpt_explorer/source_charge_response.py](../../../../tfpt_explorer/source_charge_response.py#L1) · explicit_file_citation

## Der gemeinsame Operator ist im Original bereits präzise vorgegeben

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex:34-46](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex#L34) · `section:710a570bea7ab5171bf0` · subsection

Der Flavoransatz schreibt tatsächlich auf dem zulässigen, invertierbaren Projektionsraum. Der Transportpol wird über das ursprüngliche Determinantenfunktional von [formula in source] bestimmt. Für die neue Quelle ist deshalb die konkrete Gleichheit [formula in source] mit denselben Familienlegs, [formula in source] -Gradierungen und derselben Norm zu zeigen. Die neue E8-Quelle enthält nicht automatisch die Flavorhier

## Neutrinos: Die vorhandenen Herleitungen gemeinsam lösen

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex:47-172](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex#L47) · `section:3ededccfeac789055af3` · subsection

Der Originalbestand liefert einen endlichen Diracoperator mit Dirac- und Majoranablock, den tatsächlichen Seesaw-Ausdruck und konkrete PMNS-Kanäle. Auf dem ursprünglichen Zweig stehen unter anderem [formula in source] , [formula in source] und die hexagonale Phasenlesart [formula in source] . Der spätere Pentagonzweig aus FLAV.NUSCALE.06 benutzt dagegen eine andere Mischung und Phase; er ist ein ausdrücklich bedingte

Explicit source references:

- [experiments/ftransfer/leptogenesis_boltzmann/fboltzmann_solve.py](../../../../experiments/ftransfer/leptogenesis_boltzmann/fboltzmann_solve.py#L1) · explicit_file_citation
- [experiments/theory-contracts/nu02_transport_selector.py](../../../../experiments/theory-contracts/nu02_transport_selector.py#L1) · explicit_file_citation
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [experiments/theory-contracts/nu01_casas_ibarra_seam.py](../../../../experiments/theory-contracts/nu01_casas_ibarra_seam.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.06](../../../../verification/status_ledger.csv#L765) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## Nachweise der erneuten Prüfung

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex:173-177](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex#L173) · `section:7779d02d30f1856735de` · subsection

Die Originalkennungen sind insbesondere FLAV.LEPTONC.01, FLAV.RIGID.01/02, FLAV.CKM.01, FLAV.PMNS.02, FLAV.NUSCALE.05/06, EM.WARD.01 und ALPHA.QUILLEN.EXACT.01. Neu ausgeführt wurden v20 (12/12), v71 (7/7), v118 (6/6), v88 (11/11), v3 (14/14) und v485 (5/5); diese Läufe prüfen ihre angegebenen Formeln und Operatorrechnungen. Eine neue Ausführung der gesamten Lean- oder Repository-Suite wird damit nicht behauptet.

Explicit source references:

- [verification/v20_lepton_c_derivation.py](../../../../verification/v20_lepton_c_derivation.py#L1) · explicit_script_identifier
- [FLAV.CKM.01](../../../../verification/status_ledger.csv#L37) · explicit_claim_identifier · original status at linked ledger row
- [verification/v485_contact_diagonal_closed.py](../../../../verification/v485_contact_diagonal_closed.py#L1) · explicit_script_identifier
- [FLAV.LEPTONC.01](../../../../verification/status_ledger.csv#L22) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.PMNS.02](../../../../verification/status_ledger.csv#L349) · explicit_claim_identifier · original status at linked ledger row
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier
- [experiments/theory-contracts/source-flavor-joint-dictionary-20260921/PROOF.md](../../../../experiments/theory-contracts/source-flavor-joint-dictionary-20260921/PROOF.md#L1) · explicit_file_citation
- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_script_identifier
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [EM.WARD.01](../../../../verification/status_ledger.csv#L70) · explicit_claim_identifier · original status at linked ledger row
- [verification/v118_hexagon_family_dictionary.py](../../../../verification/v118_hexagon_family_dictionary.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [FLAV.RIGID.01](../../../../verification/status_ledger.csv#L67) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)

## Fortsetzung: Der gemeinsame Flavor- und Nahtanschluss

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex:178-182](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex#L178) · `section:7f0a334934c934f50714` · section

Die gemeinsame Verbindung ist konkreter geworden. Das ursprüngliche Fuchssystem liefert jetzt einen wirklichen Wegoperator, der exakt zum bereits verwendeten Sechsertransport äquivalent ist. Auf der anderen Seite liefert die ursprüngliche E8-Quelle eine konkrete neutrale Anregung mit Gewicht zwei und Normquadrat 48. Die gemeinsame Aufgabe ist dadurch keine Suche nach irgendeiner passenden Matrix mehr: Es ist die Herl

## Der ganze endliche Operator besitzt bereits ein gemeinsames Wörterbuch

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex:183-202](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/004-subsection-auch-die-skalen-besitzen-einen-gemeinsamen-va.tex#L183) · `section:7462e3e53c3e50ebcad8` · subsection

Der Originalvertrag source-native-clock-flavor-bridge-20260922/PROOF.md liefert eine feste invertierbare Matrix [formula in source] mit [formula in source] ist die dort ausgewählte positive Familienform, [formula in source] der ganzzahlige Dreierzyklus, [formula in source] die Familienmonodromie und [formula in source] die Vierteldrehung. Die Orientierungsgerade ist in [formula in source] ausdrücklich mitgeführt. Für

Explicit source references:

- [experiments/theory-contracts/source-native-clock-flavor-bridge-20260922/PROOF.md](../../../../experiments/theory-contracts/source-native-clock-flavor-bridge-20260922/PROOF.md#L1) · explicit_file_citation

## Eine explizite gemeinsame Klasse von Randoperatoren

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/005-subsection-die-urspr-ngliche-determinantenlinie-tr-gt-be.tex:33-70](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/005-subsection-die-urspr-ngliche-determinantenlinie-tr-gt-be.tex#L33) · `section:f4ce3ea37f533d15c463` · subsection

Die endliche Flavorgram-Matrix besitzt außerdem eine genaue Darstellung als Dirichlet-zu-Neumann-Antwort. Für [formula in source] , [formula in source] , einen zyklischen Shift [formula in source] und ist der Sprungoperator von [formula in source] auf den [formula in source] Kreisintervallen Die Gleichheit folgt durch Einsetzen von [formula in source] . Sie identifiziert eine Operatorfamilie; die Interpretation des i

## Flavor und neutrale Quelle besitzen bereits eine gemeinsame berechnete Antwort

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/005-subsection-die-urspr-ngliche-determinantenlinie-tr-gt-be.tex:189-221](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/005-subsection-die-urspr-ngliche-determinantenlinie-tr-gt-be.tex#L189) · `section:ce7e00748b1472c65dca` · subsection

Der neue Kandidat lässt sich unmittelbar am ursprünglichen Flavor-Hintergrund prüfen. Dafür wird die normierte Riemann–Hilbert-Defektantwort derselben drei komplexen Familienfermionen verwendet, mit den ursprünglichen Residuen und dem vorgeschriebenen ausgehenden Sektor. In dieser Darstellung liefern die Fermionen-Wardidentitäten Die symmetrische Stressdefinition entfernt den Ableitungsterm; der verbundene [formula i

## Die vollständige neutrale Antwort im ursprünglichen Flavorprozess

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/005-subsection-die-urspr-ngliche-determinantenlinie-tr-gt-be.tex:222-300](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/005-subsection-die-urspr-ngliche-determinantenlinie-tr-gt-be.tex#L222) · `section:0cfe9479b259eaa3ab37` · subsection

Die gemeinsame Einpunktantwort bestimmt bereits einen Teil der Verträglichkeit. Der vollständige verbundene Zweipunktkern liefert nun die tatsächliche Antwort zwischen zwei verschiedenen Einsetzungsorten. Entscheidend ist die unveränderte Feldkonvention des ursprünglichen Fuchs- und Riemann–Hilbert-Systems: [formula in source] Im normierten quasifreien Riemann–Hilbert-Defektmatrixelement folgt aus symmetrischer Fermi

Explicit source references:

- [tfpt_explorer/source_flavor_correlator.py](../../../../tfpt_explorer/source_flavor_correlator.py#L1) · explicit_file_citation

## Ausführbare Nachweise dieser Fortsetzung

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex:119-123](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex#L119) · `section:e7294e8d8a250400195d` · subsection

tfpt_explorer/flavor_path_transport.py integriert die ursprüngliche Verbindung entlang beider Halbwege und unabhängig entlang des geschlossenen Kreises. Es berechnet die Determinantenwindung aus den integrierten Lösungen und vergleicht die vollständigen endlichen Greenmatrizen. tfpt_explorer/neutral_source_response.py benutzt die ursprünglichen E8-Wurzeln, ihre Stressmomentmatrizen und den tatsächlichen Heisenbergzus

Explicit source references:

- [verification/v117_monodromy_weyl_a3.py](../../../../verification/v117_monodromy_weyl_a3.py#L1) · explicit_file_citation
- [tfpt_explorer/neutral_source_response.py](../../../../tfpt_explorer/neutral_source_response.py#L1) · explicit_file_citation
- [verification/v118_hexagon_family_dictionary.py](../../../../verification/v118_hexagon_family_dictionary.py#L1) · explicit_file_citation
- [experiments/theory-contracts/matter-geometry-round15/PROOF.md](../../../../experiments/theory-contracts/matter-geometry-round15/PROOF.md#L1) · explicit_file_citation
- [verification/v498_celestial_wp5b_singular_vector.py](../../../../verification/v498_celestial_wp5b_singular_vector.py#L1) · explicit_file_citation
- [tfpt_explorer/flavor_path_transport.py](../../../../tfpt_explorer/flavor_path_transport.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)
- [(* ---- (v117) monodromy = W(A3) ---- The [N] ODE identification (scipy monodromy of the exact A0* system) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L713)
- [(* ==== v498 round: CELEST.WP5B.01 -- WP5b of CELEST.SEAM.01, "the singular vector as an operator" (the deleting object of the v497 null ideal made explicit). Exact content mirrored: (i) the case classification of the J^a_1 condition over the 248-element basis (190/57/1, exactly one case sees the level k) from the standard E8 root data + the theta-grading (1,56,134,56,1); (ii) the LEVEL DIAL derived from the affine sl2 commutation -- F^theta_1 (E^theta_{-1})^n|0> = n(k-n+1) (E_{-1})^{n-1}|0>, square coefficient 2(k-1) = -2(1-k) with values (-2,0,2) at k = 0,1,2, Shapovalov 2k(k-1) (0 at k = 1, 4 at k = 2), cube singular exactly at k = 2; (iii) the glue frame -- 240 roots with classes (52,64,60,64), inner grading <r,h> = class mod 4 on all 240, theta_glue = argmax with <theta,h> = 5 => j(theta) = 1, clock phase i^(2j) = -1, cross-table rows (1,56,126,56,1); (iv) multiplicity 1 of weight 2 theta in the level-2 Fock (U(g)|s> is THE 27000 = 30^3), lattice reading (2t,2t)/2 = 4 > 2, and the comark discriminator (E8 comarks all >= 2 -- vacuum the only level-1 primary; D8 has three comark-1 weights with h = (1/2,1,1)); (v) the twisted-slot tension (two sector-C_1 modes never sum to 8 quarters, minimum 6 = q^(3/2)) + the per-period 248. The full Chevalley/PBW singularity run (J^a_1|s> = 0 on all 248 basis elements, engine unit tests on all 61504 pairs) is Python-side (v498 S1-S3); the counting/dial/grading consequences are what is mirrored here. Mirrors v498. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3463)
- [(* ==== v500 round: CELEST.WP5C.01 -- WP5c of CELEST.SEAM.01, "the GNS limit state" (the state whose GNS kernel contains the v497/v498 null ideal). Exact content mirrored: (i) the LEVEL-2 BLOCK CENSUS from the standard E8 root data -- 31124 = 248 + 30876 monomials in 9361 weight blocks with dim profile {164:1, 37:240, 7:2160, 1:6960}, orbit census by lattice norm (8,6,4,2,0) -> (240, 6720, 2160, 240, 1) with constant block dims (1,1,7,37,164); (ii) the RANK/KERNEL ARITHMETIC of the full Gram -- rank table per orbit (0,0,1,8,44) (the Python-side Gram result) gives total rank 4124 = 1 + 248 + 3875 = chi_2 (dim V(omega) = 3875 recomputed by Weyl from the dominant norm-4 weight) and kernel per orbit (1,1,6,29,120) summing to 27000 = 30^3 = dim V(2 theta) (Weyl); (iii) the CLOCK-CLASS SPLIT at the state level -- the same census in the glue frame with class(lambda) = <lambda,h> mod 4 turns the rank table into the split (1036,1024,1040,1024) = Theta_Cj/eta^8 at q^2, and level 1 gives (52+8,64,60,64) = (60,64,60,64); (iv) the THRESHOLD + LEVEL-DIAL + D8 arithmetic -- x-adic order w*r >= N+1 for all r >= 1 iff w >= N+1 (sharp at w = N via r = 1), level-1 root-mode norm = k (no 248 layer at k = 0), <s|s> = 2k(k-1) (0 at k = 1, +4 at k = 2), D8 census 7380 = 120 + 7260 in 2705 blocks with quotient 7380 - 5304 = 2076. The exact Gram computation itself (9361 blocks over Fractions, PSD inertia, the highest-weight norms (3844, 49, 2, 0), the contravariance and anti-involution machine checks on 61504 pairs) is Python-side (v500 S1-S4). Mirrors v500. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3709)

## Die Windung wirkt auf der ganzen Quelle: neuer Anschluss und gemeinsamer Massentest

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex:124-130](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex#L124) · `section:dd6ae75f0a051dc057b2` · section

Der neue positive Herkunftssatz: Die primitive Determinantenwindung des ursprünglichen Flavorprozesses bestimmt beim internen Spin-Lift ein zusätzliches Minuszeichen. In der vorhandenen E8-Verklebung ist dieses Zeichen genau die Involution, die den 120er-Tensorsektor vom 128er-Spinorsektor unterscheidet. Damit ist ein Sechserumlauf auf tatsächlichen geladenen Quellenfeldern konstruiert. Die Identifikation dieses inne

## Der ganze Massensektor entscheidet über die neue Zusatzannahme

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex:201-223](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex#L201) · `section:62da8d57db3260c78314` · subsection

Eine gemeinsame Lösung muss dieselbe Symmetrie auch auf den bereits verwendeten Higgs- und Neutrinofeldern realisieren. Das ursprüngliche Standardmodell-Paper benutzt, weil ein elementares [formula in source] im erklärten Hull fehlt, den Einsatz Quelle: tfpt_2_standard_model.tex, Zeilen 2003–2006, und verification/v488_majorana_clebsch_door.py. Unter einer gewöhnlichen internen [formula in source] ist der Einsatz neu

Explicit source references:

- [verification/v488_majorana_clebsch_door.py](../../../../verification/v488_majorana_clebsch_door.py#L1) · explicit_file_citation

## Der symmetrische Paartransport schließt an den ursprünglichen Flavorweg an

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex:274-309](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex#L274) · `section:af381de775ce2041dbf4` · subsection

Der benutzte Spinlift wirkt auf Sein symmetrischer Familienpaarraum zerfällt daher als [formula in source] ; der konjugierte Kanal enthält [formula in source] . Der Sechserraum ist der Raum symmetrischer Matrizen für drei Familien. Seine Komponenten sind noch keine bestimmten Erwartungswerte.

## Der neutrale Alpha-Kandidat antwortet auf diesen Neutrinokanal

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex:310-331](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/006-subsection-die-48-und-die-41-sind-zwei-antworten-derselb.tex#L310) · `section:1b4dc6009cb25792e1b9` · subsection

Die neue Paarstruktur kann mit dem bereits bestimmten neutralen Feld [formula in source] in derselben Quelle geprüft werden. Verwende dieselbe Auswahl, in der [formula in source] der ausgelassene Familien-Singulettzugang und [formula in source] der Dreieranteil sind. Für einen reinen normierten Gitterzustand [formula in source] gilt mit der ursprünglichen Matrix [formula in source] Der symmetrische Paarzustand [formu

## Die vollständige Neutrinomatrix besitzt ein norm- und phasentreues Quellenwörterbuch

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:1-47](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L1) · `section:59b50548b2eacea6e329` · subsection

Die vorhandenen Neutrinoherleitungen liefern ganze komplexe Matrizen. Ihr Quellenanschluss darf sich deshalb nicht auf Massen, Spur oder Norm beschränken. Der bereits konstruierte symmetrische Sechserraum hat genau die dafür benötigte bilineare Struktur. Für eine komplex-symmetrische Koeffizientenmatrix [formula in source] sei Die 36 ursprünglichen affinen Paarungen ergeben Dabei haben diagonale Paare Normquadrat ein

## Schwere und leichte Neutrinos bleiben verschiedene physische Felder.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:48-81](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L48) · `section:6bc5f7df6561e72eadcc` · paragraph

Der konkrete D5-Singulettpaarkanal besitzt [formula in source] und gehört zum [formula in source] - beziehungsweise konjugierten schweren Majorana-Anschluss. Sein direkter Familientensor ist die ursprüngliche schwere Form [formula in source] in der erklärten Q [formula in source] -Eigenbasis. Auch sie wird durch [formula in source] samt allen sechs Rückleseamplituden dargestellt. Für den dimensionslosen Tensor [formu

## Die bereits vorhandenen gemeinsamen Neutrinobedingungen bleiben erhalten.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:82-95](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L82) · `section:9066906d14d53927649f` · paragraph

Das Programm verwendet den ursprünglichen Operator [formula in source] und die eingefrorenen Eingaben von nu_scalaron_v3.yaml. Die bestehende gleichzeitige Bedingung aus größtem Dirac-Singularwert und [formula in source] aus Abschnitt [formula in source] Dies ist die bereits dokumentierte bedingte Konsistenzlösung, keine neue Massenprognose. Insbesondere bleiben die Kalibrierung von [formula in source] , der Washout-

## Die verbleibende Phase wird nun zu einer konkreten Quellenantwort.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:96-119](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L96) · `section:68206360dff9a21fa2a7` · paragraph

Im ausdrücklich phasenoffenen Zweig mit [formula in source] verbleibt eine physische Majorana-Phase. Mit dem ursprünglichen [formula in source] lautet diese Familie Die unveränderten leichten Massen, PMNS-Winkel und Dirac-CP-Invariante, [formula in source] , die ungeflavorten schweren CP-Invarianten sowie [formula in source] wählen [formula in source] nicht aus. Mit [formula in source] , wobei [formula in source] die

## Welche Symmetrie die Matrix tatsächlich auswählen darf.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:120-155](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L120) · `section:32f4278cfa35e310cbcd` · paragraph

Die beiden ursprünglichen markierten Generatoren liefern einen zusätzlichen exakten Test. In der zyklischen Darstellung seien sie [formula in source] und [formula in source] . Sie erfüllen [formula in source] . Für eine gemeinsame Charakterlinie des symmetrischen Paarraums folgen daraus [formula in source] , also [formula in source] . Eine [formula in source] -invariante symmetrische Matrix besitzt die Form [formula 

## Der jetzt genau bestimmte Auswahlgegenstand.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:156-183](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L156) · `section:5a20ac3d1660e5433ae5` · paragraph

Alle sechs Paare tragen [formula in source] , während die neutralen Felder und die Familien-Defekte diese D5-Ladung nicht kompensieren. Im ursprünglichen [formula in source] -invarianten Vakuum gilt folglich [formula in source] Eine Matrix als geladene Einsetzung zu berechnen ist damit etwas anderes als ihre Auswahl durch einen physisch realisierten Hintergrund. Der verschwindende Einpunktwert schließt einen eichinva

Explicit source references:

- [tfpt_explorer/source_neutrino_dictionary.py](../../../../tfpt_explorer/source_neutrino_dictionary.py#L1) · explicit_file_citation

## Ein gemeinsamer Transport für primitive Windung, Massentensor und neutrale Antwort

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:184-192](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L184) · `section:13e84caf3b741e5ef992` · subsection

Die Fortsetzung vom 29. September arbeitet unmittelbar am vorher benannten Anschluss. Die ursprüngliche Fuchsverbindung bestimmt nicht nur die Familienendphasen. Ihr tatsächlicher Spin-Lift induziert auf den sechs symmetrischen Paaren eine Verbindung, aus der sich die ganze ursprüngliche Verbindung wieder zurückgewinnen lässt. Auch die primitive Determinantenwindung und die bereits berechnete neutrale RHP-Antwort las

## Die ursprüngliche Dreierwirkung muss mit ihrem Spin-Lift eingehen.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:193-215](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L193) · `section:518137b49ed8cfe0b1a2` · paragraph

Setze [formula in source] , [formula in source] und [formula in source] . Die bereits an den tatsächlichen C-Strömen geprüfte Basisabbildung ist [formula in source] , wobei [formula in source] die native Reihenfolge [formula in source] in die Außenpotenzreihenfolge [formula in source] übersetzt und [formula in source] die dreidimensionale Hodge-Abbildung ist. Die Identität [formula in source] ergibt auf dem behaltene

## Zustand und Massenkoeffizient besitzen entgegengesetzte Orientierung.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:216-267](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L216) · `section:d0851fb9eda15730139e` · paragraph

Für einen symmetrischen Quellenkoeffizienten [formula in source] und eine duale symmetrische Massenform [formula in source] lautet der faserweise Transport Denn [formula in source] . Die beiden Vorzeichen sind daher keine wählbaren Konventionen innerhalb derselben Zuordnung: Die Paarzustände und ihre kontrahierenden Koeffizienten sind dual. Das skalare Matrixelement [formula in source] bleibt erhalten, wenn gleichzei

## Die sechs Paarkanäle behalten die vollständige Verbindung.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:268-293](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L268) · `section:749f7c5e961e74c49def` · paragraph

Die induzierte Verbindung auf [formula in source] ist Aus ihrer Wirkung auf [formula in source] liest man [formula in source] auf dem diagonalen Eintrag und [formula in source] auf dem Eintrag [formula in source] ab. Damit sind sämtliche neun komplexen Einträge von [formula in source] bekannt. Es folgt [formula in source] Die Abbildung der Verbindung ist daher injektiv. Eine beliebige [formula in source] -Matrix lieg

## Die neutrale Antwort ist eine Kontraktion genau dieser Verbindung.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:294-312](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L294) · `section:9ab6936ae3a6bdf50683` · paragraph

Im festgehaltenen ursprünglichen Fuchsrahmen und mit derselben symmetrischen RHP-Normalordnung wie in Abschnitt Die rechte Seite stimmt mit dem bereits berechneten vollständigen rationalen Flavor-Defektkern überein. Es wird keine zweite neutrale Quelle eingesetzt. Die Spuren einer Verbindungsform sind bei beliebigen lokalen Rahmenwechseln nicht für sich invariant; deren Ward-/Normalordnungsterme müssen dann ebenfalls

## Auch der nötige lokale Ableitungsterm lässt sich aus derselben Quelle ergänzen.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex:313-392](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/007-subsection-die-vollst-ndige-neutrinomatrix-besitzt-ein-n.tex#L313) · `section:5112bdd23a5ba88e3d14` · paragraph

Eine faserweise Darstellung allein berechtigt noch nicht dazu, gewöhnliche Ableitungen von ortsabhängig gedrehten Feldern einzusetzen. Hier ist die Korrektur konkret. In einer Spaltenkonvention für die Feldkomponenten sei [formula in source] Der konstante Term fehlt wegen der tatsächlichen Nullrelation [formula in source] . [formula in source] ist der bereits vorhandene antisymmetrische Grad-drei-Kanal. Für eine Feld

Explicit source references:

- [tfpt_explorer/source_mass_transport.py](../../../../tfpt_explorer/source_mass_transport.py#L1) · explicit_file_citation

## Die Wand-Lesart: gemeinsamer geometrischer Anschluss und korrigierte Neutrino-Weiche

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/008-subsection-die-wand-lesart-gemeinsamer-geometrischer-ans.tex:1-5](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/008-subsection-die-wand-lesart-gemeinsamer-geometrischer-ans.tex#L1) · `section:cd6ae36102a9e34a7944` · subsection

Die Wand-Idee liefert einen bedingten geometrischen Anschluss, aber keinen Zwang zu Dirac-Neutrinos. Die volle ursprüngliche Quelle enthält bereits Standardmodell-Singuletts mit [formula in source] . Ein spezielles Spinorbündel verbindet außerdem Familienindex und Anomalieklasse. Die entscheidende gemeinsame Auswahl betrifft die Verbindung, den physischen Zustand und die Kopplung; sie folgt nicht aus dem Fehlen eines

## Die gemeinsame Bedingung für den weiteren Lösungsweg.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/008-subsection-die-wand-lesart-gemeinsamer-geometrischer-ans.tex:127-133](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/008-subsection-die-wand-lesart-gemeinsamer-geometrischer-ans.tex#L127) · `section:9873d8728c127f20b433` · paragraph

Die Wand-Lesart darf die vorhandenen [formula in source] -, Massen- und Flavorherleitungen nicht durch freie Kompaktifizierungsparameter ersetzen. Schon dimensionsanalytisch ist [formula in source] von der Dimension Länge hoch sechs, während [formula in source] dimensionslos ist. In einer unverwobenen Produktkompaktifizierung mit konstantem Hintergrund gilt schematisch [formula in source] ; Normierung, Schwellen und 

## Vom Quellenfeld zum wirklichen Massenblock und zur gemeinsamen Vergröberung

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/008-subsection-die-wand-lesart-gemeinsamer-geometrischer-ans.tex:134-325](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/008-subsection-die-wand-lesart-gemeinsamer-geometrischer-ans.tex#L134) · `section:9621677b00fd57a555f8` · subsection

Der innere Operatoranschluss ist jetzt explizit geschlossen. Die zuvor konstruierten Paarfelder erzeugen durch ihre tatsächliche Modenwirkung genau die symmetrischen Matrixeinträge des ursprünglichen schweren Neutrinoblocks. Dieselbe Einsetzung liefert nach Eliminierung der schweren Zustände die vorhandene Seesaw-Matrix, einen Determinantenbeitrag und eine vollständige Gedächtnisantwort. Die Wahl der Einsetzung und i

Explicit source references:

- [verification/v252_full_finite_triple.py](../../../../verification/v252_full_finite_triple.py#L1) · explicit_file_citation

## Zustand und Wirkung aus derselben Rückwirkung

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/009-subsection-zustand-und-wirkung-aus-derselben-r-ckwirkung.tex:1-9](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/009-subsection-zustand-und-wirkung-aus-derselben-r-ckwirkung.tex#L1) · `section:fb5a79ad28f8f85f979b` · subsection

Die gemeinsame Information ist jetzt genauer bestimmt. Eine korrekte Vergröberung muss sowohl die dynamische Antwort als auch den reduzierten Zustand aus demselben vollständigen Kern gewinnen. Am ursprünglichen Neutrinooperator ist diese Verbindung nun berechnet. Der aus einer Momentaufnahme rekonstruierte Operator ist im Allgemeinen nicht die ruhende Massenantwort. Unter passender Trennung der schweren und leichten 

## Wann die Zustandsauswertung die leichte Massenmatrix wiedergibt.

[documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/009-subsection-zustand-und-wirkung-aus-derselben-r-ckwirkung.tex:96-159](../../../../documents/tfpt_explorer--docs--session-2026-09-28--TFPT_Gesamtsynthese_2026-09-28/sections/009-subsection-zustand-und-wirkung-aus-derselben-r-ckwirkung.tex#L96) · `section:f4fc0af10aaac064b21c` · paragraph

Für schwache schwere–leichte Mischung liefert die Entwicklung in [formula in source] bei festem [formula in source] in zweiter Ordnung Das Vorzeichen folgt bereits aus der zweiten geteilten Differenz der Fermi-Funktion bei [formula in source] . Gegenüber dem statischen Beitrag [formula in source] erhält jeder schwere Eigenkanal den Faktor Die Annäherung ist somit algebraisch in [formula in source] , nicht exponentiel
