#!/usr/bin/env python3
"""Exact local constrained realization and healthy-Schur sign audit.

No repository imports, approximate CCR, continuum claim or RH work.
See README.md for theorem hypotheses and distinctions between static
constraints, propagating auxiliary oscillators and a full Dirac theory.
"""
import sympy as sp


def zero(value):
    entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
    return all(sp.simplify(sp.factor(entry)) == 0 for entry in entries)


def tensor_data(k):
    rt = sp.sqrt(2)
    b = sp.Matrix([
        [k[0], 0, 0, 0, k[2]/rt, k[1]/rt],
        [0, k[1], 0, k[2]/rt, 0, k[0]/rt],
        [0, 0, k[2], k[1]/rt, k[0]/rt, 0],
    ])
    t = sp.Matrix([1, 1, 1, 0, 0, 0])
    r2 = (k.T*k)[0]
    s = b.T*k-r2*t
    inv = 2*sp.eye(3)/r2-k*k.T/r2**2
    p = sp.eye(6)-b.T*inv*b-s*s.T/(2*r2**2)
    n = sp.Matrix.hstack(b.T, t)
    # Exact block inverse of N.T*N; Bt=k and k.T*(BB.T)^-1*k=1.
    kinv = inv*k
    ni = sp.Matrix.vstack(
        sp.Matrix.hstack(inv+kinv*kinv.T/2, -kinv/2),
        sp.Matrix.hstack(-kinv.T/2, sp.Matrix([[sp.Rational(1, 2)]])),
    )
    return b, t, r2, p, n, ni


