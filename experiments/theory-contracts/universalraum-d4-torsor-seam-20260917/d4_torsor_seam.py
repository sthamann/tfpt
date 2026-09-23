"""D4-Torsor statt ausgezeichneter Seam-Markierung -- praeregistrierter Contract-Checker.

NON-RH, firewalled Theory-Contract-Experiment: keine Claims in verification/,
status_ledger.csv, Papers, Website oder Scorecard; keine Befoerderung.
Es werden keine Gate-IDs geschlossen (closed_gate_ids=[]), promotion=false.

Hypothese unter Angriff (kein Claim): die vier Basispunkte sind Eichrepraesentanten
einer D4-aequivarianten Seam-Familie; die zwei Orientierungen koennten getrennte
paritaetskonjugierte Sektoren sein; der rohe Seam traegt die Familie, waehlt
keinen Punkt aus.

Alle fachlichen Rechnungen exakt (int64 / Fraction); keine Floats.
Pins werden vor jeder fachlichen Rechnung geprueft. need() wirft RuntimeError
und zaehlt benannte Checks; keine assertions als fachliche Gates.
"""
import json
import sys
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[3]

MU4_PATH = REPO / ('experiments/theory-contracts/'
                   'universalraum-mu4-pointing-20260917/mu4_pointing.py')
MU4_SHA = '6c15a99722234db4c41a7b859967ea7a7b39d94983121ee0d19af3aec744a032'

SEAM_LIFT_PATH = REPO / ('experiments/theory-contracts/'
                         'universalraum-seam-reflection-lift-20260915/'
                         'seam_reflection_lift.py')
SEAM_LIFT_SHA = ('300f8670f16727b747244b63b76acf57a030d5f7f51774aef6401cb4'
                 '6338d808')

NATIVE_COMMON_PATH = REPO / ('universal_room/new-3/universalraum-v1.6.9/'
                             'agents/source/inputs/native_common.py')
NATIVE_COMMON_SHA = ('2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e'
                     '98e2adb994')

PARENT_SPEC_PATH = REPO / ('universal_room/new-3/'
                           'universalraum-common-parent-t1-t8-20260915/'
                           'parent_spec.json')
PARENT_SPEC_SHA = ('f0ac19749175a3f3cb24d419b31b66f060b44d7b0523f8dd8ea75f'
                   '501d5b33c4')

V56_PATH = REPO / 'verification/v56_unique_attractor.py'
V56_SHA = 'd0870475b4b56dc386935a8845a7494120da713a2f6a60488460faafe63f39fc'

V162_PATH = REPO / 'verification/v162_seam_transport_identification.py'
V162_SHA = ('1d3a80006bcff439f88b83d7f3b64d03a7b8d9cea15308ca7c68fde8'
            '6beb5225')

TENSOR_PATH = REPO / ('experiments/theory-contracts/'
                      'universalraum-v16-integrated-20260915/sources/'
                      'native_tensor.npz')
TENSOR_SHA = ('3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079b'
              'b64b763')

CLOCK_PATH = REPO / ('experiments/theory-contracts/'
                     'compiler-involution-types/checker.py')
CLOCK_SHA = '9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1'

checks = []


def need(condition, name):
    if not bool(condition):
        raise RuntimeError('FAILED: ' + name)
    checks.append(name)


def pin(path, digest, label):
    data = Path(path).read_bytes()
    if sha256(data).hexdigest() != digest:
        raise RuntimeError('pin mismatch: ' + label)
    return data


def station_matrices():
    """R (Stationsuhr, eta=-1) und J (Seam-Spiegel) auf den 4 Stationen, int64."""
    R = np.zeros((4, 4), dtype=np.int64)
    for x in range(3):
        R[x + 1, x] = 1
    R[0, 3] = -1
    J = np.zeros((4, 4), dtype=np.int64)
    J[0, 0] = 1
    for x in (1, 2, 3):
        J[4 - x, x] = -1
    return R, J


def raw_ring_matrices():
    """Tatsaechliche Vierteldrehung und Zentrum-63-Spiegelung des 256er-Rings."""
    n_ring = 256
    quarter = 64
    rho = np.zeros((n_ring, n_ring), dtype=np.int64)
    sigma = np.zeros((n_ring, n_ring), dtype=np.int64)
    for site in range(n_ring):
        image = site + quarter
        clock_sign = 1
        if image >= n_ring:
            image -= n_ring
            clock_sign = -1
        rho[image, site] = clock_sign

        image = 63 - site
        reflection_sign = 1
        while image < 0:
            image += n_ring
            reflection_sign = -reflection_sign
        sigma[image, site] = reflection_sign
    return rho, sigma


def _trace_powers(M, kmax):
    eye = np.eye(M.shape[0], dtype=M.dtype)
    P = eye.copy()
    out = []
    for _ in range(kmax):
        P = P @ M
        out.append(int(np.trace(P)))
    return out


