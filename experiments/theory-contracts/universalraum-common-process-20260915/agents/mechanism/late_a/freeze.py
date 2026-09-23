from pathlib import Path
from hashlib import sha256
import json
import shutil

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
BASE=ROOT/'experiments/theory-contracts/universalraum-native-operations-ground-response-20260915'
SOURCES={
 'attachment.txt':Path('/Users/stefanhamann/.codex/attachments/706ea1e7-e7ab-4216-995b-119597c9e5c2/pasted-text.txt'),
 'norms_by_traces.py':BASE/'norms_by_traces.py',
 'common.py':BASE/'common.py',
 'norms_by_traces.json':BASE/'norms_by_traces.json',
 'norms_normal.json':BASE/'norms_normal.json',
 'norms_optimized.json':BASE/'norms_optimized.json',
 'norms_normal.stderr.txt':BASE/'norms_normal.stderr.txt',
 'native_ground_state.py':BASE/'native_ground_state.py',
 'native_ground_state.json':BASE/'native_ground_state.json',
 'replay_manifest.json':BASE/'replay_manifest.json',
 'spinor_tensors.npz':HERE.parent/'inputs/spinor_tensors.npz',
}


def main():
 (HERE/'inputs').mkdir(exist_ok=True)
 manifest={}
 for name,path in SOURCES.items():
  data=path.read_bytes();dest=HERE/'inputs'/name
  if dest.exists() and dest.read_bytes()!=data:raise RuntimeError('already frozen: '+name)
  if not dest.exists():shutil.copyfile(path,dest)
  manifest[name]={'source':str(path),'sha256':sha256(data).hexdigest(),'bytes':len(data)}
 encoded=json.dumps(manifest,indent=2,sort_keys=True)+'\n'
 dest=HERE/'inputs_manifest.json'
 if dest.exists() and dest.read_text()!=encoded:raise RuntimeError('manifest already frozen')
 dest.write_text(encoded)
 print(json.dumps({'frozen':len(manifest),'manifest_sha256':sha256(encoded.encode()).hexdigest()}))


if __name__=='__main__':main()
