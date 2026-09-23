#!/usr/bin/env python3
"""Build the TFPT theory graph from existing machine artefacts.

GENERATED OUTPUTS -- never edit by hand:
    verification/theory_graph.json   (nodes + edges + source hashes)
    verification/theory_primer.md    (compact human-readable summary)

Sources (all read-only):
    verification/status_ledger.csv        claims (1194) with status markers,
                                          location, dependencies, script, supersedes
    verification/script_registry.csv      script basename -> cluster/description
    verification/docs_map.csv             doc sections + cited scripts
    verification/predictions_frozen.json  frozen predictions
    experiments/evidence_scorecard.json   empirical scorecard rows (firewall)
    experiments/theory-contracts/<name>/  theory contracts (firewall):
                                          contract_index.json (new, preferred),
                                          validation.json (legacy), RESULTS.md /
                                          README.md verdict regex (legacy),
                                          run_normal/run_optimized.json, next.txt
    experiments/<dirname>/                every top-level experiment dir gets an
                                          experiment: node (no dead spots); root
                                          meta -> hub:experiments
    experiments/next.txt                  research log: contract verdict backfill
                                          + hub entry span
    rh/catalog/rh_semantic_catalog.json   RH round records (firewall)

Usage:
    python3 verification/build_theory_graph.py            # write graph + primer
    python3 verification/build_theory_graph.py --check    # exit 1 if any source
                                                          # hash drifted (audit gate)

Query the result with verification/theorycat.py (see theory_primer.md).
stdlib only -- runnable without the venv (build.sh calls it with python3).
"""
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERIF = ROOT / "verification"
GRAPH_V2_DIR = VERIF / "graph_v2"
EXPERIMENTS_DIR = ROOT / "experiments"
CONTRACTS_DIR = EXPERIMENTS_DIR / "theory-contracts"
NEXT_TXT = EXPERIMENTS_DIR / "next.txt"
GRAPH_PATH = VERIF / "theory_graph.json"
PRIMER_PATH = VERIF / "theory_primer.md"

SCHEMA_VERSION = 1
MARKER_RE = re.compile(r"\[([ECOXPLANF])\]")
DATE_SUFFIX_RE = re.compile(r"-(\d{8})$")
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
# claim-id shaped tokens (segments may carry _ and -, e.g. SEAM.S3.FROM-P1.01;
# superset of the spec's [A-Z][A-Z0-9]{1,}(\.[A-Z0-9]+){1,4} -- exact-match
# filtered against the ledger either way)
CLAIM_TOKEN_RE = re.compile(r"\b([A-Z][A-Z0-9_-]*(?:\.[A-Z0-9_-]+){1,5})\b")

# experiments/next.txt entry formats (newest first):
#   # 2026-09-17 — SLUG-TITEL: ... Verdict X ... Contract .../theory-contracts/<slug>/
#   # 2026-08-27 (DCXCVIII) — ...            (optional roman-numeral group)
#   [2026-09-15] slug (tags): ... (PASS, 26 Checks, ...)
NEXTXT_LINE_RE = re.compile(
    r"^(?:#\s*(\d{4}-\d{2}-\d{2})(?:\s*\([^)]*\))?\s*[—–-]?\s+"
    r"|\[(\d{4}-\d{2}-\d{2})\]\s*)(.*\S)\s*$"
)
NEXTXT_CONTRACT_RE = re.compile(r"theory-contracts/([a-z0-9][a-z0-9-]*)/?")
NEXTXT_VERDICT_RE = re.compile(r"\bVerdict\s+([A-Z][A-Z0-9_]{2,})\b")
NEXTXT_KNOWN_RE = re.compile(
    r"\b(PASS|PARTIAL|PARTIELL|FAIL|REFUTED|NO_CANDIDATE|CANDIDATE_PASSES_NULLS|"
    r"CANDIDATE|CONSISTENT[A-Z0-9_]*|KERNEL_VIOLATION|TRIVIAL_FROM_EXISTING_E|"
    r"NO_GO[A-Z0-9_]*|NEIN)\b"
)
NEXTXT_CHECKS_RE = re.compile(r"(\d+(?:\s*/\s*\d+)?)\s*Checks?\b")
KNOWN_VERDICT_PARTS = (
    "PASS", "PARTIAL", "PARTIELL", "FAIL", "REFUTED", "NO_GO", "CANDIDATE",
    "CONSISTENT", "KERNEL_VIOLATION", "TRIVIAL", "NEIN",
)

# never descended into when counting experiment files
EXCLUDE_DIR_NAMES = frozenset({
    "__pycache__", ".git", "venv", ".venv", "node_modules",
    ".pytest_cache", ".ruff_cache", ".lake", "data",
})

# Verdict regexes for legacy RESULTS.md / README.md parsing, most specific
# first.  Raw values seen in the wild: PASS, PARTIAL, PARTIELL, FAIL, REFUTED,
# KERNEL_VIOLATION, NO_CANDIDATE, CANDIDATE_PASSES_NULLS, ORIENTATION_SECTOR,
# TORSOR_REDUCTION, NEIN, exakt erhalten, long EVALUATED_*/CERTIFIED_* enums.
VERDICT_PATTERNS = [
    re.compile(r"\*\*Verdict:\s*`([^`]+)`\.\*\*"),
    re.compile(r"Verdict:\s*\*\*`([^`]+)`\*\*"),
    re.compile(r"Contract-Verdict nach pr.registriertem Enum:\s*\n+\s*`?([A-Z][A-Z0-9_]*)`?"),
    re.compile(r"Inhaltliches(?:\s+pr.registriertes)?\s+Verdict:\s*\*\*`([^`]+)`\*\*"),
    re.compile(r"\*\*Verdict:\*\*\s*`([^`]+)`"),
    re.compile(r"\*\*Verdict:\s*`([^`]+)`\*\*"),
    re.compile(r"(?<![A-Za-z])Verdict:\s*`([^`]+)`"),
    re.compile(r"Success verdict:\s*`([^`]+)`"),
    re.compile(r"(?<![A-Za-z])[Vv]erdict:\s*\*\*`([^`]+)`\*\*"),
    re.compile(r"\*\*Verdict:\s*([A-ZÄÖÜ][A-Za-zÄÖÜäöü0-9_ +.-]{1,60}?)\s*\.\*\*"),
    re.compile(r"\*\*[A-Za-z-]*[Vv]erdict:\s*([A-ZÄÖÜ]{2,}(?:\s+[A-ZÄÖÜ]+){0,3})\s*\.?\*\*"),
    re.compile(r"(?<![A-Za-z])Verdicts?:\s*\*\*[^\n`]*`([A-Z0-9_]+)`"),
    re.compile(r"Record verdict:\s*`?([A-Z][A-Z0-9_]*)`?"),
    re.compile(r"(?<![A-Za-z])[Vv]erdict\s*[:=]\s*\*\*([A-Z][A-Z0-9_ -]{1,50})\*\*"),
]

# docs_map doc slugs that ledger location tokens never spell out
DOC_ALIASES = {
    "AppendixH": "tfpt_horizon_readouts",
}

STOP_TOKENS = frozenset(
    "the a an of and to in for with on by is it as at or be from that this "
    "are was were been being into over under via vs not no nor its their "
    "und der die das ein eine mit von auf ist es im am den dem".split()
)


def rel(path: Path) -> str:
    """Repo-relative display path; never raises (robustness constraint)."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def warn(msg: str) -> None:
    print(f"[THEORY-GRAPH] WARNING: {msg}", file=sys.stderr)


def clip(text, width):
    if text is None:
        return ""
    text = " ".join(str(text).split())
    return text if len(text) <= width else text[: width - 3] + "..."


def slugify(text, width=60):
    slug = re.sub(r"[^a-z0-9]+", "-", str(text or "").lower()).strip("-")
    return (slug[:width].strip("-") or "row")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def dir_listing_sha(path: Path) -> str:
    """Hash a directory's immediate listing (names+sizes) so added/removed
    files (e.g. a new contract_index.json in a legacy folder) trip --check."""
    entries = []
    for e in sorted(path.iterdir(), key=lambda p: p.name):
        if e.name == "__pycache__":
            continue
        entries.append([e.name, e.stat().st_size if e.is_file() else -1])
    return hashlib.sha256(json.dumps(entries, sort_keys=True).encode()).hexdigest()


class Sources:
    """Tracks every parsed file (path, sha256, mtime) for --check freshness."""

    def __init__(self):
        self.records = []

    def add_file(self, path: Path) -> None:
        try:
            st = path.stat()
            self.records.append({
                "path": str(rel(path)),
                "sha256": sha256_file(path),
                "mtime": st.st_mtime,
            })
        except OSError as exc:
            warn(f"cannot hash source {path}: {exc}")

    def add_dir_listing(self, path: Path) -> None:
        try:
            self.records.append({
                "path": str(rel(path)) + "/",
                "sha256": dir_listing_sha(path),
                "mtime": path.stat().st_mtime,
            })
        except OSError as exc:
            warn(f"cannot hash dir listing {path}: {exc}")


def read_csv(path: Path) -> list:
    if not path.is_file():
        warn(f"missing input {rel(path)} -- skipped")
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_json(path: Path):
    if not path.is_file():
        warn(f"missing input {rel(path)} -- skipped")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        warn(f"unparseable {rel(path)}: {exc} -- skipped")
        return None


# --------------------------------------------------------------------------
# graph v2 sidecars (schema: verification/graph_v2/schema.json)
# --------------------------------------------------------------------------

SIDECAR_NAMES = ("claim_contracts", "transitions", "constraints",
                 "failure_scopes")


def load_sidecars(sources: Sources) -> dict:
    """Load the four v2 sidecar files; all four enter meta.sources."""
    out = {}
    for name in SIDECAR_NAMES:
        path = GRAPH_V2_DIR / f"{name}.json"
        data = read_json(path)
        if data is None:
            out[name] = []
            continue
        sources.add_file(path)
        recs = data.get("records") if isinstance(data, dict) else None
        if not isinstance(recs, list):
            warn(f"{rel(path)}: 'records' missing/not a list -- ignored")
            recs = []
        out[name] = recs
    return out


def provenance_ok(rec: dict) -> bool:
    prov = rec.get("provenance")
    return isinstance(prov, dict) and isinstance(prov.get("reviewed"), bool)


def resolve_ref(token, node_ids):
    """Resolve a sidecar reference to a node id: accepts bare claim ids,
    contract slugs, transition/constraint/failure ids, rh paths, script
    names (with/without .py) and already-prefixed node ids."""
    if not token:
        return None
    t = str(token).strip()
    if t in node_ids:
        return t
    for prefix in ("claim:", "contract:", "transition:", "constraint:",
                   "failure:", "rh:", "experiment:"):
        if prefix + t in node_ids:
            return prefix + t
    base = t.removesuffix(".py")
    if f"script:{base}" in node_ids:
        return f"script:{base}"
    return None


def find_claim_cycles(edges) -> list:
    """Tarjan SCC over depends_on+supersedes between claim nodes; returns
    one concrete witness path per non-trivial SCC (plus self-loops)."""
    adj = defaultdict(list)
    for e in edges:
        if (e["type"] in ("depends_on", "supersedes")
                and e["src"].startswith("claim:")
                and e["dst"].startswith("claim:")):
            adj[e["src"]].append(e["dst"])
    index_of = {}
    lowlink = {}
    on_stack = set()
    stack = []
    counter = [0]
    sccs = []

    def strongconnect(v):
        work = [(v, iter(adj.get(v, [])))]
        index_of[v] = lowlink[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on_stack.add(v)
        while work:
            node, it = work[-1]
            advanced = False
            for w in it:
                if w not in index_of:
                    index_of[w] = lowlink[w] = counter[0]
                    counter[0] += 1
                    stack.append(w)
                    on_stack.add(w)
                    work.append((w, iter(adj.get(w, []))))
                    advanced = True
                    break
                elif w in on_stack:
                    lowlink[node] = min(lowlink[node], index_of[w])
            if advanced:
                continue
            work.pop()
            if work:
                parent = work[-1][0]
                lowlink[parent] = min(lowlink[parent], lowlink[node])
            if lowlink[node] == index_of[node]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack.discard(w)
                    scc.append(w)
                    if w == node:
                        break
                if len(scc) > 1:
                    sccs.append(scc)

    for v in list(adj):
        if v not in index_of:
            strongconnect(v)
    for src, dsts in adj.items():
        if src in dsts:
            sccs.append([src])

    def witness_cycle(scc):
        members = set(scc)
        start = scc[0]
        path = [start]
        visited = set()

        def dfs(u):
            for w in adj.get(u, []):
                if w not in members:
                    continue
                if w == start and len(path) > 1:
                    return path + [start]
                if w not in visited:
                    visited.add(w)
                    path.append(w)
                    r = dfs(w)
                    if r:
                        return r
                    path.pop()
            return None

        found = dfs(start)
        return found if found else scc + [scc[0]]

    # edge-type map for classification (a step can carry both types)
    type_by_step = defaultdict(set)
    for e in edges:
        if (e["type"] in ("depends_on", "supersedes")
                and e["src"].startswith("claim:")
                and e["dst"].startswith("claim:")):
            type_by_step[(e["src"], e["dst"])].add(e["type"])

    out = []
    for s in sorted(sccs, key=lambda s: (-len(s), sorted(s)[0])):
        path = witness_cycle(sorted(s))
        sup_steps = []
        pure = True
        for a, b in zip(path, path[1:]):
            types = type_by_step.get((a, b)) or set()
            if "depends_on" not in types:
                pure = False
                if "supersedes" in types:
                    sup_steps.append(f"{a.replace('claim:', '')} -> {b.replace('claim:', '')}")
            elif "supersedes" in types:
                sup_steps.append(f"{a.replace('claim:', '')} -> {b.replace('claim:', '')} (beide)")
        out.append({
            "path": path,
            "classified": "depends_on_pure" if pure else "supersedes_involved",
            "supersedes_steps": sup_steps,
        })
    return out


# --------------------------------------------------------------------------
# verdict classification
# --------------------------------------------------------------------------

def verdict_class(raw) -> str:
    """Contract verdict raw -> pass|partial|fail|refuted|killed|candidate|
    open|other|unknown.  Negation guards first: a survived kill-test or a
    not-refuted formulation is never a kill.  Prose enums: 'conditional*'
    -> partial, 'widerlegt/refuted' -> refuted, 'no-go' -> killed,
    'bestätigt/confirmed/byteidentisch.*PASS' -> pass, 'bleibt offen /
    remains open' -> open.  Unmatched -> other (raw is kept, clipped)."""
    if not raw:
        return "unknown"
    s = re.sub(r"[^a-z0-9]+", "_", str(raw).lower()).strip("_")
    if not s:
        return "unknown"
    u = s.upper()
    if u in {"UNKNOWN", "UNBEKANNT", "KEIN_ERGEBNIS"}:
        return "unknown"
    negated = ("not_confirmed" in s or "not_refuted" in s
               or "unrefuted" in s or "nicht_widerlegt" in s)
    kill_test_passed = "kill_test" in s and ("passed" in s or "survived" in s)
    if not negated and not kill_test_passed:
        if "REFUT" in u or "widerlegt" in s:
            return "refuted"
        if "KERNEL_VIOLATION" in u or "KILLED" in u or "NO_GO" in u or "gekillt" in s:
            return "killed"
    if "CANDIDATE" in u:  # catches NO_CANDIDATE and CANDIDATE_PASSES_NULLS
        return "candidate"
    if ("PARTIAL" in u or "PARTIELL" in u or "MARGINAL" in u
            or "conditional" in s):
        return "partial"
    if "bleibt_offen" in s or "bleiben_offen" in s or "remains_open" in s:
        return "open"
    if "FAIL" in u or u.startswith("BLOCKED") or u in {
        "NEIN", "NO", "NOT_VIABLE", "NOTVIABLE",
    }:
        return "fail"
    if (
        "PASS" in u
        or "HOLDS" in u
        or "CERTIFIED" in u
        or "BESTANDEN" in u
        or "PROVED" in u
        or "best_tigt" in s  # 'bestätigt' after [^a-z0-9] normalisation
        or "confirmed" in s
        or ("byteidentisch" in s and "pass" in s)
        or u in {"CONSISTENT", "CLEAN", "EXAKT_ERHALTEN", "JA", "YES"}
    ):
        return "pass"
    return "other"


