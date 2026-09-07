#!/usr/bin/env python3
from fractions import Fraction as F
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round27_algebra import Certificate,ceil_root,error_plan,first_true,inputs,memory_relative_error,memory_witness,relative_charge_tail,relative_hop_tail,theta_upper


def main():
    previous,old=inputs(); cert=Certificate(); check=cert.check
    check('reference Gaussian envelope retains the original eight coordinates', theta_upper(1,27)==83**216==previous.theta_upper(1,27))
    roots=[(n,d) for d in (1,2,3,9,33) for n in (0,1,2,7,8,9,31,64,65,2**231+1)]
    check('integer root rounds upwards even immediately after perfect powers', all((ceil_root(n,d)==0 if n==0 else (ceil_root(n,d)-1)**d<n<=ceil_root(n,d)**d) for n,d in roots))
    theta=F(7,3); P=9
    check('relative word bound has factorial and correct geometric ratio', relative_hop_tail(theta,P)==theta**10/math.factorial(10)/(1-theta/11))
    omitted=sum(theta**k/math.factorial(k) for k in range(10,35))
    check('relative word bound dominates an exact positive omitted prefix', relative_hop_tail(theta,P)>omitted)
    check('zero hopping has no word tail or artificial sign factor', relative_hop_tail(0,0)==0 and memory_relative_error(F(1,100),0)==F(1,99))
    check('charge tail uses full-reference half beta and a Tth root', relative_charge_tail(1,3,1,0,31)==F(3*ceil_root(theta_upper(F(1,2),1),3),2**math.floor(F(32**2,372))))
    check('memory budget retains exponent margin and cancellation factor', memory_relative_error(F(1,100),F(7,3))==F(27,99))
    invalid=0
    for call in (lambda:ceil_root(1,0),lambda:relative_hop_tail(10,3),lambda:relative_hop_tail(-1,3),
                 lambda:memory_relative_error(1,1),lambda:error_plan(memory_error=F(1,100)),
                 lambda:memory_witness(-1),lambda:memory_witness(17)):
        try: call()
        except ValueError: invalid+=1
    check('invalid roots tail domains and memory margins fail explicitly', invalid==7)
    check('monotone integer search handles zero one and large thresholds', all(first_true(lambda x,b=b:x>=b)==b for b in (0,1,2,7,128,2670)))
    p=error_plan()
    check('original comparison budget certifies without full partition execution', p['total_error']<=p['tolerance'] and p['partition_sum_executed'] is False and p['full_memory'] is True)
    check('original comparison cutoffs are exact declared first passing integers', (p['K'],p['P'])==(2670,354))
    check('both immediate smaller cutoffs fail their own conservative budgets', relative_charge_tail(1,3,27,F(1,10),p['K']-1)>p['tail_allowance'] and relative_hop_tail(p['theta'],p['P']-1)>p['tail_allowance'])
    oldK=first_true(lambda k:previous.relative_charge_tail(F(1),3,27,F(1,10),k)<=F(1,200))
    oldP=first_true(lambda k:k+2>p['theta'] and previous.relative_hop_tail(p['theta'],k,previous.theta_upper(1,27))<=F(1,200))
    check('proof improvement survives equal first-passing-integer search', oldK>p['K'] and oldP>p['P'])
    w=memory_witness(12); delta=w['delta']; qb=w['q_gap']; qm=w['q_mass_lower']
    check('memory witness is the actual ell3 interior and retained lattice count', w['N']==9**3 and w['retained']==9**3-27*8 and w['cell_gap']==w['m_squared']+3)
    check('cyclic decay parameter matches cell gap and time step exactly', qb+1/qb==2+delta**2*w['cell_gap'])
    check('mass comparison is in the conservative inverse-trace direction', (qm+1/qm-2)/delta**2==F(8,9)<w['m_squared'])
    check('witness physical coupling retains all original directed channels', w['beta']*48*w['N']*w['J']==1 and w['J']==F(1,866052))
    q=F(1,4); expected_tau=delta*q**13/(((1/q-q)/2)*(1-q)*(1-q**33))
    check('memory tail keeps wrap factor both temporal directions and scalar coupling', w['epsilon']==delta**2*36*expected_tau)
    gm=delta/(1/qm-qm)*(1+qm**33)/(1-qm**33)
    check('memory logarithm retains half determinant trace and positive margin', w['B']==w['epsilon']*513*33*gm/(2*(1-w['eta'])))
    check('nonzero memory radius survives the fully summed signed budget', 0<w['eta']<1 and 0<w['B']<1 and w['memory_error']<=F(2045,1000000)<F(1,300) and 0<w['R']<w['T']//2)
    check('previous radius fails chosen subbudget without an impossibility claim', memory_witness(11)['memory_error']>F(1,300))
    check('full memory endpoint has exactly zero approximation error', memory_witness(16)['memory_error']==0)
    combined=error_plan(w['N'],w['T'],w['beta'],w['J'],memory_error=w['memory_error'])
    check('combined nonzero memory charge and hop budget is certified', combined['total_error']<=F(1,100) and (combined['K'],combined['P'])==(12235,5))
    check('combined plan keeps full determinant and never invents an evaluated sum', w['exact_fast_determinant_retained'] is True and combined['full_memory'] is False and combined['partition_sum_executed'] is False)
    check('naive candidate count remains explicitly astronomical', p['candidate_decimal_digits_upper']==1912 and combined['candidate_decimal_digits_upper']==25624)
    cert.witnesses.update({'comparison':{'N':27,'T':3,'beta':'1','J':'1/10','theta':'648/5',
        'old_published_K':4096,'old_published_P':962,'old_bound_refined_K':oldK,'old_bound_refined_P':oldP,
        'new_K':p['K'],'new_P':p['P'],'omission_error_target':'1/100',
        'candidate_envelope_digit_upper':p['candidate_decimal_digits_upper']},
        'nonzero_memory':{'L':9,'N':729,'T':33,'beta':'99/4','J':'1/866052','theta':'1',
            'm_squared':'1','u_nu':'any nonnegative','R':12,'retained_time_offsets':25,
            'omitted_time_offsets':8,'memory_error_upper':'2045/1000000','K':combined['K'],'P':combined['P'],
            'combined_error_target':'1/100','candidate_envelope_digit_upper':combined['candidate_decimal_digits_upper'],
            'full_fast_determinant_retained':True},'full_partition_sum_executed':False,
        'roundoff_for_future_partition_evaluation_is_additional':True})
    cert.emit('Exact rational finite-regulator error bounds, including one genuine nonzero quadratic-memory cutoff after the signed sum. No evaluated full partition, efficient sampler, continuum, real time or full T1-T8 solution.')


if __name__=='__main__': main()
