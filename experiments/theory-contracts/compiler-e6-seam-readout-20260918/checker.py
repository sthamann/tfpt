import os,json,argparse,hashlib,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
os.environ['TFPT_E6_OUTPUT']=str(args.out.resolve())
import dihedral_extension
from common import PINS
result={'research_id':'UR.COMPILER.E6_READOUT_CLOSURE.04','related_research_id':'UR.COMPILER.SEAM_E8_CHARACTER_EXTENSION.05','verdict':'PARTIAL','e6':json.loads((args.out/'e6.json').read_text()),'seam':json.loads((args.out/'seam.json').read_text()),'d4':json.loads((args.out/'d4.json').read_text()),'source_pins':PINS,'physical_gates_closed':[]}
(args.out/'certificate.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'verdict':result['verdict'],'e6_checks':result['e6']['checks'],'total_checks':result['d4']['total_checks'],'closure':result['e6']['closure_history'],'forced_fourth_phase':-1,'seam_trace':4,'original_J_lift_trace':0,'certificate_sha256':hashlib.sha256((args.out/'certificate.json').read_bytes()).hexdigest()},indent=2))
