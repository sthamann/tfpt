from __future__ import annotations

import csv
import json
from pathlib import Path

from tfpt_explorer.evidence import (
    STAGE_IDS,
    build_catalog,
    get_verification_modules,
    parse_check_counts,
    summarize_build_audit_log,
    summarize_verification_log,
)


REPO = Path(__file__).resolve().parents[2]


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _minimal_repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    verification = root / "verification"
    verification.mkdir(parents=True)
    (root / "experiments/theory-contracts").mkdir(parents=True)
    (root / "experiments/evidence_scorecard.json").write_text(
        json.dumps({"n_rows": 0, "rows": []}), encoding="utf-8"
    )
    scripts = ["v1_alpha", "v2_beta"]
    _write_csv(
        verification / "script_registry.csv",
        ["script", "cluster", "what_web", "what_tex"],
        [
            {"script": script, "cluster": "core", "what_web": script, "what_tex": script}
            for script in scripts
        ],
    )
    _write_csv(
        verification / "status_ledger.csv",
        [
            "claim_id",
            "claim",
            "status",
            "location",
            "dependencies",
            "script",
            "external_data",
            "supersedes",
            "canonical_status",
            "active",
        ],
        [
            {
                "claim_id": "A.1",
                "claim": "alpha",
                "status": "Open",
                "location": "paper",
                "dependencies": "",
                "script": "v1_alpha.py",
                "external_data": "",
                "supersedes": "",
                "canonical_status": "Open",
                "active": "true",
            }
        ],
    )
    _write_csv(
        verification / "docs_map.csv",
        ["doc", "kind", "title", "line_start", "line_end", "scripts", "hash", "last_changed"],
        [],
    )
    (verification / "run_all.py").write_text(
        'MODULES = [("v1_alpha", "a"), ("v2_beta", "b")]\n', encoding="utf-8"
    )
    for script in scripts:
        (verification / f"{script}.py").write_text("def run(): return 0\n", encoding="utf-8")
    (verification / "theory_graph.json").write_text(
        json.dumps({"nodes": [], "edges": [], "meta": {"counts": {}, "sources": []}}),
        encoding="utf-8",
    )
    return root


def test_real_catalog_covers_authoritative_inventory() -> None:
    catalog = build_catalog(REPO)
    source_counts = catalog["summary"]["source_counts"]
    assert source_counts["registry_scripts"] == source_counts["run_all_modules"]
    assert source_counts["registry_scripts"] == len(get_verification_modules(REPO))
    assert source_counts["graph_nodes"] == 5969
    assert source_counts["graph_edges"] == 64164
    assert source_counts["lean_files_graph"] == 179
    assert source_counts["lean_source_files"] == 178
    assert source_counts["lean_build_files"] == 1
    assert catalog["summary"]["coverage"]["registry_runner_equal"] is True
    assert catalog["summary"]["coverage"]["registered_files_present"] is True
    assert catalog["summary"]["coverage"]["experiment_units_catalogued"] == source_counts["experiment_units"]
    experiment_evidence = catalog["summary"]["experiment_evidence"]
    assert experiment_evidence["units"] == source_counts["experiment_units"]
    assert experiment_evidence["with_linkable_source"] == source_counts["experiment_units"]
    assert experiment_evidence["missing_linkable_source"] == []
    assert set(catalog["stage_ids"]) == set(STAGE_IDS)
    ids = [item["id"] for item in catalog["items"]]
    assert len(ids) == len(set(ids))
    for item in catalog["items"]:
        assert item["sources"], item["id"]
        assert all(source.get("path") for source in item["sources"]), item["id"]


def test_incomplete_module_never_gets_false_fresh_status(tmp_path: Path) -> None:
    root = _minimal_repo(tmp_path)
    runtime = root / "tfpt_explorer/runtime"
    runtime.mkdir(parents=True)
    log = runtime / "verification_full.log"
    log.write_text("v1  alpha\n  [PASS] first check\n", encoding="utf-8")
    summary = summarize_verification_log(root, running=True)
    assert summary["status"] == "running"
    assert summary["counts"]["modules_started"] == 1
    assert summary["counts"]["modules_completed"] == 0

    (runtime / "verification_run_summary.json").write_text(
        json.dumps(summary), encoding="utf-8"
    )
    catalog = build_catalog(root)
    scripts = {item["title"]: item for item in catalog["items"] if item["type"] == "script"}
    assert scripts["v1_alpha"]["last_run"] is None
    assert scripts["v2_beta"]["last_run"] is None


