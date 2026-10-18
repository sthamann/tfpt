# Modular LaTeX source ownership

Legacy entry points and PDF filenames stay stable. The authoring text now lives in
`documents/<document-id>/`; a legacy `.tex` file is a thin input wrapper.

```text
documents/
  introduction/
    preamble.tex            # original preamble, unchanged
    sections/001-source.tex # original contiguous source spans
    sections/002-....tex
    main.tex                # ordered module inputs only
  ...
  source_manifest.json      # ownership, original ranges and content hashes
  standalone_inventory.json# all 115 original standalone TeX entry points
  pdf_baseline.json         # original active PDF/page/text hashes
```

Edit the owning section module for scientific prose. Keep labels and verification
citations with their argument. The root wrapper and `main.tex` only select source
files; they are not additional copies of the paper. Shared styling and generated
verification tables remain under their existing `tex-artefacts/` ownership.

The extraction is mechanical: 63 sources (55 standalone entry points and eight
large archived source fragments) were separated into 600 unchanged source spans.
The ordered module bytes reconstruct every original source exactly. Full literal
input expansion before and after the move also has identical hashes for all 63
sources. No text, mathematical statement, scientific premise, status or label was
rewritten. `source_manifest.json` contains hashes and original ranges, not body
copies. `standalone_inventory.json` records why every other standalone is left
intact: 13 immutable source/snapshot inputs and 47 short documents.

The target is about 400 lines per body module. Splits use existing section or
paragraph boundaries outside open mathematical arguments and open TeX conditionals.
The dual-mode changelog keeps its entire conditional header in `preamble.tex`,
including the guarded standalone document opening, because TeX skips input
commands inside a false conditional branch. Five older preambles
(591–628 lines) remain whole as separate preambles. One 3056-line historical PDF
transcription remains one `MyVerbatim` block: input directives inserted inside it
would be printed literally. This is a documented syntax exception, not active
scientific prose hidden in a wrapper. Original archived claim scopes remain
historical; moving their source does not validate them.

## Compile and read sources

Compile from the entry point's original directory, using its unchanged name.
Current root documents still compile from the repository root. The archived
00–07 series still compiles from `_archive/tfpt-45/`. The manifest records each
`compile_dir`; module include paths retain that directory's TeX lookup behavior.

`verification/tex_sources.py` is the common source-reader API:

```python
from pathlib import Path
from tex_sources import read_tex, source_chunks, dependency_paths

text = read_tex(Path("introduction.tex"))
chunks = source_chunks(Path("introduction.tex"))
closure = dependency_paths(Path("introduction.tex"))
```

`read_tex` returns the exact ordered literal expansion, with no synthesized
whitespace. Each `SourceChunk` records `path`, `text`, one-based inclusive
`start_line`/`end_line`, UTF-8 `start_byte`/`end_byte` (end-exclusive), and the full
`include_chain`. `dependency_paths` includes empty files and pure wrappers, which
have no text chunks. All three functions accept an optional `compile_dir=Path(...)`
for direct reads of non-standalone fragments. Prefer reading a legacy entry point,
then use chunks to attribute the physical modules; do not register its `main.tex`
as a second document.

This reader does not execute TeX macros or evaluate conditional branches. Literal
input/include commands are expanded; comments, verbatim blocks and dynamic names
remain literal. Missing dependencies and cycles raise explicit errors with the
source line/include chain. Generated master-index chunks can be distinguished by
physical path, so they cannot accidentally count as paper-body evidence.

## Mechanical checks

```bash
python3 -m unittest discover -s verification -p test_tex_sources.py -v
python3 documents/modularize_sources.py --check
```

The second command checks the frozen migration receipt, including original byte
reconstruction and original expanded hashes. It is evidence for this mechanical
move, not a substitute for reviewing later authorized scientific edits. The
one-shot extraction script refuses to overwrite an existing migration manifest.
