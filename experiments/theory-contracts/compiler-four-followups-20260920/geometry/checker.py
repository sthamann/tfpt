#!/usr/bin/env python3
"""Exact operational-response test on the native two-source branch.

The native inputs are pinned.  The three-qubit calculation is only a small
locality-preserving control for the commutator-order criterion; it is not a
TFPT model.  All TFPT conclusions come from the pinned two-source and
three-source matrices.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

PINS = {
    "experiments/theory-contracts/compiler-bond-response-20260919/PROOF.txt":
        "67e3d788c0bfe6169bde878a6ebf431dd8c4bc6520620738253ed22eb4587e2a",
    "experiments/theory-contracts/compiler-bond-response-20260919/checker.py":
        "62fd8bb8184ba6e6b9d9c73f4e4692cc409b65616abc2b035a76ba18bd781df6",
    "experiments/theory-contracts/compiler-bond-response-20260919/triple_response.py":
        "6851daaa3ae4e575a7d8d6657384c1cb17863d44fc1b502157968c6019514a97",
    "experiments/theory-contracts/compiler-bond-response-20260919/triple_response.json":
        "f9471c23376e0359e2d5d9f0c105d1b7e5266a1d1437f7c0279027781a234dc2",
    "experiments/theory-contracts/compiler-relaxed-wall-20260919/contract_index.json":
        "479ba50d2289f2ca4a1434a3d1702d689a75a69eb293b437949c0d122d87ff1e",
    "experiments/theory-contracts/compiler-relaxed-wall-20260919/pair22_audit.json":
        "495107144114e889f4a8c5396bc01012c4cde3cf242b00f8d481d810d7b82e34",
    "experiments/theory-contracts/compiler-domain-wall-core-20260919/PROOF.txt":
        "fe9c66ef6821ff4771993cc899dd7ea385b3ad87a45712e831d12cc190c9ddb6",
}

checks: list[str] = []


def require(condition: bool, name: str) -> None:
    if not bool(condition):
        raise RuntimeError(name)
    checks.append(name)


def comm(a: s.Matrix, b: s.Matrix) -> s.Matrix:
    return s.simplify(a * b - b * a)


def ad(h: s.Matrix, a: s.Matrix, n: int) -> s.Matrix:
    out = a
    for _ in range(n):
        out = comm(h, out)
    return s.simplify(out)


def kron(*items: s.Matrix) -> s.Matrix:
    out = s.Matrix([[1]])
    for item in items:
        out = s.kronecker_product(out, item)
    return out


for rel, expected in PINS.items():
    actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
    require(actual == expected, f"source pin {rel}")

relaxed = json.loads((ROOT / "experiments/theory-contracts/compiler-relaxed-wall-20260919/contract_index.json").read_text())
pair22 = json.loads((ROOT / "experiments/theory-contracts/compiler-relaxed-wall-20260919/pair22_audit.json").read_text())
triple = json.loads((ROOT / "experiments/theory-contracts/compiler-bond-response-20260919/triple_response.json").read_text())
require(relaxed["verdict"] == "PARTIAL", "relaxed-wall verdict retained")
require("EXACT_FULL_TWO_SOURCE_GROUND_DOUBLET_AND_GAP" in relaxed["mathematical_verdict"],
        "native full two-source premise recorded")
require(pair22["status"] == "PASS" and pair22["exact"]["full_q22_floor"] == "3/5",
        "native q22 exact audit pin")
require(triple["status"] == "PASS" and triple["verdict"] == "PARTIAL",
        "three-source scope retained")
finite_gap_endpoint = s.Rational(247, 222400)
finite_w_lower = s.Rational(1, 8) - s.Rational(3, 47) - s.Rational(6, 139)
require(finite_gap_endpoint > s.Rational(1, 1600), "full weak-branch gap endpoint")
require(finite_w_lower == s.Rational(941, 52264) and finite_w_lower > 0,
        "full weak-branch response lower bound")

# Pauli conventions and the exact projected weak-branch generator of .24.
I = s.I
one = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -I], [I, 0]])
sz = s.diag(1, -1)
mu, t = s.symbols("mu t", positive=True, real=True)
h_eff = -mu * sx / 8  # scalar terms do not affect Heisenberg response
D = sz                 # bond-pattern population imbalance O_D
W = -sy / 8            # native neutral bilinear quadrature
Pg = (one + sx) / 2    # lower line of h_eff for mu>0
rho_mix = one / 2

require(I * comm(h_eff, D) == 2 * mu * W, "native binding-current equation")
require(comm(D, W) == I * sx / 4, "native conjugate bond quadratures")
require(Pg * Pg == Pg and s.trace(Pg) == 1, "projected ground line")
require(s.trace(Pg * D) == 0 and s.trace(Pg * W) == 0, "zero one-point functions")
sym_cov = s.simplify(s.trace(Pg * (D * W + W * D) / 2))
require(sym_cov == 0, "zero static symmetrized cross correlation")

theta = mu * t / 4
D_t = s.cos(theta) * sz - s.sin(theta) * sy
cross_comm = comm(D_t, W)
cross_response = s.simplify(-I * s.trace(Pg * cross_comm))
require(cross_comm == I * s.cos(theta) * sx / 4, "exact effective Heisenberg commutator")
require(cross_response == s.cos(theta) / 4, "nonzero retarded cross response")
require(s.simplify(-I * s.trace(rho_mix * cross_comm)) == 0,
        "maximally mixed state is response-blind")
require(cross_comm != s.zeros(2), "operator response survives state blind spot")

# The four matrices span M2: D and W are two quadratures of one operational
# cell, not commuting observables of two disjoint sites.
span = s.Matrix.hstack(*[m.reshape(4, 1) for m in (one, D, W, comm(D, W))])
require(span.rank() == 4, "native bond observables generate full M2")
require(comm(D, W) != s.zeros(2), "native bond observables are not disjoint local algebras")

# Minimal locality-preserving control.  For a 1--2--3 nearest-neighbour chain,
# endpoint response vanishes through order one and first appears at order two.
X, Z = sx, sz
# The two edge terms must act noncommutatively on site 2; otherwise a real
# path can be dynamically dark, which is precisely the cancellation caveat.
H_chain = kron(X, Z, one) + kron(one, X, X)
A1 = kron(Z, one, one)
B3 = kron(one, one, Z)
orders_chain = [comm(ad(H_chain, A1, n), B3) for n in range(3)]
require(orders_chain[0] == s.zeros(8), "control separated algebras commute")
require(orders_chain[1] == s.zeros(8), "control distance-two order-one vanishes")
require(orders_chain[2] != s.zeros(8), "control distance-two order-two survives")
H_shortcut = H_chain + kron(X, one, X)
require(comm(ad(H_shortcut, A1, 1), B3) != s.zeros(8),
        "control direct edge appears at order one")

# Exact native support audit.  Q1 and Q3 have disjoint full tensor supports,
# but the middle Hamiltonian term L2 touches B and C and therefore touches
# both regions.  Order-one cross-response is allowed by the actual hypergraph;
# the bare source-label chain is not the relevant support graph.
Q1_support = frozenset({"R1", "A", "B"})
Q3_support = frozenset({"R3", "C", "D"})
L2_support = frozenset({"R2", "B", "C"})
require(Q1_support.isdisjoint(Q3_support), "native outer packet supports disjoint")
require(bool(L2_support & Q1_support) and bool(L2_support & Q3_support),
        "native middle term touches both packet regions")

# A nontrivial projector on either of two disjoint tensor factors gives
# distinct commuting full operators.  This 2x2 representative checks the
# dimension-independent tensor-algebra statement used for the actual packet
# projectors, whose local dimensions are larger.
q_local = s.diag(1, 0)
Q1_full_control = kron(q_local, one)
Q3_full_control = kron(one, q_local)
require(comm(Q1_full_control, Q3_full_control) == s.zeros(4),
        "disjoint nontrivial projectors commute")
require(Q1_full_control - Q3_full_control != s.zeros(4),
        "disjoint nontrivial projectors are distinct")

# Exact native three-source invariant block from .24.  Q1 and Q3 compress to
# the same projector.  This proves noninjectivity of the compression on their
# operator system, but the early response does not prove loss of full-model
# locality because L2 already bridges their extended supports.
sqrt15 = s.sqrt(15)
H_B = s.Matrix([[15, -sqrt15], [-sqrt15, 49]]) / 20
Q = s.diag(1, 0)
alias_order0 = comm(Q, Q)
alias_order1 = comm(ad(H_B, Q, 1), Q)
require(alias_order0 == s.zeros(2), "native endpoint alias order zero")
require(alias_order1 == -sqrt15 * sx / 20, "native endpoint alias order one")
require(alias_order1.rank() == 2, "native endpoint alias response nonzero")
require(Q - Q == s.zeros(2), "native compressed projector difference vanishes")

lo = (8 - s.sqrt(19)) / 5
hi = (8 + s.sqrt(19)) / 5
gap = s.simplify(hi - lo)
P_lower = s.simplify((hi * one - H_B) / gap)
P_upper = one - P_lower
weight = s.simplify(s.trace(P_lower * Q * P_upper * Q))
covariance = s.simplify(s.trace(P_lower * Q) - s.trace(P_lower * Q) ** 2)
require(weight == s.Rational(15, 1216), "native exact inelastic weight")
require(covariance == weight, "native static endpoint alias covariance")
require(gap == 2 * s.sqrt(19) / 5, "native exact invariant-block frequency")
require(triple["exact_invariant_space"]["Q1_and_Q3"] == "diag(1,0)",
        "native endpoint projector alias source pin")
require(triple["exact_invariant_space"]["retarded_cross_response"] ==
        "-15/608 theta(t) sin(2sqrt19 kappa t/5)",
        "native retarded response source pin")

result = {
    "status": "PASS",
    "verdict": "PARTIAL_EXACT_OPERATIONAL_SINGLE_CELL_AND_COMPRESSION_NONINJECTIVITY",
    "checks": len(checks),
    "guard_names": checks,
    "native_inputs": {
        "full_two_source_H0": {
            "ground_energy_over_kappa": "1/2",
            "multiplicity": 2,
            "gap_over_kappa": "1/10",
            "evidence": "pinned .26 contract; exact full-space theorem is reused, not independently replayed here",
        },
        "weak_branch": {
            "H_eff_mod_scalars": "-mu sigma_x/8",
            "O_D": "sigma_z",
            "W": "-sigma_y/8",
            "scope": "exact projected leading generator; .24 full finite-epsilon Schur bounds become applicable once .26 supplies Assumption G",
            "full_gap_lower_at_epsilon_1_over_200_over_kappa": "247/222400",
            "full_W_transition_lower_at_epsilon_le_1_over_200": "941/52264",
        },
        "three_source_invariant_block": {
            "H_over_kappa": "[[15,-sqrt(15)],[-sqrt(15),49]]/20",
            "Q1": "diag(1,0)",
            "Q3": "diag(1,0)",
            "scope": "exact invariant block only; no independently replayed full-ground complement theorem",
        },
    },
    "controlled_two_source_response": {
        "static_symmetrized_covariance_OD_W": "0",
        "operator_commutator_OD_t_W": "i cos(mu t/4) sigma_x/4",
        "ground_retarded_response": "cos(mu t/4)/4",
        "maximally_mixed_retarded_response": "0",
        "generated_algebra": "M2",
        "operational_content": "one relational two-level cell, not two commuting spatial sites",
    },
    "commutator_order_control": {
        "nearest_neighbour_chain_1_2_3": ["zero", "zero", "nonzero"],
        "orders": [0, 1, 2],
        "direct_1_3_shortcut_order_one": "nonzero",
        "scope": "minimal declared control for the support-order theorem; not a TFPT model",
    },
    "native_support_audit": {
        "elementary_factors": ["R1", "R2", "R3", "A", "B", "C", "D"],
        "Q1_support": ["R1", "A", "B"],
        "Q3_support": ["R3", "C", "D"],
        "L2_support": ["R2", "B", "C"],
        "Q1_Q3_full_supports_disjoint": True,
        "L2_touches_both_regions": True,
        "order_one_cross_response_allowed": True,
        "conclusion": "source-label distance two is not a commutator lower bound for these extended packet observables",
    },
    "native_compression_noninjectivity": {
        "compressed_Q1_equals_Q3": True,
        "full_Q1_minus_Q3_nonzero": True,
        "compressed_Q1_minus_Q3_zero": True,
        "first_nonzero_nested_commutator_order": 1,
        "order_one_operator": "-sqrt(15) sigma_x/20",
        "static_covariance_in_lower_invariant_state": "15/1216",
        "retarded_response": "-15/608 theta(t) sin(2sqrt(19) kappa t/5)",
        "conclusion": "the invariant compression is nonfaithful on span{I,Q1,Q3}; early response is support-compatible and is not itself a locality obstruction",
    },
    "first_missing_map": {
        "name": "injective operational localization net",
        "required": "injective embeddings iota_i:A_i->B(H_phys) of pairwise commuting full local algebras plus H=sum_Z h_Z",
        "current_obstruction": "on the exact three-source block P Q1 P=P Q3 P although Q1 and Q3 are distinct commuting full operators, so the compressed observable map is not injective",
        "low_energy_requirement": "a uniform Heisenberg-response preservation bound for the compression, not only spectral or eigenvector control",
    },
    "not_claimed": [
        "physical spatial metric",
        "three-dimensional geometry",
        "relativistic light cone",
        "full three-source ground theorem",
        "full finite-epsilon response formula",
        "T1-T8 closure",
        "TOE",
    ],
    "source_pins": PINS,
}

(HERE / "results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
