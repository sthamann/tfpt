import importlib.util
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import tempfile
import unittest

import numpy as np

import checker as c


class ChargedCARTests(unittest.TestCase):
    def test_01_source_pins_and_negative_control(self):
        c.validate_pins()
        # A structurally present but altered source must be rejected before import.
        with tempfile.TemporaryDirectory() as tmp:
            for name in c.PINS:
                path = Path(tmp) / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("altered source\n")
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.validate_pins(tmp)

    def test_02_full_source_window_guards(self):
        with self.assertRaises(ValueError):
            c.bounds(16, (3,))
        with self.assertRaises(ValueError):
            c.bounds(7, (0,))
        with self.assertRaises(ValueError):
            c.local_smearing(8, np.zeros(7))

    def test_03_actual_row_identity_and_all_caps(self):
        for n in (8, 16, 32, 128, 512):
            result = c.strip_diagnostic(n)
            self.assertEqual(len(result["modes"]), 3)

    def test_04_full_cylinder_not_replaced_by_small_model(self):
        for n in (8, 16, 32):
            row = c.full_source_diagnostic(n)
            self.assertEqual(row["dimension"], 16 * n)
            self.assertEqual(row["occupied_rank"], 8 * n)
            self.assertLess(row["polarization_error"], 1e-10)
            self.assertGreater(row["charged_creation_norm_squared"], .1)
            self.assertGreater(row["charged_annihilation_norm_squared"], .1)

    def test_05_raw_locality_is_exact(self):
        n = 64
        samples = np.zeros(n, complex)
        samples[9:21] = np.linspace(.1, .8, 12) + .3j
        vector = c.local_smearing(n, samples).reshape(n, 8, 2)
        self.assertEqual(np.count_nonzero(vector[:, :7]), 0)
        self.assertEqual(np.count_nonzero(vector[:9]), 0)
        self.assertEqual(np.count_nonzero(vector[21:]), 0)
        other = np.zeros(n, complex)
        other[35:43] = 1
        self.assertEqual(np.vdot(vector.ravel(), c.local_smearing(n, other)), 0)

    def test_06_original_holonomy_and_fourier_sampling(self):
        n = 32
        coefficients = {-1: .2 + .3j, 0: -.4j, 1: 1.}
        samples = sum(value * np.exp(2j * np.pi * j * np.arange(n) / n)
                      for j, value in coefficients.items())
        expected = sum(value * c.fourier_column(n, j) for j, value in coefficients.items())
        np.testing.assert_allclose(c.local_smearing(n, samples), expected, atol=1e-14)
        wrong = np.kron(samples / np.sqrt(n), c.row_spinor())
        self.assertGreater(np.linalg.norm(wrong - expected), .5)

    def test_07_generator_uniform_bound_all_labels_and_aliases(self):
        _, source = c.inherited()
        for n in (8, 32):
            for j in (-100, -n, -2, 0, 1, 3, n, 100):
                p = 2 * np.pi * (j - .25) / n
                value = n / (2 * np.pi) * np.linalg.norm(source.strip_at_momentum(p, 8) @ c.row_spinor())
                self.assertLessEqual(value, abs(j - .25) + 1e-12)

    def test_08_sampling_tail_does_not_assume_orthogonal_aliases(self):
        n = 16
        # j and j+N are identical sampled columns. An l2 tail would be false.
        columns = c.fourier_column(n, 1) + c.fourier_column(n, 1 + n)
        self.assertAlmostEqual(np.linalg.norm(columns), 2.)
        self.assertGreater(np.linalg.norm(columns), np.sqrt(2))

    def test_09_raw_vacuum_and_generator_rates_diagnostic(self):
        rows = [c.strip_diagnostic(n)["modes"][0] for n in (64, 128, 256)]
        for old, new in zip(rows, rows[1:]):
            self.assertLess(new["wrong_occupation"], .08 * old["wrong_occupation"])
            self.assertLess(new["raw_generator_error"], .51 * old["raw_generator_error"])
            self.assertLess(new["projected_generator_error"], .26 * old["projected_generator_error"])
        # Finite ratios ward the implementation, not the asymptotic proof.

    def test_10_time_and_adjoints_same_operator(self):
        data = c.strip(64, -1)
        values, vectors = np.linalg.eigh(64 * data["h"] / (2 * np.pi))
        row = c.row_spinor()
        for time in (-3., -.2, 0., 2.):
            unitary = (vectors * np.exp(1j * time * values)) @ vectors.conj().T
            rhs = np.exp(1j * time * c.energy(-1)) * row
            error = np.linalg.norm(unitary @ row - rhs)
            adjoint_error = np.linalg.norm(row.conj() @ unitary.conj().T - rhs.conj())
            self.assertAlmostEqual(error, adjoint_error)

    def test_11_opposite_edge_not_silently_dropped(self):
        n, j = 256, 1
        h = c.strip(n, j)["h"]
        bottom = c.row_spinor("bottom")
        wrong_chirality = np.linalg.norm(n * h @ bottom / (2 * np.pi) - c.energy(j) * bottom)
        opposite = np.linalg.norm(n * h @ bottom / (2 * np.pi) + c.energy(j) * bottom)
        self.assertGreater(wrong_chirality, 1.)
        self.assertLess(opposite, .02)

    def test_12_independent_CAR_and_exact_charge_ward(self):
        aa = c.annihilators(4)
        identity = np.eye(16)
        number = sum(a.conj().T @ a for a in aa)
        for i, a in enumerate(aa):
            np.testing.assert_array_equal(number @ a - a @ number, -a)
            np.testing.assert_array_equal(number @ a.conj().T - a.conj().T @ number, a.conj().T)
            for j, b in enumerate(aa):
                np.testing.assert_array_equal(a @ b + b @ a, np.zeros((16, 16)))
                np.testing.assert_array_equal(a @ b.conj().T + b.conj().T @ a,
                                              identity if i == j else np.zeros((16, 16)))

    def test_13_particle_hole_isometry_on_entire_small_Fock(self):
        labels = (-1, 0, 1, 2)
        aa = c.annihilators(4)
        occ = [j >= 1 for j in labels]
        vacuum = np.zeros(16, complex)
        vacuum[sum(int(value) << i for i, value in enumerate(occ))] = 1
        creators = [a if occupied else a.conj().T for a, occupied in zip(aa, occ)]
        isometry = np.zeros((16, 16), complex)
        for mask in range(16):
            column = vacuum.copy()
            for i in reversed(range(4)):
                if (mask >> i) & 1:
                    column = creators[i] @ column
            isometry[:, mask] = column
        np.testing.assert_array_equal(isometry.conj().T @ isometry, np.eye(16))
        for index, a in enumerate(aa):
            target = a.conj().T if occ[index] else a
            np.testing.assert_array_equal(a @ isometry, isometry @ target)
        ident = np.eye(16)
        physical_h = sum(c.energy(j) * (a.conj().T @ a - occupied * ident)
                         for j, a, occupied in zip(labels, aa, occ))
        target_h = sum(abs(c.energy(j)) * a.conj().T @ a for j, a in zip(labels, aa))
        physical_q = sum(a.conj().T @ a - occupied * ident for a, occupied in zip(aa, occ))
        target_q = sum((-1 if occupied else 1) * a.conj().T @ a for a, occupied in zip(aa, occ))
        np.testing.assert_array_equal(physical_h @ isometry, isometry @ target_h)
        np.testing.assert_array_equal(physical_q @ isometry, isometry @ target_q)

    def test_14_wrong_hole_charge_and_empty_vacuum_rejected(self):
        a = c.annihilators(1)[0]
        number = a.conj().T @ a
        hole_creator = a
        np.testing.assert_array_equal(number @ hole_creator - hole_creator @ number, -hole_creator)
        self.assertFalse(np.array_equal(number @ hole_creator - hole_creator @ number, hole_creator))
        full, empty = np.array([0., 1.]), np.array([1., 0.])
        self.assertEqual(np.linalg.norm(a @ full), 1.)
        self.assertEqual(np.linalg.norm(a @ empty), 0.)

    def test_15_full_source_finite_excitation_energy_residual(self):
        # Independent sparse exterior construction from original strip eigenmodes.
        # No small effective Hamiltonian is exponentiated in place of the source.
        n, labels = 32, (-1, 0, 1)
        energies, vectors = {}, []
        for block, label in enumerate(labels):
            item = c.strip(n, label)
            ev, v = np.linalg.eigh(n * item["h"] / (2 * np.pi))
            coeff = v.conj().T @ item["j"]
            choices = {}
            for index, e in enumerate(ev):
                if (e < 0) == (label >= 1):
                    mode = block * 16 + index
                    energies[mode] = abs(e)
                    choices[mode] = np.conj(coeff[index]) if label >= 1 else coeff[index]
            vectors.append(choices)
        worst = 0.
        for length in (1, 2, 3):
            for subset in combinations(range(3), length):
                state = {0: 1. + 0j}
                for index in reversed(subset):
                    output = {}
                    for mask, amplitude in state.items():
                        for mode, coefficient in vectors[index].items():
                            if not ((mask >> mode) & 1):
                                sign = (-1) ** ((mask & ((1 << mode) - 1)).bit_count())
                                target = mask | (1 << mode)
                                output[target] = output.get(target, 0j) + sign * coefficient * amplitude
                    state = output
                norm2 = sum(abs(value) ** 2 for value in state.values())
                self.assertAlmostEqual(norm2, 1., places=11)
                target_energy = sum(abs(c.energy(labels[index])) for index in subset)
                residual2 = 0.
                for mask, amplitude in state.items():
                    actual = sum(e for mode, e in energies.items() if (mask >> mode) & 1)
                    residual2 += abs(amplitude) ** 2 * (actual - target_energy) ** 2
                residual = np.sqrt(residual2)
                worst = max(worst, residual)
                cap = length * c.bounds(n, labels)["projected_generator_cap"]
                self.assertLessEqual(residual, cap + 1e-10)
        self.assertGreater(worst, 1e-4)

    def test_16_exact_integer_charge_energies_and_holonomy_offset(self):
        for q in range(-20, 21):
            labels = c.charge_vacuum_labels(q)
            exact = sum((abs(Fraction(1, 4) - j) for j in labels), Fraction(0))
            self.assertEqual(exact, c.charge_energy(q))
            self.assertEqual(c.charge_energy(q + 1) - c.charge_energy(q), Fraction(q) + Fraction(1, 4))
        self.assertEqual(c.charge_energy(1), Fraction(1, 4))
        self.assertEqual(c.charge_energy(-1), Fraction(3, 4))
        self.assertNotEqual(c.charge_energy(4), c.charge_energy(0))

    def test_17_charge_energy_minimum_in_top_edge_only(self):
        labels = tuple(range(-5, 0 + 1)) + tuple(range(1, 6))
        best = {}
        for mask in range(1 << len(labels)):
            charge, total = 0, Fraction(0)
            for index, j in enumerate(labels):
                if (mask >> index) & 1:
                    charge += 1 if j <= 0 else -1
                    total += abs(Fraction(1, 4) - j)
            best[charge] = min(best.get(charge, total), total)
        for q in range(-5, 6):
            self.assertEqual(best[q], c.charge_energy(q))

    def test_18_no_half_charge_relabel(self):
        # Number commutator has integer eigenvalues on every CAR matrix unit.
        count = 4
        eigencharges = {a.bit_count() - b.bit_count()
                       for a in range(1 << count) for b in range(1 << count)}
        self.assertNotIn(Fraction(1, 2), eigencharges)
        self.assertIn(1, eigencharges)

    def test_19_complex_timed_four_field_word_against_full_sea(self):
        labels = (-1, 0, 1)
        times = (-.2, .1, .4, .7)
        fs = [np.array(x, complex) for x in ((1, .3j, .2), (.2j, 1, .4),
                                            (.3, .2, 1j), (1j, -.2, .7))]
        fs = [f / np.linalg.norm(f) for f in fs]
        aa = c.annihilators(3)
        target_vectors = [f * np.exp(1j * t * np.array([c.energy(j) for j in labels]))
                          for f, t in zip(fs, times)]
        operators = [sum(np.conj(v) * a for v, a in zip(f, aa)) for f in target_vectors]
        omega = np.zeros(8, complex)
        omega[4] = 1
        target = np.vdot(omega, operators[0] @ operators[1].conj().T @ operators[2]
                         @ operators[3].conj().T @ omega)
        _, source = c.inherited()
        for n in (16, 32):
            ev, v = np.linalg.eigh(n * source.qwz_cylinder(n, 8, 1, 1) / (2 * np.pi))
            p = v[:, ev < 0] @ v[:, ev < 0].conj().T
            q = np.eye(len(ev)) - p
            raw = np.column_stack([c.fourier_column(n, j) for j in labels])
            polarized = np.column_stack([c.fourier_column(n, j, projected=True) for j in labels])
            ws = [(v * np.exp(1j * t * ev)) @ (v.conj().T @ (raw @ f))
                  for f, t in zip(fs, times)]
            # Full original Gaussian vacuum, Wick sign independently compared
            # with the explicitly multiplied target CAR matrices above.
            observed = (np.vdot(ws[0], q @ ws[1]) * np.vdot(ws[2], q @ ws[3])
                        + np.vdot(ws[0], q @ ws[3]) * np.vdot(ws[2], p @ ws[1]))
            telescope = sum(np.linalg.norm(w - polarized @ ft)
                            for w, ft in zip(ws, target_vectors))
            self.assertLessEqual(abs(observed - target), telescope + 1e-10)
            self.assertGreater(abs(observed - target), 1e-7)


if __name__ == "__main__":
    unittest.main()
