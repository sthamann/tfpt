"""Exact 16D involution type mismatch, not a no-go for larger field embeddings."""
import argparse
import ast
from collections import Counter
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/carrier-module-conjugation/checker.py": "87cd67ca2588a41aec5b1237250e45cca69f40ff7701c9a38206c6a0d29af1e7",
    "experiments/double-cover-rh-audit-2026-09-08/seam_source.py": "5012826dffdc90775f71b6b3a908dffde441f50ae1f455de5a532a3734349a1d",
    "experiments/tfpt-discovery/seam_state_derivation_probe.py": "5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def verify_pins():
    for name, digest in PINS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                "source pin: "+name)


def load(index):
    verify_pins()
    path = ROOT/list(PINS)[index]
    spec = importlib.util.spec_from_file_location("involution_source_"+str(index), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def signed_matrix(columns):
    matrix = sp.zeros(len(columns))
    for col, (row, sign) in enumerate(columns):
        matrix[row, col] = sign
    return matrix


def exact_source_prefix():
    """Retain the frozen source docstring/guards, including under parent -OO.

    The unchanged upstream module hashes __doc__ during import. Standard -OO
    imports therefore fail before construction. Compile this pinned source
    with optimize=0; do not mutate the upstream loader or its source file.
    """
    verify_pins()
    path = ROOT/list(PINS)[2]
    source = path.read_text()
    tree = ast.parse(source)
    namespace = {"__name__": "involution_original_source", "__file__": str(path)}
    exec(compile(tree, str(path), "exec", optimize=0), namespace)
    original = copy.deepcopy(next(n for n in tree.body
                                  if isinstance(n, ast.FunctionDef) and n.name == "main"))
    body = []
    for node in original.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "Aint_f"
                                              for t in node.targets):
            break
        body.append(node)
    else:
        raise ValueError("pinned source-prefix endpoint")
    last_line = body[-1].end_lineno
    body.append(ast.Return(value=ast.Call(func=ast.Name(id="locals", ctx=ast.Load()), args=[], keywords=[])))
    original.name, original.body = "involution_construct", body
    prefix = ast.fix_missing_locations(ast.Module(body=[original], type_ignores=[]))
    exec(compile(prefix, str(path), "exec", optimize=0), namespace)
    with contextlib.redirect_stdout(io.StringIO()):
        data = namespace["involution_construct"]()
    checks = namespace["CHECKS"]
    require(len(checks) == 5 and all(bool(row[1]) for row in checks), "all original prefix checks")
    data["provenance"] = {
        "source": str(path), "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "prefix_last_line": last_line,
        "prefix_sha256": hashlib.sha256("\n".join(source.splitlines()[:last_line]).encode()).hexdigest(),
        "source_checks": len(checks), "source_check_names": [row[0] for row in checks],
        "pinned_source_compilation_optimize": 0,
        "reason": "upstream import hashes __doc__; source is unmodified and its guards retained"}
    return data


def charged_data():
    carrier = load(0)
    m, d, pk, _, _, _, algebra = carrier.build()
    signed, _ = m.schrodinger_representation(d)
    rho = {x: signed_matrix(columns) for x, columns in signed.items()}
    km = lambda x: m.linear(algebra["K_columns"], x)
    c, q = d["cocycle"], d["q"]
    operators, rows = {}, []
    choices = algebra["coherent_character_choices"]
    require(choices == [0, 126, 128, 254], "all four inherited coherent phases")
    for character in choices:
        phase = {x: pk[x] ^ m.parity(character & x) for x in range(256)}
        coefficients = Counter()
        # Sum alpha_K(rho_x) rho_x^-1. This is independently checked below,
        # not assumed to yield an implementer merely because it is an average.
        for x in range(256):
            coefficients[km(x) ^ x] += (-1)**(phase[x] ^ q(x) ^ c(km(x), x))
        operator = sum((value*rho[x] for x, value in coefficients.items()), sp.zeros(16))/128
        require(operator.T == operator and operator**2 == sp.eye(16), "exact real orthogonal involution")
        require(all(operator*rho[x]*operator == (-1)**phase[x]*rho[km(x)]
                    for x in range(256)), "all 256 actual matrix intertwining cells")
        fixed = [x for x in range(256) if km(x) == x]
        adjoint_trace = sum((-1)**phase[x] for x in fixed)
        plus, minus = (sp.eye(16)+operator)/2, (sp.eye(16)-operator)/2
        require(len(fixed) == 64 and adjoint_trace == 64, "signed fixed-word trace")
        require(sp.trace(operator) == 8 and (plus.rank(), minus.rank()) == (12, 4), "12+4 involution type")
        require(adjoint_trace == sp.trace(operator)**2, "independent adjoint-trace identity")
        operators[character] = operator
        rows.append({"character": character, "trace": 8, "ranks": [12, 4],
                     "fixed_words": len(fixed), "adjoint_trace": int(adjoint_trace),
                     "matrix_intertwining_cells": 256,
                     "rho_expansion": {str(x): str(sp.Rational(value, 128))
                                       for x, value in sorted(coefficients.items()) if value}})
    diagonal = [(-1 if i in (5, 7, 9, 11) else 1) for i in range(16)]
    require(operators[0] == sp.diag(*diagonal), "explicit independent canonical K matrix")
    require(operators[0] == (rho[0]+rho[1]+rho[102]-rho[103])/2, "four-term matrix identity")
    return operators, {"dimension": 16, "algebra": "M16(R)", "rows": rows,
                       "canonical_diagonal": diagonal,
                       "source_carrier_module_equivalence_retained": True,
                       "all_possible_microscopic_phase_choices_classified": False}


