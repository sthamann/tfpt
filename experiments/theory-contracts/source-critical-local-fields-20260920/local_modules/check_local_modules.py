#!/usr/bin/env python3
"""Exact audit of the common-T(D8) local modules at the n/z point."""

from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import sympy as S


ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
OUT = Path(__file__).resolve().parent

PINS = {
    "experiments/theory-contracts/source-graded-locality-20260920/PROOF.txt": "669309ea7f240397b2eb49c61e02b5224d4b9d1c15d50aeca30668fa97fa41bb",
    "experiments/theory-contracts/source-graded-locality-20260920/certificate.json": "265bb6e67ea602b612014385e971a5aed6594f31c030c724315a38d896f19982",
    "experiments/theory-contracts/source-graded-locality-20260920/source_manifest.json": "bba930f01eb552bffd3196a83aa39692a1d71951b78534a30948a2a1a6d2140a",
    "experiments/theory-contracts/source-dynamics-selection-20260920/PROOF.txt": "03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2",
    "experiments/theory-contracts/source-dynamics-selection-20260920/certificate.json": "439f93d133024fdea14de0a3a36f4178ad40df36ff66b02bb5a62324031bc159",
    "experiments/theory-contracts/compiler-source-channel-gate-20260918/PROOF.txt": "7c9e47e12d06c94c1ee04bf9881f866fb6901cc59a015dd51bdc62235e9fcf02",
    "experiments/theory-contracts/compiler-source-channel-gate-20260918/certificate.json": "32b907135e6539883a6580a0c9860e0dc1fad806c051434caf0183163b4a9373",
    "experiments/theory-contracts/compiler-native-root-dictionary-20260918/certificate.json": "eecbeefc433356f079a782dd715f011de6b5b27006d386e1dfcad10146ad6d53",
    "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json": "a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3",
    "experiments/theory-contracts/universalraum-fable-kernfragen-20260910/fable-runde3/check_runde3.py": "caa3e9cd15d62e0f6a7904a9809304e224f1d02fba37dfe6782ec541b815b5d4",
    "verification/v1_e8_glue.py": "1978d66a85974e5fa189cf4dec507f9be4c4dcc113e90eb1b33a9aae9259a0d7",
}

checks = Counter()


def ck(name, condition):
    if not bool(condition):
        raise RuntimeError("FAIL: " + name)
    checks[name] += 1


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


for rel, expected in PINS.items():
    ck("source_pin", digest(ROOT / rel) == expected)

K = S.diag(*([1] * 9 + [-1]))
n = S.Matrix([1, 1, 1, -1, -1, -1, -1, -1, -1, 3])
z = S.Matrix([0] * 8 + [1, -1])
a = n[:8, 0]
eye8 = S.eye(8)
eye10 = S.eye(10)
s = S.ones(8, 1) / 2


def bil(x, y):
    return (x.T * K * y)[0]


def T(p):
    k = (a.T * p)[0] / 2
    return S.Matrix(list(p) + [-k, k])


def F_aux(p):
    k = (a.T * p)[0] / 2
    return T(p) - k * n


# Standard D8 basis, then the full common even sublattice M=T(D8)+Zn+Zz.
d8_basis = []
for i in range(7):
    d8_basis.append(eye8[:, i] - eye8[:, i + 1])
d8_basis.append(eye8[:, 6] + eye8[:, 7])
D8 = S.Matrix.hstack(*d8_basis)
M = S.Matrix.hstack(*[T(p) for p in d8_basis], n, z)
GM = M.T * K * M
ck("D8_index_two", abs(D8.det()) == 2)
ck("common_index_four", abs(M.det()) == 4)
ck("common_even_integral", all(x.q == 1 for x in GM) and all(GM[i, i] % 2 == 0 for i in range(10)))

f = eye10[:, 0]
b = S.Matrix([1, 1, 1, 0, 0, 0, 0, 0, 0, 1])
reps = {"0": S.zeros(10, 1), "v": f, "s": b, "c": f + b}
ck("glue_decompositions", f == T(eye8[:, 0]) + z / 2 and b == T(s) + n / 2)
ck("representatives_pair_integrally_with_M", all(bil(r, M[:, j]).q == 1 for r in reps.values() for j in range(10)))
ck("four_distinct_order_two_cosets", len({tuple((M.inv() * r).applyfunc(lambda x: x % 1)) for r in reps.values()}) == 4 and all(all((2 * M.inv() * r)[i].q == 1 for i in range(10)) for r in reps.values()))

norms = {name: bil(r, r) for name, r in reps.items()}
parities = {name: int(norm % 2) for name, norm in norms.items()}
ck("representative_norms", norms == {"0": 0, "v": 1, "s": 2, "c": 5})
ck("whole_coset_parity_table", parities == {"0": 0, "v": 1, "s": 0, "c": 1})

