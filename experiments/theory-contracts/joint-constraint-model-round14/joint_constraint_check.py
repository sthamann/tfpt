#!/usr/bin/env python3
"""Exact actual gauge-phase/clock controls for the declared joint model.

Finite matrices below describe actual linear constraint transport or explicitly
labelled spectral MODELS, never finite canonical commutation relations.
"""
import json
import sympy as sp


def main():
    checks = []

    def check(name, value):
        if not bool(value):
            raise AssertionError(name)
        checks.append(name)

    def zero(value):
        seq = list(value) if isinstance(value, sp.MatrixBase) else [value]
        return all(sp.simplify(sp.expand(v)) == 0 for v in seq)

    r, v0, v1, v2, t, s = sp.symbols("r v0 v1 v2 t s", real=True)
    v = sp.Matrix([v0,v1,v2])
    c = sp.Matrix([r,v0,v1,v2])
    bh = -sp.Rational(1,16)
    bv = sp.Matrix([[5,-3,0],[-3,5,0],[0,0,8]])/32
    b = sp.Matrix([[2,2,0]])
    d = (b*v)[0]
    q = bh*r*r/2+(v.T*bv*v)[0]/2
    A = sp.zeros(4)
    A[0,1:] = b
    backward = sp.eye(4)-t*A
    phase = t*q-t*t*r*bh*d/2+t**3*d*bh*d/6
    check("ACTUAL nilpotent gauge transport has zero trace", A*A == sp.zeros(4) and sp.trace(A) == 0)
    check("ACTUAL characteristic and dual flows preserve Lebesgue measure",
          backward.det() == 1 and backward.T.det() == 1)
    check("ACTUAL gauge phase integrates the backward potential",
          zero(sp.diff(phase,t)-q.subs(r,r-t*d)))
    check("ACTUAL gauge phase satisfies the full transport equation",
          zero(sp.diff(phase,t)+d*sp.diff(phase,r)-q))
    check("ACTUAL exact gauge unitary group phase cocycle",
          zero(phase+phase.subs({t:s,r:r-t*d},simultaneous=True)-phase.subs(t,t+s)))
    check("ACTUAL free gauge phase vanishes on the full zero constraint fiber",
          phase.subs({r:0,v0:0,v1:0,v2:0}) == 0)
    check("ACTUAL omission of cubic-time phase is detected",
          not zero(sp.diff(phase-t**3*d*bh*d/6,t)+d*sp.diff(phase-t**3*d*bh*d/6,r)-q))

    # Differentiate on arbitrary functions; this tests the actual full
    # differential generator, not only its classical phase polynomial.
    f = sp.Function("f")(r,v0,v1,v2)
    U = sp.exp(-sp.I*phase)*f.subs(r,r-t*d)
    op = lambda z: -sp.I*d*sp.diff(z,r)+q*z
    check("ACTUAL characteristic formula solves the full differential equation",
          zero((sp.I*sp.diff(U,t)-op(U))/sp.exp(-sp.I*phase)))
    lam = sp.symbols("lambda", real=True)
    clock_U = sp.exp(-sp.I*t*lam)*U
    check("JOINT clock plus gauge group has generator Kc+lambda",
          zero((sp.I*sp.diff(clock_U,t)-op(clock_U)-lam*clock_U)/sp.exp(-sp.I*(phase+t*lam))))
    beta = sp.symbols("beta", real=True)
    check("ACTUAL c is covariant but is not a commuting constraint with the generator",
          zero(op(r*f)-r*op(f)+sp.I*d*f) and d != 0)
    covector = sp.Matrix(sp.symbols("u0:4", real=True))
    shifted_phase = (covector.T*backward*c)[0]
    check("JOINT dual semidirect action has the correct sign",
          zero(shifted_phase-((sp.eye(4)-t*A.T)*covector).dot(c)))
    check("JOINT false direct-product replacement is detected",
          not zero(shifted_phase-covector.dot(c)))

    # The tube transports with the physical unitary. This two-energy MODEL
    # detects retaining the old spectral projection after a noncommuting map.
    energy = sp.diag(2,5)
    rotation = sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
    old_band = sp.diag(1,0)  # p=-sqrt(24), I=(-1/2,1/2)
    new_energy = rotation*energy*rotation.T
    new_band = rotation*old_band*rotation.T
    seed = sp.Matrix([1,0])
    moved = rotation*seed
    check("MODEL conjugated positive operator retains the same lower bound",
          (new_energy-2*sp.eye(2)).eigenvals() == {sp.Integer(0):1,sp.Integer(3):1})
    check("MODEL original spectral tube need not be preserved by dressing",
          old_band*moved != moved)
    check("MODEL correctly transported tube contains the dressed vector",
          zero(new_band*moved-moved))
    check("MODEL transported clock-shell eigenvalue remains zero",
          zero((new_energy-2*sp.eye(2))*moved))

    # Exact normalization control for each Abelian Fourier evaluation.
    a = sp.symbols("a", real=True)
    factor = sp.sqrt(sp.pi/2)*sp.exp(-a*a/8)/(2*sp.pi)
    evaluated = sp.integrate(factor,(a,-sp.oo,sp.oo))
    check("MODEL normalized Fourier averaging evaluates the zero fiber", evaluated == 1)
    projector = sp.Matrix([[1,1],[1,1]])/2
    check("MODEL compact fixed-space projector is positive and idempotent",
          projector*projector == projector and projector.eigenvals()=={sp.Integer(0):1,sp.Integer(1):1})
    e1,e2 = sp.symbols("e1 e2", positive=True)
    half_density = sp.diag(e1,e2)
    norm_kernel = half_density*projector*half_density
    check("JOINT projection retains both noncommuting half-density factors",
          norm_kernel == norm_kernel.T and sp.det(norm_kernel)==0 and sp.trace(norm_kernel)>0)
    check("JOINT moving the energy weight past the projection is rejected",
          half_density**2*projector != norm_kernel)

    print(json.dumps({"status":"PASS","exact_check_groups":len(checks),"checks":checks,
                      "actual_gauge_phase":str(sp.expand(phase)),
                      "scope":"Actual linear gauge characteristic plus exact joint clock/group controls; explicit spectral MODELS. Full self-adjoint domains and positive joint averaging are proved in PROOF.md for the declared constraint-ideal and auxiliary gauge-unfixed completion, not the unchanged old off-shell operator or a full TOE."},indent=2))


if __name__ == "__main__":
    main()
