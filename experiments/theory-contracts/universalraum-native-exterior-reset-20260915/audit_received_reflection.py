"""Non-mutating replay of the received 331-check report, plus scope controls."""
from pathlib import Path
from hashlib import sha256
import importlib.util
import json
import os
import subprocess
import sys
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SOURCE=ROOT/'experiments/theory-contracts/universalraum-seam-reflection-lift-20260915'
OUT=HERE/'received_reflection'

def need(condition,label):
    if not bool(condition):raise RuntimeError(label)

def load_received():
    spec=importlib.util.spec_from_file_location('received_reflection',SOURCE/'seam_reflection_lift.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def child():
    module=load_received()
    data=module.run()
    print(json.dumps(data,indent=2,sort_keys=True,default=str))

def main():
    OUT.mkdir(exist_ok=True)
    names=['README.md','RESULTS.md','seam_reflection_lift.py',
           'seam_reflection_normal.json','seam_reflection_optimized.json']
    pins={name:sha256((SOURCE/name).read_bytes()).hexdigest() for name in names}
    dependency_names=[
        'verification/v480_multilocal_four_interval.py',
        'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs/native_common.py',
        'experiments/theory-contracts/compiler-involution-types/checker.py',
        'experiments/theory-contracts/carrier-module-conjugation/checker.py',
        'experiments/double-cover-rh-audit-2026-09-08/seam_source.py',
        'experiments/tfpt-discovery/seam_state_derivation_probe.py',
    ]
    dependencies={name:sha256((ROOT/name).read_bytes()).hexdigest() for name in dependency_names}
    for name in dependency_names:
        target=OUT/'dependencies'/name
        target.parent.mkdir(parents=True,exist_ok=True)
        if not target.exists():target.write_bytes((ROOT/name).read_bytes())
        need(sha256(target.read_bytes()).hexdigest()==dependencies[name],'dependency snapshot changed '+name)
    for name in names:
        target=OUT/name
        if not target.exists():target.write_bytes((SOURCE/name).read_bytes())
        need(sha256(target.read_bytes()).hexdigest()==pins[name],'received source changed since snapshot '+name)
    runs=[]
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    for name,flags in [('normal',[]),('optimized',['-OO'])]:
        result=subprocess.run([sys.executable,*flags,str(Path(__file__).resolve()),'--child'],
                              capture_output=True,text=True,cwd=ROOT,env=env)
        (OUT/(name+'.stdout.json')).write_text(result.stdout)
        (OUT/(name+'.stderr.txt')).write_text(result.stderr)
        need(result.returncode==0,name+' replay: '+result.stderr)
        data=json.loads(result.stdout)
        need(data['status']=='PASS' and data['exact_checks']==331,'received replay contract')
        runs.append({'variant':name,'sha256':sha256(result.stdout.encode()).hexdigest(),
                     'matches_received_bytes':result.stdout.encode()==(SOURCE/'seam_reflection_normal.json').read_bytes()})
    need(runs[0]['sha256']==runs[1]['sha256'],'received optimized replay differs')
    module=load_received()
    pattern=module._vertex_edge_pattern(256,8,48)
    need(pattern[63][1][1]==[None,-1,-1,None],'raw gap signs include cut-dependent profiles')
    # General signed ring representation, checked independently without floats.
    exact=[]
    for Q in (3,4,5,6,8,9,16):
        N=4*Q
        for ell in range(1,Q):
            for p in (0,Q-ell):
                intervals=[[(p+j*Q+u)%N for u in range(ell)] for j in range(4)]
                gaps=[[(p+j*Q+ell+v)%N for v in range(Q-ell)] for j in range(4)]
                occupied={x for arc in intervals for x in arc}
                centers=[c for c in range(N) if {(c-x)%N for x in occupied}==occupied]
                predicted=sorted({(2*p+ell-1+k*Q)%N for k in range(4)})
                need(centers==predicted,'general interval reflection centers')
                for k in range(4):
                    c=2*p+ell-1+k*Q
                    for j in range(4):
                        need({(c-x)%N for x in intervals[j]}==set(intervals[(k-j)%4]),'interval index rule')
                        need({(c-x)%N for x in gaps[j]}==set(gaps[(k-j-1)%4]),'gap index rule')
                exact.append({'N':N,'ell':ell,'p0':p})
    # RP by Hilbert reconstruction does not in general exclude zero energy.
    # This is not claimed to satisfy every additional geometric seam demand.
    omega=s.Matrix([1,0]);ops=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.diag(1,-1)]
    gram=s.Matrix(3,3,lambda i,j:(omega.T*ops[i].T*ops[j]*omega)[0])
    need(gram.eigenvals()=={s.Integer(2):1,s.Integer(1):1,s.Integer(0):1},'zero-energy time-reflection Gram positive')
    code=(ROOT/'verification/v480_multilocal_four_interval.py').read_text()
    need('(np.arange(n) + 0.5)' in code,'v480 imposes antiperiodic momenta as input')
    for name,digest in pins.items():
        need(sha256((SOURCE/name).read_bytes()).hexdigest()==digest,'received source mutated '+name)
    for name,digest in dependencies.items():
        need(sha256((ROOT/name).read_bytes()).hexdigest()==digest,'dependency changed during run '+name)
    report={'status':'PASS','received_source_pins':pins,'received_runs':runs,
            'dependency_pins':dependencies,
            'received_check_count':331,'received_explicit_numerical_state_checks':4,
            'received_gap_signs':[None,-1,-1,None],
            'independent_exact_geometry_cases':len(exact),
            'all_size_formula':{'centers':'2*p0+ell-1+k*Q mod 4Q',
                                'interval_index':'j -> k-j mod 4','gap_index':'j -> k-j-1 mod 4'},
            'zero_energy_time_RP_Gram_eigenvalues':[0,1,2],
            'source_files_unchanged':True,
            'claim_decision':'valid conditional ring/reflection and W witnesses; no raw-seam AP selection proof in v480; no shared ring-to-W field map'}
    (OUT/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    if '--child' in sys.argv:child()
    else:main()
