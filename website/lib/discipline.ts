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
    "rows": 1194,
    "active": 1189,
    "retired": 5,
    "dist": {
      "E": 403,
      "C": 275,
      "O": 398,
      "X": 42,
      "AXIOM": 2,
      "OTHER": 74
    },
    "killRows": 470
  },
  "suite": {
    "modules": 1028,
    "checkSites": 16647,
    "mustfailOccurrences": 9127,
    "mustfailModules": 544,
    "eMarks": 4583,
    "cMarks": 1563,
    "seededModules": 205,
    "sympyModules": 539
  },
  "contracts": {
    "ledgerRows": 168,
    "withKillCriteria": 105,
    "texMentions": 90
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
      "v555_pareto_tv_identities",
      "v600_joint_embedding",
      "v634_st31_structure",
      "v643_w1_theorem",
      "v648_sign_uncertainty"
    ],
    "passed": 12,
    "total": 12
  },
  "anchors": {
    "recomputed": 5,
    "citations": {
      "Jacobi": 68,
      "Hecke": 39,
      "Construction A": 12,
      "Suzuki": 31,
      "Weil": 113,
      "Eisenstein": 34
    },
    "arxivModules": 61
  },
  "lean": {
    "modules": 119
  },
  "openGates": {
    "count": 394
  }
};

/** Replay verdict enum of v649 (frozen). */
export const DISCIPLINE_VERDICT = "DISCIPLINE-CERTIFIED";
