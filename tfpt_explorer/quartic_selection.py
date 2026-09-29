"""Exact low-degree selector for the native quartic source.

The calculation separates two statements which are easy to conflate:

* the full two-qubit Pauli group has its first nonconstant polynomial
  invariants in degree four, where their dimension is five;
* choosing the lowest positive invariant degree is an additional source
  selection rule, not a theorem supplied by P1 or the four marked points.

The Molien coefficients are computed by an explicit average over all 64
Pauli matrices.  They are not read from the known closed Molien series.  The
module also keeps the geometric RR quarter turn, the central Gaussian action,
and the cyclic register-value action on the code as three distinct operators.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import itertools as it
from typing import Any

import sympy as sp


MAX_DEGREE = 16


def _check(
    name: str,
    ok: bool,
    actual: Any,
    expected: Any,
    method: str,
) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


def _matrix_key(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.expand(entry) for entry in matrix)


def _pauli_group() -> tuple[sp.Matrix, ...]:
    """Generate ``mu4 * P_2`` directly as 64 exact 4 by 4 matrices."""

    x = sp.Matrix([[0, 1], [1, 0]])
    z = sp.diag(1, -1)
    group = []
    for phase_power in range(4):
        phase = sp.I**phase_power
        for a, b, c, d in it.product((0, 1), repeat=4):
            first = x**a * z**b
            second = x**c * z**d
            group.append(phase * sp.kronecker_product(first, second))
    return tuple(group)


def _symmetric_characters(matrix: sp.Matrix, max_degree: int) -> tuple[sp.Expr, ...]:
    """Characters of Sym^n(matrix), obtained from Newton's trace recursion."""

    complete = [sp.Integer(1)]
    power_traces = [sp.trace(matrix**power) for power in range(1, max_degree + 1)]
    for degree in range(1, max_degree + 1):
        value = sum(
            power_traces[power - 1] * complete[degree - power]
            for power in range(1, degree + 1)
        ) / degree
        complete.append(sp.simplify(value))
    return tuple(complete)


def _intertwiner_data(source: sp.Matrix, target: sp.Matrix) -> dict[str, Any]:
    """Solve ``target A = A source`` and bound ranks by shared eigenspaces."""

    equation = sp.kronecker_product(sp.eye(source.rows), target) - sp.kronecker_product(
        source.T, sp.eye(target.rows)
    )
    equation_rank = int(equation.rank())
    nullity = source.cols * target.rows - equation_rank
    source_multiplicities = source.eigenvals()
    target_multiplicities = target.eigenvals()
    shared_eigenvalues = sorted(
        source_multiplicities.keys() & target_multiplicities.keys(), key=str
    )
    shared = {
        eigenvalue: (int(source_multiplicities[eigenvalue]), int(target_multiplicities[eigenvalue]))
        for eigenvalue in shared_eigenvalues
    }
    maximum_rank = sum(min(source_dim, target_dim) for source_dim, target_dim in shared.values())

    # Build an explicit witness attaining the shared-eigenspace bound.  Columns
    # of ``source_basis`` diagonalize the source; ``target_images`` prescribe
    # where those columns go, using independent target eigenvectors whenever
    # the same eigenvalue is available and zero otherwise.
    source_columns: list[sp.Matrix] = []
    target_images: list[sp.Matrix] = []
    for eigenvalue in sorted(source_multiplicities, key=str):
        source_vectors = (source - eigenvalue * sp.eye(source.rows)).nullspace()
        target_vectors = (
            (target - eigenvalue * sp.eye(target.rows)).nullspace()
            if eigenvalue in target_multiplicities
            else []
        )
        for index, vector in enumerate(source_vectors):
            source_columns.append(vector)
            target_images.append(
                target_vectors[index] if index < len(target_vectors) else sp.zeros(target.rows, 1)
            )
    source_basis = sp.Matrix.hstack(*source_columns)
    witness = sp.simplify(sp.Matrix.hstack(*target_images) * source_basis.inv())
    witness_residual = sp.simplify(target * witness - witness * source)
    witness_rank = int(witness.rank())
    return {
        "equation_rank": equation_rank,
        "hom_dimension": nullity,
        "maximum_intertwiner_rank": maximum_rank,
        "maximum_rank_witness": [
            [str(entry) for entry in row] for row in witness.tolist()
        ],
        "witness_rank": witness_rank,
        "witness_equation_residual_zero": witness_residual == sp.zeros(target.rows, source.cols),
        "invertible_intertwiner_exists": maximum_rank == source.cols == target.rows,
        "shared_eigenspaces": {
            str(eigenvalue): {"source": source_dim, "target": target_dim}
            for eigenvalue, (source_dim, target_dim) in shared.items()
        },
    }


