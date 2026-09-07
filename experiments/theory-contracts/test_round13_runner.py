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


RUNNER = Path(__file__).with_name('run_round13.py').resolve()
spec = importlib.util.spec_from_file_location('round13_runner_under_test', RUNNER)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='round13-manifest-fixtures-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.here = self.root/'experiments/theory-contracts'
        self.contracts = {'alpha':['check.py'], 'beta':['check.py']}
        self.inputs = ['seed/README.md', 'ROUND13_STATUS.md']
        self.prereqs = ['seed/prerequisite.py']
        self.patch = patch.multiple(runner, ROOT=self.root, HERE=self.here,
                                    CONTRACTS=self.contracts, INPUTS=self.inputs,
                                    PREREQUISITES=self.prereqs)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        files = {'run_round13.py':'# fixture runner provenance\n',
                 'seed/README.md':'# prerequisite proof\n',
                 'ROUND13_STATUS.md':'# bounded fixture status\n',
                 'seed/prerequisite.py':'print("fixture prerequisite")\n'}
        for name in self.contracts:
            files[name+'/README.md'] = '# fixture proof\n'
            files[name+'/check.py'] = 'print("fixture check")\n'
        for relative, content in files.items():
            path = self.here/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        native = self.root/'verification/v1035_matter_coupling.py'
        native.parent.mkdir(parents=True)
        native.write_text('# fixture native prerequisite\n')
        self.singles = {}
        for name, scripts in self.contracts.items():
            self.singles[name] = {
                'schema':'tfpt.round13.contract-validation.v1', 'status':'PASS',
                'artifacts':[runner.digest(p) for p in runner.artifact_paths(name)],
                'audited_inputs':[runner.digest(p) for p in runner.audited_paths()],
                'runs':[self.run_record(self.here/name/script) for script in scripts]}
        self.overall = {'schema':'tfpt.round13.research-validation.v1', 'status':'PASS',
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

    def test_empty_audited_inputs_fails(self):
        self.singles['alpha']['audited_inputs'] = []
        self.save()
        self.failed('alpha/audited_inputs: inventory mismatch')

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
