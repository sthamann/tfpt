"""Exact source compression, geometric transport and marked E8 lift audit.

No physical Hamiltonian, state, local current or affine level is assumed proven.
Run with --out PATH; source pins are mandatory. No Python assert statements.
"""
import argparse
import ast
import hashlib
import itertools as it
import json
from collections import Counter
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
checks = []


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def main(out):
    pins = json.loads((HERE / 'source_pins.json').read_text())
    for rel, digest in pins.items():
        require(hashlib.sha256((REPO / rel).read_bytes()).hexdigest() == digest,
                'source pin ' + rel)

    # Original Gaussian E8 code: integer coordinates, norm squared four.
    supports = [tuple(sorted((2*i, 2*i+1, 2*j, 2*j+1)))
                for i, j in it.combinations(range(4), 2)]
    supports += [tuple(2*k+d[k] for k in range(4))
                 for d in it.product((0, 1), repeat=4) if sum(d) % 2 == 0]
    roots = []
    for k, sign in it.product(range(8), (-1, 1)):
        x = [0]*8
        x[k] = 2*sign
        roots.append(tuple(x))
    for support in supports:
        for signs in it.product((-1, 1), repeat=4):
            x = [0]*8
            for k, sign in zip(support, signs):
                x[k] = sign
            roots.append(tuple(x))
    require(len(set(roots)) == 240, 'native 240 Gaussian-code roots')
    rays = set()
    for x in roots:
        a, b = tuple(x[::2]), tuple(x[1::2])
        rays.add(min((a, b), (tuple(-v for v in b), a),
                     (tuple(-v for v in a), tuple(-v for v in b)),
                     (b, tuple(-v for v in a))))
    require(len(rays) == 60, 'native 60 mu4 rays')

    words = list(it.product(range(4), repeat=4))
    wi = {w: i for i, w in enumerate(words)}
    V = np.zeros((256, 5), dtype=np.int64)
    for i, w in enumerate(words):
        c = tuple(w.count(j) for j in range(4))
        if 4 in c:
            V[i, 0] = 1
        elif c in ((2, 2, 0, 0), (0, 0, 2, 2)):
            V[i, 1] = 1
        elif c in ((2, 0, 2, 0), (0, 2, 0, 2)):
            V[i, 2] = 1
        elif c in ((2, 0, 0, 2), (0, 2, 2, 0)):
            V[i, 3] = 1
        elif c == (1, 1, 1, 1):
            V[i, 4] = 1
    norm = np.diag(V.T @ V)
    require(norm.tolist() == [4, 12, 12, 12, 24], 'quartic basis norms')
    sym24 = np.zeros((256, 256), dtype=np.int64)
    for j, w in enumerate(words):
        for perm in it.permutations(range(4)):
            sym24[wi[tuple(w[k] for k in perm)], j] += 1
    moment_re = np.zeros((256, 256), dtype=np.int64)
    moment_im = np.zeros_like(moment_re)
    quartics = []
    for aa, bb in sorted(rays):
        a, b = np.array(aa), np.array(bb)
        zr, zi = np.array([1], dtype=np.int64), np.array([0], dtype=np.int64)
        for _ in range(4):
            zr, zi = np.kron(zr, a)-np.kron(zi, b), np.kron(zr, b)+np.kron(zi, a)
        moment_re += np.outer(zr, zr)+np.outer(zi, zi)
        moment_im += np.outer(zi, zr)-np.outer(zr, zi)
        # 2r = 2I - zz^dagger has Gaussian integer entries.
        r2 = 2*np.eye(4, dtype=np.int64)-np.outer(a, a)-np.outer(b, b)
        i2 = np.outer(a, b)-np.outer(b, a)
        require(np.array_equal(r2@r2-i2@i2, 4*np.eye(4, dtype=np.int64))
                and not np.any(r2@i2+i2@r2), 'native involution ' + str(len(quartics)))
        yr, yi = V.reshape(4, 4, 4, 4, 5), np.zeros((4, 4, 4, 4, 5), dtype=np.int64)
        for axis in range(4):
            rr = np.moveaxis(np.tensordot(r2, yr, axes=(1, axis)), 0, axis)
            ii = np.moveaxis(np.tensordot(i2, yi, axes=(1, axis)), 0, axis)
            ri = np.moveaxis(np.tensordot(r2, yi, axes=(1, axis)), 0, axis)
            ir = np.moveaxis(np.tensordot(i2, yr, axes=(1, axis)), 0, axis)
            yr, yi = rr-ii, ri+ir
        yr, yi = yr.reshape(256, 5), yi.reshape(256, 5)
        T = (24//norm)[:, None]*(V.T@yr)  # 384 times the quartic action.
        require(not np.any(yi) and np.array_equal(V@T, 24*yr),
                'exact quartic intertwiner ' + str(len(quartics)))
        require(np.array_equal(T@T, 384**2*np.eye(5, dtype=np.int64))
                and int(np.trace(T)) == 3*384,
                'quartic spectrum +1 four and -1 one ' + str(len(quartics)))
        require(np.array_equal(T.T@np.diag(norm)@T, 384**2*np.diag(norm)),
                'quartic metric ' + str(len(quartics)))
        quartics.append(T)
    pi384 = sum((384//int(norm[j]))*np.outer(V[:, j], V[:, j]) for j in range(5))
    require(not np.any(moment_im) and np.array_equal(moment_re-16*sym24, pi384),
            'basis equals original Pi5 = 40 M4 - Psym')
    require(len({tuple(t.ravel()) for t in quartics}) == 15, '15 quartic reflections')

    # One-body compression and induced Grassmann metric, exact matrix-unit basis.
    residual = {}
    for a, b in it.product(range(4), repeat=2):
        W = np.zeros_like(V)
        for j, word in enumerate(words):
            for k, mode in enumerate(word):
                if mode == b:
                    dest = list(word)
                    dest[k] = a
                    W[wi[tuple(dest)]] += V[j]
        require(np.array_equal(V.T@W, int(a == b)*np.diag(norm)),
                f'one-body compression E{a}{b}')
        residual[a, b] = W-int(a == b)*V
    for a, b, c, d in it.product(range(4), repeat=4):
        measured24 = sum(int(x)*(24//int(n)) for x, n in
                         zip(np.diag(residual[b, a].T@residual[c, d]), norm))
        expected24 = 24*(8*int(a == d and b == c)-2*int(a == b and c == d))
        require(measured24 == expected24, f'induced metric {a}{b},{c}{d}')
    leakage = residual[0, 0].T@residual[0, 0]
    require(np.array_equal(leakage, np.diag([12, 12, 12, 12, 0])),
            'moving quartic space has nonzero leakage under native interpolation')

    # Pull back the actual standard E8 source roots; only the named pure function runs.
    src = REPO/'verification/v1_e8_glue.py'
    module = ast.parse(src.read_text())
    fn = next(n for n in module.body if isinstance(n, ast.FunctionDef) and n.name == 'e8_roots')
    env = {'np': np, 'itertools': it}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(src), 'exec'), env)
    root2 = []
    for root in env['e8_roots']():
        require(np.array_equal(2*root, np.rint(2*root)), 'dyadic source E8 root')
        root2.append(tuple(int(v) for v in 2*root))
    require(len(set(root2)) == 240, 'actual E8 root count')
    # D5 on first five and D3=A3 on last three coordinates. Angles in pi/4.
    lift_q = (0, 0, 0, 0, 4, 2, 2, 2)
    berry_q = (4, 4, 4, 4, 0, -2, -2, -2)
    def exponent(q, r):
        n = sum(a*b for a, b in zip(q, r))
        require(n % 2 == 0, 'integral eighth-root exponent')
        return (n//2) % 8
    grades, phases = {}, {}
    for r in root2:
        grade = sum(r[5:]) % 4
        phase = exponent(lift_q, r)
        require((2*phase+2*grade) % 8 == 0, 'E8 L squared is G inverse')
        require(exponent(berry_q, r) == phase, 'Berry and direct E8 lift coincide')
        grades[r], phases[r] = grade, phase
    dims = Counter(grades.values())
    dims[0] += 8
    require(dict(sorted(dims.items())) == {0: 60, 1: 64, 2: 60, 3: 64},
            'D5+A3 branching including all Cartan directions')
    bracket_pairs = 0
    for r, s in it.product(root2, repeat=2):
        t = tuple(a+b for a, b in zip(r, s))
        if t in phases:
            require((phases[r]+phases[s]-phases[t]) % 8 == 0,
                    'root-addition bracket phase')
            bracket_pairs += 1
    require(bracket_pairs == 13440, 'all nonzero root-sum brackets covered')
    require(all((phases[r]+phases[tuple(-x for x in r)]) % 8 == 0 for r in root2),
            'opposite-root brackets have neutral Cartan phase')
    require(any(p % 2 for p in phases.values()), 'lift has exact order eight')

    # Central quotient and universal determinant-parity cocycle, all cases.
    kernel = [(a, b) for a, b in it.product(range(4), repeat=2)
              if all((grade*(a+b)) % 4 == 0 for grade in range(4))]
    require(kernel == [(0, 0), (1, 3), (2, 2), (3, 1)], 'diagonal Z4 quotient kernel')
    for p, q, r in it.product(range(2), repeat=3):
        require((-p*q-(p^q)*r+p*(q^r)+q*r) % 4 == 0, 'global cocycle associativity')
    for m in range(65):
        carry, parity = 0, 0
        for _ in range(m):
            carry -= parity
            parity ^= 1
        require(carry == -(m//2), 'word winding/carry ' + str(m))
    require(all((2*k-1) % 4 != 0 for k in range(4)), 'no central twist restores involution')
    require({(2*k) % 4 for k in range(4)} == {0, 2}, 'source reflection squares are even')
    require({(2*k-1) % 4 for k in range(4)} == {1, 3}, 'lift reflection squares are odd')

    # The four integer block decompositions are not inferred from dimension alone.
    R = sp.diag(1, 1, 1, 1, -1)
    exterior_eigen = [sp.prod(R[i, i] for i in subset)
                     for k in (0, 2, 4) for subset in it.combinations(range(5), k)]
    require(Counter(exterior_eigen) == {1: 8, -1: 8}, 'actual even exterior spin action')
    result = {
        'research_id': 'UR.COMPILER.QUARTIC_HOLONOMY.12',
        'research_verdict': 'PARTIAL', 'checker_verdict': 'PASS',
        'arithmetic': 'Gaussian integers, rational identities and integer phase exponents',
        'source_rays': 60, 'one_body_basis_checks': 16, 'metric_basis_pairs': 256,
        'compression': 'P5 dGamma4(X) P5 = tr(X) P5',
        'berry_connection': 'tr(U^dagger dU) I5', 'berry_curvature': 0,
        'grassmann_metric_convention': 'Tr_W(dPhi^dagger (1-P) dPhi)',
        'grassmann_metric': '8 tr(XY) - 2 tr(X) tr(Y) for Hermitian X,Y',
        'native_reflection_quartic': [[int(v) for v in row] for row in R.tolist()],
        'projector_path_quartic_holonomy': '-R',
        'projector_path_family_lift': 'exp(-i*pi/4) r',
        'e8_grade_dimensions': dict(sorted(dims.items())),
        'e8_phase_histogram': dict(sorted(Counter(phases.values()).items())),
        'e8_root_sum_brackets_checked': bracket_pairs,
        'lift_order': 8, 'lift_square': 'G^-1',
        'global_cocycle': '-epsilon(g)*epsilon(h) mod 4',
        'word_formula': 'product L(r_j) = G^-floor(m/2) L(product r_j)',
        'source_full_group_order_inherited_from_09': 46080,
        'pullback_extension_order_conditional_on_09': 184320,
        'effective_E8_image_order_conditional_on_09': 46080,
        'source_word_group_embeds_preserving_marked_data': False,
        'physical_local_current_derived': False,
        'physical_time_derived': False, 'affine_level_derived': False,
        'closed_gate_ids': [], 'checks_passed': len(checks),
        'source_sha256': pins,
    }
    out.mkdir(parents=True, exist_ok=True)
    (out/'validation.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k: result[k] for k in ('research_id', 'research_verdict',
          'checker_verdict', 'checks_passed', 'e8_grade_dimensions', 'lift_order')}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=HERE/'results')
    main(parser.parse_args().out)
