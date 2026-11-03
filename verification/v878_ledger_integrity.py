"""v878 -- GATE.LEDGER.01: the status-ledger integrity guard (a CI sentinel, no
new physics).  Round 36 booked the first PRIMARY-KEY violation found in
status_ledger.csv: the claim_id FORM.QGEO.03 had been double-booked on
2026-06-18 (the flat-metric all-orders SeamDeckClosure formalisation) while the
id already belonged to the CohomologyGrading formalisation (2026-06-15).  The
fix (this round): the SeamDeckClosure row is RENAMED FORM.QGEO.04 with a dated
QA note in its claim text, and every flat-closure reference (papers, scripts,
registry, website, the two 2026-06-18 changelog mentions) is updated.  This
module makes the whole class of bookkeeping errors impossible to reintroduce:

  [I] S1 SCHEMA: the 10-column header is exact; every row has a nonempty
      claim_id matching the id grammar; active in {true, false}.
  [I] S2 PRIMARY KEY: claim_id is globally unique (all rows -- hence a fortiori
      unique among active rows); the round-36 fix is pinned (FORM.QGEO.03
      occurs exactly once, FORM.QGEO.04 exists and carries the QA note).
  [I] S3 SUPERSESSION: every supersedes target exists in the ledger; the
      supersession graph is ACYCLIC (Tarjan) with no self-supersession.
  [I] S4 UNIQUE ACTIVE SUPERSESSION TARGETS: no target is superseded by more
      than one active row, modulo the FROZEN remove-only allowlist of the two
      legitimate 2026-06 joint closures (FLAV.UGATE.01 <- FLAV.RIGID.01 +
      FLAV.RIGID.02; GATE.QGEO.01 <- FLAV.QGEO.02 + FLAV.QGEO.03) -- any NEW
      multi-supersession fails the suite.
  [I] S5 DEPENDENCY CROSS-REFERENCES (typed honestly): the dependencies column
      is a semicolon-separated CROSS-REFERENCE field (evidence pointers, often
      mutual), NOT a build DAG -- the measured graph contains 13 strongly
      connected components (265 ids) of mutual references, all historical.
      Explicit retained references to claims moved to Prime Front resolve to
      that external owner, not to a local TFPT claim or proof dependency.
      The guard freezes that census REMOVE-ONLY: claim-like tokens that do not
      resolve to a ledger row must stay within the frozen 37-token legacy list
      (renamed/compressed ids and range notations like FLAV.QGEO.01-03), the
      set of ids participating in reference cycles must stay a subset of the
      frozen 265, the SCC count must not grow beyond 13, and no row may
      reference itself.  Acyclicity is thereby enforced as NO NEW CYCLES; the
      frozen baseline may only shrink (audit_baseline.json precedent).

  Python-only (stdlib csv/re over verification/status_ledger.csv).
"""
import csv
import os
import re
import sys

from tfpt_constants import check, summary, reset

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "status_ledger.csv")

EXPECT_HEADER = ["claim_id", "claim", "status", "location", "dependencies",
                 "script", "external_data", "supersedes", "canonical_status",
                 "active"]

# id grammar: dotted upper-case tokens ending in a number (optional letter
# suffix), hyphens allowed inside segments (SEAM.S3.FROM-P1.01).
ID_RE = re.compile(r"^[A-Z][A-Z0-9_.\-]*[0-9][a-z]?$")

# FROZEN (2026-08-08, round 36; REMOVE-ONLY): the two legitimate 2026-06
# joint closures where two active theorems supersede one gate together.
ALLOWED_MULTI_SUPERSEDE = {
    "FLAV.UGATE.01": frozenset({"FLAV.RIGID.01", "FLAV.RIGID.02"}),
    "GATE.QGEO.01": frozenset({"FLAV.QGEO.02", "FLAV.QGEO.03"}),
}

