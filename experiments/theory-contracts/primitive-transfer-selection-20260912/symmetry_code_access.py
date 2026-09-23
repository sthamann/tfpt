"""Exact conditional Clock/anchor sector audit, not a derived Gauss law."""
import json
import sympy as S
import boundary_access as source


def main():
    _, b, o16, p16 = source.source_matrices()
    clean = lambda m: m.applyfunc(S.simplify)
    p, o = p16[::2, ::2], o16[::2, ::2]
    eta = (-1-S.I*S.sqrt(3))/2
    v0 = S.Matrix([0,0,0,1,-1,0,0,0])/S.sqrt(2)
    vp = S.Matrix([1,eta,S.expand(eta**2),0,0,0,0,0])/S.sqrt(3)
    v = S.Matrix.hstack(v0, vp, S.conjugate(vp))
    alpha, g = S.symbols('alpha g', real=True)
    h = alpha*S.eye(8)+g*(b[::2,1::2]+S.I*b[::2,::2])
    source.require(clean(v.adjoint()*v)==S.eye(3), 'orthonormal hidden modes')
    source.require(clean(v*v.adjoint())==S.eye(8)-p, 'complete hidden one-particle space')
    source.require(clean(o*v-v*S.diag(-1,eta,S.conjugate(eta)))==S.zeros(8,3), 'source Clock eigenvalues')
    source.require(o*p==p, 'Clock identity on accessible space')
    source.require(clean(h*v-v*S.diag(alpha-g,alpha+S.sqrt(3)*g,alpha-S.sqrt(3)*g))==S.zeros(8,3), 'source hidden energies')
    source.require(h*p==p*h and h*o==o*h, 'number-conserving split and Clock preservation')
    grade = lambda n: sum((3,4,2)[j] for j in range(3) if n>>j&1)%6
    hidden_fixed = [n for n in range(8) if grade(n)==0]
    source.require(hidden_fixed==[0,6], 'vacuum and opposite-Clock pair are both fixed')
    source.require(32*len(hidden_fixed)==64, 'Clock-fixed full Fock dimension 64')
    sectors = {}
    for residue in range(4):
        pairs = [(a,z) for a in range(32) for z in hidden_fixed
                 if (a.bit_count()+z.bit_count())%4==residue]
        groups = [[a for a,z in pairs if z==hidden] for hidden in hidden_fixed]
        source.require(len(pairs)==16, 'each anchor character has sixteen dimensions')
        source.require(set(groups[0]).isdisjoint(groups[1]), 'hidden flag encoded in accessible number residue')
        image = {(a,c) for a,z in pairs for c,w in pairs if z==w}
        expected = sum(len(group)**2 for group in groups)
        source.require(len(image)==expected==136, 'exact partial-trace rank on all matrix units')
        source.require(len(pairs)**2-len(image)==120, 'lost off-block operator dimensions')
        sectors[str(residue)] = {'block_dimensions':list(map(len,groups)),
                                'operator_image_rank':len(image), 'operator_kernel_dimension':120}
    # Use states with identical TOTAL particle number, not merely mod four.
    # Accessible 15 has four particles; accessible 3 has two, hidden 6 has two.
    left, right = (15,0), (3,6)
    source.require(left[0].bit_count()+left[1].bit_count()==right[0].bit_count()+right[1].bit_count()==4,
                   'phase witness has exact total charge four on both branches')
    source.require(grade(left[1])==grade(right[1])==0, 'phase witness Clock-fixed')
    basis = [(a,z) for a in range(32) for z in hidden_fixed
             if (a.bit_count()+z.bit_count())%4==0]
    il, ir = basis.index(left), basis.index(right)
    states=[]
    for sign in (1,-1):
        psi=S.zeros(16,1)
        psi[il],psi[ir]=1/S.sqrt(2),sign/S.sqrt(2)
        states.append(psi)
    source.require((states[0].adjoint()*states[1])[0]==0, 'orthogonal same-charge encoded phases')
    def erase(rho):
        out=S.zeros(32)
        for i,(a,z) in enumerate(basis):
            for j,(c,w) in enumerate(basis):
                if z==w:
                    out[a,c]+=rho[i,j]
        return out
    source.require(erase(states[0]*states[0].adjoint())==erase(states[1]*states[1].adjoint()),
                   'same-charge phase states have identical accessible marginal')
    observable=S.zeros(16)
    observable[il,ir]=observable[ir,il]=1
    total_n=S.diag(*[a.bit_count()+z.bit_count() for a,z in basis])
    source.require(total_n*observable==observable*total_n, 'joint phase witness is number neutral')
    source.require([(psi.adjoint()*observable*psi)[0] for psi in states]==[1,-1],
                   'symmetry-allowed joint observable distinguishes missing phase')
    print(json.dumps({'checks':source.count, 'source_sha256':source.PIN,
        'clock_fixed_hidden_occupations':hidden_fixed, 'clock_fixed_fock_dimension':64,
        'anchor_character_sectors':sectors, 'phase_witness_total_particle_number':4,
        'sector_constraints_source_derived':False, 'full_quantum_recovery':False,
        'conditional_boundary_algebra':'M6(C) direct_sum M10(C)',
        'physical_boundary_operations_derived':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
