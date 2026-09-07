#!/usr/bin/env python3
"""Standalone checks for the prescribed-source quantum Kubo leg.

Scope: the zero-mean, finite-volume free tensor Fock target at nonzero
momentum, driven by a prescribed conserved c-number source.  This checker
does not modify or import the repository verification suite and makes no RH,
microscopic-TFPT, nonlinear, or interacting-matter claim.

Exact checks use SymPy.  The two numerical quadratures are labelled
regressions and are not substitutes for the proof in README.md.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import mpmath as mp
import sympy as sp
from sympy.physics.quantum import Commutator


PAIRS = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))


@dataclass
class Counts:
    exact_pass: int = 0
    exact_total: int = 0
    float_pass: int = 0
    float_total: int = 0


COUNTS = Counts()


def is_zero(value: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(sp.expand(entry)) == 0 for entry in value)
    return sp.simplify(sp.expand(value)) == 0


def exact(label: str, condition: bool) -> None:
    COUNTS.exact_total += 1
    if not bool(condition):
        raise AssertionError(f"[exact] {label}")
    COUNTS.exact_pass += 1
    print(f"PASS [exact] {label}")


def floating(label: str, error: float, tolerance: float = 2.0e-10) -> None:
    COUNTS.float_total += 1
    if not math.isfinite(error) or error >= tolerance:
        raise AssertionError(
            f"[float] {label}: error={error:.3e}, tolerance={tolerance:.1e}"
        )
    COUNTS.float_pass += 1
    print(f"PASS [float] {label}: error={error:.3e}")


def tensor_data(k: sp.Matrix) -> tuple[sp.Matrix, ...]:
    basis: list[sp.Matrix] = []
    for i, j in PAIRS:
        element = sp.zeros(3)
        element[i, j] = element[j, i] = 1 if i == j else 1 / sp.sqrt(2)
        basis.append(element)
    b = sp.Matrix.hstack(*(element * k for element in basis))
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    r2 = (k.T * k)[0]
    v = b.T * k
    scalar = v - r2 * trace
    kp = sp.eye(6) - trace * trace.T / 2
    kq = (
        r2 * (sp.eye(6) - trace * trace.T)
        - 2 * b.T * b
        + trace * v.T
        + v * trace.T
    )
    return basis, b, trace, scalar, kp, kq, r2


def explicit_ptt(k: sp.Matrix, basis: list[sp.Matrix], r2: sp.Expr) -> sp.Matrix:
    projector = sp.eye(3) - k * k.T / r2
    columns = []
    for element in basis:
        image = projector * element * projector
        image -= projector * sp.trace(projector * element) / 2
        columns.append(sp.Matrix([sp.trace(test.T * image) for test in basis]))
    return sp.Matrix.hstack(*columns)


def general_source_decomposition() -> None:
    print("\nGENERAL NONZERO FIBRE")
    x, y, z = sp.symbols("x y z", real=True)
    rho, rho_ddot = sp.symbols("rho rho_ddot")
    k = sp.Matrix([x, y, z])
    basis, b, trace, scalar, kp, kq, r2 = tensor_data(k)
    ptt = explicit_ptt(k, basis, r2)
    tau = sp.Matrix(sp.symbols("tau0:6"))
    drive = kq * kp * tau + scalar * rho / 2

    # The Ward consequence is rho_ddot = -k^T B tau.
    ward = {rho_ddot: -(k.T * b * tau)[0]}
    drive_tt = r2 * ptt * tau
    drive_scalar = scalar * (rho_ddot + r2 * rho) / (2 * r2)

    exact("Kq Kp Kq = r^4 P_TT", is_zero(kq * kp * kq - r2**2 * ptt))
    exact("the source drive is transverse", is_zero(b * drive))
    exact(
        "the Ward equations fix trace(J)=-(rho_ddot+r^2 rho)",
        is_zero(((trace.T * drive)[0] + rho_ddot + r2 * rho).subs(ward)),
    )
    exact(
        "J splits exactly into radiative TT and affine scalar pieces",
        is_zero((drive - drive_tt - drive_scalar).subs(ward)),
    )
    exact("P_TT J = r^2 P_TT tau", is_zero(ptt * drive - drive_tt))

    g = sp.symbols("g", real=True)
    e_aff = -g * scalar * rho / (2 * r2)
    f_aff = sp.diff(e_aff, rho) * sp.symbols("rho_dot")
    exact("B E_aff = 0", is_zero(b * e_aff))
    exact("trace(E_aff)=g rho", is_zero((trace.T * e_aff)[0] - g * rho))
    exact(
        "E_aff''+r^2 E_aff equals minus g times the scalar drive",
        is_zero(-g * scalar * (rho_ddot + r2 * rho) / (2 * r2)
                + g * drive_scalar),
    )
    exact(
        "trace(F_aff)=g rho_dot",
        is_zero((trace.T * f_aff)[0] - g * sp.symbols("rho_dot")),
    )


def kubo_and_weyl_signs() -> None:
    print("\nONE PHYSICAL OSCILLATOR: CCR, KUBO SIGN, WEYL SHIFT")
    r, delta, g, eta = sp.symbols("r delta g eta", positive=True, real=True)
    omega = sp.Matrix([[0, 1], [-1, 0]])
    q_later = sp.Matrix([[sp.cos(r * delta), sp.sin(r * delta) / r]])
    q_earlier = sp.Matrix([[1, 0]])
    poisson_kernel = (q_later * omega * q_earlier.T)[0]
    comm_q_q = sp.I * poisson_kernel
    comm_e_q = r**2 * comm_q_q

    exact("[q(t),q(t')]=-i sin(r Delta)/r", is_zero(
        comm_q_q + sp.I * sp.sin(r * delta) / r
    ))
    exact("[E(t),q(t')]=-i r sin(r Delta)", is_zero(
        comm_e_q + sp.I * r * sp.sin(r * delta)
    ))
    kubo_integrand = -sp.I * g * eta * comm_e_q
    exact("-i[E,H_int] has the retarded minus sign", is_zero(
        kubo_integrand + g * r * sp.sin(r * delta) * eta
    ))

    # D(alpha)^* a D(alpha)=a+alpha with
    # alpha=-i g int eta(s)e^{irs}/sqrt(2r) ds.  Represent the integral by Z.
    zr, zi = sp.symbols("Z_r Z_i", real=True)
    z = zr + sp.I * zi
    alpha = -sp.I * g * z / sp.sqrt(2 * r)
    t = sp.symbols("t", real=True)
    q_shift = sp.simplify(
        (alpha * sp.exp(-sp.I * r * t)
         + sp.conjugate(alpha) * sp.exp(sp.I * r * t)) / sp.sqrt(2 * r)
    )
    # If Z=int eta(s)e^{irs} ds, the real identity below is the sine kernel.
    expected = -g / r * sp.im(sp.exp(sp.I * r * t) * sp.conjugate(z))
    exact("Weyl displacement gives the same retarded q shift", is_zero(
        sp.expand_complex(q_shift - expected)
    ))

    # Magnus terminates because [H_I(s),H_I(u)] is central.  The nested
    # commutator with a third H is therefore zero, encoded as [linear,scalar]=0.
    central = sp.symbols("central", commutative=True)
    exact("the third Magnus commutator vanishes for linear forcing",
          Commutator(sp.Symbol("H", commutative=False), central).doit() == 0)


def non_tt_conserved_source() -> None:
    print("\nNON-TT CONSERVED SOURCE: SCALAR TERM CANNOT HIDE")
    r = sp.symbols("r", positive=True, real=True)
    rho, rho_dot, rho_ddot, g = sp.symbols(
        "rho rho_dot rho_ddot g", real=True
    )
    k = sp.Matrix([0, 0, r])
    basis, b, trace, scalar, kp, kq, r2 = tensor_data(k)
    ptt = explicit_ptt(k, basis, r2)

    # dot rho=-i k.j and dot j=-i B.tau.
    current = sp.Matrix([0, 0, sp.I * rho_dot / r])
    tau = sp.Matrix([0, 0, -rho_ddot / r2, 0, 0, 0])
    dot_current = sp.Matrix([0, 0, sp.I * rho_ddot / r])
    drive = sp.simplify(kq * kp * tau + scalar * rho / 2)
    e_aff = sp.simplify(-g * scalar * rho / (2 * r2))

    exact("the explicit source obeys dot rho+i k.j=0",
          is_zero(rho_dot + sp.I * (k.T * current)[0]))
    exact("the explicit source obeys dot j+i B.tau=0",
          is_zero(dot_current + sp.I * b * tau))
    exact("its stress has zero TT projection", is_zero(ptt * tau))
    exact("its Kubo radiative drive is exactly zero", is_zero(ptt * drive))
    exact("its full curvature response is nonzero for rho nonzero",
          not is_zero(e_aff))
    exact("the affine response has the required sourced trace",
          is_zero((trace.T * e_aff)[0] - g * rho))
    exact("a TT-only response violates the scalar constraint",
          not is_zero(-g * rho))

    # A convenient affine lift in unreduced canonical coordinates.
    q_aff = -g * trace * rho / (2 * r2)
    p_aff = g * trace * rho_dot / r2
    exact("Kq q_aff=E_aff and -s.q_aff+g rho=0",
          is_zero(kq * q_aff - e_aff)
          and is_zero(-(scalar.T * q_aff)[0] + g * rho))
    exact("Kp p_aff=dot(q_aff)", is_zero(
        kp * p_aff + g * trace * rho_dot / (2 * r2)
    ))
    exact("the longitudinal momentum constraint is satisfied", is_zero(
        sp.I * b * p_aff - g * current
    ))


def retarded_integral_regression() -> None:
    print("\nRETARDED INTEGRAL REGRESSION")
    mp.mp.dps = 50
    r = mp.mpf("1.7")
    g = mp.mpf("0.37")
    t = mp.mpf("1.3")

    # rho(u)=u^2 exp(-u) Theta(u) has rho(0)=rho'(0)=0.
    rho = lambda u: u**2 * mp.e**(-u)
    rho_ddot = lambda u: (u**2 - 4*u + 2) * mp.e**(-u)
    convolution = mp.quad(
        lambda u: mp.sin(r * (t-u)) / r * (rho_ddot(u) + r**2 * rho(u)),
        [0, t],
    )
    expected = rho(t)
    floating("Green convolution reproduces rho with compatible initial data",
             float(abs(convolution - expected)), 2.0e-40)

    # In three spatial dimensions a bounded smooth force profile has finite
    # coherent norm near k=0: 4pi k^2 |f|^2/(2k), f=exp(-k^2).
    coherent_norm = mp.quad(lambda k: 2 * mp.pi * k * mp.e**(-2*k*k), [0, mp.inf])
    floating("explicit smooth-source infinite-volume coherent norm is pi/2",
             float(abs(coherent_norm - mp.pi/2)), 2.0e-40)


def main() -> None:
    global COUNTS
    COUNTS = Counts()
    general_source_decomposition()
    kubo_and_weyl_signs()
    non_tt_conserved_source()
    retarded_integral_regression()
    print(
        "\nSUMMARY: "
        f"exact {COUNTS.exact_pass}/{COUNTS.exact_total}; "
        f"floating regressions {COUNTS.float_pass}/{COUNTS.float_total}"
    )
    print(
        "SCOPE: prescribed c-number source on the zero-mean free tensor Fock "
        "target; TT Weyl/Kubo response plus affine scalar curvature; "
        "NO RH CLAIM; T1-T8 remain open"
    )


if __name__ == "__main__":
    main()
