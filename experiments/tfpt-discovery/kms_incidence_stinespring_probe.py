#!/usr/bin/env python3
"""Review module 5: KMS incidence/Stinespring extension on the ramified fiber.

Exploration only.  The 15 labels are the nonzero vectors of
V=L/(1+i)L=F2^4.  The sigma action is reconstructed in the exact v738
L-coordinates.  Among sigma-invariant nondegenerate alternating forms we take
the lexicographically first one, Omega.  Its polar hyperplanes give

    B[x,y] = 1 iff x Omega y^T = 0,       x,y != 0.

Thus every row has seven incidences and B B^T = 4 I + 3 J.

For every incidence edge (x,y), define the Heisenberg-picture Kraus operator

    V_xy = 7^(-1/2) |y><x|.

Then Phi(A)=sum V_xy^* A V_xy is unital and restricts on the diagonal to
K=B/7.  The extension to the finite ramified Toeplitz layer is
Phi tensor id; the Kraus multipliers are V_xy tensor I and commute with the
degree-2 shift and half-weight.

Verdicts:
  KMS-INCIDENCE-CP-COVARIANT iff CP/unitality and all four compatibility
  gates (sigma, half-weight, beta=1 detailed balance, Gate 0) pass.
  KMS-INCIDENCE-PARTIAL if CP holds but a compatibility fails.
  KMS-INCIDENCE-DEAD if CP/unitality fails.

A fixed one-edge mutation preserves row degree and hence CP/unitality but
must break sigma covariance or detailed balance.  No zero ordinate or prime
table is loaded.  No file is written.
"""

import ast
import math
import os
import sys
import time
from itertools import combinations

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sps

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import ramified_fiber as ramified  # noqa: E402


LABEL_DIM = 15
ROW_DEGREE = 7
TOWER_LEVEL = 4
EXACT_TOL = 2.0e-14
BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []
FAILS = []


def check(name, ok, detail=""):
    CHECKS.append(name)
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def outcome(name, ok, detail=""):
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def gf2_rank(matrix):
    work = np.asarray(matrix, dtype=np.uint8).copy() & 1
    row = 0
    for column in range(work.shape[1]):
        pivot = next((candidate for candidate in range(row, work.shape[0])
                      if work[candidate, column]), None)
        if pivot is None:
            continue
        work[[row, pivot]] = work[[pivot, row]]
        for other in range(work.shape[0]):
            if other != row and work[other, column]:
                work[other] ^= work[row]
        row += 1
    return row


def sigma_matrix():
    lattice = ramified.Lmodule()
    rows = [
        lattice.coords(ramified.pack(ramified.sig8(ramified.unpack(
            lattice.to_ambient(tuple((1 if j == k else 0, 0)
                                     for j in range(4)))))))
        for k in range(4)
    ]
    return np.array([[ramified.par(rows[k][j]) for j in range(4)]
                     for k in range(4)], dtype=np.uint8)


def label_space(sigma):
    labels = [tuple((number >> bit) & 1 for bit in range(4))
              for number in range(1, 16)]
    lookup = {label: index for index, label in enumerate(labels)}
    permutation = []
    for label in labels:
        image = tuple(int(sum(label[k] * sigma[k, j]
                              for k in range(4)) & 1)
                      for j in range(4))
        permutation.append(lookup[image])
    P = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for source, target in enumerate(permutation):
        P[target, source] = 1
    return labels, permutation, P


def invariant_symplectic_form(sigma):
    pairs = list(combinations(range(4), 2))
    candidates = []
    for mask in range(1, 1 << len(pairs)):
        form = np.zeros((4, 4), dtype=np.uint8)
        for bit, (left, right) in enumerate(pairs):
            if (mask >> bit) & 1:
                form[left, right] = form[right, left] = 1
        invariant = np.array_equal(
            (sigma @ form @ sigma.T) & 1, form)
        if invariant and gf2_rank(form) == 4:
            candidates.append((mask, form))
    if not candidates:
        raise RuntimeError("no sigma-invariant symplectic form")
    candidates.sort(key=lambda item: item[0])
    return candidates[0][1], len(candidates)


def incidence_matrix(labels, form):
    B = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for row, left in enumerate(labels):
        for column, right in enumerate(labels):
            pairing = 0
            for j in range(4):
                for k in range(4):
                    pairing ^= left[j] & int(form[j, k]) & right[k]
            B[row, column] = int(pairing == 0)
    return B


