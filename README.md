# Topological Fixed Point Theory

**TFPT investigates whether shared geometric data can explain particle families, mass hierarchies and dimensionless constants.**

The research programme connects boundary geometry, the E₈ lattice and rules for calculating particle structure and numerical outputs. The idea is to reuse the same inputs: a marked boundary supplies an internal particle space and family data; their representations determine charges and transport rules; those rules feed mass and mixing relations, an electromagnetic fixed point, and connected quantum and cosmological calculations. This repository contains the original papers, executable calculations, formal statements and public explanations.

A concrete example is a boundary equation whose positive root gives $\alpha^{-1}=137.03599921684\ldots$. You can [reproduce that number](#reproduce-the-alpha-calculation) and inspect the equation, its inputs and its controls. Identifying its root with the measured electromagnetic coupling retains the physical assumptions stated in the source.

[Explore interactively](https://www.fixpoint-theory.com/interactive) · [Understand the derivations](https://www.fixpoint-theory.com/explain) · [Predictions and tests](https://www.fixpoint-theory.com/predictions) · [Original papers](https://www.fixpoint-theory.com/papers)

## Choose a starting point

| I want to… | Start here |
|---|---|
| See how the pieces connect | [The interactive journey](https://www.fixpoint-theory.com/interactive), with visual constructions and controls |
| Follow the actual calculations | [Understand TFPT](https://www.fixpoint-theory.com/explain), from the starting structures through charges, masses and alpha |
| Examine a particular question | [Fine structure constant](https://www.fixpoint-theory.com/fine-structure-constant), [E₈ and the Standard Model](https://www.fixpoint-theory.com/e8-standard-model), or [three fermion generations](https://www.fixpoint-theory.com/three-fermion-generations) |
| Compare a readout with data | [Frozen predictions](https://www.fixpoint-theory.com/predictions), [dated empirical comparisons](https://www.fixpoint-theory.com/empirical-audit) and [failure criteria](https://www.fixpoint-theory.com/falsification) |
| Read or reproduce an argument | [Selected original arguments](https://www.fixpoint-theory.com/research), the [papers](https://www.fixpoint-theory.com/papers), and the [source registry](docs/registry/INDEX.md) |

## Results and their scope

The [claim ledger](verification/status_ledger.csv) and original sources distinguish declared premises, exact consequences, numerical calculations and conditional physical identifications. Here is how those distinctions apply to the main results:

| Result | What the statement establishes |
|---|---|
| Particle representations and E₈ | Exact representation and lattice constructions under their stated boundary, carrier, pairing and glue hypotheses. The physical particle and family dictionary retains its conditions. |
| Source masses and mixing | Integer transport lengths, charged lepton coefficients and the stated source ratios have explicit derivations. Absolute quark amplitudes and phase or neutrino branches retain their separate conditions. Measured masses require the physical comparison map, scale and scheme. |
| The alpha value | A numerical solution of the specified boundary equation, accompanied by an analytic uniqueness argument. The coefficient 41 has its own particle content and transport derivation. Identifying the full response with physical electromagnetism retains the source conditions. |
| Dynamics and the common physical source | Exact and conditional finite dynamics and reconstruction results exist. The full primitive interacting field integral, its physical responses and the common interacting spectrum remain the calculation target. |

The finite Dirac operator organizes supplied Yukawa and Majorana matrices and the specified Higgs construction. Its assembly alone does not calculate all numerical coupling entries. The mass formulas below have their own source derivation.

<details>
<summary>Five terms used in the papers</summary>

- **Seam:** the oriented boundary structure supplying the kernel, state and time data used by the construction.
- **Carrier:** the internal five dimensional space used to build particle representations. Its dimension is separate from spacetime dimensions.
- **Compiler:** the shared rules mapping geometric inputs to representations, integer transport lengths and calculated outputs.
- **Readout:** an output of a specified mathematical construction. Its identification with a measured quantity has stated physical premises.
- **Source mass:** a mass in the source construction, written with a hat. A pole mass or a mass quoted at a renormalization scale requires the corresponding physical transfer.

Precise definitions and assumptions remain in the linked original papers.

</details>

## The connected construction

**Boundary and carrier.** The declared interfaces are an oriented reflection positive seam kernel with unit winding, normalized by $c_3=1/(8\pi)$, and a five slot carrier with a marked three plus two split. The shared four mark geometry and parabolic anchor $(1,1,2)$ explain their numerical data under the source hypotheses stated in the [Architecture paper](documents/tfpt_1_architecture_e8/main.tex). The interface assumptions and their conditional reductions remain visible in the original statements.

**Particle structure and families.** The even exterior representation of the five slots has $1+10+5=16$ components. With normalized slot hypercharges $(-1/3,-1/3,-1/3,1/2,1/2)$, it gives one Standard Model generation, including the conjugate right handed neutrino, in an all left handed convention. The structure preserving group is $(SU(3)\times SU(2)\times U(1)_Y)/\mathbb Z_6$. Four punctures leave three independent cycle directions; their identification with physical families uses the stated family dictionary. The finite Dirac construction then organizes Yukawa and Majorana blocks and the specified Higgs doublet. [Follow the complete Standard Model map](https://www.fixpoint-theory.com/explain#standard-model).

**E₈, codes and clocks.** The carrier lattice $D_5$ and family lattice $A_3$ join through order four discriminant glue into the even unimodular E₈ lattice. Its four glue classes contain $52+60+64+64=240$ roots. Clifford actions, binary and Gaussian code descriptions, and the connected clock actions provide further descriptions of this structure. The order thirty Coxeter data, the order four automorphism and the relaxation operator act on specified spaces. Their orders alone do not identify their actions. [Explore the lattice](https://www.fixpoint-theory.com/interactive/e8) or read the [code working note](documents/note_e8_gaussian_code/main.tex).

**Masses and mixing.** The shared seed and the mass master formula are

```math
\begin{aligned}
\varphi_0&=\frac1{6\pi}+\frac3{256\pi^4},\\
\lambda_Y&=\sqrt{\varphi_0(1-\varphi_0)},\\
\widehat m_{f,j}&=\frac{v_{\mathrm{geo}}}{\sqrt2}\lambda_Y^{L_{f,j}}\Lambda_{f,j}\\
&=\frac{v_{\mathrm{geo}}\pi}{\sqrt2}c_{f,j}\varphi_0^{K_{f,j}}.
\end{aligned}
```

The residue, grading and sheet operators determine the transport lengths $L$ and mass powers $K$ for all nine charged fermions. The finite lepton response gives the coefficients $(16/7,4/3,7/6)$. The quark readouts give source ratios including $\widehat m_u/\widehat m_d=55/117$ for the specified discrete family of admissible operator data. The remaining absolute quark amplitude anchor has a separate role. Mixing magnitudes share the same seed, while the phase and neutrino branches retain their named conditions. These are derived source relations; comparison with pole or running masses uses the specified physical comparison map, scale and scheme. [Work through the mass calculation](https://www.fixpoint-theory.com/explain#flavor) or read [Paper 2](documents/tfpt_2_standard_model/main.tex).

**The electromagnetic fixed point.** The specified particle content and transport budgets give a fixed matter coefficient, 41, in the alpha equation. Its root gives $\alpha^{-1}=137.03599921684\ldots$. Existence and uniqueness of that root, coefficient provenance, the response calculation and the physical electromagnetic interpretation are distinct steps of the argument. [Calculate the balance yourself](https://www.fixpoint-theory.com/interactive/alpha) or [inspect the full derivation](https://www.fixpoint-theory.com/fine-structure-constant).

**Physical dynamics and other readouts.** The transfer spectrum has an exact continuous stochastic interpolation at finite level. The papers also construct quantum lifts, finite field models, horizon identities, and cosmological and physical transfer calculations. Each keeps its operator, physical branch and limiting hypotheses. The [common source explanation](https://www.fixpoint-theory.com/explain#source) connects these results to the original action, fields, state and time reconstruction. The [frontier paper](documents/tfpt_4_frontier/main.tex) and [research contracts](documents/tfpt_research_contracts/main.tex) give their precise scope.

## Read the papers and trace a claim

Begin with [the introduction](documents/introduction/main.tex). Stable root `.tex` entry points assemble the modular sources; the [published editions](https://www.fixpoint-theory.com/papers) provide the reading PDFs and their publication details.

| Source | What it develops |
|---|---|
| [Introduction](introduction.tex) | Starting assumptions, derivation map, predictions and reading routes |
| [1. Architecture and E₈](tfpt_1_architecture_e8.tex) | Boundary and carrier inputs, lattice glue and electromagnetic closure |
| [2. Standard Model](tfpt_2_standard_model.tex) | Particle representations, parabolic transport, mass and mixing readouts |
| [3. E₈ audit and bootstrap](tfpt_3_e8_audit_bootstrap.tex) | Consistency slices, cascade and bootstrap constructions |
| [4. Frontier](tfpt_4_frontier.tex) | Physical transfer calculations and their conditional inputs |
| [5. Red team](tfpt_5_redteam.tex) | Counterexamples, adversarial checks and failure criteria |

The companions cover [origin and clocks](origin_theory.tex), [horizons](tfpt_horizon_readouts.tex), [research contracts](tfpt_research_contracts.tex) and [safeguards](tfpt_safeguards.tex). The standalone [E₈ and Gaussian code note](note_e8_gaussian_code.tex) develops the code bridge. The compact introduction, verification catalog and dated history are also available as separate reading editions.

Use the [central registry](docs/registry/INDEX.md) to move from a topic to its original section, editable module and cited Python, Lean or Wolfram evidence. A bounded local query is often the quickest route:

```sh
python3 verification/make_content_registry.py --query 'hypercharge' --limit 10
python3 verification/make_content_registry.py --topic flavor-masses --limit 10
```

The [prediction register frozen on 9 June 2026](verification/predictions_frozen.json) contains sixteen main values, two assigned textures and two conditional inflation bands. A freeze records a commitment date. Whether a particular comparison is prospective depends on when the relevant measurement first became public. The [dated empirical audit](https://www.fixpoint-theory.com/empirical-audit) records the measurements, uncertainties and disclosure dates; values already known at the freeze remain comparisons with known data.

The [paper changelog](changelog.tex) preserves publication history. Earlier archived releases retain their own versions and dates.

## Run the verifier

Use Python 3.11 or 3.12, the versions exercised by the core verification workflow. Clone the repository and install the numerical dependencies:

```sh
git clone https://github.com/sthamann/topological-fixed-point-theory.git
cd topological-fixed-point-theory
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
. .venv/bin/activate
```

Start with the short core check:

```sh
./verify
```

It runs six existing Python modules covering E₈ glue, the carrier, alpha, the cascade, a neutrino texture and frozen registry consistency. Look for the recomputed E₈ root count 240, the rounded inverse alpha value 137.0359992 and a passing Python summary. The Wolfram and Lean lines point to separate engines; this command does not execute them.

### Reproduce the alpha calculation

From the repository root, with the virtual environment active:

```sh
python3 verification/v3_em_alpha.py
```

The module checks the root against 137.0359992168407, encloses it in an interval, and tests neighboring integer budgets and boundary normalizations. Its summary should report zero failed checks. This reproduces the specified numerical equation and its implemented controls. The [analytic uniqueness argument and physical scope](https://www.fixpoint-theory.com/fine-structure-constant) accompany the source; numerical checks alone do not establish the complete physical identification.

### Run broader checks

The full registered Python suite is a separate, substantially longer run:

```sh
.venv/bin/python verification/run_all.py
python3 verification/check_project_scope.py
```

Check each command's summary and exit status. A nonzero exit status means the run did not complete successfully; inspect the reported failure or setup error before using its result.

For a particular claim, follow its original section to the named verification module and inspect the inputs and negative controls. Python execution, Lean kernel checking and Wolfram evaluation are separate checks. The formal carrier development includes its own toolchain and axiom audit:

```sh
(cd experiments/lean4-carrier-rigidity && bash scripts/audit.sh --core)
```

The [ledger](verification/status_ledger.csv), [script registry](verification/script_registry.csv), actual `.lean` statements and `.wl` sources define the scope of those checks. Report the command and result actually obtained; an inventory entry or passing numerical example does not establish a broader theorem.

## Build the documents and website

Document builds use TeX Live or MacTeX. The website requires Node.js 20.9 or newer and npm; the production deployment uses Node.js 24. Run the source workflow from the repository root:

```sh
bash build.sh gen          # regenerate source maps and indices
bash build.sh notes        # compile active PDFs and reading editions
bash build.sh editions     # compile only the compact guide and reference catalog
bash build.sh website      # refresh public PDF/script mirrors and hashes
bash build.sh audit        # check source, registry and mirror consistency
```

Build or run the public presentation locally:

```sh
(cd website && npm ci && npm run dev)
# For a production build:
(cd website && npm run build)
```

`bash build.sh release` runs the complete publication rebuild. After staging newly shipped source files, generate the manifest last and check it:

```sh
python3 verification/make_manifest.py
python3 verification/make_manifest.py --check
```

See [LaTeX maintenance](docs/LATEX_MAINTENANCE.md) for targeted builds, generated outputs and registry commands. Compile from the documented directory so figures and shared includes resolve.

## Where the sources live

```text
documents/                 Editable modular paper sources and provenance
*.tex                      Stable compilation entry points
tex-artefacts/             Shared notation, figures, references and indices
verification/              Executable checks, claim ledger and frozen predictions
experiments/lean4-carrier-rigidity/
                           Formal statements, toolchain and axiom audit
docs/registry/             Generated topic, document and evidence navigation
docs/                      Reading, scope and maintenance guides
website/                   Public explanations and generated download mirrors
_archive/                  Historical document sets
```

The owning LaTeX module and cited original source own the scientific text. `verification/status_ledger.csv` owns claim status; registered scripts own executable checks. Edit the owner once and regenerate its derived tables, indices and public mirrors. Published PDFs and generated files are outputs.

The local Knowledge Atlas, accessed through `tfpt-knowledge` when installed, supplies current research navigation and reviewed decisions. The public checkout includes a reproducible public snapshot; private local databases and unpublished sources are outside that export. The [semantic navigation guide](docs/SEMANTIC_NAVIGATION.md) explains freshness, coverage and public scopes. Source summaries and graph links help locate an argument; its original premises and evidence still decide what follows.

## Authors, citation and discussion

The papers list **Stefan Hamann and Alessandro Rizzo** as authors. Their [public author pages](https://www.fixpoint-theory.com/authors) connect the publications and their versions.

When citing the theory, use the title, authors, version and date of the [paper edition](https://www.fixpoint-theory.com/papers) you actually read. When reporting a code reproduction, include the repository commit and the command you ran. The current website and historical releases retain separate publication identities.

Use [GitHub issues](https://github.com/sthamann/topological-fixed-point-theory/issues) for questions, reproduction failures or corrections. Include the relevant claim or source section and, for a failed check, the command and output.

The repository has no root project LICENSE file. Please direct questions about reuse of the code or papers to the maintainers.

## Contribute

Read [AGENTS.md](AGENTS.md) and the [maintenance guide](docs/LATEX_MAINTENANCE.md) before changing sources. Find the owning module, preserve claim scope and negative results, and check the affected path through to its public output. Record repository maintenance in [docs/CHANGELOG.md](docs/CHANGELOG.md); keep scientific and publication history in the paper changelog.

This repository owns physical TFPT and its compiler mathematics. RH, prime number, Weil window and factorisation research belongs to the independent [Prime Front repository](https://github.com/sthamann/prime-front) and [website](https://prime.fixpoint-theory.com/).