def test_completed_module_is_fresh_but_unstarted_module_is_not(tmp_path: Path) -> None:
    root = _minimal_repo(tmp_path)
    runtime = root / "tfpt_explorer/runtime"
    runtime.mkdir(parents=True)
    (runtime / "verification_full.log").write_text(
        "v1  alpha\n"
        "  [PASS] first check\n"
        "--- v1 alpha: 1 passed, 0 failed ---\n",
        encoding="utf-8",
    )
    summary = summarize_verification_log(root, running=True)
    (runtime / "verification_run_summary.json").write_text(
        json.dumps(summary), encoding="utf-8"
    )
    catalog = build_catalog(root)
    scripts = {item["title"]: item for item in catalog["items"] if item["type"] == "script"}
    assert scripts["v1_alpha"]["status"] == "registered"
    assert scripts["v1_alpha"]["last_run"]["status"] == "passed"
    assert scripts["v1_alpha"]["last_run"]["fresh"] is True
    assert scripts["v2_beta"]["last_run"] is None


def test_latest_durable_individual_replay_overlays_full_summary(tmp_path: Path) -> None:
    root = _minimal_repo(tmp_path)
    runtime = root / "tfpt_explorer/runtime"
    runtime.mkdir(parents=True)
    (runtime / "verification_run_summary.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "run_id": "full-old",
                "status": "passed",
                "generated_at": "2026-09-28T09:00:00+00:00",
                "completed_at": "2026-09-28T09:00:00+00:00",
                "log_path": "tfpt_explorer/runtime/verification_full.log",
                "modules": {
                    "v1_alpha": {"status": "passed", "checks_passed": 1, "checks_failed": 0}
                },
            }
        ),
        encoding="utf-8",
    )
    for suffix, finished, checks in (
        ("older", "2026-09-28T09:30:00+00:00", 2),
        ("newer", "2026-09-28T10:30:00+00:00", 3),
    ):
        (runtime / f"job_{suffix}.json").write_text(
            json.dumps(
                {
                    "kind": "verification",
                    "status": "complete",
                    "finished_at": finished,
                    "result": {
                        "module": "v1_alpha",
                        "status": "passed",
                        "returncode": 0,
                        "checks_passed": checks,
                        "checks_failed": 0,
                        "count_source": "reported_summary",
                        "finished_at": finished,
                        "path": f"tfpt_explorer/runtime/v1_{suffix}.log",
                    },
                }
            ),
            encoding="utf-8",
        )
    catalog = build_catalog(root)
    script = next(item for item in catalog["items"] if item["id"] == "script:v1_alpha")
    assert script["last_run"]["scope"] == "individual_module"
    assert script["last_run"]["checks_passed"] == 3
    assert script["last_run"]["finished_at"] == "2026-09-28T10:30:00+00:00"


def test_started_without_footer_stays_unverified_after_prior_completion(tmp_path: Path) -> None:
    root = _minimal_repo(tmp_path)
    runtime = root / "tfpt_explorer/runtime"
    runtime.mkdir(parents=True)
    (runtime / "verification_full.log").write_text(
        "v1  alpha\n"
        "--- v1 alpha: 1 passed, 0 failed ---\n"
        "v2  beta\n"
        "  [PASS] output exists but the module was interrupted\n",
        encoding="utf-8",
    )
    summary = summarize_verification_log(root, running=False)
    assert summary["status"] == "incomplete"
    assert summary["counts"]["modules_started"] == 2
    assert summary["counts"]["modules_completed"] == 1
    assert "v2_beta" not in summary["modules"]


def test_module_internal_all_checks_passed_is_not_a_suite_pass(tmp_path: Path) -> None:
    root = _minimal_repo(tmp_path)
    runtime = root / "tfpt_explorer/runtime"
    runtime.mkdir(parents=True)
    (runtime / "verification_full.log").write_text(
        "v1  alpha\n"
        "1/1 checks passed\n"
        "ALL CHECKS PASSED\n"
        "v2  beta\n"
        "  [PASS] interrupted module output\n",
        encoding="utf-8",
    )
    summary = summarize_verification_log(root, running=False)
    assert summary["status"] == "incomplete"
    assert summary["counts"]["modules_completed"] == 0


