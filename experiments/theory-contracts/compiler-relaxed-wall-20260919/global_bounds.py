#!/usr/bin/env python3
"""Exact analytic m=4 source-sector bounds without full-chain diagonalization.

This checker combines only:
  * the exact one-bond phase spectra from the pinned .17 certificate;
  * the exact adjacent-Omega projector angle ||Q_e Q_(e+1)||=1/4;
  * the exact .23 mixed (barSym2, trivial) two-edge floor;
  * exact finite packet matrices already derived in .24 and core_six.py;
  * the separate fixed-module relaxation certificate, used only as provenance
    for the six-state native reduction and never as a full-source lower bound.

It enumerates phase and coarse representation candidates.  Complements named
X and Y are not decomposed into irreducibles, so the output is a rigorous
candidate list, not a full representation-sector spectrum.
"""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
import itertools as it
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
PINS = {
    ROOT / "experiments/theory-contracts/compiler-root-source-backreaction-20260919/spectrum_certificate.json":
        "d1e907a341bef81f255ab553e3c6c1db672500ebf6e37411e3a1f7062f5d40d8",
    ROOT / "experiments/theory-contracts/compiler-pair-sector-audit-20260919/PROOF.txt":
        "b63d5a7a97c331f0aa0920fb77bded14981be1c6ec735fdc91e3b1536ed5a766",
    ROOT / "experiments/theory-contracts/compiler-bond-response-20260919/triple_response.json":
        "f9471c23376e0359e2d5d9f0c105d1b7e5266a1d1437f7c0279027781a234dc2",
    ROOT / "experiments/theory-contracts/compiler-domain-wall-core-20260919/PROOF.txt":
        "fe9c66ef6821ff4771993cc899dd7ea385b3ad87a45712e831d12cc190c9ddb6",
    HERE / "relaxation_certificate.json":
        "f92d980c920b1e00bbc4890e664febe0a707515211ada87409556b7e39df3556",
    HERE / "core_six.py":
        "6336b5758819738f8ca2d388fbbadc1460eb1a9c77c1245aa4c55c133f9e7d30",
    HERE / "pair22_audit.json":
        "495107144114e889f4a8c5396bc01012c4cde3cf242b00f8d481d810d7b82e34",
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


# Exact one-bond minima by source quarter charge, reconstructed directly from
# the exact class-sum spectra A=I-L in the .17 certificate.
certificate = json.loads(next(iter(PINS)).read_text())
phase_spectra = certificate["A_phase_spectra"]
local_floor: dict[int, F] = {}
for charge, spectrum in enumerate(phase_spectra):
    largest_A = max(F(value) for value in spectrum)
    local_floor[charge] = F(1) - largest_A
require(
    local_floor == {0: F(3, 5), 1: F(1, 2), 2: F(0), 3: F(1, 2)},
    "exact local phase floors",
)
require(certificate["gap_for_all_J_nonnegative"] == "2*kappa/5",
        "single q2 packet complement gap two fifths")

relaxation_certificate = json.loads((HERE / "relaxation_certificate.json").read_text())
require(relaxation_certificate["status"] == "PASS", "fixed-module certificate passes")
require(
    relaxation_certificate["scope"] ==
    "EXACT_FIXED_SOURCE_MODULE_THEOREMS_NOT_COMPLETE_SOURCE_VACUUM",
    "fixed-module certificate retains the full-source firewall",
)
require(
    relaxation_certificate["complete_fixed_module_complement_floor"] ==
    "(205-sqrt973)/120",
    "fixed-module complement floor provenance",
)


# The original packet-angle bound gives3/10.  pair22_audit.json sharpens the
# complete q22 source sector to3/5; both identities remain checked here.
packet_gap = F(2, 5)
packet_cosine = F(1, 4)
adjacent_22_floor = packet_gap * (1 - packet_cosine)
require(adjacent_22_floor == F(3, 10), "adjacent q2 q2 exact floor three tenths")
pair22_certificate = json.loads((HERE / "pair22_audit.json").read_text())
require(pair22_certificate["exact"]["full_q22_floor"] == "3/5",
        "exact full q22 pair floor three fifths")
full_22_floor = F(3, 5)
q23_floor = sp.sympify(pair22_certificate["exact"]["related_q23_q32_certified_floor"])
q20_floor = sp.sympify(pair22_certificate["exact"]["related_q20_q02_certified_floor"])
q2222_floor = sp.sympify(pair22_certificate["exact"]["full_phase2222_floor"])
require(q23_floor > sp.Rational(3, 5), "exact q23 q32 bound exceeds three fifths")
require(q20_floor > sp.Rational(3, 5), "exact q20 q02 bound exceeds three fifths")
require(q2222_floor > sp.Rational(391, 320), "exact full phase2222 bound exceeds trial upper")

# A bounded three-packet improvement is also available.  For outer packets
# P=Q_1 Q_3, the middle-packet overlap obeys ||P Q_2||^2=1/(16*10)=1/160:
# two maximally mixed shared matter factors contribute 1/16 and the exact
# Omega source Schmidt maximum is 1/10.  Since
# (I-Q1)+(I-Q3) >= I-P, the three-bond floor is
# (2/5)(1-1/sqrt(160)).  It is stronger than 3/10 on a run of three q2's,
# but will be checked below not to remove another phase string.
require(certificate["Schmidt_weights_source_vs_AB"] == "1/10 with multiplicity10",
        "Omega source Schmidt maximum one tenth")
triple_222_floor = sp.Rational(2, 5) * (1 - 1 / (4 * sp.sqrt(10)))
require(triple_222_floor > sp.Rational(3, 10),
        "three adjacent q2 packet bound improves one-pair bound")


# The exact .24 invariant 202 doublet has coefficient matrix A below in the
# nonorthogonal Gram G.  Appending a boundary Phi packet gives a scalar 1/2
# term, hence an exact m4 eigenvector at 1/2+(8-sqrt(19))/5.
triple_G = sp.Matrix([[1, sp.Rational(1, 4)], [sp.Rational(1, 4), 1]])
triple_A = sp.Matrix([
    [sp.Rational(4, 5), -sp.Rational(3, 5)],
    [-sp.Rational(1, 5), sp.Rational(12, 5)],
])
require(triple_G * triple_A == triple_A.T * triple_G,
        "triple coefficient action Hermitian in exact Gram")
triple_energies = set(triple_A.eigenvals())
require(
    triple_energies == {(8 - sp.sqrt(19)) / 5, (8 + sp.sqrt(19)) / 5},
    "exact triple invariant energies",
)
boundary_upper = sp.Rational(1, 2) + (8 - sp.sqrt(19)) / 5
require(sp.N(boundary_upper, 18) > sp.Rational(1228, 1000),
        "boundary Phi plus 202 branch value")


# Independent algebra check of the supplied exact six-packet matrix.  A small
# integer vector already improves the earlier upper bound without relying on
# its numerically computed lowest root.
six_G = sp.Matrix([
    [1, sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 16), sp.Rational(1, 16), sp.Rational(1, 4)],
    [sp.Rational(1, 4), 1, sp.Rational(1, 16), sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 16)],
    [sp.Rational(1, 4), sp.Rational(1, 16), 1, sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 16)],
    [sp.Rational(1, 16), sp.Rational(1, 4), sp.Rational(1, 4), 1, sp.Rational(1, 16), sp.Rational(1, 4)],
    [sp.Rational(1, 16), sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 16), 1, sp.Rational(1, 4)],
    [sp.Rational(1, 4), sp.Rational(1, 16), sp.Rational(1, 16), sp.Rational(1, 4), sp.Rational(1, 4), 1],
])
six_H = sp.Matrix([
    [sp.Rational(13, 10), -sp.Rational(8, 15), -sp.Rational(1, 5), 0, sp.Rational(1, 15), -sp.Rational(2, 5)],
    [-sp.Rational(1, 5), sp.Rational(77, 30), 0, -sp.Rational(1, 5), -sp.Rational(1, 3), 0],
    [0, sp.Rational(1, 15), sp.Rational(21, 10), -sp.Rational(2, 5), -sp.Rational(1, 3), 0],
    [0, -sp.Rational(2, 15), -sp.Rational(1, 5), sp.Rational(29, 10), sp.Rational(1, 15), 0],
    [0, -sp.Rational(2, 15), 0, 0, sp.Rational(101, 30), -sp.Rational(1, 5)],
    [0, sp.Rational(1, 15), 0, 0, -sp.Rational(1, 3), sp.Rational(29, 10)],
])
require(six_G.is_positive_definite, "six-packet Gram positive definite")
require(six_G * six_H == six_H.T * six_G, "six-packet action exactly Hermitian")
rational_witness = sp.Matrix([6, 1, 0, 0, 0, 0])
rational_upper = sp.factor(
    (rational_witness.T * six_G * six_H * rational_witness)[0]
    / (rational_witness.T * six_G * rational_witness)[0]
)
require(rational_upper == sp.Rational(391, 320), "exact rational six-packet trial energy")
require(rational_upper < boundary_upper, "six-packet rational witness improves boundary branch")


