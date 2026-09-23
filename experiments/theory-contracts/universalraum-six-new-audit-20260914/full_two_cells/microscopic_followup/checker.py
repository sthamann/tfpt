"""Matching-exact finite bosonic-edge/CAR-matter wedge singlet block.

No extra coupling matrix: each transition is the canonical inclusion between
images of disjoint Pminus projectors, with the source's sqrt(2)*t coefficient.
"""
from pathlib import Path
from itertools import combinations,product
import sys,json,math,importlib.util
import numpy as np
import sympy as s
from scipy.linalg import eigh
_spec=importlib.util.spec_from_file_location('microscopic_bare_source',Path(__file__).resolve().parents[1]/'checker.py')
_bare=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_bare)
young=_bare.young;transposition=_bare.transposition;graph_operator=_bare.graph_operator
star_projector=_bare.star_projector;EDGES=_bare.EDGES

HERE=Path(__file__).resolve().parent;CHECKS=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    CHECKS.append(label)

def matchings():
    out=[]
    for size in range(len(EDGES)+1):
        for m in combinations(range(len(EDGES)),size):
            occupied=[v for k in m for v in EDGES[k]]
            if len(occupied)==len(set(occupied)):out.append(m)
    return out

def ann(bits,k):
    if not ((bits>>k)&1):return None
    return bits^(1<<k),(-1)**((bits&((1<<k)-1)).bit_count())

def wedge(state,edge,color):
    """b_edge^[a,b] dagger (f_j^b f_i^a-f_j^a f_i^b), a<b."""
    i,j=edge;a,b=color;out={}
    for ci,cj,sign in [(a,b,1),(b,a,-1)]:
        left=ann(state,4*i+ci)
        if left is None:continue
        right=ann(left[0],4*j+cj)
        if right is None:continue
        out[right[0]]=out.get(right[0],0)+sign*left[1]*right[1]
    return {k:v for k,v in out.items() if v}

def apply_map(state_map,edge,color):
    out={}
    for bits,coeff in state_map.items():
        for dst,value in wedge(bits,edge,color).items():out[dst]=out.get(dst,0)+coeff*value
    return {k:v for k,v in out.items() if v}

def car_controls():
    pairB=np.zeros((6,16),dtype=int);colors=list(combinations(range(4),2))
    for a,b in product(range(4),repeat=2):
        bits=(1<<a)+(1<<(4+b))
        for row,ab in enumerate(colors):pairB[row,4*a+b]=wedge(bits,(0,1),ab).get(0,0)
    S=np.zeros((16,16),dtype=int)
    for a,b in product(range(4),repeat=2):S[4*b+a,4*a+b]=1
    need(np.array_equal(pairB.T@pairB,np.eye(16,dtype=int)-S),'exact CAR WdaggerW=2Pminus')
    need(np.array_equal(pairB@pairB.T,2*np.eye(6,dtype=int)),'exact CAR WWdagger=2I6')
    # Interlaced versus separated endpoints; all 4^4 colors, six channels.
    # Spectators are actual CAR modes, so occupancy-dependent signs are retained.
    n=0
    for e,f in [((0,2),(1,3)),((0,1),(2,3)),((0,3),(1,2))]:
        for word in product(range(4),repeat=4):
            bits=sum(1<<(4*v+word[v]) for v in range(4))
            colors_e=tuple(sorted([word[e[0]],word[e[1]]]))
            colors_f=tuple(sorted([word[f[0]],word[f[1]]]))
            if len(set(colors_e))<2 or len(set(colors_f))<2:continue
            ef=apply_map(wedge(bits,e,colors_e),f,colors_f)
            fe=apply_map(wedge(bits,f,colors_f),e,colors_e)
            if ef!=fe:raise RuntimeError('CAR disjoint-pair sign disagreement')
            n+=1
    need(n==432,'432 explicit CAR disjoint-pair order/loop checks')
    # Removing occupied spectator sites can change a single wedge phase.
    full=sum(1<<(4*v) for v in [0,1,3])+(1<<(4*2+1))
    without=full^(1<<4)
    a=wedge(full,(0,2),(0,1));b=wedge(without,(0,2),(0,1))
    need(list(a.values())[0]==-list(b.values())[0],
         'negative: naive pair signs ignore occupied-between-endpoint CAR phase')
    return {'explicit_CAR_comparisons':n,'bosonic_mediators_assumed':True,
      'fermionic_matter_assumed':True,'disjoint_even_wedges_commute':True,
      'naive_fixed_tensor_basis_phase_is_not_assumed':True}

