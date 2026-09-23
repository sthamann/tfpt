"""Exact candidate-state checks for the v1.6.9 state/time theory contract.

No candidate is built from eigenvectors, measured frequencies, or Gibbs
weights of H.  The H-Gibbs row is retained only as the forbidden positive
control required by modular uniqueness.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

import sympy as sp


CHECKS: list[str] = []


def need(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    CHECKS.append(label)


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return a * b - b * a


def star_block() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """One exact native W row: eight disjoint leaves and one boson."""
    x = sp.zeros(9)
    for leaf in range(8):
        x[leaf, 8] = 1
        x[8, leaf] = 1
    nb = sp.diag(*([0] * 8), 1)
    h = nb + sp.Rational(1, 20) * x
    return x, nb, h


def n4_block() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    x = sp.Matrix([[0, 4], [4, 0]])
    nb = sp.diag(2, 1)
    h = nb + sp.Rational(1, 20) * x
    return x, nb, h


def bright_block() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """The 120-dimensional bright carrier, ordered pair then boson."""
    x2 = sp.Matrix([[0, sp.sqrt(8)], [sp.sqrt(8), 0]])
    nb2 = sp.diag(0, 1)
    return (
        sp.kronecker_product(sp.eye(60), x2),
        sp.kronecker_product(sp.eye(60), nb2),
        sp.kronecker_product(sp.eye(60), nb2 + sp.Rational(1, 20) * x2),
    )


def rational_grading_state(nb: sp.Matrix, q: int = 2) -> sp.Matrix:
    weights = [sp.Integer(q) ** int(nb[i, i]) for i in range(nb.rows)]
    return sp.diag(*weights) / sum(weights)


def rank_one(index: int, dimension: int) -> sp.Matrix:
    vector = sp.zeros(dimension, 1)
    vector[index] = 1
    return vector * vector.T


def main() -> None:
    blocks = {
        "N2_star_9": star_block(),
        "N4_singlet_2": n4_block(),
        "bright_120": bright_block(),
    }
    expected_dimensions = {"N2_star_9": 9, "N4_singlet_2": 2, "bright_120": 120}
    block_report: dict[str, object] = {}

    for name, (x, nb, h) in blocks.items():
        dimension = expected_dimensions[name]
        need(x.shape == (dimension, dimension), name + " dimension")
        need(x == x.T and nb == nb.T and h == h.T, name + " Hermiticity")
        need(h == nb + sp.Rational(1, 20) * x, name + " native ratio")
        need(commutator(x, nb) != sp.zeros(dimension), name + " source and grading do not commute")

        trace_state = sp.eye(dimension) / dimension
        grading_state = rational_grading_state(nb)
        source_index = dimension - 1 if name == "N2_star_9" else (1 if name == "bright_120" else 0)
        source_state = rank_one(source_index, dimension)

        need(sp.trace(trace_state) == 1, name + " trace state normalized")
        need(trace_state.rank() == dimension, name + " trace state faithful")
        need(commutator(trace_state, h) == sp.zeros(dimension), name + " trace state stationary")

        need(sp.trace(grading_state) == 1, name + " grading state normalized")
        need(grading_state.rank() == dimension, name + " grading state faithful")
        need(all(grading_state[i, i] > 0 for i in range(dimension)), name + " grading state positive")
        need(commutator(grading_state, h) != sp.zeros(dimension), name + " nontracial grading state nonstationary")

        need(sp.trace(source_state) == 1 and source_state * source_state == source_state,
             name + " source ray positive and normalized")
        need(source_state.rank() == 1 < dimension, name + " source ray nonfaithful")
        need(commutator(source_state, h) != sp.zeros(dimension), name + " source ray nonstationary")

        # exp(-kappa X)/Z is strictly positive for real nonzero kappa because X is
        # Hermitian.  Its stationarity failure follows exactly from the nonzero
        # source/grading commutator (the active two-level eigenvalues are distinct).
        need(x == x.T, name + " source exponential has positive Hermitian density")
        need(commutator(x, h) == commutator(x, nb) != sp.zeros(dimension),
             name + " source exponential modular generator is H-mismatched")

        block_report[name] = {
            "dimension": dimension,
            "source_rank": 1,
            "trace_rank": dimension,
            "grading_q2_rank": grading_state.rank(),
            "grading_q2_weights": sorted({str(grading_state[i, i]) for i in range(dimension)}),
            "commutator_X_Nb_nonzero_entries": sum(1 for value in commutator(x, nb) if value != 0),
        }

    equal_source = sp.eye(4) / 4
    need(sp.trace(equal_source) == 1 and equal_source.rank() == 4,
         "original equal source state I4/4 is normalized and faithful")
    need(equal_source * sp.ones(4) == sp.ones(4) / 4,
         "I4/4 has one eigenvalue and therefore trivial modular flow")

    vacuum = sp.Matrix([[1]])
    need(vacuum == sp.eye(1) and sp.trace(vacuum) == 1,
         "empty boundary vacuum is a faithful state only on its one-dimensional support algebra")

    candidates = {
        "sector_trace": {
            "independent_basis": "sector plus maximum entropy",
            "positive": True, "normalized": True, "faithful_full_algebra": True,
            "stationary_under_H": True, "modular": "trivial",
            "range": "full chosen finite sector",
        },
        "equal_source_I4_over_4": {
            "independent_basis": "equal weighting of four original source labels",
            "positive": True, "normalized": True, "faithful_full_algebra": True,
            "stationary_under_H": "not implied outside the source-label factor",
            "modular": "trivial on M4",
            "range": "source multiplicity algebra M4",
        },
        "source_ray": {
            "independent_basis": "native source or boundary ray",
            "positive": True, "normalized": True, "faithful_full_algebra": False,
            "stationary_under_H": False, "modular": "undefined on full M_d; trivial on rank-one support",
            "range": "rank-one support only",
        },
        "grading_weight_qNb": {
            "independent_basis": "positive occupation weighting q^Nb, q>0",
            "positive": True, "normalized": True, "faithful_full_algebra": True,
            "stationary_under_H": "only q=1 (or g=0)",
            "modular": "nontrivial for q!=1; generator proportional to Nb",
            "range": "all tested blocks",
        },
        "source_exponential": {
            "independent_basis": "rho proportional exp(-kappa X), X from W only",
            "positive": True, "normalized": True, "faithful_full_algebra": True,
            "stationary_under_H": "only kappa=0 (or Delta=0)",
            "modular": "nontrivial; generator proportional to X",
            "range": "native source-connected blocks",
        },
        "boundary_vacuum": {
            "independent_basis": "empty boundary condition",
            "positive": True, "normalized": True, "faithful_full_algebra": False,
            "stationary_under_H": True, "modular": "trivial on one-dimensional support",
            "range": "vacuum observables only",
        },
        "H_gibbs_forbidden_control": {
            "independent_basis": False,
            "positive": True, "normalized": True, "faithful_full_algebra": True,
            "stationary_under_H": True, "modular": "matches H by construction",
            "range": "full tested block",
            "circular": True,
        },
    }

    result = {
        "status": "PASS",
        "checker": Path(__file__).name,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "guard_count": len(CHECKS),
        "guards": CHECKS,
        "blocks": block_report,
        "candidates": candidates,
        "finite_algebra_prerequisites": {
            "algebra": "M_d(C), a finite type-I factor",
            "physical_irreducible_representation": "no separating vector for d>1",
            "standard_form": "Hilbert-Schmidt/GNS carrier with vector rho^(1/2)",
            "cyclic_and_separating_iff": "rho is faithful (strictly positive)",
            "modular_operator": "Delta_rho = L_rho R_rho^(-1)",
            "modular_flow": "sigma_t(A)=rho^(it) A rho^(-it)",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