# All later exclusions use the stronger exact rational variational upper.
upper = F(391, 320)


def max_adjacent_matching(active_sites: set[int]) -> int:
    edges = [i for i in range(3) if i in active_sites and i + 1 in active_sites]
    best = 0
    for flags in range(1 << len(edges)):
        selected = [edges[j] for j in range(len(edges)) if flags & (1 << j)]
        if all(abs(a - b) > 1 for j, a in enumerate(selected) for b in selected[j + 1 :]):
            best = max(best, len(selected))
    return best


def phase_lower_bound(charges: tuple[int, ...]) -> sp.Expr:
    """Best disjoint exact singleton/pair bound, plus special 2222 overlap bound."""
    pair_floors = {
        (2, 2): sp.Rational(3, 5),
        (2, 3): q23_floor,
        (3, 2): q23_floor,
        (2, 0): q20_floor,
        (0, 2): q20_floor,
    }
    dp: list[sp.Expr | None] = [None] * 5
    dp[0] = sp.Integer(0)
    for i in range(4):
        require(dp[i] is not None, "phase dynamic-programming prefix reachable")
        singleton = sp.Rational(local_floor[charges[i]].numerator,
                                local_floor[charges[i]].denominator)
        candidate = dp[i] + singleton
        dp[i + 1] = candidate if dp[i + 1] is None else sp.Max(dp[i + 1], candidate)
        if i < 3 and charges[i:i + 2] in pair_floors:
            candidate = dp[i] + pair_floors[charges[i:i + 2]]
            dp[i + 2] = candidate if dp[i + 2] is None else sp.Max(dp[i + 2], candidate)
    require(dp[4] is not None, "phase dynamic-programming full path reachable")
    bound = dp[4]
    if charges == (2, 2, 2, 2):
        bound = sp.Max(bound, q2222_floor)
    return sp.simplify(bound)


