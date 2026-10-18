# Universalraum research — part 34

[Topic entry](../universalraum.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Further audit lemmas (machine-verified this round)

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:11870-11907](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L11870) · `section:5a4a32a8fac3620226a7` · section

Five more exact identities tie the flavor matrices and the [formula in source] exponents to the compiler. All checked with exact integer arithmetic.

## What this changes, and what stays open

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:11908-11947](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L11908) · `section:9dce604333464c544549` · section

[formula in source] is one container whose maximal subalgebras each project a different TFPT module:

Explicit source references:

- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation
- [verification/v118_hexagon_family_dictionary.py](../../../../verification/v118_hexagon_family_dictionary.py#L1) · explicit_script_identifier
- [verification/v122_margin_theorem.py](../../../../verification/v122_margin_theorem.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## The [formula in source] cascade bridge

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:11948-11956](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L11948) · `section:46e5fb87d8b363676201` · part

The connection in one sentence. The old E [formula in source] cascade (Paper V1.06: the nilpotent-orbit chain [formula in source] , [formula in source] ) and the new compiler/atlas are the same even-integer [formula in source] spine, read three ways: the cascade orders the numbers [formula in source] as a scale ladder, the atlas reads them as [formula in source] subalgebra branchings, and the compiler generates them 

## The old cascade, recalled

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:11957-11972](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L11957) · `section:04f7dd3db879c057f2bd` · section

Paper V1.06 builds a deterministic scale ladder from the nilpotent orbits of [formula in source] . With centralizer dimension [formula in source] and the Hasse chain restricted to [formula in source] , a unique maximal chain runs from [formula in source] ( [formula in source] ) down to the regular orbit ( [formula in source] ): [formula in source] The cascade arithmetic (endpoints, exponent rungs, IR-tail product, va

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## The spine: every rung is a current number

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:11973-12069](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L11973) · `section:460ed0402fa8a2a3cb09` · section

Reading [formula in source] against today's compiler atoms, the secondary-branching atlas and the [formula in source] anchor power sums [formula in source] , 25 of the 27 rungs are load-bearing numbers (machine-checked):

## Three views of one spine

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12070-12117](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12070) · `section:4197dff00d3e35e63045` · section

at (0.35,58) [formula in source] — E-series / atlas branchings (UV); at (0.35,40) [formula in source] ; at (0.35,30) [formula in source] \,(Coxeter rung, [formula in source] ); at (0.35,24) [formula in source] — [formula in source] , [formula in source] , [formula in source] ; at (0.35,15) [formula in source] (IR atoms); at (0.35,8) [formula in source] \,(flavor selector, end); at (0,60.5) [formula in source] start; 

Explicit source references:

- [verification/v91_spine_tetrahedron.py](../../../../verification/v91_spine_tetrahedron.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* v431 (1): two-family split forced by 30 = 2*3*5 *) checkExact["v431 E8.DEGREE.LADDER.01 (i): E8 exponents = phi(30)=8 totatives of h=30=2*N_fam*g_car; coprime to 6 => +-1 mod 6, so degrees occupy ONLY {0,2} mod 6", exps == tot30 && EulerPhi[h] == 8 && h == 2*3*5 && expMod6 == {1, 5} && degMod6 == {0, 2}]; (* v431 (2): 6k family = 6 x spine {2,3,4,5} = v91 anchor a=(1,1,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2663)

## Direct [formula in source] relations: old vs current

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12118-12142](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12118) · `section:e5efca8d093402505d08` · section

The old cascade's ``fundamental relations near [formula in source] '' connect directly to the current note — one is identical, two are early forms of current refinements:

## Sector inventory: have all the old-cascade sectors been computed?

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12143-12181](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12143) · `section:e46853028c0648b4ef2e` · section

The old cascade also carried calibrated absolute scales: per block, one unit [formula in source] was fixed on a single reference and every other scale in the block followed fit-free from the ratio law [formula in source] (Paper V1.06, App. C). These block assignments are the place where the proton mass, the EW masses and the CMB temperature lived. The honest question is: has the new compiler re-derived each of these,

Explicit source references:

- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_script_identifier
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)

## What is new, what is old, what stays open

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12182-12214](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12182) · `section:f11aafdd5b2f10d1367d` · section

The flavor selector [formula in source] is the terminal orbit of the [formula in source] cascade; the compiler is the cascade's IR endpoint. The atlas branching blocks ( [formula in source] ) are the cascade's UV head ( [formula in source] ); the secondary atlas and the orbit cascade are the same spine read top-down vs.\ as subalgebras. The anchor power sums sit on doubled-exponent rungs: [formula in source] ( [formu

## The self-consistency loop

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12215-12225](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12215) · `section:f81e7d9852f1b4758b79` · part

The question, and the honest answer. The theory rests on two inputs, [formula in source] and [formula in source] . The old theory had a Möbius seam and the seed was the start of the [formula in source] cascade. Run it backwards: can the cascade/ [formula in source] return [formula in source] and [formula in source] , closing a self-consistent loop? Answer: the discrete content is a closed, overdetermined fixed point 

## The loop for [formula in source] — an overdetermined fixed point

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12226-12323](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12226) · `section:d894d77fee6901fefaf2` · section

Two independent structural conditions, both pure Lie-theory, force [formula in source] once [formula in source] is the closure object and [formula in source] is the four-puncture family geometry:

Explicit source references:

- [verification/v15_bootstrap_classification.py](../../../../verification/v15_bootstrap_classification.py#L1) · explicit_file_citation
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)

## The loop for [formula in source] — the `` [formula in source] '' is the [formula in source] rank

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12324-12345](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12324) · `section:7b0ea6ab8f70d59feae3` · section

The boundary normalisation is [formula in source] . Its integer is exactly the carrier Coxeter number, which the loop above equals to the [formula in source] rank: [formula in source] where [formula in source] is Euler's totient (the number of primitive residues mod [formula in source] [formula in source] the [formula in source] exponents) — so the `` [formula in source] '' has five concordant readings. The tree seed

## The Möbius origin of the irreducible [formula in source]

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12346-12470](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12346) · `section:1a1734f3aaab8aa152c3` · section

What the loop does not remove is [formula in source] . In the old theory this is exactly the Möbius datum: the orientable double cover of the Möbius fibre is a cylinder with two boundaries plus one [formula in source] seam [formula in source] ; Gauss–Bonnet gives [formula in source] (hence [formula in source] ), and the [formula in source] identification is the sheet `` [formula in source] '' of [formula in source] .

Explicit source references:

