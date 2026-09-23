"""All15 SU4 types of the same matching-exact microscopic double star.

Numerical spectra only; exact ranks and Schur-Weyl dimension accounting.
"""
from pathlib import Path
import sys,json,time,math
import numpy as np
import sympy as s
from scipy.linalg import eigh
from checker import matchings,EDGES
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import importlib.util
spec=importlib.util.spec_from_file_location('bare_checker',Path(__file__).resolve().parents[1]/'checker.py')
bare=importlib.util.module_from_spec(spec);spec.loader.exec_module(bare)

HERE=Path(__file__).resolve().parent

def main():
    tic=time.time();ms=matchings();rows=[];weighted=0;levels=[];checks=[]
    for shape in bare.partitions(8):
        gens=bare.young(shape);d=gens[0].shape[0];I=np.eye(d)
        exactgens=bare.young(shape,True);II=s.eye(d)
        ep=[(I-bare.transposition(gens,*e))/2 for e in EDGES]
        epex=[(II-bare.transposition(exactgens,*e))/2 for e in EDGES]
        U={};dims={};offsets={};total=0
        for m in ms:
            P=I.copy();Pe=II.copy()
            for edge in m:P=P@ep[edge];Pe=Pe*epex[edge]
            ev,v=eigh(P);rank=int(s.trace(Pe));dim=int(sum(ev>.5))
            if rank!=dim or Pe*Pe!=Pe:raise RuntimeError('projector/rank '+str((shape,m)))
            U[m]=I.copy() if not m else v[:,ev>.5];dims[m]=dim
            offsets[m]=slice(total,total+dim);total+=dim
        H=np.zeros((total,total));drift=np.zeros(total)
        for m in ms:
            a=offsets[m];drift[a]=len(m)
            for edge in range(7):
                child=tuple(sorted(m+(edge,)))
                if edge in m or child not in U:continue
                b=offsets[child];block=math.sqrt(2)*.05*U[child].T@U[m]
                H[b,a]=block;H[a,b]=block.T
        H+=np.diag(drift)
        ev,vec=eigh(H,subset_by_index=[0,min(1,total-1)])
        residual=float(np.linalg.norm(H@vec-vec*ev))
        if residual>1e-11:raise RuntimeError('numerical residual '+str(shape))
        mult=bare.su4dim(shape);weighted+=total*mult
        for value in ev:levels.append((float(value),shape,mult))
        row={'shape':shape,'matter_Specht_dimension':d,'matching_Specht_dimension':total,
          'SU4_dimension':mult,'lowest_two_energies_over_Delta':ev.tolist(),
          'lowest_two_energies_plus7J_over_J':(ev/.005+7).tolist(),
          'eigenvector_residual_norm':residual,'ground_zero_mediator_weight':float(np.linalg.norm(vec[offsets[()],0])**2)}
        rows.append(row);checks.append('exact projector ranks and numeric lowest two '+str(shape))
        print('SECTOR',shape,total,ev.tolist(),round(time.time()-tic,2),flush=True)
    if weighted!=371200:raise RuntimeError('incomplete physical dimension')
    checks.append('exact complete microscopic Schur-Weyl dimension371200')
    levels.sort(key=lambda z:z[0]);E0=levels[0][0];E1=next(e for e,_,_ in levels if e>E0+1e-10)
    groundmult=sum(m for e,_,m in levels if abs(e-E0)<1e-10)
    firstmult=sum(m for e,_,m in levels if abs(e-E1)<1e-10)
    out={'status':'NUMERICAL_ALL_MICROSCOPIC_SU4_SECTORS_NO_INTERVAL_CERTIFICATE',
      't_over_Delta':.05,'J_over_Delta':.005,'edge_count':7,'matching_count':len(ms),
      'full_physical_dimension':weighted,'largest_matching_Specht_dimension':max(r['matching_Specht_dimension'] for r in rows),
      'numerical_global_ground_energy_over_Delta':E0,'numerical_global_first_energy_over_Delta':E1,
      'numerical_global_ground_plus7J_over_J':E0/.005+7,
      'numerical_global_first_plus7J_over_J':E1/.005+7,
      'numerical_global_gap_over_J':(E1-E0)/.005,
      'numerical_ground_degeneracy':groundmult,'numerical_first_degeneracy':firstmult,
      'ground_shapes':[sh for e,sh,m in levels if abs(e-E0)<1e-10],
      'first_shapes':[sh for e,sh,m in levels if abs(e-E1)<1e-10],
      'exact_global_order_certified':False,'interval_certificate':False,'new_vertex_or_fit_added':False,
      'sectors':rows,'checks':checks,'count':len(checks),'elapsed_seconds':time.time()-tic}
    (HERE/'all_sectors.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['sectors','checks']},indent=2))

if __name__=='__main__':main()
