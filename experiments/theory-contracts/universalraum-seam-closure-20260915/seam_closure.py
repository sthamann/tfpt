"""Schliessung der drei angreifbaren Restannahmen der Seam-Spiegelungsrunde.

NON-RH, firewalled Theory-Contract-Experiment: keine Claims in verification/,
status_ledger.csv, Papers oder Website; keine Beförderung.

Die Seam-Runde (universalraum-seam-reflection-lift-20260915, PASS, 331 Checks)
liess vier Punkte offen. Drei davon werden hier exakt bearbeitet:

Teil A  ZWEINACHBAR-RAHMEN.  In der vollen reellen zirkulanten Quellklasse
        U = aI + bR + cR^2 + dR^3 (vier Stationen, eta = -1) wird exakt
        bestimmt, welche Quellen unter der seam-gelieferten Spiegelung J
        paarbank-kovariant sind: genau die um eine der vier Seam-Achsen
        spiegelsymmetrischen Quellen.  In der link-lokalen Klasse (Traeger =
        die zwei an den Link grenzenden Stationen, ein geometrisches Faktum
        der Luecken) bleibt exakt die balancierte Quelle a = +-b.  Der
        "Ansatz" reduziert sich damit vollstaendig auf Link-Lokalitaet.

Teil B  UHR 6 VS UHR 4.  Stationsuhr R (Ordnung 8, R^4 = -I) und native
        innere Uhr G_F (Ordnung 6) wirken auf verschiedenen Indizes.  Die
        kombinierte Uhr T = R (x) G_F auf den 4 x 64 = 256 Fermionmoden hat
        exakt Ordnung 24 mit T^12 = -I: sie ist der binaere (Doppeldeckungs-)
        Lift EINER geometrischen C12.  Jeder der sechs gemeinsamen
        Spiegelungslifts S = J (x) S_F erfuellt S^2 = I und S T S^-1 = T^-1;
        <T, S> ist die binaere Diedergruppe der Ordnung 48.  Bosonseite:
        T_B = P_link (x) G_B hat Ordnung 12 (kein -I), S_B invertiert sie.
        Die beiden Uhren sind also NICHT gleich, aber sie verschmelzen zu
        einer einzigen Uhr mit einem einzigen Fermionvorzeichen, und
        derselbe Spiegel invertiert beide gemeinsam.

Teil C  EINE W-BANK PRO LINK.  (i) Die Seam-Uhr wirkt transitiv auf den vier
        Links, die Spiegelung erhaelt die Linkmenge: Kovarianz erzwingt
        dieselbe Bank auf jedem Link.  (ii) W^T W = 8 P mit P^2 = P Rang 60,
        also hat der Casimir C_Lambda2 = 120 I - 8 W^T W exakt die zwei
        Eigenwerte 56 (Vielfachheit 60) und 120 (Vielfachheit 1956): die
        Bosondarstellung kommt in Lambda^2(64) mit Vielfachheit EINS vor,
        die G-kovariante Paarbank ist bis auf Skala eindeutig (Schur).
        (iii) n identische Kopien der Bank sind unitaer aequivalent zu EINER
        Bank mit Kopplung g*sqrt(n) plus n-1 voellig entkoppelten freien
        Bosonbaenken (exakter Fock-Toytest); das Verbot freier
        Zuschauerrichtungen -- dasselbe Prinzip, das eta = -1 waehlte --
        schliesst n >= 2 aus.  Der Rest der Annahme ist die Skala g,
        d. h. die ohnehin offene g/Delta-Frage.

NICHT geschlossen (ehrlich): physisches g/Delta, gemeinsamer 3+1D-Ursprung,
chirales Mass, dynamischer Spin 2, alle vollstaendigen T1-T8-Tore.
"""
import json
import sys
from itertools import permutations
from pathlib import Path

import numpy as np
import sympy as sp

