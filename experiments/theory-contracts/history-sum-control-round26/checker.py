#!/usr/bin/env python3
from fractions import Fraction
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round26_algebra import Certificate,charge_coercivity,cycle_laplacian,error_plan,inputs,relative_charge_tail,relative_hop_tail,relative_observable_error,theta_upper,trace_log_bound
import sympy as s


def main():
    old,local,memory=inputs(); cert=Certificate(); check=cert.check
    check('actual inverse Gram norm gives the declared coercivity', old.G.inv().norm(s.oo)==31 and (old.G-s.eye(8)/31).is_positive_definite)
    check('charge energy includes both its one-half and one-over-N factors', charge_coercivity(27)==Fraction(1,1674))
    check('integer Gaussian envelope retains all eight coordinates per site', theta_upper(Fraction(1),27)==83**216)
    N,J,beta=s.symbols('N J beta',positive=True)
    r=48*N; kappa=r*J
    check('unsigned row normalization retains the physical hopping constant', s.simplify(s.exp(-beta*kappa)*s.exp(beta*J*r))==1)
    # Exact finite trace Holder test, not a replacement for the full-carrier proof.
    heat=s.diag(s.Rational(1,2),s.Rational(1,3),s.Rational(1,5))
    shift=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    check('unitary word trace is bounded by the full-time charge heat trace', abs(s.trace(heat*shift*heat*shift*heat*shift))<=s.trace(heat**3))
    v=s.Matrix([1,2,3]); Q=s.eye(3)+v*v.T
    check('positive transfer compression gives the correct lower direction', s.trace(Q**3)>=Q[0,0]**3)
    q=s.Rational(1,4); delta=s.Rational(3,4); T=5; mass2=s.Integer(4)
    A=cycle_laplacian(T)/delta+delta*mass2*s.eye(T)
    inverse=A.inv(); gm=memory.temporal_green(q,delta,T,0)
    check('temporal inverse trace is exact, not a repeated zero-frequency bound', s.trace(inverse)==T*gm and T*gm<T/(delta*mass2))
    epsilon=s.Rational(1,100); eta=epsilon/(delta*mass2)
    check('trace logarithm bound retains the Gaussian one-half and relative margin', trace_log_bound(epsilon,7,T,gm,eta)==epsilon*7*s.trace(inverse)/(2*(1-eta)))
    # Verify the stronger temporal lower bound on the actual scalar elimination.
    blocks,C,*_=memory.physical_blocks(old,local,3)
    full_sites,spatial=local.spatial_stiffness(3,s.Integer(1))
    S=[i for i,x in enumerate(full_sites) if any(a==0 for a in x)]
    temporal=cycle_laplacian(3)/delta
    fast=s.kronecker_product(temporal,s.eye(8))+delta*s.diag(*blocks)
    retained=s.kronecker_product(temporal,s.eye(len(S)))+delta*s.diag(*([spatial.extract(S,S)]*3))
    coupling=delta*s.kronecker_product(s.eye(3),C)
    K=retained-coupling*fast.inv()*coupling.T
    reference=s.kronecker_product(temporal+delta*s.eye(3),s.eye(len(S)))
    check('actual moving-cell Schur kernel retains the full temporal mass bound', (K-reference).is_positive_semidefinite)
    x,m=s.symbols('delta m',positive=True)
    qmass=1+x**2*m**2/2-x*m*s.sqrt(4+x**2*m**2)/2
    sinh=(1/qmass-qmass)/2
    check('temporal trace normalization has a finite time-refinement prefactor', s.simplify(s.limit(x/(2*sinh),x,0,dir='+')-1/(2*m))==0)
    rho=s.Symbol('rho',positive=True)
    check('normalized observable error retains numerator and denominator terms', s.simplify(relative_observable_error(rho)-(rho/(1-rho)+rho/(1-rho)))==0)
    check('charge cutoff splits half a time slice, not half the full time', relative_charge_tail(Fraction(1),3,1,Fraction(0),31)==Fraction(3*theta_upper(Fraction(5,6),1),2**math.floor(Fraction(32**2,372))))
    theta=Fraction(7,3); P=9
    partial=sum(theta**r/math.factorial(r) for r in range(P+1,P+25))
    tail=relative_hop_tail(theta,P,1)
    check('factorial hop tail dominates a positive exact omitted prefix', partial<tail and tail==theta**10/math.factorial(10)/(1-theta/11))
    for total in range(5):
        coefficient=sum(Fraction(1,math.factorial(a)*math.factorial(b)*math.factorial(total-a-b)) for a in range(total+1) for b in range(total-a+1))
        check(f'order{total}: slice allocations use total hop count and multinomial weights', coefficient==Fraction(3**total,math.factorial(total)))
    plan=error_plan()
    check('rational all-J planner certifies its combined requested error', plan['total_error']<=plan['tolerance'] and plan['theta']==Fraction(648,5))
    check('planner keeps charge and word tails separately below half tolerance', plan['charge_error']<=Fraction(1,200) and plan['hop_error']<=Fraction(1,200))
    check('planner does not pretend its full partition sum was executed', plan['partition_sum_executed'] is False and plan['full_memory'] is True and plan['candidate_decimal_digits_upper']>1000)
    try: relative_hop_tail(Fraction(10),3,1)
    except ValueError: rejected=True
    else: rejected=False
    check('invalid factorial geometric ratio is rejected', rejected)
    cert.witnesses.update({'N':27,'beta':'1','T':3,'J':'1/10','theta':str(plan['theta']),
        'certified_charge_box_K':plan['K'],'certified_total_hop_order_P':plan['P'],
        'relative_error_upper_target':'1/100','candidate_envelope_decimal_digits_upper':plan['candidate_decimal_digits_upper'],
        'memory_truncated_in_planner':False,'full_partition_sum_executed':False})
    cert.emit('Absolute convergence and certified finite charge/word/memory tails for the neutral finite-volume finite-time Euclidean model, with an exact rational bound planner. No executed full partition value, efficient sign cure, uniform continuum or real-time theorem.')


if __name__=='__main__': main()