def test_check_count_parser_ignores_must_fail_prose_and_honors_native_failure() -> None:
    output = (
        "[PASS] control [must-fail] fired\n"
        "[PASS] ordinary result\n"
        "--- demo: 2 passed, 0 failed ---\n"
    )
    assert parse_check_counts(output, 0) == {
        "checks_passed": 2,
        "checks_failed": 0,
        "count_source": "reported_summary",
    }
    assert parse_check_counts(output, 1)["checks_failed"] == 1


def test_resume_markers_preserve_boundary_and_count_new_module(tmp_path: Path) -> None:
    root = _minimal_repo(tmp_path)
    runtime = root / "tfpt_explorer/runtime"
    runtime.mkdir(parents=True)
    (runtime / "verification_full.log").write_text(
        "v1  alpha\n"
        "--- v1 alpha: 1 passed, 0 failed ---\n"
        '@@TFPT_EXPLORER_RESUME {"modules_total": 2, "resume_from": "v2_beta", "verified_through": "v1_alpha"}\n'
        "@@TFPT_EXPLORER_MODULE_START v2_beta\n"
        "  [PASS] second check\n"
        '@@TFPT_EXPLORER_MODULE_RESULT {"checks_failed": 0, "checks_passed": 1, "count_source": "reported_summary", "module": "v2_beta", "status": "passed"}\n'
        '@@TFPT_EXPLORER_RUN_RESULT {"checks_failed_in_resume": 0, "modules_completed_in_resume": 1, "status": "passed"}\n',
        encoding="utf-8",
    )
    summary = summarize_verification_log(root, running=False)
    assert summary["status"] == "passed"
    assert summary["counts"]["modules_completed"] == 2
    assert summary["counts"]["checks_passed"] == 2
    assert summary["modules"]["v2_beta"]["count_source"] == "reported_summary"


