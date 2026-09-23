"""Freeze the later user attachment and the limited RH source audit separately."""
from pathlib import Path
from hashlib import sha256
import json
import shutil

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCES = {
    'attachment_overlap.txt': Path('/Users/stefanhamann/.codex/attachments/59dc0059-8914-48ca-953d-85933f66e00b/pasted-text.txt'),
    'geometry_audit.md': REPO/'rh/catalog/analysis/geometry_audit.md',
    'event_log_function.md': REPO/'rh/catalog/analysis/event_log_function.md',
}
records = {}
for name, source in SOURCES.items():
    target = HERE/'late_sources'/name
    data = source.read_bytes()
    if target.exists() and target.read_bytes() != data:
        raise RuntimeError('Frozen addendum changed: '+name)
    target.parent.mkdir(exist_ok=True)
    if not target.exists():
        shutil.copy2(source, target)
    if target.read_bytes() != data or source.read_bytes() != data:
        raise RuntimeError('Source changed during copy')
    records['late_sources/'+name] = {'source': str(source), 'sha256': sha256(data).hexdigest()}
body = json.dumps(records, indent=2, sort_keys=True)+'\n'
manifest = HERE/'late_sources_manifest.json'
if manifest.exists() and manifest.read_text() != body:
    raise RuntimeError('Addendum manifest drift')
manifest.write_text(body)
print(json.dumps({'status':'PASS', 'frozen_addendum_files':len(records)}))
