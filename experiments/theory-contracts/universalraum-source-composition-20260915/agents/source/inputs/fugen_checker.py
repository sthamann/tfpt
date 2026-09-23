"""NON-RH. Universalraum: die fuenf gesetzten Fugen (lambda, Graph, Cross-Register-Kopplung,
Praeparation, Zeitskala) - exakte Pruefungen auf den gepinnten Quellobjekten.

F1/F2  E8-Superaustausch: Sektoren, Klammerkanaele, |N_ab| = 1, Vorzeichen von J (Sym^2(16) enthaelt die 10,
       Lambda^2(16) nicht), Traegerkern K^+K = I - S = 2 P_Lambda, Spinor-Nachbarschaftsgraph = Clebsch(16,5,0,2).
F3/F4  Sektortrennung Zelle/Aufzeichnung: Q wirkt als Identitaet auf Lambda^2, Aufzeichnungszustand in Sym^2,
       Omega ist unter gleichkontextiger Aufzeichnung invariant (alle 15 Kontexte), Registerbasis-Abhaengigkeit.
F5     240-Bijektion: Bahnen der CQ-Koordinaten (15, 45, 180) gegen Wurzeln (60 Strahlen x 4 Einheiten) - keine
       aequivariante Bijektion.
F7     Z4-Glue: E8 = D5 + D3 + zyklischer Glue, Normzaehlung pro Klasse, Stufe-1-Inhalt 60/60/64/64 = 248,
       Stufe-2 = 4124, konforme Gewichte der Klassen aus Minimalnormen.
Nichts hier bewegt T1-T8, Ledger, Papers oder Website.
"""
import hashlib
import importlib.util
import itertools
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ORIGIN = HERE.parent / 'compiler-origin-audit-20260913'
CORE_PIN = 'ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995'
CHECKS = 0
TOL = 1e-10


def require(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(label)


# ----------------------------------------------------------------------------- E8 in D8-Koordinaten
def e8_roots():
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                r = [F(0)] * 8
                r[i], r[j] = F(si), F(sj)
                roots.append(tuple(r))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(F(s, 2) for s in signs))
    return roots