# FROZEN (2026-08-08, round 36; REMOVE-ONLY): claim-like dependency tokens
# that do not resolve to a ledger row -- historical renames/compressions and
# range notations.  New dangling references fail the suite.
LEGACY_DANGLING_DEPS = frozenset({
    "ARCH.HEXRES.01", "ARCH.QBL.01", "ARCH.RR.01", "BND.GLUE.01",
    "CASCADE.BRIDGE.01", "COX.TOTATIVE.01", "DIAMOND.CENTER.01",
    "E8.CAS.01", "EM.B1.01", "FLAV.DIAMOND.01-02", "FLAV.LEPTON.01",
    "FLAV.QGEO.01-03", "FLAV.SELECTOR.01", "FLAV.SHEET.01-03",
    "FR.POLE.01", "FTR.IHARA.01", "GATE.METRIC.05-07",
    "GATE.METRIC.XI.01", "HOR.DUALANCHOR.01", "HOR.PAGE.01",
    "MARKS.GB.01", "NOUNIT.01", "PRIME.FALSIFIER.01",
    "PRIME.RELATION.MANGOLDT.01", "QBL.GATE.01", "QGEO.CAR.01",
    "QGEO.COHOM.01", "QGEO.NET.01", "QGEO.ORBIFOLD.01",
    "QGEO.UNIFORM.01", "REDTEAM.A.01-E.01", "SEAM.ATTRACT.01",
    "SEAM.COX.01", "SEAM.TRANSFER.01", "THETA13.PRESSURE.01",
    "TRANSPORT.SIXTHROOT.01", "WITNESS.INDEP.01",
})

# Exact historical cross-references whose owner moved in split commit c5135cf4.
# Every id exists in that commit's predecessor ledger. QGEO.CONEDYN.01 was
# v699's PRIME determinant-coordinate cone experiment, despite its prefix.
# These are external provenance pointers, not local claims, runtime inputs or
# additions to the frozen dangling-reference baseline. Do not allow a prefix
# wildcard: an unregistered new PRIME.* reference must still fail.
EXTERNAL_CLAIM_OWNERS = dict.fromkeys({
    "PRIME.FLOOR.RATIO.01", "PRIME.HECKEMODRAM.01",
    "PRIME.HECKEPOLARITY.01", "PRIME.KEYSTONE.01", "PRIME.MOONSHOT.01",
    "PRIME.POSITIVE_DESCENT.01", "PRIME.RELATION.MULT.01",
    "PRIME.SHADOW.01", "PRIME.UNIFC.01", "PRIME.WEIL.OPERATOR.01",
    "QGEO.CONEDYN.01",
}, "https://github.com/sthamann/prime-front")