def find_verdict_in_text(text: str):
    for pat in VERDICT_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(1).strip().rstrip(".").strip()
    return None


def read_json_trailing_stripped(path: Path):
    """run_normal/run_optimized.json may carry a trailing non-JSON line after
    the final '}' (e.g. '134/134 Bedingungen') -- cut it, then parse."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        warn(f"cannot read {rel(path)}: {exc}")
        return None
    idx = text.rfind("}")
    if idx >= 0:
        text = text[: idx + 1]
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        warn(f"unparseable {rel(path)}: {exc} -- skipped")
        return None


def known_verdict_token(token) -> bool:
    t = str(token or "").upper()
    return any(part in t for part in KNOWN_VERDICT_PARTS)


def parse_next_txt(path: Path, contract_names: set):
    """experiments/next.txt -> slug -> {date, verdict_token, checks}.

    Newest entry wins (file is newest-first).  Only known enum tokens count --
    no hit is honest, never invented.  Returns (slug_map, n_entries, span).
    """
    slug_map = {}
    n_entries = 0
    dates = []
    if not path.is_file():
        warn(f"missing input {rel(path)} -- next.txt backfill off")
        return slug_map, n_entries, [None, None]
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        warn(f"cannot read {rel(path)}: {exc}")
        return slug_map, n_entries, [None, None]
    for line in lines:
        m = NEXTXT_LINE_RE.match(line)
        if not m:
            continue
        n_entries += 1
        date = (m.group(1) or m.group(2) or "").replace("-", "")
        dates.append(date)
        rest = m.group(3) or ""
        # slug: explicit Contract reference first, then leading token forms
        slug = None
        cm = NEXTXT_CONTRACT_RE.search(rest)
        if cm and cm.group(1) in contract_names:
            slug = cm.group(1)
        else:
            head = rest.split(":", 1)[0].strip()
            head_tok = head.split()[0].lower() if head.split() else ""
            head_tok = head_tok.strip("`")
            if head_tok in contract_names:
                slug = head_tok
        if slug is None or slug in slug_map:
            continue
        # verdict token: 'Verdict X' preferred, else first known enum word
        verdict = None
        vm = NEXTXT_VERDICT_RE.search(rest)
        if vm and known_verdict_token(vm.group(1)):
            verdict = vm.group(1)
        if verdict is None:
            km = NEXTXT_KNOWN_RE.search(rest)
            if km:
                verdict = km.group(1)
        checks = None
        chm = NEXTXT_CHECKS_RE.search(rest)
        if chm:
            checks = re.sub(r"\s+", "", chm.group(1))
        slug_map[slug] = {"date": date or None, "verdict_token": verdict,
                          "checks": checks}
    dates = [d for d in dates if d]
    span = [min(dates), max(dates)] if dates else [None, None]
    return slug_map, n_entries, span


def experiment_verdict_class(raw) -> str:
    """results/results.json verdicts -> pass|partial|fail|killed|null|
    consistent|tension|other|unknown (tolerant, deterministic).

    Negation guards first: 'not_confirmed_not_refuted' or a *passed*
    kill-test must never classify as killed."""
    if raw is None:
        return "unknown"
    s = re.sub(r"[^a-z0-9]+", "_", str(raw).strip().lower()).strip("_")
    if not s:
        return "unknown"
    for key in ("pass", "partial", "fail", "killed", "null",
                "consistent", "tension"):
        if s == key or s.startswith(key + "_"):
            return key
    negated = ("not_confirmed" in s or "not_refuted" in s or "unrefuted" in s)
    kill_test_passed = "kill_test" in s and ("passed" in s or "survived" in s)
    if not negated and not kill_test_passed:
        if "refut" in s or "no_go" in s or "killed" in s:
            return "killed"
    if "tension" in s or "spannung" in s:
        return "tension"
    if "consistent" in s or "consistency" in s or "konsistent" in s:
        return "consistent"
    if negated or s.startswith("no_") or re.search(r"(^|_)null(_|$)", s):
        return "null"
    if re.search(r"(^|_)(pass|passed|holds|validated|bestanden)(_|$)", s):
        return "pass"
    if "partial" in s or "partiell" in s:
        return "partial"
    if "fail" in s or "blocked" in s:
        return "fail"
    return "other"


def extract_claim_tokens(texts, claim_ids, cap=20):
    """Claim-id candidates from free text, most frequent first, capped.

    Exact ledger matches win directly; a token without exact match is
    resolved via the ledger suffix '.<token>' -- only when EXACTLY ONE
    claim matches (e.g. KERNEL.01 -> QGEO.KERNEL.01).  Returns
    (resolved, ambiguous): resolved = [(claim_id, resolved_from|None)],
    ambiguous = tokens with >= 2 suffix matches (-> unresolved_claim_tokens).
    """
    counts = Counter()
    for txt in texts:
        if not txt:
            continue
        for tok in CLAIM_TOKEN_RE.findall(txt):
            counts.update([tok])
    resolved = []
    ambiguous = []
    seen = set()
    for tok, _n in counts.most_common():
        if tok in claim_ids:
            pair = (tok, None)
        else:
            suffix_hits = [c for c in claim_ids if c.endswith("." + tok)]
            if len(suffix_hits) == 1:
                pair = (suffix_hits[0], tok)
            else:
                if len(suffix_hits) > 1:
                    ambiguous.append(tok)
                continue
        if pair[0] in seen:
            continue
        seen.add(pair[0])
        resolved.append(pair)
        if len(resolved) >= cap:
            break
    return resolved, ambiguous


# findings: the semantic layer -- sentences carrying a verdict trigger,
# classified refutes | no_go | supports | open, with their section heading.
FINDING_TRIGGER_RE = re.compile(
    r"widerlegt|refuted|no[- ]?go|gekillt|killed|widerspruch|contradiction"
    r"|bestätigt|confirmed|bewiesen|proved|bleibt offen|remains open|offen",
    re.I,
)
FINDING_REFUTES_RE = re.compile(r"widerlegt|refuted|widerspruch|contradiction", re.I)
FINDING_NOGO_RE = re.compile(r"no[- ]?go|gekillt|killed", re.I)
FINDING_SUPPORTS_RE = re.compile(r"bestätigt|confirmed|bewiesen|proved", re.I)
SECTION_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")


def finding_kind(sentence: str) -> str:
    if FINDING_REFUTES_RE.search(sentence):
        return "refutes"
    if FINDING_NOGO_RE.search(sentence):
        return "no_go"
    if FINDING_SUPPORTS_RE.search(sentence):
        return "supports"
    return "open"


def extract_findings(readme_text, results_text, cap=10):
    """Sentences with verdict triggers from README.md + RESULTS.md.
    Paragraphs are joined before sentence splitting (markdown sentences
    span line breaks); the current '## ...' heading is carried along."""
    findings = []
    seen = set()
    for where, text in (("readme", readme_text), ("results", results_text)):
        if not text:
            continue
        section = None
        # paragraphs: blank-line separated blocks; headings tracked inline
        for block in re.split(r"\n\s*\n", text):
            block = block.strip()
            if not block:
                continue
            hm = SECTION_RE.match(block)
            if hm:
                section = clip(re.sub(r"[#*`]", "", hm.group(2)), 120)
                continue
            if block.startswith("#"):
                continue
            # the preregistered enum DEFINITIONS are not findings
            if section and "verdict-enum" in section.lower():
                continue
            para = " ".join(block.splitlines())
            for sent in re.split(r"(?<=[.!?])\s+", para):
                if not FINDING_TRIGGER_RE.search(sent):
                    continue
                clean = re.sub(r"\*\*|__|`", "", sent).strip()
                clean = " ".join(clean.split())
                if len(clean) < 25:  # too short carries no information
                    continue
                if re.match(r"^-?\s*[A-Z][A-Z0-9_]{3,}\s*—", clean):
                    continue  # enum definition item, not a result sentence
                key = clean[:120]
                if key in seen:
                    continue
                seen.add(key)
                findings.append({
                    "kind": finding_kind(clean),
                    "text": clip(clean, 200),
                    "section": section,
                    "where": where,
                })
                if len(findings) >= cap:
                    return findings
    return findings


GATE_ID_RE = re.compile(r"^T[1-8]$")
# prose: 'T1–T8[- ]Tore bleiben offen' / 'T3/T4/T7/T8 ... offen'
GATE_RANGE_OPEN_RE = re.compile(
    r"T1\s*[–—-]\s*T8[^.]*?(bleiben? offen|remains? open|stay open)", re.I)
GATE_SINGLE_OPEN_RE = re.compile(r"\bT([1-8])\b")


def extract_gate_mentions(readme_text, results_text):
    """Gate mentions from prose: 'T1–T8 ... bleiben offen' opens all eight,
    single 'T3'/'T4' tokens in an offen/open sentence open that gate."""
    leaves_open = set()
    for text in (readme_text, results_text):
        if not text:
            continue
        for sent in re.split(r"(?<=[.!?])\s+", " ".join(text.splitlines())):
            if GATE_RANGE_OPEN_RE.search(sent):
                leaves_open.update(f"T{i}" for i in range(1, 9))
            elif re.search(r"offen|open", sent, re.I):
                for g in GATE_SINGLE_OPEN_RE.findall(sent):
                    leaves_open.add(f"T{g}")
    return sorted(leaves_open)


def count_files_tree(root: Path, count_ext=None) -> int:
    """Recursive file count, skipping EXCLUDE_DIR_NAMES and hidden dirs."""
    total = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDE_DIR_NAMES and not d.startswith(".")
        ]
        if count_ext:
            filenames = [f for f in filenames if f.endswith(count_ext)]
        total += len(filenames)
    return total


def experiments_shallow_sha() -> str:
    """Shallow listing hash: experiments/ top-level names + theory-contracts
    subdir names.  A new/removed dir must trip --check."""
    top = []
    if EXPERIMENTS_DIR.is_dir():
        top = sorted(
            e.name for e in EXPERIMENTS_DIR.iterdir() if e.name != "__pycache__"
        )
    tc = []
    if CONTRACTS_DIR.is_dir():
        tc = sorted(
            p.name for p in CONTRACTS_DIR.iterdir()
            if p.is_dir() and not p.name.startswith(".")
            and p.name != "__pycache__"
        )
    blob = json.dumps({"top": top, "theory-contracts": tc}, sort_keys=True)
    return hashlib.sha256(blob.encode()).hexdigest()


# --------------------------------------------------------------------------
# Lean layer (rh/lean + experiments/lean4-carrier-rigidity; .lake excluded)
# --------------------------------------------------------------------------

LEAN_ROOTS = (ROOT / "rh" / "lean", ROOT / "experiments" / "lean4-carrier-rigidity")
LEAN_DECL_RE = re.compile(r"^(theorem|lemma|def|instance|axiom|structure|class)\s+([^\s:(]+)")
LEAN_IMPORT_RE = re.compile(r"^import\s+([A-Za-z0-9_.]+)", re.M)
LEAN_NS_RE = re.compile(r"^namespace\s+(\S+)", re.M)
SORRY_RE = re.compile(r"\bsorry\b")
LEAN_HEADER_RE = re.compile(r"\A\s*/-(?!-)(.*?)-/", re.S)
CLAIM_BOUNDARY_RE = re.compile(r"CLAIM BOUNDARY|NO .*CLAIM")


def lean_module_name(path: Path) -> str:
    for base in LEAN_ROOTS:
        try:
            rel = path.relative_to(base)
        except ValueError:
            continue
        return ".".join(rel.with_suffix("").parts)
    return path.stem


def lean_toolchain(path: Path):
    d = path.parent
    while True:
        tc = d / "lean-toolchain"
        if tc.is_file():
            try:
                return tc.read_text(encoding="utf-8", errors="replace").strip()
            except OSError:
                return None
        if d == ROOT or d.parent == d:
            return None
        d = d.parent


def parse_lean_file(path: Path, module_map, claim_ids, cap=40):
    """Static surface parse of one .lean file (no Lean toolchain needed)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        warn(f"cannot read {rel(path)}: {exc}")
        return None
    header = None
    claim_boundary = False
    hm = LEAN_HEADER_RE.match(text)
    if hm:
        raw_header = " ".join(hm.group(1).split())
        claim_boundary = bool(CLAIM_BOUNDARY_RE.search(raw_header))
        header = clip(raw_header, 400)
    imports = LEAN_IMPORT_RE.findall(text)
    imports_repo = [m for m in imports if m in module_map]
    nsm = LEAN_NS_RE.search(text)
    decls = []
    counts = Counter()
    pending_doc = None
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith("/--"):
            doc_lines = [stripped[3:]]
            while "-/" not in lines[i] and i + 1 < len(lines):
                i += 1
                doc_lines.append(lines[i])
            for dl in doc_lines:
                dl = dl.replace("-/", "").strip(" -")
                if dl:
                    pending_doc = clip(dl, 200)
                    break
            i += 1
            continue
        m = LEAN_DECL_RE.match(line)
        if m:
            kind, name = m.group(1), m.group(2)
            counts.update([kind])
            if len(decls) < cap:
                decls.append({
                    "kind": kind,
                    "name": name,
                    "signature": clip(line.strip(), 200),
                    "doc": pending_doc,
                })
            pending_doc = None
        i += 1
    n_theorems = counts.get("theorem", 0) + counts.get("lemma", 0)
    n_defs = sum(counts.get(k, 0)
                 for k in ("def", "instance", "structure", "class"))
    attrs = {
        "module": lean_module_name(path),
        "namespace": nsm.group(1) if nsm else None,
        "imports_repo": imports_repo,
        "n_imports_mathlib": sum(1 for m in imports if m.startswith("Mathlib.")),
        "declarations": decls,
        "n_theorems": n_theorems,
        "n_defs": n_defs,
        "n_axioms": counts.get("axiom", 0),
        "n_sorry": len(SORRY_RE.findall(text)),
        "header_comment": header,
        "claim_boundary": claim_boundary,
        "toolchain": lean_toolchain(path),
    }
    # proves: claim ids in header comment + docstrings (suffix-resolved)
    texts = [header] + [d["doc"] for d in decls if d.get("doc")]
    resolved, _amb = extract_claim_tokens(texts, claim_ids, cap=10)
    return attrs, resolved


