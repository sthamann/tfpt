"""Read-only comparison of source originals with this round's frozen pins.

Not part of portable mathematical replay; source paths are local provenance.
"""
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
records={}
for manifest in ['sources_manifest.json','agents/source/inputs_manifest.json','agents/protocol/inputs_manifest.json']:
    pins=json.loads((HERE/manifest).read_text())
    for name,r in pins.items():
        path=Path(r.get('original',r.get('source')))
        if not path.is_absolute():path=REPO/path
        actual=sha256(path.read_bytes()).hexdigest()
        if actual!=r['sha256']:raise RuntimeError('Original changed since pin: '+str(path))
        records[str(path)]={'sha256':actual,'unchanged_since_freeze':True}
result={'status':'PASS','unique_original_files':len(records),'original_files_modified_by_this_audit':False,
        'scope':'Local original paths recorded by the three source manifests; field frozen pins are checked by its mathematical verifier.',
        'files':records}
(HERE/'originals_audit.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','original_files_unchanged':len(records)}))
