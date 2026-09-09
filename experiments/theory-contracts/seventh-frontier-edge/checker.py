"""Complete seventh weighted source grade on the fixed original physical edge.

NON-RH / finite same-parent algebra only; no new bulk error or TOE result.
"""
import argparse
import hashlib
import importlib.util
from pathlib import Path
from fractions import Fraction as F
from collections import Counter, defaultdict
from math import factorial
import json
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    'checker.py': 'aca120c6ec9b813be9fc87fa401ae38a87d36a8d46334d504baaaee1f79b72b8',
    'SIXTH_SOURCE.md': '5350c378771f75380044b8ddb8cb8466e51ce6bc7e55efd7eb068d3872c70fae',
    'validation.json': '67ca1c8fd78a93b513f01b09a364d88d00a7f1e11b43221e2b7f62e033042832',
}

def require(ok, message):
    if not ok: raise ValueError(message)

def inherited(root):
    folder=Path(root)/'experiments/theory-contracts/sixth-source-round49'
    for name,digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest, 'Round49 pin: '+name)
    record=json.loads((folder/'validation.json').read_text())
    for name,digest in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest, 'Round49 source: '+name)
    spec=importlib.util.spec_from_file_location('r49_seventh_edge',folder/'checker.py')
    r49=importlib.util.module_from_spec(spec); spec.loader.exec_module(r49)
    return (r49,*r49.inherited(root))

