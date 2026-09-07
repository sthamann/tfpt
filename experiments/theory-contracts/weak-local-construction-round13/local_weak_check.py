"""Exact actual-model regular point and local/weak construction controls.

Read-only original Ward frontend; no repository edits, no finite CCR
matrices, no numerical flow or global completion inference.
"""
from itertools import product
from pathlib import Path
import json
import runpy
import sympy as s


def pb(f,h,coordinates,momenta):
    return s.expand(sum(s.diff(f,q)*s.diff(h,p)-s.diff(f,p)*s.diff(h,q)
                        for q,p in zip(coordinates,momenta)))


def actual_model_point():
    source = Path(__file__).resolve().parent.parent / 'free-scalar-3d/free_scalar_ward.py'
    module = runpy.run_path(str(source))
    fields = module['Fields'](period=3)
    ward = module['WardComplex'](fields)
    sites = list(product(range(3),repeat=3))
    phi = [fields.phi(x) for x in sites]
    pi = [fields.pi(x) for x in sites]
    def step(x,i,sign=1):
        y = list(x)
        y[i] = (y[i]+sign)%3
        return tuple(y)
    central = [[(fields.phi(step(x,i))-fields.phi(step(x,i,-1)))/2 for x in sites]
               for i in range(3)]
    Jscalar = [s.expand(sum(ward.current(i,x) for x in sites).subs(ward.a,1))
               for i in range(3)]
    for i in range(3):
        assert s.expand(Jscalar[i]+sum(p*d for p,d in zip(pi,central[i]))) == 0
    for i,j in product(range(3),repeat=2):
        assert pb(Jscalar[i],Jscalar[j],phi,pi) == 0

    cosine = [s.Integer(1),-s.Rational(1,2),-s.Rational(1,2)]
    sine = [s.Integer(0),s.sqrt(3)/2,-s.sqrt(3)/2]
    norm = 3*s.sqrt(3)
    weights = [[profile[x[2]]/norm for x in sites] for profile in (cosine,sine)]
    for i,j in product(range(2),repeat=2):
        assert s.simplify(2*sum(a*b for a,b in zip(weights[i],weights[j]))) == int(i==j)
    tau_difference = [s.expand((ward.tau(0,0,x)-ward.tau(1,1,x)).subs(ward.a,1)) for x in sites]
    for index,x in enumerate(sites):
        assert s.expand(tau_difference[index]-central[0][index]**2+central[1][index]**2) == 0
    Tc,Ts = [s.expand(sum(w*T for w,T in zip(row,tau_difference))) for row in weights]
    for T in (Tc,Ts):
        assert T != 0 and not (set(pi)&T.free_symbols) and ward.mass2 not in T.free_symbols

    Qc,Qs,Pc,Ps,g = s.symbols('Qc Qs Pc Ps g',real=True)
    qvars,pvars = phi+[Qc,Qs],pi+[Pc,Ps]
    kappa = s.sqrt(3)/2
    Jtensor = [s.Integer(0),s.Integer(0),kappa*(Qc*Ps-Qs*Pc)]
    Jtotal = [a+b for a,b in zip(Jscalar,Jtensor)]
    Hm = s.expand(sum(ward.rho(x) for x in sites).subs(ward.a,1))
    H0 = Hm+(Pc**2+Ps**2+3*Qc**2+3*Qs**2)/2
    H1 = Qc*Tc+Qs*Ts
    for i in range(3):
        assert s.simplify(pb(Jtotal[i],H0,qvars,pvars)) == 0
    f,a,h = [1,-1,0],[1,2,-1],[1,0,-1]
    point = {fields.phi(x):f[x[0]]*a[x[2]]+h[x[1]] for x in sites}
    point.update({p:0 for p in pi})
    point.update({Qc:1,Pc:1,Qs:0,Ps:0,ward.mass2:1})
    for J in Jtotal:
        assert s.simplify(J.subs(point)) == 0
    gradients = s.Matrix([[d.subs(point) for d in row] for row in central])
    gram = gradients*gradients.T
    assert gram == s.diag(27,s.Rational(27,2),21)
    assert gram.det() == s.Rational(15309,2)
    derivative_rows = s.Matrix([[s.diff(F,z).subs(point) for z in qvars+pvars]
                               for F in Jtotal+[H0]])
    assert derivative_rows.rank() == 4
    values = [s.simplify(T.subs(point)) for T in (Tc,Ts)]
    assert values == [-3*s.sqrt(3)/4,s.Rational(9,4)]
    mismatch = s.simplify(pb(Jtotal[2],H1,qvars,pvars).subs(point))
    assert mismatch == 9*s.sqrt(3)/8
    scalar_piece = s.simplify(pb(Jscalar[2],H1,qvars,pvars).subs(point))
    tensor_piece = s.simplify(pb(Jtensor[2],H1,qvars,pvars).subs(point))
    assert scalar_piece == 9*s.sqrt(3)/4
    assert tensor_piece == -9*s.sqrt(3)/8
    # In the FULL actual Hplus all remaining TT Q,P vanish at this point.
    # They are NOT removed. R depends only on phi, so it contributes no
    # derivative with respect to Qc or Pc. The formulas below are exact.
    qdot = s.diff(H0,Pc).subs(point)
    pdot = s.simplify(-s.diff(H0+g*H1,Qc).subs(point))
    assert qdot == 1
    assert pdot == -3+3*s.sqrt(3)*g/4
    # Repeat the same actual scalar profile on the strict 6^3 regulator,
    # where the preceding global Round12 obstruction also applies. This
    # uses the universal Ward difference identity proved above, not a
    # new scalar stress or a truncation of the TT Hamiltonian.
    sites6 = list(product(range(6),repeat=3))
    values6 = {x:s.Integer(f[x[0]%3]*a[x[2]%3]+h[x[1]%3]) for x in sites6}
    def centered6(configuration,i):
        out = {}
        for x in sites6:
            plus,minus = list(x),list(x)
            plus[i],minus[i] = (x[i]+1)%6,(x[i]-1)%6
            out[x] = (configuration[tuple(plus)]-configuration[tuple(minus)])/2
        return out
    d6 = [centered6(values6,i) for i in range(3)]
    gram6 = s.Matrix([[sum(d6[i][x]*d6[j][x] for x in sites6) for j in range(3)] for i in range(3)])
    assert gram6 == 8*gram and gram6.det() == 3919104
    norm6 = 6*s.sqrt(6)
    Tc6 = s.simplify(sum(cosine[x[2]%3]*(d6[0][x]**2-d6[1][x]**2)/norm6 for x in sites6))
    Ts6 = s.simplify(sum(sine[x[2]%3]*(d6[0][x]**2-d6[1][x]**2)/norm6 for x in sites6))
    dzdx,dzdy = centered6(d6[2],0),centered6(d6[2],1)
    scalar6 = s.simplify(sum(2*cosine[x[2]%3]*(d6[0][x]*dzdx[x]-d6[1][x]*dzdy[x])/norm6 for x in sites6))
    mismatch6 = s.simplify(scalar6-kappa*Ts6)
    assert Tc6 == -3*s.sqrt(6)/2 and Ts6 == 9*s.sqrt(2)/2
    assert mismatch6 == 9*s.sqrt(6)/4
    return {'lattice':[3,3,3], 'mass_squared_for_point':1,
            'phi':'f(x)*a(z)+h(y), f=(1,-1,0), a=(1,2,-1), h=(1,0,-1)',
            'scalar_momenta':'all zero', 'TT_point':'Qc=Pc=1, Qs=Ps=0; all other TT coordinates/momenta zero',
            'seed_total_constraints':'all three zero',
            'rank_dJ0':3,'rank_dH0_dJ0':4,
            'central_difference_Gram_diagonal':[str(gram[i,i]) for i in range(3)],
            'Gram_determinant':str(gram.det()),
            'actual_TT_sources_cos_sin':[str(v) for v in values],
            'full_total_Jz_H1':str(mismatch),
            'actual_Qc_velocity':str(qdot),'actual_Pc_velocity':str(pdot),
            'forced_first_local_correction_slope':str(-mismatch),
            'strict_cubic_6x6x6_regular_witness':{
                'Gram_diagonal':[str(gram6[i,i]) for i in range(3)],
                'Gram_determinant':str(gram6.det()),
                'actual_Tc':str(Tc6),'actual_Ts':str(Ts6),
                'full_total_Jz_H1':str(mismatch6),
                'actual_Qc_velocity':'1',
                'actual_Pc_velocity':str(-3-g*Tc6)}}


