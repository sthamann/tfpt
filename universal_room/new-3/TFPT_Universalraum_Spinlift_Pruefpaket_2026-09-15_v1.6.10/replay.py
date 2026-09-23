"""Reproduce this note and narrowly replay the historical clock witness."""
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
clock_path=HERE/'sources/clock/v480_multilocal_four_interval.py'
if not clock_path.exists():clock_path=ROOT/'verification/v480_multilocal_four_interval.py'
reports={}
for mode,flags in [('normal',[]),('optimized',['-OO'])]:
    p=subprocess.run([sys.executable,*flags,str(HERE/'verify_spin_lift.py')],capture_output=True,cwd=ROOT)
    (HERE/('verification_'+mode+'.json')).write_bytes(p.stdout)
    (HERE/('verification_'+mode+'.stderr')).write_bytes(p.stderr)
    if p.returncode:
        sys.stderr.buffer.write(p.stderr)
        raise RuntimeError('failed '+mode)
    result=json.loads(p.stdout)
    if result['status']!='PASS':raise RuntimeError('nonPASS')
    reports[mode]={'exit_code':p.returncode,'exact_checks':result['exact_checks'],'sha256':sha256(p.stdout).hexdigest()}
    print(mode+': PASS, '+str(result['exact_checks'])+' conditions',flush=True)
if reports['normal']['sha256']!=reports['optimized']['sha256']:raise RuntimeError('normal/optimized mismatch')
for mode,flags in [('normal',[]),('optimized',['-OO'])]:
    p=subprocess.run([sys.executable,*flags,str(clock_path)],capture_output=True,cwd=clock_path.parent)
    (HERE/('v480_'+mode+'.txt')).write_bytes(p.stdout+p.stderr)
    if p.returncode:raise RuntimeError('v480 failed '+mode)
    reports['v480_'+mode]={'exit_code':p.returncode,'scope':'six finite numerical/mechanism checks plus one scope declaration, not raw-seam identification'}
report={'status':'PASS','normal_optimized_byte_identical':True,'reports':reports,'T1_T8_closed':[]}
late={}
for mode,flags in [('normal',[]),('optimized',['-OO'])]:
    p=subprocess.run([sys.executable,*flags,str(HERE/'verify_new_aspects.py')],capture_output=True,cwd=HERE)
    (HERE/('late_aspects_'+mode+'.json')).write_bytes(p.stdout)
    (HERE/('late_aspects_'+mode+'.stderr')).write_bytes(p.stderr)
    if p.returncode:raise RuntimeError(p.stderr.decode())
    result=json.loads(p.stdout)
    if result['status']!='PASS':raise RuntimeError('late audit nonPASS')
    late[mode]={'exit_code':p.returncode,'exact_checks':result['exact_checks'],'sha256':sha256(p.stdout).hexdigest()}
if late['normal']['sha256']!=late['optimized']['sha256']:raise RuntimeError('late audit mismatch')
report['late_proposals']=late
selection={}
for mode,flags in [('normal',[]),('optimized',['-OO'])]:
    p=subprocess.run([sys.executable,*flags,str(HERE/'verify_reflection_selection.py')],capture_output=True,cwd=HERE)
    (HERE/('reflection_selection_'+mode+'.json')).write_bytes(p.stdout)
    (HERE/('reflection_selection_'+mode+'.stderr')).write_bytes(p.stderr)
    if p.returncode:raise RuntimeError(p.stderr.decode())
    result=json.loads(p.stdout)
    if result['status']!='PASS':raise RuntimeError('selection nonPASS')
    selection[mode]={'exit_code':p.returncode,'exact_checks':result['exact_checks'],'sha256':sha256(p.stdout).hexdigest()}
if selection['normal']['sha256']!=selection['optimized']['sha256']:raise RuntimeError('selection mismatch')
report['reflection_selection']=selection
(HERE/'REPLAY.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report),flush=True)