def inventory_lean(sources: Sources, claim_ids):
    """One lean:<relpath> node per .lean file (*/.lake/* always excluded)."""
    out = {"nodes": [], "imports_edges": [], "proves": {}, "files": []}
    files = []
    for base in LEAN_ROOTS:
        if not base.is_dir():
            warn(f"missing lean dir {rel(base)} -- skipped")
            continue
        for p in sorted(base.rglob("*.lean")):
            if "/.lake/" in str(p):
                continue
            files.append(p)
    module_map = {lean_module_name(p): p for p in files}
    for p in files:
        parsed = parse_lean_file(p, module_map, claim_ids)
        if parsed is None:
            continue
        attrs, proves = parsed
        relpath = rel(p)
        nid = f"lean:{relpath}"
        out["nodes"].append((nid, relpath, attrs))
        out["files"].append(relpath)
        out["proves"][nid] = proves
        for mod in attrs["imports_repo"]:
            tgt = module_map.get(mod)
            if tgt is not None:
                out["imports_edges"].append((nid, f"lean:{rel(tgt)}"))
    # freshness: shallow listings of the lean dirs (per spec)
    for base in LEAN_ROOTS:
        if base.is_dir():
            sources.add_dir_listing(base)
            for sub in sorted(base.iterdir(), key=lambda p: p.name):
                if sub.is_dir() and sub.name != ".lake" and not sub.name.startswith("."):
                    sources.add_dir_listing(sub)
    return out


# --------------------------------------------------------------------------
# source loaders -> nodes/edges
# --------------------------------------------------------------------------

def load_ledger(sources: Sources):
    path = VERIF / "status_ledger.csv"
    rows = read_csv(path)
    if rows:
        sources.add_file(path)
    return rows


def load_registry(sources: Sources):
    path = VERIF / "script_registry.csv"
    rows = read_csv(path)
    if rows:
        sources.add_file(path)
    return rows


def load_docs_map(sources: Sources):
    path = VERIF / "docs_map.csv"
    rows = read_csv(path)
    if rows:
        sources.add_file(path)
    return rows


def normalize_doc_token(token: str, doc_names: set):
    """Map a ledger location token to a docs_map doc slug, or None."""
    tok = token.strip()
    if not tok:
        return None
    tok = tok.split()[0] if tok.split() else tok  # 'tfpt_4 (status source)' -> tfpt_4
    tok = DOC_ALIASES.get(tok, tok)
    if tok in doc_names:
        return tok
    prefix = [d for d in doc_names if d.startswith(tok + "_")]
    if len(prefix) == 1:
        return prefix[0]
    return None


def contract_json_candidates(folder: Path):
    """Filename-tolerant run-artefact candidates, in priority order:
    *normal*.json, *optimized*.json, replay.json, results/results.json,
    then every other top-level *.json (key-filtered at parse time)."""
    out = []
    seen = set()
    for pat in ("*normal*.json", "*optimized*.json", "replay.json"):
        for p in sorted(folder.glob(pat)):
            if p.name not in seen:
                seen.add(p.name)
                out.append(p)
    res = folder / "results" / "results.json"
    if res.is_file():
        out.append(res)
    for p in sorted(folder.glob("*.json")):
        if p.name not in seen:
            seen.add(p.name)
            out.append(p)
    return out


def harvest_json_attrs(rec: dict, data: dict) -> None:
    """Merge the standard run-artefact attrs (exact_checks, closed_gate_ids,
    missing, promotion, T1_T8_closed, not_derived) -- ALWAYS when present,
    even if the verdict itself came from another source.  Never overwrite."""
    if rec["exact_checks"] is None:
        ec = data.get("exact_checks", data.get("check_count"))
        if ec is not None:
            rec["exact_checks"] = ec
    if rec["promotion"] is None and data.get("promotion") is not None:
        rec["promotion"] = bool(data.get("promotion"))
    for tok in data.get("closed_gate_ids") or []:
        tok = str(tok)
        if GATE_ID_RE.match(tok):
            if tok not in rec["closes"]:
                rec["closes"].append(tok)
        else:
            rec["claims_tested_raw"].append(tok)
    missing = data.get("missing") or []
    if missing and not rec["missing"]:
        rec["missing"] = [clip(x, 80) for x in list(missing)[:10]]
    if rec["t1_t8_closed"] is None and "T1_T8_closed" in data:
        rec["t1_t8_closed"] = data.get("T1_T8_closed")
    nd = data.get("not_derived") or []
    if nd and not rec["not_derived"]:
        rec["not_derived"] = [clip(x, 80) for x in list(nd)[:10]]