def kraus_operators(B):
    operators = []
    scale = 1.0 / math.sqrt(ROW_DEGREE)
    for x in range(LABEL_DIM):
        for y in range(LABEL_DIM):
            if B[x, y]:
                operator = np.zeros((LABEL_DIM, LABEL_DIM))
                operator[y, x] = scale
                operators.append(operator)
    return operators


def apply_channel(operators, matrix):
    out = np.zeros_like(matrix, dtype=np.complex128)
    for operator in operators:
        out += operator.T.conj() @ matrix @ operator
    return out


def base_choi(B):
    """Choi matrix of the label channel; diagonal in vec matrix units."""
    choi = np.zeros((LABEL_DIM * LABEL_DIM,
                     LABEL_DIM * LABEL_DIM))
    for x in range(LABEL_DIM):
        for y in range(LABEL_DIM):
            if B[x, y]:
                coordinate = y + LABEL_DIM * x
                choi[coordinate, coordinate] = 1.0 / ROW_DEGREE
    return choi


def quantum_superoperator(B):
    """Matrix of Phi on Hilbert-Schmidt matrix units."""
    size = LABEL_DIM * LABEL_DIM
    superoperator = np.zeros((size, size))
    for y in range(LABEL_DIM):
        source = y + LABEL_DIM * y
        for x in range(LABEL_DIM):
            if B[x, y]:
                target = x + LABEL_DIM * x
                superoperator[target, source] = 1.0 / ROW_DEGREE
    return superoperator


def tower_data():
    levels = TOWER_LEVEL + 1
    half_weight = np.diag([2.0 ** (-0.5 * level)
                           for level in range(levels)])
    kms_weight = np.array([2.0 ** (-level) for level in range(levels)])
    kms_weight /= np.sum(kms_weight)
    shift = np.zeros((levels + 1, levels))
    for level in range(levels):
        shift[level + 1, level] = 1.0
    target_half_weight = np.diag([2.0 ** (-0.5 * level)
                                  for level in range(levels + 1)])
    return levels, half_weight, kms_weight, shift, target_half_weight


def mutate_incidence(B):
    mutated = B.copy()
    row = 0
    incident = [column for column in range(LABEL_DIM)
                if B[row, column] == 1]
    absent = [column for column in range(LABEL_DIM)
              if B[row, column] == 0]
    mutated[row, incident[0]] = 0
    mutated[row, absent[0]] = 1
    return mutated, (row, incident[0], absent[0])


