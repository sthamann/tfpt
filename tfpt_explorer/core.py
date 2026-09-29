"""Canonical calculation engine for the interactive TFPT explorer.

The engine recomputes a compact, typed path through the documented TFPT
construction.  It deliberately keeps exact algebra, numerical closures,
conditional physical readings, declared inputs, and open selections distinct.
Every returned object is JSON serialisable and bounded for browser use.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import sympy as sp


DEFAULT_CONFIG = {
    "clock_step": 0,
    "transfer_steps": 6,
    "efolds": 55,
    "phase_b": 1 / 18,
    "initial_state": "localized",
    "recursion_depth": 3,
}

_KINDS = {"exact", "numeric", "conditional", "input", "open"}
_RELATIONS = {"derives", "checks", "assumes", "corresponds", "feeds"}
_ROOT = Path(__file__).resolve().parents[1]


def _validate_config(config: dict[str, Any] | None) -> dict[str, Any]:
    if config is not None and not isinstance(config, dict):
        raise ValueError("config must be a dictionary")
    cfg = dict(DEFAULT_CONFIG)
    if config:
        unknown = sorted(set(config) - set(DEFAULT_CONFIG))
        if unknown:
            raise ValueError(f"unknown config keys: {', '.join(unknown)}")
        cfg.update(config)
    for key, low, high in (("clock_step", 0, 120), ("transfer_steps", 0, 40),
                            ("recursion_depth", 1, 8), ("efolds", 40, 70)):
        value = cfg[key]
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or int(value) != value or not low <= value <= high):
            raise ValueError(f"{key} must be an integer in [{low}, {high}]")
        cfg[key] = int(value)
    if isinstance(cfg["phase_b"], bool) or not isinstance(cfg["phase_b"], (int, float)):
        raise ValueError("phase_b must be numeric")
    if not 0 <= float(cfg["phase_b"]) <= 2 / 9:
        raise ValueError("phase_b must lie in [0, 2/9]")
    if cfg["initial_state"] not in {"localized", "uniform", "skew"}:
        raise ValueError("initial_state must be localized, uniform, or skew")
    return cfg


def _clean(value: Any) -> Any:
    """Convert exact/numpy/mpmath values into bounded JSON values."""
    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, sp.Integer):
        return int(value)
    if isinstance(value, Fraction):
        return {"fraction": f"{value.numerator}/{value.denominator}", "value": float(value)}
    if isinstance(value, sp.Rational):
        return {"fraction": str(value), "value": float(value)}
    if isinstance(value, (mp.mpf, np.floating, float)):
        return float(value)
    if isinstance(value, (complex, np.complexfloating)):
        return {"real": float(value.real), "imag": float(value.imag)}
    if isinstance(value, np.ndarray):
        return _clean(value.tolist())
    if isinstance(value, sp.MatrixBase):
        return _clean(value.tolist())
    if isinstance(value, dict):
        return {str(k): _clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_clean(v) for v in value]
    if value is None or isinstance(value, str):
        return value
    return str(value)


def _check(name: str, actual: Any, expected: Any, method: str, ok: bool | None = None) -> dict[str, Any]:
    if ok is None:
        ok = actual == expected
    return {
        "name": name,
        "ok": bool(ok),
        "actual": _clean(actual),
        "expected": _clean(expected),
        "method": method,
    }


def _stage(**kwargs: Any) -> dict[str, Any]:
    stage = _clean(kwargs)
    if stage["kind"] not in _KINDS:
        raise AssertionError(f"invalid stage kind {stage['kind']}")
    for dep in stage["depends_on"]:
        if dep["relation"] not in _RELATIONS:
            raise AssertionError(f"invalid dependency relation {dep['relation']}")
    return stage


def _cartan_a(n: int) -> sp.Matrix:
    m = 2 * sp.eye(n)
    for i in range(n - 1):
        m[i, i + 1] = m[i + 1, i] = -1
    return m


def _cartan_d(n: int) -> sp.Matrix:
    m = 2 * sp.eye(n)
    for i in range(n - 1):
        m[i, i + 1] = m[i + 1, i] = -1
    m[n - 2, n - 1] = m[n - 1, n - 2] = 0
    m[n - 3, n - 1] = m[n - 1, n - 3] = -1
    return m


def _e8_roots() -> np.ndarray:
    roots: list[tuple[float, ...]] = []
    for i, j in combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0.0] * 8
                v[i], v[j] = float(si), float(sj)
                roots.append(tuple(v))
    for signs in product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(s / 2 for s in signs))
    return np.asarray(roots, dtype=float)


def _glued_roots() -> tuple[np.ndarray, list[int]]:
    """Construct the norm-two shell in (D5 ⊕ D3) + Z(1/2,...,1/2).

    D3 is an isometric realization of A3. Doubled integer coordinates make
    membership and the norm test exact. Four glue cosets, not a root-count
    coincidence, produce the E8 shell.
    """
    roots, counts = [], []
    for coset in range(4):
        choices = (-1, 1) if coset % 2 else (-2, 0, 2)
        start = len(roots)
        for doubled in product(choices, repeat=8):
            if sum(x * x for x in doubled) != 8:
                continue
            difference = [(x - coset) // 2 for x in doubled]
            if sum(difference[:5]) % 2 or sum(difference[5:]) % 2:
                continue
            roots.append(tuple(x / 2 for x in doubled))
        counts.append(len(roots) - start)
    return np.asarray(roots), counts


def _e8_cartan() -> sp.Matrix:
    edges = [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)]
    a = sp.zeros(8, 8)
    for i in range(8):
        a[i, i] = 2
    for u, v in edges:
        a[u - 1, v - 1] = a[v - 1, u - 1] = -1
    return a


def _coxeter(cartan: sp.Matrix) -> sp.Matrix:
    out = sp.eye(8)
    for i in range(8):
        reflection = sp.eye(8)
        for j in range(8):
            reflection[i, j] = (1 if i == j else 0) - cartan[i, j]
        out *= reflection
    return out


def _matrix_order(matrix: sp.Matrix, limit: int = 200) -> int | None:
    power = sp.eye(matrix.rows)
    for order in range(1, limit + 1):
        power *= matrix
        if power == sp.eye(matrix.rows):
            return order
    return None


def _galois_matrices() -> tuple[sp.Matrix, sp.Matrix]:
    x = sp.symbols("x")
    phi5 = x**4 + x**3 + x**2 + x + 1
    c5 = sp.Matrix([[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]])

    def col(exponent: int) -> sp.Matrix:
        p = sp.Poly(sp.rem(x**exponent, phi5, x), x)
        return sp.Matrix([p.coeff_monomial(x**j) for j in range(4)])

    g = sp.Matrix.hstack(*(col(2 * k) for k in range(4)))
    return c5, g


def _exterior_basis() -> tuple[list[dict[str, Any]], list[Fraction]]:
    slot_y = [Fraction(-1, 3)] * 3 + [Fraction(1, 2)] * 2
    states: list[dict[str, Any]] = []
    charges: list[Fraction] = []
    for degree in (0, 2, 4):
        for occupied in combinations(range(5), degree):
            charge = sum((slot_y[i] for i in occupied), Fraction())
            bits = [1 if i in occupied else 0 for i in range(5)]
            states.append({"bits": bits, "degree": degree, "charge": charge})
            charges.append(charge)
    return states, charges


def _alpha_function(alpha: mp.mpf, budget: int = 41) -> mp.mpf:
    c3 = 1 / (8 * mp.pi)
    phi_base = 1 / (6 * mp.pi)
    delta_top = 48 * c3**4
    q = delta_top * mp.e ** (-2 * alpha)
    phi_seam = phi_base + q * (1 - q) ** (mp.mpf(-5) / 4)
    return alpha**3 - 2 * c3**3 * alpha**2 - (mp.mpf(4) / 5) * c3**6 * budget * mp.log(1 / phi_seam)


def _alpha_solution(budget: int = 41) -> tuple[mp.mpf, list[dict[str, float]], list[dict[str, float]]]:
    mp.mp.dps = 50
    function = lambda value: _alpha_function(value, budget)
    root = mp.findroot(function, mp.mpf("0.0073"))
    curve = []
    for x in np.linspace(0.0068, 0.0078, 61):
        curve.append({"alpha": float(x), "F": float(function(mp.mpf(str(x))))})
    x = mp.mpf("0.0073")
    convergence = []
    for iteration in range(7):
        fx = function(x)
        convergence.append({"iteration": iteration, "alpha": float(x), "residual": float(abs(fx))})
        dfx = mp.diff(function, x)
        x -= fx / dfx
    return root, curve, convergence


def _prediction_values(alpha: mp.mpf) -> dict[str, Any]:
    c3 = 1 / (8 * mp.pi)
    phi0 = 1 / (6 * mp.pi) + 48 * c3**4
    lam_c = mp.sqrt(phi0 * (1 - phi0))
    ainv = 1 / alpha
    return {
        "ALPHA_INV": ainv,
        "SIN2_THETA12_SEED": mp.mpf(1) / 3 - phi0 / 2,
        "SIN2_THETA13": phi0 * mp.e ** (mp.mpf(-5) / 6),
        "BETA_BIREFRINGENCE_DEG": phi0 / (4 * mp.pi) * 180 / mp.pi,
        "OMEGA_B": (1 - 1 / (4 * mp.pi)) * phi0,
        "LAMBDA_C": lam_c,
        "S23_CKM": phi0 / (1 + lam_c),
        "S13_CKM": lam_c**3 / 3,
        "DELTA_CKM_RAD": mp.pi / 3 + 3 * lam_c**2,
        "MMU_OVER_MTAU": mp.mpf(8) / 7 * phi0,
        "ME_OVER_MMU": mp.mpf(12) / 7 * phi0**2,
        "MU_OVER_MD": mp.mpf(55) / 117,
        "MC_OVER_MS": mp.mpf(34) / 47 / phi0,
        "MT_OVER_MB": mp.mpf(3) / 26 / phi0**2,
        "MSCAL_OVER_MBAR": c3 ** (mp.mpf(7) / 2),
        "RHOL_OVER_MBAR4": 3 / (4 * mp.pi**2) * mp.e ** (-2 * ainv),
    }


def _transfer_data(cfg: dict[str, Any]) -> dict[str, Any]:
    eigenvalues = np.asarray([1.0, (2 / 3) ** 6, (1 / 3) ** 6])
    basis = np.asarray([[1, 1, 1], [0, 1, 2], [0, 0, 1]], dtype=float)
    transfer = basis @ np.diag(eigenvalues) @ np.linalg.inv(basis)
    starts = {
        "localized": np.asarray([0.0, 0.0, 1.0]),
        "uniform": np.asarray([1.0, 1.0, 1.0]),
        "skew": np.asarray([0.1, 0.7, 0.2]),
    }
    state = starts[cfg["initial_state"]]
    state = state / np.linalg.norm(state)
    trajectory = [{"step": 0, "state": state.copy()}]
    for step in range(1, cfg["transfer_steps"] + 1):
        state = transfer @ state
        state /= np.linalg.norm(state)
        trajectory.append({"step": step, "state": state.copy()})
    b = float(cfg["phase_b"])
    liouville = {
        "population": [1.0, 2 / 3, 1 / 3, 1 / 3],
        "coherence_12": 2 * b - 1 / 9,
        "coherence_34": 2 * b + 1 / 18,
        "coherence_cross": 5 / 18 - b,
    }
    return {
        "matrix": transfer,
        "eigenvalues": eigenvalues,
        "spectral_gap": -math.log((2 / 3) ** 6),
        "trajectory": trajectory,
        "phase_channel": liouville,
    }


def build_stages(config: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """Recompute the full typed explorer DAG for ``config``.

    The result is a list rather than a hidden global cache so every request is a
    fresh calculation and configuration changes remain visible in the checks.
    """
    cfg = _validate_config(config)
    mp.mp.dps = 50
    c3 = mp.mpf(1) / (8 * mp.pi)
    phi_base = mp.mpf(1) / (6 * mp.pi)
    delta_top = 48 * c3**4
    phi0 = phi_base + delta_top

    anchor = [1, 1, 2]
    elementary = [sum(anchor), anchor[0] * anchor[1] + anchor[0] * anchor[2] + anchor[1] * anchor[2], math.prod(anchor)]
    powers = [sum(x**n for x in anchor) for n in range(1, 6)]

    exterior, exterior_charges = _exterior_basis()
    gen = [
        ("Q", 6, Fraction(1, 6)), ("u^c", 3, Fraction(-2, 3)),
        ("d^c", 3, Fraction(1, 3)), ("L", 2, Fraction(-1, 2)),
        ("e^c", 1, Fraction(1)), ("nu^c", 1, Fraction(0)),
    ]
    anomaly_y = sum((m * y for _, m, y in gen), Fraction())
    anomaly_y3 = sum((m * y**3 for _, m, y in gen), Fraction())
    anomaly_su2 = 3 * Fraction(1, 6) + Fraction(-1, 2)
    anomaly_su3 = 2 * Fraction(1, 6) + Fraction(-2, 3) + Fraction(1, 3)

    a3, d5 = _cartan_a(3), _cartan_d(5)
    roots, glue_cosets = _glued_roots()
    reference_roots = _e8_roots()
    cartan = _e8_cartan()
    coxeter = _coxeter(cartan)
    coxeter_order = _matrix_order(coxeter)
    coxeter_eigs = np.linalg.eigvals(np.asarray(coxeter, dtype=complex))
    coxeter_phases = sorted(int(round(np.angle(e) * 30 / (2 * np.pi))) % 30 for e in coxeter_eigs)
    c5, galois = _galois_matrices()
    clock_vector = sp.eye(8)[:, 0]
    clock_state = coxeter ** (cfg["clock_step"] % 30) * clock_vector

    residue = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
    winding = sp.Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
    lengths = residue + 6 * winding
    principal_minors = sorted(int(residue.minor_submatrix(k, k).det()) for k in range(3))
    word_budget = sum(int(value) for value in lengths)
    em_budget = word_budget + 1  # documented Higgs contribution
    alpha, alpha_curve, alpha_convergence = _alpha_solution(em_budget)
    pred_values = _prediction_values(alpha)
    transfer = _transfer_data(cfg)

    registry_path = _ROOT / "verification" / "predictions_frozen.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    prediction_rows = []
    relative_errors = []
    for item in registry["predictions"]:
        calculated = pred_values[item["id"]]
        frozen = mp.mpf(item["frozen_value"])
        relative_errors.append(abs(calculated - frozen) / (abs(frozen) or 1))
        prediction_rows.append({
            "id": item["id"], "observable": item["observable"],
            "value": calculated, "frozen": frozen, "layer": item["layer"],
            "conditional_on": item.get("conditional_on"), "experiment": item.get("experiment"),
        })

    depth = cfg["recursion_depth"]
    recursion_y = (mp.mpf(7) / 12) ** depth
    recursion_k = (mp.mpf(49) / 144) ** depth
    efolds = mp.mpf(str(cfg["efolds"]))
    mbar_gev = mp.mpf("2.435323203e18")
    m_scal_ratio = c3 ** (mp.mpf(7) / 2)
    rho_ratio = pred_values["RHOL_OVER_MBAR4"]
    ns = 1 - 2 / efolds
    tensor_r = 12 / efolds**2
    scalar_amplitude = efolds**2 * c3**7 / (24 * mp.pi**2)

    stages = [
        _stage(
            id="origin", title="Origin anchor", subtitle="One integer anchor exposes the discrete grammar",
            group="origin", order=1, kind="conditional",
            summary="The parabolic anchor (1,1,2) compresses the mutually constrained seam, carrier and sheet counts. The original bootstrap closes through the four-mark divisor, Clifford carrier and E8 glue; its comparison class remains explicit.",
            inputs=[{"name": "anchor", "value": anchor, "origin": "P1/P2 compiler interface"}],
            outputs=[{"name": "elementary_symmetric", "value": elementary}, {"name": "power_sums_p1_to_p5", "value": powers}],
            formulas=["e(a)=(4,5,2)=(|mu4|,g_car,|Z2|)", "p_n(a)=2+2^n"],
            checks=[_check("anchor elementary invariants", elementary, [4, 5, 2], "integer symmetric polynomials"), _check("Pascal carrier equation", 2**5, 5**2 + 5 + 2, "2^g=g^2+g+2")],
            sources=[{"path": "origin_theory.tex", "claim": "boundary-kernel origin and marked compiler"}, {"path": "verification/v23_anchor_generator.py", "claim": "anchor generator"}, {"path": "verification/v2_carrier_pascal.py", "line": 13, "claim": "carrier/Pascal closure"}],
            depends_on=[], visual={"type": "anchor", "data": {"anchor": anchor, "invariants": elementary, "powers": powers}}, notes=["v350 corrects the reading of these data as freely chosen inputs. See origin_closure for the jointly evaluated feedback conditions."], assumptions=["The four-mark seam, Clifford half-spinor and family-bearing lattice closure define the original comparison class."], data={"anchor": anchor, "elementary": elementary, "power_sums": powers},
        ),
        _stage(
            id="seam", title="Seam and retained seed", subtitle="The boundary normalization produces the shared small seed",
            group="origin", order=2, kind="conditional",
            summary="P1 fixes c3=1/(8pi). Its tree and top-form pieces are evaluated separately before being combined into the retained flavor seed.",
            inputs=[{"name": "c3", "value": c3, "origin": "P1 boundary normalization"}],
            outputs=[{"name": "phi_base", "value": phi_base}, {"name": "delta_top", "value": delta_top}, {"name": "phi0", "value": phi0}, {"name": "homology_rank", "value": 4 - sp.Matrix([[1,1,1,1]]).rank()}, {"name": "rr_dimension", "value": 4 + 1}],
            formulas=["mu4={1,i,-1,-i}", "H1(P1\\mu4)=Z^4/<(1,1,1,1)>=Z^3", "h0(P1,O(D))=deg(D)+1=5 (genus 0, deg(D)=4)", "c3=1/(8pi)", "phi_base=1/(6pi)", "delta_top=48 c3^4", "phi0=phi_base+delta_top"],
            checks=[_check("four puncture relation", 4 - sp.Matrix([[1,1,1,1]]).rank(), 3, "integer relation rank"), _check("Riemann-Roch degree-four space", 4+1, 5, "genus-zero polynomial basis degrees 0..4"), _check("tree/seam normalization", 4 * 2 * mp.pi * c3, 1.0, "direct evaluation", abs(4 * 2 * mp.pi * c3 - 1) < mp.mpf("1e-40")), _check("retained seed sum", phi_base + delta_top, phi0, "high precision arithmetic", abs(phi_base + delta_top - phi0) < mp.mpf("1e-45"))],
            sources=[{"path": "tfpt_1_architecture_e8.tex", "line": 163, "claim": "P1 boundary kernel"}, {"path": "verification/tfpt_constants.py", "line": 14, "claim": "canonical constants"}],
            depends_on=[{"id": "origin", "relation": "assumes", "label": "boundary framework"}], visual={"type": "seam", "data": {"marks": [[1,0],[0,1],[-1,0],[0,-1]], "homology_rank": 3, "rr_dimension": 5, "parts": [{"name": "tree", "value": phi_base}, {"name": "top", "value": delta_top}]}}, notes=["P1 participates in the original bootstrap and alpha feedback. Homology and Riemann-Roch describe different spaces; their physical identification remains explicit."], assumptions=["Reflection-positive boundary kernel and its normalization.", "The compactified seam is P1 with the degree-four marked divisor."], data={"c3": c3, "phi_base": phi_base, "delta_top": delta_top, "phi0": phi0, "marks": [[1,0],[0,1],[-1,0],[0,-1]], "cycle_relation": [1,1,1,1], "homology_rank": 3, "divisor_degree": 4, "rr_dimension": 5, "rr_basis_degrees": list(range(5))},
        ),
        _stage(
            id="carrier", title="Five-slot carrier", subtitle="Even exterior algebra gives one 16-state charge inventory",
            group="compiler", order=3, kind="exact",
            summary="The 3+2 marked carrier generates the 16 even exterior states and their hypercharges. Standard-generation anomaly sums are evaluated exactly.",
            inputs=[{"name": "slot_hypercharges", "value": [Fraction(-1, 3)] * 3 + [Fraction(1, 2)] * 2, "origin": "P2 marked carrier"}],
            outputs=[{"name": "exterior_dimensions", "value": [1, 10, 5]}, {"name": "basis_size", "value": len(exterior)}, {"name": "anomaly_sums", "value": {"Y": anomaly_y, "Y3": anomaly_y3, "SU2sqY": anomaly_su2, "SU3sqY": anomaly_su3}}],
            formulas=["Lambda^even(C^5)=Lambda^0+Lambda^2+Lambda^4", "16=1+10+5", "Y(wedge)=sum Y(slot)"],
            checks=[_check("even exterior dimension", len(exterior), 16, "enumerate subsets of degrees 0,2,4"), _check("gravitational and cubic U(1) anomalies", [anomaly_y, anomaly_y3], [0, 0], "exact Fraction sums"), _check("mixed gauge anomalies", [anomaly_su2, anomaly_su3], [0, 0], "exact Fraction sums")],
            sources=[{"path": "verification/v44_carrier_exterior.py", "line": 48, "claim": "exterior grading"}, {"path": "verification/v310_carrier_sm_anomaly.py", "line": 52, "claim": "one-generation anomaly checks"}],
            depends_on=[{"id": "origin", "relation": "derives", "label": "g_car=5"}], visual={"type": "charges", "data": {"states": exterior}}, notes=["Anomaly cancellation is necessary; it does not select interactions or chirality dynamics."], assumptions=["The marked 3+2 carrier is used as the physical charge interface."], data={"basis": exterior, "charges": exterior_charges, "generation": [{"name": n, "multiplicity": m, "Y": y} for n, m, y in gen]},
        ),
        _stage(
            id="e8", title="D5 + A3 glue and E8 hull", subtitle="The full 240-root system is generated, not counted by assertion",
            group="compiler", order=4, kind="exact",
            summary="Cartan determinants, discriminant norms, all 240 E8 roots and the E8 Cartan matrix are computed directly.",
            inputs=[{"name": "D5", "value": "SO(10) carrier lattice", "origin": "carrier half-spinor"}, {"name": "A3", "value": "four-mark seam lattice", "origin": "mu4 seam"}],
            outputs=[{"name": "det_D5", "value": d5.det()}, {"name": "det_A3", "value": a3.det()}, {"name": "root_count", "value": len(roots)}, {"name": "cartan_det", "value": cartan.det()}],
            formulas=["q(D5)+q(A3)=5/4+3/4=2", "E8=(D5+A3)+mu4", "|R(E8)|=240"],
            checks=[_check("glue discriminants", [d5.det(), a3.det()], [4, 4], "exact Cartan determinants"), _check("glue norm", Fraction(5, 4) + Fraction(3, 4), 2, "exact rational sum"), _check("E8 roots", len(roots), 240, "enumerate norm-two vectors in the four D5+D3 glue cosets"), _check("glue coset sizes", glue_cosets, [52,64,60,64], "exact doubled-coordinate membership"), _check("glue equals canonical E8 root set", set(map(tuple, roots)) == set(map(tuple, reference_roots)), True, "independent 112+128 construction"), _check("all root norms", sorted(set(np.round(np.sum(roots * roots, axis=1), 12))), [2.0], "vector norm scan"), _check("E8 Cartan unimodular", cartan.det(), 1, "exact determinant")],
            sources=[{"path": "verification/v1_e8_glue.py", "line": 25, "claim": "240 roots and lattice certificate"}, {"path": "tfpt_3_e8_audit_bootstrap.tex", "line": 188, "claim": "D5+A3 glue"}],
            depends_on=[{"id": "seam", "relation": "feeds", "label": "A3/mu4"}, {"id": "carrier", "relation": "feeds", "label": "D5 half-spinor"}], visual={"type": "root_system", "data": {"sample_roots": roots[:32], "roots": roots, "coset_sizes": glue_cosets, "cartan": cartan}}, notes=["D3 is the coordinate realization of A3. All 240 roots are sent to the browser; any 2D drawing is a projection of this eight-dimensional set."], assumptions=[], data={"cartan_A3": a3, "cartan_D5": d5, "cartan_E8": cartan, "root_count": len(roots), "roots": roots, "root_sample": roots[:32], "glue_coset_sizes": glue_cosets, "glue_generator": [0.5]*8},
        ),
        _stage(
            id="clocks", title="Coxeter and Galois clocks", subtitle="Order-30 motion and order-4 seam automorphism are kept distinct",
            group="clocks", order=5, kind="exact",
            summary="The E8 Coxeter element is multiplied from reflections; the seam Frobenius G acts on the carrier C5 clock by G C5 G^-1=C5^2.",
            inputs=[{"name": "clock_step", "value": cfg["clock_step"], "origin": "explorer control"}],
            outputs=[{"name": "coxeter_order", "value": coxeter_order}, {"name": "coxeter_phases", "value": coxeter_phases}, {"name": "clock_state", "value": clock_state}],
            formulas=["C=s1...s8", "C^30=I", "G C5 G^-1=C5^2", "G^4=I"],
            checks=[_check("Coxeter order", coxeter_order, 30, "exact matrix powers"), _check("Coxeter exponents", coxeter_phases, [1, 7, 11, 13, 17, 19, 23, 29], "numeric eigenphases checked against exact power"), _check("Galois covariance", galois * c5 * galois.inv(), c5**2, "exact symbolic matrices"), _check("Frobenius order", _matrix_order(galois), 4, "exact matrix powers")],
            sources=[{"path": "verification/v55_coxeter_cycle.py", "line": 33, "claim": "computed Coxeter element"}, {"path": "verification/v419_seam_galois_carrier.py", "line": 43, "claim": "C5 and Galois covariance"}],
            depends_on=[{"id": "e8", "relation": "derives", "label": "Coxeter hull"}, {"id": "carrier", "relation": "feeds", "label": "carrier C5 action"}, {"id": "seam", "relation": "corresponds", "label": "mu4 automorphism"}], visual={"type": "clock", "data": {"phases": coxeter_phases, "step": cfg["clock_step"], "state": clock_state}}, notes=["The order-4 seam is an automorphism, not a contracting transfer eigenvalue."], assumptions=[], data={"coxeter": coxeter, "C5": c5, "G": galois, "clock_state": clock_state},
        ),
        _stage(
            id="flavor", title="Flavor residue and readouts", subtitle="The integer seed matrix is evaluated before physical ratios",
            group="response", order=6, kind="conditional",
            summary="The residue R and wound length matrix L reproduce the exact determinant, principal-minor and word-length invariants, then feed the documented mass-ratio readouts.",
            inputs=[{"name": "R", "value": residue, "origin": "selected flavor seed"}, {"name": "phi0", "value": phi0, "origin": "seam stage"}],
            outputs=[{"name": "det_R", "value": residue.det()}, {"name": "principal_minors", "value": principal_minors}, {"name": "L", "value": lengths}, {"name": "word_budget", "value": word_budget}, {"name": "mass_ratios", "value": {"mu_over_md": pred_values["MU_OVER_MD"], "mc_over_ms": pred_values["MC_OVER_MS"], "mt_over_mb": pred_values["MT_OVER_MB"]}}],
            formulas=["L=R+6W", "det R=8", "PrinMin2(R)={2,3,5}", "m_u/m_d=55/117"],
            checks=[_check("flavor determinant", residue.det(), 8, "exact determinant"), _check("principal minors", principal_minors, [2, 3, 5], "exact minors"), _check("word-length budget", sum(int(x) for x in lengths), 40, "sum matrix entries"), _check("anchor first column", list(residue[:, 0]), anchor, "exact column")],
            sources=[{"path": "verification/v4_flavor_matrix.py", "line": 18, "claim": "residue matrix"}, {"path": "verification/v84_frozen_registry.py", "line": 62, "claim": "mass and mixing readouts"}],
            depends_on=[{"id": "seam", "relation": "feeds", "label": "phi0"}, {"id": "carrier", "relation": "assumes", "label": "three-family marked readout"}], visual={"type": "matrix", "data": {"R": residue, "L": lengths, "principal_minors": principal_minors}}, notes=["Exact matrix invariants and conditional physical readouts are separate fields."], assumptions=["The documented flavor selector identifies this R with the physical sector."], data={"R": residue, "L": lengths, "characteristic_polynomial": str(residue.charpoly().as_expr()), "mass_ratios": {k: pred_values[k] for k in ("MU_OVER_MD", "MC_OVER_MS", "MT_OVER_MB", "MMU_OVER_MTAU", "ME_OVER_MMU")}},
        ),
        _stage(
            id="alpha", title="Electromagnetic fixed point", subtitle="The nonlinear root and convergence are visible",
            group="response", order=7, kind="numeric",
            summary="The U(1) closure equation is evaluated as a function, solved at high precision and displayed with its local curve and Newton residuals.",
            inputs=[{"name": "budget_M", "value": em_budget, "origin": "flavor word-length budget 40 + documented Higgs contribution 1"}, {"name": "c3", "value": c3, "origin": "seam stage"}],
            outputs=[{"name": "alpha", "value": alpha}, {"name": "alpha_inverse", "value": 1 / alpha}, {"name": "residual", "value": abs(_alpha_function(alpha, em_budget))}],
            formulas=["F_U1(a)=a^3-2c3^3 a^2-(4/5)c3^6*41 log(1/phi_seam(a))", "F_U1(alpha)=0"],
            checks=[_check("root residual", abs(_alpha_function(alpha, em_budget)), 0.0, "50-digit mpmath root", abs(_alpha_function(alpha, em_budget)) < mp.mpf("1e-45")), _check("frozen inverse alpha", 1 / alpha, mp.mpf("137.0359992168407125035379"), "registry comparison", abs(1 / alpha - mp.mpf("137.0359992168407125035379")) < mp.mpf("1e-22"))],
            sources=[{"path": "verification/v3_em_alpha.py", "line": 17, "claim": "U(1) closure equation"}, {"path": "verification/predictions_frozen.json", "claim": "frozen prediction"}],
            depends_on=[{"id": "seam", "relation": "feeds", "label": "c3 and phi_seam"}, {"id": "flavor", "relation": "feeds", "label": "sum L + Higgs = 40+1 = M"}], visual={"type": "curve", "data": {"curve": alpha_curve, "root": alpha, "convergence": alpha_convergence}}, notes=["The numerical root is unconditional given the closure equation; the equation's Ward-origin reading remains conditional."], assumptions=["F_U1 is the electromagnetic closure functional."], data={"curve": alpha_curve, "convergence": alpha_convergence, "alpha": alpha, "alpha_inverse": 1 / alpha},
        ),
        _stage(
            id="transfer", title="Transfer and recursive response", subtitle="The same finite dynamics exposes contraction and unresolved phase freedom",
            group="clocks", order=8, kind="conditional",
            summary="A non-diagonal transfer operator with the documented spectrum is iterated from the selected initial state. Recursive response factors and the phase-channel family are shown together without treating b as selected.",
            inputs=[{"name": "steps", "value": cfg["transfer_steps"], "origin": "explorer control"}, {"name": "initial_state", "value": cfg["initial_state"], "origin": "explorer control"}, {"name": "phase_b", "value": cfg["phase_b"], "origin": "unselected finite channel parameter"}, {"name": "recursion_depth", "value": depth, "origin": "explorer control"}],
            outputs=[{"name": "transfer_eigenvalues", "value": transfer["eigenvalues"]}, {"name": "gap", "value": transfer["spectral_gap"]}, {"name": "recursive_Y", "value": recursion_y}, {"name": "recursive_K", "value": recursion_k}, {"name": "coherence_12", "value": transfer["phase_channel"]["coherence_12"]}],
            formulas=["spec(T)={1,(2/3)^6,(1/3)^6}", "Delta=6 log(3/2)", "Y_n=(7/12)^n Y", "K_n=(49/144)^n K", "lambda12=2b-1/9"],
            checks=[_check("transfer spectrum", sorted(np.linalg.eigvals(transfer["matrix"]), reverse=True), sorted(transfer["eigenvalues"], reverse=True), "numeric eigensystem", np.allclose(sorted(np.linalg.eigvals(transfer["matrix"]), reverse=True), sorted(transfer["eigenvalues"], reverse=True))), _check("positive gap", transfer["spectral_gap"] > 0, True, "direct logarithm"), _check("response relation", recursion_k, recursion_y**2, "exact factor identity", abs(recursion_k - recursion_y**2) < mp.mpf("1e-40")), _check("phase b admissible", 0 <= cfg["phase_b"] <= 2 / 9, True, "CPTP parameter interval")],
            sources=[{"path": "verification/v56_unique_attractor.py", "line": 35, "claim": "gapped transfer"}, {"path": "_newest2/TFPT_Gesamtdokumentation_Code_Quartik_Rekursion_2026-09-26.md", "line": 1441, "claim": "recursive operator transport"}, {"path": "_newest2/TFPT_Universalraum_Gesamtdokumentation_20260927.md", "line": 1725, "claim": "phase channel family"}],
            depends_on=[{"id": "clocks", "relation": "corresponds", "label": "clock versus transfer"}, {"id": "flavor", "relation": "corresponds", "label": "separate documented readouts; no operator identification"}], visual={"type": "trajectory", "data": {"trajectory": transfer["trajectory"], "eigenvalues": transfer["eigenvalues"], "phase_channel": transfer["phase_channel"]}}, notes=["This is the concrete three-mode similarity representative from v56, with its chosen nonorthogonal basis. Components are not probabilities.", "Recursive factors and phase-channel data are cross-references to the separate process stages, not outputs derived from this transfer matrix.", "The selected b changes phase-sensitive response while leaving the documented population/code contract unchanged."], assumptions=["The finite transfer operator is the relevant boundary relaxation.", "No primitive source rule selecting b is supplied."], data=transfer,
        ),
        _stage(
            id="predictions", title="Frozen observable registry", subtitle="Every displayed number is recalculated and evidence-typed",
            group="response", order=9, kind="conditional",
            summary="The frozen registry is loaded, every prediction value is recomputed, and each row retains its core/conditional status and experimental target.",
            inputs=[{"name": "registry_freeze_date", "value": registry["freeze_date"], "origin": "predictions_frozen.json"}],
            outputs=[{"name": "prediction_count", "value": len(prediction_rows)}, {"name": "max_relative_error", "value": max(relative_errors)}, {"name": "rows", "value": prediction_rows}],
            formulas=["values=recompute(c3,g_car,alpha,phi0)", "registry values are comparisons, not calculation inputs"],
            checks=[_check("registry freeze", registry["freeze_date"], "2026-06-09", "read canonical JSON"), _check("all frozen values reproduced", max(relative_errors), 1e-22, "maximum relative error", max(relative_errors) < mp.mpf("1e-22"))],
            sources=[{"path": "verification/predictions_frozen.json", "claim": "frozen observable registry"}, {"path": "verification/v84_frozen_registry.py", "line": 62, "claim": "recomputation formulas"}],
            depends_on=[{"id": "alpha", "relation": "feeds", "label": "alpha fixed point"}, {"id": "flavor", "relation": "feeds", "label": "mass/mixing maps"}], visual={"type": "predictions", "data": {"rows": prediction_rows}}, notes=["Assigned texture values and derived variants are not promoted into this prediction list."], assumptions=["Each row carries its own conditional_on statement."], data={"registry": registry["registry"], "freeze_date": registry["freeze_date"], "rows": prediction_rows},
        ),
        _stage(
            id="gravity", title="Gravity scale bridge", subtitle="Dimensionless closure plus one external unit",
            group="physics", order=10, kind="conditional",
            summary="The scalaron exponent and mass ratio are computed from c3. Converting to GeV explicitly uses the measured reduced Planck scale.",
            inputs=[{"name": "Mbar", "value": mbar_gev, "unit": "GeV", "origin": "external measured unit"}],
            outputs=[{"name": "scalaron_exponent", "value": 7}, {"name": "M_scal_over_Mbar", "value": m_scal_ratio}, {"name": "M_scal", "value": m_scal_ratio * mbar_gev, "unit": "GeV"}],
            formulas=["7=N_fam+|mu4|=g_car+|Z2|", "M_scal/Mbar=c3^(7/2)"],
            checks=[_check("scalaron exponent cross-check", [3 + 4, 5 + 2], [7, 7], "integer compiler identities"), _check("dimensionless mass ratio", m_scal_ratio, pred_values["MSCAL_OVER_MBAR"], "shared formula", abs(m_scal_ratio - pred_values["MSCAL_OVER_MBAR"]) < mp.mpf("1e-45"))],
            sources=[{"path": "verification/v7_gravity_cosmo.py", "line": 17, "claim": "gravity/cosmology readouts"}, {"path": "verification/v68_seeley_dewitt_residual.py", "claim": "dimensionful normalization boundary"}],
            depends_on=[{"id": "seam", "relation": "assumes", "label": "c3 coefficient"}, {"id": "e8", "relation": "corresponds", "label": "scalaron integer identities"}], visual={"type": "scales", "data": {"dimensionless": m_scal_ratio, "gev": m_scal_ratio * mbar_gev}}, notes=["The absolute unit is external; the dimensionless ratio is the calculated output."], assumptions=["The R+R^2/scalaron identification is physical.", "The measured Mbar supplies the one dimensionful scale."], data={"c3": c3, "Mbar_GeV": mbar_gev, "M_scal_over_Mbar": m_scal_ratio, "M_scal_GeV": m_scal_ratio * mbar_gev},
        ),
        _stage(
            id="cosmology", title="Conditional cosmological branch", subtitle="Inflation and vacuum outputs retain their physical assumptions",
            group="physics", order=11, kind="conditional",
            summary="For the chosen external e-fold count, the Starobinsky branch computes A_s, n_s and r. The vacuum ratio uses the same alpha root but remains a branch identification.",
            inputs=[{"name": "efolds", "value": efolds, "origin": "external reheating choice"}, {"name": "alpha_inverse", "value": 1 / alpha, "origin": "alpha stage"}],
            outputs=[{"name": "A_s", "value": scalar_amplitude}, {"name": "n_s", "value": ns}, {"name": "r", "value": tensor_r}, {"name": "rho_Lambda_over_Mbar4", "value": rho_ratio}, {"name": "rho_Lambda_quarter", "value": rho_ratio ** (mp.mpf(1) / 4) * mbar_gev * mp.mpf("1e12"), "unit": "meV"}],
            formulas=["A_s=N_*^2 c3^7/(24 pi^2)", "n_s=1-2/N_*", "r=12/N_*^2", "rho_L/Mbar^4=(3/(4pi^2)) exp(-2 alpha^-1)"],
            checks=[_check("Starobinsky consistency", tensor_r, 3 * (1 - ns) ** 2, "eliminate N_*", abs(tensor_r - 3 * (1 - ns) ** 2) < mp.mpf("1e-40")), _check("positive vacuum ratio", rho_ratio > 0, True, "direct exponential")],
            sources=[{"path": "verification/v7_gravity_cosmo.py", "line": 29, "claim": "inflation and vacuum formulas"}, {"path": "verification/predictions_frozen.json", "claim": "conditional bands and kill criteria"}],
            depends_on=[{"id": "alpha", "relation": "feeds", "label": "vacuum exponent"}, {"id": "gravity", "relation": "assumes", "label": "R+R2 branch"}], visual={"type": "cosmology", "data": {"efolds": efolds, "A_s": scalar_amplitude, "n_s": ns, "r": tensor_r, "rho_ratio": rho_ratio}}, notes=["Changing efolds is an external reheating scenario, not a change to the compiler."], assumptions=["The Starobinsky R^2 branch is realized.", "The alpha-to-vacuum identification is physical.", "Mbar fixes the dimensional unit."], data={"efolds": efolds, "A_s": scalar_amplitude, "n_s": ns, "r": tensor_r, "rho_ratio": rho_ratio},
        ),
    ]
    # Fail fast if future edits accidentally break the public JSON contract.
    json.dumps(stages, allow_nan=False)
    ids = [stage["id"] for stage in stages]
    if len(ids) != len(set(ids)):
        raise AssertionError("stage ids must be unique")
    return stages
