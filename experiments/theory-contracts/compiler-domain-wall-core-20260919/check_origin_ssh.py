#!/usr/bin/env python3
"""Exact algebraic checks for the bounded origin/SSH dictionary audit."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
checks: list[str] = []


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


# Fail closed if the three primary local sources underlying the origin
# carrier/family claims change after this bounded audit.
SOURCE_PINS = {
    Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/origin_theory.tex"):
        "4a2ac752cf9beb65452d5c1aad3a9dc22b0d3fee24e8247c064ed654f910d95f",
    Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v486_transfer_full_rule.py"):
        "a8315978fb4ecbb4d178754483b03915c1016995667ac1ab7a0ea6e8dacb5825",
    Path("/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v487_transfer_clock_rungs.py"):
        "0c234246906ab637aabd816271b9f733082a1f94021db67b8fa2d4f6c63e560c",
}
for source_path, expected_sha256 in SOURCE_PINS.items():
    actual_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    require(actual_sha256 == expected_sha256,
            f"source pin {source_path.name}")


# The proposed two-sublattice Bloch matrix.
m, t1, t2, z, energy = sp.symbols("m t1 t2 z energy", real=True)
h = sp.Matrix([[m, t1 + t2 / z], [t1 + t2 * z, -m]])
expected = energy**2 - (m**2 + t1**2 + t2**2 + t1 * t2 * (z + 1 / z))
require(sp.expand((energy * sp.eye(2) - h).det() - expected) == 0,
        "Bloch characteristic polynomial")

gamma = sp.diag(1, -1)
require(sp.simplify(gamma * h + h * gamma) == 2 * m * sp.eye(2),
        "sublattice chiral symmetry holds exactly only at m=0")

h_pi = h.subs(z, -1)
require(sp.simplify(h_pi.det() + m**2 + (t1 - t2)**2) == 0,
        "positive-hopping bulk gap closes at m=0 and t1=t2")

# At the critical point the signed electronic branches cross linearly at pi,
# while a nonnegative one-wall spectrum needs a creation-energy shift.
q, t, ec = sp.symbols("q t ec", real=True, positive=True)
off_critical = sp.simplify(t * (1 - sp.exp(-sp.I * q)))
require(sp.simplify(sp.diff(off_critical, q).subs(q, 0) - sp.I * t) == 0,
        "critical electronic off-diagonal is linear near k=pi")
require(sp.simplify(2 * t * sp.cos(q / 2) - (2 * t - t * q**2 / 4)).series(q, 0, 3).removeO() == 0,
        "critical lower band has a quadratic minimum near k=0 after energy shift")
require(sp.simplify((ec - 2 * t).subs(ec, 2 * t)) == 0
        and sp.simplify((ec - 2 * t).subs(ec, 3 * t)) == t,
        "one-wall lower edge Ec-2t is nonnegative exactly when Ec>=2t")

# Phi-completed trial family: the supplied compression has uniform hopping
# mu/8.  Its unfolded lower edge is quadratic; cell doubling only folds the
# same band into a two-component midband crossing.
mu_hop, e_core, p = sp.symbols("mu_hop e_core p", real=True, positive=True)
t_phi = mu_hop / 8
one_band = e_core - 2 * t_phi * sp.cos(p)
require(sp.series(one_band, p, 0, 4).removeO()
        == e_core - mu_hop / 4 + mu_hop * p**2 / 8,
        "Phi trial uniform band has quadratic coefficient mu/8")

z_phi, e_phi = sp.symbols("z_phi e_phi", nonzero=True)
doubled = e_core * sp.eye(2) - t_phi * sp.Matrix([
    [0, 1 + 1 / z_phi], [1 + z_phi, 0]
])
require(sp.simplify(doubled.subs(z_phi, -1) - e_core * sp.eye(2))
        == sp.zeros(2),
        "doubled Phi trial chain crosses at the midband energy Ecore")

path4 = sp.zeros(4)
for path_index in range(3):
    path4[path_index, path_index + 1] = 1
    path4[path_index + 1, path_index] = 1
trial4 = e_core * sp.eye(4) - t_phi * path4
require(all(trial4[i, i + 1] == -mu_hop / 8 for i in range(3)),
        "four-position Phi trial compression has path hopping -mu/8")

# The origin text's exact carrier x family objects.
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
         (5, 6), (6, 7), (5, 8)]
A = sp.zeros(9)
for i, j in edges:
    A[i, j] = A[j, i] = 1
t_net = (A + 2 * sp.eye(9)) / 4
marks = sp.Matrix([1, 2, 3, 4, 5, 6, 4, 2, 3])
require(t_net * marks == marks,
        "origin carrier is nine-node affine-E8 network with Kac-mark fixed vector")

family = sp.Matrix([
    [1, 0, 0],
    [0, sp.Rational(1, 2), sp.Rational(1, 6)],
    [0, sp.Rational(1, 6), sp.Rational(1, 2)],
])
require(family.eigenvals() == {
    sp.Integer(1): 1, sp.Rational(2, 3): 1, sp.Rational(1, 3): 1
}, "origin family rule is three-dimensional with spectrum 1,2/3,1/3")

pair = family[1:3, 1:3]
require((pair**6).eigenvals() == {
    sp.Rational(64, 729): 1, sp.Rational(1, 729): 1
}, "six-hand family pair spectrum")

t_cusp = sp.diag(1, sp.Rational(64, 729), sp.Rational(1, 729))
transfer = sp.kronecker_product(t_net, t_cusp)
require(transfer.shape == (27, 27),
        "origin carrier x family transfer has dimension 9x3=27")
require(transfer * sp.kronecker_product(marks, sp.Matrix([1, 0, 0]))
        == sp.kronecker_product(marks, sp.Matrix([1, 0, 0])),
        "origin product fixed vector")
require(transfer * sp.kronecker_product(marks, sp.Matrix([0, 1, 0]))
        == sp.Rational(64, 729)
        * sp.kronecker_product(marks, sp.Matrix([0, 1, 0])),
        "origin recovery eigenvector")

# The older local u,w packet pair is nonorthogonal.  This is only an example;
# it is not the Gram matrix of the new maximal-packet wall-position family.
packet_gram = sp.Matrix([[1, sp.Rational(1, 4)],
                         [sp.Rational(1, 4), 1]])
require(packet_gram != sp.eye(2) and packet_gram.det() == sp.Rational(15, 16),
        "older finite u,w packet coordinates have Gram overlap 1/4")

result = {
    "status": "PASS",
    "checks": checks,
    "verdict": (
        "CRITICAL_SSH_TRIAL_COMPRESSION_DERIVED_"
        "PHYSICAL_LOW_ENERGY_WALL_BAND_AND_ORIGIN_DICTIONARY_NOT_DERIVED"
    ),
    "origin_transfer_dimension": 27,
    "origin_family_spectrum_one_step": ["1", "2/3", "1/3"],
    "origin_family_spectrum_six_hand": ["1", "64/729", "1/729"],
    "ssh_gap_closure": "m=0 and t1=t2 for positive hoppings, at k=pi",
    "chiral_symmetry": "{sigma_z,h}=2m I; exact only for m=0",
    "single_wall_boundary": (
        "after adding Ec I with Ec>=2t, the Dirac crossing is at energy Ec; "
        "the lowest one-wall branch is quadratic near k=0"
    ),
    "required_next_test": (
        "starting from the exact G=I trial compressions (flat bare wall; "
        "Phi-completed path hopping), eliminate the non-invariant complement "
        "and test whether the controlled effective kernel has SSH form"
    ),
}

(HERE / "origin_ssh_check.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2, sort_keys=True))
