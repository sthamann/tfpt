#!/usr/bin/env python3
"""Numerical second-order Schur step between the exact 20 and 02 quartets.

This is deliberately a bounded three-site patch.  It reconstructs the native
60-ray source, the exact analytic relaxed quartet in charge sectors (2,0) and
(0,2), and resolves only the two charge sectors reached by one application of

    V = 1 - Re <psi_1 | psi_2>.

The identity part is killed by Q on an H0 eigenstate.  The overlap term sends
20 only to 11 and 33.  In those sectors Q is the identity, so the requested
Schur kernel is obtained from two positive shifted linear solves rather than a
large full-spectrum diagonalisation.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.sparse.linalg import LinearOperator, cg


REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "resolvent.json"
OUT_TXT = HERE / "resolvent.txt"

SOURCE_REL = Path(
    "experiments/theory-contracts/"
    "compiler-correlated-event-clock-20260919/source_channel.py"
)
GROUND_REL = Path(
    "experiments/theory-contracts/"
    "compiler-bond-response-20260919/ground_audit.py"
)
GROUND_JSON_REL = Path(
    "experiments/theory-contracts/"
    "compiler-bond-response-20260919/ground_audit.json"
)
PAIR_REL = Path(
    "experiments/theory-contracts/"
    "compiler-pair-sector-audit-20260919/mixed_source_check.py"
)
PAIR_JSON_REL = Path(
    "experiments/theory-contracts/"
    "compiler-pair-sector-audit-20260919/mixed_source_check.json"
)
PINS = {
    SOURCE_REL: "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    GROUND_REL: "61980c8b830378f312ef6f81ad655574195e29c7287f5f14bc5aa0217f90b6e8",
    GROUND_JSON_REL: "f3e45d26034d42fdba0752d4844190221202e4e887ea411280d5ee558bf69886",
    PAIR_REL: "5f80a4e693afa138c7f57dd5a7b6f63955caafd78273f0d0a9dee3390e412ecb",
    PAIR_JSON_REL: "89670007dd1f28ff891350fef5ca8a84a99f51f9b24f2e3064852a97b5eee9cf",
}


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def complex_matrix(matrix: np.ndarray) -> dict[str, list[list[float]]]:
    return {
        "real": np.asarray(matrix.real, dtype=float).tolist(),
        "imag": np.asarray(matrix.imag, dtype=float).tolist(),
    }


def scalar_identity_error(matrix: np.ndarray) -> tuple[complex, float]:
    scalar = np.trace(matrix) / matrix.shape[0]
    error = float(np.max(np.abs(matrix - scalar * np.eye(matrix.shape[0]))))
    return complex(scalar), error


def make_states(rays: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return bare u quartets and normalized relaxed quartets in 20 and 02."""
    psi = np.stack(rays) / 2
    # Omega_{R,AB}[ell,a,b] = psi_ell[a] psi_ell[b] / sqrt(60).
    omega = np.einsum("la,lb->lab", psi, psi) / np.sqrt(60)
    source_scalar = np.ones(60, dtype=np.complex128) / np.sqrt(60)
    bare_tensor = np.einsum(
        "lab,m,Cc->lmabCc", omega, source_scalar, np.eye(4, dtype=np.complex128)
    )
    bare20 = bare_tensor.reshape(-1, 4)
    swapped20 = bare_tensor.transpose(0, 1, 2, 4, 3, 5).reshape(-1, 4)

    # Right eigenvector of [[4/5,-2/5],[-1/5,8/5]] at E_minus.
    ratio = (np.sqrt(6) - 2) / 2
    norm2 = 1 + ratio * ratio + ratio / 2  # <u,w>=1/4.
    relaxed20 = (bare20 + ratio * swapped20) / np.sqrt(norm2)

    # Mirror A<->C and R1<->R2, retaining the same internal colour label.
    bare02 = bare_tensor.transpose(1, 0, 4, 3, 2, 5).reshape(-1, 4)
    relaxed02 = relaxed20.reshape(60, 60, 4, 4, 4, 4)
    relaxed02 = relaxed02.transpose(1, 0, 4, 3, 2, 5).reshape(-1, 4)
    return bare20, bare02, relaxed20, relaxed02