- [verification/v532_e8_degree_modular_checksum.py](../../../../verification/v532_e8_degree_modular_checksum.py#L1) · explicit_file_citation
- [verification/v496_celestial_wp4_character_shadow.py](../../../../verification/v496_celestial_wp4_character_shadow.py#L1) · explicit_script_identifier
- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_file_citation
- [verification/v66_e8_casimir_degrees.py](../../../../verification/v66_e8_casimir_degrees.py#L1) · explicit_file_citation
- [verification/v180_clock_is_mobius.py](../../../../verification/v180_clock_is_mobius.py#L1) · explicit_file_citation
- [verification/v55_coxeter_cycle.py](../../../../verification/v55_coxeter_cycle.py#L1) · explicit_file_citation
- [CELEST.SEAM.01](../../../../verification/status_ledger.csv#L556) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v532 round: E8.DEGREE.MODULAR.01 -- the dual-degree checksum 744. Exact mirrors: dual products, j-series constant 744, D16 control, non-heterotic controls, prime-totative fingerprint. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8334)
- [(* ---- (v63) Seam-Engineering Index: exact closed form ---- *) checkExact["||V||=248 c3^2=31/(8pi^2); 2||V||=31/(4pi^2); 248=dim E8, 31=1+h^v(E8)", With[{c3 = 1/(8 Pi)}, Simplify[248 c3^2 - 31/(8 Pi^2)] == 0 && 248/8 == 31 == 1 + 30]]; checkExact["Xi = 2||V||/Delta = 31/(24 pi^2 log(3/2)); Delta_eff = Delta - 2||V|| > 0", Simplify[(31/(4 Pi^2))/(6 Log[3/2]) - 31/(24 Pi^2 Log[3/2])] == 0 && N[6 Log[3/2] - 31/(4 Pi^2)] > 1]; (* ---- (v66) compiler atoms = E8 Casimir invariant degrees ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L300)
- [(* ==== v496 round: CELEST.WP4.01 -- the (E8)_1 character E4/eta^8 vs the glue-equivariant E8[C^2] S-algebra (WP4 of CELEST.SEAM.01, the type mismatch head-on). Exact content mirrored: the character coefficients through q^6 with the q j = E4^3/eta^24 cross-check; the equivariant Hilbert series (60+128t+60t^2)/(1-t^2)^2 with the quadratic cumulative count 31 s^2 + 92 s + 60 and the SU(2)_+ slice; the two-sided jet-Fock mismatch f = (1,128,8436,381056) with strictly increasing f_n/chi_n (n = 1..12); the level-2 null ideal 27000 = 30^3 = h_vee^3; the boundary bridges (mu4 period sum 248, 248 not a tower dimension, loop Fock 897266); mirrors v496. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3257)
- [(* ==== v497 round: CELEST.WP5A.01 -- WP5a of CELEST.SEAM.01, "the null ideal from the limit" (the v496 boundary-limit shadow made precise). Exact content mirrored: (i) the chi_w stabilisation family (threshold w = n+1, w = 2 = the chiral jet grading, loop Fock 897266 at u^4); (ii) the null ideal DERIVED via the Weyl dimension formula in the standard E8 frame (Sym^2(248) = 27000 + 3875 + 1, 27000 = h_vee^3, Casimirs/Dynkin indices, level-1 integrability, quotient 31124 - 27000 = 4124); (iii) the two-route identity (mu4 theta-split sector sum at q^2 = (1036,1024,1040,1024) = 4124, q^3 = 34752, glue diagonal h = (0,1,1,1)); (iv) the negative controls (SO(16)_1: 5304 + 1820 + 135 + 1, 5304 != 14^3, quotient 2076 = Theta_D8/eta^8, block weights (0,1/2,1,1); false periodisation; swapped glue). The Freudenthal/peeling residual-zero derivation itself is Python-side (v497 S3); the Weyl-dimension and orbit-independent counting consequences are what is mirrored here. Mirrors v497. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3312)
- [(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *) checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8", {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] && EulerPhi[30] == 8 == gcar + Nfam]; checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5", 30 == 2*Nfam*gcar == 2*3*5]; checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)", Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0]; checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1", 32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1]; (* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L245)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)

## The celestial and twistor continuum route

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:12471-13519](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L12471) · `section:cca5b83aae425d5f0e88` · section

The previous section identified the seam's boundary [formula in source] -sphere with the celestial sphere of null directions ( [formula in source] , clock [formula in source] order- [formula in source] M\"obius map v180_clock_is_mobius.py). Taking that identification seriously and reading the seam through the celestial-holography lens (the celestial-chiral-algebra construction of Bittleston–Homans–Sharma on ALE space

Explicit source references:

- [verification/v525_seam_bit_twist_blind.py](../../../../verification/v525_seam_bit_twist_blind.py#L1) · explicit_file_citation
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v515_celestial_wp5e_m1_omega_n.py](../../../../verification/v515_celestial_wp5e_m1_omega_n.py#L1) · explicit_file_citation
- [verification/v523_celestial_wp5e_wm_derived.py](../../../../verification/v523_celestial_wp5e_wm_derived.py#L1) · explicit_file_citation
- [verification/v507_seam_bit_origin.py](../../../../verification/v507_seam_bit_origin.py#L1) · explicit_file_citation
- [verification/v565_woit_beta3_pt_duality.py](../../../../verification/v565_woit_beta3_pt_duality.py#L1) · explicit_script_identifier
- [verification/v208_bh_thermodynamics.py](../../../../verification/v208_bh_thermodynamics.py#L1) · explicit_script_identifier
- [verification/v524_woit_beta2_os_quotient.py](../../../../verification/v524_woit_beta2_os_quotient.py#L1) · explicit_file_citation
- [verification/v497_celestial_wp5a_null_ideal.py](../../../../verification/v497_celestial_wp5a_null_ideal.py#L1) · explicit_file_citation
- [SEAM.CLOCK.RIGIDITY.01](../../../../verification/status_ledger.csv#L570) · explicit_claim_identifier · original status at linked ledger row
- [verification/v513_celestial_dterm_nonderivation.py](../../../../verification/v513_celestial_dterm_nonderivation.py#L1) · explicit_file_citation
- [WOIT.THETA.FREE.01](../../../../verification/status_ledger.csv#L586) · explicit_claim_identifier · original status at linked ledger row
- [verification/v527_seam_clock_silver_spectrum.py](../../../../verification/v527_seam_clock_silver_spectrum.py#L1) · explicit_file_citation
- [verification/v499_p2_weights_deligne_bg.py](../../../../verification/v499_p2_weights_deligne_bg.py#L1) · explicit_script_identifier
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_file_citation
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [CELEST.SEAM.01](../../../../verification/status_ledger.csv#L556) · explicit_claim_identifier · original status at linked ledger row
- [verification/v972_seam_interaction_front.py](../../../../verification/v972_seam_interaction_front.py#L1) · explicit_file_citation
- [verification/v519_woit_theta_rp_free.py](../../../../verification/v519_woit_theta_rp_free.py#L1) · explicit_script_identifier
- [verification/v528_seam_bit_twist_class_definition.py](../../../../verification/v528_seam_bit_twist_class_definition.py#L1) · explicit_file_citation
- [verification/v492_celestial_z4_orbifold.py](../../../../verification/v492_celestial_z4_orbifold.py#L1) · explicit_file_citation
- [verification/v180_clock_is_mobius.py](../../../../verification/v180_clock_is_mobius.py#L1) · explicit_file_citation
- [verification/v517_celestial_wp5e_m3_a0_uplift.py](../../../../verification/v517_celestial_wp5e_m3_a0_uplift.py#L1) · explicit_file_citation
- [verification/v520_celestial_wp5e_measure_decision.py](../../../../verification/v520_celestial_wp5e_measure_decision.py#L1) · explicit_script_identifier
- [verification/v503_qgeo_emergence_light.py](../../../../verification/v503_qgeo_emergence_light.py#L1) · explicit_file_citation
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v449_seam_mmst_uniform.py](../../../../verification/v449_seam_mmst_uniform.py#L1) · explicit_script_identifier
- [verification/v518_celestial_wp5e_delta1_derived_kill.py](../../../../verification/v518_celestial_wp5e_delta1_derived_kill.py#L1) · explicit_file_citation
- [SEAM.EQUIV.TWISTOR.01](../../../../verification/status_ledger.csv#L584) · explicit_claim_identifier · original status at linked ledger row
- [verification/v516_celestial_wp5e_m2_twisted_ks_measure.py](../../../../verification/v516_celestial_wp5e_m2_twisted_ks_measure.py#L1) · explicit_file_citation
- [verification/v190_nariai_entropy_bound.py](../../../../verification/v190_nariai_entropy_bound.py#L1) · explicit_script_identifier
- [SEAM.BIT.FREEDOM.01](../../../../verification/status_ledger.csv#L572) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BIT.ORIGIN.01](../../../../verification/status_ledger.csv#L571) · explicit_claim_identifier · original status at linked ledger row
- [verification/v129_entropy_power_law.py](../../../../verification/v129_entropy_power_law.py#L1) · explicit_script_identifier
- [verification/v512_seam_tau_flag.py](../../../../verification/v512_seam_tau_flag.py#L1) · explicit_file_citation
- [verification/v522_woit_beta1_gso_gauge.py](../../../../verification/v522_woit_beta1_gso_gauge.py#L1) · explicit_script_identifier
- [verification/v215_seam_deck_killtest.py](../../../../verification/v215_seam_deck_killtest.py#L1) · explicit_script_identifier
- [SEAM.TAU.FLAG.01](../../../../verification/status_ledger.csv#L576) · explicit_claim_identifier · original status at linked ledger row
- [CELEST.DTERM.NONDERIV.01](../../../../verification/status_ledger.csv#L577) · explicit_claim_identifier · original status at linked ledger row
- [verification/v128_graded_hull.py](../../../../verification/v128_graded_hull.py#L1) · explicit_script_identifier
- [verification/v510_seam_bit_freedom.py](../../../../verification/v510_seam_bit_freedom.py#L1) · explicit_script_identifier
- [verification/v521_seam_bit_rp_blind.py](../../../../verification/v521_seam_bit_rp_blind.py#L1) · explicit_file_citation
- [verification/v490_seam_parity_census.py](../../../../verification/v490_seam_parity_census.py#L1) · explicit_script_identifier
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_file_citation
- [verification/v501_celestial_wp5d_two_interval_index.py](../../../../verification/v501_celestial_wp5d_two_interval_index.py#L1) · explicit_file_citation
- [verification/v511_celestial_wp5e_delta2_tensor_ledger.py](../../../../verification/v511_celestial_wp5e_delta2_tensor_ledger.py#L1) · explicit_file_citation
- [verification/v505_celestial_wp5e_beta_equivariant_ledger.py](../../../../verification/v505_celestial_wp5e_beta_equivariant_ledger.py#L1) · explicit_file_citation
- [verification/v100_numerology_null_mc.py](../../../../verification/v100_numerology_null_mc.py#L1) · explicit_script_identifier
- [verification/v514_celestial_wp5e_eps1_axion_slot.py](../../../../verification/v514_celestial_wp5e_eps1_axion_slot.py#L1) · explicit_file_citation
- [verification/v168_qgeo_rigidity.py](../../../../verification/v168_qgeo_rigidity.py#L1) · explicit_script_identifier
- [verification/v500_celestial_wp5c_gns_limit_state.py](../../../../verification/v500_celestial_wp5c_gns_limit_state.py#L1) · explicit_file_citation
- [verification/v377_seam_s3_e8character.py](../../../../verification/v377_seam_s3_e8character.py#L1) · explicit_script_identifier
- [verification/v498_celestial_wp5b_singular_vector.py](../../../../verification/v498_celestial_wp5b_singular_vector.py#L1) · explicit_file_citation
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [verification/v506_seam_clock_rigidity.py](../../../../verification/v506_seam_clock_rigidity.py#L1) · explicit_file_citation
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [verification/v495_celestial_wp3_gs_alignment.py](../../../../verification/v495_celestial_wp3_gs_alignment.py#L1) · explicit_file_citation
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v502_celestial_wp5e_prefactor_level.py](../../../../verification/v502_celestial_wp5e_prefactor_level.py#L1) · explicit_file_citation
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v509_celestial_wp5e_eps2_level_from_flux.py](../../../../verification/v509_celestial_wp5e_eps2_level_from_flux.py#L1) · explicit_file_citation
- [verification/v214_seam_pillowcase.py](../../../../verification/v214_seam_pillowcase.py#L1) · explicit_script_identifier
- [verification/v104_nariai_clock.py](../../../../verification/v104_nariai_clock.py#L1) · explicit_script_identifier
- [verification/v504_celestial_wp5d_klm_completeness.py](../../../../verification/v504_celestial_wp5d_klm_completeness.py#L1) · explicit_file_citation
- [verification/v496_celestial_wp4_character_shadow.py](../../../../verification/v496_celestial_wp4_character_shadow.py#L1) · explicit_file_citation
- [verification/v508_celestial_wp5e_gamma_pairing.py](../../../../verification/v508_celestial_wp5e_gamma_pairing.py#L1) · explicit_file_citation
- [verification/v493_celestial_wp2_clock_deformation.py](../../../../verification/v493_celestial_wp2_clock_deformation.py#L1) · explicit_file_citation
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v519 round: WOIT.THETA.FREE.01 -- the WOIT-alpha milestone of the OS twistor bridge: the real structure exists (two-family classification, mu4 torsor, Z8/C^4/Cl(16) levels) and the exact free-RP preconditions + site-cut degeneration + continuum control. The 40-digit positive- definiteness inertia certificates of the bond-cut Grams (R3/R5) are Python-only by the suite convention (mpmath eigh at dps 40). Mirrors v519. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7077)
- [(* ==== v525 round: SEAM.BIT.TWISTBLIND.01 -- "the twist-state kill": the NINTH side-blind test on the v512 scoreboard (8 -> 9); the free-plus-twist class is exhausted. Three exact mirrors: (i) the integer incidence frame + the sigma o r = +-sigma congruence mechanism (swap axes: sigma o r = sigma => the twisted Gram is the diagonal unitary congruence D M D = spectrally invisible; fixing axes at pi/2: sigma o r = -sigma = the eta flip); (ii) the pi/2-existence solveset of the mark-fixing axes + the exact counterwitness census ((3+4i)/5 unimodular but NEVER a root of unity up to order 64 -- no lattice mark-compatible reflection at any dyadic refinement); (iii) the delta <-> pi - delta mirror equivariance (the lattice reflection maps the m-mark set EXACTLY to the (8-m)-mark set -- the exact mechanism behind the Casimir mirror symmetry ln|omega(D)|(m) = ln|omega(D)|(8-m) and behind pi/2 as the symmetric point of every invariant readout). The Pfaffian insertion spectra, the Bogoliubov 2-of-16 pattern census, the defect energy and the 40-digit inertia certificates are numerical (mpmath), Python-only, flagged here. Mirrors v525. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8058)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* ==== v513 round: CELEST.DTERM.NONDERIV.01 -- "the c_d negative certificate": can geometry derive c_d = 1920? Anti-numerology battery on the v511 [C] fence 1920 = |W(D5)|. Six exact mirrors: (i) the propagator anchor + T3-slot pinning, (ii) the five-way convention table + the convention-stable factorisation 32 x 60, (iii) the flux enumeration + look-elsewhere ledger with control targets, (iv) the K2 quantisation lattices, (v) the K3 provenance clash + Weyl data, and (vi) the negative controls. Mirrors v513. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5859)
- [(* ==== v498 round: CELEST.WP5B.01 -- WP5b of CELEST.SEAM.01, "the singular vector as an operator" (the deleting object of the v497 null ideal made explicit). Exact content mirrored: (i) the case classification of the J^a_1 condition over the 248-element basis (190/57/1, exactly one case sees the level k) from the standard E8 root data + the theta-grading (1,56,134,56,1); (ii) the LEVEL DIAL derived from the affine sl2 commutation -- F^theta_1 (E^theta_{-1})^n|0> = n(k-n+1) (E_{-1})^{n-1}|0>, square coefficient 2(k-1) = -2(1-k) with values (-2,0,2) at k = 0,1,2, Shapovalov 2k(k-1) (0 at k = 1, 4 at k = 2), cube singular exactly at k = 2; (iii) the glue frame -- 240 roots with classes (52,64,60,64), inner grading <r,h> = class mod 4 on all 240, theta_glue = argmax with <theta,h> = 5 => j(theta) = 1, clock phase i^(2j) = -1, cross-table rows (1,56,126,56,1); (iv) multiplicity 1 of weight 2 theta in the level-2 Fock (U(g)|s> is THE 27000 = 30^3), lattice reading (2t,2t)/2 = 4 > 2, and the comark discriminator (E8 comarks all >= 2 -- vacuum the only level-1 primary; D8 has three comark-1 weights with h = (1/2,1,1)); (v) the twisted-slot tension (two sector-C_1 modes never sum to 8 quarters, minimum 6 = q^(3/2)) + the per-period 248. The full Chevalley/PBW singularity run (J^a_1|s> = 0 on all 248 basis elements, engine unit tests on all 61504 pairs) is Python-side (v498 S1-S3); the counting/dial/grading consequences are what is mirrored here. Mirrors v498. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3463)
- [(* ==== v517 round: CELEST.WP5E.M3.01 -- "the a0 uplift": milestone M3 of the CELEST.SEAM.01 back-reaction programme executed (SUCCESS on the preregistered v514 S8.3 criterion). Six exact mirrors: (i) the GH multipole ledger (selection rule m = 0 mod 4, (4, +-4) amplitude (35/16) sin^4 th) + the twistor family at general orbit phase (e1 = e3 = 0, a2 = 4 z0 zb0 zeta^2, a0(zeta), v515 slice), (ii) the kernel bridge (null coordinate: any kernel harmonic; residue V-ledger identity 1/(2r); source flux -4 pi per centre), (iii) the asymptotic kernel log (coefficient 4 = |mu4|, first seam correction a0/eta^4, exact m-grading, GLT tower p_{4k} = 4(-a0)^k with the n = 0 mod 4 selection rule, no log x power terms), (iv) the exceptional-locus log (chi(0) = log a0 = 4 log t0 + i(4 phi0 + pi), modulus response 1 at the locus vs power-law at infinity), (v) the period response (linear in t0, d log Pi/d log a0 = 1/4 = 1/|mu4|, integrated monodromy i = one Coxeter clock step, centre permutation, a0-rigid node support, K4 discriminants ~ t0^2), and (vi) the negative controls ((4,0) clock-invariant, Z2/EH reads 2 on every dial, k = 3/5 orbits move the coefficient, the forbidden family fails both dials). The contour-transform typing itself is the [C] GLT dictionary; the BM kernel anchor is already mirrored in the v515 round. Mirrors v517. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L6678)
- [experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ==== v523 round: CELEST.WP5E.WM.01 -- "the constructive w_m derivation": the residual [O] of v516/v520 closed at the fibre-zero-mode level (verdict ERFOLG; the typed premises TP-REG/TP-Q/TP-NUM/TP-CH are the [C] fence, a typing, not mirrorable). Five exact mirrors: (i) the equivariant mode ledger = the closed form 1/((1-q i^j)(1-q i^{-j})) at every order n <= 40 with the Abel value (1/2, 1/4, 1/2) = 1/det_j, Dedekind sum 5/4 and product 16; (ii) the zeta-determinant route (reflection formula symbolic, det_zeta = 4 sin^2(pi j/4) = det_j, Quillen split det Delta = det_j^2, the unique REAL POSITIVE section, the diag(i,i) control breaking realness and the conjugation pairing); (iii) the derived-weight contact vectors + per-sector Okubo squares + total 45<x,x>^2 + psi certificates on the 240 glue roots + the Z2/EH anchor; (iv) the consistency chain w = 4h = -4 ch2 with the T3 budget c = 4 and the two wrong-weight negative controls (1/det^2 leftovers (2, 12) + Quillen contradiction; 1/|1-i^j| irrational with T5/T3 leftovers in Q(sqrt2)); (v) the k = 3, 5 cyclotomic wandering controls w_m = m(k-m)/2 = k h_m. The (C,2) Cesaro truncation means, the Hurwitz/Lerch 40-digit certificates and the delta-1f stripped block limits are numerical (mpmath), Python-only, flagged here. Mirrors v523. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7792)
- [(* ---- (v126) clock-wall bridge ---- *) Module[{a0, spec, lams}, a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; spec = Sort[Eigenvalues[a0]]; checkExact["v126 the weights are the parabolic weights: spec A0* = {0, 1/3, 2/3} = n/N_fam; bridge (1-alpha)^6 = {1, (2/3)^6, (1/3)^6}", spec == {0, 1/3, 2/3} && Sort[((1 - #)^6 &) /@ spec, Greater] == {1, (2/3)^6, (1/3)^6}]; checkExact["v126 checkpoint 1 + determinant: linear coefficient p2/N = 2 = |Z2| (= v104 entropy rate 2H); det(1 - A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L890)
- [(* ==== v514 round: CELEST.WP5E.EPS1.01 -- "the O(-2) bulk-axion slot": WP5e-epsilon-1 executed (verdict B). Eight exact mirrors: (i) the equivariant Penrose ledger (pushforward blocks = wave-operator kernels, block by block, all d <= 6, all 4 characters), (ii) the character series P_m with the surviving bulk-axion zero mode and the twisted minimal content, (iii) the Molien hypersurface + the diag(i,i) Veronese control, (iv) the Okubo residue (6<x,x>)^2 on the 240 glue roots + the so8 irrationality control, (v) the measure cancellation excluding 3 and 12 + the flux/sector dial, (vi) the GH centre dichotomy re-deriving the v493 family, (vii) the period lockstep + the Coxeter clock from geometry, and (viii) the multipole selection rule + the EH log ledger. Mirrors v514. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L6056)
- [(* ==== v522 round: WOIT.BETA1.GSO.01 -- "the clock is time-like, GSO is the gauge datum": the Z8/NS tower + Ramond control, the invariant- dimension chain, the time-like reflection census, the exact Hermiticity witness of the clock insertion, the GSO 2-torsion census and the family-A tower-normalisation failure. The 40-digit GSO-fixed RP inertia certificates ((29,0,0)/(8,0,0)/(7,9,6)/(17,12,0)) are Python-only by the suite convention. Mirrors v522. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7609)
- [(* ==== v527 round: SEAM.CLOCK.SILVER.01 -- silver explained / demystified. Exact mirrors: (i) tan(pi/8) Hankel pencil; (ii) N-scaling witness; (iii) gap = arcsinh(1) = gd^{-1}(pi/4). Census Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8187)
- [(* ==== v502 round: CELEST.WP5E.ALPHA.01 -- WP5e-alpha of CELEST.SEAM.01, "prefactor and level bookkeeping" (the CFT-side anchor of the twistor uplift). Exact content mirrored: (i) the HURWITZ-ZETA vacuum energies -- zeta(-1,theta) = -B2(theta)/2 at rational twists, E_b(theta) = -1/24 + theta(1-theta)/4, Ising shift E_R - E_NS = 1/16 per Majorana, the untwisted vacuum 8 x (-1/24) = -1/3 = -c/24 with the Sugawara route 248/(1+30) = 8, and the eta^8 exponent 8/24 = 1/3; (ii) DISCRIMINANT FORM = CASIMIR ENERGY -- coset minima h_D5 = (0,5/8,1/2,5/8), h_A3 = (0,3/8,1/2,3/8), glue diagonal (0,1,1,1) INTEGER (exact lattice enumeration), spectral flow j^2 (h,h)/32 with (h,h) = 20, (h',h') = 12, sum 32 (mod-1 identity), free-fermion route n/16 = 5/8, 3/8, 1 on 10 + 6 = 16 = 2^(g_car-1) Majoranas, and the deck failure 3/16 != 3/8; (iii) the k = 1 FIXING EQUATIONS -- simple-current closed forms 5k/8, 3k/8, glue-diagonal integrality for ALL k = 1..8 (the honest 'fixes nothing' finding), current condition h(J) = k = 1 unique, conformal embedding 47k^2 + 219k - 266 = (k-1)(47k+266) with unique positive root 1, D8 route 128k(1-k) = 0, central charge 248k/(k+30) = 8 <=> 240(k-1) = 0, Shapovalov values 2k(k-1) = (0,4,12,24), and the Weyl-dim count 31124 - 27000 = 4124 (dims 248/3875/27000 recomputed); (iv) the CHARACTER SUMS -- the four glue-coset thetas sum to E4 = (1,240,2160, 6720), the sector characters (leading coefficients (1,64,60,64), currents (60,64,60,64)) sum to E4/eta^8 = q^{-1/3}(1,248,4124,34752), and the D8 control Theta_D8 + Theta_s = E4 with h_v = 1/2 non-integer. The sympy symbolic manipulations and the PBW engine are Python-side (v502 S1/S5). Mirrors v502. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3893)
- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)
- [(* ==== v499 round: P2.TYPING.01 -- the P2 weight-typing postulate hardened: the anchor a = (1,1,2) as the Birkhoff-Grothendieck splitting exponents of the Deligne canonical extension E of the flavor connection (types the v491 check-9 residual). Exact content mirrored: (i) partition enumeration under the full typing (BG dictionary h^0 = 0 <=> a_i >= 1, exhaustive window) + the naive- typing negative control (h^1(E') = 3 forces deg -6, three splittings, e2 never 5) + the h^1 discrepancy (h^1(anchor bundle) = 1 != 3); (ii) the Deligne residue-trace degree (cusp exponents {0,1/3,2/3} = the unique lift of spec(lam^3 - 1) to [0,1), trace 1 per mark, deg E = -4, par-deg 0, witness A0* charpoly); (iii) the Schur-Horn permutohedron integer points {(2,2,0),(2,1,1)} with h^0 = 0 killing {2,2,0}; (iv) the Biswas Z3-cover degree arithmetic (genus 2, eigensheaves O(-2)^2, chi cross-check, regular-rep weights, the decomposable model {0,2,2} with h^0 = 1 = the unstable companion; deck double genus 1, j = 1728); (v) the n-mark formula e2 = (n-2)(n+1)/2 = 5 only at n = 4. The sympy symbolic parts (H^1 residue basis, monodromy group closure |<U,M0>| = 24, the 324-case stability skeleton) stay Python-side (v499). Mirrors v499. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3620)
- [(* ==== v516 round: CELEST.WP5E.M2.01 -- "the twisted Kodaira-Spencer measure": milestone M2 of the CELEST.SEAM.01 back-reaction programme executed (SUCCESS on the preregistered v514 S8.2 criterion, on the DECLARED completion measure -- the completion reading itself is the [C] fence, everything mirrored here is exact arithmetic). Six exact mirrors: (i) the completion-weight identity w_m = sum_j (1 - i^{jm})/det_j = (0, 3/2, 2, 3/2) = 4 h_m = |mu4| h_m = -4 ch2(T_m) with the index bridge f(m) = -h_m = ch2 (no free scale), (ii) the root/quartic replication (class quartics Q_m, A_fix two routes, bulk Okubo 36<x,x>^2 = (K^(0))^2/100), (iii) the parameter-free locks (T5 = 0 for symbolic scale, 4:3 ratio, T3 budget forces c = 4 = |mu4|, unique leading weights det 256), (iv) the contact term two forms + the per-sector SUCCESS TABLE (perfect Okubo squares 36<x,x>^2/det_j, total 45<x,x>^2 = (5/4) x 36, certificates 32/72/psi = 64 all killed, exchange-span remainder, mu-blind chain), (v) the negative controls (wrong scale 32 - 8c, shuffled weights, SO(16) KILL, diag(i,i) degeneration, Z2/EH anchor), and (vi) the multiplier note (discriminant T-phase orders (1,8,2,8) squaring to (1,4,1,4), Gauss sums 2e(3/8), 2e(5/8), full Weil 4). Mirrors v516. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L6504)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [(* ==== v510 round: SEAM.BIT.FREEDOM.01 -- the freedom attack on the v506/v507 alignment bit: the POSITION half of the bit is topology. Exact content mirrored: (i) the DIHEDRAL CENSUS -- on the refined 2N-point seam circle D_16 has 17 involutions with EXACTLY ONE free (the antipodal shift by 8) and all 16 reflections have exactly 2 circle fixed points (8 site-axis + 8 edge-axis; robustness N = 8, 12; odd control N = 9: zero free), plus the quotient topology chi(C/antipode) = 0 (circle) vs chi(C/reflection) = 1 (interval, 2 boundary corners); (ii) the AUT COMPLETENESS -- Aut(C_8) = D_8 by brute force over all 8! = 40320 permutations and Aut(C_16) = D_16 by degree-2 propagation (all 32 candidates), so the census covers ALL circle symmetries; (iii) the Cl(16) DICHOTOMY CENSUS -- on explicit 256x256 Jordan-Wigner gammas the free deck's NS implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the implementers of ALL 16 reflections exist (one of the two spin lifts +-R) and square to SCALARS {2^7 (site-axis), 2^8 (edge-axis)} (split): NONSPLIT <=> FREE over the complete census; root dichotomy 2 (the +-quarter shifts) vs 0 total over all 16 reflections; (iv) the REAL-STRUCTURE TABLE -- the deck-commuting antiholomorphic involutions solve symbolically to exactly two families (M diagonal: mu conj z, fix line through the poles; M antidiagonal: mu/conj z, fix circle |z| = sqrt mu), and the unique mark-fixing real structure per configuration is equatorial/FREE for mu4 and generic-unit, real-axis/NOT-free for silver and generic-real, and NONEXISTENT for the hexagonal frame; (v) HARMONIC + FREE => mu4 -- the deck-pair cross-ratio (1-b)^2/(1+b)^2 = -1 solves exactly to b = +-i, with the lambda table (2, 1/2, 3/4, 5/4) real and the hexagonal lambda complex; (vi) the HONEST COUNTERWITNESSES -- the discrete witness {0,1,8,9} (shift-invariant, crossing, but not quarter-shift-invariant) and the continuous witness {+-1, +-(3+4i)/5} (pair cross-ratio -1/4, j = 148176/25 != 1728, clock does not preserve): the Fock dichotomy measures the CLASS, not the modulus. The Moebius/Klein covering models and the pillowcase branch control stay Python-side (v510). Mirrors v510. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5155)
- [(* ==== v505 round: CELEST.WP5E.BETA.01 -- WP5e-beta "the equivariant anomaly ledger on twistor space" (the Atiyah-Bott/Lefschetz skeleton of the one-loop inflow on C^2/Z4 with the E8 mu4-glue monodromy; the CFT side is v502). Exact content mirrored: (i) the AB DENOMINATORS + CHARACTERS -- det(1 - g_j^{-1}) = (2,4,2), Dedekind sum 5/4 = (|Z4|^2-1)/12, equivariant characters (248,0,-8,0) by TWO routes (graded dims / explicit root sum), invariant average 60 = carrier, Frobenius 61568; (ii) the INDEX BRIDGE -- f(m) = (1/4) sum_j (i^{jm}-1)/det_j = ch2(T_m) = -(C^{-1})_mm/2 exactly, glue defect -78 by both routes with classes (-24,-30,-24), bridge identity sum_m h_A3(m) = 5/4; (iii) OKUBO PER SECTOR -- the invariant quartic sum over the 240 glue roots is EXACTLY 36 <x,x>^2 (36 = lambda~^2_e8), the twisted quartics are NOT proportional to squares (T5/T3 content), and the AB-weighted sum leaves the rigid residual 32 T3; (iv) the LEVEL DIALS -- lattice current count 240/0/0/0 for k = 1..4, embedding residual 47k^2+219k-266 = (0,360,814,1362), det(A-1) = -4 (one scale => one level); (v) the AXION-SLOT WEIGHTS -- a0 fills the graviton slot O(2) (Hamiltonian weight arithmetic X = -2 != +2 = Y, mismatch 4 = |mu4|), the clock weights on (a3,a2,a1,a0) are the regular mu4 representation, and the Coxeter eigencharacters {i,-1,-i} = the three twisted sector characters. Mirrors v505. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4244)
- [(* ==== v528 round: SEAM.BIT.TWISTCLASS.01 -- bit = twist-class choice. Exact mirrors: (i) cardinality lemma; (ii) 224-axis flip census; (iii) O-values. Pfaffian spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8213)
- [(* ==== v497 round: CELEST.WP5A.01 -- WP5a of CELEST.SEAM.01, "the null ideal from the limit" (the v496 boundary-limit shadow made precise). Exact content mirrored: (i) the chi_w stabilisation family (threshold w = n+1, w = 2 = the chiral jet grading, loop Fock 897266 at u^4); (ii) the null ideal DERIVED via the Weyl dimension formula in the standard E8 frame (Sym^2(248) = 27000 + 3875 + 1, 27000 = h_vee^3, Casimirs/Dynkin indices, level-1 integrability, quotient 31124 - 27000 = 4124); (iii) the two-route identity (mu4 theta-split sector sum at q^2 = (1036,1024,1040,1024) = 4124, q^3 = 34752, glue diagonal h = (0,1,1,1)); (iv) the negative controls (SO(16)_1: 5304 + 1820 + 135 + 1, 5304 != 14^3, quotient 2076 = Theta_D8/eta^8, block weights (0,1/2,1,1); false periodisation; swapped glue). The Freudenthal/peeling residual-zero derivation itself is Python-side (v497 S3); the Weyl-dimension and orbit-independent counting consequences are what is mirrored here. Mirrors v497. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3312)
- [(* ==== v493 round: CELEST.WP2.01 -- the clock-invariant deformation XY = Z^4 + a0 of the A3 seam orbifold (WP2 of CELEST.SEAM.01). Exact content mirrored: clock-invariance selects the 1-parameter slice sharply (P(iZ) = P(Z) forces a3 = a2 = a1 = 0; prod(Z - i^k w) = Z^4 - w^4); disc = 256 a0^3; binary-quartic invariants I = 12 a0, J = 0 identically => j = 1728 frozen (tau = i pillowcase), cross-ratio 2; negative controls a1 (j = 0) and a2-instance (j = 1556068/81); clock on H2 = Coxeter element of W(A3) (char x^3+x^2+x+1, eigenvalues {i,-1,-i}, no invariant cycle, chi_1-Fourier eigenline, period point t(i-1)(1,i,i^2)); versal weights (1,2,3,0) = regular mu4 rep; S-algebra corrections linear in a0 at the Z4 wrap (6/16 pairs) with the EH k = 2 analogue; mirrors v493. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3147)
- [(* ---- (v129) entropy power law ---- *) Module[{levels, lams, rates}, levels = Table[(3 - n)/3, {n, 0, 2}]; lams = levels^6; rates = 6 Log[1/levels]; checkExact["v129 entropy power law: S/S_dS = {1, 2/3, 1/3} = 1 - n/N; lambda = (S/S_dS)^6 = frozen spectrum; rates = {0, Delta, 6 ln 3}; alpha = deficit fraction; p2 = 6 = 2 N_fam", levels == {1, 2/3, 1/3} && lams == {1, (2/3)^6, (1/3)^6} && Simplify[rates[[2]] - 6 Log[3/2]] === 0 && Simplify[rates[[3]] - 6 Log[3]] === 0 && Table[n/3, {n, 0, 2}] == 1 - levels && 6 == 2*3 && rates[[1]] === 0 && levels[[1]] > levels[[2]] > levels[[3]]]; ]; (* ---- (v130) Born square ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L948)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)
- [(* ==== v507 round: SEAM.BIT.ORIGIN.01 -- the tautology attack on the v506 alignment bit, executed and refuted (Part A torus origin + Part B fermion dichotomy). Exact content mirrored: (i) the HALF-PERIOD DESCENT -- the fixed points of w -> -w on C/(Z + tau Z) are the 4 half-periods (2w in Lambda <=> coefficients in {0, 1/2}; the 1/3-control fails), a translation t_c descends iff 2c in Lambda (exactly the 3 nonzero half-periods), and the descended map sigma_i(x) = e_i + (e_i-e_j)(e_i-e_k)/(x-e_i) satisfies the exact curve-lift identity prod(sigma_i - e_l) = psi_i^2 prod(x - e_l) with RATIONAL psi_i, closing to Klein V4 symbolically; (ii) the CORE SOLVE -- the pair cross-ratio condition CR = -1 solves to lambda = -1 (sigma_1), 2 (sigma_2), 1/2 (sigma_3) exactly, union = the harmonic orbit with j = 1728, against j(3) = 21952/9 and j(hex) = 0; (iii) the STABILISER COUNTS -- the complete 24-triple enumeration gives (|Stab|, #involutions, #free) = (4,3,3) generic / (8,5,3) harmonic / (12,3,3) hexagonal, and in ALL three types the free involutions are EXACTLY the three sigma_c (the deck CLASS is forced); (iv) the CM FIXED POINT -- mult-by-i mod 2 fixes exactly the half-period (1,1) = c* = (1+tau)/2 while mult-by-rho 3-cycles all three, the lemniscatic clock ghat: x -> (x-1)/(x+1) needs the curve-lift factor psi = 2i/(x+1)^2 (the CM unit; t^2+1 irreducible over Q) and squares to the central -1/x; (v) the Cl(16) DICHOTOMY -- on explicit 256x256 Jordan-Wigner gammas the central implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the EDGE implementer Utilde_e = P_3 (g1+g5)(g2+g4)(g6-g16)(g7-g15)(g8-g14) (g9-g13)(g10-g12) implements the NS edge reflection and squares to the SCALAR +2^7 (split), and in the 32-element NS dihedral lift group the central deck has EXACTLY 2 square roots (the +-quarter shifts) vs 0 for the edge deck; (vi) the SILVER BIJECTION CENSUS -- all 8 mark bijections {+-1, +-(3+2 sqrt 2)} -> {0, 1, -1, inf} carry the deck z -> -z to the EDGE sigma_2/sigma_3 (never the central sigma_1), while all 8 mu4 bijections carry it to the CENTRAL sigma_1. The v493 circularity-audit direction and the 28/21 arrangement census stay Python-side (v507). Mirrors v507. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4545)
- [(* ==== v520 round: CELEST.WP5E.MEASURE.01 -- "the WP5e BCOV measure question decided at probe level" (delta-1e + delta-1f consolidated): the exact Weil data, the invariant-subspace forcing, the character arithmetic behind the two constructive sources (F-independence + Quillen pairing), the completion/contact/psi and Z2-anchor targets, the level-1 4-design of BOTH Lagrangian gluings, and the exact negative controls. The Harvey-Moore integrals, SVD memberships and J-weighted closures are numerical (mpmath/numpy) and stay Python-only by the suite convention. Mirrors v520. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7270)
- [(* ---- (v190) Nariai entropy bound: S_tot/S_dS >= 2/3 via (x-1)^2 ---- *) Module[{x, ratio, val1, gap, mn}, ratio = (x^2 + 1)/(x^2 + x + 1); (* denom = Phi_3(x), the N_fam cyclotomic *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1574)
- [(* ---- (v168) QGEO rigidity: mu4 square cross-ratio, mu4 characters = A3 exponents ---- *) Module[{mu4, cross, zz, eig, qspec}, mu4 = {1, I, -1, -I}; cross = Simplify[(mu4[[1]] - mu4[[3]]) (mu4[[2]] - mu4[[4]]) / ((mu4[[1]] - mu4[[4]]) (mu4[[2]] - mu4[[3]])) ]; (* omega_k = z^{k-1}/(z^4-1); pullback z->i z eigenvalue should be i^k *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1452)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [(* ==== v500 round: CELEST.WP5C.01 -- WP5c of CELEST.SEAM.01, "the GNS limit state" (the state whose GNS kernel contains the v497/v498 null ideal). Exact content mirrored: (i) the LEVEL-2 BLOCK CENSUS from the standard E8 root data -- 31124 = 248 + 30876 monomials in 9361 weight blocks with dim profile {164:1, 37:240, 7:2160, 1:6960}, orbit census by lattice norm (8,6,4,2,0) -> (240, 6720, 2160, 240, 1) with constant block dims (1,1,7,37,164); (ii) the RANK/KERNEL ARITHMETIC of the full Gram -- rank table per orbit (0,0,1,8,44) (the Python-side Gram result) gives total rank 4124 = 1 + 248 + 3875 = chi_2 (dim V(omega) = 3875 recomputed by Weyl from the dominant norm-4 weight) and kernel per orbit (1,1,6,29,120) summing to 27000 = 30^3 = dim V(2 theta) (Weyl); (iii) the CLOCK-CLASS SPLIT at the state level -- the same census in the glue frame with class(lambda) = <lambda,h> mod 4 turns the rank table into the split (1036,1024,1040,1024) = Theta_Cj/eta^8 at q^2, and level 1 gives (52+8,64,60,64) = (60,64,60,64); (iv) the THRESHOLD + LEVEL-DIAL + D8 arithmetic -- x-adic order w*r >= N+1 for all r >= 1 iff w >= N+1 (sharp at w = N via r = 1), level-1 root-mode norm = k (no 248 layer at k = 0), <s|s> = 2k(k-1) (0 at k = 1, +4 at k = 2), D8 census 7380 = 120 + 7260 in 2705 blocks with quotient 7380 - 5304 = 2076. The exact Gram computation itself (9361 blocks over Fractions, PSD inertia, the highest-weight norms (3844, 49, 2, 0), the contravariance and anti-involution machine checks on 61504 pairs) is Python-side (v500 S1-S4). Mirrors v500. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3709)
- [(* ---- (v205) GRAV.XI.01: xi = c3/phi_tree = 3/4, the independent gravitational 3/4 ---- *) Module[{c3, phitree}, c3 = 1/(8 Pi); phitree = 1/(6 Pi); checkExact["v205 GRAV.XI.01: the torsion-compression factor xi = c3/phi_tree = (1/8pi)/(1/6pi) = 3/4 EXACTLY; the Einstein-limit reduction 8 pi c3^2 = c3 makes G an output (xi = c3/phi0); and 3/4 = 12 pi (c3/2) = ln(m/mu) = q(A3) (v152) -- the torsion-compression and the gapped EH replica are two independent appearances of the same gravitational 3/4", Simplify[c3/phitree - 3/4] == 0 && Simplify[8 Pi c3^2 - c3] == 0 && Simplify[12 Pi (c3/2) - 3/4] == 0]; ]; (* ---- (v208) HOR.BHTHERMO.01: scalaron Wald factor + modular 2 pi = 1/(4 c3) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1708)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v103) trisection normal form ---- *) checkExact["v103 trisection: r = 2 cos(theta) => r^3 - 3r = 2 cos(3 theta) exactly", Simplify[(2 Cos[th])^3 - 3 (2 Cos[th]) - 2 Cos[3 th]] === 0]; rcT = 2 Cos[(ps + Pi)/3]; rbT = 2 Cos[(ps - Pi)/3]; r3T = 2 Cos[(ps + 3 Pi)/3]; checkExact["v103 centered angle: m = cos(psi)/3; roots sum 0, e2 = -3; Nariai roots (1,1,-2) at psi = 0", (Simplify[-Cos[ps + Pi]/3 - Cos[ps]/3] === 0) && (Simplify[rcT + rbT + r3T] === 0) && (Simplify[rcT rbT + rcT r3T + rbT r3T + 3] === 0) && (Simplify[{rcT, rbT, r3T} /. ps -> 0] == {1, 1, -2})]; sigT = Simplify[(rbT^2 + rcT^2)/3]; checkExact["v103 NORMAL FORM: sigma(psi) = 4/3 - (2/3) cos(2 psi/3); sigma(0) = 2/3, sigma(pi/2) = 1", (Simplify[sigT - (4/3 - (2/3) Cos[2 ps/3])] === 0) && (Simplify[sigT /. ps -> 0] == 2/3) && (Simplify[sigT /. ps -> Pi/2] == 1)]; checkExact["v103 canonical curvature sigma''(0) = 8/27 = (2/3)^3 (the Koide constant to the family power)", (Simplify[D[sigT, {ps, 2}] /. ps -> 0] == 8/27) && ((2/3)^3 == 8/27)]; checkExact["v103 invariant base slope: dsigma/dm = -(4/3) sin(2 psi/3)/sin(psi), limit -8/9 = -rank(E8)/N_fam^2", (Simplify[D[sigT, ps]/D[Cos[ps]/3, ps] + (4/3) Sin[2 ps/3]/Sin[ps]] === 0) && (Limit[D[sigT, ps]/D[Cos[ps]/3, ps], ps -> 0] == -8/9)]; checkExact["v103 x-coordinate cross-check: m(x) deck-invariant, m''(1) = -1/4, sigma''(1)/m''(1) = -8/9", Module[{mxw = Sqrt[3]/2 xx (1 + xx)/(xx^2 + xx + 1)^(3/2), sxw = (xx^2 + 1)/(xx^2 + xx + 1)}, (Simplify[(mxw /. xx -> 1/xx) - mxw, Assumptions -> xx > 0] === 0) && (Simplify[D[mxw, xx] /. xx -> 1] == 0) && (Simplify[D[mxw, {xx, 2}] /. xx -> 1] == -1/4) && (Simplify[(D[sxw, {xx, 2}] /. xx -> 1)/(D[mxw, {xx, 2}] /. xx -> 1)] == -8/9)]]; checkExact["v103 bridge: (2/3)^6 = ((2/3)^3)^2 -- same base, exponent ratio 2 = |Z2|", (2/3)^6 == ((2/3)^3)^2]; (* ---- (v104) the classical Nariai clock ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L392)
- [(* ==== v508 round: CELEST.WP5E.GAMMA.01 -- WP5e-gamma "the sphere-axion pairing check", an honest rigid NEGATIVE result (the exchange route for pairing the three twisted sphere axions with the rigid 32 T3 residual of the v505 Atiyah-Bott ledger is killed with a certificate). Exact content mirrored: (i) the VERTEX-SPACE DIMS -- the W(D5) x W(A3)-invariant quadratics on the 8-dim glue Cartan have bidegree dims (1,0,1), total 2 = span{s5, s3}, and the invariant quartics have bidegree dims (2,0,1,0,2), total 5 = span{P1,P2,P3,T5,T3} (Weyl nullspace arithmetic, generator by generator); (ii) the TWISTED QUADRATICS + the K^(0) = -15 K^(2) collapse (the two even-sector quadratics are PARALLEL); (iii) the PRODUCT THEOREM -- (a s5 + b s3)(c s5 + d s3) = ac P1 + (ad+bc) P2 + bd P3 identically (zero T5/T3 content of every exchange image); (iv) the RANK-3 CERTIFICATE -- channels E13 = (16,-96,144,0,0), E22 = (16,32,16,0,0), E00 = 225 E22, exchange matrix rank 2 with kernel 0, rank([M | A_fix]) = 3, annihilator certificate (Phi_T5, Phi_T3, Phi_P)(A_fix) = (0, 32, 72), and the naturalness images (25/4,-11/2,97/4,0,0) / (12,-40,76,0,0) with certificate (0,0); (v) the SO(16) AB SUM (15,-18,-15,-4,40) -- T5 does not even cancel, odd classes empty; (vi) the D8 NATIVE QUARTIC 16 T8 + 12 s8^2 with Killing 28 s8 -- no T3 structure. Mirrors v508. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4784)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* ---- (v214) QGEO.PILLOW.01: pillowcase reduction -- cross-ratio 2 => j=1728 => order-4 CM ---- *) Module[{chiorb, jl, x, y, curve, auto, xx, yy}, chiorb = 2 - 4 (1 - 1/2); (* orbifold Euler char of S^2(2,2,2,2) *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1726)
- [(* ==== v506 round: SEAM.CLOCK.RIGIDITY.01 -- clock rigidity, Route B of the v503 classification (Part A Moebius + Part B Fock). Exact content mirrored: (i) the COMPLETE SQUARE-ROOT SOLVE -- g^2 = deck in PGL2(C) has exactly two solutions z -> +-iz (tr != 0 forces diagonal with (a/d)^2 = -1; tr = 0 forces det = 0), both automatically of projective order 4; (ii) the D4 CENTER + ORDER-4 COUNT + the COUNTEREXAMPLE -- the mu4 stabiliser D4 = {i^k z, i^k/z} has exactly 2 order-4 elements (the clocks), both squaring to the deck, center = {id, deck}; the silver harmonic set {+-1, +-(3+2 sqrt 2)} has j = 1728 and full D4 but its 4-cycle squares to the CROSSING involution v/z, not the deck (deck non-central: 0 roots -- harmonicity alone insufficient); (iii) the Cl(16) IDENTITY -- on explicit 256x256 Jordan-Wigner gamma matrices, Utilde = prod_j (1 - g_j g_{j+8}) satisfies Utilde^2 = 256 g_1...g_16 EXACTLY (U^2 = (-1)^F, the forced nonsplit Z4), the R implementer squares to +256 (split control), and the volume element anticommutes with every gamma; (iv) the N-ARITHMETIC -- S4 element orders {1,2,3,4} (faithfulness kills n >= 5: max cyclic image order < n for n = 5..8), free orbits force n | 4, the cusp side kills n = 6 (deg(lam^5-1) = 5 != 3 = deg(lam^3-1)), transfer spectrum {1, 64/729, 1/729} with gap (2/3)^6, and the generic 4-set stabiliser V4 = {+-z, +-2/z} has exponent 2 (not even the deck has a root). The full 24-triple stabiliser enumeration and the A4/hexagonal profile stay Python-side (v506 Part A). Mirrors v506. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4394)
- [(* ==== v504 round: CELEST.WP5DB.01 -- WP5d-beta "split + strong additivity from the lattice", the two remaining KLM legs of complete rationality (the mu-index is v501). Exact content mirrored: (i) the GF2 SPAN THEOREM -- Majorana monomials multiply as labels in GF(2)^n (c_S c_T = +- c_{S xor T}), so span dims are exact set counts: with the shared boundary Majorana Even(A) v Even(B) = Even(A u B) EXACTLY (64/64, 256/256, 1024/1024), disjoint EXACTLY half (64/128, 256/512, 1024/2048) = index 2; (ii) the PIMSNER-POPA IDENTITY -- E(a) = (a + PaP)/2 gives E(a) - a/2 = PaP/2 symbolically on a full 4x4 matrix, and the attainment x = 1 + h (h = c_1 odd, h^2 = 1, PhP = -h, explicit gamma matrices) has E(x*x) - lam x*x = 2(1 - lam) - 2 lam h with spec(h) = {+-1}: nonnegative iff lam <= 1/2 = 1/[F:F_even] EXACTLY; (iii) the TWO-INTERVAL GROUP -- E4 over {1,PA,PB,PAB} on the uniform 4-sector vector gives E4(vv+) = I/4 exactly, so lam_E4 = 1/4 = 1/mu, and the index consistency (1/lam_PP)^2 = 4 = 1/lam_E4 = mu(SO(16)_1) = det Cartan(D8); (iv) the LAMBDA^2 COMPOUND -- the Wick cross-Gram of even bilinears is the second compound Minors[C, 2]: Cauchy-Binet functoriality Minors[A.B, 2] = Minors[A, 2].Minors[B, 2] on explicit integer matrices, Minors[diag(s), 2] = diag(s_a s_b) symbolically (singular values = products, the same ladder at doubled rate), and Minors[-C, 2] == Minors[C, 2] IDENTICALLY (the parity flip C -> -C is invisible to the even bilinears -- the exact orbifold split-inheritance mechanism); (v) the U(1) PP CONTROL -- charge dephasing on m modes has m + 1 sectors and the uniform-spread vector gives E_U(vv+) = P_diag/(m + 1), so lam = 1/(m + 1) -> 0 EXACTLY (m = 2, 3): infinite index. The lattice curves (deficit tables, Ising exponent p = 0.2444, elliptic-nome ladder, Klich-Levitov slope, ED validations) are numerical and stay Python-only (v504 S0/S2/S3/S5). Mirrors v504. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4132)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v496 round: CELEST.WP4.01 -- the (E8)_1 character E4/eta^8 vs the glue-equivariant E8[C^2] S-algebra (WP4 of CELEST.SEAM.01, the type mismatch head-on). Exact content mirrored: the character coefficients through q^6 with the q j = E4^3/eta^24 cross-check; the equivariant Hilbert series (60+128t+60t^2)/(1-t^2)^2 with the quadratic cumulative count 31 s^2 + 92 s + 60 and the SU(2)_+ slice; the two-sided jet-Fock mismatch f = (1,128,8436,381056) with strictly increasing f_n/chi_n (n = 1..12); the level-2 null ideal 27000 = 30^3 = h_vee^3; the boundary bridges (mu4 period sum 248, 248 not a tower dimension, loop Fock 897266); mirrors v496. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3257)
- [(* ==== v521 round: SEAM.BIT.RPBLIND.01 -- "free OS positivity does not see delta": the anti-linear census solvesets on M(delta), the counterwitness census, the V4 -> D4 closure (face #13), the cut/mark incidence, the continuum axis elimination + Cauchy-Stieltjes factorisation, the clock-tower clause and the hex/silver precondition controls. The 40-digit lattice Gram inertia spectra (N = 16 / N = 32) are Python-only by the suite convention. Mirrors v521. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7479)
- [(* ==== v495 round: CELEST.WP3.01 -- the Green-Schwarz axion coefficient lambda_g (Costello) vs c3 = 1/(8 pi) (WP3 of CELEST.SEAM.01, alignment test only). Exact content mirrored: the Deligne closed form lambda~^2 = 10 h_vee^2/(dim+2) = h_vee + 6 for all 8 algebras on Costello's list, with the dimension formula dim = 2(5h_vee-6)(h_vee+1)/(h_vee+6) and the fundamental-index values (h_vee+6)/i^2; the E8 alignment (kappa/c3)^2 = lambda^2/3 = 12 = |mu4| N_fam resp. 1/300 with kappa/c3 itself irrational; the so8 factor-2 slip (exact 3, printed 3/2); the look-elsewhere pass counts (smooth 8/8, lambda-integrality 2/8 = {sl3, e8}, g_car | h_vee 1/8 = {e8}, phi(h_vee) = rank 4/8, phi(h) = rank 5/8) and the e8 exponents = totatives of 30; mirrors v495. The Okubo root-sum identity itself is polynomial (verified in Python from explicit root systems); its arithmetic consequence lambda~^2 = h_vee + 6 is mirrored here. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3209)
- [(* ==== v511 round: CELEST.WP5E.DELTA2.01 -- WP5e-delta-2 "the full-tensor ledger" (the named escape route of the v508 exchange no-go, executed: the collapse is CONFIRMED full-tensorially, and one cubic door opens). Exact content mirrored: (i) the INNERNESS COUNT -- 240 glue roots with class split (52, 64, 60, 64), h = (2,2,2,2,2;0^4) and h' = (0^5;1,1,1,-3) reading the class mod 4 on ALL 240 roots, the class-0 roots splitting 40 pure D5 + 12 pure A3 with NO mixed root (g0 = d5 (+) a3 semisimple, NO u(1); root span rank 8), and class(-alpha) = -class(alpha); (ii) the BILINEAR HOM TABLE -- dim Hom_{g0}(g_j (x) g_j') by exact Kostant alternating sums on integer-scaled minuscule weight orbits: nonzero ONLY at j' = -j with dims (2, 1, 1, 1), all 12 charged pairs ZERO (the inner-torus theorem at arity 2); (iii) the TRILINEAR HOM TABLE -- all 15 non-neutral sector triples have Hom = 0 (arity 3) and the five neutral multisets carry dims (3, 2, 2, 1, 1); (iv) the UNIQUE SYMMETRIC SURVIVOR -- Inv(S^3 adj) = (0, 1) for (d5, a3) (so(10) has NO cubic Casimir, su(4) has exactly one), Inv(L^3 adj) = (1, 1), Inv(S^2 adj) = (1, 1), and on g0: Inv(S^3 g0) = 1, Inv(L^3 g0) = 2 (of the three g0-trilinears exactly ONE is totally symmetric: the su(4) d-symbol), with the dual machinery guard 4 x 4 = 0 vs 4 x 4bar = 1; (v) Q_dd BY TWO ROUTES -- explicit su(4) matrices: bracket vertices f(x,x,B) = 0, root-direction contractions d(x,x,E_ij) = 0, tadpole sum G^{-1}_ab d(x,B_a,B_b) = 0, and the exchange quartic Q_dd = sum d(x,x,B_a)(60 G)^{-1}_ab d(x,x,B_b) = (0, 0, -1/240, 0, 1/60) = (1/60)(T3 - P3/4) agreeing exactly with the hand route |x^2 - (tr x^2/4) 1|^2/60, so Phi_T3(Q_dd) = 1/60 != 0; plus Tr X^3 = 0 for antisymmetric X (no T5 analogue); (vi) the PSI CERTIFICATE + THE RELAXED SOLUTION -- E13 = (16, -96, 144, 0, 0), E22 = (16, 32, 16, 0, 0), E00 = 225 E22, A_fix = (9, -30, -15, 0, 32); M = [E13, E22, E00, Q_dd] has rank 3 with rank([M | A_fix]) = 4 (still unsolvable), psi = Phi_P - Phi_T3/4 annihilates all four channels with psi(A_fix) = 72 - 8 = 64, and the relaxed system {u, v, w, Q_dd} solves EXACTLY: A_fix = -u + 8v + 2w + 1920 Q_dd (rank 4, c_d = 1920 = |W(D5)| = 8 x 240); (vii) the CONTROLS -- SO(16)/D8: bilinears (adj adj, adj spin, spin spin) = (1, 0, 1), trilinears (1, 0, 1, 0), Inv(S^3 adj_d8) = 0 and Inv(L^3 adj_d8) = 1 (NO symmetric cubic, no odd sectors, no A3 block -- the delta-2 channel cannot even be posed); false g0 = d5+a2+u(1): bilinear entries (5, 2, 2) != (2, 1, 1) and Inv(S^3 g0_false) = 6 != 1; false sector content (16_s, 4bar): both pairings die (0, 0) vs the true value 1. Mirrors v511. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5379)
- [(* ---- (v127) ring resummation ---- *) Module[{proj, partial}, proj = {{1, 0, 0}, {0, 0, 0}, {0, 0, 0}}; checkExact["v127 log-det identity: det(1 - a P) = 1 - a (rank-1 P); series -ln(1-a) = a + a^2/2 + a^3/3 + ...", Simplify[Det[IdentityMatrix[3] - a proj] - (1 - a)] === 0 && Normal[Series[-Log[1 - a], {a, 0, 3}]] === a + a^2/2 + a^3/3]; partial[al_, kmax_] := 6 Sum[al^j/j, {j, kmax}]; checkExact["v127 ring ladder: k=1 ring = classical (2, 4 at weights 1, 2); k=2 ring = 1/3 at weight 1; partials below exact and monotone", partial[1/3, 1] == 2 && partial[2/3, 1] == 4 && 6 (1/3)^2/2 == 1/3 && partial[1/3, 8] < -6 Log[1 - 1/3] && partial[1/3, 2] > partial[1/3, 1]]; checkExact["v127 coupling cross-link + wall: kappa_seam = 8/24 = 1/3 = alpha_1 (kappa = alpha_1/pi); ring series diverges at alpha -> 1", 8/24 == 1/3 && Limit[-Log[1 - a], a -> 1, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v128) graded hull ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L903)
- [(* ==== v512 round: SEAM.TAU.FLAG.01 -- "the flag-transitivity equivalence web": the tau = i attack on the free RP seam circle. Test family M(delta) = {+-1, +-e^(i delta)}; bare mark-transitivity is delta-blind (pair-exchanging V4), FLAG transitivity <=> delta = pi/2 <=> tau = i. Six exact mirrors: (i) the V4/D4 census over five exact members incl. flag/arc orbit counts, (ii) the solveset equivalences + family identities, (iii) the odd-split closed form + arc Laplacian + K3 indicator, (iv) the twist mode identity + AB delta-blindness + j-rationality control, (v) the H4 centraliser rigidity (Schur), and (vi) the negative controls (hexagonal/silver/Z16 census/n = 3). Mirrors v512. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5675)
- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [(* ==== v509 round: CELEST.WP5E.EPS2.01 -- WP5e-epsilon-2 "the CPS level-from-flux dial" (verdict B; k = 1 from flux quantisation on the lockstep spheres, Costello-Paquette-Sharma Burns holography). Exact content mirrored: (i) the CPS PERIOD INTEGRALS -- the S^3 period of the brane backreaction 3-form = (2 pi i)^2 (pullback density -sin 2 theta) and the exceptional-sphere Kahler flux = 2 pi N exactly (flat part dies at t -> 0); (ii) the LEVEL ~ FLUX contraction 2N (symplectic bosons, N = 1, 2, 3) with the Dynkin normalisation T(so8 vector) = 1, T(adj) = 6; (iii) the PAIRING-MATRIX ENUMERATION -- row candidates (8, 6, 8), 48 unimodular solutions of P C^-1 P^T = C^-1, with effectivity P >= 0 exactly 2 = {identity, A3 diagram flip}; (iv) the FLUXES (64, 60, 64) = dim g_i with total 188 = 248 - 60, flip-invariant, one quantum per charged current; (v) the SECTOR-COUNTER dial #primaries((E8)_k) = (1, 3, 5, 10, 15, 27) for k = 1..6 from the affine marks -- exactly one sector iff k = 1; (vi) the LOCKSTEP THEOREM -- clock invariance forces a3 = a2 = a1 = 0, periods t(i-1)(1, i, i^2) with squared moduli 2t^2 equal on all three spheres, monodromy = pure phase i, det(A-1) = -4, and the negative probe Z^4 - Z (disc -27): 0/24 orderings lockstep; (vii) the NEGATIVE CONTROLS -- SO(16) fluxes (0, 60, 0) with ch2 defect -30 and condensation stuck at 4, A2 form det 3, glue diagonal 23/24 not integer, mu = 12 not a perfect square, Coxeter order 3 != 4. Mirrors v509. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4980)
- [(* ==== v515 round: CELEST.WP5E.M1.01 -- "the A3 Omega_N": milestone M1 of the CELEST.SEAM.01 back-reaction programme executed (SUCCESS on the preregistered v514 S8.1 criterion). Eight exact mirrors: (i) the residue-form identities (cover pullback 4 = |mu4|, clock phase i, weight ledger, EH anchor 2 = |Z2|), (ii) the twistor family closed (XY = Z^4 + 4 t0^2 la^2 Z^2 - t0^4 (1 - la^4)^2, O(2) reality, seam fibre = v493, self-mirror, CY-compatible clock lift), (iii) the period reduction + lockstep + clock covariance, (iv) the collision ledger (12 nodes exactly on the 8 eighth roots of unity, antipodal double nodes, clock orbits), (v) the BM anchor (2 pi i)^2 + the lens forcing N in 4Z, (vi) the source curve (four lines, K4 connectivity, forced uniform flux), (vii) the conifold nodes (Hessian det 512 t0^6, quadric rank 4, transversality), and (viii) the KILL probe + negative controls (forbidden family 0/24 vs 8/24, twelfth-root support, EH charge 2, diag(i,i) collapse). The exterior-derivative identity dK = 0 and the generic-profile sphere parametrisation stay Python-side in v515 (dict-based exterior algebra). Mirrors v515. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L6271)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v518 round: CELEST.WP5E.DELTA1.01 -- "the delta-1 chain decided: the derived chiral measure kills the delta-1 route" (delta-1b/1c/1d consolidated; an honest, decided NEGATIVE result with the v516 tension stated). Six exact mirrors: (i) the 16-component Weil system of the D5 (+) A3 discriminant module Z4 x Z4 with q = (5x^2 + 3y^2)/8 -- Gauss sums 2 zeta_8^5 x 2 zeta_8^3 = 4 = sqrt(16) (signature 0 mod 8 = rank E8), S symmetric + unitary, S^2 = C, (ST)^3 = S^2, S^4 = 1, T^8 = 1, tensor split S = S_D5 (x) S_A3 with factor signatures e(-5/8), e(-3/8); (ii) the two invariant Lagrangians (diagonal H and anti-diagonal H', both S- and T-fixed = two E8 gluings), 6 isotropic classes, P_H S P_H = (1/4) J and 3/4 of every S-image weight on the 12 shifted classes (why the naive 4-character rule fails); (iii) the KOBOUNDARY TEST on the recorded exact transport phases (t_p, s_p) of the dressed gauge blocks M = G[a,b] eta^{-8}: the SL(2,Z) relation defects c_{S^4}, c_{(ST)^3 S^-2}, c_{[S^2,T]} are (1, 1, 1) EXACTLY on all 15 sector pairs -- the mu4 multiplier system is a CHARACTER of the orbit stabilisers, not a genuine 2-cocycle; (iv) the Gamma_1(4) CHARACTER FORMULA lambda(gamma) = i^{2B + C/4} on the recorded loop matrices (all in Gamma_1(4), exact integer check), with all four equivalent monomial solutions agreeing; (v) the T-FIX MECHANISM: v502 vacuum energies E_b exact, the f1 f3 dressing shifts every T-fixed node by e(2E + 2E) = e(-1/6) and (-1) x e(-1/6) = e(1/3) = chi_4(T) UNIFORMLY, while f1f2f3 demands {chi_3, chi_4} and f2 demands {chi_5, chi_6} (inconsistent: only the twisted fibre block supplies one character); (vi) the misassignment controls (wrong form (x^2+y^2)/4: |Gauss|^2 = 64 != 16 and S^2 != C exactly; wrong signature sigma = e(-1/4): S^2 = e(-1/2) C exactly). The Harvey-Moore integrals, the SVD contraction solves, the theta covariance certificates and the block transport measurements are numerical (mpmath 30+ digits / numpy) and stay Python-only, flagged here. Mirrors v518. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L6875)
- [(* ==== v524 round: WOIT.BETA2.OS.01 -- "the OS quotient of the free system made explicit" (verdict SUCCESS, [C]-typed per contract precision (iii)). Four exact mirrors: (i) the euclidean-rotation preconditions (alpha_1^N = (-1)^F wrap arithmetic at N = 16 and N = 8) + the exact PD certificate identity sin^2(3pi/8) - sin(pi/8) sin(5pi/8) = 1/2; (ii) the Klein-Landau one-particle transfer forms tau_k on the shrinking domains at N = 16, k = 1..7: exactly Hermitian, odd k with exactly ZERO diagonal (the C(even) = 0 checkerboard), even k = 2j obeying the exact square identity tau_2j(a, b) = <alpha_j a, alpha_j b> entrywise; (iii) the clock identities (C(9) = C(7), C(11) = C(5), the transparency product formula sin(7pi/16) - sin(5pi/16) = 2 cos(3pi/8) sin(pi/16) > 0) + the N = 8 compressed clock spectrum EXACTLY {1, sqrt(2)-1} = {1, 1/delta_S} via the generalized eigenvalues of (tau_2, G) on the one-particle domain, with sin(pi/8)/sin(3pi/8) = sqrt(2)-1; (iv) the pre-declared KMS witnesses (C(1)/C(3) = 1 + sqrt(2) = delta_S at N = 8; -(C5-C7)((C3-C7)+(C5-C7)) < 0 exactly at N = 16, i.e. det(G - tau_4) < 0 on the odd one-particle clock block). The 37x37/16x16 H_phys Grams, the 40-digit inertia certificates, the spectral projections and the reconstructed rotation group are numerical (mpmath eighe), Python-only, flagged here. Mirrors v524. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7965)

## Honest status: bootstrap, not creation from nothing

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13520-13555](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13520) · `section:62801f711a0d267461ac` · section

What is genuinely shown : [formula in source] is an overdetermined fixed point of the [formula in source] closure (two independent Lie-theory conditions); the integer `` [formula in source] '' in [formula in source] is the carrier Coxeter [formula in source] [formula in source] rank; the discrete data closes a loop. The earlier landscape scan confirms [formula in source] is the unique value at which all hierarchies/f

Explicit source references:

- [verification/v108_pascal_ladder.py](../../../../verification/v108_pascal_ladder.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean#L1) · explicit_file_citation
- [verification/v499_p2_weights_deligne_bg.py](../../../../verification/v499_p2_weights_deligne_bg.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1) · explicit_file_citation
- [verification/v510_seam_bit_freedom.py](../../../../verification/v510_seam_bit_freedom.py#L1) · explicit_script_identifier
- [verification/v512_seam_tau_flag.py](../../../../verification/v512_seam_tau_flag.py#L1) · explicit_script_identifier
- [verification/v507_seam_bit_origin.py](../../../../verification/v507_seam_bit_origin.py#L1) · explicit_script_identifier
- [TFPT.Carrier.CarrierRankUniqueness.carrier_rank_pascal_unique](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L54) · explicit_lean_symbol
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [QGEO.REALIZE.01](../../../../verification/status_ledger.csv#L253) · explicit_claim_identifier · original status at linked ledger row
- [verification/v506_seam_clock_rigidity.py](../../../../verification/v506_seam_clock_rigidity.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v525 round: SEAM.BIT.TWISTBLIND.01 -- "the twist-state kill": the NINTH side-blind test on the v512 scoreboard (8 -> 9); the free-plus-twist class is exhausted. Three exact mirrors: (i) the integer incidence frame + the sigma o r = +-sigma congruence mechanism (swap axes: sigma o r = sigma => the twisted Gram is the diagonal unitary congruence D M D = spectrally invisible; fixing axes at pi/2: sigma o r = -sigma = the eta flip); (ii) the pi/2-existence solveset of the mark-fixing axes + the exact counterwitness census ((3+4i)/5 unimodular but NEVER a root of unity up to order 64 -- no lattice mark-compatible reflection at any dyadic refinement); (iii) the delta <-> pi - delta mirror equivariance (the lattice reflection maps the m-mark set EXACTLY to the (8-m)-mark set -- the exact mechanism behind the Casimir mirror symmetry ln|omega(D)|(m) = ln|omega(D)|(8-m) and behind pi/2 as the symmetric point of every invariant readout). The Pfaffian insertion spectra, the Bogoliubov 2-of-16 pattern census, the defect energy and the 40-digit inertia certificates are numerical (mpmath), Python-only, flagged here. Mirrors v525. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8058)
- [(* ---- (v107) quantum-clock target ---- *) checkExact["v107 per-l clock: l=0 (la-1)(la+2), l=1 la(la+1); l>=2 complex Re=-1/2", (Factor[la^2 + la + (0 - 2)] == (la - 1) (la + 2)) && (Factor[la^2 + la + (2 - 2)] == la (la + 1)) && (Re[la /. Solve[la^2 + la + 4 == 0, la]] == {-1/2, -1/2})]; checkExact["v107 cusp-ladder cross-link: decay set {0,-1,-2} = -Spec(Q diag(0,1,1)) = -N_fam x cusp", Module[{Vw = Q.DiagonalMatrix[{0, 1, 1}]}, Sort[Eigenvalues[Vw]] == {0, 1, 2}]]; checkExact["v107 exact target: (1/3)^6 = ((2/3)^6)^{log_{3/2}3}; ratio = 1 + log_{3/2}2", (FullSimplify[-6 Log[3] - (Log[3]/Log[3/2]) (6 Log[2] - 6 Log[3])] === 0) && (FullSimplify[Log[3]/Log[3/2] - (1 + Log[2]/Log[3/2])] === 0)]; check["v107 bend log_{9/4}(3) = 1.354756; seam coupling 1/(3Pi) = 0.106103", Log[3]/Log[9/4], 1.3547556457`10, 10^-9]; (* ---- (v108) Pascal ladder ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L471)
- [(* ==== v512 round: SEAM.TAU.FLAG.01 -- "the flag-transitivity equivalence web": the tau = i attack on the free RP seam circle. Test family M(delta) = {+-1, +-e^(i delta)}; bare mark-transitivity is delta-blind (pair-exchanging V4), FLAG transitivity <=> delta = pi/2 <=> tau = i. Six exact mirrors: (i) the V4/D4 census over five exact members incl. flag/arc orbit counts, (ii) the solveset equivalences + family identities, (iii) the odd-split closed form + arc Laplacian + K3 indicator, (iv) the twist mode identity + AB delta-blindness + j-rationality control, (v) the H4 centraliser rigidity (Schur), and (vi) the negative controls (hexagonal/silver/Z16 census/n = 3). Mirrors v512. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5675)
- [(* ==== v507 round: SEAM.BIT.ORIGIN.01 -- the tautology attack on the v506 alignment bit, executed and refuted (Part A torus origin + Part B fermion dichotomy). Exact content mirrored: (i) the HALF-PERIOD DESCENT -- the fixed points of w -> -w on C/(Z + tau Z) are the 4 half-periods (2w in Lambda <=> coefficients in {0, 1/2}; the 1/3-control fails), a translation t_c descends iff 2c in Lambda (exactly the 3 nonzero half-periods), and the descended map sigma_i(x) = e_i + (e_i-e_j)(e_i-e_k)/(x-e_i) satisfies the exact curve-lift identity prod(sigma_i - e_l) = psi_i^2 prod(x - e_l) with RATIONAL psi_i, closing to Klein V4 symbolically; (ii) the CORE SOLVE -- the pair cross-ratio condition CR = -1 solves to lambda = -1 (sigma_1), 2 (sigma_2), 1/2 (sigma_3) exactly, union = the harmonic orbit with j = 1728, against j(3) = 21952/9 and j(hex) = 0; (iii) the STABILISER COUNTS -- the complete 24-triple enumeration gives (|Stab|, #involutions, #free) = (4,3,3) generic / (8,5,3) harmonic / (12,3,3) hexagonal, and in ALL three types the free involutions are EXACTLY the three sigma_c (the deck CLASS is forced); (iv) the CM FIXED POINT -- mult-by-i mod 2 fixes exactly the half-period (1,1) = c* = (1+tau)/2 while mult-by-rho 3-cycles all three, the lemniscatic clock ghat: x -> (x-1)/(x+1) needs the curve-lift factor psi = 2i/(x+1)^2 (the CM unit; t^2+1 irreducible over Q) and squares to the central -1/x; (v) the Cl(16) DICHOTOMY -- on explicit 256x256 Jordan-Wigner gammas the central implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the EDGE implementer Utilde_e = P_3 (g1+g5)(g2+g4)(g6-g16)(g7-g15)(g8-g14) (g9-g13)(g10-g12) implements the NS edge reflection and squares to the SCALAR +2^7 (split), and in the 32-element NS dihedral lift group the central deck has EXACTLY 2 square roots (the +-quarter shifts) vs 0 for the edge deck; (vi) the SILVER BIJECTION CENSUS -- all 8 mark bijections {+-1, +-(3+2 sqrt 2)} -> {0, 1, -1, inf} carry the deck z -> -z to the EDGE sigma_2/sigma_3 (never the central sigma_1), while all 8 mu4 bijections carry it to the CENTRAL sigma_1. The v493 circularity-audit direction and the 28/21 arrangement census stay Python-side (v507). Mirrors v507. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4545)
- [experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean#L1)
- [(* ==== v506 round: SEAM.CLOCK.RIGIDITY.01 -- clock rigidity, Route B of the v503 classification (Part A Moebius + Part B Fock). Exact content mirrored: (i) the COMPLETE SQUARE-ROOT SOLVE -- g^2 = deck in PGL2(C) has exactly two solutions z -> +-iz (tr != 0 forces diagonal with (a/d)^2 = -1; tr = 0 forces det = 0), both automatically of projective order 4; (ii) the D4 CENTER + ORDER-4 COUNT + the COUNTEREXAMPLE -- the mu4 stabiliser D4 = {i^k z, i^k/z} has exactly 2 order-4 elements (the clocks), both squaring to the deck, center = {id, deck}; the silver harmonic set {+-1, +-(3+2 sqrt 2)} has j = 1728 and full D4 but its 4-cycle squares to the CROSSING involution v/z, not the deck (deck non-central: 0 roots -- harmonicity alone insufficient); (iii) the Cl(16) IDENTITY -- on explicit 256x256 Jordan-Wigner gamma matrices, Utilde = prod_j (1 - g_j g_{j+8}) satisfies Utilde^2 = 256 g_1...g_16 EXACTLY (U^2 = (-1)^F, the forced nonsplit Z4), the R implementer squares to +256 (split control), and the volume element anticommutes with every gamma; (iv) the N-ARITHMETIC -- S4 element orders {1,2,3,4} (faithfulness kills n >= 5: max cyclic image order < n for n = 5..8), free orbits force n | 4, the cusp side kills n = 6 (deg(lam^5-1) = 5 != 3 = deg(lam^3-1)), transfer spectrum {1, 64/729, 1/729} with gap (2/3)^6, and the generic 4-set stabiliser V4 = {+-z, +-2/z} has exponent 2 (not even the deck has a root). The full 24-triple stabiliser enumeration and the A4/hexagonal profile stay Python-side (v506 Part A). Mirrors v506. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4394)
- [(* ==== v510 round: SEAM.BIT.FREEDOM.01 -- the freedom attack on the v506/v507 alignment bit: the POSITION half of the bit is topology. Exact content mirrored: (i) the DIHEDRAL CENSUS -- on the refined 2N-point seam circle D_16 has 17 involutions with EXACTLY ONE free (the antipodal shift by 8) and all 16 reflections have exactly 2 circle fixed points (8 site-axis + 8 edge-axis; robustness N = 8, 12; odd control N = 9: zero free), plus the quotient topology chi(C/antipode) = 0 (circle) vs chi(C/reflection) = 1 (interval, 2 boundary corners); (ii) the AUT COMPLETENESS -- Aut(C_8) = D_8 by brute force over all 8! = 40320 permutations and Aut(C_16) = D_16 by degree-2 propagation (all 32 candidates), so the census covers ALL circle symmetries; (iii) the Cl(16) DICHOTOMY CENSUS -- on explicit 256x256 Jordan-Wigner gammas the free deck's NS implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the implementers of ALL 16 reflections exist (one of the two spin lifts +-R) and square to SCALARS {2^7 (site-axis), 2^8 (edge-axis)} (split): NONSPLIT <=> FREE over the complete census; root dichotomy 2 (the +-quarter shifts) vs 0 total over all 16 reflections; (iv) the REAL-STRUCTURE TABLE -- the deck-commuting antiholomorphic involutions solve symbolically to exactly two families (M diagonal: mu conj z, fix line through the poles; M antidiagonal: mu/conj z, fix circle |z| = sqrt mu), and the unique mark-fixing real structure per configuration is equatorial/FREE for mu4 and generic-unit, real-axis/NOT-free for silver and generic-real, and NONEXISTENT for the hexagonal frame; (v) HARMONIC + FREE => mu4 -- the deck-pair cross-ratio (1-b)^2/(1+b)^2 = -1 solves exactly to b = +-i, with the lambda table (2, 1/2, 3/4, 5/4) real and the hexagonal lambda complex; (vi) the HONEST COUNTERWITNESSES -- the discrete witness {0,1,8,9} (shift-invariant, crossing, but not quarter-shift-invariant) and the continuous witness {+-1, +-(3+4i)/5} (pair cross-ratio -1/4, j = 148176/25 != 1728, clock does not preserve): the Fock dichotomy measures the CLASS, not the modulus. The Moebius/Klein covering models and the pillowcase branch control stay Python-side (v510). Mirrors v510. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5155)
- [(* ==== v499 round: P2.TYPING.01 -- the P2 weight-typing postulate hardened: the anchor a = (1,1,2) as the Birkhoff-Grothendieck splitting exponents of the Deligne canonical extension E of the flavor connection (types the v491 check-9 residual). Exact content mirrored: (i) partition enumeration under the full typing (BG dictionary h^0 = 0 <=> a_i >= 1, exhaustive window) + the naive- typing negative control (h^1(E') = 3 forces deg -6, three splittings, e2 never 5) + the h^1 discrepancy (h^1(anchor bundle) = 1 != 3); (ii) the Deligne residue-trace degree (cusp exponents {0,1/3,2/3} = the unique lift of spec(lam^3 - 1) to [0,1), trace 1 per mark, deg E = -4, par-deg 0, witness A0* charpoly); (iii) the Schur-Horn permutohedron integer points {(2,2,0),(2,1,1)} with h^0 = 0 killing {2,2,0}; (iv) the Biswas Z3-cover degree arithmetic (genus 2, eigensheaves O(-2)^2, chi cross-check, regular-rep weights, the decomposable model {0,2,2} with h^0 = 1 = the unstable companion; deck double genus 1, j = 1728); (v) the n-mark formula e2 = (n-2)(n+1)/2 = 5 only at n = 4. The sympy symbolic parts (H^1 residue basis, monodromy group closure |<U,M0>| = 24, the 324-case stability skeleton) stay Python-side (v499). Mirrors v499. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3620)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)

## Open items and the [formula in source] -slice scan

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13556-13558](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13556) · `section:be646416cec79e6de5b1` · part

No opening prose excerpt; see the source.

## The honest open-items list

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13559-13627](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13559) · `section:840d8edcd2db5226531d` · section

This is the complete current ledger of what is not fully closed, graded by how hard the gap is.

Explicit source references:

- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_file_citation
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v69_d4_q_geometry.py](../../../../verification/v69_d4_q_geometry.py#L1) · explicit_script_identifier
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *) checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}", Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]]; checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}", Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} && Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]]; (* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L329)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)

## The [formula in source] -slice scan: results (honest hit / miss)

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13628-13677](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13628) · `section:e96028e126dc568728a9` · section

All seven maximal slices of [formula in source] were scanned for the unassigned quantities. The rule was a meaningful (low-complexity) compiler/slice expression matching to [formula in source] ; matches that need a free fitted factor are reported as misses.

## Following the [formula in source] lead: cross-slice consistency

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13678-13715](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13678) · `section:6cc588ee5e3b1e4ba5d3` · section

The one scan lead worth following is [formula in source] . Splitting [formula in source] the [formula in source] branching [formula in source] decomposes exactly as:

## Appendix: computational verification

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex:13716-13731](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/sources/input_5_tfpt_3_e8_audit_bootstrap.tex#L13716) · `section:6aa0234a2106db691b55` · section

The audit/bridge identities of this document (marked , ) are re-derived from [formula in source] and machine-checked by the suite in the repository folder verification/; the inline tags [verification/ [formula in source] ] point to the exact script. Relevant here: v1_e8_glue.py — the [formula in source] glue [formula in source] (load-bearing). v4_flavor_matrix.py — the spectral selector [formula in source] , minors [

Explicit source references:

- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_file_citation
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_file_citation
- [verification/README.md](../../../../verification/README.md#L1) · explicit_file_citation
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)

## Front matter / support

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:1-119](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L1) · `section:1dfe8135293890933f37` · frontmatter

unicodehyperref hyphensurl dvipsnames,svgnames,x11namesxcolor ngerman, 10pt, a4paper, ]article Scale=MatchLowercase Ligatures=TeX,Scale=1

## Die fehlende halbe Drehung - einfach erklärt

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:120-124](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L120) · `section:928d4fbfd899e6845191` · section

No opening prose excerpt; see the source.

## Das Bild

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:125-140](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L125) · `section:453e5f58c4a34da852f9` · subsection

Stell dir vier Stationen im Kreis vor. Zwischen benachbarten Stationen können zwei Fermionen gemeinsam in einen anderen Zustand übergehen und zurück. Bislang haben wir oft nur das Verhalten dieser Paare angeschaut.

## Was dadurch besser wird

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:141-159](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L141) · `section:f2d497c409fb36e7fca8` · subsection

Ohne die Verdrehung bleibt im gewählten Viererzyklus ein ganzer Fermionbereich unbeteiligt. Wie ein Zimmer, das an keine Leitung angeschlossen ist. Unterschiedliche Belegungen dieses Zimmers kosten keine zusätzliche Energie. Deshalb kann das ganze Modell so keinen einzigen eindeutig bevorzugten Grundzustand haben.

## Und kann darin etwas wirklich angeregt werden?

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:160-173](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L160) · `section:63a1ad054eb1eaaf710b` · subsection

Ja, ebenfalls innerhalb eines bewiesenen kleinen Bereichs. Entfernt man ein ursprüngliches Fermion mit einer bestimmten Clock-Phase aus genau diesem Grundzustand, landet fast die gesamte Antwort auf einer einzelnen isolierten Energielinie. Je nach Clock-Phase gibt es zwei verschiedene niedrige Linien. Für den passend aufgelösten Modus sind mehr als 99.992 Prozent des Entnahmespektrums kontrolliert.

## Wo die große Hoffnung liegt

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:174-182](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L174) · `section:14b61fb216a636573aff` · subsection

Vielleicht haben wir nicht eine riesige zusätzliche Maschine übersehen, sondern beim Übergang zu den sichtbaren Paargrößen eine kleine, entscheidende Information weggeworfen. In diesem Test wirkt dasselbe Umlaufvorzeichen auf die Kopplung, die Auswahl des Grundzustands und die Anregungen. Es verbindet also mehrere Baustellen tatsächlich.

## Wo die Grenze liegt

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:183-195](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L183) · `section:5fad6c20f4e2391a1b13` · subsection

Wir haben die vier Stationen und ihre gemeinsame Quellenregel für diesen Test festgelegt. Noch nicht gezeigt ist, dass die ursprüngliche TFPT genau diese Regel erzeugt. Auch die bewiesene Kopplung ist viel kleiner als unser bisheriger Prüfwert. Und vier Stationen sind keine abgeleitete dreidimensionale Welt.

## Was die beiden neuen Texte zusätzlich klären

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:196-219](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L196) · `section:597ff3e9084bbe159d91` · subsection

Ihr Vorschlag, das Ganze über alle möglichen Handlungsfolgen und ihre Antworten zu beschreiben, ist sinnvoll: Statt getrennte Schatten zu sammeln, beschreibt man den gemeinsam ausführbaren Prozess. Aber ein vollständiges Buch aller Antworten ist noch keine einfache Regel, die dieses Buch erzeugt.

## Was jetzt den Unterschied machen würde

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex:220-241](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Einfach_2026-09-15_v1.6.10.tex#L220) · `section:0b4b7b5936fda58fa110` · subsection

Die Fortsetzung hat hier noch eine einfache Regel gefunden. Wenn linke und rechte Nachbarstation verschieden stark beitragen dürfen, funktioniert auch ein unverdrehtes Gegenmodell. Der Clock allein bestimmt das also nicht. Fordert man aber, dass dieselbe Links-rechts-Spiegelung auch den Paarübergang unverändert lässt, müssen beide Seiten gleich stark beitragen. In dieser kleinen Quellenfamilie bleibt dann ohne freie 

## Front matter / support

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:1-119](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L1) · `section:815b7c56398bfa4b858b` · frontmatter

unicodehyperref hyphensurl dvipsnames,svgnames,x11namesxcolor ngerman, 10pt, a4paper, ]article Scale=MatchLowercase Ligatures=TeX,Scale=1

## TFPT / Universalraum - Update v1.6.10

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:120-131](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L120) · `section:c9ec038ee9497d6128e6` · section

September 2026. Bezug: Hauptfassung v1.6.9 und die neu geprüfte Arbeit „Gemeinsame Quelle``, Fortsetzung 1.2.

## Die neue Verbindung

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:132-144](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L132) · `section:6f28b5063205b42ff476` · subsection

TFPT enthält bereits einen fermionischen Vierteldrehungsclock mit [formula in source] . Das neue Quellpaper zeigt gleichzeitig, dass Paarantworten ein solches Vorzeichen verlieren können. Diese beiden Befunde wurden nun an derselben festgelegten Viererquelle mit dem unveränderten inneren Tensor W zusammengeführt.

## Was neu bewiesen wurde

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:145-182](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L145) · `section:50ca9c323361bdf593b4` · subsection

Die periodische Variante besitzt 64 völlig ungekoppelte Fermionmoden; die antiperiodische besitzt keine. Ihre gesamten eingeschränkten bosonischen N=2-Antworten sind dennoch gleich. Ein zusätzlicher Fermion-Eingang macht den Unterschied ladungsneutral sichtbar. Für denselben gemischten Einboson-Einfermion-Eingang unterscheiden sich die Bosonrückkehrwahrscheinlichkeiten erstmals durch [formula in source] . Für [formul

## Was nicht verwechselt werden darf

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:183-196](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L183) · `section:ddfd78f3f4c7420fe84b` · subsection

Der bisherige Prüfpunkt [formula in source] liegt außerhalb beider neuen Bereiche. Der neue N=256-Grundzustand ist nicht der alte N=64-Grundzustand einer einzelnen Bank. Der N=3-Vergleich ist ein Diagnoseexperiment und nicht die Grundzustandsantwort. Die C8-Hebung wird nicht mit dem inneren Perioden-sechs-Clock gleichgesetzt.

## Zwei methodische Korrekturen

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:197-211](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L197) · `section:4130aba54f38215c15b7` · subsection

Die volle assoziative Erzeugung durch quadratische Cliffordwörter ist nicht volle dynamische Steuerbarkeit. Ein einzelner zusätzlicher quartischer Generator würde unter gewährten quadratischen Kontrollen genügen; seine native Realisierung ist nicht bewiesen.

## Die beiden zuletzt eingegangenen Perspektiven

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:212-243](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L212) · `section:a06a64f4c701c6817184` · subsection

Der vollständige positive Prozesskern ist ein tragfähiger Rekonstruktionsrahmen, bestimmt aber seine eigenen Daten und Instrumente nicht. Positivität allein genügt ohne passende Multiplikationsrelationen nicht. Gleicher Grundzustand und gleiche statische Beobachtungen bestimmen zudem keine eindeutigen Anregungsenergien.

## Weitergerechnet: Auswahl durch gemeinsame Spiegelung?

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:244-266](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L244) · `section:6057ad46ed5a131fc16a` · subsection

Clock und Grundzustand wählen die Verdrehung allein nicht: Die reelle Quelle [formula in source] hat ebenfalls keinen freien Fermionbereich und bei genügend kleiner Kopplung einen eindeutigen globalen Grundzustand. Sie besitzt allerdings eine andere Paarmatrix als die fixierte gleichstarke Mischung.

## Priorität

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex:267-282](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/TFPT_Universalraum_Spinlift_Update_2026-09-15_v1.6.10.tex#L267) · `section:37dd70a2a8819994fde7` · subsection

Zuerst die gemeinsame Spiegelungswirkung der TFPT-Seam auf Fermionorte und Paarübergänge prüfen; daran den zustands- und operatorverträglichen Quellenanschluss entscheiden. Danach den Kopplungsbereich erweitern und dieselbe geladene Antwort in einer Größenfolge untersuchen. Das ist eine kleinere, konkrete Forschungsaufgabe als die Suche nach immer weiteren passenden Zahlen.

## Front matter / support

[experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/header.tex:1-42](../../../../experiments/theory-contracts/universalraum-spin-lift-basics-20260915/tmp/pdfs/header.tex#L1) · `section:9cb65241c970e3ed6a2e` · frontmatter

No opening prose excerpt; see the source.

## Thermodynamic Dynamics for the TFPT Finite-Range\\ Master-Hamiltonian Class

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:1-71](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L1) · `section:0cf9d4ac86d877bda3c0` · frontmatter

colorlinks=true, linkcolor=blue!55!black, citecolor=blue!55!black, urlcolor=blue!55!black

Explicit source references:

- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row

## The concrete uniformly local class

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:72-73](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L72) · `section:3b8afe4964a445ff9fc8` · section

No opening prose excerpt; see the source.

## Ambient tensor-product algebra

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:74-154](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L74) · `section:c55d5c0e208b3eaef29d` · subsection

Let [formula in source] with graph distance [formula in source] and coordination [formula in source] . For a finite [formula in source] , put [formula in source] One cell contains the four representative physical edge modes, a mirror Fock factor, the two positively oriented outgoing finite-group gauge links, and a four-state seam clock. Thus [formula in source] The DET4 numerical analogue has dimension [formula in so

Explicit source references:

- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_file_citation

## Uniform constants

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:155-182](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L155) · `section:531637056ba3e998a467` · subsection

Define the finite-range interaction moment [formula in source] There are two assigned electric links, four plaquettes, and four bonds incident on a square-lattice cell. Consequently [formula in source] These bounds are independent of [formula in source] . More generally, bounded degree, finite [formula in source] , finite local dimension and finite [formula in source] are the class hypotheses; the displayed numbers a

## The Lieb–Robinson theorem and explicit TFPT velocity

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:183-267](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L183) · `section:974106578e6767d57f9b` · section

Let [formula in source] be a graph, let every local Hilbert space be finite dimensional with a uniform dimension bound, and let a self-adjoint interaction satisfy [formula in source] For every finite [formula in source] , define [formula in source] . If [formula in source] , [formula in source] , and [formula in source] , then, uniformly in [formula in source] , [formula in source] Thus an admissible Lieb–Robinson ve

## Norm thermodynamic limit

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:268-343](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L268) · `section:95b9cfbad79a7cc11ada` · section

For every [formula in source] , the net [formula in source] exists in norm, uniformly for [formula in source] in compact real intervals and independently of the exhausting sequence. It extends uniquely to a strongly continuous one-parameter group of [formula in source] -automorphisms of [formula in source] .

## Gauss law and the correct consistent family

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:344-406](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L344) · `section:e2e81b99b843b044bd1e` · section

Let [formula in source] be the group of finitely supported local gauge transformations on the ambient field algebra, and let [formula in source] denote its action. Define [formula in source] The electric and plaquette terms are gauge invariant; the hopping contains its parallel transporter; the determinant projector is a Spin(10) singlet; and the seam charge is neutral as assembled. Thus [formula in source]

## Existence of equilibrium states

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:407-467](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L407) · `section:93def08f20e0c9beb6ad` · section

The infinite-volume system [formula in source] , and its invariant subalgebra [formula in source] , have at least one ground state. For every [formula in source] , they have at least one [formula in source] -KMS state.

## Numeric twin

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:468-512](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L468) · `section:cd90c6924a0df8bd3f36` · section

The companion [formula in source] uses the exact nearest-neighbour physical-edge sector of the assembled model while comparing it against the complete class constant earlier IR-universality witness. It reports: [formula in source] For the one-site projector, [formula in source] , and nested open volumes, the specialization of [formula in source] The zeros are numerical precision statements, not analytic finite-speed 

Explicit source references:

- [experiments/tfpt-discovery/lieb_robinson_witness_probe.py](../../../../experiments/tfpt-discovery/lieb_robinson_witness_probe.py#L1) · explicit_file_citation

## Combined theorem and exact boundary

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:513-562](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L513) · `section:fe2cf43aaf468a3fd438` · section

For the TFPT master-Hamiltonian class finite-dimensional local factors and coefficients of Table the finite-volume dynamics satisfy the uniform Lieb–Robinson bound [formula in source] ; the thermodynamic-limit dynamics exist in norm on all local observables and define a strongly continuous automorphism group; the group restricts consistently to the Gauss-invariant quasilocal algebra, with projector compatibility in t

## Conclusion

[experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex:563-618](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/external/exchange/source/articles__2026-08-30__tfpt_thermodynamic_dynamics_en.tex#L563) · `section:c0e96880a60b78a3dc4e` · section

The amended contract makes the continuum limit optional but the thermodynamic limit mandatory. The latter is now proved at the Hamiltonian-class level for the concrete finite-group, finite-local-space TFPT assembly. The proof is insensitive to finite-volume boundary shape and does not infer thermodynamics from a finite scan. Its explicit velocity is conservative, while the numerical witness checks the expected cone, 

## Was mit Universalraum gemeint ist

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L1) · `section:1ac723376fcd16df94bd` · chapter

No opening prose excerpt; see the source.

## Kein zusätzlicher Behälter

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:3-9](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L3) · `section:68300014fb2475068c62` · section

Wenn wir gewöhnlich von Raum sprechen, denken wir an eine Bühne: Hier steht ein Tisch, dort fliegt ein Teilchen, und die Uhr läuft im Hintergrund. Die Universalraum-Idee dreht diese Reihenfolge um. Vielleicht sind zuerst Beziehungen und mögliche Veränderungen da. Eine Bühne mit Entfernungen und einer Uhr entsteht erst, wenn viele dieser Beziehungen ein beständiges Muster bilden.

## Die fünf Bestandteile

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:10-33](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L10) · `section:56b7af722c8bbe8ebdaa` · section

Eine ausreichend konkrete Fassung benötigt mindestens: Zustände: Was ist gegeben, einschließlich relevanter Korrelationen? Operationen: Welche Veränderungen sind erlaubt? Zusammensetzung: Wie dürfen Vorgänge hintereinander und nebeneinander verbunden werden? Aufzeichnungen: Welche Spuren bleiben erhalten und dürfen später erneut benutzt werden? Auslesung: Welche Ergebnisse sind mit welchen Wahrscheinlichkeiten beobac

## Wann zwei Beschreibungen wirklich dasselbe sagen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:34-46](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L34) · `section:d5cd533c817ab848555a` · section

Zwei Uhren können jetzt beide zwölf anzeigen und trotzdem verschieden weiterlaufen. Eine ist aufgezogen, die andere steht kurz vor dem Stillstand. Wer nur das Zifferblatt betrachtet, sieht den Unterschied noch nicht. Ein späterer Blick unterscheidet sie.

## TFPT als Grammatik und als Übersetzung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:47-62](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L47) · `section:45b19e11384dd7b5e54c` · section

TFPT liefert eine reichhaltige Grammatik: Träger, Darstellungen, Gitter, markierte Symmetrien, Projektoren und kurze wiederverwendete Zahlenformeln. Die Metapher vom Compiler meint eine Übersetzung zwischen diesen Beschreibungen. Sie sagt nicht, dass bereits ein kosmisches Computerprogramm identifiziert ist.

## Wie die Idee entstanden ist

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:63-63](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L63) · `section:fdb2005b26b1814cc82d` · chapter

No opening prose excerpt; see the source.

## Vom Wiedererkennen zur gemeinsamen Ursache

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:64-68](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L64) · `section:7fb9c7b945845a89d3cb` · section

Die Anhänge zeigen keine einzige plötzliche Entdeckung, sondern eine Folge von Verschiebungen der Frage. Zuerst fällt auf, dass kleine geometrische und algebraische Daten in verschiedenen Rechnungen wiederkehren. Der Fünferträger führt zu einem 16-dimensionalen Spinor; die passenden Gitterfaktoren führen zu [formula in source] ; ein komplexer Viererträger zeigt 60 besondere Strahlen. Clocks, Ladungszuordnungen und Fl

## Warum Spektren und Einzelbilder nicht genügten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:69-73](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L69) · `section:cb7ed0d105714c1bc904` · section

Die älteren, in S09 zusammengefassten Untersuchungen fanden mehrere Räume, die man nicht einfach gleichsetzen darf: eine Kommutantenalgebra, einen Majorana-/Fockraum, einen festen Teilchensektor, eine verdoppelte Familienbeschreibung und eingeschränkte Kanalmodelle. Manche lokalen Ansichten ließen verschiedene gemeinsame Dynamiken zu. Andere Tests konnten unter engeren Voraussetzungen ausgewählte Zustände bestimmen.

## Die dokumentierte Entwicklung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:74-88](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L74) · `section:7fcb92d0d09d7a794a33` · section

L30mmL55mmL65mm Etappe& Erkenntnis& Neue Frage\\ Vorarbeiten, in S09 rückblickend beschrieben&Mehrere algebraische Ansichten, Lorentzkegel, verborgene Richtungen, lokale und gemeinsame Kanäle.&Welche Informationen gehen beim Auslesen verloren?\\ 13. September: Compiler-Manuskript S09&60 Strahlen, 15 Kontexte, zwei Schatten desselben Prozesses; explizite Vormessung mit Register.&Wer wählt Kreuzkopplung, Kontextgewicht

## Was von der anschaulichen Ursprungserzählung bleibt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex:89-96](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/01_idee.tex#L89) · `section:65a1ce1de56942f22629` · section

Der eingefügte Gesprächstext spricht von einem Regelwerk mit Logbuch und von Raum und Materie als Mustern seiner Spuren. Das trifft die Forschungsintuition. Die Formulierung „TFPT ist die Grammatik, der Universalraum die Ausführung“ ist als Einstieg hilfreich.

## Die mathematischen Bauteile von TFPT

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex#L1) · `section:ab8115dfeb52d25c0b05` · chapter

No opening prose excerpt; see the source.

## Die Ausgangsannahmen enthalten mehr als zwei Zahlen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex:3-12](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex#L3) · `section:965df915fe3244035611` · section

Die historische Kurzfassung nennt [formula in source] und einen fünfteiligen Träger. Vollständig gelesen setzt P1 einen orientierten Rand beziehungsweise eine Naht, einen geeigneten positiven Kern und eine Normierung voraus. P2 setzt Art und Struktur des Trägers voraus; die spätere [formula in source] -Lesart wird mit Farb- und schwachen Richtungen verbunden. Orientierung, Positivität, komplexe Struktur und Markierun

## Vom Fünferträger zum Spinor

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex:13-26](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex#L13) · `section:0e7eb43eac9358040547` · section

Bei fünf komplexen Richtungen kann man antisymmetrische Kombinationen von null, zwei und vier Richtungen bilden. Zusammen erhält man Das ist die gerade Spinorstruktur von [formula in source] . „Antisymmetrisch“ heißt hier: Beim Vertauschen zweier Plätze wechselt ein Vorzeichen. Es ist eine genaue Bauvorschrift, keine bildliche Ähnlichkeit.

## Warum die Verklebung wirklich zu E [formula in source] 8 führt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex:27-57](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex#L27) · `section:bd56358ac4b3afeb5b4f` · section

Die beiden positiven Wurzelgitter [formula in source] und [formula in source] besitzen Determinante vier und Diskriminantengruppe [formula in source] . Eine Diskriminantengruppe beschreibt hier die möglichen Restklassen, mit denen man das Gitter ohne Verlust der Ganzzahligkeit ergänzen kann. Für passende Generatoren gilt modulo eins Diagonal gekoppelt ist die Summe [formula in source] ganzzahlig. Die vier gemeinsamen

## Wurzeln und Generatoren sind verschiedene Zählungen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex:58-85](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex#L58) · `section:031ae27da731df5e0775` · section

Die 240 Wurzeln sind besondere Vektoren in einem acht-dimensionalen Raum. Hinzu kommen acht Cartanrichtungen, sodass die Lie-Algebra 248 Dimensionen besitzt. Unter [formula in source] lautet ihre komplexe Zerlegung L47mmrY Sektor& Wurzeln& Generatoren einschließlich Cartan\\ [formula in source] &40& [formula in source] \\ [formula in source] &12& [formula in source] \\ Gemischter Vektorsektor&60& [formula in source] 

## Das endliche Fenster: 60 Strahlen und 15 Kontexte

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex:86-92](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex#L86) · `section:796380daf95ec05ff1ae` · section

Ein Strahl ist ein reiner Zustand ohne seine insgesamt irrelevante globale Phase. Ein Kontext ist eine vollständige orthogonale Viererbasis: vier mögliche Ausgänge einer scharfen Messung. Im markierten komplexen Viererträger ergeben sich 60 besondere Strahlen in 15 solchen Kontexten. In der gewählten Kodierung sind dies die reinen Zwei-Qubit-Stabilizerzustände und ihre vollständigen Pauli-Kontexte. S09, Kap. 3 und 9

## Die Räume im Größenvergleich

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex:93-108](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/02_algebra.tex#L93) · `section:dcc415ad1f88d248f358` · section

L45mmL31mmL74mm Objekt& Größe& Was die Zahl zählt\\ [formula in source] -Wurzeln&240&Besondere Vektoren, keine 240 unabhängigen Raumrichtungen.\\ [formula in source] &248&Dimension der Generatoralgebra.\\ Ein Viererträger& [formula in source] &Zustände eines Ququarts, hier als zwei Qubits kodiert.\\ Vier solche Träger& [formula in source] &Komplexe Hilbertraumdimension der Zelle.\\ 15 allgemeine CQ-Blöcke& [formula i

## Ein gemeinsamer Prozess mit zwei Schatten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L1) · `section:11dd24aa21b86cc0953d` · chapter

No opening prose excerpt; see the source.

## Eine einzelne Messrunde

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:3-19](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L3) · `section:160756f6e39172ceff81` · section

Man beginnt mit einem Strahl [formula in source] : Kontext [formula in source] , Ergebnis [formula in source] . Dann wählt man einen nächsten Kontext [formula in source] und misst in dessen Basis. Die Quellkonstruktion benutzt [formula in source] ist eine [formula in source] -Inzidenzmatrix. Sie erlaubt den aktuellen Kontext und sechs andere, mit ihm inzidente Kontexte. Jeder erlaubte Nachfolger erhält in dieser spez

## Kontext und Quantenzustand als zwei Auslesungen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:20-55](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L20) · `section:ff8098498e43a639918f` · section

Die Matrix [formula in source] summiert die vier Ergebnisgewichte jedes Kontexts. Die Matrix [formula in source] liest die 15 nichttrivialen Pauli-Erwartungswerte aus. Mit [formula in source] lauten ihre Einträge Für [formula in source] und [formula in source] ergibt sich exakt Der Systemschatten entwickelt sich somit als depolarisierender Kanal Die Dämpfung [formula in source] entsteht aus der Kontextkombinatorik. B

## Die genaue Kompression auf 30 Koordinaten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:56-74](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L56) · `section:42d2743562e0e0c25ccc` · section

Die in S01 ausgearbeitete Faktorisierung lautet Hier gelten [formula in source] , [formula in source] und [formula in source] . Die beiden Zeilenräume sind orthogonal. Im selben Kontext haben die Pauli-Vorzeichenvektoren Skalarprodukt drei für denselben Strahl und minus eins für verschiedene Strahlen; bei inzidenten Kontexten bleibt eine gemeinsame Pauli-Richtung. Diese Werte ergeben genau die Einträge von

## Warum Symmetrie die Gewichte noch nicht auswählt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:75-98](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L75) · `section:f98aaf63bec068a59875` · section

Aus [formula in source] mit Permutationsmatrizen folgt beim gleichgewichteten Mitteln unmittelbar [formula in source] . Zusätzliche Konjugation durch die Symmetriegruppe [formula in source] ändert das nicht: S07 berichtet 5040 Terme über 4500 verschiedene Matchings, gegenüber 24\,601\,472 insgesamt möglichen perfekten Matchings des bipartiten Inzidenzbildes. Diese kombinatorische Realisierung ist konkret. Die Gleichg

## Ein Schritt ist nicht dasselbe wie zwei halbe Schritte

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:99-113](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L99) · `section:4c0e3b526ca432972973` · section

Für die Kontextmatrix gilt Ihre Determinante ist negativ. Eine reelle Matrixexponentialfunktion hat jedoch [formula in source] . Deshalb ist [formula in source] auf diesem 15-dimensionalen Raum kein [formula in source] mit reellem [formula in source] .

## Gedächtnis: Was ein einzelnes Bild verschweigt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:114-115](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L114) · `section:f1b350b4f4ff17306de0` · chapter

No opening prose excerpt; see the source.

## Allgemeine Kontextblöcke brauchen eine andere Beschreibung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:116-149](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L116) · `section:7826f65d1a2c58cbc4b7` · section

Ein klassisch-quantenmechanischer Zustand, kurz CQ-Zustand, besitzt 15 positive [formula in source] -Blöcke [formula in source] . Zusammen haben sie 240 reelle lineare Koordinaten und Gesamtspur eins. Die feste Regel macht jeden Ausgangsblock in seinem Kontext diagonal. Deshalb gilt Es ist also nicht richtig, 240 Koordinaten pauschal als kleinste dauerhaft autonome Hülle dieser festen Ausführung auszugeben.

## Wie die Aufzeichnung gebaut wird

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:150-170](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L150) · `section:2cb123856760657c4ede` · section

Für die vier Projektoren eines Kontexts sind [formula in source] Spiegelungen. In Dimension vier gilt Allgemein in Dimension [formula in source] wäre die linke Seite [formula in source] . Der kurze Auslöschungseffekt ist hier also tatsächlich viererspezifisch.

## Das Echo des behaltenen Registers

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:171-184](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L171) · `section:c7ec14f6c325b400dfc1` · section

Für einen gleichförmigen reinen Eingang in der gewählten Kontextbasis erzeugt eine Vormessung maximale Verschränkung. Ohne Registerblick ist der Systemzustand [formula in source] . Nun gibt es zwei Ausführungen: Derselbe kohärente Speicher wird nochmals gekoppelt: [formula in source] stellt den reinen Eingang wieder her. Ein neuer Speicher wird benutzt: Im reduzierten System wird die Dephasierung wiederholt; [formula

## Reihenfolge bleibt wichtig

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:185-194](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L185) · `section:a458cd0a0c48d440679b` · section

Bei frischen Registern trägt eine Folge von Kontexten den kohärenten Zustand Das Weglassen des Registers summiert Dichteoperatorbeiträge. Eine kohärente Projektion auf eine Registersuperposition summiert Amplituden und beschreibt ein anderes Experiment, einschließlich seiner Erfolgswahrscheinlichkeit.

## Endliches Gedächtnis und scheinbares Vergessen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex:195-207](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/03_prozess.tex#L195) · `section:6398629093514ef7e839` · section

Eine nichtverschwindende Beobachtungsfolge eines geschlossenen endlichen Systems mit festem unitärem Schritt ist eine endliche Summe von Phasenfaktoren. Nach Zusammenfassung gleicher Frequenzen besitzt ihr mittleres Betragsquadrat einen positiven Cesàro-Grenzwert. Sie kann daher nicht für alle [formula in source] exakt wie [formula in source] abklingen.

## Die Vierträgerzelle: ein gemeinsames Muster

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L1) · `section:2ed493367af1746e6a15` · chapter

No opening prose excerpt; see the source.

## Ein Zustand, dessen Teile allein nichts verraten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:3-24](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L3) · `section:2112a15b75cb42207eba` · section

Vier Träger mit je vier Basiswerten besitzen den total antisymmetrischen Zustand Jedes Basiswort verwendet alle vier Werte genau einmal. Die 24 Permutationen erhalten passende Vorzeichen. Das Ergebnis ist ein reiner gemeinsamer Zustand. Jeder einzelne Träger sieht für sich trotzdem maximal gemischt aus: Die Paarreduktion hat Rang sechs und sechs gleich große Eigenwerte [formula in source] . Die Ordnung steckt in den 

## Der Hüllensatz und seine genaue Voraussetzung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:25-38](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L25) · `section:53f042f4f793a04fd88a` · section

Sei [formula in source] der Projektor auf den symmetrischen Paarraum. Wenn für alle Paare [formula in source] gilt, dann hat jeder Swap Eigenwert minus eins. Da Transpositionen alle Permutationen erzeugen, folgt Für [formula in source] ist dieser Raum eindimensional, für [formula in source] null. Auch gemischte Zustände mit entsprechender Trägerbedingung erfüllen die Aussage. Für [formula in source] existieren aber e

## Eine weiche Energiebedingung erlaubt Bewegung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:39-54](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L39) · `section:d49db396d1064b0b66b6` · section

Das vollständige Tetramermodell lautet Es besitzt das exakte Spektrum Der Grundzustand ist [formula in source] , die Lücke [formula in source] . Die hochgestellten Zahlen zählen die Zustände pro Energiewert und summieren sich zu 256.

## Was ein Zustand über seinen Generator verrät

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:55-68](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L55) · `section:ff315a3db540cd23c199` · section

Der vollständige Graph, ein Stern und ein Pfad besitzen auf vier Trägern denselben antisymmetrischen Grundzustand, aber verschiedene Anregungen. Für gleiche Sterngewichte ist die Lücke [formula in source] statt [formula in source] . S01 nennt für einen Pfad mit Gewichten [formula in source] etwa [formula in source] ; S06 für sechs Gewichte [formula in source] etwa [formula in source] . Die letzten Werte werden hier a

## Warum Austausch allein die Zelle nicht herstellt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:69-75](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L69) · `section:9d377aca6eca6ad1a877` · section

Der Projektor [formula in source] kommutiert mit allen Swaps. Daher erhält jede rein zellinterne Austauschentwicklung, auch mit zeitabhängigen Gewichten, den Anteil [formula in source] . Kollektive [formula in source] -Drehungen tun dasselbe. Ein Grundzustand kann also bekannt sein, ohne dass der vorhandene Ablauf einen beliebigen Eingang dorthin bringt.

## Vermittlung und Graph: die Prüfung der fünf Fugen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:76-80](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L76) · `section:0d3ffe2573ee528b84a8` · chapter

Aktualisierung v1.5: ein exakter kleinerer Spektralauftrag Der 80-dimensionale Standard-Multiplizitätsblock ist inzwischen explizit konstruiert und sein einfaches Spektrum exakt zertifiziert. Eine zusätzliche Tableau-Transposition reduziert die führenden Singulettprobleme auf höchstens 131-dimensionale quadrierte Singularwertprobleme. Das beweist noch keine globale Ordnung aller SU(4)-Sektoren. Siehe Kapitel

## Wie ein virtueller Zwischenzustand bindet

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:81-108](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L81) · `section:1085f0936587c8b168ae` · section

Der gewünschte positive Austausch lässt sich in einem kleinen Modell genau erklären. Man ergänzt den Paarraum [formula in source] durch einen sechsdimensionalen Vermittler mit Energie [formula in source] . Die partielle Isometrie [formula in source] erfüllt Für bleiben die zehn symmetrischen Zustände bei null; die antisymmetrischen Zustände koppeln paarweise an den Vermittler. Die unteren Energien sind Nach Identifik

## Der Clebsch-Vorschlag: eine genaue neue Graphlesart

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:109-130](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L109) · `section:a5f147096b897c548944` · section

S11 macht die zusätzliche Zuordnung: Ein [formula in source] -Spinorgewicht [formula in source] ist ein Ort; das [formula in source] -Gewicht [formula in source] ist der lokale Viererzustand. Die 64 Gewichte von [formula in source] werden somit als 16 Orte mit je vier inneren Zuständen gelesen. Das ist eine konkrete bedingte Interpretation, keine bloße Umbenennung einer bereits gegebenen räumlichen Geometrie.

## Welche Auswahl hier noch hinzukommt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:131-139](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L131) · `section:1ab54f5e1d418098c18f` · section

Die Graphkombinatorik folgt aus der angegebenen Ortslesart. Um daraus einen Vielteilchen-Hamiltonoperator zu erhalten, braucht man außerdem eine Fock- oder Tensorproduktstruktur, Besetzungsbedingungen, die Bedeutung der virtuellen Zustände und ihre Energien. Betragsgleiche Chevalley-Strukturkonstanten wählen noch keine physikalischen Kopplungsstärken in normierten Mehrteilchenzuständen aus. Gleiche [formula in source

## Die berichteten Clusterzahlen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:140-158](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L140) · `section:3302301a3838e99c096d` · section

L74mmY Clebsch-Cluster bei [formula in source] , nach S11& Berichteter Wert\\ Grundenergie& [formula in source] \\ Grundzustand&Eindeutiges [formula in source] -Singulett, Form [formula in source] \\ Erster angeregter Singulettwert& [formula in source] ; mindestens vier orthogonale Moden, Gap etwa [formula in source] \\ Erste adjungierte Anregung& [formula in source] , Gap etwa [formula in source] \\ Weitere Multiple

## Neue Korrektur: Singulett heißt nicht eindeutig

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:159-174](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L159) · `section:35d2a7d660e36a19933c` · section

S11 behauptet für den vollständigen Graphen mit [formula in source] einen eindeutigen Grundzustand bei [formula in source] und Gap [formula in source] . Energie und Gap stimmen; die Eindeutigkeit stimmt ab acht Trägern nicht.

## Neue Präzisierung: Aufzeichnung ist nicht durch die 248 verboten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex:175-196](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/04_zellen.tex#L175) · `section:1fe800bdd4895cbe317f` · section

Operatoren unterscheiden (v1.3): Das folgende [formula in source] beschreibt eine gleichkontextige Vierer-Aufzeichnung. Das neue binäre Austauschregister [formula in source] ist ein anderer Operator und nachweislich nicht Clifford. Seine zusätzliche Ressourcenanforderung widerspricht der folgenden Darstellbarkeit von [formula in source] nicht.

## Zwei Zellen: aus Verbindung wird Dynamik

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex:1-5](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex#L1) · `section:8b57da1e623bb492d3a1` · chapter

Aktualisierung v1.5: der Übergang zu vielen Zellen ist genauer Kapitel

## Warum die Zellen beim Verbinden ihre Reinheit verlieren

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex:6-10](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex#L6) · `section:b8b8c54d2db4ac686444` · section

Ist eine reduzierte Dichtematrix [formula in source] rein, so muss der gemeinsame Zustand bezüglich [formula in source] und seinem Rest faktorisiert sein. Sein Träger liegt in [formula in source] . Sind alle disjunkten Zellmarginalien unverändert rein, ist der Gesamtzustand ein Produkt über die Zellen.

## Ein kleiner exakter Raum in einem großen Hilbertraum

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex:11-31](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex#L11) · `section:c07b1633438c69ba3110` · section

Zwei vollständige Tetramerzellen mit genau einer Brücke haben Der volle Raum besitzt [formula in source] Dimensionen. Trotzdem bleibt die Entwicklung des Produktzustands in einem zweidimensionalen invarianten Unterraum: Die beiden Vektoren sind orthonormal; [formula in source] und [formula in source] . Es folgt Die Brücke koppelt den Produktgrundzustand an eine gemeinsame adjungierte Anregung. Beide Zellhälften verwe

## Energie und ein wirklicher Grundzustandsnachweis

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex:32-76](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex#L32) · `section:765df0a298712b60114d` · section

Mit lauten die beiden Eigenwerte Die negative Korrektur beschreibt die Absenkung gegenüber dem einfachen Produktwert [formula in source] .

## Verschränkung aus derselben Kopplung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex:77-98](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex#L77) · `section:8069cafc60ed018d26cf` · section

Der niedrige Eigenzustand lässt sich schreiben als Seine Zellreduktion besitzt das Spektrum Die Entropie in natürlichen Logarithmen ist Bei [formula in source] sind [formula in source] und [formula in source] ; bei [formula in source] gilt [formula in source] . Schon eine endliche einzelne Brücke macht die lokale Zelle gemischt. Energieabsenkung und Verschränkung sind hier keine unabhängig eingesetzten Zusätze.

## Ein Uhrsignal ohne zusätzlich gewählten lokalen Tick

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex:99-114](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex#L99) · `section:88ef392cbb45c91a536b` · section

Starte im Produkt [formula in source] und lasse denselben konstanten gekoppelten Hamiltonoperator wirken. Dann gilt Bei [formula in source] vereinfacht sich dies zu [formula in source] . Der Energieinhalt beider Zellen pulsiert in einem messbaren Muster.

## Warum viele Zellen noch ein eigener Schritt sind

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex:115-125](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/05_kopplung.tex#L115) · `section:69cca408ac4b087494e1` · section

Ein einzelner eindeutiger Singulettgrundraum besitzt keine logische Zustandsvielfalt. Das Produkt solcher Grundräume bleibt eindimensional. Wer alles auf diese Grundräume projiziert, erhält nur eine skalare Energie. Nichttriviale effektive Dynamik muss Anregungen, Randzustände, Multiplizitäten oder zusätzliche Vakuumsektoren behalten.

## Zeit: Takt, Uhrwerk und lesbare Veränderung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/06_zeit_echo.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/06_zeit_echo.tex#L1) · `section:a07306bcb0d52a262c21` · chapter

No opening prose excerpt; see the source.
