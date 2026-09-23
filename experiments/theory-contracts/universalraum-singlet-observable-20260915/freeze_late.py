"""Freeze later user ideas and narrowly audited legacy evidence."""
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
INPUTS={
 'multiplicity_z4.txt':'/Users/stefanhamann/.codex/attachments/4d8405f1-1743-4257-9bde-9eb0bc6cbc89/pasted-text.txt',
 'fundamental_reduction.txt':'/Users/stefanhamann/.codex/attachments/afeccb91-f41b-49e9-ada4-1d5256c6768b/pasted-text.txt',
 'runtime_synthesis.txt':'/Users/stefanhamann/.codex/attachments/f499030d-b62d-4d8e-968f-7fe4eab672f4/pasted-text.txt',
 'operations_ground_field_v163.txt':'/Users/stefanhamann/.codex/attachments/c309126a-315b-433b-9eff-81caa47c08ad/pasted-text.txt',
 'legacy_native_ground_state.json':'/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/native_ground_state.json',
 'legacy_native_ground_state.py':'/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/native_ground_state.py',
 'legacy_norms_by_traces.py':'/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/norms_by_traces.py',
}
def main():
 out=HERE/'late_sources';out.mkdir(exist_ok=True);manifest={}
 for name,source in INPUTS.items():
  data=Path(source).read_bytes();target=out/name
  if target.exists() and target.read_bytes()!=data:raise RuntimeError('Frozen input conflict')
  target.write_bytes(data)
  manifest[name]={'source':source,'sha256':sha256(data).hexdigest(),'bytes':len(data)}
 (HERE/'late_sources_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps({'status':'PASS','late_inputs':len(manifest)}))
if __name__=='__main__':main()
