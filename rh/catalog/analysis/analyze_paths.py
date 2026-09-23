#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic T1–T6 path analysis from the RH semantic catalog.

stdlib only. Research documentation. NO RH CLAIM.
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG_DIR = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(CATALOG_DIR, "..", ".."))
CATALOG_PATH = os.path.join(CATALOG_DIR, "rh_semantic_catalog.json")
TAXONOMY_PATH = os.path.join(CATALOG_DIR, "taxonomy.json")
OUT_REPORT = os.path.join(HERE, "paths_report.json")
SNAPSHOT_728 = os.path.join(HERE, "paths_report_728.json")
OUT_DIFF = os.path.join(HERE, "paths_report_diff.json")

CLAIM = "Structured research map only. No claim for or against RH."

OUTCOMES = (
    "PROVED",
    "CERTIFIED",
    "MEASURED",
    "KILLED",
    "INCONCLUSIVE",
    "OPEN",
    "RESTATED",
    "SEALED",
)
FAILURES = (
    "CIRCULAR",
    "WORLD_BLIND",
    "LOSSY_CONSTANT",
    "STRUCTURAL_MISMATCH",
    "NUMERIC_ARTIFACT",
    "ORACLE_LEAK",
    "RESTATEMENT",
    "NO_BRIDGE",
    "UNCONVERGED",
    "NOT_APPLICABLE",
)
ALIVE_KINDS = {"FOUNDATION", "REDUCTION", "CERTIFICATE"}
ALIVE_OUTCOMES = {"PROVED", "CERTIFIED"}
HARD_KILL = {"CIRCULAR", "WORLD_BLIND", "LOSSY_CONSTANT", "RESTATEMENT"}
STUB_REUSABLE = (
    "prime-front / prime.* suite module absent",
    "section-level path for corpus search",
)
VN_PATH_RE = re.compile(r"verification/v(\d+)_")
ROUND_RE = re.compile(r"r(\d+)", re.I)
EARLY_STACK = (
    "WEIL_POSITIVITY_WINDOWS",
    "SCREW_SUBORDINATION_LSTAR",
    "LEAN_FORMALIZATION",
    "EXPLICIT_FORMULA_IDENTITY",
    "OPERATOR_SPECTRAL",
    "RHP_IIKS_TAU",
    "TOEPLITZ_MOMENT_POSITIVITY",
    "MELLIN_PICK_LEE_YANG",
    "CERTIFICATE_INFRASTRUCTURE",
)
ROOT_RULES = (
    (
        "factor 2 loss",
        ("factor-two", "factor two", "factor-2", "factor 2"),
        "A fixed factor-two loss already exceeds the doubly-exponentially small Weil margin.",
    ),
    (
        "Hankel not Toeplitz",
        ("hankel not", "not toeplitz", "hankel/toeplitz", "hankel versus toeplitz"),
        "The additive Selberg kernel has the wrong displacement geometry for a square/Toeplitz object.",
    ),
    (
        "restates h>0",
        ("restates h>0", "h>0", "h > 0"),
        "The proposed lemma is equivalent to the original moment-positivity target.",
    ),
    (
        "compact model versus noncompact primes",
        ("noncompact", "compact completion", "compact-tail", "compact tail"),
        "Compact completion cannot absorb the translated prime channel.",
    ),
    (
        "no cofinal bridge",
        ("no cofinal", "not cofinal", "cofinal bridge"),
        "Finite or local identities do not extend to the required cofinal statement.",
    ),
    (
        "no source-pure certificate",
        ("source-pure", "source positivity"),
        "The certificate imports the source positivity it was meant to explain.",
    ),
    (
        "RH-near cancellation assumed",
        ("circular", "rh-scale", "rh-near", "begs the"),
        "The missing cancellation is already RH-scale and therefore circular.",
    ),
    (
        "float64 or precision artifact",
        ("float64", "precision artifact", "numeric artifact", "discretization"),
        "The apparent signal disappears under higher precision or stable exact reconstruction.",
    ),
    (
        "fit, alias, or holdout artifact",
        ("alias", "holdout", "overfit", "fitted"),
        "The pattern is explained by fitting, aliasing, or absent held-out data.",
    ),
    (
        "known mechanism renamed",
        ("renamed", "classical mechanism", "complexity class"),
        "The construction reproduces an existing classical mechanism or complexity class.",
    ),
    (
        "restatement without new inequality",
        ("restatement", "no independent", "no new inequality"),
        "No independent inequality is added to the existing equivalent formulation.",
    ),
    (
        "world-blind invariant",
        ("world-blind", "world blind", "control world", "survives control"),
        "The statistic survives control worlds, so it cannot transport arithmetic positivity.",
    ),
    (
        "bound exceeds vanishing margin",
        ("vanishing margin", "exceeds", "majorant"),
        "The available majorant is larger than the certified target margin.",
    ),
    (
        "nonuniform or lossy constant",
        ("lossy", "nonuniform", "no uniform"),
        "The estimate has no loss-free uniform constant on the cofinal family.",
    ),
    (
        "target reparameterized",
        ("reparameter", "same target", "new coordinates"),
        "The new coordinates preserve the unresolved target without adding a sign source.",
    ),
    (
        "positivity cone or sign mismatch",
        ("cone", "sign mismatch", "sign source", "positive cone"),
        "The proposed positive cone is not preserved by the signed arithmetic object.",
    ),
    (
        "wrong index, edge, or mode",
        ("wrong index", "wrong edge", "wrong mode", "different index", "spectral mode"),
        "The observed transition belongs to a different index or spectral mode.",
    ),
    (
        "wrong carrier or object",
        ("wrong carrier", "incompatible carrier"),
        "The compared quantities live on incompatible carriers or represent different operators.",
    ),
    (
        "no bridge to RH positivity",
        ("no bridge", "no dictionary", "no proved dictionary"),
        "The construction has no proved dictionary to the required positivity statement.",
    ),
    (
        "structural object mismatch",
        ("structural", "mismatch", "incompatible"),
        "The proposed exact dictionary identifies objects with incompatible structure.",
    ),
)
CLASS_ROOT = {
    "WORLD_BLIND": "world-blind invariant",
    "CIRCULAR": "RH-near cancellation assumed",
    "LOSSY_CONSTANT": "nonuniform or lossy constant",
    "RESTATEMENT": "restatement without new inequality",
    "NO_BRIDGE": "no bridge to RH positivity",
    "NUMERIC_ARTIFACT": "float64 or precision artifact",
    "STRUCTURAL_MISMATCH": "structural object mismatch",
    "ORACLE_LEAK": "fit, alias, or holdout artifact",
    "UNCONVERGED": "no cofinal bridge",
}
ROOT_STRUCT = {phrase: text for phrase, _keys, text in ROOT_RULES}
PAIR_CONSTRAINT = {
    frozenset(("TOEPLITZ_MOMENT_POSITIVITY", "WEIL_POSITIVITY_WINDOWS")): (
        "FAIL",
        "C1",
        "An exact congruence from Weil windows to a moment matrix would be loss-free; no such congruence is recorded, and Hankel/Toeplitz geometry conflicts.",
    ),
    frozenset(("MELLIN_PICK_LEE_YANG", "WEIL_POSITIVITY_WINDOWS")): (
        "FAIL",
        "C2",
        "Mellin continuation could probe window kernels beyond sampled positive data; certified non-real failures already block global Pick positivity.",
    ),
    frozenset(("MELLIN_PICK_LEE_YANG", "RHP_IIKS_TAU")): (
        "FAIL",
        "C2",
        "RHP continuation could expose complex-plane defects invisible to moments; the known Mellin–Pick continuation already has frozen non-Pick points.",
    ),
    frozenset(("ADELIC_GROUPOID_CONNES", "MELLIN_PICK_LEE_YANG")): (
        "FAIL",
        "C2",
        "Boundary half-densities could define a Mellin kernel, but natural analytic interpolants already fail off the positive axis.",
    ),
    frozenset(("ADELIC_GROUPOID_CONNES", "OPERATOR_SPECTRAL")): (
        "FAIL",
        "C3",
        "An exact groupoid representation could geometrize the spectral operator, but the identity side is already complete and supplies no sign.",
    ),
    frozenset(("LATTICE_E8_HECKE", "WEIL_POSITIVITY_WINDOWS")): (
        "FAIL",
        "C4",
        "E8 identities might rigidify coefficients; catalog controls treat the data as RH-neutral and unmatched to Xi positivity.",
    ),
    frozenset(("LEAN_FORMALIZATION", "TOEPLITZ_MOMENT_POSITIVITY")): (
        "PASS",
        "C1-C5",
        "Formalizing exact finite moment bricks is compatible with the recorded constraints, but by itself creates no new positivity source.",
    ),
}
OPEN_CENTER_HINTS = (
    ("lstar", "L* contraction path", "C5"),
    ("lambda_*", "L* contraction path", "C5"),
    ("lambdastar", "L* contraction path", "C5"),
    ("mincut", "FREQ mincut path", "C5"),
    ("gabor", "Countable Gabor positivity path", "C5"),
)


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path, obj):
    text = json.dumps(obj, indent=2, ensure_ascii=False)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.write("\n")


