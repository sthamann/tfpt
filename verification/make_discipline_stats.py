#!/usr/bin/env python3
"""Generate the website discipline-stats mirror from the suite's own files.

Source : verification/v649_discipline_audit.py census functions (the same
         code the load-bearing META.DISCIPLINE.01 module runs), reading
         verification/status_ledger.csv, verification/v*.py,
         tfpt_research_contracts.tex and the committed Lean tree.
Target : website/lib/discipline.ts  (typed data the /method page renders)

The target is GENERATED -- never edit it by hand.  Regenerate with:

    python3 verification/make_discipline_stats.py           # rewrite
    python3 verification/make_discipline_stats.py --check   # exit 1 if stale

It is run automatically by `bash build.sh gen`, and its freshness is
enforced by verification/audit_sync.py (section A.generated), so the
public /method page can never drift from the suite.

Only the STATIC censuses are recomputed here (deterministic parsing).
The live parts of v649 -- the 12-module deterministic replay and the
five classical anchor recomputes -- are quoted as certified by the
suite run (python3 verification/v649_discipline_audit.py replays them).

stdlib only -- runnable without the venv (build.sh calls it with python3;
v649's module-level imports are stdlib-only by design).
"""
import json
import sys
from pathlib import Path

import v649_discipline_audit as aud

ROOT = Path(__file__).resolve().parent.parent
WEBSITE_DIR = ROOT / "website"
TS_TARGET = WEBSITE_DIR / "lib" / "discipline.ts"

TS_HEADER = """\
// GENERATED FILE -- DO NOT EDIT BY HAND.
// Written by verification/make_discipline_stats.py from the suite's own
// files (status_ledger.csv, v*.py sources, tfpt_research_contracts.tex,
// the committed Lean tree). Single source of truth: the verification suite.
// Regenerate with:  python3 verification/make_discipline_stats.py
// (run automatically by `bash build.sh gen`; freshness enforced by
//  verification/audit_sync.py, so /method can never drift from the suite).
// The replay and anchor entries are certified live by
// verification/v649_discipline_audit.py (META.DISCIPLINE.01) on every
// suite run: python3 verification/run_all.py.

export interface DisciplineStats {
  /** D1: status ledger census. */
  ledger: {
    rows: number;
    active: number;
    retired: number;
    /** Public display classes ([E]/[C]/[O]/[X] + axioms + unclassified). */
    dist: { E: number; C: number; O: number; X: number; AXIOM: number; OTHER: number };
    /** Rows documenting kills / honest negatives / retypes (keyword census). */
    killRows: number;
  };
  /** D2: static census over all verification/v*.py sources. */
  suite: {
    modules: number;
    checkSites: number;
    mustfailOccurrences: number;
    mustfailModules: number;
    eMarks: number;
    cMarks: number;
    seededModules: number;
    sympyModules: number;
  };
  /** D3: preregistration census. */
  contracts: {
    ledgerRows: number;
    withKillCriteria: number;
    texMentions: number;
  };
  /** D4: deterministic replay (certified by v649 on every suite run). */
  replay: {
    sample: string[];
    passed: number;
    total: number;
  };
  /** D5: classical anchors recomputed by v649 + citation census. */
  anchors: {
    recomputed: number;
    citations: Record<string, number>;
    arxivModules: number;
  };
  /** D6: committed Lean proof modules. */
  lean: {
    modules: number;
  };
  /** D7: open gates (display class O, active). */
  openGates: {
    count: number;
  };
}

export const DISCIPLINE: DisciplineStats =
"""

TS_FOOTER = """;

/** Replay verdict enum of v649 (frozen). */
export const DISCIPLINE_VERDICT = "DISCIPLINE-CERTIFIED";
"""


def build() -> dict[Path, str]:
    rows = aud.ledger_rows()
    lc = aud.ledger_census(rows)
    sc = aud.suite_census()
    cc = aud.contracts_census(rows)
    lz = aud.lean_census()
    cites, arxiv = aud.citation_census()
    stats = {
        "ledger": {
            "rows": lc["rows"],
            "active": lc["active"],
            "retired": lc["retired"],
            "dist": lc["dist"],
            "killRows": len(lc["kill_ids"]),
        },
        "suite": {
            "modules": sc["modules"],
            "checkSites": sc["sites"],
            "mustfailOccurrences": sc["mf_occ"],
            "mustfailModules": sc["mf_mods"],
            "eMarks": sc["e_marks"],
            "cMarks": sc["c_marks"],
            "seededModules": sc["seed_mods"],
            "sympyModules": sc["sympy_mods"],
        },
        "contracts": {
            "ledgerRows": cc["prereg"],
            "withKillCriteria": cc["prereg_kill"],
            "texMentions": cc["tex_mentions"],
        },
        "replay": {
            "sample": aud.REPRO_SAMPLE,
            "passed": 12,
            "total": 12,
        },
        "anchors": {
            "recomputed": aud.ANCHORS_MIN,
            "citations": cites,
            "arxivModules": arxiv,
        },
        "lean": {
            "modules": lz["n"],
        },
        "openGates": {
            "count": len(aud.open_gate_ids(rows)),
        },
    }
    body = TS_HEADER + json.dumps(stats, ensure_ascii=False, indent=2) \
        + TS_FOOTER
    return {TS_TARGET: body}


def main() -> None:
    check_only = "--check" in sys.argv
    stale = []
    for target, content in build().items():
        # Shadow-export trees ship no website/ -- skip the mirror there
        # (mirrors make_changelog_web / make_script_index behaviour).
        if WEBSITE_DIR in target.parents and not WEBSITE_DIR.exists():
            if not check_only:
                print(f"skipped (no website/ in this tree): "
                      f"{target.relative_to(ROOT)}")
            continue
        if not target.exists() or target.read_text() != content:
            if check_only:
                stale.append(target)
            else:
                target.write_text(content)
                print(f"wrote {target.relative_to(ROOT)}")
    if check_only:
        if stale:
            for t in stale:
                print(f"STALE (re-run make_discipline_stats.py): "
                      f"{t.relative_to(ROOT)}")
            sys.exit(1)
        print("discipline mirror up to date")


if __name__ == "__main__":
    main()
