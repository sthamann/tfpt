"""One-time immutable freeze of the two additional user attachments and probes."""
from pathlib import Path
from hashlib import sha256
import json
import shutil

HERE = Path(__file__).resolve().parent
target = HERE / 'late_sources_manifest.json'
if target.exists():
    raise RuntimeError('Late source manifest already exists; refusing overwrite')
items = {
    'sources/user_late_fundamental.txt': Path('/Users/stefanhamann/.codex/attachments/8e110ae1-19e2-4d47-bfc8-ebe4fe9ab81b/pasted-text.txt'),
    'sources/user_late_native.txt': Path('/Users/stefanhamann/.codex/attachments/b928b72a-6669-4c67-a75d-124095791c6f/pasted-text.txt'),
}
root = HERE.parent / 'universalraum-fundamental-20260915'
for name in ('t1_fixed.py', 'stabilizer.py', 't5_twobank.py', 't5_varresp.py', 'README.md'):
    items['late_sources/' + name] = root / name
manifest = []
for relative, source in items.items():
    data = source.read_bytes()
    out = HERE / relative
    out.parent.mkdir(exist_ok=True, parents=True)
    if out.exists() and out.read_bytes() != data:
        raise RuntimeError('Existing late copy differs: ' + relative)
    if not out.exists():
        shutil.copy2(source, out)
    manifest.append({'copy': relative, 'original': str(source), 'sha256': sha256(data).hexdigest()})
target.write_text(json.dumps(manifest, indent=2) + '\n')
