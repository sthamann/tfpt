# TFPT — Topological Fixed-Point Theory

TFPT is a research programme connecting a discrete compiler, the E₈ lattice,
clock and code structures, Standard Model readouts, and conditional physical
interpretations. Its original assumptions, exact constructions, numerical
checks and remaining physical derivations have different scopes. The
[status ledger](verification/status_ledger.csv) and cited original sources
are authoritative; the number of checks is not a proof of a complete theory.

[Website](https://www.fixpoint-theory.com/) ·
[Published papers](https://www.fixpoint-theory.com/papers) ·
[Central content registry](docs/registry/INDEX.md) ·
[Machine-readable registry](docs/registry/registry.json) ·
[Agent instructions](AGENTS.md)

## Find a topic or a source

Start with the **[central content registry](docs/registry/INDEX.md)** or its
[compact agent entry](docs/registry/summary.json). Use the bounded query CLI
in the maintenance guide rather than loading the complete graph into context. It maps
LaTeX documents and sections to their editable source modules, topics,
registered Python verifications, ledger claims, and explicit Lean or Wolfram
references. It distinguishes a citation from a proof and an inferred topic
match from an explicit reference. Missing or ambiguous evidence links remain
visible.

The [LaTeX maintenance guide](docs/LATEX_MAINTENANCE.md) explains source
ownership, builds, registry updates and change validation. Do not edit a
published PDF, generated index or website mirror to change the theory.
Edit the owning source, then regenerate its derived surfaces.

## Repository structure

```text
documents/                 Modular LaTeX sources and extraction provenance
*.tex                      Stable entry points for the existing PDF filenames
tex-artefacts/             Shared style, notation, references and generated indices
docs/registry/             Generated document/topic/evidence registry
docs/                      Reading guides, scientific scope and maintenance docs
verification/              Registered Python checks, ledger and build/audit tools
verification/wolfram/      Independent Wolfram checks within their stated scope
experiments/               Exploratory work and recorded results
experiments/lean4-carrier-rigidity/
                           Formal TFPT statements, toolchain and axiom audit
website/                   Public presentation and generated download mirrors
_archive/                  Historical document sets; not the current authority
semantic_explorer/         Local Knowledge Atlas, when installed (not shipped)
```

Physical TFPT work belongs here. RH, prime-number, Weil-window and
factorisation campaigns belong in the independent
[Prime Front repository](https://github.com/sthamann/prime-front) and
[website](https://prime.fixpoint-theory.com/). Shared mathematical support
is explicitly scoped; an old namespace or historical citation does not
merge the two research programmes.

## Reading the document set

The **compact reading guide** (`introduction_guide.pdf`) leaves the full
module catalog and dated history in separate reference volumes
(`verification_catalog.pdf` and `changelog.pdf`). The established overall
PDFs remain available under their original names.
Their entry points now assemble maintainable source modules. Begin with
`introduction.tex`, then use the registry to choose the relevant sections.

| Document | Primary role |
|---|---|
| `introduction` | Orientation, assumptions, readouts, status and reading routes |
| `tfpt_1_architecture_e8` | Compiler architecture, seam inputs, E₈ and the EM closure |
| `tfpt_2_standard_model` | Representations, flavor and Standard Model readouts |
| `tfpt_3_e8_audit_bootstrap` | E₈ consistency slices and bootstrap constructions |
| `tfpt_4_frontier` | Conditional interfaces and outstanding physical derivations |
| `tfpt_5_redteam` | Adversarial checks, counterexamples and limits |
| `origin_theory` | Origin, anchor, clocks and source-selection questions |
| `tfpt_horizon_readouts` | Horizon and gravity-related readouts under their assumptions |
| `tfpt_research_contracts` | Detailed research interfaces and scoped contracts |
| `tfpt_safeguards` | Safeguards, uniqueness and audit mechanisms |
| `note_e8_gaussian_code` | Standalone E₈/Gaussian-code working note |
| `changelog` | Dated publication history; historical statements retain their dates |

The registry also inventories other authored LaTeX, shared fragments,
experimental notes and archived versions. A historical document can be
useful without being the current decision record.

## Sources of truth

| Information | Owner |
|---|---|
| Scientific text and assumptions | Owning LaTeX module and cited original research source |
| Claim status and scope | `verification/status_ledger.csv` |
| Registered verification modules | `verification/run_all.py`, `script_registry.csv` |
| Prediction freeze | `verification/predictions_frozen.json` |
| Document and topic navigation | Generated `docs/registry/` and its documented configuration |
| Publication history | Modular `changelog.tex` entry point |
| Formal theorem and axioms | Actual `.lean` statement and audit output |
| Wolfram identity/check | Actual `.wl` source and its stated prerequisites |
| Current local research decisions | Knowledge Atlas via `tfpt-knowledge`, when available |

A registry entry, graph edge, successful finite test or theorem name is a
navigation aid. Read the original statement and all prerequisites before
using it to support a broader conclusion.

## Build and maintain

Use Python 3 and TeX Live/MacTeX. The website needs Node.js and npm; Lean
and Wolfram have their own tools and requirements. Install the Python
requirements in a virtual environment for numerical verifications.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
bash build.sh gen          # regenerate source-derived maps and indices
bash build.sh notes        # compile the active PDF set and reading editions
bash build.sh editions     # compile only the compact guide + reference catalog
bash build.sh website      # refresh public PDF/script mirrors and hashes
bash build.sh audit        # source, scope, registry and mirror consistency
cd website && npm ci && npm run build
```

For a complete publication rebuild, run `bash build.sh release`. Run the
manifest generator last, after staging newly shipped source files:

```sh
python3 verification/make_manifest.py
python3 verification/make_manifest.py --check
```

The [maintenance guide](docs/LATEX_MAINTENANCE.md) contains targeted document
and registry commands. Existing root entry points remain valid; compile
from the documented working directory so shared figures and includes resolve.

## Check the relevant claim

```sh
./verify                                  # concise core check
.venv/bin/python verification/run_all.py   # full registered Python suite
python3 verification/check_project_scope.py
cd experiments/lean4-carrier-rigidity && bash scripts/audit.sh --core
```

Python checks, Lean elaboration, Wolfram evaluation, PDF compilation and
source consistency are separate operations. Report which actually ran and
its result. Do not infer a fresh Lean/Wolfram run from a Python summary.
For a documentation refactor, source preservation, affected consumer tests
and successful document compilation are the relevant first checks.

Repository-structure changes are recorded in [maintenance history](docs/CHANGELOG.md);
the paper changelog preserves dated scientific/publication statements.

## Contributing and agent work

Read [AGENTS.md](AGENTS.md) before changing sources. Locate the owning
module in the registry; use the code graph for code discovery and the
Knowledge Atlas for current research navigation. Keep exploratory work,
registered claims, formal proofs and presentation separate. Preserve
negative results and conditional assumptions. Update the owning source
once, regenerate derived views, and verify the affected path through to
the public output.