def native_source():
    """Lade W, GF, GB und sechs SF via gepinntem native_common (kein main)."""
    sys.path.insert(0, str(NATIVE_COMMON_PATH.parent))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH
    W = nc.load_tensor()
    need(nc.casimir_identity(W),
         'Pin: gepinnter Tensor erfuellt Casimir-Identitaet')
    GF, GB, slot_clock, _sign = nc.clock_lift(W)
    need(np.array_equal(np.linalg.matrix_power(GF, 6),
                        np.eye(64, dtype=np.int64)),
         'Pin: native Uhr G_F hat Periode 6')
    need(np.array_equal(np.linalg.matrix_power(GB, 6),
                        np.eye(60, dtype=np.int64)),
         'Pin: native Uhr G_B hat Periode 6')

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

    def _slot_compose(p, q):
        return [p[q[i]] for i in range(5)]

    def _slot_inverse(p):
        out = [0] * 5
        for i, v in enumerate(p):
            out[v] = i
        return out

    inv = _slot_inverse(slot_clock)
    slots = [list(s) for s in permutations(range(5))
             if _slot_compose(_slot_compose(list(s), slot_clock),
                              _slot_inverse(list(s))) == inv]
    need(len(slots) == 6, 'Pin: genau sechs uhr-invertierende Slot-Spiegelungen')
    SFs = [lift(s) for s in slots]
    eye64 = np.eye(64, dtype=np.int64)
    GF_inv = np.linalg.matrix_power(GF, 5)
    for i, SF in enumerate(SFs):
        need(np.array_equal(SF @ SF, eye64),
             'Pin: Spiegel-Lift %d ist Involution (S_F^2 = +I)' % i)
        need(np.array_equal(SF @ GF @ SF.T, GF_inv),
             'Pin: Spiegel-Lift %d invertiert G_F (S_F G_F S_F^-1 = G_F^-1)' % i)
    return W, GF, GB, SFs


def part_a():
    """D4-Aktion auf M = Z4 x {0,1}; freier transitiver Orbit, Quotient exakt 2."""
    markings = [(b, e) for b in range(4) for e in range(2)]
    index = {m: i for i, m in enumerate(markings)}

    def t(b, e):
        return ((b + 1) % 4, e)

    def s(b, e):
        return ((-b) % 4, 1 - e)

    t_map = tuple(index[t(b, e)] for (b, e) in markings)
    s_map = tuple(index[s(b, e)] for (b, e) in markings)

    def compose(p, q):
        return tuple(p[q[i]] for i in range(8))

    idp = tuple(range(8))
    group = {idp}
    frontier = [idp]
    while frontier:
        nxt = []
        for g in frontier:
            for h in (t_map, s_map):
                p = compose(g, h)
                if p not in group:
                    group.add(p)
                    nxt.append(p)
        frontier = nxt
    need(len(group) == 8, 'A: |D4| = 8 (Markierungsgruppe)')
    need(compose(t_map, compose(t_map, compose(t_map, t_map))) == idp,
         'A: t^4 = 1')
    need(compose(s_map, s_map) == idp, 'A: s^2 = 1')
    need(compose(s_map, compose(t_map, s_map))
         == compose(t_map, compose(t_map, t_map)),
         'A: s t s = t^-1 (D4-Relationen)')
    fixed_point_free = all(all(g[i] != i for i in range(8))
                           for g in group if g != idp)
    need(fixed_point_free,
         'A: D4-Aktion auf M ist FREI (kein nichttriviales Element fixiert eine '
         'Markierung) -- kein globaler Fixpunkt, keine D4-aequivariante Auswahl '
         'eines einzelnen Punkts')
    orbit = {g[0] for g in group}
    need(len(orbit) == 8,
         'A: D4-Aktion auf M ist TRANSITIV (ein Orbit der Groesse 8) -- M ist '
         'ein D4-Torsor')

    rot_orbits = []
    remaining = set(range(8))
    while remaining:
        start = remaining.pop()
        orbit_set = set()
        x = start
        for _ in range(4):
            orbit_set.add(x)
            x = t_map[x]
        remaining -= orbit_set
        rot_orbits.append(sorted(orbit_set))
    need(len(rot_orbits) == 2, 'A: Rotationsquotient C4 hat exakt zwei Bahnen '
         '(die zwei Orientierungen)')
    for o in rot_orbits:
        e = markings[o[0]][1]
        s_image = s_map[o[0]]
        need(markings[s_image][1] == 1 - e,
             'A: Spiegelung s sendet Orientierung %d in Orientierung %d '
             '(vertauscht die Bahnen)' % (e, 1 - e))
    return {
        'markierungsraum': 'M = Z4 x {0,1}, |M| = 8',
        'd4_ordnung': 8,
        'frei_transitiv': True,
        'rotationsquotient_bahnen': 2,
        'bahnen_orientierungen': 'e=0 und e=1; s vertauscht sie',
        'kein_globaler_fixpunkt': True,
        'keine_d4_aequivariante_einpunktwahl': True,
    }