def positive_global_counterexample():
    theta,E,Q,P,q2,p2,q3,p3,g = s.symbols('theta E Q P q2 p2 q3 p3 g',real=True)
    qs,ps = [theta,Q,q2,q3],[E,P,p2,p3]
    I = E+g*Q*P
    H = I**2/2
    H0,H1 = E**2/2,E*Q*P
    constraints = [P,p2,p3]
    for i,j in product(range(3),repeat=2):
        assert pb(constraints[i],constraints[j],qs,ps) == 0
    assert s.factor(pb(P,H,qs,ps)) == -g*I*P
    assert pb(p2,H,qs,ps) == pb(p3,H,qs,ps) == 0
    assert pb(P,H1,qs,ps) == -E*P
    K = P*s.exp(g*theta)
    assert s.simplify(pb(K,H,qs,ps)) == 0
    assert s.simplify(K.subs(theta,theta+2*s.pi)-s.exp(2*s.pi*g)*K) == 0
    qnew,pnew,enew = Q*s.exp(-g*theta),K,I
    newq,newp = [theta,qnew,q2,q3],[enew,pnew,p2,p3]
    for i,j in product(range(4),repeat=2):
        assert s.simplify(pb(newq[i],newq[j],qs,ps)) == 0
        assert s.simplify(pb(newp[i],newp[j],qs,ps)) == 0
        assert s.simplify(pb(newq[i],newp[j],qs,ps)) == int(i==j)
    orbit_forcing_integral = s.integrate(P,(theta,0,2*s.pi))
    assert orbit_forcing_integral == 2*s.pi*P
    return {'Hamiltonian':'(E+g QP)^2/2 >= 0 on T*S1 x T*R^3',
            'global_weak_constraints':['P','p2','p3'],
            'weak_M11':'-g(E+gQP)', 'global_constraint_brackets':'zero',
            'local_strong_K':'P exp(g theta)',
            'local_strong_monodromy':'exp(2pi g)',
            'first_order_strong_periodic_obstruction':str(orbit_forcing_integral),
            'canonical_local_coordinate_checks':48}


