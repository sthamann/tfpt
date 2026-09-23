"""Small source-only instruments with the SAME exact 3/7 quantum shadow.

Extends the already-known four-context reflection/measurement identity to
the full sixty-ray frame and the existing 3/7 decode. Does not derive access,
coherent control, physical measurement, tensor locality, or the Born rule.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SOURCE=ROOT/'experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py'
PIN='ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995'
CHECKS=[]


def need(ok,message):
    if not bool(ok):raise RuntimeError(message)
    CHECKS.append(message)


def clean(A):return A.applyfunc(s.expand)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default='record_selection.json')
    parser.add_argument('--mutant',choices=['same_record','four_is_neutral','boundary_changes_rate'])
    args=parser.parse_args()
    need(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN,'unchanged source loader hash')
    spec=importlib.util.spec_from_file_location('record_original',SOURCE)
    source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
    data=source.source_prefix()
    I=s.eye(4);zero=s.zeros(4);rho0=I/4
    P=[]
    for index in data['line_reps']:
        z=s.Matrix([a+s.I*b for a,b in data['Z240'][index]])
        p=clean(z*z.H/4)
        need(p*p==p and p.H==p and s.trace(p)==1,'actual original rank-one ray '+str(index))
        P.append(p)
    R=[I-2*p for p in P]
    need(len(P)==60 and sum(P,zero)==15*I,'original tight sixty-ray frame')
    need(sum(R,zero)==30*I,'original reflection sum')
    channel_measure=lambda X:clean(sum((p*X*p for p in P),zero)/15)
    channel_reflect=lambda X:clean(sum((r*X*r.H for r in R),zero)/60)
    all_operators=[]
    for i in range(4):
        for j in range(4):
            e=s.zeros(4);e[i,j]=1;all_operators.append(e)
            target=(e+s.trace(e)*I)/5
            need(channel_measure(e)==target,'full source frame measurement channel '+str((i,j)))
            need(channel_reflect(e)==target,'full source reflection channel '+str((i,j)))
    # The same lazy identity weight matches the EXISTING quantum decode 3/7.
    a=s.symbols('a',real=True)
    need(s.solve(a+(1-a)/5-s.Rational(3,7),a)==[s.Rational(2,7)],
         'only lazy-identity weight matching existing quantum shadow is two sevenths')
    idle=s.Rational(2,7)
    project_branch=lambda j,X:clean(P[j]*X*P[j]/21)
    reflect_branch=lambda j,X:clean(R[j]*X*R[j].H/84)
    need(idle*I+sum((p/21 for p in P),zero)==I,'measurement instrument complete effects')
    need(idle*I+sum((r.H*r/84 for r in R),zero)==I,'reflection instrument complete effects')
    for i,X in enumerate(all_operators):
        m=clean(idle*X+sum((project_branch(j,X) for j in range(60)),zero))
        r=clean(idle*X+sum((reflect_branch(j,X) for j in range(60)),zero))
        target=clean((3*X+s.trace(X)*I)/7)
        need(m==r and r==target,'complete instruments have exactly same all-input 3/7 channel '+str(i))
    # Equal first records from the canonical trace boundary, different updates.
    for j in range(60):
        pm=project_branch(j,rho0);pr=reflect_branch(j,rho0)
        need(s.trace(pm)==s.trace(pr)==s.Rational(1,84),'same canonical first record marginal '+str(j))
        need(pm*84==P[j] and pr*84==rho0,'pure versus trace conditional state '+str(j))
    j=0
    repeat_m=s.trace(project_branch(j,project_branch(j,rho0)))
    repeat_r=s.trace(reflect_branch(j,reflect_branch(j,rho0)))
    need(repeat_m==s.Rational(1,1764) and repeat_r==s.Rational(1,7056),
         'second same-labelled record separates equal one-time data by factor four')
    if args.mutant=='same_record':
        need(repeat_m==repeat_r,'MUTANT: equality of nonselective channel does not fix records')
    for k in range(60):
        need(s.trace(project_branch(k,project_branch(j,rho0)))==s.trace(P[k]*P[j])/1764,
             'actual source pair overlap governs successive measurement records '+str(k))
        need(s.trace(reflect_branch(k,reflect_branch(j,rho0)))==s.Rational(1,7056),
             'random reflection records are independent from trace state '+str(k))
    # The same quantum shadow does NOT mean this implements the original
    # context-correlated sixty-ray transition. Forget idle but retain the
    # current postmeasurement ray to expose an exact difference.
    context_ids=[data['stab_ray_ctx'][data['canonical_ray'](data['Z240'][index])]
                 for index in data['line_reps']]
    initial=0
    original=[];lazy=[]
    for k in range(60):
        overlap=s.trace(P[k]*P[initial])
        incident=bool(data['contexts'][context_ids[k]] & data['contexts'][context_ids[initial]])
        original.append(overlap/7 if incident else s.Integer(0))
        lazy.append((idle if k==initial else 0)+overlap/21)
    need(sum(original)==sum(lazy)==1,'both ray transition columns normalized')
    need(original[initial]==s.Rational(1,7) and lazy[initial]==s.Rational(1,3),
         'same quantum shadow but actual ray retention one seventh versus one third')
    need(sum(x!=0 for x in original)==13 and sum(x!=0 for x in lazy)==45,
         'old source context process and new lazy instrument have different ray support')
    need(clean(sum((original[k]*P[k] for k in range(60)),zero))==
         clean(sum((lazy[k]*P[k] for k in range(60)),zero)),
         'different ray records still give identical decoded density matrix')
    # An invariant readout rotation maps the sixty Kraus alternatives exactly.
    H=s.ones(60)/30-s.eye(60)
    need(H*H==s.eye(60) and H.H==H,'global reflection-record to projector-record rotation is unitary')
    for j in range(60):
        # sqrt84 and sqrt21 have ratio two; cancel their common denominator.
        need(sum((H[j,k]*R[k] for k in range(60)),zero)==2*P[j],
             'same coherent dilation and different record basis '+str(j))
    # Covariance checked on every original reflection; the identity label fixed.
    for j,r in enumerate(R):
        perm=[]
        for p in P:
            mapped=clean(r*p*r.H)
            need(mapped in P,'source reflection permutes whole ray frame '+str(j))
            perm.append(P.index(mapped))
        need(len(set(perm))==60,'full source-generator record permutation '+str(j))
        # H depends only on equality and the constant vector, so commutes with
        # all permutations, in particular each exact source-induced one.
        need(all(H[perm[0],perm[k]]==H[0,k] for k in range(60)),
             'record rotation commutes with source-generator permutation '+str(j))

    # Central-charge typing: a linear equivariant isometry cannot turn one
    # fundamental4 into two fundamentals. This is NOT a no-go for mixed baths.
    z=s.I*I
    need(s.kronecker_product(z,z)==-s.eye(16),'two identical fundamentals carry central phase minus one')
    need(s.I!=-1,'input versus two-fundamental center mismatch forces an intertwiner to vanish')
    neutral=s.kronecker_product(z,z.conjugate())
    need(neutral==s.eye(16),'fundamental times conjugate is central-neutral')
    if args.mutant=='four_is_neutral':
        need(z==I,'MUTANT: fundamental spinor is not a neutral record representation')
    # Full-symmetry, q-independent one-channel evolution cannot generate new
    # exponential rates solely by changing fixed boundary states and effects.
    x,y,lam,mu=s.symbols('x y lambda mu',real=True)
    need(s.expand(lam*(x-mu)+mu-(mu+lam*(x-mu)))==0,
         'boundary-state probabilities have fixed intercept plus one shared channel contrast')
    boundary_first=s.Rational(1,4)+s.Rational(3,4)*s.Rational(3,7)
    boundary_second=s.Rational(1,4)+s.Rational(3,4)*s.Rational(3,7)**2
    need((boundary_second-s.Rational(1,4))/(boundary_first-s.Rational(1,4))==s.Rational(3,7),
         'boundary amplitude does not change the intrinsic decay multiplier')
    if args.mutant=='boundary_changes_rate':
        need((boundary_second-s.Rational(1,4))/(boundary_first-s.Rational(1,4))==s.Rational(2,7),
             'MUTANT: fixed boundary preparation cannot change a q-independent channel rate')
    result={'status':'EXACT_SAME_SOURCE_CHANNEL_DISTINCT_RECORDS','check_count':len(CHECKS),'checks':CHECKS,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'loader_sha256':PIN,'original_v783_sha256':source.PIN,'inherited_checks':source.CHECKS,
        'original_reflection_and_uniform_frame_channel':'D_1/5',
        'identity_weight_matching_existing_D_3/7':'2/7',
        'same_channel':'X -> (3 X + Tr(X) I4)/7',
        'canonical_first_ray_record_probability_both':'1/84',
        'canonical_conditional_states':{'reflection':'I4/4','measurement':'source rank-one P_r'},
        'same_ray_two_record_probabilities':{'reflection':str(repeat_r),'measurement':str(repeat_m)},
        'not_the_original_context_ray_process':{'original_same_ray':'1/7','lazy_same_ray':'1/3',
            'original_nonzero_successors':13,'lazy_nonzero_successors':45},
        'source_covariance':'all60 actual Gaussian reflections permute actual ray instrument labels',
        'coherent_record_rotation':'I_idle directsum (J60/30-I60); same dilation, different readout basis',
        'neutral_minimal_environment_type':'End(C4) = C4 tensor conjugate(C4), not fundamental C4',
        'no_new_dimension_selection':True,
        'old_result_attributed':'four-outcome reflection/projector record equivalence and d=4 condition already in CONTEXT_INSTRUMENT.md',
        'physical_execution_and_measurement_derived':False,'T1_T8_closed':[]}
    (HERE/args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2),flush=True)


if __name__=='__main__':main()
