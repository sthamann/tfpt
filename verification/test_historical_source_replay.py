"""Historical source compatibility is exact and fails closed on mutations."""
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import historical_source_replay as replay


@contextmanager
def fixture():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        manifest = json.loads((replay.ROOT / replay.MANIFEST).read_text())
        paths = {replay.MANIFEST, "documents/source_manifest.json", "build.sh"}
        for entry in manifest["inputs"]:
            if entry["kind"] != "frozen_external_historical_input":
                paths.add(entry.get("current_path", entry["path"]))
            if "snapshot" in entry: paths.add(entry["snapshot"])
            if entry["kind"] == "exact_modular_tex":
                doc = next(d for d in json.loads((replay.ROOT / "documents/source_manifest.json").read_text())["documents"]
                           if d["entry_point"] == entry["path"])
                paths.update(p["path"] for p in doc["source_modules"])
        for path in paths:
            out = root / path; out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(replay.ROOT / path, out)
        yield root, manifest


def change_and_repin_current(root, manifest, kind, transform):
    record = next(r for r in manifest["inputs"] if r["kind"] == kind)
    path = root / record["path"]
    current = transform(path.read_bytes()); path.write_bytes(current)
    record["current_sha256"] = hashlib.sha256(current).hexdigest()
    (root / replay.MANIFEST).write_text(json.dumps(manifest))


class HistoricalReplayTests(unittest.TestCase):
    def test_five_exact_declared_inputs_and_retained_status_projection(self):
        inputs, provenance = replay.historical_inputs()
        self.assertEqual(len(inputs), 5)
        self.assertEqual(provenance["ledger_projection"], [{"historical_rows":1194,
                         "current_retained_rows":788,"explicit_migration_rows":28,"statuses_unchanged":True}])
        for record in provenance["inputs"]:
            self.assertEqual(replay.digest(inputs[record["path"]]), record["historical_sha256"])
        self.assertFalse(provenance["checker_pins_modified"])

    def test_current_python_byte_mutation_fails_original_current_pin(self):
        with fixture() as (root, manifest):
            path = root / "verification/v1033_charged_disorder.py"
            path.write_bytes(path.read_bytes() + b"\n# unrelated mutation\n")
            with self.assertRaisesRegex(ValueError, "changed verification/v1033"):
                replay.historical_inputs(root)

    def test_scientific_mutation_fails_even_if_current_digest_is_recomputed(self):
        with fixture() as (root, manifest):
            change_and_repin_current(root, manifest, "reader_only_python_adapter",
                                     lambda b:b.replace(b"TX = SX / (2j) - SZ / 2", b"TX = SX / (2j) + SZ / 2"))
            with self.assertRaisesRegex(ValueError, "beyond the declared"):
                replay.historical_inputs(root)

    def test_reader_logic_change_fails_even_if_current_digest_is_recomputed(self):
        with fixture() as (root, manifest):
            change_and_repin_current(root, manifest, "reader_only_python_adapter",
                                     lambda b:b.replace(b'path.suffix == ".tex"',b'path.suffix != ".tex"'))
            with self.assertRaisesRegex(ValueError, "beyond the declared"):
                replay.historical_inputs(root)

    def test_unrelated_ledger_field_mutation_fails_exact_projection(self):
        with fixture() as (root, manifest):
            change_and_repin_current(root, manifest, "retained_ledger_projection",
                                     lambda b:b.replace(b"AX.P1.01",b"AX.P1.02",1))
            with self.assertRaisesRegex(ValueError, "ledger ownership/order"):
                replay.historical_inputs(root)

    def test_status_delta_cannot_be_declared_as_a_navigation_adapter(self):
        with fixture() as (root, manifest):
            record=next(r for r in manifest["inputs"]if r["kind"]=="retained_ledger_projection")
            record["explicit_migration_deltas"][0]["changes"]["status"]={"historical":"E","current":"C"}
            (root/replay.MANIFEST).write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,"status changes"):
                replay.historical_inputs(root)

    def test_changed_tex_module_fails_original_hash(self):
        with fixture() as (root, manifest):
            source=json.loads((root/"documents/source_manifest.json").read_text())
            doc=next(d for d in source["documents"]if d["entry_point"]=="articles/2026-08-30/mmst_charged_scaling_limit_en.tex")
            part=root/doc["source_modules"][0]["path"]
            part.write_bytes(part.read_bytes()+b"\n")
            with self.assertRaisesRegex(ValueError,"changed documents/"):
                replay.historical_inputs(root)

    def test_relocated_helper_mutation_fails_original_hash(self):
        with fixture() as (root, manifest):
            part=root/"experiments/theory-contracts/seam_source.py"
            part.write_bytes(part.read_bytes()+b"\n")
            with self.assertRaisesRegex(ValueError,"changed experiments/theory-contracts/seam_source.py"):
                replay.historical_inputs(root)

    def test_external_prime_historical_input_cannot_reappear_in_active_tree(self):
        with fixture() as (root, manifest):
            record=next(r for r in manifest["inputs"]if r["kind"]=="frozen_external_historical_input")
            path=root/record["path"];path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes((root/record["snapshot"]).read_bytes())
            with self.assertRaisesRegex(ValueError,"external historical probe restored"):
                replay.historical_inputs(root)

    def test_overlay_is_temporary_and_never_writes_current_inputs(self):
        with fixture() as (root, manifest):
            before=(root/"verification/v1033_charged_disorder.py").read_bytes()
            with replay.historical_overlay(root) as (overlay, provenance):
                saved=overlay
                self.assertNotEqual(overlay,root)
                self.assertEqual(replay.digest((overlay/"verification/v1033_charged_disorder.py").read_bytes()),
                                 manifest["inputs"][0]["historical_sha256"])
                self.assertTrue((overlay/"experiments/double-cover-rh-audit-2026-09-08/seam_source.py").is_file())
                self.assertTrue(provenance["temporary_copy_only"])
            self.assertFalse(saved.exists())
            self.assertEqual((root/"verification/v1033_charged_disorder.py").read_bytes(),before)
            self.assertFalse((root/"experiments/double-cover-rh-audit-2026-09-08/seam_source.py").exists())
            self.assertFalse((root/"experiments/tfpt-discovery/census_qsm_normflow_probe.py").exists())


if __name__ == "__main__":
    unittest.main()
