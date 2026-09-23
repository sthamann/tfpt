"""Der uebersehene Traeger-Zeiger: die Fuenf im Vier-Bank-Modell.

NON-RH, firewalled Theory-Contract-Experiment: keine Claims in verification/,
status_ledger.csv, Papers oder Website; keine Befoerderung.

Befund der Kernlektuere (origin_theory.tex, v223/v228/v315/v316/v319/v419):
Die TFPT-Uhrdoktrin sagt exakt, was die Universalraum-Modellrunden (und die
Seam-Closure-Runde) uebersehen haben:

  1. h(E8) = 30 ist quadratfrei; Z/30 hat KEIN Element der Ordnung 4.  Die
     mu4-Stationsuhr kann daher kein Zeiger sein.  Sie ist das GETRIEBE: der
     Galois-Frobenius G des Traegerfuenfecks, G C5 G^-1 = C5^2, G^4 = I
     ((Z/5)^x = Gal(Q(zeta_5)), v419).
  2. Die wahre Uhr ist der Ordnung-30-Coxeter-Zyklus, 30 = g_car * 2N_fam
     = 5 * 6: statischer Traeger-Zeiger Z/5 mal dynamischer Familien-Zeiger
     Z/6 (v319).  Die native innere Uhr der Modellrunden (Periode 6) ist der
     Familien-Zeiger; der Traeger-Zeiger C5 FEHLTE im Modell voellig --
     obwohl g_car = 5 das zweite Axiom ist und der Stationsraum genau
     4 = deg(Phi_5) Dimensionen hat.
  3. Der Vier-Marken-Divisor erzeugt die fuenf Slots (Riemann-Roch h^0 = 5,
     v228); Spiegel = Galois-Konjugation = CP (v316).

Die C12-Vereinigung der Vorrunde (T = R (x) G_F, T^12 = -I) bleibt als
Operatoraussage wahr, war aber die falsche Lesart: sie tensoriert das
Getriebe mit einem Zeiger.  Hier wird die richtige Vervollstaendigung exakt
geprueft -- alles ganzzahlig:

  A  F20 auf dem Stationsraum: C5 = Phi_5-Companion (Ordnung 5), Frobenius G
     (Ordnung 4, ganzzahlig), G C5 G^-1 = C5^2, |<C5,G>| = 20; G^2 ist die
     Konjugation (CP); im Normalbasis-Rahmen ist G der reine Viererzyklus
     (die geometrische mu4-Stationsdrehung).
  B  Die Ordnung-30-Uhr des Modells: T30 = C5 (x) G_F auf den 4*64 = 256
     Moden hat exakt Ordnung 30; das mu4-Getriebe schaltet sie auf die
     siebte Potenz, (G (x) I) T30 (G (x) I)^-1 = T30^7 (7 = Ordnung-4-
     Generator von (Z/30)^x, v223); der Seam-Spiegel als Galois-Konjugation
     mal Slot-Spiegelung, S = G^2 (x) S_F, invertiert sie: S T30 S^-1 =
     T30^-1 = T30^29 (29 = -1, die komplexe Konjugation von Q(zeta_30)).
  C  Getriebegruppe <G (x) I, G^2 (x) S_F> = Z4 x Z2 der Ordnung
     8 = rank E8 = phi(30) = (Z/30)^x; Gesamtgruppe <T30, Getriebe> hat
     exakt 240 = 30 * 8 Elemente (Holomorph von Z/30).  Dass 240 die
     E8-Wurzelzahl ist, wird als arithmetische Beobachtung notiert, nicht
     als physische Identifikation behauptet.

Ehrlich offen: die Identifikation der vier BANK-Stationen mit der
Normalbasis des Traegerfelds ist eine Basiswahl-Frage (Marken sind vierte,
Normalbasis fuenfte Einheitswurzeln); der g/Delta-Ableitungsvertrag erhaelt
den theorieseitigen Kandidaten "dynamischer Zeiger" ((2/3)^6-Struktur,
v124/v312/v314), bleibt aber offen; MARKS.01/KERNEL.01 und T3/T4/T7/T8
bleiben offen.
"""
import json
import sys
from itertools import permutations
from pathlib import Path

import numpy as np

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


def mat_pow(M, k):
    return np.linalg.matrix_power(M, k)


def order_of(M, bound):
    eye = np.eye(M.shape[0], dtype=M.dtype)
    for k in range(1, bound + 1):
        if np.array_equal(mat_pow(M, k), eye):
            return k
    return None


def bfs_group(generators, cap):
    eye = np.eye(generators[0].shape[0], dtype=np.int64)
    seen = {eye.tobytes()}
    frontier = [eye]
    while frontier:
        nxt = []
        for M in frontier:
            for Gm in generators:
                P = M @ Gm
                key = P.tobytes()
                if key not in seen:
                    seen.add(key)
                    nxt.append(P)
                    if len(seen) > cap:
                        return len(seen)
        frontier = nxt
    return len(seen)