naive_phase_candidates: list[dict[str, object]] = []
excluded_by_packet: list[dict[str, object]] = []
surviving_phases: list[tuple[int, ...]] = []
for charges in it.product(range(4), repeat=4):
    base = sum((local_floor[q] for q in charges), F(0))
    if base > upper:
        continue
    strengthened = phase_lower_bound(charges)
    row = {
        "phase": "".join(map(str, charges)),
        "total_charge_mod4": sum(charges) % 4,
        "one_bond_floor": str(base),
        "packet_strengthened_floor": str(strengthened),
    }
    naive_phase_candidates.append(row)
    if strengthened > upper:
        excluded_by_packet.append(row)
    else:
        surviving_phases.append(charges)

require(len(naive_phase_candidates) == 67, "sixty-seven one-bond phase candidates")
require(len(excluded_by_packet) == 48, "forty-eight phases excluded by exact pair and overlap bounds")
require(len(surviving_phases) == 19, "nineteen phase strings survive exact phase-only bounds")
require(
    any("22" in row["phase"] and sp.sympify(row["packet_strengthened_floor"]) >= sp.Rational(3, 5)
        for row in naive_phase_candidates),
    "full q22 pair floor is represented in phase rows",
)
require(
    {total: sum(1 for p in surviving_phases if sum(p) % 4 == total)
     for total in range(4)} == {0: 6, 1: 6, 2: 3, 3: 4},
    "surviving phase strings have exact total-charge counts six six three four",
)


