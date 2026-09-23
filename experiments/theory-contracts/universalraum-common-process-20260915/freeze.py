"""Pin baseline and newly supplied synthesis without changing any input."""
from pathlib import Path
from hashlib import sha256
import json
HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'universalraum-singlet-observable-20260915'
PAPER=Path('/Users/stefanhamann/Documents/TFPT_Universalraum_Forschungspaper_2026-09-15')
INPUTS={
 'W.npz':OLD/'sources/spinor_tensors.npz',
 'baseline_v167.md':OLD/'deliverables/TFPT_Universalraum_Richtige_Kette_Konsolidierung_2026-09-15_v1.6.7.md',
 'baseline_replay.json':OLD/'replay_manifest.json',
 'synthesis.md':PAPER/'TFPT_Universalraum_Forschungspaper_2026-09-15.md',
 'synthesis.pdf':PAPER/'TFPT_Universalraum_Forschungspaper_2026-09-15.pdf',
 'synthesis_protocol.json':PAPER/'Pruefprotokoll.json',
 'synthesis_sources.json':PAPER/'Quellenmanifest.json',
 'synthesis_result.json':PAPER/'Verifikation_eigene_Herleitungen.json',
 'synthesis_package.zip':PAPER/'TFPT_Universalraum_Forschungspaper_Pruefpaket_2026-09-15.zip',
 'late_handgriffe.txt':Path('/Users/stefanhamann/.codex/attachments/706ea1e7-e7ab-4216-995b-119597c9e5c2/pasted-text.txt'),
 'late_machine.txt':Path('/Users/stefanhamann/.codex/attachments/b8d5cff4-faed-4189-9a07-a42fd05920bb/pasted-text.txt'),
 'late_fundamental.txt':Path('/Users/stefanhamann/.codex/attachments/b0d7e533-3ca8-4a84-966c-2546b066dd08/pasted-text.txt'),
}
def main():
 out=HERE/'sources';out.mkdir(exist_ok=True);manifest={}
 for name,p in INPUTS.items():
  data=p.read_bytes();q=out/name
  if q.exists() and q.read_bytes()!=data:raise RuntimeError('Frozen source conflict '+name)
  q.write_bytes(data);manifest[name]={'original':str(p),'sha256':sha256(data).hexdigest(),'bytes':len(data)}
 (HERE/'sources_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'PASS','source_count':len(manifest)}))
if __name__=='__main__':main()
