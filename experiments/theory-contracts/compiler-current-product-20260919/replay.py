"""Replay the bounded exact contract with source pins and active -OO guards."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
JOBS=[
 ('current_bracket_dictionary.py','current_bracket_dictionary.json',[]),
 ('current_product_readout_check.py','current_product_readout_check.json',[]),
 ('instrument_source_test_check.py','instrument_source_test_check.json',[]),
 ('spin_source_origin_check.py','spin_source_origin_check.json',['--out','spin_source_origin_check.json']),
 ('grade2_product_gram_check.py','grade2_product_gram_check.json',[]),
 ('new_response_sector_check.py','new_response_sector_check.json',[]),
]

def main():
    pins=json.loads((HERE/'source_manifest.json').read_text())
    for name,digest in pins.items():
        if hashlib.sha256((REPO/name).read_bytes()).hexdigest()!=digest:
            raise RuntimeError('source hash mismatch: '+name)
    rows=[]
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    for checker,certificate,args in JOBS:
        outputs=[]
        for flags in [('-B',),('-B','-OO')]:
            run=subprocess.run([sys.executable,*flags,str(HERE/checker),*args],
                cwd=HERE,env=env,capture_output=True,text=True)
            if run.returncode:
                raise RuntimeError(f'{checker} {flags}\n{run.stderr}\n{run.stdout[-1500:]}')
            if checker=='new_response_sector_check.py':
                json.loads(run.stdout)
                (HERE/certificate).write_text(run.stdout)
            raw=(HERE/certificate).read_bytes()
            json.loads(raw)
            outputs.append(raw)
        if outputs[0]!=outputs[1]:
            raise RuntimeError('normal/-OO certificate mismatch: '+checker)
        row={'checker':checker,'certificate':certificate,
             'normal_and_OO_identical':True,
             'sha256':hashlib.sha256(outputs[0]).hexdigest()}
        rows.append(row)
        print(json.dumps(row),flush=True)
    result={'research_id':'UR.COMPILER.CURRENT_PRODUCT.21',
            'verdict':'PASS_SCOPED_REPLAY','source_pins_checked':len(pins),
            'runs':rows,'T1_T8_closed':False,
            'scope':'Exact finite identities and conditional affine products; no microscopic origin or physical process law proved.'}
    (HERE/'replay_certificate.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
