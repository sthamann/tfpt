"""Original v117 parallel transport realizes the v118 six-phase operator.

The ODE uses the actual Fuchs residues, not a connection fitted to its
monodromy. Its raw coordinate frames are NOT Euclidean orthonormal frames.
The independent exact v117 representative supplies the unitary finite
dictionary; it is not substituted for the numerical path transport.

This is a two-fiber path operator. It does not identify a full source
covariance, a physical time step, or the P1 Calderon polarization.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import permutations
from typing import Any, Callable

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


ODE_RTOL = 2e-11
ODE_ATOL = 2e-13
NUMERICAL_TOLERANCE = 2e-8


def original_fuchs_connection(z: complex) -> np.ndarray:
    """A(z)=sum U^k A0 U^-k/(z-i^k), exactly the definition in v117."""
    a0 = np.array([[1/2, np.sqrt(8)/12, 0],
                   [np.sqrt(8)/12, 1/4, np.sqrt(5)/12],
                   [0, np.sqrt(5)/12, 1/4]], dtype=complex)
    u = np.array([1, 1j, -1j])
    return sum((u**k)[:, None] * a0 * (u**(-k))[None, :] / (z-1j**k)
               for k in range(4))


def half_arc(t: float, x: float = 0.5, orientation: int = 1,
             reflected: bool = False) -> tuple[complex, complex]:
    """Lower arc x->1/x for +1; its reciprocal goes back along the upper arc.

    c^2-r^2=1 makes the circle invariant under z->1/z. Both arcs together
    wind once about +1 and zero times about the other three punctures.
    """
    if not 0 < x < 1 or orientation not in (-1, 1):
        raise ValueError("Require 0 < x < 1 and orientation in {-1, +1}")
    center, radius = (x+1/x)/2, (1/x-x)/2
    phase = np.exp(orientation*1j*np.pi*t)
    z = center-radius*phase
    dz = -radius*orientation*1j*np.pi*phase
    return (1/z, -dz/z**2) if reflected else (z, dz)


def _integrate(path: Callable[[float], tuple[complex, complex]],
               rtol: float, atol: float) -> tuple[np.ndarray, int, np.ndarray]:
    def rhs(t: float, value: np.ndarray) -> np.ndarray:
        z, dz = path(t)
        return (dz*original_fuchs_connection(z) @ value.reshape(3, 3)).ravel()

    result = solve_ivp(rhs, (0, 1), np.eye(3, dtype=complex).ravel(),
                       method="DOP853", rtol=rtol, atol=atol,
                       t_eval=np.linspace(0, 1, 257))
    if not result.success:
        raise RuntimeError("Original Fuchs path integration failed: " + result.message)
    determinants = np.linalg.det(result.y.T.reshape(-1, 3, 3))
    return result.y[:, -1].reshape(3, 3), result.nfev, determinants


@lru_cache(maxsize=12)
def integrate_path_transport(x: float = 0.5, orientation: int = 1,
                             rtol: float = ODE_RTOL,
                             atol: float = ODE_ATOL) -> dict[str, Any]:
    """Execute both original-connection paths and an independent full circle.

    P maps E_x to E_(1/x), Q maps it back, so H=QP. The block S merely
    changes the second fiber's frame to the P-transported frame. S is not
    asserted unitary in the raw Euclidean coordinates.
    """
    half_arc(0, x, orientation)  # Validate before constructing all paths.
    p, pn, _ = _integrate(lambda t: half_arc(t, x, orientation), rtol, atol)
    q, qn, _ = _integrate(lambda t: half_arc(t, x, orientation, True), rtol, atol)
    center, radius = (x+1/x)/2, (1/x-x)/2

    def circle(t: float) -> tuple[complex, complex]:
        phase = np.exp(orientation*2j*np.pi*t)
        return center-radius*phase, -radius*orientation*2j*np.pi*phase

    loop, ln, determinant_samples = _integrate(circle, rtol, atol)
    determinant_expected = np.array([(1-circle(t)[0]**4)/(1-x**4)
                                     for t in np.linspace(0, 1, 257)])
    determinant_angles = np.unwrap(np.angle(determinant_samples))
    winding = float((determinant_angles[-1]-determinant_angles[0])/(2*np.pi))
    h = q @ p
    zero, eye = np.zeros((3, 3), complex), np.eye(3, dtype=complex)
    raw_t = np.block([[zero, q], [p, zero]])
    frame = np.block([[eye, zero], [zero, p]])
    based_t = np.linalg.solve(frame, raw_t @ frame)
    expected_based_t = np.block([[zero, h], [eye, zero]])
    roots = np.exp(2j*np.pi*np.arange(3)/3)
    eigenvalues = np.linalg.eigvals(h)
    spectrum_error = min(float(np.max(np.abs(eigenvalues-roots[list(order)])))
                         for order in permutations(range(3)))
    return {
        "x": x, "orientation": orientation, "P": p, "Q": q,
        "monodromy": h, "independent_loop": loop, "raw_T": raw_t,
        "transported_frame": frame, "based_T": based_t,
        "eigenvalues": eigenvalues,
        "errors": {
            "composition_vs_full_circle": float(np.linalg.norm(h-loop)),
            "monodromy_cube": float(np.linalg.norm(np.linalg.matrix_power(h, 3)-eye)),
            "monodromy_spectrum": spectrum_error,
            "based_frame_identity": float(np.linalg.norm(based_t-expected_based_t)),
            "path_period_six": float(np.linalg.norm(np.linalg.matrix_power(raw_t, 6)-np.eye(6))),
            "determinant_winding": abs(winding-orientation),
            "determinant_curve_relative": float(np.max(np.abs(determinant_samples-determinant_expected)
                                                        / (1+np.abs(determinant_expected)))),
        },
        "determinant_character": {
            "trace_connection": "tr A(z)=4z³/(z⁴−1)",
            "normalized_at_zero": "det Ψ(z)=1−z⁴, Ψ(0)=I",
            "normalized_at_path_basepoint": "det PT(x→z)=(1−z⁴)/(1−x⁴)",
            "integrated_phase_winding": winding,
            "phase_samples": len(determinant_samples),
            "largest_sample_phase_increment": float(np.max(np.abs(np.diff(determinant_angles)))),
            "scope": "Die Phase auf dem primitiven Punkturkreis hat die P1-Einheitswindung als K1-Klasse. Das identifiziert noch nicht den vollständigen P1-Nahtoperator.",
        },
        "raw_euclidean_unitarity_defect": float(np.linalg.norm(raw_t.conj().T @ raw_t-np.eye(6))),
        "solver": {"method": "DOP853", "rtol": rtol, "atol": atol,
                   "rhs_evaluations": [pn, qn, ln]},
    }


def exact_clock_dictionary() -> dict[str, Any]:
    """Independent exact v117/v118 matrices; no numerical ODE calibration."""
    i = sp.I
    m = sp.Matrix([[0, -(1+i)/2, (1-i)/2],
                   [-(1+i)/2, -i/2, -sp.Rational(1, 2)],
                   [(1-i)/2, -sp.Rational(1, 2), i/2]])
    zero, eye = sp.zeros(3), sp.eye(3)
    t = zero.row_join(m).col_join(eye.row_join(zero))
    j = eye.row_join(eye).col_join(m.row_join(-m))/sp.sqrt(2)
    u6 = sp.diag(m, -m)
    y, delta = sp.symbols("y delta", real=True)
    checks = {
        "original_M_unitary": sp.simplify(m.H*m) == eye,
        "original_M_cubic": sp.simplify(m**3) == eye,
        "J_unitary": sp.simplify(j.H*j) == sp.eye(6),
        "T_unitary": sp.simplify(t.H*t) == sp.eye(6),
        "T_period_six": sp.simplify(t**6) == sp.eye(6),
        "inverse_T_is_original_U6": sp.simplify(j.H*t.inv()*j) == u6,
        "linear_sheet_parity": sp.simplify(j.H*t**3*j) == sp.diag(eye, -eye),
        "transport_determinant": sp.expand((y*sp.eye(6)-delta*t.inv()).det()-(y**6-delta**6)) == 0,
    }
    return {"M": m, "T": t, "J": j, "U6": u6, "checks": checks}


def finite_kernel_comparison(y: float = 2/3, delta: float | None = None,
                             epsilon: float = 1e-3) -> dict[str, Any]:
    """Full six-dimensional matrix identities, in the exact unitary frame.

    The default delta is the original archive's transport stationary root.
    This is not an assertion about a compression of the infinite source.
    """
    if delta is None:
        delta = float(((794-7*np.sqrt(9961))/2187)**(1/6))
    if epsilon < 0:
        raise ValueError("epsilon must be nonnegative")
    exact = exact_clock_dictionary()
    t, j, u6 = [np.array(exact[key].evalf(), complex) for key in ("T", "J", "U6")]
    d_path = y*np.eye(6)-delta*t.conj().T
    d_flavor = y*np.eye(6)-delta*u6

    def kernels(d: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        positive = d.conj().T @ d + epsilon**2*np.eye(6)
        values, vectors = np.linalg.eigh(positive)
        if np.min(values) <= 0:
            raise ValueError("Transport kernel is not positive and invertible")
        root_inverse = (vectors/np.sqrt(values)) @ vectors.conj().T
        return positive, np.linalg.inv(positive), root_inverse

    a_path, green_path, k_path = kernels(d_path)
    a_flavor, green_flavor, k_flavor = kernels(d_flavor)
    expected_spectrum = np.sort(y*y+delta*delta-2*y*delta*np.cos(np.pi*np.arange(6)/3)+epsilon**2)
    return {
        "parameters": {"y": float(y), "delta": float(delta), "epsilon": float(epsilon)},
        "J": j, "D_path": d_path, "D_flavor": d_flavor,
        "positive_path": a_path, "positive_flavor": a_flavor,
        "Green_path": green_path, "Green_flavor": green_flavor,
        "K_path": k_path, "K_flavor": k_flavor,
        "expected_positive_spectrum": expected_spectrum,
        "errors": {
            "D_conjugacy": float(np.linalg.norm(j.conj().T @ d_path @ j-d_flavor)),
            "positive_conjugacy": float(np.linalg.norm(j.conj().T @ a_path @ j-a_flavor)),
            "Green_conjugacy": float(np.linalg.norm(j.conj().T @ green_path @ j-green_flavor)),
            "inverse_square_root_conjugacy": float(np.linalg.norm(j.conj().T @ k_path @ j-k_flavor)),
            "cyclotomic_determinant": float(abs(np.linalg.det(d_path)-(y**6-delta**6))),
            "positive_spectrum": float(np.max(np.abs(np.linalg.eigvalsh(a_path)-expected_spectrum))),
        },
    }


def _complex_json(matrix: np.ndarray) -> Any:
    """Each complex entry is [real, imaginary], including one-dimensional arrays."""
    value = np.asarray(matrix)
    return np.stack((value.real, value.imag), axis=-1).tolist()


@lru_cache(maxsize=1)
def build_flavor_path_transport_data() -> dict[str, Any]:
    forward = integrate_path_transport()
    reverse = integrate_path_transport(orientation=-1)
    reversal = float(np.linalg.norm(reverse["monodromy"] @ forward["monodromy"]-np.eye(3)))
    exact = exact_clock_dictionary()
    kernels = finite_kernel_comparison()

    def check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
        return {"name": name, "ok": bool(ok), "actual": actual,
                "expected": expected, "method": method}

    checks = [
        check("Zwei echte Halbwege ergeben den ursprünglichen Punkturumlauf",
              max(forward["errors"].values()) < NUMERICAL_TOLERANCE,
              forward["errors"], {"absolute_tolerance": NUMERICAL_TOLERANCE},
              "Numerische Integration der originalen v117-Verbindung; eigenständige Vollkreisintegration"),
        check("Umgekehrte Wegorientierung gibt die inverse Monodromie",
              reversal < NUMERICAL_TOLERANCE, reversal, NUMERICAL_TOLERANCE,
              "Beide umgekehrten Halbwege erneut integriert, keine Matrixinversion als Ersatz"),
        check("Der exakte Wegintertwiner liefert die originale Flavorclock",
              all(exact["checks"].values()), exact["checks"], True,
              "Unabhängige Sympy-Identitäten mit der originalen exakten v117-Matrix"),
        check("Transport, positiver Kernel und Determinante stimmen vollständig überein",
              max(kernels["errors"].values()) < NUMERICAL_TOLERANCE,
              kernels["errors"], {"absolute_tolerance": NUMERICAL_TOLERANCE},
              "Alle sechs Matrixrichtungen im unitären exakten Rahmen; keine Quellraumkompression"),
    ]
    data = {
        "title": "Die Flavorclock entsteht aus zwei Wegen derselben Originalverbindung",
        "formula": "QP=M; T=[[0,M],[I,0]]; J†T⁻¹J=M⊕(−M)",
        "paths": {
            "basepoint": forward["x"], "reflected_basepoint": 1/forward["x"],
            "first": "Unterer Halbkreis x→1/x", "second": "Bild unter z→1/z: oberer Halbkreis zurück",
            "winding": {"1": 1, "i": 0, "-1": 0, "-i": 0},
            "basepoint_scope": "Eine Verschiebung von x innerhalb (0,1) ändert den Operator nur durch parallelen Rahmentransport.",
        },
        "ode": {
            "matrix_encoding": "Jeder Eintrag ist [Realteil, Imaginärteil]",
            "P": _complex_json(forward["P"]), "Q": _complex_json(forward["Q"]),
            "QP": _complex_json(forward["monodromy"]),
            "raw_T": _complex_json(forward["raw_T"]),
            "eigenvalues": _complex_json(forward["eigenvalues"]),
            "errors": forward["errors"], "orientation_reversal_error": reversal,
            "solver": forward["solver"], "check_tolerance": NUMERICAL_TOLERANCE,
            "determinant_character": forward["determinant_character"],
            "raw_euclidean_unitarity_defect": forward["raw_euclidean_unitarity_defect"],
            "metric": "Rohe ODE-Koordinaten sind nicht euklidisch orthonormal. Die positive flache Metrik existiert analytisch durch endliche Monodromie; hier wird sie nicht numerisch rekonstruiert.",
        },
        "exact_dictionary": {
            "M": [[str(v) for v in row] for row in exact["M"].tolist()],
            "J": "(1/sqrt(2)) [[I,I],[M,−M]]", "linear_sheet_operator": "S_path=T³",
            "checks": exact["checks"],
            "scope": "Originale exakte Monodromiedarstellung; ihre unitäre Basis wird von den rohen ODE-Koordinaten getrennt.",
        },
        "kernels": {
            "parameters": kernels["parameters"], "errors": kernels["errors"],
            "D": "D_path=yI−δT⁻¹; J†D_path J=yI−δU6",
            "Green": "G=(D†D+ε²I)⁻¹", "positive_kernel": "Kε=(D†D+ε²I)⁻¹/²",
            "determinant": "det(D_path)=y⁶−δ⁶",
            "positive_spectrum": kernels["expected_positive_spectrum"].tolist(),
        },
        "scope": {
            "realized": "Basierter komplexlinearer Paralleltransport auf zwei Fasern der ursprünglichen Fuchsverbindung, mit originalem endlichem Flavoroperator.",
            "not_identified": ["Vollständige Quellenkovarianz oder ein Schurkomplement auf dem unendlichen Quellraum",
                               "P1-Calderónpolarisation iC = T³", "Physische Zeitentwicklung",
                               "P1-Einheitswindung als Auswahl genau dieses Punktur-Halbwegs"],
        },
    }
    return {"data": data, "checks": checks, "sources": [
        "verification/v117_monodromy_weyl_a3.py:54-126",
        "verification/v118_hexagon_family_dictionary.py:10-40",
        "_archive/tfpt-45/source_extracts/03_em_flavor_source.tex:725-846",
        "tfpt_2_standard_model.tex:2624-2631",
    ]}
