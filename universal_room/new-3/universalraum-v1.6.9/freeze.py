"""Freeze this research round's inputs; refuse changes to an existing pin."""
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'universalraum-common-process-20260915'
REPO=HERE.parents[2]
INPUTS={
 'W.npz':OLD/'sources/W.npz',
 'baseline_v168.md':OLD/'deliverables/TFPT_Universalraum_Gemeinsamer_Prozess_Konsolidierung_2026-09-15_v1.6.8.md',
 'baseline_replay.json':OLD/'replay_manifest.json',
 'baseline_package.zip':OLD/'TFPT_Universalraum_Gemeinsamer_Prozess_Pruefpaket_2026-09-15_v1.6.8.zip',
 'native_operations.py':OLD/'agents/mechanism/inputs/operations_commutant.py',
 'compiler_information.md':REPO/'docs/TFPT_COMPILER_INFORMATION_NEUSTART_2026-09-12.md',
}

def main():
 out=HERE/'sources';out.mkdir(exist_ok=True);records={}
 for name,p in INPUTS.items():
  data=p.read_bytes();q=out/name
  if q.exists() and q.read_bytes()!=data:raise RuntimeError('Frozen source conflict '+name)
  q.write_bytes(data)
  records[name]={'original':str(p),'bytes':len(data),'sha256':sha256(data).hexdigest()}
 (HERE/'sources_manifest.json').write_text(json.dumps(records,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'PASS','source_count':len(records)}))

if __name__=='__main__':main()
