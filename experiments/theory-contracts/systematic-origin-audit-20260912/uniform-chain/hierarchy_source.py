"""Exact NON-RH primitive-H4 hierarchy countermodel; no physical selection."""
import ast
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = "experiments/theory-contracts/compiler-clifford-bridge/checker.py"
PIN = "bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d"
CHECKS = 0


def require(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(message)


def run():
    path = ROOT / SOURCE
    require(hashlib.sha256(path.read_bytes()).hexdigest() == PIN, "original source pin")
    tree = ast.parse(path.read_text())
    nodes = [node for node in tree.body
             if isinstance(node, ast.FunctionDef) and node.name == "generators"]
    require(len(nodes) == 1, "reviewed original generator definition")
    env = {"s": s}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), env)
    g = env["generators"]()
    a = tuple(s.I * v for v in g)
    eye, identity = s.eye(4), s.eye(16)
    Q = tuple(s.kronecker_product(v, v.conjugate()) for v in g)
    for q in Q:
        require(q.H == q and q ** 2 == identity,
                "primitive mismatch is an orthogonal projector")
    h4 = sum(((identity - q) / 2 for q in Q), s.zeros(16))
    centered = h4 - 2 * identity
    require(h4.H == h4, "primitive comparison is Hermitian")
    require(s.trace(h4) / 16 == 2, "primitive mean two")
    require(s.trace(centered) == 0, "primitive centered mean zero")
    require(s.trace(centered ** 2) / 16 == 1, "primitive normalized variance one")
    require(centered == -sum((s.kronecker_product(v, v.conjugate())
                             for v in a), s.zeros(16)) / 2,
            "centered primitive tensor formula")
    for i, v in enumerate(a):
        require(v.H == v and s.trace(v) == 0, "traceless Hermitian endpoint")
        for j, z in enumerate(a):
            require(s.trace(v * z) / 4 == int(i == j), "orthonormal endpoint basis")
    w = (eye + g[0] * g[1] + g[1] * g[2] + g[2] * g[0]) / 2
    for u in (*g, w):
        require(u * u.H == eye, "source operation unitary")
        dual = s.kronecker_product(u, u.conjugate())
        require(dual * h4 * dual.H == h4, "actual primitive/family edge covariance")
    swap = s.zeros(16)
    for i in range(4):
        for j in range(4):
            swap[4 * j + i, 4 * i + j] = 1
    require(swap * h4 * swap == h4, "actual chart reversed edge has same matrix")
    partial_left = s.Matrix(4, 4, lambda i, j: sum(centered[4*k+i, 4*k+j]
                                                  for k in range(4)))
    partial_right = s.Matrix(4, 4, lambda i, j: sum(centered[4*i+k, 4*j+k]
                                                   for k in range(4)))
    require(partial_left == s.zeros(4) and partial_right == s.zeros(4),
            "centered local partial traces vanish")
    left = s.kronecker_product(centered, eye)
    right = s.kronecker_product(eye, centered)
    require(s.trace(left * right) / 64 == 0, "adjacent centered edges orthogonal")
    require(s.trace(left ** 2) / 64 == 1, "embedded primitive variance unchanged")
    r, t, lam = s.symbols("r t lambda", positive=True)
    total = r + t
    scale = total / (r + t * lam)
    excess = s.factor(scale ** 2 * (r + t * lam ** 2) - total)
    expected = total * r * t * (1 - lam) ** 2 / (r + t * lam) ** 2
    require(s.simplify(excess - expected) == 0, "all-length same-mean variance difference")
    require(s.simplify(excess.subs(lam, 1)) == 0, "uniform negative control")
    for m in range(2, 9):
        for value in (s.Rational(1, 10), s.Rational(1, 2), s.Rational(9, 10)):
            require(excess.subs({r: 2*m, t: m-1, lam: value}) > 0,
                    "connected positive-weight trimer witness")
    # Flat Bell is a separate stronger-symmetry illustration, not the main model.
    phi = eye.reshape(16, 1) / 2
    flat = identity - phi * phi.H
    require(flat != h4, "flat Bell parent not substituted for primitive parent")
    require(s.trace(flat) / 16 == s.Rational(15, 16), "separate flat mean")
    require(s.trace((flat - s.Rational(15, 16) * identity) ** 2) / 16
            == s.Rational(15, 256), "separate flat variance")
    return {"checks": CHECKS, "primary_model": "original four-generator H4",
            "local_normalized_mean": 2, "local_normalized_variance": 1,
            "distinct_centered_edge_covariance": 0,
            "variance_excess": "M*r*s*(1-lambda)^2/(r+s*lambda)^2",
            "source_pin": {SOURCE: PIN}, "graph_or_weak_links_selected": False,
            "T1_T8_closed": []}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
