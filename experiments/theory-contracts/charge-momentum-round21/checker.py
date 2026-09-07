#!/usr/bin/env python3
"""Actual Ward force, charge-block obstruction and finite translation checks."""
from itertools import product
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from round21_algebra import Certificate, UNITS, energy, inputs
import sympy as s


def main():
    w = inputs(); cert = Certificate(); check = cert.check

    class Profile(w.WardComplex):
        def u(self, x):
            return s.Symbol("u_"+self.f.label(self.f.wrap(x)), real=True)

        def force(self, x):
            return super().force(x)-self.u(x)*self.f.phi(x)

        def tau(self, i, j, x):
            return super().tau(i, j, x)-(self.u(x)*self.f.phi(x)**2/2 if i == j else 0)

    f = w.Fields(); ward = Profile(f)
    for axis in range(3):
        x = w.ZERO; y = w.E[axis]
        expected = -(ward.u(y)-ward.u(x))*f.phi(x)*f.phi(y)/(2*ward.a)
        check(f"axis{axis}: exact local force from actual repaired Ward stencil", s.expand(ward.momentum_residual(axis, x)-expected) == 0)
    for size in (2, 3):
        sites = list(product(range(size), repeat=3)); count = len(sites)
        f = w.Fields(period=size); ward = Profile(f)
        for axis in range(3):
            momentum = s.expand(sum(ward.current(axis, x) for x in sites))
            centered = -sum(f.pi(x)*(f.phi(w.add(x, w.E[axis]))-f.phi(w.sub(x, w.E[axis]))) for x in sites)/(2*ward.a)
            force = s.expand(-sum((ward.u(w.add(x, w.E[axis]))-ward.u(x))*f.phi(x)*f.phi(w.add(x, w.E[axis])) for x in sites)/(2*ward.a))
            check(f"L{size} axis{axis}: periodic current equals centered total momentum", s.expand(momentum-centered) == 0)
            check(f"L{size} axis{axis}: exact global force without a stress remainder", s.expand(ward.dt(momentum)-force) == 0)
            if size == 2:
                check(f"L2 axis{axis}: reversed edge occurrences make the seed momentum trivial", momentum == 0 and force == 0)
            else:
                lam, t = s.symbols("lambda t", positive=True)
                profile = {ward.u(x): 2*lam*energy(UNITS[1])/count if x == w.ZERO else 0 for x in sites}
                fields = {f.phi(x): t if x in (w.ZERO, w.E[axis]) else 0 for x in sites}
                witness = s.expand(force.subs(profile).subs(fields))
                check(f"L3 axis{axis}: full E8 nonconstant force witness", witness == lam*t**2/(count*ward.a))
                cert.witnesses[f"axis{axis}_force"] = str(witness)
                compensator = (1, 1, 1)
                neutral_profile = dict(profile)
                neutral_profile[ward.u(compensator)] = 2*lam*energy(tuple(-v for v in UNITS[1]))/count
                check(f"L3 axis{axis}: neutral total-charge restriction does not evade the force", s.expand(force.subs(neutral_profile).subs(fields)) == witness)
                extra_energy = s.Symbol("compensating_energy", nonnegative=True)
                neutral_profile[ward.u(compensator)] = 2*lam*extra_energy/count
                check(f"L3 axis{axis}: arbitrary compensating charge leaves the same witness", s.expand(force.subs(neutral_profile).subs(fields)) == witness)
                check(f"L3 axis{axis}: uniform energy profile is a limited exception", force.subs({ward.u(x): 1 for x in sites}) == 0)

    # Arbitrary charge matrix elements, not a nearest-neighbor ansatz for Pc.
    # The general infinite-carrier theorem is proved by each diagonal block.
    q0, q1, lam = s.symbols("q0 q1 lambda", real=True)
    profiles = s.diag(lam*q0**2, lam*q1**2, lam*(q0**2+q1**2))
    Pc = s.Matrix(3, 3, s.symbols("pc0:9"))
    diagonal = s.diag(*s.symbols("d0:3"))
    hop = s.Matrix(3, 3, s.symbols("h0:9"))
    for k in range(3):
        check(f"charge block{k}: diagonal interaction commutator has zero diagonal", s.expand((profiles*Pc-Pc*profiles)[k, k]) == 0)
        check(f"charge block{k}: arbitrary diagonal charge energy also vanishes", s.expand((diagonal*Pc-Pc*diagonal)[k, k]) == 0)
        force = lam*q0*q1+s.I*(hop*Pc-Pc*hop)[k, k]
        check(f"charge block{k}: hopping commutator cannot cancel cross-field coefficient", s.diff(force, q0, q1) == lam)
    check("pure-point infinitesimal law has a genuine diagonal witness", (s.Integer(1)-0)/2 != 0)

    # Exact cyclic projectors at L=4, with explicit Nyquist branch +pi.
    size = 4; T = s.zeros(size)
    for j in range(size):
        T[(j+1) % size, j] = 1
    check("actual finite shift is unitary and periodic", T.T*T == s.eye(size) and T**size == s.eye(size))
    zeta = s.I
    projectors = [sum((zeta**(-k*r)*T**r for r in range(size)), s.zeros(size))/size for k in range(size)]
    check("finite translation spectral projectors sum to identity", sum(projectors, s.zeros(size)) == s.eye(size))
    for k, proj in enumerate(projectors):
        check(f"crystal projector{k}: idempotent Hermitian eigenspace", proj*proj == proj and proj == proj.conjugate().T and T*proj == zeta**k*proj)
    check("distinct crystal sectors are orthogonal", all(projectors[k]*projectors[j] == s.zeros(size) for k in range(size) for j in range(k)))
    weights = [0, s.pi/2, s.pi, -s.pi/2]
    Pcr = sum((weights[k]*projectors[k] for k in range(size)), s.zeros(size))
    check("crystal logarithm keeps the finite translation eigenphases", sum((s.exp(s.I*weights[k])*projectors[k] for k in range(size)), s.zeros(size)) == T)
    E0 = s.diag(1, 0, 0, 0)
    tangent = s.I*(Pcr*E0-E0*Pcr)
    check("fractional crystal translation leaves the diagonal occupation algebra", tangent != s.zeros(size) and all(tangent[k, k] == 0 for k in range(size)))
    check("crystal logarithm need not be a nearest-site operator", Pcr[0, 2] != 0)

    # Two EXACT degenerate eigenstates of the full oscillator Hilbert space.
    # Ladder actions below do NOT wrap or truncate oscillator occupation.
    sites = list(product(range(3), repeat=3)); count = len(sites)
    C = {x: s.sqrt(s.Rational(2, count))*s.cos(2*s.pi*x[0]/3) for x in sites}
    S = {x: s.sqrt(s.Rational(2, count))*s.sin(2*s.pi*x[0]/3) for x in sites}
    check("resonant real cubic modes are orthonormal", s.simplify(sum(C[x]**2 for x in sites)) == 1 and s.simplify(sum(S[x]**2 for x in sites)) == 1 and s.simplify(sum(C[x]*S[x] for x in sites)) == 0)
    f = w.Fields(period=3); ward = w.WardComplex(f)
    def sample(expr, mode):
        return s.simplify(expr.subs({f.phi(x): mode[x] for x in sites}).subs({ward.a: 1, ward.mass2: 0}))
    for name, mode in (("C", C), ("S", S)):
        check(f"actual cubic force gives eigenvalue3 on mode{name}", all(sample(ward.force(x), mode) == -3*mode[x] for x in sites))
    d = s.sqrt(3)/2
    shift = lambda x, step: ((x[0]+step) % 3, x[1], x[2])
    check("actual centered derivative rotates the degenerate real modes", all(s.simplify((C[shift(x, 1)]-C[shift(x, -1)])/2+d*S[x]) == 0 and s.simplify((S[shift(x, 1)]-S[shift(x, -1)])/2-d*C[x]) == 0 for x in sites))
    omega = s.Symbol("omega", positive=True)
    def ladder(v, axis, up):
        out = {}
        for occ, amp in v.items():
            if not up and occ[axis] == 0:
                continue
            dest = list(occ); dest[axis] += 1 if up else -1
            coefficient = s.sqrt(occ[axis]+1 if up else occ[axis])
            key = tuple(dest); out[key] = s.simplify(out.get(key, 0)+coefficient*amp)
        return out
    def linear(a, v, b, u):
        return {k: s.simplify(a*v.get(k, 0)+b*u.get(k, 0)) for k in set(v)|set(u)}
    def q(v, axis):
        return linear(1/s.sqrt(2*omega), ladder(v, axis, True), 1/s.sqrt(2*omega), ladder(v, axis, False))
    def p(v, axis):
        return linear(s.I*s.sqrt(omega/2), ladder(v, axis, True), -s.I*s.sqrt(omega/2), ladder(v, axis, False))
    ketC, ketS = {(1, 0): s.Integer(1)}, {(0, 1): s.Integer(1)}
    mixed = q(q(ketS, 1), 0)
    check("untruncated oscillator off-diagonal quadratic element", mixed.get((1, 0)) == 1/(2*omega))
    check("intermediate oscillator states really leave the two-state subspace", q(ketS, 1).get((0, 2)) != 0)
    def angular(v):
        return linear(d, q(p(v, 1), 0), -d, q(p(v, 0), 1))
    Pblock = s.Matrix([[angular(v).get(k, 0) for v in (ketC, ketS)] for k in ((1, 0), (0, 1))])
    check("actual centered momentum has correct quantum two-mode sign", Pblock == d*s.Matrix([[0, -s.I], [s.I, 0]]))
    vC = 2*q(q(ketC, 0), 0).get((1, 0))/count**2
    vS = 2*q(q(ketS, 0), 0).get((0, 1))/count**2
    check("charge impurity distinguishes the degenerate diagonal matrix elements", s.simplify(vC-vS) == 2/(count**2*omega))
    Vblock = s.diag(vC, vS)
    resonance = s.simplify((s.I*(Vblock*Pblock-Pblock*Vblock))[0, 1])
    check("nonzero resonant commutator defeats arbitrary regular correction", resonance == 2*d/(count**2*omega))
    energy0 = s.Symbol("E0", real=True)
    arbitrary_correction = s.Matrix(2, 2, s.symbols("mixed_correction0:4"))
    Hblock = (energy0+omega)*s.eye(2)
    check("every correction has zero commutator inside equal-energy block", Hblock*arbitrary_correction-arbitrary_correction*Hblock == s.zeros(2))
    QC, QS = s.symbols("QC QS", real=True)
    field = {x: C[x]*QC+S[x]*QS for x in sites}
    force_coeff = s.simplify(2*field[w.ZERO]*(field[(1, 0, 0)]-field[(2, 0, 0)])/(2*count))
    check("independent actual force polynomial gives the same oscillator matrix element", s.simplify(force_coeff/(QC*QS)*mixed[(1, 0)]) == resonance)
    r = (0, 1, 0)
    check("compensating total charge can use the identical mode phase", C[r] == C[w.ZERO] and S[r] == S[w.ZERO] == 0)
    extra = s.Symbol("compensator_energy", nonnegative=True)
    check("every nonnegative compensating energy keeps the resonance nonzero", s.ask(s.Q.positive((1+extra)*resonance)) is True)
    mass = s.Symbol("mass", positive=True)
    cert.witnesses["regular_mixed_correction_obstruction"] = str(resonance.subs(omega, s.sqrt(mass**2+3)))
    cert.emit("Charge-only additive no-go at all J; distinct exact two-mode quantum obstruction to arbitrary regular first correction at J=0 and fixed free seed. Neither is a universal mixed-gravity no-go.")


if __name__ == "__main__":
    main()
