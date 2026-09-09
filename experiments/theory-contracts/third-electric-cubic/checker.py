"""Full cubic MEEE census, seven-leg norm control and isolated source column.

NON-RH / fixed conditional parent. No combined readout or TOE completion.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import argparse
import hashlib
import importlib.util
import json
from math import factorial, prod
from pathlib import Path
import struct
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PINS={'checker.py':'b03ce3064756d8ba6ffca22e0b3732fbbea478b26e5c0f135d7ca0bcc0db1a2c',
      'validation.json':'e72c919635012a0f4d75ae140606e6721ea17955ba19295a414011c681c3b8dc'}
CREATES=(True,False,True,False,True,False,False)
FORCE_INCIDENCE=((F(29,144),F(1,12)),(F(1,12),F(0)))
FORCE_LENGTH_INCIDENCE=((F(17,72),F(1,12)),(F(1,12),F(0)))

def require(ok,message):
    if not ok: raise ValueError(message)

def inherited(root):
    folder=Path(root)/'experiments/theory-contracts/seventh-frontier-edge'
    for name,digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'frontier pin: '+name)
    record=json.loads((folder/'validation.json').read_text())
    for name,digest in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,'frontier source: '+name)
    spec=importlib.util.spec_from_file_location('seventh_for_third_E',folder/'checker.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module.inherited(root)

@lru_cache(maxsize=100000)
def moments(dots,lengths):
    """Independent nonnegative-polynomial Dirichlet moment calculation."""
    n=len(lengths)
    require(1<=n<=8 and 1<=len(dots)<=4 and all(len(d)==n for d in dots),'moment shape')
    require(all(type(x) is int and x>=0 for x in lengths),'integer current lengths')
    require(all(type(x) is int for d in dots for x in d),'integer phase differences')
    polynomial={(0,)*n:1}
    for d in dots:
        updated=defaultdict(int)
        for powers,c in polynomial.items():
            for j,x in enumerate(d):
                if x:
                    p=list(powers);p[j]+=1;updated[tuple(p)]+=c*abs(x)
        polynomial=updated
    a=b=0
    for powers,c in polynomial.items():
        value=c*prod(factorial(x) for x in powers)
        a+=value;b+=value*sum((x+1)*length for x,length in zip(powers,lengths))
    return a,b

def append_E(parents,paths,row=None,sites=None,indexed=True):
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    actual=r40.cubic_row if row is None else row
    force=r49.force_index(r42,r40) if row is None and sites is None and indexed else lambda fs:r42.force_terms(r40,actual,fs,sites)
    @lru_cache(maxsize=256)
    def cached(prefixes):return tuple(force(prefixes))
    for q in paths:
        require(q['kind']=='MEE' and q['order']==3 and len(q['word'])==5,'complete original MEE source')
        require(len(q['dots'])==2 and len(q['prefixes'])==3 and len(q['frequencies'])==len(q['signs'])==4,'MEE phase shape')
        for a,b,shift,w,dots in cached(q['prefixes']):
            current=r40.merge(q['flux'],shift);word=(a,b)+q['word']
            energy=sum((1 if c else -1)*(25 if m[1]==0 else 9600) for m,c in zip(word,CREATES))
            last=12*r42.dot(current,current)+energy
            first=tuple(f+(last,) for f in q['frequencies']);delta=(0,)+tuple(24*x for x in dots)+(0,)
            second=tuple(tuple(x+y for x,y in zip(f,delta)) for f in first)
            yield {'kind':'MEEE','word':word,'flux':current,'weight':q['weight']*w,'order':4,
                   'prefixes':q['prefixes']+(current,),'dots':tuple(d+(0,) for d in q['dots'])+(dots+(0,),),
                   'frequencies':first+second,'signs':q['signs']+tuple(-x for x in q['signs'])}

def physical_key(flips,flux,frequencies):
    values=[len(flips)]
    for x,species in flips:values.extend((*x,species))
    values.append(len(flux))
    for edge,w in flux:values.extend((*edge,w))
    return tuple(values)+frequencies

def census_groups(parents,paths,folder,multiplicity=6):
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    require(multiplicity in (1,6),'declared source multiplicity')
    vectors={name:[0]*128 for name in ('raw_matter','raw_phase','nonzero_matter','nonzero_phase')}
    groups=defaultdict(int);counts=Counter();max_current=0;flip_counts=Counter()
    for p in paths:
        require(p['kind']=='MEEE' and p['order']==4 and len(p['word'])==7 and len(p['dots'])==3,'third-E source shape')
        lengths=tuple(map(r42.length,p['prefixes']))
        require(all(d[-1]==0 for d in p['dots']) and lengths[-1]<=7,'complete current envelope')
        a,b=moments(p['dots'],lengths);w=abs(p['weight'])
        pattern=sum(mode[1]<<j for j,mode in enumerate(p['word']))
        counts['raw']+=1;max_current=max(max_current,lengths[-1])
        dead=r48.whole_fock_zero(p['word'],CREATES)
        counts['whole_fock_zero']+=dead
        for prefix in (('raw',) if dead else ('raw','nonzero')):
            vectors[prefix+'_matter'][pattern]+=w*a;vectors[prefix+'_phase'][pattern]+=w*b
        # Preparation-specific action happens strictly after the norm census.
        step=r47.relative_action(p['word'],CREATES)
        if step:
            counts['nonzero_bare_actions']+=1;flip_counts[len(step[0])]+=1
            for f,sign in zip(p['frequencies'],p['signs']):
                groups[physical_key(step[0],p['flux'],tuple(sorted(f)))]+=step[1]*sign*p['weight']
        require(counts['raw']<=2000000 and len(groups)<=5000000,'bounded full MEEE census')
    groups={key:w for key,w in groups.items() if w}
    output=Path(folder)/'third-electric-groups.bin'
    with output.open('wb') as stream:
        stream.write(struct.pack('<Q',len(groups)))
        for key,w in sorted(groups.items()):
            require(-(1<<63)<w<(1<<63),'signed integer output weight')
            stream.write(struct.pack('<i',len(key)));stream.write(struct.pack('<'+'i'*len(key),*key));stream.write(struct.pack('<q',w))
    scale=F(multiplicity,576**4)
    census={'raw_count':multiplicity*counts['raw'],'whole_fock_zero_count':multiplicity*counts['whole_fock_zero'],
            'nonzero_bare_action_count':multiplicity*counts['nonzero_bare_actions'],
            'representative_bare_flip_census':dict(sorted(flip_counts.items())),
            'maximum_final_current_length':max_current,'multiplicity':multiplicity,
            'vectors':{name:[scale*x for x in v] for name,v in vectors.items()},
            'initial_projection_used_in_norm':False}
    grouped={'path':output,'order':4,'arity':7,'multiplicity':multiplicity,'cost':{'groups':len(groups)}}
    return census,grouped

def boundary(parents,census,time=F(1)):
    T=abs(F(time));require(T<=1,'certified time domain')
    require(census['multiplicity']==6 and census['raw_count']==441456 and
            census['whole_fock_zero_count']==346236 and not census['initial_projection_used_in_norm'],
            'complete whole-cubic MEEE norm census')
    r38=parents[-2]
    c=(r38.sqrt_interval(F(107,2048))[1],r38.sqrt_interval(F(1,96))[1])
    a=census['vectors']['nonzero_matter'];b=census['vectors']['nonzero_phase']
    A=sum(w*sum(c[(s>>j)&1] for j in range(7)) for s,w in enumerate(a))
    M=F(1,100)**3*A*T**8/factorial(8)
    E=F(1,100)**4*F(53,288)*sum(b)*T**9/factorial(9)
    old=json.loads((HERE.parent/'direct-defect-round48/validation.json').read_text())['census'][1]
    old_E=F(1,100)**3*F(53,288)*sum(map(F,old['vectors']['nonzero_phase']))*T**7/factorial(7)
    return {'MEEEM':M,'MEEEE':E,'upper':M+E,'old_MEEE_upper':old_E,
            'change_to_complete_otherwise_unchanged_defect':M+E-old_E,
            'matter_order':8,'electric_order':9,'fourth_E_kept':True,
            'isolated_source_operator_norm_upper':F(1,100)**3*sum(a)*T**7/factorial(7)}

def electric_transport(phase,order,electric_count):
    """Upper moments after one E, for the two declared original leaf families.

    Requires the original prefix envelope |r_i|_1 <= 2i-1. No new raw
    census or initial-space projection is implied by these upper tensors.
    """
    require((order,electric_count) in ((3,2),(4,1)),'declared E-transport family')
    d=2*electric_count+1
    require(len(phase)==1<<d and all(x>=0 for x in phase),'positive old phase tensor')
    coefficient=order**2+(electric_count+2)*(2*order-1)
    a=[F(0)]*(1<<(d+2));b=a.copy()
    for old,weight in enumerate(phase):
        for left in (0,1):
            for right in (0,1):
                target=(old<<2)|left|(right<<1)
                inc=FORCE_INCIDENCE[left][right];jump=FORCE_LENGTH_INCIDENCE[left][right]
                a[target]+=inc*weight;b[target]+=(coefficient*inc+jump)*weight
    return {'matter_upper':a,'phase_upper':b,'quadratic_envelope_coefficient':coefficient,
            'new_arity':d+2,'order':order+1,'electric_count':electric_count+1}

def transport_boundary(parents,phase,order,electric_count,time=F(1)):
    T=abs(F(time));require(T<=1,'transport time domain')
    tensors=electric_transport(phase,order,electric_count)
    C=[parents[-2].sqrt_interval(x)[1] for x in (F(107,2048),F(1,96))]
    n,k,d=tensors['order'],tensors['electric_count'],tensors['new_arity']
    a=sum(w*sum(C[(s>>j)&1] for j in range(d)) for s,w in enumerate(tensors['matter_upper']))
    M=F(1,100)**k*a*T**(n+k+1)/factorial(n+k+1)
    E=F(1,100)**(k+1)*F(53,288)*sum(tensors['phase_upper'])*T**(n+k+2)/factorial(n+k+2)
    old=F(1,100)**k*F(53,288)*sum(phase)*T**(n+k)/factorial(n+k)
    return {'upper':M+E,'next_matter':M,'next_electric':E,'old_electric_boundary':old,
            'tensors':tensors,'new_matter_order':n+k+1,'new_electric_order':n+k+2,
            'new_full_cubic_raw_census_claimed':False}

def edge_gate(parents):
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    data=r43.geometry(parent,'edge');row=r40.parent_rows(data)
    paths=list(append_E(parents,r45.two_e_paths(r42,r41,r40,row,0,range(2),False),row,range(2)))
    full=r38.tree_model(parent,1,center=False);charged=r38.tree_model(parent,1,particles=1,center=False)
    columns=[j for j,(_,flux) in enumerate(full['basis']) if flux==(0,)]
    matrix=[[F(0) for j in columns] for i in range(4)]
    for (word,flux),value in r49.electric_jet(paths,7).items():
        for pos,j in enumerate(columns):
            current=full['basis'][j][0];sign=1
            for (site,species),create in zip(word[::-1],CREATES[::-1]):
                step=r41.fermion_action(current,site+2*species,create)
                if step is None:break
                current,parity=step;sign*=parity
            else:matrix[charged['index'][current,(dict(flux).get(0,0),)]][pos]+=value*sign
    expected=json.loads((HERE.parent/'seventh-frontier-edge/validation.json').read_text())['seventh_order_physical_contributions']['MEEE']
    require([str(x) for row in matrix for x in row]==expected,'independent original physical MEEE matrix')
    require(all(not r49.electric_jet(paths,j) for j in range(7)) and any(x for row in matrix for x in row),'first nonzero source grade seven')
    return {'raw_count':len(paths),'first_nonzero_grade':7,'physical_matrix':[str(x) for row in matrix for x in row]}

def run(root=ROOT):
    parents=inherited(root);r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    edge=edge_gate(parents)
    with tempfile.TemporaryDirectory(prefix='tfpt-third-electric-') as folder:
        print('Computing complete cubic MEEE census',flush=True)
        census,groups=census_groups(parents,append_E(parents,r45.two_e_paths(r42,r41,r40)),folder)
        source=r47.compile_groups(r41,r39,groups)
        linear={'coefficients':{},'denominator':1,'time':F(1),'numerical_error':F(0)}
        column=r47.common_bare_column(r45,r41,linear,[],[source])
        bounds=boundary(parents,census)
        old=json.loads((HERE.parent/'direct-defect-round48/validation.json').read_text())['census']
        transported={}
        for name,item,n,k in (('MEEE',old[1],3,2),('MEMME_MMEME_MMMEE',old[0],4,1)):
            transported[name]=transport_boundary(parents,list(map(F,item['vectors']['nonzero_phase'])),n,k)
            require(transported[name]['upper']<transported[name]['old_electric_boundary'],'improved positive transport boundary')
        require(all(x<=y for x,y in zip(census['vectors']['nonzero_matter'],transported['MEEE']['tensors']['matter_upper'])) and
                all(x<=y for x,y in zip(census['vectors']['nonzero_phase'],transported['MEEE']['tensors']['phase_upper'])),
                'independent full cubic moment transport containment')
        hi=r38.sqrt_interval(column['probability'])[1]
        require(hi<=bounds['isolated_source_operator_norm_upper']+source['numerical_error'],'whole-cubic source norm control')
        require(bounds['upper']<bounds['old_MEEE_upper'],'strictly improved MEEE branch bound')
        return r38.encode({'verdict':'FULL_CUBIC_MEEE_CENSUS_AND_ISOLATED_SOURCE_EVALUATED',
            'parent_pins':PINS,'census':census,'boundary':bounds,'edge':edge,'positive_E_transport':transported,
            'isolated_source_squared_norm':column['probability'],'isolated_source_output_count':column['output_count'],
            'numerical_error':source['numerical_error'],'representative_output_count':len(source['vector']),
            'phase_kernel_count':source['frequency_kernels'],'frequency_group_count':groups['cost']['groups'],
            'grouped_bytes':groups['path'].stat().st_size,'whole_cubic_source_evaluated':True,
            'combined_bulk_readout_evaluated':False,'new_global_time_order_claimed':False,
            'full_electric_dynamics_solved':False,'T1_T8_solved':False,
            'sources':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('checker.py','test_checker.py','README.md')}})

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=ROOT);parser.add_argument('--output',type=Path)
    args=parser.parse_args();text=json.dumps(run(args.repo),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')

if __name__=='__main__':main()