def exact_weak_rescaling():
    t,e,q1,q2,q3,p1,p2,p3,g = s.symbols('t e q1 q2 q3 p1 p2 p3 g',real=True)
    qs,ps = [t,q1,q2,q3],[e,p1,p2,p3]
    tau = t+q1
    u = s.exp(g*tau)
    constraints = [u*p for p in (p1,p2,p3)]
    for J in constraints:
        assert s.simplify(pb(J,e,qs,ps)-g*J) == 0
    assert s.simplify(pb(constraints[0],constraints[1],qs,ps)+g*u*constraints[1]) == 0
    assert s.simplify(pb(constraints[0],constraints[2],qs,ps)+g*u*constraints[2]) == 0
    assert pb(constraints[1],constraints[2],qs,ps) == 0
    cyclic = sum(pb(constraints[i],pb(constraints[j],constraints[k],qs,ps),qs,ps)
                 for i,j,k in [(0,1,2),(1,2,0),(2,0,1)])
    assert s.simplify(cyclic) == 0
    return {'exact_weak_M':'g identity','nonzero_structure_coefficient_control':True,
            'Jacobi_identity_exact':True,'constraint_surface_unchanged':True}


if __name__ == '__main__':
    print(json.dumps({'status':'PASS','actual_model':actual_model_point(),
                      'positive_global_weak_counterexample':positive_global_counterexample(),
                      'weak_rescaling':exact_weak_rescaling(),
                      'scope':'Exact local hypotheses and controls; flowbox existence is proved in PROOF.md, no global actual-model or gravitational completion.'},indent=2))
