"""Freshness and attribution regressions, not a mathematical proof. NO RH CLAIM."""
import json
from pathlib import Path
import tempfile
import unittest

import sync_research as sync
import build_catalog as catalog
from analysis.analyze_paths import t5_conflicts


class SourceFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.group = self.root / "research/example"
        self.group.mkdir(parents=True)
        (self.group / "README.md").write_text("# A source report\nNo RH proof\n")
        (self.group / "result.json").write_text('{"status":"diagnostic"}')
        self.config = {"roots": [{"id": "test", "path": str(self.root), "sections": ["research"]}],
                       "excluded_components": ["__pycache__"], "primary_overrides": {}}

    def scan(self):
        return sync.discover(self.config)

    def test_identical_scan_is_stable(self):
        self.assertEqual(sync.compare_sources(self.scan(), self.scan()), [])

    def test_new_file_invalidates_snapshot(self):
        old = self.scan()
        (self.group / "new_negative.md").write_text("counterexample")
        self.assertTrue(any(x.startswith("NEW_SOURCE:") for x in sync.compare_sources(old, self.scan())))

    def test_changed_file_invalidates_snapshot(self):
        old = self.scan()
        (self.group / "result.json").write_text('{"status":"changed"}')
        self.assertTrue(any(x.startswith("CHANGED_SOURCE:") for x in sync.compare_sources(old, self.scan())))

    def test_missing_file_invalidates_snapshot(self):
        old = self.scan()
        (self.group / "result.json").unlink()
        self.assertTrue(any(x.startswith("MISSING_SOURCE:") for x in sync.compare_sources(old, self.scan())))

    def test_missing_workspace_fails(self):
        self.config["roots"][0]["path"] = str(self.root / "missing")
        with self.assertRaisesRegex(ValueError, "SOURCE_UNAVAILABLE"):
            self.scan()

    def test_no_auto_proof_promotion(self):
        record = sync.draft_records(self.scan())[0]
        self.assertTrue(record["draft"] and record["needs_review"])
        self.assertEqual(record["outcome"], "OPEN")
        self.assertEqual(record["result_verdict"], "DISCOVERED_NOT_REVIEWED")

    def test_one_group_not_one_parameter_node(self):
        for i in range(10):
            (self.group / f"trial_{i}.json").write_text("{}")
        snap = self.scan()
        self.assertEqual(len(snap["files"]), 12)
        self.assertEqual(len(sync.draft_records(snap)), 1)

    def test_frozen_sources_are_preserved_in_history(self):
        p = self.group / "frozen/old.py"
        p.parent.mkdir()
        p.write_text("historical = True")
        self.assertIn(str(p), self.scan()["files"])

    def test_review_pins_invalidate_on_changed_dependency(self):
        old = self.scan()
        pins = {k: {"digest": g["digest"]} for k, g in old["groups"].items()}
        self.assertEqual(sync.review_drift(old, pins), [])
        (self.group / "result.json").write_text("{}")
        self.assertTrue(sync.review_drift(self.scan(), pins))

    def test_bad_primary_fails(self):
        self.config["primary_overrides"]["test:research/example"] = "missing.md"
        with self.assertRaisesRegex(ValueError, "MISSING_PRIMARY"):
            self.scan()

    def test_schema_valid_discovery_records(self):
        taxonomy = sync.read(sync.HERE / "taxonomy.json")
        record = sync.draft_records(self.scan())[0]
        self.assertEqual(catalog.validate_record(record, taxonomy, catalog.schema_enums_from_taxonomy(taxonomy)), [])

    def test_contracts_cannot_self_accept(self):
        data = sync.read(sync.HERE / "analysis/research_followups_20260909.json")
        self.assertFalse(data["automatic_acceptance"])
        self.assertFalse(data["navigation_paths_are_proofs"])
        for contract in data["contracts"]:
            self.assertEqual(contract["status"], "OPEN")
            self.assertEqual(contract["premise_logic"], "ALL_REQUIRED")
            self.assertTrue(all(g["status"] == "OPEN" for g in contract["requires"]))

    def test_original_results_do_not_depend_on_future_contract(self):
        records = sync.read(sync.HERE / "fragments/part_20.json")
        for record in records:
            if Path(record["path"]).is_absolute():
                self.assertNotIn("rh/catalog/analysis/research_followups_20260909.md", record["depends_on"])

    def test_unrelated_readmes_are_not_one_conflicting_object(self):
        a = {"path": "/campaign/a/README.md", "outcome": "MEASURED", "role": "external_research_group"}
        b = {"path": "/campaign/b/README.md", "outcome": "RESTATED", "role": "external_research_group"}
        self.assertEqual(t5_conflicts([a, b]), [])

    def test_shared_ledger_conflicts_are_not_suppressed(self):
        a = {"path": "/campaign/a/README.md", "outcome": "MEASURED", "ledger_ids": ["SAME.CLAIM"]}
        b = {"path": "/campaign/b/README.md", "outcome": "KILLED", "ledger_ids": ["SAME.CLAIM"]}
        self.assertTrue(t5_conflicts([a, b]))


if __name__ == "__main__":
    unittest.main()
