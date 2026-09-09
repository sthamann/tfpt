"""Certified time-local auxiliary reduction, not a low-energy field theory.

The Krylov basis includes high states and depends on the declared preparation.
All construction, rounding, residual and source bounds use exact arithmetic.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import factorial, gcd, isqrt, lcm
from pathlib import Path

SCALE = 10**30
DEN = 14400
NAMES = ("bare_high_site0", "electric_zero_link0", "onsite_species_coherence", "Wilson_cycle_real")
PINS = {
    "checker.py": "8fd5069d391c3d3723e9d046f5089b6779eff94b960458a4bbe31d3f0e9ac382",
    "MEMORY_CLOSURE.md": "3b4141cf256b60ea173a5ae932b94f614d84be22a2d8af5531cd1699dcc60b1e",
    "validation.json": "59b9a55a5167b7766c307ecb08ae705d8e368ebd3e9dfb18e7eea92eda779df9",
}


def require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def inherited(root):
    directory = root/"experiments/theory-contracts/memory-closure-round34"
    for name, digest in PINS.items():
        path = directory/name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "Round34 source pin: "+name)
    path = directory/"checker.py"
    spec = importlib.util.spec_from_file_location("round34_auxiliary_parent", path)
    r34 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r34)
    return r34.inherited(root)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def matvec(rows, v):
    return [sum(a*v[j] for j, a in row.items()) for row in rows]


def primitive_lanczos(rows, initial, dimension):
    """Integer representatives of exactly orthogonal Krylov directions."""
    require(isinstance(dimension, int) and 2 <= dimension <= len(rows), "auxiliary dimension domain")
    require(0 <= initial < len(rows), "initial basis index")
    vectors = [[int(i == initial) for i in range(len(rows))]]
    norms, products = [1], []
    for j in range(dimension):
        v = vectors[j]
        Hv = matvec(rows, v)
        products.append(Hv)
        if j+1 == dimension:
            break
        alpha = F(dot(v, Hv), norms[j])
        beta = F(dot(vectors[j-1], Hv), norms[j-1]) if j else F(0)
        common = lcm(alpha.denominator, beta.denominator)
        previous = vectors[j-1] if j else [0]*len(rows)
        w = [common*a-int(common*alpha)*b-int(common*beta)*c
             for a, b, c in zip(Hv, v, previous)]
        divisor = 0
        for x in w:
            divisor = gcd(divisor, abs(x))
        require(divisor > 0, "Krylov space closed before requested dimension; choose smaller model")
        w = [x//divisor for x in w]
        require(all(dot(old, w) == 0 for old in vectors), "exact orthogonality, no floating reorthogonalization")
        vectors.append(w)
        norms.append(dot(w, w))
    return vectors, norms, products


def ratio_sqrt_floor(numerator, denominator, scale=SCALE):
    """Round numerator/sqrt(denominator) toward zero, on a 1/scale grid."""
    require(denominator > 0 and scale > 0, "positive square-root denominator and scale")
    magnitude = isqrt(numerator*numerator*scale*scale//denominator)
    return magnitude if numerator >= 0 else -magnitude


def sqrt_upper(value, scale=10**40):
    value = F(value)
    require(value >= 0, "nonnegative squared norm")
    integer = isqrt(value.numerator*scale*scale//value.denominator)
    if integer*integer*value.denominator < value.numerator*scale*scale:
        integer += 1
    return F(integer, scale)


def rounded_model(vectors, norms, products, scale=SCALE):
    dimension = len(vectors)
    V = [[ratio_sqrt_floor(x, n, scale) for x in v] for v, n in zip(vectors, norms)]
    A = [{} for _ in vectors]
    for i in range(dimension):
        diagonal = F(dot(vectors[i], products[i]), DEN*norms[i])
        A[i][i] = int(diagonal*scale)
        for j in range(i):
            cross = dot(vectors[i], products[j])
            if j+1 == i:
                value = ratio_sqrt_floor(cross, DEN**2*norms[i]*norms[j], scale)
                require(value > 0, "positive oriented Lanczos off-diagonal")
                A[i][j] = A[j][i] = value
            else:
                require(cross == 0, "exact parent projection is tridiagonal")
    return V, A


def defect_norms(rows, V, A, scale=SCALE):
    """Exact residual HV-VA, with a certified norm bound for each column."""
    norms = []
    for j, v in enumerate(V):
        hv = matvec(rows, v)
        residual = [scale*hv[i]-DEN*sum(A[k].get(j, 0)*V[k][i] for k in range(len(V)))
                    for i in range(len(rows))]
        norms.append(sqrt_upper(F(dot(residual, residual), (DEN*scale**2)**2)))
    return norms


def integrated_arrival(A, degree=80, scale=SCALE):
    """Upper bound on integral_0^1 |(exp(-itA)e0)[-1]| dt.

