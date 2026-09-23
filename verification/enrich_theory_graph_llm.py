#!/usr/bin/env python3
"""LLM enrichment for the TFPT theory graph (Moonshot/Kimi, OpenAI-compatible).

Two subcommands over verification/theory_graph.json:

    backfill-contracts   judge the verdict_class=unknown contracts from their
                         folder artefacts and write <folder>/contract_index.json
                         (source="llm_backfill"; existing files are NEVER
                         overwritten)
    verify-findings      review all extracted findings in batches; writes
                         verification/findings_overrides.json (keep/correct/drop)

API HYGIENE (hard rules):
  * the key is read from the MOONSHOT_API_KEY environment variable ONLY --
    never written to any file, log, contract_index.json or printed output
  * endpoint https://api.moonshot.ai/v1/chat/completions, model kimi-k3,
    thinking_effort low, timeout 120 s, backoff 5/15/45 s on 429/5xx

--dry-run prints the prompts without any API call; --limit N caps the work
items.  stdlib only -- runnable without the venv.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERIF = ROOT / "verification"
CONTRACTS_DIR = ROOT / "experiments" / "theory-contracts"
GRAPH_PATH = VERIF / "theory_graph.json"
OVERRIDES_PATH = VERIF / "findings_overrides.json"

sys.path.insert(0, str(VERIF))
import build_theory_graph as btg  # reuse CLAIM_TOKEN_RE / clip / candidates

API_BASE = "https://api.moonshot.ai/v1"
MODEL = "kimi-k3"
TIMEOUT_S = 120
BACKOFF_S = (5, 15, 45)
MAX_FILE_CHARS = 12000
MAX_JSON_CHARS = 8000

VERDICT_ENUM = ["pass", "partial", "fail", "refuted", "killed", "candidate",
                "consistent", "tension", "other", "unknown"]
REL_TYPES = {"contradicts", "supports", "followup_of", "references"}
GENERIC_VERDICT_ENUM = ["PASS", "PARTIAL", "FAIL", "REFUTED", "NO_CANDIDATE",
                        "UNKNOWN"]

USAGE = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0,
         "calls": 0, "failed_calls": 0}


# --------------------------------------------------------------------------
# API plumbing (key hygiene: env only, never logged)
# --------------------------------------------------------------------------

def chat_complete(messages, json_mode=True, timeout=TIMEOUT_S):
    """One chat completion with backoff.  Returns (content, ok)."""
    key = os.environ.get("MOONSHOT_API_KEY")
    if not key:
        sys.stderr.write("MOONSHOT_API_KEY not set -- aborting\n")
        sys.exit(2)
    body = {
        "model": MODEL,
        "messages": messages,
        # kimi-k3 allows only temperature=1 -- omit the field entirely
        "thinking_effort": "low",
    }
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    for attempt in range(len(BACKOFF_S) + 1):
        req = urllib.request.Request(
            API_BASE + "/chat/completions",
            data=json.dumps(body).encode(),
            headers={"Authorization": "Bearer " + key,
                     "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode())
            usage = payload.get("usage") or {}
            for k in USAGE:
                if k in usage:
                    USAGE[k] += int(usage[k])
            USAGE["calls"] += 1
            choice = (payload.get("choices") or [{}])[0]
            return (choice.get("message") or {}).get("content") or "", True
        except urllib.error.HTTPError as exc:
            # 400 on unknown params -> drop the optional ones once, retry
            if exc.code == 400 and (json_mode or "thinking_effort" in body):
                body.pop("response_format", None)
                body.pop("thinking_effort", None)
                json_mode = False
                continue
            if exc.code in (429,) or 500 <= exc.code < 600:
                if attempt < len(BACKOFF_S):
                    time.sleep(BACKOFF_S[attempt])
                    continue
                sys.stderr.write(f"API HTTP {exc.code} after retries -- item skipped\n")
                USAGE["failed_calls"] += 1
                return "", False
            sys.stderr.write(f"API HTTP {exc.code} -- item skipped\n")
            USAGE["failed_calls"] += 1
            return "", False
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if attempt < len(BACKOFF_S):
                time.sleep(BACKOFF_S[attempt])
                continue
            sys.stderr.write(f"API network error ({type(exc).__name__}) -- item skipped\n")
            USAGE["failed_calls"] += 1
            return "", False
    return "", False


def extract_json_block(text: str):
    """Robustly parse the first {...} block of the answer."""
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def read_clip(path: Path, limit: int):
    """Read a text file clipped to limit chars, truncation marked."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    if len(text) > limit:
        text = text[:limit] + f"\n[... abgeschnitten bei {limit} Zeichen]"
    return text


# --------------------------------------------------------------------------
# backfill-contracts
# --------------------------------------------------------------------------

BACKFILL_SYSTEM = """\
Du analysierst einen "theory contract" aus dem TFPT-Forschungsrepo \
(firewalled, präregistrierte mathematische Prüfung) und extrahierst streng \
maschinenlesbare Metadaten.
Harte Regeln:
1. Antworte NUR mit einem JSON-Objekt im geforderten Schema.
2. Rate NIEMALS ein Ergebnis. Steht im Text kein ausgewertetes Ergebnis \
(nur Präregistrierung/Plan/Manifest), ist verdict_class "unknown".
3. claims_tested darf NUR IDs aus der mitgelieferten Kandidatenliste \
enthalten (sonst weglassen).
4. relations nur gegen mitgelieferte Contract-Slugs; nur wenn der Text die \
andere Arbeit klar benennt.
5. gates nur aus T1..T8, und nur wenn der Text sie explizit adressiert.
6. kills: kurze Hypothesen-Strings, nur wenn der Text sie klar widerlegt.
7. summary_de: 2-3 ehrliche Sätze (was getestet, Ergebnis, warum)."""

BACKFILL_SCHEMA = """\
{"verdict_raw": "<Kurz-Enum oder null>",
 "verdict_class": "pass|partial|fail|refuted|killed|candidate|consistent|tension|other|unknown",
 "summary_de": "2-3 Sätze",
 "claims_tested": ["<nur IDs aus Kandidatenliste>"],
 "relations": [{"type": "contradicts|supports|followup_of|references",
                "target": "<contract-slug>"}],
 "gates": ["T1", "..."],
 "kills": ["<Hypothese kurz>"],
 "question": "<1 Satz>"}"""


def detect_verdict_enum(readme_text):
    if not readme_text:
        return None
    m = re.search(r"verdict[- ]?enum(.*?)(\n## |\Z)", readme_text, re.I | re.S)
    if not m:
        return None
    toks = sorted(set(re.findall(r"`([A-Z][A-Z0-9_]{2,})`", m.group(1))))
    return toks or None


def checker_docstring(folder: Path, checker_name):
    if not checker_name:
        return None
    path = folder / checker_name
    if not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = re.search(r'^[ \t]*("""|\'\'\')(.*?)\1', text, re.S | re.M)
    if not m:
        return None
    return btg.clip(" ".join(m.group(2).split()), 2000)


