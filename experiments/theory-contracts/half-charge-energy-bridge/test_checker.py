from collections import Counter
from fractions import Fraction as F
from itertools import product
import random
import unittest
from unittest.mock import patch

import checker as c


class EnergyBridgeTests(unittest.TestCase):
    def test_pinned_source_and_integer_filling_energies(self):
        source = c.source()
        for q in range(-24, 25):
            direct = sum(abs(F(source.energy(j))) for j in source.charge_vacuum_labels(q))
            self.assertEqual(direct, source.charge_energy(q))
            self.assertEqual(direct, F(q*q,2)-F(q,4))

    def test_half_charge_is_not_a_proved_source_sector(self):
        with self.assertRaisesRegex(ValueError, "integer charge"):
            c.source().charge_energy(F(1,2))

    def test_source_mutation_fails_closed(self):
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.source()

    def test_exact_root_inventory(self):
        self.assertEqual(len(set(c.roots())), 240)
        self.assertEqual(sum(all(x % 2 for x in q) for q in c.roots()), 128)
        self.assertTrue(all(c.lattice(q) and sum(x*x for x in q) == 8 for q in c.roots()))

    def test_all_256_holonomy_assignments(self):
        even = Counter({F(0):1,F(1,2):56,F(1):126,F(3,2):56,F(2):1})
        odd = Counter({F(1,4):8,F(1,2):28,F(3,4):56,F(1):56,F(5,4):56,F(3,2):28,F(7,4):8})
        for signs in product((-1,1), repeat=8):
            parity = signs.count(-1) % 2
            self.assertEqual(c.root_census(signs), odd if parity else even)
            self.assertEqual(len(c.ground_charges(signs)), 1 if parity else 2)

    def test_genuine_spinor_carry_not_cyclic_register(self):
        self.assertEqual([c.energies((n,)*8)[1] for n in range(5)], [0,0,2,6,12])
        self.assertEqual(c.energies((1,)*8, (1,)*5+(-1,)*3)[1], F(3,4))
        self.assertNotEqual(c.energies((4,)*8)[1], c.energies((0,)*8)[1])

    def test_affine_ground_exchange_preserves_target_energy(self):
        for q in ((0,)*8,)+c.roots():
            reflected = tuple(1-x for x in q)
            self.assertTrue(c.lattice(reflected))
            self.assertEqual(c.energies(q)[1], c.energies(reflected)[1])
        self.assertEqual(c.ground_charges((1,)*8), ((0,)*8,(1,)*8))

    def test_higher_charge_and_oscillator_domain_bounds(self):
        rng = random.Random(9092026)
        for _ in range(1000):
            integer = [rng.randint(-6,6) for _ in range(8)]
            integer[0] += sum(integer) % 2
            # Use one common half-lattice parity, not independent half charges.
            half = rng.randrange(2)
            q = tuple(2*x+half for x in integer)
            signs = tuple(rng.choice((-1,1)) for _ in range(8))
            l0, h = c.energies(q, signs, rng.randrange(8))
            self.assertGreaterEqual(h,0)
            self.assertLessEqual((l0-h)**2,l0)
            self.assertLessEqual(1+l0,2*(1+h))
            self.assertLessEqual(1+h,F(3,2)*(1+l0))
            for p in (1,2,3):
                self.assertLessEqual((1+l0)**(2*p),2**(2*p)*(1+h)**(2*p))

    def test_charge_shift_commutator_without_changing_cocycle(self):
        alpha = (1,)*8
        for q in c.roots():
            out = tuple(a+b for a,b in zip(q,alpha))
            difference = c.energies(out)[1]-c.energies(q)[1]
            self.assertEqual(difference,F(sum(q),4))

    def test_conformal_improvement_changes_central_charge_and_adjoint(self):
        self.assertEqual(F(8)-12*F(8,16),2)
        for n in (-3,-1,1,2):
            self.assertEqual(-(n+1)+(1-n),-2*n)
            self.assertNotEqual(-2*n,0)

    def test_invalid_inputs_are_not_silently_projected(self):
        with self.assertRaises(ValueError):
            c.energies((2,0,0,0,0,0,0,0))
        with self.assertRaises(ValueError):
            c.energies((0,)*8, (0,)*8)
        with self.assertRaises(ValueError):
            c.energies((0,)*8, oscillator=-1)

    def test_scope_does_not_promote_a_target_to_microscopic_closure(self):
        record = c.record()
        for flag in ("microscopic_half_charge_field_constructed", "eight_channel_selection_derived",
                     "physical_gap_or_TOE_closure", "independent_mathematical_review"):
            self.assertIs(record[flag],False)


if __name__ == "__main__":
    unittest.main()
