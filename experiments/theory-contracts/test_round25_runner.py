"""Portable isolated fixtures; never opens or edits real repo manifests."""
import contextlib
from copy import deepcopy
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


RUNNER = Path(__file__).with_name('run_round25.py').resolve()
spec = importlib.util.spec_from_file_location('round25_runner_under_test', RUNNER)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='round25-manifest-fixtures-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.here = self.root/'experiments/theory-contracts'
        self.contracts = {'alpha':['check.py'], 'beta':['check.py']}
        self.inputs = ['seed/README.md', 'ROUND25_STATUS.md']
        self.prereqs = ['seed/prerequisite.py']
        self.patch = patch.multiple(runner, ROOT=self.root, HERE=self.here,
                                    CONTRACTS=self.contracts, INPUTS=self.inputs,
                                    PREREQUISITES=self.prereqs)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        files = {'run_round25.py':'# fixture runner provenance\n',
                 'seed/README.md':'# prerequisite proof\n',
                 'ROUND25_STATUS.md':'# bounded fixture status\n',
                 'seed/prerequisite.py':'print("fixture prerequisite")\n'}
        for name in self.contracts:
            files[name+'/README.md'] = '# fixture proof\n'
            files[name+'/check.py'] = 'print("fixture check")\n'
        for relative, content in files.items():
            path = self.here/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        for relative in runner.ROOT_INPUTS:
            native = self.root/relative
            native.parent.mkdir(parents=True, exist_ok=True)
            native.write_text('# fixture native prerequisite\n')
        self.singles = {}
        for name, scripts in self.contracts.items():
            self.singles[name] = {
                'schema':'tfpt.round25.contract-validation.v1', 'status':'PASS',
                'artifacts':[runner.digest(p) for p in runner.artifact_paths(name)],
                'audited_inputs':[runner.digest(p) for p in runner.audited_paths()],
                'runs':[self.run_record(self.here/name/script) for script in scripts]}
        self.overall = {'schema':'tfpt.round25.research-validation.v1', 'status':'PASS',
                        'contracts':deepcopy(self.singles),
                        'prerequisite_runs':[self.run_record(self.here/p) for p in self.prereqs]}
        self.save()

    def run_record(self, path):
        return {**runner.digest(path), 'command':[sys.executable,'-B',runner.relative(path)],
                'exit_code':0, 'assertions_enabled':True, 'python_optimize':'0',
                'stdout':'{"status":"PASS"}', 'stderr':'',
                'structured_output':{'status':'PASS'}}

    def save(self, sync=True):
        if sync:
            self.overall['contracts'] = deepcopy(self.singles)
        for name, record in self.singles.items():
            (self.here/name/'validation.json').write_text(json.dumps(record))
        (self.here/runner.OVERALL_NAME).write_text(json.dumps(self.overall))

    def validate(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = runner.check_manifests()
        return code,json.loads(output.getvalue())

    def failed(self, fragment):
        code, record = self.validate()
        self.assertEqual(code,1)
        self.assertEqual(record['status'],'FAIL')
        self.assertTrue(any(fragment in e for e in record['errors']),record)

    def test_complete_consistent_fixture_passes(self):
        code, record = self.validate()
        self.assertEqual((code,record['status']),(0,'PASS'))

    def pinned_fixture(self):
        spec = importlib.util.spec_from_file_location('r25_pins', RUNNER.parent/'round25_algebra.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name in module.PINS:
            path = self.here/name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((RUNNER.parent/name).read_bytes())
        return module.PINS

    def consumers_reject(self, name):
        for folder in ('moving-history-memory-round25', 'history-determinant-solver-round25'):
            with self.subTest(folder=folder, changed=name):
                proc = subprocess.run([sys.executable, '-OO', '-B',
                    str(RUNNER.parent/folder/'checker.py'), '--input-root', str(self.here)],
                    cwd=self.root, text=True, capture_output=True, timeout=30)
                self.assertEqual(proc.returncode, 1)
                self.assertIn('pinned input missing or changed: '+name, proc.stderr)

    def test_every_changed_pin_is_rejected_by_both_consumers_under_optimization(self):
        for name in self.pinned_fixture():
            path = self.here/name
            original = path.read_bytes()
            path.write_bytes(original+b'\n# isolated provenance mutation\n')
            self.consumers_reject(name)
            path.write_bytes(original)

    def test_every_missing_pin_is_rejected_by_both_consumers_under_optimization(self):
        for name in self.pinned_fixture():
            path = self.here/name
            original = path.read_bytes()
            path.unlink()
            self.consumers_reject(name)
            path.write_bytes(original)

    def test_actual_ward_mutation_rejected_before_execution(self):
        self.pinned_fixture()
        name = 'free-scalar-3d/free_scalar_ward.py'
        path = self.here/name
        path.write_text(path.read_text() + "\nraise RuntimeError('MUTANT_EXECUTED')\n")
        self.consumers_reject(name)

    def checker_mutant(self, folder, old, new, expected_error, mutate_common=False):
        source_path = RUNNER.parent/('round25_algebra.py' if mutate_common else folder+'/checker.py')
        source = source_path.read_text()
        self.assertEqual(source.count(old), 1)
        checker = self.here/folder/'checker.py'
        checker.parent.mkdir(parents=True, exist_ok=True)
        checker.write_bytes((RUNNER.parent/folder/'checker.py').read_bytes())
        (self.here/'round25_algebra.py').write_bytes((RUNNER.parent/'round25_algebra.py').read_bytes())
        target = self.here/'round25_algebra.py' if mutate_common else checker
        target.write_text(source.replace(old, new))
        proc = subprocess.run([sys.executable, '-OO', '-B', str(checker),
                               '--input-root', str(RUNNER.parent)],
                              cwd=self.root, text=True, capture_output=True, timeout=90)
        self.assertEqual(proc.returncode, 1)
        self.assertIn('AssertionError: '+expected_error, proc.stderr)

    def test_periodic_images_mutant_is_rejected(self):
        self.checker_mutant("moving-history-memory-round25",
            "return delta*(q**r+q**(count-r))/(2*sinh*(1-q**count))",
            "return delta*q**min(r,count-r)/(2*sinh)",
            "T3: periodic images give the exact Green inverse", True)

    def test_two_sided_tail_mutant_is_rejected(self):
        self.checker_mutant("moving-history-memory-round25",
            "return delta*q**(radius+1)/(sinh*(1-q)*(1-q**count))",
            "return delta*q**(radius+1)/(2*sinh*(1-q)*(1-q**count))",
            "T3 R0: tail dominates exact two-sided cyclic row sum", True)

    def test_two_delta_factors_mutant_is_rejected(self):
        self.checker_mutant("moving-history-memory-round25",
            "return delta**2*coupling_norm**2*tail",
            "return delta*coupling_norm**2*tail",
            "Schur error retains both delta coupling factors", True)

    def test_cyclic_distance_mutant_is_rejected(self):
        self.checker_mutant("moving-history-memory-round25",
            "distance=min(abs(j-k),count-abs(j-k))",
            "distance=abs(j-k)",
            "T5 R1: tail dominates exact two-sided cyclic row sum", True)

    def test_periodic_determinant_mutant_is_rejected(self):
        self.checker_mutant("history-determinant-solver-round25",
            "self.determinant=s.prod(P.det() for P in self.pivots)*self.H.det()",
            "self.determinant=s.prod(P.det() for P in self.pivots)",
            "noncommuting5: recursive determinant equals the independent dense determinant", True)

    def test_ordered_periodic_solve_mutant_is_rejected(self):
        self.checker_mutant("history-determinant-solver-round25",
            "return open_result-self.F*self.H_inverse*self.R*self.U.T*open_result",
            "return open_result-self.F*self.R*self.H_inverse*self.U.T*open_result",
            "noncommuting5: periodic solve has exactly zero dense residual", True)

    def test_signed_energy_updates_mutant_is_rejected(self):
        self.checker_mutant("history-determinant-solver-round25",
            "V=s.diag(*diagonal_changes)",
            "V=s.diag(*[abs(v) for v in diagonal_changes])",
            "signed low-rank update retains the actual determinant ratio", True)

    def test_pivot_time_normalization_mutant_is_rejected(self):
        self.checker_mutant("history-determinant-solver-round25",
            "pivot-=self.t**2*self.inverses[-1]",
            "pivot-=self.t*self.inverses[-1]",
            "noncommuting5: recursive determinant equals the independent dense determinant", True)

    def test_continuum_prefactor_mutant_is_rejected(self):
        self.checker_mutant("moving-history-memory-round25",
            "prefactor=s.limit(x**2/(sh*(1-qq)),x,0,dir='+')",
            "prefactor=2*s.limit(x**2/(sh*(1-qq)),x,0,dir='+')",
            "physical-time limit counts the two directions exactly once", False)

    def test_empty_audited_inputs_fails(self):
        self.singles['alpha']['audited_inputs'] = []
        self.save()
        self.failed('alpha/audited_inputs: inventory mismatch')

    def test_determinant_memory_cannot_be_set_to_zero(self):
        self.checker_mutant('moving-history-memory-round25',
            'return -delta**2*inverse[i,k]*inverse[k,i]',
            'return s.Integer(0)',
            'mixed log determinant keeps its sign and squared inverse response', True)

    def test_duplicate_audited_input_fails(self):
        self.singles['alpha']['audited_inputs'].append(deepcopy(self.singles['alpha']['audited_inputs'][0]))
        self.save()
        self.failed('duplicate path')

    def test_changed_input_hash_fails(self):
        (self.here/'seed/README.md').write_text('# changed after validation\n')
        self.failed('changed hash')

    def test_stale_aggregate_contract_fails(self):
        self.overall['contracts']['alpha']['stale_extra'] = True
        self.save(sync=False)
        self.failed('stale/different contract record alpha')

    def test_failed_prerequisite_cannot_hide_under_overall_pass(self):
        self.overall['prerequisite_runs'][0]['exit_code'] = 7
        self.save()
        self.failed('prerequisite_runs: run did not pass')

    def test_missing_prerequisite_fails(self):
        self.overall['prerequisite_runs'] = []
        self.save()
        self.failed('prerequisite_runs: inventory mismatch')

    def test_failed_contract_status_fails_even_with_zero_exit(self):
        self.singles['alpha']['status'] = 'FAIL'
        self.save()
        self.failed('alpha: recorded status is not PASS')

    def test_failed_contract_run_cannot_hide_under_pass(self):
        self.singles['alpha']['runs'][0]['exit_code'] = 1
        self.save()
        self.failed('alpha/runs: run did not pass')

    def test_explicit_json_failure_cannot_hide_behind_zero_exit(self):
        record = self.singles['alpha']['runs'][0]
        record['stdout'] = '{"status":"FAIL"}'
        record.pop('structured_output')
        self.save()
        self.failed('alpha/runs: run did not pass')

    def test_stale_structured_output_fails(self):
        self.singles['alpha']['runs'][0]['structured_output'] = {'status':'FAIL'}
        self.save()
        self.failed('alpha/runs: run did not pass')

    def test_unittest_non_json_output_is_allowed(self):
        record = self.singles['alpha']['runs'][0]
        record['stdout'] = ''
        record['stderr'] = 'Ran 2 tests\nOK\n'
        record.pop('structured_output')
        self.save()
        self.assertEqual(self.validate()[0],0)

    def test_malformed_records_fail_without_traceback(self):
        self.singles['alpha']['runs'] = [None, {'path':[]}, {'path':'../escape','sha256':'x'}]
        self.singles['beta']['audited_inputs'] = None
        self.save()
        self.failed('expected object')

    def test_non_object_manifest_fails(self):
        (self.here/'alpha/validation.json').write_text('[]')
        self.failed('expected JSON object')

    def test_stale_run_hash_fails(self):
        self.singles['alpha']['runs'][0]['sha256'] = '0'*64
        self.save()
        self.failed('alpha/runs: changed hash')

    def test_overall_failure_flag_fails(self):
        self.overall['status'] = 'FAIL'
        self.save()
        self.failed('recorded status is not PASS')

    def test_changed_prerequisite_is_an_audited_input(self):
        (self.here/'seed/prerequisite.py').write_text('# changed code\n')
        code, record = self.validate()
        self.assertEqual(code,1)
        self.assertTrue(any('audited_inputs: changed hash' in e and 'prerequisite.py' in e
                            for e in record['errors']))

    def test_optimized_environment_cannot_disable_child_assertions(self):
        path = self.here/'alpha/check.py'
        path.write_text("assert False, 'ASSERTION_SENTINEL'\n")
        for inherited in ['1','2']:
            with self.subTest(PYTHONOPTIMIZE=inherited), patch.dict(os.environ,{'PYTHONOPTIMIZE':inherited}):
                record = runner.run_one(path)
            self.assertEqual(record['exit_code'],1)
            self.assertIn('AssertionError: ASSERTION_SENTINEL',record['stderr'])
            self.assertEqual(record['python_optimize'],'0')
            self.assertFalse(runner.run_succeeded(record))

    def test_child_reports_debug_true_under_optimized_environment(self):
        path = self.here/'alpha/check.py'
        path.write_text("import json\nprint(json.dumps({'status':'PASS','debug':__debug__}))\n")
        with patch.dict(os.environ,{'PYTHONOPTIMIZE':'2'}):
            record = runner.run_one(path)
        self.assertTrue(runner.run_succeeded(record))
        self.assertIs(record['structured_output']['debug'],True)

    def test_cli_malformed_record_is_error_exit_not_traceback(self):
        (self.here/'alpha/validation.json').write_text('{"runs":null}')
        code = ("import importlib.util,pathlib; "
                f"s=importlib.util.spec_from_file_location('rr',{str(RUNNER)!r}); "
                "m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
                f"m.ROOT=pathlib.Path({str(self.root)!r}); m.HERE=pathlib.Path({str(self.here)!r}); "
                f"m.CONTRACTS={self.contracts!r}; m.INPUTS={self.inputs!r}; m.PREREQUISITES={self.prereqs!r}; "
                "raise SystemExit(m.main())")
        proc = subprocess.run([sys.executable,'-B','-c',code,'--check-manifests'],
                              text=True,capture_output=True)
        self.assertEqual(proc.returncode,1)
        self.assertEqual(json.loads(proc.stdout)['status'],'FAIL')
        self.assertNotIn('Traceback',proc.stderr+proc.stdout)


if __name__ == '__main__':
    unittest.main()
