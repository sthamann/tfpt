"""Finite checks added by the 28 September 2026 TFPT consolidation.

The three stages in this module close concrete links that were intentionally
absent from :mod:`tfpt_explorer.process`: the full logical observable closure,
normalisation of the coherent 60-event lift, and a charge-covariant recursion
that actually fits the marked periodic A3 graph.  The last construction still
depends on a declared marking and on a changed pair Hamiltonian; those choices
are exposed instead of being promoted to primitive TFPT laws.
"""

from __future__ import annotations

from functools import lru_cache
import itertools as it
import math
from collections import deque
from typing import Any

import numpy as np

from .process import _check, _hist, _invariants, _stage


PDF = "tfpt_explorer/sources/TFPT_Konsolidierung_20260928.pdf"
DOC_CODE = "_newest2/TFPT_Gesamtdokumentation_Code_Quartik_Rekursion_2026-09-26.md"
DOC_RESULTS = "_newest2/TFPT_Gesamtdokumentation_Ergebnisse_und_Herleitungen_2026-09-27.md"
DOC_FULL = "_newest2/TFPT_Universalraum_Gesamtdokumentation_2026-09-27.md"


def _pdf_source(page: int, claim: str) -> dict[str, Any]:
    return {"path": PDF, "page": page, "claim": claim}


def _source(path: str, line: int, claim: str) -> dict[str, Any]:
    return {"path": path, "line": line, "claim": claim}


def _kron4(matrices: list[np.ndarray]) -> np.ndarray:
    result = matrices[0]
    for matrix in matrices[1:]:
        result = np.kron(result, matrix)
    return result


def _orthonormal_span(matrices: list[np.ndarray], tol: float = 1e-10) -> list[np.ndarray]:
    """Return a stable Hilbert--Schmidt basis of the supplied matrices."""

    vectors = np.empty((25, 0), dtype=complex)
    basis: list[np.ndarray] = []
    for matrix in matrices:
        vector = matrix.reshape(-1).astype(complex)
        if vectors.shape[1]:
            vector -= vectors @ (vectors.conj().T @ vector)
        norm = np.linalg.norm(vector)
        if norm > tol:
            vectors = np.column_stack((vectors, vector / norm))
            basis.append(matrix)
    return basis


def _permutation_operator(permutation: tuple[int, ...]) -> np.ndarray:
    operator = np.zeros((256, 256), dtype=float)
    for word in it.product(range(4), repeat=4):
        source = np.ravel_multi_index(word, (4, 4, 4, 4))
        target_word = tuple(word[index] for index in permutation)
        target = np.ravel_multi_index(target_word, (4, 4, 4, 4))
        operator[target, source] = 1
    return operator


def _antisymmetric_state() -> np.ndarray:
    state = np.zeros(256, dtype=complex)
    for permutation in it.permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        state[np.ravel_multi_index(permutation, (4, 4, 4, 4))] = (
            (-1) ** inversions / math.sqrt(24)
        )
    return state


def _event_matrix(pairs: list[tuple[int, int]]) -> np.ndarray:
    matrix = np.zeros((15, 15), dtype=float)
    for row, pair in enumerate(pairs):
        for column, other in enumerate(pairs):
            if row == column:
                numerator = 32
            elif set(pair) & set(other):
                numerator = 5
            else:
                numerator = -4
            matrix[row, column] = numerator / 648
    return matrix


def _covariant_chain() -> dict[str, Any]:
    dimension = 5
    identity = np.eye(dimension)
    omega = identity.reshape(-1) / math.sqrt(dimension)
    singlet = np.outer(omega, omega)
    h_cov = (5 / 6) * (np.eye(dimension**2) - singlet)

    # Sites alternate U, conjugate(U), U.  The tensor below is the explicit
    # U -> U tensor Ubar tensor U intertwiner from equation (13.1).
    w = np.zeros((dimension**3, dimension), dtype=float)
    for a, b, c, x in it.product(range(dimension), repeat=4):
        row = np.ravel_multi_index((a, b, c), (dimension,) * 3)
        w[row, x] = ((a == b and c == x) + (a == x and b == c)) / math.sqrt(12)

    chain = np.kron(h_cov, identity) + np.kron(identity, h_cov)
    covariance_error = 0.0
    for row, column in it.product(range(dimension), repeat=2):
        matrix_unit = np.zeros((dimension, dimension))
        matrix_unit[row, column] = 1
        generator = (
            np.kron(np.kron(matrix_unit, identity), identity)
            - np.kron(np.kron(identity, matrix_unit.T), identity)
            + np.kron(np.kron(identity, identity), matrix_unit)
        )
        covariance_error = max(
            covariance_error,
            float(np.linalg.norm(generator @ w - w @ matrix_unit)),
        )

    return {
        "omega": omega,
        "h_cov": h_cov,
        "w": w,
        "chain": chain,
        "covariance_error": covariance_error,
    }


TRIMERS: tuple[tuple[int, int, int, tuple[int, int, int], tuple[int, int, int], str], ...] = (
    (0, 15, 24, (0, 0, 0), (0, 0, 0), "Ubar"),
    (1, 25, 28, (0, 0, 0), (0, 0, 0), "Ubar"),
    (2, 26, 27, (0, 0, 0), (0, 0, 0), "Ubar"),
    (4, 16, 22, (1, -2, -1), (2, -1, -2), "Ubar"),
    (23, 5, 8, (0, 1, -2), (1, -1, -2), "U"),
    (17, 6, 7, (0, 0, 0), (1, -2, 1), "U"),
    (3, 21, 29, (0, 0, 0), (0, 0, 0), "Ubar"),
    (18, 10, 11, (0, -1, 2), (0, 0, 0), "U"),
    (20, 9, 12, (-2, 2, 1), (-1, 2, -1), "U"),
    (19, 13, 14, (2, -1, -2), (0, 0, 0), "U"),
)