def run(root=ROOT):
    parents=inherited(root)
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent = parents
    data, old, recent = r49.edge_paths(parents[1:]); row = r40.parent_rows(data)
    creates = lambda n: (True, False)*((n-1)//2)+(False,)

    def append_E(paths):
        for q in paths:
            require(1 <= len(q['dots']) <= 2 and len(q['word']) == 2*len(q['dots'])+1, 'one or two prior E events')
            require(len(q['prefixes']) == q['order'] and all(len(d)==q['order'] for d in q['dots']), 'complete phase prefixes')
            require(len(q['frequencies']) == len(q['signs']) == 2**len(q['dots']), 'complete signed phase branches')
            for a,b,shift,w,dots in r42.force_terms(r40,row,q['prefixes'],range(2)):
                current = r40.merge(q['flux'],shift); word = (a,b)+q['word']
                energy = sum((1 if c else -1)*(25 if mode[1]==0 else 9600) for mode,c in zip(word,creates(len(word))))
                last = 12*r42.dot(current,current)+energy
                unshifted = tuple(f+(last,) for f in q['frequencies'])
                delta = (0,)+tuple(24*d for d in dots)+(0,)
                shifted = tuple(tuple(x+y for x,y in zip(f,delta)) for f in unshifted)
                yield {**q,'kind':q['kind']+'E','word':word,'flux':current,'weight':q['weight']*w,
                       'order':q['order']+1,'prefixes':q['prefixes']+(current,),
                       'frequencies':unshifted+shifted,'signs':q['signs']+tuple(-x for x in q['signs']),
                       'dots':tuple(d+(0,) for d in q['dots'])+(dots+(0,),)}

    def first_E(depth):
        require(type(depth) is int and 1 <= depth <= 5, 'finite first-E depth')
        def walk(mode, flux, prefixes, modes, weight):
            if len(prefixes)==depth:
                base=(-9600,)+tuple(12*(2*r42.dot(f,flux)-r42.dot(f,f))-(25 if m[1]==0 else 9600)
                                    for f,m in zip(prefixes,modes))
                for a,b,shift,w,dots in r42.force_terms(r40,row,prefixes,range(2)):
                    final=r40.merge(flux,shift); word=(a,b,mode)
                    f0=base+(12*r42.dot(final,final)+r42.energy(word),)
                    delta=(0,)+tuple(24*x for x in dots)+(0,)
                    yield {'kind':'M'*depth+'E','word':word,'flux':final,'weight':(-1)**(depth-1)*weight*w,
                           'order':depth+1,'prefixes':prefixes+(final,),'dots':(dots+(0,),),
                           'frequencies':(f0,tuple(x+y for x,y in zip(f0,delta))),'signs':(1,-1)}
                return
            for target,shift,w in row(mode):
                final=r40.merge(flux,shift)
                yield from walk(target,final,prefixes+(final,),modes+(target,),weight*w)
        yield from walk((0,1),(),(),(),1)

    def canonical(paths):
        out=defaultdict(int)
        for p in paths:
            for f,sign in zip(p['frequencies'],p['signs']):
                out[p['word'],p['flux'],tuple(sorted(f))]+=p['weight']*sign
        return {k:v for k,v in out.items() if v}

    for depth in range(1,5):
        require(canonical(first_E(depth))==canonical(r49.first_e_paths(r45,r42,r40,depth,row,0,range(2),False)), 'old first-E comparison')
    first=list(first_E(1))
    two=list(r45.two_e_paths(r42,r41,r40,row,0,range(2),False))
    require(canonical(append_E(first))==canonical(two),'independent old two-E comparison')
    corrections=[]
    for p in r42.enumerate_corrections(r40,r41,row,0,range(2)):
        corrections.append({**p,'order':3,'frequencies':(p['frequencies0'],p['frequencies1']),
                            'signs':(1,-1),'dots':(p['electric_dots'],)})
    require(canonical(append_E(corrections))==canonical(p for p in recent if len(p['word'])==5),'old MEME/MMEE comparison')
    one=list(r45.one_e_paths(r42,r41,r40,row,0,range(2),False))
    append_M=lambda paths:r49.append_M(r45,r42,r40,paths,row)
    new50=list(append_M(append_M(one)))
    remaining=list(append_E(two))+list(append_M(append_M(two)))+list(append_M(p for p in recent if len(p['word'])==5))
    remaining+=list(append_E(one))+list(append_M(p for p in recent if len(p['word'])==3))+list(first_E(5))
    counts = dict(Counter(p['kind'] for p in new50+remaining))

    full=r38.tree_model(parent,1,center=False); charged=r38.tree_model(parent,1,particles=1,center=False)
    hn=s.Matrix([[s.Rational(row.get(j,0),14400) for j in range(6)] for row in full['rows']])
    hq=s.Matrix([[s.Rational(row.get(j,0),14400) for j in range(4)] for row in charged['rows']])
    c=s.zeros(4,6)
    for j,(mask,flux) in enumerate(full['basis']):
        step=r41.fermion_action(mask,2)
        if step:c[charged['index'][step[0],flux],j]=step[1]
    columns=[j for j,(_,flux) in enumerate(full['basis']) if flux==(0,)]

    def literal(values):
        matrix=s.zeros(4,6)
        for j in columns:
            for (word,flux),value in values.items():
                current=full['basis'][j][0]; sign=1
                for (site,species),create in zip(word[::-1],creates(len(word))[::-1]):
                    step=r41.fermion_action(current,site+2*species,create)
                    if step is None:break
                    current,parity=step; sign*=parity
                else:matrix[charged['index'][current,(dict(flux).get(0,0),)],j]+=s.Rational(value*sign)
        return matrix

    def matter(power):
        matrix=s.zeros(4,6)
        for site in range(2):
            aux=r43.sector(parent,data,[int(j==site) for j in range(2)])
            for species in (0,1):
                column=aux['index'][1<<(site+2*species),(0,)]
                vectors=[[int(j==column) for j in range(4)]]
                for k in range(power):vectors.append([sum(w*vectors[-1][j] for j,w in row.items()) for row in aux['rows']])
                for target,(mask,flux) in enumerate(aux['basis']):
                    if mask!=4:continue
                    energy=F(sum(x*x for x in flux),200)
                    value=sum((-1)**k*F(vectors[k][target],14400**k)*energy**(power-k)/(factorial(k)*factorial(power-k)) for k in range(power+1))
                    for j in columns:
                        step=r41.fermion_action(full['basis'][j][0],site+2*species)
                        if step:matrix[charged['index'][step[0],flux],j]+=s.Rational(value*step[1])
        return matrix

    results=[]; witnesses={}; contributions={}; matrices={}
    for power in range(9):
        expected=sum(((-1)**k*hq**(power-k)*c*hn**k/(factorial(k)*factorial(power-k)) for k in range(power+1)),s.zeros(4,6))[:,columns]
        base=matter(power)+literal(r49.electric_jet(old+recent+new50,power))
        upgraded=base+literal(r49.electric_jet(remaining,power))
        results.append({'order':power,'round50_matches':base[:,columns]==expected,'frontier_matches':upgraded[:,columns]==expected})
        if power==7:
            for kind in sorted(set(p['kind'] for p in new50+remaining)):
                contribution=literal(r49.electric_jet([p for p in new50+remaining if p['kind']==kind],power))
                witnesses[kind]=contribution!=s.zeros(4,6)
                contributions[kind]=list(map(str, contribution[:,columns]))
        matrices[str(power)] = {'full': list(map(str, expected)), 'baseline': list(map(str, base[:,columns])), 'completed': list(map(str, upgraded[:,columns]))}

    require(all(x['frontier_matches'] for x in results[:8]) and not results[7]['round50_matches'] and not results[8]['frontier_matches'],'finite edge order-seven frontier only')

    require(all(witnesses.values()), 'every seventh-order family has a physical witness')
    return {'verdict': 'COMPLETE_WEIGHTED_GRADE_SEVEN_SOURCE_ON_ORIGINAL_EDGE_ONLY',
            'parent_pins': PINS, 'checks': results, 'matrix_jets': matrices,
            'seventh_order_nonzero_physical_witnesses': witnesses,
            'seventh_order_physical_contributions': contributions, 'counts': counts,
            'old_first_E_formulas_reproduced_through_depth': 4,
            'old_MEE_MEME_MMEE_formulas_reproduced': True, 'E0_input_columns': len(columns),
            'full_source_matrix_shape': [4,6], 'checked_E0_matrix_shape': [4,len(columns)],
            'bulk_evaluated': False, 'new_bulk_remainder_certified': False,
            'full_electric_dynamics_solved': False, 'T1_T8_solved': False,
            'sources': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in ('checker.py','test_checker.py','README.md')}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=ROOT)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    text=json.dumps(run(args.repo),sort_keys=True,indent=2)+'\n'
    if args.output: args.output.write_text(text)
    else: print(text,end='')

if __name__=='__main__': main()
