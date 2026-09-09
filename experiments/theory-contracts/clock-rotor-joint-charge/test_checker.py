"""Exact finite controls for a symbolic all-flux/local-lift proof."""
import itertools
import unittest
from unittest.mock import patch

import sympy as sp

import checker as c


class JointChargeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent, cls.edge = c.make_parent()

    def test_actual_clock_permutation_and_multiplicities(self):
        row = c.source_clock()
        self.assertEqual(row["annihilation_grades"], [0, 0, 0, 0, 0, 2, 3, 4])
        self.assertEqual(row["cycle_lengths"], [1, 1, 1, 2, 3])
        self.assertEqual(sorted(row["multiplicities"].values()), [1, 1, 1, 5])

    def test_all_7776_edge_assignments_give_exactly_36_gauge_lifts(self):
        expected = {(a, b, a, b, (b-a) % 6) for a, b in itertools.product(range(6), repeat=2)}
        self.assertEqual(set(c.one_edge_solutions(self.edge)), expected)
        self.assertEqual(len(self.edge["terms"]), 6)

    def test_different_L_H_clock_grades_break_an_actual_hopping(self):
        self.assertTrue(any(c.term_residues(self.edge, (0, 0, 3, 0), (0,))))
        self.assertTrue(any(c.term_residues(self.edge, (0, 0, 0, 0), (3,))))

    def test_full_two_step_list_is_preserved(self):
        _, data = c.make_parent((2, 2, 1))
        self.assertTrue(any(len(term[2]) == 2 for term in data["terms"]))
        for q in itertools.product(range(6), repeat=4):
            self.assertFalse(any(c.term_residues(data, *c.lifted_grades(data, q))))

    def test_polynomial_Gauss_identity_for_arbitrary_integer_flux(self):
        _, data = c.make_parent((2, 2, 1))
        symbolic_q = sp.symbols("q0:4", integer=True)
        self.assertEqual(c.gauge_identity(data, symbolic_q), 0)
        self.assertEqual(c.gauge_identity(self.edge, (10**12, -10**12+3)), 0)

    def test_full_H_actions_at_positive_negative_and_large_flux(self):
        self.assertGreater(c.exact_hamiltonian_control(self.parent, self.edge, (1, 4)), 80)

    def test_Gauss_physical_phase_is_scalar_but_kinematic_phase_need_not_be(self):
        matter, rotor = c.lifted_grades(self.edge, (1, 4))
        initial = {(3, (0,)): 1}
        states = dict(initial)
        for _ in range(4):
            for state in states:
                self.assertEqual(self.parent.gauss(self.edge, state), (0, 0))
                self.assertEqual(c.phase_exponent(self.edge, state, matter, rotor), 1)
            states = self.parent.apply_parent(self.edge, states)
        self.assertNotEqual(c.phase_exponent(self.edge, (0, (0,)), matter, rotor), 1)

    def test_noncontractible_torus_holonomy_is_also_zero(self):
        _, data = c.make_parent((3, 3, 3), periodic=True)
        q = [(5*i+2*i*i) % 6 for i in range(27)]
        matter, rotor = c.lifted_grades(data, q)
        self.assertFalse(any(c.term_residues(data, matter, rotor)))
        positions = {tuple(v): i for i, v in enumerate(data["vertices"])}
        for axis in range(3):
            cycle = []
            for j in range(3):
                v = [0, 0, 0]; v[axis] = j
                cycle.append(positions[tuple(v)])
            edges = list(zip(cycle, cycle[1:]+cycle[:1]))
            edge_positions = {edge: i for i, edge in enumerate(data["edges"])}
            self.assertEqual(sum(rotor[edge_positions[edge]] for edge in edges) % 6, 0)

    def test_onsite_U2_commutant_is_diagonal_and_doubled_spectrum(self):
        a, b, cc, d = sp.symbols("a b c d")
        matrix = sp.Matrix([[a, b], [cc, d]])
        for degree in range(7):
            low = sp.Rational(self.parent.BETA*self.parent.A**2*degree)
            high = sp.Rational(self.parent.MASS)
            comm = matrix*sp.diag(low, high)-sp.diag(low, high)*matrix
            self.assertEqual(sp.solve([comm[0, 1], comm[1, 0]], (b, cc)), {b: 0, cc: 0})
        # Basis-independent obstruction: every local scalar U(2) character is
        # repeated twice, so its characteristic polynomial must be a square.
        x = sp.Symbol("x")
        _, factors = sp.factor_list((x-1)**5*(x+1)*(x*x+x+1))
        self.assertTrue(any(multiplicity % 2 for _, multiplicity in factors))

    def test_source_pins_and_dimensions_are_guarded_under_OO(self):
        with patch.object(c, "PINS", {next(iter(c.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.inherited()
        with self.assertRaises(ValueError):
            c.term_residues(self.edge, (0,), (0,))


if __name__ == "__main__":
    unittest.main()
