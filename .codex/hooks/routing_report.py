#!/usr/bin/env python3
"""Summarise .cursor/agent-runs/routing.jsonl — which tiers actually did the work.

Usage:
    python3 .cursor/hooks/routing_report.py [--since YYYY-MM-DD]
"""

import argparse
import collections
import json
import os
import sys

HOOK_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(HOOK_DIR, os.pardir, "agent-runs", "routing.jsonl")
POLICY_PATH = os.path.join(HOOK_DIR, "model-tiers.json")


def load_records(since):
    if not os.path.exists(LOG_PATH):
        sys.exit("no routing log yet: %s" % LOG_PATH)
    records = []
    with open(LOG_PATH, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except ValueError:
                continue
            if since and record.get("ts", "") < since:
                continue
            records.append(record)
    return records


def tier_index(policy):
    return {model: tier for tier, models in policy["tiers"].items() for model in models}


def table(title, counter, total):
    print("\n%s" % title)
    if not counter:
        print("  (none)")
        return
    for key, count in counter.most_common():
        share = 100.0 * count / total if total else 0.0
        print("  %-32s %5d  %5.1f %%" % (key, count, share))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", default=None, help="ISO date, e.g. 2026-08-01")
    args = parser.parse_args()

    records = load_records(args.since)
    with open(POLICY_PATH, encoding="utf-8") as handle:
        policy = json.load(handle)
    tiers = tier_index(policy)

    starts = [r for r in records if r.get("action") == "started"]
    decisions = [r for r in records if r.get("action") in ("rerouted", "kept", "untouched")]

    by_model = collections.Counter(r.get("started_model") or "?" for r in starts)
    by_tier = collections.Counter(tiers.get(r.get("started_model"), "unmapped") for r in starts)
    by_subagent = collections.Counter(r.get("subagent") or "?" for r in starts)
    escalations = collections.Counter(
        r["escalation"] for r in decisions if r.get("escalation")
    )
    reasons = collections.Counter(
        reason.split(" -")[0].split(" exceeds")[0]
        for r in decisions
        for reason in r.get("reasons", [])
    )

    rerouted = sum(1 for r in decisions if r.get("action") == "rerouted")
    oversized = sum(
        1
        for r in decisions
        if any("exceeds budget" in reason for reason in r.get("reasons", []))
    )
    chars = [r.get("prompt_chars", 0) for r in decisions if r.get("prompt_chars")]

    print("routing log: %d decisions, %d subagent starts%s"
          % (len(decisions), len(starts), " since %s" % args.since if args.since else ""))
    table("subagent starts by tier", by_tier, len(starts))
    table("subagent starts by model", by_model, len(starts))
    table("subagent starts by type", by_subagent, len(starts))
    table("escalation signals used", escalations, len(decisions))
    table("reroute reasons", reasons, len(decisions))

    reads = [r for r in records if r.get("action", "").startswith("read")]
    if reads:
        denied = sum(1 for r in reads if r["action"] == "read-denied")
        spent = sum(r.get("est_usd", 0.0) for r in reads if r["action"] == "read")
        saved = sum(r.get("est_usd", 0.0) for r in reads if r["action"] == "read-denied")
        by_file = collections.Counter()
        for r in reads:
            by_file[r.get("path", "?")] += r.get("est_usd", 0.0)
        print("\nlarge reads: %d logged, %d denied, ~$%.2f admitted, ~$%.2f blocked"
              % (len(reads), denied, spent, saved))
        for path, usd in by_file.most_common(5):
            print("  %-52s ~$%.2f" % (path[-52:], usd))

    print("\nhandoff size")
    if chars:
        chars.sort()
        print("  median %d chars, max %d chars, over budget %d"
              % (chars[len(chars) // 2], chars[-1], oversized))
    else:
        print("  (none)")
    print("  rerouted by policy: %d of %d decisions" % (rerouted, len(decisions)))


if __name__ == "__main__":
    main()
