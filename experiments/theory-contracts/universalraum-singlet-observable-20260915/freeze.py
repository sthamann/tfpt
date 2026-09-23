"""Snapshot only explicitly selected inputs; never modify the originating workers."""
from pathlib import Path
from hashlib import sha256
import json
import shutil

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OLD = REPO/'experiments/theory-contracts/universalraum-clock-origin-20260915'
FOREIGN = REPO/'experiments/theory-contracts/universalraum-operations-groundstate-20260915'
INPUTS = {
    'attachment_round.txt': Path('/Users/stefanhamann/.codex/attachments/9b5200c1-b9a0-42f5-bb8f-68b7e8930b34/pasted-text.txt'),
    'attachment_correction.txt': Path('/Users/stefanhamann/.codex/attachments/13beed73-9c61-4fe7-a452-cfd9a3076ee4/pasted-text.txt'),
    'native_source.py': FOREIGN/'native_source.py',
    'operations_commutant.py': FOREIGN/'operations_commutant.py',
    'oc_run.json': FOREIGN/'oc_run.json',
    'field_dictionary.py': FOREIGN/'field_dictionary.py',
    'fd_run.json': FOREIGN/'fd_run.json',
    'groundstate_probe.py': FOREIGN/'groundstate_probe.py',
    'gp_run.json': FOREIGN/'gp_run.json',
    'gp_err.txt': FOREIGN/'gp_err.txt',
    'old_ground_audit.json': OLD/'agents/ground_field_audit/audit.json',
    'old_contraction.json': OLD/'agents/ground_field_audit/contraction.json',
    'contracted_krylov.cpp': OLD/'agents/ground_field_audit/contracted_krylov.cpp',
    'old_clock.json': OLD/'replay_outputs/clock_normal.json',
    'spinor_tensors.npz': OLD/'agents/symmetry_audit/frozen/experiments/theory-contracts/universalraum-native-ground-response-20260915/ground_replay/outputs/simple_core/spinor_tensors.npz',
    'historical_v1.6.6.md': Path('/Users/stefanhamann/Documents/TFPT_Universalraum_Clock_Gemeinsame_Quelle_Konsolidierung_2026-09-15_v1.6.6.md'),
    'historical_v1.6.6.zip': Path('/Users/stefanhamann/Documents/TFPT_Universalraum_Clock_Gemeinsame_Quelle_Pruefpaket_2026-09-15_v1.6.6.zip'),
}

def main():
    dest = HERE/'sources'
    dest.mkdir(exist_ok=True)
    manifest = {}
    for name, source in INPUTS.items():
        data = source.read_bytes()
        target = dest/name
        if target.exists() and target.read_bytes() != data:
            raise RuntimeError('Refuse to replace frozen input: '+name)
        if not target.exists():
            shutil.copyfile(source, target)
        if target.read_bytes() != data:
            raise RuntimeError('Source changed while copying: '+name)
        manifest[name] = {'source': str(source), 'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    (HERE/'sources_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'status':'PASS','frozen_inputs':len(manifest)}))

if __name__ == '__main__':
    main()
