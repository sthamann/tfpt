# RH research freshness and source review

Research documentation only. **NO RH CLAIM.**

The legacy inventory, an external working research folder, the semantic
catalog, the concept map and the viewer are different layers. A legacy
`CATALOG CHECK OK` checks registered records; it does not mean every new
experiment in another folder has been found or adjudicated.

## Explicit workflow

From the TFPT repository, using its existing discovery Python:

```sh
experiments/tfpt-discovery/.venv/bin/python -B rh/catalog/sync_research.py --check
experiments/tfpt-discovery/.venv/bin/python -B rh/catalog/sync_research.py --refresh
```

`--check` is read-only. It discovers the declared external scope, compares
all file hashes, verifies source-review pins, and checks the exact built
catalog, concept map, viewer data, compiled viewer and exports. Missing
sources are an explicit failure, not an empty successful scan.

`--refresh` discovers new groups as **needs-review drafts**, builds all
layers offline, runs the export consistency checks, and issues a receipt
only if the inputs stayed unchanged. This runner itself does not use an LLM,
embeddings API or external upload. The Codex RH heartbeat calls the entry point
periodically and performs bounded agent-led research. Its enabled state is in
the Codex automation, not inferred from these files. No assertion is made that
Codex invokes Cursor's `afterFileEdit` hook.

The registered scope is in `external_sources_config.json`: this task's
`research`, `work` and `outputs` trees. It is not every Codex task or every
TFPT experiment on the computer. A campaign is one record; all its original
files, frozen variants, results and full search databases are linked and
hashed in `external_sources.json`, without duplicating them into `rh/`.
Only cache, dependency and version-control components listed in the config
are excluded. Absolute original paths are intentional and require access
to the original workspace; an absent workspace fails the freshness check.

## Semantic review is a separate, human/agent action

1. Read the original source and its exact limits; compare existing kills.
2. Explicitly pin the reviewed group with `--record-review GROUP_ID`.
   This records attribution review, **not independent mathematical review**.
3. Add a curated `fragments/part_*.json` entry at that group's primary path,
   and immediately rebuild the catalog before proceeding to other edits.
4. Refresh the bundle and run the read-only check.

Refresh never records a review for you. If any file in a reviewed group
changes, it refuses to bless the new source. Reconcile the actual changes,
then explicitly re-record the review; never use this merely to silence
an error. Adding a path/hash is not a sealed-probe promotion: legacy
`rh/INVENTORY.json`, the sealed suite, the verification ledger, papers and
Lean statuses are unchanged by this process.

`research_status.json` reports coverage and pending reviews. `research_refresh_receipt.json`
pins the complete delivered bundle. Old PNG screenshots in `_newest/graph`
are preserved but named as **stale**, excluded from the fresh receipt.
Current JSON/CSV/GraphML/DOT/SVG files and the compiled viewer are rebuilt.
The simple SVG export is a schematic export, not a new interactive screenshot.

## Consuming the graph in follow-up work

Run the freshness check first, query the catalog and gaps, then read the
sources of the few relevant nodes. Never interpret the navigation path
finder as a theorem prover: it traverses relevant relations in both
directions. `alive` means linked reusable/non-killed material, not a working
RH mechanism. AND-connected proof obligations are in
`analysis/research_followups_20260909.json`; all currently remain OPEN.

The executable, source-bound supplement is now `proof_search/`: its broad
Lean registry, freshly kernel-checked conditional adapters and bounded
AND/OR planner are included in refresh/check. Run `search_rh.py audit` once
before refresh, and again when an applied Lean source or adapter changes.
Refresh never fabricates or silently renews that proof receipt. Corrected
ARCH interpolation, existential rate and per-test convergence are reusable;
the old prescribed constant remains refuted. FREQ, native positivity and
complete Gabor positivity remain open. See `proof_search/README.md` for
the exact command sequence and finite/global trust boundaries.

Tests: `python -B -m unittest discover -s rh/catalog -p test_research_sync.py`.
Repeat with `-OO`; no acceptance condition relies on disabled assertions.

## Verification boundary on 9 September

The synchronization regressions cover source additions, changes, deletion,
unavailable roots, frozen-source retention, no automatic promotion, explicit
review invalidation, source/contract dependency direction and unrelated
README-name collisions. Genuine shared-ledger conflicts remain detectable.
The latter two fixes followed a failing regression and a minimal correction.

The existing viewer production build succeeds. A separate `tsc --noEmit`
reports five pre-existing diagnostics in unchanged `src/data.ts`,
`src/export.ts` and `src/matrices.ts` (the files match the current git HEAD).
This refresh does not claim a clean whole-viewer TypeScript check or a new
browser-interaction test. It checks exported data and builds the viewer;
no server or unattended process is started.

## Paper coverage and adaptive research

`research_cycle.py cycle` wraps this refresh, indexes the declared source scope
and prepares a diverse queue with exact-object result history. Hash-bound paper
annotations, unreviewed theorem-like environments and a section review queue
are exported as `paper_claims.json`. Lexical extraction is not a complete TeX
parser or a semantic review. The persistent `rh-graph-research` Codex skill
requires current provenance and source inspection before research. See
`research_engine/README.md` for the creative submission and result contracts.