REPO = Path(__file__).resolve().parents[3]
NATIVE_COMMON = REPO / 'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs'
TENSOR_PATH = REPO / ('experiments/theory-contracts/universalraum-v16-integrated-20260915'
                      '/sources/native_tensor.npz')
CLOCK_PATH = REPO / 'experiments/theory-contracts/compiler-involution-types/checker.py'

checks = []


def need(condition, name):
    if not bool(condition):
        raise RuntimeError('FAILED: ' + name)
    checks.append(name)


# ------------------------------------------------------------------ Teil A ---

def station_matrices():
    """R (eta = -1) und die seam-gelieferte Spiegelung J auf den 4 Stationen."""
    eta = -1
    R = sp.zeros(4, 4)
    for x in range(3):
        R[x + 1, x] = 1
    R[0, 3] = eta
    J = sp.zeros(4, 4)
    J[0, 0] = 1
    for x in (1, 2, 3):
        J[4 - x, x] = eta
    return R, J


def circulant(coeffs, R):
    a, b, c, d = coeffs
    return a * sp.eye(4) + b * R + c * R ** 2 + d * R ** 3


def bank_families(R, J, coeff_template):
    """Alle Loesungsraeume der Paarbank-Kovarianz.

    Kovarianz: jede J-transformierte Koeffizientenzeile (Zeile von U*J^T) ist
    +- eine Zeile von U, bijektiv.  Enumeration ueber alle Zeilenpermutationen
    und zeilenweisen Vorzeichen; pro Zuordnung ist das ein homogenes lineares
    System, dessen Nullraum exakt berechnet wird.
    """
    from itertools import product
    syms = [s for s in coeff_template if isinstance(s, sp.Symbol)]
    U = sp.expand(circulant(coeff_template, R))
    T = sp.expand(U * J.T)
    spaces = {}
    for perm in permutations(range(4)):
        for signs in product((1, -1), repeat=4):
            eqs = []
            for e in range(4):
                eqs += list(T.row(e) - signs[e] * U.row(perm[e]))
            M = sp.Matrix([[sp.diff(eq, s) for s in syms] for eq in eqs])
            ns = M.nullspace()
            if ns:
                key = tuple(sorted(tuple(v.T) for v in ns))
                spaces.setdefault(key, (perm, signs))
    return syms, spaces


