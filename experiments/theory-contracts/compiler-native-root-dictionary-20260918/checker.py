import os,sys,json,subprocess,argparse,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
env=dict(os.environ);env['TFPT_DICTIONARY_OUTPUT']=str(a.out.resolve());env['PYTHONDONTWRITEBYTECODE']='1'
opt=['-OO'] if sys.flags.optimize==2 else []
results={}
for script,key in [('abstract_spin10.py','abstract'),('weyl_decider.py','weyl'),('native_dictionary.py','native'),('clock_lifts.py','clocks')]:
 result=subprocess.run([sys.executable,'-B',*opt,str(HERE/script)],env=env,text=True,capture_output=True)
 if result.returncode:
  print(result.stdout);print(result.stderr,file=sys.stderr);raise SystemExit(result.returncode)
 data=json.loads((a.out/(key+'.json')).read_text())
 if 'checks' in data:data['check_count']=len(data.pop('checks'))
 results[key]=data;print(key+': verified',flush=True)
cert={'research_id':'UR.COMPILER.NATIVE_ROOT_DICTIONARY.03','verdict':'PARTIAL','mathematical_verdict':'EXACT_NATIVE_OPERATOR_DICTIONARY_WITH_CLOCK_LIFTS; ROOT_SPACE_SPIN8_IDENTIFICATION_REFUTED','source_pins':json.loads((HERE/'source_pins.json').read_text()),'results':results,'first_open_implication':'Selection of physical readout, state and field dynamics from the original principles; algebraic clock automorphisms are not yet physical time evolution.'}
(a.out/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('certificate '+hashlib.sha256((a.out/'certificate.json').read_bytes()).hexdigest())
