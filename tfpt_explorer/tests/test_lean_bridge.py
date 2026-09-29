from pathlib import Path

from tfpt_explorer.lean_bridge import export_candidates, project_files, strip_comments


def test_nested_comments_and_quoted_sorry_are_not_live_axioms():
    text = '/- outer /- sorry -/ axiom Fake : False -/\ndef real : Nat := 3\n-- sorry\ndef message := "sorry \\" admit"\ntheorem t : True := by sorry\n'
    cleaned = strip_comments(text)
    assert cleaned.count("\n") == text.count("\n")
    assert "Fake" not in cleaned
    assert cleaned.count("sorry") == 1
    assert "def real" in cleaned


def test_automatic_adapter_is_conservative_and_skips_noncomputable_and_heavy():
    modules = [{"module": "Tiny", "project": "sample", "path": "Tiny.lean", "sha256": "hash", "heavy_certificate": False,
                "declarations": [
                    {"name": "p", "qualified_name": "Tiny.p", "line": 1, "classification": "computation_candidate", "signature": "def p (n : ℕ) : ℕ := 2 + 2 ^ n"},
                    {"name": "q", "qualified_name": "Tiny.q", "line": 2, "classification": "noncomputable", "signature": "noncomputable def q : Nat := 1"},
                    {"name": "proof", "qualified_name": "Tiny.proof", "line": 3, "classification": "proof", "signature": "theorem proof : True := by trivial"},
                    {"name": "real", "qualified_name": "Tiny.real", "line": 4, "classification": "computation_candidate", "signature": "def real : ℝ := 1"},
                ]}]
    got = export_candidates(modules)
    assert [(x["name"], x["arity"], x["status"]) for x in got] == [("Tiny.p", 1, "candidate")]
    modules[0]["heavy_certificate"] = True
    assert export_candidates(modules) == []


def test_project_inventory_excludes_vendored_libraries_and_build_configuration(tmp_path):
    base = tmp_path / "experiments/lean4-carrier-rigidity"
    (base / ".lake/packages/Mathlib").mkdir(parents=True)
    (base / ".lake/packages/Mathlib/Tactic.lean").write_text("def hidden := 1")
    (base / "lakefile.lean").write_text("import Lake")
    (base / "Actual.lean").write_text("theorem yes : True := by trivial")
    assert [p.name for p in project_files(tmp_path)] == ["Actual.lean"]
