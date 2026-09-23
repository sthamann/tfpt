"""Primitive operations ledger for the TFPT/Universalraum v1.4 microscopic protocol.

Answers follow-up question Q1 ("Wer bedient das Labor?"): which control
operations used by the microscopic protocol are derived from native compiler
primitives, which remain additional resources, and at what exact cost.

Standalone Python 3, only numpy/scipy/sympy. No imports from research checkers.
Theory contract = internal consistency only. No promotion claims.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from math import ceil, log, pi
import hashlib
import json
import argparse
import numpy as np
from scipy.linalg import eigh

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}


def need(ok, name, kind="exact"):
    """Record a check; raise on failure (survives python3 -OO)."""
    if not bool(ok):
        raise RuntimeError("CHECK FAILED: " + name)
    CHECKS.append(dict(name=name, kind=kind))


def swap_matrix(n, i, j):
    """Permutation matrix swapping carriers i and j in an n-carrier space."""
    dim = 4 ** n
    S = np.zeros((dim, dim))
    powers = 4 ** np.arange(n - 1, -1, -1)
    for k, w in enumerate(product(range(4), repeat=n)):
        v = list(w)
        v[i], v[j] = v[j], v[i]
        S[int(np.dot(v, powers)), k] = 1
    return S


def build_star(t=0.05, Delta=1.0):
    """Build the 544-dim microscopic star Hamiltonian and the 288x256 coupling M."""
    basis = list(product(range(4), repeat=4))
    med_index = {}
    M = np.zeros((288, 256))
    for col, m in enumerate(basis):
        for j in [1, 2, 3]:
            a, b = m[0], m[j]
            if a == b:
                continue
            mm = list(m)
            mm[0] = mm[j] = -1
            key = (j, tuple(mm), min(a, b), max(a, b))
            row = med_index.setdefault(key, len(med_index))
            M[row, col] = 1 if a < b else -1

    G = np.zeros((256, 256))
    for j in [1, 2, 3]:
        S = swap_matrix(4, 0, j)
        G += (np.eye(256) + S) / 2

    Hmic = np.block([
        [np.zeros((256, 256)), t * M.T],
        [t * M, Delta * np.eye(288)],
    ])

    gvals = np.arange(0, 3.5, 0.5)
    mult = np.array([1, 30, 45, 40, 15, 90, 35])
    low = (Delta - np.sqrt(Delta ** 2 + 4 * t * t * (6 - 2 * gvals))) / 2
    upper = Delta - low[:-1]
    energies = np.concatenate([low, upper, [Delta]])
    deg = np.concatenate([mult, mult[:-1], [67]])

    microvals, microvec = eigh(Hmic)
    targetE = energies[0]
    tau = pi / (energies[1:] - targetE)

    om = np.zeros(256)
    for p in permutations(range(4)):
        inv = sum(p[i] > p[j] for i, j in combinations(range(4), 2))
        om[sum(p[i] * 4 ** (3 - i) for i in range(4))] = (-1) ** inv / np.sqrt(24)
    A = np.outer(om, om)
    w = (1 + 1 / np.sqrt(1 + 24 * t * t)) / 2

    return dict(t=t, Delta=Delta, H=Hmic, M=M, G=G, basis=basis,
                med_index=med_index, energies=energies, deg=deg,
                microvals=microvals, microvec=microvec, targetE=targetE,
                tau=tau, w=w, om=om, A=A)


def dressed_projector(star):
    """Rebuild the 544-dim dressed ground projector via the 13-factor filter."""
    microvals = star["microvals"]
    microvec = star["microvec"]
    targetE = star["targetE"]
    tau = star["tau"]
    f_full = np.ones(544, complex)
    for time in tau:
        f_full *= 0.5 * (1 + np.exp(-1j * time * (microvals - targetE)))
    return (microvec * f_full) @ microvec.conj().T


def op1_tick():
    C4 = np.eye(4)[:, [1, 2, 0, 3]]
    tick = np.kron(C4, np.eye(64))
    need(np.linalg.norm(np.linalg.matrix_power(C4, 3) - np.eye(4)) < 1e-14,
         "op1 tick C is a 3-cycle (C^3 = I)")
    need(np.linalg.norm(C4 - np.eye(4)) > 0.5,
         "op1 tick C is not the identity")
    need(np.linalg.norm(tick @ tick @ tick - np.eye(256)) < 1e-13,
         "op1 full tick is order 3 on 256-dim matter space")
    return dict(
        id="op1_local_tick",
        status="native_declared",
        construction="C = eye(4)[:,[1,2,0,3]] (3-cycle 0->1->2->0 on carrier 0, "
                     "carrier 3 fixed); tick = kron(C, I_64) on the 256-dim matter space",
        cost="1 native clock tick (no external resource)",
        checks=["tick C^3 = I", "C != I", "full tick order 3 on 256-dim"],
    )


def op2_coupling(star):
    M = star["M"]
    G = star["G"]
    H = star["H"]
    energies = star["energies"]
    deg = star["deg"]
    microvals = star["microvals"]
    need(len(star["med_index"]) == 288,
         "op2 full microscopic star mediator dimension is 288")
    need(np.linalg.norm(M.T @ M - (6 * np.eye(256) - 2 * G)) < 1e-13,
         "op2 coupling Gram M^T M = 6 I_256 - 2 G", "numerical")
    need(H.shape == (544, 544),
         "op2 microscopic Hamiltonian is 544 x 544")
    need(int(sum(deg)) == 544,
         "op2 full dressed star dimension sum = 544")
    need(max(abs(np.sort(microvals) - np.sort(np.repeat(energies, deg)))) < 1e-12,
         "op2 all 544 microscopic eigenvalues match the 14 analytic levels",
         "numerical")
    levels = [{"energy": float(energies[i]), "multiplicity": int(deg[i])}
              for i in range(len(energies))]
    return dict(
        id="op2_edge_pair_coupling",
        status="native_declared",
        construction="288x256 coupling M (3 arms j=1,2,3 x 16 remaining matter "
                     "configs x 6 pair colours, sign +1 if a<b else -1); "
                     "H = [[0, t M^T],[t M, Delta I_288]] with t/Delta = 1/20",
        cost="native Hamiltonian term (t, Delta are declared scales, not synthesised)",
        checks=["mediator dim 288", "M^T M = 6 I - 2 G", "H is 544x544",
                "deg sum 544", "14-level spectrum match to 1e-12"],
        spectrum_levels=levels,
    )


def op3_free_evolution(star):
    tau = star["tau"]
    total = float(sum(tau))
    return dict(
        id="op3_free_time_evolution",
        status="additional_resource",
        construction="exp(-i tau_j H) for exactly chosen tau_j = pi hbar/(E_j - E_0); "
                     "the exact real time is a declared ideal resource, not a "
                     "primitive-derived quantity",
        cost="{:.6f} hbar/Delta per filter (13 exact real times)".format(total),
        checks=["declared ideal resource (no operator identity to check)"],
        one_filter_total_time=total,
    )


def op4_controlled_H():
    return dict(
        id="op4_controlled_H_evolution",
        status="additional_resource",
        construction="Hadamard-test controlled version of exp(-i tau_j H): a control "
                     "qubit coherently selects evolution vs identity. NOT derived from "
                     "primitives 1-2 (local tick C, native coupling t); this is the "
                     "precise remaining control gap of the protocol.",
        cost="1 controlled-H call per filter factor; 13 per filter, 26 for start+end",
        checks=["declared additional resource (the non-native gap)"],
        is_the_gap=True,
    )


def op5_spectral_filter(star):
    microvals = star["microvals"]
    microvec = star["microvec"]
    targetE = star["targetE"]
    energies = star["energies"]
    tau = star["tau"]
    f_full = np.ones(544, complex)
    for time in tau:
        f_full *= 0.5 * (1 + np.exp(-1j * time * (microvals - targetE)))
    pf = (microvec * f_full) @ microvec.conj().T
    P0 = np.outer(microvec[:, 0], microvec[:, 0].conj())
    need(np.linalg.norm(pf - P0) < 1e-10,
         "op5 full 544-dim 13-factor filter equals dressed ground projector",
         "numerical")
    f = np.ones(len(energies), complex)
    for time in tau:
        f *= 0.5 * (1 + np.exp(-1j * time * (energies - targetE)))
    need(abs(f[0] - 1) < 1e-14,
         "op5 scalar filter keeps the ground level (f[0] = 1)")
    need(max(abs(f[1:])) < 1e-12,
         "op5 scalar filter annihilates all 13 non-ground levels", "numerical")
    short = np.ones(len(energies), complex)
    for time in tau[:6]:
        short *= 0.5 * (1 + np.exp(-1j * time * (energies - targetE)))
    need(max(abs(short[7:])) > 1e-5,
         "op5 NEGATIVE CONTROL: lower-only (6-factor) filter fails on full space",
         "numerical")
    total = float(sum(tau))
    return dict(
        id="op5_spectral_filter",
        status="derived_checked",
        construction="Ordered product over j=1..13 of A_j = (I + exp(-i tau_j "
                     "(H-E0)/hbar))/2 equals the dressed ground projector P0_dressed "
                     "on the full 544-dim space. Derived from op3 (free evolution) + "
                     "op4 (controlled-H) + 13 coherent ancilla bits (or 13 fresh "
                     "measured bits).",
        cost="13 controlled evolutions, {:.6f} hbar/Delta per filter".format(total),
        checks=["full 544-dim filter = P0_dressed (norm < 1e-10)",
                "scalar filter f[0]=1",
                "scalar filter annihilates 13 non-ground levels",
                "NEGATIVE CONTROL: 6-low-level filter fails (max |short[7:]| > 1e-5)"],
        one_filter_total_time=total,
        max_residual_after_filter=float(max(abs(f[1:]))),
    )


def op6_herald(star):
    pf = dressed_projector(star)
    P0 = np.outer(star["microvec"][:, 0], star["microvec"][:, 0].conj())
    need(np.linalg.norm(pf - P0) < 1e-10,
         "op6 filter rebuilt for herald equals dressed ground projector",
         "numerical")
    w = star["w"]
    A = star["A"]
    bare_filter = pf[:256, :256]
    need(np.linalg.norm(bare_filter - w * A) < 1e-10,
         "op6 P_bare P0_dressed P_bare = w P_Omega on bare matter", "numerical")
    need(abs(w - 0.9856429312) < 1e-7,
         "op6 w = (1 + 1/sqrt(1+24 t^2))/2 ~ 0.9856429312", "numerical")
    return dict(
        id="op6_empty_mediator_herald",
        status="native_declared",
        construction="Physical occupancy measurement of the 288-dim mediator space; "
                     "post-selecting empty mediators projects the dressed ground state "
                     "onto w P_Omega on the 256-dim bare matter space.",
        cost="1 occupancy measurement (native physical readout)",
        checks=["filter = P0_dressed", "P_bare P0 P_bare = w P_Omega (norm < 1e-10)",
                "w ~ 0.9856429312"],
        w=float(w),
    )


def op7_record_pulse():
    W = np.zeros((6, 16))
    for k, (a, b) in enumerate(combinations(range(4), 2)):
        W[k, 4 * a + b] = 1 / np.sqrt(2)
        W[k, 4 * b + a] = -1 / np.sqrt(2)
    need(np.linalg.norm(W @ W.conj().T - np.eye(6)) < 1e-14,
         "op7 W W^dagger = I_6 (partial isometry)", "numerical")
    Pm = W.T @ W
    Pp = np.eye(16) - Pm
    U22 = np.block([
        [Pp, -1j * W.T],
        [-1j * W, np.zeros((6, 6))],
    ])
    U = np.kron(U22, np.eye(2))
    need(U.shape == (44, 44),
         "op7 U_res is 44 x 44 (kron of 22-dim U with record qubit)")
    X = np.array([[0, 1], [1, 0]])
    Q = np.zeros((44, 44))
    Q[:32, :32] = np.eye(32)
    Q[32:, 32:] = np.kron(np.eye(6), X)
    R = np.kron(Pp, np.eye(2)) + np.kron(Pm, X)
    macro = np.kron(U22.conj().T, np.eye(2)) @ Q @ np.kron(U22, np.eye(2))
    target = np.zeros((44, 44))
    target[:32, :32] = R
    target[32:, 32:] = np.eye(12)
    need(np.linalg.norm(macro - target) < 1e-13,
         "op7 U_res^dagger Q U_res = R ⊕ I_12 (no extra quarter phases)",
         "numerical")
    return dict(
        id="op7_resonant_record_pulse",
        status="derived_checked",
        construction="22-dim U = [[P+, -i W^T],[-i W, 0]] with W: 6x16 partial "
                     "isometry (W W^dagger = I_6); 44-dim record space = kron(U, I_2). "
                     "Q = I_32 ⊕ (I_6 ⊗ X) (occupancy query). Verified "
                     "U_res^dagger Q U_res = R ⊕ I_12 with R = kron(P+, I_2) + "
                     "kron(P-, X) (record involution).",
        cost="1 resonant pulse + 1 occupancy query",
        checks=["W W^dagger = I_6", "U_res is 44x44",
                "U_res^dagger Q U_res = R ⊕ I_12 (norm < 1e-13)"],
        residual=float(np.linalg.norm(macro - target)),
    )


def op8_reset(star):
    om = star["om"]
    A = np.outer(om, om)
    K = np.eye(256)
    for j in [1, 2, 3]:
        S = swap_matrix(4, 0, j)
        K = (np.eye(256) - S) @ K / 2
    need(np.linalg.norm(K @ om - om) < 1e-14,
         "op8 feedback K fixes Omega (the 4-carrier singlet)", "numerical")
    beta = (9 + np.sqrt(17)) / 32
    need(np.max(eigh(K.T @ K - A, eigvals_only=True)) < beta + 1e-13,
         "op8 contraction bound max eig(K^T K - |Omega><Omega|) <= beta", "numerical")
    rr = 1 - (1 - beta) / 24
    need(abs(rr - 0.97542071045) < 1e-9,
         "op8 contraction rate r = 1-(1-beta)/24 ~ 0.97542071045", "numerical")
    need(rr ** 556 < 1e-6,
         "op8 556-cycle bound (r^556 < 1e-6)", "numerical")
    floor = 1 / (1 - rr)
    need(abs(floor - 40.6847) < 1e-2,
         "op8 error floor multiplier 1/(1-r) ~ 40.6847", "numerical")
    e0 = np.zeros(256)
    e0[27] = 1
    rho = np.eye(256) / 256
    checkpoints = {}
    for m in range(1, 557):
        success = K @ rho @ K.T
        failure = float(np.trace(rho) - np.trace(success))
        new = success + failure * np.outer(e0, e0)
        oldF = float(om @ rho @ om)
        newF = float(om @ new @ om)
        need(abs(newF - oldF - failure / 24) < 2e-13,
             "op8 feedback weight identity step " + str(m), "numerical")
        need(1 - newF <= rr * (1 - oldF) + 2e-13,
             "op8 feedback contraction step " + str(m), "numerical")
        rho = new
        if m in [1, 8, 32, 64, 128, 256, 556]:
            checkpoints[m] = 1 - newF
    return dict(
        id="op8_reset_feedback_channel",
        status="additional_resource",
        construction="Feedback channel E(rho) = K rho K^dagger + "
                     "Tr[(I-K^dagger K) rho] rho0 with K = prod_{j=1,2,3} (I-S_{0j})/2 "
                     "on the 256-dim matter space, rho0 = |e0><e0|. Needs a "
                     "measurement+reset environment (not native).",
        cost="556 feedback cycles for 1e-6 infidelity; up to 8 classical colour bits "
             "per reset cell + 3 exchange record bits per cycle",
        checks=["K fixes Omega", "contraction bound <= beta + 1e-13",
                "r ~ 0.97542071045", "r^556 < 1e-6", "error floor ~ 40.6847",
                "556-step weight+contraction identities"],
        beta=float(beta),
        rate=float(rr),
        cycle_count_for_1e6=int(ceil(log(1e-6) / log(rr))),
        independent_cells_4096_cycles_for_global_1e6=int(ceil(log(1e-6 / 4096) / log(rr))),
        error_floor_multiplier=float(floor),
        maximally_mixed_infidelity=checkpoints,
        colour_bits_per_cycle=8,
        record_bits_per_cycle=3,
    )


def op9_echo_end_test(star):
    pf = dressed_projector(star)
    w = star["w"]
    om = star["om"]
    bare_filter = pf[:256, :256]
    C4 = np.eye(4)[:, [1, 2, 0, 3]]
    tick = np.kron(C4, np.eye(64))
    plus = (np.eye(256) + swap_matrix(4, 0, 1)) / 2
    minus = np.eye(256) - plus
    ticked = tick @ om
    kept = float(np.linalg.norm(bare_filter @ tick.T @ ticked) ** 2)
    fresh = float(
        np.linalg.norm(bare_filter @ tick.T @ plus @ ticked) ** 2
        + np.linalg.norm(bare_filter @ tick.T @ minus @ ticked) ** 2
    )
    need(abs(kept - w * w) < 1e-12,
         "op9 conditional end retained = w^2", "numerical")
    need(abs(fresh - 17 * w * w / 32) < 1e-12,
         "op9 conditional end fresh = 17 w^2/32", "numerical")
    chi = np.zeros(256)
    for aa, bb, sgn1 in [(0, 1, 1), (1, 0, -1)]:
        for cc, dd, sgn2 in [(2, 3, 1), (3, 2, -1)]:
            chi[aa * 64 + bb * 16 + cc * 4 + dd] = sgn1 * sgn2 / 2
    prep = bare_filter @ chi
    p_prep = float(np.vdot(prep, prep).real)
    need(abs(p_prep - w * w / 6) < 1e-12,
         "op9 preparation raw probability w^2/6", "numerical")
    need(abs(p_prep * kept - w ** 4 / 6) < 1e-12,
         "op9 unconditional retained = w^4/6", "numerical")
    need(abs(p_prep * fresh - 17 * w ** 4 / 192) < 1e-12,
         "op9 unconditional fresh = 17 w^4/192", "numerical")
    need(abs((p_prep * fresh) / (p_prep * kept) - 17 / 32) < 1e-12,
         "op9 fresh/retained ratio exactly 17/32", "numerical")
    return dict(
        id="op9_echo_end_test",
        status="derived_checked",
        construction="Same microscopic 13-factor filter used at start and end; "
                     "tick C = 3-cycle (1,2,0,3) on carrier 0, plus/minus projectors on "
                     "carriers (0,1). Rebuilds the echo computation exactly.",
        cost="2 filters (start+end) = 26 controlled evolutions, "
             "{:.6f} hbar/Delta total filter time; 2 heralds".format(2 * float(sum(star["tau"]))),
        checks=["conditional retained = w^2", "conditional fresh = 17 w^2/32",
                "preparation raw prob = w^2/6", "unconditional retained = w^4/6",
                "unconditional fresh = 17 w^4/192", "fresh/retained ratio = 17/32"],
        w=float(w),
        conditional_retained=kept,
        conditional_fresh=fresh,
        preparation_probability=p_prep,
        unconditional_retained=float(p_prep * kept),
        unconditional_fresh=float(p_prep * fresh),
        mean_attempts_preparation=float(1 / p_prep),
    )


def op10_amplification(star):
    w = star["w"]
    a = w / 6
    phi = float(np.arccos(1 - (3 - np.sqrt(5)) / (4 * a)))
    v = np.sqrt([a, 1 - a]).astype(complex)
    Rchi = np.eye(2) + (np.exp(1j * phi) - 1) * np.outer(v, v.conj())
    Rtar = np.diag([np.exp(1j * phi), 1])
    fin = Rchi @ Rtar @ Rchi @ Rtar @ v
    need(abs(fin[0]) ** 2 > 1 - 1e-13,
         "op10 two-step amplification identity (|fin[0]|^2 > 1-1e-13)", "numerical")
    return dict(
        id="op10_amplification",
        status="additional_resource",
        construction="Optional coherent boost: 52 controlled-H calls for two steps; "
                     "phase-matching number phi = arccos(1 - (3-sqrt(5))/(4 a)) with "
                     "a = w/6. Verified the two-step amplification identity on a 2-level "
                     "toy (Rchi Rtar Rchi Rtar v -> ~|0>).",
        cost="52 controlled-H calls (two steps); declared additional resource",
        checks=["two-step amplification identity (|fin[0]|^2 > 1-1e-13)"],
        a=float(a),
        matched_phase=phi,
        amplified_success_probability=float(abs(fin[0]) ** 2),
    )


def run():
    star = build_star()
    ops = [
        op1_tick(),
        op2_coupling(star),
        op3_free_evolution(star),
        op4_controlled_H(),
        op5_spectral_filter(star),
        op6_herald(star),
        op7_record_pulse(),
        op8_reset(star),
        op9_echo_end_test(star),
        op10_amplification(star),
    ]
    tau = star["tau"]
    one_filter_time = float(sum(tau))
    two_filter_time = float(2 * sum(tau))
    w = float(star["w"])
    p_prep = w * w / 6
    not_derived = [
        "controlled-H evolution (op4): the Hadamard-test controlled version of "
        "exp(-i tau_j H) is NOT derived from native primitives (tick C, coupling t); "
        "this is the precise remaining control gap",
        "exact real times tau_j (op3): the exact choice tau_j = pi hbar/(E_j - E_0) "
        "is a declared ideal resource, not synthesised from primitives",
        "measurement+reset environment (op8): the feedback channel needs an external "
        "bath with measurement and reset capability",
        "record resonance tuning (op7): the resonant pulse frequency must be tuned "
        "to the record-block transition; the resonance condition is an additional "
        "calibration datum",
    ]
    totals = dict(
        controlled_evolutions_start_plus_end=26,
        total_filter_time_hbar_over_Delta=two_filter_time,
        one_filter_time_hbar_over_Delta=one_filter_time,
        coherent_filter_ancillas=13,
        occupation_heralds=2,
        record_pulses=1,
        mean_preparation_attempts=float(1 / p_prep),
        feedback_cycles_for_1e6=int(ceil(log(1e-6) / log(1 - (1 - (9 + np.sqrt(17)) / 32) / 24))),
        colour_bits_per_reset_cycle=8,
        record_bits_per_reset_cycle=3,
        not_derived_controls=not_derived,
    )
    RESULT["operations"] = ops
    RESULT["totals"] = totals
    RESULT["checks"] = CHECKS
    RESULT["count"] = len(CHECKS)
    RESULT["exact_count"] = sum(1 for c in CHECKS if c["kind"] == "exact")
    RESULT["numerical_count"] = sum(1 for c in CHECKS if c["kind"] == "numerical")
    RESULT["T1_T8_closed"] = []
    RESULT["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT["scope"] = ("Theory contract = internal consistency only. No promotion "
                      "claims. derived_checked = operator identity recomputed on the "
                      "actual matrices; additional_resource = declared external "
                      "resource not derivable from native primitives 1-2.")
    return RESULT


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "ops_ledger.json"))
    args = ap.parse_args()
    result = run()
    Path(args.output).write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n")
    summary = {k: v for k, v in result.items()
              if k not in ("checks", "operations")}
    summary["operation_statuses"] = [
        {"id": o["id"], "status": o["status"]} for o in result["operations"]]
    print(json.dumps(summary, indent=2, sort_keys=True))

