#!/usr/bin/env python3
"""Exact UV residues and abstract simple-current test; conditional Ising IR."""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


OUT = Path(__file__).resolve().parent
ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
checks = {}


def ck(name, condition):
    if not condition:
        raise RuntimeError("FAIL: " + name)
    checks[name] = checks.get(name, 0) + 1


source_dynamics_pins = {
    "experiments/theory-contracts/source-dynamics-selection-20260920/PROOF.txt": "03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2",
    "experiments/theory-contracts/source-dynamics-selection-20260920/certificate.json": "439f93d133024fdea14de0a3a36f4178ad40df36ff66b02bb5a62324031bc159",
}
for rel, expected in source_dynamics_pins.items():
    ck("source_dynamics_pin", sha256((ROOT / rel).read_bytes()).hexdigest() == expected)


# D8_1 discriminant fusion, with c acting as the proposed simple current.
bits = {"0": (0, 0), "v": (1, 0), "s": (0, 1), "c": (1, 1)}
from_bits = {v: k for k, v in bits.items()}
h_d8 = {"0": F(0), "v": F(1, 2), "s": F(1), "c": F(1)}


def d8_fuse(a, b):
    return from_bits[tuple(x ^ y for x, y in zip(bits[a], bits[b]))]


h_i = {"1": F(0), "psi": F(1, 2), "sigma": F(1, 16)}


def psi_fuse(a):
    return {"1": "psi", "psi": "1", "sigma": "sigma"}[a]


def ising_fuse(a, b):
    if a == "1":
        return {b}
    if b == "1":
        return {a}
    if a == b == "psi":
        return {"1"}
    if "sigma" in (a, b) and "psi" in (a, b):
        return {"sigma"}
    if a == b == "sigma":
        return {"1", "psi"}
    raise ValueError((a, b))


Q_c = {a: (h_d8["c"] + h_d8[a] - h_d8[d8_fuse("c", a)]) % 1 for a in bits}
Q_psi = {a: (h_i["psi"] + h_i[a] - h_i[psi_fuse(a)]) % 1 for a in h_i}
ck("D8_c_monodromy", Q_c == {"0": F(0), "v": F(1, 2), "s": F(1, 2), "c": F(0)})
ck("Ising_psi_monodromy", Q_psi == {"1": F(0), "psi": F(0), "sigma": F(1, 2)})
ck("J_is_order_two_fermion", d8_fuse("c", "c") == "0" and psi_fuse("psi") == "1" and h_d8["c"] + h_i["psi"] == F(3, 2))

right_all = {(a, b) for a in bits for b in h_i}
right_local = {(a, b) for a, b in right_all if (Q_c[a] + Q_psi[b]) % 1 == 0}
expected_right = {
    ("0", "1"), ("0", "psi"), ("c", "1"), ("c", "psi"),
    ("v", "sigma"), ("s", "sigma"),
}
ck("right_monodromy_local_set", right_local == expected_right)


def J_action(x):
    return d8_fuse("c", x[0]), psi_fuse(x[1])


orbits = []
remaining = set(right_local)
while remaining:
    x = min(remaining)
    orbit = frozenset((x, J_action(x)))
    orbits.append(orbit)
    remaining -= orbit
expected_orbits = {
    frozenset({("0", "1"), ("c", "psi")}),
    frozenset({("0", "psi"), ("c", "1")}),
    frozenset({("v", "sigma"), ("s", "sigma")}),
}
ck("three_J_orbits", set(orbits) == expected_orbits)

# Closure of the monodromy-local right set under D8 x Ising fusion.
for x, y in product(right_local, repeat=2):
    outcomes = {(d8_fuse(x[0], y[0]), z) for z in ising_fuse(x[1], y[1])}
    ck("right_fusion_closed", outcomes <= right_local)

# Conditional nonchiral six-sector assignment motivated by the four
# Gamma/M classes after an additional massive-vacuum/spin-structure choice.
# The third entry is the left critical Ising sector.  It is entered here as
# a candidate and is not derived from the UV residues below.
full = {
    ("0", "1", "1"),
    ("0", "psi", "psi"),
    ("c", "psi", "1"),
    ("c", "1", "psi"),
    ("v", "sigma", "sigma"),
    ("s", "sigma", "sigma"),
}
conditional_ir_assignment = {
    "0": {("1", "1"), ("psi", "psi")},
    "c": {("psi", "1"), ("1", "psi")},
    "v": {("sigma", "sigma")},
    "s": {("sigma", "sigma")},
}
ck("conditional_IR_candidate_six_terms", full == {(a, r, l) for a, pairs in conditional_ir_assignment.items() for r, l in pairs})
ck("conditional_candidate_right_part_is_monodromy_local", {(a, r) for a, r, _ in full} == right_local)
ck("J_preserves_left_and_pairs_conditional_candidate", {(J_action((a, r))[0], J_action((a, r))[1], l) for a, r, l in full} == full)

# Exact residue derivation from P0=Zn+Zz in u,v coordinates.
zero_residues = {((a + b) % 2, (a - b) % 2) for a, b in product(range(2), repeat=2)}
c_residues = {((1 + a + b) % 2, (a - b) % 2) for a, b in product(range(2), repeat=2)}
f_twice_residues = {((2 * (a + b) + 1) % 2, (2 * (a - b) - 1) % 2) for a, b in product(range(2), repeat=2)}
b_twice_residues = {((2 * (a + b) + 1) % 2, (2 * (a - b) + 1) % 2) for a, b in product(range(2), repeat=2)}
ck("Gamma_UV_neutral_residue_correlation", zero_residues == {(0, 0), (1, 1)} and c_residues == {(1, 0), (0, 1)} and f_twice_residues == b_twice_residues == {(1, 1)})

