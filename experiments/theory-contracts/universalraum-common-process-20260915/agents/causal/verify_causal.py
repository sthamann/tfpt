"""Unconditional interventions on the original TFPT N=2 Fock sector.

The local pulse and reference preparations are explicit granted operations;
their availability in the source compiler is not inferred. No extra term is
added to H. Normal and -OO runs use explicit guards and deterministic output.
"""
from argparse import ArgumentParser
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import math

import numpy as np
import sympy as s
from scipy.sparse import bmat, csr_matrix, eye
from scipy.sparse.linalg import expm_multiply


HERE = Path(__file__).resolve().parent
PIN = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"
CHECKS = []


def need(value, label, kind="exact"):
    if not value:
        raise RuntimeError(label)
    CHECKS.append({"kind": kind, "name": label})


def zero(matrix):
    return all(s.simplify(v) == 0 for v in matrix)


def fermion_remove(mask, mode):
    if not (mask >> mode) & 1:
        return None
    sign = (-1) ** ((mask & ((1 << mode) - 1)).bit_count())
    return mask ^ (1 << mode), sign


def main():
    source = HERE / "sources" / "spinor_tensors.npz"
    need(sha256(source.read_bytes()).hexdigest() == PIN, "frozen native W SHA-256")
    with np.load(source, allow_pickle=False) as archive:
        raw = archive["W"]
    need(np.count_nonzero(raw.imag) == 0, "W has no imaginary coefficients")
    need(np.array_equal(raw.real, np.rint(raw.real)), "W integer conversion is lossless")
    W = raw.real.astype(np.int64)
    pairs = list(combinations(range(64), 2))
    pair_index = {pair: k for k, pair in enumerate(pairs)}
    need(W.shape == (60, 2016), "native 64 fermion and 60 boson dimensions")
    need(set(W.flat) == {-1, 0, 1}, "native nonzero coefficients are signed units")
    need(np.count_nonzero(W) == 480, "480 native pair terms")
    need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)), "WWdag equals 8 I60 exactly")
    need(np.all(np.count_nonzero(W, axis=0) <= 1), "every active pair belongs to exactly one star")
    need(np.count_nonzero(np.count_nonzero(W, axis=0) == 0) == 1536, "1536 isolated occupation-pair states")
    need(60 * 9 + 1536 == 2076, "star decomposition exhausts the full N2 sector")
    for A in range(60):
        support = np.flatnonzero(W[A])
        need(len(support) == 8, "eight leaves in star " + str(A))
        modes = [i for col in support for i in pairs[int(col)]]
        need(len(set(modes)) == 16, "disjoint mode pairs in star " + str(A))
    for col in np.flatnonzero(np.any(W, axis=0)):
        i, j = pairs[int(col)]
        after_i, sign_i = fermion_remove((1 << i) | (1 << j), i)
        after_j, sign_j = fermion_remove(after_i, j)
        need(after_j == 0 and sign_i * sign_j == 1, "CAR sign f_j f_i on pair " + str((i, j)))

    A = 0
    columns = list(map(int, np.flatnonzero(W[A])))
    leaves = [pairs[col] for col in columns]
    signs = s.Matrix([int(W[A, col]) for col in columns])
    need(leaves[0] == (4, 57) and leaves[1] == (5, 56), "source-selected sender and receiver pairs")
    sender = 4
    receiver = 5
    p = s.eye(9)[:, 0]
    boson = s.eye(9)[:, 8]
    projector = signs * signs.T / 8
    active = s.diag(projector, s.ones(1))
    Delta, g = s.symbols("Delta g", real=True)
    H = s.zeros(9)
    H[:8, 8] = g * signs
    H[8, :8] = g * signs.T
    H[8, 8] = Delta
    Z = s.diag(-1, *([1] * 8))
    nj = s.diag(0, 1, *([0] * 7))
    Nb = s.diag(*([0] * 8), 1)
    Nf = s.diag(*([2] * 8), 0)
    need(H == H.T, "exact star Hamiltonian is Hermitian")
    need(zero(projector * projector - projector), "rank-one bright projector is idempotent")
    need(s.trace(projector) == 1, "bright projector has rank one")
    need(zero(H * H - Delta * H - 8 * g * g * active), "exact quadratic identity for native bright block")
    shifted = H - Delta * active / 2
    need(zero(shifted * shifted - (Delta * Delta / 4 + 8 * g * g) * active), "shifted bright Hamiltonian squares to Omega squared")
    need(zero(active * H - H), "bright plus boson subspace is invariant")
    need(Nf + 2 * Nb == 2 * s.eye(9), "total charge is two throughout invariant star")
    need(Z.T * Z == s.eye(9), "one-Kraus local phase instrument is completely positive and trace preserving")
    need(zero(Z * Nf - Nf * Z) and zero(Z * Nb - Nb * Z), "phase pulse preserves fermion and boson numbers")
    need(zero(Z * nj - nj * Z), "sender phase commutes with distinct receiver occupation")
    need(zero(Z.T * nj * Z - nj), "receiver probability cannot change at pulse time for any state")
    need(not zero(Z * H - H * Z), "local phase is not a symmetry of the native H")
    need(Z * p == -p, "phase before product-pair evolution has no physical effect")

    # T=pi/Omega, Omega^2=Delta^2/4+8g^2. On the bright block
    # U(T)=z I2 with z=-exp(-i pi d), d=Delta/(2 Omega).
    # Dark pair directions have energy zero and evolve identically.
    z = s.symbols("z", nonzero=True)
    UT = s.eye(9) + (z - 1) * active
    UTdag = (s.eye(9) + (1 / z - 1) * active).T
    need(zero(UTdag * UT - s.eye(9)), "full-revival propagator is unitary for |z|=1")
    need(zero(Nb * UT * p), "first native full period ends with zero bosons")
    untouched = UT * UT * p
    pulsed = UT * Z * UT * p
    need(zero(Nb * untouched) and zero(Nb * pulsed), "both final arms have zero bosons exactly")
    need(zero(Nf * untouched - 2 * untouched) and zero(Nf * pulsed - 2 * pulsed), "both final arms contain exactly two fermions")
    for q in range(1, 8):
        expected_base = signs[0] * signs[q] * (z * z - 1) / 8
        expected_pulse = signs[0] * signs[q] * 3 * (z - 1) ** 2 / 32
        need(s.simplify(untouched[q] - expected_base) == 0, "untouched receiver-pair amplitude " + str(q))
        need(s.simplify(pulsed[q] - expected_pulse) == 0, "pulsed receiver-pair amplitude " + str(q))
    q0 = s.simplify(untouched[1] * untouched[1].subs(z, 1 / z))
    q1 = s.simplify(pulsed[1] * pulsed[1].subs(z, 1 / z))
    x = s.symbols("x", real=True)
    xz = 2 - z - 1 / z
    need(s.simplify(q0 - (x * (4 - x) / 64).subs(x, xz)) == 0, "untouched probability x(4-x)/64")
    need(s.simplify(q1 - (9 * x * x / 1024).subs(x, xz)) == 0, "pulsed probability 9x^2/1024")
    delta_formula = x * (25 * x - 64) / 1024
    need(s.simplify(q1 - q0 - delta_formula.subs(x, xz)) == 0, "unconditional causal response x(25x-64)/1024")
    need(25 * 2 - 64 < 0, "strict negative response on 0<x<=2")
    need(s.Rational(1, 400) <= s.Rational(3, 32), "g/Delta=1/20 lies in proven negative-response interval")
    need(s.simplify((s.Rational(5, 3) / s.sqrt(3)) ** 2 - s.Rational(25, 27)) == 0, "test-point d=5/(3sqrt3)")
    need(s.Rational(25, 27) > s.Rational(1, 4) and s.Rational(25, 27) < 1, "test-point d strictly between one half and one")

    # An independent boson-seed intervention has a positive receiver signal
    # for every g!=0, without requiring the restricted coupling interval.
    a, b, c = s.symbols("a b c")
    Uhalf = s.eye(9)
    Uhalf[:8, :8] += (a - 1) * projector
    Uhalf[:8, 8] = b * signs / s.sqrt(8)
    Uhalf[8, :8] = b * signs.T / s.sqrt(8)
    Uhalf[8, 8] = c
    mid = Uhalf * boson
    difference = Uhalf * Z * mid - Uhalf * mid
    need(s.simplify((Uhalf * p)[1] - signs[0] * signs[1] * (a - 1) / 8) == 0,
         "general-time pair-to-pair amplitude from the same exact propagator")
    need(s.simplify(difference[1] + signs[1] * b * (a - 1) / (4 * s.sqrt(8))) == 0, "boson-seed half-period phase response amplitude")
    d = s.symbols("d", positive=True)
    boson_signal = (1 - d * d) * (1 + d * d - 2 * d * s.sin(s.pi * d / 2)) / 128
    lower_bound = (1 - d * d) * (1 - d) ** 2 / 128
    halfphase = s.cos(s.pi * d / 2) - s.I * s.sin(s.pi * d / 2)
    r = s.symbols("r", real=True)
    halfvalues = {a: s.I * d * halfphase, c: -s.I * d * halfphase, b: -s.I * r * halfphase}
    need(s.simplify((Uhalf * Uhalf * boson)[1].subs(halfvalues)) == 0,
         "untouched boson seed has exactly zero receiver amplitude after two half periods")
    boson_response_amp = s.simplify((Uhalf * Z * Uhalf * boson)[1].subs(halfvalues))
    boson_response_probability = s.simplify(s.expand_complex(boson_response_amp * s.conjugate(boson_response_amp)))
    need(s.trigsimp(s.expand(boson_response_probability.subs(r * r, 1 - d * d) - boson_signal), method="fu") == 0,
         "exact boson-seed receiver probability after local phase")
    need(s.simplify(boson_signal - lower_bound - (1 - d*d) * d * (1 - s.sin(s.pi*d/2)) / 64) == 0,
         "positive boson-seed signal lower bound for 0<d<1")

    # Local fill is a second, less conservative intervention: it exchanges
    # one unit of N with an external reservoir. It is not called N preserving.
    annihilate = s.Matrix([[0, 1], [0, 0]])
    ni = annihilate.T * annihilate
    need(ni.T * ni + annihilate * annihilate.T == s.eye(2), "local fill Kraus operators n_i and f_i^dag are trace preserving")
    need(ni * s.diag(1, 0) * ni + annihilate.T * s.diag(1, 0) * annihilate == s.diag(0, 1), "local fill prepares occupied sender from empty sender")
    need(annihilate.T * ni - ni * annihilate.T != s.zeros(2), "fill exchanges charge and is not claimed number preserving")

    # Short-time pair transfer, independently from the full-period echo.
    Hp = H * p
    H2p = H * Hp
    need(Hp[1] == 0 and H2p[1] == g * g * signs[0] * signs[1], "receiver-pair first amplitude arises through native boson at second order")
    need(s.simplify((H2p[1] / 2) ** 2 - g ** 4 / 4) == 0, "receiver occupation leading coefficient g^4 t^4 /4")
    need(Hp[8] == g * signs[0], "boson occupation leading coefficient is g^2 t^2")

    # Independent floating-point replay on ALL 2076 N=2 states, using W
    # directly rather than the symbolic nine-state star or derived U(T).
    Delta_num, g_num = 1.0, 0.05
    omega = math.sqrt(Delta_num ** 2 / 4 + 8 * g_num ** 2)
    dnum = Delta_num / (2 * omega)
    period = math.pi / omega
    wcsr = csr_matrix(W)
    Hfull = bmat([[csr_matrix((2016, 2016)), g_num * wcsr.T],
                  [g_num * wcsr, Delta_num * eye(60)]], format="csr")
    full_start = np.zeros(2076, dtype=complex)
    full_start[columns[0]] = 1
    phase = np.ones(2076)
    phase[[k for k, pair in enumerate(pairs) if sender in pair]] = -1
    readout = np.zeros(2076)
    readout[[k for k, pair in enumerate(pairs) if receiver in pair]] = 1
    need(np.array_equal(phase[columns + [2016 + A]], np.array(Z.diagonal(), dtype=int).ravel()),
         "star pulse is the restriction of globally local (-1)^n4")
    need(np.array_equal(readout[columns + [2016 + A]], np.array(nj.diagonal(), dtype=int).ravel()),
         "star readout is the restriction of globally local n5")
    full_mid = expm_multiply(-1j * period * Hfull, full_start)
    full_base = expm_multiply(-1j * period * Hfull, full_mid)
    full_pulse = expm_multiply(-1j * period * Hfull, phase * full_mid)
    numeric_x = 4 * math.cos(math.pi * dnum / 2) ** 2
    expected0 = numeric_x * (4 - numeric_x) / 64
    expected1 = 9 * numeric_x ** 2 / 1024
    measured0 = float(np.dot(readout, np.abs(full_base) ** 2))
    measured1 = float(np.dot(readout, np.abs(full_pulse) ** 2))
    need(abs(measured0 - expected0) < 1e-13, "full N2 replay matches untouched exact probability", "numeric")
    need(abs(measured1 - expected1) < 1e-13, "full N2 replay matches pulsed exact probability", "numeric")
    need(np.linalg.norm(full_base[2016:]) < 1e-12 and np.linalg.norm(full_pulse[2016:]) < 1e-12,
         "full N2 replay confirms zero final boson amplitude in both arms", "numeric")
    need(abs(np.linalg.norm(full_base) - 1) < 1e-12 and abs(np.linalg.norm(full_pulse) - 1) < 1e-12,
         "full N2 replay preserves both unconditional norms", "numeric")
    need(abs(float(np.dot(readout, np.abs(full_mid)**2)) - float(np.dot(readout, np.abs(phase*full_mid)**2))) < 1e-15,
         "full N2 receiver statistic is unchanged at the local pulse", "numeric")
    pulse_before = expm_multiply(-2j * period * Hfull, phase * full_start)
    need(np.linalg.norm(pulse_before + full_base) < 1e-12, "pulse on initial product pair alone has no observable effect", "numeric")
    znum = -np.exp(-1j * math.pi * dnum)
    star_base = np.array(untouched.subs(z, znum), dtype=complex).ravel()
    star_pulse = np.array(pulsed.subs(z, znum), dtype=complex).ravel()
    embed = columns + [2016 + A]
    expected_full0 = np.zeros(2076, dtype=complex)
    expected_full1 = np.zeros(2076, dtype=complex)
    expected_full0[embed] = star_base
    expected_full1[embed] = star_pulse
    need(np.linalg.norm(full_base - expected_full0) < 1e-12, "full N2 untouched state agrees with exact star state", "numeric")
    need(np.linalg.norm(full_pulse - expected_full1) < 1e-12, "full N2 pulsed state agrees with exact star state", "numeric")
    boson_start = np.zeros(2076, dtype=complex)
    boson_start[2016 + A] = 1
    boson_mid = expm_multiply(-0.5j * period * Hfull, boson_start)
    boson_base = expm_multiply(-0.5j * period * Hfull, boson_mid)
    boson_pulse = expm_multiply(-0.5j * period * Hfull, phase * boson_mid)
    expected_boson_signal = float(boson_signal.subs(d, dnum))
    need(float(np.dot(readout, np.abs(boson_base) ** 2)) < 1e-24,
         "full N2 boson-seed untouched receiver probability vanishes", "numeric")
    need(abs(float(np.dot(readout, np.abs(boson_pulse) ** 2)) - expected_boson_signal) < 1e-13,
         "full N2 boson-seed phase response agrees with exact formula", "numeric")

    result = {
        "status": "PASS",
        "source_sha256": PIN,
        "verifier_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_checks": sum(c["kind"] == "exact" for c in CHECKS),
        "numeric_checks": sum(c["kind"] == "numeric" for c in CHECKS),
        "checks": CHECKS,
        "native_structure": {"N2_dimension": 2076, "invariant_stars": 60,
                             "star_dimension": 9, "isolated_pair_states": 1536,
                             "boson_index": A, "leaves": leaves, "signs": list(map(int, signs))},
        "main_witness": {
            "initial_state": "f_4^dag f_57^dag |vac>; all bosons empty",
            "sender_mode": sender, "receiver_mode": receiver,
            "readout": "n_5", "intervention": "Z_4 rho Z_4; Z_4=(-1)^n_4",
            "timeline": "U(T), optional Z_4, U(T), unconditional n_5 readout",
            "T": "pi/Omega", "Omega_squared": "Delta^2/4+8g^2",
            "d": "Delta/(2Omega)", "x": "4cos^2(pi d/2)",
            "untouched_probability": "x(4-x)/64", "pulsed_probability": "9x^2/1024",
            "causal_difference": "x(25x-64)/1024",
            "strict_negative_interval": "Delta>0 and 0<g^2<=3Delta^2/32",
            "final_Nf_both_arms": 2, "final_Nb_both_arms": 0,
            "postselection": False,
            "test_point": {"Delta": 1, "g": "1/20", "T": format(period, ".14g"),
                           "untouched_probability": format(expected0, ".14g"),
                           "pulsed_probability": format(expected1, ".14g"),
                           "difference": format(expected1 - expected0, ".14g")}},
        "secondary_witnesses": {
            "boson_seed": {"initial_state": "b_0^dag |vac>", "delay": "pi/(2Omega) before and after Z_4",
                           "untouched_n5": "0", "pulsed_n5": "(1-d^2)(1+d^2-2d sin(pi d/2))/128",
                           "positive_for": "Delta>0, g!=0", "same_final_species": False},
            "fill_seed": {"reference": "f_57^dag |vac>", "Kraus": ["n_4", "f_4^dag"],
                          "N_preserving": False, "receiver_response": "|a(t)-1|^2/64",
                          "a(t)": "exp(-i Delta t/2)[cos(Omega t)+i d sin(Omega t)]",
                          "leading_receiver_probability": "g^4 t^4/4",
                          "leading_boson_probability": "g^2 t^2"}},
        "scope": {"same_original_H_and_W": True, "added_hopping_or_link": False,
                  "unconditional_mode_to_mode_intervention_proven": True,
                  "local_CPTP_phase_preserves_N": True,
                  "pair_to_pair_redistribution_proven": True,
                  "native_preparation_availability_proven": False,
                  "native_phase_control_availability_proven": False,
                  "native_number_readout_availability_proven": False,
                  "N64_ground_state_or_charged_pole_used": False,
                  "spatial_metric_or_spacetime_derived": False,
                  "new_ground_state_or_pole_theorem": False}}
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(json.dumps({"status": result["status"], "exact_checks": result["exact_checks"],
                          "numeric_checks": result["numeric_checks"], "result_sha256": sha256(rendered.encode()).hexdigest()}, sort_keys=True))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
