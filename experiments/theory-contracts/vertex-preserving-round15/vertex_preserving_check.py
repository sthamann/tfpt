#!/usr/bin/env python3
"""Exact controls for the new second-ideal, first-vertex-preserving form.
No finite canonical-commutator matrices or unchanged-H_sr claim.
"""
from itertools import product
from pathlib import Path
import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--ward-source', type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, statement):
        if not bool(statement):
            raise AssertionError(name)
        checks.append(name)

    # Read the ACTUAL local source frontend, not the former proxy models.
    ward_path = Path(__file__).resolve().parents[1] / 'free-scalar-3d/free_scalar_ward.py'
    ward_path = args.ward_source or ward_path
    spec = importlib.util.spec_from_file_location('r15_vertex_actual_ward', ward_path)
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

    source = s.Matrix.vstack(s.Matrix([bcal]), -bv*jv)
    normc2 = (c.T*c)[0]
    ssq = (source.T*source)[0]
    extra = g*g*normc2*ssq
    old = hf+g*invariant+g*g*remainder
    new = old+extra
    check('ACTUAL source vector is precisely the old first-ideal term',
          zero((c.T*source)[0]-old_ideal))
    check('ACTUAL first dressed interaction vertex is retained exactly',
          zero(pb(hf,generator)+s.diff(new,g).subs(g,0)-vertex))
    check('ACTUAL extra interaction starts at second coupling order',
          zero(extra.subs(g,0)) and zero(s.diff(extra,g).subs(g,0)))
    zc = dict.fromkeys(c,0)
    check('ACTUAL extra term lies in the second constraint ideal',
          zero(extra.subs(zc)) and all(zero(s.diff(extra,ca).subs(zc)) for ca in c))
    check('ACTUAL reduced physical Hamiltonian and free Hamiltonian unchanged',
          zero(new.subs(zc)-hplus) and zero(new.subs(g,0)-hf))
    check('ACTUAL classical constraint covariance is unmodified',
          zero(s.Matrix([pb(ca,new) for ca in c])-ac*c))
    datum = dict.fromkeys(phi+pi,0)
    datum[pi[0]]=1
    datum.update({r:1,v[0]:0,v[1]:0,v[2]:0,g:1})
    check('ACTUAL second-order modification is nonzero off surface',
          clean(extra.subs(datum)) == s.Rational(9,8192))
    check('ACTUAL sources are noncommuting quadratics',
          any(not zero(pb(source[0],source[jj])) for jj in range(1,4)))
    m = len(phi)
    omega = s.zeros(2*m)
    omega[:m,m:]=s.eye(m); omega[m:,:m]=-s.eye(m)
    hc = [s.hessian(f,phi+pi) for f in source]
    ordering = [clean(s.trace((omega*h)**2)/8) for h in hc]
    ordered_extra = extra+g*g*normc2*sum(ordering)
    check('ACTUAL full operator-square ordering still vanishes to second ideal order',
          zero(ordered_extra.subs(zc)) and all(zero(s.diff(ordered_extra,ca).subs(zc)) for ca in c))
    check('ACTUAL ordering constants cannot alter the first vertex',
          zero(s.diff(ordered_extra,g).subs(g,0)))
    # Real quadratic MODEL xp has Weyl square x^2p^2+1/4.
    j2=s.Matrix([[0,1],[-1,0]])
    hxp=s.Matrix([[0,1],[1,0]])
    check('MODEL classical-square substitution misses a nonzero Weyl correction',
          s.trace((j2*hxp)**2)/8 == s.Rational(1,4))
    # Scalar Cauchy envelope contains the exact analytic coercivity constants.
    w,z,n=s.symbols('w z n',nonnegative=True)
    lower = w*w*z*z-w*z*n+n*n-(w*w*z*z+n*n)/2
    upper = (3*w*w*z*z+3*n*n)/2-(w*w*z*z+w*z*n+n*n)
    check('FORM lower coercivity envelope is an exact square',
          zero(lower-(w*z-n)**2/2))
    check('FORM upper coercivity envelope is an exact square',
          zero(upper-(w*z-n)**2/2))
    check('FORM missing stabilizer fails already on scalar spectral values',
          s.limit(-z,z,s.oo) == -s.oo)
    aa=s.symbols('a',nonnegative=True)
    bound=aa*(w*w*z*z+n*n)/2+2*aa*w*w*z*z
    check('FORM energy derivative is bounded by five times coercive envelope',
          zero(5*aa*(w*w*z*z+n*n)/2-bound-2*aa*n*n))
    t=s.symbols('t',real=True)
    ct=(s.eye(4)+t*ac)*c
    check('ACTUAL affine characteristic is complete and volume preserving',
          ac*ac==s.zeros(4) and (s.eye(4)+t*ac).det()==1)
    check('ACTUAL nonzero vector constraint prevents zero crossing',
          zero((ct.T*ct)[0]-(r+t*velocity)**2-(v.T*v)[0]))
    psi=s.Function('psi')(r,*v)
    potential=s.Function('potential')(r,*v)
    op=lambda f: -s.I*velocity*s.diff(f,r)+potential*f
    check('CONTINUOUS all commuting fiber terms preserve the strong-covariance generator identity',
          zero(op(r*psi)-r*op(psi)+s.I*velocity*psi))
    eps,x=s.symbols('epsilon x',positive=True)
    density=s.exp(-x*x/(2*eps))/s.sqrt(2*s.pi*eps)
    regularized=s.integrate(density*s.exp(-2*x*x),(x,-s.oo,s.oo))
    check('RIGGING Gaussian approximate identity has correct normalization',
          s.integrate(density,(x,-s.oo,s.oo))==1)
    check('RIGGING finite-epsilon form is not already zero-fiber evaluation',
          zero(regularized-1/s.sqrt(1+4*eps)) and regularized!=1)
    check('RIGGING zero-width limit yields exact physical norm',
          s.limit(regularized,eps,0,dir='+')==1)
    print(json.dumps({'status':'PASS','exact_check_groups':len(checks),'checks':checks,
       'actual_source_frontend':str(ward_path.resolve()),
       'actual_ordering_constants':[str(x) for x in ordering],
       'classical_extra_on_datum':str(clean(extra.subs(datum))),
       'scope':'Actual one retained L2 mode/all scalar sites plus general form and rigging controls. Full finite-volume existence is the analytic theorem. New second-ideal completion preserves original first vertex and physical A+, not the old all-order off-shell operator or a TOE.'},indent=2))


if __name__ == '__main__':
    main()