# FROZEN (2026-08-08, round 36; REMOVE-ONLY): the ids participating in
# mutual-reference cycles of the dependencies cross-reference field (13 SCCs,
# 265 ids -- all historical, none added after this freeze).
FROZEN_CYCLE_SCC_MAX = 13
FROZEN_CYCLE_IDS = frozenset({
    'ARCH.K3.01', 'ARCH.RRCAR.01', 'ARCH.RRCAR.02', 'AX.P1.01',
    'AX.P2.01', 'CAR.COUNT.01', 'CAR.LADDER.01', 'CAR.PAIR.01',
    'CAR.PAIR.02', 'CAR.PASCAL.01', 'CAR.QFREE.01', 'CAR.QTRANS.01',
    'CELEST.DTERM.NONDERIV.01', 'CELEST.SEAM.01', 'CELEST.WP1.01',
    'CELEST.WP2.01', 'CELEST.WP3.01', 'CELEST.WP4.01', 'CELEST.WP5A.01',
    'CELEST.WP5B.01', 'CELEST.WP5C.01', 'CELEST.WP5D.01',
    'CELEST.WP5DB.01', 'CELEST.WP5E.ALPHA.01', 'CELEST.WP5E.BETA.01',
    'CELEST.WP5E.DELTA1.01', 'CELEST.WP5E.DELTA2.01',
    'CELEST.WP5E.EPS1.01', 'CELEST.WP5E.EPS2.01', 'CELEST.WP5E.GAMMA.01',
    'CELEST.WP5E.M1.01', 'CELEST.WP5E.M2.01', 'CELEST.WP5E.M3.01',
    'CONTRACT.G.01', 'CONTRACT.QFT4D.01', 'CONTRACT.QFT4D.DIRAC.01',
    'DHR.MODULAR.01', 'DHR.SECTORS.01', 'DHR.SMATRIX.01', 'DYN.GNS.01',
    'DYN.KMS.01', 'DYN.SEMIGROUP.01', 'E8.GRADE.01', 'E8.PROJHAMMING.01',
    'FLATAWAY.A2.01', 'FLATAWAY.HEAT.01', 'FLATAWAY.RIGID.01',
    'FLATAWAY.RP.01', 'FLATAWAY.SPEC.01', 'FORM.CAR.01',
    'FORM.FLATAWAY.01', 'FORM.GLUE.01', 'FORM.LADDER.01', 'FORM.P2.02',
    'FORM.PRIME.EXCESS.SKELETON.01', 'FORM.PRIME.GRADE.NO_GO.01',
    'FORM.PRIME.KREIN.DEFECT.01', 'FORM.QGEO.01', 'FORM.QGEO.02',
    'FORM.QGEO.04', 'FORM.SEAM.MMST.01', 'FORM.SEAM.RESIDUAL.01',
    'GATE.HOLO.01', 'GATE.HOLO.02', 'GATE.HOLO.03', 'GATE.METRIC.01',
    'GATE.METRIC.02', 'GATE.METRIC.03', 'GATE.METRIC.04',
    'GATE.METRIC.05', 'GATE.METRIC.06', 'GATE.METRIC.07',
    'GATE.METRIC.08', 'GATE.METRIC.09', 'GATE.METRIC.10',
    'GATE.METRIC.11', 'GATE.METRIC.12', 'GATE.METRIC.13',
    'GATE.METRIC.14', 'GATE.METRIC.15', 'GATE.METRIC.16',
    'GATE.METRIC.17', 'GATE.METRIC.18', 'GATE.METRIC.19',
    'GNET.RAMIFIED.01', 'GRAV.ENTROPY.EQUILIBRIUM.01', 'GRAV.FR.01',
    'GRAV.NONLINEAR.01', 'MARKLOCAL.RAW.01', 'MCKAY.E8.01',
    'P2.PARTITION.01', 'P2.TYPING.01', 'PRIME.ABELPAIR.01',
    'PRIME.ANTIALIAS.01', 'PRIME.BAEZDUARTE.01',
    'PRIME.CORNER.CHARACTER.01', 'PRIME.CORNER.EXPECTATION.01',
    'PRIME.CORNER.OPENDOORS.01', 'PRIME.DETECTOR.WINDOW.01',
    'PRIME.EULER.SCHUR.SEMIGROUP.01', 'PRIME.EXCLUSION.BATTERY2.01',
    'PRIME.EXCLUSION.LADDER.01', 'PRIME.EXCLUSION.LOCATOR.01',
    'PRIME.EXCLUSION.WINDOW.01', 'PRIME.FLOOR.ALIASMOMENT.01',
    'PRIME.FLOOR.BRIDGEMAP.01', 'PRIME.FLOOR.BUDGET.01',
    'PRIME.FLOOR.DEPTHKILL.01', 'PRIME.FLOOR.GUEABLATION.01',
    'PRIME.FLOOR.LAGRANGE.01', 'PRIME.FLOOR.PAIRCORR.01',
    'PRIME.FLOOR.RATIO.01', 'PRIME.FLOOR.SKELETON.01', 'PRIME.GATE0.01',
    'PRIME.GRAM.DIAGONAL.01', 'PRIME.GROUNDTRUTH.01',
    'PRIME.HANDOFFBULK.01', 'PRIME.HANDOFFGRAM.01',
    'PRIME.HANDOFFREDTEAM.01', 'PRIME.HANDOFFRES.01',
    'PRIME.HANDOFFTAIL.01', 'PRIME.HECKEMODRAM.01',
    'PRIME.HECKEPOLARITY.01', 'PRIME.HECKESOS.01',
    'PRIME.HECKETWOSTEP.01', 'PRIME.KEIPERLI.01', 'PRIME.KEYSTONE.01',
    'PRIME.KMS.INDUCTIVE_STATE.01', 'PRIME.KMS.INDUCTIVE_STATE.02',
    'PRIME.KMSEXT.01', 'PRIME.KMSSTINESPRING.01', 'PRIME.KMSTOEPLITZ.01',
    'PRIME.KREIN.CONTRACTOR.01', 'PRIME.KREIN.DEFECT_ONE.01',
    'PRIME.KREIN.NORMALFORM.01', 'PRIME.L1IDENT.01', 'PRIME.L1MONTAGE.01',
    'PRIME.LKSPLIT.01', 'PRIME.MARGIN.LAW.01', 'PRIME.MOONSHOT.01',
    'PRIME.MOONSHOT.02', 'PRIME.MOONSHOT.03', 'PRIME.MOONSHOT.04',
    'PRIME.MOONSHOT.05', 'PRIME.MOONSHOT.06', 'PRIME.PD.PERSISTENCE.01',
    'PRIME.QFBUNDLE.01', 'PRIME.QFCENSUS.01', 'PRIME.QFCOCYCLE.01',
    'PRIME.QFFESHBACH.01', 'PRIME.QFGAUGE.01', 'PRIME.RELATION.MULT.01',
    'PRIME.RELATION.SKELETON.01', 'PRIME.S1CANON.01', 'PRIME.SCHURREC.01',
    'PRIME.SOFTPORT.FESHBACH.01', 'PRIME.SOURCECONTRACTOR.NORM.01',
    'PRIME.TOWERNEST.01', 'PRIME.TURINGCERT.01', 'PRIME.UCPLIMIT.01',
    'PRIME.UNIFPOS.01', 'PRIME.W3LAND.01', 'PRIME.YOSIDAQF.01',
    'PRIME.Z1.MOONSHOT.01', 'PRIME.Z1.OPERATOR.01', 'PRIME.Z1JACOBI.01',
    'PRIME.Z1MEASURE.01', 'PRIME.Z1UVAROV.01', 'PS.ALGEBRA.01',
    'PS.DIRAC.01', 'PS.DIRAC.02', 'PS.DIRAC.03', 'PS.E8BRANCH.01',
    'PS.KAPPA.01', 'PS.RGTEST.01', 'PS.SPECACT.01', 'PS.SPECACT.02',
    'QFT.MSC.01', 'QFT.NETRP.01', 'QFT4D.FORK.01', 'QFT4D.MATTER.01',
    'QFT4D.RGTEST.01', 'QFT4D.SPERT.01', 'QG.AMB.01', 'QG.G2.01',
    'QG.GAPDEC.01', 'QGAMB.CONFORMAL.01', 'QGAMB.IDG.01',
    'QGAMB.MEASURE.01', 'QGAMB.METRIC.01', 'QGAMB.MODULAR.01',
    'QGAMB.ROADMAP.01', 'QGAMB.ROUTEII.01', 'QGAMB.TIERB.01',
    'QGAMB.UNIFY.01', 'QGEO.BW.01', 'QGEO.CONF.01', 'QGEO.DECKSECTOR.01',
    'QGEO.DTN.01', 'QGEO.EMERGE.LIGHT.01', 'QGEO.ENERGY.01',
    'QGEO.ENERGY.02', 'QGEO.ENERGY.03', 'QGEO.ISO.01', 'QGEO.KERNEL.01',
    'QGEO.KILL.01', 'QGEO.MARKLOCAL.01', 'QGEO.MARKS.01', 'QGEO.MARKS.02',
    'QGEO.MARKS.03', 'QGEO.MODHAM.01', 'QGEO.MODULAR.01', 'QGEO.OBLIG.01',
    'QGEO.PILLOW.01', 'QGEO.REALIZE.01', 'QGEO.REALIZE.02',
    'QGEO.REDUCE.01', 'QGEO.ROUTEI.01', 'QGEO.STATE.01',
    'QGEO.STEKLOV.01', 'QGEO.SUBPRIN.01', 'QGEO.SYM.01', 'QGEO.SYM.02',
    'QGEO.SYM.03', 'QGEO.TREE.01', 'QGEO.VARI.01', 'REDTEAM.A.01',
    'REDTEAM.B.01', 'SEAM.ADVERSARY.01', 'SEAM.BIT.FREEDOM.01',
    'SEAM.BIT.ORIGIN.01', 'SEAM.BIT.TWISTCLASS.01', 'SEAM.CCC.01',
    'SEAM.CLOCK.RIGIDITY.01', 'SEAM.CLOCK.SILVER.01', 'SEAM.EQUIV.01',
    'SEAM.EQUIV.A.INV.01', 'SEAM.EQUIV.A.LIT.01', 'SEAM.EQUIV.A01',
    'SEAM.EQUIV.B01', 'SEAM.EQUIV.CHAIN.01', 'SEAM.EQUIV.CONTINUUM.03',
    'SEAM.EQUIV.CROSSEDPRODUCT.01', 'SEAM.EQUIV.GAP.01',
    'SEAM.EQUIV.LATTICEVOA.01', 'SEAM.EQUIV.MMST.01',
    'SEAM.EQUIV.MMST.AUDIT.01', 'SEAM.EQUIV.TWISTOR.01',
    'SEAM.INT.FKTOY.01', 'SEAM.KHALF.01', 'SEAM.MMST.INCLASS.01',
    'SEAM.MU.01', 'SEAM.S3.CENTRALCHARGE.01', 'SEAM.S3.E8CHARACTER.01',
    'SEAM.S3.INFLOW.01', 'SEAM.S3.LATTICE.01', 'SEAM.S3.MODULAR.01',
    'SEAM.S3.RP.01', 'SEAM.TAU.FLAG.01', 'SEAM.THERMAL.KMS.01',
    'SECTOR.FLOORATTACK.01', 'SYNTH.INVENTORY.02',
    'TFPT.POSITIVE_DESCENT.MASTER.01', 'TOPO.E8.01', 'WOIT.OS.TWISTOR.01',
})