remaining = set(surviving_phases)
phase_profile_classes = []
while remaining:
    representative = min(remaining)
    profile_set = {
        representative,
        representative[::-1],
    } & remaining
    remaining -= profile_set
    phase_profile_classes.append({
        "representative": "".join(map(str, representative)),
        "members": ["".join(map(str, q)) for q in sorted(profile_set)],
        "classification": (
            "same exact lower-bound profile under the actual open-chain reversal symmetry"
        ),
    })
require(len(phase_profile_classes) == 10, "ten reversal profile classes")


# Coarse source-module refinement.
#   B = canonical barSym2 source module at q=2, the only module supporting Omega
#   X = its invariant q=2 orthogonal complement, hence local floor >=2/5
#   T = trivial source module at q=0
#   Y = its invariant q=0 orthogonal complement
#   O = unresolved q=1 or q=3 module (only the exact 1/2 local floor is used)
mixed_floor = (6 - sp.sqrt(6)) / 5


def strongest_partition_bound(
    charges: tuple[int, ...], modules: tuple[str, ...]
) -> sp.Expr:
    """Maximize proved disjoint singleton/pair operator floors on the path."""
    dp: list[sp.Expr | None] = [None] * 5
    dp[0] = sp.Integer(0)
    for i in range(4):
        require(dp[i] is not None, "dynamic-programming prefix reachable")
        if charges[i] == 2:
            singleton = sp.Integer(0) if modules[i] == "B" else sp.Rational(2, 5)
        else:
            singleton = sp.Rational(local_floor[charges[i]].numerator,
                                    local_floor[charges[i]].denominator)
        candidate = dp[i] + singleton
        dp[i + 1] = candidate if dp[i + 1] is None else sp.Max(dp[i + 1], candidate)
        if i == 3:
            continue
        pair: sp.Expr | None = None
        if charges[i:i + 2] == (2, 2):
            pair = sp.Rational(3, 5)
        elif charges[i:i + 2] in ((2, 3), (3, 2)):
            pair = q23_floor
        elif charges[i:i + 2] == (2, 0):
            pair = mixed_floor if modules[i:i + 2] == ("B", "T") else q20_floor
        elif charges[i:i + 2] == (0, 2):
            pair = mixed_floor if modules[i:i + 2] == ("T", "B") else q20_floor
        if pair is not None:
            candidate = dp[i] + pair
            dp[i + 2] = candidate if dp[i + 2] is None else sp.Max(dp[i + 2], candidate)
        if i <= 1 and charges[i:i + 3] == (2, 2, 2) \
                and modules[i:i + 3] == ("B", "B", "B"):
            candidate = dp[i] + triple_222_floor
            dp[i + 3] = candidate if dp[i + 3] is None else sp.Max(dp[i + 3], candidate)
    require(dp[4] is not None, "dynamic-programming full path reachable")
    bound = dp[4]
    if charges == (2, 2, 2, 2):
        bound = sp.Max(bound, q2222_floor)
    return sp.simplify(bound)


representation_candidates: list[dict[str, object]] = []
representation_excluded_count = 0
minimum_excluded_rep_bound: sp.Expr | None = None
maximum_surviving_rep_bound: sp.Expr = sp.Integer(0)
for charges in (tuple(q) for q in it.product(range(4), repeat=4)):
    if sum((local_floor[q] for q in charges), F(0)) > upper:
        continue
    choices = [
        ("T", "Y") if q == 0 else ("B", "X") if q == 2 else ("O",)
        for q in charges
    ]
    for modules in it.product(*choices):
        bound = strongest_partition_bound(charges, modules)
        if bound <= sp.Rational(upper.numerator, upper.denominator):
            maximum_surviving_rep_bound = max(maximum_surviving_rep_bound, bound)
            representation_candidates.append({
                "phase": "".join(map(str, charges)),
                "module_mask": "".join(modules),
                "proved_lower_bound": str(bound),
            })
        else:
            representation_excluded_count += 1
            if minimum_excluded_rep_bound is None or bound < minimum_excluded_rep_bound:
                minimum_excluded_rep_bound = bound

