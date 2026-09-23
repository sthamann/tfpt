"""Two bounded adversarial checks against the real freshly built Lean modules."""
import os
from pathlib import Path
import tempfile

from .common import DATA, HERE, dump, need, read, sha
from .kernel_audit import LEAN, ROOT, check_receipt, command, parse_audits

MISSING = '''import FrontierClosure
theorem missingFreq
    (hread : RHSeparatedTail20260905.EventuallySelectedReadLowerBound) :
    ∀ f : RH.GridElement, 0 ≤ RH.weilForm f := by
  exact (RHFrontierClosure20260905.eventual_bound_iff_weil_nonneg hread).mp hread
'''
ASSUMED = '''import FrontierClosure
axiom assumedFreq : RH.frequently_selected_augDualResolvent_ge_half
axiom assumedRead : RHSeparatedTail20260905.EventuallySelectedReadLowerBound
theorem fakePositivity : ∀ f : RH.GridElement, 0 ≤ RH.weilForm f :=
  (RHFrontierClosure20260905.eventual_bound_iff_weil_nonneg assumedFreq).mp assumedRead
#print axioms fakePositivity
'''


def run_controls():
    receipt = read(DATA / 'kernel_receipt.json')
    check_receipt(receipt, read(HERE / 'knowledge.json'))
    objects = Path(receipt['run_dir']) / 'objects'
    need(objects.is_dir(), 'FRESH_BUILD_OBJECTS_EXPIRED; run audit before these replay controls')
    paths = [objects, *sorted((ROOT / '.lake/packages').glob('*/.lake/build/lib/lean'))]
    env = dict(os.environ, LEAN_PATH=':'.join(map(str, paths)))
    tmp = Path(tempfile.mkdtemp(prefix='rh-lean-negative-controls-'))
    rows = []
    for name, source, expected in [('MissingFreq', MISSING, 1), ('AssumedFreq', ASSUMED, 0)]:
        path, log = tmp / (name + '.lean'), tmp / (name + '.log')
        path.write_text(source)
        code = command([LEAN, '-M', '8192', path], ROOT, env, log, 60)
        need(code == expected, 'LEAN_NEGATIVE_CONTROL_UNEXPECTED_EXIT: ' + str(log))
        content = log.read_text()
        if name == 'MissingFreq':
            need('Application type mismatch' in content and 'RH.frequently_selected_augDualResolvent_ge_half' in content,
                 'NEGATIVE_CONTROL_FAILED_FOR_WRONG_REASON')
            classification = 'MISSING_AND_PREMISE_REJECTED_BY_LEAN'
        else:
            audited = parse_audits(content)['fakePositivity']
            need({'assumedFreq', 'assumedRead'} <= set(audited['axioms']) and not audited['standard_only'],
                 'CUSTOM_ASSUMPTIONS_NOT_DETECTED')
            classification = 'COMPILES_BUT_AXIOM_GATE_REJECTS'
        rows.append({'name': name, 'exit_code': code, 'classification': classification,
                     'source': source, 'log': content})
    result = {'status': 'REAL_LEAN_NEGATIVE_CONTROLS_PASSED', 'RH_proved': False,
              'kernel_receipt_sha256': sha(DATA / 'kernel_receipt.json'),
              'control_code_sha256': sha(Path(__file__)), 'cases': rows,
              'temporary_work_dir': str(tmp)}
    dump(DATA / 'negative_controls.json', result)
    return result


def check_controls():
    result = read(DATA / 'negative_controls.json')
    need(result['status'] == 'REAL_LEAN_NEGATIVE_CONTROLS_PASSED', 'LEAN_CONTROLS_NOT_PASSED')
    need(result['kernel_receipt_sha256'] == sha(DATA / 'kernel_receipt.json'), 'LEAN_CONTROL_RECEIPT_STALE')
    need(result['control_code_sha256'] == sha(Path(__file__)), 'LEAN_CONTROL_CODE_CHANGED')
    return result
