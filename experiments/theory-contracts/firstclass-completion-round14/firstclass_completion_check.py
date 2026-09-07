#!/usr/bin/env python3
"""Exact actual-source and continuous-operator first-class completion checks.

The ONLY changed Hamiltonian is the explicitly declared constraint-ideal
completion in PROOF.md. No finite CCR matrices or spectral approximation.
"""
from itertools import product
from pathlib import Path
import importlib.util
import json
import sys
import sympy as s


def clean(value):
    return s.simplify(s.expand(value))


def zero(value):
    values = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(clean(x) == 0 for x in values)


def main():
    checks = []

    def check(name, statement):
        if not bool(statement):
            raise AssertionError(name)
        checks.append(name)

    # Read the ACTUAL local source frontend, not the former proxy models.
    ward_path = Path(__file__).resolve().parents[1] / 'free-scalar-3d/free_scalar_ward.py'
    spec = importlib.util.spec_from_file_location('r14_firstclass_actual_ward', ward_path)
    ward_module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = ward_module
    spec.loader.exec_module(ward_module)
    fields = ward_module.Fields(period=2)
    ward = ward_module.WardComplex(fields)

    # Actual staggered all-site matrices. The proof uses the exact
    # all-volume symbol; these ranks are finite independent controls.
    for side in (2, 3):
        sites = list(product(range(side), repeat=3))
        lookup = {x: j for j, x in enumerate(sites)}
        n = len(sites)
        minus = []
        for axis in range(3):
            shift = s.zeros(n)
            for j, x in enumerate(sites):
                target = list(x)
                target[axis] = (target[axis]+1) % side
                shift[j, lookup[tuple(target)]] = 1
            minus.append(s.eye(n)-shift.T)
        b_all = s.Matrix.hstack(*minus)
        aa = s.zeros(4*n)
        aa[:n, n:] = b_all
        check(f'ACTUAL L{side} transport is nilpotent and traceless',
              aa*aa == s.zeros(4*n) and s.trace(aa) == 0)
        check(f'ACTUAL L{side} transport rank is n-1', b_all.rank() == n-1)
        t, u = s.symbols('t u', real=True)
        check(f'ACTUAL L{side} exact complete affine flow',
              (s.eye(4*n)+t*aa)*(s.eye(4*n)+u*aa) == s.eye(4*n)+(t+u)*aa)

    # ACTUAL normalized real (pi,pi,0) mode, with every scalar site kept.
    rt = s.sqrt(2)
    trace = s.Matrix([1, 1, 1, 0, 0, 0])
    scalar = s.Matrix([4, 4, 8, 0, 0, 4*rt])
    vector = s.Matrix([[-2, 0, 0, 0, 0, rt], [0, -2, 0, 0, 0, rt],
                       [0, 0, 0, rt, rt, 0]])
    tt_frame = s.Matrix.hstack(s.Matrix([1, 1, -2, 0, 0, rt])/s.sqrt(8),
                              s.Matrix([0, 0, 0, 1, -1, 0])/rt)
    ell = s.Integer(8)
    kp = s.eye(6)-trace*trace.T/2
    kq = ell*tt_frame*tt_frame.T-scalar*scalar.T/(2*ell)
    gh = (scalar.T*scalar)[0]
    gv = vector*vector.T
    bh = -1/(2*ell)
    bv = (gv.inv()*vector*kp*vector.T*gv.inv()).applyfunc(clean)
    b = (scalar.T*kp*vector.T*gv.inv()).applyfunc(clean)
    check('ACTUAL normalized TT frame and both transverse conditions',
          zero(tt_frame.T*tt_frame-s.eye(2)) and zero(vector*tt_frame)
          and zero(scalar.T*tt_frame) and zero(trace.T*tt_frame))
    check('ACTUAL free propagation row and Bv matrix',
          b == s.Matrix([[2, 2, 0]]) and bv == s.Matrix([[5, -3, 0], [-3, 5, 0], [0, 0, 8]])/32)

    qtt = s.Matrix(s.symbols('Q0:2', real=True))
    ptt = s.Matrix(s.symbols('P0:2', real=True))
    r, xh = s.symbols('r XH', real=True)
    v = s.Matrix(s.symbols('v0:3', real=True))
    xv = s.Matrix(s.symbols('XV0:3', real=True))
    q = tt_frame*qtt+scalar*r/gh+vector.T*xv
    p = tt_frame*ptt-scalar*xh+vector.T*gv.inv()*v
    h_grav = ((q.T*kq*q)[0]+(p.T*kp*p)[0])/2
    h_tt = ((ptt.T*ptt)[0]+ell*(qtt.T*qtt)[0])/2
    velocity = (b*v)[0]
    k = bh*r*r/2+(v.T*bv*v)[0]/2
    kc = -xh*velocity+k
    check('ACTUAL all free TT and constraint blocks are retained exactly', zero(h_grav-h_tt-kc))

    sites = list(product(range(2), repeat=3))
    weights = [s.Integer(-1)**(x[0]+x[1])/s.sqrt(8) for x in sites]
    phi = [fields.phi(x) for x in sites]
    pi = [fields.pi(x) for x in sites]
    subst = {ward.a: 1, ward.mass2: 2}
    tau = s.zeros(6, 1)
    pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    for x, weight in zip(sites, weights):
        for j, (left, right) in enumerate(pairs):
            tau[j] += weight*(1 if left == right else rt)*ward.tau(left, right, x)
    tau = tau.subs(subst).applyfunc(clean)
    rho = clean(sum(w*ward.rho(x) for x, w in zip(sites, weights)).subs(subst))
    hm = clean(sum(ward.rho(x) for x in sites).subs(subst))
    j = s.Matrix([clean(sum(w*ward.current(a, x) for x, w in zip(sites, weights)).subs(subst))
                  for a in range(3)])
    jv = -j
    currents = s.Matrix.vstack(s.Matrix([rho]), jv)
    tt = (tt_frame.T*tau).applyfunc(clean)
    bcal = clean((scalar.T*tau)[0]/gh-bh*rho)
    cubic = (qtt.T*tt)[0]
    remainder = (tt.T*tt)[0]/(2*ell)
    check('ACTUAL TT stress is nonzero configuration-only quadratic',
          not zero(tt) and all(not entry.has(*pi) for entry in tt)
          and max(s.Poly(entry, *phi).total_degree() for entry in tt) == 2)
    check('ACTUAL TT delta-site source coefficient is one quarter',
          s.Poly(tt[0], *phi).coeff_monomial(phi[0]**2) == s.Rational(1, 4))
    check('ACTUAL nonzero discarded Bcal kinetic coefficient',
          clean(s.diff(bcal, pi[0], 2)) == 3*rt/64)

    coordinates = [xh]+list(xv)+list(qtt)+phi
    momenta = [r]+list(v)+list(ptt)+pi

    def pb(left, right):
        return s.expand(sum(s.diff(left, a)*s.diff(right, b_)-s.diff(left, b_)*s.diff(right, a)
                            for a, b_ in zip(coordinates, momenta)))

    c = s.Matrix([r]+list(v))
    ac = s.zeros(4)
    ac[0, 1:] = b
    generator = -xh*rho-(xv.T*jv)[0]
    hf = h_grav+hm
    vertex = (q.T*tau)[0]
    invariant = clean(vertex-pb(hf, generator))
    old_ideal = r*bcal-(v.T*bv*jv)[0]
    check('ACTUAL first Ward identity before any completion',
          zero(s.Matrix([pb(ca, vertex)+pb(ja, hm) for ca, ja in zip(c, currents)])-ac*currents))
    check('ACTUAL full invariant remainder is TT vertex plus constraint ideal',
          zero(invariant-cubic-old_ideal))

    g = s.symbols('g', real=True)
    hplus = hm+sum(ptt[a]**2/2+ell*(qtt[a]+g*tt[a]/ell)**2/2 for a in range(2))
    old = hf+g*invariant+g*g*remainder
    new = hplus+kc
    difference = -g*old_ideal
    check('ACTUAL completion is precisely the stated first-class ideal change', zero(new-old-difference))
    check('ACTUAL no physical reduced interaction or g2 term is lost',
          zero(hplus-hm-h_tt-g*cubic-g*g*remainder))
    check('ACTUAL complete free Hamiltonian retained at g0', zero(new.subs(g, 0)-hf))
    zero_c = dict.fromkeys(c, 0)
    check('ACTUAL old and new physical restrictions agree exactly',
          zero((new-old).subs(zero_c)) and zero(new.subs(zero_c)-hplus))
    datum = dict.fromkeys(phi+pi, 0)
    datum[pi[0]] = 1
    datum.update({r: 1, v[0]: 0, v[1]: 0, v[2]: 0, g: 1})
    check('ACTUAL off-shell change is genuinely nonzero', clean(difference.subs(datum)) == -3*rt/128)
    check('ACTUAL exact classical first-class propagation survives',
          zero(s.Matrix([pb(ca, new) for ca in c])-ac*c))
    check('ACTUAL first dressed vertex changes by exactly the advertised ideal',
          zero(pb(hf, generator)+s.diff(new, g).subs(g, 0)-vertex+old_ideal))
    check('ACTUAL change is not a hidden alteration of scalar kinetic energy on the physical section',
          zero(s.hessian(new, pi)-s.eye(8)))
    check('ACTUAL old off-shell kinetic dependence is absent only after the declared change',
          not zero(s.hessian(old, pi)-s.eye(8)))

    # Exact constraint Schr group on arbitrary functions of ALL four
    # actual mode constraints; no finite matrix quantum approximation.
    t, u = s.symbols('t u', real=True)
    phase = t*k-t*t*r*bh*velocity/2+t**3*bh*velocity**2/6
    flow = {r: r-t*velocity}
    check('ACTUAL exact phase is integral of transported scalar potential',
          zero(s.diff(phase, t)-k.subs(flow, simultaneous=True)))
    check('ACTUAL phase cocycle gives all-real-time group law',
          zero(phase+phase.subs(t, u).subs(flow, simultaneous=True)-phase.subs(t, t+u)))
    check('ACTUAL Schrodinger transport phase PDE has correct sign',
          zero(s.diff(phase, t)+velocity*s.diff(phase, r)-k))
    check('ACTUAL wrong transport sign fails for nonconstant scalar potential',
          not zero(s.diff(phase, t)-velocity*s.diff(phase, r)-k))
    check('ACTUAL linear flow preserves Haar and Lebesgue volume', (s.eye(4)+t*ac).det() == 1)
    check('ACTUAL all constraint zeros fixed with zero phase',
          zero(phase.subs(zero_c)) and zero(((s.eye(4)-t*ac)*c).subs(zero_c)))
    function = s.Function('psi')(r, *v)
    kop = lambda z: -s.I*velocity*s.diff(z, r)+k*z
    check('ACTUAL continuous operator scalar-constraint commutator',
          zero(r*kop(function)-kop(r*function)-s.I*velocity*function))
    check('ACTUAL continuous operator vector constraints commute with generator',
          all(zero(va*kop(function)-kop(va*function)) for va in v))
    alpha = s.Matrix(s.symbols('alpha0:4', real=True))
    check('ACTUAL group-parameter covariance uses transposed linear flow',
          zero((alpha.T*(s.eye(4)+t*ac)*c)[0]-(((s.eye(4)+t*ac).T*alpha).T*c)[0]))
    check('ACTUAL first-order generator evaluates to zero at constraint zero',
          zero(kop(function).subs(zero_c)))

    # Rigging normalization and scalar gauge identities are independent
    # continuous controls. The positive physical interacting spectrum is
    # never replaced by the scalar E used only to verify phase signs.
    a = s.symbols('a', real=True)
    gaussian_fourier = s.sqrt(s.pi/2)*s.exp(-a*a/8)
    averaged = s.integrate(gaussian_fourier/(2*s.pi), (a, -s.oo, s.oo))
    check('CONTINUOUS normalized Haar averaging equals evaluation at zero', averaged == 1)
    ss, energy = s.symbols('ss energy', real=True)
    a0, a1, a2 = s.symbols('a0 a1 a2', real=True)
    antiderivative = a0*ss+a1*ss*ss/2+a2*ss**3/3
    phase_regular = s.exp(-s.I*(antiderivative+ss*energy))
    ff = s.Function('f')(ss)
    conjugated = phase_regular*(-s.I*s.diff(ff/phase_regular, ss))
    check('CONTINUOUS regular-orbit scalar and spectral-energy gauges have correct sign',
          zero(conjugated+s.I*s.diff(ff, ss)-(energy+a0+a1*ss+a2*ss*ss)*ff))

    print(json.dumps({'status': 'PASS', 'exact_check_groups': len(checks), 'checks': checks,
                      'actual_source_frontend': str(ward_path),
                      'actual_offshell_difference_on_datum': str(clean(difference.subs(datum))),
                      'finite_actual_source_witness': 'L2, one real retained TT tensor mode, all 8 scalar sites',
                      'scope': 'Declared first-class constraint-ideal completion; proof gives ESA, strong covariance and positive physical norm. Not unchanged H_sr, microscopic selection, locality or complete TFPT.'}, indent=2))


if __name__ == '__main__':
    main()
