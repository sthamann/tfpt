"""Exact finite audit of the user submission, using actual pinned source rays.

NON-RH. Tetramer Hamiltonian and CQ execution are explicit extra assumptions.
Run with Python + SymPy + NumPy. Prints JSON; --write saves this owned report.
No physical selection, ground-state preparation or T1-T8 closure follows.
"""
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import sys
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
CORE=HERE.parent/'compiler-origin-audit-20260913/context_instrument.py'
CORE_PIN='ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995'
CHECKS=[]


def check(ok,name):
    if not ok:
        raise ValueError(name)
    CHECKS.append(name)


def spectrum_integer(matrix,eigenvalues):
    """Exact integer annihilator + exact trace moments, for a symmetric matrix."""
    n=len(matrix)
    eye=np.eye(n,dtype=np.int64)
    check(np.array_equal(matrix,matrix.T),'spectrum requires real symmetry')
    product=eye.copy()
    for e in eigenvalues:
        product=product@(matrix-e*eye)
    check(not np.any(product),'exact spectral annihilator')
    power=eye.copy()
    moments=[]
    for _ in eigenvalues:
        moments.append(int(np.trace(power)))
        power=power@matrix
    vand=s.Matrix([[s.Integer(e)**k for e in eigenvalues] for k in range(len(eigenvalues))])
    multiplicities=vand.inv()*s.Matrix(moments)
    check(all(x.is_Integer and x>=0 for x in multiplicities),'nonnegative integer multiplicities')
    check(sum(multiplicities)==n,'spectral dimension')
    return {str(e):int(m) for e,m in zip(eigenvalues,multiplicities)}


