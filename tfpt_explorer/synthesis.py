"""Whole-chain implications and tests of the user's Zuse comparison.

This layer constrains a candidate world process. It does not manufacture a
primitive update, select an A3 vacuum, or promote an analogy to a derivation.
"""
from functools import lru_cache
import math

import numpy as np

from .process import _invariants, _check
from .consolidation import HARMONIC_EDGES, _periodic_voltage_data

BASE = "_newest2/"
RESULTS = BASE + "TFPT_Gesamtdokumentation_Ergebnisse_und_Herleitungen_2026-09-27.md"
SOURCE = BASE + "TFPT_Universalraum_Gesamtdokumentation_20260927.md"
ALL2 = BASE + "TFPT_Gesamtdokumentation2_20260927.md"
PDF = "tfpt_explorer/sources/TFPT_Konsolidierung_20260928.pdf"
ZUSE = "https://sferics.idsia.ch/pub/juergen/zuserechnenderraum.pdf"


def doc(path, line, claim):
    return {"path": path, "line": line, "claim": claim}


def zuse(page, claim):
    return {"url": ZUSE + "#page=" + str(page), "claim": claim,
            "label": "Zuse · Originalübersetzung · PDF-Seite " + str(page)}


def bloch_laplacian(k):
    """Actual 30-site marked A3 cell in harmonic-edge gauge."""
    matrix = 3 * np.eye(30, dtype=complex)
    for (a, b), displacement in zip(_periodic_voltage_data()["graph_edges"], HARMONIC_EDGES):
        phase = np.exp(1j * np.dot(k, displacement))
        matrix[a, b] -= phase
        matrix[b, a] -= phase.conjugate()
    return matrix


@lru_cache(maxsize=1)
def physical_tests():
    inv = _invariants()
    eye = np.eye(256)
    cost = eye - inv["u_bar"]
    parent = (3 / 5) * eye - inv["u_bar"]
    code = inv["v_code"]
    shift_error = float(np.linalg.norm(cost - parent - (2 / 5) * eye))
    code_cost_error = float(np.linalg.norm(cost @ code - (2 / 5) * code))
    # Unitary reflection hypotheses establish the Dirichlet identity globally.
    reflection_error = max(float(np.linalg.norm((np.eye(4)-2*p).conj().T @
                                               (np.eye(4)-2*p)-np.eye(4)))
                           for p in inv["projectors"])
    hermitian_error = float(np.linalg.norm(inv["u_bar"] - inv["u_bar"].conj().T))
    # Two different real time laws can use the same spatial matrix. This is a
    # diagnostic of missing kinetic data, not a newly proposed physical model.
    dispersion = []
    for direction in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        unit = np.array(direction, dtype=float) / np.linalg.norm(direction)
        values = []
        for wave_number in (0.001, 0.002, 0.004):
            eigenvalue = float(np.linalg.eigvalsh(bloch_laplacian(wave_number * unit))[0])
            values.append({"k": wave_number, "lambda": eigenvalue,
                           "lambda_over_k2": eigenvalue / wave_number**2,
                           "omega_if_schrodinger": eigenvalue,
                           "omega_if_wave_equation": math.sqrt(max(0, eigenvalue))})
        dispersion.append({"direction": direction, "samples": values})
    curvature_error = max(abs(row["samples"][0]["lambda_over_k2"]-8/5) for row in dispersion)
    checks = [
        _check("Ereigniskosten enthalten 2/5 pro Codezelle", max(shift_error, code_cost_error) < 1e-12,
               {"shift": shift_error, "code_cost": code_cost_error}, 0,
               "D=I-Ubar=G4+2/5 I und DV=(2/5)V auf dem vollständigen 256-Raum"),
        _check("Dirichlet-Identität besitzt ihre nötigen Operatorvoraussetzungen",
               max(reflection_error, hermitian_error) < 1e-12,
               {"unitary_reflections": reflection_error, "hermitian_average": hermitian_error}, 0,
               "Für unitäre U gilt ||v-Uv||²=2<v,(I-Re U)v>; Mittel über die 60 vierfachen Reflexionen"),
        _check("Markiertes A3-Netz hat die angegebene räumliche Krümmung",
               curvature_error < 1e-4, curvature_error, "<1e-4",
               "30x30-Blochmatrix aller 45 harmonischen Kanten, drei Richtungen; λ/k²→8/5, kein Test eines physikalischen Zeitgesetzes"),
    ]
    return {"event_cost": {"identity": "D=I-Ubar=G4+(2/5)I", "code_value": "2/5",
                            "physical_units": "hbar/Delta_tau would be an additional scale identification",
                            "shift_error": shift_error, "code_cost_error": code_cost_error},
            "dispersion": dispersion, "checks": checks}