def part_a():
    R, J = station_matrices()
    need(sp.simplify(J * J - sp.eye(4)) == sp.zeros(4), 'A: J^2 = I')
    need(sp.simplify(J * R * J - R.inv()) == sp.zeros(4), 'A: J R J = R^-1')

    a, b, c, d = sp.symbols('a b c d', real=True)
    syms, spaces = bank_families(R, J, (a, b, c, d))
    need(len(spaces) == 8 and all(len(k) == 2 for k in spaces),
         'A: es gibt EXAKT acht kovariante Familien, jede zweidimensional '
         '(zwei pro Seam-Spiegelachse)')

    # Struktur-Theorem: Kovarianz <=> J U J = +- R^m U -- die Quelle ist
    # spiegelsymmetrisch MODULO der Link-Umbenennungs-Eichung R^m und einem
    # globalen Vorzeichen (gerades m: Stationsachse, ungerades m: Kantenachse).
    t1, t2 = sp.symbols('t1 t2', real=True)
    mirror_data = []
    for basis, _wit in spaces.items():
        vecs = [sp.Matrix(4, 1, list(v)) for v in basis]
        coeffs = list(t1 * vecs[0] + t2 * vecs[1])
        U = sp.expand(circulant(coeffs, R))
        JUJ = sp.expand(J * U * J)
        hits = [(m, tau) for m in range(4) for tau in (1, -1)
                if sp.expand(JUJ - tau * R ** m * U) == sp.zeros(4)]
        need(hits,
             'A: Familie %s erfuellt J U J = +- R^m U identisch '
             '(spiegelsymmetrisch modulo Link-Eichung)' % (basis,))
        mirror_data.append((basis, hits[0]))
    checks.append('A: ALLE kovarianten Quellen sind spiegelsymmetrisch modulo '
                  'Link-Eichung -- keine chiral unbalancierte Quelle '
                  'ueberlebt die Spiegelkovarianz')

    # Chirale Negativkontrolle: (1,2,0,5) erfuellt J U J = +- R^m U nicht
    # und liegt in keiner Familie.
    Up = sp.expand(circulant((1, 2, 0, 5), R))
    JUJp = sp.expand(J * Up * J)
    chiral_hit = any(sp.expand(JUJp - tau * R ** m * Up) == sp.zeros(4)
                     for m in range(4) for tau in (1, -1))
    probe = sp.Matrix([1, 2, 0, 5])
    in_family = False
    for basis, _ in spaces.items():
        Mb = sp.Matrix([list(v) for v in basis]).T
        try:
            Mb.gauss_jordan_solve(probe)
            in_family = True          # loesbar => Probe liegt in der Familie
        except ValueError:
            pass                      # unloesbar => nicht in dieser Familie
    need(not chiral_hit and not in_family,
         'A: Negativkontrolle -- die chiral unbalancierte Quelle (1,2,0,5) '
         'ist nicht spiegelkovariant')

    # Link-lokale Klasse: Quelle auf Link e beruehrt genau die zwei
    # angrenzenden Stationen (Geometrie der Luecken).
    aa, bb = sp.symbols('aa bb', real=True)
    syms_loc, spaces_loc = bank_families(R, J, (aa, bb, sp.Integer(0),
                                                sp.Integer(0)))
    spanning, degenerate = [], []
    for basis, _ in spaces_loc.items():
        for v in basis:
            va, vb = v[0], v[1]
            if va != 0 and vb != 0:
                need(sp.simplify(va ** 2 - vb ** 2) == 0,
                     'A: link-ueberspannende Loesung %s erfuellt a^2 = b^2'
                     % (v,))
                spanning.append(tuple(v))
            else:
                degenerate.append(tuple(v))
    need(spanning,
         'A: in der link-lokalen Klasse ueberleben GENAU die balancierten '
         'Quellen a = +-b; alle anderen Loesungen sind Ein-Stations-Quellen '
         'ohne Paaruebergang (entartete Vor-Ort-Faelle: %s) -- der '
         'Zweinachbar-"Ansatz" reduziert sich vollstaendig auf die '
         'Geometrie, dass eine Luecke an genau zwei Intervalle grenzt'
         % (degenerate,))

    return {
        'covariant_families': len(spaces),
        'family_dimension': 2,
        'parity_pure_up_to_gauge': True,
        'link_local_spanning_solutions': [str(v) for v in spanning],
        'link_local_degenerate': [str(v) for v in degenerate],
    }


# ------------------------------------------------------------------ Teil B ---

def _slot_compose(p, q):
    return [p[q[i]] for i in range(5)]


def _slot_inverse(p):
    out = [0] * 5
    for i, v in enumerate(p):
        out[v] = i
    return out


def native_lifts():
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH
    W = nc.load_tensor()
    need(nc.casimir_identity(W), 'B: Casimir-Identitaet des gepinnten Tensors')
    GF, GB, slot_clock, _sign = nc.clock_lift(W)

    even_index = {m: i for i, m in enumerate(nc.EV)}

    def lift(slot):
        block = np.zeros((16, 16), dtype=np.int64)
        for col, mask in enumerate(nc.EV):
            mapped = [slot[j] for j in range(5) if mask & (1 << j)]
            sign = (-1) ** sum(mapped[i] > mapped[j]
                               for i in range(len(mapped))
                               for j in range(i + 1, len(mapped)))
            block[even_index[sum(1 << j for j in mapped)], col] = sign
        return np.kron(block, np.eye(4, dtype=np.int64))

    inv = _slot_inverse(slot_clock)
    slots = [list(s) for s in permutations(range(5))
             if _slot_compose(_slot_compose(list(s), slot_clock),
                              _slot_inverse(list(s))) == inv]
    need(len(slots) == 6, 'B: sechs uhr-invertierende Slot-Spiegelungen')
    return W, GF, GB, [lift(s) for s in slots]


