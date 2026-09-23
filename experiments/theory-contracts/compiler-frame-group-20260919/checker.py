"""Exact finite group audit for the 40-event recorded reference frame.

This determines the phase-faithful Bell10 group, its action kernel and quotient,
and tests an explicit W(D5)=2^4:S5 identification.  It does not identify the
Bell10 representation with the native carrier-edge representation.
"""
from __future__ import annotations

import importlib.util
import argparse
import itertools as it
import json
import hashlib
from collections import Counter, deque
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SOURCE_PINS = {
    "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py": "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    "experiments/theory-contracts/compiler-quartic-carry-20260919/core.py": "f5b724a04ff535f080d39a014627845d83810f32361adc1721fc97a4d40132d9",
    "experiments/theory-contracts/compiler-quartic-carry-20260919/PROOF.txt": "e38c31499b54bab617e9242eb3056b0d298d5176a164b7c56095fc4977b6048a",
    "verification/v783_two_qubit_clifford.py": "8f4851634b83f61671b04f3a6211059c40758d21caaf1f779302c799e1e9d6c4"
}
spec = importlib.util.spec_from_file_location("frame_source_channel", SOURCE)
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)
checks = []


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


PHASE_EXP = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}


def encode_matrix(U):
    p, e = [], []
    for a in range(10):
        nz = np.flatnonzero(U[:, a])
        require(len(nz) == 1, "Bell10 matrix monomial")
        b = int(nz[0])
        v = U[b, a]
        key = (int(round(v.real)), int(round(v.imag)))
        require(key in PHASE_EXP, "Bell10 phase in mu4")
        p.append(b)
        e.append(PHASE_EXP[key])
    require(len(set(p)) == 10, "Bell10 monomial permutation")
    return tuple(p), tuple(e)


ID = (tuple(range(10)), (0,)*10)


def mul(A, B):
    """Matrix product A B for column-action monomial encodings."""
    pa, ea = A
    pb, eb = B
    return (tuple(pa[pb[j]] for j in range(10)),
            tuple((eb[j]+ea[pb[j]]) % 4 for j in range(10)))


def inv(A):
    p, e = A
    q, f = [0]*10, [0]*10
    for a in range(10):
        q[p[a]] = a
        f[p[a]] = (-e[a]) % 4
    return tuple(q), tuple(f)


def power(A, n):
    out = ID
    for _ in range(n):
        out = mul(A, out)
    return out


def order(A, limit=240):
    out = ID
    for n in range(1, limit+1):
        out = mul(A, out)
        if out == ID:
            return n
    raise RuntimeError("element order exceeds bound")


def perm_mul(a, b):
    return tuple(a[b[j]] for j in range(len(a)))


def signed5_mul(A, B):
    pa, ea = A
    pb, eb = B
    return (tuple(pa[pb[j]] for j in range(5)),
            tuple(eb[j] ^ ea[pb[j]] for j in range(5)))


def signed5_order(A):
    identity = (tuple(range(5)), (0,)*5)
    x = identity
    for n in range(1, 121):
        x = signed5_mul(A, x)
        if x == identity:
            return n
    raise RuntimeError("signed permutation order exceeds bound")


def closure(generators, outer_generators):
    outer_id = tuple(range(6))
    outer = {ID: outer_id}
    queue = deque([ID])
    while queue:
        g = queue.popleft()
        og = outer[g]
        for h, oh in zip(generators, outer_generators):
            x = mul(h, g)
            ox = perm_mul(oh, og)
            if x in outer:
                require(outer[x] == ox, "outer action well-defined on phase-faithful group")
            else:
                outer[x] = ox
                queue.append(x)
    return outer


def generated_subgroup(generators):
    seen = {ID}
    queue = deque([ID])
    while queue:
        g = queue.popleft()
        for h in generators:
            x = mul(h, g)
            if x not in seen:
                seen.add(x)
                queue.append(x)
    return seen


