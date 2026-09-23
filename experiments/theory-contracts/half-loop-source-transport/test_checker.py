"""Exact source-space identities, domain-bound controls and numerical replays."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import math
from pathlib import Path
import tempfile
import unittest

import mpmath as mp
import sympy as sp

import checker as c
import energy_matching as e


class SourceRootTests(unittest.TestCase):
    def test_pin_checks_and_no_new_states(self):
        report = c.root_certificate()
        self.assertEqual(report["original_matter_masks"], 70)
        self.assertEqual(report["added_states_or_sectors"], 0)
        self.assertFalse(report["source_selected_operator"])

    def test_mutated_pin_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "cell.py").write_text("mutation")
            with self.assertRaisesRegex(ValueError, "source changed"):
                c.verify_pins(directory)

    def test_invalid_state_and_pivot_rejected(self):
        for mask, pivot in ((0, 7), (105, -1), (105, 8)):
            with self.assertRaises(ValueError):
                c.half_step((mask, 0), pivot=pivot)
        for winding in (F(1, 2), .5, 0.0):
            with self.assertRaisesRegex(ValueError, "integer winding"):
                c.half_step((105, winding))

    def test_square_and_both_adjoints_for_large_signed_winding(self):
        for mask, w in product(c.MASKS, (-10**9, -3, 0, 5, 10**9)):
            state = mask, w
            s, sd = c.half_step(state), c.half_step(state, True)
            self.assertEqual(c.half_step(s), c.wilson(state))
            self.assertEqual(c.half_step(sd), state)
            self.assertEqual(c.half_step(s, True), state)

    def test_plain_matter_flip_does_not_supply_wilson_carry(self):
        source = 105, 0
        flip = lambda state: (state[0] ^ 255, state[1])
        self.assertNotEqual(flip(flip(source)), c.wilson(source))

    def test_source_chart_and_gauss_are_preserved(self):
        _, parent, data, _ = c.native()
        for mask, w, adjoint in product(c.MASKS, (-100, 0, 100), (False, True)):
            target = c.half_step((mask, w), adjoint)
            self.assertEqual(parent.gauss(data, (target[0], c.flux(target))), (0,) * 4)
            self.assertEqual(target[0].bit_count(), 4)

    def test_dressing_has_uniform_finite_integer_bound(self):
        for mask, adjoint in product(c.MASKS, (False, True)):
            source = mask, 17
            delta = [x - y for x, y in zip(c.flux(c.half_step(source, adjoint)), c.flux(source))]
            self.assertTrue(all(type(x) is int for x in delta))
            self.assertLessEqual(sum(x*x for x in delta), 44)

    def test_explicit_CAR_matrix_units_use_existing_modes_only(self):
        def apply(source, trial):
            sign, mask = 1, trial
            for i in range(8):
                if source >> i & 1:
                    if not mask >> i & 1:
                        return None
                    sign *= (-1)**(mask & ((1 << i)-1)).bit_count()
                    mask ^= 1 << i
            for i in range(8):
                if not source >> i & 1:
                    if mask >> i & 1:
                        return None
                    sign *= (-1)**(mask & ((1 << i)-1)).bit_count()
                    mask |= 1 << i
            return mask, sign
        for source, trial in product(c.MASKS, repeat=2):
            self.assertEqual(apply(source, trial), (source ^ 255, 1) if source == trial else None)

    def test_graph_domain_estimate_on_native_basis(self):
        _, p, _, _ = c.native()
        for mask, w, adjoint in product(c.MASKS, (-1000, -1, 0, 1, 1000), (False, True)):
            source = mask, w
            target = c.half_step(source, adjoint)
            hs = p.KAPPA * sum(x*x for x in c.flux(source)) / 2
            ht = p.KAPPA * sum(x*x for x in c.flux(target)) / 2
            self.assertLessEqual(ht, 2*hs + p.KAPPA * 44)

    def test_half_label_is_not_uniform_half_electric_shift(self):
        for mask in c.MASKS:
            source, target = (mask, 0), c.half_step((mask, 0))
            self.assertEqual(c.p_label(target) - c.p_label(source), F(1, 2))
            self.assertIn(target[1] - source[1], (0, 1))
            self.assertNotEqual(target[1] - source[1], F(1, 2))

    def test_singleton_charge_sectors_are_not_removed(self):
        census = Counter(c.charge(mask) for mask in c.MASKS)
        self.assertEqual(Counter(census.values()), Counter({1: 6, 4: 12, 16: 1}))


class DynamicsTests(unittest.TestCase):
    def test_diagonal_energy_matches_uncut_original_action(self):
        for mask, w in product(c.MASKS, (-100, 0, 100)):
            state = mask, w
            self.assertEqual(c.h_action(state).get(state, 0), c.h_diagonal(state))

    def test_half_label_not_conserved_by_actual_H(self):
        report = c.dynamical_test()
        self.assertEqual(report["P_H_commutator_nonzero_witness"]["P_change"], "-1")
        self.assertEqual(report["conserved_affine_charge_kernel_dimension"], 4)
        self.assertTrue(report["H_S_commutator_extra_outputs"])

    def test_all_diagonal_charges_are_scalar_in_full_winding_lift(self):
        report = c.diagonal_charge_test()
        self.assertEqual(report["matter_vertices"], 70)
        self.assertEqual(report["directed_transitions"], 640)
        self.assertEqual(report["cycle_winding_gcd"], 1)
        self.assertFalse(report["non_diagonal_conserved_operators_or_scaling_limits_excluded"])
        cycle = report["explicit_native_cycle"]
        self.assertEqual(cycle[-1], (cycle[0][0], -1))
        for source, target in zip(cycle, cycle[1:]):
            self.assertNotEqual(c.h_action(source).get(target, 0), 0)

    def test_actual_same_source_sequence(self):
        report = c.numerical_transport()
        self.assertLess(report["projected_output_norm_lost"], 1e-12)
        self.assertAlmostEqual(report["before_S"]["norm"], report["after_S"]["norm"], places=12)
        self.assertAlmostEqual(report["after_S"]["total_energy"],
                               report["after_further_evolution"]["total_energy"], places=11)
        self.assertNotAlmostEqual(report["before_S"]["total_energy"], report["after_S"]["total_energy"], places=6)


class ScalarRootTests(unittest.TestCase):
    def test_Fourier_coefficients_against_independent_integrals(self):
        with mp.workdps(40):
            for n in range(-4, 5):
                integral = mp.quad(lambda theta: mp.exp(1j*(mp.mpf("0.5")-n)*theta), [-mp.pi, mp.pi])/(2*mp.pi)
                self.assertLess(abs(integral - c.root_coeff(n)), mp.mpf("2e-16"))

    def test_root_square_in_angle_is_actual_W(self):
        with mp.workdps(40):
            for theta in (-3, -1, 0, 1, 3):
                root = mp.exp(.5j*theta)
                self.assertLess(abs(root**2 - mp.exp(1j*theta)), mp.mpf("1e-38"))

    def test_norm_converges_while_expected_energy_diverges(self):
        rows = c.scalar_root_test()["partial_sums"]
        self.assertLess(1 - rows[-1]["retained_norm_squared"], 1e-4)
        self.assertGreater(rows[-1]["electric_energy_partial_sum"], 8)
        self.assertLess(abs(rows[-1]["energy_divided_by_cutoff"] - 1/(25*math.pi**2)), 5e-6)


class EnergyMatchingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = e.energy_gate()

    def test_full_family_retains_mixing(self):
        self.assertEqual(self.report["invariant_family_dimension"], 6)
        self.assertFalse(self.report["diagonality_assumed"])

    def test_five_independent_comparisons_leave_only_scale(self):
        self.assertEqual(self.report["five_comparisons_rank"], 5)
        self.assertEqual(self.report["remaining_energy_family"], "G=v*I, v>0")

    def test_each_omitted_comparison_has_positive_counterexample(self):
        controls = self.report["minimality_controls"]
        self.assertEqual(len(controls), 5)
        for i, control in enumerate(controls):
            self.assertGreater(sp.Rational(control["positive_lower_bound"]), 0)
            self.assertEqual([j for j, x in enumerate(control["energy_differences"]) if x != "0"], [i])

    def test_pair_energy_cancels_arbitrary_background_and_reference(self):
        linear = sp.Matrix(sp.symbols("mu0:8"))
        reference = sp.Matrix(sp.symbols("r0:8"))
        offset = sp.Symbol("offset")
        for matrix in e.invariant_family()[1]:
            q = sp.ones(8, 1)/2
            self.assertEqual(e.centered_pair_energy(matrix, linear, offset, q, reference), e.energy(matrix, q))

    def test_actual_holonomy_does_not_kill_weight_one_half_twist(self):
        report = e.sourced_pair_check()
        self.assertEqual(report["root_pairs_checked"], 480)
        self.assertEqual((report["examples"][0]["half_twist_plus"], report["examples"][0]["half_twist_minus"]), ("0", "2"))
        self.assertEqual(report["examples"][0]["centered_pair"], "1")
        self.assertFalse(report["Hamiltonian_redefined_or_holonomy_retuned"])


if __name__ == "__main__":
    unittest.main()
