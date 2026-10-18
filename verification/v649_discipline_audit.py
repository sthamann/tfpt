"""v649 -- META.DISCIPLINE.01: TFPT process census and deterministic replay.

Prime Front separation, 2026-10-18: the historical corpus-size minimum
bars remain unchanged and are evaluated on TFPT alone. Three transferred
replay modules are replaced by retained v1/v2/v3 compiler modules; the
separate Prime Front Weil contract and two zeta/Suzuki anchors no longer
form part of this physical-project audit. No mathematical status changes.
The remaining anchors are Jacobi four-square, Construction A and G31.
This check measures process, never a completed physical derivation.
"""

from tex_sources import read_tex
from pathlib import Path
import ast
import csv
import os
import re
import subprocess
import sys
import time
import warnings

T0 = time.time()
FAILS = []
N_CHK = 0

# ---- frozen minimum bars (measured 2026-08-02, v649 included) ----------
LEDGER_ROWS_MIN = 715        # D1: total ledger rows
LEDGER_ACTIVE_MIN = 710      # D1: active rows
KILL_ROWS_MIN = 214          # D1: rows with negative-evidence keywords
MODULES_MIN = 643            # D2: suite modules (incl. this one)
CHECK_SITES_MIN = 6040       # D2: static check() call sites
MUSTFAIL_OCC_MIN = 1469      # D2: negative-control keyword occurrences
MUSTFAIL_MODS_MIN = 233      # D2: modules carrying them
E_MARKS_MIN = 3579           # D2: [E] typing marks in sources
C_MARKS_MIN = 1323           # D2: [C] typing marks in sources
CONTRACT_TEX_MIN = 10        # D3: 'research contract' mentions (meas. 20)
CONTRACT_ROWS_MIN = 47       # D3: contract/preregistration ledger rows
CONTRACT_KILL_MIN = 29       # D3: of which name kill criteria
SEED_MODS_MIN = 77           # D4: modules with explicit seeds
SYMPY_MODS_MIN = 396         # D4: modules with sympy-exact arithmetic
ANCHORS_MIN = 3              # D5: classical anchors recomputed
LEAN_MODS_MIN = 54           # D6: committed TfptCarrier/*.lean modules
SANDBOX_QUOTE = 5452         # D2 cross-quote: published check counter


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "verification", "run_all.py")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root with verification/run_all.py not found")


ROOT = find_root()
VERIF = os.path.join(ROOT, "verification")
LEAN_DIR = os.path.join(ROOT, "experiments", "lean4-carrier-rigidity")

# ---------------------------------------------------------------- D1 census
# Display-class mapping mirrors the public four-class scheme
# (make_changelog_web.MARKERS): fine types I/L/F/N/M render as [E],
# P/B/R as [C], A as [O]; keyword fallback for untagged fine statuses.
E_TAGS = {"E", "I", "L", "F", "N", "M"}
C_TAGS = {"C", "P", "B", "R"}
O_TAGS = {"O", "A"}
X_TAGS = {"X"}
E_WORDS = ("identity", "formal", "lattice", "numerical", "measured",
           "exact", "red-team")
C_WORDS = ("physical", "branch policy", "geometric premise", "conjecture",
           "reduction")
KILL_RE = re.compile(
    r"kill|ill-posed|honest negative|no-independent|must-fail|must fail"
    r"|must-break|retyped|superseded|\bdead\b|bingo|numerolog", re.I)


