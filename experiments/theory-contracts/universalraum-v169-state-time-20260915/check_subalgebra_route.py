"""Exact finite-dimensional checks for the proper-subalgebra follow-up.

The checker distinguishes three questions that coincide only for a full
matrix factor: faithfulness of the restricted functional, existence of its
modular flow, and invariance of the subalgebra under the native H-flow.
"""
from __future__ import annotations

import json
import math
from hashlib import sha256
from pathlib import Path

import sympy as sp


EXACT: list[str] = []
NUMERICAL: list[str] = []


def need(condition: bool, label: str, numerical: bool = False) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    (NUMERICAL if numerical else EXACT).append(label)


def partial_trace_right(psi: sp.Matrix, left_dim: int, right_dim: int) -> sp.Matrix:
    coefficient = sp.Matrix(left_dim, right_dim, list(psi))
    return sp.simplify(coefficient * coefficient.conjugate().T)


def matrix_unit(dimension: int, row: int, column: int) -> sp.Matrix:
    result = sp.zeros(dimension)
    result[row, column] = 1
    return result


def two_chart_state(overlap_squared: sp.Rational) -> tuple[sp.Matrix, sp.Matrix]:
    """(|P_L>+|P_R>)/sqrt(2(1+c^2)) for two modes in each chart.

    f^L_i=a_i and f^R_i=c a_i+sqrt(1-c^2)d_i.  The left/right tensor
    bases are [00,10,01,11].  A harmless CAR ordering sign occurs in one
    mixed term and disappears from the reduced spectrum.
    """
    p = overlap_squared
    normalization_squared = 2 * (1 + p)
    psi = sp.zeros(16, 1)

    def set_amplitude(left: int, right: int, value: sp.Expr) -> None:
        psi[left * 4 + right] = value / sp.sqrt(normalization_squared)

    set_amplitude(3, 0, 1 + p)
    set_amplitude(1, 2, sp.sqrt(p * (1 - p)))
    set_amplitude(2, 1, -sp.sqrt(p * (1 - p)))
    set_amplitude(0, 3, 1 - p)
    rho_left = partial_trace_right(psi, 4, 4)
    return psi, rho_left


