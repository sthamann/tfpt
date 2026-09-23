"""Bounded exact reconstruction of the correlated two-register source channel.

The checker uses only Gaussian-integer source rays and finite F2/Gaussian
arithmetic.  It proves statements about the specified finite channel; it does
not identify a physical TFPT clock, Hamiltonian, carrier space, or continuum.
"""
from __future__ import annotations

import hashlib
import itertools as it
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
PASTED = HERE / "submitted_text.txt"
EXPECTED_SHA256 = {
    str(PASTED): "ea5fb684af779a8effa0adb83e43cebb624280442caa50e716e44cc20daccded",
    str(REPO / "verification/v774_arf_spinor_compiler.py"): "3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c",
    str(REPO / "verification/v783_two_qubit_clifford.py"): "8f4851634b83f61671b04f3a6211059c40758d21caaf1f779302c799e1e9d6c4",
    str(REPO / "experiments/theory-contracts/compiler-quartic-holonomy-20260919/checker.py"): "4b8f4aea13350d0b76121dbf2e2b5e87c019d96446b0077c7f9ac47949c80e9d",
    str(REPO / "experiments/theory-contracts/compiler-quartic-carry-20260919/core.py"): "f5b724a04ff535f080d39a014627845d83810f32361adc1721fc97a4d40132d9",
}

checks: list[str] = []


def require(ok: bool, name: str) -> None:
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def canonical_mu4(z: np.ndarray) -> tuple[tuple[int, int], ...]:
    keys = []
    for phase in (1, 1j, -1, -1j):
        w = phase * z
        require(np.array_equal(w.real, np.rint(w.real)), "Gaussian real coordinate")
        require(np.array_equal(w.imag, np.rint(w.imag)), "Gaussian imaginary coordinate")
        keys.append(tuple((int(a.real), int(a.imag)) for a in w))
    return min(keys)


def source_rays() -> list[np.ndarray]:
    supports = [tuple(sorted((2*i, 2*i+1, 2*j, 2*j+1)))
                for i, j in it.combinations(range(4), 2)]
    supports += [tuple(2*k+d[k] for k in range(4))
                 for d in it.product((0, 1), repeat=4) if sum(d) % 2 == 0]
    roots = []
    for k, sign in it.product(range(8), (-1, 1)):
        x = [0]*8
        x[k] = 2*sign
        roots.append(x)
    for support in supports:
        for signs in it.product((-1, 1), repeat=4):
            x = [0]*8
            for k, sign in zip(support, signs):
                x[k] = sign
            roots.append(x)
    require(len({tuple(x) for x in roots}) == 240, "240 Gaussian-code roots")
    keys = sorted({canonical_mu4(np.array(x[::2]) + 1j*np.array(x[1::2])) for x in roots})
    require(len(keys) == 60, "60 mu4 rays")
    return [np.array([complex(a, b) for a, b in key], dtype=np.complex128) for key in keys]


I2 = np.eye(2, dtype=np.complex128)
X2 = np.array([[0, 1], [1, 0]], dtype=np.complex128)
Y2 = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
Z2 = np.diag([1, -1]).astype(np.complex128)


def pauli_from_bits(v: tuple[int, int, int, int]) -> np.ndarray:
    x1, z1, x2, z2 = v
    one = {(0, 0): I2, (1, 0): X2, (0, 1): Z2, (1, 1): Y2}
    return np.kron(one[x1, z1], one[x2, z2])


V4 = list(it.product((0, 1), repeat=4))
PAULIS = [pauli_from_bits(v) for v in V4]
SYMMETRIC_BITS = [v for v in V4 if (v[0]*v[1] + v[2]*v[3]) % 2 == 0]
SYMMETRIC_PAULIS = [pauli_from_bits(v) for v in SYMMETRIC_BITS]


def phase_match(a: np.ndarray, targets: list[np.ndarray], scale: int) -> tuple[int, complex]:
    for j, b in enumerate(targets):
        for phase in (1, 1j, -1, -1j):
            if np.array_equal(a, scale*phase*b):
                return j, phase
    raise RuntimeError("no exact phase match")


def symp(v: tuple[int, ...], w: tuple[int, ...]) -> int:
    return (v[0]*w[1] + v[1]*w[0] + v[2]*w[3] + v[3]*w[2]) % 2


