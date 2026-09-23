#!/usr/bin/env python3
"""Exact W24 Chevalley dictionary and the first mixed-current PBW witness.

This stays inside the already assumed level-one affine E8 vacuum.  It fixes
the finite W4/W20 basis phases by actual SU(5) and A3 root transport before
using the native quartic coefficient matrix.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import itertools as it
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT_JSON = HERE / "current_bracket_dictionary.json"
OUT_TXT = HERE / "current_bracket_dictionary.txt"
CHECKS: Counter[str] = Counter()


def require(ok: object, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS[label] += 1


class Always(ast.NodeTransformer):
    def visit_Assert(self, node: ast.Assert) -> ast.AST:
        return ast.copy_location(
            ast.Expr(
                ast.Call(
                    ast.Name("require", ast.Load()),
                    [node.test, ast.Constant("original source assertion")],
                    [],
                )
            ),
            node,
        )


def original(path: str, name: str, env: dict[str, object]) -> object:
    """Load one original definition while keeping assertions under -OO."""
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    node = next(
        item
        for item in tree.body
        if isinstance(item, (ast.ClassDef, ast.FunctionDef)) and item.name == name
    )
    env["require"] = require
    module = ast.fix_missing_locations(
        Always().visit(ast.Module(body=[node], type_ignores=[]))
    )
    exec(compile(module, str(ROOT / path), "exec"), env)
    return env[name]


def ip(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x * y for x, y in zip(a, b))


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def sub(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x - y for x, y in zip(a, b))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tensor_power(v: sp.Matrix, degree: int) -> sp.Matrix:
    out = sp.Matrix([1])
    for _ in range(degree):
        out = sp.kronecker_product(out, v)
    return out


def exact_ray(z: np.ndarray) -> sp.Matrix:
    require(
        np.array_equal(z.real, np.rint(z.real))
        and np.array_equal(z.imag, np.rint(z.imag)),
        "Gaussian integral native ray",
    )
    return sp.Matrix(
        [
            sp.Rational(int(round(x.real)), 2)
            + sp.I * sp.Rational(int(round(x.imag)), 2)
            for x in z
        ]
    )


def clean(v: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    return {i: sp.simplify(x) for i, x in v.items() if sp.simplify(x) != 0}


def main() -> None:
    source_paths = [
        "verification/v1_e8_glue.py",
        "verification/v498_celestial_wp5b_singular_vector.py",
        "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json",
        "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py",
        "experiments/theory-contracts/compiler-spatial-response-20260919/completion24_check.py",
        "experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/checker.py",
    ]
    source_hashes = {path: sha256(ROOT / path) for path in source_paths}

    triality = json.loads((ROOT / source_paths[2]).read_text(encoding="utf-8"))
    basis = sp.Matrix(triality["integral_triality"]["vector_basis"])
    raw = original(
        source_paths[0], "e8_roots", {"np": np, "itertools": it}
    )()
    require(
        all(float(2 * x).is_integer() for root in raw for x in root),
        "source roots are dyadic",
    )
    roots = [tuple(int(2 * x) for x in root) for root in raw]
    rootset = set(roots)
    require(len(rootset) == 240, "source has 240 E8 roots")
    coordinates = {
        root: tuple(F(x) for x in basis.inv() * sp.Matrix(root) / 2)
        for root in roots
    }

    class RootAdapter:
        n = dim = 8

        def __init__(self) -> None:
            self.roots = roots
            self.simple = [tuple(int(x) for x in 2 * basis[:, i]) for i in range(8)]

        def alpha_coords(self, root: tuple[int, ...]) -> tuple[F, ...]:
            return coordinates[root]

    chevalley = original(
        source_paths[1], "Chevalley", {"F": F, "ip": ip, "vadd": add}
    )(RootAdapter())
    affine = original(source_paths[1], "Affine", {"F": F})(chevalley, 1)
    require(
        chevalley.sgn == chevalley.kappa_root == -1,
        "source compact Chevalley convention",
    )

    def raw_bracket_sign(a: tuple[int, ...], b: tuple[int, ...]) -> int:
        target = add(a, b)
        out = chevalley.bracket(chevalley.ridx[a], chevalley.ridx[b])
        if target not in rootset:
            require(not out, "absent root sum has zero Chevalley bracket")
            return 0
        require(
            out == {chevalley.ridx[target]: F(out[chevalley.ridx[target]])}
            and out[chevalley.ridx[target]] in (1, -1),
            "present root sum has unit Chevalley cocycle",
        )
        return int(out[chevalley.ridx[target]])

    family_weights = [
        (-1, -1, -1),
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
    ]
    w4 = {a: (-1,) * 5 + family_weights[a] for a in range(4)}
    w20 = {
        (i, a): tuple(-1 if j == i else 1 for j in range(5))
        + family_weights[a]
        for i in range(5)
        for a in range(4)
    }
    require(set(w4.values()) <= rootset and set(w20.values()) <= rootset,
            "all W24 directions are original E8 roots")

    # Fix phases from a reference vector by raw simple-root transports.
    family_simple = {a: sub(w4[a + 1], w4[a]) for a in range(3)}
    carrier_simple = {i: sub(w20[i + 1, 0], w20[i, 0]) for i in range(4)}
    q: dict[int, int] = {0: 1}
    for a in range(3):
        q[a + 1] = q[a] * raw_bracket_sign(family_simple[a], w4[a])
    p: dict[tuple[int, int], int] = {(0, 0): 1}
    for a in range(3):
        p[0, a + 1] = p[0, a] * raw_bracket_sign(family_simple[a], w20[0, a])
    for a in range(4):
        for i in range(4):
            p[i + 1, a] = p[i, a] * raw_bracket_sign(carrier_simple[i], w20[i, a])
    require(all(value in (-1, 1) for value in q.values()), "W4 phases are signs")
    require(all(value in (-1, 1) for value in p.values()), "W20 phases are signs")
    for a in range(3):
        for i in range(5):
            coefficient = (
                p[i, a]
                * raw_bracket_sign(family_simple[a], w20[i, a])
                // p[i, a + 1]
            )
            require(coefficient == 1, "A3 simple transport is path independent on W20")
    for i in range(4):
        for a in range(4):
            coefficient = (
                p[i, a]
                * raw_bracket_sign(carrier_simple[i], w20[i, a])
                // p[i + 1, a]
            )
            require(coefficient == 1, "SU5 simple transport is path independent on W20")

    # Phase the full matrix-unit roots so they act with coefficient +1.
    family_generators: dict[tuple[int, int], tuple[tuple[int, ...], int]] = {}
    for target, source in it.permutations(range(4), 2):
        root = sub(w4[target], w4[source])
        sign = raw_bracket_sign(root, w4[source])
        phase = q[target] // (q[source] * sign)
        family_generators[target, source] = (root, phase)
        for i in range(5):
            got = phase * p[i, source] * raw_bracket_sign(root, w20[i, source])
            require(got == p[i, target], "full A3 matrix unit acts identically on W4 and W20")

    carrier_generators: dict[tuple[int, int], tuple[tuple[int, ...], int]] = {}
    for target, source in it.permutations(range(5), 2):
        root = sub(w20[target, 0], w20[source, 0])
        sign = raw_bracket_sign(root, w20[source, 0])
        phase = p[target, 0] // (p[source, 0] * sign)
        carrier_generators[target, source] = (root, phase)
        for a in range(4):
            got = phase * p[source, a] * raw_bracket_sign(root, w20[source, a])
            require(got == p[target, a], "full SU5 matrix unit acts uniformly on family factor")
        for a in range(4):
            require(
                not chevalley.bracket(chevalley.ridx[root], chevalley.ridx[w4[a]]),
                "SU5 matrix unit annihilates W4 singlet",
            )

    # Y_(i,ab) is defined by [C_a,X_(i,b)] for a<b.  This fixes the
    # target-root phase, after which the reversed input must be minus Y.
    yroot: dict[tuple[int, int, int], tuple[int, ...]] = {}
    yphase: dict[tuple[int, int, int], int] = {}
    for i in range(5):
        for a, b in it.combinations(range(4), 2):
            root = add(w4[a], w20[i, b])
            phase = q[a] * p[i, b] * raw_bracket_sign(w4[a], w20[i, b])
            yroot[i, a, b] = root
            yphase[i, a, b] = phase
            reverse = q[b] * p[i, a] * raw_bracket_sign(w4[b], w20[i, a])
            require(reverse == -phase, "mixed bracket has exact A3 wedge antisymmetry")
    require(len(set(yroot.values())) == 30, "mixed bracket spans thirty distinct roots")
    require(
        all(sum(x != 0 for x in root) == 2 and set(abs(x) for x in root if x) == {2}
            for root in yroot.values()),
        "mixed bracket roots are the expected D8 integer roots",
    )
    for i in range(5):
        for a in range(4):
            require(raw_bracket_sign(w4[a], w20[i, a]) == 0,
                    "equal family label has zero mixed bracket")

    # Verify the entire 30-space transforms as bar5 tensor Lambda2(4).
    for target, source in it.permutations(range(5), 2):
        root, phase = carrier_generators[target, source]
        for a, b in it.combinations(range(4), 2):
            raw = raw_bracket_sign(root, yroot[source, a, b])
            got = phase * yphase[source, a, b] * raw
            require(got == yphase[target, a, b],
                    "mixed image has Kronecker carrier transport")

    for target, source in it.permutations(range(4), 2):
        root, phase = family_generators[target, source]
        for i in range(5):
            for a, b in it.combinations(range(4), 2):
                pair = [a, b]
                if source not in pair or target in pair:
                    require(
                        not chevalley.bracket(
                            chevalley.ridx[root], chevalley.ridx[yroot[i, a, b]]
                        ),
                        "A3 matrix unit has the correct wedge zero",
                    )
                    continue
                position = pair.index(source)
                moved = pair.copy()
                moved[position] = target
                sign = 1 if moved[0] < moved[1] else -1
                aa, bb = sorted(moved)
                raw = raw_bracket_sign(root, yroot[i, a, b])
                got = phase * yphase[i, a, b] * raw
                require(got == sign * yphase[i, aa, bb],
                        "A3 action is the standard exterior-square action")

    # Reconstruct the exact native F20 in the now phase-aligned tensor basis.
    words3 = list(it.product(range(4), repeat=3))
    triples = list(it.combinations_with_replacement(range(4), 3))
    sym3 = sp.zeros(64, 20)
    for column, triple in enumerate(triples):
        permutations = sorted(set(it.permutations(triple)))
        for word in permutations:
            sym3[words3.index(word), column] = 1 / sp.sqrt(len(permutations))
    quartics = np.zeros((256, 5), dtype=np.int64)
    for row, word in enumerate(it.product(range(4), repeat=4)):
        counts = tuple(word.count(j) for j in range(4))
        if 4 in counts:
            quartics[row, 0] = 1
        elif counts in ((2, 2, 0, 0), (0, 0, 2, 2)):
            quartics[row, 1] = 1
        elif counts in ((2, 0, 2, 0), (0, 2, 0, 2)):
            quartics[row, 2] = 1
        elif counts in ((2, 0, 0, 2), (0, 2, 2, 0)):
            quartics[row, 3] = 1
        elif counts == (1, 1, 1, 1):
            quartics[row, 4] = 1
    norms = np.diag(quartics.T @ quartics)
    f20 = sp.Matrix.vstack(
        *[
            2 * (sp.Matrix(quartics[:, i].reshape(4, 64)) * sym3) / sp.sqrt(int(norms[i]))
            for i in range(5)
        ]
    )
    require(sp.simplify(f20.H * f20) == sp.eye(20), "native F20 is exactly unitary")

    spec = importlib.util.spec_from_file_location("current_dictionary_source", ROOT / source_paths[3])
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    psis = [exact_ray(z) for z in rays]
    cubes = [sym3.H * tensor_power(psi, 3) for psi in psis]
    readout20 = [f20 * cube.conjugate() for cube in cubes]
    require(len(readout20) == len(psis) == 60, "native frame has sixty ray labels")

    def vector_from_frame(label: int, sheet: int) -> dict[int, sp.Expr]:
        out: dict[int, sp.Expr] = {}
        aa = sp.sqrt(sp.Rational(5, 6))
        bb = sp.sqrt(sp.Rational(1, 6))
        for i in range(5):
            for a in range(4):
                index = chevalley.ridx[w20[i, a]]
                out[index] = aa * readout20[label][4 * i + a] * p[i, a]
        for a in range(4):
            index = chevalley.ridx[w4[a]]
            out[index] = sheet * bb * psis[label][a] * q[a]
        return clean(out)

    def vector_w20(label: int) -> dict[int, sp.Expr]:
        return clean(
            {
                chevalley.ridx[w20[i, a]]: readout20[label][4 * i + a] * p[i, a]
                for i in range(5)
                for a in range(4)
            }
        )

    def vector_w4(label: int) -> dict[int, sp.Expr]:
        return clean(
            {
                chevalley.ridx[w4[a]]: psis[label][a] * q[a]
                for a in range(4)
            }
        )

    def bracket_vec(left: dict[int, sp.Expr], right: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
        out: dict[int, sp.Expr] = {}
        for i, x in left.items():
            for j, y in right.items():
                for k, coefficient in chevalley.bracket(i, j).items():
                    out[k] = out.get(k, 0) + x * y * sp.Rational(coefficient.numerator, coefficient.denominator)
        return clean(out)

    def dagger(v: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
        out: dict[int, sp.Expr] = {}
        for i, x in v.items():
            if i < 240:
                out[chevalley.opp[i]] = out.get(chevalley.opp[i], 0) - sp.conjugate(x)
            else:
                out[i] = out.get(i, 0) + sp.conjugate(x)
        return clean(out)

    def kappa(left: dict[int, sp.Expr], right: dict[int, sp.Expr]) -> sp.Expr:
        value = 0
        for i, x in left.items():
            for j, y in right.items():
                coefficient = chevalley.kappa(i, j)
                if coefficient:
                    value += x * y * sp.Rational(coefficient.numerator, coefficient.denominator)
        return sp.simplify(value)

    def fourpoint(
        a: dict[int, sp.Expr],
        b: dict[int, sp.Expr],
        c: dict[int, sp.Expr],
        d: dict[int, sp.Expr],
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
        """<0|J1(a^dag)J1(b^dag)J-1(c)J-1(d)|0>."""
        ad, bd = dagger(a), dagger(b)
        pair_direct = kappa(bd, c) * kappa(ad, d)
        pair_exchange = kappa(bd, d) * kappa(ad, c)
        connected = kappa(ad, bracket_vec(bracket_vec(bd, c), d))
        total = sp.simplify(pair_direct + pair_exchange + connected)
        return tuple(sp.simplify(x) for x in (total, pair_direct, pair_exchange, connected))

    def corrected_basis(root: tuple[int, ...], phase: int) -> dict[int, sp.Expr]:
        return {chevalley.ridx[root]: sp.Integer(phase)}

    # First coordinate mixed witness and two controls.
    c_active = corrected_basis(w4[0], q[0])
    d_active = corrected_basis(w20[0, 1], p[0, 1])
    active_terms = fourpoint(d_active, c_active, c_active, d_active)
    require(active_terms == (2, 1, 0, 1),
            "mixed coordinate fourpoint is one plus one connected")
    c_orth = corrected_basis(w20[0, 0], p[0, 0])
    d_orth = corrected_basis(w20[1, 1], p[1, 1])
    orth_terms = fourpoint(d_orth, c_orth, c_orth, d_orth)
    require(not bracket_vec(c_orth, d_orth) and orth_terms == (1, 1, 0, 0),
            "orthogonal commuting coordinate control has no connected term")
    c_null = corrected_basis(w4[0], q[0])
    d_null = corrected_basis(w4[1], q[1])
    null_terms = fourpoint(d_null, c_null, c_null, d_null)
    require(not bracket_vec(c_null, d_null) and null_terms == (0, 1, 0, -1),
            "positive-inner-product commuting pair is level-one null")

    # Independent direct Affine PBW evaluation of the active basis amplitude.
    def star(index: int) -> tuple[int, int]:
        return (chevalley.opp[index], -1) if index < 240 else (index, 1)

    def basis_pbw(
        a: tuple[int, int], b: tuple[int, int], c: tuple[int, int], d: tuple[int, int]
    ) -> F:
        vac = {(): F(1)}
        state = affine.act(d[0], -1, vac)
        state = {key: value * d[1] for key, value in state.items()}
        state = affine.act(c[0], -1, state)
        state = {key: value * c[1] for key, value in state.items()}
        bi, bs = star(b[0])
        state = affine.act(bi, 1, state)
        state = {key: value * b[1] * bs for key, value in state.items()}
        ai, ass = star(a[0])
        state = affine.act(ai, 1, state)
        state = {key: value * a[1] * ass for key, value in state.items()}
        require(set(state) <= {()}, "basis PBW evaluation returns to vacuum")
        return state.get((), F(0))

    pbw_active = basis_pbw(
        (chevalley.ridx[w20[0, 1]], p[0, 1]),
        (chevalley.ridx[w4[0]], q[0]),
        (chevalley.ridx[w4[0]], q[0]),
        (chevalley.ridx[w20[0, 1]], p[0, 1]),
    )
    require(pbw_active == 2, "direct source Affine PBW witness equals bracket formula")

    # The same ray is subtler than a generic W20+W4 mixture: the exact F20
    # image factorizes as a W5 vector tensor the SAME family ray.  Therefore
    # its A3 wedge with the W4 branch vanishes, even across opposite sheets.
    factor_carriers = []
    square_terms_all = []
    for label in range(60):
        matrix = sp.Matrix(5, 4, list(readout20[label]))
        psi = psis[label]
        pivot = next(a for a in range(4) if psi[a] != 0)
        carrier = sp.Matrix([sp.simplify(matrix[i, pivot] / psi[pivot]) for i in range(5)])
        require(
            sp.simplify(matrix - carrier * psi.T) == sp.zeros(5, 4),
            "native F20 readout factorizes as W5 tensor the same family ray",
        )
        factor_carriers.append(carrier)
        plus = vector_from_frame(label, 1)
        minus = vector_from_frame(label, -1)
        mixed = bracket_vec(plus, minus)
        require(not mixed, "same-ray opposite-sheet bracket vanishes by exact A3 wedge")
        old = vector_w20(label)
        companion = vector_w4(label)
        require(kappa(dagger(old), old) == 1 and kappa(dagger(companion), companion) == 1,
                "factorized old and companion currents are normalized")
        require(not bracket_vec(old, companion),
                "factorized old and companion currents commute")
        old_square = fourpoint(old, old, old, old)
        companion_square = fourpoint(companion, companion, companion, companion)
        completed_square = fourpoint(plus, plus, plus, plus)
        require(old_square == (0, 1, 1, -2),
                "every native W20 same-current square is level-one null")
        require(companion_square == (0, 1, 1, -2),
                "every native W4 same-current square is level-one null")
        require(completed_square == (sp.Rational(5, 9), 1, 1, -sp.Rational(13, 9)),
                "every completed W24 same-current square has norm five ninths")
        square_terms_all.append(completed_square)

    # First exact nonlinear witness in the actual frame must therefore use
    # two different rays.  Search a fixed bounded lexicographic family.
    frame_witness = None
    for left_label, right_label in it.combinations(range(60), 2):
        for left_sheet, right_sheet in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            left = vector_from_frame(left_label, left_sheet)
            right = vector_from_frame(right_label, right_sheet)
            mixed = bracket_vec(left, right)
            norm = sp.simplify(kappa(dagger(mixed), mixed))
            if norm == 0:
                continue
            terms = fourpoint(right, left, left, right)
            coordinates_y = []
            for i in range(5):
                for a, b in it.combinations(range(4), 2):
                    index = chevalley.ridx[yroot[i, a, b]]
                    if index not in mixed:
                        continue
                    coefficient = sp.simplify(
                        mixed[index] / sp.Integer(yphase[i, a, b])
                    )
                    if coefficient != 0:
                        coordinates_y.append(
                            {"i": i, "a": a, "b": b, "coefficient": str(coefficient)}
                        )
            require(coordinates_y, "different-ray bracket has a nonzero Y coordinate")
            require(sp.simplify(terms[0] - sum(terms[1:])) == 0,
                    "native frame fourpoint decomposition is exact")
            frame_witness = {
                "labels": [left_label, right_label],
                "rays": [
                    [str(x) for x in psis[left_label]],
                    [str(x) for x in psis[right_label]],
                ],
                "sheets": [left_sheet, right_sheet],
                "overlap": str(kappa(dagger(left), right)),
                "bracket_norm_squared": str(norm),
                "fourpoint_total": str(terms[0]),
                "pair_direct": str(terms[1]),
                "pair_exchange": str(terms[2]),
                "connected_lie_term": str(terms[3]),
                "nonzero_Y_coordinates": coordinates_y,
            }
            break
        if frame_witness is not None:
            break
    require(frame_witness is not None, "a different-ray native nonlinear frame witness exists")

    # Actual grade-two product intertwiner after the level-one null quotient.
    # The symmetric family pairs share one lattice weight, while the
    # antisymmetric combination is precisely the current-bracket descendant.
    product50 = []
    product50_labels = []
    for i in range(5):
        for a in range(4):
            product50.append(
                [(sp.Integer(1), corrected_basis(w20[i, a], p[i, a]), corrected_basis(w4[a], q[a]))]
            )
            product50_labels.append((i, a, a))
        for a, b in it.combinations(range(4), 2):
            product50.append(
                [
                    (1 / sp.sqrt(2), corrected_basis(w20[i, a], p[i, a]), corrected_basis(w4[b], q[b])),
                    (1 / sp.sqrt(2), corrected_basis(w20[i, b], p[i, b]), corrected_basis(w4[a], q[a])),
                ]
            )
            product50_labels.append((i, a, b))
    require(len(product50) == 50 and len(set(product50_labels)) == 50,
            "product intertwiner has five times Sym2 four equals fifty states")

    def state_inner(left: list[tuple[sp.Expr, dict[int, sp.Expr], dict[int, sp.Expr]]],
                    right: list[tuple[sp.Expr, dict[int, sp.Expr], dict[int, sp.Expr]]]) -> sp.Expr:
        value = 0
        for lc, lx, ly in left:
            for rc, rx, ry in right:
                # Ket is J_-1(X)J_-1(C)|0>; its bra reverses the order.
                value += sp.conjugate(lc) * rc * fourpoint(ly, lx, rx, ry)[0]
        return sp.simplify(value)

    product_gram = sp.Matrix(
        50, 50,
        lambda row, column: state_inner(product50[row], product50[column]),
    )
    require(product_gram == sp.eye(50),
            "normalized grade-two W5 tensor Sym2(4) product Gram is I50")
    product_weights = {
        add(w20[i, a], w4[b])
        for i in range(5)
        for a in range(4)
        for b in range(a, 4)
    }
    require(len(product_weights) == 50, "product intertwiner has fifty distinct weights")
    weight_norms = Counter(ip(weight, weight) for weight in product_weights)
    require(weight_norms == {16: 20, 8: 30},
            "product weights split into twenty norm-four and thirty norm-two weights")

    dictionary_w24 = []
    for a in range(4):
        dictionary_w24.append(
            {"sector": "W4", "family": a, "root_doubled": w4[a], "chevalley_phase": q[a]}
        )
    for i in range(5):
        for a in range(4):
            dictionary_w24.append(
                {
                    "sector": "W20",
                    "carrier": i,
                    "family": a,
                    "root_doubled": w20[i, a],
                    "chevalley_phase": p[i, a],
                }
            )
    dictionary_y30 = [
        {
            "carrier": i,
            "family_wedge": [a, b],
            "root_doubled": yroot[i, a, b],
            "chevalley_phase": yphase[i, a, b],
        }
        for i in range(5)
        for a, b in it.combinations(range(4), 2)
    ]

    result = {
        "research_id": "UR.COMPILER.CURRENT_BRACKET_DICTIONARY.20260919",
        "verdict": "EXACT_SOURCE_CHEVALLEY_DICTIONARY_AND_NONZERO_NATIVE_FRAME_FOURPOINT",
        "premise": "original compact-adjoint affine E8 level-one vacuum",
        "dictionary_convention": {
            "C_a": "q_a E_(c_a), c_a=(-1,-1,-1,-1,-1;sigma_a)",
            "X_i_a": "p_i_a E_(x_i_a), x_i_a=(+,+,+,+,+ with one minus at i;sigma_a)",
            "Y_i_ab": "[C_a,X_i_b] for a<b",
            "family_weights": family_weights,
            "basis_gauge": "C_0=X_0_0=+ raw Chevalley vector; adjacent A3 and SU5 raw-root transports have coefficient +1",
        },
        "W24": dictionary_w24,
        "mixed_image_30": dictionary_y30,
        "exact_bracket": {
            "formula": "[C_a,X_(i,b)]=0 if a=b; =Y_(i,a wedge b) otherwise, with exterior sign",
            "representation": "bar5 tensor Lambda2(4)",
            "dimension": 30,
            "adjoint_dimension": 30,
            "same_chirality_commuting_blocks": ["[W20,W20]=0", "[W4,W4]=0"],
            "full_equivariance_checked": ["SU5 matrix units", "A3 matrix units"],
        },
        "coordinate_PBW_witness": {
            "currents": ["C_0", "X_(0,1)"],
            "root_inner_product": "-1",
            "bracket": "Y_(0,0 wedge 1)",
            "amplitude": "<Omega|J_1(X_(0,1)^dag) J_1(C_0^dag) J_-1(C_0) J_-1(X_(0,1))|Omega>=2",
            "decomposition": {"direct": "1", "exchange": "0", "connected_lie": "1"},
            "direct_affine_PBW": str(pbw_active),
        },
        "controls": {
            "orthogonal_commuting": {
                "currents": ["X_(0,0)", "X_(1,1)"],
                "fourpoint": "1",
                "connected_lie": "0",
            },
            "level_one_null": {
                "currents": ["C_0", "C_1"],
                "root_inner_product": "+1",
                "commutator": "0",
                "fourpoint_norm": "0=1-1",
                "meaning": "the universal PBW word has zero norm and vanishes in the irreducible E8_1 quotient",
            },
        },
        "same_ray_factorization": {
            "formula": "F20 conjugate(psi_l^3)=chi_l tensor psi_l",
            "labels_checked": 60,
            "consequence": "[w_(l,+),w_(l,-)]=0 because psi_l wedge psi_l=0",
        },
        "same_outcome_square": {
            "labels_and_sheets_checked": "60 labels; the sign drops out, so both sheets",
            "old_W20_square_norm": "0",
            "companion_W4_square_norm": "0",
            "completed_W24_square_norm": "5/9",
            "completed_fourpoint_decomposition": {
                "direct": "1",
                "exchange": "1",
                "nested_lie_term": "-13/9",
            },
            "PBW_identity": "J_-1(w24_(l,s))^2 Omega = s 2 sqrt(5/36) J_-1(w20_l)J_-1(w4_l) Omega",
            "coordinate_weight_sum": "for X_(i,a)+C_a the doubled lattice vector has norm-squared 16, hence original norm-squared 4 and affine grade 2",
            "interpretation": "exact E8_1 quotient amplitude, not the Gaussian oscillator fourth moment 2",
            "completed_cube": "0 in the irreducible E8_1 quotient: the two commuting branch squares are null, so every term in (a w20+b w4)^3 contains a null branch square",
        },
        "grade2_product_intertwiner": {
            "definition": (
                "T_(i,aa)=J_-1(X_(i,a))J_-1(C_a)Omega; "
                "T_(i,ab)=(J_-1(X_(i,a))J_-1(C_b)+J_-1(X_(i,b))J_-1(C_a))Omega/sqrt(2) for a<b"
            ),
            "representation": "bar5 tensor Sym2(4)",
            "dimension": 50,
            "Gram": "I_50 exactly",
            "distinct_weights": 50,
            "lattice_weight_norms": {
                "20 diagonal-family weights": 4,
                "30 off-diagonal-family weights": 2,
            },
            "meaning": "actual normalized affine grade-two product states after level-one null relations, not a weight-count proxy",
        },
        "native_frame_witness": frame_witness,
        "general_fourpoint_formula": (
            "kappa(b^dag,c)kappa(a^dag,d)+kappa(b^dag,d)kappa(a^dag,c)"
            "+kappa(a^dag,[[b^dag,c],d])"
        ),
        "scope": (
            "This is an exact operator statement inside the existing E8_1 source. "
            "It does not derive the raw seam-to-net map, preparation of the 120-frame, "
            "a neutral instrument, spacetime transport, or physical matter selection."
        ),
        "source_sha256": source_hashes,
        "check_evaluations": sum(CHECKS.values()),
        "checks": dict(sorted(CHECKS.items())),
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    witness = frame_witness
    text = f"""CURRENT BRACKET DICTIONARY — EXACT SOURCE RESULT

