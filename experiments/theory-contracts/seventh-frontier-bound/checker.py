"""Conditional full-cubic ideal bound for the formal complete grade-seven source.

No complete new bulk column is evaluated and no old probability is reused.
"""
from fractions import Fraction as F
import argparse
import hashlib
import importlib.util
import json
from math import factorial
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PINS={'checker.py':'d818cfb5eec4fa711bd0351012dd5edccce6e6a07bc9ba652b2ade92da4b1f88',
      'validation.json':'98788eae1362ee2a6574e95c9c5f96b246ac9764fe25864bb9c9fdfd9883fd95'}
WORDS=('MEMMMM','MMEMMM','MMMEMM','MEEE','MEEMM','MEMEM','MMEEM',
       'MEMME','MMEME','MMMEE','MMMMEM','MMMMME')

def require(ok,message):
    if not ok:raise ValueError(message)

def inherited(root=ROOT):
    folder=Path(root)/'experiments/theory-contracts/third-electric-cubic'
    for name,digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'third-E pin: '+name)
    record=json.loads((folder/'validation.json').read_text())
    for name,digest in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'third-E source: '+name)
    spec=importlib.util.spec_from_file_location('third_E_for_frontier_bound',folder/'checker.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module,module.inherited(root),record

def species_sum(vector,matrix,arity):
    """Positive Kronecker sum, retaining every literal CAR leg."""
    require(arity in (1,3,5,7) and len(vector)==1<<arity and all(x>=0 for x in vector),'species tensor')
    output=[F(0)]*len(vector)
    for pattern,weight in enumerate(vector):
        for leg in range(arity):
            old=(pattern>>leg)&1
            for new in (0,1):
                target=(pattern&~(1<<leg))|(new<<leg)
                output[target]+=weight*matrix[old][new]
    return output

def matter_transport(r40,a,b,f,arity):
    require(len(a)==len(b)==len(f) and all(x>=0 for x in b+f),'positive moments')
    hop=species_sum(a,r40.J,arity)
    aa=species_sum(a,r40.W,arity)
    bb=[x+y for x,y in zip(species_sum([x+y for x,y in zip(b,f)],r40.W,arity),hop)]
    ff=[x+y for x,y in zip(species_sum(f,r40.W,arity),hop)]
    return aa,bb,ff

def compressed_matter(r40,C,car,phase,order,arity):
    """One M suffix from the actual Round49 CAR marginals, not a new census."""
    require((order,arity) in ((5,3),(4,5)) and len(car)==2 and all(x>=0 for x in car) and phase>=0,'Round49 marginal family')
    mu=max(map(sum,r40.W));nu=max(map(sum,r40.J))
    total=sum(car)/arity
    old=sum(x*y for x,y in zip(car,C))
    replaced=sum(car[s]*sum(r40.W[s][t]*C[t] for t in (0,1)) for s in (0,1))
    new_car_bound=mu*(arity-1)*old+replaced
    new_phase_bound=arity*mu*(phase+(2*order-1)*total)+arity*nu*total
    return new_car_bound,new_phase_bound

def first_E_transport(third,phase,order=5):
    """The additional (n,k)=(5,0) case: exact old moments are (1,sum L_i)."""
    require(order==5 and len(phase)==2 and all(x>=0 for x in phase),'fifth pure-M prefix moments')
    a=[F(0)]*8;b=a.copy();coefficient=order**2+2*(2*order-1)
    for old,weight in enumerate(phase):
        for left in (0,1):
            for right in (0,1):
                target=(old<<2)|left|(right<<1)
                inc=third.FORCE_INCIDENCE[left][right]
                jump=third.FORCE_LENGTH_INCIDENCE[left][right]
                a[target]+=weight*inc;b[target]+=weight*(coefficient*inc+jump)
    return a,b

def outgoing(C,a,b,arity,electric_count,time=F(1)):
    A=sum(w*sum(C[(s>>j)&1] for j in range(arity)) for s,w in enumerate(a))
    return outgoing_marginal(A,sum(b),electric_count,time)

def outgoing_marginal(car,phase,electric_count,time=F(1)):
    T=abs(F(time));require(T<=1 and 1<=electric_count<=3 and car>=0 and phase>=0,'grade-seven boundary')
    M=F(1,100)**electric_count*car*T**8/factorial(8)
    E=F(1,100)**(electric_count+1)*F(53,288)*phase*T**9/factorial(9)
    return {'next_matter':M,'next_electric':E,'upper':M+E,'matter_order':8,'electric_order':9}

def certificate(third,parents,third_record,time=F(1)):
    T=abs(F(time));require(T<=1,'time domain')
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    folder=HERE.parent
    old49=json.loads((folder/'sixth-source-round49/validation.json').read_text())
    items=json.loads((folder/'direct-defect-round48/validation.json').read_text())['census']
    for item in items:item['vectors']={k:list(map(F,v)) for k,v in item['vectors'].items()}
    groups=old49['new_sources']
    for group in groups:
        for key in ('car','raw_car'):group[key]=list(map(F,group[key]))
        for key in ('phase','raw_phase'):group[key]=F(group[key])
    previous=r49.bound(parents[1:],groups,T)
    leaves=[r48.leaf_defect(r47,r46,r40,r38,item,T) for item in items]
    hierarchy=r40.hierarchy_bound(r38,12,T)
    infinite=r40.limiting_electric_budget(r38,T)
    first_tail5=infinite['upper']-sum(hierarchy['electric_remainders_by_level'][:4])
    # Independent positive decomposition of the entire old bound, not merely
    # a subtraction that can conceal an unassigned branch.
    partition49=sum(x['upper'] for x in leaves)+sum(x['upper'] for x in previous['new_leaf_defects_full_cubic'])+first_tail5
    require(previous['upper']==partition49,'complete Round49 positive boundary partition')
    C=[r38.sqrt_interval(x)[1] for x in (F(107,2048),F(1,96))]
    branches={};moments={}
    for item,names in zip(items,('MEMMMM_MMEMMM_MMMEMM','MEEMM')):
        a,b,f=[item['vectors']['nonzero_'+key] for key in ('matter','phase','final_flux')]
        for _ in range(2):a,b,f=matter_transport(r40,a,b,f,item['arity'])
        branches[names]=outgoing(C,a,b,item['arity'],(item['arity']-1)//2,T)
        moments[names]={'a':a,'b_upper':b,'f_upper':f}
    old_phase=items[0]['vectors']['nonzero_phase']
    tensors=third.electric_transport(old_phase,4,1)
    branches['MEMME_MMEME_MMMEE']=outgoing(C,tensors['matter_upper'],tensors['phase_upper'],5,2,T)
    moments['MEMME_MMEME_MMMEE']=tensors
    measured=third_record['census']['vectors']
    branches['MEEE']=outgoing(C,list(map(F,measured['nonzero_matter'])),list(map(F,measured['nonzero_phase'])),7,3,T)
    for group,names in zip(groups,('MMMMEM','MEMEM_MMEEM')):
        A,B=compressed_matter(r40,C,group['car'],group['phase'],group['order'],group['arity'])
        branches[names]=outgoing_marginal(A,B,(group['arity']-1)//2,T)
        moments[names]={'CAR_upper':A,'phase_upper':B}
    a,b=first_E_transport(third,hierarchy['rows'][4]['prefix_length_sum'])
    branches['MMMMME']=outgoing(C,a,b,3,1,T)
    moments['MMMMME']={'a_upper':a,'b_upper':b,'quadratic_coefficient':43}
    covered=[word for names in branches for word in names.split('_')]
    require(len(covered)==len(set(covered))==12 and set(covered)==set(WORDS),'twelve disjoint source families')
    retained_explicit=sum(x['extended_leaf_electric'] for x in leaves)+sum(x['next_electric'] for x in previous['new_leaf_defects_full_cubic'])
    retained_first=sum(hierarchy['electric_remainders_by_level'][5:])+infinite['tail_upper']
    removed=sum(x['old_leaf_electric']+x['extended_leaf_matter'] for x in leaves)+sum(x['next_matter'] for x in previous['new_leaf_defects_full_cubic'])+hierarchy['electric_remainders_by_level'][4]
    require(previous['upper']==removed+retained_explicit+retained_first,'all and only old grade-seven boundary removed')
    upper=retained_explicit+retained_first+sum(x['upper'] for x in branches.values())
    require(0<=upper<=previous['upper'],'nonnegative improved formal-source bound')
    return {'time':T,'upper':upper,'old49_upper':previous['upper'],'removed_grade7_boundary':removed,
            'retained_explicit_grade8_boundary':retained_explicit,'retained_first_E_after_at_least_6M':retained_first,
            'retained_first_E_infinite_tail':infinite['tail_upper'],
            'new_branches':branches,'moment_upper_certificates':moments,
            'target':'formal full cubic Z49 plus all twelve grade-seven electric source words',
            'conditional_ideal_remainder_order':8,'full_H_outer_remainder':True,
            'initial_state_null_pruning_used':False,'configuration_error_included':False}

def run(root=ROOT):
    third,parents,record=inherited(root)
    result=certificate(third,parents,record)
    return parents[-2].encode({'verdict':'CONDITIONAL_COMPLETE_GRADE7_SOURCE_BOUND_WITHOUT_COMBINED_READOUT',
        'parent_pins':PINS,'certificate':result,'source_words':WORDS,
        'all_new_full_cubic_raw_censuses_executed':False,'combined_bulk_readout_evaluated':False,
        'old_probability_reused':False,'full_electric_dynamics_solved':False,'T1_T8_solved':False,
        'sources':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('checker.py','test_checker.py','README.md')}})

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path);args=parser.parse_args()
    value=json.dumps(run(),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(value)
    else:print(value,end='')

if __name__=='__main__':main()
