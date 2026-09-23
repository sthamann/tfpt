#!/usr/bin/env python3
"""Build rh/catalog/viewer/public/data/*.json from the semantic catalog.

Research documentation only. NO RH CLAIM.
stdlib + optional numpy (system or experiments/tfpt-discovery/.venv).
"""

from __future__ import annotations

import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CATALOG_DIR = REPO / "rh" / "catalog"
OUT_DIR = HERE / "public" / "data"

KIND_W = {
    "ATTACK": 1.30,
    "REDUCTION": 1.15,
    "FOUNDATION": 1.10,
    "CERTIFICATE": 1.40,
    "CONTROL": 0.95,
    "FORMALIZATION": 1.25,
    "EXTERNAL_AUDIT": 0.85,
    "DOCUMENTATION": 0.55,
    "TOOLING": 0.50,
    "OTHER": 0.40,
}
OUTCOME_W = {
    "PROVED": 2.20,
    "CERTIFIED": 2.00,
    "KILLED": 1.60,
    "MEASURED": 1.20,
    "OPEN": 1.05,
    "SEALED": 0.90,
    "INCONCLUSIVE": 0.80,
    "RESTATED": 0.55,
}

ROUND_TOKEN_RE = re.compile(r"r\d+[A-Z]?")
ROUND_NUM_RE = re.compile(r"r(\d+)")


def _try_numpy():
    try:
        import numpy as np  # type: ignore

        return np
    except ImportError:
        pass
    venv = REPO / "experiments" / "tfpt-discovery" / ".venv"
    if venv.is_dir():
        for site in (venv / "lib").glob("python*/site-packages"):
            sys.path.insert(0, str(site))
        try:
            import numpy as np  # type: ignore

            return np
        except ImportError:
            return None
    return None


def load_json(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def dump_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, separators=(",", ":"))


def parse_round_num(round_s: str) -> int:
    if not round_s:
        return -1
    m = ROUND_NUM_RE.search(round_s)
    return int(m.group(1)) if m else -1


def node_score(rec: dict) -> float:
    kw = KIND_W.get(rec.get("kind") or "", 0.6)
    ow = OUTCOME_W.get(rec.get("outcome") or "", 0.7)
    score = kw * ow
    if rec.get("rh_relevance") == "LOAD_BEARING_OPEN":
        score *= 1.15
    if rec.get("draft"):
        score *= 0.72
    return round(score, 4)


def record_fields(rec: dict, abs_path: str) -> dict:
    return {
        "id": rec["path"],
        "path": rec["path"],
        "abs_path": abs_path,
        "round": rec.get("round") or "",
        "round_num": parse_round_num(rec.get("round") or ""),
        "role": rec.get("role") or "",
        "ledger_ids": list(rec.get("ledger_ids") or []),
        "kind": rec.get("kind") or "OTHER",
        "family": rec.get("family") or "OTHER",
        "family_secondary": list(rec.get("family_secondary") or []),
        "outcome": rec.get("outcome") or "OPEN",
        "failure_class": rec.get("failure_class") or "NOT_APPLICABLE",
        "rh_relevance": rec.get("rh_relevance") or "UNRELATED",
        "question": rec.get("question") or "",
        "mechanism": rec.get("mechanism") or "",
        "result_verdict": rec.get("result_verdict") or "",
        "solved": rec.get("solved") or "",
        "failed_because": rec.get("failed_because") or "",
        "reusable": rec.get("reusable") or "",
        "depends_on": list(rec.get("depends_on") or []),
        "artifacts": rec.get("artifacts") or {},
        "confidence": rec.get("confidence") or "low",
        "draft": bool(rec.get("draft")),
        "needs_review": bool(rec.get("needs_review")),
        "reconciled": rec.get("reconciled") if "reconciled" in rec else None,
        "superseded_by": rec.get("superseded_by") or None,
        "readme_lines": rec.get("readme_lines") or "",
        "status_raw": rec.get("status_raw") or "",
        "score": node_score(rec),
    }


def resolve_token(
    token: str,
    by_path: dict,
    by_basename: dict,
    by_round: dict,
    by_round_tok: dict,
    by_ledger: dict,
    by_contract: dict,
) -> list:
    if token in by_path:
        return [by_path[token]]
    if token in by_basename:
        return list(by_basename[token])
    ends = [p for p in by_path if p.endswith("/" + token) or p.endswith(token)]
    if ends:
        return [by_path[p] for p in ends]
    if token in by_round:
        return list(by_round[token])
    if token in by_round_tok:
        return list(by_round_tok[token])
    if token in by_ledger:
        return list(by_ledger[token])
    if token in by_contract:
        return list(by_contract[token])
    return []


