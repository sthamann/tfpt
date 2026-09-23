#!/usr/bin/env python3
"""Exact small-model checks for the conditional Q<=4 reconstruction theorem.

The script uses SymPy integers and radicals only.  It checks four points:

1. c, h, Omega, T1 and T2 are read directly from the Q<=4 compression.
2. The low-charge defect D4 equals the filled-state defect D_F once m>=3
   terms have already been excluded.
3. A direct T2 matrix element occurs in H, whereas two successive T1 events
   first occur in H**2.
4. A positive function of N_f can vanish on Q<=4 and change higher sectors,
   showing why the global lower-response hypotheses cannot be dropped.
"""

from __future__ import annotations

import json
from itertools import combinations
from math import comb

import sympy as sp


NF = 4
NB = 1
QMAX = 4


def require(condition, message):
    if not bool(condition):
        raise RuntimeError(message)


def qcharge(state):
    mask, bos = state
    return mask.bit_count() + 2 * sum(bos)


BASIS = []
for mask in range(1 << NF):
    for n0 in range(QMAX // 2 + 1):
        state = (mask, (n0,))
        if qcharge(state) <= QMAX:
            BASIS.append(state)
BASIS.sort(key=lambda s: (qcharge(s), s[0], s[1]))
INDEX = {state: k for k, state in enumerate(BASIS)}


def f_ann(state, i):
    mask, bos = state
    if not (mask >> i) & 1:
        return None
    sign = -1 if (mask & ((1 << i) - 1)).bit_count() % 2 else 1
    return (mask ^ (1 << i), bos), sp.Integer(sign)


def f_cre(state, i):
    mask, bos = state
    if (mask >> i) & 1:
        return None
    sign = -1 if (mask & ((1 << i) - 1)).bit_count() % 2 else 1
    return (mask | (1 << i), bos), sp.Integer(sign)


def b_ann(state, a=0):
    mask, bos = state
    if bos[a] == 0:
        return None
    out = list(bos)
    factor = sp.sqrt(out[a])
    out[a] -= 1
    return (mask, tuple(out)), factor


def b_cre(state, a=0):
    mask, bos = state
    out = list(bos)
    factor = sp.sqrt(out[a] + 1)
    out[a] += 1
    return (mask, tuple(out)), factor


def apply_ops(state, ops):
    """Apply a list of elementary operations in right-to-left order."""
    factor = sp.Integer(1)
    current = state
    for op, idx in ops:
        result = {"fa": f_ann, "fc": f_cre, "ba": b_ann, "bc": b_cre}[op](current, idx)
        if result is None:
            return None
        current, value = result
        factor *= value
    return current, sp.simplify(factor)


def add_term(matrix, coefficient, ops):
    for col, state in enumerate(BASIS):
        result = apply_ops(state, ops)
        if result is None:
            continue
        out, factor = result
        row = INDEX.get(out)
        if row is not None:
            matrix[row, col] += coefficient * factor


def build_h(c, h, omega, c1, c2):
    dim = len(BASIS)
    matrix = sp.zeros(dim)
    matrix += c * sp.eye(dim)

    for i in range(NF):
        for j in range(NF):
            add_term(matrix, h[i, j], [("fa", j), ("fc", i)])
    add_term(matrix, omega, [("ba", 0), ("bc", 0)])

    for (i, j), value in c1.items():
        # b^dagger f_j f_i and its adjoint.
        add_term(matrix, value, [("fa", i), ("fa", j), ("bc", 0)])
        add_term(matrix, value, [("ba", 0), ("fc", j), ("fc", i)])

    if c2:
        # (b^dagger)^2 f_3 f_2 f_1 f_0 and its adjoint.
        add_term(
            matrix,
            c2,
            [("fa", 0), ("fa", 1), ("fa", 2), ("fa", 3), ("bc", 0), ("bc", 0)],
        )
        add_term(
            matrix,
            c2,
            [("ba", 0), ("ba", 0), ("fc", 3), ("fc", 2), ("fc", 1), ("fc", 0)],
        )

    require(matrix == matrix.T, "constructed Hamiltonian must be self-adjoint")
    return matrix


def ket_index(mask, bosons=0):
    return INDEX[(mask, (bosons,))]


c = sp.Integer(11)
h = sp.Matrix(
    [
        [2, 1, 0, -1],
        [1, 3, 2, 0],
        [0, 2, 5, 1],
        [-1, 0, 1, 7],
    ]
)
omega = sp.Integer(13)
c1 = {pair: sp.Integer(k + 1) for k, pair in enumerate(combinations(range(NF), 2))}
c2 = sp.Integer(7)
H = build_h(c, h, omega, c1, c2)

vac = ket_index(0, 0)
require(H[vac, vac] == c, "vacuum block must recover c")
for i in range(NF):
    for j in range(NF):
        require(
            H[ket_index(1 << i), ket_index(1 << j)] - c * (i == j) == h[i, j],
            "one-fermion block must recover h",
        )
require(H[ket_index(0, 1), ket_index(0, 1)] - c == omega, "one-boson block must recover Omega")
for pair, value in c1.items():
    mask = (1 << pair[0]) | (1 << pair[1])
    require(H[ket_index(0, 1), ket_index(mask, 0)] == value, "Q=2 cross block must recover T1")
require(
    sp.simplify(H[ket_index(0, 2), ket_index((1 << NF) - 1, 0)] / sp.sqrt(2)) == c2,
    "Q=4 cross block must recover T2 with normalized boson factorial",
)

# D4 = D_F in the stable m<=2 class.
w = {pair: sp.Integer(value) for pair, value in zip(combinations(range(NF), 2), [1, -2, 3, 1, 0, -1])}
w_norm = sum(value**2 for value in w.values())
inner_wc = sum(w[pair] * c1[pair] for pair in c1)
d4 = sp.simplify(sum(value**2 for value in c1.values()) - inner_wc**2 / w_norm + 2 * c2**2)

filled = ket_index((1 << NF) - 1, 0)
hf = H[:, filled]
ef = H[filled, filled]
residual = hf.copy()
residual[filled, 0] -= ef
v = sp.zeros(len(BASIS), 1)
for pair, value in w.items():
    mask = ((1 << NF) - 1) ^ (1 << pair[0]) ^ (1 << pair[1])
    # Apply the actual forward monomial to retain its CAR sign.
    result = apply_ops(((1 << NF) - 1, (0,)), [("fa", pair[0]), ("fa", pair[1]), ("bc", 0)])
    out, sign = result
    require(out[0] == mask, "filled-state pair annihilation must create the complementary holes")
    v[INDEX[out], 0] += value * sign
require((v.T * v)[0] == w_norm, "filled-state W direction must have Hilbert-Schmidt norm")
df = sp.simplify((residual.T * residual)[0] - (v.T * residual)[0] ** 2 / w_norm)
require(sp.simplify(d4 - df) == 0, "D4 must equal the filled-state defect in the m<=2 class")

# Direct T2 versus sequential T1.
seq_c1 = {pair: sp.Integer(0) for pair in combinations(range(NF), 2)}
seq_c1[(0, 1)] = 1
seq_c1[(2, 3)] = 1
Hseq = build_h(sp.Integer(0), sp.zeros(NF), sp.Integer(0), seq_c1, sp.Integer(0))
direct = Hseq[ket_index(0, 2), filled]
sequential = (Hseq * Hseq)[ket_index(0, 2), filled]
require(direct == 0, "a pure T1 model must have zero direct four-fermion/two-boson block")
require(sequential != 0, "two successive T1 events must be visible in H squared")

# Stable hidden high-sector term: p(N_f)=product_{j=0}^4(N_f-j).
p_values = {n: sp.prod(n - j for j in range(5)) for n in range(6)}
require(all(p_values[n] == 0 for n in range(5)), "hidden term must vanish for Nf<=4")
require(p_values[5] == 120, "hidden term must first appear at Nf=5")
require(all(value >= 0 for value in p_values.values()), "hidden term must be positive")

result = {
    "status": "PASS",
    "arithmetic": "exact SymPy integers and radicals",
    "small_model": {"n_f": NF, "n_b": NB, "q_max": QMAX, "dimension": len(BASIS)},
    "recovered": ["c", "h", "Omega", "T1", "T2"],
    "D4": str(d4),
    "D_F": str(df),
    "D4_equals_DF": bool(d4 == df),
    "direct_T2_block_for_sequential_model": str(direct),
    "H_squared_sequential_block": str(sequential),
    "hidden_positive_term": {str(k): str(vv) for k, vv in p_values.items()},
    "native_Q4_C2_shape": [comb(60 + 1, 2), comb(64, 4)],
}
print(json.dumps(result, indent=2, sort_keys=True))
