#!/usr/bin/env python3
"""Exact finite-CAR checks for the QWZ charged-source correlator dictionary.

This is a narrow companion check.  It does not replace the all-N estimates in
microscopic-charged-car-limit/README.md and it does not add source channels.
"""
from __future__ import annotations

import hashlib
import json
import argparse
from pathlib import Path

import sympy as sp


ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
HERE = Path(__file__).resolve().parent
SOURCES = {
    "experiments/theory-contracts/microscopic-charged-car-limit/README.md":
        "39c613b80a1fe64200d269b782f6fb86c98f92c78058891a6144605e09c4532b",
    "experiments/theory-contracts/microscopic-charged-car-limit/checker.py":
        "2259bd7d6ab890c8cca562774b1b5cdc574e60fb72a04a8c8c8f6ed8292f113a",
    "experiments/theory-contracts/microscopic-charged-car-limit/test_checker.py":
        "fc8b16ae937cef9139e65f7316126c05f070265e3afe9548ab3b8a26335ca00d",
    "experiments/theory-contracts/charged-source-time-audit-20260920/HOLONOMY_REVIEW.txt":
        "12217b8c7e906e1142c49285ca66e8584af61815dd7f5b22218aef356ab4142a",
}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def annihilators(count: int) -> list[sp.Matrix]:
    out: list[sp.Matrix] = []
    for mode in range(count):
        matrix = sp.zeros(2**count)
        for mask in range(2**count):
            if (mask >> mode) & 1:
                sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
                matrix[mask ^ (1 << mode), mask] = sign
        out.append(matrix)
    return out


def expectation(matrix: sp.Matrix, vacuum_mask: int) -> sp.Expr:
    return sp.expand(matrix[vacuum_mask, vacuum_mask])


def timed_creation(a: list[sp.Matrix], coeffs: list[int], labels: list[int], time: int, z: sp.Symbol) -> sp.Matrix:
    # z=exp(i theta/4), h_j=(1-4j)/4.
    return sum((sp.Integer(c) * z ** (time * (1 - 4*j)) * op.T
                for c, j, op in zip(coeffs, labels, a)), sp.zeros(a[0].rows))


def timed_annihilation(a: list[sp.Matrix], coeffs: list[int], labels: list[int], time: int, z: sp.Symbol) -> sp.Matrix:
    # Coefficients are real and conjugation sends z to z^-1 on the unit circle.
    return sum((sp.Integer(c) * z ** (-time * (1 - 4*j)) * op
                for c, j, op in zip(coeffs, labels, a)), sp.zeros(a[0].rows))


def occupied_kernel(g: list[int], s: int, f: list[int], t: int,
                    labels: list[int], occupied: list[bool], z: sp.Symbol) -> sp.Expr:
    return sp.expand(sum(sp.Integer(gg*ff) * z ** ((t-s) * (1-4*j))
                         for gg, ff, j, occ in zip(g, f, labels, occupied) if occ))


def empty_kernel(g: list[int], s: int, f: list[int], t: int,
                 labels: list[int], occupied: list[bool], z: sp.Symbol) -> sp.Expr:
    return sp.expand(sum(sp.Integer(gg*ff) * z ** ((t-s) * (1-4*j))
                         for gg, ff, j, occ in zip(g, f, labels, occupied) if not occ))


def wedge(u: list[int], v: list[int]) -> sp.Matrix:
    return sp.Matrix([sp.Integer(u[i]*v[j] - u[j]*v[i])
                      for i in range(len(u)) for j in range(i+1, len(u))])


def gram(columns: list[sp.Matrix]) -> sp.Matrix:
    w = sp.Matrix.hstack(*columns)
    return w.T * w