# ------------------------------------------------------------------ Teil A ---

def part_a():
    # C5: Companion von Phi_5 = x^4+x^3+x^2+x+1 in der Potenzbasis (1,z,z2,z3)
    C5 = np.array([[0, 0, 0, -1],
                   [1, 0, 0, -1],
                   [0, 1, 0, -1],
                   [0, 0, 1, -1]], dtype=np.int64)
    need(order_of(C5, 6) == 5, 'A: C5 (Phi_5-Companion) hat exakt Ordnung 5')
    cp = np.poly(C5.astype(float))
    need(np.allclose(cp, [1, 1, 1, 1, 1]),
         'A: charakteristisches Polynom von C5 ist Phi_5')

    # Frobenius G: z -> z^2 in der Potenzbasis; z^4 = -(1+z+z^2+z^3).
    G = np.zeros((4, 4), dtype=np.int64)
    G[0, 0] = 1                      # 1 -> 1
    G[2, 1] = 1                      # z -> z^2
    G[:, 2] = [-1, -1, -1, -1]       # z^2 -> z^4
    G[1, 3] = 1                      # z^3 -> z^6 = z
    need(order_of(G, 5) == 4, 'A: Frobenius G hat exakt Ordnung 4 (das mu4-Getriebe)')
    Ginv = mat_pow(G, 3)
    need(np.array_equal(G @ C5 @ Ginv, mat_pow(C5, 2)),
         'A: G C5 G^-1 = C5^2 exakt -- das mu4 ist der Galois-Frobenius des '
         'Traegerfuenfecks, kein Zeiger (v419)')
    need(bfs_group([C5, G], 30) == 20,
         'A: <C5, G> hat exakt 20 Elemente -- die Frobeniusgruppe F20 = Z5:Z4 '
         'auf dem 4-dimensionalen Stationsraum (4 = deg Phi_5)')

    # G^2 ist die Konjugation z -> z^4 = z^-1: das CP-Element (v316).
    G2 = G @ G
    need(np.array_equal(G2 @ C5 @ G2, mat_pow(C5, 4)),
         'A: G^2 C5 G^-2 = C5^-1 -- G^2 ist die komplexe Konjugation des '
         'Traegerfelds, die Galois-Seite des Spiegels/CP')

    # Normalbasis N = (z, z^2, z^4, z^3): dort ist G der reine Viererzyklus --
    # die geometrische mu4-Stationsdrehung.
    N = np.array([[0, 0, -1, 0],
                  [1, 0, -1, 0],
                  [0, 1, -1, 0],
                  [0, 0, -1, 1]], dtype=np.int64)
    Nf = N.astype(float)
    P4 = np.linalg.inv(Nf) @ G.astype(float) @ Nf
    cyc = np.zeros((4, 4))
    for x in range(4):
        cyc[(x + 1) % 4, x] = 1
    need(np.allclose(P4, cyc, atol=1e-12),
         'A: in der Normalbasis (z, z^2, z^4, z^3) ist G der reine '
         'Viererzyklus -- die vorzeichenlose mu4-Stationsdrehung der '
         'Modellrunden ist der Frobenius in einem anderen Rahmen')
    return C5, G


# ------------------------------------------------------------------ Teil B ---

def _slot_compose(p, q):
    return [p[q[i]] for i in range(5)]


def _slot_inverse(p):
    out = [0] * 5
    for i, v in enumerate(p):
        out[v] = i
    return out


def native_clock_and_reflections():
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH
    W = nc.load_tensor()
    need(nc.casimir_identity(W), 'B: Casimir-Identitaet des gepinnten Tensors')
    GF, _GB, slot_clock, _sign = nc.clock_lift(W)
    need(order_of(GF, 7) == 6,
         'B: native innere Uhr G_F hat exakt Ordnung 6 = 2 N_fam -- der '
         'dynamische Familien-Zeiger (v319)')

    even_index = {m: i for i, m in enumerate(nc.EV)}

    def lift(slot):
        block = np.zeros((16, 16), dtype=np.int64)
        for col, mask in enumerate(nc.EV):
            mapped = [slot[j] for j in range(5) if mask & (1 << j)]
            sgn = (-1) ** sum(mapped[i] > mapped[j]
                              for i in range(len(mapped))
                              for j in range(i + 1, len(mapped)))
            block[even_index[sum(1 << j for j in mapped)], col] = sgn
        return np.kron(block, np.eye(4, dtype=np.int64))

    inv = _slot_inverse(slot_clock)
    slots = [list(s) for s in permutations(range(5))
             if _slot_compose(_slot_compose(list(s), slot_clock),
                              _slot_inverse(list(s))) == inv]
    need(len(slots) == 6, 'B: sechs uhr-invertierende Slot-Spiegelungen')
    return GF, [lift(s) for s in slots]