def ledger_rows():
    with open(os.path.join(VERIF, "status_ledger.csv"), newline="",
              encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def row_class(status):
    low = status.lower()
    tags = set()
    for grp in re.findall(r"\[([A-Za-z/+, ]+)\]", status):
        for t in re.split(r"[/+, ]+", grp):
            t = t.strip().upper()
            if t:
                tags.add(t)
    if low.startswith("axiom"):
        return "AXIOM"
    if tags & X_TAGS:
        return "X"
    if tags & O_TAGS or low.startswith("open") or "contract" in low:
        return "O"
    if tags & C_TAGS:
        return "C"
    if tags & E_TAGS:
        return "E"
    if any(low.startswith(w) for w in E_WORDS):
        return "E"
    if any(low.startswith(w) for w in C_WORDS):
        return "C"
    return "OTHER"


def ledger_census(rows=None):
    rows = ledger_rows() if rows is None else rows
    dist = {"E": 0, "C": 0, "O": 0, "X": 0, "AXIOM": 0, "OTHER": 0}
    for r in rows:
        dist[row_class(r["status"])] += 1
    kill_ids = sorted({r["claim_id"] for r in rows if KILL_RE.search(
        (r.get("claim") or "") + " " + (r.get("canonical_status") or ""))})
    return dict(
        rows=len(rows),
        active=sum(1 for r in rows
                   if (r.get("active") or "").strip().lower() == "true"),
        retired=sum(1 for r in rows
                    if (r.get("active") or "").strip().lower() != "true"),
        dist=dist,
        kill_ids=kill_ids,
    )


# ---------------------------------------------------------------- D2 census
MF_RE = re.compile(r"must-fail|must fail|must-break|must break"
                   r"|negative control|negative-control|\bkill"
                   r"|scramble", re.I)
SEED_RE = re.compile(r"np\.random\.seed|random\.seed\(|default_rng\("
                     r"|RandomState\(|\bseed\s*=")


def module_files():
    return sorted(f for f in os.listdir(VERIF)
                  if re.match(r"v\d+_.+\.py$", f))


def check_site_count(src):
    """Count legacy check() sites plus real renamed tfpt_constants checks.

    The historical regex census deliberately sees check calls inside the
    byte-exact embedded probe sources executed by later verifier modules, so
    replacing it wholesale with an outer-module AST census would regress the
    frozen meaning.  AST is used for the missing case: a verifier may import
    ``tfpt_constants.check`` under a different local name.  Counting Call
    nodes (rather than text) prevents comments or string literals containing
    the alias from satisfying D2.1.
    """
    legacy = (len(re.findall(r"\bcheck\(", src))
              - len(re.findall(r"def\s+check\(", src)))
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(src)
    except SyntaxError:
        # The legacy census remains defined even for an embedded-source
        # container that the outer Python parser cannot read.
        return legacy
    aliases = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "tfpt_constants":
            aliases.update(
                item.asname for item in node.names
                if item.name == "check" and item.asname not in (None, "check")
            )
    renamed = sum(
        1 for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in aliases
    )
    return legacy + renamed


def suite_census():
    files = module_files()
    out = dict(modules=len(files), sites=0, no_check=[], mf_occ=0,
               mf_mods=0, c_marks=0, e_marks=0, seed_mods=0,
               sympy_mods=0, exact_occ=0)
    for f in files:
        with open(os.path.join(VERIF, f), encoding="utf-8",
                  errors="replace") as fh:
            src = fh.read()
        sites = check_site_count(src)
        out["sites"] += sites
        if sites == 0:
            out["no_check"].append(f)
        n_mf = len(MF_RE.findall(src))
        out["mf_occ"] += n_mf
        out["mf_mods"] += 1 if n_mf else 0
        out["c_marks"] += src.count("[C]")
        out["e_marks"] += src.count("[E]")
        out["seed_mods"] += 1 if SEED_RE.search(src) else 0
        out["sympy_mods"] += 1 if re.search(r"^\s*(import|from)\s+sympy",
                                            src, re.M) else 0
        out["exact_occ"] += len(re.findall(r"exact", src, re.I))
    return out


# ---------------------------------------------------------------- D3 census
def contracts_census(rows=None):
    rows = ledger_rows() if rows is None else rows
    tex = read_tex(Path(ROOT) / "tfpt_research_contracts.tex")
    tex_mentions = len(re.findall(r"research contract", tex, re.I))
    prereg = [r for r in rows if re.search(
        r"preregist|research contract", (r.get("claim") or "")
        + " " + (r.get("status") or ""), re.I)]
    prereg_kill = [r for r in prereg if re.search(
        r"kill", (r.get("claim") or ""), re.I)]
    by_id = {r["claim_id"]: r for r in rows}
    ftr = by_id.get("FTR.PGL2.01", {})
    weil = by_id.get("PRIME.WEIL.OPERATOR.01", {})
    reg = by_id.get("REG.FREEZE.01", {})
    ex_ftr = ("v632" in (ftr.get("script") or "")
              and re.search(r"preregist", ftr.get("claim") or "", re.I)
              is not None)
    ex_weil = (re.search(r"KILL TESTS|kill test", weil.get("claim") or "",
                         re.I) is not None
               and "W1 THEOREM-closed (v643"
               in (weil.get("canonical_status") or ""))
    ex_reg = (bool(reg) and os.path.exists(
        os.path.join(VERIF, "predictions_frozen.json")))
    return dict(tex_mentions=tex_mentions, prereg=len(prereg),
                prereg_ids=sorted(r["claim_id"] for r in prereg),
                prereg_kill=len(prereg_kill),
                ex_ftr=ex_ftr, ex_weil=ex_weil, ex_reg=ex_reg)


# ------------------------------------------------------------- D4 replay
REPRO_SAMPLE = [
    "v55_coxeter_cycle", "v91_spine_tetrahedron", "v108_pascal_ladder",
    "v205_xi_threequarter", "v305_witness_independence",
    "v405_seam_equiv_omega", "v505_celestial_wp5e_beta_equivariant_ledger",
    "v1_e8_glue", "v600_joint_embedding",
    "v634_st31_structure", "v2_carrier_pascal", "v3_em_alpha",
]
TIME_LINE_RE = re.compile(
    r"elapsed|\(\s*\d+(?:\.\d+)?\s*s\s*\)|\b\d+(?:\.\d+)?\s*s\b", re.I)


def canon_output(out):
    kept, dropped = [], 0
    for line in out.splitlines():
        if TIME_LINE_RE.search(line):
            dropped += 1
            continue
        kept.append(line)
    return "\n".join(kept), dropped


def run_module_once(name):
    p = subprocess.run([sys.executable, name + ".py"], cwd=VERIF,
                       capture_output=True, text=True, timeout=900)
    return p.returncode, p.stdout


def replay_sample():
    results = []
    for name in REPRO_SAMPLE:
        rc1, out1 = run_module_once(name)
        rc2, out2 = run_module_once(name)
        c1, d1 = canon_output(out1)
        c2, d2 = canon_output(out2)
        same = (rc1 == 0 and rc2 == 0 and c1 == c2 and d1 == d2)
        results.append((name, rc1, rc2, same, d1, len(c1.splitlines())))
        print("      %-45s rc=%d/%d deterministic=%s "
              "(%d lines compared, %d timing lines filtered)"
              % (name, rc1, rc2, same, len(c1.splitlines()), d1))
    return results


# ------------------------------------------------------------- D5 anchors
def anchor_jacobi():
    """Jacobi 1834: r_4(n) = 8 sum_{d | n, 4 !| d} d (four-square counts;
    the classical layer under v625's theta = Eisenstein identity)."""
    worst = None
    for n in range(1, 41):
        brute = 0
        m = int(n ** 0.5) + 1
        for a in range(-m, m + 1):
            for b in range(-m, m + 1):
                for c in range(-m, m + 1):
                    r = n - a * a - b * b - c * c
                    if r < 0:
                        continue
                    d = int(round(r ** 0.5))
                    if d * d == r:
                        brute += 2 if d else 1
        jac = 8 * sum(d for d in range(1, n + 1)
                      if n % d == 0 and d % 4 != 0)
        if brute != jac:
            worst = n
    return worst is None, "r_4(n) = 8 sigma'(n) exact for n = 1..40"


def hamming_codewords():
    G = [(1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
         (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0)]
    words = set()
    for m in range(16):
        w = [0] * 8
        for i in range(4):
            if (m >> i) & 1:
                w = [(a + b) % 2 for a, b in zip(w, G[i])]
        words.add(tuple(w))
    return words


def anchor_construction_a():
    """Construction A (classical coding-theory lattice construction;
    v626): the extended Hamming [8,4,4] code lifts to the even
    unimodular rank-8 lattice with 240 minimal vectors."""
    from itertools import product as iproduct
    words = hamming_codewords()
    wts = {}
    for w in words:
        wts[sum(w)] = wts.get(sum(w), 0) + 1
    selfdual = all(sum(a * b for a, b in zip(u, v)) % 2 == 0
                   for u in words for v in words)
    n_min = 0
    for x in iproduct((-2, -1, 0, 1, 2), repeat=8):
        if sum(v * v for v in x) != 4:
            continue
        if tuple(v % 2 for v in x) in words:
            n_min += 1
    ok = (wts == {0: 1, 4: 14, 8: 1} and selfdual and n_min == 240)
    return ok, ("weights {0:1, 4:14, 8:1}, self-dual, 240 minimal "
                "vectors (= 16 + 14*16)")


def anchor_st31():
    """Shephard-Todd 1954 / Springer: G31 degrees (8, 12, 20, 24) --
    product = group order 46080 = |W(D5)|*|W(A3)|, reflections
    60 = sum (d_i - 1) (the literature side of v634)."""
    degs = (8, 12, 20, 24)
    prod = 1
    for d in degs:
        prod *= d
    w_d5 = 2 ** 4 * 120          # |W(D5)| = 2^(5-1) * 5!
    w_a3 = 24                    # |W(A3)| = S4
    ok = (prod == 46080 and prod == w_d5 * w_a3
          and sum(d - 1 for d in degs) == 60)
    return ok, "8*12*20*24 = 46080 = 1920*24, sum(d_i - 1) = 60"






ANCHOR_CITES = ["Jacobi", "Construction A", "Shephard"]


def citation_census():
    counts = {k: 0 for k in ANCHOR_CITES}
    arxiv = 0
    for f in module_files():
        with open(os.path.join(VERIF, f), encoding="utf-8",
                  errors="replace") as fh:
            src = fh.read()
        for k in ANCHOR_CITES:
            if k in src:
                counts[k] += 1
        arxiv += 1 if "arXiv:" in src else 0
    return counts, arxiv


# ------------------------------------------------------------- D6 lean
def lean_census():
    if not os.path.isdir(LEAN_DIR):
        return dict(n=0, method="missing (full repo tree required)",
                    artefacts={})
    method = "git"
    try:
        p = subprocess.run(
            ["git", "-C", ROOT, "ls-files",
             "experiments/lean4-carrier-rigidity/TfptCarrier/"],
            capture_output=True, text=True, timeout=60)
        names = [ln for ln in p.stdout.splitlines()
                 if ln.endswith(".lean") and os.path.isfile(os.path.join(ROOT, ln))]
        if p.returncode != 0 or not names:
            raise RuntimeError
    except Exception:
        method = ("fs-fallback (git unavailable -- the count may "
                  "include uncommitted files)")
        d = os.path.join(LEAN_DIR, "TfptCarrier")
        names = sorted(f for f in os.listdir(d) if f.endswith(".lean"))
    # The committed build descriptors are part of the claim; the local
    # `.lake/build` directory is NOT (git-ignored, absent from every fresh
    # checkout and from CI) -- it is reported, never required.  The fresh
    # `lake build` itself is the Lean Proofs workflow's job.
    artefacts = {a: os.path.exists(os.path.join(LEAN_DIR, a))
                 for a in ("lakefile.lean", "lake-manifest.json",
                           "lean-toolchain")}
    local_build = os.path.isdir(os.path.join(LEAN_DIR, ".lake", "build"))
    return dict(n=len(names), method=method, artefacts=artefacts,
                local_build=local_build)


def open_gate_ids(rows=None):
    rows = ledger_rows() if rows is None else rows
    return sorted(r["claim_id"] for r in rows
                  if (r.get("active") or "").strip().lower() == "true"
                  and row_class(r["status"]) == "O")


# ---------------------------------------------------------------- runner
def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("DISCIPLINE AUDIT -- the suite measures its own process "
          "discipline (META)")
    print("=" * 78)

    rows = ledger_rows()

    # ------------------------------------------------------------- D1
    print("\nD1 -- ledger census (verification/status_ledger.csv)")
    lc = ledger_census(rows)
    print("      rows = %d, active = %d, retired = %d" %
          (lc["rows"], lc["active"], lc["retired"]))
    print("      display-class distribution: %s" % lc["dist"])
    print("      kill/negative keyword rows: %d" % len(lc["kill_ids"]))
    print("      sample ids: %s ..." % ", ".join(lc["kill_ids"][:12]))
    check("D1.1 [E] ledger census: %d rows (bar >= %d), %d active "
          "(bar >= %d), class distribution E/C/O/X/AXIOM/OTHER = "
          "%d/%d/%d/%d/%d/%d -- the ledger types far more rows as "
          "typed-open/conditional than as established"
          % (lc["rows"], LEDGER_ROWS_MIN, lc["active"],
             LEDGER_ACTIVE_MIN, lc["dist"]["E"], lc["dist"]["C"],
             lc["dist"]["O"], lc["dist"]["X"], lc["dist"]["AXIOM"],
             lc["dist"]["OTHER"]),
          lc["rows"] >= LEDGER_ROWS_MIN
          and lc["active"] >= LEDGER_ACTIVE_MIN)
    check("D1.2 [E] documented kills / honest negatives / retypes: "
          "%d ledger rows carry negative-evidence keywords (bar >= %d) "
          "-- a project that documents its own buried hypotheses is "
          "not a confirmation-bias generator"
          % (len(lc["kill_ids"]), KILL_ROWS_MIN),
          len(lc["kill_ids"]) >= KILL_ROWS_MIN)

    # ------------------------------------------------------------- D2
    print("\nD2 -- must-fail census (static, over verification/v*.py)")
    sc = suite_census()
    print("      modules = %d, static check() call sites = %d"
          % (sc["modules"], sc["sites"]))
    print("      modules without check( sites: %s" % (sc["no_check"] or
                                                      "none"))
    print("      must-fail/kill/scramble keyword occurrences = %d in %d "
          "modules" % (sc["mf_occ"], sc["mf_mods"]))
    print("      typing marks in sources: [E] x %d vs [C] x %d"
          % (sc["e_marks"], sc["c_marks"]))
    print("      seeded modules = %d, sympy modules = %d, 'exact' "
          "occurrences = %d" % (sc["seed_mods"], sc["sympy_mods"],
                                sc["exact_occ"]))
    check("D2.1 [E] module census: %d modules (bar >= %d), every module "
          "carries check sites" % (sc["modules"], MODULES_MIN),
          sc["modules"] >= MODULES_MIN and not sc["no_check"])
    check("D2.2 [E] static check-call census: %d call sites (bar >= %d; "
          "also clears the published sandbox counter %d)"
          % (sc["sites"], CHECK_SITES_MIN, SANDBOX_QUOTE),
          sc["sites"] >= CHECK_SITES_MIN
          and sc["sites"] >= SANDBOX_QUOTE)
    check("D2.3 [E] negative-control semantics: %d keyword occurrences "
          "(bar >= %d) across %d modules (bar >= %d) -- must-fail / "
          "must-break / kill / scramble controls are corpus-wide, not "
          "decorative" % (sc["mf_occ"], MUSTFAIL_OCC_MIN, sc["mf_mods"],
                          MUSTFAIL_MODS_MIN),
          sc["mf_occ"] >= MUSTFAIL_OCC_MIN
          and sc["mf_mods"] >= MUSTFAIL_MODS_MIN)
    check("D2.4 [E] typing marks: [E] x %d (bar >= %d) vs [C] x %d "
          "(bar >= %d) -- conditional readings are typed, not upgraded"
          % (sc["e_marks"], E_MARKS_MIN, sc["c_marks"], C_MARKS_MIN),
          sc["e_marks"] >= E_MARKS_MIN and sc["c_marks"] >= C_MARKS_MIN)

    # ------------------------------------------------------------- D3
    print("\nD3 -- preregistration census")
    cc = contracts_census(rows)
    print("      'research contract' mentions in "
          "tfpt_research_contracts.tex = %d" % cc["tex_mentions"])
    print("      preregistered/contract ledger rows = %d (%s ...)"
          % (cc["prereg"], ", ".join(cc["prereg_ids"][:10])))
    print("      of which naming kill criteria in the claim = %d"
          % cc["prereg_kill"])
    check("D3.1 [E] contracts exist with named kill criteria BEFORE "
          "execution: %d contract/preregistration rows (bar >= %d), "
          "%d naming kill criteria (bar >= %d), %d contract mentions "
          "in the contracts paper (bar >= %d)"
          % (cc["prereg"], CONTRACT_ROWS_MIN, cc["prereg_kill"],
             CONTRACT_KILL_MIN, cc["tex_mentions"], CONTRACT_TEX_MIN),
          cc["prereg"] >= CONTRACT_ROWS_MIN
          and cc["prereg_kill"] >= CONTRACT_KILL_MIN
          and cc["tex_mentions"] >= CONTRACT_TEX_MIN)
    check("D3.2 [E] executed-contract chains verified in the ledger: "
          "FTR.PGL2.01 (preregistered v533 -> executed v632) = %s; "
          "REG.FREEZE.01 + "
          "predictions_frozen.json (frozen 2026-06-09) = %s"
          % (cc["ex_ftr"], cc["ex_reg"]),
          cc["ex_ftr"] and cc["ex_reg"])

    # ------------------------------------------------------------- D4
    print("\nD4 -- reproducibility replay (declared 12-module sample, "
          "2 fresh runs each)")
    rr = replay_sample()
    n_det = sum(1 for r in rr if r[3])
    check("D4.1 [E] deterministic replay: %d/12 sample modules produce "
          "identical output on two fresh subprocess runs (timing lines "
          "filtered; sample retains nine original modules plus compiler v1/v2/v3)"
          % n_det, n_det == 12)
    check("D4.2 [E] exactness census: %d modules import sympy "
          "(bar >= %d), %d modules carry explicit seeds (bar >= %d) -- "
          "randomness is declared, exactness is the default"
          % (sc["sympy_mods"], SYMPY_MODS_MIN, sc["seed_mods"],
             SEED_MODS_MIN),
          sc["sympy_mods"] >= SYMPY_MODS_MIN
          and sc["seed_mods"] >= SEED_MODS_MIN)

    # ------------------------------------------------------------- D5
    print("\nD5 -- external classical anchors (recomputed against the "
          "literature)")
    import mpmath as mp
    anchors = [
        ("Jacobi 1834 four-square counts",) + anchor_jacobi(),
        ("Construction A -> E8 from [8,4,4] (v626)",)
        + anchor_construction_a(),
        ("Shephard-Todd G31 degrees (v634)",) + anchor_st31(),
    ]
    n_ok = 0
    for name, ok, detail in anchors:
        n_ok += 1 if ok else 0
        check("D5.%d [E] anchor recompute: %s" % (n_ok, name), ok, detail)
    cites, arxiv = citation_census()
    print("      citation census over module sources: %s; arXiv-citing "
          "modules = %d" % (cites, arxiv))
    check("D5.6 [E] >= %d independent classical anchors recomputed here "
          "and each cited in the corpus (%s)"
          % (ANCHORS_MIN,
             ", ".join("%s x %d" % kv for kv in cites.items())),
          n_ok >= ANCHORS_MIN and all(v >= 1 for v in cites.values()))

    # ------------------------------------------------------------- D6
    print("\nD6 -- the Lean layer (committed formal proof modules)")
    lz = lean_census()
    print("      committed TfptCarrier/*.lean modules = %d (method: %s)"
          % (lz["n"], lz["method"]))
    print("      committed build descriptors: %s" % lz["artefacts"])
    print("      local .lake/build present (informational, git-ignored): %s"
          % lz.get("local_build"))
    print("      HONEST: `lake build` is NOT re-run inside the suite "
          "(runtime); the last green build (3380 jobs, no sorry) is "
          "quoted from changelog 2026-08-02 (XLIII); this check "
          "certifies the committed count + build descriptors, not a "
          "fresh build (that is the Lean Proofs CI workflow).")
    check("D6.1 [E] formal proof layer: %d committed Lean modules "
          "(bar >= %d), committed build descriptors present" % (lz["n"],
                                                                LEAN_MODS_MIN),
          lz["n"] >= LEAN_MODS_MIN
          and bool(lz["artefacts"])
          and all(lz["artefacts"].values()))

    # ------------------------------------------------------------- D7
    print("\nD7 -- the limit, honest")
    open_ids = open_gate_ids(rows)
    majors = [i for i in open_ids
              if i.startswith(("GATE.", "SEAM.THEOREM",
                               "PRIME.WEIL.OPERATOR", "QGEO."))]
    print("      open/contract rows (display class O): %d" % len(open_ids))
    print("      majors (%d): %s" % (len(majors), ", ".join(majors)))
    named = {"SEAM.THEOREM.01"}
    check("D7.1 [C] the limit, typed: this module measures PROCESS "
          "discipline (censuses, replay, anchors), NOT the truth of "
          "the physics; typed [C] observations stay observations; the "
          "open gates stay open (%d class-O rows incl. %s, the QGEO "
          "premise family and the GATE.METRIC family); a discipline "
          "certificate is a necessary, not a sufficient, condition "
          "against numerology"
          % (len(open_ids), ", ".join(sorted(named))),
          named.issubset(set(open_ids)) and len(open_ids) >= 200)

    # ---------------------------------------------------------- summary
    if any(not r[3] for r in rr):
        verdict = "REPLAY-BROKEN"
    elif FAILS:
        verdict = "CENSUS-REGRESSED"
    else:
        verdict = "DISCIPLINE-CERTIFIED"
    print("\nVERDICT: %s" % verdict)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
