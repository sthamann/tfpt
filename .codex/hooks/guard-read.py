#!/usr/bin/env python3
"""beforeReadFile hook: keep single reads from flooding the context window.

A one-shot read of a very large file is charged once and then re-charged on every
following turn of the session. Above the deny threshold the read is refused with an
instruction to grep or to page with offset/limit. Large-but-allowed reads are logged
with an estimated input cost for the model that is about to receive them.

Thresholds and prices: model-tiers.json. Fails open on any internal error.
"""

import json
import os
import sys
import time

HOOK_DIR = os.path.dirname(os.path.abspath(__file__))
POLICY_PATH = os.path.join(HOOK_DIR, "model-tiers.json")
LOG_PATH = os.path.join(HOOK_DIR, os.pardir, "agent-runs", "routing.jsonl")
CHARS_PER_TOKEN = 4.0


def emit(payload):
    sys.stdout.write(json.dumps(payload))
    sys.exit(0)


def log(record):
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
    except OSError:
        pass


def price_for(model, prices):
    for key in sorted(prices, key=len, reverse=True):
        if key != "default" and model.startswith(key):
            return prices[key]
    return prices.get("default", 3.0)


def main():
    payload = json.load(sys.stdin)
    content = payload.get("content") or ""
    size = len(content)

    with open(POLICY_PATH, encoding="utf-8") as handle:
        policy = json.load(handle)
    budget = policy["read_budget"]

    if size < budget["log_chars"]:
        emit({"permission": "allow"})

    path = payload.get("file_path") or "?"
    model = payload.get("model") or "?"
    tokens = size / CHARS_PER_TOKEN
    usd = tokens / 1e6 * price_for(model, policy["input_usd_per_mtok"])

    record = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "session": payload.get("session_id"),
        "action": "read",
        "path": os.path.relpath(path, os.getcwd()) if path.startswith(os.getcwd()) else path,
        "chars": size,
        "est_tokens": int(tokens),
        "est_usd": round(usd, 3),
        "model": model,
    }

    if size >= budget["deny_chars"]:
        record["action"] = "read-denied"
        log(record)
        emit({
            "permission": "deny",
            "agent_message": (
                "Read blocked by context budget: %s is %d chars (~%dk tokens, ~$%.2f on %s). "
                "Grep for the relevant lines first, then read with offset/limit, or reduce the "
                "file at the shell. Raise read_budget.deny_chars in .cursor/hooks/model-tiers.json "
                "if this file genuinely has to be read whole."
                % (record["path"], size, tokens / 1000, usd, model)
            ),
            "user_message": "Blocked a %dk-char read (~$%.2f) — context budget." % (size / 1000, usd),
        })

    log(record)
    if size >= budget["warn_chars"]:
        emit({
            "permission": "allow",
            "agent_message": (
                "Large read: %s, ~%dk tokens (~$%.2f). It stays in context for every following "
                "turn — prefer offset/limit or a grep next time." % (record["path"], tokens / 1000, usd)
            ),
        })
    emit({"permission": "allow"})


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        log({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "action": "hook-error", "error": str(exc)})
        sys.stdout.write(json.dumps({"permission": "allow"}))
