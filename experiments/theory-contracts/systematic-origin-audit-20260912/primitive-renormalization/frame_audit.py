"""Exact NON-RH audit of source marking versus assumed energy isotropy.

Read-only original-source pins; all guards survive -OO. No physical promotion.
"""
import ast
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[4]
PINS = {
    "verification/v752_projective_hamming_incidence.py": "9d3b20e18493937546bf69c37978b0df327b2d2b2a4d6985c387224acd4a61d2",
    "verification/v774_arf_spinor_compiler.py": "3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c",
    "verification/v783_two_qubit_clifford.py": "8f4851634b83f61671b04f3a6211059c40758d21caaf1f779302c799e1e9d6c4",
    "verification/v975_dimension_selector_4d.py": "e9e31593b4a2eb4c15384f83a936aeee1474fcce5f2702a6df37147800407673",
    "experiments/theory-contracts/compiler-clifford-bridge/checker.py": "bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d",
}
CHECKS = 0


def require(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(message)


def original_functions(path, names, environment):
    tree = ast.parse((ROOT / path).read_text())
    selected = [node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name in names]
    require({node.name for node in selected} == set(names), "reviewed source functions")
    exec(compile(ast.Module(body=selected, type_ignores=[]), path, "exec"), environment)
    return environment


def flat(matrix):
    return matrix.reshape(matrix.rows * matrix.cols, 1)


def covariance_matrix(basis, operations):
    return s.Matrix.vstack(*(s.Matrix.hstack(*(
        flat((u * b * u.adjoint() - b).expand()) for b in basis))
        for u in operations))


def run():
    for path, digest in PINS.items():
        require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest,
                "original source pin " + path)
    env = original_functions("experiments/theory-contracts/compiler-clifford-bridge/checker.py",
                             ("generators",), {"s": s})
    source = original_functions("verification/v774_arf_spinor_compiler.py",
                                ("sig_bits", "iota"), {})
    g = env["generators"]()
    eye, identity, zero = s.eye(4), s.eye(16), s.zeros(16)
    for i in range(4):
        require(g[i].adjoint() == -g[i] and g[i] * g[i] == -eye,
                "source skew-Hermitian normalized primitive")
        for j in range(i):
            require(g[i] * g[j] == -g[j] * g[i], "source Clifford relation")
    Q = tuple(s.kronecker_product(x, x.conjugate()) for x in g)
    a = tuple(s.I * x for x in g)
    D = tuple(s.kronecker_product(x, eye) - s.kronecker_product(eye, x.T)
              for x in a)
    penalties = tuple((identity - q) / 2 for q in Q)
    for i in range(4):
        require(D[i].adjoint() == D[i] and D[i] ** 2 / 4 == penalties[i],
                "Hermitian difference squared equals mismatch penalty")
    w = (eye + g[0] * g[1] + g[1] * g[2] + g[2] * g[0]) / 2
    require(w * w.adjoint() == eye, "source family lift unitary")
    for i, j in enumerate((1, 2, 0, 3)):
        require(w * g[i] * w.adjoint() == g[j], "source marked cycle")
    W = s.kronecker_product(w, w.conjugate())

    # H(C)=1/4 sum_ij C_ij D_i D_j for real symmetric C.
    labels = [(i, j) for i in range(4) for j in range(i, 4)]
    basis = [D[i] ** 2 / 4 if i == j else (D[i] * D[j] + D[j] * D[i]) / 4
             for i, j in labels]
    require(s.Matrix.hstack(*(flat(b) for b in basis)).rank() == 10,
            "quadratic coefficient-to-operator map injective")
    cycle_constraints = covariance_matrix(basis, (W,))
    word_constraints = covariance_matrix(basis, Q)
    all_constraints = cycle_constraints.col_join(word_constraints)
    require(cycle_constraints.rank() == 6, "cycle alone leaves four quadratic coefficients")
    require(word_constraints.rank() == 6, "primitive record covariance leaves four diagonal coefficients")
    require(all_constraints.rank() == 8, "source marked covariance leaves exactly two coefficients")
    family = sum(penalties[:3], zero)
    anchor = penalties[3]
    family_coeff = s.Matrix([int(i == j and i < 3) for i, j in labels])
    anchor_coeff = s.Matrix([int(i == j == 3) for i, j in labels])
    require(all_constraints * family_coeff == s.zeros(all_constraints.rows, 1), "family direction allowed")
    require(all_constraints * anchor_coeff == s.zeros(all_constraints.rows, 1), "anchor direction allowed")

    # This is an unmarked frame rotation, not an inferred physical symmetry.
    r = (eye + g[2] * g[3]) / s.sqrt(2)
    require((r * r.adjoint()).expand() == eye, "additional Spin-frame rotation unitary")
    require((r * g[2] * r.adjoint()).expand() == g[3], "extra frame operation sends family to anchor")
    require((r * g[3] * r.adjoint()).expand() == -g[2], "extra frame operation changes marked anchor")
    R = s.kronecker_product(r, r.conjugate()).expand()
    extra_constraints = all_constraints.col_join(covariance_matrix(basis, (R,)))
    require(extra_constraints.rank() == 9, "extra anchor-family symmetry leaves exactly one coefficient")
    h_equal = family + anchor
    h_unequal = family + 2 * anchor
    require(R * h_equal * R.adjoint() == h_equal, "equal primitive weights satisfy added isotropy")
    require(R * h_unequal * R.adjoint() != h_unequal, "anisotropy detected by added symmetry")
    require((R * h_unequal * R.adjoint() - h_unequal).expand()
            == penalties[2] - penalties[3], "explicit nonzero anisotropy residual")

    words = tuple(itertools.product((0, 1), repeat=4))
    matrices = []
    for v in words:
        matrix = eye
        for bit, generator in zip(v, g):
            if bit:
                matrix *= generator
        matrices.append(matrix)
    bell_basis = s.Matrix.hstack(*(flat(u) / 2 for u in matrices))
    require(bell_basis.adjoint() * bell_basis == identity, "complete exact word Bell basis")
    qstar = {v: (sum(source["iota"](v)) // 2) % 2 for v in words}
    q1 = [v for v in words if qstar[v] == 1]
    require(Counter(sum(v) for v in q1) == {1: 4, 2: 6}, "source ten-word orbit is primitives plus bivectors")
    require(all(source["sig_bits"](v) == (v[2], v[0], v[1], v[3]) for v in words),
            "actual sigma keeps anchor bit separate")
    # Source S5 acts by all permutations of the five parity-lift slots.
    orbit = set()
    e1 = (1, 0, 0, 0)
    for permutation in itertools.permutations(range(5)):
        lifted = source["iota"](e1)
        orbit.add(tuple(lifted[j] for j in permutation)[:4])
    require(orbit == set(q1), "S5 does not preserve the four-word primitive support")
    word_penalties = [(identity - s.kronecker_product(u, u.conjugate())) / 2
                      for u in matrices]
    h10 = sum((p for v, p in zip(words, word_penalties) if qstar[v] == 1), zero)
    bivectors = sum((p for v, p in zip(words, word_penalties) if sum(v) == 2), zero)
    require(h10 == h_equal + bivectors, "ten-word completion is primitive plus grade-two penalties")
    require(h10 == 5 * h_equal - h_equal ** 2, "exact ten-word polynomial in primitive parent")
    spectra = {}
    for name, h in (("equal", h_equal), ("anisotropic_J1_K2", h_unequal), ("ten_word", h10)):
        diagonal = bell_basis.adjoint() * h * bell_basis
        require(diagonal.is_diagonal(), "complete exact spectrum " + name)
        values = list(diagonal.diagonal())
        require(values[0] == 0 and all(value > 0 for value in values[1:]),
                "unique Bell ground " + name)
        require(all(u * h * u.adjoint() == h for u in (*Q, W)),
                "all actual marked source operations preserve " + name)
        spectra[name] = dict(sorted(Counter(map(int, values)).items()))
    require(spectra["equal"] == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}, "equal binomial spectrum")
    require(spectra["anisotropic_J1_K2"] == {0: 1, 1: 3, 2: 4, 3: 4, 4: 3, 5: 1},
            "genuinely inequivalent same-gap anisotropic witness")
    d10 = list((bell_basis.adjoint() * h10 * bell_basis).diagonal())
    for v, energy in zip(words, d10):
        count = sum(sum(v[i] * u[j] for i in range(4) for j in range(4)
                        if i != j) % 2 for u in q1)
        require(energy == count, "independent original binary-pairing energy count")
        require(energy == (0 if not any(v) else 6 if qstar[v] else 4),
                "ten-word spectrum by original Arf orbit")
    require(spectra["ten_word"] == {0: 1, 4: 5, 6: 10}, "S5-completed spectrum")
    h15 = sum(word_penalties, zero)
    phi = flat(eye) / 2
    require(h15 == 8 * (identity - phi * phi.adjoint()), "full word orbit yields flat parent")
    return {"checks": CHECKS, "quadratic_covariance_dimensions": {
        "family_cycle": 4, "primitive_dual_records": 4, "both": 2,
        "both_plus_anchor_family_rotation": 1}, "spectra": spectra,
        "original_source_pins": PINS, "physical_energy_selection_proven": False,
        "T1_T8_closed": []}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
