from fractions import Fraction as F
from itertools import product
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

import checker as c


class HalfSectorTests(unittest.TestCase):
    def test_source_pins_and_fail_closed_mutation(self):
        c.validate_pins()
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.validate_pins()

    def test_exact_original_hopping_reflection(self):
        _, source = c.source()
        z = np.diag([1, -1])
        np.testing.assert_array_equal(z@source.TY.conj().T@z, source.TY)
        np.testing.assert_array_equal(z@source.SX@z, -source.SX)
        np.testing.assert_array_equal(z@source.SZ@z, source.SZ)
        m = np.kron(np.eye(8)[::-1], z)
        for p in (-2.1, -.4, 0., .7, 2.9):
            np.testing.assert_allclose(m@source.strip_at_momentum(p, 8)@m.conj().T,
                                       source.strip_at_momentum(-p, 8), atol=1e-15)

    def test_full_cylinder_spectral_equality_before_normal_ordering(self):
        _, source = c.source()
        for n in (16, 24, 32):
            first = np.linalg.eigvalsh(source.qwz_cylinder(n, 8, 1, 1))
            second = np.linalg.eigvalsh(source.qwz_cylinder(n, 8, 1, 3))
            self.assertEqual(sum(first < 0), 8*n)
            self.assertGreater(min(abs(first)), 0.)
            np.testing.assert_allclose(first, second, atol=2e-13, rtol=0)
            self.assertAlmostEqual(sum(first[first < 0]), sum(second[second < 0]), places=10)

    def test_source_profiles_both_sectors_edges_and_caps(self):
        for n, r, edge in product((16, 32, 128, 512), (1, 3), ("top", "bottom")):
            for label in (-c.cutoff(n), 0, c.cutoff(n)):
                s = c.strip(n, r, label, edge)
                h, rho, p, row = s["h"], s["rho"], s["p"], s["row"]
                sign = -1 if edge == "top" else 1
                self.assertLessEqual(np.linalg.norm((h-sign*np.sin(p)*np.eye(16))@s["q"]), rho**8+1e-13)
                self.assertLessEqual(np.linalg.norm(s["j"]-row), 4*rho+1e-12)
                self.assertAlmostEqual(np.linalg.norm(h@row), 2*abs(np.sin(p/2)), places=12)
                self.assertLessEqual(np.linalg.norm(n*h@s["j"]/(2*np.pi)-s["epsilon"]*s["j"]),
                                     n/(2*np.pi)*(2*rho**8+abs(p)**3/6)+1e-11)

    def test_full_filled_sea_not_only_a_selected_edge(self):
        for n, r in product((16, 32), (1, 3)):
            result = c.full_source(n, r)
            self.assertEqual(result["dimension"], 16*n)
            self.assertEqual(result["sea_rank"], 8*n)
            self.assertLess(result["polarization_error"], 1e-10)

    def test_integer_charge_minima_from_independent_filling(self):
        for r, edge, q in product((1, 3), ("top", "bottom"), range(-20, 21)):
            # Fill particles or holes in ascending physical excitation energy.
            top = edge == "top"
            positive = q >= 0
            low_labels = (top and positive) or (not top and not positive)
            labels = range(0, -abs(q), -1) if low_labels else range(1, abs(q)+1)
            direct = sum(abs(F(r, 4)-j) for j in labels)
            self.assertEqual(direct, c.edge_energy(r, q, edge))

    def test_arbitrary_finite_excitations_integer_oscillator_remainder(self):
        labels = (-2, -1, 0, 1, 2, 3)
        for r, edge, bits in product((1, 3), ("top", "bottom"), product((0, 1), repeat=6)):
            occupied = [j >= 1 if edge == "top" else j <= 0 for j in labels]
            charge = sum((-1 if occ else 1)*bit for occ, bit in zip(occupied, bits))
            energy = sum(abs(F(r, 4)-j)*bit for j, bit in zip(labels, bits))
            remainder = energy-c.edge_energy(r, charge, edge)
            self.assertGreaterEqual(remainder, 0)
            self.assertEqual(remainder.denominator, 1)

    def test_half_shift_energy_and_total_charge_dictionary(self):
        for b, qt, qb in product((0, 1), range(-9, 10), range(-9, 10)):
            pt, pb = c.charges(b, qt, qb)
            self.assertEqual(pt+pb, qt+qb)
            self.assertEqual(c.common_energy(pt, pb),
                             c.edge_energy(1+2*b, qt)+c.edge_energy(1+2*b, qb, "bottom"))
        self.assertEqual(c.common_energy(F(1,2), F(-1,2)), 0)
        # Dropping the opposite half shift is not the same charge dictionary.
        self.assertNotEqual(F(1,2)+0, 0)

    def test_covariance_difference_independent_rational_identity(self):
        u = sp.symbols("u", nonzero=True)  # u=exp(i*t/4)
        top = u/(1-u**4)-u**3/(1-u**4)
        bottom = u**(-3)/(1-u**(-4))-u**(-1)/(1-u**(-4))
        self.assertEqual(sp.cancel(top-u/(1+u*u)), 0)
        self.assertEqual(sp.cancel(bottom+u/(1+u*u)), 0)
        self.assertEqual(sp.limit(top, u, 1), F(1,2))
        self.assertEqual(sp.limit(bottom, u, 1), F(-1,2))

    def test_regulated_covariance_is_computed_from_the_full_source(self):
        car, model = c.source()
        n, z, t = 16, .7, .4
        for r in (1,3):
            h = model.qwz_cylinder(n, 8, 1, r)
            ev, v = np.linalg.eigh(h)
            p = v[:,ev<0]@v[:,ev<0].conj().T
            labels = range(-c.cutoff(n), c.cutoff(n)+1)
            weights = np.array([z**(abs(j)/2) for j in labels])
            for edge in ("top", "bottom"):
                columns = np.column_stack([np.kron(np.exp(2j*np.pi*(j-r/4)*np.arange(n)/n)/np.sqrt(n),
                                                   car.row_spinor(edge)) for j in labels])
                first = columns@weights
                second = columns@(weights*np.exp(1j*(np.array(list(labels))-r/4)*t))
                direct = np.vdot(first,p@second)
                self.assertLess(abs(direct-c.abel_covariance(n,r,edge,z,t)["value"]),1e-12)

    def test_regulated_covariance_cap_and_convergence(self):
        for r, edge, z, t in product((1,3), ("top", "bottom"), (.6,.8), (0.,.4,-.9)):
            rows = [c.abel_covariance(n,r,edge,z,t) for n in (64,256,1024)]
            for row in rows:
                self.assertLessEqual(row["absolute_error"], row["analytic_cap"]+1e-12)
            self.assertLess(rows[-1]["absolute_error"], rows[0]["absolute_error"])
            self.assertLess(rows[-1]["absolute_error"], .005)

    def test_coincidence_before_abel_limit_is_not_the_reference_charge(self):
        z, u = sp.symbols("z u")
        cutoff_top = z*(u-u**3)/(1-z*u**4)
        first_coincident = sp.limit(sp.limit(cutoff_top, u, 1), z, 1, dir="-")
        first_boundary = sp.limit(sp.limit(cutoff_top, z, 1, dir="-"), u, 1)
        self.assertEqual(first_coincident, 0)
        self.assertEqual(first_boundary, F(1,2))

    def test_carry_bijection_adjoint_charge_and_energy(self):
        for state in product((0, 1), range(-5, 6), range(-5, 6)):
            out = c.carry(*state)
            self.assertEqual(c.carry(*out, inverse=True), state)
            self.assertEqual(c.carry(*c.carry(*state, inverse=True)), state)
            p = c.charges(*state)
            op = c.charges(*out)
            self.assertEqual((op[0]-p[0], op[1]-p[1]), (F(1,2), F(-1,2)))
            self.assertEqual(c.common_energy(*op)-c.common_energy(*p), (p[0]-p[1])/2)
            self.assertEqual(c.carry(*out), (state[0], state[1]+1, state[2]-1))

    def test_noncyclic_carry_ladder_and_wrong_flip(self):
        state = (0, 0, 0)
        for n in range(16):
            self.assertEqual(c.common_energy(*c.charges(*state)), F(n*(n-1), 4))
            state = c.carry(*state)
        p = c.charges(1, 0, 0)
        wrong = c.charges(0, 0, 0)
        self.assertNotEqual(wrong[0]-p[0], F(1,2))

    def test_integer_source_charge_guard_is_not_weakened(self):
        car, _ = c.source()
        with self.assertRaisesRegex(ValueError, "integer charge"):
            car.charge_energy(F(1,2))
        with self.assertRaisesRegex(ValueError, "integer relative source charge"):
            c.edge_energy(3, F(1,2))
        for bad in (0, 2, 5, True):
            with self.assertRaises(ValueError):
                c.edge_energy(bad, 1)
        with self.assertRaisesRegex(ValueError, "common source window"):
            c.strip(16, 3, 2)

    def test_scope_flags_do_not_claim_an_intersector_field(self):
        with patch.object(c, "full_source", return_value={"diagnostic": "stubbed in scope-only test"}):
            record = c.record()
        for name in ("microscopic_local_half_charge_field", "physical_current_prescription_selected",
                     "microscopic_adiabatic_pump_proved", "opposite_edge_removed",
                     "eight_channel_E8_selection", "independent_mathematical_review"):
            self.assertIs(record[name], False)
        self.assertEqual(record["T1_T8_closed"], [])


if __name__ == "__main__":
    unittest.main()