def q0(v: tuple[int, ...]) -> int:
    return (v[0]*v[1] + v[2]*v[3]) % 2


def q_u(u: tuple[int, ...], v: tuple[int, ...]) -> int:
    return (q0(v) + symp(v, u)) % 2


ODD_FORMS = [u for u in V4 if q0(u) == 1]


def reflection_actions(rays: list[np.ndarray]):
    bell = []
    six = []
    symp_maps = []
    for z in rays:
        r2 = 2*np.eye(4, dtype=np.complex128) - np.outer(z, z.conj())
        require(np.array_equal(r2 @ r2, 4*np.eye(4)), "native reflection involution")
        U = np.zeros((10, 10), dtype=np.complex128)
        for a, p in enumerate(SYMMETRIC_PAULIS):
            b, phase = phase_match(r2 @ p @ r2.T, SYMMETRIC_PAULIS, 4)
            U[b, a] = phase
        require(np.array_equal(U.conj().T @ U, np.eye(10)), "Bell10 monomial unitary")
        require(np.array_equal(U @ U, np.eye(10)), "Bell10 reflection involution")
        bell.append(U)

        image = {}
        for v, p in zip(V4, PAULIS):
            j, _phase = phase_match(r2 @ p @ r2.conj().T, PAULIS, 4)
            image[v] = V4[j]
        require(len(set(image.values())) == 16, "symplectic Pauli permutation")
        require(all(symp(image[v], image[w]) == symp(v, w) for v in V4 for w in V4),
                "Pauli action preserves symplectic form")
        inverse = {w: v for v, w in image.items()}
        perm6 = []
        for u in ODD_FORMS:
            vals = tuple(q_u(u, inverse[v]) for v in V4)
            hits = [j for j, u2 in enumerate(ODD_FORMS)
                    if vals == tuple(q_u(u2, v) for v in V4)]
            require(len(hits) == 1, "odd quadratic-form action")
            perm6.append(hits[0])
        require(sum(int(i != j) for i, j in enumerate(perm6)) == 6 and
                all(perm6[perm6[i]] == i for i in range(6)),
                "each native reflection is a triple transposition on six odd forms")
        six.append(tuple(perm6))
        symp_maps.append(image)
    require(len(set(six)) == 15 and all(six.count(p) == 4 for p in set(six)),
            "15 synthemes with four native lifts each")
    return bell, six, symp_maps


def verify_projective_three_design(rays: list[np.ndarray]) -> None:
    """Check M_t=P_sym/dim Sym^t exactly for t=1,2,3."""
    for degree in (1, 2, 3):
        words = list(it.product(range(4), repeat=degree))
        wi = {w: i for i, w in enumerate(words)}
        sym_sum = np.zeros((4**degree, 4**degree), dtype=np.complex128)
        for j, w in enumerate(words):
            for perm in it.permutations(range(degree)):
                sym_sum[wi[tuple(w[k] for k in perm)], j] += 1
        moment = np.zeros_like(sym_sum)
        for z in rays:
            v = np.array([1], dtype=np.complex128)
            for _ in range(degree):
                v = np.kron(v, z)
            moment += np.outer(v, v.conj())
        lhs = moment*int(sp.binomial(3+degree, degree))*int(sp.factorial(degree))
        rhs = 60*(4**degree)*sym_sum
        require(np.array_equal(lhs, rhs), f"native exact complex projective {degree}-design moment")


def outer_mark_action(raw_six: list[tuple[int, ...]]):
    """Construct the classical S6 outer duality from synthemes and pentads."""
    duads = [tuple(x) for x in it.combinations(range(6), 2)]
    synthemes = set()
    for a in it.permutations(range(6)):
        pairs = tuple(sorted((tuple(sorted(a[0:2])), tuple(sorted(a[2:4])), tuple(sorted(a[4:6])))))
        synthemes.add(pairs)
    synthemes = sorted(synthemes)
    require(len(duads) == 15 and len(synthemes) == 15, "15 duads and 15 synthemes")
    pentads = []
    for five in it.combinations(synthemes, 5):
        used = [d for s in five for d in s]
        if len(set(used)) == 15:
            pentads.append(tuple(sorted(five)))
    require(len(pentads) == 6, "six Sylvester pentads")
    pi = {p: i for i, p in enumerate(pentads)}

    def act_duad(d, p):
        return tuple(sorted((p[d[0]], p[d[1]])))

    def act_syntheme(s, p):
        return tuple(sorted(act_duad(d, p) for d in s))

    outer = []
    for p in raw_six:
        po = tuple(pi[tuple(sorted(act_syntheme(s, p) for s in pentad))] for pentad in pentads)
        require(sum(int(i != j) for i, j in enumerate(po)) == 2,
                "outer duality sends syntheme reflection to one transposition")
        outer.append(po)
    require(len(set(outer)) == 15 and all(outer.count(p) == 4 for p in set(outer)),
            "outer action has 15 transpositions with four lifts")
    return outer, pentads


