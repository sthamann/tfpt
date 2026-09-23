from copy import deepcopy
import contextlib
import io
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

import record_portability as p
import run_consolidation_20260909 as runner


class RecordPortabilityTests(unittest.TestCase):
    def metadata(self, root):
        return {"source": str(Path(root)/p.SOURCE), "source_sha256": p.SOURCE_SHA,
                "prefix_sha256": "unchanged-prefix", "source_checks": 5, "closed": False}

    def test_only_the_known_verified_root_is_canonicalized(self):
        expected = self.metadata(p.ORIGINAL_ROOT)
        observed = self.metadata(p.ROOT)
        a, b = p.portable_source_record(expected), p.portable_source_record(observed)
        self.assertEqual(a, b)
        self.assertEqual(a["source"], p.SOURCE)
        self.assertEqual(expected["source"], str(p.ORIGINAL_ROOT/p.SOURCE))
        self.assertEqual(a["prefix_sha256"], expected["prefix_sha256"])

    def test_wrong_path_and_hash_fail_closed(self):
        for key, value in (("source", "/elsewhere/"+p.SOURCE),
                           ("source", str(p.ROOT/"different.py")),
                           ("source_sha256", "0"*64)):
            data = self.metadata(p.ROOT)
            data[key] = value
            with self.assertRaises(ValueError):
                p.portable_source_record(data)

    def test_changed_source_bytes_fail_closed(self):
        with patch.object(Path, "read_bytes", return_value=b"mutated source"):
            with self.assertRaisesRegex(ValueError, "source bytes"):
                p.portable_source_record(self.metadata(p.ROOT))

    def test_all_mathematical_and_scope_fields_remain_exact(self):
        for key, value in (("prefix_sha256", "changed"), ("source_checks", 4),
                           ("closed", True), ("eigenvalue", 1.0000000000000002)):
            original = self.metadata(p.ROOT)
            changed = dict(original, **{key: value})
            self.assertNotEqual(p.portable_source_record(original), p.portable_source_record(changed))

    def test_nested_records_without_changing_unrelated_paths(self):
        record = {"source": self.metadata(p.ROOT), "rows": [self.metadata(p.ROOT)],
                  "unrelated_file": "/do/not/normalize"}
        changed = p.portable_source_record(record)
        self.assertEqual(changed["source"]["source"], p.SOURCE)
        self.assertEqual(changed["rows"][0]["source"], p.SOURCE)
        self.assertEqual(changed["unrelated_file"], record["unrelated_file"])

    def certificate(self, value=2.):
        return {"rows": [{"N": 8, "r": 1, "PH_identity_residual": 0.,
                          "opposite_holonomy_operator_difference": value, "zero_modes": 0}],
                "selected": False}

    def test_only_valid_roundoff_is_normalized(self):
        a, b = self.certificate(2.), self.certificate(2.0000000000000004)
        self.assertNotEqual(a, b)  # Reproduces the old bitwise-replay failure.
        self.assertEqual(p.carrier_source_record(a), p.carrier_source_record(b))
        self.assertEqual(b["rows"][0]["opposite_holonomy_operator_difference"], 2.0000000000000004)

    def test_tolerance_cannot_hide_a_failed_source_bound(self):
        for value in (2.000001, float("nan"), float("inf"), -2., True):
            with self.assertRaises(ValueError):
                p.carrier_source_record(self.certificate(value))
        bad = self.certificate()
        bad["rows"][0]["PH_identity_residual"] = 1e-10
        with self.assertRaises(ValueError):
            p.carrier_source_record(bad)

    def test_other_certificate_values_compare_unchanged(self):
        original = self.certificate()
        changed = deepcopy(original)
        changed["rows"][0]["zero_modes"] = 2
        self.assertNotEqual(p.carrier_source_record(original), p.carrier_source_record(changed))
        changed = dict(original, selected=True)
        self.assertNotEqual(p.carrier_source_record(original), p.carrier_source_record(changed))

    def test_failed_child_traceback_is_visible_without_a_json_artifact(self):
        failure = "FAIL: sentinel mathematical mutation\nRan 1 test in 0.001s\nFAILED\n"
        process = subprocess.CompletedProcess([], 1, "", failure)
        output = io.StringIO()
        with patch.object(runner.subprocess, "run", return_value=process), contextlib.redirect_stdout(output):
            row = runner.run_one(("normal", runner.TEST_FILES[0], False, 30))
        self.assertFalse(row["passed"])
        self.assertEqual(row["transcript"], failure)
        self.assertIn("sentinel mathematical mutation", output.getvalue())


if __name__ == "__main__":
    unittest.main()
