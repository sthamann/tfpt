# Paper semantics, source navigation and research review

The central registry locates all **6,693 public section records** with exact
source spans, excerpts, document ownership and typed references. The local
Knowledge Atlas adds dedicated paper search, outlines, section descriptions and
evidence tools using those same IDs. Its source-grounded AI summaries and the
Atlas's curated scientific reviews remain different layers.

| Layer | What it supplies | What it does not establish |
|---|---|---|
| [Content registry](registry/INDEX.md) | Exact editable source spans, includes, explicit citations, lexical topics and bounded queries | Semantic review or proof validity |
| Atlas paper layer | Full-body source search and, when complete/current, AI summaries of concepts, assumptions, results and limits | Curated review, a new ledger verdict or a proof |
| Curated Atlas research state | Source-reviewed findings, scoped problems, prerequisites and recorded decisions | Automatic review of every paper section |
| Original ledger and formal sources | Original status; exact Lean statements, hypotheses and axiom dependencies | A broader conclusion inferred from a graph edge or finite check |

## Check actual coverage

Use live `paper_coverage` for paper-specific inventory and semantic processing.
It distinguishes expected/imported sections; `complete`, `pending`, `error`,
`stale` and `source_error`; public/private scope; documents/physical sources;
and current/total chunks. Complete inventory alone is not complete AI coverage.
Only source-current, validated AI summaries/quotes covering every bounded chunk
of the full source body count as complete. Even `semantic_complete: true` leaves
the AI annotations `reviewed:false`: it does not certify scientific correctness.
Check source freshness separately from `context_state` (`current`, `stale`,
`incomplete`): a complete available-body summary can lack original document
prerequisites. Coverage exposes stale and incomplete context separately. Exact
quotation spans establish where text came from, not that the summary follows
from those quotations.

Consult `graph_status` separately for curated research review, other annotation
caches and semantic-vector availability. A stale source requires re-extraction,
not a scientific status reversal. Vector availability is not a percentage of
proved or reviewed science. Missing reviewed coverage does not establish that
the scientific question is open.

The earlier structural-only corpus snapshot on **2026-10-18**, before this paper
layer, had 1,084 `paper_section` records with structural summaries and no reviewed
section nodes. The same dated service observation reported 156 curated findings,
16 problems, zero stale curated findings, a separate stale AI claim cache
(778/788), and partial vector availability (7,580/43,887 in that subsystem).
These describe separate historical layers and denominators; none is a current
paper-completion or scientific-validity score. Use live tools after each import.

## Route for the next session

1. Start with `graph_status` and `theory_overview`, then `paper_coverage`.
2. Use `search_papers(query, scope="public", limit=5)` or `list_papers` to find
   the document or phrase. For example, search `carrier_rank_pascal_unique`.
3. Copy the returned exact `document:` ID into `paper_outline(document_id)`.
   Copy the relevant exact `section:` ID into `paper_section(section_id)`.
   Read its summary state, source freshness, parent context and every premise.
4. Use `paper_evidence(id)` to follow typed evidence links, then `read_source`
   with the returned `source_id` and bounded inclusive line ranges. Original
   source reads are hash checked and limited to 200 lines per call. Continue
   across ranges when the complete section or prerequisites require it.
5. Use `research_state` for the exact topic/problem or actual scientific
   question. Preserve its findings, strategies and conjunctive premise IDs;
   follow the existing plan/update discipline before retrying a strategy or
   recording a source-reviewed result.
6. Check the [original ledger](../verification/status_ledger.csv), cited proof
   and actual Lean/Wolfram scope. Finding a theorem does not execute Lean;
   report a kernel, script or Wolfram run only when it actually occurred.

Paged paper tools return totals, offsets, omissions, continuation and character
budgets. Follow `next_offset` and `budget.truncated`; a bounded sample is not
the entire corpus. A section response has no offset: use its source references
to retrieve omitted original context. Lexical topics, identifier joins, explicit
citations and logical derivations keep their distinct relation types.

The canonical shared skill documents exact argument defaults in
`semantic_explorer/skills/tfpt-knowledge/references/papers-navigation.md` on the
local installation. Reconnect an old MCP client if its catalog lacks
`list_papers`, `search_papers`, `paper_outline`, `paper_section`, `paper_evidence`
or `paper_coverage`; do not replace a missing tool with a whole-graph dump.

## Public, private and historical material

List/search default to public records. `scope="local_private"` (alias `private`)
explicitly selects private records; `scope="all"` includes both. Exact-ID reads
can access an explicitly known private record and retain its scope labels.
Historical, archive, support and exploratory material remain marked rather
than being presented as current scientific conclusions.

Private paper inputs and semantic caches belong only in the local ignored
Atlas. Public importing does not consult private records/cache. Do not copy
private sources, summaries or the complete private overlay into a public
registry, website download or publication. A public checkout can use bounded
registry queries and original sources when the local Atlas is unavailable:

```sh
python3 verification/make_content_registry.py --query 'carrier_rank_pascal_unique' --limit 2
python3 verification/make_content_registry.py --document origin_theory --limit 5
```

## What reviewed semantics still requires

AI descriptions make paper content retrievable beyond headings and lexical
topics. Scientific review still requires checking each load-bearing summary's
conclusion, assumptions and limits against its original source and justifying
its typed relations. Only that source review can support a curated finding or
research-state update; an import must not promote the ledger automatically.

See [agent instructions](../AGENTS.md), [relation semantics](registry/RELATIONS.md)
and [LaTeX maintenance](LATEX_MAINTENANCE.md) for the operational boundaries.
