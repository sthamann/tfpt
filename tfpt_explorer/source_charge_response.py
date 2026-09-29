"""Charge-resolved neutral states of the SAME original E8 source.

The weights are the original SM hypercharges, not fitted couplings. These
chiral Ward identities are not yet a four-dimensional photon polarization.
The beta coefficient below additionally assumes the stated chiral SM matter
content and one complex Higgs doublet; it is not inferred from a VOA alone.
"""

from functools import lru_cache
from itertools import combinations_with_replacement
from typing import Any

import sympy as sp

from .neutral_source_response import _native_neutral_branch


def hypercharge_vector() -> sp.Matrix:
    return sp.Matrix([-sp.Rational(1, 3)] * 3 + [sp.Rational(1, 2)] * 2 + [0] * 3)


@lru_cache(maxsize=1)
def exact_charge_response() -> dict[str, Any]:
    native = _native_neutral_branch()
    y = hypercharge_vector()
    roots = [sp.Matrix(root) / 2 for root in sorted(native["retained"])]
    charges = [(y.T * root)[0] for root in roots]
    moment = sum((q**2 * root * root.T for q, root in zip(charges, roots)), sp.zeros(8))
    stress = sp.trace(moment) / 8
    remainder = moment - stress * sp.eye(8)
    r = native["R_matrix"]
    level = (y.T * y)[0]
    relative = level / 4
    carrier = remainder - relative * r
    expected_carrier = sp.zeros(8)
    expected_carrier[:5, :5] = 6 * (y[:5, 0] * y[:5, 0].T - sp.diag(*[v**2 for v in y[:5, 0]]))
    gram = sp.Matrix([[sp.trace(r*r)/2, sp.trace(r*remainder)/2],
                      [sp.trace(r*remainder)/2, sp.trace(remainder**2)/2]])
    # Four-dimensional one-loop convention: Weyl 2/3, complex scalar 1/3.
    fermion_trace = sum(q*q for q in charges)
    higgs_trace = 2 * sp.Rational(1, 2)**2
    beta_y = sp.Rational(2, 3)*fermion_trace + sp.Rational(1, 3)*higgs_trace
    gut_index = 2*level
    c_roots = [root for root in roots if list(root[:5, 0]) == [-sp.Rational(1, 2)]*5]
    family_labels = [native["family"].index(tuple(int(2*v) for v in root[5:, 0])) for root in c_roots]
    pair_responses = []
    for a, b in combinations_with_replacement(range(len(c_roots)), 2):
        momentum = c_roots[a]+c_roots[b]
        oscillator = c_roots[a]-c_roots[b]
        base = (momentum.T*remainder*momentum)[0]/2
        oscillator_value = (sp.Integer(0) if a == b else
                            (oscillator.T*remainder*oscillator)[0]/(oscillator.T*oscillator)[0])
        eigenstate = a == b or remainder*oscillator == oscillator_value*oscillator
        pair_responses.append({"families": [family_labels[a], family_labels[b]], "momentum_response": str(base),
                               "oscillator_response": str(oscillator_value),
                               "total": str(base+oscillator_value), "eigenstate": bool(eigenstate),
                               "Y": str((y.T*momentum)[0])})
    return {"native": native, "hypercharge": y, "charges": charges,
            "moment": moment, "stress_coefficient": stress, "R_Y": remainder,
            "R": r, "relative_coefficient": relative, "carrier_remainder": carrier,
            "expected_carrier": expected_carrier, "gram": gram,
            "current_level": level, "fermion_trace": fermion_trace,
            "higgs_trace": higgs_trace, "beta_Y": beta_y, "kY": gut_index,
            "beta_1": beta_y/gut_index,
            "pair_responses": pair_responses,
            "R_JY_JY": (y.T*r*y)[0], "RY_JY_JY": (y.T*remainder*y)[0]}