# Appendix D, in the same lexicographic edge order as ``geometry_edges``:
# matching 0 with its three pairs, then matching 1, and so on.  These are
# harmonic Cartesian edge vectors, not the period coordinates in TRIMERS.
HARMONIC_EDGES = np.asarray(
    [
        (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 2, 2), (0, -2, -2),
        (0, 0, 0), (0, 2, -2), (0, -2, 2),
        (2, 2, 0), (-2, -2, 0), (0, 0, 0),
        (-1, -1, 0), (1, 0, -1), (0, 1, 1),
        (-1, -1, 0), (1, 0, 1), (0, 1, -1),
        (2, -2, 0), (-2, 2, 0), (0, 0, 0),
        (-1, 1, 0), (1, 0, -1), (0, -1, 1),
        (-1, 1, 0), (1, 0, 1), (0, -1, -1),
        (-1, 0, -1), (1, -1, 0), (0, 1, 1),
        (-1, 0, -1), (1, 1, 0), (0, -1, 1),
        (2, 0, 2), (-2, 0, -2), (0, 0, 0),
        (-1, 0, 1), (1, -1, 0), (0, 1, -1),
        (-1, 0, 1), (1, 1, 0), (0, -1, -1),
        (2, 0, -2), (-2, 0, 2), (0, 0, 0),
    ],
    dtype=int,
)

PERIOD_BASIS = np.asarray([[6, 3, 3], [0, 3, 0], [0, 0, 3]], dtype=int)


def _periodic_voltage_data(
    trimers: tuple[
        tuple[int, int, int, tuple[int, int, int], tuple[int, int, int], str], ...
    ] = TRIMERS,
) -> dict[str, Any]:
    """Reconstruct Appendix C shifts from Appendix D in a fixed tree gauge.

    The gauge is not fitted to the trimer table: it is fixed independently by
    breadth-first traversal from node 0, always visiting the smallest adjacent
    node first and assigning zero voltage to each tree edge.  A changed trimer
    shift therefore fails the comparison instead of being absorbed by a new
    gauge choice.
    """

    inv = _invariants()
    graph_edges = [
        (int(left[1:]), 15 + int(right[1:]))
        for left, right in inv["geometry_edges"]
    ]
    if len(graph_edges) != len(HARMONIC_EDGES):
        raise RuntimeError("harmonic edge table does not match the incidence graph")

    incidence = np.zeros((30, 45), dtype=int)
    adjacency: dict[int, list[tuple[int, np.ndarray, int]]] = {
        node: [] for node in range(30)
    }
    for edge, ((matching, pair), vector) in enumerate(zip(graph_edges, HARMONIC_EDGES)):
        incidence[matching, edge] = -1
        incidence[pair, edge] = 1
        adjacency[matching].append((pair, vector, 1))
        adjacency[pair].append((matching, vector, -1))

    # Canonical spanning-tree gauge: every tree edge has period voltage zero.
    potentials: dict[int, np.ndarray] = {0: np.zeros(3, dtype=int)}
    queue: deque[int] = deque([0])
    tree_edges: list[tuple[int, int]] = []
    while queue:
        node = queue.popleft()
        for neighbour, vector, orientation in sorted(adjacency[node], key=lambda row: row[0]):
            if neighbour in potentials:
                continue
            potentials[neighbour] = potentials[node] + orientation * vector
            tree_edges.append((node, neighbour))
            queue.append(neighbour)
    if len(potentials) != 30:
        raise RuntimeError("incidence graph is disconnected")

    voltages: dict[tuple[int, int], tuple[int, int, int]] = {}
    integrality_error = 0.0
    for (matching, pair), vector in zip(graph_edges, HARMONIC_EDGES):
        coordinates = np.linalg.solve(
            PERIOD_BASIS,
            vector - (potentials[pair] - potentials[matching]),
        )
        rounded = np.rint(coordinates).astype(int)
        integrality_error = max(integrality_error, float(np.linalg.norm(coordinates - rounded)))
        voltages[(matching, pair)] = tuple(int(value) for value in rounded)

    # The non-tree voltages generate all Z^3 iff the gcd of their nonzero
    # 3x3 minors is one.  Then the actual harmonic loop lattice is L Z^3.
    voltage_rows = np.asarray(list(voltages.values()), dtype=int)
    determinants = [
        abs(int(round(np.linalg.det(voltage_rows[list(indices)]))))
        for indices in it.combinations(range(len(voltage_rows)), 3)
    ]
    nonzero_determinants = [value for value in determinants if value]
    lattice_index = 0
    for determinant in nonzero_determinants:
        lattice_index = math.gcd(lattice_index, determinant)

    shift_comparisons = []
    orientation_comparisons = []
    for center, left, right, left_shift, right_shift, representation in trimers:
        expected_representation = "Ubar" if center < 15 else "U"
        orientation_comparisons.append(
            {
                "center": center,
                "declared": representation,
                "expected": expected_representation,
                "ok": representation == expected_representation,
            }
        )
        for leaf, declared in ((left, left_shift), (right, right_shift)):
            derived = voltages[(center, leaf)] if center < 15 else tuple(
                -value for value in voltages[(leaf, center)]
            )
            shift_comparisons.append(
                {
                    "center": center,
                    "leaf": leaf,
                    "declared": declared,
                    "derived": derived,
                    "ok": tuple(declared) == tuple(derived),
                }
            )

    return {
        "graph_edges": graph_edges,
        "incidence": incidence,
        "tree_edges": tree_edges,
        "potentials": potentials,
        "voltages": voltages,
        "integrality_error": integrality_error,
        "lattice_index": lattice_index,
        "shift_comparisons": shift_comparisons,
        "orientation_comparisons": orientation_comparisons,
    }


