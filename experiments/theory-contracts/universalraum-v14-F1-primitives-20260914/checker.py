"""F1: freeze every lab handle as a primitive TFPT compiler op, with costs.

NON-RH. experiments/ only. No promotion, no hidden target projector.
P0 / Omega are derived outputs, never circuit inputs. Allowed input is the
two-singlet chi (overlap 1/6). Controlled-exp, resonance, Q, measure/reset
remain declared primitives — they are implemented and costed, not derived
from P1/P2.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import pi, sqrt
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

import numpy as np
from scipy.linalg import eigh
import sympy as sp

HERE = Path(__file__).resolve().parent
CORE = HERE.parent / "compiler-origin-audit-20260913" / "context_instrument.py"
CORE_PIN = "ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995"
CHECKS: list[dict] = []

DELTA = 1.0
T_HOP = 0.05
HBAR = 1.0
INFIDELITY = 1e-6
AMPLITUDE_BUDGET = 1e-3  # ||dpsi|| <= 1e-3 => infidelity ~ ||dpsi||^2 <= 1e-6

PUBLISHED = {
    "sum_tau_hbar_over_Delta": 3172.829634,
    "w": 0.9856429312,
    "prep_w2_over_6": 0.16191533,
    "kept_w4_over_6": 0.15729945,
    "fresh_17_w4_over_192": 0.08356533,
    "fresh_over_kept": F(17, 32),
    "reset_attempts": 6.1761,
    "start_plus_end_controlled_H": 26,
    "start_plus_end_time": 6345.659268,
    "deltaH_plus_deltaE0_over_Delta": 7.88e-8,
}


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise ValueError(name)
    CHECKS.append({"name": name, "kind": kind})


def _py(x):
    if isinstance(x, (np.floating, np.integer)):
        return x.item()
    if isinstance(x, F):
        return str(x)
    return x


# --------------------------------------------------------------------------- primitives (frozen)
def clock_matrix():
    """Naked 3-cycle C: 0->1->2->0, idle 3. C^3 = I."""
    return np.array([[0, 0, 1, 0],
                     [1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1]], dtype=float)


def load_source():
    need(hashlib.sha256(CORE.read_bytes()).hexdigest() == CORE_PIN, "context source adapter pin")
    spec = importlib.util.spec_from_file_location("f1_context_source", CORE)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    src = core.source_prefix()
    by_label = {}
    for k in src["line_reps"]:
        z = np.array([complex(a, b) for a, b in src["Z240"][k]]) / 2.0
        need(abs(np.vdot(z, z) - 1) < 1e-14, "source ray unit")
        by_label.setdefault(src["root_label"][src["ROOTS"][k]], []).append(z)
    labels = sorted(by_label)
    need(len(labels) == 15 and all(len(by_label[l]) == 4 for l in labels), "15 contexts times 4 rays")
    bases = []
    for lab in labels:
        V = np.array(by_label[lab]).T
        need(np.allclose(V.conj().T @ V, np.eye(4)), "context basis orthonormal")
        bases.append(V)

    def pairing(x, y):
        v = src["hermC"](src["chart"](x), src["chart"](y))
        need(all(int(z) % 2 == 0 for z in v), "source pairing even")
        return (int(v[0]) // 2 + int(v[1]) // 2) % 2

    B = np.array([[int(pairing(src["REPS"][x], src["REPS"][y]) == 0) for y in labels]
                  for x in labels], dtype=int)
    rays = [p for V in bases for p in V.T]
    Cinc = np.zeros((15, 60), dtype=int)
    for i in range(15):
        Cinc[i, 4 * i:4 * i + 4] = 1
    paulis = [np.array(core.cmatrix(p), dtype=complex)
              for v, p in sorted(src["PMAT"].items()) if any(v)]
    Fmat = np.array([[np.trace(a @ np.outer(r, r.conj())).real for r in rays] for a in paulis])
    return {"B": B, "Cinc": Cinc, "F": Fmat, "bases": bases, "src": src,
            "paulis": paulis, "inherited": core.CHECKS}


def primitive_K(src):
    """Context choice K = B/7. Frozen, not re-derived from P1/P2."""
    B = src["B"].astype(float)
    K = B / 7.0
    need(np.allclose(K.sum(axis=1), 1), "K is stochastic")
    need(int(round(np.trace(B))) == 15 and np.array_equal(B, B.T), "B symmetric with unit diagonal")
    need(set(int(x) for x in B.sum(axis=1)) == {7}, "each context has seven allowed successors")
    a, b, c = sp.symbols("a b c", real=True)
    sol = sp.solve([a + b + c - 1, c, a - b / 6], [a, b, c], dict=True)
    need(sol == [{a: sp.Rational(1, 7), b: sp.Rational(6, 7), c: sp.Integer(0)}],
         "locality plus hidden erasure selects (1/7, 6/7, 0)")
    K_sel = (float(sol[0][a]) * np.eye(15)
             + float(sol[0][b]) * (B - np.eye(15)) / 6
             + float(sol[0][c]) * (np.ones((15, 15)) - B) / 8)
    need(np.allclose(K_sel, K), "selected policy is exactly B/7")
    for name, pt in (("locality alone", (0.5, 0.5, 0.0)),
                     ("hidden erasure alone", (1 / 14, 3 / 7, 0.5))):
        K_alt = pt[0] * np.eye(15) + pt[1] * (B - np.eye(15)) / 6 + pt[2] * (np.ones((15, 15)) - B) / 8
        need(not np.allclose(K_alt, K), name + " does not select B/7")
    aa = sp.symbols("aa", positive=True)
    H = -aa * sp.log(aa) - (1 - aa) * sp.log((1 - aa) / 6)
    need(sp.solve(sp.diff(H, aa), aa) == [sp.Rational(1, 7)],
         "max entropy of seven transitions selects 1/7")
    # 60-ray kernel T = C^t K C / 4 + (3/7) Pf. One row is 1/7 + 12*(1/14) + 47 zeros.
    Cinc, Fmat = src["Cinc"].astype(float), src["F"]
    Pc = Cinc.T @ Cinc / 4.0
    Pf = Fmat.T @ Fmat / 12.0
    T = Cinc.T @ K @ Cinc / 4.0 + (3 / 7) * Pf
    row = T[0]
    n_17 = int(np.sum(np.abs(row - 1 / 7) < 1e-12))
    n_114 = int(np.sum(np.abs(row - 1 / 14) < 1e-12))
    n_0 = int(np.sum(np.abs(row) < 1e-12))
    need((n_17, n_114, n_0) == (1, 12, 47), "T-row is 1/7 + 12/14 + 47 zeros")
    need(abs(row.sum() - 1) < 1e-12, "T-row stochastic")
    return {"definition": "K = B/7 on 15 contexts; T = C^t K C/4 + (3/7) Pf on 60 rays",
            "selected_point": {"a": "1/7", "b": "6/7", "c": "0"},
            "T_row_weights": {"1/7": 1, "1/14": 12, "0": 47},
            "source_derived": False,
            "cost": {"time": 0, "gates": 0, "bits": 0, "attempts": 1,
                     "note": "classical context kernel; one application, no quantum pulse"}}


def primitive_Q_U(src):
    """Q_C coupling and U_C pre-measurement on all 15 pinned contexts."""
    eye = np.eye(4)
    ket = [eye[:, j:j + 1] for j in range(4)]
    w = np.ones((4, 4)) / 2 - eye
    prep = (eye - 2 * ket[0] @ ket[0].T) @ w
    need(np.allclose(prep @ ket[0], np.ones((4, 1)) / 2), "A|0> = |+>")
    S = np.zeros((16, 16))
    for a, b in product(range(4), repeat=2):
        S[4 * a + b, 4 * b + a] = 1
    P_lam = (np.eye(16) - S) / 2
    Q_ptr = np.eye(16) - 2 * sum(np.kron(k @ k.T, k @ k.T) for k in ket)
    ev = np.linalg.eigvalsh(Q_ptr)
    need(sorted(int(round(e)) for e in ev) == [-1] * 4 + [1] * 12, "Q spectrum (-1)^4 (+1)^12")
    n_U2 = n_action = n_same_triv = n_src_triv = 0
    for V in src["bases"]:
        proj = [V[:, j:j + 1] @ V[:, j:j + 1].conj().T for j in range(4)]
        Q_C = np.eye(16) - 2 * sum(np.kron(ket[j] @ ket[j].T, proj[j]) for j in range(4))
        Q_same = np.kron(V, V) @ Q_ptr @ np.kron(V, V).conj().T
        need(np.allclose(Q_C, np.kron(eye, V) @ Q_ptr @ np.kron(eye, V).conj().T),
             "Q_C = (I x V_C) Q (I x V_C)^+")
        U_C = np.kron(w, eye) @ Q_C @ np.kron(prep, eye)
        if np.allclose(U_C @ U_C, np.eye(16)):
            n_U2 += 1
        ok_action = True
        for psi in list(eye.T) + [np.ones(4) / 2]:
            psi = np.asarray(psi).reshape(4, 1)
            out = U_C @ np.kron(ket[0], psi)
            ideal = sum(np.kron(ket[j], proj[j] @ psi) for j in range(4))
            if not np.allclose(out, ideal):
                ok_action = False
        if ok_action:
            n_action += 1
        if np.allclose(Q_same @ P_lam, P_lam):
            n_same_triv += 1
        if np.allclose(Q_C @ P_lam, P_lam):
            n_src_triv += 1
    need(n_U2 == 15, "U_C^2 = I on all 15 contexts")
    need(n_action == 15, "U_C(|0> x psi) = sum_j |j> x Pi_j psi on all 15 contexts")
    need(n_same_triv == 15, "same-context Q is identity on Lambda^2")
    need(n_src_triv == 1, "source-pointer Q is Lambda^2-trivial only in the computational context")
    return {
        "Q_C": {"definition": "I - 2 sum_j |j><j| ⊗ |b_j><b_j|",
                "spectrum": {"-1": 4, "+1": 12},
                "cost": {"time": 0, "gates": 4, "bits": 0, "attempts": 1,
                         "note": "four controlled reflections; 4-level register in pointer basis"}},
        "U_C": {"definition": "(W ⊗ I) Q_C (A ⊗ I), A|0>=|+>, W = H^{⊗2} minus |0> phase",
                "U_squared": "I",
                "contexts": 15,
                "cost": {"time": 0, "gates": 6, "bits": 0, "attempts": 1,
                         "note": "A + Q_C + W; one 4-level register, no extra time pulse"}},
    }


def primitive_C(src):
    C = clock_matrix()
    eye = np.eye(4)
    need(np.array_equal(C @ C @ C, eye) and not np.array_equal(C, eye), "C^3 = I, C != I")
    need(np.array_equal(C @ np.array([1, 0, 0, 0]), np.array([0, 1, 0, 0])), "C|0>=|1>")
    need(np.array_equal(C @ np.array([0, 0, 0, 1]), np.array([0, 0, 0, 1])), "C|3>=|3>")
    roots = [np.array([complex(a, b) for a, b in z]) for z in src["src"]["Z240"]]
    rootset = {tuple(np.round(z, 12)) for z in roots}
    need(all(tuple(np.round(C @ z, 12)) in rootset for z in roots),
         "naked tick C preserves all 240 phase-marked source roots")
    rays = []
    for V in src["bases"]:
        for j in range(4):
            rays.append(np.outer(V[:, j], V[:, j].conj()))
    need(all(any(np.allclose(C @ p @ C.T, q) for q in rays) for p in rays),
         "naked tick C preserves all 60 source projectors")
    return {"definition": "C: 0->1->2->0, 3->3; permutation of the computational 4-level",
            "order": 3,
            "idle_state": 3,
            "cost": {"time": 1, "gates": 1, "bits": 0, "attempts": 1,
                     "note": "one naked 3-cycle tick; time in clock steps, not ħ/Δ"}}


def wedge():
    W = np.zeros((6, 16))
    for k, (a, b) in enumerate(combinations(range(4), 2)):
        W[k, 4 * a + b] = 1 / sqrt(2)
        W[k, 4 * b + a] = -1 / sqrt(2)
    return W


def primitive_record():
    """Resonant Ures and occupation query Q. Quarter phases only for U0."""
    W = wedge()
    Pm = W.T @ W
    Pp = np.eye(16) - Pm
    Ures = np.block([[Pp, -1j * W.T], [-1j * W, np.zeros((6, 6))]])
    U0 = np.block([[Pp, W.T], [W, np.zeros((6, 6))]])
    need(np.linalg.norm(U0 @ U0 - np.eye(22)) < 1e-13, "U0 is an involution")
    need(np.linalg.norm(Ures @ Ures - np.eye(22)) > 0.5, "Ures is not an involution")
    need(np.linalg.norm(Ures.conj().T @ Ures - np.eye(22)) < 1e-13, "Ures is unitary")
    X = np.array([[0.0, 1.0], [1.0, 0.0]])
    Q = np.zeros((44, 44))
    Q[:32, :32] = np.eye(32)
    Q[32:, 32:] = np.kron(np.eye(6), X)
    R = np.kron(Pp, np.eye(2)) + np.kron(Pm, X)
    macro = np.kron(Ures.conj().T, np.eye(2)) @ Q @ np.kron(Ures, np.eye(2))
    target = np.zeros((44, 44))
    target[:32, :32] = R
    target[32:, 32:] = np.eye(12)
    need(np.linalg.norm(macro - target) < 1e-13,
         "Ures^dagger Q Ures = R ⊕ I on the local 44D sector")
    macro0 = np.kron(U0, np.eye(2)) @ Q @ np.kron(U0, np.eye(2))
    need(np.linalg.norm(macro0 - target) < 1e-13,
         "U0 Q U0 yields the same record; extra i-phases are only to make U0 an involution")
    need(np.linalg.norm(R @ R - np.eye(32)) < 1e-13, "record R is an involution on matter")
    return {
        "Ures": {"definition": "[[P_+, -i W^dagger], [-i W, 0]] on (C^4⊗C^4) ⊕ C^6",
                 "involution": False,
                 "cost": {"time": "one resonant pulse (not a free spectral projector)",
                          "gates": 1, "bits": 0, "attempts": 1,
                          "note": "physical full transfer; no extra quarter phases"}},
        "Q": {"definition": "I_16⊗I_2 ⊕ I_6⊗X  (copy mediator occupation into a bit)",
              "cost": {"time": 0, "gates": 1, "bits": 1, "attempts": 1,
                       "note": "one occupation-controlled X; 1 pointer bit"}},
        "record_identity": "Ures^dagger Q Ures = (P_+⊗I + P_-⊗X) ⊕ I_12",
        "quarter_phases_needed_for_record": False,
        "quarter_phases_needed_for_U0_involution": True,
    }


def primitive_hadamard_and_evolution():
    """controlled-exp(-i τ H/ħ) and the Hadamard test that yields A = (I+U)/2."""
    # Two-level witness: H = σz, τ = π ħ, U = -I on the excited state, +I on ground.
    Hz = np.diag([0.0, 1.0])
    tau = pi * HBAR
    U = np.diag(np.exp(-1j * tau * np.diag(Hz) / HBAR))
    need(np.allclose(U, np.diag([1.0, -1.0])), "controlled-exp witness: U=diag(1,-1)")
    A = 0.5 * (np.eye(2) + U)
    need(np.allclose(A, np.diag([1.0, 0.0])), "Hadamard accept implements (I+U)/2")
    # Explicit 4×4 Hadamard-test circuit on ancilla ⊗ system.
    Hgate = np.array([[1, 1], [1, -1]], dtype=complex) / sqrt(2)
    cU = np.block([[np.eye(2), np.zeros((2, 2))], [np.zeros((2, 2)), U]])
    circ = np.kron(Hgate, np.eye(2)) @ cU @ np.kron(Hgate, np.eye(2))
    # Space is ancilla ⊗ system; ancilla=0 is the leading 2×2 block.
    accept = circ[:2, :2]
    need(np.allclose(accept, A), "Hadamard-test accept block is (I+U)/2")
    return {
        "controlled_exp": {
            "definition": "|0><0|⊗I + |1><1|⊗exp(-i τ H/ħ)",
            "cost": {"time": "τ", "gates": 1, "bits": 1, "attempts": 1,
                     "note": "one controlled evolution; control bit not consumed"},
        },
        "Hadamard_test": {
            "definition": "H; controlled-U; H; measure; accept 0 ⇒ Kraus (I+U)/2",
            "cost": {"time": "τ + 2 H", "gates": 3, "bits": 1, "attempts": 1,
                     "note": "1 measured ancilla bit consumed per factor"},
        },
    }


def primitive_measure_reset_bits():
    eye = np.eye(4)
    for target in range(4):
        kraus = []
        for outcome in range(4):
            flip = np.zeros((4, 4))
            for j in range(4):
                flip[j ^ (target ^ outcome), j] = 1
            k = flip @ np.outer(eye[:, outcome], eye[:, outcome])
            need(np.allclose(k, np.outer(eye[:, target], eye[:, outcome])),
                 "reset Kraus |a><x| target=%d outcome=%d" % (target, outcome))
            kraus.append(k)
        need(np.allclose(sum(k.T @ k for k in kraus), eye),
             "reset is trace-preserving target=%d" % target)
    return {
        "measure_reset": {
            "definition": "M_x = X_(a xor x) |x><x| = |a><x|; sum_x M_x^dagger M_x = I",
            "cost": {"time": 0, "gates": 2, "bits": 2, "attempts": 1,
                     "note": "one 4-level measure (2 classical bits) + one source Pauli"},
        },
        "fresh_bit": {
            "definition": "prepare |0> on a qubit or 4-level register",
            "cost": {"time": 0, "gates": 1, "bits": 1, "attempts": 1,
                     "note": "one initialized unused bit"},
        },
        "measured_bit": {
            "definition": "computational-basis measure and keep the classical outcome",
            "cost": {"time": 0, "gates": 1, "bits": 1, "attempts": 1,
                     "note": "qubit: 1 bit; 4-level: 2 bits. Filter uses 13 qubit bits"},
        },
    }


def frozen_primitive_table(src):
    K = primitive_K(src)
    QU = primitive_Q_U(src)
    C = primitive_C(src)
    rec = primitive_record()
    hu = primitive_hadamard_and_evolution()
    mr = primitive_measure_reset_bits()
    table = [
        {"id": "K_B7", "name": "Kontextwahl K=B/7", **K, "resource": True},
        {"id": "Q_C", "name": "Q_C-Kopplung", **QU["Q_C"], "resource": True},
        {"id": "U_C", "name": "U_C-Vormessung", **QU["U_C"], "resource": True},
        {"id": "C", "name": "nackte Ticks C (3-Zykel)", **C, "resource": True},
        {"id": "Ures", "name": "resonanter Record Ures", **rec["Ures"], "resource": True},
        {"id": "Q", "name": "Belegungsabfrage Q", **rec["Q"], "resource": True},
        {"id": "c_exp", "name": "controlled-exp(-i τ H/ħ)", **hu["controlled_exp"], "resource": True},
        {"id": "Hadamard", "name": "Hadamard-Test", **hu["Hadamard_test"], "resource": True},
        {"id": "measure_reset", "name": "Messung+Reset", **mr["measure_reset"], "resource": True},
        {"id": "fresh_measured_bits", "name": "frische/gemessene Bits",
         "definition": "fresh |0> or measured classical bits as in measure_reset / measured_bit",
         "cost": mr["fresh_bit"]["cost"], "resource": True},
    ]
    ids = [p["id"] for p in table]
    need(ids == ["K_B7", "Q_C", "U_C", "C", "Ures", "Q", "c_exp", "Hadamard",
                 "measure_reset", "fresh_measured_bits"], "frozen primitive id list")
    forbidden = {"P0", "P_Omega", "P0_dressed", "Omega", "target_projector"}
    need(forbidden.isdisjoint(ids), "no hidden target projector in the primitive list")
    need(all(p["resource"] for p in table), "every listed handle is a declared resource")
    return {"primitives": table, "Q_U": QU, "record": rec, "K": K, "C": C,
            "hadamard": hu, "measure_reset": mr,
            "forbidden_as_primitives": sorted(forbidden)}


# --------------------------------------------------------------------------- (a) 544D star filter
def analytic_spectrum(delta=DELTA, t=T_HOP):
    gvals = np.arange(0.0, 3.5, 0.5)
    mult_low = np.array([1, 30, 45, 40, 15, 90, 35])
    low = (delta - np.sqrt(delta ** 2 + 4 * t * t * (6 - 2 * gvals))) / 2
    upper = delta - low[:-1]
    energies = np.r_[low, upper, delta]
    deg = np.r_[mult_low, mult_low[:-1], 67]
    need(int(sum(deg)) == 544, "full dressed star is 544-dimensional")
    need(len(energies) == 14, "fourteen distinct star energies")
    return energies, deg


def star_hamiltonian(delta=DELTA, t=T_HOP):
    basis = list(product(range(4), repeat=4))
    G = np.zeros((256, 256))
    for j in (1, 2, 3):
        S = np.zeros((256, 256))
        powers = 4 ** np.arange(3, -1, -1)
        for k, w in enumerate(product(range(4), repeat=4)):
            v = list(w)
            v[0], v[j] = v[j], v[0]
            S[int(np.dot(v, powers)), k] = 1
        G += (np.eye(256) + S) / 2
    med_index = {}
    M = np.zeros((288, 256))
    for col, m in enumerate(basis):
        for j in (1, 2, 3):
            a, b = m[0], m[j]
            if a == b:
                continue
            mm = list(m)
            mm[0] = mm[j] = -1
            key = (j, tuple(mm), min(a, b), max(a, b))
            row = med_index.setdefault(key, len(med_index))
            M[row, col] = 1 if a < b else -1
    need(len(med_index) == 288, "full microscopic star mediator dimension")
    need(np.linalg.norm(M.T @ M - (6 * np.eye(256) - 2 * G)) < 1e-13,
         "actual microscopic coupling Gram")
    Hmic = np.block([[np.zeros((256, 256)), t * M.T],
                     [t * M, delta * np.eye(288)]])
    return Hmic, G


def omega_vector():
    om = np.zeros(256)
    for p in permutations(range(4)):
        inv = sum(p[i] > p[j] for i, j in combinations(range(4), 2))
        om[sum(p[i] * 4 ** (3 - i) for i in range(4))] = (-1) ** inv / sqrt(24)
    return om


def chi_vector():
    chi = np.zeros(256)
    for a, b, s1 in ((0, 1, 1), (1, 0, -1)):
        for c, d, s2 in ((2, 3, 1), (3, 2, -1)):
            chi[a * 64 + b * 16 + c * 4 + d] = s1 * s2 / 2
    need(abs(np.vdot(chi, chi) - 1) < 1e-14, "chi is normalized")
    return chi


def filter_product(energies, tau, targetE):
    f = np.ones(len(energies), dtype=complex)
    for time in tau:
        f *= 0.5 * (1 + np.exp(-1j * time * (energies - targetE) / HBAR))
    return f


def star_filter(Hmic=None, allow_six_factor_as_projector=False):
    energies, deg = analytic_spectrum()
    if Hmic is None:
        Hmic, _ = star_hamiltonian()
    microvals, microvec = eigh(Hmic)
    need(max(abs(microvals - np.sort(np.repeat(energies, deg)))) < 1e-12,
         "all 544 actual microscopic eigenvalues match analytic levels")
    targetE = energies[0]
    tau = pi * HBAR / (energies[1:] - targetE)
    need(len(tau) == 13, "thirteen physical-time factors")
    f = filter_product(energies, tau, targetE)
    need(abs(f[0] - 1) < 1e-14 and max(abs(f[1:])) < 1e-12,
         "13-factor filter keeps E0 and kills the other 13 levels")
    f_full = np.ones(544, dtype=complex)
    for time in tau:
        f_full *= 0.5 * (1 + np.exp(-1j * time * (microvals - targetE) / HBAR))
    pf = (microvec * f_full) @ microvec.conj().T
    P0 = np.outer(microvec[:, 0], microvec[:, 0].conj())
    need(np.linalg.norm(pf - P0) < 1e-10,
         "full 544D product of Aj(H) equals dressed ground projector")
    short = filter_product(energies, tau[:6], targetE)
    leftover = float(max(abs(short[7:])))
    six_is_projector = leftover < 1e-5
    if allow_six_factor_as_projector:
        need(six_is_projector, "six-factor claimed as full projector")
    need(leftover > 1e-5, "lower-only six-factor filter fails on the full star")
    sum_tau = float(np.sum(tau))
    need(abs(sum_tau - PUBLISHED["sum_tau_hbar_over_Delta"]) < 5e-7,
         "published sum of thirteen times")
    return {"energies": energies.tolist(), "multiplicities": deg.tolist(),
            "times_hbar_over_Delta": [float(x) for x in tau],
            "sum_tau": sum_tau, "P0": P0, "pf": pf, "Hmic": Hmic,
            "microvec": microvec, "six_factor_max_leftover": leftover,
            "six_factor_equals_projector": six_is_projector,
            "Aj_definition": "(I + exp(-i τj (H-E0)/ħ))/2,  τj = π ħ / (Ej - E0)"}


# --------------------------------------------------------------------------- (b) bare herald and protocol
def w_exact(delta=DELTA, t=T_HOP):
    return (1 + delta / sqrt(delta ** 2 + 24 * t * t)) / 2


def swap_matrix(n, i, j):
    dim = 4 ** n
    S = np.zeros((dim, dim))
    powers = 4 ** np.arange(n - 1, -1, -1)
    for k, w in enumerate(product(range(4), repeat=n)):
        v = list(w)
        v[i], v[j] = v[j], v[i]
        S[int(np.dot(v, powers)), k] = 1
    return S


def preparation(filt, input_kind="chi"):
    if input_kind == "omega":
        raise ValueError("hidden target: Omega is not an allowed input resource")
    if input_kind != "chi":
        raise ValueError("allowed input is chi")
    w = w_exact()
    need(abs(w - PUBLISHED["w"]) < 5e-11, "w identity")
    om = omega_vector()
    chi = chi_vector()
    overlap = float(abs(np.vdot(om, chi)) ** 2)
    need(abs(overlap - 1 / 6) < 1e-14, "chi overlap with Omega is 1/6")
    A = np.outer(om, om)
    bare = filt["pf"][:256, :256]
    need(np.linalg.norm(bare - w * A) < 1e-10,
         "Pbare P0_dressed Pbare = w P_Omega")
    prep = bare @ chi
    p_prep = float(np.vdot(prep, prep).real)
    need(abs(p_prep - w * w / 6) < 1e-12, "preparation raw probability w^2/6")
    need(abs(p_prep - PUBLISHED["prep_w2_over_6"]) < 5e-9, "published preparation probability")
    C = clock_matrix()
    tick = np.kron(C, np.eye(64))
    plus = (np.eye(256) + swap_matrix(4, 0, 1)) / 2
    minus = np.eye(256) - plus
    ticked = tick @ om
    kept = float(np.linalg.norm(bare @ tick.T @ ticked) ** 2)
    fresh = float(np.linalg.norm(bare @ tick.T @ plus @ ticked) ** 2
                  + np.linalg.norm(bare @ tick.T @ minus @ ticked) ** 2)
    need(abs(kept - w * w) < 1e-12, "conditional end retained is w^2")
    need(abs(fresh - 17 * w * w / 32) < 1e-12, "conditional end fresh is 17 w^2/32")
    uncond_kept = p_prep * kept
    uncond_fresh = p_prep * fresh
    need(abs(uncond_kept - w ** 4 / 6) < 1e-12, "unconditional kept is w^4/6")
    need(abs(uncond_fresh - 17 * w ** 4 / 192) < 1e-12, "unconditional fresh is 17 w^4/192")
    need(abs(uncond_kept - PUBLISHED["kept_w4_over_6"]) < 5e-9, "published kept success")
    need(abs(uncond_fresh - PUBLISHED["fresh_17_w4_over_192"]) < 5e-9, "published fresh success")
    need(abs(uncond_fresh / uncond_kept - 17 / 32) < 1e-14, "fresh/kept quotient is 17/32")
    reset = 1 / p_prep
    need(abs(reset - PUBLISHED["reset_attempts"]) < 5e-5, "mean reset attempts 1/(w^2/6)")
    return {"w": w, "chi_overlap": overlap, "preparation": p_prep,
            "conditional_kept": kept, "conditional_fresh": fresh,
            "unconditional_kept": uncond_kept, "unconditional_fresh": uncond_fresh,
            "quotient_fresh_over_kept": 17 / 32, "reset_attempts": reset,
            "input": "two elementary pair singlets chi; not Omega, not P0"}


def protocol_costs(sum_tau, calls=None):
    if calls is None:
        calls = PUBLISHED["start_plus_end_controlled_H"]
    need(calls == 26, "start plus end use 26 controlled-H calls")
    total_time = 2 * sum_tau
    need(abs(total_time - PUBLISHED["start_plus_end_time"]) < 5e-7,
         "start plus end time 6345.659268 ħ/Δ")
    return {"controlled_H_calls_one_filter": 13,
            "controlled_H_calls_start_plus_end": calls,
            "Hadamard_tests_start_plus_end": 26,
            "measured_bits_one_filter": 13,
            "measured_bits_start_plus_end": 26,
            "occupation_heralds": 2,
            "time_one_filter": sum_tau,
            "time_start_plus_end": total_time,
            "additional": "record pulses (Ures, Q) and reset attempts on top"}


# --------------------------------------------------------------------------- (d) error budget
def error_budget(sum_tau, include_time_errors=False, include_gate_errors=False):
    # State (amplitude) error <= 4 Στj (δH+δE0)/ħ.
    # Times are in ħ/Δ, so 4 Στ (δH+δE0)/Δ. Demand amplitude <= 1e-3
    # so infidelity ~ error^2 <= 1e-6, with all other gates ideal.
    coeff = 4 * sum_tau
    bound = AMPLITUDE_BUDGET / coeff
    need(abs(bound - PUBLISHED["deltaH_plus_deltaE0_over_Delta"]) < 5e-11,
         "δH+δE0 bound 7.88e-8 Δ for infidelity 1e-6")
    need(not include_time_errors, "time errors are budgeted separately, not in 7.88e-8")
    need(not include_gate_errors, "remaining-gate errors are budgeted separately, not in 7.88e-8")
    return {"state_error_formula": "4 Στj (δH+δE0)/ħ",
            "sum_tau": sum_tau,
            "coefficient": coeff,
            "amplitude_budget": AMPLITUDE_BUDGET,
            "infidelity_target": INFIDELITY,
            "deltaH_plus_deltaE0_over_Delta": bound,
            "published_deltaH_plus_deltaE0_over_Delta": PUBLISHED["deltaH_plus_deltaE0_over_Delta"],
            "remaining_gates_assumed_ideal": True,
            "time_errors_included": False,
            "other_gate_errors_included": False,
            "time_error_note": "phase error Σ |δτj| (Ej-E0)/ħ is a separate budget",
            "gate_error_note": "H, Q, Ures, measure, reset errors are a separate budget"}


def run():
    CHECKS.clear()
    src = load_source()
    prim = frozen_primitive_table(src)
    filt = star_filter()
    prep = preparation(filt, input_kind="chi")
    costs = protocol_costs(filt["sum_tau"])
    err = error_budget(filt["sum_tau"])
    report = {
        "status": "PASS",
        "verdict": "consistent",
        "scope": ("lab steps reduce onto a frozen primitive list with explicit "
                  "costs; primitives themselves are not derived from P1/P2"),
        "checks": len(CHECKS),
        "inherited_source_prefix_checks": src["inherited"],
        "T1_T8_closed": [],
        "hidden_target_projector_used_as_resource": False,
        "allowed_input": "chi (two singlets, overlap 1/6)",
        "primitives": [{k: v for k, v in p.items() if k != "cost"} | {"cost": p["cost"]}
                       for p in prim["primitives"]],
        "K_B7": prim["K"],
        "Q_C_U_C": {k: v for k, v in prim["Q_U"].items()},
        "clock": prim["C"],
        "record": {k: v for k, v in prim["record"].items() if k != "Ures"} | {
            "Ures": {kk: vv for kk, vv in prim["record"]["Ures"].items() if kk != "definition"}
            | {"definition": prim["record"]["Ures"]["definition"]}
        },
        "star_filter": {
            "Aj_definition": filt["Aj_definition"],
            "n_factors": 13,
            "dimension": 544,
            "sum_tau_hbar_over_Delta": filt["sum_tau"],
            "published_sum_tau": PUBLISHED["sum_tau_hbar_over_Delta"],
            "six_factor_max_leftover": filt["six_factor_max_leftover"],
            "six_factor_equals_projector": filt["six_factor_equals_projector"],
            "equals_P0_dressed": True,
        },
        "preparation": {
            "w": prep["w"],
            "chi_overlap": prep["chi_overlap"],
            "preparation_probability": prep["preparation"],
            "conditional_kept": prep["conditional_kept"],
            "conditional_fresh": prep["conditional_fresh"],
            "unconditional_kept": prep["unconditional_kept"],
            "unconditional_fresh": prep["unconditional_fresh"],
            "quotient_fresh_over_kept": "17/32",
            "reset_attempts": prep["reset_attempts"],
            "input": prep["input"],
        },
        "protocol_costs": costs,
        "error_budget": err,
        "published": {k: (str(v) if isinstance(v, F) else v) for k, v in PUBLISHED.items()},
        "native_controls_derived": False,
        "finite_gate_synthesis_claimed": False,
    }
    return report


def jsonable(obj):
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    if isinstance(obj, (np.ndarray,)):
        return obj.tolist()
    if isinstance(obj, (np.floating, np.integer)):
        return obj.item()
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, complex):
        return {"re": obj.real, "im": obj.imag}
    return obj


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    report = jsonable(run())
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if argv:
        Path(argv[0]).write_text(text)
    print(text)
    return report


if __name__ == "__main__":
    main()