def main() -> dict:
    for rel, digest in SOURCES.items():
        need(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == digest,
             f"source hash changed: {rel}")

    z = sp.symbols("z", nonzero=True)
    labels = [-1, 0, 1, 2]
    occupied = [j >= 1 for j in labels]
    a = annihilators(4)
    identity = sp.eye(16)
    vacuum_mask = sum((1 << i) for i, occ in enumerate(occupied) if occ)

    # Exact CAR, integer Ward charge, covariance C, and H=L0-Q/4.
    for i, ai in enumerate(a):
        for j, aj in enumerate(a):
            need(ai*aj + aj*ai == sp.zeros(16), "CAR annihilator relation")
            need(ai*aj.T + aj.T*ai == (identity if i == j else sp.zeros(16)),
                 "CAR mixed relation")
    number = [ai.T*ai for ai in a]
    q = sum((ni - int(occ)*identity for ni, occ in zip(number, occupied)), sp.zeros(16))
    h_values = [sp.Rational(1, 4) - j for j in labels]
    r_values = [sp.Rational(1, 2) - j for j in labels]
    h_fock = sum((h*(ni-int(occ)*identity)
                  for h, ni, occ in zip(h_values, number, occupied)), sp.zeros(16))
    l0_fock = sum((r*(ni-int(occ)*identity)
                   for r, ni, occ in zip(r_values, number, occupied)), sp.zeros(16))
    need(h_fock == l0_fock - q/4, "quarter-holonomy identity H=L0-Q/4")
    for ai in a:
        need(q*ai-ai*q == -ai, "annihilator charge -1")
        need(q*ai.T-ai.T*q == ai.T, "creator charge +1")

    # Exact two- and normally ordered four-time Wick determinants.
    f1, f2 = [1, 2, -1, 3], [2, -1, 1, 1]
    g1, g2 = [1, -2, 3, 1], [-1, 1, 2, 2]
    t1, t2, s1, s2 = 0, 1, 2, -1
    c1 = timed_creation(a, f1, labels, t1, z)
    c2 = timed_creation(a, f2, labels, t2, z)
    d2 = timed_annihilation(a, g2, labels, s2, z)
    d1 = timed_annihilation(a, g1, labels, s1, z)
    k11 = occupied_kernel(g1, s1, f1, t1, labels, occupied, z)
    k12 = occupied_kernel(g1, s1, f2, t2, labels, occupied, z)
    k21 = occupied_kernel(g2, s2, f1, t1, labels, occupied, z)
    k22 = occupied_kernel(g2, s2, f2, t2, labels, occupied, z)
    two_fock = expectation(c1*d1, vacuum_mask)
    need(sp.simplify(two_fock-k11) == 0, "two-time occupied kernel")
    four_fock = expectation(c1*c2*d2*d1, vacuum_mask)
    four_det = sp.expand(k11*k22-k12*k21)
    need(sp.simplify(four_fock-four_det) == 0, "four-time determinant")

    # Same-source charged pair products: exact exterior-square response.
    pair_labels = [-3, -2, -1, 0]
    pair_occ = [False]*4
    pa = annihilators(4)
    pair_vac = 0
    u1, u2 = [1, 1, 0, 2], [0, 1, -1, 1]
    v1, v2 = [2, 0, 1, 1], [1, -1, 2, 0]
    su1, su2, tv1, tv2 = -1, 2, 1, 3
    pair_word = (timed_annihilation(pa, u2, pair_labels, su2, z)
                 * timed_annihilation(pa, u1, pair_labels, su1, z)
                 * timed_creation(pa, v1, pair_labels, tv1, z)
                 * timed_creation(pa, v2, pair_labels, tv2, z))
    l11 = empty_kernel(u1, su1, v1, tv1, pair_labels, pair_occ, z)
    l12 = empty_kernel(u1, su1, v2, tv2, pair_labels, pair_occ, z)
    l21 = empty_kernel(u2, su2, v1, tv1, pair_labels, pair_occ, z)
    l22 = empty_kernel(u2, su2, v2, tv2, pair_labels, pair_occ, z)
    pair_det = sp.expand(l11*l22-l12*l21)
    need(sp.simplify(expectation(pair_word, pair_vac)-pair_det) == 0,
         "same-source pair four-time determinant")
    need(wedge(u1, u1) == sp.zeros(6, 1), "Pauli diagonal pair vanishes")
    need(wedge(u1, u2) == -wedge(u2, u1), "pair antisymmetry")

    # A label called 'mediator' but represented by the same pair products is
    # a duplicate.  A different wedge vector can be independent as a state,
    # while remaining a composite quadratic field rather than a new species.
    e = [[int(i == j) for i in range(4)] for j in range(4)]
    b1, b2 = wedge(e[0], e[1]), wedge(e[0], e[2])
    m1, m2 = b1, b1+b2
    joint_duplicate = [b1, b2, m1, m2]
    duplicate_gram = gram(joint_duplicate)
    need(duplicate_gram.rank() == 2, "duplicate mediator labels add no states")
    m3 = wedge(e[2], e[3])
    independent_composite_gram = gram([b1, b2, m3])
    need(independent_composite_gram.rank() == 3,
         "a distinct wedge state can be independent but remains composite")

    # First and second pair-time jets are inherited additively from h.
    pair_h = sp.diag(*[sp.Rational(1, 4)-j for j in pair_labels])
    wedge_basis = [(i, j) for i in range(4) for j in range(i+1, 4)]
    h2 = sp.diag(*[pair_h[i, i]+pair_h[j, j] for i, j in wedge_basis])
    bw = sp.Matrix.hstack(b1, b2)
    pair_jets = [bw.T*(h2**n)*bw for n in range(3)]

    # C alone is not a time generator: h_alt has the same invariant sea but
    # a different first and second occupied time jet.
    c = sp.diag(*[int(x) for x in occupied])
    h = sp.diag(*h_values)
    h_alt = h + sp.diag(0, 0, -1, 0)
    need(sp.diag(*[int(bool(h_alt[i, i] < 0)) for i in range(4)]) == c,
         "negative spectral projector itself is unchanged")
    need(c*h == h*c and c*h_alt == h_alt*c, "both dynamics preserve C")
    need(c*h != c*h_alt and c*h**2 != c*h_alt**2,
         "same projector state, different time jets")

    result = {
        "status": "EXACT_SYMBOLIC_SOURCE_CORRELATORS_AND_COMPOSITE_PAIR_BOUNDARY",
        "source_hashes": SOURCES,
        "checks": {
            "finite_CAR_and_integer_charge": True,
            "H_equals_L0_minus_Q_over_4": True,
            "two_time_covariance_kernel": True,
            "four_time_normally_ordered_determinant": True,
            "same_source_pair_multitime_determinant": True,
            "pair_antisymmetry_and_Pauli_zero": True,
            "projector_does_not_determine_time": True,
        },
        "limit_one_particle_data": {
            "labels_j": labels,
            "occupation_C": [int(x) for x in occupied],
            "h_j": [str(x) for x in h_values],
            "r_j": [str(x) for x in r_values],
            "identity": "h_j=r_j-1/4; H=L0-Q/4",
        },
        "symbolic_four_time_laurent_terms": len(sp.Add.make_args(four_det)),
        "symbolic_pair_four_time_laurent_terms": len(sp.Add.make_args(pair_det)),
        "composite_pair_boundary": {
            "pair_space_for_four_empty_modes": 6,
            "duplicate_joint_label_count": 4,
            "duplicate_joint_gram_rank": duplicate_gram.rank(),
            "independent_composite_label_count": 3,
            "independent_composite_gram_rank": independent_composite_gram.rank(),
            "pair_jet_0": [[str(x) for x in row] for row in pair_jets[0].tolist()],
            "pair_jet_1": [[str(x) for x in row] for row in pair_jets[1].tolist()],
            "pair_jet_2": [[str(x) for x in row] for row in pair_jets[2].tolist()],
            "interpretation": "Distinct wedge vectors may be independent states, but every such vector is still a quadratic composite of the one actual CAR field.",
        },
        "candidate_gate": [
            "field_statistics_and_product_law",
            "integer_charge_Ward_identity",
            "joint_state_Gram_and_covariance",
            "occupied_and_empty_first_time_jets",
            "occupied_and_empty_second_time_jets",
        ],
        "not_claimed": [
            "eight_or_ten microscopic channels",
            "independent elementary mediator species",
            "E8 half-charge field",
            "T1-T8 closure",
        ],
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "certificate.json")
    parser.add_argument("--repo", type=Path, default=ROOT)
    args = parser.parse_args()
    ROOT = args.repo
    output = main()
    target = args.output
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))
