# RH semantic catalog

GENERATED — do not hand-edit. Built by `rh/catalog/build_catalog.py`.

Research documentation. NOT evidence for or against the Riemann Hypothesis in either direction. NO RH CLAIM.

Records: **2755** (fragments overlay: 1078; needs_review: 1658; violations: 0).

## Counts by family × outcome

| family | PROVED | CERTIFIED | MEASURED | KILLED | INCONCLUSIVE | OPEN | RESTATED | SEALED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WEIL_POSITIVITY_WINDOWS | 41 | 223 | 184 | 165 | 40 | 122 | 32 | 22 |
| SCREW_SUBORDINATION_LSTAR | 16 | 45 | 31 | 70 | 49 | 4 | 7 | 6 |
| LEAN_FORMALIZATION | 35 | 4 | 3 | 7 | 2 | 182 | 2 | 2 |
| EXPLICIT_FORMULA_IDENTITY | 6 | 14 | 10 | 8 | 3 | 11 | 0 | 6 |
| OPERATOR_SPECTRAL | 2 | 37 | 20 | 20 | 7 | 39 | 4 | 1 |
| RHP_IIKS_TAU | 2 | 25 | 31 | 16 | 9 | 15 | 0 | 8 |
| TOEPLITZ_MOMENT_POSITIVITY | 5 | 27 | 10 | 9 | 1 | 6 | 4 | 2 |
| MELLIN_PICK_LEE_YANG | 2 | 10 | 4 | 9 | 0 | 12 | 0 | 0 |
| LATTICE_E8_HECKE | 9 | 26 | 31 | 29 | 1 | 67 | 2 | 2 |
| ADELIC_GROUPOID_CONNES | 0 | 2 | 6 | 10 | 1 | 12 | 0 | 0 |
| ARAKELOV_HODGE_INTERSECTION | 0 | 1 | 9 | 0 | 0 | 27 | 1 | 0 |
| CM_CURVE_GEOMETRY | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 |
| DYNAMICS_CLOCKS_PF | 0 | 7 | 11 | 11 | 3 | 32 | 1 | 0 |
| SELBERG_TRACE_CONTACT | 0 | 2 | 3 | 3 | 0 | 6 | 0 | 0 |
| PRIME_EVENT_LOG_DECODING | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0 |
| SIEVE_FACTORING_GEOMETRY | 0 | 13 | 17 | 22 | 3 | 15 | 0 | 1 |
| CERTIFICATE_INFRASTRUCTURE | 0 | 29 | 22 | 14 | 0 | 11 | 0 | 7 |
| EXTERNAL_ADJUDICATION | 0 | 0 | 3 | 0 | 0 | 2 | 1 | 5 |
| OTHER | 0 | 4 | 13 | 9 | 2 | 529 | 20 | 1 |

## Counts by kind

| kind | n |
| --- | --- |
| ATTACK | 1099 |
| CERTIFICATE | 42 |
| CONTROL | 251 |
| DOCUMENTATION | 734 |
| EXTERNAL_AUDIT | 12 |
| FORMALIZATION | 259 |
| FOUNDATION | 261 |
| OTHER | 2 |
| REDUCTION | 53 |
| TOOLING | 42 |

## Counts by failure_class

| failure_class | n |
| --- | --- |
| CIRCULAR | 28 |
| LOSSY_CONSTANT | 118 |
| NOT_APPLICABLE | 1996 |
| NO_BRIDGE | 163 |
| NUMERIC_ARTIFACT | 28 |
| ORACLE_LEAK | 5 |
| RESTATEMENT | 37 |
| STRUCTURAL_MISMATCH | 191 |
| UNCONVERGED | 131 |
| WORLD_BLIND | 58 |

## LOAD_BEARING_OPEN

