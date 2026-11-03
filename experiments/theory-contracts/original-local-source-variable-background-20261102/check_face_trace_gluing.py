from pathlib import Path
import json
import numpy as np
from scipy.special import expit
# Reuse exactly the original v252 constructor and variable H coefficients from D.
p=Path('work/source_continuation/check_variable_background.py')
s=p.read_text().split('rows=[]')[0]
ns0={'__name__':'native_prefix'}
exec(compile(s,str(p),'exec'),ns0)
g=ns0['g']; mult=ns0['mult']; potential=ns0['potential']
checks={};rows=[]
def need(k,v):
 checks[k]=bool(v)
 if not v:raise RuntimeError(k)
for alpha in [.25,.75]:
 ns=np.arange(-2,2)
 h=np.kron(np.diag(ns+alpha),g)+mult(potential,ns)
 e,U=np.linalg.eigh(h)
 beta=.3
 a=expit(beta*e); c=expit(-beta*e)
 x=1/(2*np.cosh(beta*e/2))
 G=np.block([[np.diag(a),np.diag(x)],[np.diag(x),np.diag(c)]])
 need(f'actual_two_face_graph_is_projection_{alpha}',np.linalg.norm(G@G-G)<1e-12)
 need(f'faces_are_complementary_{alpha}',np.max(abs(a+c-1))<1e-14)
 need(f'first_face_modular_sign_is_minus_{alpha}',np.max(abs(np.log1p(-a)-np.log(a)+beta*e))<1e-10)
 need(f'second_face_modular_sign_is_plus_{alpha}',np.max(abs(np.log1p(-c)-np.log(c)-beta*e))<1e-10)
 # K=partial_r+h AP Green: jump+1 and AP sewing determine S(0+)=a.
 sp=a;sm=-c
 need(f'AP_Green_jump_{alpha}',np.max(abs(sp-sm-1))<1e-14)
 need(f'AP_Green_sewing_{alpha}',np.max(abs(-np.exp(-beta*e)*sp-sm))<1e-10)
 # Actual spectral channels, checked independently by a four-state Fock trace.
 ee=e[[0,-1]]
 probs=np.array([1,np.exp(-beta*ee[0]),np.exp(-beta*ee[1]),np.exp(-beta*sum(ee))])
 Z=float(sum(probs));probs/=Z
 occ=np.array([probs[1]+probs[3],probs[2]+probs[3]])
 need(f'charged_Fock_occupation_is_second_face_{alpha}',np.max(abs(occ-expit(-beta*ee)))<1e-13)
 need(f'Fock_trace_normalizer_{alpha}',abs(np.log(Z)-sum(np.logaddexp(0,-beta*ee)))<1e-13)
 # Exact source-function type comparison, no assumption about source operator equality.
 d=beta*e
 heat=float(sum(np.exp(-d)));logZ=float(sum(np.logaddexp(0,-d)))
 need(f'v259_heat_trace_is_not_Fock_log_partition_{alpha}',abs(heat-logZ)>1)
 rows.append({'alpha':alpha,'one_particle_dimension':len(e),'beta_test':beta,'spectrum_extrema':[float(min(e)),float(max(e))], 'modular_heat_trace':heat,'Fock_log_partition':logZ,'face_sum':float(sum(a)),'opposite_face_sum':float(sum(c))})
result={'all_passed':all(checks.values()),'checks':checks,'rows':rows,'scope':'Actual original v252 seed252 variableH Fourier data from D; finite algebra/face ordering controls only. No original full source equality, thermal boundary selection, H law or absolute determinant phase asserted.'}
Path(__file__).with_name('face-trace-gluing-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
