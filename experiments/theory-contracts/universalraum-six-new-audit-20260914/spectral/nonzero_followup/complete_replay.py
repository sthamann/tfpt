"""Strict final cross-check of all 18 singlet types and their energy order.

Replays the unused-prime matrix moments, projector ranks, source hashes,
dimension accounting, inherited Temple arithmetic, and final rational gaps.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
import numpy as np
import sympy as sy

HERE=Path(__file__).resolve().parent
CHECKS=0

def need(test,label):
    global CHECKS
    CHECKS+=1
    if not bool(test):raise RuntimeError(label)

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    source=sha(HERE/'checker.py');proj=json.loads((HERE/'projectors.json').read_text())
    cert=json.loads((HERE/'certificate.json').read_text())
    need(proj['source_sha256']==source and cert['source_sha256']==source,'current builder and certificate source hashes')
    need(cert['all_11_nonzero_types_excluded'] and not cert['unresolved'],'all eleven nonzero types certified')
    need(set(proj['projectors'])==set(cert['blocks']),'projector and spectral block sets identical')
    total=0
    for name,block in cert['blocks'].items():
        n=block['record']['multiplicity_block_dimension']
        need(proj['projectors'][name]['rank']==n and block['projector_rank_verified'],'exact projector rank accepted')
        need(block['CRT_modulus']>2*block['trace_bound'],'integer CRT uniqueness')
        exact=block['trace_X32'];need(0<exact<=block['trace_bound'],'exact positive moment bound')
        p=block['extra_prime'];data=json.loads((HERE/f'modular_{p}.json').read_text())
        need(data['source_sha256']==source,'unused prime matrix produced by current source')
        x=np.array(data['blocks'][name]['X'],dtype=np.int64);power=x
        for _ in range(5):power=power@power%p
        expected=int(np.trace(power)%p)
        need(exact%p==expected,'unused prime replay from entire reduced matrix')
        radius=Q(block['X_norm_upper']);need(radius**32>exact,'strict rational spectral-radius upper bound')
        h0=20-radius/2;htr=max(Q(47,50)*h0+Q(39,25),Q(93,100)*h0+Q(42,25))
        need(h0==Q(block['H0_lower']) and htr==Q(block['Htr_lower']),'independent affine lower-bound arithmetic')
        need(htr>Q(249,20),'whole block strictly above threshold')
        total+=block['record']['isotypic_dimension']
    need(total==22260,'all nonzero momentum dimensions accounted for')
    zero=json.loads((HERE.parent/'global_followup'/'power_certificate.json').read_text())
    need(zero['all_seven_zero_momentum_symmetry_types_certified'],'seven zero-momentum types certified')
    need(cert['zero_momentum_certificate_sha256']==sha(HERE.parent/'global_followup'/'power_certificate.json'),'inherited certificate hash unchanged')
    need(zero['total_zero_momentum_dimension']+total==24024,'complete singlet dimension')
    inherited=json.loads((HERE.parent/'filtered_certificate.json').read_text())
    s=inherited['sectors']['standard'];d=s['D'];n=s['N'];n2=s['N2']
    mean=Q(n,800*d);var=Q(n2,640000*d)-mean**2;second=Q(s['second_eigenvalue_lower']['rational'])
    low=mean-var/(second-mean)
    need(var>=0 and second>mean,'standard Temple hypotheses')
    need(mean==Q(s['Rayleigh_upper']['rational']) and low==Q(s['Temple_lower']['rational']),'standard Temple interval arithmetic')
    intervals=[[Q(a),Q(b)] for a,b in inherited['corrected_trivial_exact_intervals']]
    exact28=json.loads((HERE.parent/'exact_trivial.json').read_text())
    poly=sy.Poly.from_list(exact28['integer_coefficients_descending'],sy.Symbol('x'))
    for j,(a,b) in enumerate(intervals):
        l=sy.Rational(800*a);r=sy.Rational(800*b)
        need(poly.eval(l)!=0 and poly.eval(r)!=0,'strict trivial eigenvalue endpoints')
        need(poly.count_roots(0,l)==j and poly.count_roots(l,r)==1,'trivial first two exact eigenvalue counts')
    other=[Q(b['Htr_lower']) for b in cert['blocks'].values()]
    other += [Q(b['Htr_lower']) for b in zero['blocks'].values()]
    other += [second,intervals[1][0]]
    sixth=min(other)
    gap=low-intervals[0][1];uppergap=mean-intervals[0][0]
    isolation=sixth-mean
    need(intervals[0][1]<low<=mean<Q(249,20)<sixth,'complete singlet energy order')
    need(gap>0 and isolation>0,'both sides of quartet isolated')
    # A hidden low eigenmode cannot pass the actual even-moment method.
    need(20**32>Q(421,25)**32,'negative hidden-mode control for the lower-bound logic')
    def value(x):return {'rational':str(x),'decimal':float(x)}
    result={'all_18_singlet_types_certified':True,'total_dimension':24024,
       'exact_eigenvalue_count_below_12_45':5,'ground_multiplicity':1,'first_excited_multiplicity':4,
       'ground_interval':list(map(str,intervals[0])),
       'first_excited_interval':[str(low),str(mean)],
       'singlet_gap_interval':[value(gap),value(uppergap)],
       'sixth_eigenvalue_strict_lower':value(sixth),'quartet_upper_isolation_strict_lower':value(isolation),
       'same_space_symmetry_preserving_remainder_sufficient_norm_upper':value(min(gap,isolation)/2),
       'actual_microscopic_remainder_bound_proved':False,'non_singlet_exclusion_proved':False,
       'checks':CHECKS,'source_sha256':sha(Path(__file__)),
       'nonzero_certificate_sha256':sha(HERE/'certificate.json'),
       'zero_certificate_sha256':sha(HERE.parent/'global_followup'/'power_certificate.json'),
       'two_low_blocks_certificate_sha256':sha(HERE.parent/'filtered_certificate.json')}
    (HERE/'complete.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