def bell_permutation(U: np.ndarray) -> tuple[int, ...]:
    return tuple(int(np.flatnonzero(U[:, a])[0]) for a in range(10))


def canonical_partition(block: tuple[int, ...]) -> tuple[int, ...]:
    a = tuple(sorted(block))
    b = tuple(i for i in range(6) if i not in a)
    return min(a, b)


PARTITIONS = sorted({canonical_partition(s) for s in it.combinations(range(6), 3)})


def act_partition(part: tuple[int, ...], perm6: tuple[int, ...]) -> tuple[int, ...]:
    return canonical_partition(tuple(perm6[i] for i in part))


def find_bell_partition_intertwiner(bell: list[np.ndarray], six: list[tuple[int, ...]]):
    gens = []
    seen = set()
    for U, p6 in zip(bell, six):
        key = p6
        if key not in seen:
            seen.add(key)
            gens.append((bell_permutation(U), p6))
    for p0 in PARTITIONS:
        mapping = {0: p0}
        todo = [0]
        ok = True
        while todo and ok:
            b = todo.pop()
            p = mapping[b]
            for pb, p6 in gens:
                b2 = pb[b]
                p2 = act_partition(p, p6)
                if b2 in mapping and mapping[b2] != p2:
                    ok = False
                    break
                if b2 not in mapping:
                    mapping[b2] = p2
                    todo.append(b2)
        if ok and len(mapping) == 10 and len(set(mapping.values())) == 10:
            if all(mapping[pb[b]] == act_partition(mapping[b], p6)
                   for pb, p6 in gens for b in range(10)):
                return mapping
    raise RuntimeError("no Bell10 <-> 3+3 partition intertwiner")


def superoperator_integer(unitaries: list[np.ndarray]) -> np.ndarray:
    n = len(unitaries[0])
    out = np.zeros((n*n, n*n), dtype=np.complex128)
    for U in unitaries:
        out += np.kron(U.conj(), U)
    require(np.array_equal(out.real, np.rint(out.real)) and
            np.array_equal(out.imag, np.rint(out.imag)), "integer Gaussian superoperator")
    return out


def exact_complex_rank(a: np.ndarray) -> int:
    rows = [[sp.Integer(int(round(v.real))) + sp.I*sp.Integer(int(round(v.imag))) for v in row]
            for row in a]
    return int(sp.polys.matrices.DomainMatrix.from_list_sympy(len(rows), len(rows[0]), rows)
               .convert_to(sp.QQ_I).rank())