def is_curated(rec):
    return not rec.get("draft")


def is_stub_reusable(text):
    low = (text or "").strip().lower()
    return any(low.startswith(p) for p in STUB_REUSABLE)


def has_e_marker(rec):
    blob = "%s %s" % (rec.get("solved") or "", rec.get("status_raw") or "")
    return "[E]" in blob


def vn_of(path):
    m = VN_PATH_RE.search(path or "")
    return int(m.group(1)) if m else None


def round_nums(text):
    return [int(x) for x in ROUND_RE.findall(text or "")]


def first_round(rec):
    nums = round_nums(rec.get("round"))
    if nums:
        return nums[0]
    n = vn_of(rec.get("path"))
    return n if n is not None else 10**9


def basename(path):
    return os.path.basename(path or "")


def object_stem(path):
    name = basename(path)
    stem, _ext = os.path.splitext(name)
    for pref in ("verify_",):
        if stem.startswith(pref):
            stem = stem[len(pref) :]
    for suf in ("_probe", "_result", "_companion"):
        if stem.endswith(suf):
            stem = stem[: -len(suf)]
    return stem


def clip(text, n=80):
    text = re.sub(r"\s+", " ", (text or "").strip())
    if len(text) <= n:
        return text
    return text[: n - 1].rstrip() + "…"


