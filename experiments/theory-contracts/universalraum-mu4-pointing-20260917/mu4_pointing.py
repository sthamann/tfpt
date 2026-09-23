"""Mu4-Pointing auf der Seam: traegt die Seam mehr als die Kardinalitaet |mu4| = 4?

NON-RH, firewalled Theory-Contract-Experiment: keine Claims in verification/,
status_ledger.csv, Papers, Website oder Scorecard; keine Befoerderung.
MARKS.01 und T4 bleiben offen.

Hypothese unter Angriff (kein Claim): die Seam trage bereits eine kanonische
mu4-Pointing-Struktur (Basispunkt 1, Orientierung i, Vorzeichen -1), und das
abstrakte Z4 (nur Kardinalitaet) reiche fuer die betreffenden Tests nicht.
Diskriminator ist genau dieser Kontrast; die Negativkontrolle (Teil C) ist
Teil der Pruefung.

Vorrunden-Befund (universalraum-seam-closure-20260915, PASS, 44 Checks):
T = R (x) G_F auf den 4*64 = 256 Fermionmoden hat Ordnung 24 mit T^12 = -I;
sechs gemeinsame Spiegel S = J (x) S_F erfuellen S^2 = I und S T S^-1 = T^-1;
<T,S> hat 48 Elemente.  Boson-Uhr T_B = P_link (x) G_B hat Ordnung 12 ohne -I.

Teil A  AUSZEICHNUNG (Bedingung B1).  Die Ordnung-4-Elemente von <T,S> werden
        vollstaendig enumeriert: genau EINE C4-Untergruppe, normal, ihr
        einziges Involutionselement ist T^12 = -I (Vorzeichenschicht).
Teil B  ORIENTIERUNG / BASISPUNKT (B2, B3; T4-Angriff).  T^6 = -T^18: die zwei
        Pointings liefern entgegengesetzte chirale Graduierungen, jede exakt
        balanciert (128/128); die Bosonbank ist orientierungsblind; keine
        Station ist ausgezeichnet (Modell und roher v480-Ring).
Teil C  NEGATIVKONTROLLE / MARKIERUNGSRAUM / KONSISTENZ (B4, B5).  Das
        bosonische Z4 = <T_B^3> hat keine Vorzeichenschicht (-I liegt in
        keinem Element von <T_B, S_B>); der Markierungsraum
        M = Z4 x {+-1} traegt die aus den Operatorrelationen verifizierte
        Aktion t:(b,e)->(b+1,e), s:(b,e)->(-b,-e); Replay der
        Seam-Closure-Schnittstelle.

Alles ganzzahlig (int64) oder exakte Permutationskombinatorik, keine Floats.
"""
import json
import sys
from itertools import permutations
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix

REPO = Path(__file__).resolve().parents[3]
NATIVE_COMMON = REPO / 'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs'
TENSOR_PATH = REPO / ('experiments/theory-contracts/universalraum-v16-integrated-20260915'
                      '/sources/native_tensor.npz')
CLOCK_PATH = REPO / 'experiments/theory-contracts/compiler-involution-types/checker.py'

# v480 Seam-Ring-Geometrie (unveraendert; nur die ganzzahlige Kombinatorik).
N_RING = 256
P0 = 8
ELL = 48

checks = []


def need(condition, name):
    if not bool(condition):
        raise RuntimeError('FAILED: ' + name)
    checks.append(name)


# ------------------------------------------------------------- Grunddaten ---

def station_matrices():
    """R (Stationsuhr, eta = -1) und J (Seam-Spiegel) auf den 4 Stationen."""
    R = np.zeros((4, 4), dtype=np.int64)
    for x in range(3):
        R[x + 1, x] = 1
    R[0, 3] = -1
    J = np.zeros((4, 4), dtype=np.int64)
    J[0, 0] = 1
    for x in (1, 2, 3):
        J[4 - x, x] = -1
    return R, J


def _slot_compose(p, q):
    return [p[q[i]] for i in range(5)]


def _slot_inverse(p):
    out = [0] * 5
    for i, v in enumerate(p):
        out[v] = i
    return out


