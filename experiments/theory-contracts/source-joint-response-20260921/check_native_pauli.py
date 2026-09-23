#!/usr/bin/env python3
"""Exact finite audit of the native signed W tensor and Pauli commutator.

Scope:
  * load the archived native 60 x 2016 tensor and compare it byte-exactly to
    the in-repository Clifford reconstruction;
  * test the complete Q_A matrices and their Pauli commutator coefficients;
  * check the matrix order Q_B^dagger Q_A by a direct complex CAR model;
  * pull the previously certified dressed lattice signs back to the raw
    affine E8 root-current bracket and retain the full D5 + D3 root action.

This is a finite algebra audit.  It does not identify the affine currents
with canonical fermion fields or derive a physical Hamiltonian/time.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import numpy as np
import sympy as sp


REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
NATIVE_SOURCE = REPO / "experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py"
DRESSED_CHECKER = REPO / "experiments/theory-contracts/source-dressed-native-20260920/checker.py"
TENSOR_ARCHIVE = REPO / "experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz"

PINS = {
    str(NATIVE_SOURCE.relative_to(REPO)): "380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672",
    str(DRESSED_CHECKER.relative_to(REPO)): "15f8900cce161696a084e421bc21a501a0a841b40a74b29aebdf27e47a1a319d",
    str(TENSOR_ARCHIVE.relative_to(REPO)): "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763",
}


def require(condition: bool, message: str) -> None:
    if not bool(condition):
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_sources() -> None:
    for relative, expected in PINS.items():
        actual = sha256(REPO / relative)
        require(actual == expected, f"source pin mismatch: {relative}")


def load_native() -> tuple[dict[str, object], np.ndarray]:
    text = NATIVE_SOURCE.read_text()
    prefix, marker, _ = text.partition("# --- Root-opposite boson pairing")
    require(bool(marker), "native prefix boundary missing")
    namespace: dict[str, object] = {
        "__file__": str(NATIVE_SOURCE),
        "__name__": "native_source_prefix",
    }
    exec(compile(prefix, str(NATIVE_SOURCE), "exec", optimize=0), namespace)
    require(len(namespace["checks"]) == 6, "six native prefix guards not retained")
    rebuilt = np.asarray(namespace["W"], dtype=np.int64)
    with np.load(TENSOR_ARCHIVE, allow_pickle=False) as archive:
        stored_raw = archive["W"]
    require(np.all(stored_raw.imag == 0), "archived W has an imaginary entry")
    require(np.all(stored_raw.real == np.rint(stored_raw.real)), "archived W is not integer valued")
    stored = stored_raw.real.astype(np.int64)
    require(np.array_equal(stored, rebuilt), "archived signed W differs from Clifford reconstruction")
    require(np.array_equal(stored @ stored.T, 8 * np.eye(60, dtype=np.int64)), "W W^T != 8 I60")
    return namespace, stored


def solve_binary(rows: list[tuple[int, int]]) -> tuple[int, int]:
    """Solve mask dot x = rhs over F2, with free variables fixed to zero."""
    basis: dict[int, tuple[int, int]] = {}
    for mask, rhs in rows:
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in basis:
                mask ^= basis[pivot][0]
                rhs ^= basis[pivot][1]
            else:
                basis[pivot] = (mask, rhs)
                break
        if not mask and rhs:
            raise ValueError("inconsistent sign equations")
    solution = 0
    for pivot, (mask, rhs) in sorted(basis.items()):
        if rhs ^ ((mask & solution).bit_count() & 1):
            solution |= 1 << pivot
    require(
        all(((mask & solution).bit_count() & 1) == rhs for mask, rhs in rows),
        "binary sign solution failed replay",
    )
    return solution, len(basis)


def jordan_wigner_annihilators(mode_count: int) -> list[sp.Matrix]:
    dimension = 1 << mode_count
    operators: list[sp.Matrix] = []
    for mode in range(mode_count):
        operator = sp.zeros(dimension)
        for mask in range(dimension):
            if (mask >> mode) & 1:
                lower = mask & ((1 << mode) - 1)
                operator[mask ^ (1 << mode), mask] = (-1) ** lower.bit_count()
        operators.append(operator)
    return operators


def antisymmetric(entries: dict[tuple[int, int], sp.Expr], dimension: int) -> sp.Matrix:
    out = sp.zeros(dimension)
    for (i, j), value in entries.items():
        require(i < j, "complex test entry must use i < j")
        out[i, j] = value
        out[j, i] = -value
    return out


def pair_operator(q: sp.Matrix, annihilators: list[sp.Matrix]) -> sp.Matrix:
    out = sp.zeros(annihilators[0].rows)
    for i, j in combinations(range(q.rows), 2):
        out += q[i, j] * annihilators[j] * annihilators[i]
    return out


def direct_complex_order_control() -> dict[str, object]:
    """Directly decide the dagger/order convention in a complex CAR model."""
    annihilators = jordan_wigner_annihilators(4)
    qa = antisymmetric(
        {(0, 1): 1 + sp.I, (0, 2): 2 - sp.I, (1, 3): -1, (2, 3): 3 * sp.I},
        4,
    )
    qb = antisymmetric(
        {(0, 1): 2 - sp.I, (0, 3): 1 + 2 * sp.I, (1, 2): -2, (2, 3): 1},
        4,
    )
    pa = pair_operator(qa, annihilators)
    pb = pair_operator(qb, annihilators)
    direct = pa * pb.H - pb.H * pa

    ordered = qb.H * qa
    predicted = sp.trace(ordered) * sp.eye(direct.rows) / 2
    for i in range(4):
        for j in range(4):
            predicted -= ordered[i, j] * annihilators[i].H * annihilators[j]
    require(sp.simplify(direct - predicted) == sp.zeros(direct.rows), "complex CAR formula/order failed")

    reversed_product = qa.H * qb
    reversed_prediction = sp.trace(reversed_product) * sp.eye(direct.rows) / 2
    for i in range(4):
        for j in range(4):
            reversed_prediction -= reversed_product[i, j] * annihilators[i].H * annihilators[j]
    difference = sp.simplify(direct - reversed_prediction)
    require(difference != sp.zeros(direct.rows), "complex negative control did not distinguish reversed order")
    witness = next((i, j, difference[i, j]) for i in range(difference.rows) for j in range(difference.cols) if difference[i, j] != 0)
    return {
        "modes": 4,
        "direct_identity": "[P_A,P_B^dagger]=Tr(Q_B^dagger Q_A)/2-f^dagger Q_B^dagger Q_A f",
        "ordered_product": "Q_B^dagger Q_A",
        "reversed_order_rejected": True,
        "reversed_order_witness": {"row": witness[0], "column": witness[1], "difference": str(witness[2])},
    }


def exact_sparse_span_rank(matrices: list[np.ndarray]) -> int:
    """Exact Q-rank of sparse integer matrices, without a Lie closure."""
    basis: dict[int, dict[int, Fraction]] = {}
    for matrix in matrices:
        rows, columns = np.nonzero(matrix)
        vector = {
            int(row * matrix.shape[1] + column): Fraction(int(matrix[row, column]))
            for row, column in zip(rows, columns)
        }
        while vector:
            pivot = max(vector)
            if pivot not in basis:
                scale = vector[pivot]
                basis[pivot] = {column: value / scale for column, value in vector.items() if value}
                break
            factor = vector[pivot]
            for column, value in basis[pivot].items():
                reduced = vector.get(column, Fraction(0)) - factor * value
                if reduced:
                    vector[column] = reduced
                elif column in vector:
                    del vector[column]
    return len(basis)


def pauli_audit(w: np.ndarray, pairs: list[tuple[int, int]]) -> dict[str, object]:
    q = np.zeros((60, 64, 64), dtype=np.int64)
    for column, (i, j) in enumerate(pairs):
        q[:, i, j] = w[:, column]
        q[:, j, i] = -w[:, column]
    require(np.array_equal(q + q.transpose(0, 2, 1), np.zeros_like(q)), "Q_A is not antisymmetric")

    trace_gram = np.einsum("aij,bij->ab", q, q, optimize=True)
    require(np.array_equal(trace_gram, 16 * np.eye(60, dtype=np.int64)), "Tr(Q_B^dagger Q_A) != 16 delta_AB")

    channel_projectors = np.einsum("aji,ajk->aik", q, q, optimize=True)
    require(np.all(channel_projectors >= 0), "Q_A^dagger Q_A has a negative entry")
    require(np.all(channel_projectors == np.array([np.diag(np.diag(x)) for x in channel_projectors])), "a native channel is not a matching")
    require(set(np.diag(x).sum() for x in channel_projectors) == {16}, "channel uses other than 16 fermion endpoints")
    sum_rule = channel_projectors.sum(axis=0)
    require(np.array_equal(sum_rule, 15 * np.eye(64, dtype=np.int64)), "sum_A Q_A^dagger Q_A != 15 I64")

    degrees = np.diag(sum_rule)
    ordered_products = [q[b].T @ q[a] for b in range(60) for a in range(60)]
    response_span_rank = exact_sparse_span_rank(ordered_products)
    require(response_span_rank == 736, "span rank of Q_B^dagger Q_A changed")
    complex_control = direct_complex_order_control()
    return {
        "Q_shape": list(q.shape),
        "normalization": "P_A=sum_{i<j}(Q_A)_{ij} f_j f_i; a_A=P_A/sqrt(8)",
        "nonzero_native_pair_coefficients": int(np.count_nonzero(w)),
        "pairs_per_channel": sorted(set(map(int, np.count_nonzero(w, axis=1)))),
        "fermion_endpoint_degree_census": {str(int(value)): int(np.count_nonzero(degrees == value)) for value in sorted(set(degrees))},
        "trace_rule": "Tr(Q_B^dagger Q_A)=16 delta_AB",
        "sum_rule": "sum_A Q_A^dagger Q_A=15 I64",
        "ordered_response_matrix_span": {
            "family": "{Q_B^dagger Q_A : A,B=1,...,60}",
            "exact_Q_rank": response_span_rank,
            "ambient_End_C64_dimension": 4096,
            "lie_closure_computed": False,
        },
        "commutator": "[a_A,a_B^dagger]=delta_AB I-(1/8) f^dagger Q_B^dagger Q_A f",
        "summed_commutator": "sum_A [a_A,a_A^dagger]=60 I-(15/8) N_f",
        "invariant_density_expectation": "<commutator_AB>=(1-<N_f>/32) delta_AB for rho1=(<N_f>/64) I64",
        "vacuum_value": "+delta_AB",
        "filled_value": "-delta_AB",
        "complex_order_control": complex_control,
    }


def lattice_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    a = np.array([1, 1, 1, -1, -1, -1, -1, -1], dtype=np.int64)
    signature = np.array([1] * 9 + [-1], dtype=np.int64)
    er = np.array([0] * 8 + [-1, 0], dtype=np.int64)
    return a, signature, np.diag(signature), er


def f2_image(doubled_weight: np.ndarray, a: np.ndarray) -> np.ndarray:
    ar2 = int(a @ doubled_weight)
    numerator = np.r_[2 * doubled_weight - ar2 * a, 0, -2 * ar2]
    require(not np.any(numerator % 4), "nonintegral F(E8) image")
    return numerator // 4


def epsilon(x: np.ndarray, y: np.ndarray) -> int:
    exponent = sum(int(x[i]) * sum(map(int, y[:i])) for i in range(10)) % 2
    return -1 if exponent else 1


def native_root_operators(namespace: dict[str, object]) -> list[tuple[np.ndarray, np.ndarray]]:
    operators: list[tuple[np.ndarray, np.ndarray]] = []
    for dimension, offset in [(5, 0), (3, 5)]:
        annihilators = namespace["_jw"](dimension)
        even = [j for j in range(2 ** dimension) if j.bit_count() % 2 == 0]
        for i, j in combinations(range(dimension), 2):
            for sign_i, sign_j in product((1, -1), repeat=2):
                root2 = np.zeros(8, dtype=np.int64)
                root2[offset + i] = 2 * sign_i
                root2[offset + j] = 2 * sign_j
                op = (annihilators[i] if sign_i == 1 else annihilators[i].T) @ (annihilators[j] if sign_j == 1 else annihilators[j].T)
                small = op[np.ix_(even, even)]
                if dimension == 5:
                    op = np.kron(small, np.eye(4, dtype=np.int64))
                else:
                    op = np.kron(np.eye(16, dtype=np.int64), small)
                operators.append((root2, op))
    require(len(operators) == 52, "expected 40 D5 and 12 D3 roots")
    return operators


def induced_boson_action(w: np.ndarray, op: np.ndarray, pairs: list[tuple[int, int]], pair_index: dict[tuple[int, int], int]) -> np.ndarray:
    lifted = np.zeros_like(w)
    for column, (i, j) in enumerate(pairs):
        for h in np.flatnonzero(op[:, i]):
            h = int(h)
            if h != j:
                pair = tuple(sorted((h, j)))
                lifted[:, column] += int(op[h, i]) * (1 if h < j else -1) * w[:, pair_index[pair]]
        for h in np.flatnonzero(op[:, j]):
            h = int(h)
            if i != h:
                pair = tuple(sorted((i, h)))
                lifted[:, column] += int(op[h, j]) * (1 if i < h else -1) * w[:, pair_index[pair]]
    raw = lifted @ w.T
    require(not np.any(raw % 8), "induced mediator action is not integral")
    boson = raw // 8
    require(np.array_equal(boson @ w, lifted), "W covariance reconstruction failed")
    return boson


def phase_system(
    fermion_labels: np.ndarray,
    mediator_labels: np.ndarray,
    namespace: dict[str, object],
    w: np.ndarray,
    a: np.ndarray,
    signature: np.ndarray,
) -> dict[str, object]:
    fw = np.asarray(namespace["FW"], dtype=np.int64)
    bw = np.asarray(namespace["BW"], dtype=np.int64)
    pairs = list(namespace["PAIRS"])
    pair_index = dict(namespace["PAIR_INDEX"])
    fw_lookup = {tuple(weight): i for i, weight in enumerate(fw)}
    bw_lookup = {tuple(weight): i for i, weight in enumerate(bw)}

    coefficient = np.zeros_like(w)
    mediator_lookup = {tuple(label): index for index, label in enumerate(mediator_labels)}
    for column, (i, j) in enumerate(pairs):
        target = mediator_lookup.get(tuple(fermion_labels[i] + fermion_labels[j]))
        if target is not None:
            coefficient[target, column] = epsilon(fermion_labels[i], fermion_labels[j])
    require(np.array_equal(coefficient != 0, w != 0), "affine/source tensor support differs from W")

    equations: list[tuple[int, int]] = []
    for mediator, column in zip(*np.nonzero(w)):
        i, j = pairs[int(column)]
        mask = (1 << i) ^ (1 << j) ^ (1 << (64 + int(mediator)))
        equations.append((mask, int(coefficient[mediator, column] != w[mediator, column])))

    root_rows: list[dict[str, object]] = []
    for root_number, (root2, native_op) in enumerate(native_root_operators(namespace)):
        root = f2_image(root2, a)
        require(int(root @ (signature * root)) == 2, "source root has norm other than two")
        source_fermion = np.zeros((64, 64), dtype=np.int64)
        for i, weight in enumerate(fw):
            j = fw_lookup.get(tuple(weight + root2))
            if j is not None:
                require(int(root @ (signature * fermion_labels[i])) == -1, "root action is not a simple-pole/root bracket")
                source_fermion[j, i] = epsilon(root, fermion_labels[i])
        require(np.array_equal(source_fermion != 0, native_op != 0), "fermion root-action support mismatch")
        for j, i in zip(*np.nonzero(native_op)):
            mask = (1 << int(i)) ^ (1 << int(j)) ^ (1 << (124 + root_number))
            equations.append((mask, int(source_fermion[j, i] != native_op[j, i])))

        native_boson = induced_boson_action(w, native_op, pairs, pair_index)
        source_boson = np.zeros((60, 60), dtype=np.int64)
        for i, weight in enumerate(bw):
            j = bw_lookup.get(tuple(weight + root2))
            if j is not None:
                require(int(root @ (signature * mediator_labels[i])) == -1, "mediator root action is not a simple-pole/root bracket")
                source_boson[j, i] = epsilon(root, mediator_labels[i])
        require(np.array_equal(source_boson != 0, native_boson != 0), "mediator root-action support mismatch")
        for j, i in zip(*np.nonzero(native_boson)):
            mask = (1 << (64 + int(i))) ^ (1 << (64 + int(j))) ^ (1 << (124 + root_number))
            equations.append((mask, int(source_boson[j, i] != native_boson[j, i])))
        root_rows.append({
            "root2": root2.tolist(),
            "root": root,
            "fermion_source": source_fermion,
            "boson_source": source_boson,
        })

    solution, rank = solve_binary(equations)
    require((len(equations), rank) == (2032, 167), "full tensor/action sign-system count or rank changed")
    signs = np.array([-1 if (solution >> i) & 1 else 1 for i in range(176)], dtype=np.int64)
    transformed = coefficient.copy()
    for column, (i, j) in enumerate(pairs):
        transformed[:, column] *= signs[i] * signs[j] * signs[64:124]
    require(np.array_equal(transformed, w), "signed tensor does not transform to native W")
    return {
        "coefficient": coefficient,
        "equations": equations,
        "phase_bits": solution,
        "phase_signs": signs,
        "rank": rank,
        "root_rows": root_rows,
    }


def raw_affine_audit(namespace: dict[str, object], w: np.ndarray) -> dict[str, object]:
    fw = np.asarray(namespace["FW"], dtype=np.int64)
    bw = np.asarray(namespace["BW"], dtype=np.int64)
    pairs = list(namespace["PAIRS"])
    a, signature, _, er = lattice_data()
    raw_fermions = np.array([f2_image(weight, a) for weight in fw])
    raw_mediators = np.array([f2_image(weight, a) for weight in bw])
    dressed_fermions = raw_fermions + er
    dressed_mediators = raw_mediators + 2 * er

    require(np.all(np.einsum("ai,i,ai->a", raw_fermions, signature, raw_fermions) == 2), "raw affine fermion labels are not E8 roots")
    require(np.all(np.einsum("ai,i,ai->a", raw_mediators, signature, raw_mediators) == 2), "raw affine mediator labels are not E8 roots")
    require(np.all(raw_fermions[:, 8] == 0) and np.all(raw_mediators[:, 8] == 0), "raw F(E8) labels have an e_R coordinate")

    raw = phase_system(raw_fermions, raw_mediators, namespace, w, a, signature)
    dressed = phase_system(dressed_fermions, dressed_mediators, namespace, w, a, signature)

    require(epsilon(er, er) == 1, "epsilon(e_R,e_R) != 1")
    sigma = np.array([epsilon(label, er) for label in raw_fermions], dtype=np.int64)
    pair_sigma = np.array([sigma[i] * sigma[j] for i, j in pairs], dtype=np.int64)
    require(
        np.array_equal(dressed["coefficient"], raw["coefficient"] * pair_sigma[np.newaxis, :]),
        "dressed/raw tensor ratio is not the fermion coboundary sigma_i sigma_j",
    )

    root_sigma: list[int] = []
    for raw_row, dressed_row in zip(raw["root_rows"], dressed["root_rows"]):
        root = raw_row["root"]
        sigma_root = epsilon(root, er)
        root_sigma.append(sigma_root)
        require(
            np.array_equal(dressed_row["fermion_source"], sigma_root * raw_row["fermion_source"]),
            "dressed/raw fermion current-action ratio is not sigma_root",
        )
        require(
            np.array_equal(dressed_row["boson_source"], raw_row["boson_source"]),
            "2 e_R dressing changed the mediator current action",
        )
        for i, j in zip(*np.nonzero(raw_row["fermion_source"])):
            require(sigma[j] == sigma_root * sigma[i], "sigma is not additive along a root action")

    # Construct a raw affine solution from the dressed solution by the single
    # fermion character sigma_i.  Mediator and root-current phases stay fixed.
    pulled_signs = dressed["phase_signs"].copy()
    pulled_signs[:64] *= sigma
    pulled_mask = sum((1 << i) for i, value in enumerate(pulled_signs) if value == -1)
    require(
        all(((mask & pulled_mask).bit_count() & 1) == rhs for mask, rhs in raw["equations"]),
        "dressed phase choice does not pull back to a raw affine phase choice",
    )

    return {
        "raw_affine_labels": {"fermions": 64, "mediators": 60, "norm": 2, "e_R_coordinate": 0},
        "signed_tensor": {
            "shape": list(w.shape),
            "nonzero_entries": int(np.count_nonzero(w)),
            "zero_entries": int(w.size - np.count_nonzero(w)),
            "support_exact": True,
            "all_nonzero_signs_exact_after_one_coherent_rephasing": True,
        },
        "group_action": {
            "D5_noncartan_roots": 40,
            "D3_noncartan_roots": 12,
            "cartan_weights": "the unchanged FW/BW labels",
            "tensor_and_both_representations_use_one_phase_system": True,
        },
        "raw_phase_system": {"equations": len(raw["equations"]), "variables": 176, "rank": raw["rank"]},
        "dressed_phase_system_replayed": {"equations": len(dressed["equations"]), "variables": 176, "rank": dressed["rank"]},
        "cochain_pullback": {
            "sigma_definition": "sigma_i=epsilon(F(r_i),e_R)",
            "fermion_sigma_census": {str(value): int(np.count_nonzero(sigma == value)) for value in sorted(set(sigma))},
            "root_sigma_census": {str(value): int(root_sigma.count(value)) for value in sorted(set(root_sigma))},
            "tensor_ratio": "epsilon(F_i+e_R,F_j+e_R)/epsilon(F_i,F_j)=sigma_i sigma_j",
            "fermion_action_ratio": "epsilon(F_alpha,F_i+e_R)/epsilon(F_alpha,F_i)=sigma_alpha",
            "mediator_action_ratio": "epsilon(F_alpha,F_A+2e_R)/epsilon(F_alpha,F_A)=1",
            "additivity": "sigma_j/sigma_i=sigma_alpha whenever F_j=F_i+F_alpha",
            "pulled_dressed_solution_satisfies_all_raw_equations": True,
        },
    }


def build_certificate() -> dict[str, object]:
    pin_sources()
    namespace, w = load_native()
    pairs = list(namespace["PAIRS"])
    pauli = pauli_audit(w, pairs)
    raw_affine = raw_affine_audit(namespace, w)
    return {
        "verdict": "PASS_EXACT_FINITE_NATIVE_PAULI_AND_RAW_AFFINE_SIGN_AUDIT",
        "scope": "archived signed native W; exact finite CAR coefficient identity; raw affine E8 root-bracket signs and D5+D3 covariance",
        "native_tensor_sha256": PINS[str(TENSOR_ARCHIVE.relative_to(REPO))],
        "native_archive_equals_clifford_reconstruction": True,
        "pauli_commutator": pauli,
        "raw_affine_signed_W": raw_affine,
        "closes_exactly": [
            "the pasted Pauli commutator formula and Q_B^dagger Q_A order on the native signed W",
            "the sum rule sum_A Q_A^dagger Q_A=15 I64",
            "the previously open relative phase comparison between the raw affine E8 bracket and the full native W, including the complete D5+D3 root action",
        ],
        "does_not_close": [
            "canonical CAR/CCR field identification of affine currents",
            "a source derivation of the RR Hamiltonian or its time",
            "P1/P2 origin, 3+1D locality, chirality, interactions, gravity, or initial-state selection",
        ],
        "source_pins": PINS,
        "uses_assert": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("native_pauli_audit.json"))
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "native_W": certificate["native_archive_equals_clifford_reconstruction"],
        "raw_affine_signed_W": certificate["raw_affine_signed_W"]["signed_tensor"]["all_nonzero_signs_exact_after_one_coherent_rephasing"],
        "sum_rule": certificate["pauli_commutator"]["sum_rule"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
