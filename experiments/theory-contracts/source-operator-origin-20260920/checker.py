"""Reproduce bounded source-origin gates; no physical completion promotion."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')

def main():
    pins=json.loads((HERE/'source_manifest.json').read_text())['sources']
    for name,digest in pins.items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
            raise RuntimeError('source drift: '+name)
    entries=[('rotor_audit','check_rotor_audit.py'),
             ('family_intertwiner','check_family_intertwiner.py'),
             ('glue_correspondence','checker.py')]
    records={}
    for folder,script in entries:
        results=[]
        for flags in ([],['-OO']):
            proc=subprocess.run([sys.executable,'-B',*flags,str(HERE/folder/script)],
                                text=True,capture_output=True,check=True)
            if folder=='rotor_audit':
                obj=json.loads(proc.stdout)
                raw=(json.dumps(obj,sort_keys=True,indent=2)+'\n').encode()
                (HERE/folder/('certificate.optimized.json' if flags else 'certificate.json')).write_bytes(raw)
            else:
                raw=(HERE/folder/'certificate.json').read_bytes()
                obj=json.loads(raw)
            results.append(raw)
        if results[0]!=results[1]:
            raise RuntimeError('normal versus optimized mismatch: '+folder)
        records[folder]={'normal_optimized_identical':True,
                         'checks':obj.get('checks_passed',obj.get('checks')),
                         'verdict':obj['verdict'],
                         'certificate_sha256':hashlib.sha256(results[0]).hexdigest()}
    f=json.loads((HERE/'family_intertwiner/certificate.json').read_text())
    if f['all_operator_obstruction']['equivariant_odd_vertex_image']!='zero, even for nonlinear composites or operator closures':
        raise RuntimeError('source algebra gate not carried')
    if f['clifford_source_probe']['physical_64CAR_operator_selected'] is not False:
        raise RuntimeError('helper Clifford promoted to physical source')
    r=json.loads((HERE/'rotor_audit/certificate.json').read_text())
    if r['source_projection']['low_energy_or_E_zero_elimination_specified'] is not False:
        raise RuntimeError('rotor projection scope changed')
    if r['joint_high_rotor_reduction']['controlled_rank_one_spectral_reduction'] is not True or r['joint_high_rotor_reduction']['multi_field_quartic_or_boundary_transfer'] is not False:
        raise RuntimeError('actual high-mass gap or rank-one boundary scope lost')
    out={'research_id':'UR.SOURCE.OPERATOR_ORIGIN.01','status':'PASS_SCOPED_REPLAY',
         'verdict':'PARTIAL','source_pins_verified':len(pins),'packages':records,
         'physical_gates_closed':[],'complete_TFPT_solution':False,
         'independent_review_scope':'linear and antilinear one-particle group obstruction only; subsequent universal center and Clifford tests proved and checked in parent'}
    (HERE/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