Verdict
  {result['verdict']}

Phase-fixed dictionary
  C_a = q_a E_(c_a), X_(i,a)=p_(i,a) E_(x_(i,a)).
  The signs q,p are transported from C_0=X_(0,0)=+E by the actual source
  SU(5) and A3 Chevalley root actions.  All matrix units were then checked.
  [C_a,X_(i,b)] = 0 for a=b and equals Y_(i,a wedge b) with the exact
  exterior sign for a!=b.  The 30 distinct outputs are bar5 tensor Lambda2(4).
  Their compact adjoints provide the conjugate 30-dimensional sector.

First coordinate PBW witness
  <Omega|J_1(X_(0,1)^dag) J_1(C_0^dag)
          J_-1(C_0) J_-1(X_(0,1))|Omega> = 2.
  Direct pairing = 1; exchange pairing = 0; connected Lie term = 1.
  The original Affine class independently returns {pbw_active}.

Same-outcome square in the completed frame
  For all 60 native labels (and either sheet),
    ||J_-1(w20_l)^2 Omega||^2 = 0,
    ||J_-1(w4_l)^2 Omega||^2 = 0,
    ||J_-1(w24_(l,s))^2 Omega||^2 = 5/9.
  Exactly,
    J_-1(w24_(l,s))^2 Omega
      = s 2 sqrt(5/36) J_-1(w20_l)J_-1(w4_l) Omega.
  For a coordinate ray, the surviving cross word has lattice norm four and
  affine grade two.  Generic rays expand in the 50-state product basis below.
  The value 5/9 is an E8_1 quotient amplitude; it is not the Gaussian
  oscillator value 2.
  The same completed current has cube zero in the irreducible E8_1 quotient:
  the branches commute, and every cubic term contains a null W20 or W4 square.