def backfill_one(name, node_attrs, claim_ids, slugs, dry_run):
    """Returns (contract_index_dict, called_api)."""
    folder = CONTRACTS_DIR / name
    readme = read_clip(folder / "README.md", MAX_FILE_CHARS)
    results = read_clip(folder / "RESULTS.md", MAX_FILE_CHARS)
    einfach = read_clip(folder / "EINFACH_ERKLAERT.md", MAX_FILE_CHARS)
    # older contracts keep results under these names
    test_results = read_clip(folder / "TEST_RESULTS.md", MAX_FILE_CHARS)
    round_status = read_clip(folder / "ROUND_STATUS.md", MAX_FILE_CHARS)
    docstring = checker_docstring(folder, node_attrs.get("checker"))
    # run artefacts as evidence (truncated), first parseable candidate
    artefact = None
    for cand in btg.contract_json_candidates(folder):
        data = btg.read_json_trailing_stripped(cand)
        if isinstance(data, dict):
            artefact = (cand.name, btg.clip(json.dumps(data, ensure_ascii=False),
                                            MAX_JSON_CHARS))
            break
    has_evidence = any([results, test_results, round_status, artefact])
    if not has_evidence:
        # honest: no result files at all -> unknown, no API call, no guessing
        return {
            "contract": name,
            "date": node_attrs.get("date") or "",
            "question": node_attrs.get("question") or name,
            "verdict": "UNKNOWN",
            "verdict_enum": detect_verdict_enum(readme) or GENERIC_VERDICT_ENUM,
            "claims_tested": [],
            "gates": [],
            "kills": [],
            "checker": node_attrs.get("checker") or "",
            "firewall": "experiments",
            "source": "llm_backfill",
            "model": MODEL,
            "backfill_date": date.today().isoformat(),
            "summary_de": "kein Ergebnis abgelegt (keine RESULTS.md und kein "
                          "maschinell lesbares Run-Artefakt im Ordner)",
        }, False

    # candidate claim ids: regex + suffix resolution over all texts
    texts = [t for t in (readme, results, einfach, test_results,
                       round_status, docstring) if t]
    resolved, _ambiguous = btg.extract_claim_tokens(texts, claim_ids, cap=50)
    candidates = sorted({cid for cid, _from in resolved})

    parts = [
        f"CONTRACT: {name}",
        f"README-TITEL: {node_attrs.get('question') or name}",
        f"KANDIDATEN-CLAIM-IDS: {json.dumps(candidates)}",
        f"BEKANNTE CONTRACT-SLUGS: {json.dumps(sorted(slugs))}",
        "GATES: T1..T8",
        "",
    ]
    for label, text in (("README.md", readme), ("RESULTS.md", results),
                        ("TEST_RESULTS.md", test_results),
                        ("ROUND_STATUS.md", round_status),
                        ("EINFACH_ERKLAERT.md", einfach)):
        if text:
            parts.append(f"=== {label} ===\n{text}\n")
    if artefact:
        parts.append(f"=== Run-Artefakt {artefact[0]} (Ausschnitt) ===\n{artefact[1]}\n")
    if docstring:
        parts.append(f"=== Checker-Docstring ===\n{docstring}\n")
    parts.append("Antwort-JSON-Schema:\n" + BACKFILL_SCHEMA)
    messages = [
        {"role": "system", "content": BACKFILL_SYSTEM},
        {"role": "user", "content": "\n".join(parts)},
    ]
    if dry_run:
        print("=" * 70)
        print("DRY-RUN backfill:", name)
        print("--- system ---")
        print(BACKFILL_SYSTEM)
        print("--- user (gekürzt auf 4000 Zeichen) ---")
        print("\n".join(parts)[:4000])
        return None, False

    content, ok = chat_complete(messages, timeout=240)
    if not ok:
        return None, True
    obj = extract_json_block(content)
    if not isinstance(obj, dict):
        sys.stderr.write(f"{name}: no JSON in answer -- skipped\n")
        return None, True
    # validation: enum membership + closed-world claims/relations
    vc = obj.get("verdict_class")
    if vc not in VERDICT_ENUM:
        sys.stderr.write(f"{name}: bad verdict_class {vc!r} -- skipped\n")
        return None, True
    claims = [c for c in (obj.get("claims_tested") or []) if c in candidates]
    relations = [
        {"type": r.get("type"), "target": r.get("target")}
        for r in (obj.get("relations") or [])
        if isinstance(r, dict) and r.get("type") in REL_TYPES
        and r.get("target") in slugs and r.get("target") != name
    ]
    gates = [g for g in (obj.get("gates") or []) if g in {f"T{i}" for i in range(1, 9)}]
    kills = [btg.clip(str(k), 120) for k in (obj.get("kills") or [])][:10]
    verdict_raw = obj.get("verdict_raw")
    if vc == "unknown":
        verdict_raw = verdict_raw or "UNKNOWN"
    elif not verdict_raw:
        # the class IS the verdict when no separate raw token is given
        verdict_raw = vc.upper()
    return {
        "contract": name,
        "date": node_attrs.get("date") or "",
        "question": btg.clip(obj.get("question") or node_attrs.get("question") or name, 200),
        "verdict": str(verdict_raw),
        "verdict_enum": detect_verdict_enum(readme) or GENERIC_VERDICT_ENUM,
        "claims_tested": claims,
        "gates": gates,
        "kills": kills,
        "relations": relations,
        "checker": node_attrs.get("checker") or "",
        "firewall": "experiments",
        "source": "llm_backfill",
        "model": MODEL,
        "backfill_date": date.today().isoformat(),
        "summary_de": btg.clip(obj.get("summary_de") or "", 400),
        "verdict_class_llm": vc,
    }, True


def cmd_backfill(args, graph):
    nodes = {n["id"]: n for n in graph["nodes"]}
    claim_ids = {n["label"] for n in graph["nodes"] if n["type"] == "claim"}
    slugs = {n["label"] for n in graph["nodes"] if n["type"] == "contract"}
    unknowns = [
        n for n in graph["nodes"]
        if n["type"] == "contract" and n["attrs"].get("verdict_class") == "unknown"
    ]
    unknowns.sort(key=lambda n: n["label"])
    if args.limit:
        unknowns = unknowns[: args.limit]
    written = skipped = failed = no_call = 0
    for n in unknowns:
        name = n["label"]
        target = CONTRACTS_DIR / name / "contract_index.json"
        if target.is_file():
            print(f"{name}: contract_index.json exists -- skipped")
            skipped += 1
            continue
        rec, called_api = backfill_one(name, n["attrs"], claim_ids, slugs,
                                       args.dry_run)
        if args.dry_run:
            continue
        if rec is None:
            failed += 1
            continue
        no_call += 0 if called_api else 1
        target.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
        print(f"{name}: wrote contract_index.json "
              f"(verdict={rec['verdict']!r}, api={called_api})")
        written += 1
    print(f"backfill: written={written} skipped_existing={skipped} "
          f"failed={failed} honest_unknown_without_call={no_call}")


