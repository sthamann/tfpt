"""Fresh exact nu5 trace replay plus independent rational Ritz certification.

Only frozen files are read. No full many-body ground-state run is performed.
The original sparse Python-integer contraction is freshly executed; the Ritz
polynomials, bounds, and cross-basis corrections are reconstructed separately.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import argparse
import importlib.util
import json
import sys
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
CHECKS=[]


def need(ok,name):
 if not bool(ok):raise RuntimeError(name)
 CHECKS.append(name)


def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path)
 obj=importlib.util.module_from_spec(spec)
 sys.modules[name]=obj
 spec.loader.exec_module(obj)
 return obj


def exact_matrix(norms,extra=None):
 """Diagonal similarity to the symmetric compression; rational tree entries."""
 n=len(norms)
 M=s.diag(*range(n),*([2] if extra is not None else []))
 for j in range(n-1):
  M[j,j+1]=s.Rational(norms[j+1],norms[j])/400
  M[j+1,j]=1
 if extra is not None:
  M[3,n]=s.Rational(extra)/norms[3]/400
  M[n,3]=1
 return M


def numeric_matrix(norms,extra=None):
 n=len(norms)
 M=np.diag(np.array(list(range(n))+([2] if extra is not None else []),dtype=float))
 for j in range(n-1):M[j,j+1]=M[j+1,j]=np.sqrt(norms[j+1]/norms[j])/20
 if extra is not None:M[3,n]=M[n,3]=np.sqrt(float(extra)/norms[3])/20
 return M


def main():
 manifest=json.loads((HERE/'inputs_manifest.json').read_text())
 for name,rec in manifest.items():
  data=(HERE/'inputs'/name).read_bytes()
  need(sha256(data).hexdigest()==rec['sha256'] and len(data)==rec['bytes'],'source pin '+name)
 need(manifest['spinor_tensors.npz']['sha256']=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','original W pin retained')
 recorded=json.loads((HERE/'inputs/norms_by_traces.json').read_text())
 ground=json.loads((HERE/'inputs/native_ground_state.json').read_text())
 need(recorded['checker_sha256']==manifest['norms_by_traces.py']['sha256'],'current trace output matches frozen checker')
 need(recorded['common_sha256']==manifest['common.py']['sha256'],'current trace output matches frozen common source')
 need(ground['checker_sha256']==manifest['native_ground_state.py']['sha256'],'current ground report matches frozen checker')
 need(ground['common_sha256']==manifest['common.py']['sha256'],'current ground report matches frozen common source')
 normal=(HERE/'inputs/norms_normal.json').read_bytes()
 optimized=(HERE/'inputs/norms_optimized.json').read_bytes()
 need(normal==optimized,'upstream normal and optimized trace outputs are byte-identical')
 need(json.loads(normal)==recorded,'upstream output and saved JSON have identical content despite trailing-newline difference')
 global_replay=json.loads((HERE/'inputs/replay_manifest.json').read_text())
 need(global_replay['status']=='RUNNING','source whole-suite replay still records RUNNING at freeze')

 common=module('common',HERE/'inputs/common.py')
 common.TENSOR_PATH=HERE/'inputs/spinor_tensors.npz'
 trace=module('late_a_frozen_trace',HERE/'inputs/norms_by_traces.py')
 M,W=trace.load_model()
 norms=[1];network_counts={};canonical_counts={}
 for n in range(1,6):
  nu,networks,canonical=trace.compute_nu(n,M)
  need(nu==int(recorded['nu'][str(n)]),'fresh exact sparse source contraction nu'+str(n))
  norms.append(nu);network_counts[str(n)]=networks;canonical_counts[str(n)]=canonical
 need(norms==[1,480,439680,575078400,952296652800,1866738327552000],'all five fresh norms match the explicit sequence')
 need(network_counts==recorded['n_networks'] and canonical_counts==recorded['n_canonical'],'network and canonical counts match the source certificate')
 need((network_counts['5'],canonical_counts['5'])==(840,93),'nu5 uses 840 Wick networks in 93 sign-free graph classes')
 need(trace.STATS=={'fast':0,'crt':0},'fresh norm certificate uses sparse Python integers only, no floating network arithmetic')

 # Independent exact construction of the actual variational compressions.
 w2=s.Rational(5001523200,229)
 reports={}
 for label,extra,left,right in [
   ('pure_six',None,s.Rational(-113847420,100000000),s.Rational(-113847419,100000000)),
   ('seven_with_w2',w2,s.Rational(-113847610,100000000),s.Rational(-113847609,100000000))]:
  matrix=exact_matrix(norms,extra)
  poly=matrix.charpoly().as_poly()
  need(poly.count_roots(-s.oo,left)==0,label+' has no root below lower endpoint')
  need(poly.count_roots(left,right)==1,label+' has exactly one root in rational interval')
  need(poly.count_roots(-s.oo,s.oo)==matrix.rows,label+' has a full real simple spectrum')
  energies,vectors=np.linalg.eigh(numeric_matrix(norms,extra))
  vec=vectors[:,0];occupancies=np.array(list(range(6))+([2] if extra is not None else []))
  nb=float(np.sum(vec*vec*occupancies))
  probs=[float(np.sum(vec[occupancies==k]**2)) for k in range(6)]
  entropy=float(-sum(p*np.log2(p) for p in probs if p))
  addition=nb/32;removal=1-addition
  ref=ground['observables']['no_w2' if extra is None else 'with_w2']
  need(abs(energies[0]-ref['E_numerical'])<1e-12,label+' numerical Ritz energy matches recorded value')
  need(abs(nb-ref['Nb'])<1e-12,label+' Ritz boson expectation matches recorded value')
  need(abs(entropy-ref['entropy_bits'])<1e-12,label+' boson-number Shannon entropy matches recorded value')
  reports[label]={
   'basis_size':matrix.rows,'polynomial_coefficients':[str(x) for x in poly.all_coeffs()],
   'strict_lower':str(left),'strict_upper':str(right),
   'strict_removal_floor_with_retained_Eh':str(s.Rational(-1121899,1000000)-right),
   'numerical_E':float(energies[0]),'numerical_Nb':nb,'numerical_overlap_F_squared':float(vec[0]**2),
   'numerical_Shannon_boson_number_entropy_bits':entropy,
   'same_Ritz_state_total_addition_weight':addition,'same_Ritz_state_total_removal_weight':removal,
   'full_H_Lanczos_matrix':False,'invariant_subspace_claimed':False,
  }

 # Replay the smaller response-state matrix without constructing its millions
 # of amplitudes. Its weights are fixed by symmetry and the number expectation.
 ee,vv=np.linalg.eigh(numeric_matrix(norms[:4],w2))
 small_nb=float(np.sum(vv[:,0]**2*np.array([0,1,2,3,2])))
 charged=ground['charged_response']
 need(charged['basis']=='v0..v3 + w2' and charged['ritz_size']==5,'reported charged response explicitly uses the older five-state Ritz basis')
 need(abs(ee[0]-charged['E_K'])<1e-12 and abs(small_nb-charged['Nb'])<1e-12,'independent smaller matrix matches charged-response reference energy and boson count')
 need(abs(charged['Z']['0']['Z_add']-small_nb/32)<1e-12,'quoted addition weight belongs to the smaller Ritz state')
 need(abs(charged['Z']['0']['Z_h']-(1-small_nb/32))<1e-12,'quoted removal weight belongs to the smaller Ritz state')
 need(abs(reports['seven_with_w2']['numerical_Nb']-small_nb)>0.17,'larger and charged-response Ritz states have demonstrably different composition')
 retained_true_nb_floor=s.Rational(842846,1000000)
 need(s.Rational(str(charged['Z']['0']['Z_add']))<retained_true_nb_floor/32,
      'quoted approximate addition weight even lies below retained exact true-ground lower bound')

 return {
  'status':'PASS','exact_or_numeric_checks':len(CHECKS),'checks':CHECKS,
  'input_pins':{name:rec['sha256'] for name,rec in manifest.items()},
  'source_full_replay_status_at_freeze':global_replay['status'],
  'fresh_trace_norms':norms,'nu5_freshly_replayed':True,
  'trace_algorithm':'unchanged frozen sparse Python-integer source algorithm, freshly executed',
  'trace_guards_executed':len(trace.GUARDS),'nu5_networks':840,'nu5_canonical_networks':93,
  'independent_new_trace_method':False,
  'certified_Ritz_compressions':reports,
  'charged_response_approximation':{
    'basis':charged['basis'],'reference_energy':charged['E_K'],'Nb':small_nb,
    'total_addition_weight':charged['Z']['0']['Z_add'],
    'total_removal_weight':charged['Z']['0']['Z_h'],
    'recorded_first_moment_removal_cost':charged['eps']['0']['eps_h'],
    'recorded_first_moment_addition_cost':charged['eps']['0']['eps_add'],
    'first_moments_freshly_recomputed':False,'native_ground_observables':False},
  'scope':{'full_native_ground_archive_rerun':False,'ground_selection_theorem_refuted':False,
           'full_lanczos_sixth_vector_derived':False,'Ritz_convergence_proved':False,
           'new_nu5_two_independent_methods_claimed':False,
           'removal_energy_floor_uses_retained_exact_N63_input':True},
 }


if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
 result=main();encoded=json.dumps(result,indent=2,sort_keys=True)+'\n'
 if args.output:args.output.write_text(encoded)
 print(json.dumps({'status':result['status'],'checks':result['exact_or_numeric_checks'],
                   'nu5':result['fresh_trace_norms'][-1],'result_sha256':sha256(encoded.encode()).hexdigest()},sort_keys=True))