Use the diagonal interaction picture and the positive off-diagonal path sum.
The scalar tail includes all paths beyond the computed degree.
"""
    B = [{j: abs(a) for j, a in row.items() if j != i} for i, row in enumerate(A)]
    radius = F(max(sum(row.values()) for row in B), scale)
    require(degree >= 0 and radius < degree+3, "positive path-series tail domain")
    vector = [int(i == 0) for i in range(len(A))]
    partial = F(0)
    for n in range(degree+1):
        partial += F(vector[-1], scale**n*factorial(n+1))
        vector = matvec(B, vector)
    tail = radius**(degree+1)/factorial(degree+2)/(1-radius/F(degree+3))
    return partial+tail, radius, tail


def unitary_vector(A, degree=80, scale=SCALE):
    require(isinstance(degree, int) and degree >= 0 and scale > 0, "unitary polynomial domain")
    require(all(A[j].get(i, 0) == a for i, row in enumerate(A) for j, a in row.items()),
            "Hermitian auxiliary generator")
    re, im, denominator = [int(i == 0) for i in range(len(A))], [0]*len(A), 1
    for k in range(degree, 0, -1):
        re, im = matvec(A, im), [-x for x in matvec(A, re)]
        denominator *= scale*k
        re[0] += denominator
    radius = F(max(sum(abs(a) for a in row.values()) for row in A), scale)
    tail = radius**(degree+1)/factorial(degree+1)
    norm2 = F(dot(re, re)+dot(im, im), denominator**2)
    require(max(F(0), 1-tail)**2 <= norm2 <= (1+tail)**2, "auxiliary unitary Taylor norm")
    return re, im, denominator, tail, radius


def doubled_observable(r33, basis, name):
    """Sparse 2*O; Wilson entries are integral without half-rounding."""
    index = {key: i for i, key in enumerate(basis)}
    rows = [{} for _ in basis]
    for j, (mask, k) in enumerate(basis):
        if name in ("bare_high_site0", "electric_zero_link0"):
            value = (mask >> 3) & 1 if name == "bare_high_site0" else int(r33.gauss_flux(mask, k)[0] == 0)
            if value:
                rows[j][j] = 2
        elif name == "onsite_species_coherence":
            moved = r33.move(mask, 0, 3)
            if moved is not None:
                out, sign = moved
                i = index.get((out, k))
                if i is not None:
                    rows[i][j] = rows[j][i] = 2*sign
        elif name == "Wilson_cycle_real":
            i = index.get((mask, k+1))
            if i is not None:
                rows[i][j] = rows[j][i] = 1
        else:
            raise ValueError("unknown physical observable")
    return rows


def compress_sources(r33, basis, V):
    result = {}
    for name in NAMES:
        O = doubled_observable(r33, basis, name)
        applied = [matvec(O, v) for v in V]
        result[name] = [[dot(v, w) for w in applied] for v in V]
    return result


def reduced_readout(O, state, scale=SCALE):
    re, im, denominator = state[:3]
    return F(sum(O[i][j]*(re[i]*re[j]+im[i]*im[j]) for i in range(len(O)) for j in range(len(O))),
             2*scale**2*denominator**2)


@lru_cache(maxsize=3)
def build(root_text, cutoff=12, dimension=20):
    r33 = inherited(Path(root_text))
    basis, rows, initial, center = r33.physical_cycle(cutoff)
    vectors, norms, products = primitive_lanczos(rows, initial, dimension)
    V, A = rounded_model(vectors, norms, products)
    defects = defect_norms(rows, V, A)
    arrival, path_radius, path_tail = integrated_arrival(A)
    initial_error = sqrt_upper(F(sum((v-int(i == initial)*SCALE)**2 for i, v in enumerate(V[0])), SCALE**2))
    defect_error = initial_error+sum(defects[:-1])+defects[-1]*arrival
    sources = compress_sources(r33, basis, V)
    state = unitary_vector(A)
    embedding_error = sqrt_upper(F(len(basis)*dimension, SCALE**2))
    total_vector_error = defect_error+(1+embedding_error)*state[3]
    error = 4*r33.dyson_tail(cutoff)+total_vector_error*(2+total_vector_error)
    values = {name: reduced_readout(O, state) for name, O in sources.items()}
    return {"basis": basis, "rows": rows, "initial": initial, "center": center,
            "vectors": vectors, "norms": norms, "V": V, "A": A, "sources": sources,
            "state": state, "defects": defects, "arrival": arrival, "path_radius": path_radius,
            "path_tail": path_tail, "defect_error": defect_error, "error": error,
            "embedding_error": embedding_error, "values": values,
            "intervals": {name: r33.enclose(value, error) for name, value in values.items()}}


def upper_string(value, digits=40):
    scale = 10**digits
    return str(F((value*scale).__ceil__(), scale))


def interval(value, error, digits=14):
    scale = 10**digits
    lo, hi = ((value-error)*scale).__floor__(), ((value+error)*scale).__ceil__()
    decimal = lambda n: ("-" if n < 0 else "")+f"{abs(n)//scale}.{abs(n)%scale:0{digits}d}"
    return {"lower": str(F(lo, scale)), "upper": str(F(hi, scale)),
            "decimal_lower": decimal(lo), "decimal_upper": decimal(hi), "width": str(F(hi-lo, scale))}


def model_payload(c, cutoff=12):
    """Only online data and inherited error budgets; no parent, basis or memory."""
    return {"format": "TFPT_AUXILIARY_CYCLE_V1", "cutoff": cutoff,
            "dimension": len(c["A"]), "initial_auxiliary_index": 0,
            "time_domain": ["0", "1"], "hamiltonian_denominator": str(SCALE),
            "hamiltonian_rows": [{str(j): str(a) for j, a in row.items()} for row in c["A"]],
            "source_numerators": {name: [[str(a) for a in row] for row in matrix]
                                  for name, matrix in c["sources"].items()},
            "source_denominator": str(2*SCALE**2),
            "certified_vector_defect_upper_on_time_domain": upper_string(c["defect_error"]),
            "embedding_roundoff_norm_upper": upper_string(c["embedding_error"]),
            "bounded_interaction_norm_upper": "97/192",
            "parent_provenance": PINS, "physical_gates_closed": [],
            "scope": "Prepared-state auxiliary realization, includes high states. Not a low-energy spectral EFT or uniform 3D model."}


def solve_compiled(model, time=F(1), degree=80):
    """Self-contained time-local evolution with reduced-only source readout.