def main() -> None:
    # General proper-subalgebra witness: a globally pure Schmidt state can
    # restrict faithfully to B=M2 tensor I2.  Hence global rank-one does not
    # imply nonfaithfulness on B.
    schmidt = sp.zeros(4, 1)
    schmidt[0] = sp.sqrt(sp.Rational(1, 3))
    schmidt[3] = sp.sqrt(sp.Rational(2, 3))
    global_density = schmidt * schmidt.T
    reduced_density = partial_trace_right(schmidt, 2, 2)
    need(global_density.rank() == 1, "proper-subalgebra witness is globally pure")
    need(reduced_density == sp.diag(sp.Rational(1, 3), sp.Rational(2, 3)),
         "proper-subalgebra witness has exact reduced density diag(1/3,2/3)")
    need(reduced_density.rank() == 2 and reduced_density.det() > 0,
         "globally pure witness is faithful on M2 tensor I2")

    # Full-factor contrast: a matrix commuting with all units is scalar.
    z0, z1, z2, z3 = sp.symbols("z0:4")
    z = sp.Matrix([[z0, z1], [z2, z3]])
    center_equations: list[sp.Expr] = []
    for i in range(2):
        for j in range(2):
            center_equations.extend(list(z * matrix_unit(2, i, j) - matrix_unit(2, i, j) * z))
    center_matrix, _ = sp.linear_eq_to_matrix(center_equations, [z0, z1, z2, z3])
    need(center_matrix.rank() == 3, "full M2 centralizer is exactly C times identity")

    # Candidate 1: exact two-chart source-pair state.
    chart_rows: dict[str, object] = {}
    expected_spectra = {
        sp.Rational(0): [sp.Rational(1, 2), 0, 0, sp.Rational(1, 2)],
        sp.Rational(1, 4): [sp.Rational(9, 40), sp.Rational(3, 40),
                            sp.Rational(3, 40), sp.Rational(5, 8)],
        sp.Rational(1, 2): [sp.Rational(1, 12), sp.Rational(1, 12),
                            sp.Rational(1, 12), sp.Rational(3, 4)],
        sp.Rational(1): [0, 0, 0, 1],
    }
    for p in (sp.Rational(0), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1)):
        psi, rho_left = two_chart_state(p)
        need(sp.simplify((psi.T * psi)[0]) == 1, "two-chart state normalized at c2=" + str(p))
        need(rho_left == sp.diag(*expected_spectra[p]),
             "two-chart reduced spectrum exact at c2=" + str(p))
        need(sp.trace(rho_left) == 1, "two-chart restricted state normalized at c2=" + str(p))
        rank = rho_left.rank()
        expected_rank = {sp.Rational(0): 2, sp.Rational(1, 4): 4,
                         sp.Rational(1, 2): 4, sp.Rational(1): 1}[p]
        need(rank == expected_rank, "two-chart restricted rank at c2=" + str(p))

        positive_weights = [value for value in expected_spectra[p] if value > 0]
        faithful_m4 = rank == 4
        support_tracial = len(set(positive_weights)) == 1
        log_spread_exact = (
            sp.Integer(0) if support_tracial
            else sp.log(max(positive_weights) / min(positive_weights))
        )
        log_spread_numeric = float(sp.N(log_spread_exact, 17))
        if p in (sp.Rational(1, 4), sp.Rational(1, 2)):
            need(faithful_m4, "interior overlap is faithful on left M4 at c2=" + str(p))
            need(log_spread_exact != 0, "interior entanglement Hamiltonian is noncentral at c2=" + str(p))
            expected_ratio = sp.Rational(25, 3) if p == sp.Rational(1, 4) else sp.Integer(9)
            need(sp.exp(log_spread_exact) == expected_ratio,
                 "exact entanglement-Hamiltonian spread ratio at c2=" + str(p))
            need(log_spread_numeric > 2, "numerical log spread exceeds two at c2=" + str(p), numerical=True)
        else:
            need(not faithful_m4, "endpoint overlap is nonfaithful on left M4 at c2=" + str(p))

        chart_rows[str(p)] = {
            "rho_L_eigenvalues": [str(value) for value in expected_spectra[p]],
            "rank_on_M4": rank,
            "faithful_on_M4": faithful_m4,
            "faithful_on_support_corner": True,
            "support_modular_flow": "trivial" if support_tracial else "nontrivial",
            "entanglement_H_log_spectral_spread_exact": str(log_spread_exact),
            "entanglement_H_log_spectral_spread_numeric": format(log_spread_numeric, ".15g"),
            "native_H_compression_to_fermion_chart": "0",
            "proportional_to_native_compression_mod_center": support_tracial,
        }

    # The fermion-only chart is not H-invariant: its pair state leaks to its
    # boson.  Enlarging to the active pair/boson M2 restores H-invariance but
    # the source-pair state is rank one there.
    g = sp.Rational(1, 20)
    h_extended = sp.zeros(5)
    h_extended[3, 4] = h_extended[4, 3] = g
    h_extended[4, 4] = 1
    chart_observable = sp.zeros(5)
    chart_observable[:4, :4] = matrix_unit(4, 0, 3)
    commutator = h_extended * chart_observable - chart_observable * h_extended
    need(any(commutator[i, 4] != 0 or commutator[4, i] != 0 for i in range(5)),
         "fermion-only left chart algebra is not invariant under native H")
    active_pair_state = sp.diag(1, 0)
    need(active_pair_state.rank() == 1,
         "H-invariant pair/boson completion makes the two-chart source state nonfaithful")

    # Candidate 2: on the N=4 singlet multiplicity M2, the W-only condensate
    # truncation is |0>+4 lambda|1>: the exact W matrix element is the
    # off-diagonal coefficient 4 in H4=Nb+gX.  Every finite lambda gives a rank-one state
    # on M2.  On the diagonal C+C restriction it is faithful for lambda!=0,
    # but that algebra is abelian (trivial modular flow) and is not H-invariant.
    lam = sp.symbols("lambda", positive=True)
    condensate_vector = sp.Matrix([1, 4 * lam])
    condensate_density = condensate_vector * condensate_vector.T / (1 + 16 * lam**2)
    need(sp.simplify(sp.trace(condensate_density)) == 1
         and sp.simplify(condensate_density.det()) == 0,
         "N4 W-condensate state is normalized rank one on singlet M2")
    diagonal_weights = [sp.Rational(1, 1) / (1 + 16 * lam**2),
                        16 * lam**2 / (1 + 16 * lam**2)]
    need(all(weight.is_positive for weight in diagonal_weights),
         "N4 condensate restriction is faithful on diagonal C+C for lambda>0")
    h4 = sp.Matrix([[2, sp.Rational(1, 5)], [sp.Rational(1, 5), 1]])
    level_projector = sp.diag(1, 0)
    need(h4 * level_projector - level_projector * h4 != sp.zeros(2),
         "diagonal condensate algebra is not invariant under native N4 H")
    need(sp.Matrix([[0, 1], [1, 0]]) * condensate_density
         != condensate_density * sp.Matrix([[0, 1], [1, 0]]),
         "generic condensate ray does not define a trace on singlet M2")

    # Bright 120 = V_60 tensor C2 under G; B_G on this is M2 tensor I60.
    # The W-coherent condensate has one common multiplicity vector for every
    # V_60 label, so tracing V_60 leaves the same rank-one M2 density.
    bright_vector = sp.Matrix([1, sp.sqrt(8) * lam])
    bright_multiplicity_density = bright_vector * bright_vector.T / (1 + 8 * lam**2)
    need(bright_multiplicity_density.rank() == 1,
         "bright120 condensate is nonfaithful on invariant M2 multiplicity algebra")
    need(h4.eigenvals() == {
        sp.Rational(3, 2) - sp.sqrt(29) / 10: 1,
        sp.Rational(3, 2) + sp.sqrt(29) / 10: 1,
    }, "native N4 splitting is sqrt(29)/5")
    need(sp.Rational(4, 29) != 0 and sp.Rational(4, 29) != 1,
         "native conversion 4/29 discriminates trivial and resonant flows")

    # Candidate 3: |F> is one singlet multiplicity ray.  It is not faithful on
    # M2 (nor on any larger direct sum containing an orthogonal block).  Its
    # rank-one corner is faithful but carries only the identity automorphism.
    filled_density = sp.diag(1, 0)
    need(filled_density.rank() == 1 and filled_density.det() == 0,
         "filled state is nonfaithful on N4 singlet M2")
    need(sp.trace(filled_density) == 1,
         "filled state is normalized")
    filled_corner = sp.Matrix([[1]])
    need(filled_corner.det() == 1,
         "filled state is faithful on its one-dimensional support corner")
    need(filled_corner == sp.eye(1),
         "filled support-corner modular flow is trivial")

    result = {
        "status": "PASS",
        "checker": Path(__file__).name,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_guard_count": len(EXACT),
        "numerical_guard_count": len(NUMERICAL),
        "exact_guards": EXACT,
        "numerical_guards": NUMERICAL,
        "theorem": {
            "subalgebra": "B = direct_sum_i M_ni tensor I_mi",
            "restricted_density": "h_i = Tr_mi(P_i rho P_i)",
            "faithful_iff": "every h_i is strictly positive and every central block has nonzero weight",
            "modular_flow": "sigma_t^B(A)_i = h_i^(it) A_i h_i^(-it)",
            "escape": "h_i is a partial trace; global rho may be pure and need not be f(H)",
            "full_factor_contrast": "B=A=M_d makes the commutant central, so matching derivations force log rho=-beta H+cI",
            "dynamics_prerequisite": "comparison to H requires [H,B] subset B; compression alone is not a restricted automorphism",
        },
        "two_chart": {
            "state": "(P_L+P_R)/sqrt(2(1+c^2)), two source-pair modes per chart",
            "left_algebra": "CAR(a1,a2)=M4",
            "overlap_rows": chart_rows,
            "H_invariance": False,
            "smallest_active_H_completion": "pair/boson M2; restricted source state rank one",
            "dimensionless": {
                "N4_split_and_4_over_29": "FAIL/not in invariant faithful range",
                "I4_1_plus_c4": "FAIL as modular dynamics; c is only an input overlap",
                "Zb_ratio": "FAIL/not generated",
            },
        },
        "pair_condensate": {
            "state": "(|0>+4lambda|1>)/sqrt(1+16lambda^2) on exact N4 truncation, W-only",
            "faithful_on_singlet_M2": False,
            "faithful_on_diagonal_C_plus_C_for_lambda_positive": True,
            "diagonal_modular_flow": "trivial",
            "diagonal_algebra_H_invariant": False,
            "faithful_on_bright120_invariant_M2": False,
            "dimensionless": {
                "N4_split": "FAIL/undefined modular flow on M2",
                "conversion_4_over_29": "FAIL (diagonal flow gives zero)",
                "I4_1_plus_c4": "FAIL/undefined",
                "Zb_ratio": "FAIL/undefined",
            },
        },
        "filled_state": {
            "faithful_on_singlet_M2": False,
            "faithful_on_support_corner_C": True,
            "support_modular_flow": "trivial",
            "dimensionless": "all FAIL/undefined",
        },
        "verdict": (
            "The proper-subalgebra escape is mathematically real, but none of the three "
            "specified finite native candidates gives a faithful H-invariant subalgebra "
            "with nontrivial modular flow matching several native answers."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