def _split(field):
    return [x.strip() for x in field.split(";")
            if x.strip() and x.strip() != "-"]


def _claimlike(tok):
    return "." in tok and ID_RE.match(tok) is not None


def _sccs(graph):
    """Tarjan strongly connected components (iterative)."""
    idx, low, on, order = {}, {}, {}, []
    stack, out = [], []
    for root in graph:
        if root in idx:
            continue
        work = [(root, 0)]
        while work:
            v, pi = work.pop()
            if pi == 0:
                idx[v] = low[v] = len(idx)
                order.append(v)
                on[v] = True
            recurse = False
            nbrs = graph.get(v, [])
            for i in range(pi, len(nbrs)):
                w = nbrs[i]
                if w not in idx:
                    work.append((v, i + 1))
                    work.append((w, 0))
                    recurse = True
                    break
                if on.get(w):
                    low[v] = min(low[v], idx[w])
            if recurse:
                continue
            if low[v] == idx[v]:
                comp = []
                while True:
                    w = order.pop()
                    on[w] = False
                    comp.append(w)
                    if w == v:
                        break
                if len(comp) > 1:
                    out.append(sorted(comp))
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[v])
    return out


def run():
    reset()
    print("v878 ledger integrity guard: primary key, supersession, "
          "cross-reference census of status_ledger.csv")

    with open(LEDGER, newline="", encoding="utf-8") as fh:
        rdr = csv.reader(fh)
        header = next(rdr)
        raw = list(rdr)
    rows = [dict(zip(header, r)) for r in raw]
    ids = [r["claim_id"] for r in rows]
    idset = set(ids)
    active = [r for r in rows if r["active"] == "true"]

    # ---- S1 schema
    check("S1.1 SCHEMA [I]: header is the exact 10-column contract %s"
          % (EXPECT_HEADER,), header == EXPECT_HEADER)
    bad_width = [i for i, r in enumerate(raw) if len(r) != len(EXPECT_HEADER)]
    bad_gram = [i for i in ids if not _claimlike(i)]
    bad_act = sorted({r["active"] for r in rows} - {"true", "false"})
    check("S1.2 SCHEMA [I]: %d rows, every row 10 fields (bad: %s), every "
          "claim_id nonempty + id grammar (bad: %s), active in {true, false} "
          "(bad: %s)" % (len(rows), bad_width[:5], bad_gram[:5], bad_act),
          not bad_width and not bad_gram and not bad_act)

    # ---- S2 primary key
    dup_all = sorted({i for i in idset if ids.count(i) > 1})
    act_ids = [r["claim_id"] for r in active]
    dup_act = sorted({i for i in set(act_ids) if act_ids.count(i) > 1})
    check("S2.1 PRIMARY KEY [I]: claim_id globally unique -- %d rows, %d "
          "distinct ids, duplicates: %s (hence unique among the %d active "
          "rows too: %s)" % (len(rows), len(idset), dup_all or "none",
                             len(active), dup_act or "none"),
          not dup_all and not dup_act)
    q3 = [r for r in rows if r["claim_id"] == "FORM.QGEO.03"]
    q4 = [r for r in rows if r["claim_id"] == "FORM.QGEO.04"]
    check("S2.2 THE ROUND-36 FIX PINNED [I]: FORM.QGEO.03 occurs exactly "
          "once (the CohomologyGrading row) and FORM.QGEO.04 exists (the "
          "renamed SeamDeckClosure flat all-orders closure, dated QA note "
          "in the claim text)",
          len(q3) == 1 and "CohomologyGrading" in q3[0]["claim"]
          and len(q4) == 1 and "SeamDeckClosure" in q4[0]["claim"]
          and "QA NOTE (2026-08-08" in q4[0]["claim"])

    # ---- S3 supersession
    sup = {r["claim_id"]: [t for t in _split(r["supersedes"])] for r in rows}
    dangling = sorted({t for ts in sup.values() for t in ts
                       if t not in idset})
    check("S3.1 SUPERSESSION TARGETS EXIST [I]: every supersedes entry "
          "resolves to a ledger row (dangling: %s)" % (dangling or "none"),
          not dangling)
    sgraph = {k: [t for t in ts if t in idset] for k, ts in sup.items()}
    scycles = _sccs(sgraph)
    selfsup = sorted(k for k, ts in sgraph.items() if k in ts)
    check("S3.2 SUPERSESSION ACYCLIC [I]: the supersedes graph has no "
          "cycles (SCCs > 1: %s) and no self-supersession (%s)"
          % (scycles or "none", selfsup or "none"),
          not scycles and not selfsup)

    # ---- S4 unique active supersession targets (frozen allowlist)
    by_target = {}
    for r in active:
        for t in _split(r["supersedes"]):
            by_target.setdefault(t, []).append(r["claim_id"])
    multi = {t: sorted(v) for t, v in by_target.items() if len(v) > 1}
    new_multi = {t: v for t, v in multi.items()
                 if set(v) != ALLOWED_MULTI_SUPERSEDE.get(t, frozenset())}
    check("S4.1 UNIQUE ACTIVE SUPERSESSION TARGETS [I]: no target is "
          "superseded by more than one active row beyond the FROZEN "
          "remove-only allowlist of the two 2026-06 joint closures "
          "(measured multi: %s; violations: %s)"
          % (multi or "none", new_multi or "none"), not new_multi)

    # ---- S5 dependency cross-references (frozen census, remove-only)
    dep_tokens = {r["claim_id"]: _split(r["dependencies"]) for r in rows}
    external = sorted({t for ts in dep_tokens.values() for t in ts
                       if t in EXTERNAL_CLAIM_OWNERS and t not in idset})
    unknown = sorted({t for ts in dep_tokens.values() for t in ts
                      if _claimlike(t) and t not in idset
                      and t not in EXTERNAL_CLAIM_OWNERS})
    new_unknown = sorted(set(unknown) - LEGACY_DANGLING_DEPS)
    print("  External dependency provenance (Prime Front, not local claims): "
          "%s" % (external or "none"))
    check("S5.1 DEPENDENCY REFERENCES [I]: %d claim-like tokens do not "
          "resolve to a ledger row, ALL within the frozen 37-token legacy "
          "list (new dangling: %s)" % (len(unknown), new_unknown or "none"),
          not new_unknown and len(unknown) <= len(LEGACY_DANGLING_DEPS))
    dgraph = {k: [t for t in ts if t in idset]
              for k, ts in dep_tokens.items()}
    selfdep = sorted(k for k, ts in dgraph.items() if k in ts)
    check("S5.2 NO SELF-DEPENDENCY [I]: no row lists itself in its own "
          "dependencies (%s)" % (selfdep or "none"), not selfdep)
    dcycles = _sccs(dgraph)
    in_cyc = sorted({x for c in dcycles for x in c})
    new_cyc = sorted(set(in_cyc) - FROZEN_CYCLE_IDS)
    check("S5.3 NO NEW REFERENCE CYCLES [I]: the dependencies column is a "
          "cross-reference field (typed: mutual evidence pointers, not a "
          "build DAG); measured %d SCCs / %d ids in cycles, both within "
          "the frozen remove-only baseline (<= %d SCCs, subset of the "
          "frozen %d ids; NEW cycle members: %s)"
          % (len(dcycles), len(in_cyc), FROZEN_CYCLE_SCC_MAX,
             len(FROZEN_CYCLE_IDS), new_cyc or "none"),
          len(dcycles) <= FROZEN_CYCLE_SCC_MAX and not new_cyc)

    return summary("v878 ledger integrity guard (primary key + supersession "
                   "+ frozen cross-reference census)")


if __name__ == "__main__":
    sys.exit(1 if run() else 0)
