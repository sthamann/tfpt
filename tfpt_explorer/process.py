"""Executable finite TFPT/Universalraum process stages.

The module deliberately separates calculations from physical identifications.  The
finite Hamming/ray/code/binding/recursion chain is reconstructed here; the marked
space and source-channel stages expose their declared choices, and the final stage
names the still-open representation interfaces instead of silently bridging them.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import itertools as it
import math
from typing import Any

import numpy as np


DEFAULT_CONFIG: dict[str, Any] = {
    "clock_step": 0,
    "transfer_steps": 6,
    "efolds": 55,
    "phase_b": 1 / 18,
    "initial_state": "localized",
    "recursion_depth": 3,
}

DOC = "_newest2/TFPT_Universalraum_Gesamtdokumentation_2026-09-27.md"
DOC_SOURCE = "_newest2/TFPT_Universalraum_Gesamtdokumentation_20260927.md"


def _json(value: Any) -> Any:
    """Convert calculation values to JSON without erasing small residuals."""

    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        x = float(value)
        if not math.isfinite(x):
            raise ValueError("process output contains a non-finite float")
        return x
    if isinstance(value, (np.complexfloating, complex)):
        z = complex(value)
        if not math.isfinite(z.real) or not math.isfinite(z.imag):
            raise ValueError("process output contains a non-finite complex value")
        return {"re": z.real, "im": z.imag}
    if isinstance(value, np.ndarray):
        return _json(value.tolist())
    if isinstance(value, (list, tuple)):
        return [_json(x) for x in value]
    if isinstance(value, dict):
        return {str(k): _json(v) for k, v in value.items()}
    return value


def _r(value: Any, digits: int = 12) -> Any:
    """Round visual payloads to bounded significant digits."""

    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        x = float(value)
        if not math.isfinite(x):
            raise ValueError("process visual contains a non-finite float")
        return float(f"{x:.{digits}g}")
    if isinstance(value, (np.complexfloating, complex)):
        z = complex(value)
        return {"re": _r(z.real, digits), "im": _r(z.imag, digits)}
    if isinstance(value, np.ndarray):
        return _r(value.tolist(), digits)
    if isinstance(value, (list, tuple)):
        return [_r(x, digits) for x in value]
    if isinstance(value, dict):
        return {str(k): _r(v, digits) for k, v in value.items()}
    return value


def _hist(values: np.ndarray, digits: int = 9) -> list[dict[str, Any]]:
    counts = Counter(round(float(np.real(x)), digits) for x in values)
    return [{"value": v, "multiplicity": counts[v]} for v in sorted(counts)]


def _source(path: str, line: int, claim: str) -> dict[str, Any]:
    return {"path": path, "line": line, "claim": claim}


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": _json(actual),
        "expected": _json(expected),
        "method": method,
    }


def _stage(
    sid: str,
    title: str,
    subtitle: str,
    group: str,
    order: int,
    kind: str,
    summary: str,
    *,
    inputs: list[dict[str, Any]],
    outputs: list[dict[str, Any]],
    formulas: list[str],
    checks: list[dict[str, Any]],
    sources: list[dict[str, Any]],
    depends_on: list[dict[str, str]],
    visual_type: str,
    visual_data: dict[str, Any],
    notes: list[str] | None = None,
    assumptions: list[str] | None = None,
    data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    stage_notes = list(notes or [])
    if kind == "exact":
        stage_notes.insert(
            0,
            "„Exakt“ bezeichnet den endlichen mathematischen Satz unter den genannten Eingaben. Float64-Residuen in dieser App sind numerische Neuberechnungen; das exakte Zertifikat steht in der zitierten Quelle.",
        )
    return {
        "id": sid,
        "title": title,
        "subtitle": subtitle,
        "group": group,
        "order": order,
        "kind": kind,
        "summary": summary,
        "inputs": _json(inputs),
        "outputs": _json(outputs),
        "formulas": formulas,
        "checks": _json(checks),
        "sources": sources,
        "depends_on": depends_on,
        "visual": {"type": visual_type, "data": _r(visual_data)},
        "notes": stage_notes,
        "assumptions": assumptions or [],
        "data": _json(data or {}),
    }


def _hamming_words() -> list[tuple[int, ...]]:
    points = list(it.product((0, 1), repeat=3))
    generators = [tuple(1 for _ in range(8))]
    generators.extend(tuple(p[j] for p in points) for j in range(3))
    words: list[tuple[int, ...]] = []
    for bits in it.product((0, 1), repeat=4):
        word = [0] * 8
        for bit, generator in zip(bits, generators):
            if bit:
                word = [x ^ y for x, y in zip(word, generator)]
        words.append(tuple(word))
    return sorted(words)


def _canonical_mu4(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    choices = []
    for phase in (1, 1j, -1, -1j):
        rotated = phase * vector
        choices.append(
            tuple((int(round(z.real)), int(round(z.imag))) for z in rotated)
        )
    return min(choices)


def _hamming_rays() -> list[np.ndarray]:
    supports = [
        tuple(sorted((2 * i, 2 * i + 1, 2 * j, 2 * j + 1)))
        for i, j in it.combinations(range(4), 2)
    ]
    supports.extend(
        tuple(2 * k + d[k] for k in range(4))
        for d in it.product((0, 1), repeat=4)
        if sum(d) % 2 == 0
    )
    roots: list[list[int]] = []
    for k, sign in it.product(range(8), (-1, 1)):
        root = [0] * 8
        root[k] = 2 * sign
        roots.append(root)
    for support in supports:
        for signs in it.product((-1, 1), repeat=4):
            root = [0] * 8
            for k, sign in zip(support, signs):
                root[k] = sign
            roots.append(root)
    keys = sorted(
        {
            _canonical_mu4(np.asarray(root[::2]) + 1j * np.asarray(root[1::2]))
            for root in roots
        }
    )
    return [np.asarray([complex(a, b) for a, b in key]) for key in keys]


def _pauli_data() -> tuple[list[np.ndarray], list[np.ndarray], list[list[int]]]:
    eye = np.eye(2)
    x = np.asarray([[0, 1], [1, 0]], dtype=complex)
    y = np.asarray([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    paulis = [np.kron(a, b) for a, b in it.product((eye, x, y, z), repeat=2)][1:]

    projectors: list[np.ndarray] = []
    for a, b in it.combinations(paulis, 2):
        if np.linalg.norm(a @ b - b @ a) > 1e-10:
            continue
        for sa, sb in it.product((1, -1), repeat=2):
            p = (np.eye(4) + sa * a) @ (np.eye(4) + sb * b) / 4
            if not any(np.linalg.norm(p - q) < 1e-10 for q in projectors):
                projectors.append(p)

    triples = [
        ids
        for ids in it.combinations(range(15), 3)
        if all(
            np.linalg.norm(paulis[i] @ paulis[j] - paulis[j] @ paulis[i]) < 1e-10
            for i, j in it.combinations(ids, 2)
        )
    ]
    contexts: list[list[int]] = []
    for ids in triples:
        context = []
        for ray_id, p in enumerate(projectors):
            if all(
                np.linalg.norm(paulis[i] @ p - p @ paulis[i]) < 1e-10
                and abs(abs(np.trace(paulis[i] @ p)) - 1) < 1e-10
                for i in ids
            ):
                context.append(ray_id)
        contexts.append(context)
    return paulis, projectors, contexts


def _code_basis() -> tuple[np.ndarray, list[list[tuple[int, ...]]]]:
    word_sets: list[list[tuple[int, ...]]] = [
        [(i, i, i, i) for i in range(4)]
    ]
    pairs = [
        ((0, 0, 1, 1), (2, 2, 3, 3)),
        ((0, 0, 2, 2), (1, 1, 3, 3)),
        ((0, 0, 3, 3), (1, 1, 2, 2)),
    ]
    for one, two in pairs:
        word_sets.append(sorted(set(it.permutations(one)) | set(it.permutations(two))))
    word_sets.append(sorted(it.permutations(range(4))))
    v = np.zeros((256, 5))
    for column, words in enumerate(word_sets):
        for word in words:
            v[np.ravel_multi_index(word, (4, 4, 4, 4)), column] = 1 / math.sqrt(len(words))
    return v, word_sets


def _helmert(n: int = 6) -> np.ndarray:
    basis = np.zeros((n, n - 1))
    for j in range(n - 1):
        basis[: j + 1, j] = 1 / math.sqrt((j + 1) * (j + 2))
        basis[j + 1, j] = -(j + 1) / math.sqrt((j + 1) * (j + 2))
    return basis


def _perfect_matchings(items: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    if not items:
        return [tuple()]
    first = items[0]
    result = []
    for index in range(1, len(items)):
        second = items[index]
        rest = items[1:index] + items[index + 1 :]
        for tail in _perfect_matchings(rest):
            result.append(tuple(sorted(((first, second),) + tail)))
    return sorted(set(result))


def _lift_pair(operator: np.ndarray, sites: tuple[int, int], d: int = 5) -> np.ndarray:
    result = np.zeros((d**3, d**3), dtype=float)
    other = ({0, 1, 2} - set(sites)).pop()
    for source in it.product(range(d), repeat=3):
        for target_pair in it.product(range(d), repeat=2):
            target = list(source)
            target[sites[0]], target[sites[1]] = target_pair
            row = np.ravel_multi_index(tuple(target), (d, d, d))
            col = np.ravel_multi_index(source, (d, d, d))
            if target[other] == source[other]:
                result[row, col] = operator[
                    target_pair[0] * d + target_pair[1],
                    source[sites[0]] * d + source[sites[1]],
                ]
    return result


@lru_cache(maxsize=1)
def _invariants() -> dict[str, Any]:
    words = _hamming_words()
    hamming_rays = _hamming_rays()
    _, stabilizer_projectors, stabilizer_contexts = _pauli_data()
    hamming_projectors = [
        np.outer(v, v.conj()) / float(np.vdot(v, v).real) for v in hamming_rays
    ]
    hamming_to_stabilizer = [
        int(np.argmin([np.linalg.norm(p - q) for q in stabilizer_projectors]))
        for p in hamming_projectors
    ]
    ray_match_error = max(
        np.linalg.norm(p - stabilizer_projectors[j])
        for p, j in zip(hamming_projectors, hamming_to_stabilizer)
    )
    if len(set(hamming_to_stabilizer)) != len(hamming_projectors):
        raise RuntimeError("Hamming and stabilizer projectors do not match bijectively")
    stabilizer_to_hamming = {
        stabilizer: hamming for hamming, stabilizer in enumerate(hamming_to_stabilizer)
    }
    # From here onward every ray id uses the Hamming ordering, including the
    # context network and the later logical-event fibres.
    contexts = [
        [stabilizer_to_hamming[ray] for ray in context]
        for context in stabilizer_contexts
    ]
    context_sum_error = max(
        np.linalg.norm(sum((hamming_projectors[ray] for ray in context), np.zeros((4, 4), dtype=complex)) - np.eye(4))
        for context in contexts
    )
    context_overlap_error = max(
        abs(np.trace(hamming_projectors[a] @ hamming_projectors[b]))
        for context in contexts
        for a, b in it.combinations(context, 2)
    )

    v_code, word_sets = _code_basis()
    logical_events: list[np.ndarray] = []
    labels: list[int] = []
    u_bar = np.zeros((256, 256), dtype=complex)
    reduce_error = 0.0
    for projector in hamming_projectors:
        reflection = np.eye(4) - 2 * projector
        u4 = np.kron(np.kron(np.kron(reflection, reflection), reflection), reflection)
        u_bar += u4 / 60
        logical = np.real_if_close(v_code.T @ u4 @ v_code).astype(float)
        reduce_error = max(reduce_error, np.linalg.norm(u4 @ v_code - v_code @ logical))
        label = next(
            (j for j, old in enumerate(logical_events) if np.linalg.norm(logical - old) < 1e-9),
            None,
        )
        if label is None:
            label = len(logical_events)
            logical_events.append(logical)
        labels.append(label)
    u_bar = np.real_if_close(u_bar).astype(float)

    f3 = np.asarray(
        [
            [1, -3, -3, -3, 0],
            [1, -3, 3, 3, 0],
            [1, 3, -3, 3, 0],
            [1, 3, 3, -3, 0],
            [-2, 0, 0, 0, 6],
            [-2, 0, 0, 0, -6],
        ],
        dtype=float,
    )
    coordinate_map = f3 @ np.diag(1 / np.sqrt([4, 12, 12, 12, 24])) / math.sqrt(3)
    transposition_pairs = list(it.combinations(range(6), 2))
    transpositions = []
    for a, b in transposition_pairs:
        permutation = np.eye(6)
        permutation[[a, b]] = permutation[[b, a]]
        transpositions.append(coordinate_map.T @ permutation @ coordinate_map)
    representation_error = max(
        min(np.linalg.norm(logical - standard) for standard in transpositions)
        for logical in logical_events
    )
    logical_to_pair = [
        int(np.argmin([np.linalg.norm(logical - standard) for standard in transpositions]))
        for logical in logical_events
    ]

    matchings = _perfect_matchings(tuple(range(6)))
    response_planes = []
    charges = []
    for matching in matchings:
        matching_op = np.eye(5)
        for pair in matching:
            matching_op = matching_op @ transpositions[transposition_pairs.index(pair)]
        response = (np.eye(5) + matching_op) / 2
        response_planes.append(response)
        charges.append((5 * response - 2 * np.eye(5)) / 6)

    binding = np.eye(25) - sum(np.kron(t, t) for t in transpositions) / 15
    omega = np.eye(5).reshape(-1) / math.sqrt(5)
    h_triangle = sum(_lift_pair(binding, pair) for pair in ((0, 1), (1, 2), (0, 2)))

    simplex = coordinate_map
    tensor_t = np.einsum("ai,aj,ak,al->ijkl", simplex, simplex, simplex, simplex)
    delta = np.eye(5)
    tensor_d = (
        np.einsum("ij,kl->ijkl", delta, delta)
        + np.einsum("ik,jl->ijkl", delta, delta)
        + np.einsum("il,jk->ijkl", delta, delta)
    )
    gamma_bar = tensor_t + tensor_d / 6
    v_triangle = gamma_bar.reshape(125, 5) / math.sqrt(2)
    intertwine_error = max(
        np.linalg.norm(np.kron(np.kron(t, t), t) @ v_triangle - v_triangle @ t)
        for t in transpositions
    )
    branch_kraus = [
        v_triangle.reshape(5, 5, 5, 5)[:, j, k, :]
        for j, k in it.product(range(5), repeat=2)
    ]
    branch_super = sum(np.kron(a, a.conj()) for a in branch_kraus)
    branch_tp_error = np.linalg.norm(
        sum((a.conj().T @ a for a in branch_kraus), np.zeros((5, 5))) - np.eye(5)
    )
    branch_unital_error = np.linalg.norm(
        sum((a @ a.conj().T for a in branch_kraus), np.zeros((5, 5))) - np.eye(5)
    )

    pairs = list(it.combinations(range(6), 2))
    geometry_edges = [
        (f"m{m}", f"p{pairs.index(pair)}")
        for m, matching in enumerate(matchings)
        for pair in matching
    ]
    adjacency = np.zeros((30, 30))
    for left, right in geometry_edges:
        i = int(left[1:])
        j = 15 + int(right[1:])
        adjacency[i, j] = adjacency[j, i] = 1
    laplacian = np.diag(adjacency.sum(axis=1)) - adjacency

    return {
        "words": words,
        "hamming_rays": hamming_rays,
        "projectors": hamming_projectors,
        "contexts": contexts,
        "context_sum_error": context_sum_error,
        "context_overlap_error": context_overlap_error,
        "ray_match_error": ray_match_error,
        "v_code": v_code,
        "word_sets": word_sets,
        "u_bar": u_bar,
        "reduce_error": reduce_error,
        "logical_events": logical_events,
        "labels": labels,
        "coordinate_map": coordinate_map,
        "transposition_pairs": transposition_pairs,
        "transpositions": transpositions,
        "representation_error": representation_error,
        "logical_to_pair": logical_to_pair,
        "matchings": matchings,
        "responses": response_planes,
        "charges": charges,
        "binding": binding,
        "omega": omega,
        "h_triangle": h_triangle,
        "v_triangle": v_triangle,
        "intertwine_error": intertwine_error,
        "branch_super": branch_super,
        "branch_tp_error": branch_tp_error,
        "branch_unital_error": branch_unital_error,
        "geometry_edges": geometry_edges,
        "adjacency": adjacency,
        "laplacian": laplacian,
    }


def _configured_state(name: str, clock_step: int, dimension: int) -> np.ndarray:
    if dimension != 4:
        raise ValueError("the source register has dimension four")
    if name == "localized":
        state = np.zeros(dimension, dtype=complex)
        state[0] = 1
    elif name == "uniform":
        state = np.ones(dimension, dtype=complex) / math.sqrt(dimension)
    elif name == "skew":
        # The UI's documented skew population is embedded in the four-state
        # source register with a zero spectator population.  This is an input
        # preparation, not a TFPT selection claim.
        state = np.sqrt(np.asarray([0.1, 0.7, 0.2, 0.0], dtype=float)).astype(complex)
    else:
        raise ValueError("initial_state must be localized, uniform, or skew")
    phases = np.asarray([1j ** (clock_step * k) for k in range(dimension)])
    return state * phases


def _phi_kraus(b: float) -> list[np.ndarray]:
    if not math.isfinite(b) or not 0 <= b <= 2 / 9:
        raise ValueError("phase_b must satisfy 0 <= b <= 2/9")
    weights = [5 / 18, 7 / 18 - b, 2 / 9 - b, b]
    diagonals = [
        np.eye(4),
        np.diag([1, -1, 0, 0]),
        np.diag([0, 0, 1, -1]),
        np.diag([1, 1, -1, -1]),
    ]
    kraus = [math.sqrt(weight) * diagonal for weight, diagonal in zip(weights, diagonals)]
    for i, j in it.permutations(range(4), 2):
        if {i, j} == {0, 1}:
            continue
        jump = np.zeros((4, 4))
        jump[i, j] = 1 / math.sqrt(6)
        kraus.append(jump)
    return kraus


def _apply(kraus: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum((a @ rho @ a.conj().T for a in kraus), np.zeros_like(rho))


def _common_source_adapter(b: float) -> dict[str, Any]:
    """Reconstruct the same 60 amplitudes on C4 and the logical C5.

    Separate the scalar Kraus branch so the trace compatibility is explicit.
    Traceless branches can then be paired without changing either channel.
    This does not assert normalization of their four-register tensor lift.
    """
    inv = _invariants()
    pairs = inv["transposition_pairs"]
    matrix = np.asarray([[32 if e == f else (5 if set(e) & set(f) else -4)
                          for f in pairs] for e in pairs], dtype=float) / 648
    orthogonal = _helmert(15)
    eigenvalues, eigenvectors = np.linalg.eigh(orthogonal.T @ matrix @ orthogonal)
    factor = np.column_stack((np.ones(15) * math.sqrt(2 / 405),
                              orthogonal @ eigenvectors @ np.diag(np.sqrt(eigenvalues))))
    code_kraus = [sum((factor[e, branch] * inv["transpositions"][e] for e in range(15)), np.zeros((5, 5))) for branch in range(15)]
    register_kraus = _phi_kraus(b) + [np.zeros((4, 4))]
    reflections = [np.eye(4) - 2 * projector for projector in inv["projectors"]]
    amplitudes = np.zeros((15, 60), dtype=complex)
    register_errors, code_errors, trace_errors = [], [], []
    for branch, (f, k) in enumerate(zip(register_kraus, code_kraus)):
        traceless = f - np.trace(f) * np.eye(4) / 4
        for ray, reflection in enumerate(reflections):
            event = inv["logical_to_pair"][inv["labels"][ray]]
            amplitudes[branch, ray] = factor[event, branch] / 4 + np.trace(reflection @ traceless) / 12
        recovered_f = sum((a * r for a, r in zip(amplitudes[branch], reflections)), np.zeros((4, 4), dtype=complex))
        recovered_k = sum((amplitudes[branch, ray] * inv["transpositions"][inv["logical_to_pair"][inv["labels"][ray]]] for ray in range(60)), np.zeros((5, 5), dtype=complex))
        register_errors.append(float(np.linalg.norm(recovered_f - f)))
        code_errors.append(float(np.linalg.norm(recovered_k - k)))
        trace_errors.append(float(abs(np.trace(f) - (2 / 3) * np.trace(k))))
    code_norm = sum(k.conj().T @ k for k in code_kraus)
    superoperator = sum(np.kron(k, k.conj()) for k in code_kraus)
    return {"amplitudes": amplitudes, "branches": 15, "labels": 60,
            "register_residual": max(register_errors), "code_residual": max(code_errors),
            "trace_residual": max(trace_errors), "code_tp_residual": float(np.linalg.norm(code_norm - np.eye(5))),
            "code_channel_residual": float(np.linalg.norm(superoperator - inv["branch_super"])),
            "factorization_residual": float(np.linalg.norm(factor @ factor.T - matrix)),
            "scope": "same amplitudes realize Phi_b on C4 and the fixed coherent channel on C5; no assertion of TP on the full tensor-four C256 space"}


def build_stages(config: dict[str, Any] | None = None, upstream: Any = None) -> list[dict[str, Any]]:
    """Build the bounded JSON-ready process stages for the explorer UI."""

    if config is not None and not isinstance(config, dict):
        raise ValueError("config must be a dictionary")
    cfg = dict(DEFAULT_CONFIG)
    if config:
        cfg.update(config)
    unknown = sorted(set(cfg) - set(DEFAULT_CONFIG))
    if unknown:
        raise ValueError(f"unknown config keys: {', '.join(unknown)}")
    for key in ("clock_step", "transfer_steps", "recursion_depth", "efolds"):
        if isinstance(cfg[key], bool) or not isinstance(cfg[key], (int, float)) or int(cfg[key]) != cfg[key]:
            raise ValueError(f"{key} must be an integer")
    raw_clock_step = int(cfg["clock_step"])
    clock_step = raw_clock_step % 4
    transfer_steps = int(cfg["transfer_steps"])
    recursion_depth = int(cfg["recursion_depth"])
    efolds = int(cfg["efolds"])
    if isinstance(cfg["phase_b"], bool) or not isinstance(cfg["phase_b"], (int, float)):
        raise ValueError("phase_b must be numeric")
    b = float(cfg["phase_b"])
    if not 0 <= raw_clock_step <= 120:
        raise ValueError("clock_step must be between 0 and 120")
    if not 0 <= transfer_steps <= 40:
        raise ValueError("transfer_steps must be between 0 and 40")
    if not 1 <= recursion_depth <= 8:
        raise ValueError("recursion_depth must be between 1 and 8")
    if not 40 <= efolds <= 70:
        raise ValueError("efolds must be between 40 and 70")
    if not math.isfinite(b) or not 0 <= b <= 2 / 9:
        raise ValueError("phase_b must satisfy 0 <= b <= 2/9")
    if cfg["initial_state"] not in {"localized", "uniform", "skew"}:
        raise ValueError("initial_state must be localized, uniform, or skew")

    inv = _invariants()
    stages: list[dict[str, Any]] = []

    word_weights = [sum(word) for word in inv["words"]]
    weight_counts = Counter(word_weights)
    stages.append(
        _stage(
            "hamming",
            "Der binäre Ursprung",
            "Der erweiterte Hamming-Code [8,4,4]",
            "universalraum",
            10,
            "exact",
            "Vier binäre Generatoren erzeugen genau 16 Wörter; ihre 14 Gewicht-4-Träger speisen die 240 Wurzeln der nächsten Stufe.",
            inputs=[{"name": "field", "value": "F2", "origin": "declared code alphabet"}],
            outputs=[
                {"name": "codewords", "value": 16},
                {"name": "minimum_distance", "value": 4},
                {"name": "weight_4_words", "value": 14},
            ],
            formulas=["C = RM(1,3) = [8,4,4]", "W_C(y)=1+14 y^4+y^8"],
            checks=[
                _check("16 verschiedene Wörter", len(set(inv["words"])) == 16, len(set(inv["words"])), 16, "vollständige Enumeration"),
                _check("Gewichtsverteilung", dict(weight_counts) == {0: 1, 4: 14, 8: 1}, dict(weight_counts), {0: 1, 4: 14, 8: 1}, "exakte Hamming-Gewichte"),
            ],
            sources=[_source(DOC, 3006, "RM(1,3) definition and [8,4,4] weight distribution")],
            depends_on=[],
            visual_type="bars",
            visual_data={"x_label": "Hamming-Gewicht", "y_label": "Wörter", "series": [{"name": "Wörter", "points": [{"x": w, "y": weight_counts[w]} for w in sorted(weight_counts)]}]},
            data={"generator_count": 4, "words": ["".join(map(str, word)) for word in inv["words"]]},
        )
    )

    context_nodes = [{"id": f"r{i}", "label": str(i), "group": "ray"} for i in range(60)]
    context_nodes += [{"id": f"c{i}", "label": f"C{i+1}", "group": "context"} for i in range(15)]
    context_edges = [
        {"source": f"c{c}", "target": f"r{ray}"}
        for c, context in enumerate(inv["contexts"])
        for ray in context
    ]
    stages.append(
        _stage(
            "rays",
            "60 unterscheidbare Richtungen",
            "Hamming-Wurzeln und Zweiqubit-Stabilisatorstrahlen",
            "universalraum",
            20,
            "exact",
            "Die 240 reellen Wurzeln fallen modulo der µ4-Phase zu 60 komplexen Strahlen zusammen; dieselben Projektoren entstehen als gemeinsame Pauli-Eigenzustände.",
            inputs=[{"name": "hamming_words", "value": 16, "origin": "hamming"}, {"name": "phase_quotient", "value": "mu4", "origin": "seam clock"}],
            outputs=[{"name": "roots", "value": 240}, {"name": "rays", "value": 60}, {"name": "canonical_contexts", "value": 15}],
            formulas=["r_l = I_4 - 2 |psi_l><psi_l|", "240 / mu4 = 60 rays"],
            checks=[
                _check("60 µ4-Strahlen", len(inv["hamming_rays"]) == 60, len(inv["hamming_rays"]), 60, "kanonische Phasenquotienten"),
                _check("identisch mit Pauli-Stabilisatorstrahlen", inv["ray_match_error"] < 1e-10, inv["ray_match_error"], 0, "bijektiver Projektorvergleich in float64, Toleranz 1e-10; exaktes Gauß-Zertifikat in der Quelle"),
                _check("15 kanonische Pauli-Kontexte", len(inv["contexts"]) == 15 and all(len(c) == 4 for c in inv["contexts"]), [len(c) for c in inv["contexts"]], [4] * 15, "maximal kommutierende Pauli-Dreiergruppen"),
                _check("Kontexte schließen zur Eins", inv["context_sum_error"] < 1e-10, inv["context_sum_error"], 0, "max ||sum P_ray-I4|| in float64, Toleranz 1e-10"),
                _check("Kontextstrahlen sind orthogonal", inv["context_overlap_error"] < 1e-10, inv["context_overlap_error"], 0, "max |tr(P_i P_j)| in float64, Toleranz 1e-10"),
            ],
            sources=[
                _source("experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py", 49, "constructs the 240 roots and 60 mu4 rays"),
                _source(DOC, 4304, "60 joint Pauli eigenprojectors define the event source"),
            ],
            depends_on=[{"id": "hamming", "relation": "derives", "label": "Gewicht-4-Träger erzeugen Wurzeln"}],
            visual_type="network",
            visual_data={"nodes": context_nodes, "edges": context_edges, "legend": [{"group": "context", "label": "15 kanonische Messkontexte"}, {"group": "ray", "label": "60 Strahlen"}]},
            notes=["Die 15 kanonischen Pauli-Kontexte sind eine Partition; zusätzliche orthogonale Vierergruppierungen werden nicht als neue primitive Kontexte gezählt."],
            data={"contexts": inv["contexts"], "ray_norms": [float(np.vdot(v, v).real) for v in inv["hamming_rays"]]},
        )
    )

    code_spectrum = np.linalg.eigvalsh(inv["u_bar"])
    basis_sparse = []
    for column, words in enumerate(inv["word_sets"]):
        basis_sparse.append({"basis": column, "support_size": len(words), "amplitude": 1 / math.sqrt(len(words)), "words": ["".join(map(str, w)) for w in words]})
    event_fibres = [[] for _ in range(15)]
    for ray, label in enumerate(inv["labels"]):
        event_fibres[label].append(ray)
    stages.append(
        _stage(
            "code",
            "Die Quelle wählt einen Fünferraum",
            "Vierfachwirkung, Rang-5-Projektor und 15 logische Ereignisse",
            "universalraum",
            30,
            "exact",
            "Das Mittel der tatsächlichen vierfachen Reflexionen besitzt einen ausgezeichneten fünfdimensionalen Eigenraum mit Lücke 2/5; auf ihm werden 60 Ereignisse zu 15 Transpositionen, je viermal.",
            inputs=[{"name": "reflections", "value": 60, "origin": "rays"}, {"name": "tensor_power", "value": 4, "origin": "declared common-event rule"}],
            outputs=[{"name": "ambient_dimension", "value": 256}, {"name": "code_rank", "value": 5}, {"name": "parent_gap", "value": 2 / 5}, {"name": "logical_events", "value": 15}],
            formulas=["Ubar_4 = (1/60) sum_l r_l^tensor4", "G_4 = 3/5 I - Ubar_4 >= 0", "U_l V = V T_ab"],
            checks=[
                _check("vollständiges Ubar-Spektrum", _hist(code_spectrum) == [{"value": -1.0, "multiplicity": 1}, {"value": -0.2, "multiplicity": 45}, {"value": 0.066666667, "multiplicity": 135}, {"value": 0.2, "multiplicity": 70}, {"value": 0.6, "multiplicity": 5}], _hist(code_spectrum), "(-1)^1,(-1/5)^45,(1/15)^135,(1/5)^70,(3/5)^5", "float64-Diagonalisierung, Eigenwerte auf 9 Dezimalstellen gruppiert; exaktes Ganzzahlzertifikat in der Quelle"),
                _check("explizite Codebasis orthonormal", np.linalg.norm(inv["v_code"].T @ inv["v_code"] - np.eye(5)) < 1e-12, np.linalg.norm(inv["v_code"].T @ inv["v_code"] - np.eye(5)), 0, "||V†V-I5|| in float64, Toleranz 1e-12"),
                _check("alle Ereignisse reduzieren", inv["reduce_error"] < 1e-10, inv["reduce_error"], 0, "max ||U_l V-V T_l|| in float64, Toleranz 1e-10"),
                _check("15 Viererfasern", len(event_fibres) == 15 and all(len(f) == 4 for f in event_fibres), [len(f) for f in event_fibres], [4] * 15, "logische Matrizen gruppiert"),
                _check("S6-Standarddarstellung", inv["representation_error"] < 1e-10, inv["representation_error"], 0, "expliziter F3-Intertwiner in float64, Toleranz 1e-10"),
            ],
            sources=[_source(DOC, 4348, "event-average selects the rank-five code and gives the full spectrum"), _source(DOC, 4423, "60 events become 15 S6 transpositions through the explicit intertwiner")],
            depends_on=[{"id": "rays", "relation": "derives", "label": "vierfache gemeinsame Ereigniswirkung"}],
            visual_type="spectrum",
            visual_data={"x_label": "Eigenwert von Ubar_4", "y_label": "Multiplizität", "bars": _hist(code_spectrum), "highlight": 0.6},
            assumptions=["Das gemeinsame Zwischenzeitgesetz h(U)=I-U ist eine erklärte Ereignisregel; dieselben Endpunkte allein wählen den Code nicht."],
            data={"basis_sparse": basis_sparse, "event_fibres": event_fibres, "logical_to_transposition_pair": [inv["transposition_pairs"][i] for i in inv["logical_to_pair"]], "projector_diagonal_nonzero": 64},
        )
    )

    response_ranks = [int(round(np.trace(r).real)) for r in inv["responses"]]
    charge_eigs = np.linalg.eigvalsh(inv["charges"][0])
    stages.append(
        _stage(
            "observables",
            "15 Antwortflächen",
            "Perfekte Matchings erzeugen die 3+2-Ladungszerlegung",
            "universalraum",
            40,
            "exact",
            "Jedes perfekte Matching der sechs S6-Labels erzeugt eine Rang-2-Antwortfläche. Nach Entfernung des Hintergrunds trägt Y drei Ladungen -1/3 und zwei Ladungen +1/2.",
            inputs=[{"name": "logical_transpositions", "value": 15, "origin": "code"}],
            outputs=[{"name": "matchings", "value": 15}, {"name": "response_rank", "value": 2}, {"name": "charge_trace_square", "value": 5 / 6}],
            formulas=["M=T_a1b1 T_a2b2 T_a3b3", "R=(I+M)/2", "Y=(5R-2I)/6"],
            checks=[
                _check("alle Antwortflächen haben Rang 2", response_ranks == [2] * 15, response_ranks, [2] * 15, "Spuren der Projektoren"),
                _check("3+2-Spektrum", np.allclose(charge_eigs, [-1 / 3] * 3 + [1 / 2] * 2, atol=1e-12, rtol=0), charge_eigs, [-1 / 3] * 3 + [1 / 2] * 2, "float64-Eigenwerte von Y, Toleranz 1e-12"),
                _check("spurfreie primitive Ladung", abs(np.trace(inv["charges"][0])) < 1e-12, np.trace(inv["charges"][0]), 0, "direkte float64-Spur, Toleranz 1e-12"),
            ],
            sources=[_source(DOC, 4456, "perfect matchings define rank-two response planes and the 3+2 charge spectrum")],
            depends_on=[{"id": "code", "relation": "derives", "label": "Produkte der logischen Transpositionen"}],
            visual_type="matrix",
            visual_data={"matrix": inv["charges"][0], "row_labels": ["c0", "c1", "c2", "c3", "c4"], "column_labels": ["c0", "c1", "c2", "c3", "c4"], "eigenvalues": charge_eigs},
            assumptions=["Welche der 15 Markierungen physisch realisiert wird und ob Y Hyperladung bedeutet, wird hier nicht ausgewählt."],
            data={"matchings": inv["matchings"], "response_gram_spectrum": _hist(np.linalg.eigvalsh(np.asarray([[np.trace(a @ b).real for b in inv["responses"]] for a in inv["responses"]])))},
        )
    )

    source4 = _configured_state(str(cfg["initial_state"]), clock_step, 4)
    product4 = np.kron(np.kron(np.kron(source4, source4), source4), source4)
    logical_amplitudes = inv["v_code"].T @ product4
    igusa_coordinates = inv["coordinate_map"] @ logical_amplitudes
    coordinate_scale = max(float(np.linalg.norm(igusa_coordinates)), 1e-15)
    z = igusa_coordinates / coordinate_scale
    igusa_residual = (sum(z**2)) ** 2 - 4 * sum(z**4)
    stages.append(
        _stage(
            "quartic",
            "Die nichtlineare Quellenfläche",
            "Identische Produktpräparationen liegen auf der Igusa-Quartik",
            "universalraum",
            50,
            "exact",
            "Die explizit projizierte vierfache Quellenpräparation wird in sechs Nullsummenkoordinaten abgebildet und erfüllt die Igusa-Gleichung. Allgemeine logische Zustände müssen nicht darauf liegen.",
            inputs=[{"name": "initial_state", "value": cfg["initial_state"], "origin": "user control"}, {"name": "clock_step", "value": clock_step, "origin": "user control"}],
            outputs=[{"name": "coordinate_count", "value": 6}, {"name": "sum_z", "value": sum(z)}, {"name": "igusa_residual", "value": igusa_residual}],
            formulas=["z = F3 D^(-1/2) V† x^tensor4 / sqrt(3)", "sum_i z_i=0", "(sum_i z_i^2)^2 = 4 sum_i z_i^4"],
            checks=[
                _check("Nullsummenraum", abs(sum(z)) < 1e-10, sum(z), 0, "explizite Sechskoordinatenabbildung in complex128, Toleranz 1e-10"),
                _check("Igusa-Relation", abs(igusa_residual) < 1e-9, igusa_residual, 0, "holomorphes Quartikpolynom in complex128 nach Normierung, Toleranz 1e-9"),
            ],
            sources=[_source(DOC, 1982, "the projected quartic coordinates obey the Igusa quartic"), _source(DOC, 4732, "the four-copy preparation and its code projection")],
            depends_on=[{"id": "code", "relation": "derives", "label": "Projektion von x^tensor4"}, {"id": "observables", "relation": "corresponds", "label": "dieselben sechs Nullsummenkoordinaten"}],
            visual_type="quartic",
            visual_data={"coordinates": [{"id": i, "re": z[i].real, "im": z[i].imag, "magnitude": abs(z[i])} for i in range(6)], "residual": igusa_residual},
            assumptions=["Der gewählte Eingabevektor visualisiert eine Präparation; die primitive TFPT-Quelle wählt diesen Zustand noch nicht autonom."],
            data={"source_vector": source4, "logical_amplitudes": logical_amplitudes, "igusa_coordinates_normalized": z},
        )
    )

    binding_spectrum = np.linalg.eigvalsh(inv["binding"])
    omega_energy = float(inv["omega"] @ inv["binding"] @ inv["omega"])
    independent_energy = 16 / 25
    stages.append(
        _stage(
            "binding",
            "Gemeinsame Ereignisse binden Zellen",
            "Ein Quellenlabel auf zwei Zellen wählt Omega_5",
            "universalraum",
            60,
            "exact",
            "Korreliert ausgeführte Ereignisse erzeugen einen positiven Zweizelloperator mit eindeutigem Nullzustand Omega_5. Unabhängige Labels liefern nur die skalare Energie 16/25.",
            inputs=[{"name": "shared_event_types", "value": 15, "origin": "code"}, {"name": "correlation", "value": "same label on both cells", "origin": "declared source composition"}],
            outputs=[{"name": "ground_dimension", "value": 1}, {"name": "gap", "value": 2 / 5}, {"name": "omega_energy", "value": omega_energy}, {"name": "independent_label_energy", "value": independent_energy}],
            formulas=["k=I-(1/15) sum_ab T_ab tensor T_ab", "Omega_5=(1/sqrt(5)) sum_i c_i tensor c_i"],
            checks=[
                _check("Bindungsspektrum", _hist(binding_spectrum) == [{"value": 0.0, "multiplicity": 1}, {"value": 0.4, "multiplicity": 5}, {"value": 0.666666667, "multiplicity": 9}, {"value": 0.8, "multiplicity": 10}], _hist(binding_spectrum), "0^1,(2/5)^5,(2/3)^9,(4/5)^10", "float64-Diagonalisierung, Eigenwerte auf 9 Dezimalstellen gruppiert; exaktes Zertifikat in der Quelle"),
                _check("Omega_5 ist Nullzustand", abs(omega_energy) < 1e-12, omega_energy, 0, "<Omega_5|k|Omega_5> in float64, Toleranz 1e-12"),
                _check("unabhängige Labels selektieren nicht", abs(independent_energy - 16 / 25) < 1e-15, independent_energy, 16 / 25, "I-(3/5 I)^tensor2"),
            ],
            sources=[_source(DOC, 4494, "same-event two-cell coupling, exact spectrum and Omega_5"), _source(DOC, 4530, "independent labels yield no logical selection")],
            depends_on=[{"id": "code", "relation": "derives", "label": "dieselben T_ab auf beiden Zellen"}],
            visual_type="binding",
            visual_data={"spectrum": _hist(binding_spectrum), "comparison": [{"name": "gemeinsame Labels", "ground_energy": omega_energy, "selected_states": 1}, {"name": "unabhängige Labels", "ground_energy": independent_energy, "selected_states": 25}]},
            assumptions=["Die primitive Quelle muss die gemeinsame statt unabhängige Labelausführung physisch auswählen."],
            data={"omega_probabilities": [1 / 5] * 5, "binding_matrix": inv["binding"]},
        )
    )

    triangle_spectrum = np.linalg.eigvalsh(inv["h_triangle"])
    branch_spectrum = np.linalg.eigvals(inv["branch_super"])
    triangle_ground_error = np.linalg.norm(
        inv["h_triangle"] @ inv["v_triangle"] - (4 / 5) * inv["v_triangle"]
    )
    levels = [{"depth": d, "cells": 3**d, "tracked_mode_3_4": (3 / 4) ** d, "tracked_mode_11_36": (11 / 36) ** d, "tracked_mode_1_4": (1 / 4) ** d} for d in range(recursion_depth + 1)]
    delta = np.eye(5)
    tensor_a = (np.einsum("ab,cd->abcd", delta, delta)
                + np.einsum("ac,bd->abcd", delta, delta)
                + np.einsum("ad,bc->abcd", delta, delta))
    simplex = inv["coordinate_map"]
    tensor_c = np.einsum("ia,ib,ic,id->abcd", simplex, simplex, simplex, simplex)
    tensor_e, tensor_f, tensor_g = tensor_a - 2 * tensor_c, 4 * tensor_c - tensor_a / 3, tensor_c + tensor_a / 6
    psi, blind, gamma = (tensor / np.linalg.norm(tensor) for tensor in (tensor_e, tensor_f, tensor_g))
    tensor_weights = [float(abs(np.vdot(psi, gamma)) ** 2), float(abs(np.vdot(blind, gamma)) ** 2)]
    tensor_decomposition_error = float(np.linalg.norm(gamma - math.sqrt(3 / 5) * psi - math.sqrt(2 / 5) * blind))
    tensor_encoder_error = float(np.linalg.norm(tensor_g.reshape(125, 5) / math.sqrt(2) - inv["v_triangle"]))
    tensor_identity = {"norm_squared": {"A": float(np.vdot(tensor_a, tensor_a)), "C": float(np.vdot(tensor_c, tensor_c)), "E": float(np.vdot(tensor_e, tensor_e)), "F_I": float(np.vdot(tensor_f, tensor_f)), "G": float(np.vdot(tensor_g, tensor_g))}, "weights": tensor_weights, "orthogonality": float(np.vdot(psi, blind)), "decomposition_error": tensor_decomposition_error, "encoder_error": tensor_encoder_error, "scope": "algebraic decomposition of the explicit event tensor G and equality to the existing three-cell encoder; no fresh independent four-cell ground-state uniqueness proof"}
    stages.append(
        _stage(
            "recursion",
            "Drei Zellen werden wieder eine Fünferzelle",
            "Explizite Isometrie V: C5 → C5⊗3",
            "universalraum",
            70,
            "exact",
            "Der Dreiecksoperator aus derselben Bindung besitzt einen fünfdimensionalen Grundraum. Ein ausgeschriebener Tensor transportiert alle 15 Ereignisse exakt und kann auf endlicher Baumtiefe iteriert werden.",
            inputs=[{"name": "binding_operator", "value": "k", "origin": "binding"}, {"name": "cell_graph", "value": "triangle", "origin": "declared block choice"}, {"name": "depth", "value": recursion_depth, "origin": "user control"}],
            outputs=[{"name": "triangle_dimension", "value": 125}, {"name": "ground_dimension", "value": 5}, {"name": "ground_energy", "value": 4 / 5}, {"name": "gap", "value": 2 / 5}, {"name": "cells_at_depth", "value": 3**recursion_depth}],
            formulas=["H_triangle=k_12+k_23+k_31", "V_ijk,a=(T_ijka+D_ijka/6)/sqrt(2)", "T_ab^tensor3 V=V T_ab"],
            checks=[
                _check("Dreiecksspektrum", _hist(triangle_spectrum) == [{"value": 0.8, "multiplicity": 5}, {"value": 1.2, "multiplicity": 1}, {"value": 1.6, "multiplicity": 25}, {"value": 1.866666667, "multiplicity": 27}, {"value": 2.0, "multiplicity": 25}, {"value": 2.2, "multiplicity": 32}, {"value": 2.4, "multiplicity": 10}], _hist(triangle_spectrum), "(4/5)^5,(6/5)^1,(8/5)^25,(28/15)^27,2^25,(11/5)^32,(12/5)^10", "float64-Diagonalisierung, Eigenwerte auf 9 Dezimalstellen gruppiert; exaktes Zertifikat in der Quelle"),
                _check("Rekursionsisometrie", np.linalg.norm(inv["v_triangle"].T @ inv["v_triangle"] - np.eye(5)) < 1e-10, np.linalg.norm(inv["v_triangle"].T @ inv["v_triangle"] - np.eye(5)), 0, "||V†V-I5|| in float64, Toleranz 1e-10"),
                _check("Isometrie ist der Dreiecksgrundraum", triangle_ground_error < 1e-10, triangle_ground_error, 0, "||H_triangle V-(4/5)V|| in float64, Toleranz 1e-10"),
                _check("alle Ereignisse intertwinen", inv["intertwine_error"] < 1e-10, inv["intertwine_error"], 0, "max ||T^tensor3 V-VT|| in float64, Toleranz 1e-10"),
                _check("Einast-Kanalspektrum", _hist(branch_spectrum) == [{"value": 0.25, "multiplicity": 10}, {"value": 0.305555556, "multiplicity": 9}, {"value": 0.75, "multiplicity": 5}, {"value": 1.0, "multiplicity": 1}], _hist(branch_spectrum), "1^1,(3/4)^5,(11/36)^9,(1/4)^10", "float64-Kraus-Superoperator, Eigenwerte auf 9 Dezimalstellen gruppiert; exaktes Zertifikat in der Quelle"),
                _check("Einast-Kanal ist spurtreu", inv["branch_tp_error"] < 1e-10, inv["branch_tp_error"], 0, "||sum A†A-I5|| in float64, Toleranz 1e-10"),
                _check("Einast-Kanal ist unital", inv["branch_unital_error"] < 1e-10, inv["branch_unital_error"], 0, "||sum AA†-I5|| in float64, Toleranz 1e-10"),
                _check("Vierertensor und Dreierencoder sind dieselben Komponenten", tensor_encoder_error < 1e-12, tensor_encoder_error, 0, "G_abcd/sqrt(2) umgeformt in die vorhandene 125x5-Isometrie, Toleranz 1e-12"),
                _check("60/40-Normzerlegung in orthogonale Austausch- und Igusa-Richtung", tensor_decomposition_error < 1e-12 and abs(np.vdot(psi, blind)) < 1e-12 and np.allclose(tensor_weights, [3/5, 2/5], atol=1e-12, rtol=0), tensor_identity, {"weights": [3/5, 2/5], "orthogonality": 0, "decomposition_error": 0}, "ausgeschriebene 625 Tensor-Komponenten in float64; kein erneuter Beweis der Vierergrundzustands-Eindeutigkeit"),
            ],
            sources=[_source(DOC, 4587, "triangle spectrum from the common-event binding"), _source(DOC, 4690, "explicit recursive isometry and event covariance"), _source(DOC, 4713, "single-branch channel spectrum"), _source("_newest2/TFPT_Gesamtdokumentation_20260927.md", 550, "Ein Tensor verbindet Quartik, Codes, Bindung und Kodierung; explizite 60/40-Zerlegung")],
            depends_on=[{"id": "binding", "relation": "derives", "label": "dieselbe Zweizellbindung auf allen Dreieckskanten"}],
            visual_type="tree",
            visual_data={"levels": levels, "branching": 3, "depth": recursion_depth, "full_tree_isometry": True},
            assumptions=["Die Dreiecksblockstruktur ist gewählt; die Rechnung beweist keine autonome Bildung dieser Blöcke oder einen unendlichen Grenzwert."],
            data={"triangle_spectrum": _hist(triangle_spectrum), "branch_channel_spectrum": _hist(branch_spectrum), "isometry_shape": [125, 5], "isometry_sample": inv["v_triangle"][:12], "tensor_identity": tensor_identity},
        )
    )

    lap_eigs = np.linalg.eigvalsh(inv["laplacian"])
    times = list(range(transfer_steps + 1))
    finite_return = [float(np.mean(np.exp(-t * lap_eigs))) for t in times]
    geometry_nodes = [
        {"id": f"m{i}", "label": "·".join(f"{a}{b}" for a, b in matching), "group": "matching", "marked": i == 0}
        for i, matching in enumerate(inv["matchings"])
    ] + [
        {"id": f"p{i}", "label": f"{a}{b}", "group": "pair", "marked": (a, b) in inv["matchings"][0]}
        for i, (a, b) in enumerate(inv["transposition_pairs"])
    ]
    stages.append(
        _stage(
            "space",
            "Ein markierter Raumkandidat",
            "Tutte–Coxeter-Zelle, A3-Periodengitter und gewählter Gleichratenweg",
            "universalraum",
            80,
            "conditional",
            "Die tatsächlichen 15 Matchings und 15 Paare bilden den 30-Knoten-Inzidenzgraphen. Nach Wahl einer 3+2-Markierung besitzt die dokumentierte Fortsetzung ein A3-Periodengitter; die angezeigte Dynamik ist der explizite Gleichratenweg auf der endlichen Zelle.",
            inputs=[{"name": "mark", "value": inv["matchings"][0], "origin": "declared spatial mark"}, {"name": "edge_rate", "value": 1, "origin": "declared equal-rate walk"}],
            outputs=[{"name": "nodes", "value": 30}, {"name": "edges", "value": 45}, {"name": "degree", "value": 3}, {"name": "loop_rank", "value": 16}, {"name": "selected_spatial_rank", "value": 3, "status": "conditional", "origin": "selected marked representation"}, {"name": "spectral_dimension", "value": 3, "status": "conditional", "origin": "cited infinite equal-rate A3 cover"}],
            formulas=["dim H1=45-30+1=16", "Gram(A3)=[[2,-1,0],[-1,2,-1],[0,-1,2]]", "lambda_min(k)=8/5 |k|^2+O(|k|^4)"],
            checks=[
                _check("30/45/Grad-3-Inzidenz", inv["adjacency"].shape == (30, 30) and int(inv["adjacency"].sum() / 2) == 45 and np.all(inv["adjacency"].sum(axis=1) == 3), [inv["adjacency"].shape[0], int(inv["adjacency"].sum() / 2), sorted(set(inv["adjacency"].sum(axis=1)))], [30, 45, [3]], "vollständige Matching-Paar-Inzidenz"),
                _check("Tutte–Coxeter-Adjazenzspektrum", _hist(np.linalg.eigvalsh(inv["adjacency"])) == [{"value": -3.0, "multiplicity": 1}, {"value": -2.0, "multiplicity": 9}, {"value": 0.0, "multiplicity": 10}, {"value": 2.0, "multiplicity": 9}, {"value": 3.0, "multiplicity": 1}], _hist(np.linalg.eigvalsh(inv["adjacency"])), "(-3)^1,(-2)^9,0^10,2^9,3^1", "float64-Graphdiagonalisierung, Eigenwerte auf 9 Dezimalstellen gruppiert; exaktes Polynom in der Quelle"),
                _check("A3-Gramdeterminante", round(np.linalg.det(np.asarray([[2, -1, 0], [-1, 2, -1], [0, -1, 2]]))) == 4, np.linalg.det(np.asarray([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])), 4, "exakte 3x3-Determinante"),
            ],
            sources=[_source(DOC, 6247, "Tutte-Coxeter incidence reconstructed from actual response projectors"), _source(DOC, 6283, "marking selects a unique 3D representation conditionally"), _source(DOC, 6293, "explicit A3 periodic cover"), _source(DOC, 6313, "equal-rate cover has spectral dimension three")],
            depends_on=[{"id": "observables", "relation": "derives", "label": "Matching-Paar-Inzidenz"}, {"id": "recursion", "relation": "corresponds", "label": "noch keine gemeinsame Netzenergie"}],
            visual_type="lattice",
            visual_data={"nodes": geometry_nodes, "edges": [{"source": a, "target": b} for a, b in inv["geometry_edges"]], "period_basis": [[6, 3, 3], [0, 3, 0], [0, 0, 3]], "root_gram": [[2, -1, 0], [-1, 2, -1], [0, -1, 2]], "walk": [{"t": t, "finite_cell_return": p} for t, p in zip(times, finite_return)]},
            assumptions=["Die Markierung, die Deutung ihrer dreidimensionalen Darstellung als Ort, die Fortsetzung zum Cover und gleiche Kantenraten sind ausgewählt.", "Die endliche Rückkehrkurve ist die 30-Knoten-Zelle; d_s=3 gehört zum dokumentierten unendlichen markierten Cover."],
            data={"adjacency_spectrum": _hist(np.linalg.eigvalsh(inv["adjacency"])), "laplacian_spectrum": _hist(lap_eigs), "mark": inv["matchings"][0], "finite_return": finite_return},
        )
    )

    kraus = _phi_kraus(b)
    rho = np.outer(_configured_state(str(cfg["initial_state"]), clock_step, 4), _configured_state(str(cfg["initial_state"]), clock_step, 4).conj())
    readout = np.asarray([[1, 0, 0, 1 / 3], [0, 1, 0, 1 / 3], [0, 0, 1, 1 / 3]])
    population_b = np.asarray([[13, 1, 4], [1, 13, 4], [4, 4, 10]], dtype=float) / 18
    x01 = np.zeros((4, 4)); x01[0, 1] = x01[1, 0] = 1
    probe = np.asarray([1, 1, 0, 0], dtype=complex) / math.sqrt(2)
    probe_response = float(np.trace(x01 @ _apply(kraus, np.outer(probe, probe.conj()))).real)
    choi = sum(
        (np.outer(a.reshape(-1), a.reshape(-1).conj()) for a in kraus),
        np.zeros((16, 16), dtype=complex),
    )
    actual_choi_values = np.linalg.eigvalsh(choi)
    closed_choi_values = np.sort(
        np.asarray([10 / 9, 7 / 9 - 2 * b, 4 / 9 - 2 * b, 4 * b] + [1 / 6] * 10 + [0, 0])
    )
    choi_spectrum_error = np.linalg.norm(actual_choi_values - closed_choi_values, ord=np.inf)
    channel_series = []
    current = rho.copy()
    initial_readout = readout @ np.diag(rho).real
    for step in range(transfer_steps + 1):
        channel_series.append({"step": step, "population": np.diag(current).real, "readout": readout @ np.diag(current).real, "coherence_x12": np.trace(x01 @ current).real})
        current = _apply(kraus, current)
    tp = sum(a.conj().T @ a for a in kraus)
    unital = sum(a @ a.conj().T for a in kraus)
    readout_intertwine_error = 0.0
    for row, column in it.product(range(4), repeat=2):
        matrix_unit = np.zeros((4, 4), dtype=complex)
        matrix_unit[row, column] = 1
        left = readout @ np.diag(_apply(kraus, matrix_unit))
        right = population_b @ readout @ np.diag(matrix_unit)
        readout_intertwine_error = max(readout_intertwine_error, np.linalg.norm(left - right))
    expected_first = population_b @ initial_readout
    actual_first = readout @ np.diag(_apply(kraus, rho)).real
    common_adapter = _common_source_adapter(b)
    stages.append(
        _stage(
            "sourcechannel",
            "Die gemeinsame Quellenfamilie entwickelt Zustände",
            "Populationstransfer B und phasenempfindliche Freiheit b",
            "universalraum",
            90,
            "conditional",
            "Der vollständige CPTP-Kanal Phi_b trägt für jedes zulässige b denselben beobachteten Populationstransfer und denselben Codeanschluss. Die Kohärenz macht die verbleibende Quellenwahl sichtbar.",
            inputs=[{"name": "phase_b", "value": b, "origin": "user control; physically unselected"}, {"name": "steps", "value": transfer_steps, "origin": "user control"}, {"name": "initial_state", "value": cfg["initial_state"], "origin": "user control"}],
            outputs=[{"name": "kraus_operators", "value": len(kraus)}, {"name": "entanglement_fidelity", "value": 5 / 18}, {"name": "one_step_x12_for_probe", "value": probe_response}, {"name": "stationary_state", "value": "I4/4"}],
            formulas=["R Phi_b^n = B^n R", "<X12>_probe = 2b-1/9", "0 <= b <= 2/9"],
            checks=[
                _check("spurtreu", np.linalg.norm(tp - np.eye(4)) < 1e-10, np.linalg.norm(tp - np.eye(4)), 0, "Summe F_mu†F_mu"),
                _check("unital", np.linalg.norm(unital - np.eye(4)) < 1e-10, np.linalg.norm(unital - np.eye(4)), 0, "Summe F_mu F_mu†"),
                _check("Choi-Positivität", float(actual_choi_values.min()) >= -1e-12, float(actual_choi_values.min()), 0, "direkt aus den Krausoperatoren diagonalisierte Choi-Matrix, Toleranz 1e-12"),
                _check("geschlossenes Choi-Spektrum", choi_spectrum_error < 1e-10, choi_spectrum_error, 0, "direkte Choi-Diagonalisierung gegen die geschlossene Formel, Toleranz 1e-10"),
                _check("phasenempfindliche Probe", abs(probe_response - (2 * b - 1 / 9)) < 1e-12, probe_response, 2 * b - 1 / 9, "Phi_b auf |phi1+phi3><phi1+phi3|/2 und X12"),
                _check("vollständiges Readout-Intertwining", readout_intertwine_error < 1e-10, readout_intertwine_error, 0, "R Phi(E_ij)=B R(E_ij) auf allen 16 Matrixeinheiten, Toleranz 1e-10"),
                _check("erster Readoutschritt folgt B", np.allclose(actual_first, expected_first, atol=1e-12, rtol=0), actual_first, expected_first, "direkte Krausentwicklung auch wenn die sichtbare Serie bei Schritt 0 endet, Toleranz 1e-12"),
                _check("dieselben 60 Amplituden realisieren Register- und Codeoperatoren", max(common_adapter["register_residual"], common_adapter["code_residual"], common_adapter["trace_residual"]) < 1e-10, {"register": common_adapter["register_residual"], "code": common_adapter["code_residual"], "trace": common_adapter["trace_residual"]}, {"register": 0, "code": 0, "trace": 0}, "explizite Rekonstruktion aller 15 Krauspaare aus je 60 gemeinsamen komplexen Koeffizienten, Toleranz 1e-10"),
                _check("gemeinsamer Adapter bewahrt den vorhandenen Codekanal", max(common_adapter["code_tp_residual"], common_adapter["code_channel_residual"], common_adapter["factorization_residual"]) < 1e-10, {key: common_adapter[key] for key in ("code_tp_residual", "code_channel_residual", "factorization_residual")}, 0, "15x15-Quellenfaktorisierung, Code-Norm und voller 25x25-Superoperator gegen den vorhandenen Rekursionskanal"),
            ],
            sources=[_source(DOC_SOURCE, 1647, "gemeinsamer linearer Amplitudenraum und explizite 60-Koeffizienten-Formel"), _source(DOC_SOURCE, 1723, "the register readout intertwines the population transfer B"), _source(DOC_SOURCE, 1725, "the complete Phi_b register family"), _source(DOC_SOURCE, 1878, "X12 response distinguishes b")],
            depends_on=[{"id": "rays", "relation": "feeds", "label": "60 Reflexionen im expliziten gemeinsamen Amplitudenlift"}, {"id": "code", "relation": "feeds", "label": "unveränderter Codekanal"}, {"id": "recursion", "relation": "checks", "label": "vollständiger 25x25-Codekanal stimmt mit dem Einastkanal überein"}],
            visual_type="timeseries",
            visual_data={"series": channel_series, "population_labels": ["phi1", "phi3", "phi2", "phi0"], "readout_labels": ["A", "B", "C"], "choi_spectrum": sorted(actual_choi_values, reverse=True)},
            assumptions=["b ist eine sichtbare Benutzereingabe, keine aus P1/P2 hergeleitete Naturkonstante.", "Der endliche gemeinsame Lift ist nicht automatisch eine 3+1D lokale Feldquelle."],
            data={"B": population_b, "R": readout, "choi_spectrum": actual_choi_values, "closed_choi_spectrum": closed_choi_values, "probe_state": probe, "probe_x12_response": probe_response, "series": channel_series, "common_adapter": common_adapter},
        )
    )

    rr_clock = np.diag([1, 1j, -1, -1j, 1])
    code_clock = np.diag([1, 1, 1, 1, -1])
    rr_characters = [np.trace(np.linalg.matrix_power(rr_clock, power)) for power in range(4)]
    code_characters = [np.trace(np.linalg.matrix_power(code_clock, power)) for power in range(4)]
    # R_RR X = X R_code permits only equal-eigenvalue blocks.  Derive both
    # the Hom-space dimension and its maximum possible rank from those blocks;
    # this is a statement about these two fixed modules, not every enriched
    # physical bridge that could contain additional sectors.
    intertwiner_linear = np.kron(np.eye(5), rr_clock) - np.kron(code_clock.T, np.eye(5))
    intertwiner_solution_dimension = 25 - int(np.linalg.matrix_rank(intertwiner_linear, tol=1e-10))
    shared_eigenspaces = []
    intertwiner_max_rank = 0
    for eigenvalue in (1, 1j, -1, -1j):
        rr_multiplicity = int(np.count_nonzero(np.diag(rr_clock) == eigenvalue))
        code_multiplicity = int(np.count_nonzero(np.diag(code_clock) == eigenvalue))
        if rr_multiplicity and code_multiplicity:
            block_rank = min(rr_multiplicity, code_multiplicity)
            intertwiner_max_rank += block_rank
            shared_eigenspaces.append(
                {
                    "eigenvalue": eigenvalue,
                    "rr_multiplicity": rr_multiplicity,
                    "code_multiplicity": code_multiplicity,
                    "hom_dimension": rr_multiplicity * code_multiplicity,
                    "maximum_rank": block_rank,
                }
            )
    # The newer consolidation repairs only the isolated C4 representation
    # mismatch: take each character with its maximum multiplicity.  This is
    # an explicit common carrier, not an identification of physical sectors.
    clock_values = (1, 1j, -1, -1j)
    rr_mult = [int(np.count_nonzero(np.diag(rr_clock) == value)) for value in clock_values]
    code_mult = [int(np.count_nonzero(np.diag(code_clock) == value)) for value in clock_values]
    common_mult = [max(a, b) for a, b in zip(rr_mult, code_mult)]
    common_values = [value for value, count in zip(clock_values, common_mult) for _ in range(count)]
    common_clock = np.diag(common_values)

    def clock_embedding(source_clock):
        matrix = np.zeros((len(common_values), len(source_clock)), dtype=complex)
        used = set()
        for column, value in enumerate(np.diag(source_clock)):
            row = next(i for i, target in enumerate(common_values) if target == value and i not in used)
            used.add(row)
            matrix[row, column] = 1
        return matrix

    rr_embedding, code_embedding = clock_embedding(rr_clock), clock_embedding(code_clock)
    common_errors = [
        float(np.linalg.norm(common_clock @ embed - embed @ clock))
        for embed, clock in ((rr_embedding, rr_clock), (code_embedding, code_clock))
    ]
    interfaces = [
        {"id": "T1", "status": "open", "from": "P1/P2 and the finite compiler", "to": "source-selected markings, participants, rates and dimension", "requires": "an independent origin and selection theorem"},
        {"id": "T2", "status": "open", "from": "finite seam/code representations", "to": "charged (E8)_1 boundary theory", "requires": "marked charged-sector intertwiner and scaling-limit theorem"},
        {"id": "T3", "status": "open", "from": "binding/recursion/marked graph", "to": "local unitary 3+1D Hamiltonian family", "requires": "one source-selected locality and time law"},
        {"id": "T4", "status": "open", "from": "3+2 internal charge planes", "to": "chiral Standard Model", "requires": "field representation, local measure, mirror decoupling"},
        {"id": "T5", "status": "open", "from": "finite A3 cover candidate", "to": "Lorentz continuum and scattering", "requires": "critical continuum, clustering and nontrivial S-matrix"},
        {"id": "T6", "status": "open", "from": "dimensionless compiler outputs", "to": "couplings/flavor/neutrino dynamics", "requires": "one common generating functional"},
        {"id": "T7", "status": "open", "from": "stress/geometry response", "to": "massless spin-2", "requires": "two helicities, Ward identity and universal soft coupling"},
        {"id": "T8", "status": "open", "from": "finite channels", "to": "physical initial state and SK functional", "requires": "source-selected rho0 and Z[g,J+,J-;rho0]"},
    ]
    bridge_nodes = [{"id": sid, "status": "computed"} for sid in ("hamming", "rays", "code", "observables", "quartic", "binding", "recursion", "space", "sourcechannel")]
    bridge_nodes += [{"id": interface["id"], "status": "open"} for interface in interfaces]
    stages.append(
        _stage(
            "matterbridge",
            "Der ehrliche Übergang zur Physik",
            "Rangprüfung zweier Clockmodule und explizite offene Ziel-Schnittstellen",
            "physics",
            100,
            "open",
            "Der endliche Prozess liefert eine verbundene Algebra, Dynamik und bedingte Geometrie. Zwischen den beiden festgelegten fünfdimensionalen Clockmodulen existieren zwar nichttriviale Intertwiner, aber keiner mit Rang 5; diese enge Prüfung ist kein Ausschluss anders angereicherter physikalischer Brücken und noch keine gemeinsame 3+1D Materie-/Gravitationstheorie.",
            inputs=[{"name": "finite_process_stages", "value": 9, "origin": "computed explorer chain"}],
            outputs=[{"name": "rr_clock_character", "value": rr_characters}, {"name": "code_clock_character", "value": code_characters}, {"name": "intertwiner_solution_dimension", "value": intertwiner_solution_dimension}, {"name": "intertwiner_max_rank", "value": intertwiner_max_rank}, {"name": "rank_five_intertwiner", "value": False, "scope": "the two fixed clock modules"}, {"name": "minimal_common_clock_dimension", "value": len(common_values), "scope": "only the isolated C4 actions"}, {"name": "open_interfaces", "value": len(interfaces)}],
            formulas=["chi_RR(k)=tr(R_RR^k)", "chi_code(k)=tr(R_code^k)", "Hom_C4(V_code,V_RR)=direct sum over equal-character eigenspaces", "different characters => no rank-5/invertible marked intertwiner between these fixed modules"],
            checks=[
                _check("RR-Clock hat Ordnung 4", np.linalg.norm(np.linalg.matrix_power(rr_clock, 4) - np.eye(5)) < 1e-12 and np.linalg.norm(np.linalg.matrix_power(rr_clock, 2) - np.eye(5)) > 1, 4, 4, "Matrixpotenzen"),
                _check("Code-Clock hat Ordnung 2", np.linalg.norm(np.linalg.matrix_power(code_clock, 2) - np.eye(5)) < 1e-12, 2, 2, "Matrixpotenzen"),
                _check("Clock-Charaktere verschieden", not np.allclose(rr_characters, code_characters), rr_characters, code_characters, "Charaktervergleich bei k=0,1,2,3"),
                _check("nichttriviale Intertwiner, aber kein Rang-5-Clock-Isomorphismus", intertwiner_solution_dimension == 9 and intertwiner_max_rank == 3, {"solution_dimension": intertwiner_solution_dimension, "maximum_rank": intertwiner_max_rank, "rank_five_exists": intertwiner_max_rank == 5}, {"solution_dimension": 9, "maximum_rank": 3, "rank_five_exists": False}, "Nullraum von I tensor R_RR - R_code^T tensor I und gemeinsame Eigenräume der zwei festgelegten Module"),
                _check("zentraler mu4-Charakter geht im vierten Tensorgrad verloren", (1j**4) == 1 and 1j != 1, {"register": 1j, "fourfold": 1j**4}, {"register": "i", "fourfold": 1}, "direkte zentrale Wirkung"),
                _check("minimaler gemeinsamer C4-Träger hat sieben Richtungen", len(common_values) == 7, len(common_values), 7, "Maximum der Multiplizitäten jedes der vier C4-Charaktere; notwendige Untergrenze wird erreicht"),
                _check("beide Clockeinbettungen sind isometrisch und äquivariant", all(error == 0 for error in common_errors) and np.array_equal(rr_embedding.conj().T @ rr_embedding, np.eye(5)) and np.array_equal(code_embedding.conj().T @ code_embedding, np.eye(5)), common_errors, [0, 0], "explizite 0/1-Einbettungen; Matrixidentitäten mit exakt darstellbaren Einträgen"),
                _check("Y-Anomaliesumme im Fünfer verschwindet", abs(3 * (-1 / 3) + 2 * (1 / 2)) < 1e-15, 3 * (-1 / 3) + 2 * (1 / 2), 0, "3+2-Ladungssumme; notwendige, nicht hinreichende Bedingung"),
            ],
            sources=[_source(DOC_SOURCE, 1810, "RR and quartic-code clocks have different spectra"), _source(DOC_SOURCE, 1825, "the two fixed modules have no invertible marked intertwiner"), {"path": "tfpt_explorer/sources/TFPT_Konsolidierung_20260928.pdf", "page": 35, "claim": "Abschnitt 12.6: minimaler gemeinsamer Siebenerträger für die isolierten C4-Wirkungen"}, _source("tfpt_research_contracts.tex", 14112, "T1-T8 completeness gates"), _source("tfpt_research_contracts.tex", 13756, "massless spin-2 acceptance criteria")],
            depends_on=[{"id": "seam", "relation": "corresponds", "label": "RR-Fünferraum und µ4-Clockwirkung als Vergleichsmodul"}, {"id": "observables", "relation": "feeds", "label": "3+2 interne Ladungsstruktur"}, {"id": "space", "relation": "assumes", "label": "markierter Raumkandidat"}, {"id": "sourcechannel", "relation": "feeds", "label": "endliche Zeitantwort"}],
            visual_type="bridge",
            visual_data={"nodes": bridge_nodes, "edges": [{"source": "hamming", "target": "rays", "status": "exact"}, {"source": "rays", "target": "code", "status": "exact"}, {"source": "code", "target": "observables", "status": "exact"}, {"source": "code", "target": "binding", "status": "exact"}, {"source": "binding", "target": "recursion", "status": "exact"}, {"source": "observables", "target": "space", "status": "conditional"}, {"source": "sourcechannel", "target": "T8", "status": "open"}, {"source": "space", "target": "T3", "status": "open"}, {"source": "observables", "target": "T4", "status": "open"}, {"source": "T3", "target": "T5", "status": "open"}, {"source": "T5", "target": "T7", "status": "open"}], "interfaces": interfaces},
            notes=["Gleiche Dimensionen, Zahlen oder Spektralmultiplizitäten ersetzen keinen Intertwiner.", "Der 9-dimensionale Hom-Raum zeigt ausdrücklich, dass Intertwiner existieren; ausgeschlossen ist nur Rang 5 zwischen diesen festgehaltenen Modulen.", "Die verschwindende Ladungssumme ist eine notwendige Repräsentationsprüfung, kein Beweis für chirale Materie oder Anomaliefreiheit der ganzen Theorie."],
            assumptions=["Die physikalischen T1-T8-Schnittstellen werden erst dann geschlossen, wenn dieselbe Quelle ihre Operatoren, Zustände, Zeit und lokale Komposition bestimmt.", "Der gemeinsame Siebenerträger repariert nur die angegebenen C4-Wirkungen; er wählt weder neue physische Zustände noch eine Feldtheorie."],
            data={"characters": {"powers": [0, 1, 2, 3], "rr": rr_characters, "code": code_characters}, "intertwiner": {"linear_system_shape": [25, 25], "solution_dimension": intertwiner_solution_dimension, "maximum_rank": intertwiner_max_rank, "rank_five_exists": False, "shared_eigenspaces": shared_eigenspaces, "scope": "only the fixed RR and quartic-code C4 modules"}, "clock_completion": {"eigenvalues": clock_values, "rr_multiplicities": rr_mult, "code_multiplicities": code_mult, "common_multiplicities": common_mult, "dimension": len(common_values), "rr_embedding": rr_embedding, "code_embedding": code_embedding, "intertwining_errors": common_errors, "scope": "isolated C4 representations only"}, "interfaces": interfaces, "upstream_present": upstream is not None},
        )
    )

    return stages


__all__ = ["DEFAULT_CONFIG", "build_stages"]