def augment(stages):
    from .spatial_response import build_spatial_data
    from .history_kernel import build_kernel_data
    from .marker_selection import build_marker_data
    from .origin_closure import build_origin_closure
    from .twisted_source import build_twisted_source_data
    from .origin_transfer import build_origin_transfer_data
    from .cartan_source import build_cartan_source_data, build_cartan_clock_dictionary_data
    from .deck_constraints import build_deck_constraint_data
    from .joint_constraints import build_joint_constraints_data
    from .quartic_selection import build_quartic_selection_data
    from .torus_lift import build_torus_lift_data
    from .source_process import build_source_process_data
    from .charge_selection import build_charge_selection_data
    from .current_source_bridge import build_current_source_bridge_data
    from .current_block_geometry import build_current_block_geometry_data, build_joint_charged_source_data
    from .hecke_source import build_hecke_source_data
    from .rewrite_coherence import build_rewrite_coherence_data
    from .marked_source_process import build_marked_source_process_data
    from .source_program import build_source_program_data
    from .source_unification import build_source_unification_data
    from .flavor_path_transport import build_flavor_path_transport_data
    from .neutral_source_response import build_neutral_source_response_data
    from .source_spin_lift import build_source_spin_lift_data
    from .source_majorana_pairs import build_source_majorana_pairs_data
    from .source_charge_response import build_source_charge_response_data
    from .source_flavor_correlator import build_source_flavor_correlator_data
    from .source_neutrino_dictionary import build_source_neutrino_dictionary_data
    from .source_mass_transport import build_source_mass_transport_data
    by_id = {s["id"]: s for s in stages}
    tests = physical_tests()
    by_id["code"]["data"]["event_cost"] = tests["event_cost"]
    by_id["code"]["checks"].extend(tests["checks"][:2])
    by_id["space"]["data"]["bloch_dispersion_comparison"] = tests["dispersion"]
    by_id["space"]["checks"].extend(tests["checks"][2:])
    spatial = build_spatial_data()
    by_id["space"]["data"]["weighted_spatial_response"] = spatial["data"]
    by_id["space"]["checks"].extend(spatial["checks"])
    kernel = build_kernel_data()
    by_id["sourcechannel"]["data"]["history_kernel"] = kernel["data"]
    by_id["sourcechannel"]["checks"].extend(kernel["checks"])
    marker = build_marker_data()
    by_id["space"]["data"]["native_marker_selection"] = marker["data"]
    by_id["space"]["checks"].extend(marker["checks"])
    origin = build_origin_closure()
    by_id["origin"]["data"]["origin_closure"] = origin["data"]
    by_id["origin"]["checks"].extend(origin["checks"])
    twisted = build_twisted_source_data()
    by_id["e8"]["data"]["twisted_source_bridge"] = {
        **twisted["data"], "status": twisted["status"], "scope": twisted["scope"]}
    by_id["e8"]["checks"].extend(twisted["checks"])
    by_id["e8"]["sources"].extend(twisted["sources"])
    transfer = build_origin_transfer_data()
    by_id["assembly"]["data"]["origin_transfer"] = transfer["data"]
    by_id["assembly"]["checks"].extend(transfer["checks"])
    origin["data"]["transfer"] = transfer["data"]
    cartan = build_cartan_source_data()
    by_id["e8"]["data"]["cartan_source_bridge"] = {
        **cartan["data"], "scope": cartan["scope"]}
    by_id["e8"]["checks"].extend(cartan["checks"])
    by_id["e8"]["sources"].extend(
        {"url" if source.startswith("https:") else "path": source,
         "claim": "Unverdrehter Cartan-Anschluss und geladene Liftphasen"}
        for source in cartan["sources"])
    deck = build_deck_constraint_data()
    by_id["assembly"]["data"]["deck_constraints"] = {
        key: value for key, value in deck.items() if key != "checks"}
    by_id["assembly"]["checks"].extend(deck["checks"])
    joint = build_joint_constraints_data()
    by_id["assembly"]["data"]["joint_constraints"] = joint["data"]
    by_id["assembly"]["checks"].extend(joint["checks"])
    by_id["assembly"]["sources"].extend(joint["data"]["sources"])
    quartic = build_quartic_selection_data()
    by_id["code"]["data"]["quartic_selection"] = quartic["data"]
    by_id["code"]["checks"].extend(quartic["checks"])
    by_id["code"]["sources"].extend(quartic["sources"])
    torus = build_torus_lift_data()
    by_id["e8"]["data"]["cartan_source_bridge"]["unitary_character_lift"] = {
        key: value for key, value in torus.items()
        if key not in {"original_relations", "witness_equations", "obstruction"}}
    witness = torus["obstruction"] or {}
    by_id["e8"]["checks"].append(_check(
        "Die geladene Lift-Erweiterung bleibt auch mit U(1)-Charakteren nichtgespalten",
        torus["global_section_excluded"]
        and witness.get("left_times_A_is_zero", False)
        and witness.get("left_times_b", 0) % 2 == 1,
        {key: witness.get(key) for key in (
            "original_equation_count", "coefficient_rows", "coefficient_columns",
            "left_times_A_is_zero", "left_times_b")},
        "uA=0 und ub ungerade; daher keine Lösung At=b modulo 2 auch für reelles t",
        "Exakte ganzzahlige Hermite-/Smith-Normalform aller erreichten Relationen"))
    by_id["e8"]["sources"].append(doc(
        "tfpt_explorer/torus_lift.py", 1,
        "Gleichzeitige geladene Verklebung: kontinuierliche Charakterkorrekturen"))
    source_process = build_source_process_data()
    by_id["sourcechannel"]["data"]["charged_source_process"] = {
        **source_process["data"], "scope": source_process["scope"]}
    by_id["sourcechannel"]["checks"].extend(source_process["checks"])
    by_id["sourcechannel"]["sources"].extend(
        doc(source, 1, "Fortschreibung der ursprünglichen geladenen Quellenwirkung")
        for source in ["tfpt_explorer/source_process.py", *source_process["sources"]])
    charge = build_charge_selection_data()
    by_id["sourcechannel"]["data"]["charge_selection"] = {
        **charge["data"], "scope": charge["scope"]}
    by_id["sourcechannel"]["checks"].extend(charge["checks"])
    by_id["sourcechannel"]["sources"].extend(charge["sources"])
    by_id["sourcechannel"]["sources"].append(doc(
        "tfpt_explorer/charge_selection.py", 1,
        "P2-Ladung und natives Ereignisalphabet im selben Rahmen; Label-Record-Gegenprobe"))
    current_bridge = build_current_source_bridge_data()
    by_id["e8"]["data"]["current_source_bridge"] = {
        **current_bridge["data"], "scope": current_bridge["scope"]}
    by_id["e8"]["checks"].extend(current_bridge["checks"])
    by_id["e8"]["sources"].extend(
        doc(source.split("::", 1)[0], 1,
            "Quartik-Quellenlift, Vakuum/Strom-Abbildung und Kompositionsgrenze")
        for source in current_bridge["sources"])
    current_geometry = build_current_block_geometry_data()
    by_id["assembly"]["data"]["current_block_geometry"] = current_geometry["data"]
    by_id["assembly"]["checks"].extend(current_geometry["checks"])
    joint_source = build_joint_charged_source_data()
    by_id["assembly"]["data"]["joint_charged_source"] = joint_source["data"]
    by_id["assembly"]["checks"].extend(joint_source["checks"])
    source_program = build_source_program_data()
    source_unification = build_source_unification_data()
    flavor_path = build_flavor_path_transport_data()
    neutral_response = build_neutral_source_response_data()
    source_spin_lift = build_source_spin_lift_data()
    source_majorana_pairs = build_source_majorana_pairs_data()
    source_charge = build_source_charge_response_data()
    source_correlator = build_source_flavor_correlator_data()
    neutrino_dictionary = build_source_neutrino_dictionary_data()
    mass_transport = build_source_mass_transport_data()
    for key, result in (("source_program", source_program), ("source_unification", source_unification),
                        ("flavor_path_transport", flavor_path), ("neutral_source_response", neutral_response),
                        ("source_spin_lift", source_spin_lift), ("source_majorana_pairs", source_majorana_pairs),
                        ("source_charge_response", source_charge), ("source_flavor_correlator", source_correlator),
                        ("source_neutrino_dictionary", neutrino_dictionary),
                        ("source_mass_transport", mass_transport)):
        by_id["assembly"]["data"][key] = result["data"]
        by_id["assembly"]["checks"].extend(result["checks"])
    for key, builder in (("hecke_source", build_hecke_source_data),
                         ("rewrite_coherence", build_rewrite_coherence_data),
                         ("cartan_clock", build_cartan_clock_dictionary_data),
                         ("marked_source_process", build_marked_source_process_data)):
        result = builder()
        by_id["assembly"]["data"][key] = result["data"]
        by_id["assembly"]["checks"].extend(
            {**check, "method": check.get("method", check.get("detail", "")),
             "actual": check.get("actual", "erfüllt" if check["ok"] else "nicht erfüllt")}
            for check in result["checks"])
        by_id["assembly"]["sources"].append(doc(
            "tfpt_explorer/cartan_source.py" if key == "cartan_clock" else f"tfpt_explorer/{key}.py", 1,
            "Quellengebundene Graphregeln, vollständige Wirkung und Rekursion"))
    for source in [*current_geometry["sources"], *joint_source["sources"],
                   *source_program["sources"], *source_unification["sources"],
                   *flavor_path["sources"], *neutral_response["sources"],
                   *source_spin_lift["sources"], "tfpt_explorer/source_spin_lift.py:1",
                   *source_majorana_pairs["sources"], "tfpt_explorer/source_majorana_pairs.py:1",
                   *source_charge["sources"], "tfpt_explorer/source_charge_response.py:1",
                   *source_correlator["sources"], "tfpt_explorer/source_flavor_correlator.py:1",
                   *neutrino_dictionary["sources"], "tfpt_explorer/source_neutrino_dictionary.py:1",
                   *mass_transport["sources"], "tfpt_explorer/source_mass_transport.py:1",
                   "tfpt_explorer/source_program.py:1", "tfpt_explorer/source_unification.py:1",
                   "tfpt_explorer/flavor_path_transport.py:1", "tfpt_explorer/neutral_source_response.py:1"]:
        if isinstance(source, dict):
            by_id["assembly"]["sources"].append(source)
        elif source.startswith("https://"):
            by_id["assembly"]["sources"].append({"url": source, "claim": "Gemeinsame lokale Quelle und konforme Rekonstruktion"})
        elif "arXiv:1405.2950" in source:
            by_id["assembly"]["sources"].append({
                "url": "https://arxiv.org/abs/1405.2950",
                "claim": "Stromkorrelationen, festgelegte Einfügepunkte und SU(5)-Level-1-Struktur"})
        else:
            path, _, detail = source.partition(":")
            first_line = detail.split("-", 1)[0].split(",", 1)[0].split(" ", 1)[0]
            by_id["assembly"]["sources"].append(doc(
                path, int(first_line) if first_line.isdigit() else 1,
                "Originaler Quellenkorrelator und markierte Dreierrekursion"))


