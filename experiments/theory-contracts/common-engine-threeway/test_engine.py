"""Finite exact checks, independent matrix checks, and explicit failing controls."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import tempfile
import unittest

import numpy as np
import sympy as sp

import cell
import reverse
from source_adapter import PINS, require, verify_pins


class SourceTests(unittest.TestCase):
    def test_pinned_sources_and_transitive_parent(self):
        verify_pins()
        p, data, _ = cell.geometry()
        self.assertEqual((p.A, p.ETA, p.BETA, p.KAPPA, p.MASS),
                         (F(1, 12), F(1, 2), F(1, 4), F(1, 100), F(4)))
        self.assertEqual(len(data["terms"]), 32)
        self.assertTrue(any(len(t[2]) == 2 for t in data["terms"]))

    def test_bad_pin_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / next(iter(PINS))
            first.parent.mkdir(parents=True)
            first.write_text("changed source")
            with self.assertRaisesRegex(ValueError, "digest changed"):
                verify_pins(directory)

    def test_guards_remain_active(self):
        with self.assertRaisesRegex(ValueError, "guard"):
            require(False, "guard")
        with self.assertRaises(ValueError):
            cell.physical_basis(-1, cell.geometry()[2])


class PhysicalCellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = cell.build(2)

    def test_gauss_enumeration_matches_independent_bruteforce(self):
        model = self.model
        expected = set()
        for mask in range(256):
            if mask.bit_count() != 4:
                continue
            q = [((mask >> x) & 1) + ((mask >> (x + 4)) & 1) - 1 for x in range(4)]
            for e0, e1, e2, e3 in product(range(-2, 3), repeat=4):
                if (q[0] + e0 + e1, q[1] - e1 + e2, q[2] - e0 + e3, q[3] - e2 - e3) == (0,) * 4:
                    expected.add((mask, (e0, e1, e2, e3)))
        self.assertEqual(set(model["states"]), expected)

    def test_all_native_moves_preserve_constraints(self):
        for column in self.model["columns"]:
            for state in column:
                self.assertEqual(self.model["parent"].gauss(self.model["data"], state), (0,) * 4)
                self.assertEqual(state[0].bit_count(), 4)

    def test_exact_matrix_is_hermitian(self):
        for source, column in zip(self.model["states"], self.model["columns"]):
            for target, amplitude in column.items():
                if target in self.model["lookup"]:
                    other = self.model["columns"][self.model["lookup"][target]]
                    self.assertEqual(amplitude, other.get(source, 0))

    def test_diagonal_really_is_original_electric_plus_onsite_energy(self):
        p = self.model["parent"]
        for (mask, flux), column in zip(self.model["states"], self.model["columns"]):
            energy = p.KAPPA * sum(e * e for e in flux) / 2 + p.MASS * (mask >> 4).bit_count()
            energy += p.BETA * p.A**2 * 6 * (mask & 15).bit_count()
            self.assertEqual(F(column.get((mask, flux), 0), p.DEN), energy)

    def test_native_fermion_signs_against_creation_annihilation(self):
        for mask, source, target in product(range(256), range(8), range(8)):
            expected = None
            if mask & (1 << source):
                intermediate = mask ^ (1 << source)
                sign = (-1)**(mask & ((1 << source) - 1)).bit_count()
                if not intermediate & (1 << target):
                    sign *= (-1)**(intermediate & ((1 << target) - 1)).bit_count()
                    expected = (intermediate | (1 << target), sign)
            self.assertEqual(self.model["parent"].move(mask, source, target), expected)

    def test_hodge_reduction_and_nonadditivity(self):
        report = cell.hodge_record()
        self.assertEqual(report["mixed_charge_energy_at_fixed_integer_winding"], "1/100")
        self.assertEqual(report["cycle_vector"], [1, -1, -1, 1])

    def test_spectator_changes_same_hop_energy_not_its_coefficient(self):
        report = cell.hodge_record()
        transitions = report["same_hop_spectator_comparison"]
        self.assertEqual([row["amplitude"] for row in transitions], ["1/12", "1/12"])
        self.assertEqual([row["diagonal_energy_cost"] for row in transitions], ["1/200", "-1/200"])
        self.assertEqual(report["spectator_induced_transport_energy_shift"], "-1/100")

    def test_omitting_winding_charge_shift_is_wrong(self):
        b = self.model["incidence"]
        q = sp.Matrix([1, -1, 0, 0])
        full_energy_over_kappa = F(1, 2)  # Native E=(0,-1,0,0), w=0.
        longitudinal_only = (q.T * (b * b.T).pinv() * q)[0] / 2
        self.assertNotEqual(full_energy_over_kappa, longitudinal_only)
        self.assertEqual(longitudinal_only, sp.Rational(3, 8))

    def test_evolution_conserves_norm_and_energy(self):
        start = cell.initial(self.model)
        initial_energy = np.vdot(start, self.model["h"] @ start).real
        for time in (0, 1, 2):
            vector = cell.evolve(self.model, time, start)
            result = cell.readouts(self.model, vector)
            self.assertAlmostEqual(result["norm"], 1, places=12)
            self.assertAlmostEqual(result["total_energy"], initial_energy, places=11)
            self.assertAlmostEqual(sum(result["low_occupations"] + result["high_occupations"]), 4, places=11)

    def test_time_reversal_reconstructs_same_state(self):
        start = cell.initial(self.model)
        recovered = cell.evolve(self.model, -2, cell.evolve(self.model, 2, start))
        self.assertLess(np.linalg.norm(recovered - start), 2e-12)

    def test_nonzero_actual_transport(self):
        result = cell.readouts(self.model, cell.evolve(self.model, 1))
        self.assertGreater(result["low_occupations"][1], .01)
        self.assertGreater(result["any_flux_probability"], .02)

    def test_small_time_matches_original_all_low_jet(self):
        p = self.model["parent"]
        expected = float(p.local_jet(self.model["data"])["high_t2"])
        time = 1e-3
        result = cell.readouts(self.model, cell.evolve(self.model, time, cell.initial(self.model, ())))
        self.assertAlmostEqual(result["high_occupations"][0] / time**2, expected, delta=1e-8)


class ReverseTests(unittest.TestCase):
    def test_target_lattice_and_half_twist(self):
        result = reverse.target_record()
        self.assertEqual(result["integer_roots"] + result["spinor_roots"] + result["cartan_directions"], 248)
        self.assertFalse(result["microscopic_channel_selection_proved"])

    def test_odd_spinor_glue_is_not_same_target(self):
        basis = reverse.lattice_basis()
        wrong_spinor = sp.Matrix([-1] + [1] * 7)
        self.assertTrue(any(x.q != 1 for x in basis.inv() * wrong_spinor))

    def test_cyclic_bit_replacement_loses_integer_charge(self):
        half = ((0,) * 8, 1)
        self.assertEqual(reverse.physical(reverse.compose(half, half)), (2,) * 8)
        self.assertEqual(reverse.physical(reverse.compose(half, half, carry=False)), (0,) * 8)

    def test_transfer_operator_is_not_plain_flip(self):
        result = reverse.crossed_product_record()
        self.assertTrue(result["unitary_and_covariance"])
        self.assertFalse(result["E8_net_or_nontrivial_QCA_constructed"])

    def test_equal_velocity_constraint_and_counterexample(self):
        result = reverse.velocity_robustness()
        self.assertEqual(result["equal_energy_constraint_rank"], 7)
        self.assertEqual(result["rows"][1]["distinct_weights"], ["1", "81/80", "21/20"])

    def test_actual_symmetries_allow_velocity_mismatch(self):
        result = reverse.source_symmetry_velocity_test()
        self.assertEqual(result["remaining_velocity_scales"], 2)
        self.assertEqual(result["root_weights_in_counterexample"], ["1", "41/40", "21/20", "11/10"])

    def test_one_half_current_energy_match_would_lock_relative_velocity(self):
        result = reverse.source_symmetry_velocity_test()
        self.assertEqual(result["half_twist_minus_first_six_integer_root_energy"], "(b-a)/4")


class RobustnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = cell.robustness_record()

    def test_cutoff_and_independent_solver(self):
        self.assertLess(self.report["independent_solver_difference"], 5e-12)
        final = [row for row in self.report["cutoff_rows"] if row["cutoffs"] == [8, 10]]
        self.assertEqual(len(final), 3)
        self.assertLess(max(row["vector_difference"] for row in final), 1e-10)

    def test_electric_backreaction_is_resolved(self):
        change = self.report["deformations"][0]["max_low_occupation_change"]
        self.assertGreater(change, 100 * 2 * self.report["reference_flux_readout_bound"])

    def test_small_parameter_deformations_are_not_silent_retuning(self):
        self.assertEqual(len(self.report["deformations"]), 5)
        for row in self.report["deformations"][1:]:
            self.assertGreater(row["max_low_occupation_change"], 0)
            self.assertLess(row["max_low_occupation_change"], 1e-3)
        self.assertFalse(self.report["universality_proved"])
        self.assertFalse(self.report["spatial_continuum_tested"])


if __name__ == "__main__":
    unittest.main()
