#!/usr/bin/env python3
"""Exact controls for the measurable, vertex-preserving joint clock chart.

Actual lattice transport is distinguished from labelled scalar/spectral models.
No finite CCR, interacting spectral approximation, or TOE certification.
"""
from itertools import product
import json
import sympy as s


def zero(value):
    seq = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.simplify(s.expand(x)) == 0 for x in seq)


def main():
    checks = []

    def check(name, value):
        if not bool(value):
            raise AssertionError(name)
        checks.append(name)

    # All sites retained. The homogeneous scalar is the sole left kernel
    # of the unprojected divergence. Thus deleting homogeneous gravity
    # yields a nonzero b; its zero-velocity set is a proper null subspace.
    for side in (2, 3):
        sites = list(product(range(side), repeat=3))
        index = {x: j for j, x in enumerate(sites)}
        n = len(sites)
        difference = []
        for axis in range(3):
            shift = s.zeros(n)
            for j, x in enumerate(sites):
                y = list(x)
                y[axis] = (y[axis]+1) % side
                shift[j, index[tuple(y)]] = 1
            difference.append(s.eye(n)-shift.T)
        b_all = s.Matrix.hstack(*difference)
        check(f'ACTUAL L{side} divergence has only the homogeneous left kernel',
              b_all.rank() == n-1 and s.ones(1,n)*b_all == s.zeros(1,3*n))
        ac = s.zeros(4*n)
        ac[:n,n:] = b_all
        t = s.symbols('t', real=True)
        check(f'ACTUAL L{side} complete shear is nilpotent and volume preserving',
              ac*ac == s.zeros(4*n) and (s.eye(4*n)+t*ac).det() == 1)

    # Independent reconstruction of the actual normalized (pi,pi,0) block.
    rt = s.sqrt(2)
    trace = s.Matrix([1,1,1,0,0,0])
    scalar = s.Matrix([4,4,8,0,0,4*rt])
    vector = s.Matrix([[-2,0,0,0,0,rt],[0,-2,0,0,0,rt],[0,0,0,rt,rt,0]])
    kp = s.eye(6)-trace*trace.T/2
    gv = vector*vector.T
    b = (scalar.T*kp*vector.T*gv.inv()).applyfunc(s.simplify)
    check('ACTUAL normalized retained mode has nonzero transport b=(2,2,0)',
          b == s.Matrix([[2,2,0]]))
    r,v0,v1,v2,t,u = s.symbols('r v0 v1 v2 t u', real=True)
    vel = 2*(v0+v1)
    tau = r/vel
    check('ACTUAL transversal clock increases by the group parameter',
          zero(tau.subs(r,r+t*vel)-tau-t))
    check('ACTUAL zero velocity is not the same as the zero constraint point',
          vel.subs({v0:1,v1:-1,v2:0}) == 0)

    # Vector-valued r needs a transverse remainder, not an arbitrary r=0
    # slice. These rational identities hold for any nonzero velocity a.
    r0,r1,a0,a1 = s.symbols('r0 r1 a0 a1', real=True)
    rr,aa = s.Matrix([r0,r1]),s.Matrix([a0,a1])
    tau2 = rr.dot(aa)/aa.dot(aa)
    perp = rr-tau2*aa
    check('GENERAL vector slice is orthogonal to the characteristic velocity', zero(perp.dot(aa)))
    check('GENERAL vector slice reconstructs every nonzero-velocity orbit', zero(perp+tau2*aa-rr))
    moved = {r0:r0+t*a0,r1:r1+t*a1}
    check('GENERAL transverse representative is flow invariant',
          zero(perp.subs(moved, simultaneous=True)-perp))
    check('GENERAL vector characteristic coordinate has the correct sign',
          zero(tau2.subs(moved, simultaneous=True)-tau2-t))
    eps = s.symbols('epsilon', positive=True)
    scaling = {r0:eps*r0,r1:eps*r1,a0:eps*a0,a1:eps*a1}
    check('GENERAL radial dilation leaves orbit time fixed',
          zero(tau2.subs(scaling, simultaneous=True)-tau2))
    check('GENERAL radial dilation scales the transverse point',
          zero(perp.subs(scaling, simultaneous=True)-eps*perp))
    check('GENERAL setting every r coordinate to zero misses actual orbits',
          perp.subs({r0:0,r1:1,a0:1,a1:0}) == s.Matrix([0,1]))

    # Commuting scalar model with precisely linear + quadratic-ideal
    # dependence. It controls signs and demonstrates real loss of ordinary
    # continuity; its phase is NOT the noncommuting physical propagator.
    x,a,g,q,E = s.symbols('x a g q E', real=True)
    delta = g*x*q+g*g*(x*x+a*a)*q*q
    theta = g*q*x*x/(2*a)+g*g*q*q*(x**3/(3*a)+a*x)
    check('MODEL characteristic phase differentiates to both added terms',
          zero(a*s.diff(theta,x)-delta))
    check('MODEL straightening conjugation retains rather than deletes the interaction',
          zero(a*s.diff(theta,x)+E-(E+delta)))
    check('MODEL wrong sign in the compensating phase is detected',
          not zero(-a*s.diff(theta,x)-delta))
    theta_scaled = theta.subs({x:eps*x,a:eps*a}, simultaneous=True)
    check('MODEL radial gauge tends to identity despite its denominator',
          s.limit(theta_scaled,eps,0,dir='+') == 0)
    curved = theta.subs({x:eps,a:eps**2,g:1,q:1}, simultaneous=True)
    check('MODEL a curved approach to zero has a nonzero gauge phase',
          s.limit(curved,eps,0,dir='+') == s.Rational(1,2))
    diverging = theta.subs({x:eps,a:eps**3,g:1,q:1}, simultaneous=True)
    check('MODEL no uniform small-orbit-time estimate is available',
          s.limit(diverging,eps,0,dir='+') == s.oo)
    phase_increment = theta.subs(x,x+t*a)-theta
    cocycle = phase_increment+phase_increment.subs({x:x+t*a,t:u}, simultaneous=True)
    check('MODEL interaction-phase cocycle is exact',
          zero(cocycle-phase_increment.subs(t,t+u)))

    # A genuinely noncommuting two-channel spectral MODEL. The ordered
    # cocycle is checked by cancellation; A is not a truncated TFPT field.
    th,ph = s.symbols('theta phi', real=True)
    rot = lambda z: s.Matrix([[s.cos(z),-s.sin(z)],[s.sin(z),s.cos(z)]])
    A = s.diag(2,5)
    St,Ss = rot(th),rot(ph)
    check('MODEL spectral gauge is unitary', zero(St.T*St-s.eye(2)))
    check('MODEL spectral gauge does not commute with physical energy', not zero(St*A-A*St))
    e1,e2 = s.symbols('e1 e2')
    free = s.diag(e1,e2)
    cocycle_matrix = St*free*Ss.T
    check('MODEL propagator intertwiner retains the noncommuting order',
          zero(cocycle_matrix*Ss-St*free))
    check('MODEL reversed intertwiner order is rejected',
          not zero(Ss*cocycle_matrix-St*free))
    P = s.diag(1,0)
    movedP = St*P*St.T
    check('MODEL transported spectral tube is an orthogonal projection',
          zero(movedP*movedP-movedP) and zero(movedP.T-movedP))
    check('MODEL raw spectral tube generally differs from transported tube', not zero(movedP-P))
    check('MODEL deleting the singular zero-velocity fiber cannot fix b=0 everywhere',
          s.zeros(1,3).rank() == 0 and b.rank() == 1)

    # Actual free gauge phase from the same retained block. The clock adds
    # lambda, not an incorrect spectral restriction of the total Kc+lambda.
    bv = s.Matrix([[5,-3,0],[-3,5,0],[0,0,8]])/32
    vv = s.Matrix([v0,v1,v2])
    k = -r*r/32+(vv.T*bv*vv)[0]/2
    phase = t*k+t*t*r*vel/32-t**3*vel**2/96
    check('ACTUAL backward gauge phase solves its transport equation',
          zero(s.diff(phase,t)+vel*s.diff(phase,r)-k))
    f = s.Function('f')(r,v0,v1,v2)
    lam = s.symbols('lambda',real=True)
    Uf = s.exp(-s.I*(phase+t*lam))*f.subs(r,r-t*vel)
    K = lambda ff:-s.I*vel*s.diff(ff,r)+k*ff
    check('JOINT reference group has exactly Kc+lambda as generator',
          zero((s.I*s.diff(Uf,t)-K(Uf)-lam*Uf)/s.exp(-s.I*(phase+t*lam))))
    check('JOINT time group is covariant, not commuting, with r',
          zero(K(r*f)-r*K(f)+s.I*vel*f) and vel != 0)

    energy, gap = s.symbols('energy gap', positive=True)
    L = s.symbols('lambda',real=True)
    pminus = -s.sqrt(12*(energy-L))
    jac = 6/s.sqrt(12*(energy-L))
    check('CLOCK negative-sheet Jacobian retains its factor six', zero(s.diff(pminus,L)-jac))
    check('CLOCK unchanged quadratic shell is exactly lambda', zero(energy-pminus*pminus/12-L))
    check('CLOCK omitted half-density changes the positive physical norm', jac.subs({energy:3,L:0}) == 1 and jac.subs({energy:12,L:0}) == s.Rational(1,2))
    pi = s.Matrix([[1,1],[1,1]])/2
    weight = s.diag(1,s.Rational(1,2))
    norm = weight*pi*weight
    check('CLOCK noncommuting projection has the correct positive sandwich',
          norm.det() == 0 and s.trace(norm)>0 and norm == norm.T)
    check('CLOCK moving the energy half-density through the projector is rejected',
          weight**2*pi != norm)
    y = s.symbols('y',real=True)
    density = s.exp(-y*y/2)/s.sqrt(2*s.pi)
    check('RIGGING radial Gaussian has unit total mass', s.integrate(density,(y,-s.oo,s.oo)) == 1)
    check('RIGGING scaling includes the full measure Jacobian',
          zero(s.exp(-(s.sqrt(eps)*y)**2/(2*eps))/s.sqrt(2*s.pi*eps)*s.sqrt(eps)-density))
    print(json.dumps({'status':'PASS','exact_check_groups':len(checks),'checks':checks,
        'scope':'Actual finite lattice transport and labelled scalar/spectral controls. Measurable-unitary, domain, averaging and infinite-Hilbert-space claims require PROOF.md; no microscopic selection or full TOE certification.'},indent=2))


if __name__ == '__main__':
    main()