def parse_contract(folder: Path, sources: Sources, next_txt_map=None,
                   claim_ids=()):
    """Parse one theory-contract folder.  Fallback chain:
    contract_index.json (new mandatory format) -> validation.json (legacy)
    -> RESULTS.md regex -> run_normal/run_optimized.json -> next.txt entry
    -> README.md regex -> unknown (honest, never invented)."""
    name = folder.name
    rec = {
        "name": name,
        "date": None,
        "question": None,
        "verdict_raw": None,
        "verdict_class": "unknown",
        "checker": None,
        "parse_source": "none",
        "claims_tested": [],          # list of [claim_id, resolved_from|None]
        "claims_tested_raw": [],
        "unresolved_claim_tokens": [],
        "gates": [],
        "kills": [],
        "kills_free": [],
        "exact_checks": None,
        "promotion": None,
        "missing": [],
        "t1_t8_closed": None,
        "not_derived": [],
        "closes": [],                 # gate ids from closed_gate_ids
        "leaves_open": [],            # gate ids from prose
        "findings": [],
        "summary_de": None,
        "relations_llm": [],          # relations from an llm_backfill index
    }
    m = DATE_SUFFIX_RE.search(name)
    if m:
        rec["date"] = m.group(1)

    readme = folder / "README.md"
    readme_text = None
    if readme.is_file():
        sources.add_file(readme)
        try:
            readme_text = readme.read_text(encoding="utf-8", errors="replace")
            hm = HEADING_RE.search(readme_text)
            if hm:
                rec["question"] = clip(re.sub(r"[#*`]", "", hm.group(1)), 200)
        except OSError as exc:
            warn(f"cannot read {readme.relative_to(ROOT)}: {exc}")

    results = folder / "RESULTS.md"
    results_text = None
    if results.is_file():
        sources.add_file(results)
        try:
            results_text = results.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            warn(f"cannot read {results.relative_to(ROOT)}: {exc}")

    checkers = sorted(
        p.name for p in folder.glob("*.py") if p.name != "__init__.py"
    )
    if checkers:
        rec["checker"] = checkers[0]

    # (a) contract_index.json -- the mandatory format (hand-written or
    # LLM-backfilled via enrich_theory_graph_llm.py -> source=llm_backfill)
    cidx = folder / "contract_index.json"
    if cidx.is_file():
        sources.add_file(cidx)
        data = read_json(cidx)
        if isinstance(data, dict):
            raw = data.get("verdict")
            rec["verdict_raw"] = str(raw) if isinstance(raw, (str, int, float)) else None
            llm_backfill = data.get("source") == "llm_backfill"
            if rec["verdict_raw"]:
                rec["parse_source"] = ("contract_index_llm" if llm_backfill
                                       else "contract_index")
            rec["question"] = clip(data.get("question") or rec["question"] or "", 200) or None
            rec["date"] = str(data.get("date") or rec["date"] or "") or None
            rec["checker"] = data.get("checker") or rec["checker"]
            rec["summary_de"] = clip(data.get("summary_de"), 400) or None
            rec["claims_tested_raw"].extend(
                str(t) for t in (data.get("claims_tested") or []))
            rec["gates"] = list(data.get("gates") or [])
            for k in data.get("kills") or []:
                rec["kills"].append(str(k))
            for rel in data.get("relations") or []:
                if isinstance(rel, dict) and rel.get("target"):
                    rec["relations_llm"].append(
                        {"type": rel.get("type"), "target": str(rel.get("target"))})
            harvest_json_attrs(rec, data)
    # (b) validation.json -- legacy, schema-heterogeneous; attrs are merged
    # ALWAYS, the verdict only when still missing
    val = folder / "validation.json"
    if val.is_file():
        sources.add_file(val)
        data = read_json(val)
        if isinstance(data, dict):
            harvest_json_attrs(rec, data)
            for key in ("claims_tested",):
                for tok in data.get(key) or []:
                    rec["claims_tested_raw"].append(str(tok))
            if rec["verdict_raw"] is None:
                # verdict/status are enums when scalar; some schemas nest a
                # structured dict under 'verdict' -- then 'status' carries it
                raw = data.get("verdict")
                if not isinstance(raw, (str, int, float)):
                    raw = data.get("status")
                if isinstance(raw, (str, int, float)) and str(raw).strip():
                    rec["verdict_raw"] = str(raw)
                    rec["parse_source"] = "validation"
    # (c) RESULTS.md verdict regex
    if rec["verdict_raw"] is None and results_text:
        raw = find_verdict_in_text(results_text)
        if raw:
            rec["verdict_raw"] = raw
            rec["parse_source"] = "results_md"
    # (d) run-artefact JSONs, filename-tolerant: *normal*.json,
    # *optimized*.json, replay.json, results/results.json, then any other
    # top-level *.json carrying status/verdict.  Attrs merged ALWAYS;
    # verdict key chain: verdict | decision | status.
    for cand in contract_json_candidates(folder):
        sources.add_file(cand)
        data = read_json_trailing_stripped(cand)
        if not isinstance(data, dict):
            continue
        is_named = cand.name != "results.json" or cand.parent.name == "results"
        if not is_named and not any(k in data for k in ("status", "verdict")):
            continue  # 'any other *.json' must carry status or verdict
        harvest_json_attrs(rec, data)
        if rec["verdict_raw"] is None:
            raw = data.get("verdict")
            if not isinstance(raw, (str, int, float)):
                raw = data.get("decision")
            if not isinstance(raw, (str, int, float)):
                raw = data.get("status")
            if isinstance(raw, (str, int, float)) and str(raw).strip():
                rec["verdict_raw"] = str(raw)
                rec["parse_source"] = "run_json"
    # (e) experiments/next.txt entry (research log, newest-first map)
    if rec["verdict_raw"] is None and next_txt_map:
        entry = next_txt_map.get(name)
        if entry:
            if entry.get("verdict_token"):
                rec["verdict_raw"] = entry["verdict_token"]
                rec["parse_source"] = "next_txt"
            if not rec["date"] and entry.get("date"):
                rec["date"] = entry["date"]
            if rec["exact_checks"] is None and entry.get("checks"):
                rec["exact_checks"] = entry["checks"]
    # (f) README.md verdict regex as last resort (older folders carry the
    # preregistered verdict only in the README)
    if rec["verdict_raw"] is None and readme_text:
        raw = find_verdict_in_text(readme_text)
        if raw:
            rec["verdict_raw"] = raw
            rec["parse_source"] = "readme_md"
    # date fill from next.txt even when the verdict came from elsewhere
    if not rec["date"] and next_txt_map:
        entry = next_txt_map.get(name)
        if entry and entry.get("date"):
            rec["date"] = entry["date"]

    rec["verdict_class"] = verdict_class(rec["verdict_raw"])
    if rec["question"] is None:
        rec["question"] = name
    # claims_tested: parsed ids first (authoritative), then extracted tokens
    # with suffix resolution (KERNEL.01 -> QGEO.KERNEL.01 iff the suffix
    # match is unique); ambiguous tokens -> unresolved_claim_tokens; cap 20
    extracted, ambiguous = extract_claim_tokens(
        [readme_text, results_text], claim_ids, cap=20)
    rec["unresolved_claim_tokens"] = ambiguous[:20]
    seen = set()
    merged = []
    for tok in rec.pop("claims_tested_raw"):
        cid = tok if tok in claim_ids else None
        if cid is None:
            hits = [c for c in claim_ids if c.endswith("." + tok)]
            if len(hits) == 1:
                cid = hits[0]
        if cid and cid not in seen:
            seen.add(cid)
            merged.append([cid, None if cid == tok else tok])
    for cid, from_tok in extracted:
        if cid in seen:
            continue
        seen.add(cid)
        merged.append([cid, from_tok])
        if len(merged) >= 20:
            break
    rec["claims_tested"] = merged
    # gates from prose ('T1–T8 bleiben offen' / single 'T3' near 'offen')
    rec["leaves_open"] = extract_gate_mentions(readme_text, results_text)
    # findings: the semantic layer (verdict-carrying sentences, capped)
    rec["findings"] = extract_findings(readme_text, results_text, cap=10)
    return rec


# --------------------------------------------------------------------------
# experiments/ inventory (no dead spots: every top-level dir gets a node)
# --------------------------------------------------------------------------

def classify_experiment(name: str, has_prereg: bool, has_results: bool) -> str:
    if name == "tfpt-discovery":
        return "discovery_sandbox"
    if name == "pyrate":
        return "tooling"
    if name == "older_tests":
        return "legacy"
    if name.startswith("lean4"):
        return "lean"
    if "audit" in name:
        return "audit"
    if has_prereg or has_results:
        return "empirical_search"
    return "discovery_sandbox"


GATE_CORE_RE = re.compile(r"verdict|status|pass|gate|result|validation", re.I)


def gate_core_fields(data: dict, cap=8):
    """Core verdict/status/pass fields of a gate artefact, clipped.
    Booleans/numbers stay native (False must survive)."""
    fields = {}
    for k, v in data.items():
        if not GATE_CORE_RE.search(str(k)):
            continue
        if isinstance(v, bool):
            fields[str(k)] = v
        elif isinstance(v, (int, float)):
            fields[str(k)] = v
        elif isinstance(v, str):
            fields[str(k)] = clip(v, 120)
        else:
            fields[str(k)] = clip(json.dumps(v, ensure_ascii=False), 200)
        if len(fields) >= cap:
            break
    if not fields:  # no named core keys -> first scalars as fallback
        for k, v in data.items():
            if isinstance(v, bool):
                fields[str(k)] = v
            elif isinstance(v, (int, float, str)):
                fields[str(k)] = clip(v, 120)
            if len(fields) >= 6:
                break
    return fields


def gates_verdict_class(gates: dict):
    """Derive an experiment verdict from gate artefacts when the experiment
    itself carries none (e.g. pi-prime-event-log: fft_gate_passed=false)."""
    saw_false = saw_true = saw_null = False
    for fields in gates.values():
        for k, v in fields.items():
            kl = str(k).lower()
            if isinstance(v, bool) and ("pass" in kl or "gate" in kl):
                saw_false = saw_false or (v is False)
                saw_true = saw_true or (v is True)
            elif isinstance(v, str):
                sl = v.lower()
                if sl == "false" or "fail" in sl or "refut" in sl:
                    saw_false = True
                if "null" in sl:
                    saw_null = True
                if sl == "true" or "pass" in sl or "confirmed" in sl:
                    saw_true = True
    if saw_false:
        return "fail"
    if saw_null:
        return "null"
    if saw_true:
        return "pass"
    return None


def inventory_experiments(sources: Sources, claim_ids):
    """One experiment:<dirname> node per top-level directory under
    experiments/ (theory-contracts stays contract:*).  YAML is never parsed
    (presence + hash only); data/ dirs are counted, never indexed."""
    out = {"nodes": [], "tests_edges": [], "dirs": [], "probes_total": 0}
    if not EXPERIMENTS_DIR.is_dir():
        warn("missing experiments/ -- no experiment nodes")
        return out
    for entry in sorted(EXPERIMENTS_DIR.iterdir(), key=lambda p: p.name):
        if (not entry.is_dir() or entry.name.startswith(".")
                or entry.name in ("__pycache__", "theory-contracts")):
            continue
        name = entry.name
        readme_text = None
        title = None
        readme = entry / "README.md"
        if readme.is_file():
            sources.add_file(readme)
            try:
                readme_text = readme.read_text(encoding="utf-8", errors="replace")
                hm = HEADING_RE.search(readme_text)
                if hm:
                    title = clip(re.sub(r"[#*`]", "", hm.group(1)), 200)
            except OSError as exc:
                warn(f"cannot read {readme.relative_to(ROOT)}: {exc}")
        # preregistration: presence + hash of first yaml, never parsed
        hyp_dir = entry / "hypotheses"
        hyp_files = sorted(hyp_dir.glob("*.yaml")) if hyp_dir.is_dir() else []
        prereg_top = sorted(entry.glob("prereg*.yaml"))
        has_prereg = bool(hyp_files or prereg_top)
        prereg_sha = None
        first_prereg = (hyp_files + prereg_top or [None])[0]
        if first_prereg is not None:
            sources.add_file(first_prereg)
            try:
                prereg_sha = sha256_file(first_prereg)
            except OSError:
                prereg_sha = None
        # verdict from results/results.json (tolerant key chain)
        verdict_raw = None
        results_text = None
        res = entry / "results" / "results.json"
        if res.is_file():
            sources.add_file(res)
            try:
                results_text = res.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                warn(f"cannot read {res.relative_to(ROOT)}: {exc}")
            data = None
            if results_text:
                try:
                    data = json.loads(results_text)
                except json.JSONDecodeError as exc:
                    warn(f"unparseable {res.relative_to(ROOT)}: {exc} -- skipped")
            if isinstance(data, dict):
                for key in ("verdict", "status"):
                    val = data.get(key)
                    if isinstance(val, (str, int, float)) and str(val).strip():
                        verdict_raw = str(val)
                        break
                if verdict_raw is None:
                    overall = data.get("overall")
                    if isinstance(overall, dict):
                        val = overall.get("verdict")
                        if isinstance(val, (str, int, float)):
                            verdict_raw = str(val)
                    elif isinstance(overall, (str, int, float)):
                        verdict_raw = str(overall)
        n_files = count_files_tree(entry)
        data_dir = entry / "data"
        has_data = data_dir.is_dir()
        n_data = 0
        if has_data:
            for dirpath, dirnames, filenames in os.walk(data_dir):
                dirnames[:] = [
                    d for d in dirnames
                    if d not in EXCLUDE_DIR_NAMES and not d.startswith(".")
                ]
                n_data += len(filenames)
        # gate artefacts: */summary.json (one level deep), top-level
        # *_results.json and audit.json -> attrs.gates
        gates = {}
        gate_files = (sorted(entry.glob("*/summary.json"))
                      + sorted(entry.glob("*_results.json"))
                      + sorted(entry.glob("audit.json")))
        for gf in gate_files:
            sources.add_file(gf)
            data = read_json_trailing_stripped(gf)
            if not isinstance(data, dict):
                continue
            gname = gf.parent.name if gf.name == "summary.json" else gf.stem
            fields = gate_core_fields(data)
            if fields:
                gates[gname] = fields
        pys = sorted(p.name for p in entry.glob("*.py"))
        checker_hint = None
        for p in pys:
            if "check" in p or "run" in p:
                checker_hint = p
                break
        if checker_hint is None and pys:
            checker_hint = pys[0]
        kind = classify_experiment(name, has_prereg, (entry / "results").is_dir())
        if name == "tfpt-discovery":
            out["probes_total"] = count_files_tree(entry, count_ext=".py")
        vclass = experiment_verdict_class(verdict_raw)
        if vclass == "unknown" and gates:
            gv = gates_verdict_class(gates)
            if gv:
                vclass = gv
        attrs = {
            "kind": kind,
            "title": title,
            "n_files": n_files,
            "has_data_dir": has_data,
            "n_data_files": n_data,
            "has_prereg": has_prereg,
            "prereg_sha256": prereg_sha,
            "verdict_raw": clip(verdict_raw, 120),
            "verdict_class": vclass,
            "gates": gates,
            "checker_hint": checker_hint,
            "firewall": "experiments",
        }
        out["nodes"].append((f"experiment:{name}", name, attrs))
        out["dirs"].append(name)
        resolved, _ambiguous = extract_claim_tokens(
            [readme_text, results_text], claim_ids, cap=20)
        for cid, from_tok in resolved:
            edge_attrs = {"resolved_from": from_tok} if from_tok else {}
            out["tests_edges"].append(
                (f"experiment:{name}", f"claim:{cid}", "tests", edge_attrs))
    return out


