"""Complete Clock centralizer on the actual three-mode hidden Fock factor."""
import json
import sympy as S
import boundary_access as source


def main():
    _,B,O,_=source.source_matrices()
    alpha,g=S.symbols('alpha g',real=True)
    eta=(-1-S.I*S.sqrt(3))/2
    f0=S.Matrix([0,0,0,1,-1,0,0,0])/S.sqrt(2)
    fp=S.Matrix([1,eta,S.expand(eta**2),0,0,0,0,0])/S.sqrt(3)
    V=S.Matrix.hstack(f0,fp,S.conjugate(fp))
    clean=lambda m:m.applyfunc(S.simplify)
    h=alpha*S.eye(8)+g*(B[::2,1::2]+S.I*B[::2,::2])
    energies=[alpha-g,alpha+S.sqrt(3)*g,alpha-S.sqrt(3)*g]
    source.require(clean(V.adjoint()*V)==S.eye(3),'orthonormal source modes')
    source.require(clean(h*V-V*S.diag(*energies))==S.zeros(8,3),'actual hidden Hamiltonian')
    source.require(clean(O[::2,::2]*V-V*S.diag(-1,eta,S.conjugate(eta)))==S.zeros(8,3),
                   'actual source Clock modes')
    grades=[sum((3,4,2)[j] for j in range(3) if n>>j&1)%6 for n in range(8)]
    e=[S.expand(sum(energies[j] for j in range(3) if n>>j&1)) for n in range(8)]
    allowed=[(r,c) for r in range(8) for c in range(8) if grades[r]==grades[c]]
    source.require(len(allowed)==12,'full invariant algebra complex dimension')
    source.require(all((r&1)==(c&1) for r,c in allowed),'all invariant operators preserve n0')
    source.require(all((r.bit_count()-c.bit_count())%2==0 for r,c in allowed),
                   'hidden invariant algebra is parity even')
    source.require(all(S.diff(e[r]-e[c],g)==0 for r,c in allowed),'all hidden invariant frequencies independent of g')
    source.require(set(S.expand(e[r]-e[c]) for r,c in allowed)=={0,2*alpha,-2*alpha},'entire frequency set')
    source.require(all(r==c for r,c in allowed if r.bit_count()==c.bit_count()),
                   'number-neutral invariant hidden algebra is diagonal')
    cs=[]
    for j in range(3):
        cs.append(S.Matrix(8,8,lambda r,c: (-1)**((int(c)&((1<<j)-1)).bit_count())
                  if c&(1<<j) and r==c^(1<<j) else 0))
    T=cs[1].T*cs[2].T
    H=S.diag(*e)
    source.require(H*T-T*H==2*alpha*T,'invariant pair creation frequency')
    source.require(T[:,0].norm()==1,'pair vacuum response nonzero')
    source.require(all(T[r,c]==0 or (r,c) in allowed for r in range(8) for c in range(8)),
                   'pair is Clock invariant')
    print(json.dumps({'checks':source.count,'occupation_clock_grades':grades,
        'invariant_matrix_units':allowed,'hidden_invariant_algebra':'M2 + M2 + C^4',
        'all_hidden_invariant_frequencies':['0','2 alpha','-2 alpha'],
        'number_neutral_hidden_invariant_algebra':'C^8',
        'boundary_access_extended':False,'pair_measurement_TFPT_derived':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
