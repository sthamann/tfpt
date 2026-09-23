#!/usr/bin/env python3
"""subagentStart hook: append the model a subagent actually starts with.

Read-only audit trail. Together with the routing decisions in routing.jsonl it
shows whether the enforced model is the one that really ran.
"""

import json
import os
import sys
import time

LOG_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir, "agent-runs", "routing.jsonl"
)


def main():
    payload = json.load(sys.stdin)
    record = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "session": payload.get("session_id"),
        "action": "started",
        "subagent": payload.get("subagent_type"),
        "started_model": payload.get("subagent_model") or payload.get("model"),
        "parallel": payload.get("is_parallel_worker"),
    }
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.stdout.write(json.dumps({"permission": "allow"}))
