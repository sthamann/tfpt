"""Consumer regressions: literal TeX includes remain visible and attributed.

The shared reader's cycle/missing-file cases belong to test_tex_sources.py.
These tests exercise actual existing generators/guards without changing any
mathematical predicate or monkeypatching filesystem APIs.
"""
from pathlib import Path
import csv
import io
import json
import tempfile
import subprocess
import unittest
from unittest.mock import patch

import audit_sync
import make_changelog_web
import make_docs_map
import make_manifest
import v1006_mmst_lemma_battery as mmst
import v1016_state_gap_batteries as state
import v1033_charged_disorder as charged
import v188_frontier_wording_guard as wording
from redteam import rt_common as redteam
from tex_sources import read_tex


class ModularTexConsumerTests(unittest.TestCase):
    def test_map_preserves_nested_physical_source_lines_and_utf8_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "documents/parts").mkdir(parents=True)
            (root / "paper.tex").write_text(r"\input{documents/body}")
            body = "% Unicode α\n\\section{First}\nIntro\n\\input{parts/proof}\n"
            (root / "documents/body.tex").write_text(body)
            proof = "First proof line\n\\veri{v1_fixture.py}\n"
            (root / "documents/parts/proof.tex").write_text(proof)
            with patch.object(make_docs_map, "ROOT", root):
                rows = make_docs_map.parse_doc("paper")
                section = next(r for r in rows if r["title"] == "First")
                self.assertEqual(section["source_path"], "documents/body.tex")
                self.assertEqual(section["source_line_start"], 2)
                self.assertEqual(section["scripts"], "v1_fixture.py")
                spans = json.loads(section["source_spans"])
                child = next(s for s in spans if s["path"].endswith("proof.tex"))
                self.assertEqual((child["line_start"], child["line_end"]), (1, 2))
                self.assertEqual(child["byte_end"], len(proof.encode("utf-8")))
                self.assertEqual(child["include_chain"],
                                 ["paper.tex", "documents/body.tex", "documents/parts/proof.tex"])
                csv_text = make_docs_map.render_docs_map([{**r, "last_changed": "2026-10-18"} for r in rows])
                exported = list(csv.DictReader(io.StringIO(csv_text)))
                self.assertEqual(exported[1]["source_path"], "documents/body.tex")
                self.assertEqual(make_docs_map.parse_doc("paper"), rows)

    def test_changelog_generation_is_identical_after_source_only_split(self):
        text = (r"\documentclass{article}" "\n" r"\begin{document}" "\n"
                r"\subsection*{2026-10-18 (Ownership)}" "\n"
                r"\begin{itemize}\item Scoped \texttt{v1_fixture.py}.\end{itemize}" "\n"
                r"\end{document}" "\n")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry = root / "changelog.tex"
            entry.write_text(text)
            with patch.object(make_changelog_web, "CHANGELOG_TEX", entry):
                monolithic = make_changelog_web.build()
                (root / "documents").mkdir()
                (root / "documents/history.tex").write_text(text)
                entry.write_text(r"\input{documents/history}")
                self.assertEqual(make_changelog_web.build(), monolithic)
                self.assertEqual(make_changelog_web.build(), make_changelog_web.build())

    def test_master_index_and_history_cannot_satisfy_body_citation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tex-artefacts").mkdir()
            (root / "documents").mkdir()
            (root / "tex-artefacts/verification.tex").write_text("v1_fixture.py\n")
            (root / "changelog.tex").write_text(r"\input{documents/history}")
            (root / "documents/history.tex").write_text("Historical v1_fixture.py\n")
            entry = root / "paper.tex"
            entry.write_text(r"\input{tex-artefacts/verification}\input{changelog}")
            with patch.object(audit_sync, "ROOT", root), \
                 patch.object(audit_sync, "ACTIVE_DOCS", ["paper"]), \
                 patch.object(audit_sync, "errors", []):
                audit_sync.check_papers(["v1_fixture"], {})
                self.assertTrue(any("[B.forward]" in error for error in audit_sync.errors))
                audit_sync.errors.clear()
                entry.write_text(r"\input{documents/body}\input{tex-artefacts/verification}\input{changelog}")
                (root / "documents/body.tex").write_text(r"Body \veri{v1_fixture.py}.")
                audit_sync.check_papers(["v1_fixture"], {})
                self.assertEqual(audit_sync.errors, [])

    def test_wording_guard_keeps_explicit_history_readable_but_not_nested(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "paper.tex").write_text("Current prose\n" + r"\input{changelog}")
            (root / "changelog.tex").write_text("Historical prose\n")
            with patch.object(wording, "ROOT", str(root)):
                self.assertEqual(wording.document_body(root / "paper.tex"), "Current prose\n")
                self.assertEqual(wording.document_body(root / "changelog.tex"), "Historical prose\n")

    def test_redteam_firewall_reads_body_and_excludes_reference_appendices(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tex-artefacts").mkdir()
            (root / "body.tex").write_text("Actual body phrase\n")
            (root / "changelog.tex").write_text("Historical phrase\n")
            (root / "tex-artefacts/verification.tex").write_text("Index phrase\n")
            entry = root / "paper.tex"
            entry.write_text(r"\input{body}\input{changelog}\input{tex-artefacts/verification}")
            with patch.object(redteam, "ROOT_DIR", str(root)):
                self.assertEqual(redteam.read_text(entry), "Actual body phrase\n")
                self.assertEqual(redteam.read_text(root / "changelog.tex"), "Historical phrase\n")
                self.assertEqual(redteam.read_text(root / "missing.tex"), "")

    def test_manifest_lists_referenced_modules_and_shared_fragments_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "documents").mkdir()
            (root / "shared").mkdir()
            (root / "paper.tex").write_text(r"\input{documents/body}")
            (root / "documents/body.tex").write_text(r"\input{shared/lemma}")
            (root / "shared/lemma.tex").write_text(r"\input{shared/empty}")
            (root / "shared/empty.tex").write_text("")
            (root / "documents/unreferenced.tex").write_text("Local scratch\n")
            self.assertEqual(make_manifest.collect_tex(root, ["paper.tex"]),
                             ["documents/body.tex", "paper.tex", "shared/empty.tex", "shared/lemma.tex"])

    def test_fresh_checkout_version_audit_and_manifest_ignore_runtime_cache(self):
        version_text = (Path(__file__).resolve().parents[1] / "tex-artefacts/version.tex").read_text()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tex-artefacts").mkdir()
            version = root / "tex-artefacts/version.tex"
            version.write_text(version_text)
            with patch.object(audit_sync, "ROOT", root), patch.object(audit_sync, "SHADOW", True):
                absent = audit_sync.tex_version()
                audit_sync.check_versions()
                closure = make_manifest.collect_tex(root, ["tex-artefacts/version.tex"])
                self.assertEqual(closure, ["tex-artefacts/version.tex"])
                (root / "tex-artefacts/version-auto.tex").write_text(r"\def\TFPTrev{runtime}")
                self.assertEqual(audit_sync.tex_version(), absent)
                audit_sync.check_versions()
                self.assertEqual(make_manifest.collect_tex(root, ["tex-artefacts/version.tex"]), closure)

    def test_document_guards_expand_tex_but_keep_nontex_source_literal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "clauses.tex").write_text("\n".join(mmst.ROUND4_TELB_DOCUMENT_SNIPPETS))
            entry = root / "memo.tex"
            entry.write_text(r"\input{clauses}")
            self.assertTrue(mmst.tex_has(str(entry), "A 512-node Acb certificate"))
            self.assertTrue(mmst.telb_round4_document_guard(read_tex(entry)))
            self.assertTrue(state.source_contains(entry, "A 512-node Acb certificate"))
            code = root / "literal.py"
            code.write_text(r"\input{absent-should-not-be-expanded}")
            self.assertTrue(mmst.tex_has(str(code), "absent-should-not-be-expanded"))
            with patch.object(charged, "REPO", root):
                self.assertIn("A 512-node Acb certificate", charged.read("memo.tex"))
                self.assertEqual(charged.read("literal.py"), code.read_text())


