"""Freeze inputs and replay the original ground certificate plus new theorems."""
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OLD=ROOT/'experiments/theory-contracts/universalraum-native-exterior-reset-20260915/ground_replay'
SOURCES={
    'native_tensor.npz':ROOT/'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz',
    'native_common.py':ROOT/'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs/native_common.py',
    'weak_coupling.py':OLD/'work/many_pair/weak_coupling.py',
    'vacuum_number_sector.json':OLD/'outputs/many_pair/vacuum_number_sector.json',
    'v480_multilocal_four_interval.py':ROOT/'verification/v480_multilocal_four_interval.py',
    'v524_woit_beta2_os_quotient.py':ROOT/'verification/v524_woit_beta2_os_quotient.py',
    'v469_seam_crossedproduct_route.py':ROOT/'verification/v469_seam_crossedproduct_route.py',
}


def run():
    initial={str(p):sha256(p.read_bytes()).hexdigest() for p in SOURCES.values()}
    dest=HERE/'inputs';dest.mkdir(exist_ok=True)
    for name,src in SOURCES.items():
        target=dest/name
        if target.exists() and target.read_bytes()!=src.read_bytes():raise RuntimeError('frozen input mismatch '+name)
        if not target.exists():shutil.copyfile(src,target)
    records=[];ground=[];new=[]
    for label,flags in [('normal',[]),('optimized',['-OO'])]:
        work=HERE/('ground_'+label);out=work/'outputs/many_pair';out.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(dest/'vacuum_number_sector.json',out/'vacuum_number_sector.json')
        p=subprocess.run([sys.executable,*flags,str(dest/'weak_coupling.py')],cwd=work,capture_output=True,text=True)
        (HERE/('ground_'+label+'.stdout.txt')).write_text(p.stdout)
        (HERE/('ground_'+label+'.stderr.txt')).write_text(p.stderr)
        if p.returncode:raise RuntimeError(p.stderr)
        data=(out/'weak_coupling_ground.json').read_bytes();ground.append(data)
        records.append({'name':'original ground certificate','mode':label,'exit_code':p.returncode,'sha256':sha256(data).hexdigest()})
        print('ground '+label+' PASS',flush=True)
    if ground[0]!=ground[1]:raise RuntimeError('ground replay mismatch')
    for label,flags in [('normal',[]),('optimized',['-OO'])]:
        p=subprocess.run([sys.executable,*flags,str(HERE/'checker.py')],cwd=HERE,capture_output=True,text=True)
        (HERE/(label+'.stdout.txt')).write_text(p.stdout);(HERE/(label+'.stderr.txt')).write_text(p.stderr)
        if p.returncode:raise RuntimeError(p.stderr)
        parsed=json.loads(p.stdout)
        if parsed['status']!='PASS':raise RuntimeError('new audit did not PASS')
        encoded=json.dumps(parsed,indent=2,sort_keys=True)+'\n';(HERE/(label+'.json')).write_text(encoded);new.append(encoded)
        records.append({'name':'new equivalence decision','mode':label,'exit_code':0,'checks':parsed['check_count'],'sha256':sha256(encoded.encode()).hexdigest()})
        print('new '+label+' PASS',flush=True)
    if new[0]!=new[1]:raise RuntimeError('new replay mismatch')
    if initial!={str(p):sha256(p.read_bytes()).hexdigest() for p in SOURCES.values()}:raise RuntimeError('source changed during replay')
    result={'status':'PASS','runs':records,'normal_optimized_byte_identical':True,'frozen_input_hashes':initial,
        'audit_code_hashes':{p.name:sha256(p.read_bytes()).hexdigest() for p in [HERE/'checker.py',HERE/'replay.py']},
        'ground_replay_scope':'Exact certificate rerun using previously independently checked complete moment receipts; no new enumeration of all high-order configurations.',
        'source_modules_scope':'Read and pinned, not full numerical v480/v524/v469 reruns.',
        'proof_scope':'analytical theorems in RESULTS.md plus exact finite checks; no claim of a complete TOE'}
    (HERE/'replay.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':run()