def source_data():
    src = exact_source_prefix()
    a, b = sp.Matrix(src["A16_dep"]), sp.Matrix(src["A_int"])
    require(a == sp.kronecker_product(sp.eye(8), sp.Matrix([[0, 1], [-1, 0]])), "actual source A0")
    require(a**2 == -sp.eye(16) and a.det() == 1, "source A0 invertible")
    coupled = a+b/8
    require(coupled.det() != 0, "actual coupled u=1 t=1/8 source invertible")
    bare = sp.kronecker_product(sp.eye(8), sp.Matrix([[0, 1], [1, 0]]))
    require(bare*a*bare == -a and bare*b*bare != -b, "bare witness and coupled negative control")
    require(((sp.eye(16)+bare)/2).rank() == ((sp.eye(16)-bare)/2).rank() == 8, "balanced bare type")
    return a, bare, {"dimension": 16, "space": "sixteen real Majorana mode coordinates, complexified for H",
                     "A0_determinant": str(a.det()), "A0_squared": "-I16",
                     "coupled_u1_t_one_eighth_antisymmetric_determinant": str(coupled.det()),
                     "balanced_type_for_any_involution_reversing_invertible_source": [8, 8],
                     "bare_pair_swap_reverses_full_coupled_family": False,
                     "new_boundary_preserving_witness_recomputed_or_modified": False,
                     "source_provenance": src["provenance"]}


def sharp_rank_witness(operator):
    require(operator == sp.diag(*[(-1 if i in (5, 7, 9, 11) else 1) for i in range(16)]), "canonical diagonal input")
    positives = [i for i in range(16) if operator[i, i] == 1]
    negatives = [i for i in range(16) if operator[i, i] == -1]
    odd = sp.zeros(16)
    for p, n in zip(positives, negatives):
        odd[p, n] = odd[n, p] = 1
    require(operator*odd+odd*operator == sp.zeros(16), "odd rank witness")
    require(odd.rank() == 8 and len(odd.nullspace()) == 8, "sharp eight-zero-mode witness")
    return odd


def record():
    operators, charged = charged_data()
    _, _, source = source_data()
    sharp_rank_witness(operators[0])
    return {"verdict": "WHOLE_16D_K_TO_INVERTIBLE_SOURCE_REFLECTION_IDENTIFICATION_EXCLUDED",
            "pins": PINS, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "charged_sign_representation": charged, "Majorana_source": source,
            "rank_theorems": {"K_odd_operator_rank_at_most": 8, "K_odd_operator_nullity_at_least": 8,
                              "intertwiner_12plus4_to_8plus8_rank_at_most": 12},
            "scope": {"whole_16D_invertible_intertwiner_excluded": True,
                      "all_larger_or_infinite_field_embeddings_excluded": False,
                      "antiunitary_or_Bogoliubov_maps_excluded": False,
                      "microscopic_K_field_lift_proved": False,
                      "boundary_preserving_source_reflection_disproved": False,
                      "T1_T8_closed": [], "RH_proved": False}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(json.dumps(record(), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
