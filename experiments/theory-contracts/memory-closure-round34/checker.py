"""Closed retained-amplitude memory evolution and exact source reconstruction.

NON-RH / unpromoted. Eliminated amplitudes are not independent evolution
variables, but their information and substantial costs remain in compiled
memory/source kernels. This is not a memoryless low-energy Hamiltonian.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import factorial
from pathlib import Path

PINS = {
    "checker.py": "588afda3ef5ad6c615dcffc77d5be868153bc288d8f15eef90ca121d4d5ad413",
    "CYCLE_DYNAMICS.md": "01c8cfea79e6bb755ca05e1a60c6811f3a50b437359abbba7638b5c1a28db904",
    "validation.json": "583bfa48bcd32e927b8660d0e80c9a15b93f1c30febed5610b770302f933738e",
}
DEN = 14400
NAMES = ("bare_high_site0", "electric_zero_link0", "onsite_species_coherence", "Wilson_cycle_real")


def require(condition, name):
    if not bool(condition):
        raise ValueError(name)


def inherited(root):
    directory = root/"experiments/theory-contracts/local-flux-dynamics-round33"
    for name, digest in PINS.items():
        path = directory/name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "Round33 source pin: "+name)
    spec = importlib.util.spec_from_file_location("round33_memory_input", directory/"checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.inherited(root)
    return module


def split_parent(basis, rows, initial):
    low = [i for i, (mask, _) in enumerate(basis) if mask == 7]
    high = [i for i, (mask, _) in enumerate(basis) if mask != 7]
    ip, iq = {v: j for j, v in enumerate(low)}, {v: j for j, v in enumerate(high)}
    require(initial in ip, "unchanged bare low initial state lies in retained sector")
    L = [{ip[j]: a for j, a in rows[i].items() if j in ip and a} for i in low]
    D = [{iq[j]: a for j, a in rows[i].items() if j in iq and a} for i in high]
    C = [[rows[i].get(j, 0) for j in low] for i in high]
    Ct = [[(j, C[j][i]) for j in range(len(high)) if C[j][i]] for i in range(len(low))]
    require(all(row.keys() <= {i} for i, row in enumerate(L)), "actual bare-low block is diagonal")
    require(all(rows[low[i]].get(high[j], 0) == C[j][i]
                for i in range(len(low)) for j in range(len(high))), "physical cross-block adjoint")
    return {"low_indices": low, "high_indices": high, "L": L, "D": D,
            "C": C, "Ct": Ct, "initial_low": ip[initial]}


def sparse_times_dense(A, B):
    columns = len(B[0])
    result = []
    for row in A:
        out = [0]*columns
        for j, coefficient in row.items():
            source = B[j]
            for k in range(columns):
                out[k] += coefficient*source[k]
        result.append(out)
    return result


def left_cross(Ct, B):
    columns = len(B[0])
    return [[sum(coefficient*B[j][k] for j, coefficient in row) for k in range(columns)] for row in Ct]


def digest_matrices(matrices):
    digest = hashlib.sha256()
    for matrix in matrices:
        digest.update(f"{len(matrix)}:{len(matrix[0])}\n".encode())
        for row in matrix:
            digest.update((",".join(map(str, row))+"\n").encode())
    return digest.hexdigest()


@lru_cache(maxsize=2)
def compile_cycle(root_text, cutoff=12, degree=80):
    require(isinstance(degree, int) and degree >= 2, "memory polynomial degree >=2")
    r33 = inherited(Path(root_text))
    basis, rows, initial, center = r33.physical_cycle(cutoff)
    blocks = split_parent(basis, rows, initial)
    # All matrices are powers of the integer parent DEN*(H-center).
    source_maps, kernels = [], []
    B = blocks["C"]
    for order in range(degree):
        source_maps.append(B)
        if order < degree-1:
            K = left_cross(blocks["Ct"], B)
            require(all(K[i][j] == K[j][i] for i in range(len(K)) for j in range(len(K))),
                    "each exact C^T D^r C memory moment is symmetric")
            kernels.append(K)
        if order+1 < degree:
            B = sparse_times_dense(blocks["D"], B)
    np, nq = len(blocks["low_indices"]), len(blocks["high_indices"])
    K0 = kernels[0]
    require(all(K0[i][j] == 0 for i in range(np) for j in range(np) if i != j),
            "instantaneous return kernel is diagonal")
    require(F(K0[blocks["initial_low"]][blocks["initial_low"]], DEN**2) == F(1, 96),
            "actual initial departure coefficient")
    if cutoff >= 1 and degree >= 3:
        require(all(F(kernels[1][i+1][i], DEN**3) == -F(1, 2304) for i in range(np-1)),
                "same memory kernel generates the elementary Wilson return path")
    radius = F(max(sum(abs(a) for a in row.values()) for row in rows), DEN)
    return {"basis": basis, "rows": rows, "initial": initial, "center": center,
            "blocks": blocks, "source_maps": source_maps, "kernels": kernels,
            "degree": degree, "cutoff": cutoff, "radius": radius,
            "kernel_sha256": digest_matrices(kernels), "source_maps_sha256": digest_matrices(source_maps),
            "kernel_integer_slots": (degree-1)*np*np,
            "source_integer_slots": degree*nq*np}


def low_jets(L, kernels, initial, degree):
    """Closed online recurrence: no high matrix, high state or full propagator."""
    require(degree >= 2 and len(kernels) >= degree-1, "complete requested memory moments")
    np = len(L)
    require(0 <= initial < np, "retained initial index")
    p0 = [int(i == initial) for i in range(np)]
    jets = [p0, [sum(a*p0[j] for j, a in row.items()) for row in L]]
    for n in range(1, degree):
        nextjet = [sum(a*jets[n][j] for j, a in row.items()) for row in L]
        for r in range(n):
            vector = jets[n-1-r]
            active = [(j, v) for j, v in enumerate(vector) if v]
            for i, row in enumerate(kernels[r]):
                nextjet[i] += sum(row[j]*v for j, v in active)
        jets.append(nextjet)
    return jets


def polynomial_weights(degree):
    weights = [0]*(degree+1)
    weights[degree] = 1
    for n in range(degree-1, -1, -1):
        weights[n] = weights[n+1]*DEN*(n+1)
    return weights, weights[0]


def source_readout_vectors(jets, source_maps):
    """Factorized source functional of low history, evaluated only at readout.

