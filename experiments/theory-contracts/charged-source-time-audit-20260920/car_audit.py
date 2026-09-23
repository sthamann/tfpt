#!/usr/bin/env python3
"""Independent finite-window CAR audit.

All Fock-space coefficients are integers.  Operators and vectors are sparse
dictionaries; no floating point number enters the algebraic checks.  Floating
point is used only to sample the separately proved sine-dispersion bound.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


class Fock:
    def __init__(self, M: int, flavors: int = 2):
        self.M = M
        self.flavors = flavors
        # Store twice the half-integer mode, so all labels remain exact ints.
        self.modes2 = tuple(range(-2 * M + 1, 2 * M, 2))
        self.index = {
            (a, r2): a * len(self.modes2) + j
            for a in range(flavors)
            for j, r2 in enumerate(self.modes2)
        }
        self.n_orbitals = flavors * len(self.modes2)
        self.vacuum = sum(
            1 << self.index[a, r2]
            for a in range(flavors)
            for r2 in self.modes2
            if r2 < 0
        )

    def step(self, state: int, kind: str, orbital: int):
        occupied = (state >> orbital) & 1
        if kind == "ann":
            if not occupied:
                return None
            new_state = state ^ (1 << orbital)
        else:
            if occupied:
                return None
            new_state = state | (1 << orbital)
        sign = -1 if (state & ((1 << orbital) - 1)).bit_count() % 2 else 1
        return new_state, sign

    def apply_monomial(self, state: int, ops):
        coeff = 1
        current = state
        # ops are written in operator order, hence act right-to-left.
        for kind, a, r2 in reversed(ops):
            ans = self.step(current, kind, self.index[a, r2])
            if ans is None:
                return None
            current, sign = ans
            coeff *= sign
        return current, coeff

    def describe(self, state: int):
        deviations = []
        for a in range(self.flavors):
            for r2 in self.modes2:
                bit = (state >> self.index[a, r2]) & 1
                sea = int(r2 < 0)
                if bit != sea:
                    deviations.append({"flavor": a, "mode": f"{r2}/2", "occupation": bit})
        return deviations


# An operator is a tuple of (integer coefficient, monomial) terms.
def identity(scale=1):
    return ((scale, ()),) if scale else ()


def add(*operators):
    return tuple(term for operator in operators for term in operator if term[0])


def scale(operator, coefficient):
    return tuple((coefficient * c, ops) for c, ops in operator if coefficient * c)


def dagger(operator):
    switch = {"ann": "cre", "cre": "ann"}
    return tuple(
        (c, tuple((switch[kind], a, r2) for kind, a, r2 in reversed(ops)))
        for c, ops in operator
    )


def apply(fock: Fock, operator, vector):
    out = {}
    for state, amplitude in vector.items():
        for coefficient, ops in operator:
            ans = fock.apply_monomial(state, ops)
            if ans is None:
                continue
            target, sign = ans
            out[target] = out.get(target, 0) + amplitude * coefficient * sign
    return {state: value for state, value in out.items() if value}


def subtract_vectors(left, right):
    out = dict(left)
    for state, value in right.items():
        out[state] = out.get(state, 0) - value
        if not out[state]:
            del out[state]
    return out


def commutator_action(fock, left, right, vector):
    return subtract_vectors(
        apply(fock, left, apply(fock, right, vector)),
        apply(fock, right, apply(fock, left, vector)),
    )


def E(fock: Fock, n: int, a: int, b: int):
    terms = []
    for r2 in fock.modes2:
        s2 = r2 + 2 * n
        if s2 in fock.modes2:
            terms.append((1, (("cre", a, r2), ("ann", b, s2))))
            if n == 0 and a == b and r2 < 0:
                terms.append((-1, ()))
    return tuple(terms)


def A(fock: Fock, n: int, a: int, b: int):
    terms = []
    for r2 in fock.modes2:
        s2 = 2 * n - r2
        if s2 in fock.modes2:
            terms.append((1, (("ann", a, r2), ("ann", b, s2))))
    return tuple(terms)


def A_star_explicit(fock: Fock, n: int, a: int, b: int):
    """The written adjoint sum: sum_r c^*_{b,n-r} c^*_{a,r}."""
    terms = []
    for r2 in fock.modes2:
        s2 = 2 * n - r2
        if s2 in fock.modes2:
            terms.append((1, (("cre", b, s2), ("cre", a, r2))))
    return tuple(terms)


def current_rhs(fock, m, n, a, b, c, d):
    pieces = []
    if b == c:
        pieces.append(E(fock, m + n, a, d))
    if a == d:
        pieces.append(scale(E(fock, m + n, c, b), -1))
    if m + n == 0 and a == d and b == c:
        pieces.append(identity(m))
    return add(*pieces)


def pair_rhs(fock, n, a, b):
    return add(identity(n), scale(E(fock, 0, a, a), -1), scale(E(fock, 0, b, b), -1))


def all_states(fock):
    return range(1 << fock.n_orbitals)


def core_states(fock: Fock, R2: int):
    inside = [
        fock.index[a, r2]
        for a in range(fock.flavors)
        for r2 in fock.modes2
        if abs(r2) <= R2
    ]
    states = []
    for mask in range(1 << len(inside)):
        state = fock.vacuum
        for j, orbital in enumerate(inside):
            if (mask >> j) & 1:
                state ^= 1 << orbital
        states.append(state)
    return states


def equality_on_states(fock, left_action, right_operator, states):
    for state in states:
        vector = {state: 1}
        left = left_action(vector)
        right = apply(fock, right_operator, vector)
        difference = subtract_vectors(left, right)
        if difference:
            return False, state, difference
    return True, None, {}


def integer_cube_floor(L):
    M = round(L ** (1 / 3))
    while (M + 1) ** 3 <= L:
        M += 1
    while M ** 3 > L:
        M -= 1
    return M


def dispersion_samples(n=2):
    rows = []
    for L in (125, 1000, 8000):
        M = integer_cube_floor(L)
        modes = [r2 / 2 for r2 in range(-2 * M + 1, 2 * M, 2)]
        residuals = []
        for r in modes:
            if r + n in modes:
                e_r = L / (2 * math.pi) * math.sin(2 * math.pi * r / L)
                e_s = L / (2 * math.pi) * math.sin(2 * math.pi * (r + n) / L)
                residuals.append(abs(e_r - e_s + n))
        coefficient_l1 = sum(residuals)
        pointwise_bound = 2 * math.pi**2 * abs(n) * M**2 / L**2
        operator_bound = 4 * math.pi**2 * abs(n) * M**3 / L**2
        rows.append(
            {
                "L": L,
                "M": M,
                "terms": len(residuals),
                "max_coefficient_residual": max(residuals),
                "coefficient_l1_bound": coefficient_l1,
                "analytic_pointwise_bound": pointwise_bound,
                "analytic_operator_bound": operator_bound,
                "simplified_M_floor_bound": 4 * math.pi**2 * abs(n) / L,
                "sample_inequalities_hold": (
                    max(residuals) <= pointwise_bound * (1 + 1e-12)
                    and coefficient_l1 <= operator_bound * (1 + 1e-12)
                    and M**3 <= L
                ),
            }
        )
    return rows


def main(output: Path):
    checks = []

    # Exhaustive full-Fock checks in 8 orbitals (dimension 256).
    small = Fock(M=2, flavors=2)
    states = list(all_states(small))

    for operator, expected, label in (
        (dagger(E(small, 1, 0, 1)), E(small, -1, 1, 0), "current adjoint"),
        (dagger(A(small, 1, 0, 1)), A_star_explicit(small, 1, 0, 1), "pair adjoint"),
    ):
        ok, witness, diff = equality_on_states(
            small,
            lambda vector, operator=operator: apply(small, operator, vector),
            expected,
            states,
        )
        if not ok:
            raise AssertionError((label, witness, diff))
        checks.append(label)

    # The off-diagonal bracket has the affine answer only after edge removal.
    m, n, a, b, c, d = 1, -1, 0, 1, 1, 0
    left = lambda vector: commutator_action(
        small, E(small, m, a, b), E(small, n, c, d), vector
    )
    rhs = current_rhs(small, m, n, a, b, c, d)
    global_ok, edge_state, edge_difference = equality_on_states(small, left, rhs, states)
    if global_ok:
        raise AssertionError("finite-window affine current identity unexpectedly global")
    checks.append("finite current boundary counterexample")

    # A sufficient cutoff for D_R is M-1/2 > R+|m|+|n|.
    large = Fock(M=4, flavors=2)
    core = core_states(large, R2=1)  # R=1/2, 16 exact core basis states.
    left_large = lambda vector: commutator_action(
        large, E(large, m, a, b), E(large, n, c, d), vector
    )
    core_ok, _, _ = equality_on_states(
        large,
        left_large,
        current_rhs(large, m, n, a, b, c, d),
        core,
    )
    if not core_ok:
        raise AssertionError("current bracket failed on stabilized core")
    checks.append("off-diagonal affine current bracket on D_1/2")

    # A second off-diagonal test has a nonzero output mode and no central term.
    m2, n2 = 1, 1
    noncentral_ok, _, _ = equality_on_states(
        large,
        lambda vector: commutator_action(
            large, E(large, m2, 0, 1), E(large, n2, 1, 0), vector
        ),
        current_rhs(large, m2, n2, 0, 1, 1, 0),
        core,
    )
    if not noncentral_ok:
        raise AssertionError("noncentral off-diagonal bracket failed on core")
    checks.append("noncentral off-diagonal current bracket on D_1/2")

    # Vacuum annihilation and norm are exact integers.
    vacuum = {large.vacuum: 1}
    vacuum_rows = []
    for k in (1, 2, 3):
        annihilated = apply(large, E(large, k, 0, 1), vacuum)
        created = apply(large, E(large, -k, 0, 1), vacuum)
        norm2 = sum(value * value for value in created.values())
        if annihilated or norm2 != k:
            raise AssertionError((k, annihilated, norm2))
        vacuum_rows.append({"n": k, "E_n_vacuum_is_zero": True, "norm_E_minus_n_vacuum_squared": norm2})
    checks.append("vacuum current response n=1,2,3")

    # Different-species pair identity: boundary failure globally, exact on core.
    pair_n = 1
    pair = A(small, pair_n, 0, 1)
    pair_left = lambda vector: commutator_action(small, pair, dagger(pair), vector)
    pair_global_ok, pair_edge_state, pair_edge_difference = equality_on_states(
        small, pair_left, pair_rhs(small, pair_n, 0, 1), states
    )
    if pair_global_ok:
        raise AssertionError("finite-window pair identity unexpectedly global")
    checks.append("finite pair boundary counterexample")

    pair_large = A(large, pair_n, 0, 1)
    pair_core_ok, _, _ = equality_on_states(
        large,
        lambda vector: commutator_action(large, pair_large, dagger(pair_large), vector),
        pair_rhs(large, pair_n, 0, 1),
        core,
    )
    if not pair_core_ok:
        raise AssertionError("pair bracket failed on stabilized core")
    checks.append("different-species pair bracket on D_1/2")

    # Same species is the mandatory negative control: A_n^{aa}=0.
    same_pair = A(small, pair_n, 0, 0)
    same_pair_zero, _, _ = equality_on_states(
        small,
        lambda vector: apply(small, same_pair, vector),
        (),
        states,
    )
    same_rhs_on_vacuum = apply(small, pair_rhs(small, pair_n, 0, 0), {small.vacuum: 1})
    if not same_pair_zero or same_rhs_on_vacuum != {small.vacuum: pair_n}:
        raise AssertionError((same_pair_zero, same_rhs_on_vacuum))
    checks.append("same-species pair countercontrol")

    samples = dispersion_samples(n=2)
    if not all(row["sample_inequalities_hold"] for row in samples):
        raise AssertionError("dispersion sample violated analytic bound")
    checks.append("sine-dispersion bound samples")

    result = {
        "verdict": "CONDITIONAL_EXACT_ON_FINITE_EXCITATION_CORE",
        "scope": "finite-window CAR reference model only; no native TFPT-source or eight-copy derivation",
        "input": {
            "path": "/Users/stefanhamann/.codex/attachments/1124b2d0-3a04-43ee-b2d5-291ff850a872/pasted-text.txt",
            "sha256": "64709ed910b4736560c86222cc42a09c8e1c5a4bb6bdb7f7010df947f90b7d77",
        },
        "theory_scope": {
            "source_rg_clock_bridge_20260920": "PARTIAL",
            "TRANS.SEAMCAR.E8CURRENT.01": "missing",
        },
        "integer_checks": checks,
        "small_fock": {
            "M": small.M,
            "flavors": small.flavors,
            "orbitals": small.n_orbitals,
            "dimension": 1 << small.n_orbitals,
            "states_exhausted": len(states),
        },
        "stabilized_core": {
            "M": large.M,
            "R": "1/2",
            "basis_states_checked": len(core),
            "sufficient_current_cutoff": "M-1/2 > R+|m|+|n|",
            "sufficient_pair_cutoff": "M-1/2 > R+|n|",
        },
        "current_test": {
            "indices": {"m": m, "n": n, "a": a, "b": b, "c": c, "d": d},
            "finite_full_fock_identity": False,
            "edge_witness_deviations": small.describe(edge_state),
            "edge_witness_difference": {str(k): v for k, v in edge_difference.items()},
            "core_identity": core_ok,
        },
        "vacuum_response": vacuum_rows,
        "pair_test": {
            "n": pair_n,
            "a_not_equal_b_core_identity": pair_core_ok,
            "finite_full_fock_identity": False,
            "edge_witness_deviations": small.describe(pair_edge_state),
            "edge_witness_difference": {str(k): v for k, v in pair_edge_difference.items()},
            "a_equals_b_operator_zero": same_pair_zero,
            "a_equals_b_stated_rhs_on_vacuum": pair_n,
            "a_equals_b_identity": False,
        },
        "time_limit": {
            "commutator_bound": "||[H_LM,E_n]+n E_n|| <= 4*pi^2*|n|*M^3/L^2",
            "choice": "M=floor(L^(1/3))",
            "resulting_bound": "<=4*pi^2*|n|/L",
            "linear_generator_core_bound": "||(H_LM-H_0)|D_(R,q)|| <= (2*pi^2/3)*q*R^3/L^2",
            "samples": samples,
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "car_results.json")
    main(parser.parse_args().output)