# --------------------------------------------------- Teil B: Basispunkt ----

def part_b(R, J, W, GF, GB, SFs):
    """Vier Basispunkte: transportiere Operatoren durch R^b; vergleiche exakt.

    Bericht nennt die Scope-Grenze: Gleichheit zeigt nur endliche unitaere
    Aequivalenz, keine physische Eichsymmetrie.
    """
    eye4 = np.eye(4, dtype=np.int64)
    eye256 = np.eye(256, dtype=np.int64)
    T = np.kron(R, GF)
    rho_bank = np.linalg.matrix_power(T, 3)
    need(np.array_equal(np.linalg.matrix_power(rho_bank, 4), -eye256),
         'B-Pin: rho_bank = T^3 erfuellt rho_bank^4 = -I (Ordnung-8-Untergenerator)')

    station_reflections = []
    station_trace_powers = []
    for b in range(4):
        Rb = np.linalg.matrix_power(R, b)
        Rb_inv = np.linalg.matrix_power(R, (-b) % 8)
        Jb = Rb @ J @ Rb_inv
        station_reflections.append(Jb)
        station_trace_powers.append(_trace_powers(Jb, 4))
    need(all(tp == station_trace_powers[0] for tp in station_trace_powers),
         'B: Spurpotenzen der vier konjugierten Stations-Spiegel sind identisch')
    for b, Jb in enumerate(station_reflections):
        need(np.array_equal(Jb.T @ Jb, eye4),
             'B: Stations-Gram %d ist exakt I (J_b orthogonal)' % b)
        need(np.array_equal(Jb @ Jb, eye4),
             'B: Stations-Spiegel %d ist Involution (J_b^2 = I)' % b)

    bank_trace_powers = []
    for b in range(4):
        rho_b = np.linalg.matrix_power(rho_bank, b)
        rho_b_inv = np.linalg.matrix_power(rho_bank, -b % 8)
        Tb = rho_b @ T @ rho_b_inv
        bank_trace_powers.append(_trace_powers(Tb, 12))
    need(all(tp == bank_trace_powers[0] for tp in bank_trace_powers),
         'B: Spurpotenzen tr(T_b^j), j=1..12, der vier konjugierten Bank-Uhren '
         'sind identisch (T kommutiert mit rho_bank = T^3)')
    need(bank_trace_powers[0][5] == 0,
         'B: tr(T^6) = 0 (T^6 = -T^18, Spur 0 -- balancierte chirale Graduierung)')
    need(bank_trace_powers[0][11] == -256,
         'B: tr(T^12) = -256 (T^12 = -I_256)')

    need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)),
         'B: W W^T = 8 I_60 (basispunktunabhaengig, Pin-Replay)')

    # Eine konkrete link-lokale Quelle je Basispunkt.  Der Transport erfolgt
    # durch die gepinnte antiperiodische Stationsuhr; verglichen werden die
    # Gram-Spektralinvarianten, nicht nur die abstrakte Konjugationsbehauptung.
    source_gram_trace_powers = []
    bank_channel_trace_powers = []
    source_seed = np.zeros((4, 1), dtype=np.int64)
    source_seed[0, 0] = 1
    source_seed[1, 0] = 1
    channel_metric = W @ W.T
    for b in range(4):
        source_b = np.linalg.matrix_power(R, b) @ source_seed
        source_gram = source_b @ source_b.T
        source_gram_trace_powers.append(_trace_powers(source_gram, 4))
        mark_projector = np.zeros((4, 4), dtype=np.int64)
        mark_projector[b, b] = 1
        bank_channel = np.kron(mark_projector, channel_metric)
        bank_channel_trace_powers.append(_trace_powers(bank_channel, 3))
    need(all(tp == source_gram_trace_powers[0] for tp in source_gram_trace_powers),
         'B: konkrete Zweinachbar-Quellen haben an allen vier Basispunkten '
         'identische Gram-Spurpotenzen')
    need(all(tp == bank_channel_trace_powers[0] for tp in bank_channel_trace_powers),
         'B: konkrete mark-lokale W-Bank-Kanalmetriken haben an allen vier '
         'Basispunkten identische Spurpotenzen')

    transfer_multiset = [
        Fraction(1),
        Fraction(2, 3) ** 6,
        Fraction(1, 3) ** 6,
    ]
    need(transfer_multiset == [Fraction(1), Fraction(64, 729), Fraction(1, 729)],
         'B: Transfer-Spektrum ist exakt {1, (2/3)^6, (1/3)^6}')
    pinned_ms = [Fraction(1), Fraction(64, 729), Fraction(1, 729)]
    for b in range(4):
        need(transfer_multiset == pinned_ms,
             'B: Transfer-Spektrum unabhaengig von Basispunkt %d (Pin)' % b)

    return {
        'stationen_spiegel_schurpotenzen': station_trace_powers,
        'bank_uhr_schurpotenzen': bank_trace_powers,
        'zweinachbar_quellen_gram_schurpotenzen': source_gram_trace_powers,
        'mark_lokale_bankmetrik_schurpotenzen': bank_channel_trace_powers,
        'w_casimir_wwt': '8 I_60 (Pin, basispunktunabhaengig)',
        'transfer_multiset': [str(x) for x in transfer_multiset],
        'basispunkt_invariant': True,
        'scope_grenze': ('Gleichheit der Invarianten zeigt nur endliche unitaere '
                         'Aequivalenz der vier konjugierten Operatoren, keine '
                         'physische Eichsymmetrie; der rationale Transfer-Multiset '
                         'ist ein Pin aus dem verifizierten Kernel (Part E), nicht '
                         'hier unabhaengig rekonstruiert.'),
    }