def overlap_shift(states: np.ndarray, overlap: np.ndarray, branch: str) -> np.ndarray:
    """Apply Re-overlap branch without the minus sign from V.

    down_up sends (s1,s2)->(s1-1,s2+1) with z/2.
    up_down sends (s1,s2)->(s1+1,s2-1) with conjugate(z)/2.
    """
    multiplier = overlap if branch == "down_up" else overlap.conj()
    tensor = states.reshape(60, 60, 4, 4, 4, -1)
    return (multiplier[:, :, None, None, None, None] * tensor / 2).reshape(
        -1, states.shape[1]
    )


def solve_columns(
    hamiltonian: LinearOperator,
    energy: float,
    rhs: np.ndarray,
) -> tuple[np.ndarray, list[int], list[float]]:
    shifted = LinearOperator(
        hamiltonian.shape,
        matvec=lambda vector: hamiltonian @ vector - energy * vector,
        dtype=np.complex128,
    )
    columns = []
    iterations = []
    residuals = []
    for colour in range(rhs.shape[1]):
        count = 0

        def callback(_vector: np.ndarray) -> None:
            nonlocal count
            count += 1

        solution, info = cg(
            shifted,
            rhs[:, colour],
            rtol=2e-13,
            atol=0.0,
            maxiter=100,
            callback=callback,
        )
        if info != 0:
            raise RuntimeError(f"CG failed for colour {colour}: info={info}")
        columns.append(solution)
        iterations.append(count)
        residuals.append(float(np.linalg.norm(shifted @ solution - rhs[:, colour])))
    return np.column_stack(columns), iterations, residuals