require(len(representation_candidates) == 31, "thirty-one coarse representation candidates")
require(maximum_surviving_rep_bound == sp.Rational(17, 10) - sp.sqrt(6) / 5,
        "largest surviving proved representation floor")
require(minimum_excluded_rep_bound == sp.Rational(29, 15) - sp.sqrt(445) / 30,
        "smallest excluded coarse representation floor")


surviving_by_total = {
    str(total): ["".join(map(str, q)) for q in surviving_phases if sum(q) % 4 == total]
    for total in range(4)
}

result = {
    "status": "PASS",
    "verdict": "EXACT_BOUNDED_CANDIDATE_LIST_FULL_GROUND_REQUIRES_NEW_RECOUPLING_BOUNDS",
    "checks": len(checks),
    "guard_names": checks,
    "source_pins": {str(path): digest for path, digest in PINS.items()},
    "exact_upper_bounds": {
        "boundary_Phi_plus_exact_202_eigenstate": str(boundary_upper),
        "boundary_numeric": float(boundary_upper),
        "six_packet_rational_witness_vector": [6, 1, 0, 0, 0, 0],
        "six_packet_rational_Rayleigh": str(rational_upper),
        "six_packet_rational_numeric": float(rational_upper),
        "fixed_module_exact_root_interval_not_used_in_global_exclusions":
            relaxation_certificate["central_root_interval"],
        "fixed_module_root_numeric_for_orientation_only": 1.2214939303524752,
    },
    "local_exact_floors": {str(q): str(value) for q, value in local_floor.items()},
    "phase_classification": {
        "one_bond_candidate_count": len(naive_phase_candidates),
        "excluded_by_exact_pair_and_overlap_bounds": len(excluded_by_packet),
        "surviving_phase_count": len(surviving_phases),
        "surviving_by_total_charge": surviving_by_total,
        "lower_bound_profile_classes": phase_profile_classes,
        "profile_warning": (
            "classes use open-chain reversal only; q1 and q3 are not interchanged"
        ),
        "excluded_phase_rows": excluded_by_packet,
    },
    "coarse_representation_classification": {
        "legend": {
            "B": "barSym2 module in q2; only source module supporting the Omega kernel",
            "X": "invariant q2 complement of B; exact local floor at least 2/5",
            "T": "trivial source module in q0",
            "Y": "invariant q0 complement of T",
            "O": "unresolved q1 or q3 source module; only exact local floor 1/2 used",
        },
        "candidate_count": len(representation_candidates),
        "excluded_assignment_count_among_the_67_naive_phases": representation_excluded_count,
        "largest_surviving_proved_floor": str(maximum_surviving_rep_bound),
        "smallest_excluded_proved_floor": str(minimum_excluded_rep_bound),
        "candidates": representation_candidates,
    },
    "decision": {
        "exactly_excluded": (
            "all other phase strings; 48 of the 67 one-bond candidates by exact q22, q23/q32, "
            "q20/q02 and phase2222 overlap bounds; "
            "and every coarse B/X/T/Y assignment not listed"
        ),
        "actual_low_state_known": (
            "phase 2102 has the exact rational full-space trial upper 391/320; a separate "
            "fixed-module certificate Sturm-isolates the smaller root near 1.221493930352475, "
            "without proving that it is the full-source ground"
        ),
        "first_missing_exact_bound": (
            "independent native certification of the supplied q21/q12 complement gap and then "
            "overlap bounds among the remaining 19 phase patterns; q22, q23/q32 and q20/q02 are closed"
        ),
        "not_proved": [
            "the full m4 ground phase or multiplicity",
            "that any of the 31 coarse candidates actually reaches its lower bound",
            "a large-chain vacuum, isolated defect, wall EFT or Dirac particle",
        ],
    },
}

(HERE / "global_bounds.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({
    "status": result["status"],
    "checks": result["checks"],
    "phase_candidates": result["phase_classification"]["surviving_phase_count"],
    "representation_candidates": result["coarse_representation_classification"]["candidate_count"],
    "exact_trial_upper": result["exact_upper_bounds"]["six_packet_rational_Rayleigh"],
}, sort_keys=True))