Normalized grade-two product intertwiner
  T_(i,aa)=J_-1(X_(i,a))J_-1(C_a)Omega,
  T_(i,ab)=[J_-1(X_(i,a))J_-1(C_b)
            +J_-1(X_(i,b))J_-1(C_a)]Omega/sqrt(2), a<b.
  The complete exact Gram matrix is I_50.  The 20 diagonal-family weights have
  lattice norm four; the 30 off-diagonal weights have norm two and sit at
  affine grade two rather than being new grade-one root currents.  Thus these
  are actual quotient product states in bar5 tensor Sym2(4), not merely a
  matching weight count.

Controls and the level-one quotient
  X_(0,0),X_(1,1) commute and are root-orthogonal: total 1, connected 0.
  C_0,C_1 commute but their roots have inner product +1: norm 0=1-1.
  Thus PBW words are not all independent; the latter is a null word in E8_1.

First actual native 120-frame witness
  labels = {witness['labels']}, sheets = {witness['sheets']}
  rays = {witness['rays']}
  <w_+,w_-> = {witness['overlap']}
  ||[w_+,w_-]||^2 = {witness['bracket_norm_squared']}
  fourpoint total = {witness['fourpoint_total']}
  direct = {witness['pair_direct']}, exchange = {witness['pair_exchange']},
  connected Lie term = {witness['connected_lie_term']}.
  In contrast, all 60 same-ray opposite-sheet brackets vanish exactly because
  F20 conjugate(psi_l^3)=chi_l tensor psi_l and psi_l wedge psi_l=0.

General source formula
  <0|J_1(a^dag)J_1(b^dag)J_-1(c)J_-1(d)|0>
    = kappa(b^dag,c) kappa(a^dag,d)
    + kappa(b^dag,d) kappa(a^dag,c)
    + kappa(a^dag,[[b^dag,c],d]).

Boundary
  Exact only inside the already assumed compact-adjoint affine E8 level-one
  vacuum.  No raw seam operator, frame preparation, neutral instrument,
  spacetime transport, or physical matter selector is derived.

Checks
  {sum(CHECKS.values())} unconditional evaluations; run identically with
  normal Python and python -OO.  Machine-readable phases and all witness
  coordinates are in current_bracket_dictionary.json.
"""
    OUT_TXT.write_text(text, encoding="utf-8")
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "checks": sum(CHECKS.values()),
                "mixed_image": 30,
                "coordinate_fourpoint": 2,
                "frame_labels": witness["labels"],
                "frame_connected": witness["connected_lie_term"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
