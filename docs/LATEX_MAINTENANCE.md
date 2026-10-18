# Maintaining the LaTeX sources and content registry

Start with [the registry index](registry/INDEX.md) or its small
[summary.json](registry/summary.json). Use a bounded query to locate the actual
owner before editing:

```sh
python3 verification/make_content_registry.py --query 'Pascal' --limit 10
python3 verification/make_content_registry.py --topic e8-geometry --limit 10
python3 verification/make_content_registry.py --document introduction --limit 20
python3 verification/make_content_registry.py --query 'carrier_rank_pascal_unique' --json --limit 5
```

The full `docs/registry/registry.json` is generated. Its physical source spans,
explicit cross-references, original ledger statuses and reverse indexes are
navigation aids. The [relation guide](registry/RELATIONS.md) explains their
limits. Do not treat a file link, lexical topic hit, declaration name, source
hash or passing source-integrity check as a mathematical proof.

## Where changes belong

| Location | Owner and purpose |
|---|---|
| Legacy root `.tex` and selected archived entry points | Thin compatibility wrappers. Compile from the original directory; do not restore a second monolithic body here. |
| `documents/<id>/main.tex` | Ordered include manifest for that document. |
| `documents/<id>/preamble.tex` | That document's original preamble and title setup. |
| `documents/<id>/sections/*.tex` | The actual authored section/body owners. Edit the relevant module once. |
| `tex-artefacts/tfpt_style.tex`, `tfpt_figures.tex`, `tfpt_status.tex`, `tfpt_references.tex` | Shared styles, reusable figures, status notation and references. A change affects every consuming document view. |
| `tex-artefacts/verification.tex`, `predictions.tex` | Generated tables. Edit their owning registry/data or generator, then regenerate. |
| `experiments/`, `universal_room/`, `articles/` | Authored exploratory and research documents. Their inclusion records content, not publication or a status upgrade. |
| `_archive/` | Historical authored sources. Keep snapshots and frozen records unchanged; record corrections in a new owning source. |
| `verification/script_registry.csv`, `status_ledger.csv` | Canonical local module inventory and original claim statuses. Shared/sibling copies do not take ownership of these rows. |
| `experiments/lean4-carrier-rigidity/` | Lean modules and exact named declarations; inspect assumptions and actual kernel results separately. |
| `verification/wolfram/` | Independent-language source sections and bounded check labels; inspect their stated coverage. |
| `documents/source_manifest.json` | Modular source ownership and original contiguous byte/line spans. This is migration provenance, not a new proof. |
| `docs/registry/config.json` | Small curated topic taxonomy, active entry points, explicit public additions and shared-source ownership notes. |
| `docs/registry/source_inventory.json` | Generated public path inventory, also used by Gitless/Overleaf exports. |

Use `verification.tex_sources.source_chunks(legacy_entry_point)` when a tool
needs the expanded text with exact physical provenance. It preserves the
original compile directory, input order, UTF-8 bytes and include chain. A
module's physical directory is not automatically its TeX compile directory.
Missing includes and cycles are explicit errors. The reader is not a TeX
interpreter and does not execute macros or conditionals.

The source manifest documents long-block exceptions such as historical
preambles and verbatim PDF transcripts. Splitting an atomic verbatim block by
inserting `\input` would change what is printed; keep the owning exception
visible rather than silently altering its content.

## Regenerate and check

After intentional source changes, regenerate through the repository's normal
build workflow. The registry can also be rebuilt and checked directly:

```sh
python3 verification/make_content_registry.py
python3 verification/make_content_registry.py --check
python3 verification/test_content_registry.py
```

Generation is deterministic and has no wall-clock timestamp or hidden network
lookup. `--check` rebuilds the derived view in memory and fails if committed
outputs differ. It validates IDs, source ownership and reference endpoints;
it does not execute the claims. Current source hashes describe the current
files. Preserve historical migration hashes as provenance rather than rewriting
them to disguise a content change.

The public inventory uses tracked authored TeX plus the explicit modular
ownership manifest and explicit public additions. It excludes vendor/runtime
caches and compiled outputs. A Gitless export uses the shipped source inventory
and the same ownership manifest, so it remains reproducible without scanning an
unrelated machine. Archive source text and required include dependencies must
ship with that export; historical compiled PDFs are optional.

## Alternative reading editions

`docs/editions.json` records each derived output, its source owner and any
omitted include chains. For example, the compact introduction guide derives
from the full introduction while keeping the generated module catalogue and
dated history available as separate documents. An ignored derived
`introduction_guide.tex` is not a second authored owner. The separate
`verification_catalog.tex` is a declared public entry point. No edition changes
mathematical status or supplies missing arguments.

## Private local supplements

Unpublished local TeX is excluded from the public registry. To inspect it
explicitly, use:

```sh
python3 verification/make_content_registry.py --include-local
python3 verification/make_content_registry.py --include-local --query 'Kernessenz' --limit 10
```

This writes a **separate ignored** `docs/registry/local/` supplement. An explicit
`--output /absolute/local/directory` can choose another local destination. It
never rewrites the public registry. Discovery is limited to untracked,
nonignored authored project roots, plus the explicitly declared
`documents/local/source_manifest.json` if present; vendor/cache roots remain
excluded. A private modular source can therefore be included even when its
wrapper or modules are ignored, but only through that explicit local manifest.
Do not publish the local supplement automatically. A PDF without an editable
TeX source is not evidence of a hidden editable document or of a source mapping.