def empty_counts(keys):
    return {k: 0 for k in keys}


def count_field(rows, field, keys):
    out = empty_counts(keys)
    for r in rows:
        val = r.get(field)
        if val in out:
            out[val] += 1
    return out


def member(rec):
    return {"round": rec.get("round") or "", "path": rec.get("path") or ""}


def rec_brief(rec, extra=None):
    row = {
        "round": rec.get("round") or "",
        "path": rec.get("path") or "",
        "outcome": rec.get("outcome") or "",
        "summary": clip(rec.get("question") or rec.get("solved") or "", 90),
    }
    if extra:
        row.update(extra)
    return row


def pick_open(rows):
    opens = [r for r in rows if r.get("outcome") == "OPEN"]
    if not opens:
        return None
    load = [r for r in opens if r.get("rh_relevance") == "LOAD_BEARING_OPEN"]
    pool = load or opens

    def score(r):
        path = r.get("path") or ""
        ext = 2 if path.endswith(".tex") else 1 if path.endswith(".py") else 0
        loc = 1 if path.startswith("experiments/") or path.startswith("rh/problem/") else 0
        return (
            1 if r.get("rh_relevance") == "LOAD_BEARING_OPEN" else 0,
            ext,
            loc,
            -first_round(r),
            path,
        )

    best = max(pool, key=score)
    return rec_brief(best)


def pick_strong(rows):
    pool = [r for r in rows if r.get("outcome") in ("PROVED", "CERTIFIED")]
    if not pool:
        return None

    def score(r):
        path = r.get("path") or ""
        proven = 2 if r.get("outcome") == "PROVED" else 1
        loc = 2 if path.startswith("verification/") or path.startswith("rh/lean/") else 1
        kind = 1 if r.get("kind") in ALIVE_KINDS else 0
        return (proven, loc, kind, -first_round(r), path)

    best = max(pool, key=score)
    return rec_brief(best)


def build_indexes(curated):
    by_path = {r["path"]: r for r in curated}
    by_base = defaultdict(list)
    by_round = defaultdict(list)
    by_vn = defaultdict(list)
    by_led = defaultdict(list)
    for r in curated:
        by_base[basename(r.get("path"))].append(r)
        by_round[r.get("round") or ""].append(r)
        n = vn_of(r.get("path"))
        if n is not None:
            by_vn["v%d" % n].append(r)
        for lid in r.get("ledger_ids") or []:
            by_led[lid].append(r)
    return by_path, by_base, by_round, by_vn, by_led


def resolve_dep(tok, indexes):
    by_path, by_base, by_round, by_vn, by_led = indexes
    hits = []
    if tok in by_path:
        hits.append(by_path[tok])
    hits.extend(by_base.get(tok, []))
    hits.extend(by_base.get(basename(tok), []))
    if tok in by_round:
        hits.extend(by_round[tok])
    if tok in by_vn:
        hits.extend(by_vn[tok])
    if tok in by_led:
        hits.extend(by_led[tok])
    m = re.match(r"v(\d+)$", tok or "")
    if m:
        hits.extend(by_vn.get("v%s" % m.group(1), []))
    seen = set()
    out = []
    for h in hits:
        p = h.get("path")
        if p and p not in seen:
            seen.add(p)
            out.append(h)
    return out


def depended_paths(curated, indexes):
    used = set()
    for rec in curated:
        for tok in rec.get("depends_on") or []:
            for hit in resolve_dep(tok, indexes):
                if hit.get("path") != rec.get("path"):
                    used.add(hit.get("path"))
    return used


def family_matrix(rows, families, all_rows=None):
    out = []
    for fam in families:
        group = [r for r in rows if r.get("family") == fam]
        item = {
            "family": fam,
            "records": len(group),
            "outcomes": count_field(group, "outcome", OUTCOMES),
            "failure_classes": count_field(group, "failure_class", FAILURES),
            "most_load_bearing_open": pick_open(group),
            "strongest_proved_or_certified": pick_strong(group),
        }
        if all_rows is not None:
            ag = [r for r in all_rows if r.get("family") == fam]
            item["records_all"] = len(ag)
            item["outcomes_all"] = count_field(ag, "outcome", OUTCOMES)
            item["failure_classes_all"] = count_field(ag, "failure_class", FAILURES)
        out.append(item)
    return out


def classify_root(rec):
    text = "%s %s" % (rec.get("failed_because") or "", rec.get("solved") or "")
    low = text.lower()
    for phrase, keys, _struct in ROOT_RULES:
        if any(k in low for k in keys):
            return phrase
    return CLASS_ROOT.get(rec.get("failure_class") or "", "unclustered root")


