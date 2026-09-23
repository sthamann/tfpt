#!/usr/bin/env python3
"""Replay four bounded certificates; fail on source, result or scope drift."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
lanes=('energy','symmetry','frames','origin')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest=json.loads((HERE/'source_manifest.json').read_text())
for rel,expected in manifest['sha256'].items():
    if digest(ROOT/rel)!=expected:
        raise RuntimeError('source drift: '+rel)

result={}
for lane in lanes:
    script=HERE/lane/'checker.py'
    record=HERE/lane/'results.json'
    expected_bytes=record.read_bytes()
    normal=subprocess.run([sys.executable,'-B',str(script)],cwd=ROOT,
                          capture_output=True,check=True)
    after_normal=record.read_bytes()
    optimized=subprocess.run([sys.executable,'-B','-OO',str(script)],cwd=ROOT,
                             capture_output=True,check=True)
    if normal.stdout!=optimized.stdout:
        raise RuntimeError('optimized output drift: '+lane)
    if expected_bytes!=after_normal or after_normal!=record.read_bytes():
        raise RuntimeError('saved certificate drift: '+lane)
    data=json.loads(expected_bytes)
    output=json.loads(normal.stdout)
    if data['status']!='PASS' or output['status']!='PASS':
        raise RuntimeError('failed lane: '+lane)
    if lane=='frames' and json.loads(normal.stdout)!=data:
        raise RuntimeError('frame stdout differs from saved certificate')
    extra=HERE/lane/'results_optimized.json'
    if extra.exists() and extra.read_bytes()!=expected_bytes:
        raise RuntimeError('stale optimized certificate: '+lane)
    guards=data.get('check_count',data.get('exact_checks',data.get('checks')))
    if isinstance(guards,list):guards=len(guards)
    result[lane]={'status':data['status'],'verdict':data['verdict'],
                  'guards':guards,'normal_optimized_identical':True,
                  'checker_sha256':digest(script),'result_sha256':digest(record),
                  'stdout_sha256':hashlib.sha256(normal.stdout).hexdigest()}

index=json.loads((HERE/'contract_index.json').read_text())
if index['promotion'] or index['T1_T8_closed'] or index['closed_gate_ids']:
    raise RuntimeError('unjustified physical promotion')
if set(index['lanes'])!=set(lanes):
    raise RuntimeError('lane/index mismatch')

out={'status':'PASS_FOUR_LANE_REPLAY','research_id':index['research_id'],
     'lanes':result,'source_pin_count':len(manifest['sha256']),
     'guard_count_note':'Integrity guards, not independent physical results.',
     'numerical_support':'origin fixed-patch samples are illustrative; the error theorem is analytic.',
     'prior_contracts':'Frozen prerequisites reused; no claim all prior suites were rerun.',
     'promotion':False,'closed_gate_ids':[]}
(HERE/'replay.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