# --------------------------------------------------------------------------
# graph assembly
# --------------------------------------------------------------------------

def build() -> dict:
    sources = Sources()
    nodes = []
    edges = []
    node_ids = set()
    nodes_by_id = {}

    def add_node(nid, ntype, label, attrs):
        if nid in node_ids:
            warn(f"duplicate node id {nid} -- first kept")
            return
        node_ids.add(nid)
        node = {"id": nid, "type": ntype, "label": label, "attrs": attrs}
        nodes.append(node)
        nodes_by_id[nid] = node

    def add_edge(src, dst, etype, attrs=None):
        edges.append({"src": src, "dst": dst, "type": etype, "attrs": attrs or {}})

    # ---- scripts ------------------------------------------------------
    registry = load_registry(sources)
    reg_scripts = set()
    for row in registry:
        base = (row.get("script") or "").strip()
        if not base:
            continue
        reg_scripts.add(base)
        # proof binding (schema Punkt 6): hash the script file so
        # `theorycat recheck` can flag changed sources -- NOT meta.sources
        # (a script edit must not stale the graph, only mark the claim)
        spath = VERIF / f"{base}.py"
        script_sha = None
        if spath.is_file():
            try:
                script_sha = sha256_file(spath)
            except OSError as exc:
                warn(f"cannot hash script {rel(spath)}: {exc}")
        add_node(f"script:{base}", "script", base, {
            "cluster": (row.get("cluster") or "").strip(),
            "what_web": clip(row.get("what_web"), 300),
            "script_sha256": script_sha,
        })

    # ---- doc sections -------------------------------------------------
    docs_rows = load_docs_map(sources)
    doc_names = set()
    for row in docs_rows:
        doc = (row.get("doc") or "").strip()
        if not doc:
            continue
        doc_names.add(doc)
        nid = f"section:{doc}:{(row.get('line_start') or '').strip()}"
        add_node(nid, "section", f"{doc}:{row.get('line_start')}", {
            "doc": doc,
            "kind": (row.get("kind") or "").strip(),
            "title": clip(row.get("title"), 200),
            "line_start": (row.get("line_start") or "").strip(),
            "line_end": (row.get("line_end") or "").strip(),
            "last_changed": (row.get("last_changed") or "").strip(),
        })
        for tok in (row.get("scripts") or "").split(";"):
            base = tok.strip().removesuffix(".py")
            if base and base in reg_scripts:
                add_edge(nid, f"script:{base}", "cites")
    sections_by_doc = defaultdict(list)
    for n in nodes:
        if n["type"] == "section":
            sections_by_doc[n["attrs"]["doc"]].append(n["id"])

    # ---- claims (status ledger) ---------------------------------------
    ledger = load_ledger(sources)
    claim_ids = {(r.get("claim_id") or "").strip() for r in ledger}
    claim_ids.discard("")
    for row in ledger:
        cid = (row.get("claim_id") or "").strip()
        if not cid:
            continue
        status_raw = row.get("status") or ""
        markers = MARKER_RE.findall(status_raw)
        attrs = {
            "status_raw": clip(status_raw, 500),
            "marker": markers[0] if markers else None,
            "markers": markers,
            "active": (row.get("active") or "").strip().lower() == "true",
            "canonical_status": clip(row.get("canonical_status"), 300),
        }
        add_node(f"claim:{cid}", "claim", cid, attrs)

    for row in ledger:
        cid = (row.get("claim_id") or "").strip()
        if not cid:
            continue
        src = f"claim:{cid}"
        # verified_by: script column, only registry scripts get an edge
        unresolved = []
        for tok in (row.get("script") or "").split(";"):
            base = tok.strip().removesuffix(".py")
            if not base or base == "-":
                continue
            if base in reg_scripts:
                add_edge(src, f"script:{base}", "verified_by")
            else:
                unresolved.append(tok.strip())
        if unresolved:
            nodes_by_id[src]["attrs"]["unresolved"] = unresolved
        # stated_in: location slug -> all sections of that doc
        unresolved_locs = []
        for tok in (row.get("location") or "").split(";"):
            tok = tok.strip()
            if not tok:
                continue
            doc = normalize_doc_token(tok, doc_names)
            if doc is None:
                unresolved_locs.append(tok)
                continue
            for sec_id in sections_by_doc.get(doc, []):
                add_edge(src, sec_id, "stated_in")
        if unresolved_locs:
            nodes_by_id[src]["attrs"]["unresolved_locs"] = unresolved_locs
        # depends_on: only tokens that exactly match an existing claim id
        unresolved_deps = []
        for tok in (row.get("dependencies") or "").split(";"):
            tok = tok.strip()
            if not tok or tok == "-":
                continue
            if tok in claim_ids:
                add_edge(src, f"claim:{tok}", "depends_on")
            else:
                unresolved_deps.append(tok)
        if unresolved_deps:
            nodes_by_id[src]["attrs"]["unresolved_deps"] = unresolved_deps
        # supersedes: '-' placeholder or claim id (';'-separated)
        for tok in (row.get("supersedes") or "").split(";"):
            tok = tok.strip()
            if not tok or tok == "-":
                continue
            if tok in claim_ids:
                add_edge(src, f"claim:{tok}", "supersedes")

    # ---- frozen predictions -------------------------------------------
    pf_path = VERIF / "predictions_frozen.json"
    pf = read_json(pf_path)
    if pf:
        sources.add_file(pf_path)
    predictions = (pf or {}).get("predictions") or []
    pred_obs_tokens = {}
    for p in predictions:
        pid = (p.get("id") or "").strip()
        if not pid:
            continue
        add_node(f"prediction:{pid}", "prediction", pid, {
            "observable": clip(p.get("observable"), 200),
            "layer": p.get("layer"),
            "frozen_value": clip(p.get("frozen_value"), 120),
            "kill_criterion": clip(p.get("kill_criterion"), 200),
            "formula": clip(p.get("formula"), 200),
            "experiment": clip(p.get("experiment"), 120),
        })
        toks = {
            t for t in re.findall(r"[a-z0-9]+", (p.get("observable") or "").lower())
            if len(t) >= 3 and t not in STOP_TOKENS
        }
        pred_obs_tokens[pid] = toks
    # document frequency over prediction observables: generic tokens like
    # 'mass'/'ratio'/'angle' must not alone carry a measures edge
    pred_token_df = Counter()
    for ptoks in pred_obs_tokens.values():
        for t in ptoks:
            pred_token_df.update([t])

    def tokens_match(rtoks, ptoks) -> set:
        shared = rtoks & ptoks
        if len(shared) < 2:
            return set()
        distinctive = {
            t for t in shared if pred_token_df.get(t, 99) <= 2 and len(t) >= 4
        }
        return shared if distinctive else set()

    # ---- evidence scorecard (firewall: experiments) --------------------
    sc_path = ROOT / "experiments" / "evidence_scorecard.json"
    sc = read_json(sc_path)
    if sc:
        sources.add_file(sc_path)
    sc_rows = (sc or {}).get("rows") or []
    for row in sc_rows:
        domain = (row.get("domain") or "?").strip()
        observable = (row.get("observable") or "").strip()
        nid = f"scorecard:{domain}:{slugify(observable)}"
        add_node(nid, "scorecard", f"{domain}: {clip(observable, 60)}", {
            "domain": domain,
            "observable": clip(observable, 200),
            "status": row.get("status"),
            "stage": row.get("stage"),
            "evidence_class": row.get("evidence_class"),
            "pull_sigma": row.get("pull_sigma"),
            "kill_condition": clip(row.get("kill_condition"), 200),
            "watch_flag": bool(row.get("watch_flag")),
            "hint_flag": bool(row.get("hint_flag")),
            "source": clip(row.get("source"), 200),
            "firewall": "experiments",
        })
        # tests: tolerant exact claim-id token scan over the whole row
        try:
            blob = json.dumps(row)
        except (TypeError, ValueError):
            blob = str(row)
        for tok in set(CLAIM_TOKEN_RE.findall(blob)):
            if tok in claim_ids:
                add_edge(nid, f"claim:{tok}", "tests")
        # measures: prediction id mentioned, or observable token overlap >= 2
        for pid, ptoks in pred_obs_tokens.items():
            if pid in blob:
                add_edge(nid, f"prediction:{pid}", "measures",
                         {"match": "id"})
                continue
            rtoks = {
                t for t in re.findall(r"[a-z0-9]+", observable.lower())
                if len(t) >= 3 and t not in STOP_TOKENS
            }
            shared = tokens_match(rtoks, ptoks)
            if ptoks and shared:
                add_edge(nid, f"prediction:{pid}", "measures",
                         {"match": "observable_tokens",
                          "shared": sorted(shared)})

    # ---- theory contracts (firewall: experiments) ----------------------
    contracts_total = 0
    contracts_with_verdict = 0
    parse_source_dist = Counter()
    contract_names = set()
    if CONTRACTS_DIR.is_dir():
        contract_names = {
            p.name for p in CONTRACTS_DIR.iterdir()
            if p.is_dir() and not p.name.startswith(".")
            and p.name != "__pycache__"
        }
    # research-log backfill map (slug -> date/verdict/checks), newest first
    next_txt_map, next_txt_entries, next_txt_span = parse_next_txt(
        NEXT_TXT, contract_names)
    if NEXT_TXT.is_file():
        sources.add_file(NEXT_TXT)
    if not CONTRACTS_DIR.is_dir():
        warn(f"missing contracts dir {CONTRACTS_DIR.relative_to(ROOT)} -- skipped")
        contract_recs = []
    else:
        # top-level listing: a NEW or removed contract folder must trip --check
        sources.add_dir_listing(CONTRACTS_DIR)
        contract_recs = []
        for folder in sorted(CONTRACTS_DIR.iterdir(), key=lambda p: p.name):
            if (not folder.is_dir() or folder.name.startswith(".")
                    or folder.name == "__pycache__"):
                continue
            sources.add_dir_listing(folder)
            try:
                rec = parse_contract(folder, sources, next_txt_map, claim_ids)
            except Exception as exc:  # never crash on one bad folder
                warn(f"contract {folder.name}: parse failed ({exc}) -- unknown")
                rec = {
                    "name": folder.name, "date": None, "question": folder.name,
                    "verdict_raw": None, "verdict_class": "unknown",
                    "checker": None, "parse_source": "none",
                    "claims_tested": [], "gates": [], "kills": [], "kills_free": [],
                    "exact_checks": None, "promotion": None, "missing": [],
                }
            contract_recs.append(rec)

    # ---- findings overrides (LLM-adjudicated, findings_overrides.json) ----
    ovr_path = VERIF / "findings_overrides.json"
    ovr = read_json(ovr_path)
    overrides = {}
    overrides_meta = {}
    if isinstance(ovr, dict):
        sources.add_file(ovr_path)
        body = ovr.get("overrides") if isinstance(ovr.get("overrides"), dict) else ovr
        overrides = {k: v for k, v in body.items()
                     if k != "meta" and isinstance(v, dict)}
        overrides_meta = ovr.get("meta") or {}
    if overrides:
        for rec in contract_recs:
            if not rec["findings"]:
                continue
            kept = []
            for f in rec["findings"]:
                key = "%s#%s" % (rec["name"], hashlib.sha1(
                    f["text"].encode()).hexdigest()[:12])
                o = overrides.get(key)
                if not o:
                    kept.append(f)
                    continue
                if o.get("action") == "drop":
                    continue
                if (o.get("action") == "correct"
                        and o.get("kind") in ("refutes", "no_go", "supports", "open")):
                    f = dict(f, kind=o["kind"], override="llm")
                kept.append(f)
            rec["findings"] = kept

    for rec in contract_recs:
        contracts_total += 1
        if rec["verdict_class"] != "unknown":
            contracts_with_verdict += 1
        parse_source_dist.update([rec["parse_source"]])
        nid = f"contract:{rec['name']}"
        add_node(nid, "contract", rec["name"], {
            "date": rec["date"],
            "verdict_raw": clip(rec["verdict_raw"], 200),
            "verdict_class": rec["verdict_class"],
            "question": rec["question"],
            "checker": rec["checker"],
            "firewall": "experiments",
            "parse_source": rec["parse_source"],
            "gates": rec["gates"],
            "kills_free": rec["kills_free"],
            "claims_tested": rec["claims_tested"],
            "unresolved_claim_tokens": rec["unresolved_claim_tokens"],
            "exact_checks": rec["exact_checks"],
            "promotion": rec["promotion"],
            "missing": rec["missing"],
            "t1_t8_closed": rec["t1_t8_closed"],
            "not_derived": rec["not_derived"],
            "closes": rec["closes"],
            "leaves_open": rec["leaves_open"],
            "findings": rec["findings"],
            "summary_de": rec["summary_de"],
        })
        for cid, from_tok in rec["claims_tested"]:
            if cid in claim_ids:
                edge_attrs = {"resolved_from": from_tok} if from_tok else {}
                add_edge(nid, f"claim:{cid}", "tests", edge_attrs)
        for tok in rec["kills"]:
            if tok in claim_ids:
                add_edge(nid, f"claim:{tok}", "kills")
            else:
                nodes_by_id[nid]["attrs"]["kills_free"] = (
                    nodes_by_id[nid]["attrs"].get("kills_free") or []
                ) + [clip(tok, 120)]

    # ---- gates T1..T8 (Fix F): ledger claims win; else gate:* nodes ------
    gates_in_ledger = {f"T{i}" for i in range(1, 9)} & claim_ids
    gate_nodes_made = set()

    def gate_target(gid):
        if gid in gates_in_ledger:
            return f"claim:{gid}"
        if gid not in gate_nodes_made:
            add_node(f"gate:{gid}", "gate", gid, {"origin": "contract-mentions"})
            gate_nodes_made.add(gid)
        return f"gate:{gid}"

    for rec in contract_recs:
        nid = f"contract:{rec['name']}"
        for gid in rec["closes"]:
            add_edge(nid, gate_target(gid), "closes", {"source": "closed_gate_ids"})
        for gid in rec["leaves_open"]:
            add_edge(nid, gate_target(gid), "leaves_open", {"source": "prose"})

    # ---- inter-contract references (Fix E) -------------------------------
    slug_alt = "|".join(
        re.escape(s) for s in sorted(contract_names, key=len, reverse=True))
    slug_re = (re.compile(r"(?<![a-z0-9-])(?:" + slug_alt + r")(?![a-z0-9-])")
               if slug_alt else None)
    if slug_re is not None:
        for rec in contract_recs:
            src = f"contract:{rec['name']}"
            for where, fname in (("readme", "README.md"), ("results", "RESULTS.md")):
                fpath = CONTRACTS_DIR / rec["name"] / fname
                if not fpath.is_file():
                    continue
                try:
                    text = fpath.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                for slug in sorted(set(slug_re.findall(text))):
                    if slug != rec["name"]:
                        add_edge(src, f"contract:{slug}", "references",
                                 {"where": where})
        # next.txt lines naming several slugs -> co-mention references
        if NEXT_TXT.is_file():
            try:
                nt_lines = NEXT_TXT.read_text(
                    encoding="utf-8", errors="replace").splitlines()
            except OSError:
                nt_lines = []
            seen_pairs = set()
            for line in nt_lines:
                if not NEXTXT_LINE_RE.match(line):
                    continue
                slugs = list(dict.fromkeys(slug_re.findall(line)))
                for i in range(len(slugs)):
                    for j in range(i + 1, len(slugs)):
                        pair = (slugs[i], slugs[j])
                        if pair not in seen_pairs:
                            seen_pairs.add(pair)
                            add_edge(f"contract:{pair[0]}", f"contract:{pair[1]}",
                                     "references", {"where": "next_txt"})
    # LLM-backfilled relations (contract_index.json source=llm_backfill)
    for rec in contract_recs:
        src = f"contract:{rec['name']}"
        for rel in rec["relations_llm"]:
            if rel["target"] not in contract_names:
                continue
            rtype = rel.get("type") or "references"
            if rtype not in ("contradicts", "supports", "followup_of", "references"):
                rtype = "references"
            add_edge(src, f"contract:{rel['target']}", rtype,
                     {"where": "llm_backfill"})

    # ---- RH semantic catalog (firewall: rh-catalog) --------------------
    rh_path = ROOT / "rh" / "catalog" / "rh_semantic_catalog.json"
    rh = read_json(rh_path)
    if rh:
        sources.add_file(rh_path)
    rh_records = (rh or {}).get("records") or []
    for rec in rh_records:
        rpath = (rec.get("path") or "").strip()
        if not rpath:
            continue
        nid = f"rh:{rpath}"
        add_node(nid, "rh", rpath, {
            "outcome": rec.get("outcome"),
            "failure_class": rec.get("failure_class"),
            "family": rec.get("family"),
            "mechanism": clip(rec.get("mechanism"), 200),
            "question": clip(rec.get("question"), 200),
            "round": rec.get("round"),
            "firewall": "rh-catalog",
        })
        lids = [l for l in (rec.get("ledger_ids") or []) if l in claim_ids]
        for lid in lids:
            add_edge(nid, f"claim:{lid}", "references")
        if rec.get("outcome") == "KILLED":
            for lid in lids:
                add_edge(nid, f"claim:{lid}", "kills")

    # ---- experiments/ inventory (firewall: experiments; no dead spots) ---
    exp = inventory_experiments(sources, claim_ids)
    for nid, label, attrs in exp["nodes"]:
        add_node(nid, "experiment", label, attrs)
    for src, dst, etype, eattrs in exp["tests_edges"]:
        if dst in node_ids:
            add_edge(src, dst, etype, eattrs)
    # sourced_from: scorecard row source mentions the experiment dir name
    exp_dirs = [d for d in exp["dirs"] if len(d) >= 5]
    for n in nodes:
        if n["type"] != "scorecard":
            continue
        src_text = (n["attrs"].get("source") or "").lower().replace("_", "-")
        if not src_text:
            continue
        for d in exp_dirs:
            if d in src_text:
                add_edge(n["id"], f"experiment:{d}", "sourced_from")
    # ran_in: RH records whose path lives under experiments/tfpt-discovery/
    discovery_prefix = "experiments/tfpt-discovery/"
    probes_cataloged = set()
    for n in nodes:
        if n["type"] == "rh" and n["label"].startswith(discovery_prefix):
            probes_cataloged.add(n["label"])
            if "experiment:tfpt-discovery" in node_ids:
                add_edge(n["id"], "experiment:tfpt-discovery", "ran_in")
    # hub node for the experiments/ root meta
    add_node("hub:experiments", "hub", "experiments/", {
        "next_txt_entries": next_txt_entries,
        "next_txt_span": next_txt_span,
        "readme_present": (EXPERIMENTS_DIR / "README.md").is_file(),
        "signatures_present": (EXPERIMENTS_DIR / "SIGNATURES.md").is_file(),
        "probes_total": exp["probes_total"],
        "probes_cataloged": len(probes_cataloged),
        "firewall": "experiments",
    })
    # shallow listing hash: new/removed top-level dir (or contract folder)
    # must trip --check even though nothing inside it was parsed
    if EXPERIMENTS_DIR.is_dir():
        try:
            sources.records.append({
                "path": "experiments/",
                "sha256": experiments_shallow_sha(),
                "mtime": EXPERIMENTS_DIR.stat().st_mtime,
            })
        except OSError as exc:
            warn(f"cannot hash experiments/ listing: {exc}")
    # ---- Lean layer (rh/lean + lean4-carrier-rigidity; .lake excluded) ----
    lean = inventory_lean(sources, claim_ids)
    for nid, label, attrs in lean["nodes"]:
        add_node(nid, "lean", label, attrs)
    for src, dst in lean["imports_edges"]:
        if dst in node_ids:
            add_edge(src, dst, "imports")
    lean_by_path = {label: nid for nid, label, _a in lean["nodes"]}
    for nid, proves in lean["proves"].items():
        for cid, from_tok in proves:
            if f"claim:{cid}" in node_ids:
                add_edge(nid, f"claim:{cid}", "proves",
                         {"resolved_from": from_tok} if from_tok else {})
    # formalized_in: rh record path IS the lean file path
    for n in list(nodes):
        if n["type"] == "rh" and n["label"] in lean_by_path:
            add_edge(n["id"], lean_by_path[n["label"]], "formalized_in")
    # ledger script column 'lean4-carrier-rigidity[...]' -> proves edge from
    # the referenced file, else the project root module
    root_lean = "lean:experiments/lean4-carrier-rigidity/TfptCarrier.lean"
    for row in ledger:
        cid = (row.get("claim_id") or "").strip()
        if not cid or f"claim:{cid}" not in node_ids:
            continue
        for tok in (row.get("script") or "").split(";"):
            tok = tok.strip()
            if not tok.startswith("lean4-carrier-rigidity"):
                continue
            tgt = root_lean
            if "/" in tok:
                cand = f"lean:experiments/{tok}"
                if cand in node_ids:
                    tgt = cand
            if tgt in node_ids:
                add_edge(tgt, f"claim:{cid}", "proves",
                         {"source": "ledger_script"})

    # coverage guarantee: every top-level dir must have a node
    missing_nodes = [d for d in exp["dirs"] if f"experiment:{d}" not in node_ids]
    if missing_nodes:
        warn("experiments dirs WITHOUT node: " + ", ".join(missing_nodes))
    coverage = {
        "experiments_dirs_total": len(exp["dirs"]),
        "experiments_dirs_with_node": len(exp["dirs"]) - len(missing_nodes),
        "contracts_total": contracts_total,
        "contracts_with_verdict": contracts_with_verdict,
        "contracts_unknown": contracts_total - contracts_with_verdict,
    }

    # ---- graph v2 sidecar merge (schema verification/graph_v2/schema.json)
    sidecars = load_sidecars(sources)
    v2_stats = {"claim_contracts": 0, "transitions": 0, "constraints": 0,
                "failure_scopes": 0, "skipped": 0}
    # claim_contract: enrich existing claim nodes (premises stay ONE
    # conjunctive list -- never split into individual depends_on edges)
    for rec in sidecars["claim_contracts"]:
        if not isinstance(rec, dict):
            v2_stats["skipped"] += 1
            continue
        cid = rec.get("claim_id")
        if not cid or f"claim:{cid}" not in nodes_by_id:
            warn(f"claim_contract: unknown claim_id {cid!r} -- record skipped")
            v2_stats["skipped"] += 1
            continue
        if not provenance_ok(rec):
            warn(f"claim_contract {cid}: provenance.reviewed missing/not bool -- skipped")
            v2_stats["skipped"] += 1
            continue
        nodes_by_id[f"claim:{cid}"]["attrs"]["contract"] = {
            "statement": clip(rec.get("statement"), 400),
            "quantifiers": rec.get("quantifiers") or [],
            "limit": clip(rec.get("limit"), 120),
            "premises": rec.get("premises") or [],
            "chosen_structures": rec.get("chosen_structures") or [],
            "objects": rec.get("objects") or [],
            "epistemic": rec.get("epistemic"),
            "proof": rec.get("proof") or {},
            "provenance": rec.get("provenance"),
        }
        v2_stats["claim_contracts"] += 1
    # transition: own node type + trans_from/trans_to/checked_by edges
    seen_ids = set()
    for rec in sidecars["transitions"]:
        if not isinstance(rec, dict):
            v2_stats["skipped"] += 1
            continue
        tid = rec.get("id")
        if not tid or tid in seen_ids:
            warn(f"transition: duplicate/missing id {tid!r} -- skipped")
            v2_stats["skipped"] += 1
            continue
        if not provenance_ok(rec):
            warn(f"transition {tid}: provenance.reviewed missing/not bool -- skipped")
            v2_stats["skipped"] += 1
            continue
        seen_ids.add(tid)
        nid = f"transition:{tid}"
        status = rec.get("status")
        add_node(nid, "transition", tid, {
            "map": clip(rec.get("map"), 300),
            "preserves": rec.get("preserves") or [],
            "fails_to_preserve": rec.get("fails_to_preserve") or [],
            "status": status if status in ("established", "partial",
                                           "missing", "obstructed") else "missing",
            "counterexample": clip(rec.get("counterexample"), 200),
            "notes": clip(rec.get("notes"), 300),
            "from_raw": clip(rec.get("from"), 120),
            "to_raw": clip(rec.get("to"), 120),
            "provenance": rec.get("provenance"),
        })
        unresolved = []
        for etype, key in (("trans_from", "from"), ("trans_to", "to")):
            tgt = resolve_ref(rec.get(key), node_ids)
            if tgt:
                add_edge(nid, tgt, etype)
            elif rec.get(key):
                unresolved.append(f"{key}={rec.get(key)}")
        for cb in rec.get("checked_by") or []:
            tgt = resolve_ref(cb, node_ids)
            if tgt:
                add_edge(nid, tgt, "checked_by")
            else:
                unresolved.append(f"checked_by={cb}")
        if unresolved:
            nodes_by_id[nid]["attrs"]["unresolved"] = unresolved
        v2_stats["transitions"] += 1
    # constraint: on_object freetext attr + constrains / constrains_claim
    seen_ids = set()
    for rec in sidecars["constraints"]:
        if not isinstance(rec, dict):
            v2_stats["skipped"] += 1
            continue
        cid = rec.get("id")
        if not cid or cid in seen_ids:
            warn(f"constraint: duplicate/missing id {cid!r} -- skipped")
            v2_stats["skipped"] += 1
            continue
        if not provenance_ok(rec):
            warn(f"constraint {cid}: provenance.reviewed missing/not bool -- skipped")
            v2_stats["skipped"] += 1
            continue
        seen_ids.add(cid)
        nid = f"constraint:{cid}"
        add_node(nid, "constraint", cid, {
            "on_object": clip(rec.get("on_object"), 200),
            "requirement": clip(rec.get("requirement"), 300),
            "raised_by": rec.get("raised_by"),
            "independent_of": rec.get("independent_of") or [],
            "provenance": rec.get("provenance"),
        })
        tgt = resolve_ref(rec.get("on_object"), node_ids)
        if tgt:
            add_edge(nid, tgt, "constrains")
        rb = str(rec.get("raised_by") or "").strip()
        if rb in claim_ids:
            add_edge(nid, f"claim:{rb}", "constrains_claim")
        v2_stats["constraints"] += 1
    # failure_scope: excludes edges to evidence targets
    seen_ids = set()
    for rec in sidecars["failure_scopes"]:
        if not isinstance(rec, dict):
            v2_stats["skipped"] += 1
            continue
        fid = rec.get("id")
        if not fid or fid in seen_ids:
            warn(f"failure_scope: duplicate/missing id {fid!r} -- skipped")
            v2_stats["skipped"] += 1
            continue
        if not provenance_ok(rec):
            warn(f"failure_scope {fid}: provenance.reviewed missing/not bool -- skipped")
            v2_stats["skipped"] += 1
            continue
        seen_ids.add(fid)
        nid = f"failure:{fid}"
        add_node(nid, "failure", fid, {
            "target": clip(rec.get("target"), 300),
            "approach_class": clip(rec.get("approach_class"), 200),
            "excluded_under": rec.get("excluded_under") or [],
            "not_excluded": rec.get("not_excluded") or [],
            "retry_condition": clip(rec.get("retry_condition"), 300),
            "provenance": rec.get("provenance"),
        })
        unresolved = []
        for ev in rec.get("evidence") or []:
            tgt = resolve_ref(ev, node_ids)
            if tgt:
                add_edge(nid, tgt, "excludes")
            else:
                unresolved.append(str(ev))
        if unresolved:
            nodes_by_id[nid]["attrs"]["unresolved_evidence"] = unresolved
        v2_stats["failure_scopes"] += 1

    # ---- counts + meta --------------------------------------------------
    nodes.sort(key=lambda n: n["id"])
    edges.sort(key=lambda e: (e["type"], e["src"], e["dst"]))
    counts = {
        "nodes": len(nodes),
        "edges": len(edges),
        "nodes_by_type": dict(sorted(Counter(n["type"] for n in nodes).items())),
        "edges_by_type": dict(sorted(Counter(e["type"] for e in edges).items())),
        "contracts_with_verdict": contracts_with_verdict,
        "contracts_total": contracts_total,
        "contract_parse_source": dict(sorted(parse_source_dist.items())),
        "findings_total": sum(len(r["findings"]) for r in contract_recs),
        "findings_overrides": {
            "kept": overrides_meta.get("kept"),
            "corrected": overrides_meta.get("corrected"),
            "dropped": overrides_meta.get("dropped"),
        } if overrides_meta else None,
        "gate_nodes": len(gate_nodes_made),
        "v2": v2_stats,
    }
    # ---- acyclicity gate (schema Punkt 3): depends_on over claims MUST be
    # acyclic; cycles involving supersedes edges are warnings (supersedes is
    # a ledger bookkeeping relation, not a proof dependency)
    cycles = find_claim_cycles(edges)
    for cyc in cycles:
        path_s = " -> ".join(c.replace("claim:", "") for c in cyc["path"])
        if cyc["classified"] == "depends_on_pure":
            warn("cycle (depends_on pure, GATE): " + path_s)
        else:
            warn("cycle (supersedes involved, warning): " + path_s)
    return {
        "meta": {
            "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "generator": "build_theory_graph.py",
            "schema_version": SCHEMA_VERSION,
            "sources": sources.records,
            "counts": counts,
            "coverage": coverage,
            "cycles": cycles,
        },
        "nodes": nodes,
        "edges": edges,
    }


