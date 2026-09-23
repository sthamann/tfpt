"""Cross-gate integrity checker for the universalraum-common-parent-t1-t8-20260915 package.

This is the package-level cross-check: it imports all four sibling modules
(``parent_model``, ``seam_lift``, ``gates_t1_t4``, ``gates_t5_t8``), runs each
once, and verifies the package-level invariants that no single slice can
certify on its own:

  1. identical ``parent_id`` across all four modules (object identity through
     one canonical parent);
  2. exactly the gates T1..T8 are present, each exactly once, across the two
     gate slices;
  3. ``obligations.json`` declares exactly the eight gates T1..T8;
  4. ``parent_spec.json`` carries the required full structures (constants,
     operators, derived, assumed, absent, verdict) and its ``absent`` list
     contains exactly the eight T1..T8 labels;
  5. TOE closure is computed as the conjunction of every gate's
     ``closed_in_package`` flag.  In the present package all are False.

The checker itself adds its own exact checks on top of the module summaries;
the reported ``exact_checks`` total includes those own checks (declared as
``cross_gate_own_checks``) so a downstream replay can avoid double-counting
the module summaries.

No numpy / scipy.  SymPy + stdlib only.  Stable under ``python -OO``.
``run()`` returns a stable JSON-serialisable dict; the CLI prints sorted /
indented JSON only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# Live sibling modules.  No fallback: a missing/broken interface is a hard
# import failure, never a silent substitution.
import parent_model as _pm  # noqa: E402
import seam_lift as _sl  # noqa: E402
import gates_t1_t4 as _g14  # noqa: E402
import gates_t5_t8 as _g58  # noqa: E402

PARENT_ID: str = _pm.PARENT_ID

EXPECTED_GATE_IDS = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]

# Required top-level keys in parent_spec.json (full structures, not just the
# absent list).
PARENT_SPEC_REQUIRED_KEYS = (
    "spec_id",
    "version",
    "date",
    "description",
    "constants",
    "operators",
    "derived",
    "assumed",
    "absent",
    "verdict",
)

# Required keys inside parent_spec.verdict.
PARENT_SPEC_VERDICT_KEYS = (
    "raw_seam_to_w_intertwiner",
    "closed_gate_ids",
    "selection",
    "status_pass_means",
)


class _CrossLedger:
    def __init__(self) -> None:
        self.entries: List[Dict[str, Any]] = []

    def add(self, name: str, passed: bool, detail: str = "") -> bool:
        self.entries.append({
            "name": name, "passed": bool(passed), "detail": detail,
        })
        return bool(passed)

    @property
    def count(self) -> int:
        return len(self.entries)

    def names(self) -> List[str]:
        return [e["name"] for e in self.entries]

    def all_passed(self) -> bool:
        return all(e["passed"] for e in self.entries)


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _module_parent_id(module_result: Dict[str, Any]) -> str:
    return str(module_result.get("parent_id", ""))


def _gate_ids_from_slice(slice_result: Dict[str, Any]) -> List[str]:
    gates = slice_result.get("gates", [])
    if isinstance(gates, dict):
        return [str(g.get("gate_id", g.get("gate", ""))) for g in gates.values()]
    return [str(g.get("gate_id", g.get("gate", ""))) for g in gates]


def run() -> Dict[str, Any]:
    """Run the cross-gate integrity check and return a stable JSON report.

    ``status == "PASS"`` certifies ONLY the cross-gate integrity (identical
    parent id, exactly T1..T8 once, obligations/spec structures present).
    Gate closure remains the conjunction of the explicit gate results.
    """
    led = _CrossLedger()

    # --- run each module once -------------------------------------------------
    pm_res = _pm.run()
    sl_res = _sl.run()
    g14_res = _g14.run()
    g58_res = _g58.run()

    # --- 1. identical parent_id across all four modules -----------------------
    pm_pid = _module_parent_id(pm_res)
    sl_pid = _module_parent_id(sl_res)
    g14_pid = _module_parent_id(g14_res)
    g58_pid = _module_parent_id(g58_res)
    parent_ids = {
        "parent_model": pm_pid,
        "seam_lift": sl_pid,
        "gates_t1_t4": g14_pid,
        "gates_t5_t8": g58_pid,
    }
    same_parent = (pm_pid == sl_pid == g14_pid == g58_pid) and bool(pm_pid)
    led.add("cross.identical_parent_id_all_modules", same_parent,
            "parent_model=%s seam_lift=%s gates_t1_t4=%s gates_t5_t8=%s"
            % (pm_pid, sl_pid, g14_pid, g58_pid))

    # Also verify the canonical module-level export equals the run() value.
    led.add("cross.parent_model_module_export_matches_run",
            PARENT_ID == pm_pid,
            "module PARENT_ID=%s run() parent_id=%s" % (PARENT_ID, pm_pid))

    # --- 2. exactly T1..T8 once across the two gate slices ---------------------
    g14_ids = _gate_ids_from_slice(g14_res)
    g58_ids = _gate_ids_from_slice(g58_res)
    all_gate_ids = g14_ids + g58_ids
    exactly_once = (sorted(all_gate_ids) == EXPECTED_GATE_IDS)
    led.add("cross.exactly_T1_T8_once", exactly_once,
            "gates_t1_t4=%s gates_t5_t8=%s" % (g14_ids, g58_ids))
    no_duplicates = len(all_gate_ids) == len(set(all_gate_ids))
    led.add("cross.no_duplicate_gate_ids", no_duplicates,
            "all_gate_ids=%s" % all_gate_ids)

    # --- 3. obligations.json declares exactly the eight gates T1..T8 ----------
    obligations_path = HERE / "obligations.json"
    obligations_ok = False
    obligations_gate_ids: List[str] = []
    if obligations_path.is_file():
        try:
            obligations = _load_json(obligations_path)
            gates = obligations.get("gates", [])
            obligations_gate_ids = [str(g.get("id", "")) for g in gates]
            obligations_ok = sorted(obligations_gate_ids) == EXPECTED_GATE_IDS
        except Exception as exc:
            obligations_ok = False
            obligations_gate_ids = ["<load_error: %s>" % (exc,)]
    led.add("cross.obligations_json_exactly_T1_T8", obligations_ok,
            "obligations_gate_ids=%s" % obligations_gate_ids)

    # --- 4. parent_spec.json required full structures -------------------------
    spec_path = HERE / "parent_spec.json"
    spec_keys_ok = False
    spec_verdict_ok = False
    spec_absent_t_labels_ok = False
    spec_absent_t_labels: List[str] = []
    if spec_path.is_file():
        try:
            spec = _load_json(spec_path)
            spec_keys_ok = all(k in spec for k in PARENT_SPEC_REQUIRED_KEYS)
            verdict = spec.get("verdict", {})
            spec_verdict_ok = all(k in verdict for k in PARENT_SPEC_VERDICT_KEYS)
            absent = spec.get("absent", [])
            # The eight T-labels must each appear in the absent list.
            spec_absent_t_labels = [
                "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"
            ]
            absent_text = " ".join(str(a) for a in absent)
            spec_absent_t_labels_ok = all(
                t in absent_text for t in spec_absent_t_labels
            )
        except Exception as exc:
            spec_keys_ok = False
            spec_verdict_ok = False
            spec_absent_t_labels_ok = False
            spec_absent_t_labels = ["<load_error: %s>" % (exc,)]
    led.add("cross.parent_spec_required_top_level_keys", spec_keys_ok,
            "required=%s" % (list(PARENT_SPEC_REQUIRED_KEYS),))
    led.add("cross.parent_spec_verdict_required_keys", spec_verdict_ok,
            "required=%s" % (list(PARENT_SPEC_VERDICT_KEYS),))
    led.add("cross.parent_spec_absent_contains_T1_T8_labels",
            spec_absent_t_labels_ok,
            "expected labels T1..T8 in absent list")

    # --- 5. TOE closure = conjunction of every gate's closed_in_package --------
    gates_by_id: Dict[str, Dict[str, Any]] = {}
    for g in (g14_res.get("gates", []) if isinstance(g14_res.get("gates"), list)
              else list(g14_res.get("gates", {}).values())):
        gates_by_id[str(g.get("gate_id", g.get("gate", "")))] = g
    for g in (g58_res.get("gates", []) if isinstance(g58_res.get("gates"), list)
              else list(g58_res.get("gates", {}).values())):
        gates_by_id[str(g.get("gate_id", g.get("gate", "")))] = g

    closed_gate_ids = [
        gid for gid, g in gates_by_id.items() if g.get("closed_in_package", False)
    ]
    toe_complete = bool(closed_gate_ids) and (set(closed_gate_ids) == set(EXPECTED_GATE_IDS))

    led.add("cross.toe_complete_false", toe_complete is False,
            "toe_complete=%s closed_gate_ids=%s" % (toe_complete, closed_gate_ids))
    led.add("cross.closed_gate_ids_empty", closed_gate_ids == [],
            "closed_gate_ids=%s" % closed_gate_ids)

    # Per-gate status map for the report.
    gate_statuses: Dict[str, str] = {
        gid: str(g.get("status", g.get("closed", ""))) for gid, g in gates_by_id.items()
    }

    # --- module exact_checks (for replay accounting, no double-counting) -------
    # cross_gate's OWN checks are led.count; the module summaries are reported
    # separately so a downstream replay can compute the total as
    #   total = sum(module_counts) + cross_gate_own_checks
    # WITHOUT re-counting the module summaries inside cross_gate.
    module_counts = {
        "parent_model": int(pm_res.get("exact_checks", 0)),
        "seam_lift": int(sl_res.get("exact_checks", 0)),
        "gates_t1_t4": int(g14_res.get("exact_checks", 0)),
        "gates_t5_t8": int(g58_res.get("exact_checks", 0)),
    }
    cross_gate_own_checks = led.count

    checker_integrity = led.all_passed()
    status = "PASS" if checker_integrity else "FAIL"

    return {
        "status": status,
        "checker_status": status,
        "parent_id": PARENT_ID,
        "parent_ids": parent_ids,
        "toe_complete": toe_complete,
        "closed_gate_ids": closed_gate_ids,
        "gate_statuses": gate_statuses,
        "exact_checks": cross_gate_own_checks,
        "cross_gate_own_checks": cross_gate_own_checks,
        "checks": led.names(),
        "module_counts": module_counts,
        "obligations_gate_ids": obligations_gate_ids,
        "parent_spec_required_keys": list(PARENT_SPEC_REQUIRED_KEYS),
        "parent_spec_verdict_required_keys": list(PARENT_SPEC_VERDICT_KEYS),
        "expected_gate_ids": list(EXPECTED_GATE_IDS),
        "gates_t1_t4_ids": g14_ids,
        "gates_t5_t8_ids": g58_ids,
        "hypothesis": (
            "cross-gate integrity holds: identical canonical parent_id, "
            "exactly T1..T8 once, obligations/spec structures present; all "
            "T1-T8 closures remain false; toe_complete is False"
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
