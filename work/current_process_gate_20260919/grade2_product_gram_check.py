#!/usr/bin/env python3
"""Exact Shapovalov/Gram test for the mixed W20-W4 grade-two product.

This checker starts from the original E8 roots and compact Chevalley source.
It does not assume that PBW words are independent: the level-one connected
Lie term is included and an explicit null-word control is required.
"""

from __future__ import annotations

import ast
import hashlib
import itertools as it
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "grade2_product_gram_check.json"
CHECKS: Counter[str] = Counter()
PINS = {
    "verification/v1_e8_glue.py":
        "1978d66a85974e5fa189cf4dec507f9be4c4dcc113e90eb1b33a9aae9259a0d7",
    "verification/v498_celestial_wp5b_singular_vector.py":
        "9f5a2d62523283595b754fea6f70ddc6501a251daf86752cbc67ded252b96180",
    "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json":
        "a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3",
    "experiments/theory-contracts/compiler-current-descendant-20260919/PROOF.txt":
        "ad45198c44b84365a862b709e8b7e49af708f2e1a58adff67dc55d7cf4fa459b",
    "experiments/theory-contracts/compiler-current-descendant-20260919/checker.py":
        "b342a8b102d9b1dedf150ccbd4812ccb26fa1b9a4b7cb70401b6cdd8201b4420",
}


