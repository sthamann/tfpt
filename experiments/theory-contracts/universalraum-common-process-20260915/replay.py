"""Portable independent replay, fixed inputs, warnings as errors, normal and -OO."""
from pathlib import Path
from hashlib import sha256
import concurrent.futures
import json
import os
import subprocess
import sys

HERE=Path(__file__).resolve().parent
SCRIPTS={
 'mechanism':'agents/mechanism/verify.py',
 'shadows':'agents/shadows/verify.py',
 'causal':'agents/causal/verify_causal.py',
 'phase_bridge':'verify_phase_bridge.py',
 'resource_boundary':'verify_resource_boundary.py',
 'late_field':'agents/shadows/verify_late_field.py',
 'late_norm':'agents/mechanism/late_a/verify.py',
 'late_moments':'agents/mechanism/late_a/moment_audit.py',
}

def digest(p):return sha256(p.read_bytes()).hexdigest()

def one(item):
 name,path=item;raw=[];out=HERE/'replay_outputs';out.mkdir(exist_ok=True)
 env=dict(os.environ);env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1'
 for mode,flags in [('normal',[]),('optimized',['-OO'])]:
  target=out/(name+'_'+mode+'.json')
  extra=['--output',str(target)] if name=='late_norm' else []
  proc=subprocess.run([sys.executable,'-B','-W','error',*flags,str(HERE/path),*extra],
      capture_output=True,cwd=HERE,env=env,timeout=300)
  if proc.returncode or proc.stderr:
   raise RuntimeError(name+' '+mode+' failed: '+proc.stderr.decode(errors='replace'))
  encoded=target.read_bytes() if name=='late_norm' else proc.stdout
  result=json.loads(encoded)
  if result.get('status')!='PASS':raise RuntimeError(name+' no PASS')
  raw.append(encoded);target.write_bytes(encoded)
 if raw[0]!=raw[1]:raise RuntimeError(name+' optimization mismatch')
 result=json.loads(raw[0])
 exact=result.get('exact_checks',result.get('exact_conditions',0))
 numeric=result.get('numerical_checks',result.get('numeric_checks',0))
 if name=='late_norm':
  if result['exact_or_numeric_checks']!=46 or result['trace_guards_executed']!=1239:
   raise RuntimeError('Changed late-norm check contract')
  exact,numeric=36,10 # Individually classified in LATE_A_AUDIT.md; not 46 exact claims.
 if name=='late_moments':
  exact=result['source_pin_checks'];numeric=result['numerical_comparison_checks']
 return name,{'script':path,'checker_sha256':digest(HERE/path),'result_sha256':sha256(raw[0]).hexdigest(),
     'exact_checks':exact,'numerical_checks':numeric,
     'normal_optimized_byte_identical':True}

def main():
 pins=json.loads((HERE/'sources_manifest.json').read_text())
 for name,rec in pins.items():
  if digest(HERE/'sources'/name)!=rec['sha256']:raise RuntimeError('Changed source '+name)
 scripts=dict(SCRIPTS)
 if (HERE/'agents/causal/verify_common3.py').exists():scripts['common3']='agents/causal/verify_common3.py'
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
  reports=dict(ex.map(one,scripts.items()))
 audit=subprocess.run([sys.executable,'-B','-W','error',str(HERE/'audit_synthesis.py')],
    capture_output=True,cwd=HERE,timeout=300)
 if audit.returncode or audit.stderr:raise RuntimeError('Synthesis audit failed: '+audit.stderr.decode())
 inherited=json.loads(audit.stdout)
 (HERE/'synthesis_audit.json').write_bytes(audit.stdout)
 record={'status':'PASS','reports':reports,
    'own_exact_checks_per_variant':sum(r['exact_checks'] for r in reports.values()),
    'own_numerical_checks_per_variant':sum(r['numerical_checks'] for r in reports.values()),
    'mechanism_additional_retained_native_constructor_guards':17,
    'late_norm_additional_retained_trace_source_guards':1239,
    'exact_check_count_includes_factual_source_pin_checks':True,
    'supplied_synthesis_checks_per_variant':57,'isolated_inherited_chain_checks_per_variant':20,
    'synthesis_audit_sha256':sha256(audit.stdout).hexdigest(),
    'source_manifest_sha256':digest(HERE/'sources_manifest.json'),
    'inherited_822_suite_rerun':False,'large_ground_proof_rerun':False,
    'formal_proof_assistant_verification':False,'T1_T8_closed':[]}
 (HERE/'replay_manifest.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 print(json.dumps(record,indent=2,sort_keys=True))

if __name__=='__main__':main()