@lru_cache(maxsize=1)
def _consolidated_invariants() -> dict[str, Any]:
    inv = _invariants()
    code_isometry = inv["v_code"].astype(complex)
    code_projector = code_isometry @ code_isometry.conj().T

    symmetric_projector = sum(
        (_permutation_operator(permutation) for permutation in it.permutations(range(4))),
        np.zeros((256, 256), dtype=float),
    ) / math.factorial(4)

    i2 = np.eye(2, dtype=complex)
    x = np.asarray([[0, 1], [1, 0]], dtype=complex)
    y = np.asarray([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    paulis = [np.kron(a, b) for a, b in it.product((i2, x, y, z), repeat=2)]
    identity4 = np.eye(4, dtype=complex)
    stabilizer_projector = sum(
        (_kron4([pauli] * 4) for pauli in paulis),
        np.zeros((256, 256), dtype=complex),
    ) / 16
    moment = sum(
        (_kron4([projector] * 4) for projector in inv["projectors"]),
        np.zeros((256, 256), dtype=complex),
    ) / 60

    pair_observables = [
        code_isometry.conj().T
        @ _kron4([left, right, identity4, identity4])
        @ code_isometry
        for left, right in it.product(paulis, repeat=2)
    ]
    controls = []
    for pauli in paulis[1:]:
        physical = np.zeros((256, 256), dtype=complex)
        for left, right in it.combinations(range(4), 2):
            factors = [identity4] * 4
            factors[left] = pauli
            factors[right] = pauli
            physical += _kron4(factors) / 6
        controls.append(code_isometry.conj().T @ physical @ code_isometry)

    observable_basis = _orthonormal_span(pair_observables)
    closure_ranks = [len(observable_basis)]
    for _ in range(2):
        candidates = list(observable_basis)
        candidates.extend(
            1j * (control @ observable - observable @ control)
            for control in controls
            for observable in observable_basis
        )
        observable_basis = _orthonormal_span(candidates)
        closure_ranks.append(len(observable_basis))

    event_matrix = _event_matrix(inv["transposition_pairs"])
    event_values, event_vectors = np.linalg.eigh(event_matrix)
    factor = event_vectors @ np.diag(np.sqrt(np.clip(event_values, 0, None)))
    code_kraus = [
        sum(
            (factor[event, branch] * inv["transpositions"][event] for event in range(15)),
            np.zeros((5, 5)),
        )
        for branch in range(15)
    ]
    code_superoperator = sum(
        (np.kron(kraus, kraus.conj()) for kraus in code_kraus),
        np.zeros((25, 25), dtype=complex),
    )

    source_events = []
    for projector in inv["projectors"]:
        reflection = np.eye(4) - 2 * projector
        source_events.append(_kron4([reflection] * 4))
    lifted_kraus = []
    for branch in range(15):
        lifted = np.zeros((256, 256), dtype=complex)
        for ray, logical_label in enumerate(inv["labels"]):
            event = inv["logical_to_pair"][logical_label]
            lifted += factor[event, branch] * source_events[ray] / 4
        lifted_kraus.append(lifted)
    lift_norm = sum(
        (lifted.conj().T @ lifted for lifted in lifted_kraus),
        np.zeros((256, 256), dtype=complex),
    )
    lift_values, lift_vectors = np.linalg.eigh(lift_norm)
    inverse_sqrt = (
        lift_vectors * (1 / np.sqrt(lift_values))
    ) @ lift_vectors.conj().T
    normalized_kraus = [lifted @ inverse_sqrt for lifted in lifted_kraus]
    normalized_norm = sum(
        (kraus.conj().T @ kraus for kraus in normalized_kraus),
        np.zeros((256, 256), dtype=complex),
    )
    antisymmetric = _antisymmetric_state()

    chain = _covariant_chain()
    incidence_edges = {
        (int(left[1:]), 15 + int(right[1:]))
        for left, right in inv["geometry_edges"]
    }
    trimer_nodes = [node for trimer in TRIMERS for node in trimer[:3]]
    trimer_edges = [
        tuple(sorted((center, leaf)))
        for center, left, right, *_ in TRIMERS
        for leaf in (left, right)
    ]

    charge = inv["charges"][0]
    charge_generator = np.kron(charge, np.eye(5)) - np.kron(np.eye(5), charge.T)
    periodic = _periodic_voltage_data()
    mutated = list(TRIMERS)
    first = list(mutated[0])
    first[3] = (1, 0, 0)
    mutated[0] = tuple(first)  # type: ignore[assignment]
    mutated_periodic = _periodic_voltage_data(tuple(mutated))

    return {
        "symmetric_projector": symmetric_projector,
        "stabilizer_projector": stabilizer_projector,
        "code_projector": code_projector,
        "moment": moment,
        "closure_ranks": closure_ranks,
        "event_matrix": event_matrix,
        "event_matrix_spectrum": event_values,
        "code_kraus": code_kraus,
        "code_superoperator": code_superoperator,
        "lifted_kraus": lifted_kraus,
        "lift_norm": lift_norm,
        "lift_spectrum": lift_values,
        "normalized_kraus": normalized_kraus,
        "normalized_norm": normalized_norm,
        "antisymmetric": antisymmetric,
        "chain": chain,
        "incidence_edges": incidence_edges,
        "trimer_nodes": trimer_nodes,
        "trimer_edges": trimer_edges,
        "charge_commutator": np.linalg.norm(chain["h_cov"] @ charge_generator - charge_generator @ chain["h_cov"]),
        "periodic": periodic,
        "shift_mutation_rejected": not all(
            comparison["ok"] for comparison in mutated_periodic["shift_comparisons"]
        ),
    }


def build_stages(
    config: dict[str, Any] | None = None,
    prior_dict: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Build the consolidation stages after the core/process stages."""

    if config is not None and not isinstance(config, dict):
        raise ValueError("config must be a dictionary")
    if prior_dict is not None and not isinstance(prior_dict, dict):
        raise ValueError("prior_dict must be a dictionary")

    inv = _invariants()
    con = _consolidated_invariants()
    stages: list[dict[str, Any]] = []

    symmetric = con["symmetric_projector"]
    stabilizer = con["stabilizer_projector"]
    code = con["code_projector"]
    complement = symmetric - code
    projector_ranks = {
        "ambient": 256,
        "symmetric": int(round(np.trace(symmetric).real)),
        "stabilizer": int(round(np.trace(stabilizer).real)),
        "code": int(round(np.trace(code).real)),
        "symmetric_complement": int(round(np.trace(complement).real)),
    }
    event_fibres = [0] * 15
    for logical_label in inv["labels"]:
        event_fibres[inv["logical_to_pair"][logical_label]] += 1
    match_incidence = [0] * 15
    for matching in inv["matchings"]:
        for pair in matching:
            match_incidence[inv["transposition_pairs"].index(pair)] += 1

    stages.append(
        _stage(
            "observability",
            "Vom vollen Quellraum zur vollständigen Auslese",
            "256 → 35 → 5 und 10 → 20 → 25 sind verschiedene Abschlüsse",
            "consolidation",
            110,
            "conditional",
            "Der quartische Fünfer ist der Rang-5-Schnitt eines symmetrischen 35erraums mit einem Rang-16-Stabilisatorraum. Paarbeobachtungen sehen zunächst nur zehn Operatorrichtungen; zwei Kommutatorschritte mit den expliziten codeerhaltenden Paarkontrollen öffnen 20 und schließlich alle 25 Richtungen.",
            inputs=[
                {"name": "ambient_register_space", "value": 256, "origin": "four C4 registers"},
                {"name": "pair_controls", "value": 15, "origin": "symmetrised nontrivial two-qubit Paulis"},
            ],
            outputs=[
                {"name": "symmetric_rank", "value": projector_ranks["symmetric"]},
                {"name": "code_rank", "value": projector_ranks["code"]},
                {"name": "hidden_symmetric_rank", "value": projector_ranks["symmetric_complement"]},
                {"name": "readout_closure", "value": con["closure_ranks"]},
            ],
            formulas=[
                "P = S Q_P = 40 M_4 - S",
                "rank(S,Q_P,P,S-P)=(35,16,5,30)",
                "O_2 -> O_2+[h_A,O_2] -> End(C5): 10 -> 20 -> 25",
            ],
            checks=[
                _check("Projektorränge 35,16,5,30", projector_ranks == {"ambient": 256, "symmetric": 35, "stabilizer": 16, "code": 5, "symmetric_complement": 30}, projector_ranks, {"ambient": 256, "symmetric": 35, "stabilizer": 16, "code": 5, "symmetric_complement": 30}, "direkte Spuren der vier 256x256-Projektoren"),
                _check("Fünfer ist der Schnitt S Q_P", np.linalg.norm(code - symmetric @ stabilizer) < 1e-10, np.linalg.norm(code - symmetric @ stabilizer), 0, "direkte Matrixidentität, Toleranz 1e-10"),
                _check("Momentenidentität", np.linalg.norm(code - (40 * con["moment"] - symmetric)) < 1e-10, np.linalg.norm(code - (40 * con["moment"] - symmetric)), 0, "60 Projektoren vierfach tensoriert, Toleranz 1e-10"),
                _check("Beobachtbarkeitsabschluss 10→20→25", con["closure_ranks"] == [10, 20, 25], con["closure_ranks"], [10, 20, 25], "Hilbert-Schmidt-Ränge nach zwei Kommutatorrunden mit allen 15 Paarkontrollen"),
                _check("60 Ereignisse bilden 15 Viererfasern", event_fibres == [4] * 15, event_fibres, [4] * 15, "Quellenereignisse nach ihrer logischen Transposition gruppiert"),
                _check("15 Matchings sind eine andere 15er-Menge", len(inv["matchings"]) == 15 and match_incidence == [3] * 15, {"matchings": len(inv["matchings"]), "event_incidence": match_incidence}, {"matchings": 15, "each_event_in_matchings": [3] * 15}, "perfekte Matchings bestehen jeweils aus drei disjunkten Ereignispaaren"),
            ],
            sources=[
                _source(DOC_CODE, 362, "rank-35 symmetric and rank-16 stabilizer projectors intersect in the rank-five quartic code"),
                _source(DOC_CODE, 768, "15 commuting and 20 anticommuting triples span all 25 Hermitian directions"),
                _source(DOC_RESULTS, 302, "60 source events reduce to 15 transpositions, four per fibre"),
                _source(DOC_RESULTS, 461, "perfect matchings define the separate family of 15 response planes"),
                _source(DOC_FULL, 5195, "source-reported weak-coupling dynamics selects 35 then splits 5+30"),
                _pdf_source(17, "pair readout ranks 1,10,25 and controlled closure 10→20→25"),
            ],
            depends_on=[
                {"id": "code", "relation": "derives", "label": "Rang-5-Projektor im vollständigen 35er Zwischenraum"},
                {"id": "observables", "relation": "feeds", "label": "15 Antwortflächen werden zum vollen Operatorabschluss erweitert"},
            ],
            visual_type="flow",
            visual_data={
                "source_path": [
                    {"id": "ambient", "label": "4 Register", "dimension": 256},
                    {"id": "symmetric", "label": "symmetrisches Band", "dimension": 35},
                    {"id": "code", "label": "geschützter Fünfer", "dimension": 5},
                ],
                "readout_path": [
                    {"step": 0, "dimension": 10, "label": "Paarbeobachtung"},
                    {"step": 1, "dimension": 20, "label": "nach einer Kontrolle"},
                    {"step": 2, "dimension": 25, "label": "voller Operatorraum"},
                ],
                "branches": {"symmetric": 35, "stabilizer": 16, "intersection": 5},
            },
            notes=[
                "Die 15 logischen Ereignisse sind einfache Transpositionen. Die 15 Matchings sind Dreiermengen disjunkter Ereignisse und erzeugen die Antwortflächen; gleiche Anzahl bedeutet nicht gleiches Objekt.",
                "Die lokale Rechnung prüft die Projektoren und den Operatorabschluss. Die perturbative dynamische Auswahl 35→5 aus vier geschützten Siebenregisterquellen ist hier als Quellenbefund geführt, nicht als neu ausgeführte 28-Register-Störungsrechnung.",
            ],
            assumptions=[
                "Der dynamische 35→5-Parent setzt vier geschützte Quellenblöcke, negative schwache Austauschkopplung und den im Original angegebenen Linkgraphen voraus.",
                "Der Abschluss 10→20→25 setzt aktiven Zugriff auf die 15 symmetrisierten Paarkontrollen voraus.",
            ],
            data={
                "projector_ranks": projector_ranks,
                "source_path": [256, 35, 5],
                "readout_ranks": [1, 10, 25],
                "closure_ranks": con["closure_ranks"],
                "event_fibres": event_fibres,
                "event_vs_matching": {"events": 15, "event_fibre_size": 4, "matchings": 15, "pairs_per_matching": 3, "matchings_per_event": 3},
                "dynamic_scope": "projector geometry recomputed; weak-coupling third/sixth-order selection retained as a source finding",
            },
        )
    )

    anti = con["antisymmetric"]
    lift_norm = con["lift_norm"]
    antisymmetric_weight = float(np.vdot(anti, lift_norm @ anti).real)
    normalization_residual = float(np.linalg.norm(con["normalized_norm"] - np.eye(256)))
    code_branch_residual = max(
        float(np.linalg.norm(normalized @ inv["v_code"] - lifted @ inv["v_code"]))
        for normalized, lifted in zip(con["normalized_kraus"], con["lifted_kraus"])
    )
    code_tp_residual = float(
        np.linalg.norm(
            sum(
                (kraus.conj().T @ kraus for kraus in con["code_kraus"]),
                np.zeros((5, 5), dtype=complex),
            )
            - np.eye(5)
        )
    )
    code_spectrum = np.linalg.eigvals(con["code_superoperator"])

    stages.append(
        _stage(
            "normalization",
            "Der volle Lift scheitert – und wird konstruktiv repariert",
            "Der Code sieht Norm 1, der antisymmetrische Sektor 10/9; q⁻¹ᐟ² erhält den Codezweig",
            "consolidation",
            120,
            "exact",
            "Die kohärente 15-Ereignis-Matrix erzeugt einen korrekten Fünferkanal. Derselbe Amplitudenlift aus den 60 vierfachen Reflexionen ist auf dem vollen 256erraum nicht spurtreu: Λ⁴C⁴ erhält Gewicht 10/9. Die funktionale Normierung innerhalb der erzeugten endlichen Operatoralgebra macht den Lift spurtreu und lässt jeden Krauszweig auf dem Code unverändert.",
            inputs=[
                {"name": "coherent_event_labels", "value": 15, "origin": "C=(32I+5A-4D)/648"},
                {"name": "source_events", "value": 60, "origin": "four preimages per logical transposition"},
            ],
            outputs=[
                {"name": "code_entanglement_fidelity", "value": 2 / 5},
                {"name": "antisymmetric_weight_before", "value": antisymmetric_weight},
                {"name": "lift_min_eigenvalue", "value": float(con["lift_spectrum"][0])},
                {"name": "lift_max_eigenvalue", "value": float(con["lift_spectrum"][-1])},
                {"name": "trace_preserving_after", "value": normalization_residual},
            ],
            formulas=[
                "C=(32I+5A-4D)/648",
                "q=sum_mu L_mu^† L_mu",
                "q|_code=I, q|_{Lambda^4 C4}=10/9",
                "B_mu=L_mu q^{-1/2}",
            ],
            checks=[
                _check("Ereignismatrix positiv und Rang 15", float(con["event_matrix_spectrum"].min()) > 0 and np.linalg.matrix_rank(con["event_matrix"], tol=1e-12) == 15, {"minimum": float(con["event_matrix_spectrum"].min()), "rank": int(np.linalg.matrix_rank(con["event_matrix"], tol=1e-12))}, {"minimum": ">0", "rank": 15}, "direkte Diagonalisierung der 15x15-Matrix"),
                _check("Fünferkanal ist spurtreu", code_tp_residual < 1e-10, code_tp_residual, 0, "Krausfaktorisierung C=BB†, Toleranz 1e-10"),
                _check("Fünferkanalspektrum", _hist(code_spectrum) == [{"value": 0.25, "multiplicity": 10}, {"value": 0.305555556, "multiplicity": 9}, {"value": 0.75, "multiplicity": 5}, {"value": 1.0, "multiplicity": 1}], _hist(code_spectrum), "1^1,(3/4)^5,(11/36)^9,(1/4)^10", "Kraus-Superoperator, Eigenwerte auf 9 Dezimalstellen gruppiert"),
                _check("antisymmetrischer Sektor zeigt 10/9", abs(antisymmetric_weight - 10 / 9) < 1e-10 and np.linalg.norm(lift_norm @ anti - (10 / 9) * anti) < 1e-10, {"weight": antisymmetric_weight, "eigen_residual": np.linalg.norm(lift_norm @ anti - (10 / 9) * anti)}, {"weight": 10 / 9, "eigen_residual": 0}, "direkte volle 256x256-Matrixrechnung, Toleranz 1e-10"),
                _check("Lift ist vor Reparatur nicht spurtreu", np.linalg.norm(lift_norm - np.eye(256)) > 1, np.linalg.norm(lift_norm - np.eye(256)), 0, "||q-I||_F als absichtlicher Gegenfall"),
                _check("funktionale Normierung ist spurtreu", normalization_residual < 2e-8, normalization_residual, 0, "sum B_mu†B_mu=I256, Akzeptanzschranke der Konsolidierung 2e-8"),
                _check("jeder Code-Krauszweig bleibt erhalten", code_branch_residual < 2e-8, code_branch_residual, 0, "max ||B_mu V-L_mu V||, Akzeptanzschranke 2e-8"),
            ],
            sources=[
                _pdf_source(22, "coherent 15-label event matrix and the common code channel"),
                _pdf_source(25, "antisymmetric-sector theorem and necessary normalisation condition"),
                _pdf_source(26, "the concrete source channel gives weight 10/9 on Lambda^4 C4"),
                _pdf_source(27, "finite operator-algebra completion with q inverse square root"),
                _pdf_source(28, "full 256-dimensional numerical repair preserves every code Kraus branch"),
            ],
            depends_on=[
                {"id": "rays", "relation": "derives", "label": "60 vierfache Reflexionsereignisse"},
                {"id": "code", "relation": "feeds", "label": "der bereits normierte Fünferkanal bleibt zweigweise unverändert"},
                {"id": "sourcechannel", "relation": "corresponds", "label": "gemeinsame Quellenfrage; anderer Speicher und anderer Kanal"},
            ],
            visual_type="sector_balance",
            visual_data={
                "before": [
                    {"sector": "Fünfercode", "weight": 1},
                    {"sector": "antisymmetrischer Einerspeicher", "weight": antisymmetric_weight},
                ],
                "after": [
                    {"sector": "Fünfercode", "weight": 1},
                    {"sector": "antisymmetrischer Einerspeicher", "weight": 1},
                ],
                "lift_spectrum": con["lift_spectrum"],
            },
            notes=[
                "Der Wert 10/9 ist ein Gegenbeispiel zur unveränderten linearen 60-Ereignis-Fortsetzung, kein Gegenbeispiel gegen den bereits korrekten Codekanal.",
                "q⁻¹ᐟ² liegt in der von den Ereignissen erzeugten endlichen *-Algebra. Daraus folgt noch keine elementare, lokale oder billige physische Ausführung dieser zusammengesetzten Operation.",
            ],
            assumptions=[
                "Die konkrete Matrixrechnung verwendet die symmetrische gemeinsame Amplitudenlösung, die den angegebenen Fünferkanal realisiert.",
                "Der endliche Reparatursatz bestimmt keine eindeutige primitive Quelle und keinen konsistenten unendlichen Grenzprozess.",
            ],
            data={
                "event_matrix": con["event_matrix"],
                "event_matrix_spectrum": con["event_matrix_spectrum"],
                "code_channel_spectrum": _hist(code_spectrum),
                "lift_spectrum": con["lift_spectrum"],
                "antisymmetric_weight": antisymmetric_weight,
                "normalization_residual": normalization_residual,
                "code_branch_residual": code_branch_residual,
                "scope": "finite 256-dimensional completion inside the generated operator algebra",
            },
        )
    )

    from .composition import build_joint_data
    joint = build_joint_data()
    chain = con["chain"]
    chain_spectrum = np.linalg.eigvalsh(chain["chain"])
    chain_ground_error = float(
        np.linalg.norm(chain["chain"] @ chain["w"] - (2 / 3) * chain["w"])
    )
    cover_counts = {node: con["trimer_nodes"].count(node) for node in range(30)}
    all_path_edges_exist = all(edge in con["incidence_edges"] for edge in con["trimer_edges"])
    periodic = con["periodic"]
    shift_match = all(comparison["ok"] for comparison in periodic["shift_comparisons"])
    orientation_match = all(
        comparison["ok"] for comparison in periodic["orientation_comparisons"]
    )
    trimers = [
        {
            "id": index,
            "center": center,
            "left": left,
            "right": right,
            "left_shift": left_shift,
            "right_shift": right_shift,
            "effective_representation": representation,
        }
        for index, (center, left, right, left_shift, right_shift, representation) in enumerate(TRIMERS)
    ]
    strong_edges = [
        {"source": center, "target": leaf, "trimer": index}
        for index, (center, left, right, *_rest) in enumerate(TRIMERS)
        for leaf in (left, right)
    ]

    stages.append(
        _stage(
            "assembly",
            "Die Rekursion passt jetzt auf das markierte A3-Netz",
            "Zehn periodische Dreierpfade und eine ladungskovariante Fünferisometrie",
            "consolidation",
            130,
            "conditional",
            "Die 30 Knotentypen der Tutte-Coxeter-Zelle zerfallen mit den veröffentlichten Periodenverschiebungen in zehn disjunkte Dreierpfade. Auf jedem Pfad besitzt die geänderte Singulettbindung h_cov einen fünfdimensionalen Grundraum mit Lücke 1/3 und transportiert jede 5x5-Matrix kovariant durch U–Ubar–U.",
            inputs=[
                {"name": "marked_periodic_graph", "value": "30 node types, A3 period lattice", "origin": "selected space stage"},
                {"name": "pair_hamiltonian", "value": "h_cov=5/6(I-P_Omega)", "origin": "declared charge-covariant completion"},
                {"name": "trimer_cover", "value": 10, "origin": "explicit Appendix C construction"},
            ],
            outputs=[
                {"name": "trimers_per_cell", "value": 10},
                {"name": "covered_node_types", "value": len(cover_counts)},
                {"name": "effective_U_blocks", "value": sum(t[-1] == "U" for t in TRIMERS)},
                {"name": "effective_Ubar_blocks", "value": sum(t[-1] == "Ubar" for t in TRIMERS)},
                {"name": "chain_ground_dimension", "value": 5},
                {"name": "chain_gap", "value": 1 / 3},
            ],
            formulas=[
                "h_cov=5/6(I-P_Omega)",
                "H_3=h_cov,12+h_cov,23",
                "(Wx)_abc=(delta_ab x_c+x_a delta_bc)/sqrt(12)",
                "(X_1-X_2^T+X_3)W=WX",
            ],
            checks=[
                _check("zehn Trimere überdecken alle 30 Typen genau einmal", all(count == 1 for count in cover_counts.values()), cover_counts, {node: 1 for node in range(30)}, "vollständige Zählung der publizierten Cover-Tabelle"),
                _check("jede starke Kante ist eine echte Netzkante", all_path_edges_exist, con["trimer_edges"], "20 Matching-Paar-Inzidenzkanten", "Abgleich gegen den vollständigen 45-Kanten-Inzidenzgraphen"),
                _check("fünf fundamentale und fünf konjugierte Blöcke", [sum(t[-1] == "U" for t in TRIMERS), sum(t[-1] == "Ubar" for t in TRIMERS)] == [5, 5], [sum(t[-1] == "U" for t in TRIMERS), sum(t[-1] == "Ubar" for t in TRIMERS)], [5, 5], "Orientierung der zehn Pfadfamilien"),
                _check("effektive Darstellung folgt aus Mittelpunkt und Blättern", orientation_match, periodic["orientation_comparisons"], "Matchingzentrum U mit Ubar-Blättern ergibt Ubar; Paarzentrum Ubar mit U-Blättern ergibt U", "zeilenweiser U/Ubar-Test, nicht nur 5/5-Zählung"),
                _check("harmonische 45-Kanten-Form", np.array_equal(periodic["incidence"] @ HARMONIC_EDGES, np.zeros((30, 3), dtype=int)) and np.array_equal(HARMONIC_EDGES.T @ HARMONIC_EDGES, 48 * np.eye(3, dtype=int)), {"BW": periodic["incidence"] @ HARMONIC_EDGES, "WTW": HARMONIC_EDGES.T @ HARMONIC_EDGES}, {"BW": np.zeros((30, 3), dtype=int), "WTW": 48 * np.eye(3, dtype=int)}, "vollständige Appendix-D-Tabelle"),
                _check("Periodengitter ist L Z3", periodic["integrality_error"] < 1e-10 and periodic["lattice_index"] == 1, {"integrality_error": periodic["integrality_error"], "integer_span_index": periodic["lattice_index"], "L": PERIOD_BASIS}, {"integrality_error": 0, "integer_span_index": 1, "L": PERIOD_BASIS}, "kanonische BFS-Spannbaumeichung; gcd der nichtverschwindenden 3x3-Spannungsminoren"),
                _check("Cover-Verschiebungen aus harmonischen Kanten rekonstruiert", shift_match, periodic["shift_comparisons"], "alle 20 deklarierten Blattverschiebungen", "feste, von der Cover-Tabelle unabhängige lexikographische BFS-Spannbaumeichung"),
                _check("mutierte Cover-Verschiebung wird verworfen", con["shift_mutation_rejected"], con["shift_mutation_rejected"], True, "erste Nullverschiebung um eine Periodeneinheit verändert; derselbe feste Gauge-Vergleich muss scheitern"),
                _check("Dreierketten-Spektrum", _hist(chain_spectrum) == [{"value": 0.666666667, "multiplicity": 5}, {"value": 1.0, "multiplicity": 5}, {"value": 1.666666667, "multiplicity": 115}], _hist(chain_spectrum), "(2/3)^5,1^5,(5/3)^115", "direkte 125x125-Diagonalisierung"),
                _check("W ist die Fünfer-Grundraumisometrie", np.linalg.norm(chain["w"].T @ chain["w"] - np.eye(5)) < 1e-10 and chain_ground_error < 1e-10, {"isometry": np.linalg.norm(chain["w"].T @ chain["w"] - np.eye(5)), "ground": chain_ground_error}, {"isometry": 0, "ground": 0}, "explizites W aus Gleichung (13.1), Toleranz 1e-10"),
                _check("volle 5x5-Kovarianz", chain["covariance_error"] < 1e-10, chain["covariance_error"], 0, "alle 25 Matrixeinheiten, Toleranz 1e-10"),
                _check("markierte Ladung bleibt auf jeder Kante erhalten", con["charge_commutator"] < 1e-10, con["charge_commutator"], 0, "[h_cov,Y tensor I-I tensor Y^T], Toleranz 1e-10"),
                *joint["checks"],
            ],
            sources=[
                _source(DOC_RESULTS, 126, "the earlier graph selection does not connect the old triangle recursion to the triangle-free incidence graph"),
                _source("_newest2/TFPT_Gesamtdokumentation2_20260927.md", 1558, "charge-covariant pair Hamiltonian h_cov"),
                _source("_newest2/TFPT_Gesamtdokumentation2_20260927.md", 1591, "explicit U-Ubar-U trimer isometry and gap 1/3"),
                _pdf_source(42, "marked periodic A3 graph and its three-dimensional diffusion response"),
                _pdf_source(43, "ten-path periodic cover and local charge-covariant Hamiltonian family"),
                _pdf_source(44, "the construction changes the binding branch and does not prove a unique world process"),
                _pdf_source(63, "complete trimer cover table with period shifts"),
                _pdf_source(64, "45 harmonic edge vectors with B W=0, W^T W=48 I and the period basis L"),
            ],
            depends_on=[
                {"id": "space", "relation": "derives", "label": "markiertes A3-Periodennetz und seine echte Inzidenz"},
                {"id": "observables", "relation": "feeds", "label": "3+2-Ladung mit konjugiertem Vorzeichen auf der bipartiten Seite"},
                {"id": "recursion", "relation": "corresponds", "label": "geänderter Pfadzweig h_cov statt alter Dreiecksbindung"},
            ],
            visual_type="lattice",
            visual_data={
                "nodes": [
                    {"id": node, "group": "matching" if node < 15 else "pair", "trimer": next(i for i, trimer in enumerate(TRIMERS) if node in trimer[:3])}
                    for node in range(30)
                ],
                "strong_edges": strong_edges,
                "trimers": trimers,
                "period_basis": [[6, 3, 3], [0, 3, 0], [0, 0, 3]],
            },
            notes=[
                "Diese Montage schließt die geometrische Lücke zwischen einem dreieckfreien Netz und einer Fünferrekursion, indem sie echte Pfade verwendet.",
                "Sie verwendet h_cov und nicht die ursprüngliche Ereignisbindung k, die alte Antwortbindung -K oder deren Dreieckstensor. Die alte Rekursion bleibt ein anderer mathematischer Zweig.",
                "Die 25 Restkanten ergeben 15 gegenorientierte Blatt–Blatt- und zehn gleichorientierte Mitte–Blatt-Kopplungen. Beide Invariantentypen werden bei der Blockbildung benötigt.",
                "Neu berechnet: Die positive Neun-Port-Vervollständigung schließt exakt auf dieselbe Bindungsfamilie plus 4I pro Brücke. Sie ist eine zusätzliche Kompositionsregel; das ursprüngliche Netz enthält pro Blockpaar nur einen Restlink.",
            ],
            assumptions=[
                "Markierung, Ortsdeutung, U/Ubar-Zuordnung, Trimer-Cover und das Verhältnis schwacher zu starker Kanten sind ausgewählt.",
                "Die primitive TFPT-Quelle wählt diese Montage bislang nicht eindeutig aus.",
            ],
            data={
                "composition": joint["data"],
                "trimers": trimers,
                "cover_counts": cover_counts,
                "period_basis": [[6, 3, 3], [0, 3, 0], [0, 0, 3]],
                "strong_edges": strong_edges,
                "period_edges": [
                    {
                        "source": source,
                        "target": target,
                        "harmonic": HARMONIC_EDGES[index],
                        "period": periodic["voltages"][(source, target)],
                    }
                    for index, (source, target) in enumerate(periodic["graph_edges"])
                ],
                "chain_spectrum": _hist(chain_spectrum),
                "covariance_residual": chain["covariance_error"],
                "charge_commutator": con["charge_commutator"],
                "shift_comparisons": periodic["shift_comparisons"],
                "orientation_comparisons": periodic["orientation_comparisons"],
                "hodge": {
                    "divergence": periodic["incidence"] @ HARMONIC_EDGES,
                    "gram": HARMONIC_EDGES.T @ HARMONIC_EDGES,
                    "integrality_error": periodic["integrality_error"],
                    "integer_span_index": periodic["lattice_index"],
                },
                "shift_mutation_rejected": con["shift_mutation_rejected"],
                "scope": "explicit marked periodic construction; not a source-selected unique vacuum or continuum spacetime",
            },
        )
    )

    return stages


__all__ = ["build_stages"]