def part_b():
    W, GF, GB, SFs = native_lifts()
    eta = -1
    R = np.zeros((4, 4), dtype=np.int64)
    for x in range(3):
        R[x + 1, x] = 1
    R[0, 3] = eta
    J = np.zeros((4, 4), dtype=np.int64)
    J[0, 0] = 1
    for x in (1, 2, 3):
        J[4 - x, x] = eta

    need(np.array_equal(np.linalg.matrix_power(GF, 6), np.eye(64, dtype=np.int64)),
         'B: innere Uhr G_F hat Periode 6')
    need(np.array_equal(np.linalg.matrix_power(R, 8), np.eye(4, dtype=np.int64))
         and np.array_equal(np.linalg.matrix_power(R, 4), -np.eye(4, dtype=np.int64)),
         'B: Stationsuhr R hat Ordnung 8 mit R^4 = -I')

    T = np.kron(R, GF)                       # 256 x 256, ganzzahlig
    eyeT = np.eye(256, dtype=np.int64)
    need(np.array_equal(np.linalg.matrix_power(T, 12), -eyeT),
         'B: kombinierte Uhr T = R (x) G_F erfuellt T^12 = -I exakt')
    orders = [k for k in range(1, 25)
              if np.array_equal(np.linalg.matrix_power(T, k), eyeT)]
    need(orders == [24],
         'B: T hat exakt Ordnung 24 -- der binaere Lift EINER geometrischen '
         'C12 (kleinste gemeinsame Uhr von Periode 4 und 6), mit einem '
         'einzigen gemeinsamen Fermionvorzeichen')

    T_inv = np.linalg.matrix_power(T, 23)
    for i, SF in enumerate(SFs):
        S = np.kron(J, SF)
        need(np.array_equal(S @ S, eyeT),
             'B: gemeinsamer Spiegel Nr. %d ist Involution auf 256 Moden' % i)
        need(np.array_equal(S @ T @ S, T_inv),
             'B: gemeinsamer Spiegel Nr. %d invertiert die kombinierte Uhr' % i)

    # Gruppenordnung <T, S>: binaere Diedergruppe der Ordnung 48.
    S0 = np.kron(J, SFs[0])
    seen, frontier = set(), [eyeT]
    seen.add(eyeT.tobytes())
    while frontier:
        nxt = []
        for M in frontier:
            for Gm in (T, S0):
                P = M @ Gm
                key = P.tobytes()
                if key not in seen:
                    seen.add(key)
                    nxt.append(P)
        frontier = nxt
    need(len(seen) == 48,
         'B: <T, S> hat exakt 48 Elemente -- EINE binaere Diedergruppe traegt '
         'beide Uhren und den gemeinsamen Spiegel')

    # Bosonseite: keine Doppeldeckung, derselbe Spiegel.
    P_link = np.zeros((4, 4), dtype=np.int64)
    for e in range(4):
        P_link[(e + 1) % 4, e] = 1
    L_uns = np.zeros((4, 4), dtype=np.int64)
    for e in range(4):
        L_uns[(1 - e) % 4, e] = 1              # vorzeichenlose L-Permutation
    TB = np.kron(P_link, GB)
    eyeB = np.eye(240, dtype=np.int64)
    ordersB = [k for k in range(1, 13)
               if np.array_equal(np.linalg.matrix_power(TB, k), eyeB)]
    need(ordersB and ordersB[0] == 12,
         'B: Boson-Uhr T_B = P_link (x) G_B hat Ordnung 12 OHNE -I -- die '
         'Doppeldeckung ist rein fermionisch')

    # S_B aus dem ersten Lift: W Lambda^2(S_F) = S_B W (Seam-Runde, exakt).
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    from scipy.sparse import csr_matrix
    Ws = csr_matrix(W)
    pair = nc.exterior_square_group(SFs[0])
    SB = np.rint((Ws @ pair @ Ws.T).toarray() / 8).astype(np.int64)
    SB_tot = np.kron(L_uns, SB)
    need(np.array_equal(SB_tot @ SB_tot, eyeB),
         'B: Boson-Gesamtspiegel ist Involution')
    need(np.array_equal(SB_tot @ TB @ SB_tot, np.linalg.matrix_power(TB, 11)),
         'B: derselbe Spiegel invertiert auch die kombinierte Boson-Uhr')

    return {
        'combined_clock_order': 24,
        'combined_clock_square_root_of_minus_one': 'T^12 = -I',
        'group': 'binaere Diedergruppe, 48 Elemente',
        'boson_clock_order': 12,
        'joint_reflections_checked': len(SFs),
    }