# --------------------------------------------------------------------------
# verify-findings
# --------------------------------------------------------------------------

FINDINGS_SYSTEM = """\
Du prüfst automatisch extrahierte "findings" (verdict-tragende Sätze) aus \
TFPT-Research-Contracts. Pro Item entscheidest du:
- "keep": echter Befund-Satz (das Contract berichtet hier ein eigenes Ergebnis).
- "correct": echter Befund, aber falsche Klasse -> kind korrigieren \
(refutes|no_go|supports|open).
- "drop": Fehltrigger -- Enum-Definition, reine Konditional-Spekulation ohne \
Befund ("würde widerlegen"), Zitat fremder Arbeit, Boilerplate/Firewall-Text.
Antworte NUR als JSON: {"results": [{"i": <idx>, "action": "keep|correct|drop", \
"kind": "<nur bei correct>"}]} -- für JEDES i der Anfrage genau einmal."""


def cmd_verify_findings(args, graph):
    items = []
    for n in graph["nodes"]:
        if n["type"] != "contract":
            continue
        a = n["attrs"]
        for f in a.get("findings") or []:
            key = "%s#%s" % (n["label"],
                             hashlib.sha1(f["text"].encode()).hexdigest()[:12])
            items.append({
                "key": key,
                "contract": n["label"],
                "question": a.get("question") or "",
                "section": f.get("section") or "",
                "kind": f.get("kind") or "",
                "text": f.get("text") or "",
            })
    items.sort(key=lambda x: x["key"])
    if args.limit:
        items = items[: args.limit]
    overrides = {}
    if OVERRIDES_PATH.is_file():
        try:
            old = json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
            overrides = {k: v for k, v in (old.get("overrides") or old).items()
                         if k != "meta" and isinstance(v, dict)}
        except (OSError, json.JSONDecodeError, AttributeError):
            overrides = {}
    # never re-ask already adjudicated findings (merge semantics)
    before = len(items)
    items = [it for it in items if it["key"] not in overrides]
    print(f"verify-findings: {before} total, {len(overrides)} already "
          f"adjudicated, {len(items)} remaining", flush=True)
    kept = corrected = dropped = 0
    batch_size = 15
    for start in range(0, len(items), batch_size):
        batch = items[start: start + batch_size]
        req_items = [
            {"i": i, "contract": b["contract"], "question": b["question"],
             "section": b["section"], "kind": b["kind"], "text": b["text"]}
            for i, b in enumerate(batch)
        ]
        messages = [
            {"role": "system", "content": FINDINGS_SYSTEM},
            {"role": "user", "content": "Items:\n"
             + json.dumps(req_items, ensure_ascii=False)},
        ]
        if args.dry_run:
            print("=" * 70)
            print(f"DRY-RUN verify-findings batch {start // batch_size + 1} "
                  f"({len(batch)} items)")
            print("--- system ---")
            print(FINDINGS_SYSTEM)
            print("--- user (gekürzt auf 3000 Zeichen) ---")
            print(messages[1]["content"][:3000])
            continue
        content, ok = chat_complete(messages, timeout=240)
        if not ok:
            continue
        obj = extract_json_block(content)
        results = (obj or {}).get("results")
        if not isinstance(results, list):
            sys.stderr.write(f"batch {start}: no results list -- skipped\n")
            continue
        seen_i = set()
        for r in results:
            if not isinstance(r, dict):
                continue
            i = r.get("i")
            action = r.get("action")
            if i not in range(len(batch)) or i in seen_i:
                continue
            if action not in ("keep", "correct", "drop"):
                continue
            seen_i.add(i)
            entry = {"action": action}
            if action == "correct":
                kind = r.get("kind")
                if kind not in ("refutes", "no_go", "supports", "open"):
                    entry = {"action": "keep"}
                else:
                    entry["kind"] = kind
            overrides[batch[i]["key"]] = entry
            kept += action == "keep"
            corrected += action == "correct"
            dropped += action == "drop"
        # incremental write after EVERY batch: resumable, kill-safe
        write_overrides(overrides, len(items), kept, corrected, dropped)
        print(f"verify-findings batch {start // batch_size + 1}: "
              f"{len(seen_i)}/{len(batch)} adjudicated "
              f"(kept={kept} corrected={corrected} dropped={dropped})",
              flush=True)
    if args.dry_run:
        return
    print(f"wrote {OVERRIDES_PATH.relative_to(ROOT)}: kept={kept} "
          f"corrected={corrected} dropped={dropped} (total {len(items)})")


def write_overrides(overrides, total, kept, corrected, dropped):
    payload = {
        "meta": {
            "model": MODEL,
            "date": date.today().isoformat(),
            "total": total,
            "adjudicated": len(overrides),
            "kept": kept,
            "corrected": corrected,
            "dropped": dropped,
        },
        "overrides": dict(sorted(overrides.items())),
    }
    tmp = OVERRIDES_PATH.with_name(OVERRIDES_PATH.name + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n",
                   encoding="utf-8")
    os.replace(tmp, OVERRIDES_PATH)


# --------------------------------------------------------------------------
# extract-v2: Phase-3 content for the graph_v2 sidecars (schema-bound)
# --------------------------------------------------------------------------

GRAPH_V2_DIR = VERIF / "graph_v2"
V2_PROVENANCE = {"source": "llm_extract", "model": MODEL,
                 "date": "2026-09-17", "reviewed": False}
EPISTEMIC_ENUM = {"proved", "machine_checked", "numerical", "assumed",
                  "physically_identified", "open"}
OBJECT_KINDS = {"space", "algebra", "state", "operator", "representation",
                "map", "number"}
TRANSITION_STATUS = {"established", "partial", "missing", "obstructed"}

V2_REJECTS = {"claims": 0, "transitions": 0, "constraints": 0, "failures": 0}


def derive_epistemic(markers, has_script, status=""):
    """Deterministic from ledger status markers (never LLM-guessed)."""
    ms = set(markers or [])
    if "O" in ms:
        return "open"
    if "N" in ms:
        return "numerical"
    if "C" in ms:
        return "physically_identified"
    if "A" in ms:
        return "assumed"
    if (status or "").startswith("Axiom"):
        return "assumed"
    if "E" in ms:
        return "machine_checked" if has_script else "proved"
    return "open"


def sidecar_load(name):
    path = GRAPH_V2_DIR / f"{name}.json"
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("records"), list):
                return data
        except (OSError, json.JSONDecodeError):
            pass
    return {"schema_version": 2, "meta": {"doc": name}, "records": []}


def sidecar_merge_save(name, new_records, key):
    """Merge by key (existing keys are kept, never overwritten)."""
    payload = sidecar_load(name)
    existing = {r.get(key) for r in payload["records"] if isinstance(r, dict)}
    added = []
    for rec in new_records:
        k = rec.get(key)
        if not k or k in existing:
            continue
        existing.add(k)
        payload["records"].append(rec)
        added.append(k)
    path = GRAPH_V2_DIR / f"{name}.json"
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n",
                   encoding="utf-8")
    os.replace(tmp, path)
    return added


