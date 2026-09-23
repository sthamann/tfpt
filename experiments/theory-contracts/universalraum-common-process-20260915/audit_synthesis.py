"""Read-only-source audit of the supplied synthesis and isolated package replay."""
from pathlib import Path, PurePosixPath
from hashlib import sha256
from zipfile import ZipFile
import json
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent

def main():
    pins = json.loads((HERE/'sources_manifest.json').read_text())
    for name, info in pins.items():
        if sha256((HERE/'sources'/name).read_bytes()).hexdigest() != info['sha256']:
            raise RuntimeError('Changed frozen source: '+name)
    manifest = json.loads((HERE/'sources/synthesis_sources.json').read_text())
    protocol = json.loads((HERE/'sources/synthesis_protocol.json').read_text())
    local = {'md':'synthesis.md','pdf':'synthesis.pdf'}
    for ext, name in local.items():
        expected = protocol['deliverables_sha256']['TFPT_Universalraum_Forschungspaper_2026-09-15.'+ext]
        if pins[name]['sha256'] != expected:
            raise RuntimeError('Delivered '+ext+' disagrees with protocol')
    runs = []
    with ZipFile(HERE/'sources/synthesis_package.zip') as z:
        names = z.namelist()
        if len(set(names)) != len(names):
            raise RuntimeError('Duplicate archive path')
        for item in z.infolist():
            p = PurePosixPath(item.filename)
            if p.is_absolute() or '..' in p.parts or (item.external_attr >> 16) & 0o170000 == 0o120000:
                raise RuntimeError('Unsafe archive member')
        for entry in manifest:
            data = z.read(entry['snapshot'])
            if len(data) != entry['bytes'] or sha256(data).hexdigest() != entry['sha256']:
                raise RuntimeError('Source manifest failure '+entry['id'])
        for filename, digest in protocol['deliverables_sha256'].items():
            if sha256(z.read('outputs/'+filename)).hexdigest() != digest:
                raise RuntimeError('Packaged output failure '+filename)
        if json.loads(z.read('outputs/Quellenmanifest.json')) != manifest:
            raise RuntimeError('Different packaged source manifest')
        s074 = next(e for e in manifest if e['id']=='S074')
        if s074['sha256'] != pins['baseline_v167.md']['sha256']:
            raise RuntimeError('S074 is not this thread full latest v1.6.7')
        with tempfile.TemporaryDirectory(prefix='tfpt-synthesis-replay-') as td:
            root=Path(td)
            z.extractall(root)
            specifications = [
                ('work/verify_connections.py','work/connections_normal.json',57,'exact_conditions'),
                ('work/v167_replay/verify_hamilton_chain.py','work/v167_replay/replayed.json',20,'exact_checks'),
            ]
            for script, saved, count, key in specifications:
                raw=[]
                for optimized in (False,True):
                    command=[sys.executable]+(['-OO'] if optimized else [])+['-W','error',str(root/script)]
                    proc=subprocess.run(command,capture_output=True,timeout=240,cwd=root)
                    if proc.returncode:
                        raise RuntimeError(script+' failed: '+proc.stderr.decode(errors='replace'))
                    result=json.loads(proc.stdout)
                    if result['status']!='PASS' or result[key]!=count:
                        raise RuntimeError('Unexpected replay contract '+script)
                    if proc.stdout!=(root/saved).read_bytes():
                        raise RuntimeError('Output differs from supplied saved result '+script)
                    raw.append(proc.stdout)
                if raw[0]!=raw[1]:raise RuntimeError('Optimization changed result')
                runs.append({'script':script,'sha256':sha256((root/script).read_bytes()).hexdigest(),
                             'checks':count,'normal_optimized_byte_identical':True,
                             'matches_supplied_result_bytes':True})
    result={'status':'PASS','source_count':len(manifest),'all_frozen_source_hashes_match':True,
            'supplied_md_pdf_tex_hashes_match':True,'S074_matches_full_v167':True,
            'source_read_scope':'Full 1065-line synthesis text; selected derivations audited, not every historical source re-proved.',
            'runs':runs,'inherited_822_suite_rerun':False,'large_native_ground_proof_rerun':False,
            'formal_proof_assistant_verification':False,'T1_T8_closed':[]}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