# --------------------------------------------------------------------------
# theory_primer.md (GENERATED)
# --------------------------------------------------------------------------

def gen_primer(graph: dict) -> str:
    counts = graph["meta"]["counts"]
    nodes = graph["nodes"]
    edges = graph["edges"]
    claims = [n for n in nodes if n["type"] == "claim"]
    contracts = [n for n in nodes if n["type"] == "contract"]
    rhs = [n for n in nodes if n["type"] == "rh"]
    scs = [n for n in nodes if n["type"] == "scorecard"]

    verified = defaultdict(list)
    for e in edges:
        if e["type"] == "verified_by":
            verified[e["src"]].append(e["dst"].split(":", 1)[1])

    marker_counts = Counter()
    for n in claims:
        for mk in n["attrs"].get("markers") or []:
            marker_counts.update([mk])

    open_claims = [
        n for n in claims
        if "O" in (n["attrs"].get("markers") or [])
        or (n["attrs"].get("status_raw") or "").startswith("Open")
    ]
    open_claims.sort(key=lambda n: (not n["label"].startswith("GATE."), n["label"]))

    dated = [c for c in contracts if c["attrs"].get("date")]
    dated.sort(key=lambda c: (c["attrs"]["date"], c["label"]), reverse=True)
    undated = [c for c in contracts if not c["attrs"].get("date")]
    recent = dated + sorted(undated, key=lambda c: c["label"])

    rh_fail = Counter(n["attrs"].get("failure_class") or "?" for n in rhs)
    contract_vc = Counter(n["attrs"].get("verdict_class") for n in contracts)
    sc_status = Counter(n["attrs"].get("status") or "?" for n in scs)

    L = []
    A = L.append
    A("<!-- GENERATED by build_theory_graph.py -- do not edit -->")
    A("")
    A("# Theory graph primer")
    A("")
    A("## 1 · Was das ist")
    A("")
    A("Maschinenlesbarer Graph über `verification/theory_graph.json`: wer claims was")
    A("(Ledger), welches Script verifiziert es (Registry), wo steht es (docs_map),")
    A("welches Experiment bzw. welcher Contract es mit welchem Ausgang testete")
    A("(Scorecard/theory-contracts, Firewall `experiments`), was wurde getötet")
    A("(RH-Katalog, Firewall `rh-catalog`). Neu bauen: `python3 verification/build_theory_graph.py`.")
    A("")
    A("Abfragen mit `python3 verification/theorycat.py <cmd>`:")
    A("")
    A("```bash")
    A("python3 verification/theorycat.py stats              # counts + Verteilungen")
    A("python3 verification/theorycat.py claim EM.FP.01     # ein Claim + seine Edges")
    A("python3 verification/theorycat.py tried 'torsor'     # alle Versuche zum Thema")
    A("python3 verification/theorycat.py kills              # alles Getötete")
    A("python3 verification/theorycat.py open               # offene Fronten")
    A("python3 verification/theorycat.py path AX.P1.01 EM.FP.01   # Abhängigkeitspfad")
    A("```")
    A("")
    A("## 2 · Counts")
    A("")
    A("| | n |")
    A("|---|---:|")
    A(f"| nodes | {counts['nodes']} |")
    A(f"| edges | {counts['edges']} |")
    for t, n in counts["nodes_by_type"].items():
        A(f"| nodes.{t} | {n} |")
    for t, n in counts["edges_by_type"].items():
        A(f"| edges.{t} | {n} |")
    A(f"| contracts with verdict | {counts['contracts_with_verdict']} / {counts['contracts_total']} |")
    A("")
    A("## 3 · Claim-Status-Marker (Ledger, `[X]` im Status-Freitext)")
    A("")
    A("| marker | n |")
    A("|---|---:|")
    for mk in "ECOXPLANF":
        A(f"| [{mk}] | {marker_counts.get(mk, 0)} |")
    A("")
    A(f"Claims gesamt: {len(claims)}; davon aktiv: "
      f"{sum(1 for n in claims if n['attrs'].get('active'))}.")
    A("")
    A("## 4 · Offene Gates / Fronten (Marker `[O]` oder Status `Open*`, Top 30)")
    A("")
    A("| claim | status | script |")
    A("|---|---|---|")
    for n in open_claims[:30]:
        scripts = ", ".join(verified.get(n["id"], [])) or "-"
        A(f"| {n['label']} | {clip(n['attrs'].get('status_raw'), 80)} | {clip(scripts, 60)} |")
    A("")
    A(f"Offene Claims gesamt: {len(open_claims)} "
      f"(davon GATE.*: {sum(1 for n in open_claims if n['label'].startswith('GATE.'))}).")
    A("")
    A("## 5 · Letzte 20 Contract-Verdicts")
    A("")
    A("| datum | contract | verdict |")
    A("|---|---|---|")
    for c in recent[:20]:
        a = c["attrs"]
        d = a.get("date") or "-"
        if d != "-" and len(d) == 8:
            d = f"{d[:4]}-{d[4:6]}-{d[6:]}"
        A(f"| {d} | {c['label']} | {clip(a.get('verdict_raw') or '*(unknown)*', 50)} |")
    A("")
    A("## 6 · Kill-Statistik")
    A("")
    A("RH-Katalog `failure_class`:")
    A("")
    A("| failure_class | n |")
    A("|---|---:|")
    for k, n in rh_fail.most_common():
        A(f"| {k} | {n} |")
    A("")
    A("Contract `verdict_class`:")
    A("")
    A("| verdict_class | n |")
    A("|---|---:|")
    for k, n in contract_vc.most_common():
        A(f"| {k} | {n} |")
    A("")
    A("## 7 · Scorecard-Status (Firewall `experiments`)")
    A("")
    A("| status | n |")
    A("|---|---:|")
    for k, n in sc_status.most_common():
        A(f"| {k} | {n} |")
    A("")
    # ---- section 8: experiments coverage -------------------------------
    coverage = graph["meta"].get("coverage") or {}
    experiments = [n for n in nodes if n["type"] == "experiment"]
    experiments.sort(key=lambda n: n["label"])
    ps_dist = counts.get("contract_parse_source") or {}
    A("## 8 · Experiments coverage (keine toten Stellen)")
    A("")
    A(f"Coverage: **{coverage.get('experiments_dirs_with_node', '?')} / "
      f"{coverage.get('experiments_dirs_total', '?')}** Verzeichnisse mit Node · "
      f"Contracts mit Verdict: **{counts.get('contracts_with_verdict', '?')} / "
      f"{counts.get('contracts_total', '?')}** "
      f"(unknown: {coverage.get('contracts_unknown', '?')}).")
    A("")
    A("Backfill `parse_source`: " + ", ".join(
        f"{k}={v}" for k, v in sorted(ps_dist.items())) + ".")
    A("")
    A("| dir | kind | verdict_class | n_files |")
    A("|---|---|---|---:|")
    for n in experiments:
        a = n["attrs"]
        A(f"| {n['label']} | {a.get('kind')} | {a.get('verdict_class')} | "
          f"{a.get('n_files', 0)} |")
    A("")
    # ---- section 9: latest findings --------------------------------------
    all_findings = []
    for c in contracts:
        for f in (c["attrs"].get("findings") or []):
            all_findings.append((c["attrs"].get("date") or "", c["label"], f))
    all_findings.sort(key=lambda x: (x[0], x[1]), reverse=True)
    A("## 9 · Letzte Findings (Verdict-tragende Sätze aus README/RESULTS)")
    A("")
    A(f"Findings gesamt: {counts.get('findings_total', 0)}.")
    A("")
    A("| datum | kind | contract | text |")
    A("|---|---|---|---|")
    for date, label, f in all_findings[:15]:
        d = f"{date[:4]}-{date[4:6]}-{date[6:]}" if len(date) == 8 else (date or "-")
        A(f"| {d} | {f.get('kind')} | {label} | {clip(f.get('text'), 80)} |")
    A("")
    # ---- section 10: v2 reasoning layer ----------------------------------
    transitions = [n for n in nodes if n["type"] == "transition"]
    constraints = [n for n in nodes if n["type"] == "constraint"]
    failures = [n for n in nodes if n["type"] == "failure"]
    open_trans = [n for n in transitions
                  if n["attrs"].get("status") in ("missing", "obstructed")]
    open_trans.sort(key=lambda n: n["label"])
    A("## 10 · Offene Übergänge (v2 transitions: missing/obstructed)")
    A("")
    A("| id | status | von -> zu | map |")
    A("|---|---|---|---|")
    for n in open_trans[:20]:
        a = n["attrs"]
        A(f"| {n['label']} | {a.get('status')} | "
          f"{clip(a.get('from_raw'), 30)} -> {clip(a.get('to_raw'), 30)} | "
          f"{clip(a.get('map'), 50)} |")
    if not open_trans:
        A("| *(keine — Sidecar transitions.json noch leer)* | | | |")
    A("")
    # next heuristic, top 10 (same formula as theorycat next)
    radj = defaultdict(list)
    for e in edges:
        if e["type"] == "depends_on":
            radj[e["dst"]].append(e["src"])
    verified_claims = {e["src"] for e in edges if e["type"] == "verified_by"}

    def n_dep(nid):
        seen = set()
        queue = [nid]
        while queue:
            cur = queue.pop()
            for nb in radj.get(cur, []):
                if nb not in seen:
                    seen.add(nb)
                    queue.append(nb)
        return len(seen)

    next_rows = []
    for n in open_claims:
        score = (2 * n_dep(n["id"])
                 + (3 if "GATE." in n["label"] else 0)
                 + (1 if n["id"] in verified_claims else 0))
        next_rows.append((score, n["label"]))
    next_rows.sort(key=lambda x: (-x[0], x[1]))
    A("## 11 · Top-Kandidaten `next` (Heuristik: 2xAbhängige +3xGATE +1xChecker)")
    A("")
    A("| claim | score |")
    A("|---|---:|")
    for score, label in next_rows[:10]:
        A(f"| {label} | {score} |")
    A("")
    n_contra = (sum(1 for e in edges if e["type"] == "contradicts")
                + sum(1 for n in contracts for f in (n["attrs"].get("findings") or [])
                      if f.get("kind") in ("refutes", "no_go"))
                + sum(1 for n in scs if n["attrs"].get("status") == "tension"))
    A("## 12 · Widersprüche (contradicts + refutes/no_go + tension)")
    A("")
    A(f"Gesamt: **{n_contra}** (Details: `theorycat.py contradictions`).")
    A("")
    ref_rows = []
    for n in contracts:
        for f in (n["attrs"].get("findings") or []):
            if f.get("kind") in ("refutes", "no_go"):
                ref_rows.append((n["attrs"].get("date") or "", f.get("kind"),
                                 n["label"], f.get("text") or ""))
    ref_rows.sort(key=lambda r: (r[0], r[2]), reverse=True)
    A("| datum | kind | contract | text |")
    A("|---|---|---|---|")
    for d, k, label, text in ref_rows[:5]:
        dd = f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else (d or "-")
        A(f"| {dd} | {k} | {label} | {clip(text, 60)} |")
    A("")
    A(f"_v2: transitions={len(transitions)} constraints={len(constraints)} "
      f"failure_scopes={len(failures)} (Sidecars in `verification/graph_v2/`)_")
    A("")
    # ---- Zyklen-Warnung ---------------------------------------------------
    cycles = graph["meta"].get("cycles") or []
    pure = [c for c in cycles if isinstance(c, dict)
            and c.get("classified") == "depends_on_pure"]
    warned = [c for c in cycles if isinstance(c, dict)
              and c.get("classified") != "depends_on_pure"]
    A("## 13 · Zyklen-Warnung (Claim-Graph depends_on/supersedes)")
    A("")
    A(f"depends_on-pure Zyklen (Gate rot): **{len(pure)}** · "
      f"mit supersedes-Beteiligung (Warnung): **{len(warned)}**.")
    A("")
    if warned:
        A("| zyklus (gekürzt) | supersedes-kanten |")
        A("|---|---|")
        for c in warned[:13]:
            path = " → ".join(x.replace("claim:", "") for x in c.get("path", []))
            A(f"| {clip(path, 70)} | {clip('; '.join(c.get('supersedes_steps') or []), 60)} |")
        A("")
    A(f"_Generiert: {graph['meta']['generated']} · schema v{graph['meta']['schema_version']}_")
    A("")
    return "\n".join(L)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def stale_sources(graph: dict) -> list:
    """Recompute sha256 over meta.sources; return list of stale entries."""
    stale = []
    for rec in (graph.get("meta") or {}).get("sources") or []:
        rel_path = rec.get("path") or ""
        path = ROOT / rel_path.rstrip("/")
        try:
            if rel_path == "experiments/":
                current = experiments_shallow_sha()
            elif rel_path.endswith("/"):
                current = dir_listing_sha(path)
            else:
                current = sha256_file(path)
        except OSError:
            stale.append(f"{rel_path} (missing)")
            continue
        if current != rec.get("sha256"):
            stale.append(f"{rel_path} (hash drift)")
    return stale


