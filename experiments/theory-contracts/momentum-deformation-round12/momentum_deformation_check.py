"""Exact Round-12 actual TT vertex and resonant momentum obstruction.

No repository imports, floating-point tests, or changed Hamiltonian.
"""
from itertools import combinations_with_replacement
import json
import sympy as s


def clean(expr):
    if isinstance(expr, s.MatrixBase):
        return expr.applyfunc(lambda a: s.simplify(s.expand_complex(a)))
    return s.simplify(s.expand_complex(expr))


ROOT = (1+s.I*s.sqrt(3))/2
L = 6
N = L**3


def phase(k, i):
    return clean(ROOT**k[i])


def vertex(k, l):
    """Coefficient uv in actual sigma(u exp(ikx)+v exp(ilx))."""
    ek, el = [phase(k,i) for i in range(3)], [phase(l,i) for i in range(3)]
    dk, dl = [z-1 for z in ek], [z-1 for z in el]
    diag = [dk[i]*dl[i]*(1/ek[i]+1/el[i])/2
            -sum(dk[j]*dl[j]*(1+1/(ek[j]*el[j]))/2 for j in range(3) if j != i)
            for i in range(3)]
    off = [(dk[i]*(1+ek[j])*dl[j]*(1+el[i])+dl[i]*(1+el[j])*dk[j]*(1+ek[i]))/4
           for i,j in ((1,2),(0,2),(0,1))]
    return clean(s.Matrix(diag+off))


def projector(q):
    zz = [phase(q,i) for i in range(3)]
    d = s.Matrix([z-1 for z in zz])
    r2 = clean(sum(2-z-1/z for z in zz))
    rt = s.sqrt(2)
    V = s.Matrix([[d[0],0,0,0,(1-1/zz[2])/rt,(1-1/zz[1])/rt],
                  [0,d[1],0,(1-1/zz[2])/rt,0,(1-1/zz[0])/rt],
                  [0,0,d[2],(1-1/zz[1])/rt,(1-1/zz[0])/rt,0]])
    t = s.Matrix([1,1,1,0,0,0])
    S = clean(V.conjugate().T*d-r2*t)
    P = clean(s.eye(6)-V.conjugate().T*(2*s.eye(3)/r2-d*d.conjugate().T/r2**2)*V-S*S.conjugate().T/(2*r2**2))
    assert clean(P*P-P) == s.zeros(6)
    assert clean(P*t) == s.zeros(6,1)
    assert clean(V*P) == s.zeros(3,6)
    return P,r2


