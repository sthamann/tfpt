#!/usr/bin/env python3
"""preToolUse hook for the Task tool: enforce the TFPT model-tier routing policy.

Policy lives in model-tiers.json. A subagent gets the cheapest tier that fits its
role; a frontier model is only allowed when the parent prompt names a failure
signal via "ESCALATE: <signal>". Every decision is appended to
.cursor/agent-runs/routing.jsonl for cost forensics.

Fails open: any internal error still allows the tool call unchanged.
"""

import json
import os
import re
import sys
import time

HOOK_DIR = os.path.dirname(os.path.abspath(__file__))
POLICY_PATH = os.path.join(HOOK_DIR, "model-tiers.json")
LOG_PATH = os.path.join(HOOK_DIR, os.pardir, "agent-runs", "routing.jsonl")

TIER_RANK = {"L0": 0, "L1": 1, "L2": 2, "L3": 3}
ESCALATE_RE = re.compile(r"ESCALATE:\s*([a-z0-9-]+)")
UNSET_MODELS = {"", "inherit", "default", None}


def allow(**fields):
    out = {"permission": "allow"}
    out.update({k: v for k, v in fields.items() if v})
    sys.stdout.write(json.dumps(out))
    sys.exit(0)


def log(record):
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
    except OSError:
        pass


def tier_of(model, tiers):
    for tier, models in tiers.items():
        if model in models:
            return tier
    return None


def main():
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input") or {}
    subagent = tool_input.get("subagent_type") or "*"

    with open(POLICY_PATH, encoding="utf-8") as handle:
        policy = json.load(handle)

    if subagent in policy["untouched_subagents"]:
        log({
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "session": payload.get("session_id"),
            "subagent": subagent,
            "requested": tool_input.get("model"),
            "final": tool_input.get("model"),
            "action": "untouched",
        })
        allow()

    tiers = policy["tiers"]
    rules = policy["subagent_policy"].get(subagent, policy["subagent_policy"]["*"])
    prompt = tool_input.get("prompt") or ""

    match = ESCALATE_RE.search(prompt)
    signal = match.group(1) if match else None
    escalated = signal in policy["escalation_signals"]

    cap = "L3" if escalated else rules["cap"]
    requested = tool_input.get("model")
    final = requested
    reasons = []

    if requested in UNSET_MODELS:
        final = policy["tier_default_model"][rules["default"]]
        reasons.append("no model set -> tier %s default" % rules["default"])
    else:
        downgraded = policy["fast_downgrade"].get(final)
        if downgraded:
            final = downgraded
            reasons.append("fast mode costs 2x -> %s" % downgraded)
        tier = tier_of(final, tiers)
        if tier and TIER_RANK[tier] > TIER_RANK[cap]:
            final = policy["tier_default_model"][cap]
            reasons.append(
                "requested tier %s exceeds cap %s for %s%s"
                % (tier, cap, subagent, "" if escalated else " without ESCALATE: <signal>")
            )

    over_budget = len(prompt) > policy["handoff_char_budget"]
    if over_budget:
        reasons.append(
            "handoff prompt %d chars exceeds budget %d - hand over a STATE block, not history"
            % (len(prompt), policy["handoff_char_budget"])
        )

    log({
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "session": payload.get("session_id"),
        "subagent": subagent,
        "requested": requested,
        "final": final,
        "escalation": signal if escalated else None,
        "prompt_chars": len(prompt),
        "action": "rerouted" if final != requested else "kept",
        "reasons": reasons,
    })

    if final == requested and not over_budget:
        allow()

    updated = dict(tool_input)
    updated["model"] = final
    message = "Routing policy: model=%s. %s" % (final, "; ".join(reasons))
    allow(updated_input=updated, agent_message=message)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # fail open, never block the parent agent
        log({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "action": "hook-error", "error": str(exc)})
        sys.stdout.write(json.dumps({"permission": "allow"}))