def add_edge(edges: list, seen: set, src: str, tgt: str, etype: str) -> None:
    if not src or not tgt or src == tgt:
        return
    a, b = (src, tgt) if src < tgt else (tgt, src)
    key = (etype, a, b)
    if key in seen:
        return
    seen.add(key)
    edges.append({"source": src, "target": tgt, "type": etype})


def power_pca(np, X, k: int = 32, niter: int = 16):
    """Centered power-iteration PCA → (n, k)."""
    n, d = X.shape
    k = min(k, n, d)
    mean = X.mean(axis=0)
    residual = X - mean
    comps = []
    rng = np.random.default_rng(32)
    for _ in range(k):
        v = rng.standard_normal(d)
        nrm = float(np.linalg.norm(v))
        if nrm < 1e-15:
            break
        v = v / nrm
        for _it in range(niter):
            w = residual.T @ (residual @ v)
            nrm = float(np.linalg.norm(w))
            if nrm < 1e-15:
                break
            v = w / nrm
        comps.append(v)
        proj = residual @ v
        residual = residual - np.outer(proj, v)
    if not comps:
        return np.zeros((n, k), dtype=float)
    W = np.stack(comps, axis=1)
    return (X - mean) @ W


def cosine_top3(np, X, paths: list, thresh: float = 0.45):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms < 1e-12, 1.0, norms)
    U = X / norms
    S = U @ U.T
    n = S.shape[0]
    pairs = []
    for i in range(n):
        row = S[i]
        row[i] = -1.0
        idx = np.argpartition(row, -3)[-3:]
        idx = idx[np.argsort(row[idx])[::-1]]
        for j in idx:
            sim = float(row[j])
            if sim >= thresh:
                pairs.append((paths[i], paths[j], round(sim, 4)))
    return pairs


def count_matrix(rows: list, row_key: str, col_key: str, row_order: list, col_order: list):
    row_order = list(row_order)
    col_order = list(col_order)
    row_set = set(row_order)
    col_set = set(col_order)
    cells = {(r, c): 0 for r in row_order for c in col_order}
    for rec in rows:
        r = rec.get(row_key) or ""
        c = rec.get(col_key) or ""
        if r not in row_set:
            row_order.append(r)
            row_set.add(r)
            for col in col_order:
                cells[(r, col)] = 0
        if c not in col_set:
            col_order.append(c)
            col_set.add(c)
            for row in row_order:
                cells[(row, c)] = 0
        cells[(r, c)] = cells.get((r, c), 0) + 1
    return {
        "rows": row_order,
        "cols": col_order,
        "cells": [{"row": r, "col": c, "n": cells[(r, c)]} for r, c in cells],
    }


