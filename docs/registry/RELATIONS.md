# Reading the content registry

Use [summary.json](summary.json) or [INDEX.md](INDEX.md) first. The complete
[registry.json](registry.json) is a source graph for bounded queries; agents
should not load it wholesale. It is the one generated authority for these
navigation views. The compact summary, topic pages and reverse indexes derive
from it.

The registry answers **where a topic is discussed and which source objects are
actually named there**. It does not answer whether a mathematical argument is
correct. It runs neither Python verification nor Lean nor Wolfram.

| Relation | What was observed | What is not asserted |
|---|---|---|
| `explicit_file_citation` | A literal filename/path in TeX resolves to one local source. Escaped underscores and typesetting breaks are normalized. | That the cited file proves the surrounding statement. |
| `explicit_script_identifier` | A short `vN` resolves uniquely to the canonical local verification registry entry. | That an experiment snapshot with the same basename owns the registry status. |
| `explicit_claim_identifier` | The exact claim identifier occurs in the local ledger. | A new or stronger status. `status_as_recorded` and `canonical_status_as_recorded` are copied unchanged. |
| `explicit_lean_symbol` | An exact named declaration occurs as a code token under Lean/theorem context; a cited module may disambiguate it. | A match between the manuscript's mathematical statement and the declaration type. |
| `explicit_source_identifier` | Lean source/comments or a Wolfram section heading explicitly name a Python identifier. | A full independent mirror, proof equivalence or successful execution. |
| `cross_reference_join` | A TeX section and a Lean module/Wolfram section name the same Python identifier. | A direct manuscript citation to that theorem or an equivalence of statements. |
| `contains_declaration` | The literal named Lean declaration is in the named module. | A manuscript-to-theorem proof link. Containment does not count as a TeX citation. |
| `includes_source` | A literal TeX include is recorded in a source's `includes` list. | TeX macro/conditional execution. Both literal branches can remain visible to the static reader. |
| `lexical_topic_suggestion` | A curated expression matches the path, heading or opening excerpt. | Reviewed thematic ownership or proof relevance. |

Each physical TeX section is stored once, with one-based inclusive line ranges
and zero-based, end-exclusive UTF-8 byte ranges. A document view contains an
ordered list of those section IDs. Shared support can appear in several views
without duplicating the section body. Legacy wrappers are aliases, not a second
copy of the content. The modular ownership record retains the original source
spans as migration provenance; current physical positions remain separate.

Opening excerpts strip presentation commands and explicitly replace formula
spans with `[formula in source]`. This avoids turning a fraction into a
different integer when formatting is removed. They are excerpts, not semantic
summaries. Exact statements and mathematical titles remain in the source;
`title_latex_as_written` retains the literal title, while document navigation
uses short curated titles or safe filename fallbacks.

Lean records retain literal declaration signatures, named hypotheses, module
variable/axiom context and detected `sorry`/`admit` tokens. These are static
observations. A declaration without those tokens has **not** thereby been
kernel-checked, shown axiom-free or matched to a physical interpretation.
Wolfram records retain actual comment headings and check labels; no execution
result is inferred from them.

The canonical Python status owner is `verification/<script>.py` plus the local
ledger. Source snapshots and shared copies retain their own paths and do not
inherit a ledger status just because they have the same filename. Explicit
shared-project ownership notes distinguish the scoped TFPT copies from the
independent Prime Front research.

Files under `verification/historical_replay/` are explicitly typed
`historical_source_snapshot`, with role `historical_snapshot`, empty current
claim IDs and `current_proof_coverage: false`. The replay manifest names the
frozen inputs and their original provenance. A saved ledger CSV is catalogued
as a source file; its rows are never imported into the current claim ledger.
Historical replay success and separate current-module checks remain different
observations.

The research-evidence inventory excludes website mirrors and root editor/agent
configuration directories (`.cursor`, `.codex`, `.agents`, `.claude`, `.github`).
Those development tools are intentionally absent from the Overleaf export;
they are not manuscript or proof sources. The authored TeX inventory has its
own complete scope. Gitless exports use the shipped research inventory, require
every declared research file to exist, and hash its actual bytes. Missing
research evidence is an error rather than a reason to reduce coverage silently.

Only `--include-local` may omit a noncanonical tool/data file that Git explicitly
records as deleted in the working tree. Each omission is named in the local
supplement's diagnostics as `local_missing_noncanonical_evidence`. Registered
verification modules, Lean/Wolfram sources, required TeX and the active ledger
remain mandatory. Public generation and Gitless export validation never use
this local working-tree exception.

Diagnostics carry two dimensions: `origin_scope` distinguishes active document
content, dated records, archives, explorations and support; `resolution_scope`
distinguishes known external Prime Front ownership, ambiguous local targets and
unresolved local/historical references. These are source-navigation findings,
not mathematical verdicts. Known external ownership comes from
`verification/project_scope.json`. No sibling-project proof or status is
imported. Evidence without a TeX citation is listed explicitly; an unlinked
proof is not the same thing as a missing or invalid proof.