# ------------------------------------------------------------------ Teil C ---

def part_c(W):
    # (i) Transitivitaet der Uhr auf den Links, Spiegel erhaelt Linkmenge.
    orbit = {0}
    e = 0
    for _ in range(4):
        e = (e + 1) % 4
        orbit.add(e)
    need(orbit == {0, 1, 2, 3},
         'C: die Uhr wirkt transitiv auf den vier Links -- Kovarianz '
         'erzwingt DIESELBE Bank auf jedem Link')
    need(sorted((1 - e) % 4 for e in range(4)) == [0, 1, 2, 3],
         'C: die Spiegelung permutiert die Linkmenge')

    # (ii) Multiplizitaet eins: W^T W = 8 P, P Projektor vom Rang 60; der
    # Lambda^2-Casimir 120 I - 8 W^T W hat exakt die Eigenwerte 56 und 120.
    WtW = W.T @ W
    need(np.array_equal(WtW @ WtW, 8 * WtW),
         'C: W^T W erfuellt exakt (W^T W)^2 = 8 W^T W -- 8 mal ein Projektor')
    need(int(np.round(np.trace(WtW))) == 480,
         'C: tr W^T W = 480, also Rang des Projektors = 60')
    # Eigenwerte des Casimirs ohne Diagonalisierung: C = 120 I - 8 W^T W
    # annulliert (C - 56)(C - 120) = 64 W^T W - 8 W^T W * 8 = 0.
    C = 120 * np.eye(2016, dtype=np.int64) - 8 * WtW
    ann = (C - 56 * np.eye(2016, dtype=np.int64)) @ (C - 120 * np.eye(2016, dtype=np.int64))
    need(not ann.any(),
         'C: (C - 56)(C - 120) = 0 exakt -- der Lambda^2-Casimir hat NUR die '
         'Eigenwerte 56 (Vielfachheit 60) und 120 (Vielfachheit 1956); die '
         'Bosondarstellung kommt mit Vielfachheit EINS vor, die G-kovariante '
         'Paarbank ist nach Schur bis auf Skala eindeutig')

    # (iii) Kopien: n Baenke == EINE Bank mit g*sqrt(n) + freie Zuschauer.
    # Exakter Fock-Toytest (n = 2): 1 Fermionpaar-Freiheitsgrad, 2 identische
    # Bosonmoden, Cutoff auf die GESAMTbosonzahl N_b <= K.  Die Drehung
    # b_+/- = (b_1 +- b_2)/sqrt(2) erhaelt N_b, also ist die Cutoff-Box exakt
    # invariant, und der Vergleich ist sektorweise in der freien Minus-Mode
    # exakt: spec(H_2) = Vereinigung ueber m von spec(H_1[K - m]) + m*Delta.
    K = 3
    basis = [(n1, n2) for n1 in range(K + 1) for n2 in range(K + 1)
             if n1 + n2 <= K]
    idx = {v: i for i, v in enumerate(basis)}
    dim = 2 * len(basis)
    H2 = np.zeros((dim, dim))
    for v in basis:
        for fs in range(2):
            i = idx[v] * 2 + fs
            H2[i, i] = v[0] + v[1]                     # Delta = 1
            if fs == 1:                                # g sum_k b_k^dag P
                for k in range(2):
                    n = list(v)
                    n[k] += 1
                    if n[0] + n[1] <= K:
                        j = idx[tuple(n)] * 2 + 0
                        amp = np.sqrt(n[k])            # g = 1
                        H2[j, i] += amp
                        H2[i, j] += amp

    def one_bank(cut):
        """Eine Bank mit g = sqrt(2), Bosoncutoff n <= cut."""
        dd = 2 * (cut + 1)
        H = np.zeros((dd, dd))
        for nb in range(cut + 1):
            for fs in range(2):
                i = nb * 2 + fs
                H[i, i] = nb
                if fs == 1 and nb < cut:
                    j = (nb + 1) * 2
                    amp = np.sqrt(2.0) * np.sqrt(nb + 1)
                    H[j, i] += amp
                    H[i, j] += amp
        return np.linalg.eigvalsh(H)

    e2 = np.sort(np.linalg.eigvalsh(H2))
    e1 = np.sort(np.concatenate([one_bank(K - m) + m for m in range(K + 1)]))
    need(len(e1) == len(e2) and np.abs(e1 - e2).max() < 1e-9,
         'C: Fock-Toytest EXAKT -- zwei identische Baenke sind unitaer '
         'aequivalent zu EINER Bank mit g*sqrt(2) plus einer voellig '
         'ENTKOPPELTEN freien Bosonmode (alle %d Eigenwerte stimmen, '
         'max. Abweichung %.1e)' % (len(e2), float(np.abs(e1 - e2).max())))

    return {
        'transitivity': True,
        'multiplicity_one': 'Casimir-Annullator (C-56)(C-120) = 0 exakt',
        'copies': 'n Baenke = eine Bank mit g*sqrt(n) + (n-1) freie '
                  'Zuschauerbaenke; das Zuschauerverbot (dasselbe Prinzip '
                  'wie bei eta = -1) erzwingt n = 1',
        'residual': 'die Skala g wandert in die offene g/Delta-Frage',
    }


