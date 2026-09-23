"""Isolated, pinned replay; no writes to the other session's source tree.

All 635315 bosonic configurations at orders 2,3,4 are freshly enumerated.
The subsequent certificates retain their original scope and hypotheses.
"""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SOURCE = Path('/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3')
OUT = HERE / 'ground_replay'
PINS = {
    'work/many_pair/general_identities.py': '32f3875e2130c4dd005a800d4f7afc30e3a6264f2833214ec9f27882bb950b14',
    'work/many_pair/full_n4.py': '978f71369700b621d2af96d69eff433e8b899d249ccc3f346b1ba25142545dee',
    'work/many_pair/two_pairs.py': '468fcc7c36a6567691a5fcd5a58bad24b5371db28d6bf747150a76c95aa2db00',
    'work/many_pair/vacuum_moments.cpp': '2d30992cadb4ca7d8338cfd8d1194fd72cdabc2a948817de6f37a413cb0c8f17',
    'work/many_pair/vacuum_sector.py': '437f9a53ac3b755ba390e13804a1e46a9a43c189bf6a59b741bb126d8da03552',
    'work/many_pair/weak_coupling.py': '794554393c495ba395f34e6a58d490da821408d4f8effbc394653cd4cec4e80a',
    'work/many_pair/moment_trace.py': '16d5eab3440f48c41ec8d05b32a51d68b8448c347ef908faaff6b176bde713f3',
    'work/many_pair/pair_channels.txt': 'ba3b7f773098759285c8c676c75c570e5535cfaea9535b7710b67a4b55a3ac76',
    'outputs/simple_core/spinor_tensors.npz': '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763',
}
state = {'status': 'RUNNING', 'scope': 'declared native Fock H, no chemical-potential term',
         'source_pins': PINS, 'commands': [], 'fresh_moment_enumeration': [], 'reports': {}}

def save():
    (HERE / 'ground_replay_manifest.json').write_text(json.dumps(state, indent=2) + '\n')

def run(args, label):
    start = time.monotonic()
    result = subprocess.run(args, cwd=OUT, capture_output=True, text=True)
    (OUT / (label + '.stdout.txt')).write_text(result.stdout)
    (OUT / (label + '.stderr.txt')).write_text(result.stderr)
    state['commands'].append({'label': label, 'args': args, 'exit_code': result.returncode,
                              'seconds': round(time.monotonic() - start, 3)})
    save()
    if result.returncode:
        raise RuntimeError(label + ': ' + result.stderr[-2000:])
    print(label + ': completed', flush=True)
    return result.stdout

def main():
    save()
    for name, digest in PINS.items():
        src = SOURCE / name
        if sha256(src.read_bytes()).hexdigest() != digest:
            raise RuntimeError('source changed: ' + name)
        dst = OUT / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    (OUT / 'outputs/many_pair').mkdir(parents=True, exist_ok=True)
    run(['/usr/bin/clang++', '-std=c++20', '-O3', 'work/many_pair/vacuum_moments.cpp',
         '-o', 'work/many_pair/vacuum_moments'], 'compile')
    for order in (2, 3, 4):
        raw = run([str(OUT / 'work/many_pair/vacuum_moments'), str(order)], 'moment_' + str(order))
        record = json.loads(raw)
        (OUT / f'work/many_pair/vacuum_moment{order}.json').write_text(raw)
        record['sha256'] = sha256((OUT / f'work/many_pair/vacuum_values_{order}.bin').read_bytes()).hexdigest()
        state['fresh_moment_enumeration'].append(record)
        save()
    for script, report in [('general_identities', 'general_identities'),
                           ('vacuum_sector', 'vacuum_number_sector'),
                           ('weak_coupling', 'weak_coupling_ground'),
                           ('moment_trace', 'moment_trace_identity')]:
        digests = []
        for variant, flags in [('normal', []), ('optimized', ['-OO'])]:
            run([sys.executable, *flags, 'work/many_pair/' + script + '.py'], script + '_' + variant)
            src = OUT / ('outputs/many_pair/' + report + '.json')
            dst = OUT / (report + '_' + variant + '.json')
            shutil.copy2(src, dst)
            data = json.loads(dst.read_text())
            if 'status' in data and data['status'] != 'PASS':
                raise RuntimeError(script + ' reported non-PASS')
            digests.append(sha256(dst.read_bytes()).hexdigest())
        if digests[0] != digests[1]:
            raise RuntimeError(script + ': optimization-dependent result')
        state['reports'][script] = {'normal_optimized_sha256': digests[0], 'byte_identical': True}
        save()
    state['status'] = 'PASS'
    save()

if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        state['status'] = 'FAIL'
        state['error'] = repr(error)
        save()
        raise
