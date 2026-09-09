"""One certified reduced generator for a coherent physical preparation family.

Decimal arithmetic proposes a block basis; every accepted bound is subsequently
checked with exact integer/rational arithmetic. NON-RH, no T1-T8 promotion.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import factorial
from pathlib import Path

SCALE = 10**30
DEN = 14400
SEEDS = (-1, 0, 1)
PINS = {
    "checker.py": "4cacbc56cc199e438640f94d9f40c9352d25886db3be4d216111a2bbd40d3c4d",
    "AUXILIARY_REDUCTION.md": "52c34de1a14be773ca22f679ee01a26af020ff306484309cad056517554fba72",
    "validation.json": "28463d75dd42c622d43ff8e3d3feb2cca7e5a8c25b0ac8d423c4ce9c34692e8b",
}
NAMES = ("bare_high_site0", "electric_zero_link0", "onsite_species_coherence", "Wilson_cycle_real")


def require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def inherited(root):
    directory = root/"experiments/theory-contracts/auxiliary-dynamics-round35"
    for name, digest in PINS.items():
        path = directory/name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "Round35 source pin: "+name)
    spec = importlib.util.spec_from_file_location("round35_coherent_parent", directory/"checker.py")
    r35 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r35)
    return r35, r35.inherited(root)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def matvec(rows, vector):
    return [sum(a*vector[j] for j, a in row.items()) for row in rows]


def propose_block_basis(rows, seeds, layers, precision=80):
    require(isinstance(layers, int) and layers >= 2, "at least two block layers")
    require(len(set(seeds)) == len(seeds) and all(0 <= i < len(rows) for i in seeds), "distinct physical preparation seeds")
    require(precision >= 50, "basis proposal precision >=50")
    with localcontext() as context:
        context.prec = precision
        basis = [[Decimal(int(i == seed)) for i in range(len(rows))] for seed in seeds]
        layer_labels = [0]*len(seeds)
        active = list(range(len(seeds)))
        for layer in range(1, layers):
            following = []
            for index in active:
                w = matvec(rows, basis[index])
                for _ in range(2):
                    for q in basis:
                        projection = dot(q, w)
                        w = [a-projection*b for a, b in zip(w, q)]
                norm2 = dot(w, w)
                if norm2 < Decimal("1e-90"):
                    continue  # Proposal deflation only; exact residual validates the result.
                norm = norm2.sqrt()
                basis.append([a/norm for a in w])
                layer_labels.append(layer)
                following.append(len(basis)-1)
            require(following, "proposal exhausted before requested block depth")
            active = following
        return [[int(a*SCALE) for a in q] for q in basis], layer_labels


def certify_model(rows, V, labels, seeds, r35):
    m = len(V)
    require(len(labels) == m and len(V[0]) == len(rows), "basis shape")
    for j, seed in enumerate(seeds):
        require(V[j] == [SCALE*int(i == seed) for i in range(len(rows))], "unchanged whole input embedding")
    gram = [[dot(v, w) for w in V] for v in V]
    require(all(gram[i][j] == int(i == j)*SCALE**2 for i in range(len(seeds)) for j in range(m)),
            "whole preparation block remains exactly orthogonal to later directions")
    gram_error = F(max(sum(abs(a-int(i == j)*SCALE**2) for j, a in enumerate(row))
                       for i, row in enumerate(gram)), SCALE**2)
    require(gram_error < F(1, 10**25), "exact well-conditioned near-isometry")
    HV = [matvec(rows, v) for v in V]
    A = [{} for _ in V]
    for i in range(m):
        for j in range(i+1):
            if abs(labels[i]-labels[j]) <= 1:
                a = int(F(dot(V[i], HV[j]), DEN*SCALE))
                if a:
                    A[i][j] = A[j][i] = a
    defects = r35.defect_norms(rows, V, A)
    return A, defects, gram_error


def family_defect_bound(A, defects, input_count, r35, degree=100):
    """Residual response bound uniform over the unit sphere in C^input_count."""
    B = [{j: abs(a) for j, a in row.items() if j != i} for i, row in enumerate(A)]
    radius = F(max(sum(row.values()) for row in B), SCALE)
    require(radius < degree+3 and degree >= 0, "positive family path-tail domain")
    tail = radius**(degree+1)/factorial(degree+2)/(1-radius/F(degree+3))
    columns = []
    for seed in range(input_count):
        vector = [int(i == seed) for i in range(len(A))]
        integral = [F(0)]*len(A)
        for n in range(degree+1):
            denominator = SCALE**n*factorial(n+1)
            integral = [v+F(a, denominator) for v, a in zip(integral, vector)]
            vector = matvec(B, vector)
        columns.append(sum(d*(v+tail) for d, v in zip(defects, integral)))
    return r35.sqrt_upper(sum(e*e for e in columns)), columns, radius, tail


def input_evolution(A, count, time=F(1), degree=80):
    require(isinstance(degree, int) and degree >= 0, "Taylor degree")
    require(all(A[j].get(i, 0) == a for i, row in enumerate(A) for j, a in row.items()), "Hermitian common generator")
    time = F(time)
    require(0 <= time <= 1, "family certified on 0<=t<=1")
    require(1 <= count <= len(A), "input count")
    timed = [{j: a*time.numerator for j, a in row.items()} for row in A]
    scale = SCALE*time.denominator
    result = []
    for seed in range(count):
        re, im, den = [int(i == seed) for i in range(len(A))], [0]*len(A), 1
        for k in range(degree, 0, -1):
            re, im = matvec(timed, im), [-a for a in matvec(timed, re)]
            den *= scale*k
            re[seed] += den
        result.append((re, im))
    radius = F(max(sum(abs(a) for a in row.values()) for row in timed), scale)
    return result, den, radius**(degree+1)/factorial(degree+1)


def response_matrices(sources, columns, denominator):
    """3x3 Hermitian responses retain real AND imaginary off-diagonal entries."""
    result = {}
    for name, O in sources.items():
        applied = [([dot(row, re) for row in O], [dot(row, im) for row in O]) for re, im in columns]
        real, imag = [], []
        scale = 2*SCALE**2*denominator**2
        for re, im in columns:
            real.append([F(dot(re, a)+dot(im, b), scale) for a, b in applied])
            imag.append([F(dot(re, b)-dot(im, a), scale) for a, b in applied])
        require(all(real[i][j] == real[j][i] and imag[i][j] == -imag[j][i]
                    for i in range(len(columns)) for j in range(len(columns))), "exact Hermitian response matrix")
        result[name] = (real, imag)
    return result


@lru_cache(maxsize=3)
def build(root_text, layers=20, cutoff=13, precision=80):
    r35, r33 = inherited(Path(root_text))
    require(cutoff >= 2, "electric cutoff includes declared preparation margin")
    physical, rows, _, center = r33.physical_cycle(cutoff)
    seeds = [physical.index((7, k)) for k in SEEDS]
    V, labels = propose_block_basis(rows, seeds, layers, precision)
    A, defects, gram_error = certify_model(rows, V, labels, seeds, r35)
    delta, columns, radius, path_tail = family_defect_bound(A, defects, len(seeds), r35)
    sources = r35.compress_sources(r33, physical, V)
    states, den, taylor = input_evolution(A, len(seeds))
    # Norm of the whole matrix remainder, not sqrt(3) copies of scalar tests.
    d = delta+(1+gram_error)*taylor
    error = 4*r33.dyson_tail(cutoff-max(map(abs, SEEDS)))+d*(2+d)
    response = response_matrices(sources, states, den)
    return {"basis": physical, "rows": rows, "seeds": seeds, "center": center,
            "V": V, "labels": labels, "A": A, "sources": sources,
            "gram_error": gram_error, "defects": defects, "delta": delta,
            "column_bounds": columns, "path_radius": radius, "path_tail": path_tail,
            "states": states, "denominator": den, "taylor_tail": taylor,
            "error": error, "response": response, "layers": layers, "cutoff": cutoff}


def pure_density(coefficients):
    require(len(coefficients) == 3, "three complex preparation coefficients")
    values = [(F(a), F(b)) for a, b in coefficients]
    norm2 = sum(a*a+b*b for a, b in values)
    require(norm2 > 0, "nonzero preparation vector")
    real = [[(a*c+b*d)/norm2 for c, d in values] for a, b in values]
    imag = [[(b*c-a*d)/norm2 for c, d in values] for a, b in values]
    return real, imag


def validate_density(density):
    real, imag = density
    require(len(real) == len(imag) == 3 and all(len(row) == 3 for matrix in density for row in matrix), "3x3 density shape")
    real, imag = [[F(a) for a in row] for row in real], [[F(a) for a in row] for row in imag]
    require(all(real[i][j] == real[j][i] and imag[i][j] == -imag[j][i] for i in range(3) for j in range(3)), "Hermitian density")
    require(sum(real[i][i] for i in range(3)) == 1, "density trace one")
    require(all(real[i][i] >= 0 for i in range(3)), "nonnegative density diagonal")
    require(all(real[i][i]*real[j][j] >= real[i][j]**2+imag[i][j]**2 for i in range(3) for j in range(i)), "density 2x2 principal minors")
    multiply = lambda z, w: (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
    cycle = multiply(multiply((real[0][1], imag[0][1]), (real[1][2], imag[1][2])), (real[2][0], imag[2][0]))
    det = (real[0][0]*real[1][1]*real[2][2]+2*cycle[0]
           -real[0][0]*(real[1][2]**2+imag[1][2]**2)
           -real[1][1]*(real[0][2]**2+imag[0][2]**2)
           -real[2][2]*(real[0][1]**2+imag[0][1]**2))
    require(det >= 0, "density determinant nonnegative")
    return real, imag


def read_density(response, density):
    rr, ri = validate_density(density)
    real, imag = response
    return sum(rr[i][j]*real[j][i]-ri[i][j]*imag[j][i] for i in range(3) for j in range(3))


def named_densities():
    rays = {
        "basis_minus": [(1, 0), (0, 0), (0, 0)],
        "basis_zero": [(0, 0), (1, 0), (0, 0)],
        "basis_plus": [(0, 0), (0, 0), (1, 0)],
        "coherent_plus": [(0, 0), (1, 0), (1, 0)],
        "coherent_minus": [(0, 0), (1, 0), (-1, 0)],
        "phase_plus": [(0, 0), (1, 0), (0, 1)],
        "phase_minus": [(0, 0), (1, 0), (0, -1)],
        "three_way_phase": [(1, 0), (1, 0), (0, 1)],
    }
    result = {name: pure_density(ray) for name, ray in rays.items()}
    result["incoherent_equal"] = ([[F(0), F(0), F(0)], [F(0), F(1, 2), F(0)], [F(0), F(0), F(1, 2)]], [[F(0)]*3 for _ in range(3)])
    return result


def upper_string(value, digits=40):
    scale = 10**digits
    return str(F((value*scale).__ceil__(), scale))


def interval(value, error, digits=14):
    scale = 10**digits
    lo, hi = ((value-error)*scale).__floor__(), ((value+error)*scale).__ceil__()
    decimal = lambda n: ("-" if n < 0 else "")+f"{abs(n)//scale}.{abs(n)%scale:0{digits}d}"
    return {"lower": str(F(lo, scale)), "upper": str(F(hi, scale)),
            "decimal_lower": decimal(lo), "decimal_upper": decimal(hi), "width": str(F(hi-lo, scale))}


def model_payload(c):
    return {"format": "TFPT_COHERENT_FAMILY_V1", "dimension": len(c["A"]),
            "input_fluxes": list(SEEDS), "input_count": 3, "time_domain": ["0", "1"],
            "cutoff": c["cutoff"], "initial_max_absolute_flux": 1,
            "hamiltonian_denominator": str(SCALE), "source_denominator": str(2*SCALE**2),
            "hamiltonian_rows": [{str(j): str(a) for j, a in row.items()} for row in c["A"]],
            "source_numerators": {name: [[str(a) for a in row] for row in O] for name, O in c["sources"].items()},
            "uniform_family_vector_defect_upper_on_0_to_1": upper_string(c["delta"]),
            "embedding_norm_upper": upper_string(1+c["gram_error"]),
            "bounded_interaction_norm_upper": "97/192", "parent_provenance": PINS,
            "physical_gates_closed": [],
            "scope": "One common auxiliary model for all pure and mixed states on bare-filled flux span{-1,0,1}; not all low-energy states, spatial locality, uniform volume or a TOE."}


def solve_compiled(model, time=F(1), degree=80):
    require(model["format"] == "TFPT_COHERENT_FAMILY_V1", "supported family artifact")
    require(model["input_fluxes"] == list(SEEDS) and model["input_count"] == 3, "unchanged preparation family")
    require(model["time_domain"] == ["0", "1"] and model["initial_max_absolute_flux"] == 1, "compiled time/support contract")
    require(int(model["hamiltonian_denominator"]) == SCALE and int(model["source_denominator"]) == 2*SCALE**2, "compiled arithmetic grid")
    A = [{int(j): int(a) for j, a in row.items()} for row in model["hamiltonian_rows"]]
    require(len(A) == model["dimension"] and len(A) >= 3, "compiled dimension")
    require(all(0 <= j < len(A) for row in A for j in row), "compiled indices")
    sources = {name: [[int(a) for a in row] for row in model["source_numerators"][name]] for name in NAMES}
    require(all(len(O) == len(A) and all(len(row) == len(A) for row in O) for O in sources.values()), "compiled source dimensions")
    require(all(O[i][j] == O[j][i] for O in sources.values() for i in range(len(A)) for j in range(len(A))), "Hermitian compiled sources")
    states, den, taylor = input_evolution(A, 3, time, degree)
    delta = F(model["uniform_family_vector_defect_upper_on_0_to_1"])
    embedding = F(model["embedding_norm_upper"])
    require(delta >= 0 and embedding >= 1, "valid nonnegative family budgets")
    d = delta+embedding*taylor
    q = model["cutoff"]-model["initial_max_absolute_flux"]
    require(isinstance(q, int) and q >= 0, "cutoff margin")
    x = F(model["bounded_interaction_norm_upper"])*F(time)
    require(0 <= x < q+2, "rotor tail domain")
    rotor = x**(q+1)/factorial(q+1)/(1-x/F(q+2))
    error = 4*rotor+d*(2+d)
    return response_matrices(sources, states, den), error


def response_record(response, error):
    return {name: {part: [[interval(x, error) for x in row] for row in matrix]
                   for part, matrix in zip(("real", "imag"), matrices)} for name, matrices in response.items()}


def readout_record(response, error, density):
    return {name: interval(read_density(matrix, density), error) for name, matrix in response.items()}


def certificate(root, layers=20):
    inherited(root)  # Also on cache hits.
    c = build(str(root), layers)
    model = model_payload(c)
    response, error = solve_compiled(model)
    require(response == c["response"], "standalone response matrices match construction exactly")
    cases = {name: readout_record(response, error, rho) for name, rho in named_densities().items()}
    old = json.loads((root/"experiments/theory-contracts/auxiliary-dynamics-round35/validation.json").read_text())
    ref = next(row for row in old["certificates"] if row["dimension"] == 20)["readouts_at_time_one"]
    matches = cases["basis_zero"] == ref
    if layers == 20:
        require(matches, "common family model retains all old zero-flux intervals")
        require(c["delta"] < F(1051, 10**21), "uniform family vector defect below 1.051e-18")
        require(error < F(9309, 10**17), "uniform full-rotor readout error below 9.309e-14")
    coherent = cases["coherent_plus"]["Wilson_cycle_real"]
    mixed = cases["incoherent_equal"]["Wilson_cycle_real"]
    require(F(coherent["lower"])-F(mixed["upper"]) > F(4999, 10000), "coherence not replaced by classical mixing")
    text = json.dumps(model, indent=2, sort_keys=True)+"\n"
    return {"layers": layers, "dimension": len(c["A"]), "full_cutoff_dimension": len(c["basis"]),
            "input_family_dimension": 3, "initial_flux_support": list(SEEDS),
            "uniform_over_all_pure_and_mixed_family_states": True,
            "single_shared_generator_not_independent_seed_fits": True,
            "gram_norm_error_upper": upper_string(c["gram_error"]),
            "uniform_family_vector_defect_upper": upper_string(c["delta"]),
            "per_seed_residual_response_upper": [upper_string(a) for a in c["column_bounds"]],
            "full_rotor_uniform_readout_error_upper": upper_string(error, 22),
            "positive_path_radius_upper": upper_string(c["path_radius"]),
            "cutoff_margin": c["cutoff"]-1,
            "zero_flux_intervals_identical_to_Round35": matches,
            "response_matrices_at_time_one": response_record(response, error),
            "example_density_readouts": cases,
            "online_hamiltonian_nonzeros": sum(len(row) for row in c["A"]),
            "online_source_integer_slots": 4*len(c["A"])**2,
            "offline_basis_integer_slots": len(c["basis"])*len(c["A"]),
            "compiled_model_bytes": len(text.encode()), "compiled_model_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "proposal_arithmetic": "80-digit Decimal proposal; accepted Gram, residual, source and tail bounds are exact rational checks",
            "scope": "Fixed cycle, bounded flux preparation family; not spectral low-energy elimination or uniform spatial lattice physics."}


def run(root):
    return {"status": "PASS", "verdict": "COMMON_HERMITIAN_DYNAMICS_WITH_UNIFORM_COHERENT_FAMILY_CERTIFICATE",
            "certificates": [certificate(root, layers) for layers in (12, 16, 20)],
            "inherited_pins": PINS, "physical_gates_closed": [],
            "uniform_3D_or_spectral_low_energy_theory_proved": False}


def payload(root):
    result = run(root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("checker.py", "COHERENT_FAMILY.md", "README.md", "test_checker.py")}
    return json.dumps(result, indent=2, sort_keys=True)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write-model", type=Path)
    parser.add_argument("--model", type=Path)
    parser.add_argument("--time", type=F, default=F(1))
    parser.add_argument("--state", choices=list(named_densities()), default="coherent_plus")
    parser.add_argument("--density", type=Path, help="JSON with real and imag 3x3 rational-string matrices")
    args = parser.parse_args()
    if args.model:
        require(args.write_model is None, "standalone run must not recompile")
        response, error = solve_compiled(json.loads(args.model.read_text()), args.time)
        density = named_densities()[args.state]
        if args.density:
            data = json.loads(args.density.read_text())
            density = data["real"], data["imag"]
        result = json.dumps({"time": str(args.time), "readouts": readout_record(response, error, density),
                             "uniform_family_error_upper": upper_string(error, 22),
                             "parent_or_full_state_reconstruction_used": False}, indent=2, sort_keys=True)+"\n"
    else:
        result = payload(args.repo)
        if args.write_model:
            args.write_model.write_text(json.dumps(model_payload(build(str(args.repo))), indent=2, sort_keys=True)+"\n")
    if args.output:
        args.output.write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
