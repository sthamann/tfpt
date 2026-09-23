"""Portable, fail-closed replay of four independent v1.6.9 strands.

Frozen v1.6.8 evidence is hash-checked, not silently counted as a new replay.
"""
from pathlib import Path
from hashlib import sha256
from concurrent.futures import ThreadPoolExecutor
import json
import platform
import subprocess
import sys

HERE=Path(__file__).resolve().parent
JOBS={
    'composition':'verify_composition.py',
    'source':'agents/source/verify.py',
    'protocol':'agents/protocol/verify_protocol.py',
    'field':'agents/field/verify.py',
}

def run_one(item):
    name,relative=item
    script=HERE/relative
    variants=[]
    for mode,flags in [('normal',[]),('optimized',['-OO'])]:
        proc=subprocess.run([sys.executable,'-B','-W','error',*flags,str(script)],
                            cwd=HERE,capture_output=True,timeout=300)
        if proc.returncode or proc.stderr:
            raise RuntimeError(name+' '+mode+': '+proc.stderr.decode(errors='replace'))
        data=json.loads(proc.stdout)
        if data.get('status')!='PASS':raise RuntimeError(name+' not PASS')
        target=HERE/'replay_outputs'/(name+'_'+mode+'.json')
        target.write_bytes(proc.stdout)
        variants.append(proc.stdout)
    if variants[0]!=variants[1]:raise RuntimeError(name+' optimization discrepancy')
    data=json.loads(variants[0])
    exact=data.get('exact_checks',data.get('new_exact_checks',data.get('independent_exact_checks')))
    numeric=data.get('numerical_checks',data.get('numeric_checks',data.get('new_numeric_checks')))
    if not isinstance(exact,int) or not isinstance(numeric,int):raise RuntimeError('Missing counts '+name)
    return name,{'script':relative,'checker_sha256':sha256(script.read_bytes()).hexdigest(),
                 'result_sha256':sha256(variants[0]).hexdigest(),
                 'exact_checks':exact,'numerical_checks':numeric,
                 'source_guards':data.get('source_guard_counts',{}),
                 'normal_optimized_byte_identical':True,'exit_codes':[0,0]}

def main():
    (HERE/'replay_outputs').mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool:records=dict(pool.map(run_one,JOBS.items()))
    _,crosscheck=run_one(('independent_review','agents/source/review_parent.py'))
    result={'status':'PASS','python':platform.python_version(),'reports':records,
            'own_exact_checks_per_variant':sum(x['exact_checks'] for x in records.values()),
            'own_numerical_checks_per_variant':sum(x['numerical_checks'] for x in records.values()),
            'inherited_source_guards':records['source']['source_guards'],
            'independent_crosscheck_not_counted_in_own_total':crosscheck,
            'baseline_v168_full_suite_rerun':False,'T1_T8_closed':[],
            'exact_category_includes_source_pins_and_structural_guards':True}
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    (HERE/'replay_manifest.json').write_text(text)
    print(text,end='')

if __name__=='__main__':main()
