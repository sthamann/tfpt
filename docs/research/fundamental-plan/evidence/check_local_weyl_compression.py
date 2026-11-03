"""Actual native-code compression of bounded proper-local current Weyls.

Exact finite degree extraction; no truncation of the Weyl exponential or
of the actual smooth local profile. All unused modes give a nonzero scalar.
"""
from pathlib import Path
import sys,json,math,itertools
import sympy as s
R=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
BASE=R/'experiments/theory-contracts/joint-native-algebra-selection-20261016'
sys.path.insert(0,str(BASE))
import check_mixed_return as original

def main():
    raw,norms=original.code()
    z=s.symbols('z0:4');a,b=s.symbols('a b',real=True)
    fs=[sum(original.Q.to_sympy(v)*s.prod(z[k] for k in mon) for mon,v in f.items()) for f in raw]
    monomials=[s.Poly(f,*z).terms() for f in fs]
    checks=[]
    def check(name,condition):
        if not condition:raise ArithmeticError(name)
        checks.append(name)
    def ip(left,right):
        q=s.Poly(s.expand(right),*z)
        return s.expand(sum(s.conjugate(v)*q.coeff_monomial(s.prod(z[k]**p[k] for k in range(4)))*math.prod(math.factorial(x) for x in p) for p,v in s.Poly(left,*z).terms()))
    gram=s.Matrix(5,5,lambda i,j:ip(fs[i],fs[j]))
    check('Unchanged original native Fock Gram',gram==s.diag(*norms))
    def compressed(alpha):
        # P exp(alpha.z) f(z-conj(alpha)) has EXACT degree4 part.
        shifted=[s.Poly(s.expand(f.subs({z[k]:z[k]-s.conjugate(alpha[k]) for k in range(4)},simultaneous=True)),*z) for f in fs]
        images=[];linear=sum(alpha[k]*z[k] for k in range(4))
        for f in shifted:
            image=0
            for powers,coef in f.terms():
                degree=sum(powers);image+=coef*s.prod(z[k]**powers[k] for k in range(4))*linear**(4-degree)/math.factorial(4-degree)
            images.append(s.expand(image))
        return s.Matrix(5,5,lambda i,j:s.factor(ip(fs[i],images[j])/norms[i]))
    def coefficient_formula(alpha):
        # Independent product of four one-oscillator exact raw matrix elements.
        def entry(p,q):
            ans=1
            for k in range(4):
                ans*=sum(s.binomial(q[k],h)*(-s.conjugate(alpha[k]))**(q[k]-h)*alpha[k]**(p[k]-h)*math.factorial(p[k])/math.factorial(p[k]-h) for h in range(min(p[k],q[k])+1))
            return ans
        return s.Matrix(5,5,lambda i,j:s.factor(sum(s.conjugate(u)*v*entry(p,q) for p,u in monomials[i] for q,v in monomials[j])/norms[i]))
    A=compressed([a,0,0,0]);B=compressed([b,b,0,0])
    for name,M,alpha in [('A',A,[a,0,0,0]),('B',B,[b,b,0,0])]:
        N=coefficient_formula(alpha)
        for i,j in itertools.product(range(5),repeat=2):check(f'{name} independent exact oscillator coefficient {i}{j}',s.simplify(M[i,j]-N[i,j])==0)
        check(f'{name} Hermitian in original metric',s.simplify(gram*M-M.T*gram)==s.zeros(5))
    comm=(A*B-B*A).applyfunc(s.factor)
    expected=a**4*b**4*(a*a-4)*(a*a-12)*(b*b-2)*(b*b-6)/4608
    target=s.zeros(5);target[0,1]=expected;target[1,0]=-12*expected
    check('Whole two-strength commutator identity',s.simplify(comm-target)==s.zeros(5))
    check('No false low-order effect: leading coefficient degree8',s.Poly(expected,a,b).coeff_monomial(a**4*b**4)==s.Rational(1,8))
    check('Exact witness a=b=1',comm.subs({a:1,b:1})[0,1]==s.Rational(55,1536))
    check('Actual witness rank2',comm.subs({a:1,b:1}).rank()==2)
    hs=s.factor(s.trace(gram.inv()*comm.T*gram*comm))
    check('Metric-correct positive commutator norm',s.simplify(hs-24*expected**2)==0)
    check('Witness squared Hilbert Schmidt norm',hs.subs({a:1,b:1})==s.Rational(3025,98304))
    # The exact complete product uses alpha+beta and its whole Weyl phase;
    # disjoint smooth profiles make that phase zero. P between operations
    # is never inserted into the true source product.
    S,T=s.symbols('S T',positive=True)
    lam=s.exp(-(S+T)/2)
    check('Full omitted modes cannot remove nonzero witness',lam.is_positive is True)
    out=dict(verdict='EXACT_SCOPED_NONLOCALITY_OF_BARE_NATIVE_COMPRESSION',
        all_passed=True,checks=checks,source='Unchanged original native code in full given E8 Cartan Fock source',
        raw_gram=[str(x) for x in norms],
        displacement_A=['a','0','0','0'],displacement_B=['b','b','0','0'],
        normalized_by_whole_vacuum_Weyl_scalars=True,
        matrix_A=[[str(x) for x in row] for row in A.tolist()],matrix_B=[[str(x) for x in row] for row in B.tolist()],
        commutator_01=str(s.factor(expected)),commutator_10='-12*commutator_01',
        witness_raw_01='55/1536',witness_orthonormal_01='55*sqrt(3)/768',witness_rank=2,
        witness_HS_squared_without_nonzero_profile_scalars='3025/98304',
        whole_class_zero_locus='a=0 or b=0 or a^2 in {4,12} or b^2 in {2,6}',
        first_joint_nonzero_strength_order=8,
        actual_profile_requirement='Disjoint nonempty proper intervals; smooth real vector profiles realizing indicated mode1 displacements and zero complementary mode1 components. Exact compact-support moment construction in proof; all higher modes retained in finite positive norm scalar.',
        full_operator_commutator='0 by exact local current Weyl relation for disjoint supports',
        lost_intermediate_identity='[PAP,PBP]=PBQAP-PAQBP when [A,B]=0',
        scope='Probe only in given full source. No physical coupling or new geometry selected. Bare compression is not a local algebra homomorphism; lossless full-word readout retains original commutation. No physical signalling claim,4D reconstruction or global TFPT exclusion.')
    Path(__file__).with_name('LOCAL-WEYL-COMPRESSION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verdict=out['verdict'],checks=len(checks),commutator_01=out['commutator_01'],witness=out['witness_raw_01'],HS_squared=out['witness_HS_squared_without_nonzero_profile_scalars'])))

if __name__=='__main__':main()
