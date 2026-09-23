---
name: agent-routing
description: >-
  Route TFPT agent work by cost tier, hand off state instead of history, and escalate only on a
  named failure signal. Use when spawning subagents, planning a deep-sync or experiment round,
  handing a task to a fresh agent, when a session grows long, or when reviewing model spend in
  .cursor/agent-runs/routing.jsonl.
---

# Agent routing & context budget

Always-on ladder and stop rules: rule **`agent-economics`**. This skill holds the per-task mapping,
the handoff templates and the spend review.

Architecture: **cheap models produce artefact + evidence, an expensive model checks the one decision
that matters.** That is the same proof-carrying pattern the repo already uses for `verification/` —
a worker emits numbers, the ledger decides what they mean.

## Tier by TFPT task

| Task | Tier | Model |
|---|---|---|
| Enumerate surfaces from `docs_map.csv` / `website_map.csv` | L0 | `composer-2.5-fast` |
| Grep stale wording, old gate ids, status markers | L0 | `composer-2.5-fast` |
| Run `run_all.py` / `build.sh audit`, report pass-fail | L0 | `composer-2.5-fast` |
| Summarise a diff, fix lint/type errors, apply a decided rename | L0 | `composer-2.5-fast` |
| Audit-fix loop (parse failures, iterate until green) | L1 | `cursor-grok-4.6-xhigh` |
| Website mirror edits (`papers.ts`, status components) | L1 | `cursor-grok-4.6-xhigh` |
| Implement `verification/vN_*.py` from a specified formula | L1 | `cursor-grok-4.6-xhigh` |
| Paper prose that carries a claim or a `\veri{}` placement | L2 | `gpt-5.6-sol-high` |
| Experiment design: frozen kernel, null battery, surrogate calibration | L2 | `gpt-5.6-sol-high` |
| Debugging with no obvious cause after two L1 attempts | L2 | `gpt-5.6-sol-high` |
| RH round interpretation, Lean statement design | L2 | `gpt-5.6-sol-high` |
| `[E]` vs `[C]` call, ledger status move, contradictory numbers | L3 | `claude-opus-5-thinking-high` |

L3 is a **judge**: it receives a finished artefact plus evidence and answers one question. It never
searches, never edits files, never runs the suite.

L1 alternatives to `cursor-grok-4.6-xhigh`: `muse-spark-1.3-max`, `kimi-k3-max`, `glm-5.2-high`
(same tier, same caps — pick any).

## Handoff: STATE block, not history

Every subagent prompt and every checkpoint uses this, filled with facts only:

```text
GOAL          one sentence, the outcome that ends the task
HYPOTHESIS    current best explanation, or "none"
VERIFIED      numbers with their source (script id, ledger row, SPEC_SHA) — no recollection
FILES         paths touched or to touch, ≤ 20
SUITE         run_all.py / build.sh audit / npm build state, last known
FAILED        attempts already ruled out, with the reason each failed
NEXT          the single next action
```

Rules: no transcript excerpts, no tool logs, no "as discussed above". If the block cannot be written,
the task is not understood well enough to delegate. Above 60k chars the hook flags the handoff.

## Escalation

Escalate only after a measurable failure, one tier at a time, and name the signal in the prompt:

```text
ESCALATE: numeric-disagreement

GOAL ...
VERIFIED v9xx reports 0.834; the Wolfram readout reports 0.827 …
FAILED   recomputed both with the same constants — difference persists
NEXT     decide which implementation is authoritative
```

Valid signals live in `.cursor/hooks/model-tiers.json`. Anything else is downgraded by the hook.
Ceiling: **2 L3 calls per task**. Beyond that, stop and hand the STATE block to the user.

## Log and repo context reduction

Never feed raw output to a model. Reduce at the shell:

```bash
python verification/run_all.py 2>&1 | rg -n "FAIL|ERROR|ALL CHECKS PASSED"
bash build.sh audit          2>&1 | rg -n "FAIL|ERROR|WARN|AUDIT OK"
latexmk … 2>&1               | rg -n "^!|Overfull|Undefined|Warning"
npm run build                2>&1 | rg -n "error|Error|✓|failed"
```

Exact numbers for the *summary before edits* rule come from running the single `vN_*.py` module
standalone — not from scrolling the suite log. Terminal files already hold the full output if needed.

Repo context: `grep → select → read`. Start from `docs_map.csv` / `website_map.csv` rather than
reading papers; read `.tex` with `offset`/`limit` around the mapped line range.

The read guard enforces the ceiling: ≥ 120k chars is admitted but priced in the log, ≥ 400k chars is
refused. When it fires, do not look for a workaround — grep for the lines that matter, page the file,
or reduce it at the shell. Only a file that genuinely has to be read whole justifies raising
`read_budget.deny_chars` in `.cursor/hooks/model-tiers.json`.

## Deep-sync and experiment rounds

- Deep-sync (`tfpt-deep-sync`): all enumeration subagents are L0, the audit-fix `shell` subagent L1.
  The parent merges checklists and does the load-bearing edits.
- Experiments (`tfpt-experiment`): probe scaffolding and reruns are L0/L1; only the statistical design
  and the verdict interpretation are L2.
- RH rounds (`rh-sync`): INVENTORY, `run_rh.py` and README sync are L0; Lean statement design is L2.

## Spend review

```bash
python3 .cursor/hooks/routing_report.py          # tier mix, reroutes, oversized handoffs
python3 .cursor/hooks/routing_report.py --since 2026-08-01
```

Healthy shape: L0+L1 carry the large majority of spawns, L3 appears only with an escalation signal,
and no rerouted line reads "no model set" repeatedly — that means the parent is not choosing tiers.

## Never

- Spawn with `inherit`, or let a frontier model do enumeration, greps or suite runs
- Pass conversation history, full logs, or whole papers into a subagent prompt
- Escalate without a signal, or invent a signal to get past the hook
- Hand-edit `.cursor/agent-runs/routing.jsonl`
- Keep grinding after the stop rules in `agent-economics` fire
