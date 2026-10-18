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
{
  "ledger": {
    "rows": 788,
    "active": 783,
    "retired": 5,
    "dist": {
      "E": 192,
      "C": 217,
      "O": 328,
      "X": 39,
      "AXIOM": 2,
      "OTHER": 10
    },
    "killRows": 261
  },
  "suite": {
    "modules": 707,
    "checkSites": 8230,
    "mustfailOccurrences": 3343,
    "mustfailModules": 301,
    "eMarks": 3710,
    "cMarks": 1412,
    "seededModules": 81,
    "sympyModules": 443
  },
  "contracts": {
    "ledgerRows": 61,
    "withKillCriteria": 48,
    "texMentions": 86
  },
  "replay": {
    "sample": [
      "v55_coxeter_cycle",
      "v91_spine_tetrahedron",
      "v108_pascal_ladder",
      "v205_xi_threequarter",
      "v305_witness_independence",
      "v405_seam_equiv_omega",
      "v505_celestial_wp5e_beta_equivariant_ledger",
      "v1_e8_glue",
      "v600_joint_embedding",
      "v634_st31_structure",
      "v2_carrier_pascal",
      "v3_em_alpha"
    ],
    "passed": 12,
    "total": 12
  },
  "anchors": {
    "recomputed": 3,
    "citations": {
      "Jacobi": 17,
      "Construction A": 10,
      "Shephard": 2
    },
    "arxivModules": 38
  },
  "lean": {
    "modules": 67
  },
  "openGates": {
    "count": 324
  }
};

/** Replay verdict enum of v649 (frozen). */
export const DISCIPLINE_VERDICT = "DISCIPLINE-CERTIFIED";
