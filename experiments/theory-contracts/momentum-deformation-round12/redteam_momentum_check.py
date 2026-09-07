"""Independent actual-source, Fourier, nullspace and exchange audit.

The original Ward frontend is read only. No repository mutations and no
finite-dimensional approximation to canonical commutators are used.
"""
from itertools import combinations_with_replacement, product
from pathlib import Path
import json
import runpy
import sympy as s


ROOT = (1+s.I*s.sqrt(3))/2
L, N = 6, 216
momenta = [(1,1,0),(2,5,0),(5,5,0),(4,1,0)]
ward_source = Path(__file__).resolve().parent.parent / 'free-scalar-3d/free_scalar_ward.py'
ward_module = runpy.run_path(str(ward_source))
fields = ward_module['Fields']()
ward = ward_module['WardComplex'](fields)
components = [(0,0),(1,1),(2,2),(1,2),(0,2),(0,1)]
raw_source = [ward.tau(i,j,(0,0,0)) for i,j in components]
u,v = s.symbols('u v')


def clean(expression):
    if isinstance(expression,s.MatrixBase):
        return expression.applyfunc(lambda e:s.simplify(s.expand(e)))
    return s.simplify(s.expand(expression))


def wave(k,x):
    return clean(ROOT**(sum(k[i]*x[i] for i in range(3)) % 6))


def actual_vertex(k,l):
    result = []
    for expression in raw_source:
        substitutions = {ward.a:1,ward.mass2:0}
        for symbol in expression.free_symbols:
            if symbol not in fields.reverse:
                continue
            kind,offset = fields.reverse[symbol]
            substitutions[symbol] = u*wave(k,offset)+v*wave(l,offset) if kind=='phi' else 0
        result.append(clean(s.expand(expression.subs(substitutions, simultaneous=True)).coeff(u,1).coeff(v,1)))
    return s.Matrix(result)


def nullspace_projector(q):
    zz = [wave(q,tuple(int(j==i) for j in range(3))) for i in range(3)]
    d = [z-1 for z in zz]
    dm = [1-1/z for z in zz]
    V = s.Matrix([[d[0],0,0,0,dm[2]/s.sqrt(2),dm[1]/s.sqrt(2)],
                  [0,d[1],0,dm[2]/s.sqrt(2),0,dm[0]/s.sqrt(2)],
                  [0,0,d[2],dm[1]/s.sqrt(2),dm[0]/s.sqrt(2),0]])
    constraints = clean(V.col_join(s.Matrix([[1,1,1,0,0,0]])))
    basis = s.Matrix.hstack(*constraints.nullspace())
    assert basis.shape == (6,2)
    return clean(basis*(basis.H*basis).inv()*basis.H)


