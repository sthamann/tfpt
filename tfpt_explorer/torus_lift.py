"""Test a simultaneous G31 lift allowing all unitary lattice characters.

The unknown generator corrections are t in (R/2Z)^40, not just sign bits.
Every repeated Cayley word supplies integer equations A t = b mod 2.
A left integer relation u A=0 with u b odd excludes even this continuous
character class.  This is a test inside the marked lattice-VOA normalizer,
not an exclusion of extensions or additional junction fields.
"""
from collections import deque
from functools import lru_cache

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import hermite_normal_form

from .cartan_source import (
    _lattice_data, _reflection_lift, _bitmask, _quadratic_mask,
    _quadratic_value,
)


def _integer_left_obstruction(rows, rhs):
    original = sp.Matrix(rows).row_join(sp.Matrix(rhs))
    # Reduce the *integer row lattice*, including the RHS. Rational row
    # reduction alone would not preserve congruences modulo two.
    row_basis = hermite_normal_form(original.T).T
    matrix = row_basis[:, :-1]
    basis_rhs = row_basis[:, -1]
    domain = DomainMatrix.from_Matrix(matrix).convert_to(sp.ZZ)
    diagonal, left, _ = smith_normal_decomp(domain)
    diagonal = diagonal.to_Matrix()
    left = left.to_Matrix()
    target = left * basis_rhs
    for row in range(matrix.rows):
        if all(diagonal[row, column] == 0 for column in range(matrix.cols)) and target[row] % 2:
            witness = left[row, :]
            return {
                "original_equation_count": len(rows),
                "integer_row_basis": [[int(v) for v in row_basis.row(i)] for i in range(row_basis.rows)],
                "coefficient_rows": matrix.rows,
                "coefficient_columns": matrix.cols,
                "left_null_relation": [int(x) for x in witness],
                "left_times_A_is_zero": witness * matrix == sp.zeros(1, matrix.cols),
                "left_times_b": int((witness * basis_rhs)[0]),
                "nonzero_relation_terms": sum(x != 0 for x in witness),
            }
    return None


@lru_cache(maxsize=4)
def build_torus_lift_data(generator_indices=(0, 13, 2, 3, 1), max_nodes=100):
    lattice = _lattice_data()
    coords = lattice["root_coordinates"]
    simple = [lattice["coordinate_index"][tuple(int(i == j) for i in range(8))]
              for j in range(8)]
    indices = tuple(generator_indices)
    variable_count = 8 * len(indices)
    generators = []
    for number, index in enumerate(indices):
        lift = _reflection_lift(index)
        permutation = bytes(lift["permutation"])
        action = np.array([coords[permutation[i]] for i in simple], dtype=np.int64).T
        linear = np.zeros((8, variable_count), dtype=np.int64)
        linear[:, 8*number:8*number+8] = np.eye(8, dtype=np.int64)
        generators.append((index, permutation, action, linear))
    identity = bytes(range(240))
    # node = permutation, integer lattice action, linear phase coefficients,
    #        constant phase on basis vectors, canonical quadratic phase, word
    first = (identity, np.eye(8, dtype=np.int64), np.zeros((8, variable_count), dtype=np.int64),
             np.zeros(8, dtype=np.int64), 0, ())
    seen, queue = {identity: first}, deque([first])
    rows, rhs, descriptions = [], [], []
    processed = 0
    obstruction = None
    while queue and processed < max_nodes:
        node = queue.popleft()
        perm, action, linear, constant, quadratic, word = node
        for index, gen_perm, gen_action, gen_linear in generators:
            new_perm = bytes(perm[gen_perm[i]] for i in range(240))
            new_action = action @ gen_action
            new_linear = gen_linear + gen_action.T @ linear
            new_constant = (gen_action.T @ constant + np.array([
                _quadratic_value(quadratic, _bitmask(tuple(gen_action[:, i])))
                for i in range(8)], dtype=np.int64)) % 2
            columns = tuple(_bitmask(tuple(new_action[:, i])) for i in range(8))
            new_quadratic = _quadratic_mask(columns, lattice["lower"])
            new_word = word + (index,)
            old = seen.get(new_perm)
            if old is None:
                new_node = (new_perm, new_action, new_linear, new_constant, new_quadratic, new_word)
                seen[new_perm] = new_node
                queue.append(new_node)
                continue
            if not np.array_equal(old[1], new_action) or old[4] != new_quadratic:
                raise ArithmeticError("Same root permutation produced different lattice action")
            for coordinate in range(8):
                row = (new_linear[coordinate] - old[2][coordinate]).tolist()
                b = int((old[3][coordinate] - new_constant[coordinate]) % 2)
                if any(row) or b:
                    rows.append(row)
                    rhs.append(b)
                    descriptions.append({"old": list(old[5]), "new": list(new_word),
                                         "basis_coordinate": coordinate})
        processed += 1
        if processed in (10, 20, 40, 70, 100) and rows:
            obstruction = _integer_left_obstruction(rows, rhs)
            if obstruction is not None:
                break
    if obstruction is None and rows:
        obstruction = _integer_left_obstruction(rows, rhs)
    result = {
        "generator_indices": list(indices),
        "character_class": f"all unitary lattice characters: t in (R/2Z)^{variable_count}",
        "processed_Cayley_nodes": processed,
        "generated_Cayley_nodes": len(seen),
        "relations": len(rows),
        "obstruction": obstruction,
        "global_section_excluded": obstruction is not None,
        "scope": "A contradictory subset excludes a section on these five generators. No contradiction in the bounded subset would not prove a global section.",
    }
    if obstruction is not None:
        terms = obstruction["left_null_relation"]
        result["witness_equations"] = [
            {"multiplier": multiplier,
             "coefficients": obstruction["integer_row_basis"][i][:-1],
             "rhs": obstruction["integer_row_basis"][i][-1]}
            for i, multiplier in enumerate(terms) if multiplier
        ]
        result["original_relations"] = [
            {"coefficients": row, "rhs": b, **description}
            for row, b, description in zip(rows, rhs, descriptions)]
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(build_torus_lift_data(), indent=2))