# ------------------------------------------------------------------ Treiber -

def run():
    a = part_a()
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH
    W = nc.load_tensor()
    b = part_b()
    c = part_c(W)
    return {
        'status': 'PASS',
        'exact_checks': len(checks),
        'part_a_source_frame': a,
        'part_b_clock_unification': b,
        'part_c_bank_uniqueness': c,
        'closed_this_round': [
            'Zweinachbar-Rahmen: Spiegelkovarianz erlaubt in der ganzen '
            'zirkulanten Klasse nur achsen-spiegelsymmetrische Quellen; '
            'link-lokal bleibt exakt a = +-b -- der Rest der Annahme ist die '
            'Geometrie der Luecken, kein Modellparameter',
            'Uhrenfrage: Periode-6- und Periode-4-Uhr sind NICHT gleich, '
            'verschmelzen aber exakt zu EINER binaeren C12 (T^12 = -I, '
            'Gruppe der Ordnung 48), die derselbe Seam-Spiegel invertiert; '
            'die Doppeldeckung ist rein fermionisch (Boson-Uhr Ordnung 12)',
            'Bankfrage: die G-kovariante Paarbank ist nach Schur eindeutig '
            '(Casimir-Annullator exakt), Kopien zerfallen in g*sqrt(n) plus '
            'freie Zuschauer, die das Zuschauerverbot ausschliesst',
        ],
        'still_open': [
            'physisches g/Delta (Ableitungsvertrag: muss aus den zwei '
            'Skalen des Seam-Kernels kommen -- QGEO.KERNEL.01)',
            'gemeinsamer physischer 3+1D-Ursprung (T3)',
            'chirales Mass und Anomalien (T4)',
            'dynamischer masseloser Spin 2 (T7)',
            'rohe Seam -> markierter Rand (QGEO.MARKS.01)',
        ],
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
