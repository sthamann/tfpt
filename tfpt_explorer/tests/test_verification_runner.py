"""Regression checks for safe continuation of the long native suite."""

import json
from types import SimpleNamespace

from tfpt_explorer import verification_runner as runner


def test_worker_lock_excludes_a_second_runner(tmp_path):
    path = tmp_path / "worker.lock"
    first = runner._lock(path)
    assert first is not None
    try:
        assert runner._lock(path) is None
    finally:
        first.close()
    next_lock = runner._lock(path)
    assert next_lock is not None
    next_lock.close()


def test_archive_preserves_original_edits_and_deduplicates(tmp_path, monkeypatch):
    rel = "experiments/tfpt-discovery/user_result.json"
    source = tmp_path / rel
    source.parent.mkdir(parents=True)
    original = b'{"user_edit": true}\n'
    source.write_bytes(original)
    archive = tmp_path / "runtime/archive"
    monkeypatch.setattr(runner, "ROOT", tmp_path)
    monkeypatch.setattr(runner, "GENERATED_ARCHIVE", archive)
    monkeypatch.setattr(
        runner.subprocess, "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=0, stdout=rel.encode() + b"\0"),
    )
    assert runner._archive_generated_json_changes(1) == [rel]
    assert source.read_bytes() == original
    assert (archive / "latest" / rel).read_bytes() == original
    assert runner._archive_generated_json_changes(2) == []
    assert source.read_bytes() == original
    assert len(json.loads((archive / "manifest.json").read_text())["captures"]) == 1


def test_module_exception_is_recorded_and_next_module_runs(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(runner, "WORKER_LOCK", tmp_path / "worker.lock")
    monkeypatch.setattr(runner, "WORKER_PID", tmp_path / "worker.pid")
    monkeypatch.setattr(runner, "_remaining_modules", lambda: (["bad", "good"], {}))
    monkeypatch.setattr(runner, "_registry_names", lambda: ["bad", "good"])
    monkeypatch.setattr(runner, "summarize_verification_log", lambda *a, **k: {"counts": {"checks_failed": 1}})

    def import_module(name):
        if name == "bad":
            raise ValueError("deliberate regression probe")
        return SimpleNamespace(run=lambda: 0)

    monkeypatch.setattr(runner.importlib, "import_module", import_module)
    precision = runner.run_all.mpmath.mp.dps
    try:
        assert runner.worker() == 1
    finally:
        runner.run_all.mpmath.mp.dps = precision
    lines = capsys.readouterr().out.splitlines()
    results = [json.loads(line.split(" ", 1)[1]) for line in lines if line.startswith("@@TFPT_EXPLORER_MODULE_RESULT ")]
    assert [(row["module"], row["status"]) for row in results] == [("bad", "failed"), ("good", "passed")]
    assert results[0]["error_type"] == "ValueError"
    terminal = json.loads(next(line.split(" ", 1)[1] for line in lines if line.startswith("@@TFPT_EXPLORER_RUN_RESULT ")))
    assert terminal["status"] == "failed"
    assert not runner.WORKER_PID.exists()