def f2_rank(vectors):
    pivots = {}
    for x in vectors:
        y = x
        while y:
            p = y.bit_length()-1
            if p in pivots:
                y ^= pivots[p]
            else:
                pivots[p] = y
                break
    return len(pivots)


def standard_even_action(tau, x):
    """S5 action on even sign vectors, coordinates x0..x3 and x4=sum."""
    bits = [(x >> i) & 1 for i in range(4)]
    bits.append(sum(bits) % 2)
    out5 = [0]*5
    for i in range(5):
        out5[tau[i]] = bits[i]
    require(sum(out5) % 2 == 0, "even-sign module preserved")
    return sum(out5[i] << i for i in range(4))


def gl4_matrices():
    for cols in it.product(range(16), repeat=4):
        if f2_rank(cols) == 4:
            yield cols


def lin_apply(cols, x):
    y = 0
    for i in range(4):
        if (x >> i) & 1:
            y ^= cols[i]
    return y


def lin_comp(A, B):
    return tuple(lin_apply(A, B[i]) for i in range(len(B)))


def perm_sign_on_points(p6, points):
    p = [points.index(p6[x]) for x in points]
    inversions = sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5))
    return inversions % 2


def perm_subgroup(generators):
    identity = tuple(range(6))
    seen = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            x = perm_mul(h, g)
            if x not in seen:
                seen.add(x)
                queue.append(x)
    return seen


