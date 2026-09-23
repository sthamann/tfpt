"""Rational consequence of declared unitary Sugawara/coset premises.

This verifies the arithmetic in CENTRAL_CHARGE_GATE.txt, not those physical
premises or a thermodynamic scaling limit of the native source.
"""
from fractions import Fraction
from pathlib import Path
import json

level, dimension, dual_coxeter = 1, 248, 30
c_e8 = Fraction(level * dimension, level + dual_coxeter)
c_ising = Fraction(1, 2)
rest = c_ising - c_e8
norm = rest / 2
if (c_e8, rest, norm) != (8, Fraction(-15, 2), Fraction(-15, 4)):
    raise RuntimeError("central charge arithmetic failed")
result = {
    "scope": "rational consequences of declared unitary Sugawara/coset premises; not a continuum proof",
    "E8_c": str(c_e8),
    "Ising_each_chiral_c": str(c_ising),
    "coset_c_if_embedded": str(rest),
    "coset_vacuum_level2_norm_squared": str(norm),
    "unitarity_contradiction": norm < 0,
    "edge_signature": 9 - 1,
    "Ising_chiral_difference": str(c_ising - c_ising),
    "native_full_chain_ir_identified": False,
}
Path(__file__).with_name("central_charge_gate.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result))