def narrative(stages):
    from .kernel_narrative import build_kernel_narrative
    by_id = {s["id"]: s for s in stages}
    composition = by_id["assembly"]["data"]["composition"]
    implications = [
        {"id": "alphabet", "premise": "Dasselbe Ereignisalphabet erzeugt Code, Bindung und Rekursion.",
         "consequence": "Diese Teile müssen Wirkungen desselben Prozesses sein. Für ihre Verbindung brauchen wir passende Operatoren; gleiche Dimensionen oder dieselben Zahlen reichen nicht.",
         "status": "conditional", "sources": [doc(RESULTS, 245, "Expliziter Code und gemeinsame Ereignisse")]},
        {"id": "memory", "premise": "Heute unsichtbare Unterschiede können nach einem erlaubten Eingriff sichtbar werden.",
         "consequence": "Der Weltzustand muss alle künftig wirksamen Unterschiede behalten. Raum, Code und Gedächtnis bilden einen gemeinsamen Vorhersagezustand; eine einzelne Anzeige ersetzt ihn nicht.",
         "status": "exact", "sources": [doc(SOURCE, 399, "Abschluss unter späterer Wirkung")]},
        {"id": "source_to_charge", "premise": "Der native Encoder besitzt auf dem geladenen Pfad für jeden logischen Zustand exakt Gewicht 2/3.",
         "consequence": "Die ursprüngliche Quelle kann kontrolliert an den geladenen Pfad angeschlossen werden. Das übrige Drittel trägt ebenfalls den logischen Inhalt und muss mitgeführt oder durch eine begründete Präparation behandelt werden. Diese 2/3 ist eine Projektionswahrscheinlichkeit, keine Rate.",
         "status": "numeric", "sources": [doc("tfpt_explorer/composition.py", 1, "Hier neu berechnete G→W+R-Abbildung")]},
        {"id": "two_links", "premise": "Beim Zusammenfassen des tatsächlichen Netzes entstehen 15 gegensinnige und zehn gleichsinnige Blockverbindungen.",
         "consequence": "Die geschlossene Wechselwirkungsfamilie braucht Singulett- und Austauschbindung. Der reale Restlink und eine vollständig zusammengesetzte Blockbindung sind unterschiedliche Operatoren.",
         "status": "exact", "sources": [doc("tfpt_explorer/composition.py", 1, "Kontraktion aller 45 A3-Kanten und exakte Linkklasse")]},
        {"id": "composition", "premise": "Zwei W-Blöcke sollen durch positive Paarterme koppeln und ihren gesamten logischen Raum exakt erhalten.",
         "consequence": "In der geprüften Neun-Paar-Klasse sind die relativen Gewichte eindeutig: fünf Singulettterme und vier Austauschterme ergeben wieder dieselbe logische Bindung plus 4I. Das gilt linkweise auch für beliebige endliche Blocknetze, deren Links Blöcke teilen.",
         "status": "exact", "sources": [doc("tfpt_explorer/composition.py", 1, "Ganzzahliger Leakage-Nullraum und kollektive Kovarianz; zusätzliche Neun-Port-Regel")]},
        {"id": "time", "premise": "Die vollständige Blockbindung erhält den Kodierungsraum unter ihrem Hamiltonoperator.",
         "consequence": "Dann kommutieren Zusammenfassen und Zeitentwicklung: H9 V=V(4I+h) liefert exp(−itH9)V=exp(−4it)V exp(−ith). Damit existiert eine explizite verträgliche Dynamik über Skalen. Welche primitive Quelle diesen Generator auswählt, ist eine gemeinsame Auswahlfrage.",
         "status": "conditional", "sources": [doc("tfpt_explorer/composition.py", 1, "Dynamischer Intertwiner als Folgerung des exakten Hamiltonanschlusses")]},
        {"id": "geometry_energy", "premise": "Zahl und Stärke der Verbindungen können sich ändern oder kohärent überlagern.",
         "consequence": "Dann zählen die bisher bei fester Struktur irrelevanten Energieverschiebungen mit: 2/5 pro Ereignis-Codezelle und 4 pro vervollständigter Blockkante im jeweiligen Modell. Jede Änderung des Netzes braucht eine vollständige Energiebilanz einschließlich Gedächtnis und Quelle.",
         "status": "conditional", "sources": [doc(RESULTS, 275, "Verschobene Ereignisenergie"), doc("tfpt_explorer/composition.py", 1, "Konstante der Blockbindung")]},
        {"id": "physical_closure", "premise": "Derselbe Prozess soll Raumzeit, Teilchen, α, Flavor und Gravitation erklären.",
         "consequence": "Diese Größen müssen gemeinsam aus seinen Reaktionen auf Eingriffe folgen. Zu prüfen sind dieselben Zeitphasen, erhaltenen Ladungen und gemischten Antworten. Die ältere TFPT-Architektur wird damit zur gleichzeitigen Randbedingung an den ausführbaren Prozess.",
         "status": "conditional", "sources": [doc("tfpt_research_contracts.tex", 13620, "Gemeinsames Quellenfunktional und Antwortabschluss")]},
    ]
    candidates = [
        {"id": "A", "title": "Ein kohärenter Prozess mit veränderlichen Verbindungen", "status": "conditional",
         "idea": "Die Welt wird durch einen gemeinsamen Zustand von Verbindungen, logischem Inhalt, Clock und Gedächtnis beschrieben. Ereignisse verändern diesen Zustand lokal. Raum ist die langlebige Nachbarschaftsstruktur; Teilchen sind robuste Anregungen ihrer tatsächlichen Dynamik.",
         "derived": "Normierte endliche Quellen, vollständiger logischer Wirkungsraum, G→W-Anschluss und die exakt zusammensetzbare positive Bindung sind konkret verfügbar. Die A3-Montage stellt einen räumlichen Kandidaten bereit.",
         "requires": "Aus derselben Quelle müssen Graphübergänge, Raten und Zustand folgen. A3 muss als stabiler Sektor entstehen; die Eigenphasen der vollständigen Regel müssen relativistisch sein. Die Neun-Port-Regel ist bisher eine erklärte zusätzliche Kompositionsforderung."},
        {"id": "B", "title": "Ein festes Trägernetz mit dynamischer wirksamer Geometrie", "status": "conditional",
         "idea": "Das Trägernetz bleibt bestehen. Quantenzustände und dynamische Linkvariablen bestimmen, welche Verbindungen wirksam sind und welche Abstände Signale messen. Die rekursive Ebene trägt logische Inhalte über Skalen.",
         "derived": "Die vorhandene periodische Montage und die neue Blockkopplung passen unmittelbar in diese Klasse. Man muss nicht jeden räumlichen Unterschied als Erzeugung oder Löschung einer Zelle modellieren.",
         "requires": "Die Linkvariablen benötigen ebenfalls eine hergeleitete Update-Regel. Eine feste Nachbarschaft allein liefert keine Gravitation. Beide Varianten müssen dieselben Ladungs-, Zeit-, Zustands- und Antwortbedingungen bestehen."},
    ]
    aspects = [
        {"id": "event_energy", "title": "1 · Ereignisenergie verbindet Auswahl und Bindung",
         "claim": "Zuse erwägt Energie als Ereignisse pro Zeit und kennzeichnet dies als Spekulation.",
         "assessment": "TFPT liefert eine konkrete quadratische Änderungsform. Exakt gilt D=I−Ū₄=G₄+2/5 I. Auf dem Fünfercode ist D=2/5; dort verschwinden die Ereignisänderungen nicht.",
         "implication": "Ein gemeinsames Wirkungsprinzip ist ein sinnvoller Kandidat. Es muss zusätzlich die Zeitregel und eine Erhaltungsbilanz liefern. ℏ/Δτ ist bislang eine zusätzliche Maßstabsidentifikation.", "status": "conditional",
         "sources": [zuse(81, "Gedruckte Seite 78: Erhaltung von Ereignissen"), doc(RESULTS, 275, "Ereignisparent und konstante Verschiebung")]},
        {"id": "yield", "title": "2 · Ein Naturgesetz muss den nächsten Schritt erzeugen",
         "claim": "Zuse trennt Zustandsbedingungen von fortschreibenden Regeln.",
         "assessment": "Eine Energie und ihre Minimierer bestimmen noch keinen Updateoperator. Bei Zufallsprozessen ist die nächste Verteilung festgelegt, nicht der einzelne Ausgang. Quantummechanisch muss die Vorhersage für alle erlaubten Eingriffe geschlossen sein.",
         "implication": "Für die neue Blockregel ist dieser Anschluss konkret: Entwickeln und Kodieren vertauschen exakt. Für die primitive Quelle müssen deren tatsächliche Instrumente und Gedächtniszustände dieselbe Eigenschaft erfüllen.", "status": "conditional",
         "sources": [zuse(18, "Gedruckte Seite 15: yield form"), zuse(19, "Gedruckte Seite 16: Nebenbedingungen"), doc("tfpt_explorer/composition.py", 1, "Expliziter dynamischer Intertwiner")]},
        {"id": "levels", "title": "3 · Rekursionstiefe und Raumrichtung erfüllen verschiedene Aufgaben",
         "claim": "Zuse unterscheidet hierarchische Ebenen von Zellnachbarschaft.",
         "assessment": "Zuses Beispiel betrifft Stellenwerte und abgestimmte Übertragungen. Die Übertragung auf TFPT ist unsere Folgerung: logischer Fünfer, Dreierkodierung und A3-Ortsperioden erfüllen verschiedene Aufgaben und zählen keine gemeinsame Raumdimension.",
         "implication": "Räumliche Nachbarschaft liegt quer zur logischen Skalentiefe. Die Neun-Port-Rechnung macht deren Zusammenspiel ausdrücklich berechenbar. Eine global triviale Faserstruktur folgt daraus nicht automatisch.", "status": "conditional",
         "sources": [zuse(93, "Gedruckte Seite 90: level dimension und space dimension"), doc(ALL2, 1591, "Kovariante Pfadrekursion"), {"path": PDF, "page": 43, "claim": "Montage auf dem markierten Raumkandidaten"}]},
        {"id": "dynamic_graph", "title": "4 · Veränderliche Verbindungen gehören in den Zustand",
         "claim": "Zuse erwägt prozessabhängige Verbindungen und wachsende Automaten.",
         "assessment": "Eine Summe über Graphen stellt einen Zustandsraum bereit. Dynamik entsteht erst durch tatsächliche Übergangsblöcke F_{G′←G}. Für eine Isometrie gilt Σ_{G′}F†_{G′←G}F_{G′←H}=δ_{GH}I, einschließlich der Interferenz zwischen Eingangsgraphen.",
         "implication": "Graphbewegung, Ladung und Energiebilanz müssen dieselben Übergänge beschränken. Alternativ können dynamische Linkzustände auf einem festen Trägernetz die wirksame Geometrie verändern.", "status": "conditional",
         "sources": [zuse(66, "Gedruckte Seite 63: variable circuits und growing automaton"), doc(RESULTS, 1285, "Grenzen statischer Graphenauswahl")]},
        {"id": "particles", "title": "5 · Teilchen sind dynamische Anregungen mit erhaltenen Marken",
         "claim": "Zuse beschreibt Teilchen als wandernde wiederkehrende Muster.",
         "assessment": "F^qψ=e^{iθ}T_aψ ist ein präziser Test für besonders starre wandernde Zyklen. Er ist zu eng als notwendige Definition aller Quantenteilchen: gewöhnliche Wellenpakete können sich verbreitern und trotzdem einen stabilen Teilchensektor tragen.",
         "implication": "Am vollständigen Prozess sind langlebige lokalisierbare Anregungen, Dispersion, Ladungen und Streuung gemeinsam zu prüfen. Masse folgt erst aus einem begründeten Energie-Impuls-Zusammenhang; eine E8-Wurzel allein liefert keinen Teilchentyp.", "status": "conditional",
         "sources": [zuse(67, "Gedruckte Seite 64: digitale Teilchen"), doc("tfpt_research_contracts.tex", 13620, "Gemeinsame physikalische Antwort")]},
        {"id": "carry", "title": "6 · Eine Fusion darf ihren später wirksamen Rest nicht verlieren",
         "claim": "Zuse diskutiert einen Kapazitätsverlust von zwölf auf acht Bit.",
         "assessment": "Bei frei verfügbaren Eingängen braucht ein verlustfreier Ausgang mindestens vier zusätzliche Bit Kapazität. Allgemein gilt d_out·d_carry≥d_in. Ladungserhaltung verlangt zusätzlich passende Darstellungen; bloße Dimension genügt nicht.",
         "implication": "Ein konkreter gemeinsamer Quellenbefund liegt jetzt vor: Zwei Wörter können dieselbe Cartanwirkung besitzen und sich auf geladenen Wurzelfeldern um die D₅+A₃-Deckparität unterscheiden. Der gesamte Charakterkern lässt sich selbst mit kontinuierlichen Liftphasen nicht global entfernen. Diese Information muss in der geladenen Ereignisfortschreibung erhalten bleiben. Die physische P1-Markierung sowie der Zugriff auf kohärente Geschichten bleiben zu identifizieren.", "status": "conditional",
         "sources": [zuse(78, "Gedruckte Seite 75: Informationskapazität der Beispielreaktion"), doc(SOURCE, 399, "Spätere Unterscheidbarkeit"), doc("tfpt_explorer/cartan_source.py", 1, "Exakter geladener Deckcharakter im Liftkernel"), doc("tfpt_explorer/torus_lift.py", 1, "Auch kontinuierliche Charakterphasen entfernen den gesamten Liftkernel nicht")]},
        {"id": "causality", "title": "7 · Eine Raumdispersion ist noch keine Lichtgeschwindigkeit",
         "claim": "Zuse unterscheidet Zellübertragung und Lichtgeschwindigkeit.",
         "assessment": "Am tatsächlichen A3-Blochoperator ergibt sich λ/k²≈8/5. Setzt man H=L, folgt ω∝k². Mit einer zusätzlich gewählten Wellengleichung folgt ω²=λ und damit ω∝|k|. Der gleiche Raumoperator erlaubt also verschiedene Zeitgesetze.",
         "implication": "Die interne Clock und der Carry müssen eine lokale Zeitregel tragen, deren physikalische Eigenphasen den gemeinsamen relativistischen Grenzfall ergeben. Ein endlich tiefer lokaler Tick hat einen strikten Graphkegel; kontinuierliche lokale Hamiltondynamik verlangt eine entsprechend andere Ausbreitungsschranke.", "status": "conditional",
         "sources": [zuse(68, "Gedruckte Seite 65: verschiedene Geschwindigkeiten"), {"path": PDF, "page": 42, "claim": "Räumlicher A3-Kandidat"}, doc("tfpt_explorer/synthesis.py", 1, "Neuberechnung derselben Blochmatrix für zwei Zeitinterpretationen")]},
        {"id": "joint_rule", "title": "8 · Das gemeinsame Prinzip muss mehr als seine Einzelteile festlegen",
         "claim": "Der eingefügte Text schlägt einen gemeinsamen Ereignisprozess mit Graph und Carry vor.",
         "assessment": "Die Bedingungen werden gleichzeitig angewendet. Unabhängige Ereignislabels sind beispielsweise kein zulässiger Gegenkandidat zur bereits verlangten gemeinsamen Bindungsselektion. Umgekehrt wählt ein gemeinsamer Hilbertraum kein physisch festes Trägernetz aus. Ein positiver Transferfilter wird durch eine beliebige Normvervollständigung noch nicht zur hergeleiteten Weltregel.",
         "implication": "Die Suche richtet sich auf einen einzigen geladenen, normierten und kausalen Prozess. Raum, Skalen, Teilchen und die älteren TFPT-Antworten werden als gleichzeitig zu erfüllende Folgen desselben Prozesses behandelt.", "status": "conditional",
         "sources": [doc("tfpt_explorer/composition.py", 1, "Eine tatsächlich ausgewählte relative Kopplung in expliziter Klasse"), doc("tfpt_research_contracts.tex", 13620, "Gemeinsames Erzeugungsfunktional") ]},
    ]
    world = {
        "state": "Ein gemeinsamer Quantenzustand von Verbindungen, Code, Clock und künftig wirksamem Gedächtnis.",
        "rule": "Ein lokaler Schritt F verändert Verbindungen und Inhalt gemeinsam; nichts später Wirksames wird stillschweigend entfernt.",
        "constraints": ["Norm und Interferenz erhalten", "Ladungen passend transportieren", "Über Skalen dieselbe Wirkung behalten", "Gesamte Energie einschließlich Strukturänderungen bilanzieren", "Gemeinsame kausale und physikalische Antworten liefern"],
        "derived": "Jetzt konkret verbunden: Ereigniskosten → symmetrievervollständigte Paarbindung → W-Blöcke → Ereignisfolgen und Zeitentwicklung mit erhaltenen Interferenzphasen. Die räumliche Antwort folgt aus der vollständigen Zelle.",
        "selected": "Zusätzliche Festlegungen: Ereignisdauer und Instrument, Symmetrievervollständigung, volle Neun-Port-Bindung, Graph/Cover und Zustand. Bei gemeinsamer Dauer τ ist der Paarmaßstab bereits J=2πℏ/(5τ). Ihre gemeinsame Auswahl aus der primitiven Quelle bleibt zu lösen.",
        "composition": composition,
        "event_cost": by_id["code"]["data"].get("event_cost", {}),
        "dispersion": by_id["space"]["data"].get("bloch_dispersion_comparison", []),
    }
    return {**build_kernel_narrative(stages), "implications": implications, "candidates": candidates,
            "zuse_aspects": aspects, "world_process": world}