def run():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
        print(f"[PASS] {name}", flush=True)

    # Ordinary healthy auxiliary minimization, exact rational matrix witness.
    g = sp.symbols('g', real=True)
    aa = sp.Matrix(sp.symbols('a0:2', real=True))
    jj = sp.Matrix(sp.symbols('j0:2', real=True))
    kk = sp.Matrix([[2, 1], [1, 3]])
    bb = sp.Matrix([[1, 2], [3, -1]])
    astar = -g*kk.inv()*bb*jj
    energy = (aa.T*kk*aa)[0]/2+g*(aa.T*bb*jj)[0]
    emin = -g**2*(jj.T*bb.T*kk.inv()*bb*jj)[0]/2
    shifted = ((aa-astar).T*kk*(aa-astar))[0]/2
    check('healthy Schur identity has negative induced sign', zero(energy-shifted-emin))
    check('healthy auxiliary K is strictly positive', kk[0, 0] > 0 and kk.det() > 0)
    negative = -bb.T*kk.inv()*bb
    check('induced rational two-channel kernel is strictly negative', negative[0, 0] < 0 and negative.det() > 0)
    onechannel = sp.Matrix([[1, 2]])
    check('one auxiliary direction cannot supply a rank-two residue', (onechannel.T*onechannel).rank() == 1)

    l, d = sp.symbols('l d', positive=True)
    kl = l*(d*l-1)
    bl = d*l-1
    check('local finite-volume contact escape is exact', zero(d-bl**2/kl-1/l))
    check('fixed-volume example is healthy at l=4,8,12', all(kl.subs({d: 1, l: n}) > 0 for n in (4, 8, 12)))
    check('same contact escape is unstable at a smaller nonzero momentum', kl.subs({d: 1, l: sp.Rational(1, 2)}) < 0)
    # Gaussian completion, real versus imaginary source coupling.
    u, j = sp.symbols('u j', real=True)
    check('real Gaussian source produces negative effective action', zero(l*u**2/2-g*u*j - (l*(u-g*j/l)**2/2-g**2*j**2/(2*l))))
    check('imaginary Gaussian source produces positive effective action', zero(l*u**2/2-sp.I*g*u*j - (l*(u-sp.I*g*j/l)**2/2+g**2*j**2/(2*l))))

    # Generic nonzero fibre: all quantities are symbolic in the three kappa.
    k = sp.Matrix(sp.symbols('k1:4', real=True))
    b, t, r2, p, n, ni = tensor_data(k)
    check('generic staggered divergence Gram', zero(b*b.T-(r2*sp.eye(3)+k*k.T)/2))
    check('local complement N has rank four for r>0', zero((n.T*n).det()-r2**3/2))
    check('explicit complement Gram inverse', zero(ni*(n.T*n)-sp.eye(4)))
    check('TT projector equals complement elimination', zero(p-(sp.eye(6)-n*ni*n.T)))
    check('TT projector is idempotent', zero(p*p-p))
    check('TT projector has rank two', zero(sp.trace(p)-2))
    check('TT projector annihilates local complement', zero(p*n))
    check('TT projector is traceless and transverse', zero(t.T*p) and zero(b*p))

    div = sp.Matrix.hstack(*(component*sp.eye(6) for component in k))
    check('link divergence is first order with DDt=r2 I6', zero(div*div.T-r2*sp.eye(6)))
    # Verify solution as maps of the full six-component source, avoiding any
    # prior TT projection at the input of the local constraint.
    lambda_map = p/r2
    e_map = div.T*lambda_map
    u_map = -ni*n.T
    check('stationary multiplier obeys local TT conditions', zero(n.T*lambda_map))
    check('stationary E is the multiplier gradient', zero(e_map-div.T*lambda_map))
    check('local constraint matches arbitrary UNPROJECTED source', zero(div*e_map-n*u_map-sp.eye(6)))
    check('minimum energy kernel is positive TT inverse Laplacian', zero(e_map.T*e_map-p/r2))
    check('allowed tangent projector is orthogonal to minimizing E', zero(e_map.T*(sp.eye(18)-e_map*p*div)))
    # PD has rank two because PD D^T P = r2 P.
    check('two constraints on eighteen E components leave sixteen tangents', zero(p*div*div.T*p-r2*p))

    # The source coupling and full positive square identity are universal
    # modulo the local source constraint and TT restrictions.
    q = sp.Matrix(sp.symbols('q0:6', real=True))
    ev = sp.Matrix(sp.symbols('e0:18', real=True))
    source = sp.Matrix(sp.symbols('tau0:6', real=True))
    uv = sp.Matrix(sp.symbols('v0:4', real=True))
    qt = p*q
    residual = div*ev-n*uv-g*source
    full_potential = (qt.T*(r2*qt))[0]/2+g*(qt.T*source)[0]+(ev.T*ev)[0]/2
    square_potential = ((div.T*qt+ev).T*(div.T*qt+ev))[0]/2
    check('full local coupled potential is a square on the constraint', zero(full_potential-square_potential+(qt.T*residual)[0]))

    # A rational fibre provides a bounded exact KKT solve and a concrete
    # divergence-null, non-minimizing field direction.
    subs = dict(zip(k, (0, 0, 2)))
    dn = div.subs(subs)
    pn = p.subs(subs)
    nn = n.subs(subs)
    em = e_map.subs(subs)
    um = u_map.subs(subs)
    lm = lambda_map.subs(subs)
    tau_num = sp.Matrix([2, -1, 4, 3, -2, 5])
    en = em*tau_num
    un = um*tau_num
    ln = lm*tau_num
    kkt = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(18), sp.zeros(18, 4), -dn.T),
        sp.Matrix.hstack(sp.zeros(4, 18), sp.zeros(4), nn.T),
        sp.Matrix.hstack(-dn, nn, sp.zeros(6)),
    )
    rhs = sp.Matrix.vstack(sp.zeros(22, 1), -tau_num)
    solution = sp.Matrix.vstack(en, un, ln)
    check('exact KKT solution uses full source', zero(kkt*solution-rhs))
    check('KKT is nonsingular at a nonzero boundary-compatible fibre', kkt.rank() == 28)
    eta = sp.zeros(18, 1)
    eta[0] = 3
    check('source constraint permits a nonzero divergence-null E direction', zero(dn*eta) and eta != sp.zeros(18, 1))
    check('null direction raises energy and is not another minimizer', zero(((en+eta).T*(en+eta)-en.T*en)[0]/2-sp.Rational(9, 2)))

    # Inherited zero mode: trace is available, five traceless means are not.
    p_trace = t*t.T/3
    p_trfree = sp.eye(6)-p_trace
    check('zero-mode trace slack has rank one', p_trace.rank() == 1)
    check('five traceless homogeneous source directions are missing', p_trfree.rank() == 5)
    mean_tau = sp.Matrix(sp.symbols('mean0:6', real=True))
    h = -g*p_trfree*mean_tau
    chi = -g*(t.T*mean_tau)[0]/3
    check('five constant traceless slacks absorb precisely the deleted means', zero(-t*chi-h-g*mean_tau) and zero(t.T*h))

    # Exact phase placement of all local operators at generic lattice phases.
    phases = sp.symbols('z1:4', nonzero=True)
    plus = [z*z-1 for z in phases]
    minus = [1-z**-2 for z in phases]
    kap = sp.Matrix([(z-1/z)/sp.I for z in phases])
    bf, tf, rf, _, _, _ = tensor_data(kap)
    tensor_phase = sp.diag(1, 1, 1, phases[1]*phases[2], phases[0]*phases[2], phases[0]*phases[1])
    vector_phase = sp.diag(*phases)
    rt = sp.sqrt(2)
    vf = sp.Matrix([
        [plus[0], 0, 0, 0, minus[2]/rt, minus[1]/rt],
        [0, plus[1], 0, minus[2]/rt, 0, minus[0]/rt],
        [0, 0, plus[2], minus[1]/rt, minus[0]/rt, 0],
    ])
    check('local tensor divergence has the actual staggered Fourier phases', zero(vf*tensor_phase-sp.I*vector_phase*bf))
    masks = ((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))
    div_blocks = [sp.diag(*(minus[i] if mask[i] == 0 else plus[i] for mask in masks)) for i in range(3)]
    # adjoint on the unit circle is z -> 1/z and matrix transpose.
    reciprocal = {z: 1/z for z in phases}
    real_div = sp.Matrix.hstack(*div_blocks)
    div_adjoint = real_div.xreplace(reciprocal).T
    check('local oriented link divergence has exact real-space Laplacian Gram', zero(real_div*div_adjoint-rf*sp.eye(6)))

    # Actual free-scalar TT stress loses all momentum dependence under a
    # traceless smearing, unlike a generic collection of quadratic currents.
    momentum, mass, phi = sp.symbols('momentum mass phi', real=True)
    sigma = sp.Matrix(sp.symbols('sigma0:6', real=True))
    actual_tau = sigma+t*(momentum**2-mass**2*phi**2)/2
    check('TT stress removes the common scalar kinetic and mass trace', zero(p*actual_tau-p*sigma))
    charge = phi**2/2
    hm = momentum**2/2
    source_time_derivative = sp.diff(charge, phi)*sp.diff(hm, momentum)
    check('commuting configuration charges still need Hamiltonian stabilization', zero(source_time_derivative-phi*momentum) and source_time_derivative.subs({phi: 1, momentum: 1}) == 1)

    print(f"COUNTS: {len(checks)}/{len(checks)} exact local-auxiliary checks passed")
    print('VERDICT: LOCAL_CONSTRAINED_POSITIVE_STATIC_REALIZATION; HEALTHY_UNCONSTRAINED_SCHUR_SIGN_OBSTRUCTION')
    print('SCOPE: nonzero TT modes plus explicit five-mean bookkeeping; no extra propagators supplied; full local Dirac dynamics and causal parent remain unproved; NON_RH')


if __name__ == '__main__':
    run()

