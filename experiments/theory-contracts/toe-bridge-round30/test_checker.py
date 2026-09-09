"""Independent exact regressions and adversarial scope checks for Round30."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("toe_bridge_checker", HERE/"checker.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class Regression(unittest.TestCase):
    def test_original_signed_block_general_parameters(self):
        a, beta, eta, M = s.symbols("a beta eta M", real=True)
        h = s.Matrix([[a+beta*a*a, eta*a], [eta*a, M]])
        self.assertEqual(s.expand(h.det()-M*a*(1+(beta-eta**2/M)*a)), 0)
        D, R = s.symbols("D R", real=True)
        t = 2*eta*a/(R+D)
        numerator = s.together(eta*a*(1-t*t)-D*t).as_numer_denom()[0]
        self.assertEqual(s.rem(numerator, R*R-D*D-4*eta*eta*a*a, R), 0)

    def test_prescribed_rational_fixture_stays_inside_open_region(self):
        L, lam, g, delta = s.Integer(1), s.Integer(1), s.Integer(1), s.Rational(19, 12)
        M = delta+lam
        self.assertLess(L+lam*g*g*L*L, M)
        self.assertLess((lam*g*g-(lam*g)**2/M)*L, 1)
        z, A, V, h, diagonal = c.fixture()
        self.assertTrue(c.equal(c.star(V, z)*h*V, diagonal))
        self.assertEqual(h.subs(z, 1).eigenvals(), {0: 1, s.Rational(5, 4): 1,
                                                   s.Rational(31, 12): 1, s.Rational(10, 3): 1})

    def test_exterior_lift_is_functorial(self):
        A = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)], [-s.Rational(4, 5), s.Rational(3, 5)]])
        B = s.Matrix([[0, 1], [-1, 0]])
        self.assertEqual(c.exterior(A*B), c.exterior(A)*c.exterior(B))
        self.assertEqual(c.exterior(A).T*c.exterior(A), s.eye(4))

    def test_all_fermion_number_sectors_retained(self):
        z, _, V, _, _ = c.fixture()
        U = c.exterior(V.subs(z, 1))
        self.assertEqual(U.shape, (16, 16))
        for n in range(5):
            states = [j for j in range(16) if j.bit_count() == n]
            block = U.extract(states, states)
            self.assertEqual(block.T*block, s.eye(len(states)))

    def test_car_under_independent_exterior_rotation(self):
        z, _, V, _, _ = c.fixture()
        U = c.exterior(V.subs(z, 1))
        aa = c.car(4)
        dressed = [U.T*a*U for a in aa]
        for i, a in enumerate(dressed):
            for j, b in enumerate(dressed):
                self.assertEqual(a*b.T+b.T*a, s.eye(16) if i == j else s.zeros(16))
                self.assertEqual(a*b+b*a, s.zeros(16))

    def test_generic_noncommuting_operator_entry_counterexample_remains(self):
        swap = s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
        aa = c.car(2)
        b = sum((s.kronecker_product(swap[:2, 2*j:2*j+2], aa[j]) for j in range(2)), s.zeros(8))
        self.assertEqual(swap.T*swap, s.eye(4))
        self.assertNotEqual(b*b.T+b.T*b, s.eye(8))

    def test_full_rotor_derivative_for_independent_large_positive_negative_fluxes(self):
        z, _, V, _, _ = c.fixture()
        B = c.clean(c.star(V, z)*z*V.diff(z))
        vector = s.Matrix([1, 2, -1, 3])
        for k in [-29, -2, 0, 3, 37]:
            incoming = z**k*vector
            direct = c.clean(c.star(V, z)*z*(z*(V*incoming).diff(z)).diff(z))
            once = z*incoming.diff(z)+B*incoming
            transformed = c.clean(z*once.diff(z)+B*once)
            self.assertTrue(c.equal(direct, transformed))

    def test_gauss_covariance_is_a_differential_identity(self):
        z, _, V, _, _ = c.fixture()
        nx = s.diag(1, 0, 1, 0)
        ny = s.diag(0, 1, 0, 1)
        self.assertTrue(c.equal(z*V.diff(z)+nx*V-V*nx, s.zeros(4)))
        self.assertTrue(c.equal(-z*V.diff(z)+ny*V-V*ny, s.zeros(4)))
        # Reversing only the electric orientation breaks this identity.
        self.assertFalse(c.equal(-z*V.diff(z)+nx*V-V*nx, s.zeros(4)))

    def test_nonzero_positive_geometric_term_with_hamiltonian_coefficient(self):
        z, _, V, _, _ = c.fixture()
        B = c.clean(c.star(V, z)*z*V.diff(z))
        metric = c.clean(B[:2, 2:]*B[2:, :2])
        self.assertEqual(metric, 9*s.eye(2)/100)
        self.assertEqual(metric/2, 9*s.eye(2)/200)

    def test_two_particle_compression_keeps_born_huang_number_factor(self):
        z, _, V, _, _ = c.fixture()
        B = c.clean(c.star(V, z)*z*V.diff(z))
        many = c.dgamma(B, c.car(4))
        term = c.clean(many[:4, 4:]*many[4:, :4])
        self.assertEqual(term, s.diag(0, s.Rational(9, 100), s.Rational(9, 100), s.Rational(18, 100)))

    def test_gauss_constraints_are_not_arbitrary_flux_truncation(self):
        q = c.quantum_gauge()
        self.assertIsNone(q["rotor_flux_cutoff"])
        self.assertTrue(q["electric_identity_all_integer_flux"])
        one, two = q["Gauss_sectors"]
        self.assertEqual(one["dimension"], 4)
        self.assertEqual(two["dimension"], 6)
        self.assertEqual(one["omitted_connection_HS_squared"], "1/10")
        self.assertEqual(two["omitted_connection_HS_squared"], "9/50")
        self.assertEqual(set(two["fluxes_forced_by_Gauss"]), {-1, 0, 1})

    def test_majorana_residual_parity_from_actual_fock_lift(self):
        zeta = (1+s.I)/s.sqrt(2)
        charges = [1, 1, 2, 2, 3, 3]
        phases = [s.simplify(zeta**(-sum(charges[i] for i in range(6) if state & (1 << i)))) for state in range(64)]
        rotation = s.diag(*phases)
        K = s.simplify(rotation**4)
        self.assertEqual(s.simplify(rotation**8-s.eye(64)), s.zeros(64))
        self.assertEqual(K*K, s.eye(64))
        self.assertNotEqual(K, s.diag(*[(-1)**state.bit_count() for state in range(64)]))
        self.assertEqual(K[1 << 2, 1 << 2], 1)

    def test_controlled_low_sector_sturm_intervals(self):
        record = c.controlled_low_sector()
        self.assertEqual(record["low_energy_absolute_error_upper"], "27/13000000")
        error = s.Rational(record["low_energy_absolute_error_upper"])
        self.assertLess(error, s.Rational(21, 10**7))
        for actual, compressed in zip(record["full_energy_intervals"][:2], record["compressed_low_intervals"]):
            self.assertGreaterEqual(s.Rational(actual[0]), s.Rational(compressed[1])-error)
            self.assertLessEqual(s.Rational(actual[1]), s.Rational(compressed[0]))

    def test_feshbach_self_energy_has_exact_positive_upper_bound(self):
        z, _, V, h, _ = c.fixture()
        kappa = s.Rational(1, 100)
        full = V.subs(z, 1).T*(h.subs(z, 1)+kappa*s.diag(0, 1, 0, 1)/2)*V.subs(z, 1)
        coupling, high = full[2:, :2], full[2:, 2:]
        for energy in [0, 1, s.Rational(3, 2)]:
            sigma = coupling.T*(high-energy*s.eye(2)).inv()*coupling
            limit = 9*kappa*kappa/(400*(s.Rational(31, 12)-energy))
            self.assertTrue(sigma.is_positive_semidefinite)
            self.assertTrue((limit*s.eye(2)-sigma).is_positive_semidefinite)

    def test_low_sector_error_claim_rejects_undeclared_parameters(self):
        for invalid in [-1, 0, 1]:
            with self.assertRaisesRegex(ValueError, "controlled Gauss-sector electric parameter"):
                c.controlled_low_sector(invalid)

    def test_omitting_connection_changes_physical_spectrum_not_just_basis(self):
        z, _, _, h, diagonal = c.fixture()
        electric = s.diag(0, 1, 0, 1)/2
        exact = h.subs(z, 1)+electric
        wrong = diagonal.subs(z, 1)+electric
        self.assertEqual(s.trace(exact**4)-s.trace(wrong**4), -s.Rational(31, 64))
        self.assertEqual(s.expand(exact.charpoly().as_expr()-wrong.charpoly().as_expr()), s.Rational(31, 256))

    def test_seam_fourth_power_cannot_break_residual_parity(self):
        S = s.diag(1, s.I, -1, -s.I)
        one = s.diag(-1, 1, -1)
        self.assertEqual(S**4, s.eye(4))
        # Exhaust the basis of the entire seam matrix algebra, not a chosen polynomial list.
        for i in range(4):
            for j in range(4):
                matrix = s.zeros(4)
                matrix[i, j] = 1
                lifted = s.kronecker_product(matrix, s.eye(3))
                K = s.kronecker_product(s.eye(4), one)
                self.assertEqual(K*lifted, lifted*K)

    def test_exact_grade_table_and_forbidden_cells(self):
        report = c.flavor_state()
        table = {tuple(row["families"]): row["ordinary_seam_grades_allowed_by_rotation"]
                 for row in report["rotation_selection"]}
        self.assertEqual(table, {(1, 1): [1], (1, 2): [], (1, 3): [2],
                                 (2, 2): [2], (2, 3): [], (3, 3): [3]})
        self.assertFalse(report["full_texture_or_mass_scale_derived"])

    def test_existing_composite_is_spin_singlet_and_fermion_even(self):
        aa = c.car(6)
        B = aa[0]*aa[3]-aa[1]*aa[2]
        raising = sum((aa[2*i].T*aa[2*i+1] for i in range(3)), s.zeros(64))
        sz = sum((aa[2*i].T*aa[2*i]-aa[2*i+1].T*aa[2*i+1] for i in range(3)), s.zeros(64))/2
        self.assertEqual(raising*B-B*raising, s.zeros(64))
        self.assertEqual(raising.T*B-B*raising.T, s.zeros(64))
        self.assertEqual(sz*B-B*sz, s.zeros(64))
        parity = s.diag(*[(-1)**state.bit_count() for state in range(64)])
        self.assertEqual(parity*B, B*parity)

    def test_feshbach_reduction_preserves_residual_parity(self):
        # Low labels (-,+,-) and high labels (-,+): only matching K sectors couple.
        A = s.Matrix([[2, 0, 1], [0, 3, 0], [1, 0, 4]])
        B = s.Matrix([[1, 0], [0, 2], [3, 0]])
        D = s.diag(5, 7)
        z = s.symbols("energy")
        effective = A-B*(D-z*s.eye(2)).inv()*B.T
        P = s.diag(-1, 1, -1)
        self.assertEqual(P*effective*P, effective)
        mutant = B.copy()
        mutant[0, 1] = 1
        wrong = A-mutant*(D-z*s.eye(2)).inv()*mutant.T
        self.assertNotEqual(P*wrong*P, wrong)

    def test_unique_symmetric_ground_state_cannot_have_odd_condensate(self):
        K = s.diag(1, -1)
        B = s.Matrix([[0, 1], [1, 0]])
        H = s.diag(0, 2)
        vacuum = s.Matrix([1, 0])
        self.assertEqual(H*K, K*H)
        self.assertEqual(K*B*K, -B)
        self.assertEqual((vacuum.T*B*vacuum)[0], 0)
        mixed = s.Matrix([1, 1])
        self.assertEqual((mixed.T*B*mixed)[0]/2, 1)
        selected_cap = s.eye(2)-mixed*mixed.T/2
        self.assertNotEqual(selected_cap*K, K*selected_cap)

    def test_all_pinned_input_mutants_fail(self):
        original = Path.read_bytes
        for name in c.PINS:
            target = ROOT/name
            def changed(path, target=target):
                return original(path)+(b"\n# altered" if path == target else b"")
            with self.subTest(name=name), patch.object(Path, "read_bytes", changed):
                with self.assertRaisesRegex(ValueError, "pinned input missing or changed"):
                    c.run(ROOT)

    def test_saved_record_replays_and_hashes_all_research_sources(self):
        saved = json.loads((HERE/"validation.json").read_text())
        hashes = saved.pop("artifact_sources")
        self.assertEqual(set(hashes), {"checker.py", "QUANTUM_GAUGE.md", "FLAVOR_STATE.md", "README.md", "test_checker.py"})
        for name, expected in hashes.items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), expected)
        self.assertEqual(saved, c.run(ROOT))
        self.assertEqual(saved["physical_gates_closed"], [])


if __name__ == "__main__":
    unittest.main()