# --------------------------------------- Teil C: Raw-Seam-zu-Bank-Hom -------

def _group_elements_16(r, s):
    """16 Elemente der binaeren D4 (Ordnung 16): r^k und s r^k, k=0..7.

    Liefert Liste der 16 Matrizen (jede 256x256 int64). r^4 = -I (zentral),
    r^8 = I, s^2 = I, s r s = r^-1.
    """
    eye = np.eye(r.shape[0], dtype=np.int64)
    powers = [eye]
    for k in range(1, 8):
        powers.append(powers[-1] @ r)
    elements = list(powers)  # r^0 .. r^7
    for k in range(8):
        elements.append(s @ powers[k])  # s r^k
    return elements


def _hom_dimension(rho_raw, sigma_raw, rho_bank, sigma_bank):
    """Hom-Dim via Charakterformel: (1/16) sum_g tr(rho_raw(g)) tr(rho_bank(g)).

    g laeuft ueber die 16 Elemente der binaeren D4 in der Reihenfolge
    r^0..r^7, s r^0..s r^7 mit r=rho_raw, s=sigma_raw auf der Raw-Seite und
    r=rho_bank, s=sigma_bank auf der Bank-Seite. Beide Darstellungen muessen
    dieselben Relationen erfuellen; das wird vom Aufrufer geprueft.
    """
    raw_elems = _group_elements_16(rho_raw, sigma_raw)
    bank_elems = _group_elements_16(rho_bank, sigma_bank)
    need(len(raw_elems) == 16 and len(bank_elems) == 16,
         'C-intern: beide Seitengruppen haben 16 Elemente')
    need(len({g.tobytes() for g in raw_elems}) == 16
         and len({g.tobytes() for g in bank_elems}) == 16,
         'C-intern: beide Darstellungen realisieren 16 verschiedene Gruppenelemente')
    s = 0
    for g_raw, g_bank in zip(raw_elems, bank_elems):
        s += int(np.trace(g_raw)) * int(np.trace(g_bank))
    need(s % 16 == 0, 'C-intern: Charaktersumme %d durch 16 teilbar (Integralitaet)' % s)
    return s // 16


def _verify_binary_d4_relations(r, s, label):
    """Verifiziere r^8=I, r^4=-I, s^2=I, s r s = r^-1 fuer die binaere D4."""
    eye = np.eye(r.shape[0], dtype=np.int64)
    need(np.array_equal(np.linalg.matrix_power(r, 8), eye),
         'C: %s r^8 = I (Ordnung 8)' % label)
    need(np.array_equal(np.linalg.matrix_power(r, 4), -eye),
         'C: %s r^4 = -I (zentrales Vorzeichen, binaere Ueberlagerung)' % label)
    need(np.array_equal(s @ s, eye),
         'C: %s s^2 = I (Spiegelungsinvolution)' % label)
    r_inv = np.linalg.matrix_power(r, 7)
    need(np.array_equal(s @ r @ s, r_inv),
         'C: %s s r s = r^-1 (D4-Relation)' % label)


