"""Independent arithmetic, dynamics, standalone and scope regressions."""
import copy
import importlib.util
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("auxiliary_round35", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = r.inherited(ROOT)
        cls.models = {m: r.build(str(ROOT), 12, m) for m in (12, 16, 20)}
        cls.c = cls.models[20]
        cls.compiled = r.model_payload(cls.c)

    def test_integer_vectors_are_pairwise_orthogonal(self):
        vectors, norms = self.c["vectors"], self.c["norms"]
        for i, v in enumerate(vectors):
            for j, w in enumerate(vectors):
                self.assertEqual(sum(a*b for a, b in zip(v, w)), norms[i] if i == j else 0)

    def test_unchanged_preparation_and_high_auxiliary_mode(self):
        c = self.c
        self.assertEqual(c["basis"][c["initial"]], (7, 0))
        self.assertEqual(c["V"][0], [r.SCALE*int(i == c["initial"]) for i in range(488)])
        high = [i for i, (mask, _) in enumerate(c["basis"]) if mask != 7]
        self.assertEqual(sum(c["vectors"][1][i]**2 for i in high), c["norms"][1])
        self.assertGreater(c["norms"][1], 0)

    def test_small_known_tridiagonal_chain_has_exact_basis(self):
        H = [{0: 2, 1: 3}, {0: 3, 1: -1, 2: 4}, {1: 4, 2: 5}]
        vectors, norms, _ = r.primitive_lanczos(H, 0, 3)
        self.assertEqual(vectors, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(norms, [1, 1, 1])

    def test_basis_matches_independent_gram_schmidt_powers(self):
        import sympy as s
        H = s.Matrix([[1, 2, 0, 1], [2, -3, 1, 0], [0, 1, 4, 2], [1, 0, 2, 0]])
        rows = [{j: int(H[i, j]) for j in range(4) if H[i, j]} for i in range(4)]
        vectors, _, _ = r.primitive_lanczos(rows, 0, 4)
        powers = [H**k*s.eye(4)[:, 0] for k in range(4)]
        orthogonal = s.GramSchmidt(powers)
        for v, w in zip(vectors, orthogonal):
            nonzero = next(i for i, x in enumerate(v) if x)
            self.assertEqual(s.Matrix(v)*w[nonzero], w*v[nonzero])

    def test_rounding_normalized_vectors_is_exactly_enclosed(self):
        for integer_vector, norm, rounded in zip(self.c["vectors"], self.c["norms"], self.c["V"]):
            for x, q in zip(integer_vector, rounded):
                self.assertLessEqual(q*q*norm, x*x*r.SCALE**2)
                self.assertLess(x*x*r.SCALE**2, (abs(q)+1)**2*norm)
                self.assertGreaterEqual(x*q, 0)

    def test_square_root_rounding_on_rational_and_exact_values(self):
        for value in (F(0), F(1, 4), F(2), F(7, 13), F(1, 10**90)):
            upper = r.sqrt_upper(value, 10**50)
            self.assertGreaterEqual(upper**2, value)
            self.assertLess(max(F(0), upper-F(1, 10**50))**2, value) if value else self.assertEqual(upper, 0)
        self.assertEqual(r.ratio_sqrt_floor(3, 4, 100), 150)
        self.assertEqual(r.ratio_sqrt_floor(-3, 4, 100), -150)

    def test_reduced_generator_is_hermitian_tridiagonal(self):
        A = self.c["A"]
        self.assertEqual(sum(len(row) for row in A), 58)
        for i, row in enumerate(A):
            for j, a in row.items():
                self.assertEqual(A[j].get(i), a)
                self.assertLessEqual(abs(i-j), 1)
                if i != j:
                    self.assertGreater(a, 0)

    def test_first_hopping_reproduces_actual_departure_strength(self):
        a = F(self.c["A"][0][1], r.SCALE)
        self.assertLessEqual(a*a, F(1, 96))
        self.assertGreater((a+F(1, r.SCALE))**2, F(1, 96))

    def test_initial_moments_are_matched_with_rounding_bounds(self):
        c = self.c
        H0 = F(c["rows"][c["initial"]][c["initial"]], r.DEN)
        h2 = F(sum(a*a for a in c["rows"][c["initial"]].values()), r.DEN**2)
        A0 = F(c["A"][0][0], r.SCALE)
        a2 = sum(F(a, r.SCALE)**2 for a in c["A"][0].values())
        self.assertLessEqual(abs(H0-A0), F(1, r.SCALE))
        self.assertLess(abs(h2-a2), F(20, r.SCALE))

    def test_defect_is_not_assumed_small_in_operator_norm(self):
        self.assertGreater(self.c["defects"][-1], 3)
        self.assertLess(sum(self.c["defects"][:-1]), F(5, 10**28))
        self.assertLess(self.c["defect_error"], F(332, 10**21))
        self.assertLess(self.c["arrival"], F(95, 10**21))

    def test_positive_path_sum_starts_at_chain_distance(self):
        A = self.c["A"]
        B = [{j: abs(a) for j, a in row.items() if j != i} for i, row in enumerate(A)]
        v = [1]+[0]*19
        for n in range(20):
            self.assertEqual(v[-1], 0) if n < 19 else self.assertGreater(v[-1], 0)
            v = r.matvec(B, v)

    def test_arrival_bound_against_independent_two_state_series(self):
        A = [{0: 100, 1: 1}, {0: 1, 1: -100}]
        upper, radius, tail = r.integrated_arrival(A, degree=20, scale=1)
        partial = sum(F(1, factorial(n+1)) for n in range(1, 50, 2))
        self.assertEqual(radius, 1)
        self.assertGreater(upper, partial)
        self.assertGreater(tail, 0)

    def test_taylor_vector_against_independent_sine_cosine(self):
        A = [{1: 1}, {0: 1}]
        re, im, den, _, _ = r.unitary_vector(A, degree=12, scale=1)
        self.assertEqual(F(re[0], den), sum(F((-1)**(n//2), factorial(n)) for n in range(0, 13, 2)))
        self.assertEqual(F(im[1], den), sum(F((-1)**((n+1)//2), factorial(n)) for n in range(1, 13, 2)))
        self.assertEqual((re[1], im[0]), (0, 0))

    def test_physical_observable_construction_matches_parent(self):
        c = self.c
        re = [(i % 7)-3 for i in range(len(c["basis"]))]
        im = [(i % 5)-2 for i in range(len(c["basis"]))]
        for name in r.NAMES:
            doubled = r.doubled_observable(self.parent, c["basis"], name)
            actual = F(r.dot(re, r.matvec(doubled, re))+r.dot(im, r.matvec(doubled, im)), 2*17**2)
            self.assertEqual(actual, self.parent.expectation(c["basis"], re, im, 17, name))

    def test_reduced_sources_equal_full_embedded_readouts(self):
        c = self.c
        a, b, denominator = c["state"][:3]
        re = [sum(v[i]*x for v, x in zip(c["V"], a)) for i in range(len(c["basis"]))]
        im = [sum(v[i]*x for v, x in zip(c["V"], b)) for i in range(len(c["basis"]))]
        for name in r.NAMES:
            expected = self.parent.expectation(c["basis"], re, im, denominator*r.SCALE, name)
            self.assertEqual(c["values"][name], expected)

    def test_vector_defect_bound_against_independent_full_evolution(self):
        c = self.c
        ar, ai, ad, atail = c["state"][:4]
        br, bi, bd, btail, _ = self.parent.rational_evolution(c["rows"], c["initial"], 80)
        denominator = ad*r.SCALE*bd
        rr = [sum(v[i]*x for v, x in zip(c["V"], ar))*bd-br[i]*ad*r.SCALE for i in range(len(br))]
        ri = [sum(v[i]*x for v, x in zip(c["V"], ai))*bd-bi[i]*ad*r.SCALE for i in range(len(bi))]
        squared = F(r.dot(rr, rr)+r.dot(ri, ri), denominator**2)
        upper = c["defect_error"]+(1+c["embedding_error"])*atail+btail
        self.assertLessEqual(squared, upper**2)

    def test_standalone_uses_only_twenty_dimensional_matrices(self):
        original = r.matvec
        def checked(rows, vector):
            self.assertEqual(len(rows), 20)
            return original(rows, vector)
        with patch.object(r, "inherited", side_effect=RuntimeError("parent forbidden")), \
             patch.object(Path, "read_bytes", side_effect=RuntimeError("parent bytes forbidden")), \
             patch.object(r, "matvec", side_effect=checked):
            answer = r.solve_compiled(self.compiled)
        self.assertEqual(answer["readouts"], self.c["intervals"])
        self.assertFalse(answer["parent_or_high_state_reconstruction_used"])

    def test_compiled_artifact_has_no_parent_basis_or_history(self):
        for forbidden in ("rows", "basis", "V", "vectors", "kernels", "source_maps", "reference_values"):
            self.assertNotIn(forbidden, self.compiled)
        self.assertEqual(self.compiled["dimension"], 20)
        self.assertEqual(sum(len(O)**2 for O in self.compiled["source_numerators"].values()), 1600)

    def test_frozen_intervals_match_at_twenty_states_only_in_declared_scan(self):
        for m in (12, 16, 20):
            row = r.certificate(ROOT, m)
            expected = "IDENTICAL" if m == 20 else "OVERLAPPING_WIDER_BOUNDS"
            self.assertEqual(row["comparison_to_frozen_intervals"], expected)
        # This does not claim that 20 is a minimal dimension among all methods.

    def test_source_omission_mutant_destroys_physical_high_readout(self):
        model = copy.deepcopy(self.compiled)
        model["source_numerators"]["bare_high_site0"] = [["0"]*20 for _ in range(20)]
        answer = r.solve_compiled(model)
        self.assertLess(F(answer["readouts"]["bare_high_site0"]["upper"]), F(1, 10**10))
        self.assertGreater(F(self.c["intervals"]["bare_high_site0"]["lower"]), F("0.0007"))

    def test_hermitian_and_preparation_mutants_rejected(self):
        bad = copy.deepcopy(self.compiled)
        bad["hamiltonian_rows"][0]["1"] = "0"
        with self.assertRaisesRegex(ValueError, "Hermitian auxiliary"):
            r.solve_compiled(bad)
        bad = copy.deepcopy(self.compiled)
        bad["initial_auxiliary_index"] = 1
        with self.assertRaises(ValueError):
            r.solve_compiled(bad)

    def test_defect_check_detects_generator_mutation(self):
        A = copy.deepcopy(self.c["A"])
        A[0][0] += r.SCALE
        changed = r.defect_norms(self.c["rows"], self.c["V"], A)
        self.assertGreater(changed[0], F(99, 100))

    def test_time_zero_preserves_original_readouts(self):
        answer = r.solve_compiled(self.compiled, time=0)
        for name, expected in zip(r.NAMES, (0, 1, 0, 0)):
            x = answer["readouts"][name]
            self.assertLessEqual(F(x["lower"]), expected)
            self.assertLessEqual(expected, F(x["upper"]))

    def test_half_time_matches_independent_full_evolution(self):
        answer = r.solve_compiled(self.compiled, time=F(1, 2))
        c = self.c
        # Scale time through the common denominator; odd hopping numerators
        # must not be integer-divided and thereby change the physical parent.
        with patch.object(self.parent, "DEN", 2*r.DEN):
            re, im, den, tail, _ = self.parent.rational_evolution(c["rows"], c["initial"], 80)
        for name in r.NAMES:
            value = self.parent.expectation(c["basis"], re, im, den, name)
            interval = answer["readouts"][name]
            self.assertLessEqual(F(interval["lower"])-tail*(2+tail), value)
            self.assertLessEqual(value, F(interval["upper"])+tail*(2+tail))

    def test_invalid_domains_rejected(self):
        for time in (-1, F(1001, 1000)):
            with self.assertRaises(ValueError):
                r.solve_compiled(self.compiled, time)
        for dimension in (1, 2.5, 5):
            with self.assertRaises(ValueError):
                r.primitive_lanczos([{0: 1}, {1: 2}], 0, dimension)
        with self.assertRaises(ValueError):
            r.sqrt_upper(-1)
        with self.assertRaises(ValueError):
            r.integrated_arrival([{1: 10}, {0: 10}], degree=0, scale=1)

    def test_source_pin_mutation_fails_even_on_cached_build(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round34 source pin"):
                r.certificate(ROOT, 20)

    def test_scope_is_not_promoted_to_low_energy_or_TOE(self):
        result = r.run(ROOT)
        self.assertEqual(result["physical_gates_closed"], [])
        for row in result["certificates"]:
            self.assertFalse(row["low_energy_spectral_model"])
            self.assertTrue(row["retains_high_state_information"])
            self.assertTrue(row["initial_preparation_unchanged"])

    def test_artifacts_replay_and_standalone_without_repo(self):
        self.assertEqual((HERE/"validation.json").read_text(), r.payload(ROOT))
        model_text = json.dumps(self.compiled, indent=2, sort_keys=True)+"\n"
        self.assertEqual((HERE/"compiled_model.json").read_text(), model_text)
        process = subprocess.run([sys.executable, "-B", str(HERE/"checker.py"), "--repo", "/nonexistent-tfpt-parent",
                                  "--model", str(HERE/"compiled_model.json")], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(process.stdout)["readouts"], self.c["intervals"])


if __name__ == "__main__":
    unittest.main()
