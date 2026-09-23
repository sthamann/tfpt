"""NON-RH: all-length energy-density obstruction to the fixed trimer encoding."""
import json
import sympy as s
import bond_algebra as src

CHECKS = 0


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def clean(m):
    return m.applyfunc(s.simplify)


def main():
    gs = src.source_generators()
    aa = [s.I*g for g in gs]
    eye, ident = s.eye(4), s.eye(64)
    phi = eye.reshape(16,1)/2
    edge = 2*s.eye(16)-sum((s.kronecker_product(a,s.conjugate(a)) for a in aa),s.zeros(16))/2
    h3 = s.kronecker_product(edge,eye)+s.kronecker_product(eye,s.conjugate(edge))
    e0 = 4-s.sqrt(6)
    spec = h3.eigenvals()
    require(spec == {e0:4,2:4,4-s.sqrt(2):12,4:24,4+s.sqrt(2):12,6:4,4+s.sqrt(6):4}, 'exact full trimer spectrum')
    require(all(bool(e >= e0) for e in spec), 'trimer operator lower bound')
    b = s.kronecker_product(phi,eye)+s.kronecker_product(eye,phi)
    c = (4*ident-h3)*b
    g = clean((s.sqrt(3)-s.sqrt(2))*(b+c/s.sqrt(6)))
    require(clean(g.H*g) == eye, 'original trimer isometry')
    require(clean(h3*g-e0*g) == s.zeros(64,4), 'original exact trimer ground embedding')
    attenuation = s.sqrt(6)/4
    for a in aa:
        require(clean(g.H*s.kronecker_product(a,s.eye(16))*g) == attenuation*a, 'left boundary primitive transport')
        require(clean(g.H*s.kronecker_product(s.eye(16),a)*g) == attenuation*a, 'right boundary primitive transport')
    scale, offset = attenuation**2, 2*(1-attenuation**2)
    require(scale == s.Rational(3,8) and offset == s.Rational(5,4), 'exact inter-trimer compression constants')
    require(edge*phi == s.zeros(16,1), 'Bell dimer has zero occupied-bond energy')
    require(s.trace(edge)/16 == 2, 'unoccupied bond mean in dimer covering')
    require(s.trace(eye/4)==1 and (phi.H*phi)[0]==1, 'normalized one-site dimer marginal')
    rho = phi*phi.H
    reduced = s.Matrix(4,4,lambda i,j:sum(rho[4*i+k,4*j+k] for k in range(4)))
    require(reduced == eye/4, 'maximally mixed dimer endpoint')
    pair_of_dimers = s.kronecker_product(phi,phi)
    cross = s.kronecker_product(eye,s.conjugate(edge),eye)
    require((pair_of_dimers.H*cross*pair_of_dimers)[0] == 2, 'cross-dimer primitive bond expectation exactly two')
    bound = s.simplify((e0+offset+scale*e0/2)/3)
    require(bound == (96-19*s.sqrt(6))/48, 'encoded energy density lower bound')
    delta = s.simplify(bound-1)
    require(delta == (48-19*s.sqrt(6))/48, 'strict extensive variational separation')
    require(48**2 > 19**2*6, 'exact positivity witness without rounding')
    # Counting check of the analytic sum-of-triples proof, not a finite-size extrapolation.
    for blocks in (4,6,8,10,12):
        counts = [0]*blocks
        for j in range(blocks):
            counts[j] += 1
            counts[(j+1)%blocks] += 1
        require(counts == [2]*blocks, 'each periodic logical edge belongs to two trimer inequalities')
    print(json.dumps({'scope':'NON-RH exact local identities plus analytic all-length variational obstruction',
        'checks':CHECKS+src.CHECKS,'source_pin':src.PIN,
        'lengths':'periodic L=3M with even M>=4, hence L=12,18,24,...',
        'encoded_energy_per_site_lower_bound':str(bound),
        'true_ground_energy_per_site_upper_bound':'1 from a Bell-dimer trial state',
        'encoded_minus_true_energy_per_site_lower_bound':str(delta),
        'logical_entanglement_arbitrary':True,'fixed_trimer_ground_encoding_excluded_at_uniform_coupling':True,
        'deformed_or_nonlocal_encodings_excluded':False,'uniform_chain_ground_solved':False,
        'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
