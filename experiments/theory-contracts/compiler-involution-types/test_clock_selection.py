"""Independent exterior-minor verification of the finite clock census."""
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("clock_selection_checked", HERE / "clock_selection.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class ClockSelection(unittest.TestCase):
    def test_source_boundary_and_fixed_space(self):
        clock, boundary, _ = r.construct()
        self.assertEqual(clock * boundary, boundary)
        self.assertEqual(len((clock - sp.eye(16)).nullspace()), 10)
        self.assertEqual(boundary.rank(), 6)

    def test_exterior_minors_independently_verify_primitive_grades(self):
        clock, _, _ = r.construct()
        wedge = r.exterior_square(clock)
        z = sp.Symbol("z")
        expected = (z-1)**50 * (z+1)**20 * (z*z+z+1)**21 * (z*z-z+1)**4
        self.assertEqual(sp.expand(wedge.charpoly(z).as_expr() - expected), 0)
        self.assertEqual(wedge.T * wedge, sp.eye(120))

    def test_saved_record_and_physical_boundary(self):
        result = r.record()
        saved = json.loads((HERE / "clock_selection_validation.json").read_text())
        self.assertEqual(saved, json.loads(json.dumps(result)))
        self.assertEqual(result["exterior_square_grades"], {0:50, 1:4, 2:21, 3:20, 4:21, 5:4})
        self.assertFalse(result["scope"]["physical_Fock_polarization_or_charged_TFPT_lift_derived"])
        self.assertFalse(result["scope"]["Majorana_coordinates_identified_with_creation_modes"])


if __name__ == "__main__":
    unittest.main()
