# Verification, formalization and safeguards — part 8

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

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

## 2026-06-18 (Route-B red-team: the smooth [formula in source] adversary + Flat-Away as a mini-theorem, v290– v291)

[documents/changelog/sections/017-source.tex:270-285](../../../../documents/changelog/sections/017-source.tex#L270) · `section:1dd51adeb586c882e7c4` · subsection

v290_z4_smooth_curvature_adversary.py ( SEAM.ADVERSARY.01) is the honest red-team that [formula in source] block-diagonality is not mark-locality: a smooth [formula in source] off-mark curvature [formula in source] \ passes the v288 commutator ( [formula in source] , same as mark-local) yet \ shifts the DtN spectrum ( [formula in source] ) and the heat trace ( [formula in source] ). So the commutator is necessary, no

Explicit source references:

- [verification/v291_flataway_contract.py](../../../../verification/v291_flataway_contract.py#L1) · explicit_script_identifier
- [verification/v290_z4_smooth_curvature_adversary.py](../../../../verification/v290_z4_smooth_curvature_adversary.py#L1) · explicit_script_identifier
- [verification/v288_full_l2_subprincipal_z4.py](../../../../verification/v288_full_l2_subprincipal_z4.py#L1) · explicit_script_identifier
- [FLATAWAY.RP.01](../../../../verification/status_ledger.csv#L386) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.ADVERSARY.01](../../../../verification/status_ledger.csv#L385) · explicit_claim_identifier · original status at linked ledger row

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

## 2026-06-17 (Spectral-action matter content: the [formula in source] 16 [formula in source] one anomaly-free SM generation, v245)

[documents/changelog/sections/019-source.tex:69-85](../../../../documents/changelog/sections/019-source.tex#L69) · `section:d0aef4f5062824e2d6c2` · subsection

v245_spectral_matter_content.py ( QFT4D.MATTER.01) discharges the computable core of the 4d contract v244. The carrier half-spinor (the [formula in source] 16) is verified, in exact rational arithmetic, to be one Standard-Model generation: [formula in source] , the SM multiplet dimensions sum to [formula in source] ( [formula in source] Weyl fermions [formula in source] ), the electric charges [formula in source] are

Explicit source references:

- [verification/v245_spectral_matter_content.py](../../../../verification/v245_spectral_matter_content.py#L1) · explicit_script_identifier
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [CONTRACT.QFT4D.01](../../../../verification/status_ledger.csv#L330) · explicit_claim_identifier · original status at linked ledger row
- [verification/v244_spectral_action_contract.py](../../../../verification/v244_spectral_action_contract.py#L1) · explicit_script_identifier
- [QFT4D.MATTER.01](../../../../verification/status_ledger.csv#L331) · explicit_claim_identifier · original status at linked ledger row

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

## 2026-06-14 (Zenodo release 5.1 (rev 120) — F_transfer firewall, v184–v188)

[documents/changelog/sections/020-source.tex:332-344](../../../../documents/changelog/sections/020-source.tex#L332) · `section:1baa0cb6fdd6a6b16124` · subsection

Published to Zenodo. Version 5.1 (rev 120) of the ten-PDF document set was published as a new version of the TFPT deposit — record 20687564, DOI 10.5281/zenodo.20687564. This version carries the F_transfer-firewall round ( v184– v188): the honest [formula in source] anchored-Boltzmann test (sharper scenario, not a closure), the axion hilltop-relic typing, the ledger v187 and prose v188 guards, and the Route B/Koide/d

Explicit source references:

- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v188_frontier_wording_guard.py](../../../../verification/v188_frontier_wording_guard.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier

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

## 2026-06-12 (Overleaf shadow mirror: tfpt5-shadow)

[documents/changelog/sections/022-source.tex:336-344](../../../../documents/changelog/sections/022-source.tex#L336) · `section:38476028a7422847fd8e` · subsection

One-way GitHub mirror for Overleaf sync. Added scripts/export-shadow.sh and .github/workflows/shadow-sync.yml: on every push to main, a filtered copy is pushed to sthamann/tfpt5-shadow (papers, tex-artefacts/, figures/, verification/, experiments/; excludes _archive/, website/, all *.pdf, .cursor/). [formula in source] 270 files / [formula in source] 3\,MB — within Overleaf GitHub-sync limits.

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

## 2026-06-12 (marker simplification to 4 classes + status reconciliation)

[documents/changelog/sections/023-source.tex:242-263](../../../../documents/changelog/sections/023-source.tex#L242) · `section:4f6387455280982ea775` · subsection

Four-class display markers. The reader-facing marker system is collapsed from eleven symbols to four: \ exact / machine-proven (identity, Lie/lattice, formalised, numerical FP), \ conditional (physical / bridge / readout under named hypotheses), \ open / axiom, and \ kill test. tex-artefacts/tfpt_style.tex defines mE/ mC/ mO/ mX and keeps the legacy tI tX names as aliases that render their class. All marker call-site

Explicit source references:

- [COSMO.NSTAR.01](../../../../verification/status_ledger.csv#L160) · explicit_claim_identifier · original status at linked ledger row
- [verification/v86_nstar_reheating.py](../../../../verification/v86_nstar_reheating.py#L1) · explicit_script_identifier
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v86) reheating arithmetic (scale chain; pivot solve stays Python) ---- *) Mbar = 2.435323203`20 10^18; Mscal = c3^(7/2) Mbar; GammaScal = 4 Mscal^3/(48 Pi Mbar^2); check["v86 Gamma = 4 M^3/(48 pi Mbar^2) = 128.1 GeV", GammaScal, 128.146562596`12, 10^-6]; check["v86 T_reh = 9.55e9 GeV (g*=106.75)", (30 (3 GammaScal^2 Mbar^2)/(Pi^2 106.75))^(1/4), 9.55048669665`12 10^9, 10^-6]; AsOf[n_] := n^2 c3^7/(24 Pi^2); check["v86 A_s(51.4406) = 1.764e-9 (the A_s-disfavoured slow point)", AsOf[51.4406], 1.7637`5 10^-9, 10^-3]; check["v86 A_s-preferred N_star = 56.198", Sqrt[2.105`10 10^-9 24 Pi^2/c3^7], 56.198`6, 10^-4]; check["v86 dichotomy: matching A_s at 51.44 needs M x 1.0925", Sqrt[2.105`10 10^-9/AsOf[51.4406]], 1.09248`6, 10^-4]; (* ---- (v87) SO(16)_1 modular data and its six invariants ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L83)

## 2026-06-12 (tex-artefacts refactor + introduction visual pass B2)

[documents/changelog/sections/023-source.tex:303-330](../../../../documents/changelog/sections/023-source.tex#L303) · `section:826ddf772de04049b71a` · subsection

Shared imports moved to tex-artefacts/. The shared, imported-only TeX fragments ( tfpt_style.tex, tfpt_figures.tex, tfpt_docset.tex, tfpt_status.tex) now live in a dedicated tex-artefacts/ folder; all nine active documents input them via tex-artefacts/<name> (and tfpt_style loads tex-artefacts/tfpt_figures). changelog.tex stays at the repo root because it is also a standalone build.sh notes deliverable. The make_mani

Explicit source references:

- [README.md](../../../../README.md#L1) · explicit_file_citation
- [verification/make_manifest.py](../../../../verification/make_manifest.py#L1) · explicit_file_citation

## 2026-06-12 (visual pass: box reduction B1)

[documents/changelog/sections/023-source.tex:331-340](../../../../documents/changelog/sections/023-source.tex#L331) · `section:37c689285c5fc6a40772` · subsection

Box reduction (B1). The [formula in source] non-load-bearing aside boxes (audit / recorded / interpretation: auditbox/ audbox/ intbox/ resbox/ roadbox) across tfpt_1, tfpt_2, tfpt_3 and origin_theory are converted to inline bold run-in paragraphs — the reviewer's prescription that an audit fingerprint must not carry the same visual volume as a theorem. The loud box families are now only keybox (claim), winbox (result

## 2026-06-12 (review pass on list.txt)

[documents/changelog/sections/023-source.tex:356-381](../../../../documents/changelog/sections/023-source.tex#L356) · `section:b7fc94b9c310d988cbec` · subsection

Claim hygiene (review section A). The introduction's one-sentence claim is softened from ``derives all constants'' to ``constructs a discrete compiler; physical readouts run through named, status-typed bridges''; the ledger zombie in FLAV.QRATIO.01 is removed (the statement no longer says ``stays [P]'' — ratios are \ closed on the derived stratum, only the absolute scale stays , with an explicit forbidden-wording not

Explicit source references:

- [FLAV.QRATIO.01](../../../../verification/status_ledger.csv#L25) · explicit_claim_identifier · original status at linked ledger row

## 2026-06-12 (later)

[documents/changelog/sections/024-source.tex:1-11](../../../../documents/changelog/sections/024-source.tex#L1) · `section:e2e448f834c8b18c1b82` · subsection

Shared style and central status artifact. Two new single-source fragments: tfpt_style.tex (the canonical palette, status markers, marker key, veri reference, the four tcolorbox families with back-compat aliases, and one running header/footer) is now input by all eight documents — the per-paper duplicated preambles are gone; and tfpt_status.tex (``TFPT status at a glance'') gives one canonical overall-status card impo

## 2026-06-10

[documents/changelog/sections/024-source.tex:109-118](../../../../documents/changelog/sections/024-source.tex#L109) · `section:6b03fdb0bab2125a7ce4` · subsection

B/C/D round closed. Koide attractor toy model (v93), glue uniqueness (v92), the Wolfram extension as the independent second verification path, Lean hardening; papers and website synced with the round. Content rounds v96–v100. Sheet conjugation bridge, discriminant dictionary, Koide flow time, and the look-elsewhere-corrected numerology null test (v100: joint null probability [formula in source] , conditional on the d

Explicit source references:

- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [verification/v96_branch_kernel_selection.py](../../../../verification/v96_branch_kernel_selection.py#L1) · explicit_script_identifier
- [verification/v93_koide_relaxation_toy.py](../../../../verification/v93_koide_relaxation_toy.py#L1) · explicit_script_identifier
- [verification/v100_numerology_null_mc.py](../../../../verification/v100_numerology_null_mc.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v95) centered flavor diamond ---- *) Uop = Q.DiagonalMatrix[{1, 0, 0}]; Vop = Q.DiagonalMatrix[{0, 1, 1}]; Cc = R + Uop; Lop = R + 2 Uop; Fop = R + Q; checkExact["v95 centered cross: Q=U+V; R=C-U, L=C+U, K=C-V, F=C+V", (Q == Uop + Vop) && (R == Cc - Uop) && (Lop == Cc + Uop) && (K == Cc - Vop) && (Fop == Cc + Vop)]; checkExact["v95 axes spectra: Spec U = {3,0,0} (winding), Spec V = {0,1,2} = N_fam*cusp", (Sort[Eigenvalues[Uop]] == {0, 0, 3}) && (Sort[Eigenvalues[Vop]] == {0, 1, 2})]; checkExact["v95 center invariants: tr C=12, det C=14, sum C=31=2^g_car-1, det B_C=28", (Tr[Cc] == 12) && (Det[Cc] == 14) && (Total[Cc, 2] == 31) && (31 == 2^gcar - 1) && (Det[bb[Cc]] == 28)]; checkExact["v95 ray alignment: Pi_R(C)=7(2,3,1), Pi_R(L)=10(2,3,1)", (plR[Cc] == 7 {2, 3, 1}) && (plR[Lop] == 10 {2, 3, 1})]; (* ---- (v96) branch-kernel selection (P1) ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L204)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)

## 2026-06-07 / 2026-06-08

[documents/changelog/sections/024-source.tex:127-136](../../../../documents/changelog/sections/024-source.tex#L127) · `section:b7a05826756c1fc3ef1e` · subsection

Compiler-closure consolidation. The TFPT development is consolidated into the current document set with the verification suite (modules v1–v82: [formula in source] glue, carrier Pascal, EM fixed point, flavor matrix, cascade, bootstrap, gravity/cosmology, transport, masses, registry and gate audits) as the single proof layer; manifests ( manifest.sha256, lean_manifest.sha256) as content identity; website mirrors the 

Explicit source references:

- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)

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

## What This Note Is About

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/001-section-what-this-note-is-about.tex:268-413](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/001-section-what-this-note-is-about.tex#L268) · `section:08cfee9db593f91b22c1` · section

v1 formalised the algebraic motor of TFPT Paper 2 — the carrier polynomial and the trace identity on a concrete [formula in source] diagonal model. v2 began making the upstream dependencies explicit. v3 made the dependency graph correct. v4 replaced the Yukawa rank witness with a structurally algebraic Stage B (top form on [formula in source] ). v5 introduced a Stage C contraction iso [formula in source] .

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1) · explicit_file_citation
- [TFPT.Carrier.YukawaTrilinearForm.YukawaTrilinearForm.finrank_E_eq_zero_or_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L221) · explicit_lean_symbol
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1) · explicit_file_citation
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean#L1) · explicit_file_citation
- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v8_horizon.py](../../../../verification/v8_horizon.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1) · explicit_file_citation
- [TFPT.Carrier.CarrierData.CarrierPremises.hypercharge_carrier_packet](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierData.lean#L213) · explicit_lean_symbol
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)

## What Was Built

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:1-54](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L1) · `section:0c38c86d099cc1fbe936` · section

Twenty-seven Lean modules under experiments/lean4-carrier-rigidity/TfptCarrier/:

Explicit source references:

- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/OrientedDeterminantCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/OrientedDeterminantCarrier.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/Rigidity.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Rigidity.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/Sanity.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Sanity.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1) · explicit_file_citation
- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/lakefile.lean](../../../../experiments/lean4-carrier-rigidity/lakefile.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaRank.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaRank.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/DeterminantCharacter.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/DeterminantCharacter.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsIndexShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsIndexShadow.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/TraceProjection.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/TraceProjection.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/MathlibBridge.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/MathlibBridge.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/InvolutionProjectors.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/InvolutionProjectors.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/Hypercharge.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Hypercharge.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/LatticeRigidityGeneral.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/LatticeRigidityGeneral.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/Polarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Polarization.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierData.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierData.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTopForm.lean#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)

## Dependency Graph

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:55-215](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L55) · `section:0184d24558b3688eb8ec` · section

Every node is a separately formalised Lean theorem; every arrow is a discharged proof obligation in TfptCarrier. Blue nodes are unconditional Lean theorems. Orange nodes are Stage-A structured hypotheses. Green nodes are the bundled conclusions.

Explicit source references:

- [verification/v8_horizon.py](../../../../verification/v8_horizon.py#L1) · explicit_script_identifier
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier
- [TFPT.Carrier.YukawaTrilinearForm.YukawaTrilinearForm.finrank_E_eq_zero_or_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L221) · explicit_lean_symbol
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_script_identifier
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)

## The Headline Theorems

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:216-222](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L216) · `section:7ae44ace5c173b12d8ea` · section

We list the headline theorems by graph layer. Every name is elaborated by TfptCarrier/AuditCheck.lean.

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation

## Layer 1 — Polarization (algebraic core)

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:223-231](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L223) · `section:5f57a8721f5f3b8e8b0e` · subsection

Let [formula in source] be a ring with two orthogonal idempotents [formula in source] summing to [formula in source] . Then [formula in source] satisfies [formula in source] .

## Layer 0+ — Calderón structural certificate (Paper 1)

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:232-247](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L232) · `section:c209de143c3b0550ea0e` · subsection

Let [formula in source] be a ring with [formula in source] invertible and let [formula in source] satisfy [formula in source] . Define [formula in source] . Then [formula in source] .

## Layer 2 — Involution to projectors

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:248-257](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L248) · `section:820548a680f86eaf3ffa` · subsection

Let [formula in source] be an element of a ring [formula in source] with [formula in source] and [formula in source] invertible in [formula in source] . The spectral projectors [formula in source] defined by [formula in source] form a Polarization of [formula in source] . Each of the four polarization axioms is discharged directly from [formula in source] .

## Layer 3 — General lattice rigidity

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:258-274](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L258) · `section:9e35ff4483e6faa37934` · subsection

Let [formula in source] be positive integers and [formula in source] satisfy [formula in source] Then [formula in source] and [formula in source] .

## Layer 4 — Structural trace

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:275-293](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L275) · `section:a53d7a69f92354350f32` · subsection

For any two idempotent endomorphisms [formula in source] of a finite- dimensional [formula in source] -vector space [formula in source] , and any [formula in source] , [formula in source]

## Layer 5 — Determinant character

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:294-327](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L294) · `section:f1f4c7c4327173aa800f` · subsection

For nonzero [formula in source] in a field [formula in source] and integer charges [formula in source] , [formula in source]

Explicit source references:

- [TFPT.Carrier.DeterminantCharacter.trace_zero_of_det_one_at_two](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/DeterminantCharacter.lean#L118) · explicit_lean_symbol

## Layer 6 — Stage-A and Stage-B rank certificates

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:328-344](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L328) · `section:3c5f6d169b621baf815f` · subsection

The space of homogeneous degree-1 polynomials in two formal variables, defined concretely as [formula in source] with the natural [formula in source] -module structure, has [formula in source] -rank [formula in source] .

## Layer 6 — Stage-A rank certificates

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex:345-357](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/002-section-what-was-built.tex#L345) · `section:5118f2c988d2cc7a0844` · subsection

A HiggsIndexCertificate, defined as a linear equivalence [formula in source] , forces [formula in source] .

## Layer 6b — Yukawa Stage B (algebraic content)

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:1-41](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L1) · `section:d79578b52f4103457fa4` · subsection

A YukawaTopForm K E, defined as a linear equivalence [formula in source] , forces [formula in source] .

## Layer 6c — Yukawa Stage C (primitive indecomposable coupling)

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:42-88](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L42) · `section:4d9c450dc14cec1c3117` · subsection

A PrimitiveIndecomposableYukawaCoupling K E, defined as a linear equivalence [formula in source] plus non-triviality of [formula in source] , forces [formula in source] .

Explicit source references:

- [PrimitiveIndecomposableYukawaCoupling.ofFinrankEqThree](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L202) · explicit_lean_symbol
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [PrimitiveIndecomposableYukawaCoupling.nonempty_iff_finrank_eq_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L242) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## Layer 6d — Yukawa Stage D (primary trilinear form)

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:89-201](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L89) · `section:80f5430a98e66833b910` · subsection

For every alternating trilinear form [formula in source] , the associated contraction map [formula in source] is constructible as a LinearMap. The Lean construction uses exteriorPower.alternatingMapLinearEquiv (to convert between [formula in source] and the space of [formula in source] -valued alternating maps on [formula in source] ) and AlternatingMap.curryLeft (to split off the first argument).

Explicit source references:

- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)

## Layer 7 — Mathlib bridge

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:202-210](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L202) · `section:054c02ea3d6a19cf35e1` · subsection

A TFPT.Carrier.Polarization on a ring [formula in source] is canonically a Mathlib CompleteOrthogonalIdempotents on the pair [formula in source] . A converse map ofCompleteOrthogonalIdempotents is also provided.

Explicit source references:

- [TFPT.Carrier.Polarization](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Polarization.lean#L36) · explicit_lean_symbol

## Layer 8 — Bundled main theorems

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:211-238](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L211) · `section:ee6b6e1460d0b7b1bd43` · subsection

The carrier-rigidity payload of the project is the following set of bundled theorems on CarrierPremises K M:

## Concrete realisation

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:239-248](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L239) · `section:95d9cf94bda42fc0f31e` · subsection

On the concrete [formula in source] rational diagonal model, [formula in source] satisfies [formula in source] and [formula in source] , proved by direct per-entry rational arithmetic.

## Significance

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:249-255](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L249) · `section:f391f960dd599e630069` · section

The two load-bearing chains, with all hypotheses explicitly visible, are:

## Chain A — trace identity.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:256-281](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L256) · `section:35a557d0d4bb41900f4f` · paragraph

[formula in source] together with the rank discharges [formula in source] and the determinant-normalised coefficient choice [formula in source] give, via TraceProjection, [formula in source] The Yukawa input is now an alternating trilinear form with two explicit Prop predicates. The contraction iso and the rank-3 conclusion are both derived theorems.

## Chain B — integer rigidity.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:282-300](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L282) · `section:950d3549a66e5fd478a0` · paragraph

The trace-zero condition [formula in source] follows from the universal- [formula in source] determinant character. Combined with the primitivity and orientation conditions [formula in source] the general [formula in source] rigidity theorem gives [formula in source] For [formula in source] this specialises to [formula in source] . The integer answer is a corollary of a parametric theorem; it is not hard-coded.

## Why both chains matter together.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:301-310](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L301) · `section:992cf28e93a790907da4` · paragraph

The carrier polynomial [formula in source] is a consequence of the polarization layer alone (it does not need either rank discharge). The trace identity [formula in source] requires the rank discharges. The integer pair [formula in source] requires the primitive oriented determinant-preserving condition together with [formula in source] . The bundled theorem hypercharge_carrier_packet is the unique statement that req

Explicit source references:

- [TFPT.Carrier.CarrierData.CarrierPremises.hypercharge_carrier_packet](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierData.lean#L213) · explicit_lean_symbol

## What is not claimed.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex:311-319](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/003-subsection-layer-6b-yukawa-stage-b-algebraic-content.tex#L311) · `section:623844c7d7161b1e3813` · paragraph

The [formula in source] multiplet [formula in source] is the carrier. The full Standard-Model hypercharge spectrum — all chiral-multiplet hypercharges including duals, exterior powers, and tensor products — is not formalised in this experiment. The title and main theorem both say " [formula in source] hypercharge carrier", not "SM hypercharge spectrum".

## Interface Table: TFPT Paper 2 [formula in source] <-> Lean Status

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:1-109](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L1) · `section:18f9d14a7232cd74c3b7` · section

The following table maps each load-bearing claim of TFPT Paper 2 to its current Lean status and the still-missing upstream proof. It is the primary defence against scope-creep: the present note formalises columns 1 and 2; column 3 is explicitly out of scope.

Explicit source references:

- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)

## Limitations

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:110-113](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L110) · `section:afeac5dd63b853c239be` · section

No opening prose excerpt; see the source.

## Yukawa: Stage D resolves the v5 critique.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:114-134](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L114) · `section:5b5deee14edc9e9ff37f` · paragraph

The v5 critique of Stage C was that it bundled the contraction iso as data, so it was equivalent (in finite dimensions) to [formula in source] and did not "explain" the rank. v6 resolved this by introducing Stage D; v7 renamed its operational predicates to keep semantic-load words out of the Lean interface:

Explicit source references:

- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier
- [verification/v6_bootstrap.py](../../../../verification/v6_bootstrap.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)

## Why Nontrivial\, [formula in source] is necessary.

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:135-146](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L135) · `section:c0b758d352b686c50e93` · paragraph

