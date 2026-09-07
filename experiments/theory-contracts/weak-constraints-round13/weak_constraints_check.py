"""Exact actual-model weak-constraint obstruction on a regular null torus.

Standalone; no repository imports, no numerical tolerances, no changed H1/R.
"""
from itertools import combinations_with_replacement
import json
import sympy as s


def clean(expr):
    if isinstance(expr, s.MatrixBase):
        return expr.applyfunc(lambda x: s.simplify(s.expand_complex(x)))
    return s.simplify(s.expand_complex(expr))


ROOT = (1+s.I*s.sqrt(3))/2
L, N = 6, 216


def phase(k, i):
    return clean(ROOT**k[i])


def vertex(k, l):
    """Actual R8 sigma coefficient of uv for two unnormalized plane waves."""
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
    assert r2 != 0  # Homogeneous TT modes are excluded, not inverted.
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
    return P, r2


def main():
    k,l,h = (1,1,0),(2,5,0),(0,0,1)
    neg = lambda p: tuple(-x%L for x in p)
    q = tuple((k[i]+l[i])%L for i in range(3))
    assert q == (3,0,0) and q == neg(q)
    P,r2 = projector(q)
    orth = s.diag(1,1,1,s.sqrt(2),s.sqrt(2),s.sqrt(2))
    projected = clean(P*orth*vertex(k,l))
    assert projected == s.Matrix([0,s.Rational(3,4),-s.Rational(3,4),0,0,0])
    eplus = s.Matrix([0,1,-1,0,0,0])/s.sqrt(2)
    actual_vertex = clean((eplus.T*orth*vertex(k,l))[0])
    assert actual_vertex == 3/(2*s.sqrt(2)) and r2 == 4
    assert vertex(neg(k),neg(l)) == clean(vertex(k,l).conjugate())
    for p in (k,l):
        pp,_ = projector(tuple(2*x%L for x in p))
        assert clean(pp*orth*vertex(p,p)) == s.zeros(6,1)
    assert vertex(k,(0,0,0)) == s.zeros(6,1)

    # Full rank and exact common zero set, including the added pair +/-h.
    weight_units = s.Matrix([[1,1,-1,-1,0,0],
                             [1,-1,-1,1,0,0],
                             [0,0,0,0,1,-1]])
    weight = s.sqrt(3)*weight_units/2
    assert weight*s.ones(6,1) == s.zeros(3,1)
    W = weight[:,[0,1,4]]
    assert s.simplify(W.det()) == -3*s.sqrt(3)/4
    assert W.rank() == 3
    normal = s.zeros(6,3)
    normal[0,0] = normal[1,0] = 1/s.sqrt(3)
    normal[0,1], normal[1,1] = 1/s.sqrt(3),-1/s.sqrt(3)
    normal[4,2] = 2/s.sqrt(3)
    assert clean(weight*normal) == s.eye(3)

    mass2 = s.Rational(4,7)
    wbase = s.sqrt(s.Rational(2,7))
    w1,w2,w3 = 3*wbase,4*wbase,s.sqrt(s.Rational(11,7))
    assert clean(w1**2-(mass2+2)) == 0
    assert clean(w2**2-(mass2+4)) == 0
    assert clean(w3**2-(mass2+1)) == 0
    coupling = clean(actual_vertex/(2*s.sqrt(N*w1*w2)))
    assert coupling**2 == s.Rational(7,18432)

    # One REAL Nyquist TT oscillator, not two complex copies. The target
    # coefficient includes both dynamical pairings; the third was TT-null.
    a,b,c,d,e,f,A,B,C,D,E,F,Q,Pc = s.symbols('a b c d e f A B C D E F Q P')
    annih, create = (a,b,c,d,e,f),(A,B,C,D,E,F)
    variables = annih+create

    def bracket(v,w):
        return s.expand(-s.I*sum(s.diff(v,x)*s.diff(w,X)-s.diff(v,X)*s.diff(w,x)
                                for x,X in zip(annih,create))
                        +s.diff(v,Q)*s.diff(w,Pc)-s.diff(v,Pc)*s.diff(w,Q))

    H0 = w1*(a*A+c*C)+w2*(b*B+d*D)+w3*(e*E+f*F)+(Pc**2+r2*Q**2)/2
    actions = s.Matrix([x*X for x,X in zip(annih,create)])
    J0 = weight*actions
    assert all(s.simplify(bracket(v,H0)) == 0 for v in J0)
    T = coupling*((a+C)*(b+D)+(c+A)*(d+B))
    H1, R = Q*T, T*T/(2*r2)
    frequencies = (w1,w2,w1,w2,w3,w3,-w1,-w2,-w1,-w2,-w3,-w3)
    S1 = 0
    for powers,coefficient in s.Poly(s.expand(T),*variables).terms():
        monomial = s.prod(x**power for x,power in zip(variables,powers))
        omega = s.simplify(sum(power*frequency for power,frequency in zip(powers,frequencies)))
        denominator = s.simplify(r2-omega**2)
        assert denominator != 0
        S1 -= coefficient*(Pc+s.I*omega*Q)*monomial/denominator
    assert s.simplify(bracket(H0,S1)+H1) == 0
    mismatch = bracket(J0[0],H1)
    assert s.simplify(s.Poly(mismatch,Q,Pc,*variables).coeff_monomial(Q*a*b)
                      -s.I*s.sqrt(3)*coupling) == 0
    normal_quartic = s.expand((R+bracket(H1,S1)/2).subs({Q:0,Pc:0}))
    target = a*b*C*D
    coefficient = s.simplify(s.Poly(normal_quartic,*variables).coeff_monomial(target))
    assert coefficient == s.Rational(301,2396160)
    mu = s.symbols('mu',nonnegative=True)
    wg1,wg2 = s.sqrt(mu+2),s.sqrt(mu+4)
    factor = s.simplify(s.Rational(1,2)-1/(4-(wg1+wg2)**2)-1/(4-(wg1-wg2)**2))
    assert s.simplify(factor-(2*mu+5)/(2*(4*mu+7))) == 0
    Cgeneral = 9*(2*mu+5)/(64*N*(4*mu+7)*s.sqrt((mu+2)*(mu+4)))
    assert s.simplify(Cgeneral.subs(mu,mass2)-coefficient) == 0

    # Exhaust ALL pure-scalar quartics on the six occupied modes. Any
    # other actual exchange channel is excluded from the averaged forcing
    # by these selection rules, not assumed absent from the Hamiltonian.
    momenta = (k,l,neg(k),neg(l),h,neg(h))
    physical = momenta+tuple(neg(p) for p in momenta)
    species = (0,1,0,1,2,2)*2
    charge = tuple(tuple(weight_units[j,i] for j in range(3)) for i in range(6))
    charge += tuple(tuple(-x for x in vector) for vector in charge)
    selected = {}
    visited = 0
    for indices in combinations_with_replacement(range(12),4):
        visited += 1
        if any(sum((1 if i<6 else -1) for i in indices if species[i]==j) for j in range(3)):
            continue
        if any(sum(physical[i][j] for i in indices)%L for j in range(3)):
            continue
        charged = tuple(sum(charge[i][j] for i in indices) for j in range(3))
        if any(charged):
            selected[indices] = charged
    assert visited == 1365
    assert selected == {(0,1,8,9):(4,0,0),(2,3,6,7):(-4,0,0)}

    z,w,u = s.symbols('z w u',nonzero=True)
    eps = s.symbols('epsilon',positive=True)
    torus = {a:eps*z,b:eps*w,c:eps*z,d:s.I*eps*w,e:eps*u,f:eps*u,
             A:eps/z,B:eps/w,C:eps/z,D:-s.I*eps/w,E:eps/u,F:eps/u}
    assert all(s.simplify(v.subs(torus,simultaneous=True)) == 0 for v in J0)
    average = []
    for component in J0:
        forcing = s.expand(bracket(component,normal_quartic).subs(torus,simultaneous=True))
        average.append(s.simplify(forcing.coeff(z,0).coeff(w,0).coeff(u,0)))
    expected_mean = s.Rational(301,599040)*s.sqrt(3)*eps**4
    assert average == [expected_mean,0,0]
    assert s.simplify(expected_mean-4*s.sqrt(3)*coefficient*eps**4) == 0

    # Generic displaced-surface jet: C=j+g(f+Bj)+g^2 h. f,B,h depend on
    # the base flow parameter but not on the normal j in this jet.
    # This explicitly retains the term B f omitted by the naive argument.
    g = s.symbols('g')
    fv = s.Matrix(s.symbols('f0:3'))
    hv = s.Matrix(s.symbols('h0:3'))
    bv = s.Matrix(s.symbols('b0:3'))
    fm = s.Matrix(s.symbols('df0:3'))
    hm = s.Matrix(s.symbols('dh0:3'))
    mat = s.Matrix(3,3,s.symbols('B0:9'))
    dmat = s.Matrix(3,3,s.symbols('dB0:9'))
    chi1,chi2 = -fv,mat*fv-hv
    graph = g*chi1+g**2*chi2
    graph_constraint = graph+g*(fv+mat*graph)+g**2*hv
    assert all(s.expand(v).coeff(g,j) == 0 for v in graph_constraint for j in range(3))
    second_bracket_on_graph = bv+hm-dmat*fv
    X0chi2 = dmat*fv+mat*fm-hm
    assert s.simplify(second_bracket_on_graph-(bv-X0chi2+mat*fm)) == s.zeros(3,1)
    # At first order X0 f=0, so weak preservation is precisely b=X0 chi2.
    assert (second_bracket_on_graph-(bv-X0chi2)).subs(dict.fromkeys(fm,0)) == s.zeros(3,1)
    # Negative control: discarding the shifted-surface term is generically wrong.
    assert dmat*fv != s.zeros(3,1)

    print(json.dumps({
        'status':'PASS',
        'lattice':[L,L,L],
        'mass_squared':str(mass2),
        'six_active_momenta':momenta,
        'all_six_action_values_at_epsilon_1':1,
        'common_J0_zero':True,
        'normal_weight_determinant':str(s.simplify(W.det())),
        'actual_Nyquist_TT_uv_vertex':str(actual_vertex),
        'actual_cubic_normal_form_checked':True,
        'actual_quartic_coefficient':str(coefficient),
        'general_mass_coefficient':str(Cgeneral),
        'quartic_monomials_exhausted':visited,
        'all_charged_T3_balanced_monomials':[[list(p),list(map(int,c))] for p,c in selected.items()],
        'full_mean_vector':[str(v) for v in average],
        'shifted_surface_second_order_term_checked':True,
        'conclusion':'NO_SMOOTH_ORDER_G2_WEAK_PRESERVATION_NEAR_THE_REGULAR_NULL_TORUS',
        'scope':'Prescribed three total centered momenta; unchanged actual Hamiltonian; smooth time-independent constraints and structure functions. No pointwise flowbox, added-clock, singular-g or different-generator no-go.'
    },indent=2))


if __name__ == '__main__':
    main()
