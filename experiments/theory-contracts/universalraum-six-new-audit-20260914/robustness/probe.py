"""Independent F9 closure and noncommuting instrument-error audit.

No imports from the research implementations. Exact integer support certificates,
numerical pulse/process probes, and analytic bounds are classified separately.
Explicit guards survive -OO; --mutant introduces errors that must be detected.
"""
from pathlib import Path
from itertools import product, permutations, combinations
from fractions import Fraction as F
from math import pi, sqrt, atan, floor, acos, atan2, sin
import argparse
import hashlib
import json
import numpy as np
from scipy.linalg import expm, block_diag

HERE = Path(__file__).resolve().parent
CHECKS = []


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def exact_support(mutant):
    words = list(product(range(4), repeat=4))
    lookup = {w: k for k, w in enumerate(words)}
    eye = np.eye(256, dtype=np.int64)
    swaps = []
    for site in (1, 2, 3):
        matrix = np.zeros_like(eye)
        for col, word in enumerate(words):
            changed = list(word)
            changed[0], changed[site] = changed[site], changed[0]
            matrix[lookup[tuple(changed)], col] = 1
        swaps.append(matrix)
    matrix_m = 3 * eye + sum(swaps, np.zeros_like(eye))
    projectors = []
    for sector in range(7):
        numerator, denominator = eye.copy(), 1
        for other in range(7):
            if other != sector:
                numerator = numerator @ (matrix_m - other * eye)
                denominator *= sector - other
        need(np.array_equal(numerator @ numerator, denominator * numerator),
             f"integer spectral projector M={sector}")
        projectors.append((numerator, denominator))
    ranks = [int(np.trace(a) // b) for a, b in projectors]
    need(ranks == [1, 30, 45, 40, 15, 90, 35], "all seven exact ranks")
    ptotal = sum(((720//b)*a for a, b in projectors), np.zeros_like(eye))
    need(np.array_equal(ptotal, 720*eye), "all exact projectors resolve identity")
    chi = np.zeros(256, dtype=np.int64)
    for a, b, x in [(0, 1, 1), (1, 0, -1)]:
        for c, d, y in [(2, 3, 1), (3, 2, -1)]:
            chi[lookup[a, b, c, d]] = x*y
    omega = np.zeros(256, dtype=np.int64)
    for word in permutations(range(4)):
        omega[lookup[word]] = (-1)**sum(word[a] > word[b] for a, b in combinations(range(4), 2))
    clock = np.zeros_like(eye)
    for col, word in enumerate(words):
        clock[lookup[((1, 2, 0, 3)[word[0]],) + word[1:]], col] = 1
    echo = clock.T @ swaps[0] @ clock @ omega

    def weight(vector, sector, normalization=None):
        num, den = projectors[sector]
        norm = int(vector @ vector) if normalization is None else normalization
        return F(int(vector @ num @ vector), int(den * norm))

    source_weights = {}
    for name, vector, norm in [("chi", chi, 4), ("Omega", omega, 24),
                               ("z", echo, 24), ("Bplus_Omega", omega+echo, 96),
                               ("Bminus_Omega", omega-echo, 96)]:
        weights = [weight(vector, sector, norm) for sector in range(7)]
        need(weights[2] == weights[6] == 0, "frozen ideal source excludes M2/M6: "+name)
        source_weights[name] = [str(x) for x in weights]
    sigma = np.zeros(256, dtype=np.int64)
    for a in range(4):
        for word, sign in [((a, a^1, a^2, a^3), 1), ((a, a^1, a^3, a^2), -1),
                           ((a, a^2, a^1, a^3), -1), ((a, a^2, a, a^2), 1)]:
            sigma[lookup[word]] += sign
    sigma_weights = [weight(sigma, sector, 16) for sector in range(7)]
    need(sigma_weights == [F(3, 8), F(0), F(0), F(1, 2), F(0), F(0), F(1, 8)],
         "optimal stabilizer seed occupies omitted M6 with exact weight 1/8")
    source_weights["sigma_optimal_3_over_8_seed"] = [str(x) for x in sigma_weights]
    xi = np.zeros(256, dtype=np.int64)
    for d in range(4):
        for u, v in product((0, 1), repeat=2):
            xi[lookup[d, d^2^u, d^1^(2*v), d^3^u^(2*v)]] += (-1)**(u+v)
    xi_weights = [weight(xi, sector, 16) for sector in range(7)]
    need(xi_weights == sigma_weights, "new six-CNOT xi seed has exactly the same M support and weights")
    source_weights["xi_new_six_CNOT_seed"] = [str(x) for x in xi_weights]
    if mutant == "combine_sigma_F9":
        need(sigma_weights[6] == 0, "MUTANT: optimal seed cannot be combined blindly with F9")
    need(2*sum(ranks[k] for k in (0, 1, 3, 4, 5)) == 352, "restricted microscopic rank 352")
    # This is a member of the claimed support, not one of the frozen ideal seeds.
    allowed = projectors[5][0][:, lookup[0, 0, 0, 1]]
    record_witnesses = []
    for edge, swap in enumerate(swaps, 1):
        leaked = weight(swap @ allowed, 2)
        plus, minus = (eye+swap)@allowed, (eye-swap)@allowed
        normalization = int(4*(allowed@allowed))
        raw_plus, raw_minus = weight(plus, 2, normalization), weight(minus, 2, normalization)
        need(leaked == (F(8, 9) if edge == 3 else F(2, 9)), f"exact record support leak on edge 0{edge}")
        need(raw_plus + raw_minus == leaked/2, "ungelesener Record leakage identity")
        record_witnesses.append({"edge": f"0{edge}", "swap_M2_weight": str(leaked),
                                 "record_plus_raw_M2_weight": str(raw_plus),
                                 "record_minus_raw_M2_weight": str(raw_minus)})
    if mutant == "pretend_invariant":
        need(weight(swaps[2] @ allowed, 2) == 0, "MUTANT: false record-invariance claim detected")
    # A physical three-carrier diagonal Pauli, with each ququart regarded as two bits.
    signs = np.array([(-1)**((w[0]&1)+((w[1]>>1)&1)+(w[2]&1)) for w in words])
    vomega = signs * omega
    need(int(omega@vomega) == 0, "Pauli error state orthogonal to Omega")
    need(weight(vomega, 2) == F(4, 9), "three-local Pauli injects exact 4/9 into missing M2")
    need(np.count_nonzero(matrix_m*signs[None, :] - signs[:, None]*matrix_m) > 0,
         "Pauli error does not commute with the star spectral generator")
    for numerator, denominator in projectors:
        need(np.max(abs(numerator)) < 10**8, "integer projector arithmetic stays below overflow envelope")
    output = {"ranks": ranks, "frozen_source_weights": source_weights,
              "record_counterexample_source": "P5 |0,0,0,1> normalized",
              "record_counterexamples": record_witnesses,
              "pauli_error": "Z_bit0(site0) Z_bit1(site1) Z_bit0(site2)",
              "Pauli_error_M2_weight": "4/9", "support_invariant_under_general_records": False}
    return output, projectors, omega/sqrt(24), signs, swaps


def filter_probe(projectors, omega, signs):
    low = (1-np.sqrt(1+.01*(6-np.arange(7))))/2
    high = 1-low
    chosen = [low[k] for k in (0, 1, 3, 4, 5)] + [high[k] for k in (0, 1, 3, 4, 5)]
    times = np.array([pi/(energy-low[0]) for energy in chosen if energy != low[0]])
    full_levels = list(low) + list(high[:6]) + [1.]
    full_times = np.array([pi/(energy-low[0]) for energy in full_levels if energy != low[0]])

    def kernel(energy, schedule):
        return np.prod((1+np.exp(-1j*schedule*(energy-low[0])))/2)

    amplitudes = []
    full_amplitudes = []
    for sector in range(7):
        w = (1+1/np.sqrt(1+.01*(6-sector)))/2
        amplitudes.append(w*kernel(low[sector], times)+(1-w)*kernel(high[sector], times))
        full_amplitudes.append(w*kernel(low[sector], full_times)+(1-w)*kernel(high[sector], full_times))
    need(abs(amplitudes[2])**2 > .08, "F9 leaks at least eight percent raw weight on omitted M2", "numerical")
    need(max(abs(full_amplitudes[k]) for k in range(1, 7)) < 1e-12,
         "F13 kills every unwanted bare sector", "numerical")
    matrix = sum((amplitude*num/den for amplitude, (num, den) in zip(amplitudes, projectors)),
                 np.zeros((256, 256), complex))
    extra_zero_time = pi/(-low[0])
    ten_times = np.r_[times, extra_zero_time]
    need(abs(kernel(0., ten_times)) < 1e-12, "one extra factor removes the optimal seed M6 component", "numerical")
    seed_good = 3*abs(amplitudes[0])**2/8
    seed_bad = abs(amplitudes[6])**2/8
    seed_result = {"F9_raw_good": float(seed_good), "F9_raw_bad": float(seed_bad),
                   "F9_raw_accept": float(seed_good+seed_bad),
                   "F9_conditional_infidelity": float(seed_bad/(seed_good+seed_bad)),
                   "F10_one_filter_time": float(sum(ten_times)),
                   "F10_raw_success_restored": float(seed_good),
                   "F10_extra_factor": "(I+exp[-i*pi*(H-E0)/(-E0)])/2 kills E=0"}
    four_times = np.array([pi/(e-low[0]) for e in (low[3], high[0], high[3], low[6])])
    need(all(abs(kernel(e, four_times)) < 1e-12 for e in (low[3], high[0], high[3], low[6])),
         "four-factor filter deletes all unwanted occupied energies of sigma", "numerical")
    seed_result.update(F4_sigma_only_preparation_time=float(sum(four_times)),
                       different_F4_start_F9_end_total_time=float(sum(four_times)+sum(times)),
                       common_F10_start_end_total_time=float(2*sum(ten_times)),
                       F4_scope="only the ideal sigma preparation source; not the common echo endpoint or arbitrary inputs")
    rows = []
    for angle in (1e-4, .001, .01, .1):
        state = np.exp(-1j*angle*signs)*omega
        accepted = matrix@state
        raw = float(np.vdot(accepted, accepted).real)
        good = float(abs(np.vdot(omega, accepted))**2)
        bad = float(np.vdot(accepted-omega*np.vdot(omega, accepted),
                            accepted-omega*np.vdot(omega, accepted)).real)
        expected_bad = abs(amplitudes[2])**2 * 4*sin(angle)**2/9
        need(abs(bad-expected_bad) < 1e-13, "omitted-sector raw leakage formula", "numerical")
        rows.append({"angle": angle, "raw_accept": raw, "raw_good": good,
                     "raw_bad": bad, "raw_reject": 1-raw, "conditional_infidelity": bad/raw})
    return {"one_filter_time": float(sum(times)),
            "optimal_seed_composition": seed_result,
            "F11_time_with_both_M2_partners": float(sum(times)+pi/(low[2]-low[0])+pi/(high[2]-low[0])),
            "F13_full_space_time": float(sum(full_times)),
            "sector_raw_transmission_F9": [float(abs(x)**2) for x in amplitudes],
            "noise_before_F9": rows}


def macro_probe(mutant):
    # Independently reconstruct the documented fixed-Delta schedule and finite Q gates.
    g = sqrt(2)/20
    frequency = sqrt(1+4*g*g)
    theta = atan(2*g)
    count = floor(pi/(2*theta))-1
    beta = count*theta
    axis = np.array([sin(theta), 0., -np.cos(theta)])
    vector = np.array([sin(2*beta), 0., np.cos(2*beta)])
    reflected = np.array([-1., -1., 1.])
    mirror = reflected*axis
    u, v, d = axis@vector, mirror@vector, mirror@axis
    first = acos((np.cos(theta)-d*u)/(v-d*u))
    moved = vector*np.cos(first) + np.cross(axis, vector)*sin(first) + axis*u*(1-np.cos(first))
    moved = reflected*moved
    south = np.array([0., 0., -1.])
    last = atan2(axis@np.cross(moved, south), moved@south-np.cos(theta)**2) % (2*pi)
    times = [pi/frequency]*count+[first/frequency, last/frequency]
    gamma = len(times)*pi*(1-1/frequency)
    wedge = np.zeros((6, 16))
    for row, (a, b) in enumerate(combinations(range(4), 2)):
        wedge[row, 4*a+b] = 1/sqrt(2)
        wedge[row, 4*b+a] = -1/sqrt(2)
    pm = wedge.T@wedge
    h22 = np.block([[np.zeros((16, 16)), g*wedge.T], [g*wedge, np.eye(6)]])
    occ22 = block_diag(np.zeros((16, 16)), np.eye(6))
    identity = np.eye(88)
    drift = np.kron(occ22, np.eye(4))
    x = np.array([[0., 1.], [1., 0.]])
    qmain = block_diag(np.eye(64), np.kron(np.eye(6), np.kron(x, np.eye(2))))
    qhelper = block_diag(np.eye(64), np.kron(np.eye(6), np.kron(np.eye(2), x)))
    generators = {"on": np.kron(h22, np.eye(4)), "off": drift,
                  "main": drift+pi*(identity-qmain)/2,
                  "helper": drift+pi*(identity-qhelper)/2}
    forward = []
    for index, time in enumerate(times):
        forward.append(("on", time))
        if index < len(times)-1:
            forward.append(("helper", 0.))
    reverse = [(kind, 2*pi/frequency-time) if kind == "on" else (kind, time)
               for kind, time in reversed(forward)]
    stages = [("off", gamma)] + forward + [("main", 0.), ("off", gamma)] + reverse
    if mutant == "omit_phase_repair":
        # Same duration and segment resources, wrong placement of the phase repairs.
        stages = [("off", 2*gamma)] + forward + [("main", 0.)] + reverse
    segments = []
    for kind, duration in stages:
        if kind in ("main", "helper"):
            segments += [(kind, 1.), ("off", 2*pi-1)]
        else:
            segments.append((kind, duration))
    duration = sum(time for _, time in segments)
    need(abs(duration-70*pi) < 1e-11, "finite Q-window duration equals 70 pi", "numerical")
    rec = np.kron(np.eye(16)-pm, np.eye(2))+np.kron(pm, x)
    target = block_diag(rec, np.eye(12))
    helper = np.array([1., -1.])/sqrt(2)
    embedding = np.kron(np.eye(44), helper[:, None])
    # Norm-one leakage perturbation coupling a symmetric dark state to a mediator.
    perturb22 = np.zeros((22, 22))
    perturb22[0, 16] = perturb22[16, 0] = 1.
    perturbation = np.kron(perturb22, np.eye(4))
    need(np.linalg.norm(perturbation@generators["on"]-generators["on"]@perturbation) > 1,
         "macro perturbation is noncommuting and couples a dark sector", "numerical")
    rows = []
    for strength in (0., 1e-5, 1e-4):
        current = np.eye(88, dtype=complex)
        cache = {}
        for kind, time in segments:
            key = (kind, time)
            if key not in cache:
                cache[key] = expm(-1j*time*(generators[kind]+strength*perturbation))
            current = cache[key]@current
        error = float(np.linalg.norm(current@embedding-embedding@target, 2))
        if strength == 0:
            need(error < 1e-11, "independent full 88D finite-Q record reconstruction", "numerical")
        bound = duration*strength
        need(error <= bound+2e-12, "noncommuting full-macro Duhamel bound", "numerical")
        rows.append({"deltaH_over_Delta": strength, "isometry_error": error,
                     "analytic_bound": bound})
    return {"duration_hbar_over_Delta": duration, "finite_segments": len(segments),
            "noise_generator": "|00_matter><mediator01| + adjoint; norm 1; tensored with both pointers",
            "numerical_validation": rows,
            "bound_scope": "arbitrary bounded time-dependent perturbations, including leakage, by analytic Duhamel; samples do not prove norm bound"}


def raw_process_probe(omega, signs, swaps, mutant):
    seed = np.zeros(256)
    seed[27] = 1.
    permutations_ = [np.argmax(s, axis=0) for s in swaps]

    def exact_ideal(rounds):
        vector = {27: F(1)}
        intermediate = [F(1)]
        for step in range(3*rounds):
            perm = permutations_[step % 3]
            output = {}
            for index, amplitude in vector.items():
                swapped = int(perm[index])
                output[index] = output.get(index, F(0))+amplitude/2
                output[swapped] = output.get(swapped, F(0))-amplitude/2
            vector = {i: value for i, value in output.items() if value}
            intermediate.append(sum((v*v for v in vector.values()), F(0)))
        raw = intermediate[-1]
        overlap_numerator = sum((round(float(omega[i]*sqrt(24)))*v for i, v in vector.items()), F(0))
        good = overlap_numerator**2/24
        bad = raw-good
        need(good == F(1, 24) and bad > 0, f"exact finite-round raw good/bad mass n={rounds}")
        return {"raw_accept": float(raw), "raw_good": float(good), "raw_bad": float(bad),
                "raw_reject": float(1-raw), "conditional_infidelity": float(bad/raw),
                "expected_records_until_success": float(sum(intermediate[:-1])/raw),
                "exact_raw_accept": str(raw), "exact_raw_bad": str(bad),
                "exact_conditional_infidelity": str(bad/raw)}

    def run(rounds, angle, flip):
        rho = np.outer(seed, seed).astype(complex)
        phase = np.exp(-1j*angle*signs)
        failed, stage_weights = 0., []
        for step in range(3*rounds):
            before = float(np.trace(rho).real)
            rho = phase[:, None]*rho*phase.conj()[None, :]
            p = permutations_[step % 3]
            both = rho[p, :][:, p]
            cross = rho[p, :]+rho[:, p]
            minus = (rho+both-cross)/4
            plus = (rho+both+cross)/4
            rho = (1-flip)*minus+flip*plus
            after = float(np.trace(rho).real)
            failed += before-after
            stage_weights.append(after)
        raw = float(np.trace(rho).real)
        good = float((omega@rho@omega).real)
        bad = max(0., raw-good)
        need(abs(raw+failed-1) < 1e-12, "all rejected and accepted raw weights sum to one", "numerical")
        return {"raw_accept": raw, "raw_good": good, "raw_bad": bad,
                "raw_reject": failed, "conditional_infidelity": bad/raw,
                "expected_records_until_success": (1+sum(stage_weights[:-1]))/raw}

    rows = []
    for rounds in (8, 20):
        ideal = exact_ideal(rounds)
        numerical_ideal = run(rounds, 0., 0.)
        need(abs(ideal["raw_accept"]-numerical_ideal["raw_accept"]) < 1e-12,
             "numerical process agrees with exact ideal raw weight", "numerical")
        p0, b0 = ideal["raw_accept"], ideal["raw_bad"]
        for angle, flip in [(0., 0.), (1e-5, 1e-7), (.001, 1e-5), (.01, 1e-4)]:
            actual = ideal if angle == flip == 0 else run(rounds, angle, flip)
            eta = 3*rounds*2*sin(abs(angle)/2)
            q = min(1., 3*rounds*flip)
            lower = max(0., max(0., sqrt(p0)-eta)**2-q)
            bad_upper = min(1., (sqrt(max(b0, 0.))+eta)**2+q)
            infidelity_bound = min(1., bad_upper/lower) if lower > 0 else 1.
            raw_deviation_bound = min(1., 2*sqrt(p0)*eta+eta*eta+q)
            need(actual["raw_accept"] >= lower-2e-12, "coherent plus readout-noise raw lower bound", "numerical")
            need(actual["conditional_infidelity"] <= infidelity_bound+2e-12,
                 "coherent plus readout-noise conditioned fidelity bound", "numerical")
            need(abs(actual["raw_accept"]-p0) <= raw_deviation_bound+2e-12,
                 "unconditional success deviation bound", "numerical")
            rows.append({"rounds": rounds, "angle_per_record": angle,
                         "symmetric_measurement_flip_probability": flip,
                         "ideal": ideal, "actual": actual,
                         "total_coherent_error_bound": eta, "total_stochastic_distance_bound": q,
                         "raw_success_lower_bound": lower,
                         "conditional_infidelity_upper_bound": infidelity_bound})
    # A false positive can be rare absolutely and still contaminate a rarer accepted branch.
    p, false_positive = F(1, 24), F(1, 1000)
    posterior_bad = false_positive*(1-p)/(p+false_positive*(1-p))
    need(posterior_bad == F(23, 1023), "exact postselection amplification of measurement false positives")
    if mutant == "ignore_conditioning":
        need(posterior_bad <= false_positive, "MUTANT: raw error mistaken for conditioned error")
    return {"process": "basis |0123>, repeated 01/02/03 records, accept all reported minus; early abort",
            "unitary_fault_per_record": "exp(-i alpha V) before record, same noncommuting three-local V",
            "readout_fault": "(1-f)Pminus rho Pminus + f Pplus rho Pplus; all rejects counted",
            "rows": rows, "false_positive_exact_conditional_bad_example": str(posterior_bad)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="verification.json")
    parser.add_argument("--mutant", choices=["pretend_invariant", "omit_phase_repair", "ignore_conditioning", "combine_sigma_F9"])
    args = parser.parse_args()
    support, projectors, omega, signs, swaps = exact_support(args.mutant)
    result = {"scope": "conditional finite robustness theorem and independent probes; no native-source or TOE promotion",
              "support": support,
              "filter": filter_probe(projectors, omega, signs),
              "macro": macro_probe(args.mutant),
              "raw_process": raw_process_probe(omega, signs, swaps, args.mutant)}
    source_paths = [Path("/Users/stefanhamann/Documents")/name for name in
                    ("BEWEISE.md", "neu_1.md", "antwort_gemini.md", "TFPT_Universalraum_Forschungsfortsetzung_2026-09-14.md")]
    result["source_sha256"] = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in source_paths}
    result["checks"] = CHECKS
    result["check_count"] = len(CHECKS)
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    target = HERE/args.out
    target.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"checks": len(CHECKS), "output": str(target), "status": "passed"}))


if __name__ == "__main__":
    main()