def script_docstring(script_base, max_lines=80):
    path = VERIF / f"{script_base}.py"
    if not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    lines = text.splitlines()[:max_lines]
    return "\n".join(lines)


def claim_packet(g_nodes, g_edges, ledger_by_id, cid):
    """Assemble the LLM input packet for one claim from graph + ledger."""
    node = g_nodes.get(f"claim:{cid}")
    if node is None:
        return None
    a = node["attrs"]
    out_e = [e for e in g_edges if e["src"] == f"claim:{cid}"]
    scripts = [e["dst"].split(":", 1)[1] for e in out_e
               if e["type"] == "verified_by"]
    sections = []
    for e in out_e:
        if e["type"] == "stated_in":
            sec = g_nodes.get(e["dst"])
            if sec:
                t = sec["attrs"].get("title")
                if t and t not in sections:
                    sections.append(t)
    row = ledger_by_id.get(cid) or {}
    return {
        "claim_id": cid,
        "claim_ledger": btg.clip(row.get("claim"), 700),
        "status": a.get("status_raw"),
        "canonical_status": a.get("canonical_status"),
        "markers": a.get("markers") or [],
        "epistemic_derived": derive_epistemic(a.get("markers"), bool(scripts),
                                              a.get("status_raw")),
        "verified_by": [{"script": s,
                         "docstring": script_docstring(s)} for s in scripts[:2]],
        "stated_in_sections": sections[:6],
    }


CLAIMS_SYSTEM = """\
Du erstellst praezise mathematische Vertraege (claim_contract) fuer TFPT-Ledger-Claims.
Harte Regeln:
1. Antworte NUR als JSON: {"records": [ ... ]} — ein Record pro Claim der Anfrage.
2. NICHTS erfinden: nur was in den Quellen (Ledger-Text, Skript-Docstring, \
Section-Titel) steht. Fehlendes Feld = leere Liste/null. NIEMALS raten.
3. premises sind EINE konjunktive Menge (alle zusammen noetig) — niemals in \
Einzelschritte zerlegen.
4. epistemic: exakt den mitgelieferten Wert epistemic_derived uebernehmen.
5. proof.script: nur ein mitgeliefertes verified_by-Skript oder null.
6. objects[].kind nur aus: space|algebra|state|operator|representation|map|number.
Record-Felder: claim_id, statement (ein Satz, mit Quantoren/Grenzwert), \
quantifiers [], limit, premises [], chosen_structures [], objects [], \
epistemic, proof {script, checked_relation, scope, source_ref}."""

CLAIM_ANCHORS = [
    "AX.P1.01", "AX.P2.01", "QGEO.KERNEL.01", "QGEO.MARKS.01", "QGEO.REDUCE.01",
    "QGEO.CONF.01", "E8.GLU.01", "E8.ONEOBJECT.01", "E8.G31.CLOCK",
    "E8.DEGREE.JOINT.01", "E8.ORBIT60.01", "E8.COXETER.EULER.COMPLETION.01",
    "SEAM.EQUIV.01", "SEAM.EQUIV.BW.HSMI.01", "SEAM.KHALF.01", "FORM.P2.02",
    "EM.FP.01", "EM.BUDGET.01",
]


def select_claims(g_nodes, g_edges, claim_ids):
    anchors = [c for c in CLAIM_ANCHORS if c in claim_ids]
    anchors += sorted(c for c in claim_ids if c.startswith("CAR."))[:11]
    anchors += sorted(c for c in claim_ids if c.startswith("ARCH."))[:11]
    anchors += sorted(c for c in claim_ids if c.startswith("ALPHA."))[:9]
    seen = set()
    ordered = []
    for c in anchors:
        if c not in seen:
            seen.add(c)
            ordered.append(c)
    # + depends_on partners, 1st level
    for e in g_edges:
        if (e["type"] == "depends_on" and e["src"] in {f"claim:{c}" for c in ordered}
                and e["dst"].startswith("claim:")):
            partner = e["dst"].split(":", 1)[1]
            if partner not in seen:
                seen.add(partner)
                ordered.append(partner)
    return ordered[:60]


def _claims_call(packets, batch):
    """One API call for a claim batch; returns validated records or None.
    Never raises.  240 s: one claim generates ~4k tokens (reasoning incl.),
    which needs ~120 s at current API speed -- 120 s would kill half."""
    messages = [
        {"role": "system", "content": CLAIMS_SYSTEM},
        {"role": "user", "content": "Claims:\n"
         + json.dumps(packets, ensure_ascii=False)},
    ]
    content, ok = chat_complete(messages, timeout=240)
    if not ok:
        return None
    obj = extract_json_block(content)
    recs = (obj or {}).get("records")
    if not isinstance(recs, list):
        sys.stderr.write("claims batch: no records in answer\n")
        return None
    out = []
    for rec in recs:
        if not isinstance(rec, dict) or rec.get("claim_id") not in batch:
            V2_REJECTS["claims"] += 1
            continue
        cid = rec["claim_id"]
        packet = next((p for p in packets if p["claim_id"] == cid), {})
        proof = rec.get("proof") if isinstance(rec.get("proof"), dict) else {}
        pscript = proof.get("script")
        allowed_scripts = {s["script"] for s in packet.get("verified_by", [])}
        objects = []
        for o in (rec.get("objects") or [])[:12]:
            if (isinstance(o, dict) and o.get("name")
                    and o.get("kind") in OBJECT_KINDS):
                objects.append({"kind": o["kind"],
                                "name": btg.clip(o["name"], 120)})
        out.append({
            "claim_id": cid,
            "statement": btg.clip(rec.get("statement") or "", 500),
            "quantifiers": [btg.clip(q, 200) for q in
                            (rec.get("quantifiers") or [])[:8]],
            "limit": btg.clip(rec.get("limit") or "", 120),
            "premises": [btg.clip(p, 200) for p in
                         (rec.get("premises") or [])[:10]],
            "chosen_structures": [btg.clip(x, 120) for x in
                                  (rec.get("chosen_structures") or [])[:10]],
            "objects": objects,
            "epistemic": packet.get("epistemic_derived") or "open",
            "proof": {
                "script": pscript if pscript in allowed_scripts else None,
                "checked_relation": btg.clip(proof.get("checked_relation") or "", 200),
                "scope": btg.clip(proof.get("scope") or "", 200),
                "source_ref": btg.clip(proof.get("source_ref") or "", 200),
            },
            "provenance": dict(V2_PROVENANCE),
        })
    return out


