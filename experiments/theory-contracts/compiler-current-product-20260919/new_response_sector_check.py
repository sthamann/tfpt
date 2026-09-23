"""Bounded exact audit of two solvable sectors of the existing .19/.20 chain.

No Hamiltonian is added.  The script reconstructs the original sixty native
reflections, their phase-free action on 240 oriented roots, the uniform-source
restriction, and the coordinate-subrepresentation pair state.  It also pins
the already certified bracket-compatible current-lift obstruction.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"
OBSTRUCTION = REPO / "experiments/theory-contracts/compiler-root-phase-lift-20260919/origin_obstruction_certificate.json"
OBSTRUCTION_SHA256 = "9b2404cf3500a8225782c34c298e167f82ac01fbb1bef41b39542b9793e5bd43"

checks: Counter[str] = Counter()


def require(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    require(
        np.array_equal(vector.real, np.rint(vector.real))
        and np.array_equal(vector.imag, np.rint(vector.imag)),
        "Gaussian coordinates remain integral",
    )
    return tuple((int(round(z.real)), int(round(z.imag))) for z in vector)


def permutation_apply_rows(permutation: tuple[int, ...], matrix: np.ndarray) -> np.ndarray:
    out = np.zeros_like(matrix)
    for source, target in enumerate(permutation):
        out[target] = matrix[source]
    return out


def path_laplacian(size: int) -> sp.Matrix:
    matrix = sp.zeros(size)
    for site in range(size - 1):
        matrix[site, site] += 1
        matrix[site + 1, site + 1] += 1
        matrix[site, site + 1] -= 1
        matrix[site + 1, site] -= 1
    return matrix


def main() -> None:
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "pinned original sixty-ray source")
    require(hashlib.sha256(OBSTRUCTION.read_bytes()).hexdigest() == OBSTRUCTION_SHA256,
            "pinned current-lift obstruction")
    spec = importlib.util.spec_from_file_location("new_response_native", SOURCE)
    source = importlib.util.module_from_spec(spec)
    require(spec.loader is not None, "native source module has loader")
    spec.loader.exec_module(source)

    rays = source.source_rays()
    roots = np.stack([(1j ** phase) * ray for ray in rays for phase in range(4)])
    root_index = {key(root): index for index, root in enumerate(roots)}
    require(len(rays) == 60 and len(root_index) == 240,
            "sixty rays and 240 oriented roots")
    psi = roots / 2
    require(np.array_equal(psi.conj().T @ psi, 60 * np.eye(4)),
            "oriented-root first moment is 60I")
    require(not np.any(psi.sum(axis=0)),
            "coordinate source subspace is orthogonal to uniform source")

    identity4 = np.eye(4, dtype=np.complex128)
    identity16 = np.eye(16, dtype=np.complex128)
    swap = np.zeros((16, 16), dtype=np.complex128)
    for i in range(4):
        for j in range(4):
            swap[4 * j + i, 4 * i + j] = 1

    reflections: list[np.ndarray] = []
    permutations: list[tuple[int, ...]] = []
    sum_r2 = np.zeros((4, 4), dtype=np.complex128)
    sum_r2r2 = np.zeros((16, 16), dtype=np.complex128)
    uniform = np.ones(240, dtype=np.int64)

    for ray in rays:
        reflection = identity4 - np.outer(ray, ray.conj()) / 2
        require(np.array_equal(reflection @ reflection, identity4),
                "native matter reflection is involutive")
        permutation = tuple(
            root_index[key(reflection @ root)] for root in roots
        )
        require(len(set(permutation)) == 240,
                "native event permutes all oriented roots")
        require(np.array_equal(uniform[list(permutation)], uniform),
                "phase-free event fixes uniform source")

        # K_{alpha i}=psi_alpha^i embeds the conjugate fundamental in C^240.
        # With P|alpha>=|r alpha>, one has P K = K r^T.  Hence the coefficient
        # matrix K of sum_alpha |alpha>|psi_alpha> obeys P K r^T=K.
        transformed = permutation_apply_rows(permutation, psi)
        require(np.array_equal(transformed, psi @ reflection.T),
                "coordinate source intertwines as conjugate fundamental")
        require(np.array_equal(transformed @ reflection.T, psi),
                "source-coordinate times one-register pair is event invariant")

        reflections.append(reflection)
        permutations.append(permutation)
        reflection2 = 2 * reflection
        require(np.array_equal(reflection2.real, np.rint(reflection2.real))
                and np.array_equal(reflection2.imag, np.rint(reflection2.imag)),
                "twice each reflection is Gaussian integral")
        sum_r2 += reflection2
        sum_r2r2 += np.kron(reflection2, reflection2)

    require(np.array_equal(sum_r2, 60 * identity4),
            "native first reflection moment is I/2")
    require(np.array_equal(sum_r2r2, 48 * (identity16 + swap)),
            "native second reflection moment is (I+Swap)/5")
    mean_r = sum_r2 / 120
    mean_rr = sum_r2r2 / 240
    require(np.array_equal(240 * identity16 - sum_r2r2,
                           48 * (4 * identity16 - swap)),
            "uniform-source edge is (4I-Swap)/5")

    # Open-chain one-colour sector.  After subtracting the all-equal reference,
    # sum_e(4I-S_e)/5 becomes one fifth of the path graph Laplacian.
    x = sp.symbols("x")
    charpolys: dict[str, str] = {}
    for size in range(2, 11):
        lap = path_laplacian(size)
        expected = sp.expand((-1) ** (size - 1) * x
                             * sp.chebyshevu(size - 1, 1 - x / 2))
        actual = sp.expand(lap.charpoly(x).as_expr())
        require(actual == expected,
                "open one-colour branch has exact Neumann cosine spectrum")
        require(lap * sp.ones(size, 1) == sp.zeros(size, 1),
                "q=0 colour wave stays at reference energy")
        charpolys[str(size)] = str(actual)

    # The global product of m copies of Pair_e and an arbitrary terminal C4
    # vector is an exact eigenstate.  On Pair_e every individual P_r x r is
    # identity; the remaining averaged r on matter e+1 is I/2.  Thus every
    # edge L_e=I-average(P_r x r x r) has eigenvalue 1/2, even when the next
    # matter register is entangled with source e+1.
    require(np.array_equal(identity4 - mean_r, identity4 / 2),
            "each edge has eigenvalue one half on the chained pair state")

    obstruction = json.loads(OBSTRUCTION.read_text())
    require(obstruction["verdict"] ==
            "EXACT_OBSTRUCTIONS_UNDER_NAMED_CURRENT_LIFT_REQUIREMENT",
            "current-lift obstruction verdict retained")
    require(obstruction["root_orbit"] == 240,
            "current-lift obstruction uses same 240-root orbit")
    require(obstruction["alpha"] == [1, 1, 1, 1]
            and obstruction["beta"] == [1, -1, -1, -1]
            and obstruction["gamma"] == [2, 0, 0, 0],
            "minimal swapped-pair fixed-sum witness retained")
    require("fixed gamma requires1" in obstruction["contradiction"]
            and "bracket requires -1" in obstruction["contradiction"],
            "bracket phase contradiction retained")

    result = {
        "verdict": "EXACT_PHASE_FREE_SECTORS_CURRENT_LIFT_NOT_TRANSPORTED",
        "checks": sum(checks.values()),
        "source_sha256": SOURCE_SHA256,
        "uniform_sector": {
            "source": "|s> = 240^(-1/2) sum_alpha |alpha> on every edge source",
            "edge": "(4I-Swap)/5",
            "open_chain_reference_energy": "3*kappa*m/5",
            "branch": "E_n-E_ref=(2*kappa/5)(1-cos(q_n)), q_n=pi*n/(m+1), n=0,...,m",
        },
        "lower_exact_eigenstate": {
            "pair": "Pair_e=240^(-1/2) sum_alpha |alpha>_S_e |psi_alpha>_M_e",
            "representation": "the coordinate subspace is conjugate4: P_r K=K r^T",
            "state": "tensor_e Pair_e tensor |v>_M_(m+1), arbitrary terminal v in C4",
            "edge_eigenvalue": "1/2",
            "energy": "kappa*m/2",
            "relative_to_reference": "-kappa*m/10",
            "terminal_multiplicity_at_least": 4,
        },
        "current_lift": {
            "uniform_source_survives": False,
            "coordinate_pair_survives": False,
            "reason": (
                "For any bracket-compatible monomial lift, invariance of a rephased "
                "aligned pair requires eta_g(alpha)=f_(g alpha)/f_alpha.  The certified "
                "word swaps alpha,beta and fixes gamma=alpha+beta, forcing eta_alpha "
                "eta_beta=eta_gamma=1, while bracket order forces eta_gamma=-eta_alpha "
                "eta_beta."
            ),
            "obstruction_sha256": OBSTRUCTION_SHA256,
        },
        "scope": (
            "Existing J=mu=0 pure-permutation Hamiltonian only.  Exact finite open-chain "
            "sectors; no ground-state claim, no continuum dispersion, and no physical "
            "current-source preparation."
        ),
        "check_counts": dict(sorted(checks.items())),
        "path_characteristic_polynomials_N2_to_N10": charpolys,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
