import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async redirects() { return [
  {
    "source": "/verification/v699_cone_dynamics.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v699_cone_dynamics.py",
    "permanent": true
  },
  {
    "source": "/verification/v787_hecke_arrow_broadcast.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v787_hecke_arrow_broadcast.py",
    "permanent": true
  }
,
  {
    "source": "/verification/v747_automaton_multiway_tower.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v747_automaton_multiway_tower.py",
    "permanent": true
  },
  {
    "source": "/verification/v748_automaton_sigma_orbifold_confluence.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v748_automaton_sigma_orbifold_confluence.py",
    "permanent": true
  },
  {
    "source": "/verification/v785_hecke_check32.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v785_hecke_check32.py",
    "permanent": true
  },
  {
    "source": "/verification/v788_positive_c2_lift.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v788_positive_c2_lift.py",
    "permanent": true
  },
  {
    "source": "/verification/v789_multirate_constdepth.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v789_multirate_constdepth.py",
    "permanent": true
  },
  {
    "source": "/verification/v790_snf_mu4_theta.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v790_snf_mu4_theta.py",
    "permanent": true
  },
  {
    "source": "/verification/v795_halving_tails_k5.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v795_halving_tails_k5.py",
    "permanent": true
  },
  {
    "source": "/verification/v797_r_microstate_identification.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v797_r_microstate_identification.py",
    "permanent": true
  },
  {
    "source": "/verification/v806_hecke_local_clifford.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v806_hecke_local_clifford.py",
    "permanent": true
  },
  {
    "source": "/papers/big_picture_2026-08-02_de.pdf",
    "destination": "https://prime.fixpoint-theory.com/archive/big_picture_2026-08-02_de.pdf",
    "permanent": true
  },
  {
    "source": "/big_picture_2026-08-02_de.pdf",
    "destination": "https://prime.fixpoint-theory.com/archive/big_picture_2026-08-02_de.pdf",
    "permanent": true
  }
,
  {
    "source": "/verification/v535_hecke_from_geometry.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v535_hecke_from_geometry.py",
    "permanent": true
  },
  {
    "source": "/verification/v536_eichler_trace_layer.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v536_eichler_trace_layer.py",
    "permanent": true
  },
  {
    "source": "/verification/v537_halfintegral_bridge.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v537_halfintegral_bridge.py",
    "permanent": true
  },
  {
    "source": "/verification/v538_relative_trace_identity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v538_relative_trace_identity.py",
    "permanent": true
  },
  {
    "source": "/verification/v539_weil_structure_family.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v539_weil_structure_family.py",
    "permanent": true
  },
  {
    "source": "/verification/v540_amplitude_linear_carrier.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v540_amplitude_linear_carrier.py",
    "permanent": true
  },
  {
    "source": "/verification/v541_matching_lemma_ledger.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v541_matching_lemma_ledger.py",
    "permanent": true
  },
  {
    "source": "/verification/v868_divisor210_audits.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v868_divisor210_audits.py",
    "permanent": true
  }
,
  {
    "source": "/prime-front",
    "destination": "https://prime.fixpoint-theory.com/research",
    "permanent": true
  },
  {
    "source": "/prime-front/:path*",
    "destination": "https://prime.fixpoint-theory.com/prime-front/:path*",
    "permanent": true
  },
  {
    "source": "/papers/tfpt_prime_front.pdf",
    "destination": "https://prime.fixpoint-theory.com/papers/tfpt_prime_front.pdf",
    "permanent": true
  },
  {
    "source": "/papers/note_hilbert_polya_truncations.pdf",
    "destination": "https://prime.fixpoint-theory.com/papers/note_hilbert_polya_truncations.pdf",
    "permanent": true
  },
  {
    "source": "/papers/note_w1_suzuki_identification.pdf",
    "destination": "https://prime.fixpoint-theory.com/papers/note_w1_suzuki_identification.pdf",
    "permanent": true
  },
  {
    "source": "/papers/note_w3_detector_structure.pdf",
    "destination": "https://prime.fixpoint-theory.com/papers/note_w3_detector_structure.pdf",
    "permanent": true
  },
  {
    "source": "/papers/parity_toeplitz_classification.pdf",
    "destination": "https://prime.fixpoint-theory.com/papers/parity_toeplitz_classification.pdf",
    "permanent": true
  },
  {
    "source": "/papers/multilevel_toeplitz_lowerbound.pdf",
    "destination": "https://prime.fixpoint-theory.com/papers/multilevel_toeplitz_lowerbound.pdf",
    "permanent": true
  },
  {
    "source": "/papers/prime-front",
    "destination": "https://prime.fixpoint-theory.com/papers/prime-front",
    "permanent": true
  },
  {
    "source": "/papers/hilbert-polya-truncations",
    "destination": "https://prime.fixpoint-theory.com/papers/hilbert-polya-truncations",
    "permanent": true
  },
  {
    "source": "/papers/w1-suzuki-identification",
    "destination": "https://prime.fixpoint-theory.com/papers/w1-suzuki-identification",
    "permanent": true
  },
  {
    "source": "/papers/w3-detector-structure",
    "destination": "https://prime.fixpoint-theory.com/papers/w3-detector-structure",
    "permanent": true
  },
  {
    "source": "/papers/parity-toeplitz-classification",
    "destination": "https://prime.fixpoint-theory.com/papers/parity-toeplitz-classification",
    "permanent": true
  },
  {
    "source": "/papers/multilevel-toeplitz-lowerbound",
    "destination": "https://prime.fixpoint-theory.com/papers/multilevel-toeplitz-lowerbound",
    "permanent": true
  },
  {
    "source": "/verification/v1017_kernel_loewner_positivity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v1017_kernel_loewner_positivity.py",
    "permanent": true
  },
  {
    "source": "/verification/v1021_all_place_tate_rank_audit.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v1021_all_place_tate_rank_audit.py",
    "permanent": true
  },
  {
    "source": "/verification/v542_margin_chain_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v542_margin_chain_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v543_lumped_pair_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v543_lumped_pair_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v544_long_lag_support.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v544_long_lag_support.py",
    "permanent": true
  },
  {
    "source": "/verification/v545_hardy_core_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v545_hardy_core_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v546_capacity_chain_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v546_capacity_chain_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v547_level_lemma_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v547_level_lemma_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v548_green_szego_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v548_green_szego_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v549_gauge_parity_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v549_gauge_parity_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v550_odd_sector_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v550_odd_sector_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v551_ritz_ceiling_certificate.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v551_ritz_ceiling_certificate.py",
    "permanent": true
  },
  {
    "source": "/verification/v552_angle_instruments.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v552_angle_instruments.py",
    "permanent": true
  },
  {
    "source": "/verification/v553_exact_form_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v553_exact_form_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v554_sampling_harmonics_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v554_sampling_harmonics_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v555_pareto_tv_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v555_pareto_tv_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v556_gauge_ppr_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v556_gauge_ppr_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v557_cascade_vector_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v557_cascade_vector_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v558_bilinear_rank_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v558_bilinear_rank_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v559_phase2_capstone.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v559_phase2_capstone.py",
    "permanent": true
  },
  {
    "source": "/verification/v560_frame_deficit_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v560_frame_deficit_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v562_dense_limit_identities.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v562_dense_limit_identities.py",
    "permanent": true
  },
  {
    "source": "/verification/v563_paper2_readouts.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v563_paper2_readouts.py",
    "permanent": true
  },
  {
    "source": "/verification/v569_lambda_pencil_onemode.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v569_lambda_pencil_onemode.py",
    "permanent": true
  },
  {
    "source": "/verification/v570_separation_floor.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v570_separation_floor.py",
    "permanent": true
  },
  {
    "source": "/verification/v573_pair_band_structure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v573_pair_band_structure.py",
    "permanent": true
  },
  {
    "source": "/verification/v576_cheb_loewner_edge.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v576_cheb_loewner_edge.py",
    "permanent": true
  },
  {
    "source": "/verification/v577_nullray_census.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v577_nullray_census.py",
    "permanent": true
  },
  {
    "source": "/verification/v579_macro_kernel_signs.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v579_macro_kernel_signs.py",
    "permanent": true
  },
  {
    "source": "/verification/v580_occupation_map.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v580_occupation_map.py",
    "permanent": true
  },
  {
    "source": "/verification/v581_locking_transport.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v581_locking_transport.py",
    "permanent": true
  },
  {
    "source": "/verification/v582_density_dominance.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v582_density_dominance.py",
    "permanent": true
  },
  {
    "source": "/verification/v583_pnt_model.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v583_pnt_model.py",
    "permanent": true
  },
  {
    "source": "/verification/v585_pnt_locking_split.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v585_pnt_locking_split.py",
    "permanent": true
  },
  {
    "source": "/verification/v586_pnt_lock_direction.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v586_pnt_lock_direction.py",
    "permanent": true
  },
  {
    "source": "/verification/v587_w_closed_form.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v587_w_closed_form.py",
    "permanent": true
  },
  {
    "source": "/verification/v588_closed_delta.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v588_closed_delta.py",
    "permanent": true
  },
  {
    "source": "/verification/v589_zero_comb.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v589_zero_comb.py",
    "permanent": true
  },
  {
    "source": "/verification/v591_pole_rank_one.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v591_pole_rank_one.py",
    "permanent": true
  },
  {
    "source": "/verification/v592_continuum_det_law.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v592_continuum_det_law.py",
    "permanent": true
  },
  {
    "source": "/verification/v593_cutoff_completion.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v593_cutoff_completion.py",
    "permanent": true
  },
  {
    "source": "/verification/v594_unconditional_cert.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v594_unconditional_cert.py",
    "permanent": true
  },
  {
    "source": "/verification/v595_mapping_completion.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v595_mapping_completion.py",
    "permanent": true
  },
  {
    "source": "/verification/v596_lock_projection.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v596_lock_projection.py",
    "permanent": true
  },
  {
    "source": "/verification/v618_uniform_constant.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v618_uniform_constant.py",
    "permanent": true
  },
  {
    "source": "/verification/v619_flip_mechanics.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v619_flip_mechanics.py",
    "permanent": true
  },
  {
    "source": "/verification/v625_prime_shadow.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v625_prime_shadow.py",
    "permanent": true
  },
  {
    "source": "/verification/v627_hodge_chamber.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v627_hodge_chamber.py",
    "permanent": true
  },
  {
    "source": "/verification/v630_suzuki_contact.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v630_suzuki_contact.py",
    "permanent": true
  },
  {
    "source": "/verification/v631_w1_dictionary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v631_w1_dictionary.py",
    "permanent": true
  },
  {
    "source": "/verification/v635_p_canonicity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v635_p_canonicity.py",
    "permanent": true
  },
  {
    "source": "/verification/v636_p_construction.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v636_p_construction.py",
    "permanent": true
  },
  {
    "source": "/verification/v637_fine_c1_bridge.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v637_fine_c1_bridge.py",
    "permanent": true
  },
  {
    "source": "/verification/v640_w1_boundary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v640_w1_boundary.py",
    "permanent": true
  },
  {
    "source": "/verification/v641_w1_portability.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v641_w1_portability.py",
    "permanent": true
  },
  {
    "source": "/verification/v642_w1_matrix.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v642_w1_matrix.py",
    "permanent": true
  },
  {
    "source": "/verification/v643_w1_theorem.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v643_w1_theorem.py",
    "permanent": true
  },
  {
    "source": "/verification/v644_w2_form_density.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v644_w2_form_density.py",
    "permanent": true
  },
  {
    "source": "/verification/v648_sign_uncertainty.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v648_sign_uncertainty.py",
    "permanent": true
  },
  {
    "source": "/verification/v655_w2_mosco.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v655_w2_mosco.py",
    "permanent": true
  },
  {
    "source": "/verification/v656_margin_link.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v656_margin_link.py",
    "permanent": true
  },
  {
    "source": "/verification/v657_rid_alignment.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v657_rid_alignment.py",
    "permanent": true
  },
  {
    "source": "/verification/v658_w3_uniform_bound.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v658_w3_uniform_bound.py",
    "permanent": true
  },
  {
    "source": "/verification/v659_w3_landscape.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v659_w3_landscape.py",
    "permanent": true
  },
  {
    "source": "/verification/v660_theta_predicate.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v660_theta_predicate.py",
    "permanent": true
  },
  {
    "source": "/verification/v661_garding.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v661_garding.py",
    "permanent": true
  },
  {
    "source": "/verification/v662_garding_edgeband.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v662_garding_edgeband.py",
    "permanent": true
  },
  {
    "source": "/verification/v663_garding_envelope.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v663_garding_envelope.py",
    "permanent": true
  },
  {
    "source": "/verification/v665_keiper_li.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v665_keiper_li.py",
    "permanent": true
  },
  {
    "source": "/verification/v666_turing_cert.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v666_turing_cert.py",
    "permanent": true
  },
  {
    "source": "/verification/v667_baez_duarte.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v667_baez_duarte.py",
    "permanent": true
  },
  {
    "source": "/verification/v668_ground_truth.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v668_ground_truth.py",
    "permanent": true
  },
  {
    "source": "/verification/v669_fejer_density.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v669_fejer_density.py",
    "permanent": true
  },
  {
    "source": "/verification/v670_w3_block_deflation.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v670_w3_block_deflation.py",
    "permanent": true
  },
  {
    "source": "/verification/v671_lehmer_resonance.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v671_lehmer_resonance.py",
    "permanent": true
  },
  {
    "source": "/verification/v672_li_corollary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v672_li_corollary.py",
    "permanent": true
  },
  {
    "source": "/verification/v673_li_e4.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v673_li_e4.py",
    "permanent": true
  },
  {
    "source": "/verification/v674_packet_garding.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v674_packet_garding.py",
    "permanent": true
  },
  {
    "source": "/verification/v675_needle_mechanism.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v675_needle_mechanism.py",
    "permanent": true
  },
  {
    "source": "/verification/v676_c1_mechanism.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v676_c1_mechanism.py",
    "permanent": true
  },
  {
    "source": "/verification/v677_w3_structure_theorem.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v677_w3_structure_theorem.py",
    "permanent": true
  },
  {
    "source": "/verification/v678_zero_gap_theorem.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v678_zero_gap_theorem.py",
    "permanent": true
  },
  {
    "source": "/verification/v680_pinch_attack.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v680_pinch_attack.py",
    "permanent": true
  },
  {
    "source": "/verification/v681_coverage_hole.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v681_coverage_hole.py",
    "permanent": true
  },
  {
    "source": "/verification/v682_lk_split_theta.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v682_lk_split_theta.py",
    "permanent": true
  },
  {
    "source": "/verification/v683_rank3_functionals.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v683_rank3_functionals.py",
    "permanent": true
  },
  {
    "source": "/verification/v684_rank3_zeroside.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v684_rank3_zeroside.py",
    "permanent": true
  },
  {
    "source": "/verification/v685_rank3_uniformity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v685_rank3_uniformity.py",
    "permanent": true
  },
  {
    "source": "/verification/v686_geometric_sos.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v686_geometric_sos.py",
    "permanent": true
  },
  {
    "source": "/verification/v687_extremal_kernel.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v687_extremal_kernel.py",
    "permanent": true
  },
  {
    "source": "/verification/v688_interpolation_detector.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v688_interpolation_detector.py",
    "permanent": true
  },
  {
    "source": "/verification/v691_hecke_sos.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v691_hecke_sos.py",
    "permanent": true
  },
  {
    "source": "/verification/v692_rank3_lockgram.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v692_rank3_lockgram.py",
    "permanent": true
  },
  {
    "source": "/verification/v693_rank3_density_close.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v693_rank3_density_close.py",
    "permanent": true
  },
  {
    "source": "/verification/v694_interpolation_lemma_closure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v694_interpolation_lemma_closure.py",
    "permanent": true
  },
  {
    "source": "/verification/v695_z1_trace_operator.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v695_z1_trace_operator.py",
    "permanent": true
  },
  {
    "source": "/verification/v696_z1_jacobi.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v696_z1_jacobi.py",
    "permanent": true
  },
  {
    "source": "/verification/v697_z1_uvarov.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v697_z1_uvarov.py",
    "permanent": true
  },
  {
    "source": "/verification/v698_z1_flow_recursion.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v698_z1_flow_recursion.py",
    "permanent": true
  },
  {
    "source": "/verification/v701_big_picture_hunt.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v701_big_picture_hunt.py",
    "permanent": true
  },
  {
    "source": "/verification/v702_z1_lookahead.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v702_z1_lookahead.py",
    "permanent": true
  },
  {
    "source": "/verification/v703_chain_tolerance_scaling.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v703_chain_tolerance_scaling.py",
    "permanent": true
  },
  {
    "source": "/verification/v704_chain_mass_law.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v704_chain_mass_law.py",
    "permanent": true
  },
  {
    "source": "/verification/v706_chain_weyl_mass.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v706_chain_weyl_mass.py",
    "permanent": true
  },
  {
    "source": "/verification/v707_chain_section_edge.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v707_chain_section_edge.py",
    "permanent": true
  },
  {
    "source": "/verification/v708_chain_position_functional.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v708_chain_position_functional.py",
    "permanent": true
  },
  {
    "source": "/verification/v709_chain_zero_layer.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v709_chain_zero_layer.py",
    "permanent": true
  },
  {
    "source": "/verification/v710_chain_two_stage_hecke.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v710_chain_two_stage_hecke.py",
    "permanent": true
  },
  {
    "source": "/verification/v711_chain_firstbirth_scaling.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v711_chain_firstbirth_scaling.py",
    "permanent": true
  },
  {
    "source": "/verification/v712_rank3_transverse_deck.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v712_rank3_transverse_deck.py",
    "permanent": true
  },
  {
    "source": "/verification/v713_l1_montage.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v713_l1_montage.py",
    "permanent": true
  },
  {
    "source": "/verification/v714_moonshot_hecke_groupoid.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v714_moonshot_hecke_groupoid.py",
    "permanent": true
  },
  {
    "source": "/verification/v716_moonshot_arch_glue.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v716_moonshot_arch_glue.py",
    "permanent": true
  },
  {
    "source": "/verification/v717_moonshot_state.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v717_moonshot_state.py",
    "permanent": true
  },
  {
    "source": "/verification/v718_moonshot_spectral.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v718_moonshot_spectral.py",
    "permanent": true
  },
  {
    "source": "/verification/v719_moonshot_traceformula.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v719_moonshot_traceformula.py",
    "permanent": true
  },
  {
    "source": "/verification/v720_moonshot_k2k3.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v720_moonshot_k2k3.py",
    "permanent": true
  },
  {
    "source": "/verification/v721_k1_node_capture.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v721_k1_node_capture.py",
    "permanent": true
  },
  {
    "source": "/verification/v727_l1_identification.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v727_l1_identification.py",
    "permanent": true
  },
  {
    "source": "/verification/v728_k1b_superresolution.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v728_k1b_superresolution.py",
    "permanent": true
  },
  {
    "source": "/verification/v729_strat2_rp_universality.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v729_strat2_rp_universality.py",
    "permanent": true
  },
  {
    "source": "/verification/v730_strat2_pinning_lemma.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v730_strat2_pinning_lemma.py",
    "permanent": true
  },
  {
    "source": "/verification/v731_strat2_gap_universality.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v731_strat2_gap_universality.py",
    "permanent": true
  },
  {
    "source": "/verification/v732_strat3_sonin_prolate.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v732_strat3_sonin_prolate.py",
    "permanent": true
  },
  {
    "source": "/verification/v733_strat3_gate0_census.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v733_strat3_gate0_census.py",
    "permanent": true
  },
  {
    "source": "/verification/v734_s1_canonical.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v734_s1_canonical.py",
    "permanent": true
  },
  {
    "source": "/verification/v735_strat3_ucp_inductive.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v735_strat3_ucp_inductive.py",
    "permanent": true
  },
  {
    "source": "/verification/v738_hecke_mod_ramified.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v738_hecke_mod_ramified.py",
    "permanent": true
  },
  {
    "source": "/verification/v739_rank3_jet.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v739_rank3_jet.py",
    "permanent": true
  },
  {
    "source": "/verification/v740_kms_extension_switch.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v740_kms_extension_switch.py",
    "permanent": true
  },
  {
    "source": "/verification/v741_kms_toeplitz_semigroup.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v741_kms_toeplitz_semigroup.py",
    "permanent": true
  },
  {
    "source": "/verification/v742_channel_interference.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v742_channel_interference.py",
    "permanent": true
  },
  {
    "source": "/verification/v743_schur_cone_recursion.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v743_schur_cone_recursion.py",
    "permanent": true
  },
  {
    "source": "/verification/v744_hecke_channel_columns.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v744_hecke_channel_columns.py",
    "permanent": true
  },
  {
    "source": "/verification/v749_simpler_tower.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v749_simpler_tower.py",
    "permanent": true
  },
  {
    "source": "/verification/v750_simpler_gluing.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v750_simpler_gluing.py",
    "permanent": true
  },
  {
    "source": "/verification/v751_ward_monotone.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v751_ward_monotone.py",
    "permanent": true
  },
  {
    "source": "/verification/v753_ramified_polarity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v753_ramified_polarity.py",
    "permanent": true
  },
  {
    "source": "/verification/v754_ramodd_twostep.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v754_ramodd_twostep.py",
    "permanent": true
  },
  {
    "source": "/verification/v755_simpler_schur_recursion.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v755_simpler_schur_recursion.py",
    "permanent": true
  },
  {
    "source": "/verification/v756_kms_incidence_stinespring.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v756_kms_incidence_stinespring.py",
    "permanent": true
  },
  {
    "source": "/verification/v758_simpler_certificate.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v758_simpler_certificate.py",
    "permanent": true
  },
  {
    "source": "/verification/v759_handoff_fixed_window_resolution.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v759_handoff_fixed_window_resolution.py",
    "permanent": true
  },
  {
    "source": "/verification/v760_antialias_exact.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v760_antialias_exact.py",
    "permanent": true
  },
  {
    "source": "/verification/v761_atom_pole_abel.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v761_atom_pole_abel.py",
    "permanent": true
  },
  {
    "source": "/verification/v762_dense_weil_core.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v762_dense_weil_core.py",
    "permanent": true
  },
  {
    "source": "/verification/v763_yosida_handoff.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v763_yosida_handoff.py",
    "permanent": true
  },
  {
    "source": "/verification/v765_handoff_redteam.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v765_handoff_redteam.py",
    "permanent": true
  },
  {
    "source": "/verification/v766_handoff_bulk.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v766_handoff_bulk.py",
    "permanent": true
  },
  {
    "source": "/verification/v767_handoff_frequency_gram.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v767_handoff_frequency_gram.py",
    "permanent": true
  },
  {
    "source": "/verification/v768_handoff_tail_weil.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v768_handoff_tail_weil.py",
    "permanent": true
  },
  {
    "source": "/verification/v769_qf_contract_necessity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v769_qf_contract_necessity.py",
    "permanent": true
  },
  {
    "source": "/verification/v770_qf_spectral_bundle.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v770_qf_spectral_bundle.py",
    "permanent": true
  },
  {
    "source": "/verification/v771_qf_representation_census.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v771_qf_representation_census.py",
    "permanent": true
  },
  {
    "source": "/verification/v772_qf_feshbach_effective.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v772_qf_feshbach_effective.py",
    "permanent": true
  },
  {
    "source": "/verification/v773_qf_cell_cocycle.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v773_qf_cell_cocycle.py",
    "permanent": true
  },
  {
    "source": "/verification/v780_z1_compactness_trilogy.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v780_z1_compactness_trilogy.py",
    "permanent": true
  },
  {
    "source": "/verification/v786_prime_packet480.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v786_prime_packet480.py",
    "permanent": true
  },
  {
    "source": "/verification/v791_positive_descent.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v791_positive_descent.py",
    "permanent": true
  },
  {
    "source": "/verification/v793_f8sector_conductor.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v793_f8sector_conductor.py",
    "permanent": true
  },
  {
    "source": "/verification/v794_cp_extension_gate.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v794_cp_extension_gate.py",
    "permanent": true
  },
  {
    "source": "/verification/v801_prime_cp_intertwiner.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v801_prime_cp_intertwiner.py",
    "permanent": true
  },
  {
    "source": "/verification/v804_prime_carrier_gray.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v804_prime_carrier_gray.py",
    "permanent": true
  },
  
  {
    "source": "/verification/v811_prime_kraus_doily.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v811_prime_kraus_doily.py",
    "permanent": true
  },
  {
    "source": "/verification/v815_kraus_spread_commutant.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v815_kraus_spread_commutant.py",
    "permanent": true
  },
  {
    "source": "/verification/v816_prime_mosco_selection.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v816_prime_mosco_selection.py",
    "permanent": true
  },
  {
    "source": "/verification/v818_sector_floor_attack.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v818_sector_floor_attack.py",
    "permanent": true
  },
  {
    "source": "/verification/v819_prime_packet_rm14.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v819_prime_packet_rm14.py",
    "permanent": true
  },
  {
    "source": "/verification/v820_prime_kraus_rm24.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v820_prime_kraus_rm24.py",
    "permanent": true
  },
  {
    "source": "/verification/v821_prime_vacuum35.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v821_prime_vacuum35.py",
    "permanent": true
  },
  {
    "source": "/verification/v822_prime_vacuum_dilation.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v822_prime_vacuum_dilation.py",
    "permanent": true
  },
  {
    "source": "/verification/v823_prime_lagrange_floor.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v823_prime_lagrange_floor.py",
    "permanent": true
  },
  {
    "source": "/verification/v824_prime_floor_skeleton.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v824_prime_floor_skeleton.py",
    "permanent": true
  },
  {
    "source": "/verification/v825_prime_exclusion_ladder.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v825_prime_exclusion_ladder.py",
    "permanent": true
  },
  {
    "source": "/verification/v826_prime_exclusion_battery2.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v826_prime_exclusion_battery2.py",
    "permanent": true
  },
  {
    "source": "/verification/v827_prime_zero_locator.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v827_prime_zero_locator.py",
    "permanent": true
  },
  {
    "source": "/verification/v828_prime_comb_window.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v828_prime_comb_window.py",
    "permanent": true
  },
  {
    "source": "/verification/v829_prime_floor_depth.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v829_prime_floor_depth.py",
    "permanent": true
  },
  {
    "source": "/verification/v830_prime_float_budget.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v830_prime_float_budget.py",
    "permanent": true
  },
  {
    "source": "/verification/v831_prime_alias_second_moment.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v831_prime_alias_second_moment.py",
    "permanent": true
  },
  {
    "source": "/verification/v835_corner_hjelmslev_tower.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v835_corner_hjelmslev_tower.py",
    "permanent": true
  },
  {
    "source": "/verification/v836_commutant_sos_closure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v836_commutant_sos_closure.py",
    "permanent": true
  },
  {
    "source": "/verification/v837_corner_closure_quantifier.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v837_corner_closure_quantifier.py",
    "permanent": true
  },
  {
    "source": "/verification/v838_corner_expectation_position.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v838_corner_expectation_position.py",
    "permanent": true
  },
  {
    "source": "/verification/v839_paircorr_bridge_saturation.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v839_paircorr_bridge_saturation.py",
    "permanent": true
  },
  {
    "source": "/verification/v840_gue_ablation_loopgain.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v840_gue_ablation_loopgain.py",
    "permanent": true
  },
  {
    "source": "/verification/v841_relation_carrier_ladder.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v841_relation_carrier_ladder.py",
    "permanent": true
  },
  {
    "source": "/verification/v842_excess_certified_skeleton.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v842_excess_certified_skeleton.py",
    "permanent": true
  },
  {
    "source": "/verification/v843_margin_law_excess_lean.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v843_margin_law_excess_lean.py",
    "permanent": true
  },
  {
    "source": "/verification/v846_schur_spectral_mother.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v846_schur_spectral_mother.py",
    "permanent": true
  },
  {
    "source": "/verification/v847_wedge_cellcone_transport.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v847_wedge_cellcone_transport.py",
    "permanent": true
  },
  {
    "source": "/verification/v848_extraction_chain.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v848_extraction_chain.py",
    "permanent": true
  },
  {
    "source": "/verification/v850_completion_tax_flow.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v850_completion_tax_flow.py",
    "permanent": true
  },
  {
    "source": "/verification/v851_cluster_kernel_field.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v851_cluster_kernel_field.py",
    "permanent": true
  },
  {
    "source": "/verification/v854_relation_hodge_pfaffian.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v854_relation_hodge_pfaffian.py",
    "permanent": true
  },
  {
    "source": "/verification/v855_invariance_atlas.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v855_invariance_atlas.py",
    "permanent": true
  },
  {
    "source": "/verification/v856_connected_current_lean.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v856_connected_current_lean.py",
    "permanent": true
  },
  {
    "source": "/verification/v859_grade_no_go_elevator.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v859_grade_no_go_elevator.py",
    "permanent": true
  },
  {
    "source": "/verification/v860_phase_lever_closure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v860_phase_lever_closure.py",
    "permanent": true
  },
  {
    "source": "/verification/v861_krein_normalform_lean.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v861_krein_normalform_lean.py",
    "permanent": true
  },
  {
    "source": "/verification/v862_defect_polar_weld.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v862_defect_polar_weld.py",
    "permanent": true
  },
  {
    "source": "/verification/v863_redheffer_colligation.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v863_redheffer_colligation.py",
    "permanent": true
  },
  {
    "source": "/verification/v864_softport_kappa_law.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v864_softport_kappa_law.py",
    "permanent": true
  },
  {
    "source": "/verification/v865_weyl_port_readout.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v865_weyl_port_readout.py",
    "permanent": true
  },
  {
    "source": "/verification/v866_source_contractor_formula.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v866_source_contractor_formula.py",
    "permanent": true
  },
  {
    "source": "/verification/v867_radau_conditioning.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v867_radau_conditioning.py",
    "permanent": true
  },
  {
    "source": "/verification/v869_cdcore_clarkphase.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v869_cdcore_clarkphase.py",
    "permanent": true
  },
  {
    "source": "/verification/v870_christoffel_gauss_frame.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v870_christoffel_gauss_frame.py",
    "permanent": true
  },
  {
    "source": "/verification/v871_pole_uvarov_crossdefect.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v871_pole_uvarov_crossdefect.py",
    "permanent": true
  },
  {
    "source": "/verification/v872_damping_compensation.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v872_damping_compensation.py",
    "permanent": true
  },
  {
    "source": "/verification/v873_pruefer_cotlar_decision.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v873_pruefer_cotlar_decision.py",
    "permanent": true
  },
  {
    "source": "/verification/v876_carleson_polygon_wave.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v876_carleson_polygon_wave.py",
    "permanent": true
  },
  {
    "source": "/verification/v877_complete_comb_reversal.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v877_complete_comb_reversal.py",
    "permanent": true
  },
  {
    "source": "/verification/v879_envelope_partition_closure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v879_envelope_partition_closure.py",
    "permanent": true
  },
  {
    "source": "/verification/v881_carleson_port_geometry.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v881_carleson_port_geometry.py",
    "permanent": true
  },
  {
    "source": "/verification/v882_port_source_mellin.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v882_port_source_mellin.py",
    "permanent": true
  },
  {
    "source": "/verification/v883_tau_chain_parametrix.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v883_tau_chain_parametrix.py",
    "permanent": true
  },
  {
    "source": "/verification/v884_certified_head_positivity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v884_certified_head_positivity.py",
    "permanent": true
  },
  {
    "source": "/verification/v885_ladder_flow_anatomy.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v885_ladder_flow_anatomy.py",
    "permanent": true
  },
  {
    "source": "/verification/v886_register_gapcode_null.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v886_register_gapcode_null.py",
    "permanent": true
  },
  {
    "source": "/verification/v887_certified_ladder_complete.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v887_certified_ladder_complete.py",
    "permanent": true
  },
  {
    "source": "/verification/v889_route_decisions.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v889_route_decisions.py",
    "permanent": true
  },
  {
    "source": "/verification/v890_total_positivity_flow.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v890_total_positivity_flow.py",
    "permanent": true
  },
  {
    "source": "/verification/v891_moebius_firewall_kills.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v891_moebius_firewall_kills.py",
    "permanent": true
  },
  {
    "source": "/verification/v892_closure_architecture.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v892_closure_architecture.py",
    "permanent": true
  },
  {
    "source": "/verification/v893_relative_margins.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v893_relative_margins.py",
    "permanent": true
  },
  {
    "source": "/verification/v894_diagonal_refinement.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v894_diagonal_refinement.py",
    "permanent": true
  },
  {
    "source": "/verification/v895_collective_comb.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v895_collective_comb.py",
    "permanent": true
  },
  {
    "source": "/verification/v897_certified_interval_ladder.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v897_certified_interval_ladder.py",
    "permanent": true
  },
  {
    "source": "/verification/v899_christoffel_normsquare.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v899_christoffel_normsquare.py",
    "permanent": true
  },
  {
    "source": "/verification/v900_core_update_anatomy.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v900_core_update_anatomy.py",
    "permanent": true
  },
  {
    "source": "/verification/v901_tangent_schur_bfloor.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v901_tangent_schur_bfloor.py",
    "permanent": true
  },
  {
    "source": "/verification/v902_wall_relocation_map.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v902_wall_relocation_map.py",
    "permanent": true
  },
  {
    "source": "/verification/v904_healthcode12_diagnostic.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v904_healthcode12_diagnostic.py",
    "permanent": true
  },
  {
    "source": "/verification/v905_bfloor_ideal_certificate.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v905_bfloor_ideal_certificate.py",
    "permanent": true
  },
  {
    "source": "/verification/v906_tail_cartography.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v906_tail_cartography.py",
    "permanent": true
  },
  {
    "source": "/verification/v907_halfgap_registered_target.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v907_halfgap_registered_target.py",
    "permanent": true
  },
  {
    "source": "/verification/v909_finite_wall_closure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v909_finite_wall_closure.py",
    "permanent": true
  },
  {
    "source": "/verification/v910_finite_zero_transfer.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v910_finite_zero_transfer.py",
    "permanent": true
  },
  {
    "source": "/verification/v912_form_convergence_theorem.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v912_form_convergence_theorem.py",
    "permanent": true
  },
  {
    "source": "/verification/v913_signed_alignment_localization.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v913_signed_alignment_localization.py",
    "permanent": true
  },
  {
    "source": "/verification/v914_pascal_region_theorem.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v914_pascal_region_theorem.py",
    "permanent": true
  },
  {
    "source": "/verification/v915_eulerpick_certified_floors.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v915_eulerpick_certified_floors.py",
    "permanent": true
  },
  {
    "source": "/verification/v916_epstein_weil_violation.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v916_epstein_weil_violation.py",
    "permanent": true
  },
  {
    "source": "/verification/v917_driver_rate_certification.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v917_driver_rate_certification.py",
    "permanent": true
  },
  {
    "source": "/verification/v918_doublelimit_reduction_theorem.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v918_doublelimit_reduction_theorem.py",
    "permanent": true
  },
  {
    "source": "/verification/v919_secular_gw_pinning.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v919_secular_gw_pinning.py",
    "permanent": true
  },
  {
    "source": "/verification/v920_loop_equivalence_theorems.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v920_loop_equivalence_theorems.py",
    "permanent": true
  },
  {
    "source": "/verification/v921_counting_dominance_closures.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v921_counting_dominance_closures.py",
    "permanent": true
  },
  {
    "source": "/verification/v922_spacing_jet_sumrule_theorems.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v922_spacing_jet_sumrule_theorems.py",
    "permanent": true
  },
  {
    "source": "/verification/v923_spectral_balance_razor_theorems.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v923_spectral_balance_razor_theorems.py",
    "permanent": true
  },
  {
    "source": "/verification/v924_moment_laurent_rootladder.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v924_moment_laurent_rootladder.py",
    "permanent": true
  },
  {
    "source": "/verification/v925_edge_cleanup_closures.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v925_edge_cleanup_closures.py",
    "permanent": true
  },
  {
    "source": "/verification/v926_fullgap_growthlaw_theorems.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v926_fullgap_growthlaw_theorems.py",
    "permanent": true
  },
  {
    "source": "/verification/v927_blockaverage_substrate_theorems.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v927_blockaverage_substrate_theorems.py",
    "permanent": true
  },
  {
    "source": "/verification/v928_depthblock_transfer_theorems.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v928_depthblock_transfer_theorems.py",
    "permanent": true
  },
  {
    "source": "/verification/v929_sigmafloor_factorization.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v929_sigmafloor_factorization.py",
    "permanent": true
  },
  {
    "source": "/verification/v930_window_instrument_mechanism.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v930_window_instrument_mechanism.py",
    "permanent": true
  },
  {
    "source": "/verification/v931_jetmass_floor_theorems.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v931_jetmass_floor_theorems.py",
    "permanent": true
  },
  {
    "source": "/verification/v932_toproot_theta_statement.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v932_toproot_theta_statement.py",
    "permanent": true
  },
  {
    "source": "/verification/v933_h3_cofinal_adjudication.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v933_h3_cofinal_adjudication.py",
    "permanent": true
  },
  {
    "source": "/verification/v934_gonek_pricing_unconditional.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v934_gonek_pricing_unconditional.py",
    "permanent": true
  },
  {
    "source": "/verification/v935_thetainf_landau_bridge.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v935_thetainf_landau_bridge.py",
    "permanent": true
  },
  {
    "source": "/verification/v936_manifold_invariance_exclusion.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v936_manifold_invariance_exclusion.py",
    "permanent": true
  },
  {
    "source": "/verification/v937_l1wpd_closure_reduction.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v937_l1wpd_closure_reduction.py",
    "permanent": true
  },
  {
    "source": "/verification/v938_dbn_heatflow_census.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v938_dbn_heatflow_census.py",
    "permanent": true
  },
  {
    "source": "/verification/v939_cbj_frame_adjudication.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v939_cbj_frame_adjudication.py",
    "permanent": true
  },
  {
    "source": "/verification/v940_cbj_subdof_blockfloor.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v940_cbj_subdof_blockfloor.py",
    "permanent": true
  },
  {
    "source": "/verification/v941_alignment_law_factorization.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v941_alignment_law_factorization.py",
    "permanent": true
  },
  {
    "source": "/verification/v942_pi_pattern_transfer_specificity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v942_pi_pattern_transfer_specificity.py",
    "permanent": true
  },
  {
    "source": "/verification/v943_mangoldt_ablation_localization.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v943_mangoldt_ablation_localization.py",
    "permanent": true
  },
  {
    "source": "/verification/v944_ground_residue_observability.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v944_ground_residue_observability.py",
    "permanent": true
  },
  {
    "source": "/verification/v945_zero_causal_stratification.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v945_zero_causal_stratification.py",
    "permanent": true
  },
  {
    "source": "/verification/v946_census_krein_pencil.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v946_census_krein_pencil.py",
    "permanent": true
  },
  {
    "source": "/verification/v947_loewner_pick_dictionary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v947_loewner_pick_dictionary.py",
    "permanent": true
  },
  {
    "source": "/verification/v948_krein_sign_characteristic.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v948_krein_sign_characteristic.py",
    "permanent": true
  },
  {
    "source": "/verification/v949_commensurability_mechanism.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v949_commensurability_mechanism.py",
    "permanent": true
  },
  {
    "source": "/verification/v950_zero_channel_capacity.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v950_zero_channel_capacity.py",
    "permanent": true
  },
  {
    "source": "/verification/v951_cancellation_functional.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v951_cancellation_functional.py",
    "permanent": true
  },
  {
    "source": "/verification/v952_turan_extremal.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v952_turan_extremal.py",
    "permanent": true
  },
  {
    "source": "/verification/v953_fewatom_reduction.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v953_fewatom_reduction.py",
    "permanent": true
  },
  {
    "source": "/verification/v954_nodeless_pf.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v954_nodeless_pf.py",
    "permanent": true
  },
  {
    "source": "/verification/v955_tau_iiks_toda_dictionary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v955_tau_iiks_toda_dictionary.py",
    "permanent": true
  },
  {
    "source": "/verification/v956_signedmoment_halffilling_duality.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v956_signedmoment_halffilling_duality.py",
    "permanent": true
  },
  {
    "source": "/verification/v958_bordered_tau_readout_dictionary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v958_bordered_tau_readout_dictionary.py",
    "permanent": true
  },
  {
    "source": "/verification/v959_coupledtau_terminal_dictionary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v959_coupledtau_terminal_dictionary.py",
    "permanent": true
  },
  {
    "source": "/verification/v960_terminal_surface_closure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v960_terminal_surface_closure.py",
    "permanent": true
  },
  {
    "source": "/verification/v961_midpoint_orientation_dictionary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v961_midpoint_orientation_dictionary.py",
    "permanent": true
  },
  {
    "source": "/verification/v962_halffilling_pinning_theory.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v962_halffilling_pinning_theory.py",
    "permanent": true
  },
  {
    "source": "/verification/v963_lstar_reduction_dictionary.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v963_lstar_reduction_dictionary.py",
    "permanent": true
  },
  {
    "source": "/verification/v964_lstar_coherence_census.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v964_lstar_coherence_census.py",
    "permanent": true
  },
  {
    "source": "/verification/v965_lstar_curvature_arc.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v965_lstar_curvature_arc.py",
    "permanent": true
  },
  {
    "source": "/verification/v966_l2_reduction_chain.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v966_l2_reduction_chain.py",
    "permanent": true
  },
  {
    "source": "/verification/v967_l2_cascade_closure.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v967_l2_cascade_closure.py",
    "permanent": true
  },
  {
    "source": "/verification/v968_architecture_adjudication.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v968_architecture_adjudication.py",
    "permanent": true
  },
  {
    "source": "/verification/v969_forks_and_redteam.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v969_forks_and_redteam.py",
    "permanent": true
  },
  {
    "source": "/verification/v970_extraction_and_composition.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v970_extraction_and_composition.py",
    "permanent": true
  },
  {
    "source": "/verification/v978_terminal_density_martingale.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v978_terminal_density_martingale.py",
    "permanent": true
  },
  {
    "source": "/verification/v979_cover_growth_k2.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v979_cover_growth_k2.py",
    "permanent": true
  },
  {
    "source": "/verification/v980_lstar_margin_chain.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v980_lstar_margin_chain.py",
    "permanent": true
  },
  {
    "source": "/verification/v981_lstar_borodin_duality.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v981_lstar_borodin_duality.py",
    "permanent": true
  },
  {
    "source": "/verification/v982_dirichlet_matched_frame.py",
    "destination": "https://prime.fixpoint-theory.com/verification/v982_dirichlet_matched_frame.py",
    "permanent": true
  }
]; },
  reactStrictMode: true,
  poweredByHeader: false,
  compress: true,
  experimental: {
    // Deliver the critical Tailwind and math styles with the initial HTML.
    inlineCss: true,
    optimizePackageImports: ["lucide-react", "motion"],
  },
};

export default nextConfig;