def main():
    k,l = (1,1,0),(2,5,0)
    q = tuple((k[i]+l[i])%L for i in range(3))
    assert q == (3,0,0)
    raw = vertex(k,l)
    orth = s.diag(1,1,1,s.sqrt(2),s.sqrt(2),s.sqrt(2))*raw
    P,r2 = projector(q)
    projected = clean(P*orth)
    expected = s.Matrix([0,s.Rational(3,4),-s.Rational(3,4),0,0,0])
    assert projected == expected
    reverse_raw = vertex(tuple(-x%L for x in k),tuple(-x%L for x in l))
    assert reverse_raw == clean(raw.conjugate())
    unit_plus = s.Matrix([0,1,-1,0,0,0])/s.sqrt(2)
    vertex_plus = clean((unit_plus.T*orth)[0])
    assert vertex_plus == 3/(2*s.sqrt(2))
    assert r2 == 4
    # Other partition of the charge-changing quartet has two equal scalar
    # momenta in each source. Its actual TT vertex is zero (also Omega=0).
    for p in (k,l):
        pq = tuple(2*v % L for v in p)
        pp,_ = projector(pq)
        doubled = s.diag(1,1,1,s.sqrt(2),s.sqrt(2),s.sqrt(2))*vertex(p,p)
        assert clean(pp*doubled) == s.zeros(6,1)
    assert vertex(k,(0,0,0)) == s.zeros(6,1)

    mass2 = s.Rational(4,7)
    wbase = s.sqrt(s.Rational(2,7))
    w1,w2 = 3*wbase,4*wbase
    assert clean(w1**2-(mass2+2)) == 0
    assert clean(w2**2-(mass2+4)) == 0
    coupling = clean(vertex_plus/(2*s.sqrt(N*w1*w2)))
    assert coupling**2 == s.Rational(7,18432)
    assert (w1+w2)**2 == 14
    assert (w1-w2)**2 == s.Rational(2,7)

    aa,bb,cc,dd,AA,BB,CC,DD,Q,Pc = s.symbols('a b c d A B C D Q P')
    annihilators, creators = (aa,bb,cc,dd),(AA,BB,CC,DD)
    def bracket(f,h):
        return s.expand(-s.I*sum(s.diff(f,a)*s.diff(h,A)-s.diff(f,A)*s.diff(h,a)
                                for a,A in zip(annihilators,creators))
                        +s.diff(f,Q)*s.diff(h,Pc)-s.diff(f,Pc)*s.diff(h,Q))
    H0 = w1*(aa*AA+cc*CC)+w2*(bb*BB+dd*DD)+(Pc**2+r2*Q**2)/2
    sin_value = s.sqrt(3)/2
    J0 = sin_value*(aa*AA+bb*BB-cc*CC-dd*DD)
    T = coupling*((aa+CC)*(bb+DD)+(cc+AA)*(dd+BB))
    H1 = Q*T
    quartic_R = T*T/(2*r2)
    mismatch = bracket(J0,H1)
    assert s.simplify(s.Poly(mismatch,Q,Pc,*annihilators,*creators).coeff_monomial(Q*aa*bb)
                      -s.I*s.sqrt(3)*coupling) == 0

    # Solve {H0,S1}=-H1 monomial by monomial, with the full scalar frequency.
    scalar_variables = annihilators+creators
    frequencies = (w1,w2,w1,w2,-w1,-w2,-w1,-w2)
    S1 = 0
    for powers, coefficient in s.Poly(s.expand(T),*scalar_variables).terms():
        monomial = s.prod(variable**power for variable,power in zip(scalar_variables,powers))
        Omega = s.simplify(sum(power*frequency for power,frequency in zip(powers,frequencies)))
        denominator = s.simplify(r2-Omega**2)
        assert denominator != 0
        S1 -= coefficient*(Pc+s.I*Omega*Q)*monomial/denominator
    assert s.simplify(bracket(H0,S1)+H1) == 0
    J1 = -bracket(J0,S1)
    assert s.simplify(bracket(J1,H0)+mismatch) == 0
    H2 = s.expand(quartic_R+bracket(H1,S1)/2)
    H2_scalar = s.expand(H2.subs({Q:0,Pc:0}))
    target = aa*bb*CC*DD
    coefficient = s.simplify(s.Poly(H2_scalar,*scalar_variables).coeff_monomial(target))
    assert coefficient == s.Rational(301,2396160)
    dynamic_factor = s.simplify(2/r2-1/(r2-(w1+w2)**2)-1/(r2-(w1-w2)**2))
    assert dynamic_factor == s.Rational(43,130)
    assert coefficient == s.simplify(coupling**2*dynamic_factor)
    mass_general = s.symbols('mu', nonnegative=True)
    wg1,wg2 = s.sqrt(mass_general+2),s.sqrt(mass_general+4)
    general_factor = s.simplify(s.Rational(1,2)-1/(4-(wg1+wg2)**2)-1/(4-(wg1-wg2)**2))
    assert s.simplify(general_factor-(2*mass_general+5)/(2*(4*mass_general+7))) == 0
    general_coefficient = 9*(2*mass_general+5)/(64*N*(4*mass_general+7)*s.sqrt((mass_general+2)*(mass_general+4)))
    assert s.simplify(general_coefficient.subs(mass_general,mass2)-coefficient) == 0

    # All full-Hamiltonian degree-four resonances on these four occupied
    # travelling modes with nonzero central translation charge are exactly
    # target and its complex conjugate. Thus omitted intermediate TT modes
    # cannot supply an additional resonant charge-changing monomial.
    physical_momenta = (k,l,tuple(-x%L for x in k),tuple(-x%L for x in l),
                        tuple(-x%L for x in k),tuple(-x%L for x in l),k,l)
    freq_units = (3,4,3,4,-3,-4,-3,-4)
    central_charges = (1,1,-1,-1,-1,-1,1,1)  # in units sqrt(3)/2
    charged_resonances = set()
    charged_torus_balanced = set()
    possible_unbalanced_ratios = set()
    for indices in combinations_with_replacement(range(8),4):
        delta1 = sum((1 if i<4 else -1) for i in indices if i in (0,2,4,6))
        delta2 = sum((1 if i<4 else -1) for i in indices if i in (1,3,5,7))
        if delta2 != 0 and -s.Rational(delta1,delta2) > 0:
            possible_unbalanced_ratios.add(-s.Rational(delta1,delta2))
        momentum_zero = all(sum(physical_momenta[i][j] for i in indices)%L == 0 for j in range(3))
        charge_nonzero = sum(central_charges[i] for i in indices) != 0
        if delta1 == delta2 == 0 and momentum_zero and charge_nonzero:
            charged_torus_balanced.add(tuple(indices))
        if sum(freq_units[i] for i in indices) != 0:
            continue
        if any(sum(physical_momenta[i][j] for i in indices)%L != 0 for j in range(3)):
            continue
        if sum(central_charges[i] for i in indices) == 0:
            continue
        charged_resonances.add(tuple(indices))
    assert charged_resonances == {(0,1,6,7),(2,3,4,5)}
    assert charged_torus_balanced == charged_resonances
    assert possible_unbalanced_ratios == {s.Rational(1,3),s.Integer(1),s.Integer(3)}
    assert not any(ratio > 1 and ratio**2 <= 2 for ratio in possible_unbalanced_ratios)

    # A truly periodic H0 orbit: common frequency sqrt(2/7), period 2pi/base.
    # a=b=c=1,d=i initially, with conjugate creators. Q=P=0 stays so.
    z = s.symbols('z',nonzero=True)
    orbit = {aa:z**3,bb:z**4,cc:z**3,dd:s.I*z**4,
             AA:z**-3,BB:z**-4,CC:z**-3,DD:-s.I*z**-4}
    forcing = s.expand(bracket(J0,H2_scalar))
    orbit_forcing = s.expand(forcing.subs(orbit,simultaneous=True))
    exact_orbit_average = s.simplify(orbit_forcing.coeff(z,0))
    assert exact_orbit_average == s.Rational(301,599040)*s.sqrt(3)
    assert exact_orbit_average == 4*s.sqrt(3)*coefficient
    w = s.symbols('w',nonzero=True)
    torus = {aa:z,bb:w,cc:z,dd:s.I*w,AA:z**-1,BB:w**-1,CC:z**-1,DD:-s.I*w**-1}
    torus_forcing = s.expand(forcing.subs(torus,simultaneous=True))
    exact_torus_average = s.simplify(torus_forcing.coeff(z,0).coeff(w,0))
    assert exact_torus_average == exact_orbit_average
    assert s.simplify(J0.subs({aa:1,bb:1,cc:1,dd:s.I,AA:1,BB:1,CC:1,DD:-s.I})) == 0

    print(json.dumps({"status":"PASS","cubic_lattice":[6,6,6],
                      "mass_squared":str(mass2),"k":k,"l":l,"TT_mediator":q,
                      "actual_TT_plus_uv_vertex":str(vertex_plus),
                      "order_g_centered_translation_mismatch_nonzero":True,
                      "cubic_homological_equation_exact":True,
                      "first_order_J1_correction_exact":True,
                      "static_plus_exchange_factor":str(dynamic_factor),
                      "resonant_quartic_coefficient":str(coefficient),
                      "general_mass_static_plus_exchange_factor":str(general_factor),
                      "general_mass_resonant_coefficient":str(general_coefficient),
                      "all_charged_quartic_resonances":sorted(charged_resonances),
                      "periodic_orbit_mean_J0_H2":str(exact_orbit_average),
                      "independent_T2_phase_mean_J0_H2":str(exact_torus_average),
                      "verdict":"NO_GLOBAL_SMOOTH_ORDER_G2_STRONGLY_CONSERVED_DEFORMATION_OF_THE_SPECIFIED_J0",
                      "scope":"Fixed actual Hred+ and seed J0; periodic m2=4/7 witness plus all-m2>=0 compact-torus proof in companion; arbitrary smooth J1,J2, not only polynomial ansatz. Weak constraint-proportional closure remains open."},indent=2))


if __name__ == '__main__':
    main()