def cmd_extract_v2_claims(args, graph, g_nodes, g_edges, claim_ids, slugs):
    ledger_by_id = {}
    import csv as _csv
    with open(VERIF / "status_ledger.csv", newline="", encoding="utf-8") as f:
        for row in _csv.DictReader(f):
            ledger_by_id[(row.get("claim_id") or "").strip()] = row
    targets = select_claims(g_nodes, g_edges, claim_ids)
    # incremental resume: skip claims already contracted
    existing = {r.get("claim_id")
                for r in sidecar_load("claim_contracts")["records"]}
    targets = [c for c in targets if c not in existing]
    if args.limit:
        targets = targets[: args.limit]
    print(f"extract-v2 claims: {len(targets)} claims selected "
          f"({len(existing)} already present)", flush=True)
    batch_size = 2  # API-Reality: 5 Records > 10k Tokens Generation > Timeout
    total_written = 0
    for start in range(0, len(targets), batch_size):
        batch = targets[start: start + batch_size]
        packets = [p for p in (claim_packet(g_nodes, g_edges, ledger_by_id, c)
                             for c in batch) if p]
        if args.dry_run:
            print("=" * 70)
            print(f"DRY-RUN claims batch {start // batch_size + 1}: {[c for c in batch]}")
            print(json.dumps(packets, ensure_ascii=False)[:3000])
            continue
        recs = _claims_call(packets, batch)
        if recs is None and len(batch) > 1:
            # timeout/parse fallback: split into singles, retry each once
            sys.stderr.write(f"claims batch {start // batch_size + 1}: "
                             f"failed -- splitting into singles\n")
            recs = []
            for c in batch:
                p1 = claim_packet(g_nodes, g_edges, ledger_by_id, c)
                r1 = _claims_call([p1], [c]) if p1 else None
                if r1:
                    recs.extend(r1)
        if not recs:
            continue
        # INCREMENTAL: atomic merge after EVERY batch (crash loses <= 1 batch)
        added = sidecar_merge_save("claim_contracts", recs, "claim_id")
        total_written += len(added)
        print(f"claims batch {start // batch_size + 1}: +{len(added)} "
              f"(total {total_written})", flush=True)
    if args.dry_run:
        return
    print(f"claim_contracts.json: +{total_written} records "
          f"(rejects={V2_REJECTS['claims']})")


TRANSITIONS_SYSTEM = """\
Du extrahierst pruefbare Uebergaenge (transition) zwischen Konstruktionen des \
TFPT-Projekts aus den gegebenen Quellen (Contract-Findings, contract_index, \
Skript-Docstrings).
Harte Regeln:
1. Antworte NUR als JSON: {"records": [ ... ]}.
2. NICHTS erfinden — nur was die Quellen tragen. Ein 'missing'/'obstructed' \
Status ist ein ehrlicher Zustand.
3. Die drei MUSS-Uebergaenge (unten spezifiziert) exakt mit den spezifizierten \
Inhalten uebernehmen.
4. id im Format TRANS.<VON>.<ZU>.NN; status nur established|partial|missing|obstructed.
5. checked_by nur aus den mitgelieferten, existierenden Referenzen \
(contract:<slug> oder vN_*.py).
Record-Felder: id, from, to, map, preserves [], fails_to_preserve [], status, \
checked_by [], counterexample, notes."""


