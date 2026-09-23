"""Universalraum-Inversion: Hypothesenpruefung und Rekonstruktionsversuch (exakt, NON-RH).

Gepruefte Hypothese (Nutzer, 14.09.2026): Der Universalraum ist das System der
miteinander verbundenen Veränderungen; TFPT ist eine strukturierte Auslesung
davon, nicht das Fundament. Der Pruefer testet diese Umkehrung an den
tatsaechlichen gepinnten Quellobjekten (60 Strahlen / 15 Kontexte aus v783,
Registerausfuehrung, Viertraegerzelle) und versucht die Rekonstruktion:

  1. readout_anchors: CT=KC und ET=D E gelten; die 30 unsichtbaren Richtungen
     werden von T ausgeloescht (kein Gedaechtnis im Nullraum).
  2. no_autonomous_shadow: auf dem reinen Systemschatten existiert KEINE
     autonome Regel D mit P(Phi(X)) = D(P(X)) fuer alle erlaubten
     Fortsetzungen (Zeugenpaar mit gleichem Schatten, verschiedener
     Fortsetzung). Fuer die frische Unterausfuehrung existiert dagegen die
     Dephasierungsregel.
  3. minimal_envelope: Systemschatten + Kontextmarginalie ohne Korrelation
     reichen nicht; der volle CQ-Zustand ist die minimale autonome Huelle.
  4. context_rule_selection: Lokalitaet (c=0) + kein persistentes
     Unsichtbares (mu=0) waehlen eindeutig (1/7, 6/7, 0) = B/7; jede
     Bedingung allein laesst eine Familie. Prinzipien gesetzt, nicht
     quellenabgeleitet.
  5. closed_finite_no_exact_decay: die reduzierte Regel daempft exakt mit
     (3/7)^n; die kohärente geschlossene Ausfuehrung oszilliert (Periode 2).
     Kein geschlossenes endliches unitaeres System erzeugt exaktes Abklingen
     fuer alle n (Beweis in PROOF.md, Instanzen hier maschinell).
  6. relational_time_probe: kollektive Lifte aendern Omega nur um det(A);
     die vier bedingten Zustaende bei Traeger-0-Lesart sind rein und
     paarweise orthogonal (unterscheidbare Lesarten), aber H_tet laesst Omega
     stationaer und erhaelt die Uhrenanzeige nicht (keine PW-Uhr ausgewaehlt).
  7. subsystem_factorization_probe: Paarmarginalien-Rangprofil (6^6) und
     Zweiokoerperlichkeit der Swaps unterscheiden die Traegerfaktorisierung
     von getesteten Qubit-Umgruppierungen. Keine Allgemeinheit.

Ausfuehrung: python3 -B checker.py [validation.json]
Keine T1-T8-Schliessung, keine Promotion, keine RH-Aussage.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CORE = HERE.parent / "compiler-origin-audit-20260913" / "context_instrument.py"
PINS = {"context_instrument.py": "ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995"}
CHECKS: list[str] = []


def check(ok, name):
    if not ok:
        raise ValueError(name)
    CHECKS.append(name)


def spectrum_integer(matrix, eigenvalues):
    """Exakter Annihilator + exakte Spurmomente (symmetrische ganzzahlige Matrix)."""
    n = len(matrix)
    eye = np.eye(n, dtype=np.int64)
    check(np.array_equal(matrix, matrix.T), "spectrum requires real symmetry")
    product = eye.copy()
    for e in eigenvalues:
        product = product @ (matrix - e * eye)
    check(not np.any(product), "exact spectral annihilator")
    power = eye.copy()
    moments = []
    for _ in eigenvalues:
        moments.append(int(np.trace(power)))
        power = power @ matrix
    vand = sp.Matrix([[sp.Integer(e) ** k for e in eigenvalues] for k in range(len(eigenvalues))])
    multiplicities = vand.inv() * sp.Matrix(moments)
    check(all(x.is_Integer and x >= 0 for x in multiplicities), "nonnegative integer multiplicities")
    check(sum(multiplicities) == n, "spectral dimension")
    return {str(e): int(m) for e, m in zip(eigenvalues, multiplicities)}


def source_data():
    """Hash-gepinnte tatsaechliche Quellobjekte: 15 Kontexte, 60 Strahlen, B, C, F."""
    check(hashlib.sha256(CORE.read_bytes()).hexdigest() == PINS["context_instrument.py"],
          "source pin")
    spec = importlib.util.spec_from_file_location("inversion_source_core", CORE)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    d = core.source_prefix()
    by_label = {}
    for k in d["line_reps"]:
        z = sp.Matrix([a + sp.I * b for a, b in d["Z240"][k]])
        projector = (z * z.H / 4).applyfunc(sp.expand)
        label = d["root_label"][d["ROOTS"][k]]
        by_label.setdefault(label, []).append(projector)
    labels = sorted(by_label)
    bases = [by_label[k] for k in labels]
    check(len(bases) == 15 and all(len(b) == 4 for b in bases), "actual fifteen by four source rays")
    paulis = [core.cmatrix(p) for v, p in sorted(d["PMAT"].items()) if any(v)]

    def pairing(x, y):
        v = d["hermC"](d["chart"](x), d["chart"](y))
        check(all(z % 2 == 0 for z in v), "source pairing divisible by two")
        return (v[0] // 2 + v[1] // 2) % 2

    B = sp.Matrix([[int(pairing(d["REPS"][x], d["REPS"][y]) == 0) for y in labels] for x in labels])
    rays = [p for b in bases for p in b]
    C = sp.Matrix(15, 60, lambda i, j: int(j // 4 == i))
    F = sp.Matrix([[sp.trace(a * p).expand() for p in rays] for a in paulis])
    gram = sp.Matrix([[sp.trace(p * q).expand() for q in rays] for p in rays])
    return {"B": B, "C": C, "F": F, "gram": gram, "bases": bases, "paulis": paulis,
            "inherited": core.CHECKS}


def readout_anchors(d):
    """H1-H3 der Hypothese: Schattenidentitaeten gelten; Unsichtbar != verborgenes Gedaechtnis."""
    B, C, F, G = d["B"], d["C"], d["F"], d["gram"]
    check(C * C.T == 4 * sp.eye(15), "CCt equals four identity")
    check(F * F.T == 12 * sp.eye(15), "FFt equals twelve identity")
    check(C * F.T == sp.zeros(15), "context and Pauli sectors orthogonal")
    T = sp.Matrix(60, 60, lambda i, j: B[i // 4, j // 4] * G[i, j] / 7)
    check(T == (C.T * B * C + F.T * F) / 28, "source transition factorization")
    Pc, Pf = C.T * C / 4, F.T * F / 12
    Ph = sp.eye(60) - Pc - Pf
    check(sp.trace(Ph) == 30 and T * Ph == sp.zeros(60), "thirty invisible directions annihilated by T")
    spec = spectrum_integer(np.array(14 * T, dtype=np.int64), [0, 2, -4, 4, 6, 14])
    check(spec == {"0": 30, "2": 0, "-4": 5, "4": 9, "6": 15, "14": 1}, "full source T spectrum")
    # ker T = im Ph = ker(C,F): Nullraum ist genau der fuer beide Auslesungen
    # unsichtbare Raum; er lebt innerhalb von T NICHT weiter (H3).
    check(B * B == 4 * sp.eye(15) + 3 * sp.ones(15), "B invertible by source identity")
    K = B / 7
    check(C * T == K * C, "classical shadow intertwines: C T = K C")
    decode = sp.Matrix.hstack(*(p.reshape(16, 1) for p in [p for b in d["bases"] for p in b]))
    identity_vec = sp.eye(4).reshape(16, 1)
    depol = 3 * sp.eye(16) / 7 + identity_vec * identity_vec.T / 7
    check(decode * T == depol * decode, "quantum shadow intertwines: E T = D E with factor 3/7")
    for n in (1, 2, 3):
        check(T ** n == C.T * K ** n * C / 4 + sp.Rational(3, 7) ** n * Pf,
              "closed all-n shadow formula witnesses")
    return {"T_spectrum": {"1": 1, "3/7": 15, "2/7": 9, "-2/7": 5, "0": 30},
            "invisible_directions_are_annihilated_not_stored": True,
            "shadow_identities": ["C T = K C", "E T = D E, D(rho) = (3/7) rho + (4/7) I4/4"],
            "depol": depol}


def _pointer_basis_index(bases):
    eye = sp.eye(4)
    pointer = [eye[:, j] * eye[:, j].T for j in range(4)]
    for k, b in enumerate(bases):
        if all(any(p == q for q in b) for p in pointer):
            return k, pointer
    raise ValueError("computational context not among source contexts")


def _measurement_unitary(basis):
    """Quell-Vormessung wie in record_composition.py: W = J4/2 - I, A = (I-2|0><0|) W."""
    eye = sp.eye(4)
    ket0 = eye[:, 0]
    W = sp.ones(4) / 2 - eye
    prep = (eye - 2 * ket0 * ket0.T) * W
    coupling = sp.eye(16) - 2 * sum((sp.kronecker_product(sp.eye(4)[:, j] * sp.eye(4)[:, j].T, basis[j])
                                     for j in range(4)), sp.zeros(16))
    U = sp.kronecker_product(W, eye) * coupling * sp.kronecker_product(prep, eye)
    return U.applyfunc(sp.expand)


def _partial_trace_record(rho):
    return sum((rho[4 * r:4 * r + 4, 4 * r:4 * r + 4] for r in range(4)), sp.zeros(4))


def no_autonomous_shadow(d, continuation="coherent"):
    """Zentraler Test der Hypothese: P(X1)=P(X2), aber P(Phi X1) != P(Phi X2)."""
    idx, pointer = _pointer_basis_index(d["bases"])
    U = _measurement_unitary(pointer)
    check(U.H * U == sp.eye(16) and U * U == sp.eye(16), "source premeasurement is unitary involution")
    eye4 = sp.eye(4)
    ket0 = eye4[:, 0]
    plus = sp.ones(4, 1) / 2
    initial = sp.kronecker_product(ket0, plus)
    X1 = (U * initial) * (U * initial).H
    shadow1 = _partial_trace_record(X1)
    check(shadow1 == eye4 / 4, "after one step system shadow is maximally mixed")
    dephased_plus = sum((p * (plus * plus.T) * p for p in pointer), sp.zeros(4))
    check(dephased_plus == eye4 / 4, "dephased uniform state equals I4/4 in this source context")
    X2 = sp.kronecker_product(ket0 * ket0.T, dephased_plus)
    shadow2 = _partial_trace_record(X2)
    check(shadow1 == shadow2, "witnesses share the same system shadow")
    if continuation == "coherent":
        out1 = _partial_trace_record((U * X1 * U.H).applyfunc(sp.expand))
        out2 = _partial_trace_record((U * X2 * U.H).applyfunc(sp.expand))
        check(out1 == plus * plus.T, "coherent continuation restores the pure state")
        check(out2 == eye4 / 4, "coherent continuation of dephased witness stays mixed")
        check(out1 != out2, "WITNESS: same shadow, different allowed continuation")
        return {"autonomous_rule_for_all_allowed_continuations": False,
                "witness_shadow": "I4/4", "continuation": "U (retained coherent record)",
                "P_Phi_X1": "|+><+| (purity 1)", "P_Phi_X2": "I4/4 (purity 1/4)"}
    if continuation == "fresh":
        fresh = lambda sigma: sum((p * sigma * p for p in pointer), sp.zeros(4))
        check(fresh(shadow1) == fresh(shadow2) == eye4 / 4,
              "negative control: fresh-record continuation cannot separate the witnesses")
        return {"continuation": "fresh record", "separates_witnesses": False,
                "autonomous_rule_for_this_subprocess": "dephasing Delta (exists)"}
    raise ValueError("unknown continuation")


def minimal_envelope(d):
    """System- + Kontextmarginalie ohne Korrelation bestimmen die Fortsetzung nicht."""
    B, bases = d["B"], d["bases"]
    K = B / 7
    c0 = 0
    c1 = next(j for j in range(15) if B[c0, j] == 0)
    p, q = bases[c0][0], bases[c1][0]
    rho = (p + q) / 2

    def cq_output(sigma):
        out = sum((K[dd, cc] * sum((pp * sigma.get(cc, sp.zeros(4)) * pp for pp in bases[dd]), sp.zeros(4))
                   for dd in range(15) for cc in range(15)), sp.zeros(4))
        return out.applyfunc(sp.expand)

    matched = {c0: p / 2, c1: q / 2}
    product = {c0: rho / 2, c1: rho / 2}
    zero = sp.zeros(4)
    for name, state in (("matched", matched), ("product", product)):
        marginal_context = {c: sp.trace(state.get(c, zero)) for c in range(15)}
        check({c: v for c, v in marginal_context.items() if v != 0} == {c0: sp.Rational(1, 2), c1: sp.Rational(1, 2)},
              name + " context marginal is one half on each of two disjoint contexts")
        check(sum(state.values(), zero) == rho, name + " system marginal equals rho")
    out_matched = cq_output(matched)
    out_product = cq_output(product)
    check(sp.trace(out_matched) == 1 and sp.trace(out_product) == 1, "CQ map trace preserving on witnesses")
    check(out_matched != out_product,
          "same marginals, different context-system correlation, different future")
    return {"disjoint_context_pair": [c0, c1],
            "system_shadow_alone_autonomous": False,
            "system_plus_context_marginals_autonomous": False,
            "minimal_autonomous_envelope_in_this_model": "full CQ state (15 x 16 real coordinates)",
            "matched_output": "sum_D (K_DC0 Delta_D(p) + K_DC1 Delta_D(q))/2",
            "product_output": "sum_D (K_DC0 + K_DC1) Delta_D((p+q)/2)/2"}


def context_rule_selection(d, policy=None):
    """Lokalitaet (c=0) und kein persistentes Unsichtbares (mu=0) waehlen (1/7,6/7,0)."""
    B, C, F = d["B"], d["C"], d["F"]
    Pc, Pf = C.T * C / 4, F.T * F / 12
    Ph = sp.eye(60) - Pc - Pf
    a, b, c = sp.symbols("a b c", real=True)
    solution = sp.solve([a + b + c - 1, c, a - b / 6], [a, b, c], dict=True)
    check(solution == [{a: sp.Rational(1, 7), b: sp.Rational(6, 7), c: sp.Integer(0)}],
          "locality plus hidden erasure selects a unique point")
    point = policy or solution[0]
    K_point = point[a] * sp.eye(15) + point[b] * (B - sp.eye(15)) / 6 + point[c] * (sp.ones(15) - B) / 8
    check(K_point == B / 7, "selected policy is exactly the source policy B/7")
    # Jede Bedingung allein laesst eine Familie (exakte Gegenpunkte):
    locality_only = {a: sp.Rational(1, 2), b: sp.Rational(1, 2), c: sp.Integer(0)}
    erasure_only = {a: sp.Rational(1, 14), b: sp.Rational(3, 7), c: sp.Rational(1, 2)}
    for name, pt in (("locality alone", locality_only), ("hidden erasure alone", erasure_only)):
        check(pt[a] + pt[b] + pt[c] == 1 and all(v >= 0 for v in pt.values()), name + " is a valid policy")
        K_alt = pt[a] * sp.eye(15) + pt[b] * (B - sp.eye(15)) / 6 + pt[c] * (sp.ones(15) - B) / 8
        check(K_alt != B / 7, name + " does not select the source policy")
    check(locality_only[a] - locality_only[b] / 6 != 0, "locality alone leaves hidden directions persistent")
    check(erasure_only[c] != 0, "hidden erasure alone allows nonlocal disjoint transitions")

    def T_abc(pt):
        K_abc = pt[a] * sp.eye(15) + pt[b] * (B - sp.eye(15)) / 6 + pt[c] * (sp.ones(15) - B) / 8
        lam = pt[a] + pt[b] / 3
        mu = pt[a] - pt[b] / 6
        return C.T * K_abc * C / 4 + lam * Pf + mu * Ph, mu

    T_src, mu_src = T_abc({a: sp.Rational(1, 7), b: sp.Rational(6, 7), c: sp.Integer(0)})
    check(mu_src == 0 and T_src * Ph == sp.zeros(60), "at the source point invisible means annihilated")
    T_alt, mu_alt = T_abc(locality_only)
    check(mu_alt != 0 and T_alt * Ph == mu_alt * Ph and (T_alt * Ph) != sp.zeros(60),
          "away from mu=0 the invisible sector persists inside T")
    # Maximale Entropie der sieben einzelnen zulaessigen Uebergaenge (c=0):
    H = -a * sp.log(a) - (1 - a) * sp.log((1 - a) / 6)
    check(sp.solve(sp.diff(H, a), a) == [sp.Rational(1, 7)],
          "max entropy over the seven allowed transitions selects the same point")
    return {"selected_point": {"a": "1/7", "b": "6/7", "c": "0"},
            "selection_principles": ["c = 0 (support only on source-incident contexts)",
                                     "mu = a - b/6 = 0 (no invisible direction persists in T)",
                                     "equivalently: max Shannon entropy of the seven transitions"],
            "principles_source_derived": False,
            "each_condition_alone_insufficient": True}


def closed_finite_no_exact_decay(d, anchors):
    """Reduzierte Regel: exakt (3/7)^n. Geschlossene Ausfuehrung: Periode, kein Abklingen."""
    depol = anchors["depol"]
    p = d["bases"][0][0]
    contrast = (p - sp.eye(4) / 4).reshape(16, 1)
    for n in (1, 2, 3, 4):
        check(depol ** n * contrast == sp.Rational(3, 7) ** n * contrast,
              "reduced rule decays exactly by 3/7 per step")
    idx, pointer = _pointer_basis_index(d["bases"])
    U = _measurement_unitary(pointer)
    ket0 = sp.eye(4)[:, 0]
    plus = sp.ones(4, 1) / 2
    state = sp.kronecker_product(ket0, plus)
    contrasts = []
    for n in range(7):
        rho_sys = _partial_trace_record(state * state.H)
        purity = sp.trace(rho_sys * rho_sys)
        contrasts.append((4 * purity - 1) / 3)
        state = U * state
    check(contrasts == [sp.Integer(1), sp.Integer(0)] * 3 + [sp.Integer(1)],
          "closed coherent execution oscillates with period two, no decay")
    for n, value in enumerate(contrasts):
        check(value == sp.Rational(1 + (-1) ** n, 2), "contrast is the two-term phase sum 1/2 + (-1)^n/2")
    mean_square = sum(v * v for v in contrasts[:6]) / 6
    check(mean_square == sp.Rational(1, 2), "time-averaged squared contrast over full periods is one half")
    return {"reduced_rule_exact_factor_per_step": "3/7",
            "closed_execution_contrasts": [str(v) for v in contrasts],
            "closed_execution_mean_squared_contrast": "1/2",
            "exact_decay_for_all_n_in_closed_finite_unitary": False,
            "theorem": "PROOF.md P1: finite phase sums have positive Cesaro mean of |f|^2",
            "consequence": "exact (3/7)^n for all n requires open fresh-record supply or a limit process"}


def _tetramer():
    digits = list(it.product(range(4), repeat=4))
    lookup = {x: i for i, x in enumerate(digits)}
    eye = np.eye(256, dtype=np.int64)
    swaps = []
    for i, j in it.combinations(range(4), 2):
        swap = np.zeros((256, 256), dtype=np.int64)
        for col, digit in enumerate(digits):
            target = list(digit)
            target[i], target[j] = target[j], target[i]
            swap[lookup[tuple(target)], col] = 1
        swaps.append(swap)
    H2 = 6 * eye + sum(swaps)
    omega = np.zeros(256, dtype=np.int64)
    for perm in it.permutations(range(4)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        omega[lookup[perm]] = sign
    return digits, lookup, swaps, H2, omega


def relational_time_probe():
    """Page-Wootters-Sonde auf der Viertraegerzelle: Lesarten ja, Uhr dynamisch nein."""
    digits, lookup, swaps, H2, omega = _tetramer()
    spectrum = spectrum_integer(H2, [0, 4, 6, 8, 12])
    check(spectrum == {"0": 1, "4": 45, "6": 40, "8": 135, "12": 35}, "tetramer exact full spectrum")
    check(not np.any(H2 @ omega), "unique zero-energy ground vector")
    for swap in swaps:
        check(np.array_equal(swap @ omega, -omega), "antisymmetric under every carrier pair")
    # Kollektive Lifte: A^tensor4 Omega = det(A) Omega — globale Phase, kein Signal.
    A_roots = np.diag(np.array([1, 1j, -1, -1j]))
    A_perm = np.zeros((4, 4), dtype=np.int64)
    A_perm[1, 0] = A_perm[0, 1] = A_perm[2, 2] = A_perm[3, 3] = 1
    for A, det in ((A_roots, -1), (A_perm, -1)):
        collective = np.kron(np.kron(A, A), np.kron(A, A))
        image = collective @ omega
        check(np.array_equal(np.real_if_close(image), det * np.real_if_close(omega)),
              "collective lift changes Omega only by det(A) phase")
        density = np.outer(image, image.conjugate())
        check(np.allclose(density, np.outer(omega, omega)), "global density operator invariant")
    # Bedingte Zustaende: Traeger 0 als Lesart-Referenz.
    tensor = omega.reshape((4, 4, 4, 4))
    conditional = [tensor[t].reshape(-1) for t in range(4)]
    for t, psi in enumerate(conditional):
        check(int(psi @ psi) == 6, "conditional norm squared is one fourth of total")
        outer = np.outer(psi, psi)
        check(np.array_equal(outer @ outer, 6 * outer), "normalized conditional state is pure")
        support = {digits[i][1:] for i in np.flatnonzero(psi)}
        check(support == set(it.permutations([v for v in range(4) if v != t])),
              "conditional state is the antisymmetric state on the complement values")
    gram = np.array([[a @ b for b in conditional] for a in conditional])
    check(np.array_equal(gram, 6 * np.eye(4, dtype=np.int64)),
          "the four clock readings are pairwise orthogonal: perfectly distinguishable")
    # Keine relationale Dynamik aus H_tet: Omega ist stationaer, und die Kopplung
    # erhaelt die Lesart nicht (Traeger 0 ist keine PW-Uhr dieses Modells).
    projector_t = [np.diag([int(d[0] == t) for d in digits]).astype(np.int64) for t in range(4)]
    moved = projector_t[1] @ swaps[0] @ projector_t[0]
    check(bool(np.any(moved)), "swap coupling moves carrier-zero readings between sectors")
    return {"collective_signal_visible": False,
            "conditional_readings": {"count": 4, "orthogonal": True, "pure": True,
                                     "reading_probability": "1/4 each"},
            "ground_state_stationary_under_H_tet": True,
            "clock_reading_conserved_by_coupling": False,
            "page_wootters_clock_selected": False}


def subsystem_factorization_probe():
    """Umgekehrte Bausteinfrage: Traegerfaktorisierung aus Beziehungen erkennbar?"""
    digits, lookup, swaps, H2, omega = _tetramer()
    tensor = omega.reshape((4, 4, 4, 4))

    def pair_ranks(axes_tensor):
        ranks = []
        for i, j in it.combinations(range(4), 2):
            rest = [k for k in range(4) if k not in (i, j)]
            block = np.transpose(axes_tensor, [i, j] + rest).reshape(16, -1)
            reduced = block @ block.T
            ranks.append(int(sp.Matrix(reduced).rank()))
        return sorted(ranks)

    true_profile = pair_ranks(tensor)
    check(true_profile == [6] * 6, "carrier factorization: every pair marginal has rank six")
    # Alternative Faktorisierung: 8 Qubits, falsche Vierertraeger = Qubitpaare {j, j+4}.
    omega8 = omega.reshape([2] * 8)
    fake = np.transpose(omega8, [0, 4, 1, 5, 2, 6, 3, 7]).reshape((4, 4, 4, 4))
    fake_profile = pair_ranks(fake)
    check(fake_profile != [6] * 6, "tested qubit regrouping has a different relational fingerprint")
    # Zweiokoerperlichkeit: S_01 kommutiert mit allen Operatoren auf Traegern 2,3 (wahr),
    # aber in der falschen Faktorisierung beruehrt die Kopplung jeden falschen Traeger.
    dim = 256
    Z = []
    X = []
    for q in range(8):
        weight = 1 << (7 - q)
        Z.append(np.diag([1 if (n & weight) == 0 else -1 for n in range(dim)]).astype(np.int64))
        flip = np.zeros((dim, dim), dtype=np.int64)
        for n in range(dim):
            flip[n ^ weight, n] = 1
        X.append(flip)
    S01 = swaps[0]
    for q in range(4, 8):
        check(not np.any(S01 @ Z[q] - Z[q] @ S01) and not np.any(S01 @ X[q] - X[q] @ S01),
              "true factorization: swap S_01 is two-body (acts trivially on carriers 2 and 3)")
    for k in range(4):
        touched = any(np.any(S01 @ Z[q] - Z[q] @ S01) or np.any(S01 @ X[q] - X[q] @ S01)
                      for q in (k, k + 4))
        check(touched, "fake factorization: S_01 touches every regrouped carrier")
    return {"carrier_pair_marginal_rank_profile": true_profile,
            "regrouped_pair_marginal_rank_profile": fake_profile,
            "swap_two_body_in_carrier_factorization": True,
            "swap_two_body_in_regrouped_factorization": False,
            "scope": "probe over tested alternative factorizations, not a uniqueness theorem"}


def main():
    data = source_data()
    anchors = readout_anchors(data)
    result = {
        "scope": "NON-RH inversion hypothesis check and reconstruction attempt on actual source objects",
        "hypothesis_anchors": {
            "register_experiment_same_shadow_two_continuations": True,
            "thirty_invisible_directions_annihilated_not_hidden_memory": True,
            "channel_triangle_point_not_selected_by_symmetry_alone": True,
            "collective_lift_changes_omega_only_by_phase": True,
        },
        "readout_anchors": {k: v for k, v in anchors.items() if k != "depol"},
        "no_autonomous_shadow": no_autonomous_shadow(data),
        "fresh_record_negative_control": no_autonomous_shadow(data, continuation="fresh"),
        "minimal_envelope": minimal_envelope(data),
        "context_rule_selection": context_rule_selection(data),
        "closed_finite_no_exact_decay": closed_finite_no_exact_decay(data, anchors),
        "relational_time_probe": relational_time_probe(),
        "subsystem_factorization_probe": subsystem_factorization_probe(),
        "reconstruction_candidate": {
            "definition": "composable process: carriers + operations + composition + state + records + readouts",
            "source_derived": ["15 contexts / 60 rays from actual E8 roots",
                               "incidence support B (seven allowed successors)",
                               "context reflections and premeasurement unitaries"],
            "principle_selected_not_derived": ["normalization of K via c=0 and mu=0 (or max entropy)"],
            "explicitly_set_not_derived": ["tetramer Hamiltonian H_tet and coupling J",
                                           "ground state preparation Omega",
                                           "fresh-record supply and register availability",
                                           "inter-register CZ coupling between carriers",
                                           "any physical time scale or clock splitting"],
        },
        "open_gates": ["G1 context-rule principles stated, not source-derived",
                       "G2 coupling, preparation and record supply not derived",
                       "G3 relational readings distinguishable but no clock dynamics selected",
                       "G4 factorization probe scoped to tested alternatives",
                       "G5 exact irreversible decay needs open record supply or limit process"],
        "verdict": "consistent_partial",
        "T1_T8_closed": [],
    }
    result["checks"] = len(CHECKS)
    result["check_names"] = CHECKS
    result["source_sha256"] = {
        "context_instrument.py": hashlib.sha256(CORE.read_bytes()).hexdigest(),
        "checker.py": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = json.dumps(result, indent=2, sort_keys=True)
    if len(sys.argv) > 1 and sys.argv[1].endswith(".json"):
        (HERE / sys.argv[1]).write_text(output + "\n")
    print(output)
    return result


if __name__ == "__main__":
    main()
