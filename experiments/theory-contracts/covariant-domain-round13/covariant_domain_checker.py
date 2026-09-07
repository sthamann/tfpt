#!/usr/bin/env python3
"""Actual nilpotent constraint transport and its remaining domain obstacles.

No repository imports and no numerical approximation to the CCR. The actual
L2 source is reconstructed; the Robin boundary example is explicitly a model.
Infinite-dimensional assertions are proved, or left open, in README.md.
"""

from itertools import product
import sympy as sp


def clean(x):
    return sp.simplify(sp.expand(x))


def zero(x):
    if isinstance(x, sp.MatrixBase):
        return all(clean(a) == 0 for a in x)
    return clean(x) == 0


def main():
    checks = []

    def check(label, statement):
        good = bool(statement)
        checks.append(good)
        print(f"{'PASS' if good else 'FAIL'} {label}", flush=True)

    # All-volume real-space formula is A=[[0,div_-],[0,0]]. These finite
    # matrices check its sign convention, rank, and exact nilpotence.
    for side in (2, 3):
        sites = list(product(range(side), repeat=3))
        lookup = {x: i for i, x in enumerate(sites)}
        n = len(sites)
        minus = []
        for axis in range(3):
            shift = sp.zeros(n)
            for i, x in enumerate(sites):
                xx = list(x)
                xx[axis] = (xx[axis] + 1) % side
                shift[i, lookup[tuple(xx)]] = 1
            minus.append(sp.eye(n) - shift.T)
        b = sp.Matrix.hstack(*minus)
        aa = sp.zeros(4*n)
        aa[:n, n:] = b
        check(f"actual L{side} A squared vanishes, with zero trace", zero(aa*aa) and sp.trace(aa) == 0)
        check(f"actual L{side} propagation rank is n-1", b.rank() == n-1)
        t, u = sp.symbols("t u", real=True)
        check(f"actual L{side} affine flow group law", zero((sp.eye(4*n)+t*aa)*(sp.eye(4*n)+u*aa)-(sp.eye(4*n)+(t+u)*aa)))

    rt = sp.sqrt(2)
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    v = sp.Matrix([[-2, 0, 0, 0, 0, rt], [0, -2, 0, 0, 0, rt], [0, 0, 0, rt, rt, 0]])
    scalar = sp.Matrix([4, 4, 8, 0, 0, 4*rt])
    ell = sp.Integer(8)
    polar = sp.Matrix.hstack(sp.Matrix([1, 1, -2, 0, 0, rt])/sp.sqrt(8), sp.Matrix([0, 0, 0, 1, -1, 0])/rt)
    kp = sp.eye(6)-trace*trace.T/2
    kq = ell*polar*polar.T-scalar*scalar.T/(2*ell)
    gv = v*v.T
    bv = (gv.inv()*v*kp*v.T*gv.inv()).applyfunc(clean)
    bh = -1/(2*ell)
    arow = (scalar.T*kp*v.T*gv.inv()).applyfunc(clean)
    check("actual one-mode propagation row is (2,2,0)", arow == sp.Matrix([[2, 2, 0]]))
    check("actual vector-constraint quadratic matrix", bv == sp.Matrix([[5,-3,0],[-3,5,0],[0,0,8]])/32)

    Q = sp.Matrix(sp.symbols("Q0:2", real=True))
    P = sp.Matrix(sp.symbols("P0:2", real=True))
    ch = sp.symbols("ch", real=True)
    cv = sp.Matrix(sp.symbols("cv0:3", real=True))
    xh = sp.symbols("xh", real=True)
    xv = sp.Matrix(sp.symbols("xv0:3", real=True))
    q = polar*Q+scalar*ch/(scalar.T*scalar)[0]+v.T*xv
    p = polar*P-scalar*xh+v.T*gv.inv()*cv
    check("actual inverse Darboux chart gives all constraints", zero(scalar.T*q-sp.Matrix([ch])) and zero(v*p-cv))
    check("actual inverse Darboux chart gives all gauge coordinates", zero(-scalar.T*p/(scalar.T*scalar)[0]-sp.Matrix([xh])) and zero(gv.inv()*v*q-xv))
    htt = (P.T*P)[0]/2+ell*(Q.T*Q)[0]/2
    hzero = (q.T*kq*q)[0]/2+(p.T*kp*p)[0]/2
    hzero_expected = htt-xh*(arow*cv)[0]+bh*ch**2/2+(cv.T*bv*cv)[0]/2
    check("actual free Hamiltonian exact Darboux normal form", zero(hzero-hzero_expected))

    sites = list(product(range(2), repeat=3))
    lookup = {x: i for i, x in enumerate(sites)}
    phi = sp.Matrix(sp.symbols("f0:8", real=True))
    pi = sp.Matrix(sp.symbols("r0:8", real=True))
    mass2 = sp.Integer(2)

    def shift(x, axis, step=1):
        xx = list(x)
        xx[axis] = (xx[axis]+step) % 2
        return tuple(xx)

    def field(x):
        return phi[lookup[x]]

    def grad(x, axis):
        return field(shift(x, axis))-field(x)

    rho = hm = sp.Integer(0)
    js = sp.zeros(3, 1)
    tau = sp.zeros(6, 1)
    weights = []
    for x in sites:
        i = lookup[x]
        w = sp.Integer(-1)**(x[0]+x[1])/sp.sqrt(8)
        weights.append(w)
        density = pi[i]**2/2+mass2*phi[i]**2/2+sum(grad(x,j)**2+grad(shift(x,j,-1),j)**2 for j in range(3))/4
        rho += w*density
        hm += density
        for j in range(3):
            js[j] -= w*(pi[i]+pi[lookup[shift(x,j)]])*grad(x,j)/2
            tau[j] += w*(pi[i]**2/2-mass2*phi[i]**2/2+grad(x,j)*grad(shift(x,j,-1),j)/2-sum(grad(x,k)**2+grad(shift(x,k,-1),k)**2 for k in range(3) if k != j)/4)
        for k, (i1, i2) in enumerate(((1,2),(0,2),(0,1)), 3):
            tau[k] += w*rt*(grad(x,i1)+grad(shift(x,i2),i1))*(grad(x,i2)+grad(shift(x,i1),i2))/4
    rho, hm = sp.expand(rho), sp.expand(hm)
    js, tau = js.applyfunc(sp.expand), tau.applyfunc(sp.expand)
    jvec = -js
    jall = sp.Matrix.vstack(sp.Matrix([rho]), jvec)
    tt = (polar.T*tau).applyfunc(clean)
    B = clean((scalar.T*tau)[0]/128+rho/16)
    check("actual TT source is nonzero configuration-only quadratic", not zero(tt) and all(sp.diff(f,r) == 0 for f in tt for r in pi))

    coords = [xh]+list(xv)+list(Q)+list(phi)
    momenta = [ch]+list(cv)+list(P)+list(pi)

    def pb(a, b):
        return sp.expand(sum(sp.diff(a,x)*sp.diff(b,k)-sp.diff(a,k)*sp.diff(b,x) for x,k in zip(coords,momenta)))

    S = -xh*rho-(xv.T*jvec)[0]
    hf = sp.expand(hzero+hm)
    V1 = sp.expand((q.T*tau)[0])
    W = sp.expand(V1-pb(hf,S))
    expected_W = (Q.T*tt)[0]+ch*B-(cv.T*bv*jvec)[0]
    propagation = sp.zeros(4)
    propagation[0,1:] = arow
    c_all = [ch]+list(cv)
    check("actual Ward identity reconstructed before fiber reduction", zero(sp.Matrix([pb(ca,V1)+pb(ja,hm) for ca,ja in zip(c_all,jall)])-propagation*jall))
    check("actual W exact affine-constraint normal form", zero(W-expected_W))
    check("actual W contains no gauge coordinates", all(sp.diff(W,x) == 0 for x in [xh]+list(xv)))
    check("actual B_H matter kinetic Hessian is 3/16 times density weights", zero(sp.hessian(B,list(pi))-sp.diag(*weights)*sp.Rational(3,16)))

    g, time = sp.symbols("g time", real=True)
    # An actual regular orbit: cv=(1/2,0,0), ch=time, speed arow.cv=1.
    cv0 = sp.Matrix([sp.Rational(1,2),0,0])
    frozen = htt+hm-g*(cv0.T*bv*jvec)[0]+g*(Q.T*tt)[0]+(cv0.T*bv*cv0)[0]/2
    fiber = frozen+g*time*B-time**2/32
    check("actual orbit has speed one", (arow*cv0)[0] == 1)
    check("actual fiber is affine modulo an exact scalar quadratic", zero(sp.diff(fiber,time,2)+sp.Rational(1,16)))
    phase = -time**3/96
    check("actual scalar phase removes only -time squared /32", zero(sp.diff(phase,time)+time**2/32))
    kinetic = sp.hessian(fiber,list(pi))
    kinetic_expected = sp.eye(8)+g*time*sp.diag(*weights)*sp.Rational(3,16)
    check("actual complete scalar kinetic matrix on orbit", zero(kinetic-kinetic_expected))
    crossing = 32*rt/3
    at = kinetic.subs({g:1,time:crossing})
    after = kinetic.subs({g:1,time:2*crossing})
    check("actual finite-time kinetic degeneracy has rank four", at.rank() == 4)
    check("actual later kinetic signature is (4+,4-)", sorted(after.diagonal()) == [-1]*4+[3]*4)
    check("actual time dependence is not scalar", not zero(sp.hessian(B,list(phi)+list(pi))))
    check("actual B_H does not commute with TT interaction", not zero(pb(B,(Q.T*tt)[0])))
    check("actual separated-time fiber commutator is nonzero", not zero(pb(frozen,B)))
    quartic = pb((Q.T*tt)[0],pb((Q.T*tt)[0],(P.T*P)[0]/2))
    check("actual nested TT vertex produces nonzero quartic source", zero(quartic-(tt.T*tt)[0]) and not zero(quartic))

    # Every fixed polynomial oscillator Gronwall comparison N^k fails:
    # principal Poisson term from Q.tau has degree 2k+1 against 2k.
    physcoords, physmom = list(Q)+list(phi), list(P)+list(pi)
    radius = sum(x*x for x in physcoords+physmom)/2
    cubic = (Q.T*tt)[0]
    ncomm = pb(cubic,radius)
    datum = dict(zip(phi,[-2,1,3,-1,4,0,-4,2]))
    datum.update(dict.fromkeys(pi,0))
    datum.update(dict.fromkeys(Q,0))
    datum.update(dict(zip(P,[1,0])))
    gamma = clean(ncomm.subs(datum))
    check("actual oscillator commutator has nonzero cubic coherent-ray coefficient", gamma != 0 and sp.Poly(ncomm,*physcoords,*physmom).total_degree() == 3)
    amp = sp.symbols("amp", positive=True)
    ray = {x:amp*datum[x] for x in physcoords+physmom}
    for power in (1,2,3):
        lhs = clean(power*radius**(power-1)*ncomm).subs(ray,simultaneous=True)
        rhs = (radius**power).subs(ray,simultaneous=True)
        check(f"actual N^{power} commutator grows one degree faster than N^{power}", sp.Poly(clean(lhs),amp).degree() == 2*power+1 and sp.Poly(clean(rhs),amp).degree() == 2*power)

    # Actual nilpotent regular-orbit coordinate. Formula is general in a
    # fixed nonzero velocity d and works for any number of scalar labels.
    r = sp.Matrix(sp.symbols("a0:2", real=True))
    d = sp.Matrix([1,2])
    orbit_time = (d.T*r)[0]/(d.T*d)[0]
    transverse = r-d*orbit_time
    moved = dict(zip(r,r+time*d))
    check("regular-orbit coordinate shifts by exactly physical time", zero(orbit_time.subs(moved,simultaneous=True)-orbit_time-time))
    check("regular-orbit transverse label is invariant", zero(transverse.subs(moved,simultaneous=True)-transverse))

    # Explicit MODEL counterexample: H=-i partial_s-partial_x^2 on x>0,
    # Fourier-s Robin condition partial_x f(k,0)=k^2 f(k,0).
    # Self-adjoint and time reversal invariant, but NOT s-covariant.
    k, beta, x, ss = sp.symbols("k beta x ss", real=True)
    fboundary = (1+(k*k+1)*x)*sp.exp(-x)
    check("MODEL Robin packet obeys original k-dependent boundary", zero(sp.diff(fboundary,x).subs(x,0)-k*k*fboundary.subs(x,0)))
    shifted = fboundary.subs(k,k-beta)
    defect = clean(sp.diff(shifted,x).subs(x,0)-k*k*shifted.subs(x,0))
    check("MODEL modulation violates boundary by beta squared -2k beta", zero(defect-(beta**2-2*k*beta)) and not zero(defect))
    f = sp.Function("f")(ss,x)
    Hop = lambda z: -sp.I*sp.diff(z,ss)-sp.diff(z,x,2)
    check("MODEL correct formal Weyl commutator survives on interior tests", zero(Hop(sp.exp(sp.I*beta*ss)*f)-sp.exp(sp.I*beta*ss)*(Hop(f)+beta*f)))
    check("MODEL Robin coefficient is real, permitting reflection-conjugation", sp.conjugate(k*k) == k*k)
    # Averaging unitary boundary maps does not preserve unitarity.
    average = (sp.eye(2)+sp.diag(-1,-1))/2
    check("MODEL averaging deficiency unitaries can produce zero contraction", average == sp.zeros(2) and average.T*average != sp.eye(2))

    print(f"ACTUAL_BV: {bv}")
    print(f"ACTUAL_KINETIC_CROSSING_G1: {crossing}")
    print(f"ACTUAL_CUBIC_OSCILLATOR_COMMUTATOR_RAY: {gamma}")
    print(f"COUNTS: {sum(checks)}/{len(checks)} exact checks; 0 floating checks")
    print("SCOPE: actual normal form and analytic obstructions; MODEL boundary negative control; no actual covariant propagator existence claim")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
