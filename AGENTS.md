# Working in TFPT

## Start with the actual task

This repository owns physical TFPT, its compiler mathematics and its stated
physical interfaces. Prime-number, RH, Weil-window and factorisation research
belongs to [Prime Front](https://github.com/sthamann/prime-front). Do not
reintroduce its modules, registries or runtime dependency into TFPT.

1. Read `README.md` and the central `docs/registry/INDEX.md`.
2. Read the compact `docs/registry/summary.json` or use
   `python3 verification/make_content_registry.py --query "topic"` to locate
   a document, topic, editable
   module and its cited verification/formal sources. The complete
   `registry.json` is a large machine graph: query it in bounded slices rather
   than loading it wholesale into an agent context. Read the original
   statements; registry links alone do not establish a proof.
   Read `docs/SEMANTIC_NAVIGATION.md` for coverage limits and the next-session
   route. In the local Atlas use `paper_coverage`, `search_papers`/`list_papers`,
   `paper_outline`, `paper_section`, `paper_evidence` and `read_source` before
   joining the exact question to `research_state`. Source-grounded AI summaries
   remain `reviewed:false`; check freshness, incomplete states and scope.
   Structural/AI coverage is not curated scientific review; a missing reviewed
   Atlas match is not evidence that a scientific question is open. Paper search
   defaults public; explicitly include local/private material only for local work
   and never copy it automatically into public artifacts.
3. Read the relevant `.cursor/rules/` and any nested `AGENTS.md` that applies
   to the files being changed. Current user instructions take precedence.
4. Inspect the working tree. Preserve unrelated staged, modified, untracked
   and ignored research. Never reset working files or broadly add another
   research session's results.

## Source ownership and document editing

- `documents/` contains the editable modules of the modularized documents.
  Existing `.tex` entry points retain their names for compilation and stable
  PDF URLs. Follow the owning module path in the registry instead of putting
  new chapters into a thin entry point.
- `tex-artefacts/` owns shared style, notation, common references and reusable
  fragments. Shared material has one owner; do not paste a copy into each paper.
- `docs/registry/` is a generated navigation layer. Its documented configuration
  owns curated descriptions/topic rules; the generator owns inventories,
  source locations and reverse links. Regenerate rather than editing outputs.
- `verification/status_ledger.csv` owns claim status. `run_all.py` and the
  script registry own the registered executable suite. Exploratory scripts
  stay under `experiments/` until an explicit reviewed promotion.
- Actual `.lean` statements and `.wl` code own their formal/computational
  scope. Keep hypotheses, axiom dependencies and open obligations explicit.
- `website/` and generated TeX/CSV/TypeScript indices are derived surfaces.
  Update them through the documented generators in the same change.
- Documentation-only source organization/tooling changes belong in
  `docs/CHANGELOG.md`; scientific/publication changes belong in the modular
  paper changelog. Do not change scientific history merely to record a file move.
- `_archive/` is historical. Do not silently rewrite a historical verdict to
  match a later result. Make the dated scope and current source clear.

When splitting or moving text, preserve ordering, macro definitions, labels,
reference keys and mathematical content. Use the shared TeX include reader
for tooling; do not regex only a root wrapper or invent another include
expansion implementation. Keep include cycles and missing required sources
as errors. Generated/optional build artifacts must be identified explicitly.

## Find code and research without conflating them

Prefer `codebase-memory-mcp` for code discovery:
`search_graph`, `trace_path`, `get_code_snippet`, `query_graph`, `search_code`.
Index an unindexed project first. Use targeted text search for literals,
configuration, non-code sources, or insufficient graph coverage.

For TFPT/Universalraum research, first read the complete available whole-system
entry map and the `tfpt-knowledge` skill. On the maintained local installation:

- `/Users/stefanhamann/.codex/context/tfpt-gesamtkontext.md`
- `/Users/stefanhamann/.codex/skills/tfpt-knowledge/SKILL.md`
- repository `semantic_explorer/skills/tfpt-knowledge/SKILL.md`, when present.

Use `tfpt-knowledge` as the sole current theory-atlas interface. Start with
`graph_status` and `theory_overview`, then query the actual question with
`research_state`. Use exact problem/strategy/premise IDs with
`assess_research_plan` before repeating a recorded approach. Load bounded
original sources through the research context/dossier/source tools. Persist
source-reviewed research changes through `record_research_update` using its
revision check. Keep current source freshness and review coverage visible.

The local Atlas may not be included in a public checkout. If unavailable,
use the registry, ledger and original sources and state that the current
local decision state was not consulted. Do not replace it with the retired
`verification/theory_graph.json` or `theorycat.py`. The code graph, content
registry and research Atlas serve different purposes.

## Scientific discipline

- Preserve the complete connected TFPT structure: inputs, compiler/E₈,
  Standard Model/flavor, alpha, clocks, quantum/boundary structure, gravity,
  consistency and the source question. Do not reduce it to the last model gap.
- Distinguish declared input, exact consequence under assumptions, numerical
  observation, conditional physical identification and open derivation.
  Ledger status and original sources prevail over prose summaries.
- Matching numbers or dimensions do not establish an operator dictionary.
  Check actual group actions, charges, grading, adjoints and composition.
- Name the first additional geometry, metric, state, coupling, calibration
  or selection rule. A working chosen model does not derive that choice.
- Before expensive work, perform the smallest decisive structural test.
  New models need a concrete question, success criterion and stopping rule.
- Keep conjunctive prerequisites together. Common seeds are correlated
  evidence; necessary conditions are not automatically sufficient.
- Preserve scoped negative results. Revisit a failed route only after naming
  the changed premise. Do not promote a finite check, source index or source
  consistency audit to a physical or all-case proof.
- Reconstruct the requested outcome and work toward it. Fix the existing
  consumer path; do not substitute a growing collection of reports or models.

## Validation and integration

Read `docs/LATEX_MAINTENANCE.md` for precise commands and generated outputs.
For a structural document change:

1. Verify expanded source preservation and the affected include/consumer tests.
2. Regenerate the content registry, existing maps and document indices.
3. Compile affected PDFs from their documented directory; check errors,
   missing references and visible layout regressions. A TeX exit code alone
   does not show that every reference is resolved.
4. Refresh website/download mirrors; run `bash build.sh audit` and the website
   production build when its content or inputs changed.
5. Generate manifests last and run their `--check` mode. Ensure exports contain
   all modular sources and their shared inputs.

For a scientific or executable change, run the actual affected verification
and its meaningful negative control before editing its paper/ledger/status.
Report the exact result first. Broaden tests when changes or unresolved
failures justify it. Full numerical, Lean and Wolfram runs are separate;
report unexecuted checks honestly. Independently review material physics,
learning/restore and response-path changes once at the relevant diff.

Do not hand-edit generated `verification.tex`, document maps, script index,
changelog data, website version metadata or generated Atlas data. Do not
silently add audit-baseline exceptions to make a refactor pass.

## Collaboration and delivery

Use bounded, task-specific delegation when helpful. Follow the applicable
agent-routing skill within available runtime tools; Cursor model names,
hooks and AgentStores are not automatically available in Codex. Preserve
existing ownership and avoid duplicate writers. Hand over a compact state
with goal, exact files/interfaces, verified results, failures and next action.
No cost/reservation gate is a prerequisite for a local diagnosis or repair.

Communicate the outcome in clear language. Keep progress updates about the
next real uncertainty or repair. Report what changed, what actually passed,
what remains unverified and any concrete blocker. Do not ask again for an
already authorized reversible step. Publishing/merging follows the user's
actual authorization; a local rule does not invent a second approval flow.
