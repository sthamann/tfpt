"""The original 24 currents give two conformal readings of one E8 source.

All finite claims below use the original doubled E8 root coordinates and
Chevalley brackets. The common Virasoro vector is identified by orthogonal
Cartan projectors, not inferred merely from matching central charges.
This does not identify the conformal parameter with physical raw-seam time.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from typing import Any

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from .current_block_geometry import _actual_current_source


def _matrix_json(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(value) for value in row] for row in matrix.tolist()]


def _root_closure(chevalley: Any, roots: set[tuple[int, ...]]) -> tuple[set[int], list[int]]:
    """Close the supplied ORIGINAL currents under their actual brackets."""
    known = {chevalley.ridx[root] for root in roots}
    frontier, counts = set(known), [len(known)]
    while frontier:
        new = {
            output
            for left in frontier for right in known
            for output, coefficient in chevalley.bracket(left, right).items()
            if coefficient and output < chevalley.nR
        } - known
        if not new:
            break
        known.update(new)
        frontier = new
        counts.append(len(known))
    return known, counts


@lru_cache(maxsize=1)
def build_source_unification_data() -> dict[str, Any]:
    """Return exact source identities and the conditional quantization route."""
    source = _actual_current_source()
    chevalley, xs = source["chevalley"], source["w20"]
    roots = sorted(chevalley.ridx)
    family = [(-1, -1, -1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]
    cs = [(-1,) * 5 + weight for weight in family]
    vectors = {root: sp.Matrix(root) for root in roots}
    simple = sp.Matrix.hstack(
        *[vectors[xs[i + 1, 0]] - vectors[xs[i, 0]] for i in range(4)],
        -vectors[xs[4, 0]],
        *[vectors[xs[0, a]] - vectors[xs[0, a + 1]] for a in range(3)],
    )
    gram = simple.T * simple / 4
    a8_cartan = sp.Matrix(8, 8, lambda i, j: 2 if i == j else -int(abs(i-j) == 1))
    inverse = simple.inv()
    cosets = {root: tuple(value % 1 for value in inverse * vector)
              for root, vector in vectors.items()}
    zero = (sp.Integer(0),) * 8
    generator = cosets[cs[0]]
    opposite = tuple((-value) % 1 for value in generator)
    counts = Counter(cosets.values())
    dominant = {
        key: [list(simple.T * vectors[root] / 4)
              for root in roots if cosets[root] == key
              and all(value >= 0 for value in simple.T * vectors[root] / 4)]
        for key in (zero, opposite, generator)
    }

    # An actual E8 lattice basis: 2e1, e1+e_j (j=2..7), s=(1/2)^8.
    # 2e1 is a sum of two original integer roots; s=-C_0 is original too.
    unit = sp.eye(8)
    e8_basis = sp.Matrix.hstack(2*unit[:, 0],
                               *[unit[:, 0]+unit[:, j] for j in range(1, 7)],
                               -vectors[cs[0]]/2)
    e8_gram = e8_basis.T * e8_basis
    inclusion = e8_basis.inv() * simple / 2
    smith = smith_normal_form(inclusion, domain=sp.ZZ)
    smith_diagonal = [abs(int(smith[i, i])) for i in range(8)]
    native_basis = (
        tuple(2*(unit[:, 0]+unit[:, 1])) in chevalley.ridx
        and tuple(2*(unit[:, 0]-unit[:, 1])) in chevalley.ridx
        and all(tuple(2*(unit[:, 0]+unit[:, j])) in chevalley.ridx for j in range(1, 7))
        and tuple(-vectors[cs[0]]) in chevalley.ridx
    )
    lattice_exact = (
        native_basis and e8_gram.det() == 1
        and all(value.is_Integer for value in e8_gram)
        and all(e8_gram[i, i] % 2 == 0 for i in range(8))
        and all(value.is_Integer for value in inclusion)
        and all(value.is_Integer for root in roots for value in e8_basis.inv()*vectors[root]/2)
    )

    x_roots = set(xs.values())
    x_roots |= {tuple(-value for value in root) for root in x_roots}
    a8_closed, a8_rounds = _root_closure(chevalley, x_roots)
    complete_roots = x_roots | set(cs) | {tuple(-value for value in root) for root in cs}
    complete_closed, complete_rounds = _root_closure(chevalley, complete_roots)
    a8_exact = a8_closed == {chevalley.ridx[root] for root in roots if cosets[root] == zero}

    p4 = sp.zeros(8)
    p4[:5, :5] = sp.eye(5) - sp.ones(5)/5
    p3 = sp.diag(0, 0, 0, 0, 0, 1, 1, 1)
    p1 = sp.zeros(8)
    p1[:5, :5] = sp.ones(5)/5
    p5 = sp.diag(1, 1, 1, 1, 1, 0, 0, 0)
    projectors = [p4, p3, p1]
    orthogonal = all(left*right == (left if i == j else sp.zeros(8))
                     for i, left in enumerate(projectors) for j, right in enumerate(projectors))
    source_spans = (
        sp.Matrix.hstack(*[vectors[root] for root in roots if not any(root[5:])]).rank() == 5
        and sp.Matrix.hstack(*[vectors[root] for root in roots if not any(root[:5])]).rank() == 3
        and simple[:, :4].rank() == 4 and simple[:, 5:].rank() == 3
        and p4*simple[:, :4] == simple[:, :4]
        and p3*simple[:, 5:] == simple[:, 5:]
    )
    h_u1 = sp.Matrix([1/sp.sqrt(5)]*5 + [0]*3)
    y_p2 = sp.Matrix([sp.Rational(-1, 3)]*3 + [sp.Rational(1, 2)]*2 + [0]*3)

    def weights(root: tuple[int, ...]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        vector = vectors[root]/2
        return tuple((vector.T*projector*vector)[0]/2 for projector in projectors)

    x_weights = {weights(root) for root in xs.values()}
    c_weights = {weights(root) for root in cs}
    expected_x = (sp.Rational(2, 5), sp.Rational(3, 8), sp.Rational(9, 40))
    expected_c = (sp.Integer(0), sp.Rational(3, 8), sp.Rational(5, 8))
    x_charges = {sp.simplify((h_u1.T*vectors[root])[0]/2) for root in xs.values()}
    c_charges = {sp.simplify((h_u1.T*vectors[root])[0]/2) for root in cs}
    grade_exact = (counts == {zero: 72, generator: 84, opposite: 84}
                   and generator != zero and tuple((3*x) % 1 for x in generator) == zero
                   and all(cosets[root] == generator for root in cs))
    expected_highest = [
        [[1, 0, 0, 0, 0, 0, 0, 1]],
        [[0, 0, 1, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 1, 0, 0]],
    ]
    highest_exact = [dominant[key] for key in (zero, opposite, generator)] == expected_highest
    stress_exact = orthogonal and sum(projectors, sp.zeros(8)) == sp.eye(8) and p4+p1 == p5

    def check(name: str, ok: Any, actual: Any, expected: Any, method: str) -> dict[str, Any]:
        return {"name": name, "ok": bool(ok), "actual": actual, "expected": expected, "method": method}

    checks = [
        check("Die wirklichen X-Ströme erzeugen A8 im ursprünglichen E8", a8_exact and gram == a8_cartan,
              {"root_rounds": a8_rounds, "determinant": int(gram.det())},
              {"root_rounds": [40, 72], "determinant": 9},
              "Original Chevalley brackets and doubled-root Gram matrix"),
        check("Die ganze Ladungserweiterung ist E8/A8 = Z3", lattice_exact and smith_diagonal == [1]*7+[3] and grade_exact,
              {"Smith": smith_diagonal, "root_classes": [counts[zero], counts[opposite], counts[generator]]},
              {"Smith": [1]*7+[3], "root_classes": [72, 84, 84]},
              "Integral lattice inclusion, Smith normal form and all 240 original root coordinates"),
        check("Die ursprünglichen vier C-Ströme gehören derselben Lambda6-Erweiterung an", highest_exact and grade_exact,
              {"C4_class": [str(v) for v in generator], "highest_weight": [str(v) for v in dominant[generator][0]]},
              {"C4_class": ["1/3", "2/3", "0", "1/3", "2/3", "0", "1/3", "2/3"],
               "highest_weight": ["0", "0", "0", "0", "0", "1", "0", "0"]},
              "Actual A8 Dynkin labels and lattice residues, not dimension matching"),
        check("Die gesamte ursprüngliche 24-Strom-Signatur erzeugt E8", len(complete_closed) == 240 and simple.rank() == 8,
              {"root_rounds": complete_rounds, "Cartan_rank": int(simple.rank())},
              {"root_rounds": [48, 140, 240], "Cartan_rank": 8},
              "Original C4+X20 and adjoints under exact Chevalley closure"),
        check("Beide Zerlegungen haben denselben Virasorovektor", stress_exact and source_spans,
              {"projector_ranks": [int(p.rank()) for p in projectors], "sum": _matrix_json(sum(projectors, sp.zeros(8)))},
              {"projector_ranks": [4, 3, 1], "sum": _matrix_json(sp.eye(8))},
              "Orthogonal projector identity in the same eight Heisenberg currents; level-one simply-laced lattice Sugawara formula"),
        check("Alle 24 Quellfelder haben im gemeinsamen Stress-Tensor Gewicht eins", x_weights == {expected_x} and c_weights == {expected_c},
              {"X20": [str(v) for v in next(iter(x_weights))], "C4": [str(v) for v in next(iter(c_weights))]},
              {"X20": ["2/5", "3/8", "9/40"], "C4": ["0", "3/8", "5/8"]},
              "Exact half squared projected charge norms of every original field"),
        check("Der zusätzliche U1-Strom ist orthogonal zur P2-Hyperladung", h_u1.dot(y_p2) == 0 and h_u1.dot(h_u1) == 1 and y_p2.dot(y_p2) == sp.Rational(5, 6),
              {"inner_product": str(h_u1.dot(y_p2)), "P2_norm": str(y_p2.dot(y_p2))},
              {"inner_product": "0", "P2_norm": "5/6"},
              "Original diagonal P2 root frame and normalized complementary Cartan direction"),
    ]
    sectors = []
    for label, key, dimension, module in [
        ("A8-Ströme", zero, 80, "V_A8"),
        ("Erweiterung Lambda3", opposite, 84, "V_(A8+Lambda3)"),
        ("Erweiterung Lambda6", generator, 84, "V_(A8+Lambda6)"),
    ]:
        sectors.append({"label": label, "module": module, "root_count": counts[key],
                        "weight_one_dimension": dimension, "residue": [str(v) for v in key],
                        "highest_weight": [str(v) for v in dominant[key][0]],
                        "highest_weight_scope": "Höchstes Gewicht des Gewicht-eins-Raums; das affine V_A8-Modul selbst ist das Vakuummodul.",
                        "affine_module_highest_weight": "0" if key == zero else "Lambda3" if key == opposite else "Lambda6"})
    data = {
        "title": "Zwei Beschreibungen, ein vollständiger Quellprozess",
        "summary": "Die alte 5+3-Quelle und die neue 5×4-Stromrekursion liegen im selben E8. Ihre Felder, ihr Vakuum und ihr konformer Zeitgenerator passen zusammen.",
        "chain": ["X20 und Adjungierte → A8-Ströme", "Die vorhandenen C4 öffnen die Z3-Ladungserweiterung", "24 Ströme und Adjungierte → ganz E8", "Ein gemeinsamer Virasorovektor → dieselbe intrinsische konforme Zeit"],
        "a8_extension": {
            "simple_roots_doubled": _matrix_json(simple.T), "coordinate_convention": "Zeilen sind ursprüngliche doppelte Wurzelkoordinaten; Skalarprodukt = r·s/4.",
            "gram_matrix": _matrix_json(gram), "determinant": int(gram.det()),
            "E8_determinant": int(e8_gram.det()), "lattice_index": abs(int(inclusion.det())),
            "embedding_index": 1, "level": "A8 bei Level 1 innerhalb derselben E8-Level-1-Quelle; alle einfachen Wurzeln haben dieselbe Norm 2.",
            "quotient": "E8/A8 = Z3", "smith_diagonal": smith_diagonal,
            "sectors": sectors, "C4_sector": "Lambda6", "C4_highest_field": "C_0",
            "X20_root_closure": a8_rounds, "full24_root_closure": complete_rounds,
            "voa_decomposition": "V_E8 = V_A8 ⊕ V_(A8+Lambda3) ⊕ V_(A8+Lambda6)",
            "meaning": "A8 hat vollen Rang. Seine 80 Ströme und die beiden 84er-Sektoren ergeben dieselben 248 E8-Ströme. Die Erweiterung ist schon in den ursprünglichen C-Feldern vorhanden.",
        },
        "shared_stress_tensor": {
            "identity": "T_E8 = T_A8 = T_A4 + T_A3 + T_u1 = T_D5 + T_A3",
            "virasoro_vector": "omega = (1/2) sum_(j=1)^8 h_j(-1)^2 Omega",
            "projector_sum_exact": bool(stress_exact),
            "projectors": {"A4": _matrix_json(p4), "A3": _matrix_json(p3), "u1": _matrix_json(p1), "D5": _matrix_json(p5)},
            "central_charges": {"E8_1": "248/31 = 8", "A8_1": "80/10 = 8", "A4_1": "4", "A3_1": "3", "u1": "1", "D5_1": "5"},
            "weights": [
                {"field": "X20", "representation": "bar(5) tensor 4", "A4": "2/5", "A3": "3/8", "u1": "9/40", "total": "1", "u1_charge": str(next(iter(x_charges)))},
                {"field": "C4", "representation": "1 tensor 4", "A4": "0", "A3": "3/8", "u1": "5/8", "total": "1", "u1_charge": str(next(iter(c_charges)))},
            ],
            "meaning": "Die Projektoren summieren sich zur Identität auf denselben acht Strömen. Deshalb stimmen der Stress-Tensor und alle seine Virasoromoden überein; es ist mehr als die gleiche Zentralzahl.",
            "u1_direction": [str(v) for v in h_u1],
            "time_scope": "Identisch ist die intrinsische konforme Zeit L0 im selben Vakuummodell. Eine physische Messzeit oder der alte diskrete Compiler-Transfer ist dadurch noch nicht identifiziert.",
        },
        "direct_quantization": {
            "formula": "markiertes E8-Gitter + Kokzyklus → V_E8 mit Omega und L0 → lokales E8_1-Netz",
            "source": "H = direct_sum_(lambda in E8) Fock_lambda; alle geladenen Vertexfelder bleiben erhalten",
            "vacuum": "Omega = |0>; der gemeinsame positive Vakuumzustand bestimmt mit der Stromalgebra sämtliche Wortkorrelationen",
            "intrinsic_time": "L0 = |lambda|^2/2 + sum_(j,n>0) n N_(j,n)",
            "origin_assumption": "Die physische TFPT-Quelle ist die minimale positive lokale Level-1-Vakuumquantisierung des ursprünglichen markierten Ladungsgitters. Diese Identifikation ist eine präzise Herkunftshypothese, keine bereits aus den P1/P2-Zahlen allein bewiesene Folgerung.",
            "holomorphy": "Aus dem geraden unimodularen E8-Gitter folgt Holomorphie; sie ist in diesem direkten Weg kein weiterer frei gewählter Selektor.",
            "CAR_route": "FE-GEN/ALG-EXH wird für die behauptete Realisierung als alter CAR/QWZ-Skalierungsgrenzwert benötigt, nicht als Voraussetzung jeder direkten Gitterquantisierung.",
            "inherited_marking_scope": "Die ursprünglichen Ladungen, Kokzyklusphasen und tatsächlich geprüften .12-Operatorwirkungen werden mitgeführt. Die A8-Erweiterungsgruppe Z3 ist nicht mit der Familienmarkierung sigma identifiziert.",
        },
        "scope": {
            "proved": "Exakte gemeinsame Gitter-, Strom- und Virasorostruktur innerhalb der ursprünglichen E8-Level-1-Quelle; der direkte Quellkandidat ist mathematisch zusammenhängend.",
            "not_identified": ["Z3-Ladungsklassen mit der Familienmarkierung sigma", "der ergänzende u1-Strom mit der P2-Hyperladung", "intrinsische konforme Zeit mit physischer Messzeit"],
            "open": ["Herkunft der minimalen Vakuumquantisierungsregel aus den ursprünglichen P1/P2-Prinzipien", "gemeinsamer physischer Transfer in 3+1 Dimensionen einschließlich Zustands- und Auslesezuordnung"],
        },
    }
    return {"data": data, "checks": checks, "sources": [
        "verification/v498_celestial_wp5b_singular_vector.py",
        "experiments/theory-contracts/compiler-current-product-20260919/PROOF.txt:43-72",
        "tfpt_explorer/current_block_geometry.py::_actual_current_source",
        "origin_theory.tex:1199-1214",
        "experiments/theory-contracts/matter-geometry-round15/PROOF.md:126-182",
        "verification/v459_seam_lattice_voa_route.py",
        "experiments/theory-contracts/source-three-route-closure-20260922/SELECTION.md",
        "https://arxiv.org/abs/hep-th/0701244",
        "https://arxiv.org/abs/1503.01260",
    ]}
