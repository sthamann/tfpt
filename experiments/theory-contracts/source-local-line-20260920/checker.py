"""Replay exact symbols and bounded diagnostics; no physics-gate promotion."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

def require(condition, message):
    if not condition:
        raise ValueError(message)

def run_script(filename):
    flags = ['-B'] + (['-OO'] if sys.flags.optimize else [])
    completed = subprocess.run([sys.executable, *flags, str(HERE/filename)],
                               text=True, capture_output=True, check=True)
    return json.loads(completed.stdout)

def main():
    manifest = json.loads((HERE/'source_manifest.json').read_text())
    for row in manifest['sources']:
        require(hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()==row['sha256'],
                'source drift: '+row['path'])
    exact = run_script('source_exact_check.py')
    target = run_script('review_checker.py')
    source = run_script('source_line_check.py')
    require(exact['status']=='PASS' and target['status']=='PASS', 'finite checks')
    rows = source['joint_growing_radius_refining_lattice']
    require(len(rows)==8 and {x['r'] for x in rows}=={1,3}, 'both original seam sectors')
    require(max(x['raw_row_residual_bound_violation'] for x in rows)<1e-12, 'row residual bound')
    for r in (1,3):
        data = [x for x in rows if x['r']==r]
        require(data[-1]['filled_error_to_1_over_2'] < data[0]['filled_error_to_1_over_2']/7,
                'charged filled-source convergence diagnostic')
        require(data[-1]['response_error_to_continuum'] < data[0]['response_error_to_continuum']/7,
                'charged source time convergence diagnostic')
    require(all(x['holonomy_filled_difference']>.07 for x in source['fixed_radius_negative_control']),
            'fixed-radius holonomy negative control remains visible')
    result = {'status':'PASS','research_verdict':'PARTIAL',
        'research_id':'UR.SOURCE.LOCAL_LIMIT.01',
        'source_pins_checked':len(manifest['sources']),
        'exact':exact,'conditional_target_diagnostics':target,'one_copy_source_diagnostics':source,
        'analytic_proofs':['SOURCE_LINE_PROOF.txt','LOCAL_LIMIT_REVIEW.txt','POLARIZATION_GATE.txt'],
        'source_origin_audit':'SOURCE_AUDIT.txt',
        'complete_TFPT_solution':False,'physical_gates_closed':[]}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