# This makes the all-lattice quantifier exact: for every r+M k, the norm
# differs from r^2 by 2<r,Mk>+(Mk)^2, an even integer.  It is not a finite
# short-vector census.
for name, r in reps.items():
    pairings = [bil(r, M[:, j]) for j in range(10)]
    ck("coset_parity_is_constant", all(x.q == 1 for x in pairings) and all(GM[j, j] % 2 == 0 for j in range(10)))

# Genuine doubled half-root list and the oriented D5+D3 (=D5+A3) split.
native_path = ROOT / "experiments/theory-contracts/compiler-native-root-dictionary-20260918/certificate.json"
native = json.loads(native_path.read_text())
source_halfroots = {tuple(r) for r in native["results"]["native"]["spinor_root_order"]}
generated_s = {signs for signs in product((-1, 1), repeat=8) if sum(x < 0 for x in signs) % 2 == 0}
generated_c = {signs for signs in product((-1, 1), repeat=8) if sum(x < 0 for x in signs) % 2 == 1}
ck("native_s_halfroots_exact", source_halfroots == generated_s and len(generated_s) == 128)
ck("conjugate_c_halfroots", len(generated_c) == 128 and generated_s.isdisjoint(generated_c))

def chirality(signs, sl):
    return sum(x < 0 for x in signs[sl]) % 2

s_branches = Counter()
c_branches = Counter()
for signs in generated_s:
    d5 = "16" if chirality(signs, slice(0, 5)) == 1 else "bar16"
    a3 = "4" if chirality(signs, slice(5, 8)) == 1 else "bar4"
    s_branches[(d5, a3)] += 1
for signs in generated_c:
    d5 = "16" if chirality(signs, slice(0, 5)) == 1 else "bar16"
    a3 = "4" if chirality(signs, slice(5, 8)) == 1 else "bar4"
    c_branches[(d5, a3)] += 1
ck("s_oriented_branch", s_branches == Counter({("16", "4"): 64, ("bar16", "bar4"): 64}))
ck("c_oriented_branch", c_branches == Counter({("16", "bar4"): 64, ("bar16", "4"): 64}))
ck("D5_clock_orients_16", {sum(r[:5]) % 4 for r in generated_s if chirality(r, slice(0, 5)) == 1} == {3} and {sum(r[:5]) % 4 for r in generated_s if chirality(r, slice(0, 5)) == 0} == {1})

vector_weights = []
for j in range(8):
    for sign in (-1, 1):
        vector_weights.append(tuple(sign if i == j else 0 for i in range(8)))
ck("v_branch_10_plus_6", sum(any(r[:5]) for r in vector_weights) == 10 and sum(not any(r[:5]) for r in vector_weights) == 6)

# The parent triality certificate itself keeps the physical D5+A3
# identification open; using it cannot promote this algebraic branch.
triality = json.loads((ROOT / "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json").read_text())
ck("triality_scope_remains_open", any("Identification with source D5+A3" in x for x in triality["open"]))

# Exact dimensions at the selected competition metric.
u, v = (n + z) / 2, (n - z) / 2
Vc = K + 2 * K * v * v.T * K
ck("critical_uv_orthonormal", bil(u, u) == 1 and bil(v, v) == -1 and bil(u, v) == 0 and (u.T * Vc * u)[0] == 1 and (v.T * Vc * v)[0] == 1 and (u.T * Vc * v)[0] == 0)
ck("T_plane_critical_orthogonal", all((T(p).T * Vc * y)[0] == 0 for p in d8_basis for y in (u, v)))

cmin = S.Matrix([S.Rational(1, 2), -S.Rational(1, 2)] + [S.Rational(1, 2)] * 6)
attainers = {
    "0": S.zeros(10, 1),
    "v": T(eye8[:, 0]) + z / 2,
    "s": T(s) + n / 2,
    "c": T(cmin) + u,
}
deltas = {name: S.factor((x.T * Vc * x)[0] / 2) for name, x in attainers.items()}
ck("critical_attainers_integral", all(all(y.q == 1 for y in x) for x in attainers.values()))
ck("critical_module_minima", deltas == {"0": 0, "v": S.Rational(3, 4), "s": S.Rational(5, 4), "c": S.Rational(3, 2)})
ck("c_attainer_same_coset", all(y.q == 1 for y in M.inv() * (reps["c"] - attainers["c"])))
ck("uv_not_microscopic_vertices", not all(y.q == 1 for y in u) and not all(y.q == 1 for y in v))
raw_c = f + b
ck("raw_f_plus_b_full_dimensions", bil(raw_c, raw_c) == 5 and (raw_c.T * Vc * raw_c)[0] / 2 == S.Rational(5, 2))
ck("minimal_c_full_dimensions", bil(attainers["c"], attainers["c"]) == 3 and (attainers["c"].T * Vc * attainers["c"])[0] / 2 == S.Rational(3, 2))

