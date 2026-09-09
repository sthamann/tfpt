"""Family-wide matrix, interference, provenance and standalone regressions."""
import copy
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("coherent_round36", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r35, cls.parent = r.inherited(ROOT)
        cls.c = r.build(str(ROOT))
        cls.model = r.model_payload(cls.c)
        cls.full = [cls.parent.rational_evolution(cls.c["rows"], seed, 80) for seed in cls.c["seeds"]]

    def full_responses(self, full=None):
        full = self.full if full is None else full
        result = {}
        for name in r.NAMES:
            O = self.r35.doubled_observable(self.parent, self.c["basis"], name)
            applied = [(r.matvec(O, col[0]), r.matvec(O, col[1])) for col in full]
            real, imag = [], []
            for a in full:
                real.append([F(r.dot(a[0], x)+r.dot(a[1], y), 2*a[2]*b[2]) for (x, y), b in zip(applied, full)])
                imag.append([F(r.dot(a[0], y)-r.dot(a[1], x), 2*a[2]*b[2]) for (x, y), b in zip(applied, full)])
            result[name] = real, imag
        return result

    def test_family_is_one_physical_Gauss_sector(self):
        c = self.c
        self.assertEqual(len(c["basis"]), 528)
        self.assertEqual([c["basis"][i] for i in c["seeds"]], [(7, -1), (7, 0), (7, 1)])
        for mask, k in [c["basis"][i] for i in c["seeds"]]:
            self.assertEqual(self.parent.gauss_flux(mask, k), (k, k, k))
            self.assertTrue(all(self.parent.occupation(mask, x) == 1 for x in range(3)))

    def test_whole_input_block_is_exactly_preserved(self):
        c = self.c
        for j, seed in enumerate(c["seeds"]):
            self.assertEqual(c["V"][j], [r.SCALE*int(i == seed) for i in range(528)])
            for i, v in enumerate(c["V"]):
                self.assertEqual(r.dot(v, c["V"][j]), int(i == j)*r.SCALE**2)

    def test_all_input_energies_are_uniformly_bounded(self):
        c = self.c
        energies = [F(c["rows"][i][i], r.DEN)+c["center"] for i in c["seeds"]]
        self.assertEqual(energies, [F(61, 2400), F(1, 96), F(61, 2400)])
        for i in c["seeds"]:
            self.assertTrue(all(c["rows"][i].get(j, 0) == 0 for j in c["seeds"] if i != j))

    def test_near_isometry_verified_by_exact_gram(self):
        V = self.c["V"]
        gram = [[r.dot(v, w) for w in V] for v in V]
        actual = F(max(sum(abs(a-int(i == j)*r.SCALE**2) for j, a in enumerate(row)) for i, row in enumerate(gram)), r.SCALE**2)
        self.assertEqual(actual, self.c["gram_error"])
        self.assertLess(actual, F(8, 10**29))

    def test_shared_generator_is_not_three_independent_seed_chains(self):
        c = self.c
        self.assertEqual(len(c["A"]), 60)
        self.assertTrue(any(a and i % 3 != j % 3 for i, row in enumerate(c["A"]) for j, a in row.items()))
        for i, row in enumerate(c["A"]):
            for j, a in row.items():
                self.assertEqual(c["A"][j].get(i), a)
                self.assertLessEqual(abs(c["labels"][i]-c["labels"][j]), 1)

    def test_basis_proposal_precision_is_not_the_certificate(self):
        rows = [{0: 1, 3: 2}, {1: 2, 4: 3}, {2: 3, 5: 4}, {0: 2, 3: 4}, {1: 3, 4: 5}, {2: 4, 5: 6}]
        a = r.propose_block_basis(rows, [0, 1, 2], 2, precision=60)
        b = r.propose_block_basis(rows, [0, 1, 2], 2, precision=90)
        self.assertEqual(a, b)
        A, defects, g = r.certify_model(rows, a[0], a[1], [0, 1, 2], self.r35)
        self.assertEqual(g, 0)
        self.assertLess(sum(defects), F(1, 10**25))

    def test_bad_basis_proposal_fails_exact_gram_check(self):
        V = copy.deepcopy(self.c["V"])
        V[3] = V[4].copy()
        with self.assertRaisesRegex(ValueError, "near-isometry"):
            r.certify_model(self.c["rows"], V, self.c["labels"], self.c["seeds"], self.r35)

    def test_family_defect_is_euclidean_combination_not_single_seed_bound(self):
        squares = sum(a*a for a in self.c["column_bounds"])
        self.assertGreaterEqual(self.c["delta"]**2, squares)
        self.assertGreater(self.c["delta"], max(self.c["column_bounds"]))
        self.assertLess(self.c["delta"], F(1051, 10**21))

    def test_operator_input_error_against_all_full_columns(self):
        c = self.c
        total_squared = F(0)
        for (ar, ai), full in zip(c["states"], self.full):
            br, bi, bd, _, _ = full
            ad = c["denominator"]
            re = [sum(v[i]*a for v, a in zip(c["V"], ar))*bd-br[i]*ad*r.SCALE for i in range(528)]
            im = [sum(v[i]*a for v, a in zip(c["V"], ai))*bd-bi[i]*ad*r.SCALE for i in range(528)]
            total_squared += F(r.dot(re, re)+r.dot(im, im), (ad*r.SCALE*bd)**2)
        # Independent Frobenius bound also implies an operator bound for ALL c.
        # Frobenius tails get a conservative factor 3; the analytic operator
        # remainder on the isometric input block itself needs no such factor.
        upper = c["delta"]+3*(1+c["gram_error"])*c["taylor_tail"]+3*self.full[0][3]
        self.assertLessEqual(total_squared, upper**2)

    def test_full_complex_response_matrices_are_independently_reproduced(self):
        full = self.full_responses()
        for name in r.NAMES:
            real, imag = self.c["response"][name]
            fr, fi = full[name]
            row_bound = max(sum(abs(real[i][j]-fr[i][j])+abs(imag[i][j]-fi[i][j]) for j in range(3)) for i in range(3))
            self.assertLess(row_bound, self.c["error"])

    def test_response_matrices_are_hermitian(self):
        for real, imag in self.c["response"].values():
            self.assertTrue(all(real[i][j] == real[j][i] and imag[i][j] == -imag[j][i] for i in range(3) for j in range(3)))

    def test_coherent_and_incoherent_states_are_not_confused(self):
        densities = r.named_densities()
        O = self.c["response"]["Wilson_cycle_real"]
        plus = r.read_density(O, densities["coherent_plus"])
        mixed = r.read_density(O, densities["incoherent_equal"])
        self.assertGreater(plus-mixed-2*self.c["error"], F(4999, 10000))
        self.assertGreater(plus, F(4999, 10000))
        self.assertLess(mixed, F(22, 10**8))

    def test_imaginary_coherence_is_not_discarded(self):
        densities = r.named_densities()
        O = self.c["response"]["Wilson_cycle_real"]
        a = r.read_density(O, densities["phase_plus"])
        b = r.read_density(O, densities["phase_minus"])
        self.assertGreater(abs(a-b), F(1499, 100000))
        self.assertGreater(abs(O[1][1][2]), F(7499, 10**6))

    def test_phase_readout_against_explicit_full_superposition(self):
        # psi=(|k=0>+i|k=1>)/sqrt(2), no density-matrix helper as oracle.
        b, c = self.full[1], self.full[2]
        self.assertEqual(b[2], c[2])
        re, im = [a-y for a, y in zip(b[0], c[1])], [x+z for x, z in zip(b[1], c[0])]
        rho = r.named_densities()["phase_plus"]
        for name in r.NAMES:
            full_value = self.parent.expectation(self.c["basis"], re, im, b[2], name)/2
            reduced = r.read_density(self.c["response"][name], rho)
            self.assertLess(abs(full_value-reduced), self.c["error"])

    def test_global_phase_invariance_of_density(self):
        ray = [(1, 2), (-3, 1), (2, -1)]
        self.assertEqual(r.pure_density(ray), r.pure_density([(-b, a) for a, b in ray]))

    def test_mixtures_are_linear_with_one_fixed_response(self):
        a, b = r.named_densities()["coherent_plus"], r.named_densities()["phase_minus"]
        mixed = tuple([[(a[k][i][j]+2*b[k][i][j])/3 for j in range(3)] for i in range(3)] for k in range(2))
        for response in self.c["response"].values():
            self.assertEqual(r.read_density(response, mixed), (r.read_density(response, a)+2*r.read_density(response, b))/3)

    def test_density_principal_minors_include_determinant(self):
        bad = ([[F(1, 3) if i == j else -F(1, 3) for j in range(3)] for i in range(3)], [[F(0)]*3 for _ in range(3)])
        with self.assertRaisesRegex(ValueError, "determinant"):
            r.validate_density(bad)
        for rho in r.named_densities().values():
            r.validate_density(rho)

    def test_invalid_density_shape_trace_and_hermiticity(self):
        with self.assertRaises(ValueError):
            r.validate_density(([[1]], [[0]]))
        bad = copy.deepcopy(r.named_densities()["basis_zero"])
        bad[0][1][1] = 2
        with self.assertRaisesRegex(ValueError, "trace"):
            r.validate_density(bad)
        bad = copy.deepcopy(r.named_densities()["basis_zero"])
        bad[1][0][1] = 1
        with self.assertRaisesRegex(ValueError, "Hermitian"):
            r.validate_density(bad)

    def test_initial_response_matches_full_input_compression(self):
        response, _ = r.solve_compiled(self.model, time=0)
        Wreal, Wimag = response["Wilson_cycle_real"]
        self.assertEqual(Wreal, [[F(0), F(1, 2), F(0)], [F(1, 2), F(0), F(1, 2)], [F(0), F(1, 2), F(0)]])
        self.assertEqual(Wimag, [[0]*3 for _ in range(3)])
        self.assertEqual(response["electric_zero_link0"][0], [[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    def test_full_rotor_bound_uses_distance_from_largest_initial_flux(self):
        c = self.c
        proper = 4*self.parent.dyson_tail(12)
        wrong_zero_flux_bound = 4*self.parent.dyson_tail(13)
        self.assertGreater(proper, wrong_zero_flux_bound)
        self.assertGreater(c["error"], proper)
        self.assertEqual(c["cutoff"]-max(map(abs, r.SEEDS)), 12)

    def test_cutoff_prefix_matches_from_nonzero_flux(self):
        b1, H1, _, _ = self.parent.physical_cycle(2)
        b2, H2, _, _ = self.parent.physical_cycle(4)
        for seed in (-1, 1):
            v1 = [int(x == (7, seed)) for x in b1]
            v2 = [int(x == (7, seed)) for x in b2]
            for _ in range(2):  # K-max|k|=1, not K=2.
                self.assertEqual({k: v for k, v in zip(b1, v1) if v}, {k: v for k, v in zip(b2, v2) if v})
                v1, v2 = r.matvec(H1, v1), r.matvec(H2, v2)

    def test_standalone_uses_only_common_reduced_generator(self):
        matvec = r.matvec
        def restricted(rows, v):
            self.assertEqual(len(rows), 60)
            return matvec(rows, v)
        with patch.object(r, "inherited", side_effect=RuntimeError("parent forbidden")), \
             patch.object(r, "matvec", side_effect=restricted):
            response, error = r.solve_compiled(self.model)
        self.assertEqual(response, self.c["response"])
        self.assertLess(error, F(9309, 10**17))

    def test_no_basis_parent_or_reference_in_compiled_model(self):
        for name in ("V", "basis", "rows", "response", "reference", "seeds", "kernels"):
            self.assertNotIn(name, self.model)
        self.assertEqual(self.model["dimension"], 60)
        self.assertEqual(self.model["input_count"], 3)

    def test_no_fit_to_previous_zero_flux_readouts(self):
        old = json.loads((HERE.parent/"auxiliary-dynamics-round35/validation.json").read_text())
        expected = next(row for row in old["certificates"] if row["dimension"] == 20)["readouts_at_time_one"]
        actual = r.readout_record(self.c["response"], self.c["error"], r.named_densities()["basis_zero"])
        self.assertEqual(actual, expected)

    def test_domain_mutants_rejected(self):
        for t in (-1, F(1001, 1000)):
            with self.assertRaises(ValueError):
                r.solve_compiled(self.model, time=t)
        bad = copy.deepcopy(self.model)
        bad["initial_max_absolute_flux"] = 0
        with self.assertRaises(ValueError):
            r.solve_compiled(bad)
        bad = copy.deepcopy(self.model)
        bad["input_fluxes"] = [0, 1, 2]
        with self.assertRaises(ValueError):
            r.solve_compiled(bad)

    def test_pin_mutation_rejected_on_cached_build(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round35 source pin"):
                r.certificate(ROOT)

    def test_scope_and_dimension_scan(self):
        result = r.run(ROOT)
        self.assertEqual(result["physical_gates_closed"], [])
        self.assertFalse(result["uniform_3D_or_spectral_low_energy_theory_proved"])
        self.assertEqual([row["dimension"] for row in result["certificates"]], [36, 48, 60])
        for row in result["certificates"]:
            self.assertTrue(row["uniform_over_all_pure_and_mixed_family_states"])

    def test_exact_replay_and_standalone_without_repo(self):
        self.assertEqual((HERE/"validation.json").read_text(), r.payload(ROOT))
        self.assertEqual((HERE/"compiled_model.json").read_text(), json.dumps(self.model, indent=2, sort_keys=True)+"\n")
        result = subprocess.run([sys.executable, "-B", str(HERE/"checker.py"), "--repo", "/nonexistent-tfpt-repo",
                                 "--model", str(HERE/"compiled_model.json"), "--state", "phase_plus"], capture_output=True, text=True, check=True)
        out = json.loads(result.stdout)
        expected = r.readout_record(self.c["response"], self.c["error"], r.named_densities()["phase_plus"])
        self.assertEqual(out["readouts"], expected)
        self.assertFalse(out["parent_or_full_state_reconstruction_used"])


if __name__ == "__main__":
    unittest.main()