def sector(r):
    """D5 auf Koordinaten 0..4, A3 = D3 auf 5..7 (wie in fable-runde3)."""
    w = r[5:]
    nz = [x for x in w if x != 0]
    if not nz:
        return '(45,1)'
    if len(nz) == 2 and all(abs(x) == 1 for x in nz):
        return '(1,15)'
    if len(nz) == 1:
        return '(10,6)'
    neg = sum(1 for x in nz if x < 0)
    return '(16,4)' if neg % 2 == 1 else '(16bar,4bar)'


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def f1_superexchange():
    roots = e8_roots()
    rset = set(roots)
    require(len(roots) == 240 and len(rset) == 240, 'E8: 240 Wurzeln')
    by = defaultdict(list)
    for r in roots:
        by[sector(r)].append(r)
    counts = {k: len(v) for k, v in by.items()}
    require(counts == {'(45,1)': 40, '(1,15)': 12, '(10,6)': 60, '(16,4)': 64, '(16bar,4bar)': 64},
            'Sektorzaehlung 40+12+60+64+64 (+8 Cartan = 248)')
    require(all(tuple(-x for x in r) in set(by['(16bar,4bar)']) for r in by['(16,4)']),
            '(16bar,4bar) = -(16,4)')

    # Klammerkanaele
    cc = Counter()
    for a in by['(16,4)']:
        for b in by['(16,4)']:
            s = add(a, b)
            if s in rset:
                cc[sector(s)] += 1
    require(dict(cc) == {'(10,6)': 960}, 'Traeger-Traeger: [(16,4),(16,4)] nur in (10,6), 960 Paare')
    ca = Counter()
    zero = tuple([F(0)] * 8)
    for a in by['(16,4)']:
        for b in by['(16bar,4bar)']:
            s = add(a, b)
            if s == zero:
                ca['Cartan'] += 1
            elif s in rset:
                ca[sector(s)] += 1
    require(dict(ca) == {'(45,1)': 640, '(1,15)': 192, 'Cartan': 64},
            'Traeger-Antitraeger: [(16,4),(16bar,4bar)] in (45,1)+(1,15)+Cartan, nie (10,6)')

    # Einfach geschnuert: fuer alle Paare mit a+b Wurzel ist <a,b> = -1 und b-a keine Wurzel  =>  N_ab^2 = 1.
    npairs = 0
    for a in roots:
        for b in roots:
            if add(a, b) in rset:
                npairs += 1
                require(dot(a, b) == -1, 'einfach geschnuert: <a,b> = -1')
                require(tuple(x - y for x, y in zip(b, a)) not in rset, 'a-Kette durch b hat Laenge 2')
    require(npairs == 240 * 56, 'jede Wurzel hat 56 Partner mit Wurzelsumme')

    # Spinor-Nachbarschaftsgraph: Orte = 16 D5-Spinorgewichte, Kante iff s+s' Vektorgewicht (+-e_i)
    sites = sorted({r[:5] for r in by['(16,4)']})
    carriers = sorted({r[5:] for r in by['(16,4)']})
    require(len(sites) == 16 and len(carriers) == 4, '16 Orte x 4 Traegerzustaende = 64')
    idx = {s: i for i, s in enumerate(sites)}
    A = np.zeros((16, 16), int)
    edge_label = {}
    for s, t in itertools.combinations(sites, 2):
        u = add(s, t)
        nz = [i for i, x in enumerate(u) if x != 0]
        if len(nz) == 1 and abs(u[nz[0]]) == 1:
            A[idx[s], idx[t]] = A[idx[t], idx[s]] = 1
            edge_label[(idx[s], idx[t])] = (nz[0], int(u[nz[0]]))
    deg = A.sum(1)
    require(all(d == 5 for d in deg) and A.sum() // 2 == 40, 'Graph 5-regulaer mit 40 Kanten')
    A2 = A @ A
    lam_common = {int(A2[i, j]) for i in range(16) for j in range(16) if i != j and A[i, j] == 1}
    mu_common = {int(A2[i, j]) for i in range(16) for j in range(16) if i != j and A[i, j] == 0}
    require(lam_common == {0} and mu_common == {2}, 'stark regulaer (16,5,0,2): dreiecksfrei, mu = 2')
    ev = np.linalg.eigvalsh(A.astype(float))
    spec = Counter(int(round(e)) for e in ev)
    require(spec == Counter({5: 1, 1: 10, -3: 5}), 'Adjazenzspektrum {5^1, 1^10, (-3)^5} = Clebsch-Graph')
    # nicht bipartit (Spektrum nicht symmetrisch), zusammenhaengend (5 einfach)
    require(spec.get(-5, 0) == 0, 'nicht bipartit')
    # 1-Faktorisierung durch die fuenf D5-Koordinaten
    per_coord = defaultdict(list)
    for e, (i, sgn) in edge_label.items():
        per_coord[i].append(e)
    require(sorted(per_coord) == [0, 1, 2, 3, 4] and all(len(v) == 8 for v in per_coord.values()),
            'fuenf Kantenklassen zu je 8 Kanten')
    for i, es in per_coord.items():
        touched = [v for e in es for v in e]
        require(len(set(touched)) == 16, f'Koordinate {i}: perfektes Matching')
    per_bond = Counter(edge_label.values())
    require(len(per_bond) == 10 and set(per_bond.values()) == {4}, '10 Bindungslabels (+-e_i) zu je 4 Kanten')
    # Omega-Produktzustaende: intra-Block-Kanten kosten 0, inter-Block-Kanten 5/8. Dreiecksfrei => ein Viererblock
    # spannt hoechstens 4 Kanten (einen 4-Zykel), also E >= (5/8)(40 - 16) = 15 J; Gleichheit iff Zerlegung in vier 4-Zykel.
    cycles4 = set()
    for i, j in itertools.combinations(range(16), 2):
        if A[i, j] == 0:
            common = [k for k in range(16) if A[i, k] and A[j, k]]
            if len(common) == 2:
                cycles4.add(frozenset((i, j, *common)))
    require(len(cycles4) == 40, '40 Viererzykel (einer je Nichtkante-Paar, zwei Diagonalen je Zykel)')
    cyc = sorted(cycles4, key=sorted)

    def cover(remaining, chosen):
        if not remaining:
            return chosen
        v = min(remaining)
        for c in cyc:
            if v in c and c <= remaining:
                got = cover(remaining - c, chosen + [sorted(c)])
                if got:
                    return got
        return None
    partition = cover(frozenset(range(16)), [])
    require(partition is not None and len(partition) == 4, 'Zerlegung in vier disjunkte 4-Zykel existiert')
    omega_product_energy = F(5, 8) * (40 - 16)
    require(omega_product_energy == 15, 'Omega-Produkt auf vier 4-Zykeln: E = 15 J (variationell)')

    # Traegerkern auf einer Kante: genau die 12 geordneten Paare a != b haben Klammer, gleiche Zielwurzel fuer (a,b),(b,a)
    s, t = sites[0], next(x for x in sites if A[idx[sites[0]], idx[x]] == 1)
    kern = {}
    for a in carriers:
        for b in carriers:
            u = add(s + a, t + b)
            if u in rset:
                kern[(a, b)] = u
    require(len(kern) == 12 and all(a != b for a, b in kern), '12 geordnete Traegerpaare a != b koppeln, a = b nie')
    require(all(add(s + a, s + b) not in rset for a in carriers for b in carriers),
            'hard-core: zwei Traeger am selben Ort bilden nie eine Wurzel (Norm >= 5)')
    require(all(add(sites[i] + a, sites[j] + b) not in rset
                for i in range(16) for j in range(16) if i != j and A[i, j] == 0 for a in carriers for b in carriers),
            'Nichtkanten (Abstand 2 im Graphen) koppeln in keiner Traegerkombination')
    require(all(kern[(a, b)] == kern[(b, a)] for a, b in kern), '(a,b) und (b,a) treffen dieselbe (10,6)-Wurzel')
    require(len(set(kern.values())) == 6, 'sechs Zielzustaende = Lambda^2(4)')
    # Fuer jede Kante gleiche Struktur (Uniformitaet der Kopplung)
    for (i, j) in edge_label:
        k2 = 0
        for a in carriers:
            for b in carriers:
                if add(sites[i] + a, sites[j] + b) in rset:
                    k2 += 1
        require(k2 == 12, 'Traegerkern auf jeder Kante identisch (12)')
    # Kern mit antisymmetrischem Vorzeichen: K^+K = I - S = 2 P_Lambda
    cidx = {c: i for i, c in enumerate(carriers)}
    targets = sorted(set(kern.values()))
    K = np.zeros((6, 16))
    for (a, b), u in kern.items():
        sign = 1.0 if cidx[a] < cidx[b] else -1.0
        K[targets.index(u), 4 * cidx[a] + cidx[b]] = sign
    S = np.zeros((16, 16))
    for a in range(4):
        for b in range(4):
            S[4 * a + b, 4 * b + a] = 1
    require(np.allclose(K.T @ K, np.eye(16) - S), 'K^+K = I - S = 2 P_Lambda: H_eff = -(t^2/Delta) K^+K = J(I+S)/2 + const, J = 2t^2/Delta > 0')
    return {
        'sector_counts': counts,
        'bracket_carrier_carrier': dict(cc),
        'bracket_carrier_anticarrier': dict(ca),
        'root_pairs_with_root_sum': npairs,
        'simply_laced_structure_constants': '|N_ab| = 1 for all 240*56 pairs',
        'site_graph': {'vertices': 16, 'edges': 40, 'degree': 5, 'srg': [16, 5, 0, 2],
                       'adjacency_spectrum': {str(k): v for k, v in sorted(spec.items())},
                       'name': 'Clebsch graph (folded 5-cube)', 'one_factorisation': '5 perfect matchings = 5 D5 coordinates',
                       'bond_labels': '10 vector weights +-e_i, 4 edges each'},
        'carrier_kernel_per_edge': {'ordered_pairs': 12, 'diagonal_pairs': 0, 'targets': 6,
                                    'KtK': 'I - S (exact)'},
        'omega_product_reference': {'four_cycles': len(cycles4), 'partition_into_four_4cycles': partition,
                                    'variational_energy_over_J': 15, 'bound': 'any Omega-product state has E >= 15 J (triangle-free)'},
        'effective_exchange': 'J_edge = 2 t^2 / Delta > 0 on every Clebsch edge, 0 elsewhere; sign from 10 in Sym^2(16) x Lambda^2(4)',
    }


# ----------------------------------------------------------------------------- Vorzeichen: 10 in Sym^2(16)
def so10_spinor_bilinear():
    """Explizite so(10)-Gammamatrizen (32x32), chirale 16, Ladungskonjugation; die invariante
    Paarung 16 x 16 -> 10 ist symmetrisch (die 10 liegt in Sym^2(16), nicht in Lambda^2(16) = 120)."""
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.diag([1, -1]).astype(complex)
    I2 = np.eye(2)

    def kron(*ms):
        out = np.eye(1)
        for m in ms:
            out = np.kron(out, m)
        return out
    gam = []
    for k in range(5):
        pre = [sz] * k
        post = [I2] * (4 - k)
        gam.append(kron(*pre, sx, *post))
        gam.append(kron(*pre, sy, *post))
    for i in range(10):
        for j in range(10):
            anti = gam[i] @ gam[j] + gam[j] @ gam[i]
            require(np.allclose(anti, 2 * np.eye(32) * (i == j)), 'Clifford-Relationen')
    chi = kron(sz, sz, sz, sz, sz)          # Gamma_11 = (-i)^5 prod = prod of sz up to phase
    for g in gam:
        require(np.allclose(chi @ g, -g @ chi), 'Chiralitaet antikommutiert')
    Pp = (np.eye(32) + chi) / 2
    cols = [i for i in range(32) if abs(Pp[i, i] - 1) < 1e-12]
    require(len(cols) == 16, '16-dimensionale chirale Haelfte')
    B = np.zeros((32, 16), complex)
    for a, c in enumerate(cols):
        B[c, a] = 1
    # Ladungskonjugation: C Gamma_i C^-1 = +- Gamma_i^T; Kandidaten aus Produkten der imaginaeren/reellen Gammas
    real = [i for i in range(10) if np.allclose(gam[i].imag, 0)]
    imag = [i for i in range(10) if np.allclose(gam[i].real, 0)]
    results = {}
    for name, sel in (('C_real', real), ('C_imag', imag)):
        C = np.eye(32, dtype=complex)
        for i in sel:
            C = C @ gam[i]
        signs = set()
        for g in gam:
            lhs = C @ g @ np.linalg.inv(C)
            if np.allclose(lhs, g.T):
                signs.add(+1)
            elif np.allclose(lhs, -g.T):
                signs.add(-1)
            else:
                signs.add(0)
        results[name] = {'conjugation_sign': sorted(signs)}
        blocks = [B.T @ (C @ g) @ B for g in gam]
        nonzero = [not np.allclose(M, 0) for M in blocks]
        if all(nonzero):
            sym = all(np.allclose(M, M.T) for M in blocks)
            asym = all(np.allclose(M, -M.T) for M in blocks)
            results[name]['pairs_16x16_to_10'] = True
            results[name]['symmetric'] = bool(sym)
            results[name]['antisymmetric'] = bool(asym)
        else:
            results[name]['pairs_16x16_to_10'] = False
    hit = [v for v in results.values() if v.get('pairs_16x16_to_10')]
    # C_+ und C_- unterscheiden sich um Gamma_11, auf der chiralen 16 ein Skalar: beide liefern dieselbe Paarung.
    require(len(hit) == 2 and all(h['symmetric'] and not h['antisymmetric'] for h in hit)
            and {tuple(v['conjugation_sign']) for v in results.values()} == {(1,), (-1,)},
            'die Paarung 16 x 16 -> 10 ist symmetrisch: 10 in Sym^2(16) = 10 + 126, nicht in Lambda^2(16) = 120')
    return {'dimension_identities': {'Sym2(16)': 136, '10+126': 136, 'Lambda2(16)': 120, 'Sym2(4)': 10, 'Lambda2(4)': 6},
            'charge_conjugation': results,
            'consequence': 'the E8 bracket (16,4)x(16,4)->(10,6) is symmetric in the spinor (site) labels and antisymmetric in the carrier labels; second-order exchange lowers only Lambda^2: J > 0'}


# ----------------------------------------------------------------------------- Quelle: 15 Kontexte
def load_source():
    path = ORIGIN / 'context_instrument.py'
    require(hashlib.sha256(path.read_bytes()).hexdigest() == CORE_PIN, 'context source adapter pin')
    spec = importlib.util.spec_from_file_location('fugen_context_source', path)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    src = core.source_prefix()
    by_label = defaultdict(list)
    for k in src['line_reps']:
        z = np.array([complex(a, b) for a, b in src['Z240'][k]]) / 2.0
        require(abs(np.vdot(z, z) - 1) < TOL, 'Quellstrahl normiert (Norm 4 / 2)')
        by_label[src['root_label'][src['ROOTS'][k]]].append(z)
    labels = sorted(by_label)
    require(len(labels) == 15 and all(len(by_label[l]) == 4 for l in labels), '15 Kontexte zu je 4 Strahlen')
    bases = []
    for l in labels:
        V = np.array(by_label[l]).T          # Spalten = Kets
        require(np.allclose(V.conj().T @ V, np.eye(4)), 'Kontextbasis orthonormal')
        bases.append(V)
    return src, bases


def swap4():
    S = np.zeros((16, 16))
    for a in range(4):
        for b in range(4):
            S[4 * a + b, 4 * b + a] = 1
    return S


def f3_f4_sector_separation(bases):
    eye = np.eye(4)
    ket = [eye[:, j:j + 1] for j in range(4)]
    S = swap4()
    P_lam = (np.eye(16) - S) / 2
    P_sym = (np.eye(16) + S) / 2
    Q = np.eye(16) - 2 * sum(np.kron(k @ k.T, k @ k.T) for k in ket)
    require(np.allclose(Q @ P_lam, P_lam), 'Q wirkt als Identitaet auf Lambda^2 (Rechenkontext)')
    ev = np.linalg.eigvalsh(Q)
    require(Counter(int(round(e)) for e in ev) == Counter({-1: 4, 1: 12}), 'Q reflektiert genau vier Zustaende')
    w = np.ones((4, 4)) / 2 - eye
    prep = (eye - 2 * ket[0] @ ket[0].T) @ w
    plus = np.ones((4, 1)) / 2
    require(np.allclose(prep @ ket[0], plus), 'A|0> = |+>')

    comp_index = None
    same_context_trivial = 0
    source_trivial = 0
    omega = omega_vector()
    omega_fixed_same = 0
    omega_fixed_src = 0
    record_in_sym = 0
    for ci, V in enumerate(bases):
        if np.allclose(np.abs(V), eye):
            comp_index = ci
        VV = np.kron(V, V)
        Q_same = VV @ Q @ VV.conj().T
        Q_src = np.kron(eye, V) @ Q @ np.kron(eye, V).conj().T
        proj = [V[:, j:j + 1] @ V[:, j:j + 1].conj().T for j in range(4)]
        require(np.allclose(Q_src, np.eye(16) - 2 * sum(np.kron(ket[j] @ ket[j].T, proj[j]) for j in range(4))),
                'Quellkopplung = (I x V_C) Q (I x V_C)^+')
        require(np.allclose(Q_same, np.eye(16) - 2 * sum(np.kron(proj[j], proj[j]) for j in range(4))),
                'gleichkontextige Kopplung = (V_C x V_C) Q (V_C x V_C)^+')
        if np.allclose(Q_same @ P_lam, P_lam):
            same_context_trivial += 1
        if np.allclose(Q_src @ P_lam, P_lam):
            source_trivial += 1
        # Aufzeichnungszustand nach einem Schritt fuer beliebige Eingabe: sum_j |j> x Pi_j psi
        U = np.kron(w, eye) @ Q_src @ np.kron(prep, eye)
        require(np.allclose(U @ U, np.eye(16)), 'U^2 = I')
        ok_sym = True
        for psi in np.eye(4, dtype=complex).T.tolist() + [np.ones(4) / 2]:
            psi = np.array(psi).reshape(4, 1)
            out = U @ np.kron(ket[0], psi)
            ideal = sum(np.kron(ket[j], proj[j] @ psi) for j in range(4))
            require(np.allclose(out, ideal), 'U(|0> x psi) = sum_j |j> x Pi_j psi')
            same = np.kron(V, eye) @ out       # Register in derselben Kontextbasis gelesen
            if not np.allclose(P_lam @ same, 0):
                ok_sym = False
        if ok_sym:
            record_in_sym += 1
        # Zelle: gleichkontextige Aufzeichnung zwischen zwei Zelltraegern laesst Omega fest
        for (i, j) in itertools.combinations(range(4), 2):
            if np.allclose(apply_pair(Q_same, omega, i, j), omega):
                omega_fixed_same += 1
            if np.allclose(apply_pair(Q_src, omega, i, j), omega):
                omega_fixed_src += 1
    require(comp_index is not None, 'Rechenkontext ist einer der 15 Quellkontexte')
    require(same_context_trivial == 15, 'gleichkontextige Kopplung trivial auf Lambda^2 fuer alle 15 Kontexte')
    require(source_trivial == 1, 'Quellkopplung (Register in Pointerbasis) trivial auf Lambda^2 nur im Rechenkontext')
    require(record_in_sym == 15, 'Aufzeichnungszustand liegt fuer alle Kontexte und Eingaben in Sym^2')
    require(omega_fixed_same == 90, 'Omega fest unter gleichkontextiger Aufzeichnung: 15 Kontexte x 6 Paare')
    require(omega_fixed_src == 6, 'Omega fest unter Quellkopplung nur im Rechenkontext (6 Paare)')
    # Paarmarginalien: Aufzeichnung rein symmetrisch, Zelle rein antisymmetrisch
    once = sum(np.kron(k, k) for k in ket) / 2
    rho_rec = once @ once.T
    rho_cell = (np.eye(16) - S) / 12
    require(abs(np.trace(rho_rec @ P_lam)) < TOL and abs(np.trace(rho_cell @ P_sym)) < TOL,
            'Aufzeichnungs- und Zellmarginale liegen in orthogonalen Sektoren 10 bzw. 6')
    # Q ist nicht A3-kovariant: Kommutante von S ist span{I,S}; Q liegt nicht darin
    G = np.array([np.eye(16).ravel(), S.ravel()]).T
    coef, res, *_ = np.linalg.lstsq(G, Q.ravel(), rcond=None)
    require(res.size and res[0] > 1e-6, 'Q ist keine Linearkombination von I und S (nicht SU(4)-kovariant)')
    return {'Q_spectrum': {'-1': 4, '+1': 12},
            'Q_trivial_on_Lambda2_same_context': same_context_trivial,
            'Q_trivial_on_Lambda2_source_pointer_register': source_trivial,
            'computational_context_index': comp_index,
            'record_state_in_Sym2_all_contexts': record_in_sym,
            'Omega_fixed_same_context_pairs': omega_fixed_same,
            'Omega_fixed_source_pointer_pairs': omega_fixed_src,
            'Q_in_span_I_S': False,
            'reading': 'cells live in Lambda^2(4) = 6 (E8-native); records live in Sym^2(4) = 10 (absent from 248). '
                       'Same-context recording cannot act inside a cell; a record needs a carrier outside the hull. '
                       'The register readout basis is an extra datum (source coupling is Lambda^2-trivial only in the computational context).'}


def omega_vector():
    v = np.zeros(256)
    for perm in itertools.permutations(range(4)):
        sign = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sign = -sign
        v[perm[0] * 64 + perm[1] * 16 + perm[2] * 4 + perm[3]] = sign
    return v / np.sqrt(24)


def apply_pair(op16, vec, i, j):
    t = vec.reshape(4, 4, 4, 4)
    t = np.moveaxis(t, (i, j), (0, 1))
    shp = t.shape
    out = (op16 @ t.reshape(16, -1)).reshape(shp)
    out = np.moveaxis(out, (0, 1), (i, j))
    return out.reshape(256)


# ----------------------------------------------------------------------------- F5: 240-Bijektion
def f5_orbits(src):
    # Sp(4,2)
    Jm = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
    vecs = list(itertools.product((0, 1), repeat=4))
    group = []
    for entries in itertools.product((0, 1), repeat=16):
        M = np.array(entries).reshape(4, 4)
        if np.array_equal((M.T @ Jm @ M) % 2, Jm):
            group.append(M)
    require(len(group) == 720, '|Sp(4,2)| = 720')

    def form(u, v):
        return int(np.array(u) @ Jm @ np.array(v)) % 2
    nonzero = [v for v in vecs if any(v)]
    lagr = set()
    for u, v in itertools.combinations(nonzero, 2):
        if form(u, v) == 0:
            span = frozenset([(0, 0, 0, 0), u, v, tuple((a + b) % 2 for a, b in zip(u, v))])
            lagr.add(span)
    lagr = sorted(lagr, key=sorted)
    require(len(lagr) == 15, '15 Lagrange-Ebenen = Kontexte')
    lidx = {L: i for i, L in enumerate(lagr)}

    def act(M, v):
        return tuple(int(x) % 2 for x in (M @ np.array(v)))
    labels = [(i, v) for i in range(15) for v in vecs]
    parent = {x: x for x in labels}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for M in group:
        for (i, v) in labels:
            L2 = frozenset(act(M, u) for u in lagr[i])
            y = (lidx[L2], act(M, v))
            ra, rb = find((i, v)), find(y)
            if ra != rb:
                parent[ra] = rb
    orbits = Counter(find(x) for x in labels)
    sizes = sorted(orbits.values())
    require(sizes == [15, 45, 180], 'Bahnen der CQ-Koordinatenlabels (Kontext, Pauli): 15 + 45 + 180 = 240')

    # Wurzeln: 60 Strahlen x 4 Einheiten
    Z = {k: tuple(complex(a, b) for a, b in src['Z240'][k]) for k in range(len(src['Z240']))}
    require(len(Z) == 240, '240 Gauss-Wurzeln')
    reps = [Z[k] for k in src['line_reps']]
    require(len(reps) == 60, '60 Strahlrepraesentanten')
    units = (1, 1j, -1, -1j)
    covered = set()
    for r in reps:
        for u in units:
            covered.add(tuple(u * x for x in r))
    require(covered == set(Z.values()), '240 Wurzeln = 60 Strahlen x {1,i,-1,-i}')
    # Weyl-Gruppe transitiv auf den 240 reellen Wurzeln
    roots = e8_roots()
    rset = set(roots)
    simple = [r for r in roots if False]
    # einfache Wurzeln von E8 in D8-Koordinaten
    half = F(1, 2)
    simple = [tuple([half, -half, -half, -half, -half, -half, -half, half]),
              (F(1), F(1), F(0), F(0), F(0), F(0), F(0), F(0)),
              (F(-1), F(1), F(0), F(0), F(0), F(0), F(0), F(0)),
              (F(0), F(-1), F(1), F(0), F(0), F(0), F(0), F(0)),
              (F(0), F(0), F(-1), F(1), F(0), F(0), F(0), F(0)),
              (F(0), F(0), F(0), F(-1), F(1), F(0), F(0), F(0)),
              (F(0), F(0), F(0), F(0), F(-1), F(1), F(0), F(0)),
              (F(0), F(0), F(0), F(0), F(0), F(-1), F(1), F(0))]
    require(all(s in rset for s in simple), 'einfache Wurzeln sind Wurzeln')
    seen = {simple[1]}
    frontier = [simple[1]]
    while frontier:
        nxt = []
        for r in frontier:
            for s in simple:
                img = tuple(x - dot(r, s) * y for x, y in zip(r, s))
                if img not in seen:
                    seen.add(img)
                    nxt.append(img)
        frontier = nxt
    require(len(seen) == 240 and seen == rset, 'W(E8) transitiv auf den 240 Wurzeln')
    # Clifford-Gruppe transitiv auf den 60 Quellstrahlen
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    Sg = np.diag([1, 1j])
    I2 = np.eye(2)
    CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    gens = [np.kron(H, I2), np.kron(I2, H), np.kron(Sg, I2), np.kron(I2, Sg), CNOT]

    def canon(v):
        v = np.array(v, complex)
        k = next(i for i in range(4) if abs(v[i]) > 1e-9)
        v = v / (v[k] / abs(v[k]))
        v = v / np.linalg.norm(v)
        return tuple(np.round(v, 6) + 0)
    start = canon([1, 0, 0, 0])
    orbit = {start}
    frontier = [np.array([1, 0, 0, 0], complex)]
    while frontier:
        nxt = []
        for v in frontier:
            for g in gens:
                w = g @ v
                c = canon(w)
                if c not in orbit:
                    orbit.add(c)
                    nxt.append(w)
        frontier = nxt
    require(len(orbit) == 60, 'Clifford-Bahn des Rechenstrahls hat 60 Elemente')
    src_rays = {canon(np.array(r) / 2) for r in reps}
    require(src_rays == orbit, 'die 60 Quellstrahlen sind genau die 60 Zwei-Qubit-Stabilizerzustaende')
    return {'Sp42_order': 720, 'lagrangians': 15,
            'cq_label_orbits': sizes,
            'roots': '60 rays x 4 units; W(E8) one orbit of 240; Clifford one orbit of 60 rays',
            'verdict': 'no Sp(4,2)/Clifford-equivariant bijection between the 240 CQ coordinates (orbits 15,45,180) '
                       'and the 240 roots (orbits multiples of 60): the 240-bijection is a counting coincidence unless a '
                       'non-equivariant construction is exhibited'}


# ----------------------------------------------------------------------------- F7: Z4-Glue und (E8)_1
def dclass(v):
    """Klasse eines Vektors in Q^n relativ zu D_n: 0, v (ganzzahlig, Summe gerade/ungerade), s/c (halbzahlig)."""
    if all(x.denominator == 1 for x in v):
        return '0' if sum(v) % 2 == 0 else 'v'
    m = sum(1 for x in v if (x - F(1, 2)) % 2 == 1)   # Eintraege == -1/2 mod 2
    return 's' if m % 2 == 0 else 'c'


def f7_glue():
    vectors = []
    rng = [F(k) for k in range(-2, 3)]
    for x in itertools.product(rng, repeat=8):
        if sum(x) % 2 == 0 and dot(x, x) <= 6:
            vectors.append(x)
    hrng = [F(k, 2) for k in (-3, -1, 1, 3)]
    for x in itertools.product(hrng, repeat=8):
        if sum(x) % 2 == 0 and dot(x, x) <= 6:
            vectors.append(x)
    norms = Counter(int(dot(x, x)) for x in vectors)
    require(norms[2] == 240 and norms[4] == 2160 and norms[6] == 6720, 'Theta_E8: 240, 2160, 6720')
    coset = Counter()
    per = defaultdict(Counter)
    minnorm5 = {}
    minnorm3 = {}
    for x in vectors:
        c5, c3 = dclass(x[:5]), dclass(x[5:])
        n = int(dot(x, x))
        coset[(c5, c3)] += 1
        per[(c5, c3)][n] += 1
        n5 = dot(x[:5], x[:5])
        n3 = dot(x[5:], x[5:])
        minnorm5[c5] = min(minnorm5.get(c5, n5), n5)
        minnorm3[c3] = min(minnorm3.get(c3, n3), n3)
    glue = sorted(coset)
    require(len(glue) == 4 and ('0', '0') in glue and ('v', 'v') in glue, 'genau vier Glue-Klassen, darunter (0,0),(v,v)')
    spin = [g for g in glue if g[0] in 'sc']
    require(len(spin) == 2 and {g[1] for g in spin} == {'s', 'c'}, 'Spinorklassen von D5 gepaart mit Spinorklassen von D3')
    # zyklisch: 2 x (Spinorklasse) = (v,v)
    xs = next(x for x in vectors if (dclass(x[:5]), dclass(x[5:])) == spin[0] and int(dot(x, x)) == 2)
    twice = tuple(2 * t for t in xs)
    require((dclass(twice[:5]), dclass(twice[5:])) == ('v', 'v'), 'Glue-Gruppe zyklisch Z4: 2*(s,.) = (v,v)')
    level1 = {str(g): per[g][2] + (8 if g == ('0', '0') else 0) for g in glue}
    require(sorted(level1.values()) == [60, 60, 64, 64] and sum(level1.values()) == 248, 'Stufe 1: 60+60+64+64 = 248')
    # Charakter chi = Theta/eta^8: Koeffizienten von prod (1-q^n)^-8
    N = 4
    inv_eta8 = [0] * (N + 1)
    inv_eta8[0] = 1
    for n in range(1, N + 1):
        for _ in range(8):
            for k in range(n, N + 1):
                inv_eta8[k] += inv_eta8[k - n]
    theta = [1, norms[2], norms[4], norms[6]]
    chi = [sum(theta[k] * inv_eta8[m - k] for k in range(0, min(m, 3) + 1)) for m in range(4)]
    require(chi[:3] == [1, 248, 4124], '(E8)_1-Vakuumcharakter: 1, 248, 4124')
    weights5 = {k: str(F(v) / 2) for k, v in minnorm5.items()}
    weights3 = {k: str(F(v) / 2) for k, v in minnorm3.items()}
    require(weights5 == {'0': '0', 'v': '1/2', 's': '5/8', 'c': '5/8'} and weights3 == {'0': '0', 'v': '1/2', 's': '3/8', 'c': '3/8'},
            'konforme Gewichte h = Minimalnorm/2: D5 {0,1/2,5/8,5/8}, A3 {0,1/2,3/8,3/8}')
    return {'glue_classes': [list(g) for g in glue], 'cyclic': True,
            'norm_counts_per_class': {str(g): dict(sorted(per[g].items())) for g in glue},
            'level1_content': level1, 'character_coefficients': chi[:3],
            'h_D5': weights5, 'h_A3': weights3,
            'reading': '(E8)_1 = [(D5)_1 x (A3)_1] / Z4 (diagonal centre): a conformal embedding by a Z4 simple-current '
                       'extension, not an RG flow. Lattice content: A3 glue class = carrier number mod 4 (h = 0,3/8,1/2,3/8), '
                       'D5 glue class = NS-even/NS-odd/R sectors of ten Majoranas (h = 0,1/2,5/8,5/8), and the Z4 Gauss law ties them.'}


# ----------------------------------------------------------------------------- Graph-Fuge: vollstaendige Kopplung
def f2_complete_graph():
    """Ohne Graph (alle Paare gekoppelt) ist die Zelle fuer N = 4m eindeutig mit Gap exakt 2J (Inhaltsformel)."""
    def content(shape):
        return sum(c - r for r, row in enumerate(shape) for c in range(row))
    out = {}
    for m in (1, 2, 3, 4):
        N = 4 * m
        e0 = F(N * (N - 1), 4) + F(content((m,) * 4), 2)
        e1 = F(N * (N - 1), 4) + F(content((m + 1, m, m, m - 1)), 2)
        require(e0 == 5 * m * (m - 1) and e1 - e0 == 2, f'vollstaendiger Graph N={N}: E0 = 5m(m-1) J, Gap = 2J')
        out[f'N={N}'] = {'E0_over_J': int(e0), 'gap_over_J': int(e1 - e0), 'ground_irrep': [m] * 4, 'first_excited_irrep': [m + 1, m, m, m - 1]}
    return out


def main():
    out = {'F1_superexchange': f1_superexchange(),
           'F1_sign_of_J': so10_spinor_bilinear(),
           'F2_complete_graph': f2_complete_graph()}
    src, bases = load_source()
    out['F3_F4_sector_separation'] = f3_f4_sector_separation(bases)
    out['F5_240_bijection'] = f5_orbits(src)
    out['F7_Z4_glue'] = f7_glue()
    out['checks'] = CHECKS
    out['python_optimised'] = not __debug__
    return out


if __name__ == '__main__':
    result = main()
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    text = json.dumps(result, indent=1, sort_keys=True, default=str)
    if target:
        target.write_text(text + '\n')
    print(f'universalraum-fugen checker: {result["checks"]} checks passed')
    for key in ('F1_superexchange', 'F3_F4_sector_separation', 'F5_240_bijection', 'F7_Z4_glue'):
        print(' ', key, '->', {k: v for k, v in result[key].items() if k in ('site_graph', 'Q_trivial_on_Lambda2_same_context',
                                                                              'Q_trivial_on_Lambda2_source_pointer_register',
                                                                              'cq_label_orbits', 'level1_content', 'character_coefficients')})