def native_lifts():
    """Gepinnter Tensor, innere Uhr G_F, G_B und die sechs Spiegelungslifts."""
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH
    W = nc.load_tensor()
    need(nc.casimir_identity(W), 'C-Replay: Casimir-Identitaet des gepinnten Tensors')
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
    need(len(slots) == 6, 'C-Replay: sechs uhr-invertierende Slot-Spiegelungen')
    return nc, W, GF, GB, [lift(s) for s in slots]


def bfs_elements(generators, eye, cap):
    """Alle Gruppenelemente als {tobytes: Matrix}; bricht ueber cap ab."""
    seen = {eye.tobytes(): eye}
    frontier = [eye]
    while frontier:
        nxt = []
        for M in frontier:
            for G in generators:
                P = M @ G
                key = P.tobytes()
                if key not in seen:
                    seen[key] = P
                    nxt.append(P)
                    if len(seen) > cap:
                        raise RuntimeError('Gruppengroesse ueber Cap %d' % cap)
        frontier = nxt
    return seen


def order_of(M, bound):
    eye = np.eye(M.shape[0], dtype=np.int64)
    P = eye.copy()
    for k in range(1, bound + 1):
        P = P @ M
        if np.array_equal(P, eye):
            return k
    return None


def signed_perm(M):
    """Permutationsbild einer Vorzeichen-Permutationsmatrix (Spalte j -> Zeile)."""
    return [int(v) for v in np.argmax(np.abs(M), axis=0)]


# ------------------------------------------------------- rohe Seam (v480) ---

def _intervals():
    quarter = N_RING // 4
    return [list(range(P0 + j * quarter, P0 + j * quarter + ELL)) for j in range(4)]


def _ap_image(site, centre):
    t = centre - site
    while t < 0:
        t += N_RING
    while t >= N_RING:
        t -= N_RING
    return t


def _block_action(blocks, centre):
    """Permutationsbild der Spiegelung s -> centre - s auf den Bloecken."""
    where = {s: j for j, arc in enumerate(blocks) for s in arc}
    image = []
    for arc in blocks:
        targets = set()
        for s in arc:
            t = _ap_image(s, centre)
            if t not in where:
                return None
            targets.add(where[t])
        if len(targets) != 1:
            return None
        image.append(targets.pop())
    if sorted(image) != list(range(len(blocks))):
        return None
    return image


# --------------------------------------------------------- Boson-Seite ------

def link_matrices():
    P_link = np.zeros((4, 4), dtype=np.int64)
    for e in range(4):
        P_link[(e + 1) % 4, e] = 1
    L_uns = np.zeros((4, 4), dtype=np.int64)
    for e in range(4):
        L_uns[(1 - e) % 4, e] = 1
    return P_link, L_uns


def boson_reflection(nc, W, SF0, L_uns):
    """S_B aus W Lambda^2(S_F) = S_B W (exakt), Gesamtspiegel L_uns (x) S_B."""
    Ws = csr_matrix(W)
    pair = nc.exterior_square_group(SF0)
    SB = np.rint((Ws @ pair @ Ws.T).toarray() / 8).astype(np.int64)
    residual = Ws @ pair - csr_matrix(SB) @ Ws
    residual.eliminate_zeros()
    need(residual.nnz == 0, 'C-Replay: W Lambda^2(S_F) = S_B W exakt')
    return np.kron(L_uns, SB)


# ------------------------------------------------------------------ Teil A ---

