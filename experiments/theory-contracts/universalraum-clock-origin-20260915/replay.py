"""Portable replay of eight frozen checks; never refresh the live sources."""
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
OUT = HERE/'replay_outputs'
FROZEN = HERE/'agents/symmetry_audit/frozen/experiments/theory-contracts/universalraum-native-ground-response-20260915'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    for name in ('sources_manifest.json', 'late_sources_manifest.json'):
        for relative, record in json.loads((HERE/name).read_text()).items():
            if digest(HERE/relative) != record['sha256']:
                raise RuntimeError('Frozen source changed: '+relative)
    agent = HERE/'agents/ground_field_audit'
    build = subprocess.run(['c++', '-std=c++17', '-O2', str(agent/'contracted_krylov.cpp'),
                            '-o', str(agent/'contracted_krylov')], capture_output=True, timeout=60)
    if build.returncode:
        raise RuntimeError('Contraction build failed: '+build.stderr.decode())
    jobs = [(name, FROZEN/(name+'.py'), None) for name in
            ('operation_symmetry','symmetry_availability','lorentz_types')]
    jobs += [('scope', HERE/'agents/symmetry_audit/check_scope.py', None),
             ('clock', HERE/'verify_clock_casimir.py', None),
             ('ground_field', agent/'verify.py', 'file'),
             ('minimal', HERE/'agents/minimal_origin/verify.py', None),
             ('overlap', HERE/'agents/overlap_audit/check_overlap.py', None)]

    def run(job):
        label, path, mode = job
        before = digest(path)
        reports = []
        for variant, flags in [('normal',['-B']),('optimized',['-B','-OO'])]:
            output = OUT/(label+'_'+variant+'.json')
            argv = [sys.executable, *flags, str(path)]
            if mode == 'file':
                argv += ['--output', str(output)]
            proc = subprocess.run(argv, cwd=HERE, capture_output=True, timeout=150)
            (OUT/(label+'_'+variant+'.stderr.txt')).write_bytes(proc.stderr)
            if proc.returncode or proc.stderr:
                raise RuntimeError(label+' '+variant+' failed: '+proc.stderr.decode()[-3000:])
            if mode != 'file':
                output.write_bytes(proc.stdout)
            data = json.loads(output.read_text())
            if data.get('status') != 'PASS':
                raise RuntimeError(label+' not PASS')
            count = data.get('checks_count', data.get('checks'))
            if not isinstance(count, int):
                raise RuntimeError('Missing integer count: '+label)
            reports.append((digest(output),count))
        if reports[0] != reports[1] or digest(path) != before:
            raise RuntimeError(label+' replay or source changed')
        return label, {'sha256':reports[0][0], 'checks':reports[0][1],
                       'source_sha256':before, 'both_variants_identical':True}

    with ThreadPoolExecutor(max_workers=3) as pool:
        reports = dict(pool.map(run, jobs))
    total = sum(row['checks'] for row in reports.values())
    if total != 2205:
        raise RuntimeError('Documented total stale: '+str(total))
    # Reproduction of the new program outputs is not a new execution of the
    # older native whole-sector theorem or the historical v1.6.5 package.
    summary = {'status':'PASS', 'validation_scope':'FROZEN_INPUTS_ONLY',
               'checks_per_variant':total, 'supplied_guard_count':1127,
               'own_checks':total-1127, 'ground_numerical_checks':5,
               'supplied_literal_true_guards':9,
               'prior_ground_full_enumeration_replayed':False,
               'RH_graph_globally_current':False,
               'reports':reports}
    (HERE/'replay_manifest.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