def _operator_record(matrix: sp.Matrix) -> dict[str, Any]:
    identity = sp.eye(matrix.rows)
    order = next(power for power in range(1, 17) if matrix**power == identity)
    spectrum = Counter()
    for eigenvalue, multiplicity in matrix.eigenvals().items():
        spectrum[str(eigenvalue)] += int(multiplicity)
    return {
        "matrix": [[str(entry) for entry in row] for row in matrix.tolist()],
        "dimension": matrix.rows,
        "order": order,
        "trace": str(sp.trace(matrix)),
        "spectrum": dict(spectrum),
        "characteristic_polynomial": str(sp.factor(matrix.charpoly().as_expr())),
    }


@lru_cache(maxsize=1)
def build_quartic_selection_data() -> dict[str, Any]:
    """Return the exact Molien selector and the three typed clock actions."""

    group = _pauli_group()
    distinct_group = {_matrix_key(matrix) for matrix in group}
    identity4 = sp.eye(4)
    group_closed = all(
        _matrix_key(left * right) in distinct_group
        for left, right in it.product(group, repeat=2)
    )

    # Independent finite trace average.  The known rational Molien function is
    # reconstructed only after these coefficients have been computed.
    character_rows = [_symmetric_characters(matrix, MAX_DEGREE) for matrix in group]
    coefficients = []
    for degree in range(MAX_DEGREE + 1):
        average = sp.simplify(sum(row[degree] for row in character_rows) / len(group))
        if average.is_Integer is not True:
            raise ArithmeticError(f"non-integral Molien coefficient in degree {degree}: {average}")
        coefficients.append(int(average))

    variable = sp.symbols("t")
    determinant_census = Counter(
        str(sp.factor((identity4 - variable * matrix).det())) for matrix in group
    )
    finite_molien = sp.factor(
        sum(
            multiplicity / sp.sympify(determinant, locals={"t": variable, "I": sp.I})
            for determinant, multiplicity in determinant_census.items()
        )
        / len(group)
    )
    reference_molien = (1 - variable**16) / (1 - variable**4) ** 5
    molien_identity = sp.simplify(finite_molien - reference_molien) == 0

    nonconstant_degrees = [degree for degree, dimension in enumerate(coefficients) if degree and dimension]
    first_nonconstant_degree = nonconstant_degrees[0]
    first_nonconstant_dimension = coefficients[first_nonconstant_degree]

    rr = sp.diag(1, sp.I, -1, -sp.I, 1)
    gaussian_source = sp.I * identity4
    gaussian_degree4 = sp.eye(5)  # Sym^4(i I4) restricts as i^4 I5.
    cyclic_code = sp.Matrix(
        [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
    rr_to_cyclic = _intertwiner_data(rr, cyclic_code)
    rr_to_gaussian = _intertwiner_data(rr, gaussian_degree4)
    cyclic_to_gaussian = _intertwiner_data(cyclic_code, gaussian_degree4)

    expected_coefficients = [
        1, 0, 0, 0, 5, 0, 0, 0, 15, 0, 0, 0, 35, 0, 0, 0, 69
    ]
    checks = [
        _check(
            "the explicitly generated two-qubit Pauli group has 64 elements and is closed",
            len(group) == len(distinct_group) == 64 and group_closed,
            {"generated": len(group), "distinct": len(distinct_group), "closed": group_closed},
            {"generated": 64, "distinct": 64, "closed": True},
            "Exact products of mu4 times X^a Z^b tensor X^c Z^d",
        ),
        _check(
            "finite trace averaging gives every invariant dimension through degree 16",
            coefficients == expected_coefficients,
            coefficients,
            expected_coefficients,
            "For each of 64 matrices, Newton recursion computes tr Sym^n(g); dimensions are the exact group average",
        ),
        _check(
            "the independently averaged series equals the documented Pauli Molien function",
            molien_identity,
            str(finite_molien),
            "(1-t**16)/(1-t**4)**5",
            "Direct average of 1/det(I-tg), grouped only by the exact determinant census",
        ),
        _check(
            "degree four is the first nonconstant invariant sector and has dimension five",
            first_nonconstant_degree == 4 and first_nonconstant_dimension == 5,
            {"degree": first_nonconstant_degree, "dimension": first_nonconstant_dimension},
            {"degree": 4, "dimension": 5},
            "First positive coefficient of the independently computed Molien average",
        ),
        _check(
            "RR, central Gaussian, and cyclic code actions are three distinct operators",
            (
                rr**4 == sp.eye(5)
                and rr**2 != sp.eye(5)
                and gaussian_source**4 == identity4
                and gaussian_degree4 == sp.eye(5)
                and cyclic_code**2 == sp.eye(5)
                and sp.trace(rr) == 1
                and sp.trace(gaussian_degree4) == 5
                and sp.trace(cyclic_code) == 3
            ),
            {
                "RR": _operator_record(rr),
                "central_Gaussian_on_degree4": _operator_record(gaussian_degree4),
                "cyclic_code": _operator_record(cyclic_code),
            },
            {"orders": [4, 1, 2], "traces": ["1", "5", "3"]},
            "Exact powers, traces, spectra, and characteristic polynomials",
        ),
        _check(
            "RR and cyclic code actions admit nonzero but no invertible intertwiner",
            (
                rr_to_cyclic["hom_dimension"] == 9
                and rr_to_cyclic["equation_rank"] == 16
                and rr_to_cyclic["maximum_intertwiner_rank"] == 3
                and rr_to_cyclic["witness_rank"] == 3
                and rr_to_cyclic["witness_equation_residual_zero"]
                and not rr_to_cyclic["invertible_intertwiner_exists"]
            ),
            rr_to_cyclic,
            {
                "hom_dimension": 9,
                "equation_rank": 16,
                "maximum_intertwiner_rank": 3,
                "witness_rank": 3,
                "witness_equation_residual_zero": True,
                "invertible_intertwiner_exists": False,
            },
            "Rank of the 25 by 25 exact Sylvester equation plus shared-eigenspace rank bound",
        ),
    ]

    selection_rule = {
        "rule": "choose the lowest positive degree carrying a nonconstant Pauli-invariant polynomial readout",
        "selected_degree": first_nonconstant_degree,
        "selected_dimension": first_nonconstant_dimension,
        "consequence": "Under this explicit filter, the vacuum degree 0 is excluded and the quartic five-space is selected before degree 8.",
        "status": "conditional selection rule",
        "boundary": "The finite invariant calculation proves the consequence of the filter. It does not derive the filter from P1, P2, the four marked points, a state rule, or a physical instrument algebra.",
    }

    data = {
        "pauli_group": {
            "order": len(group),
            "construction": "mu4 times {X^a Z^b tensor X^c Z^d | a,b,c,d in F2}",
            "closed": group_closed,
            "determinant_census": dict(sorted(determinant_census.items())),
        },
        "molien": {
            "method": "exact finite trace average over all 64 generated matrices",
            "maximum_degree": MAX_DEGREE,
            "coefficients": [
                {"degree": degree, "invariant_dimension": dimension}
                for degree, dimension in enumerate(coefficients)
            ],
            "nonzero_coefficients": {
                str(degree): dimension
                for degree, dimension in enumerate(coefficients)
                if dimension
            },
            "finite_average": str(finite_molien),
            "normalized_form": "(1-t**16)/(1-t**4)**5",
            "identity_exact": molien_identity,
        },
        "selection_rule": selection_rule,
        "quarter_turns": {
            "geometric_RR": {
                **_operator_record(rr),
                "carrier": "E_RR=H0(P1,O(mu4))",
                "meaning": "geometric rotation of the four marked points on the five-dimensional RR function space",
            },
            "central_Gaussian_source": {
                **_operator_record(gaussian_source),
                "carrier": "native C4 source",
                "meaning": "J=i I4; on Sym^N it acts by i^N",
                "degree4_restriction": _operator_record(gaussian_degree4),
            },
            "cyclic_register_code": {
                **_operator_record(cyclic_code),
                "carrier": "quartic code5",
                "meaning": "cyclic shift of the four register values, lifted to four registers and restricted to the code",
            },
        },
        "intertwiners": {
            "RR_to_cyclic_code": rr_to_cyclic,
            "RR_to_central_Gaussian_degree4": rr_to_gaussian,
            "cyclic_code_to_central_Gaussian_degree4": cyclic_to_gaussian,
            "interpretation": "Nonzero low-rank maps exist. The obstruction concerns an invertible marked identification of the full five-dimensional actions, not the existence of every linear intertwiner.",
        },
    }
    scope = [
        "Exact finite invariant theory for the explicitly generated 64-element two-qubit Pauli group through source degree 16.",
        "Exact comparison of three named operators on their stated carriers; equal symbols or dimensions are not used as identifications.",
        "The minimal positive Pauli-invariant readout is a transparent conditional selection filter, not a P1/P2 theorem and not a derivation of the physical instrument algebra.",
        "The calculation does not identify the geometric RR quarter turn with the central Gaussian J or with the cyclic register-value lift.",
    ]
    sources = [
        {
            "path": "_newest2/TFPT_Gesamtdokumentation2_20260927.md",
            "line": 3441,
            "claim": "Pauli invariant ring, Molien function, five degree-four generators, and the degree-16 relation",
        },
        {
            "path": "_newest2/TFPT_Universalraum_Gesamtdokumentation_20260927.md",
            "line": 6292,
            "claim": "RR and cyclic-code quarter-turn matrices and the noninvertible marked-bridge obstruction",
        },
        {
            "path": "verification/v690_quartic_half.py",
            "line": 13,
            "claim": "Central Gaussian J action and the distinct G31 scalar-invariant degrees 8,12,20,24",
        },
    ]
    return {
        "status": "PASS" if all(check["ok"] for check in checks) else "FAIL",
        "data": data,
        "checks": checks,
        "scope": scope,
        "sources": sources,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(build_quartic_selection_data(), indent=2, sort_keys=True))
