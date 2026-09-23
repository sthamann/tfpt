# Graph-bound autonomous RH research

This is a research workflow, not an RH solver or an omniscient semantic index.
Paper statements, source versions, attempts, exact finite controls, hypotheses
and the separately Lean-checked proof rules remain distinct.

## One entry point

From the repository, using the existing Python environment:

```sh
python3 -B rh/catalog/research_cycle.py cycle
python3 -B rh/catalog/research_cycle.py check
python3 -B rh/catalog/research_cycle.py search 'rank three joint arithmetic'
python3 -B rh/catalog/research_cycle.py claim paper-multilevel-rung
python3 -B rh/catalog/research_cycle.py controls
```

`cycle` acquires an exclusive local lock, checks/rebuilds the existing catalog,
concept graph and exports, indexes declared sources incrementally, executes
bounded exact mechanism controls, and selects a diverse queue of research
contracts. Existing semantic review pins and Lean audit failures stop refresh;
the runner never renews them simply to turn a check green. A stopped cycle
exits nonzero and requires source review or the appropriate proof audit.

`source_scope.json` declares the actual source universe: the TFPT repository
without caches/dependencies/generated graph exports, this RH task's research,
work and outputs, the paper audit, and other already registered Lean sources.
Files added under these roots are discovered on the next cycle. Other project
folders are not silently treated as covered. Symlinks are reported as skipped.
The full hash of each indexed file is tracked. Text has an explicit size cap;
large texts are marked partial and binary files hash-only. Query results link
back to originals. **Index coverage is not semantic review and not evidence
that every byte of data has been consumed by a model.**

SQLite FTS is lexical retrieval, not an embedding model. The graph provides
typed context; the scheduled agent reads selected originals and checks their
actual mathematical meanings. The complete catalog and registered constraint
list are loaded for proposal triage. Similarity alone never kills a candidate,
and listing constraints does not mean every constraint has been semantically
checked against it.

## Papers and graph

`paper_reviews.json` is authored review data. Statements have source anchors,
source hashes, all-required premises, and explicit evidence states. Changes
to a paper invalidate its prior annotations; they are not automatically
approved again. Complete statements and requirements are exported in
`generated/papers.json` and `_newest/graph/paper_claims.json`; the regular
concept graph contains source and claim nodes with conditional connections.
The reviews are partial source/scope audits, not full refereeing.

The seven registered papers also expose unreviewed theorem-like environments
with their unabridged source bodies and a section review queue. This is lexical
extraction, not a complete TeX parser; an environment name is not a proof status.
These discovered claims are blocked as accepted premises until reviewed.

The root TeX/PDF inventory and TeX style dependencies are now in the refresh
input boundary. A newly added root document is detected even when no reviewed
claim annotation exists for it yet. Root PDFs are versioned by hash; no visual
or textual equivalence to TeX is inferred automatically.

## Adaptive proposal search

The initial grammar has eight domains and three methods. These produce
research contracts, **not 24 constructed operators or discovered solutions**.
Priorities use target connectivity, work cost, prior exposure and domain
diversity, not invented success probabilities. Failed results suppress the
same mathematical object, not every future idea with a similar name.
The exclusion penalty is applied only while its original result evidence hash
still matches. Changed or missing evidence requires review, not a permanent ban.
The finite exact controls actively seek an abstract rank-two counterexample
and check zero-residual and valid Schur cases. They are not zeta experiments.

The creative part is the recurring Codex agent: it may construct a different
explicit object outside this grammar, including geometry, topology, analytic
number theory, operators, dynamics, information theory or an unlisted domain.
It should derive one concrete new implication or refutation per bounded
investigation, not merely produce more analogy names.

To submit a candidate, author a JSON object with nonempty `object`, `target`,
`method`, `scope`, `difference`, `next_test`, `stop_condition`, `domain`, and
lists `obligations`, `sources`, `asserted_claims`. Targets normally refer to
`proof_search/knowledge.json`. Include exact definitions or equations in
`object`, normalization and quantifiers in `scope`, and concrete reasons why
nearby historical kills do or do not apply in `difference`. Set neither
`proof_accepted` nor `RH_proved` to true.

```sh
python3 -B rh/catalog/research_cycle.py submit /absolute/path/to/candidate.json
python3 -B rh/catalog/research_cycle.py record-result CANDIDATE_ID \
  --result INCONCLUSIVE --evidence /absolute/path/to/analysis.md
python3 -B rh/catalog/research_cycle.py cycle
```

Submission IDs ignore labels/fitness and depend on the mathematical object,
target, method, scope and obligations. Source-attributed result records accept
`REFUTED_SCOPED`, `FINITE_PASS`, `INCONCLUSIVE`, `DUPLICATE`, or
`REVIEWED_CANDIDATE`; none authorizes proof inference. Evidence changes are
visible and may invalidate a result's applicability. Submissions and outcomes
are preserved and linked through the regular concept graph on refresh.

Generated queue, history, coverage and checkpoint files live in `generated/`.
These outputs are not copied back into the source index recursively. Do not
delete historical candidates or overwrite original evidence to improve scores.

## Scheduled agent and resource bounds

The app heartbeat in the current RH task runs every two hours when enabled.
It invokes the installed `$rh-graph-research` skill, refreshes, reads originals,
and investigates one selected or genuinely new candidate. It stays quiet for
unchanged/non-actionable state, and reports a substantive result, failure or
needed decision. This is periodic, not an always-on filesystem watcher, and
execution depends on app scheduling and host availability.

One cycle launches no arbitrary submitted code. A scheduled agent may author
and run a separately reviewed small local probe in this campaign's experiments
folder, initially with a five-minute CPU budget and no GPU, paid API sweep,
network upload, remote worker dispatch, or original-paper/Lean/ledger changes.
Those broader actions require their own applicable authorization. New probes
must be reproducible, record source versions and uncertainty, and preserve
prior artifacts. A genuine sealed RH probe promotion follows `rh-sync`; these
infrastructure controls are not promoted to the sealed mathematical suite.

Before an external mathematical claim, require the complete proof and an
independent audit, including exact Lean types/axioms where applicable. An
RH-equivalent assumption remains an open obligation even if renamed.

Tests: `python3 -B -m unittest -q test_research_engine test_research_sync test_proof_search`
from `rh/catalog`; repeat under `-OO`.
