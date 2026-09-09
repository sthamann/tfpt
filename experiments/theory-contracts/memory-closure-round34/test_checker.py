"""Independent block-power, full-vector, source and provenance regressions."""
import importlib.util
import inspect
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("memory_round34", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def dense_product(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def dense_powers_on_vector(H, initial, degree):
    vectors = [[int(i == initial) for i in range(len(H))]]
    for _ in range(degree):
        vectors.append([sum(a*b for a, b in zip(row, vectors[-1])) for row in H])
    return vectors


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = r.inherited(ROOT)
        cls.cycles = {K: r.compile_cycle(str(ROOT), K) for K in (8, 12)}
        cls.solutions = {K: r.solve_cycle(str(ROOT), K) for K in (8, 12)}

    def test_minimum_degree_compiles_only_available_moments(self):
        c = r.compile_cycle.__wrapped__(str(ROOT), 1, 2)
        self.assertEqual(len(c["kernels"]), 1)
        self.assertEqual(len(c["source_maps"]), 2)
        b = c["blocks"]
        jets = r.low_jets(b["L"], c["kernels"], b["initial_low"], 2)
        actual = r.assemble_readout(c, r.source_readout_vectors(jets, c["source_maps"]))
        expected = self.parent.rational_evolution(c["rows"], c["initial"], 2)
        self.assertEqual(actual, expected[:3])

    def test_parent_split_is_exact_and_preparation_unchanged(self):
        for K, c in self.cycles.items():
            b = c["blocks"]
            self.assertEqual(len(b["low_indices"]), 2*K+1)
            self.assertEqual(len(b["high_indices"]), 38*K+7)
            self.assertEqual(c["basis"][c["initial"]], (7, 0))
            self.assertEqual(c["center"], 6)
            self.assertTrue(all(c["basis"][i][0] == 7 for i in b["low_indices"]))
            self.assertTrue(all(c["basis"][i][0] != 7 for i in b["high_indices"]))
            for i, original_i in enumerate(b["high_indices"]):
                for j, original_j in enumerate(b["low_indices"]):
                    self.assertEqual(b["C"][i][j], c["rows"][original_i].get(original_j, 0))

    def test_retained_block_has_only_electric_and_constant_energy(self):
        c = self.cycles[12]
        for j, original in enumerate(c["blocks"]["low_indices"]):
            _, k = c["basis"][original]
            physical = F(c["blocks"]["L"][j][j], r.DEN)+c["center"]
            self.assertEqual(physical, F(3*k*k, 200)+F(1, 96))

    def test_kernel_zero_positive_diagonal_and_boundary_loss(self):
        for c in self.cycles.values():
            K0 = c["kernels"][0]
            for i, row in enumerate(K0):
                self.assertTrue(all(v == 0 for j, v in enumerate(row) if j != i))
                self.assertEqual(F(row[i], r.DEN**2), F(1, 192) if i in (0, len(K0)-1) else F(1, 96))

    def test_first_memory_moment_keeps_signed_Wilson_return(self):
        for c in self.cycles.values():
            K1 = c["kernels"][1]
            for i in range(len(K1)-1):
                self.assertEqual(F(K1[i+1][i], r.DEN**3), -3*F(1, 2)**2*F(1, 12)**3)
                self.assertEqual(K1[i+1][i], K1[i][i+1])
            self.assertTrue(all(K1[i][j] == 0 for i in range(len(K1))
                                for j in range(len(K1)) if abs(i-j) > 1))

    def test_source_and_memory_moments_independently_recomputed(self):
        c = r.compile_cycle.__wrapped__(str(ROOT), 1, 6)
        b = c["blocks"]
        D = [[row.get(j, 0) for j in range(len(b["D"]))] for row in b["D"]]
        Ct = [list(row) for row in zip(*b["C"])]
        B = b["C"]
        for n in range(6):
            self.assertEqual(c["source_maps"][n], B)
            if n < 5:
                self.assertEqual(c["kernels"][n], dense_product(Ct, B))
            B = dense_product(D, B)

    def test_all_compiled_memory_moments_are_symmetric(self):
        for c in self.cycles.values():
            for K in c["kernels"]:
                self.assertEqual(K, [list(row) for row in zip(*K)])

    def test_closed_recurrence_on_nondiagonal_independent_toy(self):
        L, D, C = [[2, 1], [1, -1]], [[3, -2], [-2, 4]], [[1, 2], [0, -1]]
        Ct = [list(row) for row in zip(*C)]
        H = [L[i]+Ct[i] for i in range(2)]+[C[i]+D[i] for i in range(2)]
        B, sources, kernels = C, [], []
        for n in range(12):
            sources.append(B)
            if n < 11:
                kernels.append(dense_product(Ct, B))
            B = dense_product(D, B)
        rows = [{j: a for j, a in enumerate(row) if a} for row in L]
        for initial in (0, 1):
            full = dense_powers_on_vector(H, initial, 12)
            jets = r.low_jets(rows, kernels, initial, 12)
            self.assertEqual(jets, [v[:2] for v in full])
            pr, pi, qr, qi, den = r.source_readout_vectors(jets, sources)
            for i in range(4):
                self.assertEqual(F((pr+qr)[i], den), sum(F((-1)**(n//2)*full[n][i], r.DEN**n*factorial(n)) for n in range(0, 13, 2)))
                self.assertEqual(F((pi+qi)[i], den), sum(F((-1)**((n+1)//2)*full[n][i], r.DEN**n*factorial(n)) for n in range(1, 13, 2)))

    def test_entire_physical_vector_equals_independent_full_Horner(self):
        # The full-state solver is an independent TEST ORACLE, never an input.
        for K, c in self.cycles.items():
            actual = r.assemble_readout(c, self.solutions[K][1])
            expected = self.parent.rational_evolution(c["rows"], c["initial"], 80)
            self.assertEqual(actual, expected[:3])

    def test_evolution_without_full_solver_or_reference_file(self):
        c = self.cycles[8]
        with patch.object(self.parent, "rational_evolution", side_effect=RuntimeError("forbidden full solver")), \
             patch.object(Path, "read_text", side_effect=RuntimeError("forbidden reference file")):
            b = c["blocks"]
            jets = r.low_jets(b["L"], c["kernels"], b["initial_low"], 80)
            actual = r.source_readout_vectors(jets, c["source_maps"])
        self.assertEqual((jets, actual), self.solutions[8])

    def test_low_evolution_interface_contains_no_eliminated_blocks(self):
        self.assertEqual(list(inspect.signature(r.low_jets).parameters), ["L", "kernels", "initial", "degree"])
        source = inspect.getsource(r.low_jets)
        for forbidden in ("rational_evolution", "read_text", "source_maps", "compile_cycle", 'blocks["D"]'):
            self.assertNotIn(forbidden, source)

    def test_omitting_memory_changes_second_derivative(self):
        c = self.cycles[8]
        b = c["blocks"]
        np = len(b["L"])
        with_memory = r.low_jets(b["L"], c["kernels"], b["initial_low"], 2)
        without_memory = r.low_jets(b["L"], [[[0]*np for _ in range(np)]], b["initial_low"], 2)
        delta = [a-b for a, b in zip(with_memory[2], without_memory[2])]
        self.assertEqual(delta, [row[b["initial_low"]] for row in c["kernels"][0]])
        self.assertNotEqual(with_memory[2], without_memory[2])

    def test_omitting_first_nonlocal_memory_changes_third_jet(self):
        c = self.cycles[8]
        b, kernels = c["blocks"], c["kernels"][:2]
        np = len(b["L"])
        actual = r.low_jets(b["L"], kernels, b["initial_low"], 3)
        mutant = r.low_jets(b["L"], [kernels[0], [[0]*np for _ in range(np)]], b["initial_low"], 3)
        self.assertEqual(actual[:3], mutant[:3])
        self.assertNotEqual(actual[3], mutant[3])

    def test_source_omission_is_not_a_valid_readout(self):
        c = r.compile_cycle.__wrapped__(str(ROOT), 1, 4)
        b = c["blocks"]
        jets = r.low_jets(b["L"], c["kernels"], b["initial_low"], 4)
        actual = r.source_readout_vectors(jets, c["source_maps"])
        zeros = [[[0]*len(b["L"]) for _ in b["D"]] for _ in range(4)]
        mutant = r.source_readout_vectors(jets, zeros)
        self.assertEqual(actual[:2], mutant[:2])
        self.assertNotEqual(actual[2:4], mutant[2:4])
        self.assertTrue(all(v == 0 for part in mutant[2:4] for v in part))

    def test_initial_survival_curvature_rules_out_same_space_unitarity(self):
        c = self.cycles[12]
        jets = self.solutions[12][0]
        i = c["blocks"]["initial_low"]
        curvature = F(2*(sum(a*a for a in jets[1])-jets[2][i]), r.DEN**2)
        self.assertEqual(curvature, -F(1, 48))
        self.assertEqual(curvature, -2*F(c["kernels"][0][i][i], r.DEN**2))

    def test_integer_weights_match_exponential_series(self):
        for degree in (2, 7, 80):
            weights, den = r.polynomial_weights(degree)
            self.assertEqual(den, r.DEN**degree*factorial(degree))
            self.assertEqual([F(w, den) for w in weights], [F(1, r.DEN**n*factorial(n)) for n in range(degree+1)])

    def test_total_norm_certified_but_retained_norm_not_renormalized(self):
        for K, c in self.cycles.items():
            pr, pi, qr, qi, den = self.solutions[K][1]
            tail = c["radius"]**81/factorial(81)
            p2, q2 = [F(sum(a*a+b*b for a, b in zip(re, im)), den**2)
                      for re, im in ((pr, pi), (qr, qi))]
            self.assertLessEqual((1-tail)**2, p2+q2)
            self.assertLessEqual(p2+q2, (1+tail)**2)
            self.assertLess(p2, F("0.997844"))
            self.assertGreater(q2, F("0.002156"))

    def test_both_certificates_match_frozen_intervals(self):
        ref = json.loads((HERE.parent/"local-flux-dynamics-round33/validation.json").read_text())
        for row in ref["cycle_dynamics"]:
            got = r.certificate(ROOT, row["cutoff"])
            self.assertEqual(got["readouts_at_time_one"], row["readouts_at_time_one"])
            self.assertEqual(got["comparison_to_frozen_Round33_intervals"], "IDENTICAL")

    def test_all_four_readouts_need_eliminated_source_terms(self):
        row = r.certificate(ROOT, 12)
        for interval in row["full_minus_undressed_projected_readouts"].values():
            self.assertTrue(F(interval["lower"]) > 0 or F(interval["upper"]) < 0)
        self.assertGreater(F(row["full_minus_undressed_projected_readouts"]["Wilson_cycle_real"]["lower"]), F("0.0000858"))
        full = row["readouts_at_time_one"]["Wilson_cycle_real"]
        missing = row["full_minus_undressed_projected_readouts"]["Wilson_cycle_real"]
        self.assertGreater(F(full["lower"]), 0)
        self.assertLess(F(full["upper"])-F(missing["lower"]), 0)

    def test_full_rotor_tail_and_survival_enclosure(self):
        row = r.certificate(ROOT, 12)
        self.assertLessEqual(F(row["full_rotor_readout_error_upper"]), F(93081, 10**18))
        self.assertEqual(row["all_bare_low_survival"]["decimal_lower"], "0.99784311496210")
        self.assertEqual(row["all_bare_low_survival"]["decimal_upper"], "0.99784311496230")

    def test_cost_accounting_does_not_hide_eliminated_sector(self):
        row = r.certificate(ROOT, 12)
        self.assertEqual((row["retained_evolution_components"], row["eliminated_kernel_components"]), (25, 463))
        self.assertEqual(row["memory_integer_slots"], 79*25*25)
        self.assertEqual(row["source_integer_slots"], 80*463*25)
        self.assertTrue(row["high_components_reconstructed_at_readout"])
        self.assertFalse(row["independent_high_state_evolution_performed"])

    def test_memory_mean_square_bound_from_actual_source_norm(self):
        c = self.cycles[12]
        b = c["blocks"]
        norm2 = F(sum(row[b["initial_low"]]**2 for row in b["C"]), r.DEN**2)
        self.assertEqual(norm2, F(1, 96))
        bound = r.memory_persistence_bound(norm2, len(b["D"]))
        self.assertEqual(bound, F(1, 4267008))
        row = r.certificate(ROOT, 12)
        self.assertEqual(F(row["finite_cutoff_memory_mean_square_lower"]), bound)
        self.assertFalse(row["memory_decay_or_finite_history_window_proved"])

    def test_spectral_weight_bound_with_and_without_degeneracy(self):
        for weights in ([F(1, 288)]*3, [F(1, 192), F(1, 384), F(1, 384)]):
            bound = r.memory_persistence_bound(sum(weights), len(weights))
            mean_square = sum(w*w for w in weights)
            self.assertGreaterEqual(mean_square, bound)
            degenerate_mean_square = (weights[0]+weights[1])**2+weights[2]**2
            self.assertGreaterEqual(degenerate_mean_square, mean_square)
        for norm, size in ((F(0), 3), (F(1), 0), (F(1), 1.5)):
            with self.assertRaises(ValueError):
                r.memory_persistence_bound(norm, size)

    def test_invalid_degree_and_missing_moments_rejected(self):
        for degree in (-1, 1, 2.5):
            with self.assertRaises(ValueError):
                r.compile_cycle.__wrapped__(str(ROOT), 1, degree)
        with self.assertRaises(ValueError):
            r.low_jets([{0: 1}], [], 0, 2)
        with self.assertRaises(ValueError):
            r.low_jets([{0: 1}], [[[1]]], 1, 2)
        with self.assertRaises(ValueError):
            r.source_readout_vectors([[1], [1], [1]], [[[1]]])

    def test_pin_mutation_rejected_even_with_cached_solution(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round33 source pin"):
                r.certificate(ROOT, 12)

    def test_comparison_is_not_fitted_when_reference_changes(self):
        original_loads = json.loads
        def mutant_loads(raw):
            result = original_loads(raw)
            for row in result["cycle_dynamics"]:
                row["readouts_at_time_one"]["bare_high_site0"]["lower"] = "0"
            return result
        with patch.object(r.json, "loads", side_effect=mutant_loads):
            with self.assertRaisesRegex(ValueError, "reproduces all frozen readout intervals"):
                r.certificate(ROOT, 12)
        self.assertEqual(r.solve_cycle(str(ROOT), 12), self.solutions[12])

    def test_scope_stays_conditional_and_non_RH(self):
        row = r.run(ROOT)
        self.assertEqual(row["physical_gates_closed"], [])
        self.assertFalse(row["memoryless_low_Hamiltonian_proved"])
        self.assertIn("Not a uniform 3D", row["scope"])
        self.assertIn("unchanged bare-prepared cycle", row["scope"])

    def test_saved_replay_and_source_digests(self):
        saved = (HERE/"validation.json").read_text()
        self.assertEqual(saved, r.payload(ROOT))
        self.assertEqual(len(json.loads(saved)["artifact_sources"]), 4)


if __name__ == "__main__":
    unittest.main()