def t2_kills(curated):
    killed = [r for r in curated if r.get("outcome") == "KILLED"]
    by_cls = defaultdict(list)
    by_root = defaultdict(list)
    for rec in killed:
        by_cls[rec.get("failure_class") or "NOT_APPLICABLE"].append(rec)
        by_root[classify_root(rec)].append(rec)
    class_rows = []
    for cls in FAILURES:
        members = by_cls.get(cls) or []
        if not members:
            continue
        members = sorted(members, key=lambda r: (first_round(r), r.get("path") or ""))
        class_rows.append(
            {
                "failure_class": cls,
                "count": len(members),
                "members": [member(r) for r in members],
            }
        )
    root_rows = []
    for phrase, members in sorted(by_root.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        members = sorted(members, key=lambda r: (first_round(r), r.get("path") or ""))
        root_rows.append(
            {
                "root_phrase": phrase,
                "count": len(members),
                "structural_root": ROOT_STRUCT.get(
                    phrase,
                    "Recurring failed_because cluster; no independent positivity source is added.",
                ),
                "members": [member(r) for r in members],
            }
        )
    return {
        "killed_total": len(killed),
        "by_failure_class": class_rows,
        "by_recurring_root": root_rows,
    }


def t3_orphans(curated, used):
    eligible = []
    for rec in curated:
        if rec.get("kind") not in ALIVE_KINDS:
            continue
        if rec.get("outcome") not in ALIVE_OUTCOMES:
            continue
        if is_stub_reusable(rec.get("reusable")):
            continue
        if rec.get("path") in used:
            continue
        eligible.append(rec)

    def score(r):
        return (
            1 if has_e_marker(r) else 0,
            2 if r.get("outcome") == "PROVED" else 1,
            1 if r.get("kind") == "FOUNDATION" else 0,
            -first_round(r),
            r.get("path") or "",
        )

    ranked = sorted(eligible, key=score, reverse=True)
    top = []
    for i, rec in enumerate(ranked[:12], start=1):
        secs = rec.get("family_secondary") or []
        top.append(
            {
                "rank": i,
                "round": rec.get("round") or "",
                "path": rec.get("path") or "",
                "family": rec.get("family") or "",
                "reusable": clip(rec.get("reusable") or "", 100),
                "potential": clip(rec.get("question") or rec.get("solved") or "", 120),
                "consumer_family": secs[0] if secs else rec.get("family") or "",
            }
        )
    e_orphans = []
    for rec in curated:
        n = vn_of(rec.get("path"))
        if n is None or not (535 <= n <= 954):
            continue
        if not has_e_marker(rec):
            continue
        if rec.get("outcome") not in ALIVE_OUTCOMES:
            continue
        if rec.get("path") in used:
            continue
        e_orphans.append(
            {
                "round": rec.get("round") or "",
                "path": rec.get("path") or "",
                "family": rec.get("family") or "",
                "kind": rec.get("kind") or "",
                "outcome": rec.get("outcome") or "",
                "solved": clip(rec.get("solved") or "", 120),
            }
        )
    e_orphans.sort(key=lambda r: (vn_of(r["path"]) or 0, r["path"]))
    return {
        "eligible_total": len(eligible),
        "ranked_top": top,
        "v535_v954_E_orphans": e_orphans,
        "v535_v954_E_orphan_count": len(e_orphans),
    }


def observed_family_pairs(curated, families):
    observed = set()
    for rec in curated:
        f = rec.get("family")
        if f not in families:
            continue
        for s in rec.get("family_secondary") or []:
            if s in families and s != f:
                observed.add(tuple(sorted((f, s))))
    return observed


def screen_pair(a, b, fam_killed):
    key = frozenset((a, b))
    if key in PAIR_CONSTRAINT:
        screen, constraint, why = PAIR_CONSTRAINT[key]
        return {
            "pair": sorted([a, b]),
            "why": why,
            "screen": screen,
            "constraint": constraint,
        }
    hard_a = sum(fam_killed[a].get(c, 0) for c in HARD_KILL)
    hard_b = sum(fam_killed[b].get(c, 0) for c in HARD_KILL)
    lean = "LEAN_FORMALIZATION" in (a, b)
    if lean and hard_a + hard_b == 0:
        return {
            "pair": sorted([a, b]),
            "why": "Formalization of an existing finite brick is compatible with recorded constraints but adds no new sign source.",
            "screen": "PASS",
            "constraint": "C1-C5",
        }
    if hard_a + hard_b >= 8:
        return {
            "pair": sorted([a, b]),
            "why": "At least one family already records repeated hard-kill classes (circular / world-blind / lossy / restatement).",
            "screen": "FAIL",
            "constraint": "C5",
        }
    return {
        "pair": sorted([a, b]),
        "why": "No recorded depends_on / family_secondary co-occurrence; screen is a constraint template, not a launch license.",
        "screen": "PASS" if lean else "FAIL",
        "constraint": "C3" if lean else "C4",
    }


def t4_pairs(curated, families):
    observed = observed_family_pairs(curated, families)
    all_pairs = [tuple(sorted(p)) for p in itertools.combinations(families, 2)]
    never = [p for p in all_pairs if p not in observed]
    fam_killed = {f: Counter() for f in families}
    late_fams = set()
    for rec in curated:
        fam_killed[rec.get("family") or "OTHER"][rec.get("failure_class") or "NOT_APPLICABLE"] += (
            1 if rec.get("outcome") == "KILLED" else 0
        )
        if (rec.get("path") or "").startswith("experiments/tfpt-discovery/") and any(
            n >= 600 for n in round_nums(rec.get("round"))
        ):
            late_fams.add(rec.get("family"))
    ranked = []
    for a, b in never:
        early_late = (a in EARLY_STACK and b in late_fams) or (
            b in EARLY_STACK and a in late_fams
        )
        row = screen_pair(a, b, fam_killed)
        row["_early_late"] = bool(early_late)
        ranked.append(row)
    ranked.sort(
        key=lambda r: (
            0 if r["_early_late"] else 1,
            0 if r["screen"] == "PASS" else 1,
            r["pair"],
        )
    )
    top = []
    for row in ranked[:8]:
        top.append({k: row[k] for k in ("pair", "why", "screen", "constraint")})
    return {
        "family_count": len(families),
        "observed_pairs": len(observed),
        "never_tried_count": len(never),
        "pairs": [list(p) for p in never],
        "top_8": top,
        "early_x_late_untried": [
            list(r["pair"])
            for r in ranked
            if r["_early_late"]
        ],
    }


def t5_conflicts(curated):
    by_stem = defaultdict(list)
    by_led = defaultdict(list)
    for rec in curated:
        path = rec.get("path") or ""
        stem = object_stem(path)
        # Paper clauses are distinct assertions, not the source document's
        # filename stem. Still compare repeated claims and shared ledger IDs.
        if rec.get("role") == "paper_claim":
            stem = path
        # Campaign documentation is not the same mathematical object merely
        # because both files are called README/PROOF. Keep real ledger links.
        if rec.get("role") == "external_research_group" or stem.lower() in {
            "readme", "proof", "contract", "next_gate"
        }:
            stem = os.path.join(os.path.dirname(path), stem)
        by_stem[stem].append(rec)
        for lid in rec.get("ledger_ids") or []:
            by_led[lid].append(rec)

    items = []
    seen_paths = set()

    def emit(name, family, recs, recon):
        key = tuple(sorted(r.get("path") for r in recs))
        if key in seen_paths:
            return
        # Reconciled splits stay in fragments as history; T5 keeps only genuine review items.
        if recs and all(r.get("reconciled") for r in recs) and not any(
            r.get("needs_review") for r in recs
        ):
            return
        if recs and not any(r.get("needs_review") for r in recs):
            live = [r for r in recs if not r.get("superseded_by")]
            if len(live) < 2 or len({r.get("outcome") for r in live}) < 2:
                return
        seen_paths.add(key)
        items.append(
            {
                "object": name,
                "family": family,
                "records": [
                    {
                        "round": r.get("round") or "",
                        "path": r.get("path") or "",
                        "outcome": r.get("outcome") or "",
                        "verdict": clip(r.get("solved") or r.get("result_verdict") or "", 160),
                    }
                    for r in sorted(recs, key=lambda x: (first_round(x), x.get("path") or ""))
                ],
                "reconciliation": recon,
            }
        )

    for stem, recs in sorted(by_stem.items()):
        if len(recs) < 2:
            continue
        outcomes = {r.get("outcome") for r in recs}
        if len(outcomes) < 2:
            continue
        emit(
            stem,
            recs[0].get("family") or "",
            recs,
            "Outcomes differ across records for the same object; distinguish theorem content, companions, and status grade.",
        )
    for lid, recs in sorted(by_led.items()):
        if len(recs) < 2:
            continue
        outcomes = {r.get("outcome") for r in recs}
        if len(outcomes) < 2:
            continue
        emit(
            lid,
            recs[0].get("family") or "",
            recs,
            "Records share ledger id %s with different outcomes; ledger wins on status grade." % lid,
        )

    v1017 = [
        r
        for r in curated
        if vn_of(r.get("path")) == 1017
        or "kernel_loewner" in (r.get("path") or "")
        or any("KERNEL_LOEWNER" in x for x in (r.get("ledger_ids") or []))
    ]
    if v1017:
        emit(
            "v1017_kernel_loewner",
            "WEIL_POSITIVITY_WINDOWS",
            v1017,
            (
                "Catalog outcomes for the L=0.3 floor are CERTIFIED / [C]; "
                "rh/paper/rh_program.tex:359 is a theorem environment while "
                "ledger PRIME.RDAGGER.KERNEL_LOEWNER.01 is Numerical/certified, not [E]. "
                "r496 compact-tail at L=0.8 is KILLED (method no-go)."
            ),
        )
    return items


def open_center(rec):
    blob = " ".join(
        [
            rec.get("path") or "",
            rec.get("question") or "",
            rec.get("round") or "",
        ]
    ).lower()
    for hint, name, constraint in OPEN_CENTER_HINTS:
        if hint in blob:
            return name, constraint
    return None, ""


def t6_paths(curated, indexes):
    opens = [
        r
        for r in curated
        if r.get("outcome") == "OPEN"
        and r.get("rh_relevance") in ("LOAD_BEARING_OPEN", "EQUIVALENCE")
    ]
    scored = []
    for rec in opens:
        deps = []
        seen = set()
        for tok in rec.get("depends_on") or []:
            for hit in resolve_dep(tok, indexes):
                if hit.get("path") in seen or hit.get("path") == rec.get("path"):
                    continue
                if hit.get("outcome") not in ALIVE_OUTCOMES:
                    continue
                seen.add(hit.get("path"))
                deps.append(hit)
        deps = sorted(deps, key=lambda r: (first_round(r), r.get("path") or ""))[:4]
        name, constraint = open_center(rec)
        rel = rec.get("rh_relevance")
        assessment = "RH-EQUIVALENT" if rel == "EQUIVALENCE" else "RH-STRONG"
        scored.append(
            {
                "name": name or clip((rec.get("family") or "") + " " + object_stem(rec.get("path")), 60),
                "chain": [member(d) for d in deps] + [member(rec)],
                "new_theorem": clip(rec.get("question") or "", 140),
                "loss_free": clip(rec.get("reusable") or "", 120),
                "assessment": assessment,
                "assessment_why": (
                    "Catalog marks this as an equivalence packet."
                    if rel == "EQUIVALENCE"
                    else "Catalog marks this as a load-bearing open edge, not a new independent mechanism."
                ),
                "smallest_test": "Re-run the named probe; kill on a certified no-go or a failed source reconstruction.",
                "killed_by": constraint or "C5",
                "why_killed": (
                    "This is a declared open center, so it is not an independent path."
                    if constraint
                    else "Open edge only; no certified independent route is recorded."
                ),
                "_n_deps": len(deps),
                "_round": first_round(rec),
                "_path": rec.get("path") or "",
            }
        )
    scored.sort(key=lambda r: (-r["_n_deps"], r["_round"], r["_path"]))
    misses = []
    seen_names = set()
    for row in scored:
        if row["name"] in seen_names:
            continue
        seen_names.add(row["name"])
        misses.append({k: row[k] for k in row if not k.startswith("_")})
        if len(misses) >= 6:
            break
    return {
        "verdict": (
            "No independent path found. Nearest exact routes are recorded open centers "
            "or unfinished edges, not new mechanisms."
        ),
        "surviving_candidates": [],
        "nearest_misses": misses,
    }


def t7_lean(curated):
    formal = [
        r
        for r in curated
        if r.get("kind") == "FORMALIZATION" and (r.get("path") or "").endswith(".lean")
    ]
    proved = [r for r in formal if r.get("outcome") == "PROVED"]
    holes = [
        r
        for r in formal
        if r.get("outcome") in ("OPEN",) or r.get("rh_relevance") in ("LOAD_BEARING_OPEN", "EQUIVALENCE")
    ]
    bricks = []
    for i, rec in enumerate(sorted(proved, key=lambda r: (first_round(r), r.get("path") or ""))[:3], 1):
        bricks.append(
            {
                "rank": i,
                "name": object_stem(rec.get("path")),
                "file": rec.get("path") or "",
                "effort": "M",
                "evidence": [rec.get("round") or ""],
                "purpose": clip(rec.get("question") or rec.get("solved") or "", 140),
            }
        )
    hole_rows = []
    for rec in sorted(holes, key=lambda r: (first_round(r), r.get("path") or ""))[:6]:
        hole_rows.append(
            {
                "name": object_stem(rec.get("path")),
                "file": rec.get("path") or "",
                "classification": (
                    "RH-EQUIVALENT"
                    if rec.get("rh_relevance") == "EQUIVALENCE"
                    else "RH-STRONG"
                ),
                "evidence": [rec.get("round") or ""],
            }
        )
    return {
        "classical_bricks": bricks,
        "rh_strength_holes": hole_rows,
        "note": "Deterministic extract from curated FORMALIZATION Lean records; not a hand ranking.",
    }


def band_for_vn(n):
    if 535 <= n <= 600:
        return "v535-v600"
    if 601 <= n <= 700:
        return "v601-v700"
    if 701 <= n <= 800:
        return "v701-v800"
    if 801 <= n <= 900:
        return "v801-v900"
    if 901 <= n <= 954:
        return "v901-v954"
    if 1017 <= n <= 1019:
        return "v1017-v1019"
    return None


def round_bands(curated):
    order = (
        "v535-v600",
        "v601-v700",
        "v701-v800",
        "v801-v900",
        "v901-v954",
        "v1017-v1019",
        "r600+ probes",
    )
    buckets = {name: [] for name in order}
    for rec in curated:
        path = rec.get("path") or ""
        n = vn_of(path)
        if n is not None:
            band = band_for_vn(n)
            if band:
                buckets[band].append(rec)
                continue
        if path.startswith("experiments/tfpt-discovery/") and any(
            x >= 600 for x in round_nums(rec.get("round"))
        ):
            buckets["r600+ probes"].append(rec)
    out = []
    for name in order:
        rows = buckets[name]
        fams = Counter(r.get("family") for r in rows)
        out.append(
            {
                "band": name,
                "curated_records": len(rows),
                "outcomes": count_field(rows, "outcome", OUTCOMES),
                "dominant_families": [
                    {"family": f, "count": c} for f, c in fams.most_common(4)
                ],
            }
        )
    return out


def build_report(catalog, taxonomy):
    records = catalog.get("records") or []
    families = list(taxonomy["families"])
    curated = [r for r in records if is_curated(r)]
    drafts = [r for r in records if not is_curated(r)]
    indexes = build_indexes(curated)
    used = depended_paths(curated, indexes)
    t1 = family_matrix(curated, families, all_rows=records)
    report = {
        "claim_boundary": CLAIM,
        "catalog": {
            "path": "rh/catalog/rh_semantic_catalog.json",
            "total_records_seen": len(records),
            "curated_records_used": len(curated),
            "draft_records_ignored": len(drafts),
            "filter": 'not rec.get("draft")',
        },
        "T1_matrix": t1,
        "T2_kill_roots": t2_kills(curated),
        "T3_orphan_foundations": t3_orphans(curated, used),
        "T4_never_tried": t4_pairs(curated, families),
        "T5_contradictions": t5_conflicts(curated),
        "T6_candidate_paths": t6_paths(curated, indexes),
        "T7_formalization_targets": t7_lean(curated),
        "meta": {
            "n_records": len(records),
            "n_curated": len(curated),
            "n_draft": len(drafts),
            "generated_from": {
                "catalog": "rh/catalog/rh_semantic_catalog.json",
                "inventory_generated": catalog.get("built_from_inventory_generated"),
                "catalog_generated": catalog.get("built_from_inventory_generated"),
                "fragments": (catalog.get("generated_from") or {}).get("fragments"),
            },
            "round_bands": round_bands(curated),
            "t1_scope": "T1 rows are curated; records_all / outcomes_all / failure_classes_all count all records including drafts.",
            "t2_t6_scope": "curated-only",
        },
    }
    return report


def _paths(items, key="path"):
    out = []
    if isinstance(items, list):
        for it in items:
            if isinstance(it, dict) and it.get(key):
                out.append(it[key])
            elif isinstance(it, dict) and it.get("members"):
                out.extend(_paths(it["members"]))
    return out


def diff_reports(old, new):
    def t1_map(rep):
        return {row["family"]: row for row in rep.get("T1_matrix") or []}

    o1, n1 = t1_map(old), t1_map(new)
    t1_changes = []
    for fam in n1:
        ov, nv = o1.get(fam, {}), n1[fam]
        if ov.get("records") != nv.get("records"):
            t1_changes.append(
                {
                    "family": fam,
                    "records_old": ov.get("records", 0),
                    "records_new": nv.get("records", 0),
                    "outcomes_old": ov.get("outcomes"),
                    "outcomes_new": nv.get("outcomes"),
                }
            )

    def root_map(rep):
        return {
            r["root_phrase"]: r
            for r in (rep.get("T2_kill_roots") or {}).get("by_recurring_root") or []
        }

    o2, n2 = root_map(old), root_map(new)
    new_clusters = []
    for phrase, row in n2.items():
        if phrase not in o2:
            new_clusters.append(
                {
                    "root_phrase": phrase,
                    "count": row["count"],
                    "sample_paths": [m["path"] for m in row["members"][:5]],
                }
            )
        elif row["count"] > o2[phrase]["count"]:
            old_paths = {m["path"] for m in o2[phrase]["members"]}
            added = [m["path"] for m in row["members"] if m["path"] not in old_paths]
            if added:
                new_clusters.append(
                    {
                        "root_phrase": phrase,
                        "count_old": o2[phrase]["count"],
                        "count_new": row["count"],
                        "new_paths": added[:8],
                    }
                )

    o3 = {(r.get("path"), r.get("round")) for r in (old.get("T3_orphan_foundations") or {}).get("ranked_top") or []}
    n3_rows = (new.get("T3_orphan_foundations") or {}).get("ranked_top") or []
    new_orphans = [r for r in n3_rows if (r.get("path"), r.get("round")) not in o3]
    e_orphans = (new.get("T3_orphan_foundations") or {}).get("v535_v954_E_orphans") or []

    o4 = {tuple(p) for p in (old.get("T4_never_tried") or {}).get("pairs") or []}
    n4 = [p for p in (new.get("T4_never_tried") or {}).get("pairs") or [] if tuple(p) not in o4]
    early_late = (new.get("T4_never_tried") or {}).get("early_x_late_untried") or []

    o5 = {c.get("object") for c in old.get("T5_contradictions") or []}
    n5 = [c for c in new.get("T5_contradictions") or [] if c.get("object") not in o5]

    o6 = [m.get("name") for m in (old.get("T6_candidate_paths") or {}).get("nearest_misses") or []]
    n6 = [m.get("name") for m in (new.get("T6_candidate_paths") or {}).get("nearest_misses") or []]

    top10 = []
    for row in e_orphans[:5]:
        top10.append(
            {
                "item": "T3 v535-v954 [E] orphan",
                "path": row["path"],
                "detail": row.get("solved"),
            }
        )
    for row in new_clusters[:3]:
        paths = row.get("new_paths") or row.get("sample_paths") or []
        top10.append(
            {
                "item": "T2 new/grown kill cluster: " + row["root_phrase"],
                "path": paths[0] if paths else "",
                "detail": "count %s" % (row.get("count_new") or row.get("count")),
            }
        )
    for pair in early_late[:2]:
        top10.append(
            {
                "item": "T4 early×late untried",
                "path": " × ".join(pair),
                "detail": "family pair never co-occurred",
            }
        )
    v1017 = next(
        (c for c in new.get("T5_contradictions") or [] if c.get("object") == "v1017_kernel_loewner"),
        None,
    )
    if v1017:
        top10.append(
            {
                "item": "T5 v1017 Kernel-Loewner status grade",
                "path": "verification/v1017_kernel_loewner_positivity.py",
                "detail": v1017.get("reconciliation"),
            }
        )
    return {
        "claim_boundary": CLAIM,
        "old": old.get("catalog"),
        "new": new.get("catalog"),
        "counts": {
            "T1_families": [len(old.get("T1_matrix") or []), len(new.get("T1_matrix") or [])],
            "T2_killed": [
                (old.get("T2_kill_roots") or {}).get("killed_total"),
                (new.get("T2_kill_roots") or {}).get("killed_total"),
            ],
            "T2_root_clusters": [
                len((old.get("T2_kill_roots") or {}).get("by_recurring_root") or []),
                len((new.get("T2_kill_roots") or {}).get("by_recurring_root") or []),
            ],
            "T3_eligible": [
                (old.get("T3_orphan_foundations") or {}).get("eligible_total"),
                (new.get("T3_orphan_foundations") or {}).get("eligible_total"),
            ],
            "T3_ranked": [
                len((old.get("T3_orphan_foundations") or {}).get("ranked_top") or []),
                len((new.get("T3_orphan_foundations") or {}).get("ranked_top") or []),
            ],
            "T4_never_tried": [
                (old.get("T4_never_tried") or {}).get("never_tried_count"),
                (new.get("T4_never_tried") or {}).get("never_tried_count"),
            ],
            "T5_conflicts": [
                len(old.get("T5_contradictions") or []),
                len(new.get("T5_contradictions") or []),
            ],
            "T6_nearest_misses": [
                len((old.get("T6_candidate_paths") or {}).get("nearest_misses") or []),
                len((new.get("T6_candidate_paths") or {}).get("nearest_misses") or []),
            ],
        },
        "T1": {"record_count_changes": t1_changes},
        "T2": {"new_or_grown_clusters": new_clusters},
        "T3": {
            "new_ranked_orphans": new_orphans,
            "v535_v954_E_orphans": e_orphans,
        },
        "T4": {
            "new_never_tried_pairs": n4,
            "early_x_late_untried": early_late,
            "observed_pairs": [
                (old.get("T4_never_tried") or {}).get("observed_pairs"),
                (new.get("T4_never_tried") or {}).get("observed_pairs"),
            ],
        },
        "T5": {"new_conflicts": n5},
        "T6": {"old_names": o6, "new_names": n6, "order_changed": o6 != n6},
        "top_10": top10[:10],
        "round_bands": (new.get("meta") or {}).get("round_bands"),
    }


def print_diff(diff):
    print("PATHS DIFF old→new counts:")
    for k, pair in (diff.get("counts") or {}).items():
        print("  %s: %s → %s" % (k, pair[0], pair[1]))
    print("T1 family record changes:")
    for row in (diff.get("T1") or {}).get("record_count_changes") or []:
        print("  %s %s → %s" % (row["family"], row["records_old"], row["records_new"]))
    print("T2 new/grown clusters: %d" % len((diff.get("T2") or {}).get("new_or_grown_clusters") or []))
    print(
        "T3 new ranked orphans: %d; v535-v954 [E] orphans: %d"
        % (
            len((diff.get("T3") or {}).get("new_ranked_orphans") or []),
            len((diff.get("T3") or {}).get("v535_v954_E_orphans") or []),
        )
    )
    print(
        "T4 new never-tried: %d; early×late: %d"
        % (
            len((diff.get("T4") or {}).get("new_never_tried_pairs") or []),
            len((diff.get("T4") or {}).get("early_x_late_untried") or []),
        )
    )
    print("T5 new conflicts: %d" % len((diff.get("T5") or {}).get("new_conflicts") or []))
    t6 = diff.get("T6") or {}
    print("T6 names old %s" % t6.get("old_names"))
    print("T6 names new %s" % t6.get("new_names"))
    print("top_10:")
    for i, item in enumerate(diff.get("top_10") or [], 1):
        print("  %d. %s | %s | %s" % (i, item.get("item"), item.get("path"), clip(item.get("detail") or "", 100)))
    print("round_bands:")
    for band in diff.get("round_bands") or []:
        dom = ", ".join("%s %d" % (x["family"], x["count"]) for x in band.get("dominant_families") or [])
        print("  %s curated=%d outcomes=%s | %s" % (band["band"], band["curated_records"], band["outcomes"], dom))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Rebuild RH catalog path tables T1–T6.")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--no-diff", action="store_true")
    args = parser.parse_args(argv)

    catalog = load_json(CATALOG_PATH)
    taxonomy = load_json(TAXONOMY_PATH)
    report = build_report(catalog, taxonomy)
    write_json(OUT_REPORT, report)

    diff = None
    if not args.no_diff and os.path.isfile(SNAPSHOT_728):
        old = load_json(SNAPSHOT_728)
        diff = diff_reports(old, report)
        write_json(OUT_DIFF, diff)

    if not args.quiet:
        meta = report["meta"]
        print(
            "WROTE rh/catalog/analysis/paths_report.json (%d records, %d curated, %d draft)"
            % (meta["n_records"], meta["n_curated"], meta["n_draft"])
        )
        if diff is not None:
            print("WROTE rh/catalog/analysis/paths_report_diff.json")
            print_diff(diff)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