def part_a(T, S_list, eye256):
    """B1: genau eine C4 in <T,S>, normal, Involution = -I."""
    group = bfs_elements([T, S_list[0]], eye256, 60)
    need(len(group) == 48, 'A: <T, S> hat exakt 48 Elemente (Replay)')
    need(order_of(T, 24) == 24, 'A: T hat exakt Ordnung 24 (Replay)')
    T6 = np.linalg.matrix_power(T, 6)
    T12 = np.linalg.matrix_power(T, 12)
    T18 = np.linalg.matrix_power(T, 18)
    need(np.array_equal(T12, -eye256), 'A: T^12 = -I exakt (Replay)')

    order4 = [M for M in group.values() if order_of(M, 24) == 4]
    need(len(order4) == 2
         and any(np.array_equal(M, T6) for M in order4)
         and any(np.array_equal(M, T18) for M in order4),
         'A: die Ordnung-4-Elemente von <T,S> sind EXAKT T^6 und T^18 -- es '
         'gibt genau EINE C4-Untergruppe (alle Elemente S T^k ausserhalb <T> '
         'sind Involutionen)')
    need(order_of(T6, 24) == 4 and np.array_equal(T18, T6 @ T6 @ T6),
         'A: die C4 ist <T^6> = {I, T^6, T^12, T^18} mit T^18 = (T^6)^3')
    need(np.array_equal(T6 @ T6, T12),
         'A: das einzige Involutionselement der C4 ist (T^6)^2 = T^12 = -I -- '
         'die Vorzeichenschicht der Pointing ist kanonisch und IST das '
         'Fermionvorzeichen')
    need(all(np.array_equal(S @ T6 @ S, T18) and np.array_equal(S @ T18 @ S, T6)
             for S in S_list),
         'A: die C4 ist normal in <T,S> -- jede der sechs Spiegelungen '
         'konjugiert T^6 zu T^18 (Auszeichnung ohne Wahl)')
    return T6, T12, T18


# ------------------------------------------------------------------ Teil B ---

def part_b(T6, T18, TB, R, J, eye256):
    """B2/B3: Orientierung und Basispunkt sind NICHT geometrisch ausgezeichnet."""
    zero256 = np.zeros((256, 256), dtype=np.int64)
    need(not np.array_equal(T6, T18) and np.array_equal(T6 + T18, zero256),
         'B: T^6 = -T^18 als Operatoren -- die zwei Pointings liefern '
         'ENTGEGENGESETZTE chirale Graduierungen; die Graduierung haengt echt '
         'an der Pointing (Diskriminator: ohne Erzeugerwahl ist sie unbestimmt)')
    need(np.array_equal(T18 @ T18, -eye256),
         'B: (T^18)^2 = -I -- die Eigenwerte des Erzeugers sind nur +i und -i')
    need(int(np.trace(T18)) == 0,
         'B: tr(T^18) = 0, also Eigenwerte +i und -i je 128-fach -- jede '
         'Pointing liefert eine bestimmte, exakt BALANCIERTE chirale '
         'Graduierung der 256 Moden (Netto-Chiralitaet 0: kein chirales Mass, '
         'T4 bleibt offen)')
    need(np.array_equal(np.linalg.matrix_power(TB, 6), np.linalg.matrix_power(TB, 18)),
         'B: T_B^6 = T_B^18 -- die Bosonbank ist orientierungsblind; die '
         'Orientierung ist ein rein fermionisches Datum')
    need(signed_perm(R) == [1, 2, 3, 0] and signed_perm(J) == [0, 3, 2, 1],
         'B: R wirkt als 4-Zyklus transitiv auf den Stationen, J fixiert genau '
         '{0,2} -- keine Station ist im Modell ausgezeichnet')

    centres = {}
    iv = _intervals()
    for c in range(N_RING):
        st = _block_action(iv, c)
        if st is not None:
            centres[c] = st
    need(sorted(centres) == [63, 127, 191, 255],
         'B: rohe Seam (v480-Ring): exakt vier stationenerhaltende '
         'Spiegelungen, Zentren 63/127/191/255 (Replay)')
    actions = sorted(centres.values())
    need(actions == [[0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3], [3, 2, 1, 0]],
         'B: rohe Seam: die Stationsbilder sind exakt die vier Spiegelachsen '
         'des Quadrats -- zwei Eckenachsen [0,3,2,1] und [2,1,0,3] sowie '
         'zwei Kantenachsen [1,0,3,2] und [3,2,1,0]')
    fixed_sets = [frozenset(j for j in range(4) if st[j] == j)
                  for st in centres.values()]
    need(sorted(tuple(sorted(f)) for f in fixed_sets)
         == [(), (), (0, 2), (1, 3)],
         'B: rohe Seam: Fixstationen exakt {0,2} bzw. {1,3} bei den '
         'Eckenachsen, KEINE bei den Kantenachsen')
    need(not fixed_sets[0].intersection(*fixed_sets[1:]),
         'B: rohe Seam: KEINE Station wird von allen vier Spiegelungen '
         'fixiert -- einen kanonischen Basispunkt gibt es bereits auf der '
         'rohen Seam nicht')