def main():
    k,l = momenta[:2]
    plus = s.Matrix([0,1,-1,0,0,0])/s.sqrt(2)
    metric_root = s.diag(1,1,1,s.sqrt(2),s.sqrt(2),s.sqrt(2))
    tt_projector = nullspace_projector((3,0,0))
    assert clean(plus.T*plus)[0] == 1
    source_uv = metric_root*actual_vertex(k,l)
    assert clean(tt_projector*source_uv) == s.Matrix([0,s.Rational(3,4),-s.Rational(3,4),0,0,0])
    scalar_vertex = clean((plus.T*source_uv)[0])
    assert scalar_vertex == 3*s.sqrt(2)/4
    for p in [k,l]:
        q = tuple(2*ki % 6 for ki in p)
        assert clean(nullspace_projector(q)*metric_root*actual_vertex(p,p)) == s.zeros(6,1)

    a,b,c,d,A,B,C,D = s.symbols('a b c d A B C D')
    variables = [a,b,c,d,A,B,C,D]
    x = s.Rational(4,7)
    wa,wb = s.sqrt(x+2),s.sqrt(x+4)
    fourier_phi = [(a+C)/s.sqrt(2*wa),(b+D)/s.sqrt(2*wb),
                   (c+A)/s.sqrt(2*wa),(d+B)/s.sqrt(2*wb)]
    fourier_pi = [-s.I*s.sqrt(wa/2)*(a-C),-s.I*s.sqrt(wb/2)*(b-D),
                  -s.I*s.sqrt(wa/2)*(c-A),-s.I*s.sqrt(wb/2)*(d-B)]
    neg = [2,3,0,1]
    frequency = [wa,wb,wa,wb]
    reconstructed_Hm = clean(sum((fourier_pi[j]*fourier_pi[neg[j]]
                                  +frequency[j]**2*fourier_phi[j]*fourier_phi[neg[j]])/2 for j in range(4)))
    assert clean(reconstructed_Hm-wa*(a*A+c*C)-wb*(b*B+d*D)) == 0
    reconstructed_J = clean(sum(s.I*s.sin(s.pi*momenta[j][0]/3)
                                *fourier_pi[j]*fourier_phi[neg[j]] for j in range(4)))
    assert clean(reconstructed_J-s.sqrt(3)*(a*A+b*B-c*C-d*D)/2) == 0

    # Sum ordered Fourier pairs with the necessary 1/2: the source_uv
    # coefficient already contains the two cross terms of a quadratic.
    actual_T = 0
    for i,j in product(range(4),repeat=2):
        if tuple((momenta[i][h]+momenta[j][h])%6 for h in range(3)) != (3,0,0):
            continue
        coeff = clean((plus.T*metric_root*actual_vertex(momenta[i],momenta[j]))[0])
        actual_T += coeff*fourier_phi[i]*fourier_phi[j]/(2*s.sqrt(N))
    actual_T = clean(actual_T)
    coupling = scalar_vertex/(2*s.sqrt(N*wa*wb))
    expected_T = coupling*((a+C)*(b+D)+(c+A)*(d+B))
    assert clean(actual_T-expected_T) == 0
    assert clean(coupling**2) == s.Rational(7,18432)

    # Independently sum pure-scalar quartic contraction coefficients, not
    # the original checker's Poisson differentiation implementation.
    terms = s.Poly(actual_T,*variables).terms()
    frequencies = [wa,wb,wa,wb,-wa,-wb,-wa,-wb]
    target = (1,1,0,0,0,0,1,1)
    static,exchange = 0,0
    for exp_i,ci in terms:
        for exp_j,cj in terms:
            if tuple(e+f for e,f in zip(exp_i,exp_j)) != target:
                continue
            Omega = sum(e*w for e,w in zip(exp_j,frequencies))
            static += ci*cj/8
            exchange -= ci*cj/(2*(4-Omega**2))
    coefficient = clean(static+exchange)
    assert coefficient == s.Rational(301,2396160)

    # Stronger filtering independent of the accidental rational frequency
    # ratio: Haar average on the two-angle free torus.
    physical = momenta+[momenta[j] for j in neg]
    freq_vectors = [(1,0),(0,1),(1,0),(0,1),(-1,0),(0,-1),(-1,0),(0,-1)]
    charges = [1,1,-1,-1,-1,-1,1,1]
    found = set()
    for indices in combinations_with_replacement(range(8),4):
        if any(sum(freq_vectors[i][j] for i in indices) for j in range(2)):
            continue
        if any(sum(physical[i][j] for i in indices)%6 for j in range(3)):
            continue
        if sum(charges[i] for i in indices):
            found.add(indices)
    assert found == {(0,1,6,7),(2,3,4,5)}
    mean = clean(4*s.sqrt(3)*coefficient)
    assert mean == 301*s.sqrt(3)/599040

    # This is separate support for, not an unqualified promotion of, the
    # all-mass torus proof. Its global normal-form hypotheses remain textual.
    mass2 = s.symbols('mass2', nonnegative=True)
    freq_product = s.sqrt((mass2+2)*(mass2+4))
    A0 = -2*(mass2+1)
    B0 = 2*freq_product
    all_mass_factor = clean(s.Rational(1,2)-1/(A0-B0)-1/(A0+B0))
    assert clean(all_mass_factor-(2*mass2+5)/(2*(4*mass2+7))) == 0
    assert clean(all_mass_factor.subs(mass2,x)) == s.Rational(43,130)
    print(json.dumps({'status':'PASS',
                      'actual_original_Ward_plus_vertex':str(scalar_vertex),
                      'independent_nullspace_TT_channels_checked':3,
                      'actual_equal_pair_channels_vanish':True,
                      'full_Fourier_H0_J0_and_Nyquist_T_normalization':True,
                      'static_coefficient':str(clean(static)),
                      'exchange_coefficient':str(clean(exchange)),
                      'sum_quartic_coefficient':str(coefficient),
                      'independent_two_angle_charged_resonances':sorted(found),
                      'mean_at_mass_squared_4_over_7':str(mean),
                      'separate_all_mass_factor':str(all_mass_factor),
                      'scope':'Exact algebra; global-smooth obstruction additionally uses the explicit normal-form and compact-orbit/torus proof.'},indent=2))


if __name__ == '__main__':
    main()