Without the non-triviality hypothesis the rank-3 slogan would be false: for [formula in source] the spaces [formula in source] and [formula in source] are both zero, the contraction [formula in source] is trivially bijective, both operational predicates hold vacuously, but [formula in source] . The transparency theorem finrank_E_eq_zero_or_three (v9) records the unconditional disjunction [formula in source] ; the ran

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [TFPT.Carrier.YukawaTrilinearForm.YukawaTrilinearForm.finrank_E_eq_zero_or_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L221) · explicit_lean_symbol

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)

## Stage D characterisation, both directions formalised (v10).

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:147-166](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L147) · `section:7da7283875b2911aa2f3` · paragraph

For all four Yukawa stages the note now proves the full characterisation [formula in source] . For Stage D, under Nontrivial\, [formula in source] : [formula in source] The forward direction is finrank_E_eq_three_of_condition; the backward direction is YukawaStageDExistence.exists_yukawaTrilinearForm_of_finrank_eq_three, proved via Module.Basis.det transported through exteriorPower.alternatingMapLinearEquiv and direc

Explicit source references:

- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)

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

## How It Was Verified

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:252-319](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L252) · `section:fe53e8d4ab98d645d8ec` · section

The audit gate scripts/audit.sh enforces seven hard checks on every commit:

Explicit source references:

- [experiments/lean4-carrier-rigidity/TfptCarrier/Sanity.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Sanity.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1) · explicit_file_citation

## Changelog

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex:320-323](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/004-section-interface-table-tfpt-paper-2-texorpdfstring-left.tex#L320) · `section:3f2aaf619c0723316625` · section

No opening prose excerpt; see the source.

## v11 — review-pass closure and typed targets for the remaining upstream theorems (the present revision)

[documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex:1-94](../../../../documents/experiments--lean4-carrier-rigidity--note_carrier_rigidity_lean4/sections/005-subsection-v11-review-pass-closure-and-typed-targets-for.tex#L1) · `section:307d97065ae218f24093` · subsection

Relative to v10, this version is a closure-and-naming pass. It addresses the v10 reviewer's three actionable findings:

Explicit source references:

- [TFPT.Carrier.BoundaryYukawaKernelInterface.BoundaryYukawaKernel.finrank_E_eq_three](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L99) · explicit_lean_symbol
- [BoundaryPolarization.ofCarrierInvolution](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L184) · explicit_lean_symbol
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1) · explicit_file_citation
- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_script_identifier
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v10_projection_involution.py](../../../../verification/v10_projection_involution.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