# ------------------------------------------------------------------ Teil C ---

def part_c(T, T6, T18, S_list, R, GF, TB, SB_tot, eye240):
    """B4 Negativkontrolle, B5 Markierungsraum und Konsistenz."""
    need(order_of(TB, 12) == 12, 'C: T_B hat exakt Ordnung 12 (Replay)')
    TB3 = np.linalg.matrix_power(TB, 3)
    need(order_of(TB3, 12) == 4,
         'C: auch die Bosonseite enthaelt ein abstraktes Z4 = <T_B^3> -- die '
         'Kardinalitaet 4 allein ist NICHT das Unterscheidungsmerkmal')
    P_link, _L_uns = link_matrices()
    TB6 = np.linalg.matrix_power(TB, 6)
    need(np.array_equal(TB6, np.kron(P_link @ P_link, np.eye(60, dtype=np.int64))),
         'C: T_B^6 = P_link^2 (x) I (Strukturpin)')
    need(not np.array_equal(TB6, -eye240),
         'C: Negativkontrolle Vorzeichen: das Involutionselement T_B^6 der '
         'bosonischen Z4 ist NICHT -I')
    boson_group = bfs_elements([TB, SB_tot], eye240, 60)
    need(len(boson_group) == 24, 'C: <T_B, S_B> hat exakt 24 Elemente (Replay)')
    need((-eye240).tobytes() not in boson_group,
         'C: Negativkontrolle: -I liegt in KEINEM Element der bosonischen '
         'Seam-Gruppe <T_B, S_B> -- die Vorzeichenschicht fehlt jedem '
         'abstrakten/bosonischen Z4; sie ist rein fermionisch')

    # Markierungsraum M = Z4 x {+-1}: die Aktion wird aus den Operatoren
    # verifiziert, nicht positiert.
    need(np.array_equal(T @ T18, T18 @ T),
         'C: T kommutiert mit dem Erzeuger T^18 -- die Uhr fixiert die '
         'Orientierung (t wirkt nur auf den Basispunkt)')
    need(all(np.array_equal(S @ T18 @ S, T6) for S in S_list),
         'C: jede der sechs Spiegelungen sendet T^18 zu T^6 = (T^18)^-1 -- '
         'die Spiegelung flippt die Orientierung')
    need(signed_perm(np.linalg.matrix_power(R, 12)) == [0, 1, 2, 3],
         'C: T^12 = -I wirkt trivial auf den Markierungen (Stationsbild '
         'identisch, Orientierung fix) -- die Markierungsgruppe ist eine '
         'Quotientenaktion von <T,S>')

    markings = [(b, e) for b in range(4) for e in range(2)]
    index = {m: i for i, m in enumerate(markings)}
    t_map = tuple(index[((b + 1) % 4, e)] for (b, e) in markings)
    s_map = tuple(index[((-b) % 4, 1 - e)] for (b, e) in markings)

    def compose(p, q):
        return tuple(p[q[i]] for i in range(8))

    idp = tuple(range(8))
    mgroup = {idp}
    frontier = [idp]
    while frontier:
        nxt = []
        for g in frontier:
            for h in (t_map, s_map):
                p = compose(g, h)
                if p not in mgroup:
                    mgroup.add(p)
                    nxt.append(p)
        frontier = nxt
    need(len(mgroup) == 8,
         'C: die Markierungsgruppe auf M hat exakt 8 Elemente')
    t2 = compose(t_map, t_map)
    need(compose(t2, t2) == idp and compose(s_map, s_map) == idp
         and compose(s_map, compose(t_map, s_map)) == compose(t2, t_map),
         'C: t^4 = s^2 = 1 und s t s = t^-1 -- die Markierungsgruppe ist die '
         'Diedergruppe D4 des Stationsquadrats')
    orbit = {g[0] for g in mgroup}
    fixed_point_free = all(all(g[i] != i for i in range(8))
                           for g in mgroup if g != idp)
    need(len(orbit) == 8 and fixed_point_free,
         'C: die Aktion auf den 8 Markierungen ist FREI TRANSITIV -- M ist '
         'ein D4-Torsor: exakt acht Markierungen (4 Basispunkte x 2 '
         'Orientierungen), keine ausgezeichnet; MARKS.01 ist genau diese Wahl')


