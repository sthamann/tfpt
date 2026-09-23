"""Freeze read-only inputs once; refuse drift within this research version."""
from pathlib import Path
from hashlib import sha256
import json
import shutil

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
RELATIVE = [
    'experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py',
    'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz',
    'experiments/theory-contracts/compiler-involution-types/checker.py',
    'experiments/theory-contracts/carrier-module-conjugation/checker.py',
    'experiments/double-cover-rh-audit-2026-09-08/seam_source.py',
    'experiments/tfpt-discovery/seam_state_derivation_probe.py',
    'verification/tfpt_constants.py',
]
EXTERNAL = {
    'attachment_symmetry.txt': '/Users/stefanhamann/.codex/attachments/71ca865d-1f41-4b39-a253-d1293acf9f36/pasted-text.txt',
    'attachment_ground.txt': '/Users/stefanhamann/.codex/attachments/7380c383-f364-4ef8-8066-24aa4d180d85/pasted-text.txt',
    'historical_v1.6.5.md': '/Users/stefanhamann/Documents/TFPT_Universalraum_Zwei_Banken_Konsolidierung_2026-09-15_v1.6.5.md',
    'historical_v1.6.5.zip': '/Users/stefanhamann/Documents/TFPT_Universalraum_Zwei_Banken_Pruefpaket_2026-09-15_v1.6.5.zip',
}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    records = {}
    inputs = [(REPO / rel, 'sources/repo/' + rel) for rel in RELATIVE]
    inputs += [(Path(source), 'sources/' + name) for name, source in EXTERNAL.items()]
    for source, relative in inputs:
        target = HERE / relative
        before = digest(source)
        if target.exists() and digest(target) != before:
            raise RuntimeError('Refusing changed frozen source: ' + relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(source, target)
        if digest(source) != before or digest(target) != before:
            raise RuntimeError('Input changed while freezing: ' + str(source))
        records[relative] = {'source': str(source), 'sha256': before}
    manifest = HERE / 'sources_manifest.json'
    body = json.dumps(records, indent=2, sort_keys=True) + '\n'
    if manifest.exists() and manifest.read_text() != body:
        raise RuntimeError('Refusing changed source manifest')
    manifest.write_text(body)
    print(json.dumps({'status': 'PASS', 'inputs': len(records)}))


if __name__ == '__main__':
    main()