Uses the certified model's error budgets; validating those budgets against the
parent is the separate build/replay workflow, not a claim about arbitrary JSON.
"""
    require(model["format"] == "TFPT_AUXILIARY_CYCLE_V1", "supported compiled format")
    time = F(time)
    require(F(0) <= time <= F(1), "compiled model certified only on 0<=t<=1")
    require(model["initial_auxiliary_index"] == 0 and model["time_domain"] == ["0", "1"], "fixed compiled preparation/domain")
    dimension, scale = model["dimension"], int(model["hamiltonian_denominator"])
    A = [{int(j): int(a) for j, a in row.items()} for row in model["hamiltonian_rows"]]
    require(len(A) == dimension and dimension >= 2 and scale > 0, "compiled matrix dimension/scale")
    require(all(0 <= j < dimension for row in A for j in row), "compiled matrix indices")
    timed = [{j: a*time.numerator for j, a in row.items()} for row in A]
    state = unitary_vector(timed, degree, scale*time.denominator)
    sources = {name: [[int(a) for a in row] for row in model["source_numerators"][name]] for name in NAMES}
    require(int(model["source_denominator"]) == 2*scale**2, "compiled source scale")
    for O in sources.values():
        require(len(O) == dimension and all(len(row) == dimension for row in O), "compiled source dimension")
        require(all(O[i][j] == O[j][i] for i in range(dimension) for j in range(dimension)), "Hermitian compiled source")
    embedding = F(model["embedding_roundoff_norm_upper"])
    defect = F(model["certified_vector_defect_upper_on_time_domain"])
    require(embedding >= 0 and defect >= 0, "nonnegative certified error budgets")
    delta = defect+(1+embedding)*state[3]
    x, K = F(model["bounded_interaction_norm_upper"])*time, model["cutoff"]
    require(isinstance(K, int) and K >= 0 and 0 <= x < K+2, "compiled rotor-tail domain")
    rotor = x**(K+1)/factorial(K+1)/(1-x/F(K+2))
    error = 4*rotor+delta*(2+delta)
    values = {name: reduced_readout(O, state, scale) for name, O in sources.items()}
    return {"time": str(time), "dimension": dimension,
            "readouts": {name: interval(value, error) for name, value in values.items()},
            "full_rotor_readout_error_upper": upper_string(error, 22),
            "parent_or_high_state_reconstruction_used": False,
            "certification": "Uses certified compiled budgets; full provenance and residual verification require the build/replay workflow."}


def certificate(root, dimension=20):
    inherited(root)  # Mandatory even when the construction is cached.
    c = build(str(root), 12, dimension)
    model = model_payload(c)
    answer = solve_compiled(model)
    require(answer["readouts"] == c["intervals"], "standalone and construction interval identity")
    frozen = json.loads((root/"experiments/theory-contracts/memory-closure-round34/validation.json").read_text())
    ref = next(row for row in frozen["cycle_certificates"] if row["cutoff"] == 12)["readouts_at_time_one"]
    comparison = "IDENTICAL" if answer["readouts"] == ref else "OVERLAPPING_WIDER_BOUNDS"
    for name in NAMES:
        a, b = answer["readouts"][name], ref[name]
        require(F(a["lower"]) <= F(b["upper"]) and F(b["lower"]) <= F(a["upper"]), "independent parent reference overlap")
    if dimension == 20:
        require(comparison == "IDENTICAL", "20-state model reproduces all frozen intervals without fitting")
        require(c["defect_error"] < F(332, 10**21), "certified auxiliary vector defect below 3.32e-19")
    model_text = json.dumps(model, sort_keys=True, indent=2)+"\n"
    return {"dimension": dimension, "full_cutoff_dimension": len(c["basis"]),
            "retains_high_state_information": True, "low_energy_spectral_model": False,
            "time_local_Hermitian_generator": True, "initial_preparation_unchanged": True,
            "comparison_to_frozen_intervals": comparison, "readouts_at_time_one": answer["readouts"],
            "vector_defect_upper_on_0_to_1": upper_string(c["defect_error"]),
            "last_defect_column_norm_upper": upper_string(c["defects"][-1]),
            "other_defect_column_norms_sum_upper": upper_string(sum(c["defects"][:-1])),
            "integrated_last_component_upper": upper_string(c["arrival"]),
            "positive_path_norm_upper": upper_string(c["path_radius"]),
            "full_rotor_readout_error_upper": answer["full_rotor_readout_error_upper"],
            "online_hamiltonian_nonzeros": sum(len(row) for row in c["A"]),
            "online_real_Horner_coefficient_visits": 2*80*sum(len(row) for row in c["A"]),
            "full_real_Horner_coefficient_visits": 2*80*sum(len(row) for row in c["rows"]),
            "online_source_integer_slots": sum(len(O)**2 for O in c["sources"].values()),
            "offline_basis_integer_slots": len(c["basis"])*dimension,
            "offline_basis_max_integer_bits": max(abs(x).bit_length() for v in c["vectors"] for x in v),
            "compiled_model_bytes": len(model_text.encode()),
            "compiled_model_sha256": hashlib.sha256(model_text.encode()).hexdigest(),
            "cost_claim": "Smaller online state and matrix counts, not an end-to-end speedup or volume-uniform low-energy theory."}


def run(root):
    return {"status": "PASS", "verdict": "CERTIFIED_20_STATE_TIME_LOCAL_AUXILIARY_REALIZATION",
            "certificates": [certificate(root, m) for m in (12, 16, 20)],
            "inherited_pins": PINS, "physical_gates_closed": [],
            "scope": "Same prepared three-site cycle with high-state auxiliary information. No low-energy spectral elimination, uniform 3D EFT, selected parameters/state, chiral SM, continuum gravity, TOE or RH proof."}


def payload(root):
    result = run(root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("checker.py", "AUXILIARY_REDUCTION.md", "README.md", "test_checker.py")}
    return json.dumps(result, indent=2, sort_keys=True)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write-model", type=Path)
    parser.add_argument("--model", type=Path, help="Run the compiled model without loading a parent repository")
    parser.add_argument("--time", type=F, default=F(1))
    args = parser.parse_args()
    if args.model:
        require(args.write_model is None, "do not compile while running standalone")
        result = json.dumps(solve_compiled(json.loads(args.model.read_text()), args.time), indent=2, sort_keys=True)+"\n"
    else:
        result = payload(args.repo)
        if args.write_model:
            model = model_payload(build(str(args.repo), 12, 20))
            args.write_model.write_text(json.dumps(model, indent=2, sort_keys=True)+"\n")
    if args.output:
        args.output.write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