def source_data():
    check(hashlib.sha256(CORE.read_bytes()).hexdigest()==CORE_PIN,'adapter pin unchanged')
    spec=importlib.util.spec_from_file_location('source_core',CORE)
    core=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    d=core.source_prefix()
    by_label={}
    for k in d['line_reps']:
        z=s.Matrix([a+s.I*b for a,b in d['Z240'][k]])
        p=(z*z.H/4).applyfunc(s.expand)
        label=d['root_label'][d['ROOTS'][k]]
        by_label.setdefault(label,[]).append(p)
    labels=sorted(by_label)
    bases=[by_label[k] for k in labels]
    check(len(bases)==15 and all(len(b)==4 for b in bases),'actual fifteen by four source rays')
    paulis=[core.cmatrix(p) for v,p in sorted(d['PMAT'].items()) if any(v)]
    def pairing(x,y):
        v=d['hermC'](d['chart'](x),d['chart'](y))
        check(all(z%2==0 for z in v),'source pairing divisible by two')
        return (v[0]//2+v[1]//2)%2
    B=s.Matrix([[int(pairing(d['REPS'][x],d['REPS'][y])==0) for y in labels] for x in labels])
    rays=[p for b in bases for p in b]
    C=s.Matrix(15,60,lambda i,j:int(j//4==i))
    F=s.Matrix([[s.trace(a*p).expand() for p in rays] for a in paulis])
    gram=s.Matrix([[s.trace(p*q).expand() for q in rays] for p in rays])
    return B,C,F,gram,bases,paulis,core.CHECKS


def sixty_and_cq():
    B,C,F,G,bases,paulis,inherited=source_data()
    swap16=s.Matrix(16,16,lambda i,j:int(i//4==j%4 and i%4==j//4))
    check(sum((s.kronecker_product(p,p) for p in [s.eye(4),*paulis]),s.zeros(16))/4==swap16,
          'new swap is bilinear in actual source Pauli matrices')
    I=s.eye(60)
    check(C*C.T==4*s.eye(15),'CCt equals four identity')
    check(F*F.T==12*s.eye(15),'FFt equals twelve identity')
    check(C*F.T==s.zeros(15),'context and Pauli sectors orthogonal')
    T=s.Matrix(60,60,lambda i,j:B[i//4,j//4]*G[i,j]/7)
    check(T==(C.T*B*C+F.T*F)/28,'source transition factorization')
    Pc=C.T*C/4
    Pf=F.T*F/12
    Ph=I-Pc-Pf
    check(Pc**2==Pc and Pf**2==Pf and Ph**2==Ph,'orthogonal sector projectors')
    check(s.trace(Ph)==30 and T*Ph==s.zeros(60),'thirty hidden directions annihilated')
    # Equality and invertibility on C/F sectors prove ker(C,F)=ker(T).
    check(B*B==4*s.eye(15)+3*s.ones(15),'B invertible by source identity')
    for n in (1,2,3):
        check(T**n==C.T*(B/7)**n*C/4+s.Rational(3,7)**n*Pf,'closed all-n formula induction witnesses')
    spec=spectrum_integer(np.array(14*T,dtype=np.int64),[0,2,-4,4,6,14])
    # Including a deliberately absent candidate 2 yields multiplicity zero.
    check(spec=={'0':30,'2':0,'-4':5,'4':9,'6':15,'14':1},'full source T spectrum')
    adjacent=s.Matrix(60,60,lambda i,j:(B[i//4,j//4]-int(i//4==j//4))*G[i,j]/6)
    disjoint=s.Matrix(60,60,lambda i,j:(1-B[i//4,j//4])*G[i,j]/8)
    for branch,k,lam,mu in [(I,s.eye(15),1,1),
                            (adjacent,(B-s.eye(15))/6,s.Rational(1,3),s.Rational(-1,6)),
                            (disjoint,(s.ones(15)-B)/8,0,0)]:
        check(branch==C.T*k*C/4+lam*Pf+mu*Ph,'full symmetric family decomposition')
    a,b,c=s.symbols('a b c',real=True)
    check(s.solve([a+b-1,a-b/6],[a,b])=={a:s.Rational(1,7),b:s.Rational(6,7)},
          'local support plus hidden erasure selects source policy')
    # Independent derivation of orbit sizes under full symplectic context symmetry:
    # each row splits into self, 6 adjacent, 8 disjoint by the pinned incidence.
    check(all(sum(B[i,j] for j in range(15))==7 for i in range(15)),'policy orbit row sizes 1 6 8')

    # CQ channel in Pauli coordinates: identity block K and 15 blocks D_v K.
    incidence=s.Matrix(15,15,lambda v,j:int(any(F[v,4*j+k]!=0 for k in range(4))))
    check(all(sum(incidence[v,j] for j in range(15))==3 for v in range(15)),
          'each Pauli belongs to exactly three contexts')
    ranks=[15,15,15]
    for v in range(15):
        D=s.diag(*list(incidence[v,:]))
        M=D*B/7
        for n in range(1,4):
            ranks[n-1]+=(M**n).rank()
        check(M**3==s.Rational(3,7)*M**2,'CQ cubic block identity')
        check(M.rank()==3 and (M**2).rank()==1,'CQ two nilpotent Jordan chains per Pauli')
        initial=s.ones(15,1)/15
        for n in (1,2,3,4):
            check(sum(M**n*initial)==s.Rational(1,5)*s.Rational(3,7)**(n-1),
                  'independent first preparation then retained context formula')
    check(ranks==[60,30,30],'CQ rank 240 to 60 to 30 then stable')
    check(s.Rational(3,35)!=s.Rational(1,25),'retained versus refreshed context second step')
    # Explicit input rho=one source ray; independent and matched give same rho,
    # but output purities of different depolarizing contractions differ.
    p=bases[0][0]
    out3=s.Rational(3,7)*p+s.eye(4)/7
    out1=p/5+s.eye(4)/5
    check(out3!=out1 and s.trace(out3)==1 and s.trace(out1)==1,'same rho different CQ preparations')
    # Affine positive section obstruction: distinct uniform contextual mixtures.
    center0=C.T[:,0]/4
    center1=C.T[:,1]/4
    check(center0!=center1 and F*center0==F*center1==s.zeros(15,1),
          'distinct contextual decompositions of maximally mixed state')
    return {'source_prefix_checks':inherited,
            'T_spectrum':{'1':1,'3/7':15,'2/7':9,'-2/7':5,'0':30},
            'CQ_ranks_including_identity':[240,*ranks],
            'CQ_zero_Jordan_blocks':{'size_1':150,'size_2':30},
            'retained_context_contraction':'(1/5)*(3/7)^(n-1), n>=1',
            'refreshed_context_contraction':'(1/5)^n',
            'symmetric_policy_bands':{'quantum':'a+b/3','hidden':'a-b/6',
                                      'context_9':'a+b/6-c/4','context_5':'a-b/2+c/4'}}


def formula_followups():
    import mpmath as mp
    mp.mp.dps=60
    N=s.Symbol('N',positive=True)
    c=s.Symbol('c',positive=True)
    ns=1-2/N
    r=12/N**2
    As=N**2*c**7/(24*s.pi**2)
    check(s.simplify(r-3*(1-ns)**2)==0,'inflation eliminate N from r')
    check(s.simplify(As*(1-ns)**2-c**7/(6*s.pi**2))==0,'inflation eliminate N from amplitude')
    cnum=1/(8*mp.pi)
    Ncal=mp.sqrt(mp.mpf('2.10e-9')*24*mp.pi**2/cnum**7)
    check(50<Ncal<60,'amplitude matching N lies inside stated interval')
    # Rational margins used in the independent analytic positive-root proof.
    check(s.Rational(3,256*3**4)<s.Rational(1,6000),'dtop coarse upper bound using pi greater than three')
    check(s.Rational(1,18)+s.Rational(2,6000)<s.Rational(1,16),'seam phi below one sixteenth')
    check((1-s.Rational(1,6000))**(-3)<2,'bound on response derivative denominator')
    check(s.Rational(80,6000)<s.Rational(1,50),'alpha times gprime bounded below 0.02')
    return {'As_calibration_input':'2.10e-9, illustrative Planck2018 value',
            'N_calibrated':mp.nstr(Ncal,20),'ns_conditional':mp.nstr(1-2/Ncal,20),
            'r_conditional':mp.nstr(12/Ncal**2,20),
            'As_independent_prediction_after_calibration':False,
            'positive_alpha_root_unique':'analytic proof for fixed equation; physical identification unproved'}


def tetramer():
    digits=list(it.product(range(4),repeat=4))
    lookup={x:i for i,x in enumerate(digits)}
    eye=np.eye(256,dtype=np.int64)
    swaps=[]
    for i,j in it.combinations(range(4),2):
        swap=np.zeros((256,256),dtype=np.int64)
        for col,d in enumerate(digits):
            target=list(d); target[i],target[j]=target[j],target[i]
            swap[lookup[tuple(target)],col]=1
        check(np.array_equal(swap@swap,eye),'carrier swap involution')
        swaps.append(swap)
    H2=6*eye+sum(swaps)  # 2 H/J: exact integers
    spectrum=spectrum_integer(H2,[0,4,6,8,12])
    check(spectrum=={'0':1,'4':45,'6':40,'8':135,'12':35},'tetramer exact full spectrum')
    omega=np.zeros(256,dtype=np.int64)
    for perm in it.permutations(range(4)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        omega[lookup[perm]]=sign
    check(int(omega@omega)==24,'antisymmetric vector normalization')
    check(not np.any(H2@omega),'unique zero energy vector')
    for swap in swaps:
        check(np.array_equal(swap@omega,-omega),'antisymmetric under every pair')
    tensor=omega.reshape((4,)*4)
    for keep_size in (1,2):
        for kept in it.combinations(range(4),keep_size):
            axes=list(kept)+[k for k in range(4) if k not in kept]
            A=np.transpose(tensor,axes).reshape(4**keep_size,-1)
            reduced24=A@A.T
            if keep_size==1:
                check(np.array_equal(reduced24,6*np.eye(4,dtype=np.int64)),'one-site reduced state I4/4')
            else:
                swap=np.zeros((16,16),dtype=np.int64)
                for i,j in it.product(range(4),repeat=2): swap[4*j+i,4*i+j]=1
                check(np.array_equal(reduced24,2*(np.eye(16,dtype=np.int64)-swap)),
                      'pair reduced state (I-S)/12')
    weights=np.array([n.bit_count() for n in range(256)])
    check(all(weights[i]==4 for i in np.flatnonzero(omega)),'explicit eight-mode weight-four support')
    check(not np.any((weights[:,None]-weights[None,:])*H2),'H preserves total fermion number in fixed encoding')
    indices=np.flatnonzero(weights==4)
    check(len(indices)==70,'four-particle sector dimension')
    restricted=spectrum_integer(H2[np.ix_(indices,indices)],[0,4,6,8,12])
    # Jordan-Wigner annihilation with bit0 the least significant mode.
    annihilators=[]
    for mode in range(8):
        matrix=np.zeros((256,256),dtype=np.int64)
        for state in range(256):
            if state & (1<<mode):
                sign=(-1)**((state & ((1<<mode)-1)).bit_count())
                matrix[state^(1<<mode),state]=sign
        annihilators.append(matrix)
    for i,j in it.product(range(8),repeat=2):
        ai,aj=annihilators[i],annihilators[j]
        check(np.array_equal(ai@aj.T+aj.T@ai,eye if i==j else np.zeros_like(eye)),'canonical CAR')
        check(not np.any(ai@aj+aj@ai),'annihilator CAR')
    one_rdm24=np.array([[(ai@omega)@(aj@omega) for aj in annihilators] for ai in annihilators])
    check(np.array_equal(one_rdm24,12*np.eye(8,dtype=np.int64)),'one-body fermion density equals half identity')
    check(np.count_nonzero(omega)==24 and 24&(24-1)!=0,'non-stabilizer support is not power of two')
    # Unique ground state is not an attractor of its unitary evolution.
    fixed_dimension=sum(n*n for n in spectrum.values())
    check(fixed_dimension==23076,'unitary fixed-operator algebra is highly nonunique')
    # The actual Clifford carrier reflection -1 on |00> acts collectively as det R.
    R=s.diag(-1,1,1,1)
    collective=np.array(s.kronecker_product(R,R,R,R),dtype=np.int64)
    check(np.array_equal(collective@omega,-omega),'collective source reflection changes only global phase')
    # Two cells, one positive cross-edge. Local product state I16/16 on edge:
    # <P_sym>=5/8; variance=15/64. No 65536-square diagonalization is needed.
    mean=s.Rational(5,8)
    check(mean-mean**2==s.Rational(15,64),'cross-cell edge variance nonzero')
    return {'H_over_J_spectrum':{'0':1,'2':45,'3':40,'4':135,'6':35},
            'H70_over_J_spectrum':{str(s.Rational(k)/2):v for k,v in restricted.items()},
            'gap':'2J','unitary_fixed_operator_dimension':fixed_dimension,
            'non_Slater':True,'non_stabilizer':True,'physical_ground_state_preparation_derived':False,
            'source_operator_intertwiner_proved':False,
            'two_cells_positive_cross_edge':{
                'product_energy':'5 lambda / 8','product_energy_variance':'15 lambda^2 / 64',
                'gap_lower_bound':'2J - 5 lambda/8',
                'guaranteed_unique_ground_state_range':'0 <= lambda < 16J/5'}}


def main():
    result={'scope':'NON-RH finite source process and explicitly added SU4 tetramer',
            'sixty':sixty_and_cq(),'tetramer':tetramer(),
            'formula_followups':formula_followups(),'T1_T8_closed':[]}
    result['checks']=len(CHECKS)
    result['check_names']=CHECKS
    result['source_sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in [CORE,HERE/'USER_SUBMISSION.md',Path(__file__)]}
    output=json.dumps(result,indent=2,sort_keys=True)
    if '--write' in sys.argv:
        (HERE/'verification.json').write_text(output+'\n')
    print(output)


if __name__=='__main__':
    main()
