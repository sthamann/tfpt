"""Freeze supplied work and replay unchanged programs in this owned directory.

No original is executed in place or overwritten. Prior v1.6.4 proofs are
included as a pinned dependency, not advertised as freshly re-enumerated here.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
EXT = Path('/Users/stefanhamann/Documents/Codex/2026-09-15/suc')
OLD = HERE.parent / 'universalraum-native-ground-response-20260915'
TENSOR_REL = 'TFPT_Universalraum_Native_Antwort_Pruefpaket_2026-09-15_v1.6.4/TFPT_Native_Antwort_v1.6.4/ground_replay/outputs/simple_core/spinor_tensors.npz'
KNOWN = {
    'sources/user_attachment.txt': '6ac995cffe25ccaa6ca85996d2f4f550005ced25b1f01f4e9e144489ddf9101b',
    'external/unification/verify_unification.py': '4507bc05d73cfdc538434360106d5a25a55f37edf5a0b7396447b4dc52617bd5',
}
# Explicitly pinned programs and original reports; the remaining source files
# receive immutable content hashes on the first --freeze call.
KNOWN.update({
    'external/exchange/verify_exchange.py': '087f18372cc9c74ee640a9f69828dc6a4147b00a20a0c364bfadd99486107eb8',
    'sources/external_beweisversuch.md': '44622c6db559e2bd38d59b643c4d44f41e23b6085197559482c8404ca11f774a',
    'sources/external_austausch.md': '30ca411008735b55903d907c3c459403a1119751550b58d6aa553ef62a76fc44',
    'sources/external_unification_original.json': 'ce1d58c5f864afaa4af2d11e12ef49a6a32df451747221fd15cd37e3d2572b2c',
    'sources/external_exchange_original.json': 'f08ec841098096899c32dccdfdae312e6eabe74a7a55e949e4390c998c9f1bee',
    'external/exchange/source/round37_checker.py': '559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52',
    'external/unification/' + TENSOR_REL: '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763',
})


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def inputs():
    result = {
        'sources/user_attachment.txt': Path('/Users/stefanhamann/.codex/attachments/addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt'),
        'sources/external_beweisversuch.md': EXT / 'outputs/Universalraum_Beweisversuch_2026-09-15.md',
        'sources/external_austausch.md': EXT / 'outputs/Universalraum_Urspruenglicher_Austausch_2026-09-15.md',
        'sources/external_unification_original.json': EXT / 'work/new_proofs_normal.json',
        'sources/external_exchange_original.json': EXT / 'outputs/Universalraum_Austausch_Pruefergebnisse_2026-09-15.json',
        'external/unification/verify_unification.py': EXT / 'work/verify_unification.py',
        'external/exchange/verify_exchange.py': EXT / 'work/exchange_package_replay/Universalraum_Austausch/verify_exchange.py',
        'external/unification/' + TENSOR_REL: OLD / 'ground_replay/outputs/simple_core/spinor_tensors.npz',
        'sources/native_v1.6.4_Pruefpaket.zip': OLD / 'TFPT_Universalraum_Native_Antwort_Pruefpaket_2026-09-15_v1.6.4.zip',
        'sources/native_pole_consolidation.json': OLD / 'pole_consolidation_normal.json',
        'sources/native_charged_response.json': OLD / 'charged_response_normal.json',
        'sources/native_external_pole.json': OLD / 'external_pole_normal.json',
        'sources/native_RESULTS.md': OLD / 'RESULTS.md',
        'sources/OPEN_PROBLEMS_2026-09-15_snapshot.md': REPO / 'docs/OPEN_PROBLEMS.md',
        'sources/RESEARCH_2026-09-09_snapshot.md': REPO / 'experiments/theory-contracts/RESEARCH_2026-09-09.md',
    }
    source = EXT / 'work/exchange_package_replay/Universalraum_Austausch/source'
    for path in sorted(source.iterdir()):
        if path.is_file():
            result['external/exchange/source/' + path.name] = path
    return result


def freeze():
    target = HERE / 'sources_manifest.json'
    if target.exists():
        raise RuntimeError('Refusing to replace an existing frozen source manifest')
    manifest = []
    for relative, original in inputs().items():
        sha = digest(original)
        if relative in KNOWN and sha != KNOWN[relative]:
            raise RuntimeError('Known source changed: ' + relative)
        out = HERE / relative
        if out.exists():
            raise RuntimeError('Refusing to overwrite source: ' + relative)
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(original, out)
        manifest.append({'copy': relative, 'original': str(original), 'sha256': sha})
    target.write_text(json.dumps(manifest, indent=2) + '\n')


def run(frozen_only=False):
    manifest = json.loads((HERE / 'sources_manifest.json').read_text())
    if (HERE / 'late_sources_manifest.json').exists():
        manifest += json.loads((HERE / 'late_sources_manifest.json').read_text())
    status = {'status': 'RUNNING', 'commands': [], 'reports': {},
              'validation_scope': 'FROZEN_SOURCE_SNAPSHOT' if frozen_only else 'FROZEN_AND_LIVE_SOURCES',
              'previous_native_proofs': 'pinned v1.6.4 package; full enumeration not rerun in this revision'}

    def save():
        (HERE / 'replay_manifest.json').write_text(json.dumps(status, indent=2) + '\n')

    def check_sources(originals=False):
        for entry in manifest:
            path = Path(entry['original']) if originals else HERE / entry['copy']
            if digest(path) != entry['sha256']:
                raise RuntimeError('Source changed: ' + str(path))

    def live_differences():
        differences = []
        for entry in manifest:
            path = Path(entry['original'])
            current = digest(path) if path.exists() else None
            if current != entry['sha256']:
                differences.append({'path': str(path), 'frozen_sha256': entry['sha256'],
                                    'current_sha256': current})
        return differences

    save()
    try:
        check_sources()
        # The shipped package replays without requiring the original locations.
        status['originals_checked_at_start'] = all(Path(e['original']).exists() for e in manifest)
        status['live_differences_at_start'] = live_differences()
        if status['originals_checked_at_start'] and not frozen_only:
            check_sources(originals=True)
        programs = [
            ('unification', 'external/unification/verify_unification.py', 'sources/external_unification_original.json'),
            ('exchange', 'external/exchange/verify_exchange.py', 'sources/external_exchange_original.json'),
            ('two_bank_transfer', 'verify_two_bank_transfer.py', None),
            ('symmetry_scope', 'verify_symmetry_scope.py', None),
            ('late_addenda', 'audit_addenda.py', None),
        ]
        for label, relative, original in programs:
            results = []
            for variant, flags in [('normal', []), ('optimized', ['-OO'])]:
                out = HERE / (label + '_' + variant + '.json')
                args = [sys.executable, '-B', *flags, str(HERE / relative)]
                if label == 'exchange':
                    args += ['--output', str(out)]
                started = time.monotonic()
                proc = subprocess.run(args, cwd=HERE, text=True, capture_output=True)
                (HERE / (label + '_' + variant + '.stderr.txt')).write_text(proc.stderr)
                status['commands'].append({'name': label, 'variant': variant,
                                           'exit_code': proc.returncode,
                                           'seconds': round(time.monotonic()-started, 3)})
                save()
                if proc.returncode:
                    raise RuntimeError(label + ': ' + proc.stderr[-3000:])
                if label != 'exchange':
                    out.write_text(proc.stdout)
                data = json.loads(out.read_text())
                if data.get('status', 'PASS') != 'PASS':
                    raise RuntimeError(label + ': non-PASS result')
                results.append(digest(out))
                print(label, variant, data['checks'], 'checks', flush=True)
            if results[0] != results[1]:
                raise RuntimeError(label + ': optimization changed result')
            if original and results[0] != digest(HERE / original):
                raise RuntimeError(label + ': differs from supplied result')
            status['reports'][label] = {'checks': data['checks'], 'sha256': results[0],
                                        'normal_optimized_identical': True,
                                        'identical_to_supplied_report': bool(original)}
            save()
        check_sources()
        status['live_differences_at_end'] = live_differences()
        if status['originals_checked_at_start'] and not frozen_only:
            check_sources(originals=True)
        status['source_copies_unchanged'] = True
        status['originals_unchanged'] = not status['live_differences_at_end']
        status['status'] = 'PASS'
        save()
    except BaseException as error:
        status['status'] = 'FAIL'
        status['error'] = repr(error)
        save()
        raise


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--freeze', action='store_true')
    ap.add_argument('--frozen-only', action='store_true',
                    help='Replay immutable snapshot, report rather than conceal any live source drift')
    args = ap.parse_args()
    if args.freeze:
        freeze()
    run(frozen_only=args.frozen_only)
