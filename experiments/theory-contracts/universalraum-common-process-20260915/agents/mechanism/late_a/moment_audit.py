"""Small CAR-sum-rule audit of the three different Ritz states; no large replay."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import numpy as np

HERE=Path(__file__).resolve().parent


def main():
 manifest=json.loads((HERE/'inputs_manifest.json').read_text())
 for name in ['native_ground_state.json','norms_by_traces.json']:
  if sha256((HERE/'inputs'/name).read_bytes()).hexdigest()!=manifest[name]['sha256']:
   raise RuntimeError('input pin '+name)
 ground=json.loads((HERE/'inputs/native_ground_state.json').read_text())
 nu=json.loads((HERE/'inputs/norms_by_traces.json').read_text())['nu']
 norms=[1]+[int(nu[str(j)]) for j in range(1,6)]
 result={}
 for label,n,w in [('five',4,True),('six',6,False),('seven',6,True)]:
  H=np.diag(np.array(list(range(n))+([2] if w else []),dtype=float))
  for j in range(n-1):H[j,j+1]=H[j+1,j]=np.sqrt(norms[j+1]/norms[j])/20
  if w:H[3,n]=H[n,3]=np.sqrt((5001523200/229)/norms[3])/20
  e,v=np.linalg.eigh(H);z=v[:,0]
  nb=np.array(list(range(n))+([2] if w else []))
  Tplus=np.where(nb[:,None]==nb[None,:]+1,20*H,0)
  b=float(z@(nb*z));b2=float(z@(nb**2*z))
  nr=64*b-2*b2+.1*z@Tplus@((62-2*nb)*z)
  na=2*b2+.1*z@Tplus@(2*nb*z)
  rem=float(nr/(64-2*b)-e[0]);add=float(na/(2*b)-e[0])
  result[label]={'basis_dimension':len(nb),'E_Ritz':float(e[0]),'Nb':b,
                 'removal_total_weight':1-b/32,'addition_total_weight':b/32,
                 'removal_first_moment_cost':rem,'addition_first_moment_cost':add}
 ref=ground['charged_response']['eps']['0']
 if abs(result['five']['removal_first_moment_cost']-ref['eps_h'])>1e-12:
  raise RuntimeError('small-state removal sum rule')
 if abs(result['five']['addition_first_moment_cost']-ref['eps_add'])>1e-12:
  raise RuntimeError('small-state addition sum rule')
 return {'status':'PASS','source_pin_checks':2,'numerical_comparison_checks':2,
         'Ritz_states':result,'Delta':1,'g':'1/20',
         'exact_general_identities':{
          'sum_r_fdag_H_f':'Delta*(64*<Nb>-2*<Nb^2>)+2*g*Re<Tplus*(62-2*Nb)>',
          'sum_r_f_H_fdag':'2*Delta*<Nb^2>+2*g*Re<Tplus*(2*Nb)>'},
         'assumptions':['G-singlet normalized state','physical N=64','native H contract'],
         'true_ground_state_observables_claimed':False,'spectral_line_energies_claimed':False}


if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
 encoded=json.dumps(main(),indent=2,sort_keys=True)+'\n'
 if args.output:args.output.write_text(encoded)
 print(encoded,end='')
