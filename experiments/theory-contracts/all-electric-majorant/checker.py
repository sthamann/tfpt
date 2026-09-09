"""All-event source normal form and a uniform local high-field majorant.

Fixed compact U(1) parent, not parameter selection or a complete TOE.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import argparse
import hashlib
import importlib.util
import json
from math import factorial,prod
from pathlib import Path
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PINS={'checker.py':'15d6c5b7138637a510b9394ce01d2315a936739391532ac1f55a85bb75e122da',
      'validation.json':'206e07ca63db82f1ff76d290fb9752e6be0ff045bc0143f9083209b75cad2ff9'}
MU=F(77,96)
FORCE_L1=F(53,144)
KAPPA=F(1,100)

def require(ok,message):
    if not ok:raise ValueError(message)

def inherited(root=ROOT):
    folder=Path(root)/'experiments/theory-contracts/seventh-frontier-bound'
    for name,digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'frontier-bound pin: '+name)
    data=json.loads((folder/'validation.json').read_text())
    for name,digest in data['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'frontier-bound source: '+name)
    spec=importlib.util.spec_from_file_location('frontier_for_all_E',folder/'checker.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    third,parents,record=module.inherited(root)
    require(max(map(sum,parents[-4].W))==MU,'original absolute hopping row')
    require(sum(map(sum,third.FORCE_INCIDENCE))==FORCE_L1,'original absolute force incidence')
    require(parents[-3].KAPPA==KAPPA,'original electric coupling')
    return parents

def creates(word):return (True,False)*((len(word)-1)//2)+(False,)

def initial(root=(0,0,0)):
    return {'kind':'','word':((root,1),),'flux':(),'order':0,'weight':1,
            'prefixes':(),'dots':(),'base':(-9600,)}

def advance(parents,p,branch,row=None,sites=None):
    """Exact raw commutator sign; source prefactor is i**n, not -i**n.

    The finite implementation guard is a resource guard, NOT a bound on
    the number of events in the mathematical induction in README.md.
    """
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    require(branch in ('M','E') and p['order']<=15 and len(p['dots'])<=8,'finite normal-form implementation domain')
    n,k=p['order'],len(p['dots'])
    require(len(p['word'])==2*k+1 and len(p['base'])==n+1 and len(p['prefixes'])==n and all(len(d)==n for d in p['dots']),'normal form shape')
    actual=r40.cubic_row if row is None else row
    if branch=='M':
        for leg,(mode,create) in enumerate(zip(p['word'],creates(p['word']))):
            for target,shift,w in actual(mode):
                if create:shift=tuple((edge,-x) for edge,x in shift)
                word=p['word'][:leg]+(target,)+p['word'][leg+1:]
                final=r40.merge(p['flux'],shift)
                energy=sum((1 if c else -1)*(25 if m[1]==0 else 9600) for m,c in zip(word,creates(word)))
                delta=(0,)+tuple(24*r42.dot(f,shift) for f in p['prefixes'])
                base=tuple(x+y for x,y in zip(p['base'],delta))+(12*r42.dot(final,final)+energy,)
                yield {**p,'kind':p['kind']+'M','word':word,'flux':final,'order':n+1,
                       'weight':p['weight']*w*(1 if create else -1),'prefixes':p['prefixes']+(final,),
                       'dots':tuple(d+(0,) for d in p['dots']),'base':base}
    else:
        require(k<8,'finite electric-event implementation guard')
        # This intentionally uses the original full scanner, not the later index.
        for a,b,shift,w,dots in r42.force_terms(r40,actual,p['prefixes'],sites):
            word=(a,b)+p['word'];final=r40.merge(p['flux'],shift)
            energy=sum((1 if c else -1)*(25 if m[1]==0 else 9600) for m,c in zip(word,creates(word)))
            yield {**p,'kind':p['kind']+'E','word':word,'flux':final,'order':n+1,'weight':p['weight']*w,
                   'prefixes':p['prefixes']+(final,),'dots':tuple(d+(0,) for d in p['dots'])+(dots+(0,),),
                   'base':p['base']+(12*r42.dot(final,final)+energy,)}

def branches(p):
    for mask in range(1<<len(p['dots'])):
        f=list(p['base'])
        for j,d in enumerate(p['dots']):
            if (mask>>j)&1:
                for i,x in enumerate(d,1):f[i]+=24*x
        yield tuple(f),(-1)**mask.bit_count()

def paths_for_word(parents,word,row=None,root=(0,0,0),sites=None):
    require(len(word)<=16 and (not word or word[0]=='M') and set(word)<=set('ME'),'declared finite source word')
    def walk(p,remaining):
        if not remaining:yield p;return
        for q in advance(parents,p,remaining[0],row,sites):yield from walk(q,remaining[1:])
    yield from walk(initial(root),word)

@lru_cache(maxsize=100000)
def moments(dots,lengths):
    n,k=len(lengths),len(dots)
    require(1<=n<=16 and 0<=k<=8 and all(len(d)==n for d in dots),'finite moment shape')
    require(all(type(x) is int and x>=0 for x in lengths) and all(type(x) is int for d in dots for x in d),'integer moments')
    polynomial={(0,)*n:1}
    for d in dots:
        updated=defaultdict(int)
        for powers,c in polynomial.items():
            for j,x in enumerate(d):
                if x:
                    p=list(powers);p[j]+=1;updated[tuple(p)]+=c*abs(x)
        polynomial=updated
    A=B=0
    for powers,c in polynomial.items():
        a=c*prod(factorial(m) for m in powers)
        A+=a;B+=a*sum((m+1)*ell for m,ell in zip(powers,lengths))
    return A,B

def ratios(n,k,time=F(1)):
    T=abs(F(time))
    require(type(n) is int and type(k) is int and n>=1 and 0<=k<n and T<=1,'majorant event domain')
    beta=n*n+k*(2*n-1)
    M=MU*T*F(2*k+1,n+k+1)
    E=KAPPA*FORCE_L1*T*T*F(beta,(n+k+1)*(n+k+2))
    rho=MU*T+KAPPA*FORCE_L1*T*T
    require(M+E<=rho<1,'strict combined contraction')
    return M,E

def majorant(through=32,time=F(1)):
    T=abs(F(time));require(type(through) is int and 1<=through<=128 and T<=1,'finite certificate request')
    rho=MU*T+KAPPA*FORCE_L1*T*T
    level={0:T/4};rows=[]
    for n in range(1,through+1):
        mass=sum(level.values());tail=mass*rho/(1-rho)
        rows.append({'events':n,'electric_count_weights':dict(level),'level_norm_upper':mass,
                     'all_later_events_tail_upper':tail,'coarse_level_upper':T/4*rho**(n-1),
                     'two_volume_difference_upper':2*tail,'sufficient_matching_radius':2*n+2})
        if n<through:
            new=defaultdict(F)
            for k,value in level.items():
                M,E=ratios(n,k,T);new[k]+=value*M;new[k+1]+=value*E
            require(sum(new.values())<=rho*mass,'every next layer contracts')
            level=dict(sorted(new.items()))
    return {'time':T,'rho':rho,'rows':rows,'finite_code_event_cutoff':through,
            'analytic_event_cutoff':None,'tail_target':'free high field plus ALL M/E source words through the given EVENT depth',
            'numerical_evaluation_error_included':False,'tail_may_be_applied_to_Round50_column':False}

def physical_gate(parents):
    spec=importlib.util.spec_from_file_location('unsplit_all_E_check',HERE/'benchmark.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    normal=SimpleNamespace(initial=initial,advance=advance,branches=branches,creates=creates)
    return module.run(parents,normal)

def run(root=ROOT):
    parents=inherited(root)
    return parents[-2].encode({'verdict':'FIXED_PARENT_ALL_EVENT_LOCAL_SOURCE_MAJORANT',
        'parent_pins':PINS,'majorant':majorant(),'independent_physical_gate':physical_gate(parents),
        'whole_flux_and_Fock_estimate':True,'finite_volume_source_identity_derived':True,
        'local_high_field_norm_limit_derived_for_abs_time_le_1':True,
        'global_automorphism_group_constructed':False,'continuum_dynamics_constructed':False,
        'new_bulk_occupation_evaluated':False,'parameters_or_preparation_selected':False,'T1_T8_solved':False,
        'sources':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('checker.py','benchmark.py','README.md','test_checker.py')}})

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path);args=parser.parse_args()
    value=json.dumps(run(),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(value)
    else:print(value,end='')

if __name__=='__main__':main()
