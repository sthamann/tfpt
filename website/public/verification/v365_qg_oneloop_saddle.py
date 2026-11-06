"""v365 -- QGAMB.SADDLE.01: finite saddle diagnostics and conditional Gaussian data.

The scalar stiffness 1/c3=8pi and gap margin are inherited inputs to the
fluctuation discussion. They do not specify a whole geometric Hessian,
its integration base, ghost/reference factors or common field measure.

Correction, 6 November 2026: with E1=6 log(3/2), E2=6 log 3, the old
sum 6 log(9/2) is Tr' H=-log det' T for T=exp(-H), not log det' H.
If M is additionally identified with this two-mode H, log det' M is
log[36 log(3/2) log 3]. Its half log determinant remains conditional;
stiffness and the complete original measure normalization are retained.

The exact susceptibility chi=729/665 is a finite geometric series. It
alone proves no geometric measure tightness or projective consistency.
This module does not construct the whole original measure. The separate
conditional admissible IR/ambient redundancy route remains unchanged.
Python-only; no new physical kernel or common field value is claimed.
"""
import sympy as sp

from tfpt_constants import check, summary, reset, g_car, N_fam

pi = sp.pi
c3 = sp.Rational(1, 8) / pi
dimE8 = 248


def run():
    reset()
    print("v365  QGAMB.SADDLE.01: finite saddle diagnostics; conditional Gaussian determinant")

    # Scalar coefficient inherited from the original saddle discussion.
    stiffness = 1 / c3
    check("SCALAR STIFFNESS [E]: 1/c3=8pi (v358/v359); this coefficient alone "
          "does not specify the whole fluctuation Hessian or integration base",
          sp.simplify(stiffness - 8 * pi) == 0)

    # The numeric margin; application to a whole Hessian is conditional.
    twoV = 2 * dimE8 * c3**2
    Delta = 6 * sp.log(sp.Rational(3, 2))
    Delta_eff = Delta - twoV
    check("GAP MARGIN [E]: Delta-2||V||=6 ln(3/2)-31/(4pi^2)=%.4f>0; modewise "
          "Gaussian convergence is conditional on the actual fluctuation operator "
          "satisfying this lower bound" % float(Delta_eff),
          sp.simplify(twoV - sp.Rational(31, 4) / pi**2) == 0
          and 31 == 2**g_car - 1 and dimE8 == 8 * 31
          and float(Delta_eff) > 0 and abs(float(Delta_eff) - 1.6476) < 1e-3)

    # Literal original two positive transfer energies; omit the Perron mode.
    energies = [6 * sp.log(sp.Rational(3, 2)), 6 * sp.log(3)]
    transfer_eigenvalues = [sp.Rational(2, 3)**6, sp.Rational(1, 3)**6]
    trace_H = sum(energies)
    neg_logdet_T = -sp.log(sp.prod(transfer_eigenvalues))
    check("FINITE TRANSFER TRACE [E]: Tr' H=-log det' T=6 ln(9/2)=%.8f; "
          "the old energy sum is not a Gaussian Hessian log determinant" % float(trace_H),
          sp.simplify(trace_H - 6 * sp.log(sp.Rational(9, 2))) == 0
          and sp.simplify(trace_H - neg_logdet_T) == 0)

    # Conditional M=H only; no physical Hessian or base density is selected.
    det_H = sp.prod(energies)
    logdet_H = sp.log(det_H)
    W_if_M_eq_H = logdet_H / 2
    check("CONDITIONAL GAUSSIAN DATA [C]: if M=H on these two positive modes, "
          "det' M=36 ln(3/2) ln3, log det' M=%.8f and (1/2)log det' M=%.8f; "
          "stiffness, measure normalization and original relative/ghost factors remain"
          % (float(logdet_H), float(W_if_M_eq_H)),
          sp.simplify(det_H - 36 * sp.log(sp.Rational(3, 2)) * sp.log(3)) == 0
          and all(e > 0 for e in energies)
          and sp.simplify(sp.exp(logdet_H) - det_H) == 0
          and abs(float(logdet_H - trace_H)) > 1)

    # 4. conformal direction convergent on the GHP contour
    c_conf = sp.Rational(-3, 2)
    phi = sp.symbols('phi', real=True)
    ghp_int = sp.integrate(sp.exp(-sp.Abs(c_conf) * phi**2), (phi, -sp.oo, sp.oo))
    check("GHP CONTOUR [C]: for the stated rotated conformal Gaussian, "
          "int exp(-|c|phi^2)=sqrt(2pi/3); the whole source contour is not derived here",
          sp.simplify(ghp_int - sp.sqrt(pi / sp.Abs(c_conf))) == 0
          and sp.simplify(ghp_int - sp.sqrt(2 * pi / 3)) == 0)

    # A scalar transfer susceptibility, not a geometric tightness certificate.
    lambda2 = sp.Rational(2, 3)**6
    chi = 1 / (1 - lambda2)
    check("FINITE SUSCEPTIBILITY [E]: sum_n (2/3)^(6n)=729/665; this scalar series "
          "alone proves no geometric measure tightness or projective limit",
          sp.simplify(chi - sp.Rational(729, 665)) == 0 and float(chi) < sp.oo)

    central_charge = g_car + N_fam
    check("DIMENSIONLESS BOOKKEEPING [E]: c=g_car+N_fam=8; these expressions use "
          "the supplied atoms, not an evaluated whole fluctuation spectrum",
          central_charge == 8)

    check("SCOPE [C]/[O]: whole original field integration and its marked values "
          "are not computed here; the separate conditional IR/ambient redundancy "
          "route is retained", True)

    return summary("v365 finite saddle diagnostics: stiffness 8pi; positive gap margin; "
                   "Tr' H=-log det' T=6 ln(9/2); conditional M=H logdet "
                   "log[36 ln(3/2) ln3]; GHP integral and susceptibility 729/665; "
                   "no whole measure or tightness construction")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