def require(ok: object, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS[label] += 1


class Always(ast.NodeTransformer):
    """Keep assertions in extracted original definitions under python -OO."""

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
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    node = next(
        item for item in tree.body
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


def clean(vector: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    return {
        index: sp.simplify(value)
        for index, value in vector.items()
        if sp.simplify(value) != 0
    }


def main() -> None:
    for path, digest in PINS.items():
        require(
            hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest,
            "source pin " + path,
        )

    triality = json.loads(
        (ROOT / "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json")
        .read_text(encoding="utf-8")
    )
    basis = sp.Matrix(triality["integral_triality"]["vector_basis"])
    raw_roots = original(
        "verification/v1_e8_glue.py", "e8_roots", {"np": np, "itertools": it}
    )()
    roots = [tuple(int(2 * x) for x in root) for root in raw_roots]
    rootset = set(roots)
    require(len(rootset) == 240, "original E8 root count")
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
        "verification/v498_celestial_wp5b_singular_vector.py",
        "Chevalley",
        {"F": F, "ip": ip, "vadd": add},
    )(RootAdapter())
    require(
        chevalley.sgn == chevalley.kappa_root == -1,
        "original compact Chevalley convention",
    )

    def raw_sign(left: tuple[int, ...], right: tuple[int, ...]) -> int:
        target = add(left, right)
        out = chevalley.bracket(chevalley.ridx[left], chevalley.ridx[right])
        if target not in rootset:
            require(not out, "absent root sum has zero bracket")
            return 0
        require(
            out == {chevalley.ridx[target]: F(out[chevalley.ridx[target]])}
            and out[chevalley.ridx[target]] in (-1, 1),
            "present root sum has unit cocycle",
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
        (i, a): tuple(-1 if j == i else 1 for j in range(5)) + family_weights[a]
        for i in range(5)
        for a in range(4)
    }
    require(
        set(w4.values()) | set(w20.values()) <= rootset,
        "all W24 directions are original E8 roots",
    )

    family_simple = {a: sub(w4[a + 1], w4[a]) for a in range(3)}
    carrier_simple = {i: sub(w20[i + 1, 0], w20[i, 0]) for i in range(4)}
    q: dict[int, int] = {0: 1}
    for a in range(3):
        q[a + 1] = q[a] * raw_sign(family_simple[a], w4[a])
    p: dict[tuple[int, int], int] = {(0, 0): 1}
    for a in range(3):
        p[0, a + 1] = p[0, a] * raw_sign(family_simple[a], w20[0, a])
    for a in range(4):
        for i in range(4):
            p[i + 1, a] = p[i, a] * raw_sign(carrier_simple[i], w20[i, a])
    require(
        all(value in (-1, 1) for value in q.values())
        and all(value in (-1, 1) for value in p.values()),
        "transport phases are signs",
    )
    for a in range(3):
        for i in range(5):
            require(
                p[i, a] * raw_sign(family_simple[a], w20[i, a]) == p[i, a + 1],
                "A3 simple transport is path independent",
            )
    for i in range(4):
        for a in range(4):
            require(
                p[i, a] * raw_sign(carrier_simple[i], w20[i, a]) == p[i + 1, a],
                "SU5 simple transport is path independent",
            )

    def basis_vector(root: tuple[int, ...], phase: int) -> dict[int, sp.Expr]:
        return {chevalley.ridx[root]: sp.Integer(phase)}

    c = {a: basis_vector(w4[a], q[a]) for a in range(4)}
    x = {
        (i, a): basis_vector(w20[i, a], p[i, a])
        for i in range(5)
        for a in range(4)
    }

    def bracket(left: dict[int, sp.Expr], right: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
        out: dict[int, sp.Expr] = {}
        for i, u in left.items():
            for j, v in right.items():
                for k, coefficient in chevalley.bracket(i, j).items():
                    value = sp.Rational(coefficient.numerator, coefficient.denominator)
                    out[k] = out.get(k, 0) + u * v * value
        return clean(out)

    def dagger(vector: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
        out: dict[int, sp.Expr] = {}
        for index, value in vector.items():
            if index < 240:
                opposite = chevalley.opp[index]
                out[opposite] = out.get(opposite, 0) - sp.conjugate(value)
            else:
                out[index] = out.get(index, 0) + sp.conjugate(value)
        return clean(out)

    def kappa(left: dict[int, sp.Expr], right: dict[int, sp.Expr]) -> sp.Expr:
        value = sp.Integer(0)
        for i, u in left.items():
            for j, v in right.items():
                coefficient = chevalley.kappa(i, j)
                if coefficient:
                    value += u * v * sp.Rational(
                        coefficient.numerator, coefficient.denominator
                    )
        return sp.simplify(value)

    def fourpoint(
        a: dict[int, sp.Expr],
        b: dict[int, sp.Expr],
        cket: dict[int, sp.Expr],
        dket: dict[int, sp.Expr],
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
        """<0|J1(a^dag)J1(b^dag)J-1(cket)J-1(dket)|0>."""
        ad, bd = dagger(a), dagger(b)
        direct = kappa(bd, cket) * kappa(ad, dket)
        exchange = kappa(bd, dket) * kappa(ad, cket)
        connected = kappa(ad, bracket(bracket(bd, cket), dket))
        total = sp.simplify(direct + exchange + connected)
        return tuple(sp.simplify(v) for v in (total, direct, exchange, connected))

    # Exact wedge phase: the two off-diagonal brackets cancel in Sym^2(4).
    for i in range(5):
        for a, b in it.combinations(range(4), 2):
            left = bracket(c[a], x[i, b])
            right = bracket(c[b], x[i, a])
            require(bool(left), "mixed wedge bracket is nonzero")
            summed = dict(left)
            for index, value in right.items():
                summed[index] = summed.get(index, 0) + value
            require(not clean(summed), "symmetric mixed bracket cancels exactly")

    # T(i,aa)=X_ia C_a; T(i,ab)=(X_ia C_b+X_ib C_a)/sqrt(2).
    labels: list[tuple[int, int, int]] = []
    terms: list[list[tuple[sp.Expr, dict[int, sp.Expr], dict[int, sp.Expr]]]] = []
    for i in range(5):
        for a in range(4):
            for b in range(a, 4):
                labels.append((i, a, b))
                if a == b:
                    terms.append([(sp.Integer(1), x[i, a], c[a])])
                else:
                    terms.append([
                        (1 / sp.sqrt(2), x[i, a], c[b]),
                        (1 / sp.sqrt(2), x[i, b], c[a]),
                    ])
    require(len(labels) == 50, "bar5 tensor Sym2(4) basis dimension")

    gram = sp.zeros(50)
    for row in range(50):
        for column in range(50):
            value = sp.Integer(0)
            for left_coefficient, left_x, left_c in terms[row]:
                for right_coefficient, right_x, right_c in terms[column]:
                    value += (
                        sp.conjugate(left_coefficient)
                        * right_coefficient
                        * fourpoint(left_x, left_c, right_c, right_x)[0]
                    )
            gram[row, column] = sp.simplify(value)
    require(gram == sp.eye(50), "full mixed-product Gram matrix is identity")

    # Controls prove that the computation did not silently use a free-boson
    # tensor Gram matrix and does see the irreducible level-one quotient.
    active = fourpoint(x[0, 1], c[0], c[0], x[0, 1])
    null = fourpoint(c[1], c[0], c[0], c[1])
    require(active == (2, 1, 0, 1), "connected mixed-coordinate control")
    require(null == (0, 1, 0, -1), "level-one null-word control")

    result = {
        "research_id": "UR.COMPILER.GRADE2.PRODUCT.GRAM.20260919",
        "verdict": "EXACT_ISOMETRIC_GRADE2_PRODUCT_INTERTWINER",
        "premise": "original compact-adjoint affine E8 level-one vacuum",
        "representation": "bar5 tensor Sym2(4)",
        "basis_formula": {
            "diagonal": "T(i,aa)=J_-1(X_i_a) J_-1(C_a) Omega",
            "off_diagonal": (
                "T(i,ab)=[J_-1(X_i_a)J_-1(C_b)+"
                "J_-1(X_i_b)J_-1(C_a)]Omega/sqrt(2), a<b"
            ),
        },
        "dimension": len(labels),
        "gram": {
            "equals_identity": True,
            "rank": int(gram.rank()),
            "nullity": 50 - int(gram.rank()),
            "diagonal_values": sorted({str(value) for value in gram.diagonal()}),
            "nonzero_off_diagonal": sum(
                gram[i, j] != 0 for i in range(50) for j in range(50) if i != j
            ),
        },
        "quotient_controls": {
            "connected_mixed_coordinate": [str(value) for value in active],
            "positive_inner_product_null_word": [str(value) for value in null],
        },
        "phase_gauge": {
            "reference": "C_0=X_0_0=+ raw Chevalley vector",
            "q": [q[a] for a in range(4)],
            "p_rows": [[p[i, a] for a in range(4)] for i in range(5)],
        },
        "interpretation": (
            "The symmetric W20-W4 product survives the E8_1 null quotient "
            "as a normalized equivariant 50-space; this is not inferred from dimension."
        ),
        "source_sha256": PINS,
        "check_evaluations": sum(CHECKS.values()),
        "checks": dict(sorted(CHECKS.items())),
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "checks"}, sort_keys=True))


if __name__ == "__main__":
    main()
