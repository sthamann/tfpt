# Consolidation verification receipt — 12 September 2026

This records the initial consolidation build before the requested follow-up
extension. Its PDF page counts and digests below are historical, not the
current files. The current artifact receipt is
[FOLLOWUPS_VERIFICATION.md](FOLLOWUPS_VERIFICATION.md). Mathematical test
results below remain the recorded initial runs, not fresh roadmap tests.

## Executed this round

| Checker | Checks | Normal versus -OO |
| --- | ---: | --- |
| source_edge_access.py | 44 | Byte-identical JSON |
| covariant_edge_channel.py | 20 | Byte-identical JSON |
| edge_channel_stationary.py | 15 | Byte-identical JSON |

All three source-pinned probes exited successfully. These are exact local
finite checks plus the associated written arguments, not TOE completion.
The four external task reports were read and archived; their claimed
finite-field and expanded-family certificates were not all independently rerun.

## Documents

All three PDF builds completed successfully with latexmk/pdflatex. The new
standalone paper has five pages. The German explanation has two pages.
The fully rebuilt Research Contracts paper has 244 pages; the new section
starts on PDF page 217. The pre-existing root-level PDF was not overwritten:
the newly built copy is in this directory's `pdf/` subdirectory.

The new standalone PDFs have no final log entries matching Overfull,
Underfull or Warning. The full legacy paper retains font/layout warnings;
this pass did not redesign or independently audit its pre-existing content.
The German final PDF was visually inspected on both pages; selected
standalone paper pages were also inspected. Text extraction verified the
new section inside the full PDF. Twelve explicit Markdown links in the
two new top-level summaries resolve locally. The main TeX includes the
new section exactly once. `git diff --check` passed for tracked changes.

## PDF SHA-256 digests

- `pdf/tfpt_research_contracts.pdf`:
  `f0c1f5667edcbc460a76ef47cf2fb130712eab09a9312d99853bb0cdc68852bd`
- `pdf/tfpt_universalraum_synthesis_2026-09-12.pdf`:
  `2866040fd6ca92abcd66f097db438e553f386684203e846afa5123b921452a39`
- `pdf/tfpt_universalraum_einfach_2026-09-12.pdf`:
  `56fb5338b6266c50b2f096925ca2564b8cf7fa073109e0b83463a35a98c0f555`

## Scoped repairs during document verification

The first standalone build exposed a missing closing math delimiter in
the new section; corrected and rebuilt. An output-capture wrapper initially
assumed the large legacy TeX log was UTF-8; raw-byte capture established the
successful build without changing the document or its scientific claims.
The missing pdftotext executable was replaced by the available pypdf reader
for extraction. These are tooling repairs, not proof results.

No commits, pushes, website deployment, RH index refresh, Hylæan changes,
or physical acceptance-marker promotions were performed.