High components are reconstructed, not advanced as independent state variables.
This step explicitly retains their dimension and their cost.
"""
    degree, np = len(jets)-1, len(jets[0])
    require(len(source_maps) >= degree, "complete source reconstruction moments")
    nq = len(source_maps[0])
    weights, denominator = polynomial_weights(degree)
    low_re, low_im = [0]*np, [0]*np
    for n, vector in enumerate(jets):
        target = low_re if n % 2 == 0 else low_im
        sign = (1, -1, -1, 1)[n % 4]
        for j in range(np):
            target[j] += sign*weights[n]*vector[j]
    high_re, high_im = [0]*nq, [0]*nq
    for r in range(degree):
        integrated_re, integrated_im = [0]*np, [0]*np
        for j in range(degree-r):
            n = r+j+1
            target = integrated_re if n % 2 == 0 else integrated_im
            coefficient = (1, -1, -1, 1)[n % 4]*weights[n]
            for k in range(np):
                target[k] += coefficient*jets[j][k]
        active_re = [(j, v) for j, v in enumerate(integrated_re) if v]
        active_im = [(j, v) for j, v in enumerate(integrated_im) if v]
        for i, row in enumerate(source_maps[r]):
            high_re[i] += sum(row[j]*v for j, v in active_re)
            high_im[i] += sum(row[j]*v for j, v in active_im)
    return low_re, low_im, high_re, high_im, denominator


def assemble_readout(c, reconstructed):
    pr, pi, qr, qi, denominator = reconstructed
    re, im = [0]*len(c["basis"]), [0]*len(c["basis"])
    for indices, real, imag in ((c["blocks"]["low_indices"], pr, pi), (c["blocks"]["high_indices"], qr, qi)):
        for i, a, b in zip(indices, real, imag):
            re[i], im[i] = a, b
    return re, im, denominator


def memory_persistence_bound(kernel_zero, source_dimension):
    """Finite-cutoff Cesaro mean of |<c,exp(-iDt)c>|^2, not a pointwise bound."""
    require(kernel_zero > 0 and isinstance(source_dimension, int) and source_dimension > 0,
            "nonzero source and positive eliminated dimension")
    return kernel_zero**2/source_dimension


@lru_cache(maxsize=2)
def solve_cycle(root_text, cutoff=12, degree=80):
    c = compile_cycle(root_text, cutoff, degree)
    blocks = c["blocks"]
    jets = low_jets(blocks["L"], c["kernels"], blocks["initial_low"], degree)
    reconstructed = source_readout_vectors(jets, c["source_maps"])
    return jets, reconstructed


def certificate(root, cutoff=12, degree=80):
    # Recheck provenance even on cache hits; no cached source bypass.
    r33 = inherited(root)
    c = compile_cycle(str(root), cutoff, degree)
    _, reconstructed = solve_cycle(str(root), cutoff, degree)
    re, im, denominator = assemble_readout(c, reconstructed)
    tail = c["radius"]**(degree+1)/factorial(degree+1)
    require(tail < F(1, 10**30), "exact finite-polynomial tail bound")
    norm2 = F(sum(a*a+b*b for a, b in zip(re, im)), denominator**2)
    require((1-tail)**2 <= norm2 <= (1+tail)**2, "reconstructed total state norm enclosure")
    error = 4*r33.dyson_tail(cutoff)+tail*(2+tail)
    source_values = {name: r33.expectation(c["basis"], re, im, denominator, name) for name in NAMES}
    values = {name: r33.enclose(value, error) for name, value in source_values.items()}
    reference = json.loads((root/"experiments/theory-contracts/local-flux-dynamics-round33/validation.json").read_text())
    matching = next(row for row in reference["cycle_dynamics"] if row["cutoff"] == cutoff)
    require(values == matching["readouts_at_time_one"], "independently closed memory solution reproduces all frozen readout intervals")
    pr, pi, qr, qi, _ = reconstructed
    survival = F(sum(a*a+b*b for a, b in zip(pr, pi)), denominator**2)
    require(survival+error < 1, "bare retained propagator is not unitary")
    bare_re, bare_im = re.copy(), im.copy()
    for i in c["blocks"]["high_indices"]:
        bare_re[i] = bare_im[i] = 0
    missing_sources = {name: r33.enclose(source_values[name]-r33.expectation(c["basis"], bare_re, bare_im, denominator, name),
                                        2*error) for name in NAMES}
    return {"cutoff": cutoff, "polynomial_degree": degree,
            "retained_evolution_components": len(pr), "eliminated_kernel_components": len(qr),
            "full_reference_components": len(re),
            "low_only_evolution_has_memory": True, "independent_high_state_evolution_performed": False,
            "high_components_reconstructed_at_readout": True,
            "memory_moment_count": len(c["kernels"]), "source_moment_count": len(c["source_maps"]),
            "memory_integer_slots": c["kernel_integer_slots"], "source_integer_slots": c["source_integer_slots"],
            "memory_moments_sha256": c["kernel_sha256"], "source_moments_sha256": c["source_maps_sha256"],
            "initial_kernel_diagonal": "1/96", "initial_survival_second_derivative": "-1/48",
            "neighbor_first_kernel_moment": "-1/2304",
            "finite_cutoff_memory_mean_square_lower": str(memory_persistence_bound(F(1, 96), len(qr))),
            "memory_decay_or_finite_history_window_proved": False,
            "readouts_at_time_one": values, "all_bare_low_survival": r33.enclose(survival, error),
            "full_minus_undressed_projected_readouts": missing_sources,
            "full_rotor_readout_error_upper": str(F((error*10**18).__ceil__(), 10**18)),
            "comparison_to_frozen_Round33_intervals": "IDENTICAL",
            "cost_claim": "No speedup claimed: the high sector remains in offline memory/source compilation and readout reconstruction."}


def run(root):
    return {"status": "PASS", "verdict": "CLOSED_MEMORY_EVOLUTION_WITH_SOURCE_RECONSTRUCTION",
            "inherited_pins": PINS, "cycle_certificates": [certificate(root, K) for K in (8, 12)],
            "physical_gates_closed": [], "memoryless_low_Hamiltonian_proved": False,
            "scope": "Closed, evaluated retained-amplitude memory equation for the unchanged bare-prepared cycle, with full-rotor and source errors. Not a uniform 3D low-energy EFT, selected state, chiral SM, graviton, TOE or RH proof."}


def payload(root):
    result = run(root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("checker.py", "MEMORY_CLOSURE.md", "README.md", "test_checker.py")}
    return json.dumps(result, indent=2, sort_keys=True)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = payload(args.repo)
    if args.output:
        args.output.write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