| round | family | path | question |
| --- | --- | --- | --- |
| r26 contract | EXPLICIT_FORMULA_IDENTITY | `verification/v894_diagonal_refinement.py` | Can the pair-correlation wall be made a concrete conditional diagonal contract? |
| r279 | RHP_IIKS_TAU | `experiments/tfpt-discovery/oriented_theorem_probe.py` | Does an oriented-midpoint index bilanz prove the remaining midpoint theorem? |
| r283 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/lstar_problem.pdf` | State L* as a standalone open inequality for external mathematicians? |
| r283 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/lstar_problem.tex` | State L* as a standalone open inequality for external mathematicians? |
| r300 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/diag_target_probe.py` | Can the diagonal decay sl_D<=sigma* be derived, and is the pair ratio structural? |
| r301 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/neff_target_probe.py` | Why does n_eff grow ~N, and can slope(n_eff)>=+0.908 be proved? |
| r302 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/unif_target_probe.py` | Why is the /PDelta/ block profile quasi-uniform (UNIF_TARGET)? |
| r317-r322 | SCREW_SUBORDINATION_LSTAR | `verification/v969_forks_and_redteam.py` | What does the red-team extraction audit find, and which of the two forks survive? |
| r323-r327 | SCREW_SUBORDINATION_LSTAR | `verification/v970_extraction_and_composition.py` | Can the extraction seam be repaired elementwise, and does the terminal composition close? |
| r324 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/qmax_m2_origin_probe.py` | What is the origin of QMAX and M2 after the sliding-bound GO? |
| r326 | LEAN_FORMALIZATION | `rh/lean/RH/Elementwise.lean` | Can window-local positivity extract the Weil form on native dyadic autocorrelations? |
| r341 | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/fold_bellman_reverse_holder_probe.py` | Does a path-weighted Bellman / reverse-Hölder two-arm theorem close the terminal? |
| r344 | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/fold_two_scale_balance_probe.py` | What two-scale R* mass balance freezes after the r341 deficiencies? |
| r359 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/schur_wronskian_dual_probe.py` | Does the critical 2×2 Schur block in the dual resolvent carry the full L* margin? |
| r360 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/critical_saturation_probe.py` | Does critical saturation of the dual-void block close the r359 asymptotics handoff? |
| r360+r362 companion, updated r367-r373 | SCREW_SUBORDINATION_LSTAR | `rh/problem/rdagger_saturation.pdf` | What is the minimal inertia form of the bordered dual resolvent R-dagger? |
| r360+r362 companion, updated r367-r373 / r412 / r426 / R-DOSSIER DCCXCVII | SCREW_SUBORDINATION_LSTAR | `rh/problem/rdagger_saturation.tex` | What is the minimal inertia form of the bordered dual resolvent R-dagger? |
| r363 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/canonical_sturm_induction_probe.py` | Can an internal Sturm/pinning or CD-induction prove R-dagger>I/2? |
| r366 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/edge_gap_ms_probe.py` | Does Markov–Stieltjes mass counting force a dual-OP zero into the pair-gap? |
| r367 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/final_two_rank_inertia_probe.py` | Can a Haynsworth two-rank inertia cut bypass edge-gap and rest positivity? |
| r370 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/matrix_weyl_index_probe.py` | Is a matrix Weyl phase index a source-pure replacement for Haynsworth/hBal? |
| r398 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/high_moment_inertia_probe.py` | Can a fixed high even moment of (I-R_{N-3}) certify P1 (nneg≤1)? |
| r399 | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/source_weyl_energy_probe.py` | Does source-pure Weyl energy of the centered mass difference decay? |
| r400 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/bulk_one_defect_probe.py` | Is P1 a rank-1 bulk one-defect frame inequality or a phase form? |
| r403 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/p1_construction_probe.py` | Is lam2(R_{N-3})≥1/2 a theorem of the fold mask with arbitrary sign-conforming weights? |
| r404 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/one_defect_gram_probe.py` | Is Q^T A0 Q = FF^T-ell ell^T source-explicit from Lambda, log, fold, tent, digamma? |
| r405 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/edge_contractive_lift_probe.py` | Can the missing Euler null mode be written ell=Vc with 1-//c//^2 equal to kappa(-sch)? |
| r413 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/hole_top_mode_probe.py` | Is the defect the top OP of the hole measure, with T0 contractive on that complement? |
| r416 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/debranges_index_probe.py` | Is P1 a Hermite–Biehler/Potapov index theorem with kappa(Theta)≤1? |
| r417 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/source_sch_sign_probe.py` | Can sch<0 be read source-pure from the r401 Sylvester chart? |
| r417 companion | RHP_IIKS_TAU | `rh/problem/source_sch_sign.pdf` | Is the source Schur-sign chart exact, and is its decay rate source-derived? |
| r417 companion | RHP_IIKS_TAU | `rh/problem/source_sch_sign.tex` | Is the source Schur-sign chart exact, and is its decay rate source-derived? |
| r418 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/phi_bb_sign_probe.py` | Is phibb<0 the asymptotic edge-sign carrier after /tau_un/→0? |
| r419 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/vacuous_overflow_probe.py` | Do the 6 VAC overflow rows cross to phibb<0, or do they live by a tau save? |
| r419 companion | RHP_IIKS_TAU | `rh/problem/vacuous_overflow.pdf` | Do vacuous overflows empty, or does a razor pole explain remaining life? |
| r419 companion | RHP_IIKS_TAU | `rh/problem/vacuous_overflow.tex` | Do vacuous overflows empty, or does a razor pole explain remaining life? |
| r420 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/cj_sigma_probe.py` | Does cofinal VAC c_J<-Sigma hold as the r419 reduction of sch<0? |
| r420 companion | OPERATOR_SPECTRAL | `rh/problem/cj_sigma.pdf` | Does an O(1) c_J–Σ gap survive, or does the reserve shrink? |
| r420 companion | OPERATOR_SPECTRAL | `rh/problem/cj_sigma.tex` | Does an O(1) c_J–Σ gap survive, or does the reserve shrink? |
| r421 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/reserve_limit_probe.py` | Does reserve R=-phibb go to 0 or to a positive R_inf on a_k=2^k? |
| r421 companion | OPERATOR_SPECTRAL | `rh/problem/reserve_limit.pdf` | Does the reserve −φ_bb tend to a positive floor or log-decay to zero? |
| r421 companion | OPERATOR_SPECTRAL | `rh/problem/reserve_limit.tex` | Does the reserve −φ_bb tend to a positive floor or log-decay to zero? |
| r422 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/sigma_limit_probe.py` | Is limsup Sigma < 2-den_inf on selected a_k=2^k source-pure? |
| r423 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/den_limit_probe.py` | Does den_k → den_inf<2 source-pure, or is limsup den≤dbar<2 explicit? |
| r424 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/gamma_chain_probe.py` | Is //b//^2 ≤ B_w = S_{N-2}+5/7 a border-chain theorem so gamma<1? |
| r424 companion | OPERATOR_SPECTRAL | `rh/problem/gamma_chain.pdf` | Does a termwise weight bound on the μ-Parseval chain prove γ<1? |
| r424 companion | OPERATOR_SPECTRAL | `rh/problem/gamma_chain.tex` | Does a termwise weight bound on the μ-Parseval chain prove γ<1? |
| r425 companion | OPERATOR_SPECTRAL | `rh/problem/cross_chain_gamma.pdf` | Does //b//^2≤S plus q_N<1 give a cofinal γ<1 theorem? |
| r425 companion | OPERATOR_SPECTRAL | `rh/problem/cross_chain_gamma.tex` | Does //b//^2≤S plus q_N<1 give a cofinal γ<1 theorem? |
| r428 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/qn_reopened_probe.py` | Does the selected 2^k sequence reopen a q_N margin with a fourth death coordinate? |
| r428 companion | RHP_IIKS_TAU | `rh/problem/qn_reopened.pdf` | On a_k=2^k, is q_N<1 with a usable selected margin toward cofinality? |
| r428 companion | RHP_IIKS_TAU | `rh/problem/qn_reopened.tex` | On a_k=2^k, is q_N<1 with a usable selected margin toward cofinality? |
| r431 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/source_potapov_probe.py` | Is I-T0*T0 a source Potapov/Redheffer product of point-mass 2×2 factors? |
| r438 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/evolutionary_certificate_probe.py` | Can grammar-GP / NNLS / truncation search find a source certificate for P1 or q-dagger? |
| r440 companion | RHP_IIKS_TAU | `rh/problem/mean_tau_index.pdf` | Do τ^dagger zeros give an unconditional block-mean bound on the 1/2-cluster? |
| r440 companion | RHP_IIKS_TAU | `rh/problem/mean_tau_index.tex` | Do τ^dagger zeros give an unconditional block-mean bound on the 1/2-cluster? |
| r442 companion | RHP_IIKS_TAU | `rh/problem/block_mean.pdf` | Is the block-mean of {q^dagger>1} unconditionally bounded below 1? |
| r442 companion | RHP_IIKS_TAU | `rh/problem/block_mean.tex` | Is the block-mean of {q^dagger>1} unconditionally bounded below 1? |
| r443 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/delta_floor_probe.py` | Does selected delta=1-q-dagger have a positive floor on a_k=2^k? |
| r443 companion | RHP_IIKS_TAU | `rh/problem/delta_floor.pdf` | Is liminf δ_k>0 on the selected sequence, i.e. a δ-floor? |
| r443 companion | RHP_IIKS_TAU | `rh/problem/delta_floor.tex` | Is liminf δ_k>0 on the selected sequence, i.e. a δ-floor? |
| r444 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/signed_border_mean_probe.py` | Does a signed border-mean triple sum give a non-circular q-dagger<1 bound? |
| r450 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/prefix_mincut.pdf` | Is n_stab-compression of R-dagger the frequently-mincut object, and does the prefix floor decide? |
| r457 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/jp_increment_probe.py` | Does the MAIN–ARCH increment from J_P race to the cap without eating the k=10 margin? |
| r457 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/jp_increment.pdf` | Does the J_P prime increment cancel in rho and save the k=10 race? |
| r457 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/jp_increment.tex` | Does the J_P prime increment cancel in rho and save the k=10 race? |
| r458 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/cofinal_family.pdf` | Is there a cofinal selected family living at the cap through large k? |
| r458 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/cofinal_family.tex` | Is there a cofinal selected family living at the cap through large k? |
| r459 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/fullcomb_cleanup.pdf` | Was RACE_EATS_K10 a TABLE_CAP artefact, and does the race trend survive? |
| r459 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/fullcomb_cleanup.tex` | Was RACE_EATS_K10 a TABLE_CAP artefact, and does the race trend survive? |
| r460 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/race_proof_probe.py` | Can a source-derived two-band/spectral certificate prove the selected race q<1? |
| r460 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/race_proof.pdf` | Can the selected-window race be proved cofinally via spectral overlap? |
| r460 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/race_proof.tex` | Can the selected-window race be proved cofinally via spectral overlap? |
| r467 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/overlap_mechanism_probe.py` | Does qualitative MAIN-mode alignment yield an Abel-currency overlap bound? |
| r467 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/overlap_mechanism.pdf` | Does a smooth-versus-rough Abel mechanism bound selected-window spectral overlap? |
| r467 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/overlap_mechanism.tex` | Does a smooth-versus-rough Abel mechanism bound selected-window spectral overlap? |
| r468 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/octave_renorm_probe.py` | Does octave renormalization of the a^2-comb make the selected race Cauchy? |
| r468 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/octave_renorm.pdf` | Does octave renormalization yield a Cauchy block-limit cut for q-dagger? |
| r468 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/octave_renorm.tex` | Does octave renormalization yield a Cauchy block-limit cut for q-dagger? |
| r474 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/modulus_upgrade_probe.py` | Can r471 grid certificates upgrade to a continuity modulus on the H^2 ball? |
| r477 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/highmode_probe.py` | Does lambda_*(L)>=0 reduce to high-mode dominance plus a finite Schur block? |
| r478 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/endtoend_fixedl_probe.py` | Can a fixed-L SATZ for lambda_*(0.3) close end-to-end? |
| r479 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/lambdastar03_probe.py` | Does multiplier-plus-rank-one close lambda_*(0.3)>=c>0? |
| r480 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kappa_high_probe.py` | Is the named r479 kappa_high<=1.79e-2 bound true? |
| r481 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/schur_cert_probe.py` | Can interval FT plus IBP tail certify the r480 Schur remainder? |
| r482 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/carleson_edgeband_probe.py` | Does selected-window edge mass F_k(t) obey a restricted large-sieve law? |
| r482 | WEIL_POSITIVITY_WINDOWS | `rh/problem/carleson_edgeband.pdf` | Is there a Carleson testing-law envelope that closes selected-window edge bands? |
| r482 | WEIL_POSITIVITY_WINDOWS | `rh/problem/carleson_edgeband.tex` | Is there a Carleson testing-law envelope that closes selected-window edge bands? |
| r483 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/filon_enclosure_probe.py` | Can Filon enclose the two open r481 integral classes and close lambda_*(0.3)? |
| r484 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/block_completion_probe.py` | Does a ~20x coupling drop per even double-step push leftover below budget? |
| r485 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weighted_schur_probe.py` | Does a frequency-weighted tail reserve close the L=0.3 Schur? |
| r486 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/woodbury_minf_probe.py` | Can a Woodbury/Birman–Schwinger enemy representation close lambda_*(0.3)? |
| r488 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/resolvent_solve_probe.py` | Is certified R^{-1} on the r486 enemy modes available? |
| r490 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/operator_residual_probe.py` | Is the r488 Galerkin residual below the 5.6e-3 BS margin? |
| r535 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_separation_redteam_probe.py` | Do compact FullWeil tests separate injected off-critical zeros? |
| r539 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_gaussian_separation_probe.py` | Do centered Hermite–Gaussians separate off-critical zeros with a certified tail? |
| r540 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_online_null_separation_probe.py` | Can on-line nulling inside the compact Weil class separate off-critical zeros? |
| r544 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_uniform_inequality_probe.py` | Is the exact pure-Gabor inequality uniform on a one-quadruple scan? |
| r549 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_density_transfer_probe.py` | Is discrete Gaussian density transfer uniform, and does an offline adversary kill it? |
| r551 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_extremal_selection_probe.py` | Does extremal selection after seeing an off-line zero repair the r549 killer? |
| r553 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_config_first_probe.py` | Does a config-first quantifier flip let 1- or 2-packet Gabors beat every increment catalog? |
| r554 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_mixture_witness_probe.py` | Can a mixture witness beat the r553 cluster wall on the leftover scale? |
| r561 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_uniform_dominance_probe.py` | Is there a constructive (a,omega) isolation-shrink rule with uniform dominance? |
| r563 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_dominance_redteam_probe.py` | Does the sealed r561 isolation-shrink rule survive an adversarial twin? |
| r591 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_fixed_packet_cofinal_probe.py` | Can a Z-independent fixed packet stay cofinally negative? |
| r592 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_window_adaptive_tail_probe.py` | Does a window-adaptive tail after seeing W_R beat equal-sigma killers? |
| r596-r600 | LEAN_FORMALIZATION | `rh/lean/RH/GaborAnchoredWitness.lean` | Does an anchored window witness close host-retune and float64 gaps? |
| r601 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_weil_positivity_subfamily_probe.py` | Is there a prime+digamma subfamily of pure Gabor tests with Z>=0? |
| r606 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/connes_prolate_residual_gap_probe.py` | Does the Connes residual-vs-gap ratio stay positive and converge in L? |
| r611 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/connes_observable_aubin_nitsche_probe.py` | Does the observable Aubin–Nitsche eta_obs converge to 0 with L? |
| r622 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/support_darboux_probe.py` | Does a Darboux/Lyapunov transport identity exist for scaled Qtilde(L)? |
| r623 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/semilocal_p2_dilation_probe.py` | Can the 2-adic Weil channel be a principal-block / rank-one dilation? |
| r625 | RHP_IIKS_TAU | `experiments/tfpt-discovery/iiks_vanishing_metric_probe.py` | Does Zhou's vanishing-lemma metric apply to the corpus discrete IIKS jump? |
| r638 | SELBERG_TRACE_CONTACT | `experiments/tfpt-discovery/gabor_first_contact_selberg_probe.py` | Do first-contact conditions plus Selberg square-completion yield a PSD operator L? |
| 2026-09-05-all-place-audit | ARAKELOV_HODGE_INTERSECTION | `rh/catalog/analysis/all_place_tate_audit.md` | Can the rigid level-8 Calabi--Yau Tate factor carry the complete Weil form? |
| 2026-09-09-research-followups | WEIL_POSITIVITY_WINDOWS | `rh/catalog/analysis/research_followups_20260909.md` | Which source-specific obligations remain after full odd coercivity and the whole-core dilation counterexample? |
| PRIME.RDAGGER.PROGRAM_EVOLUTION.01 | LEAN_FORMALIZATION | `experiments/tfpt-discovery/evolve/evolve_props.py` | Can evolved programs expose classical formulas for two Lean Props and map the remaining FREQ spectral kernel? |
| ledger:PRIME.EXCLUSION.BATTERY2.01 | WEIL_POSITIVITY_WINDOWS | `verification/v826_prime_exclusion_battery2.py` | PRIME.EXCLUSION.BATTERY2.01: the preregistered battery v2 and the measurement-range extension -- the exclusion floor of the certified ladder drops from Xi ~ 0.2187 to the uncensored declining Xi_v2 (deepest 0.0816, slope |
| ledger:PRIME.EXCLUSION.LADDER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v825_prime_exclusion_ladder.py` | PRIME.EXCLUSION.LADDER.01: the certified exclusion ladder of the GL1 prime-comb tower -- verified PSD rungs inverted into rigorous quadruple-exclusion regions -- extended to X = 24.81 with hardened floating-point certificates, and |
| ledger:PRIME.EXCLUSION.WINDOW.01 | WEIL_POSITIVITY_WINDOWS | `verification/v828_prime_comb_window.py` | PRIME.EXCLUSION.WINDOW.01: the comb-native window verification -- the capstone of the exclusion-detector strand: on the disjoint test window gamma in (60, 120] the SAME certified positivity object yields both legs -- |
| relative_window_flow_20260907 | WEIL_POSITIVITY_WINDOWS | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/relative_window_flow_20260907/relative_flow_proof.md` | Can a whole-core relative dilation estimate continue positive Weil windows globally? |
| rh_zero_temperature_readout_20260908 | TOEPLITZ_MOMENT_POSITIVITY | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_zero_temperature_readout_20260908/README.md` | Does a compact positive readout realize all arithmetic target moments without assuming RH? |

## CERTIFIED / PROVED

| round | outcome | family | path | solved |
| --- | --- | --- | --- | --- |
| ledger:PRIME.KR4.DRIVER.CERT.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v917_driver_rate_certification.py` | Certified-given-audit rate detection [C] (fine type Numerical; grade CERT-GIVEN-AUDIT carried verbatim -- rigorous Cauchy enclosure GIVEN the incomplete-gamma audit comparator PLUS the DECLARED Lambda-tail and peel-box models, never upgraded; DISGUISE-ADJACENT value channel per the round-120 tau-screen; the exact matched-pin algebra |
| ledger:PRIME.KR4.EPSTEIN.COLLAPSE.01 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v916_epstein_weil_violation.py` | Certified violation certificate [E] (fine type Numerical, CERT-NUM: two-precision budgeted evaluation, sha-pinned test vector reproduced in-run; the off-line-zero interpretation step COND-CLASSICAL, cited; PINNING DISCLOSURE: sieve + wards + deaths + ZK prefix + FULL certificate recomputed in-run, the L = |
| r112-r128 | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/l1_weyllaw_probe.py` |  |
| r114-r162 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/window_instrument_probe.py` |  |
| r114-r165 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tau_blockaverage_probe.py` |  |
| r115 | CERTIFIED | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/coupling_ansatz_probe.py` |  |
| r115-r119 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/irwall_probe.py` |  |
| r116-r129 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bughunt3_probe.py` |  |
| r116-r133 | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/hpin_floor_probe.py` |  |
| r116-r136 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/counteq_seedball_probe.py` |  |
| r116-r138 | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/jetlock_bandmass_probe.py` |  |
| r116-r138 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/qsubgap_probe.py` |  |
| r116-r147 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/collapserate_probe.py` |  |
| r116-r148 | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/tlawcap_blocks_probe.py` |  |
| r116-r153 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/nearalign_probe.py` |  |
| r116-r154 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/assembly_walls_probe.py` |  |
| r116-r154 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/rootladder_probe.py` |  |
| r116-r156 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/edge_cleanup_probe.py` |  |
| r116-r161 | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/fullgap_growthlaw_probe.py` |  |
| r116-r162 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/novelty_synthesis_probe.py` |  |
| r116-r168 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/sigmafloor_probe.py` |  |
| r116-r169 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/jetmass_floor_probe.py` |  |
| r120-r124 | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/frameschedule_probe.py` |  |
| r121-r124 | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/selection_probe.py` |  |
| r131-r172 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gonek_pricing_probe.py` |  |
| r131-r195 | PROVED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/turan_extremal_probe.py` |  |
| r131-r198 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/fewatom_reduction_probe.py` |  |
| r137-r162 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bughunt5_probe.py` |  |
| r156-r180 | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/census_lift_probe.py` |  |
| r171-r198 | CERTIFIED | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/pole_homotopy_probe.py` |  |
| r171-r200 | CERTIFIED | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/eigvec_geometry_probe.py` |  |
| r171-r206 | CERTIFIED | LEAN_FORMALIZATION | `experiments/tfpt-discovery/secular_crossing_coord_probe.py` |  |
| r224 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/tau_symbolic_probe.py` | Finite-identity tau equals det(I-sE) via s-dressed port; confluence diagonal exact [C]. |
| r224-r226 | CERTIFIED | RHP_IIKS_TAU | `verification/v955_tau_iiks_toda_dictionary.py` | [E] finite IIKS/Toda dictionary (Lax1, rank-2, Hirota) certified. [O] no-pole cofinal remains open. |
| r224-r305 | PROVED | WEIL_POSITIVITY_WINDOWS | `rh/lean/RH/Window.lean` |  |
| r225-r233 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/plateau_sumrule_probe.py` |  |
| r225-r238 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tstar_leading_sign_probe.py` |  |
| r226 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/hirota_sign_probe.py` | Hirota equals gammahat/gamma exactly; positivity is wall-equivalent, not an independent sign [E]. |
| r228-r231 | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `verification/v956_signedmoment_halffilling_duality.py` | [E] half-filling law, duality and L-gauge. [O] positive-prefix firewall still open. |
| r228-r305 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/Inertia.lean` |  |
| r230 | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/jfraction_probe.py` | Free-prefix J-fraction matches 2N-1 moments; wall-equivalent, not a new sign source [C]. |
| r231 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/rhp_midpoint_probe.py` | Midpoint connection exact; node-log pole typed; dictionary closes in both variants [C]. |
| r243-r263 | PROVED | EXPLICIT_FORMULA_IDENTITY | `rh/lean/RH/Recursion.lean` |  |
| r243-r305 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/Closure.lean` |  |
| r243-r320 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/Counterexamples.lean` |  |
| r243-r320 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/PairBound.lean` |  |
| r243-r397 | PROVED | WEIL_POSITIVITY_WINDOWS | `rh/lean/RH/Source.lean` |  |
| r243-r434 | PROVED | WEIL_POSITIVITY_WINDOWS | `rh/lean/RH/Canonical.lean` |  |
| r243-r459 | PROVED | LEAN_FORMALIZATION | `rh/problem/endtoend_gapmap.tex` |  |
| r243-r463 | PROVED | LEAN_FORMALIZATION | `rh/problem/lean_fidelity.tex` |  |
| r244 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/bordered_hankel_probe.py` | Bordered PSD dictionary exact; corner is imported only [E]. |
| r244-r253 | CERTIFIED | RHP_IIKS_TAU | `verification/v958_bordered_tau_readout_dictionary.py` | [E] bordered dictionary, error formulas, PSD base. [O] fullsource base/fiber campaign remains open. |
| r245 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/bordered_finite_rank_probe.py` | Border formulated as Schlesinger rank-1 insertion [C]. |
| r248 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/border_centering_probe.py` | Centering congruence exact on the bordered readout [C]. |
| r256-r259 | CERTIFIED | RHP_IIKS_TAU | `verification/v959_coupledtau_terminal_dictionary.py` | [E] coupled-tau recursion, bilinear form, telescope. [O] two last edges remain open. |
| r260-r275 | CERTIFIED | RHP_IIKS_TAU | `verification/v960_terminal_surface_closure.py` | [E] 42/42 q_N<1 census (41 mechanism + kz15 exact-finite); H1-H4 Lean. [O] cofinal front / H5. |
| r270 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/kz15_boss_probe.py` | kz15 closed by interval certificate (dps 640, width 1.5e-92, margin +0.0268). Surface 41/42+kz15. |
| r274 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/wronskian_dictionary_probe.py` | Exact D_n↔Wronskian dictionary (32/32); r231 sign-blindness becomes an identity. |
| r274-r278 | CERTIFIED | RHP_IIKS_TAU | `verification/v961_midpoint_orientation_dictionary.py` | [E] midpoint dictionary and Maslov R2 GO (atom-Sturm refuted). [O] oriented midpoint theorem remains. |
| r277 | CERTIFIED | RHP_IIKS_TAU | `experiments/tfpt-discovery/maslov_census_probe.py` | Maslov R2 GO: Jacobi interlacing/reality, blind 42/42, controls at flip+1, one-way. |
| r279-r281 | CERTIFIED | RHP_IIKS_TAU | `verification/v962_halffilling_pinning_theory.py` | [E] half-filling pinning theory; open statement is minC>=N_w iff all free-window h_n>0. |
| r282-r285 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v963_lstar_reduction_dictionary.py` | [E] L* reduction dictionary: mu-frame congruence and contraction exact; classical languages all dead. |
| r283 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_lstar_instance.py` | 12/12 gates; lambda_max(E_184)<1<lambda_max(E_185); 42/42 windows positive. Finite [C]. |
| r286-r289 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v964_lstar_coherence_census.py` | [E] L* coherence census: 15 new anchors all positive; vdC candidate named; METRIC_ONLY twin adjudication. |
| r296-r300 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v966_l2_reduction_chain.py` | [E] L2 reduction chain; DENS fork closed honestly. [O] NEFF_TARGET the remaining inequality. |
| r298 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/window_border_transfer_probe.py` | Transfer exact and sign-preserving; window main term empty; S_F≈B(PDelta,PDelta). |
| r305-r316 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v968_architecture_adjudication.py` | [E] four-level structure frozen; rank-one source identities banked. Fiber GO with provenance open. |
| r305-r332 | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/lean/RH/Augmented.lean` |  |
| r306 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/renyi3_probe.py` | Rényi-3 GO (27/27): pointwise cubic law holds on the tested fiber. |
| r314 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/signed_cubic_flux_probe.py` | Signed-cube algebra exact (29/29); bookkeeping identity only. |
| r317-r322 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v969_forks_and_redteam.py` | [E] extraction-chain audit U1-U3. [O] Renyi-3 sliding bound fork; base antiphase is ALGORITHM_ARTIFACT. |
| r319-r434 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/DualResolvent.lean` |  |
| r321 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/continuous_coordinate_probe.py` | SLIDING_BOUND_GO (39/39). Pointwise G still fails; two-regime stays dead. |
| r323-r327 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v970_extraction_and_composition.py` | [E] elementwise extraction repair. [O] measured composition subcritical with typed extrapolation gap. |
| r325 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/extraction_order_probe.py` | Elementwise stabilization GO: repair is a quantifier statement, not a new mesh. Promoted in v970. |
| r329 | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/ext3_fresh_anchors_probe.py` | Fresh-anchor audit repair: sliding bound re-checked off the original 65-rung class ladder. |
| r331 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/twin_resolution_probe.py` | Twin footprint ≥3.4 orders below every margin to 1.8e-8; 11/11 anchors RESOLVE. |
| r339 | CERTIFIED | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/fold_density_dictionary_probe.py` | Density-per-descendant is a martingale from mass conservation; dictionary identity (must-fail e1). |
| r339+r341 (wave 14) | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v978_terminal_density_martingale.py` | [E] density martingale, moment dictionary, tilted tower, exact hand-off and pair ceiling. |
| r344/r346/r351/r353/r355 (wave 14) | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v979_cover_growth_k2.py` | [E] three-arm cover, growth ceiling C_FAB, K2 two-family law; Frame-A finite sliding coverage. |
| r345/r347/r348/r350/r352/r354 (wave 14) | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v980_lstar_margin_chain.py` | [E] closed L* margin-law chain: one-line identity, two-level theorem, pinning, rate equality. |
| r346 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/fold_cover_canonization_probe.py` | K1 stop at R=8/5 keeps 0/51 coverage; P02 predictor 1.000 core/OOS. Finite cover [C]. |
| r351 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/qmax_growth_law_probe.py` | Zero fresh FAB violations at frozen C_FAB 14.93. Finite family law [C]. |
| r355 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/k2_source_formula_probe.py` | Zero violations at C_2=11.87 on frame-B, NU-test, and fresh rows. Finite [C]. |
| r356 (wave 14) | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v981_lstar_borodin_duality.py` | [E] Borodin complementation bit-exact at half-filling; L* equivalent to R>1/2 I. |
| r357 (wave 14) | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `verification/v982_dirichlet_matched_frame.py` | [E] matched Dirichlet frame; chi-arch F_A symbolically derived from Lambda(s,chi). |
| r361 | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/mean_sieve_floor_probe.py` | g_i≥3/8 is mesh algebra; MED-CAP 8/3 tight; scramble still quantized [C]. |
| r361 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_medcap_steps.py` | 11/11 gates; Fractions geometry and chi4 kz53 prefix pins hold [C]. |
| r362 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/augmented_borodin_duality_probe.py` | L-dagger ⇔ R-dagger>I/2 ⇔ L* AND Terminal; border sits in the local 3×3 [C]. |
| r364 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_xn_steps.py` | Machine-check of pairing lemmas plus chi4 kz53 prefix pin [C]. |
| r365 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_v2_steps.py` | 12/12 gates; XOR, 2-regular refutation, and construction pins hold [C]. |
| r367-r373 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/Haynsworth.lean` |  |
| r369 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/mixed_haynsworth_probe.py` | Mixed update residual ~1e-14; generalized Haynsworth SATZ; r367 warning resolved as a form [C]. |
| r373-r380 | PROVED | TOEPLITZ_MOMENT_POSITIVITY | `rh/lean/RH/PivotCoordinate.lean` |  |
| r374 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_v2_lemma.py` | Machine-check of Wronskian, contrast dichotomy, and Path A pins [C]. |
| r375 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_p2_steps.py` | 12/12 gates; factorization and construction pins hold [C]. |
| r377 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_postcap_steps.py` | 16/16 gates; dictionary, inertia complement, and kz12 LATE pin [C]. |
| r378 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_compose_lemma.py` | Machine-check of Fejer/vdC/H-rule identities and 42-rung FRAME-A pins [C]. |
| r379 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_v3prime.py` | 17/17 gates; mesh, Jacobi, A_15, and Path A pins hold [C]. |
| r381 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_g_eps.py` | 13/13 gates; FO/R2 identities and FRAME-A w9 pins hold [C]. |
| r382 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_pivot_entry.py` | 14/14 gates; energy/interlacing toys and w9 flank-entry pins [C]. |
| r383 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_compose_premises.py` | 16/16 gates; toys and construction pins including scramble M3-kill [C]. |
| r384 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/FlankEntry.lean` | Finite algebra and FlankEntryPrefix bridge proved over Q; census stays 5 [E] Lean. |
| r385 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_christoffel_quiet.py` | 13/13 gates; trig identities and w9 Koksma-failure pins [C]. |
| r386 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_compose_premises2.py` | 16/16 gates; death-triangle toys and living/dead chi pins [C]. |
| r387 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_coherence_assist.py` | 13/13 gates; CD/Gershgorin toys and w9 wall/AP pins [C]. |
| r388 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_delta_deformation.py` | 13/13 gates; homogeneity/Fejer-pure toys and w9 Delta/FO pins [C]. |
| r389 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_weyl_energy.py` | 14/14 gates; Parseval toys and w9 energy/QM pins [C]. |
| r390 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_g_eps_mu.py` | 13/13 gates; Jacobi/U toys and w9 Fejer-occ/perm-kill pins [C]. |
| r391 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_construction_rl.py` | 17/17 gates; CS/eta toys and white-block/scramble pins [C]. |
| r392 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_deletion_transform.py` | 14/14 gates; one-point/block Uvarov toys and w9 identity pins [C]. |
| r393 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_tau_field.py` | 13/13 gates; tau toys and w9 F1-split/rank-1 pins [C]. |
| r394 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_sign_schur.py` | 14/14 gates; Dirichlet-sign toys and w9 Assist/mass-agree pins [C]. |
| r395 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_three_gap_mask.py` | 11/11 gates; Steinhaus toys and w9 nuniq=12 pins [C]. |
| r396 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_isolation_lemma.py` | 10/10 gates; packing toys and pair-rich/1010 lambda pins [C]. |
| r397/r638L | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/Selected.lean` | a_k=2^k sequence and Delta_k→0 proved; domain nonempty by construction [E] Lean. |
| r398 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_high_moment.py` | 12/12 gates; moment toys and w9 contraction/scramble nneg=21 pins [C]. |
| r399 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_source_weyl.py` | 11/11 gates; stencil/Laplacian toys and w9 C0=C1=0 pins [C]. |
| r400 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_bulk_one_defect.py` | 12/12 gates; frame/interlacing toys and w9 lift-rank pins [C]. |
| r401 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_edge_signature.py` | 13/13 gates; mixed-form toys and w9 reconstruction/dead-chi pins [C]. |
| r403 companion | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_p1_construction.py` | 11/11 gates; interlacing toys and w9 Gram/weight-rand pins [C]. |
| r404 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_one_defect_gram.py` | 11/11 gates; Cauchy/Loewner toys and w9 PD-compression pins [C]. |
| r405 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_edge_lift.py` | 12/12 gates; Euler/Parseval/Woodbury toys and w9 ones-lift pins [C]. |
| r406 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/OneDefect.lean` | Four one-defect theorems proved; independent of source R404/R405 [E] Lean. |
| r406-r430 | PROVED | OPERATOR_SPECTRAL | `rh/lean/RH/GraphResolvent.lean` |  |
| r407 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/dual_intertwiner_probe.py` | Formula residual 1.8e-14; P1 reduced to lam2(C)≥1; FL dictionary exact [C]. |
| r407 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/dual_intertwiner.pdf` | R=C(I+C)^{-1} and P1 iff λ2(C)≥1 [C]; SOURCE_GRAM_EXACT on the Euler moment layer. |
| r407 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/dual_intertwiner.tex` | Intertwiner exact; Euler moment SOURCE_GRAM_EXACT on the moment layer; P1 ⇔ lam_2(C)>=1 [C]. |
| r407 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_dual_intertwiner.py` | R=C(I+C)^{-1} and P1 iff λ2(C)≥1 [C]; SOURCE_GRAM_EXACT on the Euler moment layer. |
| r408 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_c_threshold.py` | 2×2 coherence/Rayleigh/rank/Cauchy SATZ [C]; source nC≤1 is a census not a Nyquist theorem. |
| r409 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_borodin_birkhoff.py` | Source-pure min-norm CLS graph identity SATZ [C]; T^dagger equals the r362 graph factor. |
| r410 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_hole_nyquist.py` | RK/degree/C_ii/Rayleigh SATZ [C]; d_min≥1 remains a source census; sequential birth reduced. |
| r411 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/threshold_identity_probe.py` | //T//=1/sqrt(Cmin) to 1e-14; excess = C-ev0 = top SV [C]. |
| r411 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_threshold_identity.py` | //T0//=1/sqrt(λ_min(C)) and the K0^perp energy split are SATZ [C]. |
| r413 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_hole_top_mode.py` | Lagrange/OP formulae SATZ over Q [C]; v_top is source-pure from Y, u^vee, P_Y'. |
| r415 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/top_mode_edge_probe.py` | beta-alpha=-sch SATZ; MAIN 42/42 sch<0; v_top is not the defect [C]. |
| r415 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_top_mode_edge.py` | −sch=β−α over Q SATZ [C]; Euler-on-v_top is constant content, not α_T. |
| r416 companion | CERTIFIED | MELLIN_PICK_LEE_YANG | `rh/problem/verify_debranges_index.py` | Wronskian over Q and Hermite–Biehler interlacing SATZ [C] (MAIN 42/42, χ 84/84). |
| r417 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_source_sch.py` | Woodbury and Sylvester-chart formulae SATZ [C]; τ→0 is a named finite census. |
| r418 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_phi_bb.py` | φ_bb=c_J+Σ SATZ [C] via the C-resolvent split. |
| r419 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_vacuous_overflow.py` | H3 and razor-pole accounts refuted [C]; six windows live by τ at finite N. |
| r420 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_cj_sigma.py` | den=1+//b//^2/B_w−v_t·s SATZ [C]; all 42 windows have den<2 with a flat O(1) gap. |
| r421 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_reserve_limit.py` | R=−φ_bb SATZ [C]; log model killed; five selected points prefer a floor vs k [C]. |
| r422 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_sigma_limit.py` | Σ=2//s//^2+4 s^T(C−I)^{-1}s SATZ [C]; near-1 mass stays O(0.01). |
| r423 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_den_limit.py` | den=1+γ−v_t·s SATZ [C]; γ<1 on 42/42+EXT+dead is a census [C]. |
| r424 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_gamma_chain.py` | b_k=⟨σ,π̂_k^μ⟩ Parseval SATZ [C]; census //b//^2≤0.80 S and γ≤0.724 [C]. |
| r425 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/cross_chain_gamma_probe.py` | //b//^2≤S SATZ; posted //b//^2<B_w reduces to q_N<1 [C]. |
| r425 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_cross_chain.py` | //b//^2≤S SATZ [C]; posted //b//^2<B_w reduces to q_N<1 on the 42-rung census. |
| r426 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/EdgeBalance.lean` | Finite-algebra chain proved; named Props for Parseval/Loewner/q_N [E] Lean. |
| r427 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_campaign_audit.py` | Five targets CLEAN [C]; no R397–R426 verdict flips; QD mass 1.357 and //T0// pins reproduced. |
| r428 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_qn_reopened.py` | Selected margin 0.617 vs 42-rung 0.0195 [C]; razor-overlap is VAC-only; /Z_loc/ wins COMPOSE. |
| r429 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_zloc_head.py` | Z_loc=t_loc+chain SATZ [C]; /Z_loc/≤1/2 is a finite selected census, not an explicit k0. |
| r430 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/FrequentlySelected.lean` | r434 Loewner and r430 FREQ extraction proved as finite implications [C]. |
| r431 companion | CERTIFIED | MELLIN_PICK_LEE_YANG | `rh/problem/verify_source_potapov.py` | Unipotent Redheffer product equals Cauchy m_X SATZ [C]; Lagrange S0 is Cauchy-π SATZ [C]. |
| r431-AUDIT companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_r431_audit.py` | r431 pins reproduced [C]; positive-mass J-products stay in S_0; Cauchy-π holds on a second window. |
| r433 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/edge_redheffer_probe.py` | Redheffer residual 1.9e-15; delta=1-q-dagger=-sch with c'=1 [C]. |
| r433 companion | CERTIFIED | MELLIN_PICK_LEE_YANG | `rh/problem/edge_redheffer.pdf` | R→R^dagger is the terminating 2×2-block Redheffer star SATZ [C]; δ=1−q^dagger=−sch with c'=1. |
| r433 companion | CERTIFIED | MELLIN_PICK_LEE_YANG | `rh/problem/edge_redheffer.tex` | R→R^dagger is the terminating 2×2-block Redheffer star SATZ [C]; δ=1−q^dagger=−sch with c'=1. |
| r433 companion | CERTIFIED | MELLIN_PICK_LEE_YANG | `rh/problem/verify_edge_redheffer.py` | R→R^dagger is the terminating 2×2-block Redheffer star SATZ [C]; δ=1−q^dagger=−sch with c'=1. |
| r434-r475 | PROVED | TOEPLITZ_MOMENT_POSITIVITY | `rh/lean/RH/InnerBridges.lean` |  |
| r435 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_p1_overload.py` | n_-(A0)≤1 is a crossing budget of the nested μ-CD chain SATZ [C]; dictionary n_-=n_C(N_w-3). |
| r436 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_p2_determinant.py` | det K2=det(K2_+)−Q reverse-CS SATZ [C]; drop-ψ_- kills P2; alternation matches r377. |
| r438 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_evolutionary_cert.py` | Search negatives named [C]; truncation nC=2 is r395, not a two-case falsifier. |
| r439 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/residual_loewner_probe.py` | rank(YD0-D0Y)=2 exact; S0=K_YY^{-1}; D0 itself is not ones-Loewner [C]. |
| r439 companion | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/residual_loewner.pdf` | Disp rank 2, S0=K_YY^{-1}, and dressed Loewner at kdim=0 are SATZ [C]. |
| r439 companion | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/residual_loewner.tex` | Disp rank 2, S0=K_YY^{-1}, and dressed Loewner at kdim=0 are SATZ [C]. |
| r439 companion | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/verify_residual_loewner.py` | Disp rank 2, S0=K_YY^{-1}, and dressed Loewner at kdim=0 are SATZ [C]. |
| r440 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_mean_tau.py` | T1/T2/MI2 SATZ [C]; selected+core mean 0<1; dead χ have κ^dagger=1; collar of s=1 quantified. |
| r441 companion | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/verify_diag_lifts.py` | Dressed Cauchy Gram PSD and lift-count n_-(W_Y−K^{-1})=#{λ(W^{1/2}KW^{1/2})<1} SATZ [C]. |
| r442 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_block_mean.py` | κ^dagger=1{q^dagger>1} SATZ [C]; selected+core pointwise living (q^dagger<1) [C]. |
| r443 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_delta_floor.py` | δ=R+τ-correction chart SATZ [C]; floor preferred only on the k=5..9 slice [C]. |
| r444 companion | CERTIFIED | RHP_IIKS_TAU | `rh/problem/verify_signed_border.py` | Triple-sum expansion SATZ [C]; pole share ≤0.003 is not the living-mean carrier. |
| r445 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_deep_builder.py` | Skip-Lanczos atoms bitwise-identical [C]; k=8 live confirms the r421 pin; slice floor still preferred. |
| r446 | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/deep_abd_probe.py` | First flip n=3788 bit-identical at dps 40 and 60; not a float64 artefact [C]. |
| r446 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/deep_abd.pdf` | k=10/11/12 breaks are REAL at dps 40/60 [C]; last observed living window is kz136. |
| r446 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/deep_abd.tex` | k=10/11/12 breaks are REAL at dps 40/60 [C]; last observed living window is kz136. |
| r446 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_deep_abd.py` | k=10/11/12 breaks are REAL at dps 40/60 [C]; last observed living window is kz136. |
| r447 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_exact_atom.py` | Exact k=10 atoms agree with float64 to one ulp [C]; flip at n=3788 is dps-stable; family does not feed frequently. |
| r448 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_exact_band.py` | Float mesh ends at kz136 [C]; kz197 is an in-chain ζ-death; next-odd dies at k=10. |
| r449 companion | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_flip_vs_stab.py` | Every measured chain flip sits past n_stab [C]; prefix-80 q^dagger lives; no anti-RH candidate. |
| r450 companion | CERTIFIED | OPERATOR_SPECTRAL | `rh/problem/verify_prefix_mincut.py` | n_stab-compression of R^dagger is the frequently-cone (Iff.rfl) [C]; χ prefix lives while full χ stays edge-dead. |
| r452 | PROVED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/plateau_theorem_probe.py` | Plateau identity proved; constancy ⇔ rho_n=0; sister 136/137 kills an a-law [C]. |
| r452 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/plateau_theorem.pdf` | Plateau identity q_*=M_d/(M_d+5/7) on kz≥69. [C] Whether M_d unbounded stays open. |
| r452 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/plateau_theorem.tex` | Plateau identity q_*=M_d/(M_d+5/7) on kz≥69. [C] Whether M_d unbounded stays open. |
| r452 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_plateau_theorem.py` | Plateau identity q_*=M_d/(M_d+5/7) on kz≥69. [C] Whether M_d unbounded stays open. |
| r453 | PROVED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/border_mass_probe.py` | q_n<1 ⇔ rho_n<5/7; err/margin ≤3e-5 on the plateau [C]. |
| r453 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/border_mass.pdf` | Bound and fixed-n race proved; M_d is folded m_0 growing with log N. [C] |
| r453 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/border_mass.tex` | Bound and fixed-n race proved; M_d is folded m_0 growing with log N. [C] |
| r453 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_border_mass.py` | Bound and fixed-n race proved; M_d is folded m_0 growing with log N. [C] |
| r453-r463 | CERTIFIED | LEAN_FORMALIZATION | `rh/problem/interval_cert.tex` |  |
| r455 | PROVED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/arch_chain_probe.py` | [L1] elementary via c^P_i=0 before log 2; [L3] h>0 classical; not RH-circular [C]. |
| r455 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/arch_chain.pdf` | L3 proved classically; L1 elementary and not RH-circular. [C] |
| r455 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/arch_chain.tex` | L3 proved classically; L1 elementary and not RH-circular. [C] |
| r455 companion | PROVED | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_arch_chain.py` | L3 proved classically; L1 elementary and not RH-circular. [C] |
| r458-r465 | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/interval_cert_probe.py` |  |
| r459-r463 | CERTIFIED | LEAN_FORMALIZATION | `rh/problem/verify_interval_cert.py` |  |
| r463/r638L | CERTIFIED | LEAN_FORMALIZATION | `experiments/tfpt-discovery/lean_fidelity_probe.py` | FaithfulFold replaces raw-atom cosine fold; endpoint renamed internal_weil_nonneg_of_frequently_selected [C]. |
| r464/r638L | PROVED | LEAN_FORMALIZATION | `experiments/tfpt-discovery/inner_bridges_probe.py` | Finite implication exact selected-window QR + A_cap PSD ⇒ plain-read ≥0 proved [C]. |
| r471 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/classical_cert_probe.py` | Grid positivity certified through L_16=2.7726 [C]; L=0.8 and Yoshida/Bombieri L=0.30 green. |
| r471 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/classical_cert.pdf` | Grid Q_L certified through L_16=2.7726; scramble-sensitive. [C] Not λ_*. |
| r471 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/classical_cert.tex` | Grid Q_L certified through L_16=2.7726; scramble-sensitive. [C] Not λ_*. |
| r471 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_classical_cert.py` | Grid Q_L certified through L_16=2.7726; scramble-sensitive. [C] Not λ_*. |
| r475 | PROVED | EXPLICIT_FORMULA_IDENTITY | `rh/problem/arch_rate.pdf` | weilArchSide concrete; O(Δ^2) rate named; selectedArchError→0 at fixed f. [C] |
| r475 | PROVED | EXPLICIT_FORMULA_IDENTITY | `rh/problem/arch_rate.tex` | weilArchSide concrete; O(Δ^2) rate named; selectedArchError→0 at fixed f. [C] |
| r475 companion/r638L | PROVED | EXPLICIT_FORMULA_IDENTITY | `rh/problem/verify_arch_rate.py` | weilArchSide concrete; O(Δ^2) rate named; selectedArchError→0 at fixed f. [C] |
| r475/r638L | PROVED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/arch_rate_probe.py` | productionArchDelta_tendsto_atTop proved; remnant O(Delta_k^2) along selected sequence [C]. |
| r476 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/crossterm_probe.py` | H^2-ball positivity unconditional through L_16 [C]; YB gate PASS. Not lambda_*(L)>=0. |
| r476 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/crossterm.pdf` | All 12 schedule points H2BALL_POS through L_16; YB PASS. [C] Not λ_*. |
| r476 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/crossterm.tex` | All 12 schedule points H2BALL_POS through L_16; YB PASS. [C] Not λ_*. |
| r476 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_crossterm.py` | All 12 schedule points H2BALL_POS through L_16; YB PASS. [C] Not λ_*. |
| r494 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kernel_loewner_probe.py` | Fixed-support floor Q_W>=2.1e-3 //h//_2^2 at L=0.3 [C]/finite theorem. |
| r494 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_loewner.pdf` | Operator floor sealed at c=2.1e-3 at L=0.3. [C] Later v1017; not [E]. |
| r494 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_loewner.tex` | Operator floor sealed at c=2.1e-3 at L=0.3. [C] Later v1017; not [E]. |
| r494 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_kernel_loewner.py` | Operator floor sealed at c=2.1e-3 at L=0.3. [C] Later v1017; not [E]. |
| r495 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kernel_redteam_probe.py` | Adversarial audit confirms c=2.1e-3 [C]; five tests to 5.7e-21; 6/6 Q-exact shifts. |
| r495 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_redteam.pdf` | Outward floor 2.122e-3; false world correctly negative; HS blocks included. [C] |
| r495 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_redteam.tex` | Outward floor 2.122e-3; false world correctly negative; HS blocks included. [C] |
| r495 companion | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_kernel_redteam.py` | Outward floor 2.122e-3; false world correctly negative; HS blocks included. [C] |
| r537 | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/honest_contour_audit_probe.py` | All identities confirmed within truncation [C]; no Lean definition bug. |
| r543 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborIntegral.lean` | pureGaborHat_integral_representation sorry-free [E]; one r542 classical input closed. |
| r546 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/ZeroIncrement.lean` | zeta_unit_increment and gaborIncrementBound_holds sorry-free [E]; Path A increment is a theorem. |
| r548 | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/weil_gabor_explicit_formula_probe.py` | Classical identity confirmed 36/36 [C]; Lean (1+1/n) is a false contour inversion. |
| r552/r579 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborThetaBound.lean` | Discrete density transfer sorry-free [E]; Theta_lobe(a)=3+2*Sum exp(-m^2/2a). |
| r555/r587 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborHatAnalytic.lean` | Entirety, hat_W(1-s)=hat_W(s), three-lobe bound, Gaussian strip decay sorry-free [E]. |
| r557 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborHorizontalEdges.lean` | gabor_horizontal_edges_tendsto_zero proved [E]; remainders named not sorry-asserted. |
| r557/r587 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborZeroSummable.lean` | summable_gaborHat_over_zeros and quartic variant theorems [E]. |
| r557/r631L | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborContourResidue.lean` | gabor_contour_identity_fixed_T sorry-free [E]; GaborContourLimitRemainder later a theorem. |
| r570 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborLeftVertical.lean` | Left vertical closed sorry-free [E]; of_parts reduced to (hlim,harch,hhalf). |
| r572 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborAutocorrelation.lean` | ACF closed form and GaborHalfCombReal sorry-free [E]; of_parts to (hlim,harch). |
| r574/r575/r597/r598 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborDominanceLog.lean` | Counting => log-compliance proved; GaborDominanceBoundLog a theorem [E]. |
| r576 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborVerticalLimit.lean` | gaborContourVerticalLimit_holds sorry-free [E]; of_parts reduced to (harch). |
| r578/r581 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborArchContour.lean` | gaborArchCriticalPairingReal_holds and gaborArchContourShift_holds [E]. |
| r582/r583/r589/r597 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborDominanceLog2.lean` | GaborDominanceBoundLog2 theorem [E]; axioms only propext/choice/Quot.sound. |
| r582/r585 | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborFEMultiplicity.lean` | riemannZetaMultiplicity_eq_one_sub_all and window sum <= 2*C_inner*(1+log(/N/+3)) [E]. |
| r612C/r634L | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/GaborCountableCriterion.lean` | Unconditional; #print axioms = propext/choice/Quot.sound. Rational and real pure-Gabor iff RH [E]. |
| r617 | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/e8_coxeter_euler_completion_probe.py` | Tr C=-1; Phi_30 Moebius; D_E8 residuals 1.28e-4 / 3.5e-14 [C]. Analytic RH-split fenced. |
| r617L | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/CoxeterCompletion.lean` | Algebraic core sorry-free [E]; axioms propext/choice/Quot.sound only. |
| r617L | PROVED | LEAN_FORMALIZATION | `rh/lean/RH/PrimeLogIndependence.lean` | Full Q-linear independence of {log p} [E]; Mathlib had no such lemma. |
| r628 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/window_box_verifier_probe.py` | lambda_min>=1.05e-7 (L=0.55,N=24,{2,3}) through 9.3e-17 (L=0.80,N=40,{2,3,4}) [C]. |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/adaptive_scaling_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/alignment_eta_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/angle_floor_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/anthropic_moment_inertia_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/anthropic_ranktrace_core_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/arbiter_assembly_precision_probe.py` |  |
|  | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/archimedean_pi_conformity_result.json` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/b_christoffel_deflation_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/baez_duarte_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/ball_arithmetic_head_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/ball_arithmetic_ladder_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bare_wing_bound_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/beurling_nyman_gram_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bfloor_christoffel_congruence_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/bfloor_k5_closure_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bfloor_node_congruence_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/bfloor_perstep_certification_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/bfloor_pg_dominance_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/bigpicture_logic_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bilinear_sieve_probe.py` |  |
|  | PROVED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/blockreal_lemma_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bottom_floor_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/boundary_decay_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/boundary_formulation_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/bulk_remainder_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/capacity_inequality_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/cased_replicate_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/certified_head_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/certified_ladder_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/certified_ladder_tail_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/chain_audit_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/christoffel_energy_lemma_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/classical_closure_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/conductance_profile_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/continuous_cone_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/continuum_det_law_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/continuum_extension_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/core_fluctuation_normalform_probe.py` |  |
|  | PROVED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/correlated_cancellation_probe.py` |  |
|  | CERTIFIED | ARAKELOV_HODGE_INTERSECTION | `experiments/tfpt-discovery/coupling_currency_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/cp_extension_gate_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/cp_invariant_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/cross_lemma_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/curvature_bridge_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/damping_cert_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/deep_alpha_sign_probe.py` |  |
|  | PROVED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/deep_rate_mechanism_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/deep_zone_stress_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/dense_limit_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/directional_defect_correction_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/directional_floor_density_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/directional_lanczos_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/dk_recursion_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/door_a_spectral_polarization_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/driver_cert_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/e8_ramified_jetcode_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/epsilon_theorem_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/epstein_collapse_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/etasource_kyp_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/euler_operator_lift_probe.py` |  |
|  | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/eulerpick_ladder_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/exact_form_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/excess_certified_skeleton_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/exclusion_battery_v2_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/exclusion_ladder_deep_probe.py` |  |
|  | CERTIFIED | OTHER | `experiments/tfpt-discovery/exclusion_ladder_saturation_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/exterior_pg_renormalized_probe.py` |  |
|  | CERTIFIED | OTHER | `experiments/tfpt-discovery/exterior_pg_schur_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/extremal_window_budget_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/final_map_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/finite_harmonic_certificate_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/frame_beyond_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/frame_rate_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/friedrichs_angle_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/g2_lawwall_asymptotics_probe.py` |  |
|  | CERTIFIED | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/garding_minorant_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/grand_assembly_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/green_align_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/green_asymptotic_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/green_decay_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/h1h2_envelope_derivation_probe.py` |  |
|  | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/halfgap_riccati_increment_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/halfgap_riccati_transition_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/hardness_calibration_falsification_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/harnack_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/hausdorff_safepoint_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/hecke_constant_depth_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/instrument_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/j16_verified_zero_supply_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kappa_deep_seams_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/kill_atlas_dag_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kr4_defectjet_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kr4_depth_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/krein_normalform_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/ks_carrier_formula_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/ks_dual_rigor2_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/ks_dual_rigor3_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/ks_dual_rigor_probe.py` |  |
|  | PROVED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/lambda_equivariant_design_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/lemma_window_proof_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/level_lemma_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/li_corollary_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/li_lemma_attack_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/limit_operator_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/lk_split_theta_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/local_factor_nogo_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/long_lag_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/lowfreq_discrepancy_gain_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/m_matrix_pair_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/margin_free_step_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/margin_law_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/margin_propagation_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/mazya_proof_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/mode_ladder_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/monotone_composition_probe.py` |  |
|  | CERTIFIED | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/moonshot_arch_glue_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/moonshot_hecke_groupoid_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/mt_window_family_probe.py` |  |
|  | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/multilevel_telescope_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/multiplicative_sign_source_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/net_balance_repair_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/null_vector_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/odd_channel_closure_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/odd_ladder_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/oddtoeplitz_pole_branch_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/oscillation_mass_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/pairing_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/pareto_front_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/pencil_ratio_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/pg_chain_interval_rollout_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/pgram_directional_schur_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/phase_placement_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/phase_polygon_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/phys_ramified_ns_r_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/pi_resonance_anatomy_probe.py` |  |
|  | CERTIFIED | SELBERG_TRACE_CONTACT | `experiments/tfpt-discovery/pinch_attack_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/pole_free_floor_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/port_bfloor_uniformity_probe.py` |  |
|  | PROVED | LEAN_FORMALIZATION | `experiments/tfpt-discovery/positive_descent_master_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/prime_floor_theorem_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/prime_lagrange_pair_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/psi4_block_model_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/psi_ladder_probe.py` |  |
|  | CERTIFIED | OTHER | `experiments/tfpt-discovery/qgeo_fourier_logsum_probe.py` |  |
|  | CERTIFIED | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/qgeo_h1_candidate_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/radau_class_assembly_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/radau_sos_certificate_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/ratio_certificate_probe.py` |  |
|  | PROVED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/recipe_coherent_avoidance_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/relation_corner_ladder_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/relative_flag_margin_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/residual_quadrature_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/rh_leverage_probe.py` |  |
|  | CERTIFIED | OTHER | `experiments/tfpt-discovery/rho_margin_derivation_probe.py` |  |
|  | CERTIFIED | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/roadmap_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/schoenberg_core_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/schur_cascade_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/schur_entry_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/schur_profile_bound_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/schur_profile_chain_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/schur_transport_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/schur_ward_identity_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/sector_change_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/self_supply_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/selfdual_construction_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/separation_floor_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/sharp_capacity_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/shift_average_deep_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/shift_average_hh_audit_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/sieve4_eulerpick_n4_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/signed_only_nogo_probe.py` |  |
|  | CERTIFIED | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/simple_principle_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/squarelock_adjudication_probe.py` |  |
|  | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/stage1_construction_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/strat2_pinning_lemma_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/structural_cbs_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/subgamma_fourier_bound_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/symbol_lemmas_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/szego_bottom_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tail_abel_transport_probe.py` |  |
|  | PROVED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tail_correlation_lemma_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tail_difference_envelope_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tail_oscillation_pairing_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tail_segment_split_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tail_sign_mechanism_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/tail_sign_repair_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/teml_probe.py` |  |
|  | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/third_split_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/threebounds_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/transport_ledger_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/twelve_by_eight_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/two_inequalities_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/ub4_congruence_upgrade_probe.py` |  |
|  | CERTIFIED | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/ub4_identity_or_measurement_probe.py` |  |
|  | CERTIFIED | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/vbk_invariant_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/w1_assembly_certificate_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/w1_christoffel_floor_probe.py` |  |
|  | PROVED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/w2_exact_transport_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/w2_full_zero_closure_probe.py` |  |
|  | CERTIFIED | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/waldspurger_canonical_measure_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/wall_cut_schedule_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/wall_edge_completion_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/wall_gram_radau_probe.py` |  |
|  | CERTIFIED | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/wall_head_tail_bound_probe.py` |  |
|  | CERTIFIED | LATTICE_E8_HECKE | `experiments/tfpt-discovery/wall_matched_asymptotics_probe.py` |  |
|  | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/wall_pole_exactness_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/wedge_scale_law_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weight_smoothing_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/wide_window_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/z1_trace_operator_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/zero_window_bootstrap_probe.py` |  |
|  | CERTIFIED | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/zeroframe_unification_probe.py` |  |
|  | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/zeroframe_uniform_bound_probe.py` |  |
|  | CERTIFIED | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/zolotarev_phase_filter_probe.py` |  |
|  | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/zone_extension_proof_probe.py` |  |
|  | PROVED | LEAN_FORMALIZATION | `rh/catalog/test_proof_search.py` |  |
| 2026-09-09-arch-source-reconciliation | PROVED | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/ArchRateClosure.lean` | SelectedArchWeightedInterpolationEstimate, SelectedArchErrorQuadraticRateExists and selectedArchError_tendsto_zero hold without extra hypotheses, using only standard Lean axioms. Each constant may depend on the fixed test. |
| 2026-09-09-frontier-source-reconciliation | PROVED | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/FrontierClosure.lean` | Under FREQ, the eventual selected read lower bound is equivalent to nonnegativity of native weilForm on every GridElement. No convergence assumption remains. |
| CENSUS.QSM.NORMFLOW.01 | CERTIFIED | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/census_qsm_normflow_probe.py` | Bridge 1 is constructed as a standard GL4 Gaussian arithmetic QSM with TFPT-selected module input [C]. |
| MELLIN.PICK.CUSP-SADDLE.01 | PROVED | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_cusp_saddle_probe.py` | Closed right outer half-plane Re q≥0, /q/≥R0 certified; identity theorem used [C]. |
| MELLIN.PICK.CUSP-SADDLE.01 | PROVED | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_cusp_saddle_result.json` | OUTER_DOMAIN_PROVED; mapped repo-M domain Re s≥0, /s/≥2 R0 [C]. |
| PRIME.POSITIVE.CONE.BLINDNESS.01 | PROVED | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/positive_cone_blindness_probe.py` | Nu-scaling-invariant positive-cone certificates are structurally insufficient; a metric comparison or operator bridge is required [C]. |
| WEIL.WINDOW.CERTIFICATE.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_window_certificate_probe.py` | Even T=200 first eigenvalue in paper interval; c≈1.027689e-17 [C]. |
| WEIL.WINDOW.CERTIFICATE.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_window_certificate_result.json` | CERTIFIED(1.027689e-17); miller_seeds=rigorous_power_series [C]. |
| doc-sweep | PROVED | WEIL_POSITIVITY_WINDOWS | `experiments/lean4-carrier-rigidity/TfptCarrier/DenseWeilCore.lean` | Section or narrative surface indexed; no new certificate. |
| doc-sweep | PROVED | WEIL_POSITIVITY_WINDOWS | `experiments/lean4-carrier-rigidity/TfptCarrier/WeilDictionary.lean` | Section or narrative surface indexed; no new certificate. |
| ledger:E8.DIRECTED.READOUT.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v1018_e8_directed_readout.py` | Proven finite statement [E] (Identity, exact over Z/Q via sympy); C7 Gauss-code transform stays OPEN (rem:c7-audit); NO RH claim |
| ledger:HECKE.CARRIER_CHECK32.01 | PROVED | LATTICE_E8_HECKE | `verification/v785_hecke_check32.py` | Theorem-grade [E] congruence modulo the one cited Sturm ingredient (verified 25000x beyond the bound); the 32 = 2^g_car reading typed OBSERVATION; Lean kernel companion Check32.lean; no marker move (Python-only per GATE.WOLFRAM.02). |
| ledger:HECKE.GEOM.01 | PROVED | LATTICE_E8_HECKE | `verification/v535_hecke_from_geometry.py` | Identity [E] (exact integer/Rational/sympy: Kneser counts, (a,b)/lambda laws, dim-7/projector/oldform arithmetic + live p=3 geometry; Wolfram-mirrored exact identities) + [C] (p=5 geometric S[1] as T31-validated freeze) + [O] (weight-4 -> GL(1) transport); NO marker moves |
| ledger:HECKE.GEOM.EICHLER.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v536_eichler_trace_layer.py` | Identity [E] (exact integer/sympy: Witt lambda_Eis, N_perp, N_A/N_B densities, assembler R=a_p^2, signed Shell(p) a_p, live p=3 type-(ii); Wolfram-mirrored exact identities) + [C] (p=5 type-(ii) as T36-validated freeze; p>=7 two-sided via closed forms) + [O] (weight-4 -> GL(1) transport); NO marker |
| ledger:HECKE.GEOM.HALFINT.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v537_halfintegral_bridge.py` | Identity [E] (exact integer: Shimura uniqueness at scale -8, T(p^2) equivariance, U4(g)=0 / Kohnen scope fence; Wolfram-mirrored exact a_p/scale/scope/root-number identities) + [C] (AFE-numeric Waldspurger constancy, measured R); NO marker moves |
| ledger:HECKE.GEOM.RTF.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v538_relative_trace_identity.py` | Identity [E] (exact integer/Rational/sympy: bilateral Tr_V(nu_p o pi), orbit dictionary lambda_Eis+a_p^2, closed nu_law anchors; Wolfram-mirrored exact R1/R2 arithmetic) + [C] (AFE-numeric Waldspurger R3 / measured R; lattice enumeration exact); NO marker moves |
| ledger:HECKE.HALVINGTAILS.01 | PROVED | LATTICE_E8_HECKE | `verification/v795_halving_tails_k5.py` | Exact [E] termwise-divisibility identities and census-clean tower determinism (10^6, zero exceptions) modulo the named h = 1 / Gauss ingredients (instances machine-verified); the class-1 single-character bridge and the governing-field derivation typed OPEN (Cohn-Lagarias frame cited); the run-1 census catch and |
| ledger:HECKE.MULTIRATE2ADIC.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v789_multirate_constdepth.py` | Theorem-grade [E] ladder modulo two cited classical ingredients (Sturm; twist lemma) with census-level sharpness; the constant depths for classes 3 and 5 mod 8 PROVEN modulo the two named h = 1 representation theorems (instances machine-verified); the 32 -> 256 |
| ledger:HECKE.POSITIVE_C2_LIFT.01 | PROVED | LATTICE_E8_HECKE | `verification/v788_positive_c2_lift.py` | Theorem-grade [E neu] positive decomposition and automaton algebra modulo the typed classical citations (each machine-verified far beyond Sturm); the sheet-parity readings [C neu] fenced; Lean kernel companion PositiveC2Lift.lean; no marker move (Python-only per GATE.WOLFRAM.02). |
| ledger:HECKE.SNF_THETA.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v790_snf_mu4_theta.py` | Exact [E] representation/SNF identities with the isometry census honestly EMPTY (fingerprint typing); the new csig identity exact [E-candidate] with the -8 = -rank(E8) tie; the all-shell vanishing claim adjudicated FALSE; no marker move (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.ABELPAIR.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v761_atom_pole_abel.py` | Exact [E] symbolic/matrix identities + [MEASURED] unconditional finite-range bound; honest control-standard derivation; the parent's preregistered ABEL-DEAD documented (sympy mandated for the certificate). |
| ledger:PRIME.ANTIALIAS.01 | PROVED | TOEPLITZ_MOMENT_POSITIVITY | `verification/v760_antialias_exact.py` | Exact [E] quadrature identities + designed must-fail witnesses; Lean companion module (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.BAEZDUARTE.01 | PROVED | TOEPLITZ_MOMENT_POSITIVITY | `verification/v667_baez_duarte.py` | Exact [E-mp] Vasyunin/C_BD anchors + [MEASURED] ladder, corridor (recalibrated, documented) and frame comparison + [C] typed reading (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.BLOCKDEFL.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v670_w3_block_deflation.py` | Exact [E] block wiring + anchors + [MEASURED] honest double MISS (fidelity + predicate) with the leak-ladder failure record + [C] typed reading (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.CANCELLATION.FUNCTIONAL.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v951_cancellation_functional.py` | Certified finite theorems + exact structural identity [E] (fine types Formal (the convolution/wraparound/Laplace algebra sympy-generic; the ACF/pole/arch laws at h = 4, 5 recomputed on an own wall build; the KD digamma limit recomputed at L = 80) and Numerical |
| ledger:PRIME.CAPCHAIN.IDENT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v546_capacity_chain_identities.py` | Identity [E] (matrix / interval-geometry identities at rel 1e-16..1e-12 with mutation controls, per-instance theorems with checked hypotheses, and per-window certified inequalities by completed Cholesky with the direction in the name); the c_0 of item (5) is MEASURED at the minimiser's |
| ledger:PRIME.CELLCONE.KERNELFIELD.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v851_cluster_kernel_field.py` | Honest split verdicts under the frozen preregistered protocols [typed evidence line: 15 + 10 + 7 checks with the SIX frozen-honest FAILS S3.2/S4.1 (connectivity/scramble: the cluster weights are position-geometric, the corner route closes) and S2.C1/S2.C2/S4.C1/S4.C2 (all four must-break kernel/field controls |
| ledger:PRIME.CENSUS.SPECTRAL.LIFT.01 | PROVED | LATTICE_E8_HECKE | `verification/v946_census_krein_pencil.py` | Certified finite theorems + partial-lift record [E] (fine types Formal (the MDL/Krein-assembly/transform lemmas + the E1/E2 identity chain recomputed in-run on exact instances; probe: dyadic-exact E1, integer-Bareiss E2 at h <= 13) and Numerical (the six-rung ladders, c_0/A_0 and ENVJ |
| ledger:PRIME.CERTROOT.01 | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `verification/v758_simpler_certificate.py` | Exact [E] anchors + [MEASURED] ladder-wide negatives; honest keystone typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.CHANNELINT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v742_channel_interference.py` | Exact [E] Ward identities + [MEASURED] collective balance anatomy over 35 windows (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.CHEBLOEWNER.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v576_cheb_loewner_edge.py` | Identity [E] + typed compression [C] (exact formulas and series coefficients; the bridge typed; regimes B/C open) |
| ledger:PRIME.CLOSEDDELTA.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v588_closed_delta.py` | Exact [E] + measured census [M] (G machine-exact; near-field window declared; tolerances declared) |
| ledger:PRIME.COMMUTANT.SOS.01 | PROVED | RHP_IIKS_TAU | `verification/v836_commutant_sos_closure.py` | Exact rational closure certificates [Identity-grade certificates, float achievability legs typed]: the degree-2 abelian-commutant SOS ansatz has a UNIQUE feasible point = the trivial diagonal rewriting (exact LP), and the rank-3 det form admits NO flag-space Gram representation (forced G = |
| ledger:PRIME.CORNER.OPENDOORS.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v837_corner_closure_quantifier.py` | Measured/typed evidence line under the frozen preregistered protocols [E-grade exact wards (Fractions group-algebra Fourier, exact ring duals), float window legs typed]; the closure is a typed route decision -- the structural half kernel-checked in TfptCarrier/SectorPositiveDescent.lean with IdentificationPositivity the single named |
| ledger:PRIME.COUNTING.DOMINANCE.CLOSURES.01 | PROVED | SCREW_SUBORDINATION_LSTAR | `verification/v921_counting_dominance_closures.py` | Certified finite theorems [E] (fine type Formal, certified-finite; Theorems M/E/T/C unconditional (counting logic + exact inequalities, recomputed on exact instances); Theorem A CONDITIONAL on H-pin (typed, closed forms recomputed); T1/T3 classical-citation closures (HSW22/RvM/PT21; Landau/Gonek cited AS FORM with >= 500x |
| ledger:PRIME.CP.EXTENSION.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v794_cp_extension_gate.py` | Measured/typed [MEASURED] net properties and deep margin trends under frozen preregistered gates (two declared run-1 -> run-2 repairs carried honestly: the S2 transcription bug caught by its own ward, the N3 pole-growth recalibration); the exact limit object typed (Z1-COMPACTNESS sector-decorated); |
| ledger:PRIME.CUTOFF.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v593_cutoff_completion.py` | Exact [E] + measured [M] (closed forms exact; comparisons at declared windows) |
| ledger:PRIME.DENSE.LIMIT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v562_dense_limit_identities.py` | Identity [E] (per-instance identities and certified inequalities with the direction in the name -- the Feynman-Hellmann identity exact at the U-minimum of a declared step ladder (2.3e-7 at delta = 1e-6; mutations miss by 4.0e1 while the true form sits |
| ledger:PRIME.DENSECORE.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v762_dense_weil_core.py` | Exact [E] enumeration/closure certificates in Q + [MEASURED] density rates; Lean companion module; honest analytic remainder (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.DETLAW.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v592_continuum_det_law.py` | Exact [E] + measured [M] + conditional certificate (symbolic exact; ladder at declared windows) |
| ledger:PRIME.DOUBLELIMIT.REDUCTION.THEOREM.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v918_doublelimit_reduction_theorem.py` | Certified finite theorem [E] (fine type Formal, certified-finite; exact algebra + elementary series + cited classical inputs (Vitali/Cauchy, Cauchy-Hadamard, B. Simon Trace Ideals Thm 2.21 class, round-122 NF-closure); measured ladders pinned and typed MEASURED; L1/WPD legs typed OBSTRUCTED/OPEN and NOT |
| ledger:PRIME.EULERPICK.CERTIFIED.FLOORS.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v915_eulerpick_certified_floors.py` | Certified interval floors [E] (fine type Numerical, certified-finite, outward-rounded intervals; citations disclosed: Buethe 2018 + Rosser--Schoenfeld 1962 + Nair 1982 + Rump 2010; PINNING DISCLOSURE: N <= 3 floors + wards + models recomputed in-run, the cap-10^13 N = 4 |
| ledger:PRIME.FEJERDENS.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v669_fejer_density.py` | Exact [E] identity (derived + verified) + [ANALYTIC, cited] unconditional chain + [E-candidate] finite zero-free certificates + [C] typed floor (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.FEWATOM.REDUCTION.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v953_fewatom_reduction.py` | Certified finite theorems + KA-scoped measured headline [E] (fine types Formal (the h = 4, 5 continuum Sturm certificates -- exact dyadic Fractions, Chebyshev conversion, INTEGER primitive-PRS chain, no floats; the one-line mechanism implication; the budget resplit; the KC un-normalized |
| ledger:PRIME.FLIPMECH.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v619_flip_mechanics.py` | Measured (declared surface) + [E] exact saturation census + injection mechanism + must-fail control |
| ledger:PRIME.FRAME.DEFICIT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v560_frame_deficit_identities.py` | Identity [E] (per-instance identities and certified inequalities with the direction in the name -- the identity transfer exact on a frame-B and a non-prime-power instance (KMS/Schur pair 3.2e-16, lag-sum 1.4e-16, R4-free det collapse at 0.020 of its conditioned bar, additive |
| ledger:PRIME.GARDENV.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v663_garding_envelope.py` | Exact [E] derived bound validity + [MEASURED] a-uniform envelope and quantified breaking point + [C] named Fejer remainder (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.GLUEDETECT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v750_simpler_gluing.py` | Exact [E] detector construction + honest falsification of the rigidity thesis (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.GONEK.PRICING.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v934_gonek_pricing_unconditional.py` | Certified statements + census pricing [E] (fine types Formal (GP2/GP3 envelope closed form + symbolic absorption, exact sympy recomputed in-run; the conditionality ledger + loop graphs recomputed) and Numerical (the spike/DC/WF/control tables pinned from the 20M-zero record); the constant typed |
| ledger:PRIME.GROUND.RESIDUE.OBS.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v944_ground_residue_observability.py` | Certified finite theorems + observability record [E] (fine types Formal (the residue/Feshbach/CDLI/interlacing/displacement exact layer recomputed in-run) and Numerical (the 14-rung identity/gap/overlap/margin/witness/alt-jet ladders pinned and typed MEASURED); THE BH9-K1 MAJOR CORRECTED WORDING adopted verbatim on every surface of this row (WALL-OFF-DIAGONAL-IS-ONE-FUNCTION-LOEWNER-EXACT |
| ledger:PRIME.GROUNDTRUTH.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v668_ground_truth.py` | Exact [E] ground-truth laboratory (both controls) + [MEASURED] calibration profile + [C] typed W3 recalibration (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HANDOFFBULK.01 | CERTIFIED | OPERATOR_SPECTRAL | `verification/v766_handoff_bulk.py` | Exact [E] Ward/battery freeze machinery + [MEASURED] eps-robust convergence rates; the bare-inverse negative block and the wall quantified honestly (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HANDOFFGRAM.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v767_handoff_frequency_gram.py` | Exact [E] frozen construction (PSD by construction, byte-hashed source-before-target) + [MEASURED] convergence profile; declared single iteration documented (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HANDOFFREDTEAM.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v765_handoff_redteam.py` | Exact [E] static firewall audit + [MEASURED] control battery; the RT6 decision gated under a fresh preregistration; binding both-gate-families note (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HANDOFFRES.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v759_handoff_fixed_window_resolution.py` | Exact [E] q-invariance at rounding level; [MEASURED] classifier under frozen preregistered gates (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HANDOFFTAIL.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v768_handoff_tail_weil.py` | Exact [E] algebraic tail termination + [MEASURED] identification and compatibility under frozen preregistered gates; part-1 PARTIAL honest and on record, decided by the part-2 preregistration (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HECKEPOLARITY.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v753_ramified_polarity.py` | Exact [E] finite census/bijection (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HECKETWOSTEP.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v754_ramodd_twostep.py` | Exact [E] integer-matrix transport identity (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HODGECONE.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v627_hodge_chamber.py` | Exact [E] transport + [MEASURED] chamber/sheet + honest scramble typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.HOLECLOSED.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v681_coverage_hole.py` | Analytic adjudication (machine-checked) + Exact [E] budget-certified RS scan and hole floor + [E/ABSTRACT] exact-prime Weil chain (identity-verified) + [SYNTHESIS] gapless split-type map + [C] typed W2 end-state (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.INTERP.01 | CERTIFIED | SELBERG_TRACE_CONTACT | `verification/v688_interpolation_detector.py` | Exact [E] master identity (sine form) + [E/MEASURED] detection guarantee and full masking adjudication + [C] lemma with measured constants (inverted firewall, declared zero input; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.INTERPCLOSURE.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v694_interpolation_lemma_closure.py` | Exact [E] retention certificate + [MEASURED] form-corrected additive separation law + [C] near-proof typing with named residues (inverted firewall, declared zero input; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.K1CAPTURE.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v721_k1_node_capture.py` | Proof-near [E] capture chain (Markov-Stieltjes + symmetrized Christoffel + closed capture condition, SHA256 firewall) with the honest [M] adjudication: capture only, super-resolution = trace-formula content (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.KEIPERLI.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v665_keiper_li.py` | Exact [E] two-route consistency + closed forms + must-fail injection + honest tail budget (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.KERNELCLASS.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v687_extremal_kernel.py` | Exact [EXACT] sympy pinning + collapse certificates + [ANALYTIC, cited] Shannon sampling closure + [MEASURED] LP ladder confirmation + [C] false-PASS trap typing (AST zero-firewall; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.KMSSTINESPRING.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v756_kms_incidence_stinespring.py` | Exact [E] explicit Kraus construction with exact covariances (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.KRAUS.DOILY.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v811_prime_kraus_doily.py` | Exact [E] protocol-grade operator identities (integer/Z[i]/Fraction) + the certified Sp(4,2) obstruction; the commutant surprise and the spread non-invariance measured (report-only); one declared report-text repair (spec v2) |
| ledger:PRIME.KREIN.DEFECT_ONE.01 | PROVED | RHP_IIKS_TAU | `verification/v862_defect_polar_weld.py` | Honest structural localization under the frozen preregistered protocols [typed evidence line: 8/8 + 22/22 checks, zero fails; the v2 monomial-closure amendment typed in the frozen spec (the two-band corridor form found VACUOUS at fine scale -- the honest surprise first, |
| ledger:PRIME.L1IDENT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v727_l1_identification.py` | Classical [E] determinacy chain (damped moments identified, Carleman) + [M] PD-persistence typing of the wall (9/9 windows, finite Levinson decision each; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.L1MONTAGE.01 | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `verification/v713_l1_montage.py` | [MEASURED] assembled continuum candidate (cover limit 6.2e-8, D^2 mass rate, one UV slot) + [E] normalization repair of the 5b negative + honest naming of the missing theorems; AST zero firewall (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.L1WPD.CLOSURE.01 | PROVED | LATTICE_E8_HECKE | `verification/v937_l1wpd_closure_reduction.py` | Certified statements + consolidation [E] (fine types Formal (R1-R5 restatement licenses + linearity exhibits + the AND-fire closure, exact, recomputed in-run) and Numerical (the x_0/D_cs/d_1/MRB/bridge/eps-gap tables pinned; the replication legs digit-identical to the cited tables); the SW-HSW pricing typed VACUOUS-ADJUDICATED |
| ledger:PRIME.LEHMERNULL.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v671_lehmer_resonance.py` | Measured [E-float] pair statistics + clean h-controlled null with placement control and must-detect teeth + [C] typed reading (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.LICOROLLARY.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v672_li_corollary.py` | Exact [E] Laguerre derivation + window lock + pole cancellation + [MEASURED] 30/32 band table + [C] finite typing (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.LKSPLIT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v682_lk_split_theta.py` | Exact [E] sign-structure/assembly identities (AST zero-firewall) + [MEASURED] theta tables and the death mechanism + [C] circularity typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.LOOP.EQUIVALENCE.THEOREMS.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v920_loop_equivalence_theorems.py` | Certified finite theorems [E] (fine type Formal, certified-finite; all nine theorems exact algebra recomputed in-run (sympy generic + exact-rational/CRootOf/mp instances); per-rung tables pinned and typed MEASURED incl. the TIGHT delta_1 == FULLGAP lock; PINNING DISCLOSURE: r142 re-run green at promotion, |
| ledger:PRIME.LORENTZ.SPINOR.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v807_lorentz_nullselector.py` | Exact [E neu] spinor-square identities (sympy) + measured REVEAL (alpha-monotone 1D structure; the three frozen h-order gates fail honestly, encoded in the run gate) + exact [E] null-selector algebra with the seam-family theorem typed OPEN; carries the BOUNDARY.NULLSELECTOR addendum to |
| ledger:PRIME.MACROKERNEL.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v579_macro_kernel_signs.py` | Identity [E] + typed boundary [C] (kernel geometry exact and sign-verified; the arithmetic half open) |
| ledger:PRIME.MAPCLOSE.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v595_mapping_completion.py` | Exact [E] + measured identity-level match [M] (closed forms exact; declared windows) |
| ledger:PRIME.MARGIN.IDENT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v542_margin_chain_identities.py` | Identity [E] (exact interval geometry + dense linear-algebra identities at rel 1e-16..1e-13 with mutation controls; nine per-instance identities/theorems of the phase-2 margin chain) -- PER INSTANCE on small windows only, NOTHING uniform in the zone index; the kappa law itself |
| ledger:PRIME.MOONSHOT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v714_moonshot_hecke_groupoid.py` | Exact [E] tower facts (primitive degrees = Gaussian prime norms; de-divisorization 4e-13; sigma descent dev 0.00) with the E8-unspecificity fence typed and the declared ingredients named (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.MOONSHOT.03 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v717_moonshot_state.py` | Constructive [E] state exhibition on truncations (Levinson PD + binding identity 1e-12) + [M] Delta/KMS measurements; both control labs calibrate (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.MOONSHOT.05 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v719_moonshot_traceformula.py` | Exact [E] finite trace formula (Gauss quadrature 1.7e-11) + [E] closed term dictionary to the Weil formula + [M] Delta convergence rates + [E] 2-class E8 census (Mordell 1938 cited) (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.MOONSHOT.06 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v720_moonshot_k2k3.py` | [MEASURED] tightness + [E] unconditional tail majorant (Rosser-Schoenfeld verified in range) + exact slowdown law; the line s = 1/2 as the honest boundary (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.PACKET.RM14.01 | PROVED | LATTICE_E8_HECKE | `verification/v819_prime_packet_rm14.py` | Exact [E neu] code censuses (row hull, enumerators, cycle, CSS, triorthogonality) with Lean companion PacketRM14.lean (kernel-checked, 30 theorems); zeta8 pointer and TFPT fingerprints typed [H] |
| ledger:PRIME.PACKETGARD.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v674_packet_garding.py` | Exact [E] wiring/construction + [MEASURED] typed-residual central negative (inverted expectation) + frame/theorem link + Mosco battery + [C] named remainder (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.PASCAL.REGION.THEOREM.01 | PROVED | SCREW_SUBORDINATION_LSTAR | `verification/v914_pascal_region_theorem.py` | Certified finite theorem [E] (fine type Formal, certified-finite, verification-powered, FORM-LOCAL; citations disclosed: Platt--Trudgian 2021 Thm 1 + Hasanalizade--Shen--Wong JNT 235 (2022) Cor. 1.2 + Rosser 1941 Thm 19 + gamma_1 isolation; NOT an RH-evidence row -- says nothing about other |
| ledger:PRIME.PCANON.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v635_p_canonicity.py` | Exact [E] census/guards + [MEASURED] fine-invariant separation (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.PCONSTRUCT.01 | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `verification/v636_p_construction.py` | Exact [E] construction/normal form/census + documented must-fail (sympy exact; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.PINCHBREAK.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v680_pinch_attack.py` | Analytic thresholds (machine-checked on the comb) + Exact [E] Beurling-Selberg machinery and reach floors + [E/MEASURED] Selberg chain (identity-verified) + [CITED] literature block + [C] typed residue (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.PINLEMMA.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v730_strat2_pinning_lemma.py` | Proof-near [E] lemma pair (residual + Kato-Temple, one-line proofs, 0 violations everywhere incl. all 377 zeros of the largest window) + [M] width-saturation typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.POLERANKONE.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v591_pole_rank_one.py` | Exact [E] + measured law match [M] (symbolic algebra exact; ladder comparison at declared windows) |
| ledger:PRIME.PORT.BALLLADDER.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v897_certified_interval_ladder.py` | Proven finite statement [Numerical/certified]: rigorous interval shifts on all 42 rungs; the informal error model retired; no marker move |
| ledger:PRIME.PORT.CERTIFIED.LADDER.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v887_certified_ladder_complete.py` | Proven finite statement [Numerical/certified]: the complete head of the ladder; error model upgraded to rigorous interval shifts (v897); no marker move |
| ledger:PRIME.PORT.FACTORAVOID.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v895_collective_comb.py` | Decided law shape [Numerical]: one-sided spectral bound, collectively carried; no norm-bound route; no marker move |
| ledger:PRIME.PORT.TAU.01 | CERTIFIED | MELLIN_PICK_LEE_YANG | `verification/v883_tau_chain_parametrix.py` | Open contract [O] (the finite-identity level EXECUTED and carved out as PRIME.PORT.TAU.FINITE.IIKS.01 [E]; the fully symbolic arbitrary-h statement is the remaining demand) |
| ledger:PRIME.QFCENSUS.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v771_qf_representation_census.py` | Measured/typed evidence line under frozen preregistered gates [MEASURED] + exact [E]-typable label-side identities (incidence spectrum, canonicity census, sigma characters); the census outcome an honest preregistered OPEN; no marker move (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.QFFESHBACH.01 | CERTIFIED | OPERATOR_SPECTRAL | `verification/v772_qf_feshbach_effective.py` | Measured/typed evidence line under frozen preregistered gates [MEASURED] + exact [E]-typable Feshbach reconstruction and Herglotz certificates; the declared guard-normalization correction carried honestly in the provenance; no marker move (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.RANK3DENSITY.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v693_rank3_density_close.py` | Exact [E] refined envelope + [A-cited] explicit zero-density/count citations + [MEASURED] growth law + [C] honest scope (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.RANK3FUNC.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v683_rank3_functionals.py` | Exact [E] functional extraction (independent sieve cross-check, AST zero-firewall) + [MEASURED] circularity classes and CS/pretentious soundings + [C] typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.RANK3LOCKGRAM.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v692_rank3_lockgram.py` | Exact [E] decomposition + margin identity + superadditivity certificate + [A-cited] verification height + [C] honest partial-RH-tail typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.RANK3ZERO.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v684_rank3_zeroside.py` | Exact [E] explicit-formula identity + [E, declared input] budget-certified zero list (inverted firewall) + [MEASURED] unconditional kappa and zone mechanism + [C] typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.RDAGGER.KERNEL_LOEWNER.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v1017_kernel_loewner_positivity.py` | Proven finite statement [Numerical/certified]: float64 Gauss-Legendre + Chebyshev/Bernstein + HS tail (NOT interval arithmetic, NOT [E]); A2 translation identity exact over Q [Identity]; G2 Loewner algebra exact; floor 2.1e-3 with documented rounding headroom |
| ledger:PRIME.RIDGEOM.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v657_rid_alignment.py` | Exact [E] closed 2D formula + [MEASURED] angle-driven decomposition and honest controls + [C] typed W3 reduction (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.S1CANON.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v734_s1_canonical.py` | Exact [E] Krein correspondence (1.6e-15) + [M] H_h >= 0 witness on all 9 windows + [M] boundary-phase gluing at scale exactly 1 (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.SCHURREC.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v755_simpler_schur_recursion.py` | Exact [E] frame + [MEASURED] ladder positivity; honest equivalence typing (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.SECTIONEDGE.01 | CERTIFIED | OPERATOR_SPECTRAL | `verification/v707_chain_section_edge.py` | Exact [E] resolvent edge identity (3e-13) + [MEASURED] corridor-position census (median 0.534); AST zero firewall (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.SECULAR.GW.PINNING.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v919_secular_gw_pinning.py` | Certified finite theorem + per-rung certificate [E] (fine types Formal (secular identity, crossover, tail algebra -- exact) and Numerical (GW/gap/smallness tables -- certified per rung against cited PT21/HSW22 envelopes, PT21-warranted cache ordinates consumed by the probe only; the module consumes |
| ledger:PRIME.SHADOW.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v625_prime_shadow.py` | Exact [E] theta/Hecke/multiplicativity identities + [E-float] L-value + [C] the typed reading (integer convolution + sympy + mpmath) |
| ledger:PRIME.SIGNUNC.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v648_sign_uncertainty.py` | Exact [E] dictionary anchors (25 digits) + [MEASURED] typed negative and surface positivity + [C] typed verdict (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.SPACING.JETSUMRULES.THEOREMS.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v922_spacing_jet_sumrule_theorems.py` | Certified finite theorems [E] (fine type Formal, certified-finite; D1/D2/D2'/D3/D4 + gap-demand exact algebra recomputed in-run (sympy generic); the sign-uniform corollary CONDITIONAL with its hypothesis measured FALSE, carried as an obstruction; ladder tables pinned and typed MEASURED; PINNING DISCLOSURE: r135 PINNED |
| ledger:PRIME.THETAPRED.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v660_theta_predicate.py` | Exact [E] 2x2 machinery + [MEASURED] mechanism table and honest predicate FAIL + [C] typed successor (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.TOWERNEST.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v749_simpler_tower.py` | Exact [E] nesting/inheritance reduction (X-nesting 6.7e-18, dyadic D-refinement exact) with the honest limits typed (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.TURINGCERT.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v666_turing_cert.py` | Exact [E] band + Turing-integral certificate with must-break controls (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.UCPLIMIT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v735_strat3_ucp_inductive.py` | Exact [E] UCP/transport construction (LP-exact quantile couplings, linear Choi rank) + honest [M] negative on the preregistered covariance gate (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.UNCONDCERT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v594_unconditional_cert.py` | Exact [E] with one cited external bound (Buethe 2018); identity machine-verified |
| ledger:PRIME.W3BOUND.01 | CERTIFIED | LATTICE_E8_HECKE | `verification/v658_w3_uniform_bound.py` | Exact [E] slope identity + [MEASURED] risk survey and fragility + [C] typed verdict (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.W3STRUCT.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v677_w3_structure_theorem.py` | Exact [E] structure theorem (Cantoni-Butler split, sandwich, master identity, Epstein census + factor-2 prediction) + [MEASURED] threshold map + [C] honest typing (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.WCLOSED.01 | CERTIFIED | EXPLICIT_FORMULA_IDENTITY | `verification/v587_w_closed_form.py` | Exact [E] + measured payoff [M] (formula machine-exact; model comparison at declared tolerances) |
| ledger:PRIME.WEIL.BOUNDARY.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v640_w1_boundary.py` | Exact [E] sympy identities + [E, 20+ digits] certified boundary equation + [E-quad] derived moment law (Python-only per GATE.WOLFRAM.02; Lean identities). |
| ledger:PRIME.WEIL.CONTACT.01 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v630_suzuki_contact.py` | Exact [E] atom identity + [MEASURED] Galerkin profile + [C] typed contract status (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.WEIL.MATRIX.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v642_w1_matrix.py` | Exact [E] closed forms + [E-float] operator-level closure + typed lattice residuals with inverted-expectation checks (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.WEIL.THEOREM.01 | CERTIFIED | SCREW_SUBORDINATION_LSTAR | `verification/v643_w1_theorem.py` | Exact [E] projection lemma / measure-level identities + [E-float] form equality + erratum evidence (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.WEYL.PORT.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v865_weyl_port_readout.py` | Honest diagnosis-and-repair under the frozen preregistered protocols [typed evidence line: 9 checks with the TWO frozen-honest FAILS S1.SPR + S4.RSP kept and pattern-gated, NOT refit + 5/5 checks; the WHERE-LOST addendum v1.1 typed in the frozen spec; the repair's exactness |
| ledger:PRIME.WEYLMASS.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v706_chain_weyl_mass.py` | Honest [MEASURED, null] point-evaluation falsified + exact [E] Schur-parameter identity (1e-40) + [MEASURED] log-2 background find; AST zero firewall (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.Z1FLOWREC.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v698_z1_flow_recursion.py` | Exact [E] slot identity + [MEASURED] forced positions, shooting recovery, honest negatives (lookahead, noise-like residual, recursive E-transport); AST-confined zero diagnostic (Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.Z1UVAROV.01 | CERTIFIED | WEIL_POSITIVITY_WINDOWS | `verification/v697_z1_uvarov.py` | Exact [E] duality + transfer identity + sequential composition + [MEASURED] inverted stabilization law (AST zero-firewall; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.ZERO.CHANNEL.CAPACITY.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v950_zero_channel_capacity.py` | Instrument characterization, NOT arithmetic novelty [E] (fine types Formal (the capacity ceiling, the erasure bar, the Miller-Madow excess bound, the 108-case parity-code erasure theorem -- recomputed in-run) and Numerical (the capacity/NL/erasure/gain/control tables pinned and typed MEASURED); THE BUGHUNT-X F6 QUANTIFICATION |
| ledger:PRIME.ZEROGAP.01 | PROVED | LATTICE_E8_HECKE | `verification/v678_zero_gap_theorem.py` | Analytic [cited] theorem + Exact [E] comb verification and adaptive counts + [MEASURED] unconditional frame Boden + typed-residual projection negative (inverted expectation) + [C] quantified pinch (diagnostic zero-side line; Python-only per GATE.WOLFRAM.02). |
| ledger:PRIME.ZEROLAYER.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v709_chain_zero_layer.py` | Honest [MEASURED, null] layering rejection (best corr 0.042 = scramble level) behind a temporal SHA256 firewall (residual hashed before any zero read); zeros as comparison target only (Python-only per GATE.WOLFRAM.02). |
| ledger:RTF.GNS.LEDGER.01 | PROVED | WEIL_POSITIVITY_WINDOWS | `verification/v541_matching_lemma_ledger.py` | Identity [E] (exact integer/Fraction/sympy: full-window certificates, structure laws, ledger + kernel identities, character decomposition, duplication bridge, two-route CM carrier; mpmath identities at rel 1e-16..1e-41) + [C] (frontier facts: coherent-chain crossing, lambda-window margin, Robin tail factor -- window constants with declared |
| port lane | CERTIFIED | TOEPLITZ_MOMENT_POSITIVITY | `verification/v881_carleson_port_geometry.py` | [E] port geometry: rank-2 Jacobi displacement, testing law, port=wall, IIKS-class dressed kernel. [O] one-sidedness. |
| v1021 | PROVED | EXPLICIT_FORMULA_IDENTITY | `verification/v1021_all_place_tate_rank_audit.py` | Tate factorization, pole normalization, the abstract rank-nullity lemma and the historical Rankin counterexample are exact; applying the lemma to the Weil window is conditional on the external strict-floor preprint. |

## Reusable assets

| round | family | path | reusable |
| --- | --- | --- | --- |
| ledger:PRIME.KR4.DRIVER.CERT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v917_driver_rate_certification.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KR4.EPSTEIN.COLLAPSE.01 | SCREW_SUBORDINATION_LSTAR | `verification/v916_epstein_weil_violation.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| r26 contract | EXPLICIT_FORMULA_IDENTITY | `verification/v894_diagonal_refinement.py` | Weighted prime-pair kernel K_h,m, endpoint concavity bracket, scale-normalized inner-zone diagnostic. |
| ledger:PRIME.DIVISOR210.GAPCODE.01 | LATTICE_E8_HECKE | `verification/v886_register_gapcode_null.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| r224 | RHP_IIKS_TAU | `experiments/tfpt-discovery/tau_symbolic_probe.py` | Sylvester s-family, dressed-port D_P(s), CD confluence diagonal. |
| r224-r226 | RHP_IIKS_TAU | `verification/v955_tau_iiks_toda_dictionary.py` | Finite IIKS/Toda evaluators, Gauss J=QXQ^T forms, Hirota sign gates. |
| r225 | RHP_IIKS_TAU | `experiments/tfpt-discovery/lax_conditioned_probe.py` | Relative rank-2 generators; FIXED_DP_ALIAS kill. |
| r226 | RHP_IIKS_TAU | `experiments/tfpt-discovery/hirota_sign_probe.py` | tau = D(mu-nu)/D(mu); r_n = h(mutilde)/h(mu); signed Toda H_n. |
| r227 | RHP_IIKS_TAU | `experiments/tfpt-discovery/fermiedge_classify_probe.py` | FIK_IIKS_GAUGE_EXACT intertwiner; chi/A leakage coordinates. |
| r228 | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/holedual_probe.py` | Hankel complement identity; half-filling law N_w=ceil(S/2). |
| r228-r231 | TOEPLITZ_MOMENT_POSITIVITY | `verification/v956_signedmoment_halffilling_duality.py` | Half-filling counters, dual-FIK L-gauge, complement identity checks. |
| r229 | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/pontryagin_maxpos_probe.py` | Free-moment counting n=(S+1)/2; Frobenius inertia wards. |
| r230 | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/jfraction_probe.py` | Euclid remainder chain; beta reversal; free-prefix parameter budget. |
| r231 | RHP_IIKS_TAU | `experiments/tfpt-discovery/rhp_midpoint_probe.py` | Dual-FIK L-gauge; midpoint connection. |
| r232a | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/szego_equilibrium_probe.py` | Equilibrium QP builder for later v959 probes. |
| r243 | RHP_IIKS_TAU | `experiments/tfpt-discovery/principal_bessel_probe.py` | Budget coordinate B=S_{N-2}+5/7 used by later L† probes. |
| r244 | RHP_IIKS_TAU | `experiments/tfpt-discovery/bordered_hankel_probe.py` | Bordered PSD = wall + budget dictionary. |
| r244-r253 | RHP_IIKS_TAU | `verification/v958_bordered_tau_readout_dictionary.py` | Bordered readout error formulas, contour R1, PSD-base theorem gates. |
| r245 | RHP_IIKS_TAU | `experiments/tfpt-discovery/bordered_finite_rank_probe.py` | Schlesinger rank-1 insertion constructor. |
| r248 | RHP_IIKS_TAU | `experiments/tfpt-discovery/border_centering_probe.py` | Centering congruence. |
| r250 | RHP_IIKS_TAU | `experiments/tfpt-discovery/centered_basefiber_probe.py` | Centered base/fiber residual, Szego equilibrium solver import. |
| r251 | RHP_IIKS_TAU | `experiments/tfpt-discovery/targetreadout_error_probe.py` | Target-readout error functionals. |
| r251a | RHP_IIKS_TAU | `experiments/tfpt-discovery/corner_provenance_probe.py` | Corner-interface detector, three-budget split b1/b2/b3. |
| r252 | RHP_IIKS_TAU | `experiments/tfpt-discovery/base_gauge_constant_probe.py` | Contour R1 identity, gauge-constant battery. |
| r253 | RHP_IIKS_TAU | `experiments/tfpt-discovery/schlesinger_pairing_probe.py` | Schlesinger pairing, tau-ratio and pole-removal wards. |
| r254 | RHP_IIKS_TAU | `experiments/tfpt-discovery/offdiag_gram_probe.py` | Off-diagonal Gram mass split, scramble persistence check. |
| r255 | RHP_IIKS_TAU | `experiments/tfpt-discovery/nodebands_base_probe.py` | Node-band layer controls, drift localization detectors. |
| r256 | RHP_IIKS_TAU | `experiments/tfpt-discovery/baseborder_factorial_probe.py` | Base-border factorial mix detector, dominance re-adjudication. |
| r256-r259 | RHP_IIKS_TAU | `verification/v959_coupledtau_terminal_dictionary.py` | Coupled-tau recursion, Schur budget telescope, terminal q-law, microfalsifier. |
| r257 | RHP_IIKS_TAU | `experiments/tfpt-discovery/coupledtau_probe.py` | Coupled-tau coefficient typology, microfalsifier. |
| r258 | RHP_IIKS_TAU | `experiments/tfpt-discovery/budget_anatomy_probe.py` | Exact budget telescope, terminal q_N law. |
| r259 | RHP_IIKS_TAU | `experiments/tfpt-discovery/parametrix_pass_probe.py` | Parametrix candidate battery, three negative gates. |
| r260 | RHP_IIKS_TAU | `experiments/tfpt-discovery/terminal_crossratio_probe.py` | 42-rung terminal cross-ratio census. |
| r260-r275 | RHP_IIKS_TAU | `verification/v960_terminal_surface_closure.py` | kz15 interval certificate, two-branch decomposition, PairBound.lean H1-H4. |
| r261 | RHP_IIKS_TAU | `experiments/tfpt-discovery/prefix_resummation_probe.py` | Prefix-resummation bases, three sealed GO rules. |
| r262 | RHP_IIKS_TAU | `experiments/tfpt-discovery/terminal_triangle_probe.py` | Terminal triangle census, frozen joined-verdict form. |
| r263 | RHP_IIKS_TAU | `experiments/tfpt-discovery/cancellation_adjudication_probe.py` | Two-branch identity, exact-cancellation GO, scramble-discriminating K2. |
| r264 | RHP_IIKS_TAU | `experiments/tfpt-discovery/quenched_opening_probe.py` | Frozen campaign SHA, Z^RHP dictionary, S1_TERMDRIVE signature. |
| r265 | RHP_IIKS_TAU | `experiments/tfpt-discovery/s_monotonicity_probe.py` | s-coordinate admissibility battery, wall-equivalence gate. |
| r266 | RHP_IIKS_TAU | `experiments/tfpt-discovery/border_resolvent_identity_probe.py` | Decision-fingerprint / rank-fingerprint wall detector. |
| r267 | EXTERNAL_ADJUDICATION | `experiments/tfpt-discovery/ranktrace_adjudication_probe.py` | Ceiling-vs-wall comparison, NO_IMPORT frame-mismatch quantifiers. |
| r268 | RHP_IIKS_TAU | `experiments/tfpt-discovery/drive_local_asymptotics_probe.py` | Drive-local depth power, edge-region triangle bound. |
| r269 | RHP_IIKS_TAU | `experiments/tfpt-discovery/phase_bulk_bound_probe.py` | Phase-aware bulk bounds, block-alternation triangles. |
| r270 | RHP_IIKS_TAU | `experiments/tfpt-discovery/kz15_boss_probe.py` | kz15 interval certificate (dps 640), split-rule fail gate. |
| r271 | LEAN_FORMALIZATION | `experiments/tfpt-discovery/universal_pair_theorem_probe.py` | rh/lean/RH/PairBound.lean H1-H4, measured-trend-only guard. |
| r272 | RHP_IIKS_TAU | `experiments/tfpt-discovery/l2_scaling_anatomy_probe.py` | L2 scaling anatomy (alpha/beta/gamma), slack ranking. |
| r273 | RHP_IIKS_TAU | `experiments/tfpt-discovery/euler_mechanism_probe.py` | Euler perturbation ladder, firewall maintenance gates. |
| r274 | RHP_IIKS_TAU | `experiments/tfpt-discovery/wronskian_dictionary_probe.py` | Casoratian=h_n, node-polynomial midpoint form, augmented telescope. |
| r274-r278 | RHP_IIKS_TAU | `verification/v961_midpoint_orientation_dictionary.py` | Wronskian/Casoratian dictionary, Maslov R2 census, Hellmann-Feynman metric gates. |
| r275 | RHP_IIKS_TAU | `experiments/tfpt-discovery/kyp_memory_probe.py` | KYP infeasibility battery, target-inverse detector. |
| r276 | RHP_IIKS_TAU | `experiments/tfpt-discovery/minimal_firewall_probe.py` | Five-surgery dose-response continuum. |
| r277 | RHP_IIKS_TAU | `experiments/tfpt-discovery/maslov_census_probe.py` | Maslov R2 census, sealed training cascade, scramble holdouts. |
| r278 | RHP_IIKS_TAU | `experiments/tfpt-discovery/metric_stability_probe.py` | Hellmann-Feynman d log h_n / du_j, border/CD gradients. |
| r279 | RHP_IIKS_TAU | `experiments/tfpt-discovery/oriented_theorem_probe.py` | Two-sided index bilanz, sealed first-failure invariants. |
| r279-r281 | RHP_IIKS_TAU | `verification/v962_halffilling_pinning_theory.py` | T1 moment counters, T2 Jacobi/Sylvester crossing budget, T3 parity exhaustion. |
| r280 | RHP_IIKS_TAU | `experiments/tfpt-discovery/budget_localization_probe.py` | minC-N_w offset census, first-failing-bracket refinement. |
| r281 | RHP_IIKS_TAU | `experiments/tfpt-discovery/halffilling_pinning_probe.py` | Upper-pinning C=5 census, v956/r280 regression wards. |
| r282 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/representation_contest_probe.py` | Four-language contest gate, SOS_EXISTS GO rule, control-class rejection. |
| r282-r285 | SCREW_SUBORDINATION_LSTAR | `verification/v963_lstar_reduction_dictionary.py` | mu-frame congruence minors, L* subordination form, four-language kill gates. |
| r283 | RHP_IIKS_TAU | `experiments/tfpt-discovery/fullsource_quasidefiniteness_probe.py` | mu-frame congruence, lambda_max contraction, A1/A2/A3 candidate split. |
| r283 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/lstar_problem.pdf` | Printable external statement of L*. |
| r283 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/lstar_problem.tex` | First-principles mu/nu construction; S=367 table; sampling equivalents. |
| r283 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_lstar_instance.py` | Standalone mu/nu rebuild; dps-60 mpmath ward; 42-window ladder. |
| r284 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/lstar_two_measure_probe.py` | Two-measure subordination packing, shielding-blind detector. |
| r285 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/christoffel_decomposition_probe.py` | Christoffel (D)/(C) split, assist=lambda_max/maxdiag-1. |
| r286 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/lstar_margin_scaling_probe.py` | mp-sign-safe extended-anchor margin census. |
| r286-r289 | SCREW_SUBORDINATION_LSTAR | `verification/v964_lstar_coherence_census.py` | mp-sign-safe margin census, vdC H=ceil(sqrt(m)) bound, twin METRIC_ONLY switch. |
| r287 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/l2_deterministic_cancellation_probe.py` | vdC H=ceil(sqrt(m)) bound, deterministic-cancellation census. |
| r288 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/destructive_coherence_probe.py` | Destructive-coherence carrier map, ARCH-ARCH antiphase detector. |
| r289 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/arch_kernel_diophantine_probe.py` | Twin METRIC_ONLY switch, gap-preserving diophantine detune. |
| r290 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/profile_functional_probe.py` | theta_eq LAG basin geometry, killfrac ladder. |
| r290-r295 | SCREW_SUBORDINATION_LSTAR | `verification/v965_lstar_curvature_arc.py` | theta_eq LAG basin geometry, ridge budget threshold, DENS curvature valley. |
| r291 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/ridge_anatomy_probe.py` | Ridge budget-threshold interval, MAIN-specific plateau. |
| r292 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/curvature_form_probe.py` | Curvature two-form, DENS valley, diagonal protocol skeleton. |
| r293 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/metric_reconciliation_probe.py` | Metric-reconciliation protocol. |
| r294 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/f10_stability_probe.py` | F10 stability bars. |
| r295 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/f10_sp_hardening_probe.py` | F10 sp-hardening majority test. |
| r296 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/dens_identity_probe.py` | DENS coupling-number bar, sealed 0.40 threshold. |
| r296-r300 | SCREW_SUBORDINATION_LSTAR | `verification/v966_l2_reduction_chain.py` | Fejer energy transfer S_F, decay-split spectrum, n_eff participation identity. |
| r297 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/vdc_chain_provenance_probe.py` | vdC target inequality freeze (sigma<=-0.516), three provenance routes. |
| r298 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/window_border_transfer_probe.py` | Positional Fejer transfer identity, TRANSFER_DOMINANT gate. |
| r299 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/fejer_decay_probe.py` | Fejer decay-split spectrum, c-value difference-measure test. |
| r300 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/diag_target_probe.py` | n_eff=L1^2/D identity, kernel-envelope ratio majorant. |
| r301 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/neff_target_probe.py` | n_eff=n_act/(1+CV^2), perfect count link n_act==m. |
| r301-r304 | SCREW_SUBORDINATION_LSTAR | `verification/v967_l2_cascade_closure.py` | n_eff=n_act/(1+CV^2) identity, regress-invariance of S, period-4 comb detector. |
| r302 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/unif_target_probe.py` | Pooled-KS stationarity, coherence identity 1+CV^2=n_act χ/(surv^2 n_eff_atom). |
| r303 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/atom_target_probe.py` | Regress-invariance of S, synthetic dc rearrangement battery. |
| r304 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/shortrange_law_probe.py` | Period-4 comb detector, χ lag decomposition, short-range stop rule. |
| r305-r316 | SCREW_SUBORDINATION_LSTAR | `verification/v968_architecture_adjudication.py` | Four-level claim split, rank-one update identities, Renyi-3 GO/NO_GO bars. |
| r306 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/renyi3_probe.py` | Pointwise Rényi-3 cubic gates. |
| r307 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/fixed_head_probe.py` | Fixed-head kill battery, edge-pass fraction. |
| r308 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/block_green_probe.py` | Block-Green identity search harness. |
| r309 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/paired_cone_probe.py` | Paired-cone pilot harness. |
| r311 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/blockgreen_nontriviality_probe.py` | Block-Green nontriviality / STRICT_SOURCE_CONE gate. |
| r312 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/blockgreen_membership_probe.py` | Rank-one section membership test. |
| r313 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/renyi3_proof_fork_probe.py` | Triple-incidence vs Floquet proof-form bars. |
| r314 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/signed_cubic_flux_probe.py` | Signed-cubic-flux exact algebra. |
| r315 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/phi3_functional_probe.py` | Pre-declared Phi_3 functional, must-fail ledger. |
| r316 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/two_regime_bound_probe.py` | Two-regime bound bars, mid-ladder fail detector. |
| r317 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/exception_families_probe.py` | Exception-family census, generic-fail minimum. |
| r317-r322 | SCREW_SUBORDINATION_LSTAR | `verification/v969_forks_and_redteam.py` | U1-U3 extraction-type checks, sliding-bound fork contract, antiphase artifact test. |
| r318 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/indefinite_fork_probe.py` | Indefinite-fork premise battery. |
| r321 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/continuous_coordinate_probe.py` | Sliding cubic bound GO, pointwise-G fail gate. |
| r322 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/antiphase_sign_law_probe.py` | Antiphase artifact tests. |
| r323-r327 | SCREW_SUBORDINATION_LSTAR | `verification/v970_extraction_and_composition.py` | Elementwise stabilization GO, measured-composition chain, r324-pre FA bank. |
| r324 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/qmax_m2_origin_probe.py` | QMAX multiscale bars, M2 origin split. |
| r324-pre | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/fa_provenance_probe.py` | Banked FA provenance trees (fa/share/compose). |
| r325 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/extraction_order_probe.py` | Elementwise stabilization GO, three-variant repair fork. |
| r326 | LEAN_FORMALIZATION | `rh/lean/RH/Elementwise.lean` | Native dyadic GridElement and floor-free cell representation. |
| r327 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/group_mass_cap_probe.py` | Fold-group mass-cap bars, lambda-pair vs balance. |
| r329 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/ext3_fresh_anchors_probe.py` | EXT3 fresh-anchor battery, independence check for F_A. |
| r330 | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/dirichlet_secondworld_probe.py` | Dirichlet-L chi-mod-3 living-world builder. |
| r331 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/twin_resolution_probe.py` | Twin-resolution certificate at 1.8e-8, gap-preserving detune. |
| r333 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/companion_orbit_packing_probe.py` | Companion-orbit packing, weight-comparability ward. |
| r334 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/fold_capacity_probe.py` | Fold-capacity Cap_{mu,N} evaluator, golden-ratio draws. |
| r335 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/edge_packing_dichotomy_probe.py` | One-sided edge-orbit packing, composition chain bars. |
| r336 | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/lstar_parity_section_probe.py` | Chebyshev parity-section map, trigonometric q=p(cos theta)^2. |
| r337 | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/fold_martingale_probe.py` | Fold-group signed-mass martingale, maximal-function bar. |
| r339 | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/fold_density_dictionary_probe.py` | Fold-genealogy density dictionary, wrong-child-weighting must-fail. |
| r339+r341 (wave 14) | SCREW_SUBORDINATION_LSTAR | `verification/v978_terminal_density_martingale.py` | Mass-conservation martingale, moment dictionary, pair-ceiling identity. |
| r340 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/cauchybinet_hall_probe.py` | Weighted Cauchy-Binet transport, cut-reduction fail gate. |
| r341 | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/fold_bellman_reverse_holder_probe.py` | Path-weighted Bellman, reverse-Hölder good-tree split. |
| r342 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/pair_extremal_probe.py` | Two-atom determinant condition, pair-extremal anatomy. |
| r343 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/pair_coupling_probe.py` | Dressed pair reserve r'_det, fresh-family refutation battery. |
| r344 | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/fold_two_scale_balance_probe.py` | Two-scale R* balance, HSH split. |
| r344/r346/r351/r353/r355 (wave 14) | SCREW_SUBORDINATION_LSTAR | `verification/v979_cover_growth_k2.py` | FAB identity F_A B == m q_max/log m, K2 two-family law, Frame-A census. |
| r345 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/gap_ratio_primary_probe.py` | Gap-ratio g21, top-2 eigenvector geometry. |
| r345/r347/r348/r350/r352/r354 (wave 14) | SCREW_SUBORDINATION_LSTAR | `verification/v980_lstar_margin_chain.py` | Vieta one-line identity, dressed-scalar theorem, rho_K identities. |
| r346 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/fold_cover_canonization_probe.py` | K1–K3 stop tree; P02 predictor; r344 cover scaffold; must-fail mutants. |
| r347 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/delta_alpha_closure_probe.py` | One-line 2x2 identity; dressed-dictionary flatness clauses; must-fail ledger. |
| r348 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/delta_source_anatomy_probe.py` | Order-0 split identity; rate-equality toys T1/T2; eight-world discriminator. |
| r349 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/thirdarm_spike_law_probe.py` | Spike-class law tree; EXT4 hole list; scramble-in-class control. |
| r350 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/alpha_source_anatomy_probe.py` | CD kernel-column ward; candidate-law typing; world must-fails. |
| r351 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/qmax_growth_law_probe.py` | Convention-free FAB coordinate; frozen C_FAB; EXT5 clean list. |
| r352 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/rhor_source_anatomy_probe.py` | Weight-free rho_K identities; g_K12 factorisation; eight-world discriminator. |
| r353 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/second_family_erosion_probe.py` | Frame-B tent construction; FAB/floor kill mutants; grel lower-bound candidate. |
| r354 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/phi_wander_anatomy_probe.py` | CD dictionary reconstruction; phi_pred composition; EXT5 running-exponent model. |
| r355 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/k2_source_formula_probe.py` | NU-free K2 constant; grel-sharpened caps; six-zone NU test. |
| r356 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/borodin_dual_hole_probe.py` | Borodin dual-hole kernel; AC-class falsifier; carrier/compression clauses. |
| r356 (wave 14) | SCREW_SUBORDINATION_LSTAR | `verification/v981_lstar_borodin_duality.py` | Reciprocal dual weight, rational conjugator, half-filling complementation check. |
| r357 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/dirichlet_matched_frame_probe.py` | Matched Dirichlet frame derivation; chi4 ledger; scramble/twin controls. |
| r357 (wave 14) | EXPLICIT_FORMULA_IDENTITY | `verification/v982_dirichlet_matched_frame.py` | GRH-faithful chi-arch symbol, matched Dirichlet frame builder. |
| r358 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/local_gap_carleson_probe.py` | Quadratic packing bars; min-g floor 0.375; scramble P1-admission break. |
| r359 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/schur_wronskian_dual_probe.py` | Schur split; Casoratian resolvent identity; bind=lamS/eps. |
| r360 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/critical_saturation_probe.py` | Occupation duality o_eta+o_dual=1; t_geo margin lock. |
| r360+r362 companion, updated r367-r373 | SCREW_SUBORDINATION_LSTAR | `rh/problem/rdagger_saturation.pdf` | Printable R-dagger dossier. |
| r360+r362 companion, updated r367-r373 / r412 / r426 / R-DOSSIER DCCXCVII | SCREW_SUBORDINATION_LSTAR | `rh/problem/rdagger_saturation.tex` | R-dagger definition; duality package (A1)–(A7); pair-(2,4) saturation edge. |
| r361 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/mean_sieve_floor_probe.py` | SEP-SATZ; MED-CAP 8/3; exact 3/8 floor atoms. |
| r361 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/medcap_lemma.pdf` | Printable companion of medcap_lemma.tex. |
| r361 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/medcap_lemma.tex` | SEP identity; tiling⇒gap=sep; C2 16/3 violator; saturating prefix (1,2,6,5,4,4). |
| r361 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_medcap_steps.py` | Window-convention checks; C2 violator; saturating-prefix pin. |
| r362 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/augmented_borodin_duality_probe.py` | R-dagger Sherman–Morrison form; q-dagger dictionary; border-Schur closed form. |
| r363 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/canonical_sturm_induction_probe.py` | CD update R_{n+1}=R_n+vv^T; named EDGE-GAP lemma. |
| r364 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_xn_steps.py` | Pairing lemmas; C2 still-violates control; Chebyshev x-mask 0 C2. |
| r364 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/xn_invariant.pdf` | Printable companion of xn_invariant.tex. |
| r364 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/xn_invariant.tex` | Run-length pairing combinatorics; (1,2) locus; Chebyshev x-mask control. |
| r365 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/v2_regularity.pdf` | Printable companion of v2_regularity.tex. |
| r365 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/v2_regularity.tex` | Product XOR; Chebyshev x-mask and Nyquist-burst controls; plateau violator. |
| r365 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_v2_steps.py` | 2-regular refutation; plateau and spike toys; sign-identity pin. |
| r366 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/edge_gap_ms_probe.py` | Exact MS sandwich; discrete gap theorem. |
| r367 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/final_two_rank_inertia_probe.py` | haynsworth_two_rank Lean-shaped form; −det K2 source object. |
| r368 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/weighted_l2_t1_probe.py` | Exact T2 factorization; leave-family-out test. |
| r369 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/mixed_haynsworth_probe.py` | haynsworth_mixed; Phi_N(0)=J^{-1}+U^T A^{-1}U. |
| r370 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/matrix_weyl_index_probe.py` | Phi_N(z) block resolvent; Xi:=nneg Phi(0). |
| r371 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/compound_cd_wedge_probe.py` | Identity (12) det K2=1+q11+q22+wterm; product nneg(wedge2). |
| r372 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/source_prufer_one_defect_probe.py` | XOR sign(ct)=sign(w x v2); N2≥N3. |
| r374 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/v2_lemma_v3.pdf` | Printable companion of v2_lemma_v3.tex. |
| r374 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/v2_lemma_v3.tex` | Lagrange/Wronskian step over Q; slow-fast contrast dichotomy; Archimedes dwell. |
| r374 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_v2_lemma.py` | Wronskian residual 1e-15 pin; constant-step 0-violator; Chebyshev theta-compress. |
| r375 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/p2_lemma_proof.pdf` | Printable companion of p2_lemma_proof.tex. |
| r375 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/p2_lemma_proof.tex` | Six-scalar det identity; tiny-overlap adversary; Fractions 4-node toy. |
| r375 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_p2_steps.py` | det K2 identity; tiny-overlap adversary; RANK_KZ gamma>lam pin. |
| r377 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/postcap_pivots_probe.py` | (detK<0)==(sN*sNp1<0); aliasing P_X. |
| r377 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/postcap_pivots.pdf` | Printable companion of postcap_pivots.tex. |
| r377 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/postcap_pivots.tex` | Pivot dictionary; Stieltjes=Hankel; kz12 LATE counterexample. |
| r377 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_postcap_steps.py` | kz12 LATE counterexample; live/dead dictionary pins. |
| r378 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/compose_lemma.pdf` | Printable companion of compose_lemma.tex. |
| r378 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/compose_lemma.tex` | Pointwise compose chain; 42-rung FRAME-A certificate; exception list. |
| r378 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_compose_lemma.py` | vdC covering; T1-floor algebra; 42-rung qZ<1 certificate. |
| r379 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/v3prime_proof.pdf` | Printable companion of v3prime_proof.tex. |
| r379 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/v3prime_proof.tex` | Cosine-grid L=4h-2 identity; Jacobi-(0,1) Fejer; A_15 two-period class. |
| r379 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_v3prime.py` | L=4h-2 identity; A_15 amplitude bound; coherent-ray in/out. |
| r381 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/g_eps_lemma_probe.py` | d gamma_k/d w_j FO formula; Lambda(n)≤log n trial division. |
| r381 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/g_eps_lemma.pdf` | Printable companion of g_eps_lemma.tex. |
| r381 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/g_eps_lemma.tex` | FO Jacobi pairing; quadratic remainder; scramble last-12 kill. |
| r381 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_g_eps.py` | FO vs FD pin; R2 midpoint ratio; scramble kill. |
| r382 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/pivot_entry_lemma_probe.py` | Pair-energy identity; Christoffel comparison; 5-atom interlacing. |
| r382 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/pivot_entry_lemma.pdf` | Printable companion of pivot_entry_lemma.tex. |
| r382 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/pivot_entry_lemma.tex` | Pair-energy identity; 5-atom interlacing; two-period half-filling adversary. |
| r382 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_pivot_entry.py` | 5-atom interlacing; clustered H3<0; lambda wall. |
| r383 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/compose_premises_probe.py` | Fejer identity; L2 identity M3; T1-floor algebra under g_i≥3/8. |
| r383 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/compose_premises.pdf` | Printable companion of compose_premises.tex. |
| r383 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/compose_premises.tex` | R0=4 / Lambda=3 census; kz37 R-star; kz111 E_pi spike. |
| r383 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_compose_premises.py` | Death-triangle toy; kz111 E_pi spike; scramble M3-kill of (L). |
| r384 | LEAN_FORMALIZATION | `rh/lean/RH/FlankEntry.lean` | Pair-energy identity; 3-atom flank toy; clustered H3=-28500 kill. |
| r385 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/christoffel_quiet_probe.py` | FO_k=gamma_k(Q_k-Q_{k-1}); Chebyshev-Gauss Q_k==1 on cosine grid. |
| r385 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/christoffel_quiet.pdf` | Printable companion of christoffel_quiet.tex. |
| r385 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/christoffel_quiet.tex` | Chebyshev-Gauss Q==1; two-period Q-span; Koksma-failure pin. |
| r385 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_christoffel_quiet.py` | Koksma-failure pin; two-period lambda wall; EXT kz69 depth-200. |
| r386 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/compose_premises2_probe.py` | Death triangle; w9 dictionary q_N=(7/5)Z^2. |
| r386 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/compose_premises2.pdf` | Printable companion of compose_premises2.tex. |
| r386 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/compose_premises2.tex` | Death triangle; living Z0'=21/25; CHI4 kz46 sup. |
| r386 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_compose_premises2.py` | Death triangle; 4/5 mutant; living CHI4-46. |
| r387 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/coherence_assist_probe.py` | lambda=maxdiag*(1+assist); rho_AP discriminator. |
| r387 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/coherence_assist.pdf` | Printable companion of coherence_assist.tex. |
| r387 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/coherence_assist.tex` | Chebyshev-Dirichlet CD; rho_AP<1/5; two-period AP SATZ. |
| r387 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_coherence_assist.py` | 2x2 Gershgorin; two-period AP; clustered run-3. |
| r388 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/delta_deformation_probe.py` | FO=gamma(dQ^T+dDelta); Fejer-pure two-period FO=0. |
| r388 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/delta_deformation.pdf` | Printable companion of delta_deformation.tex. |
| r388 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/delta_deformation.tex` | FO-split; Fejer-pure two-period; C×2 mutant. |
| r388 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_delta_deformation.py` | Neumann bar; Chebyshev-Gauss; C×2 mutant. |
| r389 | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/weyl_energy_probe.py` | Finite-grid Parseval; two-period comb HHI discriminator. |
| r389 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_weyl_energy.py` | S=21 Parseval; two-period comb; scramble QM. |
| r389 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/weyl_energy.pdf` | Printable companion of weyl_energy.tex. |
| r389 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/weyl_energy.tex` | Chebyshev energy; finite-grid Parseval; two-period spectral comb. |
| r390 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/g_eps_mu_probe.py` | Bernstein–Szegő discrete Fejer; Jacobi-(0,1) g formula. |
| r390 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/g_eps_mu.pdf` | Printable companion of g_eps_mu.tex. |
| r390 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/g_eps_mu.tex` | Jacobi-(0,1); Bernstein-Szegő full-grid; permutation kill. |
| r390 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_g_eps_mu.py` | Permutation kill; signed-Fejer C_eps; two-period weight. |
| r391 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/construction_pure_rl_probe.py` | Euclidean split; CS counting; DC Rayleigh 3.6875. |
| r391 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/construction_rl.pdf` | Printable companion of construction_rl.tex. |
| r391 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/construction_rl.tex` | CS counting L1^2<=m D; white-block class; DC/align/merge mutants. |
| r391 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_construction_rl.py` | White-block class; weight-rand; DC/align/merge mutants. |
| r392 | RHP_IIKS_TAU | `experiments/tfpt-discovery/deletion_transform_probe.py` | tau_n=det(I-K_n[Xi] W); Bernstein–Szegő specialisation. |
| r392 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/deletion_transform.pdf` | Printable companion of deletion_transform.tex. |
| r392 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/deletion_transform.tex` | Uvarov gamma-ratio; Bernstein-Szegő specialisation; AP-in/clustered-out. |
| r392 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_deletion_transform.py` | One-point and block Uvarov; tau_0=1; scramble seed=3. |
| r393 | RHP_IIKS_TAU | `experiments/tfpt-discovery/tau_field_probe.py` | Cluster SM/2x2 det; rho_n=1-(W pi)^T(I-KW)^{-1}pi. |
| r393 companion | RHP_IIKS_TAU | `rh/problem/tau_field.pdf` | Printable companion of tau_field.tex. |
| r393 companion | RHP_IIKS_TAU | `rh/problem/tau_field.tex` | 1x1/2x2 tau; cluster decomp; rank-1 locality. |
| r393 companion | RHP_IIKS_TAU | `rh/problem/verify_tau_field.py` | tau_0=1; JUMP air; coupling mutant. |
| r394 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/sign_schur_probe.py` | Dirichlet envelope /D_n/; 2x2 Z-matrix counterexample. |
| r394 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/sign_schur.pdf` | Printable companion of sign_schur.tex. |
| r394 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/sign_schur.tex` | Dirichlet zonal signs; envelope SATZ; checkerboard rank-1 control. |
| r394 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_sign_schur.py` | 2x2 Z-matrix false pin; checkerboard rank-1; mesh step. |
| r395 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/three_gap_mask_probe.py` | Steinhaus nuniq≤3 on Z/q; PNT-free integer-log local 3-gap. |
| r395 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/three_gap_mask.pdf` | Printable companion of three_gap_mask.tex. |
| r395 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/three_gap_mask.tex` | Steinhaus Z/q; log-local 3-gap; 3/8 and 8/3 shadow controls. |
| r395 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_three_gap_mask.py` | Steinhaus Z/q; small-n census; discriminator pin. |
| r396 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/isolation_lemma_probe.py` | PNT-free folded non-adjacency; wrap(2,3,4) isolated class. |
| r396 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/isolation_lemma.pdf` | Printable companion of isolation_lemma.tex. |
| r396 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/isolation_lemma.tex` | Folded-small-integer SATZ; packing bound; wrap234 isolated control. |
| r396 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_isolation_lemma.py` | Packing O(n_atom); 1010 lambda>1; injection and fattail. |
| r397/r638L | LEAN_FORMALIZATION | `rh/lean/RH/Selected.lean` | RealCanonicalWindow; selected sequence (a_k,m_k); weil_nonneg_of_selected_windows. |
| r398 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/high_moment_inertia_probe.py` | Cycle-sum tr(A^k); pointwise 1_{r<1/2}≤[2(1-r)]^{2d}. |
| r398 companion | OPERATOR_SPECTRAL | `rh/problem/high_moment_inertia.pdf` | Printable companion of high_moment_inertia.tex. |
| r398 companion | OPERATOR_SPECTRAL | `rh/problem/high_moment_inertia.tex` | Frozen even-moment set; 2x2 cycle-sum; eigenvalue-1/2 cluster diagnosis. |
| r398 companion | OPERATOR_SPECTRAL | `rh/problem/verify_high_moment.py` | Frozen d-set; 3x3 walk-sum; scramble nneg=21. |
| r399 | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/source_weyl_energy_probe.py` | Tent interpolant dP; Fejer Laplacian IFFT identity. |
| r399 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/source_weyl_energy.pdf` | Printable companion of source_weyl_energy.tex. |
| r399 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/source_weyl_energy.tex` | Dirichlet interpolant; Fejer Laplacian; energy-path firewall. |
| r399 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_source_weyl.py` | Energy-path firewall; MVT-ratio pin; selected k=4<k=6. |
| r400 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/bulk_one_defect_probe.py` | Rank-r interlacing; Weyl nneg(A+B)≤nneg(A)+nneg(B). |
| r400 companion | OPERATOR_SPECTRAL | `rh/problem/bulk_one_defect.pdf` | Printable companion of bulk_one_defect.tex. |
| r400 companion | OPERATOR_SPECTRAL | `rh/problem/bulk_one_defect.tex` | Rank-r interlacing; Weyl SATZ; phase-blindness census. |
| r400 companion | OPERATOR_SPECTRAL | `rh/problem/verify_bulk_one_defect.py` | Rank-1 interlacing; threshold x2; source-frame failure pin. |
| r401 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/edge_signature_probe.py` | Phi_edge(a,b) chart; Haynsworth additivity on explicit 3×3. |
| r401 companion | OPERATOR_SPECTRAL | `rh/problem/edge_signature.pdf` | Printable companion of edge_signature.tex. |
| r401 companion | OPERATOR_SPECTRAL | `rh/problem/edge_signature.tex` | 3x3 mixed Haynsworth; both-chart model lemma; 64-pt disk. |
| r401 companion | OPERATOR_SPECTRAL | `rh/problem/verify_edge_signature.py` | Mixed Haynsworth; 64-pt disk; drop-border. |
| r403 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/p1_construction_probe.py` | Scale-invariance R(cw)=R(w); rank-1 interlacing toy. |
| r403 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/p1_construction.pdf` | Printable companion of p1_construction.tex. |
| r403 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/p1_construction.tex` | Weight-rand kill; Rademacher/permute controls; scale invariance. |
| r403 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_p1_construction.py` | Weight-rand kill; mild 1e-4; dead-chi weights vs perm. |
| r404 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/one_defect_gram_probe.py` | Loewner nsum identity; folded-weight linearity. |
| r404 companion | OPERATOR_SPECTRAL | `rh/problem/one_defect_gram.pdf` | Printable companion of one_defect_gram.tex. |
| r404 companion | OPERATOR_SPECTRAL | `rh/problem/one_defect_gram.tex` | Cauchy kernel; Loewner identity; Cholesky-tautology vs permute. |
| r404 companion | OPERATOR_SPECTRAL | `rh/problem/verify_one_defect_gram.py` | Cholesky tautology vs permute; ones-mode; Lambda-perm mutant. |
| r405 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/edge_contractive_lift_probe.py` | Woodbury Delta=kappa_closed(-sch); disk Parseval reserve. |
| r405 companion | OPERATOR_SPECTRAL | `rh/problem/edge_contractive_lift.pdf` | Printable companion of edge_contractive_lift.tex. |
| r405 companion | OPERATOR_SPECTRAL | `rh/problem/edge_contractive_lift.tex` | Euler tail; disk Parseval; Woodbury kappa_closed; wrong-sign J. |
| r405 companion | OPERATOR_SPECTRAL | `rh/problem/verify_edge_lift.py` | Wrong-sign J; ones-split Delta/c2/kappa; border-vs-tail. |
| r406 | LEAN_FORMALIZATION | `rh/lean/RH/OneDefect.lean` | indNeg_sub_rankOne_le_one; Woodbury; posDef_of_contractive_lift. |
| r407 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/dual_intertwiner_probe.py` | R=C(I+C)^{-1}; nneg(R-I/2)={lam(C)<1}. |
| r407 companion | OPERATOR_SPECTRAL | `rh/problem/dual_intertwiner.pdf` | FL dictionary eig(R)=λ(C)/(1+λ(C)); Q Woodbury/Hankel toys; scramble/permute/dead-chi controls. |
| r407 companion | OPERATOR_SPECTRAL | `rh/problem/dual_intertwiner.tex` | R=C(I+C)^{-1}; Hankel/Woodbury/FL; Euler moment layer. |
| r407 companion | OPERATOR_SPECTRAL | `rh/problem/verify_dual_intertwiner.py` | FL dictionary eig(R)=λ(C)/(1+λ(C)); Q Woodbury/Hankel toys; scramble/permute/dead-chi controls. |
| r408 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/c_threshold_probe.py` | Rayleigh lam_min≤dmin; C=dressed mu-dual CD kernel. |
| r408 companion | OPERATOR_SPECTRAL | `rh/problem/c_threshold.pdf` | C=BB^T anatomy; 1010 Nyquist kill; thin/densify and scramble/permute dmin controls. |
| r408 companion | OPERATOR_SPECTRAL | `rh/problem/c_threshold.tex` | C=BB^T anatomy; 1010 Nyquist kill; thin/densify and scramble/permute dmin controls. |
| r408 companion | OPERATOR_SPECTRAL | `rh/problem/verify_c_threshold.py` | C=BB^T anatomy; 1010 Nyquist kill; thin/densify and scramble/permute dmin controls. |
| r409 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/borodin_birkhoff_intertwiner_probe.py` | Jacobi-free T0 constructor; three-basis identity. |
| r409 companion | OPERATOR_SPECTRAL | `rh/problem/borodin_birkhoff_intertwiner.pdf` | Three-basis Q toys; graph=CD Woodbury; Phi/Krein miss and scramble/permute/jitter pins. |
| r409 companion | OPERATOR_SPECTRAL | `rh/problem/borodin_birkhoff_intertwiner.tex` | Three-basis Q toys; graph=CD Woodbury; Phi/Krein miss and scramble/permute/jitter pins. |
| r409 companion | OPERATOR_SPECTRAL | `rh/problem/verify_borodin_birkhoff.py` | Three-basis Q toys; graph=CD Woodbury; Phi/Krein miss and scramble/permute/jitter pins. |
| r410 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/hole_nyquist_probe.py` | Theta-prefix Cmin crossing table. |
| r410 companion | OPERATOR_SPECTRAL | `rh/problem/hole_nyquist.pdf` | RK/Rayleigh Q toys; Y-Lagrange bmax pin; Fourier off-fraction and sequential-birth census. |
| r410 companion | OPERATOR_SPECTRAL | `rh/problem/hole_nyquist.tex` | RK/Rayleigh Q toys; Y-Lagrange bmax pin; Fourier off-fraction and sequential-birth census. |
| r410 companion | OPERATOR_SPECTRAL | `rh/problem/verify_hole_nyquist.py` | RK/Rayleigh Q toys; Y-Lagrange bmax pin; Fourier off-fraction and sequential-birth census. |
| r411 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/threshold_identity_probe.py` | T*T=C^{-1}; Fourier face //T vF//<//T//. |
| r411 companion | OPERATOR_SPECTRAL | `rh/problem/threshold_identity.pdf` | T*T=Cinv Q toys; kz42 saturation gap; k=36/37 crossing vs Klast pin. |
| r411 companion | OPERATOR_SPECTRAL | `rh/problem/threshold_identity.tex` | T*T=Cinv Q toys; kz42 saturation gap; k=36/37 crossing vs Klast pin. |
| r411 companion | OPERATOR_SPECTRAL | `rh/problem/verify_threshold_identity.py` | T*T=Cinv Q toys; kz42 saturation gap; k=36/37 crossing vs Klast pin. |
| r413 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/hole_top_mode_probe.py` | Lagrange identity on deg≤q-2; constructor audit (no eig/SVD). |
| r413 companion | OPERATOR_SPECTRAL | `rh/problem/hole_top_mode.pdf` | Lagrange/GS Q toys; constructor audit (no eig/SVD); corr(v_top,C-ev0) and QD-mass pins. |
| r413 companion | OPERATOR_SPECTRAL | `rh/problem/hole_top_mode.tex` | Lagrange/GS Q toys; constructor audit (no eig/SVD); corr(v_top,C-ev0) and QD-mass pins. |
| r413 companion | OPERATOR_SPECTRAL | `rh/problem/verify_hole_top_mode.py` | Lagrange/GS Q toys; constructor audit (no eig/SVD); corr(v_top,C-ev0) and QD-mass pins. |
| r415 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/top_mode_edge_probe.py` | alpha=(eta-1)/kappa, beta=r^T K^{-1}r/kappa, beta-alpha=-sch. |
| r415 companion | OPERATOR_SPECTRAL | `rh/problem/top_mode_edge.pdf` | Euler-tail/disk-Parseval Q toys; α/β chart; ones=r405 identity pin. |
| r415 companion | OPERATOR_SPECTRAL | `rh/problem/top_mode_edge.tex` | Euler-tail/disk-Parseval Q toys; α/β chart; ones=r405 identity pin. |
| r415 companion | OPERATOR_SPECTRAL | `rh/problem/verify_top_mode_edge.py` | Euler-tail/disk-Parseval Q toys; α/β chart; ones=r405 identity pin. |
| r416 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/debranges_index_probe.py` | Monic Wronskian W(p2,q2)=-gamma_1; HB interlacing. |
| r416 companion | MELLIN_PICK_LEE_YANG | `rh/problem/debranges_index.pdf` | Wronskian/disc Q toys; HB interlacing census; yy_A combinatorial Rücklauf pin. |
| r416 companion | MELLIN_PICK_LEE_YANG | `rh/problem/debranges_index.tex` | Wronskian/disc Q toys; HB interlacing census; yy_A combinatorial Rücklauf pin. |
| r416 companion | MELLIN_PICK_LEE_YANG | `rh/problem/verify_debranges_index.py` | Wronskian/disc Q toys; HB interlacing census; yy_A combinatorial Rücklauf pin. |
| r417 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/source_sch_sign_probe.py` | sch=den-2+s^T(A0+Ucd Ucd^T)^{-1}s; P1/VAC chart formulae. |
| r417 companion | RHP_IIKS_TAU | `rh/problem/source_sch_sign.pdf` | Woodbury/chart Q toys; sign-map grids; drop-border and two-period mutants. |
| r417 companion | RHP_IIKS_TAU | `rh/problem/source_sch_sign.tex` | Woodbury/chart Q toys; sign-map grids; drop-border and two-period mutants. |
| r417 companion | RHP_IIKS_TAU | `rh/problem/verify_source_sch.py` | Woodbury/chart Q toys; sign-map grids; drop-border and two-period mutants. |
| r418 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/phi_bb_sign_probe.py` | c_J=den-2; A0^{-1}=2(C+I)(C-I)^{-1}. |
| r418 companion | RHP_IIKS_TAU | `rh/problem/phi_bb_sign.pdf` | Q-split and C-resolvent toys; pole-save mutant; drop-border control. |
| r418 companion | RHP_IIKS_TAU | `rh/problem/phi_bb_sign.tex` | Q-split and C-resolvent toys; pole-save mutant; drop-border control. |
| r418 companion | RHP_IIKS_TAU | `rh/problem/verify_phi_bb.py` | Q-split and C-resolvent toys; pole-save mutant; drop-border control. |
| r419 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/vacuous_overflow_probe.py` | Life rule live OVF tau2>phibb; dead VAC tau2<phibb. |
| r419 companion | RHP_IIKS_TAU | `rh/problem/vacuous_overflow.pdf` | VAC chart; drop-τ/drop-border; kz12 overflow and kz26 razor pins. |
| r419 companion | RHP_IIKS_TAU | `rh/problem/vacuous_overflow.tex` | VAC chart; drop-τ/drop-border; kz12 overflow and kz26 razor pins. |
| r419 companion | RHP_IIKS_TAU | `rh/problem/verify_vacuous_overflow.py` | VAC chart; drop-τ/drop-border; kz12 overflow and kz26 razor pins. |
| r420 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/cj_sigma_probe.py` | den identity; one-balance phibb=c_J+Sigma. |
| r420 companion | OPERATOR_SPECTRAL | `rh/problem/cj_sigma.pdf` | den-over-Q toy; drop-border; selected-shrink and VAC overflow pins. |
| r420 companion | OPERATOR_SPECTRAL | `rh/problem/cj_sigma.tex` | den-over-Q toy; drop-border; selected-shrink and VAC overflow pins. |
| r420 companion | OPERATOR_SPECTRAL | `rh/problem/verify_cj_sigma.py` | den-over-Q toy; drop-border; selected-shrink and VAC overflow pins. |
| r421 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/reserve_limit_probe.py` | T0-1=-(C_min-1)/2 on VAC; AIC floor vs decay. |
| r421 companion | OPERATOR_SPECTRAL | `rh/problem/reserve_limit.pdf` | R-over-Q and T0-linear toys; AIC M1/M3 battery; k=8 pin and k=10 lock. |
| r421 companion | OPERATOR_SPECTRAL | `rh/problem/reserve_limit.tex` | R-over-Q and T0-linear toys; AIC M1/M3 battery; k=8 pin and k=10 lock. |
| r421 companion | OPERATOR_SPECTRAL | `rh/problem/verify_reserve_limit.py` | R-over-Q and T0-linear toys; AIC M1/M3 battery; k=8 pin and k=10 lock. |
| r422 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/sigma_limit_probe.py` | Stieltjes Sigma identity. |
| r422 companion | OPERATOR_SPECTRAL | `rh/problem/sigma_limit.pdf` | Stieltjes-over-Q toy; g=1 mutant; drop-border; kz26 near-1 pin. |
| r422 companion | OPERATOR_SPECTRAL | `rh/problem/sigma_limit.tex` | Stieltjes-over-Q toy; g=1 mutant; drop-border; kz26 near-1 pin. |
| r422 companion | OPERATOR_SPECTRAL | `rh/problem/verify_sigma_limit.py` | Stieltjes-over-Q toy; g=1 mutant; drop-border; kz26 near-1 pin. |
| r423 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/den_limit_probe.py` | den=1+gam-vts. |
| r423 companion | OPERATOR_SPECTRAL | `rh/problem/den_limit.pdf` | den-over-Q bookkeeping; drop-vts/drop-border; not-subsum pin. |
| r423 companion | OPERATOR_SPECTRAL | `rh/problem/den_limit.tex` | den-over-Q bookkeeping; drop-vts/drop-border; not-subsum pin. |
| r423 companion | OPERATOR_SPECTRAL | `rh/problem/verify_den_limit.py` | den-over-Q bookkeeping; drop-vts/drop-border; not-subsum pin. |
| r424 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/gamma_chain_probe.py` | //b//^2 == mu_side_budget. |
| r424 companion | OPERATOR_SPECTRAL | `rh/problem/gamma_chain.pdf` | Bessel-over-Q leftover; γ bookkeeping; unnorm/scramble mutants. |
| r424 companion | OPERATOR_SPECTRAL | `rh/problem/gamma_chain.tex` | Bessel-over-Q leftover; γ bookkeeping; unnorm/scramble mutants. |
| r424 companion | OPERATOR_SPECTRAL | `rh/problem/verify_gamma_chain.py` | Bessel-over-Q leftover; γ bookkeeping; unnorm/scramble mutants. |
| r425 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/cross_chain_gamma_probe.py` | Kernel Loewner K_mu ≼ K_{mu-nu}; q_N dictionary. |
| r425 companion | OPERATOR_SPECTRAL | `rh/problem/cross_chain_gamma.pdf` | K_μ≼K_{μ-ν} Q toy; q_N bridge; unnorm ONB-break and dead-q_N>1 pins. |
| r425 companion | OPERATOR_SPECTRAL | `rh/problem/cross_chain_gamma.tex` | K_μ≼K_{μ-ν} Q toy; q_N bridge; unnorm ONB-break and dead-q_N>1 pins. |
| r425 companion | OPERATOR_SPECTRAL | `rh/problem/verify_cross_chain.py` | K_μ≼K_{μ-ν} Q toy; q_N bridge; unnorm ONB-break and dead-q_N>1 pins. |
| r426 | LEAN_FORMALIZATION | `rh/lean/RH/EdgeBalance.lean` | Woodbury-sch corollary; 3x3 chart trichotomy; vacuous tau^2-separator. |
| r427 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/campaign_audit_probe.py` | Independent C versus A0+I/2 constructors; four death coordinates. |
| r427 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/campaign_audit.pdf` | Independent intertwiner/QD/KKT paths; floor-vs-N AIC flip; live-χ non-fire control. |
| r427 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/campaign_audit.tex` | Independent intertwiner/QD/KKT paths; floor-vs-N AIC flip; live-χ non-fire control. |
| r427 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_campaign_audit.py` | Independent intertwiner/QD/KKT paths; floor-vs-N AIC flip; live-χ non-fire control. |
| r428 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/qn_reopened_probe.py` | COMPOSE envelopes on selected; /Z_loc/ sublemma. |
| r428 companion | RHP_IIKS_TAU | `rh/problem/qn_reopened.pdf` | Prime-power map k→kz; COMPOSE envelopes; VAC-overlap and kz16 false-anchor pins. |
| r428 companion | RHP_IIKS_TAU | `rh/problem/qn_reopened.tex` | Prime-power map k→kz; COMPOSE envelopes; VAC-overlap and kz16 false-anchor pins. |
| r428 companion | RHP_IIKS_TAU | `rh/problem/verify_qn_reopened.py` | Prime-power map k→kz; COMPOSE envelopes; VAC-overlap and kz16 false-anchor pins. |
| r429 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/zloc_head_probe.py` | canonical_split Z_loc=t_loc+chain. |
| r429 companion | RHP_IIKS_TAU | `rh/problem/verify_zloc_head.py` | canonical_split identity; triangle/scramble/dead-15 battery; k=3 tightness pin. |
| r429 companion | RHP_IIKS_TAU | `rh/problem/zloc_head.pdf` | canonical_split identity; triangle/scramble/dead-15 battery; k=3 tightness pin. |
| r429 companion | RHP_IIKS_TAU | `rh/problem/zloc_head.tex` | canonical_split identity; triangle/scramble/dead-15 battery; k=3 tightness pin. |
| r430 | LEAN_FORMALIZATION | `rh/lean/RH/FrequentlySelected.lean` | R† ⪰ ½I ↔ augmented PSD and frequent-selection mincut. |
| r431 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/source_potapov_probe.py` | Unipotent Redheffer=mass sum; Cauchy-pi=Lagrange at kdim=0. |
| r431 companion | MELLIN_PICK_LEE_YANG | `rh/problem/source_potapov.pdf` | Redheffer=Cauchy Q pin m_X(7/3); Cauchy-π S0; Gate-3 D11=−1744/2025 mismatch. |
| r431 companion | MELLIN_PICK_LEE_YANG | `rh/problem/source_potapov.tex` | Redheffer=Cauchy Q pin m_X(7/3); Cauchy-π S0; Gate-3 D11=−1744/2025 mismatch. |
| r431 companion | MELLIN_PICK_LEE_YANG | `rh/problem/verify_source_potapov.py` | Redheffer=Cauchy Q pin m_X(7/3); Cauchy-π S0; Gate-3 D11=−1744/2025 mismatch. |
| r431-AUDIT | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/r431_audit_probe.py` | Homma Redheffer star; closure lemma kappa additive. |
| r431-AUDIT companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/r431_audit.pdf` | Independent (no import) constructors; BP non-commute; Homma Redheffer star=mass sum. |
| r431-AUDIT companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/r431_audit.tex` | Independent (no import) constructors; BP non-commute; Homma Redheffer star=mass sum. |
| r431-AUDIT companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_r431_audit.py` | Independent (no import) constructors; BP non-commute; Homma Redheffer star=mass sum. |
| r433 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/edge_redheffer_probe.py` | Terminating Redheffer star; delta=4 sch_b/(1+2 sch_b). |
| r433 companion | MELLIN_PICK_LEE_YANG | `rh/problem/edge_redheffer.pdf` | Redheffer mixed-form Q toys; last-pivot dictionary; ones-Woodbury kill; living/dead χ split. |
| r433 companion | MELLIN_PICK_LEE_YANG | `rh/problem/edge_redheffer.tex` | Redheffer mixed-form Q toys; last-pivot dictionary; ones-Woodbury kill; living/dead χ split. |
| r433 companion | MELLIN_PICK_LEE_YANG | `rh/problem/verify_edge_redheffer.py` | Redheffer mixed-form Q toys; last-pivot dictionary; ones-Woodbury kill; living/dead χ split. |
| r435 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/p1_overload_probe.py` | nC antitone drop≤1; dictionary nC(N_w-3)=n_-(A0). |
| r435 companion | OPERATOR_SPECTRAL | `rh/problem/p1_overload.pdf` | 2×2/3×3 GK-fail toys; depth-lift; false depth N_w-1 control; nC-curve pin. |
| r435 companion | OPERATOR_SPECTRAL | `rh/problem/p1_overload.tex` | 2×2/3×3 GK-fail toys; depth-lift; false depth N_w-1 control; nC-curve pin. |
| r435 companion | OPERATOR_SPECTRAL | `rh/problem/verify_p1_overload.py` | 2×2/3×3 GK-fail toys; depth-lift; false depth N_w-1 control; nC-curve pin. |
| r436 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/p2_determinant_probe.py` | det K2=det(K2_+)-Q; C_min=psi_- cosine 1. |
| r436 companion | OPERATOR_SPECTRAL | `rh/problem/p2_determinant.pdf` | Reverse-CS Q toy det=−7; drop-ψ and tiny-overlap adversaries; C_min=ψ_- pin. |
| r436 companion | OPERATOR_SPECTRAL | `rh/problem/p2_determinant.tex` | Reverse-CS Q toy det=−7; drop-ψ and tiny-overlap adversaries; C_min=ψ_- pin. |
| r436 companion | OPERATOR_SPECTRAL | `rh/problem/verify_p2_determinant.py` | Reverse-CS Q toy det=−7; drop-ψ and tiny-overlap adversaries; C_min=ψ_- pin. |
| r438 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/evolutionary_certificate_probe.py` | Hard train/holdout split; illegal CHI3 a=0 nC=3 control. |
| r438 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/evolutionary_certificate.pdf` | Hard train/holdout split; ONES-Y and r375 Q toys; illegal a=0 and permute/scramble battery. |
| r438 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/evolutionary_certificate.tex` | Hard train/holdout split; ONES-Y and r375 Q toys; illegal a=0 and permute/scramble battery. |
| r438 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_evolutionary_cert.py` | Hard train/holdout split; ONES-Y and r375 Q toys; illegal a=0 and permute/scramble battery. |
| r439 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/residual_loewner_probe.py` | Rank-2 commutator; kdim=0 dressed Loewner Delta D0 Delta. |
| r439 companion | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/residual_loewner.pdf` | Disp-rank and Cauchy-π Q toys; dressed Loewner; Sturm≠1−q^d control. |
| r439 companion | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/residual_loewner.tex` | Disp-rank and Cauchy-π Q toys; dressed Loewner; Sturm≠1−q^d control. |
| r439 companion | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/verify_residual_loewner.py` | Disp-rank and Cauchy-π Q toys; dressed Loewner; Sturm≠1−q^d control. |
| r440 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/mean_tau_index_probe.py` | exists_index_zero_of_block_mean_lt_one landing site; MI2 linearity. |
| r440 companion | RHP_IIKS_TAU | `rh/problem/mean_tau_index.pdf` | T1 κ=1 and T2 winding Q toys; MI2 linearity; collar radii 0.40/0.499; landing site r430. |
| r440 companion | RHP_IIKS_TAU | `rh/problem/mean_tau_index.tex` | T1 κ=1 and T2 winding Q toys; MI2 linearity; collar radii 0.40/0.499; landing site r430. |
| r440 companion | RHP_IIKS_TAU | `rh/problem/verify_mean_tau.py` | T1 κ=1 and T2 winding Q toys; MI2 linearity; collar radii 0.40/0.499; landing site r430. |
| r441 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/diag_lifts_loewner_probe.py` | Lift count n_-(W-K^{-1})=#{lam(W^{1/2}KW^{1/2})<1}. |
| r441 companion | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/diag_lifts_loewner.pdf` | Gram/L-ND/lift-count Q toys; 6-node refute; kz52 slip pin. |
| r441 companion | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/diag_lifts_loewner.tex` | Gram/L-ND/lift-count Q toys; 6-node refute; kz52 slip pin. |
| r441 companion | TOEPLITZ_MOMENT_POSITIVITY | `rh/problem/verify_diag_lifts.py` | Gram/L-ND/lift-count Q toys; 6-node refute; kz52 slip pin. |
| r442 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/block_mean_probe.py` | q-dagger=(1/Bw) b^T(I-C)^{-1}b. |
| r442 companion | RHP_IIKS_TAU | `rh/problem/block_mean.pdf` | Last-pivot dictionary Q toy; MI2 linearity; living/dead χ q^dagger split. |
| r442 companion | RHP_IIKS_TAU | `rh/problem/block_mean.tex` | Last-pivot dictionary Q toy; MI2 linearity; living/dead χ q^dagger split. |
| r442 companion | RHP_IIKS_TAU | `rh/problem/verify_block_mean.py` | Last-pivot dictionary Q toy; MI2 linearity; living/dead χ q^dagger split. |
| r443 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/delta_floor_probe.py` | delta=R+tau-correction chart; AIC M1/M3 split. |
| r443 companion | RHP_IIKS_TAU | `rh/problem/delta_floor.pdf` | P1/VAC chart Q toys; frozen-slice AIC; kz16-below and k=10 lock pins. |
| r443 companion | RHP_IIKS_TAU | `rh/problem/delta_floor.tex` | P1/VAC chart Q toys; frozen-slice AIC; kz16-below and k=10 lock pins. |
| r443 companion | RHP_IIKS_TAU | `rh/problem/verify_delta_floor.py` | P1/VAC chart Q toys; frozen-slice AIC; kz16-below and k=10 lock pins. |
| r444 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/signed_border_mean_probe.py` | Triple sum; pole/regular split; dead-chi pole overshoot. |
| r444 companion | RHP_IIKS_TAU | `rh/problem/signed_border_mean.pdf` | Triple-sum and pole-split Q toys; diag-not-whole control; dead-χ pole-overshoot pin. |
| r444 companion | RHP_IIKS_TAU | `rh/problem/signed_border_mean.tex` | Triple-sum and pole-split Q toys; diag-not-whole control; dead-χ pole-overshoot pin. |
| r444 companion | RHP_IIKS_TAU | `rh/problem/verify_signed_border.py` | Triple-sum and pole-split Q toys; diag-not-whole control; dead-χ pole-overshoot pin. |
| r445 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/deep_builder_probe.py` | Slim-atom chain; bit-gate k=3..9; unused-Lanczos hotspot. |
| r445 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/deep_builder.pdf` | Skip-Lanczos builder; q^dagger formula pin; k=8/10/11/12 maps; ABD-ok slice AIC. |
| r445 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/deep_builder.tex` | Skip-Lanczos builder; q^dagger formula pin; k=8/10/11/12 maps; ABD-ok slice AIC. |
| r445 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_deep_builder.py` | Skip-Lanczos builder; q^dagger formula pin; k=8/10/11/12 maps; ABD-ok slice AIC. |
| r446 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/deep_abd_probe.py` | mpmath dps-raise sign-stability ward; last live kz=136. |
| r446 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/deep_abd.pdf` | mpmath dps-identity REAL pins; k=12 ETA_UNDERFLOW class; last-live kz136 map. |
| r446 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/deep_abd.tex` | mpmath dps-identity REAL pins; k=12 ETA_UNDERFLOW class; last-live kz136 map. |
| r446 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_deep_abd.py` | mpmath dps-identity REAL pins; k=12 ETA_UNDERFLOW class; last-live kz136 map. |
| r447 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/exact_atom_probe.py` | Exact-integer atom constructor; dps 70 prefix. |
| r447 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/exact_atom.pdf` | Exact-atom ulp pins; k=5 exact-live chain; dps 50/70 flip-stable n=3788. |
| r447 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/exact_atom.tex` | Exact-atom ulp pins; k=5 exact-live chain; dps 50/70 flip-stable n=3788. |
| r447 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_exact_atom.py` | Exact-atom ulp pins; k=5 exact-live chain; dps 50/70 flip-stable n=3788. |
| r448 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/exact_band_probe.py` | Exact generic a=1259; zeta-chain death coordinates. |
| r448 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/exact_band.pdf` | kz136 live / kz230 death pins; next-odd wall; kz197 chain-death coordinates. |
| r448 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/exact_band.tex` | kz136 live / kz230 death pins; next-odd wall; kz197 chain-death coordinates. |
| r448 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_exact_band.py` | kz136 live / kz230 death pins; next-odd wall; kz197 chain-death coordinates. |
| r449 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/flip_vs_stab_probe.py` | eps-robust n_stab via Chebyshev-moment Fenster-Vergleich. |
| r449 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/flip_vs_stab.pdf` | Chebyshev Fenster-Vergleich n_stab; kz17 comb-stab anchor; kz197 prefix-80 living pin. |
| r449 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/flip_vs_stab.tex` | Chebyshev Fenster-Vergleich n_stab; kz17 comb-stab anchor; kz197 prefix-80 living pin. |
| r449 companion | CERTIFICATE_INFRASTRUCTURE | `rh/problem/verify_flip_vs_stab.py` | Chebyshev Fenster-Vergleich n_stab; kz17 comb-stab anchor; kz197 prefix-80 living pin. |
| r450 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/prefix_mincut_probe.py` | n_stab pack B_w; frequently_selected_prefix_augDualResolvent_ge_half. |
| r450 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/prefix_mincut.pdf` | Prefix-object split charts; n_stab growth fit; chi-prefix vs edge-dead chi. |
| r450 companion | OPERATOR_SPECTRAL | `rh/problem/prefix_mincut.tex` | n_stab-pack vs full-window split; object-pure M2 chart; χ prefix-live pin; Lean Iff.rfl. |
| r450 companion | OPERATOR_SPECTRAL | `rh/problem/verify_prefix_mincut.py` | n_stab-pack vs full-window split; object-pure M2 chart; χ prefix-live pin; Lean Iff.rfl. |
| r451 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/nstab_transition_probe.py` | Prefix q plateau; n_res=L/2 mismatch. |
| r451 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/nstab_transition.pdf` | n_stab/n_res pins; scramble collapse of plateau; kz17 q-cliff. |
| r451 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/nstab_transition.tex` | n_stab/n_res pins; scramble collapse of plateau; kz17 q-cliff. |
| r451 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_nstab_transition.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r452 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/plateau_theorem_probe.py` | q_*=M_d/(M_d+5/7); degreewise fold-moment cofinality reduction. |
| r452 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/plateau_theorem.pdf` | Exact pack grade-0 identity; sister kz136/137 moment-vs-q control. |
| r452 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/plateau_theorem.tex` | Exact pack grade-0 identity; sister kz136/137 moment-vs-q control. |
| r452 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_plateau_theorem.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r453 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/border_mass_probe.py` | delta=(5/7-rho_n)/B_w; M_d signed folded m_0. |
| r453 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/border_mass.pdf` | Pack identity q_n=S_{n-1}/B_w; scramble race pin; M_d vs N growth. |
| r453 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/border_mass.tex` | Pack identity q_n=S_{n-1}/B_w; scramble race pin; M_d vs N growth. |
| r453 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_border_mass.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r454 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/limit_object_probe.py` | ARCH-fold moment limit; Lipschitz dq/dm_2. |
| r454 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/limit_object.pdf` | m_inf vs ARCH pins; Lipschitz/drop-500 controls; rho_16 chain. |
| r454 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/limit_object.tex` | m_inf vs ARCH pins; Lipschitz/drop-500 controls; rho_16 chain. |
| r454 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_limit_object.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r455 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/arch_chain_probe.py` | 3-lag ARCH identity; J_P and J_B=BG_DU/Delta. |
| r455 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/arch_chain.pdf` | 3-lag identity; J_B=BG_DU/Δ; MAIN-ARCH kernel pin. |
| r455 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/arch_chain.tex` | 3-lag identity; J_B=BG_DU/Δ; MAIN-ARCH kernel pin. |
| r455 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_arch_chain.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r456 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/vacuity_redteam_probe.py` | MAIN-vs-ARCH world pair; combRead tent U=2 constant. |
| r456 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/vacuity_redteam.pdf` | MAIN-vs-ARCH worlds test; kz69 Δq pin; combRead onset. |
| r456 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/vacuity_redteam.tex` | MAIN-vs-ARCH worlds test; kz69 Δq pin; combRead onset. |
| r456 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_vacuity_redteam.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r457 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/jp_increment_probe.py` | Race ratio Delta q/(1-q*); J_P onset. |
| r457 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/jp_increment.pdf` | Delta-rho drift pin; k=10 race-eats-margin; scramble increment. |
| r457 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/jp_increment.tex` | Delta-rho drift pin; k=10 race-eats-margin; scramble increment. |
| r457 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_jp_increment.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r458 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/cofinal_family_probe.py` | Lean selectedMesh k=5..16; SCAN_KZ 76 pre-pack windows. |
| r458 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/cofinal_family.pdf` | Lean k=10 mesh pin; TABLE_CAP wall; kz197 capped-dead revival. |
| r458 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/cofinal_family.tex` | Lean k=10 mesh pin; TABLE_CAP wall; kz197 capped-dead revival. |
| r458 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_cofinal_family.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r459 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/fullcomb_cleanup_probe.py` | Full a^2 comb race table; Lean selectedMesh exact dps=50. |
| r459 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/fullcomb_cleanup.pdf` | Full-comb race table; Lean a=641 live window; kz137 outside-mincut pin. |
| r459 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/fullcomb_cleanup.tex` | Full-comb race table; Lean a=641 live window; kz137 outside-mincut pin. |
| r459 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_fullcomb_cleanup.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r460 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/race_proof_probe.py` | q=sum /⟨u,e_j⟩/^2/(1-λ_j); fixed-r plateau cardinality 2r+1. |
| r460 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/race_proof.pdf` | Exact rational spectral/two-band wards; full-comb k=5..12 pins. |
| r460 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/race_proof.tex` | Exact rational spectral/two-band wards; full-comb k=5..12 pins. |
| r460 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_race_proof.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r461/r638L | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/narrowband_weil_probe.py` | GridElement even dyadic piecewise-linear autocorrelation; completed mincut translation. |
| r462 | LEAN_FORMALIZATION | `experiments/tfpt-discovery/gapmap_probe.py` | Historical gap map; sealed diagnostic only. |
| r463 | LEAN_FORMALIZATION | `rh/problem/verify_lean_fidelity.py` | Fidelity-repair artefact pins. |
| r463/r638L | LEAN_FORMALIZATION | `experiments/tfpt-discovery/lean_fidelity_probe.py` | FaithfulFold pipeline; ArchGaussMellinDigammaIdentity explicit hypothesis. |
| r464 | LEAN_FORMALIZATION | `rh/problem/verify_inner_bridges.py` | Lean sorry-census helper shared with sibling verifiers. |
| r464/r638L | LEAN_FORMALIZATION | `experiments/tfpt-discovery/inner_bridges_probe.py` | Finite PSD half; concrete near/far lag integrals. |
| r467 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/overlap_mechanism_probe.py` | Top-mode frequency alignment; scramble destroy test. |
| r467 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/overlap_mechanism.pdf` | Top-mode alignment vs ARCH control; Abel stop-gate; scramble alignment kill. |
| r467 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/overlap_mechanism.tex` | Top-mode alignment vs ARCH control; Abel stop-gate; scramble alignment kill. |
| r467 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_overlap_mechanism.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r468 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/octave_renorm_probe.py` | n<a live-source observation; interval-certified k=13..16. |
| r468 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/octave_renorm.pdf` | Isolated-octave r-sequence; 8→9 edge; Delta-halving two-point test. |
| r468 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/octave_renorm.tex` | Isolated-octave r-sequence; 8→9 edge; Delta-halving two-point test. |
| r468 companion | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_octave_renorm.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r469 | EXTERNAL_ADJUDICATION | `rh/problem/correlation_wall_judgment.pdf` | Binding anti-list; scramble gate; dual-extremal q-dagger and det-ratio 1-q diagnoses. |
| r469 | EXTERNAL_ADJUDICATION | `rh/problem/correlation_wall_judgment.tex` | Binding anti-list; scramble gate; dual-extremal q-dagger and det-ratio 1-q diagnoses. |
| r470 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/quadrep_probe.py` | Lean quadraticRepresentation_refuted_of_negative_read; meshExp witness. |
| r470 | SCREW_SUBORDINATION_LSTAR | `rh/problem/quadrep.pdf` | SelectedOnsetCompatibleNegativeRead; exists_mesh_compatible_steps_gt_cap. |
| r470 | SCREW_SUBORDINATION_LSTAR | `rh/problem/quadrep.tex` | SelectedOnsetCompatibleNegativeRead; exists_mesh_compatible_steps_gt_cap. |
| r470 companion/r638L | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_quadrep.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r471 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/classical_cert_probe.py` | Dictionary-free Q=A-P+Pi evaluator; interval Cholesky grid family. |
| r471 | WEIL_POSITIVITY_WINDOWS | `rh/problem/classical_cert.pdf` | Dictionary-free Q=A-P+Π; interval Toeplitz Q_L; YB L=0.30 calibration. |
| r471 | WEIL_POSITIVITY_WINDOWS | `rh/problem/classical_cert.tex` | Dictionary-free Q=A-P+Π; interval Toeplitz Q_L; YB L=0.30 calibration. |
| r471 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_classical_cert.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r473 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/extraction_joint_probe.py` | Arch tent-error identity; polynomial A_cap bridge lemmas. |
| r473 | SCREW_SUBORDINATION_LSTAR | `rh/problem/extraction_joint.pdf` | fullRead_weilForm_gap_eq_arch; selectedACapPsdImpliesPolynomialReads. |
| r473 | SCREW_SUBORDINATION_LSTAR | `rh/problem/extraction_joint.tex` | fullRead_weilForm_gap_eq_arch; selectedACapPsdImpliesPolynomialReads. |
| r473 companion/r638L | SCREW_SUBORDINATION_LSTAR | `rh/problem/verify_extraction_joint.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r474 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/modulus_upgrade_probe.py` | Exact S_eff(L); Jackson H^2 interpolant constants. |
| r474 | WEIL_POSITIVITY_WINDOWS | `rh/problem/modulus_upgrade.pdf` | S_eff(L) exact; C_Π=8 sinh L; Jackson 1/π^2 interpolants. |
| r474 | WEIL_POSITIVITY_WINDOWS | `rh/problem/modulus_upgrade.tex` | S_eff(L) exact; C_Π=8 sinh L; Jackson 1/π^2 interpolants. |
| r474 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_modulus_upgrade.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r475 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/arch_rate.pdf` | weilArchSide u-space pairing; err/Δ^2 witness table k=5..12. |
| r475 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/arch_rate.tex` | weilArchSide u-space pairing; err/Δ^2 witness table k=5..12. |
| r475 companion/r638L | EXPLICIT_FORMULA_IDENTITY | `rh/problem/verify_arch_rate.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r475-repair | LEAN_FORMALIZATION | `rh/lean/RH/SelectedArchErrorQuadraticRateClassical.lean` | Explicit 1/12 estimate, endpoint-kink defect, corrected Exists-rate interface, and tendsto consumer. |
| r475/r638L | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/arch_rate_probe.py` | Named Prop GaussDigammaIntegralRepresentation; tent-rate evaluator. |
| r476 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/crossterm_probe.py` | Route-B 1-mode Rayleigh; regularized Peano vs weilArchSide. |
| r476 | WEIL_POSITIVITY_WINDOWS | `rh/problem/crossterm.pdf` | First-Dirichlet H^2 ball; sigma_A(0) pin; Peano C0 interval. |
| r476 | WEIL_POSITIVITY_WINDOWS | `rh/problem/crossterm.tex` | First-Dirichlet H^2 ball; sigma_A(0) pin; Peano C0 interval. |
| r476 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_crossterm.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r477 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/highmode_probe.py` | sigma_A = Re psi(1/4+it/2)-log pi; Bose identity checks. |
| r477 | WEIL_POSITIVITY_WINDOWS | `rh/problem/highmode.pdf` | sigma_A=Re psi(1/4+it/2)-log π; t0 schedule; direct 2×2 Schur_lo. |
| r477 | WEIL_POSITIVITY_WINDOWS | `rh/problem/highmode.tex` | sigma_A=Re psi(1/4+it/2)-log π; t0 schedule; direct 2×2 Schur_lo. |
| r477 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_highmode.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r478 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/endtoend_fixedl_probe.py` | Even Fourier Gram interval certificates at L=0.3. |
| r478 | WEIL_POSITIVITY_WINDOWS | `rh/problem/endtoend_fixedl.pdf` | Even Fourier Gram; Higham congruence PD; K_P almost-periodic gain. |
| r478 | WEIL_POSITIVITY_WINDOWS | `rh/problem/endtoend_fixedl.tex` | Even Fourier Gram; Higham congruence PD; K_P almost-periodic gain. |
| r478 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_endtoend_fixedl.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r479 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/lambdastar03_probe.py` | Digamma t_c enclosure; even/odd Pi rank-one forms. |
| r479 | WEIL_POSITIVITY_WINDOWS | `rh/problem/lambdastar03.pdf` | Digamma t_c enclosure; tr(K)=2L t_c/π; interlacing minorant. |
| r479 | WEIL_POSITIVITY_WINDOWS | `rh/problem/lambdastar03.tex` | Digamma t_c enclosure; tr(K)=2L t_c/π; interlacing minorant. |
| r479 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_lambdastar03.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r480 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kappa_high_probe.py` | Nyström Slepian kappa_high estimator; refined-Schur remainder. |
| r480 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kappa_high.pdf` | Nyström kappa_high scan; refined S=B-CC^T/c_tail; crude-kill pin. |
| r480 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kappa_high.tex` | Nyström kappa_high scan; refined S=B-CC^T/c_tail; crude-kill pin. |
| r480 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_kappa_high.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r481 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/schur_cert_probe.py` | Entire-sinc GL remainder; IBP tail envelope. |
| r481 | WEIL_POSITIVITY_WINDOWS | `rh/problem/schur_cert.pdf` | Nyström-Slepian interpolant; ε lift from entire sinc; c_tail proof. |
| r481 | WEIL_POSITIVITY_WINDOWS | `rh/problem/schur_cert.tex` | Nyström-Slepian interpolant; ε lift from entire sinc; c_tail proof. |
| r481 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_schur_cert.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r482 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/carleson_edgeband_probe.py` | Dyadic F_k(t) census; pooled log-log fit controls. |
| r482 | WEIL_POSITIVITY_WINDOWS | `rh/problem/carleson_edgeband.pdf` | Finite F_k envelope; pooled log-log; Christoffel overshoot; strict-F scramble. |
| r482 | WEIL_POSITIVITY_WINDOWS | `rh/problem/carleson_edgeband.tex` | Finite F_k envelope; pooled log-log; Christoffel overshoot; strict-F scramble. |
| r482 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_carleson_edgeband.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r483 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/filon_enclosure_probe.py` | Filon [0,150] enclosure; 4-term IBP tail. |
| r483 | WEIL_POSITIVITY_WINDOWS | `rh/problem/filon_enclosure.pdf` | Filon remainder bound; Higham mu on finite S; leftover-C HS deficit. |
| r483 | WEIL_POSITIVITY_WINDOWS | `rh/problem/filon_enclosure.tex` | Filon remainder bound; Higham mu on finite S; leftover-C HS deficit. |
| r483 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_filon_enclosure.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r484 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/block_completion_probe.py` | Garbage criterion /u(L)/ n vs 2n; leftover-vs-block table. |
| r484 | WEIL_POSITIVITY_WINDOWS | `rh/problem/block_completion.pdf` | Garbage /u(L)/ n-vs-2n criterion; leftover-drop table; QR-IBP kill. |
| r484 | WEIL_POSITIVITY_WINDOWS | `rh/problem/block_completion.tex` | Garbage /u(L)/ n-vs-2n criterion; leftover-drop table; QR-IBP kill. |
| r484 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_block_completion.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r485 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weighted_schur_probe.py` | Weighted-Schur S_w constructor; A-first hi-frac test. |
| r485 | WEIL_POSITIVITY_WINDOWS | `rh/problem/weighted_schur.pdf` | A-first leftover hi-frac; weighted S_w Higham; checkpoint freeze. |
| r485 | WEIL_POSITIVITY_WINDOWS | `rh/problem/weighted_schur.tex` | A-first leftover hi-frac; weighted S_w Higham; checkpoint freeze. |
| r485 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_weighted_schur.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r486 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/woodbury_minf_probe.py` | t_c Slepian enemy basis; Birman–Schwinger G-certificate pattern. |
| r486 | WEIL_POSITIVITY_WINDOWS | `rh/problem/woodbury_minf.pdf` | Slepian enemy spectrum; Birman-Schwinger lmax; Q_E Higham pin. |
| r486 | WEIL_POSITIVITY_WINDOWS | `rh/problem/woodbury_minf.tex` | Slepian enemy spectrum; Birman-Schwinger lmax; Q_E Higham pin. |
| r486 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_woodbury_minf.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r487 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/outer_bridges.pdf` | FullWeilTest autocorrelation class; fullWeil_channel_continuity; zeta wrapper. |
| r487 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/outer_bridges.tex` | FullWeilTest autocorrelation class; fullWeil_channel_continuity; zeta wrapper. |
| r487 companion/r638L | EXPLICIT_FORMULA_IDENTITY | `rh/problem/verify_outer_bridges.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r487/r638L | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/outer_bridges_probe.py` | fullWeil_fixedSupport_grid_density; zeta endpoint interface. |
| r488 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/resolvent_solve_probe.py` | Shifted resolvent G-certificate; non-coercivity census. |
| r488 | WEIL_POSITIVITY_WINDOWS | `rh/problem/resolvent_solve.pdf` | Shifted G^{1/2} B G^{1/2} certificate; r486 BSE recovery; N=5 tail. |
| r488 | WEIL_POSITIVITY_WINDOWS | `rh/problem/resolvent_solve.tex` | Shifted G^{1/2} B G^{1/2} certificate; r486 BSE recovery; N=5 tail. |
| r488 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_resolvent_solve.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r489 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/outer_bridges2.pdf` | Common-anchor finite-comb continuity; bounded-cosh polar integral. |
| r489 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/outer_bridges2.tex` | Common-anchor finite-comb continuity; bounded-cosh polar integral. |
| r489 companion/r638L | EXPLICIT_FORMULA_IDENTITY | `rh/problem/verify_outer_bridges2.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r489/r638L | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/outer_bridges2_probe.py` | Common-anchor comb continuity; polar-integral lemma. |
| r490 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/operator_residual_probe.py` | Operator-residual vs BS-margin diagnostic. |
| r490 | WEIL_POSITIVITY_WINDOWS | `rh/problem/operator_residual.pdf` | Off-space /s residual; GL-tiny-not-certificate diagnostic; FINAL_CHECKPOINT. |
| r490 | WEIL_POSITIVITY_WINDOWS | `rh/problem/operator_residual.tex` | Off-space /s residual; GL-tiny-not-certificate diagnostic; FINAL_CHECKPOINT. |
| r490 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_operator_residual.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r491 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/outer_bridges3.pdf` | dyadicSampleGrid support bound; polar +2 cosh pin 2.042015443302091. |
| r491 | EXPLICIT_FORMULA_IDENTITY | `rh/problem/outer_bridges3.tex` | dyadicSampleGrid support bound; polar +2 cosh pin 2.042015443302091. |
| r491 companion/r638L | EXPLICIT_FORMULA_IDENTITY | `rh/problem/verify_outer_bridges3.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r491/r638L | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/outer_bridges3_probe.py` | Corrected +2*cosh polar normalization; Lipschitz support-length contracts. |
| r492 | EXTERNAL_ADJUDICATION | `rh/problem/keystone_judgment.pdf` | x-space k(x)=e^{x/2}/sinh x; c_L pin; Loewner-safe truncation diagnosis. |
| r492 | EXTERNAL_ADJUDICATION | `rh/problem/keystone_judgment.tex` | x-space k(x)=e^{x/2}/sinh x; c_L pin; Loewner-safe truncation diagnosis. |
| r494 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kernel_loewner_probe.py` | x-space digamma kernel; Bernstein-ellipse Loewner pads; c_L enclosure. |
| r494 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_loewner.pdf` | Zero-extension translation; quintic C2 cutoff; 3× HS off-block charge. |
| r494 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_loewner.tex` | Zero-extension translation; quintic C2 cutoff; 3× HS off-block charge. |
| r494 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_kernel_loewner.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r495 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kernel_redteam_probe.py` | Independent digamma x-space identity tests; interval translation norms. |
| r495 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_redteam.pdf` | False doubled-c_L world; exact-Q boundary masses; Clenshaw-Curtis order 1025. |
| r495 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_redteam.tex` | False doubled-c_L world; exact-Q boundary masses; Clenshaw-Curtis order 1025. |
| r495 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_kernel_redteam.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r496 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kernel_loewner08_probe.py` | Factor-two prime g(0) calibration; L=0.8 G0/G1 stops. |
| r496 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_loewner08.pdf` | x-space identity, factor-two prime normalization, r471/r477 calibration stops. |
| r496 | WEIL_POSITIVITY_WINDOWS | `rh/problem/kernel_loewner08.tex` | Factor-two prime g(0) mass; interlacing n≤800 NO-GO; off-block op-norm. |
| r496 companion | WEIL_POSITIVITY_WINDOWS | `rh/problem/verify_kernel_loewner08.py` | Gate harness, scramble pins, and sealed CERT/SHAPE token checks. |
| r502 | WEIL_POSITIVITY_WINDOWS | `rh/problem/l08_judgment.pdf` | Same numerals as l08_judgment.tex. |
| r502 | WEIL_POSITIVITY_WINDOWS | `rh/problem/l08_judgment.tex` | Odd Legendre witness, Galerkin ceiling ladder, kappa_w table, anti-list F-VII N5–N10. |
| r517-r532/r638L | LEAN_FORMALIZATION | `rh/lean/RH/ExternalBridges.lean` | contour_identity_fixed_T, horizontalEdgesTendstoZero, hat_fourier_inversion, rightVerticalIntegral_eq_prime_sum. |
| r517-r634L/r638L | LEAN_FORMALIZATION | `rh/lean/RH/Audit.lean` | #print axioms checklist; named-open list. |
| r517-r638L | LEAN_FORMALIZATION | `rh/lean/RH/Open.lean` | Sorry classification R/T/A; gabor_primeSide_rational_criterion_iff_rh statement. |
| r535 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_separation_redteam_probe.py` | Off-critical injection grid; truncated Rayleigh search harness. |
| r536 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/kernel_loewner_window_probe.py` | Frozen r494 Loewner window mapper; block-Schur tail alternative. |
| r537 | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/honest_contour_audit_probe.py` | 40-digit contour identity suite; g*cosh dictionary map. |
| r539 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_gaussian_separation_probe.py` | Trudgian JNT 134 certified tail label; crude-safe C=4 majorant. |
| r540 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_online_null_separation_probe.py` | On-line nullspace constructor; support-vs-height frontier table. |
| r541 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_gabor_separation_probe.py` | Gabor lock a=sigma^2/64, omega=gamma-pi a/sigma; certified-mass cells. |
| r542-r617L | LEAN_FORMALIZATION | `rh/lean/RH.lean` | RH.lean import order; proved-vs-sorry README pointer. |
| r542-r634L | LEAN_FORMALIZATION | `rh/lean/RH/GaborSeparation.lean` | gabor_inputs_to_mathlib_rh; noncompact Gabor class. |
| r543 | LEAN_FORMALIZATION | `rh/lean/RH/GaborIntegral.lean` | integral_cexp_neg_half_mul_sq_add; pure-Gabor hat representation. |
| r544 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_uniform_inequality_probe.py` | Exact pure-Gabor closed forms; unit-bin C=4 majorant. |
| r544/r552/r579 | LEAN_FORMALIZATION | `rh/lean/RH/GaborInequality.lean` | gaborScalingOmega; gauss_density_transfer_binMax alias. |
| r546 | LEAN_FORMALIZATION | `rh/lean/RH/ZeroIncrement.lean` | gaborZeroCount; explicit 2*zetaZerosInDiskCardBoundInner. |
| r548 | EXPLICIT_FORMULA_IDENTITY | `experiments/tfpt-discovery/weil_gabor_explicit_formula_probe.py` | Correct comb 2*Lambda/sqrt(n); EF residual suite. |
| r549 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_density_transfer_probe.py` | Uniform transfer bound 15079.64; offline-adversarial config. |
| r551 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_extremal_selection_probe.py` | Extremal-selection budget; spectral-gap threshold 0.919. |
| r552/r579 | LEAN_FORMALIZATION | `rh/lean/RH/GaborThetaBound.lean` | gauss_binMax_tsum_le; gauss_online_mass_uniform. |
| r553 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_config_first_probe.py` | Config-first cluster/game catalogs; leftover W_left scores. |
| r554 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_mixture_witness_probe.py` | Signed/positive mixture classes; leftover-opt 1-packet cover test. |
| r555/r587 | LEAN_FORMALIZATION | `rh/lean/RH/GaborHatAnalytic.lean` | norm_gaborHat_le_poly_three_lobe; FE-symmetry hat_W(1-s)=hat_W(s). |
| r557 | LEAN_FORMALIZATION | `rh/lean/RH/GaborHorizontalEdges.lean` | norm_horizontal_logDeriv_gaborHat_integral_le. |
| r557/r587 | LEAN_FORMALIZATION | `rh/lean/RH/GaborZeroSummable.lean` | summable_gaborHat_over_zeros_quartic; log-versus-Gaussian comparison. |
| r557/r631L | LEAN_FORMALIZATION | `rh/lean/RH/GaborContourResidue.lean` | contour_identity_fixed_T_of_entire. |
| r558/r564/r581/r634L | LEAN_FORMALIZATION | `rh/lean/RH/GaborExplicitFormula.lean` | gabor_explicitFormula_of_remainders; of_parts remainder split. |
| r560 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_honest_weil_game_probe.py` | W_honest = Q_off+R_on evaluator; increment-compliant catalog. |
| r561 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_uniform_dominance_probe.py` | Isolation-shrink (a,omega) rule; afac=1/8 lock. |
| r562/r568/r571/r589 | LEAN_FORMALIZATION | `rh/lean/RH/GaborDominance.lean` | isolationShrink; GaborCanonicalConfig (gamma>0, omega>0). |
| r563 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_dominance_redteam_probe.py` | Equal-sigma twin-at-minus-omega adversary. |
| r564/r581 | LEAN_FORMALIZATION | `rh/lean/RH/GaborVertical.lean` | gabor_rightVerticalIntegral_eq_prime_sum; gabor_hat_fourier_inversion. |
| r565 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_scramble_gate_probe.py` | Late r469 scramble-gate harness for Gabor forms. |
| r567 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_canonical_dominance_probe.py` | Canonical (gamma>0, omega>0) isolation-shrink; 119-cell catalog. |
| r569/r597 | LEAN_FORMALIZATION | `rh/lean/RH/GaborDominanceProof.lean` | gaborHost_unique_gamma_of_isolated; gaborSmallnessA. |
| r570 | LEAN_FORMALIZATION | `rh/lean/RH/GaborLeftVertical.lean` | gaborLeftPrimeReflection_holds; psi(1/4)=-gamma-3log2-pi/2 spec. |
| r571/r597 | LEAN_FORMALIZATION | `rh/lean/RH/GaborDominanceAssembly.lean` | Far/plus/on-line packing constants; RemainderBudget. |
| r572 | LEAN_FORMALIZATION | `rh/lean/RH/GaborAutocorrelation.lean` | gabor_carrier_of_pure; GaborHalfCombReal. |
| r574/r575/r597/r598 | LEAN_FORMALIZATION | `rh/lean/RH/GaborDominanceLog.lean` | gaborKBinAt; LogFarPacking; RemainderBudgetLog. |
| r576 | LEAN_FORMALIZATION | `rh/lean/RH/GaborVerticalLimit.lean` | Landau-gap T-sequence; gaborContourVerticalLimit_holds. |
| r577 | LEAN_FORMALIZATION | `rh/lean/RH/GaborArchDigamma.lean` | logDeriv_zetaFEFactor_criticalLine; GammaR reflection. |
| r578/r581 | LEAN_FORMALIZATION | `rh/lean/RH/GaborArchContour.lean` | logDeriv_zetaFEFactor_pole_split; arch contour T-shift. |
| r579-r589 | LEAN_FORMALIZATION | `rh/lean/RH/GaborSpectralBridge.lean` | gaborLogThreeLobeMajorant_le_closed; log-occupancy transfer. |
| r582/r583/r589/r597 | LEAN_FORMALIZATION | `rh/lean/RH/GaborDominanceLog2.lean` | GaborRemainderBudgetLog2; online_exp_le_log. |
| r582/r585 | LEAN_FORMALIZATION | `rh/lean/RH/GaborFEMultiplicity.lean` | riemannZetaMultiplicity_eq_one_sub_all; sum_multiplicity_stripZerosWindow_le. |
| r590/r600/r605A | LEAN_FORMALIZATION | `rh/lean/RH/GaborArithmeticSeparator.lean` | gabor_arithmetic_inputs_to_mathlib_rh implication. |
| r591 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_fixed_packet_cofinal_probe.py` | Fixed-packet cofinal host catalog; epsilon-floor scan. |
| r592 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_window_adaptive_tail_probe.py` | Window-adaptive (a,omega) rule; tail-metric checker. |
| r593/r594/r600 | LEAN_FORMALIZATION | `rh/lean/RH/GaborOuterTail.lean` | gaborOuterTail_num_le_neg_quarter; gaborWindowAdaptiveRule_exists. |
| r595 | LEAN_FORMALIZATION | `rh/lean/RH/GaborWindowGlue.lean` | gaborHonestWeil_window_add_outer; lockDelta T-free factor. |
| r596-r600 | LEAN_FORMALIZATION | `rh/lean/RH/GaborAnchoredWitness.lean` | GaborAnchoredWindowWitnessAt type-bundle; log-glue. |
| r601 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_weil_positivity_subfamily_probe.py` | Pure-Gabor prime+digamma Z reader; omega0(a) threshold. |
| r603 | PRIME_EVENT_LOG_DECODING | `experiments/tfpt-discovery/prime_inequality_evosearch_probe.py` | Two-key GP filter; density-preserving scramble worlds. |
| r604 | OTHER | `experiments/tfpt-discovery/tfpt_spectrum_zero_crosscorr_probe.py` | Unfolding null battery; TFPT-spectrum vs gamma table. |
| r605B/r605C | LEAN_FORMALIZATION | `rh/lean/RH/GaborExposedOrbit.lean` | gaborScore; ExposedOrbit; gaborExposedOrbitAssembly_holds. |
| r605N | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_exposed_orbit_probe.py` | Exposed-orbit score S; phase-lock cos=-1; three-lobe majorant. |
| r606 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/connes_prolate_residual_gap_probe.py` | Tall Slepian/Fourier residual-gap ladder; Davis–Kahan eta. |
| r607 | PRIME_EVENT_LOG_DECODING | `experiments/tfpt-discovery/event_lindblad_twokey_probe.py` | Four-world Lindblad/Q_W battery; Euler-Pick Gram scalars. |
| r608 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/gabor_tropical_heat_probe.py` | Tropical F(omega)=sup S_rho; traveling-lobe heat identity. |
| r609 | LATTICE_E8_HECKE | `experiments/tfpt-discovery/e8_directed_readout_probe.py` | Seifert S+S^T=A checks; Phi_30 charpoly; H_8 enumerator. |
| r611 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/connes_observable_aubin_nitsche_probe.py` | Observable Aubin–Nitsche eta_obs; hybrid Q_lambda spectrum. |
| r612C/r634L | LEAN_FORMALIZATION | `rh/lean/RH/GaborCountableCriterion.lean` | GaborZeroSideContinuous; overspecified forall-zero Prop warning. |
| r613 | LATTICE_E8_HECKE | `experiments/tfpt-discovery/prime_e8_ordered_herglotz_probe.py` | Siegel-half-space Im W test; ordered Seifert deformation. |
| r615 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/semilocal_firststep_probe.py` | One-prime window Q_L; v1017 x-space arch kernel; G0/G1 calibration. |
| r616 | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/inertia_highermoment_probe.py` | A–F rank-trace replay; moment-support obstruction table. |
| r617 | LATTICE_E8_HECKE | `experiments/tfpt-discovery/e8_coxeter_euler_completion_probe.py` | cyclotomic30 identities; D_E8(s) Euler product. |
| r617L | LEAN_FORMALIZATION | `rh/lean/RH/CoxeterCompletion.lean` | cyclotomic30_explicit; completion_linear_coeff_zero. |
| r617L | LEAN_FORMALIZATION | `rh/lean/RH/PrimeLogIndependence.lean` | linearIndependent_log_primes; log_ratio_irrational. |
| r618 | LATTICE_E8_HECKE | `experiments/tfpt-discovery/jensen_compiler_rigidity_probe.py` | Random M S M* Phi_30 invariance; Jensen C_{n,8} grid-distance. |
| r619 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/support_relay_census_probe.py` | Support-event lead Delta_q; copied r615 window form. |
| r620 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/p2_reflection_factor_probe.py` | Odd-sector reflection identity; E_- dimension census. |
| r621 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/p2_digamma_duplication_probe.py` | Digamma-duplication check; ARCH operator split. |
| r622 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/support_darboux_probe.py` | Scaled Qtilde(L) transport residual; c0(L) formula. |
| r623 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/semilocal_p2_dilation_probe.py` | m2 Poisson-kernel multiplier; r623/r624 dilation obstruction. |
| r625 | RHP_IIKS_TAU | `experiments/tfpt-discovery/iiks_vanishing_metric_probe.py` | Discrete IIKS jump J_s; Zhou unitarity check. |
| r626 | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/xi_finitefree_collision_probe.py` | dBN heat-flow discriminant identity; Xi Taylor-section detector. |
| r627 | TOEPLITZ_MOMENT_POSITIVITY | `experiments/tfpt-discovery/af_twomoment_optimizer_probe.py` | A–F two-moment R(psi); Montgomery–Taylor critical point. |
| r628 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/window_box_verifier_probe.py` | 40-digit window-form builder; interval Cholesky/Weyl. |
| r629 | CERTIFICATE_INFRASTRUCTURE | `experiments/tfpt-discovery/certificate_class_atlas_probe.py` | Certificate-class LP atlas; A1 two-moment baseline. |
| r630 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/margin_law_symreg_probe.py` | Tall QR/SVD margin pipeline; N-sweep lambda*(L) table. |
| r632 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/jet_deflated_ldet_probe.py` | Jet-deflated window form; L_det gain G. |
| r633 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/frontier_followups_probe.py` | a_max(sigma,gamma*) fit; Haar random-Euler battery; Hellmann–Feynman dBN. |
| r635 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/relay_lead_precision_probe.py` | mp Cholesky lead bisection; D1/D2 event forms. |
| r635 | PRIME_EVENT_LOG_DECODING | `experiments/tfpt-discovery/relay_lead_precision_result.json` | Converged Delta_2..Delta_5 table replacing the r619 N=80 artefact. |
| r636 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/relay_lead_law_probe.py` | Four-model lead-law suite on sealed r635 JSON. |
| r636 | PRIME_EVENT_LOG_DECODING | `experiments/tfpt-discovery/relay_lead_law_result.json` | Lead-law model residuals against the r635 table. |
| r637 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/relay_vote_map_probe.py` | Mode vote map; R_q-odd flip counterexample at L=0.40,q=2. |
| r638 | SELBERG_TRACE_CONTACT | `experiments/tfpt-discovery/gabor_first_contact_selberg_probe.py` | Hankel-vs-Toeplitz Selberg gate; contact-heat residual; Euler-local DC cost. |
| r638 | SELBERG_TRACE_CONTACT | `experiments/tfpt-discovery/gabor_first_contact_selberg_result.json` | Hankel-versus-Toeplitz Selberg gate and contact-condition collapse test. |
| r639 | EXTERNAL_ADJUDICATION | `experiments/tfpt-discovery/lamzouri_hilbert_adjudication_probe.py` | 921-multiset Bessel rebuild; C_eta=R(eta^2) identity; BGSTB support-one check. |
| r640 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/weil_level_n_blindness_probe.py` | Principal-character blindness identity and class-number ambiguous-form check. |
| r640 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/weil_level_n_blindness_result.json` | Chi_0 blindness and h(-4N) ambiguous-class measurements. |
| r641 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/clock_torsion_ecm_probe.py` | ECM torsion-family smoothness census on 16-bit primes. |
| r641 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/clock_torsion_ecm_result.json` | Sealed gain table versus generic Montgomery baseline. |
| r642 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/seam_geodesic_factor.py` | Deterministic Miller–Rabin plus multiplier-schedule SQUFOF solver. |
| r642 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/seam_geodesic_infrastructure_probe.py` | Seam geodesic = reduction cycle of sqrt(N); SQUFOF identification. |
| r642 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/seam_geodesic_infrastructure_result.json` | Measured geodesic and square-form exponents. |
| r642 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/tests/test_seam_geodesic_factor.py` | Miller–Rabin boundary cases and multiplier-one repair fixtures. |
| r643 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/regulator_jump_probe.py` | Oracle-free form-reduction jump on disc 4N. |
| r643 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/regulator_jump_result.json` | Counted-step G6 comparison table. |
| r644 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/regulator_relation_probe.py` | Relation collector that feeds GEOM.REGULATOR.JUMP.01. |
| r644 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/regulator_relation_result.json` | Exact integer-kernel regulator multiple. |
| r646 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/hylaean_relation_fiber_probe.py` | Information-matched relation-planner harness (no p,q leak). |
| r646 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/hylaean_relation_fiber_result.json` | Work-normalized relation-rank table. |
| r647 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/e8_composite_gauss_probe.py` | Exact E8 composite Gauss formula and CRT zero-count inversion. |
| r647 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/e8_composite_gauss_result.json` | Quartic p+q recovery from an exact Z_N. |
| r648 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/hylaean_boolean_factorgraph_probe.py` | Explicit Boolean-field multiplication energy and decoder firewall. |
| r648 | SIEVE_FACTORING_GEOMETRY | `experiments/tfpt-discovery/hylaean_boolean_factorgraph_result.json` | Per-size success and work table. |
|  | CERTIFICATE_INFRASTRUCTURE | `rh/INVENTORY.json` | Path/SHA/round/status schema consumed by run_rh.py. |
|  | OTHER | `rh/README.md` | Claim-boundary wording mirrored by paper and Lean READMEs. |
|  | LEAN_FORMALIZATION | `rh/lean/README.md` | Sorry-census chronology for the Lean pilot. |
|  | OTHER | `rh/paper/rh_program.tex` | Claim-split remarks and finite-window status boxes. |
|  | CERTIFICATE_INFRASTRUCTURE | `rh/verification/make_inventory.py` | Single writer for INVENTORY.json. |
|  | CERTIFICATE_INFRASTRUCTURE | `rh/verification/run_rh.py` | Pinned-inventory integrity plus probe-smoke runner. |
| - | OTHER | `tfpt_prime_front.tex` | Narrative map of lanes and contracts. |
| - | CERTIFICATE_INFRASTRUCTURE | `verification/status_ledger.csv` | PRIME.* rows are the status source of truth. |
| 2026-09-05-all-place-audit | ARAKELOV_HODGE_INTERSECTION | `rh/catalog/analysis/all_place_tate_audit.md` | Seven-gate A1--A7 completion contract with exact local normalization and claim fences. |
| 2026-09-05-external-heat-A | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/heat_gabor_restatement_probe.py` | Exact heat-kernel normalization, inverse transform, and fail-closed prime-tail budget. |
| 2026-09-05-external-nb-B | OPERATOR_SPECTRAL | `experiments/tfpt-discovery/nb_dyadic_capture_probe.py` | Dyadic block transform, Schur-capture computation, and 80-digit Gram cross-check. |
| 2026-09-09-arch-source-reconciliation | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/ArchRateClosure.lean` | Three exact typed ARCH interfaces; downstream searches should consume their proofs instead of reopening the corrected convergence gap. |
| 2026-09-09-frontier-source-reconciliation | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/FrontierClosure.lean` | Two conditional typed implication rules with an AND-premise; circular forward and reverse equivalence cannot create a positivity proof. |
| 2026-09-09-research-followups | WEIL_POSITIVITY_WINDOWS | `rh/catalog/analysis/research_followups_20260909.md` | Two auditable contracts with conjunctive prerequisites and explicit forbidden shortcuts. |
| ARCHIMEDEAN.PI.CONFORMITY.01 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/archimedean_pi_conformity_probe.py` | Typed archimedean decomposition, exact log-pi derivative, scramble and digit-null controls. |
| CENSUS.QSM.NORMFLOW.01 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/census_qsm_normflow_probe.py` | Exact Gaussian HNF coefficients, norm-flow semigroup action, finite KMS harness, and Hecke homogeneity obstruction. |
| CHIRAL4D.MIRROR.DET16.01 | OTHER | `experiments/tfpt-discovery/det16_plaquette_twin_probe.py` | Neutral one-particle/one-hole DET16 plaquette builder. |
| CHIRAL4D.MIRROR.DET16.01 | OTHER | `experiments/tfpt-discovery/det16_plaquette_twin_result.json` | Pinned 1D four-mode reduction numbers R1–R3. |
| CHIRAL4D.MIRROR.DET16.01 | OTHER | `experiments/tfpt-discovery/det16_traceless_rotor_twin_probe.py` | Traceless four-mode Gauss-sector twin of the uniform-charge DET model. |
| GROUPOID.HALFDENSITY.GLOBAL.01 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/groupoid_halfdensity_probe.py` | v714 groupoid fibre-census and unimodularity kill K2. |
| GROUPOID.HALFDENSITY.GLOBAL.01 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/groupoid_halfdensity_result.json` | Unimodularity witness for the rank-4 Z[i] correspondence groupoid. |
| KNESER.GROUPOID.HALFDENSITY.01 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/kneser_groupoid_halfdensity_probe.py` | Exact marked Kneser unimodularity and non-unimodular tree control. |
| MELLIN.COFACTOR.NONREAL-ZERO.01 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_cofactor_nonreal_zero_probe.py` | Complex-box Interval Newton for the Mellin cofactor F. |
| MELLIN.COFACTOR.NONREAL-ZERO.01 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_cofactor_nonreal_zero_result.json` | Three certified non-real zero boxes at 1e-13 radius. |
| MELLIN.PICK.CUSP-SADDLE.01 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_cusp_saddle_probe.py` | Exact M_repo↔I dictionary and repaired q_tail<1 saddle bookkeeping. |
| MELLIN.PICK.CUSP-SADDLE.01 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_cusp_saddle_result.json` | SPEC_SHA 97a4e916c94ad1258abc64c617eea969aececb518aaefb0d25466f8858424a53 |
| MELLIN.PICK.ZERO-RESIDUE.01 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_zero_residue_probe.py` | Proved n-tail and high-u tail lemmas for Phi balls. |
| MELLIN.PICK.ZERO-RESIDUE.01 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_zero_residue_result.json` | SPEC_SHA 05255fa3d8f032796f1ddc8ea69afa43e24c442594b616c41b3c0ed65a57bf6e |
| MELLIN.PICK.ZERO-RESIDUE.02 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_zero_residue2_probe.py` | Entire-function E_j continuation and ball winding for H on B1. |
| MELLIN.PICK.ZERO-RESIDUE.02 | MELLIN_PICK_LEE_YANG | `experiments/tfpt-discovery/mellin_pick_zero_residue2_result.json` | 512-bit B1 contour certificate plus planted-winding control. |
| PRIME.CLOCK.COMBINATION.SPECTRUM.01 | DYNAMICS_CLOCKS_PF | `experiments/tfpt-discovery/clock_combination_spectrum_probe.py` | Exact log-rational rank audit, modular integrality test, and clock-product kill classifier. |
| PRIME.PARABOLIC.DETLINE.01 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/parabolic_detline_probe.py` | Busemann/RN half-density on v714 cylinders. |
| PRIME.PARABOLIC.DETLINE.01 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/parabolic_detline_result.json` | Identity-side Connes local-term realisation on the tree boundary. |
| PRIME.PARABOLIC.DETLINE.02 | ADELIC_GROUPOID_CONNES | `experiments/tfpt-discovery/parabolic_detline2_probe.py` | Exact boundary fixed-point versus Connes-shell trace dictionary and cylinder-cutoff no-go. |
| PRIME.POSITIVE.CONE.BLINDNESS.01 | SCREW_SUBORDINATION_LSTAR | `experiments/tfpt-discovery/positive_cone_blindness_probe.py` | Exact scaling no-go, rational moment threshold, and positivity-source classification. |
| PRIME.RDAGGER.PROGRAM_EVOLUTION.01 | LEAN_FORMALIZATION | `experiments/tfpt-discovery/evolve/evolve_props.py` | Program log, exact selected-margin evaluator, arch-rate fitness, Jackson type-check, and deterministic budget kill switch. |
| SPECTATOR.OBSTRUCTION.01 | OTHER | `experiments/tfpt-discovery/spectator_sector_obstruction_probe.py` | Krylov spectator_dim and commutant separator for strip models. |
| SPECTATOR.OBSTRUCTION.01 | OTHER | `experiments/tfpt-discovery/spectator_sector_obstruction_result.json` | Chern and spectator_dim tables for B versus B⊕C. |
| T49-correction-2026-09-05 | LATTICE_E8_HECKE | `experiments/tfpt-discovery/rankin_positivity_miniature_probe.py` | Finite f8 and Delta identities plus corrected symmetric-square Euler-factor checks. |
| TELB.BOUND.A.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_bound_a_probe.py` | All-m TV Fourier tail and four-fold-cover remainder evaluator. |
| TELB.BOUND.A.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_bound_a_result.json` | Measured K3_TV and jump-removal residuals. |
| TELB.BOUND.B.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_bound_b_probe.py` | Exact saw/Hardy split and position-space s_N closed form. |
| TELB.BOUND.B.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_bound_b_result.json` | Relaxed target sum /Res_N/^2 ≤ 0.27687 for even N≥16. |
| TELB.COVER.SPLIT.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_cover_split_probe.py` | Exact 4-fold-cover coefficients and memory-light N×N remainder. |
| TELB.COVER.SPLIT.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_cover_split_result.json` | SPEC_SHA 5c9248349e917563a9edc154c064163095e4b84c2c3eeb5e60713dacf15da43e |
| TELB.KERNEL.STRUCTURE.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_kernel_structure_probe.py` | Mode-basis remainder and Hardy-difference constructors copied by later TELB probes. |
| TELB.TRACE.DECOMP.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_trace_decomposition_probe.py` | O(N^2) trace decomposition of the TEL-B remainder. |
| TELB.TRACE.DECOMP.01 | OTHER | `experiments/tfpt-discovery/mmst_telb_trace_decomposition_result.json` | Predicted dT1/dT2/dT3 = ±(2/π^2)ln 2 cancellation check. |
| TFPT.HECKE.INDEX.01 | LATTICE_E8_HECKE | `experiments/tfpt-discovery/hecke_index_theorem_probe.py` | Exact covering-index harness, Gaussian prime-splitting table, rank-eight HNF coefficients, and heat-modular counterexample. |
| WEIL.WINDOW.CERTIFICATE.01 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_window_certificate_probe.py` | Arb Legendre one-stroke assembly, Miller rigorous seeds, fft-free audit, FLINT regression. |
| WEIL.WINDOW.CERTIFICATE.01 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_window_certificate_result.json` | Arb Legendre one-stroke assembly, Miller rigorous seeds, fft-free audit, FLINT regression. |
| WEIL.WINDOW.PROFILE.SCOUT.01 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_window_profile_scout.py` | Time-domain POLE+ARCH−PRIME assembly for compact windows. |
| WEIL.WINDOW.PROFILE.SCOUT.01 | WEIL_POSITIVITY_WINDOWS | `experiments/tfpt-discovery/weil_window_profile_scout_result.json` | Even/odd lambda*(L) table for L=0.30..1.00. |
| codex-rh-scha-2:outputs/Forschungsupdate_9_September_Pruefung_und_Transfergrenzen.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/Forschungsupdate_9_September_Pruefung_und_Transfergrenzen.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Arch_Formal_2026-09-05 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Arch_Interpolation_2026-09-05.lean | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Interpolation_2026-09-05.lean` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Arch_Quadrature_Check_2026-09-05.py | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Quadrature_Check_2026-09-05.py` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Arch_Regression_2026-09-05.json | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Regression_2026-09-05.json` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Archimedischer_Konvergenzbeweis_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Archimedischer_Konvergenzbeweis_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Arithmetischer_Grundzustandsvergleich_und_Faktorisierung_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arithmetischer_Grundzustandsvergleich_und_Faktorisierung_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Arithmetischer_Relativvergleich_und_Korrektur_2026-09-09.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arithmetischer_Relativvergleich_und_Korrektur_2026-09-09.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Autonome_Kandidatensuche_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Autonome_Kandidatensuche_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Beidseitige_Restpruefung_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Beidseitige_Restpruefung_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Bessel_Paarverschiebung_und_signierte_Suche_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Bessel_Paarverschiebung_und_signierte_Suche_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Compiler_Umsetzung_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Compiler_Umsetzung_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Compiler_und_fortlaufendes_Protokoll_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Compiler_und_fortlaufendes_Protokoll_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Defektformel_und_Fourierbruecke_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Defektformel_und_Fourierbruecke_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Differentialgeometrie_Sochi_Pruefung_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Differentialgeometrie_Sochi_Pruefung_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Drei_gezielte_Reserven_lokaler_Nachweis_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Drei_gezielte_Reserven_lokaler_Nachweis_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Ereignis9_Hochraumaufloesung_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Ereignis9_Hochraumaufloesung_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Ereignis9_Vergleichsgrenze_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Ereignis9_Vergleichsgrenze_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Exakte_Prolate_Moden_und_Skalierungsgrenze_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Exakte_Prolate_Moden_und_Skalierungsgrenze_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Exakte_Wechselwirkende_Quotienten_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Exakte_Wechselwirkende_Quotienten_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Fermionischer_Ereigniscompiler_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Fermionischer_Ereigniscompiler_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Fester_Zielkern_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Fester_Zielkern_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Forschungsfortschritt_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Forschungsfortschritt_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Ganze_Versuchsfamilien_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Ganze_Versuchsfamilien_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Genetische_Struktursuche_und_Primzahlprotokoll_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Genetische_Struktursuche_und_Primzahlprotokoll_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Gesamte_ungerade_Koerzivitaet_und_Randanschluss_2026-09-09.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Gesamte_ungerade_Koerzivitaet_und_Randanschluss_2026-09-09.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Gewichtete_Saettigung_ungerader_Weg_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Gewichtete_Saettigung_ungerader_Weg_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Gezielte_Reserve_und_Rekonstruktion_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Gezielte_Reserve_und_Rekonstruktion_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Globalbruecke_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Globalbruecke_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Globale_Basis_und_Relativer_Rest_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Globale_Basis_und_Relativer_Rest_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Globale_Hilbertstruktur_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Globale_Hilbertstruktur_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Globaler_Stabilitaetsangriff_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Globaler_Stabilitaetsangriff_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Graphrekonstruktion_und_Rangbarriere_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Graphrekonstruktion_und_Rangbarriere_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Kompensierte_Uhr_und_Korrelationszeit_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Kompensierte_Uhr_und_Korrelationszeit_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Kreativer_Neustart_Primcluster_Dualitaet_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Kreativer_Neustart_Primcluster_Dualitaet_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Lean_Graph_Audit_2026-09-09 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Lean_Graph_Audit_2026-09-09/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Mischmatrix_und_arithmetische_Reserve_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Mischmatrix_und_arithmetische_Reserve_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Neubewertung_ohne_TFPT_und_neuester_Stand_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Neubewertung_ohne_TFPT_und_neuester_Stand_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Normvergleich_Radius1_und_Projektionsverluste_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Normvergleich_Radius1_und_Projektionsverluste_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Nulltemperatur_und_Ereigniscompiler_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Nulltemperatur_und_Ereigniscompiler_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Primereignisse_Randenergie_und_Operatorreserve_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Primereignisse_Randenergie_und_Operatorreserve_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Primzahlpotenz8_Volltest_und_Quartische_Kandidaten_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Primzahlpotenz8_Volltest_und_Quartische_Kandidaten_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Projizierter_Polrest_und_Primereignis8_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Projizierter_Polrest_und_Primereignis8_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Quartischer_Vollnachweis_und_Radius3_Budget_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Quartischer_Vollnachweis_und_Radius3_Budget_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Quelloperator_Resolvente_und_Rangzwei_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Quelloperator_Resolvente_und_Rangzwei_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Radius3_Volltest_und_Ereignisreserve_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Radius3_Volltest_und_Ereignisreserve_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Randabschluss_und_Residuenlimit_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Randabschluss_und_Residuenlimit_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Randenergie_Durchbruch_im_Zertifizierer_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Randenergie_Durchbruch_im_Zertifizierer_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Randenergie_Primprotokoll_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Randenergie_Primprotokoll_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Recheck_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Recheck_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Recheck_Lemmas_2026-09-05.lean | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Recheck_Lemmas_2026-09-05.lean` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Rekonstruktion_Zeitkorrelation_und_Eindeutigkeit_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Rekonstruktion_Zeitkorrelation_und_Eindeutigkeit_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Schurrest_Momente_und_Nullraum_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Schurrest_Momente_und_Nullraum_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Seam_Korrekturraum_und_nichtlinearer_Abschluss_2026-09-09.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Seam_Korrekturraum_und_nichtlinearer_Abschluss_2026-09-09.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Sessionsabgleich_und_Spektralbruecke_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Sessionsabgleich_und_Spektralbruecke_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Stationaere_Metrik_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Stationaere_Metrik_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_TFPT_Faktorisierung_Vogelperspektive_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_TFPT_Faktorisierung_Vogelperspektive_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Theta_Stabilitaetscompiler_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Theta_Stabilitaetscompiler_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Unendliche_Polspiegelung_und_Operatorbereich_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Unendliche_Polspiegelung_und_Operatorbereich_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Ungerade_Arithmetikreserve_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Ungerade_Arithmetikreserve_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Vogelperspektive_Saettigung_und_ungerader_Weg_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Vogelperspektive_Saettigung_und_ungerader_Weg_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Vollstaendige_Kantenreserve_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Vollstaendige_Kantenreserve_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Vollstaendiger_Gewichteter_Defekt_2026-09-08.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Vollstaendiger_Gewichteter_Defekt_2026-09-08.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Weiterforschung_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Weiterforschung_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Xi_Dynamik_und_Spektralhuerde_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Xi_Dynamik_und_Spektralhuerde_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Zertifikatsuche_und_Lane_Abgleich_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Zertifikatsuche_und_Lane_Abgleich_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/RH_Zustandsauswahl_2026-09-05.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Zustandsauswahl_2026-09-05.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Additiver_Anschluss_und_exakte_Positivitaetsgrenze_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Additiver_Anschluss_und_exakte_Positivitaetsgrenze_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Calabi_Yau_Pruefung_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Calabi_Yau_Pruefung_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Direktversuch_Weil_aus_GNS_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Direktversuch_Weil_aus_GNS_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Ereignislog_Quelltest_und_Vorhersage_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Ereignislog_Quelltest_und_Vorhersage_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Genus2_Exakte_Seam_Bruecke_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Genus2_Exakte_Seam_Bruecke_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Halbgruppe_Zustand_und_Fixpunktspur_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Halbgruppe_Zustand_und_Fixpunktspur_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Modulare_Normzeit_und_kritischer_Protokollzustand_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Modulare_Normzeit_und_kritischer_Protokollzustand_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Neueste_Durchbrueche_und_markierte_E8_Reparatur_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Neueste_Durchbrueche_und_markierte_E8_Reparatur_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Prym_Normfluss_und_Bereichsauswahl_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Prym_Normfluss_und_Bereichsauswahl_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Prym_Zustandsabschluss_und_Weil_Grenze_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Prym_Zustandsabschluss_und_Weil_Grenze_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Fensterfortsetzung_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Fensterfortsetzung_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Gewichtserweiterung_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Gewichtserweiterung_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Globale_Stabilitaet_und_Zweipaketkriterium_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Globale_Stabilitaet_und_Zweipaketkriterium_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Grundzustand_und_Spektralkontrolle_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Grundzustand_und_Spektralkontrolle_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Legendre_Restbereich_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Legendre_Restbereich_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Positive_Halbgewichte_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Positive_Halbgewichte_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Prim5_und_uniforme_Restkontrolle_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Prim5_und_uniforme_Restkontrolle_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Primereignis_5_und_Fenster_085_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Primereignis_5_und_Fenster_085_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Primereignisse_ohne_Wiederholungen_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Primereignisse_ohne_Wiederholungen_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Primgewichte_und_neuester_Stand_2026-09-06.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Primgewichte_und_neuester_Stand_2026-09-06.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Primketten_und_Restkopplung_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Primketten_und_Restkopplung_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Protokollkorrelationen_und_Randfehler_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Protokollkorrelationen_und_Randfehler_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Relativer_Fensterfluss_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Relativer_Fensterfluss_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Relativer_Primoperator_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Relativer_Primoperator_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Round26_und_korrigiertes_Protokoll_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Round26_und_korrigiertes_Protokoll_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Skalenbloecke_und_Round27_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Skalenbloecke_und_Round27_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_RH_Vollstaendiges_Fensterzertifikat_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_RH_Vollstaendiges_Fensterzertifikat_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/TFPT_Vogelperspektive_Ereignislog_Zeit_Entropie_2026-09-07.md | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/TFPT_Vogelperspektive_Ereignislog_Zeit_Entropie_2026-09-07.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_affine_branch_grade_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_affine_branch_grade_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_balanced_interferometer_20260910 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_balanced_interferometer_20260910/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_character_halfdensity_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_character_halfdensity_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_dominant_word_decoder_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_dominant_word_decoder_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_forward_label_reader_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_forward_label_reader_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_frobenius_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_frobenius_20260909/GRAPH_SCOPE.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_future_tomography_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_future_tomography_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_graded_return_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_graded_return_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_integral_correspondence_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_integral_correspondence_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_morita_audit_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_morita_audit_20260909/AUDIT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_morita_multiplicity_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_morita_multiplicity_20260909/REPORT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_multinorm_reference_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_multinorm_reference_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_norm_character_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_norm_character_20260909/REPORT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_padic_tower_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_padic_tower_20260909/REPORT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_rational_quotient_audit_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_rational_quotient_audit_20260909/REPORT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_relative_fock_interface_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_relative_fock_interface_20260909/REPORT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_selfcalibrated_precision_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_selfcalibrated_precision_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_solenoid_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_solenoid_20260909/GRAPH_SCOPE.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_thermal_interference_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_thermal_interference_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_transported_fock_bundle_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_transported_fock_bundle_20260909/REPORT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/compiler_word_only_fock_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_word_only_fock_20260909/CONTRACT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/cross_graph_cone_frontier_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/cross_graph_cone_frontier_20260909/DELTA_RESOURCE.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:outputs/crossfront_delta_20260909 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/crossfront_delta_20260909/READ_ONLY_DELTA.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_adaptive_reserve_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_adaptive_reserve_20260908/ADAPTIVE_PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_bessel_pair_swap_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_bessel_pair_swap_20260908/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_boundary_resolvent_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_boundary_resolvent_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_cauchy_radius3_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_cauchy_radius3_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_certificate_search_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_certificate_search_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_comparison_bracket_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_comparison_bracket_20260908/BRACKET_PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_compensated_clock_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_compensated_clock_20260908/PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_cross_structure_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_cross_structure_20260908/STABLE_QUOTIENT_NEXT.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_direct_defect_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_direct_defect_20260908/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_edge_reserve_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_edge_reserve_20260908/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_even_response_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_even_response_20260908/EVEN_PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_event9_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_event9_20260908/COLUMN_PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_event_onset_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_event_onset_20260907/EVENT_ONSET.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_extended_window_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_extended_window_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_global_stability_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_global_stability_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_graph_lift_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_graph_lift_20260908/INERTIA_REPAIR.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_interacting_quotient_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_interacting_quotient_20260908/PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_inverse_moments_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_inverse_moments_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_limit_family_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_limit_family_20260908/FAMILY_PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_mixed_gram_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_mixed_gram_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_norm_ablation_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_norm_ablation_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_odd_minimizer_transport_20260910 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_odd_minimizer_transport_20260910/PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_odd_reserve_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_odd_reserve_20260908/NEXT_GATE.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_odd_saturation_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_odd_saturation_20260908/ASSEMBLY_PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_output_resolution_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_output_resolution_20260908/AUXILIARY_REFRESH_REPAIR.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_prime8_full_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_prime8_full_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_projected_pole_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_projected_pole_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_quartic_full_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_quartic_full_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_radius3_full_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_radius3_full_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_saturation_response_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_saturation_response_20260908/ODD_ROUTE.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_session_bridge_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_session_bridge_20260908/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_shell_attachment_20260910 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_shell_attachment_20260910/PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_shell_coupling_certificate_20260910 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_shell_coupling_certificate_20260910/PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_theta_stability_compiler_20260908 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_theta_stability_compiler_20260908/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_threshold_transport_20260910 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_threshold_transport_20260910/PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/rh_xi_dynamics_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_xi_dynamics_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:research/tfpt_event_log_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/tfpt_event_log_20260907/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack10 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack10/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack3 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack3/Native_Weil_Fourier_Density.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack4 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack4/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack5 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack5/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack6 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack6/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack7 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack7/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack8 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack8/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_attack9 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack9/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_transcription2 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_transcription2/ArchLagTranscription.lean` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arch_weighted2 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_weighted2/ArchRateClosure.lean` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/arithmetic_candidate_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arithmetic_candidate_20260907/preregistration.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/big_picture_audit_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/big_picture_audit_20260907/audit.py` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/budget_attack11 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/budget_attack11/cayley_review.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/calabi_yau_review_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/calabi_yau_review_20260906/check_algebra.py` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/cauchy_attack8 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/cauchy_attack8/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/compiler_attack12 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/compiler_attack12/cohomology_candidates.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/compiler_attack13 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/compiler_attack13/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/domain_attack11 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/domain_attack11/bounded_rank_two_defect.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/dyadic_protocol_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/dyadic_protocol_20260907/block_proof.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/e8_full_carrier_dirac_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/e8_full_carrier_dirac_20260906/full_carrier_dirac_audit.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/e8_modular_weight_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/e8_modular_weight_20260906/concrete_weight_audit.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/e8_relative_generator_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/e8_relative_generator_20260907/channel_audit.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/e8_relative_trace_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/e8_relative_trace_20260906/archimedean_proof.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/e8_semigroup_completion_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/e8_semigroup_completion_20260906/affine_state_proof.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/e8_weight_escape_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/e8_weight_escape_20260906/debug_record.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/freq_attack | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/freq_attack/separated_tail_analysis.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/full_residual_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/full_residual_20260907/full_window_proof.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/genus2_domain_selection_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/genus2_domain_selection_20260906/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/genus2_marked_bridge_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/genus2_marked_bridge_20260906/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/global_attack3 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/global_attack3/ground_state_contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/global_attack4 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/global_attack4/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/global_stability_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/global_stability_20260907/preregistration.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/ground_state_control_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/ground_state_control_20260907/debug_record.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/ideal_attack7 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/ideal_attack7/arithmetic_filter_cost.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/legendre_complement_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/legendre_complement_20260907/complement_proof.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/legendre_residual_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/legendre_residual_20260907/preregistration.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/legendre_uniform_cross_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/legendre_uniform_cross_20260907/preregistration.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/markov_attack6 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/markov_attack6/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack/dyadic_annihilator.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack2 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack2/two_scale_constructive_closure.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack3 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack3/historical_lemma_warning.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack4 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack4/dilation_lift_obstruction.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack5 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack5/preregistration.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack6 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack6/log_uniform_continuity_exclusion.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack7 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack7/actual_mellin_regularization_failure.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack8 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack8/cauchy_boundary_domain_review.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/nb_attack9 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/nb_attack9/finite_native_residue_interpolation.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/newest_tfpt_bridge_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/newest_tfpt_bridge_20260906/charged_dilation_proof.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/pole_attack10 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/pole_attack10/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/pole_attack9 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/pole_attack9/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/prime5_window_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/prime5_window_20260907/preregistration.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/primitive_pair_split_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/primitive_pair_split_20260907/debug_record.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/prolate_scaling_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/prolate_scaling_20260907/PROOF.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/protocol_pair_energy_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/protocol_pair_energy_20260907/debug_record.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/prym_additive_boundary_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/prym_additive_boundary_20260906/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/prym_ratio_completion_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/prym_ratio_completion_20260906/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/prym_weil_completion_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/prym_weil_completion_20260906/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/prym_weil_transduction_20260906 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/prym_weil_transduction_20260906/README.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/renormalized_protocol_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/renormalized_protocol_20260907/preregistration.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/rh_boundary_compensation_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/rh_boundary_compensation_20260907/audit.py` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/rh_relative_reference_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/rh_relative_reference_20260907/basis_checks.json` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/rh_schur_structure_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/rh_schur_structure_20260907/probe.py` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/sochi_geometry_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/sochi_geometry_20260907/sources/sochi_differential_geometry.pdf` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/state_attack5 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/state_attack5/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/strategy_reset_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/strategy_reset_20260907/analytic_gates.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack/abel_torsion_two_point_test.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack10 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack10/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack11 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack11/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack2 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack2/common_ambient_construction.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack3 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack3/compression_relative_pairing.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack4 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack4/preregistered_folner_attempt.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack5 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack5/gamma_folner_limit.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack6 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack6/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack7 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack7/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack8 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack8/cauchy_gram_defect.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/tate_attack9 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/tate_attack9/contract.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| codex-rh-scha-2:work/window_extension_20260907 | OTHER | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/window_extension_20260907/independent_window_audit.md` | Original documents, executable sources, results and complete campaign histories remain at pinned paths. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `big_picture_2026-08-02_de.tex` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `experiments/lean4-carrier-rigidity/TfptCarrier/DenseWeilCore.lean` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `experiments/lean4-carrier-rigidity/TfptCarrier/WeilDictionary.lean` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | OPERATOR_SPECTRAL | `notes/arxiv_w1_note/note_w1_suzuki_identification.tex` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `notes/arxiv_w3_note/note_w3_detector_structure.tex` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:balance` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | LATTICE_E8_HECKE | `tfpt_prime_front.tex#sec:bigpicture` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:certification` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | OPERATOR_SPECTRAL | `tfpt_prime_front.tex#sec:frontier` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:handover` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:i5` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:kills` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | LATTICE_E8_HECKE | `tfpt_prime_front.tex#sec:motivation` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:phase2` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:status` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:theory` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `tfpt_prime_front.tex#sec:verified` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/app/prime-front/page.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/components/CodePrimesBand.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | SCREW_SUBORDINATION_LSTAR | `website/components/primefront/CenterAtlas.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/components/primefront/HonestyBanner.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/components/primefront/ModuleLadder.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/components/primefront/StorySixty.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/components/primefront/WeilArcMap.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/components/primefront/WhereWeAre.tsx` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/lib/primeFront.ts` | Section-level path for corpus search; file itself may already be catalogued. |
| doc-sweep | WEIL_POSITIVITY_WINDOWS | `website/lib/primeFrontArchive.ts` | Section-level path for corpus search; file itself may already be catalogued. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/ArchLagTranscription.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/KinkIntegral.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/NativeHinges.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/SeparatedTail.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Arch_Formal_2026-09-05/WeightedKink.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack10/NativeArchEndpoint.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack10/NativeFullFrequency.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack10/QuarterGaussBase.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack3/QuarterValue.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack4/GammaRatioMonotone.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack5/DigammaSeries.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack5/GaussIntegral.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack6/ComplexGauss.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack6/ComplexLaplace.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack6/ComplexLogSeries.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack6/GammaLogIdentification.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack6/KorpusGauss.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack7/NativeAutocorrelation.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack8/NativeFourier.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack8/NativeFourierDecay.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack8/NativeParseval.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack8/NativePhysicalFrequency.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack9/NativeWeightedIntegrability.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_attack9/NativeWeightedTonelli.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_weighted2/KinkIntegral.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_weighted2/NativeHinges.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/arch_weighted2/WeightedKink.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/freq_attack/SeparatedTail.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/global_attack3/GroundStateCertificate.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/AnchorLadder.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/AntiAliasExact.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/AuditCheck.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/AuditContract.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/AxiomCheck.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/BWKeystone.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryPolarization.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CIRoot.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CalderonProjector.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CarrierData.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CarrierRankUniqueness.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CartanDeterminants.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CellCocycle.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/Check32.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CofinalCurrent.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CofinalEnvelope.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CofinalPredefinition.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CofinalWeil.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CohomologyGrading.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CoverEmbedding.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/CoxeterPrime2.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/DeltaOneNoGo.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/DeterminantCharacter.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/EulerPick.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/ExcessSkeleton.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/FlavorFeedback.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/G31Orders.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/G31WordOrders.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/GaussianCodeBridge.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/GaussianShells.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/GlueUniqueness.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/GradeNoGo.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/GramCompactness.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/HammingCode.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/HiggsIndexShadow.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/HiggsSchemeCohomologyShadow.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/Hypercharge.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/InvolutionProjectors.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/JetSumRules.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/KreinDefect.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/KronheimerMarks.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/LatticeRigidityGeneral.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/LorentzCongruence.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/MatchedPin.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/MathlibBridge.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/MobiusUniformisation.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/MomentLaurent.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/Mu4Commutation.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/NFClosure.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/OrbitPacket.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/OrientedDeterminantCarrier.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/PacketRM14.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/ParityLemma.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/ParityWeightLaws.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/PascalLadder.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/PinchIdentity.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/PinningLemma.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/Polarization.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/PositiveC2Lift.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/PositiveDescentMaster.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/ProjectiveHamming.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/QuarticHalf.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/Radius4Algebra.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/Rigidity.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SVSkeleton.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/Sanity.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamApplicabilityLedger.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamDeckClosure.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamEdgeChern.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamEquivChain.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamResidualAxiom.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamRigidityForcing.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamStandardPair.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SeamWindingInterface.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SectorPositiveDescent.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SineGramKeystone.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SpacingProduct.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SpectralBalance.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SpectralGapAttractor.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/SquareParity.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/TraceLedger.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/TraceProjection.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallCertifiedHead.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallCofinalComposition.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz12.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz13.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz14.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz15.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz18.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz19.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz20.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz22.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz23.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz25.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz27.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz29.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz32.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz33.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz39.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz46.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz59.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadder/RungKz9.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadderAudit.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallLadderChecker.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallReducedMinuscule.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WallRegularSemisimple.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/WatataniIndexFour.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/YukawaRank.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTopForm.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| lean-source-discovery | LEAN_FORMALIZATION | `experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean` | Exact source path, hash and declaration navigation; see the separate audited rule registry. |
| ledger:CONTRACT.U.01 | OTHER | `verification/v32_rh_splitting.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:E8.COXETER.EULER.COMPLETION.01 | LATTICE_E8_HECKE | `verification/v1019_coxeter_euler_completion.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:E8.DIRECTED.READOUT.01 | LATTICE_E8_HECKE | `verification/v1018_e8_directed_readout.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.ARROW_MESSAGE.01 | LATTICE_E8_HECKE | `verification/v787_hecke_arrow_broadcast.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.CARRIER_CHECK32.01 | LATTICE_E8_HECKE | `verification/v785_hecke_check32.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.GEOM.01 | LATTICE_E8_HECKE | `verification/v535_hecke_from_geometry.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.GEOM.EICHLER.01 | LATTICE_E8_HECKE | `verification/v536_eichler_trace_layer.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.GEOM.HALFINT.01 | LATTICE_E8_HECKE | `verification/v537_halfintegral_bridge.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.GEOM.RTF.01 | WEIL_POSITIVITY_WINDOWS | `verification/v538_relative_trace_identity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.HALVINGTAILS.01 | LATTICE_E8_HECKE | `verification/v795_halving_tails_k5.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.LOCAL.CLIFFORD.01 | WEIL_POSITIVITY_WINDOWS | `verification/v806_hecke_local_clifford.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.MULTIRATE2ADIC.01 | WEIL_POSITIVITY_WINDOWS | `verification/v789_multirate_constdepth.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.POSITIVE_C2_LIFT.01 | LATTICE_E8_HECKE | `verification/v788_positive_c2_lift.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.R_MICROSTATE.01 | LATTICE_E8_HECKE | `verification/v797_r_microstate_identification.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:HECKE.SNF_THETA.01 | LATTICE_E8_HECKE | `verification/v790_snf_mu4_theta.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ABELPAIR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v761_atom_pole_abel.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ALIGNMENT.LAW.01 | LATTICE_E8_HECKE | `verification/v941_alignment_law_factorization.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ANGLE.INSTR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v552_angle_instruments.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ANTIALIAS.01 | TOEPLITZ_MOMENT_POSITIVITY | `verification/v760_antialias_exact.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.AORB.REFINEMENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v815_kraus_spread_commutant.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ARITH.HEALTHCODE12.01 | WEIL_POSITIVITY_WINDOWS | `verification/v904_healthcode12_diagnostic.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.BAEZDUARTE.01 | TOEPLITZ_MOMENT_POSITIVITY | `verification/v667_baez_duarte.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.BILINEAR.RANK.01 | WEIL_POSITIVITY_WINDOWS | `verification/v558_bilinear_rank_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.BLOCKAVERAGE.SUBSTRATE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v927_blockaverage_substrate_theorems.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.BLOCKDEFL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v670_w3_block_deflation.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.C1MECH.01 | WEIL_POSITIVITY_WINDOWS | `verification/v676_c1_mechanism.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CANCELLATION.FUNCTIONAL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v951_cancellation_functional.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CAPCHAIN.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v546_capacity_chain_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CARRIER.GRAY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v804_prime_carrier_gray.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CASCADE.VECT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v557_cascade_vector_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CASE.EDGE.CHRISTOFFEL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v902_wall_relocation_map.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CBJ.CONFLUENT.FRAME.01 | WEIL_POSITIVITY_WINDOWS | `verification/v939_cbj_frame_adjudication.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CBJ.SUBDOF.BLOCKFLOOR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v940_cbj_subdof_blockfloor.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CD.DAMPING.COMPENSATION.01 | RHP_IIKS_TAU | `verification/v872_damping_compensation.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CELLCONE.KERNELFIELD.01 | WEIL_POSITIVITY_WINDOWS | `verification/v851_cluster_kernel_field.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CENSUS.SPECTRAL.LIFT.01 | LATTICE_E8_HECKE | `verification/v946_census_krein_pencil.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CERTROOT.01 | TOEPLITZ_MOMENT_POSITIVITY | `verification/v758_simpler_certificate.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CHAINMASS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v704_chain_mass_law.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CHAINTOL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v703_chain_tolerance_scaling.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CHANNELINT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v742_channel_interference.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CHANNELSOS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v744_hecke_channel_columns.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CHEBLOEWNER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v576_cheb_loewner_edge.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CLOSEDDELTA.01 | WEIL_POSITIVITY_WINDOWS | `verification/v588_closed_delta.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.COMMENSURABILITY.MECHANISM.01 | RHP_IIKS_TAU | `verification/v949_commensurability_mechanism.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.COMMUTANT.SOS.01 | RHP_IIKS_TAU | `verification/v836_commutant_sos_closure.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CONTINUUM.UNSHORTEN.01 | WEIL_POSITIVITY_WINDOWS | `verification/v822_prime_vacuum_dilation.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CONTRACTOR.CDCORE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v869_cdcore_clarkphase.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CONTRACTOR.CHRISTOFFEL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v870_christoffel_gauss_frame.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CORNER.CHARACTER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v835_corner_hjelmslev_tower.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CORNER.EXPECTATION.01 | WEIL_POSITIVITY_WINDOWS | `verification/v838_corner_expectation_position.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CORNER.OPENDOORS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v837_corner_closure_quantifier.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.COUNTING.DOMINANCE.CLOSURES.01 | SCREW_SUBORDINATION_LSTAR | `verification/v921_counting_dominance_closures.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CP.EXTENSION.01 | WEIL_POSITIVITY_WINDOWS | `verification/v794_cp_extension_gate.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CP.INTERTWINER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v801_prime_cp_intertwiner.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CRITERIA.ATLAS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v855_invariance_atlas.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.CUTOFF.01 | WEIL_POSITIVITY_WINDOWS | `verification/v593_cutoff_completion.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DBN.HEATFLOW.01 | WEIL_POSITIVITY_WINDOWS | `verification/v938_dbn_heatflow_census.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DEEPALPHA.SIGN.01 | WEIL_POSITIVITY_WINDOWS | `verification/v877_complete_comb_reversal.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DENSE.LIMIT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v562_dense_limit_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DENSECORE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v762_dense_weil_core.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DENSITYDOM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v582_density_dominance.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DEPTHBLOCK.TRANSFER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v928_depthblock_transfer_theorems.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DETLAW.01 | WEIL_POSITIVITY_WINDOWS | `verification/v592_continuum_det_law.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.DOUBLELIMIT.REDUCTION.THEOREM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v918_doublelimit_reduction_theorem.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EDGE.CLEANUP.CLOSURES.01 | LATTICE_E8_HECKE | `verification/v925_edge_cleanup_closures.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EULER.SCHUR.SEMIGROUP.01 | WEIL_POSITIVITY_WINDOWS | `verification/v859_grade_no_go_elevator.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EULERPICK.CERTIFIED.FLOORS.01 | LATTICE_E8_HECKE | `verification/v915_eulerpick_certified_floors.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EXACT.FORM.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v553_exact_form_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EXCLUSION.BATTERY2.01 | WEIL_POSITIVITY_WINDOWS | `verification/v826_prime_exclusion_battery2.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EXCLUSION.LADDER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v825_prime_exclusion_ladder.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EXCLUSION.LOCATOR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v827_prime_zero_locator.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EXCLUSION.WINDOW.01 | WEIL_POSITIVITY_WINDOWS | `verification/v828_prime_comb_window.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.EXTRACTION.CHAIN.01 | WEIL_POSITIVITY_WINDOWS | `verification/v848_extraction_chain.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FEJERDENS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v669_fejer_density.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FEWATOM.REDUCTION.01 | WEIL_POSITIVITY_WINDOWS | `verification/v953_fewatom_reduction.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FINEC1.01 | WEIL_POSITIVITY_WINDOWS | `verification/v637_fine_c1_bridge.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FIRSTBIRTH.01 | WEIL_POSITIVITY_WINDOWS | `verification/v711_chain_firstbirth_scaling.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLIPMECH.01 | WEIL_POSITIVITY_WINDOWS | `verification/v619_flip_mechanics.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.BRIDGEMAP.01 | WEIL_POSITIVITY_WINDOWS | `verification/v839_paircorr_bridge_saturation.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.GUEABLATION.01 | WEIL_POSITIVITY_WINDOWS | `verification/v840_gue_ablation_loopgain.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.RATIO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v823_prime_lagrange_floor.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.RATIO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v824_prime_floor_skeleton.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.RATIO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v829_prime_floor_depth.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.RATIO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v830_prime_float_budget.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.RATIO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v831_prime_alias_second_moment.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FLOOR.RATIO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v843_margin_law_excess_lean.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FORM.CONVERGENCE.THEOREM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v912_form_convergence_theorem.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FRAME.DEFICIT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v560_frame_deficit_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.FULLGAP.GROWTHLAW.THEOREMS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v926_fullgap_growthlaw_theorems.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GAPUNIV.01 | WEIL_POSITIVITY_WINDOWS | `verification/v731_strat2_gap_universality.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GARDEDGE.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v662_garding_edgeband.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GARDENV.01 | WEIL_POSITIVITY_WINDOWS | `verification/v663_garding_envelope.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GARDING.01 | WEIL_POSITIVITY_WINDOWS | `verification/v661_garding.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GATE0.01 | LATTICE_E8_HECKE | `verification/v733_strat3_gate0_census.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GAUGE.PARITY.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v549_gauge_parity_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GAUGE.PPR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v556_gauge_ppr_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GEOMSOS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v686_geometric_sos.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GLUEDETECT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v750_simpler_gluing.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GONEK.PRICING.01 | WEIL_POSITIVITY_WINDOWS | `verification/v934_gonek_pricing_unconditional.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GREEN.SZEGO.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v548_green_szego_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GROUND.RESIDUE.OBS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v944_ground_residue_observability.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.GROUNDTRUTH.01 | WEIL_POSITIVITY_WINDOWS | `verification/v668_ground_truth.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.H3.COFINAL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v933_h3_cofinal_adjudication.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HANDOFFBULK.01 | OPERATOR_SPECTRAL | `verification/v766_handoff_bulk.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HANDOFFGRAM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v767_handoff_frequency_gram.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HANDOFFREDTEAM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v765_handoff_redteam.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HANDOFFRES.01 | WEIL_POSITIVITY_WINDOWS | `verification/v759_handoff_fixed_window_resolution.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HANDOFFTAIL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v768_handoff_tail_weil.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HARDY.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v545_hardy_core_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HECKEMODRAM.01 | LATTICE_E8_HECKE | `verification/v738_hecke_mod_ramified.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HECKEPOLARITY.01 | LATTICE_E8_HECKE | `verification/v753_ramified_polarity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HECKESOS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v691_hecke_sos.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HECKETWOSTEP.01 | LATTICE_E8_HECKE | `verification/v754_ramodd_twostep.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HODGECONE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v627_hodge_chamber.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.HOLECLOSED.01 | WEIL_POSITIVITY_WINDOWS | `verification/v681_coverage_hole.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.INTERP.01 | SELBERG_TRACE_CONTACT | `verification/v688_interpolation_detector.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.INTERPCLOSURE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v694_interpolation_lemma_closure.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.JACOBI.POLE.UVAROV.01 | WEIL_POSITIVITY_WINDOWS | `verification/v871_pole_uvarov_crossdefect.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.JETMASS.FLOOR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v931_jetmass_floor_theorems.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.K1BPIN.01 | WEIL_POSITIVITY_WINDOWS | `verification/v728_k1b_superresolution.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.K1CAPTURE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v721_k1_node_capture.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KEIPERLI.01 | WEIL_POSITIVITY_WINDOWS | `verification/v665_keiper_li.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KERNELCLASS.01 | LATTICE_E8_HECKE | `verification/v687_extremal_kernel.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KEYSTONE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v701_big_picture_hunt.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KMSEXT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v740_kms_extension_switch.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KMSSTINESPRING.01 | WEIL_POSITIVITY_WINDOWS | `verification/v756_kms_incidence_stinespring.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KMSTOEPLITZ.01 | WEIL_POSITIVITY_WINDOWS | `verification/v741_kms_toeplitz_semigroup.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KRAUS.DOILY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v811_prime_kraus_doily.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KRAUS.RM24.01 | LATTICE_E8_HECKE | `verification/v820_prime_kraus_rm24.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KREIN.DEFECT_ONE.01 | RHP_IIKS_TAU | `verification/v862_defect_polar_weld.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KREIN.DEFINITIZER.01 | RHP_IIKS_TAU | `verification/v948_krein_sign_characteristic.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.KREIN.NORMALFORM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v861_krein_normalform_lean.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.L1IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v727_l1_identification.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.L1MONTAGE.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v713_l1_montage.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.L1WPD.CLOSURE.01 | LATTICE_E8_HECKE | `verification/v937_l1wpd_closure_reduction.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LEHMERNULL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v671_lehmer_resonance.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LEVEL.LEMMA.01 | WEIL_POSITIVITY_WINDOWS | `verification/v547_level_lemma_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LICOROLLARY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v672_li_corollary.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LIE4.01 | LATTICE_E8_HECKE | `verification/v673_li_e4.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LKSPLIT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v682_lk_split_theta.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LOCKDIR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v586_pnt_lock_direction.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LOCKPROJ.01 | WEIL_POSITIVITY_WINDOWS | `verification/v596_lock_projection.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LOCKSPLIT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v585_pnt_locking_split.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LOEWNER.PICK.01 | WEIL_POSITIVITY_WINDOWS | `verification/v947_loewner_pick_dictionary.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LONGLAG.SUPP.01 | WEIL_POSITIVITY_WINDOWS | `verification/v544_long_lag_support.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LOOP.EQUIVALENCE.THEOREMS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v920_loop_equivalence_theorems.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.LORENTZ.SPINOR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v807_lorentz_nullselector.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MACROKERNEL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v579_macro_kernel_signs.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MANGOLDT.ABLATION.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v943_mangoldt_ablation_localization.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MANIFOLD.INVARIANCE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v936_manifold_invariance_exclusion.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MAPCLOSE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v595_mapping_completion.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MARGIN.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v542_margin_chain_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MARGINLINK.01 | WEIL_POSITIVITY_WINDOWS | `verification/v656_margin_link.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MMATRIX.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v543_lumped_pair_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOMENT.LAURENT.ROOTLADDER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v924_moment_laurent_rootladder.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOONSHOT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v714_moonshot_hecke_groupoid.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOONSHOT.02 | WEIL_POSITIVITY_WINDOWS | `verification/v716_moonshot_arch_glue.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOONSHOT.03 | WEIL_POSITIVITY_WINDOWS | `verification/v717_moonshot_state.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOONSHOT.04 | WEIL_POSITIVITY_WINDOWS | `verification/v718_moonshot_spectral.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOONSHOT.05 | WEIL_POSITIVITY_WINDOWS | `verification/v719_moonshot_traceformula.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOONSHOT.06 | WEIL_POSITIVITY_WINDOWS | `verification/v720_moonshot_k2k3.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.MOSCO.SELECTION.01 | TOEPLITZ_MOMENT_POSITIVITY | `verification/v816_prime_mosco_selection.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.NEEDLEMECH.01 | WEIL_POSITIVITY_WINDOWS | `verification/v675_needle_mechanism.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.NODELESS.PF.01 | DYNAMICS_CLOCKS_PF | `verification/v954_nodeless_pf.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.NOGO.SIGNED.ONLY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v913_signed_alignment_localization.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.NULLRAY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v577_nullray_census.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.OCCUPATION.01 | WEIL_POSITIVITY_WINDOWS | `verification/v580_occupation_map.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ODD.SECTOR.IDENT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v550_odd_sector_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PACKET.RM14.01 | LATTICE_E8_HECKE | `verification/v819_prime_packet_rm14.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PACKET480.01 | LATTICE_E8_HECKE | `verification/v786_prime_packet480.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PACKETGARD.01 | WEIL_POSITIVITY_WINDOWS | `verification/v674_packet_garding.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PAIRBAND.01 | WEIL_POSITIVITY_WINDOWS | `verification/v573_pair_band_structure.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PARETO.TV.01 | WEIL_POSITIVITY_WINDOWS | `verification/v555_pareto_tv_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PARTITION.CLOSURE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v879_envelope_partition_closure.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PASCAL.REGION.THEOREM.01 | SCREW_SUBORDINATION_LSTAR | `verification/v914_pascal_region_theorem.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PCANON.01 | WEIL_POSITIVITY_WINDOWS | `verification/v635_p_canonicity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PCONSTRUCT.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v636_p_construction.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PENCIL.ONEMODE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v569_lambda_pencil_onemode.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PENCIL.SEPFLOOR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v570_separation_floor.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PHASE.LEVER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v860_phase_lever_closure.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PHASE.POLYGON.01 | WEIL_POSITIVITY_WINDOWS | `verification/v876_carleson_polygon_wave.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PHASE2.CAPSTONE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v559_phase2_capstone.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PINCHBREAK.01 | WEIL_POSITIVITY_WINDOWS | `verification/v680_pinch_attack.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PINLEMMA.01 | WEIL_POSITIVITY_WINDOWS | `verification/v730_strat2_pinning_lemma.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PNTMODEL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v583_pnt_model.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.POLERANKONE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v591_pole_rank_one.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.BALLLADDER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v897_certified_interval_ladder.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.BFLOOR.PG.01 | RHP_IIKS_TAU | `verification/v905_bfloor_ideal_certificate.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.CERTIFIED.HEAD.01 | WEIL_POSITIVITY_WINDOWS | `verification/v884_certified_head_positivity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.CERTIFIED.LADDER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v887_certified_ladder_complete.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.CHRISTOFFEL.RATIO.01 | RHP_IIKS_TAU | `verification/v899_christoffel_normsquare.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.DIAGSEP.01 | WEIL_POSITIVITY_WINDOWS | `verification/v889_route_decisions.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.ETASOURCE.01 | RHP_IIKS_TAU | `verification/v893_relative_margins.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.FACTORAVOID.01 | WEIL_POSITIVITY_WINDOWS | `verification/v895_collective_comb.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.HALFGAP.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v907_halfgap_registered_target.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.HIROTA.01 | WEIL_POSITIVITY_WINDOWS | `verification/v890_total_positivity_flow.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.ISOFLOW.01 | RHP_IIKS_TAU | `verification/v885_ladder_flow_anatomy.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.MOEBIUS.KILLS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v891_moebius_firewall_kills.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.NORMALIZED.CORE.01 | RHP_IIKS_TAU | `verification/v900_core_update_anatomy.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.RELCONG.01 | RHP_IIKS_TAU | `verification/v892_closure_architecture.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.TAILSIGN.01 | WEIL_POSITIVITY_WINDOWS | `verification/v906_tail_cartography.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.TANGENT.SCHUR.01 | RHP_IIKS_TAU | `verification/v901_tangent_schur_bfloor.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PORT.TAU.01 | MELLIN_PICK_LEE_YANG | `verification/v883_tau_chain_parametrix.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.POSFUNC.01 | WEIL_POSITIVITY_WINDOWS | `verification/v708_chain_position_functional.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.POSITIVE_DESCENT.01 | SCREW_SUBORDINATION_LSTAR | `verification/v791_positive_descent.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PRUEFER.COMPENSATION.01 | WEIL_POSITIVITY_WINDOWS | `verification/v873_pruefer_cotlar_decision.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.PSD.COMPLETION.TAX.01 | WEIL_POSITIVITY_WINDOWS | `verification/v850_completion_tax_flow.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.QFBUNDLE.01 | LATTICE_E8_HECKE | `verification/v770_qf_spectral_bundle.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.QFCENSUS.01 | LATTICE_E8_HECKE | `verification/v771_qf_representation_census.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.QFCOCYCLE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v773_qf_cell_cocycle.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.QFFESHBACH.01 | OPERATOR_SPECTRAL | `verification/v772_qf_feshbach_effective.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.QFGAUGE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v769_qf_contract_necessity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RANK3DENSITY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v693_rank3_density_close.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RANK3FUNC.01 | WEIL_POSITIVITY_WINDOWS | `verification/v683_rank3_functionals.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RANK3JET.01 | WEIL_POSITIVITY_WINDOWS | `verification/v739_rank3_jet.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RANK3LOCKGRAM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v692_rank3_lockgram.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RANK3TRANSV.01 | WEIL_POSITIVITY_WINDOWS | `verification/v712_rank3_transverse_deck.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RANK3UNIF.01 | WEIL_POSITIVITY_WINDOWS | `verification/v685_rank3_uniformity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RANK3ZERO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v684_rank3_zeroside.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RDAGGER.KERNEL_LOEWNER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v1017_kernel_loewner_positivity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.REDHEFFER.COLLIGATION.01 | RHP_IIKS_TAU | `verification/v863_redheffer_colligation.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RELATION.CONNECTED_COVARIANCE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v856_connected_current_lean.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RELATION.HODGE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v854_relation_hodge_pfaffian.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RELATION.MULT.01 | SELBERG_TRACE_CONTACT | `verification/v841_relation_carrier_ladder.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RELATION.SKELETON.01 | WEIL_POSITIVITY_WINDOWS | `verification/v842_excess_certified_skeleton.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RELATION.SKELETON.01 | WEIL_POSITIVITY_WINDOWS | `verification/v846_schur_spectral_mother.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RELATION.SKELETON.01 | WEIL_POSITIVITY_WINDOWS | `verification/v847_wedge_cellcone_transport.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RIDGEOM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v657_rid_alignment.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RITZ.CEIL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v551_ritz_ceiling_certificate.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.RPUNIV.01 | WEIL_POSITIVITY_WINDOWS | `verification/v729_strat2_rp_universality.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.S1CANON.01 | WEIL_POSITIVITY_WINDOWS | `verification/v734_s1_canonical.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SAMPLING.HARM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v554_sampling_harmonics_identities.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SCHURCONE.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v743_schur_cone_recursion.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SCHURREC.01 | WEIL_POSITIVITY_WINDOWS | `verification/v755_simpler_schur_recursion.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SECTIONEDGE.01 | OPERATOR_SPECTRAL | `verification/v707_chain_section_edge.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SECTOR_CONTINUA.01 | WEIL_POSITIVITY_WINDOWS | `verification/v793_f8sector_conductor.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SECULAR.GW.PINNING.01 | WEIL_POSITIVITY_WINDOWS | `verification/v919_secular_gw_pinning.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SHADOW.01 | LATTICE_E8_HECKE | `verification/v625_prime_shadow.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SIGMAFLOOR.FACTORIZATION.01 | WEIL_POSITIVITY_WINDOWS | `verification/v929_sigmafloor_factorization.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SIGNUNC.01 | WEIL_POSITIVITY_WINDOWS | `verification/v648_sign_uncertainty.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SOFTPORT.FESHBACH.01 | RHP_IIKS_TAU | `verification/v864_softport_kappa_law.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SOFTPORT.RADAU.01 | TOEPLITZ_MOMENT_POSITIVITY | `verification/v867_radau_conditioning.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SONIN.01 | WEIL_POSITIVITY_WINDOWS | `verification/v732_strat3_sonin_prolate.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SOURCECONTRACTOR.NORM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v866_source_contractor_formula.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SPACING.JETSUMRULES.THEOREMS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v922_spacing_jet_sumrule_theorems.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SPECTRAL.BALANCE.RAZOR.01 | WEIL_POSITIVITY_WINDOWS | `verification/v923_spectral_balance_razor_theorems.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.SQRT.UNIFORM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v882_port_source_mellin.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.THETAINF.PIN.01 | LATTICE_E8_HECKE | `verification/v935_thetainf_landau_bridge.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.THETAPRED.01 | WEIL_POSITIVITY_WINDOWS | `verification/v660_theta_predicate.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.TOPROOT.THETA.01 | WEIL_POSITIVITY_WINDOWS | `verification/v932_toproot_theta_statement.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.TOWERNEST.01 | WEIL_POSITIVITY_WINDOWS | `verification/v749_simpler_tower.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.TRANSPORT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v581_locking_transport.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.TURAN.EXTREMAL.01 | WEIL_POSITIVITY_WINDOWS | `verification/v952_turan_extremal.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.TURINGCERT.01 | LATTICE_E8_HECKE | `verification/v666_turing_cert.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.TWOSTAGE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v710_chain_two_stage_hecke.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.UCPLIMIT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v735_strat3_ucp_inductive.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.UNCONDCERT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v594_unconditional_cert.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.UNIFC.01 | WEIL_POSITIVITY_WINDOWS | `verification/v618_uniform_constant.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.VACUUM35.01 | WEIL_POSITIVITY_WINDOWS | `verification/v821_prime_vacuum35.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.W3BOUND.01 | LATTICE_E8_HECKE | `verification/v658_w3_uniform_bound.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.W3LAND.01 | LATTICE_E8_HECKE | `verification/v659_w3_landscape.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.W3STRUCT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v677_w3_structure_theorem.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WALL.FINITE_CLOSURE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v909_finite_wall_closure.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WALL.FINITE_ZERO_TRANSFER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v910_finite_zero_transfer.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WARDMONO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v751_ward_monotone.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WCLOSED.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v587_w_closed_form.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.BOUNDARY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v640_w1_boundary.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.CONTACT.01 | SCREW_SUBORDINATION_LSTAR | `verification/v630_suzuki_contact.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.DICT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v631_w1_dictionary.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.MATRIX.01 | WEIL_POSITIVITY_WINDOWS | `verification/v642_w1_matrix.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.MOSCO.01 | WEIL_POSITIVITY_WINDOWS | `verification/v655_w2_mosco.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.PORTABLE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v641_w1_portability.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.THEOREM.01 | SCREW_SUBORDINATION_LSTAR | `verification/v643_w1_theorem.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEIL.W2.01 | WEIL_POSITIVITY_WINDOWS | `verification/v644_w2_form_density.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEYL.PORT.01 | WEIL_POSITIVITY_WINDOWS | `verification/v865_weyl_port_readout.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WEYLMASS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v706_chain_weyl_mass.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.WINDOW.INSTRUMENT.MECHANISM.01 | WEIL_POSITIVITY_WINDOWS | `verification/v930_window_instrument_mechanism.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.YOSIDAQF.01 | SCREW_SUBORDINATION_LSTAR | `verification/v763_yosida_handoff.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.Z1.COMPACTNESS.01 | WEIL_POSITIVITY_WINDOWS | `verification/v780_z1_compactness_trilogy.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.Z1FLOWREC.01 | WEIL_POSITIVITY_WINDOWS | `verification/v698_z1_flow_recursion.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.Z1JACOBI.01 | EXPLICIT_FORMULA_IDENTITY | `verification/v696_z1_jacobi.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.Z1LOOKAHEAD.01 | LATTICE_E8_HECKE | `verification/v702_z1_lookahead.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.Z1MEASURE.01 | WEIL_POSITIVITY_WINDOWS | `verification/v695_z1_trace_operator.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.Z1UVAROV.01 | WEIL_POSITIVITY_WINDOWS | `verification/v697_z1_uvarov.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ZERO.CAUSAL.SYNTH.01 | LATTICE_E8_HECKE | `verification/v945_zero_causal_stratification.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ZERO.CHANNEL.CAPACITY.01 | WEIL_POSITIVITY_WINDOWS | `verification/v950_zero_channel_capacity.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ZEROCOMB.01 | WEIL_POSITIVITY_WINDOWS | `verification/v589_zero_comb.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ZEROGAP.01 | LATTICE_E8_HECKE | `verification/v678_zero_gap_theorem.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:PRIME.ZEROLAYER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v709_chain_zero_layer.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:RH.BUNDLE.01 | OTHER | `verification/v33_explicit_flat_bundle.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:RTF.GNS.LEDGER.01 | WEIL_POSITIVITY_WINDOWS | `verification/v541_matching_lemma_ledger.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| ledger:SECTOR.FLOORATTACK.01 | WEIL_POSITIVITY_WINDOWS | `verification/v818_sector_floor_attack.py` | Prime-front / PRIME.* suite module absent from prior catalog fragments. |
| notes DLXXIX-DXCVII | OTHER | `experiments/next.txt` | Newest-at-bottom campaign log. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-04ab11d40f5c6677d9` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-0bb8faf64bbcef970f` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-260b2934308834ff30` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-277d4d5753cbf897c9` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-31a48bca49bc25f595` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-359a5118ff380b46ba` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-374366a61d8e88b9c7` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-464981fcb582cb4bfb` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-4bb24a32d7a2fce33a` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-531a2025ac71db9bc2` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-67bbad60c4a1985633` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-6c988252dca50004e0` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-754adaa262b1ef6121` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-783a08a56ff0106824` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-81216f9874163553ab` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-87371be527b0ef0c67` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-93d65f46ae53dc156a` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-a1d61877760ed3ac3b` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-a5d7adbbf921c779a1` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-acae8e74441cab7e90` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-b227bcf1d92ecdba07` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-bee39834231c391ab5` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-ce83b845a8bd9df7ed` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-d38def5027354cd175` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-d48cc24f5085a51427` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-ea194f2f8599f6f54c` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-discovered-f7a15c6fb50abac144` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-multilevel-harnack` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-multilevel-rung` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-multilevel-strictness` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `multilevel_toeplitz_lowerbound.tex#paper-multilevel-uniform` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-discovered-3504e75554f1f37349` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-discovered-46a68271538be83dc2` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-discovered-598b44928fc93a5cb5` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-discovered-8dc82f4043f70167dd` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-discovered-ce734a484154a3d26a` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-discovered-dce0e5a2a5788314cd` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-discovered-f74bee94924e767a92` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-gaussian-formal-scope` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_e8_gaussian_code.tex#paper-gaussian-rh-boundary` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_hilbert_polya_truncations.tex` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_hilbert_polya_truncations.tex#paper-hp-lean-scope` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_hilbert_polya_truncations.tex#paper-hp-limit-obligations` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_hilbert_polya_truncations.tex#paper-hp-proof-label` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w1_suzuki_identification.tex` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w1_suzuki_identification.tex#paper-discovered-44db965e63b3fa54e8` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w1_suzuki_identification.tex#paper-discovered-c991f463f411418889` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w1_suzuki_identification.tex#paper-w1-measure-dictionary` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w1_suzuki_identification.tex#paper-w1-odd-domain` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w3_detector_structure.tex` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w3_detector_structure.tex#paper-discovered-d98f4a27b960353189` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w3_detector_structure.tex#paper-discovered-ff8789dd2cda2b2c35` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w3_detector_structure.tex#paper-w3-alias-identity` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w3_detector_structure.tex#paper-w3-c1-direction` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `note_w3_detector_structure.tex#paper-w3-fejer-resolution` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-03d8498cd556b29e0a` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-046a1842c93f90f6fe` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-07b5aa2669740c8e79` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-0a4cc3d2e4a374ea80` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-14f5f7232fc2859a27` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-1a6f06bc02556a8ca6` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-1f96c335fecc55f2cf` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-253effbf6f5f46825f` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-349dd5af8d96923ab3` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-378eb1262f9dd2b1be` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-38a476ad8509aee5de` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-3a1eca64fb645f29c5` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-3aff9152d2bd04cab1` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-3d26df7a0e7e5437e7` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-3f03cf24714ee83491` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-4d8e1a944892a9a5e3` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-4eaf76115c306583dd` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-5190bd1266a72a4973` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-55ff3d411848ad93c5` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-58840f2040f7420a8c` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-5d49bd988d2bc8e9eb` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-5da139a2071d587e3f` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-62efe60cf67603b80b` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-64597a32c4adead53b` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-68330f2f534e12542c` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-68f52772ef01f9ce16` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-69d122a848f2db0bd6` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-6fcd2a9ea18ba95a63` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-75ccc86efc2e2d6d33` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-7844ff09026f55e965` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-7eee5c29b01361d2a5` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-7f8e6cf518a8e191cf` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-82a4d7628ada178d3a` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-8339c3da6d817cd7c1` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-8a28e4348fb57dcbb9` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-8c0f25dc4f915e05d0` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-95e1f921bcce25b6d9` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-97c79d4ab0e8dd30cb` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-980fd48d416e18d93c` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-99c762258200cee48f` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-9c57574c3a6ebc7aaf` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-9f2dfb456cb556dd25` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-a1dfb788db1b66f2bc` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-a387e9609981c9ab05` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-a573b2c473eb5bd09c` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-ae8a84340577309de3` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-b084b87f76b0a9e9d2` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-b25a77f9a4c290a31f` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-b92f45406321154a17` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-bc95440a2d345d61e5` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-bfaa5f451dd2db10c2` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-c1f1a1eaf716b58454` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-c4f584830691972127` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-cd5e3cce9ea4f3170f` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-ce3d5f0fc40b3225c8` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-d3e6ad4539ec004f95` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-dafcaa980aca53ed92` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-dddbca0e17742f0bfa` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-dee174ffb08a5ceb18` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-e288556fb374acee75` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-e3fb89428aae11080a` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-discovered-fa175f6232986ee441` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-parity-r1-open` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-parity-rank-three` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-parity-rank-two-refuted` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `parity_toeplitz_classification.tex#paper-parity-tv-floor` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/00ee7a7d71d24d9992dc-137733c98f183a37d23f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/01c1c1f85b1922cd5555-ce6b31dc4aef29dde28a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/02a3af21aad8e34acdac-7815c7ba7c1747a50ebc.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/02ab4dfa1b4f8fe3f653-1448eda75c0d9f7c54b9.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/04133e2e7b324db349c6-ec5009d27856decd8da9.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/054838d44e5ebecca19f-8ea50ab6b1b9ece914cd.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/197b476fcee6ddf87925-7e6b629d2b396dd307c6.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/1b20bd62752303f80e3b-0ae4c77a6c6348f40064.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/1d38897a7c613767cef1-3f514638489df697b7a4.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/1deef5a392a300dd18d3-d3c2831cc307ad761991.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/1edaee96b51c865c6c96-5160b6331d71b5f58190.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/2201c1f528e2ad759dbc-4a8a1a6ff153a8459fdd.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/226bed110858038c9d22-836d2c397f1aa94e1d32.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/22a7c052cefc781c698c-0a508f17a9aed177a291.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/23ad10578c30a41c1dd9-c5aeb50cef50e8b6d0ab.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/2495edd2d4c00938ab67-7859bd6009c4686b82b2.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/24a4f0c34f23ace4b258-6f69746427ddfd2d56d1.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/2665966261f63a5be264-c1833814d2b315557703.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/2a5119f4be4d183f35ca-6ea69c52145748826c6c.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/2bca6b421f2cab3db40d-917e012b83ea0594ce16.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/2fe73304c82980ba7274-f2a80208450f2bf5cbef.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/30e2c1ea8c5c34f23609-fe7f92c213b7542a08b6.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/31f4cbc64c9fcf9a690e-0ccba4c1570398b97848.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/396e2aed8501c2c6ec04-869050aa2e95e1ea1fa1.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/3ed8c913159a8e42fbfe-1d31edad4059e269a417.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/4465b0893e26290a5c71-2e4926c370927c6e333b.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/44bdb8960247e9e41ddb-d7cd51360b513d5f329c.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/4805350b2720e3271e71-14793f3d1f870fca9cf9.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/491b9280f7f01a8a37fe-f154186a35d1cd74d0e1.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/49206e31105f9b010004-c23e5d737be98c3344e8.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/495998e71e8f4c789b64-e433b495cea7c94219ee.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/503430682f427668488b-db9d173c181a3bc7b182.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/54871ccf0c417b1be1c5-f3ffe3e6aa76fe08df5c.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/55a4575c929b484cd6cf-ba76610dc052de42b534.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/56c71e165621d9782eab-81d325a2648236d38357.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/56e2f7259d3e1eddfef2-d8a10c59661f08dc71b1.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/58d51f149dd9b146c68f-7ded60fa159efe3fedfc.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/59f266ce0bf6d8d3f736-9bafa0ea341a0262a29a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/59f266ce0bf6d8d3f736-e77228951b79efab687a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/5bb72a2dd025609bf7c8-4ce3af5c971e940e8742.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/5e61d54c7fc94ba87fb3-9ff1795eb8cdce256fab.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/5e61d54c7fc94ba87fb3-d933cb97bbe60a4df147.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/6593fe1682fa1c612586-7d1ea5a105817cb7ca86.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/6c63b79bc4b3ae978d4c-b2058615bc29ef758d1a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/7632581451a561f8a598-26aef13f80769f12b819.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/7731668a96b791a00760-c5b473f8ac97378a2c7a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/7c143aa16194c0430198-4c6967e0320f06919adf.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/8089983e645565143e67-54d2d2aa3c153b463d12.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/838b3b3d42bad99210ca-d200bd98a4161d18771d.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/8660fe7a567215dc1e7d-0ad3a93e9fffed8fce47.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/86e1a0a653cc477a4c2e-982f6f9e923d4ed4aa06.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/8e6e2acd80d27c201412-3b5592ee1b81c4925fbb.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/8ea5f9a999677d8c1fc2-bc732a52d1f99f03fed4.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/933e292f75fe6cccb46d-2935d1f45ad3a4081572.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/943a24806adc5110bfac-7a83eba58cbdebf2d463.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/952ab0ef9e61a6314ee0-ebcf489aaec71e03ef1b.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/9649bf8ecce60a8a3e38-df4732698cbeda550642.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/98376f761b136af87a3a-b7bc220266499bd84e80.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/9b5df48ca2a537b5f090-3a2372c7adfc6272f5ee.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/9bafcb5d890ed63b1583-efdeb23e18eefa36fa3f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/9fb53ea037ff5464edee-707dddd23bc1fa457b96.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/a04ac936f779ff00b5f1-4197857072240bc1c0c9.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/a05d2c08c25414107b60-f4e1657edc8caf25ee48.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/a0f8aa486f0f64c03825-27122c10b61fe513cce3.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/a4e723ed85107148e5cd-d44f763a4f1c89ec595c.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/adf473a211e62d082946-3e5b6ecae6ca8083433c.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/b0191b67d2f7cbab9df2-e351803cb77e48208d8e.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/b17d002396911bfee16f-7c48401dbcd62c0552d2.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/b1e3d23bbf7959bf7058-793dd088543f2fa510fb.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/b2d1536430b4160671da-c96e01fcc484cf6d3a96.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/b7b5d259fb821653794b-76d846c70398a203ea7a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/bd2948c33ea1366efeb2-36af07e1911381ace9a3.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/befea4742a94a35e4201-11d42aa5f0601bb3cae8.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/c01cb4a6cd94ae40bfa8-076cc573c89643811629.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/c7a5b9a901d71e4e3992-49f33427ef7bf8def3fd.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/cab32e6011ca282684e1-8cfc42a7b06935836ddd.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/cc2897fe68d1da8a9cd0-e73f6e7396ac7f90861a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/cc857032ec0523eff1a0-07b59ef5a34e85a220b8.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/cf3e42f061fc941ef1cb-4f619f4844b93053f3f9.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/cf7c855ae564f86c79fd-3e303f5d4089c67dcce5.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/d5b566672d584b3f6168-175d112bbfa03b23ca4f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/d65295d5e3fe40fb3701-b69208d88fa0d9614386.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/daa5ba359ceb354e2f88-e44ecb341937c401af9f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/dee4dbd465492c8a29b0-fa8365b8fab9a2525941.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/e4804354c70a3c1992c9-1072c65194fbaba5102a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/ed34b2d2f5ac4f46c5cf-17dde544f9dc30d52e0f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/f50550d0b55c8398f7f7-2f3a7f9a1cd4f2977aa6.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/f529de163b9eff9064ec-bdaf5af883920f7d4ffd.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/f9f81a97bebf4e47a2dc-9b4b9ffd3ac31a07edef.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/results/fca79d9e6596a5e41121-e7e0d3617ea12a06a89e.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/00ee7a7d71d24d9992dc.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/01c1c1f85b1922cd5555.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/02a3af21aad8e34acdac.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/02ab4dfa1b4f8fe3f653.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/04133e2e7b324db349c6.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/054838d44e5ebecca19f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/197b476fcee6ddf87925.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/1b20bd62752303f80e3b.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/1d38897a7c613767cef1.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/1deef5a392a300dd18d3.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/1edaee96b51c865c6c96.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/2201c1f528e2ad759dbc.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/226bed110858038c9d22.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/22a7c052cefc781c698c.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/23ad10578c30a41c1dd9.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/2495edd2d4c00938ab67.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/24a4f0c34f23ace4b258.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/2665966261f63a5be264.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/2a5119f4be4d183f35ca.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/2bca6b421f2cab3db40d.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/2fe73304c82980ba7274.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/30e2c1ea8c5c34f23609.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/31f4cbc64c9fcf9a690e.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/396e2aed8501c2c6ec04.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/3ed8c913159a8e42fbfe.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/4465b0893e26290a5c71.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/44bdb8960247e9e41ddb.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/4805350b2720e3271e71.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/491b9280f7f01a8a37fe.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/49206e31105f9b010004.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/495998e71e8f4c789b64.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/503430682f427668488b.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/54871ccf0c417b1be1c5.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/55a4575c929b484cd6cf.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/56c71e165621d9782eab.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/56e2f7259d3e1eddfef2.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/58d51f149dd9b146c68f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/59f266ce0bf6d8d3f736.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/5bb72a2dd025609bf7c8.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/5e61d54c7fc94ba87fb3.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/6593fe1682fa1c612586.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/6c63b79bc4b3ae978d4c.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/7632581451a561f8a598.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/7731668a96b791a00760.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/7c143aa16194c0430198.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/8089983e645565143e67.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/838b3b3d42bad99210ca.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/8660fe7a567215dc1e7d.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/86e1a0a653cc477a4c2e.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/8e6e2acd80d27c201412.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/8ea5f9a999677d8c1fc2.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/933e292f75fe6cccb46d.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/943a24806adc5110bfac.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/952ab0ef9e61a6314ee0.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/9649bf8ecce60a8a3e38.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/98376f761b136af87a3a.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/9b5df48ca2a537b5f090.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/9bafcb5d890ed63b1583.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/9fb53ea037ff5464edee.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/a04ac936f779ff00b5f1.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/a05d2c08c25414107b60.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/a0f8aa486f0f64c03825.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/a4e723ed85107148e5cd.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/adf473a211e62d082946.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/b0191b67d2f7cbab9df2.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/b17d002396911bfee16f.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/b1e3d23bbf7959bf7058.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/b2d1536430b4160671da.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/b7b5d259fb821653794b.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/bd2948c33ea1366efeb2.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/befea4742a94a35e4201.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/c01cb4a6cd94ae40bfa8.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/c7a5b9a901d71e4e3992.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/cab32e6011ca282684e1.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/cc2897fe68d1da8a9cd0.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/cc857032ec0523eff1a0.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/cf3e42f061fc941ef1cb.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/cf7c855ae564f86c79fd.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/d5b566672d584b3f6168.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/d65295d5e3fe40fb3701.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/daa5ba359ceb354e2f88.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/dee4dbd465492c8a29b0.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/e4804354c70a3c1992c9.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/ed34b2d2f5ac4f46c5cf.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/f50550d0b55c8398f7f7.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/f529de163b9eff9064ec.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/f9f81a97bebf4e47a2dc.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `rh/catalog/research_engine/submissions/fca79d9e6596a5e41121.json` | Read the unabridged claim, all premises, source hash and review status before use. |
| paper-claim-audit-20260909 | OTHER | `tfpt_prime_front.tex#paper-route-lemma-separation` | Read the unabridged claim, all premises, source hash and review status before use. |
| phase2 | TOEPLITZ_MOMENT_POSITIVITY | `verification/v563_paper2_readouts.py` | von_mangoldt_table, build_window, reference-window polarisation identities. |
| port lane | TOEPLITZ_MOMENT_POSITIVITY | `verification/v881_carleson_port_geometry.py` | CD Pick scalarization, Carleson testing functional, Haynsworth port Schur, IIKS generators. |
| relative_window_flow_20260907 | WEIL_POSITIVITY_WINDOWS | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/relative_window_flow_20260907/relative_flow_proof.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| research_update_audit_20260909 | EXTERNAL_ADJUDICATION | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/research_update_audit_20260909/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_arithmetic_relative_correction_20260909 | WEIL_POSITIVITY_WINDOWS | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_arithmetic_relative_correction_20260909/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_autonomous_search_20260907 | OPERATOR_SPECTRAL | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_autonomous_search_20260907/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_barrier_search_20260907 | WEIL_POSITIVITY_WINDOWS | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_barrier_search_20260907/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_fermion_event_identity_20260908 | TOEPLITZ_MOMENT_POSITIVITY | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_fermion_event_identity_20260908/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_residual_response_20260908 | WEIL_POSITIVITY_WINDOWS | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_residual_response_20260908/RESPONSE_PROOF.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_seam_gram_correction_20260909 | DYNAMICS_CLOCKS_PF | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_seam_gram_correction_20260909/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_whole_odd_coercivity_20260909 | WEIL_POSITIVITY_WINDOWS | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_whole_odd_coercivity_20260909/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| rh_zero_temperature_readout_20260908 | TOEPLITZ_MOMENT_POSITIVITY | `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_zero_temperature_readout_20260908/README.md` | Original written arguments, complete run history and source hashes; keep each stated hypothesis and finite/global boundary. |
| v1021 | EXPLICIT_FORMULA_IDENTITY | `verification/v1021_all_place_tate_rank_audit.py` | Exact Tate projector, bad-place scalar factor, pole ward, abstract rank-nullity lemma with an external-premise fence, and sparse mean-to-pointwise counterexample. |

