"""The original P1/P2 feedback constraints, computed as one connected object.

This is the existing TFPT bootstrap, not a new origin postulate or a
classification of all quantum processes. Sources and the scope of each loop
remain attached to the data consumed by the guided tour.
"""
from functools import lru_cache
from itertools import combinations_with_replacement

import mpmath as mp
import sympy as sp

from .core import _alpha_solution, _alpha_function, _cartan_a, _cartan_d
from .process import _check


@lru_cache(maxsize=1)
def build_origin_closure():
    marks = 4
    family = marks - 1
    carrier = marks + 1
    rank = carrier + family
    cover = carrier - family
    anchors = [list(a) for a in combinations_with_replacement(range(1, marks), family)
               if sum(a) == marks]
    index = marks
    det_d, det_a = _cartan_d(carrier).det(), _cartan_a(family).det()
    det_hull = det_d * det_a / index**2
    q_d, q_a = sp.Rational(carrier, index), sp.Rational(family, index)
    coxeter = cover * family * carrier
    gauge_dimension = family**2 - 1 + cover**2 - 1 + 1
    cascade_start = carrier * gauge_dimension
    spine = list(range(cascade_start, rank-1, -2))
    cascade = {
        "required_for_joint_selection": False,
        "spine": spine, "start": cascade_start, "end": rank,
        "root_count": cascade_start*rank//2,
        "adjoint_dimension": cascade_start*rank//2 + rank,
        "gauge_dimension": gauge_dimension,
        "scope": "Die Kaskade Dₙ=60−2n ist ein optionaler Anschluss. Sie wird nicht als notwendige Bedingung für die gemeinsame Quellenauswahl verwendet. Ihre Identifikation mit räumlicher Vergröberung wäre eine zusätzliche Abbildung von Zellen, Zeit und Energie.",
    }
    integer = {
        "marks": marks, "family": family, "carrier": carrier,
        "rank": rank, "cover": cover, "anchor": anchors[0],
        "glue_index": index, "glue_norms": [str(q_d), str(q_a)],
        "glued_determinant": int(det_hull), "coxeter_order": coxeter,
        "live_phases": int(sp.totient(coxeter)),
        "half_spinor": 2**(carrier-1),
        "occupied_components": family * 2**(carrier-1),
        "abelian_budget": carrier**2 + marks**2,
        "scope": "Vier Marken auf P¹, Clifford-Halbspinor und familienhaltiger μ₄-Gitterabschluss sind die gemeinsame Vergleichsklasse. Die Rückschleife prüft und beschränkt diese Klasse.",
    }
    s, h = sp.symbols("s h", real=True)
    even, odd = sp.Rational(2, family), sp.Rational(1, family)
    solution = sp.solve([s+h-even, s-h-odd], [s, h])
    reverse = sp.solve([s+h-odd, s-h-even], [s, h])
    pair = sp.Matrix([[solution[s], solution[h]], [solution[h], solution[s]]])
    # The lazy block is a survival/substochastic rule. It is not the
    # symmetric, normalized population matrix in the physical cusp basis.
    cusp = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]])/18
    clock = {
        "stay": str(solution[s]), "hop": str(solution[h]),
        "leak": str(1-solution[s]-solution[h]),
        "survival_block": [[str(x) for x in row] for row in pair.tolist()],
        "spectrum": ["1", str(even), str(odd)],
        "full_turn": 2*family,
        "six_step_spectrum": ["1", str(even**(2*family)), str(odd**(2*family))],
        "reverse_hop": str(reverse[h]),
        "scope": "Eindeutig unter treuer vollständiger resummierter Leiter, Z₂-Äquivarianz und nichtnegativen Raten. Dies ist die ursprüngliche lokale Transferregel; kein Satz über jedes Quanteninstrument mit diesem Populationsschatten.",
    }
    with mp.workdps(50):
        cascade["kappa_e8"] = str(mp.mpf(carrier)/(carrier+1)
            /mp.log(mp.mpf(cascade["adjoint_dimension"])/cascade_start))
        alpha, _, _ = _alpha_solution()
        c3 = 1/(cover * 2*mp.pi * 2)
        base = (mp.mpf(4)/3)*c3
        correction = integer["occupied_components"] * c3**4
        q = correction*mp.exp(-cover*alpha)
        phase = base + q*(1-q)**(-mp.mpf(carrier)/marks)
        em = {"c3": str(c3), "phi_base": str(base),
              "delta_top": str(correction), "phi0": str(base+correction),
              "q_alpha": str(q), "phi_seam_alpha": str(phase),
              "alpha": str(alpha), "alpha_inverse": str(1/alpha),
              "root_residual": float(abs(_alpha_function(alpha))),
              "formula": "α³−2c₃³α²−(4/5)·41c₃⁶·log(1/φs(α))=0",
              "scope": "Gekoppelte skalare U(1)-Fixpunktgleichung der Originaltheorie. Ihre Fortsetzung auf geladene und mehrzeitige Quellen ist ein zusätzlicher Identifikationssatz."}
    checks = [
        _check("P1/P2-Rückschleife erfüllt ihre gemeinsamen diskreten Bedingungen",
               anchors == [[1, 1, 2]] and det_hull == 1 and q_d+q_a == 2
               and carrier == max(sp.primefactors(coxeter))
               and sp.totient(coxeter) == rank
               and 2**(carrier-1) == 1+carrier+sp.binomial(carrier, 2),
               integer, "μ4 → (5,3) → E8 → (8,30) → (5,3,2)",
               "Exakte Original-Rückbedingungen aus v6, v15, v350; Vergleichsklasse bleibt angegeben"),
        _check("Originale Deckparität und treue Clock-Leiter wählen die lokale Regel",
               solution == {s: sp.Rational(1, 2), h: sp.Rational(1, 6)}
               and reverse[h] < 0
               and set(cusp.eigenvals()) == {sp.Integer(1), even, odd},
               clock, "stay=1/2, hop=1/6, leak=1/3",
               "Exakte Gleichungen aus v486/v487; vertauschte Paritätszuordnung benötigt negative Hoprate"),
        _check("φ0 und α verwenden dieselbe Rückkopplung und dieselben Budgets",
               em["root_residual"] < 1e-45
               and integer["occupied_components"] == 48
               and integer["abelian_budget"] == 41,
               em["root_residual"], "<1e-45",
               "50-stellige Lösung des vorhandenen EM-Funktionals; keine neue dynamische Auswahl behauptet"),
        _check("E8-Kaskade schließt auf dieselben Träger- und Familienbudgets",
               spine[0] == 60 and spine[-1] == 8 and len(spine) == 27
               and sp.ilcm(integer["occupied_components"], cascade_start) == cascade["root_count"]
               and sp.igcd(integer["occupied_components"], cascade_start) == gauge_dimension
               and (spine[0]+spine[-1])//2 == sum(x**5 for x in anchors[0])
               and sp.prod([12, 10, 8, 6, 4, 2]) == (2**4*sp.factorial(5))*sp.factorial(4),
               cascade, "60→8, 240 Wurzeln, 248 Generatoren, gcd(48,60)=12",
               "Originale v5-Kaskade und exakte Arithmetik; keine Gleichsetzung von Skalenindex und Raum-RG"),
    ]
    return {"data": {"integer": integer, "clock": clock, "electromagnetic": em, "cascade": cascade,
        "title": "Die Rückschleifen bestimmen den Ausgangspunkt mit",
        "lead": "P1 und P2 sind im diskreten TFPT-Abschluss keine zwei frei drehbaren Zahlen. Cover, vier Marken, Träger, Familien, E₈ und elektromagnetische Antwort müssen zugleich zusammenpassen.",
        "structural_loop": ["Orientierte Doppelüberdeckung", "Vier μ₄-Marken", "Zyklen 3 · Funktionen 5", "D₅ + A₃ · Verklebung mit Index 4", "E₈ · Rang 8 · Clock 30", "30=2·3·5 · acht lebende Phasen", "P1: c₃=1/(8π) · P2: g=5"],
        "response_loop": ["3 Familien × 16 Komponenten = 48", "φ₀=1/(6π)+48c₃⁴", "Trägernorm 5/4 · Flavor/Higgsbudget 41", "q(α)=48c₃⁴ exp(−2α)", "φs(α) und eindeutige α-Wurzel", "Rückwirkung auf dieselbe Nahtphase"],
        "process_requirements": [
            "Die vollständige Vergröberung muss die Z₄-Grade und den Spinlift mitführen, statt nur die sichtbare Z₂-Parität zu behalten.",
            "Ihr ursprünglicher Transfersektor muss beide Moden 2/3 und 1/3 samt Parität und Sechser-Clock reproduzieren.",
            "Ihre Quellenvariationen müssen denselben φ₀-/α-Schnitt und die gemeinsamen Ladungs- und Flavorantworten erzeugen.",
            "Die Identifikation von Randnetz, endlichem Compiler und rekursiver Codezelle muss an den tatsächlichen Gruppen- und Operatorwirkungen geprüft werden."],
        "sources": [
            {"path": "origin_theory.tex", "line": 954, "claim": "Explizite Korrektur: Eingaben sind Bootstrap-Fixpunkte"},
            {"path": "origin_theory.tex", "line": 87, "claim": "Derselbe Vierpunktdivisor liefert Familie 3 und Träger 5"},
            {"path": "origin_theory.tex", "line": 294, "claim": "Treue Clock-Leiter erzwingt die lokale Regel"},
            {"path": "_archive/tfpt-45/source_extracts/02_carrier_source.tex", "line": 297, "claim": "Double Cover, Exterior-Signatur und primitiver 3+2-Träger"},
            {"path": "tfpt_1_architecture_e8.tex", "line": 3789, "claim": "Gekoppelte φs-/α-Gleichung"},
            {"path": "verification/v5_e8_cascade.py", "line": 13, "claim": "Ursprüngliche Kaskade Dₙ=60−2n"},
            {"path": "tfpt_1_architecture_e8.tex", "line": 4310, "claim": "E8-Kaskade als nachgelagerte Skalenstruktur"}]},
        "checks": checks}