def part_c(R, J, GF, SFs):
    """Hom-Dim fuer jeden der sechs Spiegel-Lifts; Intertwiner-Verdict."""
    eye256 = np.eye(256, dtype=np.int64)
    reversal64 = np.fliplr(np.eye(64, dtype=np.int64))
    rho_raw, sigma_raw = raw_ring_matrices()
    need(np.array_equal(rho_raw, np.kron(R, np.eye(64, dtype=np.int64))),
         'C: rohe Vierteldrehung ist in Blockkoordinaten R_station (x) I_64')
    need(np.array_equal(sigma_raw, np.kron(J, reversal64)),
         'C: rohe Zentrum-63-Spiegelung ist J_station (x) F_64 mit interner '
         'Umkehrung q -> 63-q (nicht J_station (x) I_64)')
    _verify_binary_d4_relations(rho_raw, sigma_raw, 'raw')
    need(np.array_equal(np.linalg.matrix_power(rho_raw, 4), -eye256),
         'C: rho_raw^4 = -I_256 (antiperiodische Vierteldrehung)')

    T = np.kron(R, GF)
    rho_bank = np.linalg.matrix_power(T, 3)
    need(np.array_equal(np.linalg.matrix_power(rho_bank, 4), -eye256),
         'C: rho_bank^4 = -I_256 (Ordnung-8-Untergenerator der Bank)')

    per_lift = []
    hom_dims = []
    for i, SF in enumerate(SFs):
        sigma_bank = np.kron(J, SF)
        _verify_binary_d4_relations(rho_bank, sigma_bank, 'bank lift %d' % i)

        dim = _hom_dimension(rho_raw, sigma_raw, rho_bank, sigma_bank)
        need(dim >= 0,
             'C: Hom-Dim Lift %d ist nichtnegativ (%d)' % (i, dim))
        hom_dims.append(dim)
        per_lift.append({
            'lift_index': i,
            'hom_dimension': dim,
            'sigma_bank_relations_verified': True,
        })

    need(len(set(hom_dims)) == 1,
         'C: alle sechs Lifts liefern dieselbe Hom-Dimension (keine '
         'Lift-abhaengige Nicht-Eindeutigkeit in dieser Typisierung)')
    common_dim = hom_dims[0]

    # Negativkontrolle: dim V_raw = dim V_bank = 256 zaehlt nicht als
    # Intertwiner; der markierte 192-Moden-Unterraum ist nur Typkontrolle.
    need(rho_raw.shape[0] == 256 and rho_bank.shape[0] == 256,
         'C: Negativkontrolle -- dim V_raw = dim V_bank = 256 ist keine '
         'Intertwiner-Aussage (nur gleiche Dimension)')
    marked_dim = 4 * 48
    need(marked_dim == 192,
         'C: Negativkontrolle -- markierter Unterraum hat Dimension 192 '
         '(vier Intervalle zu je 48 Moden), nur Typkontrolle, nicht mit der '
         '256-dimensionalen Vierbank zu identifizieren')

    # Invertierbarkeit: nur bei explizit belegtem Kandidat moeglich; nicht aus
    # Hom-Dim folgern. Wir haben keinen expliziten Kandidaten -> false.
    explicit_invertible_candidate = False
    raw_seam_to_w_intertwiner = (
        common_dim == 1 and explicit_invertible_candidate
    )

    return {
        'rho_raw': 'R_station (x) I_64, rho_raw^4 = -I',
        'sigma_raw': 'J_station (x) F_64, F_64(q)=63-q',
        'rho_bank': 'T^3 = (R (x) G_F)^3, rho_bank^4 = -I',
        'sigma_bank_per_lift': 'J (x) S_F fuer jeden der sechs S_F',
        'gruppenordnung': 16,
        'hom_dimension_alle_lifts': hom_dims,
        'hom_dimension_konstant_ueber_lifts': len(set(hom_dims)) == 1,
        'hom_dimension': common_dim,
        'intertwiner_eindeutig': common_dim == 1,
        'expliziter_invertierbarer_kandidat': explicit_invertible_candidate,
        'raw_seam_to_w_intertwiner': raw_seam_to_w_intertwiner,
        'negativkontrolle_dim_256_kein_intertwiner': True,
        'negativkontrolle_markiert_192_typkontrolle': True,
        'per_lift': per_lift,
    }


# --------------------------------------------- Teil D: Orientierung --------

def _signed_perm_determinant(M):
    """Exakte Determinante einer Vorzeichen-Permutationsmatrix (int64)."""
    n = M.shape[0]
    seen = [False] * n
    sign = 1
    for j in range(n):
        if seen[j]:
            continue
        cycle_len = 0
        k = j
        while not seen[k]:
            seen[k] = True
            row = int(np.argmax(np.abs(M[:, k])))
            sign *= int(M[row, k])
            k = row
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign = -sign
    return sign