def cmd_extract_v2_transitions(args, graph, g_nodes, g_edges, claim_ids, slugs):
    # sources: findings + contract_index of the involved contracts
    involved = [
        "universalraum-d4-torsor-seam-20260917",
        "modular-source-selection-audit-20260917",
        "universalraum-source-equivalence-decision-20260915",
        "universalraum-mu4-pointing-20260917",
        "clock-bilinear-response",
        "carrier-module-conjugation",
    ]
    packets = []
    for slug in involved:
        node = g_nodes.get(f"contract:{slug}")
        folder = CONTRACTS_DIR / slug
        cidx = None
        if (folder / "contract_index.json").is_file():
            try:
                cidx = json.loads((folder / "contract_index.json").read_text(
                    encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                cidx = None
        readme = read_clip(folder / "README.md", 6000)
        results = read_clip(folder / "RESULTS.md", 6000)
        packets.append({
            "contract": slug,
            "contract_index": cidx,
            "findings": (node["attrs"].get("findings") if node else []) or [],
            "README": readme,
            "RESULTS": results,
        })
    v438 = script_docstring("v438_seam_hsmi_borchers", 60)
    muss = [
        {"id": "TRANS.D4RAW.BANK.01",
         "from": "raw 256-mode seam space",
         "to": "W-Vierbank",
         "status": "obstructed",
         "counterexample": "dim Hom_D4 = 8192 für alle sechs Lifts (d4-torsor-seam-20260917)",
         "checked_by": ["contract:universalraum-d4-torsor-seam-20260917"]},
        {"id": "TRANS.BOUNDARY.MODULAR.01",
         "from": "Randnetz",
         "to": "modulare Dynamik",
         "status": "obstructed",
         "notes": "v438 prüft exp(it) statt exp(-t); Phasenrest 3.89e-16 vs reeller Rest .434894",
         "checked_by": ["contract:modular-source-selection-audit-20260917",
                        "v438_seam_hsmi_borchers"]},
        {"id": "TRANS.SEAMCAR.E8CURRENT.01",
         "from": "Seam-CAR",
         "to": "E8-Ströme",
         "status": "missing",
         "notes": "direkte Gleichsetzung REFUTED (source-equivalence-decision-20260915); notes aus Quelle",
         "checked_by": ["contract:universalraum-source-equivalence-decision-20260915"]},
    ]
    messages = [
        {"role": "system", "content": TRANSITIONS_SYSTEM},
        {"role": "user", "content":
            "MUSS-Uebergaenge (Inhalte exakt uebernehmen, fehlende Felder aus "
            "den Quellen ergaenzen):\n" + json.dumps(muss, ensure_ascii=False)
            + "\n\nv438_seam_hsmi_borchers Docstring:\n" + str(v438)
            + "\n\nQuellen-Contracts:\n"
            + json.dumps(packets, ensure_ascii=False)[:30000]
            + "\n\nLiefere 5-10 transition-Records (die 3 MUSS + weitere nur "
              "wenn die Quellen sie tragen)."},
    ]
    if args.dry_run:
        print("=" * 70)
        print("DRY-RUN transitions")
        print(messages[1]["content"][:3000])
        return
    content, ok = chat_complete(messages, timeout=240)
    if not ok:
        return
    obj = extract_json_block(content)
    recs = (obj or {}).get("records")
    if not isinstance(recs, list):
        sys.stderr.write("transitions: no records -- skipped\n")
        return
    seen = set()
    n_written = 0
    for rec in recs:
        if not isinstance(rec, dict):
            V2_REJECTS["transitions"] += 1
            continue
        tid = rec.get("id")
        if not tid or not str(tid).startswith("TRANS.") or tid in seen:
            V2_REJECTS["transitions"] += 1
            continue
        status = rec.get("status")
        if status not in TRANSITION_STATUS:
            V2_REJECTS["transitions"] += 1
            continue
        checked = []
        for cb in rec.get("checked_by") or []:
            cb = str(cb)
            if (cb.startswith("contract:") and cb[9:] in slugs) or \
               (cb.removesuffix(".py") and (VERIF / cb).is_file()) or \
               (VERIF / (cb + ".py")).is_file():
                checked.append(cb)
        seen.add(tid)
        rec_out = {
            "id": tid,
            "from": btg.clip(rec.get("from") or "", 120),
            "to": btg.clip(rec.get("to") or "", 120),
            "map": btg.clip(rec.get("map") or "", 300),
            "preserves": [btg.clip(x, 80) for x in (rec.get("preserves") or [])[:10]],
            "fails_to_preserve": [btg.clip(x, 80) for x in
                                  (rec.get("fails_to_preserve") or [])[:10]],
            "status": status,
            "checked_by": checked,
            "counterexample": btg.clip(rec.get("counterexample") or "", 200),
            "notes": btg.clip(rec.get("notes") or "", 300),
            "provenance": dict(V2_PROVENANCE),
        }
        # INCREMENTAL: atomic merge after EVERY record
        added = sidecar_merge_save("transitions", [rec_out], "id")
        n_written += len(added)
        print(f"transitions: wrote {tid}", flush=True)
    print(f"transitions.json: +{n_written} records "
          f"(rejects={V2_REJECTS['transitions']})")


CONSTRAINTS_SYSTEM = """\
Du extrahierst gemeinsame Bedingungen (constraint) an GETEILTE \
Ursprungsobjekte des TFPT-Projekts: unabhaengig begruendete Anforderungen \
von verschiedenen Seiten an dasselbe Objekt (gemeinsamer Bedingungsraum).
Harte Regeln:
1. Antworte NUR als JSON: {"records": [ ... ]}.
2. NICHTS erfinden — nur Anforderungen, die in den mitgelieferten Quellen \
(Ledger-Zeilen, Contract-READMEs) tatsaechlich belegt sind. Fehlende Felder \
= leer lassen, niemals raten.
3. raised_by MUSS eine claim_id aus der mitgelieferten Kandidatenliste oder \
ein contract:<slug> aus der mitgelieferten Liste sein.
4. on_object: das geteilte Objekt (z.B. 'seam carrier', 'raw 256-mode \
space', 'W-Bank (vier Basispunkte)', 'Station clock') — praezise, quellennah.
5. id im Format CONS.<BEREICH>.NN, eindeutig.
6. independent_of: nur ids anderer Records DIESER Antwort, die unabhaengig \
begruendet sind (sonst leer lassen).
Record-Felder: id, on_object, requirement, raised_by, independent_of []."""


CONSTRAINT_PREFIXES = ("SEAM.CLOCK.", "E8.G31.CLOCK", "QGEO.", "FLAV.",
                       "EM.", "GATE.")
CONSTRAINT_CONTRACTS = ("clock-bilinear-response",
                        "universalraum-d4-torsor-seam-20260917")


def cmd_extract_v2_constraints(args, graph, g_nodes, g_edges, claim_ids, slugs):
    import csv as _csv
    rows = []
    ledger_path = VERIF / "status_ledger.csv"
    if not ledger_path.is_file():
        sys.stderr.write("status_ledger.csv missing -- constraints aborted\n")
        return
    with open(ledger_path, newline="", encoding="utf-8") as f:
        for row in _csv.DictReader(f):
            cid = (row.get("claim_id") or "").strip()
            if cid.startswith(CONSTRAINT_PREFIXES) and cid in claim_ids:
                rows.append({
                    "claim_id": cid,
                    "status": btg.clip((row.get("status") or "").strip(), 200),
                    "claim": btg.clip((row.get("claim") or "").strip()
                                      .replace("\n", " "), 200),
                })
    readmes = {}
    for slug in CONSTRAINT_CONTRACTS:
        if slug not in slugs:
            sys.stderr.write(f"constraint source contract missing: {slug}\n")
            continue
        text = read_clip(CONTRACTS_DIR / slug / "README.md", 5000)
        if text:
            readmes[f"contract:{slug}"] = text
    allowed = {r["claim_id"] for r in rows} | set(readmes)
    context = (
        "ERLAUBTE raised_by claim_ids:\n"
        + json.dumps(sorted(r["claim_id"] for r in rows), ensure_ascii=False)
        + "\n\nERLAUBTE raised_by contracts:\n"
        + json.dumps(sorted(readmes), ensure_ascii=False)
        + "\n\nLEDGER-ZEILEN (claim_id, status, claim):\n"
        + json.dumps(rows, ensure_ascii=False)
        + "\n\nCONTRACT-READMES:\n"
        + json.dumps(readmes, ensure_ascii=False))
    # two small generation calls instead of one large one (API-Reality:
    # grosse Antworten laufen in den 240-s-Timeout); resume-safe: ein
    # bereits befuellter Fokus (id-Praefix vorhanden) wird uebersprungen
    calls = [
        (("CONS.CARRIER.", "CONS.RAW256."),
         "Objektfokus 1: 'seam carrier' und 'raw 256-mode space'. "
         "Liefere ca. 5 Records (ids CONS.CARRIER.NN / CONS.RAW256.NN)."),
        (("CONS.WBANK.", "CONS.CLOCK."),
         "Objektfokus 2: 'W-Bank (vier Basispunkte)' und 'Station clock' "
         "(plus hoechstens 2 weitere geteilte Objekte, wenn die Quellen "
         "sie tragen). Liefere ca. 5 Records (ids CONS.WBANK.NN / "
         "CONS.CLOCK.NN / CONS.<BEREICH>.NN)."),
    ]
    known = {r.get("id") for r in sidecar_load("constraints")["records"]
             if isinstance(r, dict)}
    seen = set()
    n_written = 0
    for focus_prefixes, focus in calls:
        if any(str(k).startswith(focus_prefixes) for k in known):
            print(f"constraints: focus {focus_prefixes[0]}.. already "
                  f"present -- skipped", flush=True)
            continue
        messages = [
            {"role": "system", "content": CONSTRAINTS_SYSTEM},
            {"role": "user", "content": context + "\n\n" + focus},
        ]
        if args.dry_run:
            print("=" * 70)
            print("DRY-RUN constraints:", focus[:60])
            print(messages[1]["content"][:2500])
            continue
        content, ok = chat_complete(messages, timeout=240)
        if not ok:
            continue
        obj = extract_json_block(content)
        recs = (obj or {}).get("records")
        if not isinstance(recs, list):
            sys.stderr.write("constraints: no records -- call skipped\n")
            continue
        for rec in recs:
            if not isinstance(rec, dict):
                V2_REJECTS["constraints"] += 1
                continue
            cid = rec.get("id")
            rb = str(rec.get("raised_by") or "").strip()
            if (not cid or not str(cid).startswith("CONS.") or cid in seen
                    or rb not in allowed
                    or not str(rec.get("on_object") or "").strip()
                    or not str(rec.get("requirement") or "").strip()):
                V2_REJECTS["constraints"] += 1
                continue
            seen.add(cid)
            indep = [str(x) for x in (rec.get("independent_of") or [])
                     if str(x) in seen or str(x) in known][:8]
            rec_out = {
                "id": cid,
                "on_object": btg.clip(rec.get("on_object") or "", 200),
                "requirement": btg.clip(rec.get("requirement") or "", 300),
                "raised_by": rb,
                "independent_of": indep,
                "provenance": dict(V2_PROVENANCE),
            }
            # INCREMENTAL: atomic merge after EVERY record
            added = sidecar_merge_save("constraints", [rec_out], "id")
            known.add(cid)
            n_written += len(added)
            print(f"constraints: wrote {cid}", flush=True)
    if args.dry_run:
        return
    print(f"constraints.json: +{n_written} records "
          f"(rejects={V2_REJECTS['constraints']})")


FAILURES_SYSTEM = """\
Du extrahierst failure_scope-Eintraege (Ausschluss-Gedaechtnis MIT \
Reichweite) aus getoeteten Ansaetzen des TFPT/RH-Programms.
Harte Regeln:
1. Antworte NUR als JSON: {"records": [ ... ]}.
2. Negationen korrekt: 'nicht widerlegt' ist KEIN Ausschluss. \
excluded_under, not_excluded und retry_condition NUR aus dem mitgelieferten \
Quelltext (failed_because / mechanism / question / Ledger-Status der \
getoeteten Claims / RESULTS-Auszug / contract_index), niemals raten. \
Steht nichts da: Feld leer lassen.
3. evidence NUR aus den mitgelieferten Referenzen des jeweiligen Items \
(rh:<path>, contract:<slug>, claim_id) — unveraendert uebernehmen.
4. id im Format FAIL.<THEMA>.NN, eindeutig; vorgegebene MUSS-ids exakt \
uebernehmen.
5. target: die ausgeschlossene Hypothese/Ansatzklasse, praezise und eng. \
approach_class: die Klasse, die tatsaechlich scheitert.
Record-Felder: id, target, approach_class, excluded_under [], \
not_excluded [], retry_condition, evidence []."""


FAIL_MUSS_CONTRACTS = [
    ("FAIL.QUELLENABBILDUNG.GAUSS.01",
     "universalraum-source-equivalence-decision-20260915"),
    ("FAIL.ORIENTIERUNG.T4C4.01",
     "universalraum-d4-torsor-seam-20260917"),
]
FAIL_MUSS_RH = [
    ("FAIL.CLOCK.TORSIONECM.01", "clock_torsion_ecm"),
    ("FAIL.PRIME.EVOSEARCH.01", "prime_inequality_evosearch"),
    ("FAIL.EVENT.LINDBLAD.01", "event_lindblad_twokey"),
    ("FAIL.KERNEL.LOEWNER08.01", "kernel_loewner08"),
]
FAIL_TOP_RH = 16  # weitere Records: bestreferenzierte rh-KILLED


def cmd_extract_v2_failures(args, graph, g_nodes, g_edges, claim_ids, slugs):
    import csv as _csv
    ledger_by_id = {}
    ledger_path = VERIF / "status_ledger.csv"
    if ledger_path.is_file():
        with open(ledger_path, newline="", encoding="utf-8") as f:
            for row in _csv.DictReader(f):
                ledger_by_id[(row.get("claim_id") or "").strip()] = row
    else:
        sys.stderr.write("status_ledger.csv missing -- ledger text skipped\n")
    catalog = {}
    cat_path = ROOT / "rh" / "catalog" / "rh_semantic_catalog.json"
    if cat_path.is_file():
        try:
            cat = json.loads(cat_path.read_text(encoding="utf-8"))
            for r in cat.get("records") or []:
                if r.get("path"):
                    catalog[r["path"]] = r
        except (OSError, json.JSONDecodeError):
            sys.stderr.write("rh catalog unreadable -- failed_because skipped\n")
    else:
        sys.stderr.write("rh catalog missing -- failed_because skipped\n")
    kills_by_rh = {}
    ref_count = Counter()
    for e in g_edges:
        src = e.get("src") or ""
        if not src.startswith("rh:"):
            continue
        if e.get("type") == "references":
            ref_count.update([src])
        elif e.get("type") == "kills" and (e.get("dst") or "").startswith("claim:"):
            kills_by_rh.setdefault(src, []).append(e["dst"].split(":", 1)[1])

    def rh_payload(path):
        n = g_nodes.get(f"rh:{path}") or {}
        a = n.get("attrs") or {}
        rec = catalog.get(path) or {}
        killed = []
        for cid in (kills_by_rh.get(f"rh:{path}") or [])[:3]:
            row = ledger_by_id.get(cid) or {}
            killed.append({
                "claim_id": cid,
                "status": btg.clip((row.get("status") or "").strip(), 160),
                "claim": btg.clip((row.get("claim") or "").strip()
                                  .replace("\n", " "), 240),
            })
        return {
            "evidence": [f"rh:{path}"],
            "round": a.get("round"),
            "failure_class": a.get("failure_class"),
            "mechanism": btg.clip(a.get("mechanism"), 300),
            "question": btg.clip(a.get("question"), 200),
            "failed_because": btg.clip(rec.get("failed_because"), 400),
            "killed_claims": killed,
        }

    def contract_payload(slug, results_chars=7000):
        n = g_nodes.get(f"contract:{slug}") or {}
        a = n.get("attrs") or {}
        folder = CONTRACTS_DIR / slug
        cidx = None
        if (folder / "contract_index.json").is_file():
            try:
                cidx = json.loads((folder / "contract_index.json").read_text(
                    encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                cidx = None
        return {
            "evidence": [f"contract:{slug}"],
            "verdict": a.get("verdict_raw"),
            "verdict_class": a.get("verdict_class"),
            "contract_index": cidx,
            "findings_refutes_no_go": [
                f for f in (a.get("findings") or [])
                if f.get("kind") in ("refutes", "no_go")][:6],
            "README": read_clip(folder / "README.md", 5000),
            "RESULTS": read_clip(folder / "RESULTS.md", results_chars),
        }

    # --- MUSS items (ids are binding) ------------------------------------
    existing_fail = sidecar_load("failure_scopes")["records"]
    existing_ids = {r.get("id") for r in existing_fail
                    if isinstance(r, dict)}
    covered_evidence = {ev for r in existing_fail if isinstance(r, dict)
                        for ev in (r.get("evidence") or [])}
    muss = []
    for fid, slug in FAIL_MUSS_CONTRACTS:
        if fid in existing_ids:
            continue
        if f"contract:{slug}" not in g_nodes:
            sys.stderr.write(f"MUSS contract missing from graph: {slug}\n")
            continue
        p = contract_payload(slug)
        p["id"] = fid
        muss.append(p)
    muss_rh_paths = set()
    for fid, needle in FAIL_MUSS_RH:
        hits = sorted(p for p in catalog
                      if needle in p and f"rh:{p}" in g_nodes)
        if not hits:
            sys.stderr.write(f"MUSS rh needle {needle!r}: no graph node\n")
            continue
        muss_rh_paths.update(hits)
        if fid in existing_ids:
            continue
        muss.append({"id": fid,
                     "evidence": [f"rh:{p}" for p in hits],
                     "items": [rh_payload(p) for p in hits]})
    # --- rest: top-referenced rh KILLED + failed contracts ----------------
    killed_rh = [n for n in graph["nodes"]
                 if n["type"] == "rh"
                 and n["attrs"].get("outcome") == "KILLED"
                 and n["label"] not in muss_rh_paths]
    killed_rh.sort(key=lambda n: (-ref_count.get(n["id"], 0), n["label"]))
    top_rh = [rh_payload(n["label"]) for n in killed_rh[:FAIL_TOP_RH]]
    # resume-safe: Items deren evidence bereits im Sidecar abgedeckt ist,
    # werden nicht erneut angefragt (sonst Doppel-Records unter neuer id)
    top_rh = [p for p in top_rh
              if not set(p["evidence"]) & covered_evidence]
    muss_slugs = {s for _i, s in FAIL_MUSS_CONTRACTS}
    extra_contracts = []
    for n in graph["nodes"]:
        if (n["type"] == "contract"
                and n["attrs"].get("verdict_class") in ("killed", "refuted",
                                                        "fail")
                and n["label"] not in muss_slugs):
            extra_contracts.append(contract_payload(n["label"], 4000))
    extra_contracts.sort(key=lambda p: p["evidence"][0])
    extra_contracts = [p for p in extra_contracts
                       if not set(p["evidence"]) & covered_evidence]

    batches = [
        ("MUSS", muss,
         "Liefere fuer JEDES MUSS-Item genau einen Record mit der "
         "vorgegebenen id. excluded_under / not_excluded / retry_condition "
         "strikt aus den Quelltexten des Items."),
        ("RH-TOP", top_rh,
         "Liefere pro Item genau einen Record; id FAIL.<THEMA>.NN mit THEMA "
         "aus Mechanismus/Familie des Items."),
        ("CONTRACTS", extra_contracts,
         "Liefere pro Contract genau einen Record; id FAIL.<THEMA>.NN."),
    ]

    def valid_evidence(ev_list):
        out = []
        for ev in ev_list or []:
            ev = str(ev)
            if (ev.startswith("rh:") and ev in g_nodes) or \
               (ev.startswith("contract:") and ev[9:] in slugs) or \
               (ev in claim_ids):
                out.append(ev)
        return out

    n_written = 0
    seen = set()
    for bname, items, instr in batches:
        if not items:
            continue
        # cap generation size: split large batches into chunks of 5
        for start in range(0, len(items), 5):
            chunk = items[start: start + 5]
            messages = [
                {"role": "system", "content": FAILURES_SYSTEM},
                {"role": "user", "content":
                    instr + "\n\nItems:\n"
                    + json.dumps(chunk, ensure_ascii=False)},
            ]
            if args.dry_run:
                print("=" * 70)
                print(f"DRY-RUN failures {bname} [{start}:{start + len(chunk)}]")
                print(messages[1]["content"][:3000])
                continue
            content, ok = chat_complete(messages, timeout=240)
            if not ok:
                continue
            obj = extract_json_block(content)
            recs = (obj or {}).get("records")
            if not isinstance(recs, list):
                sys.stderr.write(f"failures {bname}: no records -- skipped\n")
                continue
            for rec in recs:
                if not isinstance(rec, dict):
                    V2_REJECTS["failures"] += 1
                    continue
                fid = rec.get("id")
                if (not fid or not str(fid).startswith("FAIL.")
                        or fid in seen
                        or not str(rec.get("target") or "").strip()):
                    V2_REJECTS["failures"] += 1
                    continue
                evidence = valid_evidence(rec.get("evidence"))
                if not evidence:
                    V2_REJECTS["failures"] += 1
                    continue
                seen.add(fid)
                rec_out = {
                    "id": fid,
                    "target": btg.clip(rec.get("target") or "", 300),
                    "approach_class": btg.clip(rec.get("approach_class") or "",
                                               200),
                    "excluded_under": [btg.clip(x, 160) for x in
                                       (rec.get("excluded_under") or [])[:8]],
                    "not_excluded": [btg.clip(x, 160) for x in
                                     (rec.get("not_excluded") or [])[:8]],
                    "retry_condition": btg.clip(rec.get("retry_condition")
                                                or "", 300),
                    "evidence": evidence[:8],
                    "provenance": dict(V2_PROVENANCE),
                }
                # INCREMENTAL: atomic merge after EVERY record
                added = sidecar_merge_save("failure_scopes", [rec_out], "id")
                n_written += len(added)
                print(f"failure_scopes: wrote {fid}", flush=True)
    if args.dry_run:
        return
    print(f"failure_scopes.json: +{n_written} records "
          f"(rejects={V2_REJECTS['failures']})")


def cmd_extract_v2(args, graph):
    g_nodes = {n["id"]: n for n in graph["nodes"]}
    g_edges = graph["edges"]
    claim_ids = {n["label"] for n in graph["nodes"] if n["type"] == "claim"}
    slugs = {n["label"] for n in graph["nodes"] if n["type"] == "contract"}
    only = args.only
    if only in (None, "claims"):
        cmd_extract_v2_claims(args, graph, g_nodes, g_edges, claim_ids, slugs)
    if only in (None, "transitions"):
        cmd_extract_v2_transitions(args, graph, g_nodes, g_edges, claim_ids, slugs)
    if only in (None, "constraints"):
        cmd_extract_v2_constraints(args, graph, g_nodes, g_edges, claim_ids, slugs)
    if only in (None, "failures"):
        cmd_extract_v2_failures(args, graph, g_nodes, g_edges, claim_ids, slugs)
    if not args.dry_run:
        print("extract-v2 rejects total: %s" % json.dumps(V2_REJECTS))


# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="enrich_theory_graph_llm",
        description="LLM enrichment for the TFPT theory graph (Moonshot/Kimi).")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ("backfill-contracts", "verify-findings"):
        p = sub.add_parser(name)
        p.add_argument("--dry-run", action="store_true",
                       help="print prompts only, no API call")
        p.add_argument("--limit", type=int, default=0, metavar="N")
    p = sub.add_parser("extract-v2",
                       help="Phase-3: fill the graph_v2 sidecars (schema-bound)")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=0, metavar="N")
    p.add_argument("--only", choices=["claims", "transitions", "constraints",
                                      "failures"], default=None)
    args = parser.parse_args()
    if not GRAPH_PATH.is_file():
        sys.stderr.write("theory graph missing: run: "
                         "python verification/build_theory_graph.py\n")
        sys.exit(2)
    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    if args.cmd == "backfill-contracts":
        cmd_backfill(args, graph)
    elif args.cmd == "verify-findings":
        cmd_verify_findings(args, graph)
    else:
        cmd_extract_v2(args, graph)
    if not args.dry_run:
        print("token usage: prompt=%d completion=%d total=%d calls=%d failed=%d"
              % (USAGE["prompt_tokens"], USAGE["completion_tokens"],
                 USAGE["total_tokens"], USAGE["calls"], USAGE["failed_calls"]))


if __name__ == "__main__":
    main()
