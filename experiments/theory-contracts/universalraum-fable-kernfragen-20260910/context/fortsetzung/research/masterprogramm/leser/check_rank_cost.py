#!/usr/bin/env python3
"""Small exact counterexamples; no original research scripts are executed."""
import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

checks = []


def check(label, condition):
    assert condition, label
    checks.append(label)


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][c]
        a[r] = [x / divisor for x in a[r]]
        for i in range(len(a)):
            if i != r:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def infnorm(a):
    return max(sum(map(abs, row)) for row in a)


M = [[F(x, 2) for x in row] for row in
     [[0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0]]]
check("all four preparation rows are probability distributions", all(sum(r) == 1 for r in M))
check("ordinary linear rank is exactly three", rank(M) == 3)
check("signed row relation r3=r0+r2-r1", M[3] == [x + y - z for x, y, z in zip(M[0], M[2], M[1])])
fooling = [(0, 2), (1, 3), (2, 0), (3, 1)]
for i, j in fooling:
    check(f"fooling entry {(i, j)} is positive", M[i][j] > 0)
for (i, j), (k, l) in combinations(fooling, 2):
    check(f"pair {(i,j),(k,l)} cannot share positive rank-one support", M[i][l] * M[k][j] == 0)
# A nonnegative factorization M=sum_h u_h v_h^T has no cancellation at
# zero entries. Each rank-one support is a rectangle and hence contains
# at most one fooling entry. Therefore four positive summands are needed.
I4 = [[F(i == j) for j in range(4)] for i in range(4)]
check("four nonnegative hidden states suffice", mul(I4, M) == M)

precision_examples = []
for m in [1, 2, 8, 64, 1024]:
    delta = F(1, 2**m)
    B = [[F(1), F(1)], [F(0), delta]]
    Binv = [[F(1), -1 / delta], [F(0), 1 / delta]]
    check(f"m={m}: exact rank remains two", rank(B) == 2)
    check(f"m={m}: explicit exact inverse", mul(B, Binv) == [[1, 0], [0, 1]])
    check(f"m={m}: exact infinity norm condition number", infnorm(B) * infnorm(Binv) == 2 * (1 + 2**m))
    # An error delta/4 in the second observed coordinate changes the
    # recovered second source coordinate by exactly 1/4.
    check(f"m={m}: reconstruction error amplification", mul(Binv, [[F(0)], [delta / 4]])[1][0] == F(1, 4))
    check(f"m={m}: denominator bit length", delta.denominator.bit_length() == m + 1)
    precision_examples.append({"m": m, "rank": 2, "denominator_bits": m + 1,
                               "required_absolute_error_for_output_quarter": f"2^(-{m + 2})",
                               "condition_infinity": f"2*(1+2^{m})"})

out = {"status": "EXACT_SCOPED_CHECKS_PASS", "count": len(checks), "checks": checks,
       "linear_rank": 3, "nonnegative_rank": 4,
       "nonnegative_rank_scope": "Classical hidden state preparation/readout factorization only; no quantum dimension claim.",
       "precision_examples": precision_examples,
       "hypothetical_37_dimension_was_measured": False,
       "original_campaigns_rerun": False,
       "new_general_factoring_RH_or_P_NP_result": False}
Path(__file__).with_name("rank-cost-checks.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"status": out["status"], "count": out["count"]}))