# Embedding boundary.  The T-table cannot be relabelled as a theorem about
# arbitrary F_aux weights: the Cartan pairing changes by -k_a(p)<n,x>.
m = n + eye10[:, 8]
transported = []
for i in range(8):
    ai = a[i]
    ri = eye8[:, i] - ai * a / 2
    transported.append(F_aux(ri) - ai * m == eye10[:, i] and (ri.T * ri)[0] == 2 and bil(eye10[:, i], eye10[:, i]) % 2 == 1)
ck("Faux_original_odd_spinor_weight_countercontrol", all(transported))

Y8 = S.Matrix([-S.Rational(1, 3)] * 3 + [S.Rational(1, 2)] * 2 + [0] * 3)
Y = S.Matrix(list(Y8) + [1, 1])
q = lambda x: sum(x)
ck("charges_carried_by_T_plane", all(q(T(p)) == sum(p) and Y.dot(T(p)) == Y8.dot(p) for p in d8_basis))
ck("neutral_plane_really_neutral", q(n) == q(z) == 0 and Y.dot(n) == Y.dot(z) == 0)
xu, xv = T(cmin) + u, T(cmin) + v
ck("explicit_integral_odd_c_pair", all(y.q == 1 for y in xu) and all(y.q == 1 for y in xv) and bil(xu, xu) % 2 == bil(xv, xv) % 2 == 1)
ck("explicit_c_charge_family_type", q(xu) == q(xv) == 3 and Y.dot(xu) == Y.dot(xv) == S.Rational(1, 3) and chirality(tuple(int(2 * y) for y in cmin), slice(0, 5)) == 1 and chirality(tuple(int(2 * y) for y in cmin), slice(5, 8)) == 0)

result = {
    "research_id": "UR.SOURCE.LOCAL_MODULES.01",
    "verdict": "PARTIAL",
    "mathematical_verdict": "EXACT_COMMON_TD8_PARITY_BRANCHING_AND_CRITICAL_MODULE_MINIMA",
    "source_pins": PINS,
    "checks": dict(sorted(checks.items())),
    "common_TD8_parity": {"0": "even", "v": "odd", "s": "even", "c": "odd"},
    "oriented_D5_A3": {
        "v_odd": ["(10,1)", "(1,6)"],
        "s_even": ["(16,4)", "(bar16,bar4)"],
        "c_odd": ["(16,bar4)", "(bar16,4)"],
        "orientation": "native degree convention: lambda=(+1/2)^8 is in (bar16,bar4); D5 clock exponent 3 labels 16 and exponent 1 labels bar16",
    },
    "critical_Vc_module_minima": {"0": "0", "v": "3/4", "s": "5/4", "c": "3/2"},
    "minimal_odd_local_modules": {
        "v": "h=3/4, (10,1)+(1,6), including required neutral half-lattice dressing",
        "c": "h=3/2, (16,bar4)+(bar16,4), spinor projection times a neutral critical u/v dressing",
    },
    "explicit_odd_c_fields": {
        "p": ["1/2", "-1/2", "1/2", "1/2", "1/2", "1/2", "1/2", "1/2"],
        "T(p)+u": [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        "T(p)+v": [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        "parity": "odd",
        "q": 3,
        "Y": "1/3",
        "family_type": "(16,bar4)",
        "Delta_Vc": "3/2",
    },
    "raw_c_representative_control": {
        "f_plus_b_K_norm": 5,
        "f_plus_b_spin": "5/2",
        "f_plus_b_Delta_Vc": "5/2",
        "minimal_c_K_norm": 3,
        "minimal_c_plus_u_spin": "3/2",
        "minimal_c_plus_v_K_norm": 1,
        "minimal_c_plus_v_spin": "1/2",
        "minimal_c_Delta_Vc": "3/2"
    },
    "scope": "Fixed Gamma=Z^(9,1), microscopic parity, selected Vc, and oriented common T(D8) inclusion. No continuum field-selection or four-dimensional interpretation.",
    "embedding_warning": "The parity table labels common T(D8) discriminant classes only. F_aux(p)=T(p)-k_a(p)n changes Cartan weights on general Gamma fields; original e_i are odd although they have F_aux spinor-root weights.",
    "not_claimed": [
        "u or v is an independent microscopic local field",
        "h=3/2 is a four-dimensional Weyl scaling dimension",
        "the odd c module is dynamically light or selected",
        "a universal TFPT spinor/parity no-go",
    ],
}

(OUT / "certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "research_id": result["research_id"], "checks": sum(checks.values()), "verdict": result["verdict"]}, sort_keys=True))
