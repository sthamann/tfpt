# Verification, formalization and safeguards — part 13

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## T3/T4: canonical DET excitations and the signed wall.

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex:243-303](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex#L243) · `section:e34efc6d3388a546fda0` · paragraph

CHIRAL4D.MIRROR.SIGNED.CAR.01. v1027_ signed_ det_ car_ wall.py checks the following algebra and its finite countermodels. The old Hubbard operators [formula in source] satisfy [formula in source] , not CAR, and [formula in source] . For even [formula in source] (in particular [formula in source] ), write [formula in source] and define [formula in source] This is a two-dimensional rotation and identity elsewhere. It 

Explicit source references:

- [verification/v1027_signed_det_car_wall.py](../../../../verification/v1027_signed_det_car_wall.py#L1) · explicit_file_citation
- [CHIRAL4D.MIRROR.SIGNED.CAR.01](../../../../verification/status_ledger.csv#L781) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v1027: exact signed-wall determinant and unsquared low branch. *) {a, delta, lambda, g} = Unique /@ {"a", "delta", "lambda", "g"}; mass = delta + lambda; beta = lambda g^2; eta = lambda g; c = beta - eta^2/mass; h = {{a + beta a^2, eta a}, {eta a, mass}}; check["v1027 signed determinant M a (1+c a)", Together[Det[h] - mass a (1 + c a)] === 0]; check["v1027 physical kernel remains one-dimensional at a=0", NullSpace[h /. a -> 0] === {{1, 0}}]; (* v1028: exact characteristic-five reduction of the full 192-mode one-site character. P^12 == P^2 P(z^5)^2 mod 5 is evaluated by coefficient dictionaries, never by floating group quadrature. *)](../../../../verification/wolfram/tfpt_round4.wl#L28)

## T6/T8: full Gauss counts, internal cap and selection rules.

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex:304-374](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex#L304) · `section:5da67bc01aba5e43512c` · paragraph

PARENT.GAUSS.D4.ROUND4.01. v1028_ gauss_ d4_ cap.py uses the full exterior character, not a low-occupation truncation. Let [formula in source] consist of [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] , with charges [formula in source] . For color weights [formula in source] and weak weights [formula in source] , set [formula in source

Explicit source references:

- [verification/v1028_gauss_d4_cap.py](../../../../verification/v1028_gauss_d4_cap.py#L1) · explicit_file_citation
- [PARENT.GAUSS.D4.ROUND4.01](../../../../verification/status_ledger.csv#L782) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v1028: exact ordinary D4 cap on the selected 12D even pair space. *) cs = DiagonalMatrix[{1, -I, -1, I}]; cf = DiagonalMatrix[{-I, -1, I}]; js = SparseArray[Table[{Mod[-kk, 4] + 1, kk + 1} -> 1, {kk, 0, 3}], {4, 4}]; jf = {{0, 0, 1}, {0, 1, 0}, {1, 0, 0}}; rot = KroneckerProduct[cs, cf]; refl = KroneckerProduct[js, jf]; check["v1028 ordinary D4 relations on selected even pair space", zeroQ[MatrixPower[rot, 4] - IdentityMatrix[12]] && zeroQ[refl.refl - IdentityMatrix[12]] && zeroQ[refl.rot.refl - ConjugateTranspose[rot]]]; (* One-based flattened slots for (k,g)=(1,3),(2,2),(3,1). *)](../../../../verification/wolfram/tfpt_round4.wl#L112)
- [(* v1027: exact signed-wall determinant and unsquared low branch. *) {a, delta, lambda, g} = Unique /@ {"a", "delta", "lambda", "g"}; mass = delta + lambda; beta = lambda g^2; eta = lambda g; c = beta - eta^2/mass; h = {{a + beta a^2, eta a}, {eta a, mass}}; check["v1027 signed determinant M a (1+c a)", Together[Det[h] - mass a (1 + c a)] === 0]; check["v1027 physical kernel remains one-dimensional at a=0", NullSpace[h /. a -> 0] === {{1, 0}}]; (* v1028: exact characteristic-five reduction of the full 192-mode one-site character. P^12 == P^2 P(z^5)^2 mod 5 is evaluated by coefficient dictionaries, never by floating group quadrature. *)](../../../../verification/wolfram/tfpt_round4.wl#L28)

## T7: local constraints and zero-mode removal.

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex:375-422](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex#L375) · `section:36bd7adad54b2ccf5753` · paragraph

GRAV.SPIN2.LOCAL.CONSTRAINT.01. v1029_ local_ tensor_ constraints.py implements a quadratic target, not a TFPT embedding. For six orthonormal symmetric tensor coordinates, let [formula in source] , [formula in source] , [formula in source] , [formula in source] . Set [formula in source] with constraints [formula in source] , [formula in source] . Direct polynomial algebra gives [formula in source] The four constraint

Explicit source references:

- [GRAV.SPIN2.LOCAL.CONSTRAINT.01](../../../../verification/status_ledger.csv#L783) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1029_local_tensor_constraints.py](../../../../verification/v1029_local_tensor_constraints.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v1029: exact generic local tensor identities and the k=0 instability. *) {x, y, z} = Unique /@ {"x", "y", "z"}; k = {x, y, z}; basis = Join[ Table[Outer[Times, UnitVector[3, ii], UnitVector[3, ii]], {ii, 1, 3}], Table[With[{ii = pair[[1]], jj = pair[[2]]}, (Outer[Times, UnitVector[3, ii], UnitVector[3, jj]] + Outer[Times, UnitVector[3, jj], UnitVector[3, ii]])/Sqrt[2]], {pair, {{2, 3}, {1, 3}, {1, 2}}}] ]; bmat = Transpose[(#.k) & /@ basis]; trace = {1, 1, 1, 0, 0, 0}; k2 = k.k; v = Transpose[bmat].k; scalar = v - k2 trace; kp = IdentityMatrix[6] - Outer[Times, trace, trace]/2; kq = k2 (IdentityMatrix[6] - Outer[Times, trace, trace]) - 2 Transpose[bmat].bmat + Outer[Times, trace, v] + Outer[Times, v, trace]; check["v1029 generic local tensor constraint identities", zeroQ[bmat.Transpose[bmat] - (k2 IdentityMatrix[3] + Outer[Times, k, k])/2] && zeroQ[kq.Transpose[bmat]] && zeroQ[kp.scalar - Transpose[bmat].k] && PossibleZeroQ[scalar.scalar - 2 k2^2]]; r = Unique[]; zeroEnergy = Expand[(r trace).kp.(r trace)/2]; check["v1029 periodic k=0 trace mode has exact energy -3 r^2/4", zeroEnergy === -3 r^2/4]; (* v1030: actual connected-sector words span M4; a disconnected mutant leaves one extra commutant degree. *)](../../../../verification/wolfram/tfpt_round4.wl#L135)

## ALG2: sector generation and conditional uniform section.

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex:423-457](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tex-artefacts/toe_round4_proofs.tex#L423) · `section:0c057e20a3b1322e45f5` · paragraph

SEAM.MMST.ALG2.FRAME.01. v1030_ alg2_ sector_ frame.py does not restore the refuted Vandermonde implication. Suppose, explicitly, [formula in source] and the actual neutral algebra is [formula in source] . Join [formula in source] if [formula in source] . Then [formula in source] precisely when this undirected sector graph is connected: the neutral commutant is [formula in source] , and each nonzero corner forces [fo

Explicit source references:

- [SEAM.MMST.ALG2.FRAME.01](../../../../verification/status_ledger.csv#L784) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1030_alg2_sector_frame.py](../../../../verification/v1030_alg2_sector_frame.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v1029: exact generic local tensor identities and the k=0 instability. *) {x, y, z} = Unique /@ {"x", "y", "z"}; k = {x, y, z}; basis = Join[ Table[Outer[Times, UnitVector[3, ii], UnitVector[3, ii]], {ii, 1, 3}], Table[With[{ii = pair[[1]], jj = pair[[2]]}, (Outer[Times, UnitVector[3, ii], UnitVector[3, jj]] + Outer[Times, UnitVector[3, jj], UnitVector[3, ii]])/Sqrt[2]], {pair, {{2, 3}, {1, 3}, {1, 2}}}] ]; bmat = Transpose[(#.k) & /@ basis]; trace = {1, 1, 1, 0, 0, 0}; k2 = k.k; v = Transpose[bmat].k; scalar = v - k2 trace; kp = IdentityMatrix[6] - Outer[Times, trace, trace]/2; kq = k2 (IdentityMatrix[6] - Outer[Times, trace, trace]) - 2 Transpose[bmat].bmat + Outer[Times, trace, v] + Outer[Times, v, trace]; check["v1029 generic local tensor constraint identities", zeroQ[bmat.Transpose[bmat] - (k2 IdentityMatrix[3] + Outer[Times, k, k])/2] && zeroQ[kq.Transpose[bmat]] && zeroQ[kp.scalar - Transpose[bmat].k] && PossibleZeroQ[scalar.scalar - 2 k2^2]]; r = Unique[]; zeroEnergy = Expand[(r trace).kp.(r trace)/2]; check["v1029 periodic k=0 trace mode has exact energy -3 r^2/4", zeroEnergy === -3 r^2/4]; (* v1030: actual connected-sector words span M4; a disconnected mutant leaves one extra commutant degree. *)](../../../../verification/wolfram/tfpt_round4.wl#L135)

## Research Contract — WOIT.OS.TWISTOR.01 (the Osterwalder–Schrader twistor bridge)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:12137-12469](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L12137) · `section:2db6bd35ce5c578613f3` · section

Typing. This is the actual bridge from compiler to physics — everything in CELEST.SEAM.01 is preparation for it. It is a research contract \ (ledger row WOIT.OS.TWISTOR.01: Open, research contract), not a claim; nothing below asserts that the construction exists. The external programme it engages — Woit's Euclidean Twistor Unification ( arXiv:2104.05099) — is a named reference frame for the shape of the target, never

Explicit source references:

- [verification/v615_gamma_toy_interacting.py](../../../../verification/v615_gamma_toy_interacting.py#L1) · explicit_file_citation
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_file_citation
- [verification/v522_woit_beta1_gso_gauge.py](../../../../verification/v522_woit_beta1_gso_gauge.py#L1) · explicit_file_citation
- [verification/v565_woit_beta3_pt_duality.py](../../../../verification/v565_woit_beta3_pt_duality.py#L1) · explicit_file_citation
- [verification/v519_woit_theta_rp_free.py](../../../../verification/v519_woit_theta_rp_free.py#L1) · explicit_script_identifier
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_file_citation
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v616_su2_internal_kinematic.py](../../../../verification/v616_su2_internal_kinematic.py#L1) · explicit_file_citation
- [SEAM.CLOCK.SILVER.01](../../../../verification/status_ledger.csv#L594) · explicit_claim_identifier · original status at linked ledger row
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v524_woit_beta2_os_quotient.py](../../../../verification/v524_woit_beta2_os_quotient.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [verification/v517_celestial_wp5e_m3_a0_uplift.py](../../../../verification/v517_celestial_wp5e_m3_a0_uplift.py#L1) · explicit_script_identifier
- [WOIT.THETA.FREE.01](../../../../verification/status_ledger.csv#L586) · explicit_claim_identifier · original status at linked ledger row
- [verification/v608_gamma_free_slice.py](../../../../verification/v608_gamma_free_slice.py#L1) · explicit_file_citation
- [verification/v527_seam_clock_silver_spectrum.py](../../../../verification/v527_seam_clock_silver_spectrum.py#L1) · explicit_file_citation
- [WOIT.BETA2.OS.01](../../../../verification/status_ledger.csv#L591) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.INT.FKTOY.01](../../../../verification/status_ledger.csv#L596) · explicit_claim_identifier · original status at linked ledger row
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v972_seam_interaction_front.py](../../../../verification/v972_seam_interaction_front.py#L1) · explicit_file_citation
- [WOIT.BETA1.GSO.01](../../../../verification/status_ledger.csv#L589) · explicit_claim_identifier · original status at linked ledger row
- [CELEST.SEAM.01](../../../../verification/status_ledger.csv#L556) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.THERMAL.KMS.01](../../../../verification/status_ledger.csv#L593) · explicit_claim_identifier · original status at linked ledger row
- [WOIT.BETA3.DUALITY.01](../../../../verification/status_ledger.csv#L604) · explicit_claim_identifier · original status at linked ledger row
- [verification/v528_seam_bit_twist_class_definition.py](../../../../verification/v528_seam_bit_twist_class_definition.py#L1) · explicit_script_identifier
- [SEAM.STRADDLE.CONE.01](../../../../verification/status_ledger.csv#L597) · explicit_claim_identifier · original status at linked ledger row
- [verification/v492_celestial_z4_orbifold.py](../../../../verification/v492_celestial_z4_orbifold.py#L1) · explicit_script_identifier
- [verification/v510_seam_bit_freedom.py](../../../../verification/v510_seam_bit_freedom.py#L1) · explicit_script_identifier
- [SEAM.INT.OSAVOID.01](../../../../verification/status_ledger.csv#L751) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.INT.ODDSPLIT.01](../../../../verification/status_ledger.csv#L750) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.TWISTOR.01](../../../../verification/status_ledger.csv#L584) · explicit_claim_identifier · original status at linked ledger row
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)
- [(* ==== v519 round: WOIT.THETA.FREE.01 -- the WOIT-alpha milestone of the OS twistor bridge: the real structure exists (two-family classification, mu4 torsor, Z8/C^4/Cl(16) levels) and the exact free-RP preconditions + site-cut degeneration + continuum control. The 40-digit positive- definiteness inertia certificates of the bond-cut Grams (R3/R5) are Python-only by the suite convention (mpmath eigh at dps 40). Mirrors v519. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7077)
- [(* ==== v524 round: WOIT.BETA2.OS.01 -- "the OS quotient of the free system made explicit" (verdict SUCCESS, [C]-typed per contract precision (iii)). Four exact mirrors: (i) the euclidean-rotation preconditions (alpha_1^N = (-1)^F wrap arithmetic at N = 16 and N = 8) + the exact PD certificate identity sin^2(3pi/8) - sin(pi/8) sin(5pi/8) = 1/2; (ii) the Klein-Landau one-particle transfer forms tau_k on the shrinking domains at N = 16, k = 1..7: exactly Hermitian, odd k with exactly ZERO diagonal (the C(even) = 0 checkerboard), even k = 2j obeying the exact square identity tau_2j(a, b) = <alpha_j a, alpha_j b> entrywise; (iii) the clock identities (C(9) = C(7), C(11) = C(5), the transparency product formula sin(7pi/16) - sin(5pi/16) = 2 cos(3pi/8) sin(pi/16) > 0) + the N = 8 compressed clock spectrum EXACTLY {1, sqrt(2)-1} = {1, 1/delta_S} via the generalized eigenvalues of (tau_2, G) on the one-particle domain, with sin(pi/8)/sin(3pi/8) = sqrt(2)-1; (iv) the pre-declared KMS witnesses (C(1)/C(3) = 1 + sqrt(2) = delta_S at N = 8; -(C5-C7)((C3-C7)+(C5-C7)) < 0 exactly at N = 16, i.e. det(G - tau_4) < 0 on the odd one-particle clock block). The 37x37/16x16 H_phys Grams, the 40-digit inertia certificates, the spectral projections and the reconstructed rotation group are numerical (mpmath eighe), Python-only, flagged here. Mirrors v524. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7965)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [(* ==== v527 round: SEAM.CLOCK.SILVER.01 -- silver explained / demystified. Exact mirrors: (i) tan(pi/8) Hankel pencil; (ii) N-scaling witness; (iii) gap = arcsinh(1) = gd^{-1}(pi/4). Census Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8187)
- [(* ==== v528 round: SEAM.BIT.TWISTCLASS.01 -- bit = twist-class choice. Exact mirrors: (i) cardinality lemma; (ii) 224-axis flip census; (iii) O-values. Pfaffian spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8213)
- [(* ==== v522 round: WOIT.BETA1.GSO.01 -- "the clock is time-like, GSO is the gauge datum": the Z8/NS tower + Ramond control, the invariant- dimension chain, the time-like reflection census, the exact Hermiticity witness of the clock insertion, the GSO 2-torsion census and the family-A tower-normalisation failure. The 40-digit GSO-fixed RP inertia certificates ((29,0,0)/(8,0,0)/(7,9,6)/(17,12,0)) are Python-only by the suite convention. Mirrors v522. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7609)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v517 round: CELEST.WP5E.M3.01 -- "the a0 uplift": milestone M3 of the CELEST.SEAM.01 back-reaction programme executed (SUCCESS on the preregistered v514 S8.3 criterion). Six exact mirrors: (i) the GH multipole ledger (selection rule m = 0 mod 4, (4, +-4) amplitude (35/16) sin^4 th) + the twistor family at general orbit phase (e1 = e3 = 0, a2 = 4 z0 zb0 zeta^2, a0(zeta), v515 slice), (ii) the kernel bridge (null coordinate: any kernel harmonic; residue V-ledger identity 1/(2r); source flux -4 pi per centre), (iii) the asymptotic kernel log (coefficient 4 = |mu4|, first seam correction a0/eta^4, exact m-grading, GLT tower p_{4k} = 4(-a0)^k with the n = 0 mod 4 selection rule, no log x power terms), (iv) the exceptional-locus log (chi(0) = log a0 = 4 log t0 + i(4 phi0 + pi), modulus response 1 at the locus vs power-law at infinity), (v) the period response (linear in t0, d log Pi/d log a0 = 1/4 = 1/|mu4|, integrated monodromy i = one Coxeter clock step, centre permutation, a0-rigid node support, K4 discriminants ~ t0^2), and (vi) the negative controls ((4,0) clock-invariant, Z2/EH reads 2 on every dial, k = 3/5 orbits move the coefficient, the forbidden family fails both dials). The contour-transform typing itself is the [C] GLT dictionary; the BM kernel anchor is already mirrored in the v515 round. Mirrors v517. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L6678)
- [(* ==== v510 round: SEAM.BIT.FREEDOM.01 -- the freedom attack on the v506/v507 alignment bit: the POSITION half of the bit is topology. Exact content mirrored: (i) the DIHEDRAL CENSUS -- on the refined 2N-point seam circle D_16 has 17 involutions with EXACTLY ONE free (the antipodal shift by 8) and all 16 reflections have exactly 2 circle fixed points (8 site-axis + 8 edge-axis; robustness N = 8, 12; odd control N = 9: zero free), plus the quotient topology chi(C/antipode) = 0 (circle) vs chi(C/reflection) = 1 (interval, 2 boundary corners); (ii) the AUT COMPLETENESS -- Aut(C_8) = D_8 by brute force over all 8! = 40320 permutations and Aut(C_16) = D_16 by degree-2 propagation (all 32 candidates), so the census covers ALL circle symmetries; (iii) the Cl(16) DICHOTOMY CENSUS -- on explicit 256x256 Jordan-Wigner gammas the free deck's NS implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the implementers of ALL 16 reflections exist (one of the two spin lifts +-R) and square to SCALARS {2^7 (site-axis), 2^8 (edge-axis)} (split): NONSPLIT <=> FREE over the complete census; root dichotomy 2 (the +-quarter shifts) vs 0 total over all 16 reflections; (iv) the REAL-STRUCTURE TABLE -- the deck-commuting antiholomorphic involutions solve symbolically to exactly two families (M diagonal: mu conj z, fix line through the poles; M antidiagonal: mu/conj z, fix circle |z| = sqrt mu), and the unique mark-fixing real structure per configuration is equatorial/FREE for mu4 and generic-unit, real-axis/NOT-free for silver and generic-real, and NONEXISTENT for the hexagonal frame; (v) HARMONIC + FREE => mu4 -- the deck-pair cross-ratio (1-b)^2/(1+b)^2 = -1 solves exactly to b = +-i, with the lambda table (2, 1/2, 3/4, 5/4) real and the hexagonal lambda complex; (vi) the HONEST COUNTERWITNESSES -- the discrete witness {0,1,8,9} (shift-invariant, crossing, but not quarter-shift-invariant) and the continuous witness {+-1, +-(3+4i)/5} (pair cross-ratio -1/4, j = 148176/25 != 1728, clock does not preserve): the Fock dichotomy measures the CLASS, not the modulus. The Moebius/Klein covering models and the pillowcase branch control stay Python-side (v510). Mirrors v510. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5155)

## Research Contract — CCC.SEAM.CROSSOVER.01 (the conformal-cyclic crossover on the seam geometry)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:12470-12570](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L12470) · `section:2a4b108348409f980f6d` · section

Typing. A research contract \ (ledger row CCC.SEAM.CROSSOVER.01: Open, research contract), not a claim. It engages Penrose's Conformal Cyclic Cosmology (Tod, arXiv:1309.7248; Penrose–Meissner, arXiv:2503.24263) as a named reference frame for the shape of the target — never a confirmation in either direction. The cyclic reading of origin_theory stays \ regardless of this contract's fate; nothing below asserts that CCC

Explicit source references:

- [verification/v522_woit_beta1_gso_gauge.py](../../../../verification/v522_woit_beta1_gso_gauge.py#L1) · explicit_script_identifier
- [CCC.SEAM.KINEMATICS.01](../../../../verification/status_ledger.csv#L737) · explicit_claim_identifier · original status at linked ledger row
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_script_identifier
- [verification/v976_seam_lift_birkhoff.py](../../../../verification/v976_seam_lift_birkhoff.py#L1) · explicit_file_citation
- [VGEO.TORSOR.01](../../../../verification/status_ledger.csv#L670) · explicit_claim_identifier · original status at linked ledger row
- [CCC.SEAM.CROSSOVER.01](../../../../verification/status_ledger.csv#L738) · explicit_claim_identifier · original status at linked ledger row
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_script_identifier
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_file_citation
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)
- [(* ==== v522 round: WOIT.BETA1.GSO.01 -- "the clock is time-like, GSO is the gauge datum": the Z8/NS tower + Ramond control, the invariant- dimension chain, the time-like reflection census, the exact Hermiticity witness of the clock insertion, the GSO 2-torsion census and the family-A tower-normalisation failure. The 40-digit GSO-fixed RP inertia certificates ((29,0,0)/(8,0,0)/(7,9,6)/(17,12,0)) are Python-only by the suite convention. Mirrors v522. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7609)

## Firewall Contract — DIMENSION.UPLIFT.FIREWALL.01 (no [formula in source] D theorem closes a [formula in source] D claim)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:12571-12632](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L12571) · `section:fd8a259cd96f2b7b4df5` · section

Typing. A standing discipline rule, in force immediately (ledger row DIMENSION.UPLIFT.FIREWALL.01); the uplift theorems it names are separate \ contracts. It formalizes the core diagnosis of the 2026-08-27 external deep review: a chiral [formula in source] D seam net does not imply a local, interacting [formula in source] D quantum world. The corpus's strongest finite results are boundary/kinematic building blocks — 

Explicit source references:

- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [CELEST.SEAM.01](../../../../verification/status_ledger.csv#L556) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [experiments/tfpt-discovery/ccc_uplift_4d_probe.py](../../../../experiments/tfpt-discovery/ccc_uplift_4d_probe.py#L1) · explicit_file_citation
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_script_identifier
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — SEAM.BULK4D.RECON.01 (from seam data to a 4D local quantum theory)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:12633-12686](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L12633) · `section:73dd631de817637ce12d` · section

Typing. A research contract \ (ledger row SEAM.BULK4D.RECON.01: Open, research contract), not a claim. It makes explicit the theorem that was previously only implicit between the SEAM.EQUIV.01 conclusion (a chiral [formula in source] boundary object) and the WOIT.OS.TWISTOR.01 goal statement (a Poincar\'e-covariant, causal, chiral 4D theory): the missing seam [formula in source] bulk reconstruction is a theorem of it

Explicit source references:

- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_script_identifier
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [verification/v377_seam_s3_e8character.py](../../../../verification/v377_seam_s3_e8character.py#L1) · explicit_script_identifier
- [verification/v1020_spectator_sector_obstruction.py](../../../../verification/v1020_spectator_sector_obstruction.py#L1) · explicit_file_citation
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v524_woit_beta2_os_quotient.py](../../../../verification/v524_woit_beta2_os_quotient.py#L1) · explicit_script_identifier
- [verification/v519_woit_theta_rp_free.py](../../../../verification/v519_woit_theta_rp_free.py#L1) · explicit_script_identifier
- [BULK.PRIME_COMPLETION.01](../../../../verification/status_ledger.csv#L773) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [(* ==== v519 round: WOIT.THETA.FREE.01 -- the WOIT-alpha milestone of the OS twistor bridge: the real structure exists (two-family classification, mu4 torsor, Z8/C^4/Cl(16) levels) and the exact free-RP preconditions + site-cut degeneration + continuum control. The 40-digit positive- definiteness inertia certificates of the bond-cut Grams (R3/R5) are Python-only by the suite convention (mpmath eigh at dps 40). Mirrors v519. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7077)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ==== v524 round: WOIT.BETA2.OS.01 -- "the OS quotient of the free system made explicit" (verdict SUCCESS, [C]-typed per contract precision (iii)). Four exact mirrors: (i) the euclidean-rotation preconditions (alpha_1^N = (-1)^F wrap arithmetic at N = 16 and N = 8) + the exact PD certificate identity sin^2(3pi/8) - sin(pi/8) sin(5pi/8) = 1/2; (ii) the Klein-Landau one-particle transfer forms tau_k on the shrinking domains at N = 16, k = 1..7: exactly Hermitian, odd k with exactly ZERO diagonal (the C(even) = 0 checkerboard), even k = 2j obeying the exact square identity tau_2j(a, b) = <alpha_j a, alpha_j b> entrywise; (iii) the clock identities (C(9) = C(7), C(11) = C(5), the transparency product formula sin(7pi/16) - sin(5pi/16) = 2 cos(3pi/8) sin(pi/16) > 0) + the N = 8 compressed clock spectrum EXACTLY {1, sqrt(2)-1} = {1, 1/delta_S} via the generalized eigenvalues of (tau_2, G) on the one-particle domain, with sin(pi/8)/sin(3pi/8) = sqrt(2)-1; (iv) the pre-declared KMS witnesses (C(1)/C(3) = 1 + sqrt(2) = delta_S at N = 8; -(C5-C7)((C3-C7)+(C5-C7)) < 0 exactly at N = 16, i.e. det(G - tau_4) < 0 on the odd one-particle clock block). The 37x37/16x16 H_phys Grams, the 40-digit inertia certificates, the spectral projections and the reconstructed rotation group are numerical (mpmath eighe), Python-only, flagged here. Mirrors v524. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7965)

## Research Contract — BULK.PRIME_COMPLETION.01 (prime/seam-generated completions, no spectator)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:12687-12725](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L12687) · `section:f287beabd75c01fb7360` · section

Typing. A research contract \ (ledger row BULK.PRIME_COMPLETION.01: Open, research contract), not a claim. Registered 2026-09-04 from the r644 audit harvest; it replaces the ``unique from seam data alone'' reading of SEAM.BULK4D.RECON.01/B7 by uniqueness in the category of seam-generated (prime) completions. Dimension typing ( DIMENSION.UPLIFT.FIREWALL.01 F2): the hypothesis is [formula in source] D free-fermion, the

Explicit source references:

- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1020_spectator_sector_obstruction.py](../../../../verification/v1020_spectator_sector_obstruction.py#L1) · explicit_file_citation
- [BULK.PRIME_COMPLETION.01](../../../../verification/status_ledger.csv#L773) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — QFT4D.OS.RECON.01 (the genuine 4D Euclidean lattice package)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:12869-12959](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L12869) · `section:c01350c4771209b4c9e1` · section

Typing. A research contract \ (ledger row QFT4D.OS.RECON.01: Open, research contract), not a claim. This is step (3) of the DIMENSION.UPLIFT.FIREWALL.01 route ordering: the nonperturbative 4D existence statement that no perturbative or seam-level result can substitute for.

Explicit source references:

- [verification/v1013_thermodynamic_dynamics.py](../../../../verification/v1013_thermodynamic_dynamics.py#L1) · explicit_file_citation
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_file_citation
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.EG.ALLORDER.01](../../../../verification/status_ledger.csv#L444) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1008_master_assembly_scaffold.py](../../../../verification/v1008_master_assembly_scaffold.py#L1) · explicit_file_citation
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [verification/v989_lattice_gate_battery.py](../../../../verification/v989_lattice_gate_battery.py#L1) · explicit_file_citation
- [verification/v381_qft4d_eg_allorder.py](../../../../verification/v381_qft4d_eg_allorder.py#L1) · explicit_script_identifier

## Research Contract — CHIRAL4D.NOMIRROR.01 (the chiral 4D lattice matter theorem)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:12960-13028](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L12960) · `section:11cf2220db595f7b5339` · section

Typing. A research contract \ (ledger row CHIRAL4D.NOMIRROR.01: Open, research contract), not a claim. Step (4) of the firewall route ordering: chirality and mirror decoupling must be proven in the same 4D model that QFT4D.OS.RECON.01 constructs — the seam's [formula in source] and Chern/inflow structure are a boundary- anomaly signal, not yet 4D matter.

Explicit source references:

- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_file_citation
- [verification/v997_spin2_smg_witnesses.py](../../../../verification/v997_spin2_smg_witnesses.py#L1) · explicit_file_citation
- [verification/v989_lattice_gate_battery.py](../../../../verification/v989_lattice_gate_battery.py#L1) · explicit_file_citation
- [docs/OPEN_PROBLEMS.md](../../../../docs/OPEN_PROBLEMS.md#L1) · explicit_file_citation
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v997) GRAV.SPIN2.EMERGENCE.01: Barnes-Rivers ranks (5,3,1,1) ---- Python-only: Weyl^2 ghost residues, random-p numeric, SMG N=8 Fidkowski-Kitaev toy (spectrum / Spin(7) / Schmidt / edge). *)](../../../../verification/wolfram/tfpt_readouts.wl#L699)

## Research Contract — CHIRAL4D.MIRROR.DET16.01 (DET16 rank-one projector, finite cluster)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13029-13091](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13029) · `section:6ce553746490f88b0988` · section

Typing. A candidate \ (ledger row CHIRAL4D.MIRROR.DET16.01), registered 2026-08-29 from review wave 5. ( v1002_ spin10_ mirror_ projector.py.) Content. Exact finite-cluster gapping on the full chiral [formula in source] Fock space via the number-violating determinant vertex, as executed above. Open. Dynamical gauge fields, domain-wall geometry, and a [formula in source] D volume theorem — this is not a [formula in so

Explicit source references:

- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.MIRROR.DFILTER.BLOCK.01](../../../../verification/status_ledger.csv#L776) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [verification/v1007_det16_stability_battery.py](../../../../verification/v1007_det16_stability_battery.py#L1) · explicit_file_citation
- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_file_citation
- [verification/v1023_derivative_filtered_wall.py](../../../../verification/v1023_derivative_filtered_wall.py#L1) · explicit_file_citation

## Firewall Contract — GRAV.NONCIRCULAR.01 (the Bisognano–Wichmann direction discipline)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13092-13141](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13092) · `section:136a1e576865c1424f29` · section

Typing. A standing discipline rule, in force immediately (ledger row GRAV.NONCIRCULAR.01), with an audit census at registration. Bisognano–Wichmann (BW) is a theorem within an already-local, Poincar\'e-covariant QFT with a suitable vacuum: the modular flow of a wedge algebra acts as the boost. It is not a device that generates Lorentz spacetime from an arbitrary modular flow — there exist Poincar\'e-covariant nets vi

Explicit source references:

- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v446_seam_clock_invariance.py](../../../../verification/v446_seam_clock_invariance.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [verification/v478_entropic_continuum_legs.py](../../../../verification/v478_entropic_continuum_legs.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v215_seam_deck_killtest.py](../../../../verification/v215_seam_deck_killtest.py#L1) · explicit_script_identifier
- [verification/v440_seam_lto_rp_beta.py](../../../../verification/v440_seam_lto_rp_beta.py#L1) · explicit_script_identifier
- [verification/v438_seam_hsmi_borchers.py](../../../../verification/v438_seam_hsmi_borchers.py#L1) · explicit_script_identifier
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamRigidityForcing.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamRigidityForcing.lean#L1)
- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamStandardPair.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamStandardPair.lean#L1)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)

## Research Contract — OBS.TRANSDUCTION.01 (the transduction principle: eigenvalue, projection, coupling)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13142-13187](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13142) · `section:e37df96de6e66060644b` · section

Typing. A research contract (ledger row OBS.TRANSDUCTION.01); the principle is machine-checked on the minimal model at exploration level, the per-bundle transduction proofs are . It elevates the S15 typing rule to a named principle: [formula in source] Without the middle arrow, neither a non-observation falsifies nor an observation confirms. The minimal model is machine-checked in experiments/ theory-contracts/ fo01_

Explicit source references:

- [experiments/theory-contracts/fo01_transduction_invisibility.py](../../../../experiments/theory-contracts/fo01_transduction_invisibility.py#L1) · explicit_file_citation
- [verification/v990_wj_transduction_mechanism.py](../../../../verification/v990_wj_transduction_mechanism.py#L1) · explicit_file_citation
- [OBS.TRANSDUCTION.01](../../../../verification/status_ledger.csv#L748) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — PRED.JOINTLIKELIHOOD.01 (from hit-counting to overdetermined relations)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13188-13235](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13188) · `section:66ed6033e537375adb6f` · section

Typing. A research contract \ (ledger row PRED.JOINTLIKELIHOOD.01: Open, statistics-construction contract), not a claim. The [formula in source] individually matched values all descend from the same few atoms ( [formula in source] , [formula in source] , [formula in source] , [formula in source] ) and are therefore statistically correlated: counting hits overstates independent evidence. The evidence is to be reorgani

Explicit source references:

- [verification/v84_frozen_registry.py](../../../../verification/v84_frozen_registry.py#L1) · explicit_script_identifier
- [verification/v100_numerology_null_mc.py](../../../../verification/v100_numerology_null_mc.py#L1) · explicit_script_identifier
- [verification/v992_joint_likelihood_v1.py](../../../../verification/v992_joint_likelihood_v1.py#L1) · explicit_file_citation
- [docs/FALSIFICATION.md](../../../../docs/FALSIFICATION.md#L1) · explicit_file_citation
- [OBS.TRANSDUCTION.01](../../../../verification/status_ledger.csv#L748) · explicit_claim_identifier · original status at linked ledger row
- [PRED.JOINTLIKELIHOOD.01](../../../../verification/status_ledger.csv#L749) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ---- (v84) frozen registry decimals recompute from the axioms ---- *) phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); FU1[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 41 Log[1/phiseam[a]]; aStar = a /. FindRoot[FU1[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; check["v84 ALPHA_INV frozen", 1/aStar, 137.0359992168407125035379`30, 10^-20]; lamC = Sqrt[phi0 (1 - phi0)]; check["v84 SIN2_THETA12_SEED frozen", 1/3 - phi0/2, 0.3067473572449105696786871`30, 10^-20]; check["v84 SIN2_THETA13 frozen", phi0 Exp[-5/6], 0.02310843515888110429328466`30, 10^-20]; check["v84 BETA_BIREFRINGENCE_DEG frozen", (phi0/(4 Pi)) (180/Pi), 0.2424350309009295284924315`30, 10^-20]; check["v84 OMEGA_B frozen", (1 - 1/(4 Pi)) phi0, 0.04894066266545011220054565`30, 10^-20]; check["v84 LAMBDA_C frozen", lamC, 0.2243762368847217731120972`30, 10^-20]; check["v84 S23_CKM frozen", phi0/(1 + lamC), 0.04342778843220215630289116`30, 10^-20]; check["v84 S13_CKM frozen", lamC^3/3, 0.003765384454486429837965432`30, 10^-20]; check["v84 DELTA_CKM_RAD frozen", Pi/3 + 3 lamC^2, 1.198231638232244084651243`30, 10^-20]; check["v84 MMU_OVER_MTAU frozen", (8/7) phi0, 0.06076794534496631692490568`30, 10^-20]; check["v84 ME_OVER_MMU frozen", (12/7) phi0^2, 0.004846725425651567674771059`30, 10^-20]; checkExact["v84 MU_OVER_MD = 55/117 exactly", 55/117 == 55/117]; check["v84 MC_OVER_MS frozen", (34/47)/phi0, 13.60499710285539356302651`30, 10^-20]; check["v84 MT_OVER_MB frozen", (3/26)/phi0^2, 40.8115130177002629681607`30, 10^-20]; check["v84 MSCAL_OVER_MBAR frozen", c3^(7/2), 0.00001256494208322844896998079`30, 10^-20]; check["v84 RHOL_OVER_MBAR4 frozen", (3/(4 Pi^2)) Exp[-2/aStar], 7.125329526706216792033797`30 10^-121, 10^-15]; checkExact["v84 theta12 variants distinct (seed < seam < nonlin band)", (1/3 - phi0/2) < (1/3 - 1/(12 Pi))]; (* ---- (v85) master cover: GL(2) covariance on the anchor plane ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L38)

## Verified Selector — DIMENSION.SELECTOR.4D.01 (why [formula in source] , conditionally)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13343-13377](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13343) · `section:ccf4833d317bae46eaf7` · section

Typing. A conditional identity \ (ledger row DIMENSION.SELECTOR.4D.01), machine-checked in v975_dimension_selector_4d.py ( [formula in source] , sympy-exact). The [formula in source] structure of the compiler must not be read as a proof of four spacetime dimensions ( DIMENSION.UPLIFT.FIREWALL.01); what is checkable is a selector theorem under a named axiom set. Statement. Under A1 [formula in source] (propagating loc

Explicit source references:

- [verification/v975_dimension_selector_4d.py](../../../../verification/v975_dimension_selector_4d.py#L1) · explicit_file_citation
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — SEAM.SIMPLECURRENT.GENERATOR.01 (one generator instead of 128 currents)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13378-13529](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13378) · `section:c9d9fdab1f8620914792` · section

Typing. A research contract \ (ledger row SEAM.SIMPLECURRENT.GENERATOR.01), not a claim. Context. The seam coverage carve ( v973_seam_route_narrowing.py) shows the [formula in source] fermion-bilinear half of the seam target is covered by the cited scaling-limit theorem; the named residual is N1 (the [formula in source] /GSO extension [formula in source] as a net statement — the 128 spinor currents are not bilinears)

Explicit source references:

- [verification/v993_minimal_defect_selector.py](../../../../verification/v993_minimal_defect_selector.py#L1) · explicit_file_citation
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v994_mmst_criteria_battery.py](../../../../verification/v994_mmst_criteria_battery.py#L1) · explicit_script_identifier
- [verification/v983_simple_current_generator.py](../../../../verification/v983_simple_current_generator.py#L1) · explicit_file_citation
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v624_external_lattice_audit.py](../../../../verification/v624_external_lattice_audit.py#L1) · explicit_script_identifier
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [verification/v988_psi_lambda_reduction.py](../../../../verification/v988_psi_lambda_reduction.py#L1) · explicit_file_citation
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v813_p1_index_kms.py](../../../../verification/v813_p1_index_kms.py#L1) · explicit_script_identifier
- [verification/v469_seam_crossedproduct_route.py](../../../../verification/v469_seam_crossedproduct_route.py#L1) · explicit_script_identifier
- [verification/v973_seam_route_narrowing.py](../../../../verification/v973_seam_route_narrowing.py#L1) · explicit_file_citation
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_script_identifier
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v998_seam_modular_closure.py](../../../../verification/v998_seam_modular_closure.py#L1) · explicit_file_citation
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [verification/v484_seam_contact_unit.py](../../../../verification/v484_seam_contact_unit.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [(* v469 (i): the LR locality integers of both extension routes *) hs = 16/16; (* so(N)_1 spinor weight N/16, N = 16 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2930)
- [(* ---- (v983) SEAM.SIMPLECURRENT.GENERATOR.01: glue vector lambda = (omega_s, omega_f) ---- *) Module[{omegaS, omegaF, lam, inD5, inA3, inL0, gensD5, gensA3, dots, cosetRoots, census, lamV, omega2, nV, n2, cartanD8}, omegaS = ConstantArray[1/2, 5]; omegaF = {3/4, -1/4, -1/4, -1/4}; lam = Join[omegaS, omegaF]; inD5[x_] := (And @@ (IntegerQ /@ x)) && EvenQ[Total[x]]; inA3[y_] := (And @@ (IntegerQ /@ y)) && Total[y] === 0; inL0[z_] := inD5[Take[z, 5]] && inA3[Take[z, {6, 9}]]; checkExact["v983 NORMS+WEIGHT [E]: |omega_s|^2=5/4, |omega_f|^2=3/4, |lambda|^2=2, h_lambda=1", Total[omegaS^2] === 5/4 && Total[omegaF^2] === 3/4 && Total[lam^2] === 2 && Total[lam^2]/2 === 1]; checkExact["v983 ORDER FOUR [E]: 4*lambda in D5(+)A3, lambda and 2*lambda not -- [lambda] generates the diagonal Z4", inL0[4 lam] && ! inL0[2 lam] && ! inL0[lam]]; gensD5 = {{1, 1, 0, 0, 0}, {1, -1, 0, 0, 0}, {0, 1, 1, 0, 0}, {0, 0, 1, 1, 0}, {0, 0, 0, 1, 1}}; gensA3 = {{1, -1, 0, 0}, {0, 1, -1, 0}, {0, 0, 1, -1}}; dots = Join[omegaS . # & /@ gensD5, omegaF . # & /@ gensA3]; checkExact["v983 ISOTROPY+UNIMODULAR [E]: lambda.L0 subset Z on a generator set; det(D5)*det(A3)=16, index-4 glue => det L=1", (And @@ (IntegerQ /@ dots)) && 16/4^2 === 1]; cosetRoots[k_] := Module[{t = k lam, d5, a3}, d5 = Counts @ Select[ Total[(# + Take[t, 5])^2] & /@ Select[Tuples[Range[-5, 3], 5], EvenQ[Total[#]] &], # <= 2 &]; a3 = Counts @ Select[ Total[(Join[#, {-Total[#]}] + Take[t, {6, 9}])^2] & /@ Tuples[Range[-6, 6], 3], # <= 2 &]; Total[KeyValueMap[#2 Lookup[a3, 2 - #1, 0] &, d5]]]; census = Table[cosetRoots[k], {k, 0, 3}]; checkExact["v983 COSET ROOT CENSUS [E]: norm-2 vectors per fusion power k=0..3 = {52,64,60,64}, total 240; odd powers 64+64=128", census === {52, 64, 60, 64} && Total[census] === 240 && census[[2]] + census[[4]] === 128]; lamV = Join[{1, 0, 0, 0, 0}, omegaF]; omega2 = {1/2, 1/2, -1/2, -1/2}; nV = Total[lamV^2]; n2 = Total[omegaS^2] + Total[omega2^2]; cartanD8 = {{2, -1, 0, 0, 0, 0, 0, 0}, {-1, 2, -1, 0, 0, 0, 0, 0}, {0, -1, 2, -1, 0, 0, 0, 0}, {0, 0, -1, 2, -1, 0, 0, 0}, {0, 0, 0, -1, 2, -1, 0, 0}, {0, 0, 0, 0, -1, 2, -1, -1}, {0, 0, 0, 0, 0, -1, 2, 0}, {0, 0, 0, 0, 0, -1, 0, 2}}; checkExact["v983 KILLS+HOLOMORPHY SHADOW [E]: vector glue (v,omega_f) norm 7/4 and mismatched (omega_s, omega_2) norm 9/4 not in 2Z; det Cartan D8=4 vs glued det=1", nV === 7/4 && n2 === 9/4 && Det[cartanD8] === 4 && 16/4^2 === 1]; ]; (* ---- (v985) ALPHA.QUILLEN.EXACT.01: mu4 circulant spectra + graded channel swap ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L444)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* v463 (ii): the (E8)_1 tower = E4/eta^8 coefficients {1,248,4124,34752,213126} *) inv8 = Series[Product[(1 - q^n)^-8, {n, 1, 6}], {q, 0, 5}]; chiSer = Series[(1 + 240 Sum[DivisorSigma[3, n] q^n, {n, 1, 6}]) inv8, {q, 0, 5}]; tower = CoefficientList[Normal[chiSer], q][[1 ;; 5]]; checkExact["v463 SEAM.EQUIV.UNIQ.01 (ii): the holomorphic c=8 partition function is the unique j^{1/3}=E4/eta^8, whose q-coefficients are the (E8)_1 tower {1,248,4124,34752,213126} -- the q^1=248 is the forced weight-1 dimension (Dong-Mason/Schellekens: the holomorphic c=8 VOA is unique = V_{E8})", tower == {1, 248, 4124, 34752, 213126}]; ]; (* ==== v469 round: the net-level crossed-product certification -- the LR locality integers (h_s(SO(16)_1) = 16/16 = 1 in Z; the mu4 glue h(J^k) = {1,1,1} all integer), the KLM mu-index arithmetic (4/2^2 = 1 and 16/4^2 = 1, both holomorphic) and the Kitaev 16-fold-way pin (nu = 16 x |C| = 16 = 0 mod 16, c_- = nu/2 = 8 = g_car+N_fam); mirrors v469 (the FHS Chern itself is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2916)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ---- (v993) AX.P2.01 census: SNF disc groups, unique (D5,A3), [lambda]^2=[v], CE dims ---- Python-only: random CE axiom sampling on M_d^{Z4} / crossed product. *)](../../../../verification/wolfram/tfpt_readouts.wl#L557)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean#L1)
- [(* ---- (v994) SEAM.EQUIV.MMST.01 C3: Theta_E8 / eta^8 = {1,248,4124,34752} ---- Python-only: C1 entropy, C2 QWZ spectrum, C4 two-point numeric, C5 sector recombination beyond det, C6 cited, C7 open, GSO/N=8 must-fail combinatorics. *)](../../../../verification/wolfram/tfpt_readouts.wl#L680)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)

## Research Contract — TFPT4D.LATTICE.ACTION.01 (the explicit finite 4D lattice action and its seven finite gates)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13530-13615](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13530) · `section:0a835f45f6d36c79eb46` · section

Typing. A research contract \ (ledger row TFPT4D.LATTICE.ACTION.01); route step (2) of the DIMENSION.UPLIFT.FIREWALL.01 ordering made concrete — the single object on which nearly all open 4D questions become simultaneously testable. Demand. Exhibit one fully explicit finite family of 4D Euclidean lattice theories [formula in source] where [formula in source] are the fundamental holonomies (TFPT fixes representation c

Explicit source references:

- [verification/v989_lattice_gate_battery.py](../../../../verification/v989_lattice_gate_battery.py#L1) · explicit_file_citation
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1008_master_assembly_scaffold.py](../../../../verification/v1008_master_assembly_scaffold.py#L1) · explicit_file_citation
- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_file_citation
- [verification/v1013_thermodynamic_dynamics.py](../../../../verification/v1013_thermodynamic_dynamics.py#L1) · explicit_file_citation

## Research Contract — SEAM.DETLINE.UNIFICATION.01 (the determinant-line unification hypothesis)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13616-13662](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13616) · `section:ce12b2c64758813c083c` · section

Typing. A research hypothesis contract \ (ledger row SEAM.DETLINE.UNIFICATION.01) — a precise conjecture, not a result. Observation. Three separately open structures may be projections of one geometric object: (1) the seam extension is described by a Q-system/simple current ( SEAM.SIMPLECURRENT.GENERATOR.01); (2) the chiral fermion measure lives on a determinant line ( CHIRAL4D.NOMIRROR.01 demand C1); (3) anomalies a

Explicit source references:

- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [verification/v991_detline_bulk_edge.py](../../../../verification/v991_detline_bulk_edge.py#L1) · explicit_file_citation
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v977_transfer_unistochastic_wilson.py](../../../../verification/v977_transfer_unistochastic_wilson.py#L1) · explicit_file_citation
- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_file_citation
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.DETLINE.UNIFICATION.01](../../../../verification/status_ledger.csv#L758) · explicit_claim_identifier · original status at linked ledger row
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_file_citation

## Research Contract — FTRANSFER.GENERATING.01 (four transfer bridges from one generating functional)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13663-13696](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13663) · `section:1fc598d7241c419069ab` · section

Typing. A research contract \ (ledger row FTRANSFER.GENERATING.01); the constructive successor named by the FR.TRANSFER.01 typing guard. The four continuous-transfer interfaces ( [formula in source] : source masses [formula in source] pole, v183; [formula in source] : CP source [formula in source] , v169/ v184; [formula in source] : [formula in source] , v185; [formula in source] : [formula in source] , v164) are cur

Explicit source references:

- [verification/v164_qcd_scale.py](../../../../verification/v164_qcd_scale.py#L1) · explicit_script_identifier
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier
- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row
- [verification/v990_wj_transduction_mechanism.py](../../../../verification/v990_wj_transduction_mechanism.py#L1) · explicit_file_citation
- [verification/v169_etaB_boltzmann_interface.py](../../../../verification/v169_etaB_boltzmann_interface.py#L1) · explicit_script_identifier
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [FR.TRANSFER.01](../../../../verification/status_ledger.csv#L181) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_script_identifier
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)

## Research Contract — GAUGE.DETLINE.FIXPOINT.01 (all three gauge couplings from one zeta-det functional)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13697-13755](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13697) · `section:d5ab0f60059af6a8fe27` · section

Typing. A research contract \ (ledger row GAUGE.DETLINE.FIXPOINT.01), registered 2026-08-28 from review wave 3. Demand. All three gauge couplings ( [formula in source] / equivalently [formula in source] , [formula in source] , [formula in source] ) arise as stationary points of one nonabelian zeta-det / inflow functional on the determinant line — the nonabelian upgrade of the [formula in source] face ALPHA.QUILLEN.EX

Explicit source references:

- [verification/v1008_master_assembly_scaffold.py](../../../../verification/v1008_master_assembly_scaffold.py#L1) · explicit_file_citation
- [verification/v996_gauge_grammar_kill.py](../../../../verification/v996_gauge_grammar_kill.py#L1) · explicit_script_identifier
- [experiments/tfpt-discovery/gauge_stiffness_stepscaling_probe.py](../../../../experiments/tfpt-discovery/gauge_stiffness_stepscaling_probe.py#L1) · explicit_file_citation
- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/gauge_stiffness_fixpoint_probe.py](../../../../experiments/tfpt-discovery/gauge_stiffness_fixpoint_probe.py#L1) · explicit_file_citation
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — GRAV.SPIN2.EMERGENCE.01 (massless transversal spin-2 from the same spectral determinant)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13756-13823](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13756) · `section:e4bb9a238c9f340ff5d1` · section

Typing. A research contract \ (ledger row GRAV.SPIN2.EMERGENCE.01), registered 2026-08-28 from review wave 3. Demand. From the same spectral determinant that carries the gauge fixpoints, a massless transversal spin-2 pole with two helicities, universal [formula in source] coupling, diffeomorphism Ward identities, and positive Hessian / reflection-positive transfer. Relation. The entanglement-equilibrium Einstein equa

Explicit source references:

- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.WEINBERG.WITTEN.01](../../../../verification/status_ledger.csv#L770) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1000_spin2_sk_witnesses.py](../../../../verification/v1000_spin2_sk_witnesses.py#L1) · explicit_file_citation
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [verification/v997_spin2_smg_witnesses.py](../../../../verification/v997_spin2_smg_witnesses.py#L1) · explicit_file_citation
- [GRAV.PARENT.GAP.NO_GO.01](../../../../verification/status_ledger.csv#L778) · explicit_claim_identifier · original status at linked ledger row
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ---- (v997) GRAV.SPIN2.EMERGENCE.01: Barnes-Rivers ranks (5,3,1,1) ---- Python-only: Weyl^2 ghost residues, random-p numeric, SMG N=8 Fidkowski-Kitaev toy (spectrum / Spin(7) / Schmidt / edge). *)](../../../../verification/wolfram/tfpt_readouts.wl#L699)

## Research Contract — FTRANSFER.SK.RHO0.01 (Schwinger–Keldysh completion: cosmological transfers need [formula in source] )

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13824-13892](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13824) · `section:d8ed1f80544bebc4760c` · section

Typing. A research contract \ (ledger row FTRANSFER.SK.RHO0.01), registered 2026-08-28 from review wave 3; mechanism executed 2026-08-29. Demand. Cosmological transfers ( [formula in source] , [formula in source] , and any nonequilibrium 4D readout) need the pair [formula in source] , not [formula in source] alone — the Euclidean-cap / KMS initial state. Typed candidate. The [formula in source] saddle [formula in sou

Explicit source references:

- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1009_rho0_minimizer.py](../../../../verification/v1009_rho0_minimizer.py#L1) · explicit_file_citation
- [verification/v1000_spin2_sk_witnesses.py](../../../../verification/v1000_spin2_sk_witnesses.py#L1) · explicit_file_citation
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [FTRANSFER.PARENT.Z5CAP.01](../../../../verification/status_ledger.csv#L779) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation
- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — SEAM.MMST.TYPEIII.CHARGED.01 (one scaling-limit theorem)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:13893-13935](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L13893) · `section:2465208e294a3178e3e1` · section

Typing. A research contract \ (ledger row SEAM.MMST.TYPEIII.CHARGED.01), registered 2026-08-29 from review wave 5. Demand. One scaling-limit theorem [formula in source] strongly on the finite-energy core [formula in source] crossed-product continuity, from which [formula in source] , [formula in source] , type III [formula in source] , unique rotational KMS, unique conditional expectation, deck equidistribution and m

Explicit source references:

- [verification/v1006_mmst_lemma_battery.py](../../../../verification/v1006_mmst_lemma_battery.py#L1) · explicit_file_citation
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [verification/v998_seam_modular_closure.py](../../../../verification/v998_seam_modular_closure.py#L1) · explicit_script_identifier

## Research Contract — TFPT.TOE.COMPLETE.01 (the named AND of eight completeness gates)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:14103-14237](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L14103) · `section:b9be0eca5eee141eabc7` · section

Typing. A research contract \ (ledger row TFPT.TOE.COMPLETE.01), registered 2026-08-29 from review wave 4. This row names the AND of eight gates; it does not close any of them and it does not upgrade a marker. Dual rest: the compiler residual [formula in source] sits beside [formula in source] ; this contract is the named AND, not a closure of either.

Explicit source references:

- [verification/v1023_derivative_filtered_wall.py](../../../../verification/v1023_derivative_filtered_wall.py#L1) · explicit_file_citation
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [PRED.JOINTLIKELIHOOD.01](../../../../verification/status_ledger.csv#L749) · explicit_claim_identifier · original status at linked ledger row
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [TFPT.IRREDUCIBLE.01](../../../../verification/status_ledger.csv#L103) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NU.TEXTURE.MECHANISM.01](../../../../verification/status_ledger.csv#L768) · explicit_claim_identifier · original status at linked ledger row
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.WEINBERG.WITTEN.01](../../../../verification/status_ledger.csv#L770) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation
- [SEAM.DETLINE.UNIFICATION.01](../../../../verification/status_ledger.csv#L758) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1015_axiom_core_closure.py](../../../../verification/v1015_axiom_core_closure.py#L1) · explicit_file_citation
- [verification/v1013_thermodynamic_dynamics.py](../../../../verification/v1013_thermodynamic_dynamics.py#L1) · explicit_file_citation
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.TWISTOR.01](../../../../verification/status_ledger.csv#L584) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_file_citation
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1022_telb_round3_certificates.py](../../../../verification/v1022_telb_round3_certificates.py#L1) · explicit_file_citation
- [verification/v1025_telb_c1_c2a_certificates.py](../../../../verification/v1025_telb_c1_c2a_certificates.py#L1) · explicit_file_citation
- [DYN.MARKOV.EMBED.01](../../../../verification/status_ledger.csv#L741) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NUSCALE.01](../../../../verification/status_ledger.csv#L365) · explicit_claim_identifier · original status at linked ledger row
- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1020_spectator_sector_obstruction.py](../../../../verification/v1020_spectator_sector_obstruction.py#L1) · explicit_script_identifier
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [OBS.TRANSDUCTION.01](../../../../verification/status_ledger.csv#L748) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — FLAV.NUSCALE.06 (pentagon-class misalignment candidate)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:14238-14255](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L14238) · `section:12feef6a28eadbb9a373` · section

Typing. A candidate \ (ledger row FLAV.NUSCALE.06); mechanism [formula in source] the [formula in source] -to-flavor operator . No seesaw closure; FLAV.NUSCALE.05 unmoved. ( v1001_ nu_ pentagon_ chain.py.)

Explicit source references:

- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v1001_nu_pentagon_chain.py](../../../../verification/v1001_nu_pentagon_chain.py#L1) · explicit_file_citation
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.06](../../../../verification/status_ledger.csv#L765) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)

## Research Contract — FLAV.NU.TEXTURE.MECHANISM.01 (both structural nulls as binding constraints)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:14256-14301](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L14256) · `section:11b8cd7b32010b22189d` · section

Typing. A research contract \ (ledger row FLAV.NU.TEXTURE.MECHANISM.01), registered 2026-08-29 from review wave 5. ( v1003_ nu_ structural_ nulls.py.) Executed content. Charged-sector data [formula in source] , [formula in source] (coset min-norms all [formula in source] ) . Schur-texture NULL : all [formula in source] preregistered [formula in source] combinations fail; D4 reflection forces [formula in source] ; hie

Explicit source references:

- [FLAV.NU.TEXTURE.MECHANISM.01](../../../../verification/status_ledger.csv#L768) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NU.PARENT.INTERTWINER.01](../../../../verification/status_ledger.csv#L777) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1003_nu_structural_nulls.py](../../../../verification/v1003_nu_structural_nulls.py#L1) · explicit_file_citation
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation

## Research Contract — SEAM.MILNOR.LOCALRING.01 (canonical identification of the seam collar with the reduced Milnor algebra)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:14302-14380](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L14302) · `section:2cbe5d1807cd76c5e04d` · section

Typing. A research contract \ (ledger row SEAM.MILNOR.LOCALRING.01), registered 2026-08-30 from review wave 6. ( v1004_ milnor_ frobenius_ gray.py.) Demand. A canonical identification between the raw seam collar / [formula in source] transition bus and the reduced Milnor algebra [formula in source] preserving simultaneously the dual-number action, the Frobenius pairing, the Gray torsor, the deck action and CP. Accept

Explicit source references:

- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_script_identifier
- [verification/v1005_relative_pencil_bridges.py](../../../../verification/v1005_relative_pencil_bridges.py#L1) · explicit_script_identifier
- [verification/v1010_simplicity_bridge_census.py](../../../../verification/v1010_simplicity_bridge_census.py#L1) · explicit_file_citation
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v1004_milnor_frobenius_gray.py](../../../../verification/v1004_milnor_frobenius_gray.py#L1) · explicit_file_citation
- [SEAM.MILNOR.LOCALRING.01](../../../../verification/status_ledger.csv#L769) · explicit_claim_identifier · original status at linked ledger row
- [verification/v119_review_validation_2.py](../../../../verification/v119_review_validation_2.py#L1) · explicit_script_identifier
- [verification/v106_review_validation.py](../../../../verification/v106_review_validation.py#L1) · explicit_script_identifier
- [verification/v1015_axiom_core_closure.py](../../../../verification/v1015_axiom_core_closure.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## Research Contract — GRAV.WEINBERG.WITTEN.01 (Weinberg–Witten firewall before any spin-2 marker move)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:14381-14396](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L14381) · `section:b83de37eb381c3c07bbe` · section

Typing. A research contract \ (ledger row GRAV.WEINBERG.WITTEN.01), registered 2026-08-30 from review wave 6. Child of TOE gate T7; cross-link GRAV.SPIN2.EMERGENCE.01 (listed here, not back — that would cycle). Demand. The microscopic Hamiltonian family must not possess a fundamental Lorentz-covariant local conserved [formula in source] ; Lorentz symmetry, diffeomorphism Ward identities and the spin-2 mode must emerg

Explicit source references:

- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.WEINBERG.WITTEN.01](../../../../verification/status_ledger.csv#L770) · explicit_claim_identifier · original status at linked ledger row

## Externalization Contract — SEAM.EQUIV.01 (the seam scaling-limit theorem, packaged for external specialists)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:14397-14558](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L14397) · `section:03b9058ca08ba4829ac7` · section

Typing. This section is a hand-off document: it packages the one remaining seam obligation as a self-contained problem statement for an outside specialist in conformal nets / vertex operator algebras / algebraic QFT. It documents, it does not close: the ledger row SEAM.EQUIV.01 stays \ (its conditional route SEAM.EQUIV.MMST.01 is closed modulo cited theorems; the unconditional parent is the target below). Nothing in 

Explicit source references:

- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [verification/v286_seam_equivalence_contract.py](../../../../verification/v286_seam_equivalence_contract.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1) · explicit_file_citation
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_file_citation
- [TfptCarrier.SeamScalingLimit.mmst_scaling_limit](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L76) · explicit_lean_symbol
- [verification/v377_seam_s3_e8character.py](../../../../verification/v377_seam_s3_e8character.py#L1) · explicit_file_citation
- [TfptCarrier.SeamScalingLimit.collar_gapped](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L72) · explicit_lean_symbol
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamScalingLimit.holomorphic_discriminator](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L58) · explicit_lean_symbol
- [TfptCarrier.SeamScalingLimit.mmst_range](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L53) · explicit_lean_symbol
- [verification/v366_mmst_seam_collar.py](../../../../verification/v366_mmst_seam_collar.py#L1) · explicit_script_identifier
- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_file_citation
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamEquivChain.conway_sloane_e8](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L61) · explicit_lean_symbol
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [verification/v461_seam_strict_locality.py](../../../../verification/v461_seam_strict_locality.py#L1) · explicit_script_identifier
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [verification/v356_continuum_mmst_applicability.py](../../../../verification/v356_continuum_mmst_applicability.py#L1) · explicit_script_identifier
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamEquivChain.mueger_klm_holomorphy](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L58) · explicit_lean_symbol
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_file_citation
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_file_citation
- [TfptCarrier.SeamEquivChain.kitaev_invertibility](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L52) · explicit_lean_symbol
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation
- [verification/v217_marks_emergence_scan.py](../../../../verification/v217_marks_emergence_scan.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [verification/v351_continuum_realisation_sharpened.py](../../../../verification/v351_continuum_realisation_sharpened.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1) · explicit_file_citation
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [verification/v973_seam_route_narrowing.py](../../../../verification/v973_seam_route_narrowing.py#L1) · explicit_file_citation
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [verification/v469_seam_crossedproduct_route.py](../../../../verification/v469_seam_crossedproduct_route.py#L1) · explicit_script_identifier
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1) · explicit_file_citation
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [verification/v301_route_a_invertible.py](../../../../verification/v301_route_a_invertible.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamScalingLimit.ChiralCFT_c8](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L68) · explicit_lean_symbol
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamScalingLimit.adamo_holomorphic_e8](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L87) · explicit_lean_symbol
- [verification/v994_mmst_criteria_battery.py](../../../../verification/v994_mmst_criteria_battery.py#L1) · explicit_file_citation
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [(* ---- (v994) SEAM.EQUIV.MMST.01 C3: Theta_E8 / eta^8 = {1,248,4124,34752} ---- Python-only: C1 entropy, C2 QWZ spectrum, C4 two-point numeric, C5 sector recombination beyond det, C6 cited, C7 open, GSO/N=8 must-fail combinatorics. *)](../../../../verification/wolfram/tfpt_readouts.wl#L680)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* v463 (ii): the (E8)_1 tower = E4/eta^8 coefficients {1,248,4124,34752,213126} *) inv8 = Series[Product[(1 - q^n)^-8, {n, 1, 6}], {q, 0, 5}]; chiSer = Series[(1 + 240 Sum[DivisorSigma[3, n] q^n, {n, 1, 6}]) inv8, {q, 0, 5}]; tower = CoefficientList[Normal[chiSer], q][[1 ;; 5]]; checkExact["v463 SEAM.EQUIV.UNIQ.01 (ii): the holomorphic c=8 partition function is the unique j^{1/3}=E4/eta^8, whose q-coefficients are the (E8)_1 tower {1,248,4124,34752,213126} -- the q^1=248 is the forced weight-1 dimension (Dong-Mason/Schellekens: the holomorphic c=8 VOA is unique = V_{E8})", tower == {1, 248, 4124, 34752, 213126}]; ]; (* ==== v469 round: the net-level crossed-product certification -- the LR locality integers (h_s(SO(16)_1) = 16/16 = 1 in Z; the mu4 glue h(J^k) = {1,1,1} all integer), the KLM mu-index arithmetic (4/2^2 = 1 and 16/4^2 = 1, both holomorphic) and the Kitaev 16-fold-way pin (nu = 16 x |C| = 16 = 0 mod 16, c_- = nu/2 = 8 = g_car+N_fam); mirrors v469 (the FHS Chern itself is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2916)
- [(* ==== v461/v462 round: the Kapustin-Fidkowski strict-locality obstruction (integer logic; the Wilson-loop winding/Chern themselves are numerical, Python-only) and the 128-spinor extension at character level -- the Jacobi/E8 theta identity theta2^8+theta3^8+theta4^8=2E4 (so the (E8)_1 character is the SO(16)_1 vacuum+spinor sum) and the 120+128=248 sector + finite 16-Majorana Fock counts; mirrors v461/v462. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2874)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [(* v461: tied obstruction integers + the reflection forcing (strict-local => C=-C => C=0) *) cMinus = 2^(gcar - 1)*1/2; (* 16*|C|/2 = 8, |C|=1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2881)
- [(* v469 (i): the LR locality integers of both extension routes *) hs = 16/16; (* so(N)_1 spinor weight N/16, N = 16 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2930)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ==== v351 SEAM.EQUIV.CONTINUUM.02: the order-4 clock + Coxeter-match pin E8 over SO(16) ==== *) Module[{cE8, cD8}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; checkExact["v351 SEAM.EQUIV.CONTINUUM.02: the c=8 which-net ambiguity (E8 det 1 vs SO(16)=D8 det 4) is RESOLVED by the seam's ORDER-4 mu4 clock -- index-4 extension of D5(+)A3 = E8 (full mu4 condensation 16->4->1), index-2 = SO(16) (partial Z2 16->4); the order (4 not 2) selects E8. The bootstrap agrees: h(E8)=30 max prime 5=g_car, h(D8)=14 max prime 7, so SO(16) fails the Coxeter-match. The residual of SEAM.EQUIV.01 is then PURELY the chiral-edge existence, not which-net", Det[cE8] == 1 && Det[cD8] == 4 && Max[FactorInteger[30][[All,1]]] == 5 && Max[FactorInteger[14][[All,1]]] == 7]; ]; (* ==== v352 TFPT.IRREDUCIBLE.01: both axioms bootstrap-forced; irreducibles = framework + pi ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2334)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)

## Externalization Contract — PRIME.RESIDUE.EXTERNAL.01 (the prime-front terminal residue, packaged for external specialists)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:14783-15054](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L14783) · `section:a2199f712fb927b5b732` · section

Typing. The third hand-off document: the terminal open statements of the prime-front programme (diary and status record: tfpt_prime_front), packaged self-containedly for outside specialists in analytic number theory — large sieve, sampling and frame theory, de Branges spaces, explicit-formula methods. It documents, it does not close: the contract identifier names this document, not a ledger row; every prime-front led

Explicit source references:

- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation

## Certifiability and recommended order

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex:15055-15361](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/tfpt/tfpt_research_contracts.tex#L15055) · `section:568b5e9acdb7b04367d3` · section

@Ylc@ Building block & Machine & Hardness \\ [formula in source] enumeration ( [formula in source] ) & Lean / Python / Wolfram & easy ( done) \\ [formula in source] fixed-locus polynomial ( [formula in source] ) & Sage / Mathematica & medium \\ selector uniqueness ( [formula in source] ) & interval arithmetic & medium \\ SNF, determinants, spectra & Lean & easy–medium \\ principal-symbol ellipticity (G1) & xAct / Cad

Explicit source references:

- [verification/v578_native_jets.py](../../../../verification/v578_native_jets.py#L1) · explicit_file_citation
- [verification/v136_dual_normal_selector.py](../../../../verification/v136_dual_normal_selector.py#L1) · explicit_script_identifier
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [verification/v93_koide_relaxation_toy.py](../../../../verification/v93_koide_relaxation_toy.py#L1) · explicit_script_identifier
- [verification/v566_parabolic_anchor_selfcode.py](../../../../verification/v566_parabolic_anchor_selfcode.py#L1) · explicit_file_citation
- [FTRANSFER.CLOCKS.01](../../../../verification/status_ledger.csv#L676) · explicit_claim_identifier · original status at linked ledger row
- [DYN.MARKOV.EMBED.01](../../../../verification/status_ledger.csv#L741) · explicit_claim_identifier · original status at linked ledger row
- [verification/v724_phys_t3b_modular_flows.py](../../../../verification/v724_phys_t3b_modular_flows.py#L1) · explicit_file_citation
- [CONTRACT.F.01](../../../../verification/status_ledger.csv#L302) · explicit_claim_identifier · original status at linked ledger row
- [verification/v320_galois_cp_relation.py](../../../../verification/v320_galois_cp_relation.py#L1) · explicit_script_identifier
- [verification/v777_ftransfer_clock_jets.py](../../../../verification/v777_ftransfer_clock_jets.py#L1) · explicit_file_citation
- [verification/v971_markov_embedding_generator.py](../../../../verification/v971_markov_embedding_generator.py#L1) · explicit_file_citation
- [verification/v575_cr_continuous_uniflow.py](../../../../verification/v575_cr_continuous_uniflow.py#L1) · explicit_file_citation
- [verification/v533_ftransfer_disc7_norm.py](../../../../verification/v533_ftransfer_disc7_norm.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_script_identifier
- [verification/v213_ftransfer_functor.py](../../../../verification/v213_ftransfer_functor.py#L1) · explicit_file_citation
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v723_phys_modular_clock.py](../../../../verification/v723_phys_modular_clock.py#L1) · explicit_file_citation
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_file_citation
- [FTRANSFER.COCYCLE.01](../../../../verification/status_ledger.csv#L669) · explicit_claim_identifier · original status at linked ledger row
- [verification/v571_cr_discrete_corners.py](../../../../verification/v571_cr_discrete_corners.py#L1) · explicit_file_citation
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier
- [verification/v238_modular_lindblad_dynamics.py](../../../../verification/v238_modular_lindblad_dynamics.py#L1) · explicit_script_identifier
- [FR.DYNAMICS.01](../../../../verification/status_ledger.csv#L396) · explicit_claim_identifier · original status at linked ledger row
- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_script_identifier
- [verification/v224_diamond_ftransfer_path.py](../../../../verification/v224_diamond_ftransfer_path.py#L1) · explicit_script_identifier
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_file_citation
- [verification/v632_ftransfer_pgl2.py](../../../../verification/v632_ftransfer_pgl2.py#L1) · explicit_script_identifier
- [FTRANSFER.KMSCOSET.01](../../../../verification/status_ledger.csv#L688) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.STT.01](../../../../verification/status_ledger.csv#L668) · explicit_claim_identifier · original status at linked ledger row
- [DYN.TRANSFER.UNIVERSAL.01](../../../../verification/status_ledger.csv#L492) · explicit_claim_identifier · original status at linked ledger row
- [verification/v99_koide_flow_time.py](../../../../verification/v99_koide_flow_time.py#L1) · explicit_script_identifier
- [verification/v792_ftransfer_kms_coset.py](../../../../verification/v792_ftransfer_kms_coset.py#L1) · explicit_file_citation
- [verification/v425_dyn_transfer_universal.py](../../../../verification/v425_dyn_transfer_universal.py#L1) · explicit_file_citation
- [verification/v240_gns_os_reconstruction.py](../../../../verification/v240_gns_os_reconstruction.py#L1) · explicit_script_identifier
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_file_citation
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* ==== v533 round: FTR.DISC7.NORM.01 -- the disc -7 norm line. Exact mirrors: norm identity, translation, norms (2,4,14,32), constant discriminant -7, vertex, negative controls. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8372)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)
- [(* v230 center budget (7,11,13) = three local norms *) RRm = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; QQm = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Cc2 = RRm + QQm.DiagonalMatrix[{1, 0, 0}]; checkExact["v230 CENTER.NORM.01: C=R+Q diag(1,0,0) row sums (7,11,13) = " <> "(N_Z[omega](3+2w)=7 hex, C(4,0)+C(4,1)+C(4,2)=11 QBL Fock, N_Z[i](3+2i)=13 square) " <> "= (hex norm, boundary Fock count, square norm)", Total /@ Cc2 == {7, 11, 13} && {Nw[3, 2], Binomial[4, 0] + Binomial[4, 1] + Binomial[4, 2], Ni[3, 2]} == {7, 11, 13}]; (* v224 diamond F_transfer path: sheet axis curved, winding axis flat, Plucker steps *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1838)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)
- [(* ---- (v136) dual-normal selector ---- *) Module[{dv, nv, av, rmat, qmat, kmat, sols, a0, v0, sigma, adjA0, grp, gens, reals}, dv = {-1/2, -1/2, 1}; nv = {5, -9, 6}; av = {1, 1, 2}; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; kmat = rmat + qmat . DiagonalMatrix[{1, -1, -1}]; sols = Table[Select[Tuples[Range[0, 5], 3], dv . # == av[[j]] && nv . # == 8 Boole[j == 1] &], {j, 3}]; checkExact["v136 column normal form: d.c_j = a_j, n.c_j = 8 delta_1j; kernel (6,8,7); each column UNIQUE in {0..5}^3 (1 of 216)", (dv . #) & /@ Transpose[rmat] == av && (nv . #) & /@ Transpose[rmat] == {8, 0, 0} && 7 First[NullSpace[{dv, nv}]] == {6, 8, 7} && Length /@ sols == {1, 1, 1} && (First /@ sols) == Transpose[rmat]]; checkExact["v136 honesty: K not pinned by (d,n) (d.K = (1,1/2,1), n.K = (14,1,-6)); det K = 4 via the diamond", dv . kmat == {1, 1/2, 1} && nv . kmat == {14, 1, -6} && Det[kmat] == 4]; a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; v0 = First[NullSpace[a0]]; v0 = v0/v0[[2]] 3; sigma = {2, -9, 5}; adjA0 = Transpose[Table[(-1)^(i + j) Det[Drop[a0, {i}, {j}]], {i, 3}, {j, 3}]]; checkExact["v136 spectral normal: A0* zero mode signed squares = -(2,-9,5); ||v||^2 = 16/9; adj(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1050)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean#L1)
- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)

## Research consolidation: source fields, dynamics and the remaining bridge (2026-09-09)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_research_20260909.tex:2-15](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_research_20260909.tex#L2) · `section:18b3031aad48b3897a19` · section

tocsectionResearch consolidation: source fields and dynamics (2026-09-09) Status and provenance. The research archive after Round 27 is now integrated, including the Round 28–50 development chain and the subsequent named branches. These are written, model-specific arguments accompanied by executable controls, not newly formalized or independently reviewed theorems. All physical T1–T8 gates and TFPT.TOE.COMPLETE.01 re

Explicit source references:

- [experiments/theory-contracts/RESEARCH_2026-09-09.md](../../../../experiments/theory-contracts/RESEARCH_2026-09-09.md#L1) · explicit_file_citation
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row

## 4. What the compiler, Clock and lattice audits actually decide

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_research_20260909.tex:159-192](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_research_20260909.tex#L159) · `section:8e5cd1b65e53fa375312` · subsection

The charge-sign quotient [formula in source] loses commutator information. The minimal additive refinement is the eight-bit symplectic space [formula in source] , with four-dimensional kernel [formula in source] . There are 64 quadratic-form-preserving sections, four compatible with the family marking; the deck exchanges complementary sections. The full target on [formula in source] has charge shifts, cocycle and [fo

## Non-RH research through Round 27: a full-reference control theorem

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_round27_full_reference.tex:2-17](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_round27_full_reference.tex#L2) · `section:294c00be71c5846e45ed` · subsection

The previously local research contracts through Round 27 are now shipped with their proof sources, source-pinned checkers, negative controls and saved validation records under experiments/theory-contracts/. They extend the positive matter/constraint constructions to an interacting scalar/charge model, local charge transport, exact scalar elimination and controlled signed history sums. Additional off-shell fields, sel

Explicit source references:

- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row

## Full-reference theorem and proof.

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_round27_full_reference.tex:66-113](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tex-artefacts/toe_round27_full_reference.tex#L66) · `section:f6a4452580c2f7e16d7b` · paragraph

Let [formula in source] be the sum of moduli before cancellation, resolved into elementary hopping words, initial charge profiles and scalar integrals. Then Every elementary hop changes the complete profile, hence [formula in source] . Scalar spectral Jensen gives [formula in source] . Pinching [formula in source] into its charge blocks [formula in source] contracts the Schatten [formula in source] norm, so [formula 

## [formula in source] as the Pascal closure

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:1732-1780](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L1732) · `section:9656cb78a4cbdf493637` · subsection

A family is exactly the complete Pascal truncation to degree two: the unique positive-integer solution of [formula in source] . Proof of uniqueness. Direct evaluation gives [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula in source] ; so [formula in source] is the only root in [formula in source] . For [formula in source] the forward difference is 

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_file_citation
- [verification/v45_family_exterior.py](../../../../verification/v45_family_exterior.py#L1) · explicit_file_citation
- [verification/v46_grand_mass_volume.py](../../../../verification/v46_grand_mass_volume.py#L1) · explicit_file_citation
- [verification/v14_carrier_uniqueness.py](../../../../verification/v14_carrier_uniqueness.py#L1) · explicit_file_citation
- [verification/v44_carrier_exterior.py](../../../../verification/v44_carrier_exterior.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *) checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+", Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16]; checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car", Sort[Abs[plLeft[K]]] == {1, 4, 6} && Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar]; checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car", 4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15]; (* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L168)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v44) exterior leg = carrier exterior-algebra grading ---- *) checkExact["16 = Lambda^even(5) = C(5,0)+C(5,2)+C(5,4) = 1+10+5", {Binomial[5, 0], Binomial[5, 2], Binomial[5, 4]} == {1, 10, 5}]; (* u^c in 10=Lambda^2(5) deg 2 ; d^c in 5bar=Lambda^4(5) deg 4 *)](../../../../verification/wolfram/tfpt_readouts.wl#L161)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean#L1)

## The [formula in source] compiler: [formula in source] as a closure, not an input

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:1809-1910](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L1809) · `section:cb1bdab881371b610e8f` · section

This section upgrades the [formula in source] atlas (Section lattice construction. The whole content is consolidated and verified in the standalone companion note ``The Even Carrier Code and the [formula in source] Coxeter Compiler.'' The thesis: the carrier code is the [formula in source] half-spinor, the family geometry is an [formula in source] , and [formula in source] is the standard unimodular glue closure of [

Explicit source references:

- [verification/v726_phys_car_pp_index.py](../../../../verification/v726_phys_car_pp_index.py#L1) · explicit_file_citation
- [verification/v802_gnet_martingale.py](../../../../verification/v802_gnet_martingale.py#L1) · explicit_file_citation
- [GATE.METRIC.08](../../../../verification/status_ledger.csv#L210) · explicit_claim_identifier · original status at linked ledger row
- [verification/v469_seam_crossedproduct_route.py](../../../../verification/v469_seam_crossedproduct_route.py#L1) · explicit_file_citation
- [verification/v92_glue_uniqueness.py](../../../../verification/v92_glue_uniqueness.py#L1) · explicit_script_identifier
- [verification/v277_seam_calderon_e8_match.py](../../../../verification/v277_seam_calderon_e8_match.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v722_phys_ramified_ns_r.py](../../../../verification/v722_phys_ramified_ns_r.py#L1) · explicit_file_citation
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v234_seam_holomorphy_selection.py](../../../../verification/v234_seam_holomorphy_selection.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [verification/v779_gnet_gns_arf.py](../../../../verification/v779_gnet_gns_arf.py#L1) · explicit_file_citation
- [verification/v489_seam_modular_commutator.py](../../../../verification/v489_seam_modular_commutator.py#L1) · explicit_file_citation
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [GNET.RAMIFIED.01](../../../../verification/status_ledger.csv#L667) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v260_k3_kummer_unification.py](../../../../verification/v260_k3_kummer_unification.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.TWISTOR.01](../../../../verification/status_ledger.csv#L584) · explicit_claim_identifier · original status at linked ledger row
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_script_identifier
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* v463 (ii): the (E8)_1 tower = E4/eta^8 coefficients {1,248,4124,34752,213126} *) inv8 = Series[Product[(1 - q^n)^-8, {n, 1, 6}], {q, 0, 5}]; chiSer = Series[(1 + 240 Sum[DivisorSigma[3, n] q^n, {n, 1, 6}]) inv8, {q, 0, 5}]; tower = CoefficientList[Normal[chiSer], q][[1 ;; 5]]; checkExact["v463 SEAM.EQUIV.UNIQ.01 (ii): the holomorphic c=8 partition function is the unique j^{1/3}=E4/eta^8, whose q-coefficients are the (E8)_1 tower {1,248,4124,34752,213126} -- the q^1=248 is the forced weight-1 dimension (Dong-Mason/Schellekens: the holomorphic c=8 VOA is unique = V_{E8})", tower == {1, 248, 4124, 34752, 213126}]; ]; (* ==== v469 round: the net-level crossed-product certification -- the LR locality integers (h_s(SO(16)_1) = 16/16 = 1 in Z; the mu4 glue h(J^k) = {1,1,1} all integer), the KLM mu-index arithmetic (4/2^2 = 1 and 16/4^2 = 1, both holomorphic) and the Kitaev 16-fold-way pin (nu = 16 x |C| = 16 = 0 mod 16, c_- = nu/2 = 8 = g_car+N_fam); mirrors v469 (the FHS Chern itself is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2916)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* v469 (i): the LR locality integers of both extension routes *) hs = 16/16; (* so(N)_1 spinor weight N/16, N = 16 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2930)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [(* ==== v233: CP = the universal family/triality phase, sheet-split (mu6 = mu3 x mu2) ==== *) Module[{rho, omega}, rho = Exp[I Pi/3]; omega = Exp[2 I Pi/3]; checkExact["v233 CP.TRIALITY.01: the CP phase is the universal family/triality phase, sheet-split. " <> "mu6 = mu3(triality) x mu2(sheet): omega=e^{2pi i/3} the Z3 triality centre (2/3 cusp weight), " <> "rho = omega^2*(-1). Since rho^4 = rho^1*rho^3 with rho^3 in mu2, the quark (rho^1) and lepton " <> "(rho^4) CP phases share the SAME family class and differ only by the sheet: rho^1*(-1)=omega^2 " <> "(quark family part), rho^4=omega^2 (lepton). So CP = the universal triality phase + the sheet, " <> "not a free power choice; omega is the mu3 factor of the order-30 (2,3,5) monodromy (v232).", Simplify[omega^3] == 1 && Simplify[rho^3 + 1] == 0 && Simplify[rho - omega^2 (-1)] == 0 && Simplify[rho^4 - rho^1 rho^3] == 0 && Simplify[rho^1 (-1) - omega^2] == 0 && Simplify[rho^4 - omega^2] == 0]; ]; (* ==== v234: Seam-Holomorphy selection -- one condition, three faces, E8 ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1915)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ==== v235: the closing step in abelian Chern-Simons -- holomorphic <=> det K = 1 ==== *) Module[{cartanA, cartanD, e8edges, A3, D5, D8, E8, carrier}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; checkExact["v235 GATE.HOLO.02: the closing step in abelian Chern-Simons -- a free gapped bosonic 2+1d " <> "bulk = an even integer K-matrix with #anyons=|det K|, edge c=signature(K), holomorphic <=> det=1. " <> "The TFPT tower (v92) read by det: carrier D5(+)A3 (even, det 16, 16 anyons) -> SO(16)_1=D8 (det 4) " <> "-> (E8)_1 (det 1, holomorphic), all rank 8, c=signature=8=g_car+N_fam. Holomorphic <=> det 1 <=> E8 " <> "= the Kitaev E8 quantum-Hall state. Condensation: a Lagrangian glue of order sqrt(16)=|mu4|=4 takes " <> "det 16->1; an order-2 isotropic only ->4=D8. NEG: D8 free+bosonic but 4 anyons (not holomorphic). " <> "Residual: condense the |mu4| Lagrangian glue = the sheet/QGEO selection.", Det[E8] == 1 && Det[D8] == 4 && Det[carrier] == 16 && Det[A3] == 4 && Det[D5] == 4 && And @@ (EvenQ[#] & /@ Join[Diagonal[E8], Diagonal[D8], Diagonal[carrier]]) && Min[Eigenvalues[N[E8]]] > 0 && Min[Eigenvalues[N[D8]]] > 0 && Min[Eigenvalues[N[carrier]]] > 0 && Length[E8] == Length[D8] == Length[carrier] == 8 && 16/4^2 == 1 && 16/2^2 == 4 && (5 + 3 == 8)]; ]; (* ==== v236: the (2,3,5) Brieskorn singularity generates the skeleton ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1950)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [experiments/lean4-carrier-rigidity/TfptCarrier.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier.lean#L1)
- [(* ==== v277: seam-Calderon -> (E8)_1 matching certificate (QGAMB.TIERB.01) ==== v276 (flat-pillowcase commutator, numerical) is Python-only; v277's exact lattice discriminator (det E8 vs det D8) + the (E8)_1 character 248 are mirrored. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2119)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v91) spine tetrahedron ---- *) spine = {2, 3, 4, 5}; checkExact["v91 edges/faces/volume of {2,3,4,5}", (Sort[Times @@@ Subsets[spine, {2}]] == {6, 8, 10, 12, 15, 20}) && (Sort[Times @@@ Subsets[spine, {3}]] == {24, 30, 40, 60}) && (Times @@ spine == 120) && (120 == Total[{1, 7, 11, 13, 17, 19, 23, 29}])]; checkExact["v91 graph reading 240 = |mu4| |E(K4)| |E(K5)|; breaks at K6", (4 Binomial[4, 2] Binomial[5, 2] == 240) && (Binomial[6, 2] == 15) && (1 + 1 + 2^4 != 15)]; chiT[t_] := (t - 2) (t - 3) (t - 4) (t - 5); checkExact["v91 chi_T audit: coeffs (14,71,154,120); chi(0)=chi(7)=120, chi(1)=chi(6)=24", (Expand[chiT[t]] == t^4 - 14 t^3 + 71 t^2 - 154 t + 120) && (chiT[0] == 120) && (chiT[7] == 120) && (chiT[1] == 24) && (chiT[6] == 24)]; (* ---- (v92) glue uniqueness ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L136)

## The full power tower: [formula in source] on the carrier graph [formula in source]

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4070-4089](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4070) · `section:217cad99a393e32ff110` · subsection

The decuple bridge is one rung of a tower. Writing [formula in source] for the stripped electroweak unit, all three cosmological scales are powers of the same [formula in source] with binomial exponents (verified exactly): with residues [formula in source] and [formula in source] . . The exponents are the complete-graph counts of the five-slot carrier [formula in source] : [formula in source] So the cosmological cons

## Level 2.5 — the even-flip transition atlas (a falsifiable program)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4344-4404](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4344) · `section:5e1509353325b787484d` · subsection

Identify [formula in source] with the even-weight binary code on five bits. A transition [formula in source] has flip [formula in source] , even and nonempty, so [formula in source] ; per state there are [formula in source] flips, giving and the [formula in source] undirected flips match the [formula in source] [formula in source] root pairs ( , counting). This makes the atlas conjecture testable: a genuine root map 

Explicit source references:

- [verification/v418_cyclotomic_norm_triple.py](../../../../verification/v418_cyclotomic_norm_triple.py#L1) · explicit_script_identifier
- [verification/v532_e8_degree_modular_checksum.py](../../../../verification/v532_e8_degree_modular_checksum.py#L1) · explicit_file_citation
- [verification/v531_coxeter_tensor_stage_a.py](../../../../verification/v531_coxeter_tensor_stage_a.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v418 (1): the carrier-5 clock C5 + the golden ratio *) checkExact["v418 ARITH.NORMTRIPLE.01 (i): the carrier-5 clock C5 (Phi5-companion, 4x4) has C5^5=I, tr=-1, det=1 (the four primitive 5th roots); the golden ratio is its real-part data 2cos(72)=1/phi, 2cos(144)=-phi (output-side, v313/v349; dim 4, not 3 -- refines v417's gap)", MatrixPower[C5, 5] == I4 && Tr[C5] == -1 && Det[C5] == 1 && Simplify[2 Cos[2 Pi/5] - 1/phi] == 0 && Simplify[2 Cos[4 Pi/5] + phi] == 0]; (* v418 (2): the carrier norm = the quark numerator *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2539)
- [(* ==== v531 round: COX.STAGEA.TENSOR.01 -- the Stage A tensor clock. Exact mirrors: order 30, chi = Phi30, Ramanujan trace tomography, honest Phi15 scope, coprimality controls. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8300)
- [(* v418 (3): the triple + negative controls *) checkExact["v418 ARITH.NORMTRIPLE.01 (iii): det(3I+2 Comp(Phi_{3,4,5}))=(7,13,55) over Z[omega],Z[i],Z[zeta5] (atoms 3,2,5); NEG control anchor (5,4)->(21,41,461) (461 prime, only the carrier ring distinguishes); (3,2) FORCED not unique, (2,1)->(3,5,11)", {Det[3 I2 + 2 C3], Det[3 I2 + 2 C4], Det[3 I4 + 2 C5]} == {7, 13, 55} && {Det[5 I2 + 4 C3], Det[5 I2 + 4 C4], Det[5 I4 + 4 C5]} == {21, 41, 461} && PrimeQ[461] && {Det[2 I2 + C3], Det[2 I2 + C4], Det[2 I4 + C5]} == {3, 5, 11}]; ]; (* ==== v419 round: the seam mu4 = Gal(Q(zeta5)) = (Z/5)^x ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2548)
- [(* v417 (3): one order-30 Coxeter clock; seam mu4 is the Galois side *) checkExact["v417 DIAMOND.EISEN.01 (iii): all flavor clocks are powers of zeta30 (h(E8)=30): z30^15=-1 (mu2), z30^10=omega (mu3), z30^6=zeta5 (mu5), z30^5=zeta6 (mu6); the seam mu4 (i) is NOT a power (4 nmid 30), it is the Galois side (Z/30)^x of order phi(30)=8=rank E8", Simplify[z30^15 + 1] == 0 && Simplify[z30^10 - omega] == 0 && Simplify[z30^6 - Exp[2 Pi I/5]] == 0 && Simplify[z30^5 - zeta6] == 0 && Mod[30, 4] != 0 && EulerPhi[30] == 8 && Length[Select[Range[29], GCD[#, 30] == 1 &]] == 8]; ]; (* ==== v418 round: the cyclotomic norm triple (7,13,55) over the atom-rings ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2524)
- [(* ==== v532 round: E8.DEGREE.MODULAR.01 -- the dual-degree checksum 744. Exact mirrors: dual products, j-series constant 744, D16 control, non-heterotic controls, prime-totative fingerprint. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8334)

## [formula in source] monodromy, flavor and CP readouts

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:4495-4512](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L4495) · `section:98302c2c61efc4bc092a` · section

Machine checks for this section: v88_ cp_ phase_ audit.py

Explicit source references:

- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_file_citation

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

## Master statement and status

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5446-5495](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5446) · `section:8ab1f0d3c74dd8b84247` · section

tocsectionMaster statement Five carrier slots give [formula in source] ,\ four family corners give [formula in source] ,\ and [formula in source] gives the [formula in source] atlas. Equivalently: [formula in source] , [formula in source] , [formula in source] ; [formula in source] , [formula in source] , the [formula in source] Coxeter structure and the action ladder read the same five-slot pair-decuple. The Standar

## Appendix: machine-checkable [formula in source] construction

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex:5496-5542](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_1_architecture_e8.tex#L5496) · `section:9dbcdb3b5820985270ed` · section

The lift is reproducible by a short script (all entries below verified exactly).

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

## Closing the audit gates: is [formula in source] , [formula in source] , [formula in source] derived or imported?

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:1627-1750](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L1627) · `section:8e700f46596426722c86` · subsection

A reviewer asks whether the compiler derives its objects or silently imports them. We answer the three flavor/EM gates explicitly ( v13_open_gates.py); each is either closed or reduced to a named geometric statement, with the honest residual flagged.

Explicit source references:

- [verification/v159_pyrate_gauge_crosscheck.py](../../../../verification/v159_pyrate_gauge_crosscheck.py#L1) · explicit_file_citation
- [verification/v74_compiler_micro_lemmas.py](../../../../verification/v74_compiler_micro_lemmas.py#L1) · explicit_file_citation
- [verification/v13_open_gates.py](../../../../verification/v13_open_gates.py#L1) · explicit_file_citation
- [verification/v21_solar_product_quark.py](../../../../verification/v21_solar_product_quark.py#L1) · explicit_file_citation
- [verification/v11_unique_KQ.py](../../../../verification/v11_unique_KQ.py#L1) · explicit_file_citation
- [verification/v164_qcd_scale.py](../../../../verification/v164_qcd_scale.py#L1) · explicit_file_citation
- [verification/v467_thirdgen_mixing_pattern.py](../../../../verification/v467_thirdgen_mixing_pattern.py#L1) · explicit_script_identifier
- [verification/v79_review_identities.py](../../../../verification/v79_review_identities.py#L1) · explicit_file_citation
- [verification/v163_rg_stability_flavor.py](../../../../verification/v163_rg_stability_flavor.py#L1) · explicit_file_citation
- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
- [experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean#L1)
- [(* ---- (v79) hypercharge Lucas-Binet D_n + the quark-ratio reading ---- *) checkExact["Lucas-Binet D_n=(3^n-(-2)^n)/5 = {1,1,7,13,55,133}; c_u/c_d = D_5/(N_fam^2 D_4) = 55/117", Module[{D}, D = Table[(3^n - (-2)^n)/5, {n, 1, 6}]; D == {1, 1, 7, 13, 55, 133} && D[[5]]/(Nfam^2 D[[4]]) == 55/117]]; (* ---- (v79) Inverse Anchor Theorem: 1^T M^-1 1 = 1/atom; a^T M^-1 a = 1 for R,K,L ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L385)
- [(* ---- (v159) PyR@TE gauge cross-check: carrier content -> SM 1-loop b_i ---- *) Module[{fields, pre, u1, su2, su3, b1, b2, b3, fermIdx, scalIdx}, (* {Y, dimSU2, dimSU3, nGen, kind}: kind 1 = Weyl fermion, 2 = complex scalar *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1432)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ---- (v73) k=c3/2 forced: variational factor x Gauss-Bonnet topology; Fursaev-Solodukhin S=A/4 ---- *) checkExact["k=c3/2=1/(16pi)=(1/2)*(1/(|Z2|*2pi*chi(S2))), chi(S2)=2; Fursaev-Solodukhin 4pi k = 1/4", Module[{c3 = 1/(8 Pi), chi = 2, Z2 = 2}, (c3/2 == 1/(16 Pi)) && (c3 == 1/(Z2*2 Pi*chi)) && (4 Pi*(c3/2) == 1/4)]]; (* ---- (v74) compiler micro-lemmas: pencil differences 2->16->48; anchor QF 41-25=16 ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L352)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean#L1)
- [(* ---- (v10) K/Q/Sigma determinant ladder ---- *) R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}}; L = R + 6 W; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Sig = DiagonalMatrix[{1, -1, -1}]; checkExact["K = R + Q.Sigma", K == R + Q.Sig]; checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)]; checkExact["det ladder (Q,K,R,L) = (3,4,8,20)", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}]; checkExact["det product = 1920 = |W(D5)|", Det[Q] Det[K] Det[R] Det[L] == 1920]; aVec = {1, 1, 2}; checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41]; (* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L61)

## Downstream flavor readout: the rare kaons [formula in source]

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:1791-1822](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L1791) · `section:de65561a933aa5ea02ba` · subsection

The closed CKM point is not an end state — it feeds the theoretically cleanest flavor-changing neutral-current probe, the rare decays [formula in source] and [formula in source] . These are not a new compiler power: the only TFPT-specific content is the CKM point above; the short-distance loop functions ( [formula in source] , [formula in source] , [formula in source] , [formula in source] , Brod–Gorbahn–Stamou) are 

Explicit source references:

- [verification/v202_rare_kaon.py](../../../../verification/v202_rare_kaon.py#L1) · explicit_file_citation
- [verification/v88_cp_phase_audit.py](../../../../verification/v88_cp_phase_audit.py#L1) · explicit_script_identifier

## How the legacy layers simplify (bridge map)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2091-2117](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2091) · `section:2ffaaee2ce19180008ab` · section

@p0.7cmp3.5cmY@ layer & before & in the compiler picture \\ 1 & boundary [formula in source] & axiom (P1), unchanged; hardenable via Calder\'on/Lean \\ 2 & carrier, [formula in source] , [formula in source] , [formula in source] , [formula in source] & all one Pascal row [formula in source] on [formula in source] ; [formula in source] is the [formula in source] half-spinor \\ 3 & EM fixed point [formula in source] fl

Explicit source references:

- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)

## Closure status of the five former open questions

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2169-2175](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2169) · `section:1a2458f59412a5e4396c` · section

For each question the entry is typed honestly as closed, reduced or conditional: the proof chain isolating one sharply named remainder — and, where possible, a reduction that makes the problem smaller than previously thought. This is a resolution map, not a claim that all five are fully solved.

## (5) Axioms P1/P2 — P2 machine-verified, P1 as an interface /

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2385-2448](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2385) · `section:c80612b5b357f44d318a` · subsection

Here the hardening is empirical and concrete. The Lean 4 proof ( lean4-carrier-rigidity, toolchain v4.29.1 [formula in source] Mathlib) builds cleanly: @lY@ Verified (Lean, 0 sorry) & Content \\ Polarization.sixY_carrier_polynomial & [formula in source] as a corollary of orthogonal idempotents \\ Rigidity.unique_carrier_pair & [formula in source] unique (integer rigidity) \\ Hypercharge.trace_Y, _carrier_polynomial &

Explicit source references:

- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)

## The parabolic-weight computation (resolved this round)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:2669-2726](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L2669) · `section:10dfd6e9f65946a0b7ff` · section

Status (no drift). The splitting type is now closed: the unique partition [formula in source] fixes the anchor and [formula in source] fixes the residue branch (verified, below and v4_flavor_matrix.py), and the solar texture is built ( v9_neutrino_texture.py). The roadmap below is kept as the derivation record of how [formula in source] is obtained; it is no longer an open project. The only residual is the parabolic 

Explicit source references:

- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)

## Status

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:3249-3293](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L3249) · `section:35abcdeb3c5b2946d464` · section

tocsectionStatus @p0.56 p0.08 Y@ Statement & Status & Note \\ weights [formula in source] from cusps [formula in source] data & & Mehta–Seshadri \\ [formula in source] & & exact \\ balanced bundle [formula in source] & & stable splitting \\ [formula in source] , [formula in source] degree, [formula in source] & & winding/residue split \\ [formula in source] , [formula in source] & & budget bookkeeping \\ rigid [formu

## Closing computations and proofs

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:3294-3305](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L3294) · `section:0fbf9d0da4afc6e6a3e8` · part

Scope and honesty. This note discharges the items that were flagged ``standard but not written out,'' and now also carries the closures previously collected in the research-sprints note: the seam-fixed Starobinsky mass, the derived solar angle [formula in source] , the H2 splitting type, and the quark [formula in source] amplitude band. It does not force the items that stay typed transfer targets, never compiler powe

Explicit source references:

- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier
- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier

## H2: the moduli computation, set up explicitly

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:3913-4019](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L3913) · `section:c7d8a7dfe6518305774c` · section

H2 (Theorem 4 of the parabolic note) is reduced to: the [formula in source] -equivariant stable parabolic structure on [formula in source] realises the spectral-selector branch. We set up the finite computation and verify the selector.

Explicit source references:

- [verification/v49_readout_rigidity.py](../../../../verification/v49_readout_rigidity.py#L1) · explicit_script_identifier
- [verification/v27_wall_representative.py](../../../../verification/v27_wall_representative.py#L1) · explicit_file_citation
- [verification/v26_flavor_frontier_unification.py](../../../../verification/v26_flavor_frontier_unification.py#L1) · explicit_file_citation
- [verification/v69_d4_q_geometry.py](../../../../verification/v69_d4_q_geometry.py#L1) · explicit_file_citation
- [verification/v70_q_integer_lift.py](../../../../verification/v70_q_integer_lift.py#L1) · explicit_file_citation
- [verification/v53_compiler_core.py](../../../../verification/v53_compiler_core.py#L1) · explicit_script_identifier
- [P2.TYPING.01](../../../../verification/status_ledger.csv#L554) · explicit_claim_identifier · original status at linked ledger row
- [verification/v19_monodromy_moduli.py](../../../../verification/v19_monodromy_moduli.py#L1) · explicit_file_citation
- [verification/v491_p2_partition_corollary.py](../../../../verification/v491_p2_partition_corollary.py#L1) · explicit_file_citation
- [verification/v71_simple_r_bridge.py](../../../../verification/v71_simple_r_bridge.py#L1) · explicit_script_identifier
- [verification/v499_p2_weights_deligne_bg.py](../../../../verification/v499_p2_weights_deligne_bg.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [(* ==== v499 round: P2.TYPING.01 -- the P2 weight-typing postulate hardened: the anchor a = (1,1,2) as the Birkhoff-Grothendieck splitting exponents of the Deligne canonical extension E of the flavor connection (types the v491 check-9 residual). Exact content mirrored: (i) partition enumeration under the full typing (BG dictionary h^0 = 0 <=> a_i >= 1, exhaustive window) + the naive- typing negative control (h^1(E') = 3 forces deg -6, three splittings, e2 never 5) + the h^1 discrepancy (h^1(anchor bundle) = 1 != 3); (ii) the Deligne residue-trace degree (cusp exponents {0,1/3,2/3} = the unique lift of spec(lam^3 - 1) to [0,1), trace 1 per mark, deg E = -4, par-deg 0, witness A0* charpoly); (iii) the Schur-Horn permutohedron integer points {(2,2,0),(2,1,1)} with h^0 = 0 killing {2,2,0}; (iv) the Biswas Z3-cover degree arithmetic (genus 2, eigensheaves O(-2)^2, chi cross-check, regular-rep weights, the decomposable model {0,2,2} with h^0 = 1 = the unstable companion; deck double genus 1, j = 1728); (v) the n-mark formula e2 = (n-2)(n+1)/2 = 5 only at n = 4. The sympy symbolic parts (H^1 residue basis, monodromy group closure |<U,M0>| = 24, the 324-case stability skeleton) stay Python-side (v499). Mirrors v499. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3620)
- [(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *) checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}", Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]]; checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}", Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} && Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]]; (* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L329)
- [(* ==== v491 round: P2.PARTITION.01 -- g_car = 5 as the partition corollary of the four marks (the sharpening of v53). Exact content: 4 into exactly 3 positive integer parts is uniquely {1,1,2} => e = (4,5,2) => g_car = e2 = 5, |Z2| = e3 = 2, N_fam = e2 - e3 = 3 as corollaries; every assumption load-bearing (positivity / sum / part count / integrality negative controls); v53 needs all three targets, the partition only e1 = 4; sum rule 4(N-1)/2 = 4 iff N = 3; mirrors v491. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3116)
- [(* ---- (v97) sheet-conjugation bridge (P1 -> one [P]) ---- *) TA = {{0, 1, 0}, {1, 0, 0}, {2, -2, 1}}; SigM = DiagonalMatrix[{1, -1, -1}]; sig12 = {{0, 1, 0}, {1, 0, 0}, {0, 0, 1}}; e1v = {0, 0, 1}; e2v = {0, 1, 2}; e3v = {1, 0, 0}; QPm = (Q + SigM.Q.SigM)/2; checkExact["v97 Q_+ eigenvectors e1=(0,0,1) [l=1], e2=(0,1,2) [l=2], e3=(1,0,0) [l=3]", (QPm.e1v == 1 e1v) && (QPm.e2v == 2 e2v) && (QPm.e3v == 3 e3v)]; checkExact["v97 T_A integer involution, det -1, fixes 1 and a; T_A swaps e2 <-> e3, fixes e1", (TA.TA == IdentityMatrix[3]) && (Det[TA] == -1) && (TA.one == one) && (TA.av == av) && (TA.e2v == e3v) && (TA.e3v == e2v) && (TA.e1v == e1v)]; checkExact["v97 anchor = conjugation-symmetric vector: a = e2+e3, 1 = a-e1; odd line e2-e3", (av == e2v + e3v) && (one == av - e1v) && (TA.(e2v - e3v) == -(e2v - e3v))]; ddir = {-1, 1, 0}; coeffs = LinearSolve[Transpose[{one, av, ddir}], TA.ddir]; checkExact["v97 one deck action: T_A = -1 on R^3/span{1,a} (like sigma_12); parity det T_A = det sigma_12 = -1, det Sigma = +1", (coeffs[[3]] == -1) && (sig12.ddir == -ddir) && (Det[sig12] == -1) && (Det[SigM] == 1)]; Gm = TA.SigM; RrotM = {{0, 0, -1}, {1, 0, -1}, {0, 1, -1}}; checkExact["v97 D4 closure: G = T_A.Sigma has order 4, char (t+1)(t^2+1) = char(v70 R_rot)", (MatrixPower[Gm, 4] == IdentityMatrix[3]) && (MatrixPower[Gm, 2] != IdentityMatrix[3]) && (Expand[CharacteristicPolynomial[Gm, t] + (t + 1) (t^2 + 1)] === 0) && (Expand[CharacteristicPolynomial[Gm, t] - CharacteristicPolynomial[RrotM, t]] === 0)]; Svars = Array[sv, {3, 3}]; solS = Quiet[Solve[Flatten[Svars.Gm - RrotM.Svars] == 0, Flatten[Svars]], Solve::svars]; Sgen = Svars /. First[solS]; detSgen = Factor[Det[Sgen]]; checkExact["v97 sheet-index lemma: det S always EVEN on the integer intertwiner space, minimum |det| = 2 = |Z2|", Module[{vars = Variables[detSgen], vals}, vals = Select[Abs[detSgen /. Thread[vars -> #]] & /@ Tuples[Range[-2, 2], Length[vars]], # =!= 0 &]; (And @@ (EvenQ /@ vals)) && (Min[vals] == 2)]]; checkExact["v97 Q (det = N_fam) does NOT intertwine G -> R_rot (independent bridge)", Q.Gm != RrotM.Q]; (* ---- (v98) discriminant dictionary derived ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L249)
- [(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *) Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2; checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}", Sort[Eigenvalues[Qp]] == {1, 2, 3}]; checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)", Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}]; (* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L194)
- [(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *) checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam", {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam]; checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)", (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4]; (* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L342)

## Status: what is now written out, and what is honestly left

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:4020-4071](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L4020) · `section:354f7e98a6c16208d1a4` · section

tocsectionStatus @p5.6cmcY@ Item & Status & Result \\ Dynamics / clustering (Lemma Gravity Fredholm (Lemma [formula in source] truncation (Lemma Starobinsky [formula in source] / [formula in source] & / & [formula in source] GeV exact ; [formula in source] a \ band over [formula in source] \\ [formula in source] typing (Prop. [formula in source] (Prop. quark [formula in source] -rationals & / & hierarchy + source rat

Explicit source references:

- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v304_idg_nonlocal_ghost.py](../../../../verification/v304_idg_nonlocal_ghost.py#L1) · explicit_script_identifier
- [verification/v723_phys_modular_clock.py](../../../../verification/v723_phys_modular_clock.py#L1) · explicit_file_citation
- [verification/v19_monodromy_moduli.py](../../../../verification/v19_monodromy_moduli.py#L1) · explicit_file_citation
- [verification/v724_phys_t3b_modular_flows.py](../../../../verification/v724_phys_t3b_modular_flows.py#L1) · explicit_file_citation
- [verification/v371_ftransfer_pole.py](../../../../verification/v371_ftransfer_pole.py#L1) · explicit_script_identifier
- [verification/v380_grav_kms_hessian.py](../../../../verification/v380_grav_kms_hessian.py#L1) · explicit_script_identifier
- [verification/v375_observatory_registry.py](../../../../verification/v375_observatory_registry.py#L1) · explicit_script_identifier
- [verification/v370_grav_spin2_unitarity.py](../../../../verification/v370_grav_spin2_unitarity.py#L1) · explicit_script_identifier

## Appendix: computational verification

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex:4072-4089](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_2_standard_model.tex#L4072) · `section:c00bc2d86d1d497a58b2` · section

The Standard-Model identities used here (marked , , ) are re-derived from [formula in source] and machine-checked by the suite in the repository folder verification/; the inline tags [verification/ [formula in source] ] point to the exact script. Relevant here: v2_carrier_pascal.py — the carrier/Pascal packet ( [formula in source] , [formula in source] ). v3_em_alpha.py — the EM fixed point [formula in source] . v4_f

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_file_citation
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_file_citation
- [verification/v7_gravity_cosmo.py](../../../../verification/v7_gravity_cosmo.py#L1) · explicit_file_citation
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/README.md](../../../../verification/README.md#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## Research Contract — WOIT.OS.TWISTOR.01 (the Osterwalder–Schrader twistor bridge)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:12137-12469](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L12137) · `section:b191b0a66e5bacdc1a0e` · section

Typing. This is the actual bridge from compiler to physics — everything in CELEST.SEAM.01 is preparation for it. It is a research contract \ (ledger row WOIT.OS.TWISTOR.01: Open, research contract), not a claim; nothing below asserts that the construction exists. The external programme it engages — Woit's Euclidean Twistor Unification ( arXiv:2104.05099) — is a named reference frame for the shape of the target, never

Explicit source references:

- [verification/v522_woit_beta1_gso_gauge.py](../../../../verification/v522_woit_beta1_gso_gauge.py#L1) · explicit_file_citation
- [verification/v608_gamma_free_slice.py](../../../../verification/v608_gamma_free_slice.py#L1) · explicit_file_citation
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_file_citation
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_file_citation
- [verification/v519_woit_theta_rp_free.py](../../../../verification/v519_woit_theta_rp_free.py#L1) · explicit_file_citation
- [WOIT.THETA.FREE.01](../../../../verification/status_ledger.csv#L586) · explicit_claim_identifier · original status at linked ledger row
- [verification/v615_gamma_toy_interacting.py](../../../../verification/v615_gamma_toy_interacting.py#L1) · explicit_file_citation
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v524_woit_beta2_os_quotient.py](../../../../verification/v524_woit_beta2_os_quotient.py#L1) · explicit_script_identifier
- [verification/v565_woit_beta3_pt_duality.py](../../../../verification/v565_woit_beta3_pt_duality.py#L1) · explicit_file_citation
- [verification/v528_seam_bit_twist_class_definition.py](../../../../verification/v528_seam_bit_twist_class_definition.py#L1) · explicit_script_identifier
- [verification/v616_su2_internal_kinematic.py](../../../../verification/v616_su2_internal_kinematic.py#L1) · explicit_file_citation
- [WOIT.BETA3.DUALITY.01](../../../../verification/status_ledger.csv#L604) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.INT.OSAVOID.01](../../../../verification/status_ledger.csv#L751) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.STRADDLE.CONE.01](../../../../verification/status_ledger.csv#L597) · explicit_claim_identifier · original status at linked ledger row
- [verification/v517_celestial_wp5e_m3_a0_uplift.py](../../../../verification/v517_celestial_wp5e_m3_a0_uplift.py#L1) · explicit_script_identifier
- [WOIT.BETA1.GSO.01](../../../../verification/status_ledger.csv#L589) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.INT.ODDSPLIT.01](../../../../verification/status_ledger.csv#L750) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.INT.FKTOY.01](../../../../verification/status_ledger.csv#L596) · explicit_claim_identifier · original status at linked ledger row
- [verification/v492_celestial_z4_orbifold.py](../../../../verification/v492_celestial_z4_orbifold.py#L1) · explicit_script_identifier
- [verification/v510_seam_bit_freedom.py](../../../../verification/v510_seam_bit_freedom.py#L1) · explicit_script_identifier
- [CELEST.SEAM.01](../../../../verification/status_ledger.csv#L556) · explicit_claim_identifier · original status at linked ledger row
- [verification/v972_seam_interaction_front.py](../../../../verification/v972_seam_interaction_front.py#L1) · explicit_file_citation
- [SEAM.THERMAL.KMS.01](../../../../verification/status_ledger.csv#L593) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.TWISTOR.01](../../../../verification/status_ledger.csv#L584) · explicit_claim_identifier · original status at linked ledger row
- [WOIT.BETA2.OS.01](../../../../verification/status_ledger.csv#L591) · explicit_claim_identifier · original status at linked ledger row
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_script_identifier
- [SEAM.CLOCK.SILVER.01](../../../../verification/status_ledger.csv#L594) · explicit_claim_identifier · original status at linked ledger row
- [verification/v527_seam_clock_silver_spectrum.py](../../../../verification/v527_seam_clock_silver_spectrum.py#L1) · explicit_file_citation
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v519 round: WOIT.THETA.FREE.01 -- the WOIT-alpha milestone of the OS twistor bridge: the real structure exists (two-family classification, mu4 torsor, Z8/C^4/Cl(16) levels) and the exact free-RP preconditions + site-cut degeneration + continuum control. The 40-digit positive- definiteness inertia certificates of the bond-cut Grams (R3/R5) are Python-only by the suite convention (mpmath eigh at dps 40). Mirrors v519. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7077)
- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)
- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [(* ==== v510 round: SEAM.BIT.FREEDOM.01 -- the freedom attack on the v506/v507 alignment bit: the POSITION half of the bit is topology. Exact content mirrored: (i) the DIHEDRAL CENSUS -- on the refined 2N-point seam circle D_16 has 17 involutions with EXACTLY ONE free (the antipodal shift by 8) and all 16 reflections have exactly 2 circle fixed points (8 site-axis + 8 edge-axis; robustness N = 8, 12; odd control N = 9: zero free), plus the quotient topology chi(C/antipode) = 0 (circle) vs chi(C/reflection) = 1 (interval, 2 boundary corners); (ii) the AUT COMPLETENESS -- Aut(C_8) = D_8 by brute force over all 8! = 40320 permutations and Aut(C_16) = D_16 by degree-2 propagation (all 32 candidates), so the census covers ALL circle symmetries; (iii) the Cl(16) DICHOTOMY CENSUS -- on explicit 256x256 Jordan-Wigner gammas the free deck's NS implementer squares to 256 gamma_1...gamma_16 = 256 (-1)^F (nonsplit) while the implementers of ALL 16 reflections exist (one of the two spin lifts +-R) and square to SCALARS {2^7 (site-axis), 2^8 (edge-axis)} (split): NONSPLIT <=> FREE over the complete census; root dichotomy 2 (the +-quarter shifts) vs 0 total over all 16 reflections; (iv) the REAL-STRUCTURE TABLE -- the deck-commuting antiholomorphic involutions solve symbolically to exactly two families (M diagonal: mu conj z, fix line through the poles; M antidiagonal: mu/conj z, fix circle |z| = sqrt mu), and the unique mark-fixing real structure per configuration is equatorial/FREE for mu4 and generic-unit, real-axis/NOT-free for silver and generic-real, and NONEXISTENT for the hexagonal frame; (v) HARMONIC + FREE => mu4 -- the deck-pair cross-ratio (1-b)^2/(1+b)^2 = -1 solves exactly to b = +-i, with the lambda table (2, 1/2, 3/4, 5/4) real and the hexagonal lambda complex; (vi) the HONEST COUNTERWITNESSES -- the discrete witness {0,1,8,9} (shift-invariant, crossing, but not quarter-shift-invariant) and the continuous witness {+-1, +-(3+4i)/5} (pair cross-ratio -1/4, j = 148176/25 != 1728, clock does not preserve): the Fock dichotomy measures the CLASS, not the modulus. The Moebius/Klein covering models and the pillowcase branch control stay Python-side (v510). Mirrors v510. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L5155)
- [(* ==== v522 round: WOIT.BETA1.GSO.01 -- "the clock is time-like, GSO is the gauge datum": the Z8/NS tower + Ramond control, the invariant- dimension chain, the time-like reflection census, the exact Hermiticity witness of the clock insertion, the GSO 2-torsion census and the family-A tower-normalisation failure. The 40-digit GSO-fixed RP inertia certificates ((29,0,0)/(8,0,0)/(7,9,6)/(17,12,0)) are Python-only by the suite convention. Mirrors v522. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7609)
- [(* ==== v524 round: WOIT.BETA2.OS.01 -- "the OS quotient of the free system made explicit" (verdict SUCCESS, [C]-typed per contract precision (iii)). Four exact mirrors: (i) the euclidean-rotation preconditions (alpha_1^N = (-1)^F wrap arithmetic at N = 16 and N = 8) + the exact PD certificate identity sin^2(3pi/8) - sin(pi/8) sin(5pi/8) = 1/2; (ii) the Klein-Landau one-particle transfer forms tau_k on the shrinking domains at N = 16, k = 1..7: exactly Hermitian, odd k with exactly ZERO diagonal (the C(even) = 0 checkerboard), even k = 2j obeying the exact square identity tau_2j(a, b) = <alpha_j a, alpha_j b> entrywise; (iii) the clock identities (C(9) = C(7), C(11) = C(5), the transparency product formula sin(7pi/16) - sin(5pi/16) = 2 cos(3pi/8) sin(pi/16) > 0) + the N = 8 compressed clock spectrum EXACTLY {1, sqrt(2)-1} = {1, 1/delta_S} via the generalized eigenvalues of (tau_2, G) on the one-particle domain, with sin(pi/8)/sin(3pi/8) = sqrt(2)-1; (iv) the pre-declared KMS witnesses (C(1)/C(3) = 1 + sqrt(2) = delta_S at N = 8; -(C5-C7)((C3-C7)+(C5-C7)) < 0 exactly at N = 16, i.e. det(G - tau_4) < 0 on the odd one-particle clock block). The 37x37/16x16 H_phys Grams, the 40-digit inertia certificates, the spectral projections and the reconstructed rotation group are numerical (mpmath eighe), Python-only, flagged here. Mirrors v524. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7965)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v517 round: CELEST.WP5E.M3.01 -- "the a0 uplift": milestone M3 of the CELEST.SEAM.01 back-reaction programme executed (SUCCESS on the preregistered v514 S8.3 criterion). Six exact mirrors: (i) the GH multipole ledger (selection rule m = 0 mod 4, (4, +-4) amplitude (35/16) sin^4 th) + the twistor family at general orbit phase (e1 = e3 = 0, a2 = 4 z0 zb0 zeta^2, a0(zeta), v515 slice), (ii) the kernel bridge (null coordinate: any kernel harmonic; residue V-ledger identity 1/(2r); source flux -4 pi per centre), (iii) the asymptotic kernel log (coefficient 4 = |mu4|, first seam correction a0/eta^4, exact m-grading, GLT tower p_{4k} = 4(-a0)^k with the n = 0 mod 4 selection rule, no log x power terms), (iv) the exceptional-locus log (chi(0) = log a0 = 4 log t0 + i(4 phi0 + pi), modulus response 1 at the locus vs power-law at infinity), (v) the period response (linear in t0, d log Pi/d log a0 = 1/4 = 1/|mu4|, integrated monodromy i = one Coxeter clock step, centre permutation, a0-rigid node support, K4 discriminants ~ t0^2), and (vi) the negative controls ((4,0) clock-invariant, Z2/EH reads 2 on every dial, k = 3/5 orbits move the coefficient, the forbidden family fails both dials). The contour-transform typing itself is the [C] GLT dictionary; the BM kernel anchor is already mirrored in the v515 round. Mirrors v517. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L6678)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v527 round: SEAM.CLOCK.SILVER.01 -- silver explained / demystified. Exact mirrors: (i) tan(pi/8) Hankel pencil; (ii) N-scaling witness; (iii) gap = arcsinh(1) = gd^{-1}(pi/4). Census Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8187)
- [(* ==== v528 round: SEAM.BIT.TWISTCLASS.01 -- bit = twist-class choice. Exact mirrors: (i) cardinality lemma; (ii) 224-axis flip census; (iii) O-values. Pfaffian spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8213)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)

## Research Contract — CCC.SEAM.CROSSOVER.01 (the conformal-cyclic crossover on the seam geometry)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:12470-12570](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L12470) · `section:f8ad9138e39428999ab9` · section

Typing. A research contract \ (ledger row CCC.SEAM.CROSSOVER.01: Open, research contract), not a claim. It engages Penrose's Conformal Cyclic Cosmology (Tod, arXiv:1309.7248; Penrose–Meissner, arXiv:2503.24263) as a named reference frame for the shape of the target — never a confirmation in either direction. The cyclic reading of origin_theory stays \ regardless of this contract's fate; nothing below asserts that CCC

Explicit source references:

- [VGEO.TORSOR.01](../../../../verification/status_ledger.csv#L670) · explicit_claim_identifier · original status at linked ledger row
- [verification/v221_seam_qecc.py](../../../../verification/v221_seam_qecc.py#L1) · explicit_script_identifier
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [verification/v534_seam_straddle_cone.py](../../../../verification/v534_seam_straddle_cone.py#L1) · explicit_script_identifier
- [CCC.SEAM.CROSSOVER.01](../../../../verification/status_ledger.csv#L738) · explicit_claim_identifier · original status at linked ledger row
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_file_citation
- [CCC.SEAM.KINEMATICS.01](../../../../verification/status_ledger.csv#L737) · explicit_claim_identifier · original status at linked ledger row
- [verification/v529_seam_interacting_toy_fk.py](../../../../verification/v529_seam_interacting_toy_fk.py#L1) · explicit_script_identifier
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_script_identifier
- [verification/v522_woit_beta1_gso_gauge.py](../../../../verification/v522_woit_beta1_gso_gauge.py#L1) · explicit_script_identifier
- [verification/v976_seam_lift_birkhoff.py](../../../../verification/v976_seam_lift_birkhoff.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [(* ==== v534 round: SEAM.STRADDLE.CONE.01 -- the RP cone on the interacting FK quartets (the first dynamical selection of the alignment bit). Exact mirrors: the stabilizer census of the mark family, the pi/2 partition + straddle incidence, the reflection-closure signs of the straddling quartets, and the equivariant Fix rays (uniform on m=2..6, NS-wrap-twisted on m=1,7). The 256-dim Fock spectra, the PT Gram corrections and the finite-g survival scan are Python-only (numpy), flagged per GATE.WOLFRAM.02. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8401)
- [(* ==== v522 round: WOIT.BETA1.GSO.01 -- "the clock is time-like, GSO is the gauge datum": the Z8/NS tower + Ramond control, the invariant- dimension chain, the time-like reflection census, the exact Hermiticity witness of the clock insertion, the GSO 2-torsion census and the family-A tower-normalisation failure. The 40-digit GSO-fixed RP inertia certificates ((29,0,0)/(8,0,0)/(7,9,6)/(17,12,0)) are Python-only by the suite convention. Mirrors v522. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7609)
- [(* ==== v529 round: SEAM.INT.FKTOY.01 -- interacting FK toy / Kill-Test-2 shadow. Exact mirrors: (i) Z8 integer identities; (ii) straddle combinatorics; (iii) FK binomial ladder multiplicities. 256-dim spectra Python-only. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8245)

## Firewall Contract — DIMENSION.UPLIFT.FIREWALL.01 (no [formula in source] D theorem closes a [formula in source] D claim)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:12571-12632](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L12571) · `section:ea28e660b1549c41a88a` · section

Typing. A standing discipline rule, in force immediately (ledger row DIMENSION.UPLIFT.FIREWALL.01); the uplift theorems it names are separate \ contracts. It formalizes the core diagnosis of the 2026-08-27 external deep review: a chiral [formula in source] D seam net does not imply a local, interacting [formula in source] D quantum world. The corpus's strongest finite results are boundary/kinematic building blocks — 

Explicit source references:

- [experiments/tfpt-discovery/ccc_uplift_4d_probe.py](../../../../experiments/tfpt-discovery/ccc_uplift_4d_probe.py#L1) · explicit_file_citation
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_script_identifier
- [CELEST.SEAM.01](../../../../verification/status_ledger.csv#L556) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — SEAM.BULK4D.RECON.01 (from seam data to a 4D local quantum theory)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:12633-12686](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L12633) · `section:fbf67a6377a333f71dff` · section

Typing. A research contract \ (ledger row SEAM.BULK4D.RECON.01: Open, research contract), not a claim. It makes explicit the theorem that was previously only implicit between the SEAM.EQUIV.01 conclusion (a chiral [formula in source] boundary object) and the WOIT.OS.TWISTOR.01 goal statement (a Poincar\'e-covariant, causal, chiral 4D theory): the missing seam [formula in source] bulk reconstruction is a theorem of it

Explicit source references:

- [verification/v1020_spectator_sector_obstruction.py](../../../../verification/v1020_spectator_sector_obstruction.py#L1) · explicit_file_citation
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v524_woit_beta2_os_quotient.py](../../../../verification/v524_woit_beta2_os_quotient.py#L1) · explicit_script_identifier
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v519_woit_theta_rp_free.py](../../../../verification/v519_woit_theta_rp_free.py#L1) · explicit_script_identifier
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_script_identifier
- [WOIT.OS.TWISTOR.01](../../../../verification/status_ledger.csv#L585) · explicit_claim_identifier · original status at linked ledger row
- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [verification/v377_seam_s3_e8character.py](../../../../verification/v377_seam_s3_e8character.py#L1) · explicit_script_identifier
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [BULK.PRIME_COMPLETION.01](../../../../verification/status_ledger.csv#L773) · explicit_claim_identifier · original status at linked ledger row
- [verification/v957_ccc_crossover_kinematics.py](../../../../verification/v957_ccc_crossover_kinematics.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [(* ==== v524 round: WOIT.BETA2.OS.01 -- "the OS quotient of the free system made explicit" (verdict SUCCESS, [C]-typed per contract precision (iii)). Four exact mirrors: (i) the euclidean-rotation preconditions (alpha_1^N = (-1)^F wrap arithmetic at N = 16 and N = 8) + the exact PD certificate identity sin^2(3pi/8) - sin(pi/8) sin(5pi/8) = 1/2; (ii) the Klein-Landau one-particle transfer forms tau_k on the shrinking domains at N = 16, k = 1..7: exactly Hermitian, odd k with exactly ZERO diagonal (the C(even) = 0 checkerboard), even k = 2j obeying the exact square identity tau_2j(a, b) = <alpha_j a, alpha_j b> entrywise; (iii) the clock identities (C(9) = C(7), C(11) = C(5), the transparency product formula sin(7pi/16) - sin(5pi/16) = 2 cos(3pi/8) sin(pi/16) > 0) + the N = 8 compressed clock spectrum EXACTLY {1, sqrt(2)-1} = {1, 1/delta_S} via the generalized eigenvalues of (tau_2, G) on the one-particle domain, with sin(pi/8)/sin(3pi/8) = sqrt(2)-1; (iv) the pre-declared KMS witnesses (C(1)/C(3) = 1 + sqrt(2) = delta_S at N = 8; -(C5-C7)((C3-C7)+(C5-C7)) < 0 exactly at N = 16, i.e. det(G - tau_4) < 0 on the odd one-particle clock block). The 37x37/16x16 H_phys Grams, the 40-digit inertia certificates, the spectral projections and the reconstructed rotation group are numerical (mpmath eighe), Python-only, flagged here. Mirrors v524. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7965)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [(* ==== v519 round: WOIT.THETA.FREE.01 -- the WOIT-alpha milestone of the OS twistor bridge: the real structure exists (two-family classification, mu4 torsor, Z8/C^4/Cl(16) levels) and the exact free-RP preconditions + site-cut degeneration + continuum control. The 40-digit positive- definiteness inertia certificates of the bond-cut Grams (R3/R5) are Python-only by the suite convention (mpmath eigh at dps 40). Mirrors v519. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L7077)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)

## Research Contract — BULK.PRIME_COMPLETION.01 (prime/seam-generated completions, no spectator)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:12687-12725](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L12687) · `section:9541b674d713737f6e7f` · section

Typing. A research contract \ (ledger row BULK.PRIME_COMPLETION.01: Open, research contract), not a claim. Registered 2026-09-04 from the r644 audit harvest; it replaces the ``unique from seam data alone'' reading of SEAM.BULK4D.RECON.01/B7 by uniqueness in the category of seam-generated (prime) completions. Dimension typing ( DIMENSION.UPLIFT.FIREWALL.01 F2): the hypothesis is [formula in source] D free-fermion, the

Explicit source references:

- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [BULK.PRIME_COMPLETION.01](../../../../verification/status_ledger.csv#L773) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1020_spectator_sector_obstruction.py](../../../../verification/v1020_spectator_sector_obstruction.py#L1) · explicit_file_citation
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row

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

## Research Contract — CHIRAL4D.MIRROR.DET16.01 (DET16 rank-one projector, finite cluster)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13029-13091](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13029) · `section:845ed867739988332e9e` · section

Typing. A candidate \ (ledger row CHIRAL4D.MIRROR.DET16.01), registered 2026-08-29 from review wave 5. ( v1002_ spin10_ mirror_ projector.py.) Content. Exact finite-cluster gapping on the full chiral [formula in source] Fock space via the number-violating determinant vertex, as executed above. Open. Dynamical gauge fields, domain-wall geometry, and a [formula in source] D volume theorem — this is not a [formula in so

Explicit source references:

- [verification/v1007_det16_stability_battery.py](../../../../verification/v1007_det16_stability_battery.py#L1) · explicit_file_citation
- [CHIRAL4D.MIRROR.DFILTER.BLOCK.01](../../../../verification/status_ledger.csv#L776) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [verification/v1023_derivative_filtered_wall.py](../../../../verification/v1023_derivative_filtered_wall.py#L1) · explicit_file_citation
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1002_spin10_mirror_projector.py](../../../../verification/v1002_spin10_mirror_projector.py#L1) · explicit_file_citation
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row

## Firewall Contract — GRAV.NONCIRCULAR.01 (the Bisognano–Wichmann direction discipline)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13092-13141](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13092) · `section:9f2ef8163653328e6c3e` · section

Typing. A standing discipline rule, in force immediately (ledger row GRAV.NONCIRCULAR.01), with an audit census at registration. Bisognano–Wichmann (BW) is a theorem within an already-local, Poincar\'e-covariant QFT with a suitable vacuum: the modular flow of a wedge algebra acts as the boost. It is not a device that generates Lorentz spacetime from an arbitrary modular flow — there exist Poincar\'e-covariant nets vi

Explicit source references:

- [verification/v438_seam_hsmi_borchers.py](../../../../verification/v438_seam_hsmi_borchers.py#L1) · explicit_script_identifier
- [verification/v215_seam_deck_killtest.py](../../../../verification/v215_seam_deck_killtest.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v440_seam_lto_rp_beta.py](../../../../verification/v440_seam_lto_rp_beta.py#L1) · explicit_script_identifier
- [verification/v526_seam_thermal_kms_nariai_bridge.py](../../../../verification/v526_seam_thermal_kms_nariai_bridge.py#L1) · explicit_script_identifier
- [verification/v369_qgamb_redundancy.py](../../../../verification/v369_qgamb_redundancy.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [QG.AMB.01](../../../../verification/status_ledger.csv#L47) · explicit_claim_identifier · original status at linked ledger row
- [verification/v446_seam_clock_invariance.py](../../../../verification/v446_seam_clock_invariance.py#L1) · explicit_script_identifier
- [verification/v259_modular_cutoff_kappa.py](../../../../verification/v259_modular_cutoff_kappa.py#L1) · explicit_script_identifier
- [verification/v323_bw_geometric_modular.py](../../../../verification/v323_bw_geometric_modular.py#L1) · explicit_script_identifier
- [verification/v478_entropic_continuum_legs.py](../../../../verification/v478_entropic_continuum_legs.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)
- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ==== v503 round: QGEO.EMERGE.LIGHT.01 -- the v215 deferred emergence test (lever 7) executed light + the residual convergence QGEO-R1 == P2-R1. Exact/numeric content mirrored: (i) the CM-POINT IDENTITIES -- E2(i) = 3/Pi and E2(rho) = 2 Sqrt[3]/Pi (30-digit q-series vs the classical closed forms), hence E2*(i) = E2*(rho) = 0 EXACTLY by arithmetic; j(i) = 1728, j(rho) = 0 (KleinInvariantJ); DedekindEta[I] = Gamma[1/4]/(2 Pi^(3/4)) exact; (ii) NO DYNAMICAL SELECTION -- logF = log(tau2 |eta|^4) is S-invariant (30 digits at a generic point), the HEXAGONAL point wins (logF(rho) > logF(i)) and tau = i is a saddle (max along it, min along tau1 + i, sampled); (iii) the PILLOWCASE HALVING -- exact N = 8 discrete-torus spectrum (algebraic eigenvalues), Z2 pairing with exactly 4 self-paired cone modes, dim(even) = (N^2+4)/2 = 34, and det'_even^2 = det'_torus x prod_self EXACTLY; (iv) CLOCK => SQUARE + COXETER -- P(iZ) = P(Z) forces a3 = a2 = a1 = 0 (SolveAlways), j = 6912 I^3/(4 I^3 - J^2) = 1728 identically for Z^4 + a0, the order-4 element on H^1 has char poly lam^3 + lam^2 + lam + 1 (Coxeter of W(A3), order 4 = |mu4| = N_fam + 1), and Z6 = Aut(hexagonal) has element orders {1,2,3,6} -- no order 4. The v280-style lattice DtN curves (mod-4 off-character weights, sqrtm/expm) are numerical and stay Python-only (v503 B3-B5). Mirrors v503. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L4053)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ==== v526 round: SEAM.THERMAL.KMS.01 -- the thermal seam / third leg of c3. Exact mirrors: (i) Q-polynomial / measured beta = N at N = 8; (ii) beta_angle = 2 pi = 1/(4 c3) chain + Hawking/Nariai identities; (iii) nu char-poly / closed modular spectrum at N = 8. Tomita 40-digit residuals and the entropy tower are Python-only. Mirrors v526. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8139)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* ==== v237: closing step as physics -- no topological degeneracy <=> det K=1 <=> SRE ==== *) Module[{cartanA, cartanD, e8edges, E8, D8, A3, D5, carrier, gsd}, cartanA[n_] := SparseArray[{{i_, i_} -> 2, {i_, j_} /; Abs[i - j] == 1 -> -1}, {n, n}] // Normal; cartanD[n_] := Module[{K}, K = 2 IdentityMatrix[n]; Do[K[[i, i + 1]] = K[[i + 1, i]] = -1, {i, n - 2}]; K[[n - 2, n]] = K[[n, n - 2]] = -1; K]; e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; A3 = cartanA[3]; D5 = cartanD[5]; D8 = cartanD[8]; carrier = ArrayFlatten[{{D5, 0}, {0, A3}}]; gsd[K_, g_] := Abs[Det[K]]^g; checkExact["v237 GATE.HOLO.03: the closing step as a physical condition -- the abelian K-matrix " <> "ground-state degeneracy on a genus-g surface is |det K|^g (torus: carrier D5(+)A3 -> 16, D8 -> 4, " <> "E8 -> 1), so 'no topological ground-state degeneracy on any closed surface' <=> det K = 1 <=> the " <> "seam bulk is short-range-entangled (the unique bosonic SRE c=8 phase = the Kitaev E8 state, edge " <> "holomorphic). A unique vacuum on the plane (genus 0, always 1) is necessary but not sufficient; the " <> "torus sees |det K|. NEG: an LRE bulk (D8, det 4) has 4-fold torus degeneracy + non-holomorphic edge.", gsd[carrier, 1] == 16 && gsd[D8, 1] == 4 && gsd[E8, 1] == 1 && gsd[carrier, 2] == 256 && gsd[E8, 2] == 1 && gsd[carrier, 0] == 1 && gsd[E8, 0] == 1 && Det[E8] == 1 && (5 + 3 == 8)]; ]; (* ==== v259: the modular/KMS spectral-action cutoff fixes f_2/f_0 = 1 (PS.SPECACT.02) ==== v258 (Dirac as covariance induction) is numerical matrix-log linear algebra -> Python-only. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1991)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamStandardPair.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamStandardPair.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamRigidityForcing.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamRigidityForcing.lean#L1)

## Research Contract — OBS.TRANSDUCTION.01 (the transduction principle: eigenvalue, projection, coupling)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13142-13187](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13142) · `section:1a140dd2e54c1f43c055` · section

Typing. A research contract (ledger row OBS.TRANSDUCTION.01); the principle is machine-checked on the minimal model at exploration level, the per-bundle transduction proofs are . It elevates the S15 typing rule to a named principle: [formula in source] Without the middle arrow, neither a non-observation falsifies nor an observation confirms. The minimal model is machine-checked in experiments/ theory-contracts/ fo01_

Explicit source references:

- [verification/v990_wj_transduction_mechanism.py](../../../../verification/v990_wj_transduction_mechanism.py#L1) · explicit_file_citation
- [experiments/theory-contracts/fo01_transduction_invisibility.py](../../../../experiments/theory-contracts/fo01_transduction_invisibility.py#L1) · explicit_file_citation
- [OBS.TRANSDUCTION.01](../../../../verification/status_ledger.csv#L748) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — PRED.JOINTLIKELIHOOD.01 (from hit-counting to overdetermined relations)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13188-13235](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13188) · `section:f08abc84c0e5893cbfe5` · section

Typing. A research contract \ (ledger row PRED.JOINTLIKELIHOOD.01: Open, statistics-construction contract), not a claim. The [formula in source] individually matched values all descend from the same few atoms ( [formula in source] , [formula in source] , [formula in source] , [formula in source] ) and are therefore statistically correlated: counting hits overstates independent evidence. The evidence is to be reorgani

Explicit source references:

- [verification/v992_joint_likelihood_v1.py](../../../../verification/v992_joint_likelihood_v1.py#L1) · explicit_file_citation
- [verification/v100_numerology_null_mc.py](../../../../verification/v100_numerology_null_mc.py#L1) · explicit_script_identifier
- [docs/FALSIFICATION.md](../../../../docs/FALSIFICATION.md#L1) · explicit_file_citation
- [OBS.TRANSDUCTION.01](../../../../verification/status_ledger.csv#L748) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v84_frozen_registry.py](../../../../verification/v84_frozen_registry.py#L1) · explicit_script_identifier
- [PRED.JOINTLIKELIHOOD.01](../../../../verification/status_ledger.csv#L749) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v84) frozen registry decimals recompute from the axioms ---- *) phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); FU1[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 41 Log[1/phiseam[a]]; aStar = a /. FindRoot[FU1[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; check["v84 ALPHA_INV frozen", 1/aStar, 137.0359992168407125035379`30, 10^-20]; lamC = Sqrt[phi0 (1 - phi0)]; check["v84 SIN2_THETA12_SEED frozen", 1/3 - phi0/2, 0.3067473572449105696786871`30, 10^-20]; check["v84 SIN2_THETA13 frozen", phi0 Exp[-5/6], 0.02310843515888110429328466`30, 10^-20]; check["v84 BETA_BIREFRINGENCE_DEG frozen", (phi0/(4 Pi)) (180/Pi), 0.2424350309009295284924315`30, 10^-20]; check["v84 OMEGA_B frozen", (1 - 1/(4 Pi)) phi0, 0.04894066266545011220054565`30, 10^-20]; check["v84 LAMBDA_C frozen", lamC, 0.2243762368847217731120972`30, 10^-20]; check["v84 S23_CKM frozen", phi0/(1 + lamC), 0.04342778843220215630289116`30, 10^-20]; check["v84 S13_CKM frozen", lamC^3/3, 0.003765384454486429837965432`30, 10^-20]; check["v84 DELTA_CKM_RAD frozen", Pi/3 + 3 lamC^2, 1.198231638232244084651243`30, 10^-20]; check["v84 MMU_OVER_MTAU frozen", (8/7) phi0, 0.06076794534496631692490568`30, 10^-20]; check["v84 ME_OVER_MMU frozen", (12/7) phi0^2, 0.004846725425651567674771059`30, 10^-20]; checkExact["v84 MU_OVER_MD = 55/117 exactly", 55/117 == 55/117]; check["v84 MC_OVER_MS frozen", (34/47)/phi0, 13.60499710285539356302651`30, 10^-20]; check["v84 MT_OVER_MB frozen", (3/26)/phi0^2, 40.8115130177002629681607`30, 10^-20]; check["v84 MSCAL_OVER_MBAR frozen", c3^(7/2), 0.00001256494208322844896998079`30, 10^-20]; check["v84 RHOL_OVER_MBAR4 frozen", (3/(4 Pi^2)) Exp[-2/aStar], 7.125329526706216792033797`30 10^-121, 10^-15]; checkExact["v84 theta12 variants distinct (seed < seam < nonlin band)", (1/3 - phi0/2) < (1/3 - 1/(12 Pi))]; (* ---- (v85) master cover: GL(2) covariance on the anchor plane ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L38)
- [(* ---- (v122) margin theorem ---- *) Module[{rmat, qmat, sig, uax, colsT, c8, c0, cands, final}, rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; sig = DiagonalMatrix[{1, -1, -1}]; uax = 3 Outer[Times, {1, 1, 1}, {1, 0, 0}]; colsT[t_] := Select[Tuples[Range[0, 5], 3], 5 #[[1]] - 9 #[[2]] + 6 #[[3]] == t &]; c8 = colsT[8]; c0 = colsT[0]; cands = Select[Flatten[Table[Transpose[{a, b, c}], {a, c8}, {b, c0}, {c, c0}], 2], Det[#] == 8 &]; final = Select[cands, Det[# + qmat . sig] == 4 &]; checkExact["v122 census: 4 x 4 x 4 = 64 annihilator candidates, det 8 leaves 12, det K = 4 leaves exactly ONE = R", Length[c8] == 4 && Length[c0] == 4 && Length[cands] == 12 && Length[final] == 1 && final[[1]] == rmat]; checkExact["v122 corollary: margins are theorems - rows (4,8,10), cols (4,13,5), anchor column (1,1,2); bonus: det(M+2U) = 20 on ALL 12 candidates", (Total /@ final[[1]]) == {4, 8, 10} && Total[final[[1]]] == {4, 13, 5} && final[[1]][[All, 1]] == {1, 1, 2} && AllTrue[cands, Det[# + 2 uax] == 20 &]]; ]; (* ---- (v123) inventory update: ledger-bookkeeping module (CSV parsing of status_ledger.csv, typing contract) -- Python-only by nature, like the statistical v100; no algebraic content to mirror. ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L834)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## Verified Selector — DIMENSION.SELECTOR.4D.01 (why [formula in source] , conditionally)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13343-13377](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13343) · `section:8af62b489904198afb19` · section

Typing. A conditional identity \ (ledger row DIMENSION.SELECTOR.4D.01), machine-checked in v975_dimension_selector_4d.py ( [formula in source] , sympy-exact). The [formula in source] structure of the compiler must not be read as a proof of four spacetime dimensions ( DIMENSION.UPLIFT.FIREWALL.01); what is checkable is a selector theorem under a named axiom set. Statement. Under A1 [formula in source] (propagating loc

Explicit source references:

- [verification/v975_dimension_selector_4d.py](../../../../verification/v975_dimension_selector_4d.py#L1) · explicit_file_citation
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — SEAM.SIMPLECURRENT.GENERATOR.01 (one generator instead of 128 currents)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13378-13529](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13378) · `section:daecafc150c9651ad391` · section

Typing. A research contract \ (ledger row SEAM.SIMPLECURRENT.GENERATOR.01), not a claim. Context. The seam coverage carve ( v973_seam_route_narrowing.py) shows the [formula in source] fermion-bilinear half of the seam target is covered by the cited scaling-limit theorem; the named residual is N1 (the [formula in source] /GSO extension [formula in source] as a net statement — the 128 spinor currents are not bilinears)

Explicit source references:

- [verification/v973_seam_route_narrowing.py](../../../../verification/v973_seam_route_narrowing.py#L1) · explicit_file_citation
- [verification/v993_minimal_defect_selector.py](../../../../verification/v993_minimal_defect_selector.py#L1) · explicit_file_citation
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v469_seam_crossedproduct_route.py](../../../../verification/v469_seam_crossedproduct_route.py#L1) · explicit_script_identifier
- [verification/v998_seam_modular_closure.py](../../../../verification/v998_seam_modular_closure.py#L1) · explicit_file_citation
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v988_psi_lambda_reduction.py](../../../../verification/v988_psi_lambda_reduction.py#L1) · explicit_file_citation
- [verification/v813_p1_index_kms.py](../../../../verification/v813_p1_index_kms.py#L1) · explicit_script_identifier
- [verification/v983_simple_current_generator.py](../../../../verification/v983_simple_current_generator.py#L1) · explicit_file_citation
- [verification/v994_mmst_criteria_battery.py](../../../../verification/v994_mmst_criteria_battery.py#L1) · explicit_file_citation
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_script_identifier
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_script_identifier
- [verification/v624_external_lattice_audit.py](../../../../verification/v624_external_lattice_audit.py#L1) · explicit_script_identifier
- [verification/v484_seam_contact_unit.py](../../../../verification/v484_seam_contact_unit.py#L1) · explicit_script_identifier
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* v469 (i): the LR locality integers of both extension routes *) hs = 16/16; (* so(N)_1 spinor weight N/16, N = 16 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2930)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [(* ---- (v994) SEAM.EQUIV.MMST.01 C3: Theta_E8 / eta^8 = {1,248,4124,34752} ---- Python-only: C1 entropy, C2 QWZ spectrum, C4 two-point numeric, C5 sector recombination beyond det, C6 cited, C7 open, GSO/N=8 must-fail combinatorics. *)](../../../../verification/wolfram/tfpt_readouts.wl#L680)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [(* v463 (ii): the (E8)_1 tower = E4/eta^8 coefficients {1,248,4124,34752,213126} *) inv8 = Series[Product[(1 - q^n)^-8, {n, 1, 6}], {q, 0, 5}]; chiSer = Series[(1 + 240 Sum[DivisorSigma[3, n] q^n, {n, 1, 6}]) inv8, {q, 0, 5}]; tower = CoefficientList[Normal[chiSer], q][[1 ;; 5]]; checkExact["v463 SEAM.EQUIV.UNIQ.01 (ii): the holomorphic c=8 partition function is the unique j^{1/3}=E4/eta^8, whose q-coefficients are the (E8)_1 tower {1,248,4124,34752,213126} -- the q^1=248 is the forced weight-1 dimension (Dong-Mason/Schellekens: the holomorphic c=8 VOA is unique = V_{E8})", tower == {1, 248, 4124, 34752, 213126}]; ]; (* ==== v469 round: the net-level crossed-product certification -- the LR locality integers (h_s(SO(16)_1) = 16/16 = 1 in Z; the mu4 glue h(J^k) = {1,1,1} all integer), the KLM mu-index arithmetic (4/2^2 = 1 and 16/4^2 = 1, both holomorphic) and the Kitaev 16-fold-way pin (nu = 16 x |C| = 16 = 0 mod 16, c_- = nu/2 = 8 = g_car+N_fam); mirrors v469 (the FHS Chern itself is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2916)
- [(* ---- (v983) SEAM.SIMPLECURRENT.GENERATOR.01: glue vector lambda = (omega_s, omega_f) ---- *) Module[{omegaS, omegaF, lam, inD5, inA3, inL0, gensD5, gensA3, dots, cosetRoots, census, lamV, omega2, nV, n2, cartanD8}, omegaS = ConstantArray[1/2, 5]; omegaF = {3/4, -1/4, -1/4, -1/4}; lam = Join[omegaS, omegaF]; inD5[x_] := (And @@ (IntegerQ /@ x)) && EvenQ[Total[x]]; inA3[y_] := (And @@ (IntegerQ /@ y)) && Total[y] === 0; inL0[z_] := inD5[Take[z, 5]] && inA3[Take[z, {6, 9}]]; checkExact["v983 NORMS+WEIGHT [E]: |omega_s|^2=5/4, |omega_f|^2=3/4, |lambda|^2=2, h_lambda=1", Total[omegaS^2] === 5/4 && Total[omegaF^2] === 3/4 && Total[lam^2] === 2 && Total[lam^2]/2 === 1]; checkExact["v983 ORDER FOUR [E]: 4*lambda in D5(+)A3, lambda and 2*lambda not -- [lambda] generates the diagonal Z4", inL0[4 lam] && ! inL0[2 lam] && ! inL0[lam]]; gensD5 = {{1, 1, 0, 0, 0}, {1, -1, 0, 0, 0}, {0, 1, 1, 0, 0}, {0, 0, 1, 1, 0}, {0, 0, 0, 1, 1}}; gensA3 = {{1, -1, 0, 0}, {0, 1, -1, 0}, {0, 0, 1, -1}}; dots = Join[omegaS . # & /@ gensD5, omegaF . # & /@ gensA3]; checkExact["v983 ISOTROPY+UNIMODULAR [E]: lambda.L0 subset Z on a generator set; det(D5)*det(A3)=16, index-4 glue => det L=1", (And @@ (IntegerQ /@ dots)) && 16/4^2 === 1]; cosetRoots[k_] := Module[{t = k lam, d5, a3}, d5 = Counts @ Select[ Total[(# + Take[t, 5])^2] & /@ Select[Tuples[Range[-5, 3], 5], EvenQ[Total[#]] &], # <= 2 &]; a3 = Counts @ Select[ Total[(Join[#, {-Total[#]}] + Take[t, {6, 9}])^2] & /@ Tuples[Range[-6, 6], 3], # <= 2 &]; Total[KeyValueMap[#2 Lookup[a3, 2 - #1, 0] &, d5]]]; census = Table[cosetRoots[k], {k, 0, 3}]; checkExact["v983 COSET ROOT CENSUS [E]: norm-2 vectors per fusion power k=0..3 = {52,64,60,64}, total 240; odd powers 64+64=128", census === {52, 64, 60, 64} && Total[census] === 240 && census[[2]] + census[[4]] === 128]; lamV = Join[{1, 0, 0, 0, 0}, omegaF]; omega2 = {1/2, 1/2, -1/2, -1/2}; nV = Total[lamV^2]; n2 = Total[omegaS^2] + Total[omega2^2]; cartanD8 = {{2, -1, 0, 0, 0, 0, 0, 0}, {-1, 2, -1, 0, 0, 0, 0, 0}, {0, -1, 2, -1, 0, 0, 0, 0}, {0, 0, -1, 2, -1, 0, 0, 0}, {0, 0, 0, -1, 2, -1, 0, 0}, {0, 0, 0, 0, -1, 2, -1, -1}, {0, 0, 0, 0, 0, -1, 2, 0}, {0, 0, 0, 0, 0, -1, 0, 2}}; checkExact["v983 KILLS+HOLOMORPHY SHADOW [E]: vector glue (v,omega_f) norm 7/4 and mismatched (omega_s, omega_2) norm 9/4 not in 2Z; det Cartan D8=4 vs glued det=1", nV === 7/4 && n2 === 9/4 && Det[cartanD8] === 4 && 16/4^2 === 1]; ]; (* ---- (v985) ALPHA.QUILLEN.EXACT.01: mu4 circulant spectra + graded channel swap ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L444)
- [experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean#L1)
- [(* ---- (v993) AX.P2.01 census: SNF disc groups, unique (D5,A3), [lambda]^2=[v], CE dims ---- Python-only: random CE axiom sampling on M_d^{Z4} / crossed product. *)](../../../../verification/wolfram/tfpt_readouts.wl#L557)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)

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

## Research Contract — SEAM.DETLINE.UNIFICATION.01 (the determinant-line unification hypothesis)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13616-13662](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13616) · `section:203b4eaaede7d9249190` · section

Typing. A research hypothesis contract \ (ledger row SEAM.DETLINE.UNIFICATION.01) — a precise conjecture, not a result. Observation. Three separately open structures may be projections of one geometric object: (1) the seam extension is described by a Q-system/simple current ( SEAM.SIMPLECURRENT.GENERATOR.01); (2) the chiral fermion measure lives on a determinant line ( CHIRAL4D.NOMIRROR.01 demand C1); (3) anomalies a

Explicit source references:

- [SEAM.DETLINE.UNIFICATION.01](../../../../verification/status_ledger.csv#L758) · explicit_claim_identifier · original status at linked ledger row
- [verification/v991_detline_bulk_edge.py](../../../../verification/v991_detline_bulk_edge.py#L1) · explicit_file_citation
- [verification/v977_transfer_unistochastic_wilson.py](../../../../verification/v977_transfer_unistochastic_wilson.py#L1) · explicit_file_citation
- [verification/v974_alpha_faces_computed.py](../../../../verification/v974_alpha_faces_computed.py#L1) · explicit_file_citation
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_file_citation
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — FTRANSFER.GENERATING.01 (four transfer bridges from one generating functional)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13663-13696](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13663) · `section:6f0af99769531bda7e90` · section

Typing. A research contract \ (ledger row FTRANSFER.GENERATING.01); the constructive successor named by the FR.TRANSFER.01 typing guard. The four continuous-transfer interfaces ( [formula in source] : source masses [formula in source] pole, v183; [formula in source] : CP source [formula in source] , v169/ v184; [formula in source] : [formula in source] , v185; [formula in source] : [formula in source] , v164) are cur

Explicit source references:

- [FR.TRANSFER.01](../../../../verification/status_ledger.csv#L181) · explicit_claim_identifier · original status at linked ledger row
- [verification/v164_qcd_scale.py](../../../../verification/v164_qcd_scale.py#L1) · explicit_script_identifier
- [verification/v169_etaB_boltzmann_interface.py](../../../../verification/v169_etaB_boltzmann_interface.py#L1) · explicit_script_identifier
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_script_identifier
- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [verification/v990_wj_transduction_mechanism.py](../../../../verification/v990_wj_transduction_mechanism.py#L1) · explicit_file_citation
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_script_identifier
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)

## Research Contract — GAUGE.DETLINE.FIXPOINT.01 (all three gauge couplings from one zeta-det functional)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13697-13755](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13697) · `section:2256a2d99fd8e09d2837` · section

Typing. A research contract \ (ledger row GAUGE.DETLINE.FIXPOINT.01), registered 2026-08-28 from review wave 3. Demand. All three gauge couplings ( [formula in source] / equivalently [formula in source] , [formula in source] , [formula in source] ) arise as stationary points of one nonabelian zeta-det / inflow functional on the determinant line — the nonabelian upgrade of the [formula in source] face ALPHA.QUILLEN.EX

Explicit source references:

- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row
- [experiments/tfpt-discovery/gauge_stiffness_stepscaling_probe.py](../../../../experiments/tfpt-discovery/gauge_stiffness_stepscaling_probe.py#L1) · explicit_file_citation
- [experiments/tfpt-discovery/gauge_stiffness_fixpoint_probe.py](../../../../experiments/tfpt-discovery/gauge_stiffness_fixpoint_probe.py#L1) · explicit_file_citation
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1011_3p1d_ladder_battery.py](../../../../verification/v1011_3p1d_ladder_battery.py#L1) · explicit_file_citation
- [verification/v1008_master_assembly_scaffold.py](../../../../verification/v1008_master_assembly_scaffold.py#L1) · explicit_file_citation
- [verification/v996_gauge_grammar_kill.py](../../../../verification/v996_gauge_grammar_kill.py#L1) · explicit_script_identifier

## Research Contract — GRAV.SPIN2.EMERGENCE.01 (massless transversal spin-2 from the same spectral determinant)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13756-13823](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13756) · `section:3ef64d782ddc411f1754` · section

Typing. A research contract \ (ledger row GRAV.SPIN2.EMERGENCE.01), registered 2026-08-28 from review wave 3. Demand. From the same spectral determinant that carries the gauge fixpoints, a massless transversal spin-2 pole with two helicities, universal [formula in source] coupling, diffeomorphism Ward identities, and positive Hessian / reflection-positive transfer. Relation. The entanglement-equilibrium Einstein equa

Explicit source references:

- [verification/v997_spin2_smg_witnesses.py](../../../../verification/v997_spin2_smg_witnesses.py#L1) · explicit_file_citation
- [verification/v1000_spin2_sk_witnesses.py](../../../../verification/v1000_spin2_sk_witnesses.py#L1) · explicit_file_citation
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.PARENT.GAP.NO_GO.01](../../../../verification/status_ledger.csv#L778) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [verification/v358_grav_entropy_equilibrium.py](../../../../verification/v358_grav_entropy_equilibrium.py#L1) · explicit_script_identifier
- [verification/v359_grav_nonlinear_einstein.py](../../../../verification/v359_grav_nonlinear_einstein.py#L1) · explicit_script_identifier
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [GRAV.WEINBERG.WITTEN.01](../../../../verification/status_ledger.csv#L770) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v359 GRAV.NONLINEAR.01: full covariant Einstein eq, both coefficients parameter-free ==== *) Module[{c3, eta, d, Rs, traceG, dtop, prefactor}, c3 = 1/(8 Pi); eta = 1/4; traceG = (1 - d/2); (* g^{ab}G_ab = (1-d/2) R; coefficient of R *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2382)
- [(* ---- (v997) GRAV.SPIN2.EMERGENCE.01: Barnes-Rivers ranks (5,3,1,1) ---- Python-only: Weyl^2 ghost residues, random-p numeric, SMG N=8 Fidkowski-Kitaev toy (spectrum / Spin(7) / Schmidt / edge). *)](../../../../verification/wolfram/tfpt_readouts.wl#L699)
- [(* ==== v358 GRAV.ENTROPY.EQUILIBRIUM.01: parameter-free linearised Einstein + thermo=geo ==== *) Module[{c3, eta, Z2, mu4, chi, r, R, w, wint}, c3 = 1/(8 Pi); eta = 1/4; Z2 = 2; mu4 = 4; chi = 2; w = (R^2 - r^2)/(2 R); wint = Integrate[w * 4 Pi r^2, {r, 0, R}]; (* CHM 3-ball weight integral *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2371)

## Research Contract — FTRANSFER.SK.RHO0.01 (Schwinger–Keldysh completion: cosmological transfers need [formula in source] )

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13824-13892](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13824) · `section:16a3dfffba2175d45b88` · section

Typing. A research contract \ (ledger row FTRANSFER.SK.RHO0.01), registered 2026-08-28 from review wave 3; mechanism executed 2026-08-29. Demand. Cosmological transfers ( [formula in source] , [formula in source] , and any nonequilibrium 4D readout) need the pair [formula in source] , not [formula in source] alone — the Euclidean-cap / KMS initial state. Typed candidate. The [formula in source] saddle [formula in sou

Explicit source references:

- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row
- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1000_spin2_sk_witnesses.py](../../../../verification/v1000_spin2_sk_witnesses.py#L1) · explicit_file_citation
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [verification/v1009_rho0_minimizer.py](../../../../verification/v1009_rho0_minimizer.py#L1) · explicit_file_citation
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation
- [FTRANSFER.PARENT.Z5CAP.01](../../../../verification/status_ledger.csv#L779) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — SEAM.MMST.TYPEIII.CHARGED.01 (one scaling-limit theorem)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:13893-13935](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L13893) · `section:d185199a34886354d525` · section

Typing. A research contract \ (ledger row SEAM.MMST.TYPEIII.CHARGED.01), registered 2026-08-29 from review wave 5. Demand. One scaling-limit theorem [formula in source] strongly on the finite-energy core [formula in source] crossed-product continuity, from which [formula in source] , [formula in source] , type III [formula in source] , unique rotational KMS, unique conditional expectation, deck equidistribution and m

Explicit source references:

- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1006_mmst_lemma_battery.py](../../../../verification/v1006_mmst_lemma_battery.py#L1) · explicit_file_citation
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [verification/v998_seam_modular_closure.py](../../../../verification/v998_seam_modular_closure.py#L1) · explicit_script_identifier

## Research Contract — TFPT.TOE.COMPLETE.01 (the named AND of eight completeness gates)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:14103-14237](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L14103) · `section:14713793ccdcb9ca035e` · section

Typing. A research contract \ (ledger row TFPT.TOE.COMPLETE.01), registered 2026-08-29 from review wave 4. This row names the AND of eight gates; it does not close any of them and it does not upgrade a marker. Dual rest: the compiler residual [formula in source] sits beside [formula in source] ; this contract is the named AND, not a closure of either.

Explicit source references:

- [FTRANSFER.GENERATING.01](../../../../verification/status_ledger.csv#L759) · explicit_claim_identifier · original status at linked ledger row
- [TFPT.IRREDUCIBLE.01](../../../../verification/status_ledger.csv#L103) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.MMST.TYPEIII.CHARGED.01](../../../../verification/status_ledger.csv#L767) · explicit_claim_identifier · original status at linked ledger row
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_file_citation
- [verification/v1023_derivative_filtered_wall.py](../../../../verification/v1023_derivative_filtered_wall.py#L1) · explicit_file_citation
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [FLAV.NU.TEXTURE.MECHANISM.01](../../../../verification/status_ledger.csv#L768) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation
- [verification/v1013_thermodynamic_dynamics.py](../../../../verification/v1013_thermodynamic_dynamics.py#L1) · explicit_file_citation
- [GAUGE.DETLINE.FIXPOINT.01](../../../../verification/status_ledger.csv#L761) · explicit_claim_identifier · original status at linked ledger row
- [DYN.MARKOV.EMBED.01](../../../../verification/status_ledger.csv#L741) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.SIMPLECURRENT.GENERATOR.01](../../../../verification/status_ledger.csv#L756) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1020_spectator_sector_obstruction.py](../../../../verification/v1020_spectator_sector_obstruction.py#L1) · explicit_script_identifier
- [TFPT.TOE.COMPLETE.01](../../../../verification/status_ledger.csv#L764) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.NONCIRCULAR.01](../../../../verification/status_ledger.csv#L747) · explicit_claim_identifier · original status at linked ledger row
- [ALPHA.QUILLEN.EXACT.01](../../../../verification/status_ledger.csv#L445) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row
- [AX.P1.01](../../../../verification/status_ledger.csv#L2) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.WEINBERG.WITTEN.01](../../../../verification/status_ledger.csv#L770) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.TWISTOR.01](../../../../verification/status_ledger.csv#L584) · explicit_claim_identifier · original status at linked ledger row
- [TFPT4D.LATTICE.ACTION.01](../../../../verification/status_ledger.csv#L757) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1025_telb_c1_c2a_certificates.py](../../../../verification/v1025_telb_c1_c2a_certificates.py#L1) · explicit_file_citation
- [OBS.TRANSDUCTION.01](../../../../verification/status_ledger.csv#L748) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.OS.RECON.01](../../../../verification/status_ledger.csv#L745) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NUSCALE.01](../../../../verification/status_ledger.csv#L365) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1015_axiom_core_closure.py](../../../../verification/v1015_axiom_core_closure.py#L1) · explicit_file_citation
- [SEAM.DETLINE.UNIFICATION.01](../../../../verification/status_ledger.csv#L758) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1022_telb_round3_certificates.py](../../../../verification/v1022_telb_round3_certificates.py#L1) · explicit_file_citation
- [FTRANSFER.SK.RHO0.01](../../../../verification/status_ledger.csv#L763) · explicit_claim_identifier · original status at linked ledger row
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.MIRROR.DET16.01](../../../../verification/status_ledger.csv#L766) · explicit_claim_identifier · original status at linked ledger row
- [CHIRAL4D.NOMIRROR.01](../../../../verification/status_ledger.csv#L746) · explicit_claim_identifier · original status at linked ledger row
- [SEAM.STATE.RPMIXING.01](../../../../verification/status_ledger.csv#L752) · explicit_claim_identifier · original status at linked ledger row
- [QFT4D.LATTICE.FUNDAMENTAL.01](../../../../verification/status_ledger.csv#L760) · explicit_claim_identifier · original status at linked ledger row
- [PRED.JOINTLIKELIHOOD.01](../../../../verification/status_ledger.csv#L749) · explicit_claim_identifier · original status at linked ledger row

## Research Contract — FLAV.NUSCALE.06 (pentagon-class misalignment candidate)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:14238-14255](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L14238) · `section:f66120aaaa353a653001` · section

Typing. A candidate \ (ledger row FLAV.NUSCALE.06); mechanism [formula in source] the [formula in source] -to-flavor operator . No seesaw closure; FLAV.NUSCALE.05 unmoved. ( v1001_ nu_ pentagon_ chain.py.)

Explicit source references:

- [verification/v270_pmns_jarlskog_assembly.py](../../../../verification/v270_pmns_jarlskog_assembly.py#L1) · explicit_script_identifier
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [verification/v9_neutrino_texture.py](../../../../verification/v9_neutrino_texture.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v1001_nu_pentagon_chain.py](../../../../verification/v1001_nu_pentagon_chain.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.06](../../../../verification/status_ledger.csv#L765) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean#L1)
- [(* ==== v268: reactor-angle exponent = carrier hypercharge trace (FLAV.TH13.01) ==== *) Module[{Yvec, trY2, roots}, roots = Sort[Y /. Solve[6 Y^2 - Y - 1 == 0, Y]]; Yvec = {-1/3, -1/3, -1/3, 1/2, 1/2}; trY2 = Total[Yvec^2]; checkExact["v268 FLAV.TH13.01: the theta_13 exponent is the carrier hypercharge trace -- " <> "tr_E Y^2 = 3(1/3)^2 + 2(1/2)^2 = 5/6 over the 5-slot carrier hypercharge " <> "Y=diag(-1/3,-1/3,-1/3,1/2,1/2) (the anomaly-free roots {-1/3,1/2} of 6Y^2-Y-1=0), so " <> "sin^2 theta_13 = phi0 e^{-5/6} = phi0 e^{-tr_E Y^2}; complement 1 - 5/6 = 1/6 = the neutrino ratio. " <> "theta_13 is its own carrier-trace channel (the mu-tau breaking gives only ~1e-3, not 0.023).", roots === Sort[{-1/3, 1/2}] && trY2 === 5/6 && (1 - trY2) === 1/6]; ]; (* ==== v271: concrete Epstein-Glaser one-loop quartic renormalization (QFT4D.SPERT.02) ==== v269 (S_pert skeleton) + v270 (PMNS Jarlskog, numerical) are Python-only; v271's exact EG core (scaling degree, counterterm count, loop factor) is mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2069)

## Research Contract — FLAV.NU.TEXTURE.MECHANISM.01 (both structural nulls as binding constraints)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:14256-14301](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L14256) · `section:b26740716a2d0cca0ac3` · section

Typing. A research contract \ (ledger row FLAV.NU.TEXTURE.MECHANISM.01), registered 2026-08-29 from review wave 5. ( v1003_ nu_ structural_ nulls.py.) Executed content. Charged-sector data [formula in source] , [formula in source] (coset min-norms all [formula in source] ) . Schur-texture NULL : all [formula in source] preregistered [formula in source] combinations fail; D4 reflection forces [formula in source] ; hie

Explicit source references:

- [verification/v1024_parent_internal_boundaries.py](../../../../verification/v1024_parent_internal_boundaries.py#L1) · explicit_file_citation
- [FLAV.NUSCALE.05](../../../../verification/status_ledger.csv#L550) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NU.TEXTURE.MECHANISM.01](../../../../verification/status_ledger.csv#L768) · explicit_claim_identifier · original status at linked ledger row
- [FLAV.NU.PARENT.INTERTWINER.01](../../../../verification/status_ledger.csv#L777) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1012_toe_gate_witnesses.py](../../../../verification/v1012_toe_gate_witnesses.py#L1) · explicit_file_citation
- [verification/v1003_nu_structural_nulls.py](../../../../verification/v1003_nu_structural_nulls.py#L1) · explicit_file_citation

## Research Contract — SEAM.MILNOR.LOCALRING.01 (canonical identification of the seam collar with the reduced Milnor algebra)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:14302-14380](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L14302) · `section:789583ec50a9f61cdf33` · section

Typing. A research contract \ (ledger row SEAM.MILNOR.LOCALRING.01), registered 2026-08-30 from review wave 6. ( v1004_ milnor_ frobenius_ gray.py.) Demand. A canonical identification between the raw seam collar / [formula in source] transition bus and the reduced Milnor algebra [formula in source] preserving simultaneously the dual-number action, the Frobenius pairing, the Gray torsor, the deck action and CP. Accept

Explicit source references:

- [verification/v1005_relative_pencil_bridges.py](../../../../verification/v1005_relative_pencil_bridges.py#L1) · explicit_file_citation
- [verification/v106_review_validation.py](../../../../verification/v106_review_validation.py#L1) · explicit_script_identifier
- [AX.P2.01](../../../../verification/status_ledger.csv#L3) · explicit_claim_identifier · original status at linked ledger row
- [verification/v1015_axiom_core_closure.py](../../../../verification/v1015_axiom_core_closure.py#L1) · explicit_file_citation
- [verification/v1004_milnor_frobenius_gray.py](../../../../verification/v1004_milnor_frobenius_gray.py#L1) · explicit_file_citation
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v1010_simplicity_bridge_census.py](../../../../verification/v1010_simplicity_bridge_census.py#L1) · explicit_file_citation
- [verification/v119_review_validation_2.py](../../../../verification/v119_review_validation_2.py#L1) · explicit_script_identifier
- [verification/v1014_bridge_refinements.py](../../../../verification/v1014_bridge_refinements.py#L1) · explicit_file_citation
- [SEAM.MILNOR.LOCALRING.01](../../../../verification/status_ledger.csv#L769) · explicit_claim_identifier · original status at linked ledger row

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean#L1)
- [(* ---- (v118) hexagon-family dictionary ---- *) Module[{m0, usym, t, z6, specU, mu6, detm, detp, elems, frontier, newE}, m0 = {{0, -(1 + I)/2, (1 - I)/2}, {-(1 + I)/2, -I/2, -1/2}, {(1 - I)/2, -1/2, I/2}}; usym = DiagonalMatrix[{1, I, -I}]; z6 = Exp[I Pi/3]; specU = Sort[Join[Eigenvalues[m0], -Eigenvalues[m0]], LessEqual[Arg[#1], Arg[#2]] &]; mu6 = Sort[Table[Exp[I Pi k/3], {k, 0, 5}], LessEqual[Arg[#1], Arg[#2]] &]; checkExact["v118 sign-twist lemma: (-M0)^3 = -1 and spec(M0) u spec(-M0) = mu_6 (the hexagon); denominators 5/4 - cos(r pi/3) = |1 - zeta_6^r/2|^2", Simplify[MatrixPower[-m0, 3]] === -IdentityMatrix[3] && AllTrue[Transpose[{FullSimplify[specU], FullSimplify[mu6]}], FullSimplify[#[[1]] - #[[2]]] === 0 &] && AllTrue[Range[0, 5], FullSimplify[(5/4 - Cos[# Pi/3]) - (1 - z6^#/2) (1 - Conjugate[z6^#]/2)] === 0 &]]; t = \[FormalT]; detm = Det[IdentityMatrix[3] - m0/2]; detp = Det[IdentityMatrix[3] + m0/2]; checkExact["v118 cyclotomic determinant: det(1 - t M0) = 1 - t^3; det(1 -+ M0/2) = (7/8, 9/8)", FullSimplify[Det[IdentityMatrix[3] - t m0] - (1 - t^3)] === 0 && Simplify[detm] == 7/8 && Simplify[detp] == 9/8]; checkExact["v118 lepton coefficients = resolvent determinants: c_e = 4/(2 det-) = 16/7, c_mu = 3/(2 det+) = 4/3, c_tau = 4 det-/3 = 7/6, product = 4/det+ = 32/9", Simplify[4/(2 detm)] == 16/7 && Simplify[3/(2 detp)] == 4/3 && Simplify[4 detm/3] == 7/6 && Simplify[4/detp] == 32/9 && Abs[m0[[2, 2]]] == 1/2]; elems = <|Expand[IdentityMatrix[3]] -> True|>; frontier = {IdentityMatrix[3]}; While[frontier =!= {}, newE = {}; Do[Module[{xg = Expand[g . e]}, If[! KeyExistsQ[elems, xg], elems[xg] = True; AppendTo[newE, xg]]], {e, frontier}, {g, {usym, m0, -IdentityMatrix[3]}}]; frontier = newE]; checkExact["v118 sheet-extended group: <U, M0, -1> has order 48 = Omega_adm = 3 x 16 = |S4 x Z2|", Length[elems] == 48 && 3*16 == 48]; ]; (* ---- (v119) second review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L749)
- [(* ---- (v105) residual inventory ---- *) checkExact["v105 one-constant inventory (exact items): Koide branch -2/3; gap base (2/3)^6; Nariai bound 2/3; branch separation 2/3; canonical amplitude/frequency 2/3; curvature (2/3)^3", ((3 (-2/3) + 2) == 0) && ((2/3)^6 == 64/729) && ((4/3 - (2/3) Cos[0]) == 2/3) && ((1/3) - (-1/3) == 2/3) && (Coefficient[4/3 - (2/3) Cos[2 ps/3], Cos[2 ps/3]] == -2/3) && (((2/3)^3) == 8/27)]; checkExact["v105 anchor triptych: chi_a = (t-1)^2(t-2); Nariai = (t-1)^2(t+2) = (t-1) x clock (lam-1)(lam+2)", (Expand[(t - 1)^2 (t - 2)] == t^3 - 4 t^2 + 5 t - 2) && (Expand[(t - 1)^2 (t + 2) - (t - 1) (t^2 + t - 2)] === 0)]; check["v105 relocation: eps = (8/24Pi) * 7.125e-121 = 7.56e-122 (deficient ~121.5 orders vs Delta)", (8/(24 Pi)) 7.125329526706`20 10^-121 / (6 Log[3/2]), 10^-121.5076, 10^-3]; checkExact["v105 residual table: exactly FIVE structural objects + 2 irreducibles (typing contract)", Length[{"R1clock", "R2holc8", "R3seamEH", "R4H2", "R5Qreal"}] == 5]; (* ---- (v106) review validation ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L435)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## Research Contract — GRAV.WEINBERG.WITTEN.01 (Weinberg–Witten firewall before any spin-2 marker move)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:14381-14396](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L14381) · `section:8a4e51786c63605a14f0` · section

Typing. A research contract \ (ledger row GRAV.WEINBERG.WITTEN.01), registered 2026-08-30 from review wave 6. Child of TOE gate T7; cross-link GRAV.SPIN2.EMERGENCE.01 (listed here, not back — that would cycle). Demand. The microscopic Hamiltonian family must not possess a fundamental Lorentz-covariant local conserved [formula in source] ; Lorentz symmetry, diffeomorphism Ward identities and the spin-2 mode must emerg

Explicit source references:

- [GRAV.WEINBERG.WITTEN.01](../../../../verification/status_ledger.csv#L770) · explicit_claim_identifier · original status at linked ledger row
- [GRAV.SPIN2.EMERGENCE.01](../../../../verification/status_ledger.csv#L762) · explicit_claim_identifier · original status at linked ledger row

## Externalization Contract — SEAM.EQUIV.01 (the seam scaling-limit theorem, packaged for external specialists)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:14397-14558](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L14397) · `section:fd15b9954fc0175fba1b` · section

Typing. This section is a hand-off document: it packages the one remaining seam obligation as a self-contained problem statement for an outside specialist in conformal nets / vertex operator algebras / algebraic QFT. It documents, it does not close: the ledger row SEAM.EQUIV.01 stays \ (its conditional route SEAM.EQUIV.MMST.01 is closed modulo cited theorems; the unconditional parent is the target below). Nothing in 

Explicit source references:

- [verification/v217_marks_emergence_scan.py](../../../../verification/v217_marks_emergence_scan.py#L1) · explicit_script_identifier
- [verification/v377_seam_s3_e8character.py](../../../../verification/v377_seam_s3_e8character.py#L1) · explicit_file_citation
- [verification/v125_glue_qsystem.py](../../../../verification/v125_glue_qsystem.py#L1) · explicit_script_identifier
- [verification/v336_continuum_limit.py](../../../../verification/v336_continuum_limit.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamEquivChain.mueger_klm_holomorphy](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L58) · explicit_lean_symbol
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation
- [verification/v351_continuum_realisation_sharpened.py](../../../../verification/v351_continuum_realisation_sharpened.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamEquivChain.kitaev_invertibility](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L52) · explicit_lean_symbol
- [experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean#L1) · explicit_file_citation
- [verification/v994_mmst_criteria_battery.py](../../../../verification/v994_mmst_criteria_battery.py#L1) · explicit_file_citation
- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/v378_seam_s3_modular.py](../../../../verification/v378_seam_s3_modular.py#L1) · explicit_script_identifier
- [verification/v376_seam_s3_centralcharge.py](../../../../verification/v376_seam_s3_centralcharge.py#L1) · explicit_script_identifier
- [verification/v281_holomorphy_modular_data.py](../../../../verification/v281_holomorphy_modular_data.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamScalingLimit.mmst_scaling_limit](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L76) · explicit_lean_symbol
- [verification/v356_continuum_mmst_applicability.py](../../../../verification/v356_continuum_mmst_applicability.py#L1) · explicit_script_identifier
- [SEAM.EQUIV.MMST.01](../../../../verification/status_ledger.csv#L583) · explicit_claim_identifier · original status at linked ledger row
- [TfptCarrier.SeamScalingLimit.mmst_range](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L53) · explicit_lean_symbol
- [DIMENSION.UPLIFT.FIREWALL.01](../../../../verification/status_ledger.csv#L739) · explicit_claim_identifier · original status at linked ledger row
- [TfptCarrier.SeamScalingLimit.collar_gapped](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L72) · explicit_lean_symbol
- [TfptCarrier.SeamScalingLimit.ChiralCFT_c8](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L68) · explicit_lean_symbol
- [verification/v160_seam_gaussianity_from_pf.py](../../../../verification/v160_seam_gaussianity_from_pf.py#L1) · explicit_script_identifier
- [verification/v367_seam_s3_lattice.py](../../../../verification/v367_seam_s3_lattice.py#L1) · explicit_file_citation
- [verification/v286_seam_equivalence_contract.py](../../../../verification/v286_seam_equivalence_contract.py#L1) · explicit_script_identifier
- [verification/v469_seam_crossedproduct_route.py](../../../../verification/v469_seam_crossedproduct_route.py#L1) · explicit_script_identifier
- [verification/v301_route_a_invertible.py](../../../../verification/v301_route_a_invertible.py#L1) · explicit_script_identifier
- [verification/v368_seam_s3_inflow.py](../../../../verification/v368_seam_s3_inflow.py#L1) · explicit_file_citation
- [verification/v302_seam_gap.py](../../../../verification/v302_seam_gap.py#L1) · explicit_script_identifier
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1) · explicit_file_citation
- [verification/v461_seam_strict_locality.py](../../../../verification/v461_seam_strict_locality.py#L1) · explicit_script_identifier
- [verification/v154_simple_current_theorem.py](../../../../verification/v154_simple_current_theorem.py#L1) · explicit_script_identifier
- [verification/v366_mmst_seam_collar.py](../../../../verification/v366_mmst_seam_collar.py#L1) · explicit_script_identifier
- [verification/v155_quasifree_boundary.py](../../../../verification/v155_quasifree_boundary.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamScalingLimit.adamo_holomorphic_e8](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L87) · explicit_lean_symbol
- [SEAM.EQUIV.01](../../../../verification/status_ledger.csv#L381) · explicit_claim_identifier · original status at linked ledger row
- [TfptCarrier.SeamScalingLimit.holomorphic_discriminator](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L58) · explicit_lean_symbol
- [verification/v379_seam_s3_rp.py](../../../../verification/v379_seam_s3_rp.py#L1) · explicit_script_identifier
- [verification/v113_quasifree_kernel.py](../../../../verification/v113_quasifree_kernel.py#L1) · explicit_script_identifier
- [TfptCarrier.SeamEquivChain.conway_sloane_e8](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L61) · explicit_lean_symbol
- [SEAM.BULK4D.RECON.01](../../../../verification/status_ledger.csv#L740) · explicit_claim_identifier · original status at linked ledger row
- [FORM.SEAM.MMST.01](../../../../verification/status_ledger.csv#L92) · explicit_claim_identifier · original status at linked ledger row
- [verification/v973_seam_route_narrowing.py](../../../../verification/v973_seam_route_narrowing.py#L1) · explicit_file_citation
- [verification/v216_marks_gauss_bonnet.py](../../../../verification/v216_marks_gauss_bonnet.py#L1) · explicit_script_identifier
- [verification/v1016_state_gap_batteries.py](../../../../verification/v1016_state_gap_batteries.py#L1) · explicit_file_citation
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ==== v351 SEAM.EQUIV.CONTINUUM.02: the order-4 clock + Coxeter-match pin E8 over SO(16) ==== *) Module[{cE8, cD8}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; checkExact["v351 SEAM.EQUIV.CONTINUUM.02: the c=8 which-net ambiguity (E8 det 1 vs SO(16)=D8 det 4) is RESOLVED by the seam's ORDER-4 mu4 clock -- index-4 extension of D5(+)A3 = E8 (full mu4 condensation 16->4->1), index-2 = SO(16) (partial Z2 16->4); the order (4 not 2) selects E8. The bootstrap agrees: h(E8)=30 max prime 5=g_car, h(D8)=14 max prime 7, so SO(16) fails the Coxeter-match. The residual of SEAM.EQUIV.01 is then PURELY the chiral-edge existence, not which-net", Det[cE8] == 1 && Det[cD8] == 4 && Max[FactorInteger[30][[All,1]]] == 5 && Max[FactorInteger[14][[All,1]]] == 7]; ]; (* ==== v352 TFPT.IRREDUCIBLE.01: both axioms bootstrap-forced; irreducibles = framework + pi ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2334)
- [(* v469 (ii): KLM mu-index + the 16-fold-way pin *) muI2 = 4/2^2; muI4 = 16/4^2; nu = 16*1; cminus = nu/2; checkExact["v469 SEAM.EQUIV.CROSSEDPRODUCT.01 (ii): KLM mu-index -- both routes land holomorphic, mu = 4/2^2 = 1 (index-2 SO(16)_1 route) and mu = 16/4^2 = 1 (index-4 mu4 route); and the Kitaev 16-fold-way pin nu = 16 x |C| = 16 = 0 mod 16 with c_- = nu/2 = 8 = g_car + N_fam = rank E8 (the class-D phase whose edge is the purely bosonic (E8)_1 state)", muI2 == 1 && muI4 == 1 && Mod[nu, 16] == 0 && cminus == 8 && cminus == 5 + 3]; ]; (* ==== v470 round: the alpha^3 level / embedding-index rigidity -- the exact k_Y = 5/3 arithmetic (tr Y^2 / tr T3^2 over the 5bar), the b1 conversion (3/5)(41/6) = 41/10, and the carrier decomposition 41/6 = 20/3 + 1/6; mirrors v470 (the FHS Chern and the alpha^-1 root re-verification are numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2937)
- [(* ==== v501 round: CELEST.WP5D.01 -- WP5d-alpha of CELEST.SEAM.01, "the two-interval index from the lattice" (the local-net question, alpha stage). Exact content mirrored: (i) the Cartan determinants det(D5) = det(A3) = 4, product 16 = mu(carrier), det(D8) = 4 = mu(SO(16)_1), det(E8) = 1 = mu((E8)_1) (v378 replication, explicit matrices); (ii) the KLM/Longo-Rehren quotients mu/|L|^2 -- 16/4^2 = 1 (one-step mu4 glue, |L| = |mu4| = 4) and 16/2^2 = 4 -> 4/2^2 = 1 (via SO(16)_1), both routes exact; (iii) the Sigma d_i^2 cross-checks (Ising 1+1+2 = 4, SO(16)_1 four abelian sectors = 4, (E8)_1 one sector = 1) + the index reading arithmetic ([F:F_even] = e^(ln 2) = 2, mu_gauged = e^(2 ln 2) = 4, per-layer gauging 16 ln 2 = ln 2^16, budget ln 4 = ln mu(SO(16)_1)); (iv) the 16-fold-way condensability theta_v = e^(2 pi i nu/16) = 1 EXACTLY at nu = 2 c_- = 16 (c_- = 8 = g_car + N_fam, 16 layers = 2^(g_car - 1)) vs the rivals nu = 1, 2, 8. The lattice curves (Peschel covariance, Renyi-2 offsets, the ln 2 plateau, the duality-asymmetry witness, all ED validations) are numerical and stay Python-only (v501 S0-S4, S6). Mirrors v501. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L3830)
- [(* v463 (ii): the (E8)_1 tower = E4/eta^8 coefficients {1,248,4124,34752,213126} *) inv8 = Series[Product[(1 - q^n)^-8, {n, 1, 6}], {q, 0, 5}]; chiSer = Series[(1 + 240 Sum[DivisorSigma[3, n] q^n, {n, 1, 6}]) inv8, {q, 0, 5}]; tower = CoefficientList[Normal[chiSer], q][[1 ;; 5]]; checkExact["v463 SEAM.EQUIV.UNIQ.01 (ii): the holomorphic c=8 partition function is the unique j^{1/3}=E4/eta^8, whose q-coefficients are the (E8)_1 tower {1,248,4124,34752,213126} -- the q^1=248 is the forced weight-1 dimension (Dong-Mason/Schellekens: the holomorphic c=8 VOA is unique = V_{E8})", tower == {1, 248, 4124, 34752, 213126}]; ]; (* ==== v469 round: the net-level crossed-product certification -- the LR locality integers (h_s(SO(16)_1) = 16/16 = 1 in Z; the mu4 glue h(J^k) = {1,1,1} all integer), the KLM mu-index arithmetic (4/2^2 = 1 and 16/4^2 = 1, both holomorphic) and the Kitaev 16-fold-way pin (nu = 16 x |C| = 16 = 0 mod 16, c_- = nu/2 = 8 = g_car+N_fam); mirrors v469 (the FHS Chern itself is numerical, Python-only). ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2916)
- [(* ---- (v113) quasi-free kernel ---- *) Module[{jwOps, g = 5, a, ad, cs, vac, vev, m2, amat, pol, k10, pf, ok4, ok6, a16, p16}, jwOps[gg_] := Module[{eye = IdentityMatrix[2], zee = {{1, 0}, {0, -1}}, am = {{0, 1}, {0, 0}}}, Table[KroneckerProduct @@ Join[ConstantArray[zee, i - 1], {am}, ConstantArray[eye, gg - i]], {i, gg}]]; checkExact["v113 Majorana bookkeeping: c(D5)1 = 45/9 = 5 = g_car, c(A3)1 = 15/5 = 3 = N_fam, c(SO16)1 = 8, c(E8)1 = 248/31 = 8; carrier = 10+6 = 16 free Majoranas; tower index 2x2 = 4 = |mu4|", 45/9 == 5 && 15/5 == 3 && 120/15 == 8 && 248/31 == 8 && 10 + 6 == 16 && Sqrt[16/4] Sqrt[4/1] == 4]; a = jwOps[g]; ad = Transpose /@ a; cs = Flatten[Table[{a[[i]] + ad[[i]], I (ad[[i]] - a[[i]])}, {i, g}], 1]; vac = UnitVector[2^g, 1]; vev[ops_] := vac . (Dot @@ ops) . vac; m2 = Table[vev[{cs[[j]], cs[[k]]}], {j, 10}, {k, 10}]; amat = (m2 - IdentityMatrix[10])/I; pol = (IdentityMatrix[10] + I amat)/2; checkExact["v113 kernel = Calderon involution of rank g: M = I+iA, A integer antisym, A^2 = -I, P = M/2 projection of rank 5 = g_car, eps = iA involution", amat == -Transpose[amat] && AllTrue[Flatten[amat], IntegerQ] && amat . amat == -IdentityMatrix[10] && pol . pol == pol && MatrixRank[pol] == 5 && (I amat) . (I amat) == IdentityMatrix[10]]; k10 = Table[If[x < y, vev[{cs[[x]], cs[[y]]}], 0], {x, 10}, {y, 10}]; pf[idx_] := If[idx === {}, 1, Sum[(-1)^(t - 1) k10[[idx[[1]], idx[[t + 1]]]] pf[Delete[Rest[idx], t]], {t, Length[idx] - 1}]]; ok4 = AllTrue[Subsets[Range[10], {4}], (vev[cs[[#]]] == pf[#]) &]; ok6 = AllTrue[Subsets[Range[10], {6}], (vev[cs[[#]]] == pf[#]) &]; checkExact["v113 Wick/Pfaffian: all 210 vacuum 4-point AND all 210 6-point functions equal the Pfaffian of the single 2-point kernel", ok4 && ok6]; checkExact["v113 one kernel <=> one state: joint annihilator kernel exactly 1-dimensional", 2^g - MatrixRank[Join @@ a] == 1]; a16 = SparseArray[Join[Table[{2 i - 1, 2 i} -> 1, {i, 8}], Table[{2 i, 2 i - 1} -> -1, {i, 8}]], {16, 16}] // Normal; p16 = (IdentityMatrix[16] + I a16)/2; checkExact["v113 seam level: 16-Majorana kernel rank 8 = rank E8 = c (the central charge is the rank of the one kernel)", p16 . p16 == p16 && MatrixRank[p16] == 8]; ]; (* ---- (v114) torsion normal form + delta = 1/2 theorem ---- The [N] branch census (scipy Nelder-Mead sampling of the D4-fixed flat cusp locus) is Python-only by convention; the exact statements are mirrored here. *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L607)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean#L1)
- [(* ---- (v216) QGEO.MARKS.03: the four marks from Gauss-Bonnet + Euclidean-orbifold uniqueness ---- *) Module[{orbs, gb, nn}, orbs = {{2, 3, 6}, {2, 4, 4}, {3, 3, 3}, {2, 2, 2, 2}}; gb = nn /. Solve[nn (2 Pi - Pi) == 2 Pi 2, nn][[1]]; (* Z2 deficit pi, chi(S^2)=2 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1740)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean#L1)
- [(* v461: tied obstruction integers + the reflection forcing (strict-local => C=-C => C=0) *) cMinus = 2^(gcar - 1)*1/2; (* 16*|C|/2 = 8, |C|=1 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2881)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean#L1)
- [(* ---- (v994) SEAM.EQUIV.MMST.01 C3: Theta_E8 / eta^8 = {1,248,4124,34752} ---- Python-only: C1 entropy, C2 QWZ spectrum, C4 two-point numeric, C5 sector recombination beyond det, C6 cited, C7 open, GSO/N=8 must-fail combinatorics. *)](../../../../verification/wolfram/tfpt_readouts.wl#L680)
- [(* v469 (i): the LR locality integers of both extension routes *) hs = 16/16; (* so(N)_1 spinor weight N/16, N = 16 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2930)
- [(* ---- (v124) resummed clock ---- *) Module[{lams, rate, ser}, lams = Table[((3 - n)/3)^6, {n, 0, 2}]; checkExact["v124 spectrum reads (1-n/3)^6: eigenvalues {1, (2/3)^6, (1/3)^6}", lams == {1, (2/3)^6, (1/3)^6}]; rate[n_] := -6 Log[(3 - n)/3]; checkExact["v124 closed-form clock: rates {0, Delta, 6 ln 3}; bend rate(2)/rate(1) = log_{3/2}3", Simplify[rate[1] - 6 Log[3/2]] === 0 && Simplify[rate[2] - 6 Log[3]] === 0 && FullSimplify[rate[2]/rate[1] - Log[3]/Log[3/2]] === 0]; ser = Normal[Series[-6 Log[1 - x/3], {x, 0, 3}]]; checkExact["v124 linearisation carries the sheet: series 2x + x^2/3 + 2x^3/27 (slope |Z2| = 2); pole at n = N_fam = 3", Expand[ser - (2 x + x^2/3 + 2 x^3/27)] === 0 && Limit[-6 Log[1 - x/3], x -> 3, Direction -> "FromBelow"] === Infinity]; ]; (* ---- (v125) glue Q-system ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L856)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean#L1)
- [(* ==== v281: anyon-condensation tower + Gauss-Milgram (QGAMB.MODULAR.01) ==== *) Module[{cE8, cD8, cD5, cA3, dE8, dD8, dcar, gm}, cE8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,-1},{0,0,0,0,-1,2,-1,0},{0,0,0,0,0,-1,2,0},{0,0,0,0,-1,0,0,2}}; cD8 = {{2,-1,0,0,0,0,0,0},{-1,2,-1,0,0,0,0,0},{0,-1,2,-1,0,0,0,0},{0,0,-1,2,-1,0,0,0}, {0,0,0,-1,2,-1,0,0},{0,0,0,0,-1,2,-1,-1},{0,0,0,0,0,-1,2,0},{0,0,0,0,0,-1,0,2}}; cD5 = {{2,-1,0,0,0},{-1,2,-1,0,0},{0,-1,2,-1,-1},{0,0,-1,2,0},{0,0,-1,0,2}}; cA3 = {{2,-1,0},{-1,2,-1},{0,-1,2}}; dE8 = Det[cE8]; dD8 = Det[cD8]; dcar = Det[cD5] Det[cA3]; gm = Sum[Exp[2 Pi I h], {h, {0, 1/2, 1, 1}}]; (* D8 anyons 1,v,s,c *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2153)
- [(* ---- (v154) Simple-Current Extension Theorem ---- *) Module[{Lord = 4, cB, muA, muB}, cB = 5 + 3; muA = 4*4; muB = muA/Lord^2; checkExact["v154 Simple-Current Extension: |L|=4=|mu4| (isotropic q(k(1,1))=k^2 in Z); c(B)=5+3=8; mu(B)=mu(A)/|L|^2=16/16=1 => holomorphic => B=(E8)1 (unique even-unimodular rank-8; SO(16)1 mu=4 excluded)", AllTrue[Range[0, 3], IntegerQ[5 #^2/8 + 3 #^2/8] &] && Lord == 4 && cB == 8 && muA == 16 && muB == 1 && 4 != muB]; ]; (* ---- (v156) seam-net construction: DtN = |k| + the (E8)_1 character ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1380)
- [(* ==== v461/v462 round: the Kapustin-Fidkowski strict-locality obstruction (integer logic; the Wilson-loop winding/Chern themselves are numerical, Python-only) and the 128-spinor extension at character level -- the Jacobi/E8 theta identity theta2^8+theta3^8+theta4^8=2E4 (so the (E8)_1 character is the SO(16)_1 vacuum+spinor sum) and the 120+128=248 sector + finite 16-Majorana Fock counts; mirrors v461/v462. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2874)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean#L1)

## Externalization Contract — PRIME.RESIDUE.EXTERNAL.01 (the prime-front terminal residue, packaged for external specialists)

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:14783-15054](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L14783) · `section:3fda22a74bef961db1d2` · section

Typing. The third hand-off document: the terminal open statements of the prime-front programme (diary and status record: tfpt_prime_front), packaged self-containedly for outside specialists in analytic number theory — large sieve, sampling and frame theory, de Branges spaces, explicit-formula methods. It documents, it does not close: the contract identifier names this document, not a ledger row; every prime-front led

Explicit source references:

- [verification/run_all.py](../../../../verification/run_all.py#L1) · explicit_file_citation
- [verification/status_ledger.csv](../../../../verification/status_ledger.csv#L1) · explicit_file_citation

## Certifiability and recommended order

[experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex:15055-15361](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/tfpt_research_contracts.tex#L15055) · `section:f0ac30137703825661c6` · section

@Ylc@ Building block & Machine & Hardness \\ [formula in source] enumeration ( [formula in source] ) & Lean / Python / Wolfram & easy ( done) \\ [formula in source] fixed-locus polynomial ( [formula in source] ) & Sage / Mathematica & medium \\ selector uniqueness ( [formula in source] ) & interval arithmetic & medium \\ SNF, determinants, spectra & Lean & easy–medium \\ principal-symbol ellipticity (G1) & xAct / Cad

Explicit source references:

- [verification/v139_selector_triangle.py](../../../../verification/v139_selector_triangle.py#L1) · explicit_script_identifier
- [verification/v777_ftransfer_clock_jets.py](../../../../verification/v777_ftransfer_clock_jets.py#L1) · explicit_file_citation
- [verification/v93_koide_relaxation_toy.py](../../../../verification/v93_koide_relaxation_toy.py#L1) · explicit_script_identifier
- [verification/v792_ftransfer_kms_coset.py](../../../../verification/v792_ftransfer_kms_coset.py#L1) · explicit_file_citation
- [verification/v136_dual_normal_selector.py](../../../../verification/v136_dual_normal_selector.py#L1) · explicit_script_identifier
- [FTRANSFER.KMSCOSET.01](../../../../verification/status_ledger.csv#L688) · explicit_claim_identifier · original status at linked ledger row
- [verification/v240_gns_os_reconstruction.py](../../../../verification/v240_gns_os_reconstruction.py#L1) · explicit_script_identifier
- [verification/v303_ftransfer_dynamics.py](../../../../verification/v303_ftransfer_dynamics.py#L1) · explicit_file_citation
- [FR.DYNAMICS.01](../../../../verification/status_ledger.csv#L396) · explicit_claim_identifier · original status at linked ledger row
- [verification/v183_koide_f_corner_transfer.py](../../../../verification/v183_koide_f_corner_transfer.py#L1) · explicit_file_citation
- [verification/v425_dyn_transfer_universal.py](../../../../verification/v425_dyn_transfer_universal.py#L1) · explicit_file_citation
- [verification/v723_phys_modular_clock.py](../../../../verification/v723_phys_modular_clock.py#L1) · explicit_file_citation
- [FTRANSFER.STT.01](../../../../verification/status_ledger.csv#L668) · explicit_claim_identifier · original status at linked ledger row
- [verification/v724_phys_t3b_modular_flows.py](../../../../verification/v724_phys_t3b_modular_flows.py#L1) · explicit_script_identifier
- [FTRANSFER.CLOCKS.01](../../../../verification/status_ledger.csv#L676) · explicit_claim_identifier · original status at linked ledger row
- [verification/v383_dynamics_universal.py](../../../../verification/v383_dynamics_universal.py#L1) · explicit_script_identifier
- [QGEO.SYM.01](../../../../verification/status_ledger.csv#L261) · explicit_claim_identifier · original status at linked ledger row
- [verification/v566_parabolic_anchor_selfcode.py](../../../../verification/v566_parabolic_anchor_selfcode.py#L1) · explicit_file_citation
- [verification/v54_seam_horizon_keystones.py](../../../../verification/v54_seam_horizon_keystones.py#L1) · explicit_script_identifier
- [DYN.UNITARY.DILATION.01](../../../../verification/status_ledger.csv#L742) · explicit_claim_identifier · original status at linked ledger row
- [verification/v82_koide_attractor_splitting.py](../../../../verification/v82_koide_attractor_splitting.py#L1) · explicit_script_identifier
- [verification/v187_ftransfer_laws.py](../../../../verification/v187_ftransfer_laws.py#L1) · explicit_file_citation
- [DYN.TRANSFER.UNIVERSAL.01](../../../../verification/status_ledger.csv#L492) · explicit_claim_identifier · original status at linked ledger row
- [verification/v575_cr_continuous_uniflow.py](../../../../verification/v575_cr_continuous_uniflow.py#L1) · explicit_file_citation
- [verification/v533_ftransfer_disc7_norm.py](../../../../verification/v533_ftransfer_disc7_norm.py#L1) · explicit_script_identifier
- [CONTRACT.F.01](../../../../verification/status_ledger.csv#L302) · explicit_claim_identifier · original status at linked ledger row
- [DYN.MARKOV.EMBED.01](../../../../verification/status_ledger.csv#L741) · explicit_claim_identifier · original status at linked ledger row
- [verification/v971_markov_embedding_generator.py](../../../../verification/v971_markov_embedding_generator.py#L1) · explicit_file_citation
- [verification/v153_no_unit_theorem.py](../../../../verification/v153_no_unit_theorem.py#L1) · explicit_script_identifier
- [verification/v320_galois_cp_relation.py](../../../../verification/v320_galois_cp_relation.py#L1) · explicit_script_identifier
- [verification/v238_modular_lindblad_dynamics.py](../../../../verification/v238_modular_lindblad_dynamics.py#L1) · explicit_script_identifier
- [verification/v571_cr_discrete_corners.py](../../../../verification/v571_cr_discrete_corners.py#L1) · explicit_file_citation
- [verification/v632_ftransfer_pgl2.py](../../../../verification/v632_ftransfer_pgl2.py#L1) · explicit_script_identifier
- [verification/v578_native_jets.py](../../../../verification/v578_native_jets.py#L1) · explicit_file_citation
- [verification/v213_ftransfer_functor.py](../../../../verification/v213_ftransfer_functor.py#L1) · explicit_file_citation
- [FTRANSFER.COCYCLE.01](../../../../verification/status_ledger.csv#L669) · explicit_claim_identifier · original status at linked ledger row
- [verification/v184_etaB_anchored_boltzmann.py](../../../../verification/v184_etaB_anchored_boltzmann.py#L1) · explicit_file_citation
- [verification/v185_axion_relic_solver.py](../../../../verification/v185_axion_relic_solver.py#L1) · explicit_file_citation
- [verification/v99_koide_flow_time.py](../../../../verification/v99_koide_flow_time.py#L1) · explicit_script_identifier
- [verification/v224_diamond_ftransfer_path.py](../../../../verification/v224_diamond_ftransfer_path.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *) checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)", gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 && Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}]; checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+", Module[{rs = Total /@ K}, gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 && (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]]; checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)", Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] && {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}]; (* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L222)
- [(* ---- (v93) Koide relaxation toy ---- *) FK[q_] := 2 (569 q - 3325)/(665 q - 3517); checkExact["v93 F fixes branch points; F'(2)=(2/3)^6, F'(5)=(3/2)^6", (FK[2] == 2) && (FK[5] == 5) && (Simplify[FK'[2]] == (2/3)^6) && (Simplify[FK'[5]] == (3/2)^6)]; Qsrc = Module[{me = (16/7) phi0^5, mm = (4/3) phi0^3, mt = (7/6) phi0^2}, (me + mm + mt)/(Sqrt[me] + Sqrt[mm] + Sqrt[mt])^2]; check["v93 Q_src = 0.6644638161 from the exact ladder", Qsrc, 0.664463816123`12, 10^-10]; checkExact["v93 basin lemma: Q in [1/3,1] -> q = 3Q in [1,3]: attractor 2 in, repeller 5 out", (3 (1/3) == 1) && (3*1 == 3) && (1 < 2 < 3) && ! (1 < 5 < 3)]; rhoOf[q_] := (q - 2)/(5 - q); check["v93 rho_src = -phi0/24 to 0.8% (v25 conjecture in attractor coordinates)", rhoOf[3 Qsrc]/(-phi0/24), 0.992105906542`12, 10^-8]; (* ---- (v94) sheet diamond & winding line ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L165)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean#L1)
- [(* v230 center budget (7,11,13) = three local norms *) RRm = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; QQm = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; Cc2 = RRm + QQm.DiagonalMatrix[{1, 0, 0}]; checkExact["v230 CENTER.NORM.01: C=R+Q diag(1,0,0) row sums (7,11,13) = " <> "(N_Z[omega](3+2w)=7 hex, C(4,0)+C(4,1)+C(4,2)=11 QBL Fock, N_Z[i](3+2i)=13 square) " <> "= (hex norm, boundary Fock count, square norm)", Total /@ Cc2 == {7, 11, 13} && {Nw[3, 2], Binomial[4, 0] + Binomial[4, 1] + Binomial[4, 2], Ni[3, 2]} == {7, 11, 13}]; (* v224 diamond F_transfer path: sheet axis curved, winding axis flat, Plucker steps *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1838)
- [(* ---- (v136) dual-normal selector ---- *) Module[{dv, nv, av, rmat, qmat, kmat, sols, a0, v0, sigma, adjA0, grp, gens, reals}, dv = {-1/2, -1/2, 1}; nv = {5, -9, 6}; av = {1, 1, 2}; rmat = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; qmat = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; kmat = rmat + qmat . DiagonalMatrix[{1, -1, -1}]; sols = Table[Select[Tuples[Range[0, 5], 3], dv . # == av[[j]] && nv . # == 8 Boole[j == 1] &], {j, 3}]; checkExact["v136 column normal form: d.c_j = a_j, n.c_j = 8 delta_1j; kernel (6,8,7); each column UNIQUE in {0..5}^3 (1 of 216)", (dv . #) & /@ Transpose[rmat] == av && (nv . #) & /@ Transpose[rmat] == {8, 0, 0} && 7 First[NullSpace[{dv, nv}]] == {6, 8, 7} && Length /@ sols == {1, 1, 1} && (First /@ sols) == Transpose[rmat]]; checkExact["v136 honesty: K not pinned by (d,n) (d.K = (1,1/2,1), n.K = (14,1,-6)); det K = 4 via the diamond", dv . kmat == {1, 1/2, 1} && nv . kmat == {14, 1, -6} && Det[kmat] == 4]; a0 = {{1/2, Sqrt[2]/6, 0}, {Sqrt[2]/6, 1/4, Sqrt[5]/12}, {0, Sqrt[5]/12, 1/4}}; v0 = First[NullSpace[a0]]; v0 = v0/v0[[2]] 3; sigma = {2, -9, 5}; adjA0 = Transpose[Table[(-1)^(i + j) Det[Drop[a0, {i}, {j}]], {i, 3}, {j, 3}]]; checkExact["v136 spectral normal: A0* zero mode signed squares = -(2,-9,5); ||v||^2 = 16/9; adj(A0*)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1050)
- [(* ---- (v99) Koide flow time ---- *) DeltaGap = 6 Log[3/2]; rhoK[q_] := (q - 2)/(5 - q); qOfRho[r_] := (2 + 5 r)/(1 + r); checkExact["v99 canonical generator: time-1 map of the rho-scaling flow IS the v82 Moebius F (exact symbolic identity)", Simplify[FK[q] - qOfRho[(2/3)^6 rhoK[q]]] === 0]; checkExact["v99 e^{-Delta} = (2/3)^6 exactly (the gap is the multiplier)", Simplify[Exp[-DeltaGap] - (2/3)^6] === 0]; koideQ[a_, b_, c_] := (a + b + c)/(Sqrt[a] + Sqrt[b] + Sqrt[c])^2; mE = 0.51099895069`20; mMU = 105.6583755`20; (* PDG 2024 pole masses, MeV *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L303)
- [(* ==== v313-v320: the cyclotomic / Galois arithmetic arc (exact) ==== *) Module[{edges, cAff, x, units, maxord, z6, z30, gauss}, (* v313 GOLD.ATOMS.01 -- the golden ratio is the g_car=5 spectral signature *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2182)
- [(* ---- (v183) Koide 53/54 = a^T(R+Q)1 / (2 1^T R a): missing Sheet-Diamond corner ---- *) Module[{R, Q, K, L, one, a, F, f, cubic, corner, ratio, detBF, others}, R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}}; Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}; K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}}; L = {{7, 3, 0}, {7, 5, 2}, {8, 5, 3}}; one = {1, 1, 1}; a = {1, 1, 2}; F = R + Q; f[m_, u_, v_] := u . m . v; cubic = f[R, one, a]; (* 1^T R a = 27 *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1546)
- [(* ---- (v138) VW firewall ---- *) checkExact["v138 external datum + edge match: 22/45 - 8/3 = -98/45 (VW hep-th/0003081 / arXiv:2506.02142); edge = -8/3 = 2 x (-4/3) = two copies of the v133 reduced seam budget; diff -38/45, 38 = 2*19, no atom", 22/45 - 8/3 == -98/45 && -8/3 == 2 (-4/3) && -98/45 + 60/45 == -38/45 && FactorInteger[38] == {{2, 1}, {19, 1}} && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 98/45] && ! MemberQ[{2/3, 4/3, 1/3, 8/9, 2/9, 16/9, 13/144}, 38/45]]; (* ---- (v139) selector triangle ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1102)
- [(* ==== v533 round: FTR.DISC7.NORM.01 -- the disc -7 norm line. Exact mirrors: norm identity, translation, norms (2,4,14,32), constant discriminant -7, vertex, negative controls. ==== *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L8372)
- [(* ---- (v152) R3 normalisation = the anchor ---- *) Module[{c3, k, lnratio, dlogdet}, c3 = 1/(8 Pi); k = c3/2; lnratio = Simplify[12 Pi k]; dlogdet = -D[(mm/muu)^(-2 ss), ss] /. ss -> 0; checkExact["v152 R3 normalisation = anchor: Delta log det' = 2 C ln(m/mu) (scale-ambiguous ln m; only m/mu physical); k = c3/2 <=> ln(m/mu) = 3/4 => m/mu = e^{3/4}; 1/(16 pi G)|_{G=1} = c3/2 (induced 1/G = the v68 anchor); audit: 3/4 = q(A3) is the target value, not a derivation", Simplify[dlogdet - 2 Log[mm/muu]] === 0 && k == 1/(16 Pi) && lnratio == 3/4 && Simplify[1/(16 Pi) - c3/2] === 0 && 3/4 == 3/4]; ]; (* ---- (v153) No-Unit Theorem ---- *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L1355)
- [(* v318 ARITH.CAPSTONE.01 -- the magnitude seed reduces to a pure pi-function *) checkExact["v318 ARITH.CAPSTONE.01: phi0 = (|mu4|/Nfam) c3 + Omega_adm c3^4 = (4/3)c3 + 48 c3^4 = 1/(6 Pi) + 3/(256 Pi^4) (a pure function of Pi => 0 dimensionless free parameters)", Simplify[(4/3) c3 + 48 c3^4 - (1/(6 Pi) + 3/(256 Pi^4))] == 0 && Simplify[(4/3) c3 + 48 c3^4 - phi0] == 0]; (* v320 GALOIS.CP.PREDICT.01 -- the falsifiable CP lock *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2213)

## Warum die Paarenergien unter dem Tetramer stillstehen

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/06_zeit_echo.tex:16-20](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/06_zeit_echo.tex#L16) · `section:35bfac0bdfd197b60694` · section

Der vollständige gleichgewichtete Tetramer-Hamiltonoperator ist eine zentrale Transpositionssumme. Deshalb kommutiert er mit jedem [formula in source] und jedem [formula in source] . Die Paarenergien ändern sich unter seiner freien Entwicklung nicht. Eine Tabelle, die nacheinander einen lokalen [formula in source] -Tick anwendet, ist somit kein Beweis, dass genau diese Anzeige unter [formula in source] von selbst läu

## Ressourcen und Beweisgrenze der Originalschaltung

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/06_zeit_echo.tex:211-218](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/06_zeit_echo.tex#L211) · `section:59617a673609f0732add` · section

Y r Ressource nach S02& Anzahl\\ Systemqubits&8\ , wiederverwendet&10\ ätze&2\ reservierte Qubits&20\ Erfolgsbits beider Filter&12\ -Gatter&574\ CNOT vor Toffoliauflösung&382\ &26\ - [formula in source] / Pauli- [formula in source] &276 / 26\\T/T^ [formula in source] T-Varianten waren durch lokale Matrixidentität und Ersetzung zertifiziert, nicht zusätzlich als komplette komplexe 20-Qubit-Vektoren simuliert.

## Die Naht braucht mehr als die Zahl acht

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/07_seam.tex:45-70](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/07_seam.tex#L45) · `section:67e571744e99ca5b1bfd` · section

Die zentrale Ladung ist eine Kennzahl einer konformen Feldtheorie. Für die chiralen Niveau-1-Faktoren gilt Das Produkt hat also schon vor einer Kopplung [formula in source] . Ein später gefundener Wert acht allein ist kein Beweis einer [formula in source] -Erweiterung und kein Beweis eines Kondo-Flusses.

## Zuse und Wolfram: eine Verwandtschaft ohne Rangordnung

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/10_ausblick.tex:2-15](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/10_ausblick.tex#L2) · `section:6f65165d9f307d71c65f` · section

Der eingefügte Gesprächstext vergleicht den Universalraum mit Konrad Zuse und Stephen Wolfram. Zuses Werk heißt Rechnender Raum, nicht „denkender Raum“. In seinem Buch von 1969 untersucht er digitale Beschreibungen physikalischer Felder und Teilchen und die Rolle von Automaten. Das ist ein historischer Bezugspunkt für die Vorstellung von Physik als regelgeleitetem Prozess. https://link.springer.com/book/10.1007/978-3

## RH, Faktorisierung und P versus NP

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/10_ausblick.tex:26-36](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/10_ausblick.tex#L26) · `section:b2ec414c784bcf2ba002` · section

Die Universalraumlinie liefert keinen neuen Beweis dieser Probleme. Die in S04 genannten RH-Katalogzahlen – 2753 Records, 1097 kuratierte, 122 offene, 319 kuratierte beziehungsweise 405 gesamte Kills – sind ein datierter Bericht dieser Quelle und hier nicht live geprüft.

## Wie die Quellen ihre eigenen Prüfungen beschreiben

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/11_anhang.tex:97-108](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/11_anhang.tex#L97) · `section:665c3efa018681437595` · section

L16mmL41mmY Quelle& Berichtete Prüfung& Reichweite\\ S09&11214 Bedingungen pro Modus, elf Negativvarianten&Ursprungsaudits und Zahlenprüfungen; kein vollständiger Lean-/RH-Neubau.\\ S07&325 + 147 Bedingungen, 19 Tests&Inversion und Follow-ups; mehrere spätere Minimalitätskorrekturen erforderlich.\\ S06&86 eigene Bedingungen sowie ausgewählte Originalreplays&45-/30-Quotienten, Uhr und Herkunftskontrollen; begrenzte Ke

## Eine bedingte Auswahlregel für die logarithmische Energie

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex:26-36](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex#L26) · `section:3da3131701887f7eb677` · subsection

Warum gerade [formula in source] ? Aus [formula in source] allein folgt das noch nicht: Man darf jeder Primzahl zunächst einen beliebigen Wert [formula in source] geben. Eine zusätzliche Ordnungsregel schließt die Lücke. Ist [formula in source] monoton in der natürlichen Zahl [formula in source] , so gilt notwendig Der Beweis ist kurz. Setze [formula in source] . Aus [formula in source] folgen [formula in source] Div

## Eigene Anschlussrechnung: Ein verschwindendes Signal ist mehrdeutig

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex:130-150](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/12_schatten_arithmetik.tex#L130) · `section:8052fbf017c8c33b46c5` · subsection

Unabhängig vom vollständigen Ressourcenbeweis dieser Arbeit untersuchen wir den folgenden einfachen thermischen Eta-Auslesekanal: Er entsteht durch einen Gibbszustand für [formula in source] und eine diagonal ausgelesene Paritätsphase. Bei festem [formula in source] und [formula in source] konvergiert der Zähler gegen [formula in source] , während [formula in source] Also geht das Rohsignal [formula in source] an jed

## Weitere offene Stellen mit unterschiedlicher Beweiskraft

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/15_schatten_offene_phaenomene.tex:27-43](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/15_schatten_offene_phaenomene.tex#L27) · `section:2ed06791fbfcca01ddab` · section

L32mmL56mmL60mm Thema& Was den Ansatz einschränkt& Was eine Erklärung liefern müsste\\ Zeitpfeil&Beständige Aufzeichnungen und irreversible Makroprozesse bei oft reversiblen Grundgleichungen.&Zustandsauswahl, Anfangskorrelationen, Zugriff und Entropiefluss; keine bloße Benennung eines inneren Parameters als Zeit.\\ Messproblem&Interferenz und stabile Messergebnisse müssen zusammen beschrieben werden.&Ein vollständige

## Zusätzlicher Einblick in den RH-Forschungsbestand

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/17_schatten_quellen.tex:3-29](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/17_schatten_quellen.tex#L3) · `section:1315342ad619cf8c4410` · section

Die Erweiterung wurde am 14. September 2026 gegen verfügbare Originalabschnitte im lokalen Repository tfpt-theoryv4 abgeglichen. Der gelesene Git-Stand war 66b91e40e245569f06ab440ead80f446c9be0ee5. Dies identifiziert den Checkout; es behauptet keinen frischen vollständigen Beweis- oder Testlauf. Die tatsächlich verwendeten Dateiinhalte sind zusätzlich mit SHA-256 im Paket erfasst, auch soweit der Arbeitsbaum von Git 

Explicit source references:

- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/experiments/tfpt-discovery/gabor_first_contact_selberg_result.json](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/transformationen/source-snapshots/tfpt/experiments/tfpt-discovery/gabor_first_contact_selberg_result.json#L1) · explicit_file_citation

## Die 128 zusätzlichen Bedingungen

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/17_schatten_quellen.tex:30-38](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/17_schatten_quellen.tex#L30) · `section:506f3fb05137a3b6a269` · section

Der separate Prüfer verify_shadows.py importiert keinen ursprünglichen TFPT- oder RH-Code und keine Nullstellentabellen. Er enthält 126 exakte beziehungsweise symbolische Bedingungen und zwei numerische Kontrollen. Die Nummer der ersten Nullstelle im Eta-Diagramm ist ein ausdrücklich eingesetzter Referenzwert; das Diagramm ist kein eigener Nullstellensuchlauf.

## Die sechs neuen Quellen: geprüfte Korrekturen

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex:1-2](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex#L1) · `section:5db26c5c342537bd32e7` · chapter

No opening prose excerpt; see the source.

## Was gegenüber v1.1 neu ist

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex:3-5](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex#L3) · `section:866e9030194940799837` · section

Die sechs zusätzlichen Unterlagen heißen im neuen Quellenregister N1 bis N6; die ursprünglichen S01 bis S11 bleiben unverändert. Ihr Audit trennt exakte endliche Identitäten, numerische Spektren und zusätzliche Modellannahmen. 100 eigene Bedingungen bestanden: 78 exakte beziehungsweise Integritätsprüfungen und 22 numerische. Die anschließende gemeinsame Ausführung hat einen eigenen 231-Bedingungen-Vertrag. Diese Zähl

## Die zentrale Reparatur: Wege nicht zu früh unterscheiden

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex:6-28](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex#L6) · `section:a736ece557b95fcb2fb0` · section

Setze [formula in source] und [formula in source] . Der Wedge-Kanal besitzt Für [formula in source] verschwindet [formula in source] . Beide geordneten Wege enden im gleichen virtuellen Zustand und interferieren. Orthogonale Records für [formula in source] und [formula in source] ersetzen dies durch [formula in source] : Der antisymmetrische Rang-6-Kanal wird zum Rang-12-Kanal. Bei gleichem Energienenner entsteht ein

## Der erste Schatten wählt die Fortsetzung noch nicht

[experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex:29-35](../../../../experiments/theory-contracts/universalraum-five-source-frontier-20260914/baseline-v1.3/chapters/18_audit_v13.tex#L29) · `section:d1d7ed4cb3c96e4c4450` · section

Mit [formula in source] und [formula in source] ist auf [formula in source] unitär und kollektiv [formula in source] -kovariant. Alle [formula in source] liefern für Materieeingänge denselben ersten blockdephasierten Schatten. Dennoch wirkt [formula in source] dort als [formula in source] , während [formula in source] als [formula in source] wirkt: [formula in source] kehrt als [formula in source] oder als [formula i