def main() -> int:
    catalog_path = CATALOG_DIR / "rh_semantic_catalog.json"
    paths_path = CATALOG_DIR / "analysis" / "paths_report.json"
    tax_path = CATALOG_DIR / "taxonomy.json"
    emb_path = CATALOG_DIR / "embeddings" / "catalog_embeddings.json"

    catalog = load_json(catalog_path)
    records = list(catalog.get("records") or [])
    taxonomy = load_json(tax_path) if tax_path.is_file() else {}
    paths_report = load_json(paths_path) if paths_path.is_file() else {}

    nodes = []
    for rec in records:
        abs_path = str((REPO / rec["path"]).resolve()) if rec.get("path") else ""
        nodes.append(record_fields(rec, abs_path))

    by_path = {n["id"]: n["id"] for n in nodes}
    by_basename = defaultdict(list)
    by_round = defaultdict(list)
    by_round_tok = defaultdict(list)
    by_ledger = defaultdict(list)
    by_contract = defaultdict(list)
    for n in nodes:
        base = Path(n["path"]).name
        if base:
            by_basename[base].append(n["id"])
        if n["round"]:
            by_round[n["round"]].append(n["id"])
            for tok in ROUND_TOKEN_RE.findall(n["round"]):
                by_round_tok[tok].append(n["id"])
        for lid in n["ledger_ids"]:
            by_ledger[lid].append(n["id"])
            by_contract[lid].append(n["id"])

    edges = []
    seen = set()

    for n in nodes:
        for tok in n["depends_on"]:
            for tgt in resolve_token(
                tok, by_path, by_basename, by_round, by_round_tok, by_ledger, by_contract
            ):
                add_edge(edges, seen, n["id"], tgt, "DEPENDS")
        sup = n.get("superseded_by")
        if isinstance(sup, str) and sup:
            for tgt in resolve_token(
                sup, by_path, by_basename, by_round, by_round_tok, by_ledger, by_contract
            ):
                add_edge(edges, seen, n["id"], tgt, "SUPERSEDES")
        elif isinstance(sup, list):
            for tok in sup:
                for tgt in resolve_token(
                    tok, by_path, by_basename, by_round, by_round_tok, by_ledger, by_contract
                ):
                    add_edge(edges, seen, n["id"], tgt, "SUPERSEDES")

    for rid, members in by_round.items():
        if not rid or len(members) < 2:
            continue
        uniq = sorted(set(members))
        for i, a in enumerate(uniq):
            for b in uniq[i + 1 :]:
                add_edge(edges, seen, a, b, "SAME_ROUND")

    for lid, members in by_ledger.items():
        if len(members) < 2:
            continue
        uniq = sorted(set(members))
        for i, a in enumerate(uniq):
            for b in uniq[i + 1 :]:
                add_edge(edges, seen, a, b, "SHARED_LEDGER")

    by_family = defaultdict(list)
    for n in nodes:
        by_family[n["family"]].append(n)
    for fam, members in by_family.items():
        if len(members) < 2:
            continue
        hub = max(members, key=lambda x: (x["score"], x["id"]))
        for n in members:
            add_edge(edges, seen, n["id"], hub["id"], "FAMILY")

    np = _try_numpy()
    semantic = False
    vectors_payload = None
    if emb_path.is_file() and np is not None:
        emb = load_json(emb_path)
        emb_recs = list(emb.get("records") or [])
        path_to_vec = {}
        dim = int(emb.get("dim") or 0)
        for er in emb_recs:
            p = er.get("path")
            v = er.get("vector")
            if p and v and p in by_path:
                path_to_vec[p] = v
                if not dim:
                    dim = len(v)
        aligned_paths = [n["id"] for n in nodes if n["id"] in path_to_vec]
        if aligned_paths and dim:
            X = np.asarray([path_to_vec[p] for p in aligned_paths], dtype=np.float64)
            pairs = cosine_top3(np, X, aligned_paths, thresh=0.45)
            for a, b, sim in pairs:
                if a > b:
                    continue
                key = ("SEMANTIC", a, b)
                if key in seen:
                    continue
                seen.add(key)
                edges.append(
                    {"source": a, "target": b, "type": "SEMANTIC", "weight": sim}
                )
            reduced = power_pca(np, X, k=32, niter=16)
            # L2-normalise 32-d rows for browser cosine
            rn = np.linalg.norm(reduced, axis=1, keepdims=True)
            rn = np.where(rn < 1e-12, 1.0, rn)
            reduced = reduced / rn
            vectors_payload = {
                "dim": int(reduced.shape[1]),
                "ids": aligned_paths,
                "vectors": [
                    [round(float(x), 6) for x in row] for row in reduced.tolist()
                ],
            }
            semantic = True
    elif emb_path.is_file() and np is None:
        print("WARN: embeddings present but numpy missing — SEMANTIC edges skipped", file=sys.stderr)

    n_curated = sum(1 for n in nodes if not n["draft"])
    n_draft = sum(1 for n in nodes if n["draft"])
    edge_counts = Counter(e["type"] for e in edges)
    generated = catalog.get("generated") or catalog.get("built_from_inventory_generated")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    families = list((taxonomy.get("families") or {}).keys()) or sorted(by_family)
    outcomes = list((taxonomy.get("outcomes") or {}).keys()) or sorted(
        {n["outcome"] for n in nodes}
    )
    kinds = list((taxonomy.get("kinds") or {}).keys()) or sorted(
        {n["kind"] for n in nodes}
    )
    failures = list((taxonomy.get("failure_classes") or {}).keys()) or sorted(
        {n["failure_class"] for n in nodes}
    )
    relevances = list((taxonomy.get("rh_relevances") or {}).keys()) or sorted(
        {n["rh_relevance"] for n in nodes}
    )

    meta = {
        "claim_boundary": catalog.get("claim_boundary")
        or "Research documentation. NO RH CLAIM.",
        "generated": stamp,
        "catalog_generated": generated,
        "n_nodes": len(nodes),
        "n_edges": len(edges),
        "edges_by_type": dict(edge_counts),
        "n_curated": n_curated,
        "n_draft": n_draft,
        "semantic": semantic,
        "n_vectors": len(vectors_payload["ids"]) if vectors_payload else 0,
        "taxonomy": {
            "families": taxonomy.get("families") or {},
            "kinds": taxonomy.get("kinds") or {},
            "outcomes": taxonomy.get("outcomes") or {},
            "failure_classes": taxonomy.get("failure_classes") or {},
            "rh_relevances": taxonomy.get("rh_relevances") or {},
        },
        "orders": {
            "families": families,
            "outcomes": outcomes,
            "kinds": kinds,
            "failure_classes": failures,
            "rh_relevances": relevances,
        },
    }

    graph = {"meta": meta, "nodes": nodes, "edges": edges}

    fam_out = count_matrix(nodes, "family", "outcome", list(families), list(outcomes))
    fam_fail = count_matrix(
        nodes, "family", "failure_class", list(families), list(failures)
    )
    kind_out = count_matrix(nodes, "kind", "outcome", list(kinds), list(outcomes))
    curated_vs_draft = {
        "curated": n_curated,
        "draft": n_draft,
        "needs_review": sum(1 for n in nodes if n["needs_review"]),
    }
    t1 = paths_report.get("T1_matrix") or []

    matrix = {
        "meta": {"generated": stamp, "n_nodes": len(nodes)},
        "family_x_outcome": fam_out,
        "family_x_failure_class": fam_fail,
        "kind_x_outcome": kind_out,
        "curated_vs_draft": curated_vs_draft,
        "t1": t1,
    }

    items = []
    for n in nodes:
        items.append(
            {
                "id": n["id"],
                "round": n["round"],
                "round_num": n["round_num"],
                "family": n["family"],
                "outcome": n["outcome"],
                "kind": n["kind"],
                "draft": n["draft"],
                "score": n["score"],
            }
        )
    numbered = [it["round_num"] for it in items if it["round_num"] >= 0]
    timeline = {
        "items": items,
        "min_round": min(numbered) if numbered else 0,
        "max_round": max(numbered) if numbered else 0,
        "n_unnumbered": sum(1 for it in items if it["round_num"] < 0),
    }

    t2 = paths_report.get("T2_kill_roots") or {}
    kills = {
        "killed_total": t2.get("killed_total"),
        "by_failure_class": t2.get("by_failure_class") or [],
        "clusters": t2.get("by_recurring_root") or [],
    }

    t3 = paths_report.get("T3_orphan_foundations") or {}
    orphans = {
        "eligible_total": t3.get("eligible_total"),
        "ranked": t3.get("ranked_top") or [],
    }

    t4 = paths_report.get("T4_never_tried") or {}
    screen_map = {}
    for row in t4.get("top_8") or []:
        pair = row.get("pair") or []
        if len(pair) == 2:
            key = tuple(sorted(pair))
            screen_map[key] = row
    pair_rows = []
    for pair in t4.get("pairs") or []:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            continue
        key = tuple(sorted(pair))
        extra = screen_map.get(key) or {}
        pair_rows.append(
            {
                "a": pair[0],
                "b": pair[1],
                "screen": extra.get("screen") or "UNTRIED",
                "why": extra.get("why") or "",
                "constraint": extra.get("constraint") or "",
            }
        )
    pairs = {
        "family_count": t4.get("family_count"),
        "observed_pairs": t4.get("observed_pairs"),
        "never_tried_count": t4.get("never_tried_count"),
        "pairs": pair_rows,
        "top_8": t4.get("top_8") or [],
    }

    conflicts = {"items": paths_report.get("T5_contradictions") or []}

    t6 = paths_report.get("T6_candidate_paths") or {}
    misses = {
        "verdict": t6.get("verdict") or "",
        "surviving_candidates": t6.get("surviving_candidates") or [],
        "nearest_misses": t6.get("nearest_misses") or [],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump_json(OUT_DIR / "graph.json", graph)
    dump_json(OUT_DIR / "matrix.json", matrix)
    dump_json(OUT_DIR / "timeline.json", timeline)
    dump_json(OUT_DIR / "kills.json", kills)
    dump_json(OUT_DIR / "orphans.json", orphans)
    dump_json(OUT_DIR / "pairs.json", pairs)
    dump_json(OUT_DIR / "conflicts.json", conflicts)
    dump_json(OUT_DIR / "misses.json", misses)
    if vectors_payload is not None:
        dump_json(OUT_DIR / "vectors.json", vectors_payload)
    else:
        dump_json(OUT_DIR / "vectors.json", {"dim": 0, "ids": [], "vectors": []})

    print(
        "nodes={n} edges={e} curated={c} draft={d} semantic={s}".format(
            n=len(nodes),
            e=len(edges),
            c=n_curated,
            d=n_draft,
            s=str(semantic).lower(),
        )
    )
    print("edges_by_type", dict(edge_counts))
    print("wrote", OUT_DIR)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