def build_source_charge_response_data() -> dict[str, Any]:
    e = exact_charge_response()
    def check(name, ok, actual, expected):
        return {"name": name, "ok": bool(ok), "actual": actual, "expected": expected,
                "method": "Exact original E8 root charges and Heisenberg Wick form"}
    gram = e["gram"]
    checks = [
        check("Die ursprünglichen 48 Materiefelder behalten ihre Hyperladungen",
              e["fermion_trace"] == 10 and e["current_level"] == sp.Rational(5, 6),
              [str(e["fermion_trace"]), str(e["current_level"])], ["10", "5/6"]),
        check("Der ladungsgewichtete Rest entsteht aus denselben Wurzeln",
              e["stress_coefficient"] == sp.Rational(5, 2)
              and e["relative_coefficient"] == sp.Rational(5, 24)
              and e["carrier_remainder"] == e["expected_carrier"]
              and sp.trace(e["R_Y"]) == 0,
              [str(e["stress_coefficient"]), str(e["relative_coefficient"])], ["5/2", "5/24"]),
        check("Topologischer und ladungsgewichteter Zustand sind zwei Richtungen",
              gram == sp.Matrix([[48, 10], [10, sp.Rational(35, 3)]]) and gram.det() == 460,
              {"Gram": [[str(x) for x in row] for row in gram.tolist()], "det": str(gram.det())},
              {"Gram": [["48", "10"], ["10", "35/3"]], "det": "460"}),
        check("Die gemeinsame Quellenantwort unterscheidet Familien- und Eichstrom",
              e["R_JY_JY"] == 0 and e["RY_JY_JY"] == sp.Rational(115, 36),
              [str(e["R_JY_JY"]), str(e["RY_JY_JY"])], ["0", "115/36"]),
        check("Die bekannte 41 verwendet dieselben Ladungen und den erklärten Higgsinhalt",
              e["beta_Y"] == sp.Rational(41, 6) and e["kY"] == sp.Rational(5, 3)
              and e["beta_1"] == sp.Rational(41, 10),
              [str(e["beta_Y"]), str(e["kY"]), str(e["beta_1"])], ["41/6", "5/3", "41/10"]),
        check("Derselbe ladungsgewichtete Quellenoperator antwortet auf die Neutrinopaare",
              len(e["pair_responses"]) == 6 and all(
                  row["eigenstate"] and row["Y"] == "0" and row["total"] == "-5/3"
                  for row in e["pair_responses"]),
              [row["total"] for row in e["pair_responses"]], ["-5/3"]*6),
    ]
    data = {
        "title": "Die 48 und die 41 sind verschiedene Antworten derselben Materiefelder",
        "summary": "Die ungewichtete Familienantwort und die mit realen Hyperladungen gewichtete Antwort sind nun in derselben Quelle berechnet. Ihre zwei Richtungen bleiben unterscheidbar; die ursprünglichen Alpha- und Flavorformeln werden dadurch nicht ersetzt.",
        "charge_counts": {str(q): e["charges"].count(q) for q in sorted(set(e["charges"]))},
        "source_identities": ["B_Y=sum_beta Y(beta)^2 B_beta=(5/2)T+R_Y",
                              "R_Y=(5/24)R+S_Y", "S_Y matrix=6(yy^T-diag(y_i^2)) on D5"],
        "hypercharge": [str(x) for x in e["hypercharge"]],
        "gram": [[str(x) for x in row] for row in gram.tolist()], "gram_determinant": str(gram.det()),
        "norms": {"R": "48", "R_Y": "35/3", "S_Y": "115/12", "R_RY_inner": "10"},
        "current_ward": {"level": str(e["current_level"]), "R_JY_JY": str(e["R_JY_JY"]),
                         "RY_JY_JY": str(e["RY_JY_JY"]),
                         "denominator": "(z-w)^2(z-u)^2",
                         "scope": "Vacuum chiral three-point response with J_Y=y.h; not a 4D polarization tensor."},
        "neutrino_pair_ward": {"rows": e["pair_responses"], "coefficient": "-5/3",
                               "meaning": "R_Y acts as -5/3 times identity on the retained pair sextet. These neutral pairs still have hypercharge zero. This response does not select their relative Majorana phase."},
        "physical_beta": {"fermion_charge_trace": str(e["fermion_trace"]),
                          "higgs_charge_trace": str(e["higgs_trace"]), "bY": str(e["beta_Y"]),
                          "kY": str(e["kY"]), "b1": str(e["beta_1"]),
                          "assumptions": "Existing 4D Weyl matter identification, one complex Higgs doublet and standard one-loop convention."},
        "scope": "Exact source identities after the existing 3+2 hypercharge and three-family marking. A lossless joint state map must preserve this rank-two Gram form; this is not a theorem that the original scalar topological port must itself have rank two, and it does not fix the physical coupling or source state.",
    }
    return {"data": data, "checks": checks, "sources": [
        "tfpt_explorer/neutral_source_response.py::_native_neutral_branch",
        "verification/v2_carrier_pascal.py",
        "_archive/tfpt-45/source_extracts/02_carrier_source.tex:1729-1746",
        "_archive/tfpt-45/source_extracts/03_em_flavor_source.tex:94-120",
    ]}
