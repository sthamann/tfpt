# Semantic navigation and coverage

All **6,693 registry section records** have structural navigation: physical
source locations, source excerpts, document ownership and lexical topic hints.
They do **not** all have reviewed summaries of their mathematical content or
reviewed links explaining how their arguments depend on one another. The
registry and the local Knowledge Atlas serve different purposes.

| Layer | What it supplies | What it does not establish |
|---|---|---|
| [Content registry](registry/INDEX.md) | Exact editable source spans, opening excerpts, includes, explicit citations and bounded topic queries | Complete semantic understanding, reviewed conclusions or proof validity |
| Local Atlas corpus | Searchable source context and structural section/theorem/formula records | A reviewed interpretation of every section |
| Curated Atlas research state | Source-reviewed findings, scoped problems, prerequisites and recorded decisions | Coverage of the whole corpus or a proof beyond each record's stated scope |
| Original ledger and formal sources | Original claim status; exact Lean statements, hypotheses and axiom dependencies | A broader conclusion inferred from a filename, graph edge or passing finite check |

## Observed coverage on 2026-10-18

These are dated navigation/service observations, **not scientific coverage or
completion percentages**. Consult live `graph_status` for subsequent sessions.

- The local corpus snapshot contains **1,084 `paper_section` nodes**. All use
  the structural-only section summary; none has `reviewed: true`. The Atlas
  `parse_tex` extractor explicitly creates section headings with structural
  summaries and `reviewed: false`. The service composes this corpus with its
  other data; the base knowledge file alone has no `paper_section` records.
  Its section count and granularity differ from the registry's physical records.
- `graph_status.meta.research_program` reports **156 reviewed findings,
  16 reviewed problems and zero stale reviewed findings**. This describes that
  curated subset, not all sections or all scientific questions.
- The separate AI claim-annotation cache reports **778 stale annotations out
  of 788**. Those unreviewed interpretations are distinct from the curated
  findings; their cache state does not change the original ledger verdicts.
- The semantic-search subsystem reports **7,579 existing graph vectors plus
  one hydrated vector for 43,887 nodes in its reported denominator**, about
  **17.3%**. That measures partial vector availability, not source review or
  mathematical validity. The overall service node count is a different metric.

The extractor's own wording is “semantic status is structural only.” Neither
regex topic suggestions nor embeddings supply missing reviewed semantics.

## Route for the next session

1. Start with [the compact registry](registry/summary.json) and a bounded query:

   ```sh
   python3 verification/make_content_registry.py --query 'carrier_rank_pascal_unique' --limit 2
   python3 verification/make_content_registry.py --document origin_theory --limit 5
   ```

2. Read the exact original section, its parent context and every stated premise.
   Follow its owning document/include chain; an isolated excerpt can omit a
   condition or an earlier definition.
3. When the local Atlas is available, start with `graph_status` and
   `theory_overview`, then use `research_state` for the exact topic or problem.
   Preserve the resulting problem, finding, strategy and conjunctive premise
   IDs. A missing reviewed match can mean missing review coverage; it does
   **not** establish that the scientific question is open.
4. Check the [original ledger](../verification/status_ledger.csv), cited source
   and actual Lean/Wolfram scope. Read the Lean theorem's hypotheses and axiom
   dependencies. Finding a theorem is not a fresh kernel run; report execution
   only when it actually occurred.

For example, registry retrieval can locate the physical `origin_theory`
section discussing `carrier_rank_pascal_unique`; Atlas search can locate the
corresponding Lean proposition. These are complementary retrieval results,
not a new proof or a fresh Lean execution.

## Remaining semantic work

Complete section-level semantics would require reviewed summaries stating each
section's conclusion, assumptions and limits, together with justified typed
relations to original evidence and other sections. Those reviews need exact
source provenance and freshness. This work remains incomplete; lexical matches
must remain navigation suggestions rather than being relabelled as reviewed
scientific relationships.

See [the agent instructions](../AGENTS.md), [relation semantics](registry/RELATIONS.md)
and [LaTeX maintenance](LATEX_MAINTENANCE.md) for the operational boundaries.
