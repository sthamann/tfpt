#!/usr/bin/env python3
"""Exact first-bridge audit for a common E8 current/clock generator.

The finite checks certify the algebraic statements used in PROOF.txt.  They do
not construct the raw seam-to-affine-current map or promote a ledger claim.
"""

from __future__ import annotations

import hashlib
import itertools as it
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[4]
SOURCES = {
    "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json":
        "a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3",
    "experiments/theory-contracts/compiler-root-phase-lift-20260919/certificate.json":
        "74c6743c54811449719ac0a91192a712dc4f8bcb2c281eaf6d7860e4018772cc",
}
CHECKS: list[str] = []


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    CHECKS.append(label)


def e8_roots() -> set[tuple[F, ...]]:
    roots: set[tuple[F, ...]] = set()
    for i, j in it.combinations(range(8), 2):
        for si, sj in it.product((-1, 1), repeat=2):
            root = [F(0)] * 8
            root[i], root[j] = F(si), F(sj)
            roots.add(tuple(root))
    for signs in it.product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.add(tuple(F(sign, 2) for sign in signs))
    return roots


def negate(vector: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(-entry for entry in vector)


def add(left: tuple[F, ...], right: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(a + b for a, b in zip(left, right))


def main() -> dict[str, object]:
    source_hashes = {}
    for relpath, expected in SOURCES.items():
        actual = hashlib.sha256((REPO / relpath).read_bytes()).hexdigest()
        require(actual == expected, "source pin: " + relpath)
        source_hashes[relpath] = actual

    roots = e8_roots()
    require(len(roots) == 240, "standard E8 root census is 240")
    require(all(sum(entry * entry for entry in root) == 2 for root in roots),
            "every E8 root has norm squared two")

    # A simple E8 basis in the same standard D8-plus-half-spinor coordinates
    # used by the pinned C/J clock certificate.
    simple = (
        (F(1, 2), F(-1, 2), F(-1, 2), F(-1, 2),
         F(-1, 2), F(-1, 2), F(-1, 2), F(1, 2)),
        (F(1), F(1), F(0), F(0), F(0), F(0), F(0), F(0)),
        (F(-1), F(1), F(0), F(0), F(0), F(0), F(0), F(0)),
        (F(0), F(-1), F(1), F(0), F(0), F(0), F(0), F(0)),
        (F(0), F(0), F(-1), F(1), F(0), F(0), F(0), F(0)),
        (F(0), F(0), F(0), F(-1), F(1), F(0), F(0), F(0)),
        (F(0), F(0), F(0), F(0), F(-1), F(1), F(0), F(0)),
        (F(0), F(0), F(0), F(0), F(0), F(-1), F(1), F(0)),
    )
    require(all(root in roots for root in simple), "simple basis lies in E8 roots")
    basis = sp.Matrix.hstack(*(sp.Matrix(root) for root in simple))
    gram = basis.T * basis
    require(abs(basis.det()) == 1 and gram.det() == 1,
            "simple roots are a unimodular E8 basis")
    require(all(gram[i, i] == 2 for i in range(8))
            and sum(1 for i in range(8) for j in range(i) if gram[i, j] == -1) == 7
            and all(gram[i, j] in (0, -1) for i in range(8) for j in range(i)),
            "simple-root Gram is the E8 tree Cartan matrix")
    inverse = basis.inv()

    coordinate_columns = {root: inverse * sp.Matrix(root) for root in roots}
    require(all(value.q == 1 for column in coordinate_columns.values() for value in column),
            "every E8 root has integral simple-root coordinates")
    coordinates = {
        root: tuple(int(value) for value in column)
        for root, column in coordinate_columns.items()
    }
    require(len(set(coordinates.values())) == 240,
            "simple-root coordinates distinguish all roots")

    root_sums = [(alpha, beta, add(alpha, beta))
                 for alpha in roots for beta in roots if add(alpha, beta) in roots]
    require(len(root_sums) == 13440,
            "all ordered nonzero E8 root-sum brackets are enumerated")
    require(all(tuple(x + y for x, y in zip(coordinates[alpha], coordinates[beta]))
                == coordinates[gamma] for alpha, beta, gamma in root_sums),
            "simple-root coordinates satisfy every nonzero root bracket addition")

    # The bracket equations determine any diagonal zero-mode derivation by its
    # eight simple-root values.  This constructive reachability check is the
    # finite converse, not merely an eight-parameter ansatz.
    signed_simple = simple + tuple(negate(root) for root in simple)
    reached = set(signed_simple)
    reach_layers = [len(reached)]
    while True:
        enlarged = reached | {
            add(root, step)
            for root in reached
            for step in signed_simple
            if add(root, step) in roots
        }
        if enlarged == reached:
            break
        reached = enlarged
        reach_layers.append(len(reached))
    require(reached == roots, "bracket graph reaches every root from the simple roots")

    triality = json.loads((REPO / next(iter(SOURCES))).read_text(encoding="utf-8"))

    def clock(label: str) -> sp.Matrix:
        return sp.Matrix([[sp.Rational(value) for value in row]
                          for row in triality["clock_matrices"][label]["vector"]])

    C, J, c = clock("C"), clock("J"), clock("c")
    identity = sp.eye(8)
    x = sp.symbols("x")
    phi30 = x**8 + x**7 - x**5 - x**4 - x**3 + x + 1
    require(C.T * C == identity and C**15 == -identity and C**30 == identity,
            "actual C clock is exact orthogonal order thirty with half-period minus identity")
    require(sp.factor(C.charpoly(x).as_expr()) == phi30,
            "actual C clock has Coxeter polynomial Phi_30")
    require(J.T * J == identity and J**2 == -identity and J**4 == identity,
            "actual J clock is exact orthogonal order four with half-period minus identity")
    require(c.T * c == identity and c**12 == identity,
            "actual compiler c clock is exact orthogonal order twelve")

    def rational_tuple(column: sp.Matrix) -> tuple[F, ...]:
        return tuple(F(int(value.p), int(value.q)) for value in column)

    require({rational_tuple(C * sp.Matrix(root)) for root in roots} == roots,
            "actual C clock preserves the selected E8 root system")
    require({rational_tuple(J * sp.Matrix(root)) for root in roots} == roots,
            "actual J clock preserves the selected E8 root system")
    fixed_dimensions = {
        label: 8 - (matrix.T - identity).rank()
        for label, matrix in (("C", C), ("J", J), ("c", c))
    }
    require(fixed_dimensions == {"C": 0, "J": 0, "c": 0},
            "each actual nontrivial clock separately has zero fixed Cartan dimension")
    require(8 - sp.Matrix.vstack(C.T - identity, J.T - identity, c.T - identity).rank() == 0,
            "joint actual-clock fixed Cartan space is zero")

    # A phase-compatible monomial lift sends E_alpha to eta(alpha)E_{g alpha}.
    # In U D U^-1 the nonzero eta cancels, so diagonal derivation covariance is
    # exactly lambda(g alpha)=lambda(alpha), independent of the lift gauge.
    h = sp.Matrix(sp.symbols("h0:8"))
    clock_equations = (C.T - identity) * h
    require(sp.linear_eq_to_matrix(list(clock_equations), tuple(h))[0].rank() == 8,
            "C covariance kills all eight inner Cartan derivation parameters")

    phase_lift = json.loads(
        (REPO / "experiments/theory-contracts/compiler-root-phase-lift-20260919/certificate.json")
        .read_text(encoding="utf-8")
    )
    require(phase_lift["root_count"] == 240
            and phase_lift["ordered_nonzero_root_sums_per_reflection"] == 13440
            and phase_lift["verdict"] == "EXACT_BRACKET_LIFTS_EXIST_CHARACTER_SECTION_OPEN",
            "pinned current-lift certificate distinguishes bracket phases from root permutations")

    # Positivity is a type obstruction for interpreting zero-mode derivation
    # weights themselves as 240 positive root-register energies.
    require(all(negate(root) in roots for root in roots),
            "every root has an opposite root")
    require(all(tuple(-entry for entry in coordinates[root]) == coordinates[negate(root)]
                for root in roots),
            "bracket-compatible zero-mode weights are odd under root opposition")

    # Exact counterfamily when only vacuum, positivity, internal clocks and one
    # discrete quarter-step are retained.  ad(H_b) is of course a Leibniz
    # derivation on the full operator algebra.  What fails for b != 0 is the
    # stronger invariant-linear-current condition: each J_n must be an
    # eigenoperator with a state-independent scalar frequency.
    def energy(n: int, b: int) -> int:
        return n + 4 * b * n * (n - 1)

    require(all(energy(n, b) >= 0 for b in range(4) for n in range(17)),
            "counterfamily is positive on checked nonnegative grades")
    require(all((energy(n, b) - n) % 4 == 0 for b in range(4) for n in range(17)),
            "counterfamily has the same quarter-step phase as L0")
    require(all(energy(0, b) == 0 and energy(1, b) == 1 for b in range(4)),
            "counterfamily has the same vacuum and grade-one energy")
    n, m, b = sp.symbols("n m b", integer=True)
    f = lambda q: q + 4 * b * q * (q - 1)
    grade_energy_nonadditivity = sp.expand(f(n + m) - f(n) - f(m))
    require(grade_energy_nonadditivity == 8 * b * n * m,
            "nonlinear grade family has exact additive grade-energy defect")
    ell = sp.symbols("ell", integer=True)
    current_mode_factor = sp.expand(f(ell - n) - f(ell))
    expected_mode_factor = -n - 8 * b * n * ell + 4 * b * n * (n + 1)
    require(sp.expand(current_mode_factor - expected_mode_factor) == 0,
            "nonlinear grade family has exact state-dependent current-mode factor")
    require(energy(2, 0) == 2 and energy(2, 1) == 10,
            "two preserved-input generators have different grade-two response")

    result = {
        "status": "PASS",
        "verdict": "PARTIAL_FIRST_BRIDGE",
        "exact_checks": len(CHECKS),
        "failed_checks": 0,
        "source_sha256": source_hashes,
        "root_count": len(roots),
        "ordered_nonzero_root_sum_brackets": len(root_sums),
        "bracket_reach_layers": reach_layers,
        "diagonal_zero_mode_derivation_dimension_before_clocks": 8,
        "clock_fixed_cartan_dimensions": fixed_dimensions,
        "joint_clock_fixed_cartan_dimension": 0,
        "actual_C_charpoly": str(phi30),
        "forced_affine_phase_rule_under_named_premises": "omega(alpha,n)=a*n",
        "forced_generator_under_named_premises": "H=a*L0+c*I",
        "vacuum_and_positivity_reduction": "c=0; a>=0; a>0 remains a time-unit choice",
        "positive_root_register_current_derivation": "only the zero weight assignment",
        "remaining_discrete_only_family": "H_b=L0+4*b*L0*(L0-1), integer b>=0",
        "remaining_family_grade_energy_nonadditivity": str(grade_energy_nonadditivity),
        "remaining_family_current_mode_identity":
            "[f(L0),J_n]=J_n*(f(L0-n)-f(L0))",
        "remaining_family_current_mode_factor": str(current_mode_factor),
        "grade_two_witness": {"b=0": 2, "b=1": 10},
        "first_untransported_premise": (
            "a same-space raw-source map to affine E8 modes whose continuous evolution "
            "leaves the linear affine-current span invariant with bracket-compatible "
            "state-independent scalar mode frequencies/local current rotation"
        ),
        "preserved_by_counterfamily": [
            "the affine vacuum vector",
            "positive spectrum on nonnegative grades",
            "all internal grade-preserving E8 clock operations, including C/J/c",
            "the same grade-one energy",
            "the same exp(-i*pi*H/2) discrete quarter-step",
        ],
        "not_preserved_by_counterfamily": [
            "invariance of the linear affine-current mode space with state-independent scalar frequencies",
            "geometric conformal rotations/local net evolution",
            "multi-time response above grade one",
        ],
        "closed_gate_ids": [],
        "not_claimed": [
            "raw P1/P2 seam to an invariant affine current-mode evolution",
            "physical time calibration",
            "3+1D locality or Lorentz dynamics",
            "a physical Hamiltonian selected without the named affine premise",
            "TOE completion or ledger promotion",
        ],
        "checks": CHECKS,
    }
    return result


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
