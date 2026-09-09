# Publication verification — 9 September 2026

This record concerns integration and reproducibility, not new proof status.
Source snapshot before integration: `b803b7e5d0e4ac20c0a1ce7bffee0f91326dcff4`.
The research map is [RESEARCH_2026-09-09.md](RESEARCH_2026-09-09.md).

## Fresh execution

- The [charged-field dependency rerun](publication_charged_20260909.json):
  **131 tests in each mode**, ordinary and optimized Python, all passed.
- The [frozen new-archive bounded inventory](publication_bounded_20260909.json):
  **61 modules, 971 tests in each mode**, all passed. Completed
  2026-09-09 06:42:49 UTC, Python 3.14.3 on the local macOS host.
  The three excluded production-replay methods are listed in the report;
  their bounded module tests, native grouping checks and saved-record
  controls were executed. No full-core or large digit-data rerun is claimed.
- `./verify`: **89 core checks passed**. This was not `./verify --full`.
- `verification/test_make_manifest.py`: **4 tests passed in both modes**.
  A new failing-then-passing regression covers C++ sources, headers and
  `.sha256` source-pin files in both Git-index and exported-tree layouts.
  Unstaged or ignored local files still cannot leak into the release manifest.
- `verification/audit_sync.py`: **AUDIT OK, 1028 registered scripts**.
  This count is an inventory/synchronization result, not 1028 newly run modules.
- Next.js production build: **success**, including TypeScript and 34 static
  page-generation entries. Existing edge-runtime static-generation notice
  is retained. Research section and paper navigation rendered in the browser;
  the scoped browser log inspection returned no errors or warnings.

## PDFs and source integrity

Rebuilt the contracts paper (239 pages), frontier (23), introduction (715,
including the imported canonical changelog), and standalone changelog (425).
The new and adjacent pages were rendered and visually inspected. The website
copies and release checksums were regenerated; unedited papers were mirrored,
not represented as newly revised research. No Zenodo publication was made.

The new contracts section is on pages 214–217; frontier update on page 18;
the canonical new changelog entry is also in introduction page 290.
Old paper macros and old research validation records keep their original
status scope. Frozen generated SVG/CSV whitespace and two historical trailing
blank lines were retained; authored integration text has no whitespace errors.

## Explicit limits and diagnostic history

The initial unbounded inventory attempt hit the five-minute per-module cap
inside Round47's full deterministic replay. Stack inspection located the
95,599,440-extension native production calculation, not a failed identity.
Round49/50 also invoke full native production replays. Only the newly launched
publication/diagnostic jobs were stopped; existing unrelated local previews
were untouched. The final runner separates exactly those three methods and
offers `--include-large-replays --timeout 7200 --workers 1` for an explicit
large run. The partial attempt is not counted as a successful full replay.

Historical numerical, timing and digit-data outputs are shipped with their
source records but are not new measurements. Known upstream unclosed-file
ResourceWarnings remain in full transcripts; they were neither suppressed
nor treated as failed mathematical tests. No source-pinned scientific file
was rewritten to make a regression pass. None of this is independent
mathematical review, a shared physical parent, or closure of T1–T8/RH.
