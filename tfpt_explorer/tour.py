"""Source-bound teaching layer over the live computations, not a second model.

Every displayed numerical observation comes from a named stage. Source results
not replayed by that stage remain explicitly labelled as source results.
"""
from __future__ import annotations

from math import comb

PDF = "tfpt_explorer/sources/TFPT_Konsolidierung_20260928.pdf"
BASE = "_newest2/"
CODE = BASE + "TFPT_Gesamtdokumentation_Code_Quartik_Rekursion_2026-09-26.md"
RESULTS = BASE + "TFPT_Gesamtdokumentation_Ergebnisse_und_Herleitungen_2026-09-27.md"
ALL = BASE + "TFPT_Gesamtdokumentation_20260927.md"
ALL2 = BASE + "TFPT_Gesamtdokumentation2_20260927.md"
SPACE = BASE + "TFPT_Universalraum_Gesamtdokumentation_2026-09-27.md"
SOURCE = BASE + "TFPT_Universalraum_Gesamtdokumentation_20260927.md"


def _pdf(page, claim):
    return {"path": PDF, "page": page, "claim": claim}


def _doc(path, line, claim):
    return {"path": path, "line": line, "claim": claim}


def build_tour(stages):
    from .synthesis import narrative
    by_id = {stage["id"]: stage for stage in stages}

    def value(stage_id, name):
        return next(row["value"] for row in by_id[stage_id]["outputs"] if row["name"] == name)

    def chapter(id, title, question, lead, before, action, after, contribution,
                limit, status, stage_ids, lenses, visual, sources, metrics=()):
        selected = [by_id[key] for key in stage_ids if key in by_id]
        return {"id": id, "eyebrow": "Ein gemeinsamer Prozess · mehrere notwendige Anschlüsse",
                "title": title, "question": question, "lead": lead,
                "before": before, "action": action, "after": after,
                "contribution": contribution, "limit": limit, "status": status,
                "stage_ids": [stage["id"] for stage in selected],
                "lenses": dict(zip(("geometry", "topology", "mathematics", "physics"), lenses)),
                "visual": {"type": id, "data": visual}, "sources": sources,
                "metrics": list(metrics),
                "calculation": {"stage_count": len(selected),
                                "checks": sum(len(stage["checks"]) for stage in selected),
                                "failed": sum(check["ok"] is False for stage in selected for check in stage["checks"])}}

    chapters = [chapter(
        "big_picture", "Was soll am Ende aus allem werden?", "Wie hängen der alte TFPT-Compiler und die neuen Codeprozesse zusammen?",
        "Gesucht ist eine einzige begründete Quelle, aus der Bewegung, Information, Raum und messbare Naturgesetze gemeinsam folgen. Die beiden Forschungswege treffen sich dort, wo dieselben Operationen dieselben Zustände und Antworten tragen müssen.",
        "Links steht das TFPT-Gerüst: Naht, Träger, E₈, Flavor, α und geometrische Antworten. Rechts stehen die neuen konkreten Register, Codezellen, Bindungen und Rekursionen.",
        "Wir verfolgen tatsächliche Abbildungen zwischen beiden Wegen. Eine gleiche Zahl genügt nicht: Auch die Wirkung auf einen Zustand muss zusammenpassen.",
        "Ein zusammenhängender endlicher Rechenweg mit identifizierten Anschlüssen. Mehrere physische Übergänge brauchen noch einen gemeinsamen Herkunftssatz.",
        "Die neuen Codeergebnisse sollen erklären, wie das ältere Gerüst ausgeführt wird. Der entscheidende Maßstab ist ein gemeinsamer Prozess, der alle physikalischen Antworten zugleich liefert.",
        "Die Zeichnung ist eine Landkarte des Forschungswegs. Sie ist keine zeitliche Darstellung einer bereits hergeleiteten Entstehung des Universums.", "conditional",
        ["origin", "e8", "alpha", "code", "sourcechannel", "matterbridge"],
        ["Eine geometrische Form ist hier zunächst ein Zustands- oder Beziehungsraum. Erst ein zusätzlich bewiesener Anschluss macht daraus räumliche Entfernung.",
         "Zusammenpassen heißt auch: Welche Teile sind verbunden, welche Schleifen bleiben erhalten, welche Zusammenschlüsse sind erlaubt?",
         "Kodierung, Ereigniswirkung, Ladung, Normierung und Dynamik müssen durch passende Abbildungen gemeinsam erhalten bleiben.",
         "Die Gesamtlösung würde Teilchen, Wechselwirkungen, Raumzeit und Anfangszustand aus derselben Quelle erklären und überprüfbare Vorhersagen liefern."],
        {"branches": [{"title": "TFPT-Gerüst", "steps": ["Naht + Träger", "E₈ + Quantenrand + Clocks", "Flavor + Neutrinos + α", "Gravitation + Horizonte + Kosmologie"]},
                      {"title": "Ausführbarer Prozess", "steps": ["60 Ereignisse", "Geschützter Code", "Bindung + Rekursion", "Quelle + Netz"]}],
         "meeting": "Gleiche Quelle · passende Wirkungen · gemeinsamer Anfangszustand", "destination": "Physikalische Gesamtlösung", "destination_status": "open"},
        [_pdf(2, "Gesamtergebnis und vier neue Anschlüsse"), _doc(RESULTS, 212, "Der größere TFPT-Zusammenhang"), _doc(SOURCE, 138, "Zwei verzahnte Wege")]),

        chapter("boundary", "Vier Marken — zwei verschiedene Arten zu zählen", "Warum tauchen drei und fünf auf, ohne Raumdimensionen zu sein?",
        "Stell dir eine Kugeloberfläche mit vier markierten Löchern vor. Du kannst um die Löcher herumlaufen; getrennt davon kannst du Funktionen auf dieser Oberfläche untersuchen.",
        "Die ursprüngliche TFPT verbindet die orientierte Doppelüberdeckung mit vier Marken. P1 und P2 werden innerhalb dieses Abschlussrahmens durch die folgenden Rückbedingungen mitbestimmt.",
        "Für Umläufe gibt es eine Relation: Alle vier zusammen sind abhängig. Für die angegebenen meromorphen Funktionen liefert die eigene Zählregel fünf Richtungen.",
        "Drei unabhängige Umläufe und ein anderer, fünfdimensionaler Funktionenraum. Der ursprüngliche Fünfer-Träger ist nochmals in seiner angegebenen Rolle zu lesen.",
        "Die Rückschleife läuft weiter: D₅ und A₃ verkleben mit Index vier zu E₈. Dessen Rang acht und Coxeterordnung 30=2·3·5 prüfen die ursprünglichen Zahlen zurück. Der goldene Anteil entsteht im verklebten System.",
        "Vier Marken, drei Umläufe und fünf Funktionen sind verschiedene mathematische Größen. Der diskrete Bootstrap schränkt seinen erklärten Abschlussrahmen ein; die gemeinsame Realisierung als vollständiger physischer Prozess muss diese Ergebnisse erhalten.", "conditional", ["origin", "seam", "carrier", "e8"],
        ["Die vier Punkte liegen in der gezeichneten Darstellung einer markierten Oberfläche; sie sind keine vier Teilchenorte.",
         "Vier Randumlaufklassen mit einer Relation ergeben Rang drei. Das ist eine topologische Aussage.",
         "Bei Gattung null und dem angegebenen Divisorgrad vier hat der Funktionenraum Dimension fünf. Umlaufklassen und Funktionen sind unterschiedliche Objekte.",
         "Der 3+2-markierte Träger liefert eine interne Ladungstabelle. Seine fünf Plätze sind keine fünf Raumdimensionen."],
        {"marks": by_id["seam"]["visual"]["data"]["marks"], "cycle_rank": value("seam", "homology_rank"), "function_dimension": value("seam", "rr_dimension"), "carrier_components": value("carrier", "basis_size")},
        [_pdf(11, "Vier Marken, zwei unterschiedliche Räume"), _doc("origin_theory.tex", 87, "Derselbe Vierpunktdivisor liefert Familie und Träger"), _doc("origin_theory.tex", 954, "P1/P2 als rückbestimmte Bootstrap-Daten")],
        [{"label": "Unabhängige Umläufe", "value": value("seam", "homology_rank"), "note": "Homologierang"}, {"label": "Funktionenrichtungen", "value": value("seam", "rr_dimension"), "note": "Riemann–Roch unter dem angegebenen Vertrag"}]),

        chapter("alphabet", "Ein Alphabet für mögliche Ereignisse", "Wie werden Hamming, E₈ und die 60 Richtungen zu einer konkreten Verbindung?",
        "Ein kleiner binärer Code bestimmt erlaubte Vorzeichenmuster. Daraus entstehen konkrete Vektoren; je vier Phasenvarianten können dieselbe komplexe Richtung beschreiben.",
        "Der Hammingcode enthält 16 binäre Wörter. Der ältere TFPT-Weg liefert daneben die D₅/A₃-Verklebung.",
        "Wir erzeugen die Wurzeln und die komplexen Quellenprojektoren ausdrücklich. Die 60 Richtungen definieren Reflexionen: eine Komponente wird umgedreht, die senkrechten bleiben erhalten.",
        "Ein endliches Alphabet von 60 Operatoren auf einem Register. Das ist der gemeinsame Einstieg in die Codekonstruktion.",
        "Der Anschluss an E₈ beruht auf Vektoren und Abbildungen. Dadurch kann der neue Prozess mit dem alten algebraischen Gerüst verglichen werden.",
        "Die Zeichnung projiziert hochdimensionale Vektoren in zwei Dimensionen. Ihre Bildabstände sind keine physischen Entfernungen; die komplexe Paarung ist angegeben, nicht aus dem Bild bewiesen.", "exact", ["e8", "hamming", "rays"],
        ["240 reelle Wurzeln werden in einer festgelegten komplexen Darstellung zu 60 Strahlprojektoren zusammengefasst.",
         "Orthogonalität erzeugt eine endliche Inzidenzstruktur. Diese innere Nachbarschaft ist noch kein Netz von Raumorten.",
         "Jede normierte Richtung ψ definiert die Reflexion r = I − 2|ψ⟩⟨ψ|. Der Code liefert tatsächliche Richtungen und Matrizen.",
         "Diese Operatoren sind Kandidaten für elementare Ereignisse. Wann und wo sie auftreten, ist eine weitere Auswahl."],
        {"roots": by_id["e8"]["visual"]["data"]["sample_roots"], "root_count": value("rays", "roots"), "ray_count": value("rays", "rays"), "words": value("hamming", "codewords")},
        [_doc(CODE, 310, "Hamming, E₈ und 60 Quellen"), _pdf(13, "Konkrete Reflexionen")]),

        chapter("protected_code", "Vier Register tragen einen gemeinsamen Inhalt", "Wie wird aus 256 Richtungen der geschützte Fünfer?",
        "Wie bei vier aufeinander abgestimmten Stimmen steckt die Information in ihrem Zusammenspiel. Eine gemeinsame Ereignisregel lässt einen bestimmten Teil dieses Zusammenspiels besonders beständig.",
        "Vier Register mit je vier Basisrichtungen bilden einen Raum mit 4⁴ = 256 Basisrichtungen. Beliebige Überlagerungen sind möglich.",
        "Die angegebene gemeinsame Ereignisenergie wird diagonalisiert. Ihr tiefster Energieraum wird mit dem ausdrücklich konstruierten Codeprojektor verglichen.",
        "Ein fünfdimensionaler Grundraum mit einer Energielücke zu anderen Richtungen. Ein gesondertes Mikromodell beschreibt den Weg über 35 symmetrische Richtungen.",
        "Jetzt besitzen wir einen berechenbaren Informationsträger und können fragen, welche Eingriffe ihn bewegen, welche ihn schützen und wie mehrere solche Träger koppeln.",
        "Die Energie wählt einen Grundraum, aber präpariert ihn nicht automatisch. Ereignisgesetz, Gewichte und vier Register gehören zu den Voraussetzungen. Der Weg 256→35→5 ist ein eigener Modellzweig.", "conditional", ["code"],
        ["Eine Ebene innerhalb eines größeren Raums ist das passende Bild. Fünf Basisrichtungen bedeuten unendlich viele mögliche Superpositionen.",
         "Es gibt hier noch keine räumlich topologische Speicherordnung. Die vier Register sind Tensorfaktoren, keine nachgewiesenen Raumpunkte.",
         "Der Projektor P hat Rang fünf. P = 40M₄ − S verbindet ihn mit dem vierten Quellenmoment und dem Symmetrisierer.",
         "Eine Energielücke ist ein Schutzmerkmal im gewählten Modell. Kühlung, thermische Stabilität und Ursprung der Energie sind zusätzliche Aussagen."],
        {"ambient": value("code", "ambient_dimension"), "symmetric": comb(7, 4), "code": value("code", "code_rank"), "spectrum": by_id["code"]["visual"]["data"], "gap": value("code", "parent_gap"), "intermediate_status": "separate_source_model"},
        [_doc(RESULTS, 245, "Explizite Codebasis und Normierung"), _doc(ALL2, 114, "Dynamischer Weg über 35 Richtungen"), _pdf(14, "Momentenidentität und Codeauswahl")]),

        chapter("information", "Die Anzeige zeigt nicht den ganzen Zustand", "Wie kann heute unsichtbare Information morgen sichtbar werden?",
        "Zwei Melodien können auf einem einzelnen Messgerät gleich aussehen. Nach demselben erlaubten Eingriff zeigt das Gerät plötzlich einen Unterschied. Dann war seine erste Anzeige als Zustandsbeschreibung zu klein.",
        "Ein Register sieht nur die Normierung. Die Paaransicht sieht zehn unabhängige Operatorrichtungen; der volle Fünferzustand benötigt 25.",
        "Wir ergänzen die Messungen um ihre tatsächlich durch die Kontrollen erreichbaren Folgetests und berechnen den Rang nach jedem Erweiterungsschritt.",
        "Der Abschluss 10→20→25 bewahrt alle unter diesen Kontrollen später sichtbaren Richtungen. Die ursprüngliche Paaransicht allein ist nicht autonom.",
        "Ein gemeinsamer Weltprozess darf keine Information wegwerfen, die später die Physik beeinflusst. Das ist derselbe Prüfgedanke für Quellen, Rekursion und Gedächtnis.",
        "25 bezeichnet die Dimension eines Operatorraums, nicht 25 Teilchen oder Raumrichtungen. Der Abschluss gilt für die angegebenen Kontrollen.", "exact", ["code", "observability"],
        ["Die sichtbare Projektion wächst, bis keine unter den erlaubten Operationen später sichtbare Richtung mehr fehlt.",
         "Die Zahl der Register ist keine räumliche Dimension. Hier geht es um die Verteilung von Information über Teilsysteme.",
         "Erweitere die Messeffekte wiederholt um i[H,O]. Erst ein unter allen Kontrollen abgeschlossener Messraum trägt eine sichere reduzierte Beschreibung.",
         "Ein Zustand muss alle künftigen Messantworten vorhersagen können. Eine gleiche momentane Anzeige reicht dafür nicht."],
        {"stages": by_id.get("observability", {}).get("data", {}), "readout_ranks": [1, 10, 25], "readout_rank_scope": "Quellenresultat für ein, zwei und drei Register; Abschluss wird separat gerechnet"},
        [_pdf(16, "Ein-, Zwei- und Dreiregisterauslesung"), _pdf(20, "Autonomiekriterium"), _pdf(21, "Beobachtbarkeitsabschluss 10→20→25")]),

        chapter("response", "Zwei verschiedene Arten von fünfzehn", "Woher kommt die 3+2-Struktur — und was bedeutet sie?",
        "Auf sechs internen Marken gibt es 15 Möglichkeiten, zwei zu vertauschen. Es gibt auch 15 Möglichkeiten, alle sechs zu drei Paaren zu ordnen. Die Zahlen sind gleich; die Operationen sind verschieden.",
        "Die 60 ursprünglichen Ereignisse fallen im Code in 15 Gruppen zusammen, je vier mit derselben Codewirkung.",
        "Wir unterscheiden einzelne Vertauschungen von Produkten dreier disjunkter Vertauschungen. Die letzteren liefern Rang-zwei-Antwortprojektoren im Fünfer.",
        "Zwei aktive und drei andere Richtungen: die interne 3+2-Markierung mit den angegebenen Ladungswerten.",
        "Hier liegt eine konkrete Brücke zur Ladungsorganisation des älteren Trägers. Ob dies dieselben physischen Felder und dieselbe Eichdynamik sind, wird eigens geprüft.",
        "Ein Zentralisator mit passender Lie-Algebra erzeugt noch keine lokalen Eichfelder. Die beiden 15er-Listen dürfen nicht als identische Ereignisse ausgegeben werden.", "exact", ["observables", "code", "carrier"],
        ["Die Antwort teilt einen internen Fünferraum in eine Zweier- und eine Dreiergruppe.",
         "Paarungen auf sechs Marken bilden eine Inzidenzgeometrie. Sie beschreibt zunächst verträgliche interne Operationen.",
         "Tₐᵦ vertauscht zwei Marken. M ist das Produkt dreier disjunkter T. R=(I+M)/2 hat Rang zwei; Y=−I/3+5R/6.",
         "Die interne Ladungstabelle ist berechenbar. Lokale geladene Felder, ihre Bewegung und ihre Erhaltung verlangen weitere Nachweise."],
        {"mark_count": 6, "matchings": by_id["observables"]["data"]["matchings"], "rank": value("observables", "response_rank"), "event_fibres": by_id["code"]["data"]["event_fibres"]},
        [_doc(RESULTS, 190, "Wörterbuch: T, M und R"), _doc(CODE, 780, "Steuerung, 3+2 und Grenze zur Eichphysik"), _pdf(18, "Quartik und Singularlinien")]),

        chapter("quartic", "Eine Quellenform ist nicht die ganze Welt", "Was zeigt die Igusa-Quartik tatsächlich?",
        "Die Quartik beschreibt die Zustände, die eine bestimmte einfache Präparation erzeugt. Sie ist wie die Spur eines Werkzeugs: Nicht jeder im ganzen Material erreichbare Punkt liegt auf dieser Spur.",
        "Eine Quelle z wird viermal identisch eingesetzt und in den Code projiziert.",
        "Die fünf logischen Amplituden werden in sechs Koordinaten mit Summenbedingung dargestellt. Die Igusa-Gleichung wird am erzeugten Punkt ausgewertet.",
        "Eine konkrete algebraische Quellengeometrie. Allgemeine logische Steuerung kann diese Präparationsfläche verlassen und trotzdem im Fünfercode bleiben.",
        "So wird klar, welche geometrische Form denselben Code beschreibt und welche zusätzliche Information für seine volle Zukunft mitgeführt werden muss.",
        "Die Grafik zeigt Koordinaten einer hochdimensionalen algebraischen Menge, kein Foto eines dreidimensionalen Universums. Ein kleiner Gleichungsrest bestätigt nur den berechneten Punkt.", "exact", ["quartic", "observables"],
        ["Sechs Koordinaten mit einer linearen Relation beschreiben fünf Richtungen. Die zusätzliche Quartikgleichung schränkt die Quellenpräparation weiter ein.",
         "Die 15 singulären Linien hängen mit den Antwortbereichen zusammen. Singular bedeutet hier algebraisch besonders, nicht physisch unendlich dicht.",
         "Für die Quellenabbildung gilt (Σzᵢ²)² − 4Σzᵢ⁴ = 0 und Σzᵢ=0. Das ist keine Gleichung für sämtliche dynamischen Codezustände.",
         "Quellenzustand und sichtbare Quotientenkoordinaten müssen getrennt bleiben, wenn ein erlaubter Puls verborgene Unterschiede aufdeckt."],
        {"coordinates": by_id["quartic"]["visual"]["data"]["coordinates"], "residual": value("quartic", "igusa_residual")},
        [_doc(CODE, 861, "Quartik und Grenze der Quellenmannigfaltigkeit"), _pdf(18, "Präparationsabbildung"), _pdf(19, "Expliziter Nichtautonomie-Zeuge")]),

        chapter("binding", "Aus zwei Inhalten wird eine bevorzugte Beziehung", "Warum können Zellen binden — und warum ist die Bauanleitung wichtig?",
        "Zwei Zellen können einen verschränkten gemeinsamen Zustand bevorzugen. Entscheidend ist dann ihre Beziehung. Zwei verschiedene Bewegungsregeln können dieselbe bevorzugte Zweierbeziehung besitzen.",
        "Die Dokumente enthalten die Ereignisbindung k und die Antwort-/Austauschbindung −K.",
        "Der Explorer diagonalisiert die Ereignisbindung. Gemeinsame Ereignislabels werden mit unabhängigen Labels verglichen. Die Quellen halten den anderen Bindungszweig getrennt.",
        "Ein eindeutiger Paargrundzustand im angegebenen Modell. Die Übereinstimmung des Paarzustands macht die beiden Hamiltonoperatoren nicht identisch.",
        "Bindung ist der erste echte Zusammenschluss von Informationsträgern. Nur mit einer festgelegten Bindungsregel können wir die Rekursion und ihre Ladungserhaltung prüfen.",
        "Die ursprüngliche Antwortbindung verletzt den zusätzlichen additiven Ladungstest. Die ladungskovariante Vervollständigung ist ein geänderter Zweig mit anderen Übertragungswerten.", "conditional", ["binding", "observables"],
        ["Zwei Codezellen besitzen zusammen 5×5=25 Basisrichtungen. Die bevorzugte Bindung ist ein Vektor in diesem gemeinsamen Raum.",
         "Eine gezeichnete Verbindung bezeichnet einen gewählten Wechselwirkungsterm. Die Anzahl solcher Kanten ist nicht bereits aus dem Code bestimmt.",
         "Spektrum, Lücke und Grundvektor gehören zum konkreten Operator. Gleiches Grundniveau oder gleicher Grundvektor bestimmen den übrigen Operator nicht.",
         "Die Ladung muss mit der tatsächlichen Gesamtbewegung kommutieren. Eine passende Ladungstabelle allein genügt nicht."],
        {"spectrum": by_id["binding"]["visual"]["data"]["spectrum"], "comparison": by_id["binding"]["visual"]["data"]["comparison"], "branches": ["Ereignis k", "Antwort −K", "ladungskovariantes h_cov"], "branch_comparison_scope": "Drei in den Quellen unterschiedene Operatorverträge; Live-Spektrum: k"},
        [_doc(RESULTS, 87, "Zwei Modelle mit gleichem Paar und verschiedener Fortsetzung"), _pdf(33, "Bindung und Ladung"), _pdf(34, "Kovariante Vervollständigung")]),

        chapter("recursion", "Drei Zellen können wieder eine logische Zelle tragen", "Was bleibt bei der Vergrößerung wirklich gleich?",
        "Drei miteinander gekoppelte Speicher können gemeinsam denselben logischen Befehlssatz tragen wie ein einzelner. Dazu muss die Wirkung jedes Befehls durch eine konkrete Kodierung hindurchpassen.",
        "Im Ereignisdreieck stehen 5³=125 Basisrichtungen zur Verfügung.",
        "Die Isometrie in den Fünfergrundraum und die Ereigniswirkung werden geprüft. Die gewählte Rekursionstiefe bestimmt, wie viele ursprüngliche Zellen im Baum enthalten sind.",
        "Ein wirklicher Darstellungsanschluss: fünf logische Richtungen mit derselben Ereigniswirkung. Einzelne Übertragungswerte und Schutzmerkmale ändern sich.",
        "Das ist der Ansatz für viele Skalen. Für die Gesamtlösung müssen zusätzlich die Kopplung, die Ladung und der mitgeführte Kontext bei jeder Zusammenfassung stimmen.",
        "Ereignis-, Austausch- und kovariante Pfadrekursion verwenden verschiedene Tensoren. Die 40% Igusa-Richtung sind ein berechnetes Normgewicht des angegebenen Ereignistensors, keine Materiequote; seine Deutung als eindeutiger Vierergrundzustand bleibt hier ein Quellenresultat.", "conditional", ["recursion", "binding", "quartic"],
        ["Ein Fünferraum wird isometrisch in einen 125-dimensionalen Verbund eingebettet. Das Bild 3→1 meint drei Zellen zu einer effektiven Zelle.",
         "Das hier geprüfte Ereignismodell braucht ein Dreieck. Ein späteres dreiecksfreies Netz kann diesen Block nicht einfach unverändert enthalten.",
         "Eine echte Rekursion prüft U_mikro V = V U_logisch. Eine gleiche Grundraumdimension allein würde das nicht leisten.",
         "Eine Darstellungsrekursion ist noch kein physischer Fixpunkt aller Wechselwirkungen. Neue Mehrkörperterme und Leckage müssen mitgerechnet werden."],
        {"levels": by_id["recursion"]["visual"]["data"]["levels"], "ground_dimension": value("recursion", "ground_dimension"), "ambient": value("recursion", "triangle_dimension"), "cells": value("recursion", "cells_at_depth"), "quartic_weights": by_id["recursion"]["data"]["tensor_identity"]["weights"], "tensor_identity": by_id["recursion"]["data"]["tensor_identity"], "quartic_weights_status": "Ausgeschriebener Tensor und 60/40-Zerlegung hier berechnet; Vierergrundzustands-Eindeutigkeit nicht neu bewiesen"},
        [_doc(CODE, 1346, "Austauschrekursion und Operatortransport"), _doc(RESULTS, 95, "40 Prozent des Ereignis-Viererzustands"), _pdf(36, "Drei Tensoren, verschiedene Zweige")]),

        chapter("source", "Ein Motor, verschiedene Anzeigen", "Warum legt der alte Populationstransfer noch nicht die ganze Quelle fest?",
        "Der gleiche Motor kann mehrere Anzeigen antreiben. Umgekehrt können zwei Motoren dieselbe grobe Anzeige erzeugen und sich bei einem empfindlicheren Versuch unterscheiden.",
        "Je vier der 60 Ereignisse wirken im Code gleich, auf dem ursprünglichen Viererregister jedoch verschieden.",
        "Der berechnete Registerkanal trägt denselben Populationstransfer. Ändere den Phasenparameter b: Die Populationen bleiben gleich, eine Kohärenzmessung ändert sich.",
        "Ein gemeinsamer Anschluss mit einem messbaren verbleibenden Freiheitsgrad. Die Übereinstimmung einer Anzeige identifiziert den vollständigen Quantenprozess noch nicht.",
        "Hier kann die gesuchte primitive Quelle konkret geprüft werden: Sie muss b und ihre mehrzeitigen Antworten festlegen, statt nur bekannte Populationswerte zu reproduzieren.",
        "Der bisherige gemeinsame Adapter gilt auf dem Register plus Code. Seine Normierung auf allen 256 Vierregisterrichtungen ist eine stärkere Frage im nächsten Schritt. Eine Clockordnung liefert zudem noch keine Dauer in Sekunden.", "conditional", ["sourcechannel", "rays", "clocks"],
        ["Eine Projektion kann vier verschiedene ursprüngliche Ereignisse auf dieselbe Codewirkung abbilden. Diese Faserunterschiede bleiben am Register wirksam.",
         "Ein Ereignislabel bezeichnet eine innere Operation. Es wählt noch nicht, welche äußeren Zellen gemeinsam teilnehmen.",
         "R P₄ = B R verbindet die Populationsanzeigen. Die zusätzliche Antwort ⟨X₁₂⟩ = 2b − 1/9 unterscheidet Kanäle mit derselben Anzeige.",
         "Gleiche Endkanäle garantieren keine gleichen Zwischenzeiten oder Reaktionen auf Eingriffe. Zustand, Umgebung und Gedächtnis gehören zur vollen Quelle."],
        {"series": by_id["sourcechannel"]["data"]["series"], "probe_response": by_id["sourcechannel"]["data"]["probe_x12_response"], "B": by_id["sourcechannel"]["data"]["B"], "R": by_id["sourcechannel"]["data"]["R"], "common_adapter": by_id["sourcechannel"]["data"]["common_adapter"]},
        [_doc(SOURCE, 1627, "Gemeinsame Quelle über 60 Ereignissen"), _pdf(23, "Derselbe Amplitudenadapter auf Register und Code"), _doc(SOURCE, 1333, "Zwischenzeit und Gedächtnis"), _pdf(24, "Gleiche Populationen, verschiedene Kohärenz")]),

        chapter("normalization", "Eine Quelle muss an jedem Anschluss aufgehen", "Was bedeutet der neue Fehler 10/9 — und wie wird er repariert?",
        "Eine Wahrscheinlichkeitsmaschine muss für jeden erlaubten Eingang insgesamt Gewicht eins liefern. Der bisherige Anschluss stimmt im Code; an einem anderen erlaubten Eingang liefert derselbe Ansatz zu viel.",
        "Die 60 einzelnen Vierregisterereignisse werden mit denselben Amplituden wie der normierte Codekanal kombiniert.",
        "Der vollständig antisymmetrische Einerspeicher prüft diese Fortsetzung. Danach wird die positive Gesamtnorm sektorgerecht mit ihrer inversen Quadratwurzel korrigiert.",
        "Der unveränderte Einzelereignislift scheitert mit 10/9. Die Vervollständigung in der erzeugten Operatoralgebra normiert den ganzen Raum und erhält den bereits richtigen Codeprozess.",
        "Damit wird aus zwei passenden Teilanschlüssen ein mathematisch normierter größerer Kandidat. Das ist ein echter geschlossener Anschluss, dessen physische Ausführung noch begründet werden muss.",
        "Hier wird ein gleichfaseriger Lift des Codekanals gerechnet, nicht zugleich die separate Φ_b-Registerfamilie. Die Reparatur erweitert den Befehlssatz; Wortlänge, lokale Stütze, Zeit und primitive Auswahl sind dadurch nicht automatisch gelöst.", "conditional", ["normalization", "sourcechannel", "code"],
        ["Der volle Raum enthält verschiedene Symmetriesektoren. Ein auf fünf Richtungen passender Operator kann auf einer anderen Richtung falsch normiert sein.",
         "Neue Operatorprodukte sind neue Zusammensetzungen. Ihre algebraische Existenz sagt noch nicht, an welchen räumlichen Stellen sie elementar verfügbar sind.",
         "Mit q=ΣL†L gilt B=Lq⁻¹ᐟ² auf seinem Träger; der Kern wird ergänzt. Auf dem schon normierten Code wirkt die Korrektur als Identität.",
         "Ein Sektor mit Gesamtgewicht 10/9 kann keine spurtreue Quantenentwicklung tragen. Normierung ist nötig, aber allein noch keine Herkunft des Naturgesetzes."],
        {"stages": by_id.get("normalization", {}).get("data", {})},
        [_pdf(25, "Exakter Ausschluss auf Λ⁴C⁴"), _pdf(26, "Der Wert 10/9 ist unabhängig von Faserfreiheit"), _pdf(27, "Konstruktive Normvervollständigung"), _pdf(28, "Code bleibt unverändert; Befehlssatz wächst")]),

        chapter("space", "Ein Netz ist noch keine ausgewählte Raumzeit", "Was ist innerer Zusammenhang — und was könnte äußerer Raum sein?",
        "Ein Straßenplan sagt, welche Orte direkt verbunden sind. Eine Liste aller irgendwie erreichbaren Ziele vergisst diesen Plan. Für Raum brauchen wir gerade die unmittelbaren Verbindungen und ihre Kosten.",
        "Die interne Inzidenzstruktur enthält 30 Knoten und 45 Kanten. Ihr Schleifenraum besitzt 16 Richtungen.",
        "Mit einer zusätzlichen Markierung und periodischer Konstruktion wird ein dreidimensionaler A₃-Kandidat aufgebaut. Das ist eine Auswahl innerhalb der vorhandenen Struktur.",
        "Ein konkretes periodisches Raummodell. Die einfacheren energetischen Auswahlregeln der Quellen bevorzugen dagegen Cliquen, Paare oder das leere Netz.",
        "Die Gesamtlösung muss erklären, warum die Quelle gerade unmittelbare lokale Links, ihre Raten und diesen räumlichen Grenzfall auswählt. Ein beliebiger dichter Graph wäre eine andere Welt.",
        "Die dreidimensionale Langwellen-Diffusion des markierten Kandidaten ist noch keine Lorentz-Raumzeit. Der Ausschluss dünner Grundzustandsnetze gilt für die ausdrücklich klassifizierte Modellfamilie.", "conditional", ["space"],
        ["Ein periodisches Netz kann reale Abstandskoordinaten tragen, sobald Verschiebungen und Maßstab festgelegt sind.",
         "Der endliche Graph ist zusammenhängend und dreiecksfrei. E−V+1=16 zählt Schleifen; die gewählte räumliche Darstellung verwendet davon drei Richtungen.",
         "Interner Graph, Periodengitter, Laplaceoperator und physischer Hamiltonoperator sind getrennte Objekte mit eigenen Abbildungen.",
         "Diffusion beschreibt Ausbreitung einer Verteilung. Relativistische Felder und eine gemeinsame Lichtgeschwindigkeit erfordern einen weiteren kontrollierten Grenzübergang."],
        {"graph": by_id["space"]["visual"]["data"], "nodes": value("space", "nodes"), "edges": value("space", "edges"), "loop_rank": value("space", "loop_rank"), "spatial_rank": value("space", "selected_spatial_rank"), "countermodels": ["vollständiger Graph", "getrennte Paare", "leeres Netz"], "countermodel_status": "allgemeiner Quellenbeweis für die erklärte lineare Kantenmodellklasse"},
        [_doc(RESULTS, 128, "Keine dünne zusammenhängende Grundzustandsphase"), _doc(SPACE, 655, "Raumgrenzen und markierter A₃-Kandidat"), _pdf(40, "Raumauswahl und ihre Voraussetzungen"), _pdf(41, "Periodengitter")]),

        chapter("assembly", "Der passende Dreierbaustein für das Netz", "Wie passt Rekursion in ein Netz ohne Dreiecke?",
        "Drei Orte auf einem Pfad sind ein anderer Baustein als ein Dreieck. Die neue Konsolidierung setzt deshalb eine bereits gelöste, ladungserhaltende Pfadregel ein.",
        "Das A₃-Netz ist dreiecksfrei. Die ursprüngliche Ereignis-Dreiecksrekursion passt dort nicht unverändert hinein.",
        "Die 30 Knotentypen werden durch zehn disjunkte Dreierpfade überdeckt. Auf benachbarten Standorten wechseln Träger und konjugierter Träger; die kovariante Bindung erhält ihre additive Ladung.",
        "Die 25 Restlinks erzeugen zwei logische Bindungstypen. Ergänzt man jeden Blocklink zur vollständigen positiven Neun-Port-Bindung, bleibt der gesamte logische Raum auch bei gekoppelten Blöcken exakt erhalten.",
        "Jetzt passt nicht nur der Raumbaustein: Die vervollständigte Wechselwirkung und ihre Zeitentwicklung lassen sich über Skalen exakt zusammensetzen. Die Grafik darunter zeigt die neu berechnete Verbindung.",
        "Netzmarkierung, Cover und die Neun-Port-Vervollständigung sind zusätzliche Wahlen. Das ursprüngliche Netz hat pro Blockpaar einen Restlink. Invarianz wählt weder den globalen Grundzustand noch automatisch die primitive Quelle.", "conditional", ["assembly", "space", "recursion"],
        ["Die Blätter eines Dreierpfads dürfen in benachbarten Periodenzellen liegen. Ihre ganzzahligen Verschiebungen gehören zur Konstruktion.",
         "Jeder Knotentyp kommt genau einmal vor. Das ist ein Überdeckungstest auf dem periodischen Netz, kein Hinzuerfinden fehlender Dreieckskanten.",
         "Die wirklichen Restlinks projizieren mit 49/144 beziehungsweise −7/72 plus Konstanten. Für vollständige positive Blockbindungen gilt stärker H9V=V(4I+h): keine verlorene Blockinformation, auch auf endlichen Netzen mit gemeinsam genutzten Blöcken.",
         "Die alternierende Darstellung macht Ladungserhaltung möglich. Der große entartete Gesamtgrundraum wählt noch kein eindeutiges Weltvakuum."],
        {"stages": by_id.get("assembly", {}).get("data", {})},
        [_pdf(43, "Neue periodische Pfadmontage und lokale Hamiltonfamilie"), _pdf(44, "Geänderter Bindungszweig und damalige offene Blockfortsetzung"), _doc("tfpt_explorer/composition.py", 1, "Jetzt berechnete eindeutige Komposition in der angegebenen positiven Klasse")]),

        chapter("physics", "Dieselben Zahlen müssen dieselbe Wirkung tragen", "Wie verbinden wir den neuen Prozess mit Teilchen, α und Gravitation?",
        "Zwei Schlüssel mit fünf Zacken passen nicht deshalb ins gleiche Schloss. Genauso müssen zwei fünfdimensionale Räume die tatsächlich verlangten Transformationen passend ausführen.",
        "Der ältere TFPT-Träger liefert Ladungen, Flavor- und α-Formeln. Der neue Code liefert endliche Operatoren, Kanäle und Bindungen.",
        "Ein expliziter Clockvergleich verhindert die direkte Gleichsetzung zweier Fünferräume. Für genau diese isolierten Clockwirkungen wird stattdessen ein gemeinsamer Siebenerträger konstruiert.",
        "Ein genauer teilweiser Anschluss statt einer falschen Identifikation. Die α-Gleichung wird weiterhin gerechnet; ihre physische Herkunft muss mit der tatsächlichen Quelle verbunden werden.",
        "Zur Gesamtlösung gehören dieselben Ladungen, dieselbe normierte Dynamik und ein gemeinsames Erzeugungsfunktional. Erst dann hängen die verschiedenen physikalischen Antworten zwingend zusammen.",
        "Der Siebenerträger repariert nur zwei festgelegte C₄-Wirkungen. Er erzeugt weder sieben Raumrichtungen noch ein vollständiges Standardmodell. Auch die α-Wurzel legt keine additive Vakuumenergie fest.", "open", ["matterbridge", "carrier", "flavor", "alpha", "gravity", "cosmology"],
        ["Die benötigte gemeinsame Darstellung hängt von den Symmetriewirkungen ab. Dimensionen allein bestimmen ihre Einbettung nicht.",
         "Eine innere Symmetrie und eine räumliche Verbindung sind verschiedene Strukturen; eine Verbindungsmatrix ist noch keine Eichfeldenergie.",
         "Die isolierten C₄-Multiplizitäten werden komponentenweise vereinigt. Explizite isometrische Einbettungen erreichen die minimale gemeinsame Dimension sieben.",
         "Lokale chirale Materie, Streuung und ein universell gekoppelter quantisierter Spin zwei sind eigene gemeinsame Nachweise am selben Modell."],
        {"clock_completion": by_id["matterbridge"]["data"]["clock_completion"], "intertwiner": by_id["matterbridge"]["data"]["intertwiner"], "alpha_inverse": value("alpha", "alpha_inverse"), "predictions": ["Ladungen", "Flavor", "α", "Gravitation", "Kosmologie"]},
        [_pdf(35, "Gemeinsamer minimaler Clockträger"), _pdf(48, "α und gemeinsame physische Bilanz"), _pdf(49, "Vakuumkonstante und Flavor")]),

        chapter("closure", "Wie wird daraus die gesuchte Gesamtlösung?", "Welche Verbindung muss wirklich geschlossen werden?",
        "Das gemeinsame Objekt ist ein lokaler Prozess, der Verbindungen, logischen Inhalt, Clock und Gedächtnis zugleich fortschreibt. Raum, Teilchen und Naturkonstanten müssen verschiedene beobachtbare Seiten seiner einen Dynamik sein.",
        "Wir haben ausdrückliche endliche Konstruktionen, passende Teilabbildungen und präzise Gegenbeispiele gegen mehrere Abkürzungen.",
        "Die neue Zusammensetzungsregel macht einen Teil davon konkret: Derselbe logische Inhalt kann durch geladene Blöcke und ihre vollständige Wechselwirkung hindurchwirken. Jetzt sind Quellenamplituden, Teilnehmer, Raten und Zustandsauswahl gemeinsam durch diesen Anschluss und die ältere TFPT-Physik einzuschränken.",
        "Dann müssen derselbe Prozess und dieselbe Grenzfolge die lokale Raumzeit, chirale Materie, Kopplungen und Gravitation tragen. Diese Forderungen sind unten als T1–T8 konkret aufgeschlüsselt.",
        "Das ist ein überprüfbarer Weg zur Gesamtantwort: Jede zusätzliche Auswahl wird sichtbar und muss aus derselben Quelle folgen. Ein Fehlschlag lokalisiert eine falsche Identifikation oder einen noch fehlenden Eingang.",
        "Die finite Zusammensetzung ist jetzt konstruiert. Ihre primitive Auswahl, Graphdynamik und physikalische Grenztheorie sind damit noch nicht bewiesen. Die Wenn→Dann-Kette und die zwei möglichen Gesamtarchitekturen darunter zeigen, welche Schlussfolgerungen bereits tragen.", "open", ["normalization", "assembly", "matterbridge", "alpha"],
        ["Erst der gemeinsame Prozess bestimmt, welche Zustandsgeometrie und welche räumliche Geometrie physisch gebraucht werden.",
         "Lokale Zusammensetzung und unendliche Fortsetzung müssen kompatibel bleiben. Ein einzelner endlicher Block garantiert diesen Grenzvertrag nicht.",
         "Zu prüfen sind gleichzeitig V†V=I, U_mikro V=V U_logisch, passende Ladung, dynamische Invarianz und ΣK†K=I — danach der kontrollierte gemeinsame Grenzwert.",
         "Die endgültige Probe sind gemeinsame messbare Vorhersagen derselben Theorie. Für jeden Sektor getrennt passende Zusatzmodelle reichen dafür nicht."],
        {"steps": ["Primitive Quelle begründet auswählen", "Einen vollständigen Prozess normieren", "Lokale Zusammensetzung + Zustand ableiten", "Gemeinsamen physikalischen Grenzwert zeigen", "Vorhersagen an Beobachtungen prüfen"], "statuses": ["open", "conditional", "open", "open", "open"]},
        [_pdf(51, "Gemeinsames Identifikationsproblem"), _pdf(53, "Physische Tore T1–T5"), _pdf(54, "Physische Tore T6–T8 und Gesamtstatus")]),
    ]

    gate_data = [
        ("T1", "Warum gerade diese Quelle?", "Herkunft der minimalen positiven lokalen Vakuumquantisierung aus den ursprünglichen P1/P2-Prinzipien samt Markierungen", "Direkter Original-Gitteraufbau; 24 Felder erzeugen E8, ein gemeinsames Vakuum und die vollständige Stromantwort sind konstruiert", "Die physische Herkunftsidentifikation dieser Quantisierung beweisen. Frei gewählte Einfügepositionen oder Messapparate sind keine zusätzlichen Lücken im schon festgelegten Vakuumgesetz.", ["origin", "seam", "code", "assembly"]),
        ("T2", "Trägt die Quelle die tatsächliche E₈-Randtheorie?", "Zustands-, feld- und zeitverträglicher Anschluss der ursprünglichen C/X-Felder an die physische Realisierung", "Direkte lokale E8-Level-1-Quelle; sämtliche endlichen Stromantworten ausführbar; der CAR-Skalierungsweg hat eigene FE-GEN/ALG-EXH-Verpflichtungen", "Dieselbe Niveau-1-Paarung, Klammer, Dagger- und Vakuumwirkung am physischen Rand nachweisen; die Ward-Regel legt dann alle höheren Antworten fest.", ["e8", "normalization", "matterbridge", "assembly"]),
        ("T3", "Wie entstehen lokale Bewegung und Zeit?", "Eine quellengebundene lokale unitäre 3+1D-Realisierung", "Gemeinsamer konformer Zeitgenerator aller Quellenzerlegungen; thermodynamische Dynamik, Lieb–Robinson-Schranke und Grund-/KMS-Existenz für die bereits festgelegte lokale Hamiltonklasse", "Die Quellenfelder mit Zustand und Zeitwirkung in dieselbe räumliche Theorie abbilden. Der vorhandene Existenzsatz der Hamiltonklasse allein liefert diesen Anschluss nicht.", ["sourcechannel", "assembly", "space"]),
        ("T4", "Warum genau unsere chirale Materie?", "Lokale chirale Fermionen, kompatibles Maß und kontrollierte Spiegelentkopplung", "Interne Ladungen, Halbspinorinhalt und kovariante Bindungen", "Chirale Antwort, Anomalien und Spiegellücke bei wachsendem System gemeinsam prüfen.", ["carrier", "observables", "matterbridge"]),
        ("T5", "Wird daraus relativistische Wechselwirkung?", "Ein wechselwirkender Kontinuumsgrenzwert mit Lorentzverhalten und Streuung", "Berechnete A3-Blochdispersion und räumlicher Antworttensor einschließlich Korrektor bei veränderten Raten", "Korrelatoren, Dispersion mehrerer Sektoren, Leckage und Streuung unter derselben Grenzfolge kontrollieren.", ["space", "assembly"]),
        ("T6", "Entstehen α, Flavor und Neutrinos gemeinsam?", "Gemeinsame Herkunft der Kopplungs-, Flavor- und Neutrinoantworten", "Vorhandene physische Herleitungen; tatsächliche Ladungsgewichtung, schweres Majorana-Paarwörterbuch mit Seesaw-Anschluss und vollständiger neutraler Flavor-Defektkern", "Die ursprünglichen Naht- und Higgs-/Masseneinsetzungen gemeinsam in diese berechneten Quellenkanäle übersetzen; ihre Kopplung und Normierung aus demselben Prozess herleiten.", ["alpha", "flavor", "sourcechannel"]),
        ("T7", "Trägt derselbe Prozess Gravitation?", "Quantisierter masseloser Spin zwei mit universeller konsistenter Kopplung", "Bedingte geometrische und thermodynamische Anschlüsse", "Polarisationen, Ward-Identitäten und universelle Kopplung in der gemeinsamen Langwellenantwort nachweisen.", ["gravity", "cosmology"]),
        ("T8", "Warum dieser Zustand und diese Weltgeschichte?", "Physische Zustands- und kosmologische Identifikation derselben Quelle", "Die gewählte minimale positive E8-Vakuumdarstellung bestimmt den Quellenzustand zusammen mit sämtlichen Stromkorrelationen", "Die physische Zustandsabbildung und ihre Anfangs-/Randbedingungen herleiten. Ein festes Gesetz, verlustfreie Rekodierung und ein attraktiver Mischzustand sind verschiedene Bedingungen.", ["recursion", "sourcechannel", "normalization", "assembly"]),
    ]
    gates = [{"id": id, "title": title, "status": "open", "requires": requires,
              "available": available, "next_decisive": next_decisive,
              "stage_ids": [key for key in ids if key in by_id],
              "sources": [_pdf(53 if int(id[1:]) < 6 else 54, "Vollständiger physischer Abschlussvertrag " + id)]}
             for id, title, requires, available, next_decisive, ids in gate_data]
    coverage = [
        {"path": path, "label": label, "chapters": ids, "note": note}
        for path, label, ids, note in [
            (CODE, "26.09 · Code, Quartik, Bindung und Rekursion", ["alphabet", "protected_code", "response", "quartic", "recursion"], "Früher Austauschzweig bleibt vom späteren Ereignis- und kovarianten Zweig getrennt."),
            (RESULTS, "27.09 · Ergebnisse und Herleitungen", ["binding", "recursion", "space"], "Zwei Paarmechanismen, 40%-Quellenbefund und analytische Grenzen freier Graphauswahl."),
            (ALL2, "27.09 · Gesamtdokumentation 2", ["protected_code", "binding", "physics"], "Dynamische 35→5-Auswahl und spätere Ladungskorrektur als eigene Modellverträge."),
            (ALL, "27.09 · Gesamtdokumentation", ["big_picture", "recursion", "space", "closure"], "Mehrzellenalgebra ist kein Ersatz für unmittelbare gewichtete Nachbarschaften."),
            (SPACE, "27.09 · Universalraum mit Raumkandidat", ["space", "assembly"], "Der markierte A₃-Kandidat bleibt von seiner noch offenen primitiven Auswahl getrennt."),
            (SOURCE, "27.09 · Universalraum mit gemeinsamer Quelle", ["boundary", "information", "source", "physics"], "60-Ereignisadapter, Faserinformation, Zwischenzeit und Gedächtnis; enger ursprünglicher Normvertrag."),
            (PDF, "28.09 · Neue Konsolidierung", ["information", "normalization", "assembly", "physics", "closure"], "10→20→25, 10/9-Ausschluss, algebraische Normreparatur, Pfadmontage und Siebener-Clockträger ausdrücklich aufgenommen."),
        ]
    ]
    return {**narrative(stages), "title": "Vom gemeinsamen Code zur gesuchten Weltphysik", "version": 2,
            "intro": "15 Stationen: jedes Bild erklärt Eingang, Veränderung, Ergebnis und den Beitrag zur Gesamtlösung. Die vier Blickwinkel unterscheiden Form, Verbindung, Rechnung und physische Bedeutung.",
            "chapters": chapters, "gates": gates, "coverage": coverage,
            "coverage_scope": "Alle sieben neuen Dokumente sind in den Lesepfad eingeordnet. Das ist keine Behauptung, jeden Satz und jeden historischen Versuch als eigene Funktion neu implementiert zu haben.",
            "selection_question": "Welche unabhängig begründete primitive Quelle legt Amplituden, Teilnehmermengen, Raten, Zustand und Komposition gleichzeitig fest?",
            "completion_criterion": "Dieselbe Quelle und derselbe Grenzvertrag müssen alle acht physischen Anforderungen T1–T8 zugleich erfüllen."}
