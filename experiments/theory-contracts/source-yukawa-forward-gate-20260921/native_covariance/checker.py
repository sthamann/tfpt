#!/usr/bin/env python3
"""Compress the unchanged QWZ filled-sea covariance to the original 3-mode block.

No target Dirac/Yukawa matrix is used.  The only optional comparison is the
same limiting one-particle generator in a declared beta-KMS state.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
HERE = Path(__file__).resolve().parent
LABELS = (-1, 0, 1)
SIZES = (8, 16, 32)
SOURCE_HASHES = {
    "verification/v258_dirac_covariance_induction.py":
        "16c60e831dceba773f3629466895f1009654827286e5b760ae01bd755fd5c0b1",
    "experiments/theory-contracts/microscopic-charged-car-limit/README.md":
        "39c613b80a1fe64200d269b782f6fb86c98f92c78058891a6144605e09c4532b",
    "experiments/theory-contracts/microscopic-charged-car-limit/checker.py":
        "2259bd7d6ab890c8cca562774b1b5cdc574e60fb72a04a8c8c8f6ed8292f113a",
    "experiments/theory-contracts/microscopic-energy-linearization/checker.py":
        "393ee8e6362ca96c4fbf0354f5f9250ed445a56ba32e22659573649346cd2ce9",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_source():
    path = ROOT / "experiments/theory-contracts/microscopic-charged-car-limit/checker.py"
    spec = importlib.util.spec_from_file_location("native_qwz_charged", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.validate_pins()
    return module


def hermitian(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.conj().T) / 2


def encode_real_matrix(matrix: np.ndarray) -> list[list[float]]:
    require(np.linalg.norm(matrix.imag) < 1e-11, "expected real matrix in momentum block")
    return [[float(x) for x in row] for row in matrix.real]


def logit_without_clipping(values: np.ndarray) -> tuple[list[float | str], list[str]]:
    logits: list[float | str] = []
    statuses: list[str] = []
    for value in values:
        x = float(value)
        if x == 0.0:
            logits.append("+Infinity")
            statuses.append("singular_zero_endpoint")
        elif x == 1.0:
            logits.append("-Infinity")
            statuses.append("singular_one_endpoint")
        elif 0.0 < x < 1.0:
            logits.append(float(np.log((1.0-x)/x)))
            statuses.append("finite_interior")
        else:
            raise ArithmeticError(f"covariance eigenvalue outside [0,1]: {x!r}")
    return logits, statuses


def analyse_size(source_module, n: int) -> dict:
    _, source = source_module.inherited()
    h_source = source.qwz_cylinder(n, 8, 1, 1)
    evals, vectors = np.linalg.eigh(h_source)
    occupied = evals < 0
    require(int(occupied.sum()) == 8*n, "half-filled original source")
    p = vectors[:, occupied] @ vectors[:, occupied].conj().T
    d = n*h_source/(2*np.pi)

    # This is precisely the raw top-row Fourier block used in the earlier
    # full-source diagnostic, not the already spectrally polarized J_N block.
    r_raw = np.column_stack([source_module.fourier_column(n, j) for j in LABELS])
    gram = hermitian(r_raw.conj().T @ r_raw)
    gw, gu = np.linalg.eigh(gram)
    require(np.all(gw > 0), "raw mode block has positive Gram")
    gram_inverse_sqrt = gu @ np.diag(gw**-0.5) @ gu.conj().T
    s = r_raw @ gram_inverse_sqrt
    normalized_gram = hermitian(s.conj().T @ s)
    ss = s @ s.conj().T

    a = hermitian(s.conj().T @ p @ s)
    a_values = np.linalg.eigvalsh(a)
    require(np.all(a_values >= -2e-14) and np.all(a_values <= 1+2e-14),
            "compressed source covariance is a contraction")
    ns_projector = np.diag([float(j >= 1) for j in LABELS])
    logits, logit_status = logit_without_clipping(a_values)
    projector_defect = hermitian(a-a@a)

    full_identity = np.eye(16*n, dtype=complex)
    entanglement_gram = hermitian(s.conj().T @ p @ (full_identity-ss) @ p @ s)
    entanglement_identity_residual = np.linalg.norm(entanglement_gram-projector_defect, 2)

    first_moment = hermitian(s.conj().T @ d @ s)
    second_moment = hermitian(s.conj().T @ (d@d) @ s)
    time_defect = hermitian(second_moment-first_moment@first_moment)
    qhs = (full_identity-ss) @ d @ s
    time_defect_gram = hermitian(qhs.conj().T @ qhs)
    time_identity_residual = np.linalg.norm(time_defect-time_defect_gram, 2)

    # Exact source formulas from h(p)r=-sin(p)r+(1-cos(p))chi_- and
    # ||h(p)r||=2|sin(p/2)|.  Translation makes distinct momenta diagonal.
    theta = np.array([2*np.pi*(j-0.25)/n for j in LABELS])
    scale = n/(2*np.pi)
    exact_first_diagonal = -scale*np.sin(theta)
    exact_second_diagonal = scale**2 * 4*np.sin(theta/2)**2
    exact_variance_diagonal = scale**2 * (1-np.cos(theta))**2
    require(np.linalg.norm(first_moment-np.diag(exact_first_diagonal), 2) < 2e-12,
            "exact QWZ first moment")
    require(np.linalg.norm(second_moment-np.diag(exact_second_diagonal), 2) < 2e-11,
            "exact QWZ second moment")
    require(np.linalg.norm(time_defect-np.diag(exact_variance_diagonal), 2) < 2e-11,
            "exact QWZ variance")

    wrong_sign_bound_by_label = np.tan(theta/2)**2
    wrong_sign_actual_by_label = np.array([
        a[index, index].real if exact_first_diagonal[index] > 0
        else 1-a[index, index].real
        for index in range(len(LABELS))
    ])
    require(np.all(wrong_sign_actual_by_label <= wrong_sign_bound_by_label+2e-12),
            "spectral Chebyshev wrong-sign occupation bound")
    b_n = float(np.tan(5*np.pi/(4*n))**2)
    require(b_n < 0.5, "N>=8 gives nontrivial logit bound")
    require(np.linalg.norm(a-ns_projector, 2) <= b_n+2e-12,
            "uniform fixed-window NS projector bound")
    logit_abs_lower_bound = float(np.log((1-b_n)/b_n))
    finite_logits = [abs(float(x)) for x in logits if not isinstance(x, str)]
    require(all(x+2e-12 >= logit_abs_lower_bound for x in finite_logits),
            "all finite logits obey analytic divergence lower bound")

    return {
        "N": n,
        "ambient_dimension": 16*n,
        "occupied_rank": int(occupied.sum()),
        "labels_j": list(LABELS),
        "raw_Gram_eigenvalues": [float(x) for x in gw],
        "raw_Gram_minus_I_operator_norm": float(np.linalg.norm(gram-np.eye(3), 2)),
        "normalized_Gram_minus_I_operator_norm": float(np.linalg.norm(normalized_gram-np.eye(3), 2)),
        "A_matrix_real": encode_real_matrix(a),
        "A_eigenvalues": [float(x) for x in a_values],
        "A_diagonal_by_label": {str(j): float(a[k, k].real) for k, j in enumerate(LABELS)},
        "A_minus_NS_projector_operator_norm": float(np.linalg.norm(a-ns_projector, 2)),
        "projector_defect_operator_norm": float(np.linalg.norm(projector_defect, 2)),
        "projector_defect_eigenvalues": [float(x) for x in np.linalg.eigvalsh(projector_defect)],
        "entanglement_Gram_eigenvalues": [float(x) for x in np.linalg.eigvalsh(entanglement_gram)],
        "entanglement_Gram_trace": float(np.trace(entanglement_gram).real),
        "entanglement_equals_A_minus_A2_residual": float(entanglement_identity_residual),
        "logit_eigenvalues_no_clipping": logits,
        "logit_status": logit_status,
        "first_time_moment_eigenvalues": [float(x) for x in np.linalg.eigvalsh(first_moment)],
        "first_time_moment_matrix_real": encode_real_matrix(first_moment),
        "second_time_moment_eigenvalues": [float(x) for x in np.linalg.eigvalsh(second_moment)],
        "time_moment_defect_eigenvalues": [float(x) for x in np.linalg.eigvalsh(time_defect)],
        "time_moment_defect_operator_norm": float(np.linalg.norm(time_defect, 2)),
        "time_moment_defect_equals_QhS_Gram_residual": float(time_identity_residual),
        "exact_QWZ_source_formulas": {
            "theta_j": [float(x) for x in theta],
            "d_j_equals_minus_N_over_2pi_sin_theta": [float(x) for x in exact_first_diagonal],
            "second_moment_equals_scale2_4sin2_half_theta": [float(x) for x in exact_second_diagonal],
            "variance_equals_scale2_one_minus_cos_squared": [float(x) for x in exact_variance_diagonal],
            "first_moment_formula_residual": float(np.linalg.norm(first_moment-np.diag(exact_first_diagonal), 2)),
            "second_moment_formula_residual": float(np.linalg.norm(second_moment-np.diag(exact_second_diagonal), 2)),
            "variance_formula_residual": float(np.linalg.norm(time_defect-np.diag(exact_variance_diagonal), 2)),
            "wrong_sign_actual_by_label": [float(x) for x in wrong_sign_actual_by_label],
            "wrong_sign_Chebyshev_bound_tan2_half_theta": [float(x) for x in wrong_sign_bound_by_label],
            "uniform_b_N": b_n,
            "A_minus_NS_projector_le_b_N": True,
            "finite_logit_abs_lower_bound": logit_abs_lower_bound,
        },
    }


def kms_control(beta: float = 1.0) -> dict:
    # Same limiting source generator only.  beta is declared, not selected.
    r = np.array([0.5-j for j in LABELS], dtype=float)
    h = r-0.25
    occupations = 1.0/(1.0+np.exp(beta*h))
    logits, statuses = logit_without_clipping(occupations)
    residual = np.linalg.norm(np.array(logits, float)-beta*h, np.inf)
    return {
        "scope": "conditional KMS control on the same invariant limiting mode block",
        "general_formula": "C_beta(r)=1/(1+exp(beta*(r-1/4))); logit(C_beta)=beta*(r-1/4)",
        "beta": beta,
        "r_half_integer": [float(x) for x in r],
        "h_limit": [float(x) for x in h],
        "C_beta_eigenvalues": [float(x) for x in occupations],
        "logit_eigenvalues_no_clipping": logits,
        "logit_status": statuses,
        "logit_minus_beta_h_max_abs": float(residual),
        "mu_geo_or_temperature_derived": False,
        "new_flavor_hierarchy_derived": False,
    }


def main() -> dict:
    for rel, digest in SOURCE_HASHES.items():
        actual = hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
        require(actual == digest, f"source hash changed: {rel}")
    source_module = load_source()
    rows = [analyse_size(source_module, n) for n in SIZES]
    # The compression should move toward the already known NS sea projector;
    # report the measured monotonic trend without promoting it to a new theorem.
    for key in ("A_minus_NS_projector_operator_norm", "projector_defect_operator_norm",
                "time_moment_defect_operator_norm"):
        require(all(rows[i+1][key] < rows[i][key] for i in range(len(rows)-1)),
                f"measured source trend is not decreasing: {key}")
    result = {
        "status": "ACTUAL_QWZ_COMPRESSION_APPROACHES_PURE_NS_PROJECTOR",
        "claim_scope": "source-side test of the open physical identification in PS.DIRAC.03",
        "source_hashes": SOURCE_HASHES,
        "raw_source_parameters": {"width": 8, "mass": 1, "sector": 1},
        "mode_block": {"labels_j": list(LABELS), "dimension": 3, "fitted_parameters": 0},
        "normalization": "S_N=R_N(R_N^dagger R_N)^(-1/2), basis normalization only",
        "finite_source_results": rows,
        "conditional_kms_control": kms_control(1.0),
        "verdict": {
            "actual_filled_sea": "finite logits exist from leakage but the exact source bound forces divergence toward the pure NS projector endpoints",
            "faithful_finite_modular_Yukawa_block_observed": False,
            "known_NS_projector_limit_supported": True,
            "reason": "the exact QWZ row identity gives ||A_N-diag(0,0,1)|| <= tan^2(5pi/(4N)); hence every finite logit has absolute value at least log((1-b_N)/b_N) and diverges, while endpoint values are already singular",
            "kms_control": "thermalization at declared beta makes logits finite and returns beta*h, but adds no flavor spectrum and does not derive beta or mu_geo",
        },
        "not_claimed": [
            "R_N is the physical 48/96-dimensional carrier",
            "general no-go for TFPT or for other compressions",
            "derivation of target Yukawas",
            "derivation of beta, temperature, or mu_geo",
            "change to PS.DIRAC.03 ledger status",
        ],
    }
    return result


if __name__ == "__main__":
    result = main()
    (HERE/"results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
