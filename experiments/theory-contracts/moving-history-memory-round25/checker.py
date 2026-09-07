#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round25_algebra import Certificate,inputs,kernel_error,memory_mask,memory_tail,mixed_logdet_response,physical_blocks,temporal_green
import sympy as s


def cycle_laplacian(count):
    L=2*s.eye(count)
    for j in range(count):
        L[j,(j+1)%count]-=1
        L[(j+1)%count,j]-=1
    return L


def main():
    old,local=inputs(); cert=Certificate(); check=cert.check
    q=s.Rational(1,4); delta=s.Rational(3,4); b=s.Integer(4)
    check('massive temporal root has the physical delta squared normalization', q+1/q==2+delta**2*b)
    for T in (3,5,9):
        A=cycle_laplacian(T)/delta+delta*b*s.eye(T)
        G=s.Matrix(T,T,lambda j,k:temporal_green(q,delta,T,(j-k)%T))
        check(f'T{T}: periodic images give the exact Green inverse', A*G==s.eye(T))
        check(f'T{T}: constant mode keeps the zero-frequency normalization', G*s.ones(T,1)==s.ones(T,1)/(delta*b))
        line=delta/(1/q-q)
        check(f'T{T}: the infinite-line diagonal alone is insufficient', G[0,0]>line)
        for R in range(T//2):
            masked=memory_mask(G,1,T,R)
            actual=sum(abs(x) for x in (G-masked)[0,:])
            bound=memory_tail(q,delta,T,R)
            check(f'T{T} R{R}: tail dominates exact two-sided cyclic row sum', 0<actual<=bound)
        check(f'T{T}: retaining full circle has exactly zero tail', memory_tail(q,delta,T,T//2)==0)
    G=s.Matrix(5,5,lambda j,k:temporal_green(q,delta,5,(j-k)%5))
    masked=memory_mask(G,1,5,1)
    check('memory masking retains the cyclic wraparound neighbors', masked[0,4]==G[0,4] and masked[0,2]==0)
    blocks,C,initial,moved,phase=physical_blocks(old,local,3)
    check('physical regression is a nonstatic neutral integer-charge history', moved!=initial and tuple(sum(x[k] for x in moved) for k in range(8))==old.ZERO)
    check('physical spatial blocks at different times need not commute', blocks[0]*blocks[1]!=blocks[1]*blocks[0])
    M=s.kronecker_product(cycle_laplacian(3)/delta,s.eye(8))+delta*s.diag(*blocks)
    inverse=M.inv()
    for j,k in ((0,0),(0,1),(1,2)):
        block=inverse[j*8:(j+1)*8,k*8:(k+1)*8]
        bound=temporal_green(q,delta,3,(j-k)%3)
        check(f'physical block{j}{k}: dimension-free Green bound holds in operator norm', (bound**2*s.eye(8)-block.T*block).is_positive_definite)
    check('actual eliminated moving history has nonzero cross-time response', inverse[0,8]>0)
    v1,v2,dt=s.symbols('v1 v2 delta',positive=True)
    response_matrix=s.Matrix([[3+dt*v1,-1],[-1,4+dt*v2]])
    response=mixed_logdet_response(response_matrix.inv(),0,1,dt)
    check('mixed log determinant keeps its sign and squared inverse response', s.simplify(s.diff(s.log(response_matrix.det()),v1,v2)-response)==0 and response.subs({v1:1,v2:1,dt:1})<0)
    response=mixed_logdet_response(inverse,0,20,delta)
    check('separated physical determinant response has the squared memory bound', 0<abs(response)<=delta**2*temporal_green(q,delta,3,2)**2)
    small=s.Matrix(cycle_laplacian(3)/delta+delta*b*s.eye(3))
    one=small.copy(); one[0,0]+=2*delta
    two=small.copy(); two[2,2]+=6*delta
    both=one.copy(); both[2,2]+=6*delta
    check('finite positive updates have a nonpositive mixed log determinant', 0<both.det()*small.det()/(one.det()*two.det())<1)
    # Arbitrarily high charge magnitudes are not enumerated; this tests a large diagonal jump.
    big=cycle_laplacian(3)/delta+delta*s.diag(b,b+2*10**12,b)
    big_inverse=big.inv()
    check('large positive jump does not change the declared uniform bound', all(abs(big_inverse[j,k])<=temporal_green(q,delta,3,(j-k)%3) for j in range(3) for k in range(3)))
    d,c,tail=s.symbols('delta c tail',positive=True)
    check('Schur error retains both delta coupling factors', s.expand(kernel_error(d,c,tail)-d**2*c**2*tail)==0)
    e=kernel_error(delta,6,memory_tail(q,delta,9,3))/delta
    check('declared moving-history memory window preserves a positive kernel', 0<e<s.Rational(1,10))
    check('cell coupling bound is volume-free rather than summed over cells', C.norm(1)<=6 and C.norm(s.oo)<=6)
    x,bb=s.symbols('delta b',positive=True)
    qq=1+x**2*bb/2-x*s.sqrt(bb)*s.sqrt(4+x**2*bb)/2
    sh=(1/qq-qq)/2
    prefactor=s.limit(x**2/(sh*(1-qq)),x,0,dir='+')
    check('physical-time limit counts the two directions exactly once', s.simplify(prefactor-1/bb)==0)
    check('memory exponent has a finite physical mass scale', s.simplify(s.limit(-s.log(qq)/x,x,0,dir='+')-s.sqrt(bb))==0)
    eta=s.Rational(1,5); K=s.Matrix([[3,-1],[-1,3]])
    KR=K+s.Matrix([[s.Rational(1,10),0],[0,-s.Rational(1,10)]])
    check('relative Gaussian determinant is extensive not silently set to one', KR.det()!=K.det() and (1-eta)**2<=KR.det()/K.det()<=(1+eta)**2)
    for T,R in ((2,0),(3,-1)):
        try: memory_tail(q,delta,T,R)
        except ValueError: rejected=True
        else: rejected=False
        check(f'invalid temporal truncation T{T} R{R} is rejected', rejected)
    cert.witnesses.update({'q_at_delta_3_over_4_b4':str(q),'normalized_kernel_error_T9_R3_c6':str(e),
        'physical_time_prefactor':str(prefactor),'charge_jump_energy_test':2*10**12,
        'small_hopping_required_for_this_conditional_bound':False,'real_time_theorem':False})
    cert.emit('Uniform finite-memory bound for original g=0 Gaussian charge histories at the finite Euclidean regulator. Arbitrary jumps allowed, determinant retained separately; not a real-time, reflection-positivity or charge-sum continuum theorem.')


if __name__=='__main__': main()
