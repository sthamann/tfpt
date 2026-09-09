"""Release regression: local research output must not break the shadow export."""
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import make_manifest as manifest


class ResearchManifestTests(unittest.TestCase):
    def test_only_indexed_research_files_are_shipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "experiments/theory-contracts"
            research.mkdir(parents=True)
            (research / ".gitignore").write_text("qgeo_dtn_results.json\n")
            (research / "proof.md").write_text("shipped proof\n")
            (research / "qgeo_dtn_results.json").write_text("{}\n")
            (research / "unpublished_round.json").write_text("{}\n")
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "add", "experiments/theory-contracts/proof.md"], check=True)
            self.assertEqual(manifest.collect_research(str(root)),
                             ["experiments/theory-contracts/proof.md"])

    def test_non_git_export_can_be_regenerated(self):
        with tempfile.TemporaryDirectory() as tmp:
            research = Path(tmp) / "experiments/theory-contracts"
            research.mkdir(parents=True)
            (research / "proof.md").write_text("shipped proof\n")
            (research / "__pycache__").mkdir()
            (research / "__pycache__/scratch.json").write_text("{}\n")
            self.assertEqual(manifest.collect_research(tmp),
                             ["experiments/theory-contracts/proof.md"])

    def test_git_failure_cannot_silently_include_local_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / ".git").write_text("gitdir: /worktree/metadata\n")
            with patch.object(manifest.subprocess, "check_output", side_effect=OSError("git unavailable")):
                with self.assertRaises(OSError):
                    manifest.collect_research(tmp)

    def test_native_research_sources_and_source_pins_are_shipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "experiments/theory-contracts"
            research.mkdir(parents=True)
            names = ("group.cpp", "orbits.hpp", "executed-sources.sha256")
            for name in names:
                (research / name).write_text("source fixture\n")
            expected = sorted("experiments/theory-contracts/" + name for name in names)
            self.assertEqual(manifest.collect_research(tmp), expected)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "add", *expected], check=True)
            (research / "unpublished.cpp").write_text("local only\n")
            self.assertEqual(manifest.collect_research(tmp), expected)


if __name__ == "__main__":
    unittest.main()
