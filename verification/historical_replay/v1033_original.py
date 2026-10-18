#!/usr/bin/env python3
"""Round-7 microscopic QWZ disorder-insertion probe.

Construct an actual boundary-condition changer on the QWZ CAR Fock space
tensored with one four-level flux-link register.  A sharp matter charge
string dresses the register shift; its commutator with the register-coupled
QWZ Hamiltonian is supported only on the other endpoint of the string.

The common quarter twist of eight complex edge channels has minimal
q=(1/4)^8 and h=1/4, not the sourced lambda weight h_lambda=1.  Floating
scaling checks below are diagnostics, not tail theorems.  NO RH CLAIM.

Port provenance: native verification port of
`toe_round7_charged_disorder/charged_disorder_probe.py`
(source SHA-256 7b53a74ea58629a6925c854290feb507932b1f2a174e80ba7cefe3a82e5dc951).
The initial port changed only harness integration, repository lookup, and
execution lifecycle.  The 2026-09-06 amendment replaces an eigensolver-selected
zero-mode vacuum by its basis-independent fixed-particle ground-space mixture
and reports the full one-body energy interval over pure ground-state fillings.
"""
from __future__ import annotations

import ast
import importlib.util
import os
import sys
from dataclasses import dataclass, field
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp

from tfpt_constants import check as suite_check, reset, summary

DEFAULT_REPO = Path(__file__).resolve().parents[1]
REPO = Path(os.environ.get("TFPT_REPO", str(DEFAULT_REPO))).resolve()


@dataclass
class CheckBook:
    checks: dict[str, list[tuple[str, bool]]] = field(
        default_factory=lambda: {
            "source_contract": [],
            "symbolic_exact": [],
            "finite_qwz": [],
            "scaling_diagnostic": [],
        }
    )

    def check(self, kind: str, name: str, condition: bool) -> None:
        passed = bool(condition)
        self.checks[kind].append((name, passed))
        suite_check(f"[{kind}] {name}", passed)

    def counts(self) -> dict[str, dict[str, int]]:
        return {
            kind: {
                "passed": sum(ok for _, ok in rows),
                "failed": sum(not ok for _, ok in rows),
                "total": len(rows),
            }
            for kind, rows in self.checks.items()
        }

    def all_pass(self) -> bool:
        return all(ok for rows in self.checks.values() for _, ok in rows)


BOOK = CheckBook()
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TX = SX / (2j) - SZ / 2
TY = SY / (2j) - SZ / 2


def read(relative: str) -> str:
    return (REPO / relative).read_text(encoding="utf-8")