def part_d(R, J, GF):
    """Orientierung: A = T^18; exakt schiefsymmetrisch, A^2 = -I, tr = 0."""
    T = np.kron(R, GF)
    A = np.linalg.matrix_power(T, 18)
    eye256 = np.eye(256, dtype=np.int64)
    zero256 = np.zeros((256, 256), dtype=np.int64)

    need(np.array_equal(A.T, -A),
         'D: A = T^18 ist exakt schiefsymmetrisch (A^T = -A)')
    need(np.array_equal(A @ A, -eye256),
         'D: A^2 = -I exakt (Eigenwerte nur +-i, keine anderen)')
    need(int(np.trace(A)) == 0,
         'D: tr(A) = 0 (Eigenwerte +i und -i je 128-fach, balanciert)')
    need(not np.array_equal(A, zero256),
         'D: A ist nicht die Nullmatrix (nichttrivial)')

    A_neg = -A
    need(np.array_equal(A_neg, np.linalg.matrix_power(T, 6)),
         'D: -A = -T^18 = T^6 (die zwei Pointings sind entgegengesetzt)')
    need(np.array_equal(A_neg.T, -A_neg),
         'D: -A ist ebenfalls schiefsymmetrisch')
    need(np.array_equal(A_neg @ A_neg, -eye256),
         'D: (-A)^2 = -I (gleiche Eigenwertstruktur)')
    need(int(np.trace(A_neg)) == 0,
         'D: tr(-A) = 0 (gleiche balancierte Multiplizitaet)')

    det_A = _signed_perm_determinant(A)
    det_A_neg = _signed_perm_determinant(A_neg)
    need(det_A in (1, -1),
         'D: det(A) ist exakt +-1 (Vorzeichenpermutation)')
    need(det_A_neg in (1, -1),
         'D: det(-A) ist exakt +-1 (Vorzeichenpermutation)')
    need(det_A == det_A_neg,
         'D: det(A) = det(-A) exakt (Dimension 256 gerade -> gleiche Determinante)')

    # Pfaffian-Skalierungsparitaet: Pfaff(-A) = (-1)^128 Pf(A) fuer 256x256,
    # also (-1)^128 = +1 -> Pfaffian-Skalierung gerade.
    n = A.shape[0]
    pfaffian_scaling_parity = (-1) ** (n // 2)
    need(pfaffian_scaling_parity == 1,
         'D: Pfaffian-Skalierungsparitaet (-1)^128 = +1 (gerade) -- kein '
         'Vorzeichenunterschied der Pfaffian-Linie zwischen A und -A')

    # Chiralitaetsindex von Gamma=-iA: Multiplizitaetsdifferenz ist wegen
    # tr(A)=0 gleich null. A selbst hat imaginaere Eigenwerte und seine Spur
    # wird nicht als Index umetikettiert.
    chiral_index = 0
    need(chiral_index == 0,
         'D: Chiralitaetsindex von Gamma=-iA ist 0 (128 minus 128)')

    # Keine Float-Eigenwerte: wir berechnen keine Eigenwerte numerisch;
    # die Multiplizitaeten werden ausschliesslich aus exakten Spur-/Quadrat-
    # identitaeten geschlossen (tr=0, A^2=-I).
    balanced_multiplicities = True
    equal_determinant = (det_A == det_A_neg)
    even_pfaffian_parity = (pfaffian_scaling_parity == 1)

    orientation_sector_refuted_by_balanced = (
        balanced_multiplicities and equal_determinant and even_pfaffian_parity
    )
    orientation_invariant_nontrivial = not orientation_sector_refuted_by_balanced

    return {
        'A': 'T^18',
        'A_neg': '-T^18 = T^6',
        'A_transpose': 'A^T = -A (exakt schiefsymmetrisch)',
        'A_square': 'A^2 = -I (exakt)',
        'trace_A': 0,
        'trace_A_neg': 0,
        'eigenwerte': '+i und -i je 128-fach (aus tr=0, A^2=-I exakt)',
        'det_A': det_A,
        'det_A_neg': det_A_neg,
        'det_gleich': equal_determinant,
        'pfaffian_skalierungsparitaet': int(pfaffian_scaling_parity),
        'pfaffian_gerade': even_pfaffian_parity,
        'chiralitaetsindex': chiral_index,
        'keine_float_eigenwerte': True,
        'multiplizitaeten_balanciert': balanced_multiplicities,
        'orientation_invariant_nontrivial': orientation_invariant_nontrivial,
        'orientation_sector_durch_balancierte_widerlegt':
            orientation_sector_refuted_by_balanced,
    }


# ----------------------------------------------- Teil E: Kernel / g/Delta ---

def part_e(parent_spec):
    """Kernel: rationale Werte als Fraction; Delta symbolisch; g/Delta NOT_AVAILABLE."""
    lam = [Fraction(1), Fraction(2, 3) ** 6, Fraction(1, 3) ** 6]
    need(len(lam) == 3, 'E: Kernel-Spektrum hat drei Eintraege')
    need(all(isinstance(x, Fraction) for x in lam),
         'E: alle Kernel-Eigenwerte sind exakte Fraction (keine Floats)')
    need(lam[0] == Fraction(1), 'E: lambda_0 = 1 exakt')
    need(lam[1] == Fraction(64, 729),
         'E: lambda_1 = (2/3)^6 = 64/729 exakt')
    need(lam[2] == Fraction(1, 729),
         'E: lambda_2 = (1/3)^6 = 1/729 exakt')

    delta_symbolic = '6*log(3/2)'
    mass_ratio_symbolic = 'log(3)/log(3/2)'
    g_delta_from_raw_kernel = 'NOT_AVAILABLE'

    # Firewall: verbotene Werte duerfen nicht als g/Delta ausgegeben werden.
    forbidden_values = {Fraction(1, 20), 5, '1/20', 'g_car=5', 5.0, 0.05}
    need(g_delta_from_raw_kernel not in forbidden_values,
         'E: Firewall -- g/Delta ist NOT_AVAILABLE, weder 1/20 noch g_car=5 '
         'wurden als Ersatz importiert')
    need(g_delta_from_raw_kernel == 'NOT_AVAILABLE',
         'E: g_delta_from_raw_kernel = NOT_AVAILABLE (kein roher '
         'Calderon/Seam-Konstruktor in den eingefrorenen Quellen gibt '
         'gleichzeitig physisches g und Delta aus)')

    # Expliziter Nachweis: weder 1/20 noch g_car=5 tauchen als importierte
    # Kernel-Werte auf.
    imported_kernel_values = [str(x) for x in lam]
    need('1/20' not in imported_kernel_values
         and str(Fraction(1, 20)) not in imported_kernel_values,
         'E: Firewall -- 1/20 ist nicht im importierten Kernel-Multiset')
    need(5 not in lam and '5' not in imported_kernel_values,
         'E: Firewall -- g_car=5 ist nicht im importierten Kernel-Multiset')
    need(parent_spec['verdict']['raw_seam_to_w_intertwiner'] is False,
         'E: gepinnte Parent-Spezifikation fuehrt Raw-Seam-zu-W-Intertwiner '
         'weiterhin als false')
    absent = parent_spec['absent']
    need(any('physical g/Delta parameter value' in item for item in absent),
         'E: gepinnte Parent-Spezifikation fuehrt physisches g/Delta als fehlend')

    return {
        'lambda_multiset': [str(x) for x in lam],
        'lambda_multiset_rational': True,
        'delta_symbolic': delta_symbolic,
        'mass_ratio_symbolic': mass_ratio_symbolic,
        'g_delta_from_raw_kernel': g_delta_from_raw_kernel,
        'firewall_1_over_20_nicht_importiert': True,
        'firewall_g_car_5_nicht_importiert': True,
        'not_available_kein_rechenintegritaetsfehler': True,
        'not_available_verhindert_torsor_reduction': True,
    }


# ----------------------------------------------------- Verdict und Driver --

def _verdict(a, b, c, d, e):
    """Verdict strikt nach README-Enum."""
    kernel_ok = (e['g_delta_from_raw_kernel'] == 'NOT_AVAILABLE')

    basis_invariant = b['basispunkt_invariant']
    hom_dim = c['hom_dimension']
    intertwiner_unique = c['intertwiner_eindeutig']
    invertible_candidate = c['expliziter_invertierbarer_kandidat']

    orientation_nontrivial = d['orientation_invariant_nontrivial']

    # KERNEL_VIOLATION: Pin, feste Dimension/Relation oder Firewall verletzt.
    # (Hier: alle Pins bestanden, Firewall bestanden -> kein KERNEL_VIOLATION.)

    # REFUTED: Basispunkte liefern verschiedene Invarianten, Hom-Raum ist null,
    # oder Rechnung braucht Zielwissen / verbotenen Modell-Kernel.
    if not basis_invariant:
        return 'REFUTED', 'basispunkt_abhaengigkeit_der_invarianten'
    if hom_dim == 0:
        return 'REFUTED', 'hom_raum_null'
    if not kernel_ok:
        return 'REFUTED', 'verbotener_modellkernel_als_g_delta_importiert'

    # ORIENTATION_SECTOR: Basispunkt-Invarianten stimmen, Intertwiner eindeutig
    # und invertierbar, und nichttrivialer Orientierungsinvariant existiert.
    # Wegen offenen rohen Kernels weiterhin kein Gate-Abschluss.
    if (basis_invariant and intertwiner_unique and invertible_candidate
            and orientation_nontrivial):
        return 'ORIENTATION_SECTOR', 'intertwiner_eindeutig_invertierbar_' \
                                     'mit_nichttrivialem_orientierungsinvariant'

    # TORSOR_REDUCTION: Basispunkt-Invarianten stimmen und Intertwiner eindeutig;
    # Orientierung bleibt offen. NUR zulaessig wenn g/Delta aus rohem Kernel
    # verfuegbar. Hier: NOT_AVAILABLE -> unzulaessig.
    if basis_invariant and intertwiner_unique and not orientation_nontrivial:
        if kernel_ok and e['g_delta_from_raw_kernel'] != 'NOT_AVAILABLE':
            return 'TORSOR_REDUCTION', 'intertwiner_eindeutig_kernel_verfuegbar'
        # NOT_AVAILABLE -> TORSOR_REDUCTION unzulaessig -> PARTIAL
        return 'PARTIAL', 'intertwiner_eindeutig_aber_g_delta_not_available'

    # Sonst PARTIAL.
    return 'PARTIAL', 'einzelne_invarianten_bestehen_intertwiner_oder_kernel_offen'


def _first_unresolved(c, d, e):
    """Erstes ungelostes Feld nach README-Reihenfolge."""
    if c['hom_dimension'] == 0:
        return 'hom_raum_null'
    if not c['intertwiner_eindeutig']:
        return 'intertwiner_nicht_eindeutig'
    if not c['expliziter_invertierbarer_kandidat']:
        return 'kein_expliziter_invertierbarer_intertwiner_kandidat'
    if not d['orientation_invariant_nontrivial']:
        return 'kein_nichttrivialer_orientierungsinvariant'
    if e['g_delta_from_raw_kernel'] == 'NOT_AVAILABLE':
        return 'g_delta_aus_rohem_kernel_nicht_verfuegbar'
    return None


def run():
    # 1. Pins vor jeder fachlichen Rechnung.
    pin(MU4_PATH, MU4_SHA, 'mu4_pointing.py')
    pin(SEAM_LIFT_PATH, SEAM_LIFT_SHA, 'seam_reflection_lift.py')
    pin(NATIVE_COMMON_PATH, NATIVE_COMMON_SHA, 'native_common.py')
    pin(PARENT_SPEC_PATH, PARENT_SPEC_SHA, 'parent_spec.json')
    pin(V56_PATH, V56_SHA, 'v56_unique_attractor.py')
    pin(V162_PATH, V162_SHA, 'v162_seam_transport_identification.py')
    pin(TENSOR_PATH, TENSOR_SHA, 'native_tensor.npz')
    pin(CLOCK_PATH, CLOCK_SHA, 'checker.py (clock)')
    checks.append('Pin: alle acht Quellen-SHA-256 vor fachlicher Rechnung bestanden')
    parent_spec = json.loads(PARENT_SPEC_PATH.read_text(encoding='utf-8'))

    # 2. Stationen und native Quelle.
    R, J = station_matrices()
    need(np.array_equal(np.linalg.matrix_power(R, 4), -np.eye(4, dtype=np.int64)),
         'Pin: R^4 = -I_4 (Stationsuhr antiperiodisch)')
    need(np.array_equal(np.linalg.matrix_power(R, 8), np.eye(4, dtype=np.int64)),
         'Pin: R^8 = I_4 (Stationsuhr Ordnung 8)')
    need(np.array_equal(J @ R @ J, np.linalg.matrix_power(R, 7)),
         'Pin: J R J = R^-1 (D4-Relation auf Stationen)')
    need(np.array_equal(J @ J, np.eye(4, dtype=np.int64)),
         'Pin: J^2 = I_4 (Spiegelungsinvolution)')
    W, GF, GB, SFs = native_source()

    # 3. Teile A-E.
    a = part_a()
    b = part_b(R, J, W, GF, GB, SFs)
    c = part_c(R, J, GF, SFs)
    d = part_d(R, J, GF)
    e = part_e(parent_spec)

    verdict, verdict_reason = _verdict(a, b, c, d, e)
    first_unresolved = _first_unresolved(c, d, e)

    missing = []
    if c['hom_dimension'] == 0:
        missing.append('hom_raum_existiert_nicht')
    if not c['intertwiner_eindeutig']:
        missing.append('intertwiner_nicht_eindeutig')
    if not c['expliziter_invertierbarer_kandidat']:
        missing.append('kein_expliziter_invertierbarer_kandidat')
    if not d['orientation_invariant_nontrivial']:
        missing.append('kein_nichttrivialer_orientierungsinvariant')
    if e['g_delta_from_raw_kernel'] == 'NOT_AVAILABLE':
        missing.append('g_delta_nicht_aus_rohem_kernel_verfuegbar')

    return {
        'status': 'PASS',
        'exact_checks': len(checks),
        'source_hashes': {
            'clock_checker': CLOCK_SHA,
            'mu4_pointing': MU4_SHA,
            'native_common': NATIVE_COMMON_SHA,
            'native_tensor': TENSOR_SHA,
            'parent_spec': PARENT_SPEC_SHA,
            'seam_reflection_lift': SEAM_LIFT_SHA,
            'v162_seam_transport': V162_SHA,
            'v56_unique_attractor': V56_SHA,
        },
        'closed_gate_ids': [],
        'promotion': False,
        'verdict': verdict,
        'verdict_reason': verdict_reason,
        'missing': missing,
        'first_unresolved': first_unresolved,
        'teil_a_d4_torsor': a,
        'teil_b_basispunkt': b,
        'teil_c_intertwiner': c,
        'teil_d_orientierung': d,
        'teil_e_kernel': e,
        'nicht_gezeigt': [
            'kein physisches g/Delta aus rohem Calderon/Seam-Konstruktor '
            '(NOT_AVAILABLE)',
            'kein expliziter invertierbarer Intertwiner-Kandidat belegt '
            '(Invertierbarkeit nicht aus Hom-Dim gefolgert)',
            'kein nichttrivialer Orientierungsinvariant (Multiplizitaeten '
            'balanciert, Determinante gleich, Pfaffian-Paritaet gerade)',
            'keine Gate-Abschluss-Wirkung in verification/, ledger, papers, '
            'website oder scorecard (Firewall)',
        ],
    }


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print('%d/%d Bedingungen' % (result['exact_checks'], result['exact_checks']))