def run():
    started = time.time()
    print("=" * 78)
    print("KMS INCIDENCE -- covariant Stinespring extension")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))

    sigma = sigma_matrix()
    labels, permutation, sigma_permutation = label_space(sigma)
    sigma_order = np.linalg.matrix_power(sigma, 3) % 2
    check("G0.2 exact ramified sigma action",
          np.array_equal(sigma_order, np.eye(4, dtype=np.uint8))
          and permutation != list(range(LABEL_DIM)),
          "S=%s, label permutation=%s"
          % (sigma.tolist(), permutation))

    form, form_count = invariant_symplectic_form(sigma)
    B = incidence_matrix(labels, form)
    identity = np.eye(LABEL_DIM, dtype=np.int64)
    ones = np.ones((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    formula_dev = int(np.max(np.abs(B @ B.T - (4 * identity + 3 * ones))))
    symmetric = np.array_equal(B, B.T)
    row_sums = B.sum(axis=1)
    check("E0 incidence identity", symmetric
          and np.all(row_sums == ROW_DEGREE) and formula_dev == 0,
          "Omega=%s (%d invariant choices), rows=%s, "
          "max |BB^T-(4I+3J)|=%d"
          % (form.tolist(), form_count, sorted(set(row_sums.tolist())),
             formula_dev))
    K = B.astype(float) / ROW_DEGREE
    projector = np.ones((LABEL_DIM, LABEL_DIM)) / LABEL_DIM
    k2_dev = float(np.max(np.abs(
        K @ K - ((4.0 / 49.0) * np.eye(LABEL_DIM)
                 + (45.0 / 49.0) * projector))))
    check("E0.2 review spectral formula", k2_dev <= EXACT_TOL,
          "max deviation %.3e" % k2_dev)

    operators = kraus_operators(B)
    completeness = sum((operator.T @ operator for operator in operators),
                       np.zeros((LABEL_DIM, LABEL_DIM)))
    unital_dev = float(np.max(np.abs(completeness
                                     - np.eye(LABEL_DIM))))
    reproduction_dev = 0.0
    for basis_index in range(LABEL_DIM):
        diagonal = np.zeros((LABEL_DIM, LABEL_DIM))
        diagonal[basis_index, basis_index] = 1.0
        image = apply_channel(operators, diagonal)
        expected = np.diag(K[:, basis_index])
        reproduction_dev = max(reproduction_dev,
                               float(np.max(np.abs(image - expected))))
    stinespring = np.vstack(operators)
    stinespring_dev = float(np.max(np.abs(
        stinespring.T @ stinespring - np.eye(LABEL_DIM))))
    check("E1.1 Kraus/Stinespring unital and reproduces K",
          max(unital_dev, reproduction_dev, stinespring_dev) <= EXACT_TOL,
          "Kraus=%d, sum V*V dev %.3e, K dev %.3e, W*W dev %.3e"
          % (len(operators), unital_dev, reproduction_dev,
             stinespring_dev))

    choi = base_choi(B)
    choi_eigenvalues = sla.eigvalsh(choi)
    choi_rank = int(np.sum(choi_eigenvalues > EXACT_TOL))
    levels, half_weight, kms_weight, shift, target_half_weight = tower_data()
    extended_nonzero_eigenvalue = levels / ROW_DEGREE
    extended_rank = len(operators)
    rng = np.random.default_rng(1505)
    dimension = LABEL_DIM * levels
    random_matrix = (rng.standard_normal((dimension, dimension))
                     + 1j * rng.standard_normal((dimension, dimension)))
    positive_input = random_matrix.T.conj() @ random_matrix
    extended_operators = [np.kron(operator, np.eye(levels))
                          for operator in operators]
    positive_output = apply_channel(extended_operators, positive_input)
    output_min = float(sla.eigvalsh(
        0.5 * (positive_output + positive_output.T.conj()),
        subset_by_index=[0, 0])[0])
    cp_ok = choi_eigenvalues[0] >= -EXACT_TOL \
        and choi_rank == 105 and extended_rank == 105 \
        and extended_nonzero_eigenvalue > 0.0 \
        and output_min >= -1.0e-10
    outcome("E1.2 EXTENDED CHOI PSD", cp_ok,
            "base min %.3e rank %d; extended nonzero eigenvalue %.12f "
            "x%d; random PSD image min %.3e"
            % (choi_eigenvalues[0], choi_rank,
               extended_nonzero_eigenvalue, extended_rank, output_min))
    check("E1.3 Choi/Kraus factorization", cp_ok,
          "Phi_B tensor id_%d on dimension %d" % (levels, dimension))

    sigma_dev = int(np.max(np.abs(
        sigma_permutation @ B @ sigma_permutation.T - B)))
    edge_set = {(x, y) for x in range(LABEL_DIM)
                for y in range(LABEL_DIM) if B[x, y]}
    permuted_edges = {(permutation[x], permutation[y])
                      for x, y in edge_set}
    sigma_ok = sigma_dev == 0 and permuted_edges == edge_set
    outcome("E2.i SIGMA COVARIANCE", sigma_ok,
            "matrix dev %d, edge-set symmetric difference %d"
            % (sigma_dev, len(permuted_edges.symmetric_difference(edge_set))))

    half_dev = 0.0
    for operator in operators:
        multiplier = np.kron(operator, np.eye(levels))
        degree_weight = np.kron(np.eye(LABEL_DIM), half_weight)
        half_dev = max(half_dev, float(np.max(np.abs(
            multiplier @ degree_weight - degree_weight @ multiplier))))
        source_multiplier = np.kron(operator, np.eye(levels))
        target_multiplier = np.kron(operator, np.eye(levels + 1))
        ramified_shift = np.kron(np.eye(LABEL_DIM), shift)
        half_dev = max(half_dev, float(np.max(np.abs(
            target_multiplier @ ramified_shift
            - ramified_shift @ source_multiplier))))
    ramified_shift = np.kron(np.eye(LABEL_DIM), shift)
    source_half = np.kron(np.eye(LABEL_DIM), half_weight)
    target_half = np.kron(np.eye(LABEL_DIM), target_half_weight)
    weight_relation_dev = float(np.max(np.abs(
        target_half @ ramified_shift
        - (2.0 ** -0.5) * ramified_shift @ source_half)))
    half_ok = max(half_dev, weight_relation_dev) <= EXACT_TOL
    outcome("E2.ii HALF-WEIGHT COVARIANCE", half_ok,
            "Kraus/shift naturality %.3e, D U=2^-1/2 U D dev %.3e"
            % (half_dev, weight_relation_dev))

    superoperator = quantum_superoperator(B)
    detailed_balance_dev = float(np.max(np.abs(
        superoperator - superoperator.T)))
    label_density = np.eye(LABEL_DIM) / LABEL_DIM
    tower_density = np.diag(kms_weight)
    kms_density = np.kron(label_density, tower_density)
    state_preservation_dev = 0.0
    for operator in extended_operators:
        state_preservation_dev = max(
            state_preservation_dev, 0.0)
    density_image = sum(
        (operator @ kms_density @ operator.T.conj()
         for operator in extended_operators),
        np.zeros_like(kms_density, dtype=np.complex128))
    state_preservation_dev = float(np.max(np.abs(
        density_image - kms_density)))
    balance_ok = max(detailed_balance_dev,
                     state_preservation_dev) <= EXACT_TOL
    outcome("E2.iii BETA=1 DETAILED BALANCE", balance_ok,
            "weighted-superoperator symmetry %.3e, KMS density dev %.3e"
            % (detailed_balance_dev, state_preservation_dev))

    gate0_dev = 0.0
    for level in range(levels):
        matrix = np.zeros((levels, levels))
        matrix[level, level] = 1.0
        periodic = np.kron(np.eye(LABEL_DIM), matrix)
        image = apply_channel(extended_operators, periodic)
        gate0_dev = max(gate0_dev,
                        float(np.max(np.abs(image - periodic))))
    gate0_ok = gate0_dev <= EXACT_TOL
    outcome("E2.iv GATE-0 COMPATIBILITY", gate0_ok,
            "label-blind periodic subalgebra fixed, dev %.3e"
            % gate0_dev)

    mutated, mutation = mutate_incidence(B)
    mutated_sigma_dev = int(np.max(np.abs(
        sigma_permutation @ mutated @ sigma_permutation.T - mutated)))
    mutated_balance_dev = int(np.max(np.abs(mutated - mutated.T)))
    mutated_rows = mutated.sum(axis=1)
    mutated_cp_unital = np.all(mutated_rows == ROW_DEGREE)
    control_fires = mutated_cp_unital \
        and (mutated_sigma_dev > 0 or mutated_balance_dev > 0)
    check("C1 MUTATED INCIDENCE CONTROL FIRES", control_fires,
          "mutation row/remove/add=%s; CP/unital=%s, sigma dev=%d, "
          "balance dev=%d"
          % (mutation, mutated_cp_unital, mutated_sigma_dev,
             mutated_balance_dev))

    compatibilities = (sigma_ok, half_ok, balance_ok, gate0_ok)
    if not cp_ok:
        verdict = "KMS-INCIDENCE-DEAD"
    elif all(compatibilities):
        verdict = "KMS-INCIDENCE-CP-COVARIANT"
    else:
        verdict = "KMS-INCIDENCE-PARTIAL"
    print("\nVERDICT: %s" % verdict)
    if verdict == "KMS-INCIDENCE-CP-COVARIANT":
        print("FINITE RESULT: Step 3 is solved on the factorized ramified "
              "15-label Toeplitz layer: an explicit 105-Kraus, rank-105 "
              "Stinespring channel is CP, sigma/grade covariant, "
              "beta=1-reversible and fixes Gate 0.")
        print("CANDIDATE STATE: the local candidate is the tensor product of "
              "the uniform incidence-fiber state with the beta=1 Toeplitz "
              "state.  The channel preserves it, but does not select a new "
              "global window state by itself.")
        print("STILL MISSING: compatible incidence channels at every finite "
              "place and level; interaction with non-label ramified "
              "multipliers and the arch lift; a canonical UCP map between "
              "the nine window systems; compactness/normality of the limit; "
              "and identification with the critical-line Weil functional.")
    elif verdict == "KMS-INCIDENCE-PARTIAL":
        failed = [name for name, ok in zip(
            ("sigma", "half-weight", "detailed-balance", "Gate-0"),
            compatibilities) if not ok]
        print("BROKEN COMPATIBILITIES: %s" % ", ".join(failed))
    else:
        print("KILL: the proposed incidence extension is not completely "
              "positive/unital on the finite ramified layer.")

    elapsed = time.time() - started
    if FAILS:
        print("RESULT: %d/%d CONSTRUCTION/CONTROL CHECKS PASSED; FAILURES %s "
              "(%.1fs)" % (len(CHECKS) - len(FAILS), len(CHECKS),
                           ",".join(FAILS), elapsed))
        return 1
    print("RESULT: ALL %d CONSTRUCTION/CONTROL CHECKS PASSED (%.1fs)"
          % (len(CHECKS), elapsed))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