def function_node(source: str, name: str) -> ast.FunctionDef:
    hits = [
        node for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(hits) != 1:
        raise AssertionError(f"expected one function {name}, found {len(hits)}")
    return hits[0]


def source_contract_audit() -> None:
    v983 = read("verification/v983_simple_current_generator.py")
    v988 = read("verification/v988_psi_lambda_reduction.py")
    memo = read("articles/2026-08-30/mmst_charged_scaling_limit_en.tex")
    cylinder = ast.get_source_segment(v988, function_node(v988, "qwz_cylinder"))
    BOOK.check(
        "source_contract",
        "v988 uses the frozen QWZ TX and TY hops",
        "TX = (SX / (2j) - SZ / 2)" in v988
        and "TY = (SY / (2j) - SZ / 2)" in v988,
    )
    BOOK.check(
        "source_contract",
        "v988 puts scalar i^r only on the periodic x seam",
        "ph = 1j ** k_twist" in cylinder
        and "amp = ph if x == Nx - 1 else 1.0" in cylinder
        and "if y + 1 < Ny" in cylinder,
    )
    BOOK.check(
        "source_contract",
        "artifact overrides v988's Ny=6 campaign default with manuscript Ny=8",
        "NY, WIN = 6, 4" in v988
        and "fixed open width $N_y=8$" in memo,
    )
    BOOK.check(
        "source_contract",
        "charged-limit manuscript states the quarter momentum shift",
        "fixed open width $N_y=8$" in memo
        and r"n+\frac r4" in memo
        and "boundary phase $i^r$" in memo,
    )
    BOOK.check(
        "source_contract",
        "source uses sixteen Majoranas and eight complex bosons",
        "sixteen Majorana copies" in memo
        and "Each complex-fermion" in memo
        and "pair gives one boson" in memo,
    )
    BOOK.check(
        "source_contract",
        "target lambda has norm squared two and h=1",
        "lambda = (omega_s, omega_f)" in v983
        and "|lambda|^2 = 2" in v983
        and "h_lambda = |lambda|^2/2 = 1" in v983,
    )
    BOOK.check(
        "source_contract",
        "support-preserving microscopic realization remains fenced",
        "support-preserving microscopic realization" in memo
        and "FE-GEN or an exact" in memo,
    )


def qwz_cylinder(nx: int, ny: int, mass: float, sector: int) -> np.ndarray:
    """Source-identical finite QWZ cylinder used for independent checks."""
    dim = 2 * nx * ny
    h = np.zeros((dim, dim), dtype=complex)

    def sl(x: int, y: int) -> int:
        return 2 * ((x % nx) * ny + y)

    phase = 1j ** sector
    for x in range(nx):
        for y in range(ny):
            i = sl(x, y)
            h[i:i + 2, i:i + 2] += mass * SZ
            j = sl(x + 1, y)
            amp = phase if x == nx - 1 else 1.0
            h[j:j + 2, i:i + 2] += amp * TX
            h[i:i + 2, j:j + 2] += np.conj(amp) * TX.conj().T
            if y + 1 < ny:
                j = sl(x, y + 1)
                h[j:j + 2, i:i + 2] += TY
                h[i:i + 2, j:j + 2] += TY.conj().T
    return h


def load_source_qwz():
    verification = REPO / "verification"
    sys.path.insert(0, str(verification))
    try:
        spec = importlib.util.spec_from_file_location(
            "round7_frozen_v988", verification / "v988_psi_lambda_reduction.py"
        )
        if spec is None or spec.loader is None:
            raise RuntimeError("cannot load v988")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.qwz_cylinder
    finally:
        sys.path.pop(0)


def matrix_unit(d: int, row: int, col: int) -> sp.Matrix:
    out = sp.zeros(d)
    out[row, col] = 1
    return out


def symbolic_construction() -> None:
    z = sp.diag(1, sp.I, -1, -sp.I)
    x = sum(
        (matrix_unit(4, (r + 1) % 4, r) for r in range(4)), sp.zeros(4)
    )
    projectors = [matrix_unit(4, r, r) for r in range(4)]
    BOOK.check(
        "symbolic_exact",
        "local flux register is a Z4 Weyl pair",
        x**4 == sp.eye(4) and z**4 == sp.eye(4)
        and z * x * z.conjugate().T == sp.I * x,
    )
    BOOK.check(
        "symbolic_exact",
        "X and X* have all forward and reverse charged corners",
        all(
            (projectors[(r + 1) % 4] * x * projectors[r]).rank() == 1
            and (projectors[r] * x.conjugate().T
                 * projectors[(r + 1) % 4]).rank() == 1
            for r in range(4)
        ),
    )
    gamma_i = sp.diag(1, sp.I)
    parity = sp.kronecker_product(sp.eye(4), sp.diag(1, -1))
    disorder = sp.kronecker_product(x, gamma_i)
    clock = sp.kronecker_product(z, sp.eye(2))
    BOOK.check(
        "symbolic_exact",
        "flux shift times number-rotation string has order four",
        disorder**4 == sp.eye(8),
    )
    BOOK.check(
        "symbolic_exact",
        "disorder string is even under canonical fermion parity",
        parity * disorder == disorder * parity,
    )
    BOOK.check(
        "symbolic_exact",
        "parity evenness preserves dual Z4 charge one",
        clock * disorder * clock.conjugate().T == sp.I * disorder,
    )

    quarter = sp.Rational(1, 4)
    q_common = sp.Matrix([quarter] * 8)
    omega_s = sp.Matrix([sp.Rational(1, 2)] * 5)
    omega_f = sp.Matrix(
        [sp.Rational(3, 4)] + [sp.Rational(-1, 4)] * 3
    )
    lambda_norm2 = omega_s.dot(omega_s) + omega_f.dot(omega_f)
    BOOK.check(
        "symbolic_exact",
        "minimal common quarter twist of eight complex channels has h=1/4",
        q_common.dot(q_common) == sp.Rational(1, 2)
        and q_common.dot(q_common) / 2 == sp.Rational(1, 4),
    )
    BOOK.check(
        "symbolic_exact",
        "D5+A3 lambda instead has h=5/8+3/8=1",
        omega_s.dot(omega_s) == sp.Rational(5, 4)
        and omega_f.dot(omega_f) == sp.Rational(3, 4)
        and lambda_norm2 == 2 and lambda_norm2 / 2 == 1,
    )
    BOOK.check(
        "symbolic_exact",
        "lambda phases require Z^2 on D5 and Z^-1 on A3",
        all(sp.simplify(sp.exp(2 * sp.pi * sp.I * q) + 1) == 0
                for q in omega_s)
        and all(sp.simplify(sp.exp(2 * sp.pi * sp.I * q) + sp.I) == 0
                for q in omega_f),
    )
    BOOK.check(
        "symbolic_exact",
        "common quarter twist has order four and its square order two",
        all((4 * q).q == 1 for q in q_common)
        and any((2 * q).q != 1 for q in q_common)
        and all((2 * (2 * q)).q == 1 for q in q_common),
    )
    q_excited = sp.Matrix([sp.Rational(5, 4)] + [quarter] * 7)
    dressing = q_excited - q_common
    BOOK.check(
        "symbolic_exact",
        "matching h=1 in the scalar phase class needs odd fermion dressing",
        q_excited.dot(q_excited) == 2
        and all(sp.simplify(sp.exp(2 * sp.pi * sp.I * q_excited[j]) - sp.I) == 0
                for j in range(8))
        and sum(int(v) for v in dressing) % 2 == 1,
    )
    BOOK.check(
        "symbolic_exact",
        "general norm-two scalar-phase dressing has odd parity by mod-two census",
        all(
            sum(bits) % 2 == 1
            for bits in product((0, 1), repeat=8)
            if (2 * sum(bit * bit for bit in bits) + sum(bits) - 3) % 2 == 0
        ),
    )
    a3_min = sp.Matrix([sp.Rational(-1, 4)] * 4)
    a3_endpoint = sp.Matrix([1, 0, 0, 0])
    BOOK.check(
        "symbolic_exact",
        "A3 fundamental is quarter disorder plus one endpoint fermion",
        a3_min + a3_endpoint == omega_f
        and a3_min.dot(a3_min) / 2 == sp.Rational(1, 8)
        and omega_f.dot(omega_f) / 2 == sp.Rational(3, 8),
    )


def seam_forward(nx: int, ny: int) -> np.ndarray:
    out = np.zeros((2 * nx * ny, 2 * nx * ny), dtype=complex)
    for y in range(ny):
        i = 2 * ((nx - 1) * ny + y)
        j = 2 * y
        out[j:j + 2, i:i + 2] = TX
    return out


def register_hamiltonian(nx: int, ny: int) -> tuple[np.ndarray, np.ndarray]:
    hs = [qwz_cylinder(nx, ny, 1.0, r) for r in range(4)]
    dim = hs[0].shape[0]
    direct = np.zeros((4 * dim, 4 * dim), dtype=complex)
    for r, h in enumerate(hs):
        direct[r * dim:(r + 1) * dim, r * dim:(r + 1) * dim] = h
    forward = seam_forward(nx, ny)
    base = hs[0] - forward - forward.conj().T
    z = np.diag([1j**r for r in range(4)])
    linked = (
        np.kron(np.eye(4), base)
        + np.kron(z, forward)
        + np.kron(z.conj().T, forward.conj().T)
    )
    return direct, linked


def sharp_arc_phase(nx: int, ny: int, endpoint: int) -> np.ndarray:
    phase = np.ones(2 * nx * ny, dtype=complex)
    phase[:2 * (endpoint + 1) * ny] = 1j
    return np.diag(phase)


def smooth_phase(nx: int, ny: int) -> np.ndarray:
    phi = np.pi / 2
    site_phase = np.exp(1j * phi * (1 - np.arange(nx) / nx))
    return np.diag(np.repeat(site_phase, 2 * ny))


def endpoint_mask(nx: int, ny: int, endpoint: int) -> np.ndarray:
    mask = np.zeros((2 * nx * ny, 2 * nx * ny), dtype=bool)
    for y in range(ny):
        i = 2 * (endpoint * ny + y)
        j = 2 * ((endpoint + 1) * ny + y)
        mask[j:j + 2, i:i + 2] = True
        mask[i:i + 2, j:j + 2] = True
    return mask


def finite_qwz_checks() -> None:
    source_qwz = load_source_qwz()
    BOOK.check(
        "finite_qwz",
        "independent builder equals executable v988 at Ny=8",
        all(np.array_equal(qwz_cylinder(5, 8, 1.0, r),
                           source_qwz(5, 8, 1.0, r)) for r in range(4)),
    )
    reconstructed = fourier_reconstruction(5, 8, 1)
    BOOK.check(
        "finite_qwz",
        "Bloch blocks reconstruct the imported r=1 seam Hamiltonian",
        np.allclose(reconstructed, source_qwz(5, 8, 1.0, 1), atol=2e-13),
    )
    direct, linked = register_hamiltonian(5, 8)
    BOOK.check(
        "finite_qwz",
        "register-coupled hopping equals direct sum_r H_QWZ(r)",
        np.array_equal(direct, linked),
    )
    phases = np.exp(1j * np.array([0.13, -0.72, 1.11, 0.44, -0.31]))
    links = np.array([1, 1, 1, 1, 1j], dtype=complex)
    transformed = np.array([
        links[x] * phases[(x + 1) % 5] * phases[x].conjugate()
        for x in range(5)
    ])
    BOOK.check(
        "finite_qwz",
        "matter-only onsite gauge preserves total QWZ holonomy",
        np.allclose(np.prod(transformed), np.prod(links), atol=1e-14)
        and np.allclose(np.prod(links), 1j, atol=1e-14),
    )

    endpoint = 2
    u = sharp_arc_phase(5, 8, endpoint)
    mask = endpoint_mask(5, 8, endpoint)
    residuals = [
        qwz_cylinder(5, 8, 1.0, (r + 1) % 4) @ u
        - u @ qwz_cylinder(5, 8, 1.0, r)
        for r in range(4)
    ]
    BOOK.check(
        "finite_qwz",
        "sharp flux-string commutator lives only at far endpoint",
        all(
            np.count_nonzero(np.abs(residual[~mask]) > 1e-13) == 0
            and np.count_nonzero(np.abs(residual[mask]) > 1e-13) == 64
            for residual in residuals
        ),
    )
    BOOK.check(
        "finite_qwz",
        "endpoint defect has rank 2*Ny and norm sqrt(2)",
        all(
            np.linalg.matrix_rank(residual, tol=1e-12) == 16
            and abs(np.linalg.norm(residual, 2) - np.sqrt(2)) < 1e-12
            for residual in residuals
        ),
    )
    dim = 2 * 5 * 8
    shift = np.roll(np.eye(4), 1, axis=0).astype(complex)
    full_disorder = np.kron(shift, u)
    full_commutator = direct @ full_disorder - full_disorder @ direct
    expected = np.zeros_like(full_commutator)
    for r, residual in enumerate(residuals):
        row = (r + 1) % 4
        expected[row * dim:(row + 1) * dim,
                 r * dim:(r + 1) * dim] = residual
    BOOK.check(
        "finite_qwz",
        "full common-Hilbert commutator equals endpoint residual blocks",
        np.allclose(full_commutator, expected, atol=1e-13),
    )


def half_filled_ground_space(
    h: np.ndarray,
) -> tuple[float, np.ndarray, np.ndarray, int]:
    """Particle-hole-symmetric half filling, including an unresolved zero space.

    C=P_-+(m/d)P_0 is the one-body covariance of the uniform mixture over
    rank-m fillings of the d-dimensional zero eigenspace.  It is not renamed
    a pure Slater vacuum.  The numerical cluster threshold must be separated
    from every nonzero level; this is a finite diagnostic, not an interval proof.
    """
    vals, vecs = np.linalg.eigh(h)
    nocc = h.shape[0] // 2
    tolerance = 64 * h.shape[0] * np.finfo(float).eps * max(1.0, np.linalg.norm(h, np.inf))
    negative = vals < -tolerance
    zero = np.abs(vals) <= tolerance
    zero_vectors = vecs[:, zero]
    dimension = zero_vectors.shape[1]
    remaining = nocc - int(np.count_nonzero(negative))
    if not 0 <= remaining <= dimension:
        raise ValueError("Half filling is not supported by the zero-energy cluster")
    outside = np.abs(vals[~zero])
    if outside.size and float(np.min(outside)) <= 100 * tolerance:
        raise ValueError("Zero-energy cluster is not numerically isolated")
    occupied = vecs[:, negative]
    covariance = occupied @ occupied.conj().T
    if dimension:
        covariance += (remaining / dimension) * zero_vectors @ zero_vectors.conj().T
    return float(vals[:nocc].sum()), covariance, zero_vectors, remaining


def half_filled_data(h: np.ndarray) -> tuple[float, np.ndarray]:
    energy, covariance, _zero_vectors, _remaining = half_filled_ground_space(h)
    return energy, covariance


def ground_space_excess_bounds(
    covariance: np.ndarray, zero_vectors: np.ndarray, remaining: int,
    transformed_target: np.ndarray, target_ground_energy: float,
) -> tuple[float, float]:
    """Extrema over ALL rank-m zero-space fillings (Ky Fan variational bound)."""
    mean = float(np.trace(covariance @ transformed_target).real - target_ground_energy)
    dimension = zero_vectors.shape[1]
    if not dimension:
        return mean, mean
    compressed = zero_vectors.conj().T @ transformed_target @ zero_vectors
    values = np.linalg.eigvalsh((compressed + compressed.conj().T) / 2)
    fixed = mean - (remaining / dimension) * float(values.sum())
    low = float(values[:remaining].sum())
    high = float(values[-remaining:].sum()) if remaining else 0.0
    return fixed + low, fixed + high


def strip_at_momentum(k: float, ny: int = 8) -> np.ndarray:
    h = np.zeros((2 * ny, 2 * ny), dtype=complex)
    onsite = SZ + np.exp(-1j * k) * TX + np.exp(1j * k) * TX.conj().T
    for y in range(ny):
        i = 2 * y
        h[i:i + 2, i:i + 2] += onsite
        if y + 1 < ny:
            j = 2 * (y + 1)
            h[j:j + 2, i:i + 2] += TY
            h[i:i + 2, j:j + 2] += TY.conj().T
    return h


def sector_momentum(nx: int, mode: int, sector: int) -> float:
    return (2 * np.pi * mode - sector * np.pi / 2) / nx


def fourier_reconstruction(nx: int, ny: int, sector: int) -> np.ndarray:
    dim = 2 * nx * ny
    transform = np.zeros((dim, dim), dtype=complex)
    blocks = np.zeros((dim, dim), dtype=complex)
    for mode in range(nx):
        k = sector_momentum(nx, mode, sector)
        for x in range(nx):
            phase = np.exp(1j * k * x) / np.sqrt(nx)
            for y in range(ny):
                row = 2 * (x * ny + y)
                col = 2 * (mode * ny + y)
                transform[row:row + 2, col:col + 2] = phase * np.eye(2)
        start = 2 * mode * ny
        blocks[start:start + 2 * ny, start:start + 2 * ny] = strip_at_momentum(k, ny)
    return transform @ blocks @ transform.conj().T


def momentum_ground_energy(nx: int, sector: int, ny: int = 8) -> float:
    values: list[float] = []
    for n in range(nx):
        k = sector_momentum(nx, n, sector)
        values.extend(np.linalg.eigvalsh(strip_at_momentum(k, ny)))
    values.sort()
    return float(sum(values[:nx * ny]))


def scaling_diagnostics() -> None:
    nxs = (16, 24, 32, 48, 64)
    sharp_excess = []
    sharp_intervals = []
    smooth_excess_scaled = []
    smooth_intervals_scaled = []
    smooth_comm_scaled = []
    for nx in nxs:
        h0 = qwz_cylinder(nx, 8, 1.0, 0)
        h1 = qwz_cylinder(nx, 8, 1.0, 1)
        e0, c0, zero_vectors, remaining = half_filled_ground_space(h0)
        e1, _ = half_filled_data(h1)
        sharp = sharp_arc_phase(nx, 8, nx // 2 - 1)
        sharp_state = sharp @ c0 @ sharp.conj().T
        sharp_excess.append(float(np.trace(sharp_state @ h1).real - e1))
        sharp_intervals.append(ground_space_excess_bounds(
            c0, zero_vectors, remaining, sharp.conj().T @ h1 @ sharp, e1))
        smooth = smooth_phase(nx, 8)
        smooth_state = smooth @ c0 @ smooth.conj().T
        smooth_excess = float(np.trace(smooth_state @ h1).real - e1)
        smooth_excess_scaled.append(nx * smooth_excess)
        bounds = ground_space_excess_bounds(
            c0, zero_vectors, remaining, smooth.conj().T @ h1 @ smooth, e1)
        smooth_intervals_scaled.append(tuple(nx * value for value in bounds))
        residual = h1 @ smooth - smooth @ h0
        smooth_comm_scaled.append(nx * np.linalg.norm(residual, 2))
        BOOK.check(
            "scaling_diagnostic",
            f"half-filled energies are finite at Nx={nx}",
            np.isfinite(e0) and np.isfinite(e1),
        )
    BOOK.check(
        "scaling_diagnostic",
        "sharp endpoint energy is bounded across the complete half-filled ground space on the sampled sizes",
        all(4.0 < low <= high < 5.0 for low, high in sharp_intervals)
        and abs(sharp_excess[-1] - sharp_excess[-2]) < 0.03,
    )
    BOOK.check(
        "scaling_diagnostic",
        "smooth nonlocal dressing has one-body commutator pi/(2N)",
        max(abs(value - np.pi / 2) for value in smooth_comm_scaled) < 7e-4,
    )
    BOOK.check(
        "scaling_diagnostic",
        "smooth ground-space mixture and all pure fillings have measured O(1/N) excess",
        max(smooth_excess_scaled) - min(smooth_excess_scaled) < 0.02
        and 6.88 < smooth_excess_scaled[-1] < 6.93
        and all(5.2 < low <= mean <= high < 8.6
                for (low, high), mean in zip(smooth_intervals_scaled, smooth_excess_scaled)),
    )
    casimir = []
    for nx in (32, 64, 128, 256):
        delta = momentum_ground_energy(nx, 1) - momentum_ground_energy(nx, 0)
        casimir.append(nx * delta / (2 * np.pi))
    BOOK.check(
        "scaling_diagnostic",
        "one-copy two-edge vacuum shift approaches -3/16",
        abs(casimir[-1] + 3 / 16) < 2e-6
        and all(abs(casimir[j + 1] + 3 / 16)
                < abs(casimir[j] + 3 / 16)
                for j in range(len(casimir) - 1)),
    )
    print("DIAGNOSTIC sharp_excess", [f"{x:.12f}" for x in sharp_excess])
    print("DIAGNOSTIC sharp_ground_space_intervals", sharp_intervals)
    print("DIAGNOSTIC N_times_smooth_excess",
          [f"{x:.12f}" for x in smooth_excess_scaled])
    print("DIAGNOSTIC N_times_smooth_ground_space_intervals", smooth_intervals_scaled)
    print("DIAGNOSTIC N_times_smooth_comm_norm",
          [f"{x:.12f}" for x in smooth_comm_scaled])
    print("DIAGNOSTIC N_deltaE_over_2pi", [f"{x:.12f}" for x in casimir])


def run() -> int:
    global BOOK
    reset()
    BOOK = CheckBook()
    source_contract_audit()
    symbolic_construction()
    finite_qwz_checks()
    scaling_diagnostics()
    counts = BOOK.counts()
    print("COUNTS", counts)
    print("TOTAL", sum(row["total"] for row in counts.values()))
    print("VERDICT", "PASS" if BOOK.all_pass() else "FAIL")
    return summary("v1033 charged disorder")


if __name__ == "__main__":
    raise SystemExit(run())