# ------------------------------------------------------------------ Treiber --

def run():
    R, J = station_matrices()
    nc, W, GF, GB, SFs = native_lifts()
    eye256 = np.eye(256, dtype=np.int64)
    eye240 = np.eye(240, dtype=np.int64)
    T = np.kron(R, GF)
    S_list = [np.kron(J, SF) for SF in SFs]
    P_link, L_uns = link_matrices()
    TB = np.kron(P_link, GB)
    SB_tot = boson_reflection(nc, W, SFs[0], L_uns)

    # B5: Replay der pointing-relevanten Seam-Closure-Schnittstelle.
    need(np.array_equal(np.linalg.matrix_power(R, 4), -np.eye(4, dtype=np.int64))
         and np.array_equal(np.linalg.matrix_power(R, 8), np.eye(4, dtype=np.int64)),
         'C-Replay: R^4 = -I und R^8 = I')
    need(np.array_equal(np.linalg.matrix_power(GF, 6), np.eye(64, dtype=np.int64)),
         'C-Replay: G_F^6 = I')
    need(np.array_equal(J @ R @ J, np.linalg.matrix_power(R, 7)),
         'C-Replay: J R J = R^-1')
    for i, S in enumerate(S_list):
        need(np.array_equal(S @ S, eye256)
             and np.array_equal(S @ T @ S, np.linalg.matrix_power(T, 23)),
                 'C-Replay: Spiegel Nr. %d ist Involution und invertiert T' % i)
    need(np.array_equal(SB_tot @ SB_tot, eye240)
         and np.array_equal(SB_tot @ TB @ SB_tot, np.linalg.matrix_power(TB, 11)),
         'C-Replay: Boson-Gesamtspiegel ist Involution und invertiert T_B')

    T6, T12, T18 = part_a(T, S_list, eye256)
    part_b(T6, T18, TB, R, J, eye256)
    part_c(T, T6, T18, S_list, R, GF, TB, SB_tot, eye240)

    return {
        'status': 'PASS',
        'exact_checks': len(checks),
        'befund': {
            'c4_eindeutig_und_normal': True,
            'vorzeichenschicht': 'kanonisch: einziges Involutionselement der '
                                 'einzigen C4 ist T^12 = -I = Fermionvorzeichen',
            'orientierung_ausgezeichnet': False,
            'basispunkt_ausgezeichnet': False,
            'chirale_graduierung': 'je Pointing bestimmt und exakt balanciert '
                                   '(128/128), Netto-Chiralitaet 0; die zwei '
                                   'Pointings sind entgegengesetzt (T^6 = -T^18)',
            'bosonbank': 'orientierungsblind (T_B^6 = T_B^18)',
            'markierungsraum': '8 Markierungen (4 Basispunkte x 2 '
                               'Orientierungen), D4-Torsor (frei transitiv)',
            'negativkontrolle_diskriminiert': True,
        },
        'konsequenz': [
            'die Seam traegt kanonisch die UNORIENTIERTE C4 samt Vorzeichen '
            '-1; Orientierung und Basispunkt sind die Markierung, die die '
            'rohe Seam NICHT liefert -- MARKS.01 bekommt damit einen exakten '
            'endlichen Inhalt: Wahl einer von 8 Markierungen',
            'T4-Angriff: die Pointing induziert hoechstens eine '
            'pointing-abhaengige Z2-Graduierung mit Netto-Chiralitaet 0, '
            'kein chirales Mass -- T4 bleibt offen',
        ],
        'nicht_gezeigt': [
            'keine Konstruktion des markierten Randes (MARKS.01 bleibt offen, '
            'nur sein Wahldatum ist exakt bestimmt)',
            'kein chirales Mass, keine Anomalie (T4 bleibt offen)',
            'keine Aussage zur physischen Identifikation der C4; der '
            'Carrier-Hand-Befund (mu4 als Galois-Getriebe, wahre Uhr 30) '
            'wird nicht angefasst',
        ],
    }


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print('%d/%d Bedingungen' % (result['exact_checks'], result['exact_checks']))