full_weights = {(a, r, l): (h_d8[a] + h_i[r], h_i[l]) for a, r, l in full}
expected_weights = {
    ("0", "1", "1"): (F(0), F(0)),
    ("0", "psi", "psi"): (F(1, 2), F(1, 2)),
    ("c", "psi", "1"): (F(3, 2), F(0)),
    ("c", "1", "psi"): (F(1), F(1, 2)),
    ("v", "sigma", "sigma"): (F(9, 16), F(1, 16)),
    ("s", "sigma", "sigma"): (F(17, 16), F(1, 16)),
}
ck("six_sector_IR_weights", full_weights == expected_weights)

# Direct Vc decomposition.  For x=T(p)+A u+B v,
# (h_R,h_L)=((p^2+A^2)/2,B^2/2).  Half-lattice twist fields contain one
# additional massive-Ising 1/16 on each side before the massive vacuum is
# projected, hence the conditional subtraction shown here.
uv_weights = {
    "f_UV": ((F(1) + F(1, 4)) / 2, F(1, 4) / 2),
    "b_UV": ((F(2) + F(1, 4)) / 2, F(1, 4) / 2),
    "raw_f_plus_b": ((F(4) + F(1)) / 2, F(0)),
    "minimal_c_plus_u": ((F(2) + F(1)) / 2, F(0)),
    "minimal_c_plus_v": (F(2) / 2, F(1) / 2),
}
ck("UV_lattice_weights", uv_weights == {
    "f_UV": (F(5, 8), F(1, 8)),
    "b_UV": (F(9, 8), F(1, 8)),
    "raw_f_plus_b": (F(5, 2), F(0)),
    "minimal_c_plus_u": (F(3, 2), F(0)),
    "minimal_c_plus_v": (F(1), F(1, 2)),
})
ck("conditional_twist_IR_weights", (uv_weights["f_UV"][0] - F(1, 16), uv_weights["f_UV"][1] - F(1, 16)) == expected_weights[("v", "sigma", "sigma")] and (uv_weights["b_UV"][0] - F(1, 16), uv_weights["b_UV"][1] - F(1, 16)) == expected_weights[("s", "sigma", "sigma")])

previous = json.loads((OUT / "certificate.json").read_text())
ck("prior_exact_result_retained", previous["critical_Vc_module_minima"]["c"] == "3/2" and previous["raw_c_representative_control"]["f_plus_b_Delta_Vc"] == "5/2")

result = {
    "research_id": "UR.SOURCE.IR_GLUE.01",
    "verdict": "PARTIAL",
    "mathematical_verdict": "EXACT_UV_RESIDUES_AND_ABSTRACT_FERMIONIC_SIMPLE_CURRENT_DIAGNOSTIC_WITH_CONDITIONAL_IR_CANDIDATE",
    "checks": dict(sorted(checks.items())),
    "right_simple_current": {
        "J": "(c,psi_R)",
        "h": "3/2",
        "statistics": "fermionic",
        "monodromy_local_sectors": ["(0,1)", "(0,psi)", "(c,1)", "(c,psi)", "(v,sigma)", "(s,sigma)"],
        "orbits": ["(0,1)<->(c,psi)", "(0,psi)<->(c,1)", "(v,sigma)<->(s,sigma)"],
    },
    "conditional_correlated_IR_candidate": [
        "(0,1_R,1_L)", "(0,psi_R,psi_L)",
        "(c,psi_R,1_L)", "(c,1_R,psi_L)",
        "(v,sigma_R,sigma_L)", "(s,sigma_R,sigma_L)",
    ],
    "exact_UV_inheritance": "The four Gamma/M classes fix only the u/v coefficient residues: equal integer parity for 0, opposite integer parity for c, and half-integer residues for v and s.",
    "conditional_J_support": "Integral Gamma representatives exist for the c class dressed by u or v. Identifying the massless projection of the chiral u dressing with psi_R is an additional refermionization and massive-vacuum assumption; it motivates J but does not derive it from the source.",
    "conditional_step": "Identifying the UV residues with independently conserved critical Ising 1/psi/sigma sectors after removing the massive copy requires the massive-Majorana mass sign, massive vacuum, spin structure, and order/disorder-line convention.",
    "decision": "The right simple-current monodromy algebra is exact inside the assumed D8_1 x Ising_R product category. The six-sector expression is only a compatible conditional candidate, not a Gamma-derived or source-derived physical IR projector.",
    "source_dynamics_boundary": "UR.SOURCE.DYNAMICS_SELECTION.01 selects no Vc dynamics. Its direct V0-to-Vaux midpoint has Delta(n)=Delta(z)=2, whereas the separate diagnostic Vc used here has Delta(n)=Delta(z)=1.",
    "not_claimed": ["N=1 supersymmetry", "simultaneous ordinary locality of sigma and mu", "four-dimensional chirality", "source selection of a light spinor"],
}
(OUT / "ir_glue_certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "research_id": result["research_id"], "checks": sum(checks.values()), "verdict": result["verdict"]}, sort_keys=True))
