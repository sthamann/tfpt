#!/usr/bin/env python3
"""Exact bounded selection audit; this is a counterexample space, not a model proposal."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
P0 = s.diag(1, 0)
P1 = s.diag(0, 1)
W = s.Matrix([[1, 0], [0, 0], [0, 0], [0, 1]])
PAULIS = [I, X, Y, Z]
checks: list[str] = []


def clean(m):
    return m.applyfunc(s.simplify) if isinstance(m, s.MatrixBase) else s.simplify(m)


def equal(a, b):
    d = clean(a - b)
    return d == (s.zeros(*d.shape) if isinstance(d, s.MatrixBase) else 0)


def require(label, condition):
    if condition is not True:
        raise RuntimeError(f"FAILED: {label}: {condition!r}")
    checks.append(label)


def eq(label, a, b):
    require(label, equal(a, b))


def partial_trace(matrix, keep):
    if keep == "system":
        return s.Matrix(2, 2, lambda a, b: sum(matrix[2*a+j, 2*b+j] for j in range(2)))
    return s.Matrix(2, 2, lambda a, b: sum(matrix[2*j+a, 2*j+b] for j in range(2)))


def expectation(rho, observable):
    return clean(s.trace(rho * observable))


def signature(rho, unitary):
    state = tuple(expectation(rho, p) for p in PAULIS)
    channel = tuple(clean(s.trace(q * unitary * p * unitary.H) / 2)
                    for q in PAULIS for p in PAULIS)
    return state + channel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve().parent != HERE:
        raise ValueError("Output must stay in this worker's directory")

    eq("record_isometry", W.H * W, I)
    candidates = []
    signatures = set()
    survivors = []
    rx = [I, (s.sqrt(3) * I - s.I * X) / 2]
    ry = [I, (s.sqrt(3) * I - s.I * Y) / 2]
    for a, b, c, d in itertools.product((0, 1), repeat=4):
        tag = f"{a}{b}{c}{d}"
        phase = s.I if c == 0 else -1
        p = s.Rational(1, 2) if d == 0 else s.Rational(1, 4)
        unitary = clean(s.diag(1, phase) * rx[a] * ry[b])
        psi = s.Matrix([s.sqrt(p), s.sqrt(1-p)])
        rho = psi * psi.H
        eq(f"{tag}:unitary", unitary.H * unitary, I)
        eq(f"{tag}:positive_pure_normalized_state", rho * rho, rho)
        eq(f"{tag}:state_trace", s.trace(rho), 1)
        sig = signature(rho, unitary)
        require(f"{tag}:distinct_marked_process", sig not in signatures)
        signatures.add(sig)

        # One fixed information -> reconstruction map for every candidate.
        reconstructed_state = sum((expectation(rho, q) * q / 2 for q in PAULIS), s.zeros(2))
        eq(f"{tag}:full_record_reconstruction_state", reconstructed_state, rho)
        for j, q in enumerate(PAULIS):
            out = unitary * q * unitary.H
            reconstructed = sum((s.trace(pj * out) * pj / 2 for pj in PAULIS), s.zeros(2))
            eq(f"{tag}:full_record_reconstruction_channel_{j}", reconstructed, out)

        # Historical record survives arbitrary subsequent local system dynamics.
        joint = W * rho * W.H
        evolution = s.kronecker_product(unitary, I)
        after = clean(evolution * joint * evolution.H)
        eq(f"{tag}:historical_record_invariant", partial_trace(after, "record"), s.diag(p, 1-p))
        eq(f"{tag}:global_purity_retained", after * after, after)
        eq(f"{tag}:record_event_internal", W.H * s.kronecker_product(I, Z) * W, Z)
        eq(f"{tag}:historical_pointer_operator_invariant",
           evolution.H * s.kronecker_product(I, Z) * evolution, s.kronecker_product(I, Z))

        # A stronger, different condition: the CURRENT event value never changes.
        fixed = equal(Z * unitary * Z, unitary)
        invariant = all(equal(unitary.H * q * unitary, q) for q in (P0, P1))
        require(f"{tag}:same_FZ_equals_QND", fixed == invariant)
        require(f"{tag}:QND_exactly_two_bits_removed", fixed == (a == 0 and b == 0))
        if fixed:
            survivors.append(tag)
            eq(f"{tag}:record_then_evolve_intertwines", evolution * W, W * unitary)
            require(f"{tag}:minimal_cyclic_dimension_two", s.Matrix.hstack(psi, unitary*psi).rank() == 2)
        candidates.append({"bits": tag, "p": str(p), "phase": str(phase),
                           "historical_record_stable": True, "current_record_stable": fixed,
                           "FZ_fixed": fixed, "full_reconstruction_fixed": True})

    require("sixteen_distinct_processes", len(signatures) == 16)
    require("four_FZ_fixed_processes", survivors == ["0000", "0001", "0010", "0011"])

    phase_pairs = []
    for p in (s.Rational(1, 2), s.Rational(1, 4)):
        psi = s.Matrix([s.sqrt(p), s.sqrt(1-p)])
        for phase, period in ((s.I, 4), (-1, 2)):
            unitary = s.diag(1, phase)
            row = {"p": str(p), "phase": str(phase), "period": period, "responses": []}
            for n in range(5):
                v = W * (unitary ** n) * psi
                rho = v * v.H
                eq(f"p={p}:phase={phase}:n={n}:same_record", partial_trace(rho, "record"), s.diag(p, 1-p))
                answer = expectation(rho, s.kronecker_product(X, X))
                expected = clean(2*s.sqrt(p*(1-p))*s.re(phase**n))
                eq(f"p={p}:phase={phase}:n={n}:global_phase", answer, expected)
                row["responses"].append(str(answer))
            eq(f"phase={phase}:period", unitary**period, I)
            require(f"phase={phase}:smallest_period", all(not equal(unitary**n, I) for n in range(1, period)))
            phase_pairs.append(row)

    # General pure-state preservation: the simple nonorthogonal pair obstructs copying.
    zero = s.Matrix([1, 0])
    plus = s.Matrix([1, 1]) / s.sqrt(2)
    overlap_before = (zero.H * plus)[0]
    overlap_after_cloning = overlap_before**2
    require("cloning_pair_has_incompatible_inner_products", not equal(overlap_before, overlap_after_cloning))
    pair_commutator = zero*zero.H * (plus*plus.H) - plus*plus.H * (zero*zero.H)
    require("broadcast_pair_noncommutes", not equal(pair_commutator, s.zeros(2)))
    copied_plus = W * plus
    copied_plus_rho = copied_plus * copied_plus.H
    eq("copy_preserves_global_purity", copied_plus_rho**2, copied_plus_rho)
    eq("copy_dephases_local_plus", partial_trace(copied_plus_rho, "system"), I/2)
    eq("copy_record_does_not_encode_input_phase", partial_trace(copied_plus_rho, "record"), I/2)

    # Exact partial-record tradeoff for equal branch weights and real overlap gamma.
    tradeoffs = []
    for gamma in (s.Integer(0), s.Rational(1, 2), s.Integer(1)):
        r0 = zero
        r1 = s.Matrix([gamma, s.sqrt(1-gamma**2)])
        v = (s.kronecker_product(zero, r0) + s.kronecker_product(s.Matrix([0, 1]), r1))/s.sqrt(2)
        rho = v*v.H
        visibility = expectation(partial_trace(rho, "system"), X)
        diff = r0*r0.H - r1*r1.H
        distinguishability_sq = clean(s.trace(diff**2)/2)
        eq(f"gamma={gamma}:visibility", visibility, gamma)
        eq(f"gamma={gamma}:pure_record_tradeoff", visibility**2 + distinguishability_sq, 1)
        tradeoffs.append({"record_overlap": str(gamma), "visibility": str(visibility),
                          "distinguishability_squared": str(distinguishability_sq)})

    # Two incompatible complete current-value records leave only scalar dynamics.
    aa, bb, cc, dd = s.symbols("aa bb cc dd")
    matrix = s.Matrix([[aa, bb], [cc, dd]])
    equations = list(matrix*X-X*matrix) + list(matrix*Z-Z*matrix)
    solution = s.linsolve(equations, (aa, bb, cc, dd))
    require("all_X_Z_values_invariant_implies_scalar", solution == s.FiniteSet((dd, 0, 0, dd)))

    # Every subset of a fixed finite universe is the fixed set of one idempotent
    # retraction (nonempty subset). Fixed-point syntax alone has no selectivity.
    omega = range(4)
    retractions = []
    for mask in range(1, 16):
        chosen = [x for x in omega if (mask >> x) & 1]
        retraction = [x if x in chosen else chosen[0] for x in omega]
        require(f"retraction_{mask}:idempotent", all(retraction[retraction[x]] == retraction[x] for x in omega))
        require(f"retraction_{mask}:exact_fixed_set", [x for x in omega if retraction[x] == x] == chosen)
        retractions.append({"fixed_set": chosen, "map": retraction})

    sources = [ROOT / "AGENTS.md",
               ROOT / "experiments/theory-contracts/universalraum-primitive-source-audit-20260915/RESULTS.md",
               ROOT / "experiments/theory-contracts/universalraum-primitive-source-audit-20260915/EINSEITER.md",
               Path("/Users/stefanhamann/.codex/attachments/b3a502d5-9938-4c56-9cf2-f0c80f004db6/pasted-text.txt"),
               Path(__file__).resolve()]
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result = {"status": "PASS_SCOPED_EXACT_AUDIT", "physical_selection_found": False,
              "scope": "16 declared two-state quantum counterprocesses, fixed observation dictionary",
              "sympy_version": s.__version__, "checks_count": len(checks), "checks": checks,
              "counts": {"before_processes": 16, "before_independent_bits": 4,
                         "A_composition_after": 16, "B_historical_after": 16,
                         "B_current_QND_or_C_FZ_after": 4, "after_QND_independent_bits": 2,
                         "delta_QND_bits": 2, "C_full_reconstruction_after": 16,
                         "D_minimal_cyclic_dimension_after_QND": 4,
                         "B_complete_unknown_state_preserving_record": "impossible, not a selection success"},
              "candidates": candidates, "same_record_distinct_processes": phase_pairs,
              "record_tradeoffs": tradeoffs, "idempotent_fixed_set_examples": retractions,
              "input_hashes_sha256": hashes,
              "first_unproved_implication": "Self-consistency or record existence selects the physical event algebra, phase, or state."}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "checks_count": len(checks),
                      "counts": result["counts"], "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
