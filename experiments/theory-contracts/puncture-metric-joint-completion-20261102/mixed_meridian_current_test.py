"""One mixed consequence, using the ORIGINAL current constructor and cocycle.

No P1 source, Higgs measure or independent root phases are supplied here.
The explicit A3-to-D3 map just transports the original v983 glue vectors.
"""
import itertools
import json
import sys
from pathlib import Path
from collections import Counter
import sympy as s

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'verification'))
import v983_simple_current_generator as glue
from tfpt_explorer.current_block_geometry import _actual_current_source

def need(ok,msg):
    if not ok:raise ArithmeticError(msg)

source=_actual_current_source(); ch=source['chevalley']
engine=source['affine'].Affine(ch,1)
O=s.Matrix([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
m0=s.Matrix(glue.OMEGA_F)
meridians=[]
for i in range(4):
    perm=list(range(4));perm[0],perm[i]=perm[i],perm[0]
    meridians.append(s.Matrix([m0[perm[j]] for j in range(4)]))
need(O*O.T==s.eye(3) and O*m0==s.ones(3,1)/2,'explicit isometry, same original glue vector')
spinors=[tuple(s.Rational(x,2) for x in signs) for signs in itertools.product([-1,1],repeat=5) if signs.count(-1)%2==0]
need(len(spinors)==16,'same D5 spinor class as the original generator')
need(ch.kappa_root==-1 and ch.sgn==-1,'original compact adjoint convention')

rows=[];signs=Counter();diagonal=0;family_targets=set()
vacuum={():s.Rational(1)}
for spinor in spinors:
    roots=[]
    for m in meridians:
        # The actual e8_std() current coordinates are doubled standard R8.
        r=tuple(int(2*z) for z in (*spinor,*tuple(O*m)))
        need(r in ch.ridx,'literal original current root, without search or fit')
        roots.append(r)
    for i in range(4):
        for j in range(4):
            ri,rj=roots[i],roots[j]
            ai=ch.ridx[ri]; bj=ch.ridx[tuple(-x for x in rj)]
            # The original compact dagger is E_r^dagger=-E_-r.
            input_state={((-1,bj),):s.Rational(-1)}
            simple=engine.act(ai,0,input_state)
            double=engine.act(ai,1,input_state)
            if i!=j:
                family=tuple(s.Integer(0) for _ in range(5))+tuple(2*O*(meridians[i]-meridians[j]))
                family=tuple(int(z) for z in family)
                need(tuple(x-y for x,y in zip(ri,rj))==family,'common spinor cancels exactly')
                target=ch.ridx[family]
                actual=ch.bracket(ai,bj)
                need(set(actual)=={target} and actual[target] in [-1,1],'original cocycle has one unit target coefficient')
                coefficient=-actual[target]
                need(simple=={((-1,target),):coefficient},'actual affine mode path yields exactly family root')
                need(double=={},'no mixed double pole')
                need(coefficient==-ch.eps(ai,bj),'unchanged actual ordered cocycle')
                family_targets.add(family)
                signs[int(coefficient)]+=1
                rows.append({'spinor_doubled':[int(2*z) for z in spinor],
                             'i':i,'j':j,'left_current_root':ri,
                             'dagger_source_root':tuple(-z for z in rj),
                             'family_target_root':family,
                             'actual_simple_pole_coefficient':int(coefficient)})
            else:
                need(double==vacuum,'original dagger double-pole normalization is exactly +1')
                expected={((-1,index),):value for index,value in ch.hvec_index(ri).items()}
                need(simple==expected,'diagonal simple pole is exactly original Cartan current')
                diagonal+=1

original_family_roots={tuple(x-y for x,y in zip(source['w20'][0,a],source['w20'][0,b]))
                       for a in range(4) for b in range(4) if a!=b}
need(family_targets==original_family_roots,'literal twelve family roots of the original current source')

result={'result':'PASS','constructor':'tfpt_explorer.current_block_geometry._actual_current_source',
        'actual_affine_implementation':'verification/v498_celestial_wp5b_singular_vector.py',
        'original_glue_vector':'verification/v983_simple_current_generator.py:OMEGA_S,OMEGA_F',
        'A3_to_D3_map':[[str(z) for z in row] for row in O.tolist()],
        'spinors':len(spinors),'ordered_mixed_pairs':len(rows),'diagonal_double_poles':diagonal,
        'literal_original_family_root_count':len(family_targets),
        'actual_compact_dagger_simple_pole_sign_counts':dict(signs),
        'fitted_phases':False,'physical_Z_adm_dictionary_derived':False,
        'scope':'Exact local source OPE. Actual affine engine, original root coordinates and actual ordered cocycle. Twist leading OPE transport proved separately; no physical time/measure construction.',
        'rows':rows}
out=Path(__file__).with_name('mixed_meridian_current_results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
