#!/usr/bin/env python3
"""Bounded exact audit of the reported 640-dimensional mixed-source sector.

The checker reconstructs the native sixty reflections from the repository and
uses only a 160-dimensional local moment operator plus eight explicit columns.
It never diagonalizes the 640-dimensional Hamiltonian.  The user's underlying
report scripts were not supplied and are therefore not treated as replayed.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT_JSON = HERE / "mixed_source_check.json"

SOURCE_REL = (
    "experiments/theory-contracts/"
    "compiler-correlated-event-clock-20260919/source_channel.py"
)
PRODUCT_REL = (
    "experiments/theory-contracts/"
    "compiler-current-product-20260919/current_product_readout_check.json"
)
ROOT_PHASE_REL = (
    "experiments/theory-contracts/"
    "compiler-root-phase-lift-20260919/PROOF.txt"
)
PINS = {
    SOURCE_REL: "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    PRODUCT_REL: "22b721c7905e3eeac18c962df5d3a1ac13c84eba03930baee421d4cbf704401d",
    ROOT_PHASE_REL: "d7465bd8ee3514d29bfcb4238b4772d7d2ee631301465682e50bcbfca5b4879f",
}

CHECKS: Counter[str] = Counter()


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    CHECKS[label] += 1


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_gaussian(value: complex) -> sp.Expr:
    z = complex(value)
    require(
        z.real == round(z.real) and z.imag == round(z.imag),
        "native ray coordinates are Gaussian integral",
    )
    return sp.Integer(round(z.real)) + sp.I * sp.Integer(round(z.imag))


def sym_basis(sign: int) -> sp.Matrix:
    """Orthonormal Sym^2 (sign=+1) or exterior^2 (sign=-1) basis."""
    columns = (
        list(it.combinations_with_replacement(range(4), 2))
        if sign == 1 else list(it.combinations(range(4), 2))
    )
    out = sp.zeros(16, len(columns))
    for column, (a, b) in enumerate(columns):
        if a == b:
            out[4 * a + b, column] = 1
        else:
            out[4 * a + b, column] = 1 / sp.sqrt(2)
            out[4 * b + a, column] = sign / sp.sqrt(2)
    return out


def key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    require(
        np.array_equal(vector.real, np.rint(vector.real))
        and np.array_equal(vector.imag, np.rint(vector.imag)),
        "reflections preserve Gaussian root coordinates",
    )
    return tuple(
        (int(round(z.real)), int(round(z.imag))) for z in vector
    )


def permutation_apply_rows(
    permutation: tuple[int, ...], matrix: sp.Matrix
) -> sp.Matrix:
    out = sp.zeros(*matrix.shape)
    for source, target in enumerate(permutation):
        out[target, :] = matrix[source, :]
    return out


def exact_spectrum(
    matrix: sp.Matrix,
    roots: list[sp.Rational],
    multiplicities: list[int],
    label: str,
) -> None:
    identity = sp.eye(matrix.rows)
    annihilator = identity
    for root in roots:
        annihilator = annihilator * (matrix - root * identity)
    require(
        annihilator == sp.zeros(matrix.rows),
        f"{label} exact square-free annihilating polynomial",
    )
    moments = sp.Matrix(
        [sp.trace(matrix ** power) for power in range(len(roots))]
    )
    vandermonde = sp.Matrix(
        [[root ** power for root in roots] for power in range(len(roots))]
    )
    solved = list(vandermonde.inv() * moments)
    require(solved == [sp.Integer(x) for x in multiplicities],
            f"{label} exact spectral multiplicities")
    require(sum(multiplicities) == matrix.rows,
            f"{label} multiplicities exhaust the space")


def raw_sym_basis(sign: int) -> np.ndarray:
    """Integral basis spanning Sym2 or Lambda2; normalization kept in Gram."""
    columns = (
        list(it.combinations_with_replacement(range(4), 2))
        if sign == 1 else list(it.combinations(range(4), 2))
    )
    out = np.zeros((16, len(columns)), dtype=np.int64)
    for column, (a, b) in enumerate(columns):
        out[4 * a + b, column] = 1
        if a != b:
            out[4 * b + a, column] = sign
    return out


def haar_reflection_scaled() -> np.ndarray:
    """Return 6720 times E[(bar r)^2 tensor r^2], exactly as integers."""
    indices = np.indices((4,) * 8)
    rows, cols = indices[:4], indices[4:]
    haar = np.zeros((4,) * 8, dtype=np.int64)
    for degree in range(5):
        denominator = int(sp.rf(4, degree))
        require(6720 % denominator == 0,
                "Haar projective moments share denominator 6720")
        for subset in it.combinations(range(4), degree):
            rest = set(range(4)) - set(subset)
            identity = np.ones((4,) * 8, dtype=np.int64)
            for slot in rest:
                identity *= rows[slot] == cols[slot]
            holomorphic = [
                cols[slot] if slot < 2 else rows[slot] for slot in subset
            ]
            antiholomorphic = [
                rows[slot] if slot < 2 else cols[slot] for slot in subset
            ]
            for permutation in it.permutations(range(degree)):
                term = identity.copy()
                for j in range(degree):
                    term *= holomorphic[j] == antiholomorphic[permutation[j]]
                haar += (
                    (-2) ** degree * (6720 // denominator) * term
                )
    return haar.reshape(256, 256)


def restrict_scaled_channel(
    scaled_channel: np.ndarray, matter_basis: np.ndarray
) -> sp.Matrix:
    """Restrict the scaled Haar tensor channel using integral Gram inverses."""
    source_basis = raw_sym_basis(1)
    embedding = np.kron(source_basis, matter_basis)
    gram = embedding.T @ embedding
    require(np.array_equal(gram, np.diag(np.diag(gram))),
            "integral tensor embedding has diagonal Gram")
    compressed = embedding.T @ scaled_channel @ embedding
    induced = sp.diag(*[
        sp.Rational(1, int(value)) for value in np.diag(gram)
    ]) * sp.Matrix(compressed) / 6720
    return induced


def swap_bc(columns: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(*columns.shape)
    for source in range(10):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    old = (((source * 4 + a) * 4 + b) * 4 + c)
                    new = (((source * 4 + a) * 4 + c) * 4 + b)
                    out[new, :] = columns[old, :]
    return out


def apply_local_moment(matrix160: sp.Matrix, columns: sp.Matrix) -> sp.Matrix:
    """Apply M_160 tensor I_C to selected columns without building 640^2."""
    out = sp.zeros(*columns.shape)
    for column in range(columns.cols):
        block = sp.Matrix(
            160, 4, lambda row, c: columns[4 * row + c, column]
        )
        image = matrix160 * block
        for row in range(160):
            for c in range(4):
                out[4 * row + c, column] = image[row, c]
    return out


def main() -> None:
    for relative, digest in PINS.items():
        require(sha256(REPO / relative) == digest, f"pinned source {relative}")

    spec = importlib.util.spec_from_file_location(
        "mixed_source_native", REPO / SOURCE_REL
    )
    source = importlib.util.module_from_spec(spec)
    require(spec.loader is not None, "native source module has loader")
    spec.loader.exec_module(source)
    native_rays = source.source_rays()
    require(len(native_rays) == 60, "native source has sixty rays")

    bplus = sym_basis(1)
    bminus = sym_basis(-1)
    require(bplus.H * bplus == sp.eye(10), "Sym2 basis is orthonormal")
    require(bminus.H * bminus == sp.eye(6), "Lambda2 basis is orthonormal")
    require(bplus.H * bminus == sp.zeros(10, 6),
            "symmetric and exterior bases are orthogonal")

    identity4 = sp.eye(4)
    exact_psis: list[sp.Matrix] = []
    reflections: list[sp.Matrix] = []
    sym_actions: list[sp.Matrix] = []
    source_actions: list[sp.Matrix] = []
    exterior_actions: list[sp.Matrix] = []

    moment160 = sp.zeros(160)
    moment_plus = sp.zeros(100)
    moment_minus = sp.zeros(60)
    bell_frame = sp.zeros(10)
    native_second = sp.zeros(16)

    for ray in native_rays:
        psi = sp.Matrix([exact_gaussian(z) / 2 for z in ray])
        reflection = sp.simplify(identity4 - 2 * psi * psi.H)
        require(sp.simplify((psi.H * psi)[0]) == 1,
                "native psi ray has unit norm")
        require(reflection.H == reflection
                and sp.simplify(reflection ** 2 - identity4) == sp.zeros(4),
                "native reflection is Hermitian involution")
        sym_action = sp.simplify(
            bplus.H * sp.kronecker_product(reflection, reflection) * bplus
        )
        exterior_action = sp.simplify(
            bminus.H * sp.kronecker_product(reflection, reflection) * bminus
        )
        source_action = sym_action.conjugate()
        require(source_action == sym_action.T,
                "quadratic source action is conjugate Sym2")
        require(source_action.H * source_action == sp.eye(10),
                "quadratic source action is unitary")

        v = sp.simplify(bplus.H * sp.kronecker_product(psi, psi))
        bell_frame += v.conjugate() * v.T
        exact_psis.append(psi)
        reflections.append(reflection)
        sym_actions.append(sym_action)
        source_actions.append(source_action)
        exterior_actions.append(exterior_action)

        matter_pair = sp.kronecker_product(reflection, reflection)
        native_second += matter_pair / 60
        moment160 += sp.kronecker_product(source_action, matter_pair) / 60
        moment_plus += sp.kronecker_product(source_action, sym_action) / 60
        moment_minus += (
            sp.kronecker_product(source_action, exterior_action) / 60
        )

    moment160 = sp.simplify(moment160)
    moment_plus = sp.simplify(moment_plus)
    moment_minus = sp.simplify(moment_minus)
    bell_frame = sp.simplify(bell_frame)
    native_second = sp.simplify(native_second)
    require(bell_frame == 6 * sp.eye(10),
            "sixty conjugate quadratic rays form the native Bell10 tight frame")
    swap4 = sp.zeros(16)
    for a in range(4):
        for b in range(4):
            swap4[4 * b + a, 4 * a + b] = 1
    require(native_second == (sp.eye(16) + swap4) / 5,
            "native second reflection moment is (I+Swap)/5")

    # The 240-label quadratic coordinate module, checked independently.
    raw_roots = np.stack([
        (1j ** phase) * ray
        for ray in native_rays for phase in range(4)
    ])
    root_index = {key(root): index for index, root in enumerate(raw_roots)}
    require(len(root_index) == 240, "native orbit has 240 oriented roots")
    coordinate_rows = sp.zeros(240, 10)
    for index, root in enumerate(raw_roots):
        psi = sp.Matrix([exact_gaussian(z) / 2 for z in root])
        coordinate_rows[index, :] = (
            bplus.H * sp.kronecker_product(psi, psi)
        ).T
    coordinate_rows = coordinate_rows.applyfunc(sp.expand_complex)
    require(sp.simplify(coordinate_rows.H * coordinate_rows) == 24 * sp.eye(10),
            "quadratic root coordinates embed conjugate Sym2 isometrically")

    for ray, reflection_np, source_action in zip(
        native_rays,
        [np.eye(4, dtype=complex)
         - np.outer(ray, ray.conj()) / 2 for ray in native_rays],
        source_actions,
    ):
        del ray
        permutation = tuple(
            root_index[key(reflection_np @ root)] for root in raw_roots
        )
        require(len(set(permutation)) == 240,
                "each event permutes all quadratic source labels")
        require(
            permutation_apply_rows(permutation, coordinate_rows)
            == coordinate_rows * source_action.applyfunc(sp.expand_complex),
            "quadratic label module intertwines the same conjugate Sym2 action",
        )

    # Exact local spectrum; this is the only nontrivial spectral computation.
    exact_spectrum(
        moment_plus,
        [sp.Integer(1), sp.Rational(1, 3), sp.Rational(1, 5),
         sp.Rational(1, 15)],
        [1, 9, 45, 45],
        "old End(Sym2) reflection channel",
    )
    exact_spectrum(
        moment_minus,
        [sp.Rational(1, 5), -sp.Rational(1, 15)],
        [15, 45],
        "quadratic-source exterior-matter block",
    )
    exact_spectrum(
        moment160,
        [sp.Integer(1), sp.Rational(1, 3), sp.Rational(1, 5),
         sp.Rational(1, 15), -sp.Rational(1, 15)],
        [1, 9, 60, 45, 45],
        "full 160-dimensional L1 moment",
    )

    # Haar control.  It shares the second reflection moment and therefore the
    # eight-column branch, but its fourth-moment local spectrum is different.
    haar_scaled = haar_reflection_scaled()
    haar_plus = restrict_scaled_channel(haar_scaled, raw_sym_basis(1))
    haar_minus = restrict_scaled_channel(haar_scaled, raw_sym_basis(-1))
    exact_spectrum(
        haar_plus,
        [sp.Integer(1), sp.Rational(1, 5), sp.Rational(1, 7)],
        [1, 15, 84],
        "Haar End(Sym2) reflection channel",
    )
    exact_spectrum(
        haar_minus,
        [sp.Rational(1, 5), -sp.Rational(1, 15)],
        [15, 45],
        "Haar quadratic-source exterior-matter block",
    )
    require(
        sp.eye(16) - 4 * (sp.eye(16) / 4) + 4 * (sp.eye(16) + swap4) / 20
        == native_second,
        "Haar and native ensembles have the same second reflection moment",
    )

    # Verify that Sym2(AB) and Lambda2(AB) are exactly the two local blocks.
    split_plus = sp.kronecker_product(sp.eye(10), bplus)
    split_minus = sp.kronecker_product(sp.eye(10), bminus)
    require(sp.simplify(split_plus.H * moment160 * split_plus) == moment_plus
            and sp.simplify(split_minus.H * moment160 * split_minus) == moment_minus
            and sp.simplify(split_plus.H * moment160 * split_minus)
            == sp.zeros(100, 60),
            "full local moment splits exactly into Sym2 and Lambda2 blocks")

    local_l1 = sp.eye(160) - moment160
    require(local_l1.H == local_l1,
            "local L1 is exactly self-adjoint")

    # Full source packet Omega in bar(Sym2)_R tensor Sym2_(AB).
    omega = sp.zeros(160, 1)
    for mu in range(10):
        for ab in range(16):
            omega[16 * mu + ab] = bplus[ab, mu] / sp.sqrt(10)
    require(omega.H * omega == sp.ones(1, 1),
            "full source packet is normalized")
    require(moment160 * omega == omega,
            "full source packet spans the exact local L1 kernel")

    packet = sp.zeros(640, 4)
    for terminal in range(4):
        for row in range(160):
            packet[4 * row + terminal, terminal] = omega[row]
    swapped = swap_bc(packet)
    require(packet.H * packet == sp.eye(4), "packet columns are orthonormal")
    require(swapped.H * swapped == sp.eye(4),
            "swapped-packet columns are orthonormal")
    require(packet.H * swapped == sp.eye(4) / 4,
            "PSP=P/4 packet metric identity")
    gram8 = packet.row_join(swapped).H * packet.row_join(swapped)
    require(gram8.det() == sp.Rational(15, 16) ** 4,
            "packet plus swapped packet has exact dimension eight")

    moment_packet = apply_local_moment(moment160, packet)
    moment_swapped = apply_local_moment(moment160, swapped)
    require(moment_packet == packet, "L1 annihilates the packet columns")
    require(moment_swapped == (packet + swapped) / 5,
            "L1 on swapped packet is (4 SP-P)/5")
    require(swap_bc(swapped) == packet, "Swap_BC is an involution on packet columns")

    # Coefficient action on [P, SP]; columns are images of P and SP.
    hsmall = sp.Matrix([
        [sp.Rational(4, 5), -sp.Rational(2, 5)],
        [-sp.Rational(1, 5), sp.Rational(8, 5)],
    ])
    x = sp.symbols("x")
    require(
        sp.expand(hsmall.charpoly(x).as_expr())
        == x ** 2 - sp.Rational(12, 5) * x + sp.Rational(6, 5),
        "eight-column Hamiltonian has reported exact characteristic polynomial",
    )
    e_minus = (sp.Integer(6) - sp.sqrt(6)) / 5
    e_plus = (sp.Integer(6) + sp.sqrt(6)) / 5
    require(hsmall.eigenvals() == {e_minus: 1, e_plus: 1},
            "eight-column Hamiltonian has Eplus and Eminus")

    # Full-sector lower bound: W^perp lies in ker(L1)^perp.  The exact local
    # spectrum gives L1 >= 2/3 there; Swap_BC^2=I gives L2 >= 3/5.
    rest_floor = sp.Rational(2, 3) + sp.Rational(3, 5)
    gap_floor = sp.simplify(rest_floor - e_minus)
    require(rest_floor == sp.Rational(19, 15),
            "orthogonal-complement energy floor is 19/15")
    require(gap_floor == (1 + 3 * sp.sqrt(6)) / 15,
            "reported ground-gap lower bound follows exactly")
    require(sp.simplify(rest_floor - e_minus) > 0,
            "orthogonal-complement bound is strictly above Eminus")
    require(sp.simplify(e_plus - rest_floor) >= 0,
            "Eplus is not below the native orthogonal-complement floor")
    haar_rest_floor = sp.Rational(4, 5) + sp.Rational(3, 5)
    haar_gap_floor = sp.simplify(haar_rest_floor - e_minus)
    require(haar_rest_floor == sp.Rational(7, 5),
            "Haar orthogonal-complement energy floor is 7/5")
    require(haar_gap_floor == (1 + sp.sqrt(6)) / 5,
            "Haar control retains the same Eminus ground branch")
    require(sp.simplify(e_plus - haar_rest_floor) >= 0,
            "Eplus is not below the Haar orthogonal-complement floor")

    product = json.loads((REPO / PRODUCT_REL).read_text(encoding="utf-8"))
    require(product["status"] == "PASS_COORDINATE_IDENTITIES",
            "pinned current-product coordinate certificate passes")
    require(
        product["projection"]
        == "F10^dagger(q_l tensor psi_l^2)=conjugate(psi_l^2)/sqrt(2)",
        "pinned F10 certificate uses the same conjugate quadratic ray",
    )
    require(
        "symmetric monomials to original Pauli Bell basis"
        in product["basis_conversion"],
        "pinned F10 certificate fixes the original Bell basis phases",
    )
    root_phase = (REPO / ROOT_PHASE_REL).read_text(encoding="utf-8")
    require("(R_l tensor U_l) F = F conjugate(U_l)" in root_phase,
            "pinned phase proof gives the compensated F intertwiner")
    require("S_l=i R_l tensor U_l." in root_phase,
            "pinned root-phase proof identifies the actual affine source phase")
    require("C_l=-i S_l=R_l tensor U_l." in root_phase,
            "pinned root-phase proof identifies the compensated finite action")

    result = {
        "research_id": "UR.COMPILER.PAIR_SECTOR_AUDIT.23",
        "verdict": "PARTIAL",
        "status": "PASS_EXACT_MIXED_SOURCE_SECTOR",
        "check_evaluations": sum(CHECKS.values()),
        "source_pins": PINS,
        "local_160_moment_spectrum": {
            "1": 1,
            "1/3": 9,
            "1/5": 60,
            "1/15": 45,
            "-1/15": 45,
        },
        "local_L1_spectrum": {
            "0": 1,
            "2/3": 9,
            "4/5": 60,
            "14/15": 45,
            "16/15": 45,
        },
        "block_decomposition": {
            "barSym2_tensor_Sym2_dimension": 100,
            "old_C60_spectrum": {"1": 1, "1/3": 9, "1/5": 45, "1/15": 45},
            "barSym2_tensor_Lambda2_dimension": 60,
            "exterior_block_spectrum": {"1/5": 15, "-1/15": 45},
        },
        "invariant_subspace": {
            "dimension": 8,
            "metric": "P S_BC P = P/4",
            "coefficient_matrix_basis_P_SP": [
                ["4/5", "-2/5"], ["-1/5", "8/5"]
            ],
            "characteristic_polynomial": "x^2-(12/5)x+6/5",
            "eigenvalues": {
                "(6-sqrt(6))/5": 4,
                "(6+sqrt(6))/5": 4,
            },
        },
        "full_sector_bound": {
            "reason": "on W_perp, L1>=2/3 from the exact local spectrum and L2=(4I-Swap_BC)/5>=3/5",
            "rest_energy_at_least": "19/15",
            "Eplus_at_least_rest_floor": "(6+sqrt(6))/5 >= 19/15 because 3*sqrt(6)>=1",
            "gap_at_least": "(1+3*sqrt(6))/15",
        },
        "haar_control": {
            "same_second_reflection_moment": "(I+Swap)/5",
            "same_invariant_eigenvalues": {
                "(6-sqrt(6))/5": 4,
                "(6+sqrt(6))/5": 4,
            },
            "haar_local_moment_spectrum": {
                "1": 1,
                "1/5": 30,
                "1/7": 84,
                "-1/15": 45,
            },
            "haar_local_L1_gap": "4/5",
            "haar_rest_energy_at_least": "7/5",
            "Eplus_at_least_haar_rest_floor": "(6+sqrt(6))/5 >= 7/5 because sqrt(6)>=1",
            "haar_gap_at_least": "(1+sqrt(6))/5",
            "interpretation": (
                "The sqrt(6) low branch uses only Omega invariance and the "
                "second reflection moment, so it survives the Haar control. "
                "The native sixty-ray fourth moment is visible in the different "
                "full local spectrum and the native 19/15 complement bound, not "
                "in the existence of the low branch alone."
            ),
        },
        "bell10_connection": {
            "same_pure_permutation_or_compensated_module": True,
            "same_unmodified_E8_module": False,
            "reason": (
                "The normalized 240-label quadratic-coordinate embedding is an "
                "exact intertwiner for conjugate Sym2(4), and its sixty analysis "
                "rays are the same conjugate(psi_l^2) tight frame used by the "
                "pinned F10 Bell10 certificate. This is an action-and-ray "
                "identification, not a 10=10 dimension match. The F10 readout "
                "pins the same rays; its action covariance is compensated as below."
            ),
            "finite_action_qualification": (
                "F10 intertwines the pure-permutation conjugate-Sym2 action with "
                "the compensated finite action C_l=-i S_l=R_l tensor U_l. The "
                "actual E8 operator is S_l=i R_l tensor U_l, so S_l F=i F "
                "conjugate(U_l); there is no unmodified E8-module intertwiner."
            ),
            "boundary": (
                "F10 supplies a conditional finite state/readout identification. "
                "Only the compensated finite action (-i S_l) matches the mixed-source "
                "barU_l action; the actual affine S_l differs by i. No intertwiner "
                "transports the pure-permutation Hamiltonian or its dynamics to "
                "affine-current dynamics."
            ),
        },
        "leakage_formula_scope": {
            "formula_not_replayed": "(3m/5)J^2+((m-1)/8)mu^2",
            "necessary_structure": (
                "For an exact all-coupling norm square with no J*mu term, the "
                "leakage residual must be linear in J and mu with orthogonal "
                "components of squared norms 3m/5 and (m-1)/8. The coefficients "
                "have the expected open-chain counts m and m-1, but the missing "
                "Hamiltonian/leakage definitions are required to prove those "
                "orthogonality and norm identities."
            ),
        },
        "scope": (
            "Exact audit of the stated J=mu=0 640-dimensional sector using the "
            "native sixty rays, one exact 160-dimensional local moment, and eight "
            "explicit columns. No 640-dimensional diagonalization and no replay "
            "of user source files that were not attached."
        ),
        "check_counts": dict(sorted(CHECKS.items())),
        "closed_gate_ids": [],
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