class BuildFailureBoundaryTests(unittest.TestCase):
    def build_with_fake_compiler(self, root: Path, compiler_text: str):
        build = Path(__file__).resolve().parents[1] / "build.sh"
        source = build.read_text()
        function = source[source.index("build_one() {"):source.index("\nNOTES=(")]
        compiler = root / "fake-pdflatex"
        compiler.write_text("#!/usr/bin/env bash\n" + compiler_text)
        compiler.chmod(0o755)
        script = ("set -u\nPASS=0; FAIL=0; FAILED=()\nPDFLATEX=(\"$2\")\n"
                  + function + '\nbuild_one "$1" sample\nprintf "RESULT %s %s\\n" "$PASS" "$FAIL"\n')
        return subprocess.run(["bash", "-c", script, "fixture", str(root), str(compiler)],
                              capture_output=True, text=True, timeout=10)

    def test_stale_existing_pdf_cannot_turn_compiler_failure_into_success(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "sample.pdf").write_bytes(b"%PDF existing")
            for suffix in ("aux", "toc", "out"):
                (root / f"sample.{suffix}").write_text("poisoned reference")
            result = self.build_with_fake_compiler(root, "exit 1\n")
            self.assertIn("RESULT 0 1", result.stdout, result.stderr)
            for suffix in ("aux", "toc", "out"):
                self.assertFalse((root / f"sample.{suffix}").exists())

    def test_successful_retry_requires_two_successful_compiler_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            compiler = ("n=0; [ ! -f .calls ] || n=$(cat .calls)\n"
                        "n=$((n+1)); printf '%s' \"$n\" > .calls\n"
                        "[ \"$n\" -ne 1 ] || exit 1\n"
                        "printf '%%PDF regenerated' > sample.pdf\nexit 0\n")
            result = self.build_with_fake_compiler(root, compiler)
            self.assertIn("RESULT 1 0", result.stdout, result.stderr)
            self.assertEqual((root / ".calls").read_text(), "3")

    def test_success_exit_without_any_pdf_is_still_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.build_with_fake_compiler(Path(directory), "exit 0\n")
            self.assertIn("RESULT 0 1", result.stdout, result.stderr)


if __name__ == "__main__":
    unittest.main()