def test_interrupted_build_audit_is_not_promoted_to_pass(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    log = root / "tfpt_explorer/runtime/build_audit.log"
    log.parent.mkdir(parents=True)
    log.write_text(
        "== Sync audit ==\n"
        "AUDIT OK (2 scripts; papers, ledger, changelog and website in sync)\n"
        "== RH workspace ==\n"
        "  [PASS] inventory-pinned-files 2/2\n"
        "  [PASS] r1 one_probe.py\n",
        encoding="utf-8",
    )
    summary = summarize_build_audit_log(root, running=False)
    assert summary["status"] == "incomplete"
    assert summary["counts"]["sync_scripts"] == 2
    assert summary["counts"]["rh_checks_passed"] == 2
    assert summary["stages"]["sync_audit"] == "passed"
    assert summary["stages"]["rh_workspace"] == "incomplete"


def test_resumed_build_audit_requires_explicit_successful_stage_markers(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    log = root / "tfpt_explorer/runtime/build_audit.log"
    log.parent.mkdir(parents=True)
    log.write_text(
        "== Sync audit ==\n"
        "AUDIT OK (1028 scripts; papers, ledger, changelog and website in sync)\n"
        "== RH workspace ==\n"
        "  [PASS] inventory-pinned-files 555/555\n"
        '@@TFPT_EXPLORER_RH_RESULT {"status":"passed","probe_count_total":264,"lean_status":"passed"}\n'
        "== RH semantic catalog ==\n"
        "== Theory graph ==\n"
        "THEORY-GRAPH OK (1 nodes, 0 edges)\n"
        '@@TFPT_EXPLORER_AUDIT_RESULT {"status":"passed","rh_catalog":true,"theory_graph":true}\n',
        encoding="utf-8",
    )
    summary = summarize_build_audit_log(root, running=False)
    assert summary["status"] == "passed"
    assert set(summary["stages"].values()) == {"passed"}


def test_rh_audit_result_overlays_exact_probe_without_changing_verdict(tmp_path: Path) -> None:
    root = _minimal_repo(tmp_path)
    graph_path = root / "verification/theory_graph.json"
    graph_path.write_text(
        json.dumps(
            {
                "nodes": [
                    {
                        "id": "rh:experiments/tfpt-discovery/block_completion_probe.py",
                        "type": "rh",
                        "label": "experiments/tfpt-discovery/block_completion_probe.py",
                        "path": "experiments/tfpt-discovery/block_completion_probe.py",
                        "attrs": {"outcome": "KILLED", "round": "r484"},
                        "sources": ["experiments/tfpt-discovery/block_completion_probe.py"],
                    },
                    {
                        "id": "rh:rh/problem/block_completion.pdf",
                        "type": "rh",
                        "label": "rh/problem/block_completion.pdf",
                        "path": "rh/problem/block_completion.pdf",
                        "attrs": {"outcome": "KILLED", "round": "r484"},
                        "sources": ["rh/problem/block_completion.pdf"],
                    },
                ],
                "edges": [],
                "meta": {"counts": {}, "sources": []},
            }
        ),
        encoding="utf-8",
    )
    for rel in (
        "experiments/tfpt-discovery/block_completion_probe.py",
        "rh/problem/block_completion.pdf",
    ):
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("source", encoding="utf-8")
    runtime = root / "tfpt_explorer/runtime"
    runtime.mkdir(parents=True)
    (runtime / "build_audit.log").write_text(
        "  [FAIL] r484 block_completion_probe.py 0.3 s BLOCK_COMPLETION FAILED\n",
        encoding="utf-8",
    )
    (runtime / "build_audit_summary.json").write_text(
        json.dumps(
            {
                "status": "failed",
                "run_id": "audit-test",
                "completed_at": "2026-09-28T10:32:12+00:00",
            }
        ),
        encoding="utf-8",
    )

    catalog = build_catalog(root)
    probe = next(item for item in catalog["items"] if item["id"].endswith("block_completion_probe.py"))
    paper = next(item for item in catalog["items"] if item["id"].endswith("block_completion.pdf"))
    assert probe["status"] == "KILLED"
    assert probe["verdict"] == "KILLED"
    assert probe["last_run"]["status"] == "failed"
    assert probe["last_run"]["scope"] == "rh_fast_probe_exit_gate"
    assert paper["last_run"] is None
    assert catalog["summary"]["coverage"]["rh_audit_records"] == {
        "parsed": 1,
        "mapped": 1,
        "passed": 0,
        "failed": 1,
        "scope": "Fresh RH fast-probe exit gates; repository verdicts remain unchanged.",
    }


def test_real_rh_audit_records_are_searchable_and_keep_r484_killed() -> None:
    catalog = build_catalog(REPO)
    coverage = catalog["summary"]["coverage"]["rh_audit_records"]
    assert coverage == {
        "parsed": 264,
        "mapped": 264,
        "passed": 263,
        "failed": 1,
        "scope": "Fresh RH fast-probe exit gates; repository verdicts remain unchanged.",
    }
    r484 = next(
        item
        for item in catalog["items"]
        if item["id"] == "rh:experiments/tfpt-discovery/block_completion_probe.py"
    )
    assert r484["status"] == "KILLED"
    assert r484["verdict"] == "KILLED"
    assert r484["last_run"]["status"] == "failed"
    assert r484["last_run"]["checks_failed"] == 1


def test_verification_allowlist_has_no_arbitrary_commands() -> None:
    modules = get_verification_modules(REPO)
    assert modules
    for module in modules:
        assert module["registered_in_run_all"] is True
        assert module["exists"] is True
        assert module["command"] == ["python3", module["path"]]
        assert module["path"].startswith("verification/v")
        assert module["path"].endswith(".py")


def test_requested_source_documents_are_direct_catalog_items() -> None:
    catalog = build_catalog(REPO)
    coverage = catalog["summary"]["coverage"]["requested_source_documents"]
    assert coverage["catalogued"] == 19
    assert coverage["missing"] == []
    documents = {
        item["path"]: item
        for item in catalog["items"]
        if item["type"] == "source_document"
    }
    assert "introduction.pdf" in documents
    assert "tfpt_explorer/sources/TFPT_Konsolidierung_20260928.pdf" in documents
    assert "tfpt_explorer/sources/Eingefuegter_Text_20260928.txt" in documents
    for name in ("Zuse_Vergleich_20260928.txt", "Prozesskern_Kandidat_20260928.txt",
                 "Prozessrekonstruktion_Fixpunkt_Kandidat_20260928.txt"):
        assert f"tfpt_explorer/sources/{name}" in documents
    assert all(item["sources"] for item in documents.values())
