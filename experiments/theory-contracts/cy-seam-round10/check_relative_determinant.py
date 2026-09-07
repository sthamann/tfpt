"""Exact arithmetic checks for RELATIVE_DETERMINANT.md.

Standard library only. Prints JSON; writes no files. The checker verifies
finite/algebraic consequences of the geometric hypotheses stated in the note,
not an analytic determinant comparison or a physical spectrum.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import permutations
import json


def dot(u, v):
    # Ordered geometric divisor basis P, O, F.
    gram = ((-1, 0, 1), (0, -1, 1), (1, 1, 0))
    return sum(u[i] * gram[i][j] * v[j] for i in range(3) for j in range(3))


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def scale(n, v):
    return tuple(n * a for a in v)


def mm(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def transpose(A):
    return list(map(list, zip(*A)))


def det(A):
    total = 0
    for perm in permutations(range(len(A))):
        inversions = sum(perm[i] > perm[j] for i in range(len(A)) for j in range(i + 1, len(A)))
        term = (-1) ** inversions
        for i, j in enumerate(perm):
            term *= A[i][j]
        total += term
    return total


def char_shift(v, shift):
    answer = [0] * 4
    for j, coefficient in enumerate(v):
        answer[(j + shift) % 4] += coefficient
    return answer


def wedge(A, B):
    result = defaultdict(Fraction)
    for xs, a in A.items():
        for ys, b in B.items():
            if set(xs) & set(ys):
                continue
            seq = xs + ys
            inversions = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))
            result[tuple(sorted(seq))] += a * b * (-1) ** inversions
    return dict(result)


def main():
    fibre = (0, 0, 1)
    canonical = (0, 0, -1)
    D = (1, -1, -1)
    assert dot(D, fibre) == 0
    assert dot(D, (0, 1, 0)) == 0
    assert dot(D, D) == -2
    table = []
    for n in (-5, -3, -2, -1, 1, 2, 3, 5):
        assert n % 4 != 0
        for q in (-7, -1, 0, 1, 9):
            E = add(scale(n, D), scale(q, fibre))
            chi = 1 + Fraction(dot(E, add(E, scale(-1, canonical))), 2)
            assert chi == 1 - n * n
            assert -chi == n * n - 1
        if n > 0:
            table.append({"n": n, "restriction_power_mod4": n % 4,
                          "D_square": -2 * n * n, "chi": 1 - n * n,
                          "h": [0, n * n - 1, 0]})
    assert 1 % 4 == 5 % 4
    assert 1 - 5 * 5 == -24
    family = {"base": "P1", "twist": "O(1)", "bulk_degree": -24,
              "canonical_twisted_bulk_degree": -24, "boundary_degree": 0}
    assert family["bulk_degree"] - family["canonical_twisted_bulk_degree"] == family["boundary_degree"]
    assert family["bulk_degree"] != family["boundary_degree"]

    # Serre duality: exponent of det H^p(V^vee) in lambda(V K).
    exponents = [-(1 if (2 - p) % 2 == 0 else -1) for p in range(3)]
    assert exponents == [-1, 1, -1]  # lambda(V^vee)^{-1}

    # E_i[4] written as (Z/4)^2; pullback sends P to -iP.
    torsion_orbits = []
    for a in range(4):
        for b in range(4):
            P = (a, b)
            T = (2 * a % 4, 2 * b % 4)
            iT = (-T[1] % 4, T[0])
            if T == (0, 0) or iT == T:
                continue
            orbit = [P]
            for _ in range(3):
                x, y = orbit[-1]
                orbit.append((y, -x % 4))
            assert len(set(orbit)) == 4
            assert (0, 0) not in orbit
            for j in range(4):
                assert tuple((orbit[j][k] + orbit[(j + 2) % 4][k]) % 4 for k in range(2)) == (0, 0)
            torsion_orbits.append(orbit)
    assert len(torsion_orbits) == 8

    C = [[int(i == (j + 1) % 4) for j in range(4)] for i in range(4)]
    I = [[int(i == j) for j in range(4)] for i in range(4)]
    B = [[int((i - j) % 4 == 2) for j in range(4)] for i in range(4)]
    assert mm(mm(C, C), mm(C, C)) == I
    assert det(C) == -1
    assert transpose(B) == B and det(B) != 0
    assert mm(mm(transpose(C), B), C) == B
    # Twisting all four eigencharacters by chi^k cannot change det=-1.
    assert all(sum((j + k) % 4 for j in range(4)) % 4 == 2 for k in range(4))
    # The only holomorphic alternating forms pair opposite summands.
    for a in (-2, -1, 0, 1, 2):
        for b in (-2, -1, 0, 1, 2):
            A = [[0] * 4 for _ in range(4)]
            A[0][2], A[2][0], A[1][3], A[3][1] = a, -a, b, -b
            invariant = mm(mm(transpose(C), A), C) == A
            assert invariant == (a == b == 0)

    H0 = [0, 1, 1, 1]
    H1 = char_shift(H0, -1)
    equiv_index = [a - b for a, b in zip(H0, H1)]
    assert H1 == [1, 1, 1, 0]
    assert equiv_index == [-1, 0, 0, 1]
    assert sum(H0) == sum(H1) == 3
    assert sum(equiv_index) == 0 and equiv_index[0] == -1

    # Forms ordered as a,b,alpha,beta; c1(Poin)=a^beta-b^alpha.
    c1 = {(0, 3): Fraction(1), (1, 2): Fraction(-1)}
    c1sq = wedge(c1, c1)
    assert c1sq == {(0, 1, 2, 3): Fraction(-2)}
    integrated_half_square = c1sq[(0, 1, 2, 3)] / 2
    assert integrated_half_square == -1

    print(json.dumps({"status": "PASS", "cohomology_under_stated_geometric_hypotheses": table,
                      "same_boundary_family_counterexample": family,
                      "serre_dual_determinant_exponents": exponents,
                      "number_of_order4_points_with_nonfixed_double": len(torsion_orbits),
                      "orbit_lift_determinant": det(C), "symmetric_pairing_invariant": True,
                      "End0_H0_character_multiplicities": H0,
                      "End0_H1_character_multiplicities": H1,
                      "End0_equivariant_index": equiv_index,
                      "Poincare_integrated_half_square_coefficient": int(integrated_half_square),
                      "scope": "Exact finite and intersection arithmetic only; no analytic or physical closure."},
                     indent=2))


if __name__ == "__main__":
    main()

