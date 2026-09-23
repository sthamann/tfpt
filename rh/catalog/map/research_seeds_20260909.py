"""Source-attributed late research overlay; no new theorem-strength edges."""
BASE = "/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/"
CONTRACT = "rh/catalog/analysis/research_followups_20260909.md"


def extend(node, edge):
    sources = {
        "odd": BASE + "research/rh_whole_odd_coercivity_20260909/README.md",
        "relative": BASE + "research/rh_arithmetic_relative_correction_20260909/README.md",
        "response": BASE + "research/rh_residual_response_20260908/RESPONSE_PROOF.md",
        "dilation": BASE + "work/relative_window_flow_20260907/relative_flow_proof.md",
        "seam": BASE + "research/rh_seam_gram_correction_20260909/README.md",
        "moments": BASE + "research/rh_zero_temperature_readout_20260908/README.md",
        "fermion": BASE + "research/rh_fermion_event_identity_20260908/README.md",
        "search": BASE + "research/rh_autonomous_search_20260907/README.md",
        "barrier": BASE + "research/rh_barrier_search_20260907/README.md",
        "update": BASE + "research/research_update_audit_20260909/README.md",
    }
    rows = [
        ("whole-odd-coercivity-l9-4", "METHOD", "Reported complete odd coercivity at L=9/4", "Source-reported original signed Weil lower comparison retaining one eighth of both low arithmetic metric and infinite-high energy. Fixed odd window only; independent source/domain review is a separate obligation.", "OPEN", "odd"),
        ("arithmetic-relative-corridor", "METHOD", "Complete arithmetic relative reserve", "Source-reported corridor 9/32 < delta < 289/1024 on the complete eighty-direction comparison at L9/4. Gram iteration uses its already established positivity.", "OPEN", "relative"),
        ("whole-output-inverse-responses", "METHOD", "Joint whole-output inverse-response reserves", "Finite exact selector inputs generate jointly orthogonal complete event outputs; full mixed Grams and infinite residual are retained. Not an infinite inverse or larger-window construction.", "OPEN", "response"),
        ("whole-core-relative-dilation", "METHOD", "Whole-core relative dilation strategy: excluded", "Actual prime-two high-frequency packets refute every finite whole-core relative dilation bound in the specified chart. This does not refute a bound confined to minimizing branches.", "KILLED_HERE", "dilation"),
        ("independent-source-domain-audit", "OPEN_QUESTION", "Independent original-operator and domain audit", "Independently check the original signed form, normalization, low/high domain split, analytic infinite tail and original-error transitions. Shared matrix software and source hashes alone do not discharge this gate.", "OPEN", None),
        ("full-new-complement-domain", "OPEN_QUESTION", "Compatible complete new-window form domain", "Construct a legitimate full new-complement decomposition for an actual larger original Weil window; establish old-form restriction and all normalization cross terms without assuming sharp-cut admissibility.", "OPEN", None),
        ("full-arithmetic-boundary-coupling", "OPEN_QUESTION", "Complete low and infinite-high boundary coupling", "Derive and bound the actual new diagonal and both old-space couplings with Gamma, every active prime power, signed poles and unchanged error budget.", "OPEN", None),
        ("full-boundary-attachment", "OPEN_QUESTION", "Full boundary attachment at proposed L=12/5", "Given independent source review and compatible domains, bound the entire new diagonal below both energy-dual coupling penalties. This would certify one new odd window, not a cofinal family or RH.", "OPEN", None),
        ("cofinal-full-window-family", "OPEN_QUESTION", "Cofinal full-window positivity with test-class coverage", "Construct complete inequalities at an unbounded sequence of legitimate windows, with proved parity/test-class coverage, common normalization and the required form/core limit argument. Finitely many local successes are insufficient.", "OPEN", None),
        ("full-test-class-coverage", "OPEN_QUESTION", "Exact parity, test-class and global-limit coverage", "Establish coverage of the full Weil criterion by the admitted windows and sectors, including any claimed odd-only reduction, domain density and limiting argument. No particular TFPT Galerkin construction is mandatory.", "OPEN", None),
        ("first-zero-exclusion", "OPEN_QUESTION", "Exclude a first zero of the actual spectral bottom", "From a verified positive start, prove actual-bottom regularity and a zero-independent relative estimate integrable through every hypothetical finite first zero; complete test-class identification is required.", "OPEN", None),
        ("minimizer-arithmetic-relative-control", "OPEN_QUESTION", "Minimizer-specific arithmetic relative control", "Derive the needed bound on shifted correlations from true minimizing equations or controlled minimizing sequences. High-frequency whole-core counterexamples do not directly decide this narrower statement.", "OPEN", None),
        ("all-order-compact-readout", "OPEN_QUESTION", "Independent all-order compact arithmetic readout", "Construct a source-defined positive contraction and vector realizing every arithmetic target moment, or prove all complete moment inequalities without presupposing their positivity.", "OPEN", "moments"),
        ("finite-bernstein-exact-readout", "METHOD", "Finite Bernstein exact moment realization: rejected", "The target-derived finite Bernstein construction matches factorial moments, not every ordinary moment; its second-moment defect is positive and its zero endpoint has residual mass.", "KILLED_HERE", "moments"),
        ("fermion-event-scope-filters", "METHOD", "Hypothesis-aware fermionic event filters", "Occupation and intensity obstructions depend on gauge invariance, pairing, rank and readout. Globally positive count laws need not have the determinant factorization required for an RH bridge.", "OPEN", "fermion"),
        ("seam-nine-dimensional-gram-correction", "METHOD", "Finite seam quadratic correction space", "Source-specific Sylvester and nonlinear correction construction in an enlarged nine-dimensional symmetry family. Neither its physical admissibility nor an exact identification with the signed Weil form is supplied.", "OPEN", "seam"),
        ("original-autonomous-residual-miss", "METHOD", "Original autonomous moment campaign: residual miss", "1048 parameter candidates, fifteen initial finite passes and zero passes of a later residual diagnostic. A completed bounded family experiment, not 1048 independent mechanisms or a universal spectral no-go.", "KILLED_HERE", "search"),
    ]
    for id_, kind, title, definition, status, source in rows:
        node(id_, kind, title, [id_.replace("-", " ")], definition, status,
             [sources[source] if source else CONTRACT], ["research-20260909", "source-attributed", "no-rh-promotion"])
        if source:
            rel = "KILLED_BY" if status == "KILLED_HERE" else "USED_BY"
            edge(id_, sources[source], rel, "CONDITIONAL", sources[source],
                 "Source-attribution review; retain original hypothesis and finite/global scope. Not independent proof verification.")
        else:
            edge(id_, CONTRACT, "USED_BY", "CONDITIONAL", CONTRACT, "Open AND-prerequisite contract; no automatic acceptance.")
        edge(id_, "research-question" if kind == "OPEN_QUESTION" else "spectral-framework", "INSTANCE_OF",
             "HEURISTIC", CONTRACT, "Research classification, not a mathematical implication.")
    links = [
        ("whole-odd-coercivity-l9-4", "arithmetic-relative-corridor", "REQUIRES"),
        ("arithmetic-relative-corridor", "whole-output-inverse-responses", "REQUIRES"),
        ("full-boundary-attachment", "whole-odd-coercivity-l9-4", "REQUIRES"),
        ("full-boundary-attachment", "independent-source-domain-audit", "REQUIRES"),
        ("full-boundary-attachment", "full-new-complement-domain", "REQUIRES"),
        ("full-boundary-attachment", "full-arithmetic-boundary-coupling", "REQUIRES"),
        ("cofinal-full-window-family", "independent-source-domain-audit", "REQUIRES"),
        ("cofinal-full-window-family", "full-test-class-coverage", "REQUIRES"),
        ("cofinal-full-window-family", "weil-positivity", "WOULD_CLOSE"),
        ("first-zero-exclusion", "independent-source-domain-audit", "REQUIRES"),
        ("first-zero-exclusion", "minimizer-arithmetic-relative-control", "REQUIRES"),
        ("first-zero-exclusion", "full-test-class-coverage", "REQUIRES"),
        ("first-zero-exclusion", "weil-positivity", "WOULD_CLOSE"),
        ("seam-nine-dimensional-gram-correction", "open-independent-positivity-source", "BLOCKED_BY"),
    ]
    for src, dst, rel in links:
        edge(src, dst, rel, "CONDITIONAL", CONTRACT,
             "Read the full contract. All prerequisites are conjunctive; a traversable edge does not prove either endpoint.")
    edge("full-arithmetic-boundary-coupling", sources["barrier"], "USED_BY", "HEURISTIC", sources["barrier"],
         "Comparison-only precedent, not a construction of the future boundary operators.")
    edge("all-order-compact-readout", sources["fermion"], "USED_BY", "CONDITIONAL", sources["fermion"],
         "Necessary hypothesis-aware filters for one proposed source realization, not sufficient conditions.")
    edge("all-order-compact-readout", sources["update"], "USED_BY", "HEURISTIC", sources["update"],
         "Exact transfer controls show why finitely many statistics cannot decide positivity.")
