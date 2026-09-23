"""Follow-up 1: who operates the laboratory?

The primitive list is frozen here. Every handle is either reduced to another
handle, derived from the source, or shown to be an independent resource by an
obstruction with a number attached. Weight multisets and root data are exact
integer arithmetic; the two dynamical bounds are numerical and marked as such.

No T1-T8 closure, no promotion. Research checker for experiments/ only.
"""
from itertools import product, combinations
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import argparse, hashlib, json
import numpy as np
from scipy.linalg import eigh

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(dict(name=name, kind=kind))


# ---------------------------------------------------------------- obstruction 1
def record_sector():
    """Recording needs Sym^2(4). The adjoint has no such channel; 3875 has one."""
    roots = set()
    for i, j in combinations(range(8), 2):
        for si, sj in product((2, -2), repeat=2):
            v = [0] * 8
            v[i] = si
            v[j] = sj
            roots.add(tuple(v))
    for s in product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0:
            roots.add(s)
    need(len(roots) == 240, "E8 roots")

    # A3 = D3 weight content of every branch of the adjoint, in doubled coordinates.
    content = Counter()
    for r in roots:
        content[r[5:]] += 1
    content[(0, 0, 0)] += 8  # Cartan
    need(sum(content.values()) == 248, "adjoint weight bookkeeping closes")

    spinor_plus = [a for a in product((1, -1), repeat=3) if a.count(-1) % 2 == 0]
    spinor_minus = [a for a in product((1, -1), repeat=3) if a.count(-1) % 2 == 1]
    sym2_4 = Counter(tuple(x + y for x, y in zip(a, b))
                     for a, b in combinations(spinor_plus, 2))
    sym2_4 += Counter(tuple(2 * x for x in a) for a in spinor_plus)
    sym2_4bar = Counter(tuple(x + y for x, y in zip(a, b))
                        for a, b in combinations(spinor_minus, 2))
    sym2_4bar += Counter(tuple(2 * x for x in a) for a in spinor_minus)
    need(sum(sym2_4.values()) == 10 and sum(sym2_4bar.values()) == 10,
         "Sym^2(4) and Sym^2(4bar) have ten weights each")
    triples = [w for w in sym2_4 if all(w)]
    need(len(triples) == 4, "Sym^2(4) contains the four fully occupied weights")
    need(all(content[w] == 0 for w in triples),
         "no weight of Sym^2(4) with three nonzero entries occurs in the adjoint")

    # 3875 = 135 + 1820 + 1920 under SO(16); 1820 = Lambda^4(16).
    need(135 + 1820 + 1920 == 3875, "SO(16) content of the 3875")
    need(len(list(combinations(range(16), 4))) == 1820, "1820 = Lambda^4(16)")
    split = [(k, len(list(combinations(range(10), k))) * len(list(combinations(range(6), 4 - k))))
             for k in range(5)]
    need(sum(n for _, n in split) == 1820, "Lambda^4(10+6) closes")
    need(dict(split)[1] == 10 * 20, "the (10, Lambda^3(6)) channel has dimension 200")

    # Lambda^3(6) = 10 + 10bar of SU(4): exact weight multiset identity.
    six = [tuple(2 * x for x in e) for e in
           [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
    lam3 = Counter(tuple(a + b + c for a, b, c in zip(*t)) for t in combinations(six, 3))
    need(sum(lam3.values()) == 20, "Lambda^3(6) has twenty weights")
    need(lam3 == sym2_4 + sym2_4bar, "Lambda^3(6) = Sym^2(4) + Sym^2(4bar), exact weight identity")

    # Witness that recording really lives in Sym^2: computational context.
    proj = np.zeros((16, 16))
    for j in range(4):
        proj[5 * j, 5 * j] = 1.0
    Q = np.eye(16) - 2 * proj
    swap = np.zeros((16, 16))
    for a, b in product(range(4), repeat=2):
        swap[4 * b + a, 4 * a + b] = 1.0
    sym = (np.eye(16) + swap) / 2
    reflected = np.eye(16) - (np.eye(16) + Q) / 2
    need(abs(np.trace(reflected) - 4) < 1e-12, "the reflected space of Q is four dimensional", "numerical")
    need(np.linalg.norm(sym @ reflected - reflected) < 1e-12,
         "the reflected space lies entirely inside Sym^2", "numerical")
    A = np.stack([np.eye(16).ravel(), swap.ravel()], axis=1)
    residual = float(np.linalg.norm(A @ np.linalg.lstsq(A, Q.ravel(), rcond=None)[0] - Q.ravel()))
    need(residual > 1e-6,
         "Q is not a combination of identity and exchange: recording is not A3 covariant", "numerical")

    return {"sym2_4_present_in_248": False,
            "blocking_weights": [list(w) for w in sorted(triples)],
            "record_channel_in_3875": "Lambda^4(16) contains (10_D5, Lambda^3(6)) = (10, 10 + 10bar), dimension 200",
            "identity_checked": "Lambda^3(6) weight multiset equals Sym^2(4) + Sym^2(4bar)",
            "consequence": "the record is an independent resource inside the adjoint and requires the 3875"}


# ---------------------------------------------------------------- obstruction 2
def unital_obstruction():
    """Free evolution plus a classical clock generates unital channels only."""
    rng = np.random.default_rng(20260914)
    t = 0.05
    Delta = 1.0
    basis = list(product(range(4), repeat=4))
    med = {}
    M = np.zeros((288, 256))
    for col, m in enumerate(basis):
        for j in (1, 2, 3):
            a, b = m[0], m[j]
            if a == b:
                continue
            mm = list(m)
            mm[0] = mm[j] = -1
            key = (j, tuple(mm), min(a, b), max(a, b))
            M[med.setdefault(key, len(med)), col] = 1 if a < b else -1
    need(len(med) == 288, "star mediator dimension")
    H = np.block([[np.zeros((256, 256)), t * M.T], [t * M, Delta * np.eye(288)]])
    vals, vecs = eigh(H)
    levels = np.unique(np.round(vals, 12))
    need(len(levels) == 14, "the star has fourteen distinct levels", "numerical")

    # Channel A: evolve for a random time, forget the time. Exactly unital.
    times = rng.uniform(0.0, 4000.0, size=64)
    dim = H.shape[0]
    img = np.zeros((dim, dim), complex)
    for tau in times:
        U = vecs @ np.diag(np.exp(-1j * tau * vals)) @ vecs.conj().T
        img += U @ np.eye(dim) @ U.conj().T
    img /= len(times)
    need(np.linalg.norm(img - np.eye(dim)) < 1e-8,
         "random-time evolution is unital: it maps the identity to the identity", "numerical")

    # Entropy cannot fall under a unital channel, so no pure target is reachable.
    rho = np.eye(dim) / dim
    out = np.zeros_like(img)
    for tau in times:
        U = vecs @ np.diag(np.exp(-1j * tau * vals)) @ vecs.conj().T
        out += U @ rho @ U.conj().T
    out /= len(times)
    need(np.linalg.norm(out - rho) < 1e-10,
         "the maximally mixed state is a fixed point of every unital channel", "numerical")
    need(float(max(eigh(out, eigvals_only=True))) < 1e-2,
         "no purification: the largest population stays at the mixed value", "numerical")

    # Channel B: the thirteen factor filter. Not unital, and that is the point.
    target = vals[0]
    taus = [np.pi / (lv - target) for lv in levels[1:]]
    need(len(taus) == 13, "thirteen filter times")
    A = np.eye(dim, dtype=complex)
    for tau in taus:
        A = 0.5 * (np.eye(dim) + vecs @ np.diag(np.exp(-1j * tau * (vals - target))) @ vecs.conj().T) @ A
    P0 = np.outer(vecs[:, 0], vecs[:, 0].conj())
    need(np.linalg.norm(A - P0) < 1e-9, "the filter reproduces the dressed ground projector", "numerical")
    need(np.linalg.norm(A @ A.conj().T - np.eye(dim)) > 1.0,
         "the filter is not unital: it is a genuine entropy sink", "numerical")

    total_time = float(sum(taus))
    J = 2 * t * t / Delta
    return {"random_time_channel_unital": True,
            "filter_channel_unital": False,
            "filter_total_time_hbar_over_Delta": total_time,
            "filter_total_time_hbar_over_J": total_time * J,
            "start_plus_end_time_hbar_over_J": 2 * total_time * J,
            "statement": "unital channels cannot lower entropy, so preparation of a pure target "
                         "from a generic input needs measurement or a cold reservoir; free evolution "
                         "and a classical clock supply neither"}


# ---------------------------------------------------------------- obstruction 3
def isolation_window():
    """An isolated star is not a native handle: neighbouring bonds do not commute."""
    def swap3(i, j):
        S = np.zeros((64, 64))
        for w in product(range(4), repeat=3):
            v = list(w)
            v[i], v[j] = v[j], v[i]
            S[v[0] * 16 + v[1] * 4 + v[2], w[0] * 16 + w[1] * 4 + w[2]] = 1.0
        return S
    Pe = (np.eye(64) + swap3(0, 1)) / 2
    Pf = (np.eye(64) + swap3(1, 2)) / 2
    C = Pe @ Pf - Pf @ Pe
    elementary = float(max(abs(eigh(C.conj().T @ C, eigvals_only=True))) ** 0.5)
    need(elementary > 0.4, "two bonds sharing one place do not commute", "numerical")

    # Clebsch star: five bonds at the centre, every leaf carries four outside bonds.
    pairs = 5 * 4
    total = pairs * elementary
    t, Delta = 0.05, 1.0
    J = 2 * t * t / Delta
    basis = list(product(range(4), repeat=4))
    med = {}
    for m in basis:
        for j in (1, 2, 3):
            a, b = m[0], m[j]
            if a == b:
                continue
            mm = list(m)
            mm[0] = mm[j] = -1
            med.setdefault((j, tuple(mm), min(a, b), max(a, b)), len(med))
    M = np.zeros((len(med), 256))
    for col, m in enumerate(basis):
        for j in (1, 2, 3):
            a, b = m[0], m[j]
            if a == b:
                continue
            mm = list(m)
            mm[0] = mm[j] = -1
            M[med[(j, tuple(mm), min(a, b), max(a, b))], col] = 1 if a < b else -1
    H = np.block([[np.zeros((256, 256)), t * M.T], [t * M, Delta * np.eye(len(med))]])
    vals = eigh(H, eigvals_only=True)
    levels = np.unique(np.round(vals, 12))
    required = 2 * float(sum(np.pi / (lv - levels[0]) for lv in levels[1:])) * J

    # Guaranteed factorisation window from the standard commutator bound.
    eps = 1e-6
    window = float(np.sqrt(2 * eps / total))
    need(window < required, "the guaranteed isolation window is shorter than the protocol", "numerical")
    return {"elementary_commutator_norm_over_J": elementary,
            "non_commuting_pairs_at_one_Clebsch_star": pairs,
            "commutator_budget_over_J": total,
            "guaranteed_isolation_window_hbar_over_J_at_1e_6": window,
            "required_isolated_time_hbar_over_J": required,
            "shortfall_factor": required / window,
            "statement": "the star filter needs about thirty inverse exchange times of isolated "
                         "evolution; the guaranteed factorisation window at infidelity 1e-6 is four "
                         "orders of magnitude shorter, so isolation is an external switch, not a "
                         "consequence of the source Hamiltonian"}


# ---------------------------------------------------------------- reduction
def record_reduction():
    """Occupation query and projective measurement reduce to the resonant record."""
    W = np.zeros((6, 16))
    for k, (a, b) in enumerate(combinations(range(4), 2)):
        W[k, 4 * a + b] = 1 / np.sqrt(2)
        W[k, 4 * b + a] = -1 / np.sqrt(2)
    Pm = W.T @ W
    Pp = np.eye(16) - Pm
    U = np.block([[Pp, -1j * W.T], [-1j * W, np.zeros((6, 6))]])
    need(np.linalg.norm(U @ U.conj().T - np.eye(22)) < 1e-13, "resonant transfer is unitary", "numerical")
    X = np.array([[0, 1], [1, 0]])
    Q = np.zeros((44, 44))
    Q[:32, :32] = np.eye(32)
    Q[32:, 32:] = np.kron(np.eye(6), X)
    R = np.kron(Pp, np.eye(2)) + np.kron(Pm, X)
    macro = np.kron(U.conj().T, np.eye(2)) @ Q @ np.kron(U, np.eye(2))
    target = np.zeros((44, 44))
    target[:32, :32] = R
    target[32:, 32:] = np.eye(12)
    need(np.linalg.norm(macro - target) < 1e-13,
         "the record macro operation needs no extra quarter phases", "numerical")

    # Reading the register bit is exactly the projective measurement of Lambda^2 / Sym^2.
    rng = np.random.default_rng(14092026)
    for trial in range(16):
        psi = rng.normal(size=16) + 1j * rng.normal(size=16)
        psi /= np.linalg.norm(psi)
        out = R @ np.kron(psi, np.array([1, 0])).reshape(32)
        branch0 = out.reshape(16, 2)[:, 0]
        branch1 = out.reshape(16, 2)[:, 1]
        need(np.linalg.norm(branch0 - Pp @ psi) < 1e-13,
             "register bit zero leaves the symmetric component, trial " + str(trial), "numerical")
        need(np.linalg.norm(branch1 - Pm @ psi) < 1e-13,
             "register bit one leaves the antisymmetric component, trial " + str(trial), "numerical")
    return {"record_is_unitary_on_the_local_44_sector": True,
            "measurement_reduces_to": "resonant record plus reading one register bit",
            "occupation_query_reduces_to": "the same record applied to the mediator number sector",
            "reset_reduces_to": "measurement plus a fresh carrier from outside the hull"}


# ---------------------------------------------------------------- obstruction 4
def half_charge_obstruction():
    """Is a half charge shift an operation of this source? The Z4 glue says no.

    E8 contains D5 + D3 with cyclic glue group of order four generated by (s,s).
    A half charge shift is an element g with 2g = (s,s), that is a Z8 extension.
    Write everything in quadrupled integer coordinates: 4g = (1,...,1).
    """
    glue = tuple(F(1, 2) for _ in range(8))  # (s,s), the order four generator
    need(sum(x * x for x in glue) == 2, "the glue generator has norm two")
    need(sum(x * x for x in glue) / 2 == 1, "the order four glue class has integer conformal weight")
    doubled = tuple(2 * x for x in glue)
    need(all(x == 1 for x in doubled) and sum(x * x for x in doubled) == 8,
         "twice the generator is an integral vector of the lattice")

    # Minimal norms of the four classes, hence their conformal weights.
    minimal = {"(0,0)": (F(0), F(0)), "(v,v)": (F(1), F(1)),
               "(s,s)": (F(5, 4), F(3, 4)), "(c,c)": (F(5, 4), F(3, 4))}
    weights = {k: (a + b) / 2 for k, (a, b) in minimal.items()}
    need(list(weights.values()) == [F(0), F(1), F(1), F(1)],
         "all four glue classes carry integer conformal weight: the Z4 extension is allowed")

    # Every representative of a square root of the generator, over a full box of
    # lattice shifts. Coordinates are quadrupled, so the squared norm is n/16.
    offenders = 0
    tested = 0
    for lam in product(range(-2, 3), repeat=8):
        if sum(lam[:5]) % 2 or sum(lam[5:]) % 2:
            continue  # not in D5 + D3
        tested += 1
        n16 = sum((1 + 4 * x) ** 2 for x in lam)
        need_norm = F(n16, 16)
        if need_norm.denominator != 2:
            offenders += 1
        h = need_norm / 2
        if h.denominator == 1:
            offenders += 1
    need(tested > 20000, "the lattice shift box is large enough to be a real census")
    need(offenders == 0,
         "every square root of the glue generator has squared norm one half modulo one, "
         "hence conformal weight one quarter or three quarters, never an integer")
    return {"glue_group_order": 4,
            "glue_class_weights": {k: str(v) for k, v in weights.items()},
            "half_charge_candidate_weight_mod_one": ["1/4", "3/4"],
            "lattice_shifts_tested": tested,
            "integer_weight_candidates": offenders,
            "verdict": "a half charge shift would double the glue group to Z8. Every candidate "
                       "generator has conformal weight one quarter modulo one half, so it is not an "
                       "integer spin simple current and does not extend the conformal embedding. "
                       "The obstruction is a property of this source, not of an added charge lattice.",
            "what_would_be_needed": "a different embedding whose glue group already has even order "
                                    "eight, or a half charge carried outside the glue"}


# ---------------------------------------------------------------- frozen list
def frozen_primitives(unital, isolation):
    J_time = isolation["required_isolated_time_hbar_over_J"]
    return [
        {"handle": "free evolution exp(-i H t)", "status": "derived",
         "implementation": "the source Hamiltonian itself", "cost": "time t, no ancilla, no entropy"},
        {"handle": "classical clock randomisation", "status": "derived up to a clock",
         "implementation": "free evolution with a forgotten duration",
         "cost": "one classical random number; the channel is unital"},
        {"handle": "isolated star / isolated bond", "status": "independent resource",
         "implementation": "none inside the source: neighbouring bonds do not commute",
         "cost": "an external switch; guaranteed window "
                 + repr(isolation["guaranteed_isolation_window_hbar_over_J_at_1e_6"])
                 + " against a requirement of " + repr(J_time) + " hbar/J"},
        {"handle": "controlled evolution c-exp(-i tau H)", "status": "reducible",
         "implementation": "one ancilla qubit plus a switchable coupling; the ancilla is not "
                           "supplied by the adjoint",
         "cost": "13 ancillas or 13 fresh measured bits per filter, "
                 + repr(unital["filter_total_time_hbar_over_J"]) + " hbar/J per marker"},
        {"handle": "resonant record", "status": "independent resource",
         "implementation": "exact as a 44 dimensional unitary, but its sector Sym^2(4) is absent "
                           "from the adjoint and first appears in the 3875",
         "cost": "one register carrier outside the hull per record"},
        {"handle": "mediator occupation query", "status": "reducible",
         "implementation": "resonant record on the mediator number sector plus one register bit",
         "cost": "one register bit, no extra sector beyond the record"},
        {"handle": "projective colour measurement", "status": "reducible",
         "implementation": "record plus register readout", "cost": "one classical bit per readout"},
        {"handle": "reset to a fresh carrier", "status": "independent resource",
         "implementation": "measurement plus supply of a carrier outside the hull",
         "cost": "up to 8 erased classical bits per cell and cycle, k_B T ln 2 each"},
        {"handle": "target state projector P_Omega", "status": "forbidden as a primitive",
         "implementation": "must be built from the list above; the 13 factor filter does exactly that",
         "cost": "the filter cost, never free"},
    ]


def run():
    RESULT["record_sector"] = record_sector()
    unital = unital_obstruction()
    RESULT["unital_obstruction"] = unital
    isolation = isolation_window()
    RESULT["isolation"] = isolation
    RESULT["reductions"] = record_reduction()
    RESULT["half_charge"] = half_charge_obstruction()
    RESULT["frozen_primitive_list"] = frozen_primitives(unital, isolation)
    independent = [p["handle"] for p in RESULT["frozen_primitive_list"]
                   if p["status"] == "independent resource"]
    need(len(independent) == 3, "exactly three independent resources remain after all reductions")
    RESULT["minimality"] = {
        "independent_resources": independent,
        "separating_invariants": {
            "isolated star / isolated bond": "breaks time translation invariance of the source Hamiltonian",
            "resonant record": "breaks the A3 sector content of the adjoint: needs Sym^2(4)",
            "reset to a fresh carrier": "breaks unitality: it is the only entropy sink",
        },
        "argument": "the three obstructions are witnessed by three different invariants, so no two of "
                    "them can be traded for one another, and none follows from free evolution",
        "native_controls_derived": False,
    }
    RESULT["checks"] = CHECKS
    RESULT["count"] = len(CHECKS)
    RESULT["T1_T8_closed"] = []
    RESULT["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return RESULT


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "primitives.json"))
    args = ap.parse_args()
    out = run()
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "checks"}, indent=2, sort_keys=True))
