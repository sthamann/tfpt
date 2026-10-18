#!/usr/bin/env python3
"""Focused regressions for source attribution and honest citation boundaries."""
import csv
import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import make_content_registry as registry


class ContentRegistryTests(unittest.TestCase):
    def test_escaped_percent_and_comment_offsets(self):
        source = "kept \\% sign % hidden theorem\nnext"
        masked = registry.mask_tex_comments(source)
        self.assertEqual(len(masked), len(source))
        self.assertIn("\\% sign", masked)
        self.assertNotIn("hidden", masked)
        self.assertEqual(source.count("\n"), masked.count("\n"))

    def test_split_filename_resolves_without_tail_pseudocitation(self):
        source = "before\n\\texttt{v1035\\_matter\\_\\allowbreak\n coupling.py} after"
        self.assertEqual(list(registry.file_citations(source)), [("v1035_matter_coupling.py", 1)])

    def test_even_backslash_rowbreak_does_not_escape_comment(self):
        source = r"row \\% hidden v999_fictional.py" + "\n" + r"kept \% real v3.py"
        masked=registry.mask_tex_comments(source)
        self.assertNotIn("fictional",masked)
        self.assertIn(r"\% real",masked)
        self.assertEqual(list(registry.file_citations(source)),[("v3.py",1)])

    def test_math_is_omitted_explicitly_not_changed_to_integer(self):
        text = registry.plain_tex(r"The constant $c_3=\frac{1}{8\pi}$ remains a declared input.")
        self.assertIn("[formula in source]", text)
        self.assertNotIn("18", text)

    def test_archive_include_uses_original_compile_directory(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(registry, "ROOT", Path(directory)):
            available = {"documents/archive-note/preamble.tex"}
            target = registry.resolve_include("../../../documents/archive-note/preamble.tex", "documents/archive-note/main.tex", available, "_archive/paper/old")
            self.assertEqual(target, "documents/archive-note/preamble.tex")
            self.assertIsNone(registry.resolve_include("../../outside.tex", "note.tex", {"outside.tex"}, "."))

    def test_pure_wrapper_has_no_second_content_body(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(registry, "ROOT", Path(directory)):
            Path(directory, "note.tex").write_text("% compatibility\n\\input{documents/note/main.tex}")
            config = {"generated_tex": [], "active_entry_points": ["note.tex"]}
            source, sections, _ = registry.parse_tex("note.tex", config)
            self.assertTrue(source["is_wrapper"])
            self.assertEqual(source["role"], "active_wrapper")
            self.assertEqual(sections, [])

    def test_lean_signature_keeps_hypotheses_and_sorry_is_not_proof_status(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(registry, "ROOT", Path(directory)):
            Path(directory, "Example.lean").write_text("/- theorem fake : False := by sorry -/\nnamespace Example\nvariable (x : Nat)\ntheorem conditional (h : x = 1) : x = 1 := by\n  sorry\nend Example\n")
            declarations, _ = registry.parse_lean("Example.lean")
            self.assertEqual(len(declarations), 1)
            theorem = declarations[0]
            self.assertEqual(theorem["qualified_name"], "Example.conditional")
            self.assertIn("(h : x = 1)", theorem["statement_as_written"])
            self.assertTrue(theorem["contains_sorry_or_admit"])
            self.assertFalse(theorem["checked_by_registry"])

    def test_wolfram_mapping_comes_from_real_heading_and_check(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(registry, "ROOT", Path(directory)):
            Path(directory, "mirror.wl").write_text('(* ---- (v1031) bounded exact check ---- *)\ncheck["v1031 projector", True];\n')
            sections, _ = registry.parse_wolfram("mirror.wl")
            self.assertEqual(sections[0]["python_identifiers_in_heading"], ["v1031"])
            self.assertEqual(sections[0]["check_labels_as_written"], ["v1031 projector"])
            self.assertFalse(sections[0]["checked_by_registry"])

    def test_historical_replay_snapshots_cannot_inherit_current_status(self):
        for filename in ("v1033_original.py","status_ledger_original.csv","v1033_charged_disorder.py"):
            info=registry.historical_snapshot_info("verification/historical_replay/"+filename,
                {"kind":"reader_only_python_adapter","path":"verification/v1033_charged_disorder.py",
                 "historical_sha256":"a"*64,"status":"PASS","retained_claim_ids":["CURRENT.01"]})
            self.assertEqual(info["role"],"historical_snapshot")
            self.assertEqual(info["claim_ids"],[])
            self.assertTrue(info["ledger_status_not_inherited"])
            self.assertFalse(info["current_proof_coverage"])
            self.assertNotIn("status",info["historical_provenance_as_recorded"])
            self.assertNotIn("retained_claim_ids",info["historical_provenance_as_recorded"])
        self.assertIsNone(registry.historical_snapshot_info("verification/v1033_charged_disorder.py"))

    def test_gitless_inventory_does_not_sweep_private_neighbor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "docs/registry"
            output.mkdir(parents=True)
            (root / "public.tex").write_text("public")
            (root / "private.tex").write_text("unpublished")
            (output / "source_inventory.json").write_text(json.dumps({"tex_sources": ["public.tex"]}))
            config = {"excluded_components": [], "module_manifest": "documents/source_manifest.json", "explicit_public_sources": []}
            with patch.object(registry, "ROOT", root), patch.object(registry, "OUT", output):
                paths, _ = registry.discover(config)
            self.assertEqual(paths, ["public.tex"])

    def test_gitless_evidence_scope_excludes_editor_tools_but_requires_research_bytes(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(registry,"ROOT",Path(directory)):
            root=Path(directory)
            (root/"verification").mkdir()
            (root/"verification/v1.py").write_text("actual research source")
            config={"excluded_components":[],"excluded_evidence_roots":["website",".cursor",".codex"]}
            declared=["verification/v1.py",".cursor/hooks/guard-read.py",".codex/hooks/guard-read.py","website/public/verification/v1.py"]
            self.assertEqual(registry.research_evidence_paths(declared,config),["verification/v1.py"])
            (root/"verification/v1.py").unlink()
            with self.assertRaisesRegex(ValueError,"Missing declared research evidence sources: verification/v1.py"):
                registry.research_evidence_paths(declared,config)

    def test_local_git_deleted_tools_are_explicit_omissions_but_proof_sources_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(registry,"ROOT",Path(directory)):
            config={"excluded_components":[]}
            retired="verification/build_theory_graph.py";omissions=[]
            self.assertEqual(registry.research_evidence_paths([retired],config,{retired},{"v1"},omissions),[])
            self.assertEqual(omissions[0]["source"],retired)
            self.assertEqual(omissions[0]["kind"],"local_missing_noncanonical_evidence")
            self.assertFalse(omissions[0]["current_proof_coverage"])
            with self.assertRaisesRegex(ValueError,"Missing declared research evidence"):
                registry.research_evidence_paths([retired],config)
            for required in ("verification/v1.py","proof.lean","mirror.wl","mirror.wls","required.tex","verification/status_ledger.csv"):
                with self.subTest(required=required),self.assertRaisesRegex(ValueError,"Missing declared research evidence"):
                    registry.research_evidence_paths([required],config,{required},{"v1"},[])

    def test_owned_shadow_with_stale_git_index_reproduces_shipped_registry(self):
        config=json.loads(registry.CONFIG.read_text())
        config.update(active_entry_points=["fresh.tex"],explicit_public_sources=[],topics=[])
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);out=root/"docs/registry";out.mkdir(parents=True)
            (root/"verification").mkdir()
            for name,text in {
                "fresh.tex":r"\documentclass{article}\begin{document}\section{Fresh} Exact source.\end{document}",
                "verification/tool.py":"# actual shipped source\n",
                "verification/make_content_registry.py":"# fixture generator source\n",
                "verification/tex_sources.py":"# fixture helper source\n",
                "verification/script_registry.csv":"script,cluster,what_web\n",
                "verification/status_ledger.csv":"claim_id,status\n",
            }.items():(root/name).write_text(text)
            (out/"config.json").write_text(json.dumps(config))
            (out/"source_inventory.json").write_text(json.dumps({"tex_sources":["fresh.tex"],"evidence_sources":["verification/tool.py"]}))
            marker=root/".tfpt-shadow-export"
            marker.write_text(json.dumps({"owner":"tfpt-shadow-export","source_repository":"sthamann/tfpt"}))
            with patch.object(registry,"ROOT",root),patch.object(registry,"OUT",out),patch.object(registry,"CONFIG",out/"config.json"),contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(registry.main([]),0)
                original=(out/"registry.json").read_bytes()
                subprocess.run(["git","init","--quiet",str(root)],check=True,capture_output=True)
                (root/"stale.tex").write_text("old Git index content")
                subprocess.run(["git","-C",str(root),"add","stale.tex"],check=True,capture_output=True)
                self.assertEqual(registry.git_files("*.tex"),["stale.tex"])
                self.assertFalse(registry.is_git_root())
                self.assertEqual(registry.main(["--check"]),0)
                self.assertEqual(registry.main([]),0)
                self.assertEqual((out/"registry.json").read_bytes(),original)
                marker.write_text('{"owner":"another-export"}')
                with self.assertRaisesRegex(ValueError,"Unrecognized shadow export"):
                    registry.is_git_root()

    def test_generated_registry_statuses_are_original_and_copies_do_not_inherit(self):
        path = registry.OUT / "registry.json"
        if not path.exists(): self.skipTest("Generate the public registry first")
        data = json.loads(path.read_text())
        with (registry.ROOT / "verification/status_ledger.csv").open() as stream:
            ledger = {r["claim_id"]: r for r in csv.DictReader(stream)}
        for entity in data["evidence"]:
            if entity["type"] == "claim_ledger_row":
                self.assertEqual(entity["status_as_recorded"], ledger[entity["claim_id"]]["status"])
                self.assertEqual(entity["canonical_status_as_recorded"], ledger[entity["claim_id"]]["canonical_status"])
            if entity["type"] == "python_verification":
                self.assertTrue(entity["path"].startswith("verification/"))
            if entity["type"] == "python_source_copy":
                self.assertEqual(entity["claim_ids"], [])
                self.assertTrue(entity["ledger_status_not_inherited"])
        for document in data["documents"]:
            if document["role"] == "active":
                self.assertEqual(document["expansion_status"], "complete_literal_expansion")


if __name__ == "__main__":
    unittest.main()
