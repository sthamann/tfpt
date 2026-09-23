#!/usr/bin/env python3
"""Exact q21/q12 gap and full two-source vacuum audit.

No diagonalization is performed.  The checker combines pinned exact native
partial-trace identities, exact source-class band certificates, and the
independently certified q22/q23/q20 pair bounds.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
RELAXATION = HERE / "relaxation_certificate.json"
SOURCE_CLASSES = HERE / "source_classes.json"
PAIR22 = HERE / "pair22_audit.json"
LOCAL_CERT = ROOT / (
    "experiments/theory-contracts/"
    "compiler-root-source-backreaction-20260919/spectrum_certificate.json"
)
PINS = {
    RELAXATION: "f92d980c920b1e00bbc4890e664febe0a707515211ada87409556b7e39df3556",
    SOURCE_CLASSES: "5ea297c7f84f32f2053d39a9632832f81c9eebcbcf46b2ed9b6866c826f12cde",
    PAIR22: "495107144114e889f4a8c5396bc01012c4cde3cf242b00f8d481d810d7b82e34",
    LOCAL_CERT: "d1e907a341bef81f255ab553e3c6c1db672500ebf6e37411e3a1f7062f5d40d8",
}

checks: list[str] = []


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path, digest in PINS.items():
    require(sha256(path) == digest, "pin " + str(path))

relaxation = json.loads(RELAXATION.read_text())
classes = json.loads(SOURCE_CLASSES.read_text())
pair22 = json.loads(PAIR22.read_text())
local = json.loads(LOCAL_CERT.read_text())

require(relaxation["status"] == "PASS", "native partial-trace certificate passes")
for guard in (
    "bar4 local roots 1/2,5/6,11/10",
    "partial L =9I/10-BellBell*/10",
    "partial L squared =251I/300-11 BellBell*/75",
    "adjoint bar4 variance 2/75",
):
    require(guard in relaxation["guard_names"], "native guard " + guard)

q1_local_classes = {
    row["central_value"]: row for row in classes["local_class_spectra"]["1"]["classes"]
}
q1_single_classes = {
    row["central_value"]: row
    for row in classes["single_matter_class_spectra"]["1"]["classes"]
}
require(set(q1_local_classes) == {"1/6", "3/10", "1/2"},
        "q1 has the three exact central source classes")
require(q1_local_classes["1/6"]["dimension"] == 36,
        "q1 central one-sixth class has dimension36")
require(q1_local_classes["1/6"]["local_L_minimum"] == "1/2",
        "q1 dimension36 class local floor one half")
require(
    {row["eigenvalue"] for row in q1_local_classes["1/6"]["K_spectrum"]}
    == {"-3/10", "-1/10", "0", "1/10", "1/6", "3/10", "1/2"},
    "q1 dimension36 exact local band set",
)
require(q1_single_classes["1/6"]["B_maximum"] == "1/3",
        "q1 dimension36 one-matter maximum one third")
require(q1_local_classes["3/10"]["dimension"] == 20
        and q1_local_classes["3/10"]["local_L_minimum"] == "7/10",
        "q1 dimension20 class local floor seven tenths")
require(q1_local_classes["1/2"]["dimension"] == 4
        and q1_local_classes["1/2"]["module"] == "bar4 coordinate source",
        "q1 bar4 coordinate class is identified")
require(q1_single_classes["1/2"]["B_maximum"] == "1",
        "q1 bar4 one-matter maximum one")
one_band = next(
    row for row in q1_single_classes["1/2"]["B_spectrum"]
    if row["eigenvalue"] == "1"
)
require(one_band["multiplicity"] == 1, "q1 bar4 B1 eigenvalue one is unique")
require(one_band["multiplicity_evidence"] == "EXACT_RANK_ONE_GAUSSIAN_MINOR_IDENTITY",
        "q1 bar4 invariant uniqueness is exact")

# q1 dimension36 against the q2 B packet.  The local interval is [1/2,13/10],
# the normalized packet compression mean is >=1-(1/2)(1/3)=5/6, and the q2 B
# complement gap is g=2/3.  The decreasing convex resolvent is bounded by its
# endpoint chord.
energy = sp.symbols("energy", real=True)
left = sp.Rational(1, 2)
right = sp.Rational(13, 10)
mean = sp.Rational(5, 6)
gap_B = sp.Rational(2, 3)
f_left = 1 / (left + gap_B - energy)
f_right = 1 / (right + gap_B - energy)
chord_at_mean = sp.simplify(
    f_left + (f_right - f_left) * (mean - left) / (right - left)
)
zeta = sp.Rational(37, 30) - sp.sqrt(71) / 15
require(sp.simplify(chord_at_mean.subs(energy, zeta) - sp.Rational(3, 2)) == 0,
        "q1 dimension36 chord floor saturates Schur threshold")
require(zeta > sp.Rational(3, 5),
        "q1 dimension36 pair comparison lies strictly above three fifths")

# Exact bar4 block.  On the packet range, the unique B1=1 direction Phi has
# energy1/2 and the orthogonal15-dimensional component has mean9/10.  The Q
# block is at least 2/3+1/2=7/6 and the exact off-block norm squared is2/75.
packet_adjoint_mean = sp.Rational(9, 10)
q_block_floor = sp.Rational(7, 6)
off_squared = sp.Rational(2, 75)
c21 = sp.simplify(
    (packet_adjoint_mean + q_block_floor
     - sp.sqrt((packet_adjoint_mean - q_block_floor) ** 2 + 4 * off_squared)) / 2
)
require(c21 == (31 - 2 * sp.sqrt(10)) / 30,
        "exact bar4 q21 complement constant")
require(c21 > sp.Rational(3, 5), "bar4 q21 complement lies above three fifths")

# The other invariant source blocks cannot compete: q1 dimension20 has local
# floor7/10, and q2 X plus any q1 class has floor2/5+1/2=9/10.
require(sp.Rational(7, 10) > zeta > sp.Rational(3, 5),
        "q1 dimension20 direct floor exceeds the central chord floor")
require(sp.Rational(2, 5) + sp.Rational(1, 2) == sp.Rational(9, 10),
        "q2 X plus q1 direct floor is nine tenths")
q21_complement = min(c21, zeta, sp.Rational(7, 10), sp.Rational(9, 10))
require(q21_complement == zeta, "full q21 complement is controlled by dimension36 chord")

# Full two-source theorem.  q21 and q12 each have one exact Phi channel at1/2.
# q22 supplies an attained quartet at3/5; q20/q02 and q23/q32 are strictly
# above3/5; every remaining phase pair is already >=1 by local floors.
require(pair22["exact"]["full_q22_floor"] == "3/5",
        "q22 exact floor three fifths")
require(pair22["exact"]["full_q22_ground_multiplicity"] == 4,
        "q22 ground quartet multiplicity")
q23_floor = sp.sympify(pair22["exact"]["related_q23_q32_certified_floor"])
q20_floor = sp.sympify(pair22["exact"]["related_q20_q02_certified_floor"])
require(q23_floor > sp.Rational(3, 5) and q20_floor > sp.Rational(3, 5),
        "q23 q32 q20 q02 lie strictly above three fifths")
require(
    {charge: 1 - max(sp.Rational(value) for value in spectrum)
     for charge, spectrum in enumerate(local["A_phase_spectra"])}
    == {0: sp.Rational(3, 5), 1: sp.Rational(1, 2),
        2: sp.Integer(0), 3: sp.Rational(1, 2)},
    "full exact one-edge phase floors",
)
two_source_ground = sp.Rational(1, 2)
two_source_next = sp.Rational(3, 5)
two_source_gap = two_source_next - two_source_ground
require(two_source_gap == sp.Rational(1, 10), "full two-source exact gap one tenth")

# Two disjoint q21/q12 ground projectors sharing one matter register have
# overlap1/4 because each ground state's shared-matter marginal is I4/4.
# The pair complement gap delta=c21-1/2 then gives the m4 lower bound below.
pair_ground_overlap = sp.Rational(1, 4)
delta_bar4 = c21 - sp.Rational(1, 2)
double_pair_floor = sp.simplify(
    1 + (1 - pair_ground_overlap) * delta_bar4
)
require(double_pair_floor == sp.Rational(7, 5) - sp.sqrt(10) / 20,
        "exact double bar4 pair lower bound")
require(double_pair_floor > sp.Rational(391, 320),
        "double bar4 pair sectors exceed the m4 trial upper")

result = {
    "status": "PASS",
    "verdict": "EXACT_FULL_TWO_SOURCE_GROUND_DOUBLET_AND_GAP",
    "checks": len(checks),
    "guard_names": checks,
    "pins": {str(path): digest for path, digest in PINS.items()},
    "exact": {
        "q21_q12_ground": "1/2",
        "q21_q12_ground_multiplicity_each_orientation": 1,
        "q1_dimension36_pair_floor": str(zeta),
        "q1_dimension36_pair_floor_numeric": float(zeta),
        "bar4_q21_complement": str(c21),
        "bar4_q21_complement_numeric": float(c21),
        "q1_dimension20_pair_floor": "7/10",
        "q2_X_plus_q1_floor": "9/10",
        "full_q21_q12_complement_floor": str(q21_complement),
        "full_two_source_ground": "1/2",
        "full_two_source_ground_multiplicity": 2,
        "full_two_source_next_energy": "3/5",
        "full_two_source_next_multiplicity": 4,
        "full_two_source_gap": "1/10",
        "double_pair_ground_projector_overlap": "1/4",
        "double_bar4_pair_floor": str(double_pair_floor),
        "double_bar4_pair_floor_numeric": float(double_pair_floor),
        "excluded_all_bar4_module_patterns": ["1212", "2112", "2121"],
    },
    "scope": (
        "Pure-permutation J=mu=0 two-source, three-matter Hamiltonian and the "
        "specified all-bar4 double-pair m4 subspaces.  This closes the former "
        ".24 full-ground Assumption G only at the unperturbed two-source level."
    ),
    "not_claimed": [
        "that the full m4 ground lies in a particular source sector",
        "exclusion of non-bar4 modules in phases1212,2112,2121",
        "a large-chain vacuum, wall dispersion, or Dirac field",
    ],
}

(HERE / "q21_audit.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": result["status"],
    "checks": result["checks"],
    "two_source_ground": result["exact"]["full_two_source_ground"],
    "two_source_gap": result["exact"]["full_two_source_gap"],
    "q21_complement": result["exact"]["full_q21_q12_complement_floor"],
}, sort_keys=True))
