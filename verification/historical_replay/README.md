# Historical source replay inputs

These inputs reproduce the source context of the unchanged 9 September contract
checkers. They are historical provenance, not the active TFPT ledger, a new
scientific result or an RH implementation. Never update the old validation.json
receipts or checker PIN dictionaries to make a current source look historical.

`manifest.json` declares five bounded transformations:

- `v1033_original.py` has the exact originally pinned SHA256. The active v1033
  differs only by importing read_tex and replacing its document-reading helper.
  Replay verifies the exact two-edit byte transformation and unchanged AST outside
  that helper. Mathematical changes are rejected even if a current hash is updated.
- `status_ledger_original.csv` is the exact historical combined ledger recovered
  from commit461603b295c1dcbb0cacb01c0fd4aea5a1c62d29. Its1194 rows are a historical
  input only. The active788-row TFPT ledger remains separate. Every retained row
  must equal the historical projection plus28 explicit ownership/location/scope
  deltas; status and canonical_status changes are forbidden as adapter deltas.
- The original MMST article is reconstructed from its current physical modules,
  verifying contiguous byte extents, every module hash and the original full hash.
  No duplicate authored article body is stored here.
- The neutral seam helper is byte-identical at its new TFPT-owned path. Its old
  path is materialized only inside the temporary replay copy, with unchanged hash.

- `census_qsm_normflow_original.py.txt` is an explicitly external Prime Front
  arithmetic-QSM historical source input. The origin-composition audit uses its
  original Gaussian-HNF cell counts to reproduce a classical connected-count
  certificate. It is data here, not an active TFPT probe. Its exact original hash
  is enforced and its old executable path exists only in the temporary replay.
  No arithmetic/RH result or old source status is imported into active TFPT.

`historical_source_replay.historical_overlay(root)` uses ordinary temporary copies
and cleans them up on exit. It never monkeypatches filesystem APIs or writes the
current checkout. Its root is injectable for mutation regressions. The original
checker hash guards still execute over exact historical bytes at their original
paths. All mathematical predicates and historical receipts remain intact.

Run the actual consolidation runner; its report labels `source_context` as
`explicit_historical_provenance_replay`. Its separate `current_source_checks`
execute the current v1033 module and modular source tests in the current checkout.
Replay PASS is not a claim that an old byte pin matches a changed current source,
a proof of a physical derivation or a status promotion. Large production replays
remain the runner's existing separate explicit tier.

CI runs test_historical_source_replay.py in normal and optimized Python before
the inventory replay. Those tests reject current byte changes, changes to math
and reader logic despite recomputed hashes, ledger mutations/status adapters,
changed modules/helpers, and leakage of temporary aliases into the active tree.
