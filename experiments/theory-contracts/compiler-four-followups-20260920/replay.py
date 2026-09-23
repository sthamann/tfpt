#!/usr/bin/env python3
"""Replay the four claim-specific checkers and retain evidence classes."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
lanes=[('origin','checker.py','run_normal.json'),
       ('geometry','checker.py','results.json'),
       ('vacuum','k3_vacuum_certificate.py','k3_vacuum_certificate.json'),
       ('large_chain','checker.py','results.json')]
results={}
for lane,script,record in lanes:
    path=HERE/lane/script
    before=(HERE/lane/record).read_bytes()
    normal=subprocess.run([sys.executable,'-B',str(path)],cwd=ROOT,capture_output=True,check=True)
    after_normal=(HERE/lane/record).read_bytes()
    optimized=subprocess.run([sys.executable,'-B','-OO',str(path)],cwd=ROOT,capture_output=True,check=True)
    if normal.stdout!=optimized.stdout:raise RuntimeError('optimized drift '+lane)
    if before!=after_normal or after_normal!=(HERE/lane/record).read_bytes():
        raise RuntimeError('certificate bytes drift '+lane)
    saved=json.loads(after_normal)
    output=json.loads(normal.stdout)
    # The vacuum checker saves its full certificate and prints summary JSON.
    data=saved if lane=='vacuum' else output
    if data.get('status')!='PASS':raise RuntimeError('lane failed '+lane)
    if output.get('status')!=data['status'] or output.get('checks')!=data.get('checks'):
        raise RuntimeError('stdout summary disagrees '+lane)
    if saved!=data:raise RuntimeError('saved result drift '+lane)
    guards=data.get('checks')
    if isinstance(guards,list):guards=len(guards)
    results[lane]={'status':data['status'],'guards':guards,
        'normal_optimized_identical':True,'stdout_sha256':hashlib.sha256(normal.stdout).hexdigest(),
        'checker_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

num=json.loads((HERE/'large_chain/numerical_results.json').read_text())
if num['status']!='PASS_NUMERICAL_COMPRESSION_ONLY' or num['full_vacuum_or_critical_point_proved']:
    raise RuntimeError('compression numerical scope')
index=json.loads((HERE/'contract_index.json').read_text())
if index['T1_T8_closed'] or index['promotion']:raise RuntimeError('invalid promotion')
if set(results)!=set(index['lanes']):raise RuntimeError('missing requested follow-up')

result={'status':'PASS_FOUR_LANE_REPLAY','lanes':results,
    'guard_count_note':'Integrity totals, not a count of independent theorems or physical capabilities.',
    'large_chain_numerics':'Previously executed five compression sizes, pinned in numerical_results.json; not full H eigenvalues.',
    'prior_native_contracts':'Reused hash-pinned prerequisites; prior full contract suites are not rerun here.',
    'promotion':False,'closed_gate_ids':[]}
(HERE/'replay.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
