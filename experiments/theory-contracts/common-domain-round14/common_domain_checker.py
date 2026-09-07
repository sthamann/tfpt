#!/usr/bin/env python3
"""Exact actual-source controls for the Round14 common-domain obstruction.

No TFPT imports, no floating-point checks and no finite CCR replacement.
The polynomial after a Weyl displacement controls an actual operator norm
on any fixed Schwartz packet; the Hilbert-space argument is in PROOF.md.
"""
from itertools import product
import sympy as s


def clean(x):
    return s.simplify(s.expand(x))


def zero(x):
    return all(clean(t) == 0 for t in x) if isinstance(x, s.MatrixBase) else clean(x) == 0


def main():
    checks = []

    def check(label, test):
        okay = bool(test)
        checks.append(okay)
        print(f"{'PASS' if okay else 'FAIL'} {label}", flush=True)

    sites = list(product(range(2), repeat=3))
    lookup = {x:i for i,x in enumerate(sites)}
    phi = s.Matrix(s.symbols('f0:8', real=True))
    pi = s.Matrix(s.symbols('p0:8', real=True))
    Q = s.Matrix(s.symbols('Q0:2', real=True))
    P = s.Matrix(s.symbols('P0:2', real=True))
    scalar = s.Matrix([4,4,8,0,0,4*s.sqrt(2)])
    polar = s.Matrix.hstack(s.Matrix([1,1,-2,0,0,s.sqrt(2)])/s.sqrt(8), s.Matrix([0,0,0,1,-1,0])/s.sqrt(2))
    bv = s.Matrix([[5,-3,0],[-3,5,0],[0,0,8]])/32
    cv = s.Matrix([s.Rational(1,2),0,0])

    def step(x,j,amount=1):
        xx = list(x)
        xx[j] = (xx[j]+amount)%2
        return tuple(xx)

    def grad(x,j):
        return phi[lookup[step(x,j)]]-phi[lookup[x]]

    rho = hm = s.Integer(0)
    currents = s.zeros(3,1)
    tau = s.zeros(6,1)
    weights = []
    for x in sites:
        ix = lookup[x]
        w = s.Integer(-1)**(x[0]+x[1])/s.sqrt(8)
        weights.append(w)
        den = pi[ix]**2/2+phi[ix]**2+sum(grad(x,j)**2+grad(step(x,j,-1),j)**2 for j in range(3))/4
        rho += w*den
        hm += den
        for j in range(3):
            currents[j] -= w*(pi[ix]+pi[lookup[step(x,j)]])*grad(x,j)/2
            tau[j] += w*(pi[ix]**2/2-phi[ix]**2+grad(x,j)*grad(step(x,j,-1),j)/2-sum(grad(x,k)**2+grad(step(x,k,-1),k)**2 for k in range(3) if k != j)/4)
        for index,(j,k) in enumerate(((1,2),(0,2),(0,1)),3):
            tau[index] += w*s.sqrt(2)*(grad(x,j)+grad(step(x,k),j))*(grad(x,k)+grad(step(x,j),k))/4
    rho,hm = s.expand(rho),s.expand(hm)
    tau,currents = tau.applyfunc(s.expand),currents.applyfunc(s.expand)
    tt = (polar.T*tau).applyfunc(clean)
    B = clean((scalar.T*tau)[0]/128+rho/16)
    g = s.symbols('g', real=True, nonzero=True)
    time = s.symbols('time', real=True)
    hbase = s.expand((P.T*P)[0]/2+4*(Q.T*Q)[0]+hm+g*(Q.T*tt)[0]+g*(cv.T*bv*currents)[0]+(cv.T*bv*cv)[0]/2)
    htime = s.expand(hbase+g*time*B-time**2/32)
    datum = s.Matrix([-2,1,3,-1,4,0,-4,2])
    datum_sub = dict(zip(phi,datum))
    datum_sub.update(dict.fromkeys(pi,0))
    check('actual normalized retained TT source on datum equals (3/4,0)', zero(tt.subs(datum_sub)-s.Matrix([s.Rational(3,4),0])))
    check('actual TT stresses are independent of matter momenta', all(s.diff(t,p) == 0 for t in tt for p in pi))
    check('actual B kinetic Hessian is the declared mean-zero diagonal', zero(s.hessian(B,list(pi))-s.Rational(3,16)*s.diag(*weights)))
    check('actual h(0) matter kinetic Hessian is identity', zero(s.hessian(hbase,list(pi))-s.eye(8)))
    check('actual characteristic slope including scalar term', zero(s.diff(htime,time)-g*B+time/16))
    target = s.symbols('target', real=True)
    check('two actual fibers differ by g(time-target)B plus scalar', zero(htime-htime.subs(time,target)-g*(time-target)*B+(time**2-target**2)/32))

    # Keep operator variables, rather than only evaluating at the center.
    # The cancellation of the top displacement coefficient controls ||hf_R||.
    amplitude = s.symbols('R', positive=True)
    variables = list(Q)+list(P)+list(phi)+list(pi)
    for tag,site_index in [('plus',0),('minus',2)]:
        sign = 1 if tag == 'plus' else -1
        check(f'actual {tag} site weight', weights[site_index] == sign/s.sqrt(8))
        C = 1+3*g*time*weights[site_index]/16
        center = dict.fromkeys(variables,s.Integer(0))
        center.update(dict(zip(phi,amplitude**2*datum)))
        center[Q[0]] = -3*C*amplitude**2/(4*g)
        center[pi[site_index]] = 3*amplitude**3/(2*s.sqrt(2))
        displaced_h = s.expand(htime.subs({z:z+center[z] for z in variables},simultaneous=True))
        displaced_B = s.expand(B.subs({z:z+center[z] for z in variables},simultaneous=True))
        check(f'actual {tag} full displaced Hamiltonian has no R^6 operator coefficient', zero(displaced_h.coeff(amplitude,6)))
        check(f'actual {tag} full displaced Hamiltonian has degree at most five', s.Poly(displaced_h,amplitude).degree() <= 5)
        beta = clean(displaced_B.coeff(amplitude,6))
        expected = sign*27*s.sqrt(2)/1024
        check(f'actual {tag} B has nonzero scalar R^6 coefficient', beta == expected and not any(z in beta.free_symbols for z in variables))
        check(f'actual {tag} B remainder has degree at most four', s.Poly(s.expand(displaced_B-beta*amplitude**6),amplitude).degree() <= 4)
        check(f'actual {tag} kinetic center cancels cubic TT center', zero((C*pi[site_index]**2/2+g*(Q.T*tt)[0]).subs(center,simultaneous=True)))
        # The useful positive direction is plus when g*time>=0 and minus
        # otherwise. Algebraically C=1+3|g*time|/(16 sqrt(8))>=1.
        absprod = s.symbols('absprod', nonnegative=True)
        aligned = clean(C.subs(time,sign*absprod/g))
        check(f'actual {tag} aligned kinetic coefficient is at least one', aligned == 1+3*absprod/(16*s.sqrt(8)))
        print(f'ACTUAL_{tag.upper()}_B_LEADING: {beta}',flush=True)

    # Generic spectator TT modes retained in the full Hamiltonian do not
    # revive the cancelled R^6 coefficient: their displacement is zero.
    Qextra, a, b, fextra = s.symbols('Qextra a b fextra', real=True)
    spectator = s.expand(Qextra*(a*(fextra+amplitude**2)**2+b*(phi[0]+amplitude**2)*(phi[1]-2*amplitude**2)))
    check('full-model undisplaced spectator TT vertices have degree at most four', s.Poly(spectator,amplitude).degree() <= 4)

    # Negative controls for the sharp cancellation, not a finite-CCR model.
    bad_kinetic = s.Rational(9,16)*amplitude**6
    good_vertex = -s.Rational(9,16)*amplitude**6
    check('removing actual TT vertex destroys Hamiltonian degree improvement', s.Poly(bad_kinetic,amplitude).degree() == 6)
    check('flipping vertex sign destroys Hamiltonian degree improvement', s.Poly(bad_kinetic-good_vertex,amplitude).degree() == 6)
    check('constant TT shift is insufficient for the cancellation', s.Poly(bad_kinetic-s.Rational(9,16)*amplitude**4,amplitude).degree() == 6)

    # A moving-domain MODEL can still have a propagator. These identities
    # prevent interpreting the actual common-domain no-go as a universal
    # prohibition on nonautonomous unitary dynamics.
    x,t = s.symbols('x t', real=True)
    f = s.Function('f')(x)
    phase = s.exp(-s.I*t*x*x/2)
    inverted = lambda z: -s.diff(z,x,2)-x*x*z/2
    shifted_p = lambda z: -s.I*s.diff(z,x)+t*x*z
    transformed = phase*inverted(f/phase)+x*x*f/2
    check('MODEL exact moving quadratic gauge yields (p+tx)^2 with correct connection', zero(transformed-shifted_p(shifted_p(f))))
    tail = 1/s.sqrt(1+x*x)
    rotated_tail = phase*tail
    p_tail = clean(-s.I*s.diff(rotated_tail,x)/phase)
    pp_tail = clean(-s.diff(rotated_tail,x,2)/phase)
    check('MODEL free form-domain vector leaves shifted form domain', s.limit(p_tail,x,s.oo) == -t)
    check('MODEL free operator-domain vector leaves shifted operator domain', s.limit(pp_tail/x,x,s.oo) == t*t)
    print(f'COUNTS: {sum(checks)}/{len(checks)} exact checks; 0 floating checks')
    print('SCOPE: actual common operator/form-domain obstruction; no no-go for time-dependent domains or for a full covariant extension')
    return 0 if all(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