def build():
    ms=matchings();need(len(ms)==25,'25 matchings of the actual seven-edge double star')
    gens=young((2,2,2,2));I=np.eye(14)
    edgeP=[(I-transposition(gens,*e))/2 for e in EDGES]
    basis={};dims={};exactgens=young((2,2,2,2),True);II=s.eye(14)
    exactP=[(II-transposition(exactgens,*e))/2 for e in EDGES]
    for m in ms:
        P=I.copy();Pex=II.copy()
        for k in m:P=P@edgeP[k];Pex=Pex*exactP[k]
        need(Pex*Pex==Pex,'exact matching projector '+str(m))
        vals,U=eigh(P);basis[m]=I.copy() if m==() else U[:,vals>.5];dims[m]=basis[m].shape[1]
        need(dims[m]==int(s.trace(Pex)),'exact image rank matches orthogonal coordinates '+str(m))
    offsets={};start=0
    for m in ms:offsets[m]=slice(start,start+dims[m]);start+=dims[m]
    drift=np.zeros((start,start));coupling=np.zeros_like(drift)
    for m in ms:
        sl=offsets[m];drift[sl,sl]=len(m)*np.eye(dims[m])
        for k in range(7):
            child=tuple(sorted(m+(k,)))
            if k in m or child not in basis:continue
            dst=offsets[child]
            block=math.sqrt(2)*basis[child].T@basis[m]
            coupling[dst,sl]=block;coupling[sl,dst]=block.T
    need(np.linalg.norm(coupling-coupling.T)<1e-12,'canonical microscopic coupling Hermitian')
    need(np.max(abs(coupling[offsets[()],offsets[()]]))==0,'no manually added zero-mediator exchange')
    Hbare=(7*I+graph_operator(gens))/2
    sl=offsets[()];C0=coupling[:,sl]
    need(np.linalg.norm(-.5*C0.T@C0-(Hbare-7*I))<1e-11,
         'exact-structure second-order reduction is Hbare/J minus7I')
    full_dim=sum(6**len(m)*4**(8-2*len(m)) for m in ms)
    records=[];barevals,barevec=eigh(Hbare)
    XstarA=graph_operator(gens,EDGES[:3]);XstarB=graph_operator(gens,EDGES[3:6])
    vacuum=star_projector(XstarA,-3)@star_projector(XstarB,-3)
    _,W=eigh(vacuum);omega=W[:,-1]
    for t in [.0125,.025,.05,.1]:
        H=drift+t*coupling;vals,U=eigh(H);g=U[:,0];J=2*t*t
        matter=basis[()].copy()@g[sl];w=float(matter@matter)
        cond=matter/math.sqrt(w)
        levelweights={str(n):float(sum(np.linalg.norm(g[offsets[m]])**2 for m in ms if len(m)==n))
                      for n in range(4)}
        levels=(vals[:14]/J+7).tolist()
        records.append({'t_over_Delta':t,'J_over_Delta':J,'microscopic_singlet_dimension':start,
           'ground_energy_over_Delta':float(vals[0]),'ground_after_plus7J_and_divide_J':float(vals[0]/J+7),
           'ground_deviation_from_leading_bare_over_J':float(vals[0]/J+7-barevals[0]),
           'first_singlet_energy_over_Delta':float(vals[1]),
           'first_singlet_gap_over_J':float((vals[1]-vals[0])/J),
           'first14_rescaled_eigenvalues':levels,
           'first14_difference_from_bare':((vals[:14]/J+7)-barevals).tolist(),
           'ground_mediator_number_weights':levelweights,'zero_mediator_weight':w,
           'conditional_matter_overlap_squared_with_bare_ground':float(abs(cond@barevec[:,0])**2),
           'conditional_matter_overlap_squared_with_omega_omega':float(abs(cond@omega)**2),
           'unconditional_overlap_squared_with_omega_omega_zero_mediators':float(abs(matter@omega)**2),
           'ground_residual_norm':float(np.linalg.norm(H@g-vals[0]*g))})
        need(abs(sum(levelweights.values())-1)<1e-12,'mediator distribution normalized '+str(t))
        need(np.linalg.norm(H@g-vals[0]*g)<1e-12,'numerical microscopic ground residual '+str(t))
    target=records[2]
    need(target['ground_deviation_from_leading_bare_over_J']>0,
         'finite Delta raises ground relative to leading effective source result')
    need(records[0]['ground_deviation_from_leading_bare_over_J']<records[1]['ground_deviation_from_leading_bare_over_J']<records[2]['ground_deviation_from_leading_bare_over_J'],
         't toward0 removes leading-order error')
    # Negative control: deleting m>=2 branches is not the matching-complete source.
    ids=np.concatenate([np.arange(offsets[m].start,offsets[m].stop) for m in ms if len(m)<=1])
    H=.05*coupling+drift;trunc=eigh(H[np.ix_(ids,ids)],eigvals_only=True)[0]
    need(abs(trunc-target['ground_energy_over_Delta'])>1e-5,
         'negative: omitting allowed two/three mediators changes the microscopic ground')
    out={'status':'NUMERICAL_COMPLETE_MICROSCOPIC_SU4_SINGLET_ONLY',
      'edges':EDGES,'matching_count':len(ms),'matching_sizes_counts':{str(n):sum(len(m)==n for m in ms) for n in range(4)},
      'full_physical_matching_dimension_not_diagonalized':full_dim,
      'singlet_dimension':start,'singlet_dimensions_per_matching':[{'matching':m,'dimension':dims[m]} for m in ms],
      'bare_first_singlet_gap_over_J':float(barevals[1]-barevals[0]),
      'matching_complete':True,'all_SU4_sectors_diagonalized':False,'global_ground_or_gap_certified':False,
      'interval_certificate':False,'arbitrary_new_vertex_added':False,'new_hard_core_postulate_added':False,
      'hard_core_origin':'Qv=1 plus nonnegative additive fermion/boson occupations in the specified Fock contract',
      'source_assumptions':['CAR matter modes','bosonic edge-local six-channel mediator modes',
        'linear wedge vertex with identical t','drift Delta times mediator number','local Qv=1',
        'no extra direct mediator hopping or interactions'],
      'records':records,'at_t_over_Delta_005':target,
      'negative_truncated_one_mediator_ground_over_Delta':float(trunc),
      'CAR_controls':car_controls(),'checks':CHECKS,'count':len(CHECKS)}
    (HERE/'verification.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    np.savez_compressed(HERE/'singlet_matching_matrices.npz',drift=drift,coupling=coupling)
    print(json.dumps({k:v for k,v in out.items() if k not in ['records','checks','singlet_dimensions_per_matching']},indent=2))

if __name__=='__main__':build()