def main(out):
    for rel, digest in SOURCE_PINS.items():
        require(hashlib.sha256((REPO/rel).read_bytes()).hexdigest() == digest, "source pin " + rel)
    rays = src.source_rays()
    bell, raw, _ = src.reflection_actions(rays)
    six, _ = src.outer_mark_action(raw)
    mark = 0
    background_idx = [k for k, p in enumerate(six) if p[mark] == mark]
    require(len(background_idx) == 40, "fixed-mark background has 40 reflections")
    generators = [encode_matrix(bell[k]) for k in background_idx]
    outer_generators = [six[k] for k in background_idx]
    group_outer = closure(generators, outer_generators)
    group = set(group_outer)
    group_order = len(group)

    scalar = [g for g in group if g[0] == tuple(range(10)) and len(set(g[1])) == 1]
    center = [g for g in group if all(mul(g, h) == mul(h, g) for h in generators)]
    outer_image = set(group_outer.values())
    outer_id = tuple(range(6))
    kernel_h = [g for g, o in group_outer.items() if o == outer_id]
    require(group_order == 3840, "phase-faithful background group order 3840")
    require(len(scalar) == 2 and ID in scalar, "phase-faithful scalar kernel C2")
    central_sign = next(g for g in scalar if g != ID)
    require(central_sign == (tuple(range(10)), (2,)*10), "nontrivial scalar is -I10")
    require(set(center) == set(scalar), "phase-faithful center is {+I,-I}")
    require(len(outer_image) == 120 and all(p[mark] == mark for p in outer_image), "outer quotient is full S5")
    require(len(kernel_h) == 32, "phase-faithful outer kernel order 32")
    require(all(order(k) in (1, 2) for k in kernel_h), "phase-faithful outer kernel exponent two")
    require(all(mul(a, b) == mul(b, a) for a in kernel_h for b in kernel_h), "phase-faithful outer kernel abelian")

    # Find a genuine S5 Coxeter complement already in the phase-faithful group.
    points = [i for i in range(6) if i != mark]
    target_outer = []
    for i in range(4):
        p = list(range(6))
        p[points[i]], p[points[i+1]] = p[points[i+1]], p[points[i]]
        target_outer.append(tuple(p))
    fibers = [[g for g, o in group_outer.items() if o == p and order(g) == 2] for p in target_outer]
    require(all(len(f) > 0 for f in fibers), "each adjacent S5 transposition has involutive lifts")
    solution = None

    def search(path):
        nonlocal solution
        if solution is not None:
            return
        j = len(path)
        if j == 4:
            solution = list(path)
            return
        for g in fibers[j]:
            ok = True
            for i, h in enumerate(path):
                wanted = 3 if j == i+1 else 2
                if order(mul(h, g)) != wanted:
                    ok = False
                    break
            if ok:
                search(path+[g])
    search([])
    require(solution is not None, "phase-faithful S5 Coxeter section exists")
    complement = generated_subgroup(solution)
    require(len(complement) == 120, "Coxeter lifts generate complement S5 of order 120")
    require(set(complement) & set(kernel_h) == {ID}, "S5 complement intersects phase kernel trivially")
    require(len({mul(k, s) for k in kernel_h for s in complement}) == 3840, "C2^5 times S5 covers phase group")

    # Conjugation fingerprint of the phase kernel.  Apart from identity and
    # central -I, the chosen S5 complement has two 15-element orbits.
    unused = set(kernel_h)-{ID}
    kernel_orbits = []
    while unused:
        k = next(iter(unused))
        orbit = {mul(mul(s, k), inv(s)) for s in complement}
        kernel_orbits.append(orbit)
        unused -= orbit
    orbit_signature_h = sorted(len(o) for o in kernel_orbits)
    require(orbit_signature_h == [1, 15, 15], "phase-kernel S5 orbit signature 1+15+15")

    complement_by_outer = {group_outer[s]: s for s in complement}
    require(len(complement_by_outer) == 120, "phase S5 complement maps bijectively to outer S5")

    # Projectivize by the scalar center.
    def canon(g):
        return min(g, mul(central_sign, g))
    def pmul(a, b):
        return canon(mul(a, b))
    def pinv(a):
        return canon(inv(a))
    projective = {canon(g) for g in group}
    require(len(projective) == 1920, "projective background group order 1920")
    projective_outer = {}
    for g, o in group_outer.items():
        c = canon(g)
        if c in projective_outer:
            require(projective_outer[c] == o, "outer action descends projectively")
        projective_outer[c] = o
    kernel_p = [g for g, o in projective_outer.items() if o == outer_id]
    require(len(kernel_p) == 16, "projective outer kernel order 16")
    require(all(pmul(a, b) == pmul(b, a) for a in kernel_p for b in kernel_p), "projective kernel C2^4 abelian")
    require(all(pmul(k, k) == ID for k in kernel_p), "projective kernel exponent two")
    complement_p = {canon(s) for s in complement}
    require(len(complement_p) == 120 and set(complement_p) & set(kernel_p) == {ID}, "projective extension splits over S5")
    complement_p_by_outer = {projective_outer[s]: s for s in complement_p}
    unused_p = set(kernel_p)-{ID}
    kernel_orbits_p = []
    while unused_p:
        k = next(iter(unused_p))
        orbit = {pmul(pmul(s, k), pinv(s)) for s in complement_p}
        kernel_orbits_p.append(orbit)
        unused_p -= orbit
    orbit_signature_p = sorted(len(o) for o in kernel_orbits_p)
    require(orbit_signature_p == [15], "projective S5 is transitive on all 15 nonzero kernel vectors")

    # Positive identification of the transitive module as F4^2 semilinear.
    coord_p = {ID: 0}
    basis_p = []
    for candidate in sorted(kernel_p):
        if candidate in coord_p:
            continue
        bit = 1 << len(basis_p)
        for g, x in list(coord_p.items()):
            coord_p[pmul(candidate, g)] = x ^ bit
        basis_p.append(candidate)
    require(len(basis_p) == 4 and len(coord_p) == 16, "projective kernel coordinated as F2^4")

    def module_action(s):
        cols = []
        for k in basis_p:
            image = pmul(pmul(s, k), pinv(s))
            require(image in coord_p, "projective kernel normal in module action")
            cols.append(coord_p[image])
        return tuple(cols)

    a = pmul(canon(solution[0]), canon(solution[1]))
    b = pmul(canon(solution[2]), canon(solution[3]))
    require(len(perm_subgroup([projective_outer[a], projective_outer[b]])) == 60,
            "two even Coxeter products generate A5")
    A_actions = [module_action(a), module_action(b)]
    centralizer = []
    for X in it.product(range(16), repeat=4):
        if all(lin_comp(T, X) == lin_comp(X, T) for T in A_actions):
            centralizer.append(tuple(X))
    require(len(centralizer) == 4, "A5 module centralizer is F4 of order four")
    I4 = (1, 2, 4, 8)
    J_candidates = [X for X in centralizer if X not in ((0, 0, 0, 0), I4)
                    and tuple(lin_comp(X, X)[i] ^ X[i] for i in range(4)) == I4]
    require(len(J_candidates) == 2, "two primitive F4 scalar structures J,J^2")
    J3 = min(J_candidates)
    J3_sq = lin_comp(J3, J3)
    odd = module_action(canon(solution[0]))
    require(lin_comp(lin_comp(odd, J3), odd) == J3_sq,
            "odd S5 element applies Frobenius J -> J^2")
    require(all(perm_sign_on_points(o, points) == 0 for o in perm_subgroup([projective_outer[a], projective_outer[b]])),
            "identified A5 is the even outer subgroup")

    # W(D5)'s characteristic O2 is the even-sign module on five coordinates.
    # Its nonzero vectors have Hamming weights 2 and 4, hence S5 orbits 10+5.
    even_vectors = [bits for bits in range(32) if bits.bit_count() % 2 == 0]
    remaining = set(even_vectors)-{0}
    wd5_orbits = []
    perms5 = list(it.permutations(range(5)))
    while remaining:
        x = next(iter(remaining))
        orbit = set()
        for p in perms5:
            y = 0
            for i in range(5):
                if (x >> i) & 1:
                    y |= 1 << p[i]
            orbit.add(y)
        wd5_orbits.append(orbit)
        remaining -= orbit
    wd5_signature = sorted(len(o) for o in wd5_orbits)
    require(wd5_signature == [5, 10], "W(D5) even-sign kernel orbit signature 5+10")
    require(orbit_signature_p != wd5_signature, "projective frame group is not W(D5)")

    wd5_elements = [(tuple(p), tuple((bits >> i) & 1 for i in range(5)))
                     for p in perms5 for bits in even_vectors]
    wd5_order_hist = Counter(signed5_order(g) for g in wd5_elements)
    require(sum(wd5_order_hist.values()) == 1920, "complete W(D5) order census")

    # K is O2: every normal 2-subgroup maps to a normal 2-subgroup of S5,
    # and O2(S5)=1.  Therefore the module fingerprint is isomorphism-invariant.
    require(len(kernel_p) == 16, "projective kernel is the full normal 2-core O2")

    order_hist_phase = Counter(order(g) for g in group)
    def porder(g):
        x = ID
        for n in range(1, 241):
            x = pmul(g, x)
            if x == ID:
                return n
        raise RuntimeError("projective element order exceeds bound")
    order_hist_projective = Counter(porder(g) for g in projective)
    require(sum(order_hist_phase.values()) == 3840 and sum(order_hist_projective.values()) == 1920,
            "complete phase/projective element-order census")
    require(order_hist_projective != wd5_order_hist, "element-order census independently excludes W(D5)")

    # Full Bell observables quotient only the central scalar +/-I.
    ad_keys = set()
    for p, e in group:
        ad_keys.add((tuple(p[a]+10*p[b] for b in range(10) for a in range(10)),
                     tuple((e[a]-e[b]) % 4 for b in range(10) for a in range(10))))
    require(len(ad_keys) == 1920, "Adjoint action kernel is exactly central C2")
    classical_perms = {g[0] for g in group}
    require(len(classical_perms) == 120, "Bell-label-only frame quotient is S5")
    reflection_traces = {sum((1j)**e[j] for j in range(10) if p[j] == j)
                         for p, e in generators}
    require(reflection_traces == {4+0j}, "every background Bell reflection has trace four")
    result = {
        "research_id": "UR.COMPILER.FRAME_GROUP.14",
        "verdict": "EXACT_ORDER1920_BUT_NOT_WD5_MODULE_OBSTRUCTION",
        "fixed_outer_mark": mark,
        "background_reflections": 40,
        "phase_faithful_group_order": group_order,
        "phase_faithful_group": "C2^5 semidirect S5 with kernel orbit signature 1+15+15",
        "scalar_kernel_order_for_Ad": 2,
        "center_order": 2,
        "outer_quotient": "S5",
        "outer_quotient_order": len(outer_image),
        "phase_outer_kernel": "C2^5",
        "phase_outer_kernel_order": len(kernel_h),
        "projective_group_order": len(projective),
        "projective_outer_kernel": "C2^4",
        "projective_outer_kernel_order": len(kernel_p),
        "extension_splits": True,
        "coxeter_fiber_involution_counts": [len(f) for f in fibers],
        "coxeter_section_generators": [
            {"permutation10": list(g[0]), "phase_exponents_mod4": list(g[1])} for g in solution
        ],
        "projective_structure": "C2^4 semidirect S5 with S5 transitive on the 15 nonzero kernel vectors",
        "positive_module_identification": "C2^4 = additive F4^2; A5=SL2(4) centralizes F4 scalars and odd S5 acts by Frobenius",
        "semilinear_group_name": "F4^2 semidirect (SL2(4) semidirect Gal(F4/F2)) = ASL2(4):2",
        "F4_scalar_J_columns_in_kernel_basis": list(J3),
        "F4_scalar_J_squared_columns": list(J3_sq),
        "wd5_comparison": "NOT ISOMORPHIC: W(D5) even-sign O2 has nonzero orbit signature 5+10",
        "phase_kernel_orbit_signature": orbit_signature_h,
        "projective_kernel_orbit_signature": orbit_signature_p,
        "wd5_even_sign_orbit_signature": wd5_signature,
        "wd5_element_order_histogram": {str(k): v for k, v in sorted(wd5_order_hist.items())},
        "phase_element_order_histogram": {str(k): v for k, v in sorted(order_hist_phase.items())},
        "projective_element_order_histogram": {str(k): v for k, v in sorted(order_hist_projective.items())},
        "full_Bell_observable_Ad_kernel_order": 2,
        "full_Bell_frame_states": len(ad_keys),
        "classical_Bell_label_frame_states": len(classical_perms),
        "minimal_exact_full_observable_record": "one projective frame element: 16 kernel choices times 120 S5 choices, total 1920",
        "conditional_program_bound": "for deterministic exact correction on arbitrary independent Bell10 data, the 1920 inequivalent frame unitaries require 1920 mutually orthogonal Nielsen-Chuang program states",
        "program_bound_scope": "not a universal bound for state-specific correlated relational encodings",
        "single_background_event_normalized_Choi_overlap_with_identity": "Tr(U)/10=2/5",
        "raw_Choi_program_consequence": "the unflagged single-event Choi state is not itself a perfect deterministic frame program",
        "representation_boundary": "the projective group is not W(D5), and Bell10 is not the native carrier Lambda2(W5) representation; order 1920 is only a numerical coincidence",
        "physical_scope": "finite exact reference-frame algebra only; no physical observer, memory, clock selection, carrier identification, or TOE gate is derived",
        "source_sha256": SOURCE_PINS,
        "checks_passed": len(checks),
    }
    HERE.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: result[k] for k in ("verdict", "phase_faithful_group_order",
          "outer_quotient", "projective_group_order", "extension_splits", "wd5_comparison",
          "full_Bell_frame_states", "classical_Bell_label_frame_states", "checks_passed")}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=HERE/"certificate.json")
    main(parser.parse_args().out)