def main() -> None:
    checks: list[str] = []
    for relative, expected in PINS.items():
        observed = hashlib.sha256((REPO / relative).read_bytes()).hexdigest()
        require(observed == expected, f"pinned input {relative}", checks)

    pair_certificate = json.loads((REPO / PAIR_JSON_REL).read_text())
    require(
        pair_certificate["status"] == "PASS_EXACT_MIXED_SOURCE_SECTOR",
        "exact mixed-source quartet certificate passes",
        checks,
    )
    ground_certificate = json.loads((REPO / GROUND_JSON_REL).read_text())

    source = load_module("domain_wall_source", REPO / SOURCE_REL)
    ground = load_module("domain_wall_ground", REPO / GROUND_REL)
    rays = source.source_rays()
    require(len(rays) == 60, "native source has sixty rays", checks)
    blocks = ground.build_charge_blocks(rays, Counter())

    bare20, bare02, left20, right02 = make_states(rays)
    identity4 = np.eye(4, dtype=np.complex128)
    require(
        np.max(np.abs(left20.conj().T @ left20 - identity4)) < 2e-12,
        "20 relaxed quartet is orthonormal",
        checks,
    )
    require(
        np.max(np.abs(right02.conj().T @ right02 - identity4)) < 2e-12,
        "02 relaxed quartet is orthonormal",
        checks,
    )

    energy = float((6 - np.sqrt(6)) / 5)
    h20 = ground.sector_operator(blocks[2], blocks[0])
    h02 = ground.sector_operator(blocks[0], blocks[2])
    state_residuals = {
        "20": [float(np.linalg.norm(h20 @ left20[:, c] - energy * left20[:, c])) for c in range(4)],
        "02": [float(np.linalg.norm(h02 @ right02[:, c] - energy * right02[:, c])) for c in range(4)],
    }
    require(max(state_residuals["20"] + state_residuals["02"]) < 2e-12,
            "analytic relaxed states have the exact target energy numerically", checks)

    psi = np.stack(rays) / 2
    overlap = psi.conj() @ psi.T

    # V=-D between distinct charge sectors.  One step from 20 or 02 reaches
    # only 11 and 33.  These sectors are automatically orthogonal to P.
    rhs_left = {
        "11": -overlap_shift(left20, overlap, "down_up"),
        "33": -overlap_shift(left20, overlap, "up_down"),
    }
    rhs_right = {
        "11": -overlap_shift(right02, overlap, "up_down"),
        "33": -overlap_shift(right02, overlap, "down_up"),
    }

    # Phase/convention control from the unrelaxed packet: <u02|V^2|u20>=I4/160.
    bare_left = {
        "11": -overlap_shift(bare20, overlap, "down_up"),
        "33": -overlap_shift(bare20, overlap, "up_down"),
    }
    bare_right = {
        "11": -overlap_shift(bare02, overlap, "up_down"),
        "33": -overlap_shift(bare02, overlap, "down_up"),
    }
    bare_v2 = sum(bare_right[key].conj().T @ bare_left[key] for key in ("11", "33"))
    require(np.max(np.abs(bare_v2 - identity4 / 160)) < 2e-13,
            "bare packet V squared matrix is delta_cd over 160", checks)

    channel_data: dict[str, Any] = {}
    schur_kernel = np.zeros((4, 4), dtype=np.complex128)
    diagonal_left = np.zeros((4, 4), dtype=np.complex128)
    diagonal_right = np.zeros((4, 4), dtype=np.complex128)
    max_reciprocity_error = 0.0

    for key, charge in (("11", 1), ("33", 3)):
        hamiltonian = ground.sector_operator(blocks[charge], blocks[charge])
        solved_left, iterations_left, residuals_left = solve_columns(
            hamiltonian, energy, rhs_left[key]
        )
        solved_right, iterations_right, residuals_right = solve_columns(
            hamiltonian, energy, rhs_right[key]
        )
        cross = rhs_right[key].conj().T @ solved_left
        reverse_cross = rhs_left[key].conj().T @ solved_right
        reciprocity_error = float(np.max(np.abs(cross - reverse_cross.conj().T)))
        max_reciprocity_error = max(max_reciprocity_error, reciprocity_error)
        self_left = rhs_left[key].conj().T @ solved_left
        self_right = rhs_right[key].conj().T @ solved_right
        schur_kernel += cross
        diagonal_left += self_left
        diagonal_right += self_right
        cross_scalar, cross_error = scalar_identity_error(cross)
        left_scalar, left_error = scalar_identity_error(self_left)
        right_scalar, right_error = scalar_identity_error(self_right)
        channel_data[key] = {
            "observed_floor_over_kappa_from_pinned_ground_audit":
                float(ground_certificate["numerical_full_space_audit"]["sectors"][f"{charge},{charge}"]["lowest_four"][0]),
            "distance_floor_minus_Estar":
                float(ground_certificate["numerical_full_space_audit"]["sectors"][f"{charge},{charge}"]["lowest_four"][0] - energy),
            "cg_iterations_left": iterations_left,
            "cg_iterations_right": iterations_right,
            "linear_residuals_left": residuals_left,
            "linear_residuals_right": residuals_right,
            "cross_kernel": complex_matrix(cross),
            "cross_scalar_real": float(cross_scalar.real),
            "cross_scalar_imag": float(cross_scalar.imag),
            "cross_scalar_identity_max_error": cross_error,
            "forward_reverse_reciprocity_max_error": reciprocity_error,
            "left_diagonal_scalar_real": float(left_scalar.real),
            "left_diagonal_scalar_identity_max_error": left_error,
            "right_diagonal_scalar_real": float(right_scalar.real),
            "right_diagonal_scalar_identity_max_error": right_error,
        }

    kernel_scalar, kernel_error = scalar_identity_error(schur_kernel)
    left_scalar, left_error = scalar_identity_error(diagonal_left)
    right_scalar, right_error = scalar_identity_error(diagonal_right)
    hopping = -schur_kernel
    hopping_scalar = -kernel_scalar

    max_linear_residual = max(
        residual
        for data in channel_data.values()
        for field in ("linear_residuals_left", "linear_residuals_right")
        for residual in data[field]
    )
    require(max_linear_residual < 5e-13, "all shifted solves have small residual", checks)
    require(max_reciprocity_error < 5e-13,
            "forward and reverse Schur kernels satisfy reciprocity", checks)
    require(kernel_error < 2e-14, "Schur transition is scalar on the internal quartet", checks)
    require(left_error < 3e-14 and right_error < 3e-14,
            "diagonal shifts are scalar on both quartets", checks)
    require(abs(left_scalar - right_scalar) < 2e-13,
            "mirror quartets have equal diagonal shift", checks)
    require(abs(hopping_scalar.real) > 1e-6,
            "second-order resolvent hopping is nonzero", checks)

    result = {
        "status": "PASS_NUMERICAL_BARE_WALL_RESOLVENT_STEP",
        "verdict": "NONZERO_SECOND_ORDER_BARE_WALL_STEP_IN_BOUNDED_PATCH",
        "kappa": 1.0,
        "energy_Estar": energy,
        "energy_exact": "(6-sqrt(6))/5",
        "dimensions": {
            "charge_sector": 230400,
            "low_quartets": [4, 4],
            "resolved_intermediate_sectors": ["11", "33"],
        },
        "routing": {
            "20_to_02_direct_V": "zero by Z4 source-charge selection",
            "20_one_V": ["11 via z/2", "33 via conjugate(z)/2"],
            "02_one_V": ["11 via conjugate(z)/2", "33 via z/2"],
            "Q_in_intermediate_sectors": "identity because 11 and 33 are disjoint from the 20+02 low space",
        },
        "state_residuals": state_residuals,
        "bare_packet_V2_control": complex_matrix(bare_v2),
        "channels": channel_data,
        "schur_kernel_K_RL": complex_matrix(schur_kernel),
        "schur_kernel_scalar_real": float(kernel_scalar.real),
        "schur_kernel_scalar_imag": float(kernel_scalar.imag),
        "schur_kernel_scalar_identity_max_error": kernel_error,
        "requested_hopping_T_LR_equals_minus_K_RL": complex_matrix(hopping),
        "hopping_scalar_real": float(hopping_scalar.real),
        "hopping_scalar_imag": float(hopping_scalar.imag),
        "left_second_order_energy_shift_scalar": float(-left_scalar.real),
        "right_second_order_energy_shift_scalar": float(-right_scalar.real),
        "diagonal_shift_mirror_difference": float(abs(left_scalar - right_scalar)),
        "max_linear_residual": max_linear_residual,
        "max_forward_reverse_reciprocity_error": max_reciprocity_error,
        "checks": checks,
        "check_count": len(checks),
        "pins": {str(path): digest for path, digest in PINS.items()},
        "scope_boundary": (
            "Actual second-order Schur matrix element between the existing exact local relaxed bare-wall "
            "quartets.  This patch omits the Phi-dressed complete core, where the free four is absorbed "
            "and direct first-order hops occur.  It therefore does not prove that this quartet is an "
            "isolated manifold in a full chain, does not derive an SSH/Dirac continuum theory, and does "
            "not select a global vacuum or environment."
        ),
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    text = f"""DOMAIN-WALL LOCAL RESOLVENT TEST

status: {result['status']}
verdict: {result['verdict']}
kappa: 1
E*: (6-sqrt(6))/5 = {energy:.15f}

The exact relaxed 20 and 02 quartet states were reconstructed analytically.
Maximum H0 eigenstate residual: {max(state_residuals['20'] + state_residuals['02']):.3e}

Charge routing under one V:
  20 -> 11,33
  02 -> 11,33
  20 -> 02 directly: zero

Bare-packet convention check:
  <u_02|V^2|u_20> = I_4/160 to max error {np.max(np.abs(bare_v2-identity4/160)):.3e}

Resolved Schur kernel K_RL=<R|V Q(H0-E*)^-1 Q V|L>:
  sector 11: {channel_data['11']['cross_scalar_real']:.15f} * I_4
  sector 33: {channel_data['33']['cross_scalar_real']:.15e} * I_4
  total:     {kernel_scalar.real:.15f} * I_4
  scalar-identity max error: {kernel_error:.3e}

Requested hopping T_LR=-K_RL:
  T_LR = {hopping_scalar.real:.15f} * I_4

Second-order diagonal energy correction:
  delta E_20 = {-left_scalar.real:.15f}
  delta E_02 = {-right_scalar.real:.15f}
  mirror difference = {abs(left_scalar-right_scalar):.3e}

Numerics:
  observed intermediate floors: E_11={channel_data['11']['observed_floor_over_kappa_from_pinned_ground_audit']:.15f}, E_33={channel_data['33']['observed_floor_over_kappa_from_pinned_ground_audit']:.15f}
  maximum shifted-solve residual: {max_linear_residual:.3e}
  maximum forward/reverse reciprocity error: {max_reciprocity_error:.3e}
  CG iterations per colour: 11 L/R={channel_data['11']['cg_iterations_left']}/{channel_data['11']['cg_iterations_right']}; 33 L/R={channel_data['33']['cg_iterations_left']}/{channel_data['33']['cg_iterations_right']}

Boundary:
  This is an actual local second-order Schur matrix element for the relaxed
  bare-wall patch.  It omits the Phi-dressed complete core, where the free four
  is absorbed and direct first-order hops occur.  It is not a proof of an
  isolated full-chain quartet manifold, a global vacuum, or an SSH/Dirac limit.
"""
    OUT_TXT.write_text(text)
    print(json.dumps({
        "status": result["status"],
        "hopping_scalar": result["hopping_scalar_real"],
        "diagonal_shift": result["left_second_order_energy_shift_scalar"],
        "max_linear_residual": max_linear_residual,
        "check_count": len(checks),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
