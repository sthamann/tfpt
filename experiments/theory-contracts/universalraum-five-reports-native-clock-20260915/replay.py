"""Reproduce both audits without changing received reports or foreign files."""
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
DOCS=Path('/Users/stefanhamann/Documents')
REPORT_PINS={
    'results_15_sol.md':'a76e862f3bd6d2ed5e2d920bcdbb3e3ec1f8edc887704cea220e63eca80d3ea1',
    'results_15_opus.md':'948771b957aecb11fac01da866b3416eb7fb35ee26ae60cff8974507a10d1817',
    'results_15_kimi1.md':'c2b859657b5bb9ef646391b88e620048ca894abc892b4ba3d45ee4af273a6cb1',
    'results_15_kimi2.md':'5b904934b8b55e585fb40375af2cb1c07cb758e3cdef9e88afc2a19cf2696cc8',
    'results_15_fable.md':'fbd956c5a2b100ae469354a1de1a3fda7084a32797bd1bac05b4bdf91a8cc299',
}
carrier=ROOT/'experiments/theory-contracts/universalraum-carrier-hand-20260915/carrier_hand.py'
inputs=[DOCS/name for name in REPORT_PINS]+[
    carrier,
    ROOT/'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs/native_common.py',
    ROOT/'experiments/theory-contracts/compiler-involution-types/checker.py',
    ROOT/'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz',
    ROOT/'experiments/theory-contracts/universalraum-native-exterior-reset-20260915/normal.json',
    ROOT/'experiments/theory-contracts/universalraum-native-exterior-reset-20260915/ground_replay/weak_coupling_ground_normal.json',
    HERE/'verify_native_clock.py',HERE/'verify_moment_bridge.py',HERE/'replay.py',
]


def hashes():
    return {str(p):sha256(p.read_bytes()).hexdigest() for p in inputs}


def run():
    initial=hashes()
    for name,digest in REPORT_PINS.items():
        if initial[str(DOCS/name)]!=digest:raise RuntimeError('received report changed: '+name)
    if initial[str(carrier)]!='f11d0c097bbbbf8d70284a1584566b3a35d486459ddb82bfcd72c8f7ae129fcf':
        raise RuntimeError('received carrier code changed')
    records=[]
    for title,path in [('native',HERE/'verify_native_clock.py'),('moment_bridge',HERE/'verify_moment_bridge.py'),('received_carrier',carrier)]:
        outputs=[]
        for mode,flags in [('normal',[]),('optimized',['-OO'])]:
            child=subprocess.run([sys.executable,*flags,str(path)],cwd=ROOT,capture_output=True,text=True)
            (HERE/(title+'_'+mode+'.stdout.txt')).write_text(child.stdout)
            (HERE/(title+'_'+mode+'.stderr.txt')).write_text(child.stderr)
            if child.returncode:raise RuntimeError(title+' '+mode+' failed: '+child.stderr)
            parsed=json.loads(child.stdout)
            if parsed.get('status')!='PASS':raise RuntimeError(title+' did not PASS')
            encoded=json.dumps(parsed,indent=2,sort_keys=True)+'\n'
            (HERE/(title+'_'+mode+'.json')).write_text(encoded)
            outputs.append(encoded)
            records.append({'title':title,'mode':mode,'exit_code':child.returncode,
                'sha256':sha256(encoded.encode()).hexdigest(),
                'reported_checks':parsed.get('check_count',parsed.get('exact_checks'))})
            print(title+' '+mode+' PASS',flush=True)
        if outputs[0]!=outputs[1]:raise RuntimeError(title+' normal / optimized mismatch')
    if initial!=hashes():raise RuntimeError('source changed while audit ran')
    result={'status':'PASS','runs':records,'normal_optimized_byte_identical':True,
        'input_hashes_before_and_after':initial,
        'received_carrier_warning':'26 reported checks include numpy.poly/allclose floating checks; replay does not certify the physical prose',
        'native_ground_note':'Previously replayed exact certificate inspected and pinned here, not independently rerun in this receipt.',
        'physical_source_selected':False,'TOE_complete':False}
    (HERE/'replay.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':run()
