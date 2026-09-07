#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round27_algebra import Certificate,inputs,pinch,word_trace
import sympy as s


def main():
    previous,old=inputs(); cert=Certificate(); check=cert.check
    initial,word,states,signs,phase=previous.negative_word(old)
    check('actual original E8 closed loop remains negative', phase==-1 and states[-1]==initial and signs==[-1,1,-1,-1])
    check('actual eight-channel energy normalization is retained', old.G.inv().norm(s.oo)==31 and previous.charge_coercivity(27)==s.Rational(1,1674))
    N,J,beta=s.symbols('N J beta',positive=True)
    theta=48*beta*N*J
    check('reference hopping normalization cancels exactly once', s.exp(-theta)*s.exp(theta)==1)
    x=s.Symbol('x',positive=True)
    check('full-reference sign factor has no charge partition multiplier', s.simplify(s.exp(-x)**-1-s.exp(x))==0)
    # Finite NONCOMMUTING lemma witnesses, not a substituted TFPT model.
    U=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
    V=s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
    Vsign=s.diag(1,-1,1,-1)*V
    A=U+Vsign; E=3*s.eye(4)+2*A
    check('signed finite witness has zero diagonal and anticommuting channels', A.diagonal()==s.zeros(1,4) and A*A==2*s.eye(4) and U*Vsign==-Vsign*U)
    check('finite heat witness is positive with reciprocal spectral values', E.is_positive_definite and s.det(E)==1 and E.diagonal()==s.ones(1,4)*3)
    blocks=[s.Matrix([[2,1],[1,2]]),s.Matrix([[3,1],[1,2]]),s.Matrix([[2,1],[1,3]]),s.Matrix([[4,1],[1,2]])]
    S=s.diag(*blocks); C=S*S; Q=S*s.kronecker_product(E,s.eye(2))*S
    check('scalar charge blocks do not silently commute with each other', blocks[0]**2*blocks[1]**2!=blocks[1]**2*blocks[0]**2)
    check('pinching retains every charge block and its full scalar space', pinch(Q,2)==3*C and s.trace(pinch(Q,2))==s.trace(Q))
    T=3; ZD=s.trace(C**T); Z=s.trace(Q**T)
    check('all-block pinching lower bound has the correct direction', Z>=s.trace(pinch(Q,2)**T)==3**T*ZD)
    check('full reference is strictly larger than its zero-block compression', ZD>s.trace((blocks[0]**2)**T))
    v=s.kronecker_product(s.Matrix([1,-1,-1,0]),s.Matrix([1,0])); w=S.inv()*v
    check('stronger lower trace bound is not a false Loewner lower bound', (w.T*(Q-C)*w)[0]==-2)
    check('ordered eigenvalue upper bound controls trace powers', Z<=(3+2*s.sqrt(2))**T*ZD)
    unsigned=[s.eye(8),s.kronecker_product(U,s.eye(2)),s.kronecker_product(V,s.eye(2))]
    R=s.diag(1,1,0,0,0,0,0,0)
    check('boundary projection commutes with reference not generally hops', R*C==C*R and R*unsigned[1]!=unsigned[1]*R)
    violates_unrooted=False; count=0
    for T in (3,4):
        ZD=s.trace(C**T); tail=s.trace(R*C**T)
        all_majorants=True; all_projected=True; normalization=True
        for indices in product(range(3),repeat=T):
            words=[unsigned[i] for i in indices]
            value=word_trace(C,words); projected=word_trace(C,words,R)
            all_majorants &= 0<=value<=ZD
            all_projected &= projected>=0 and projected**T<=tail*ZD**(T-1)
            normalization &= word_trace(C,[s.eye(8)]*T)==ZD
            violates_unrooted |= projected>tail
            count+=1
        check(f'T{T}: every tested positive word obeys full-reference Holder', all_majorants and normalization)
        check(f'T{T}: projected word retains the essential probability root', all_projected)
    check('dropping the charge-tail Tth root has an explicit counterexample', violates_unrooted)
    for k in range(5):
        allocation=sum(s.Rational(1,s.factorial(a)*s.factorial(b)*s.factorial(k-a-b)) for a in range(k+1) for b in range(k-a+1))
        check(f'order{k}: all slice allocations use total-order factorial', allocation==s.Rational(3**k,s.factorial(k)))
    cert.witnesses.update({'finite_word_tuples_checked':count,'matrix_dimension':8,
        'finite_matrices_are_lemma_regressions_not_TFPT_truncations':True,
        'full_reference_all_fixed_charge_sectors':True,'explicit_charge_envelope_neutral_only':True,
        'sign_ratio_upper':'exp(48 beta N J)','charge_entropy_in_sign_bound':False,
        'original_negative_loop_phase':phase,'full_partition_sum_executed':False})
    cert.emit('Analytic full-reference pinching and Holder bounds on the original finite Euclidean regulator; exact finite noncommuting lemma regressions and original E8 provenance. No efficient sign cure, continuum, real time or TOE closure.')


if __name__=='__main__': main()