def run_check() -> int:
    if not GRAPH_PATH.is_file():
        print(f"[THEORY-GRAPH] stale: {rel(GRAPH_PATH)} missing -- "
              f"run: python3 verification/build_theory_graph.py")
        return 1
    try:
        graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[THEORY-GRAPH] stale: {rel(GRAPH_PATH)} unreadable ({exc}) -- "
              f"run: python3 verification/build_theory_graph.py")
        return 1
    stale = stale_sources(graph)
    if stale:
        for s in stale[:20]:
            print(f"[THEORY-GRAPH] stale: {s}")
        if len(stale) > 20:
            print(f"[THEORY-GRAPH] stale: ... and {len(stale) - 20} more")
        print("[THEORY-GRAPH] re-run: python3 verification/build_theory_graph.py")
        return 1
    # acyclicity gate: only PURE depends_on cycles fail (proof cycles);
    # supersedes-involved cycles are bookkeeping warnings
    cycles = (graph.get("meta") or {}).get("cycles") or []
    pure = []
    warned = []
    for cyc in cycles:
        if isinstance(cyc, dict) and cyc.get("classified") != "depends_on_pure":
            warned.append(cyc)
        else:
            pure.append(cyc)  # unknown/old format: fail-safe = treat as pure
    for cyc in warned:
        path = cyc.get("path") or []
        print("[THEORY-GRAPH] cycle warning (supersedes involved): "
              + " -> ".join(c.replace("claim:", "") for c in path))
    if pure:
        critical = []
        for cyc in pure:
            path = cyc.get("path") if isinstance(cyc, dict) else cyc
            nodes = [c.replace("claim:", "") for c in (path or [])]
            if any(n.startswith("AX.") or n.startswith("BOOT") for n in nodes):
                critical.append(nodes)
            else:
                print("[THEORY-GRAPH] cycle warning (depends_on core, non-axiom): "
                      + " -> ".join(nodes))
        if critical:
            for nodes in critical[:10]:
                print("[THEORY-GRAPH] cycle (axiom/root, GATE): " + " -> ".join(nodes))
            if len(critical) > 10:
                print(f"[THEORY-GRAPH] cycle: ... and {len(critical) - 10} more")
            return 1
    counts = (graph.get("meta") or {}).get("counts") or {}
    print(f"THEORY-GRAPH OK ({counts.get('nodes', '?')} nodes, {counts.get('edges', '?')} edges)")
    return 0


def atomic_write(path: Path, text: str) -> None:
    """tmp-file + os.replace: the graph is never partially readable."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def main() -> None:
    if "--check" in sys.argv:
        sys.exit(run_check())
    graph = build()
    atomic_write(
        GRAPH_PATH,
        json.dumps(graph, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
    )
    print(f"wrote {rel(GRAPH_PATH)}")
    atomic_write(PRIMER_PATH, gen_primer(graph))
    print(f"wrote {rel(PRIMER_PATH)}")
    c = graph["meta"]["counts"]
    print(f"THEORY-GRAPH built: {c['nodes']} nodes, {c['edges']} edges, "
          f"contracts {c['contracts_with_verdict']}/{c['contracts_total']} with verdict")


if __name__ == "__main__":
    main()