def rank_mod_p(a: np.ndarray, prime: int = 5, sqrt_minus_one: int = 2) -> int:
    m = (np.rint(a.real).astype(object) + sqrt_minus_one*np.rint(a.imag).astype(object)) % prime
    m = [[int(v) for v in row] for row in m]
    rows, cols = len(m), len(m[0])
    rank = 0
    for c in range(cols):
        pivot = next((r for r in range(rank, rows) if m[r][c] % prime), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        inv = pow(m[rank][c] % prime, -1, prime)
        m[rank] = [(v*inv) % prime for v in m[rank]]
        for r in range(rows):
            if r != rank and m[r][c] % prime:
                f = m[r][c] % prime
                m[r] = [(x-f*y) % prime for x, y in zip(m[r], m[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def marked_data(mark: int, bell: list[np.ndarray], six: list[tuple[int, ...]], mapping):
    idx = [k for k, p in enumerate(six) if p[mark] != mark]
    require(len(idx) == 20, f"mark {mark}: selected 20 lifts")
    counts = np.zeros((10, 10), dtype=int)
    for k in idx:
        p = bell_permutation(bell[k])
        for a, b in enumerate(p):
            counts[b, a] += 1
    require(sorted(set(counts.ravel())) == [0, 4, 8], f"mark {mark}: transition counts")
    require(np.array_equal(np.diag(counts), 8*np.ones(10, dtype=int)), f"mark {mark}: eight self events")
    A = (counts == 4).astype(int)
    require(np.array_equal(A, A.T) and np.all(A.sum(axis=0) == 3), f"mark {mark}: cubic adjacency")
    require(np.array_equal(A@A, 2*np.eye(10, dtype=int)-A+np.ones((10, 10), dtype=int)),
            f"mark {mark}: Petersen identity")

    # The explicit mark readout turns each 3+3 partition into a duad of the other five.
    others = [i for i in range(6) if i != mark]
    duads = {}
    for b, part in mapping.items():
        side = set(part)
        if mark not in side:
            side = set(range(6))-side
        duads[b] = tuple(sorted(side-{mark}))
    require(len(set(duads.values())) == 10 and all(set(d).issubset(others) for d in duads.values()),
            f"mark {mark}: Bell labels biject to five-point duads")
    for a, b in it.product(range(10), repeat=2):
        expected = int(a != b and set(duads[a]).isdisjoint(duads[b]))
        require(A[b, a] == expected, f"mark {mark}: adjacency is duad disjointness {a},{b}")

    # Quantum stay/jump instruments.  D_S(l) selects labels fixed by l.
    n = 10
    S = np.zeros((n*n, n*n), dtype=np.complex128)
    J = np.zeros_like(S)
    C = superoperator_integer([bell[k] for k in idx])
    fixed_phase_global = []
    for k in idx:
        U = bell[k]
        perm = bell_permutation(U)
        ds = np.diag([int(perm[a] == a) for a in range(n)]).astype(np.complex128)
        dj = np.eye(n)-ds
        Ks, Kj = U@ds, U@dj
        S += np.kron(Ks.conj(), Ks)
        J += np.kron(Kj.conj(), Kj)
        fixed = [a for a in range(n) if perm[a] == a]
        phases = [U[a, a] for a in fixed]
        require(len(fixed) == 4 and len(set(phases)) == 1,
                f"mark {mark}: each no-jump event has one global phase on its fixed four-space")
        fixed_phase_global.append((int(round(phases[0].real)), int(round(phases[0].imag))))
    instrument_equals_channel = np.array_equal(S+J, C)
    require(instrument_equals_channel, f"mark {mark}: stay/jump monitoring sums exactly to C20")
    require(not np.any(C.imag), f"mark {mark}: C20 is real in the Bell basis")
    c_roots = (20, 12, 4, -4, 0)
    c_int = np.rint(C.real).astype(np.int64)
    c_poly = np.eye(100, dtype=np.int64)
    for root in c_roots:
        c_poly = c_poly@(c_int-root*np.eye(100, dtype=np.int64))
    require(not np.any(c_poly), f"mark {mark}: C20 spectral polynomial")
    c_traces = [int(np.trace(np.linalg.matrix_power(c_int, k))) for k in range(5)]
    c_vand = sp.Matrix([[r**k for r in c_roots] for k in range(5)])
    c_mult = [int(v) for v in c_vand.inv()*sp.Matrix(c_traces)]
    require(c_mult == [1, 5, 75, 15, 4], f"mark {mark}: C20 exact spectrum multiplicities")
    effect_s = np.zeros((n, n), dtype=np.complex128)
    effect_j = np.zeros_like(effect_s)
    for k in idx:
        U = bell[k]
        perm = bell_permutation(U)
        ds = np.diag([int(perm[a] == a) for a in range(n)]).astype(np.complex128)
        dj = np.eye(n)-ds
        effect_s += (U@ds).conj().T@(U@ds)
        effect_j += (U@dj).conj().T@(U@dj)
    require(np.array_equal(effect_s, 8*np.eye(n)) and np.array_equal(effect_j, 12*np.eye(n)),
            f"mark {mark}: stay/jump effects 2/5 and 3/5")

    # Exact operator-basis action.  No-jump phases are global per event and
    # cancel in conjugation; the coherence filtering comes from incidence.
    for a, b in it.product(range(10), repeat=2):
        col = a + 10*b  # column-major vec(E_ab)
        overlap = len(set(duads[a]) & set(duads[b]))
        expected_s = np.zeros(100, dtype=np.complex128)
        expected_s[col] = 4*overlap
        require(np.array_equal(S[:, col], expected_s),
                f"mark {mark}: S(E_{a}{b})=4|e cap f| E_{a}{b}")
        if a != b and overlap == 1:
            expected_c = np.zeros(100, dtype=np.complex128)
            expected_c[col] = 4
            require(np.array_equal(C[:, col], expected_c),
                    f"mark {mark}: C20 intersecting offdiagonal E_{a}{b}/5")
        if overlap == 0:
            swap = b + 10*a
            nz = np.flatnonzero(C[:, col])
            require(len(nz) == 1 and int(nz[0]) == swap and abs(C[swap, col]) == 4,
                    f"mark {mark}: C20 disjoint offdiagonal transpose with phase E_{a}{b}")

    # Stopped first-jump channel Phi=J(I-S)^-1.  With unnormalised integer
    # S,J this is J(20I-S)^-1.  Scale by 240 to keep an integer certificate.
    sdiag = np.diag(S).real.astype(int)
    require(np.array_equal(S, np.diag(sdiag)), f"mark {mark}: S diagonal in Bell matrix units")
    den = 20-sdiag
    require(set(den.tolist()) == {12, 16, 20}, f"mark {mark}: stopped denominators 12,16,20")
    T = J @ np.diag(240//den)
    require(np.array_equal(T.real, np.rint(T.real)) and np.array_equal(T.imag, np.rint(T.imag)),
            f"mark {mark}: 240 Phi Gaussian integer")
    require(not np.any(T.imag), f"mark {mark}: 240 Phi real")
    roots = (240, 80, -160, 0, 48, -48)
    t_int = np.rint(T.real).astype(object)
    poly = np.eye(100, dtype=object)
    for root in roots:
        poly = poly@(t_int-root*np.eye(100, dtype=object))
    require(not np.any(poly), f"mark {mark}: stopped-channel spectral polynomial")
    trace_moments = [int(np.trace(np.linalg.matrix_power(t_int, k))) for k in range(6)]
    vand = sp.Matrix([[r**k for r in roots] for k in range(6)])
    stopped_mult = [int(v) for v in vand.inv()*sp.Matrix(trace_moments)]
    require(stopped_mult == [1, 5, 4, 60, 15, 15],
            f"mark {mark}: stopped-channel multiplicities")
    return (idx, counts, A, S, J, C, instrument_equals_channel,
            {"global_phase_counts": {str(k): fixed_phase_global.count(k) for k in sorted(set(fixed_phase_global))},
             "coherence_action": "S(E_ef)=|e intersection f|/5 E_ef; phases are global per event"},
            stopped_mult, c_mult)


def main(out=None):
    checks.clear()
    for path, digest in EXPECTED_SHA256.items():
        require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, "source pin " + path)

    rays = source_rays()
    verify_projective_three_design(rays)
    bell, raw_six, _ = reflection_actions(rays)
    six, pentads = outer_mark_action(raw_six)
    mapping = find_bell_partition_intertwiner(bell, six)
    require(all(mapping[bell_permutation(U)[b]] == act_partition(mapping[b], p6)
                for U, p6 in zip(bell, six) for b in range(10)),
            "all 60 events intertwine Bell10 and 3+3 partitions")

    S60 = superoperator_integer(bell)
    require(np.array_equal(S60, S60.conj().T), "C60 superoperator self-adjoint")
    eye100 = np.eye(100, dtype=np.complex128)
    poly = (S60-60*eye100)@(S60-20*eye100)@(S60-12*eye100)@(S60-4*eye100)
    require(np.array_equal(poly, np.zeros_like(poly)), "C60 exact minimal-polynomial divisibility")
    traces = [int(round(np.trace(np.linalg.matrix_power(S60, k)).real)) for k in range(4)]
    M = sp.Matrix([[1, 1, 1, 1], [60, 20, 12, 4],
                   [60**2, 20**2, 12**2, 4**2], [60**3, 20**3, 12**3, 4**3]])
    mult = [int(v) for v in M.inv()*sp.Matrix(traces)]
    require(mult == [1, 9, 45, 45], "C60 spectrum multiplicities 1,9,45,45")

    flat = np.array([U.reshape(-1) for U in bell])
    kraus_rank = exact_complex_rank(flat)
    require(kraus_rank == 55, "C60 Kraus span rank 55")
    products = np.array([(u@v).reshape(-1) for u in bell for v in bell])
    product_rank_mod5 = rank_mod_p(products)
    require(product_rank_mod5 == 100, "two-step products span M10 exactly (full rank mod 5 witness)")

    # Native |00,00> return uses r_00^4; r2=2r makes the denominator 16.
    source_num = 0
    for z in rays:
        r2 = 2*np.eye(4)-np.outer(z, z.conj())
        source_num += int(round(abs(r2[0, 0]**2)**2))
    native_return = Fraction(source_num, 60*16)
    require(native_return == Fraction(3, 10), "native correlated e0 return 3/10")
    # Haar C^4: x=|z_0|^2 has E[x^k]=6 k!/(k+3)!.
    moments = [Fraction(1, 1), Fraction(1, 4), Fraction(1, 10), Fraction(1, 20), Fraction(1, 35)]
    isotropic_return = sum(Fraction(((-2)**k)*sp.binomial(4, k))*moments[k] for k in range(5))
    require(isotropic_return == Fraction(9, 35), "isotropic correlated e0 return 9/35")
    require(native_return-isotropic_return == Fraction(3, 70), "fourth-moment return excess 3/70")

    marked = []
    for mark in range(6):
        idx, counts, A, S, J, C, same, witness, stopped_mult, c20_mult = marked_data(mark, bell, six, mapping)
        marked.append({
            "mark": mark,
            "selected_ray_indices": idx,
            "counts": counts.tolist(),
            "petersen_adjacency": A.tolist(),
            "instrument_equals_unmonitored_C20": bool(same),
            "c20_spectrum": {"1": 1, "3/5": 5, "1/5": 75, "-1/5": 15, "0": 4},
            "no_jump_phase_witness": witness,
            "stopped_channel_spectrum": {"1": 1, "1/3": 5, "-2/3": 4,
                                          "0": 60, "1/5": 15, "-1/5": 15},
            "six_jump_spectrum": {"1": 1, "1/729": 5, "64/729": 4,
                                   "0": 60, "1/15625": 30},
            "c20_kraus_rank": exact_complex_rank(np.array([bell[k].reshape(-1) for k in idx])),
        })
        require(marked[-1]["c20_kraus_rank"] == 20, f"mark {mark}: C20 Kraus rank 20")

    # The determinant-cleaned lift \tilde r=e^{-i pi/4}r multiplies Sym2(r) by -i.
    # Hence conjugation channels and all fixed-length coherent products are unchanged
    # (the latter only by one common global phase).
    result = {
        "scope": "exact finite correlated reflection channel; no physical clock, Hamiltonian, carrier identification, continuum, or TOE claim",
        "source_sha256": EXPECTED_SHA256,
        "source_rays": 60,
        "projective_design_moments_exact": [1, 2, 3],
        "bell_dimension": 10,
        "bell_partition_intertwiner": {str(k): list(v) for k, v in sorted(mapping.items())},
        "outer_mark_pentads": [[[list(d) for d in s] for s in p] for p in pentads],
        "c60_spectrum": {"1": 1, "1/3": 9, "1/5": 45, "1/15": 45},
        "c60_integer_trace_moments_k0_to_k3": traces,
        "c60_kraus_rank": kraus_rank,
        "two_step_span_rank": product_rank_mod5,
        "native_e0_return": str(native_return),
        "isotropic_e0_return": str(isotropic_return),
        "return_excess": str(native_return-isotropic_return),
        "marked_channels": marked,
        "lift_boundary": "tilde r=exp(-i*pi/4)r gives Sym2(tilde r)=-i Sym2(r); homogeneous paired channels cannot detect this lift",
        "representation_boundary": "the Bell10 ray permutation can match the 3+3/duad action without a linear equivariant identification with the separate carrier-edge 10-space",
        "checks_passed": len(checks),
    }
    (Path(out) if out is not None else HERE/"source_certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: result[k] for k in ("source_rays", "bell_dimension", "c60_spectrum",
          "c60_kraus_rank", "two_step_span_rank", "native_e0_return", "isotropic_e0_return",
          "return_excess", "checks_passed")}, indent=2))

    return result


if __name__ == "__main__":
    main()