def part_b(C5, G):
    GF, SFs = native_clock_and_reflections()
    eye64 = np.eye(64, dtype=np.int64)

    T30 = np.kron(C5, GF)
    need(order_of(T30, 31) == 30,
         'B: T30 = C5 (x) G_F hat exakt Ordnung 30 = h(E8) = g_car * 2N_fam '
         'auf den 4*64 = 256 Moden -- die Coxeter-Uhr, die dem Modell '
         'fehlte, sobald der Traeger-Zeiger ergaenzt ist')

    Gear = np.kron(G, eye64)
    Gear_inv = np.kron(mat_pow(G, 3), eye64)
    need(np.array_equal(Gear @ T30 @ Gear_inv, mat_pow(T30, 7)),
         'B: das mu4-Getriebe schaltet die 30er-Uhr exakt auf die 7. Potenz '
         '(7 = Ordnung-4-Generator von (Z/30)^x, v223) -- Automorphismus, '
         'kein Zeiger')

    T30_inv = mat_pow(T30, 29)
    for i, SF in enumerate(SFs):
        S = np.kron(G @ G, SF)
        need(np.array_equal(S @ S, np.eye(256, dtype=np.int64)),
             'B: Spiegel Nr. %d (Galois-Konjugation x Slot-Spiegelung) ist '
             'Involution' % i)
        need(np.array_equal(S @ T30 @ S, T30_inv),
             'B: Spiegel Nr. %d invertiert die 30er-Uhr: S T30 S = T30^29, '
             'und 29 = -1 ist die komplexe Konjugation von Q(zeta_30)' % i)

    return T30, Gear, np.kron(G @ G, SFs[0])


# ------------------------------------------------------------------ Teil C ---

def part_c(T30, Gear, S):
    n = bfs_group([Gear, S], 20)
    need(n == 8,
         'C: die Getriebegruppe <G (x) I, G^2 (x) S_F> hat exakt 8 Elemente '
         '= (Z/30)^x = mu4 x Z2 = rank E8 = phi(30)')
    total = bfs_group([T30, Gear, S], 300)
    need(total == 240,
         'C: <T30, Getriebe> hat exakt 240 = 30 * 8 Elemente -- das '
         'Holomorph von Z/30: Zeiger und Getriebe der Coxeter-Uhr in EINER '
         'Gruppe auf den Modellmoden. (240 = |E8-Wurzelsystem| wird als '
         'arithmetische Beobachtung notiert, nicht als Identifikation '
         'behauptet.)')
    return {'gear_group': 8, 'holomorph': total}


# ------------------------------------------------------------------ Treiber -

def run():
    C5, G = part_a()
    T30, Gear, S = part_b(C5, G)
    c = part_c(T30, Gear, S)
    return {
        'status': 'PASS',
        'exact_checks': len(checks),
        'holonomy': c,
        'overlooked': [
            'g_car = 5 (Axiom P2) kam im Vier-Bank-Modell nirgends vor; der '
            '4-dimensionale Stationsraum ist genau deg(Phi_5) und traegt '
            'kanonisch die Frobeniusgruppe F20 = <C5, G>',
            'die mu4-Stationsuhr ist kein Zeiger, sondern das Galois-Getriebe '
            'des Traegerfuenfecks (Z/30 quadratfrei => kein Ordnung-4-Zeiger)',
            'die richtige Uhrvereinigung ist 30 = 5 * 6 (Coxeter), nicht '
            '12 = lcm(4, 6); die C12-Aussage der Vorrunde bleibt als '
            'Operatoridentitaet wahr, war aber die falsche Lesart',
            'der Seam-Spiegel ist auf der Galois-Seite die komplexe '
            'Konjugation (29 = -1 von Q(zeta_30)) -- dieselbe Operation, die '
            'v316 als CP-Konjugation identifiziert',
        ],
        'g_delta_contract': 'der einzige dynamische Satz der Theorie ist die '
                            'Rate (2/3)^6 = (|Z2|/N_fam)^(2 N_fam) auf dem '
                            'Familien-Zeiger (v124/v312/v314/v319); der '
                            'naechste Test muss die effektive Seam-Rate des '
                            'Modells gegen diese Struktur stellen -- hier '
                            'NICHT behauptet',
        'still_open': [
            'Basisidentifikation Marken (4. Einheitswurzeln) vs Normalbasis '
            '(primitive 5. Einheitswurzeln) auf den Bank-Stationen',
            'g/Delta (KERNEL.01), MARKS.01, T3/T4/T7/T8',
        ],
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
